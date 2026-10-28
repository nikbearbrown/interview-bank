# Chapter 8: MCP from scratch

## ES-ch08.1

Two servers advertise a tool called `lookup`. Both return valid JSON-RPC messages and copy request identifiers correctly; one reads a declared public fixture and the other writes files as a side effect. Explain why protocol syntax cannot separate them and which question a clean handshake leaves unanswered.

**Points:** 5

**Rubric (1 point each):**

1. States that protocol syntax cannot tell the two servers apart, so it cannot show that they deserve different permissions.
2. Defines interoperability as whether components can exchange messages they understand.
3. Defines authorization as whether a particular capability should run in this task.
4. Says a clean handshake settles the first question and is silent on the second.
5. Notes that both servers copy request identifiers correctly, so identifier handling does not distinguish them.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.2

Claude is handed only the tool listing for the two servers in the opening scenario. What does Claude lack, what does it not lack, and who decides whether to connect?

**Points:** 5

**Rubric (1 point each):**

1. Says the listing gives Claude two descriptions to compare, and a description is a sentence the server wrote about itself.
2. Says that what Claude lacks is not skill with JSON.
3. Says Claude lacks any standpoint on whether this server belongs in this task.
4. Names at least two facts Claude lacks: whose data sits behind the server, what a stray file write would cost, who maintains it.
5. States that the decision to connect is the human's, with Claude's role being to read the transcript and list every discrepancy.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.3

The chapter says it applies the book's three jobs at the scale of one connection. Name the three jobs and say what each means for an MCP connection.

**Points:** 5

**Rubric (1 point each):**

1. Names Conduct, Check, and Drive as the three jobs.
2. Conduct: fix the order of events and the scope of use before anything is connected.
3. Check: ask what a transcript entitles you to believe and what it never tested.
4. Drive: let Claude read the transcript and list every discrepancy.
5. Says the decision to connect stays with the human under Drive.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.4

The research run recorded four observations of the local Python server. List them, and explain what claim they do and do not support.

**Points:** 5

**Rubric (1 point each):**

1. Listing tools before initialization returns an error.
2. An initialize request returns protocol version `2025-11-25`.
3. A valid initialized notification returns no response.
4. Looking up an unknown record produces a tool result with `isError: true`.
5. States that these are executed observations of this server, not claims about MCP generally.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.5

A classmate writes: 'The teaching server always answers 2025-11-25, so it violates the MCP lifecycle specification.' Evaluate the claim using the chapter's discussion of the version result.

**Points:** 5

**Rubric (1 point each):**

1. Says the server returns its one supported version without inspecting the client's requested version.
2. Says that under the versioned lifecycle specification a server may return another supported version when the requested one is unsupported.
3. Says the client is then left to decide whether it can continue.
4. Concludes that a fixed fallback is not, by itself, a violation.
5. Notes the server remains a teaching subset whose omissions the later sections spell out.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.6

The chapter warns that protocol education 'decays into a cargo cult of field names'. Explain what that means and what reading the lifecycle 'as behavior' asks you to track.

**Points:** 5

**Rubric (1 point each):**

1. Describes the cargo cult as copying field names or visible keys without understanding the behavior behind them.
2. Says a message can copy every visible key of the example and still miss the state machine around it.
3. Names tracking which message may come next.
4. Names tracking what state changes and which response belongs to which request.
5. Names tracking what the host may infer from a result.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.7

A student says: 'I ran the default demo, so my server is integrated with Claude.' Using the chapter's opening, say what the demo is and what must happen before anyone may claim a live Claude integration.

**Points:** 5

**Rubric (1 point each):**

1. Says the server runs offline and needs no direct API credits.
2. Says the default demo terminates without waiting on standard input.
3. Says a client may be connected only later, in an explicitly controlled exercise.
4. Says a live Claude integration must not be claimed unless you actually configured, ran, and recorded it.
5. Notes that Claude Code remains the assumed course assistant, which is separate from the offline server.

**Source:** Chapter 8 - MCP from scratch (opening)

## ES-ch08.8

Name the four questions the chapter wants you to keep apart for any connection, and give one scenario in which a connection passes one question but fails another.

**Points:** 5

**Rubric (1 point each):**

1. Names whether the exchange is well formed.
2. Names whether the code does what the listing says.
3. Names whether this task may use the connection.
4. Names whether the returned content supports the claim built on it.
5. Gives a valid scenario in which one question is passed and another failed (for example, a well-formed exchange with an undeclared write).

**Source:** What you will be able to do

## ES-ch08.9

Name the four parties in an MCP connection and state what each does. Then say what MCP itself does and does not do.

**Points:** 5

