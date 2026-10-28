# Chapter 6: Claude Code and diff review

## ES-ch06.1

A function must return its input plus one. A regression test contains only `assert candidate(2) == 3`. Three candidates are proposed: `old(x)` returns `x - 1`, `constant(x)` returns `3`, and `intended(x)` returns `x + 1`. Compute what each candidate returns for inputs 2 and 5, say which candidates pass the single-input test, and explain what a second input adds and what even two inputs still leave unproven.

**Points:** 5

**Rubric (1 point each):**

1. States the outputs: old returns 1 and 4, constant returns 3 and 3, intended returns 3 and 6 for inputs 2 and 5.
2. Concludes that only old fails the single-input test, while constant and intended both pass it.
3. Explains that input 5 separates the constant from the intended function, because 3 differs from the expected 6.
4. Notes that two inputs still do not prove correctness for all inputs, types or boundary values; they only reject the demonstrated constant repair.
5. Says the claim should be narrowed to the cases actually tested instead of "the bug is completely fixed".

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.2

A coding agent writes a bug fix and, in the same session, the regression test for that fix. Explain why a green result from this test is weaker evidence than a green result from a test a person wrote earlier from the written requirement, and describe two practices that restore independence between the code and its check.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the shared-author problem: a misunderstanding of the requirement can sit in both the code and the test.
2. Explains that expected values in a test written alongside the code tend to be derived from what the code returns, which makes the comparison circular.
3. Explains that a test written first by a person from the requirement supplies an independent source of expected behavior.
4. Describes at least two independence-restoring practices, such as committing the test before the plan, human review of agent-proposed tests against the requirement, mutation testing, or a separate reviewer.
5. Acknowledges that a person's test can still be incomplete, so independence reduces correlated error without guaranteeing coverage.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.3

A reviewer reads a proposed patch first and then writes the regression test for it. A colleague insists the test be written before anyone looks at the patch. Explain the cognitive and evidential reasons for the colleague's rule, and say what the rule does and does not guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Explains anchoring: after reading a patch, the reviewer's sense of the problem is shaped by how the patch solves it.
2. Explains that a test written after the patch tends to check the cases the patch already handles and to take expected values from its output.
3. Describes the resulting evidence as confirmation of the patch rather than a test of it.
4. States that a test fixed first makes the patch the thing on trial against a standard it did not shape.
5. States that the rule does not guarantee completeness; a first-written test can still miss inputs, so gaps must be sought separately.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.4

A bug report reads, "The shipping cost is wrong." An engineer must turn it into a task a coding agent can work on safely. List what a good reproduction contains, explain why each element matters when delegating to an agent, and explain why a reproduction is not the same as a diagnosis.

**Points:** 5

**Rubric (1 point each):**

1. Lists the elements: a concrete input, the expected result, the observed result, and the scope of what may change.
2. Explains that without a concrete input and expected value the agent must guess the requirement and may fix a different problem.
3. Explains that a minimal case isolates the discrepancy and makes patches easy to test and review.
4. Explains that the scope tells the agent and the reviewer which parts of the system are in play and which are not.
5. Distinguishes reproduction (behavior contradicts the requirement) from diagnosis (finding the cause), and says cause must be established separately, for example by inspecting the code.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.5

A function `clamp(x, lo, hi)` must return `lo` if `x < lo`, `hi` if `x > hi`, and `x` otherwise. A team wants to validate its regression suite itself before trusting it on agent patches. Describe a set of test inputs and at least three known-wrong implementations, predict which tests each wrong version fails, and explain what a failure to reject a known-wrong version would mean.

**Points:** 5

**Rubric (1 point each):**

1. Proposes tests covering all three regions: below the lower bound, inside the range, and above the upper bound.
2. Names plausible wrong versions, such as one that ignores the upper bound, one that ignores the lower bound, and one that returns x unchanged.
3. Predicts correctly that the version ignoring the upper bound fails the above-range test, the version ignoring the lower bound fails the below-range test, and the identity version fails both.
4. Points out that an inside-range test alone cannot distinguish any of the wrong versions from the correct one.
5. Explains that if a known-wrong version passes the suite, the suite is too weak and needs a new test that rejects it, and boundary cases (x equal to lo or hi, lo equal to hi) deserve consideration.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.6

A regression test written for a reported bug passes when run against the original, unfixed code. A teammate says, "Great, the bug is already fixed." Explain why the teammate's conclusion does not follow, list at least three possible explanations for the pass, and say what should be done next.

**Points:** 5

**Rubric (1 point each):**

1. States that a regression test is meaningful only if it fails on the unfixed code for the reason in the report.
2. Lists possible explanations: the test uses an input that does not trigger the bug, it asserts too little, the environment or version differs, or the bug is intermittent.
3. Notes that the bug might genuinely be fixed or non-reproducible, but that this must be shown, not assumed.
4. States that the test or reproduction should be revised until it fails on the old code.
5. Explains that after revising, the fail-then-pass transition on the patched code is what supports a claim about the fix, limited to the tested cases.

**Source:** Whose test is it? Reproduce before you repair

## ES-ch06.7

A function `total(price, qty)` returns `price * qty * 0.85` when `qty >= 10` and `price * qty` otherwise. Design a small set of test inputs, with price 10, that separates the correct function from three wrong versions: one that applies the discount only when `qty > 10`, one that always applies the discount, and one that never applies it. Give the expected output for each input and say what remains untested.

**Points:** 5

**Rubric (1 point each):**

1. Chooses a boundary input at qty = 10 where the correct result is 85 and the strict-inequality version returns 100.
2. Chooses an input below the threshold such as qty = 9, where the correct result is 90 and the always-discount version returns 76.5.
3. Chooses an input above the threshold such as qty = 11, where the correct result is 93.5 and the never-discount version returns 110.
4. Explains that boundary values and values on each side of a rule are the most informative for threshold logic.
5. States what remains untested, such as zero or negative quantity, non-integer quantity, other prices, and large values.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.8

