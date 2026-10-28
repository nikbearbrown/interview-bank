# Chapter 10: Planning before acting

## MA-ch10.1

A team represents an agent's proposed plan as a Python dictionary and validates it with this function:

```python
FIELDS = ("objective", "inputs", "scope", "steps", "tools", "risks", "verification", "stop")

def missing_fields(plan):
    return [f for f in FIELDS if not plan.get(f)]
```

They call it on a dictionary in which all eight keys are present and every value is the string "x". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The empty result is the correct output for the rule the function implements.
- [ ] B. A reviewer could still reject every field of this plan as meaningless.
- [ ] C. Rejecting this plan would require checks beyond truthiness, such as a review of what the entries mean.
- [ ] D. The empty result shows the plan is ready for approval.
- [ ] E. The function returns an empty list.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The function was written to detect absent or false-valued fields, and none are.
- B: Presence is not meaning; a single repeated character answers none of the questions a field exists to answer.
- C: Truthiness cannot tell a meaningful entry from a placeholder, so something beyond it is needed.
- D: The function checks only that values are truthy; it says nothing about whether they mean anything.
- E: Every value is a nonempty string, which is truthy, so no field is reported missing.

**Source:** What missing_fields actually checks

## MA-ch10.2

A presence checker uses `not plan.get(f)` to decide that a field is missing. It is run on this plan:

```python
plan = {"objective": "Fix bug", "inputs": [], "scope": 0, "steps": ["inspect"],
        "tools": False, "risks": " ", "verification": None, "stop": "when done"}
```

The checker loops over the eight field names in the order objective, inputs, scope, steps, tools, risks, verification, stop and returns the names it finds missing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "risks" is reported missing because it contains only whitespace.
- [ ] B. "verification" is reported missing even though the key is present.
- [ ] C. "inputs" is reported missing.
- [ ] D. "stop" is reported missing because "when done" is not an observable condition.
- [ ] E. The returned list follows the order of the field names above, not any other order.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A string containing a space is nonempty and therefore truthy, so it passes.
- B: The stored value None is falsy, so it is treated like an absent entry.
- C: An empty list is falsy in Python.
- D: The function cannot judge meaning or observability; "when done" is a nonempty string and passes.
- E: The checker loops over the field names in the fixed order given, so missing names come back in that order: inputs, scope, tools, verification.

**Source:** What missing_fields actually checks

## MA-ch10.3

An agent platform accepts a plan only if `all(plan.get(f) for f in FIELDS)` is true, where FIELDS names objective, inputs, scope, steps, tools, risks, verification and stop. A plan passes this test. Check each statement that describes a problem that could still be present in the passing plan. Each statement is worth 1 point (5 points total).

- [ ] A. The tools entry names only a product and says nothing about permitted operations.
- [ ] B. The declared steps contain a dependency cycle.
- [ ] C. The steps value is a plain string rather than a list of steps.
- [ ] D. The risks entry is an empty list.
- [ ] E. The scope entry permits deleting records in a production database.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A truthy string such as a product name satisfies the test even though it specifies no capability or limits.
- B: Cycles are a property of how steps relate, which a presence test never examines.
- C: A truthiness test enforces no type, so a nonempty string passes.
- D: An empty list is falsy, so the test would fail the plan.
- E: Whether a scope is safe is a semantic judgment the test cannot make.

**Source:** What missing_fields actually checks

## MA-ch10.4

A support assistant must reply in JSON with the form {"answer": string, "confidence": number from 0 to 1}. A schema validator checks that the reply parses and has these two keys with the right types. The company's refund window is 30 days. The model returns {"answer": "Our refund window is 90 days.", "confidence": 0.97}. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The pass rate of this validator over many replies measures factual accuracy.
- [ ] B. Tightening the schema so that confidence must lie between 0 and 1 would catch this error.
- [ ] C. Because the reply passes validation, comparing the answer with the policy text is unnecessary.
- [ ] D. The reply passes schema validation.
- [ ] E. The confidence of 0.97 is evidence that the answer is grounded in the policy.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The validator measures structure; a well-formed reply can state a false fact.
- B: The confidence is already within range, and a range rule says nothing about the answer text.
- C: Validation checks only structure; a comparison with the policy text is what detects a false claim.
- D: The reply parses, has both keys and has the right types.
- E: A model-reported confidence is not a check of grounding and can be high for a false statement.

**Source:** What missing_fields actually checks

## MA-ch10.5

A team runs a deterministic, inexpensive structural check on every plan an agent proposes before a person reviews it. The check never examines meaning. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because it never tires and never notices meaning, it fails differently from a human reviewer.
- [ ] B. Running it first removes the need for a human to read the plan.
- [ ] C. A plan that passes it has been shown safe to execute.
- [ ] D. The check is worthless unless it can detect every kind of defect.
- [ ] E. Requiring the steps field to be a nonempty list would catch more structural defects but would still not show that the objective serves the right person.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Machine and human errors are different in kind, which is why combining them covers more ground.
- B: It clears only structural failures; a person must still judge meaning.
- C: Passing a structural check says nothing about safety or authority.
- D: A narrow check that reliably rejects what it targets is useful even though it is incomplete.
- E: Stricter structure rules reduce structural defects only; relevance to the stakeholder remains a judgment call.

**Source:** What missing_fields actually checks

## MA-ch10.6

In Python, consider this dictionary:

```python
plan = {"risks": [], "stop": "after tests pass"}
```

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. `plan.get("verification")` evaluates to None.
- [ ] B. `plan.get("risks")` evaluates to None.
- [ ] C. `plan.get("verification")` raises a KeyError.
- [ ] D. `"risks" in plan` evaluates to True.
- [ ] E. `not plan.get("risks")` evaluates to True.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Missing key with no default gives None.
- B: The key is present, so `get` returns its value, the empty list, not None.
- C: `dict.get` returns None for a missing key instead of raising; only `plan["verification"]` would raise.
- D: The `in` operator tests for the key, and the key is present.
- E: An empty list is falsy, so `not []` is True; this is why a key-presence test and a truthiness test disagree.

**Source:** What missing_fields actually checks

## MA-ch10.7

A team strengthens its plan validator: the verification field must now be a string that contains a shell command. A plan states the objective "restore correct rounding in the invoice-total function" and the verification entry `ls tests/`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The command is a sound proxy for the rounding claim because both concern the invoice module.
- [ ] B. The stricter validator makes a human comparison of the objective with the verification entry unnecessary.
- [ ] C. Adding another structural rule, such as requiring the command to start with a known program name, would settle whether the command tests the right claim.
- [ ] D. The command shows that the rounding behavior is correct.
- [ ] E. The plan satisfies the stricter validator.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: A directory listing observes nothing about rounding, so it is not a sound proxy for that claim.
- B: The mismatch between objective and check is exactly what a cross-field review exists to catch.
- C: Whether a command tests the claimed behavior is a semantic question that no further format rule decides.
- D: Listing a directory runs no test and observes no rounding behavior.
- E: The entry is a string containing a shell command.

**Source:** What missing_fields actually checks

## MA-ch10.8

An engineer writes preconditions, postconditions and invariants for a function, then asks a coding agent to write the implementation. Tests and assertions are derived from the written contract, not from the agent's code. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the contract is incomplete, the agent will reliably stop and report each gap.
- [ ] B. The decisions about boundaries and required behavior are fixed before the code exists.
- [ ] C. Tests derived from the contract can check the implementation without relying on the agent's description of it.
- [ ] D. The contract is satisfied once the agent states that it holds.
- [ ] E. Deriving the tests from the agent's own implementation is equally independent of the agent.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Models often complete underspecified requests with plausible guesses and may not flag them.
- B: Writing the contract first moves the important decisions ahead of implementation, where they are cheap to change.
- C: The contract is an external reference, so the tests do not inherit the agent's assumptions.
- D: A claim of compliance is not evidence; the tests or assertions are the evidence.
- E: Tests built from the implementation encode whatever the implementation does, including its mistakes.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.9

