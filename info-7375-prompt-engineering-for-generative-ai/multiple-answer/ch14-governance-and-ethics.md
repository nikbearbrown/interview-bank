# Chapter 14: Governance and ethics

## MA-ch14.1

Check each statement that is true about the situation in the chapter's opening, where every register field is filled and nobody is responsible. Each statement is worth 1 point (5 points total).

- [ ] A. A governance record can be structurally complete and operationally hollow.
- [ ] B. If the incident contact field says "project owner," a named person has accepted responsibility for incidents.
- [ ] C. Python can truthfully report ready-for-human-review while no threshold triggers any response.
- [ ] D. The chapter's central question is whether the register is complete.
- [ ] E. The chapter asks what has been decided, who decided it, and who will answer when the system causes harm.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: That is the opening sentence's point.
- B: A role label can fill the field with no one accepting the work.
- C: The status describes structure, not operation.
- D: It asks what "complete" is standing in for.
- E: That is the question posed when the status turns green.

**Source:** Chapter 14 - Governance and ethics (opening)

## MA-ch14.2

Check each statement that is true about Claude filling in the governance register. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can propose an owner, a threshold, a retention period, and a paragraph on risk in seconds.
- [ ] B. Naming an owner in its draft makes that person the owner.
- [ ] C. Claude was not in the room with the people the workflow touches.
- [ ] D. Claude's draft makes Claude answerable for the workflow after the conversation ends.
- [ ] E. A fluent, plausible draft is evidence that a real person accepted the role it names.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The draft is fast, fluent, and plausible.
- B: Claude cannot make anyone the owner it names.
- C: It has no first-hand context for them.
- D: Nothing in its draft makes it answerable.
- E: Fluency says nothing about acceptance.

**Source:** Chapter 14 - Governance and ethics (opening)

## MA-ch14.3

Check each statement that is true about the four predictions the chapter asks you to make before reading the implementation. Each statement is worth 1 point (5 points total).

- [ ] A. One asks what issues an empty record will report.
- [ ] B. One asks which Claude model the validator should call.
- [ ] C. One asks whether retention_days=True will pass as one day.
- [ ] D. The chapter says to discard the predictions once the code has run.
- [ ] E. One asks how many labels the data-class allowlist contains.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Prediction one.
- B: The validator is an offline teaching mechanism.
- C: Prediction two.
- D: It says to preserve the answers.
- E: The four cover the empty record, True, a string for data_classes, and whether ready means reviewed.

**Source:** What you will be able to do

## MA-ch14.4

Check each statement that is true about "What you will be able to do" and the prerequisites stated with it. Each statement is worth 1 point (5 points total).

- [ ] A. You should be able to distinguish ready-for-human-review from approval, consent, compliance, or ethical acceptability.
- [ ] B. You should be able to write the gate for a team register before it is filled, with the person who decided each item.
- [ ] C. Naming a generic "risk" in the register is the way to identify harms.
- [ ] D. You should be able to say which work you handed to Claude and which you kept.
- [ ] E. Chapters 5, 12, and 13 on authority boundaries, shared memory, and approval gates should be completed first.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: First listed outcome.
- B: The "conduct" outcome.
- C: The outcome is concrete harms and affected people rather than generic "risk".
- D: The "drive" outcome.
- E: Stated prerequisites.

**Source:** What you will be able to do

## MA-ch14.5

Check each statement that is true about the five choices that sit under every register. Each statement is worth 1 point (5 points total).

- [ ] A. Owner: who accepts responsibility for the workflow as a continuing system, and what they are allowed to stop.
- [ ] B. Threshold: which observable signal triggers a response, and what that response is.
- [ ] C. Retention is only a question of how many days a record is kept.
- [ ] D. Consultation: who was asked, what their answer could have changed, and what is still pending.
- [ ] E. Recourse is settled once an incident contact address is listed.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Stated definition.
- B: Stated definition.
- C: It also asks which copies exist and how deletion is checked.
- D: Stated definition.
- E: Recourse asks how an affected person reaches a human who can change the outcome.

**Source:** Who decided? Five choices that exist before the form does

## MA-ch14.6

Check each statement that is true about how the five choices relate to the register form. Each statement is worth 1 point (5 points total).

- [ ] A. An assignment of authority exists only when someone accepts it.
- [ ] B. Claude can accept an owner role on the team's behalf once it has drafted the role.
- [ ] C. The form is filled first, and people then decide whatever it requires.
- [ ] D. A team that fills the form first has still made the decisions, only in a different order.
- [ ] E. The five choices are drafting problems that Claude can finish in a minute.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Acceptance is what makes an assignment.
- B: It can draft all five but cannot accept any.
- C: People decide first and the form records the decisions.
- D: It has produced the shape of a decision, not a decision.
- E: None of them is a drafting problem.

**Source:** Who decided? Five choices that exist before the form does

## MA-ch14.7

Check each statement that is true about the two gates in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The validator's pass condition is that a named person accepted each role.
- [ ] B. The validator is a machine gate whose pass condition is a list of tests you can run.
- [ ] C. The register's content is a human gate, and its pass condition includes that the routes work when someone uses them.
- [ ] D. A passing validator is evidence for both gates.
- [ ] E. Treating the validator as evidence for the human gate is the failure the opening sentence describes.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That is the pass condition of the human gate.
- B: Stated definition.
- C: Stated definition.
- D: It is evidence for the first gate only.
- E: "Every field is filled. Nobody is responsible."