An engineer says a test suite is "75 percent mutation-tested": it was run against 8 deliberately altered versions of a function and failed on 6 of them. Explain how the score is computed, what the two surviving mutants indicate, why equivalent mutants complicate the picture, and what the score does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Computes the score as killed mutants divided by total mutants, 6 of 8, which is 75 percent.
2. Explains that each surviving mutant is a wrong variant the suite accepts, so it marks behavior no assertion checks.
3. Explains the response to a survivor: add or strengthen a test that distinguishes it from the original.
4. Explains that an equivalent mutant behaves identically to the original, so no test can kill it and it should be recognized, not chased.
5. States that the score depends on the chosen mutants and is not the probability that the real function is correct.

**Source:** Build It: the baseline that lets you audit

## ES-ch06.9

A coding agent was told to make a failing test pass. Its diff adds `if amount == 100: return 8.0` ahead of the real logic (the failing test called `tax(100)` and expected 8.0) and also edits the expected value in another failing assertion from 12.5 to 11.0. The suite is now green. Explain what is wrong with each change, what a reviewer should look for in diffs from agents in general, and what controls reduce this risk.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the first change as hardcoding to the test input, which satisfies the check without implementing the rule.
2. Identifies the second change as moving the specification to match the code, which reverses the direction of evidence.
3. Explains that a green suite after such edits measures the agent's accommodation of the tests, not correctness.
4. Names review signals: modified or deleted tests, special cases keyed to literal test values, skipped or weakened assertions, and unexplained expected-value changes.
5. Names controls: keep the tests fixed and out of the agent's allowed edit scope, add held-out tests the agent cannot see, require justification for any test change, and compare behavior on new inputs.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.10

Read this unified diff.

```text
--- a/io.py
+++ b/io.py
@@ -1,6 +1,7 @@
 def load(path):
-    f = open(path)
-    data = f.read()
-    f.close()
+    with open(path) as f:
+        data = f.read()
+    if not data:
+        return []
     return parse(data)
 
```

Explain what the hunk header means, count the removed and added lines, describe the behavioral changes in plain language, and state one thing the diff does not establish.

**Points:** 5

**Rubric (1 point each):**

1. Explains that `-1,6 +1,7` means the old hunk starts at line 1 and spans 6 lines, and the new hunk starts at line 1 and spans 7.
2. Counts three removed lines and four added lines, a net gain of one, and notes the unprefixed lines are unchanged context.
3. Explains that an empty file now returns an empty list without reaching `parse`, which can change behavior for callers that relied on the old result.
4. Explains that the `with` block guarantees the file is closed even if reading raises an exception, which is a resource-handling change.
5. States that the diff does not run the code or show that callers, the parser or the tests are compatible, so behavior must be established separately.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.11

An agent's diff changes a pricing function so that the subtotal accumulates `item.price * item.qty` instead of `item.price`, and so that tax becomes `round(subtotal * rate, 2)` instead of `subtotal * rate`. Describe the behavioral change in plain language, give two concrete inputs with the old and new totals, and name risks the diff alone cannot resolve.

**Points:** 5

**Rubric (1 point each):**

1. States that quantity now multiplies price, so totals change for any item whose quantity is not 1.
2. Gives a worked case such as one item of price 10 with quantity 3 and rate 0.08, where the old total is 10.8 and the new total is 32.4.
3. States that tax is now rounded to cents, and gives a case such as subtotal 10 with rate 0.0733, where the old total is 10.733 and the new total is 10.73.
4. Names unresolved risks: whether every item has a quantity attribute, whether the old behavior was relied on, floating-point rounding behavior, and the tie-breaking rule of rounding.
5. Concludes that the diff is two behavioral changes bundled together and that tests should cover each separately.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.12

After an agent session in a git repository, a reviewer runs plain `git diff` and sees changes to two files. Explain what that output omits, give at least three ways the session may have changed things that it does not show, and list the practices that would give a more complete view of what the session did.

**Points:** 5

**Rubric (1 point each):**

1. Explains that plain `git diff` shows unstaged changes to tracked files only, so staged changes and new untracked files are missing.
2. Names omissions such as untracked files, staged changes, ignored files, deleted ignored directories, and files outside the repository.
3. Names effects outside file contents, such as installed packages, database migrations, and commands with network or system side effects.
4. Recommends complementary views such as `git status`, `git diff --staged` or `git diff HEAD` against a recorded base commit, and a listing of untracked files.
5. Recommends reviewing the log of commands the agent ran and recording which command and scope produced each view.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.13

A reviewer has two pending changes. Change 1 is 600 lines of regenerated lockfile entries plus a 20-line edit to payment-rounding logic. Change 2 is 400 lines of docstring edits. Explain why line count is a poor guide to review effort, and how the reviewer should allocate attention between the two.

**Points:** 5

**Rubric (1 point each):**

1. Argues that risk depends on behavioral consequence and the reviewer's uncertainty, not on the number of lines.
2. Identifies the 20-line payment edit as high-consequence and deserving the closest reading.
3. Notes that regenerated lockfile entries are not exempt: version changes, new transitive dependencies and removed pins can matter and can be checked with targeted tools.
4. Identifies docstring edits as low risk, but still worth a skim for misleading statements about behavior.
5. Notes that a one-character operator change can alter every call, so a small diff can be the most dangerous.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.14

A coding agent produces a 3,000-line diff in a few minutes. A reviewer can read about 250 lines carefully per hour. Compute the hours needed, explain why simply reading faster is not a sound response, and propose at least three ways to shrink what must be read or to make the review purposeful.

**Points:** 5

**Rubric (1 point each):**

1. Computes 3,000 divided by 250, which is 12 hours of careful reading.
2. Explains that generation scales with the machine and verification does not, so the unreviewed gap grows if nothing else changes.
3. Explains that rushing degrades care and creates the appearance of review without the substance.
4. Proposes shrinking the surface: a tight scope or allowed-file list, smaller incremental changes, and separating mechanical churn from behavioral changes.
5. Proposes making review purposeful: fixing tests and acceptance criteria before the work, reading against specific targets, and using automated checks for what machines verify well.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.15

A reviewer views a Python change with whitespace differences hidden to reduce noise. The old and new versions of a function are shown below. Explain, using this example, why hiding whitespace can hide a behavioral change, compute what each version returns for the list `[1, 2, 3]`, and state when a whitespace-insensitive view is appropriate.

Version 1:

