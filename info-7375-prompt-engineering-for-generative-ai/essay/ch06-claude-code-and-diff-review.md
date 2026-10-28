# Chapter 6: Claude Code and diff review

## ES-ch06.1

The chapter's opening compares three functions against the rule "return the input plus one": `old(x)` returns `x - 1`, `inadequate_patch(x)` returns `3`, and `intended_patch(x)` returns `x + 1`. Compute what each returns for inputs two and five, then say which of them would pass a regression test that contains only `assert candidate(2) == 3`, and what that result shows about the test.

**Points:** 5

**Rubric (1 point each):**

1. States that `old` returns 1 for input two and 4 for input five.
2. States that `inadequate_patch` returns 3 and 3, and that `intended_patch` returns 3 and 6 (the expected results are 3 and 6).
3. Concludes that both `inadequate_patch` and `intended_patch` pass the input-two-only test, while `old` fails it.
4. Explains that input five separates them, because the constant returns 3 where 6 is expected.
5. Concludes that the input-two test does not distinguish the intended function from a convenient constant, so one green test does not prove the intended rule has been restored.

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## ES-ch06.2

The opening says of the constant-three patch: "Every step was performed, and the claim still does not hold." List the steps the recipe got right, explain why the claim still fails, and state the question the chapter asks instead of "what are the steps of a code review?"

**Points:** 5

**Rubric (1 point each):**

1. Names the steps performed: the defect was reproduced, a test was written, and a patch was proposed.
2. Names the remaining steps: the test passed and the changed line (the diff) was small.
3. Explains that the claim still fails because the patch returns the constant three, which works for test input two and fails for five.
4. Notes that nothing about the patch's size reveals the defect and that one green test does not prove the intended rule has been restored.
5. States the chapter's question: what did the green test actually test, who decided that, and when?

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## ES-ch06.3

Chapter 1 named three jobs that stay with you when Claude does the fast work. Name them, give the device attached to each, and say what each job means at the scale of this chapter's code-review work.

**Points:** 5

**Rubric (1 point each):**

1. Names the three jobs as conduct, check, and drive, with their devices as the gate, the sign-off, and the driver's seat.
2. Conducting: the reproduction, the regression test, and the scope exist before the patch does.
3. Checking: you write down what you suspect before you run the check.
4. Checking: the evidence, not the last sentence of Claude's report, decides between accept, revise, and reject.
5. Driving: the scope decision and the merge are yours.

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## ES-ch06.4

Explain the sense in which this chapter "moves from the file boundary to the content boundary," what Chapter 5 had established, and why the chapter says not to compete with Claude Code on speed.

**Points:** 5

**Rubric (1 point each):**

1. States that Chapter 5 established that an authorized path can still receive a bad change.
2. States that this chapter moves from the file boundary to the content boundary, where the three jobs meet code you did not write.
3. Notes that Claude Code can read a repository, propose a plan, edit files, and run commands faster than you can read the result.
4. States that you should not compete with that speed.
5. Says what you do instead: conducting (reproduction, test, scope before the patch), checking (writing down what you suspect before the run), and driving (owning scope and the merge).

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## ES-ch06.5

Before running a check on a patch, the chapter asks you to record four things and keep the record intact. Name the four things and explain why the record must not be rewritten after the run.

**Points:** 5

**Rubric (1 point each):**

1. Names the verdict.
2. Names the target (what the check should hunt for).
3. Names the suspected mechanism.
4. Names what would change your view.
5. Explains that the record must stay intact so the result can be compared with the prediction and any gap remains visible as the learning; rewriting it afterward destroys that comparison.

**Source:** What you will be able to do

## ES-ch06.6

A teammate files the bug report "the result is wrong." Explain why that is too weak to guide a bounded change, what the first useful artifact is, and why the decision about acceptable evidence has to be made before any patch exists.

**Points:** 5

**Rubric (1 point each):**

1. Says the report names no input.
2. Says it names no expected result or observed result.
3. Says it names no scope.
4. Identifies the reproduction as the first useful artifact: the smallest legitimate case that shows the gap between intended and current behavior.
5. Explains that the decision must be made while no patch exists, because a patch shapes how you see the problem the moment you read it.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.7

Using the example `old(2) == 1` against the rule "return input plus one," distinguish behavior evidence from inspection evidence and explain why the packet should keep them apart.

**Points:** 5

**Rubric (1 point each):**

1. States that the rule plus one gives an expected result of three for input two.
2. Identifies the observation `old(2) == 1` as behavior evidence: it contradicts the stated requirement.
3. Identifies reading the source and finding the `x - 1` expression as inspection evidence of the cause.
4. States that reproducing a defect is not the same as proving its cause.
5. States that the two kinds of evidence should be kept apart in the packet.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.8

A learner's packet records only one command: `assert candidate(2) == 3` passes. What claim does that packet support, what does it not show, and what single change to the test would reject the constant-three repair? Does that change prove the function correct?

**Points:** 5

**Rubric (1 point each):**

