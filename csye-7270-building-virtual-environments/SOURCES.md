# MCP and agent workflow sources

Research checked **November 3, 2026**. These are instructor notes, not additional facts students must memorize. Question wording and answer keys are original; the linked documentation supports protocol definitions and engine distinctions. Hypothetical operations, tool contracts, numeric examples and recovery scenarios are explicitly supplied in the questions. The existing `source` field remains a topic label; the mappings below provide external references without changing the JSON schema.

## Current product distinctions

- **Unity Spark** is Unity's browser-based game-creation experience, announced with Google. Its public product page currently presents a waitlist/coming-soon offering. It is not the name of the MCP protocol or a synonym for installing an editor bridge. Access and supported export workflows should be checked before assigning a practical exercise. [Unity announcement](https://unity.com/blog/why-we-built-unity-spark), [Unity Spark product page](https://unity.com/spark).
- **Official Unity MCP** now has a migration distinction: Unity deprecated the MCP server in `com.unity.ai.assistant`; the CLI's `unity mcp` server, built on Unity Pipeline, replaces it. The CLI also offers direct editor commands. Unity says the deprecation does not apply to third-party MCP packages. Do not describe an arbitrary community package as Unity's official integration. [Unity migration documentation](https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli).
- **Epic's Unreal MCP** is documented as experimental in the Unreal Engine 5.8 documentation. It runs inside the editor, exposes separately supplied toolsets and documents local HTTP access, same-machine restrictions and no remote authentication layer. Tool invocations are serialized on the game thread. Availability is not a promise of production readiness or permission to expose the endpoint remotely. [Epic's Unreal MCP documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor).
- **MCP** is the integration protocol, not a language model, a game engine or a requirement to run inference in the cloud. The official latest specification resolved to the **2026-07-28** revision during research. Its lifecycle differs from older revisions; older engine documentation can still describe an initialization handshake. Questions therefore test compatibility investigation rather than claiming one initialization sequence applies to every deployment. [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28), [transport specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports).

These details are dated context. Recheck vendor documentation and the deployed protocol revision before turning an assessment scenario into a setup guide. The questions avoid testing the release numbers, beta status, commands or port defaults above.

## Reference catalog

| Code | Primary source | Use in this expansion |
|---|---|---|
| P1 | [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) | Host/client/server roles; protocol versus model; tools, resources and prompts. |
| P2 | [MCP tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | Discovery, tool schemas and the distinction between a call and its result. |
| P3 | [MCP resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) | URI-addressed context; a read does not freeze subsequent editor state. |
| P4 | [MCP transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) | Stdio and Streamable HTTP; transport versus operation semantics. |
| P5 | [JSON-RPC specification](https://www.jsonrpc.org/specification) | Request/response correlation and notification semantics. |
| S1 | [MCP security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | Local-server risks and security boundary analysis. |
| S2 | [MCP project security policy](https://github.com/modelcontextprotocol/modelcontextprotocol/security) | Stdio transport is not a sandbox; deployment controls enforce isolation. |
| U1 | [Unity Spark announcement](https://unity.com/blog/why-we-built-unity-spark) and [product page](https://unity.com/spark) | Product role and distinction from an editor integration. |
| U2 | [Unity CLI replacement for the in-editor server](https://docs.unity.com/en-us/unity-cli/replace-mcp-server-unity-cli) | Current official migration context and direct-command/MCP alternatives. |
| U3 | [Unity prefab instance overrides](https://docs.unity.com/en-us/engine/6000.7/manual/working-with-gameobjects/prefabs/override/prefab-instance-overrides) | Instance scope versus prefab changes. The referenced page is beta documentation; questions use the established override concept, not beta-specific collection behavior. |
| U4 | [Unity Test Framework guide](https://unity.com/how-to/automated-tests-unity-test-framework) | Editor/play testing and observed behavior; installation/version instructions are not assessment content. |
| E1 | [Unreal MCP](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor) | Editor integration, separate toolsets, local deployment and serialized operations. |
| E2 | [Blueprints visual scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) | Blueprint gameplay logic and its distinction from agent inference. |
| E3 | [Unreal automation framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine) | Functional and other engine testing; running a test versus obtaining evidence. |

## Question mappings

Each range includes both endpoints. References establish the underlying concepts; scenario-specific acceptance criteria and deductions are supplied by the original question, not claimed as vendor guarantees.

| Set and question IDs | References and grounding |
|---|---|
| MA-mcp.1-3; ES-mcp.1-2 | P1-P3: roles and primitives. |
| MA-mcp.4-5, .8, .11-12; ES-mcp.3-4, .8 | P1-P2: discovery/contracts; original error, semantic-validation and bounded-workflow scenarios. |
| MA-mcp.6 | P5: correlation and notifications. |
| MA-mcp.7, .9; ES-mcp.5-6 | P1, P4: deployment and revision compatibility; original diagnostic plans. |
| MA-mcp.10; ES-mcp.7 | P3: readable context; original stale-state and concurrent-edit scenarios. |
| MA-unity.1; ES-unity.1 | U1, P1: Spark versus protocol integration. |
| MA-unity.2-3; ES-unity.2 | U2: migration and interface choice, with the relevant premise supplied in the stem. |
| MA-unity.4-5, .9; ES-unity.3, .5 | U3: scoped object edits; original project-identity and explicitly defined transform scenarios. |
| MA-unity.6-8, .10-11; ES-unity.4, .6, .8 | P2, U3-U4: original compilation, persistence, import, shared-reference and contract-design scenarios. |
| MA-unity.12; ES-unity.7 | U1, U4: original prototype-acceptance criteria; no unsupported Spark export claim. |
| MA-unreal.1-2, .6-7; ES-unreal.1-3, .7 | E1-E2: editor role and integration boundaries; operational premises supplied in stems. |
| MA-unreal.3-5, .8, .10-12; ES-unreal.4, .6, .8 | E2-E3: original instance, collision, persistence, shared-reference and recovery scenarios. |
| MA-unreal.9; ES-unreal.5 | E3, P2: test evidence; asynchronous job behavior is explicitly hypothetical. |
| MA-security.1-12; ES-security.1-8 | P1, S1-S2: original threat-model, authorization, injection, filesystem, disclosure and audit scenarios. Their controls are design recommendations, not claims that MCP automatically enforces them. |
| MA-verification.1-5, .8, .10-12; ES-verification.1-2, .4, .7-8 | U4, E3, P2: original test-oracle, failure-recovery and evidence scenarios. |
| MA-verification.6, .9; ES-verification.3, .5 | P1-P2, U3, E2: original cross-engine requirements and adapter comparison; units are defined by the hypothetical contracts. |
| MA-verification.7; ES-verification.6 | Original arithmetic: milliseconds per frame = 1000 / FPS; 2.5 meters = 250 centimeters for MA-verification.6. |

## Validation scope

The additions contain **60 multiple-answer questions and 40 essays**, all using the existing five-point format. The repository's format checker and JSON builder are the required commands. Supplemental checks compare generated questions with the Markdown, enforce unique IDs and nonempty keys/rubrics, preserve all 425 original question objects, check section metadata and recompute the numeric scenarios. A repeat build is checked for byte-identical output, and the diff is checked for whitespace errors and unintended changes.

This is a content and export validation, not a live Unity/Unreal integration test. The expansion has not undergone the original pool's independent blind-answer review. Its answer keys and rubrics were reviewed during authoring, with product-specific facts checked against the primary sources above.
