# Chapter 13: Evaluation and approval gates

## ES-ch13.1

A reviewer is shown a proposal to write `report.md`, reads the evidence, and approves. The system files a yes with her name and a timestamp. Later the target becomes `elsewhere`. Explain how the approval can survive after the thing it approved has disappeared, even though a button, a name, and a timestamp were all recorded.

**Points:** 5

**Rubric (1 point each):**

1. States that the system filed a yes with the reviewer's name and a timestamp after she approved a proposal to write `report.md`.
2. States that the target later became `elsewhere`.
3. Explains that if the system retained only a generic yes, the old decision can be presented as permission for an action she never saw.
4. Notes that every step of the recipe (a button, a name, a timestamp) was followed and the authorization still drifted away from its object.
5. Names the remedy the chapter's fixture demonstrates: bind the decision to a fingerprint of the exact proposal so a changed target no longer matches.

**Source:** Opening (before "What you will be able to do")

## ES-ch13.2

State what the chapter's fixture demonstrates and what it does not demonstrate. Why does the chapter insist on listing the second group?

**Points:** 5

**Rubric (1 point each):**

1. States that the fixture turns six proposal fields into a stable serialized representation and computes a SHA-256 fingerprint recorded with a simulated decision.
2. States that the decision matches the original proposal and no longer matches once the target changes, which is content binding.
3. Says it does not demonstrate a real person's consent.
4. Says it does not demonstrate the approver's identity, authority, or comprehension.
5. Says it does not demonstrate that the proposal is safe, so a passing fixture must not be read as a sign-off.

**Source:** Opening (before "What you will be able to do")

## ES-ch13.3

The chapter says the question is "what, exactly, a yes is a yes to, and who was in a position to give it." Using the three jobs conduct, check, and drive, explain what each job means and which parts of an approval gate stay with a person even though Claude is fast.

**Points:** 5

**Rubric (1 point each):**

1. Defines conduct as deciding what the gate evaluates, covers, and refuses before anything is approved.
2. Defines check as asking whether an approval can still be true after the thing approved has changed, and what the record leaves out.
3. Defines drive as Claude assembling the proposal, running the evaluation, and highlighting the diff in seconds.
4. States that the yes, the no, and the attention behind them are a person's.
5. States that automated checks can prepare the decision and a fingerprint can prevent unnoticed content drift, but neither performs the human judgment inside the word "approve."

**Source:** Opening (before "What you will be able to do")

## ES-ch13.4

Before running any code, the chapter asks for four predictions. Give your prediction for each and justify it from the course implementation: (1) does changing dictionary key order change the fingerprint, (2) does changing only the target change it, (3) does an approval containing the right fingerprint but no approver name pass, (4) does a matching fingerprint prove that a particular human approved?

**Points:** 5

**Rubric (1 point each):**

1. Answers no for key order and explains that keys are sorted before serialization.
2. Answers yes for a changed target and explains that the target is part of the serialized proposal.
3. Answers no for a missing approver name and explains that the approver must be a nonblank string.
4. Answers no for the fourth prediction and explains that anyone can compute a digest and no identity appears in the code.
5. Notes that the chapter asks you to preserve your answers before running anything.

**Source:** Opening (before "What you will be able to do")

## ES-ch13.5

The objectives say you should write the gate before Claude implements it. Name the five things that the gate you write must contain or specify, and say what you do after Claude returns its implementation.

**Points:** 5

**Rubric (1 point each):**

1. Names the approval predicate.
2. Names scope.
3. Names expiry.
4. Names revocation.
5. Names an evaluation set that can embarrass the proposal, and says you then conduct Claude Code against the gate and run your own tests on what returns.

**Source:** What you will be able to do

## ES-ch13.6

Explain why a generic "Allow?" prompt is not a gate, then name the six fields the chapter requires and the question each one answers for the reviewer.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a generic prompt moves the cognitive burden onto the reviewer at the moment of interruption, often without the context to carry it.
2. Names action (what operation will occur) and target (the object or destination).
3. Names reason (ties the action to the task) and effects (anticipated changes, including external and irreversible ones).
4. Names evidence (checks that support proceeding) and rollback (how recovery would work, admitting when partial or impossible).
5. Notes that the six fields are a minimum teaching contract, not a universal governance schema.

**Source:** A gate is not a button

## ES-ch13.7

A draft approval request reads: action "update", target "the config", reason "Claude can edit files", effects "none", evidence "looks fine", rollback "undo". Using the chapter's guidance on individual fields, say what is wrong with each of the first four fields and how you would fix it.

**Points:** 5

**Rubric (1 point each):**

1. Says "update" may be too vague and gives a more reviewable form such as "overwrite one local Markdown file."
2. Says a display name for the target without a resolved path, account, environment, or recipient may conceal the consequential difference, and replaces it with a resolved identity.
3. Says reason should tie the action to the task rather than merely describing capability.
4. Says effects should name anticipated changes, including external and irreversible ones, so "none" needs checking against the world.
5. Says the reviewer, not Claude, must check whether the description is what will physically happen and whether the effects are complete.

**Source:** A gate is not a button

## ES-ch13.8

A proposal has six nonempty, fluent fields whose contents are meaningless. Explain why `fingerprint` accepts it, what the word "meaningful" in the error message does and does not guarantee, and what still has to happen.

**Points:** 5

**Rubric (1 point each):**