**Rubric (1 point each):**

1. The server implements capabilities and describes them.
2. The host constructs requests, interprets responses, exposes selected tools to Claude, and decides what content enters context.
3. Claude, or a workflow around it, proposes using a tool.
4. People and policies define authority.
5. MCP supplies a communication structure; it did not choose the tool and does not vouch for what comes back.

**Source:** Four parties and one decision

## ES-ch08.10

Three of the four parties are software, and none can answer the fourth party's question. State that question and explain, party by party, why each of the three cannot answer it.

**Points:** 5

**Rubric (1 point each):**

1. States the question: whether this server, this data, and this action are appropriate for this task.
2. Server: its description is its own testimony.
3. Host: it can enforce a policy but cannot write one.
4. Claude: it can weigh a description against a request but has only what the session supplied, which does not include who owns the data, what the task is for, or what a wrong answer costs.
5. Says the protocol carries the capability declaration while the authority is written somewhere else, by someone, before the call.

**Source:** Four parties and one decision

## ES-ch08.11

Describe the two state variables in the reference server and trace both through the legal sequence of initialize, the initialized notification, and a tool request.

**Points:** 5

**Rubric (1 point each):**

1. Both flags start false.
2. A valid initialize request sets `initialized` to true and returns server information and capabilities.
3. A `notifications/initialized` message arriving while `initialized` is true sets `ready` to true.
4. Tool operations are rejected until the server is ready.
5. Says the two flags are related but not interchangeable.

**Source:** Initialization is a state transition

## ES-ch08.12

Why does the protocol use two steps, an initialize request and response followed by an initialized notification, instead of treating the server as ready once initialize succeeds? Include the cost of the design.

**Points:** 5

**Rubric (1 point each):**

1. The request and response let client and server exchange protocol information.
2. The notification lets the client say it has finished that phase.
3. Readiness becomes a statement by the client and a precondition for the server.
4. It is not inferred from the fact that a process exists or that a tool list could be built.
5. The cost is state, a place where two parties can disagree about history; a stateless server would be shorter but impossible to hold to an order.

**Source:** Initialization is a state transition

## ES-ch08.13

A client sends `notifications/initialized` before it has sent `initialize` and receives nothing back. What did the server do, why is the silence correct, and what can the client not infer from it?

**Points:** 5

**Rubric (1 point each):**

1. A message with no `id` is treated as a notification.
2. Before initialize, nothing changes: `ready` stays false.
3. The handler returns `None`, because no response is expected on this route.
4. The silence is not a lost message to be patched with an invented acknowledgement.
5. Silence looks the same as a notification that took effect, so the client cannot infer readiness and must keep its own record of the lifecycle.

**Source:** Initialization is a state transition

## ES-ch08.14

The recorded run sends an initialize request whose requested version is `unsupported-fixture`. What happened, and what can and cannot be concluded?

**Points:** 5

**Rubric (1 point each):**

1. The server answered `2025-11-25` anyway.
2. The server does not inspect a `params` object on initialize.
3. On this branch it cannot distinguish a supported request from a malformed one.
4. Capability negotiation is narrow: a tools capability with an empty object, with nothing checked about the client, which suffices for the tool list that follows.
5. It does not certify any lifecycle clause.

**Source:** The initialize exchange

## ES-ch08.15

Compare the claim 'The fixed version violates MCP' with the claim 'The teaching server does not evaluate the requested version or validate the required initialization fields, so it is not a conformance implementation.' Which is better, and what test does the better one suggest?

**Points:** 5

**Rubric (1 point each):**

1. The first claim overstates the case, since a server may return another supported version.
2. The second names the mechanisms actually missing.
3. The second says the teaching server is not a conformance implementation, rather than saying it violates the protocol.
4. Proposes a concrete next test, such as sending initialize with an unsupported requested version or without the required initialization fields and checking whether the server evaluates it.
5. Says a criticism too broad to test is one more fluent claim.

**Source:** The initialize exchange

## ES-ch08.16

After readiness, `tools/list` returns one tool. Describe the declaration (name, description, input schema) and say who uses it and for what.

**Points:** 5

**Rubric (1 point each):**

1. The name is `lookup`.
2. The description is 'Read a public course fixture'.
3. The input schema requires exactly one property, `key`, which must be a string, and allows no additional properties.
4. A host uses the declaration to build a request.
5. In some integration designs a model or a user uses it to decide whether the tool is worth calling, and it is server-supplied text about the server.

**Source:** Discovery reveals a declared capability

## ES-ch08.17

The tool description says 'Read a public course fixture'. In what sense is it accurate, what word in it does the server have no standing to assert, and where does that word belong?