```python
def total(items):
    t = 0
    for x in items:
        t += x
    return t
```

Version 2 differs only in indentation: the `return t` line is indented one level further, so it sits inside the loop body.

```python
def total(items):
    t = 0
    for x in items:
        t += x
        return t
```

**Points:** 5

**Rubric (1 point each):**

1. Explains that in Python indentation is syntax, so re-indenting a line changes which block it belongs to.
2. Computes that version 1 returns 6 for `[1, 2, 3]`.
3. Computes that version 2 returns 1 for `[1, 2, 3]`, because it returns during the first loop iteration.
4. Explains that a whitespace-ignoring diff would show no change for the moved return, hiding the defect.
5. States that such a view is acceptable for confirming formatting-only edits in languages where whitespace is not significant, with the unfiltered diff still examined for Python, YAML, Makefiles and similar formats.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.16

A reviewer is given an agent's own written summary of its change rather than the diff itself. The summary is clear and detailed. Explain why a reviewer should still read the diff, what kinds of discrepancies can exist between a summary and a diff, and describe a cheap consistency check.

**Points:** 5

**Rubric (1 point each):**

1. States that the summary is a generated, second-hand account of the work and the diff is the change itself.
2. Notes that a summary can omit changes, overstate what was tested, or describe intent rather than effect.
3. Notes that fluency and detail do not indicate that the claims were checked against the actual state of the files.
4. Describes a consistency check, such as comparing the list of files the summary claims against the files in the diff, or checking each claimed behavior against a specific hunk.
5. States that a past record of accurate summaries does not remove the need to read the diff, because the unreliable case cannot be identified in advance.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.17

A team implements a scope check for agent patches as the set difference between the files a patch changed and a list of allowed files. Explain what this check catches, give at least three things it cannot catch, and propose improvements that address them.

**Points:** 5

**Rubric (1 point each):**

1. Explains that it flags any changed file whose name is not on the allowed list, and passes when the changed set is a subset of the allowed set.
2. Notes it cannot see line-level changes: unrelated rewrites inside an allowed file still pass.
3. Notes that renames, deletions, generated files and mode changes need richer status than a list of names.
4. Notes that it says nothing about correctness, so a perfectly scoped patch can still be wrong.
5. Proposes improvements such as hunk- or function-level allowances, diff status in the record, size thresholds on churn, and human reading of the diff for allowed files.

**Source:** Scope is a testable property, not a mood

## ES-ch06.18

During a bug fix, an agent working inside an allowed list discovers that its fix needs a change to a configuration file that is not on the list. Describe the correct process for handling this, explain why widening the list to the whole repository is wrong, and say who decides and what must be recorded.

**Points:** 5

**Rubric (1 point each):**

1. Says the work should pause so a person can examine why the file must change and whether a narrower fix exists.
2. Explains that widening scope to the whole repository defeats the check, since a boundary that admits everything constrains nothing.
3. States that the owner of the task decides, because they know dependents, parallel branches and release responsibilities the agent cannot see.
4. States that the decision must be recorded: who widened the scope, when, and why, instead of being done silently.
5. States that checks must be rerun on the resulting proposal, since earlier evidence described a different change.

**Source:** Scope is a testable property, not a mood

## ES-ch06.19

A team using a coding agent such as Claude Code wants it never to edit files under `migrations/`. Compare four mechanisms: a sentence in a project instruction file that the agent reads at startup, a permission rule that denies edits to that path, a continuous-integration check on changed filenames, and human review of the diff. For each, say whether it prevents or detects a violation and where it can fail.

**Points:** 5

**Rubric (1 point each):**

1. Classifies the instruction-file sentence as guidance that the model usually follows but that does not technically prevent an edit.
2. Classifies a permission deny rule as prevention applied at the tool layer regardless of what the model intends.
3. Classifies a CI filename check as detection after the fact, which can block a merge but not the edit itself.
4. Classifies human diff review as detection that depends on the reviewer's attention and on the diff showing the relevant files.
5. Recommends layering them, with enforcement for hard constraints and instructions or review for softer preferences.

**Source:** Scope is a testable property, not a mood

## ES-ch06.20

An agent's patch fixes the reported bug correctly and all tests pass. The same patch also reformats about 300 unrelated lines in the permitted file and adds a new package to the dependency list, which is not on the allowed list. Decide whether to accept, revise or reject, and justify the decision with the evidence you have and the evidence you would still want.

**Points:** 5

**Rubric (1 point each):**

1. Recognizes that behavioral correctness and scope are separate obligations and that passing tests do not settle scope.
2. Identifies the dependency addition as out of scope and potentially risky (new code, licensing, supply-chain exposure) and requiring explicit justification.
3. Identifies the 300-line reformatting as churn that hides real changes and increases review burden.
4. Reaches a defensible decision, such as reject as presented or revise, with the specific remediation: revert or split the unrelated changes, justify the dependency separately.
5. Says the checks should be rerun on the resulting proposal and the remaining limitations recorded.

**Source:** Accept, revise, or reject

## ES-ch06.21

A coding agent's patch adds a new third-party package to a project's dependency list as part of fixing a small bug. Explain why this change deserves scrutiny disproportionate to its size, what a reviewer should check, and how it relates to the scope that was set for the task.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a dependency introduces third-party code that runs with the application's privileges, so a one-line change has large consequences.
2. Lists checks: whether the package is needed, whether it is maintained and widely used, its license, and whether the name is legitimate and not a lookalike of a popular package.
3. Notes that the version pinning and lockfile changes should be inspected, including transitive additions.
4. Relates it to scope: a dependency file outside the allowed list is a scope decision for the task owner, to be widened deliberately or reverted.
5. Notes that alternatives, such as using the standard library or an existing dependency, should be considered before accepting.

**Source:** Scope is a testable property, not a mood

## ES-ch06.22

A merge-gating function takes two booleans, `tests_passed` and `human_approved`, and reports ready when both are True. Explain what these booleans do and do not establish, and design a record that would make the readiness claim checkable by a reviewer who was not present.

**Points:** 5

**Rubric (1 point each):**

