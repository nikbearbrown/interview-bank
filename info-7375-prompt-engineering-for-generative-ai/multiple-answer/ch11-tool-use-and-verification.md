# Chapter 11: Tool use and verification

## MA-ch11.1

Check each statement that is true about the chapter's opening fixture, in which the tool returned 42 and the assistant then said 99. Each statement is worth 1 point (5 points total).

- [ ] A. The 99 came from a live Claude session that happened to make an arithmetic error.
- [ ] B. The fixture was deliberately constructed and run offline for the chapter's research.
- [ ] C. The controller reported its own status as finished.
- [ ] D. The tool returned 42 and the assistant's final sentence said 99.
- [ ] E. The controller compared the assistant's final sentence with the tool result before reporting its status.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The 99 came from a scripted fixture, not a live transcript.
- B: The chapter calls it a deliberately constructed offline fixture.
- C: The reported status was finished.
- D: That is the 42-versus-99 trace.
- E: The controller never compared the final sentence with the tool result.

**Source:** Chapter opening (the 42 versus 99 fixture)

## MA-ch11.2

Check each statement that is true about what the opening trace got right. Each statement is worth 1 point (5 points total).

- [ ] A. The request to add 17 and 25 was well formed.
- [ ] B. The result carried the matching identifier.
- [ ] C. A well formed request, a validating dispatcher, a matching identifier, and a recognized loop exit together guarantee that the final sentence is true.
- [ ] D. The dispatcher validated the request.
- [ ] E. The loop ended in a recognized state.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The chapter says the request was well formed.
- B: The result carried the matching identifier.
- C: "A correct recipe is not a check"; the trace can still end in a false sentence.
- D: The dispatcher validated it.
- E: The loop ended in a recognized state.

**Source:** Chapter opening (the 42 versus 99 fixture)

## MA-ch11.3

Check each statement that is true about the four prediction questions the chapter asks before the trace. Each statement is worth 1 point (5 points total).

- [ ] A. One question asks whether Python will accept True as the number 1.
- [ ] B. The chapter says the value of the predictions lies in guessing correctly.
- [ ] C. The chapter asks you to write the predictions down and date them.
- [ ] D. One question asks whether an unknown tool will crash the program or be silently ignored.
- [ ] E. One question asks whether the loop will call the outcome verified when the assistant stops after saying 99.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The first prediction concerns True and the number 1.
- B: The value is not guessing correctly but exposing the model of the machinery you brought.
- C: The predictions are to be written down and dated.
- D: The question is whether an unknown tool becomes a Python exception or a returned tool error.
- E: The question is whether the loop will call that outcome finished.

**Source:** What you will be able to do

## MA-ch11.4

Check each statement that is true about the outcomes the chapter says you should reach. Each statement is worth 1 point (5 points total).

- [ ] A. Audit a final claim using evidence that is chosen to agree with it.
- [ ] B. Design failure behavior on the assumption that every response requests a tool.
- [ ] C. Explain why a tool schema is an invitation rather than an execution engine.
- [ ] D. Match every result to its request identifier and state what that match does not show.
- [ ] E. Validate a proposed call before dispatching it and state what the dispatcher must refuse as a contract you wrote.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The outcome is evidence that can disagree with the claim.
- B: The outcome is bounded failure behavior "rather than assuming every response requests a tool".
- C: A listed outcome.
- D: A listed outcome.
- E: A listed outcome.

**Source:** What you will be able to do

## MA-ch11.5

Check each statement that is true about the three jobs at the scale of one tool call. Each statement is worth 1 point (5 points total).

- [ ] A. A finished status establishes that the controller saw a stop signal.
- [ ] B. Under Conduct, you leave it to the loop to decide what counts as done.
- [ ] C. A fluent sentence at the end of the trace counts as evidence for the claim it states.
- [ ] D. A matching identifier establishes that the final answer is correct.
- [ ] E. Under Conduct, you decide which operations must be exact and therefore live in your program.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: That is all finished establishes.
- B: You decide what the loop may call done.
- C: A fluent sentence establishes nothing.
- D: A matching identifier establishes only who asked.
- E: Exact operations belong in your program, not the model's continuation.

**Source:** Three jobs at the scale of one tool call

## MA-ch11.6

Check each statement that is true about the choice between Claude writing 17 + 25 = 42 and a dispatcher returning 42. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter says Claude's arithmetic is rarely right.
- [ ] B. A dispatcher's 42 comes from an operation you can read, re-run, and break with a test.
- [ ] C. The design question is how often Claude's sentence is right.
- [ ] D. Nothing outside the continuation recomputes the sum when Claude writes it directly.
- [ ] E. When Claude writes 17 + 25 = 42, that sentence is a continuation, ranked and sampled like any other.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It is "very often right".
- B: The dispatcher's number is inspectable and testable.
- C: The question is whether anything in the path would tell you the one time it is not.
- D: Nothing recomputes it.
- E: Chapter 1's loop makes the sentence a sampled continuation.

**Source:** Conduct: what must be exact does not belong in the model

## MA-ch11.7

Check each statement that is true about verifiability-first engineering as the chapter presents it. Each statement is worth 1 point (5 points total).

- [ ] A. The reason given is that the most constrained tool is the one you can check.
- [ ] B. The rule is to choose the most capable model that can do the step.
- [ ] C. Arithmetic, exact lookups, deterministic transforms, and schema validation belong inside the probabilistic layers.
- [ ] D. The "easier to verify" value ranks how reliable each layer is.
- [ ] E. The five-layer capability stack is an industry standard.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The most constrained tool is the one you can check.
- B: The rule is the lowest capability that does the step.
- C: They belong outside the probabilistic layers.
- D: It is not a ranking of reliability.
- E: The stack is a teaching device, not an industry standard.

**Source:** Conduct: what must be exact does not belong in the model

## MA-ch11.8

Check each statement that is true about the book's example of totaling every line item over $10,000 across 200 invoices. Each statement is worth 1 point (5 points total).

- [ ] A. Only the sum, not the filter, is handed to deterministic code in the better design.
- [ ] B. The example concerns 200 invoices and line items over $10,000.
- [ ] C. Extracting fields per invoice and handing the filter and the sum to deterministic code leaves seams where you can compare records with invoices.
- [ ] D. Handing the sum to deterministic code makes the total certain to be correct.
- [ ] E. Asking a chat window for the total gives a number you can audit step by step.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Both the filter and the sum go to deterministic code.
- B: Those are the example's figures.
- C: The seams are where you compare records and recompute the sum.
- D: Deterministic code is inspectable, not infallible.
- E: The chat window gives a fluent number with nothing behind it to audit.

**Source:** Conduct: what must be exact does not belong in the model

