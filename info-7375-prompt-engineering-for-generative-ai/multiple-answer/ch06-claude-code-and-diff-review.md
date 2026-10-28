# Chapter 6: Claude Code and diff review

## MA-ch06.1

Check each statement that is true about the constructed comparison in the chapter's opening. Each statement is worth 1 point (5 points total).

- [ ] A. The same research run shows that the review function rejects a proposal when its approval flag is false.
- [ ] B. The inadequate patch returns three for both input two and input five.
- [ ] C. The inadequate patch fails on input two and passes on input five.
- [ ] D. For inputs two and five, the old function `x - 1` returns one and four.
- [ ] E. The chapter presents the comparison as a real Claude Code failure recorded in a live session.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The research run records that outcome for approved = false.
- B: The constant patch returns 3 and 3.
- C: It is the reverse: 3 equals the expected 3 at input two, and 3 does not equal the expected 6 at input five.
- D: The chapter reports 1 and 4 for inputs 2 and 5.
- E: The chapter says it is a constructed comparison against the offline review exercise, not a real Claude Code failure.

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## MA-ch06.2

Check each statement that is true about what the opening says the recipe got right and why the claim still fails. Each statement is worth 1 point (5 points total).

- [ ] A. The patch's small size is evidence that the change is safe.
- [ ] B. The chapter's question is "what did the green test actually test, who decided that, and when?"
- [ ] C. One green test is enough to show the intended rule has been restored.
- [ ] D. The chapter says the main question is "what are the steps of a code review?"
- [ ] E. The defect was reproduced, a test was written, a patch was proposed, the test passed, and the diff was small, yet the claim still does not hold.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Nothing about the patch's size reveals the defect.
- B: That is the question the chapter poses.
- C: Nothing about one green test proves the intended rule has been restored.
- D: The chapter says the question is explicitly not that one.
- E: The chapter says every step was performed and the claim still does not hold.

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## MA-ch06.3

Check each statement that is true about who writes the test and when. Each statement is worth 1 point (5 points total).

- [ ] A. A test written after the patch, to fit the patch, is a retrospective blessing.
- [ ] B. Who wrote the test matters less than the fact that it passes.
- [ ] C. A test written by the patch's author is independent evidence simply because it lives in a separate file.
- [ ] D. The requirement is supposed to come from Claude's reading of the existing code.
- [ ] E. A test that Claude writes alongside its own patch shares an author with the code, and so shares whatever that author misunderstood.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The chapter uses exactly that phrase for a test written to fit the patch.
- B: The chapter's whole question is who decided what the green test tests.
- C: Shared authorship is the problem, regardless of which file holds the test.
- D: The requirement was supposed to come first, and to come from you.
- E: A shared author means a shared misunderstanding.

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## MA-ch06.4

Check each statement that is true about the three jobs and how this chapter applies them. Each statement is worth 1 point (5 points total).

- [ ] A. Checking Claude's work means writing down what you suspect before you run the check.
- [ ] B. Chapter 1's devices for the three jobs are the gate, the sign-off, and the driver's seat.
- [ ] C. Driving means Claude decides the scope and merges once its own tests pass.
- [ ] D. The chapter advises matching Claude Code's speed by reading its results as fast as it produces them.
- [ ] E. Checking means letting the last sentence of Claude's report decide between accept, revise, and reject.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The record of suspicion comes before the run.
- B: Conduct, check, and drive each come with one of those devices.
- C: The scope decision and the merge are yours.
- D: The chapter says not to compete with Claude's speed.
- E: The evidence, not the last sentence of Claude's report, decides.

**Source:** Opening (Chapter 6 - Claude Code and diff review)

## MA-ch06.5

Check each statement that is true about what the chapter expects you to be able to do. Each statement is worth 1 point (5 points total).

- [ ] A. Explain a unified diff as changed behavior rather than decoration.
- [ ] B. Before running a check, record a verdict, a target, a suspected mechanism, and what would change your view, and keep that record intact.
- [ ] C. Trace every reason returned by the review function.
- [ ] D. Ask Claude for a patch first and write the failing behavior afterward, so the patch guides the test.
- [ ] E. Bring Chapters 4 and 5, basic Python functions, and unit tests to the chapter.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Listed among the chapter's outcomes.
- B: This is the audit record the chapter builds on.
- C: Listed among the chapter's outcomes.
- D: The failing behavior and prediction come before asking for a patch, so the patch cannot redefine the problem.
- E: These are the stated prerequisites.

**Source:** What you will be able to do

## MA-ch06.6

Check each statement that is true about reproducing a defect. Each statement is worth 1 point (5 points total).

- [ ] A. Behavior evidence and inspection evidence should be merged into a single entry in the packet.
- [ ] B. A reproduction is the smallest legitimate case that shows the gap between intended and current behavior.
- [ ] C. "The result is wrong" is too weak a bug report because it names no input, expected result, observed result, or scope.
- [ ] D. Observing `old(2) == 1` proves the cause of the defect is the `x - 1` expression.
- [ ] E. The evidence you will accept should be decided after reading the patch, so you can judge it in context.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: They should be kept apart, because reproducing a defect is not proving its cause.
- B: That is the definition given.
- C: The chapter lists exactly those missing pieces.
- D: The observation contradicts the requirement; reading the source reveals the expression.
- E: The decision has to be made while no patch exists, because a patch shapes how you see the problem.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.7

Check each statement that is true about a regression test that contains only `assert candidate(2) == 3`. Each statement is worth 1 point (5 points total).

- [ ] A. Passing at both inputs two and five proves the function is correct for all Python inputs.
- [ ] B. Even the two-input test leaves open which input types are supported, what happens at boundary values, and whether the function belongs to a larger invariant.
- [ ] C. Adding input five makes the constant patch fail.
- [ ] D. Both the constant-three patch and the `x + 1` patch pass it.
- [ ] E. A packet that records only that command supports the claim that the candidate returns three for input two, and no more.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The pair rejects the demonstrated constant repair but does not prove correctness for all inputs.
- B: The chapter lists these open questions.
- C: The constant returns 3, not the expected 6.
- D: At input two, 3 equals 3 for both.
- E: The case did not separate the intended function from every wrong one.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.8

