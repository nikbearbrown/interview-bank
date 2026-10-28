# Chapter 11: Tool use and verification

## ES-ch11.1

The chapter opens with a trace in which the tool returned 42 and the assistant then said 99, and the controller reported `finished`. Explain what this fixture is and what it shows about protocol completion versus factual verification.

**Points:** 5

**Rubric (1 point each):**

1. States that the tool returned 42 while the assistant's final sentence said 99.
2. States that the controller correctly accepted the request to add 17 and 25 and reported its own status as `finished`.
3. States that the controller did not compare the assistant's final sentence with the tool result.
4. Concludes that protocol completion and factual verification are different mechanisms.
5. Identifies the trace as a deliberately constructed offline fixture used in the chapter's research run, not a hypothetical defect and not a live transcript.

**Source:** Chapter opening (the 42 versus 99 fixture)

## ES-ch11.2

The chapter says "A correct recipe is not a check." Using the opening trace, explain what that sentence means and name the pieces that were built correctly.

**Points:** 5

**Rubric (1 point each):**

1. Names that the request was well formed and that the dispatcher validated it.
2. Names that the result carried the matching identifier and that the loop ended in a recognized state.
3. Explains that building every one of those pieces correctly can still ship a trace that ends in a false sentence.
4. Explains that a check must compare a later claim against something other than the claim itself (the chain of custody ends in an independent check).
5. Explains that the example is intentionally small because arithmetic lets us know the answer independently, while in a file edit, a database query, or a deployment the independent check is harder and more consequential.

**Source:** Chapter opening (the 42 versus 99 fixture)

## ES-ch11.3

A colleague says: "Claude can read the trace for me and explain why 42 and 99 differ, so I do not need to look at anything else." Respond using the chapter's argument.

**Points:** 5

**Rubric (1 point each):**

1. Grants that Claude can write a fluent account of why 42 and 99 differ, and that the account may be right.
2. States that one transcript does not show what 17 and 25 were supposed to be.
3. States that one transcript does not show where each of your checks got its inputs.
4. States that one transcript does not show whose name goes on the report.
5. Ties these gaps to the three jobs Chapter 1 named, conduct, check, and drive.

**Source:** Chapter opening (the 42 versus 99 fixture)

## ES-ch11.4

Before reading the trace, the chapter asks four prediction questions. Answer each one using the mechanism the chapter later shows, and say what the chapter says the predictions are for.

**Points:** 5

**Rubric (1 point each):**

1. Says that True is not accepted as the number 1: the exact-type check rejects it even though `bool` is a subclass of `int`.
2. Says that an unknown tool becomes a returned tool error, because `dispatch` raises ValueError and `results` converts it to a `tool_result` with `is_error: True`.
3. Says that two calls sharing one identifier in a batch are not both run: the duplicate-identifier guard raises.
4. Says that the loop calls that outcome `finished`: the assistant stopped with `end_turn` after saying 99.
5. Says the value of writing down and dating predictions is exposing the model of the machinery you brought, not guessing correctly.

**Source:** What you will be able to do

## ES-ch11.5

Describe the three jobs, conduct, check, and drive, at the scale of one tool call. For each job, say what you do and what the chapter says it cannot be handed to.

**Points:** 5

**Rubric (1 point each):**

1. Conduct before the call: you decide which operations must be exact and therefore live in your program, not in the model's continuation.
2. Conduct after the call: you decide what the loop may call done, and the gate is the tool evidence matrix design written before the run.
3. Check: a matching identifier establishes who asked, a `finished` status establishes that the controller saw a stop signal, and a fluent sentence establishes nothing.
4. Check: only a check that fails differently from the thing it checks can say no to it.
5. Drive: Claude can run and log the checks faster than you can type the command, but which verification surface counts as independent is your call, and the log cannot make it for you.

**Source:** Three jobs at the scale of one tool call

## ES-ch11.6

You need the sum of 17 and 25 in a report. Compare letting Claude write the number in its reply with having Claude propose a call that your program executes. Which does the chapter favor and why?

**Points:** 5

**Rubric (1 point each):**

1. Says that when Claude writes `17 + 25 = 42`, the sentence is a continuation ranked and sampled like any other.
2. Says it is very often right, but the design question is whether anything in the path would tell you the one time it is not.
3. Says that nothing outside the continuation recomputes the sum in the first design.
4. Says that a dispatcher's 42 comes from an operation you can read, re-run, and break with a test.
5. Connects the choice to verifiability-first engineering: choose the lowest capability that does the step, because the most constrained tool is the one you can check.

**Source:** Conduct: what must be exact does not belong in the model

## ES-ch11.7

You are asked to total every line item over $10,000 across 200 invoices. Compare asking a chat window for the total with extracting fields per invoice and handing the filter and the sum to deterministic code, and state what the second design still does not guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Says the chat window gives a fluent number with nothing behind it to audit.
2. Describes the second design: extract fields per invoice, then deterministic code does the filter and the sum.
3. Says the second design leaves seams where you can compare records with invoices and recompute the sum.
4. Says that arithmetic, exact lookups, deterministic transforms, and schema validation belong outside the probabilistic layers.
5. Says routing out makes the step inspectable, not infallible: deterministic code can encode the wrong formula, parse the wrong field, or read stale input, and will do so consistently.

**Source:** Conduct: what must be exact does not belong in the model

## ES-ch11.8

The chapter says every operation you route to the dispatcher is "authority you have granted," and describes the book's five-layer capability stack as a teaching device. Explain both points and the division of labor the chapter chooses.

**Points:** 5

**Rubric (1 point each):**

