# Chapter 6: Claude Code and diff review

## MA-ch06.1

A user files a bug report that says only "the shipping cost is wrong." An engineer wants to hand a bounded task to a coding agent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The report as written is enough to bound the change, because an agent can infer the inputs and expectations from the codebase.
- [ ] B. Reproducing the failure with a concrete input also proves which line of code causes it.
- [ ] C. The preferred reproduction is the smallest legitimate case that still shows the gap between expected and observed behavior.
- [ ] D. A useful reproduction names a concrete input, the expected result, and the observed result.
- [ ] E. The reproduction should be written only after a fix exists, so that it matches the fix's output format.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: A vague report leaves the inputs, expectations and scope to guesswork, so the agent can solve a different problem than the one reported.
- B: A failing input shows that behavior contradicts the requirement; locating the cause takes separate inspection or debugging.
- C: A minimal case isolates the discrepancy and keeps later diagnosis and review cheap.
- D: Without a specific input, expected value and observed value there is nothing to test a patch against.
- E: A reproduction written to fit a fix stops being independent evidence that the original defect existed.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.2

A requirement says amounts are rounded half up to whole dollars, so 2.5 becomes 3. In one session a coding agent writes a fix that uses Python's built-in `round()` and also writes the regression test for its own fix, asserting that the fixed function returns 2 for input 2.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The test is independent evidence for the requirement because it lives in a separate file from the fix.
- [ ] B. Having the agent propose extra test cases remains useful if a person checks each one against the requirement before adopting it.
- [ ] C. A test written from the written requirement before the fix would expect 3 for input 2.5 and would fail against this fix.
- [ ] D. Because one model wrote both pieces, a misreading in one is unlikely to be repeated in the other.
- [ ] E. The agent's test passes even though the requirement is violated.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Independence comes from a different source of expected values, not from a different filename.
- B: Agent-proposed cases are cheap and often find missed inputs, provided a human decides whether each matches the real requirement.
- C: The requirement gives 3 for 2.5, so a requirement-derived test exposes the mismatch the self-written test hides.
- D: Errors from one author are correlated: the same misunderstanding that shaped the code shapes the test's expected value.
- E: Python 3's round() rounds halves to the nearest even number, so round(2.5) is 2, and the test encodes that same behavior.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.3

A function `sq(n)` must return n squared. The only existing test is `assert sq(1) == 1`. A proposed patch replaces the body with `return 1`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding `assert sq(0) == 0` would make the patch fail.
- [ ] B. The passing test shows that the patch implements squaring for the inputs that matter.
- [ ] C. Adding `assert sq(3) == 9` would make the patch fail.
- [ ] D. The patch passes the only existing test.
- [ ] E. Adding `assert sq(-1) == 1` would make the patch fail.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The constant returns 1 where 0 is expected, so zero separates the patch from the correct function.
- B: One passing case supports only the claim about that case; many wrong functions share the same output at input 1.
- C: The constant returns 1, not 9, so a second input with a different square exposes it.
- D: The constant 1 equals 1 squared, so the single test cannot tell the patch from the real function.
- E: The square of -1 is 1, which the constant also returns, so this input adds no discriminating power.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.4

A developer writes a new regression test for a reported bug and runs it against the unfixed code before any patch exists. The test passes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The pass proves the bug was already fixed, so no further investigation is needed.
- [ ] B. As written, the test does not reproduce the reported failure and so cannot show that a later patch fixed anything.
- [ ] C. A test that passes both before and after the patch is the strongest kind of regression test.
- [ ] D. The developer should adjust the test or the reproduction until it fails on the unfixed code for the reason given in the report.
- [ ] E. Watching the test fail on the unfixed code and pass on the patched code proves the patch is correct for all inputs.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The pass may mean the test hits a different path, uses the wrong input or environment, or that the bug is intermittent; it needs investigation, not closure.
- B: A regression test earns its name by failing without the fix; a test that already passes distinguishes nothing.
- C: A test that never changes outcome gives no evidence about the patch.
- D: Validating the test against the known-broken code confirms it is aimed at the real defect.
- E: A fail-then-pass transition shows the tested cases changed, not that every input is handled.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.5

A team requires that the regression test for any coding-agent patch be written and committed before the agent is asked for a plan. Check each statement that is true about that rule. Each statement is worth 1 point (5 points total).

- [ ] A. A commit of the test that precedes the plan lets a reviewer later verify the order in which things were decided.
- [ ] B. A test written first from the rule is guaranteed to be complete.
- [ ] C. The main reason for the ordering is that tests execute faster when the code does not exist yet.
- [ ] D. A test written after reading the patch tends to check the cases the patch already handles, with expected values copied from what the patch returns.
- [ ] E. With the test fixed first, the patch rather than the test is what is on trial.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Timestamps and commit history give checkable provenance for the claim that the test came first.
- B: The test's writer can still miss inputs and edge cases; the rule limits bias, not incompleteness.
- C: The justification is independence of the expected behavior from the implementation, not speed.
- D: Seeing the answer first anchors the test to the implementation, which is a form of confirmation bias.
- E: A fixed test is a standard the proposal must meet instead of a description of what the proposal does.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.6

A function `clamp(x, lo, hi)` must return lo if x < lo, hi if x > hi, and x otherwise. Four candidates: P is `max(lo, min(x, hi))`; Q is `max(lo, x)`; R is `min(x, hi)`; S is `x`. The three tests are T1 `clamp(5, 0, 10) == 5`, T2 `clamp(-3, 0, 10) == 0`, and T3 `clamp(15, 0, 10) == 10`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Candidate Q passes T1 and T3 but fails T2.
- [ ] B. A suite containing only T1 accepts all four candidates.
- [ ] C. Passing all three tests proves candidate P is correct for every numeric input.
- [ ] D. Candidate R passes T1 and T3 but fails T2.
- [ ] E. A suite containing only T1 and T3 would reject candidate R.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Q forgets the upper bound, so it passes T1 and T2 and fails T3 (it returns 15 instead of 10).
- B: With x inside the range every candidate returns x, so T1 cannot separate them.
- C: Three cases show agreement on those cases only; untested types, equal bounds, lo greater than hi and floating-point edge cases remain open.
- D: R forgets the lower bound, so min(-3, 10) is -3 rather than 0, failing T2 while passing T1 and T3.
- E: R passes both T1 and T3, so that two-test suite would still accept it.

**Source:** The gate: reproduction, test, and scope, before the patch

## MA-ch06.7

A function `f(x)` must return x + 1 for integers. The suite asserts `f(2) == 3` and `f(5) == 6`. Four mutants (deliberately wrong variants) are tried: m1 returns x + 2; m2 returns x - 1; m3 returns x + 1 when x < 10 and x otherwise; m4 returns 0 when x is 0 and x + 1 otherwise. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding `assert f(0) == 1` would kill mutant m3.
- [ ] B. Mutant m3 survives the suite.
- [ ] C. The suite kills mutant m1.
- [ ] D. Mutant m4 survives the suite.
- [ ] E. The suite kills mutant m2.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: m3 returns 1 for input 0 because 0 < 10, so that assertion passes on m3; an input of 10 or more is needed to kill it.
- B: For inputs 2 and 5, which are both below 10, m3 behaves like the correct function.
- C: m1 returns 4 for input 2 where 3 is expected, so the first assertion fails.
- D: Neither 2 nor 5 is 0, so m4 matches the correct function on both assertions.
- E: m2 returns 1 for input 2, so the first assertion fails.

