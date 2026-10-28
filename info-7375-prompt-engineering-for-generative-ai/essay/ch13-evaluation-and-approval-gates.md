# Chapter 13: Evaluation and approval gates

## ES-ch13.1

A reviewer is shown a proposal to write a file named report.md. She reads the supporting evidence and clicks Approve, and the system stores a record containing "approved", her name and a timestamp. Later, before the write happens, the target of the proposal is changed to a different path. Explain how the stored approval can still appear valid even though the thing it approved no longer exists, and describe the technical measure that prevents this.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that the record attests only that someone said yes, at a time, under a name; none of those three facts identifies what was approved.
2. Explains that after the target changed, the old yes would be presented as permission for an action the reviewer never saw.
3. Proposes binding the decision to the exact proposal content, for example a hash of a canonical serialization of the whole proposal, stored with the decision.
4. States that the fingerprint must be recomputed from the proposal about to execute and compared with the stored value at the point of the effect.
5. Explains that a mismatch must send the changed proposal back to review as a new decision, and notes that content binding does not show who approved or that anyone read it.

**Source:** A gate is not a button

## ES-ch13.2

An agent harness asks a human "Allow the agent to run this command?" and shows only the command name and two buttons. Explain what information a reviewer needs before a yes can be meaningful, and why each item is needed.

**Points:** 5

**Rubric (1 point each):**

1. Names the specific action to be performed, stated precisely enough to show what operation will occur.
2. Names the resolved target (path, account, environment or recipient) rather than a friendly label that could refer to several objects.
3. Requires a reason that ties the action to the user's task, because capability or permission alone does not show the action is wanted.
4. Requires the anticipated effects, including external and irreversible ones, and the evidence supporting the decision to proceed, as references that can be checked.
5. Requires an honest statement of how the action could be undone, including when recovery is partial or impossible, and explains that this shifts the burden from the reviewer to the request.

**Source:** A gate is not a button

## ES-ch13.3

Explain the difference between an approval request that is structurally complete and one that is substantively adequate. Give a concrete example of a request that is complete but inadequate, and describe which mechanisms can catch each kind of problem.

**Points:** 5

**Rubric (1 point each):**

1. Defines structural completeness as the required fields being present and well formed, which a schema or validator can check mechanically.
2. Defines substantive adequacy as the content being specific, accurate, and credible for the action, which presence checks cannot judge.
3. Gives a valid example, such as evidence that reads only "looks good" or effects listed as "none" for a destructive action, that passes a presence check.
4. Describes mechanisms for substantive problems: reviewer judgment, links to checkable artifacts, domain-expert review, and graders whose scores are treated as evidence rather than decisions.
5. States that a passing validator should be reported as a structural result and not as an assessment of the proposal's quality or safety.

**Source:** A gate is not a button

## ES-ch13.4

An agent requests approval to "update the shared config". Explain why a display name or relative path is an inadequate description of the target in an approval request, and describe what the request should contain instead.

**Points:** 5

**Rubric (1 point each):**

1. Explains that one name can refer to several objects, such as files in different directories or in different environments.
2. Gives examples of how the real target can differ from the displayed one, such as symbolic links, relative paths, or ".." segments.
3. States that the request should show a resolved identity, such as the canonical absolute path, account, environment, or recipient.
4. Notes that the consequential difference (for example, a file shared with other teams or a production system) is often exactly what the friendly name hides.
5. Explains that the reviewer cannot be expected to discover this unaided, so the interface and request format must surface it.

**Source:** A gate is not a button

## ES-ch13.5

In an automated review pipeline for agent actions, define evaluation and authorization, explain why they should be kept distinct, and say what a test suite, a policy checker, and a model-based grader can and cannot decide.

**Points:** 5

**Rubric (1 point each):**

1. Defines evaluation as producing evidence about what happened or could happen and how well a proposal meets stated criteria.
2. Defines authorization as a decision by a responsible person or policy that the action may proceed; it spends the evidence evaluation produced.
3. Explains that merging the two on one screen makes a passing score look like permission and hides who made the decision.
4. States that a test suite evaluates selected behaviors but cannot decide whether a destructive change is worth making.
5. States that a policy checker flags rule violations but cannot judge exceptions, and that a model grader's score is evidence with its own failure modes and not a decision.

**Source:** Evaluation comes before authorization

## ES-ch13.6

A team watches an agent attempt ten tasks, then writes evaluation cases around what it did and adjusts expected answers until all ten pass. Explain what is wrong with this process and describe the order of work that keeps an evaluation capable of finding problems.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that the criteria were chosen after seeing the outputs, so the passing result records accommodation to the observed behavior.
2. Explains that such an evaluation could not have failed, so a pass tells the reader little about the system.
3. Recommends deciding in advance what outcomes would count as evidence against the proposal, before looking at evidence in its favor.
4. Recommends including cases chosen to embarrass the system: boundary conditions, refusal cases, and structurally complete but weak inputs.
5. Recommends recording expected outcomes before running, and documenting any later change to an expectation with its reason.

**Source:** Evaluation comes before authorization

## ES-ch13.7

An agent is asked to close inactive accounts. The database tool logged a single successful UPDATE with "42 rows affected", but the agent's final message says it closed 99 accounts. Distinguish trace evidence, narration, and outcome evidence, and design an independent check that could contradict the agent's claim.

**Points:** 5

**Rubric (1 point each):**

1. Defines trace evidence as the record of what commands or calls were made and what they returned.
2. Defines narration as the agent's own statement of what happened, which can be fluent and wrong.
3. Defines outcome evidence as an observation of the resulting state of the system, separate from the agent's actions and statements.
4. Designs a post-action check, such as an independent query counting accounts in the closed state before and after, compared with the expected number.
5. Explains what the check establishes and its scope, noting that it covers only the state it queries and not other side effects.

**Source:** Evaluation comes before authorization

## ES-ch13.8