1. Explains that Python checks only that each retrieved value is truthy.
2. Identifies filling every field as structural validity.
3. Says the word "meaningful" in the error message expresses intended use more strongly than the implementation can enforce.
4. Concludes that passing the precondition does not show the descriptions are adequate.
5. Says human and domain evaluation still matter.

**Source:** A gate is not a button

## ES-ch13.9

Distinguish evaluation from authorization, say how they relate, and explain why the chapter says the merge of the two on an approval screen is where gates go soft.

**Points:** 5

**Rubric (1 point each):**

1. Defines evaluation as asking what happened, what could happen, and how well the proposal meets a stated criterion.
2. Defines authorization as asking whether a responsible person or policy permits the action.
3. States that the first produces evidence and the second spends it.
4. Explains that merging the two questions on one screen is where gates go soft.
5. Adds the design-order point: decide what would count as evidence against the proposal before looking at the evidence for it.

**Source:** Evaluation comes before authorization

## ES-ch13.10

A team writes 12 test cases after watching their implementation run, then adjusts the expected answers until all 12 pass. They report "12 of 12." What does the chapter say this evidence records, and what four things should change in how they build and report the set?

**Points:** 5

**Rubric (1 point each):**

1. Says the set records accommodation, not evaluation.
2. Says the cases should be decided before looking at the evidence for the proposal, including what would count as evidence against it.
3. Says the set should be able to embarrass the proposal.
4. Says the report should show which cases were run and why they represent intended use, with exclusions recorded beside the result.
5. Says at least one case should require refusal, otherwise a system that always proceeds can appear perfect.

**Source:** Evaluation comes before authorization

## ES-ch13.11

Name three evaluation instruments from the chapter, say what each can and cannot do, and state the single thing none of them returns.

**Points:** 5

**Rubric (1 point each):**

1. States that a test suite can evaluate selected behavior but cannot decide whether a destructive change is worth making.
2. States that a policy checker can flag an unapproved directory but cannot say whether an exception serves the affected people.
3. States that a model grader's score is evidence with scope and failure modes, not a decision.
4. States that Claude can run every one of these instruments and should.
5. States that none of them returns a decision.

**Source:** Evaluation comes before authorization

## ES-ch13.12

Chapter 11's false final claim had 42 in the trace and 99 in the sentence. Explain what this teaches about building an evaluation set and about what a tool trace can and cannot show.

**Points:** 5

**Rubric (1 point each):**

1. States that a tool trace showing a command ran is not an observation that the intended state exists.
2. Identifies the example as 42 in the trace and 99 in the sentence.
3. States that success narration is not an outcome check.
4. Says trials and transcripts should be kept but distinguished from actual outcomes.
5. Says evaluation sets should be built around tasks, expected outcomes, refusal cases, and boundary failures.

**Source:** Evaluation comes before authorization

## ES-ch13.13

A report says "passed 20 cases." Explain why the chapter calls this uninterpretable, what a reviewer needs to see before it means anything, and what kinds of cases an evaluation built from ordinary successful writes would leave out.

**Points:** 5

**Rubric (1 point each):**

1. Says the result is uninterpretable until a reviewer can see which cases were run and why they represent the intended use.
2. Names at least three of the excluded categories: symlinks, permission errors, concurrent changes, private data, or malicious paths.
3. Says exclusions should be recorded beside the result.
4. Says at least one case should require refusal, or a system that always proceeds can appear perfect.
5. Says one case should be structurally complete but substantively weak, to test whether review reads meaning or treats field presence as safety.

**Source:** Evaluation comes before authorization

## ES-ch13.14

A dashboard shows task success rising and time-to-approval falling after a gate redesign. Using the chapter's discussion of metrics, explain why this is not yet evidence that the gate improved and what else should be measured or reported.

**Points:** 5

**Rubric (1 point each):**

1. Says task success may rise while the invalid action rate also rises.
2. Says reviewer burden may fall because the gate hides detail, while informed decisions worsen.
3. Says time-to-approval may improve because reviewers click reflexively.
4. Says a gate needs a portfolio of evidence, with errors and deferrals included, not one celebratory rate.
5. Says to evaluate task success, invalid action rate, and reviewer burden separately.

**Source:** Evaluation comes before authorization

## ES-ch13.15

For each of these inputs to `fingerprint`, say whether it fails or passes the precondition and what happens next: (a) a list instead of a dictionary, (b) all six fields present but `rollback` is an empty string, (c) all six fields plus an extra `"environment": "production"`, (d) `evidence` is an empty list, (e) the `reason` key is missing.

**Points:** 5

**Rubric (1 point each):**

1. Says (a) fails because a non-dictionary fails.
2. Says (b) fails because an empty string is falsey.
3. Says (c) passes, and that the extra field becomes part of the serialized proposal and affects the fingerprint.
4. Says (d) fails because an empty list is falsey.
5. Says (e) fails because a missing required field fails.

**Source:** Canonical content and its fingerprint

## ES-ch13.16

Explain the roles of `sort_keys=True` and the compact separators in the serialization, and say what problem each solves.

**Points:** 5

**Rubric (1 point each):**

1. Explains that JSON objects do not conceptually depend on insertion order but Python dictionaries preserve one.
2. Explains that without sorting, equivalent proposals built in different orders could produce different byte sequences.
3. States that `sort_keys=True` canonicalizes key order for this bounded representation.
4. States that compact separators remove default spaces so formatting choices do not alter the bytes.
5. Notes that the entire dictionary is serialized (including extra fields) before being encoded and hashed with SHA-256 to a hexadecimal digest.

