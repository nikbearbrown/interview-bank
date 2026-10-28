# Chapter 14: Governance and ethics

## MA-ch14.1

A team keeps an AI-use register for an LLM workflow. Every required field is filled: owner is "project team", incident contact is "project owner", evaluation is "citation audit". A script that checks only that each field is non-empty reports the record as ready for human review. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the owner is a group, it is unclear who can pause the workflow when it causes harm.
- [ ] B. A green completeness check is sufficient evidence that the workflow complies with applicable regulation.
- [ ] C. A record can be structurally complete while no individual has accepted responsibility for the workflow.
- [ ] D. Presence checks still have value because they make omissions visible.
- [ ] E. A non-empty check on the owner field verifies that the named owner has agreed to the role.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Pause authority attaches to a person or a defined role-holder, not to a collective label.
- B: Compliance is a legal and institutional determination; a format check cannot make it.
- C: Filling a field with a group or role label satisfies a presence check without assigning any person the work.
- D: A required field left blank is an unambiguous gap; surfacing it costs nothing and prevents silent omissions.
- E: A script can see that text exists; it cannot see whether anyone accepted anything.

**Source:** Opening: a complete register is not a responsible team

## MA-ch14.2

A manager asks an LLM assistant to draft a risk register for a new customer-support automation. In seconds it returns an owner, an alerting threshold, a retention period and a paragraph on risks, all fluent and plausible. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the assistant produced the register, it remains answerable for the workflow after the conversation ends.
- [ ] B. The assistant has no first-hand knowledge of the people the automation will affect.
- [ ] C. A fluent, internally consistent draft is evidence that its proposed threshold is one the organization can actually act on.
- [ ] D. Writing a person's name into the owner field makes that person the accountable owner.
- [ ] E. The assistant can produce a useful first draft quickly.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The assistant holds no ongoing duty or channel; responsibility stays with the people and organization that deploy the system.
- B: It only sees what was put in the conversation, so its picture of affected people is inferred, not observed.
- C: Fluency says nothing about whether staffing, tooling and authority exist to respond when the threshold trips.
- D: Accountability exists only when the person accepts the role; the draft cannot create that acceptance.
- E: Drafting structured text from a description is something language models do well.

**Source:** Opening: what Claude can and cannot do in a governance register

## MA-ch14.3

A governance validator returns one of three statuses: "incomplete" (fields missing), "review-required" (an issue was flagged for a person) and "ready-for-human-review" (no issues found). A record gets "ready-for-human-review". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The status "review-required" routes the decision to a person instead of resolving it automatically.
- [ ] B. A human has already reviewed the record.
- [ ] C. The record cleared the validator's structural checks.
- [ ] D. Everyone whose data is processed has consented.
- [ ] E. The workflow has been approved.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: When the machine cannot decide, the conservative design hands the question to a human.
- B: The status says the record is ready to be reviewed, not that review happened.
- C: That is exactly what the status reports and nothing more.
- D: Consent is given by individuals; no field-presence check can establish it.
- E: Approval is an act by an authorized person on a specific proposal; a script's output is not that act.

**Source:** Teardown of the validator: what a status means

## MA-ch14.4

A department head lists Dana as the "owner" of an LLM triage workflow in a spreadsheet and never tells her. Dana has no authority to disable the workflow and no time allocated to monitor it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An owner is accountable only for the initial launch; after that the workflow belongs to whoever operates it day to day.
- [ ] B. An owner who cannot stop the workflow holds a label rather than control.
- [ ] C. Being the person who wrote the original code makes someone the owner of the workflow as a continuing system.
- [ ] D. Assigning owner, approver and incident contact all to one person is the best way to avoid gaps.
- [ ] E. Listing Dana's name does not by itself create accountability.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Drift, new data and new uses appear after deployment, and someone must still answer for the workflow as it runs.
- B: Accountability without authority to pause or change the system cannot be exercised when it matters.
- C: Authorship of the initial code says nothing about ongoing monitoring, change decisions or incident response.
- D: It removes independent review and creates a single point of failure; it often just completes the form.
- E: Responsibility has to be accepted by the person; being named in a cell is not acceptance.

**Source:** Who decided? Five choices that exist before the form does

## MA-ch14.5

A team needs five governance decisions for a new LLM workflow: who owns it, which signal triggers a response, how long data is kept, who was consulted, and how an affected person reaches a human. They ask an assistant to fill in a template first and plan to "review it afterwards". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A decision no one has accepted should be recorded as unresolved, with the workflow constrained until someone accepts it.
- [ ] B. The team should leave thresholds and owners to emerge from the template because the form structure forces good decisions.
- [ ] C. A fluent draft is neutral and does not influence how reviewers decide.
- [ ] D. An unresolved owner is acceptable if the workflow launches at full scope, since ownership can be settled later.
- [ ] E. A form filled before the decisions are made records the shape of a decision rather than a decision.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Constraints such as draft-only output, synthetic data or no external writes keep exposure bounded while authority is missing.
- B: Structure prompts questions; it does not supply the power or evidence to answer them.
- C: Reviewers tend to adjust a supplied draft rather than generate their own answer, so a draft shapes the outcome.
- D: Launching at full scope with no accountable person means harm could occur with nobody authorized to respond.
- E: The fields can be populated with plausible text regardless of whether anyone has actually decided anything.

**Source:** Who decided? Five choices that exist before the form does

## MA-ch14.6

A team is rewriting vague monitoring promises into thresholds. A threshold is useful for governance when a stranger, reading only the record, could tell whether it fired. Check each statement that would qualify as such a threshold. Each statement is worth 1 point (5 points total).

- [ ] A. "Any single confirmed disclosure of personal data triggers an immediate stop and an incident review."
- [ ] B. "Quality will be monitored regularly."
- [ ] C. "If a weekly random sample of 100 outputs contains more than 2 unsupported claims, publication pauses and the content owner investigates."
- [ ] D. "The team will remain responsive to concerns raised by users."
- [ ] E. "We will intervene when risk becomes unacceptable."

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A confirmed-event trigger is observable and has a defined response.
- B: It names no signal, measurement or trigger, so nobody could tell whether it fired.
- C: It specifies a signal, a measurement procedure, a numeric trigger, a response and a responsible role.
- D: It states an attitude, not a condition and a response.
- E: "Unacceptable" is undefined and there is no observable condition to check.

**Source:** Owners, thresholds, and bounded responses

## MA-ch14.7

A team monitors an LLM drafting tool that produced 20,000 outputs last month. Its dashboard shows a 99.5% pass rate on an automated quality check. Review of the 100 failing outputs found that 2 of them exposed customers' personal data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reducing the failure rate from 0.5% to 0.4% guarantees fewer personal-data disclosures.
- [ ] B. 100 outputs failed the check.
- [ ] C. The pass rate already accounts for severity, so the two disclosures need no separate handling.
- [ ] D. A 99.5% aggregate pass rate can coexist with severe incidents.
- [ ] E. Severe harm classes should be handled only by trend thresholds, since a single event is statistically meaningless.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The aggregate can fall while the rare severe category stays the same or grows.
- B: 0.5% of 20,000 is 100.
- C: A pass rate counts failures; it does not weight them by harm.
- D: Averages weight every failure equally, so rare high-severity events disappear into the denominator.
- E: One severe event can be unacceptable on its own, which is why stop rules respond to the first occurrence.

**Source:** Owners, thresholds, and bounded responses

## MA-ch14.8