**Source:** Who decided? Five choices that exist before the form does

## MA-ch14.8

Check each statement that is true about the design step of the chapter's gate. Each statement is worth 1 point (5 points total).

- [ ] A. For your capstone workflow, write one sentence for each of the five decisions and, beside it, the name of the person who made it.
- [ ] B. Where no person has accepted a decision, leave the entry blank until someone volunteers.
- [ ] C. While a decision is unresolved, the workflow may proceed unchanged until someone accepts.
- [ ] D. Do this design step after Claude drafts the register, as a review of the draft.
- [ ] E. A model can tell you which of your five decisions are real.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The design step.
- B: Write "unresolved".
- C: It is constrained, for example to a private draft, synthetic data, or no external write.
- D: It comes before you ask Claude for anything.
- E: No model can know which of them are real.

**Source:** The gate: write the governance before the form is filled

## MA-ch14.9

Check each statement that is true about the validator contract in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. A record with nothing in it reports all seven field names and the status incomplete.
- [ ] B. With every field present, a negative retention count raises ValueError.
- [ ] C. A string where the list of data classes belongs is wrapped into a one-item list.
- [ ] D. A data class outside public, synthetic, and internal raises ValueError.
- [ ] E. A truthy external_write raises ValueError.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated contract.
- B: Stated contract.
- C: With every field present it raises ValueError.
- D: It returns review-required.
- E: It adds the issue "external action approval".

**Source:** The gate: write the governance before the form is filled

## MA-ch14.10

Check each statement that is true about the two wrong versions your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. Replacing the exact-type retention test with isinstance(days, int) lets retention_days=True pass as one day.
- [ ] B. The lesson's six tests still pass against the isinstance variant.
- [ ] C. Replacing the omission check with a falsiness test reports a retention of zero as missing.
- [ ] D. One of the lesson's six tests catches the falsiness variant.
- [ ] E. If your tests catch only the falsiness variant, the gate is finished.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Python treats True as an integer.
- B: So that variant escapes the six tests.
- C: Zero is a legitimate design intent.
- D: The chapter says so.
- E: The list must tell the right program from both wrong ones.

**Source:** The gate: write the governance before the form is filled

## MA-ch14.11

Check each statement that is true about the "what a failure looks like" sentence and about what the register may claim. Each statement is worth 1 point (5 points total).

- [ ] A. The sentence is dated and describes what you would see if the register were hollow although the validator is green.
- [ ] B. One example is sending the named incident contact a labeled test report and getting no acknowledgment within the stated time.
- [ ] C. Writing the sentence after reading the validator's output is better because it then matches what you saw.
- [ ] D. The register may claim a minimum shape, and that named people accepted named roles on named dates.
- [ ] E. A green validator lets the register claim the workflow is ethical, consented to, and compliant.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Stated requirement.
- B: The chapter's example.
- C: Written after reading output, it describes the output instead of testing understanding.
- D: Stated claim.
- E: It cannot say any of these.

**Source:** The gate: write the governance before the form is filled

## MA-ch14.12

Check each statement that is true about what the register fields are meant to open. Each statement is worth 1 point (5 points total).

- [ ] A. The owner is accountable for the workflow as a continuing system, not merely its initial code.
- [ ] B. Purpose bounds why the system exists and reveals later use beyond that scope.
- [ ] C. The approver identifies the decision route.
- [ ] D. Evaluation names the evidence used to judge performance and failure.
- [ ] E. The fields are sufficient answers once each one contains a string.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: They are necessary prompts, not sufficient answers.

**Source:** A register makes questions inspectable

## MA-ch14.13

Check each statement that is true about weak field values and what the validator can see. Each statement is worth 1 point (5 points total).

- [ ] A. owner: "someone" occupies the field without assigning work.
- [ ] B. purpose: "use AI" does not bound use.
- [ ] C. Python cannot infer substantive adequacy from truthy strings.
- [ ] D. evaluation: "test" is reported as a missing field.
- [ ] E. A whitespace-only value is reported as missing.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The chapter's example.
- B: The chapter's example.
- C: It can only force omissions into view.
- D: It occupies the field; it just does not say which outcomes were tested.
- E: Whitespace can pass the missing check.

**Source:** A register makes questions inspectable

## MA-ch14.14

Check each statement that is true about the missing-field check. Each statement is worth 1 point (5 points total).

- [ ] A. A field counts as missing if its key is absent.
- [ ] B. A field counts as missing if its value is None, the empty string, or the empty list.
- [ ] C. A value of zero is reported as missing in most fields.
- [ ] D. An empty dictionary is reported as missing.
- [ ] E. An empty record reports all seven field names.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Stated rule.
- B: Stated rule.
- C: Zero in most fields can pass.
- D: An empty dictionary can pass.
- E: The executed fixture observed the seven-item report.

**Source:** A register makes questions inspectable

## MA-ch14.15

Check each statement that is true about the design choice behind the validator. Each statement is worth 1 point (5 points total).

- [ ] A. It refuses only what it can refuse exactly.
- [ ] B. Judging "project team" would require a list of bad owner names, and lazy entries step around such lists.
- [ ] C. Because it refuses exactly, the validator can also tell whether each line is true.
- [ ] D. The validator rejects vague owners such as "everyone".
- [ ] E. A longer list of bad owner names would let the validator judge each line.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The named design choice.
- B: The chapter's reason.
- C: Deciding whether a line is true is left to people.
- D: A weak but complete record can return ready-for-human-review.
- E: Lazy entries step around such lists.