1. Says that every operation granted to the dispatcher is authority granted.
2. Says a one-tool allowlist is easy to audit because it can do almost nothing.
3. Says the five-layer capability stack and its "easier to verify" value are teaching devices.
4. Says they are not an industry standard and not a ranking of how reliable each layer is.
5. States the division: Claude proposes the call and interprets the trace, and Python owns exact argument validation and arithmetic.

**Source:** Conduct: what must be exact does not belong in the model

## ES-ch11.9

The chapter says a tool schema is "an invitation rather than an execution engine." Explain what the `add` schema does and does not do, and describe what Claude actually produces and what the application does with it.

**Points:** 5

**Rubric (1 point each):**

1. Says the schema tells Claude which request shape the application is prepared to consider.
2. Says it does not import an `add` function into the model.
3. Says it does not prove that the application enforces the schema and does not authorize the model to run arbitrary Python.
4. Says Claude produces a structured block that can be read as a proposal: call the tool named `add` with these arguments.
5. Says the application decides what the name means, checks the arguments, executes its own implementation, and constructs the result message.

**Source:** A tool description does not run a tool

## ES-ch11.10

A model proposes the following calls to the course `dispatch` function. For each, say whether it is accepted or refused and why: (a) the name `subtract` with a=5 and b=3; (b) `add` with keys a, b, and c; (c) `add` with a=True and b=2; (d) `add` with a=infinity and b=1; (e) `add` with two huge finite floats whose sum overflows.

**Points:** 5

**Rubric (1 point each):**

1. (a) is refused because the name must be exactly `add` (an unknown tool).
2. (b) is refused because the arguments must have exactly the keys a and b.
3. (c) is refused because each value must have the exact type `int` or `float` and `bool` does not qualify.
4. (d) is refused because each argument must be finite.
5. (e) is refused because the result must also be finite, so the overflow is caught by the separate check on the sum.

**Source:** A tool description does not run a tool

## ES-ch11.11

Explain why the dispatcher uses `type(v) not in (int, float)` instead of an `isinstance` test, and what the choice shows about who owns validation rules.

**Points:** 5

**Rubric (1 point each):**

1. States that in Python `bool` is a subclass of `int`, so `isinstance(True, int)` is true.
2. States that a casual numerical guard would admit `True + 2` and produce 3.
3. States that the exact-type test rejects the Boolean, and that the research fixture observed the rejection.
4. States that a JSON-facing description saying "number" is not enough, because Python still needs rules for the values it actually receives.
5. States that the refusals are decisions about what the operation means and are yours: a specification that never mentions `True` gives an implementer, human or Claude, no reason to refuse it.

**Source:** A tool description does not run a tool

## ES-ch11.12

Why does the dispatcher require finite numbers, and why is the sum checked separately from the inputs?

**Points:** 5

**Rubric (1 point each):**

1. Says that infinity and not-a-number are floats in Python.
2. Says they are poor inputs for an addition tool whose output will be serialized as JSON and read as an ordinary answer.
3. Says that finite inputs can overflow when added.
4. Says that is why the result is checked separately for finiteness (and a failure raises ValueError "Result overflow").
5. Concludes that validation is not decoration before the real work: it defines what the operation means.

**Source:** A tool description does not run a tool

## ES-ch11.13

Why does the chapter insist that the application, not the model, decides how a proposed tool name is executed? Include the role of the allowlist, the argument rules, and what the same idea means for a file tool and a database tool.

**Points:** 5

**Rubric (1 point each):**

1. Says that letting the model decide collapses description, authority, and implementation into one unreviewable gesture.
2. Says an allowlist gives the application a closed set of operations, and exact argument rules narrow each operation further.
3. Says Chapter 5's point applies: who may do what is a human decision, and the allowlist is where it is written down.
4. Says a file tool's dispatcher would resolve paths, compare the destination with an approved root, and distinguish reads from writes.
5. Says a database tool's dispatcher would restrict the statement type, credentials, and row count, and that tool schemas help form proposals but do not substitute for these enforcement checks.

**Source:** Dispatch belongs to the application

## ES-ch11.14

The result builder catches `ValueError` from `dispatch` and returns a `tool_result` with `is_error: True`. Explain what the result contains, why this conversion is a good design, and why the builder catches nothing broader.

**Points:** 5

**Rubric (1 point each):**

1. Says the error result carries the request's identifier and the exception text as its content.
2. Says a rejected proposal is useful evidence for the next turn: the model can see that a particular request failed and why.
3. Says the application does not pretend the tool ran and does not crash the whole conversation, so the error becomes part of the protocol trace.
4. Says `ValueError` is a bounded, anticipated validation failure.
5. Says catching every exception and relabeling it as a tool error would launder an unexpected programming defect into a routine message while the host continues in an unknown state, so "catch everything" is not verification.

**Source:** Dispatch belongs to the application

## ES-ch11.15

A teammate says: "The result has the right `tool_use_id`, so the answer is right." Respond, using the luggage-tag analogy and the ways a matched result can still be wrong.

**Points:** 5

**Rubric (1 point each):**

1. Says the identifier answers a narrow question: which result belongs to which request.
2. Says that without identifiers an answer like 42 could be attached to the wrong addition.
3. Says correspondence is not correctness, and gives at least two ways a matched result can be wrong (a dispatcher bug, stale data from an external service, a request that encoded the wrong task, evidence interpreted too broadly).
4. Uses the analogy that an ID is like a luggage tag: it helps establish ownership of the suitcase and does not inspect what is inside.
5. Notes that in the fixture every tag is attached correctly and the claim at the end still disagrees with the result it is tagged to.

**Source:** Identifiers create correspondence, not truth

## ES-ch11.16

Describe what `results` does with a content batch and state precisely the scope of its duplicate-identifier check. Why is "Duplicate identifiers are rejected" too broad?

**Points:** 5

**Rubric (1 point each):**

