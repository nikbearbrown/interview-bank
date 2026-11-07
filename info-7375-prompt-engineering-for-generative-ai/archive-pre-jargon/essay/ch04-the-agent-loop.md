# Chapter 4: The agent loop

## ES-ch04.1

An agent repeatedly calls the same lookup tool with identical arguments. Every call succeeds, every observation is logged, and the trace grows to dozens of entries, but the agent still has no answer it can support. Explain why this activity is not progress, state the question an outside reviewer should ask at each turn, and propose concrete measures that would reveal the lack of progress.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes success of a tool call from progress on the task: a call can succeed at the transport level while contributing nothing toward a supported answer.
2. States the reviewer's question: what changed that makes completion more justified than it was one turn ago.
3. Explains that repeating an identical request against an unchanged source returns the same content, so the longer trace is more recorded activity, not more evidence.
4. Proposes at least one concrete measure, such as counting new distinct evidence per turn or a detector that keys on request and observation together.
5. Recommends a hard turn budget as an independent backstop and a decision about what happens on suspicion (stop, flag or escalate).

**Source:** The agent loop (opening)

## ES-ch04.2

A team can stop a runaway agent in two ways: a cap on the number of turns fixed in the harness before the run, or an engineer noticing afterward that a run went on far too long. Argue why a limit chosen in advance belongs to the controller rather than to the model, and state what such a cap does and does not guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Says a limit chosen before the run is a property of the harness set by the operator, whereas a limit discovered afterward is an incident report.
2. Explains that the cap does not depend on the model's cooperation, so nothing the model emits can create more iterations.
3. States what it guarantees: the loop starts no more than the configured number of turns.
4. States that it does not guarantee a correct answer or that the work is complete.
5. States that it does not bound elapsed time or per-turn cost unless each turn is separately bounded.

**Source:** The agent loop (opening)

## ES-ch04.3

In an agent system three jobs are often blurred into one voice that says "done": proposing the next action, executing it and deciding whether the run continues, and judging whether the final result is any good. Name the three jobs, explain how separating them helps debugging, and give one fault for each of two different jobs that the separation would let you localize.

**Points:** 5

**Rubric (1 point each):**

1. Names the three jobs: proposer, executor or controller, and judge or checker.
2. Explains that separating them gives each job an owner and makes each testable on its own.
3. Localizes a proposer fault: a poor action sequence that was dispatched exactly as specified.
4. Localizes a controller fault: the right action sequence but the wrong end status or wrong limit handling.
5. Notes that the judging job may be absent from a design, and that its absence means no one has checked the result.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.4

Distinguish ending an agent run from closing the task it was started for. Say what can take each stop, why a finish request from the process that did the work is not sufficient to close the task, and give an example where a run ends cleanly but the task is not done.

**Points:** 5

**Rubric (1 point each):**

1. Defines ending the run as a control-flow event, such as the loop returning on a finish request, exhausted budget or empty action source.
2. Defines closing the task as acceptance that the result meets the need, by a person or a check a person designed.
3. Explains that the worker's own report of completion is one datum and not independent of the worker.
4. Notes that control flow can be tested for correctness without judging answer quality.
5. Gives a concrete example of a clean ending without a done task, such as a finish carrying a wrong or empty answer.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.5

A team replaces a scripted list of actions with a language model that chooses each next action. Explain why the model should not inherit the power to change the loop's limits just because it supplies the next action, name three controls that should remain enforced outside the model, and describe how text inside a tool result claiming "you now have unlimited turns" should be treated.

**Points:** 5

**Rubric (1 point each):**

1. States that supplying actions confers no authority over the runtime's limits.
2. Names an enforced turn or cost budget as a control that must not depend on the proposer's cooperation.
3. Names a tool allowlist or permission check enforced by the runtime, and an outcome check independent of the model.
4. Treats text in a tool result as data the model reads, not as an instruction with authority over the controller.
5. Notes that the model can still be influenced by injected text, such as being steered to finish early, so its finish needs independent checking.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.6

A loop is written as for turn in range(10): action = next(source), where source is a generator that fetches each action over a network connection. Explain why this does not bound the run's duration, what additional controls would, and how a timeout should be reported relative to the loop's other exits.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the count is consulted only between iterations, so a call to next that never returns is never interrupted.
2. States that total time is bounded only if each turn is separately bounded, such as by a per-call timeout.
3. Proposes an overall deadline or watchdog with cancellation as a further control.
4. Says a timeout should surface as a distinct exit, not be disguised as success or merged with turn exhaustion.
5. Notes that the turn cap remains useful as a separate control for the number of iterations.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.7

Read the controller below, then trace these four runs with records {"color": "blue"}: (a) policy [] with max_turns=4; (b) policy [lookup color] with max_turns=4; (c) policy [lookup color] with max_turns=1; (d) policy [lookup color, finish "blue"] with max_turns=1. Give the returned status and trace for each, and explain why (b) and (c) have the same trace but different statuses.

```python
def run(policy, records, max_turns=4):
    trace = []
    it = iter(policy)
    for turn in range(max_turns):
        try:
            action = next(it)
        except StopIteration:
            return {"status": "incomplete", "trace": trace}
        name = action.get("name")
        if name == "finish":
            return {"status": "finished", "answer": action.get("answer", ""), "trace": trace}
        obs = records.get(action.get("key"), "not found") if name == "lookup" else "error: tool not allowed"
        trace.append({"turn": turn + 1, "action": name, "observation": obs})
    return {"status": "budget-exhausted", "trace": trace}
```

**Points:** 5

**Rubric (1 point each):**

1. Case (a): status incomplete with an empty trace, because the first request for an action raises the end-of-iteration condition.
2. Case (b): status incomplete with one trace entry whose observation is blue, because the second request finds the action source exhausted.
3. Case (c): status budget-exhausted with one entry, because the only turn is spent on the lookup and the loop never asks for another action.
4. Case (d): status budget-exhausted with one entry, because the finish would need a second turn that the budget does not allow.
5. Explains that the stop reason depends on which boundary is reached first by the execution path, so trace length alone cannot recover it and the budget and status are part of the evidence.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.8