## MA-ch11.9

Check each statement that is true about the costs of routing a step out to deterministic code. Each statement is worth 1 point (5 points total).

- [ ] A. In the chapter's division, Claude proposes the call and interprets the trace while Python owns exact argument validation and arithmetic.
- [ ] B. Deterministic code that encodes the wrong formula will produce the error inconsistently, so it is easy to spot.
- [ ] C. Every operation granted to the dispatcher is authority granted.
- [ ] D. A one-tool allowlist is hard to audit because it can do almost nothing.
- [ ] E. Routing a step out makes it inspectable, not infallible.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: That is the deliberate division.
- B: It will encode the wrong formula consistently.
- C: The second honest cost.
- D: It is easy to audit precisely because it can do almost nothing.
- E: The first honest cost.

**Source:** Conduct: what must be exact does not belong in the model

## MA-ch11.10

Check each statement that is true about the `add` tool schema. Each statement is worth 1 point (5 points total).

- [ ] A. The schema authorizes the model to run arbitrary Python.
- [ ] B. The schema tells Claude which request shape the application is prepared to consider.
- [ ] C. The schema imports an `add` function into the model.
- [ ] D. The schema is part of a protocol conversation, while the runtime remains application code.
- [ ] E. The schema proves that the application enforces the schema.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: It grants no such authority.
- B: It describes the request shape.
- C: No function is imported into the model.
- D: The runtime stays in the application.
- E: Enforcement is a separate matter.

**Source:** A tool description does not run a tool

## MA-ch11.11

A model proposes the calls below. Check each statement that is true about how the course `dispatch` function treats them. Each statement is worth 1 point (5 points total).

- [ ] A. Name `add` with input {"a": True, "b": 2} raises ValueError.
- [ ] B. Name `subtract` with input {"a": 5, "b": 3} raises ValueError.
- [ ] C. Name `add` with input {"a": 1} is accepted and b is treated as 0.
- [ ] D. Name `add` with input {"a": 17, "b": 25} returns 42.
- [ ] E. Name `add` with input {"a": 1, "b": 2, "c": 3} is accepted and the extra key is ignored.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The exact-type rule rejects a Boolean.
- B: The name must be exactly add.
- C: A missing key fails the exact-keys rule.
- D: Exact keys, exact int types, finite sum 42.
- E: The keys must be exactly a and b, so the extra key is refused.

**Source:** A tool description does not run a tool

## MA-ch11.12

Check each statement that is true about the Boolean check in `dispatch`. Each statement is worth 1 point (5 points total).

- [ ] A. A specification that never mentions `True` still gives an implementer a reason to refuse it.
- [ ] B. The implementation relies on `isinstance(v, (int, float))` to reject that impostor.
- [ ] C. In Python, `bool` is a subclass of `int`.
- [ ] D. `isinstance(True, int)` is true.
- [ ] E. A casual numerical guard would admit `True + 2` and produce 3.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A silent specification gives no reason to refuse it.
- B: It uses `type(v) not in (int, float)`, not isinstance, to reject it.
- C: The subclass relationship is why the guard matters.
- D: Hence isinstance admits True.
- E: True + 2 gives 3.

**Source:** A tool description does not run a tool

## MA-ch11.13

Check each statement that is true about finite numbers and validation in the `add` tool. Each statement is worth 1 point (5 points total).

- [ ] A. The refusals in the contract are decisions about what the operation means.
- [ ] B. Validation is decoration before the real work.
- [ ] C. Infinity and not-a-number are ints in Python.
- [ ] D. A JSON-facing description that says "number" tells Python exactly which values to accept.
- [ ] E. Two finite inputs always produce a finite sum.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The refusals are decisions, and they are the author's.
- B: Validation defines what the operation means.
- C: They are floats.
- D: Python still needs rules for the values it actually receives.
- E: Finite inputs can overflow when added, so the result is checked separately.

**Source:** A tool description does not run a tool

## MA-ch11.14

Check each statement that is true about why the application, not the model, dispatches the proposed name. Each statement is worth 1 point (5 points total).

- [ ] A. Exact argument rules replace the need for an allowlist.
- [ ] B. A tool schema is a substitute for the dispatcher's enforcement checks.
- [ ] C. An allowlist gives the application a closed set of operations.
- [ ] D. Chapter 5 said the model should decide who may do what.
- [ ] E. Letting the model decide how to execute the name collapses description, authority, and implementation into one unreviewable gesture.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Argument rules narrow each operation within the allowlist; they do not replace it.
- B: Schemas help form proposals but do not enforce.
- C: The allowlist is the closed set.
- D: Who may do what is a human decision.
- E: That is the chapter's objection.

**Source:** Dispatch belongs to the application

## MA-ch11.15

Check each statement that is true about the result builder that catches ValueError. Each statement is worth 1 point (5 points total).

- [ ] A. The application pretends the tool ran and returns a default value.
- [ ] B. A caught ValueError becomes a tool_result that carries the request's identifier.
- [ ] C. A rejected proposal is designed to crash the whole conversation.
- [ ] D. The model can see that a particular request failed and why.
- [ ] E. That result is marked `is_error: True`.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The application does not pretend the tool ran.
- B: The row repeats the identity.
- C: The conversation does not crash.
- D: The error becomes evidence for the next turn.
- E: The error flag is set.

**Source:** Dispatch belongs to the application

## MA-ch11.16

Check each statement that is true about what the result builder deliberately does not catch. Each statement is worth 1 point (5 points total).

- [ ] A. "Catch everything" is a form of verification.
- [ ] B. An unexpected programming defect should not be laundered into a routine model-visible message.
- [ ] C. It catches only ValueError, a bounded and anticipated validation failure.
- [ ] D. Catching every exception and relabeling it as a tool error would be stronger verification.
- [ ] E. Relabeling a defect as a routine tool error would let the host stop in a known state.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The chapter says it is not.
- B: Laundering a defect hides it.
- C: ValueError is the anticipated failure.
- D: Catch-all is not verification.
- E: The host would continue in an unknown state.

**Source:** Dispatch belongs to the application

## MA-ch11.17

Check each statement that is true about what a request identifier does and does not establish. Each statement is worth 1 point (5 points total).

- [ ] A. The identifier answers which result belongs to which request.
- [ ] B. Like a luggage tag, the identifier inspects what is inside the suitcase.
- [ ] C. A result matched to the right request must be correct.
- [ ] D. A matched result can still be wrong because the dispatcher contains a bug.
- [ ] E. Because the identifier matches, stale data from an external service cannot be the cause of a wrong result.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Its job is correspondence.
- B: A tag helps establish ownership, not contents.
- C: Correspondence is not correctness.
- D: A dispatcher bug survives a matching ID.
- E: A matched result can still be wrong because of stale data.