A team reports that a file-writing agent "passed 20 of 20 evaluation cases", where every case wrote an ordinary text file into an empty directory. Explain what the result does and does not show, and what the team should record so that readers can interpret it.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the result shows the agent handled the kinds of situations the cases covered.
2. Lists situations left untested, such as symbolic links, permission errors, concurrent changes, path traversal, existing files, or private data.
3. States that a pass count cannot be interpreted without knowing which cases ran and why they represent the intended use.
4. Recommends recording exclusions beside the result, so that a reader can see where the evidence stops.
5. Recommends adding cases designed to expose boundary and refusal behavior rather than more cases of the same kind.

**Source:** Evaluation comes before authorization

## ES-ch13.9

An evaluation set for an agent that decides whether to carry out file operations has 30 cases whose correct behavior is to proceed and 10 whose correct behavior is to refuse. Calculate the score an always-proceed agent and an always-refuse agent would each receive, and explain what this shows about designing and reporting such evaluations.

**Points:** 5

**Rubric (1 point each):**

1. Computes the always-proceed agent's accuracy as 30 of 40, or 75%.
2. Computes the always-refuse agent's accuracy as 10 of 40, or 25%.
3. Explains that a single accuracy figure can make a useless policy look respectable, and that the result depends on the mix of cases.
4. Recommends reporting the rate for each class of case separately (for example, correct proceeds and correct refusals).
5. Explains that a set with no should-refuse cases cannot distinguish a careful agent from an indiscriminate one.

**Source:** Evaluation comes before authorization

## ES-ch13.10

After a redesign of its approval screen, a team celebrates that median time to approval fell sharply. Explain why optimizing one such metric can make an approval process worse, name at least four measurements that can pull against each other, and describe how results should be reported.

**Points:** 5

**Rubric (1 point each):**

1. Explains that time to approval can fall because reviewers click reflexively or because the screen hides detail, not because review became more efficient.
2. Names task success as one measure that may rise while others worsen.
3. Names the rate of invalid or later-reversed actions as a measure of whether decisions were well informed.
4. Names reviewer burden and refusal or deferral rates as further measures that can move in opposing directions.
5. Recommends reporting a portfolio of measures together, including errors and deferrals, and not a single celebratory number.

**Source:** Evaluation comes before authorization

## ES-ch13.11

A team uses a language model to grade free-text rollback plans against a rubric. Describe the failure modes of this approach, how the team should calibrate it, and how it should be combined with other kinds of checks.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that fluent, detailed prose can score well while omitting an irreversible side effect or being factually wrong.
2. Identifies that graders sharing a prompt, rubric assumption, or source error can agree and still be wrong together, so agreement is not independent confirmation.
3. Recommends calibrating the grader against human-labeled examples and analyzing its failures before trusting its scores.
4. Recommends pairing it with deterministic checks wherever the property can be checked mechanically.
5. Recommends human review proportional to the stakes, and treating the grader's output as evidence for that review rather than as the decision.

**Source:** Evaluation comes before authorization

## ES-ch13.12

A prototype approval gate passes all 8 of 8 evaluation cases. Assuming the cases were independent random draws from real usage, compute the approximate 95% upper confidence bound on the true failure rate (using 1 - 0.05^(1/8), and the "rule of three" shortcut 3/n), and explain what the team can and cannot responsibly claim.

**Points:** 5

**Rubric (1 point each):**

1. Computes the exact bound as about 31% (1 - 0.05^(1/8) = 0.312).
2. Computes the rule-of-three approximation as 3/8, or about 37.5%, and notes it is a rough upper estimate.
3. Explains that zero failures in a small sample leaves a wide range of plausible true failure rates.
4. Explains that hand-picked cases are not a random sample and so do not support a population reliability figure at all.
5. Recommends reporting the cases and what they covered and excluded rather than a reliability percentage.

**Source:** Evaluation comes before authorization

## ES-ch13.13

An agent succeeds on a task independently with probability 0.9 on each attempt, and is evaluated with 5 trials per task. Compute the probability of at least one success and the probability that all five trials succeed, and explain which measure matters for a destructive action that must be right every time and which for a task where failures can simply be retried.

**Points:** 5

**Rubric (1 point each):**

1. Computes the probability of at least one success as 1 - 0.1^5 = 0.99999.
2. Computes the probability of all five succeeding as 0.9^5, about 0.59.
3. Explains that the gap between the two shows how much a single headline number can hide about consistency.
4. States that for an action that causes harm when it fails, the all-trials (consistency) measure is the relevant one.
5. States that for cheaply retried tasks with verifiable results, the at-least-one measure can be appropriate, and that single trials are not enough for a nondeterministic system.

**Source:** Evaluation comes before authorization

## ES-ch13.14

During an evaluation run, one case produces a result different from the expected outcome written down beforehand. Describe how a team should handle the discrepancy and why simply editing the expectation is a problem.

**Points:** 5

**Rubric (1 point each):**

1. States that the discrepancy may come from the implementation, the test's expectation, or the original requirement.
2. Recommends investigating each possibility rather than assuming the implementation is at fault.
3. Explains that silently editing the expectation to match the output turns the evaluation into accommodation.
4. Recommends recording any change to an expectation or requirement, with the reason and the date.
5. Notes that a surprising result, harmless or not, should feed into the next version of the evaluation set.

**Source:** Evaluation comes before authorization

## ES-ch13.15

Explain why an evaluation of an agent should keep full transcripts and tool traces yet grade outcomes, and say what a useful record for each evaluation case contains.

**Points:** 5

**Rubric (1 point each):**

1. Explains that transcripts and traces show what the agent said and did, which helps diagnose failures.
2. Explains that outcomes are the resulting state of the world, and an agent can claim success without that state having changed.
3. States that the record should contain the task input and the expected behavior, written in advance.
4. States that the record should contain the actual output, the checker used, and the rationale for any discrepancy.
5. Explains that a single aggregate score discards the trace of what failed, which is what a reviewer most needs to see.

**Source:** Evaluation comes before authorization

## ES-ch13.16