A team debates whether a coding agent that edits a repository should first propose a plan that a person reviews, before any file changes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. To be useful, the plan must reproduce the model's private reasoning in full.
- [ ] B. Once reviewed, the plan fixes the version that is implemented, and evidence can still reopen it.
- [ ] C. When an intermediate result contradicts an assumption the plan rested on, the plan should be revised and the reason recorded.
- [ ] D. Revising a proposed plan costs much less than rolling back executed changes.
- [ ] E. The plan serves as a record of intended actions that other people can critique.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A plan is an action commitment others can inspect; it need not mirror internal deliberation.
- B: Approval fixes a version to implement against, but a contradicting result can send it back for revision.
- C: Updating with a recorded reason keeps track of which decision the evidence overturned.
- D: Editing a paragraph before action is cheaper than reverting work after it.
- E: A plan exposes destination, scope, steps and stopping rule while change is still cheap.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.10

An LLM application team compares two designs. In a plan-and-execute design, a planner writes a full list of steps first and an executor then runs them. In an adaptive design, the model chooses each next action after seeing the previous observation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Plan-and-execute removes the need to check results between steps.
- [ ] B. A plan written up front can be inspected by a person before any action is taken.
- [ ] C. A plan produced up front never needs revision because the prerequisites are known in advance.
- [ ] D. An adaptive loop cannot respond to an unexpected tool output until a new plan is written.
- [ ] E. A fixed, predictable sequence of steps favors a predefined workflow over open-ended model-directed choices.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Intermediate results still need checking, because an early failure can invalidate later steps.
- B: The main benefit of an explicit plan is that it can be reviewed before it acts.
- C: Plans rest on assumptions that results can falsify, so replanning is a normal event.
- D: In an observe-then-act loop each observation can change the next action directly.
- E: When the path is known, a fixed sequence is simpler, cheaper and more predictable.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.11

An agent implements a discount rule. While auditing the diff, a reviewer sees that the code rounds prices using one particular rounding mode, and the requirements never said how to round. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The episode shows that planning before acting is pointless because requirements change.
- [ ] B. The reviewer should leave the code as is because the agent's choice is already implemented.
- [ ] C. The requirement should be reopened, the gap logged and the plan updated with the reason.
- [ ] D. The revised plan can be implemented immediately because the reviewer already saw the problem.
- [ ] E. The episode shows that a move in the solution space can force a reframing of the problem.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A first reviewed plan is what makes it possible to see which decision the new evidence reopens.
- B: An unrecorded implicit decision stays hidden and may be wrong.
- C: A missing requirement is a decision that was never made; recording it keeps the history of the design honest.
- D: A revised plan is a new version and needs its own review.
- E: Problem and solution develop together, so work on a solution often reveals an unstated requirement.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.12

A developer asks a coding agent to propose a plan for a refactor and states that no file may be modified yet. The agent returns a plan whose last line reads "Approved by reviewer." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the agent interface is unavailable, the team should write a plausible agent-authored plan so that the record looks complete.
- [ ] B. A fluent justification inside the plan is evidence that the plan is sound.
- [ ] C. The returned plan is a proposal, not an approval.
- [ ] D. Because the developer asked for no file changes, the returned plan is already authorized for execution.
- [ ] E. The line "Approved by reviewer" records an approval.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Fabricating output or approvals misrepresents the record; the honest course is to state that the session did not run.
- B: How well a plan is argued says little about whether its commitments are correct or safe.
- C: Approval is an act by an accountable person, not a property of the text a model returns.
- D: Asking for a proposal yields a reviewable plan; authorization is a separate act by a person.
- E: A sentence written by the model cannot record that a person approved anything.

**Source:** Use It: conduct Claude Code against the plan

## MA-ch10.13

A pipeline moves an AI-drafted document to a human reviewer only if a stated condition holds. The team wants conditions that are testable. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "The draft has been reviewed and looks reasonable" is a testable condition.
- [ ] B. A condition is testable if someone who did not build the pipeline can read it, observe the system and decide whether it holds.
- [ ] C. A condition that only its author has ever applied has not yet been shown to be testable.
- [ ] D. "Every figure in the draft appears in the supplied source table with the same value" is more testable than "the draft is accurate".
- [ ] E. Interpretive words such as "reasonable" should be replaced by criteria, and the result tried by someone who did not write it on a sample case.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Five reviewers would do five different things and all call it reviewing.
- B: Testability means an independent person reaches a decision from observation.
- C: Testability is shown when someone else can apply the condition to a sample and reach a decision.
- D: It names an observable comparison with a defined outcome.
- E: The replace-then-hand-to-a-stranger procedure exposes remaining ambiguity.

**Source:** Evidence belongs on the edges

## MA-ch10.14

A data team spends a quarter building a very accurate model that predicts which customers will open a marketing email. The business actually needed to know which customers are about to cancel their subscriptions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A fluent, internally consistent answer from an AI assistant can make a wrong framing harder to challenge.
- [ ] B. Raising the model's accuracy further would remove the problem.
- [ ] C. In hypothesis-testing terms it is a Type II error, a false negative.
- [ ] D. In the sense Kimball gave the term, this is an error of the third kind: a right answer to the wrong problem.
- [ ] E. Checking the finished result against the framing it already assumes is a weak test of whether the framing was right.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Polish lends authority to an answer that the question never earned.
- B: Accuracy on the wrong target is irrelevant to the business need.
- C: A Type II error is failing to reject a false null hypothesis; it concerns a decision inside a given problem, not the choice of problem.
- D: Kimball used "error of the third kind" for solving the wrong problem correctly, which is what happened here.
- E: An audit that shares the framing's assumptions cannot reveal that the framing is off.

**Source:** Formulate before you plan

## MA-ch10.15

Design researchers describe a "primary generator": an early, often tacit idea of what a problem is really about, which determines which solutions a designer can see. A developer asks an LLM to frame a problem before writing down any framing of their own. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Auditing the model's answer against the framing it already assumes is independent of that framing.
- [ ] B. The model's framing is wrong by construction.
- [ ] C. Writing candidate framings first preserves a basis for judging the model's framing independently.
- [ ] D. A developer can avoid having any primary generator by staying neutral.
- [ ] E. The model's framing can become the developer's anchor by default.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The audit would be measured against the very assumption it needs to be independent of.
- B: A model's framing may be perfectly good; the risk is adopting it unexamined.
- C: Having your own candidates gives you something to compare the model's against.
- D: One cannot start thinking about a problem without some first idea, so the realistic choice is whether to name it.
- E: Whoever names the first framing sets which solutions look natural; if the model names it, the model's anchor is adopted.

**Source:** Formulate before you plan

## MA-ch10.16