1. States that the packet supports only the claim that the candidate returns three for input two.
2. States that the case did not separate the intended function from every wrong one, because both the constant and `x + 1` pass it.
3. Says that adding input five (expected six) makes the constant patch fail, because it returns three.
4. Says that the two-input pair still does not prove correctness for all Python inputs.
5. Says the pair rejects the demonstrated constant repair, so the evidence supports a narrower claim than "completely fixed."

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.9

Compare three regression tests for the same patch: one written after you have read the patch, one that Claude writes alongside its own patch, and one that you write first from the rule. For each, say what weakness or strength the chapter identifies.

**Points:** 5

**Rubric (1 point each):**

1. Test written after the patch: it is shaped by the patch, so you check the cases the patch handles.
2. Test written after the patch: the expected values are taken from what the patch returns, so it is a retrospective blessing.
3. Test Claude writes alongside its patch: the two share an author, so a misunderstanding of the requirement sits on both sides of the comparison and cancels out.
4. Test written first by you from the rule: it represents the expected behavior, so the patch is what is on trial.
5. Adds that the test written first is still your design and can still be incomplete.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.10

Describe the reviewer's habit of asking which different implementation could pass the current test. Apply it to the two-input test: what does that test still leave open, and how should you word the claim without inventing a specification?

**Points:** 5

**Rubric (1 point each):**

1. States the habit: ask which different implementation could pass the current test.
2. Notes that one plausible counterexample is enough to show the evidence supports a narrower claim than "the bug is completely fixed."
3. Names one open question of the two-input test: which input types are supported or what happens at boundary values.
4. Names the other open question: whether the function belongs to a larger invariant.
5. States that, because the exercise supplies no complete specification, the claim should say the selected checks cover the declared integer examples and the transformation they illustrate, without inventing more.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.11

In the vocabulary of Conducting AI, the chapter's gate is a phase gate. Define a phase gate, explain why the gate is the part of the work Claude cannot do for you, and say when it is written and what it must record about who decided.

**Points:** 5

**Rubric (1 point each):**