An incident owner has been named for an LLM-powered publishing pipeline. Managers have told the team that delays will count against its quarterly goals and that shipping on time is rewarded. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If incentives punish delay, a nominal pause authority is unlikely to be used.
- [ ] B. The owner needs explicit authority to pause the pipeline for the role to have effect.
- [ ] C. A written policy that says the owner may pause the pipeline is enough regardless of incentives.
- [ ] D. The cost of a pause should fall on the individual who triggers it, so that they weigh the decision carefully.
- [ ] E. How staff are evaluated is an HR matter that a governance record need not address.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: People respond to what is rewarded; unused authority is governance on paper only.
- B: A nominal owner who must ask permission to stop cannot respond at the speed harm requires.
- C: Policy that conflicts with how performance is judged is routinely ignored in practice.
- D: Making the individual absorb the cost discourages use of that power; the organization should absorb it.
- E: How people are rewarded determines whether controls are used, so it is part of whether governance works.

**Source:** Owners, thresholds, and bounded responses

## MA-ch14.9

The designated incident contact for an LLM service is on leave. An alert about a possible data exposure has gone unacknowledged for six hours; the declared acknowledgment window is two hours. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Waiting for the primary contact to return is acceptable if the exposure may be ongoing.
- [ ] B. The AI agent running the service can close the gap by nominating itself as the responsible party.
- [ ] C. The system halting its own work while the alert is open is a reasonable safe default, as long as a person remains responsible for the outcome.
- [ ] D. A documented backup with delegated pause authority should receive the alert and act.
- [ ] E. If no backup exists, the team can treat the gap as acceptable because the contact will eventually return.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Continued exposure means harm accrues while the response waits.
- B: An agent is not an accountable person or organization; self-nomination assigns nothing.
- C: Stopping is low-risk and reversible; responsibility still has to sit with an authorized human.
- D: A backup path exists precisely so that response does not depend on one person's availability.
- E: A missing escalation path is a defect to fix; harm can accrue while waiting for one person.

**Source:** Worked incident rehearsal

## MA-ch14.10

A validator checks the retention period with this function:

```python
def valid_days(d):
    return isinstance(d, int) and d >= 0
```

Check each statement that is true about its behavior in Python. Each statement is worth 1 point (5 points total).

- [ ] A. valid_days(30.0) returns True.
- [ ] B. valid_days(0) returns False.
- [ ] C. bool is not a subclass of int in Python.
- [ ] D. valid_days(True) returns True.
- [ ] E. Replacing isinstance(d, int) with type(d) is int would make valid_days(True) return False.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: 30.0 is a float, not an int instance, so the isinstance test fails.
- B: Zero is an int and is not negative, so the function returns True.
- C: bool derives from int, which is why True behaves as 1 in arithmetic.
- D: bool is a subclass of int in Python, so isinstance(True, int) is True and True >= 0.
- E: type(True) is bool, which is not int, so an exact type test rejects Booleans.

**Source:** Tear down the validator

## MA-ch14.11

A validator decides which required fields are missing with `missing = [f for f in FIELDS if not record.get(f)]`. A record supplies every field, including `retention_days: 0` as a deliberate design intent of no retention after processing, and `data_classes: []`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. This check distinguishes a legitimate zero from an absent value.
- [ ] B. retention_days is reported as missing.
- [ ] C. A key that is absent from the record is not reported as missing, because get returns None and None is ignored.
- [ ] D. A field containing only the string " " (a single space) is reported as missing.
- [ ] E. The empty data_classes list is reported as missing.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Falsiness treats both the same; a test such as `value is None` or a key-presence test is needed to separate them.
- B: 0 is falsy in Python, so `not 0` is True and the intended value is treated as absent.
- C: record.get returns None for an absent key and `not None` is True, so the field is reported.
- D: A non-empty string is truthy even when it contains only whitespace.
- E: An empty list is falsy, which here happens to be the desired behavior.

**Source:** Tear down the validator

## MA-ch14.12

A validator receives `data_classes` and runs `set(classes) - {"public", "synthetic", "internal"}`; any leftover element adds the issue "sensitive or unknown data review". It has no type check. A caller passes the bare string `"public"` instead of the list `["public"]`. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The validator reports no issues because "public" is an allowed label.
- [ ] B. An explicit check that the value is a list of strings would reject the bare string with a clear error.
- [ ] C. A string and a list of labels are interchangeable inputs for this comparison.
- [ ] D. With the same case-sensitive allowlist, the input `["Public"]` would also be flagged.
- [ ] E. The validator flags the record for review.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The allowed-label comparison never sees the whole string; it sees p, u, b, l, i, c separately.
- B: Failing fast on the wrong shape is clearer than a misleading downstream review flag.
- C: Both are iterable, but they iterate different things, so results differ in meaning.
- D: "Public" is not equal to "public", so the exact comparison leaves one unmatched element.
- E: Iterating a string yields single characters, none of which equals an allowed label, so the set difference is non-empty.

**Source:** Tear down the validator

## MA-ch14.13

A team debates two designs for checking data labels. Design 1 keeps a denylist of known sensitive labels (for example "medical", "financial") and raises a flag on a match. Design 2 keeps an allowlist of approved labels and sends anything else to human review. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A flag from Design 2 proves the data is sensitive.
- [ ] B. Design 2 establishes that data labeled "internal" is safe to use in the proposed workflow.
- [ ] C. Design 1 will miss a sensitive category that nobody thought to put on the list.
- [ ] D. A case-sensitive allowlist will silently accept 'Public', which is a safety gap.
- [ ] E. Design 2 routes unknown labels to a person, which is the more conservative default.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It only shows that this label was not recognized; the data may be perfectly harmless.
- B: A label being on the allowlist says nothing about whether the specific use of that data is appropriate.
- C: A denylist only catches what it enumerates.
- D: An exact comparison fails for 'Public', so the value is routed to review rather than accepted.
- E: When the machine cannot classify, the safe fallback is to ask a human.

**Source:** Tear down the validator

## MA-ch14.14

A designer wants an automated check that rejects governance records whose owner, purpose or evaluation lines are "bad". One proposal is a list of banned phrases such as "everyone", "team", "looks fine". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If an LLM judge scores an owner line as adequate, the named person no longer needs to confirm the role.
- [ ] B. A narrow validator that claims only what it checks is more honest than one implying it assesses quality.
- [ ] C. A string-matching validator can reliably decide whether an evaluation line describes an adequate test.
- [ ] D. Leaving the adequacy judgment to a human reviewer is a legitimate division of labor with the validator.
- [ ] E. A phrase blacklist is easy to evade with minor rewording.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: A model's score cannot substitute for the person accepting the role.
- B: Overstated validators encourage readers to trust status labels beyond what was tested.
- C: Adequacy depends on the system and the harm; strings cannot encode that.
- D: The machine refuses what it can refuse exactly; people judge whether a line is true and sufficient.
- E: "The whole group" or "seems okay" passes while saying the same thing.

**Source:** Tear down the validator

## MA-ch14.15

A validator contains `if record.get("external_write"): issues.append("external action approval")`. Check each statement that is true about this check. Each statement is worth 1 point (5 points total).

- [ ] A. A record where external_write is False or absent adds no issue.
- [ ] B. It identifies which external system will be written to.
- [ ] C. A record where external_write is the string "no" would still trigger the flag.
- [ ] D. It confirms that someone approved the external action.
- [ ] E. It flags a condition that must be handled by another control.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A falsy value fails the condition.
- B: The flag is a boolean-style value and carries no target information.
- C: Non-empty strings are truthy in Python regardless of their meaning.
- D: It only marks that approval is needed; it never looks for evidence of approval.
- E: The flag is a routing signal for an approval step, not the approval itself.

