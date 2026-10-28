# Chapter 13: Evaluation and approval gates

## MA-ch13.1

Check each statement that is true about the opening scenario, in which a reviewer approves a proposal to write `report.md` and the target later becomes `elsewhere`. Each statement is worth 1 point (5 points total).

- [ ] A. If the system retained only a generic yes, the old decision could be presented as permission for an action the reviewer never saw.
- [ ] B. Recording the reviewer's name and a timestamp is enough to keep an approval attached to what was approved.
- [ ] C. The drift happened because someone forged the reviewer's approval.
- [ ] D. Every step of the recipe was followed (a button, a name, a timestamp) and the authorization had still drifted away from its object.
- [ ] E. The scenario shows that the reviewer approved without reading the evidence.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: This is the drift the chapter describes.
- B: Name and timestamp were present and did not prevent the drift.
- C: The yes was genuinely filed with her name; it was the target that changed afterward.
- D: The chapter says the recipe was followed and the drift happened anyway.
- E: The scenario says she reads the evidence and then approves; the failure is in what the yes is bound to.

**Source:** Opening (before "What you will be able to do")

## MA-ch13.2

Check each statement that is true about what the course fixture does and what it demonstrates. Each statement is worth 1 point (5 points total).

- [ ] A. It turns six proposal fields into a stable serialized representation and computes a SHA-256 fingerprint of it.
- [ ] B. It demonstrates that a real person gave informed consent.
- [ ] C. It records the fingerprint together with a simulated decision.
- [ ] D. It demonstrates that the proposal is safe to execute.
- [ ] E. After the target is changed, the same decision no longer matches.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: That is the mechanism the fixture uses.
- B: The chapter says it does not demonstrate a real person's consent.
- C: The decision is simulated, not a person's.
- D: The chapter says it does not demonstrate the proposal's safety.
- E: This is what "content binding" means here.

**Source:** Opening (before "What you will be able to do")

## MA-ch13.3

Check each statement that is true about the three jobs and the two halves of an approval gate introduced at the start of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A fingerprint can perform the human judgment hidden inside the word "approve."
- [ ] B. To check is to ask whether an approval can still be true after the thing approved has changed, and what the record leaves out.
- [ ] C. Once Claude has run the evaluation and highlighted the diff, the yes or no can be left to Claude.
- [ ] D. An approval gate consists of authorization alone, and evaluation belongs to a separate system outside the gate.
- [ ] E. To conduct is to decide what the gate evaluates, covers, and refuses before anything is approved.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Neither automated checks nor a fingerprint can perform that judgment.
- B: That is the chapter's definition of checking.
- C: The yes, the no, and the attention behind them are a person's.
- D: The chapter treats evaluation and authorization as the two halves of an approval gate.
- E: That is the chapter's definition of conducting.

**Source:** Opening (before "What you will be able to do")

## MA-ch13.4

Check each statement that names something the chapter says you should be able to do by its end, as opposed to something it rules out or leaves outside the lesson. Each statement is worth 1 point (5 points total).

- [ ] A. Sign off on your gate whenever the automated tests pass, because withholding a sign-off signals failure.
- [ ] B. Explain why canonical serialization precedes content fingerprinting.
- [ ] C. Treat review capacity as a design constraint.
- [ ] D. Derive the cryptographic internals of SHA-256.
- [ ] E. Build a production authorization service with authentication and a role registry.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The objective is to withhold the sign-off when the record does not support signing.
- B: This is a listed objective.
- C: This is the last listed objective.
- D: Hashes appear by operational role; cryptographic internals are outside the lesson.
- E: The chapter says you need not build an enterprise authorization service.

**Source:** What you will be able to do

## MA-ch13.5

Before running anything, the chapter asks you to predict four outcomes for the course implementation. Check each statement that is a correct prediction or instruction. Each statement is worth 1 point (5 points total).

- [ ] A. An approval containing the right fingerprint but no approver name passes.
- [ ] B. You are asked to preserve your answers before running anything.
- [ ] C. Changing only the target does change the fingerprint.
- [ ] D. A matching fingerprint proves that a particular human approved.
- [ ] E. Changing dictionary key order does not change the fingerprint.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The approver must be a nonblank string.
- B: The chapter says to preserve predictions first.
- C: The target is part of the serialized proposal.
- D: A matching fingerprint says nothing about who wrote the record.
- E: Keys are sorted before serialization.

**Source:** Opening (before "What you will be able to do")

## MA-ch13.6

Check each statement that is true about the six required proposal fields and the chapter's status for them. Each statement is worth 1 point (5 points total).

- [ ] A. `evidence` points to checks that support proceeding.
- [ ] B. The chapter calls the six fields a minimum teaching contract, not a universal governance schema.
- [ ] C. The six fields are a universal governance schema that every approval system should adopt.
- [ ] D. Each field exists because a reviewer cannot decide without it.
- [ ] E. The fields are action, target, reason, effects, evidence, and rollback.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: That is the field's definition.
- B: It says so directly.
- C: They are a minimum teaching contract only.
- D: That is the stated rationale.
- E: These are the six names in `FIELDS`.

**Source:** A gate is not a button

## MA-ch13.7

Check each statement that is true about what individual proposal fields should contain. Each statement is worth 1 point (5 points total).

- [ ] A. `effects` should list only reversible local changes, since irreversible ones belong in `rollback`.
- [ ] B. "Overwrite one local Markdown file" is more reviewable than "update" as an `action`.
- [ ] C. `reason` should describe what the tool is capable of doing.
- [ ] D. `rollback` should admit when recovery is only partial or impossible.
- [ ] E. A `target` given only as a display name, with no resolved path, account, environment, or recipient, may conceal the consequential difference.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: `effects` names anticipated changes, including external and irreversible ones.
- B: The chapter says "update" may be too vague.
- C: It ties the action to the task rather than merely describing capability.
- D: The chapter says it should.
- E: The chapter says so about display names.

**Source:** A gate is not a button

## MA-ch13.8

Check each statement that is true about a generic "Allow?" prompt and about Claude's role in drafting the six fields. Each statement is worth 1 point (5 points total).