**Source:** Build It: the baseline that lets you audit

## MA-ch06.8

A team measures a test suite by running it against 8 mutants of a function (small deliberate defects). The suite fails on 6 mutants and passes on 2. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 75 percent mutation score proves the unmutated function is correct.
- [ ] B. A surviving mutant that is not equivalent to the original points to behavior the suite does not assert.
- [ ] C. Full line coverage would guarantee that every mutant is killed.
- [ ] D. A score of 75 percent means the real function has a 25 percent chance of being wrong.
- [ ] E. The mutation score is 75 percent.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Mutation score measures the suite's ability to detect the injected defects, not the correctness of the original function.
- B: A survivor is a wrong variant that every assertion tolerates, so it marks an unchecked behavior (or an equivalent mutant that behaves identically).
- C: Lines can execute without their results being asserted, so coverage does not imply detection.
- D: The score describes the suite against a chosen mutant set, not a probability that the production code is wrong.
- E: 6 killed out of 8 is 0.75.

**Source:** Build It: the baseline that lets you audit

## MA-ch06.9

A coding agent is asked to make a failing test pass. The failing test called `tax(100)` and expected 8.0. The agent's diff adds `if amount == 100: return 8.0` ahead of the general logic in `tax.py`. The same diff changes the expected value in a second failing assertion in the test file from 12.5 to 11.0. The whole suite is now green. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Editing the expected value of an assertion changes the specification of correct behavior and needs its own justification.
- [ ] B. When the task was to fix source behavior, edits to test files in the diff deserve at least as much scrutiny as the source edits.
- [ ] C. Changing a test's expected value is acceptable whenever it makes the suite pass.
- [ ] D. Because the suite is green, the diff can be accepted.
- [ ] E. The special case for amount 100 is a hardcoded response to a test input rather than a general fix.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The expected value encodes the requirement; moving it to match the code reverses the direction of evidence.
- B: Weakening, deleting or rewriting tests is a standard way to turn red into green, so these edits need independent confirmation.
- C: Making a suite pass is not a justification; the new value must be shown correct from the requirement.
- D: A green suite that was edited and special-cased measures the agent's accommodation of the tests, not the fix.
- E: Branching on the exact test input makes the test pass without implementing the rule, a known way for optimizing agents to game checks.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.10

A reviewer runs a regression suite against a candidate patch and gets a SyntaxError raised from the reviewer's own test file, before any assertion executes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The first run is still worth recording, because it shows that run did not test the patch at all.
- [ ] B. The error says nothing about whether the candidate patch is correct.
- [ ] C. After the rerun passes, the failed run's output should be deleted to keep the record clean.
- [ ] D. The candidate should be rejected because its run failed.
- [ ] E. The reviewer should repair the harness, rerun, and keep the records of both runs.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Recording that the first run never reached an assertion prevents anyone from counting it as evidence either way.
- B: A fault in the test harness is a fault in the measuring instrument, not in the object measured.
- C: Deleting earlier evidence hides the path from failure to correction, which is often the most informative part of the record.
- D: Rejecting on a harness error attributes a tooling defect to the patch.
- E: Fix the instrument, rerun, and keep both runs so the timeline of what was actually tested is honest.

**Source:** Keep the failure in the record

## MA-ch06.11

A reviewer is shown this unified diff.

```text
--- a/pricing.py
+++ b/pricing.py
@@ -2,5 +2,5 @@
     subtotal = 0
     for item in items:
-        subtotal += item.price
-    tax = subtotal * rate
+        subtotal += item.price * item.qty
+    tax = round(subtotal * rate, 2)
     return subtotal + tax
```

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The change to the tax line can alter the computed total for some inputs.
- [ ] B. The subtotal now multiplies price by quantity, which changes the result for any item whose quantity is not 1.
- [ ] C. The hunk header says the old text spans 5 lines starting at line 2 and the new text spans 5 lines starting at line 2.
- [ ] D. The diff demonstrates that the new code runs without error.
- [ ] E. Lines that begin with a single space are unchanged context lines.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: round(..., 2) changes the tax whenever the unrounded product has more than two decimal places, for example 0.733 becomes 0.73.
- B: price * qty equals price only when qty is 1, so totals change for any other quantity.
- C: In `-2,5 +2,5`, the first number is the starting line and the second is the line count in each version.
- D: A diff is a text comparison; it neither executes the code nor shows that the new attribute exists on the items.
- E: A unified diff prefixes unchanged context with a space, removed lines with a minus and added lines with a plus.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.12

A reviewer is shown this diff.

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

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The header shows the hunk is one line longer in the new version than in the old (7 lines versus 6).
- [ ] B. The hunk removes four lines and adds three.
- [ ] C. A reviewer can conclude from this diff alone that every caller of `load` will continue to work unchanged.
- [ ] D. Replacing manual open and close with a `with` block cannot change behavior in any circumstance.
- [ ] E. For an empty file, `load` now returns an empty list instead of whatever `parse("")` returned.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: `-1,6 +1,7` gives the line count of each version of the hunk.
- B: The hunk removes three lines and adds four, which is why the new side is longer by one.
- C: Callers that relied on the old empty-input result, or on parse's handling of it, may break and need to be checked beyond the visible lines.
- D: A `with` block closes the file even when an exception is raised, so cleanup behavior differs in error paths.
- E: The added early return bypasses `parse` for empty input, so an empty file no longer reaches it.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.13

A team reviews code changes proposed by an AI agent using unified diffs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A diff computed between two arbitrary strings shows that those strings came from the intended file in the repository.
- [ ] B. A small diff is safe because less text changed.
- [ ] C. A diff reports textual differences; it does not execute the code or show that the new code behaves correctly.
- [ ] D. A one-character change to an operator can alter the result of every call to a function.
- [ ] E. To rely on a diff, the reviewer should record the command and scope that produced it, so it can be tied to the working tree under review.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Nothing in the diff output certifies where its inputs came from; the command and the files compared establish that.
- B: Risk depends on what the change does, not how many lines it touches.
- C: Diffing is string comparison; behavior must be established by tests, execution or reasoning about the change.
- D: Swapping a minus for a plus, or a less-than for a less-than-or-equal, changes every evaluation of that expression.
- E: Recording how the diff was produced links the evidence to the exact state being reviewed.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.14

After an agent session in a git repository, a reviewer runs plain `git diff` and sees modifications to two tracked files. During the session the agent also created a new file, `scripts/migrate.py`, that was never added to git, and it ran `git add config.yaml` on a third tracked file and did not touch that file again. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Plain `git diff` prints a warning about untracked files in the working tree.
- [ ] B. From plain `git diff` output alone the reviewer can conclude the agent modified only two files.
- [ ] C. Plain `git diff` shows the staged change to `config.yaml`.
- [ ] D. Plain `git diff` does not show the contents of the new untracked file.
- [ ] E. `git status` would list `scripts/migrate.py` as untracked.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: `git diff` does not warn about untracked files; silence is not evidence of absence.
- B: The new file and the staged change are both invisible in that output, so at least four files were affected.
- C: A staged, otherwise unmodified file matches the index, so it appears only in `git diff --staged` or `git diff HEAD`.
- D: `git diff` compares the working tree with the index for tracked files and ignores untracked files.
- E: `git status` is the command that reports untracked files and staged changes.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.15

