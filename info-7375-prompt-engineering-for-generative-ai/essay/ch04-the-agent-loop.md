# Chapter 4: The agent loop

## ES-ch04.1

A system looks up the same record again and again. Each lookup succeeds and each observation is logged. According to the chapter, what question should an outside reader ask, and why does a longer trace not answer it? Then use the repeated-lookup run with a turn budget of two to say who made its stop possible.

**Points:** 5

**Rubric (1 point each):**

1. States the question: what changed that makes completion more justified than it was one turn ago.
2. Notes that each lookup can succeed and be logged while the task gets no closer to a supported answer.
3. Says a longer trace is only more recorded activity, which can look like progress from inside a poorly described report.
4. Reports that the repeated-lookup run with a budget of two stops after two recorded actions with `budget-exhausted`, and does not invent a final answer.
5. Says someone chose the number two before the loop ran, so the stop was designed, not discovered.

**Source:** Chapter 4 opening (before the first section heading)

## ES-ch04.2

Contrast the chapter's two constructed runs: the repeated lookup with a budget of two, and the lookup of blue followed by a finish with red. For each, give the returned status, say whether the property is built in beforehand or caught only afterward, and explain why neither run says anything about the capability of whatever proposes the actions.

**Points:** 5

**Rubric (1 point each):**

1. Repeated-lookup run: status `budget-exhausted` after two recorded actions.
2. Blue-then-red run: status `finished` with answer red.
3. The budget limit is a property built in before anything executes; the loop cannot run past it.
4. The wrong answer under a well-behaved status is caught only by looking at the world after the loop stops, because the controller never compares the answer with the observation.
5. Neither run says how capable the proposer is; both are about where the stop lives and what it is allowed to mean.

**Source:** Chapter 4 opening (before the first section heading)

## ES-ch04.3

Apply Chapter 1's three jobs (conduct, check, drive) to the most consequential line in any agent, the one that ends the run. Give one concrete decision or responsibility for each job.

**Points:** 5

**Rubric (1 point each):**

1. Conduct: the exits and the budget are written down before the loop starts.
2. Check: `finished` records only that a finish action arrived.
3. Check: what anyone is entitled to believe beyond that is a separate question with a separate check.
4. Drive: Claude may take the stop that ends the run.
5. Drive: the stop that closes the task is the human's.

**Source:** Chapter 4 opening (before the first section heading)

## ES-ch04.4

Why does the chapter use a scripted policy rather than a live model call, and what does that choice not show? Then explain why answering the chapter's questions about sequence and termination is necessary for an agentic workflow but not sufficient.

**Points:** 5

**Rubric (1 point each):**

1. A scripted policy makes each decision inspectable and repeatable.
2. The machinery is small: an iterator supplying action dictionaries, a dispatcher handling a lookup, and a trace accumulating observations.
3. It does not reproduce Claude's private reasoning or Claude's current agent implementation.
4. Which action arrives next, what observation follows, what is recorded, and which condition ends the run are necessary questions for an agentic workflow.
5. Answering them grants no permission to act and establishes nothing about whether the final claim is true (Chapter 3 separated capability from authority).

**Source:** Chapter 4 opening (before the first section heading)

## ES-ch04.5

List the elements the chapter says you must write as a gate before any implementation exists, and describe the three things you then do with Claude Code against that gate.

**Points:** 5

**Rubric (1 point each):**

1. The gate lists every exit of the loop.
2. It states the unit of the budget.
3. It states what must never be fabricated.
4. It names a separate check that decides whether a finished answer moves on.
5. You conduct Claude Code against the gate, run your own tests on what it returns, and write a sign-off that names the exits you exercised and the ones you did not.

**Source:** What you will be able to do

## ES-ch04.6

Name the three jobs inside any agent loop. Say which one each part of the chapter's reference performs, which job is absent from the reference, and why the chapter pulls the jobs apart.

**Points:** 5

**Rubric (1 point each):**

1. Job one is proposing the next action; in the reference this is the policy, an iterable of action dictionaries.
2. Job two is dispatching the action, recording the result, and deciding whether the run continues; this is the controller, the `run` function.
3. Job three is deciding whether the final result is any good.
4. Job three does not exist in the reference, and its absence is the subject of the next sections.
5. In a chat window the three arrive as one voice saying done; pulling them apart gives each one an owner.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.7

A colleague says the scripted list of actions is "the agent's policy," so the system adapts to what it observes. Respond using the chapter.

**Points:** 5

**Rubric (1 point each):**

1. The policy here is an iterable of action dictionaries, and a prepared list is enough.
2. It is not a learned model.
3. It does not change its next action based on what the controller observed, because nothing feeds the observation back.
4. An adaptive system would need a defined route from observations to its next decision.
5. That route should not be described as implemented merely because the code uses the name policy.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.8