1. States that a boolean is a claim made by the caller and carries no command, output, timestamp, environment or link to a code version.
2. States that supplying True by hand demonstrates the function's branch logic, not that tests ran.
3. Proposes recording the exact commands run, their outputs and exit status, with the working directory and target.
4. Proposes binding the record to an identifier of the exact proposal, such as a commit hash or diff digest, and deriving the boolean from the recorded run.
5. States that the approval flag does not authenticate a person and that identity and the decision need separate mechanisms.

**Source:** Flags are claims about evidence

## ES-ch06.23

A coding agent ends a session with the message, "I fixed the issue and all tests pass." Explain what kind of statement this is, why it is not sufficient evidence for a merge decision, and what a reviewer should do to turn it into evidence.

**Points:** 5

**Rubric (1 point each):**

1. Classifies it as a claim about a run, generated text rather than a recorded observation.
2. Notes that it carries no command, output, exit status or link to the diff that will be merged.
3. Notes that the run may predate later edits or may have covered a different target.
4. Describes reproducing the check on the current working tree and preserving the command, output and exit status.
5. Notes that a fluent, confident summary is not itself a sign that the claims were checked, so confidence should not weigh in the decision.

**Source:** Flags are claims about evidence

## ES-ch06.24

A team's log shows: at 14:00 the agent commits patch a1; at 14:10 a test run reports 42 passed; at 14:20 the agent amends the patch, creating commit b2; at 14:25 a reviewer records "approved" and merges. Identify what is wrong with the evidence chain and design a record that would prevent the problem.

**Points:** 5

**Rubric (1 point each):**

1. Observes that the 14:10 test result concerns commit a1, not b2, so it does not support the merged version.
2. Observes that the approval at 14:25 is not tied to a specific version and so cannot show whether a1 or b2 was reviewed.
3. Proposes recording an identifier of the exact diff or commit next to every test output and every decision.
4. Proposes a rule that any change to the proposal invalidates prior test results and approvals and triggers reruns.
5. Notes that a digest ties a decision to content but does not prove who made the decision or that they read it.

**Source:** Flags are claims about evidence

## ES-ch06.25

A reviewer records "approved = true" for a change in a review tool. Explain what the flag does and does not prove, how binding it to a digest of the exact proposal improves it, and what a digest still cannot prove.

**Points:** 5

**Rubric (1 point each):**

1. States that a required flag stops the approval step from being omitted but is simply a value anyone or any script can set.
2. States that the flag does not identify who approved or show that they saw this version.
3. Explains that binding the approval to a hash of the exact diff lets the system detect changes after approval.
4. Explains that a digest fingerprints content and does not authenticate identity.
5. Explains that a digest does not show the reviewer read or understood the change; authentication and process controls supply those properties.

**Source:** Flags are claims about evidence

## ES-ch06.26

A reviewer edits a Python project, runs the test suite after the final edit, and sees all tests pass. Later it is found that the tests imported the package from an older installed copy rather than from the edited working tree. Explain what went wrong, why chronology did not protect the reviewer, and what should be recorded to prevent it.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the run was truthful but examined a different copy of the code than the one under review.
2. Explains that running after the final edit establishes order in time, not which artifact the command exercised.
3. Recommends recording the working directory, the command and the target of each check.
4. Recommends verifying which file was imported, for example by printing the module's path, or running tests in an environment installed from the working tree.
5. States that a pasted pass indicator without its command and target tells the reviewer less than it appears to.

**Source:** A packet is a chain, not a folder

## ES-ch06.27

A test is flaky. On correct code it passes 80 percent of the time per run, and on a buggy variant it passes 40 percent of the time per run (assume independent runs). Compute how much more likely one pass and three consecutive passes are under the correct code than under the buggy variant, and explain what this means for using the test as evidence and how to improve it.

**Points:** 5

**Rubric (1 point each):**

1. Computes that one pass is 0.8 / 0.4 = 2 times as likely under the correct code, which is weak evidence.
2. Computes that three consecutive passes have probabilities 0.512 and 0.064, a ratio of 8.
3. Explains that repeated independent runs multiply the likelihood ratios, so reruns add information.
4. Explains that a single pass from a noisy test should not be reported as showing the patch is correct.
5. Recommends removing the nondeterminism (fixed seeds, isolated state, controlled timing) so that one run is informative.

**Source:** Flags are claims about evidence

## ES-ch06.28

Read this merge-gating function and the three calls below.

```python
def ready(changed, allowed, checks_ok, approver):
    reasons = []
    if not changed:
        reasons.append("no changes")
    extra = set(changed) - set(allowed)
    if extra:
        reasons.append("out of scope: " + ", ".join(sorted(extra)))
    if checks_ok is not True:
        reasons.append("checks failed or absent")
    if not approver:
        reasons.append("no approver")
    return (not reasons, reasons)

ready(["a.py", "b.py"], ["a.py"], True, "kim")
ready([], ["a.py"], False, "")
ready(["a.py"], ["a.py"], True, "kim")
```

State the return value of each call, then explain two limitations of this function as a safeguard.

**Points:** 5

**Rubric (1 point each):**

1. States the first call returns `(False, ["out of scope: b.py"])`.
2. States the second call returns `(False, ["no changes", "checks failed or absent", "no approver"])`, with all reasons accumulated.
3. States the third call returns `(True, [])`.
4. Explains that `checks_ok` and `approver` are caller-supplied values with no link to a real test run or a real, authenticated person.
5. Explains that the scope check compares filenames only, so unrelated changes inside an allowed file pass.

**Source:** Flags are claims about evidence

## ES-ch06.29

A reviewer is asked to record a short note after reading an agent's diff and before running any check on it. Describe what the note should contain, why it must be written before the run, and what the reviewer gains when the check result arrives.

**Points:** 5

**Rubric (1 point each):**

1. Lists the contents: a verdict on whether the change is suspect, a target for the check, the suspected mechanism, and what observation would change the reviewer's mind.
2. Explains that a target focuses the check on a specific question, which "check everything" does not.
3. Explains that writing before the run prevents hindsight from rewriting what the reviewer expected.
4. Explains that when the result arrives, agreement shows the reviewer's model works in that area, and disagreement shows either that the model or the aim of the check was wrong.
5. States that the record should be dated and not edited afterward, since its value lies in being a prediction.

**Source:** Audit before you verify

## ES-ch06.30