**Source:** Tear down the validator

## MA-ch14.16

A governance validator accepts any record whose fields are non-empty and well-formed. This record gets "ready-for-human-review": owner "everyone", purpose "help", data classes ["public"], retention_days 99999, approver "manager", evaluation "looks fine", incident contact "team". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A human reviewer must question what each line means.
- [ ] B. Adding a policy maximum for retention to the validator would catch that value without needing human judgment.
- [ ] C. A retention period of 99999 days (roughly 274 years) deserves scrutiny regardless of the validator's verdict.
- [ ] D. The record is a counterexample to reading the status as evidence of adequate governance.
- [ ] E. The validator has a defect, because it should have rejected this record.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The vague lines can only be tested against the real world by a person.
- B: A numeric range is something a validator can enforce exactly.
- C: It is effectively unlimited retention, which defeats the purpose of stating a period.
- D: A status that lets such a record through cannot certify quality.
- E: Relative to its narrow contract (presence and shape) it behaved correctly.

**Source:** Complete, reviewable, and still weak

## MA-ch14.17

A developer writes a test suite for a retention validator before asking an assistant to implement it. Two deliberately wrong implementations exist: V1 accepts any value for which isinstance(d, int) is true; V2 treats any falsy value as missing, so 0 is rejected as missing. The correct implementation accepts 0, rejects True, and rejects negative numbers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A suite containing only the normal-success case and the empty-record case is enough to catch both wrong versions.
- [ ] B. A test that expects retention_days=0 to be accepted distinguishes the correct version from V2.
- [ ] C. If the suite passes on an implementation, that implementation is correct for all inputs.
- [ ] D. Checking the suite against deliberately wrong implementations is unnecessary if the correct implementation passes.
- [ ] E. A test that expects retention_days=True to be rejected distinguishes the correct version from V1.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Both wrong versions still pass those two cases.
- B: V2 reports 0 as missing and would fail that test.
- C: Tests demonstrate only the behavior they exercise.
- D: A suite can pass the correct version and still pass wrong ones; only trying wrong versions shows whether it can tell them apart.
- E: V1 accepts True because bool is a subclass of int.

**Source:** Build It, Use It, Ship It

## MA-ch14.18

A developer asks an LLM assistant to write both a validator and its tests, then runs the tests and sees all pass. Separately, a colleague wrote tests first from a written specification and then asked the assistant to write only the implementation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tests and implementation produced by the same model can share the same misreading of the specification.
- [ ] B. If the assistant cannot produce a wrong version that passes the tests, the suite is proven complete.
- [ ] C. A person who never writes a baseline version can audit the assistant's version just as well as one who did.
- [ ] D. A passing result in the first setup is stronger evidence than in the second, because the tests were consistent with the code.
- [ ] E. Tests written by a person before seeing the implementation capture that person's intent independently.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The model's error appears on both sides, so agreement between them is weak evidence.
- B: Failure to find a counterexample is not proof that none exists.
- C: Building a baseline first gives the person a concrete reference for spotting differences in behavior.
- D: Consistency between two products of one source is not independent confirmation.
- E: They are not shaped by what the implementation happens to do.

**Source:** Build It, Use It, Ship It

## MA-ch14.19

A reviewer is deciding how to word claims in a validation write-up so that each claim is no stronger than the evidence behind it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A team that sends a labeled test report to the incident contact and observes an acknowledgment within the stated time has evidence the route works.
- [ ] B. "The validator reported that all seven fields were present and well shaped" is a precise description of a script run that did exactly that.
- [ ] C. Inspecting the stores you control supports claims about backups that a vendor operates.
- [ ] D. A passing test suite on the validator is permission to apply the workflow to cases the tests never exercised.
- [ ] E. Reading a provider's documentation that says logs are deleted after 30 days supports "we verified deletion at the provider".

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The route was exercised, not merely listed.
- B: The verb matches what the script did: reported, not confirmed.
- C: Evidence covers only what was actually examined; vendor-operated copies remain unexamined.
- D: Test coverage bounds the claim; untested cases remain unknown.
- E: Documentation is a claim by the provider; verifying requires inspecting the store or independent evidence.

**Source:** Complete, reviewable, and still weak

## MA-ch14.20

A summarization assistant was approved for condensing public course notes. Six months later the same assistant is pointed at student-submitted essays. The register's purpose field reads "use AI". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A broad purpose statement is preferable because it permits future uses without re-review.
- [ ] B. If the model and prompt are unchanged, the risk profile is unchanged.
- [ ] C. Pointing the assistant at student essays is a use beyond the original scope that should trigger re-review.
- [ ] D. A purpose field is only decoration because the validator cannot judge it.
- [ ] E. A purpose of "use AI" fails to bound what the system may be used for.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A broad purpose excludes nothing, which is exactly why scope creep goes unnoticed.
- B: Risk depends on the data, the people and the consequences, not only on the model.
- C: Different data, different people affected and different risks need a fresh decision.
- D: The field's value is in forcing the team to state a boundary that people can later check.
- E: It excludes nothing, so no later use can be identified as out of scope.

**Source:** A register makes questions inspectable

## MA-ch14.21

A register states "retention: 30 days" for user prompts. Prompts also appear in: an application log (deleted at 30 days), a nightly backup retained for 90 days, an exported weekly report e-mailed to managers, and a third-party model provider's service logs under the provider's own terms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A prompt captured by the first nightly backup after it arrived could still exist in that backup about 90 days later.
- [ ] B. The policy is satisfied once the primary store deletes at 30 days.
- [ ] C. Deleting the prompt from the application log also removes summaries derived from it elsewhere.
- [ ] D. The declared 30 days does not show that the backup, the exported report and the provider logs are deleted at 30 days.
- [ ] E. To verify the policy, the team must list each copy and say how deletion is performed and checked.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The backup's own 90-day retention sets its lifetime regardless of the 30-day application policy.
- B: The policy is about the data, not only the primary store.
- C: Derived artifacts live in their own stores and may still reveal source content.
- D: A retention number describes the policy for one store; other copies follow their own lifecycles.
- E: Without an inventory of copies, deletion cannot be tested.

**Source:** Retention is a lifecycle

## MA-ch14.22

A design document sets `retention_days = 0` for a workflow that handles customer messages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Stating zero in the record is evidence that no copies exist.
- [ ] B. Zero can mean different things: delete immediately after the task, do not persist application data, or keep only de-identified evidence.
- [ ] C. A validator that treats falsy values as missing would incorrectly report this record as missing a field.
- [ ] D. Zero retention means a third-party model provider processes nothing, so the provider's terms are irrelevant.
- [ ] E. A validator should reject zero as invalid because data must always be kept for some period.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A stated value is a design intent; copies can exist whatever the record says.
- B: The number does not define which of those is intended, so the document needs to say.
- C: 0 is falsy, so a presence check must test for absence, not falsiness.
- D: Processing by a provider still occurs and is governed by its own terms.
- E: Zero can be a legitimate design intent; rejecting it prevents expressing a minimal-retention design.

**Source:** Retention is a lifecycle

## MA-ch14.23