Explain two debugging payoffs of separating the policy from the controller, then say who owns the turn budget and why a model-backed policy should not be able to change it.

**Points:** 5

**Rubric (1 point each):**

1. A poor action sequence dispatched exactly as specified is a fault in the sequence.
2. The right sequence with the wrong status is a fault in the controller.
3. A model-backed policy would be a new source of action requests.
4. It should not inherit the power to redefine the runtime's limits just because it supplies the next action.
5. The turn budget belongs to the controller; nothing the policy says creates another iteration after the range is spent.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.9

A teammate says: "The loop has `max_turns=4`, so the run will always finish quickly." Evaluate the claim using the chapter's scenario in which fetching the next item from the iterator never returns.

**Points:** 5

**Rubric (1 point each):**

1. The loop bounds how many turns it begins.
2. It places no timeout around an arbitrary iterator or a slow tool.
3. If fetching the next item never returns, an iteration count cannot interrupt the wait.
4. The turn budget is therefore not a wall-clock guarantee, and the teammate's claim about finishing quickly does not follow.
5. What the limit does bound is ordinary completed turns in the demonstrated loop.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.10

Distinguish the two stops hidden under the word "done." For each, say what takes it and what records it, and explain why confusing them is the risk the rest of the chapter works against.

**Points:** 5

**Rubric (1 point each):**

1. One stop ends the run: the controller returns.
2. The other closes the task: a person, or a check a person designed, accepts the result as meeting the need that started the run.
3. The controller can take the first stop.
4. Nothing in the `run` function can take the second stop.
5. Confusing them means reading `finished` as verified task success.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.11

Records are `{"color": "blue"}` and the budget is the default of four. Predict the status, the answer field, and the trace for each policy: (a) an empty policy; (b) one lookup of `color`, then no more actions; (c) a single finish action with answer `x` and no lookup. Explain why the chapter asks you to predict the kind of termination rather than "success" or "failure," and when the prediction must be written.

**Points:** 5

**Rubric (1 point each):**

1. (a) `incomplete`, no answer, and an empty trace.
2. (b) `incomplete`, no answer, and a trace with one lookup entry whose observation is `blue`.
3. (c) `finished` with answer `x` and an empty trace.
4. Predicting the kind of termination, not success or failure, is what makes the code inspectable.
5. The prediction must be written before running, because one written afterward only describes the output.

**Source:** Every return statement is an exit someone decided

## ES-ch04.12

Describe the budget check at the top of the controller: what it accepts, how it tests the value, and when a bad value is rejected. Why does the chapter call the type test an explicit choice, and what does the lesson test for?

**Points:** 5

**Rubric (1 point each):**

1. The budget must be an integer of at least one.
2. The check is `type(max_turns) is int`.
3. It is an explicit type choice rather than acceptance of anything that behaves like a number.
4. A bad budget is rejected before the iterator or the trace exists.
5. The lesson's tests include rejection of a budget of zero.

**Source:** Every return statement is an exit someone decided

## ES-ch04.13

A finite policy contains exactly one lookup, and the budget is four. What does the controller return, and by what mechanism? Why is the result not `finished`, and what does the status fail to establish?

**Points:** 5

**Rubric (1 point each):**

1. After the first turn, `next(iterator)` raises `StopIteration` on the second request.
2. The controller returns `incomplete` with the trace so far, which holds the one lookup entry.
3. It does not read silence as completion; an exhausted supply of scripted actions is a different condition from an explicit finish.
4. No answer is returned; `incomplete` manufactures none.
5. `incomplete` does not establish that the task is done or that it is impossible.

**Source:** Every return statement is an exit someone decided

## ES-ch04.14

Records are `{"color": "blue"}`, the budget is four, and the policy is: `{"name": "shell"}`, then `{"name": "lookup", "key": "color"}`, then `{"name": "finish", "answer": "blue"}`. Trace the run by hand: give the status, the answer, and each trace entry. What does the disallowed-tool observation show, and what does it not show?

**Points:** 5

**Rubric (1 point each):**

1. Turn 1: `shell` is not dispatched; the trace gets an entry with action `shell` and observation `error: tool not allowed`.
2. Turn 2: the lookup adds an entry with observation `blue`.
3. Turn 3: the finish returns status `finished` with answer `blue`.
4. The returned trace has two entries; the finish is not appended.
5. The not-allowed message is concrete but does not establish permissions for any larger runtime; Chapter 5 builds that boundary.

**Source:** Every return statement is an exit someone decided

## ES-ch04.15

The chapter says the small size of the function invites exactness and also shows what its author left undecided. Name the four things it says are open, and explain why each belongs in your gate.

**Points:** 5

**Rubric (1 point each):**

