# Chapter 15: Supervised capstone

## ES-ch15.1

A packet consists of ten Markdown files, each containing sixty copied `x` characters. Explain why `validate_packet` reports `structurally_complete: True` for it, what the example shows about what a mechanical check can and cannot establish, and what the empty-folder case adds.

**Points:** 5

**Rubric (1 point each):**

1. States that all ten named Markdown files exist inside the packet and exceed forty stripped characters, which is all the validator requires.
2. States that nothing in the files demonstrates a need, boundary, implementation, controlled failure, independent result, consenting owner, or defensible decision.
3. Explains that structure can be checked mechanically while substance must be established through connected evidence and accountable judgment, so the pass is the validator doing its honest job rather than a trick played on a weak validator.
4. Notes that an empty folder reports ten missing artifacts while the ten meaningless files pass, so the pair of fixtures shows that presence and length do not establish substance.
5. Says the counterexample keeps the capstone from becoming a scavenger hunt in which file presence substitutes for learning.

**Source:** Chapter 15 opening (before "What you will be able to do")

## ES-ch15.2

Now that Claude can draft ten plausible capstone files in minutes, where does the capstone's real difficulty lie? State the question the chapter says the capstone must answer.

**Points:** 5

**Rubric (1 point each):**

1. Notes that Claude can draft ten plausible files quickly, in clean prose, with cross-references that look right.
2. Notes that the validator would pass such files and a tired reader might as well.
3. Says producing a packet has become cheap and the cost has moved to finding out whether anything in it is true.
4. Adds that the cost has also moved to deciding whether the work should be used at all.
5. States the question: what would let a person who was not in the room trust this packet, and who answers if they are wrong.

**Source:** Chapter 15 opening (before "What you will be able to do")

## ES-ch15.3

Define the book's three jobs (conduct, check, drive) as the chapter does, and explain why the chapter says the capstone is the one place where you cannot do only one.

**Points:** 5

**Rubric (1 point each):**

1. Defines conduct as deciding before Claude implements.
2. Defines check as finding out what is wrong and signing only what the record supports.
3. Defines drive as keeping the choices that are yours.
4. Says earlier chapters practiced the jobs one artifact at a time, while the capstone requires all three together.
5. Says the capstone is one bounded workflow whose packet lets another person trace a line from need and consenting owner through to transfer, and that the final decision is defended from that trace rather than from presentation quality.

**Source:** Chapter 15 opening (before "What you will be able to do")

## ES-ch15.4

Before reading the validator, the chapter asks four predictions. Give the correct answer to each, with the reason: (a) how many issues an empty folder returns, (b) the result for a five-character `brief.md`, (c) the result when `brief.md` is a symbolic link to a file outside the packet, (d) whether ten polished files can prove that a real stakeholder consented.

**Points:** 5

**Rubric (1 point each):**

1. An empty folder returns ten issues, one missing issue per required stem.
2. A five-character `brief.md` exists inside the packet but is under forty characters, so it is reported as insufficient content while the other nine stems remain missing.
3. A symbolic link to an external target is reported as `brief: outside packet`.
4. Explains the symlink result comes from the containment check, which runs before the presence check.
5. Says polished files cannot prove consent, because consent cannot be generated as fixture text and requires a real decision record from the owner.

**Source:** What you will be able to do

## ES-ch15.5

Map the ten packet artifacts onto the three jobs, name the device each job takes at capstone scale, and say what each device answers.

**Points:** 5

**Rubric (1 point each):**

1. Conduct covers the brief, data-boundary, action-surface-map, plan, gates, and pre-mortem, and its device is the gate.
2. Check covers the evidence and audit-note, and its device is the sign-off (claim-to-evidence graph, reviewer audit, Gap Account).
3. Drive covers the artifact (its use) and the transfer-reflection, and its device is the driver's seat (ship, narrow, defer, or stop).
4. States that the gate says what Claude may do and the sign-off says what the record supports.
5. States that the driver's seat says what you will do with both.

**Source:** Three jobs, one packet

## ES-ch15.6

A student builds the workflow with Claude first, writes the six pre-build artifacts afterward to describe what was built, and then ships it. Using the chapter's three devices, say which device is missing and what kind of build results. Then name the build that results when the sign-off is missing and when the driver's seat is missing.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the missing device as the gate, because the student's decisions were not on record before Claude implemented.
2. Names the resulting build as improvised.
3. Says a build with no sign-off is a demo.
4. Says a build with no driver's seat is a task Claude completed and nobody chose.
5. Explains that the gate is where the student's decisions go on the record and what Claude's implementation is tested against, so writing it afterward defeats its purpose.

**Source:** Three jobs, one packet

## ES-ch15.7

A student proposes a capstone that searches private drives, edits records, and publishes externally, arguing that this makes it "in the wild". Evaluate the proposal using the chapter's meaning of "in the wild" and suggest a narrower version.

**Points:** 5

**Rubric (1 point each):**

1. States that "in the wild" means a real context with a known owner, approved data, and explicit boundaries, not unrestricted access to somebody else's systems.
2. Says reality enters through consequences, constraints, and evidence, not through maximal autonomy.
3. Says every added action is something a person must be able to check and attention is finite, so ambition is demonstrated through control, not surface area.
4. Suggests a narrower version, such as drafting a report from approved sources, which is easier to evaluate.
5. Notes that the narrower capstone should still include a meaningful action and failure boundary.

**Source:** "In the wild" means bounded reality

## ES-ch15.8

The workflow's owner cannot be reached before the deadline. A student asks Claude to write the owner's approval email and files it as the consent record. Explain what is wrong and what the chapter says to do instead.

**Points:** 5

**Rubric (1 point each):**

1. Says consent cannot be generated as fixture text.
2. Says Claude can draft the questions to put to the owner, but nothing it writes is the owner's answer.
3. Names the pattern as synthetic consent, a failure of conduct.
4. Says that when access or consultation is pending, the project should be constrained to synthetic or public data.
5. Says the remaining decision must be labeled as pending.

**Source:** "In the wild" means bounded reality

## ES-ch15.9

A workflow summarizes public course notes. Write a non-purpose and an inspectable success state for it, and explain why "the agent completed the task" is not an acceptable success state.

**Points:** 5

**Rubric (1 point each):**

