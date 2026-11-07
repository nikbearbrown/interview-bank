# Convert report: ch06-claude-code-and-diff-review (MA-ch06)

- Old MA: 58. Old essays: 61. New MA: 36 (true-counts: 3 one, 13 two, 13 three, 7 four). check_format: 0 problems; forbidden-word grep on statements clean.
- Dropped/merged old MA: 22 (examples: MA-ch06.6, .7, .47 clamp/mutant/W1-W2 computations merged into the mutant and known-wrong questions; .17/.18 line-count and review-speed merged; .48 flaky-test odds dropped as calculation; .50/.51 branch and verify-guidance trimmed; .53, .52, .45, .44 policy and division-of-labour opinion dropped or folded into the claim-vs-evidence questions).
- Essays converted (folded into MA content, same-contrast essays merged): ES-ch06.2, 3, 4, 6, 8, 9, 12, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 50, 52, 54, 55, 56, 58, 59, 60 (approximately 43 of 61).
- NOT CONVERTED: ES-ch06.1, 5, 7, 51 (design or compute test inputs and mutant predictions); ES-ch06.10, 11, 15, 28 (read-this-code/diff and compute outputs); ES-ch06.13/14 (line-count and hours arithmetic, only the risk-over-size contrast kept); ES-ch06.27 (probability calculation); ES-ch06.35, 39, 48, 49, 53, 57, 61 (design opinion or tradeoff discussion with no distinct term).

## Terms especially tested (for the glossary)

### Claude Code and diff review
regression test :: a test that checks behaviour that was fixed or established has not broken again; it fails on the unfixed code and passes after the fix
reproduction :: the input, observed output and expected output that trigger a reported failure
diagnosis :: the explanation of the cause of a failure
oracle :: the trusted source of the expected value, such as the written requirement
mutant :: a deliberately altered, wrong variant of code used to test a test suite
killed mutant / surviving mutant :: a mutant the suite detects (fails on) / one the suite passes, pointing to behaviour not checked
equivalent mutant :: a mutant that behaves the same as the original, so no test can kill it
known wrong implementation :: a version the checks must reject, used to test the tests
hard-coding :: returning the expected answer for the tested input without implementing the rule
weakening a test :: editing an assertion to match the output instead of fixing the code
harness error vs test failure :: an error stops the run before assertions about the patch; a failure is a false assertion
unified diff, hunk, context lines :: textual change format; a hunk is a block of changes with surrounding unchanged lines
git diff vs git diff --staged vs git status :: working tree vs index; index vs last commit; status lists untracked files
side effect :: a change outside the reviewed output, such as an installed package or a database migration
scope / allowed-file list / scope creep :: the files the agent may change / the list itself / changes beyond it
scope check (set difference) :: changed files minus allowed files; sees file names, not content
planning before acting (plan mode) :: the agent proposes a plan and makes no edits until it is approved
permission rule (allow, ask, deny) :: tool-level control of what Claude Code may do
approval gate :: a point where a person decides whether a result moves forward
hook :: a user-defined command that runs at a point in the agent lifecycle and can block an action
CLAUDE.md (instruction file) :: guidance the model reads; it is not enforcement
detective vs preventive control :: finds a problem after the fact vs stops it happening
claim vs evidence :: a statement or boolean vs the recorded command, exit status and commit
stale evidence :: a result gathered before the code last changed
binding approval to a hash/digest :: tying a decision to the exact version approved
plausibility judgment vs verification :: the reviewer's own prediction before running vs a check against an external source
falsifiable prediction (verdict, target, mechanism) :: a written prediction naming what would change the reviewer's mind
not-checked list :: the stated limits of a sign-off
claim calibration :: matching claim strength to evidence strength
verification vs validation :: checking against the stated requirement vs checking that the requirement is right
contribution record / session transcript :: what the agent drafted and the person decided, backed by the transcript