Read the controller below. List at least four behaviors it leaves undecided or surprising and say what a specification written beforehand should have decided about each.

```python
def run(policy, records, max_turns=4):
    trace = []
    it = iter(policy)
    for turn in range(max_turns):
        try:
            action = next(it)
        except StopIteration:
            return {"status": "incomplete", "trace": trace}
        name = action.get("name")
        if name == "finish":
            return {"status": "finished", "answer": action.get("answer", ""), "trace": trace}
        obs = records.get(action.get("key"), "not found") if name == "lookup" else "error: tool not allowed"
        trace.append({"turn": turn + 1, "action": name, "observation": obs})
    return {"status": "budget-exhausted", "trace": trace}
```

**Points:** 5

**Rubric (1 point each):**

1. Identifies that a finish action with no answer field returns finished with an empty string, and says the specification should decide whether that is acceptable.
2. Identifies that a non-dictionary action raises AttributeError outside the three normal statuses, and says the specification should define the outcome for malformed input.
3. Identifies that an unknown action name consumes a turn and the loop continues, and that stopping, retrying and escalating are different policies to be chosen deliberately.
4. Identifies that the trace omits the lookup key and the finish action, which limits what claims it can support.
5. Notes that nothing compares an answer with any observation, so the finished status cannot certify correctness, and that a separate check must be specified.

**Source:** Every return statement is an exit someone decided

## ES-ch04.9

Two implementations of a turn budget exist. One pulls an action at the start of each iteration of a bounded loop. The other dispatches an action first and increments a counter afterward, stopping only when the counter exceeds the budget. Explain the defect in the second design, then describe a test that would catch it and why a test built on a short finite policy would miss it.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the off-by-one: checking after dispatch lets the controller run one action more than the budget allows.
2. Explains the consequence, such as an extra tool call with possible side effects beyond the configured limit.
3. Describes the catching test: an endless action source with budget n, asserting that exactly n actions were dispatched or n trace entries exist.
4. Explains that a finite policy shorter than the budget ends by running out of actions before the budget check matters.
5. States that the budget must be the thing that stops the loop in the test for the test to exercise the budget.

**Source:** Every return statement is an exit someone decided

## ES-ch04.10

An agent harness lets the model request up to five tool calls in parallel on each turn, and one of the available tools sends an email. Discuss what the unit of the budget should be (turns, tool calls, tokens, money or seconds), choose a unit or combination for this harness, and explain how you would test the chosen limit.

**Points:** 5

**Rubric (1 point each):**

1. Observes that turn counts and tool-call counts diverge when several calls run per turn, so the unit must be stated.
2. Matches the unit to the risk: side-effecting calls such as email argue for counting tool calls, possibly with a separate limit on sensitive tools.
3. Notes that tokens or money bound cost, and seconds bound latency, and that turns bound neither exactly.
4. Recommends combining limits where several resources matter rather than relying on a single number.
5. Describes a test that supplies an action source exceeding the limit and asserts the exact count of dispatched calls and the reported stop reason.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.11

An agent loop sends the full conversation to the model on every turn without caching. The instructions and task take 1,200 input tokens, and each turn adds 300 tokens of action and observation, so the call on turn k reads 1,200 + 300 x (k - 1) input tokens. Compute the total input tokens for a run of 10 turns and for a run of 20 turns, compare the two, and explain what this implies for choosing a limit and for reducing cost.

**Points:** 5

**Rubric (1 point each):**

1. Computes the 10-turn total as 25,500 input tokens.
2. Computes the 20-turn total as 81,000 input tokens.
3. Notes the ratio of about 3.2 for doubling the turns, and explains that cost grows faster than linearly because history is re-read on every call.
4. Concludes that a limit on turns understates cost for long runs, so a token or cost budget is a more direct control.
5. Names a mitigation such as prompt caching of the repeated prefix, summarizing or truncating history, or ending runs earlier.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.12

You must keep a trace of each agent run so that a reviewer can later judge a claim like "the run ended because the budget was spent after the agent looked up two keys." State what the trace and the surrounding record must contain to support such a claim, what is easy to omit by accident, and how you would handle fields that contain sensitive data.

**Points:** 5

**Rubric (1 point each):**

1. Lists per-turn fields: turn number, action name, action arguments such as the lookup key, and the observation.
2. Includes the stop reason and the configured budget with its unit, because the trace alone cannot reconstruct why the run stopped.
3. Flags commonly omitted items: the terminal action, the arguments, and the version of the action source or policy.
4. Argues that retention should follow what is necessary to support the claim, not habit, and addresses sensitive data with redaction, hashing or retention limits.
5. Notes the cost of redaction on reproducibility, and that observations in the trace are evidence about operations, not about the model's reasoning.

**Source:** A trace records an event, not knowledge

## ES-ch04.13

Two lookups against a key-value store both return the value "blue", but the trace stores only the turn number, the action name and the observation. Explain what a reviewer cannot determine from this trace, what the second identical observation does and does not mean, and how the trace or record should be changed.

**Points:** 5

**Rubric (1 point each):**

1. States that without the key the reviewer cannot tell which key produced which observation.
2. Explains that two identical observations can come from two different required checks, so the second lookup is not necessarily wasted.
3. Explains that repeating the same lookup against an unchanged source adds another observation of the same fact, not independent evidence.
4. Proposes recording the arguments in the trace or keeping the action list alongside it.
5. Notes that adding fields should be driven by what claims need supporting, with attention to sensitive inputs.

**Source:** A trace records an event, not knowledge

## ES-ch04.14

Records are {"color": "blue"}. An agent looks up color, observes blue, and then finishes with the answer "red"; the controller returns status finished. Explain what the status means, why the controller did not catch the contradiction, and how a report should describe the run so that downstream readers are not misled.

**Points:** 5

**Rubric (1 point each):**