To cut noise, a reviewer views an AI agent's changes to a Python module with whitespace differences ignored (as with `git diff -w`). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The whitespace-ignoring view is a safe substitute for the full diff, because it shows a strict subset of the same changes.
- [ ] B. Ignoring whitespace is safe for any language, because whitespace never affects behavior.
- [ ] C. Trailing-whitespace changes never matter in any file type, including Makefiles and multi-line string literals.
- [ ] D. Indentation changes in Python can move a statement into or out of a block, so hiding them can hide a behavioral change.
- [ ] E. A whitespace-ignoring view makes it easier to spot a re-indentation that moves a line out of a loop.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: A filtered view omits changes by design, so for Python or YAML the unfiltered diff remains the source of truth for what text actually changed.
- B: Some formats and languages (Python, YAML, Makefiles) give whitespace meaning.
- C: Whitespace inside string literals and in tab-sensitive formats can alter output, so no blanket claim holds.
- D: In indentation-sensitive languages, whitespace is syntax; re-indenting a line can change control flow.
- E: The whitespace-ignoring view hides exactly that kind of change, which is the danger of using it blindly.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.16

An agent given shell access in a repository produced a final diff that is small: two source files and one test. During the session it also ran `pip install somepackage`, applied a schema migration to a local development database, and deleted a build-cache directory that is listed in `.gitignore`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reviewer should also inspect the log of commands the agent ran.
- [ ] B. The diff does not capture the package installation, the migration or the deleted ignored directory.
- [ ] C. Files ignored by version control do not appear in `git diff`.
- [ ] D. The small diff shows that the session's effects were confined to two source files and one test.
- [ ] E. A fresh clone with the diff applied might still fail to reproduce the agent's results.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Commands and their outputs are part of the change record when an agent can act on the machine.
- B: Environment and data changes happen outside the tracked text, so a source diff cannot show them.
- C: Ignored paths are excluded from git's view of the working tree.
- D: The diff covers tracked source text only; other effects are invisible in it.
- E: A dependency installed only in the agent's environment, or a migration applied only to its database, can make a clean checkout behave differently.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.17

A reviewer has two diffs to read in one afternoon. Diff 1 contains 600 lines of regenerated lockfile entries and a 20-line change to payment rounding logic. Diff 2 contains 400 lines of docstring edits. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Review effort should be set by line count and the seniority of whoever wrote the change.
- [ ] B. Regenerated lockfile entries are exempt from scrutiny because a tool produced them.
- [ ] C. Review effort should be proportional to line count.
- [ ] D. Reading the larger diff first reliably surfaces the riskiest changes.
- [ ] E. The 20-line payment change likely deserves more careful reading per line than the docstring edits.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: What a change could break and how well the reviewer understands it should set how closely to read it; author seniority and line count are weak proxies.
- B: Generated dependency changes can add or upgrade packages, so the resulting version changes still need checking.
- C: Proportionality to size spends attention on bulk and starves small, high-impact changes.
- D: Size and risk are different axes; a large generated diff can be low risk while a tiny change is dangerous.
- E: Code that moves money carries high consequence per line; docstrings rarely change behavior.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.18

A reviewer can read about 300 lines of diff carefully per hour. A coding agent produces a 2,400-line diff in six minutes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The gap between generation speed and verification speed closes on its own as models get faster.
- [ ] B. Reading faster is the most effective way to close the gap.
- [ ] C. Reading the diff carefully would take about 8 hours.
- [ ] D. Narrowing the allowed scope and writing the checks before the agent starts reduces how much must be read and gives the review something specific to look for.
- [ ] E. If the tests pass, reading the diff is unnecessary.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Faster generation widens the gap, because verification throughput does not scale with the machine.
- B: Human reading speed has a ceiling and care degrades as it is pushed; shrinking the review surface works better.
- C: 2,400 divided by 300 is 8 hours.
- D: Constraining the change and fixing the standard in advance turns open-ended reading into targeted review.
- E: Tests cover only what they assert; scope creep, hardcoding and edits to tests themselves are visible only on reading.

**Source:** Read a diff as a behavioral proposal

## MA-ch06.19

A developer asks a coding agent for a plan before permitting any edits. The returned plan lists four files to change, and one of them is outside the set the developer expected to need touching. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A plan removes the need to read the diff afterward, since it already describes the diff.
- [ ] B. Whether the task should grow to include the extra file is a decision for the owner of the task, not something the agent should settle by assumption.
- [ ] C. Approving the plan is the same as approving the final diff.
- [ ] D. Separating exploration, planning and implementation gives checkpoints at which a person can redirect the work cheaply.
- [ ] E. Reviewing the plan lets the developer catch the out-of-scope file before any edit exists.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Only the diff shows what was done; the plan states intent.
- B: The agent may have a sound reason, but it lacks knowledge of dependents, parallel work and release ownership.
- C: A plan is a prediction; the implementation can drift from it, so the actual diff still needs review.
- D: Staged work with review points is the documented way to keep an agent's work steerable.
- E: A plan is cheap to correct; an edit that already happened must be undone.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.20

A coding agent such as Claude Code asks for permission before editing files or running shell commands by default, and can be configured to pre-approve some actions or to deny access to specified paths. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Permission prompts give the reviewer a chance to see each command before it runs.
- [ ] B. Denying the agent access to certain paths prevents edits there, whereas a check of changed filenames afterward only detects them.
- [ ] C. A pre-approval setting is an authenticated record of a person's decision on the final change.
- [ ] D. Pre-approving all edits and commands removes the review points that prompts provide, so the review of the resulting diff carries more weight.
- [ ] E. Once a session is approved to run commands, the diff is no longer needed.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Prompts interpose a human decision before side effects occur.
- B: Prevention at the permission layer stops the action; a post-hoc scope check finds it after the fact.
- C: A permission setting authorizes classes of actions in advance; it does not record anyone judging this particular change.
- D: Fewer interactive checkpoints mean the after-the-fact evidence must do more of the work.
- E: Approving the ability to act is not a review of what was done.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.21

A merge-gating function is defined as follows.

```python
def gate(changed, allowed, tests_ok, approved):
    reasons = []
    if not changed:
        reasons.append("empty")
    if set(changed) - set(allowed):
        reasons.append("scope")
    if tests_ok is not True:
        reasons.append("tests")
    if approved is not True:
        reasons.append("approval")
    return reasons
```

Check each statement about its return values that is true. Each statement is worth 1 point (5 points total).

- [ ] A. `gate(["a.py", "c.py"], ["a.py"], True, False)` returns `["scope", "approval"]`.
- [ ] B. `gate(["a.py"], ["a.py", "b.py"], True, True)` returns `["scope"]`, because b.py is allowed but was not changed.
- [ ] C. `gate(["a.py"], [], True, True)` returns an empty list.
- [ ] D. `gate([], ["a.py"], "yes", True)` returns `["empty"]` only, because "yes" counts as passing.
- [ ] E. `gate(["a.py"], ["a.py"], 1, True)` returns an empty list.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: c.py is outside the allowed set and the approval flag is False, so both reasons accumulate in order.
- B: The set difference is changed minus allowed, so an allowed file that was not changed does not matter; with both flags True the result is an empty list.
- C: With an empty allowed list, a.py is outside it, so "scope" is returned.
- D: An empty change list triggers "empty", but the string "yes" is not the literal True, so "tests" is reported as well.
- E: The integer 1 equals True but is not the object True, so the identity test reports "tests".