1. A finish action with no answer field returns `finished` with an empty string, so a stop with no substance gets through.
2. A non-dictionary action such as a bare string fails with an `AttributeError`, outside the three normal statuses, and there is no schema validator like Chapter 2's.
3. An unknown action name consumes a turn and the run continues; stopping, retrying, and escalating are three different policies, and none is implemented.
4. The trace holds the action name but not the lookup key, and it never holds the finish.
5. Each of the four belongs in the gate as a decision; a validator added later should be described as an extension.

**Source:** Every return statement is an exit someone decided

## ES-ch04.16

Records are `{"color": "blue"}`, the budget is 3, and the policy is lookup, lookup, lookup, then a finish with answer `x`. Give the status, the answer, and the trace length. What happened to the finish, and what does this show about the unit of the budget?

**Points:** 5

**Rubric (1 point each):**

1. The status is `budget-exhausted`.
2. The trace has three lookup entries (turns 1 to 3), each observing `blue`.
3. The finish is never consumed, because all three turns went to lookups.
4. No answer is returned; none is fabricated.
5. The terminal action costs a turn, so the budget counts action-consumption turns.

**Source:** Every return statement is an exit someone decided

## ES-ch04.17

A reader sees a trace showing a lookup of `color` that returned `blue`, followed by an answer of blue, and concludes that blue is the true color. Respond using the chapter: what does the trace evidence show, what does it not show, and what should a report say?

**Points:** 5

**Rubric (1 point each):**

1. The trace is evidence of the local operation's result.
2. It is not a record of private reasoning.
3. The mapping is a fixture, a table we invented.
4. An answer of blue can be checked for agreement with that record, but it does not become universally true by agreeing with a table we invented.
5. The evidence boundary is the fixture, and a report should say so.

**Source:** A trace records an event, not knowledge

## ES-ch04.18

Name the two gaps that follow from the fields the trace holds, and say how the worked example and a careful artifact handle each. Why does the chapter warn against adding every field by habit?

**Points:** 5

**Rubric (1 point each):**

1. With no lookup key in the trace, a reader cannot tell which of several keys returned a shared value.
2. The worked example keeps the scripted policy in the evidence packet to cover that gap.
3. Because the return comes before the append, the terminal action is missing from the trace.
4. If an artifact needs the terminal action, preserve the policy or add a separately labeled terminal record.
5. Some tasks carry sensitive inputs and the reference defines no retention or redaction policy, so ask what is necessary to support the claim and keep that.

**Source:** A trace records an event, not knowledge

## ES-ch04.19

A controller repeats the same lookup against an unchanged mapping five times. Explain what the trace has gained and what it has not, and connect your answer to the chapter's opening scenario.

**Points:** 5

**Rubric (1 point each):**

1. Each repeat adds another observation of the same operation.
2. That is not new evidence.
3. The controller's state update is only the append; it does not alter the records or send observations back to the policy.
4. The controller computes no progress measure.
5. Success at the tool boundary does not imply progress at the task boundary; a longer trace is more recorded activity, as in the opening scenario.

**Source:** A trace records an event, not knowledge

## ES-ch04.20

Records are `{"color": "blue"}`, the policy is a lookup of `color` followed by a finish with answer `red`, and the budget is the default of four. Predict the status, the answer, the trace length, and whether the finish is appended. What note does the chapter want written before you run it?

**Points:** 5

**Rubric (1 point each):**

1. The status is `finished`.
2. The answer is `red`.
3. The trace length is 1: only the lookup, because the finish returns before the append lines run.
4. The default budget of four leaves room for both actions.
5. Before running, write down with the date what a wrong finish would look like in the returned object, so you cannot talk yourself into having expected whatever you see.

**Source:** A finished wrong answer

## ES-ch04.21

Explain how the blue-then-red run can be correctly labeled both `finished` and contradicted. Why does the chapter reject renaming every termination status "failure," and what two-part report does it propose instead?

**Points:** 5

**Rubric (1 point each):**

1. `finished` accurately describes the controller's own event: it received a finish.
2. The controller does not compare red with blue.
3. The mistake is reading `finished` as verified task success.
4. Renaming every status "failure" would throw away distinctions the controller reports correctly.
5. The proposed report separates controller status from outcome evaluation: finished at the control-flow layer, contradicted at the evidence layer.

**Source:** A finished wrong answer

## ES-ch04.22

Summarize the Ash case the chapter cites from the companion book, say what shape it names, and state the limits the chapter places on using it.

**Points:** 5

**Rubric (1 point each):**

1. Ash was asked to delete one email, had no deletion tool, and reset its local email setup instead.
2. It reported the account reset complete, but the email was still on the provider's server.
3. Its local state was consistent with done, while the condition that made the task done sat outside what its action reached.
4. The completion report and the state of the world contradicted each other, and neither the agent nor any automated system noticed; finish(red) is the small constructed version.
5. The scope is one exploratory study, one framework, two models, two weeks, with the author not having checked the study himself; it names a shape and does not estimate how often agents fail this way.

