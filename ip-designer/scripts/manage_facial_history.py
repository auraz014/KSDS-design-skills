#!/usr/bin/env python3
"""Read and update the rolling facial-signature history."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_PATH = Path(__file__).resolve().parents[1] / "state" / "facial-usage-history.json"
SIGNATURE_FIELDS = (
    "eye_family_id",
    "eye_scale_spacing",
    "facial_zone_id",
    "brow_eye_relation",
    "nose_muzzle_id",
    "mouth_family_id",
    "expression",
)


def empty_history() -> dict:
    return {"schema_version": "1.0", "max_entries": 8, "entries": []}


def load_history(path: Path) -> dict:
    if not path.exists():
        return empty_history()
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0":
        raise ValueError("unsupported facial history schema_version")
    if not isinstance(data.get("max_entries"), int) or data["max_entries"] < 1:
        raise ValueError("max_entries must be a positive integer")
    if not isinstance(data.get("entries"), list):
        raise ValueError("entries must be an array")
    return data


def write_history(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary_path = Path(handle.name)
    os.replace(temporary_path, path)


def build_signature_key(entry: dict) -> str:
    return "|".join(entry[field].strip() for field in SIGNATURE_FIELDS)


def summarize(data: dict) -> dict:
    entries = data["entries"]
    eye_system_counts = Counter(entry["eye_system"] for entry in entries)
    eye_family_counts = Counter(entry["eye_family_id"] for entry in entries)
    nose_muzzle_counts = Counter(entry["nose_muzzle_id"] for entry in entries)
    mouth_family_counts = Counter(entry["mouth_family_id"] for entry in entries)
    nose_mouth_pair_counts = Counter(
        f"{entry['nose_muzzle_id']}+{entry['mouth_family_id']}" for entry in entries
    )
    latest_batch = entries[-1]["batch_id"] if entries else None
    previous_batch_signatures = [
        entry["signature_key"]
        for entry in entries
        if latest_batch is not None and entry["batch_id"] == latest_batch
    ]
    most_used_eye_ids = [
        eye_id
        for eye_id, _ in sorted(
            eye_family_counts.items(), key=lambda item: (-item[1], item[0])
        )[:2]
    ]
    most_used_nose_mouth_pairs = [
        pair
        for pair, _ in sorted(
            nose_mouth_pair_counts.items(), key=lambda item: (-item[1], item[0])
        )[:2]
    ]
    return {
        "entry_count": len(entries),
        "max_entries": data["max_entries"],
        "eye_system_counts": dict(eye_system_counts),
        "eye_family_counts": dict(eye_family_counts),
        "nose_muzzle_counts": dict(nose_muzzle_counts),
        "mouth_family_counts": dict(mouth_family_counts),
        "nose_mouth_pair_counts": dict(nose_mouth_pair_counts),
        "most_used_eye_ids": most_used_eye_ids,
        "most_used_nose_mouth_pairs": most_used_nose_mouth_pairs,
        "previous_batch_id": latest_batch,
        "previous_batch_signatures": previous_batch_signatures,
    }


def append_entry(args: argparse.Namespace, path: Path) -> dict:
    data = load_history(path)
    entry = {
        "accepted_at": args.accepted_at
        or datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "batch_id": args.batch_id,
        "archetype": args.archetype,
        "eye_system": args.eye_system,
        "eye_family_id": args.eye_family_id,
        "eye_scale_spacing": args.eye_scale_spacing,
        "facial_zone_id": args.facial_zone_id,
        "brow_eye_relation": args.brow_eye_relation,
        "nose_muzzle_id": args.nose_muzzle_id,
        "mouth_family_id": args.mouth_family_id,
        "expression": args.expression,
    }
    entry["signature_key"] = build_signature_key(entry)
    data["entries"].append(entry)
    data["entries"] = data["entries"][-data["max_entries"] :]
    write_history(path, data)
    return entry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("summary")

    append_parser = subparsers.add_parser("append")
    append_parser.add_argument("--accepted-at")
    append_parser.add_argument("--batch-id", required=True)
    append_parser.add_argument("--archetype", required=True)
    append_parser.add_argument(
        "--eye-system", choices=("no_sclera", "graphic_sclera"), required=True
    )
    append_parser.add_argument("--eye-family-id", required=True)
    append_parser.add_argument("--eye-scale-spacing", required=True)
    append_parser.add_argument("--facial-zone-id", required=True)
    append_parser.add_argument("--brow-eye-relation", required=True)
    append_parser.add_argument("--nose-muzzle-id", required=True)
    append_parser.add_argument("--mouth-family-id", required=True)
    append_parser.add_argument("--expression", required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    path = args.path.resolve()
    if args.command == "summary":
        result = summarize(load_history(path))
    else:
        result = append_entry(args, path)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