- [ ] A. Claude holds only what is in its context.
- [ ] B. Claude can fill the six fields quickly and say which ones it could not fill.
- [ ] C. Whether `report.md` resolves to the object the reviewer means is a check against the world, and it is the reviewer's.
- [ ] D. Because Claude drafted the `effects` field, the effects can be treated as complete without the reviewer checking.
- [ ] E. A generic prompt moves the cognitive burden onto the reviewer at the moment of interruption, often without the context to carry it.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is why some checks remain the reviewer's.
- B: Drafting is where Claude is good.
- C: It cannot be settled from context alone.
- D: Whether the effects are complete is the reviewer's check.
- E: The chapter says so.

**Source:** A gate is not a button

## MA-ch13.9

Check each statement that is true about a proposal whose six fields all contain fluent but meaningless strings. Each statement is worth 1 point (5 points total).

- [ ] A. Because the function checks structure, human and domain evaluation are no longer needed.
- [ ] B. The word "meaningful" in the error message means the function checks the meaning of each value.
- [ ] C. It can pass the `fingerprint` precondition.
- [ ] D. It passes because Python checks only that each retrieved value is truthy.
- [ ] E. Passing the precondition establishes that the descriptions are adequate.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The chapter says human and domain evaluation still matter.
- B: The word expresses intended use more strongly than the implementation can enforce.
- C: The precondition checks structure only.
- D: Truthiness is the whole check.
- E: Filling every field is structural validity only.

**Source:** A gate is not a button

## MA-ch13.10

Check each statement that is true about evaluation and authorization. Each statement is worth 1 point (5 points total).

- [ ] A. Putting both questions on one approval screen is harmless because they are the same question.
- [ ] B. Authorization produces the evidence, and evaluation spends it.
- [ ] C. A passing evaluation score is itself a decision to proceed.
- [ ] D. Authorization asks whether a responsible person or policy permits the action.
- [ ] E. Evaluation asks what happened, what could happen, and how well the proposal meets a stated criterion.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The chapter says the merge is where gates go soft.
- B: Evaluation produces the evidence; authorization spends it.
- C: None of the instruments returns a decision.
- D: That is the chapter's definition.
- E: That is the chapter's definition.

**Source:** Evaluation comes before authorization

## MA-ch13.11

Check each statement that is true about the order in which an evaluation set should be designed. Each statement is worth 1 point (5 points total).

- [ ] A. You should decide what would count as evidence against the proposal before you look at the evidence for it.
- [ ] B. It is acceptable to choose cases after seeing the implementation as long as every case passes.
- [ ] C. Adjusting expected answers until the suite passes is a form of calibration that strengthens the evaluation.
- [ ] D. You should look at the evidence for the proposal first and decide afterward what would count against it.
- [ ] E. If cases were picked after observing the implementation and expected answers were adjusted until everything passed, the set records accommodation, not evaluation.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: That is the stated design order.
- B: Passing cases chosen that way show only accommodation.
- C: It records accommodation instead.
- D: The order is the reverse of that.
- E: The chapter says so.

**Source:** Evaluation comes before authorization

## MA-ch13.12

Check each statement that is true about the scope of evaluation instruments. Each statement is worth 1 point (5 points total).

- [ ] A. A policy checker can say whether an exception serves the affected people.
- [ ] B. Claude should not be asked to run these instruments, because running them is the reviewer's job.
- [ ] C. A model grader's score is evidence with scope and failure modes, not a decision.
- [ ] D. A test suite can evaluate selected behavior but cannot decide whether a destructive change is worth making.
- [ ] E. If Claude runs every instrument and all of them pass, the combined result is a decision to approve.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: It can flag an unapproved directory but cannot say that.
- B: The chapter says Claude can run every one of them, and should.
- C: The chapter says so.
- D: That is its scope.
- E: None of them returns a decision.

**Source:** Evaluation comes before authorization

## MA-ch13.13

Check each statement that is true about traces, transcripts, and outcomes. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 11's false final claim had 42 in the trace and 99 in the sentence.
- [ ] B. Success narration in the agent's final sentence counts as an outcome check.
- [ ] C. A tool trace showing that a command ran is not an observation that the intended state exists.
- [ ] D. Trials and transcripts should be kept, but distinguished from actual outcomes.
- [ ] E. If a trace shows the write command ran, the file's intended contents can be assumed.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is the example the chapter cites.
- B: The chapter says success narration is not an outcome check.
- C: A trace shows what ran, not what resulted.
- D: The chapter says so.
- E: A trace does not establish the intended state.

**Source:** Evaluation comes before authorization

## MA-ch13.14

Check each statement that is true about what an evaluation set excludes and must include. Each statement is worth 1 point (5 points total).

- [ ] A. At least one case should require refusal; otherwise a system that always proceeds can appear perfect.
- [ ] B. A set built from ordinary successful writes may say nothing about symlinks, permission errors, concurrent changes, private data, or malicious paths.
- [ ] C. "Passed 20 cases" is uninterpretable until a reviewer can see which cases were run and why they represent the intended use.
- [ ] D. One case should be structurally complete but substantively weak, to test whether review reads meaning or treats field presence as safety.
- [ ] E. Exclusions should be left out of the report so the pass count is not undermined.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is the stated reason.
- B: Evaluation sets exclude.
- C: The chapter says so.
- D: That is the stated reason.
- E: Exclusions should be recorded beside the result.

**Source:** Evaluation comes before authorization

## MA-ch13.15

Check each statement that is true about metrics for judging a gate. Each statement is worth 1 point (5 points total).

- [ ] A. Deferrals and errors should be left out of the evidence because they lower the headline rate.
- [ ] B. Task success may rise while the invalid action rate also rises.
- [ ] C. A falling time-to-approval is always evidence that reviewers are working more efficiently.
- [ ] D. Reviewer burden may fall because the gate hides detail, while informed decisions worsen.
- [ ] E. A single task-success rate is the best summary of a gate's quality.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Errors and deferrals belong in the portfolio.
- B: The chapter says metrics can pull against one another.
- C: It may improve because reviewers click reflexively.
- D: That is the chapter's example.
- E: A gate needs a portfolio of evidence, not one celebratory rate.

**Source:** Evaluation comes before authorization

## MA-ch13.16

Check each statement that is true about the checks `fingerprint` makes before it computes anything. Each statement is worth 1 point (5 points total).

- [ ] A. A non-dictionary proposal fails.
- [ ] B. Extra fields beyond the six do not cause failure.
- [ ] C. A required field holding an empty list passes, because a list is still a value.
- [ ] D. Extra fields are ignored when the fingerprint is computed.
- [ ] E. A missing required field fails.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The `isinstance` check rejects it.
- B: The six names are minimum requirements, not an exact-key schema.
- C: Empty lists and other falsey values fail.
- D: They become part of the serialized proposal and affect the fingerprint.
- E: Each of the six keys must be present.