1. Says `results` acts only on blocks whose type is `tool_use`.
2. Says it requires a nonempty string identifier not already seen in that content batch, and returns a block whose `tool_use_id` repeats the request identifier.
3. Says two tool requests with the same identifier cause a ValueError before both results are represented, and that the executed fixture observed this.
4. Says the `seen` set is local to one invocation, so global uniqueness across every turn is not established.
5. Gives the precisely scoped wording (duplicate identifiers within one processed assistant content batch are rejected) and says precision about scope stops a small guard acquiring mythical powers.

**Source:** Identifiers create correspondence, not truth

## ES-ch11.17

Describe the three main exits of the `loop` controller and how the controller is set up, including why the `call` argument is injected.

**Points:** 5

**Rubric (1 point each):**

1. Says `call` is injected so a fixture can return known response dictionaries, making the controller testable offline, and live transport can use the same controller through a different callable.
2. Says that at setup `max_turns` must be an integer from one through four and the messages list is copied.
3. Says an `end_turn` stop returns status `finished` with the trace.
4. Says any stop reason other than `tool_use` returns `stopped` with the reason preserved.
5. Says a `tool_use` stop builds results, appends the assistant content followed by a user message containing the results, and continues unless the turn budget is exhausted.

**Source:** The controller is a message machine

## ES-ch11.18

The test fixture supplies `max_tokens` and the test expects the status `stopped`. Explain why that is the right behavior, and what the loop does when a response claims `tool_use` but has no tool calls.

**Points:** 5

**Rubric (1 point each):**

1. Says the controller does not treat every non-tool stop as success.
2. Says a truncated response needs a policy decision.
3. Says presenting a truncated response as a completed answer would erase the reason execution ended.
4. Says that a response that claims `tool_use` but contains no tool calls makes the loop raise an error.
5. Says that otherwise the assistant content is retained and the results go in the next user-role message, so the next model call sees both its requests and the application's responses.

**Source:** The controller is a message machine

## ES-ch11.19

A teammate says: "We capped the loop at four turns, so it is safe and it will make progress." Respond.

**Points:** 5

**Rubric (1 point each):**

1. Says a turn budget prevents unbounded continuation.
2. Says it does not guarantee progress.
3. Gives the chapter's reason: four repeated calls can consume the budget without moving the task forward.
4. Says it does not certify safety.
5. Gives the chapter's reason: an unauthorized operation could be damaging on the first turn.

**Source:** The controller is a message machine

## ES-ch11.20

In the two-response example the controller returns `finished`. Explain what that status means, what it does not mean, and why the chapter warns against naming the exit `verified`.

**Points:** 5

**Rubric (1 point each):**

1. Says `finished` is correct about the controller: the response used the recognized completion signal before the request budget expired.
2. Says it is silent about arithmetic and does not mean the final claim agrees with the tool evidence.
3. Says `finished` names a controller state.
4. Says that had it been called `verified`, downstream code would read the name and not the mechanism.
5. States the naming rule: name each exit for the evidence behind it and keep the word verified for a claim whose claim-specific check passed.

**Source:** The controller is a message machine

## ES-ch11.21

Explain why the worked example uses scripted responses, and describe the honesty note about how the two-turn `sum-1` trace was assembled.

**Points:** 5

**Rubric (1 point each):**

1. Says scripted responses isolate controller behavior from model behavior.
2. Says they avoid spending API credits.
3. Says model variability would not be evidence about the Python mechanism, so a live transcript is not used.
4. Says the research run recorded the pieces separately: `results` on a good and a bad block, the duplicate rejection, and a loop whose single scripted response says 99 and ends the turn.
5. Says the two-turn trace composes those pieces and that `sum-1` is an illustrative identifier.

**Source:** Worked example: 42 in the trace, 99 in the claim

## ES-ch11.22

Trace `results([valid])` for the block with id `sum-1`, name `add`, and input a=17, b=25, from input block to returned content. Then say what that recorded observation supports and what it does not.

**Points:** 5

**Rubric (1 point each):**

1. Says `results` confirms `sum-1` is a new nonempty string and passes the name and input to `dispatch`.
2. Says `dispatch` finds the exact keys, exact `int` types, and finite values.
3. Says Python computes 42, which is finite, and `json.dumps(42)` produces the string "42".
4. Says the result block has `tool_use_id` equal to `sum-1` and content "42".
5. Says the observation supports claims about this implementation under this fixture, and is not evidence that every external call is correct, that Claude chose the right operands, or that the live API behaved in some unrecorded way.

**Source:** Worked example: 42 in the trace, 99 in the claim

## ES-ch11.23

In the worked example, three single changes are made to the valid `sum-1` block: replace 17 with `True`, replace the tool name with `subtract`, and put two blocks with ID `sum-1` in the same batch. Describe the outcome of each and explain why the third behaves differently from the first two.

**Points:** 5

**Rubric (1 point each):**

1. Says replacing 17 with `True` is rejected by the exact-type rule and becomes a result tied to `sum-1` with `is_error: True`.
2. Says replacing the name with `subtract` is rejected by the allowlist.
3. Says two blocks with the same ID in one batch make the duplicate-ID guard raise.
4. Says the first two are per-call dispatch failures represented to the model as `tool_result` errors, and the model may repair an invalid argument after receiving one.
5. Says the third violates the association mechanism itself, so the implementation raises, because ambiguous identity is a protocol integrity problem no repair from inside the conversation can fix.

**Source:** Worked example: 42 in the trace, 99 in the claim

## ES-ch11.24

In the worked example the assistant says 99 and the check `claimed == expected` rejects it. Explain what makes the hand calculation of 17 + 25 a genuinely independent check here, and when independence fails.

**Points:** 5

**Rubric (1 point each):**