Two services each build the same approval proposal as a Python dictionary, inserting the keys in different orders, and each hashes the output of json.dumps with SHA-256. The digests differ. Explain why serialization must be canonical before hashing, which choices make Python's output canonical for this purpose, and what additional problems remain if the services are written in different languages.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a hash operates on bytes, and equivalent data serialized differently produces different bytes and so different digests.
2. Identifies that dictionary insertion order leaks into the output, although JSON objects have no meaningful key order.
3. Names sorting the keys as the fix for order, and fixed separators (no optional whitespace) and a fixed encoding such as UTF-8 as fixes for formatting.
4. Names cross-language problems such as number formatting (1 versus 1.0), Unicode normalization, string escaping, and duplicate keys.
5. Recommends a written canonicalization specification (such as RFC 8785) shared by both services, and notes that the canonical form decides what counts as the same proposal.

**Source:** Canonical content and its fingerprint

## ES-ch13.17

A system stores a SHA-256 digest of each approval request in a log and treats it as proof of approval. Explain what a digest of a proposal does establish, what it does not establish, and which additional mechanisms would be needed to establish the rest.

**Points:** 5

**Rubric (1 point each):**

1. States that a digest establishes content identity: a changed proposal produces a different digest, so a stored value detects modification.
2. States that a digest does not provide secrecy, since anyone who has or can guess the content can compute it and compare.
3. States that a digest does not establish who produced the record, because no secret is involved in computing it.
4. States that it does not show that a person read or understood the proposal, or had authority to approve it.
5. Names mechanisms for the rest: digital signatures or keyed MACs for authenticity, authenticated sessions or credentials for identity, an authority registry, and processes for review quality.

**Source:** Canonical content and its fingerprint

## ES-ch13.18

Approval gates must decide what counts as "the same proposal". Discuss the difference between comparing exact bytes and comparing meaning, using path spellings and symbolic links as examples, and explain the trade-off between false rejections and false acceptances.

**Points:** 5

**Rubric (1 point each):**

1. Explains that fingerprinting a string treats two spellings of the same file, such as "./report.md" and "report.md", as different proposals.
2. Explains that an identical string can refer to a different object later, for example when a symbolic link is repointed or a mutable name is reassigned.
3. Recommends binding resolved identifiers, immutable versions, or content hashes of the object in high-stakes cases.
4. Explains that false rejections (re-asking over irrelevant differences) cost reviewer attention and breed fatigue.
5. Explains that false acceptances (reusing approval for a consequentially different action) defeat the approval gate, so the canonical form should erase noise but preserve every consequential difference.

**Source:** Canonical content and its fingerprint

## ES-ch13.19

A Python gate rejects a proposal if `not proposal.get(field)` is true for any of six required fields. Explain which inputs this check rejects and accepts, why that is not a check of meaning, and how the validation could be strengthened and what limits would remain.

**Points:** 5

**Rubric (1 point each):**

1. States that falsey values such as empty strings, empty lists, None, 0 and False are rejected.
2. States that any non-empty string is accepted, including whitespace only, "0", "n/a", or fluent but meaningless text.
3. Explains that the check tests presence and form, not whether the content is adequate for the action.
4. Suggests stricter checks: required types, trimmed non-empty strings, length or format limits, and references to artifacts that can be resolved.
5. States that even strict validation cannot judge adequacy or credibility, which still need reviewer judgment.

**Source:** Canonical content and its fingerprint

## ES-ch13.20

A review interface and a backend both receive the same JSON text, {"target":"report.md","target":"/etc/passwd"}. The interface parser keeps the first value of a repeated key and the backend parser keeps the last. Explain what goes wrong, why hashing the text does not fix it, and how to prevent the problem.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the reviewer sees one target while the executor acts on another although both processed identical bytes.
2. Names this as a parser differential: different parsers resolve duplicate keys differently, and the standard leaves this behavior unspecified.
3. Explains that a digest of the raw text only shows the bytes are unchanged, not that the two sides interpret them alike.
4. Recommends rejecting documents with duplicate keys at ingestion with a strict parser.
5. Recommends parsing once, then fingerprinting and executing the same parsed canonical object, so the reviewer sees what runs.

**Source:** Canonical content and its fingerprint

## ES-ch13.21

Describe in prose the conditions under which a stored decision record should authorize a single attempt at an action, and explain why each condition exists.

**Points:** 5

**Rubric (1 point each):**

1. States that the decision must be an explicit, strictly typed approval, not merely a truthy value, because loosely typed values such as "no" can evaluate as true.
2. States that the approver must be identified, ideally by an authenticated identity with authority for this action, not just a nonblank string.
3. States that the recorded fingerprint must equal a fresh fingerprint of the exact proposal about to execute, computed at the point of the effect.
4. States that the decision must be unexpired, not revoked, and not already used, and that scope such as environment is checked.
5. States that absence, silence, timeouts, model confidence or favorable automated scores authorize nothing, and that refusal and deferral are legitimate recorded outcomes.

**Source:** The approval predicate

## ES-ch13.22

A workflow computes the fingerprint when the proposal is shown to the reviewer and, at execution, only checks that a well-formed fingerprint is stored with the decision. Explain the time-of-check to time-of-use problem this creates, how to close it, and what the fix still does not guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Describes the gap: the proposal can change between review and execution, and the stored value then no longer describes what runs.
2. Explains that the executor's check compares the decision with itself and so passes whatever content is run.
3. States that the fingerprint should be recomputed from the exact object about to be executed, at the effect boundary.
4. Recommends freezing or copying the reviewed representation so that it cannot be mutated unnoticed, and failing closed on mismatch.
5. Notes that the fix does not show that anyone read the proposal, who they were, or that the action will have the intended result.

**Source:** The approval predicate

## ES-ch13.23

A decision record contains approved=true, an approver name, and a fingerprint matching the current proposal. List at least five claims a reader might be tempted to make from this record and classify which are supported and which are not, with the reasoning.

**Points:** 5

**Rubric (1 point each):**