Check each statement that is true about why the regression test is written before the proposed fix. Each statement is worth 1 point (5 points total).

- [ ] A. A test you write first from the rule is guaranteed to be complete.
- [ ] B. A test written first, from the rule, represents the expected behavior, so when the patch arrives the patch is what is on trial.
- [ ] C. A test written after seeing the patch is unaffected by the patch.
- [ ] D. When Claude writes the test alongside its own patch, a misunderstanding of the requirement sits on both sides of the comparison and cancels out.
- [ ] E. A test written first is mainly valuable because it runs faster than one written afterward.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: It is still your design and can still be incomplete.
- B: That is the point of the ordering.
- C: It is shaped by the patch: you check the cases the patch handles and take expected values from what it returns.
- D: The shared author means the error cancels out.
- E: The reason given is provenance, not speed.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.9

Check each statement that is true about the review habit of asking which different implementation could pass the current test. Each statement is worth 1 point (5 points total).

- [ ] A. Two passing inputs are enough to claim the bug is completely fixed.
- [ ] B. The habit shows that one plausible counterexample is enough to show the evidence supports a narrower claim than "the bug is completely fixed."
- [ ] C. The two-input test fully settles supported input types and boundary values.
- [ ] D. Because the exercise supplies no complete specification, the reviewer should invent one covering all input types.
- [ ] E. Figure 6.1 shows that a single test input is enough to distinguish the constant patch from `x + 1`.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: "Completely fixed" is the claim the two-input record cannot support.
- B: The chapter says exactly this about a counterexample.
- C: The two-input test leaves those questions open.
- D: The chapter says not to invent a specification.
- E: The figure shows the opposite: one test cannot distinguish both implementations.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.10

Check each statement that is true about the gate. Each statement is worth 1 point (5 points total).

- [ ] A. The gate should be written after Claude proposes its plan, so the plan can inform it.
- [ ] B. The gate's design choices for the exercise (rule, inputs, allowed files) were produced by a model.
- [ ] C. The gate is the part Claude cannot do for you, because it is where your understanding of the requirement goes on the record.
- [ ] D. In the constructed exercise, the allowed files are every file in the repository.
- [ ] E. A phase gate is a specific, testable condition that must hold before the output moves downstream.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It is written before you ask Claude for a plan.
- B: The chapter says these are the author's choices and no model produced them.
- C: The gate records your understanding of the requirement.
- D: The allowed files are `app.py` and its learner test file.
- E: That is the chapter's definition of a phase gate.

**Source:** The gate: reproduction, test, and scope, before the patch

## MA-ch06.11

Check each statement that is true about the gate's contract and stop condition. Each statement is worth 1 point (5 points total).

- [ ] A. The stop condition requires the test to have been saved before the plan, which a file timestamp or a commit can show.
- [ ] B. The regression test should fail against `old` on both inputs.
- [ ] C. The stop condition is met once Claude reports that the tests pass.
- [ ] D. The stop condition is met as soon as the plan names only allowed files, even if no check has been run.
- [ ] E. The regression test should pass against `inadequate_patch` on input five.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: That is the first element of the stop condition.
- B: The contract says the test fails against old on both inputs.
- C: Claude's report is a claim about a run, not the recorded commands and exit status.
- D: The test and existing suite must also be run against the current diff, with commands and exit status recorded.
- E: The contract says it fails against the constant patch on input five.

**Source:** The gate: reproduction, test, and scope, before the patch

## MA-ch06.12

Check each statement that is true about the wrong versions your tests must catch and the "what a failure looks like" sentence. Each statement is worth 1 point (5 points total).

- [ ] A. The failure sentence may be written after reading the test output, since it is then more accurate.
- [ ] B. The constant three is a wrong version the gate's test must catch.
- [ ] C. The failure sentence should be left undated so it can be reused.
- [ ] D. A patch with correct arithmetic that also edits an unrelated configuration file is not a concern for the gate.
- [ ] E. If the test and scope check cannot tell the wrong versions from the right patch, the gate is still finished.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Written after reading the output, it describes the output rather than testing your understanding.
- B: The chapter names it as the wrong version to catch.
- C: The sentence is dated.
- D: The chapter names that patch as a second wrong version the scope check must catch.
- E: In that case the gate is not finished.

**Source:** The gate: reproduction, test, and scope, before the patch

## MA-ch06.13

Check each statement that is true about what the packet may claim and the gate's pass condition. Each statement is worth 1 point (5 points total).

- [ ] A. The packet may claim behavior on the declared integer examples.
- [ ] B. If your test against the three candidates does not give fail on both inputs for `old`, fail on five only for `inadequate_patch`, and pass on both for `intended_patch`, the gate is wrong and should be fixed first.
- [ ] C. The packet may claim the function is correct for all inputs.
- [ ] D. The packet may claim that a person approved the patch.
- [ ] E. The packet may claim scope by filename.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: This is the first thing the packet may claim.
- B: The chapter says to fix the gate before anything else.
- C: The packet cannot claim correctness for all inputs.
- D: The packet cannot claim a person approved it.
- E: Scope by filename is the second.

**Source:** The gate: reproduction, test, and scope, before the patch

## MA-ch06.14

Check each statement that is true about reading a unified diff. Each statement is worth 1 point (5 points total).

- [ ] A. In the recorded output, the header lines are `--- before.py` and `+++ after.py`.
- [ ] B. The leading minus and plus lines are arithmetic that the diff performs on the code.
- [ ] C. "The plus sign looks right" is an equally good explanation because it transfers across inputs.
- [ ] D. When Claude Code edits your files, the diff is the thing you review, and its narration is a second-hand account.
- [ ] E. A useful review explains that replacing subtraction with addition changes the rule from one below x to one above x.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Those are the fromfile and tofile names in the recorded diff.
- B: The markers are change notation, not arithmetic.
- C: The chapter contrasts that explanation with "the plus sign looks right," which does not transfer.
- D: The chapter says the diff is the change.
- E: That explanation transfers across inputs.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.15

Check each statement that is true about what a diff is evidence of. Each statement is worth 1 point (5 points total).

