#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def main():
    parser = argparse.ArgumentParser(description="Validate a registered IP Style Engine asset pair.")
    parser.add_argument("registry", type=Path)
    parser.add_argument("style_key")
    parser.add_argument("--require-active", action="store_true")
    args = parser.parse_args()

    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(f"cannot read registry: {exc}")

    entry = registry.get("styles", {}).get(args.style_key)
    if not isinstance(entry, dict):
        return fail(f"style is not registered: {args.style_key}")
    if args.require_active and entry.get("status") != "active":
        return fail(f"style is not active: {args.style_key}")

    base = args.registry.parent
    profile_path = (base / entry["profile_path"]).resolve()
    bible_value = entry.get("style_bible_path")
    bible_path = (base / bible_value).resolve() if bible_value else None

    if not profile_path.is_file():
        return fail(f"profile file is missing: {profile_path}")
    if bible_path and not bible_path.is_file():
        return fail(f"Style Bible is missing: {bible_path}")

    try:
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"profile is not valid JSON: {exc}")

    expected_id = entry.get("profile_style_id")
    if expected_id and profile.get("style_id") != expected_id:
        return fail(f"profile style_id does not match registry: {profile.get('style_id')}")

    expected_profile_hash = entry.get("profile_sha256")
    if expected_profile_hash and digest(profile_path) != expected_profile_hash:
        return fail("profile content differs from the registered read-only asset")
    expected_bible_hash = entry.get("style_bible_sha256")
    if expected_bible_hash and bible_path and digest(bible_path) != expected_bible_hash:
        return fail("Style Bible content differs from the registered read-only asset")

    schema = entry.get("profile_schema", "")
    if schema == "brand-mascot-profile-v1":
        required_profile_fields = {
            "style_id", "version", "source", "design_intent", "shape_system",
            "silhouette_rules", "face_system", "color_system", "material_system",
            "presentation", "brand_translation", "commercial_checks",
            "avoid_rules", "generation_workflow"
        }
    elif schema == "native-published-v1":
        required_profile_fields = {
            "schema_version", "style_id", "name", "category", "version",
            "status", "source_summary", "rules", "prompt_template"
        }
        if profile.get("status") != "published":
            return fail("active native profile is not published")
    else:
        return fail(f"unsupported profile schema: {schema}")
    missing = sorted(required_profile_fields - set(profile))
    if missing:
        return fail(f"profile is missing required fields: {', '.join(missing)}")

    print(f"OK: {args.style_key} -> {profile['style_id']} v{profile['version']} ({entry['status']})")
    print(f"PROFILE: {profile_path}")
    if bible_path:
        print(f"STYLE_BIBLE: {bible_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