A function should return its input plus one but returns its input minus one. The failing test calls f(2) and expects 3. Three candidate formulations of success are: (X) the f(2) test passes; (Y) f returns input plus one for every integer, and no file outside the function's module and its test changes; (Z) the developer can explain the cause of the bug. Two constructed results are tried against them. Result 1 is a patch that returns the constant 3, applied without diagnosing the cause. Result 2 is a correct patch (input plus one) written by an AI and accepted without being read, so the developer cannot explain the cause. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Result 1 satisfies formulation X and fails formulation Y.
- [ ] B. Both results satisfy formulation X.
- [ ] C. Because the formulations disagree about whether a result succeeded, they describe different problems and not one problem in different words.
- [ ] D. Results 1 and 2 cannot tell formulations X and Y apart.
- [ ] E. Result 2 satisfies formulation Z.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A constant 3 passes the f(2) test but gives 3 for input five instead of 6.
- B: Both patches return 3 for input two.
- C: If every constructed result were judged the same by all three, there would be one formulation; disagreement shows distinct success conditions.
- D: Result 1 passes X and fails Y, so it separates them.
- E: The developer accepted the patch unread and cannot explain the cause.

**Source:** Formulate before you plan

## MA-ch10.17

A team must choose among several candidate formulations of a problem and is writing the criteria for choosing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A salience criterion, asking whether solving the problem addresses what matters in this context, helps counter a bias toward the merely tractable.
- [ ] B. The criteria should be fixed before any candidate is scored, so they are not tuned to favor a preferred option.
- [ ] C. If every criterion concerns cost, time and technical feasibility, the process tends to select the most tractable formulation, not the most important one.
- [ ] D. A model can propose candidate criteria, but the team owns the final criteria.
- [ ] E. The criteria are best written after the scores are known, so they reflect what was learned.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Salience brings the question of importance into the comparison.
- B: Criteria chosen after seeing scores can be bent to justify a prior preference.
- C: Feasibility-only scoring rewards what is easy to build or measure.
- D: Drafting can be delegated; the criteria encode what the team values, and the team answers for them.
- E: Writing criteria afterward lets the outcome shape the standard that is supposed to judge it.

**Source:** Formulate before you plan

## MA-ch10.18

A team chooses formulation P, "restore the documented behavior for every caller of the function", over formulation Q, "make the learner able to explain the bug". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Saying "we chose P; it leaves out the learner's understanding, which a separate step addresses" is a defended selection.
- [ ] B. Choosing P also chooses not to serve the learner's understanding in this plan.
- [ ] C. Because P and Q could both be pursued eventually, naming what P leaves out is unnecessary.
- [ ] D. Deciding whose interests to center can be delegated to the model because it can list stakeholders.
- [ ] E. The choice involves no value judgment because both formulations are technically feasible.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Naming what was left out, and where it is handled, makes the choice open to challenge.
- B: Every formulation centers some interests and decenters others.
- C: Even if both are pursued later, this plan serves one of them, and saying so makes the trade-off visible.
- D: Listing stakeholders is not the same as deciding between them, and the decision needs a named owner.
- E: Deciding whom the work serves is a value judgment regardless of feasibility.

**Source:** Formulate before you plan

## MA-ch10.19

A developer has written three candidate formulations of a task and wants to use an LLM in the formulation step. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The model's statement that two formulations are distinct is enough to certify that they are distinct for this organization.
- [ ] B. The developer can accept the model's objections without checking them against the plan.
- [ ] C. Letting the model write the only candidate list is as protective against anchoring as writing candidates first.
- [ ] D. The model can suggest candidates the developer missed.
- [ ] E. Asking the model to construct a result that satisfies one formulation but fails another is a useful way to probe whether the two really differ.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Whether two framings need different solutions in a given domain depends on situated knowledge that a model's assertion does not establish.
- B: Objections can be wrong or irrelevant, and each should be verified.
- C: If the model's list is the only one, its framing sets the anchor.
- D: Extending the candidate set is a low-risk use of a model.
- E: Finding a separating result is a concrete test of distinctness and the kind of search a model does quickly.

**Source:** Formulate before you plan

## MA-ch10.20

A reviewer reads entries from the fields of a proposed plan for an agent that fixes a bug in a billing module. Check each entry that a reviewer can concretely challenge, as opposed to an entry that merely fills its field. Each statement is worth 1 point (5 points total).

- [ ] A. Tools: "Claude Code."
- [ ] B. Stop: "Stop when done."
- [ ] C. Risks: "There may be risks."
- [ ] D. Objective: "Make the failing invoice-rounding test pass without changing any file outside src/invoice.py and its test."
- [ ] E. Verification: "Run pytest tests/test_invoice.py; require exit status 0 and a diff that touches only src/invoice.py and that test file."

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It names a product, not the capability needed, the reason, or the operations permitted and forbidden.
- B: It gives no observable condition, so it cannot be applied or contested.
- C: It names no risk, mitigation, owner or trigger, so there is nothing to disagree with.
- D: It states an outcome someone can check and a boundary someone can argue is too tight or too loose.
- E: It names an exact command, an expected outcome and a diff boundary a reviewer can dispute.

**Source:** The eight fields are eight questions

## MA-ch10.21

A planning template has eight fields: objective, inputs, scope, steps, tools, risks, verification and stop. Each field is meant to answer a question. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The risks field is stronger when each risk is tied to a mitigation, an owner or a stop trigger.
- [ ] B. The scope field answers what may change and what must stay untouched.
- [ ] C. The inputs field is adequate when it lists filenames; provenance and version need not be recorded.
- [ ] D. The tools field names the capability needed, why it is needed, and which operations remain under human approval.
- [ ] E. A steps entry is adequate when it says what the step produces and how anyone would know it finished.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A risk that triggers nothing is decoration.
- B: Scope is the boundary of permitted change.
- C: A reviewer needs to know where inputs came from and which version, or the work cannot be reproduced or trusted.
- D: A tool entry should say what the capability is for and where human approval is required.
- E: An observable output and a completion test make a step something a reviewer can check.

**Source:** The eight fields are eight questions

## MA-ch10.22

A plan's steps only read files, run a test suite and write a report. Its tools field lists a shell with write access and network access. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Write access is unnecessary for the stated steps.
- [ ] B. The scope field is adequate if it lists only file names.
- [ ] C. If a step required a capability absent from the tools field, the agent should acquire it quietly and note it afterward.
- [ ] D. Extra capabilities are harmless as long as the agent does not use them.
- [ ] E. Because the tools are available, they are permitted for this task.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Nothing in the steps writes, so the write capability exceeds the need (least privilege).
- B: Scope should also say which operations are permitted and which systems are excluded.
- C: A plan that lacks a capability a step needs is infeasible as written and should be revised and reviewed.
- D: Unneeded capability is a risk surface, since errors or injected instructions can use it.
- E: Capability does not create authority; a tool can be available yet forbidden.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.23

A developer decides which parts of a plan to let an AI assistant draft and which to answer personally. Check each statement that describes a part that is reasonable to hand to the assistant for a first draft, which the developer then reviews. Each statement is worth 1 point (5 points total).

- [ ] A. Deciding which risks the organization is willing to accept.
- [ ] B. A first draft of the step list.
- [ ] C. A first draft of the tools list.
- [ ] D. Deciding to widen the scope of the work.
- [ ] E. Deciding who has authority to stop the work.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Risk acceptance depends on what the organization will tolerate, which no file contains.
- B: Drafting steps is a task a model does well, and a person can revise the draft.
- C: A tools list depends on the steps and can be drafted and checked.
- D: Widening scope changes what is authorized and needs a named decider.
- E: Who may stop work is an authority decision that must be assigned by a person.

**Source:** The eight fields are eight questions

## MA-ch10.24

