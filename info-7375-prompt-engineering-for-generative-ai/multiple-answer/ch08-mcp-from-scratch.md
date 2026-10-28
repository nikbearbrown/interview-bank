# Chapter 8: MCP from scratch

## MA-ch08.1

Check each statement that is true about two servers that both advertise a tool called `lookup`, both return valid JSON-RPC messages and copy request identifiers correctly, but only one of which writes files as a side effect. Each statement is worth 1 point (5 points total).

- [ ] A. The file-writing server could be recognized by how it copies request identifiers.
- [ ] B. Protocol syntax cannot tell the two servers apart.
- [ ] C. Interoperability answers whether components can exchange messages they understand.
- [ ] D. A clean handshake settles whether this capability should run in this task.
- [ ] E. Authorization answers whether components can exchange messages they understand.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Both servers copy identifiers correctly.
- B: Syntax cannot show that they deserve different permissions.
- C: That is the chapter's definition.
- D: It settles the first question and is silent on the second.
- E: That is interoperability; authorization asks whether a capability should run in this task.

**Source:** Chapter 8 - MCP from scratch (opening)

## MA-ch08.2

Check each statement that is true about Claude being handed only the tool listing for two competing servers. Each statement is worth 1 point (5 points total).

- [ ] A. A tool description is a sentence the server wrote about itself.
- [ ] B. Once Claude has compared the two descriptions, the decision to connect becomes Claude's.
- [ ] C. Under the Drive job, Claude reads the transcript and lists every discrepancy while you keep the decision to connect.
- [ ] D. What Claude lacks is skill with JSON.
- [ ] E. Claude has no standpoint on whose data sits behind the server, what a stray file write would cost, or who maintains it.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The description is the server's own testimony.
- B: The chapter says the decision is yours.
- C: That is how the chapter divides the third job.
- D: It lacks a standpoint on whether this server belongs in the task.
- E: The listing supplies none of these facts.

**Source:** Chapter 8 - MCP from scratch (opening)

## MA-ch08.3

Check each statement that is true about the chapter's teaching server. Each statement is worth 1 point (5 points total).

- [ ] A. It implements initialization, an initialized notification, tool listing, and one read-only lookup.
- [ ] B. It keeps two Boolean state variables.
- [ ] C. It rejects a tool request made too early.
- [ ] D. It also advertises a write-capable tool alongside `lookup`.
- [ ] E. It separates protocol errors from a tool result whose `isError` field is true.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is the whole feature list.
- B: They are `initialized` and `ready`.
- C: Tool operations are refused until the server is ready.
- D: Its only tool is the read-only lookup; the write-capable server is hypothetical.
- E: The two are distinct layers.

**Source:** Chapter 8 - MCP from scratch (opening)

## MA-ch08.4

Check each statement that is true about the four recorded observations of the local Python server. Each statement is worth 1 point (5 points total).

- [ ] A. Looking up an unknown record produces a JSON-RPC error.
- [ ] B. Listing tools before initialization returns an error.
- [ ] C. An initialize request returns protocol version `2025-11-25`.
- [ ] D. They are executed observations of this server, not claims about MCP generally.
- [ ] E. A valid initialized notification returns no response.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It produces a tool result with `isError: true`.
- B: That is the first recorded observation.
- C: That is the second recorded observation.
- D: The chapter limits the claim to this server.
- E: That is the third recorded observation.

**Source:** Chapter 8 - MCP from scratch (opening)

## MA-ch08.5

Check each statement that is true about the chapter's treatment of the version the server returns. Each statement is worth 1 point (5 points total).

- [ ] A. A fixed fallback version is, by itself, a violation of the specification.
- [ ] B. When a server returns a different version, the server decides whether the client can continue.
- [ ] C. Under the versioned lifecycle specification, a server may return another supported version when the requested one is unsupported.
- [ ] D. The teaching server is a full conformance implementation of the lifecycle.
- [ ] E. The server returns its one supported version without inspecting the client's requested version.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The chapter says it is not, by itself, a violation.
- B: The client makes that decision.
- C: The client then decides whether it can continue.
- D: It remains a teaching subset.
- E: The branch never reads the requested version.

**Source:** Chapter 8 - MCP from scratch (opening)

## MA-ch08.6

Check each statement that is true about the four questions the chapter wants you to keep apart for any connection. Each statement is worth 1 point (5 points total).

- [ ] A. Whether the returned content supports the claim built on it is one of the four questions.
- [ ] B. Whether the code does what the listing says is one of the four questions.
- [ ] C. Whether this task may use the connection is one of the four questions.
- [ ] D. Whether Claude's summary of the exchange reads fluently is one of the four questions.
- [ ] E. Once the exchange is well formed, the other three questions are answered as well.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It is the evidence question.
- B: It is the capability question.
- C: It is the permission question.
- D: The four are form, listing versus code, task permission, and content support.
- E: A well-formed exchange answers only the first.

**Source:** What you will be able to do

## MA-ch08.7

Check each statement that is true about the four parties in a connection. Each statement is worth 1 point (5 points total).

- [ ] A. MCP itself chose the tool and vouches for what comes back.
- [ ] B. The server implements capabilities and describes them.
- [ ] C. Claude decides on its own which servers the task is authorized to use.
- [ ] D. People and policies define authority.
- [ ] E. The host constructs requests, interprets responses, exposes selected tools to Claude, and decides what content enters context.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: MCP supplies a communication structure; it did not choose the tool and does not vouch.
- B: That is the server's role.
- C: Claude, or a workflow around it, only proposes using a tool.
- D: Authority is the fourth party's role.
- E: That is the host's role.

**Source:** Four parties and one decision

## MA-ch08.8