**Points:** 5

**Rubric (1 point each):**

1. It is accurate in the author's sense, because the code consults one mapping.
2. 'Public' is a classification of data.
3. Nothing in the code classifies anything, so the server cannot tell you the fixture is public.
4. The word belongs in the permission ledger, filled in by whoever owns the data.
5. A description can be technically accurate and still carry a word the server had no standing to assert.

**Source:** Discovery reveals a declared capability

## ES-ch08.18

A candidate server's description says it only reads a public course fixture. Explain why you should not accept that on faith, and how a tool description can influence a model.

**Points:** 5

**Rubric (1 point each):**

1. A defective or malicious server could advertise a harmless purpose and do something else.
2. Evaluating a candidate takes source inspection, sandboxing, provenance, or other evidence appropriate to the deployment.
3. Recalls the Chapter 1 point that a system prompt is a request, not a gate.
4. A tool description placed in Claude's context is more text competing for influence there.
5. A misleading description can steer which tool gets chosen before any runtime check runs.

**Source:** Discovery reveals a declared capability

## ES-ch08.19

'Discovery is not consent to call.' Explain this with a contrast between a read-only server and a write-capable server whose listings are equally well formed.

**Points:** 5

**Rubric (1 point each):**

1. A host can learn which tools exist and still deny them under its permission policy.
2. A read-only tool may suit public course fixtures and not restricted material.
3. A write-capable server needs a different action boundary.
4. This holds even when its listing is equally well formed.
5. Concludes that a well-formed listing is evidence about capability, not permission to call.

**Source:** Discovery reveals a declared capability

## ES-ch08.20

A `tools/call` can go wrong at three layers. Name them, give the lookup example of each, and say what a host learns by reading the reply this way.

**Points:** 5

**Rubric (1 point each):**

1. Lifecycle: the call came too early.
2. Request: the tool or its arguments are wrong, such as an unknown tool or a bad `key`, reported as `-32602`.
3. Task: the lookup ran and found nothing, reported as a result with `isError` true.
4. The reply tells you which layer failed, if you read it that way.
5. Request-validation failures mean the tool never produced a content result.

**Source:** Requests, identifiers, and tool results

## ES-ch08.21

Why is a missing record a tool result with `isError: true` and not a JSON-RPC error? What does that let a host do, and what mistake does the chapter name?

**Points:** 5

**Rubric (1 point each):**

1. The request was well formed, the method existed, and the tool ran its lookup.
2. The failure belongs to the task result, whose text is `Record not found`.
3. Keeping the layer distinct lets a host decide whether to revise the arguments, report an absence, or stop.
4. It avoids treating every negative as a broken protocol.
5. A host that ignores `isError` and presents `Record not found` as an ordinary fact misuses a well-formed result.

**Source:** Requests, identifiers, and tool results

## ES-ch08.22

Explain two limits that apply to every reply: what a matching identifier does not prove, and why returned content stays untrusted.

**Points:** 5

**Rubric (1 point each):**

1. A matching id shows which response belongs with which request.
2. It says nothing about whether the tool used the intended data.
3. It says nothing about whether the result is safe to pass on.
4. The content stays untrusted data: a successful response containing text does not make the text correct.
5. In this fixture the mapping is declared in source so you can compare directly, while a different server's result needs provenance appropriate to where it came from.

**Source:** Requests, identifiers, and tool results

## ES-ch08.23

Using the transition table, explain what a list of isolated JSON examples hides. Use two pairs of rows.

**Points:** 5

**Rubric (1 point each):**

1. `tools/list` fails in row 2 and succeeds in row 7.
2. The only difference between those rows is history.
3. Rows 3 and 6 receive the same response, which is none.
4. In row 3 nothing changes, while in row 6 readiness begins.
5. Concludes that a message must be read together with the prior state, not alone.

**Source:** History is part of the protocol

## ES-ch08.24

A fresh server receives, in order: (1) `tools/list` with id 1, (2) `initialize` with id 2, (3) `tools/list` with id 3, (4) `notifications/initialized`, (5) `tools/list` with id 5. Predict the response and the (initialized, ready) state after each message.

**Points:** 5

**Rubric (1 point each):**

1. Message 1: error `-32000`, state stays F, F.
2. Message 2: a result with version `2025-11-25`, state T, F.
3. Message 3: error `-32000` again, state stays T, F.
4. Message 4: no response, state T, T.
5. Message 5: a result listing one tool, `lookup`, state stays T, T.

**Source:** History is part of the protocol

## ES-ch08.25

Explain why a method named `bad` can receive different error codes, and what an error code does and does not tell you. Include the two parse-level cases in stdio mode.