1. Classifies as supported that the record was written against this exact proposal content.
2. Classifies as unsupported that a particular named person approved, since a name in a record is not authenticated.
3. Classifies as unsupported that the person had authority over the target or data.
4. Classifies as unsupported that anyone read or understood the proposal, or had time to.
5. Classifies as unsupported that the proposal is safe, or that the action will succeed or remain authorized, because expiry, revocation, and use limits are not checked by these three fields alone.

**Source:** The approval predicate

## ES-ch13.24

Approval can fail through three different person-level gaps: the wrong person acts under someone's name, the person has no authority over the action, or the person does not actually examine the proposal. For each, name a control and the residual risk that remains.

**Points:** 5

**Rubric (1 point each):**

1. For wrong person: names authenticated identity controls such as strong authentication or signed decisions.
2. For wrong person: states a residual risk such as stolen credentials, shared accounts, or an insider acting under another's account.
3. For missing authority: names a registry or policy mapping actions or data to roles that may approve them, with escalation to the right owner.
4. For missing authority: states a residual risk such as stale role assignments or delegation that is not tracked.
5. For missing comprehension: names interface design, workload limits and review practice as the controls, and states the residual risk that no technical check can prove a human attended.

**Source:** The approval predicate

## ES-ch13.25

A developer writes `if decision["approved"]:` in the check, while another writes `if decision.get("approved") is True:`. Explain the difference in behavior, give an example input that distinguishes them, and state the general design principle for code that makes authorization decisions.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the first accepts any truthy value, so the string "no" or "false", a non-empty list, or the number 1 would pass.
2. Explains that the second accepts only the Boolean True object.
3. Gives a concrete distinguishing input such as {"approved": "no"}.
4. States the principle that authorization checks should be strict, explicit and fail closed, with anything unexpected treated as a denial.
5. States that a test for each rejected form (wrong type, missing key, blank approver) is needed, since a permissive implementation can pass tests that only check valid cases.

**Source:** The approval predicate

## ES-ch13.26

A decision authorizes one action, but two workers receive the same valid decision at the same moment. Explain how a naive "check unused, run, mark used" flow can execute the action twice, and design a correct single-use mechanism including how to handle a crash during execution.

**Points:** 5

**Rubric (1 point each):**

1. Describes the race: both workers can read the flag as unused before either records use.
2. States that checking and claiming must be one atomic operation at the point of effect, such as compare-and-set, a transaction, or a unique constraint.
3. Notes that a content fingerprint alone does not limit how many times a decision is presented.
4. Proposes distinguishing states such as unused, claimed or in progress, and completed.
5. Explains how to handle a crash: the claimed state shows an attempt may be partially applied, so retry needs a deliberate decision (possibly a new approval) and should not be automatic.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.27

Design the expiry rules for an approval decision. Cover the time basis, boundary handling, testing, and the circumstances in which a decision should become invalid before its deadline.

**Points:** 5

**Rubric (1 point each):**

1. Requires an unambiguous time basis, such as UTC instants, since a local time without a zone is ambiguous.
2. Requires a stated comparison policy for the boundary, such as whether the deadline moment itself is still valid.
3. Recommends passing the current time into the check as a parameter, so that tests can assert behavior just before and after the deadline without waiting.
4. Explains that approvals can become invalid before expiry because the evidence, environment, classification, or other premises changed.
5. Recommends binding the premises that matter or checking for staleness at execution, so that changed premises force a new review.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.28

Design a revocation mechanism for approvals. State what should be recorded, where revocation must be enforced, and how to handle work that has already started.

**Points:** 5

**Rubric (1 point each):**

1. Requires recording who revoked, under what authority, when, and which decision or proposal is affected.
2. Requires that the execution-time check consult revocation state at the effect boundary, otherwise revocation is merely advisory.
3. Requires a rule for in-flight work, such as stopping at the next safe point, rolling back, or flagging it for review.
4. Recommends preserving the original decision in the audit trail marked as withdrawn, not deleting it.
5. Recommends limiting who may revoke and defining how a revocation interacts with expiry and single-use state.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.29

A reviewer approves a database migration against a staging database. Later the identical statement is submitted against production with the old decision attached. Explain why a content-only binding fails here, which attributes should be bound, and what the cost of binding too many attributes is.

**Points:** 5

**Rubric (1 point each):**

1. Explains that identical text produces an identical fingerprint, so a gate that hashes only the statement accepts it.
2. Explains that the environment changes the consequences, since production data and users are affected.
3. Lists attributes to consider binding: resolved target, account, environment, repository revision, data classification, tool version.
4. Explains that over-binding (including volatile attributes) causes spurious re-approvals and reviewer fatigue.
5. States that choosing what to bind is a judgment about which changes should force reconsideration, not something the hash decides.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.30

An agent's approval request says the rollback for rotating a production credential is "restore the previous credential". Explain how a team should evaluate such a rollback claim and what an honest request says when full rollback is impossible.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the assumptions behind the claim: the previous credential exists, is retrievable, and is still valid after the action.
2. Recommends checking whether dependent effects occur before rollback, such as services failing in the gap.
3. Recommends rehearsing the restore in a safe environment rather than trusting a written description.
4. Notes that some actions, such as sending messages, disclosing data or payments, cannot be undone.
5. States that the request should say "no complete rollback" and describe partial recovery, rather than invent reassurance.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.31

A team writes tests for an approval predicate. All pass on the correct implementation, but three wrong implementations also pass: one hashes only a fixed list of six fields, one tests the approved flag for truthiness, and one checks a decision is unused and marks it used in two separate steps. For each wrong version, describe a test that would catch it, and explain what this shows about judging a test suite.

**Points:** 5

**Rubric (1 point each):**

1. Explains that hashing only a fixed list of fields lets a consequential extra field change without invalidating the approval.
2. Gives a test for it: add an extra field such as an environment to an approved proposal and expect rejection.
3. Explains that a truthiness check lets values such as the string "no" approve, and gives a test such as approved="no" expecting rejection.
4. Explains that the check-then-mark flaw is a race, and describes a test that interleaves two consumers of the same decision.
5. Explains that passing tests shows only that the tested statements hold; surviving wrong versions reveal gaps in the tests, so a suite must be judged by what it fails to catch.