**Source:** Scope is a testable property, not a mood

## MA-ch06.22

A team defines allowed files as `{app.py, tests/test_app.py}`. An agent's patch changes `{app.py, tests/test_app.py, requirements.txt}`. The team's scope check computes the set difference of changed minus allowed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the dependency change is genuinely required, the right response is to widen the allowed list explicitly, record who decided and why, and rerun the checks.
- [ ] B. A file rename may need richer handling than a plain list of names, because the same change can appear as a deletion plus an addition or as a rename depending on the tool.
- [ ] C. The set difference is `{requirements.txt}`, so the check flags the patch.
- [ ] D. If the patch had changed only `app.py`, the check would still flag it.
- [ ] E. A patch that rewrites unrelated functions inside `app.py` would pass this check.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A legitimate dependency can reopen the scope decision, but it must be explicit and traceable, and evidence must be regenerated on the new proposal.
- B: Diff tooling reports renames in different ways, so a simple name list loses information a reviewer needs.
- C: requirements.txt is in the changed set but not the allowed set.
- D: A changed set that is a subset of the allowed set yields an empty difference, which passes.
- E: Filename-level scope cannot see line-level changes inside a permitted file.

**Source:** Scope is a testable property, not a mood

## MA-ch06.23

A patch correctly fixes the reported bug and all tests pass, but the diff also reformats 300 unrelated lines in the same permitted file. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A filename-level scope check would pass this patch.
- [ ] B. Asking for the formatting churn to be split into a separate change is unreasonable, since it makes no behavioral difference.
- [ ] C. Because the tests pass, the extra reformatting is irrelevant to the decision.
- [ ] D. A file-level allowlist is strong enough to catch this kind of scope creep.
- [ ] E. The unrelated reformatting makes the diff harder to review and can hide or introduce regressions.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The only changed file is on the allowed list, so a name comparison finds nothing.
- B: Separating mechanical churn from behavioral changes is standard review practice and makes both easier to verify.
- C: Scope and correctness are separate obligations; a correct but sprawling patch still fails the scope obligation.
- D: Line-level or hunk-level inspection is required to see changes within an allowed file.
- E: Noise in a diff dilutes the reviewer's attention and can bury a real change among cosmetic ones.

**Source:** Scope is a testable property, not a mood

## MA-ch06.24

An agent working within an allowed file list finds that its fix requires editing `config/limits.yaml`, which is not on the list. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the dependency is legitimate, the right move is to pause, review why the file must change, and widen the scope explicitly, noting who decided and why.
- [ ] B. Widening the scope after seeing the patch proves the original process failed and the whole task should be restarted.
- [ ] C. After the scope is widened, checks run before the widening remain valid evidence for the new proposal.
- [ ] D. The agent may add the file on its own, as long as it mentions the edit in its summary.
- [ ] E. Setting the allowed list to the entire repository so the check passes erases the boundary the check was meant to enforce.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Design can be reopened by what the work reveals, but reopening must be deliberate and recorded.
- B: Discovering a real dependency is a normal reason to revise scope; the failure would be doing so silently.
- C: The proposal changed, so evidence from before it no longer describes what will be merged.
- D: Deciding that the task should grow belongs to the task owner, who knows dependents and parallel work the agent cannot see.
- E: A boundary that includes everything constrains nothing.

**Source:** Scope is a testable property, not a mood

## MA-ch06.25

A merge-gating function accepts two booleans, `tests_passed` and `human_approved`, and reports ready only when both are True. A pipeline author calls it with both set to the literal True in a script. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The booleans carry information about which command ran, on which commit, and when.
- [ ] B. Requiring `human_approved` to be True authenticates a person.
- [ ] C. A sturdier design derives `tests_passed` from the exit status and output of a recorded test run tied to the commit being merged.
- [ ] D. Supplying literal True completes the audit trail because the function checks its arguments.
- [ ] E. A ready result from that call shows the function's branching works, not that any test ran.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A bare boolean has no command, output, timestamp, environment or link to a version of the code.
- B: Requiring the flag prevents omission of approval, but anyone or any script can set it; identity needs a separate mechanism.
- C: Tying the flag to captured evidence about the exact proposal turns an assertion into a derived fact.
- D: The function validates the type of the value, not its provenance, so no evidence has been recorded.
- E: A hand-supplied flag exercises the control path only.

**Source:** Flags are claims about evidence

## MA-ch06.26

At the end of a session a coding agent reports: "I fixed the bug and all tests pass." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reviewer should rerun the relevant tests on the current working tree and keep the command, output and exit status.
- [ ] B. A summary can be accurate about a run and still describe a run that happened before a later edit.
- [ ] C. The statement is a claim about a run; without the command, output and the relation to the final diff it is not evidence.
- [ ] D. A fluent, confident summary is a sign that the claims in it were checked.
- [ ] E. Because the agent can run tests itself, its summary carries the same weight as an exit status the reviewer observes directly.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Reproducing the check on the state being merged turns the claim into an observation.
- B: Edits after the test run silently invalidate its conclusion for the current tree.
- C: Reports are generated text; they become evidence only when tied to reproducible commands and outputs.
- D: Fluency and groundedness arise from different processes and correlate only imperfectly.
- E: A second-hand description of a run is weaker than observing the run, since the summary can be wrong, partial or stale.

**Source:** Flags are claims about evidence

## MA-ch06.27

At 10:00 an agent edits `parser.py`. At 10:05 a reviewer runs the test suite and every test passes. At 10:10 the agent refactors `utils.py`, which `parser.py` imports. At 10:12 the reviewer is about to merge, citing the 10:05 result. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 10:05 result describes the code as it was before the 10:10 edit.
- [ ] B. Saving a digest of the diff next to each test output would reveal the mismatch between what was tested and what is being merged.
- [ ] C. Merging is justified because the suite passed once.
- [ ] D. The 10:05 result remains valid because the refactor was small.
- [ ] E. Rerunning only the tests for `parser.py` is enough, because that file was the one originally changed.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Evidence is about the state at the time of the run.
- B: Recording an identifier for the tested diff makes version drift mechanically checkable.
- C: A pass on a tree that no longer exists says nothing about the tree being merged.
- D: Small changes can still alter behavior; validity depends on whether the tested state equals the merged state.
- E: A refactor of an imported module can break other callers, so the whole relevant suite needs rerunning on the final state.

**Source:** Flags are claims about evidence

## MA-ch06.28

A review tool records a reviewer's decision only as `approved = true`. After approval, before merge, the agent amends its proposal. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A cryptographic hash of the diff proves the reviewer read it.
- [ ] B. Binding the approval to a digest of the exact diff would let the system detect that the merged version differs from the approved one.
- [ ] C. The record cannot show which version of the proposal was approved.
- [ ] D. A digest of the diff identifies the person who approved.
- [ ] E. An approval given before the amendment automatically covers the amended proposal.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A hash shows what was approved, not that anyone read or understood it.
- B: A digest changes whenever the content changes, so a mismatch is detectable.
- C: A bare boolean has no link to content.
- D: A hash fingerprints content; identity needs authentication of the approving account.
- E: Approval attaches to the version reviewed; a changed proposal needs a new decision.

**Source:** Flags are claims about evidence

## MA-ch06.29

