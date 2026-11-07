# Chapter 14: Governance and ethics

## ES-ch14.1

A team's AI-use register has every required field filled. The owner field reads "project team", the incident contact reads "project owner" and the evaluation field reads "citation audit". A script that checks only that fields are non-empty reports the record as ready for human review. Explain how a register can be complete and the workflow still have no one responsible, and say what question a reviewer should ask instead of "is the register complete?"

**Points:** 5

**Rubric (1 point each):**

1. A record can be structurally complete yet operationally hollow: presence of text in a field is not the same as a decision having been made.
2. Group or role labels such as "project team" do not identify a person who has accepted responsibility, and a vague evaluation line does not say what was tested.
3. A completeness script checks structure only, so it can truthfully report a green status while no one is accountable, no affected person was consulted and no threshold triggers any response.
4. The status "ready for review" is not approval, consent, compliance or an ethical judgment.
5. The better question is what "complete" stands in for: what has been decided, who decided it, and who will answer when the system causes harm.

**Source:** Opening: a complete register is not a responsible team

## ES-ch14.2

A teammate says: "An LLM can fill the whole governance register in seconds, so the governance work is done." Respond. Say what a language model can and cannot contribute, and describe how responsibilities divide between the model and the humans in the team.

**Points:** 5

**Rubric (1 point each):**

1. The model can draft fluent, plausible proposals quickly, such as an owner, a threshold, a retention period and a risk paragraph.
2. It cannot make anyone the owner it names: accountability exists only when a person accepts it.
3. It has no first-hand contact with the people affected and is not answerable for the workflow after the conversation ends.
4. Humans decide and record the key choices (owners, thresholds, retention, consultation, recourse) before the form is filled, and check that a complete-looking register is not weak.
5. Relationships, consent, recourse and the decision to ship, narrow or stop remain with people, who also sign or withhold the final sign-off.

**Source:** Opening: what Claude can and cannot do in a governance register

## ES-ch14.3

A validator reports one of three statuses for a governance record: "incomplete", "review-required" and "ready-for-human-review". Write precise one-sentence descriptions of what "ready-for-human-review" and "review-required" each claim, and explain what stronger claims would need as evidence.

**Points:** 5

**Rubric (1 point each):**

1. "Ready for human review" means the record cleared the validator's structural checks and nothing was flagged; it describes the record's shape.
2. "Review required" means the validator found a condition it cannot resolve (for example an unknown data class) and is routing the decision to a person.
3. Neither status states that a human has reviewed, approved or accepted anything.
4. Claims of approval would need an identifiable authorized person who approved a specific proposal on a specific date.
5. Claims of consent or legal compliance would need evidence from the affected individuals or from legal review respectively, which a script cannot supply.

**Source:** Teardown of the validator: what a status means

## ES-ch14.4

Five decisions underlie any governance record for an AI workflow: owner, threshold, retention, consultation and recourse. Define each in one sentence as an assignment of authority or responsibility, and explain why a team should make these decisions before it fills in a governance form.

**Points:** 5

**Rubric (1 point each):**

1. Owner: the person who accepts responsibility for the workflow as an ongoing system and has authority to stop it.
2. Threshold: the observable signal that triggers a response, together with what the response is.
3. Retention: which copies of data exist, for how long, and how deletion is performed and checked.
4. Consultation: who was asked, what their answers could have changed, and what remains pending; recourse: how an affected person reaches a human who can change the outcome.
5. Each is an assignment of authority that exists only when someone accepts it; filling the form first yields the shape of a decision and anchors reviewers to a draft instead of a decision.

**Source:** Who decided? Five choices that exist before the form does

## ES-ch14.5

A team cannot find anyone willing to accept ownership of a planned LLM workflow that will send e-mails to customers. Describe how the team should record this gap, what constraints they should place on the workflow until the gap is closed, and why they should not simply put a placeholder name in the owner field.

**Points:** 5

**Rubric (1 point each):**

1. The gap should be recorded explicitly as unresolved, not filled with a plausible name.
2. A placeholder name creates the appearance of accountability without anyone having accepted it.
3. Until someone accepts ownership, the workflow should be constrained, for example to private drafts, synthetic data, or no external writes.
4. The constraints should be tied to a condition for lifting them, such as a named person accepting the role with authority to pause.
5. Assigning every role to one person or to the AI agent merely to complete the form does not solve the gap, because the owner must be someone who can accept and exercise responsibility.

**Source:** Who decided? Five choices that exist before the form does

## ES-ch14.6

Before asking an LLM assistant to implement a validator for a governance record, a developer writes a specification (what must pass, what must raise errors, what must be flagged) and a set of tests. Explain what the developer gains by doing this first and what the developer should do with the assistant's implementation afterward.

**Points:** 5

**Rubric (1 point each):**

1. Writing the contract first forces decisions about edge cases (such as zero retention and wrong input types) to be made by the person, not inherited from the model.
2. Tests written before seeing the implementation capture the person's intent independently of the code.
3. Running the tests on the assistant's implementation, personally, shows whether it satisfies the specification; failures can expose gaps in the specification itself.
4. The developer can ask for a deliberately wrong implementation that still passes the tests; if one exists, the test suite is too weak.
5. Building a baseline first gives the developer a concrete reference to name differences in behavior between versions, which is what auditing requires.

**Source:** Build It, Use It, Ship It

## ES-ch14.7

A Python function validates a retention-day count with `isinstance(days, int) and days >= 0`. Explain what happens for the inputs True, 0, 30.0 and -1, why exact type checking such as `type(days) is int` changes one of these results, and what a test suite needs to include to detect the isinstance version.