**Source:** Tear down the validator

## MA-ch14.16

Check each statement that is true about the retention check, which requires type(days) to be int and days to be nonnegative. Each statement is worth 1 point (5 points total).

- [ ] A. retention_days=True is rejected even though bool subclasses int.
- [ ] B. A negative value is rejected.
- [ ] C. Zero is rejected because it is not a positive count.
- [ ] D. The implementation enforces immediate deletion when retention_days is zero.
- [ ] E. A valid retention number is evidence that the data lifecycle follows it.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Exact int typing rejects Booleans.
- B: It fails the range check.
- C: Zero is allowed.
- D: It does not enforce deletion or define transient copies.
- E: A number in a record is not evidence.

**Source:** Tear down the validator

## MA-ch14.17

Check each statement that is true about the data-class shape check. Each statement is worth 1 point (5 points total).

- [ ] A. The value must be a list and every element must be a string.
- [ ] B. Passing the single string "public" instead of a list fails the shape check.
- [ ] C. Any string inside the list passes the shape check, including unknown labels.
- [ ] D. An empty data_classes list is caught by the missing-field check, not by the shape check.
- [ ] E. The shape check rejects the label "personal" because it is not in the allowlist.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated shape.
- B: Iterability is not the declared container shape.
- C: Unknown labels are caught later.
- D: The missing check already rejects it.
- E: The allowlist comparison comes next and flags it for review.

**Source:** Tear down the validator

## MA-ch14.18

Check each statement that is true about the classroom allowlist of data classes. Each statement is worth 1 point (5 points total).

- [ ] A. The allowlist contains public, synthetic, and internal.
- [ ] B. Anything outside those three labels produces a review issue.
- [ ] C. The allowlist is case-sensitive, so a capitalized "Public" also goes to review.
- [ ] D. When the machine cannot tell, the conservative routing action sends the decision to a person.
- [ ] E. A class labeled internal is therefore safe for the proposed workflow.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: The code appends a sensitive-or-unknown issue.
- C: Stated trade-off.
- D: Stated principle.
- E: The code does not decide that.

**Source:** Tear down the validator

## MA-ch14.19

Check each statement that is true about external_write and the returned status. Each statement is worth 1 point (5 points total).

- [ ] A. A truthy external_write adds "external action approval" to the issues.
- [ ] B. The check identifies the external target and authenticates the approval.
- [ ] C. The check marks a condition that needs another control.
- [ ] D. The status is review-required when issues exist.
- [ ] E. A truthy external_write on an otherwise complete record yields the status incomplete.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Stated.
- B: It does neither.
- C: It does not execute Chapter 13's fingerprint gate.
- D: Otherwise it is ready-for-human-review.
- E: It adds an issue, so the status is review-required.

**Source:** Tear down the validator

## MA-ch14.20

Check each statement that is true about why the demo record returns ready-for-human-review. Each statement is worth 1 point (5 points total).

- [ ] A. Thirty has exact type int and is nonnegative.
- [ ] B. data_classes is a list whose only item is a string, and "public" is in the allowlist.
- [ ] C. A truthy external-write flag was present but ignored.
- [ ] D. The result shows that a particular instructor accepted the approval responsibility.
- [ ] E. The result is strong evidence that someone confirmed each line.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It passes the retention check.
- B: It passes the shape and allowlist checks.
- C: There is no truthy external-write flag.
- D: "Instructor" may describe a role without such proof.
- E: It is accurate about the function but weak as governance evidence.

**Source:** Complete, reviewable, and still weak

## MA-ch14.21

Check each statement that is true about the weaknesses the chapter finds in the demo record. Each statement is worth 1 point (5 points total).

- [ ] A. "Project team" may name no accountable individual.
- [ ] B. "Citation audit" leaves the sampling, checker, criteria, and failure response unstated.
- [ ] C. "Project owner" may be unreachable to affected people.
- [ ] D. Thirty days says nothing about caches, backups, exported artifacts, or deletion verification.
- [ ] E. The validator's ready-for-human-review output is inaccurate about the function.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: The result is accurate about the function.

**Source:** Complete, reviewable, and still weak

## MA-ch14.22

Check each statement that is true about running assess on different records. Each statement is worth 1 point (5 points total).

- [ ] A. assess({}) returns incomplete with all seven field names in issues.
- [ ] B. Setting data_classes to ["personal"] with other required values present raises ValueError.
- [ ] C. Setting external_write=True on a public-data record leaves the status ready-for-human-review.
- [ ] D. These cases demonstrate agreement by named people and stakeholder consent.
- [ ] E. A review-required status shows the sensitive class has been mitigated.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A useful negative case.
- B: It yields review-required with the sensitive-or-unknown issue.
- C: It adds the external-action issue.
- D: They demonstrate routing only.
- E: It only routes the decision to a person.

**Source:** Complete, reviewable, and still weak

## MA-ch14.23

Check each statement that is true about the structurally complete but weak record with owner "everyone", purpose "help", retention 99999, approver "manager", evaluation "looks fine", and incident contact "team". Each statement is worth 1 point (5 points total).

- [ ] A. The current function can return ready-for-human-review for it.
- [ ] B. That is not a defect relative to the function's narrow contract.
- [ ] C. It is a counterexample to broad claims about what the status means.
- [ ] D. The retention of 99999 is rejected because it is too large.
- [ ] E. Human review can be skipped for it since the validator passed it.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The chapter says so.
- B: The contract is structural.
- C: The status is not approval.
- D: It is a nonnegative integer and passes.
- E: The human review must interrogate meaning.