1. Gives a non-purpose consistent with the chapter's example, such as not evaluating students, not ingesting private submissions, or not publishing without review.
2. Explains that non-purposes give reviewers concrete misuse and scope-drift checks.
3. Gives a success state that can be inspected, such as required sections present, every consequential claim mapped to an approved source passage, the target file matching the reviewed diff, and publication still pending.
4. Calls "the agent completed the task" narration rather than an observable state.
5. Includes at least one condition that would make the result unacceptable.

**Source:** "In the wild" means bounded reality

## ES-ch15.10

Describe the three structural checks `validate_packet` applies to each artifact, in the order it applies them, with the issue each produces, and explain why the order matters.

**Points:** 5

**Rubric (1 point each):**

1. Containment comes first: the resolved path must remain relative to the resolved root, and the issue is `name: outside packet`.
2. Presence comes second: the path must be a file, and the issue is `name: missing`.
3. Length comes third: the stripped text must contain at least forty characters, and the issue is `name: insufficient content`.
4. Gives the order's consequence: a symlink to an external file is reported as outside packet before presence or length is considered.
5. Notes the loop runs over ten declared stems, building `root / (name + ".md")` for each.

**Source:** Tear down the packet validator

## ES-ch15.11

The repository test links `brief.md` to `/etc/hosts`. What does the validator report, which check produces that report, and why does passing that check not make a packet's contents trustworthy?

**Points:** 5

**Rubric (1 point each):**

1. States the report is `brief: outside packet`.
2. Attributes it to the containment check, where the resolved path is not relative to the resolved root.
3. Notes that this check runs before presence, so the fact that the target is a file does not matter.
4. Says containment is about location, not content trust.
5. Says a malicious file physically inside the packet can still contain harmful instructions.

**Source:** Tear down the packet validator

## ES-ch15.12

A student's packet contains only a `brief.md` whose text is `short`. State the validator's complete result, say what the forty-character threshold can and cannot catch, and explain why a file of repeated `x` characters longer than forty still passes.

**Points:** 5

**Rubric (1 point each):**

1. States that the brief is reported as insufficient content because it exists but is under forty stripped characters.
2. States that the other nine artifacts are reported missing, so ten issues are returned in total.
3. Says the threshold catches empty placeholders and few-word stubs.
4. Says it cannot judge relevance, truth, authorship, evidence, or quality.
5. Explains that the repeated-`x` file passes because it is inside the root, is a file, and exceeds forty stripped characters.

**Source:** Tear down the packet validator

## ES-ch15.13

Explain what the `human_review` string in the validator's return value is for, why the chapter calls it part of the contract, and what `structurally_complete: True` does and does not mean.

**Points:** 5

**Rubric (1 point each):**

1. States the string says that evidence, authority, and understanding must still be assessed.
2. Says the string is part of the contract, not a disclaimer to skip.
3. Notes that a test confirms "understanding" remains in the human-review message.
4. Explains that `structurally_complete` is `not issues`, meaning every stem passed the three structural checks.
5. Says structural completeness deliberately stops before substantive approval, and the string hands substance to a person.

**Source:** Tear down the packet validator

## ES-ch15.14

A classmate wants to strengthen the validator with a keyword list or relevance score so that it rejects meaningless packets. Using the chapter's argument, explain why narrowness is the point and what the chapter proposes instead.

**Points:** 5

**Rubric (1 point each):**

1. Says a mechanical check is reliable exactly where it is narrow.
2. Says judging relevance would require a heuristic such as a keyword list or a score.
3. Says fluent drafting tends to satisfy any heuristic that reads only the surface of prose, which is what Claude produces best.
4. Says the check worth having fails differently from the thing it checks, and a path resolution and a character count do not care how good the prose sounds.
5. Says the remedy for a meaningless pass is not a better validator but a sentence inside the packet saying what was checked, and the validator's `True` must never stand in for the rest of the review.

**Source:** Tear down the packet validator

## ES-ch15.15

For each of the five fixtures in the chapter's table (empty folder, short brief, escaping symlink, ten repeated strings, connected real packet), give the structural result and the substantive conclusion.

**Points:** 5

**Rubric (1 point each):**

1. Empty folder: ten missing issues; the packet is absent.
2. Short brief: insufficient plus missing issues; a placeholder is detected.
3. Escaping symlink: an outside-packet issue; containment is violated.
4. Ten repeated strings: structurally complete; no learning is established.
5. Connected real packet: possibly complete; it requires claim-level review.

**Source:** Worked example: missing, escaping, meaningless, and useful

## ES-ch15.16

Why does the chapter call the ten-repeated-strings packet "the decisive counterexample" and "the fluency trap at its smallest"? What is the remedy, and what must a full human review inspect?

**Points:** 5

**Rubric (1 point each):**

1. Explains it is the decisive counterexample because it proves that presence and length do not establish substance.
2. Explains it is the fluency trap because the packet is well formed and passes, and the pass invites the belief that someone checked something.
3. States that the remedy is not a better validator.
4. States that the remedy is a sentence, inside the packet, saying what was checked.
5. States that a full human review must inspect whether each artifact performs its role and whether the links between artifacts hold.

**Source:** Worked example: missing, escaping, meaningless, and useful

## ES-ch15.17

Contrast what a validator sees with what a reviewer sees in `evidence.md` and `audit-note.md`. What makes each file useful?

**Points:** 5

**Rubric (1 point each):**

1. Says the validator sees only that both files are long, while the reviewer sees whether they form evidence.
2. Says a useful `evidence.md` records exact commands, versions, inputs, outputs, failures, and interpretations.
3. Says it maps claims to checks that can disagree, rather than merely saying "tests passed".
4. Says a useful `audit-note.md` predicts review findings before Claude critiques the packet.
5. Says it records whether the learner revised, defended, or acknowledged each finding.

**Source:** Worked example: missing, escaping, meaningless, and useful

## ES-ch15.18

List what the `brief` and `data-boundary` artifacts must contain. Then explain, with an example consequence, why labeling data with the label most likely to pass is a failure.

**Points:** 5

**Rubric (1 point each):**