1. Says that for elementary arithmetic a hand calculation is genuinely independent of the helper being audited.
2. Says the expected value is 42, so the comparison with 99 rejects the claim.
3. Says that in a consequential system independence should be designed around failure modes, not assumed.
4. Says that calling the same buggy helper twice is repetition, not corroboration.
5. Says two routes that share the same incorrect source data are not independent merely because their code differs.

**Source:** Worked example: 42 in the trace, 99 in the claim

## ES-ch11.25

For each of the following claims from the evidence matrix, say what the evidence establishes and give one independent check: (a) the dispatcher accepted the arguments; (b) Python produced 42; (c) the result belongs to `sum-1`; (d) the loop completed; (e) the final answer is correct.

**Points:** 5

**Rubric (1 point each):**

1. (a) The absence of a dispatch error and a returned value establish that local validation passed; the check is boundary tests or code review.
2. (b) The matching `tool_result` content establishes the output of this implementation; the check is a hand calculation or separate derivation.
3. (c) The matching identifier establishes request/result correspondence; the check is a trace invariant check.
4. (d) `end_turn` and `finished` establish that the controller recognized completion; the check is to inspect the stop reason and budget.
5. (e) Completion establishes nothing about correctness until compared; the check is to compare the parsed claim with 42.

**Source:** Worked example: 42 in the trace, 99 in the claim

## ES-ch11.26

The chapter calls the last row of the evidence matrix "the teardown." Explain why a polished final sentence is a new claim and list the options the chapter gives for handling it.

**Points:** 5

**Rubric (1 point each):**

1. Says a polished sentence at the end of a correct-looking trace is a new claim.
2. Says evidence does not automatically flow into narration.
3. Gives the option of constraining the final output so correspondence is checkable.
4. Gives the options of parsing and comparing the claim, or presenting the evidence for a human decision.
5. Says which option is appropriate depends on stakes and task semantics.

**Source:** Worked example: 42 in the trace, 99 in the claim

## ES-ch11.27

Suppose the assistant's final sentence had said 42 instead of 99. Explain how a reader could still be misled and what the chapter says to do about it.

**Points:** 5

**Rubric (1 point each):**

1. Says the final sentence would be correct.
2. Says a reader could still leave believing something the trace has not shown.
3. Says the reason is scope: a tool result reports on an operation, while a reader's sentence is about an outcome.
4. Says that before a report ships you write the inference the reader will draw from each verb and ask which observation would make that inference true.
5. Says that if no row in the trace supplies that observation, the report should say the narrower thing, as in the gap between "Python produced 42" and "final answer is correct."

**Source:** When the report is accurate and the reader is still misled

## ES-ch11.28

Describe the screening-tool case from the companion book on computational skepticism and the question it adds to this chapter.

**Points:** 5

**Rubric (1 point each):**

1. Says the case is labeled a composite, not a sourced incident.
2. Says the screening tool names the two features that drove its prediction.
3. Says the radiologist checks that both features are present in the image and concurs.
4. Says the explanation was accurate about the model but did not say the model had learned a shortcut, so an accurate explanation made a wrong decision feel right.
5. Names the missing question as the audience question: who is reading this, and what do these words mean to them?

**Source:** When the report is accurate and the reader is still misled

## ES-ch11.29

A tool report says a file was "saved," a record was "deleted," a message was "sent," and a build was "deployed." For each verb, explain how an accurate report could still mislead the reader.

**Points:** 5

**Rubric (1 point each):**

1. Saved: tells the reader the file exists where they expect, with the content they meant, and will exist tomorrow, while a successful write call establishes far less.
2. Deleted: may mean removed from this folder, from the repository history, or from every copy.
3. Sent: may mean handed to a mail server or received by a person.
4. Deployed: may mean uploaded or serving traffic.
5. Concludes each word is accurate in the operation's use and misleading in the reader's, so the report should say the narrower thing.

**Source:** When the report is accurate and the reader is still misled

## ES-ch11.30

A file-writing tool returns success. State what a successful write establishes, what it does not establish, and the checks the chapter lists for closing the gap.

**Points:** 5

**Rubric (1 point each):**

1. Says a successful write establishes that bytes were written to a particular resolved path at a particular time.
2. Says it does not establish that the file satisfies the user's assignment.
3. Says it does not establish that another process did not change the file afterward, that the repository contains the change, or that a remote copy exists.
4. Lists verification checks: read the resolved target back, compare expected content, inspect `git diff`, run relevant tests, and check remote state separately if publication is claimed.
5. Says each check answers a different question and "the tool returned success" is only one item in that chain.

**Source:** Verification surfaces for real tools

## ES-ch11.31

Give the chapter's examples of tool evidence that describes something narrower than it appears (a row count, an upload report, a retrieved passage), and describe the design move that makes verification surfaces explicit at tool boundaries.

**Points:** 5

**Rubric (1 point each):**

1. Says a row count describes the snapshot the query actually saw.
2. Says an upload report can coexist with failing health checks.
3. Says a retrieved passage can be the most similar one without entailing the answer.
4. Says the design move is to return resolved paths, preserve query parameters, timestamps, and stable identifiers, and keep errors structured.
5. Says to record enough of the trace to reproduce a decision without leaking credentials or restricted data, asking what minimum evidence lets an authorized reviewer test the claim.

**Source:** Verification surfaces for real tools

## ES-ch11.32

Evaluate the claim "If the schema is correct, invalid calls cannot happen." Say what is true in it, what is false, and which fixture in the chapter shows the problem.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the claim as a misconception the chapter breaks with a counterexample.
2. Grants that the schema guides model output.
3. Grants that a platform may check the schema.
4. Says the local runtime must defend its boundary regardless.
5. Cites the Boolean fixture as a Python-specific edge that a vague numerical assumption can miss.

**Source:** Common misconceptions, broken with counterexamples

## ES-ch11.33