**Source:** Canonical content and its fingerprint

## MA-ch13.17

Check each statement that is true about how the course function serializes a proposal before hashing. Each statement is worth 1 point (5 points total).

- [ ] A. `sort_keys=True` canonicalizes key order for this bounded representation.
- [ ] B. Python dictionaries preserve insertion order even though JSON objects do not conceptually depend on it.
- [ ] C. Without sorted keys, two equivalent proposals built in different orders would be guaranteed to produce identical bytes.
- [ ] D. Compact separators remove default spaces so formatting choices do not alter the bytes.
- [ ] E. The serialization covers only the six named fields and ignores extras.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It removes dependence on insertion order.
- B: That is why sorting is needed.
- C: They could produce different byte sequences.
- D: That is their purpose.
- E: Python serializes the entire dictionary.

**Source:** Canonical content and its fingerprint

## MA-ch13.18

Check each statement that is true about the reversed-insertion-order test and what it shows. Each statement is worth 1 point (5 points total).

- [ ] A. It shows that the course function implements universal canonical JSON.
- [ ] B. Number formatting and Unicode normalization are already handled by sorted keys and compact separators.
- [ ] C. It is an observed property of the course function for its JSON-compatible fixture.
- [ ] D. It confirms that reversing dictionary item order does not change the resulting fingerprint.
- [ ] E. Two programs in different languages will agree on the digest whenever both use SHA-256.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The chapter explicitly denies that claim.
- B: Those issues require additional specifications.
- C: The chapter limits the claim this way.
- D: That is the test's result.
- E: Cross-language serialization requires additional specification.

**Source:** Canonical content and its fingerprint

## MA-ch13.19

Check each statement that is true about the SHA-256 digest in the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Hashing public content hides it from readers who lack the digest.
- [ ] B. A matching digest in a decision record identifies who wrote the record, since only the author could compute it.
- [ ] C. The reference implementation signs the digest with a private key as proof of authorship.
- [ ] D. The digest encrypts the proposal so its contents are hidden.
- [ ] E. The function returns a hexadecimal digest of 64 characters that serves operationally as a compact content identity.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Hashing public content does not hide it.
- B: Anyone can calculate a digest, so it says nothing about who wrote the record.
- C: No private signing key appears.
- D: The chapter does not use the digest as encryption or secrecy.
- E: If the serialized proposal changes, the comparison should fail.

**Source:** Canonical content and its fingerprint

## MA-ch13.20

Check each statement that is true about what `approved(proposal, decision)` requires. Each statement is worth 1 point (5 points total).

- [ ] A. The approver must be a nonblank string.
- [ ] B. A decision with an empty approver string passes as long as the fingerprint matches.
- [ ] C. The recorded fingerprint must equal a newly computed fingerprint of the proposal now under consideration.
- [ ] D. The `approved` value must be the exact Boolean `True`, so the string `"yes"` does not pass.
- [ ] E. The decision must be a dictionary.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A missing or blank approver fails.
- B: The approver must be nonblank.
- C: That is the content-binding condition.
- D: The check uses `is True`.
- E: That is the first condition.

**Source:** The approval predicate

## MA-ch13.21

Check each statement that is true about what a `True` result from `approved` means. Each statement is worth 1 point (5 points total).

- [ ] A. It means the decision record has the required shape and content binding.
- [ ] B. It means a real authorized human gave informed consent.
- [ ] C. The implementation contains evidence that a person saw the proposal.
- [ ] D. The implementation includes an expiry time and a revocation list.
- [ ] E. The string `"human"` in the test is the authenticated identity of the reviewer.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: That is the narrow reading the chapter gives.
- B: The chapter says not to read it that way.
- C: It has no such evidence.
- D: It has no login, signature, role registry, delegation rule, expiry time, revocation list, or decision ID.
- E: It is fixture data.

**Source:** The approval predicate

## MA-ch13.22

Check each statement that is true about what the chapter's code binds an approval to. Each statement is worth 1 point (5 points total).

- [ ] A. The code records which authority the approver holds.
- [ ] B. The code establishes that the approver read the proposal.
- [ ] C. The code limits how often a decision may be used.
- [ ] D. The fingerprint comparison ties a decision to the exact serialized proposal.
- [ ] E. The code limits how long a decision lives.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The person binding is not done by any code in the chapter.
- B: No code can do that alone.
- C: No consumption or use limit exists in the six-test lesson.
- D: That is content binding, which the code does.
- E: Scope and time are code "you have not written yet."

**Source:** The approval predicate

## MA-ch13.23

Check each statement that is true about the demo proposal and decision. Each statement is worth 1 point (5 points total).

- [ ] A. `approved(proposal, decision)` is true because the proposal's contents were judged adequate.
- [ ] B. The exact digest carries semantic meaning about the proposal.
- [ ] C. All six values of the demo proposal are nonempty, so `fingerprint` returns a 64-character SHA-256 hexadecimal string.
- [ ] D. `approved(proposal, decision)` returning true is a fixture result, not a human sign-off.
- [ ] E. The demo decision was produced by a human reviewer reading the proposal.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The predicate validates record shape and content binding, not adequacy.
- B: The chapter says we need not pretend it does.
- C: The proposal meets the precondition.
- D: The decision was generated to test content binding.
- E: It was generated to test the mechanism.

**Source:** Worked example: approval that cannot follow a changed target

## MA-ch13.24

Check each statement that is true about changing the target to `"elsewhere"` after the simulated decision. Each statement is worth 1 point (5 points total).

- [ ] A. The changed dictionary serializes to different bytes and receives a different fingerprint.
- [ ] B. A changed target creates a new decision object, and the reviewer must see it and decide again.
- [ ] C. `approved(changed, decision)` returns false because the old digest no longer equals the current proposal's digest.
- [ ] D. The system does not ask whether "elsewhere" is similar, safer, or probably what the reviewer meant.
- [ ] E. The rejection is a defect that a production gate should remove so old approvals carry over.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: One changed field changes the serialization.
- B: That is the intended behavior.
- C: The comparison fails.
- D: It only compares digests.
- E: The chapter says the rejection is what we want.

**Source:** Worked example: approval that cannot follow a changed target

