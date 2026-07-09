#!/usr/bin/env python3
"""Validate the NOVA organism bot registry and MCP manifest.

This script intentionally uses only the Python standard library so it can run
inside fresh repos, terminals, CI jobs, and local AI workspaces without setup.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "organism-bots.registry.json"
MCP_PATH = ROOT / "mcp" / "organism-bots.mcp.json"

REQUIRED_BOT_FIELDS = {
    "id",
    "name",
    "house",
    "role",
    "inputs",
    "outputs",
    "proof_gates",
}

VALID_HOUSES = {
    "Medina",
    "Genesis",
    "Substratum",
    "Cura",
    "Translatio",
    "Expressio",
    "Civitas",
}


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def validate_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    bots = registry.get("bots")
    if not isinstance(bots, list) or not bots:
        return ["Registry must contain a non-empty bots array"]

    seen_ids: set[str] = set()
    for index, bot in enumerate(bots):
        label = f"bots[{index}]"
        if not isinstance(bot, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_BOT_FIELDS - set(bot))
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")

        bot_id = bot.get("id")
        if not isinstance(bot_id, str) or not bot_id.strip():
            errors.append(f"{label}.id must be a non-empty string")
        elif bot_id in seen_ids:
            errors.append(f"duplicate bot id: {bot_id}")
        else:
            seen_ids.add(bot_id)

        house = bot.get("house")
        if house not in VALID_HOUSES:
            errors.append(f"{label}.house must be one of {sorted(VALID_HOUSES)}")

        for list_field in ("inputs", "outputs", "proof_gates"):
            value = bot.get(list_field)
            if not isinstance(value, list) or not value:
                errors.append(f"{label}.{list_field} must be a non-empty array")
            elif not all(isinstance(item, str) and item.strip() for item in value):
                errors.append(f"{label}.{list_field} must contain only non-empty strings")

    return errors


def validate_mcp_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("name", "version", "resources", "tools"):
        if field not in manifest:
            errors.append(f"MCP manifest missing field: {field}")
    if not isinstance(manifest.get("resources"), list) or not manifest.get("resources"):
        errors.append("MCP manifest resources must be a non-empty array")
    if not isinstance(manifest.get("tools"), list) or not manifest.get("tools"):
        errors.append("MCP manifest tools must be a non-empty array")
    return errors


def main() -> int:
    registry = load_json(REGISTRY_PATH)
    manifest = load_json(MCP_PATH)
    errors = validate_registry(registry) + validate_mcp_manifest(manifest)

    if errors:
        print("NOVA organism registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    bot_count = len(registry.get("bots", []))
    tool_count = len(manifest.get("tools", []))
    print(f"NOVA organism registry validation passed: {bot_count} bots, {tool_count} MCP tools")
    return 0


if __name__ == "__main__":
    sys.exit(main())