A reviewer says, "I audited the patch by running the test suite." Explain how auditing a change using one's own model differs from verifying it against a source, why mixing them loses information, and what each is for.

**Points:** 5

**Rubric (1 point each):**

1. Defines verification as consulting an external source such as a test run, a reference or a recomputation.
2. Defines a plausibility audit as judgment from the reviewer's own model of expected behavior, made before any lookup.
3. Explains that once a check result is seen, the reviewer cannot tell whether their model or the result produced the judgment.
4. States that the audit decides whether a source needs consulting and what the verification should look for.
5. States that without the audit the checks lack a question, and without the checks the audit remains unvalidated opinion.

**Source:** Audit before you verify

## ES-ch06.31

A diff changes how a numerical library call rounds a value, and the reviewer has never used the library. Explain what the reviewer should do, why approving on the strength of clean formatting and a persuasive description would be a mistake, and how the unfamiliarity should be recorded.

**Points:** 5

**Rubric (1 point each):**

1. States that the honest verdict is that the reviewer cannot audit the change and should say so.
2. Names the missing knowledge, such as the library's rounding rules and their edge cases.
3. Routes the change to a source: documentation, a person who knows the library, or a targeted test of the rounding behavior.
4. Explains that formatting, comments and a persuasive description reflect fluency, which can arise whether or not the change is correct.
5. Explains that the unchecked area should be recorded in the sign-off, or the claim narrowed to what was verified.

**Source:** Audit before you verify

## ES-ch06.32

Language models and human writers can both produce explanations that sound authoritative. Explain why a fluent, well-formatted patch description is poor evidence that a patch is correct, and what a reviewer should look at instead.

**Points:** 5

**Rubric (1 point each):**

1. Explains that fluency and groundedness arise from different processes and correlate imperfectly.
2. Explains that human instinct trained on writers whose fluency tracked competence reads polish as a signal of correctness, which is unreliable for model output.
3. Notes that a persuasive description can be wrong, partial or describing intent rather than behavior.
4. Names evidence to prefer: the diff itself, executed checks tied to the current version, reproduction of the defect, and scope comparison.
5. Notes that reviewer knowledge of how the system should behave is what detects a mismatch between the description and the code.

**Source:** Audit before you verify

## ES-ch06.33

A reviewer predicted that a change would break behavior on empty input. The test suite then ran and passed, including an empty-input case. Describe at least two explanations for the disagreement between prediction and result, what the reviewer should do next, and what should happen to the original prediction record.

**Points:** 5

**Rubric (1 point each):**

1. Names the explanation that the reviewer's model of the code was wrong in this area.
2. Names the explanation that the check was aimed at the wrong target, for example the empty-input test does not exercise the path the reviewer suspected.
3. Describes follow-up that distinguishes the explanations, such as reading the test, running a targeted check on the suspected path, or inspecting the code.
4. States that the disagreement is information that updates the reviewer's model rather than a failure to be hidden.
5. States that the original prediction record is left as written, with the result placed beside it.

**Source:** Audit before you verify

## ES-ch06.34

A reviewer reading a patch has a strong feeling that it is fine. Another reviewer has a strong feeling that a different patch is broken, but cannot yet say why. Explain how each intuition should be treated, why neither is enough on its own, and how stating a mechanism helps.

**Points:** 5

**Rubric (1 point each):**

1. States that a feeling of "fine" does not license skipping the checks the task requires.
2. States that a feeling of "broken" is a reason to investigate and is not evidence of a defect.
3. Explains that intuition can reflect real pattern recognition or merely familiarity, and the reviewer cannot tell which without articulating the basis.
4. Explains that naming the mechanism, such as a violated constraint or a missing pattern, makes the suspicion testable and defensible.
5. Explains that a verdict that cannot be explained cannot be taught, defended to a skeptic or trusted by the reviewer.

**Source:** Audit before you verify

## ES-ch06.35

Three patches are proposed for a function that must return its input plus one, within a task that allows changes to one source file and its test file. Patch 1 returns the constant 3 and passes the existing test, which only uses input 2. Patch 2 returns `x + 1`, passes all checks, and also modifies an unrelated configuration file. Patch 3 returns `x + 1`, passes all checks and stays in scope, but the requester later says the real requirement was something else. Decide accept, revise or reject for each and justify the decisions.

**Points:** 5

**Rubric (1 point each):**

1. Treats Patch 1 as a revise case: the goal is valid, the implementation fails the stated rule on other inputs, and the evidence is too thin.
2. Treats Patch 2 as rejectable as presented, or revisable after the configuration change is reverted or justified, because scope is an independent obligation.
3. Explains that passing behavioral tests does not neutralize an unexamined change elsewhere.
4. Treats Patch 3 as a failure of the requirement, not of the implementation: tests cannot repair an invalid requirement, so the specification must be reopened.
5. States that the decision belongs to the accountable human reviewer, with the evidence and limits recorded; the agent may recommend but not decide.

**Source:** Accept, revise, or reject

## ES-ch06.36

A reviewer's note says only "Looks good, merging." Rewrite it as an accept decision for a patch that returns `x + 1` after two regression inputs and the existing suite passed. Explain what the rewritten version contains that the original lacks and why a reader benefits.

**Points:** 5

**Rubric (1 point each):**

1. Names the exact version reviewed, such as a commit hash or diff digest.
2. Names the scope inspected, such as which files were changed and compared against the allowed list.
3. Names the checks run and on what: the two regression inputs and the existing suite, run on the current diff.
4. Names the remaining limitations, such as non-integer input types and other boundary values not evaluated.
5. Explains that a specific, falsifiable record lets a reader disagree, find gaps or reproduce the checks, whereas "looks good" hides the basis of the judgment.

**Source:** Accept, revise, or reject

## ES-ch06.37

A coding agent implements precisely the rule in a ticket ("round prices down to the nearest dollar"), every test derived from the ticket passes, and the diff is clean and in scope. Weeks later finance says prices should have been rounded to the nearest cent. Explain why the review process did not catch this, what review could have done differently, and why more tests from the same ticket would not have helped.

**Points:** 5

**Rubric (1 point each):**