Check each statement that is true about why three of the four parties cannot answer the fourth party's question. Each statement is worth 1 point (5 points total).

- [ ] A. The session supplies Claude with who owns the data, what the task is for, and what a wrong answer costs.
- [ ] B. The server can answer whether it belongs in the task, because its description states what it does.
- [ ] C. The question none of the three software parties can answer is whether this server, this data, and this action are appropriate for this task.
- [ ] D. Claude can weigh a tool description against a request.
- [ ] E. The host can both enforce and write the permission policy for the task.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The chapter says the session does not include those.
- B: Its description is its own testimony.
- C: That is the fourth party's question.
- D: But it only has what the session supplied.
- E: The host can enforce a policy but cannot write one.

**Source:** Four parties and one decision

## MA-ch08.9

Check each statement that is true about the two state variables in the reference server. Each statement is worth 1 point (5 points total).

- [ ] A. A valid initialize request also sets `ready` to true.
- [ ] B. Tool operations are rejected until `ready` is true.
- [ ] C. A valid initialize request sets `initialized` to true.
- [ ] D. Both `initialized` and `ready` start as false.
- [ ] E. A `notifications/initialized` message sets `ready` to true only if `initialized` is already true.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Readiness waits for the initialized notification.
- B: Having `initialized` true is not enough.
- C: It also returns server information and capabilities.
- D: Both are set false in `__init__`.
- E: Otherwise nothing changes.

**Source:** Initialization is a state transition

## MA-ch08.10

Check each statement that is true about why initialization takes two steps. Each statement is worth 1 point (5 points total).

- [ ] A. A stateless server would be shorter to write but impossible to hold to an order.
- [ ] B. The initialized notification lets the client say it has finished the initialization phase.
- [ ] C. Readiness is inferred from the fact that the server process exists.
- [ ] D. The design makes readiness a statement by the client and a precondition for the server.
- [ ] E. The price of the design is state, and every piece of state is a place where two parties can disagree about history.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Without state there is nothing to enforce the order.
- B: The request and response only exchange protocol information.
- C: The design deliberately avoids that inference.
- D: That is the stated design choice.
- E: That is the cost the chapter names.

**Source:** Initialization is a state transition

## MA-ch08.11

Check each statement that is true about how `handle` treats incoming messages. Each statement is worth 1 point (5 points total).

- [ ] A. That check covers every JSON-RPC validity condition.
- [ ] B. The first check validates that the message is a dictionary with `jsonrpc` equal to `2.0`.
- [ ] C. A message with no `id` is treated as a notification.
- [ ] D. A notification that arrives before `initialize` gets an error response.
- [ ] E. A message that fails that check gets an invalid-request error with a null identifier.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The chapter calls it a narrow rule.
- B: That is the base validation.
- C: That routes it to the notification branch.
- D: Nothing changes and the handler returns `None`.
- E: The id is null because there is no usable id.

**Source:** Initialization is a state transition

## MA-ch08.12

Check each statement that is true about the silence that follows a `notifications/initialized` message. Each statement is worth 1 point (5 points total).

- [ ] A. Because silence looks the same in both cases, the client must keep its own record of the lifecycle.
- [ ] B. Receiving nothing back tells the client that the server is now ready.
- [ ] C. The missing response is a lost message that the server should patch with an invented acknowledgement.
- [ ] D. A valid initialized notification gets no response; the handler returns `None`.
- [ ] E. A notification that arrives before `initialize` still sets `ready` to true.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: It cannot read readiness off the wire.
- B: Silence looks the same whether or not the notification took effect.
- C: The chapter says not to patch it.
- D: No response is the expected behavior on this route.
- E: It changes nothing because `initialized` is false.

**Source:** Initialization is a state transition

## MA-ch08.13

Check each statement that is true about the result of the initialize request. Each statement is worth 1 point (5 points total).

- [ ] A. The declared name and version are independent evidence that the server behaves as described.
- [ ] B. The declared fields are inputs to a compatibility decision.
- [ ] C. The response omits the request's identifier because initialize is special.
- [ ] D. The `capabilities` field lists the `lookup` tool by name.
- [ ] E. The result declares protocol version `2025-11-25`.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The process under review wrote them.
- B: They feed the decision; they do not prove behavior.
- C: The response wraps the result with the JSON-RPC version and the request's id.
- D: It declares a tools capability with an empty object.
- E: The server returns that version.

**Source:** The initialize exchange

## MA-ch08.14

Check each statement that is true about the recorded run in which the client requests version `unsupported-fixture`. Each statement is worth 1 point (5 points total).

- [ ] A. The server does not inspect a `params` object on initialize.
- [ ] B. Capability negotiation is narrow: the server declares a tools capability with an empty object and checks nothing about the client.
- [ ] C. The server still answers `2025-11-25`.
- [ ] D. On this branch the server can distinguish a supported request from a malformed one.
- [ ] E. The empty tools capability certifies the lifecycle clauses about capabilities.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It ignores what the client asked for.
- B: That suffices for the tool list that follows.
- C: It answers the same regardless of the request.
- D: It cannot.
- E: It does not certify any lifecycle clause.

**Source:** The initialize exchange

## MA-ch08.15

Check each statement that is true about how strongly to word a criticism of the teaching server. Each statement is worth 1 point (5 points total).

- [ ] A. 'The teaching server does not evaluate the requested version or validate the required initialization fields' names mechanisms that are actually missing.
- [ ] B. A broader criticism is stronger because it covers more possible defects.
- [ ] C. 'The fixed version violates MCP' overstates the case.
- [ ] D. A claim that names the missing mechanism tells you which test to write next.
- [ ] E. A criticism too broad to test is one more fluent claim.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Naming mechanisms makes the criticism testable.
- B: Breadth that cannot be tested is a weakness.
- C: A server may return another supported version.
- D: That is what makes it useful.
- E: That is the chapter's warning.