Midway through a task, an agent reports that fixing the bug properly requires editing a file outside the plan's declared scope. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The scope field is advisory and the agent may override it when it judges the change to be beneficial.
- [ ] B. Treating an out-of-scope change as a logged warning while the edit proceeds is a sound design.
- [ ] C. Describing the edit as an implementation detail of an in-scope step is an appropriate way to proceed.
- [ ] D. If the edit is small, the scope field can be ignored.
- [ ] E. The plan should be revised and the expansion approved before the edit.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The scope field is what the approval covered; the agent's judgment of benefit is not authorization.
- B: A boundary that only warns does not stop the change that needed authorization.
- C: Hiding an expansion inside an implementation detail launders it past the review.
- D: A boundary that yields to small exceptions stops bounding anything.
- E: Scope changes need review before action so that authority stays with a person.

**Source:** The eight fields are eight questions

## MA-ch10.25

A team compares two designs for an LLM application. In a workflow, the model calls are orchestrated through predefined code paths. In an agent, the model directs its own process and tool use. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In a prompt-chaining workflow, programmatic checks between steps are impossible.
- [ ] B. Agents are preferable for every task because they can plan.
- [ ] C. A common recommendation is to start with the simplest solution and add complexity only when it demonstrably helps.
- [ ] D. A workflow trades flexibility for predictability, which suits tasks whose steps are known in advance.
- [ ] E. An agent suits open-ended tasks where the number and order of steps cannot be predicted.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Prompt chaining commonly inserts programmatic gates that verify an intermediate output before the next step.
- B: Agents add cost, latency and risk of compounding errors, so they are not a default choice.
- C: This is widely documented guidance for building LLM systems.
- D: Fixed paths are easier to test, cost-control and review.
- E: When the path cannot be fixed in advance, model-directed choices are needed.

**Source:** Anthropics

## MA-ch10.26

A plan's steps are ordered by this function:

```python
def topo_order(steps):
    graph = {}
    for s in steps:
        if s["id"] in graph:
            raise ValueError("Duplicate step")
        graph[s["id"]] = set(s.get("after", []))
    if any(deps - graph.keys() for deps in graph.values()):
        raise ValueError("Unknown prerequisite")
    result = []
    while graph:
        ready = sorted(k for k, d in graph.items() if not d)
        if not ready:
            raise ValueError("Dependency cycle")
        for k in ready:
            result.append(k)
            del graph[k]
        for d in graph.values():
            d.difference_update(ready)
    return result
```

It is called with `[{"id": "a"}, {"id": "b", "after": ["a"]}, {"id": "c", "after": ["a"]}, {"id": "d", "after": ["b", "c"]}]`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Step d becomes ready as soon as b finishes.
- [ ] B. The body of the while loop runs four times.
- [ ] C. Steps b and c become ready in the same iteration of the while loop.
- [ ] D. That b precedes c in the output is evidence that b should be executed first.
- [ ] E. The function returns ["a", "b", "c", "d"].

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: d needs both b and c, so it is not ready until both are removed.
- B: Rounds are {a}, {b, c}, {d}, so the body runs three times.
- C: Both depend only on a, so once a is removed both have empty prerequisite sets.
- D: Sorting within a ready batch is a tie-break for deterministic output; it says only that b and c do not depend on each other.
- E: Round one yields a, round two yields b and c in sorted order, round three yields d.

**Source:** Dependencies are directed obligations

## MA-ch10.27

The function below orders plan steps by their declared prerequisites:

```python
def topo_order(steps):
    graph = {}
    for s in steps:
        if s["id"] in graph:
            raise ValueError("Duplicate step")
        graph[s["id"]] = set(s.get("after", []))
    if any(deps - graph.keys() for deps in graph.values()):
        raise ValueError("Unknown prerequisite")
    result = []
    while graph:
        ready = sorted(k for k, d in graph.items() if not d)
        if not ready:
            raise ValueError("Dependency cycle")
        for k in ready:
            result.append(k)
            del graph[k]
        for d in graph.values():
            d.difference_update(ready)
    return result
```

It is called on four inputs. Input 1 has two steps that both have id "test". Input 2 is a single step `{"id": "verify", "after": ["test"]}` and no step named "test". Input 3 is `{"id": "a", "after": ["b"]}` and `{"id": "b", "after": ["a"]}`. Input 4 is a single step `{"id": "a", "after": ["a"]}`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Input 3 raises ValueError("Dependency cycle").
- [ ] B. Input 2 raises ValueError("Dependency cycle").
- [ ] C. Input 4 returns ['a'].
- [ ] D. Input 1 returns ["test"].
- [ ] E. Input 1 raises ValueError("Duplicate step").

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Neither step can become ready because each waits for the other.
- B: The unknown-prerequisite check runs before the loop and fires first, with its own message.
- C: A step waiting on itself can never become ready, so the call raises instead of returning.
- D: A dictionary key can hold only one step, so duplicates are rejected, not merged.
- E: The second "test" finds its key already in the graph, so the duplicate check fires.

**Source:** Dependencies are directed obligations

## MA-ch10.28

A developer deletes the unknown-prerequisite check from an ordering function, leaving this version:

```python
def topo_order(steps):
    graph = {}
    for s in steps:
        if s["id"] in graph:
            raise ValueError("Duplicate step")
        graph[s["id"]] = set(s.get("after", []))
    result = []
    while graph:
        ready = sorted(k for k, d in graph.items() if not d)
        if not ready:
            raise ValueError("Dependency cycle")
        for k in ready:
            result.append(k)
            del graph[k]
        for d in graph.values():
            d.difference_update(ready)
    return result
```

It is called on a single step `{"id": "verify", "after": ["test"]}` with no step named "test". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The call raises ValueError("Dependency cycle").
- [ ] B. The error message the call produces correctly identifies the defect in the input.
- [ ] C. With the original check in place, the error would name the real problem: a reference to work that does not exist.
- [ ] D. The call returns ["verify"] because the missing step is ignored.
- [ ] E. The remedy for a missing prerequisite is the same as the remedy for a cycle.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: verify's prerequisite set is {"test"} and nothing can remove it, so no step is ever ready.
- B: There is no cycle; the input refers to a step that was never defined, so the message misleads.
- C: Checking references first separates the two defects and gives each its own message.
- D: The unsatisfied prerequisite keeps verify from ever becoming ready.
- E: A missing prerequisite is fixed by defining or correcting the reference; a cycle is fixed by redefining the steps.

**Source:** Dependencies are directed obligations

## MA-ch10.29

The function below orders plan steps:

```python
def topo_order(steps):
    graph = {}
    for s in steps:
        if s["id"] in graph:
            raise ValueError("Duplicate step")
        graph[s["id"]] = set(s.get("after", []))
    if any(deps - graph.keys() for deps in graph.values()):
        raise ValueError("Unknown prerequisite")
    result = []
    while graph:
        ready = sorted(k for k, d in graph.items() if not d)
        if not ready:
            raise ValueError("Dependency cycle")
        for k in ready:
            result.append(k)
            del graph[k]
        for d in graph.values():
            d.difference_update(ready)
    return result
```

A user writes the steps `[{"id": "build"}, {"id": "verify", "after": "build"}]`, passing the prerequisite as a bare string instead of a list. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the call raises an error, its message points directly to the real cause, which is that the value should be a list.
- [ ] B. The call raises ValueError("Unknown prerequisite").
- [ ] C. Passing the prerequisite as a list would change the exception to a TypeError.
- [ ] D. `set("build")` contains five elements.
- [ ] E. The call raises a TypeError.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The message says a prerequisite is unknown, which hides that the string was split into characters.
- B: The set built from the string is {"b", "u", "i", "l", "d"}, none of which is a step id.
- C: A list of known ids works normally and no TypeError is involved.
- D: Iterating a string yields its characters, giving five distinct letters.
- E: A string is iterable, so `set(...)` succeeds and no TypeError occurs.