**Source:** Canonical content and its fingerprint

## ES-ch13.17

The reversed-insertion-order test passes. State exactly what that shows about the course function, and say what two programs in different languages would still have to agree on before their digests could match.

**Points:** 5

**Rubric (1 point each):**

1. States that the test confirms reversing dictionary item order does not change the fingerprint for the course function.
2. States that this is an observed property of the course function for its JSON-compatible fixture, not a claim of universal canonical JSON.
3. Names number handling as an additional specification needed.
4. Names Unicode normalization as an additional specification needed.
5. Names unsupported objects, duplicate keys arriving in raw JSON, or cross-language serialization as further needs, and notes the digest is computed over bytes.

**Source:** Canonical content and its fingerprint

## ES-ch13.18

Walk through the four conditions that `approved(proposal, decision)` checks, give one input that would fail each, and say what a `True` result does and does not mean.

**Points:** 5

**Rubric (1 point each):**

1. States that the decision must be a dictionary.
2. States that `approved` must be the exact Boolean `True`, so the string `"yes"` fails.
3. States that the approver must be a nonblank string and that the recorded fingerprint must equal a newly computed fingerprint of the proposal now under consideration.
4. States that `True` means the decision record has the required shape and content binding.
5. States that it does not mean a real authorized human gave informed consent, because the implementation has no login, signature, role registry, delegation rule, expiry time, revocation list, decision ID, or evidence a person saw the proposal.

**Source:** The approval predicate

## ES-ch13.19

The chapter distinguishes three things an approval can be bound to. Name them, say what each covers, and say which one the chapter's code actually does.

**Points:** 5

**Rubric (1 point each):**

1. Names content and says the fingerprint ties a decision to the exact serialized proposal.
2. Says the code binds content.
3. Names scope and time and says it covers how long a decision lives, how often it may be used, and in which environment.
4. Says scope and time is code not yet written, designed in the next section.
5. Names person (who decided, with what authority, having read what) and says no code can do it alone, so a gate binding only content is "a good seal on an envelope nobody opened."

**Source:** The approval predicate

## ES-ch13.20

Describe the chapter's worked example from the proposal through the changed target. What does each of the three results (fingerprint, simulated decision, rejection) show, and what must the reader not conclude?

**Points:** 5

**Rubric (1 point each):**

1. Describes the proposal with six nonempty values (write, report.md, deliver draft, one local file, source checks passed, restore previous file) and a 64-character SHA-256 fingerprint.
2. Describes the simulated decision with approved True, a simulated approver, and the proposal's fingerprint, and says `approved` returning true is a fixture result, not a human sign-off.
3. Says that changing the target to `elsewhere` serializes to different bytes and yields a different fingerprint.
4. Says `approved(changed, decision)` returns false because the old digest no longer equals the current one.
5. Says the system does not ask whether `elsewhere` is similar or safer, and the reviewer must see the new decision object and decide again.

**Source:** Worked example: approval that cannot follow a changed target

## ES-ch13.21

Reordering a dictionary's keys does not change the fingerprint, but two spellings of a path to the same file do. Explain what this shows about what counts as "the same proposal," and what a high-stakes gate may bind instead of friendly text.

**Points:** 5

**Rubric (1 point each):**

1. Says reordering is a representation change, not a proposal change, and the fingerprint stays the same.
2. Says a gate should avoid demanding new approval for irrelevant formatting while reliably detecting consequential change.
3. Says two path spellings that resolve to the same file hash differently as strings.
4. Says a target string can stay identical while the filesystem object it names changes.
5. Says a high-stakes gate may bind resolved identifiers, immutable versions, or object hashes rather than friendly text alone.

**Source:** Worked example: approval that cannot follow a changed target

## ES-ch13.22

Using the chapter's evidence table, give for each of these observations one conclusion it supports and one it does not: (a) target change with a digest mismatch, (b) a decision that matches the original digest, (c) the predicate returns true.

**Points:** 5

**Rubric (1 point each):**

1. For (a), says it supports that the serialized proposal changed.
2. For (a), says it does not support that the changed action is necessarily harmful.
3. For (b), says it supports that the record binds to the original content.
4. For (b), says it does not support that a named person was authenticated.
5. For (c), says it supports that the fixture contract passes and does not support that informed, authorized consent occurred.

**Source:** Worked example: approval that cannot follow a changed target

## ES-ch13.23

The chapter says the evidence table contains no row that would support "a person reviewed this." Explain why that absence is called the sign-off standard and what a recorded fingerprint is and is not evidence of. Also say what the six passing lesson tests do and do not show.

**Points:** 5

**Rubric (1 point each):**

1. Says no row in the table supports the claim that a person reviewed the proposal, and that this absence is the sign-off standard.
2. Says a recorded fingerprint is evidence that a record was written against these bytes.
3. Says it is not evidence that anyone read them.
4. Says that all six tests passing shows the reference meets six statements.
5. Says it does not show that six statements are enough, and that finding wrong versions that pass all six is the work of the gate.

**Source:** Worked example: approval that cannot follow a changed target

## ES-ch13.24

Explain what a fingerprint answers and what it does not, and list the kinds of scope a reviewer might approve beyond content. Why does the chapter say a gate that leaves scope to defaults has still made decisions?

**Points:** 5