**Source:** Identifiers create correspondence, not truth

## MA-ch11.18

Check each statement that is true about the duplicate-identifier guard in `results`. Each statement is worth 1 point (5 points total).

- [ ] A. The `seen` set is local to one invocation of `results`.
- [ ] B. "Duplicate identifiers within one processed assistant content batch are rejected" matches the implementation.
- [ ] C. The guard establishes global uniqueness across every turn of a conversation.
- [ ] D. "Duplicate identifiers are rejected" is the precisely scoped statement of the guard.
- [ ] E. `results` raises ValueError when two tool requests in one content batch share an identifier.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A fresh set is made on each call.
- B: That wording states the scope of the check.
- C: Uniqueness is only within one batch.
- D: That wording is too broad.
- E: The executed fixture observed this rejection.

**Source:** Identifiers create correspondence, not truth

## MA-ch11.19

Check each statement that is true about how the `loop` controller is set up. Each statement is worth 1 point (5 points total).

- [ ] A. The loop appends a response to `trace` only when that response requests a tool.
- [ ] B. Injecting `call` is what makes the controller testable offline.
- [ ] C. `max_turns` must be an integer from one through four.
- [ ] D. Optional live transport requires writing a different controller.
- [ ] E. `loop` accepts a callable named `call`, a request body, and a bounded number of turns.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Each response is appended to the trace.
- B: A fixture can return known response dictionaries.
- C: That is the setup check.
- D: A live transport uses the same controller through a different callable.
- E: Those are the parameters.

**Source:** The controller is a message machine

## MA-ch11.20

Check each statement that is true about the exits of the `loop` controller. Each statement is worth 1 point (5 points total).

- [ ] A. A `max_tokens` stop is reported as `finished`.
- [ ] B. A `tool_use` stop that contains no tool calls is quietly returned as `stopped`.
- [ ] C. A stop reason of `end_turn` returns status `finished` with the trace.
- [ ] D. A stop reason other than `tool_use` and `end_turn` returns status `stopped` with the reason preserved.
- [ ] E. A `tool_use` stop ends the loop immediately with status `stopped`.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The fixture's max_tokens case is expected to be stopped.
- B: It raises an error instead.
- C: The first exit.
- D: The second exit preserves the reason.
- E: A tool_use stop builds results, appends them, and continues unless the budget is exhausted.

**Source:** The controller is a message machine

## MA-ch11.21

Check each statement that is true about the turn budget. Each statement is worth 1 point (5 points total).

- [ ] A. Four repeated calls can consume the budget without moving the task forward.
- [ ] B. A turn budget certifies safety.
- [ ] C. A turn budget guarantees progress.
- [ ] D. A budget of four turns makes any single turn safe.
- [ ] E. A turn budget prevents unbounded continuation.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Repetition can use it all.
- B: It does not certify safety.
- C: It does not guarantee progress.
- D: An unauthorized operation could be damaging on the first turn.
- E: That is its purpose.

**Source:** The controller is a message machine

## MA-ch11.22

Check each statement that is true about the word `finished` and the word `verified`. Each statement is worth 1 point (5 points total).

- [ ] A. The word verified belongs to a claim whose claim-specific check passed.
- [ ] B. Each exit should be named for the evidence behind it.
- [ ] C. Renaming the `finished` exit to `verified` would make the final sentence verified.
- [ ] D. `finished` names a controller state.
- [ ] E. Had the same state been called `verified`, downstream code would still read the mechanism rather than the name.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Reserve verified for a passed claim-specific check.
- B: Name exits for their evidence.
- C: A rename changes the label, not the evidence.
- D: It is a controller state.
- E: Downstream code would read the name and not the mechanism.

**Source:** The controller is a message machine

## MA-ch11.23

Check each statement that is true about why the worked example uses scripted responses. Each statement is worth 1 point (5 points total).

- [ ] A. Model variability would be useful evidence about the Python mechanism.
- [ ] B. Scripted responses isolate the controller's behavior.
- [ ] C. Scripted responses avoid spending API credits.
- [ ] D. The research run recorded its pieces separately: `results` on a good and a bad block, the duplicate rejection, and a loop whose single scripted response says 99.
- [ ] E. The two-turn trace in the chapter is a single recorded run of a live Claude session.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Model variability is not evidence about the Python mechanism.
- B: Controller behavior is isolated from model behavior.
- C: No credits are spent.
- D: Those were the separately recorded pieces.
- E: The two-turn trace composes the pieces, and `sum-1` is an illustrative identifier.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.24

Check each statement that is true about running `results([valid])` on the `sum-1` block with a=17 and b=25. Each statement is worth 1 point (5 points total).

- [ ] A. `dispatch` computes 17 + 25 as 42.
- [ ] B. The recorded run shows that Claude chose the right operands.
- [ ] C. `json.dumps(42)` returns the integer 42, so the result's content is an integer.
- [ ] D. The result block's `tool_use_id` is "42".
- [ ] E. `results` confirms that `sum-1` is a new nonempty string.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Both values are exact ints and finite, and the sum is 42.
- B: The fixture says nothing about who chose the operands.
- C: json.dumps serializes 42 to the string "42".
- D: The `tool_use_id` repeats the request identifier, `sum-1`.
- E: The block must have a new nonempty string identifier.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.25

Check each statement that is true about what the recorded 42 result supports. Each statement is worth 1 point (5 points total).

- [ ] A. It records 42 together with matching identifiers.
- [ ] B. It is evidence that the live API behaved in some unrecorded way.
- [ ] C. It supports claims about this implementation under this fixture.
- [ ] D. It is evidence that Claude chose the right operands.
- [ ] E. It is evidence that every external tool call is correct.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The research script recorded 42 with matching identifiers.
- B: Live behavior was not recorded.
- C: That is its scope.
- D: Operand choice is not tested by the fixture.
- E: Nothing about external calls was observed.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.26

Check each statement that is true about changing one boundary at a time in the `sum-1` example. Each statement is worth 1 point (5 points total).

- [ ] A. Two tool-use blocks with ID `sum-1` in one batch produce two error results.
- [ ] B. `results` turns that rejection into a result tied to `sum-1` with `is_error: True`.
- [ ] C. The model may repair an invalid argument after receiving an error result.
- [ ] D. Replacing the tool name with `subtract` is rejected by the allowlist.
- [ ] E. Replacing 17 with `True` is rejected by the exact-type rule.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The duplicate-ID guard raises instead.
- B: The failure is represented to the model.
- C: Per-call dispatch failures can be repaired by the model.
- D: Unknown names are not on the allowlist.
- E: The Boolean is refused by type.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.27

