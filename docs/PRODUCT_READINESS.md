# Product Readiness: NOVA Organism Bots MCP

## Product Name

**NOVA Organism Bots MCP**

## One-Line Offer

A registry-governed MCP platform for launching role-specific AI workflow organisms that can build, connect, prove, launch, and remember across repos, terminals, IDEs, and external AI systems.

## Product Views

1. **Builder View**: choose or create a bot, define accepted inputs, assign proof gates, and generate launch artifacts.
2. **Operator View**: invoke registered bots through CLI, IDE, browser workbench, or API.
3. **Proof View**: inspect receipts, validation reports, task outcomes, and readiness levels.
4. **Marketplace View**: list bot families, creator profiles, guided post-clone setup, and pricing recommendations.

## Minimum Launch Flow

1. Register the bot in `organism-bots.registry.json`.
2. Validate the registry and MCP manifest.
3. Start the local server.
4. Invoke a task through `/tasks`.
5. Save the returned receipt.
6. Promote the bot from L1 to L2 or L3 only when the proof path exists.

## Launch Levels

| Level | Name | Gate |
| --- | --- | --- |
| L0 | Draft | Concept and role only |
| L1 | Registered | Registry validates |
| L2 | Runnable | Server loads bot and accepts task |
| L3 | Proved | Receipt and replay path exist |
| L4 | Marketable | Docs, UX, security posture, and support path exist |

## Production Gates

- Registry and MCP manifest validation pass.
- Each bot has a house, role, input contract, output contract, and proof gates.
- Server exposes health and registry endpoints.
- Task invocation returns a deterministic receipt.
- Docs explain install, operation, limits, and readiness.
- Unsafe external execution is explicitly marked as unverified unless observed.

## Marketing Angles

- **For builders**: stop rebuilding the same agent scaffolds; register them once and invoke them everywhere.
- **For teams**: turn AI workers into governed workflow organs with roles, proof, and launch levels.
- **For agencies**: package business automation as repeatable bot families instead of one-off scripts.
- **For platform owners**: connect external AI systems without letting the LLM overshadow the product intelligence.

## Readiness Status

Current status after this hardening pass:

- L1: achieved through the registry and manifest.
- L2: achieved through the stdlib server and task endpoint.
- L3: partial; receipts exist, but replay storage and proof artifact persistence should be added next.
- L4: partial; docs and product framing exist, but a browser dashboard and installer are still needed.

## Next Engineering Tasks

- Add persistent receipt storage.
- Add CLI wrapper for validate, serve, invoke, and report.
- Add a dashboard for bot selection, task submission, and readiness inspection.
- Add CI checks for registry validation.
- Add example integrations for Caffeine, Grok Build, Claude, Cursor, Antigravity, and local terminal workers.