A report states a total that came from correct addition of numbers a tool returned. Explain, using the chapter's misconception "A tool result proves the answer," why the total could still be the wrong business answer and where in the matrix the failure would be caught.

**Points:** 5

**Rubric (1 point each):**

1. Says a tool result proves only what the operation and its evidence support.
2. Says that if the operands were chosen from the wrong records, correct addition produces the wrong business answer.
3. Says correspondence by identifier and correct arithmetic do not establish that the operands were the intended ones.
4. Locates the failure at the task-to-request transition, where wrong operands are the plausible failure.
5. Gives the check for that transition: read the request against the task text, and stop and fix the request path if it disagrees.

**Source:** Common misconceptions, broken with counterexamples

## ES-ch11.34

Evaluate the claim "Deterministic Python is infallible." Say what Python does reliably, what it cannot guarantee, and why that still makes deterministic code a good audit tool.

**Points:** 5

**Rubric (1 point each):**

1. Says Python repeats its implementation consistently.
2. Says the implementation can still encode the wrong formula.
3. Says it can parse the wrong field or use stale input.
4. Says deterministic code does not confabulate and is wrong the same way on every run, so a test can find the error.
5. Says routing a step to deterministic code makes it inspectable, not infallible.

**Source:** Common misconceptions, broken with counterexamples

## ES-ch11.35

Describe how to start building a reusable tool evidence matrix and the order of work the chapter recommends.

**Points:** 5

**Rubric (1 point each):**

1. Says to start with the final sentence you want to be able to say and break it into atomic claims.
2. Says that for each claim you name the producing operation, the evidence artifact, the scope of that evidence, an independent check, and a failure response.
3. Says that if you cannot name a check that could reject the claim, the workflow is relying on assurance.
4. Gives the first half of the order: decide which checks fail differently, write the gate, build your own baseline.
5. Gives the second half of the order: conduct Claude Code against the gate, ship the matrix with a sign-off, then divide the work honestly.

**Source:** Building a reusable tool evidence matrix

## ES-ch11.36

Explain the rule from Conducting AI that using one tool to audit another reduces error only to the degree that the two fail differently. Include the example of two chat models, the confidence level the chapter attaches to it, and the stronger advice that does not depend on it.

**Points:** 5

**Rubric (1 point each):**

1. States the rule: using one tool to audit another reduces error only to the degree the two fail differently.
2. Says that if two checks make the same mistake on the same input, combining them leaves the mistake where it was.
3. Says two chat models asked the same question can fail the same way because they learned from overlapping text, so agreement can occur without verification.
4. Says the book marks this point as medium confidence, to be held loosely.
5. Gives the stronger advice that does not depend on it: audit a generative claim with a non-generative tool.

**Source:** Choose checks by failure mode

## ES-ch11.37

A teammate proposes having a second chatbot review the first chatbot's total instead of recomputing it. Respond using the chapter's account of non-generative checks.

**Points:** 5

**Rubric (1 point each):**

1. Says an AI checking an AI is not a second opinion; it is the first opinion run twice (the line from Chapter 1).
2. Says a model's verdict on quality is a verdict, not a verification.
3. Says deterministic code does not confabulate and is wrong the same way on every run, so a test can find it.
4. Says a lookup against a real source either finds the source or does not, and a schema validator catches malformed structure however plausible the content reads.
5. Concludes that the audit should use a non-generative tool.

**Source:** Choose checks by failure mode

## ES-ch11.38

List the ways the producing route in the addition example could be wrong, and for three checks (a hand calculation of 17 + 25, inspecting the task against the request, comparing the final claim to the returned result) say what each catches and what it misses.

**Points:** 5

**Rubric (1 point each):**

1. Lists the failure points: wrong operands, dispatch mapping the name to the wrong operation, serialization changing the value, association attaching the result to the wrong ID, and narration stating a different number.
2. Says a hand calculation avoids the dispatcher and serialization path.
3. Says a hand calculation does not establish that 17 and 25 were the intended operands.
4. Says inspecting the task against the request checks operand selection but does not recompute the result, while comparing the final claim to the result catches narration drift.
5. Says a shared wrong result can make the claim and the result agree, so no single check covers the entire chain.

**Source:** Choose checks by failure mode

## ES-ch11.39

State the six-step design procedure the chapter gives for choosing checks.

**Points:** 5

**Rubric (1 point each):**

1. Write the consequential claim in a form that can be false.
2. Draw the operations and transformations that produced it.
3. Name one plausible failure at every transition.
4. Select checks that enter the chain from different evidence sources.
5. Record the shared assumptions that remain after the checks agree, and decide in advance what disagreement will stop, retry, or escalate.

**Source:** Choose checks by failure mode

## ES-ch11.40

Define verification theater using the chapter's example of a checker that disagrees with the controller, and say what prevents it.

**Points:** 5

**Rubric (1 point each):**

1. Describes the situation: a checker disagrees and the controller simply asks the model to choose which number sounds better.
2. Says the workflow has not used the check.
3. Says it has converted evidence into another prompt.
4. Says a stop policy makes disagreement operational.
5. Gives at least two of the gate matrix's disagreement responses as examples (such as do not run the tool, treat the result as untrusted, raise, report the exit and not a verdict, withhold verified and escalate).

**Source:** Choose checks by failure mode

## ES-ch11.41

A receipt tool returns a subtotal, and Python recomputes the sum of the extracted rows. The two agree. What does the agreement establish, what does it not establish, and what check would fail differently?

**Points:** 5

**Rubric (1 point each):**

1. Says agreement establishes internal consistency.
2. Says both routes share the extracted rows.
3. Says a missing row would fool both routes together.
4. Says that checking a sample against the source image fails differently.
5. Says human review may still be needed where handwriting or business rules make the interpretation ambiguous.

**Source:** Choose checks by failure mode