**Source:** The initialize exchange

## MA-ch08.16

Check each statement that is true about the `tools/list` result. Each statement is worth 1 point (5 points total).

- [ ] A. The schema permits additional properties beyond `key`.
- [ ] B. After readiness, `tools/list` returns one tool named `lookup`.
- [ ] C. The input schema requires exactly one property, `key`, which must be a string.
- [ ] D. Before the server is ready, `tools/list` returns an error instead of the tool description.
- [ ] E. The description says the tool reads a public course fixture.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: `additionalProperties` is false.
- B: Row 7 of the table.
- C: That is the declared schema.
- D: Row 2 of the table.
- E: The text is 'Read a public course fixture'.

**Source:** Discovery reveals a declared capability

## MA-ch08.17

Check each statement that is true about the word 'public' in the tool description. Each statement is worth 1 point (5 points total).

- [ ] A. A description can be technically accurate and still carry a word the server had no standing to assert.
- [ ] B. The server can tell you the fixture is public.
- [ ] C. 'Public' is a classification of data, and that word belongs in your permission ledger.
- [ ] D. The description is accurate in the author's sense, because the code consults one mapping.
- [ ] E. The word 'public' is established by inspecting the lookup source.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 'Public' is the example.
- B: Nothing in the code classifies anything.
- C: It is filled in by whoever owns the data.
- D: The chapter grants this.
- E: Source inspection shows what the code does, not how the data is classified.

**Source:** Discovery reveals a declared capability

## MA-ch08.18

Check each statement that is true about evaluating a candidate server whose description sounds harmless. Each statement is worth 1 point (5 points total).

- [ ] A. A misleading description can steer which tool gets chosen before any runtime check runs.
- [ ] B. Faith in the description is adequate evidence for a candidate.
- [ ] C. If a host places a tool description in Claude's context, it is more text competing for influence there.
- [ ] D. A defective or malicious server could advertise a harmless purpose and do something else.
- [ ] E. Evaluating a candidate takes source inspection, sandboxing, provenance, or other evidence appropriate to the deployment.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: It competes for influence in context.
- B: The chapter says to use evidence instead.
- C: Chapter 1: a system prompt is a request, not a gate.
- D: A description is only a claim.
- E: Not faith in the description.

**Source:** Discovery reveals a declared capability

## MA-ch08.19

Check each statement that is true about the three layers at which a `tools/call` can go wrong. Each statement is worth 1 point (5 points total).

- [ ] A. The task layer covers a lookup that ran and found nothing.
- [ ] B. The reply cannot show which layer failed; you need the server's source to tell.
- [ ] C. The request layer covers a lookup that ran and found nothing.
- [ ] D. The lifecycle layer covers a wrong tool name or wrong arguments.
- [ ] E. The lifecycle layer covers a call that came too early.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The failure belongs to the task result.
- B: The reply tells you which, if you read it that way.
- C: That is the task layer.
- D: Those are request-layer failures.
- E: That is the first layer.

**Source:** Requests, identifiers, and tool results

## MA-ch08.20

Check each statement that is true about how the server validates a `tools/call`. Each statement is worth 1 point (5 points total).

- [ ] A. An additional argument alongside `key` also produces `-32602`.
- [ ] B. A `key` that is not a string produces a tool result with `isError` true.
- [ ] C. A missing `key` argument produces `-32602` with the message `Expected a string key`.
- [ ] D. An unknown tool name produces JSON-RPC error `-32602` in this teaching implementation.
- [ ] E. In all of these cases the tool never produced a content result.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The arguments must contain exactly the key `key`.
- B: It produces a `-32602` error.
- C: Argument structure must be exact.
- D: Tool name is checked first.
- E: They are request-validation failures.

**Source:** Requests, identifiers, and tool results

## MA-ch08.21

Check each statement that is true about a lookup of a key that has no record. Each statement is worth 1 point (5 points total).

- [ ] A. A host that ignores `isError` and presents `Record not found` as an ordinary fact is using the result correctly.
- [ ] B. The request was well formed and the method existed.
- [ ] C. Treating every negative result as a broken protocol is the right way for a host to handle `Record not found`.
- [ ] D. The missing record is reported as JSON-RPC error `-32602`.
- [ ] E. The tool never ran its lookup, so the failure belongs to the request layer.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: That misuses a well-formed result.
- B: So the failure is not a protocol failure.
- C: The distinct layers let the host choose among revising, reporting, or stopping.
- D: It is a tool result whose `isError` is true.
- E: The tool ran its lookup; the failure belongs to the task result.

**Source:** Requests, identifiers, and tool results

## MA-ch08.22

Check each statement that is true about what a reply to a tool request does and does not show. Each statement is worth 1 point (5 points total).

- [ ] A. A successful response containing text makes the text correct.
- [ ] B. A matching id shows that the tool used the intended data.
- [ ] C. A matching id shows that the result is safe to pass on.
- [ ] D. A matching id shows which response belongs with which request.
- [ ] E. The content of a successful response stays untrusted data.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Correctness needs provenance appropriate to the source.
- B: It says nothing about that.
- C: It says nothing about safety.
- D: Identifiers solve association.
- E: Success does not validate content.

**Source:** Requests, identifiers, and tool results

## MA-ch08.23

Check each statement that is true about what the transition table shows for rows 2, 3, 6, and 7. Each statement is worth 1 point (5 points total).