**Points:** 5

**Rubric (1 point each):**

1. Sent to a ready server, `bad` receives `-32601`.
2. Sent in row 2's state it would have received `-32000`.
3. An error code reports the branch the server reached, not every defect the message had.
4. The text `{` fails before the handler: the main loop catches a parsing `ValueError` and emits `-32700` with a null id.
5. The text `{}` parses and receives `-32600`, so the raw text should be preserved to tell the two apart.

**Source:** History is part of the protocol

## ES-ch08.26

The chapter names two behaviors 'never chosen by anyone'. Identify them, and explain why the chapter does not call them bugs or specification violations.

**Points:** 5

**Rubric (1 point each):**

1. A second `initialize` sent to a ready server leaves `ready` true.
2. A `tools/call` sent without an id is dropped without a response, even when the server is ready.
3. Neither behavior is pinned by the lesson's tests.
4. The chapter does not claim to know what the specification requires for either.
5. They are what the code does because nothing said otherwise, which is the cost of leaving a handshake rule implicit.

**Source:** History is part of the protocol

## ES-ch08.27

Describe what the default demo and the `--stdio` mode do, and why you should not infer production transport guarantees from the stdio loop.

**Points:** 5

**Rubric (1 point each):**

1. The default demo constructs a server, initializes it, sends the notification, lists tools, prints the response, and exits.
2. The `--stdio` flag opts into reading newline-delimited messages until input ends.
3. The loop reads one line at a time.
4. It prints one JSON response per non-notification result and flushes.
5. It has no framing, cancellation, timeout, concurrency, or security feature beyond that.

**Source:** History is part of the protocol

## ES-ch08.28

Name the four ledgers. For each, state its question, what fills it, and what reopens it. Then say whether one ledger can stand in for another.

**Points:** 5

**Rubric (1 point each):**

1. Protocol: is the exchange well formed and in order; filled by the transcript; reopened by a protocol-version change.
2. Capability: does the code do what the listing says; filled by source inspection, disposable fixtures, and who maintains it; reopened by a new advertised tool or a new release.
3. Permission: does this task allow that capability; filled by the task brief, the data owner, and your policy; reopened by a changed task or broader data scope.
4. Evidence: does the returned content support the claim built on it; filled by comparison with the declared source; reopened by a changed corpus.
5. States that no ledger can stand in for another, and that the ledgers are a teaching device rather than a standard.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## ES-ch08.29

Apply the four ledgers to the teaching lookup. What can each ledger record?

**Points:** 5

**Rubric (1 point each):**

1. Protocol ledger: a legal initialization and call.
2. Capability ledger: the code reads one in-memory mapping and performs no file write.
3. Permission ledger: whether the public fixture is allowed for the classroom task.
4. Evidence ledger: a comparison of `505A Dana Hall` with the declared fixture source.
5. States that none of these records can stand in for another.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## ES-ch08.30

Consider two cases: (a) the protocol ledger is perfect but the capability ledger reveals an undeclared write; (b) the capability is properly read-only but the returned fixture is stale. For each, say what succeeds and what fails, and what the word 'passed' must always include.

**Points:** 5

**Rubric (1 point each):**

1. Case (a): the connection succeeds and the behavior exceeds the task boundary.
2. Case (a): the failure appears in the capability ledger, not the protocol ledger.
3. Case (b): permission is satisfied.
4. Case (b): the evidence claim fails.
5. 'Passed' must always name which review passed.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## ES-ch08.31

How should you record what you did not inspect, and why does the last column of the ledger table turn a verdict into a bounded decision?

**Points:** 5

**Rubric (1 point each):**

1. Write 'uninspected', not 'none'.
2. The absence of observed harm in a test you did not perform is not evidence that the capability is absent.
3. For a closed-source server, advertised behavior may be the only evidence available, and the decision should say so.
4. The 'what reopens it' column bounds the decision by naming the changes that trigger review.
5. Trust becomes a decision over identifiable inputs that reopens when one changes, not a permanent property of a server's name.

**Source:** Compatibility is not authorized: Four ledgers for one connection decision

## ES-ch08.32

Where does the server's responsibility end, and what do the host and client decide? Why can the teaching server not demonstrate the client's side, and what would a complete interoperability test need?

**Points:** 5

**Rubric (1 point each):**

1. The server's responsibility ends at its reply, and the host decides what enters context.
2. The client must decide whether it supports the server-selected version, and the specification's fallback route depends on that decision.
3. The teaching server implements only the server object, so it cannot demonstrate the client's behavior.
4. A complete interoperability test needs both sides, or an explicit harness that represents the client's obligations.
5. Names at least three host defenses (approval before consequential tools, independent argument validation, restricted data access, call caps, result verification) and notes the chapter does not claim any particular host implements all of them.