Check each statement that is true about the status `finished` in the two-response example. Each statement is worth 1 point (5 points total).

- [ ] A. That status is silent about arithmetic.
- [ ] B. The controller returns `finished`.
- [ ] C. That status is correct about the controller.
- [ ] D. That status means the final claim agrees with the tool evidence.
- [ ] E. That status means the response used the controller's recognized completion signal before the request budget expired.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It says nothing about 17 + 25.
- B: The status is finished.
- C: It accurately describes the controller.
- D: It does not mean the claim agrees with the tool evidence.
- E: That is what finished means.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.28

Check each statement that is true about independence in the check `claimed == expected`. Each statement is worth 1 point (5 points total).

- [ ] A. With expected = 17 + 25 = 42 and claimed = 99, the comparison rejects the claim.
- [ ] B. Two routes that share the same incorrect source data are independent merely because their code differs.
- [ ] C. Calling the same buggy helper twice is corroboration.
- [ ] D. For elementary arithmetic, a hand calculation is genuinely independent of the helper being audited.
- [ ] E. In a consequential system, independence should be designed around failure modes, not assumed.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: 99 does not equal 42.
- B: Shared data defeats independence.
- C: It is repetition, not corroboration.
- D: Hand arithmetic avoids the dispatcher entirely.
- E: Design independence around failure modes.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.29

Check each statement that is true about the evidence matrix in the worked example. Each statement is worth 1 point (5 points total).

- [ ] A. For the claim "final answer is correct", completion establishes it.
- [ ] B. For the claim "Python produced 42", the matching `tool_result` content establishes that 42 is the correct answer to the intended task.
- [ ] C. For the claim "Claude proposed add(17, 25)", the evidence is the recorded `tool_use` block.
- [ ] D. For the claim "result belongs to sum-1", the matching identifier establishes request/result correspondence.
- [ ] E. For the claim "loop completed", `end_turn` and `finished` establish that the final answer is right.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Nothing is established until the claim is compared with 42.
- B: It establishes only the output of this implementation.
- C: The trace holds the proposal.
- D: That is what the identifier shows.
- E: They show only that the controller recognized completion.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.30

Check each statement that is true about the final row of the evidence matrix, the teardown. Each statement is worth 1 point (5 points total).

- [ ] A. Which approach is appropriate is the same whatever the stakes and task semantics.
- [ ] B. A polished sentence at the end of a correct-looking trace is a new claim.
- [ ] C. Evidence automatically flows into narration.
- [ ] D. The application can parse and compare the claim.
- [ ] E. The application cannot constrain the final output; only a human can check it.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: It depends on stakes and task semantics.
- B: It must be checked like any claim.
- C: Evidence does not automatically flow into narration.
- D: Parsing and comparing the claim is another option the chapter names.
- E: The application can constrain the final output so correspondence is checkable.

**Source:** Worked example: 42 in the trace, 99 in the claim

## MA-ch11.31

Check each statement that is true about the case where the 99 had been 42. Each statement is worth 1 point (5 points total).

- [ ] A. The final sentence would be correct.
- [ ] B. A reader's sentence is about an operation.
- [ ] C. A tool result reports on an outcome.
- [ ] D. A correct final number removes the gap between operation and outcome.
- [ ] E. A reader could still leave believing something the trace has not shown.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The number would match.
- B: A reader's sentence is about an outcome.
- C: A tool result reports on an operation.
- D: The scope gap remains however correct the number.
- E: The reason is scope.

**Source:** When the report is accurate and the reader is still misled

## MA-ch11.32

Check each statement that is true about the screening-tool case from the companion book on computational skepticism. Each statement is worth 1 point (5 points total).

- [ ] A. The screening tool names the two features that drove its prediction.
- [ ] B. The missing question is the audience question: who is reading this, and what do these words mean to them?
- [ ] C. The chapter labels it a composite, not a sourced incident.
- [ ] D. The explanation was inaccurate about the model.
- [ ] E. The explanation told the radiologist that the model had learned a shortcut.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Two features are named.
- B: That is the book's name for the missing question.
- C: It is a composite.
- D: The explanation was accurate about the model.
- E: It did not say the model had learned a shortcut.

**Source:** When the report is accurate and the reader is still misled

## MA-ch11.33

Check each statement that is true about the verbs that tool reports use. Each statement is worth 1 point (5 points total).

- [ ] A. A successful write call establishes all of that.
- [ ] B. "Deployed" always means serving traffic.
- [ ] C. "Sent" may mean handed to a mail server or received by a person.
- [ ] D. A report that says "saved" tells the reader the file exists where they expect, with the content they meant, and will exist tomorrow.
- [ ] E. "Deleted" may mean removed from this folder, from the repository history, or from every copy.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A successful write establishes far less.
- B: It may mean uploaded or serving traffic.
- C: Two different events.
- D: That is the reader's inference.
- E: Several scopes are possible.

**Source:** When the report is accurate and the reader is still misled

## MA-ch11.34

Check each statement that is true about what a successful file write establishes. Each statement is worth 1 point (5 points total).

- [ ] A. It establishes that no other process changed the file afterward.
- [ ] B. It establishes that bytes were written to a particular resolved path at a particular time.
- [ ] C. It establishes that the file satisfies the user's assignment.
- [ ] D. It establishes that the repository contains the change.
- [ ] E. Reading the resolved target back is unnecessary once the write returns success.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A later change is not excluded.
- B: That is what it establishes.
- C: Meeting the assignment is separate.
- D: Repository state needs its own check such as git diff.
- E: Read-back is one of the checks the chapter lists; the success return is only one item in the chain.

**Source:** Verification surfaces for real tools

## MA-ch11.35

Check each statement that is true about evidence from other kinds of tools. Each statement is worth 1 point (5 points total).

- [ ] A. If a tool returned success, no further checks are needed.
- [ ] B. Tool evidence is always evidence of something specific.
- [ ] C. An upload report that says success guarantees passing health checks.
- [ ] D. A row count describes the snapshot the query actually saw.
- [ ] E. A retrieved passage that is the most similar one necessarily entails the answer.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: "The tool returned success" is one item in a chain.
- B: The chapter's summary point.
- C: An upload report can coexist with failing health checks.
- D: It reports a snapshot.
- E: Most similar is not the same as entailing the answer.

**Source:** Verification surfaces for real tools

## MA-ch11.36

Check each statement that is true about the design move of making verification surfaces explicit at tool boundaries. Each statement is worth 1 point (5 points total).