**Rubric (1 point each):**

1. Says a fingerprint answers "is this still the proposal?"
2. Says it does not answer "may this be done now, here, once?"
3. Names at least three scope types: one execution, one environment, one time window, one data set, or one maximum effect.
4. Says that if the proposal says "write report.md" but the operation can repeat, the fingerprint alone does not limit replay.
5. Says a gate that leaves these to defaults has made those decisions anyway.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.25

Two workers present the same valid decision at the same moment and both execute the action. Explain how the chapter's design prevents this and why a check followed by a separate mark does not.

**Points:** 5

**Rubric (1 point each):**

1. Says the fingerprint alone does not limit replay.
2. Says to add a unique decision ID and consumption state for single-use actions.
3. Says the ID must be checked and consumed atomically at the effect boundary.
4. Explains that checking unused and marking used in two separate steps lets two workers both pass between them.
5. Says the authorization service must own that rule where the action occurs.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.26

A decision carries the deadline "2026-11-01 17:00" with no time zone. Using the chapter's discussion of expiry and revocation, explain what is wrong with that deadline and what an expiry and a revocation record each need.

**Points:** 5

**Rubric (1 point each):**

1. Says a deadline in local time without a zone is ambiguous and expiry needs an explicit time basis and comparison policy.
2. Says expiry is not just a timer, because new evidence can invalidate approval early.
3. Says revocation withdraws a still-unexpired decision.
4. Says a revocation record should say who revoked and under what authority.
5. Says it should also say which proposal is affected and how already-started work is handled.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.27

A reviewer approves a database query against a test database. The identical query text is later presented against production. Explain why the old approval must not carry over, which identities the chapter lists as candidates to bind, and how to decide which ones to include.

**Points:** 5

**Rubric (1 point each):**

1. Says approval for a test database must not authorize production merely because the query text matches.
2. Says to bind the environment identity that matters.
3. Names at least three candidates: resolved target, account, repository revision, data classification, or tool version.
4. Says to add the identities whose change should force reconsideration and no others.
5. Says which ones those are is a judgment about consequence, not a property of the hash.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.28

A proposal's rollback field says "restore previous file." List what that claim assumes, give examples of effects that may make rollback impossible, and say what the gate should say when rollback is incomplete.

**Points:** 5

**Rubric (1 point each):**

1. Says the claim assumes a previous copy exists.
2. Says it assumes the writer can access that copy and no dependent effects have occurred.
3. Says it assumes restoration is semantically sufficient.
4. Gives an irreversible example: sending a message, disclosing data, or triggering a payment.
5. Says the gate should say "no complete rollback" rather than inventing reassurance, since an approved change can still be a bad change.

**Source:** Scope, expiry, revocation, and replay

## ES-ch13.29

Describe the Design part of the gate you write before asking Claude for any code. What must it contain, and which of its decisions can Claude not make for you?

**Points:** 5

**Rubric (1 point each):**

1. Says it covers one consequential action from the capstone or the `report.md` write, with its six fields.
2. Says friendly targets are replaced by resolved identities.
3. Says it names the identities beyond the six whose change should force a new decision.
4. Says the decision owner is a role that can be asked, not "the team," and the review budget is labeled an assumption unless measured.
5. Says these are the writer's choices and no model produced them.

**Source:** The gate: write the approval predicate before anything is approved

## ES-ch13.30

State the contract for the approval predicate: the conditions under which a decision authorizes one bounded attempt.

**Points:** 5

**Rubric (1 point each):**

1. States that `approved` is exactly True and the approver is a nonblank string.
2. States that the recorded fingerprint equals a fresh fingerprint of the proposal about to execute.
3. States that the fresh fingerprint is computed at the effect boundary, not at review time.
4. States that the deadline has not passed and the decision has not been revoked.
5. States that the decision has not already been used.

**Source:** The gate: write the approval predicate before anything is approved

## ES-ch13.31

List what the contract says authorizes nothing, how refusal and deferral are treated, and why the chapter would pass the current time into the check instead of reading it inside.

**Points:** 5

**Rubric (1 point each):**

1. Says absence authorizes nothing.
2. Says silence and a timeout authorize nothing.
3. Says a model's confidence and a favorable automated score authorize nothing.
4. Says refusal and deferral are recorded outcomes, not errors.
5. Says passing the current time in lets tests say "one second after the deadline" without waiting.

**Source:** The gate: write the approval predicate before anything is approved

## ES-ch13.32

The chapter says two plausible wrong predicates pass all six lesson tests and a third has no lesson test at all. Describe all three and explain what that implies about your tests.

**Points:** 5

**Rubric (1 point each):**

1. Describes the predicate that fingerprints only the six named fields, so adding `"environment": "production"` changes nothing.
2. Describes the predicate that tests `approved` for truthiness, so the string `"no"` approves.
3. Describes the predicate that checks a decision is unused and marks it used in two separate steps, so two workers can both pass between them.
4. Says the third has no lesson test because the lesson has no consumption.
5. Concludes that if your tests cannot tell these from the right program, the gate is not finished.

**Source:** The gate: write the approval predicate before anything is approved

## ES-ch13.33

Explain the "failure sentence" the chapter asks you to write, when it must be written and why, and what the finished gate may and may not claim.

**Points:** 5

**Rubric (1 point each):**