**Source:** Compatibility is not authorized: The host is part of the mechanism

## ES-ch08.33

You are recording an actual host integration. What host configuration belongs in the record, what stays out, and why?

**Points:** 5

**Rubric (1 point each):**

1. Include the command and the working directory.
2. Include the environment boundary and the enabled tools.
3. A transcript without configuration leaves the source of the server ambiguous.
4. Leave out secrets.
5. Do not commit credentials or private paths to make the record complete.

**Source:** Compatibility is not authorized: The host is part of the mechanism

## ES-ch08.34

Explain 'laundering' as the chapter uses it, including what each hop in the lookup chain adds and what none of them checked.

**Points:** 5

**Rubric (1 point each):**

1. A valid text result is inserted into Claude's context and restated fluently, until a string a server produced reads as an established fact.
2. The JSON-RPC envelope gives the text the shape of a protocol-valid reply, and the matching id gives it the look of an answer to your question.
3. `isError: false` gives it the look of success.
4. Claude's sentence gives it fluency.
5. None of those hops checked the content: polish is not provenance.

**Source:** Compatibility is not authorized: Laundering: valid transport, borrowed authority

## ES-ch08.35

Fill in the chapter's handoff table for the course lookup: for each of the three handoffs, say what passes, what it is trusted to be, and how that trust is earned. Then say what an unverified handoff allows.

**Points:** 5

**Rubric (1 point each):**

1. States the defense: treat each handoff as a decision and write down what is passed, what it is trusted to be, and how that trust was earned.
2. Server to host: the reply carrying `505A Dana Hall`, trusted to be the fixture's value for key `office` from this server version, earned by comparison with the mapping in the inspected source.
3. Host to Claude's context: that text as data to cite with its role, not an instruction and not a current fact, earned by the recorded host configuration and your instruction about how the text may be used.
4. Claude to answer: a sentence such as 'The course fixture lists the office as 505A Dana Hall', earned by keeping the fixture role and tracing the value to the source comparison.
5. A handoff with no verification lets an unverified output travel onward wearing the authority of every clean step it passed through.

**Source:** Compatibility is not authorized: Laundering: valid transport, borrowed authority

## ES-ch08.36

From the first row of the handoff table, what may the host infer and what may it not? What is the right continuation when the tool returns a missing record, and why can the model's own loop not be relied on to stop a guess?

**Points:** 5

**Rubric (1 point each):**

1. The host may infer that this server returned the displayed fixture text for a particular request under the recorded implementation.
2. It may not infer that an external fact is current or universally correct without another source check.
3. The phrasing is narrower because the evidence is narrower.
4. For a missing record, the right continuation is the absence itself plus a decision about whether to ask another authorized source.
5. Nothing in the loop that produces Claude's next token stops a fluent guess; the stop must be a rule written into the host or instruction and a check run on the answer afterward.

**Source:** Compatibility is not authorized: Laundering: valid transport, borrowed authority

## ES-ch08.37

State the contract for the state machine that the gate asks you to write.

**Points:** 5

**Rubric (1 point each):**

1. Tool operations are refused until initialize and then the initialized notification have both arrived, in that order.
2. A notification never produces a response.
3. Every response carries the id of the request it answers.
4. A tool-level negative is a result with `isError`, while a protocol-level problem is an error with a code.
5. The subset does not claim version negotiation.

**Source:** The gate: write the connection decision before you connect

## ES-ch08.38

For the task of finding the office for key `office` from the declared course fixture, write the connection contract: what each of the permission, capability, and evidence ledgers must contain, and what each entry needs.

**Points:** 5

**Rubric (1 point each):**

1. Permission ledger: names the sources the task may read, the effects it may have (none beyond returning text), and where results may go.
2. Capability ledger: lists the claims to check in source: one mapping, no write, no network.
3. Evidence ledger: requires that every value Claude may cite be compared with the declared source first.
4. Every entry is given an evidence type.
5. Names at least four of the five evidence types: advertised, source-inspected, executed on a fixture, independently sourced, uninspected.

**Source:** The gate: write the connection decision before you connect

## ES-ch08.39

Describe the three constructed wrong versions your checks must catch, and which ledger or test catches each.

**Points:** 5

**Rubric (1 point each):**

1. A server that sets `ready` inside the initialize branch skips the notification, and applied to a copy of the reference it leaves all six of the lesson's tests passing.
2. The case that fails it, `tools/list` after initialize and before the notification, is not among the lesson's tests.
3. A `lookup` with a flawless lifecycle that appends to a log file on every call passes the protocol ledger and fails the capability ledger.
4. A read-only `lookup` whose fixture value disagrees with the declared source passes three ledgers and fails the evidence ledger.
5. If your checks cannot tell these from the right server, the gate is not finished.