**Source:** Write the approval predicate before anything is approved

## ES-ch13.32

Before asking an AI coding assistant to implement an approval gate, an engineer writes the predicate, the tests, and a one-sentence prediction of what a failure would look like. Explain why this order matters, and which decisions the engineer must make rather than delegate.

**Points:** 5

**Rubric (1 point each):**

1. Explains that acceptance criteria written by the accountable person before implementation give an independent standard to test the assistant's work against.
2. Explains that tests written by the same model that wrote the code can share its blind spots.
3. Explains that a failure prediction written before seeing output is falsifiable, whereas one written afterward tends to describe the output.
4. Lists decisions that depend on consequences and so stay with the engineer: which identities force a new decision, who the decision owner is, and the review capacity assumed.
5. Recommends building a baseline implementation by hand, so the engineer can audit the assistant's version and notice what differs.

**Source:** Write the approval predicate before anything is approved

## ES-ch13.33

An AI assistant returns code adding decision IDs, deadlines, revocation, and single-use consumption to an approval check. Describe how an engineer should review and test it, naming the places where consequential decisions are likely to be hidden, and how to find gaps in the engineer's own tests.

**Points:** 5

**Rubric (1 point each):**

1. Says to run the engineer's own tests on the returned code rather than relying on the assistant's report.
2. Names where the current time is read, since this affects testability and manipulation.
3. Names where a used decision is recorded and whether checking and recording are one atomic step.
4. Says to check that earlier strictness was not weakened, such as the exact Boolean requirement or the blank-approver rejection.
5. Recommends asking the assistant for a deliberately wrong version that still passes the tests and checking by hand whether it does, to find gaps in the tests.

**Source:** Write the approval predicate before anything is approved

## ES-ch13.34

Design an evaluation set for a gate that guards an agent's file-writing action. List at least six cases with their expected gate behavior and explain what each is meant to reveal.

**Points:** 5

**Rubric (1 point each):**

1. Includes an ordinary success case with the expected outcome of approval, because a gate that always refuses is useless.
2. Includes a case with reordered but identical content, expecting the same fingerprint, which removes representation noise.
3. Includes a case with a changed target, expecting the old decision to be rejected.
4. Includes a malformed proposal, such as a missing rollback, expecting a structural rejection, and a replayed decision, expecting the second use to be rejected.
5. Includes a structurally complete but substantively weak proposal, such as evidence reading only "looks good", expecting deferral, to test whether review reads meaning rather than field presence; also notes expected outcomes are written before running.

**Source:** Build an evaluation set that can embarrass the proposal

## ES-ch13.35

Design the screen on which a human reviews an agent's proposed action. State at least five principles and explain how each supports an informed decision.

**Points:** 5

**Rubric (1 point each):**

1. States that the action and target appear first, as the facts the reviewer needs soonest.
2. States that differences from any previously reviewed proposal are highlighted, including that a prior approval no longer applies.
3. States that evidence claims link to their underlying artifacts rather than showing a bare green label.
4. States that irreversible effects and missing rollback are prominent and cannot be collapsed away.
5. States that approve, refuse and defer are genuine, equally available choices, with no default selection or visual pressure toward approval.

**Source:** The approval interface is part of the control

## ES-ch13.36

A review dialog shows a large green "Continue" button next to a small gray refusal link, and a message from the requesting agent reading "Approve within 60 seconds or the job will fail!" Explain what is wrong with this design and what rules should govern it.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the unequal prominence of the buttons as a dark pattern that nudges the reviewer toward approval.
2. Identifies the urgency message, written by the party seeking approval, as an unvalidated claim serving the proposer.
3. Explains that pressure shortens deliberation and weakens the independence of the decision.
4. Recommends symmetrical presentation of approve, refuse and defer, with no pre-selected option.
5. Recommends that priority and urgency be set by a declared policy or a validated source, not by the requesting agent's label.

**Source:** The approval interface is part of the control

## ES-ch13.37

A proposal lists as evidence the URL of a test report, and the fingerprint covers the proposal text. After approval the report at that URL is replaced. Explain the gap, and describe what the decision should be bound to.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the fingerprint of the URL string does not change when the document behind the URL changes.
2. Concludes that the evidence the reviewer relied on can be substituted without invalidating the approval.
3. Recommends referencing evidence by an immutable identifier such as a content hash or version ID.
4. States that the decision should bind to the representation the reviewer actually saw, together with the immutable artifacts it references.
5. Notes related risks in presentation, such as hidden fields covered by the hash that the reviewer never saw, or truncated targets.

**Source:** The approval interface is part of the control

## ES-ch13.38

At execution time, a system recomputes a proposal's fingerprint and finds it differs from the one in the stored decision. Describe what should happen, and explain why asking an AI model whether the old approval "probably still applies" is the wrong response.

**Points:** 5

**Rubric (1 point each):**

1. States that the action must be blocked and the proposal returned to review.
2. Recommends showing the reviewer which fields changed so they can decide on the new content.
3. Explains that the old decision is evidence about history, not authority for the new proposal.
4. Explains that the model is the proposer's tool and has no authority to reinterpret the reviewer's decision.
5. Warns against shortcuts such as overwriting the stored fingerprint or letting the agent classify the change as minor.

**Source:** The approval interface is part of the control

## ES-ch13.39

A reviewer fully understands a proposal to export a customer dataset but has no authority over that data. Describe the outcomes a well-designed gate should allow, and explain why treating anything other than approval as failure damages the approval gate.

**Points:** 5

**Rubric (1 point each):**

1. States that the approval gate should allow approve, refuse, defer, and escalate as genuine outcomes.
2. Explains that escalation lets the reviewer pass the decision to someone with authority without impersonating an approver.
3. Explains that understanding a proposal does not confer authority over the data or action.
4. Argues that deferral with documented unresolved gaps is a successful gate outcome because it prevents an unsupported yes.
5. Explains that treating non-approval as failure pressures people to manufacture certainty, turning the approval gate into a ritual.