A reviewer edits the working tree of a Python project and runs the test suite, which passes. Later the reviewer discovers that the tests had imported the package from an older copy installed in the environment's site-packages, not from the edited working tree. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A screenshot of a green status badge is sufficient to show what was tested.
- [ ] B. Recording the working directory and target of each check, and verifying which file was actually imported, ties the evidence to the code under review.
- [ ] C. The passing run says nothing about the edited code.
- [ ] D. A correct output can be about the wrong target.
- [ ] E. Running the tests after the last edit settles the question of whether the right code was tested.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A badge without its command and target conveys less than it appears to.
- B: Provenance of the tested artifact is part of the evidence.
- C: The run exercised a different copy of the code.
- D: A check can execute faithfully and report truthfully while examining something other than the proposal.
- E: Order in time does not show which code a command examined.

**Source:** A packet is a chain, not a folder

## MA-ch06.30

A review packet contains an issue, a failing test, a plan, a diff, test output and a decision, all saved in one folder. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Placing the right filenames in one folder is enough to guarantee that the records correspond.
- [ ] B. If test output carries a later timestamp than the diff, it must be about that diff.
- [ ] C. If one link points to an earlier version of the diff, the packet can look complete while its argument is broken.
- [ ] D. The packet works as an argument only if each record refers to the same proposal: the test reproduces the issue, the diff follows the plan, outputs come after the diff, and the decision names that diff.
- [ ] E. An uncommitted working-tree description is exactly as precise an identifier as a commit hash.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Files in a directory need not refer to one another; the links must be checked.
- B: A later run can still have targeted the wrong module, branch or directory.
- C: Surface completeness can mask a stale reference.
- D: Evidence supports a claim only when every record concerns the same version of the change.
- E: A hash identifies content exactly, whereas a description of a working tree is ambiguous and can drift.

**Source:** A packet is a chain, not a folder

## MA-ch06.31

A reviewer's sign-off includes the line "Not checked: Unicode input, behavior outside the allowed files, anything that ran before the last edit." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Listing unperformed checks weakens the packet, so reviewers should leave it out.
- [ ] B. A sign-off may state that the bug is fixed in general whenever all supplied tests pass.
- [ ] C. A model drafting the sign-off has no record of which checks the human skipped, so this line must come from the human's own record.
- [ ] D. Listing what was not checked tells the reader the limits of the claim.
- [ ] E. Withholding sign-off is an honest outcome when the evidence does not support signing.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Omitting gaps overstates the evidence, which is the failure a sign-off is meant to prevent.
- B: Passing tests support claims about the tested behaviors, not general correctness.
- C: Absence of work leaves no trace for a model to summarize; only the person knows what they skipped.
- D: Naming gaps lets a reader disagree or fill them, which is what makes the claim checkable.
- E: A signature should reflect what the record supports, and declining is legitimate.

**Source:** The sign-off

## MA-ch06.32

A student submission says "AI wrote about 70 percent of the code." An instructor wants a more informative contribution record. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the agent drafted the plan, the human should omit that from the record to keep the packet focused.
- [ ] B. The record should point to a transcript line, timestamp or edit showing where a person changed or rejected something the agent proposed.
- [ ] C. A percentage that counts boilerplate lines equally with critical logic is a fair summary of responsibility.
- [ ] D. Naming actions (agent: plan, patch proposal, test suggestion; human: reproduction, scope, pre-patch test, decision) says more than a single percentage.
- [ ] E. A percentage is more precise because it is computed from line counts and is unaffected by which lines were written.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Omitting agent contributions misstates provenance.
- B: Evidence of a human decision in the record distinguishes oversight from rubber-stamping.
- C: Equal weighting hides where the consequential decisions were made.
- D: Naming who did which task reveals the division of judgment, which a number cannot.
- E: Line counts treat a trivial import and a core decision as equal, so precision is spurious.

**Source:** Ship It: the review packet

## MA-ch06.33

A student's coding-agent session failed to start, so the student has no transcript for a required review packet. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A test input that hands the function `approved=True` may be presented as evidence that a person approved the change.
- [ ] B. If a session did run, the actual transcript should be preserved with its date and the displayed model label.
- [ ] C. An honest record of what did not run is worth more than a seamless story that conceals it.
- [ ] D. The student should report that the session was unavailable and complete the parts of the work that do not need it.
- [ ] E. Writing a realistic invented transcript and presenting it as the session record is acceptable if the invented code works.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A hand-supplied input exercises a code path and records no human act.
- B: Dated transcripts with model identification make the work reproducible and auditable.
- C: Reviewers rely on the record to calibrate trust, so concealed gaps cost more than visible ones.
- D: Reporting a gap preserves integrity and still allows partial work.
- E: Fabricated provenance misrepresents what happened, whatever the code does.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.34

A reviewer is looking at a patch to a function specified as "return the input plus one." The new body is `return 3`. Before running anything, the reviewer writes down: verdict suspect; target, behavior on an input other than the one in the existing test; mechanism, the body never uses its argument. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Check at least one input other than the one in the existing test" is a useful target for the verification.
- [ ] B. "Check the whole thing" is as useful a target as a specific one.
- [ ] C. Running the tests first and then deciding whether the patch is suspicious is equivalent, because the test output supplies the same information.
- [ ] D. Having written the suspicion down, the reviewer may treat it as proof of a defect.
- [ ] E. The suspicion can be formed from the reviewer's own knowledge that an input-plus-one function must return different values for different inputs.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A target tells the verification what to hunt for and why a single existing input is insufficient.
- B: An unspecific target gives the check no question to answer.
- C: Once the test has spoken, the reviewer cannot tell whether their own model or the test's result produced the suspicion.
- D: A suspicion is a reason to investigate, not evidence of a bug.
- E: A plausibility judgment draws on the reviewer's model of how the function should behave, before any lookup.

**Source:** Audit before you verify

## MA-ch06.35

A reviewer writes down a prediction about what a diff will do and what would change their mind, then runs the checks. Check each statement that is true about that practice. Each statement is worth 1 point (5 points total).

- [ ] A. Writing the prediction before running guards against rewriting history after the result is known.
- [ ] B. After the run, the reviewer should edit the record so it matches the result.
- [ ] C. If the check disagrees with the prediction, the gap is information: either the reviewer's model was wrong or the check was aimed at the wrong target.
- [ ] D. Stating in advance what observation would change their view commits the reviewer to evidence criteria before seeing any evidence.
- [ ] E. A written suspicion is a reason to investigate, not a substitute for the checks the task requires.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A dated, pre-run record prevents hindsight bias from altering what was predicted.
- B: Editing the record after the fact removes its only value as a test of the reviewer's understanding.
- C: A mismatch is diagnostic of either the mental model or the experimental design.
- D: Pre-committing to disconfirming observations is the core discipline of falsification.
- E: Intuition guides where to look; required checks still need to run.

**Source:** Audit before you verify

## MA-ch06.36