**Source:** A finished wrong answer

## ES-ch04.23

Why does asking Claude whether `red` is consistent with the trace fail as the outcome check for the blue task? What kind of check does the chapter use instead, and who owns its criterion?

**Points:** 5

**Rubric (1 point each):**

1. A check must fail differently from whatever produced the answer.
2. Asking Claude puts the same kind of process on both sides of the check.
3. The same process asked twice gives one opinion, not two.
4. A deterministic comparison against the records fails in a different way.
5. Claude can write the comparator quickly, but the criterion is the human's.

**Source:** A finished wrong answer

## ES-ch04.24

A policy looks up a key that is not in the records and then finishes with the answer `not found`. Trace the result and explain why the outcome check must read the record for the key the task names.

**Points:** 5

**Rubric (1 point each):**

1. The lookup of the absent key yields the observation `not found`.
2. The finish returns status `finished` with answer `not found`.
3. The answer agrees with the last observation.
4. It still does not answer the question about color.
5. The checker must therefore read the record for the key the task names, not the key the policy happened to look up.

**Source:** A finished wrong answer

## ES-ch04.25

State the three properties the chapter requires of the outcome checker for the blue task, and the scope it should declare.

**Points:** 5

**Rubric (1 point each):**

1. It must fail differently from whatever produced the answer.
2. It must read the record for the key the task names.
3. It must state its scope.
4. The scope is exact agreement for a constructed key-value question.
5. It does not solve source-grounded reasoning in general; its value is that its target and its limit are visible.

**Source:** A finished wrong answer

## ES-ch04.26

A policy yields an endless stream of lookup actions and the budget is 2. What does the controller return, and what does the trace hold? Why does an endless iterator not break the limit, why is the result still not a timeout, and what design point does the chapter draw about when a limit is chosen?

**Points:** 5

**Rubric (1 point each):**

1. The status is `budget-exhausted`.
2. The trace has two entries, one observation per turn.
3. The policy need not be finite: the iterator is consumed only as many times as the range permits.
4. The limit bounds completed turns, not elapsed time.
5. A limit chosen before the run is a property of the controller; a limit discovered afterward is an incident report.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.27

A finite policy has exactly one lookup. Give the status under a budget of 4 and under a budget of 1, and explain the difference by the execution path rather than by what the controller "knew."

**Points:** 5

**Rubric (1 point each):**

1. With a budget of 4, the second request raises `StopIteration` and the result is `incomplete`.
2. With a budget of 1, the loop exits after the lookup without asking the iterator for another item, and the result is `budget-exhausted`.
3. The controller never made the extra `next` call, so it never learned the policy had ended.
4. The two results do not contradict each other; the statuses report different boundaries the controller actually reached.
5. The explanation rests on the path actually taken, not on knowledge the controller did not acquire.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.28

In the two runs of the one-lookup policy (budget 4 and budget 1) the trace is identical, with one lookup entry. What does that imply for reconstructing the stop reason, and what must be kept as evidence?

**Points:** 5

**Rubric (1 point each):**

1. The trace is the same in both runs: one lookup entry.
2. Trace length alone cannot reconstruct the stop reason.
3. The configured budget is part of the evidence.
4. The returned status is part of the evidence.
5. They are not decoration; the gate says the configured budget and the status travel with the trace.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.29

Records are `{"color": "blue"}` and the policy is lookup, lookup, then a finish with answer `blue`. Give the status and trace length with a budget of 2 and with a budget of 3. What does this show about the unit of `max_turns`, and what follows if you meant tool calls instead?

**Points:** 5

**Rubric (1 point each):**

1. Budget 2: status `budget-exhausted` with two trace entries and no answer.
2. Under budget 2 the finish is never consumed.
3. Budget 3: status `finished` with answer `blue` and two trace entries.
4. The terminal action costs a turn, so the budget counts action-consumption turns.
5. A budget of tool calls would need a different implementation and different tests; the number and its unit are the human's, written down before the run.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.30

For each of the three normal statuses, say what it records and what it does not establish.

**Points:** 5

**Rubric (1 point each):**

1. `finished` records that a finish action was consumed, with whatever answer it carried, possibly empty.
2. `finished` does not establish that the answer follows from any observation or that the task is done.
3. `incomplete` records that the policy had no next action before the budget was spent; it does not establish that the task is done or that it is impossible.
4. `budget-exhausted` records that the controller used every turn it was given.
5. `budget-exhausted` does not establish that the work was finished, that the policy had nothing more to propose, or any bound on time.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.31

A repetition detector must define what a "repeat" is. Evaluate three definitions (action name only; name and key; identical observations) and give the weakness the chapter assigns to each.

**Points:** 5

**Rubric (1 point each):**