## MA-ch13.25

Check each statement that is true about representation changes versus proposal changes. Each statement is worth 1 point (5 points total).

- [ ] A. Changing only dictionary insertion order while preserving all key-value pairs leaves the fingerprint the same.
- [ ] B. Two path spellings that resolve to the same file hash differently as strings.
- [ ] C. A target string can stay identical while the filesystem object it names changes.
- [ ] D. Content binding is fully semantic: the fingerprint reflects what the target actually is on disk.
- [ ] E. A gate should avoid demanding new approval for irrelevant formatting while reliably detecting consequential change.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Keys are sorted before serialization.
- B: The fingerprint is over the text.
- C: The string does not guarantee the object.
- D: It is only as semantic as the proposal representation.
- E: That is the stated goal.

**Source:** Worked example: approval that cannot follow a changed target

## MA-ch13.26

Check each statement that is true about what each observation in the chapter's evidence table supports. Each statement is worth 1 point (5 points total).

- [ ] A. A digest mismatch after a target change supports the conclusion that the changed action is necessarily harmful.
- [ ] B. Six truthy fields support the conclusion that the minimum shape passes.
- [ ] C. A decision that matches the original digest supports the conclusion that the record binds to the original content.
- [ ] D. Six truthy fields support the conclusion that the descriptions are adequate.
- [ ] E. A target change with a digest mismatch supports the conclusion that the serialized proposal changed.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That is listed as unsupported.
- B: That is the supported conclusion.
- C: That is the supported conclusion.
- D: That is listed as unsupported.
- E: That is the supported conclusion.

**Source:** Worked example: approval that cannot follow a changed target

## MA-ch13.27

Check each statement that is true about what the evidence table does and does not support. Each statement is worth 1 point (5 points total).

- [ ] A. That all six lesson tests pass tells you the reference meets six statements.
- [ ] B. A recorded fingerprint is evidence that a record was written against these bytes.
- [ ] C. A recorded fingerprint is evidence that someone read the proposal.
- [ ] D. Nothing in the evidence table supports the claim that a person reviewed the proposal.
- [ ] E. Six passing tests show that six statements are enough for a safe gate.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It tells you no more than that.
- B: That is what it shows.
- C: It is not evidence that anyone read it.
- D: The chapter says this absence is the sign-off standard.
- E: Passing six tests does not show that six statements are enough.

**Source:** Worked example: approval that cannot follow a changed target

## MA-ch13.28

Check each statement that is true about what a fingerprint does and does not answer. Each statement is worth 1 point (5 points total).

- [ ] A. A fingerprint answers "is this still the proposal?"
- [ ] B. A fingerprint does not answer "may this be done now, here, once?"
- [ ] C. A gate that leaves scope, time, and use to defaults has made no decision about them.
- [ ] D. Scope is fully determined by the proposal content, so it needs no separate design.
- [ ] E. If the proposal says "write report.md", the fingerprint alone limits how many times the operation can repeat.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It detects content change.
- B: Those are separate decisions.
- C: The chapter says it has made those decisions anyway.
- D: Approval needs scope beyond content.
- E: The fingerprint alone does not limit replay.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.29

Check each statement that matches the chapter's guidance on preventing replay of a single-use decision. Each statement is worth 1 point (5 points total).

- [ ] A. Checking that a decision is unused in one step and marking it used in a later step is equivalent to atomic consumption.
- [ ] B. Add a unique decision ID and consumption state for single-use actions.
- [ ] C. The authorization service must own the single-use rule where the action occurs.
- [ ] D. The decision ID should be checked and consumed atomically at the effect boundary.
- [ ] E. Without atomic check-and-consume, two workers can present the same valid decision simultaneously.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Two workers can both pass between the steps.
- B: That is the chapter's remedy.
- C: The chapter says so.
- D: Atomicity closes the race.
- E: That is the stated failure.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.30

Check each statement that is true about expiry and revocation. Each statement is worth 1 point (5 points total).

- [ ] A. Expiry needs an explicit time basis and comparison policy.
- [ ] B. Revocation withdraws a still-unexpired decision.
- [ ] C. A revocation record needs only to say that the decision was withdrawn.
- [ ] D. Expiry is not just a timer, because new evidence can invalidate approval early.
- [ ] E. A deadline in local time without a zone is ambiguous.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The chapter says so.
- B: That is its definition.
- C: It should record who revoked, under what authority, which proposal, and how started work is handled.
- D: The chapter says so.
- E: The chapter gives this example.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.31

Check each statement that is true about binding environment identity. Each statement is worth 1 point (5 points total).

- [ ] A. Candidate identities to bind include resolved target, account, repository revision, data classification, and tool version.
- [ ] B. Approval for a test database must not authorize production merely because the query text matches.
- [ ] C. Matching query text is sufficient to show that the same environment is meant.
- [ ] D. Which identities should force reconsideration is a judgment about consequence, not a property of the hash.
- [ ] E. You should bind as many identities as possible, since extra bindings cost nothing.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: These are the chapter's candidates.
- B: The environment identity matters.
- C: Environment identity must be bound separately.
- D: The chapter says so.
- E: Add the identities whose change should force reconsideration and no others.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.32

Check each statement that is true about rollback claims. Each statement is worth 1 point (5 points total).

- [ ] A. Once a change has been approved through a gate, it can be assumed to be a good change.
- [ ] B. Sending a message, disclosing data, or triggering a payment may be irreversible.
- [ ] C. "Restore previous file" also assumes no dependent effects have occurred and that restoration is semantically sufficient.
- [ ] D. "Restore previous file" assumes a previous copy exists and the writer can access it.
- [ ] E. A gate should say "no complete rollback" rather than inventing reassurance.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: An approved change can still be a bad one.
- B: The chapter says so.
- C: These are named assumptions.
- D: These are named assumptions.
- E: The chapter says so.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.33

Check each statement that is true about the Design part of the gate you write. Each statement is worth 1 point (5 points total).

- [ ] A. The decision owner can be named as "the team."
- [ ] B. The review budget should be stated as a measured fact even when it is only an estimate.
- [ ] C. Claude should propose which identities force a new decision, since it can see the whole plan.
- [ ] D. Friendly targets in the six fields are replaced by resolved identities.
- [ ] E. You write the gate after Claude's first implementation so you can see how the behavior turns out.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The owner should be a role that can be asked, not "the team."
- B: It is labeled an assumption unless you measured it.
- C: These are your choices; no model produced them.
- D: The Design item says so.
- E: You write the gate before asking Claude for any code.

