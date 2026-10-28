# Chapter 14: Governance and ethics

## ES-ch14.1

The chapter opens: "Every field is filled. Nobody is responsible." Explain how that can be true of a register that Python reports as ready-for-human-review, using the chapter's example field values. Then state the question the chapter asks instead of "is the register complete?"

**Points:** 5

**Rubric (1 point each):**

1. States that a governance record can be structurally complete and operationally hollow.
2. Gives example field values from the chapter, such as owner "project team", incident contact "project owner", or evaluation "citation audit".
3. Explains that Python can truthfully report ready-for-human-review because it checks structure only.
4. Notes that despite the green status no named person may have accepted responsibility, no affected person may have been consulted, and no threshold may trigger a response.
5. States the replacement question: what "complete" is standing in for, meaning what has been decided, who decided it, and who will answer when the system causes harm.

**Source:** Chapter 14 - Governance and ethics (opening)

## ES-ch14.2

A teammate says, "Claude can fill the whole register in seconds, so the governance work is done." Respond using the chapter: say what Claude can and cannot do, and how the chapter divides the work into conduct, check, and drive.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude can quickly propose an owner, a threshold, a retention period, and a risk paragraph that read as fluent and plausible.
2. Says Claude cannot make anyone the owner it names, was not in the room with the people the workflow touches, and is not made answerable by its draft.
3. Conduct: owners, thresholds, retention, consultation, and recourse are designed into the system before it ships, with the register and its validator as the gate.
4. Check: a register can be complete and reviewable and still weak.
5. Drive: relationships, consent, and recourse are people's work.

**Source:** Chapter 14 - Governance and ethics (opening)

## ES-ch14.3

Define governance as this chapter does, say when applied ethics begins, and state what the course fixture contributes and what it explicitly does not grant.

**Points:** 5

**Rubric (1 point each):**

1. Says governance is not prose wrapped around a technical system.
2. Describes governance as the assignment of decisions, evidence, authority, relationships, monitoring, recourse, and response (names at least four).
3. Says applied ethics begins when those abstractions are attached to people who can be affected and people who must act.
4. Says the fixture makes missing governance information visible.
5. Says the fixture does not grant ethical clearance.

**Source:** Chapter 14 - Governance and ethics (opening)

## ES-ch14.4

The chapter asks for four predictions before you read the implementation. State the four questions and give the answer the chapter's validator produces for each.

**Points:** 5

**Rubric (1 point each):**

1. An empty record reports all seven required field names.
2. retention_days=True does not pass as one day: the exact-type check rejects it with ValueError even though Python treats True as an integer.
3. data_classes given as the string "public" rather than a list is rejected with ValueError.
4. ready-for-human-review does not mean a human has reviewed the record; it means the structural checks cleared.
5. Says the answers to the predictions should be preserved so they can be compared with what is observed.

**Source:** What you will be able to do

## ES-ch14.5

Name the five decisions that the chapter says exist before the form does, and for each give the question it asks.

**Points:** 5

**Rubric (1 point each):**

1. Owner: who accepts responsibility for the workflow as a continuing system, and what they are allowed to stop.
2. Threshold: which observable signal triggers a response, and what the response is.
3. Retention: which copies exist, for how long, and how deletion is checked.
4. Consultation: who was asked, what their answer could have changed, and what is still pending.
5. Recourse: how an affected person reaches a human who can change the outcome.

**Source:** Who decided? Five choices that exist before the form does

## ES-ch14.6

A team fills in the register first and asks Claude to supply the decisions afterward. Explain what the team has and has not produced, describe the chapter's two gates, and say what the validator is evidence for.

**Points:** 5

**Rubric (1 point each):**

1. States that an assignment of authority exists only when someone accepts it, and that Claude can draft all five decisions but cannot accept any.
2. States that filling the form first produces the shape of a decision, not a decision; people decide first and the form records.
3. Describes the validator as a machine gate whose pass condition is a list of tests you can run.
4. Describes the register's content as a human gate: a named person accepted each role and the routes work when someone uses them.
5. States that the validator is evidence for the first gate only, and that treating it as evidence for the second is the failure the opening sentence describes.

**Source:** Who decided? Five choices that exist before the form does

## ES-ch14.7

Your capstone team has a draft register, but nobody has yet accepted the retention decision or the incident-contact role. Using the chapter's gate, say what you write in the design step for these decisions, what the workflow is constrained to, and when this step happens relative to asking Claude.

**Points:** 5

**Rubric (1 point each):**

1. Says the design step is one sentence for each of the five decisions with the name of the person who made it.
2. Says to write "unresolved" for a decision no person has accepted, rather than naming someone.
3. Says to state what the workflow is constrained to until someone accepts, such as a private draft, synthetic data, or no external write.
4. Says this is done in plain sentences before asking Claude for anything.
5. Says these are your choices and no model can know which of them are real.

**Source:** The gate: write the governance before the form is filled

## ES-ch14.8

State the validator contract from the gate: what assess should return or raise for (a) an empty record, (b) the demo record, (c) a negative retention count or a string where the data-class list belongs, (d) a data class outside public, synthetic, and internal, and (e) a truthy external_write.

**Points:** 5

**Rubric (1 point each):**

1. (a) Reports all seven field names with the status incomplete.
2. (b) Returns ready-for-human-review with no issues.
3. (c) Both raise ValueError when every field is present.
4. (d) Returns review-required.
5. (e) Adds the issue "external action approval".

