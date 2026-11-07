# MCP fundamentals

## MA-mcp.1

A studio connects a language-model assistant to a scene editor through Model Context Protocol (MCP). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. MCP is the model that predicts the next words in the assistant's reply.
- [ ] B. Installing MCP trains the assistant on the project's assets.
- [ ] C. MCP supplies the engine's rendering pipeline.
- [ ] D. The MCP server replaces the project's gameplay scripts.
- [ ] E. MCP defines an interface through which the assistant application can access external capabilities.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Inference belongs to the language model, not the integration protocol.
- B: Connecting a service does not update model weights.
- C: Rendering remains an engine responsibility.
- D: The server exposes operations; gameplay still needs its implementation.
- E: The protocol connects applications to tools and context.

**Source:** Foundational: protocol versus model

## MA-mcp.2

An assistant application contains an MCP connector that calls a service exposing a game editor. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The connector plays the client role.
- [ ] B. The assistant application plays the host role.
- [ ] C. The user-written gameplay character is the MCP client in this arrangement.
- [ ] D. The editor-facing service plays the server role.
- [ ] E. The server role implies that the service runs in a cloud data center.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The client communicates with the MCP server on the host's behalf.
- B: The host contains the user interaction and integration machinery.
- C: The client is the integration connector, not an in-game character.
- D: It supplies the external capabilities.
- E: A server can be a local process.

**Source:** Foundational: host, client and server

## MA-mcp.3

A hypothetical editor server exposes a spawn operation, a readable scene manifest and a reusable review template. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The spawn operation fits the tool primitive.
- [ ] B. Reading the manifest can inform a later spawn request.
- [ ] C. The review template fits the prompt primitive.
- [ ] D. The scene manifest fits a resource if the server exposes it as URI-addressed content.
- [ ] E. Retrieving the review template is evidence that the scene passed review.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: A tool invokes an operation with inputs.
- B: Context can guide a subsequent action.
- C: Prompts provide reusable messages or workflows.
- D: Resources supply context that a client can read.
- E: Obtaining instructions does not execute or satisfy them.

**Source:** Foundational: tools, resources and prompts

## MA-mcp.4

An agent knows a tool name from a tutorial, but the connected editor does not advertise that tool. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The missing tool proves that the scene file is corrupt.
- [ ] B. A familiar tutorial name is a sufficient substitute for the live tool schema.
- [ ] C. The agent should inspect the connected server's available tools before constructing a call.
- [ ] D. Renaming a scene object to the missing tool name registers that tool.
- [ ] E. The installed integration may expose a different operation for the same goal.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Tool availability and scene integrity are different questions.
- B: Names and arguments may differ across integrations.
- C: Discovery grounds the operation in the actual integration.
- D: Object names do not implement server operations.
- E: Tool catalogs are implementation-specific.

**Source:** Applied: tool discovery

## MA-mcp.5

A hypothetical move tool accepts an object identifier and a numeric distance. The schema does not specify units or coordinate space. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent needs the tool contract or an inspected example to determine coordinate space.
- [ ] B. A schema-valid request establishes that the target object is the intended one.
- [ ] C. Reading back the final transform checks the effect of the operation.
- [ ] D. Using a number proves that the intended unit was used.
- [ ] E. A numeric argument can pass schema validation while expressing the wrong distance.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Local and world coordinates can produce different changes.
- B: Identity must be checked separately.
- C: Observed state can reveal semantic mistakes.
- D: The same number may mean meters, centimeters or another unit.
- E: Type correctness does not establish units.

**Source:** Applied: schema versus semantics

## MA-mcp.6

An MCP trace contains JSON-RPC requests and replies while several editor operations are being investigated. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A notification's lack of a reply is sufficient evidence of a broken connection.
- [ ] B. A JSON-RPC notification has no request identifier and receives no JSON-RPC response.
- [ ] C. The identifier is the index of the target Actor in the level.
- [ ] D. A response identifier associates a reply with its request.
- [ ] E. A syntactically valid JSON message proves that the requested edit succeeded.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: No reply is expected for a notification.
- B: Notifications do not provide request-response acknowledgment.
- C: Protocol correlation is separate from engine identity.
- D: Correlation uses the request's identifier.
- E: Message syntax says nothing about the operation's result.

**Source:** Foundational: JSON-RPC correlation