**Points:** 5

**Rubric (1 point each):**

1. True is accepted by the isinstance version because bool is a subclass of int in Python, so True behaves as 1.
2. 0 is accepted, which is correct if zero retention is a legitimate design intent.
3. 30.0 is rejected because a float is not an int instance, and -1 is rejected by the range test.
4. `type(days) is int` rejects True because type(True) is bool, not int.
5. The suite needs a test that expects True to be rejected, and ideally the zero and negative boundary cases, so that an isinstance implementation fails.

**Source:** Tear down the validator

## ES-ch14.8

A validator treats a field as missing if `not record.get(field)` is true. Describe two kinds of wrong behavior this causes for a record with `retention_days: 0` and for a record with `owner: "   "` (spaces only), and propose a better missing-field test and how to treat blank text.

**Points:** 5

**Rubric (1 point each):**

1. Zero is falsy, so a deliberate zero-day retention value is wrongly reported as missing.
2. A whitespace-only string is truthy and so is accepted as present although it names no one.
3. The better presence test distinguishes absence (key not present or value is None) from other values, so zero is retained as a legitimate value.
4. For text fields, normalize with strip() and then reject empty strings.
5. These are narrow structural fixes; they still cannot tell whether a non-empty owner is a real accountable person.

**Source:** Tear down the validator

## ES-ch14.9

A validator for data labels uses an allowlist (public, synthetic, internal) and sends anything else to human review. Explain why an allowlist routing unknown values to review is a conservative design, what costs it imposes, and what it cannot establish about the data.

**Points:** 5

**Rubric (1 point each):**

1. When the machine cannot classify a label, sending the decision to a person is the safe default.
2. An allowlist catches categories nobody listed in advance, unlike a denylist.
3. Costs include reviewer workload and false alarms, such as a case-sensitive comparison sending "Public" to review.
4. The check cannot determine whether an unknown label is actually sensitive, nor whether an allowed label such as "internal" is appropriate for the specific use.
5. It also does not verify that the data was assigned its label correctly in the first place.

**Source:** Tear down the validator

## ES-ch14.10

Explain why a governance validator should refuse only what it can refuse exactly, and what kinds of judgment it should leave to people. Give two examples of checks that belong in code and two judgments that belong to humans.

**Points:** 5

**Rubric (1 point each):**

1. Code is reliable on exact, mechanical conditions, such as required fields present, correct types and ranges, and membership in a list.
2. Judgments about adequacy, such as whether an owner line names an accountable person or an evaluation line is a real test, depend on context that string checks cannot encode.
3. A deny-list of "bad phrases" would be evaded by rewording, so it gives false assurance.
4. Examples in code: type and range checks on retention; flagging unknown data classes. Examples for humans: whether an owner has accepted the role; whether an evaluation tests the relevant harm.
5. A validator that claims only what it checks is more honest than one that implies quality assessment.

**Source:** Tear down the validator

## ES-ch14.11

A validator adds the issue "external action approval" whenever a record's `external_write` value is truthy. Describe what this check does and does not accomplish, and name two Python pitfalls in relying on truthiness for such a flag.

**Points:** 5

**Rubric (1 point each):**

1. It marks that an external action is involved and routes the record to an approval control.
2. It does not verify that approval was obtained, who approved, or what the external target is.
3. Non-empty strings such as "no" and "false" are truthy, so a mistyped flag can trigger or fail to trigger the check.
4. Values like 0, None or an empty string are falsy and will silently skip the check, so required Boolean type enforcement is needed.
5. The flag is a routing signal; a separate control must bind approval to the exact proposed action.

**Source:** Tear down the validator

## ES-ch14.12

Construct a record that passes a structural validator (all fields present and well formed) but is weak as governance, and for each of three vague lines write the question a named person would need to answer and the act that would answer it.

**Points:** 5

**Rubric (1 point each):**

1. The example includes vague entries such as owner "everyone", evaluation "looks fine" and incident contact "team".
2. Owner: "Who personally accepts responsibility and can pause the workflow?" answered by a named person confirming acceptance.
3. Evaluation: "What outcomes were tested, by whom, on what data, and what happens on failure?" answered by a documented test with criteria and sampling.
4. Incident contact: "Can an affected person reach a human who can act?" answered by sending a labeled test report and observing acknowledgment within the stated time.
5. The structural validator is not defective for passing such a record; its contract is narrow, which is why human review must interrogate meaning.

**Source:** Complete, reviewable, and still weak

## ES-ch14.13

A reviewer is writing up what a governance validation run and a test of an incident-reporting route established. Explain how to word each claim so it is no stronger than the evidence behind it. Illustrate with claims about the incident route at three or more levels of evidence, from weakest to strongest, naming the evidence each level needs.

**Points:** 5

**Rubric (1 point each):**

1. The principle: the wording of a claim should match what was actually done, so a script that checked structure "reported" presence and did not "confirm" anyone's acceptance.
2. Weakest level: a name or role appears in a document, which supports only "is listed".
3. Next level: the named person has said they accept the role, which supports "has agreed".
4. Stronger level: the route was run and observed to work, for example a clearly labeled test report was acknowledged within the stated time.
5. Strongest level: the reviewer inspected the system or store directly, and claims about systems that were not inspected must stay at the weaker levels.

**Source:** Complete, reviewable, and still weak

## ES-ch14.14

A summarizer was approved for public course notes. Months later it is pointed at student-submitted essays. Explain how a well-written purpose statement helps detect this change, why the change needs fresh review even if the model and prompt are unchanged, and what a purpose line like "use AI" fails to do.

