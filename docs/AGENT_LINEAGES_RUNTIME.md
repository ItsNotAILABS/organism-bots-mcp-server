# Agent Lineages Runtime Specification

## Trait axes

| Axis | Values |
|---|---|
| persistence | mortal, persistent, undead |
| activation | continuous, on_demand, ephemeral |
| recovery | none, checkpoint, phoenix |
| degradation | fail_stop, zombie_capable |
| distribution | single_body, replicated, swarm |
| embodiment | none, desktop, browser, phone, droid, robot, drone |
| human_relation | independent, supervised, cyborg |
| operation_style | standard, ninja, sentinel, researcher |

## Canonical lifecycle

`DORMANT -> AWAKENING -> ACTIVE -> DEGRADED -> CHECKPOINTING -> TERMINATED -> RESURRECTING -> ACTIVE`

Optional Phoenix path: `ACTIVE -> TRANSFORMING -> TERMINATED -> REBORN`.

## Invariants

1. Identity lineage must be independently verifiable.
2. Stale capabilities are revoked on death, migration, degradation, or resurrection.
3. Zombie mode cannot silently retain high-risk authority.
4. Resurrection is a new execution session even when identity lineage continues.
5. Evidence of continuity is distinct from philosophical claims of consciousness continuity.
6. Every real-world mutation emits a receipt and consequence record.
7. Phantasma workers are ephemeral and sandboxed by default.
8. Droid bodies expose typed capabilities rather than ambient host authority.

## Production resurrection flow

1. detect termination or migration request;
2. revoke stale capabilities;
3. retrieve signed checkpoint;
4. verify lineage and policy;
5. select new substrate;
6. restore permitted memory and commitments;
7. run integrity and capability checks;
8. issue new scoped capabilities;
9. announce lineage continuation;
10. create resurrection receipt.

## Zombie default boundary

Permitted: health beacon, checkpoint write, safe shutdown, operator notification, read-only diagnostics.

Denied by default: financial mutation, arbitrary host execution, new external delegation, privilege expansion, unsupervised destructive actions.
