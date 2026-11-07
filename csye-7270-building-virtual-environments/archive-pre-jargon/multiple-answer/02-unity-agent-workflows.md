# Unity, Spark and agent workflows

## MA-unity.1

Unity Spark is presented as a browser-based game-creation experience. A Unity MCP integration connects an external assistant to editor capabilities. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A team should evaluate either workflow against its actual game requirements.
- [ ] B. Using the same vendor's products establishes that their project workflows are interchangeable.
- [ ] C. Spark is the expanded spelling of the MCP acronym.
- [ ] D. These descriptions identify different product roles.
- [ ] E. A Spark demonstration does not establish which tools an installed MCP server exposes.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Product labels are not acceptance evidence.
- B: Workflow compatibility needs evidence.
- C: MCP means Model Context Protocol.
- D: A creation experience and an integration interface serve different purposes.
- E: The server's own capabilities need inspection.

**Source:** Foundational: Spark versus an editor bridge

## MA-unity.2

A vendor note says an older in-editor MCP server is deprecated and a CLI-hosted MCP server replaces it. A Unity team uses the older server. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A replacement server can be assumed to preserve every old tool name.
- [ ] B. The team should identify its installed integration before changing configuration.
- [ ] C. Deleting the project's scenes is a necessary first migration step.
- [ ] D. Deprecating one server means that the MCP protocol itself has been retired.
- [ ] E. The team should verify the replacement in a small project before migrating production work.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The replacement's catalog and contracts must be checked.
- B: The note applies to a particular component.
- C: Connection migration does not justify deleting game content.
- D: A component lifecycle is not a protocol lifecycle.
- E: A bounded trial exposes compatibility problems.

**Source:** Applied: migrating an integration

## MA-unity.3

A Unity automation package offers both direct commands and an MCP interface to its editor operations. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The same high-level task may be automated without language-model inference.
- [ ] B. Direct commands make authorization unnecessary because no MCP message is involved.
- [ ] C. A tool-based interface can expose structured inputs for an operation.
- [ ] D. An agent's supported interfaces affect which route is usable.
- [ ] E. Both routes still require checking the editor operation's result.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Scripted automation can invoke known operations directly.
- B: The commands can still change project state.
- C: A schema can describe the accepted arguments.
- D: Some hosts expose tools while others can run commands.
- E: Interface choice does not prove correctness.

**Source:** Foundational: CLI and MCP roles

## MA-unity.4

Two Unity projects are open and each contains a scene called Arena. An agent is asked to add a light to one project's Arena scene. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A successful tool connection proves that it targets the correct project.
- [ ] B. The most recently opened editor is necessarily the requested target.
- [ ] C. The agent should verify project identity as well as scene identity.
- [ ] D. A light appearing in either Arena satisfies the request.
- [ ] E. Matching the scene name is sufficient to select the intended project.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Connectivity does not identify the user's intended workspace.
- B: Recency is not user intent.
- C: A shared scene name is ambiguous across projects.
- D: The destination project is part of the requirement.
- E: Both projects satisfy that name.

**Source:** Applied: selecting a Unity target

## MA-unity.5

A Unity scene contains twenty instances of a lamp prefab. The request is to make just one named lamp blue while leaving the other lamps as they are. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The intended scope is the selected instance.
- [ ] B. The agent should verify the other lamps after editing.
- [ ] C. Applying the selected instance's change to the prefab asset preserves a one-instance scope.
- [ ] D. Editing a shared material asset is guaranteed to affect only the selected lamp.
- [ ] E. Deleting the prefab asset is a reasonable way to isolate the selected lamp.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The request identifies one placed lamp.
- B: That checks the stated preservation requirement.
- C: Applying a change can propagate it to other instances.
- D: Other objects may reference the same material.
- E: That damages the reusable asset rather than scopes the edit.

**Source:** Applied: prefab instance scope

## MA-unity.6

An agent changes a Unity script, then tries to configure a component whose new serialized field is missing. The editor reports compilation errors. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The compilation errors should be investigated before assuming the new field is available.
- [ ] B. Hiding console errors makes the new component definition usable.
- [ ] C. The agent should inspect the component after the editor has successfully processed the script.
- [ ] D. The text file being saved is weaker evidence than successful compilation.
- [ ] E. Repeating the field assignment repairs a compiler error in the script.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The revised script may not have loaded successfully.
- B: Display filtering does not fix compilation.
- C: That checks the actual loaded state.
- D: Saving bytes does not validate code.
- E: The cause must be corrected in the code or dependencies.