**Points:** 5

**Rubric (1 point each):**

1. A precise purpose bounds what the system is for, so a new use can be recognized as out of scope.
2. Student essays involve different people, different data classes and different consequences, so risk changes even with identical model and prompt.
3. The change should trigger review of data classes, consent, retention, evaluation and who is affected.
4. "Use AI" excludes nothing, so no later use can be flagged as beyond scope.
5. Scope creep tends to go unnoticed unless the purpose is stated precisely and reviewed when use changes.

**Source:** A register makes questions inspectable

## ES-ch14.15

Rewrite the vague promise "monitor quality and intervene if needed" as an operational control for an LLM tool that publishes summaries. Your rewrite should specify the signal, threshold, owner, response, scope and recovery condition, and you should explain what makes a threshold testable by a stranger.

**Points:** 5

**Rubric (1 point each):**

1. Signal: an observable measure, such as published summaries containing a claim without a supporting source.
2. Threshold and owner: a numeric or event trigger (for example any single such claim) and a named person responsible for acting.
3. Response and scope: publication pauses, affected drafts are examined, and the scope of what pauses is defined.
4. Recovery condition: work resumes only after correction and a repeated check passes.
5. A stranger can tell from the record whether it fired because the signal, trigger and response are observable and unambiguous.

**Source:** Owners, thresholds, and bounded responses

## ES-ch14.16

An LLM service processed 20,000 requests last month and an automated check passed 99.5% of them. A manual review of the failures found that 2 of them exposed customers' personal data. Calculate how many failures there were, explain why the pass rate alone is an inadequate governance signal, and propose a better trigger design.

**Points:** 5

**Rubric (1 point each):**

1. 0.5% of 20,000 is 100 failures.
2. The aggregate rate weights all failures equally, so rare severe events are hidden inside the average.
3. Two disclosures among 100 failures are a severity category the pass rate does not display.
4. Severe harms warrant a stop-on-first-occurrence trigger and separate monitoring by harm category.
5. Less severe failures can use a trend or rate threshold, and the trigger design should specify who can pause and what the response is.

**Source:** Owners, thresholds, and bounded responses

## ES-ch14.17

An organization names an incident owner for an AI pipeline but rewards on-time delivery and penalizes delays. Explain why the owner cannot effectively govern in that environment and what must change for the role to work.

**Points:** 5

**Rubric (1 point each):**

1. Authority to pause must be explicit; a nominal owner who has to ask permission cannot respond quickly.
2. If delay is penalized, people will avoid using pause authority, so it exists only on paper.
3. The cost of pausing should be assigned in advance to the organization, not to the individual who triggers it.
4. Escalation must be defined for cases when the owner is unavailable, implicated or lacks expertise.
5. Incentives and metrics should be aligned so that exercising the control is not punished, and the team should test that the pause actually works.

**Source:** Owners, thresholds, and bounded responses

## ES-ch14.18

The incident contact for an AI service is unreachable during a possible data exposure and nobody acknowledges an alert within the declared window. Describe what a well-designed response structure does, what it means if no backup exists, and why the AI system should not name itself as the responsible party.

**Points:** 5

**Rubric (1 point each):**

1. A named backup with delegated pause authority is alerted after the acknowledgment window, pauses the service and records why.
2. If there is no backup, the exercise has found an unresolved dependency that people must fix.
3. The AI system cannot accept accountability, so naming itself responsible leaves no accountable person.
4. The system may safely stop its own work as a default, while responsibility remains with an authorized person or organization.
5. The rehearsal result should be fed back into the governance record as a change (add a backup, shorten the window) instead of left as an observation.

**Source:** Worked incident rehearsal

## ES-ch14.19

An AI system publishes a summary stating a wrong assignment deadline. Its evaluation was an audit confirming that each cited source identifier exists. Explain why the audit failed to protect against this harm and describe three changes that would address it.

**Points:** 5

**Rubric (1 point each):**

1. The audit checked that a citation exists, not that the cited material supports the claim.
2. The harm mechanism is reliance on a false date, and the audit did not address that mechanism.
3. Change one: add a check for support of consequential claims, by a person or an entailment-style method.
4. Change two: pause publication and correct existing copies, with a record of copies that cannot be reached.
5. Change three: assign a named owner with pause authority and define the acknowledgment, triage and escalation steps for the reporting route.

**Source:** Worked incident rehearsal

## ES-ch14.20

A team writes a governance plan before building an AI feature. After an incident they discover one of the plan's decisions was wrong. Explain why designing governance before implementation does not mean it is frozen, and describe how the record should show what changed.

**Points:** 5

**Rubric (1 point each):**

1. Design before implementation sets the starting decisions; evidence from operation can show that one was inadequate.
2. An incident can reopen an earlier choice, such as an evaluation that did not test the harm that occurred.
3. The record should state what the incident revealed, which earlier decision it reopened, and what changed.
4. Changes should name who made them and when, so the revised decision has an owner.
5. A record that is never revised after an incident suggests that the feedback loop from operation to design is not working.

**Source:** Worked incident rehearsal

## ES-ch14.21

A register states "retention: 30 days" for user prompts sent to an LLM application. List the copies of the data that may exist beyond the primary store, explain why the stated number does not show that deletion follows it, and describe how to verify deletion for the copies the team controls.

**Points:** 5

**Rubric (1 point each):**

1. Copies include application logs, caches, backups, exported reports, repository or ticket history, incident records, and the model provider's handling under its own terms.
2. The number states a policy for one store; other copies follow their own lifecycles and may outlast it.
3. Define for each class when the retention clock starts, who deletes, and how deletion is checked.
4. Test by inserting a labeled record, running the lifecycle, and inspecting the stores the team controls.
5. State what remains unverified, such as the provider and backups, instead of claiming erasure everywhere.