**Source:** The gate: write the governance before the form is filled

## ES-ch14.9

Describe the two wrong versions of the validator that your tests must catch, what each does wrongly, and what this implies about your test list.

**Points:** 5

**Rubric (1 point each):**

1. The isinstance(days, int) variant replaces the exact-type test, so retention_days=True passes as one day because Python treats True as an integer.
2. States that the lesson's six tests still pass against the isinstance variant.
3. The falsiness variant replaces the omission check, so a retention of zero, a legitimate design intent, is reported as missing.
4. States that one of the lesson's six tests catches the falsiness variant.
5. States that if your test list cannot tell the right program from both wrong ones, the gate is not finished.

**Source:** The gate: write the governance before the form is filled

## ES-ch14.10

The gate asks for one dated sentence describing what you would see if the register were hollow although the validator is green. Give an example from the chapter, and explain why the sentence has to be written before you read any output.

**Points:** 5

**Rubric (1 point each):**

1. Says the sentence is dated.
2. Says it describes an observable event that would show the register is hollow while the validator is still green.
3. Gives the chapter's example: you send the named incident contact a labeled test report and nobody acknowledges it within the stated time.
4. Explains that written after reading output, the sentence describes the output instead of testing your understanding.
5. Connects the point to the validator being evidence for the machine gate only.

**Source:** The gate: write the governance before the form is filled

## ES-ch14.11

State what the register may claim once the validator is green and named people have accepted roles, what it may not claim, and what Claude can and cannot do in writing the gate.

**Points:** 5

**Rubric (1 point each):**

1. The register may claim that the record has a minimum shape.
2. The register may claim that named people accepted named roles on named dates.
3. The register may not say the workflow is ethical, consented to, or compliant.
4. Claude can sharpen the gate by hunting for the case you missed.
5. Claude cannot write the gate without defeating its purpose, because the gate is where your decisions go on the record and what you test Claude's validator against.

**Source:** The gate: write the governance before the form is filled

## ES-ch14.12

List the seven required fields, state the question that owner, purpose, data classes, and retention days each open, and explain why the fields are "necessary prompts, not sufficient answers."

**Points:** 5

**Rubric (1 point each):**

1. Lists all seven: owner, purpose, data_classes, retention_days, approver, evaluation, incident_contact.
2. Owner is accountable for the workflow as a continuing system, not merely its initial code; purpose bounds why the system exists and reveals later use beyond that scope.
3. Data classes describe what information crosses the boundary; retention days make storage lifetime discussable.
4. Gives a weak value that still fills a field, such as owner "someone", purpose "use AI", or evaluation "test", and says why it fails to assign work, bound use, or say which outcomes were tested.
5. States that a register can force omissions into view but Python cannot infer substantive adequacy from truthy strings.

**Source:** A register makes questions inspectable

## ES-ch14.13

Explain what the missing-field check counts as missing, give at least three kinds of weak value that still pass it, and say what a register should not do as a result.

**Points:** 5

**Rubric (1 point each):**

1. Says a field is missing if its key is absent or its value is None, the empty string, or the empty list.
2. Says an empty record therefore reports all seven field names.
3. Names at least three weak values that pass: whitespace, zero in most fields, an empty dictionary, or a vague string.
4. Notes that later specialized checks catch some shapes but the boundary remains structural.
5. States that a register should not advertise more intelligence than its validator contains.

**Source:** A register makes questions inspectable

## ES-ch14.14

The validator "refuses only what it can refuse exactly." Explain this design choice using the chapter's example of the owner "project team," and name its cost.

**Points:** 5

**Rubric (1 point each):**

1. States the principle that the validator refuses only what it can refuse exactly.
2. Explains that judging "project team" would need a list of bad owner names.
3. Explains that lazy entries step around such lists.
4. Says the exactness is honest about what the validator can do.
5. Names the cost: the hard part, deciding whether a line is true, is left to people.

**Source:** Tear down the validator

## ES-ch14.15

Explain what the retention check does with True, -1, 0, and 30, and what a passing retention value still does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Says exact int typing rejects True even though bool subclasses int.
2. Says -1 fails the nonnegative range check with ValueError.
3. Says 0 is allowed and can represent a design intent such as no post-processing retention.
4. Says 30 has exact type int and is nonnegative, so it passes.
5. States that passing does not enforce immediate deletion or define transient copies, and that a number in a record is not evidence that the lifecycle follows it.

**Source:** Tear down the validator

## ES-ch14.16

Say what the validator does with each value of data_classes, assuming all other fields are valid: the string "public", ["public"], ["personal"], ["Public"], and [].

**Points:** 5

**Rubric (1 point each):**

1. The string "public" raises ValueError because the value must be a list of strings.
2. ["public"] passes the shape check and the allowlist.
3. ["personal"] yields review-required with a sensitive-or-unknown issue.
4. ["Public"] also goes to review because the allowlist is case-sensitive.
5. [] is rejected by the missing-field check.

**Source:** Tear down the validator

## ES-ch14.17

Why does the validator route an unknown data class to review instead of deciding for itself? Explain the principle and the trade-off.

**Points:** 5

**Rubric (1 point each):**

1. Says the code cannot decide whether an unknown class is legally sensitive.
2. Says the code cannot decide whether all "internal" information is safe for the proposed workflow.
3. States the conservative routing action: when the machine cannot tell, send the decision to a person.
4. Names the trade-off as noise.
5. Illustrates the noise with case sensitivity: a capitalized "Public" also goes to review.