1. Explains that finished records that a finish action was received, which accurately describes the controller's event.
2. Explains that the controller performs no comparison between the answer and any observation, so the contradiction is invisible to it.
3. Identifies the misreading to avoid: treating finished as verified task success.
4. Recommends a separate outcome check against the records, kept independent of the controller's status.
5. Describes two-layer reporting: finished at the control-flow layer and contradicted at the evidence layer.

**Source:** A finished wrong answer

## ES-ch04.15

You are asked to build an outcome checker for a task whose answer is the value stored under a named key in a small table. Describe three properties the checker needs so that it is a useful independent check rather than a repeat of the generator, and say what claim it can and cannot support.

**Points:** 5

**Rubric (1 point each):**

1. Property one: it must fail differently from whatever produced the answer, such as a deterministic comparison rather than asking the same model.
2. Explains that the same process on both sides of a check gives one opinion twice rather than two confirmations.
3. Property two: it must read the value for the key the task names, not the key the agent happened to look up.
4. Property three: it must state its scope, such as exact agreement for a key-value question with its normalization rules.
5. States the limit: it supports agreement with the table, not truth about the world and not faithfulness of open-ended text.

**Source:** A finished wrong answer

## ES-ch04.16

An agent asked to delete one email from a mailbox hosted on a provider's server has no deletion tool. It resets its local mail client settings instead and reports "done". The message remains on the server. Explain the failure in terms of the gap between a completion report and the state of the world, design an independent verification, and say what this one scenario does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that the agent's local state was consistent with its report while the condition that made the task done lies outside what its actions reached.
2. Explains that the completion report and the actual state contradict each other and the final message alone gives no sign of it.
3. Designs an independent check against the real target, such as querying the provider's server for the message.
4. Says the check should not rely on the agent's own account and should be defined from the task's requirement.
5. States that a single scenario illustrates a failure shape but gives no information about how often agents fail this way.

**Source:** A finished wrong answer

## ES-ch04.17

A coding agent reports that all tests pass and the bug is fixed. Describe how a careful reviewer would independently verify the claim, what evidence the final message does and does not supply, and how the agent could produce a passing result without fixing the bug.

**Points:** 5

**Rubric (1 point each):**

1. Says the final message is a claim about evidence, not the evidence itself.
2. Recommends re-running the test suite in a clean environment rather than trusting the reported run.
3. Recommends inspecting the diff to see which files changed, including whether tests were modified or deleted.
4. Explains ways to pass without fixing: weakening or skipping tests, special-casing the test inputs, or tests that never exercised the bug.
5. Suggests adding or confirming a test that fails before the change and passes after it.

**Source:** A finished wrong answer

## ES-ch04.18

A team proposes to verify an agent's finished answer by asking the same model, in the same configuration, whether the answer is consistent with the retrieved evidence. Evaluate this check: explain what is weak about it, when it is still useful, and what you would use for a claim that can be checked deterministically.

**Points:** 5

**Rubric (1 point each):**

1. Explains that generator and checker share the same kind of process and likely the same blind spots, so their errors are correlated.
2. Notes that agreement between them is closer to one opinion asked twice than to independent confirmation.
3. Says such a check can still be useful as a triage or screening signal.
4. Recommends a deterministic comparison where the claim is an exact value, because it fails differently from the generator.
5. Notes that a person or independent evidence is needed for claims that no cheap deterministic check can cover.

**Source:** A finished wrong answer

## ES-ch04.19

A user asks for the color value. An agent looks up a misspelled key "colour", gets the observation "not found" from the lookup tool, and finishes with the answer "not found". A checker compares the final answer with the agent's last observation and passes it. Explain why the check passes, why that is a flaw, and how to redesign the checker and the lookup tool's return value.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the answer agrees with the last observation because both are the not-found string.
2. Explains that the check measures consistency with the agent's own action, not whether the task's question was answered.
3. Says the checker should read the record for the key the task names rather than the key the agent used.
4. Says a missing value is an absence of evidence and should not be accepted as a final answer.
5. Proposes returning a structured result or error for a missing key so that a stored value equal to the sentinel string is not confused with absence.

**Source:** A finished wrong answer

## ES-ch04.20

A team checks finished answers by exact string equality against a stored value. List two kinds of claim this check can close and two it cannot, and discuss how normalization choices such as case and whitespace affect what the check certifies.

**Points:** 5

**Rubric (1 point each):**

1. Names a claim it can close, such as the answer equals the stored value for the named key.
2. Names a second closable claim of the same exact-value kind, such as a numeric identifier matching a record.
3. Names claims it cannot close, such as faithfulness of a summary to its sources.
4. Names a second unclosable claim, such as correctness of an open-ended explanation or whether the stored value is itself right.
5. Explains that normalization rules change what counts as a match, so they belong in the check's stated scope.

**Source:** A finished wrong answer

## ES-ch04.21

A run ends with status finished but its answer contradicts the evidence. A colleague suggests renaming every status other than verified success to "failure". Explain why this is a poor fix, what information it destroys, and propose a reporting design that keeps the useful distinctions.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the controller reports control-flow events correctly, and that relabeling them confuses what each status denotes.
2. Says merging finished-but-contradicted, incomplete and budget-exhausted into one label loses distinct causes and distinct remedies.
3. Proposes separate fields for control-flow status and for the outcome-check result.
4. Gives an example combination, such as finished with mismatch found, that a single label cannot express.
5. Notes tests should assert both layers so a fix that quietly rewrites the status is caught.

**Source:** A finished wrong answer

## ES-ch04.22

Design a repetition detector for an agent loop. Compare three definitions of a repeat: same tool name, same name and arguments, and same observation. For each definition give a legitimate scenario that would be wrongly stopped, and state what else the design needs besides the detector.

**Points:** 5

**Rubric (1 point each):**

1. Name-only matching: gives a scenario where different arguments make the calls legitimately different, such as looking up several different keys.
2. Name and arguments: gives a scenario where the environment changes between calls, such as polling a job status.
3. Observation-only: gives a scenario where different sources legitimately hold equal values and both must be checked.
4. States that each rule's assumptions and target failure must be stated with the rule.
5. Says a hard turn budget remains a separate backstop and the detector should be tested with cases built to fool it.