A team claims that a customer's personal data was removed from their LLM application. They deleted the row from the application database. The same customer's data also fed a vector index of embeddings, a nightly summary report, a log of hashed email addresses used for matching, and a backup. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Unverified stores, such as provider systems and backups, should be listed as open rather than assumed clean.
- [ ] B. "Removed from this table" supports the claim "erased everywhere".
- [ ] C. The team can test deletion by inserting a labeled test record, running the full lifecycle, and inspecting the stores it controls.
- [ ] D. A hash of an email address can still be personal data if it can be matched against a small known set.
- [ ] E. Deleting the row does not show that derived artifacts such as embeddings and summaries are gone.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Reporting unknowns avoids turning a desired policy into a claim about systems no one inspected.
- B: The claim covers only the store inspected.
- C: An end-to-end test on marked data checks what actually happens rather than what the policy says.
- D: Hashing a guessable input is reversible by lookup; the hash can identify the person.
- E: Derived data can retain or reveal source information.

**Source:** Retention is a lifecycle

## MA-ch14.24

A team is deciding how long to keep traces of an LLM agent's actions. Option 1 keeps full prompts and outputs forever. Option 2 keeps nothing. Option 3 keeps an operation ID, the policy decision taken, references to evidence stored elsewhere, an error category, and the responsible role, with sensitive payloads kept only when justified and protected. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Audit logs are exempt from retention limits because they are used for oversight.
- [ ] B. Option 2 can make accountability and incident investigation impossible.
- [ ] C. Option 1 improves the ability to investigate incidents but enlarges privacy exposure.
- [ ] D. Full payloads should be stored by default because debugging value always outweighs privacy cost.
- [ ] E. Option 3 is inferior to Option 1 in every respect because it removes investigative detail.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Audit records are still data with a lifecycle and a risk; they need their own retention decision.
- B: With no record of what happened, causes cannot be established.
- C: More retained detail helps replay and raises the cost of any breach or misuse.
- D: Data minimization says to keep only what is needed and justified.
- E: Option 3 keeps the information needed to reconstruct decisions while cutting privacy exposure, so it is not worse in every respect.

**Source:** Retention is a lifecycle

## MA-ch14.25

Two agents each score 92% on the same 500-item evaluation set. Agent A reads public notes, writes a local draft, keeps inputs one day, and requires a person to publish. Agent B reads internal HR records, publishes directly to an external site, and keeps complete traces for a year. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equal accuracy implies equal governance needs.
- [ ] B. Agent B has a larger action surface and longer exposure window than Agent A.
- [ ] C. Both agents made 40 errors on the evaluation set.
- [ ] D. Ethical review can wait until after model selection because model score determines risk.
- [ ] E. The architectural choices of Agent A (minimal data, human publication, short retention) reduce the harm surface independent of model accuracy.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Accuracy measures output correctness under selected tests, not consequences or reversibility.
- B: Direct external publication and long retention of sensitive traces expand both.
- C: 8% of 500 is 40.
- D: Data, authority and retention choices shape harm before any score exists.
- E: These choices limit how much damage an error can do.

**Source:** Who bears the error

## MA-ch14.26

Two document summarizers are tested on the same 300 policy questions. Each makes exactly 12 deadline errors, so both score 96%. Summarizer X errs by stating a deadline its sources do not support. Summarizer Y errs by omitting the deadline when sources conflict. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Y's omissions are harmless because users can always check the source.
- [ ] B. A single accuracy figure is sufficient to choose between them.
- [ ] C. The accuracy number does not say which kind of error to prefer.
- [ ] D. Both kinds of error harm the same people, so the choice between them has no distributional effect.
- [ ] E. Both have an identical overall accuracy figure.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Omissions impose costs: delay, support requests and missed deadlines for people who do not check.
- B: It hides the type of error, which matters more than the count here.
- C: Choosing means weighing whose costs count, which is a value judgment.
- D: A wrong date harms those who rely on it; an omission harms those who must seek clarification, so the burdens differ.
- E: (300 - 12) / 300 = 96% for each.

**Source:** Who bears the error

## MA-ch14.27

A risk-scoring model is applied to two groups. Group 1 has a base rate of 50% positives and group 2 has 20%. For both groups the classifier has a true positive rate of 0.8 and a false positive rate of 0.2. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The positive predictive value (precision) for group 1 is 0.80.
- [ ] B. The precision gap indicates a computation bug in the classifier.
- [ ] C. With differing base rates, holding error rates equal across groups and also holding precision equal is generally impossible unless prediction is perfect.
- [ ] D. The two groups are flagged at the same rate.
- [ ] E. The positive predictive value for group 2 is 0.50.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Of every 100 people, 40 true positives and 10 false positives are flagged, so 40 / 50 = 0.80.
- B: It follows arithmetically from equal error rates and unequal base rates.
- C: This is a known impossibility result for fairness criteria, which follows from Bayes' rule.
- D: Group 1 is flagged at 0.50 and group 2 at 0.32 of the population.
- E: Of every 100 people, 16 true positives and 16 false positives are flagged, so 16 / 32 = 0.50.

**Source:** Who bears the error

## MA-ch14.28

A team building a scoring tool for loan applications must pick a fairness criterion. Its data scientist says "the numbers will tell us which definition is correct". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Choosing among fairness definitions is a normative decision, not only a technical one.
- [ ] B. Two parties can both report accurate statistics and still disagree about which statistic should decide fairness.
- [ ] C. The definition should be whichever the default loss function happened to encode.
- [ ] D. The decision need not be recorded, since the chosen metric speaks for itself.
- [ ] E. If the tool does not rank or allocate opportunities among people, the team should add demographic columns to its evaluation to look rigorous.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Each definition protects a different kind of equality and trades off against the others.
- B: The disagreement is about values, not about arithmetic.
- C: An implicit default is a choice made by accident; the decision should rest with an accountable party.
- D: A recorded rationale with alternatives and conditions for change is what makes the choice reviewable.
- E: Metrics should be tied to a harm mechanism that exists; invented columns add the look of rigor without meaning.

**Source:** Who bears the error

## MA-ch14.29

A risk register for an LLM-based tool lists the risk "There may be bias or privacy concerns." Another entry reads: "A student relies on a summary that states the wrong submission deadline and misses the real one." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A register with 40 generic risks is more useful than one with three concrete harm scenarios.
- [ ] B. A concrete harm entry lets reviewers ask who bears the cost and who could have prevented it.
- [ ] C. Generic risk language tells a team what to do.
- [ ] D. The second entry names an affected person, a mechanism and a consequence.
- [ ] E. The first entry is a concrete harm description.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Concreteness, not count, makes a register actionable.
- B: Specificity connects a harm to people with different roles.
- C: Without a person, mechanism or consequence it guides no specific action.
- D: Those elements allow someone to design a test and a mitigation for it.
- E: It names no person, mechanism or consequence and could be pasted into any register.

**Source:** Who bears the error

## MA-ch14.30

A company uses an LLM to screen resumes. It reports 90% overall agreement with past hiring decisions on an evaluation set built from people who were hired. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Candidates wrongly rejected bear the cost of false negatives.
- [ ] B. Whether a rejected candidate can reach a human who can change the decision is a governance question that accuracy does not capture.
- [ ] C. An overall agreement of 90% implies that errors are spread evenly across groups of applicants.
- [ ] D. An evaluation set drawn only from past hires under-represents people who were never hired.
- [ ] E. Recruiters bear part of the cost of false positives because they spend time reviewing weak candidates.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: They lose an opportunity and may never learn why.
- B: Recourse is a property of the surrounding system, not the model score.
- C: Aggregate figures say nothing about distribution across subgroups.
- D: Selecting on the outcome hides how the model treats those excluded by earlier processes.
- E: Errors have costs for the staff who must correct them.

**Source:** Who bears the error

## MA-ch14.31

