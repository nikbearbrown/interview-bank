# Conversion report: ch15-supervised-capstone (MA-ch15)

- Old MA: 66. Old essays: 65. New MA: 36 (0 essays).
- Dropped/merged old MA: 30 net (near-duplicates merged, e.g. MA-ch15.1-3 and 6-7 folded into the validator and format-check items; MA-ch15.9-10, 24-25, 28 folded into success-criteria and bounded-project items; MA-ch15.41 and 66 reduced to a single point each; non-vocabulary arithmetic dropped: MA-ch15.24 review-effort count, MA-ch15.41 failure-rate calculation, MA-ch15.62 option scoring).
- Essays converted into MA content: about 57 of 65, folded by shared contrast (validator/containment ES 1-4, 6; acceptance/spec ES 8-14; control vs instruction ES 15-18; capability/approval ES 19-21; evidence/claim graph ES 5, 25, 29, 47-49; verification ES 30-33, 35; reviewer ES 36, 39-46; sign-off/options ES 52-57, 59-61; failures ES 64-65).
- NOT CONVERTED: ES-ch15.37 (compute a failure-rate bound; calculation), ES-ch15.38 (sampling probability calculation; only the sampling-limit idea kept), ES-ch15.58 (option scoring arithmetic), ES-ch15.62 and 63 (reflection/opinion), ES-ch15.22 (design choice among proposals; opinion), ES-ch15.14 (process advice on session records), ES-ch15.7 and 27 (partly folded; open design discussion), ES-ch15.43 (gap list; opinion on process).

## Terms tested (term :: definition)

### Validation and evidence
- structural check :: a check of presence, location and length of files, not their content
- substantive check :: a judgment of what a file says and whether it does its job
- containment check :: test that a file's resolved path lies inside an allowed folder
- resolved path :: the real location of a path after following symbolic links
- symbolic link (symlink) :: a file that points to another path, possibly outside the folder
- false accept / false reject :: a check passing what it should reject / blocking what it should allow
- proxy measure :: a measurable stand-in correlated with the property you care about
- Goodhart's law :: a measure that becomes a target stops measuring what it stood for
- format (schema) check :: test of the shape of output, such as keys and types
- grounding :: tying each claim to supporting source text
- unsupported citation :: a citation present but not supported by the cited passage
- hallucination :: fluent content without a basis in the source

### Specification and testing
- acceptance criteria / acceptance tests :: conditions fixed in advance that define done and judge the output
- success criterion, falsifiable :: a pass or fail condition that a result could contradict
- non-goal :: something the project declines to do, bounding scope
- specification defect :: an ambiguity or gap in the stated requirement
- baseline :: a hand-built reference version to compare against
- adversarial test case :: input chosen to break the function at its boundaries
- stub :: a scripted stand-in for the model call, giving repeatable tests
- planted defect :: a deliberate flaw inserted to test whether a check detects it
- pre-registered prediction :: a prediction written before the run so the result can contradict it
- pre-mortem :: imagining the project has failed to list failure modes before building
- evaluation harness, task, trial, grader :: tasks with success criteria, repeated runs, and a scorer
- transcript vs outcome :: record of the steps vs the final state of the environment
- trace :: step-by-step record of requests, tool calls and results
- read-back :: observing the real state after an action instead of trusting the tool's report
- independent verification :: a check using a different method or source than the producer
- false positive / false negative (reviewer) :: reported problem that is not real / real problem not reported
- reproducibility :: others can rerun the work from recorded commands, inputs and versions
- cherry-picking :: selecting favourable runs or cases and hiding the rest

### Control and agents
- prompt injection :: instruction hidden in content the model reads as data
- trust boundary :: line between trusted instructions and untrusted input
- allowlist :: fixed list of permitted tools or values the controller checks
- capability vs permission :: what the agent can do vs what it is allowed to do
- action surface :: the set of actions an agent can take
- approval gate :: a pause until a person approves a specific proposed action
- stale approval :: an approval that no longer matches the changed proposal
- stop condition, token budget, iteration cap :: rules that end an agent loop and bound cost
- idempotency, idempotency key :: repeated calls give the same result; key lets the API recognise a retry
- advisory output :: model comments that inform but do not decide

### Judgment and sign-off
- claim-to-evidence graph :: table linking each claim to the evidence that supports it
- unsupported claim :: a claim with no linked evidence
- circular evidence :: a document justified by what it says about itself
- limitation statement :: a sentence saying what was not tested or established
- sign-off :: a named person's acceptance of accountability for the claims
- ship / narrow / defer / stop :: deploy fully / deploy reduced scope / postpone with named evidence / end
- handoff test :: observing whether someone else can run the work from written instructions alone
- attribution and licence :: crediting and following terms for adapted code