- [ ] A. The only difference between those two rows is history.
- [ ] B. `tools/list` fails in row 2 and succeeds in row 7.
- [ ] C. In row 3 nothing changes.
- [ ] D. In row 6 readiness begins.
- [ ] E. Rows 3 and 6 receive the same response and have the same effect on state.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Row 2 starts at F, F and row 7 at T, T.
- B: Same message, different outcome.
- C: The early notification leaves the state at F, F.
- D: The state goes from T, F to T, T.
- E: Same response (none), different state effects.

**Source:** History is part of the protocol

## MA-ch08.24

Check each statement that is true about row 10, where a method named `bad` reaches a ready server. Each statement is worth 1 point (5 points total).

- [ ] A. The server returns `-32601` for an unknown method in every state.
- [ ] B. The same `bad` method sent in row 2's state would also have received `-32601`.
- [ ] C. An error code lists every defect the message had.
- [ ] D. An error code reports the branch the server reached.
- [ ] E. The response is error `-32601`.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It does so only because the server was ready.
- B: It would have received `-32000`.
- C: Only the branch reached is reported.
- D: It does not report every defect.
- E: Row 10 of the table.

**Source:** History is part of the protocol

## MA-ch08.25

Check each statement that is true about parse errors and invalid requests in stdio mode. Each statement is worth 1 point (5 points total).

- [ ] A. The texts `{` and `{}` produce the same error code.
- [ ] B. The main loop catches a parsing `ValueError` and emits `-32700` with a null id.
- [ ] C. Preserving the raw text is how you tell those two failures apart.
- [ ] D. The text `{}` fails to parse and receives `-32700`.
- [ ] E. The text `{` fails before the handler runs.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: They produce `-32700` and `-32600`.
- B: That happens before the handler.
- C: The code alone would not say which input caused it.
- D: It parses and receives `-32600`.
- E: It does not parse.

**Source:** History is part of the protocol

## MA-ch08.26

Check each statement that is true about the two behaviors the chapter says nobody chose. Each statement is worth 1 point (5 points total).

- [ ] A. A `tools/call` sent without an id is dropped without a response, even when the server is ready.
- [ ] B. They are what the code does because nothing said otherwise.
- [ ] C. The chapter states what the specification requires for both cases.
- [ ] D. A second `initialize` sent to a ready server leaves `ready` true.
- [ ] E. The lesson's tests pin both behaviors.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Messages without an id are treated as notifications.
- B: That is the cost of leaving a handshake rule implicit.
- C: It explicitly does not claim to know.
- D: The code does not reset it.
- E: Neither is pinned by the lesson's tests.

**Source:** History is part of the protocol

## MA-ch08.27

Check each statement that is true about the questions the four ledgers ask. Each statement is worth 1 point (5 points total).

- [ ] A. The permission ledger asks whether the code does what the listing says.
- [ ] B. The protocol ledger asks whether the exchange is well formed and in order.
- [ ] C. A protocol-version change reopens the capability ledger.
- [ ] D. The capability ledger asks whether this task allows that capability.
- [ ] E. The evidence ledger asks whether the exchange is in order.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: That is the capability ledger's question.
- B: Its evidence is the transcript.
- C: It reopens the protocol ledger.
- D: That is the permission ledger's question.
- E: It asks whether the returned content supports the claim built on it.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## MA-ch08.28

Check each statement that is true about what fills and what reopens each ledger. Each statement is worth 1 point (5 points total).

- [ ] A. The evidence ledger is reopened by a protocol-version change.
- [ ] B. The protocol ledger is filled by comparison with the declared source.
- [ ] C. The capability ledger is reopened by a changed task or broader data scope.
- [ ] D. The permission ledger is filled by the task brief, the data owner, and your policy.
- [ ] E. The capability ledger is filled by source inspection, disposable fixtures, and who maintains the server.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: A changed corpus reopens the evidence ledger; a version change reopens the protocol ledger.
- B: That fills the evidence ledger.
- C: That reopens the permission ledger.
- D: That is its 'what fills it' cell.
- E: That is its 'what fills it' cell.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## MA-ch08.29

Check each statement that is true about applying the four ledgers to the teaching lookup. Each statement is worth 1 point (5 points total).

- [ ] A. The capability ledger can show that the code reads one in-memory mapping and performs no file write.
- [ ] B. A clean protocol ledger can stand in for the capability ledger.
- [ ] C. The protocol ledger can show a legal initialization and call.
- [ ] D. The permission ledger says whether the public fixture is allowed for the classroom task.
- [ ] E. The evidence ledger compares `505A Dana Hall` with the declared fixture source.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Source inspection supports it.
- B: None of these records can stand in for another.
- C: The transcript supports it.
- D: It depends on the task and the data owner.
- E: That comparison is its job.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## MA-ch08.30

Check each statement that is true about two cases: a perfect protocol ledger with an undeclared write, and a read-only server whose fixture is stale. Each statement is worth 1 point (5 points total).

- [ ] A. With a perfect protocol ledger and an undeclared write, the connection succeeds and the behavior exceeds the task boundary.
- [ ] B. With a properly read-only capability and a stale fixture, permission is satisfied and the evidence claim fails.
- [ ] C. 'Passed' is a complete statement without naming which review passed.
- [ ] D. In the stale-fixture case, the capability ledger fails.
- [ ] E. In the undeclared-write case, the protocol ledger fails.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The capability ledger reveals the write.
- B: The returned content does not support the claim.
- C: 'Passed' must always name which review passed.
- D: The capability is properly read-only; the evidence ledger fails.
- E: The protocol ledger is perfect in that case.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## MA-ch08.31

Check each statement that is true about recording unknowns and about what trust is. Each statement is worth 1 point (5 points total).