**Source:** The approval interface is part of the control

## ES-ch13.40

Agents submit 40 proposals per day that need careful human review. Each reviewer can carefully review 12 per day, and two reviewers are available. Calculate the daily backlog growth, the backlog after five days, and the number of reviewers needed, then recommend what the team should do besides speeding up clicking.

**Points:** 5

**Rubric (1 point each):**

1. Computes capacity as 24 per day (2 x 12) and backlog growth as 16 per day (40 - 24).
2. Computes the backlog after five days as 80 proposals.
3. Computes the reviewers needed as 4 (40 / 12 rounded up).
4. Recommends options such as pausing intake, narrowing the scope of agent actions, adding qualified reviewers, or deferring work.
5. Explains that showing less information to reviewers to raise throughput degrades judgment and is not capacity planning.

**Source:** Human attention is a finite gate resource

## ES-ch13.41

Five proposals are pending and one reviewer can carefully review two this period. A is a reversible local formatting change, B sends material to an external recipient, C changes a production target, D duplicates B's effect, and E depends on C being approved. Propose a queue policy and justify it.

**Points:** 5

**Rubric (1 point each):**

1. Prioritizes B and C because their effects are external or high-impact.
2. Detects D as a likely duplicate of B and holds it rather than spending review on it.
3. Keeps E blocked on the decision about C.
4. Lets A wait, expire, or proceed only under a separately authorized low-risk policy.
5. States that the policy must be set by accountable people before agents label their own work, and that proposer-supplied urgency labels must not set priority unvalidated.

**Source:** Human attention is a finite gate resource

## ES-ch13.42

A team finds that reviewers approve 99.6% of proposals in a median of 8 seconds, and a dashboard ranks reviewers by throughput. Diagnose what may be wrong, and propose changes to the process and measurements.

**Points:** 5

**Rubric (1 point each):**

1. Identifies habituation or rubber-stamping as a possible explanation for the very high approval rate and short review time.
2. Notes that a high approval rate alone does not show that proposals are good or that decisions were informed.
3. Recommends checking whether reviewers have real options, sufficient evidence, and support for saying no.
4. Recommends tracking refusal, deferral and later-reversed approvals as measures of review quality.
5. Explains that ranking reviewers by throughput rewards speed over care and should be replaced by measures of decision quality.

**Source:** Human attention is a finite gate resource

## ES-ch13.43

Reviewers keep receiving nearly identical low-consequence proposals, such as formatting changes to documentation in a sandbox repository. Discuss whether and how a standing policy could replace individual approvals for this class.

**Points:** 5

**Rubric (1 point each):**

1. Says that it is a governance decision owned by accountable people, not a shortcut the agent can take.
2. Requires the class to be defined precisely so that membership is unambiguous.
3. Requires testing the exclusions: cases just outside the class must still be routed to a reviewer.
4. Requires monitoring of outcomes and a way to revoke the policy.
5. States that everything outside the class remains gated and that the policy must not drift to adjacent classes without review.

**Source:** Human attention is a finite gate resource

## ES-ch13.44

A pipeline lets an action proceed if no reviewer responds within 30 minutes, if the agent reports confidence above 0.95, or if an automated evaluation score is at least 90%. Argue why none of these constitutes authorization and describe what legitimate automation of approvals looks like.

**Points:** 5

**Rubric (1 point each):**

1. Argues that a timeout is the absence of a decision, not consent.
2. Argues that a model's self-reported confidence is neither a calibrated measure nor a decision by someone with authority.
3. Argues that an evaluation score is evidence about tested cases and not permission.
4. Notes that destructive or irreversible actions make these shortcuts especially risky.
5. Describes legitimate automation as a narrowly defined standing policy set in advance by accountable people, with monitoring and revocation.

**Source:** Human attention is a finite gate resource

## ES-ch13.45

A team adopts agents that generate 10 times as many proposals per day (200 instead of 20), while reviewers can still carefully review 20 per day. Calculate what share can be carefully reviewed and explain the consequences and design responses.

**Points:** 5

**Rubric (1 point each):**

1. Computes that 20 of 200 is 10% that can be carefully reviewed.
2. Explains that generation scales with compute while careful verification does not scale with it.
3. Explains that proposals that proceed unreviewed are effectively unverified, so more output means less oversight per item.
4. Rejects the idea that skimming or using the same model to review restores independent judgment.
5. Recommends treating review capacity as a design constraint: measure or declare it, limit intake or scope to match, and report honestly when safe throughput is below production rate.

**Source:** Human attention is a finite gate resource

## ES-ch13.46

A marketing manager is asked to approve an agent's proposed database migration. The proposal is fluent and its claims sound reasonable, but it contains a subtle locking problem that would cause an outage. Explain why the review can fail even though the reviewer is diligent, and what the organization should do about it.

**Points:** 5

**Rubric (1 point each):**

1. Explains that judging whether a claim is credible relies on the reviewer's own domain knowledge, so errors outside it are not noticed.
2. Notes that fluent, confident text is not evidence of correctness, and an agent's own explanation of safety is another claim the reviewer cannot verify.
3. Recommends routing each proposal to a reviewer able to audit it, and sending proposals outside the reviewer's field to a specialist.
4. Recommends support such as deterministic checks, tests, or an expert's analysis as evidence the non-expert can rely on.
5. Recommends keeping reviewer workload low enough for judgment and tracking which reviewer each proposal went to and why.

**Source:** Human attention is a finite gate resource

## ES-ch13.47

Describe a feedback loop that uses what happens after approvals to improve a gate. Include what is compared, what is inspected, and how findings change the evaluation process.

**Points:** 5

**Rubric (1 point each):**

1. Compares the effects predicted in proposals with the outcomes actually observed.
2. Inspects approvals that were later reversed and asks what evidence or support the reviewer lacked.
3. Tracks refusals and deferrals as well as approvals, to see whether reviewers have real options.
4. Updates the next evaluation set after any unexpected outcome, harmless or not, before further approvals are requested.
5. Avoids scoring reviewers on throughput, which would train the approval gate toward ceremony.