1. Says it is one sentence, dated, saying what you would see if the gate approved something it should not.
2. Says it must be written before you read any output.
3. Says written afterwards it describes the output instead of testing you.
4. Says the gate may claim content binding, expiry, and single use under a fixture clock and a simulated approver.
5. Says it may not claim that a person reviewed, understood, or was authorized.

**Source:** The gate: write the approval predicate before anything is approved

## ES-ch13.34

The chapter says Claude can attack your gate usefully but cannot write it for you. Explain both halves of that claim.

**Points:** 5

**Rubric (1 point each):**

1. Says you can ask Claude for a decision record that would still pass your predicate and should not.
2. Says Claude cannot write the gate for you without defeating its purpose.
3. Says the owner is a judgment about consequence.
4. Says the review budget is a judgment about consequence.
5. Says the identities that force a new decision are also judgments, and they go on the record in your words.

**Source:** The gate: write the approval predicate before anything is approved

## ES-ch13.35

For each of these cases in the chapter's compact evaluation set, state the construction's expected gate behavior: reordered keys, changed target, missing rollback, vague evidence, and replayed decision.

**Points:** 5

**Rubric (1 point each):**

1. Says reordered keys expect the same fingerprint.
2. Says a changed target expects the old decision to be rejected.
3. Says a missing rollback expects the proposal shape to be rejected.
4. Says vague evidence expects a structural pass and a human defer.
5. Says a replayed decision expects the second use to be rejected in the extension.

**Source:** Build an evaluation set that can embarrass the proposal

## ES-ch13.36

A proposal's evidence field says only "looks good." The function fingerprints it. Is that a bug? Explain, and say whose work it is to catch it.

**Points:** 5

**Rubric (1 point each):**

1. Says the function fingerprints it because the string is nonempty.
2. Says it is not a failing test if the function's contract is structural content binding.
3. Says it becomes a workflow failure only if documentation claims the function evaluated evidence quality.
4. Defines plausibility auditing as judging whether a claim is credible and consistent with what you know, independent of how confidently it was stated.
5. Says that is the reviewer's work and no field name does it.

**Source:** Build an evaluation set that can embarrass the proposal

## ES-ch13.37

A team uses a model to grade rollback fields and reports 100 percent agreement with a second model grader using the same prompt. Using the chapter, explain why this is weak evidence and how the grading should be set up and reported.

**Points:** 5

**Rubric (1 point each):**

1. Says model graders can assist with qualitative fields but need calibration and failure analysis.
2. Says a model may reward fluent rollback prose that omits an irreversible effect.
3. Says two graders that share a prompt assumption or a source error can agree and still be wrong together.
4. Says that agreement is not a second opinion.
5. Says to pair qualitative grading with deterministic checks and human review proportional to the stakes, and to keep inputs, expected behavior, actual output, checker, and rationale for discrepancies.

**Source:** Build an evaluation set that can embarrass the proposal

## ES-ch13.38

A reviewer sees a friendly summary and a truncated target while the fingerprint covers hidden fields and effects are collapsed behind a disclosure panel. Explain the problem and describe what the interface should do instead.

**Points:** 5

**Rubric (1 point each):**

1. Says the decision binds to bytes the reviewer did not meaningfully inspect.
2. Says the record may be mechanically exact and socially uninformed.
3. Says to present the action and target first and highlight differences from any previously reviewed proposal.
4. Says to link evidence claims to artifacts and make irreversible effects and absent rollback unavoidable.
5. Says to provide approve, refuse, and defer as genuine choices and to avoid dark patterns such as a default-selected approval, a green continue button beside a muted refusal link, or agent-generated urgency language.

**Source:** The approval interface is part of the control

## ES-ch13.39

Evidence referenced by an approved proposal lives at a URL whose content can change after approval. Explain the gap this creates, what the decision should bind to, and what should happen at execution if the fingerprint no longer matches.

**Points:** 5

**Rubric (1 point each):**

1. Says the decision should bind to the representation the person actually saw, together with any referenced immutable artifacts.
2. Says that if evidence can change at the same URL after approval, binding only the proposal text leaves another substitution path.
3. Says the interface should say why this person is the decision owner, because someone can understand a proposal and still lack authority over the target, data, or recipient.
4. Says the person should be able to escalate without impersonating an approver.
5. Says at execution the fingerprint is recomputed, and on a mismatch the changed fields are shown and the proposal returns to review without asking the model why the old approval probably still applies.

**Source:** The approval interface is part of the control

## ES-ch13.40

Explain the volume trap and why a perfectly bound proposal can still receive superficial review. What does the chapter say about the status of this claim?

**Points:** 5

**Rubric (1 point each):**

1. Says the case for generating ten times as much in the same time is real.
2. Says the ability to verify ten times as much does not come with it, so the extra output is reviewed less or not at all.
3. Says the chapter presents this as the book's argument, not a measurement of any team.
4. Says Claude sits on the generating side of the gap.
5. Says speeding up the button does not restore judgment and turns the gate into a queue or click ritual.

**Source:** Human attention is a finite gate resource

## ES-ch13.41

Five proposals arrive while one reviewer can carefully inspect two in the stated period. How large is the shortfall, what status does the capacity number have, and how do a naive and a governed system differ? If six more arrived in the same period with the same capacity, how many would exceed capacity?

**Points:** 5

**Rubric (1 point each):**

