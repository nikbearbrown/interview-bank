# Unity, Spark and agent workflows

## ES-unity.1

A teammate says, 'Unity Spark is Unity's MCP, so installing an MCP server gives us Spark.' Correct the reasoning and propose a small evaluation of each workflow without assuming access to either product.

**Points:** 5

**Rubric (1 point each):**

1. Describes Spark as a browser-based game-creation experience based on the supplied product distinction.
2. Describes an MCP integration as an interface exposing editor capabilities to a client.
3. Explains why installing an interface does not establish access to a separate product experience.
4. Proposes a bounded creation task with observable gameplay acceptance criteria for evaluating Spark if access is available.
5. Proposes discovery, a reversible editor edit and read-back verification for evaluating an installed MCP integration.

**Source:** Foundational: distinguish Unity products

## ES-unity.2

A Unity team's vendor documentation replaces its older in-editor MCP server with a CLI-hosted server. Plan the migration while preserving project work. Do not give version numbers or menu paths.

**Points:** 5

**Rubric (1 point each):**

1. Inventories the installed editor integration and client configuration to establish that the migration applies.
2. Creates a recoverable project/configuration checkpoint and selects a small test project.
3. Follows the replacement's documented setup and checks the actual advertised tool contracts.
4. Verifies project targeting, a read-only query and a reversible edit with persistence before switching normal work.
5. Records compatibility findings and a rollback route rather than treating the new connection as sufficient acceptance.

**Source:** Applied: Unity integration migration

## ES-unity.3

Write a precise instruction for a Unity agent to add three instances of an existing checkpoint prefab to a specified scene. The positions are world-space coordinates supplied by the designer. Existing prefab behavior must be preserved.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the project, destination scene and existing prefab asset without relying on display name alone.
2. Requires three distinct instances at the supplied world-space positions with coordinate units made explicit.
3. Preserves the prefab asset and existing instance behavior unless a stated requirement needs an approved change.
4. Requires checking instance count, transforms and checkpoint activation through normal gameplay interaction.
5. Requires saving and reopening the scene and reporting the changed assets plus actual validation evidence.

**Source:** Applied: say it to the Unity agent

## ES-unity.4

A Unity script edit introduces a field, but the agent cannot set it through the editor bridge. The editor shows compilation errors and the old component layout. Explain a repair and verification sequence.

**Points:** 5

**Rubric (1 point each):**

1. Treats compilation failure as a reason the edited script may not be loaded into the editor.
2. Reads the compiler diagnostics and fixes the relevant code or dependency issue without suppressing the error.
3. Waits for successful compilation/reload before inspecting the actual component layout.
4. Checks that the field belongs to the intended component and is exposed through the supported tool contract.
5. Sets the field, reads it back and tests the intended behavior rather than concluding from file contents alone.

**Source:** Troubleshooting: missing serialized field

## ES-unity.5

A Unity scene has twenty instances of a lamp prefab sharing a material. A designer wants one lamp blue. Explain how an agent should establish the edit scope, avoid unintended propagation and prove the result.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the requested lamp instance unambiguously.
2. Distinguishes an instance change from editing the prefab definition or shared material asset.
3. Chooses a justified per-instance material/property solution supported by the project's rendering setup.
4. Checks the requested lamp and representative unchanged lamps, including the shared asset's state.
5. Saves and reloads the intended changes and records any new asset or override for review.

**Source:** Applied: one lamp versus a prefab

## ES-unity.6

A Unity agent imports a mesh, creates a prefab and places instances. Import succeeds, prefab creation fails, and no instances have yet been created. Design recovery without rerunning the entire sequence blindly.

**Points:** 5

**Rubric (1 point each):**

1. Records each step's actual result and identifies prefab creation as the first failed stage.
2. Inspects the imported asset and error details before choosing a targeted correction.
3. Reuses the verified import rather than generating duplicate assets on retry.
4. Creates and validates the prefab before placing instances, using stable identifiers or duplicate detection.
5. Verifies the final asset/instance counts and persistence while removing only artifacts known to belong to the failed attempt.

**Source:** Advanced: editor workflow recovery

## ES-unity.7

An AI-assisted prototype looks impressive in a browser demo. Your team needs an accessible game with keyboard controls, a save system and a defined target platform. Specify an acceptance plan before adopting the prototype.

**Points:** 5

**Rubric (1 point each):**

1. Turns the controls, accessibility behavior and save/load requirements into observable checks.
2. Verifies the available export/build workflow and tests the required target rather than inferring it from the browser demo.
3. Inspects asset provenance, dependencies and permissions relevant to the team's intended use without assuming generated means unrestricted.
4. Measures performance and functional behavior under a representative play session, including restart and save recovery.
5. Assesses whether the team can inspect, modify and maintain the delivered project and records unmet requirements.

**Source:** Advanced: prototype acceptance

## ES-unity.8

A team can expose either a general script evaluator or three narrow tools for inspecting lights, setting one light's intensity and saving a specified scene. Compare the designs for an automated lighting task.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a general evaluator is flexible but can perform much broader actions than lighting edits.
2. Shows how narrow tools validate project/object identity, allowed values and write scope.
3. Acknowledges that narrow tools may need extension when a legitimate operation is missing rather than inventing support.
4. Defines evidence such as old/new intensity, affected object identifiers and save results.
5. Chooses a justified design with independent validation and a recovery strategy for unexpected changes.

**Source:** Advanced: designing a Unity bridge