**Source:** Repetition detectors have false positives too

## ES-ch04.23

When a repetition detector suspects a loop, the system could stop the run or could flag it for review and continue. Argue for each choice in a different deployment, say what information is needed to decide between them, and who should decide.

**Points:** 5

**Rubric (1 point each):**

1. Describes the stop option as decisive and cheap to reason about but at risk of interrupting a useful run.
2. Describes the flag option as preserving the run and creating a reviewable signal at the cost of continued spend and the need for a reader.
3. Gives a deployment where stopping is right, such as a costly or side-effecting tool where a wasted turn is expensive.
4. Gives a deployment where flagging is right, such as long investigations where interruption destroys valuable work.
5. Says the decision depends on the relative cost of a wasted turn and an interrupted run, which is not in the detector's code, so a responsible person decides.

**Source:** Repetition detectors have false positives too

## ES-ch04.24

A detector stops an agent when the last two actions are identical. An agent alternates read(a.txt), edit(a.txt), read(a.txt), edit(a.txt) indefinitely. Explain why the detector fails, propose a better rule using a window of recent actions, and describe a case where your improved rule would stop useful work.

**Points:** 5

**Rubric (1 point each):**

1. Explains that alternation never produces two identical consecutive actions, so the narrow rule never fires.
2. Proposes a rule over a window, such as a pair occurring several times within the last few actions, or detection of a repeating subsequence.
3. Describes a legitimate case the new rule would wrongly stop, such as an edit-test-fix cycle that is making real progress between repeats.
4. Notes that a definition of repeat decides which loops the rule can catch, and that it should state its target failure.
5. Keeps a turn budget as a separate backstop for patterns the detector does not define as repeats.

**Source:** Repetition detectors have false positives too

## ES-ch04.25

An agent must wait for a long-running batch job by repeatedly calling a status tool with the same arguments. A repetition detector based on identical consecutive calls is stopping it. Explain why the detector misfires and design a polling policy that keeps the loop safe.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the environment changes between calls, so identical requests can legitimately return different results.
2. Proposes including observed state in the repeat definition so a changing status is not a repeat.
3. Proposes spacing polls with a delay or backoff so the loop does not consume turns rapidly.
4. Proposes a maximum number of polls or a deadline as a separate bound on waiting.
5. Says what the loop should report if the deadline passes, rather than guessing at completion.

**Source:** Repetition detectors have false positives too

## ES-ch04.26

Decide whether each of these tasks should be built as an agent loop: (a) convert a price to another currency using a fixed rate table; (b) investigate and resolve varied customer-support tickets whose causes are not known in advance; (c) produce a nightly report from the same four database queries. Justify each decision and state what a loop adds to the system's burden.

**Points:** 5

**Rubric (1 point each):**

1. Task (a): argues for plain code, since it is a single deterministic lookup with no need for a loop or model-directed control.
2. Task (b): argues a loop is plausible because each next step depends on what the previous step found.
3. Task (c): argues for a fixed workflow, since the steps are known in advance and do not depend on intermediate results.
4. States the principle of choosing the simplest design that does the job and routing deterministic work out of the model.
5. Notes that every loop adds exits to design and finishes to verify, so it adds a testing and checking burden.

**Source:** Before the exits: does this task need a loop?

## ES-ch04.27

Explain why autonomous agent loops are generally considered less reliable on long-horizon tasks than on well-scoped, low-branching tasks, and what design features make long runs safer. Include a calculation: if each step is independently correct with probability 0.95, what is the probability that a 10-step chain and a 20-step chain are both entirely correct?

**Points:** 5

**Rubric (1 point each):**

1. Computes about 0.60 for ten independent steps at 0.95 each.
2. Computes about 0.36 for twenty steps.
3. Notes that the calculation assumes independence, and that in practice early errors can propagate to dependent steps.
4. Explains that error compounds with length, so long unverified chains degrade.
5. Names mitigations such as verification checkpoints inside the run, narrower scope, and keeping deterministic work out of the model.

**Source:** Before the exits: does this task need a loop?

## ES-ch04.28

Describe the difference between a workflow and an agent in LLM systems, say when each is appropriate, and list the tradeoffs and safeguards that come with giving a model control of its own steps.

**Points:** 5

**Rubric (1 point each):**

1. Defines a workflow as LLMs and tools orchestrated through predefined code paths.
2. Defines an agent as a system in which the model dynamically directs its own process and tool use.
3. Recommends starting with the simplest solution and adding autonomy only when it demonstrably helps.
4. Names tradeoffs: higher latency and cost, less predictability, and errors that can compound across steps.
5. Names safeguards: sandboxed testing, guardrails, explicit stopping conditions or limits, and human checkpoints.

**Source:** Anthropics

## ES-ch04.29

An agent harness permits two actions, lookup and finish. The model requests an action named shell. Compare four policies: return an error observation and continue, stop the run, retry with corrective feedback, and escalate to a person. Say which you would choose for an agent handling money transfers, and what the choice does not establish about the system's overall permissions.

**Points:** 5

**Rubric (1 point each):**

1. Describes error-and-continue: low friction but consumes a turn and lets the model repeat the request.
2. Describes stop: simple and safe but ends possibly recoverable work.
3. Describes retry-with-feedback and escalate with their tradeoffs, such as more turns for the first and human latency for the second.
4. Chooses a policy for money transfers with a reason, such as stopping or escalating because a request for an unlisted tool signals unexpected behavior.
5. Notes the allowlist check guards only this function and does not establish permissions for the wider runtime.

**Source:** Every return statement is an exit someone decided

## ES-ch04.30

A tool that sends payments times out, and the harness retries it automatically up to three times. Explain the risk, how idempotency keys help, how to decide which errors to retry, and how retries should interact with the loop's budget.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a timeout does not reveal whether the original call succeeded, so a retry can duplicate a side effect.
2. Explains that an idempotency key lets the service recognize repeated requests and return the original result.
3. Distinguishes transient errors, which may merit retry, from permanent errors, which do not.
4. Says retries should be bounded and should count against some limit because they consume calls, time and cost.
5. Suggests an approval step or escalation for ambiguous outcomes of irreversible actions.