**Source:** Tear down the validator

## ES-ch14.18

Explain what a truthy external_write does in the validator, three things the check does not do, and what the status ready-for-human-review means.

**Points:** 5

**Rubric (1 point each):**

1. A truthy external_write adds "external action approval" to the issues.
2. The check does not identify the external target.
3. The check does not authenticate approval and does not execute Chapter 13's fingerprint gate.
4. "Ready" means the teaching record cleared the structural checks with no flagged class or external-write condition.
5. It does not mean "approved"; both statuses lead to people.

**Source:** Tear down the validator

## ES-ch14.19

The demo record returns {"status": "ready-for-human-review", "issues": []}. Explain why that result is accurate about the function but weak as governance evidence. Name the question the validator cannot ask and at least three of the weak lines.

**Points:** 5

**Rubric (1 point each):**

1. Explains the result is accurate: thirty is an exact nonnegative int, data_classes is a list holding one allowlisted string, and no external-write flag is truthy.
2. Names the question the validator cannot ask: who confirmed each of these lines, and how?
3. Notes that "Project team" may name no accountable individual and "Instructor" may describe a role without proving a particular instructor accepted it.
4. Notes that "Citation audit" leaves sampling, checker, criteria, and failure response unstated, and "Project owner" may be unreachable to affected people.
5. Notes that thirty days says nothing about caches, backups, exported artifacts, or deletion verification.

**Source:** Complete, reviewable, and still weak

## ES-ch14.20

You run assess({}), assess with data_classes ["personal"], and assess with external_write=True on a public-data record. Say what each returns and what these runs do not demonstrate.

**Points:** 5

**Rubric (1 point each):**

1. assess({}) returns incomplete with all seven field names.
2. data_classes ["personal"] gives review-required with the sensitive-or-unknown issue.
3. external_write=True adds the external-action issue.
4. States that these runs demonstrate routing.
5. States that they do not demonstrate agreement by named people, stakeholder consent, lawful processing, effective mitigation, or outcome fairness (names at least three).

**Source:** Complete, reviewable, and still weak

## ES-ch14.21

A team submits owner "everyone", purpose "help", retention_days 99999, approver "manager", evaluation "looks fine", incident_contact "team", and data_classes ["public"]. What can the validator return, is that a defect, and what must the human review do?

**Points:** 5

**Rubric (1 point each):**

1. States that the current function can return ready-for-human-review.
2. States that this is not a defect relative to the function's narrow contract.
3. States that it is a counterexample to broad claims about what the status means.
4. States that the human review must interrogate meaning.
5. States that Claude can list the vague lines but you must confirm each against the world.

**Source:** Complete, reviewable, and still weak

## ES-ch14.22

Complete the chapter's evidence table: for each of "seven fields present", "retention is a nonnegative integer", "classes are known labels", "external-write issue", and "ready for human review", say what it supports and give one thing that remains open.

**Points:** 5

**Rubric (1 point each):**

1. Seven fields present supports a minimum record shape; adequacy and acceptance remain open.
2. Retention is a nonnegative integer supports valid shape of the declared day count; the actual deletion lifecycle remains open.
3. Classes are known labels supports no unknown label under the course allowlist; classification accuracy remains open.
4. The external-write issue supports that a routing trigger was detected; target, authority, and outcome remain open.
5. Ready for human review supports that a structural preflight was completed; consent, ethics, and compliance remain open.

**Source:** Complete, reviewable, and still weak

## ES-ch14.23

Using the chapter's verb ladder, choose the weakest verb the evidence supports for each: (a) the register shows a named owner; (b) the owner told you she accepts the role; (c) you sent a labeled test report to the incident contact and watched it be acknowledged; (d) you inspected the log store yourself and checked the fixture was gone. Then say what verb the validator itself earned.

**Points:** 5

**Rubric (1 point each):**

1. (a) listed.
2. (b) confirmed.
3. (c) exercised.
4. (d) verified.
5. Says the function only reported that fields were present and well shaped, without confirming, accepting, or verifying anything, and that the ladder is a teaching device and not an industry standard.

**Source:** Complete, reviewable, and still weak

## ES-ch14.24

A register says "There may be bias or privacy concerns." Rewrite this for a public-course-note summarizer by naming affected groups and concrete harms, and say who pays and who could have prevented each harm. Why is the original line weak?

**Points:** 5

**Rubric (1 point each):**

1. Says the original line can be pasted into almost any register and tells no one what to do.
2. Names at least two affected groups, such as students whose work is quoted, instructors whose policies are paraphrased, maintainers, or readers.
3. Names at least two concrete harms, such as misrepresenting a deadline, exposing a student's attributed work, omitting an accommodation route, or publishing an unsupported instruction.
4. Says each harm has a person who pays and, usually, a different person who could have prevented it.
5. States that applied ethics asks who can be affected, through which mechanism, with what consequence, and whether they can contest it.

**Source:** Who bears the error

## ES-ch14.25

State at least five of the distribution questions the chapter asks about a workflow, and apply two of them to the note summarizer.

**Points:** 5

**Rubric (1 point each):**

1. Asks who receives the benefit.
2. Asks who bears false positives and false negatives, and who has to spend time correcting the system.
3. Asks who is absent from the development examples and who can opt out.
4. Asks who is exposed when data is retained and who can reach a human when the output is wrong.
5. Applies at least two of these questions to the note summarizer with a concrete answer, such as students whose work is quoted or maintainers who field questions.

