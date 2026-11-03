# Unreal and agent workflows

## ES-unreal.1

Explain how an Unreal editor MCP server can help build an NPC without being that NPC's runtime intelligence. Give a plausible workflow and its limits.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the MCP server as an editor-facing integration exposing available operations.
2. Separates the assistant's development-time decisions from the NPC's packaged runtime behavior.
3. Describes creating or configuring the relevant Actor, components or gameplay logic through supported operations.
4. Requires compiling or validating the changed assets and testing the NPC during play.
5. Explains that an editor connection alone does not establish runtime behavior, packaged compatibility or production readiness.

**Source:** Foundational: Unreal MCP and game AI

## ES-unreal.2

An Unreal MCP endpoint is reachable, but its expected scene toolset is absent. The integration uses separately enabled toolsets. Plan a diagnosis that avoids changing level content until the integration is understood.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes successful transport communication from availability of the needed tool implementation.
2. Checks the enabled toolsets and applicable integration documentation.
3. Refreshes or rechecks the catalog using the integration's supported workflow.
4. Verifies the client targets the intended editor/project and uses a supported protocol configuration.
5. Runs a minimal read-only operation once available and records any unresolved capability gap instead of inventing a tool name.

**Source:** Troubleshooting: endpoint but no tools

## ES-unreal.3

Write an instruction for an Unreal agent to place five existing checkpoint Blueprint Actors in a specified level. The designer supplies transforms and wants the Blueprint class left unchanged.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the project, level and Blueprint asset unambiguously.
2. Specifies five distinct instances with the supplied transforms and explicit coordinate semantics.
3. Limits edits to the placed instances and preserves the Blueprint class definition.
4. Requires count/transform inspection plus an activation test through representative gameplay interaction.
5. Requires saving the affected content, reopening it and reporting changed packages and validation results.

**Source:** Applied: say it to the Unreal agent

## ES-unreal.4

A Blueprint door compiles, but it opens without a key and sometimes opens twice. Explain how to investigate the logic and verify a repair.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes compilation success from correctness of the gameplay conditions.
2. Inspects the key check and event path, including possible duplicate bindings or repeated overlap events.
3. Uses a minimal reproduction with no-key and has-key cases and records the observed transitions.
4. Repairs the condition and guards repeated activation according to the intended door behavior.
5. Runs regression cases for no key, one valid activation and repeated interaction without weakening the requirements.

**Source:** Troubleshooting: compiled but wrong Blueprint

## ES-unreal.5

An Unreal test tool returns a job identifier before the test finishes. Design an agent workflow that reports the pressure-plate test accurately and avoids launching duplicates.

**Points:** 5

**Rubric (1 point each):**

1. Treats the initial result as accepted or running rather than passed.
2. Stores the job identifier and uses the tool's documented status/result mechanism.
3. Waits or polls within a bounded policy while keeping a distinction between running, failed, completed and unknown states.
4. Obtains the final assertions and diagnostics before claiming success.
5. On timeout or lost connection, checks the existing job before retrying and reports unresolved status honestly.

**Source:** Advanced: asynchronous result handling

## ES-unreal.6

An Unreal tool is replacing ten placeholder Actors with props. It replaces four, fails on the fifth and stops. Design recovery that preserves the original transforms and avoids duplicate props.

**Points:** 5

**Rubric (1 point each):**

1. Records the identities and outcomes of the four completed replacements and the failed/remaining targets.
2. Inspects the failure and current scene state before changing anything else.
3. Uses recorded transforms and target identities to verify completed work and prevent duplicate replacement.
4. Chooses either a bounded resume or a rollback based on available recovery support, explaining the choice.
5. Verifies all ten final placements or the restored originals and reports any remaining partial state.

**Source:** Advanced: batch replacement recovery

## ES-unreal.7

An Unreal editor integration is documented for same-machine use with no remote authentication layer. A team wants to use it from a remote workstation. Explain why port forwarding is not a complete solution and propose a responsible evaluation.

**Points:** 5

**Rubric (1 point each):**

1. Explains that exposing the endpoint broadens who can reach powerful editor operations.
2. Distinguishes network reachability from authentication and per-operation authorization.
3. Checks documented supported deployment options rather than assuming a local service is ready for remote exposure.
4. Proposes a local client or a deliberately designed access-controlled remote arrangement with restricted reachability.
5. Tests with a disposable project and verifies identities, allowed operations and audit evidence before production use.

**Source:** Applied: local service deployment

## ES-unreal.8

An Unreal agent changes a light during play, and the value reverts afterward. The request was to deliver a persistent level change. Explain the likely state confusion and a verifiable repair.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes a runtime object instance from saved authoring data.
2. Checks which world/object the tool actually targeted rather than assuming the revert is a transport failure.
3. Applies the intended value to the correct authoring target through a supported edit operation.
4. Saves the affected level or asset and reopens it to verify persistence.
5. Runs a play check afterward and considers runtime logic that might intentionally override the authored value.

**Source:** Advanced: authoring versus runtime state