- [ ] A. Keep errors structured.
- [ ] B. Save every argument in full, including credentials, so a reviewer can reproduce everything.
- [ ] C. Preserve query parameters, timestamps, and stable identifiers.
- [ ] D. Return resolved paths rather than only friendly names.
- [ ] E. The guiding question is what minimum evidence lets an authorized reviewer test the claim.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Structured errors are usable evidence.
- B: Tool arguments can contain personal information or secrets and must not be leaked.
- C: They let a reviewer reproduce a decision.
- D: Resolved paths are checkable.
- E: The question is minimum evidence, not "save everything".

**Source:** Verification surfaces for real tools

## MA-ch11.37

Check each statement that is true about the misconception "If the schema is correct, invalid calls cannot happen." Each statement is worth 1 point (5 points total).

- [ ] A. The schema guides model output.
- [ ] B. The local runtime still has to defend its boundary.
- [ ] C. The Boolean fixture shows a Python-specific edge that a vague numerical assumption can miss.
- [ ] D. A platform is required to check the schema before the call reaches your code.
- [ ] E. A correct schema makes the local type checks redundant.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Guiding output is its role.
- B: The runtime is the last defense.
- C: True counts as a number to a casual guard.
- D: A platform may check the schema, but the chapter does not require it.
- E: The checks remain necessary.

**Source:** Common misconceptions, broken with counterexamples

## MA-ch11.38

Check each statement that is true about the misconceptions "A tool result proves the answer" and "Deterministic Python is infallible." Each statement is worth 1 point (5 points total).

- [ ] A. Python repeats its implementation consistently.
- [ ] B. Consistent behavior shows that the implementation is correct.
- [ ] C. An implementation can still encode the wrong formula, parse the wrong field, or use stale input.
- [ ] D. A tool result proves the answer whenever the dispatcher validated its arguments.
- [ ] E. If the operands were chosen from the wrong records, correct addition produces the wrong business answer.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Consistency is the strength.
- B: Consistent is not correct.
- C: Consistency also repeats errors.
- D: A tool result proves only what the operation and its evidence support.
- E: Right sum, wrong records.

**Source:** Common misconceptions, broken with counterexamples

## MA-ch11.39

Check each statement that is true about the order of work the chapter recommends. Each statement is worth 1 point (5 points total).

- [ ] A. Conducting Claude Code against the gate comes before writing the gate.
- [ ] B. Deciding which checks fail differently comes before writing the gate.
- [ ] C. Shipping the matrix with a sign-off comes before building your own baseline.
- [ ] D. Building your own baseline comes before conducting Claude Code against the gate.
- [ ] E. Dividing the work honestly is the last step.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The gate comes first.
- B: First step.
- C: Shipping follows conducting Claude Code.
- D: Baseline precedes Claude Code.
- E: The honest division is last.

**Source:** Building a reusable tool evidence matrix

## MA-ch11.40

Check each statement that is true about how to start building a tool evidence matrix. Each statement is worth 1 point (5 points total).

- [ ] A. For each claim, name only the producing operation.
- [ ] B. Start with the final sentence you want to be able to say.
- [ ] C. Treat that sentence as one claim, so it can be checked in one step.
- [ ] D. A workflow in which no check could reject the claim is still verified, as long as the final sentence is fluent.
- [ ] E. If you cannot name a check that could reject the claim, the workflow is relying on assurance.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Also name the evidence artifact, its scope, an independent check, and a failure response.
- B: Start from the sentence.
- C: Break it into atomic claims.
- D: Fluency is not a check; such a workflow relies on assurance.
- E: Without a rejecting check there is only assurance.

**Source:** Building a reusable tool evidence matrix

## MA-ch11.41

Check each statement that is true about the rule from Conducting AI on using one tool to audit another. Each statement is worth 1 point (5 points total).

- [ ] A. If two checks make the same mistake on the same input, combining them leaves the mistake where it was.
- [ ] B. The book rates that overlapping-text point as high confidence.
- [ ] C. Using one tool to audit another reduces error only to the degree the two fail differently.
- [ ] D. The stronger advice, to audit a generative claim with a non-generative tool, depends on the overlapping-text point.
- [ ] E. Two chat models asked the same question cannot fail the same way, since each was trained separately.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Shared mistakes survive combination.
- B: The book marks it medium confidence, to be held loosely.
- C: The rule.
- D: The stronger advice does not depend on it.
- E: They can fail the same way because they learned from overlapping text.

**Source:** Choose checks by failure mode

## MA-ch11.42

Check each statement that is true about auditing a generative claim with a non-generative tool. Each statement is worth 1 point (5 points total).

- [ ] A. An AI checking an AI is a second opinion.
- [ ] B. A schema validator catches malformed structure however plausible the content reads.
- [ ] C. A model's verdict on quality counts as a verification.
- [ ] D. Deterministic code does not confabulate.
- [ ] E. Deterministic code is wrong the same way on every run, so a test can find it.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It is the first opinion run twice.
- B: Structure is checked regardless of fluency.
- C: A verdict is not a verification.
- D: It can be wrong but does not invent.
- E: Consistency makes errors findable.

**Source:** Choose checks by failure mode

## MA-ch11.43

Check each statement that is true about what particular checks catch and miss in the addition example. Each statement is worth 1 point (5 points total).

- [ ] A. A hand calculation of 17 + 25 avoids the dispatcher and serialization path.
- [ ] B. A hand calculation establishes that 17 and 25 were the intended operands.
- [ ] C. Inspecting the task against the request checks operand selection.
- [ ] D. Comparing the final claim to the returned result catches narration drift, but a shared wrong result can make both agree.
- [ ] E. Inspecting the task against the request recomputes the result.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: It enters by a different route.
- B: It does not touch the operands' origin.
- C: It crosses the task-to-request boundary.
- D: Both can be wrong together.
- E: It does not recompute anything.

**Source:** Choose checks by failure mode

## MA-ch11.44

Check each statement that is true about the six-step design procedure for checks. Each statement is worth 1 point (5 points total).

- [ ] A. Name one plausible failure at every transition.
- [ ] B. Decide what disagreement will stop, retry, or escalate only after a disagreement occurs.
- [ ] C. Select checks that enter the chain from different evidence sources.
- [ ] D. Record the shared assumptions that remain after the checks agree.
- [ ] E. Write the consequential claim in a form that can be false.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Step three.
- B: Step six says to decide in advance.
- C: Step four.
- D: Step five.
- E: Step one.

**Source:** Choose checks by failure mode

## MA-ch11.45

Check each statement that is true about verification theater. Each statement is worth 1 point (5 points total).