1. Computes the shortfall as three (five minus two).
2. Says the capacity of two is a labeled assumption, not a measured result.
3. Says a naive system shows all five as urgent and lets dependent agents wait indefinitely.
4. Says a governed system classifies consequence, preserves arrival and dependency information, and applies a declared queue policy.
5. Computes that eleven proposals against a capacity of two leaves nine beyond capacity, and says automatic checks cannot manufacture the missing human attention.

**Source:** Human attention is a finite gate resource

## ES-ch13.42

Proposal A is a reversible local formatting change, B sends material to an external recipient, C changes a production target, D duplicates B's effect, and E depends on C. Apply the chapter's reasoning to the queue and say what the example is and is not meant to establish.

**Points:** 5

**Rubric (1 point each):**

1. Says B and C may receive priority because their effects are external or high-impact.
2. Says D should be detected as a potential duplicate and held.
3. Says E remains blocked on C.
4. Says A may wait, expire, or proceed under a separately authorized low-risk policy if one genuinely exists.
5. Says this ordering is not universally correct; someone must choose and document the policy before the proposing model labels its own work urgent, and proposer urgency labels should never set priority unvalidated.

**Source:** Human attention is a finite gate resource

## ES-ch13.43

The review queue exceeds capacity. Name the responses the chapter endorses, the responses it rejects, and what happens to pending decisions whose premises go stale.

**Points:** 5

**Rubric (1 point each):**

1. Names at least three endorsed responses: pause intake, narrow scope, add qualified reviewers, or defer work.
2. Says cutting the information shown until reviewers can click faster is not capacity planning.
3. Says pending decisions should be invalidated when their evidence or environment goes stale.
4. Says timeout, absence, and queue delay are not approval.
5. Says more prompts do not mean more oversight, because past the available attention they produce habituation.

**Source:** Human attention is a finite gate resource

## ES-ch13.44

Describe the feedback loop that keeps review quality from decaying, including what to track, what not to score, and what an unexpected outcome should change.

**Points:** 5

**Rubric (1 point each):**

1. Says to compare predicted effects with observed outcomes and inspect approvals later reversed.
2. Says to track refusal and deferral, not just approvals.
3. Says if every decision is yes, ask whether reviewers have real options, adequate evidence, and support for saying no.
4. Says not to score reviewers on throughput, which trains the gate to become ceremonial.
5. Says an unexpected outcome, harmless or not, should change the next evaluation set before another approval is requested.

**Source:** Human attention is a finite gate resource

## ES-ch13.45

Reviewers keep receiving nearly identical low-consequence proposals. The chapter says capacity moves the automation boundary. Explain what option arises, what conditions it requires, and why it is not an agent shortcut.

**Points:** 5

**Rubric (1 point each):**

1. Says a team can ask whether a narrow standing policy should authorize that class of proposals.
2. Says it needs monitoring and revocation.
3. Says it is a governance decision, not an agent shortcut.
4. Says the class must be defined precisely and its exclusions tested.
5. Says everything outside the class stays gated.

**Source:** Human attention is a finite gate resource

## ES-ch13.46

Describe the sign-off experiment the chapter takes from the companion book, the predicted result, and why the prediction is that the paragraph is "empty" even though it looks complete.

**Points:** 5

**Rubric (1 point each):**

1. Says you ask an agent for the sign-off statement for the thing you just validated.
2. Says the predicted result is a fluent, structurally complete paragraph that names a person and asserts a review happened.
3. Says it is empty because, unless you supplied the record, the system has nothing to say about what was done or skipped.
4. Says you run the experiment once and save what you actually get.
5. Says you read it against the four-part standard, noting the shape of a sign-off is easy to produce and its substance is not.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.47

Name and explain the four parts of the companion's attestation standard.

**Points:** 5

**Rubric (1 point each):**

1. Names what was tested: specific checks against specific criteria, with the results.
2. Names what was not tested: the conditions not probed and the failure modes known and not reached.
3. Names who cleared which gate: a named person or role per decision who can be asked and answers if the gate was cleared wrongly, not "the team."
4. Names calibrated verbs: "passed" means passed a stated test.
5. Says a weaker verb such as "believe safe" should say that it is weaker.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.48

Why does the chapter call "what was not tested" the part that makes a sign-off honest, and why is it the part an AI-written sign-off omits?

**Points:** 5

**Rubric (1 point each):**

1. Says it is the part an AI-written sign-off omits.
2. Says it is the part that makes the document honest.
3. Says a list of only what passed reads as a clean bill of health.
4. Says the affected person cannot act on that list when the untested region is where harm lives.
5. Says if you cannot fill the "Not checked" entry with real entries, you have not looked hard enough, not found nothing.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.49

A reviewer writes: "The local tests pass, but remote publication permissions and data licensing are unverified; defer." Evaluate this as a gate outcome, and say what the fingerprint can and cannot contribute to such a record.

**Points:** 5

**Rubric (1 point each):**

1. Says this is a successful gate outcome.
2. Says treating anything but approval as failure pressures people to manufacture certainty.
3. Says a useful decision record lets the reviewer decline or defer and preserves unresolved gaps.
4. Says the fingerprint binds the record to content.
5. Says it cannot show that the reviewer opened the test report, understood the target, or had enough time, and a signature can strengthen identity evidence without proving comprehension.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.50

Explain what an attestation regime optimizes for, what it sacrifices, and why the signer's authority to withhold is essential.

**Points:** 5

**Rubric (1 point each):**

