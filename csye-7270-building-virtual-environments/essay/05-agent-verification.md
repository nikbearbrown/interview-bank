# Agent testing, troubleshooting and engine comparisons

## ES-verification.1

An agent claims a door interaction is complete after creating a script and taking a screenshot. Design a minimum evidence package for accepting a door that opens only when the player holds a key.

**Points:** 5

**Rubric (1 point each):**

1. Requires inspecting the actual implementation and changed assets for the intended condition and scope.
2. Requires compilation/import validation without presenting it as behavioral proof.
3. Tests both the no-key rejection and has-key opening paths through representative interaction.
4. Checks persistence and the relevant play/build environment for the intended deliverable.
5. Reports actual outcomes and remaining limitations rather than relying on the completion claim or screenshot alone.

**Source:** Foundational: evidence-based completion

## ES-verification.2

An editor tool times out while creating a checkpoint. The operation has no documented atomicity guarantee. Explain how to recover without duplicating the checkpoint or deleting unrelated work.

**Points:** 5

**Rubric (1 point each):**

1. Recognizes that a timeout leaves the execution outcome unknown.
2. Inspects the current scene and available operation records using a stable identifier or bounded search.
3. Uses a supported idempotency mechanism or explicit existence check before retrying creation.
4. Verifies exactly one intended checkpoint and its configured behavior after recovery.
5. Reports unresolved uncertainty if inspection is insufficient and avoids broad deletion or a false success claim.

**Source:** Advanced: retry after uncertainty

## ES-verification.3

Write an engine-neutral specification for a checkpoint, then explain how Unity and Unreal implementations could satisfy it while using different object and scripting systems.

**Points:** 5

**Rubric (1 point each):**

1. Defines activation, saved location and respawn behavior in observable terms independent of engine terminology.
2. Maps the Unity implementation to appropriate scene objects/components and a reusable asset where useful.
3. Maps the Unreal implementation to appropriate Actors/components and Blueprint or code behavior where useful.
4. Makes units, coordinate spaces, object identities and persistence explicit at each adapter boundary.
5. Uses equivalent gameplay acceptance cases in both engines without requiring identical tools or serialized assets.

**Source:** Applied: cross-engine checkpoint specification

## ES-verification.4

An automated game test passes intermittently. It uses random spawn positions, rendered-frame waits and an asynchronously imported asset. Design a repeatable diagnosis and repair plan.

**Points:** 5

**Rubric (1 point each):**

1. Records failures with seed, timing, import status and relevant engine configuration.
2. Controls or records random input so a failing spawn can be reproduced.
3. Uses a suitable fixed simulation step or bounded simulation-condition wait instead of assuming rendered frames equal elapsed game time.
4. Waits for successful asset readiness and distinguishes import failure from gameplay failure.
5. Reruns the repaired test under the controlled setup and retains failures rather than reporting only the first pass.

**Source:** Applied: diagnose a flaky agent test

## ES-verification.5

A team wants an agent to import props, place them, configure collisions and run tests. Design a fair comparison of Unity and Unreal integrations without assuming that using MCP gives them identical capabilities.

**Points:** 5

**Rubric (1 point each):**

1. Defines the same observable scene and gameplay requirements for both trials.
2. Inventories the actual tools, supported operations and required manual steps in each integration.
3. Measures task completion, correctness, recovery from a controlled failure and human effort on comparable inputs.
4. Includes team skills, target platform and engine-specific asset/workflow constraints in the decision.
5. Records compatibility and evidence limitations and chooses based on the measured task rather than tool count or a demo alone.

**Source:** Advanced: compare Unity and Unreal workflows

## ES-verification.6

An agent reduces a benchmark's steady frame time from 20 to 15 milliseconds for a 60 FPS target, but disables required shadows. Calculate the timing result and propose an acceptable next step.

**Points:** 5

**Rubric (1 point each):**

1. Computes the target budget as about 16.67 milliseconds per frame and the baseline as 50 FPS.
2. Computes the new steady rate as about 66.67 FPS and the time saving as 5 milliseconds per frame.
3. Recognizes that the changed result meets the timing budget but violates the visual requirement.
4. Restores or preserves required shadows and profiles the actual bottleneck before choosing another optimization.
5. Rebenchmarks under the same workload and checks both timing variation and visual acceptance on the target environment.

**Source:** Advanced: optimize with constraints

## ES-verification.7

An agent writes a checkpoint feature and its test. The test directly assigns the expected saved position before asserting equality. Explain the weakness and design stronger evidence, including a negative case.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that the test sets its own expected outcome and bypasses the checkpoint behavior.
2. Drives the player through the actual activation path and then exercises respawn or load behavior.
3. Observes the resulting position independently of the setup assignment and uses a justified tolerance if needed.
4. Adds a negative case such as respawning before any checkpoint is activated or entering an inactive checkpoint.
5. Reviews the test against the requirement and checks that a deliberately broken activation path would be detected.

**Source:** Advanced: independent test oracle

## ES-verification.8

An agent changes five of ten lights before a tool fails. The contract does not provide transactions. Explain atomicity, design a recovery record and propose acceptance criteria for a resumed operation.

**Points:** 5

**Rubric (1 point each):**

1. Defines atomicity as an all-or-nothing operation and explains why a batch call alone does not provide it.
2. Records per-light identity, original value, attempted value and observed outcome.
3. Inspects current state before choosing a bounded resume or restoration of verified prior values.
4. Avoids overwriting unrelated concurrent changes by checking preconditions or coordinating access.
5. Verifies all intended final values and unchanged out-of-scope objects, saves the result and reports any unresolved partial state.

**Source:** Advanced: recover a partial scene batch