A team plans to consult people affected by a new AI workflow. It decides to ask one friendly colleague to speak for all stakeholders, and to ask only how to make the planned deployment more acceptable. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Consultation is meaningful only if the answers could change the purpose, boundaries, retention or the decision to automate.
- [ ] B. Participants should be enrolled by default, with an explanation of how their answers are used given only if they ask.
- [ ] C. The team should promise that every request will be adopted.
- [ ] D. One convenient person can stand in for every stakeholder group.
- [ ] E. Asking only how to make a predetermined deployment more acceptable is participation theater.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: If nothing can change, the process is performance rather than input.
- B: Voluntary, informed participation is the basis for treating answers as input or consent.
- C: Promising what cannot be delivered erodes trust; the team should explain how decisions and conflicts will be recorded.
- D: Different groups have different stakes, and a single proxy hides the ones missing from the room.
- E: The outcome was already fixed, so affected people's views cannot matter.

**Source:** Consultation and recourse are people's work

## MA-ch14.32

A team prepares for stakeholder conversations by asking an LLM to play an affected student and answer questions about a new AI workflow. The model replies agreeably. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The model's agreeable answers are statements by the student.
- [ ] B. The record should label simulated responses as simulation and state which real consultation is still pending.
- [ ] C. The model's reaction shows what real students in this program think.
- [ ] D. Invented agreement counts as consent.
- [ ] E. Role-play can reveal unclear explanations and missing questions.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The model generates plausible text; the student said nothing.
- B: Honest labeling prevents later readers from mistaking rehearsal for evidence.
- C: It reflects patterns in training data and the prompt, not the actual views of these people.
- D: Consent is something a real person gives, knowingly.
- E: A fluent responder will expose confusing wording and obvious gaps.

**Source:** Consultation and recourse are people's work

## MA-ch14.33

A researcher drafts interview questions for people who will be affected by an automated decision tool. Check each statement that is true about which questions invite honest disagreement. Each statement is worth 1 point (5 points total).

- [ ] A. Leading questions produce stronger consent because respondents agree more often.
- [ ] B. "What would make you withdraw your support?" invites disagreement.
- [ ] C. "What information should never enter this workflow?" invites disagreement.
- [ ] D. "Does this helpful tool sound good?" mostly solicits reassurance.
- [ ] E. After interviews, actual statements should be kept separate from AI-generated summaries, with a summary returned to the participant for confirmation when appropriate.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Agreement obtained by framing is not informed consent.
- B: It surfaces conditions under which the respondent would object.
- C: It asks for boundaries and lets the respondent veto parts of the design.
- D: The wording presupposes the tool is helpful and invites agreement.
- E: This prevents a model's paraphrase from replacing what a person said.

**Source:** Consultation and recourse are people's work

## MA-ch14.34

A participant in a user study gave permission for their feedback to be used, then withdrew it. Their words were quoted in a summary, added to a vector store, used as an example in an evaluation set, and captured in a backup. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tracking which artifacts derive from a contribution makes honoring a withdrawal feasible.
- [ ] B. Consent given once is irrevocable for the project's duration.
- [ ] C. Deleting the original transcript alone does not honor the withdrawal if derived artifacts remain.
- [ ] D. An immutable backup that cannot be edited can be left out of what the participant is told.
- [ ] E. A written promise to remove the data is as good as verifying that it was removed.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Without lineage, nobody knows what to find and delete.
- B: Consent that is given can generally be withdrawn, and the process should plan for it.
- C: The quoted summary, embedding and evaluation example still carry the participant's contribution.
- D: Disclosing what could not be removed is part of honest handling of a withdrawal.
- E: A promise is an intention; verification checks outcomes.

**Source:** Consultation and recourse are people's work

## MA-ch14.35

A team asks an LLM to write a plain-language explanation of its workflow for people who will be affected: what it receives, what it produces, where a person decides, what is retained and how to report a problem. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The explanation need not mention retention, because retention is a technical detail.
- [ ] B. Shorter and simpler wording is always more accurate.
- [ ] C. The draft will be accurate about the real configuration as long as the assistant was given a one-line description of the workflow.
- [ ] D. If the draft reads smoothly, checking is unnecessary.
- [ ] E. A person who knows the real system must check the draft against it before sharing.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Retention affects people's exposure, so affected people need to know about it.
- B: Simplification can drop caveats and change meaning.
- C: A model describes what it was given; a thin description leaves gaps it fills with plausible guesses.
- D: Readability is unrelated to correctness.
- E: Smooth simplification can omit exactly the external write or retention detail an affected person needs.

**Source:** Consultation and recourse are people's work

## MA-ch14.36

During a stakeholder interview, a student says they care less about accuracy than about being quoted without context. A maintainer says an appeals channel would create unpaid support work. An instructor separates public course material from student submissions held in the same repository. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Concerns raised in interviews should be logged but should not alter the data classes or scope that were already approved.
- [ ] B. A fixed list of prepared question categories captures concerns as well as open-ended listening does.
- [ ] C. A concern not on the prepared list should be set aside as out of scope.
- [ ] D. Because public and student-submitted content sit in the same repository, they must share the same data class.
- [ ] E. The maintainer's workload concern is a governance input, since a recourse route nobody is resourced to staff will fail.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: If findings never change anything, consultation was not real input; situated concerns can change data classes, access and purpose.
- B: Prepared categories reflect only what the team already thought to ask.
- C: Unexpected concerns are often the ones that change the design.
- D: Treatment should follow the nature and sensitivity of the content, not where it happens to be stored.
- E: Capacity is part of whether a control works.

**Source:** Consultation and recourse are people's work

## MA-ch14.37

An LLM-assisted benefits-eligibility tool denies a claim. The claimant has only a general support e-mail address to contact. Check each statement that is true about effective recourse. Each statement is worth 1 point (5 points total).

- [ ] A. An e-mail address alone is a recourse path.
- [ ] B. Explaining the model's reasoning restores an opportunity that was denied.
- [ ] C. There should be a second route when the original owner is conflicted.
- [ ] D. The reviewer must have the power to change the result.
- [ ] E. A correction should reach downstream copies of the contested output.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It lacks acknowledgment, triage, authority to change the outcome and escalation.
- B: An explanation does not undo the denial; a correction would.
- C: A person cannot impartially review their own decision.
- D: A reviewer who can only explain and not correct gives no remedy.
- E: Fixing one record while copies persist leaves the harm in place.

**Source:** Consultation and recourse are people's work

## MA-ch14.38

A team reviews three kinds of harm from an AI-written summary: a displayed summary containing an error, a personal detail that already appeared in a public copy, and an opportunity that was denied on the strength of the summary. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Correcting the displayed summary does not repair a decision already made from it.
- [ ] B. A contest route is contestable only if every challenge is upheld.
- [ ] C. Removing personal data from the active store does not recall a public copy.
- [ ] D. A rejected challenge should still be acknowledged and explained.
- [ ] E. Response times should be promised only when the team can meet them.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The downstream decision needs its own review and remedy.
- B: Contestability means genuine reconsideration is possible, not that the person always wins.
- C: Copies outside the team's control need separate handling or disclosure.
- D: The person is owed a reasoned answer and a way to escalate.
- E: Missed promises damage trust more than modest, honest commitments.

**Source:** Consultation and recourse are people's work

## MA-ch14.39

A team designs how contested AI-assisted decisions are handled. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The contested output, input provenance where lawful, the applicable policy and the human decision record should be preserved.
- [ ] B. The reviewer should be the same person who made the original decision when the case is a conflict.
- [ ] C. If the same class of report recurs while only the reply template changes, the process is absorbing complaints without controlling the system.
- [ ] D. The affected person should be asked to debate the model that produced the error.
- [ ] E. A recurring class of reports should lead to engineering change.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Without them the reviewer cannot reconstruct what happened.
- B: A conflicted reviewer cannot independently reassess.
- C: A response that never alters the system leaves the cause intact.
- D: The person needs an answerable human, not an argument with a system.
- E: Fixing the cause is the purpose of an incident process.