## ES-ch11.42

How should the depth of verification be chosen? Contrast a formatting preview with a payment instruction.

**Points:** 5

**Rubric (1 point each):**

1. Says verification costs time, permissions, and attention.
2. Says depth should be tied to consequence and reversibility.
3. Says a formatting preview may need only a visual glance.
4. Says a payment instruction needs identity, amount, destination, authorization, and post-action confirmation.
5. Says those checks must be available before the action and not bolted onto a celebratory report afterward.

**Source:** Choose checks by failure mode

## ES-ch11.43

Describe what the chapter's gate contains and when and where it is written. Which parts of the design did the lesson fix, and which parts are yours in your own matrix?

**Points:** 5

**Rubric (1 point each):**

1. Says the gate is written in your learner workspace before you ask Claude Code for anything.
2. Says it is written in plain sentences and one table, and names who decided each item.
3. Says the lesson fixed the design: one tool `add`, scripted fixtures, operands 17 and 25, a scripted final claim of 99, and a request budget of at most four.
4. Says that in your own matrix the claims and the operands are yours.
5. Says the contract (what `dispatch`, `results`, and `loop` do) does not say the final sentence is true, which is a separate claim needing its own row.

**Source:** The gate: design the matrix before the run

## ES-ch11.44

For each of these transitions from the gate's matrix, state the plausible failure, the check that fails differently, and what disagreement does: (a) task to request; (b) request to dispatch; (c) result to request; (d) loop to status; (e) narration to claim.

**Points:** 5

**Rubric (1 point each):**

1. (a) Wrong operands; you read the request against the task text; stop and fix the request path.
2. (b) Wrong operation mapped, or `True` accepted; boundary tests you wrote before reading the reference; do not run the tool.
3. (c) Result attached to the wrong ID; a trace invariant that each `tool_use_id` appears once and matches a request; raise and do not continue.
4. (d) `finished` read as success; inspect the stop reason and budget; report the exit, not a verdict.
5. (e) Final sentence differs from the result; parse the number and compare with the independent value; withhold verified and escalate to you.

**Source:** The gate: design the matrix before the run

## ES-ch11.45

The chapter describes wrong versions of the program that your tests must catch. Describe the changes, which are and are not caught by the six reference tests, and the lesson for your own gate.

**Points:** 5

**Rubric (1 point each):**

1. Says replacing the exact-type test with `isinstance(v, (int, float))` makes `True + 2` return 3, and the reference suite catches that one.
2. Says deleting the duplicate-identifier guard leaves all six reference tests passing.
3. Says renaming the `finished` exit to `verified`, or deleting the overflow check, also leaves all six reference tests passing.
4. Explains why: none of the reference tests sends a duplicate, reaches the `end_turn` exit, or adds two huge floats.
5. Concludes that a gate that does not name those cases will not catch them either, and that if your tests cannot tell these from the right program the gate is not finished.

**Source:** The gate: design the matrix before the run

## ES-ch11.46

Explain the gate's "what a failure looks like" sentence and "what this evidence may claim" statement.

**Points:** 5

**Rubric (1 point each):**

1. Says you write one dated sentence about what you would see if the matrix were wrong.
2. Describes that sentence's content: a trace where the status is `finished`, every identifier matches, and no row can say no to the final sentence.
3. Says that written after reading the output, the sentence only describes the output.
4. Says the evidence may claim protocol-level statements about this implementation under these fixtures, and equality between a parsed number and an independently derived one.
5. Says it cannot say that 17 and 25 were the operands anyone meant.

**Source:** The gate: design the matrix before the run

## ES-ch11.47

What can Claude do for your gate, and what can it not do without defeating the gate's purpose? Include what you give Claude Code and why a failing test of yours is informative.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude can sharpen the gate by finding a transition you left without a check.
2. Says Claude cannot write the gate for you without defeating its purpose.
3. Says the gate is where your decision about what counts as independent goes on the record.
4. Says you give Claude Code the contract, the tests, and the matrix, and not your implementation.
5. Says a failing test is often a gap in your gate, which Claude cannot see because it only has what you wrote.

**Source:** The gate: design the matrix before the run

## ES-ch11.48

Describe what the chapter asks you to do in "Build It," why you do it before consulting the reference, and how to read the six reference tests.

**Points:** 5

**Rubric (1 point each):**

1. Says you write your own `dispatch`, `results`, and `loop` under `learning-artifacts/week-11/` before the reference, with a one-tool allowlist, exact argument keys and numeric types, bounded turns, and an explicit stop on truncation and unsupported stop reasons.
2. Says every `tool_use` block is processed, the assistant content is kept unchanged, and user-role `tool_result` blocks are appended.
3. Says you trace one successful case by hand, marking the input boundary, the transformation, and the returned result, and trace one failure from the tests, changing one input at a time.
4. Says your version is the baseline: the record of what you understood before Claude touched anything, and the instrument you measure Claude's version against.
5. Says to read the six tests (happy path, unknown tool, Boolean, preserved identifier, represented error, truncated stop) as six questions and not as "the code works," and that the demo's scripted responses are fixtures, not evidence Claude generated or verified anything.

**Source:** Build It: the baseline that lets you audit

## ES-ch11.49

After you hand Claude Code your gate, the chapter asks you to do four things with the result. Describe them and say which part stays yours.

**Points:** 5

**Rubric (1 point each):**

1. Says to run your own tests on what it returns and note which failed, since a failing test is often a gap in your gate.
2. Says to compare its implementation with your baseline and name one difference in behavior.
3. Says that a boundary it handled that you missed is a revision to your gate, and one it silently ignored is a defect your tests failed to catch.
4. Says to ask Claude for a deliberately wrong version that still passes your tests, and if it does, your test list was too weak.
5. Says to ask Claude to run the matrix's checks and log commands, outputs, and versions, while the reason each check is independent of the route it checks is the column you write.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch11.50