- [ ] A. The stop policy is decided in advance.
- [ ] B. If a checker disagrees and the controller asks the model which number sounds better, the workflow has not used the check.
- [ ] C. The model choosing between two disagreeing numbers counts as a stop policy.
- [ ] D. A stop policy makes disagreement operational.
- [ ] E. That converts a prompt into evidence.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The last step of the procedure is deciding in advance.
- B: The check was not used.
- C: That is the failure described, not a stop policy.
- D: A stop policy gives disagreement an effect.
- E: That converts evidence into another prompt.

**Source:** Choose checks by failure mode

## MA-ch11.46

A receipt tool returns a subtotal, and Python recomputes the sum of the extracted rows. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Agreement shows that no row is missing.
- [ ] B. Both routes share the extracted rows, so a missing row fools them together.
- [ ] C. Agreement between the subtotal and the recomputed sum establishes internal consistency.
- [ ] D. Checking a sample against the source image fails differently from the recomputation.
- [ ] E. Human review may still be needed where handwriting or business rules make interpretation ambiguous.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A missing row fools both routes.
- B: A shared input is shared exposure.
- C: The sum matches the rows.
- D: The image is a different source.
- E: Ambiguity can need a person.

**Source:** Choose checks by failure mode

## MA-ch11.47

Check each statement that is true about how the gate for this chapter is written. Each statement is worth 1 point (5 points total).

- [ ] A. It names who decided each item.
- [ ] B. The lesson fixed the design: one tool `add`, scripted fixtures, operands 17 and 25, a scripted final claim of 99, and a request budget of at most four.
- [ ] C. It is written in your learner workspace before you ask Claude Code for anything.
- [ ] D. A live Claude session is part of the fixed design.
- [ ] E. It is written in plain sentences and one table.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Each item records who decided it.
- B: Those are the lesson's choices.
- C: The gate comes before the first request to Claude Code.
- D: The design uses scripted fixtures, not a live session.
- E: Sentences plus one table.

**Source:** The gate: design the matrix before the run

## MA-ch11.48

Check each statement that is true about the contract in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. Identifiers are nonempty strings, unique within the batch.
- [ ] B. `results` returns one `tool_result` per `tool_use` block, carrying that block's identifier.
- [ ] C. The contract says that when `loop` returns `finished` the final sentence is true.
- [ ] D. `loop` raises on a `tool_use` stop with no calls.
- [ ] E. `loop` returns `finished` on both `end_turn` and `max_tokens`.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Uniqueness is scoped to the batch.
- B: One result per request, same identifier.
- C: None of the contract says the final sentence is true; that needs its own row.
- D: A tool_use stop with no calls is an error.
- E: `finished` is returned only on `end_turn`.

**Source:** The gate: design the matrix before the run

## MA-ch11.49

Check each statement that is true about the rows of the gate's matrix. Each statement is worth 1 point (5 points total).

- [ ] A. For narration to claim, a disagreement means you mark the claim verified anyway and note the difference.
- [ ] B. For loop to status, a disagreement means you report a verdict that the answer failed.
- [ ] C. For request to dispatch, the check is boundary tests you wrote before reading the reference.
- [ ] D. For dispatch to result, a disagreement means you treat the result as untrusted.
- [ ] E. For task to request, the plausible failure is wrong operands, and the check is you reading the request against the task text.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The response is to withhold verified and escalate to you.
- B: The response is to report the exit, not a verdict.
- C: Tests written before the reference was read.
- D: The result is untrusted on disagreement.
- E: That row's failure and check.

**Source:** The gate: design the matrix before the run

## MA-ch11.50

Check each statement that is true about the wrong versions of the program that your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. Renaming the `finished` exit to `verified` is caught by the six reference tests.
- [ ] B. Deleting the duplicate-identifier guard is caught by the six reference tests.
- [ ] C. The reference suite catches that change.
- [ ] D. Deleting the overflow check is caught by the six reference tests.
- [ ] E. Replacing the exact-type test with `isinstance(v, (int, float))` makes `True + 2` return 3.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: No reference test reaches the end_turn exit.
- B: No reference test sends a duplicate.
- C: The reference suite catches that one.
- D: No reference test adds two huge floats.
- E: A bool passes the isinstance test.

**Source:** The gate: design the matrix before the run

## MA-ch11.51

Check each statement that is true about the failure sentence and about what the evidence may claim. Each statement is worth 1 point (5 points total).

- [ ] A. The evidence may claim equality between a parsed number and an independently derived one.
- [ ] B. You write one dated sentence about what you would see if the matrix were wrong.
- [ ] C. The evidence may claim that 17 and 25 were the operands anyone meant.
- [ ] D. The sentence is just as useful when it is written after reading the output.
- [ ] E. The sentence describes a trace in which the status is `verified` and every identifier matches.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Along with protocol-level statements about this implementation.
- B: A dated failure sentence.
- C: That is what the evidence cannot say.
- D: Written after the output, it only describes the output.
- E: The status in the sentence is `finished`, with no row able to say no to the final sentence.

**Source:** The gate: design the matrix before the run

## MA-ch11.52

Check each statement that is true about Claude's role in relation to the gate. Each statement is worth 1 point (5 points total).

- [ ] A. The gate is where your decision about what counts as independent goes on the record.
- [ ] B. Naming checks and failure responses in advance is part of designing the matrix before the run.
- [ ] C. Claude can write the gate for you without defeating its purpose.
- [ ] D. The gate should be finished after Claude's draft so that it matches the code.
- [ ] E. Claude can sharpen the gate by finding a transition you left without a check.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: That is what the gate records.
- B: Failure responses are decided before the run.
- C: A gate Claude writes defeats its purpose.
- D: A gate edited to match the code is the failure the sign-off exists to prevent.
- E: A legitimate use of Claude.

**Source:** The gate: design the matrix before the run

## MA-ch11.53

Check each statement that is true about building your own baseline. Each statement is worth 1 point (5 points total).

- [ ] A. The baseline includes a one-tool allowlist and exact argument keys and numeric types.
- [ ] B. You change several inputs at once so that interactions show up.
- [ ] C. You write your own `dispatch`, `results`, and `loop` under `learning-artifacts/week-11/`.
- [ ] D. The assistant content is kept unchanged and user-role `tool_result` blocks are appended.
- [ ] E. You trace one successful case by hand, marking the input boundary, the transformation, and the returned result.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Part of the specification.
- B: Change one input at a time so a difference has an identifiable cause.
- C: The stated location.
- D: The message-construction rule.
- E: The by-hand trace.

**Source:** Build It: the baseline that lets you audit

## MA-ch11.54

Check each statement that is true about the reference demo and its six tests. Each statement is worth 1 point (5 points total).