**Source:** The gate: write the connection decision before you connect

## ES-ch08.40

Explain the failure sentence, the pass condition, and the role of a qualified reviewer in the gate.

**Points:** 5

**Rubric (1 point each):**

1. The failure sentence is written and dated before you read any transcript, saying what you would see if your table were wrong.
2. If it is written after reading the output, you have described the output.
3. The pass condition is that a stranger holding your transcript, the source, and the task brief can mark every line of the four ledgers with an evidence type.
4. The stranger finds no empty cell, no word like safe or trusted without a named evidence type, and a re-review trigger beside the decision.
5. Whether the fixture is public needs a qualified reviewer, its owner, and you should record who that is.

**Source:** The gate: write the connection decision before you connect

## ES-ch08.41

Why does the chapter ask you to build the state machine by hand before consulting the reference, and what are the build steps?

**Points:** 5

**Rubric (1 point each):**

1. Your own version is the record of what you understood before Claude touched anything.
2. It is also the instrument you will measure Claude's version against.
3. Create the two flags and the base message validation, implement initialize and then the initialized notification, and test both orders.
4. Add `tools/list` behind the readiness check, then the lookup tool, separating malformed arguments, unknown tool, known record, and missing record.
5. Once you can explain your version, compare it with the reference and name a difference in behavior, not in line count or style.

**Source:** Build It: implement the state machine before connection

## ES-ch08.42

Describe how to use the six existing tests, and which lifecycle case you should add and why.

**Points:** 5

**Rubric (1 point each):**

1. Read the six existing tests before the reference and predict each error code or state.
2. Add one malformed-argument case and one lifecycle case the suite lacks.
3. The best candidate is initialize, then `tools/list` without the notification, which must still return `-32000`.
4. That case catches the ready-on-initialize change, which leaves all six existing tests passing.
5. State what remains outside the subset.

**Source:** Build It: implement the state machine before connection

## ES-ch08.43

Describe how to conduct Claude Code against your gate and what to do with what it returns, including what you preserve.

**Points:** 5

**Rubric (1 point each):**

1. Give Claude the gate (transition table, contract, test list), not your implementation.
2. Ask for a server that satisfies the contract and passes your tests, then run your tests on what it returns yourself.
3. Note which tests failed, since a failing test is often a gap in your gate that Claude could not see.
4. Compare its server with your baseline and name one difference in behavior.
5. Preserve the actual transcript (prompt, plan, diff, commands, outputs, date, displayed model label), and if a session failed or did not run, record that rather than substituting a fixture.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## ES-ch08.44

Explain how to test whether your own tests are strong enough, using a deliberately wrong server and a control. What do you do when a case slips through?

**Points:** 5

**Rubric (1 point each):**

1. Ask Claude for a deliberately wrong server that still passes your tests, and run your tests against it.
2. As a control, make the ready-on-initialize change to a copy of your own server and run the same tests.
3. If the tests do not catch it, your list was too weak, and you found out cheaply.
4. A case your gate missed reopens the gate: revise it, date the revision, and keep the original.
5. Designing first is not freezing the design.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## ES-ch08.45

Describe the discrepancy prompt: what you give Claude, what you ask for, what you withhold, and what you do with the answer.

**Points:** 5

**Rubric (1 point each):**

1. You provide a transcript, the server source, and the advertised description.
2. You ask for every place where they disagree, or where one claims more than another supports, with the line relied on quoted.
3. You withhold the verdict: no advice on whether to connect, and no calling any behavior safe.
4. You check every item against the source yourself, since some will be wrong and an item's absence is not evidence that no discrepancy exists.
5. The decision is yours: allow, deny, or pending, in your own words.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## ES-ch08.46

Explain the trap in using a server's import list as evidence that it cannot write files, and say what evidence does establish it. Then say how to treat an external candidate whose inspection is incomplete.

**Points:** 5

**Rubric (1 point each):**

1. The reference imports only `argparse`, `json`, and `sys`.
2. That proves nothing about files, because `open` is a builtin and needs no import.
3. What establishes that the lookup writes nothing is the call branch itself, where the only data consulted is a literal mapping.
4. For an external candidate, use only source and documentation you have actually inspected, and record the decision as pending or deny if inspection is incomplete.
5. Do not invent a server's behavior from its tool description, and note that the exercise certifies no external package.

**Source:** Use It: conduct Claude Code, then ask it for discrepancies, not a verdict