**Source:** Build It: the baseline that lets you audit the plan

## MA-ch10.30

A planning tool represents steps as nodes of a directed graph, with an edge from step X to step Y when Y declares X as a prerequisite. It orders them by repeatedly removing all nodes that have no remaining prerequisites. Check each statement that is true about topological ordering in general. Each statement is worth 1 point (5 points total).

- [ ] A. If a nonempty graph has no node without prerequisites, the graph contains a cycle.
- [ ] B. A topological ordering can be computed in time proportional to the number of nodes plus the number of edges.
- [ ] C. A graph can have several valid topological orderings.
- [ ] D. Every directed acyclic graph has exactly one valid topological ordering.
- [ ] E. Every nonempty directed acyclic graph has at least one node with no prerequisites.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: If every node has a prerequisite, following them forever in a finite graph must revisit a node.
- B: Standard algorithms such as Kahn's algorithm run in O(V + E).
- C: Independent steps can be swapped, as with two steps that share only a common prerequisite.
- D: Uniqueness holds only when the graph forces a single chain.
- E: Following prerequisites backward from any node must end, since no cycle exists to loop in.

**Source:** Dependencies are directed obligations

## MA-ch10.31

A build plan has four steps. Lint and test have no prerequisites. Build requires both lint and test. Deploy requires build. Check each statement that is a valid execution order for these dependencies. Each statement is worth 1 point (5 points total).

- [ ] A. build, lint, test, deploy
- [ ] B. test, lint, build, deploy
- [ ] C. lint, build, test, deploy
- [ ] D. lint, test, build, deploy
- [ ] E. lint, test, deploy, build

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Build runs before lint and test, which it requires.
- B: Lint and test are independent, so either order is allowed.
- C: Build runs before test, which it requires.
- D: Both prerequisites of build come first, then build, then deploy.
- E: Deploy runs before build, which it requires.

**Source:** Dependencies are directed obligations

## MA-ch10.32

In a plan, the step "verify" declares that it comes after the step "build". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An ordering function can confirm that build actually produces something usable by verify.
- [ ] B. Verify should not be treated as ready until build has produced what verify needs.
- [ ] C. In any valid order, build appears before verify.
- [ ] D. The declared edge by itself specifies which artifact build hands to verify.
- [ ] E. If the plan's writer forgets to declare a dependency that is really needed, the ordering function will infer it from the step descriptions.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: An ordering function sees only identifiers and arrows, not what steps do.
- B: An edge is an obligation about readiness, not merely a line in a list.
- C: That is what the edge means.
- D: An arrow gives order, not the content of the handoff.
- E: It orders only the arrows that were declared.

**Source:** Dependencies are directed obligations

## MA-ch10.33

In a plan graph, the steps "migrate_schema" and "seed_test_data" have no dependency between them and become ready in the same batch. Both write to the same database. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Every pair of steps in the same ready batch is necessarily unsafe to run concurrently.
- [ ] B. No declared dependency means the ordering function treats the two steps as independent.
- [ ] C. The graph represents the conflict automatically because both steps write to the same database.
- [ ] D. An added edge, a lock or a separate database would address the conflict.
- [ ] E. Being in the same ready batch proves the two steps can safely run concurrently.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Many parallel-ready pairs touch nothing in common and are safe.
- B: The function sees only declared arrows.
- C: The graph holds only the arrows that were declared; resource conflicts must be added explicitly.
- D: Serializing or isolating the steps removes the contention.
- E: Absence of a declared dependency says nothing about shared resources or authority.

**Source:** Dependencies are directed obligations

## MA-ch10.34

A data pipeline plan has seven steps. fetch and docs have no prerequisites. clean requires fetch. features requires clean. split requires clean. train requires features and split. report requires train. The steps are ordered by a function that repeatedly removes, in one batch sorted by id, all steps whose prerequisites are done. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The function's loop runs five times, once per batch.
- [ ] B. The step docs comes first only because ids are sorted within a ready batch; placing it after report would violate no declared dependency.
- [ ] C. There are exactly 14 distinct valid orderings of these seven steps.
- [ ] D. docs must precede fetch in every valid ordering.
- [ ] E. The function returns docs, fetch, clean, features, split, train, report, in that order.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Five batches means five loop iterations.
- B: docs is unconnected, so any position is valid.
- C: The connected chain has two orderings (features before split or after), and docs can sit in any of 7 positions, giving 2 x 7 = 14.
- D: docs and fetch are unrelated, so either order is valid.
- E: Batches are {docs, fetch}, {clean}, {features, split}, {train}, {report}, each sorted by id.

**Source:** Dependencies are directed obligations

## MA-ch10.35

A plan declares three steps with no prerequisites: "analyze", "load" and "archive". In the real world, analyze needs the file that load produces. A function orders the steps by sorted id within each batch of ready steps. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The function has no way to know what each step requires in the world.
- [ ] B. The function returns ["analyze", "archive", "load"].
- [ ] C. An acyclic graph guarantees that the declared prerequisites are the real ones.
- [ ] D. The order the function returns is not guaranteed to be executable, even though the graph has no cycle.
- [ ] E. Declaring that analyze comes after load would fix the ordering.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The function sees only the arrows it was given.
- B: With no edges all three are ready in one batch, sorted alphabetically.
- C: Acyclicity says an order exists, not that the arrows match reality.
- D: Acyclic means some order satisfies the declared arrows; it does not mean the arrows match real needs.
- E: Adding the omitted edge encodes the real dependency.

**Source:** Acyclic does not mean executable

## MA-ch10.36

A plan has three steps: inspect, delete_old_exports and verify, each declared after the one before it. An ordering function returns ["inspect", "delete_old_exports", "verify"] without error. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The graph contains an operation allowlist that would have flagged the deletion.
- [ ] B. A runtime permission boundary that denies deletion can stop the action even if review misses it.
- [ ] C. A reviewer must compare each action with the plan's scope, authority and consequences.
- [ ] D. The ordering function accepts this plan.
- [ ] E. A valid ordering implies the plan is authorized.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A dependency graph encodes order only, not which operations are allowed.
- B: Enforcing permissions at the runtime layer is a second line of defense independent of the plan review.
- C: Safety is judged by comparing what each action does with what is permitted.
- D: The chain has no cycle, so an order exists.
- E: Acyclic and authorized are different properties.

**Source:** Acyclic does not mean executable

## MA-ch10.37

A plan has two steps: "implement", which depends on "review", and "review", which depends on "implement". An ordering function raises a dependency-cycle error. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Resolving a cycle starts by asking what each step needs as input, not by deleting an arrow.
- [ ] B. Deleting the edge from review to implement is the right fix without further thought.
- [ ] C. Replacing the steps with plan_review, implement and result_review gives a valid linear order.
- [ ] D. Plan review approves a proposed method, whereas result review evaluates what was actually produced.
- [ ] E. The cycle can indicate that one word is doing two jobs: approving a proposed method and evaluating actual output.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The cycle may expose an unclear step definition, which deleting an edge would hide.
- B: Removing an edge makes the error disappear without asking what each step actually needs.
- C: Plan review precedes implementation, which precedes result review, so no cycle remains.
- D: The first judges an intention, the second judges an outcome.
- E: Review before implementation and review after implementation have different inputs.

**Source:** Acyclic does not mean executable

## MA-ch10.38