**Source:** Human attention is a finite gate resource

## ES-ch13.48

An engineer's sign-off for a newly built approval gate reads in full: "Reviewed by the team. All tests passed. The approval gate is safe for production. Approved." Critique this sign-off and explain what a useful one would contain.

**Points:** 5

**Rubric (1 point each):**

1. Notes that it does not say which checks were run, against which criteria, or what the results were.
2. Notes that it does not say what was not tested or which failure modes were not reached, which is what makes a sign-off honest.
3. Notes that "the team" is not a person or role who can be asked and who answers if the approval gate was cleared wrongly.
4. Notes that "safe for production" overclaims, and that verbs should match the strength of the evidence (passed a stated test versus believed safe).
5. Describes a better form: what was tested and how, what was not tested, who cleared which gate, calibrated verbs, and an explicit statement of what is not being claimed.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.49

An engineer asks an AI assistant, without providing any test logs or notes, to write the sign-off statement for her validation work. It returns a fluent paragraph naming a reviewer and asserting that a full review took place. Explain why this paragraph is empty and how a truthful sign-off should be produced.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a language model has no knowledge of what was tested or skipped unless it is given the record.
2. Explains that the paragraph has the shape of a sign-off without substance, and shape is easy to produce.
3. Notes that a reviewer's name or confident wording in generated text is not evidence that any review took place.
4. States that the engineer should write the statement from her own record of tests run, results, and gaps, using the assistant at most for wording.
5. States that a signer must be able to support every claim and should withhold the signature if the record does not.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.50

A release process requires the test lead's signature, and in two years the lead has never declined to sign. Explain what this suggests, why the signer's right to withhold matters, and how the process could be changed so that a signature carries information.

**Points:** 5

**Rubric (1 point each):**

1. Explains that if signing is the only permitted outcome, the process is a rubber stamp that hides missing review behind a name.
2. Explains that a signature only carries information if refusing or deferring is a real possibility.
3. Recommends making withholding and deferral legitimate, recorded outcomes, not process failures.
4. Recommends giving the signer authority, time, and an escalation path, so declining does not cost them.
5. Recommends tracking how often sign-offs are withheld or conditioned and what happened afterward.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.51

The engineer who built an evaluation gate must write its sign-off, and finds she wants to write "no known issues." Explain the bias at work and describe practices that counter it.

**Points:** 5

**Rubric (1 point each):**

1. Identifies ownership bias: builders tend to overrate and under-examine their own work.
2. Recommends requiring a minimum number of entries (for example, three) in a "not tested" section.
3. Recommends noting for each untested item whether it was skipped as out of scope or because time ran out.
4. Recommends asking whether any untested condition is where harm would be most likely.
5. Recommends independent review of the sign-off, and notes that being unable to list gaps suggests insufficient scrutiny rather than a perfect system.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.52

A company adopts named sign-offs for high-risk automated actions. Discuss what this regime provides, what it costs, and why accountability should not rest only on the person who signed or clicked.

**Points:** 5

**Rubric (1 point each):**

1. States that it provides answerability: after a failure one can find who signed, read what they claimed and what they said they did not warrant.
2. States that it costs speed, because documenting limits takes effort, and removes deniability for the signer.
3. Notes that under schedule pressure, questions about what was not tested will be felt as friction, and the process may route around them.
4. Argues that governance should name organizational owners and escalation paths, not push every consequence onto the individual who clicked.
5. Notes that a signature strengthens identity evidence but does not prove comprehension or competence.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.53

Describe the sequence of steps that takes an agent's proposed action from construction to observed outcome in a sound approval workflow, and explain what happens when the proposal is changed after approval.

**Points:** 5

**Rubric (1 point each):**

1. Describes constructing the proposal from the plan and current state, then validating required fields and policy boundaries.
2. Describes running scoped evaluations and recording what they do not cover.
3. Describes freezing the exact proposal and computing its fingerprint before presenting evidence and consequences to an authorized reviewer.
4. Describes recording approve, refuse or defer against that fingerprint, and rechecking fingerprint, expiry, revocation and use limits at execution.
5. Explains that a changed proposal returns to evaluation and review, and that the actual outcome is observed and stored as a separate record afterward.

**Source:** Where the approval step sits in the build so far

## ES-ch13.54

An approved action runs, its fingerprint check passes, and a later check shows the file contains the wrong content. Explain why the fingerprint, the effect evidence, and the post-action check should be kept as separate linked records, and what each shows.

**Points:** 5

**Rubric (1 point each):**

1. States that approval permits a bounded attempt and does not guarantee the intended result.
2. States that the fingerprint shows the executed proposal was the approved one.
3. States that effect evidence, such as a trace, shows what the executor actually did.
4. States that the post-action check shows the resulting state of the world.
5. Explains that merging them hides which link failed, and that keeping them separate lets a team locate whether the proposal, the execution, or the outcome was wrong.

**Source:** Where the approval step sits in the build so far

## ES-ch13.55

A developer configures an agent to run any command matching the pattern "npm run *" without asking. One repository defines a script named "cleanup" that deletes a user's project directory. Explain what this reveals about approval by pattern, and propose a safer permission policy.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the pattern approves a form of command, not the effects of what the script does, which can be arbitrary.
2. Notes that the script's content is controlled by the repository, which may be untrusted or changed later.
3. Proposes narrower allow rules, such as specific named scripts, and explicit deny rules for destructive commands.
4. Proposes isolation controls such as a sandbox, least-privilege credentials, or running in a disposable environment.
5. States that any pre-approval is a standing authorization that should be scoped, reviewed periodically, and revocable.

**Source:** A gate is not a button

## ES-ch13.56

Describe a sound division of labor between an AI assistant and a human in an approval gate. Name tasks for each and explain why the human tasks cannot be delegated.

**Points:** 5

**Rubric (1 point each):**