**Source:** Retention is a lifecycle

## ES-ch14.22

A design document sets retention to zero days for a workflow that handles customer messages. Explain what zero could mean, what it does not guarantee, and why a validator should not report zero as a missing value.

**Points:** 5

**Rubric (1 point each):**

1. Zero could mean delete immediately after the task, do not persist application data, or retain only de-identified evidence.
2. Data still exists transiently in memory and in any third-party processing, subject to the provider's terms.
3. A stated value is a design intent and does not show that no copies exist.
4. A validator that treats falsy values as missing wrongly reports zero as absent; it should test for absence directly.
5. The design document should define what zero means so that reviewers can check it.

**Source:** Retention is a lifecycle

## ES-ch14.23

A team deletes a customer's row from its application database after a deletion request. The same customer's data also fed a vector index, a weekly summary and a log of hashed e-mail addresses. Explain why the deletion may be incomplete and how the team should handle derived data.

**Points:** 5

**Rubric (1 point each):**

1. Derived artifacts such as embeddings and summaries can retain or reveal source information.
2. Hashes of guessable identifiers can be matched against a small known set, so they can still identify the person.
3. The team needs lineage records showing which artifacts derive from which sources.
4. Deletion should be tested end to end with labeled data, and each store marked verified or unverified.
5. Copies the team cannot alter, such as immutable backups, should be listed and disclosed as a limitation.

**Source:** Retention is a lifecycle

## ES-ch14.24

Compare three approaches to logging an AI agent's actions: keep everything forever, keep nothing, and keep a minimal audit record. Describe the trade-offs and propose what the minimal record should contain.

**Points:** 5

**Rubric (1 point each):**

1. Keeping everything improves investigation and replay but increases privacy exposure and breach impact.
2. Keeping nothing minimizes retained risk but makes incident investigation and accountability difficult.
3. A minimal audit record can include operation identity, the policy decision taken, references to evidence stored elsewhere, an error category and responsible roles.
4. Sensitive payloads should be kept only when justified and should be protected and separated.
5. The audit record itself needs a retention decision and access controls.

**Source:** Retention is a lifecycle

## ES-ch14.25

A team claims two LLM agents are equally risky because both score 92% on the same 500-item evaluation. Agent A reads public notes, drafts locally and needs a person to publish. Agent B reads internal HR records, publishes externally and keeps year-long traces. Argue which needs stronger governance, calculating each agent's error count, and say why accuracy does not settle the question.

**Points:** 5

**Rubric (1 point each):**

1. Each agent made 40 errors, since 8% of 500 is 40.
2. Agent B has a broader action surface, since it writes externally, and a longer exposure window.
3. B handles more sensitive context, so each error can do more damage.
4. Accuracy describes selected outputs under selected trials; it does not describe the consequences, reversibility or who is affected.
5. Architecture choices such as data minimization, human publication and short retention shape harm before any score is computed, so ethics should not be added after model selection.

**Source:** Who bears the error

## ES-ch14.26

Two summarizers make the same number of deadline errors on the same test set. One states unsupported deadlines. The other omits the deadline when sources conflict. Explain who bears each kind of error, why identical accuracy does not tell which to prefer, and who should make the choice.

**Points:** 5

**Rubric (1 point each):**

1. Users who plan around a wrong date bear the unsupported-deadline error.
2. Users who must ask for clarification, and those who handle their questions, bear the omission.
3. The accuracy figure hides the type of error and so cannot choose between them.
4. Preferring one error is a value judgment about whose costs count.
5. The choice should belong to the party accountable for the policy the tool serves, made and recorded deliberately.

**Source:** Who bears the error

## ES-ch14.27

A classifier is applied to two groups with base rates of 50% and 20%. For both groups the true positive rate is 0.8 and the false positive rate is 0.2. Calculate the positive predictive value for each group, explain what this shows about fairness criteria, and say what follows for decision-making.

**Points:** 5

**Rubric (1 point each):**

1. For the first group, 40 true positives and 10 false positives per 100 people give precision 0.80.
2. For the second group, 16 true positives and 16 false positives per 100 give precision 0.50.
3. Equal error rates across groups coexist with unequal precision when base rates differ.
4. Several reasonable fairness criteria cannot all hold together at once unless prediction is perfect or base rates match.
5. Selecting a criterion is a values decision with an owner, who must record whose errors count and what evidence would change the choice.

**Source:** Who bears the error

## ES-ch14.28

A hiring tool ranks applicants. The team reports 90% overall agreement with past hiring decisions, measured on a set built from people who were hired. Identify who bears false positives and false negatives, critique the evaluation set, and list questions about distribution of burden the team should ask.

**Points:** 5

**Rubric (1 point each):**

1. Applicants wrongly rejected bear false negatives; recruiters and others bear the cost of reviewing false positives.
2. An evaluation set built only from hired people hides how the model treats those never hired.
3. Overall agreement says nothing about how errors fall across subgroups.
4. Questions include who benefits, who corrects errors, who is absent from development examples, who can opt out, and who can reach a human.
5. Whether a rejected applicant can reach a human with power to change the outcome is a governance property the accuracy figure does not capture.

**Source:** Who bears the error

## ES-ch14.29

Explain the difference between a generic risk statement and a concrete harm description in an AI risk register. Write an example of each for an AI summarizer of course notes and say what the concrete one lets a team do.

**Points:** 5

**Rubric (1 point each):**