**Source:** The gate: write the approval predicate before anything is approved

## MA-ch13.34

Check each statement that is true about the contract for the approval predicate. Each statement is worth 1 point (5 points total).

- [ ] A. A timeout with no reviewer response counts as approval once the deadline passes.
- [ ] B. Refusal and deferral are errors that should be logged as failures.
- [ ] C. The fresh fingerprint is computed at the effect boundary, not at review time.
- [ ] D. The check should read the current time inside itself so tests exercise the real clock.
- [ ] E. Absence, silence, a timeout, a model's confidence, and a favorable automated score authorize nothing.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A timeout authorizes nothing.
- B: They are recorded outcomes, not errors.
- C: That is the stated requirement.
- D: The chapter would pass the current time in so tests can say "one second after the deadline" without waiting.
- E: The chapter lists them.

**Source:** The gate: write the approval predicate before anything is approved

## MA-ch13.35

Check each statement that is true about the wrong predicates your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. The six lesson tests catch the check-then-mark version, because the lesson includes replay tests.
- [ ] B. A predicate that fingerprints only the six named fields passes all six lesson tests.
- [ ] C. A predicate that tests `approved` for truthiness rejects the string `"no"`.
- [ ] D. A predicate that tests `approved` for truthiness lets the string `"no"` approve.
- [ ] E. With the six-field-only predicate, adding `"environment": "production"` to an approved proposal forces a new approval.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The lesson has no consumption, so it has no test for it.
- B: The lesson tests do not catch it.
- C: A nonempty string is truthy and approves.
- D: A nonempty string is truthy.
- E: The extra field is outside the fingerprint, so nothing changes.

**Source:** The gate: write the approval predicate before anything is approved

## MA-ch13.36

Check each statement that is true about the failure sentence and what the gate may claim. Each statement is worth 1 point (5 points total).

- [ ] A. The gate may claim content binding, expiry, and single use under a fixture clock and a simulated approver.
- [ ] B. The failure sentence should be written before you read any output.
- [ ] C. The gate may claim that a person reviewed it, because the fixture records an approver string.
- [ ] D. Claude can write the whole gate for you without defeating its purpose, because the owner, budget, and identities are mechanical.
- [ ] E. Written afterward, the failure sentence describes the output instead of testing you.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: That is the stated claim.
- B: That is the instruction.
- C: It may not claim that a person reviewed, understood, or was authorized.
- D: They are judgments about consequence that go on record in your words.
- E: That is the stated reason.

**Source:** The gate: write the approval predicate before anything is approved

## MA-ch13.37

Check each statement that is true about the expected gate behavior in the chapter's compact evaluation set. Each statement is worth 1 point (5 points total).

- [ ] A. The "changed target" case expects the old decision to be rejected.
- [ ] B. The "vague evidence" case expects the proposal shape to be rejected.
- [ ] C. The "reordered keys" case expects a new fingerprint.
- [ ] D. The "missing rollback" case expects a structural pass and a human defer.
- [ ] E. The "exact original" case exists to test refusal.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: It blocks approval drift.
- B: It expects a structural pass and a human defer.
- C: It expects the same fingerprint.
- D: It expects the proposal shape to be rejected.
- E: It establishes the happy path.

**Source:** Build an evaluation set that can embarrass the proposal

## MA-ch13.38

Check each statement that is true about a proposal whose evidence says only "looks good." Each statement is worth 1 point (5 points total).

- [ ] A. It is a workflow failure whenever the function fingerprints a vague statement.
- [ ] B. This is a failing test of the function whatever its documented contract says.
- [ ] C. A well-named field such as `evidence` can perform the plausibility audit automatically.
- [ ] D. The current Python function will fingerprint it because the string is nonempty.
- [ ] E. Plausibility auditing means judging whether a claim is credible and consistent with what you know, independent of how confidently it was stated.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It becomes one only if documentation claims the function evaluated evidence quality.
- B: It is not a failing test if the contract is structural content binding.
- C: No field name does it; it is the reviewer's work.
- D: The function checks truthiness.
- E: That is the chapter's definition.

**Source:** Build an evaluation set that can embarrass the proposal

## MA-ch13.39

Check each statement that matches the chapter's guidance on running the evaluation and reporting results. Each statement is worth 1 point (5 points total).

- [ ] A. A single aggregate score gives the reviewer the trace they most need.
- [ ] B. Expected outcomes should be locked before running.
- [ ] C. With a tiny fixture, one held-out result can be reported as a reliability percentage.
- [ ] D. When an observation differs from expectation, the expectation should be edited quietly so the suite passes.
- [ ] E. When an observation differs from expectation, you investigate whether the implementation, the test expectation, or the original requirement is wrong, and preserve the change.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A single aggregate score discards that trace.
- B: The chapter says so.
- C: The chapter says not to inflate it that way.
- D: The change should be investigated and preserved.
- E: That is the instruction.

**Source:** Build an evaluation set that can embarrass the proposal

## MA-ch13.40

Check each statement that is true about using model graders in a gate. Each statement is worth 1 point (5 points total).

- [ ] A. A model may reward fluent rollback prose that omits an irreversible effect.
- [ ] B. A model grader that agrees with the deterministic checker removes the need for human review.
- [ ] C. Model graders can assist with qualitative fields, but their judgments need calibration and failure analysis.
- [ ] D. Qualitative grading should be paired with deterministic checks and human review proportional to the stakes.
- [ ] E. Two graders that share a prompt assumption and agree provide a second opinion.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is a named failure mode.
- B: Human review remains, proportional to stakes.
- C: The chapter says so.
- D: The chapter says so.
- E: They can agree and still be wrong together.

**Source:** Build an evaluation set that can embarrass the proposal

## MA-ch13.41

Check each statement that is true about how presentation can undermine a strong backend predicate. Each statement is worth 1 point (5 points total).

- [ ] A. Even a strong backend predicate can be undermined by presentation.
- [ ] B. If the reviewer sees a friendly summary while the fingerprint covers hidden fields, the decision binds to bytes the reviewer did not meaningfully inspect.
- [ ] C. Truncating a target or collapsing effects behind a disclosure panel can leave a record mechanically exact and socially uninformed.
- [ ] D. If the fingerprint is computed correctly, the interface cannot weaken the control.
- [ ] E. The reviewer's view is irrelevant as long as the same fingerprint is stored.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: That is the section's thesis.
- B: The chapter says so.
- C: The chapter says so.
- D: Presentation can undermine it.
- E: The decision should bind to what the reviewer saw.