- [ ] A. It shows untracked changes even when the comparison omitted them.
- [ ] B. It runs the code and reports the result.
- [ ] C. It shows what text differs between two supplied strings.
- [ ] D. In a real Claude Code workflow, you should record the command and scope used to inspect changes and connect the displayed diff to the working tree.
- [ ] E. It proves that either string was loaded from the intended repository file.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: It does not show untracked changes omitted from the comparison.
- B: It does not run the code.
- C: That is exactly what it shows.
- D: The chapter asks you to record the command and scope.
- E: It does not prove provenance of the strings.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.16

Check each statement that is true about small diffs and review effort. Each statement is worth 1 point (5 points total).

- [ ] A. Review effort should follow behavioral consequence and uncertainty, not line count.
- [ ] B. A small diff means the reviewer needs no analysis of behavior.
- [ ] C. Review effort should scale with the number of changed lines.
- [ ] D. A one-character operator change can alter every call.
- [ ] E. A small diff is a safe diff.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: That is the chapter's rule for allocating effort.
- B: Small diffs reduce reading, but small is not safe.
- C: Line count is exactly what effort should not follow.
- D: The `x - 1` to `x + 1` change is such an example.
- E: Small is not safe: a one-character change can alter every call.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.17

Check each statement that is true about the volume trap. Each statement is worth 1 point (5 points total).

- [ ] A. Irreducibly Human names the volume trap: generation scales with the machine, verification does not.
- [ ] B. Reading faster closes the gap.
- [ ] C. In the volume trap, the gap between generation and verification fills with output nobody verified.
- [ ] D. Shrinking what must be read, and deciding in advance what the reading is for, helps close the gap.
- [ ] E. The gate turns "read everything Claude changed" into "read these files, against this test."

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: This is the shape the chapter attributes to Irreducibly Human.
- B: Reading faster does not close it.
- C: Unverified output accumulates in the gap.
- D: This is the remedy named.
- E: A test written first and a short allowed-file list do this.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.18

Check each statement that is true about the lesson's `review` function. Each statement is worth 1 point (5 points total).

- [ ] A. It adds `out of scope` when any changed filename is not in the allowed set.
- [ ] B. It stops at the first failed obligation and returns only that reason.
- [ ] C. It returns a dictionary with `merge_ready` and `reasons`.
- [ ] D. The four reasons it can give are no changes, out of scope, checks failed or absent, and human review required.
- [ ] E. `merge_ready` is true when at least one of the four conditions is satisfied.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The set difference between changed and allowed names triggers it.
- B: It accumulates every reason so more than one failure stays visible.
- C: That is the return value.
- D: Those are the four strings in the code.
- E: `merge_ready` is true only when there are no reasons.

**Source:** Scope is a testable property, not a mood

## MA-ch06.19

Check each statement that is true about an empty changed list. Each statement is worth 1 point (5 points total).

- [ ] A. The function diagnoses why the changed list is empty.
- [ ] B. An empty changed list means the fix is already in place and nothing needs to change.
- [ ] C. An empty changed list is rejected.
- [ ] D. A claimed fix with no recorded file change deserves explanation, for example that the change was never applied or the wrong comparison was used.
- [ ] E. For an empty list, the function reports `out of scope`.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The function names only `no changes`; diagnosis remains outside.
- B: The chapter treats it as something needing explanation, not as success.
- C: The function adds `no changes`.
- D: The chapter gives those possible explanations.
- E: The reason is `no changes`.

**Source:** Scope is a testable property, not a mood

## MA-ch06.20

Check each statement that is true about filename scope. Each statement is worth 1 point (5 points total).

- [ ] A. Filename scope is complete, so no further review of an allowed file is needed.
- [ ] B. A patch that rewrites unrelated functions in `app.py` is flagged `out of scope` when `app.py` is permitted.
- [ ] C. The set difference exposes any changed name that is not in the allowed set.
- [ ] D. A renamed or generated file always maps cleanly onto a simple list of names.
- [ ] E. The check inspects line-level scope inside an allowed file.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The chapter calls filename scope useful and incomplete.
- B: Such a patch can pass if the file is permitted.
- C: That is what the set difference does.
- D: Such files may need a richer representation than a simple list.
- E: It does not inspect line-level scope.

**Source:** Scope is a testable property, not a mood

## MA-ch06.21

Check each statement that is true about widening the allowed list. Each statement is worth 1 point (5 points total).

- [ ] A. Making the allowed list the whole repository is a good response to the limits of filename scope.
- [ ] B. When the list is widened, record who widened it, when, and why, and rerun the checks on the resulting proposal.
- [ ] C. If the patch reveals a legitimate dependency outside the initial scope, you should pause and revise the scope explicitly.
- [ ] D. A finding in the patch can reopen an earlier design decision.
- [ ] E. The scope may be widened silently when the added file is obviously needed.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: That erases the boundary the check was meant to enforce.
- B: The chapter asks for that record and a rerun.
- C: The revision must be explicit.
- D: Design first does not mean freeze the design.
- E: It can be reopened, but not silently.

**Source:** Scope is a testable property, not a mood

## MA-ch06.22

Check each statement that is true about scope, correctness, and who decides. Each statement is worth 1 point (5 points total).

- [ ] A. A behaviorally correct patch can include an unrelated change.
- [ ] B. Whether the task should grow to include a new file stays with the person who owns the task.
- [ ] C. Claude knows who else depends on a configuration file, so it should decide whether the task grows.
- [ ] D. The review function accumulates every reason so that more than one failed obligation stays visible.
- [ ] E. A perfectly scoped patch can be wrong.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Plus one with an extra config edit is the chapter's example.
- B: It is a decision about what the change is for.
- C: Claude lacks that context, such as who depends on the file and what is in flight on another branch.
- D: Reasons are collected, not short-circuited.
- E: The constant three is in scope but wrong.

**Source:** Scope is a testable property, not a mood

## MA-ch06.23

Check each statement that is true about `checks_passed=True`. Each statement is worth 1 point (5 points total).