- [ ] A. The demo's scripted responses are evidence that Claude generated and verified something.
- [ ] B. One reference test covers the happy path.
- [ ] C. The chapter advises reading the six tests as six questions, not as "the code works".
- [ ] D. One reference test adds two huge floats to trigger overflow.
- [ ] E. One reference test sends a duplicate identifier.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: They are fixtures, not evidence of Claude's work.
- B: The happy path is among the six.
- C: That is the stated reading.
- D: None adds two huge floats.
- E: None sends a duplicate.

**Source:** Build It: the baseline that lets you audit

## MA-ch11.55

Check each statement that is true about handing the work to Claude Code. Each statement is worth 1 point (5 points total).

- [ ] A. You give Claude Code the gate you wrote, with the contract, the tests, and the matrix.
- [ ] B. You give Claude Code your own implementation as well.
- [ ] C. A failing test is often a gap in your gate, which Claude cannot see because it only has what you wrote.
- [ ] D. You run your tests on what it returns, yourself.
- [ ] E. You compare its implementation with your baseline and name one difference in behavior.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The gate is the specification.
- B: It gets the gate, not your implementation.
- C: Gaps in the gate are invisible to Claude.
- D: You run the tests.
- E: The comparison with the baseline is the second step.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch11.56

Check each statement that is true about the differences you find between Claude's implementation and your baseline, and the follow-up steps. Each statement is worth 1 point (5 points total).

- [ ] A. A boundary Claude silently ignored is a revision to your gate.
- [ ] B. A boundary Claude handled that you missed is a revision to your gate.
- [ ] C. If a deliberately wrong version passes your tests, that shows the test list is strong.
- [ ] D. You can ask Claude for a deliberately wrong version that still passes your tests.
- [ ] E. The reason each check is independent of the route it checks is a column Claude writes.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A boundary it silently ignored is a defect your tests failed to catch, not a gate revision.
- B: The gate needs revising.
- C: It shows the test list was too weak.
- D: A cheap way to probe the tests.
- E: You write that column.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch11.57

Check each statement that is true about preserving the record of the session and the optional live mode. Each statement is worth 1 point (5 points total).

- [ ] A. Nothing in the chapter requires running `--live`.
- [ ] B. If you run live, merge the live trace into the offline fixture so there is a single record.
- [ ] C. The optional `--live` mode can make up to four billable requests.
- [ ] D. Preserve your prompt, the plan, the diff, the commands, and the outputs, with the date and displayed model label.
- [ ] E. If a session failed or did not run, record that rather than substituting a fixture.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Live mode is optional.
- B: The live trace is kept apart from the offline fixture.
- C: The cost limit.
- D: The preservation list.
- E: Do not substitute a fixture for a failed session.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch11.58

Check each statement that is true about what to ship. Each statement is worth 1 point (5 points total).

- [ ] A. The reference tests prove security under hostile inputs.
- [ ] B. Ship the tool schema, the validation rules, a valid and a rejected request/result trace, and the matrix, with exact commands and observed outputs.
- [ ] C. Identify which behaviors came from fixtures and which, if any, came from an explicitly authorized live run.
- [ ] D. The matrix should also record what remains untested.
- [ ] E. The reference tests prove global identifier uniqueness.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Hostile inputs are untested.
- B: The shipping list.
- C: Provenance of behaviors.
- D: Untested items belong in the matrix.
- E: Global uniqueness is untested.

**Source:** Ship It: the matrix, the trace, and the sign-off

## MA-ch11.59

Check each statement that is true about negative evidence and extra tests. Each statement is worth 1 point (5 points total).

- [ ] A. Preserve one failed case and the decision it changed.
- [ ] B. A file-writing capstone might test traversal rejection and read-back.
- [ ] C. A system demonstrated only on its happy path has demonstrated control.
- [ ] D. Add as many tests as possible so the test count is high.
- [ ] E. A rejected Boolean, a duplicate identifier, or a mismatched final claim shows that the boundary can say no.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Keep the negative evidence.
- B: Those are the chapter's examples.
- C: That demonstrates production, not control.
- D: Add tests because a capstone claim needs them, not to inflate a count.
- E: Negative cases show the boundary can refuse.

**Source:** Ship It: the matrix, the trace, and the sign-off

## MA-ch11.60

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. The template has the lines Checked, How, Not checked, Not claiming, and Signed or withheld.
- [ ] B. You should write the sign-off by asking Claude to summarize its own account of what it did.
- [ ] C. Claude's draft will include the "Not checked" line because it saw your whole record.
- [ ] D. The "Not checked" line is the one a drafted sign-off is most likely to include.
- [ ] E. If your evidence does not support signing, signing anyway is the honest result.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Those are the template's lines.
- B: Write it from your record.
- C: The draft has no record of what you did not run.
- D: The draft has no record of what you did not run, so it is the line it is least likely to include.
- E: Withholding is the honest result.

**Source:** Ship It: the matrix, the trace, and the sign-off

## MA-ch11.61

Check each statement that is true about the words a sign-off may use. Each statement is worth 1 point (5 points total).

- [ ] A. Verified may be used whenever the controller status is finished.
- [ ] B. Verified is for a claim whose check came from outside the route that produced it.
- [ ] C. This chapter's sign-off covers a record of what ran.
- [ ] D. Chapter 10's sign-off covered a record of what ran.
- [ ] E. It may say what was recorded, computed, and tested.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Finished is a controller state.
- B: That is the standard for verified.
- C: This one covers what ran.
- D: Chapter 10's sign-off covered a plan, which is a prediction.
- E: Those are the permitted verbs.

**Source:** Ship It: the matrix, the trace, and the sign-off

## MA-ch11.62

Check each statement that is true about the sample sign-off template's "Not checked" and "Not claiming" lines. Each statement is worth 1 point (5 points total).

- [ ] A. Not checked includes any tool but `add`.
- [ ] B. Not claiming includes that any final sentence is true because the status read `finished`.
- [ ] C. Not checked includes global identifier uniqueness.
- [ ] D. Not checked includes whether 17 and 25 were the intended operands.
- [ ] E. The sample Not checked line lists the arithmetic 17 + 25 = 42.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Other tools are listed.
- B: Not claiming says this.
- C: Global uniqueness is listed.
- D: Operand intent is listed.
- E: The line lists operands, identifier uniqueness, hostile inputs, live services, and other tools; the sum was computed and compared.

**Source:** Ship It: the matrix, the trace, and the sign-off

## MA-ch11.63

Check each statement that is true about the driver's seat table. Each statement is worth 1 point (5 points total).