**Source:** The approval interface is part of the control

## MA-ch13.42

Check each statement that matches the chapter's guidance on how an approval screen should present a proposal. Each statement is worth 1 point (5 points total).

- [ ] A. A green continue button beside a muted refusal link is acceptable because refusal is still available.
- [ ] B. Urgency language generated by the requesting agent helps reviewers prioritize.
- [ ] C. A default-selected approval is an acceptable convenience if the reviewer can change it.
- [ ] D. Link evidence claims to their artifacts rather than copying a green label.
- [ ] E. Present the action and target first.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It is listed as a dark pattern.
- B: It is listed as a dark pattern.
- C: It is listed as a dark pattern.
- D: The chapter says so.
- E: That is the instruction.

**Source:** The approval interface is part of the control

## MA-ch13.43

Check each statement that matches the chapter's guidance on what a decision binds to and what happens at execution. Each statement is worth 1 point (5 points total).

- [ ] A. On a fingerprint mismatch at execution, it is appropriate to ask the model to explain why the old approval probably still applies.
- [ ] B. The decision should bind to the representation the person actually saw, together with any referenced immutable artifacts.
- [ ] C. Someone can understand a proposal and still lack authority over the target, the data, or the recipient.
- [ ] D. If evidence can change at the same URL after approval, binding only the proposal text leaves another substitution path.
- [ ] E. At execution, recompute the fingerprint; on a mismatch, show the changed fields and return to review.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The chapter says never to invite that.
- B: The chapter says so.
- C: Understanding is not authority.
- D: The chapter says so.
- E: That is the stated procedure.

**Source:** The approval interface is part of the control

## MA-ch13.44

Check each statement that is true about the volume trap and why a perfectly bound proposal can still be reviewed superficially. Each statement is worth 1 point (5 points total).

- [ ] A. Because a proposal is perfectly bound by its fingerprint, the quality of the review is guaranteed.
- [ ] B. Speeding up the approval button restores the reviewer's judgment.
- [ ] C. The chapter presents this as the book's argument, not a measurement of any team.
- [ ] D. The case for generating ten times as much in the same time is real, but the ability to verify ten times as much does not come with it.
- [ ] E. Claude sits on the generating side of the gap.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A perfectly bound proposal can still receive superficial review.
- B: It turns the gate into a queue or a click ritual.
- C: It says so directly.
- D: That is the volume trap as the chapter states it.
- E: It can produce proposals faster than a careful reviewer can read them.

**Source:** Human attention is a finite gate resource

## MA-ch13.45

Five proposals arrive while one reviewer can carefully inspect two in the stated period. Check each statement that is true about the chapter's treatment of this scenario. Each statement is worth 1 point (5 points total).

- [ ] A. The shortfall is three proposals beyond careful-review capacity.
- [ ] B. A naive system shows all five as urgent and lets dependent agents wait indefinitely.
- [ ] C. Because checks can run automatically on all five, the system can also supply the three missing units of human attention.
- [ ] D. A governed system classifies consequence, preserves arrival and dependency information, and applies a declared queue policy.
- [ ] E. The capacity of two is a labeled assumption, not a measured result.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Five minus two is three.
- B: That is the naive pattern described.
- C: It cannot manufacture human attention.
- D: That is the governed pattern described.
- E: The chapter says so.

**Source:** Human attention is a finite gate resource

## MA-ch13.46

Proposal A is a reversible local formatting change, B sends material to an external recipient, C changes a production target, D duplicates B's effect, and E depends on C. Check each statement that is true about the chapter's handling. Each statement is worth 1 point (5 points total).

- [ ] A. A proposing model's urgency label can be used directly to order the queue.
- [ ] B. The ordering the chapter gives is the universally correct queue policy.
- [ ] C. B and C may receive priority because their effects are external or high-impact.
- [ ] D. D should be detected as a potential duplicate and held.
- [ ] E. E remains blocked on C.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Urgency labels written by the proposer should never set priority unvalidated.
- B: The chapter says the point is that someone must choose and document a policy.
- C: That is the stated reasoning.
- D: It duplicates B's effect.
- E: It depends on C.

**Source:** Human attention is a finite gate resource

## MA-ch13.47

Check each statement that is true about what to do when the queue exceeds reviewer capacity. Each statement is worth 1 point (5 points total).

- [ ] A. Pending decisions should stay valid until their deadline even when the evidence they relied on has gone stale.
- [ ] B. Past the available attention, more prompts produce habituation rather than more oversight.
- [ ] C. Cutting the information shown so reviewers can click faster is not capacity planning.
- [ ] D. The main remedy for a long queue is to shorten what reviewers are shown so each decision is faster.
- [ ] E. Timeout or queue delay can be treated as approval after a long enough wait.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Pending decisions should be invalidated when evidence or environment goes stale.
- B: The chapter says so.
- C: The chapter says so.
- D: The remedies are to pause intake, narrow scope, add qualified reviewers, or defer work.
- E: Timeout, absence, and queue delay are not approval.

**Source:** Human attention is a finite gate resource

## MA-ch13.48

Check each statement that is true about standing policies and the feedback loop on review quality. Each statement is worth 1 point (5 points total).

- [ ] A. If reviewers keep receiving nearly identical low-consequence proposals, a team can ask whether a narrow standing policy should authorize that class, with monitoring and revocation.
- [ ] B. Reviewers should be scored on throughput to keep the gate fast.
- [ ] C. Refusal and deferral should be tracked, not just approvals.
- [ ] D. Authorizing such a class is a governance decision, not an agent shortcut.
- [ ] E. If every decision is yes, that is evidence the gate is working well.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is the stated option.
- B: Scoring on throughput trains the gate to become ceremonial.
- C: The chapter says so.
- D: The chapter says so.
- E: The chapter says to ask whether reviewers have real options, adequate evidence, and support for saying no.

**Source:** Human attention is a finite gate resource

## MA-ch13.49

Check each statement that is true about the sign-off experiment from the companion book. Each statement is worth 1 point (5 points total).