1. Says the brief states the need, consenting owner, affected people, success condition, non-purpose, and decision scope.
2. Says the brief also states what would make the workflow inappropriate.
3. Says the data-boundary inventories sources, classifications, provenance, access, retention, deletion, and exclusions.
4. Says data is labeled public, synthetic, internal, personal, or unknown by the project's real policy, not by the label most likely to pass.
5. Gives a consequence of mislabeling, such as the claim that fixtures are public resting on a misclassified source (the graph's residual gap for that claim is misclassification, with the data owner responsible).

**Source:** Ten artifacts, one argument

## ES-ch15.19

Describe the `action-surface-map` and the `plan`. Use a local-write approval to illustrate why the map separates capability from authority.

**Points:** 5

**Rubric (1 point each):**

1. Says the map shows what the workflow can read, propose, write, send, or publish.
2. Says it separates capability from authority and flags external or irreversible effects.
3. Says the plan lays out evidence-producing steps with dependencies, stop conditions, budgets, and replanning triggers.
4. Illustrates with the point that approval of a local write is not authority to publish.
5. Names the failure "authority drift" for describing a local-write approval as permission to publish.

**Source:** Ten artifacts, one argument

## ES-ch15.20

What do the `gates` and `pre-mortem` artifacts each contain, and how does the gate's dated failure sentence connect to the pre-mortem?

**Points:** 5

**Rubric (1 point each):**

1. Says the gates bind consequential proposals to exact content and responsible decisions.
2. Says the gates specify evidence, effects, rollback limits, expiry, and what happens while review is pending.
3. Says the pre-mortem predicts stale state, invalid calls, injection, duplicate actions, privacy exposure, misleading success, and other project-specific failures.
4. Says each pre-mortem failure comes with detection, owner, response, and residual risk.
5. Says the gate's dated failure sentence is the lead entry in the pre-mortem.

**Source:** Ten artifacts, one argument

## ES-ch15.21

Describe the four artifacts that record and judge the build: `evidence`, `artifact`, `audit-note`, and `transfer-reflection`. Why is a screenshot alone not enough for the `artifact`?

**Points:** 5

**Rubric (1 point each):**

1. Says `evidence` holds reproducible commands and observed results and distinguishes code inspection, deterministic fixture output, model output, human observation, and external product behavior.
2. Says the `artifact` is the usable output or a precise pointer and reproduction route, and that a screenshot alone is not reproducibility.
3. Says the `audit-note` records predictions before critique, findings, evidence-based responses, failed cases, corrections, and unresolved gaps, and ends with the Gap Account and the sign-off.
4. Says the `transfer-reflection` records what the learner will delegate more readily, what capability must remain practiced, and what decision remains human, each pointing to project evidence.
5. Says the `transfer-reflection` also holds the final ship, narrow, defer, or stop decision and its reason.

**Source:** Ten artifacts, one argument

## ES-ch15.22

The chapter says a packet is ten documents and an argument is the lines between them. Give at least four cross-references that tie the artifacts together, and explain how each should be treated.

**Points:** 5

**Rubric (1 point each):**

1. Says the brief's success criterion maps to evidence.
2. Says the data boundary constrains the action map.
3. Says the plan invokes the gates.
4. Says the pre-mortem predicts a failure demonstrated in the audit note, or the transfer reflection cites the controlled recovery.
5. Says each reference is a claim to be confirmed by opening the target, because Claude can add cross-references in minutes and a validator cannot check them; without links the documents are ten islands.

**Source:** Ten artifacts, one argument

## ES-ch15.23

Before asking Claude Code for any part of the workflow, the chapter says to write a short gate. List its five parts and say who owns the decisions in the first.

**Points:** 5

**Rubric (1 point each):**

1. Design: the workflow, the owner, the approved data, and the one action that matters are the learner's or the owner's choices, and the gate says which; Claude can challenge them but did not make any.
2. Contract: what the workflow must do and must refuse (publish, read outside approved sources, count a retrieved passage as support when it does not entail the claim), the observable done state, and the conditions that make the result unacceptable.
3. A wrong version your checks must catch: a run that completes, reads well, and leaves the wrong state, where inability to tell it from the right run means the gate is not finished.
4. What a failure looks like: one dated sentence, written before the run.
5. What this build may claim: a bounded local result under recorded conditions, not that the workflow is safe, that the owner consents beyond the brief, or that a live Claude run would behave the same.

**Source:** The gate: Claude proposes, Python constrains

## ES-ch15.24

Suppose your workflow drafts a source-grounded report. Describe a "wrong version" that your checks must catch, explain what makes it dangerous, and say what to conclude if your checks cannot tell it from the right version.

**Points:** 5

**Rubric (1 point each):**

1. Gives a wrong version, such as a fluent draft whose citation does not support its claim, or a local-write approval treated as permission to publish.
2. Says the wrong version completes and reads well.
3. Says it nevertheless leaves the wrong state.
4. Names the contract line it violates, such as refusing to count a retrieved passage as support when it does not entail the claim, or refusing to publish.
5. Concludes that if the checks cannot tell the wrong run from the right one, the gate is not finished.

**Source:** The gate: Claude proposes, Python constrains

## ES-ch15.25

Explain "Claude proposes, Python constrains": what each side does, why a prompt is not a boundary, and what the trade-off is.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude does the language work: drafting, summarizing, and proposing a tool call.
2. Says Python holds what must be the same every time: which tools exist, whether an argument is valid, whether a path stays inside the approved root, whether a proposal matches content a person approved, and what gets recorded.
3. Says a prompt is a request, not a boundary: "do not publish" is useful task context, but the boundary is an application that lacks or gates the capability.
4. Says a prompt-injected source should not be able to grant itself tools.
5. Names the trade-off: every boundary you code is a case you foresaw and an unforeseen case passes straight through, which is why the gate also asks what a failure looks like.

**Source:** The gate: Claude proposes, Python constrains

## ES-ch15.26

The chapter advises starting offline. Describe how to build the controller, which records to keep, the conditions on any live Messages path, and what must never be done when a live run is missing.

**Points:** 5

**Rubric (1 point each):**

1. Says to inject a callable into the controller where possible so tests do not need network access.
2. Says to validate tool names and arguments in Python and resolve paths before action.
3. Says to preserve model requests, application results, and final claims as three separate records, because the claim is the part most likely to say more than the other two support.
4. Says a live path must be opt-in, bound requests, identify the model actually used, protect credentials, and record cost-bearing behavior.
5. Says never to replace a missing live run with invented output, and that live behavior is evidence about that run under its recorded conditions, not a universal guarantee.

**Source:** The gate: Claude proposes, Python constrains

## ES-ch15.27

Describe the Build It baseline and explain why it comes before Claude touches anything.

**Points:** 5

**Rubric (1 point each):**

1. Says you write your own `validate_packet` from the ten names and the three conditions before consulting the reference.
2. Says you run the Practice Lab cases: a removed evidence artifact and a long but meaningless file.
3. Says you add at least two tests of your own: a meaningful success outside the demo, and a failure that would matter in your capstone.
4. Says you state what remains untested.
5. Says the validator is the baseline, the record of what you understood before Claude touched anything and a mechanism small enough to audit, because you cannot audit a containment check you have never tried to break.

**Source:** Build It: the baseline

## ES-ch15.28

After Claude Code returns an implementation built against your gate, what three things does the chapter ask you to do, and what should you preserve?

**Points:** 5

**Rubric (1 point each):**

1. Says to note which tests failed, since a failing test is often a gap in the gate because Claude had only what you wrote.
2. Says to name one difference in behavior between Claude's implementation and your plan: a boundary it handled that you missed, or one it silently ignored.
3. Says to ask Claude to propose a deliberately wrong version that still passes your checks and test by hand whether it does; if it does, the checks were too weak.
4. Says to preserve the actual transcript: prompt, plan, diff, commands, and outputs, with the date and displayed model label.
5. Says that if a session failed or did not run, you record that rather than substituting a fixture.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch15.29

Claude's implementation handles a boundary your gate missed, so you change the gate after the build has started. Does this violate "design first"? What do you record?

**Points:** 5

**Rubric (1 point each):**

1. Says it does not violate design-first; it is a re-engagement.
2. Says a later finding can reopen an earlier decision.
3. Says you log the reopening and its reason.
4. Says this case, a boundary Claude handled that you missed, revises your gate.
5. Distinguishes it from the other difference the chapter names, a boundary Claude silently ignored.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch15.30

Why does the chapter say a gate you have never seen fail has not been tested? Describe how to choose, predict, run, and record a controlled failure.

**Points:** 5

**Rubric (1 point each):**

1. Says a polished happy-path demo proves very little.
2. Says to choose one failure that matters to the workflow and can be reproduced safely.
3. Says to predict it before running, and that the prediction is the sentence written in the gate.
4. Says to preserve the input, action, reported outcome, independently observed outcome, and gap.
5. Says to preserve failed output when privacy and safety permit, because a demo edited to show only success hides the most valuable part of supervision.

**Source:** Controlled failure and reviewed recovery

## ES-ch15.31

In the chapter's example, a source-grounded report workflow meets a relevant-looking passage that does not support a deadline claim. Describe what happens at each step of the trace, and say what the example is and is not.

**Points:** 5

**Rubric (1 point each):**

1. Says the model produces fluent prose and a citation.
2. Says the source check rejects entailment.
3. Says nothing is published, and the trace ends in a stop state.
4. Lists the trace as request, retrieved passage, draft, failed check, and stop state.
5. Says the example is a constructed illustration of the shape, not a recorded run.

**Source:** Controlled failure and reviewed recovery

## ES-ch15.32

A student reruns the same prompt six times until the report passes the check and calls this recovery. Explain what is wrong and describe reviewed recovery as the chapter defines it.

**Points:** 5

**Rubric (1 point each):**

1. Says recovery is not asking Claude again until it passes, and names this as recovery by repetition, a failure of check.
2. Says a human or declared policy reviews why the case failed.
3. Says the plan may narrow the claim, select a different approved source, add an abstention rule, or defer.
4. Says the changed proposal goes through its gate again, and a later success is compared with the original failure and checked independently.
5. Says recovery can reopen the design (a source classification, a scope line, or the success condition itself) and the honest record says so.

**Source:** Controlled failure and reviewed recovery

## ES-ch15.33

What does it mean for a check to fail differently from the thing it checks? Give two examples from the chapter, one pair that is not independent, and the name of the failure that results when the routes share a mistaken source or helper.

**Points:** 5

**Rubric (1 point each):**

1. Says the check should use a different route so that it does not share the production route's mistakes.
2. Gives the example that when Claude drafts the claim, Python can validate source identifiers and structure while a person inspects semantic support.
3. Gives the example that when Python calculates a total, a separate derivation can check it.
4. Says two Claude prompts sharing the same context are not automatically independent.
5. Names the failure shared-check dependence: the production and checker routes rely on the same mistaken source or helper.

**Source:** Controlled failure and reviewed recovery

## ES-ch15.34

What is a prediction-lock, and what are the eight parts of a casebook entry?

**Points:** 5

**Rubric (1 point each):**

1. Defines a prediction-lock as writing what you expect, dated, before you observe, and never editing it afterward.
2. Says the learning is the gap between the prediction and what happened, and that "look at it and iterate" never means re-prompting until the output looks right.
3. Lists parts one to three: the prediction recorded before execution, the exact sanitized input and provenance, and the action or tool request.
4. Lists parts four to six: the system-reported outcome, the independently observed outcome, and the gap between report and evidence.
5. Lists parts seven and eight: the containment and recovery decision, and the remaining uncertainty.

**Source:** The miniature casebook

## ES-ch15.35

In one case a student's staged failure was correctly rejected by the checker; in another the system accepted something the student expected it to refuse. What should the casebook record in each case, what may such outcomes support, and what must not be done?

**Points:** 5

**Rubric (1 point each):**

1. Says that when the checker correctly rejected, the entry should explain which mechanism did the work.
2. Says that if the system did something other than the prediction (for example accepted when refusal was expected), that is recorded.
3. Says not to manufacture a surprising error for drama.
4. Says one observed miss does not prove a permanent limitation of every future model; it supports a bounded claim about this workflow, case, and check.
5. Says one clean run does not establish general reliability, and the casebook accumulates inspectable encounters rather than universal slogans.

**Source:** The miniature casebook

## ES-ch15.36

Before asking Claude Code to review the packet, what must you record, and why is "the review will find weak integration" a poor prediction? Give a better one.

**Points:** 5

**Rubric (1 point each):**

1. Says to predict three specific findings, each with an artifact location and a reason.
2. Says a prediction has to forbid something, and the vague one can be matched by anything so it teaches nothing.
3. Gives a specific prediction naming an artifact and a reason, such as the data boundary not tracing deletion from exported reports, the gate's rollback claim ignoring an external message, or the evidence matrix relying on the same parser for production and checking.
4. Says to mark each prediction as a finding expected to be genuine or a false positive.
5. Says to record the displayed model label and the date, because a later run of the reviewer may differ.

**Source:** Audit the reviewer

## ES-ch15.37

Claude Code returns three findings: (1) a real defect in the data boundary, (2) a concern the packet already addresses in `gates.md`, (3) a vague worry with no located evidence. For each, what response does the chapter prescribe? What is wrong with accepting all findings or rejecting all of them?

**Points:** 5

**Rubric (1 point each):**

1. Says finding 1 should be revised, because the critique identifies a supported defect.
2. Says finding 2 should be defended, citing the exact passage and explaining why the critique missed it.
3. Says finding 3 is not a finding, because a finding without located evidence is not a finding.
4. Names the third legitimate response, acknowledging an unresolved limit, for cases where neither revision nor defense is justified.
5. Says accepting every finding is a failure (a misreading you accept is someone else's error signed as yours) and rejecting every finding is its mirror.

**Source:** Audit the reviewer

## ES-ch15.38

How do you evaluate the reviewer itself? Say what you score, what you credit, and what a clean review does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Says to ask whether it found the predicted issues, raised a plausible but unsupported concern, or overlooked a controlled failure already visible.
2. Says to score each prediction matched, partly matched, or missed.
3. Says to credit the specificity of your reasoning over the hit rate.
4. Says the course holds no measurement of how often such a review is wrong about a packet like yours, so every finding is a hypothesis to check.
5. Says a clean review is corroboration, not proof: this reviewer, this time, did not refute you.

**Source:** Audit the reviewer

## ES-ch15.39

Explain the Gap Account's distinction between a contingent miss and a structural gap for this review. Classify (a) a missing test that a better prompt would have found, and (b) an owner's agreement that came with an unwritten condition only you remember.

**Points:** 5

**Rubric (1 point each):**

1. States the test question: would a better prompt, a second run, a differently built reviewer, or more evidence close the gap.
2. Says that if yes, it is a contingent miss to be fixed, or the better review run, and said so.
3. Says that if the answer turns on the kind of reviewer (a model that reads only your packet), it is a structural gap for this review.
4. Classifies (a) as a contingent miss and (b) as a structural gap, a consequence visible only from inside a relationship you answer to.
5. Says "structural" means owing to the reviewer's kind and access, not for all time, and that a reviewer sharing the draft's model and context shares its blind spots so a second pass by the same reviewer will not close the gap.

**Source:** The Gap Account

## ES-ch15.40

Name the three patterns of structural gap the chapter describes, give an example of each, and say what you must record for each gap.

**Points:** 5

**Rubric (1 point each):**

1. Names a consequence visible only from inside a relationship you answer to, such as an agreement that came with an unwritten condition.
2. Names a judgment grounded in domain experience the packet never stated, such as a number that is fine on paper and wrong for this site.
3. Names an asymmetry of stakes: you will bear the consequence and the reviewer will not.
4. Says that for each gap you name the evidence or expertise that could help and the person accountable for the decision now.
5. Says a gap is a boundary on the final claim, not permission to give up, and that the patterns are not a form to fill in.

**Source:** The Gap Account

## ES-ch15.41

Distinguish the companion book's claim about reviewers from the claim your own Gap Account makes. Why does the course ask for the smaller one?

**Points:** 5

**Rubric (1 point each):**

1. Says the companion book argues that no reviewer of any capability can reach what depends on being situated, having a stake, and being accountable.
2. Says it grounds this in philosophy and in safety literature on correlated errors.
3. Says the course treats it as an argued position and does not ask you to agree with it or prove it.
4. Says the Gap Account claims only that this review, on this packet, did not reach this item, that repeating it would not, and that this person can.
5. Says one observed miss does not show that no future model could find the issue; it sets a boundary for the decision being made now.

**Source:** The Gap Account

## ES-ch15.42

For each claim, say what the chapter says it needs: (a) "the report was created", (b) "the report is source-grounded", (c) "the owner consented", (d) "the workflow is safe". Then explain why you must inspect resulting state and not only the trajectory.

**Points:** 5

**Rubric (1 point each):**

1. Says (a) can map to file existence and read-back.
2. Says (b) needs claim-to-passage inspection.
3. Says (c) needs a real decision record, not model text.
4. Says (d) is probably too broad and should be decomposed.
5. Explains that an agent can execute the planned calls while the destination remains wrong, for example a local write that was never committed or published, or a request that returned a success code while the intended person never received it.

**Source:** Independent verification and outcome state

## ES-ch15.43

Why does the chapter say that output is cheap and verification is not, when discussing the claim-to-evidence graph? What follows for how you use Claude on it?

**Points:** 5

**Rubric (1 point each):**

1. Says Claude can produce such a graph in a minute because it is an index-and-cross-reference task.
2. Says checking one edge means opening its target.
3. Says an edge is a claim that this evidence bears on that claim, so you decide whether each edge is real.
4. Says a project that does not budget for verification will not get it.
5. Says the graph is built by starting with the final recommendation and breaking it into smaller claims until each can be checked by one or more artifacts.

**Source:** Build a claim-to-evidence graph

## ES-ch15.44

Decompose the recommendation "Narrow the workflow to create a local source-grounded draft, retain only public fixtures for one day, and require a human before publication" into claims, and give the evidence and residual gap for two of them.

**Points:** 5

**Rubric (1 point each):**

1. Lists the six claims: a draft exists, it uses approved sources, the target remains local, retained fixtures are public, deletion follows the stated day boundary, and publication is gated.
2. Says each claim is mapped separately with a producing mechanism, evidence, decision owner, and residual gap.
3. Gives correct evidence and residual gap for one chosen claim (for example local draft: resolved path, read-back, and diff, with later mutation as the gap).
4. Gives correct evidence and residual gap for a second chosen claim (for example fixtures are public: source IDs and classification review, with misclassification as the gap).
5. Says the sentence contains at least six claims, so one check of the draft is not enough.

**Source:** Build a claim-to-evidence graph

## ES-ch15.45

Why does the claim-to-evidence graph include a residual-gap column? Illustrate with the limits of read-back, an event trace, and a classification review, and say where those limits go.

**Points:** 5

**Rubric (1 point each):**

1. Says the column prevents the graph from becoming decorative certainty, because every evidence route has scope.
2. Says read-back establishes content at an observed time.
3. Says an event trace can show no publish action inside the instrumented workflow but not every possible external channel.
4. Says a classification review can be wrong.
5. Says these limits inform the deployment choice and are the raw material of the sign-off's "not checked" line.

**Source:** Build a claim-to-evidence graph

## ES-ch15.46

How do you find weak points in a claim-to-evidence graph? Cover orphan nodes, heavily cited evidence, and circular support.

**Points:** 5

**Rubric (1 point each):**

1. Says a claim with no evidence should be removed, narrowed, or marked pending.
2. Says an artifact supporting no claim may be busywork, and a decision with no named owner is unresolved.
3. Says evidence cited by many claims deserves extra scrutiny because one defect can collapse several conclusions.
4. Says the audit note cannot establish that the evidence is correct by summarizing `evidence.md`, which cites the audit note; that is circular support.
5. Says the central result should connect to an observation or derivation outside its production narrative.

**Source:** Build a claim-to-evidence graph

## ES-ch15.47

Describe the contradiction pass before handoff: what you compare, how you resolve a conflict, and what you do about later edits.

**Points:** 5

**Rubric (1 point each):**

1. Lists at least three of the comparisons: the brief's purpose with the implemented tools, the data inventory with actual fixtures, the action map with the trace, gate decisions with executed targets, and retention promises with deletion evidence.
2. Says not to resolve a contradiction by choosing the newest document.
3. Says to determine which artifact is authoritative, correct the dependent claims, and preserve the revision reason.
4. Says to freeze the review candidate by revision or digest so later edits cannot masquerade as reviewed work.
5. Says that if a consequential file changes, you rerun the checks whose premises changed plus the integration checks, and treat it as a new review candidate rather than a continuation of the old approval.

**Source:** Build a claim-to-evidence graph

## ES-ch15.48

Why is a handoff "a seam", and how does the chapter propose to test one? Give four kinds of hidden knowledge the test is designed to expose.

**Points:** 5

**Rubric (1 point each):**

1. Says seams are where risk lives, and a packet only its author can run has a gate with one person behind it.
2. Says to give a bounded participant only the documented prerequisites and commands, in a sanitized environment.
3. Names at least four kinds of hidden knowledge: an unstated working directory, an unexplained environment variable, a dependency installed globally on your machine, a fixture at an absolute personal path, or a recovery step known only from your debugging session.
4. Says the participant runs the offline path first, compares actual output with the documented expectation, triggers the controlled failure, and locates the evidence matrix, with live behavior later and only with explicit authorization.
5. Says each question the participant has to ask marks missing transfer evidence.

**Source:** Handoff that survives the author

## ES-ch15.49

After a handoff attempt, what should be recorded and redone, and what must a handed-over capstone state? List the maintenance questions.

**Points:** 5

**Rubric (1 point each):**

1. Says to record the environment, commands, failures, questions, and revisions as evidence.
2. Says that after revising the documentation you rerun from a clean-enough context rather than assuming the prose fixed the problem, and state what persisted.
3. Says reproduction is an observed property of a particular handoff, not an adjective awarded to documentation.
4. Says exclusions must be stated prominently (for example live API behavior untested, stakeholder consultation pending, only local writes authorized so no implied publication) and that API keys, private data, and unauthorized excerpts are never packaged.
5. Lists the maintenance questions: who refreshes sources, what invalidates memory, when approvals expire, which threshold pauses the system, and how dependencies are updated and re-evaluated.

**Source:** Reproduce the handoff as an experiment

## ES-ch15.50

A student's offline tests all pass, no live run was recorded, and stakeholder consultation is pending. Write the "Checked", "How", "Not checked", and "Not claiming" lines of the sign-off, and say which verbs they may use.

**Points:** 5

**Rubric (1 point each):**

1. "Checked" names the specific claims in the graph and the evidence they were checked against.
2. "How" says whether the check was by hand, by a test written before reading Claude's version, by recomputation, by a check that fails differently, or with Claude's help, saying which parts.
3. "Not checked" includes live behavior (no live run recorded), each residual gap in the graph, each Gap Account item, and the pending consultation.
4. "Not claiming" includes that the workflow is safe and that the owner's consent covers any use beyond the brief.
5. Uses verbs such as recorded, computed, tested, inspected, or reviewed, not "established" or "proven" unless a criterion supports them; a passing test supports "tested", not "safe".

**Source:** The sign-off: the last thing the evidence says

## ES-ch15.51

Why does the chapter treat "withheld" as a legitimate sign-off outcome? Discuss what the sign-off buys and costs, the "cleared by" line, and what a typed name does not do.

**Points:** 5

**Rubric (1 point each):**

1. Says a process whose only permitted result is "signed" is a rubber stamp with a person's name on it.
2. Says that if the record does not support signing, the author says what would, and stops there.
3. Says the sign-off buys legible answerability: after a failure someone can find who signed and read what they did not warrant.
4. Says it costs speed and deniability, since someone must be willing to be named, and that friction is the point.
5. Says "cleared by" needs a named person for each consequential decision, in a role that can be asked about it and can lose something if it was wrong, and that a typed name does not authenticate anyone or make a legal compliance determination.

**Source:** The sign-off: the last thing the evidence says

## ES-ch15.52

Describe how to compare ship, narrow, defer, and stop, and say what Claude can and cannot contribute.

**Points:** 5

**Rubric (1 point each):**

1. Says not to write the recommendation first and assemble supporting facts afterward.
2. Says to put all four options into one comparison against the same criteria.
3. Names at least five criteria: benefit, data exposure, action consequence, evidence strength, reversibility, review labor, consent, maintenance, unresolved harm.
4. Says the criteria express values, so you say who chose them.
5. Says Claude can draft the comparison, including doing less, but cannot supply the weights, and that passing structure and tests does not oblige deployment because evidence informs the decision but does not make it.

**Source:** Defend the four options against the same evidence

## ES-ch15.53

Choose ship, narrow, defer, or stop for each case and justify it with the chapter's conditions: (a) the data owner has not yet classified one source, (b) the draft is well supported but automatic publication creates most of the uncertainty, (c) consent cannot be obtained from the owner, (d) a simpler non-AI process would do the job.

**Points:** 5

**Rubric (1 point each):**

1. Says (a) is defer, naming the concrete condition (the data owner classifies the source) and its owner.
2. Says (b) is narrow: remove automatic publication and keep the artifact local, which is a design response to evidence, not a failure.
3. Says (c) is stop, because consent cannot be obtained.
4. Says (d) is stop because a simpler non-AI process dominates, and that you record what was learned and retire data and permissions safely.
5. Says an indefinite "more research is needed" evades the decision, and effort already spent is not evidence for continuing.

**Source:** Defend the four options against the same evidence

## ES-ch15.54

What is the sensitivity test for a deployment recommendation, and what must the final recommendation contain?

**Points:** 5

**Rubric (1 point each):**

1. Names at least three counterfactuals: external-write capability removed, retention falling from a year to a day, the owner withdrawing consent, the independent checker disagreeing once, the reviewer backlog doubling.
2. Says these reveal which assumptions actually drive the decision.
3. Lists at least six contents of the recommendation: chosen option, rejected alternatives, evidence, affected interests, conditions, owner, review date, change triggers, and who may revisit it.
4. Says it should include one sentence of epistemic restraint about what the packet does not establish.
5. Says that sentence is often the strongest evidence the author understands the system, and that a later source change, incident, or stakeholder objection can reopen the choice.

**Source:** Defend the four options against the same evidence

## ES-ch15.55

Explain the Memo A / Memo B form and list the labeled parts of the recommendation.

**Points:** 5

**Rubric (1 point each):**

1. Says Memo A is the machine's analysis, here Claude's evidence assembly and option comparison.
2. Says Memo B is not Memo A with your name added, because a signature without the account behind it counterfeits accountability.
3. Lists the parts: what Claude produced, and what you add that the packet could not show.
4. Lists the parts: why the evidence should be trusted (citing graph rows and not Claude's confidence), why this is the right action here for these people, and the recommendation you sign.
5. Says the separation makes your part defensible, because you cannot answer for a judgment you cannot tell apart from the draft.

**Source:** Write the recommendation so the judgments are separable

## ES-ch15.56

Using the driver's-seat table, say for (i) assembling the evidence trail, (ii) consent and authority, and (iii) the choice and signature, what Claude should do, what you should do, and why the task stays with you.

**Points:** 5

**Rubric (1 point each):**

1. For (i), says Claude cross-references, runs `validate_packet`, and lists contradictions, while you decide which artifact is authoritative and recheck a sample by hand.
2. For (i), gives the reason: a list of contradictions does not say which document to believe.
3. For (ii), says Claude drafts the questions to put to the owner while you obtain a real decision from a real owner and record it, because consent cannot be generated, only given.
4. For (iii), says Claude does nothing beyond the draft while you decide, sign or withhold, and name who may revisit.
5. For (iii), gives the reason: whoever signs is the one who will be asked.

**Source:** The driver's seat

## ES-ch15.57

Explain the three verdicts from Irreducibly Human (deprioritize, supervise, protect), say which rows of the driver's-seat table fall under each, and explain the warning that governs the first.

**Points:** 5

**Rubric (1 point each):**

1. Defines deprioritize as handing the work over gladly, supervise as using it and auditing it, and protect as keeping it.
2. Places the first row (evidence trail and validator) under deprioritize with a spot-check.
3. Places the second and third rows (comparing the options, reviewing the packet) under supervise.
4. Places the last two rows (consent and authority, the choice and signature) under protect.
5. Explains that deprioritization is not deletion: you can hand Claude the claim-to-passage matrix only because you can still check a row, which is why you built the validator by hand.

**Source:** The driver's seat

## ES-ch15.58

State the thesis the chapter attributes to Irreducibly Human about reckoning and judgment, say how the chapter treats it, and give the smaller claim the course relies on instead.

**Points:** 5

**Rubric (1 point each):**

1. States the thesis: what machines do is reckoning (calculation, pattern, inference at scale), while judgment takes the world to matter and answers for the result.
2. Says the book presents it as an argued position and marks its strongest form as contested.
3. Says the learner is not asked to adopt it.
4. States the smaller checkable claim: whoever signs the packet will be asked about it, and no institution around the capstone will ask Claude.
5. Says this is a fact about where accountability lands, and it is enough to keep the choice with the learner.

**Source:** The driver's seat

## ES-ch15.59

What three things does the transfer reflection record, and how can you tell that the split is in the record rather than only in your head?

**Points:** 5

**Rubric (1 point each):**

1. Says it records one task you delegated more readily.
2. Says it records one capability you kept practicing.
3. Says it records one decision you retained.
4. Says each must be pointed to with a transcript line, a diff, or an edit; if you cannot point to one, the split happened in your head and not in the record.
5. Names the failure "reflection without evidence" for generic lessons that identify no changed decision or preserved capability.

**Source:** The driver's seat

## ES-ch15.60

What does the student submit for the capstone, what checklist does it follow, and what is the acceptance test?

**Points:** 5

**Rubric (1 point each):**

1. Says to submit the ten files with exact commands, kept under learning-artifacts/week-15/.
2. Names at least four items of the artifact brief checklist: Claude usage disclosure, source citations, student-versus-external code estimate, license, style declaration, and one decision revised after testing.
3. States the acceptance test: another student can reproduce the offline behavior and name what still needs human verification.
4. Says to include no credentials or restricted source material.
5. Says a Progress Reel can show mechanism, failure, recovery, and decision but cannot substitute for reproducibility.

**Source:** Ship It: submitting the packet

## ES-ch15.61

What do the verify-and-reflect steps ask you to run and reflect on, and what does a passing suite establish?

**Points:** 5

**Rubric (1 point each):**

1. Says to run the demo and the six tests, then your two additional tests, and preserve the commands, outputs, and your interpretation.
2. Says a passing suite establishes only the tested behavior, not universal reliability or permission to act.
3. Says to find the sentence in your packet a skeptical reader would attack first, and find its evidence.
4. Says that if you cannot find the evidence, you narrow the sentence or mark it pending.
5. Says the most useful reflection asks which of the three jobs you did least well, naming the artifact where it shows and the edit that would have fixed it.

**Source:** Verify and reflect

## ES-ch15.62

Match each case to the chapter's named failure and the job left undone: (a) ten long files pass but no central claim can be reproduced, (b) a recording shows success but omits commands and failed cases, (c) Claude-drafted stakeholder language is filed as permission, (d) a local-write approval is described as permission to publish. Then name the two failures that belong to drive.

**Points:** 5

**Rubric (1 point each):**

1. Says (a) is packet completeness theater, a failure of check.
2. Says (b) is demo-only evidence, a failure of check.
3. Says (c) is synthetic consent, a failure of conduct.
4. Says (d) is authority drift, a failure of conduct.
5. Names reflection without evidence and polish as quartile strategy as the drive failures, and says each failure is one of the three jobs left undone.

**Source:** Common capstone failures

## ES-ch15.63

How does the chapter position its Assessments, and what do Assessments 1 and 9 each ask you to do?

**Points:** 5

**Rubric (1 point each):**

1. Says the Assessments are ungraded practice that prepare the capstone evidence.
2. Says they do not create a second capstone, and the Lesson 15 knowledge check is self-review rather than an additional graded assignment.
3. Says Assessment 1 asks you to predict and run the empty-folder case, explain why ten missing issues establish structure rather than substance, and say what the `human_review` string hands to a person.
4. Says Assessment 9 asks you to record three expected Claude Code review findings, request a read-only critique, and judge each returned finding as genuine or a false positive using located evidence.
5. Says Assessment 9 also asks for a response of revision, defense, or an acknowledged limit, and a Gap Account separating a contingent miss from any gap that depends on the reviewer's kind.

**Source:** Assessments - ungraded practice

## ES-ch15.64

Summarize, in terms of the three jobs, what the chapter says you did across the capstone, and what you can now distinguish.

**Points:** 5

**Rubric (1 point each):**

1. Says that in conducting, you wrote the gate before Claude implemented.
2. Says that in checking, you built a graph whose edges could disagree and audited a reviewer.
3. Says that in checking, you also wrote down what the reviewer could not reach and signed only what the record supported, or withheld.
4. Says that in driving, you made the choice and kept the record that shows which work was yours.
5. Says you can now distinguish a structurally complete packet from a defensible capstone.

**Source:** Capabilities summary

## ES-ch15.65

State the chapter's closing question and explain what the mechanisms built across the course each did and did not do.

**Points:** 5

**Rubric (1 point each):**

1. Says the course began with watching prompts produce variation.
2. Names several of the mechanisms built, such as contracts, controllers, permissions, reviews, retrieval, protocols, configuration, plans, tool loops, memory, approval gates, and governance.
3. Says each mechanism made some claim easier to inspect.
4. Says each mechanism also exposed another claim it could not establish.
5. States the closing question: which part of this system can you explain from evidence, and which part still needs a person to decide.

**Source:** Closing question

## ES-ch15.66

How should you use Anthropic's Claude cookbooks and its evals guidance in the capstone, and what must you record?

**Points:** 5

**Rubric (1 point each):**

1. Says the cookbooks provide Python examples you may adapt when the mechanism genuinely matches your project.
2. Says to record the specific source, URL, revision or date, license, changes, and evidence for those changes.
3. Says not to adopt an entire stack merely because it is upstream.
4. Says "Demystifying evals for AI agents" can sharpen the distinction among tasks, trials, graders, transcripts, and outcomes, and should be compared with your evidence packet.
5. Notes the links were checked for the approved research packet on 2026-09-06, and current product guidance may change.

**Source:** Anthropics

## ES-ch15.67

Apply the chapter's halt test to a capstone whose only review is Claude's read-only critique. What is the test, what does it find, and what does it not validate?

**Points:** 5

**Rubric (1 point each):**

1. Says the companion's accountability chapter lists independent review among the requirements of a working accountability regime.
2. States the test: a named reviewer other than the builders, with authority to halt or revise.
3. Says Claude's read-only critique can comment but cannot stop anything.
4. Says you must find the person who can stop the workflow and the line where that authority is written down, and if you cannot, the review was commentary.
5. Says that without such a person the sign-off's "withheld" option has no one behind it, and that borrowing the test does not validate the rest of the regime or authenticate a signature.

**Source:** Computational Skepticism

## ES-ch15.68

Explain the "aim at the seams" diagnostic and the thin-sentence test from the Conducting AI note.

**Points:** 5

**Rubric (1 point each):**

1. Says a reviewer who confirms that each artifact is thorough has confirmed what is cheap to confirm.
2. Says the valuable finding names a relationship between two artifacts that each look fine alone.
3. Gives the example of a data-boundary exclusion that the action map's read capability quietly reaches around, and says to rewrite one prediction so it names two artifacts.
4. Says the thin-sentence test marks every sentence in the transfer reflection you could have written without knowing anything Claude's summary did not already state.
5. Says those marked sentences are the draft restated, and the reflection has to carry the others.

**Source:** Conducting AI

## ES-ch15.69

Describe the test for honest deprioritizing and the "AI should" / "Human should" split in the Irreducibly Human note.

**Points:** 5

**Rubric (1 point each):**

1. Describes the test: pick a task handed to Claude, such as the first-draft claim-to-passage matrix, and redo three rows by hand.
2. Says that if you cannot tell whether a row is right, you surrendered the task rather than deprioritized it, and the sign-off's "how" line claims a check you could not have performed.
3. Says AI should assemble existing evidence, run the Python packet validator, identify contradictions, compare bounded options including doing less, and draft summaries.
4. Says AI should not invent stakeholder consent, approvals, deployment decisions, personal reflection, or confidence unsupported by the record.
5. Says the human should decide whether the work serves the intended people, weigh competing goods the score does not settle, own the choice and remain answerable for revision, and treat claims about irreducible human capacities as argued positions.

**Source:** Irreducibly Human
