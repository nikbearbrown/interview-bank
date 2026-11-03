# MCP fundamentals

## ES-mcp.1

Explain Model Context Protocol to a game designer who thinks it is a cloud model that writes the game. Use an editor example to distinguish the host, client and server.

**Points:** 5

**Rubric (1 point each):**

1. Defines MCP as an integration protocol connecting an AI application with external context and capabilities.
2. Identifies the host as the assistant application and the client as its protocol connector.
3. Identifies the server as the service exposing editor operations, with a concrete example such as inspecting a scene.
4. Separates language-model inference from tool execution and engine gameplay execution.
5. Explains that local or remote deployment is a configuration choice rather than a requirement to use cloud inference.

**Source:** Foundational: explain MCP

## ES-mcp.2

Design an MCP interface for a hypothetical editor that must expose a scene inventory, a create-light operation and a reusable lighting-review checklist. Explain how the agent should use them together.

**Points:** 5

**Rubric (1 point each):**

1. Maps the inventory to a readable resource with an identifier, or justifies a query tool when dynamic arguments are required.
2. Maps light creation to a tool with explicit target scene and meaningful parameters.
3. Maps the reusable checklist to a prompt template rather than claiming retrieval performs a review.
4. Describes reading scene context before deciding where and how to create a light.
5. Requires inspecting and testing the resulting lighting against stated criteria after the edit.

**Source:** Foundational: choose the primitive

## ES-mcp.3

Specify a hypothetical move-object tool for an agent. The editor contains several objects with the same display name. Describe the contract without relying on a particular engine API.

**Points:** 5

**Rubric (1 point each):**

1. Requires an unambiguous object identifier and checks the intended project and scene.
2. Defines position units, coordinate space and whether the input is an offset or an absolute destination.
3. Specifies validation for missing objects and invalid or out-of-range values before mutation.
4. Returns structured evidence of the affected object and its resulting transform, with explicit failure information.
5. Describes a stale-state check or equivalent precondition plus a way to recover the prior transform.

**Source:** Applied: define a safe tool contract

## ES-mcp.4

A tool call reaches an MCP server, but no object appears in the editor. Propose a diagnostic sequence that separates message delivery, argument validation, engine execution and verification.

**Points:** 5

**Rubric (1 point each):**

1. Checks the matching request and response rather than inferring success from connection status.
2. Checks the advertised tool and argument contract, including identity, units and supported operation.
3. Inspects reported tool failure and relevant editor logs for execution errors.
4. Checks the correct project, scene and editor state, including whether the result exists but is hidden or unsaved.
5. Rereads the actual scene and records evidence before choosing a targeted repair or retry.

**Source:** Troubleshooting: trace a failed call

## ES-mcp.5

A studio wants a cloud-hosted language model to help edit a Unity project on a workstation through a local MCP service. Describe the data flow and two separate boundaries the studio must manage.

**Points:** 5

**Rubric (1 point each):**

1. Places model inference remotely while placing the editor and its MCP-facing integration locally.
2. Traces user intent through the host/client to an editor tool and the resulting observation back to the host.
3. Explains that project context sent to the remote model crosses a data-disclosure boundary.
4. Explains that invoking a local editing tool crosses an action/permission boundary distinct from remote inference.
5. Proposes concrete controls for both boundaries, such as context filtering and narrowly scoped local tools.

**Source:** Applied: design a deployment

## ES-mcp.6

An older editor MCP plugin works with one client but fails with another. Plan an investigation without assuming a particular protocol revision's initialization sequence.

**Points:** 5

**Rubric (1 point each):**

1. Records client, plugin and supported protocol revisions for both working and failing combinations.
2. Consults the specification and vendor documentation applicable to those revisions.
3. Compares a minimal read-only trace to distinguish transport, discovery and capability mismatches.
4. Uses a documented compatible configuration or upgrade path and retests in an isolated project.
5. Records the resulting compatibility requirements and avoids inventing unsupported methods to force a connection.

**Source:** Advanced: compatibility investigation

## ES-mcp.7

A human and an agent are editing the same level. The agent plans changes from a scene inventory read several minutes earlier. Design a workflow that prevents overwriting the human's recent work.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the inventory as a potentially stale observation rather than a current authority.
2. Resolves object identities and compares relevant current state with the planning snapshot before mutation.
3. Uses an available revision precondition, lock or coordinated editing window to detect or avoid conflicting writes.
4. Applies a small bounded change and verifies its result without resetting unrelated edits.
5. On conflict, stops or replans from fresh state and preserves a recovery record rather than silently overwriting.

**Source:** Advanced: stale context and concurrent editing

## ES-mcp.8

Design a common agent workflow for placing checkpoints in Unity and Unreal. Explain what belongs in the shared layer and what must remain engine-specific.

**Points:** 5

**Rubric (1 point each):**

1. Defines shared intent with observable requirements such as checkpoint count, locations and activation behavior.
2. Places discovery, planning, verification and failure reporting in a reusable workflow.
3. Keeps object creation, asset references and component configuration in engine-specific adapters.
4. Requires each adapter to expose its argument semantics and supported operations rather than reusing tool names blindly.
5. Verifies gameplay behavior independently in each engine and does not equate protocol compatibility with asset compatibility.

**Source:** Advanced: portable editor integration