**Source:** Consultation and recourse are people's work

## MA-ch14.40

A student reports that a published summary gives a deadline different from the official schedule. On investigation the student was comparing the summary with an outdated schedule, and the published date matches the current official source. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The team should not revisit the summary's wording because the published date was correct.
- [ ] B. Explaining the evidence to the reporter is unnecessary when the report turns out to be wrong.
- [ ] C. The route should still acknowledge and investigate the report.
- [ ] D. A report that turns out wrong can be discarded without reply.
- [ ] E. The contest route is only credible if it upholds every challenge.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A correct but ambiguous summary can still mislead, so wording deserves a check.
- B: An explanation respects the reporter and keeps people willing to report.
- C: Reports are inputs even when they turn out wrong.
- D: Silence discourages future reports and gives the team nothing to learn from.
- E: Credible contestability allows genuine reconsideration, not guaranteed success.

**Source:** Worked incident rehearsal

## MA-ch14.41

A summarization service cites a source identifier for every claim, and its audit checks that each cited identifier exists in the document store. The service publishes a summary with a deadline that the cited document does not state. The audit passes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The finding means the original evaluation design was adequate and needs no revisiting.
- [ ] B. A person who checks only that each cited identifier exists in the store would catch this error.
- [ ] C. Making the existence check stricter, for example verifying that the identifier format is valid, would fix the problem.
- [ ] D. The audit passing does not show the claim is supported by the cited source.
- [ ] E. Deciding governance before implementation means it should not change after launch.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The audit passed a harmful output, which is evidence the evaluation did not test the relevant harm.
- B: Existence does not show that the cited text states the deadline, so this check misses the error.
- C: The failure is about meaning, not about identifier validity.
- D: It checks that a citation exists, not that the cited text entails the claim.
- E: Design-first sets the starting point; evidence from operation can and should reopen decisions.

**Source:** Worked incident rehearsal

## MA-ch14.42

A published AI-written summary is found to be wrong. The team pauses publication of affected summaries, locates copies in the systems it controls and corrects them, and notes that it cannot reach copies outside those systems. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The team should capture the source identifiers, generated output, approvals and publication evidence before changing the system.
- [ ] B. The correction should go out through the same channel that carried the original.
- [ ] C. Publication of affected items should pause while the cause is investigated.
- [ ] D. Copies the team cannot reach should be acknowledged as a limitation instead of being implied to be fixed.
- [ ] E. The reporting route should be closed once the correction is published.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Evidence can be overwritten by fixes if not preserved first.
- B: Readers who saw the error are most likely to see the correction there.
- C: Continuing to publish items of the same kind risks repeating the harm.
- D: Honest scope prevents false assurance.
- E: The correction may have missed some effect; the route lets people report that.

**Source:** Worked incident rehearsal

## MA-ch14.43

A team's service produces 150 deadline claims per day. Policy says every deadline claim must be reviewed by a person before publication. Reviewers have 2 hours per day, at 4 minutes per claim. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Narrowing the feature, such as only extracting dates with the source passage visible, can reduce the review load.
- [ ] B. Publishing the 120 unreviewed claims while still describing every claim as reviewed would accurately represent the control.
- [ ] C. The unreviewed backlog grows by 120 claims per day under the stated policy.
- [ ] D. A control that requires review of every claim but cannot be staffed to do so is not functioning as a control.
- [ ] E. Reviewers can examine 30 claims per day.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Smaller scope lowers the review needed per output.
- B: It would misstate what was done.
- C: 150 produced minus 30 reviewed is 120.
- D: A control's value depends on its being performed.
- E: 120 minutes divided by 4 minutes is 30.

**Source:** Worked incident rehearsal

## MA-ch14.44

A team says "a human is in the loop" for an LLM system that drafts decisions on 500 items an hour. A single reviewer clicks Approve on each item. The reviewer has no stated time budget per item, no authority to reject beyond clicking a different button, and no guidance on what to look for. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Human in the loop" does not specify a control unless the human task, evidence, authority, time budget and stop rule are defined.
- [ ] B. High volume can turn approval into a ritual without scrutiny.
- [ ] C. A person clicking Approve on each of 500 items an hour provides meaningful review.
- [ ] D. Throughput should be capped to the capacity of review and response.
- [ ] E. Naming a human in the process satisfies oversight regardless of whether they can reject.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The phrase names a person, not what the person is positioned to do.
- B: Fatigue and time pressure erode attention.
- C: The pace, about 7 seconds per item, leaves no time to assess content.
- D: Review quality depends on volume being matched to reviewer capacity.
- E: Oversight requires authority and ability to act on what they see.

**Source:** When deferral is the responsible output

## MA-ch14.45

A company wants to use an LLM to rank employees for promotion. The evaluation cannot observe real career outcomes, employees have not been consulted, the data boundary is unclear, and no manager has agreed to own the decisions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Deferring the project is a legitimate result.
- [ ] B. Narrowing the tool to organizing documents instead of ranking people is a possible alternative.
- [ ] C. If the model scores well on a proxy metric, the project should go ahead.
- [ ] D. A register that can only record "go" works as a rubber stamp.
- [ ] E. The team should record why it deferred and what evidence or capacity would justify reconsidering.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The preconditions for responsible use are missing.
- B: A lower-stakes variant can proceed while the missing preconditions are addressed.
- C: A proxy score does not address consultation, ownership or the data boundary.
- D: Without a legitimate way to say no or narrow, review has no force.
- E: A recorded reason makes the decision reviewable and the reconsideration conditions explicit.

**Source:** When deferral is the responsible output

## MA-ch14.46

An agent can read a CRM and send e-mails to customers on its own. Leadership has concerns about errors. Check each statement that is a valid way of narrowing the workflow. Each statement is worth 1 point (5 points total).

- [ ] A. Remove high-impact actions such as refunds until outcome checks exist.
- [ ] B. Shorten how long conversation traces are retained.
- [ ] C. Run the pilot on synthetic customer records instead of real ones.
- [ ] D. Change the agent so it drafts messages that a staff member sends.
- [ ] E. Keep the full scope and add a footer saying that e-mails may contain errors.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Excluding what cannot be safely checked limits harm.
- B: Less retained data reduces privacy exposure.
- C: Synthetic data removes exposure of real people while testing behavior.
- D: Human sending adds a review point and reversibility before external effects.
- E: A disclaimer shifts burden to recipients without reducing risk.

**Source:** When deferral is the responsible output

## MA-ch14.47

Five failure patterns can make an AI governance record look sound while the system is not governed. Hollow ownership: roles are filled with labels but nobody has accepted responsibility. Unobservable trigger: a response condition with no measurable signal. Simulated consent: model-generated reactions are presented as feedback from real people. Compliance theater: a completed internal form is treated as legal clearance. Open-ended pilot: a deployment called temporary has no end condition or review date. Check each statement in which the case is matched to the correct pattern. Each statement is worth 1 point (5 points total).