**Source:** Complete, reviewable, and still weak

## MA-ch14.24

Check each statement that is true about the chapter's evidence table, which pairs a register observation with what it supports and what remains open. Each statement is worth 1 point (5 points total).

- [ ] A. "Seven fields present" supports a minimum record shape, while adequacy and acceptance remain open.
- [ ] B. "Retention is a nonnegative integer" supports that the declared day count has valid shape, while the actual deletion lifecycle remains open.
- [ ] C. "Classes are known labels" supports that classification is accurate.
- [ ] D. "External-write issue" supports that the external target is authorized.
- [ ] E. "Ready for human review" supports that consent, ethics, and compliance were established.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: First row.
- B: Second row.
- C: It supports only that no unknown label appears under the course allowlist.
- D: It supports a routing trigger; target, authority, and outcome remain open.
- E: Those remain open.

**Source:** Complete, reviewable, and still weak

## MA-ch14.25

Check each statement that is true about the verb ladder the chapter offers for describing a register line. Each statement is worth 1 point (5 points total).

- [ ] A. Use the weakest verb your evidence supports.
- [ ] B. "Listed" fits when a name appears.
- [ ] C. "Exercised" fits when you ran the route and watched it work.
- [ ] D. "Verified" fits when you inspected the store yourself.
- [ ] E. The ladder is an industry standard for audit evidence.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated rule.
- B: Lowest rung.
- C: Stated.
- D: Stated.
- E: It is a teaching device for this chapter, not an industry standard.

**Source:** Complete, reviewable, and still weak

## MA-ch14.26

Check each statement that is true about generic risk language and concrete harms. Each statement is worth 1 point (5 points total).

- [ ] A. "There may be bias or privacy concerns" can be pasted into almost any register and tells no one what to do.
- [ ] B. Applied ethics asks who can be affected, through which mechanism, with what consequence, and whether they can contest it.
- [ ] C. For a public-course-note summarizer, affected groups may include students whose work is quoted and maintainers who must correct errors.
- [ ] D. Omitting a required accommodation route is one concrete harm for such a summarizer.
- [ ] E. The person who pays for a harm is usually the same person who could have prevented it.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: Usually a different person.

**Source:** Who bears the error

## MA-ch14.27

Check each statement that is true about the distribution questions the chapter asks. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter asks who receives the benefit.
- [ ] B. The chapter asks who bears false positives and false negatives.
- [ ] C. The chapter asks who is absent from the development examples.
- [ ] D. The chapter asks who can reach a human when the output is wrong.
- [ ] E. The distribution questions concern only average accuracy across all users.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: They ask who pays and who is exposed.

**Source:** Who bears the error

## MA-ch14.28

Check each statement that is true about Agent A (reads public notes, creates a local draft, retains inputs for one day, requires human publication) and Agent B (reads internal records, publishes externally, retains complete traces for a year), which have the same measured accuracy on the same bounded evaluation set. Each statement is worth 1 point (5 points total).

- [ ] A. Agent B has a broader action surface than Agent A.
- [ ] B. Agent B has a longer privacy exposure than Agent A.
- [ ] C. Equal accuracy gives the two agents equal risk.
- [ ] D. Accuracy describes the surrounding power and consequences, while governance describes selected outputs under selected trials.
- [ ] E. Ethics can be appended after model selection because accuracy fixes the harm surface.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: B publishes externally.
- B: A year of traces versus one day.
- C: Equal accuracy does not produce equal risk.
- D: It is the other way around.
- E: Architecture choices shape the harm surface before the first score.

**Source:** Who bears the error

## MA-ch14.29

Check each statement that is true about the constructed case of two summarizers that make the same number of deadline errors on the same bounded set. Each statement is worth 1 point (5 points total).

- [ ] A. One errs by stating a deadline its sources do not support.
- [ ] B. The other errs by leaving the deadline out when sources conflict.
- [ ] C. Students who plan around a wrong date bear the first error.
- [ ] D. Students who must ask, and the maintainers who field their questions, bear the first error.
- [ ] E. The accuracy figure tells the team which error to prefer.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: They bear the second.
- E: Nothing in the number says; that is a choice about whose cost counts.

**Source:** Who bears the error

## MA-ch14.30

Check each statement that is true about the companion book's point on fairness definitions for systems that rank or evaluate people. Each statement is worth 1 point (5 points total).

- [ ] A. Equal rates of favorable prediction across groups is one of three reasonable definitions.
- [ ] B. The three definitions cannot all hold when the groups' base rates differ, short of perfect prediction.
- [ ] C. The book treats each definition as a values claim about which error or which equality matters.
- [ ] D. The book treats choosing among the definitions as an optimization problem.
- [ ] E. In the sentencing risk-score case, the disagreement arose because one party reported inaccurate numbers.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: It is a decision with an owner, not an optimization.
- E: Both reported accurate numbers and disagreed about which should count.

**Source:** Who bears the error

## MA-ch14.31

Check each statement that is true about owners, thresholds, and mitigations. Each statement is worth 1 point (5 points total).

- [ ] A. A mitigation without an owner is a wish.
- [ ] B. An owner without authority or resources is a label.
- [ ] C. A threshold without an observable signal is prose.
- [ ] D. A 99 percent pass rate shows that no severe harm occurred.
- [ ] E. Every threshold should trigger an immediate stop on a single occurrence.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: It can conceal one severe disclosure.
- E: Some events do; others justify trend monitoring.