In a plan, the step "review" is declared to come after "build", and build's described output is "the work is done". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because review comes after build in the order, the reviewer has what it needs.
- [ ] B. The better fix is a more precise handoff condition on the edge, not another arrow.
- [ ] C. A reviewer can work from build's description "the work is done" alone.
- [ ] D. Adding more arrows between the same two steps would make the handoff clearer.
- [ ] E. The edge states order but does not define the handoff object.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Sequence does not guarantee the needed artifacts exist.
- B: Specifying the handoff content closes the gap, whereas arrows only order.
- C: A reviewer needs concrete artifacts such as a diff, test results and acceptance criteria.
- D: Duplicate arrows carry no additional information.
- E: An arrow says one step follows another, not what is passed between them.

**Source:** Acyclic does not mean executable

## MA-ch10.39

A team wants handoff conditions that a stranger could apply, meaning someone who did not build the pipeline can read the condition, observe the system and decide whether it holds. Check each condition that is testable in that sense. Each statement is worth 1 point (5 points total).

- [ ] A. "All 14 tests named in the ticket pass in a continuous-integration run on the commit under review."
- [ ] B. "pytest exits with status 0 and `git diff --name-only` lists only paths under src/billing/."
- [ ] C. "The summary is accurate."
- [ ] D. "The assistant reports high confidence in its work."
- [ ] E. "The code has been reviewed and looks reasonable."

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It names the tests, the environment and the commit, so any observer reaches the same verdict.
- B: An exit status and a list of changed paths are observable and decidable by anyone.
- C: Accuracy has no stated criterion or reference to compare against.
- D: A model's self-reported confidence is a statement, not an observation of the system.
- E: "Reviewed" and "reasonable" are interpretive; different people would apply them differently.

**Source:** Evidence belongs on the edges

## MA-ch10.40

A coding agent finishes a task and writes, "I ran the tests and they pass." A team is deciding what counts as evidence for moving the work to the next step. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A good check fails differently from the thing it certifies.
- [ ] B. The test runner's exit status and output are stronger evidence than the agent's description of them.
- [ ] C. A model's explanation of why it chose a step is guaranteed to reflect the computation that produced the choice.
- [ ] D. A checker whose errors tend to correlate with the errors of the thing it checks adds less independent assurance.
- [ ] E. Asking the same model to reread its own output and say it looks right is an independent check.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Independence of failure modes is what makes a second check informative.
- B: The runner's record comes from executing the code, not from the model's account.
- C: Self-explanations are plausible stories, not verified traces of internal computation.
- D: Shared blind spots mean the checker misses what the producer missed.
- E: A model checking itself repeats the same opinion and shares its blind spots.

**Source:** Evidence belongs on the edges

## MA-ch10.41

A plan defines a handoff from a test-run step to a review step. The targeted test fails when run. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The plan should define what happens when the evidence fails, not only what happens when it passes.
- [ ] B. Returning to implementation, or stopping pending diagnosis, is a reasonable route.
- [ ] C. Re-running the same command unchanged until it happens to pass, then recording the pass, is a sound policy.
- [ ] D. The agent should proceed to review anyway because review is next in the order.
- [ ] E. If a source needed by a step is unavailable, the agent should substitute a plausible replacement.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A plan written only for success pressures every observation into forward motion.
- B: A failed check should route to diagnosis or revision, not to approval.
- C: Selecting the passing run hides the failures and reports a result the code does not reliably produce.
- D: Passing a failing result to review as if it were approval undermines the check.
- E: Inventing a stand-in input hides that the real evidence is missing.

**Source:** Evidence belongs on the edges

## MA-ch10.42

An agent works in a repository under version control. One step adds a new test file. Another step runs a shell command that deletes files in a directory outside the repository. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Both steps deserve identical scrutiny because both change state.
- [ ] B. The test-file step is reversible from the diff, so it needs evidence but not necessarily a human gate.
- [ ] C. Evidence conditions should be attached first to the edges that are cheapest to undo.
- [ ] D. A clear sequence diagram makes an unsafe transition acceptable.
- [ ] E. The deletion step cannot be reverted from the diff, so it needs hard human approval or should be outside the scope.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Reversibility, cost of error and visibility of a trail all differ between the two steps.
- B: Version control makes the change cheap to undo, which lowers the cost of being wrong.
- C: State-changing edges that are hard to undo are where evidence matters most.
- D: A tidy diagram describes the order of steps; it does not make any step safe.
- E: A deletion outside version control is irreversible, so the cost of an error is high.

**Source:** Evidence belongs on the edges

## MA-ch10.43

Two teams propose AI pipelines for screening loan applications. Team 1 documents what each stage produces and the condition under which each handoff may occur. Team 2's document says only "the loan officer reviews." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Team 1's proposal can be reviewed on its substance.
- [ ] B. "Reviews" is an interpretive word that would need to be replaced with a criterion.
- [ ] C. Team 2's proposal cannot be assessed because nobody can say what the officer checks or what the pipeline does.
- [ ] D. Team 1's documentation proves that the decisions inside its pipeline are good.
- [ ] E. Handoff documentation is unnecessary when the reviewer is experienced.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated handoffs give reviewers something specific to examine and dispute.
- B: Words like "reviews" leave the actual check undefined.
- C: Without a stated check, no one can tell what the review would do.
- D: A clear map can be reviewed, but its decisions may still be wrong.
- E: Experience varies between reviewers, which is why a stated condition is needed.

**Source:** Evidence belongs on the edges

## MA-ch10.44

Handoff conditions differ in who can apply them. Example 1: "the exit status of the test command is 0." Example 2: "the cited regulatory clause actually governs the proposed change." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Example 1 can be applied by any non-author who can read the output.
- [ ] B. Marking each condition with who can apply it shows which edges lack a competent reviewer.
- [ ] C. A condition that needs a qualified reviewer is worthless.
- [ ] D. A condition that only its author can apply has not yet become a usable handoff condition.
- [ ] E. Example 2 generally needs a qualified reviewer.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: It is a mechanical observation.
- B: Naming the applicant exposes unstaffed or overloaded checks.
- C: Qualified-reviewer checks are essential for domain judgments; the point is to name who does them.
- D: A condition others cannot apply gives the handoff no independence.
- E: Whether a clause governs a change is a domain judgment.

**Source:** Computational Skepticism

## MA-ch10.45

A handoff from a test run to a review step requires: the exact commands run, their exit statuses, their output, and a hash or version description of the code that was tested. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Listing the exact commands lets the reviewer check that the checks match the proposal.
- [ ] B. A bare statement that review comes after run gives order without correspondence between what ran and what is reviewed.
- [ ] C. The exit status and output come from the test runner, not from the model.
- [ ] D. A matching hash proves the code is correct.
- [ ] E. Without identifying the code version, test results could describe an earlier state of the code.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Commands show whether the checks actually exercise the proposed behavior.
- B: The arrow orders steps but does not tie the evidence to the code under review.
- C: Evidence should be produced by a component independent of whoever wrote the code.
- D: A hash shows which code was tested, not that the code is right.
- E: Evidence for an older version can be mistaken for evidence about the current diff.

**Source:** Evidence belongs on the edges

## MA-ch10.46

A plan's stop field should define three exits: completion, halt and defer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "The turn budget is exhausted with two scoped tests still failing" is a completion condition.
- [ ] B. "The next command would write outside the permitted directory" is a halt condition.
- [ ] C. "All scoped tests pass and the named reviewer accepts the current diff" is a completion condition.
- [ ] D. Reaching a time limit should produce an incomplete status and preserved partial artifacts, and name who decides whether to resume.
- [ ] E. "Stop when it looks good" is an adequate completion exit.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: An exhausted budget is a defer case; failing tests mean the task is not complete.
- B: A boundary violation is a reason to stop before completing.
- C: It names observable outcomes and a named acceptor.
- D: A limit bounds effort without proving success, so the honest output is an incomplete status, not a fabricated finish.
- E: "Looks good" cannot be applied by someone else.