## MA-mcp.7

Two integrations carry MCP messages using stdio and Streamable HTTP respectively. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. HTTP can be used for a service on the same machine.
- [ ] B. A transport fault can prevent a valid tool request from reaching the editor.
- [ ] C. Changing the transport translates Unity components into Unreal components.
- [ ] D. Stdio can connect a client to a subprocess through standard streams.
- [ ] E. The transport and the engine operation are separate layers.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: HTTP does not imply a remote cloud service.
- B: Delivery can fail before execution.
- C: A transport does not convert engine data models.
- D: It is a process communication transport.
- E: Message delivery does not define scene-editing semantics.

**Source:** Foundational: transports

## MA-mcp.8

A hypothetical tool reports that its request was received but the named scene object could not be found. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Changing the network port repairs an obsolete object identifier.
- [ ] B. Reinstalling the model is the first diagnosis supported by this evidence.
- [ ] C. The next investigation should include object identity and current scene state.
- [ ] D. Receiving a structured reply means that the object was successfully modified.
- [ ] E. A successful network exchange can carry an unsuccessful editor operation.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Port selection does not restore object identity.
- B: There is no evidence of a model installation fault.
- C: The error concerns the operation's target.
- D: The reply explicitly reports a failure.
- E: Transport success and domain success differ.

**Source:** Troubleshooting: layered errors

## MA-mcp.9

A client and server were developed against different MCP revisions. Both claim to support MCP, but their first exchange fails. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The applicable specification and implementation documentation should guide discovery and setup.
- [ ] B. The supported protocol revisions are relevant diagnostic evidence.
- [ ] C. A small read-only interoperability check is useful before authorizing scene edits.
- [ ] D. A tutorial's initialization sequence is sufficient evidence of the current protocol's requirements.
- [ ] E. The MCP name establishes that the two implementations support the same revision.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Lifecycle details should be checked for the deployed revision.
- B: The same protocol family can have incompatible revision requirements.
- C: It isolates communication without risking scene changes.
- D: Protocol lifecycle rules evolve.
- E: A product label is not a compatibility guarantee.

**Source:** Advanced: protocol compatibility

## MA-mcp.10

A resource returned a list of lights. A designer then deleted one of those lights before the agent prepared its edit. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The earlier list is a snapshot that may now be stale.
- [ ] B. Resource content is locked against later editor changes once read.
- [ ] C. Reusing the old list proves that the deleted light still exists.
- [ ] D. The agent should resolve the target again before changing it.
- [ ] E. The deletion changes the historical resource response into a protocol error.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Editor changes can invalidate read context.
- B: Reading context does not freeze the scene.
- C: A cached observation is not current evidence.
- D: A fresh lookup checks continued existence and identity.
- E: The earlier response can have been valid when produced.

**Source:** Applied: context freshness

## MA-mcp.11

Two engine servers both expose a tool described as creating an object. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An identical tool description proves identical side effects.
- [ ] B. A reusable agent can share high-level intent while using different adapters.
- [ ] C. Their created objects may have different engine-specific semantics.
- [ ] D. A shared protocol makes their asset files mutually loadable.
- [ ] E. Their argument schemas may differ.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Contracts and observed behavior must also be checked.
- B: Portability can live above engine-specific operations.
- C: An Actor and a GameObject are not interchangeable serialized objects.
- D: Asset formats are outside that guarantee.
- E: MCP standardizes communication rather than a universal game-editor API.

**Source:** Advanced: interoperability boundaries

## MA-mcp.12

A scene-building agent may inspect, edit and test repeatedly. Its operator sets a maximum of ten edit attempts and requires it to report unresolved failures. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reaching ten attempts establishes that the scene is correct.
- [ ] B. The attempt limit bounds a possible repair loop.
- [ ] C. The agent should compare observed state with the requested outcome after an edit.
- [ ] D. Preserving failure evidence helps a human decide the next step.
- [ ] E. Removing a failing requirement is equivalent to satisfying it.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The limit is a stopping condition, not an acceptance condition.
- B: Repeated unsuccessful edits cannot continue indefinitely under that policy.
- C: Tool invocation is only one step in verification.
- D: Unresolved symptoms are useful diagnostic context.
- E: Changing the target hides failure rather than fixes it.

**Source:** Advanced: bounded agent execution
