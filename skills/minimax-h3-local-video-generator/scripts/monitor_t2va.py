import argparse
import json
import urllib.request
from pathlib import Path


def request_json(server, path):
    with urllib.request.urlopen(server.rstrip("/") + path, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_args():
    parser = argparse.ArgumentParser(
        description="Inspect one local ComfyUI prompt without blocking."
    )
    parser.add_argument("prompt_id")
    parser.add_argument("--server", default="http://127.0.0.1:8188")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--prefix")
    return parser.parse_args()


def main():
    args = parse_args()
    queue = request_json(args.server, "/queue")
    history = request_json(args.server, f"/history/{args.prompt_id}")
    running_ids = [entry[1] for entry in queue.get("queue_running", [])]
    pending_ids = [entry[1] for entry in queue.get("queue_pending", [])]

    if args.prompt_id in history:
        state = "complete"
    elif args.prompt_id in running_ids:
        state = "running"
    elif args.prompt_id in pending_ids:
        state = "pending"
    else:
        state = "unknown"

    files = []
    if args.output_dir and args.output_dir.exists():
        pattern = f"{args.prefix}*" if args.prefix else "*"
        files = [
            {
                "path": str(path.resolve()),
                "bytes": path.stat().st_size,
                "modified": path.stat().st_mtime,
            }
            for path in sorted(args.output_dir.glob(pattern))
            if path.is_file()
        ]

    result = {
        "prompt_id": args.prompt_id,
        "state": state,
        "running_count": len(running_ids),
        "pending_count": len(pending_ids),
        "history": history.get(args.prompt_id),
        "files": files,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