**Source:** Troubleshooting: script compilation

## MA-unity.7

A Unity tool reports a successful scene edit. After closing and reopening the project, the change is missing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The missing change proves that the language model forgot the scene.
- [ ] B. The agent should verify which scene and project were actually saved.
- [ ] C. Reopening the saved scene is a useful persistence check.
- [ ] D. The success result may describe a completed mutation without describing a completed save.
- [ ] E. The investigation should distinguish in-memory state from saved scene state.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Project persistence is an editor/storage issue, not conversational memory.
- B: Saving the wrong target does not persist the intended change.
- C: It tests that the change survives reload.
- D: The tool contract determines what success means.
- E: An edit can exist in memory without durable persistence.

**Source:** Applied: scene persistence

## MA-unity.8

A texture file has been copied into a Unity project. The editor is still importing it when an agent tries to assign it to a material. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent should wait for the import result before relying on the asset.
- [ ] B. Import errors are relevant evidence if the asset remains unavailable.
- [ ] C. A file's presence proves that the editor has finished processing it.
- [ ] D. Assigning a placeholder proves that the requested texture was imported.
- [ ] E. Creating more copies is the appropriate way to wait for import completion.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A copied file may not yet be an available engine asset.
- B: The processing step can fail independently of file copying.
- C: Filesystem presence and engine readiness are different states.
- D: A placeholder does not verify the requested asset.
- E: Duplicates add ambiguity rather than resolve readiness.

**Source:** Applied: import readiness

## MA-unity.9

A hypothetical Unity placement tool accepts local position. A parent object is translated ten units along an axis and has identity rotation and scale. Its child is assigned local position zero. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Renaming the child changes the coordinate space used by the tool.
- [ ] B. Local position zero puts the child at the world origin despite the parent translation.
- [ ] C. The child lies at the parent's world position.
- [ ] D. A world-origin requirement needs a conversion or a tool that accepts world coordinates.
- [ ] E. Reading the world transform verifies the intended placement.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Names do not change transform semantics.
- B: The parent's transform contributes to world position.
- C: Zero local offset places it at the parent origin.
- D: The tool's coordinate contract matters.
- E: The requested outcome is expressed in world space.

**Source:** Applied: local and world transforms

## MA-unity.10

A Unity agent changes one wall's material color. Several other walls change too. The walls reference the same material asset. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A screenshot of only the selected wall establishes that the scope was correct.
- [ ] B. The intended scope should determine whether to edit the shared asset or use an appropriate per-object solution.
- [ ] C. The additional color changes establish an MCP transport fault.
- [ ] D. The shared reference explains why an asset edit can affect several walls.
- [ ] E. Moving the selected wall to a different position makes its material reference independent.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: It does not show unintended changes elsewhere.
- B: The desired propagation is a design choice.
- C: Shared asset semantics already explain them.
- D: They consume the same material definition.
- E: Transform changes do not clone materials.

**Source:** Troubleshooting: shared material mutation

## MA-unity.11

A team proposes a hypothetical tool that changes the intensity of one identified light instead of granting an agent a general script evaluator. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reporting the previous and resulting intensity supports review and recovery.
- [ ] B. A narrow tool's existence proves its implementation has no bugs.
- [ ] C. A free-text request to be careful provides the same enforcement as argument validation.
- [ ] D. The tool still needs authorization to modify the project.
- [ ] E. Validating light identity and an allowed intensity range narrows the operation.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The record describes the actual change.
- B: Implementation quality still needs verification.
- C: Instruction following is not a technical validation boundary.
- D: A narrow operation remains a write.
- E: The tool can enforce a specific contract.

**Source:** Advanced: narrow Unity tool design

## MA-unity.12

A team receives a playable prototype from an AI-assisted game-creation workflow and wants to use it as the basis for a Unity release. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The team's target-device performance budget remains relevant.
- [ ] B. The ability to create a prototype establishes support for the team's required export workflow.
- [ ] C. The prototype should be tested against explicit controls and win/lose conditions.
- [ ] D. A convincing demonstration proves the project can be maintained by the team.
- [ ] E. The team needs evidence about asset rights and dependencies.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A preview does not establish release performance.
- B: Export and integration capabilities require separate verification.
- C: Being playable does not establish requirement coverage.
- D: Maintainability requires inspecting and working with the deliverable.
- E: Generated output does not settle provenance or distribution conditions.

**Source:** Advanced: evaluating a generated prototype