1. Says it optimizes for legible answerability: after a failure you can find the signer, read the claim, and see what they did not warrant.
2. Says it sacrifices speed and deniability.
3. Says under schedule pressure "what did we not test?" is experienced as friction arriving late, and that friction is the point.
4. Says if the only outcome the process permits is "signed," it is a rubber stamp with a person's name on it.
5. Says governance must name organizational owners and escalation paths, not place every consequence on the person who clicked.

**Source:** Attestation: what the signer states, and the right to withhold

## ES-ch13.51

List the eight steps of the sequence in order and say what Chapters 10, 11, and 12 each contribute.

**Points:** 5

**Rubric (1 point each):**

1. Gives steps 1 and 2 as constructing a proposal from the current plan and state, and validating required fields and policy boundaries.
2. Gives steps 3 and 4 as running scoped evaluations while recording exclusions, and freezing the exact proposal and computing its fingerprint.
3. Gives steps 5 and 6 as presenting evidence and effects to an authorized reviewer, and recording approve, refuse, or defer against the fingerprint.
4. Gives steps 7 and 8 as rechecking fingerprint, expiry, revocation, and use constraints at execution, and observing the actual outcome and preserving it separately.
5. Says Chapter 10 creates the proposed step, Chapter 11 supplies execution evidence, and Chapter 12 stores versioned state and exposes conflicts.

**Source:** Where the gate sits in the build so far

## ES-ch13.52

After the reviewer approves at step 6, the proposal's target changes. What does the chapter say happens to the workflow and to the old approval, and which records should be kept separately?

**Points:** 5

**Rubric (1 point each):**

1. Says the workflow returns to step three or earlier.
2. Says a valid old approval is evidence about history, not authority for the new object.
3. Says that at execution the fingerprint is rechecked along with expiry, revocation, and use constraints.
4. Says approval permits a bounded attempt and does not guarantee the intended result.
5. Says the proposal fingerprint, the effect evidence, and the post-action check should be separate linked records.

**Source:** Where the gate sits in the build so far

## ES-ch13.53

Describe the Build It procedure and explain why you write `fingerprint` and `approved` yourself before opening the reference solution.

**Points:** 5

**Rubric (1 point each):**

1. Says to write the functions yourself before consulting the reference solution.
2. Says to read the six tests first and write down which input should fail and why.
3. Says to explain each intermediate quantity (the canonical bytes, the digest, the comparison) and what would count as an impossible value.
4. Says to trace one success and one failure by hand, changing one input at a time so a difference has an identifiable cause.
5. Says your version is the baseline, and you cannot audit a predicate you have never written, because a gate that approves the wrong thing does not crash.

**Source:** Build It: the baseline that lets you audit

## ES-ch13.54

Describe the three things you do with the result when Claude Code extends your predicate with a decision ID, deadline, revocation, and single-use consumption.

**Points:** 5

**Rubric (1 point each):**

1. Says you give Claude the contract and the test list but not your implementation, and you run your own tests on what it returns.
2. Says to note which of your tests failed, since a failing test is often a gap in your gate that Claude could not see.
3. Says to read the diff for where the current time is read, where a used decision is recorded, and whether checking and recording happen as one step.
4. Says to name one difference in behavior from your baseline.
5. Says to ask Claude for a deliberately wrong version that still passes your tests and check by hand whether it does, which would mean your tests were too weak.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch13.55

List what the Ship It artifact must contain, how the fingerprint should be handled, and what it must not claim.

**Points:** 5

**Rubric (1 point each):**

1. Lists before-and-after gate wording, an evaluated proposal, rejection tests, and a decision record.
2. Says the decision record carries the fingerprint, the simulated decision labeled as a simulation, and the unresolved gaps.
3. Says never to fabricate a classmate's or stakeholder's approval.
4. Says to calculate the fingerprint only after the proposal is ready for review and to freeze or copy the reviewed representation.
5. Says to enumerate production gaps (naming at least three, such as authentication, authorization registry, single-use consumption, expiry, revocation, audit access, privacy retention, queue behavior, incident response) and not to claim the teaching Boolean is an authorization service.

**Source:** Ship It: a gate design that survives a skeptical reader

## ES-ch13.56

Distinguish the decision record from the sign-off, say who produces each, and explain what to do when the evidence does not support signing.

**Points:** 5

**Rubric (1 point each):**

1. Says the decision record is what a reviewer produces: approve, refuse, or defer, with scope, gaps, and authority.
2. Says the sign-off is what you produce about the gate you built.
3. Says when the reviewer is a simulation, the decision record is a labeled fixture and not a decision.
4. Says you may withhold the sign-off, and withholding is an honest result if the evidence does not support signing.
5. Says if you cannot fill "Not checked" with real entries, you have not looked hard enough, not found nothing.

**Source:** Ship It: a gate design that survives a skeptical reader

## ES-ch13.57

Use the driver's seat table to explain, for implementing the predicate and for approving, refusing, deferring, or escalating, what Claude does, what you do, and why it stays with you. What must you record in the artifact?

**Points:** 5

**Rubric (1 point each):**

1. Says for the predicate that Claude implements from your gate, fast.
2. Says you write the gate and tests first, build your own baseline, and run your tests on its version, because you cannot audit a predicate you have not built.
3. Says for the decision that Claude keeps the action queued and stops at the boundary.
4. Says you decide within your authority, because authority and accountability attach to a person and the right to say no is part of the job.
5. Says to record one task you delegated and one judgment you retained, with a transcript line or edit as proof.