**Source:** Stop conditions and refusal paths

## MA-ch10.47

An agent run has a maximum of 30 turns and a separate finish action the agent can call. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A deadline makes it acceptable to skip verification without telling anyone.
- [ ] B. A turn limit and a finish action answer different questions: how much effort is allowed versus whether the task is complete.
- [ ] C. Partial artifacts should be preserved, and it should be stated who decides whether to resume.
- [ ] D. Reaching the limit means the task is done.
- [ ] E. Reaching the limit should yield an incomplete status, not a fabricated final result.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A reduced objective can be justified by a deadline when disclosed, but skipped verification cannot be silently accepted.
- B: The limit bounds resources; the finish action reports a claim about the task.
- C: A deferred run needs its partial work and a named decider so it can resume.
- D: Exhausting a budget is not evidence of completion.
- E: A limit says nothing about success, so reporting success would be false.

**Source:** Stop conditions and refusal paths

## MA-ch10.48

A plan's stop field assigns an owner to each exit. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A person should decide whether a newly discovered risk changes the scope.
- [ ] B. A summary of evidence is not a decision with a name on it.
- [ ] C. An automated test can own a halt that triggers on a failing assertion.
- [ ] D. If an exit has no owner, the agent should decide for itself.
- [ ] E. The decision can be handed to the model because it summarizes evidence well.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Changing scope changes what is authorized, which needs accountable judgment.
- B: A decision requires an accountable decider, which a summary lacks.
- C: A mechanical, objective trigger can be automated.
- D: An unowned exit is a defect in the plan; letting the agent fill it silently moves authority to the agent.
- E: Skill at summarizing does not confer authority or accountability.

**Source:** Stop conditions and refusal paths

## MA-ch10.49

A team adds refusal paths to an agent's plan, where refusal means that the workflow preserves its state and reports what blocks the next transition. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A refusal report should say why the step stopped, what evidence was available and what decision would allow safe resumption.
- [ ] B. An unexplained halt is hard to tell from a crashed workflow.
- [ ] C. Refusal paths should cover missing authority, unavailable evidence, out-of-scope changes and failed checks.
- [ ] D. When a source cannot support a claim, the agent should fill the field with plausible language to satisfy the checklist.
- [ ] E. When a source cannot support a claim, shrinking the claim or marking it unresolved is acceptable.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A useful stop tells a person what is blocked and what could unblock it.
- B: Without a reason, operators cannot distinguish a designed stop from a failure.
- C: These are the situations in which continuing would be unsafe or unsupported.
- D: Plausible filler satisfies the form while hiding that evidence is missing.
- E: Narrowing the claim keeps the record honest about what is supported.

**Source:** Stop conditions and refusal paths

## MA-ch10.50

An agent runs the same failing test command three times, with no change to the code, the inputs or its hypothesis, and gets the same failure each time. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Activity counts as progress only when it changes the evidence or the decision state.
- [ ] B. If the failure were random, rerunning would be expected to produce the same result every time.
- [ ] C. A better next step is to diagnose the cause, revise the plan or defer.
- [ ] D. A retry cap is a resource bound and is not evidence of success.
- [ ] E. The number of reruns is a measure of progress.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: An identical retry yields nothing new, so it is motion without progress.
- B: Random failures vary between runs, and the repeated identical failure points to a deterministic cause.
- C: Each of these changes what is known or decided.
- D: A cap limits cost but proves nothing about correctness.
- E: Repetition without new evidence is not progress.

**Source:** Stop conditions and refusal paths

## MA-ch10.51

An agent is blocked in two ways. In case 1 it lacks documentation that exists in an approved source it can search. In case 2 it lacks permission to change a production configuration. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Both cases should be handled by the same halt.
- [ ] B. In case 2 proposing a smaller task that avoids the production change is an appropriate response.
- [ ] C. In case 2 the agent can grant itself permission if it has a good reason.
- [ ] D. Missing information that can be obtained within scope differs from a decision that needs new authority.
- [ ] E. In case 1 the agent can search the approved sources, since the information is obtainable within scope.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: One case is solved by looking, the other needs a person's decision, so they need different responses.
- B: Narrowing the task is a legitimate way to continue without new authority.
- C: Permission can only be granted by whoever holds the authority, not by the party asking.
- D: The distinction determines whether the agent may proceed or must stop.
- E: Searching approved sources stays inside the authorized boundary.

**Source:** Stop conditions and refusal paths

## MA-ch10.52

A plan for reviewing a codebase produces several hundred items for human review without any prioritization. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. More review items always mean more assurance.
- [ ] B. A deadline can justify a reduced objective if the reduction is disclosed.
- [ ] C. A deadline makes skipped verification acceptable without disclosure.
- [ ] D. The plan may be structurally complete and still practically unauditable.
- [ ] E. The plan should state which items need human judgment.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Beyond reviewers' capacity, extra items reduce the chance each is examined.
- B: Disclosed scope reduction is honest; the claim shrinks to match the work.
- C: Undisclosed skipped verification misleads anyone relying on the result.
- D: Human attention is a bounded resource, and an unprioritized flood defeats review.
- E: Prioritization directs scarce judgment to the items that need it.

**Source:** Stop conditions and refusal paths

## MA-ch10.53

A team treats a plan as a set of predictions and the result as a record of what happened. Before running anything, they write down the expected observations and what a wrong outcome would look like. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A plan edited after the run to match the run has become a description of the result.
- [ ] B. The gap between the prediction and the record is where the team learns.
- [ ] C. Dating predictions before the run is analogous to preregistering a hypothesis.
- [ ] D. Predictions are unnecessary when the plan is detailed.
- [ ] E. The note describing a wrong outcome should be updated after the run to fit what happened.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Once the plan is rewritten to fit the outcome, it no longer predicts anything and the earlier review is lost.
- B: A surprise shows which assumption was wrong.
- C: Stating expectations before seeing data is the logic of preregistration.
- D: Detail is not the same as a testable prediction.
- E: Revising the failure criterion after seeing the result removes the possibility of being wrong.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.54

A plan's objective is "restore the documented behavior of the date-parsing function for all supported formats." Its verification entry is "confirm that tests/test_dates.py exists." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. When a check is a proxy, the plan should name what the check can and cannot reject.
- [ ] B. A stronger entry would run the tests and compare outputs with expected values for each supported format.
- [ ] C. The existence of the test file implies that the tests pass.
- [ ] D. There is no cross-field problem, because each field is individually nonempty.
- [ ] E. The verification is a proxy that does not measure the outcome the objective names.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Naming the proxy's limits keeps the claim honest.
- B: Running tests against expected outputs observes the claimed behavior.
- C: A file can exist and contain failing, wrong or no tests.
- D: Contradiction between fields is a defect that nonemptiness cannot show.
- E: A file existing says nothing about whether any format is parsed correctly.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.55

A plan's risks field reads "data loss; wrong output; cost overrun." No mitigation, owner or trigger is given for any of them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Assigning ownership of a risk to a fictitious person is acceptable if the plan then looks complete.
- [ ] B. A short list of risks, each tied to a mitigation, owner or trigger, can serve better than a long unconnected list.
- [ ] C. Each risk should be stated as accepted, mitigated, or a trigger for deferral or halt.
- [ ] D. A risks list can be detailed and still be disconnected from what the plan does.
- [ ] E. Risks disconnected from the plan's actions give a reviewer little to challenge.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Ownership by a nonexistent person leaves the risk unowned while appearing owned.
- B: Usefulness comes from the link between a risk and what the plan does about it.
- C: Each risk needs a stated consequence for the plan.
- D: Detail and relevance are independent.
- E: A risk that changes nothing about the work is decoration.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.56

