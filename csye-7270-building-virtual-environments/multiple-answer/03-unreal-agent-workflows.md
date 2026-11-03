# Unreal and agent workflows

## MA-unreal.1

An Unreal MCP service exposes editor operations to an external assistant. A designer asks whether this makes the assistant part of the shipped game's AI. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A successful editor query demonstrates that an NPC makes correct runtime decisions.
- [ ] B. A tool that places an Actor can help construct a level.
- [ ] C. The editor connection replaces the packaged game's gameplay code.
- [ ] D. Connecting an editor assistant installs its reasoning loop into each NPC.
- [ ] E. Editor automation and runtime game AI are different roles.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The query does not exercise the NPC's behavior.
- B: Placement is an editor operation.
- C: The built game still needs gameplay logic.
- D: Runtime behavior requires its own implementation.
- E: One changes the project; the other controls behavior during play.

**Source:** Foundational: Unreal editor automation

## MA-unreal.2

An Unreal editor MCP endpoint responds, but the agent cannot find the expected scene-editing tools. The integration loads its tools from separately enabled toolsets. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent should inspect the actual catalog after configuration changes.
- [ ] B. A reachable endpoint does not establish that the needed operation is installed.
- [ ] C. Changing the requested Actor's label adds a missing tool to the server.
- [ ] D. Toolset enablement is relevant to the missing catalog.
- [ ] E. A reachable endpoint proves that every optional toolset is active.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: That verifies which tools are available now.
- B: Connectivity is only one prerequisite.
- C: Actor metadata does not register tool implementations.
- D: The endpoint and the exposed operations are separate components.
- E: The stem states that tools are separately enabled.

**Source:** Troubleshooting: missing Unreal toolsets

## MA-unreal.3

An Unreal level contains twelve Actors created from one Blueprint class. A designer asks for one placed Actor to start with a different health value. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Testing the selected Actor and unchanged peers helps verify scope.
- [ ] B. Deleting the Blueprint class is required before an instance can differ.
- [ ] C. The request identifies an instance-level customization.
- [ ] D. The agent should inspect existing overrides before assuming propagation.
- [ ] E. Changing a class default can have broader effects than changing that instance.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Both the intended change and preservation requirement matter.
- B: The class/instance model supports instance customization where exposed.
- C: Only one placed object is named.
- D: Overrides can change which value is used.
- E: Other instances may inherit the class default.

**Source:** Foundational: Actor instance versus Blueprint class

## MA-unreal.4

An Unreal Actor has a visible mesh but no configured collision response for a projectile. A hypothetical agent tool can inspect and configure its components. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A screenshot of the mesh is enough to validate projectile blocking.
- [ ] B. The investigation should include collision components and their response settings.
- [ ] C. Reconnecting MCP directly repairs the collision settings.
- [ ] D. Renaming the Actor to Wall configures its collision response.
- [ ] E. A visible mesh establishes that projectile collision is configured correctly.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The interaction needs to be exercised.
- B: Rendering and collision are separate concerns.
- C: A connection is not a gameplay configuration change.
- D: Labels do not define physical behavior.
- E: Visibility does not demonstrate collision behavior.

**Source:** Applied: component configuration

## MA-unreal.5

An agent changes a Blueprint graph and reports that it compiles. The requirement is that a door opens only after the player has collected a key. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Compilation is useful evidence that the graph is structurally acceptable to the engine.
- [ ] B. Removing the key condition is a valid repair if the door previously failed to open.
- [ ] C. Playing the no-key and has-key cases tests the stated condition.
- [ ] D. Seeing the open-door animation proves that the no-key case is blocked.
- [ ] E. Compilation establishes that the key condition is implemented correctly.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: It catches some graph errors.
- B: That violates the requirement.
- C: Both branches matter for the requirement.
- D: It covers only an opening outcome.
- E: A valid graph can encode wrong logic.

**Source:** Applied: Blueprint validation

## MA-unreal.6

An Unreal integration documents that tool invocations execute serially on the game thread. An agent must create an Actor and then configure it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding more client threads guarantees a higher editor mutation rate.
- [ ] B. Configuration should use the identity returned or resolved after creation.
- [ ] C. A slow operation can delay subsequent work in the same queue.
- [ ] D. Issuing both calls concurrently proves configuration runs after creation.
- [ ] E. The client should respect the integration's sequencing contract.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The documented execution path remains serial.
- B: The target must exist before the dependent operation.
- C: Serial execution creates ordering dependencies.
- D: Submission timing does not establish the required dependency.
- E: Unsupported overlapping calls can cause failures or ambiguity.