## ES-ch08.47

A student's evaluation packet contains only the `tools/list` output and the sentence 'looks safe'. List what is missing.

**Points:** 5

**Rubric (1 point each):**

1. A chronological transcript preserving requests, notifications, responses, identifiers, state transitions, and errors.
2. One successful and one failing call with matching ids, and an explanation of why the missing record is a tool error and not a protocol error.
3. For each capability: what the server says, what source inspection shows, which disposable tests ran, and what remains unknown.
4. An allow, deny, or pending decision for the bounded task, with a reason.
5. Says a valid tool listing belongs in the evidence but is not the decision, and that 'safe' needs a named evidence type.

**Source:** Ship It: an MCP evaluation packet

## ES-ch08.48

In your packet, a fixture value is deliberately wrong. Where should it be caught, which ledger catches it, and what must you not conclude?

**Points:** 5

**Rubric (1 point each):**

1. The packet includes a handoff analysis: the three-row table filled in for your own run.
2. The source comparison that catches the wrong value must be shown, and it must happen before generation.
3. The evidence ledger is the one that fails.
4. You must not call the protocol exchange failed when the factual check is what rejects the value.
5. Notes the wrong value still passes the protocol, capability, and permission ledgers.

**Source:** Ship It: an MCP evaluation packet

## ES-ch08.49

Describe the sign-off template line by line: what goes on each line, and what the 'Not checked' and 'Not claiming' lines are for.

**Points:** 5

**Rubric (1 point each):**

1. Checked: which ledger lines, and the evidence type for each.
2. How: by hand, by a test written before reading the reference, by source comparison, or with Claude's help, saying which parts.
3. Not checked: examples such as network behavior, other versions of the server, client-side version handling, and whether the fixture is true in the world.
4. Not claiming: that the server is secure, conformant to MCP, or endorsed beyond this task and version.
5. Decision (allow, deny, or pending, for a named task and server version), a re-review trigger, and a signed or withheld line with name and date.

**Source:** Ship It: an MCP evaluation packet

## ES-ch08.50

Distinguish the decision from the sign-off, and say which verbs the evidence earns.

**Points:** 5

**Rubric (1 point each):**

1. The decision is about the server, while the sign-off is about your evidence for the decision.
2. You can sign a deny, and you can withhold your signature from an allow that your evidence does not support.
3. The 'Not checked' line is the one an AI-written sign-off leaves empty, because the system has no record of what you did not do.
4. Earned verbs: recorded for a transcript, inspected for source you read, executed for a fixture you ran, compared for a source check.
5. Secure, trusted, and verified need a criterion this exercise never supplies.

**Source:** Ship It: an MCP evaluation packet

## ES-ch08.51

Using the driver's seat table, divide the work on out-of-order and malformed messages and on implementing the state machine, and give the reason each part stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Claude can generate many out-of-order and malformed messages quickly and run them.
2. You decide the expected response for each message.
3. The expected response is the contract, and the code cannot supply it.
4. Claude can implement the state machine from your gate and write tests, but you build your own baseline first and run your tests, including against a wrong server.
5. You cannot audit a lifecycle you have not built.

**Source:** The driver's seat

## ES-ch08.52

Using the driver's seat table, divide the work on the lifecycle page, on classifying the data, and on allow, deny, or pending, and give the reason each part stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Claude can quote and summarize the lifecycle page, but you check the clauses and keep the version claim narrow.
2. A recollection of a protocol is not the protocol.
3. Claude can draft the capability inventory, but you decide what the data is and what the task may touch.
4. Classification and scope are facts about your world that a transcript does not contain.
5. Claude can draft the packet, but you decide, set the re-review trigger, and sign or withhold, since the decision carries your name and the cost of a wrong one lands on whoever owns the data.

**Source:** The driver's seat

## ES-ch08.53

Does the chapter claim that Claude cannot reason about trust decisions? Explain what it does claim.

**Points:** 5

**Rubric (1 point each):**

1. The trust decision rests on facts about the world around the transcript.
2. Names those facts: who owns the data, what the task needs, what a wrong answer costs, and who maintains the server.
3. The transcript contains none of them.
4. The claim is not that Claude is incapable of reasoning about such facts; in this task they are not among its inputs unless you supply them.
5. Accountability for a wrong decision lands on a person.

**Source:** The driver's seat

## ES-ch08.54

Explain what it means to read the transcript 'in both directions', and what a tool list or tool result in isolation leaves out.

**Points:** 5

**Rubric (1 point each):**

