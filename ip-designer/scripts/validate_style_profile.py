#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

RULE_KEYS = [
    "visual_language",
    "shape",
    "proportion",
    "silhouette",
    "face_expression",
    "color",
    "material_rendering",
    "detail",
    "commercial_application",
    "avoid",
]
STRENGTHS = {"dominant", "supporting", "optional", "avoid"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def fail(errors):
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


def main():
    parser = argparse.ArgumentParser(description="Validate an IP Style Engine profile.")
    parser.add_argument("profile", type=Path)
    parser.add_argument("--require-published", action="store_true")
    args = parser.parse_args()

    try:
        data = json.loads(args.profile.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail([f"Cannot read valid JSON: {exc}"])

    errors = []
    for key in ("schema_version", "style_id", "name", "category", "version", "status",
                "source_summary", "rules", "prompt_template"):
        if key not in data:
            errors.append(f"Missing top-level field: {key}")

    if not ID_RE.match(str(data.get("style_id", ""))):
        errors.append("style_id must use lowercase letters, digits, and hyphens")
    if not SEMVER_RE.match(str(data.get("version", ""))):
        errors.append("version must be semantic version x.y.z")
    if data.get("status") not in {"draft", "published", "archived"}:
        errors.append("status must be draft, published, or archived")
    if args.require_published and data.get("status") != "published":
        errors.append("profile is not published")

    rules = data.get("rules", {})
    seen = set()
    for category in RULE_KEYS:
        items = rules.get(category)
        if not isinstance(items, list):
            errors.append(f"rules.{category} must be an array")
            continue
        for index, item in enumerate(items):
            prefix = f"rules.{category}[{index}]"
            if not isinstance(item, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for field in ("id", "statement", "strength", "evidence", "confidence"):
                if field not in item:
                    errors.append(f"{prefix} missing {field}")
            rule_id = item.get("id")
            if rule_id in seen:
                errors.append(f"duplicate rule id: {rule_id}")
            seen.add(rule_id)
            if item.get("strength") not in STRENGTHS:
                errors.append(f"{prefix}.strength is invalid")
            confidence = item.get("confidence")
            if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
                errors.append(f"{prefix}.confidence must be between 0 and 1")

    source = data.get("source_summary", {})
    prompt = data.get("prompt_template", {})
    if data.get("status") == "published" or args.require_published:
        if not isinstance(source.get("reference_count"), int) or source.get("reference_count", 0) <= 0:
            errors.append("published profile requires reference_count > 0")
        if not any(rules.get(key) for key in RULE_KEYS):
            errors.append("published profile requires at least one rule")
        if not prompt.get("required_slots"):
            errors.append("published profile requires prompt_template.required_slots")
        if not prompt.get("ordering"):
            errors.append("published profile requires prompt_template.ordering")
        notes = str(source.get("notes", "")).lower()
        if "human-reviewed: yes" not in notes:
            errors.append("published profile source_summary.notes must include 'human-reviewed: yes'")

    if errors:
        return fail(errors)
    print(f"OK: {data['style_id']} v{data['version']} ({data['status']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