Describe what the chapter says to ship, what the matrix should record about what remains untested, and what the negative evidence shows.

**Points:** 5

**Rubric (1 point each):**

1. Says to ship the tool schema, the validation rules, a valid and a rejected request/result trace, and the matrix, with exact commands and observed outputs, identifying which behaviors came from fixtures and which from an authorized live run.
2. Says the reference tests do not prove global identifier uniqueness, security under hostile inputs, safe concurrency, durable logging, live service behavior, or correctness for a different tool.
3. Says to add tests because a capstone claim needs them, not to inflate a count, such as traversal rejection and read-back for a file-writing capstone.
4. Says to preserve one failed case and the decision it changed, since a rejected Boolean, duplicate identifier, or mismatched final claim shows the boundary can say no, while a system demonstrated only on its happy path has demonstrated production, not control.
5. Says to record versions, and when adding the artifact to the Week 15 evidence trail to name which capstone claim it supports and what further review it needs.

**Source:** Ship It: the matrix, the trace, and the sign-off

## ES-ch11.51

Describe the sign-off template. Which line does the most work, and why is it the line a drafted sign-off is least likely to include?

**Points:** 5

**Rubric (1 point each):**

1. Names the template's lines: Checked, How, Not checked, Not claiming, and Signed or withheld.
2. Says the How line records whether a row was checked by hand, by a test written before reading the reference, by a recomputation outside the controller, or with Claude's help.
3. Says the Not checked line does the work.
4. Says a drafted sign-off is least likely to include it because the draft has no record of what you did not run.
5. Says you write the sign-off from your record, and if your evidence does not support signing, withholding is an honest result.

**Source:** Ship It: the matrix, the trace, and the sign-off

## ES-ch11.52

Explain what words this chapter's sign-off may use and how that differs from Chapter 10's sign-off. When may it use the word verified?

**Points:** 5

**Rubric (1 point each):**

1. Says Chapter 10's sign-off covered a plan, which is a prediction.
2. Says this chapter's sign-off covers a record of what ran.
3. Says it may therefore say what was recorded, computed, and tested.
4. Says verified is for a claim whose check came from outside the route that produced it.
5. Says that a `finished` status or a matching identifier does not license the word verified (those appear in the Not claiming line).

**Source:** Ship It: the matrix, the trace, and the sign-off

## ES-ch11.53

Using the driver's seat table, say what Claude should do and what you should do for each of the five tasks, and explain why the fourth row is the one to look at.

**Points:** 5

**Rubric (1 point each):**

1. Proposing a call: Claude proposes the name and arguments as structured data; you decide which operations exist and what the dispatcher refuses, because the allowlist is policy, not syntax.
2. Writing the contract and matrix: Claude challenges it by finding an unchecked transition; you write it first, with a failure per transition.
3. Implementing `dispatch`, `results`, `loop`: Claude implements fast and proposes extra tests; you build your own baseline first and run your tests on its version, because you cannot audit a boundary you never broke.
4. Running and logging the checks: Claude runs them, diffs outputs, and logs commands and versions; you say which check is independent of which route and what disagreement does, because independence depends on where each route's inputs came from, which the log does not show.
5. Wording the report: Claude drafts it and flags overclaim; you choose the verb and sign or withhold, and your name is on the claim.

**Source:** The driver's seat

## ES-ch11.54

The chapter says Claude can compute both routes but cannot show whether they are independent. Explain, and say what the artifact must record to prove the split happened.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude can compute and log both routes.
2. Says whether two routes share an input, a source, or an assumption is a fact about your data and your task.
3. Says a transcript of both routes does not display that fact.
4. Says the artifact records one check Claude ran and logged and one independence judgment you made, in your own words.
5. Says that if you cannot point to the log line and the sentence, the split happened in your head and not in the record.

**Source:** The driver's seat

## ES-ch11.55

Explain how Chapters 4, 5, 8, and 10 come together in this chapter, and give the three examples of keeping layers separate in code.

**Points:** 5

**Rubric (1 point each):**

1. Names Chapter 4 as supplying the bounded controller and Chapter 5 as separating capability from authority.
2. Names Chapter 8 as exposing request identity and result messages and Chapter 10 as requiring a plan to stay auditable as execution diverges.
3. Describes the combined flow: a planned step becomes a model-proposed request, validation decides whether the application may dispatch it, execution produces an observation, and verification compares consequential claims with evidence outside the model's narration.
4. Gives examples of separation: a model adapter should not silently gain filesystem authority, and a dispatcher should not decide a business outcome is satisfied merely because a function returned.
5. Adds that a presentation layer should not omit errors to make the report cleaner, because separation gives reviewers places to disagree with the system and gives you places to put a gate.

**Source:** Integration with the agent built so far

## ES-ch11.56

During your work, a check disagrees, or Claude finds a case your contract missed. What should you do with the gate, and what does the chapter say distinguishes good practice from the failure the sign-off exists to prevent?

**Points:** 5

**Rubric (1 point each):**

1. Says design-first does not mean frozen.
2. Says to reopen the gate and change it.
3. Says to record that you did, with a dated reason.
4. Says a revised gate with a dated reason is evidence of control.
5. Says a gate quietly edited to match what the code does is the failure the sign-off exists to prevent.

**Source:** Integration with the agent built so far

## ES-ch11.57

Describe the verify-and-reflect tasks: what small claims you test, how you explain a passing case and a rejected input, what you do with the word verified, and what the reflection asks.

**Points:** 5

**Rubric (1 point each):**