1. Explains that tests derived from the ticket check implementation against the specification, not the specification against the real need.
2. Explains that an exact implementation of a wrong rule is still a failure for the actual task.
3. States that the requirement's owner decides what the requirement is and the code cannot supply it.
4. Suggests review could have confirmed the requirement with its owner, checked an example of expected output, or flagged doubt and reopened the specification.
5. Explains that additional tests from the same source reproduce the same error, so correlated evidence does not add independence.

**Source:** A worked decision from beginning to end

## ES-ch06.38

A report contains these sentences about a patch whose evidence is one run of three tests on one commit: "The patch completely fixes the bug." "The patch returns the expected values for the three tested inputs." "The patch is safe to merge." Rank the sentences by how well the evidence supports them, rewrite the overclaims to match the record, and explain why rewriting can change what readers do.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the second sentence as supported: it reports exactly what was observed.
2. Identifies "completely fixes the bug" as unsupported, since three inputs cannot establish behavior over the whole domain.
3. Identifies "safe to merge" as a decision requiring an accountable person, scope check and risk judgment, not a result of three tests.
4. Rewrites the overclaims at a strength the record supports, for example that the results suggest the patch implements the rule on the tested inputs.
5. Explains that a stronger claim invites merging while a weaker one invites further checks, so calibration changes the next action.

**Source:** Choose the verb the record supports

## ES-ch06.39

A developer wrote a status summary of a code change and is confident that every claim in it is supported. A colleague, asked to critique it, says "this is too strong." Explain why writers have trouble seeing overclaims in their own summaries, and describe what a useful peer critique looks like, with an example.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the writer's sense of the evidence comes from memory of the work, which fills gaps that the page does not.
2. Explains that the writer chose each sentence's strongest verb by what felt true, so the mismatches are the ones the writer cannot see.
3. Says a useful critique names a specific sentence, the verb used, the evidence that verb requires, and the verb the record supports.
4. Gives an example such as "completely fixed" being unsupported by two inputs on one function, with "suggest" matching the record.
5. States that the original, the revision and the reason should be preserved.

**Source:** Choose the verb the record supports

## ES-ch06.40

An AI review assistant produces the line "decision: accept" for a patch. A manager proposes treating that line as the required human approval to speed up merges. Explain why this is a mistake, what the assistant may legitimately contribute, and what must remain with a person.

**Points:** 5

**Rubric (1 point each):**

1. States that approval is a human act with accountability, which a model's output cannot supply.
2. States that a recommendation from the assistant can summarize evidence, challenge a rationale and flag overclaims.
3. States that deciding which verb a result supports, whether scope should widen and whether to merge belongs to the responsible reviewer.
4. Notes the failure mode: if the same system proposes, checks and approves, errors correlate and no independent check exists.
5. Notes that treating the field as approval would let the process certify itself, which is exactly what the approval step is meant to prevent.

**Source:** Accept, revise, or reject

## ES-ch06.41

A manager asks a reviewer to sign a note saying "The patch is safe to merge." Explain why this sentence is not an evidence finding in the same sense as "the patch returns the expected values for these inputs," what it depends on, and how the reviewer can respond honestly if the evidence is thin.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes an observation about tested behavior from a judgment about acceptable risk.
2. Notes that "safe to merge" depends on scope, unchecked areas, consequences of failure and organizational standards, not on a single result.
3. Notes that it is a decision belonging to a named person, who accepts accountability for it.
4. Says the reviewer can sign a narrower statement that lists what was checked, how, and what was not checked.
5. Says that withholding the signature or labeling the note a recommendation is honest when the record does not support signing.

**Source:** The sign-off

## ES-ch06.42

A review packet contains: an issue describing a crash on an empty list; a failing test that checks a negative number; a plan that names three files, two of them outside the allowed list; a diff touching five files; test output dated before the final edit; and a decision that says only "approved." Identify the broken links in this chain and explain why the packet can look complete while its argument fails.

**Points:** 5

**Rubric (1 point each):**

1. Notes that the failing test does not reproduce the issue (negative number versus empty list).
2. Notes that the plan names files outside the allowed scope and the diff touches more files than the plan, so the diff does not follow the reviewed plan.
3. Notes that the test output predates the final edit and so does not describe the diff under review.
4. Notes that the decision does not name which version of the proposal it covers.
5. Explains that files in a folder do not guarantee the records refer to one another; each record must name and match the same proposal.

**Source:** A packet is a chain, not a folder

## ES-ch06.43

A reviewer must identify the exact proposal that was reviewed. Compare three identifiers: a commit hash, a saved digest of the diff, and a dated description of the working tree. Explain the strengths and weaknesses of each and what each cannot prove.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a commit hash identifies content and history exactly and is the strongest identifier when a real commit exists.
2. Explains that a diff digest fingerprints the exact change text and works without a commit, but needs a stated base and the saved diff to be useful.
3. Explains that a dated working-tree description is ambiguous and can drift, so it is the weakest option.
4. States that none of them proves who reviewed the change or that the reviewer understood it.
5. States that none of them shows the tests targeted the right code; the working directory and target must be recorded as well.

**Source:** A packet is a chain, not a folder

## ES-ch06.44

A sign-off template ends with a line "Not checked:" followed by a list. Explain why this line carries much of the sign-off's value, why a draft written by the AI system that made the change would tend to omit it, and give three examples of what it might list for a small bug fix.

**Points:** 5

**Rubric (1 point each):**

1. Explains that listing gaps tells the reader the limits of the claim so they can agree, disagree or fill them.
2. Explains that a claim without stated limits invites over-reading, and an honest record includes negative space.
3. Explains that a model drafting the note has no record of which checks the human skipped, so the list must come from the human's own record.
4. Gives examples such as inputs and types outside the test cases, behavior in files outside the allowed list, and anything that ran before the last edit.
5. Notes that listing what was not checked does not weaken the packet, and that withholding the signature is acceptable when the record does not support it.

**Source:** The sign-off

## ES-ch06.45

A reviewer's first test run on a candidate patch fails with a syntax error in the reviewer's own test harness. The reviewer fixes the harness, reruns, and sees a pass. Explain what the first run does and does not show, how both runs should be recorded, and why deleting the first is a mistake.

**Points:** 5

**Rubric (1 point each):**