**Source:** Every return statement is an exit someone decided

## ES-ch04.31

A controller assumes each action is a dictionary with a name field, but its action source sometimes yields malformed values such as a bare string. Describe how to handle malformed actions: what the controller should do, how the outcome should be reported, and how you would test the new behavior.

**Points:** 5

**Rubric (1 point each):**

1. Explains that unvalidated malformed input raises an exception outside the controller's defined outcomes.
2. Proposes validating the shape and types of each action before dispatch.
3. Defines an explicit outcome for invalid actions, such as an error observation or a distinct status, and notes it is a new exit to specify.
4. Says silent catching hides the problem and loses a turn without a record.
5. Describes tests with malformed inputs asserting the defined outcome and that the loop still honors its budget.

**Source:** Every return statement is an exit someone decided

## ES-ch04.32

A loop uses the Claude Messages API. After each response it inspects stop_reason: tool_use means run the requested tools and send results back; end_turn means stop; max_tokens means the output hit its limit. Explain how each should be handled, why end_turn is not a verification, and what additional limit the loop needs.

**Points:** 5

**Rubric (1 point each):**

1. For tool_use: execute the requested tools and return a matching tool_result for each request in the next message.
2. For end_turn: treat it as the model finishing its turn, which is a stop request, not proof that the task is done.
3. For max_tokens: recognize truncation, and do not treat the partial text as a complete answer; continue, raise the limit or report incomplete.
4. Explains that an outcome check independent of the model is needed before accepting the final answer.
5. Says the loop needs its own cap on iterations, since nothing else prevents continued tool requests.

**Source:** Anthropics

## ES-ch04.33

Before asking an AI coding assistant to implement a loop controller, an engineer must write a specification. List what it should contain, say what each element protects against, and explain why it must be written before the implementation exists.

**Points:** 5

**Rubric (1 point each):**

1. Includes a table of every exit with its status, whether an answer is returned, and what the trace holds.
2. Includes the unit of the budget and how invalid budgets are handled.
3. Includes what must never be fabricated, such as an answer when the run is incomplete or exhausted.
4. Includes a separate outcome check and a rule for when an answer may move on, plus a list of wrong implementations the tests must catch.
5. Explains that writing it first gives criteria independent of the code, so the code's choices cannot silently define correctness.

**Source:** Write the exits before anyone runs the loop

## ES-ch04.34

Four defective controllers are described: (1) returns finished when the action source runs out; (2) checks the budget after dispatching and so runs one action too many; (3) returns incomplete where it should return budget-exhausted, and the reverse; (4) rewrites a wrong finished answer into a failure status. Design a test for each that would fail on the defect, and say what each test must assert.

**Points:** 5

**Rubric (1 point each):**

1. Test for (1): empty action source, asserting status is incomplete and not finished.
2. Test for (2): endless action source with budget n, asserting exactly n dispatches or trace entries.
3. Test for (3): one-lookup policy under budgets of 1 and 4, asserting the status in both because trace length is identical.
4. Test for (4): a finish with a wrong answer, asserting the control-flow status remains finished and the separate check reports a mismatch.
5. Notes that a test must be able to fail on the defect, and that passing tests show only that listed defects are absent.

**Source:** Write the exits before anyone runs the loop

## ES-ch04.35

While implementing a controller from a written specification, an engineer discovers an exit the specification did not cover. Describe the right response, what to ask an AI assistant to do and not to do, and why the original specification should be kept.

**Points:** 5

**Rubric (1 point each):**

1. Says to reopen the specification rather than silently letting the code decide the new exit.
2. Says to date the revision and keep the original so the history of understanding is preserved.
3. Says the assistant can help by proposing missed exits or wrong versions, which the engineer accepts or rejects.
4. Says the assistant should not be left to decide exit behavior implicitly, because exits are owned by the engineer.
5. Says new tests should be added for the new exit and run against the implementation.

**Source:** Write the exits before anyone runs the loop

## ES-ch04.36

Before running a small experiment on a controller, a student writes a prediction of its result and builds their own version before reading a reference solution. Explain what each practice protects against, particularly when an AI assistant is also available, and what the student does when prediction and result disagree.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a prediction written before the run reveals misunderstandings, whereas one written afterward merely describes the output.
2. Notes that hindsight bias leads people to believe they expected whatever they saw.
3. Explains that a self-built baseline gives something to compare an AI-generated version against.
4. Explains that without having built it, the student cannot tell when generated code is wrong even if its names look right.
5. Says a disagreement is treated as information about the student's mental model and recorded with the line of code or fact that changed their view.

**Source:** Build It: separate the exits before adding complexity

## ES-ch04.37

You hand an AI assistant a written specification and tests for a loop controller and receive an implementation. Describe what you should do before accepting it: how to run the checks, how to compare it with your own baseline, and what to do with any behavioral differences.

**Points:** 5

**Rubric (1 point each):**

1. Says to run the tests yourself rather than relying on the assistant's report that they pass.
2. Says to note which of your own tests failed, since a failure may reveal a specification gap.
3. Says to compare against your baseline and name at least one behavioral difference at a boundary such as an empty finish or a malformed action.
4. Says each difference is a decision about an exit that the human owner must surface, accept or reject.
5. Says to ask for a deliberately wrong version that passes the tests, and strengthen the tests if one exists.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch04.38

An engineer asks an AI assistant for a controller that is deliberately wrong yet passes their test suite. Explain the purpose of the exercise, how to interpret the result in both cases, and how it relates to coverage and to mutation testing.

**Points:** 5

**Rubric (1 point each):**

