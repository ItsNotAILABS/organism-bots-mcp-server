# NOVA Organism Bots MCP

![Status](https://img.shields.io/badge/status-draft%20platform-blue)
![MCP](https://img.shields.io/badge/MCP-compatible%20contract-0b7285)
![Python](https://img.shields.io/badge/python-stdlib%20server-3776ab)
![Bots](https://img.shields.io/badge/organism%20bots-12-6f42c1)
![Proof](https://img.shields.io/badge/proof-receipt%20first-2f9e44)

![NOVA Organism Bots MCP Platform](assets/organism-bots-platform.svg)

NOVA Organism Bots MCP is a registry-governed platform for launching role-specific AI workflow organisms. It connects repositories, external AI workers, MCP/MTP servers, local terminals, browser workbenches, documents, proof gates, CI checks, product specs, SEO, pricing, customer workflows, and launch surfaces through one governed contract.

This is not a chatbot wrapper. It is an operator layer for business-building agents: build, connect, prove, launch, remember, secure, price, index, and support.

## Search Keywords

MCP server for AI agents, governed AI workflow bots, AI agent registry, business automation agents, AI proof receipts, launch-ready AI agent platform, external AI connector platform, NOVA Build, organism bots, developer automation platform.

## Why It Exists

AI builders can generate code quickly, but production work fails when the surrounding system is missing: registry, permissions, task contracts, proof receipts, launch readiness, consequence memory, customer workflow, and reusable operator paths.

This repo gives those pieces a shared shape. A bot is not just a prompt. A bot is a governed workflow organ with a role, house, inputs, outputs, proof gates, and launch level.

## What You Can Build

- Caffeine / Grok Build / Claude / Cursor / Antigravity connector bots.
- Repo builder bots that generate production packages and docs.
- Browser workbench bots for manifests, service workers, storage, WASM, and console telemetry.
- Proof bots that create receipts, benchmark reports, audit trails, and release gates.
- Launch bots for marketplace listings, creator profiles, onboarding flows, SEO, pricing, and customer success.
- Consequence bots that preserve lessons, drift, operator outcomes, and next-build continuity.

## Quick Start

Run the validation gate:

```bash
python tools/validate_organism_registry.py
```

Start the local server:

```bash
python server/organism_bots_server.py --port 8766
```

Inspect health, registry, tools, and a bot:

```bash
curl http://127.0.0.1:8766/health
curl http://127.0.0.1:8766/registry
curl http://127.0.0.1:8766/tools
curl http://127.0.0.1:8766/bots/transitus-connector-bot
```

Submit a dry-run task receipt:

```bash
curl -s -X POST http://127.0.0.1:8766/tasks \
  -H 'Content-Type: application/json' \
  -d @examples/minimal-task.json
```

Ask the platform for a route plan:

```bash
curl -s -X POST http://127.0.0.1:8766/route \
  -H 'Content-Type: application/json' \
  -d @examples/route-plan.json
```

The first server intentionally creates receipts and routing plans only. It does not execute arbitrary external code. Real tool execution should be added behind explicit allowlists and proof storage.

## Organism Bot Family

| Bot | House | Use It For |
| --- | --- | --- |
| ORIGO Builder Bot | Genesis | Repos, packages, app shells, launch packs |
| TRANSITUS Connector Bot | Translatio | External AI workers, MCP/MTP servers, CLIs, IDEs |
| SACE Proof Bot | Medina | Proof packs, benchmark trails, audit records |
| MERCATUS Launch Bot | Expressio | Product pages, onboarding, outreach, creator profiles |
| MEMORIA Consequence Bot | Cura | Outcome tracking, drift, lessons, consequence memory |
| AEDIFICIUM Spec Bot | Genesis | Click-only app specs and 10-section exports |
| SPECULUM Browser Workbench Bot | Substratum | Service workers, storage, manifests, WASM, browser telemetry |
| CUSTOS CI Sentinel Bot | Cura | CI gates, validator runs, failure reports |
| VIGIL Securitas Bot | Cura | Auth, permissions, unsafe execution, connector abuse surfaces |
| INDEXUS SEO Bot | Expressio | Repository discoverability, keyword strategy, GitHub topics |
| PRETIUM Pricing Advisor Bot | Civitas | Pricing tiers, assumptions, support-load modeling |
| CIVITAS Customer Workflow Bot | Civitas | Onboarding, support triage, success checklists |

See [docs/BOT_CATALOG.md](docs/BOT_CATALOG.md) for the full bot catalog.

## Repository Map

- `organism-bots.registry.json` — machine-readable bot family registry.
- `mcp/organism-bots.mcp.json` — MCP-style resource/tool contract.
- `server/organism_bots_server.py` — dependency-free runnable development server.
- `tools/validate_organism_registry.py` — dependency-free validation gate.
- `examples/minimal-task.json` — sample task invocation payload.
- `examples/route-plan.json` — sample route-planning payload.
- `skills/organism-bot-orchestrator/SKILL.md` — agent activation workflow.
- `research/ORGANISM_BOTS_PLATFORM_RESEARCH.md` — deep platform paper.
- `docs/ORGANISM_BOTS_WORKING_PAPER.md` — concise working paper for the product architecture.
- `docs/PRODUCT_READINESS.md` — launch levels, product views, and next gates.
- `docs/BOT_CATALOG.md` — public catalog, use cases, SEO phrases, and topic recommendations.

## MCP Tool Contract

The current MCP-style manifest exposes:

- `organism_bots.list`
- `organism_bots.describe`
- `organism_bots.submit_task`
- `organism_bots.route_plan`
- `organism_bots.import_artifact`
- `organism_bots.readiness_report`

The stdlib server mirrors the first runtime surface through `/health`, `/registry`, `/tools`, `/bots/{bot_id}`, `POST /tasks`, `POST /route`, and `POST /readiness`.

## Launch Levels

| Level | Name | Gate |
| --- | --- | --- |
| L0 | Draft | Concept and role only |
| L1 | Registered | Registry validates |
| L2 | Runnable | Server loads bot and accepts task |
| L3 | Proved | Receipt and replay path exist |
| L4 | Marketable | Docs, UX, security posture, and support path exist |

Current state: L2 is present for the platform substrate. L3 is partially present through deterministic receipts. The next hardening step is persistent receipt storage plus CI validation.

## Operating Law

- No organism bot can claim completion without an artifact or proof record.
- External AI systems are connected through bounded handoff contracts, not treated as the whole intelligence.
- Registry law comes before runtime action.
- Tool execution must be allowlisted and receipt-backed.
- Market-facing launch claims require validation, reproducible operation, and operator-readable limits.

## GitHub Discoverability

Recommended repository topics:

`mcp`, `model-context-protocol`, `ai-agents`, `agent-platform`, `workflow-automation`, `developer-tools`, `ai-infrastructure`, `local-ai`, `github-automation`, `product-launch`, `nova`, `organism-bots`.

## Product Direction

This repo should become the MCP-facing organism control plane for NOVA Build: choose a bot, connect a surface, submit a task, inspect proof, import artifacts, and promote the result into a launch package.

Next build: add persistent receipts, CI checks, a CLI wrapper, and the browser dashboard for bot selection and task inspection.