- [ ] A. A deployment announced as a one-month pilot is still running fourteen months later, collecting data, with no scheduled review: open-ended pilot.
- [ ] B. A team cites answers produced by a language model playing affected students as the stakeholder feedback it gathered: simulated consent.
- [ ] C. A completed internal template is presented to executives as proof that the system meets regulatory requirements: compliance theater.
- [ ] D. A trigger written as "act when quality falls", with no metric or measurement procedure: simulated consent.
- [ ] E. A named owner with explicit authority to pause the system, who has never needed to use it: hollow ownership.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The temporary framing has no end condition, so the deployment persists unexamined.
- B: Invented agreement is offered as if real people had weighed in.
- C: The form's existence is treated as legal clearance it cannot provide.
- D: That is an unobservable trigger; no one reading the record can tell whether it fired.
- E: A person has accepted the role and holds authority; hollow ownership describes fields filled with no one accountable.

**Source:** Governance failure patterns

## MA-ch14.48

A chatbot logs users' health questions for a year. The listed harm is that retained logs could expose sensitive health information if accessed improperly. The listed mitigation is a weekly test that checks the chatbot's answers for factual accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding the accuracy test makes the log-exposure risk resolved.
- [ ] B. Reducing retention, redacting health details before logging, or limiting access would address the mechanism more directly.
- [ ] C. A mitigation should be matched to the mechanism of the harm it is meant to reduce.
- [ ] D. The accuracy test might be useful for another risk, yet it does not reduce log exposure.
- [ ] E. The mitigation does not address the stated harm mechanism.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The exposure is unchanged.
- B: These controls act on the stored data and who can see it.
- C: Otherwise the register shows a control that controls nothing relevant.
- D: Value elsewhere does not make it relevant to this harm.
- E: Answer accuracy and log exposure are different risks.

**Source:** Governance failure patterns

## MA-ch14.49

A team of three works on an LLM workflow and records in its register: an owner, an approver and an incident contact. Check each statement that is true about how these roles differ. Each statement is worth 1 point (5 points total).

- [ ] A. The approver is the decision route for whether a proposal or change goes ahead.
- [ ] B. The owner is accountable for the workflow as a continuing system.
- [ ] C. The three roles can legitimately be held by different people to provide independent review.
- [ ] D. The approver and owner should always be the same person so the register has no ambiguity.
- [ ] E. The incident contact is where people report problems.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Approval is a gate on specific proposals.
- B: Operation, monitoring and changes over time sit with the owner.
- C: Separation reduces the chance that one person's blind spot goes unchecked.
- D: Combining them removes the independence that review is meant to provide.
- E: It is the entry point to the response path.

**Source:** A register makes questions inspectable

## MA-ch14.50

A team builds a summarizer that reads notes written by instructors and students, summarizes them for a portal, and routes corrections through a volunteer maintainer. Check each statement that is true about identifying who is affected. Each statement is worth 1 point (5 points total).

- [ ] A. Listing only the end users is sufficient.
- [ ] B. The maintainer's extra work is a staffing matter and not a governance concern.
- [ ] C. Affected people include those who never use the portal, such as students whose written work is quoted.
- [ ] D. People who cannot opt out can be given less attention, since they are not users.
- [ ] E. Groups absent from the development examples can be ignored if the tests show no problems.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It leaves out quoted authors, instructors and maintainers.
- B: Who bears the correction burden is part of who pays for errors.
- C: Harm can reach people who are not users.
- D: Lack of choice leaves them dependent on the quality of governance, which calls for more attention.
- E: Tests built without those groups cannot reveal problems affecting them.

**Source:** Governance failure patterns

## MA-ch14.51

A developer records a decision about an AI-assisted policy change, listing what the model proposed, what context a person added or corrected, the evidence supporting the recommendation, whose interests the change serves or disadvantages, and the named person's recommendation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A longer decision note demonstrates more diligence.
- [ ] B. Separating the model's proposal from the human contribution lets an auditor see where a person changed the substance.
- [ ] C. Listing whose interests are disadvantaged forces the writer to consider affected people.
- [ ] D. Evidence cited should be independent of the model's fluency.
- [ ] E. A sentence that merely repeats the model's wording is not evidence of human review.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Length is not evidence; specificity and independent support are.
- B: A note that merges them hides whether review happened.
- C: It prevents the note from reading as pure justification.
- D: The model's own claim cannot be its own support.
- E: Repetition shows copying, not judgment.

**Source:** Build It, Use It, Ship It

## MA-ch14.52

A team completes an internal AI-use register and states in a briefing: "We are compliant." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A practice that is legal is thereby ethical.
- [ ] B. A completed internal form counts as regulatory approval once management signs it.
- [ ] C. A general internal register satisfies statutory impact-assessment requirements by design.
- [ ] D. Whether personal data is processed on a lawful basis is a legal determination, not a form field.
- [ ] E. If the register status is green, legal review can be skipped.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Legal and ethical are different standards; legal practices can still harm people.
- B: Regulatory approval comes from the regulator or the legal process, not from an organization's own sign-off.
- C: A legal obligation is met only by performing what the law prescribes.
- D: Lawfulness depends on law, jurisdiction and facts that a register cannot decide.
- E: Status from a structural check says nothing about legal review.

**Source:** Governance failure patterns

## MA-ch14.53

A policy says records are deleted "30 days after the case is created." A case record was created on 10 January 2027 and last used on 20 February 2027. Another team interprets the clock as starting at last use. Check each statement that is true. Assume 2027 is not a leap year. Each statement is worth 1 point (5 points total).

- [ ] A. The ambiguity does not matter because the stated number is 30 either way.
- [ ] B. Counting from creation, deletion is due on 9 February 2027.
- [ ] C. Counting from last use, deletion is due on 22 March 2027.
- [ ] D. A policy only needs to state the number of days.
- [ ] E. The two readings differ by 41 days.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The date the data is actually deleted depends on when the clock starts.
- B: 30 days after 10 January is 9 February.
- C: 30 days after 20 February is 22 March.
- D: It also needs the clock start, who performs deletion and how deletion is checked.
- E: 9 February to 22 March is 41 days.

**Source:** Retention is a lifecycle

## MA-ch14.54

A company sends customer messages to an external LLM provider's API. Its register lists "retention: 0 days" because the company's own systems store nothing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The company can assume the provider retains nothing, since providers generally say they take privacy seriously.
- [ ] B. Zero retention in the company's own systems establishes zero retention everywhere.
- [ ] C. Provider handling can be listed as verified once the provider's marketing page states a policy.
- [ ] D. Using an external provider removes the company's responsibility for the data.
- [ ] E. Data sent to the provider is a copy handled under the provider's terms.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: An assumption is not evidence; the applicable terms must be read and unknowns recorded.
- B: The provider's handling is separate.
- C: A published claim by the provider is not verification by the company.
- D: The company that chose to send the data still answers to its customers.
- E: The provider receives and processes it outside the company's systems.

**Source:** Retention is a lifecycle

## MA-ch14.55

A developer writes a register entry and asks an assistant: "Do not rewrite it. List every field that names a group instead of a person, every threshold with no observable signal, every mitigation that does not address the harm I named, and one decision I have not written down." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Findings need no verification because the assistant has the whole document.
- [ ] B. Asking the assistant to rewrite the entry would tend to smooth over weak lines instead of exposing them.
- [ ] C. Each finding should be checked against the entry, since a finding that cannot be located in the text may be a plausible guess.
- [ ] D. If the assistant lists no problems, the entry has no problems.
- [ ] E. Using the assistant as a challenger keeps authorship of the entry with the person.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Having the text does not make the model reliable.
- B: Rewrites optimize fluency, which hides vagueness.
- C: Language models can produce confident but unfounded critiques.
- D: Absence of findings is not proof of absence.
- E: The model critiques; the person decides what to change.

**Source:** Build It, Use It, Ship It

## MA-ch14.56

