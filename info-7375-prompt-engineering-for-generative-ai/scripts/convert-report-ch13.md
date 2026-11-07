# Convert report: ch13-evaluation-and-approval-gates (MA-ch13)

Old MA 72, old essay 62, new MA 36 (true-counts: 1T x4, 2T x12, 3T x13, 4T x7). Dropped/merged MA: 36 (hash/canonicalization, JSON duplicate-key, fingerprint, expiry, single-use and reviewer-capacity variants merged; arithmetic/probability/code-trivia items such as the 0.7 trial calculation, SHA-256 key-order and `not proposal.get` truthiness items reduced to the term involved or removed).
Essays: 62 old; vocabulary-bearing skills converted into MA content (approval request fields, evaluation vs authorization, binding, replay, expiry/revocation, fail closed, rubber-stamping, sign-off, ownership bias, standing policy, TOCTOU, plan vs apply). NOT CONVERTED: the confidence-interval and pass@k calculation essays (calculation), backlog and 10x-volume arithmetic essays (calculation), the "review the following gate code, find four defects" essay (code procedure), the threat-model and sign-off-critique essays (design opinion/procedure), the ordered-case-list design essay (design).

## Terms tested (term :: definition)
### Evaluation and approval gates
approval gate :: checkpoint where a proposed action waits for a recorded decision by an authorised person
proposal :: description of the action shown to the reviewer before it runs
decision record :: stored verdict naming approver and what it applies to
evaluation vs authorization :: measuring behaviour against criteria vs granting permission for an action
permission vs approval :: standing rule about what a tool may do vs a decision about one proposed action
target / effects / rollback / evidence :: the object acted on / what will change / how to undo / checkable support
irreversible, blast radius :: effect cannot be undone; how far damage spreads
least privilege :: grant the narrowest permissions the task needs
test case, grader, evaluation set, regression, flaky :: input with expected outcome; scorer; collection of cases; formerly working behaviour that fails; inconsistent result on same input
circular evaluation :: expectation written after seeing output
trace, outcome grading, hallucination :: record of tool calls; grading the real result not the agent's summary; unsupported claim stated as fact
coverage, edge case, negative case, class imbalance :: breadth of situations tested; boundary input; case where refusing is right; uneven outcome mix
precision, recall, false positive, false negative :: share of flags that are right; share of real cases caught; safe case flagged; real case missed
proxy metric, Goodhart's law, guardrail metric :: stand-in measure; target stops measuring; watched side-effect measure
LLM-as-judge, rubric, calibration, self-preference bias :: model scoring outputs; written criteria; aligning judge with human labels; favouring own style
confidence interval :: plausible range for the true rate
pass@k, pass^k, trial :: at least one of k succeeds; all k succeed; one attempt
hash, digest, fingerprint, canonicalization :: one-way fixed-length output; digest of exact content; agreed serialised form before hashing
digital signature :: binds a digest to a key holder
content / scope / identity binding :: tie to exact proposal / environment, deadline, uses / authenticated approver
time-of-check to time-of-use (TOCTOU) :: gap between verifying and acting
single-use, race condition, atomic, replay, idempotent :: one consumption; timing-dependent outcome; indivisible step; reuse of valid record; repeat gives same result
expiry, revocation :: automatic end of validity; explicit early withdrawal
fail closed / fail open :: deny / allow when the check cannot complete
rubber-stamping, approval fatigue, automation bias :: approval without examination; quality decline from volume; over-trusting system output
triage, batching, throttling, escalation :: ranking by risk; grouping similar items; limiting proposal rate; routing to expertise
standing policy, allowlist, sandbox :: pre-authorised class; permitted-only list; isolated environment
mutable vs immutable reference :: can change after reading vs fixed
audit log :: tamper-resistant event record
sign-off, ownership bias, independent review :: signed accountability statement; overvaluing own work; reviewer other than builder
dry run, drift :: preview without doing; difference between reviewed and live state
test oracle, mutation testing, diff review :: source of correct answer; seeded defects to test the tests; reading changes
stub / mock :: stand-in for a dependency in tests