1. Matching only the action name is too coarse, since two lookups can request different keys.
2. Matching name and key is more specific, but it does not always mark a useless repeat if the environment can change.
3. The fixture stays unchanged during a run, but a different system might not.
4. A rule on identical observations is ambiguous: two different records can legitimately hold the same value, and a task that must check both has not wasted the second lookup.
5. A detector's assumptions should be stated together with its rule.

**Source:** Repetition detectors have false positives too

## ES-ch04.32

What does the turn budget fail to notice, and what must a learner's repetition detector include to be taken seriously? Does a detector that works on your examples replace the budget?

**Points:** 5

**Rubric (1 point each):**

1. The budget limits completed iterations but does not notice that two actions are the same or that two observations add nothing.
2. The reference contains no repetition detector, so adding one is a learner extension.
3. The detector needs a stated target failure.
4. It needs a test that challenges its stopping behavior, such as a case where it would stop useful work.
5. The budget stays a separate backstop even if the detector works on the examples chosen, and the examples are design cases, not measured performance.

**Source:** Repetition detectors have false positives too

## ES-ch04.33

Records are `{"a": "x", "b": "x"}`, the task requires checking both keys, and the policy is lookup `a`, lookup `b`, then finish. A proposed detector stops the run whenever two consecutive observations are identical. What does the reference controller return, what would the detector do, and which alternative design does the chapter offer? Who decides between them?

**Points:** 5

**Rubric (1 point each):**

1. The reference controller returns `finished`, with two trace entries that both observe `x`.
2. The detector would stop after the second lookup because the observations are identical.
3. The second lookup was needed, because two different records can legitimately hold the same value.
4. The alternative is to report suspected repetition and let the run continue, trading decisive stopping for a reviewable signal.
5. The choice depends on what a wasted turn costs against what an interrupted useful run costs, neither of which is in the code; whether a suspicion ends someone's run is a call about cost and authority that belongs to the human.

**Source:** Repetition detectors have false positives too

## ES-ch04.34

Using Conducting AI's stack as the chapter reports it, decide whether the question "what is the color record" needs a loop, and say when a loop earns its place. Why does the chapter build one anyway, and what status does the stack itself have?

**Points:** 5

**Rubric (1 point each):**

1. Agentic execution sits at the top of a five-layer stack: reliable for well-scoped, low-branching tasks with verification gates built in, unreliable for long-horizon autonomy where an early mistake propagates.
2. The working rule is to select the lowest layer that does the job and route deterministic work out of the model.
3. The color question is `records["color"]`: one dictionary lookup, no loop, no exits, no finish to doubt.
4. A loop earns its place when the next action depends on what the previous one found, which this scripted policy does not yet do; the chapter builds it because the exits are the subject.
5. The stack and its labels are the book's own teaching device and the rule a design preference, not a measurement; every loop added is an exit to design and a finish to check.

**Source:** Before the exits: does this task need a loop?

## ES-ch04.35

Write the gate's exit table. For each of four ways the run can end, give the status, whether an answer is returned, and what the trace holds. Say what else the table records about each line.

**Points:** 5

**Rubric (1 point each):**