**Source:** Owners, thresholds, and bounded responses

## MA-ch14.32

Check each statement that is true about the rewritten record that begins "The content owner reviews every unsupported-source flag before publication." Each statement is worth 1 point (5 points total).

- [ ] A. It names a signal, threshold, owner, response, scope, and recovery condition.
- [ ] B. Another person can now test whether the process ran.
- [ ] C. It is complete, and nothing about it can be improved.
- [ ] D. Work resumes as soon as the incident contact has examined the affected drafts.
- [ ] E. The standard for a threshold is that a stranger can tell, from the record, whether it fired.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The chapter lists these.
- B: That is the benefit of the rewrite.
- C: It can still be improved, for example in what counts as approved.
- D: It resumes only after correction and a repeated citation audit.
- E: Stated standard.

**Source:** Owners, thresholds, and bounded responses

## MA-ch14.33

Check each statement that is true about retention as a lifecycle. Each statement is worth 1 point (5 points total).

- [ ] A. retention_days: 30 is a policy input, not a deletion mechanism.
- [ ] B. Only the application log needs tracing; caches, backups, and repository history are outside the lifecycle.
- [ ] C. Stores you inspected are verified; the provider's and the backups' are, at best, listed.
- [ ] D. "Removed from this dictionary" means the data is erased everywhere.
- [ ] E. Unknown provider or backup behavior should be assumed to match the stated retention period.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Stated.
- B: The trace covers every copy in scope, including those.
- C: Stated.
- D: It is not "erased everywhere."
- E: Mark unknowns; do not turn a desired policy into a claim.

**Source:** Retention is a lifecycle

## MA-ch14.34

Check each statement that is true about what to state for each data class. Each statement is worth 1 point (5 points total).

- [ ] A. State why it is collected and the minimum needed.
- [ ] B. State who can access it.
- [ ] C. State when the clock begins.
- [ ] D. State how deletion is performed and how deletion is checked.
- [ ] E. Derived summaries cannot reveal source information.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: Derived summaries may still reveal source information.

**Source:** Retention is a lifecycle

## MA-ch14.35

Check each statement that is true about zero-day retention and incident replay. Each statement is worth 1 point (5 points total).

- [ ] A. Zero-day retention may mean delete immediately after the task, do not persist application data, or retain only de-identified evidence.
- [ ] B. Temporary memory and provider-side processing still exist under zero-day retention.
- [ ] C. Keeping everything forever improves both investigation and privacy.
- [ ] D. A minimal, separated audit record can hold operation identity, policy decision, safe evidence references, error category, and responsible roles.
- [ ] E. Sensitive payloads should be stored in the audit record by default.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Three readings.
- B: Stated.
- C: It makes investigation easier and privacy risk worse.
- D: Stated.
- E: Only when justified and protected.

**Source:** Retention is a lifecycle

## MA-ch14.36

Check each statement that is true about why consultation and consent cannot be handed to Claude. Each statement is worth 1 point (5 points total).

- [ ] A. The operational version of the argument needs no position on machine minds.
- [ ] B. A reply Claude generates in the voice of an affected student is not a statement by that student.
- [ ] C. Consent is something a person gives.
- [ ] D. You must accept the philosophical argument from Irreducibly Human to follow the chapter.
- [ ] E. If Claude writes a thorough enough reply, the consultation is complete.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: The chapter says you do not need to.
- E: Someone still has to ask the actual person, hear the answer, and stay reachable.

**Source:** Consultation and recourse are people's work

## MA-ch14.37

Check each statement that is true about designing consultation. Each statement is worth 1 point (5 points total).

- [ ] A. Decide who is affected directly, who maintains the surrounding work, who has relevant domain knowledge, and who is routinely missing from design decisions.
- [ ] B. One convenient person can stand in for every stakeholder.
- [ ] C. Participation should be voluntary where appropriate.
- [ ] D. The team should explain what will be recorded, how it will be used, and whether declining has consequences.
- [ ] E. Consultation counts only if the answer could have changed the purpose, boundaries, retention, or the decision to automate.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Stated.
- B: Do not ask one convenient person to do so.
- C: Stated.
- D: Stated.
- E: Otherwise it is theater.

**Source:** Design consultation that can change the project

## MA-ch14.38

Check each statement that is true about preparing and asking consultation questions. Each statement is worth 1 point (5 points total).

- [ ] A. "Does this helpful tool sound good?" solicits reassurance.
- [ ] B. Better questions ask what outcome would be unacceptable and what would make the person withdraw support.
- [ ] C. Promise each person that every request will be adopted.
- [ ] D. Claude's plain-language explanation can be shared without checking it against the real system.
- [ ] E. If the team asks only how to make a predetermined deployment more acceptable, participation becomes theater.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Stated.
- B: Stated.
- C: Do not promise that; explain how conflicts and decisions will be recorded.
- D: A human must check it first.
- E: Stated.

**Source:** Design consultation that can change the project

## MA-ch14.39

Check each statement that is true about recourse as a system path. Each statement is worth 1 point (5 points total).