1. Defines a phase gate as a specific, testable condition that must hold before the output moves downstream.
2. Says the gate is where your understanding of the requirement goes on the record.
3. Concludes from this that Claude cannot do the gate for you.
4. Says the gate is written before you ask Claude for a plan.
5. Says the gate names who decided each item (in the exercise, the author's own choices, with no model producing them).

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.12

State the gate's stop condition for the plus-one exercise. Give each element and say what artifact would show it was met.

**Points:** 5

**Rubric (1 point each):**

1. The patch does not move downstream until the stop condition is met.
2. The test was saved before the plan, shown by a file timestamp or a commit.
3. The plan names only allowed files.
4. The test and the existing suite have been run against the current diff.
5. The commands and exit status are recorded.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.13

Name the two wrong versions the gate's checks must catch, say which check catches each, and explain what it means if your checks cannot tell them from the right patch. Then explain why the one-sentence "what a failure looks like" must be written before you read the test output.

**Points:** 5

**Rubric (1 point each):**

1. Names the constant three as the first wrong version.
2. Names a patch that gets the arithmetic right while editing an unrelated configuration file as the second.
3. Says the test (input five) catches the constant, and the scope check against the allowed list catches the unrelated file.
4. Says that if the test and scope check cannot tell these from the right patch, the gate is not finished.
5. Says that a failure sentence written after reading the output describes the output and does not test your understanding.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.14

State what the gate's packet may claim and what it may not claim for the plus-one exercise, and give the rule, the reproduction inputs, and the allowed files that the gate's design fixed.

**Points:** 5

**Rubric (1 point each):**

1. States the rule: return the input plus one, for the declared integer examples.
2. States the reproduction inputs two and five with expected results three and six.
3. States the allowed files: `app.py` and its learner test file.
4. States the packet may claim behavior on the declared integer examples, and scope by filename.
5. States the packet cannot claim the function is correct for all inputs, or that a person approved it.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.15

The gate has a pass condition you can check before any Claude session. Describe the expected result of running your test against `old`, `inadequate_patch`, and `intended_patch`; say what to do if the results differ; and describe Claude's role in sharpening the gate.

**Points:** 5

**Rubric (1 point each):**

1. `old` fails on both inputs.
2. `inadequate_patch` fails on input five only.
3. `intended_patch` passes on both inputs.
4. If the results differ, the gate is wrong and must be fixed before anything else.
5. Claude is good at proposing the input you missed and can sharpen the gate, but what it proposes you adopt or reject.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.16

Given the unified diff that removes `return x - 1` and adds `return x + 1`, explain the hunk without treating the markers as arithmetic. State one claim the diff supports and one claim it does not.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the leading minus and plus lines are change notation, not arithmetic performed by the diff.
2. States that the diff reports a textual transformation and the reviewer connects it to expected behavior.
3. Explains the changed expression: replacing subtraction with addition changes the rule from one below x to one above x.
4. Notes that this explanation transfers across inputs, while "the plus sign looks right" does not.
5. Gives a claim the diff does not support, such as that it runs the code, proves either string came from the intended repository file, or shows untracked changes omitted from the comparison.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.17

Be exact about what a diff is evidence of. Say what it shows, name three things it does not show, and say what you should record in an actual Claude Code workflow.

**Points:** 5

**Rubric (1 point each):**

1. States that it shows what text differs between two supplied strings.
2. States that it does not prove either string was loaded from the intended repository file.
3. States that it does not run the code.
4. States that it does not show untracked changes omitted from the comparison.
5. States that you should record the command and scope used to inspect changes and connect the displayed diff to the working tree.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.18

Claude can produce a large diff in seconds while your reading speed has not changed. Explain the volume trap from Irreducibly Human, say why reading faster does not solve it, and say how the gate changes what you have to read.

**Points:** 5

**Rubric (1 point each):**

1. States that generation scales with the machine and verification does not.
2. States that the gap fills with output nobody verified.
3. States that reading faster does not close the gap.
4. States that shrinking what must be read and deciding in advance what the reading is for does help.
5. Explains that a test written first and a short allowed-file list turn "read everything Claude changed" into "read these files, against this test."

**Source:** Read a diff as a behavioral proposal

## ES-ch06.19

Predict `merge_ready` and `reasons` for each call to the lesson's `review(changed, allowed, checks_passed, approved)` function: (a) `review([], ["app.py"], True, True)`; (b) `review(["app.py", "settings.cfg"], ["app.py"], False, False)`; (c) `review(["app.py"], ["app.py"], True, False)`. Say what rule governs when `merge_ready` is true.

**Points:** 5

**Rubric (1 point each):**

1. (a) `merge_ready` is false with the single reason `no changes`.
2. (b) `merge_ready` is false, and the reasons include `out of scope` because `settings.cfg` is not in the allowed list.
3. (b) The reasons also include `checks failed or absent` and `human review required`, so all three appear together.
4. (c) `merge_ready` is false with the single reason `human review required`.
5. States that `merge_ready` is true only when the reasons list is empty, and that the function accumulates every reason so more than one failed obligation stays visible.

**Source:** Scope is a testable property, not a mood

## ES-ch06.20

Explain what the filename comparison in the `review` function catches, what it cannot catch, and what you should do for renamed or generated files in a real packet.

**Points:** 5

**Rubric (1 point each):**

1. States that the set difference between changed and allowed files exposes any changed name not in the allowed set.
2. States that it does not inspect line-level scope inside an allowed file.
3. Gives the example that a patch can rewrite unrelated functions in `app.py` and still pass if `app.py` is permitted.
4. States that renamed or generated files may need a richer representation than a simple list.
5. States that in a real packet you should preserve the real diff status and explain how it maps to the simplified input, and that filename scope is useful and incomplete.

**Source:** Scope is a testable property, not a mood

## ES-ch06.21

During review, a patch reveals a legitimate dependency on a file outside the allowed list, and a teammate proposes setting the allowed list to the whole repository. Respond: what is wrong with that proposal, and what should be done instead?

**Points:** 5

**Rubric (1 point each):**

1. States that making the allowed list the whole repository erases the boundary the check was meant to enforce.
2. States that the right response is to pause and revise the scope explicitly.
3. States that design first does not mean freeze the design: a finding in the patch can reopen an earlier decision.
4. States that the decision cannot be reopened silently.
5. States that you record who widened the list, when, and why, and rerun the checks on the resulting proposal instead of pretending the file was always included.

**Source:** Scope is a testable property, not a mood

## ES-ch06.22

Claude Code reports that it must touch a configuration file to complete the fix, and the reason sounds good. Who decides whether the task grows to include that file, and why? Name what Claude can and cannot know.

**Points:** 5

**Rubric (1 point each):**

1. States that scope is a decision about the task, made before the plan, and that it is the decision on which Claude has the least context.
2. States that Claude can tell you which files it believes it must touch and why, and the reason may be good.
3. Names at least two things Claude cannot see: who else depends on that file, what is in flight on another branch, whose name is on the release.
4. States that whether the task should grow is a decision about what the change is for.
5. States that the decision stays with the person who owns the task.

**Source:** Scope is a testable property, not a mood

## ES-ch06.23

What does `checks_passed=True` mean in the `review` function, and what must the surrounding artifact supply? Explain the difference between deriving the Boolean from a packet and supplying it by hand in a fixture.

**Points:** 5

**Rubric (1 point each):**

1. States that `checks_passed=True` means the caller said so.
2. States that the function has no command, output, timestamp, or environment.
3. States that the function has no association between a check and the current diff.
4. States that the surrounding artifact must supply those, and a packet with exact commands, outputs, and exit status can derive the Boolean.
5. States that supplying True by hand in a fixture demonstrates the branch, not that a real check passed.

**Source:** Flags are claims about evidence

## ES-ch06.24

Claude Code ends a session with the message "all tests pass." Explain where that statement stands relative to `checks_passed=True`, what it lacks, and what the chapter says about finishing and succeeding.

**Points:** 5

**Rubric (1 point each):**

1. States that the message is a claim about a run.
2. States that it stands exactly where `checks_passed=True` stands.
3. States that it carries no command, output, or link to the diff you are about to merge unless you go and get them.
4. Cites Chapter 4's point about loops: finishing is not succeeding.
5. States that a tidy summary is the finish, not the evidence.

**Source:** Flags are claims about evidence

## ES-ch06.25

What does the `approved` argument of `review` require, and what does it not establish? Include what Chapter 13 will do and what a required flag does accomplish.

**Points:** 5

**Rubric (1 point each):**

1. States that the function requires literal True.
2. States that it does not authenticate a reviewer.
3. States that it does not prove the reviewer saw this version of the diff.
4. States that Chapter 13 will bind a simulated decision to a proposal fingerprint while still refusing to treat a digest as identity.
5. States that a required flag stops the caller from omitting approval, but the meaning of the value depends on the process around it.

**Source:** Flags are claims about evidence

## ES-ch06.26

The lesson's demo calls `review(["app.py"], ["app.py"], True, False)`. State the result, explain what it does and does not show, and explain what the lesson test that supplies True for approval and sees merge-ready does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. States that `merge_ready` is false with the single reason `human review required`.
2. States that this is an executed control-path result.
3. States that it is not evidence that a person declined the patch.
4. States that the lesson test supplying True and seeing merge-ready is a simulated input, not a human act.
5. States that the function aggregates conditions without generating their evidence, so integration must construct trustworthy inputs; a dashboard is only as honest as the records behind its green indicators.

**Source:** Flags are claims about evidence

## ES-ch06.27

A student says, "I audited the patch by running the tests." Diagnose what is wrong with that sentence by distinguishing the audit from verification.

**Points:** 5

**Rubric (1 point each):**

1. States that verification consults a source, such as a test run, a reference, or a recomputation.
2. States that the audit consults no source and runs on your own model of how the thing should behave.
3. States that the audit decides whether a source needs consulting at all, and what the verification should look for.
4. Identifies running the tests as verification, so verification has leaked into the audit.
5. Explains that once the test has spoken, you cannot tell whether your model fired or the test did the work.

**Source:** Audit before you verify

## ES-ch06.28

The diff shows a function specified as "input plus one" whose body is `return 3`. Write the audit record's four lines for this diff (verdict, target, mechanism, what would change your view), and say what the audit depended on.

**Points:** 5

**Rubric (1 point each):**

1. Gives the verdict as suspect.
2. Gives the target as behavior at an input other than two.
3. Gives the mechanism as an anomaly against a held model: a function that adds one must return different values for different inputs, and the body never mentions x.
4. Gives what would change the view as a second input returning input plus one, or learning that the written rule was not the rule the task needed.
5. States that the audit used one piece of knowledge, that the output depends on the input, and that learning the rule was wrong would send you back to the reproduction rather than forward to the check.

**Source:** Audit before you verify

## ES-ch06.29

A diff changes how a library call rounds a value, and you have never used the library. What does the audit chapter say your honest verdict is, where does it route you, and why must the patch's polish not fill the gap?

**Points:** 5

**Rubric (1 point each):**

1. States that your held model is silent.
2. States that the honest verdict is `cannot audit`.
3. States that you name the missing knowledge.
4. States that the verdict routes you to a source, a person who knows, or a narrower claim.
5. Explains that fluency and groundedness come from the same process and correlate only by accident, while instinct trained on people whose fluency tracked competence reads them as one signal, so polish must not stand in for the missing model.

**Source:** Audit before you verify

## ES-ch06.30

After you run the check, what should you do with the audit record, and how do you interpret agreement and disagreement between the result and your prediction? What may you not do afterward, and what is an intuition worth?

**Points:** 5

**Rubric (1 point each):**

1. States that you put the result beside the prediction.
2. States that agreement means your model is working in this corner.
3. States that disagreement means the gap is the learning.
4. States that the gap means either your model was wrong or the check was aimed at the wrong target.
5. States that you must not rewrite the record afterward, and that an intuition is a reason to investigate, not proof of a bug and not permission to skip required checks.

**Source:** Audit before you verify

## ES-ch06.31

Distinguish the gate from the audit: when is each written, what does each say, and why does each need the other?

**Points:** 5

**Rubric (1 point each):**

1. States that the gate is written before the patch exists.
2. States that the gate says what must hold.
3. States that the audit is written after you have seen this particular patch.
4. States that the audit says what you suspect about the patch.
5. States that without the gate the audit has no standard, and without the audit the gate's checks run without a question.

**Source:** Audit before you verify

## ES-ch06.32

A reviewer's note says only "Looks good." Explain why that is inadequate and rewrite it as the kind of accept sentence the chapter recommends, naming what it must contain.

**Points:** 5

**Rubric (1 point each):**

1. States that "Looks good" hides the basis of judgment.
2. States that an accept should name the version reviewed.
3. States that an accept should name the scope inspected and the checks run.
4. States that an accept should name the remaining limitations.
5. Gives a rewrite in the chapter's form, such as accepting the x+1 patch for the declared integer behavior after the two regression inputs and the existing suite passed, with broader type behavior not evaluated.

**Source:** Accept, revise, or reject

## ES-ch06.33

Classify each of these as accept, revise, or reject and justify it: (1) the constant `return 3` patch; (2) a patch that gets the arithmetic right but also edits an unrelated configuration file and passes the regression. Say what rejection does and does not claim.

**Points:** 5

**Rubric (1 point each):**

1. Classifies the constant patch as revise.
2. Justifies it: the goal remains valid and the patch is in file scope, but it demonstrates the expected result for one input and fails a second case representing the same rule.
3. States that the next action for a revise is to change the implementation or narrow the claim honestly, not to broaden approval.
4. Says the unrelated-file patch can justify rejection even if the regression passes.
5. States that rejection is a decision about the proposal as a package under the current task boundary, not a claim that every line is bad.

**Source:** Accept, revise, or reject

## ES-ch06.34

Name the verbs on the Computational Skepticism ladder from weakest to strongest, say what observe and conclude each require, and explain the editing remedy the chapter proposes for AI-written prose that reaches for strong verbs.

**Points:** 5

**Rubric (1 point each):**

1. Lists the ladder in order: hypothesize, suggest, observe, find, show, demonstrate, conclude, prove.
2. States that each verb names a posture and the minimum evidence it needs.
3. States that observe is the most defensible verb for a result from one run under stated conditions.
4. States that conclude means the motivating question is settled, with alternatives considered and rejected.
5. States that engineering evidence usually sits between observe and find while prose reaches for conclude, and the remedy is to downgrade the verb until it matches the evidence.

**Source:** Choose the verb the record supports

## ES-ch06.35

For the patch summary sentences "The patch returns three and six for inputs two and five," "The data suggest the patch implements plus one on the declared integers," "The patch completely fixes the bug," and "The patch is safe to merge," assign the verb the chapter gives, say whether the two-input record supplies the needed evidence, and explain why downgrading a verb is not cosmetic.

**Points:** 5

**Rubric (1 point each):**

1. Gives "returns three and six" as an observe sentence, needing the command, inputs, and output run on the current diff.
2. Gives "the data suggest" as a suggest sentence that the two-input record supplies, since two inputs point toward the rule and rule out the constant.
3. Gives "completely fixes" as a conclude sentence that the two-input record does not supply.
4. Says "safe to merge" is not a finding or evidence verb; it is a decision by a named reviewer with the packet attached.
5. Explains that a downgrade changes what a reader does next: a reader of conclude may merge, while a reader of suggest may ask for one more test.

**Source:** Choose the verb the record supports

## ES-ch06.36

Claude Code can write the candidates, the test, and the review policy faster than you can. Why does the chapter still have you build them yourself first, and what is your version used for afterward?

**Points:** 5

**Rubric (1 point each):**

1. States that Claude can write these functions faster than you can.
2. States that the one thing Claude cannot hand you is the ability to read its patch and hear that something is off.
3. States that this ability comes from having written the candidates, the test, and the policy yourself.
4. Quotes or paraphrases the line from Irreducibly Human that you cannot audit what you do not know.
5. States that your version is the baseline, the record of what you understood before Claude touched anything, against which you compare Claude's version by naming a difference in behavior (not line count or style).

**Source:** Build It: the baseline that lets you audit

## ES-ch06.37

The lesson has six tests. Two wrong versions of `review` are proposed: one returns `merge_ready` false for every call, and one reports `no changes` as the reason whatever the failure. Which lesson tests catch each, and what general lesson about a green suite does the chapter draw?

**Points:** 5

**Rubric (1 point each):**

1. States that tests 02 through 05 each assert only that `merge_ready` is false.
2. States that none of the six tests checks the reasons.
3. States that the always-false version is caught only by test 01.
4. States that the always-`no changes` version passes all five review tests.
5. States that a green suite reports on what the suite asserts, and the part nobody asserted is the part nobody checked.

**Source:** Build It: the baseline that lets you audit

## ES-ch06.38

Describe, in order, how you conduct Claude Code against your gate: what you hand over and withhold, what you ask for first, what you do with the plan, and what happens between the edit and the first test run.

**Points:** 5

**Rubric (1 point each):**

1. States that you give Claude the issue, the reproduction, the failing regression test, and the allowed-file list, but not your implementation.
2. States that you ask for a plan before any edit and check it against the allowed list.
3. States that a plan naming a file outside the list is a decision for you, not an assumption for Claude.
4. States that you permit a bounded edit and then read the diff and write the audit record before running anything.
5. States that only then do you run the targeted regression and existing tests on the current diff, preserving commands, outputs, and exit status.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.39

You ask Claude to propose additional test cases before it writes the patch, and later it writes another test after seeing its own patch. How should you treat each, and what should the packet record?

**Points:** 5

**Rubric (1 point each):**

1. States that each test Claude proposes before the patch is a proposal that you adopt or reject.
2. States that the packet records which tests came from Claude.
3. States that an adopted test becomes part of the gate.
4. States that a test Claude writes after seeing its own patch is evidence of what it understood.
5. States that such a test is not an independent check.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.40

After the targeted tests have run, the chapter asks for three things. Describe them, and explain what it means if Claude's deliberately wrong patch passes your tests.

**Points:** 5

**Rubric (1 point each):**

1. States that you compare Claude's patch with your baseline and name one difference in behavior.
2. Gives the two kinds of difference: a boundary it handled that you missed (a revision to your gate) or one it silently ignored (a defect your test failed to catch).
3. States that you note which of your tests failed, since a failing test is often a gap in your gate that Claude could not see because it had only what you wrote.
4. States that you ask Claude to propose a deliberately wrong patch that still passes your tests and check by hand whether it does.
5. States that if it passes, your tests were too weak and you found out cheaply, because whether your tests are enough cannot be judged by the system they are testing.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.41

The chapter cites Anthropic's Claude Code best practices, checked on 2026-09-06. State what the chapter says that guidance recommends, how the chapter maps it to artifacts, and what the chapter warns you not to claim about the local review function.

**Points:** 5

**Rubric (1 point each):**

1. States that the guidance recommends giving work executable checks.
2. States that it recommends separating exploration, planning, and implementation where appropriate.
3. States that the chapter maps these ideas to reproduction, reviewed plan, diff, and test output.
4. States that the mapping is an adaptation, and that the toy review function is not Anthropic's runtime and does not reproduce Claude Code's safeguards.
5. States that the learner should identify which human scope decision remains after every command passes.

**Source:** Use It: conduct Claude Code against your gate; Anthropics

## ES-ch06.42

Your Claude Code session is unavailable or fails partway through. What does the chapter tell you to do, what must you not do, and what must you preserve if a session did run?

**Points:** 5

**Rubric (1 point each):**

1. States that you report that the session was unavailable or failed.
2. States that you complete the offline review exercise.
3. States that you must not manufacture a plan or transcript, or replace the failed session with invented dialogue.
4. States that if a session ran, you preserve the actual transcript with the date and displayed model label.
5. States the principle that a review packet is worth more than a seamless story that conceals what did not run.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.43

The chapter says to arrange the review packet "as an argument, not a pile of screenshots." Describe the packet's contents and its order, and how checks should be attached to claims.

**Points:** 5

**Rubric (1 point each):**

1. Lists the packet's contents: issue, reproduction, plan, before-and-after diff, exact check commands and output, review notes, and merge decision.
2. States that the packet begins with the dated gate, then the pre-patch reproduction.
3. States that it then preserves the proposed plan and actual diff, then the audit record.
4. States that checks are attached to claims by identifying which behavior each command examines.
5. States that the packet ends with the decision, the sign-off, and the remaining gaps.

**Source:** Ship It: the review packet

## ES-ch06.44

"A packet is a chain, not a folder." Explain what that means, and describe what each link should correspond to.

**Points:** 5

**Rubric (1 point each):**

1. States that putting the right filenames in one directory does not guarantee that the records refer to one another.
2. States that the issue should identify the behavior the failing test reproduces.
3. States that the plan should address the issue and respect the allowed scope.
4. States that the diff should implement the reviewed plan or explain why it changed.
5. States that the test outputs should come after the current diff and the decision should name that same proposal, and that if one link points to an earlier version the packet can look complete while its argument has broken.

**Source:** A packet is a chain, not a folder

## ES-ch06.45

What identifiers should tie a packet's records to one proposal, why does chronology alone not settle correspondence, and what is "negative space" in a packet?

**Points:** 5

**Rubric (1 point each):**

1. States that a commit hash is used when a real commit exists, otherwise a saved diff digest or a dated working-tree description.
2. States that chronology does not settle correspondence, since a test run after an edit can still target the wrong module.
3. States that you record the working directory and target.
4. States that output should be kept as searchable text, because a pasted green badge without its command tells the reviewer less than it appears to.
5. Defines negative space: list the relevant checks you did not run and the files you did not inspect.

**Source:** A packet is a chain, not a folder

## ES-ch06.46

A patch's first test run fails with a syntax error in the test harness, and a later revision passes. What should the packet keep, and what can and cannot be concluded from the harness error?

**Points:** 5

**Rubric (1 point each):**

1. States that an unsuccessful run deserves the same provenance discipline as a successful one.
2. States that the packet records what version failed and which command exposed the defect.
3. States that it also records whether the failure belongs to the patch or to the test environment.
4. States that a syntax error in the harness does not show the candidate is wrong; repair the harness, rerun, and keep both records.
5. States that the earlier evidence must not be deleted once a later revision passes, because the move from failure to correction is often the strongest demonstration that the final test matters.

**Source:** Keep the failure in the record

## ES-ch06.47

Someone calls the constant-three patch foolish and says it proves AI output should not be trusted. Using the chapter, respond to both claims and explain what "evidence-based rather than AI-proof" means.

**Points:** 5

**Rubric (1 point each):**

1. States that the constant patch is not malicious and need not be called foolish.
2. States that it is a locally adequate response to one inadequate test, and many review failures arise that way.
3. States that whether Claude or a human proposes it, the diagnosis is about code and evidence, and attribution does not change what `return 3` does (it matters for the contribution record).
4. States that review should avoid both automatic deference to AI output and automatic suspicion of it.
5. Explains that "evidence-based rather than AI-proof" means the workflow does not prove AI involvement safe in general; it only exposes the proposal, scope, checks, and accountable decision so that this change can be judged.

**Source:** Keep the failure in the record

## ES-ch06.48

Walk through the chapter's worked decision for the first candidate patch, `return 3`: the scope result, the test results, the decision, and what would be wrong with setting `checks_passed` to True after the first case.

**Points:** 5

**Rubric (1 point each):**

1. States that the diff is in scope.
2. States that the input-two regression passes.
3. States that input five fails because three does not equal six.
4. States that the decision is revise, because the proposal stays within file scope but does not implement the stated transformation.
5. States that setting `checks_passed` to True on the first case alone would summarize evidence that does not match the declared behavior.

**Source:** A worked decision from beginning to end

## ES-ch06.49

For the second candidate (replace subtraction with addition), both targeted cases pass and, as a labeled fixture, the existing lesson checks pass. Why does the policy function still return `human review required` when approved is false, and why does the worked example end without a signature?

**Points:** 5

**Rubric (1 point each):**

1. States that the diff is in scope and both targeted cases produce the expected values.
2. States that the assumption that the existing lesson checks passed is only a labeled fixture.
3. States that the policy function still returns `human review required` when approved is false.
4. States that this is correct for the simulated call, because evidence is assembled but no actual person has been represented as deciding.
5. States that the book cannot synthesize the human's acceptance in advance, so the example ends with evidence sufficient for a bounded recommendation, not a fabricated signature.

**Source:** A worked decision from beginning to end

## ES-ch06.50

Change one assumption in the worked decision at a time. (a) The plus-one patch also edits an unrelated configuration file. (b) The diff is in scope and the tests pass, but the requirement was never confirmed. How should each be handled?

**Points:** 5

**Rubric (1 point each):**

1. (a) States that the behavior tests can still pass but the review function adds `out of scope`.
2. (a) States that the file should not be ignored because the arithmetic is right; inspect why it changed.
3. (a) States that you revert it or revise the scope explicitly, and rerun the checks on the resulting proposal.
4. (b) States that plus one can be implemented perfectly and still be wrong, and testing cannot repair an invalid requirement.
5. (b) States that when the requirement is in doubt, the last line of the audit record (what would change my view) tells you to reopen the gate instead of treating an exact implementation of the wrong rule as success.

**Source:** A worked decision from beginning to end

## ES-ch06.51

Describe the sign-off the chapter asks you to end the packet with: who writes its words, which lines the template includes, which line does the most work and why, and what you do if the evidence does not support signing.

**Points:** 5

**Rubric (1 point each):**

1. States that Claude can draft the words in seconds and the draft will be fluent, but you write the sign-off from your own record.
2. Names at least six of the template's lines (Proposal, Checked, How, Not checked, Not claiming, Strongest verb, Decision, Signed or withheld).
3. States that the "Not checked" line does the work.
4. Explains that an AI-written sign-off leaves it out because the system that wrote it has no record of what you did not do.
5. States that if the evidence does not support signing, withholding is an honest result, and that a decision that is only a recommendation for someone else should be labeled as one.

**Source:** The sign-off

## ES-ch06.52

Take the driver's seat rows "Setting scope" and "Running checks and summarizing." For each, say what Claude should do, what you should do, and why the human part stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Setting scope, Claude's part: report which files it needs and why.
2. Setting scope, your part: decide the allowed list and every revision to it, because you know the callers, the branches, and whose release this is.
3. Running checks, Claude's part: run commands and capture output and exit status.
4. Running checks, your part: choose which command bears on which claim, and record what was not run.
5. Running checks, why: a correct output can be about the wrong target.

**Source:** The driver's seat

## ES-ch06.53

Take the driver's seat rows "Stating the rule and the reproduction," "Writing the regression test," and "Drafting the patch." For each, say what Claude should do, what you should do, and the reason the work stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Rule: Claude proposes minimal reproductions and edge inputs and runs them; you say what the rule is and which inputs count as the defect.
2. Rule, why: the requirement lives in your task, not in the code, and Claude can implement a wrong rule perfectly.
3. Test: Claude proposes extra cases and a wrong patch that survives; you write the test before the patch and adopt or reject each proposal.
4. Test, why: a test written after the patch tends to bless it.
5. Patch: Claude plans and implements against the gate, fast; you build your own baseline first and compare the two, because you cannot audit what you have not built.

**Source:** The driver's seat

## ES-ch06.54

The chapter says to record one test case you wrote before the patch existed and one place where you changed or rejected something Claude proposed or summarized. Why must each be traceable in the record, and what does it mean if you cannot point to the evidence?

**Points:** 5

**Rubric (1 point each):**

1. States that the packet should contain one test case written before the patch existed.
2. States that the packet should contain one place where you changed or rejected something Claude proposed or summarized.
3. States that the evidence is a transcript line, a timestamp, or an edit.
4. States that if you cannot point to that evidence, the split of work happened in your head and not in the record.
5. Connects this to recording contributions by named action (for Claude: plan, code proposal, test suggestion, summary; for you: reproduction, scope, the test written before the patch, the audit record, the decision), which says more than percentages.

**Source:** The driver's seat

## ES-ch06.55

You ran a test, then made a later edit to the candidate. What does the chapter say about the earlier passing result, what should you inspect, and what happens to the audit record if the check disagreed with your prediction?

**Points:** 5

**Rubric (1 point each):**

1. States that review evidence must remain attached to the exact proposal.
2. States that a passing test from before a later edit is stale evidence for the current proposal.
3. States that you inspect the current diff after the checks.
4. States that you put the audit record beside the result.
5. States that if the check disagreed, you say which side was wrong (your model or the aim of the check) and leave the record as written.

**Source:** Verify and reflect

## ES-ch06.56

Of the gate, the audit, and the verb, suppose you skipped each in turn and the patch was the constant three. What would skipping each have cost you?

**Points:** 5

**Rubric (1 point each):**

1. Notes that the constant three passes input two and fails input five.
2. Skipping the gate: a test with only input two (written after the patch) would let the constant pass.
3. Skipping the audit: nothing would prompt you to notice that the body never mentions x, or to set the target as an input other than two.
4. Skipping the verb: a sentence like "completely fixes" would overstate the evidence, and a reader of conclude may merge.
5. Explains that the gate says what must hold before the patch, while the audit says what you suspect about this patch.

**Source:** Verify and reflect

## ES-ch06.57

The challenge exercise "A different survivor" asks you to find a wrong implementation that passes your current cases, and then to repeat the search on the lesson's `review` function. Describe what you do and give the chapter's own example of a surviving wrong `review`.

**Points:** 5

**Rubric (1 point each):**

1. States that you design a wrong implementation of the function that passes your current cases.
2. States that you add one justified test that catches it.
3. States that you explain what remains untested instead of claiming completeness.
4. States that you repeat the exercise on the lesson's `review` function by finding a wrong version that passes every lesson test.
5. Gives the chapter's example: a version of `review` that reports `no changes` as the reason whatever the failure passes all five review tests.

**Source:** Assessments - ungraded practice

## ES-ch06.58

The challenge exercise "Richer review record" asks you to propose a record that binds commands and outputs to the reviewed diff. Describe what such a record could contain, what it improves, and why it still cannot authenticate human consent by itself.

**Points:** 5

**Rubric (1 point each):**

1. Includes an identifier for the reviewed proposal: a commit hash, a saved diff digest, or a dated working-tree description.
2. Includes the command, the working directory and target, the output, and the exit status.
3. Explains that it improves the link between each check and the current diff, avoiding stale or mis-targeted evidence.
4. Explains that it still cannot authenticate human consent, because an approval value is still an asserted claim.
5. Notes that a digest or fingerprint is not identity, as Chapter 13 will still refuse to treat it.

**Source:** Assessments - ungraded practice

## ES-ch06.59

The review packet tells us what changed and which tests ran. What does it not tell us, why can a patch fail upstream even when it is tidy, and what question does Chapter 7 take up next?

**Points:** 5

**Rubric (1 point each):**

1. States that the packet does not explain which information was selected before the change was proposed.
2. States that a source-grounded task can fail upstream if the relevant passage never entered context.
3. States that this can happen even when the resulting patch is syntactically tidy.
4. States that coherence is visible in a diff, but whether the patch is grounded depends on what Claude was given.
5. States that Chapter 7 builds a tiny retrieval system (token counts to vectors, cosine similarity, ranking, an omitted synonym case) and then asks whether the selected passage actually supports the claim, which ranking cannot answer.

**Source:** Which source material reached the system?

## ES-ch06.60

According to the Computational Skepticism note, why can you not run the verb check on your own summary, and what form of peer critique does the chapter ask for? Give the chapter's example and its caution about the ladder.

**Points:** 5

**Rubric (1 point each):**

1. States that you wrote each sentence with the strongest verb that felt true, and that the feeling came from how the evidence sat in your head, which a re-read no longer has.
2. States that the mismatches you made are the ones you cannot see.
3. States that the peer's critique names the sentence, the verb, the evidence that verb requires, and the verb the record supports; "too strong" is not a critique.
4. Gives the example: "completely fixed" when the record is two inputs on one function, where "suggest" would match.
5. States that you preserve the original, the revision, and the reason, and that the ladder flattens inferential caution (suggest) and evidential strength (observe, find, show) onto one line, which is why verb ladders wobble.

**Source:** Computational Skepticism

## ES-ch06.61

According to the Conducting AI note, why does the audit demand the mechanism and not just the catch? Apply the book's follow-up question to the `return 3` case and to a rounding change in an unfamiliar library.

**Points:** 5

**Rubric (1 point each):**

1. States that a verdict you cannot explain is one you cannot teach or defend to a skeptic.
2. States that you also cannot trust it yourself, because you cannot tell whether you reasoned or merely reacted.
3. States the follow-up question: what specific knowledge made the finding possible, and would a competent generalist without it have caught the same thing?
4. For `return 3`: the answer is almost nothing, since anyone who knows the rule depends on x catches it.
5. For a rounding change in an unfamiliar library: the answer is a great deal, which tells you who must review the patch and what belongs in the sign-off's "Not checked" line.

**Source:** Conducting AI

## ES-ch06.62

The Conducting AI note closes the chapter by dividing responsibility between Claude and you around the audit. State what Claude can help with, what you remain responsible for, and what the chapter says an intuition and a passing command are each worth.

**Points:** 5

**Rubric (1 point each):**

1. States that Claude can help propose the mechanism and the test.
2. States that you remain responsible for deciding whether the evidence addresses the actual change.
3. States that you remain responsible for deciding whether the proposal stays within scope.
4. States that an intuition is a reason to investigate, not proof.
5. States that a passing command is evidence, not permission to merge.

**Source:** Conducting AI