A diff changes how a numerical library call rounds a value. The reviewer has never used the library and cannot tell from the diff whether the new behavior is right. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reviewer's unfamiliarity is useful information about who should review this change.
- [ ] B. The honest verdict is that the reviewer cannot audit this change, naming the missing knowledge and routing it to documentation, a person who knows the library, or a narrower claim.
- [ ] C. A fluent, confident explanation in the patch description settles whether the new rounding behavior is correct.
- [ ] D. The patch should be approved because it is well formatted and carries explanatory comments.
- [ ] E. Every patch that touches an unfamiliar library should be rejected automatically.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: If the knowledge to judge is missing, assignment to a qualified reviewer, or documented limits, follow.
- B: Admitting where one's own model is silent is part of auditing, and it directs the work toward a real source.
- C: Fluent, confident text can be produced whether or not the explanation is true, so it cannot settle correctness.
- D: Polish is not evidence of correctness; model-generated text is fluent whether or not it is grounded.
- E: Blanket rejection substitutes a rule for judgment; the correct response is to obtain the missing knowledge or narrow the claim.

**Source:** Audit before you verify

## MA-ch06.37

A reviewer says, "I audited the patch by running the test suite." In this question, a plausibility judgment is the reviewer's own prediction, made before running anything, of what the code should do; verification is checking against an external source such as a test run. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A plausibility judgment decides only whether to run checks, not what the checks should look for.
- [ ] B. A prior prediction is irrelevant when the tests pass.
- [ ] C. After seeing test results, a reviewer can still reliably say what their own prior model predicted.
- [ ] D. The sentence describes a plausibility judgment, since running tests is the most rigorous way to make one.
- [ ] E. Running the suite consults an external source, whereas a plausibility judgment relies on the reviewer's own model of how the code should behave before any lookup.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: A good judgment also directs the verification toward a target.
- B: A pass that matches no prediction may mean the check was aimed wrong; predictions give the pass meaning.
- C: Outcome knowledge distorts memory and reasoning about earlier expectations, which is why the record must precede the run.
- D: Running the suite is verification against an external source; a plausibility judgment would have been made before the run, and here it was skipped or contaminated by the lookup.
- E: Verification consults a test, reference or recomputation; a prior judgment consults none of them.

**Source:** Audit before you verify

## MA-ch06.38

Two reviewers each flag a patch as suspect. Reviewer 1 flags `return 3` in a function specified as input plus one. Reviewer 2 flags a changed rounding mode in a numerical library call. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Both findings are equally independent of the reviewer's expertise.
- [ ] B. Almost any competent programmer who knows the specification could catch Reviewer 1's finding.
- [ ] C. Reviewer 2's finding depends on specific domain knowledge, so who reviews that kind of patch matters.
- [ ] D. Where catching a defect needs specialized knowledge, that dependence should shape who reviews and what the sign-off says was and was not checked.
- [ ] E. A reviewer who cannot explain the mechanism behind a verdict has a verdict that is just as easy to teach and defend.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The two findings differ greatly in the expertise they require.
- B: The constant ignores its input, which anyone who knows the rule can see.
- C: Rounding semantics are library-specific, so recognizing the problem needs knowledge that a generalist may lack.
- D: Naming what knowledge a finding depends on determines who can make it and what remains unchecked.
- E: A verdict without a mechanism cannot be taught or defended, and the reviewer cannot tell reasoning from reaction.

**Source:** Audit before you verify

## MA-ch06.39

Three patches are proposed for a function that must return its input plus one, within an allowed list of one source file and its test file. Patch 1 returns the constant 3 and passes the single visible test at input 2. Patch 2 returns x + 1, passes the regression and existing suites, and also edits an unrelated configuration file. Patch 3 returns x + 1 and passes everything, but the team later learns the real requirement was to return x * 1.1. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Patch 2 should be accepted because the behavior tests pass and a configuration edit is minor.
- [ ] B. Patch 3 shows that testing cannot repair an invalid requirement, so the specification itself must be reopened.
- [ ] C. Patch 3 should be accepted because it implements the stated rule exactly and passes every test.
- [ ] D. Patch 2 can justifiably be rejected as presented, or revised once the configuration edit is reverted or explicitly justified, despite passing tests.
- [ ] E. Patch 1 is a clear case for revision: the goal is valid but the implementation and the evidence are insufficient.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Passing behavior tests does not cancel an out-of-scope change that nobody has examined.
- B: Tests encode the requirement as understood; if that is wrong, the tests agree with the wrong rule.
- C: An exact implementation of a wrong requirement is still a failure for the real task.
- D: Scope and correctness are separate obligations; an unrelated edit can justify rejection of the package.
- E: The constant passes one case but fails the stated rule on others, which calls for a better implementation or a narrower claim.

**Source:** Accept, revise, or reject

## MA-ch06.40

Reviewers record accept rationales. Reviewer X writes "Looks good." Reviewer Y writes "Accept commit 9f3c for integer inputs; the two regression cases and the existing suite passed; non-integer inputs were not evaluated." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Y's note is weaker because it admits what was not evaluated.
- [ ] B. Y's note names the version, the behavior checked, the checks run and the limits, so a reader has something specific to agree or disagree with.
- [ ] C. X's note hides the basis of the judgment.
- [ ] D. An accept record need not mention the checks if the agent's own summary lists them.
- [ ] E. A good accept record names the version reviewed, the scope inspected, the checks run and the remaining limitations.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Stating limits strengthens the record because the claim matches the evidence.
- B: A specific, falsifiable record lets others find gaps.
- C: Without a basis, no one can check or challenge the decision later.
- D: The record should carry the reviewer's own evidence, not defer to a summary written by whoever made the change.
- E: Those four elements make the decision auditable.

**Source:** Accept, revise, or reject

## MA-ch06.41

An AI review tool ends its analysis of its own patch with the line `decision: accept`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The tool can summarize evidence and recommend, but the accountable decision belongs to the responsible human reviewer.
- [ ] B. A reject decision means every line of the patch is wrong.
- [ ] C. Merging automatically is fine whenever the tests pass and the field says accept.
- [ ] D. An accept recommendation from the tool removes the need to examine the scope of the change.
- [ ] E. The field counts as human approval if the tool reports high confidence.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Where a workflow assigns responsibility to a person, the model's output is input to that person's decision.
- B: Rejection concerns the proposal as a package under the current task boundary; parts may be fine.
- C: Automatic merge on a self-reported field removes the accountable check entirely.
- D: Scope is a separate property that needs its own inspection.
- E: Confidence is not a person's approval, and a model cannot supply a human act.

**Source:** Accept, revise, or reject

## MA-ch06.42

A patch was tested once. The record shows three assertions passed on commit c41 in one environment. Check which sentences in a summary the record supports. Each statement is worth 1 point (5 points total).

- [ ] A. "The patch completely fixes the bug."
- [ ] B. "The function has been proven correct."
- [ ] C. "The patch implements the rule for every integer."
- [ ] D. "The patch is safe to merge, as established by these results."
- [ ] E. "On commit c41 in this environment, the three assertions passed."

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: "Completely fixes" implies alternatives were considered and rejected over the whole input domain, which three assertions do not do.
- B: Proof requires a formal argument or exhaustive coverage, not a handful of passing cases.
- C: Three cases cannot establish behavior for all integers.
- D: Safety to merge is a decision with scope, risk and accountability, not a result of three assertions.
- E: A report limited to what ran, on which version and where, matches the evidence exactly.

**Source:** Choose the verb the record supports

## MA-ch06.43