- [ ] A. An incident contact field often becomes an inbox nobody owns.
- [ ] B. A reporter must supply complete private details so the team can investigate.
- [ ] C. A triage owner and escalation route are unnecessary when the first contact is a named person.
- [ ] D. An email address in the incident contact field is a complete recourse path.
- [ ] E. Response times should be stated for every report regardless of the team's capacity.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Stated.
- B: A reporter should not be forced to expose more private data.
- C: Escalation is needed when the first contact cannot resolve the issue.
- D: The whole path must be built.
- E: State them only when the team can meet them.

**Source:** Recourse is a system path, not an email address

## MA-ch14.40

Check each statement that is true about remedies for different harms. Each statement is worth 1 point (5 points total).

- [ ] A. Correcting a displayed summary does not repair a decision already made from it.
- [ ] B. Removing personal data from the active store does not recall a public copy.
- [ ] C. Explaining a model's reasoning does not restore an opportunity denied to someone.
- [ ] D. Ask the affected person what meaningful correction looks like, while recognizing that institutional constraints may require additional decision makers.
- [ ] E. A single remedy, correcting the record, serves every kind of harm.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: Different harms need different remedies.

**Source:** Recourse is a system path, not an email address

## MA-ch14.41

Check each statement that is true about the five-question test of a recourse route. Each statement is worth 1 point (5 points total).

- [ ] A. The test asks whether a person can challenge a result.
- [ ] B. The test asks whether a person can obtain an explanation appropriate to the decision.
- [ ] C. The test asks whether a person can see downstream copies updated.
- [ ] D. The test asks whether a person can appeal beyond the original owner.
- [ ] E. The test asks whether the affected person can debate the model until it changes its output.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: First question.
- B: Second question.
- C: Fourth question.
- D: Fifth question.
- E: The affected person should not have to debate a model.

**Source:** Recourse is a system path, not an email address

## MA-ch14.42

Check each statement that is true about the worked incident rehearsal. Each statement is worth 1 point (5 points total).

- [ ] A. It uses a labeled fixture in which a course-note agent publishes a summary stating the wrong assignment deadline.
- [ ] B. It is a simulated response sequence, not a claim that an actual incident occurred.
- [ ] C. The harm mechanism is a privacy exposure of student work.
- [ ] D. A successful rehearsal proves people trust the route.
- [ ] E. The rehearsal may include invented stakeholder testimony if it is realistic.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: The mechanism is reliance on a wrong deadline.
- D: A rehearsal tests the route and does not prove trust.
- E: Do not invent testimony, distress, permission, or repair.

**Source:** Worked incident rehearsal

## MA-ch14.43

Check each statement that is true about what the incident investigation found. Each statement is worth 1 point (5 points total).

- [ ] A. The citation audit checked whether a citation string existed.
- [ ] B. The citation audit checked whether the cited passage entailed the deadline.
- [ ] C. The mitigation did not address the harm.
- [ ] D. The incident reopened the evaluation line of a register that was written before the system shipped.
- [ ] E. The register was structurally incomplete before the incident.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Stated.
- B: It did not; that is the gap the investigation found.
- C: Stated.
- D: Design before implementation is not a freeze.
- E: It was structurally ready for review.

**Source:** Worked incident rehearsal

## MA-ch14.44

Check each statement that is true about the before-to-after revisions in the incident table. Each statement is worth 1 point (5 points total).

- [ ] A. "Citation audit" became a support check for consequential claims.
- [ ] B. A generic project owner became a named content owner and backup.
- [ ] C. An implicit external write remained implicit because the approver field already covered it.
- [ ] D. "Correction means edit" became deleting every copy everywhere.
- [ ] E. "Contact receives report" was kept because the response sequence was adequate.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: First row.
- B: Second row.
- C: It became an explicit publication approval.
- D: It became a bounded copy inventory and limitation.
- E: It became acknowledgment, triage, escalation, and recovery.

**Source:** Worked incident rehearsal

## MA-ch14.45

Check each statement that is true about the three variants that test the incident route further. Each statement is worth 1 point (5 points total).

- [ ] A. If the student compared the summary with an outdated schedule, a respectful route still acknowledges, investigates, and explains the evidence.
- [ ] B. Contestability means a person can trigger genuine reconsideration, not that every challenge decides the outcome.
- [ ] C. If the incident contact is unavailable, the backup pauses publication under delegated authority after the declared acknowledgment threshold and records why.
- [ ] D. If no backup exists, the agent should nominate itself as the responsible party.
- [ ] E. A review of every deadline claim counts as a control if it reads well, even when the team cannot sustain it.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: First variant.
- B: Stated.
- C: Second variant.
- D: That is an unresolved dependency; do not fill it that way.
- E: A mitigation that cannot be maintained is not a control.

**Source:** Worked incident rehearsal

## MA-ch14.46

Check each statement that is true about deferral and narrowing scope. Each statement is worth 1 point (5 points total).

- [ ] A. Defer when the purpose is contested or no authorized owner will accept the decision.
- [ ] B. Narrowing scope, such as shortening retention, signals that the project failed.
- [ ] C. Automation is the default destination of every workflow.
- [ ] D. If a workflow is technically feasible, proceed even when the benefit is marginal and the cost falls on people who cannot contest it.
- [ ] E. A register that can only say "go" is useful because it saves review time.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Two of the listed conditions.
- B: Narrowing is often productive.
- C: It is not the default.
- D: Feasibility is not a reason to proceed.
- E: It is a rubber stamp with a form attached.

**Source:** When deferral is the responsible output

## MA-ch14.47

Check each statement that correctly pairs a situation with one of the chapter's governance failure patterns. Each statement is worth 1 point (5 points total).