- [ ] A. Trust is a permanent property of a server's name.
- [ ] B. If a server is closed-source, advertised behavior may be the only evidence available, and the decision should say so.
- [ ] C. The absence of observed harm in a test you did not perform is evidence that the capability is absent.
- [ ] D. Trust becomes a decision over identifiable inputs that reopens when one of them changes.
- [ ] E. If you have not inspected network behavior, you should write 'uninspected', not 'none'.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Trust is a decision over identifiable inputs.
- B: State the weakness of the evidence.
- C: It is not evidence.
- D: That is what the last column provides.
- E: Not looking is not the same as finding nothing.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## MA-ch08.32

Check each statement that is true about where the server's responsibility ends and what the host and client do. Each statement is worth 1 point (5 points total).

- [ ] A. The client must decide whether it supports the server-selected version.
- [ ] B. The teaching server can demonstrate the client's version-handling behavior.
- [ ] C. The server's responsibility ends at its reply.
- [ ] D. The server decides what content enters Claude's context.
- [ ] E. A complete interoperability test needs only the server side.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The specification's fallback route depends on that decision.
- B: It implements only the server object.
- C: After that the host takes over.
- D: The host decides that.
- E: It needs both sides or a harness representing the client's obligations.

**Source:** Compatibility is not authorized: The host is part of the mechanism

## MA-ch08.33

Check each statement that is true about laundering. Each statement is worth 1 point (5 points total).

- [ ] A. The word 'laundering' is the companion book's framing, and the mechanism is polish conferring credibility the content never earned.
- [ ] B. The failure the ledgers exist to stop is rarely a malformed message.
- [ ] C. Laundering is an unverified output acquiring authority as it passes through downstream steps.
- [ ] D. The JSON-RPC envelope gives the text the shape of a protocol-valid reply but does not check the content.
- [ ] E. The mechanism is credibility the content earned by being checked at each hop.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The chapter says so directly.
- B: The messages can be perfectly valid.
- C: That is the companion book's definition.
- D: None of the hops checked the content.
- E: None of the hops checked the content.

**Source:** Compatibility is not authorized: Laundering: valid transport, borrowed authority

## MA-ch08.34

Check each statement that is true about the three-row handoff table for the course lookup. Each statement is worth 1 point (5 points total).

- [ ] A. The server-to-host trust is earned by Claude agreeing with the text.
- [ ] B. A handoff with no verification is harmless as long as the next step is fluent.
- [ ] C. Claude's sentence may state the office as a current fact without naming the fixture.
- [ ] D. For the host-to-Claude handoff, the text is trusted as an instruction Claude should follow.
- [ ] E. For the server-to-host handoff, the reply is trusted to be the fixture's value for key `office` from this server version.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: It is earned by comparison with the mapping in the source.
- B: Fluency lets unverified output travel onward wearing the authority of every clean step.
- C: The sentence should keep the fixture role.
- D: It is data to cite with its role, not an instruction.
- E: That trust is earned by comparison with the mapping in the inspected source.

**Source:** Compatibility is not authorized: Laundering: valid transport, borrowed authority

## MA-ch08.35

Check each statement that is true about the gate you write before connecting a server. Each statement is worth 1 point (5 points total).

- [ ] A. You write it before you read the reference.
- [ ] B. You write it before you ask Claude for anything.
- [ ] C. It has two halves: the lifecycle as a state machine you predicted, and the four ledgers for the connection decision.
- [ ] D. You name who decided each item.
- [ ] E. You write it after Claude's first implementation so the details match.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Prediction comes before the answer.
- B: Otherwise it is not your decision on the record.
- C: Both halves are written before the reference.
- D: The gate records decisions and who made them.
- E: It is written before Claude touches anything.

**Source:** The gate: write the connection decision before you connect

## MA-ch08.36

Check each statement that is true about the gate's design and its contract for the state machine. Each statement is worth 1 point (5 points total).

- [ ] A. A notification produces a response that acknowledges it.
- [ ] B. Tool operations are accepted once initialize has arrived, even before the notification.
- [ ] C. The candidates are the read-only teaching server, which you will execute, and a hypothetical write-capable server advertising `save_report`, which you will never run.
- [ ] D. The subset claims version negotiation.
- [ ] E. The task is to answer where the office for key `office` is, using only the declared course fixture.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A notification never produces a response.
- B: They are refused until both have arrived, in that order.
- C: Only one is executed.
- D: The contract says it does not.
- E: That is the stated design.

**Source:** The gate: write the connection decision before you connect

## MA-ch08.37

Check each statement that is true about the gate's contract for the connection. Each statement is worth 1 point (5 points total).

- [ ] A. The permission ledger names the sources the task may read, the effects it may have, and where results may go.
- [ ] B. The evidence ledger requires that every value Claude may cite be compared with the declared source first.
- [ ] C. 'Trusted' is one of the evidence types.
- [ ] D. The capability ledger lists the claims you will check in source: one mapping, no write, no network.
- [ ] E. 'Uninspected' is one of the evidence types.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Here the only effect is returning text.
- B: Comparison comes before citation.
- C: Trusted needs a named evidence type behind it.
- D: Those are the claims for the lookup.
- E: The others include advertised, source-inspected, executed on a fixture, and independently sourced.

**Source:** The gate: write the connection decision before you connect

## MA-ch08.38

Check each statement that is true about the three constructed wrong versions the gate's checks must catch. Each statement is worth 1 point (5 points total).