- [ ] A. Claude chooses the verb in the report, and you sign.
- [ ] B. Claude builds the baseline first, and you then run your tests on your own version.
- [ ] C. You write the contract and matrix only after Claude has written its own.
- [ ] D. Claude decides which operations exist and what the dispatcher refuses.
- [ ] E. Claude should propose the name and arguments as structured data.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: You choose the verb; Claude drafts and flags overclaim.
- B: You build your own baseline first.
- C: You write the contract and matrix first.
- D: You decide which operations exist; the allowlist is policy.
- E: Claude proposes calls as data.

**Source:** The driver's seat

## MA-ch11.64

Check each statement that is true about the fourth row of the driver's seat table, running and logging the checks. Each statement is worth 1 point (5 points total).

- [ ] A. If you cannot point to the log line and the sentence, the split happened in your head and not in the record.
- [ ] B. A transcript of both routes displays whether they share an input, a source, or an assumption.
- [ ] C. The artifact should record one check Claude ran and logged and one independence judgment, written in Claude's words.
- [ ] D. Claude can compute both routes.
- [ ] E. Whether two routes share an assumption is a fact about Claude's training data.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The record must show the split.
- B: A transcript does not display shared inputs.
- C: The independence judgment is in your own words.
- D: Claude computes and logs both routes.
- E: It is a fact about your data and your task.

**Source:** The driver's seat

## MA-ch11.65

Check each statement that is true about revising the gate. Each statement is worth 1 point (5 points total).

- [ ] A. Once the gate is written, it may never be changed.
- [ ] B. Design-first does not mean frozen.
- [ ] C. A gate quietly edited to match what the code does is the failure the sign-off exists to prevent.
- [ ] D. A revised gate with a dated reason shows that the original gate was worthless.
- [ ] E. If a check disagrees or Claude finds a case your contract missed, reopen the gate and record that you did.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Revision is allowed when recorded.
- B: The gate can change.
- C: Quiet edits defeat the sign-off.
- D: A revised gate with a dated reason is evidence of control.
- E: Reopen and record.

**Source:** Integration with the agent built so far

## MA-ch11.66

Check each statement that is true about the verification and reflection tasks. Each statement is worth 1 point (5 points total).

- [ ] A. The reflection asks which distinction you originally collapsed, such as identity and truth or repetition and independence.
- [ ] B. The reflection asks you to resolve to be more careful with AI in general.
- [ ] C. Explain one passing case from input block to returned content without reading Claude's explanation.
- [ ] D. If the strongest sentence in your report says verified, point to the check that came from outside the route.
- [ ] E. Name which matrix row each check addresses.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The reflection is local.
- B: The chapter prefers a concrete habit to a generic resolution.
- C: Explain a pass without leaning on Claude.
- D: Verified needs an outside check.
- E: Tie checks to rows.

**Source:** Verify and reflect

## MA-ch11.67

Check each statement that is true about the assessments at the end of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Do not submit solutions inline with the prompts.
- [ ] B. Answer the Lesson 11 knowledge check before reading its feedback.
- [ ] C. The knowledge check is a separate graded exercise.
- [ ] D. Preserve predictions, commands, outputs, and revisions.
- [ ] E. The assessments are ungraded practice.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: No inline solutions.
- B: Answer before the feedback.
- C: It is for self-review, not a separate graded exercise.
- D: What to preserve.
- E: Ungraded.

**Source:** Assessments - ungraded practice

## MA-ch11.68

Check each statement that is true about the Anthropics section. Each statement is worth 1 point (5 points total).

- [ ] A. Direct API credits are required for the learning path.
- [ ] B. Upstream notebooks are an explicit optional extension.
- [ ] C. The guidance is fixed, so it does not need to be checked again when implementing against the live API.
- [ ] D. Anthropic's Handle tool calls guidance describes client-tool request/result association and message construction.
- [ ] E. Anthropic's public tool-use course notebooks are required for the learning path.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The offline mechanism and a Claude Code account suffice.
- B: Run them only as an optional extension.
- C: It is rolling documentation to be checked again.
- D: Its subject.
- E: Notebooks are optional.

**Source:** Anthropics

## MA-ch11.69

Check each statement that is true about the Computational Skepticism closing section. Each statement is worth 1 point (5 points total).

- [ ] A. The book's agent studies supply rates you can rely on.
- [ ] B. Of any check that held, ask under what condition it would have failed.
- [ ] C. The false-success catch says to observe the world's state independently of the agent's report.
- [ ] D. If you cannot name that condition, you have still validated the check.
- [ ] E. For every row where the independent check agreed, write the condition under which it would have agreed anyway.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The studies are exploratory; take the question, not rates.
- B: The diagnostic question.
- C: Observe state independently.
- D: Then you have only observed that nothing went wrong this time.
- E: Same operands, same rows, same source.

**Source:** Computational Skepticism

## MA-ch11.70

Check each statement that is true about laundering and the 42 in the Conducting AI closing section. Each statement is worth 1 point (5 points total).

- [ ] A. At each seam you write what is passed, what it is trusted to be, and how that trust was earned.
- [ ] B. A typed field or a serialized string shows that a value has been checked.
- [ ] C. Laundering is an unverified value gaining authority as it passes through clean steps.
- [ ] D. You trace the 42 through the dispatcher's return, `json.dumps`, the `tool_result` content, the assistant's sentence, and the matrix row.
- [ ] E. Polish is provenance.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The three notes at each seam.
- B: Such things only make a value look checked.
- C: The book's definition.
- D: The five seams.
- E: Polish is not provenance.

**Source:** Conducting AI

## MA-ch11.71

Check each statement that is true about where the gate belongs. Each statement is worth 1 point (5 points total).

- [ ] A. A check at the last seam cannot catch a wrong operand chosen at the first.
- [ ] B. The conductor's work is to make the model's performance fluent.
- [ ] C. The gate belongs where the claim first enters, which in this chapter is the request.
- [ ] D. The gate belongs at the report, the last seam.
- [ ] E. Fluency alone can show that a performance was correct.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A last-seam check is too late for first-seam errors.
- B: The conductor's work is choosing the routing and defining what evidence must cross each seam.
- C: The request is where the claim first enters.
- D: The chapter places it at the request.
- E: The model makes the performance fluent; fluency alone cannot show correctness.

**Source:** Conducting AI

## MA-ch11.72

Check each statement that is true about the forward bridge. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 12 is about the dispatcher.
- [ ] B. The sign-off's date and versions are there so that it can be carried forward.
- [ ] C. A verified result stays verified in every future context.
- [ ] D. Tomorrow, a memory system may retrieve "42" after the operands, source, code, or task have changed.
- [ ] E. Today, 42 is supported by a recorded operation and an independent calculation.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Chapter 12 asks what has to travel with memory.
- B: Date and versions travel with it.
- C: A verified result is not permanently verified.
- D: Recall can outlive its evidence.
- E: The two supports.

**Source:** Forward bridge