- [ ] A. The experiment asks an agent for the sign-off statement for the thing you just validated.
- [ ] B. The predicted paragraph is empty, because unless you supplied the record the system has nothing to say about what was done or skipped.
- [ ] C. The shape of a sign-off is hard to produce while its substance is easy.
- [ ] D. The system can be relied on to know which checks were skipped even if given no record.
- [ ] E. The predicted result is a fluent, structurally complete paragraph that names a person and asserts a review happened.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: That is the setup.
- B: That is why it is empty.
- C: The shape is easy to produce; the substance is not.
- D: It has nothing to say without the record.
- E: That is the prediction.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.50

Check each statement that is true about the four-part attestation standard. Each statement is worth 1 point (5 points total).

- [ ] A. "What was not tested" names the conditions not probed and the failure modes known and not reached.
- [ ] B. Calibrated verbs mean "passed" should mean passed a stated test, and a weaker verb such as "believe safe" should say that it is weaker.
- [ ] C. "Who cleared which gate" names a person or role per decision who can be asked and who answers if the gate was cleared wrongly.
- [ ] D. "The team" is an acceptable answer for who cleared a gate.
- [ ] E. "What was tested" names the specific checks, against the specific criteria, with the results.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is part two.
- B: That is part four.
- C: That is part three.
- D: The chapter says a named person or role, not "the team."
- E: That is part one.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.51

Check each statement that is true about the "what was not tested" part of an attestation. Each statement is worth 1 point (5 points total).

- [ ] A. An empty "Not checked" entry shows that nothing was left untested.
- [ ] B. An affected person cannot act on a clean-bill list when the untested region is where harm lives.
- [ ] C. It is the part an AI-written sign-off omits.
- [ ] D. A list of only what passed reads as a clean bill of health.
- [ ] E. The part can be omitted when all the tests that were run passed.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: If you cannot fill it with real entries, you have not looked hard enough.
- B: That is the stated reason it matters.
- C: The chapter says so.
- D: That is the risk the chapter names.
- E: Omitting it is what makes the document dishonest.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.52

Check each statement that is true about what a fingerprint cannot show and about deferral. Each statement is worth 1 point (5 points total).

- [ ] A. Treating anything but approval as failure is good practice because it keeps work moving.
- [ ] B. A recorded approver name proves the reviewer understood the target.
- [ ] C. "The local tests pass, but remote publication permissions and data licensing are unverified; defer" is described as a successful gate outcome.
- [ ] D. The fingerprint cannot show that the reviewer opened the test report, understood the target, or had enough time.
- [ ] E. A signature can strengthen identity evidence without proving comprehension.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It pressures people to manufacture certainty.
- B: Identity evidence does not prove comprehension.
- C: The chapter gives it as an example.
- D: Those are process questions.
- E: The chapter says so.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.53

Check each statement that is true about the trade-off an attestation regime makes. Each statement is worth 1 point (5 points total).

- [ ] A. It optimizes for legible answerability: after a failure you can find the signer, read what they claimed, and see what they did not warrant.
- [ ] B. Governance must name organizational owners and escalation paths, not place every consequence on the person who clicked.
- [ ] C. It sacrifices speed and deniability.
- [ ] D. If the only outcome the process permits is "signed," it is a rubber stamp with a person's name on it.
- [ ] E. The companion's attestation standard authenticates a signature and provides a legal compliance determination.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is the stated benefit.
- B: The chapter says so.
- C: That is the stated cost.
- D: The chapter says so.
- E: The chapter says it does neither.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.54

Check each statement that is true about the eight-step sequence. Each statement is worth 1 point (5 points total).

- [ ] A. The evaluations of step 3 are run after the decision is recorded in step 6.
- [ ] B. Step 4 freezes the exact proposal and computes its fingerprint.
- [ ] C. Step 5, presenting evidence to a reviewer, is where the gate does its work in a way you can fully automate.
- [ ] D. Step 7 rechecks fingerprint, expiry, revocation, and use constraints at execution.
- [ ] E. Step 3 runs scoped evaluations and records exclusions.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Evaluation comes before the decision.
- B: That is step 4.
- C: Steps 5 and 6 are where the gate stops being yours to automate.
- D: That is step 7.
- E: That is step 3.

**Source:** Where the gate sits in the build so far

## MA-ch13.55

Check each statement that is true about what happens when the proposal changes and about what approval guarantees. Each statement is worth 1 point (5 points total).

- [ ] A. Approval permits a bounded attempt and does not guarantee the intended result.
- [ ] B. A changed proposal can reuse the old approval if the fingerprint comparison is skipped.
- [ ] C. A valid old approval is evidence about history, not authority for the new object.
- [ ] D. The proposal fingerprint, the effect evidence, and the post-action check should be separate linked records.
- [ ] E. Changing the proposal returns the workflow to step three or earlier.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The chapter says so.
- B: The old approval is not authority for the new object.
- C: The chapter says so.
- D: The chapter says so.
- E: The chapter says so.

**Source:** Where the gate sits in the build so far

## MA-ch13.56

Check each statement that is true about the Build It baseline. Each statement is worth 1 point (5 points total).

- [ ] A. You read the six tests first and write down which input should fail and why.
- [ ] B. You write `fingerprint` and `approved` yourself before opening the reference solution.
- [ ] C. Your own version is the baseline against which you measure Claude's version.
- [ ] D. You can audit a predicate you never wrote by reading Claude's explanation of it.
- [ ] E. A gate that approves the wrong thing does not crash.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is the instruction.
- B: That is the instruction.
- C: The chapter says so.
- D: You cannot audit a predicate you have never written.
- E: The failures this chapter cares about are quiet ones.

**Source:** Build It: the baseline that lets you audit

## MA-ch13.57

Check each statement that is true about conducting Claude Code against your gate. Each statement is worth 1 point (5 points total).

- [ ] A. You give Claude Code your implementation so that it can extend it.
- [ ] B. Whether checking and recording a used decision happen as one step is a style choice not worth reading the diff for.
- [ ] C. You give Claude Code the contract and the test list but not your implementation.
- [ ] D. If the deliberately wrong version passes your tests, that confirms your tests are strong.
- [ ] E. A failing test is often a gap in your gate that Claude could not see because it only had what you wrote.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: You give it the contract and tests, not your implementation.
- B: It is one of the three places a human decision hides.
- C: That is the instruction.
- D: It means your tests were too weak.
- E: The chapter says so.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch13.58

Check each statement that is true about the Ship It artifact. Each statement is worth 1 point (5 points total).