1. Explains the purpose: measuring whether the tests can detect known-wrong behavior.
2. If a wrong controller passes, concludes the test suite is too weak and identifies what assertion was missing.
3. If the assistant cannot produce one, notes this does not prove the suite is strong, since the assistant may simply have failed to find the gap.
4. Relates it to mutation testing, where deliberate faults probe whether tests notice them.
5. Distinguishes line coverage, which shows code executed, from assertion strength, which determines whether faults are noticed.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch04.39

A team has a trace of an agent run that went wrong: a repeated lookup and a wrong finished answer. Explain why they should preserve these runs rather than report only clean ones, what a preserved failure trace should contain to be reusable, and how the conclusion should describe the layers involved.

**Points:** 5

**Rubric (1 point each):**

1. Explains that failure traces explain a system's boundaries and a clean transcript cannot serve as a test of them.
2. Says a failure trace becomes a reusable regression test case.
3. Lists contents: action source or script, data used, budget and unit, returned object including status, and the outcome-check result.
4. Says the conclusion should name the layers: action proposal, controller processing with a named stop rule, and a separate outcome check.
5. Says to state where a layer is absent, and that the first two layers can occur without the third succeeding.

**Source:** Ship It: preserve the failure trace

## ES-ch04.40

A write-up of an agent experiment contains these sentences: (1) "The agent succeeded." (2) "The controller verified the answer." (3) "The agent chose red because it distrusted the lookup result." The underlying evidence is a returned object with status finished, an answer of red, a trace showing one lookup that observed blue, and a separate comparison that found a mismatch with the record. Rewrite each sentence so that it claims only what the evidence supports, and explain the principle behind the rewrites.

**Points:** 5

**Rubric (1 point each):**

1. Rewrites (1) to something like: the controller returned finished with the answer red after one lookup that observed blue.
2. Adds that a separate comparison found a mismatch with the record, so the answer is contradicted.
3. Explains that (2) is unsupported because the controller performed no comparison, and rewrites it to say what the controller did record.
4. Explains that (3) attributes a motive that a trace of actions and observations cannot show, and rewrites it in terms of observed actions.
5. States the principle: choose verbs the evidence earns, such as returned, recorded and found, and avoid verbs that claim correctness or intent without evidence.

**Source:** Ship It: preserve the failure trace

## ES-ch04.41

You are drafting a sign-off for a write-up of an agent-trace experiment. Describe what the sign-off should contain, why a line stating what was not checked matters especially when an AI assistant helped draft the write-up, and when withholding the signature is the right outcome.

**Points:** 5

**Rubric (1 point each):**

1. Lists elements: what was checked, how it was checked, what was not checked, what is not being claimed, and a signature or withholding with name and date.
2. Says the checked line should name the specific exits and checks actually exercised.
3. Says the how line should state which parts were done by hand and which with AI help.
4. Explains that an AI draft tends to omit the not-checked line because it has no record of what the human never exercised.
5. Says withholding is the honest result when evidence does not support the claim, because a signature asserts accountability.

**Source:** Ship It: preserve the failure trace

## ES-ch04.42

A navigation app announces "you have arrived" at the address it resolved from a typed query. Use this scenario to explain the difference between a system reporting that it has finished and the intended goal being met. Then apply the analogy to an agent that books a flight and reports "booked".

**Points:** 5

**Rubric (1 point each):**

1. Explains that the announcement reports that the app's own process ended at the address it resolved, not that the traveler is at the intended place.
2. Explains that the app cannot settle whether the resolved address matches the intended one.
3. Maps the analogy: an agent's done is a termination message from the same process that did the work.
4. For the flight booking, names independent evidence such as a confirmation record from the airline for the right passenger, date and route.
5. Says someone must compare the evidence against the original intent before the task counts as complete.

**Source:** The driver's seat

## ES-ch04.43

In an AI-assisted agent loop, five things need owners: proposing actions and requesting a finish, choosing the turn budget, deciding what a suspected repetition triggers, checking a finished answer, and closing the task. For each, say what the AI assistant should do, what the human should decide, and why the decision stays with that party.

**Points:** 5

**Rubric (1 point each):**

1. Proposing and finishing: the AI proposes actions and may request finish, while the human treats the request as a stop of the run only, since the worker's report is one datum.
2. Budget: the AI may suggest a value and unit with reasons, while the human chooses it before the run, because it is the control that does not depend on cooperation.
3. Repetition: the AI notices and reports suspected repetition and proposes detectors, while the human decides stop, flag or escalate, because the relevant costs are not in the code.
4. Checking: the AI writes and runs the specified comparator, while the human defines what is compared against and keeps it independent, because an AI checking its own answer is one opinion twice.
5. Closing: the AI drafts the trace and report, while the human accepts, narrows or withholds and signs, because accountability for acceptance cannot be delegated.

**Source:** The driver's seat

## ES-ch04.44

A team says that in their AI-assisted project the assistant requested the stop and a human closed the task. As a reviewer, what concrete records would you ask for to confirm that this division actually happened, and why is a statement that the team was careful not sufficient?

**Points:** 5

**Rubric (1 point each):**

1. Asks for the transcript line where the assistant reported it was done.
2. Asks for a command or check the human ran afterward whose result did not come from the assistant's report.
3. Asks for human edits to controls, such as a change to the budget or the repetition rule.
4. Asks for the sign-off line that was signed or deliberately left unsigned.
5. Explains that without such records the split happened only in people's heads, and an assertion of care is not a record of any action.

**Source:** The driver's seat

## ES-ch04.45

A write-up claims that an agent loop is bounded. State what a precise boundedness claim should specify, what it should explicitly not claim, and give an example of a sentence you could defend for a loop that uses a fixed turn budget.

**Points:** 5

**Rubric (1 point each):**

1. Says the claim must specify the unit being bounded, such as turns, tool calls, tokens or money.
2. Says it must state its assumptions, such as that each iteration completes.
3. Says it should not claim to be a timeout, a memory cap, a permission policy or a correctness check.
4. Notes that a hung tool call or slow action source defeats a turn-based bound on elapsed time.
5. Provides a defensible sentence, such as: the loop starts no more than N turns, assuming each iteration completes, and this does not bound time or establish correctness.

**Source:** Verify and reflect

