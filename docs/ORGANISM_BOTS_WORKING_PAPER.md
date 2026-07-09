# Organism Bots MCP: A Working Paper for Governed Agent Organisms

## Abstract

Organism Bots MCP is a production architecture for agent systems that act less like isolated chat assistants and more like governed workflow organs. Each bot has a role, house route, input contract, output contract, proof gate, and launch-readiness level. The platform uses a registry-first MCP-style contract so external AI systems, local CLIs, IDEs, browser workbenches, and product runtimes can discover and invoke the same governed bot family without every integration becoming a one-off adapter.

This paper defines the organism-bot pattern, the initial bot family, the registry and server contract, the proof model, the launch model, and the production risks that must be controlled before the platform is marketed as reliable business infrastructure.

## 1. Problem

Most agent stacks fail in one of two ways. They either remain demos with attractive prompts and no operational continuity, or they become brittle integrations that require a separate adapter for every product surface. Businesses do not need another chatbot wrapper. They need repeatable workflow organisms that can build, connect, verify, launch, and learn from consequences across repositories, terminals, documents, dashboards, and external AI systems.

The platform therefore treats a bot as a governed unit of work, not a personality. A bot is a role-bearing runtime object with boundaries, permissions, inputs, outputs, proof, and a readiness state.

## 2. Definition: Organism Bot

An organism bot is a registered workflow organ with these minimum properties:

- `id`: stable machine identifier.
- `name`: human-readable role name.
- `house`: governing House Codex route.
- `role`: operational responsibility.
- `inputs`: accepted task and artifact forms.
- `outputs`: artifacts it may produce.
- `proof_gates`: evidence required before claims are trusted.
- `launch_level`: current maturity level from L0 to L4.

An organism bot may call models, CLIs, APIs, MCP servers, or local tools, but the intelligence is not reduced to any single model call. The durable intelligence lives in the protocol, registry, proof chain, templates, and reproducible execution path.

## 3. Initial Bot Family

The first family contains five production roles:

- **ORIGO Builder Bot**: creates repo structure, launch packs, templates, documentation, and reproducible builds.
- **TRANSITUS Connector Bot**: connects Caffeine, Grok Build, Claude, Cursor, Antigravity, CLIs, and MCP/MTP surfaces through bounded handoff contracts.
- **SACE Proof Bot**: creates receipts, health reports, replay objects, benchmark packets, and audit artifacts.
- **MERCATUS Launch Bot**: prepares market-facing launch surfaces, creator profiles, publish flows, onboarding, and pricing gates.
- **MEMORIA Consequence Bot**: records decisions, outcomes, drift, operator feedback, and next-build continuity.

This family gives the platform a complete loop: build, connect, prove, launch, and remember.

## 4. MCP Contract

The MCP-style contract exposes organism bots through predictable surfaces:

- `resources`: registry and runtime metadata.
- `tools`: task routing, artifact handoff, readiness validation, and proof receipt generation.
- `prompts`: reusable operator instructions for bot invocation.
- `receipts`: replayable task records with bot identity, input hash, output route, and proof gates.

This lets an IDE, terminal, browser workbench, desktop shell, or external AI worker invoke the same governed bot without rewriting platform law for every channel.

## 5. Registry-First Architecture

The registry is the source of truth. Code loads from the registry; docs explain the registry; validation protects the registry. This avoids hidden bot behavior and makes the platform auditable.

The registry should be treated as a compact civilization manifest. It states which organs exist, what they are allowed to do, what proof they must produce, and what launch level they have reached.

## 6. Launch Levels

- **L0 Draft**: concept exists, no registry contract.
- **L1 Registered**: registry entry exists and validates.
- **L2 Runnable**: server exposes the bot and accepts a task.
- **L3 Proved**: task receipt, proof gates, and replay path exist.
- **L4 Marketable**: docs, launch story, user workflow, security posture, and support path are present.

A bot should not be marketed as production until at least L3. A product surface should not be marketed until L4.

## 7. Security and Containment

Organism bots must not execute arbitrary code by default. They should route tasks into declared tools, validate inputs, preserve receipts, and mark external execution as bounded or unverified unless the platform has observed the actual run.

Key containment gates:

- registry validation before launch
- tool allowlists by bot role
- proof-gate enforcement before success claims
- explicit external surface labels
- durable task receipts
- operator-readable failure messages

## 8. Market Position

The strongest market framing is not “AI agents.” It is governed business-infrastructure automation: a platform that turns agentic coding, product launch, connector routing, and proof generation into a repeatable operating system for builders and teams.

This matters because many teams can generate code, but fewer can repeatedly produce launchable systems with documentation, validation, governance, and proof.

## 9. Next Research Questions

- How should bot health be scored across coherence, latency, proof completeness, and operator value?
- Which parts of MCP should remain strict protocol, and which should become house-specific extensions?
- How should consequence memory alter future task routing without creating uncontrolled self-modification?
- What benchmark distinguishes a real organism bot from a prompt macro?

## 10. Conclusion

Organism Bots MCP defines a practical bridge between Alfredo's civilization architecture and market-facing automation. It packages agents as governed organs, exposes them through MCP-compatible contracts, validates them through registry checks, and prepares them for real product deployment through launch levels and proof gates.