1. States that a syntax error in the harness is a fault in the measuring instrument and shows nothing about the candidate's correctness.
2. States that the first run never reached an assertion, so it cannot count as evidence for or against the patch.
3. Says the harness should be repaired, the check rerun, and both runs recorded with their commands and outputs.
4. Explains that the path from failure to correction documents what was actually tested and when.
5. Explains that deleting earlier evidence hides provenance and weakens the record, even if the final run is clean.

**Source:** Keep the failure in the record

## ES-ch06.46

A student's report says, "AI wrote about 70 percent of the code." Explain why this is a poor contribution record for a review packet, describe a better one, and say what evidence should back the claim that a person exercised judgment.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a percentage hides which tasks were delegated and which judgments were kept.
2. Explains that line counts weight trivial and critical lines equally and are sensitive to formatting.
3. Describes a record by named action, for example agent: plan, proposed code, suggested tests, summary; human: reproduction, scope, pre-patch test, audit note, decision.
4. Says evidence of human judgment should point to a transcript line, timestamp or edit where the person changed or rejected something.
5. Notes that if no such trace exists, the claimed split may have happened only in the person's head and cannot be audited.

**Source:** Ship It: the review packet

## ES-ch06.47

A student's coding-agent session would not start on the day a review packet was due. The student is tempted to write a plausible transcript of what the session "would have" produced. Explain what the student should do instead and why fabricated records are damaging even when the code in them works.

**Points:** 5

**Rubric (1 point each):**

1. States the student should report that the session was unavailable and complete the parts that do not depend on it.
2. Explains that a fabricated transcript misrepresents provenance, so a reader cannot calibrate trust in any of the packet.
3. Explains that working code in an invented transcript does not make the transcript true.
4. Notes that hand-supplied values (such as an approval flag set in a test) must be labeled as simulated and not presented as human acts.
5. States that an honest record of what did not run is worth more than a seamless story that hides it.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.48

A team is deciding how to divide the work of fixing and reviewing a bug between a coding agent and a human reviewer. For five tasks (stating the rule, writing the regression test, drafting the patch, setting scope, deciding to merge), say what the agent should do, what the human should do, and why that split makes sense.

**Points:** 5

**Rubric (1 point each):**

1. Says the human states the rule and defines which inputs count as the defect; the agent may propose edge inputs.
2. Says the human writes the regression test before the patch, and adopts or rejects agent-proposed cases, because a test written after or with the patch tends to bless it.
3. Says the agent may plan and implement against the standard quickly, while the human builds or understands a baseline.
4. Says the human sets and revises the scope because the agent does not know dependents, parallel work or release ownership.
5. Says the human decides to merge, choosing the claim's strength and signing or withholding, since accountability cannot be delegated.

**Source:** The driver's seat

## ES-ch06.49

A student plans to let a coding agent write all of a module and only review the result. A mentor says the student should first write their own version. Explain the mentor's reasoning, what the student gains from comparing the two versions, and what kind of difference is worth naming.

**Points:** 5

**Rubric (1 point each):**

1. Explains that judging a patch requires a model of how the code should behave, which comes from having built it.
2. Explains that a self-built baseline records what the student understood before seeing the agent's work.
3. Explains that comparing the two exposes gaps in either implementation and in the student's tests.
4. Says the difference worth naming is a difference in behavior, such as an edge case one version handles and the other does not.
5. Says differences in line count or style are weak evidence of anything.

**Source:** Build It: the baseline that lets you audit

## ES-ch06.50

A developer asks a coding agent to propose a deliberately wrong implementation that still passes the developer's tests, then checks by hand whether it does. Explain the purpose of the exercise, how to interpret each outcome, and what limits remain.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the exercise probes test strength by searching for implementations the suite wrongly accepts.
2. Explains that if a wrong implementation passes, the tests are too weak and a new test that rejects it should be added to the standard.
3. Explains that if no wrong implementation is found, this does not show the tests are complete, since the agent may simply not have found one.
4. Notes that the developer should verify the claim by running the tests, not accept the agent's statement that the implementation passes or fails.
5. Notes that adequacy of the tests relative to the requirement is a human judgment that the system under test cannot make.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.51

A function returns a dictionary with a boolean `ready` and a list `reasons`. Its five tests check only that `ready` is False in four failing cases and True in one passing case. Wrong version W1 always returns `ready` False. Wrong version W2 computes `ready` correctly but always returns `reasons` as `["unknown"]`. Determine which tests catch each wrong version, explain what this shows about a green suite, and propose a fix.

**Points:** 5

**Rubric (1 point each):**

1. States that W1 passes the four failing-case tests and is caught only by the test expecting True.
2. States that W2 passes all five tests because none inspects `reasons`.
3. Explains that a suite reports on what it asserts, and what nobody asserted is what nobody checked.
4. Proposes asserting the expected reasons in each failing case so W2 is caught.
5. Proposes keeping wrong versions like W1 and W2 as a standing check that the suite can reject known defects.

**Source:** Build It: the baseline that lets you audit

## ES-ch06.52

A developer using a coding agent asks for a plan before allowing any edit. Explain the value of this step, what the developer should check in the plan, and why approving a plan is not the same as approving the resulting change.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a plan is cheap to correct whereas edits already made must be undone.
2. Says to check the plan's files against the intended scope; a file outside it is a decision for the task's owner.
3. Says to check that the plan addresses the stated issue and reproduction and proposes how the change will be tested.
4. Explains that the implementation may drift from the plan, so the diff must still be reviewed.
5. Explains that separating exploration, planning and implementation provides checkpoints at which a person can redirect the work.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.53

A coding agent such as Claude Code asks permission before editing files or running shell commands by default, and can be set to pre-approve certain actions. A team is considering approving everything automatically to speed up work. Discuss the tradeoffs, what the review of the final diff must then bear, and which controls should remain.

**Points:** 5

**Rubric (1 point each):**

1. Notes that speed improves, since interruptions and waiting for approval are removed.
2. Explains that prompts act as checkpoints at which a person can see each command before side effects occur, and automatic approval removes them.
3. Explains that the after-the-fact diff and check evidence must then carry more weight.
4. Says some actions, such as deleting data, network access, installing packages or touching production resources, should stay gated or sandboxed.
5. Says pre-approval is authorization in advance for classes of actions, not a record of a person judging this particular change.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.54