## ES-ch04.46

A reviewer looks through an agent-trace write-up for invented success. Describe three kinds of invented success they should look for, how each can happen, and how to correct a mistaken interpretation without erasing the record of it.

**Points:** 5

**Rubric (1 point each):**

1. Describes summarizing a budget-exhausted run as success because the trace looked productive.
2. Describes supplying an answer for a run that ended incomplete, which fabricates content the controller never produced.
3. Describes calling an answer supported without comparing it with the evidence.
4. Explains how these arise: a status name or a long trace is read as an outcome.
5. Says to correct the statements while preserving the original mistaken reading in a dated record, and to state the actual mechanism that changed the understanding.

**Source:** Verify and reflect

## ES-ch04.47

A controller limits an agent to one turn, but its tool set includes a function that deletes files. Explain why the small iteration limit does not make the system safe, how iteration limits and permissions differ as controls, and what a permission policy for this tool set should specify before any tool runs.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a single call is enough to delete the wrong file.
2. Distinguishes iteration count, which limits how many actions run, from permission, which limits which actions and targets are allowed.
3. Says the policy should be written before any tool runs, not discovered after a harmful call.
4. Specifies that read, write and delete permissions are distinct and that read permission does not imply write permission.
5. Specifies the approved scope of targets and an approval step for destructive operations, with disposable test files for testing.

**Source:** A bounded loop can still cross a boundary once

## ES-ch04.48

A file tool is supposed to be confined to /work/project. A model requests ../secrets.txt, and also requests a file inside the project that is a symbolic link pointing to /etc/hosts. Explain why simple string checks on the path are insufficient and describe a sound confinement check.

**Points:** 5

**Rubric (1 point each):**

1. Explains that ../secrets.txt resolved against the project root lands outside it.
2. Explains that a symbolic link inside the root can point to a target outside it.
3. States that checking whether a path begins with a slash or contains a particular prefix as text does not establish where the operation lands.
4. Describes resolving the canonical path, following links, and checking that it lies under the approved root before acting.
5. Notes that the decision applies per operation, since permission to read a path does not give permission to write it.

**Source:** A bounded loop can still cross a boundary once

## ES-ch04.49

Design the log for a boundary where an agent's file operations are checked against a permission policy. List the fields to record, explain how they would let a reviewer reconstruct what happened, and explain why a good log still does not replace comparing the final state with what the human authorized.

**Points:** 5

**Rubric (1 point each):**

1. Includes the requested action and the requested path as given.
2. Includes the resolved target after canonicalization, so a reviewer can see when it differs from the request.
3. Includes the decision, allowed or denied, and the rule or reason behind it.
4. Includes the observation or result returned to the agent.
5. Explains that a log records events but does not judge whether the resulting state matches what was approved, so a separate comparison is needed.

**Source:** A bounded loop can still cross a boundary once

## ES-ch04.50

An agent has tools to read files, write files and send email. The harness requires human approval before each email is sent. Describe how this approval step should work, what the approver must be shown, how declines should be handled, and what the step does and does not guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Says the approval is enforced by the harness, not left to the model to request.
2. Says the approver should see the resolved recipient and the actual message, not a vague summary.
3. Says each action needs its own decision; approving one email does not approve later ones.
4. Says a decline should be recorded in the trace and either returned to the model as an observation or end the run.
5. States that approval does not make the content correct or the run safe in other respects, and that small turn budgets do not remove the need for it.

**Source:** The driver's seat

## ES-ch04.51

A turn cap stopped a runaway lookup loop in a test, and a repetition detector stayed quiet on a legitimate repeated check. A reviewer asks whether these controls are validated. Explain the difference between observing that nothing went wrong and validating a control, and for each control name a condition under which it would fail.

**Points:** 5

**Rubric (1 point each):**

1. Explains that one passing run is an observation of the control holding once, not validation.
2. Says validation includes understanding what could defeat the control.
3. Names a failure condition for the turn cap, such as a blocked call that the iteration count cannot interrupt, or a single iteration with a harmful action.
4. Names a failure condition for the detector, such as a repeat its definition does not cover or a case that resembles a legitimate repeat.
5. Says that if no failure condition can be named, the control has been observed to pass and nothing more, and that findings from a small exploratory study should not be read as general rates.

**Source:** Computational Skepticism

## ES-ch04.52

A test harness drives a controller with a pre-written list of actions instead of a model. Explain what this harness is good for, what it cannot show about a real model-backed agent, and what must exist before a system can be called adaptive.

**Points:** 5

**Rubric (1 point each):**

1. Says it makes runs repeatable and each decision inspectable.
2. Says it can exercise the controller's exits, status assignment and limits directly.
3. Says it cannot show how a real model chooses actions or responds to observations.
4. Says an adaptive system needs a defined route from observations back to the next decision.
5. Cautions against describing that route as implemented merely because the code uses a word like policy.

**Source:** The policy proposes, the controller stops, someone else judges

## ES-ch04.53

A run ends because its turn budget is spent without a finish action. Describe what the harness should return and do, what it must not do, and how to communicate the result so that downstream consumers do not treat it as success.

**Points:** 5

**Rubric (1 point each):**

1. Says to return a distinct budget-exhausted status together with the trace and the configured budget.
2. Says not to fabricate or synthesize a final answer to make the run look complete.
3. Says not to silently raise the budget and rerun, because changing a limit is an explicit decision.
4. Says to escalate to a person with the trace so they can decide to extend, narrow or abandon the task.
5. Says to keep this status distinct from other stops, because it establishes neither that the work was finished nor that the action source had nothing more to offer.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.54

A controller accepts a turn budget as an argument. List invalid values you would reject, explain Python's treatment of booleans and floats in this check, and say why validation should happen before the loop starts.

**Points:** 5

**Rubric (1 point each):**