- [ ] A. You calculate the fingerprint only after the proposal is ready for review and freeze or copy the reviewed representation.
- [ ] B. The decision record carries the fingerprint, the simulated decision labeled as a simulation, and the unresolved gaps.
- [ ] C. You enumerate production gaps such as authentication, single-use consumption, expiry, revocation, audit access, privacy retention, queue behavior, and incident response.
- [ ] D. You may supply a classmate's approval from memory if the classmate would likely agree.
- [ ] E. The artifact contains before-and-after gate wording, an evaluated proposal, rejection tests, and a decision record.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That prevents unnoticed mutation.
- B: That is the listed content.
- C: The chapter lists these.
- D: Never fabricate a classmate's or stakeholder's approval.
- E: That is the listed content.

**Source:** Ship It: a gate design that survives a skeptical reader

## MA-ch13.59

Check each statement that is true about the decision record and the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. The decision record is what a reviewer produces: approve, refuse, or defer, with scope, gaps, and authority.
- [ ] B. If the evidence does not support signing, you must sign anyway to complete the artifact.
- [ ] C. If you cannot fill "Not checked" with real entries, you have not looked hard enough, not found nothing.
- [ ] D. When the reviewer is a simulation, the decision record is a labeled fixture and not a decision.
- [ ] E. The sign-off is what you produce about the gate you built.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: That is the chapter's definition.
- B: Withholding is an honest result.
- C: The chapter says so.
- D: The chapter says so.
- E: That is the chapter's definition.

**Source:** Ship It: a gate design that survives a skeptical reader

## MA-ch13.60

Check each statement that is true about the driver's seat table and the delegated-versus-retained record. Each statement is worth 1 point (5 points total).

- [ ] A. Claude should draft the six-field proposal, flag the fields it could not fill, and show the diff against the last proposal.
- [ ] B. You choose the cases that can embarrass the proposal and record exclusions.
- [ ] C. Claude should keep the action queued and stop at the boundary.
- [ ] D. Claude should choose the verb for what the gate supports and sign or withhold.
- [ ] E. In the artifact, you record one task you delegated and one judgment you retained.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is Claude's part of the first row.
- B: That is your part of the evaluation row.
- C: That is Claude's part of the approval row.
- D: You choose the verb; you sign or withhold.
- E: The chapter asks for both.

**Source:** Ship It: a gate design that survives a skeptical reader

## MA-ch13.61

Check each statement that is true about verification and reflection at the end of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Verification begins with claims small enough to test, such as reversed insertion order leaving the fingerprint unchanged.
- [ ] B. One reflection question is which distinction you originally collapsed, such as a hash and a decision.
- [ ] C. "Recorded" describes an observation, "computed" a calculation, and "tested" a check you ran.
- [ ] D. "Approved" and "authorized" require a person and an authority the fixture never contains.
- [ ] E. The strongest sentence in the artifact should say "approved," because the fixture produced an approval.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The chapter gives this example.
- B: The chapter poses it.
- C: Those are the verbs the chapter endorses.
- D: The chapter says so.
- E: The fixture contains no person or authority.

**Source:** Verify and reflect

## MA-ch13.62

Check each statement that is true about the chapter's Anthropics section. Each statement is worth 1 point (5 points total).

- [ ] A. It points to Anthropic's "Demystifying evals for AI agents," which emphasizes examining what an agent actually did, not merely its final answer.
- [ ] B. Required work for the chapter depends on direct API use.
- [ ] C. It points to the Claude Code permissions documentation as current product behavior to compare with the course gate.
- [ ] D. The primary links were checked for the approved research packet on 2026-09-06.
- [ ] E. The six-field proposal and Python fingerprint are Anthropic's authentication system.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is how the chapter describes it.
- B: Required work stays offline.
- C: That is the stated use.
- D: The chapter gives that date.
- E: They are course mechanisms, not representations of Anthropic's system.

**Source:** Anthropics

## MA-ch13.63

Check each statement that is true about the Computational Skepticism note. Each statement is worth 1 point (5 points total).

- [ ] A. The diagnostic it adds is ownership bias.
- [ ] B. Ownership bias is the tendency to under-sign work you built yourself.
- [ ] C. Every untested entry must be marked out of scope, because out of time is not an acceptable reason.
- [ ] D. The note asks you to list untested conditions only when they are within the scope of the gate.
- [ ] E. The exercise has you force at least three entries into the "not tested" part.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The note names it.
- B: It is the pull to sign a clean bill because you built the thing.
- C: Each is marked as out of scope (and why) or out of time.
- D: Out-of-scope items are listed too: each of the three is marked out of scope (and why) or out of time.
- E: That is the build exercise.

**Source:** Computational Skepticism

## MA-ch13.64

Check each statement that is true about the Irreducibly Human note on supervisory cognition. Each statement is worth 1 point (5 points total).

- [ ] A. The capacity you hand over is the capacity you need to audit the result, which is why you build the predicate by hand first.
- [ ] B. AI should decide when to approve, because a human can only check afterward.
- [ ] C. The chapter offers this as the book's argument and a design prompt, not a measurement of any reviewer.
- [ ] D. Plausibility auditing fails when the error sits outside the reviewer's own domain knowledge, so the check sails through.
- [ ] E. Humans should route every proposal to the same reviewer regardless of the reviewer's field.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is the stated reason.
- B: AI should stop at the authorization boundary.
- C: It says so.
- D: That is the condition named.
- E: Humans should match each proposal to a reviewer who can audit it.

**Source:** Irreducibly Human

## MA-ch13.65

Check each statement that is true about the "AI should" and "Human should" statements. Each statement is worth 1 point (5 points total).

- [ ] A. AI should decide which pending proposals are within its own authority to approve.
- [ ] B. AI should prepare the six-field proposal, expose changed fields, assemble scoped evaluation evidence, identify missing information, and keep the action queued during review.
- [ ] C. Silence, timeout, model confidence, and a favorable automated score are not consent.
- [ ] D. Humans should send proposals outside a reviewer's field to a specialist and keep a workload that permits judgment.
- [ ] E. The backlog simulation should show which reviewer each proposal went to, which were escalated and why, and which transcript lines show what Claude prepared.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: AI stops at the authorization boundary.
- B: That is the AI should list.
- C: The chapter says so.
- D: That is the Human should list.
- E: That is the requested evidence of the split.

**Source:** Irreducibly Human