**Source:** Ship It: a gate design that survives a skeptical reader

## ES-ch13.58

Fill in the sign-off template for a gate whose reviewer was simulated: explain what goes on the "Not checked," "Cleared by," "Verbs," and "Not claiming" lines.

**Points:** 5

**Rubric (1 point each):**

1. Says "Not checked" can include authentication, a real reviewer, concurrent use, clock skew, and evidence that changes after approval (naming at least three).
2. Says "Cleared by" names a role or person per gate, or "SIMULATED, not a person."
3. Says "Verbs" words each claim at the strength of its evidence, such as recorded, computed, or tested, not established.
4. Says "Not claiming" states that no person reviewed or was authorized and that the proposal is not claimed safe.
5. Says the last line records signed or withheld with a name and date.

**Source:** Ship It: a gate design that survives a skeptical reader

## ES-ch13.59

A student's artifact says: "The gate approved the write and the reviewer authorized it." Rewrite the sentence at the strength the evidence supports, and explain your choices of verbs.

**Points:** 5

**Rubric (1 point each):**

1. Says "approved" and "authorized" require a person and an authority the fixture never contains.
2. Uses "recorded," "computed," or "tested" for what was observed, calculated, or checked.
3. Labels the decision as simulated fixture data.
4. States what is supported: the record was written against this fingerprint, which establishes content binding.
5. States what is not claimed: that a person reviewed, was authorized, or that the proposal is safe.

**Source:** Verify and reflect

## ES-ch13.60

The Challenge assessment asks for a threat model. For the threats mutation after display, decision replay, and reviewer overload, name a control from the chapter for each and mark whether it is code or people.

**Points:** 5

**Rubric (1 point each):**

1. Pairs mutation after display with recomputing the fingerprint at execution or binding to the representation the person saw, marked as code.
2. Pairs decision replay with a unique decision ID and atomic consumption, marked as code.
3. Pairs reviewer overload with a declared queue policy and capacity, marked as people.
4. States a residual risk, such as that a fingerprint does not show the reviewer read the proposal.
5. Marks each control explicitly as code or people.

**Source:** Assessments - ungraded practice

## ES-ch13.61

Describe how the chapter relates the course gate to Anthropic's own resources, and what it says about the status of the course mechanisms and the links.

**Points:** 5

**Rubric (1 point each):**

1. Says Anthropic's "Demystifying evals for AI agents" distinguishes evaluation components.
2. Says it emphasizes examining what an agent actually did, not merely its final answer.
3. Says Claude Code permissions documentation records current product behavior to compare with the course gate.
4. Says the six-field proposal and Python fingerprint are course mechanisms, not representations of Anthropic's authentication system.
5. Says the links were checked for the approved research packet on 2026-09-06, product behavior can change, and required work stays offline.

**Source:** Anthropics

## ES-ch13.62

Explain the ownership-bias diagnostic from the companion book and how the chapter says to apply it to your gate sign-off.

**Points:** 5

**Rubric (1 point each):**

1. Names the diagnostic as ownership bias.
2. Says the build exercise has you write an attestation for something you made and force at least three entries into the "not tested" part.
3. Says for each entry you say whether you skipped it because it was out of scope or out of time.
4. Says the discomfort is the signal: you want to sign a clean bill because you built the thing.
5. Says to ask whether any untested condition is the region where harm would live.

**Source:** Computational Skepticism

## ES-ch13.63

The chapter's Irreducibly Human note names a condition under which plausibility auditing fails. State it, say what status the chapter gives the claim, and explain why it motivates building the predicate by hand before conducting Claude.

**Points:** 5

**Rubric (1 point each):**

1. States the condition: the error sits outside the reviewer's own domain knowledge, so the check sails through.
2. Says the chapter offers this as the book's argument and a design prompt, not a measurement of any reviewer.
3. Says the capacity you hand over is the capacity you need to audit the result.
4. Says humans should match each proposal to a reviewer who can audit it and send those outside that reviewer's field to a specialist.
5. Says the backlog simulation should show which reviewer each proposal went to, which were escalated and why, and which transcript lines show what Claude prepared.

**Source:** Irreducibly Human

## ES-ch13.64

State the "AI should" and "Human should" division the chapter gives for this lesson, and say where the line between them falls.

**Points:** 5

**Rubric (1 point each):**

1. Says AI should prepare the six-field proposal and expose changed fields.
2. Says AI should assemble scoped evaluation evidence and identify missing information.
3. Says AI should keep the action queued during review and can state what a reviewer would need to know to notice a wrong evidence claim.
4. Says AI should stop at the authorization boundary, since silence, timeout, model confidence, and a favorable automated score are not consent.
5. Says humans should inspect the exact proposal and consequential evidence, decide within their authority (approve, refuse, defer, or escalate), and keep a workload that permits judgment.

**Source:** Irreducibly Human

## ES-ch13.65

The chapter ends by saying a bound decision record still sits inside a team. What does the team still have to do, and where does Chapter 14 go next?

**Points:** 5

**Rubric (1 point each):**

1. Says a bound decision record still sits inside a team.
2. Says someone must own the mitigation.
3. Says someone must hear from affected people and manage retained data.
4. Says someone must respond when a threshold is crossed, and the right to say no needs an owner and a path, not only a button.
5. Says Chapter 14 moves from one approval to the governance structure around many consequential actions.

**Source:** Forward bridge
