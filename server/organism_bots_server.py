#!/usr/bin/env python3
"""NOVA Organism Bots MCP development server.

This is the first runnable substrate for the registry. It does not execute
arbitrary external code. It loads the registry, exposes health/discovery
endpoints, and creates deterministic task receipts that can later be persisted
or handed to proof storage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "organism-bots.registry.json"
MCP_PATH = ROOT / "mcp" / "organism-bots.mcp.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def receipt_hash(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class OrganismState:
    def __init__(self) -> None:
        self.registry = load_json(REGISTRY_PATH)
        self.manifest = load_json(MCP_PATH)
        self.bots = {bot["id"]: bot for bot in self.registry.get("bots", [])}

    def health(self) -> dict[str, Any]:
        return {
            "status": "ok",
            "service": "nova-organism-bots-mcp",
            "time": utc_now(),
            "bot_count": len(self.bots),
            "tool_count": len(self.manifest.get("tools", [])),
        }

    def create_task_receipt(self, task: dict[str, Any]) -> tuple[int, dict[str, Any]]:
        bot_id = task.get("bot_id")
        if bot_id not in self.bots:
            return 404, {
                "status": "rejected",
                "reason": "unknown_bot_id",
                "known_bots": sorted(self.bots),
            }

        bot = self.bots[bot_id]
        requested = {
            "bot_id": bot_id,
            "task": task.get("task", ""),
            "target": task.get("target", ""),
            "operator_scope": task.get("operator_scope", "dry-run"),
            "time": utc_now(),
        }
        task_id = receipt_hash(requested)[:24]
        receipt = {
            "schema": "nova.organism.task_receipt.v1",
            "status": "accepted",
            "task_id": task_id,
            "bot": {
                "id": bot_id,
                "name": bot.get("name"),
                "house": bot.get("house"),
                "role": bot.get("role"),
            },
            "request": requested,
            "proof_gates": bot.get("proof_gates", []),
            "execution_mode": "receipt_only_no_external_code_execution",
            "next_gate": "persist_receipt_and_bind_real_tool_execution",
        }
        receipt["receipt_hash"] = receipt_hash(receipt)
        return 202, receipt


class Handler(BaseHTTPRequestHandler):
    state: OrganismState

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003 - stdlib API name
        print(f"[{utc_now()}] {self.address_string()} {format % args}")

    def send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        return json.loads(raw.decode("utf-8"))

    def do_GET(self) -> None:  # noqa: N802 - stdlib API name
        path = urlparse(self.path).path
        if path == "/health":
            self.send_json(200, self.state.health())
        elif path == "/registry":
            self.send_json(200, self.state.registry)
        elif path == "/tools":
            self.send_json(200, {"tools": self.state.manifest.get("tools", [])})
        else:
            self.send_json(404, {"status": "not_found", "paths": ["/health", "/registry", "/tools", "/tasks"]})

    def do_POST(self) -> None:  # noqa: N802 - stdlib API name
        path = urlparse(self.path).path
        if path != "/tasks":
            self.send_json(404, {"status": "not_found", "paths": ["/tasks"]})
            return
        try:
            task = self.read_json_body()
        except json.JSONDecodeError as exc:
            self.send_json(400, {"status": "rejected", "reason": "invalid_json", "detail": str(exc)})
            return
        status, receipt = self.state.create_task_receipt(task)
        self.send_json(status, receipt)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the NOVA Organism Bots MCP development server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args()

    Handler.state = OrganismState()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"NOVA Organism Bots MCP server listening on http://{args.host}:{args.port}")
    print("Available paths: /health, /registry, /tools, POST /tasks")
    server.serve_forever()


if __name__ == "__main__":
    main()