- [ ] A. Supplying True by hand in a fixture demonstrates the branch of the function.
- [ ] B. Supplying True by hand in a fixture shows that a real check passed.
- [ ] C. The function has no command, output, timestamp, environment, or association between a check and the current diff.
- [ ] D. It means the caller said so.
- [ ] E. A packet can contain exact commands, outputs, and exit status, and then derive the Boolean for the policy summary.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: That is all a fixture value demonstrates.
- B: A hand-supplied True shows no real check passed.
- C: The surrounding artifact must supply those things.
- D: The flag is an assertion by the caller.
- E: That is how the Boolean should be derived.

**Source:** Flags are claims about evidence

## MA-ch06.24

Check each statement that is true about Claude Code's final message that says the tests pass. Each statement is worth 1 point (5 points total).

- [ ] A. A tidy summary is the evidence needed to merge.
- [ ] B. It carries a command, output, and a link to the diff you are about to merge.
- [ ] C. It stands exactly where `checks_passed=True` stands.
- [ ] D. It is a claim about a run.
- [ ] E. Chapter 4 made the point about loops that finishing is not succeeding.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A tidy summary is the finish, not the evidence.
- B: It carries none of these unless you go and get them.
- C: Like the flag, it carries no evidence by itself.
- D: The message reports on a run you did not see.
- E: The chapter cites Chapter 4 for this.

**Source:** Flags are claims about evidence

## MA-ch06.25

Check each statement that is true about the `approved` argument. Each statement is worth 1 point (5 points total).

- [ ] A. The function requires the literal value True.
- [ ] B. The function proves the reviewer saw this version of the diff.
- [ ] C. A required flag proves a person approved.
- [ ] D. The function authenticates the reviewer.
- [ ] E. Chapter 13 will treat a digest of the proposal as proof of a person's identity.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: It must be literally True, not just truthy.
- B: It does not prove the reviewer saw this version.
- C: A required flag only stops the caller from omitting approval; its meaning depends on the surrounding process.
- D: It does not authenticate anyone.
- E: Chapter 13 binds a simulated decision to a proposal fingerprint while still refusing to treat a digest as identity.

**Source:** Flags are claims about evidence

## MA-ch06.26

Check each statement that is true about the demo call `review(["app.py"], ["app.py"], True, False)`. Each statement is worth 1 point (5 points total).

- [ ] A. It returns `merge_ready` false with the single reason `human review required`.
- [ ] B. The lesson test that supplies True and sees merge-ready is a simulated input, not a human act.
- [ ] C. The function aggregates conditions without generating their evidence.
- [ ] D. A green indicator is trustworthy regardless of the records behind it.
- [ ] E. That result is evidence that a person declined the patch.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Only the approval obligation fails in that call.
- B: No human acted in that test.
- C: That keeps the function small and testable and leaves integration to build trustworthy inputs.
- D: A dashboard is only as honest as the records behind its green indicators.
- E: It is an executed control-path result, not evidence that anyone declined.

**Source:** Flags are claims about evidence

## MA-ch06.27

Check each statement that is true about the difference between an audit and a verification. Each statement is worth 1 point (5 points total).

- [ ] A. The audit consults no source and runs on your own model of how the thing should behave.
- [ ] B. Once the test has spoken, you can still tell whether your model fired or the test did the work.
- [ ] C. The audit consults the test run to confirm your suspicion.
- [ ] D. Verification consults a source such as a test run, a reference, or a recomputation.
- [ ] E. "I audited it by running the tests" correctly describes an audit.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The audit uses your held model.
- B: After the test speaks, the two cannot be told apart.
- C: The audit consults no source.
- D: That is what makes it verification.
- E: Verification has leaked into the audit in that sentence.

**Source:** Audit before you verify

## MA-ch06.28

Check each statement that is true about the Audit-First Protocol. Each statement is worth 1 point (5 points total).

- [ ] A. The mechanism explains why the output drew your attention, or failed to.
- [ ] B. The verdict answers whether the output needs verification.
- [ ] C. "Check the whole thing" is an acceptable target.
- [ ] D. A complete audit produces a verdict, a target, and a mechanism, in that order.
- [ ] E. Its inviolable rule is to render the verdict and name the mechanism before any lookup.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: That is the definition of the mechanism.
- B: The verdict is "does this need verification?"
- C: A target must say what the verification should hunt for.
- D: The order is verdict, target, mechanism.
- E: That is the one inviolable rule.

**Source:** Audit before you verify

## MA-ch06.29

Check each statement that is true about mechanisms and the fourth line of the audit record. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter treats that split as an established taxonomy of expert intuition.
- [ ] B. The fourth line is filled in after the results, once you know which evidence mattered.
- [ ] C. The book names two mechanisms: pattern recognition and anomaly detection against a held model.
- [ ] D. The audit record is written after reading the plan and diff and before running a command against them.
- [ ] E. The fourth line asks you to state which verb the record supports.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The book labels the split a teaching scaffold, not an established taxonomy.
- B: It commits you to what evidence would count before you see any.
- C: Those are the two named.
- D: That is the stated timing.
- E: The fourth line asks what would change your mind; the verb ladder is a separate device.

**Source:** Audit before you verify

## MA-ch06.30

Check each statement that is true about the chapter's audit of a diff whose body is `return 3` in a function specified as input plus one. Each statement is worth 1 point (5 points total).

- [ ] A. The target is behavior at an input other than two.
- [ ] B. If the rule written down turns out not to be the rule the task needed, you should go forward and run the check.
- [ ] C. The mechanism is pattern recognition, because the body looks unfamiliar.
- [ ] D. The verdict is suspect.
- [ ] E. The audit used one piece of knowledge: that the output depends on the input.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: That is the target.
- B: That finding sends you back to the reproduction, not forward to the check.
- C: The mechanism is anomaly against a held model, because the body never mentions x.
- D: The chapter's verdict is suspect.
- E: Without that knowledge the audit goes silent.

**Source:** Audit before you verify

## MA-ch06.31

Check each statement that is true about the `cannot audit` verdict. Each statement is worth 1 point (5 points total).