**Source:** Applied: serial editor operations

## MA-unreal.7

An editor MCP service is configured for same-machine access without a remote authentication layer. A teammate suggests exposing its port to the internet so a remote agent can connect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The team should inspect the integration's documented network limitations.
- [ ] B. The proposed network exposure changes the security boundary.
- [ ] C. Keeping the client near the editor can avoid exposing the editor endpoint publicly.
- [ ] D. A remote workflow needs a supported design with appropriate access controls.
- [ ] E. Changing the listening address supplies user authentication.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Those limitations affect safe deployment.
- B: Remote callers would gain a new route to editor operations.
- C: A local connector can communicate with the editor on the same machine.
- D: Local assumptions are not a remote security design.
- E: Address binding controls reachability, not identity verification.

**Source:** Troubleshooting: local endpoint

## MA-unreal.8

An agent places Actors in an Unreal level and observes them in the editor. The requested deliverable is a saved level another teammate can open. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An editor screenshot establishes that all needed packages were saved.
- [ ] B. A successful tool invocation makes version-control review redundant.
- [ ] C. Saving an unrelated level satisfies the request if the Actors remain visible.
- [ ] D. The level's saved state must be verified.
- [ ] E. Required referenced assets must also be available to the teammate.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It shows appearance, not persistence.
- B: Review is still needed to see what files changed.
- C: The requested level must contain the durable edits.
- D: Visible in-memory state is not the complete deliverable.
- E: A level may depend on other content.

**Source:** Applied: saving an Unreal level

## MA-unreal.9

A hypothetical Unreal MCP tool can launch an automation test for a pressure plate. The test should open a door when a player stands on the plate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Writing the door's open flag directly is sufficient to test the pressure plate.
- [ ] B. The test should trigger the interaction through a representative player action.
- [ ] C. The agent should retain the actual test outcome and diagnostics.
- [ ] D. A test launch acknowledgment is equivalent to a passing result.
- [ ] E. The test should observe the door state after an appropriate wait or condition.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That bypasses the causal path.
- B: This exercises the behavior under test.
- C: The evidence supports acceptance and troubleshooting.
- D: Starting and completing successfully are separate events.
- E: It must measure the result.

**Source:** Applied: functional tests

## MA-unreal.10

An Unreal agent edits an Actor visible during a play session, but the designer expected a persistent change to the authoring level. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent should determine whether it edited a runtime instance or authoring data.
- [ ] B. Extending the play session ensures the value is saved to the authoring level.
- [ ] C. The designer's request is satisfied by a screenshot of the temporary instance.
- [ ] D. The intended change should be verified after ending play and reopening the saved level.
- [ ] E. A value observed during play proves the level asset contains that value.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The two states have different persistence roles.
- B: Elapsed play time is not a save operation.
- C: The requirement was persistence.
- D: That checks the deliverable the designer requested.
- E: Runtime state can differ from saved authoring state.

**Source:** Troubleshooting: wrong editor world

## MA-unreal.11

Two Unreal Actors reference one material instance asset. A designer wants only the first Actor's appearance to change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Changing the Actor label breaks its material reference.
- [ ] B. The second Actor is part of the verification set.
- [ ] C. The word instance in the asset's name proves it is private to one Actor.
- [ ] D. Editing the referenced asset may affect both Actors.
- [ ] E. The agent must choose a solution whose ownership matches the requested scope.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Label changes do not make shared assets independent.
- B: It must remain unchanged.
- C: A material instance asset can have multiple consumers.
- D: They share the same material instance asset.
- E: An independent asset or suitable per-object runtime approach may be appropriate.

**Source:** Advanced: material instance scope

## MA-unreal.12

A studio adds a hypothetical custom tool that replaces selected placeholder Actors with approved props. It must preserve each placeholder's transform. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The tool should validate the replacement asset and all target identities before making changes.
- [ ] B. Comparing before/after transforms checks a key invariant.
- [ ] C. The result should identify replaced objects and any failures.
- [ ] D. An aggregate success message establishes that every transform was preserved.
- [ ] E. Deleting the placeholders first is sufficient validation of replacement availability.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Preflight checks reduce partial failures.
- B: The task explicitly requires transform preservation.
- C: A per-target record makes partial completion visible.
- D: The invariant needs per-object evidence.
- E: Deletion does not establish that replacement can succeed.

**Source:** Advanced: bounded Unreal extension
