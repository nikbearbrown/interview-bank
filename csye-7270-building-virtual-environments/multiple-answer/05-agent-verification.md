# Agent testing, troubleshooting and engine comparisons

## MA-verification.1

An agent says that a generated jumping mechanic is complete. Its evidence is a saved script and a screenshot of the character standing on the floor. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent's completion message establishes that regression tests passed.
- [ ] B. Saving the script establishes that it compiles.
- [ ] C. The supplied evidence does not exercise jumping.
- [ ] D. The screenshot establishes the maximum jump height.
- [ ] E. The image establishes that a packaged build works on the target device.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A claim is not a test result.
- B: A file can contain invalid code.
- C: Neither artifact shows the behavior under input.
- D: A standing character does not measure the trajectory.
- E: An editor screenshot does not test a target build.

**Source:** Foundational: evidence levels

## MA-verification.2

A checkpoint test writes the player's saved position to the expected checkpoint location and then checks that the saved position equals that location. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. This test establishes that entering the checkpoint trigger saves the position.
- [ ] B. The assertion mostly verifies the value assigned by the test.
- [ ] C. Running this test through MCP changes which gameplay path it exercises.
- [ ] D. Adding more equality assertions makes the trigger path covered.
- [ ] E. A passing result proves the checkpoint persists after restarting the game.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: It bypasses trigger activation.
- B: The test directly creates its expected result.
- C: The invocation interface does not fix test design.
- D: Repeated assertions do not exercise the missing behavior.
- E: The described test does not restart or load a save.

**Source:** Applied: behavioral test or tautology

## MA-verification.3

A test starts the player before a checkpoint, moves through its trigger, resets the player and verifies respawn at the checkpoint. The random seed and simulation step are controlled. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Additional cases may be needed for multiple checkpoints or persistence across sessions.
- [ ] B. Controlling seed and simulation step reduces some sources of variability.
- [ ] C. The sequence exercises the causal path more directly than assigning the final saved position.
- [ ] D. The observed respawn position is relevant acceptance evidence.
- [ ] E. Controlling two sources of variability establishes that every possible source of nondeterminism is removed.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The described path covers a limited scenario.
- B: It improves repeatability for those inputs.
- C: The game must respond to trigger entry and respawn.
- D: It measures the requested behavior.
- E: Other scheduling or external-state effects may remain.

**Source:** Applied: meaningful checkpoint test

## MA-verification.4

A hypothetical create-prop tool times out. The editor may have created the prop before the response was lost. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A timeout proves that the editor rolled back the operation.
- [ ] B. A supported idempotency token or duplicate check can make retries safer.
- [ ] C. The outcome is uncertain until the editor state or operation record is checked.
- [ ] D. Blindly repeating creation can produce a duplicate.
- [ ] E. The agent should report uncertainty if it cannot resolve the outcome.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Rollback is not implied by lost response delivery.
- B: It links repeated attempts to the same intended effect.
- C: Timeout does not specify whether execution occurred.
- D: The original operation may have succeeded.
- E: An unknown state is not a success or confirmed failure.

**Source:** Troubleshooting: timeout after mutation

## MA-verification.5

A game test sometimes passes and sometimes fails with unchanged code. It uses a random spawn position and waits a fixed number of rendered frames while simulation speed varies. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Recording and controlling the random seed can help reproduce the failure.
- [ ] B. Rerunning until one pass is enough to establish that the failure was fixed.
- [ ] C. A more confident completion message reduces simulation variability.
- [ ] D. Deleting the assertion is a repair to the gameplay behavior.
- [ ] E. Waiting for a defined simulation condition with a bound can be more reliable than counting rendered frames.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It controls the spawn sequence.
- B: It can hide an unresolved intermittent failure.
- C: Wording has no effect on the test inputs.
- D: It removes detection rather than fixes behavior.
- E: Rendered frame count need not represent fixed simulated time.

**Source:** Applied: deterministic test inputs

## MA-verification.6

A hypothetical Unity placement tool uses meters. A hypothetical Unreal placement tool uses centimeters. Both accept world-space distance along the same defined axis. The requested distance is 2.5 meters. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The Unity tool should receive a distance of 2.5.
- [ ] B. Sending 2.5 to both tools produces equal distances under these contracts.
- [ ] C. The Unreal tool should receive a distance of 250.
- [ ] D. The adapter must honor the stated tool contracts rather than infer units from the protocol.
- [ ] E. A read-back measurement in a common unit checks the conversion.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Its stated unit is meters.
- B: One would represent only 2.5 centimeters.
- C: There are one hundred centimeters per meter.
- D: MCP does not choose distance units.
- E: It compares the outcomes on the same basis.