Published guidance for agentic coding tools such as Claude Code recommends giving them executable ways to verify their work, such as tests and linters. Explain why this helps, and explain the limits of an agent verifying its own work, including how those limits are managed.

**Points:** 5

**Rubric (1 point each):**

1. Explains that execution feedback lets an agent detect and correct mistakes it could not see by reasoning alone.
2. Explains that tests the agent writes share its assumptions, so a pass is weaker evidence than a pass of independent checks.
3. Notes the risk that the agent resolves a failing check by weakening or special-casing it rather than fixing the code.
4. Describes mitigation: person-authored checks written before the patch, test files outside the editable scope, review of any test change.
5. States that executable checks cover only what they assert, so scope, requirement validity and test quality still need human judgment.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.55

A developer lets a coding agent work in a throwaway git branch or worktree, with the starting commit recorded. Explain the benefits of this setup, what it does not protect against, and how the recorded base commit helps the review.

**Points:** 5

**Rubric (1 point each):**

1. Explains that isolation makes failure cheap, since the branch can be discarded without affecting the main line.
2. Explains that the recorded base lets the reviewer compute an exact diff of everything the agent changed in tracked files.
3. Notes that the setup does not cover effects outside the repository, such as installed packages, databases or files elsewhere on the machine.
4. Notes that isolation says nothing about whether the change is correct, so review is still needed.
5. Notes that uncommitted work in the same directory can be lost or entangled, so committing or stashing before starting is prudent.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch06.56

An agent's final diff is small, but during the session it installed a package, ran a database migration against a local development database, and deleted a build-cache directory that is git-ignored. Explain why the diff alone is an incomplete record, what else the reviewer should examine, and what should be recorded.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the diff covers tracked file text only, not environment, data or ignored files.
2. Names what to examine: the log of commands run, installed packages and versions, migration scripts and database state, and deleted paths.
3. Explains that a fresh clone may not reproduce the result if the package was installed only in the agent's environment.
4. Recommends recording the commands with their outputs, and declaring new dependencies and migrations in version-controlled files.
5. Notes that a migration against a real database may be irreversible, so it should be reviewed before execution, not after.

**Source:** Read a diff as a behavioral proposal

## ES-ch06.57

One reviewer approves all AI-written patches that pass tests. Another rejects all AI-written patches on principle. Explain what each policy gets wrong, what a sound policy rests on, and why attribution still matters.

**Points:** 5

**Rubric (1 point each):**

1. Explains that each policy substitutes a rule about origin for evidence about the change.
2. Explains that automatic approval trusts the tests blindly and ignores scope, test quality and requirement validity.
3. Explains that blanket rejection discards good changes and cultivates no skill at telling good from bad.
4. States that a sound policy rests on the proposal, its scope, executed checks tied to the current version and an accountable decision.
5. Explains that attribution does not change what the code does but belongs in the contribution record.

**Source:** Keep the failure in the record

## ES-ch06.58

A team requires a single human approval click on every AI-generated change. Over time reviewers click through quickly. Explain how a review step becomes ceremonial, the conditions that cause it, and what the team can do instead of either abandoning review or demanding more clicks.

**Points:** 5

**Rubric (1 point each):**

1. Explains that review becomes ceremonial when the reviewer cannot be informed by the evidence or the volume exceeds attention.
2. Names causes: weak or missing evidence, large diffs, ambiguous standards and pressure for throughput.
3. Explains that a click records an event, not understanding.
4. Proposes improving the packet: tests fixed in advance, tight scope, recorded commands and outputs, and clear statements of what was not checked.
5. Proposes measuring review quality by reasons recorded and defects caught instead of counting approvals.

**Source:** Choose the verb the record supports

## ES-ch06.59

A coding agent is asked to fix a bug in an authentication module. Its patch is well written and passes the tests it wrote. Later the team finds that behavior in that module is overridden by a configuration file the agent never saw. Explain how this failure arose upstream of the patch, why reading the diff would not necessarily reveal it, and how to reduce the risk.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the agent can only be grounded in material that reached its context, and the configuration never did.
2. Explains that a coherent diff does not show that the relevant information was available to the model.
3. Explains that tests the agent wrote share the same incomplete picture, so passing them does not reveal the gap.
4. Suggests checking what files the agent read or was given, and comparing against what the task depends on.
5. Suggests remedies: pointing the agent at the relevant files, project documentation of configuration layers, and tests that exercise the deployed configuration.

**Source:** Which source material reached the system?

## ES-ch06.60

Before asking a coding agent for a patch, a team writes down: the rule in plain language, reproduction inputs with expected outputs, the files that may change, a stop condition for moving the patch forward, and a known wrong implementation their tests must reject. Explain the purpose of each element and how the team can check the standard itself before involving the agent.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the rule and reproduction fix what correct behavior means before any patch can reshape it.
2. Explains that the allowed-file list turns "keep the change focused" into a testable comparison.
3. Explains that the stop condition states in advance what evidence must exist (test saved before the plan, checks run on the current diff, commands and exit status recorded) for the patch to proceed.
4. Explains that a known wrong implementation validates the tests: if it passes, the standard is too weak.
5. Describes checking the standard by running the tests against the old code, the known wrong version and the intended version, expecting fail, fail and pass respectively on the relevant cases.

**Source:** The gate: reproduction, test, and scope, before the patch

## ES-ch06.61

Under deadline pressure a reviewer can skip one of three things: writing the standard before the patch, writing down predictions before running checks, or calibrating the strength of the final claim. For a patch that replaces the correct logic with a constant, explain what skipping each would cost.

**Points:** 5

**Rubric (1 point each):**

1. Explains that skipping the pre-patch standard lets the patch shape the tests, so a one-input test can bless the constant.
2. Explains that skipping the prediction removes the question the checks should answer, so the reviewer may not notice that the body ignores its input.
3. Explains that skipping calibration lets "completely fixed" stand on a single passing case.
4. Explains that each skipped step leaves the others weaker, since the three work together as a chain.
5. Concludes with a defensible ranking or a rule for which to protect first, with a reason.

**Source:** What you can now defend