- [ ] A. Every field holds a generic role and nobody has accepted operational ownership: complete form, absent responsibility.
- [ ] B. A pilot has no end date and keeps accumulating data and effects: permanent pilot.
- [ ] C. A citation audit is offered for a privacy-retention harm: unobservable threshold.
- [ ] D. Model-generated stakeholder reactions presented as feedback from people: compliance theater.
- [ ] E. A threshold reading "when quality falls": consent by simulation.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated pattern.
- B: Stated pattern.
- C: That is mitigation mismatch.
- D: That is consent by simulation.
- E: That is an unobservable threshold.

**Source:** Governance failure patterns

## MA-ch14.48

Check each statement that is true about the Build It step. Each statement is worth 1 point (5 points total).

- [ ] A. Write your own assess from the contract in the gate before opening the reference solution.
- [ ] B. Trace one successful case by hand, marking the input boundary, the transformation, and the returned result.
- [ ] C. For each of the lesson's six tests, write down which wrong program it exists to catch.
- [ ] D. When comparing with the reference, name a difference in line count or style.
- [ ] E. Build It happens after Claude has implemented the validator.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Name a difference in behavior.
- E: It comes before Claude touches anything.

**Source:** Build It, Use It, Ship It

## MA-ch14.49

Check each statement that is true about the first pass of Use It, the validator. Each statement is worth 1 point (5 points total).

- [ ] A. Give Claude the gate (the contract and your test list, including your two added tests), not your implementation.
- [ ] B. Run your tests on what Claude returns, yourself.
- [ ] C. A failing test is often a gap in your gate, which Claude cannot see because it has only what you wrote.
- [ ] D. Ask Claude to propose a deliberately wrong version that still passes your tests, and check by hand whether it does.
- [ ] E. If the wrong version passes your tests, your tests were strong.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: Then your list was too weak.

**Source:** Build It, Use It, Ship It

## MA-ch14.50

Check each statement that is true about the second pass of Use It, the register. Each statement is worth 1 point (5 points total).

- [ ] A. Read Claude's draft as the author of the gate, asking for each line which of the five decisions it answers and whether there is a person's name.
- [ ] B. The challenger prompt tells Claude not to rewrite the entry.
- [ ] C. The challenger prompt asks for thresholds with no observable signal and for mitigations that do not address the named harm.
- [ ] D. A finding you cannot locate in the text is still useful evidence of a weak line.
- [ ] E. Asking Claude to play an affected student tells you what a real student thinks.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Withholding the rewrite is deliberate.
- C: Stated items.
- D: It is a fluent guess.
- E: It only tests whether your explanation is clear.

**Source:** Build It, Use It, Ship It

## MA-ch14.51

Check each statement that is true about the Ship It register entry. Each statement is worth 1 point (5 points total).

- [ ] A. Start with the actual capstone workflow, not a generic AI policy paragraph.
- [ ] B. Name the bounded purpose and non-purpose.
- [ ] C. Assign a mitigation owner who has pause authority.
- [ ] D. Record unresolved authority rather than assigning it fictionally.
- [ ] E. If consultation is pending, leave it out so the workflow can proceed unconstrained.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: Say so and constrain the workflow accordingly.

**Source:** Build It, Use It, Ship It

## MA-ch14.52

Check each statement that is true about the decision note and the register as a control plane. Each statement is worth 1 point (5 points total).

- [ ] A. The decision note records what Claude proposed, what context a person added or corrected, the supporting evidence, whose interests it serves or disadvantages, and the named human recommendation.
- [ ] B. Highlight any sentence that merely repeats Claude, because repetition is not review.
- [ ] C. Memory defines action authority, and tool permissions record data lineage and lifetime.
- [ ] D. If updating the register changes nothing the system does, it is still governance.
- [ ] E. The register replaces the earlier layers rather than drawing on them.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Tool permissions define action authority; memory records lineage and lifetime.
- D: Then it is only documentation.
- E: It draws on every previous layer.

**Source:** Build It, Use It, Ship It

## MA-ch14.53

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. The template has the lines Checked, How, Not checked, Not claiming, and Signed or withheld.
- [ ] B. "Not checked" is the line an AI-written sign-off never includes, because the system that wrote it has no record of what you did not do.
- [ ] C. The approver field and the sign-off state the same thing.
- [ ] D. A sign-off means something only if withholding is a real option.
- [ ] E. If the evidence does not support signing, the right action is to find words that make the form pass.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The chapter's template.
- B: Stated.
- C: The approver names who may approve; the sign-off states what the register has earned.
- D: Stated.
- E: Narrow or defer the workflow instead.

**Source:** Build It, Use It, Ship It

## MA-ch14.54

Check each statement that is true about the driver's seat table. Each statement is worth 1 point (5 points total).

- [ ] A. You replace every group or role in Claude's drafted entries with a named person who accepted it.
- [ ] B. You build your own baseline validator first, then run your tests on Claude's version.
- [ ] C. You decide which candidate harms Claude lists are real here, and you talk to the people.
- [ ] D. You choose the threshold, who may pause, and who absorbs the cost of pausing.
- [ ] E. Claude hears the affected person, decides the appeal, and corrects the record.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: First row.
- B: Second row.
- C: Third row.
- D: Fourth row.
- E: Claude assembles the contested output; you hear, decide, and correct.

**Source:** The driver's seat

## MA-ch14.55

Check each statement that is true about verification and reflection. Each statement is worth 1 point (5 points total).