**Source:** Who bears the error

## ES-ch14.26

Agent A reads public notes, creates a local draft, retains inputs for one day, and requires human publication. Agent B reads internal records, publishes externally, and retains complete traces for a year. Both have the same measured accuracy on the same bounded evaluation set. Which needs stronger governance, and why can ethics not be added after model selection?

**Points:** 5

**Rubric (1 point each):**

1. States that equal accuracy does not produce equal risk.
2. Says Agent B has a broader action surface than Agent A, since it reads internal records and publishes externally.
3. Says Agent B has more sensitive context and a longer privacy exposure, a year of traces versus one day.
4. Says Agent B's rollback and incident needs differ because of its external effects.
5. Explains that accuracy describes selected outputs under selected trials while governance describes surrounding power and consequences, and that architecture choices such as data minimization, authority, retention, reversibility, and review routing shape the harm surface before the first score.

**Source:** Who bears the error

## ES-ch14.27

Two summarizers make the same number of deadline errors on the same bounded set. One states a deadline its sources do not support; the other omits the deadline when sources conflict. Say who pays for each error, what the accuracy number fails to say, and who should choose.

**Points:** 5

**Rubric (1 point each):**

1. Says students who plan around a wrong date bear the first error.
2. Says students who must ask, and the maintainers who field their questions, bear the second error.
3. Notes that the accuracy figure is identical for both summarizers.
4. Says nothing in the accuracy number shows which error the team should prefer; that is a choice about whose cost counts.
5. Says someone makes that choice whether or not they notice, so it should be made on the record by the party accountable for the policy the tool serves.

**Source:** Who bears the error

## ES-ch14.28

The companion book on computational skepticism says three reasonable fairness definitions cannot all hold. Name them, state the condition, and state what the book concludes about choosing one, using its sentencing example.

**Points:** 5

**Rubric (1 point each):**

1. Names equal rates of favorable prediction across groups.
2. Names equal error rates across groups and scores that mean the same thing for every group.
3. States they cannot all hold when the groups' base rates differ, short of perfect prediction.
4. States that each definition is a values claim about which error or equality matters, so choosing one is a decision with an owner, not an optimization.
5. Describes the criminal-sentencing risk score case: two parties reported accurate numbers and disagreed about which numbers should count, a disagreement about values and not data.

**Source:** Who bears the error

## ES-ch14.29

A classmate building the note summarizer proposes adding demographic columns "to look rigorous." Respond using the chapter: when does the fairness analysis apply, what should the summarizer team do instead, and what defended choice is the deliverable?

**Points:** 5

**Rubric (1 point each):**

1. Says the analysis applies where the task supports it, for example when the workflow ranks people or allocates opportunity among them.
2. Says that for a summarizer one should not invent demographic columns to look rigorous.
3. Says to name the harm mechanism the workflow actually has and ask which error the team will risk and who pays.
4. Says the deliverable is a defended choice: the deployment and who bears the cost of error, which option was chosen where options conflict, why, and what evidence would change your mind.
5. Says the decider should be the party accountable for the policy the tool serves, not whoever's loss function encoded a default, and that the register is where this is done on the record.

**Source:** Who bears the error

## ES-ch14.30

Rewrite the vague line "monitor quality and intervene if needed" as an operational record for the note summarizer, and name each element your rewrite includes.

**Points:** 5

**Rubric (1 point each):**

1. Includes an observable signal, such as an unsupported-source flag.
2. Includes a threshold, such as any public draft with a deadline claim lacking an approved source identifier.
3. Includes an accountable owner, such as the content owner.
4. Includes a bounded response and scope, such as pausing publication and having the incident contact examine affected drafts.
5. Includes a recovery condition, such as resuming only after correction and a repeated citation audit.

**Source:** Owners, thresholds, and bounded responses

## ES-ch14.31

A dashboard shows a 99 percent pass rate. Explain why that does not settle whether the threshold is adequate, and what the chapter says about pause authority, escalation, and role assignment.

**Points:** 5

**Rubric (1 point each):**

1. Says a 99 percent pass rate can conceal one severe disclosure, so thresholds should connect to harm and not only aggregate performance.
2. Says some events require an immediate stop on a single occurrence while others justify trend monitoring.
3. Says the owner needs explicit authority to pause, because if incentives punish delay and only reward shipping a nominal incident contact cannot govern.
4. Says escalation must be defined for when the owner is unavailable, implicated, or lacks expertise.
5. Says to avoid assigning every role to one person merely to complete the form.

**Source:** Owners, thresholds, and bounded responses

## ES-ch14.32

Explain why "retention_days: 30" is "a policy input, not a deletion mechanism," and describe how you would trace the copies of one data class.

**Points:** 5

**Rubric (1 point each):**

1. States that retention_days is a policy input, not a deletion mechanism.
2. Names at least five copies to trace, such as the incoming prompt, local fixture, application log, provider handling, cache, exported report, repository history, backup, or incident record.
3. Says to include only systems actually in scope and to mark unknowns.
4. Lists at least four things to state for each data class: why it is collected, the minimum needed, who can access it, when the clock begins, how deletion is performed, how deletion is checked.
5. Says not to turn a desired policy into a claim about systems you have not inspected.

**Source:** Retention is a lifecycle

## ES-ch14.33