An AI-assisted workflow publishes a wrong figure. Several parties made choices that mattered: the user who reported it, the content owner, the vendor of the drafting tool, the provider of the underlying model, and the institution whose data was the source. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A useful question is what change made before the incident would have prevented it.
- [ ] B. If the model provider's output was wrong, the team that deployed it carries no responsibility.
- [ ] C. The answer should be judged by whether the change is an action someone takes or only a sentence someone writes.
- [ ] D. Responsibility for failures in socio-technical systems is commonly distributed across several parties.
- [ ] E. Naming one owner does not remove dependencies on the other parties.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: This turns the review toward actions that could have been taken.
- B: Deployers choose to use the model and answer for the consequences in their setting.
- C: Controls exist when they change behavior.
- D: Each choice may be necessary without being sufficient alone.
- E: The register should record those as dependencies that were checked or assumed.

**Source:** Governance failure patterns

## MA-ch14.57

An organization's policy says customer data must not be pasted into public chatbots. Employees are evaluated on speed and have no time allowance for compliance questions; people who raise concerns about shortcuts are described as slowing delivery. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Publishing the policy is enough to ensure compliance.
- [ ] B. Organizations tend to produce the behavior they reward more than what policies say.
- [ ] C. If using pause power is penalized, that power is nominal.
- [ ] D. Time for consultation and review must be resourced if it is to happen.
- [ ] E. If shipping is rewarded and listening is not, the register will say one thing and the team will do another.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Policies without enforcement or aligned incentives are widely ignored.
- B: Incentives shape practice.
- C: Unused authority gives no protection.
- D: Unfunded obligations get dropped under delivery pressure.
- E: Documentation does not override incentives.

**Source:** Governance failure patterns

## MA-ch14.58

A team deploys a coding agent that can read files, run shell commands and call external services in developers' environments. Check each statement that is true about securing it. Each statement is worth 1 point (5 points total).

- [ ] A. Approving every shell command permanently in advance is consistent with least privilege.
- [ ] B. Granting the agent only the permissions it needs reduces the harm if it misbehaves.
- [ ] C. Security measures should be tied to a named owner, a monitoring signal and an incident response in the governance record.
- [ ] D. Text from web pages or files the agent reads can contain instructions that attackers hope the agent will follow, so such content should be treated as data and not as commands.
- [ ] E. Running the agent with a developer's full credentials carries the same risk as running it in a restricted sandbox.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Blanket approval removes the review that permission prompts provide.
- B: Least privilege limits blast radius.
- C: Controls without owners and responses are prose.
- D: This is the prompt-injection risk with untrusted inputs.
- E: Broader credentials mean larger possible damage.

**Source:** Anthropics

## MA-ch14.59

A company's lawyers argue that because an AI system cannot be sued, no one need be named as accountable for its outputs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An automated system can safely stop its own work while an authorized person retains responsibility.
- [ ] B. Assigning the AI system as the "owner" in a register is acceptable if the human team supervises it informally.
- [ ] C. An AI system is not a legal person and cannot bear legal responsibility.
- [ ] D. Because the system produced the output autonomously, accountability disappears.
- [ ] E. Accountability for an AI-assisted decision should rest with an authorized person or organization.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Stopping is a safe default that does not shift accountability.
- B: The owner must be someone who can accept and exercise responsibility.
- C: Responsibility falls on natural persons and organizations.
- D: Choosing to deploy and rely on the system is a human decision.
- E: Someone must be able to answer and correct the outcome.

**Source:** Who decided? Five choices that exist before the form does

## MA-ch14.60

A team compares three agent actions by how hard they are to undo: (1) saving a draft in a private workspace, (2) sending an e-mail to external customers, (3) publishing to a public website that search engines index. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Action (1) is the easiest to reverse.
- [ ] B. If the agent's accuracy is equal across the three actions, they need the same level of oversight.
- [ ] C. Reversibility is a reasonable input to how much review an action should require.
- [ ] D. Rollback plans are unnecessary if the model is accurate.
- [ ] E. Actions (2) and (3) have effects that escape the team's control once taken.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A private draft can be deleted without anyone else having seen it.
- B: Consequences differ, so oversight should too.
- C: Less reversible actions justify stronger review.
- D: Errors still occur and the plan limits damage when they do.
- E: Recipients and crawlers keep copies.

**Source:** Who bears the error

## MA-ch14.61

A team lead must sign off on a governance record for an LLM workflow. One draft sign-off says "Reviewed and found safe, ethical and compliant." Another lists what was checked and how, what was not checked, what is not claimed, and leaves a line for the signer's name or a note that signing was withheld. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A sign-off should state how each checked claim was verified, such as own tests, exercising an incident route, or inspecting a store.
- [ ] B. An LLM is a reliable author of the "not checked" part, because the model has a record of what the signer did not do.
- [ ] C. A sign-off should state that the workflow is ethical and compliant once all automated tests pass.
- [ ] D. The second form is more informative, because it states the limits of the evidence.
- [ ] E. Withholding a signature is a legitimate outcome when the evidence does not support signing.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The method determines how much weight the claim deserves.
- B: The model only sees what it is told; it has no record of the signer's actual activity.
- C: Tests do not establish ethics or legal compliance.
- D: Readers can see which claims rest on checks and which are open.
- E: A sign-off that cannot be refused carries no information.

**Source:** Build It, Use It, Ship It

## MA-ch14.62

A governance register can be stored as a document or wired into the system, for example so that updating a record can pause execution, revoke an approval or shorten retention. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If updating the register changes nothing in the system, it is only documentation.
- [ ] B. A register that can change what the system does is a control, not just documentation.
- [ ] C. After an incident, the register should be updated to reflect decisions that were revised.
- [ ] D. A register stored as a PDF in a shared folder is a control by virtue of being official.
- [ ] E. A well-maintained register removes the need for enforcement in the running system.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Text that has no operational effect cannot constrain anything.
- B: Governance acts when records connect to behavior.
- C: Records should show what changed and why.
- D: Official status is not operational effect.
- E: A register states intent; enforcement makes the system obey it.

**Source:** Build It, Use It, Ship It

## MA-ch14.63

A developer runs a validator's test suite and every test passes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A raised error in a test can be correct behavior under the specification.
- [ ] B. Explaining a passing case from input to returned status, without reading an assistant's explanation, is a check on one's own understanding.
- [ ] C. The result establishes that the tested behaviors work as tested.
- [ ] D. The result establishes the validator is reliable in all cases.
- [ ] E. The result gives permission to deploy the workflow it guards.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Refusal of invalid input is part of a validator's contract.
- B: It tests whether the person can account for the behavior.
- C: Tests show what they exercise.
- D: Untested inputs remain unexamined.
- E: Deployment depends on risk, ownership and approval beyond unit tests.

**Source:** Verify and reflect

## MA-ch14.64

A validator uses the allowlist {"public", "synthetic", "internal"}. It requires `data_classes` to be a non-empty list of strings, and flags any class outside the allowlist for review. Evaluate these inputs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. `["personal"]` is flagged for review.
- [ ] B. `["synthetic", "personal"]` passes because at least one label is allowed.
- [ ] C. `["Public"]` is flagged for review.
- [ ] D. `["public", "internal"]` raises no review issue.
- [ ] E. A record passing this check has data that is safe for the proposed workflow.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That label is not on the allowlist.
- B: Any label outside the allowlist produces a flag.
- C: Comparison is case-sensitive, so the capitalized label is unknown.
- D: Both labels are on the allowlist.
- E: Labels may be wrong or incomplete, and "internal" does not mean safe for every use.

**Source:** Tear down the validator
