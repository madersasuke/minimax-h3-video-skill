import argparse
import hashlib
import json
import os
import secrets
import shutil
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image


DEFAULT_SERVER = "http://127.0.0.1:8188"
DEFAULT_TEMPLATE = os.environ.get("MINIMAX_H3_REF2VA_TEMPLATE")
DEFAULT_INPUT_DIR = os.environ.get("COMFYUI_INPUT_DIR")
DEFAULT_REF2VA_UNET = "minimax_h3_ref2va_int8_convrot.safetensors"
REQUIRED_PROMPT_FIELDS = (
    "subject_definitions:",
    "summary:",
    "retention_analysis:",
    "detailed_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
)
AUDIO_EXTENSIONS = {".wav", ".mp3", ".flac", ".m4a", ".aac", ".ogg"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
REFERENCE_INPUT_PREFIXES = (
    "ref_images.",
    "ref_videos.",
    "ref_video_audios.",
    "ref_audios.",
)


def request_json(server, path, *, method="GET", payload=None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        server.rstrip("/") + path,
        data=body,
        method=method,
        headers={"Content-Type": "application/json"} if body is not None else {},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {error.code} for {path}: {detail}") from error


def load_graph(template_png):
    with Image.open(template_png) as image:
        encoded = image.info.get("prompt")
    if not encoded:
        raise RuntimeError(f"No ComfyUI prompt metadata in {template_png}")
    return json.loads(encoded)


def find_one(graph, class_type, title_contains=None):
    matches = []
    for node_id, node in graph.items():
        if node.get("class_type") != class_type:
            continue
        title = node.get("_meta", {}).get("title", "")
        if title_contains and title_contains.lower() not in title.lower():
            continue
        matches.append((node_id, node))
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected one {class_type} node, found {len(matches)}: "
            f"{[node_id for node_id, _ in matches]}"
        )
    return matches[0]


def validate_prompt(prompt):
    positions = [prompt.find(field) for field in REQUIRED_PROMPT_FIELDS]
    if any(position < 0 for position in positions):
        missing = [
            field for field, position in zip(REQUIRED_PROMPT_FIELDS, positions) if position < 0
        ]
        raise RuntimeError(f"Missing required Ref2VA prompt fields: {missing}")
    if positions != sorted(positions):
        raise RuntimeError("Ref2VA prompt fields are not in the required order")
    if "<Audio 1>" not in prompt:
        raise RuntimeError("Audio-reference prompt must define and use <Audio 1>")


def validate_asset(path, extensions, label):
    path = path.resolve()
    if not path.is_file():
        raise RuntimeError(f"{label} does not exist: {path}")
    if path.suffix.lower() not in extensions:
        raise RuntimeError(
            f"Unsupported {label} extension {path.suffix}; expected {sorted(extensions)}"
        )
    return path


def staged_name(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    safe_stem = "".join(
        character if character.isalnum() or character in "-_" else "_"
        for character in path.stem
    ).strip("_") or "reference"
    return f"codex_h3_{safe_stem}_{digest}{path.suffix.lower()}"


def stage_asset(path, input_dir, *, dry_run):
    filename = staged_name(path)
    target = input_dir / filename
    if not dry_run:
        input_dir.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            shutil.copy2(path, target)
    return filename, target


def next_node_id(graph):
    numeric_ids = [int(node_id) for node_id in graph if str(node_id).isdigit()]
    return str(max(numeric_ids, default=0) + 1)


def remove_template_references(graph, generation_node):
    removable_source_ids = set()
    for key in list(generation_node.get("inputs", {})):
        if not key.startswith(REFERENCE_INPUT_PREFIXES):
            continue
        link = generation_node["inputs"].pop(key)
        if isinstance(link, list) and link:
            removable_source_ids.add(str(link[0]))
    for node_id in removable_source_ids:
        node = graph.get(node_id, {})
        if node.get("class_type") in {"LoadAudio", "LoadImage", "VHS_LoadVideo"}:
            graph.pop(node_id, None)


def add_load_audio(graph, generation_node, filename):
    node_id = next_node_id(graph)
    graph[node_id] = {
        "inputs": {"audio": filename},
        "class_type": "LoadAudio",
        "_meta": {"title": "Audio Reference (BGM)"},
    }
    generation_node["inputs"]["ref_audios.ref_audio_0"] = [node_id, 0]
    return node_id


def add_load_images(graph, generation_node, filenames):
    node_ids = []
    for index, filename in enumerate(filenames):
        node_id = next_node_id(graph)
        graph[node_id] = {
            "inputs": {"image": filename},
            "class_type": "LoadImage",
            "_meta": {"title": f"Character Reference {index + 1}"},
        }
        generation_node["inputs"][f"ref_images.ref_image_{index}"] = [node_id, 0]
        node_ids.append(node_id)
    return node_ids


def build_graph(graph, args, prompt, audio_filename, character_filenames):
    _, unet_node = find_one(graph, "UNETLoader")
    _, duration_node = find_one(graph, "PrimitiveFloat", "Duration")
    _, resolution_node = find_one(graph, "ResolutionSelector")
    _, noise_node = find_one(graph, "RandomNoise")
    _, scheduler_node = find_one(graph, "BasicScheduler")
    _, prompt_node = find_one(graph, "PrimitiveStringMultiline", "Prompt")
    _, output_node = find_one(graph, "VHS_VideoCombine")
    _, generation_node = find_one(graph, "MiniMaxH3ReferenceToVideo")

    remove_template_references(graph, generation_node)
    audio_node_id = add_load_audio(graph, generation_node, audio_filename)
    character_node_ids = add_load_images(graph, generation_node, character_filenames)

    unet_node["inputs"]["unet_name"] = DEFAULT_REF2VA_UNET
    duration_node["inputs"]["value"] = args.duration
    resolution_node["inputs"]["aspect_ratio"] = args.aspect_ratio
    resolution_node["inputs"]["megapixels"] = args.megapixels
    resolution_node["inputs"]["multiple"] = 32
    noise_node["inputs"]["noise_seed"] = args.seed
    scheduler_node["inputs"]["steps"] = args.steps
    prompt_node["inputs"]["value"] = prompt
    output_node["inputs"]["filename_prefix"] = args.output_prefix
    return graph, audio_node_id, character_node_ids


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Submit one MiniMax H3 Ref2VA job with an uploaded BGM connected to "
            "ref_audios.ref_audio_0."
        )
    )
    parser.add_argument("--prompt-file", type=Path, required=True)
    parser.add_argument("--audio-reference", type=Path, required=True)
    parser.add_argument("--audio-style-guide", choices=("yes", "no"), required=True)
    parser.add_argument("--character-reference", type=Path, action="append", default=[])
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument(
        "--template-png",
        type=Path,
        default=Path(DEFAULT_TEMPLATE) if DEFAULT_TEMPLATE else None,
        required=DEFAULT_TEMPLATE is None,
        help=(
            "ComfyUI PNG containing prompt metadata. Supply this argument or set "
            "MINIMAX_H3_REF2VA_TEMPLATE."
        ),
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path(DEFAULT_INPUT_DIR) if DEFAULT_INPUT_DIR else None,
        required=DEFAULT_INPUT_DIR is None,
        help="ComfyUI input directory. Supply this argument or set COMFYUI_INPUT_DIR.",
    )
    parser.add_argument("--server", default=DEFAULT_SERVER)
    parser.add_argument("--duration", type=float, default=15.0)
    parser.add_argument("--aspect-ratio", default="16:9 (Widescreen)")
    parser.add_argument("--megapixels", type=float, default=0.8)
    parser.add_argument("--steps", type=int, default=10)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--allow-nonempty-queue", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.seed is None:
        args.seed = secrets.randbelow(1_000_000_000_000_000)

    audio_path = validate_asset(args.audio_reference, AUDIO_EXTENSIONS, "audio reference")
    character_paths = [
        validate_asset(path, IMAGE_EXTENSIONS, "character reference")
        for path in args.character_reference
    ]
    prompt = args.prompt_file.read_text(encoding="utf-8").strip()
    validate_prompt(prompt)

    audio_filename, audio_target = stage_asset(
        audio_path, args.input_dir, dry_run=args.dry_run
    )
    character_staging = [
        stage_asset(path, args.input_dir, dry_run=args.dry_run)
        for path in character_paths
    ]
    character_filenames = [filename for filename, _ in character_staging]

    graph, audio_node_id, character_node_ids = build_graph(
        load_graph(args.template_png),
        args,
        prompt,
        audio_filename,
        character_filenames,
    )

    summary = {
        "mode": "Ref2VA",
        "conditioning": "audio-reference"
        + ("+character-reference" if character_paths else ""),
        "unet_name": DEFAULT_REF2VA_UNET,
        "audio_style_guide": args.audio_style_guide,
        "audio_source": str(audio_path),
        "audio_input": str(audio_target),
        "audio_node": audio_node_id,
        "audio_input_port": "ref_audios.ref_audio_0",
        "character_sources": [str(path) for path in character_paths],
        "character_inputs": [str(target) for _, target in character_staging],
        "character_nodes": character_node_ids,
        "duration": args.duration,
        "aspect_ratio": args.aspect_ratio,
        "megapixels": args.megapixels,
        "steps": args.steps,
        "seed": args.seed,
        "output_prefix": args.output_prefix,
    }
    if args.dry_run:
        print(json.dumps({"dry_run": True, **summary}, ensure_ascii=False, indent=2))
        return

    queue = request_json(args.server, "/queue")
    if not args.allow_nonempty_queue and (
        queue.get("queue_running") or queue.get("queue_pending")
    ):
        raise RuntimeError("ComfyUI queue is not empty; refusing duplicate submission")

    result = request_json(
        args.server,
        "/prompt",
        method="POST",
        payload={
            "prompt": graph,
            "client_id": f"codex-h3-ref2va-{secrets.token_hex(8)}",
        },
    )
    if result.get("node_errors"):
        raise RuntimeError(json.dumps(result["node_errors"], ensure_ascii=False))
    print(json.dumps({**summary, **result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