After a plan's risk analysis and verification were written, its objective is narrowed from "migrate all tables" to "migrate only the orders table." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The supporting fields should be left unchanged for consistency with the earlier review.
- [ ] B. Narrowing an objective cannot affect verification.
- [ ] C. Reopening a plan is a normal event when it carries a recorded reason.
- [ ] D. The versions should be preserved and the relevant review rerun.
- [ ] E. The earlier risk analysis and verification may no longer match the objective.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Leaving stale fields in place creates a plan whose parts argue for different goals.
- B: Verification must test the objective actually pursued.
- C: A recorded reason makes the revision part of the design history.
- D: Keeping versions shows what changed, and rerunning review keeps supporting fields from going stale.
- E: Risks and checks written for a broader objective may be irrelevant or incomplete for the narrower one.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.57

Before approving a plan, a reviewer imagines, for each important field, a plan that satisfies the field's wording but fails its purpose. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A specific objective can still be wrong for the stakeholder.
- [ ] B. Writing one counterexample before approval and checking whether the plan rejects it is a way to test the plan.
- [ ] C. If the plan rejects the counterexample, that proves the plan cannot fail.
- [ ] D. A verification step can be executable yet test only a proxy.
- [ ] E. A stop condition can be observable and still trigger only after harm has occurred.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Specificity does not guarantee the objective serves the right person.
- B: A counterexample turns a vague worry into a concrete test of the plan.
- C: Rejecting identified counterexamples shows those failure modes were addressed, not that no others exist.
- D: An executable check may measure something other than the claim.
- E: Observability concerns detection, and detection can arrive too late.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.58

A reviewer asks an AI assistant for counterexamples to a proposed plan. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Rejected counterexamples should be kept with the reason for rejection, because a dismissal can reveal an assumption.
- [ ] B. If the plan survives the assistant's counterexamples, the plan cannot fail.
- [ ] C. The assistant can generate many counterexamples quickly.
- [ ] D. The reviewer decides which counterexamples are plausible in this context.
- [ ] E. Because the assistant has no stake in the outcome, it should decide which risks deserve load-bearing checks.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The record of why a case was dismissed shows what the plan assumes.
- B: Surviving a finite set of tests does not rule out untested failure modes.
- C: Producing volume cheaply is a good use of a model.
- D: Plausibility depends on context that the plan alone does not contain.
- E: Choosing where to put checks depends on stakes and accountability, which the assistant does not carry.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.59

A reviewer ends a plan review with a written sign-off whose lines state what was checked, how it was checked, what was not checked, what is not claimed, and whether the reviewer signs or withholds. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The "not checked" line is where the sign-off is most informative about its limits.
- [ ] B. A fluent sign-off drafted by a model is as good as one written from the reviewer's own record.
- [ ] C. Withholding a signature is an honest outcome when the evidence does not support signing.
- [ ] D. A sign-off should claim the plan is safe beyond the situations that were examined.
- [ ] E. A sign-off on a plan claims less than a sign-off on a result: it says the plan survived the described review, not that the work succeeded.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Stating what was not examined prevents readers from over-trusting the approval.
- B: Fluency is not evidence of review; the statement should come from what the reviewer actually did.
- C: A refusal to sign, with reasons, reports the state of the evidence accurately.
- D: Claims beyond what was examined are unsupported.
- E: A plan predicts action and has not yet been tested by running.

**Source:** Ship It: the reviewed plan

## MA-ch10.60

A team adopts a pre-implementation checklist. Item 1: the objective was chosen from at least three candidate formulations. Item 2: the structural check passes and a cross-field review found no contradictions. Item 3: an ordering exists and every state-changing edge has an evidence condition and a failure route. Item 4: the stop field has completion, halt and defer exits with owners. Item 5: one counterexample was written and the plan rejects it. Item 6: a named person approved the plan with a date. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Approval fixes the version being implemented, and a result that contradicts the plan reopens it.
- [ ] B. The approver in item 6 may be the model that drafted the plan.
- [ ] C. Passing the structural check alone does not satisfy item 2.
- [ ] D. Once approved, the plan is frozen.
- [ ] E. If nobody has approved the plan, its status is pending and nothing consequential runs.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A reviewed version is what gets implemented, and contradicting evidence sends it back through review.
- B: Approval is an accountable person's act; a model's sentence of approval records nothing.
- C: Item 2 requires both a structural pass and a semantic cross-field review.
- D: A plan is a versioned object that evidence may reopen.
- E: Approval is the condition for acting, and its absence leaves the plan a draft.

**Source:** The gate: a reviewed plan, before Claude implements

## MA-ch10.61

An assistant returns a plan with a persuasive explanation of why each step was chosen. A reviewer is deciding how to evaluate it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reviewer can ask the assistant to critique the reviewer's own plan, then verify each criticism against the plan and the code.
- [ ] B. The plan should be judged by what it commits to, not by how well it is argued.
- [ ] C. The reviewer should run structural checks on the returned plan.
- [ ] D. A well-argued rationale lowers the need for independent checks of the plan's commitments.
- [ ] E. A criticism stated confidently by the assistant can be accepted without checking.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Critique is useful input; verification keeps the reviewer in control.
- B: Commitments are what will be done and can be checked.
- C: A mechanical check is cheap and catches omissions.
- D: Persuasiveness is not correctness, so independent checks matter more when prose is fluent.
- E: Confidence is not evidence, and criticisms can be wrong.

**Source:** Use It: conduct Claude Code against the plan

## MA-ch10.62

A developer writes tests for a function that orders plan steps by prerequisites and raises ValueError for a duplicate id, an unknown prerequisite and a cycle. When two steps are ready at once, the function returns them sorted by id. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A single test using a linear chain of steps is enough to exercise cycle detection.
- [ ] B. A test that asserts the exact order for a diamond-shaped graph is stable only because ties are broken deterministically.
- [ ] C. A duplicate id and an unknown prerequisite deserve separate tests because they fail differently.
- [ ] D. A step that lists itself as its own prerequisite is a useful boundary case for cycle detection.
- [ ] E. An empty list of steps is a useful boundary case, and the expected result is an empty list.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A chain has no cycle, so it exercises only the success path.
- B: Independent ready steps could appear in either order unless a tie-break fixes it.
- C: Each defect has its own rejection message and remedy, so each needs its own test.
- D: A self-edge is the smallest cycle and never becomes ready.
- E: With nothing to order, the loop never runs and an empty ordering is the natural result.

**Source:** Build It: the baseline that lets you audit the plan

## MA-ch10.63

A plan's steps include "read the customer table and compute churn rates." The inputs field lists only the source files of the analysis code, and the scope field excludes personal data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A step needs information that is neither listed in inputs nor authorized by scope, so the plan is inconsistent.
- [ ] B. The plan should be revised and re-reviewed before the agent acts.
- [ ] C. The mismatch is harmless because each field is nonempty.
- [ ] D. The agent should read the table anyway and record that it did so afterward.
- [ ] E. Every step should need only information that it is authorized to use.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Cross-field review looks for exactly this kind of contradiction.
- B: Resolving the contradiction before action is cheap and keeps authority with the approver.
- C: Nonemptiness does not show that the fields agree.
- D: Acting first and documenting later turns the plan into a description of what already happened.
- E: A step should not rely on data that the plan does not authorize.

**Source:** Review before action: a plan predicts, a result records