- [ ] A. The log-appending `lookup` with a flawless lifecycle fails the protocol ledger.
- [ ] B. The first sets `ready` inside the initialize branch and so skips the notification.
- [ ] C. Applied to a copy of the reference, that change leaves all six of the lesson's tests passing.
- [ ] D. The read-only `lookup` whose fixture value disagrees with the declared source passes all four ledgers.
- [ ] E. The lesson's tests include `tools/list` after initialize and before the notification.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: It passes the protocol ledger and fails the capability ledger.
- B: That is the ready-on-initialize change.
- C: The suite lacks the case that would fail it.
- D: It passes three and fails the evidence ledger.
- E: That case is not among them.

**Source:** The gate: write the connection decision before you connect

## MA-ch08.39

Check each statement that is true about the failure sentence and the pass condition. Each statement is worth 1 point (5 points total).

- [ ] A. Writing the sentence after reading the output is fine, since you can then be more precise.
- [ ] B. 'Looks good' is an acceptable handoff condition if the protocol ledger is clean.
- [ ] C. The words 'safe' and 'trusted' are acceptable without an evidence type when the decision is deny.
- [ ] D. Whether the fixture is public can be settled by the author of the gate.
- [ ] E. You write a dated sentence, before reading any transcript, saying what you would see if your table were wrong.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: If you write it after, you have described the output.
- B: A stranger must be able to tell whether the condition is met.
- C: The pass condition allows no such word without a named evidence type.
- D: Only its owner can settle it.
- E: That is the failure sentence.

**Source:** The gate: write the connection decision before you connect

## MA-ch08.40

Check each statement that is true about building the state machine by hand before consulting the reference. Each statement is worth 1 point (5 points total).

- [ ] A. Your own version is the record of what you understood before Claude touched anything.
- [ ] B. After comparing, you should name a difference in behavior, not in line count or style.
- [ ] C. The best lifecycle case to add is initialize, then `tools/list` without the notification, which must still return `-32000`.
- [ ] D. Your own version is the instrument you will measure Claude's version against.
- [ ] E. You should read the reference first so your table matches it.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is the reason for building by hand.
- B: Behavior is what matters.
- C: The suite lacks it.
- D: It is the baseline.
- E: You build from your own table, then compare.

**Source:** Build It: implement the state machine before connection

## MA-ch08.41

Check each statement that is true about running the demo and stdio mode. Each statement is worth 1 point (5 points total).

- [ ] A. Leaving an unbounded server process running counts as a completed exercise.
- [ ] B. You can test stdio by typing lines interactively without a controlled process.
- [ ] C. The client parses standard output as protocol messages, so a stray print there corrupts the channel.
- [ ] D. A stray print on standard output is harmless because the client reads only standard error.
- [ ] E. You should test stdio mode before running the default demo.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The chapter says it does not.
- B: Feed only declared lines in a controlled process.
- C: Debug output must go elsewhere.
- D: The client parses standard output.
- E: Run the default demo first.

**Source:** Build It: implement the state machine before connection

## MA-ch08.42

Check each statement that is true about conducting Claude Code against your gate. Each statement is worth 1 point (5 points total).

- [ ] A. If Claude's server passes every one of your tests, your test list cannot be too weak.
- [ ] B. You run your tests on what Claude returns yourself.
- [ ] C. A failing test is often a gap in your gate, which Claude could not see because it had only what you wrote.
- [ ] D. You also give Claude your own implementation so it can match your style.
- [ ] E. You give Claude the transition table, the contract, and the test list.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A deliberately wrong server may also pass.
- B: You do not take its word.
- C: The gate was incomplete.
- D: You give it the gate, not your implementation.
- E: Those are the gate.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## MA-ch08.43

Check each statement that is true about testing whether your tests are strong enough. Each statement is worth 1 point (5 points total).

- [ ] A. You can ask Claude for a deliberately wrong server that still passes your tests, and run your tests against it.
- [ ] B. Designing first means the design is frozen once written.
- [ ] C. A case your gate missed reopens the gate: revise it, date the revision, and delete the original.
- [ ] D. If your tests do not catch that change, your list was too weak, and you found out cheaply.
- [ ] E. As a control, you make the ready-on-initialize change to a copy of your own server and run the same tests.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: That probes the list.
- B: Designing first is not freezing the design.
- C: Keep the original.
- D: That is the chapter's wording.
- E: If they do not catch it, the list is too weak.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## MA-ch08.44

Check each statement that is true about the prompt that asks Claude to compare a transcript, the source, and the tool description. Each statement is worth 1 point (5 points total).

- [ ] A. It asks Claude to list every place where they disagree, or where one claims more than another supports.
- [ ] B. It asks Claude to tell you whether to connect the server.
- [ ] C. It asks Claude to quote the line it relied on for each item.
- [ ] D. It asks Claude to call behavior safe once it finds no discrepancy.
- [ ] E. It asks Claude to rewrite the server source to remove the discrepancies.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: That is the core request.
- B: It says not to.
- C: So that you can check each one.
- D: It says not to call any behavior safe.
- E: It asks only for a list of discrepancies.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## MA-ch08.45

Check each statement that is true about what you do with Claude's list of discrepancies. Each statement is worth 1 point (5 points total).

- [ ] A. You check every item it returns against the source yourself.
- [ ] B. After the list is returned, the allow, deny, or pending decision is Claude's.
- [ ] C. You treat the list as places to look.
- [ ] D. An item's absence from the list is evidence that no such discrepancy exists.
- [ ] E. An item that quotes a source line can be accepted without checking.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Some will be wrong.
- B: The decision is yours.
- C: The list is leads.
- D: Absence proves nothing.
- E: Check every item.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## MA-ch08.46

Check each statement that is true about source inspection of the reference server and of external candidates. Each statement is worth 1 point (5 points total).