1. A generic statement such as "there may be bias or privacy concerns" is not tied to a person, mechanism or consequence and can fit any system.
2. A concrete statement names who is affected, how the harm arises and what the consequence is.
3. Example: a student relies on an AI summary giving a wrong deadline and misses the real one.
4. It lets the team design a test, set a threshold, assign an owner and choose a mitigation that targets that mechanism.
5. It also enables questions about who pays for the error and who could have prevented it.

**Source:** Who bears the error

## ES-ch14.30

A team plans to consult people affected by a new AI workflow. Describe how to design consultation so it is real, including who to include, what can change as a result, how to ask questions, and what to promise.

**Points:** 5

**Rubric (1 point each):**

1. Identify directly affected people, maintainers of the surrounding work, domain experts and groups usually missing from design decisions; one convenient person cannot stand in for all.
2. Consultation counts only if the answers could change purpose, boundaries, retention or the decision to automate.
3. Participation should be voluntary where appropriate, with explanation of what is recorded, how it is used and whether declining has consequences.
4. Questions should invite disagreement: what would be unacceptable, what must never enter the workflow, what would make you withdraw support.
5. Do not promise every request will be adopted; explain how decisions and conflicts will be recorded.

**Source:** Consultation and recourse are people's work

## ES-ch14.31

A team uses an LLM to role-play affected stakeholders, and the model answers agreeably. Explain what this can and cannot show, and how the team's records should treat simulated responses.

**Points:** 5

**Rubric (1 point each):**

1. Role-play can reveal unclear explanations and missing questions.
2. It cannot show what real people think; the model produces plausible text, not testimony.
3. Invented agreement is not consent, which only an informed person can give.
4. Simulated responses should be labeled as simulation in the record.
5. The record should state which real consultation remains pending and which actions are prohibited until it occurs.

**Source:** Consultation and recourse are people's work

## ES-ch14.32

After a stakeholder interview, a team uses an LLM to summarize what participants said. Later one participant withdraws permission for their contribution. Describe how the team should keep actual statements distinct from summaries, and what the withdrawal requires of the team's data practices.

**Points:** 5

**Rubric (1 point each):**

1. Keep the participant's actual words or notes separate from AI-generated summaries.
2. Return a summary to the participant for confirmation where appropriate.
3. Record concrete design changes and unresolved concerns that came from the conversation.
4. To honor a withdrawal, the team must know which artifacts derive from the participant's contribution, such as quotes, embeddings and evaluation examples.
5. Where removal is impossible, for example from an immutable backup, the limitation should be disclosed to the participant.

**Source:** Consultation and recourse are people's work

## ES-ch14.33

An LLM drafts a plain-language explanation of an AI workflow for affected people. Describe what the explanation should include, why a person must check it against the real system before sharing, and what a careful check looks for.

**Points:** 5

**Rubric (1 point each):**

1. It should cover what the workflow receives, what it produces, where a person decides, what is retained and how to report a problem.
2. Fluent simplification can omit exactly the external write or retention detail that matters to the reader.
3. The checker compares each claim in the draft with the actual system configuration.
4. The check looks for omitted data flows, overstated human review and understated retention.
5. Being readable is not evidence of accuracy, so the checker should be someone who knows the system.

**Source:** Consultation and recourse are people's work

## ES-ch14.34

Describe the components of a recourse path for people affected by an AI-assisted decision, and explain why a contact e-mail address is not enough.

**Points:** 5

**Rubric (1 point each):**

1. A discoverable channel with guidance on what information helps without forcing the person to reveal more private data.
2. An acknowledgment rule, a triage owner and an urgent-stop trigger.
3. Investigation access to the contested output, inputs and policy, and power to correct the outcome.
4. Escalation when the first contact cannot resolve the issue, including a second route when the original owner is conflicted.
5. An email address alone has no staffing, authority, timing or escalation behind it, so it can be an inbox nobody owns.

**Source:** Consultation and recourse are people's work

## ES-ch14.35

Explain why different harms from an AI error need different remedies, using three examples, and state the five questions a team can ask to test whether a recourse route works.

**Points:** 5

**Rubric (1 point each):**

1. Correcting a displayed summary does not repair a decision already made from it.
2. Removing personal data from an active store does not recall a public copy.
3. Explaining a model's reasoning does not restore an opportunity that was denied.
4. Test questions: can the person challenge the result, obtain an appropriate explanation, reach a human who can correct the record, see downstream copies updated, and appeal beyond the original owner?
5. The affected person should be asked what meaningful correction would look like, within institutional limits.

**Source:** Consultation and recourse are people's work

## ES-ch14.36

Describe how a team should make contesting an AI-assisted decision practical: what it must preserve, who reviews, what the reviewer can do, how it handles conflicts of interest, and how it closes the loop with engineering.

**Points:** 5

**Rubric (1 point each):**

1. Preserve the contested output, input provenance where lawful, the applicable policy and the human decision record.
2. Reviewers must have the power to change the result.
3. Provide a second route when the original owner is conflicted.
4. State response times only when the team can meet them.
5. If the same class of report keeps recurring while only the reply changes, the process is absorbing complaints; fix the system.

**Source:** Consultation and recourse are people's work

## ES-ch14.37

A student reports that a published AI summary contradicts the official schedule. Investigation shows the student compared it with an outdated schedule and the published date is correct. Explain how a well-designed contest route should respond and what this shows about contestability.

**Points:** 5

**Rubric (1 point each):**

1. Acknowledge and investigate the report rather than dismiss it.
2. Explain the evidence supporting the published date to the reporter.
3. Preserve the challenge in the record.
4. Check whether the wording of the summary created reasonable ambiguity.
5. Contestability means a person can trigger genuine reconsideration; it does not mean every challenge succeeds.