- [ ] A. Fluency and groundedness come from the same process and correlate only by accident.
- [ ] B. If a diff changes how a library call rounds a value and you have never used the library, your model is silent.
- [ ] C. The patch's polish can stand in for the model you lack.
- [ ] D. The honest verdict then is `cannot audit`, naming the missing knowledge.
- [ ] E. That verdict routes you to a source, a person who knows, or a narrower claim.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The book's argument is that your instinct nevertheless reads them as one signal.
- B: Your held model has nothing to compare against.
- C: You may not let polish substitute for the model you lack.
- D: Naming the missing knowledge is part of the verdict.
- E: Those are the three routes the chapter gives.

**Source:** Audit before you verify

## MA-ch06.32

Check each statement that is true about keeping and using the audit record. Each statement is worth 1 point (5 points total).

- [ ] A. After a disagreement, revise the record so it reflects what you meant.
- [ ] B. A strong intuition is permission to skip required checks.
- [ ] C. If the check agrees with the prediction, your model is working in this corner.
- [ ] D. After the run, put the result beside the prediction.
- [ ] E. If the check disagrees, the gap is the learning: either your model was wrong or the check was aimed at the wrong target.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Do not rewrite the record afterward.
- B: An intuition is a reason to investigate, not permission to skip checks.
- C: Agreement is a sign your model is working there.
- D: That is the comparison the chapter asks for.
- E: Those are the two possible explanations.

**Source:** Audit before you verify

## MA-ch06.33

Check each statement that is true about the gate and the audit. Each statement is worth 1 point (5 points total).

- [ ] A. The gate is written before the patch exists and says what must hold.
- [ ] B. Without the audit, the gate's checks run without a question.
- [ ] C. The gate and the audit do the same job, so one of them can be skipped.
- [ ] D. Without the gate, the audit has no standard.
- [ ] E. The audit is written after you have seen this particular patch and says what you suspect about it.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: That is the gate's timing and purpose.
- B: The audit supplies the question.
- C: They do different jobs.
- D: The gate supplies the standard.
- E: That is the audit's timing and purpose.

**Source:** Audit before you verify

## MA-ch06.34

Check each statement that is true about an accept decision. Each statement is worth 1 point (5 points total).

- [ ] A. Accepting means the patch is verified correct for all inputs.
- [ ] B. An accept decision should name the version reviewed, the scope inspected, the checks run, and the remaining limitations.
- [ ] C. "Looks good" is a sufficient accept decision because it is short.
- [ ] D. The chapter's example accept sentence claims correct behavior for all Python inputs.
- [ ] E. The decision follows the gate, the audit, and the executed checks, not the last sentence Claude Code printed.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The example accepts only the declared integer behavior.
- B: That is the content of a good accept.
- C: "Looks good" hides the basis of judgment.
- D: It states that broader type behavior was not evaluated.
- E: Those three records are what the decision rests on.

**Source:** Accept, revise, or reject

## MA-ch06.35

Check each statement that is true about revise and reject. Each statement is worth 1 point (5 points total).

- [ ] A. After a revise, the next action is to broaden approval.
- [ ] B. Revise is appropriate when the goal remains valid but the evidence or implementation is insufficient.
- [ ] C. The constant patch is a clean revise case.
- [ ] D. Rejection claims that every line in the proposal is bad.
- [ ] E. An unrelated file change can justify rejection even if the regression passes.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The next action is to change the implementation or narrow the claim honestly.
- B: That is the chapter's condition for revise.
- C: It passes input two but fails a second case for the same rule.
- D: Rejection is a decision about the proposal as a package under the current task boundary.
- E: Reject concerns scope, requirement, or risk, not only test results.

**Source:** Accept, revise, or reject

## MA-ch06.36

Check each statement that is true about who owns the accept, revise, or reject outcome. Each statement is worth 1 point (5 points total).

- [ ] A. Claude cannot summarize evidence or challenge a rationale.
- [ ] B. Once Claude has proposed a recommendation, the reviewer's job is only to relay it.
- [ ] C. These labels are human review outcomes.
- [ ] D. Claude's recommendation counts as the decision once it is stated.
- [ ] E. The AI should invent these labels on behalf of a person when that is convenient.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Claude can summarize evidence, challenge a rationale, and propose a recommendation.
- B: The responsible reviewer owns the decision where the workflow assigns that responsibility.
- C: The chapter says so directly.
- D: A recommendation is not a decision.
- E: They are not values the AI should invent for a person.

**Source:** Accept, revise, or reject

## MA-ch06.37

Check each statement that is true about the verb ladder. Each statement is worth 1 point (5 points total).

- [ ] A. Observe is the most defensible verb for a result from one run under stated conditions.
- [ ] B. Engineering evidence usually sits between conclude and prove.
- [ ] C. The ladder is a universal scale of certainty.
- [ ] D. Conclude means the motivating question is settled, with alternatives considered and rejected.
- [ ] E. Weakest to strongest, the ladder runs hypothesize, suggest, observe, find, show, demonstrate, conclude, prove.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: One run under stated conditions supports observe.
- B: The chapter says engineering evidence usually sits between observe and find.
- C: It is the author's editorial instrument, not a universal scale.
- D: That is the minimum evidence for conclude.
- E: That is the frozen order.

**Source:** Choose the verb the record supports

## MA-ch06.38

Check each statement that is true about the chapter's table of patch-summary sentences. Each statement is worth 1 point (5 points total).

- [ ] A. "The data suggest the patch implements plus one on the declared integers" is a suggest sentence that the two-input record supplies.
- [ ] B. The two-input record supplies the evidence that "The patch completely fixes the bug" requires.
- [ ] C. "The patch is safe to merge" belongs to a person, a named reviewer with the packet attached.
- [ ] D. "The patch is safe to merge" is an evidence verb.
- [ ] E. "The patch returns three and six for inputs two and five" is an observe sentence that needs the command, inputs, and output, run on the current diff.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Two inputs point toward the rule and rule out the constant.
- B: Conclude needs alternatives rejected, the input domain covered, the suite run, and scope confirmed.
- C: It is a decision, not an evidence verb.
- D: The table marks it as not a finding.
- E: The record supplies it, if it was run after the last edit.

**Source:** Choose the verb the record supports

## MA-ch06.39

Check each statement that is true about downgrading a verb and about speed versus inspectability. Each statement is worth 1 point (5 points total).