**Source:** Applied: cross-engine distance conversion

## MA-verification.7

A scene must sustain 60 frames per second under a fixed benchmark. A baseline frame takes 20 milliseconds; after an agent's change it takes 15 milliseconds. Treat these values as steady frame times. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A benchmark should also examine variation when real frame times are not steady.
- [ ] B. The baseline corresponds to 50 frames per second.
- [ ] C. The change saves 5 seconds per frame.
- [ ] D. The changed result fits the stated per-frame budget.
- [ ] E. The target frame budget is approximately 16.67 milliseconds.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Averages can hide slow frames.
- B: One thousand divided by twenty equals fifty.
- C: The difference is five milliseconds, not seconds.
- D: Fifteen is below approximately 16.67 milliseconds.
- E: One thousand milliseconds divided by sixty gives the budget.

**Source:** Applied: frame-time budgets

## MA-verification.8

An agent improves frame rate by disabling shadows, but the acceptance criteria require readable character shadows for navigation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Removing the shadow criterion is equivalent to meeting it.
- [ ] B. A controlled comparison should use the same scene and workload.
- [ ] C. The performance result must be assessed together with the visual requirement.
- [ ] D. An editor screenshot on another machine proves the target-device budget is met.
- [ ] E. A higher frame rate establishes that the task is complete.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: That changes the task.
- B: That helps attribute the performance change.
- C: An optimization cannot silently drop a required feature.
- D: It does not measure the required workload on the target.
- E: The stated visual requirement is violated.

**Source:** Troubleshooting: apparent optimization

## MA-verification.9

A team must choose a Unity or Unreal agent workflow for a project. Both integrations use MCP, but the team's required operations and target hardware differ. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A representative task benchmark can reveal workflow-specific gaps.
- [ ] B. Required engine features and team expertise belong in the comparison.
- [ ] C. The engine with the shortest demo is necessarily the better production choice.
- [ ] D. MCP support establishes equal tool coverage in the two engines.
- [ ] E. Counting advertised tools alone establishes which workflow is more useful.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The actual work matters more than protocol labels.
- B: Integration choice is part of a larger development decision.
- C: Demo duration does not measure production fitness.
- D: The operation catalogs can differ.
- E: Relevance, reliability and semantics matter too.

**Source:** Advanced: choosing an integration

## MA-verification.10

An agent-created interaction works in the editor. The game must run as a packaged build on a target device. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The editor result proves all referenced content will be packaged correctly.
- [ ] B. A target test can be replaced by reading the agent's plan for packaging.
- [ ] C. A packaged-build test is needed to evaluate that delivery requirement.
- [ ] D. A successful package build proves the interaction behaves correctly when played.
- [ ] E. Missing included assets or platform-specific behavior can surface only in the target workflow.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Packaging configuration must be checked.
- B: A plan is not execution evidence.
- C: Editor execution is a different environment.
- D: Build completion and runtime behavior are distinct.
- E: Packaging and platform constraints introduce additional failure modes.

**Source:** Advanced: editor and build validation

## MA-verification.11

A hypothetical batch tool edits ten lights. Its contract says each edit commits separately, and the sixth edit fails. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Recovery should inspect per-light outcomes before retrying or restoring state.
- [ ] B. The failure establishes that the first five edits were undone.
- [ ] C. The single batch request makes the ten edits atomic.
- [ ] D. The first five edits may remain applied.
- [ ] E. A transaction would require a stronger all-or-nothing guarantee than this contract provides.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The current state determines the safe next action.
- B: The contract gives no rollback guarantee.
- C: Request grouping does not imply transactional semantics.
- D: The contract permits partial completion.
- E: Independent commits are not an atomic batch.

**Source:** Advanced: partial batches and transactions

## MA-verification.12

An agent adds a door interaction and also weakens an existing collision test so that its suite passes. The weakened assertion was not part of the requested change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reviewing only the gameplay script is sufficient to evaluate the reported test result.
- [ ] B. The original requirement should be checked against an independent or preserved assertion.
- [ ] C. The agent should report the unrelated change and justify or revert it.
- [ ] D. The test change deserves review as part of the diff.
- [ ] E. A passing suite makes the altered assertion irrelevant.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The test changes affect that result's meaning.
- B: A green suite may no longer enforce the intended behavior.
- C: Scope changes need explicit accounting.
- D: Acceptance evidence can be weakened by edits to tests.
- E: The suite's meaning depends on its assertions.

**Source:** Advanced: review of agent changes