A team writes "retention: 0 days" and says that, with no audit trail at all, privacy is perfect. Evaluate this using the chapter's discussion of zero-day retention and incident replay.

**Points:** 5

**Rubric (1 point each):**

1. Says zero-day needs clarification, since it may mean delete immediately after the task, do not persist application data, or retain only de-identified evidence.
2. Says temporary memory and provider-side processing still exist.
3. Says keeping everything forever makes privacy risk worse, while keeping nothing may prevent accountability.
4. Proposes a minimal, separated audit record with items such as operation identity, policy decision, safe evidence references, error category, and responsible roles.
5. Says sensitive payloads should be stored only when justified and protected.

**Source:** Retention is a lifecycle

## ES-ch14.34

You insert a labeled fixture, run the deletion lifecycle, and the fixture no longer appears in the dictionary your code uses. State what you may claim, what you may not claim, and how the verb ladder applies to the stores involved.

**Points:** 5

**Rubric (1 point each):**

1. Says to test deletion like any other behavior: insert a labeled fixture, run the lifecycle, and inspect the stores you control.
2. Says "removed from this dictionary" is not "erased everywhere."
3. Says the stores you inspected are verified.
4. Says the provider's and the backups' are, at best, listed.
5. Says to state what remains unverified.

**Source:** Retention is a lifecycle

## ES-ch14.35

A teammate asks Claude to write the reaction of an affected student and records it as consultation. Explain why this fails, using the chapter's operational argument, and what a real consultation still requires.

**Points:** 5

**Rubric (1 point each):**

1. Says a reply Claude generates in the voice of an affected student is not a statement by that student.
2. Says consent is something a person gives.
3. Says the operational argument needs no position on machine minds, and the philosophical argument need not be accepted to follow the chapter.
4. Says someone still has to ask the actual person, hear the answer, and stay reachable afterward.
5. Says invented agreement is not consent, and the register should say which real consultation remains pending.

**Source:** Consultation and recourse are people's work

## ES-ch14.36

Describe how to design a consultation that can change the project: who to include, what to tell participants, and the test for whether the consultation is real or theater.

**Points:** 5

**Rubric (1 point each):**

1. Says to decide who is affected directly, who maintains the surrounding work, who has relevant domain knowledge, and who is routinely missing from design decisions.
2. Says not to ask one convenient person to stand in for every stakeholder.
3. Says participation should be voluntary where appropriate, and the team should explain what will be recorded, how it will be used, and whether declining has consequences.
4. Says consultation counts only if the answer could have changed the purpose, boundaries, retention, or the decision to automate.
5. Says that asking only how to make a predetermined deployment more acceptable turns participation into theater.

**Source:** Design consultation that can change the project

## ES-ch14.37

Critique the question "Does this helpful tool sound good?" and write better ones. Say what Claude may do to help prepare the consultation and what a human must do before the explanation is shared.

**Points:** 5

**Rubric (1 point each):**

1. Says the question solicits reassurance.
2. Offers a better question about what outcome would be unacceptable or what information should never enter the workflow.
3. Offers better questions about what correction process would be usable or what would make the person withdraw support.
4. Says Claude can help prepare a plain-language explanation of what the workflow receives, produces, where a person decides, what is retained, and how to report a problem.
5. Says a human must check the explanation against the real system, because fluent simplification can omit the external write or retention detail a person needs.

**Source:** Design consultation that can change the project

## ES-ch14.38

During a consultation a student says she cares less about summary accuracy than about being quoted without context. Explain what the team should do during and after the conversation, and how a classroom role-play must be handled differently from real consultation.

**Points:** 5

**Rubric (1 point each):**

1. Says to listen beyond the prepared categories, since situated distinctions can change data classes, access, purpose, or the decision to proceed.
2. Says afterward to separate actual statements from AI summaries and return a summary for confirmation when appropriate.
3. Says to record concrete design changes and unresolved concerns.
4. Says that if someone withdraws permission, the retention and deletion process must know which artifacts derived from their contribution.
5. Says role-play is useful rehearsal but every response is labeled simulated because invented agreement is not consent, and the register states which real consultation remains pending.

**Source:** Design consultation that can change the project

## ES-ch14.39

The incident contact field says "project owner." Explain why that is not recourse, and list the parts of a recourse path the team must build.

**Points:** 5

**Rubric (1 point each):**

1. Says an incident contact field often becomes an inbox nobody owns.
2. Says a reporter needs a discoverable channel and a description of what information is helpful without being forced to expose more private data.
3. Says the team needs an acknowledgment rule and a triage owner.
4. Says the team needs an urgent-stop trigger, investigation access, and correction authority.
5. Says the team needs escalation for when the first contact cannot resolve the issue.

**Source:** Recourse is a system path, not an email address

## ES-ch14.40

Give three examples from the chapter showing that different harms need different remedies, and say how to decide what counts as meaningful correction.

**Points:** 5

**Rubric (1 point each):**

1. Says correcting a displayed summary does not repair a decision already made from it.
2. Says removing personal data from the active store does not recall a public copy.
3. Says explaining a model's reasoning does not restore an opportunity denied to someone.
4. Says to ask the affected person what meaningful correction looks like.
5. Says to recognize that institutional constraints may require additional decision makers.

**Source:** Recourse is a system path, not an email address

## ES-ch14.41

A tool lets people appeal a result by emailing an address answered by a chatbot, and the person who made the original decision owns the inbox. Evaluate this route with the chapter's five questions.