- [ ] A. A reader of "suggest" may ask for one more test.
- [ ] B. A reader of "conclude" may merge.
- [ ] C. The chapter establishes criteria for removing human review once the evidence is strong.
- [ ] D. Replacing "completely fixes" with "the data suggest" can change what a reader does next.
- [ ] E. Manual review becomes ceremonial when the evidence is weak or the volume exceeds attention.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Weaker verbs invite more checking.
- B: Strong verbs invite action.
- C: The chapter says it has not established such criteria.
- D: A downgrade is not cosmetic.
- E: The remedy is to improve the packet and the scope.

**Source:** Choose the verb the record supports

## MA-ch06.40

Check each statement that is true about why you build the baseline yourself. Each statement is worth 1 point (5 points total).

- [ ] A. "You cannot audit what you do not know" is a line from Computational Skepticism.
- [ ] B. After building it, you should compare your version with the reference by line count and style.
- [ ] C. You build them anyway because the ability to read its patch and hear that something is off cannot be handed to you by Claude.
- [ ] D. Your version is the baseline: the record of what you understood before Claude touched anything.
- [ ] E. Claude Code can write the candidates, the test, and the policy faster than you can.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The chapter attributes the line to Irreducibly Human.
- B: Name a difference in behavior, not in line count or style.
- C: That ability comes from having written them yourself.
- D: It is also the instrument you measure Claude's version against.
- E: The chapter grants the speed.

**Source:** Build It: the baseline that lets you audit

## MA-ch06.41

Check each statement that is true about the lesson's six tests and the two wrong versions of `review`. Each statement is worth 1 point (5 points total).

- [ ] A. A green suite reports on what the suite asserts, and the part nobody asserted is the part nobody checked.
- [ ] B. None of the six tests checks the reasons.
- [ ] C. A version of `review` that returns `merge_ready` false for every call is caught only by test 01.
- [ ] D. Tests 02 through 05 each assert only that `merge_ready` is false.
- [ ] E. A version that reports `no changes` as the reason whatever the failure is caught by the lesson tests.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is the chapter's lesson at lesson scale.
- B: None of the six checks the reasons.
- C: Only the positive case catches the always-false version.
- D: The chapter says so.
- E: That version passes all five review tests.

**Source:** Build It: the baseline that lets you audit

## MA-ch06.42

Check each statement that is true about how to hand the work to Claude Code. Each statement is worth 1 point (5 points total).

- [ ] A. You may ask Claude to propose additional test cases before it writes the patch.
- [ ] B. Put the issue, the reproduction, the failing regression test, and the allowed-file list where Claude Code can read them.
- [ ] C. Ask for a plan before any edit and check it against the allowed list.
- [ ] D. A plan that names a file outside the list is an assumption Claude may make.
- [ ] E. Hand Claude your implementation so it can match your approach.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Each proposed test is something you adopt or reject.
- B: That is the gate you hand over.
- C: Plan first, then edit.
- D: Such a plan is a decision for you, not an assumption for Claude.
- E: The chapter says not to hand it your implementation.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.43

Check each statement that is true about the order of work and the status of tests in the Use It section. Each statement is worth 1 point (5 points total).

- [ ] A. Run the targeted tests first and write the audit record afterward, so the record reflects the result.
- [ ] B. After the audit record, run the targeted regression and existing tests on the current diff, preserving commands, outputs, and exit status.
- [ ] C. After a bounded edit, read the diff and write the audit record before running anything.
- [ ] D. An adopted test becomes part of the gate.
- [ ] E. A test Claude writes after seeing its own patch is an independent check.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: That order defeats the audit's purpose.
- B: Evidence must attach to the current diff.
- C: The audit comes before the run.
- D: The packet records which tests came from Claude.
- E: It is evidence of what Claude understood, not an independent check.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.44

Check each statement that is true about what to do after Claude's patch and your checks. Each statement is worth 1 point (5 points total).

- [ ] A. Compare Claude's patch with your baseline and name one difference in behavior.
- [ ] B. Whether your tests are enough can be judged by the system they are testing.
- [ ] C. A difference can be one Claude silently ignored, which is a defect your test failed to catch.
- [ ] D. If a deliberately wrong patch that Claude proposes still passes your tests, your tests were too weak.
- [ ] E. A difference can be a boundary Claude handled that you missed, which is a revision to your gate.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The comparison is by behavior.
- B: That cannot be judged by the system under test.
- C: The test missed a defect.
- D: You found that out cheaply.
- E: The gate gets revised.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.45

Check each statement that is true about Anthropic's best practices and an unavailable Claude session. Each statement is worth 1 point (5 points total).

- [ ] A. It also recommends separating exploration, planning, and implementation where appropriate.
- [ ] B. The chapter cites Claude Code best practices, checked during research on 2026-09-06, as recommending executable checks.
- [ ] C. If a session ran, preserve the actual transcript with the date and displayed model label.
- [ ] D. The toy review function is Anthropic's runtime.
- [ ] E. If the Claude session is unavailable, report that and complete the offline exercise instead of manufacturing a plan or transcript.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: This is the second recommendation cited.
- B: The chapter gives the check date.
- C: The date and model label belong in the record.
- D: The mapping is an adaptation; the toy function is not Anthropic's runtime.
- E: The chapter forbids invented dialogue.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.46

Check each statement that is true about the review packet's contents and how contributions are recorded. Each statement is worth 1 point (5 points total).

- [ ] A. The packet begins with the merge decision and then works backward to the gate.
- [ ] B. Contributions recorded by named action say more than percentages, unless the assignment separately requires an estimate.
- [ ] C. The packet should be arranged as an argument, not a pile of screenshots.
- [ ] D. Claude's contributions are best recorded as percentages.
- [ ] E. The artifact brief asks for issue, reproduction, plan, before-and-after diff, exact check commands and output, review notes, and merge decision.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It begins with the dated gate, then the pre-patch reproduction, and ends with the decision.
- B: Named actions are plan, code proposal, test suggestion, and summary for Claude.
- C: The chapter says to arrange it as an argument.
- D: The chapter prefers named actions.
- E: That is the brief's list.

**Source:** Ship It: the review packet

## MA-ch06.47