**Source:** Worked incident rehearsal

## ES-ch14.38

An AI service produces 150 deadline claims a day. Policy requires every claim to be reviewed by a person before publication. Reviewers have two hours per day at four minutes per claim. Calculate the daily gap, explain what this means for the control, and propose how to respond.

**Points:** 5

**Rubric (1 point each):**

1. Reviewers can examine 30 claims a day (120 minutes divided by 4).
2. The backlog grows by 120 claims a day (150 minus 30).
3. A control that cannot be performed is not functioning as a control, even if it reads well in the register.
4. Options include narrowing the feature, such as extracting dates with visible source passages, or adding review capacity.
5. Publishing unreviewed claims while describing all as reviewed would misstate the control; throughput should be limited to review capacity.

**Source:** Worked incident rehearsal

## ES-ch14.39

After an AI-generated summary is found to be wrong, describe a sound correction sequence: what to do first, how to find and fix copies, how to communicate, and what to keep open.

**Points:** 5

**Rubric (1 point each):**

1. Pause publication of affected items and preserve evidence, including source identifiers, the output, approvals and publication records.
2. Identify cause, such as an evaluation that checked citation existence but not support.
3. Locate and correct copies in systems the team controls; acknowledge copies outside its control as a limitation.
4. Issue the correction through the same channel that carried the error, and have the approver review the changed process.
5. Keep the reporting route open in case the correction missed an effect, and record the governance changes made.

**Source:** Worked incident rehearsal

## ES-ch14.40

A company wants to use an LLM to rank employees for promotion. The evaluation cannot observe real career outcomes, employees have not been consulted, the data boundary is unclear and no manager has agreed to own the decisions. Argue for what the team should do, including options other than full deployment, and what to record.

**Points:** 5

**Rubric (1 point each):**

1. Defer: the preconditions for responsible use are missing (consultation, ownership, a measurable consequential outcome, a known data boundary).
2. Technical feasibility or a good proxy score is not a reason to proceed.
3. Narrowing is an option, such as limiting the tool to organizing documents rather than ranking people, or using synthetic data.
4. Record why the team deferred and what evidence or capacity would justify reconsideration.
5. A record that can only say "go" is a rubber stamp; stopping or narrowing is a legitimate result.

**Source:** When deferral is the responsible output

## ES-ch14.41

An agent with access to a CRM can send e-mails to customers on its own, and leadership is worried about errors. List four ways to narrow the workflow and explain what each reduces.

**Points:** 5

**Rubric (1 point each):**

1. Draft for human sending instead of autonomous sending: adds review and reversibility before external effects.
2. Synthetic or test customer data in pilots: removes exposure of real people.
3. Shorter retention of traces: reduces privacy exposure over time.
4. Removing high-impact actions such as refunds until outcome checks exist: limits severe harm.
5. A disclaimer alone is not a narrowing, because it shifts burden to recipients without reducing risk.

**Source:** When deferral is the responsible output

## ES-ch14.42

A vendor says "a human is in the loop" for a system that produces 500 decisions an hour reviewed by one person clicking Approve. Explain what is missing from the claim and how to specify a meaningful human review step.

**Points:** 5

**Rubric (1 point each):**

1. "Human in the loop" names a person but not a control: the task, evidence, authority, time budget and stop rule must be defined.
2. At 500 items an hour (about 7 seconds each) the reviewer cannot meaningfully assess content.
3. The reviewer needs authority to reject and information needed to judge.
4. Throughput should be limited to review and response capacity.
5. Review quality should be measured, for example by seeded errors or sampling, to detect rubber-stamping.

**Source:** When deferral is the responsible output

## ES-ch14.43

Describe four distinct ways a governance record for an AI system can look complete while the system remains ungoverned. Consider the roles the record names, the mitigations it offers, the triggers it sets, and the people it claims to have consulted. Give a one-line concrete example of each.

**Points:** 5

**Rubric (1 point each):**

1. Roles filled with generic labels (such as "the team") so that no identifiable person has accepted responsibility or holds authority to act.
2. A mitigation that does not address the stated harm mechanism, for example an answer-accuracy test offered for a risk of stored data being exposed.
3. A trigger with no observable signal or measurement procedure, such as "act when quality falls", so nobody can tell whether it fired.
4. Consultation that is simulated or token, such as model-generated stakeholder reactions presented as feedback from people, or a completed form treated as legal clearance.
5. Gives a concrete example for each and explains why the record looks fine while the system is not governed.

**Source:** Governance failure patterns

## ES-ch14.44

A chatbot logs users' health questions for a year. The register lists the harm as exposure of sensitive health information from the retained logs, and the mitigation as a weekly accuracy test of the chatbot's answers. Analyze the mismatch and propose controls that fit the harm.

**Points:** 5

**Rubric (1 point each):**

1. The accuracy test addresses answer correctness, not exposure of stored data.
2. A mitigation must match the mechanism of the stated harm.
3. The accuracy test may be valuable for another risk, but does not reduce this one.
4. Fitting controls include shortening or eliminating retention, redacting health details before logging, and restricting access to logs.
5. The register should name an owner and an observable signal, such as audit of access to the logs, for the harm that was actually listed.

**Source:** Governance failure patterns

## ES-ch14.45

Explain what it means for a governance register to be a control plane rather than documentation. Give three examples of effects a register entry could have on a running AI system.

**Points:** 5

**Rubric (1 point each):**