A report changes the sentence "the patch completely fixes the bug" to "the data suggest the patch implements the rule on the tested inputs." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Matching a verb's strength to the evidence means asking what evidence that verb requires and downgrading the sentence until the record meets it.
- [ ] B. A narrower verb is not timid when it accurately communicates the tested boundary.
- [ ] C. A peer can often spot an overstated verb that the writer cannot, because the writer's sense of the evidence is shaped by what they remember doing.
- [ ] D. The change can alter what a reader does next, such as asking for one more test instead of merging.
- [ ] E. The change is cosmetic, since both sentences describe the same evidence.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Calibrating language is an evidence audit applied to prose.
- B: Precision about limits is accuracy, not hedging.
- C: Writers read their own sentences with the full memory of the work, which fills gaps the page does not.
- D: Readers act on the strength of a claim; a weaker claim invites more checking.
- E: The sentences make different claims about scope and certainty.

**Source:** Choose the verb the record supports

## MA-ch06.44

A team divides review tasks between a coding agent and a human reviewer. Check each statement that is true about a sensible division. Each statement is worth 1 point (5 points total).

- [ ] A. The first regression test should be written by the agent that will implement the patch, to save time.
- [ ] B. The allowed-file list should be set by the agent, because it has read the whole repository.
- [ ] C. The agent can propose minimal reproductions and edge inputs; the human decides what the rule is and which inputs count as the defect.
- [ ] D. The agent should make the final accept or reject call, because it can summarize the evidence.
- [ ] E. Running commands and capturing output suits the agent; choosing which command bears on which claim is the reviewer's job.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A test written alongside its own patch shares its writer's misunderstandings.
- B: The agent lacks knowledge of dependents, parallel work and release ownership, which determine scope.
- C: The requirement lives in the task and its owner, not in the code the agent reads.
- D: Accountability for the merge stays with the responsible person.
- E: Choosing evidence that actually bears on a claim requires judgment about what the claim is.

**Source:** The driver's seat

## MA-ch06.45

A student plans to let a coding agent write all the code and only review the output. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reviewing well depends on knowing how the thing should behave, and building your own version first creates a baseline to compare against.
- [ ] B. If the agent's version passes your tests, there is nothing left to learn from comparing.
- [ ] C. Comparing your version with the agent's by line count is a good way to learn from the comparison.
- [ ] D. An effective comparison names a difference in behavior, such as an edge case one version handles and the other does not.
- [ ] E. The ability to sense that a patch is off comes from the agent's explanation rather than from your own earlier work.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: You cannot audit what you do not know; a self-built baseline supplies the model that audits draw on.
- B: Passing your tests may only mean they miss the difference; comparing can expose gaps in them.
- C: Size and style say little about whether behavior differs.
- D: Behavioral differences reveal gaps in either implementation or in your tests.
- E: An explanation supplied by the code's writer cannot give the reader independent judgment.

**Source:** Build It: the baseline that lets you audit

## MA-ch06.46

A developer asks a coding agent to propose a deliberately wrong implementation that still passes the developer's tests, then checks by hand whether it does. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the agent fails to produce a passing wrong implementation, the tests are proven complete.
- [ ] B. This is a cheap way to find gaps in a test suite.
- [ ] C. A surviving wrong implementation should lead to a new test that fails it, which then joins the standard.
- [ ] D. Whether the tests are enough cannot be judged by the system they are testing.
- [ ] E. If such a wrong implementation passes, the tests are too weak.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Failure to find a survivor says little about whether one exists.
- B: Generating mutants and running the suite costs little compared with finding the gap in production.
- C: Closing the gap with a test that rejects the survivor turns the discovery into a lasting check.
- D: A test's adequacy is a judgment about the requirement, which the system under test does not own.
- E: A passing wrong variant is a surviving mutant by definition.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.47

A function returns a dictionary with a boolean `ready` and a list `reasons`. Its test suite has five tests; four assert only that `ready` is False for a failing case, and one asserts that `ready` is True for a passing case. No test inspects `reasons`. Wrong version W1 returns `ready` False for every call. Wrong version W2 computes `ready` correctly but always returns `reasons` as `["unknown"]`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A green suite shows that the `reasons` list is correct.
- [ ] B. A suite that asserts only a boolean cannot detect wrong explanations.
- [ ] C. Adding assertions on `reasons` for each failing case would catch W2.
- [ ] D. W2 passes every test in the suite.
- [ ] E. W1 is caught only by the test that expects `ready` to be True.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A green result reports on what the suite asserts, and nothing asserts the reasons.
- B: Whatever the suite does not assert, it does not check.
- C: Asserting the expected reasons for each failing case makes W2's constant list fail.
- D: W2's `ready` values are right and no test looks at `reasons`.
- E: W1's constant False satisfies the four failing-case tests and contradicts only the passing-case test.

**Source:** Build It: the baseline that lets you audit

## MA-ch06.48

A test is flaky: on correct code it fails 1 run in 10, and on a buggy variant it fails 1 run in 2 (assume independent runs). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The correct code passes five consecutive runs with probability about 0.9.
- [ ] B. A single pass is conclusive evidence that the code is correct.
- [ ] C. Five consecutive passes are about 19 times as likely under the correct code as under the buggy variant.
- [ ] D. Rerunning the test adds no information, because the outcomes are random.
- [ ] E. One passing run is 0.9 / 0.5 = 1.8 times as likely under the correct code as under the buggy variant, which is only modest evidence.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: 0.9^5 is about 0.59, not 0.9.
- B: A single pass is likely under both hypotheses, so it barely discriminates.
- C: 0.9^5 is about 0.59 and 0.5^5 is 0.03125, a ratio near 18.9.
- D: Repeated independent runs multiply likelihood ratios, so reruns are informative.
- E: Pass probabilities are 0.9 and 0.5, so the likelihood ratio for one pass is 1.8.

**Source:** Flags are claims about evidence

## MA-ch06.49

A coding agent is asked to fix a bug in an authentication module. Behavior in that module is overridden by a configuration file the agent never read. Its patch is coherent, well formatted and passes new tests the agent wrote. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reviewer should check which files the agent actually read or was given.
- [ ] B. Coherence of a diff does not show that the relevant information reached the agent.
- [ ] C. Pointing the agent at the relevant configuration file would address the cause more directly than polishing the patch.
- [ ] D. The agent's own new tests are independent evidence that the patch is grounded.
- [ ] E. Tidy formatting is evidence that the patch is grounded in the codebase.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The agent's inputs determine what its output could be grounded in.
- B: Fluent, internally consistent code can be built on an incomplete picture of the system.
- C: A source-grounding failure is fixed by getting the right material into context.
- D: Tests written from the same incomplete picture share its blind spot.
- E: Formatting reflects style conventions, not knowledge of the system.

**Source:** Which source material reached the system?

## MA-ch06.50

A developer lets a coding agent work in a throwaway git branch (or worktree) with the starting commit recorded. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Using a branch removes the need to review the diff.
- [ ] B. Letting the agent edit directly on top of the developer's uncommitted work is equally safe, because git can always recover uncommitted changes.
- [ ] C. Recording the starting commit lets the reviewer produce an exact diff of everything the agent changed in tracked files against that base.
- [ ] D. Edits the agent makes to files outside the repository are covered by the branch.
- [ ] E. If the result is bad, the branch can be discarded without affecting the main line.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Isolation limits damage; it says nothing about whether the change is right.
- B: Uncommitted changes are not recorded in git history, so they cannot generally be recovered if overwritten.
- C: A fixed base commit gives an unambiguous reference for the diff.
- D: Version control covers tracked files in the repository only.
- E: Isolation makes failure cheap to undo.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.51