1. Assigns the assistant drafting the structured proposal, flagging fields it could not fill, and showing changes from the last proposal.
2. Assigns the assistant running checkers, grouping traces, and flagging missing rollback or evidence.
3. Assigns the human choosing the cases that can embarrass the proposal, recording exclusions, and deciding which changes force a new decision.
4. Assigns the human approving, refusing, deferring or escalating within their authority.
5. Explains that authority and accountability attach to a person, that attention is finite, and that the assistant should stop at the authorization boundary and keep the action queued.

**Source:** The driver's seat

## ES-ch13.57

A student's prototype gate fingerprints proposals and verifies that the decision has an approved flag and a nonblank approver string. List at least five things that must be added or established before relying on it in production, and state what the student can and cannot honestly claim about it.

**Points:** 5

**Rubric (1 point each):**

1. Lists authenticated identity for approvers, since a name string can be typed by anyone.
2. Lists an authority registry saying who may approve which actions.
3. Lists expiry, revocation and atomic single-use consumption.
4. Lists audit logging with access control and retention, queue and capacity behavior, and an incident-response path.
5. States the honest claims: content binding under a simulated approver; and not that any person reviewed, was authorized, or that the proposal is safe.

**Source:** Ship It: a gate design that survives a skeptical reader

## ES-ch13.58

A manager says: "We added an approval step to our agent pipeline, so human oversight is guaranteed." Respond by describing at least five ways such a step can exist and still fail to provide oversight.

**Points:** 5

**Rubric (1 point each):**

1. Notes that the approval may be bound to something other than the executed content, so drift or substitution can occur.
2. Notes that the reviewer may lack the information, such as target, effects or rollback, needed to decide.
3. Notes that the reviewer may lack authority or the domain expertise to detect problems.
4. Notes that review capacity may be exceeded so that decisions become reflexive clicks or are skipped by timeouts.
5. Notes that interface pressure, a record with no genuine refusal option, or an unverified identity can turn the step into a ritual.

**Source:** Evaluation comes before authorization

## ES-ch13.59

Review the following gate code and identify at least four defects, with a fix for each.

```python
import json, hashlib

FIELDS = ("action", "target", "reason", "effects", "evidence", "rollback")

def fingerprint(p):
    subset = {k: p[k] for k in FIELDS}
    return hashlib.sha256(json.dumps(subset).encode()).hexdigest()

def approved(p, d, used):
    if d.get("approved") and d.get("approver") and d.get("fingerprint") == fingerprint(p):
        if d["id"] not in used:
            used.add(d["id"])
            return True
    return False
```

**Points:** 5

**Rubric (1 point each):**

1. Identifies that only six fields are hashed, so changes to any other field of the proposal do not invalidate the approval; fix by hashing the entire proposal (or an explicit full set).
2. Identifies that json.dumps is called without sorted keys or fixed separators, so equivalent proposals can hash differently; fix with canonical serialization.
3. Identifies that the approved and approver checks use truthiness, so "no" or a whitespace-only name passes; fix with approved is True and a stripped, nonblank (ideally authenticated) approver.
4. Identifies that the used set is checked and then updated in separate steps in process memory, so concurrent workers can both pass; fix with an atomic claim in a shared store.
5. Identifies missing expiry, revocation and clock handling, and fragile error handling such as KeyError on missing keys; fix by adding these checks and returning a denial on any malformed input.

**Source:** Canonical content and its fingerprint

## ES-ch13.60

A team must choose how to check three things in its gate: that a proposal is valid JSON with six required fields, that a rollback plan is plausible and specific, and that releasing a customer dataset is acceptable. Choose a type of grader (deterministic code, model-based, or human) for each and justify the choices.

**Points:** 5

**Rubric (1 point each):**

1. Chooses deterministic code for the JSON and field check, because it is mechanical, cheap and reliable.
2. Chooses a model-based grader, calibrated against human-labeled examples, for judging plausibility and specificity of free-text rollback plans, or a human, with the reasoning.
3. Notes that model-based grading has failure modes such as fluent but wrong text and shared biases, so its scores are evidence rather than decisions.
4. Chooses a human with authority for the dataset release, because it is a judgment about consequence and permission.
5. Recommends combining graders, keeping deterministic checks where possible and human review proportional to stakes.

**Source:** Evaluation comes before authorization

## ES-ch13.61

An approval workflow reports four things: the share of tasks the agent completed, whether actions complied with policy, how much effort reviewers spent, and whether an authorized person approved each consequential action. Explain why these are separate questions and why a high value on one does not imply the others.

**Points:** 5

**Rubric (1 point each):**

1. States that task success measures whether the work was done, and an agent can complete tasks by violating policy.
2. States that policy compliance is checked against stated rules and says nothing about whether a responsible person permitted an exception.
3. States that reviewer burden can fall because information was hidden or reviewers click reflexively, not because decisions were well informed.
4. States that authorization concerns a person with authority deciding, which no automated score can supply.
5. Recommends reporting the four separately, with errors and deferrals included, so that tradeoffs between them are visible.

**Source:** Evaluation comes before authorization

## ES-ch13.62

Build a threat model for an approval gate covering these threats: mutation of the proposal after it is shown, target aliasing, replay of a decision, stolen reviewer identity, reviewer overload, a misleading rollback claim, and revoked approval. For at least five of them, name a control, say whether it is code or a human practice, and state a residual risk.

**Points:** 5

**Rubric (1 point each):**

1. For mutation after display: recompute the fingerprint at the effect boundary (code); residual risk is that the displayed representation may differ from the hashed one.
2. For target aliasing: bind resolved identifiers and show canonical paths (code); residual risk is changes to what an identifier points to.
3. For replay: use decision IDs with atomic single-use consumption and expiry (code); residual risk is crash and retry ambiguity.
4. For stolen identity and reviewer overload: authenticated, signed decisions (code) and workload limits with escalation (people); residual risk is stolen credentials, habituation, and capacity.
5. For misleading rollback and revoked approval: test the rollback and state partial recovery honestly (people), and check revocation at execution (code); residual risk is unforeseen dependent effects and in-flight work.

**Source:** Ship It: a gate design that survives a skeptical reader