Check each statement that is true about a packet as a chain. Each statement is worth 1 point (5 points total).

- [ ] A. If one link points to an earlier version, the packet is still sound as long as all the files are present.
- [ ] B. Putting the right filenames in one directory does not guarantee that the records refer to one another.
- [ ] C. The plan should address the issue and respect the allowed scope.
- [ ] D. The issue should identify the behavior the failing test reproduces.
- [ ] E. The test outputs should come after the current diff, and the decision should name that same proposal.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The packet can look complete while its argument has broken.
- B: Presence of files is not correspondence.
- C: The plan ties to the issue and scope.
- D: The issue ties to the test.
- E: The outputs and decision tie to the current diff.

**Source:** A packet is a chain, not a folder

## MA-ch06.48

Check each statement that is true about identifiers, chronology, and negative space in a packet. Each statement is worth 1 point (5 points total).

- [ ] A. Otherwise use a saved diff digest or a dated working-tree description.
- [ ] B. Keep output as searchable text, because a pasted green badge without its command tells the reviewer less than it appears to.
- [ ] C. Use a commit hash when a real commit exists.
- [ ] D. List the relevant checks you did not run and the files you did not inspect.
- [ ] E. Chronology settles correspondence, so a test run after an edit must target the right module.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: These are the fallbacks.
- B: Searchable text beats a badge.
- C: That is the preferred identifier.
- D: The chapter calls this retaining negative space.
- E: A test run after an edit can still target the wrong module, so record the working directory and target.

**Source:** A packet is a chain, not a folder

## MA-ch06.49

Check each statement that is true about keeping the failure in the record. Each statement is worth 1 point (5 points total).

- [ ] A. After repairing the harness, rerun and keep both records.
- [ ] B. A syntax error in the harness shows that the candidate is wrong.
- [ ] C. The move from failure to correction is often the strongest demonstration that the final test matters.
- [ ] D. Once a later revision passes, delete the earlier failure evidence to keep the packet clean.
- [ ] E. An unsuccessful patch deserves the same provenance discipline as a successful one.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Both the failed and repaired runs stay in the record.
- B: A harness error does not show the candidate is wrong.
- C: The failure shows what the test caught.
- D: The chapter says not to delete the evidence.
- E: Record what version failed and which command exposed the defect.

**Source:** Keep the failure in the record

## MA-ch06.50

Check each statement that is true about how to regard the constant patch and AI involvement. Each statement is worth 1 point (5 points total).

- [ ] A. Review should avoid both automatic deference to AI output and automatic suspicion of it.
- [ ] B. "Evidence-based rather than AI-proof" means the workflow proves AI involvement safe in general.
- [ ] C. If a human rather than Claude proposed it, `return 3` would behave differently.
- [ ] D. The constant patch is not malicious and need not be called foolish.
- [ ] E. It is a locally adequate response to one inadequate test.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: That is the chapter's stance.
- B: The workflow only exposes the proposal, scope, checks, and accountable decision so this change can be judged.
- C: Attribution matters for the contribution record but does not change what `return 3` does.
- D: The diagnosis is about code and evidence.
- E: Many review failures arise that way.

**Source:** Keep the failure in the record

## MA-ch06.51

Check each statement that is true about the worked decision on the two candidate patches. Each statement is worth 1 point (5 points total).

- [ ] A. The example ends with a signature from the responsible human, recorded with the proposal version.
- [ ] B. The decision for the `return 3` candidate is reject.
- [ ] C. For the `x + 1` candidate, the policy function still returns `human review required` when approved is false.
- [ ] D. The `return 3` candidate is in scope and passes the input-two regression.
- [ ] E. It fails input five because three does not equal six.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The book cannot synthesize that event, so the example ends with a bounded recommendation, not a fabricated signature.
- B: The decision is revise.
- C: That is correct for the simulated call, since no person is represented as deciding.
- D: Its diff is in scope and input two passes.
- E: The expected value at five is six.

**Source:** A worked decision from beginning to end

## MA-ch06.52

Check each statement that is true about the two changed assumptions in the worked decision. Each statement is worth 1 point (5 points total).

- [ ] A. If the plus-one patch also edits an unrelated configuration file, the behavior tests can still pass.
- [ ] B. The right response includes inspecting why the file changed, reverting it or revising the scope explicitly, and rerunning the checks on the resulting proposal.
- [ ] C. In that case the review function adds `out of scope`.
- [ ] D. If the requirement was never confirmed, thorough tests can repair an invalid requirement.
- [ ] E. The right response is to ignore the file because the arithmetic is right.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Behavior and scope are separate obligations.
- B: Those are the steps given.
- C: The extra file is outside the allowed list.
- D: Testing cannot repair an invalid requirement; reopen the gate instead.
- E: The chapter says not to ignore it.

**Source:** A worked decision from beginning to end

## MA-ch06.53

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. If the evidence does not support signing, withholding is an honest result.
- [ ] B. If the decision is only your recommendation for someone else, present it as the final decision.
- [ ] C. The template includes Proposal, Checked, How, Not checked, Not claiming, a strongest-verb line, Decision, and Signed or withheld.
- [ ] D. Claude can draft the words of the sign-off in seconds, but you should write it from your record.
- [ ] E. The "Not checked" line is the one an AI-written sign-off tends to leave out.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A sign-off that claims more than the record supports is the failure.
- B: The chapter says to label it as a recommendation.
- C: Those are the template's lines.
- D: The draft will be fluent, which is why it must come from the record.
- E: The writing system has no record of what you did not do.

**Source:** The sign-off

## MA-ch06.54

Check each statement that is true about the first three rows of the driver's seat table. Each statement is worth 1 point (5 points total).

- [ ] A. For drafting the patch, you build your own baseline first and compare the two.
- [ ] B. For the regression test, Claude writes it before the patch and you adopt it.
- [ ] C. Stating the rule and which inputs count as the defect stays with you, because the requirement lives in your task, not in the code.
- [ ] D. A test written after the patch tends to be independent of it.
- [ ] E. Claude can propose minimal reproductions and edge inputs, and run them.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: You cannot audit what you have not built.
- B: You write the test before the patch; Claude proposes extra cases and a wrong patch that survives.
- C: Claude can implement a wrong rule perfectly.
- D: A test written after the patch tends to bless it.
- E: That is Claude's role in the first row.