**Points:** 5

**Rubric (1 point each):**

1. Asks whether a person can challenge a result.
2. Asks whether a person can obtain an explanation appropriate to the decision.
3. Asks whether a person can reach a human who can correct the record, and notes the affected person should not have to debate a model.
4. Asks whether a person can see downstream copies updated.
5. Asks whether a person can appeal beyond the original owner, noting that a second route is needed when the original owner is conflicted.

**Source:** Recourse is a system path, not an email address

## ES-ch14.42

Describe what the chapter says makes contestability practical, and what it means when a process is absorbing complaints instead of controlling the system.

**Points:** 5

**Rubric (1 point each):**

1. Says to preserve the contested output, input provenance where lawful, applicable policy, and the human decision record.
2. Says to give the reviewer power to change the result.
3. Says to provide a second route when the original owner is conflicted.
4. Says to state response times only when the team can meet them, and that Claude can assemble the passages in dispute but a reachable human must own the response.
5. Says that if the same class of report recurs while only the explanation template changes, the process is absorbing complaints rather than controlling the system.

**Source:** Recourse is a system path, not an email address

## ES-ch14.43

In the chapter's worked rehearsal a course-note agent publishes the wrong assignment deadline. Trace detection, the immediate response, and the investigation finding, and state the harm mechanism.

**Points:** 5

**Rubric (1 point each):**

1. States the harm mechanism: reliance on a wrong deadline, so students may allocate work incorrectly.
2. States detection: a student reports a mismatch with the official schedule, and the observable trigger is a published deadline claim whose cited source does not support it.
3. States that the content owner pauses publication of affected summaries and captures source identifiers, generated output, the approved proposal, and publication evidence.
4. States the finding: the citation audit checked whether a citation string existed, not whether the cited passage entailed the deadline.
5. States that the mitigation did not address the harm, even though the register was structurally ready for review.

**Source:** Worked incident rehearsal

## ES-ch14.44

The register was written before the system shipped, yet the incident changes it. What does this show about "design before implementation," which register decision was reopened, and how was it changed?

**Points:** 5

**Rubric (1 point each):**

1. Says design before implementation is not a freeze.
2. Says a later finding can send you back to an earlier choice, and the governance record should say that it did.
3. Identifies the reopened decision as the evaluation line.
4. Says the team adds an entailment-oriented human check for deadline claims.
5. Says the team also creates a refusal case with conflicting schedules and prevents external publication until the claim is reviewed.

**Source:** Worked incident rehearsal

## ES-ch14.45

List the five before-to-after revisions in the chapter's incident table and the incident evidence behind each.

**Points:** 5

**Rubric (1 point each):**

1. "Citation audit" becomes a support check for consequential claims, because the citation existed but did not support the claim.
2. A generic project owner becomes a named content owner and backup, because pause authority was uncertain.
3. An implicit external write becomes an explicit publication approval, because the public effect was under-described.
4. "Correction means edit" becomes a bounded copy inventory and limitation, because downstream copies were unknown.
5. "Contact receives report" becomes acknowledgment, triage, escalation, and recovery, because the response sequence was absent.

**Source:** Worked incident rehearsal

## ES-ch14.46

Explain the chapter's three variants of the deadline incident (a wrong report, an unavailable incident contact, and the labor of the remedy) and what each teaches.

**Points:** 5

**Rubric (1 point each):**

1. Wrong report: the route still acknowledges and investigates, explains the evidence, preserves the challenge, and checks whether the public wording created reasonable ambiguity.
2. States that contestability means a person can trigger genuine reconsideration, not that every challenge decides the outcome.
3. Unavailable contact: the backup receives the alert after the declared acknowledgment threshold, pauses publication under delegated authority, and records why.
4. If no backup exists, that is an unresolved dependency; the agent must not nominate itself, and responsibility remains with an authorized person or organization.
5. Labor: if the team cannot sustain review of every deadline claim, narrow the feature to extracting dates with visible source passages, since a mitigation that cannot be maintained is not a control.

**Source:** Worked incident rehearsal

## ES-ch14.47

When is deferral the responsible output? Give at least four conditions, three ways to narrow scope, and say what the register should record.

**Points:** 5

**Rubric (1 point each):**

1. Names at least four conditions, such as a contested purpose, unconsulted affected people, an unknown data boundary, evaluation that cannot observe the consequential outcome, no incident capacity, or no authorized owner.
2. Names at least three ways to narrow scope, such as a draft for review instead of an external write, synthetic data, organizing documents instead of ranking people, shorter retention, or removing a high-impact action.
3. Says stopping is also a design result when the benefit is marginal and the cost falls on people who cannot contest it.
4. Says to record why the team deferred and what evidence or capacity would justify reconsideration, because a register that can only say "go" is a rubber stamp.
5. Says "human in the loop" must name the human task, evidence, authority, time budget, and stop rule, and that governance must limit agent throughput to review and response capacity.

**Source:** When deferral is the responsible output

## ES-ch14.48

Name the failure pattern shown by each situation, then name and define the two patterns not shown: (a) every field holds a role such as "team" and nobody has accepted ownership; (b) a citation audit is offered for a privacy-retention harm; (c) the threshold reads "when quality falls"; (d) Claude-written student reactions are presented as feedback.

**Points:** 5

**Rubric (1 point each):**