1. Reading as the server: given this state and message, which branch runs, what response it produces, and what state changes.
2. Reading as a reviewer: given this response, which request and prior transition must be present before the interpretation is justified.
3. The two passes catch different omissions.
4. A tool list in isolation omits the initialize request, the notification, the process configuration, and the source version; a tool result in isolation loses the arguments and identifier.
5. Every error code you report should be attached to the raw constructed message and server state it came from, because 'MCP failed' erases the mechanism.

**Source:** Verify and reflect

## ES-ch08.55

Describe the correspondence review between transcript and source, and the 'what did not happen' row you should add. Why must you not call the subset conformant?

**Points:** 5

**Rubric (1 point each):**

1. The review checks that the advertised tool name matches the dispatch branch.
2. It checks that the schema matches the argument validation and that `isError` appears for the recorded missing key.
3. It is stronger than the listing or code inspection alone, and it is still evidence about the tested implementation and version.
4. The default demo did not connect to Claude, expose a network port, write a file, authenticate a user, or validate a production deployment.
5. A narrow server can be complete as a teaching artifact and incomplete as a product, and a happy path that resembles the specification does not make it conformant.

**Source:** Verify and reflect

## ES-ch08.56

Describe the 'Too early' Assessment, including what you must explain and what test you must write.

**Points:** 5

**Rubric (1 point each):**

1. Send `tools/list` before readiness and preserve the code.
2. Complete initialization and retry.
3. Explain the changed state rather than calling the first message malformed.
4. Write the test that stops the ready-on-initialize change.
5. Show that test failing against that change.

**Source:** Assessments - ungraded practice

## ES-ch08.57

A student says: 'I had Claude Code build the server and tell me it was safe, then I signed the sign-off.' Using the chapter's three jobs, say what the student skipped.

**Points:** 5

**Rubric (1 point each):**

1. Conduct was skipped: no lifecycle table, four-ledger contract, or wrong servers were written before Claude saw any code.
2. Check was skipped: no record of what a wrong server would show, and no separate evidence types for each ledger.
3. 'Safe' without a named evidence type fails the pass condition, since secure, trusted, and verified need a criterion the exercise never supplies.
4. Drive was misapplied: the student handed Claude the question of whether to connect, which the chapter keeps with the human.
5. The sign-off should be written from the student's own record, since an AI-written sign-off leaves the 'Not checked' line empty.

**Source:** What you can now trace

## ES-ch08.58

Why does the chapter end by saying that connecting a tool is not training a model, and what does it set up for Chapter 9?

**Points:** 5

**Rubric (1 point each):**

1. An MCP server can add information and actions to a host without changing model parameters.
2. That distinction is the bridge to Chapter 9.
3. Chapter 9 implements a tiny logistic predictor whose weight and bias genuinely update under a loss function.
4. It compares that mechanism with changes to prompts, context, tools, and settings.
5. The gate question comes with us: before you change anything, state what should change and what would show that it did.

**Source:** Connecting a tool is not training a model

## ES-ch08.59

What does the 'Anthropics' section ask you to do with Anthropic's MCP builder materials and evaluation guide, and what does it say not to do?

**Points:** 5

**Rubric (1 point each):**

1. Compare your server with Anthropic's MCP builder materials and evaluation guide, which were checked through the course research on 2026-09-06.
2. Identify one answerable task and an independently verifiable result for the read-only fixture.
3. Keep the versioned specification as the protocol authority.
4. Do not treat upstream examples as permission to connect an unreviewed server.
5. Do not install an external skill merely because the links exist.

**Source:** Anthropics

## ES-ch08.60

Apply the Conducting AI test to the check 'ask Claude whether `505A Dana Hall` looks right'. Why is it weak, what is a stronger check, and what exercise does the chapter propose for each check in your packet?

**Points:** 5

**Rubric (1 point each):**

1. An audit reduces error only to the degree that the checker fails differently from the thing it checks.
2. Asking Claude whether the value looks right, with no source in hand, judges plausibility.
3. Plausibility is the ground the original answer stood on.
4. Comparing the value with the mapping in the inspected source fails in an unrelated way: it errors loudly and cannot be persuaded.
5. For each check, write one sentence on how it can fail and one on how the thing it checks can fail; if the two match, you have a repeat, not a check.

**Source:** Conducting AI

## ES-ch08.61

What does a successful MCP exchange establish, what does it not establish, and how does the chapter divide the final responsibilities between Claude and the human?

**Points:** 5

**Rubric (1 point each):**

1. A successful exchange establishes transport behavior.
2. It does not make the returned value true.
3. It does not authorize the next action.
4. Claude can organize and inspect the transcript and propose which source to compare against.
5. The human decides whether the server, data, and action scope are appropriate for the task.

**Source:** Conducting AI