**Source:** The driver's seat

## MA-ch06.55

Check each statement that is true about the last three rows of the driver's seat table and the evidence of the split. Each statement is worth 1 point (5 points total).

- [ ] A. Claude runs commands and captures output and exit status, while you choose which command bears on which claim.
- [ ] B. If you cannot point to the transcript line, timestamp, or edit that shows a test written before the patch, the split happened in your head and not in the record.
- [ ] C. A correct output can never be about the wrong target.
- [ ] D. For accept, revise, or reject, Claude can summarize evidence, challenge the rationale, and flag an overclaim.
- [ ] E. Claude should report which files it needs and why, and you decide the allowed list and every revision to it.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: You also record what was not run.
- B: The packet should record one test written first and one place you changed or rejected something.
- C: The chapter says a correct output can be about the wrong target.
- D: Your name is on the merge, so you decide, choose the verb, and sign or withhold.
- E: You know the callers, the branches, and whose release this is.

**Source:** The driver's seat

## MA-ch06.56

Check each statement that is true about the Verify and reflect section. Each statement is worth 1 point (5 points total).

- [ ] A. A passing test from before a later edit is stale evidence for the current proposal.
- [ ] B. If a check disagreed with your prediction, say which side was wrong and leave the record as written.
- [ ] C. Review evidence must remain attached to the exact proposal.
- [ ] D. A narrower verb is timid even when it accurately communicates the tested boundary.
- [ ] E. If the review function received True only in a fixture, you may leave that out of the report.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Inspect the current diff after the checks.
- B: Either your model or the aim of the check was wrong.
- C: That is the section's opening principle.
- D: A narrower verb is not timid when it matches the tested boundary.
- E: If True came only from a fixture, say so.

**Source:** Verify and reflect

## MA-ch06.57

Check each statement that is true about the Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. In the Stale check, an earlier test result remains sufficient even after you alter the candidate.
- [ ] B. The Assessments carry no points.
- [ ] C. In the Stale check, you restore the candidate by changing the reference.
- [ ] D. In the Revise the claim exercise, Claude can both list the strong verbs and judge the evidence behind them.
- [ ] E. Use the paired lesson's knowledge check, preserving your answers before viewing explanations.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The earlier result no longer justifies the current patch.
- B: They are ungraded practice.
- C: Restore through a new learner edit, not by changing the reference.
- D: Claude can list the strong verbs, but not judge the evidence behind them.
- E: Answers are preserved before explanations are viewed.

**Source:** Assessments - ungraded practice

## MA-ch06.58

Check each statement that is true about what you can now defend. Each statement is worth 1 point (5 points total).

- [ ] A. Its Booleans create evidence rather than summarize it.
- [ ] B. The review policy's four obligations are that a change exists, changed filenames stay in scope, checks are asserted as passed, and approval is asserted as present.
- [ ] C. You conducted: the reproduction, the test, the scope, and the stop condition were yours and came before the patch.
- [ ] D. A final sentence from Claude Code summarizes a run in the same way the Booleans summarize evidence.
- [ ] E. You drove: Claude proposed and implemented while you set the scope, ran your own tests, and held the merge.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The Booleans summarize evidence; they do not create it.
- B: Those are the four obligations.
- C: That is the conducting job at this scale.
- D: Both are claims, not evidence.
- E: That is the driving job at this scale.

**Source:** What you can now defend

## MA-ch06.59

Check each statement that is true about the section on which source material reached the system. Each statement is worth 1 point (5 points total).

- [ ] A. That can happen even when the resulting patch is syntactically tidy.
- [ ] B. The review packet tells you which information was selected before the change was proposed.
- [ ] C. Chapter 7 builds a tiny retrieval system using token-count vectors, cosine similarity, and ranking.
- [ ] D. A source-grounded task can fail upstream if the relevant passage never entered context.
- [ ] E. Chapter 7 will show that ranking answers whether the selected passage supports the claim.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Coherence is visible in a diff, but groundedness depends on what Claude was given.
- B: The packet shows what changed and which tests ran, not what was selected.
- C: That is the chapter's preview.
- D: Upstream selection can fail.
- E: Ranking cannot answer that; the question is left for after ranking.

**Source:** Which source material reached the system?

## MA-ch06.60

Check each statement that is true about the Computational Skepticism note on verb choice. Each statement is worth 1 point (5 points total).

- [ ] A. The ladder keeps inferential caution and evidential strength on two separate lines.
- [ ] B. You cannot run the check on your own summary, because the feeling that your verb was right came from how the evidence sat in your head.
- [ ] C. The mismatches you made are the ones you can easily see when you re-read your own summary.
- [ ] D. A peer's critique should name the sentence, the verb, the evidence that verb requires, and the verb the record supports.
- [ ] E. "Too strong" is a sufficient critique.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The ladder flattens them onto one line, which is why verb ladders wobble.
- B: A re-read no longer has that feeling's source.
- C: They are the ones you cannot see.
- D: The note gives a worked example: "completely fixed" versus "suggest."
- E: "Too strong" is not a critique.

**Source:** Computational Skepticism

## MA-ch06.61

Check each statement that is true about the Conducting AI note on the audit. Each statement is worth 1 point (5 points total).

- [ ] A. A passing command is permission to merge.
- [ ] B. The follow-up question asks what specific knowledge made the finding possible, and whether a competent generalist without it would have caught the same thing.
- [ ] C. A verdict you cannot explain is one you cannot teach, cannot defend to a skeptic, and cannot trust yourself.
- [ ] D. For `return 3`, the answer is that a great deal of specialized knowledge was needed.
- [ ] E. For a rounding change in an unfamiliar library, the answer is a great deal, which tells you who must review it and what belongs in "Not checked."

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A passing command is evidence, not permission to merge.
- B: That is the book's follow-up question.
- C: Without the mechanism you cannot tell whether you reasoned or merely reacted.
- D: For `return 3` the answer is almost nothing; anyone who knows the rule depends on x catches it.
- E: That is the chapter's contrast.

**Source:** Conducting AI