Published guidance for agentic coding tools such as Claude Code recommends giving them executable ways to verify their work, such as tests and linters. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An agent that can run tests can iterate until they pass, which often improves its results.
- [ ] B. Executable checks make human review unnecessary.
- [ ] C. A failure that the agent resolves by weakening the test shows the verification loop has been gamed.
- [ ] D. Checks written by a person before the patch keep the standard fixed independently of what the agent changes.
- [ ] E. If the agent writes the tests it uses to check itself, a pass is independent confirmation.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Feedback from execution lets an agent correct mistakes it could not see by reasoning alone.
- B: Checks cover what they assert; scope, requirement validity and test quality still need human judgment.
- C: Changing the check instead of the code defeats the check's purpose.
- D: A fixed external standard prevents the target from moving with the implementation.
- E: Self-written checks inherit the agent's assumptions and can be tuned to pass.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch06.52

Two reviewers handle patches from an AI coding agent. Reviewer 1 approves them automatically because "it passed the tests." Reviewer 2 rejects every AI-written patch on principle. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Attribution still matters for the record of who contributed what.
- [ ] B. Knowing that a patch came from an agent changes what the code does.
- [ ] C. Review should rest on the proposal, its scope, the checks run and an accountable decision, whoever wrote the change.
- [ ] D. Both are substituting a rule about who wrote the change for evidence about the change.
- [ ] E. Reviewer 2's policy is the safe default because AI patches are unreliable.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Provenance of contributions is part of an honest packet even though it does not alter the diagnosis.
- B: Code behaves identically regardless of who or what wrote it.
- C: The same evidence-based standard applies to every proposal.
- D: One trusts by origin, the other distrusts by origin; neither examines the change.
- E: Blanket rejection discards good changes and teaches nothing about how to check bad ones.

**Source:** Keep the failure in the record

## MA-ch06.53

A team requires one human "approve" click on every agent-authored change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Requiring a click guarantees a meaningful review.
- [ ] B. Human approval becomes ceremonial when the evidence behind it is weak or the volume of changes exceeds reviewers' attention.
- [ ] C. The number of approvals is a good measure of review quality.
- [ ] D. The remedy for ceremonial review is to remove human review altogether.
- [ ] E. Increasing change volume while keeping the same reviewers always increases safety.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A click records an event, not that the reviewer understood the change.
- B: A sign-off that cannot be informed by the evidence or the reviewer's capacity is a ritual.
- C: Counting approvals measures throughput; quality shows in the reasons recorded and the defects caught.
- D: The remedy is to improve the packet and narrow the scope, not to remove accountability.
- E: More volume dilutes attention and raises the chance of unreviewed defects.

**Source:** Choose the verb the record supports

## MA-ch06.54

An agent implements exactly the rule in a ticket ("round prices down to the nearest dollar") and every test derived from the ticket passes. Finance later says prices should be rounded to the nearest cent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tests that encode the ticket cannot detect that the ticket itself is wrong.
- [ ] B. When the requirement is in doubt, the specification should be reopened instead of counting an exact implementation of the wrong rule as success.
- [ ] C. A larger test suite derived from the same ticket would have caught the error.
- [ ] D. Passing tests show that the requirement was valid.
- [ ] E. Confirming the requirement with the people who own it is part of the inputs to a review.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Tests check implementation against a specification, not the specification against the need.
- B: Perfect implementation of the wrong rule is still failure for the task.
- C: More tests from the same source reproduce the same error.
- D: Agreement between code and tests says nothing about whether either matches what the business wants.
- E: The requirement's owner decides what the requirement is; the code cannot supply it.

**Source:** A worked decision from beginning to end

## MA-ch06.55

An engineer distinguishes two kinds of evidence. A call `old(2)` returns 1 where the requirement says 3. Reading the source shows the expression `x - 1`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Inspection evidence alone suffices to show how the function behaves for all inputs in all environments.
- [ ] B. The failing call is behavior evidence and the source reading is inspection evidence.
- [ ] C. The two should be merged into one entry to keep the record short.
- [ ] D. Observing the wrong output proves which expression caused it.
- [ ] E. The behavior evidence can exist before anyone has read the source.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Reading code does not establish behavior under every runtime condition.
- B: One is an observation of what runs; the other is a reading of what the code says.
- C: They support different claims and should be recorded separately.
- D: The observation contradicts the requirement; locating the cause is a separate step.
- E: Running the function requires no knowledge of its source.

**Source:** Whose test is it? Reproduce before you repair

## MA-ch06.56

A team writes a stop condition before any patch exists: the patch does not move forward until (1) the regression test was saved before the plan, (2) the plan names only files on the allowed list, and (3) the test and the existing suite were run against the current diff with commands and exit status recorded. The team also keeps a known wrong implementation that the checks must reject. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Parts of the condition can be checked mechanically, but the allowed list itself must come from a person who decided it.
- [ ] B. If the checks cannot distinguish the known wrong implementation from the correct one, the standard is finished.
- [ ] C. Condition (1) can be checked afterward with a file timestamp or a commit.
- [ ] D. A stop condition written after reading the test output is equally credible.
- [ ] E. Keeping a known wrong implementation shows whether the test and scope checks can tell wrong from right.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Scripts can compare sets and timestamps, but the decision about what the change should touch is a judgment about the task.
- B: If a known wrong version passes, the standard is too weak and needs more work.
- C: Timestamps and commit history make ordering claims verifiable.
- D: A criterion written after the fact is fitted to the outcome and tests nothing.
- E: Running the checks against a known-bad candidate validates the checks themselves.

**Source:** The gate: reproduction, test, and scope, before the patch

## MA-ch06.57

A team using a coding agent such as Claude Code wants to guarantee that it never edits files under `migrations/`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The instruction file alone provides a hard guarantee.
- [ ] B. A permission rule that denies edits to that path enforces the restriction at the tool level.
- [ ] C. Writing "do not edit migrations" in a project instruction file the agent reads at startup is guidance the model usually follows but does not technically prevent edits.
- [ ] D. A continuous-integration check on changed filenames detects violations after they happen.
- [ ] E. Because the agent replied that it understood the rule, the rule is enforced.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Text instructions can be ignored, misread or overridden by later context.
- B: Permission rules are applied by the tool layer regardless of what the model intends.
- C: Instructions are text in the model's context and influence behavior without enforcing it.
- D: A post-hoc filename check finds violations but does not prevent them.
- E: A statement of understanding is a generated sentence, not a control.

**Source:** Scope is a testable property, not a mood

## MA-ch06.58

A reviewer reads the agent's natural-language description of its change instead of the diff. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing the agent's list of changed files with the actual diff is a cheap consistency check.
- [ ] B. The description is a second-hand account; the diff is the change.
- [ ] C. If the descriptions were accurate in 9 of the last 10 sessions, they can replace the diff.
- [ ] D. The description is more reliable than the diff because it is written in natural language.
- [ ] E. A description can omit or mischaracterize changes that the diff would show.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Mismatch between claimed and actual changes is a red flag that costs little to check.
- B: The narration is generated text about the work; the diff is the work.
- C: A 90 percent record still leaves one in ten sessions with an inaccurate account, and the unreliable one cannot be told in advance.
- D: Natural language is not evidence; the diff is the primary artifact.
- E: Omissions and mischaracterizations are exactly what an independent reading of the diff catches.

**Source:** Read a diff as a behavioral proposal
