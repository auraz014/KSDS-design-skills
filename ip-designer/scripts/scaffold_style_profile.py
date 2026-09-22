#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

RULE_KEYS = [
    "visual_language", "shape", "proportion", "silhouette",
    "face_expression", "color", "material_rendering", "detail",
    "commercial_application", "avoid"
]


def main():
    parser = argparse.ArgumentParser(description="Create a blank IP Style Engine profile.")
    parser.add_argument("style_id")
    parser.add_argument("name")
    parser.add_argument("--category", default="")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.style_id):
        parser.error("style_id must contain lowercase letters, digits, and hyphens")

    output = args.output or Path(f"{args.style_id}.json")
    if output.exists():
        parser.error(f"refusing to overwrite existing file: {output}")

    profile = {
        "schema_version": "1.0",
        "style_id": args.style_id,
        "name": args.name,
        "category": args.category,
        "version": "0.1.0",
        "status": "draft",
        "source_summary": {
            "reference_count": 0,
            "analysis_date": None,
            "notes": ""
        },
        "rules": {key: [] for key in RULE_KEYS},
        "prompt_template": {
            "required_slots": [],
            "ordering": [],
            "negative_constraints": []
        }
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