1. (a) Complete form, absent responsibility.
2. (b) Mitigation mismatch.
3. (c) Unobservable threshold.
4. (d) Consent by simulation.
5. Names compliance theater (the register treated as legal clearance despite its classroom scope) and permanent pilot (a temporary deployment accumulating data and effects without an end condition or review date).

**Source:** Governance failure patterns

## ES-ch14.49

Describe the Build It step for this chapter: what you do before opening the reference solution and how you compare afterward.

**Points:** 5

**Rubric (1 point each):**

1. Says to write your own assess from the contract in the gate before opening the reference solution.
2. Says to trace one successful case by hand, marking the input boundary, the transformation, and the returned result.
3. Says to trace one failure from the tests, changing one input at a time so a difference has an identifiable cause.
4. Says to write down, for each of the lesson's six tests, which wrong program it exists to catch.
5. Says to compare with the reference and name a difference in behavior, not in line count or style.

**Source:** Build It, Use It, Ship It

## ES-ch14.50

Describe the first pass of Use It, the validator: what you give Claude, what you do with what it returns, and how you test whether your test list is strong enough.

**Points:** 5

**Rubric (1 point each):**

1. Says to give Claude the gate (the contract and your test list including your two added tests), not your implementation.
2. Says to run your tests on what Claude returns, yourself.
3. Says a failing test is often a gap in your gate, which Claude cannot see because it has only what you wrote.
4. Says to compare its implementation with your baseline and name one difference in behavior.
5. Says to ask Claude for a deliberately wrong version that still passes your tests and check by hand; if it does, your list was too weak.

**Source:** Build It, Use It, Ship It

## ES-ch14.51

Describe the second pass of Use It, the register: how you read Claude's draft, what the challenger prompt asks for, and why you tell Claude not to rewrite the entry.

**Points:** 5

**Rubric (1 point each):**

1. Says to read the draft as the author of the gate: which of the five decisions each line answers, whether there is a person's name, and where it sits on the verb ladder.
2. Says the challenger prompt asks for fields whose value names a group or role rather than a person, and thresholds with no observable signal.
3. Says it also asks for mitigations that do not address the named harm and one decision not written down.
4. Says withholding the rewrite is deliberate: you want weak lines found, not smoothed.
5. Says to verify each finding against the entry yourself, since a finding you cannot locate in the text is a fluent guess.

**Source:** Build It, Use It, Ship It

## ES-ch14.52

List what the Ship It register entry must contain for your capstone and what to do about unresolved authority or pending consultation.

**Points:** 5

**Rubric (1 point each):**

1. Starts with the actual capstone workflow, not a generic AI policy paragraph, and names the bounded purpose and non-purpose.
2. Lists input sources, data classes, tools, and action targets, linking the Week 11 evidence matrix and Week 13 approval gate.
3. Adds one concrete harm scenario saying who bears it and how it occurs.
4. Assigns a mitigation owner with pause authority, an observable threshold and response, the retention lifecycle with deletion evidence, and an incident route and appeal path.
5. Records unresolved authority rather than assigning it fictionally, and if consultation is pending says so and constrains the workflow.

**Source:** Build It, Use It, Ship It

## ES-ch14.53

What five things does the decision note record, and what should you do with a sentence that only repeats Claude?

**Points:** 5

**Rubric (1 point each):**

1. Records what Claude proposed.
2. Records what context a person added or corrected.
3. Records what evidence supports the recommendation.
4. Records whose interests the recommendation serves or disadvantages.
5. Records the named human recommendation, and highlights any sentence that merely repeats Claude because repetition is not review.

**Source:** Build It, Use It, Ship It

## ES-ch14.54

Describe the five lines of the sign-off template and what belongs in each.

**Points:** 5

**Rubric (1 point each):**

1. Checked: which register lines you confirmed against the running workflow, and which named owners confirmed they accept the role.
2. How: by what means, such as your own tests on the validator, exercising the incident route, inspecting stores you control, conversation with the named owner, or with Claude's help.
3. Not checked: deletion in systems you do not control, whether the threshold fires under real load, consultation with affected people (done or pending), and any legal or institutional compliance.
4. Not claiming: that the workflow is ethical, consented to, or compliant, and that ready-for-human-review means anyone has reviewed it.
5. Signed or withheld: a name and date.

**Source:** Build It, Use It, Ship It

## ES-ch14.55

Why does the chapter say the "Not checked" line does the work, how does the sign-off differ from the approver field, and what should you do if your evidence does not support signing?

**Points:** 5

**Rubric (1 point each):**

1. Says "Not checked" is the line an AI-written sign-off never includes, because the system that wrote it has no record of what you did not do.
2. Says the approver field names who may approve the workflow.
3. Says the sign-off states what the register itself has earned.
4. Says a sign-off means something only if withholding is a real option.
5. Says that when evidence does not support signing, withholding is an honest result and the right action is to narrow or defer the workflow, not to find words that make the form pass.

**Source:** Build It, Use It, Ship It

## ES-ch14.56

For three tasks in the driver's seat table (choosing thresholds, consultation, and recourse and appeal), say what Claude should do, what you should do, and why the task stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Thresholds: Claude computes rates, proposes signals, and simulates a breach; you choose the threshold, who may pause, and who absorbs the cost of pausing.
2. Thresholds stay with you because which error to risk, and who pays, is a values claim with an owner.
3. Consultation: Claude drafts questions and organizes authorized, sanitized feedback; you hold the conversation, obtain or withhold permission, and stay reachable.
4. Recourse: Claude assembles the contested output and the passages in dispute; you hear the person, decide, correct, and provide a second route if conflicted.
5. These stay with you because consent and relationship are acts between people, and the affected person needs an answerable human, not a better explanation.