1. Names claims small enough to test, such as the rejection of a Boolean, the preservation of an identifier, the exit taken on `max_tokens`, or the equality between a parsed claim and 42, and says to name which matrix row each check addresses.
2. Says to explain one passing case from input block to returned content without reading Claude's explanation.
3. Says to explain why one rejected input's refusal belongs to the contract.
4. Says that if your strongest sentence says verified, you must point to the check that came from outside the route.
5. Says the reflection asks which distinction you originally collapsed (identity and truth, completion and verification, deterministic and infallible, repetition and independence) and to name the input or check that separated them again, instead of a generic resolution to be more careful with AI.

**Source:** Verify and reflect

## ES-ch11.58

Assessment 5 asks you to construct a duplicate-identifier batch. Describe what you record and explain, and what extra test you write to show the guard matters.

**Points:** 5

**Rubric (1 point each):**

1. Says to construct a batch with duplicate IDs and record the observed failure.
2. Says to explain why the implementation raises instead of returning two ambiguous results.
3. Says to state the scope of the guard precisely (within one batch, not global).
4. Says to write the test the six reference tests lack.
5. Says to show that the test fails when you delete the guard.

**Source:** Assessments - ungraded practice

## ES-ch11.59

Assessment 11 asks you to design a controller extension that may return `verified` only after a claim-specific checker passes. List what the design must cover and how it should be tested.

**Points:** 5

**Rubric (1 point each):**

1. Says the status `verified` is returned only after a claim-specific checker passes.
2. Says the design must define behavior for an unparsable final claim.
3. Says it must define behavior for checker failure and for budget exhaustion.
4. Says it must define behavior for a tool result whose content cannot safely be logged.
5. Says it must state who may override a failed checker and what that person must record, and that the design must test at least one false-positive risk.

**Source:** Assessments - ungraded practice

## ES-ch11.60

Summarize what the chapter says you can now do, in terms of reading a tool loop, who owns validation and execution, identity versus truth, stop reasons, and the word verified.

**Points:** 5

**Rubric (1 point each):**

1. Says you can read a tool loop as a chain of separately testable claims.
2. Says Claude proposes structured calls while Python owns validation and execution, and you write the contract that says what the dispatcher refuses before anyone implements it.
3. Says you can preserve request/result identity without mistaking identity for truth.
4. Says you can treat stop reasons as controller signals, bound continuation, and keep expected tool failures visible.
5. Says you can place an independent check between a fluent final sentence and the word verified, say which checks Claude ran for you and which judgment of independence stayed yours, and sign only as far as the record supports.

**Source:** Capabilities summary

## ES-ch11.61

The Anthropics section points to Anthropic's Handle tool calls guidance and the public tool-use course. Say what the chapter asks you to do with each, and what it does not require.

**Points:** 5

**Rubric (1 point each):**

1. Says the Handle tool calls guidance describes client-tool request/result association and message construction.
2. Says to compare it with the course implementation, especially the use of `tool_use` identifiers, matching `tool_result` blocks, and ordering in the next user message.
3. Says the page was retrieved for the research packet on 2026-09-06 and should be treated as rolling documentation, checked again when implementing against the live API.
4. Says the public tool-use course offers upstream examples for comparison, to be run only as an explicit optional extension.
5. Says the course's offline Python mechanism and your Claude Code account are sufficient, so direct API credits are not required.

**Source:** Anthropics

## ES-ch11.62

The Computational Skepticism section adds a diagnostic question from the companion book's discussion of agent outcomes. State it and apply it to your evidence matrix.

**Points:** 5

**Rubric (1 point each):**

1. States the question: of any check or defense that held, under what condition would this have failed?
2. Says that if you cannot name the condition, you have not validated it, only observed that this time nothing went wrong.
3. Says the false-success catch is to observe the world's state independently of the agent's report.
4. Says that for every row where the independent check agreed, you write the condition under which it would have agreed anyway: the same operands, the same extracted rows, the same source.
5. Says that a row with no such condition named is a row you observed, not one you checked, and that the book's agent studies are exploratory, so you take the question from them, not rates.

**Source:** Computational Skepticism

## ES-ch11.63

The Conducting AI section introduces laundering. Define it and explain how you would trace the 42 through the chapter's seams.

**Points:** 5

**Rubric (1 point each):**

1. Defines laundering as an unverified value gaining authority as it passes through clean steps.
2. Names the seams for the 42: the dispatcher's return, `json.dumps`, the `tool_result` content, the assistant's sentence, and the row in your matrix.
3. Says that at each seam you write what is passed.
4. Says that at each seam you write what it is trusted to be and how that trust was earned.
5. Says that a typed field, a serialized string, or a row that says "Python produced 42" makes a value look checked, and that polish is not provenance.

**Source:** Conducting AI

## ES-ch11.64

Where does the Conducting AI section say the gate belongs in this chapter, and why would a check at the report be too late?

**Points:** 5

**Rubric (1 point each):**

1. Says the gate belongs where the claim first enters, which in this chapter is the request, not the report.
2. Says a check at the last seam cannot catch a wrong operand chosen at the first.
3. Says the conductor's work is choosing the routing and defining what evidence must cross each seam.
4. Says the model can make the performance fluent.
5. Says fluency alone cannot show that it was correct.

**Source:** Conducting AI

## ES-ch11.65

Explain the forward bridge to Chapter 12. Why is a verified result not permanently verified, and what does the chapter ask you to carry forward?

**Points:** 5

**Rubric (1 point each):**

1. Says that today 42 is supported by a recorded operation and an independent calculation.
2. Says that tomorrow a memory system may retrieve "42" after the operands, source, code, or task have changed.
3. Says a verified result is not permanently verified in every future context.
4. Says to carry the sign-off forward, with its date and versions, for this reason.
5. Says Chapter 12 asks what has to travel with memory so that recall does not turn yesterday's evidence into today's unsupported confidence.

**Source:** Forward bridge
