# x-organism-bots-mcp

NOVA Organism Bots MCP is the repo for role-bearing workflow organisms that connect repos, external AI workers, MCP/MTP servers, artifacts, proof gates, and product launch surfaces.

## What This Is

Organism bots are not chatbots. They are runtime organs that:

- sense task context
- route work
- activate tools
- verify outputs
- record artifacts
- hand off the next action

## Initial Bot Family

- ORIGO Builder Bot — code, repo, release, package.
- TRANSITUS Connector Bot — external AI, MCP/MTP, webhooks, CLIs.
- SACE Proof Bot — proof packs, benchmarks, audits, release gates.
- MERCATUS Launch Bot — market surfaces, pricing, onboarding, outreach.
- MEMORIA Consequence Bot — outcome tracking, risk, lessons, replay.

## Files

- `research/ORGANISM_BOTS_PLATFORM_RESEARCH.md` — deep platform paper.
- `organism-bots.registry.json` — machine-readable bot registry.
- `mcp/organism-bots.mcp.json` — MCP-style server contract.
- `skills/organism-bot-orchestrator/SKILL.md` — activation workflow for agents.

## Product Direction

The platform should become a control plane where builders can:

1. choose a bot
2. connect tools
3. submit a task
4. watch the run
5. import artifacts
6. verify proof
7. launch a package

## Operating Law

No organism bot can claim completion without an artifact or proof record.