- [ ] A. The import list proves nothing about files, because `open` is a builtin and needs no import.
- [ ] B. The reference imports only `argparse`, `json`, and `sys`, which shows that it cannot write files.
- [ ] C. What establishes that the lookup writes nothing is the call branch itself, whose only data is a literal mapping.
- [ ] D. If inspection of an external candidate is incomplete, you record the decision as pending or deny.
- [ ] E. If inspection of an external candidate is incomplete, you may fill the gap from its tool description.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Imports are the wrong evidence.
- B: The import list proves nothing about files.
- C: That is the correct evidence.
- D: That is the stated rule.
- E: Do not invent behavior from a description.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## MA-ch08.47

Check each statement that is true about the transcript section of the evaluation packet. Each statement is worth 1 point (5 points total).

- [ ] A. The artifact brief asks for an initialization transcript, a capability inventory, and a trust decision.
- [ ] B. The transcript is arranged chronologically and preserves requests, notifications, responses, identifiers, state transitions, and errors.
- [ ] C. The packet explains the missing record as a protocol error.
- [ ] D. The transcript includes one successful and one failing call with their matching ids.
- [ ] E. The optional Progress Reel is a separate requirement and point category.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Those are the three parts.
- B: Order matters because history is part of the protocol.
- C: It explains why the missing record is a tool error, not a protocol error.
- D: That shows both layers.
- E: It is not a separate requirement or point category.

**Source:** Ship It: an MCP evaluation packet

## MA-ch08.48

Check each statement that is true about the rest of the evaluation packet. Each statement is worth 1 point (5 points total).

- [ ] A. Constructed messages are marked separately from any actual host integration.
- [ ] B. The office value is labeled a course fixture.
- [ ] C. Credentials are left in the transcript so the record is complete.
- [ ] D. For each capability, you record what the server says, what source inspection shows, which disposable tests ran, and what remains unknown.
- [ ] E. A valid tool listing is the trust decision.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Constructed and actual must not be mixed.
- B: That keeps its role visible.
- C: Credentials are redacted; this fixture uses none.
- D: Four items per capability.
- E: A valid listing belongs in the evidence; it is not the decision.

**Source:** Ship It: an MCP evaluation packet

## MA-ch08.49

Check each statement that is true about the handoff analysis in the packet when a fixture value is deliberately wrong. Each statement is worth 1 point (5 points total).

- [ ] A. You include one handoff analysis: the three-row table filled in for your own run.
- [ ] B. The protocol ledger is the one that rejects the wrong value.
- [ ] C. A deliberately wrong fixture value means the JSON-RPC exchange failed.
- [ ] D. You show the source comparison that catches the wrong value before generation.
- [ ] E. The wrong value can be caught after Claude has written its answer, as long as someone notices.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: It records server output, host inference, supporting evidence, and allowed use.
- B: The factual check against the source rejects it.
- C: The chapter says not to call the protocol exchange failed.
- D: The check happens before Claude restates it.
- E: The chapter wants the comparison before generation.

**Source:** Ship It: an MCP evaluation packet

## MA-ch08.50

Check each statement that is true about the sign-off template. Each statement is worth 1 point (5 points total).

- [ ] A. A sign-off is needed only when the decision is allow.
- [ ] B. The 'Not checked' line can name network behavior, other versions of the server, client-side version handling, and whether the fixture is true in the world.
- [ ] C. The 'Not checked' line is the line an AI-written sign-off fills most thoroughly.
- [ ] D. The template ends with a 're-review if' trigger and a 'signed or withheld' line.
- [ ] E. The 'Not claiming' line can name that the server is secure, conformant to MCP, or endorsed beyond this task and version.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: You can sign a deny.
- B: Those are the template's examples.
- C: It is the line an AI-written sign-off leaves empty.
- D: Both appear in the template.
- E: Those are the template's examples.

**Source:** Ship It: an MCP evaluation packet

## MA-ch08.51

Check each statement that is true about the decision, the sign-off, and the verbs you may use. Each statement is worth 1 point (5 points total).

- [ ] A. The decision is about the server, and the sign-off is about your evidence for the decision.
- [ ] B. You can withhold your signature from an allow that your evidence does not support.
- [ ] C. 'Verified' is the right verb for a fixture you ran without error.
- [ ] D. 'Recorded' fits a transcript and 'compared' fits a source check.
- [ ] E. You can sign a deny.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: They are different statements.
- B: That is explicitly allowed.
- C: The right verb is 'executed'; 'verified' needs a criterion this exercise never supplies.
- D: These are verbs the evidence earns.
- E: The signature attests to the evidence.

**Source:** Ship It: an MCP evaluation packet

## MA-ch08.52

Check each statement that is true about how the chapter divides the work between Claude and you. Each statement is worth 1 point (5 points total).

- [ ] A. You can skip building your own baseline if Claude writes the tests.
- [ ] B. Claude should classify the fixture as public, since it can read the code.
- [ ] C. Claude can generate many out-of-order and malformed messages quickly and run them.
- [ ] D. Claude should decide the expected response for each out-of-order message.
- [ ] E. Claude should sign or withhold the final packet.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: You cannot audit a lifecycle you have not built.
- B: Classification is a fact about your world.
- C: That is Claude's part of the task.
- D: You decide it; the expected response is the contract.
- E: The decision carries your name.

**Source:** The driver's seat

## MA-ch08.53

Check each statement that is true about why the trust decision stays with a person. Each statement is worth 1 point (5 points total).

- [ ] A. Accountability for a wrong decision lands on Claude.
- [ ] B. The transcript contains none of those facts.
- [ ] C. The chapter's claim is that Claude is incapable of reasoning about such facts.
- [ ] D. Those facts are already among Claude's inputs once the session starts.
- [ ] E. The trust decision rests on facts about the world around the transcript: who owns the data, what the task needs, what a wrong answer costs, and who maintains the server.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: It lands on a person.
- B: That is why it cannot supply them.
- C: The chapter says the claim is not that.
- D: They are not, unless you supply them.
- E: Those are the chapter's examples.

