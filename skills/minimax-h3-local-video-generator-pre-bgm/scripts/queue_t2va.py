import argparse
import json
import os
import secrets
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image


DEFAULT_SERVER = "http://127.0.0.1:8188"
DEFAULT_TEMPLATE = os.environ.get("MINIMAX_H3_T2VA_TEMPLATE")
DEFAULT_FL2VA_UNET = "minimax_h3_fl2va_pruned_int8_convrot.safetensors"
REQUIRED_PROMPT_FIELDS = (
    "integrated_multimodal_description:",
    "overall_soundscape:",
    "non_diegetic_music:",
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
        raise RuntimeError(f"Missing required H3 prompt fields: {missing}")
    if positions != sorted(positions):
        raise RuntimeError("H3 prompt fields are not in the required order")


def build_graph(graph, args, prompt):
    _, unet_node = find_one(graph, "UNETLoader")
    _, duration_node = find_one(graph, "PrimitiveFloat", "Duration")
    _, resolution_node = find_one(graph, "ResolutionSelector")
    _, noise_node = find_one(graph, "RandomNoise")
    _, scheduler_node = find_one(graph, "BasicScheduler")
    _, prompt_node = find_one(graph, "PrimitiveStringMultiline", "Prompt")
    _, output_node = find_one(graph, "VHS_VideoCombine")
    _, generation_node = find_one(graph, "MiniMaxH3ImageToVideo")

    if any(key.startswith("start_image") for key in generation_node.get("inputs", {})):
        raise RuntimeError("Template is not a text-only T2VA graph")

    # The legacy template metadata points at Ref2VA. Text-only character generation
    # must explicitly override it with the locally installed FL2VA checkpoint.
    unet_node["inputs"]["unet_name"] = DEFAULT_FL2VA_UNET
    duration_node["inputs"]["value"] = args.duration
    resolution_node["inputs"]["aspect_ratio"] = args.aspect_ratio
    resolution_node["inputs"]["megapixels"] = args.megapixels
    resolution_node["inputs"]["multiple"] = 32
    noise_node["inputs"]["noise_seed"] = args.seed
    scheduler_node["inputs"]["steps"] = args.steps
    prompt_node["inputs"]["value"] = prompt
    output_node["inputs"]["filename_prefix"] = args.output_prefix
    return graph


def parse_args():
    parser = argparse.ArgumentParser(
        description="Submit one MiniMax H3 T2VA job to the local ComfyUI workflow."
    )
    parser.add_argument("--prompt-file", type=Path, required=True)
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument(
        "--template-png",
        type=Path,
        default=Path(DEFAULT_TEMPLATE) if DEFAULT_TEMPLATE else None,
        required=DEFAULT_TEMPLATE is None,
        help=(
            "ComfyUI PNG containing prompt metadata. Supply this argument or set "
            "MINIMAX_H3_T2VA_TEMPLATE."
        ),
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
    prompt = args.prompt_file.read_text(encoding="utf-8").strip()
    validate_prompt(prompt)
    graph = build_graph(load_graph(args.template_png), args, prompt)

    summary = {
        "mode": "T2VA",
        "conditioning": "text-only",
        "unet_name": DEFAULT_FL2VA_UNET,
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
            "client_id": f"codex-h3-t2va-{secrets.token_hex(8)}",
        },
    )
    if result.get("node_errors"):
        raise RuntimeError(json.dumps(result["node_errors"], ensure_ascii=False))
    print(json.dumps({**summary, **result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