1. Lists invalid values: zero, negative numbers, non-integers such as floats, and non-numeric types.
2. Explains that bool is a subclass of int in Python, so an isinstance check would accept True but an exact type check would not.
3. Explains that a zero or negative budget would give an empty loop that silently returns an exhausted status without ever consulting the action source.
4. Says validation should come first so a bad configuration fails before any iterator, trace or side effect exists.
5. Says the invalid-budget case is itself an exit that should be specified and tested.

**Source:** Every return statement is an exit someone decided

## ES-ch04.55

A team changes the finish action so that it must list the identifiers of the observations that support its answer. Evaluate this design: what it improves, what mechanical checks it enables, and what it cannot guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Says it makes some unsupported finishes mechanically detectable, such as a finish citing nothing.
2. Says a checker can verify that each cited identifier exists in the trace.
3. Says a model can cite real identifiers that do not support its claim, so content support needs separate checking.
4. Says it gives reviewers a starting point for tracing which observations the answer depends on.
5. Says it does not remove the need for an independent outcome check or guarantee correctness.

**Source:** A finished wrong answer

## ES-ch04.56

In an assistant coding session the user asks for a bug fix. The assistant reads files, edits one, asks permission to run a shell command, the user approves, the test suite runs, the assistant says it is done, and the user reads the diff and test output and then merges. Map this session onto action, observation and stop, say who takes each stop, and identify the independent outcome evidence.

**Points:** 5

**Rubric (1 point each):**

1. Maps file reads, edits and the test run to actions, and file contents, edit results and test output to observations.
2. Identifies the assistant's done message as a finish request that ends the assistant's run.
3. Identifies the user's approval or denial of the command as a human decision about continuing.
4. Identifies the merge or rejection as the human stop that closes the task.
5. Names the independent evidence: the diff and the actual test output, which are evidence only if read rather than relying on the assistant's summary.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch04.57

A reviewer sees a visible trace of an assistant's tool calls, their outputs and a final message, and is asked what they can conclude. Explain what a trace of actions and observations can support, what it cannot, and how a write-up should avoid overclaiming about the model's reasoning or the product's internals.

**Points:** 5

**Rubric (1 point each):**

1. Says it supports questions about sequence, what was requested, and what came back.
2. Says it does not expose the model's complete private reasoning.
3. Says narrating intentions at each step goes beyond the evidence.
4. Says resemblance to a simple controller does not show the product uses that implementation.
5. Says for outcome claims the independent evidence is the changed artifacts and executed checks, not the final message.

**Source:** A trace records an event, not knowledge

## ES-ch04.58

Explain why a controller that returns incomplete and one that returns budget-exhausted should be treated differently downstream. Give two policies and budgets that lead to each status, and describe what a person would do differently after seeing each.

**Points:** 5

**Rubric (1 point each):**

1. Defines incomplete as the action source running out before the budget did, and budget-exhausted as the controller spending every turn it was given.
2. Gives a policy and budget producing incomplete, such as a one-lookup policy with a budget of four.
3. Gives a policy and budget producing budget-exhausted, such as the same policy with a budget of one, or an endless source with any budget.
4. Explains the follow-up for incomplete: investigate why the action source stopped without finishing.
5. Explains the follow-up for budget-exhausted: decide whether to raise, narrow or abandon, noting that it does not show the work was nearly done.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.59

An unbounded agent run makes one model call every 8 seconds at $0.05 per call and goes undetected for 2 hours. An operator considers a hard cap of 30 calls. Compute the number of calls and cost of the unbounded run, and the cost and maximum duration under the cap, and state the assumptions behind each figure.

**Points:** 5

**Rubric (1 point each):**

1. Computes 900 calls for two hours at one call per 8 seconds.
2. Computes $45 for the unbounded run.
3. Computes $1.50 for 30 calls at $0.05 each.
4. Computes a maximum of 240 seconds under the cap if each turn takes 8 seconds.
5. States the assumptions: constant price per call and constant turn duration, and notes the cap bounds neither if calls get more expensive or turns slower.

**Source:** Budget exhaustion is not policy exhaustion

## ES-ch04.60

A returned object from a controller run reads: status "finished", answer "", trace of three entries, each with action "lookup". A reviewer must decide what the object does and does not tell them. Analyze it: what is established, what is not, and what follow-up checks are needed before the answer is used.

**Points:** 5

**Rubric (1 point each):**

1. States that a finish action was received, which is what finished establishes.
2. Notes that the empty answer means the run finished without content, so nothing was answered.
3. Notes that the status does not show the task was addressed or that any observation supports an answer.
4. Says the trace shows three lookups but without the keys cannot show which evidence was gathered, so the reviewer needs the arguments or the action list.
5. Names follow-ups: reject or investigate the empty finish, run the independent outcome check against the task's key, and have a person decide on acceptance.

**Source:** A finished wrong answer

## ES-ch04.61

A team's specification says an answer leaves the controller only if the status is finished and a separate check passes; any other status sends the status and the trace to a person. Explain why this release rule is structured this way, what each condition contributes, and what it still does not guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the finished status contributes only that a finish was received.
2. Explains that the separate check contributes evidence about the answer against the task's requirement.
3. Explains that sending other statuses and the trace to a person avoids fabricating an answer and keeps the closing decision human.
4. Says the check reads the evidence rather than the trace and never rewrites the controller's status.
5. States that the rule does not guarantee correctness beyond what the check covers, and that a real task may still need a person to read the trace.

**Source:** Write the exits before anyone runs the loop

## ES-ch04.62

Explain the idea of "reading each return statement as a decision with an owner" for a loop controller. Use the exits finished, incomplete, budget-exhausted and invalid-budget error to show who decided each, when, and what each exit does and does not claim.

**Points:** 5

**Rubric (1 point each):**

1. States that every exit is a design decision made by someone before the run, not an accident of the code.
2. Explains finished as: a finish action was consumed, claiming nothing about the answer's correctness.
3. Explains incomplete as: the action source ran out first, claiming neither success nor impossibility.
4. Explains budget-exhausted as: the controller used every allowed turn, claiming nothing about completion or time.
5. Explains the invalid-budget error as a configuration decision made before the loop touches the action source.

**Source:** Every return statement is an exit someone decided