1. A control plane's contents determine what the system is allowed to do; documentation only describes it.
2. Example: changing an entry pauses execution or removes a tool permission.
3. Example: revoking an approval stops an action bound to it, or shortening retention triggers deletion.
4. Example: changing the evaluation requirement blocks release until the new check passes.
5. If updating the register changes nothing in the system, it is only documentation.

**Source:** Build It, Use It, Ship It

## ES-ch14.46

Draft the structure of an honest sign-off for a governance record, explaining what each part contains and why the "not checked" part matters. Also say when withholding a signature is the right result.

**Points:** 5

**Rubric (1 point each):**

1. Checked: which register lines the signer confirmed against the running system and which owners confirmed their roles.
2. How: the method, such as own tests, exercising the route, inspecting stores, conversation with an owner, or help from an AI assistant and which parts.
3. Not checked: unverified systems like providers and backups, behavior under real load, consultation not done.
4. Not claiming: that the workflow is ethical, consented to or compliant, or that "ready for review" means someone reviewed.
5. Withholding is right when the evidence does not support signing, and the correct action is to narrow or defer the workflow rather than reword the sign-off.

**Source:** Build It, Use It, Ship It

## ES-ch14.47

An AI-assisted workflow publishes a wrong figure. The user who reported it, the content owner, the vendor of the drafting tool, the provider of the underlying model and the institution that supplied the data all made choices that mattered. Explain how responsibility distributes and what a team should record.

**Points:** 5

**Rubric (1 point each):**

1. In socio-technical systems each party's choice may be necessary while none is sufficient alone.
2. Naming one owner does not remove dependencies on the others.
3. The record should show for each dependency whether it was checked or only assumed.
4. A useful question is what change made before the incident would have prevented it.
5. The answer should be an action someone takes, not a sentence someone writes.

**Source:** Governance failure patterns

## ES-ch14.48

An organization's policy forbids pasting customer data into public chatbots, yet employees are rewarded for speed and those who raise concerns are called obstructive. Explain why the policy is likely to fail and what changes would make it work.

**Points:** 5

**Rubric (1 point each):**

1. People do what an organization rewards, not what its documents say.
2. If speed is rewarded and listening is not, the stated policy and actual behavior diverge.
3. Authority to pause or object is nominal if exercising it is penalized.
4. Time and resources for review and consultation must be allocated.
5. Measures include aligning incentives, protecting those who raise concerns, giving approved tools that fit the work, and monitoring actual practice.

**Source:** Governance failure patterns

## ES-ch14.49

A team deploys a coding agent that can read files, run shell commands and call external services in developers' environments. Describe how to reduce its risk through permissions and handling of untrusted input, and how to connect those measures to a governance record.

**Points:** 5

**Rubric (1 point each):**

1. Apply least privilege: grant only the permissions the task needs and keep the agent out of broader credentials.
2. Require approval for actions with side effects, and avoid blanket permanent approvals.
3. Treat text from web pages, documents or tool output as data, because it may contain instructions meant to hijack the agent.
4. Prefer sandboxing and restricted environments to limit damage.
5. In the register tie each measure to a named owner, a monitoring signal and an incident response, instead of copying generic security prose.

**Source:** Anthropics

## ES-ch14.50

A developer records a decision note for an AI-assisted policy change. Describe what the note should contain, why it separates the model's proposal from human input, and how a reader can tell whether a person actually reviewed it.

**Points:** 5

**Rubric (1 point each):**

1. It records what the model proposed, what a person added or corrected, the evidence supporting the recommendation, and whose interests are served or disadvantaged.
2. It ends with a named human recommendation.
3. Separation shows where a person changed substance and where they merely accepted the draft.
4. Sentences that simply repeat the model are flagged, since repetition is not review.
5. Evidence cited should be independent of the model's fluency, and the note should show the person's reasoning.

**Source:** Build It, Use It, Ship It

## ES-ch14.51

A team announces "We are compliant" after completing an internal AI-use register. Explain why that statement is unsupported, and distinguish the roles of structural checks, legal review and ethical judgment.

**Points:** 5

**Rubric (1 point each):**

1. A completed internal form is not regulatory approval.
2. Lawful basis for processing personal data is a legal determination that depends on law, jurisdiction and facts.
3. Some regulations require specific processes, such as impact assessments, that must actually be carried out.
4. Legal compliance is not the same as ethical acceptability; lawful practices can still harm people.
5. Structural checks catch missing information, legal review addresses obligations, and ethical judgment involves affected people and consequences, with each leaving open questions the others cannot answer.

**Source:** Governance failure patterns

## ES-ch14.52

A policy says records are deleted "30 days after the case is created". A case was created on 10 January 2027 and last used on 20 February 2027 (not a leap year). Compute the deletion date under creation-based and last-use-based readings, state the difference, and list what a retention policy should specify.

**Points:** 5

**Rubric (1 point each):**

1. Creation-based: 30 days after 10 January is 9 February 2027.
2. Last-use-based: 30 days after 20 February is 22 March 2027.
3. The two interpretations differ by 41 days.
4. The policy should state when the clock starts, who performs deletion, and how deletion is checked.
5. It should also cover all copies, including backups, derived data and provider-held data.

**Source:** Retention is a lifecycle

## ES-ch14.53

A company sends customer messages to an external LLM provider's API and records "retention: 0 days" because its own systems store nothing. Critique that entry and say what the company should record instead.

**Points:** 5

**Rubric (1 point each):**

1. Data sent to the provider is a copy handled under the provider's terms.
2. The company should read the terms for its service tier and record unknowns instead of assuming zero.
3. Zero retention in the company's own systems does not establish zero retention elsewhere.
4. The register should distinguish stores the company inspected from those it relies on others' statements about.
5. Using a provider does not remove the company's responsibility to its customers for the data it chose to send.