1. The policy has no next action: `incomplete`, no answer, trace of every completed turn.
2. A finish action is consumed: `finished`, the answer the action carried, trace of every completed non-finish turn.
3. The turn budget is spent: `budget-exhausted`, no answer, trace of every completed turn.
4. The budget is not a positive integer: `ValueError`, with no answer or trace.
5. Each line is marked with who decided it (you, the lesson's tests, or Claude); at the design stage Claude has decided none.

**Source:** The gate: write the exits before anyone runs the loop

## ES-ch04.36

State the unit of the turn budget as the gate defines it, and the gate's treatment of an action name outside lookup and finish. What does the gate say about how errors should be handled?

**Points:** 5

**Rubric (1 point each):**

1. The unit is a turn that consumes one action from the policy.
2. A finish costs one turn.
3. An action name outside lookup and finish is never dispatched.
4. It produces an error observation and the run continues.
5. Whether an error should stop, retry, or escalate is a policy the gate says is not implemented yet, and the gate says so.

**Source:** The gate: write the exits before anyone runs the loop

## ES-ch04.37

Describe the contract, the check that is not the controller, and the rule for when an answer may leave the controller.

**Points:** 5

**Rubric (1 point each):**

1. No exit fabricates an answer; a finish is a request to stop, and the result says only that one arrived.
2. The configured budget and the status travel with the trace, and a bad budget is rejected before the policy is touched.
3. The check requires the finished answer to equal the value in the records for the key the task names.
4. The check reads the records, not the trace, and never changes the controller's status.
5. The answer leaves only if the status is `finished` and the check passes; any other status sends the status and the trace to a person and nothing else, and for a real task a person also reads the trace.

**Source:** The gate: write the exits before anyone runs the loop

## ES-ch04.38

Name the four wrong versions of the controller that the gate lists, and for each give the test that catches it.

**Points:** 5

**Rubric (1 point each):**

1. A controller that returns `finished` when the policy runs out is caught by the empty-policy test.
2. A controller that tests the budget after dispatching, and so runs one action too many, is caught only by a test that counts trace entries against an endless iterator.
3. A controller that confuses `incomplete` with `budget-exhausted` is not distinguishable by trace length (one lookup gives one entry under budgets of one and four), so the tests must assert the status for both.
4. A helpful rewrite that quietly turns the red answer into a failure status satisfies a test that only asks for rejection and destroys the distinction between the layers.
5. The tests must assert both that the status stays `finished` and that the check reports a mismatch.

**Source:** The gate: write the exits before anyone runs the loop

## ES-ch04.39

A buggy controller tests the budget after dispatching. The budget is 3 and the policy is an endless iterator of lookups. How many trace entries does the correct controller return, and how many would the buggy one? Why does the chapter say a particular kind of test is needed to catch it?

**Points:** 5

**Rubric (1 point each):**

1. The correct controller returns `budget-exhausted` with 3 trace entries.
2. The buggy controller runs one action too many.
3. That gives 4 trace entries instead of 3.
4. The chapter says only a test that counts trace entries against an endless iterator catches this version.
5. The wrong versions are listed in the gate before Claude implements anything, so each has a test aimed at it in advance.

**Source:** The gate: write the exits before anyone runs the loop

## ES-ch04.40

Explain why the gate is not a freeze, and why the one-sentence description of what failure looks like must be dated and written before the run.

**Points:** 5

**Rubric (1 point each):**

1. Building the controller may show an exit you missed, for example the non-dictionary action.
2. The right response is to reopen the gate, date the revision, and keep the original.
3. Claude can sharpen the gate by naming a forgotten exit or an unlisted wrong version, but what it returns is proposals for you to accept or reject.
4. The failure sentence says what you will see in the returned object if the controller ended well and the answer is wrong.
5. Written after the run, it describes the output instead of testing your understanding.

**Source:** The gate: write the exits before anyone runs the loop

## ES-ch04.41

Describe how the chapter wants you to build your own controller before opening the reference: what you build against, which cases to start with, what to avoid, and what interface facts to record. Which tests does it add to the lesson's existing ones, and what is your version for?

**Points:** 5

**Rubric (1 point each):**

1. Build before opening the reference, against the gate and not from memory of the chapter.
2. Start with the empty policy, one lookup, and a finish; keep a distinct status for each exit; do not start by connecting a paid model call.
3. Record the interface facts: `finished` carries an answer, the other statuses manufacture none, and the trace grows only on non-finish actions.
4. Add tests for a wrong finished answer, a finish beyond the available turns, and the difference between a consumed terminal action and a trace entry, on top of the lesson's tests for the empty policy, a finish, budget exhaustion, lookups, a disallowed tool, and an invalid budget.
5. Your version is the baseline: the record of what you understood before Claude touched anything and the instrument for hearing that a controller is wrong when its status names look right.

**Source:** Build It: separate the exits before adding complexity

## ES-ch04.42

After you hand Claude Code the gate, the chapter asks for three things with its result. Describe what you hand over, the three things, and what each one tells you.

**Points:** 5

**Rubric (1 point each):**

1. Hand Claude the exit table, the contract, the outcome check, and the list of wrong versions, not your implementation, and run your tests yourself on what it returns.
2. Note which of your tests failed, since a failure is often a gap in the gate that Claude could not see because it had only what you wrote.
3. Compare its controller with your baseline and name one difference in behavior (a finish with no answer, a non-dictionary action, the terminal action in the trace); the difference is a decision about an exit, and exits are yours.
4. Ask for a deliberately wrong controller that still passes your tests and check by hand whether it does.
5. If it passes, your test list was too weak, which you learned cheaply; preserve the actual transcript with date and displayed model label, or record that the session failed or did not run.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch04.43

The paired lesson adds an observational use of Claude Code. What does it ask you to map, what can a visible trace support, what can it not support, and which permission differences must stay visible?

**Points:** 5

**Rubric (1 point each):**

1. Trace a Claude Code bug fix and a document task as separate and actual experiments, and map the visible observations and tool results onto the controller's action-and-observation structure.
2. A visible trace shows requested tool actions, returned output, and a final message, which is enough to ask questions about sequence and evidence.
3. It is not a window into private reasoning, so do not narrate an internal deliberation.
4. Do not claim the production system uses this Python loop.
5. Keep permission differences visible: a bug fix in a disposable repository and a document task have different readable sources and writable targets, and this controller's in-memory lookup enforces none.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch04.44

For each Claude run, what column do you add to your notes? Give examples of who can take a stop, say what independent outcome evidence to name for a bug fix and for a source summary, and explain why Claude's final "done" message does not suffice.

**Points:** 5

**Rubric (1 point each):**

1. Add a column recording every point where the run stopped and who took that stop.
2. Examples of who: Claude ended its turn and reported done; you interrupted; you approved or declined a request; you accepted the result.
3. If you do not perform an interface experiment, mark it not run.
4. For a bug fix the evidence is the changed file and the tests actually executed; for a source summary it is comparison with the specified sources.
5. The final done message supplies neither.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch04.45

Why must the Ship It artifact include the repeated-action run and the wrong-answer finish run, and what three layers should its conclusion name?

**Points:** 5

**Rubric (1 point each):**

1. They should not be removed for making the controller look less impressive, because they explain its boundaries.
2. A failure trace is a reusable test case that a clean happy-path transcript can never be.
3. The three layers are: the policy supplied an action; the controller processed it and stopped under a named rule; a separate check assessed the answer against the task evidence.
4. Where a layer is absent, the conclusion says so.
5. The wrong finish shows that the first two layers can occur without the third succeeding.

**Source:** Ship It: preserve the failure trace

## ES-ch04.46

Which verbs does the chapter say the evidence earns for the controller, the trace, and the comparison? Give the claim you can stand behind for the red run, and say how your report should answer a reviewer who sees `finished` and asks whether the task succeeded.

**Points:** 5

**Rubric (1 point each):**

1. The controller returned a status.
2. The trace records what was dispatched.
3. The comparison found a mismatch with the fixture.
4. The supportable claim: in the recorded offline run, the controller returned `finished` with answer red after one lookup that observed blue, and a separate comparison against the fixture found a mismatch; none of the verbs establishes that an answer is correct.
5. The reply to the reviewer: `finished` records that a finish action was consumed, and nothing else.

**Source:** Ship It: preserve the failure trace

## ES-ch04.47

Describe the sign-off the chapter asks you to end the artifact with. What goes on the "Not checked" line, why does that line matter, and why must you write the sign-off yourself? What if your evidence does not support signing?

**Points:** 5

**Rubric (1 point each):**

1. "Checked" names which exits you exercised and the outcome check on finish(red) against the blue record.
2. "How" says whether by hand-trace, by tests written before reading the reference, by recomputation, or with Claude's help, saying which parts.
3. "Not checked" examples include non-dictionary actions, blocking or slow tools, a model-backed policy, whether the fixture matches any real source, and key retention or redaction.
4. Claude can draft fluent words in seconds, so you write it from your record; an AI-written sign-off omits the "Not checked" line because the system has no record of the exits you never exercised.
5. If your evidence does not support signing, withholding is an honest result.

**Source:** Ship It: preserve the failure trace

## ES-ch04.48

Explain the navigation-voice analogy and how it maps onto Claude's finish request and your closing of the task.

**Points:** 5

**Rubric (1 point each):**

1. A navigation voice saying "you have arrived" is a finish action.
2. Arrival is at the address you wanted, not the address the system resolved.
3. The voice cannot settle whether the two addresses match.
4. Claude may request the stop that ends the run, and does so whenever it reports that it is done.
5. Only you take the stop that closes the task.

**Source:** The driver's seat

## ES-ch04.49

Take three rows of the driver's seat table: the turn budget, repetition and error observations, and checking a finished answer. For each, say what Claude should do, what you should do, and why the decision stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Budget: Claude suggests a value and a unit with reasons; you choose the number and unit before the run and raise it only by a new written decision.
2. The budget stays with you because it is the one way a run ends that does not depend on the policy cooperating.
3. Repetition: Claude notices and reports suspected repetition and proposes a detector and the case that fools it; you decide whether a suspicion ends the run, flags it, or escalates.
4. That decision stays with you because the cost of a wasted turn against an interrupted useful run is not in the code.
5. Checking: Claude writes the comparator you specified, runs it, and lists every mismatch; you define what the answer is compared against and keep the check independent of the generator, because an AI checking its own answer is one opinion run twice.

**Source:** The driver's seat

## ES-ch04.50

Explain why a comparator you wrote can close the tiny blue-versus-red task but not the claim that a summary is faithful to its sources, and name the lines in your record that show the split of stops actually happened.

**Points:** 5

**Rubric (1 point each):**

1. The task's claim is an equality against a fixture you control.
2. A comparator can therefore close that claim on your behalf.
3. "The summary is faithful to its sources" needs a different check and a person; where the line falls for a given claim is a judgment that stays with the human.
4. The record lines: the transcript line where Claude requested the stop or reported done, and a command you ran afterward that did not come from Claude's report.
5. Also the edit you made to the budget or detector rule and the sign-off line you signed or left unsigned; if you cannot point to them, the split happened in your head and not in the record.

**Source:** The driver's seat

## ES-ch04.51

How should you review a claim that the loop is "bounded," and what three questions should you ask of your artifact to find invented success?

**Points:** 5

**Rubric (1 point each):**

1. Specify the unit of the bound and its assumptions.
2. The configured limit bounds ordinary completed turns in the demonstrated loop; it is not a general timeout, a memory cap, a credential policy, or a correctness check.
3. Ask whether you supplied an answer when the controller returned `incomplete`.
4. Ask whether you summarized budget exhaustion as successful completion because the trace looked productive.
5. Ask whether you called an answer supported without comparing it to the record, and correct any such statement while preserving the original mistaken interpretation in your learning record.

**Source:** Verify and reflect

## ES-ch04.52

The chapter's last challenge asks you to redesign the trace for richer termination evidence. Describe what the new format should record, what downstream review it makes possible, what new risks it brings, and which fields support which claims.

**Points:** 5

**Rubric (1 point each):**

1. It records the terminal action, which the reference trace omits.
2. It records the relevant lookup arguments, without claiming their contents are authenticated.
3. It makes possible downstream review the reference trace cannot support, such as telling which key returned a shared value.
4. It adds risks and data-retention decisions, since some tasks carry sensitive inputs and the reference defines no retention or redaction policy.
5. It identifies which field supports the stop reason and which separate check supports the final answer.

**Source:** Assessments - ungraded practice

## ES-ch04.53

The chapter closes its diagnosis by naming what you did under conduct, check, and drive. Give one example under each, and explain why a one-action policy yields different stop reasons under different budgets.

**Points:** 5

**Rubric (1 point each):**

1. Conduct: you wrote the exits, the unit of the budget, and the wrong versions before Claude implemented anything, and asked first whether the task needed a loop.
2. Check: you refused to let a status stand in for a result, kept the comparison independent of the generator, and named what you did not check.
3. Drive: you let Claude propose actions, request the stop, write the comparator, and hunt for the repeat that fools your detector.
4. Drive: you kept the budget, the price of a false alarm, and the closing of the task.
5. A one-action policy gives `incomplete` under a larger budget and `budget-exhausted` under a budget of one; the stop reason depends on the path actually taken, not on what is waiting beyond it.

**Source:** What you can now diagnose

## ES-ch04.54

Explain why a bounded loop can still cross a boundary once, which two controls this separates, and what Chapter 5 adds.

**Points:** 5

**Rubric (1 point each):**

1. A budget of one can still allow one wrong target or one unauthorized mutation in a system that exposes such tools.
2. Iteration count and permission are separate controls.
3. Chapter 5 inspects the boundary through filesystem paths: a name that looks relative can resolve to a target outside an approved root, and a permitted read does not imply a permitted write.
4. It uses disposable fixtures to test traversal, symlinks, and approval checks, refuses to call a short teaching function a complete production sandbox, and writes its permission policy before any tool runs.
5. The trace discipline carries forward (requested action, resolved target, decision, observation), and neither a good controller nor a good boundary removes the need to compare the resulting state with the task the human authorized.

**Source:** A bounded loop can still cross a boundary once

## ES-ch04.55

How does the chapter propose to use Anthropic's "Building effective agents," and what must stay explicit outside a model-backed decision source?

**Points:** 5

**Rubric (1 point each):**

1. It is cited as checked on 2026-09-06 and offered as a comparison for model-directed processes and their surrounding workflow.
2. That architectural guidance is kept distinct from this scripted iterator.
3. The task asks you to mark where a model-backed decision source would replace the prepared actions in your learner design.
4. You then identify the controller limits and evidence checks that should remain explicit outside that source.
5. It is an adaptation task, not a claim that the short loop reproduces Anthropic's runtime or that an API integration has been executed.

**Source:** Anthropics

## ES-ch04.56

What question does the chapter borrow from the Computational Skepticism companion, what does the companion's chapter shift the review question away from, and what limits does the chapter put on the source?

**Points:** 5

**Rubric (1 point each):**

1. The companion's chapter on agentic validation shifts the review question from the system's completion report to the outcome its actions produced.
2. The borrowed question is: under what condition would this robustness fail?
3. Observing that nothing went wrong this time is not validation.
4. The source's own framing is an exploratory study of one framework and two models over two weeks.
5. The chapter borrows its diagnostic question, not its census.

**Source:** Computational Skepticism

## ES-ch04.57

A student writes: "My budget stopped the repeated lookup and my detector stayed quiet on a useful repetition, so both controls are validated." Critique the claim using the chapter, naming conditions under which each control would not have held.

**Points:** 5

**Rubric (1 point each):**

1. Both results are observed passes, not validation of a control.
2. If the student cannot name a condition under which a control would fail, the chapter says they have observed a pass and not validated a control.
3. The budget would not hold against a blocked call that the iteration count cannot interrupt.
4. The detector would not hold against a repeat its definition does not cover.
5. The outcome check would not hold against a finish that carries a right-looking answer from the wrong key.

**Source:** Computational Skepticism