- [ ] A. Verification begins with claims small enough to test.
- [ ] B. A passing test suite establishes only the tested behavior, not universal reliability or permission to act.
- [ ] C. "Approved" in a register requires a person who did the approving.
- [ ] D. The most useful reflection is a general resolution to be more careful with AI.
- [ ] E. Explain a passing case by first reading Claude's explanation.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: The useful reflection is a concrete local habit.
- E: Explain it without reading Claude's explanation.

**Source:** Verify and reflect

## MA-ch14.56

Check each statement that is true about the chapter's Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. They are ungraded practice.
- [ ] B. The paired lesson's knowledge check is used after the practice and before viewing its explanations, and it remains self-review.
- [ ] C. The knowledge check is a separate graded assignment.
- [ ] D. Assessment 1 asks you to run assess({}) first and predict afterward.
- [ ] E. You may record an approval you expect to receive as though it had been given.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: It remains self-review.
- D: It asks you to predict, then run.
- E: Do not fabricate stakeholders or approvals.

**Source:** Assessments - ungraded practice

## MA-ch14.57

Check each statement that is true about the chapter's summary of what the three jobs look like at this scale. Each statement is worth 1 point (5 points total).

- [ ] A. Conducted: you wrote the five decisions and the wrong validator your tests had to catch before Claude drafted anything.
- [ ] B. Checked: you found the weak line in a complete register and named who bears each kind of error.
- [ ] C. Drove: you handed Claude the drafting and the implementation, kept the relationships, the consent, and the choice to ship or defer, and signed or withheld.
- [ ] D. Drove: you handed Claude the relationships and consent and kept only the drafting.
- [ ] E. You can now read an AI-use register as a certificate.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: You kept the relationships and consent.
- E: You can read it as a set of operational claims rather than a certificate.

**Source:** Capabilities summary

## MA-ch14.58

Check each statement that is true about the Anthropics section. Each statement is worth 1 point (5 points total).

- [ ] A. It points to Anthropic's Claude Code security guidance as input for analyzing access boundaries, untrusted inputs, and safe operation.
- [ ] B. Connect a relevant recommendation to a named owner, monitoring signal, and incident response rather than copying general security prose.
- [ ] C. The primary link was checked for the approved research packet on 2026-09-06.
- [ ] D. Applicable Northeastern policies determine institutional use.
- [ ] E. The register is a claim about Anthropic's internal governance.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: It is not such a claim, nor a legal compliance tool.

**Source:** Anthropics

## MA-ch14.59

Check each statement that is true about the Computational Skepticism section. Each statement is worth 1 point (5 points total).

- [ ] A. Responsibility for a failure distributes across parties whose choices were each necessary and none sufficient.
- [ ] B. The parties include the reporting student, the content owner, the maker of the drafting tool, the model provider, and the institution whose schedule is the source of truth.
- [ ] C. The diagnostic concludes that the content owner alone caused the incident.
- [ ] D. The governance-counterfactual question asks which party deserves the most blame.
- [ ] E. Adding a sentence to the register is the same kind of change as an action someone takes.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The diagnostic.
- B: Stated list.
- C: No single party's choice was sufficient.
- D: It asks what change to the register, made before the incident, would have prevented it.
- E: The question asks which of the two the change is.

**Source:** Computational Skepticism

## MA-ch14.60

Check each statement that is true about the three-cell test in the Conducting AI section. Each statement is worth 1 point (5 points total).

- [ ] A. It borrows Suchman's three legitimacies, an adaptation by the book's author and not Suchman's own.
- [ ] B. Pragmatic: does it serve the people it is for? A fluent draft usually passes.
- [ ] C. Moral: whose standards would acting on it have to survive, and who would have to answer for it?
- [ ] D. Cognitive: do you trust the sentence because you can account for it, with these facts verified in these ways, or because it reads well?
- [ ] E. Fluent output supplies the grounds for cognitive trust.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Stated.
- D: Stated.
- E: It supplies the appearance of that trust without its grounds.

**Source:** Conducting AI

## MA-ch14.61

Check each statement that is true about the Irreducibly Human note. Each statement is worth 1 point (5 points total).

- [ ] A. An institution teaches what it actually rewards, not what it nominally teaches.
- [ ] B. The book's example is medical training, where environments rewarding efficiency erode the empathy their curricula ask for.
- [ ] C. AI should draft plain-language explanations, suggest questions, and organize authorized, sanitized feedback.
- [ ] D. AI should obtain permission where required and remain reachable for correction.
- [ ] E. If shipping is rewarded and listening is not, the register's stated values decide what the team does.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The diagnostic.
- B: Stated.
- C: Stated.
- D: Those are human responsibilities.
- E: The team does what is rewarded.

**Source:** Irreducibly Human

## MA-ch14.62

Check each statement that is true about the forward bridge to Chapter 15. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 15 asks whether the team's parts form one defensible system.
- [ ] B. The capstone succeeds only when another person can reproduce its central result, observe a controlled failure, and inspect recovery.
- [ ] C. The sign-off is retired once the capstone starts, so only the register is carried forward.
- [ ] D. The capstone also requires that another person can understand why the accountable owner chose to ship, narrow, defer, or stop.
- [ ] E. A green validator is enough for the capstone to succeed.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Stated.
- B: Stated.
- C: Carry the register forward with its sign-off or with your reason for withholding it.
- D: Stated.
- E: The capstone needs reproduction, a controlled failure, recovery, and an explained choice.

**Source:** Forward bridge
