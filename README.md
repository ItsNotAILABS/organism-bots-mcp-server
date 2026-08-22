# NOVA Organism Bots MCP

**Governed workflow workers for repeatable multi-step operations in the NEXUS ecosystem.**

Organism Bots packages reusable operational workflows behind MCP/API-style task surfaces. Bots can be discovered, routed, submitted and inspected as bounded workers while POCKET/NEXUS retains identity, policy, budgets and cross-system coordination.

```text
POCKET / NEXUS task
       │
       ▼
workflow route
       │
       ▼
Organism Bot
       │
       ├── bounded steps
       ├── context/artifact inputs
       ├── progress/readiness
       └── task receipt
       │
       ▼
artifact + receipt + handoff
```

## NEXUS federation

Declaration: [`ecosystem.surface.json`](ecosystem.surface.json).

Primary actions:

```text
bot.list
bot.describe
bot.route
bot.submit
bot.readiness
artifact.import
```

The workflow plane consumes:

```text
nexus.task.v1
nexus.policy-decision.v1
nexus.budget.v1
nexus.context-pack.v1
nexus.artifact.v1
```

and returns capability, receipt and handoff objects that can be inspected by the host or next worker.

## Workflow lifecycle

```text
discover bot
 -> validate inputs
 -> policy / budget
 -> run bounded workflow
 -> persist step/result state
 -> produce artifact
 -> emit execution receipt
 -> hand off
```

A workflow is successful because its acceptance criteria and outputs are satisfied, not simply because every internal step ran.

## Production bot requirements

```text
[ ] stable bot ID and version
[ ] explicit required inputs
[ ] bounded tool/capability set
[ ] timeout and retry behavior
[ ] readiness/health check
[ ] output schema
[ ] artifact hashes where files are produced
[ ] failure/denial outcome
[ ] NEXUS request correlation
[ ] operator documentation
```

## MCP integration

Connect the server through the repository's MCP entrypoint and use the bot registry to enumerate currently available workers. Keep client configuration external to the repository when it contains local paths or credentials.

## Verify

Run the repository's bot/server validators and smoke tests. After changing the federation surface, validate against NEXUS:

```bash
# from ItsNotAILABS/nexus
python tools/validate_ecosystem_protocols.py
python tools/validate_ecosystem_registry.py
python tools/production_gate.py
```

## Ecosystem

- [NEXUS](https://github.com/ItsNotAILABS/nexus) — routing and shared protocols
- [POCKET](https://github.com/ItsNotAILABS/pocket) — identity/policy/product gateway
- [POCKET Agent](https://github.com/ItsNotAILABS/pocket-agent) — long-running execution
- [x-mcp-skills](https://github.com/ItsNotAILABS/x-mcp-skills) — reusable external connector contracts
- [NOVA Connector Control Plane](https://github.com/ItsNotAILABS/nova-connector-control-plane) — live connector routing

Organism Bots is the repeatable workflow layer: **turn a known operating process into a bounded worker that the rest of the ecosystem can route and verify.**