**Source:** The driver's seat

## MA-ch08.54

Check each statement that is true about reading the transcript in both directions. Each statement is worth 1 point (5 points total).

- [ ] A. The two passes catch the same omissions, so one pass is enough.
- [ ] B. Reading as a reviewer, you ask which request and prior transition must be present before the interpretation is justified.
- [ ] C. A tool list in isolation is enough to reconstruct the initialize request and the notification.
- [ ] D. Reading as the server, you ask which branch runs, what response it produces, and what state changes.
- [ ] E. A tool result in isolation keeps the arguments and identifier but loses the content.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: They catch different omissions.
- B: That is the second pass.
- C: It omits them, along with the process configuration and source version.
- D: That is the first pass.
- E: It keeps the content and loses the arguments and identifier.

**Source:** Verify and reflect

## MA-ch08.55

Check each statement that is true about comparing the transcript with the source and about what the default demo did not do. Each statement is worth 1 point (5 points total).

- [ ] A. Because the happy path resembles the specification, the subset can be called conformant.
- [ ] B. The default demo did not connect to Claude, expose a network port, or write a file.
- [ ] C. The correspondence review asks whether the advertised tool name matches the dispatch branch and whether the schema matches the argument validation.
- [ ] D. The correspondence review establishes the behavior of every version of the server.
- [ ] E. The correspondence review is stronger than either the listing or code inspection alone.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The chapter says not to call it conformant.
- B: That is the 'what did not happen' row.
- C: Plus whether `isError` appears for the recorded missing key.
- D: It is evidence about the tested version only.
- E: It is still evidence about the tested implementation and version.

**Source:** Verify and reflect

## MA-ch08.56

Check each statement that is true about the chapter's Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. In 'Compatibility test, not certification', a passing test would certify security and full conformance.
- [ ] B. In 'Trust decision', a withheld signature counts as a failed exercise.
- [ ] C. In 'Too early', you explain the changed state rather than calling the first message malformed.
- [ ] D. The Assessments carry no points.
- [ ] E. In 'Too early', you write the test that stops the ready-on-initialize change and show it failing against that change.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The exercise states what success would not establish.
- B: Withholding the signature is an acceptable result.
- C: The same message succeeds later because of history.
- D: They are ungraded practice.
- E: That is the exercise's instruction.

**Source:** Assessments - ungraded practice

## MA-ch08.57

Check each statement that is true about what you can now trace. Each statement is worth 1 point (5 points total).

- [ ] A. The version limitation is: one supported version returned without evaluating client parameters, a fallback a client may legally receive, and no demonstration of full negotiation or conformance.
- [ ] B. Initialize changes one state, the initialized notification changes another, and tool operations become available only afterward.
- [ ] C. Protocol compatibility determines what the workflow should do with the communication.
- [ ] D. A tool-level negative result and a protocol-level error should be handled identically.
- [ ] E. The server itself can settle whether the word 'public' in its description is true.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The chapter states it that way.
- B: That is the first summary.
- C: Compatibility only enables communication.
- D: They are different layers.
- E: The server had no standing to assert it.

**Source:** What you can now trace

## MA-ch08.58

Check each statement that is true about connecting a tool and training a model. Each statement is worth 1 point (5 points total).

- [ ] A. The gate question carried into Chapter 9 asks you to change first and decide afterward what the change showed.
- [ ] B. Connecting a server is a form of training the model.
- [ ] C. Chapter 9 compares the weight-and-bias mechanism with changes to prompts, context, tools, and settings.
- [ ] D. An MCP server can add information and actions to a host without changing model parameters.
- [ ] E. Chapter 9 implements a tiny logistic predictor whose weight and bias genuinely update under a loss function.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It asks you to state what should change and what would show that it did before you change anything.
- B: Connection does not change model parameters.
- C: That comparison is how the chapter frames the next lesson.
- D: That is the distinction.
- E: That is the contrast case.

**Source:** Connecting a tool is not training a model

## MA-ch08.59

Check each statement that is true about the 'Anthropics' section. Each statement is worth 1 point (5 points total).

- [ ] A. You compare your server with Anthropic's MCP builder materials and evaluation guide.
- [ ] B. You should install the external skill as soon as you read the links.
- [ ] C. The versioned specification stays the protocol authority.
- [ ] D. Upstream examples are permission to connect an unreviewed server.
- [ ] E. You identify one answerable task and an independently verifiable result for the read-only fixture.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: They were checked through the course research on 2026-09-06.
- B: Do not install an external skill merely because the links exist.
- C: Upstream examples do not replace it.
- D: The section says not to treat them that way.
- E: That is the section's task.

**Source:** Anthropics

## MA-ch08.60

Check each statement that is true about the Conducting AI test the chapter applies to your own checks. Each statement is worth 1 point (5 points total).

- [ ] A. An audit reduces error only to the degree that the checker fails differently from the thing it checks.
- [ ] B. Plausibility is the ground the original answer stood on.
- [ ] C. If the sentence on how a check can fail matches the sentence on how the checked thing can fail, you have a strong check.
- [ ] D. Asking Claude whether `505A Dana Hall` looks right, with no source in hand, is an independent check on the original answer.
- [ ] E. Comparing the value with the mapping in the inspected source fails in an unrelated way: it errors loudly and cannot be persuaded.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: That is the test.
- B: So a plausibility check repeats the original failure mode.
- C: If they match, you have a repeat, not a check.
- D: It judges plausibility.
- E: That is why it is a real check.

**Source:** Conducting AI