**Source:** The driver's seat

## ES-ch14.57

How does the chapter say to verify the validator and the register, and what does a passing test suite establish?

**Points:** 5

**Rubric (1 point each):**

1. Says verification begins with claims small enough to test.
2. Says to run the demo and the lesson's six tests, then your two, and keep commands, observed outputs, and your interpretation.
3. Says that for the register you name the verb each line earned.
4. Says a passing test suite establishes only the tested behavior, not universal reliability or permission to act.
5. Says to explain one passing case without reading Claude's explanation and one raised error, and that "approved" requires a person who did the approving.

**Source:** Verify and reflect

## ES-ch14.58

Assessment 3 asks you to rewrite ready-for-human-review and review-required as precise sentences that do not overclaim. Write both sentences, choose the verb, and say what evidence would justify a stronger one.

**Points:** 5

**Rubric (1 point each):**

1. Writes ready-for-human-review as: the teaching record cleared the structural checks and nothing was flagged for review.
2. Writes review-required as: the validator flagged an unknown or sensitive data class or an external write and routes the decision to a person.
3. Makes clear that neither sentence implies approval, consent, or compliance.
4. Chooses "reported" as the verb the function earned, not confirmed, accepted, or verified.
5. Names the evidence behind stronger verbs: confirmed (the person told you), exercised (you ran the route), verified (you inspected the store).

**Source:** Assessments - ungraded practice

## ES-ch14.59

What does the Anthropics section tell you to do with Anthropic's Claude Code security guidance, and what limits does it put on how that guidance and the register may be read?

**Points:** 5

**Rubric (1 point each):**

1. Says the guidance can inform analysis of access boundaries, untrusted inputs, and safe operation.
2. Says to connect a relevant recommendation to a named owner, monitoring signal, and incident response in your register rather than copying general security prose.
3. Notes the primary link was checked for the approved research packet on 2026-09-06.
4. Says product guidance supplements the governance analysis and applicable Northeastern policies determine institutional use.
5. Says the register is a course mechanism and not a claim about Anthropic's internal governance or a legal compliance tool.

**Source:** Anthropics

## ES-ch14.60

Using the Computational Skepticism section, name the diagnostic about responsibility, list the parties whose choices shaped the rehearsal incident, and state the questions it asks you to apply to your register.

**Points:** 5

**Rubric (1 point each):**

1. States the diagnostic: responsibility for a failure distributes across parties whose choices were each necessary and none sufficient.
2. Lists at least four of the parties: the reporting student, the content owner, the maker of the drafting tool, the model provider, and the institution whose schedule is the source of truth.
3. Says that for each party other than the register's one owner, you find where the register records their decision as a dependency checked rather than assumed.
4. Asks what change to the register, made before the incident, would have prevented it.
5. Asks whether that change is an action someone takes or a sentence someone wrote.

**Source:** Computational Skepticism

## ES-ch14.61

Apply the three-cell test from the Conducting AI section to one sentence of Claude's register draft: name each cell and its question, and say what the section argues about fluent output.

**Points:** 5

**Rubric (1 point each):**

1. Notes the test borrows Suchman's three legitimacies, an adaptation by the book's author and not Suchman's own.
2. Pragmatic: does the sentence serve the people it is for? A fluent draft usually passes.
3. Moral: whose standards would acting on it have to survive, and who would have to answer for it?
4. Cognitive: do you trust the sentence because you can account for it, with these facts verified in these ways, or because it reads well?
5. Says fluent output supplies the appearance of cognitive trust without its grounds, and supplying the grounds is the human's work, which the decision note shows.

**Source:** Conducting AI

## ES-ch14.62

According to the Irreducibly Human section, what does an institution teach, what example does the book give, what should you ask of your own team, and what are the "AI should" and "Human should" responsibilities?

**Points:** 5

**Rubric (1 point each):**

1. Says an institution teaches what it actually rewards, not what it nominally teaches.
2. Gives the example of medical training, where environments rewarding efficiency erode the empathy their curricula ask for.
3. Asks whether anyone gets time for consultation and whether the person with pause authority is rewarded or penalized for using it, noting that if shipping is rewarded and listening is not, the team does what is rewarded.
4. AI should draft plain-language explanations, suggest questions, organize authorized sanitized feedback, surface uncertainty, and preserve objections, but not invent stakeholder testimony, imply consent, or speak as though it represents an affected person.
5. Human should hold the actual conversation, listen for concerns outside the script, obtain permission where required, remain reachable, and decide how feedback changes access, retention, evaluation, or deployment.

**Source:** Irreducibly Human

## ES-ch14.63

What does Chapter 15 ask of the team's parts, what must be true for the capstone to succeed, and what do you carry forward?

**Points:** 5

**Rubric (1 point each):**

1. Says Chapter 15 asks whether the register, owners, gates, evidence, and incident routes form one defensible system.
2. Says another person must be able to reproduce the capstone's central result.
3. Says another person must be able to observe a controlled failure.
4. Says another person must be able to inspect recovery and understand why the accountable owner chose to ship, narrow, defer, or stop.
5. Says to carry the register forward with its sign-off, or with your reason for withholding it.

**Source:** Forward bridge