**Source:** Retention is a lifecycle

## ES-ch14.54

A team compares three agent actions: saving a draft in a private workspace, sending an e-mail to external customers, and publishing to an indexed public website. Explain how reversibility and action surface should influence governance, and why model accuracy alone is not enough.

**Points:** 5

**Rubric (1 point each):**

1. Private drafts can be deleted without others having seen them, so they are the easiest to reverse.
2. E-mails and public posts escape the team's control once sent; recipients and crawlers keep copies.
3. Less reversible actions justify stronger review, narrower scope and tighter approval.
4. A rollback plan limits damage when errors occur, whatever the accuracy.
5. Equal accuracy across actions does not mean equal consequences, so oversight should scale with the consequences.

**Source:** Who bears the error

## ES-ch14.55

A developer asks an LLM to critique a register entry, with instructions not to rewrite it and to list group-named owners, thresholds without signals, mitigations that do not address the named harm, and one undocumented decision. Explain why this prompt is better than asking the model to improve the entry, and how to treat the model's findings.

**Points:** 5

**Rubric (1 point each):**

1. A rewrite tends to smooth over weak lines, hiding vagueness instead of exposing it.
2. The critique keeps authorship and decisions with the person.
3. The prompt targets specific known failure patterns, which makes the output checkable.
4. Each finding should be verified against the entry, since a finding that cannot be located may be a plausible guess.
5. The absence of findings does not prove the entry is sound.

**Source:** Build It, Use It, Ship It

## ES-ch14.56

During stakeholder conversations, a student says they care more about being quoted without context than about accuracy, and a maintainer says an appeals channel would create unpaid support work. Explain how such concerns should influence the design and why prepared questionnaires may miss them.

**Points:** 5

**Rubric (1 point each):**

1. Open-ended listening can reveal concerns outside the categories the designers anticipated.
2. The student's concern may change data classes, quoting rules or purpose.
3. The maintainer's workload concern shows a recourse route must be staffed to function.
4. Concerns should be recorded, with design changes made or the reasons for declining them.
5. Unresolved concerns should be tracked and, where serious, should constrain the workflow until addressed.

**Source:** Consultation and recourse are people's work

## ES-ch14.57

A register's roles include owner, approver and incident contact. Explain what each is for, why they should be distinct where possible, and what goes wrong if all three are assigned to one person to complete the form.

**Points:** 5

**Rubric (1 point each):**

1. The owner is accountable for the workflow as a continuing system.
2. The approver decides whether a proposal or change goes ahead.
3. The incident contact is where people report problems and starts the response.
4. Separate roles provide independent review and cover for absence.
5. One person in all roles removes independence, creates a single point of failure and may be implicated in the incident.

**Source:** A register makes questions inspectable

## ES-ch14.58

A company argues that because an AI system cannot be sued, no one needs to be accountable for its outputs. Explain why this is wrong, and what accountability for AI-assisted decisions should look like.

**Points:** 5

**Rubric (1 point each):**

1. An AI system is not a legal person; responsibility falls on natural persons and organizations.
2. Choosing to deploy and rely on a system is a human decision with consequences.
3. Someone must be able to answer for outcomes, correct errors and stop the system.
4. The accountable party should be named and have authority and resources.
5. A system may stop its own work as a safe default, but this does not move accountability to the system.

**Source:** Who decided? Five choices that exist before the form does

## ES-ch14.59

A hollow governance record has a green validator status but no working response. Describe how a team can test whether its incident route works, and what a failing result would look like.

**Points:** 5

**Rubric (1 point each):**

1. Send a clearly labeled test report to the named incident contact.
2. Check whether it is acknowledged within the stated time.
3. A failing result is no acknowledgment, an unreachable contact, or an acknowledgment with no one able to act.
4. Test the backup path and the escalation when the first contact is unavailable.
5. Record the date, the result and any fixes; this upgrades the claim from "a contact is named" to "the route was exercised and worked".

**Source:** A register makes questions inspectable

## ES-ch14.60

A retention-day validator must accept non-negative integers (including 0) and reject negative numbers, Booleans, strings and floats. Describe two plausible wrong implementations that a good test suite must catch, explain the specific inputs that expose each, and explain why passing only a demonstration case is not enough.

**Points:** 5

**Rubric (1 point each):**

1. Wrong version one accepts anything that isinstance(int) accepts, so True passes as one day; the test input is True.
2. Wrong version two treats any falsy value as missing, so a deliberate zero is rejected; the test input is 0.
3. A demonstration case with a typical value like 30 and an empty record passes under both wrong versions.
4. Boundary and type cases are needed: zero, negative, Boolean, string and float.
5. A suite should be checked against deliberately wrong implementations to confirm it can tell right from wrong.

**Source:** Tear down the validator

## ES-ch14.61

A developer's validator tests all pass. State what this establishes and what it does not, and describe two things the developer should do beyond running the tests to understand the result.

**Points:** 5

**Rubric (1 point each):**

1. The tests establish that the exercised behaviors work as the tests specify.
2. They do not establish reliability for untested inputs, the adequacy of the specification, or permission to deploy.
3. The developer should walk through one passing case from input to returned status without relying on an assistant's explanation.
4. The developer should explain why one raised error belongs to the contract, as refusing invalid input is part of what the validator promises.
5. The developer should record the commands, outputs and interpretation, and test the strongest claim in the write-up by asking what evidence, and whose action, actually supports it.

**Source:** Verify and reflect
