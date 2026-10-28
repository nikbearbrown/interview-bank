# Chapter 15: Supervised capstone

## MA-ch15.1

Check each statement that is true about the packet of ten files that each contain sixty copied `x` characters. Each statement is worth 1 point (5 points total).

- [ ] A. The files demonstrate a need, a boundary, and an implementation, although the text is repetitive.
- [ ] B. A tired reader can be relied on to catch a packet like this even when the validator passes it.
- [ ] C. The pass shows the validator is weak and should be replaced by a stricter one.
- [ ] D. Producing a packet has become cheap, so the cost has moved to finding out whether anything in it is true.
- [ ] E. The packet validator passes it and returns `structurally_complete: True`.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Nothing in them demonstrates a need, boundary, implementation, failure, independent result, consenting owner, or decision.
- B: The chapter says the validator would pass such a packet "and so might a tired reader".
- C: The chapter says this is the validator revealing its honest job, not a trick played on a weak validator.
- D: Claude can draft ten plausible files quickly; verification is where the cost now sits.
- E: All ten named Markdown files exist inside the packet and exceed forty stripped characters.

**Source:** Chapter 15 opening (before "What you will be able to do")

## MA-ch15.2

Check each statement that is true about the three jobs and the capstone as one workflow. Each statement is worth 1 point (5 points total).

- [ ] A. Drive means choosing the tools Claude uses so that the workflow runs end to end.
- [ ] B. Conduct means deciding before Claude implements.
- [ ] C. The final ship, narrow, defer, or stop decision should be defended mainly from the polish of the packet's presentation.
- [ ] D. Check means finding out what is wrong and signing only what the record supports.
- [ ] E. The packet should let another person trace a line from a real need and consenting owner through to transfer.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Drive means keeping the choices that are yours.
- B: This is the chapter's definition of the first job.
- C: It must be defended from the trace rather than from presentation quality.
- D: This is the chapter's definition of the second job.
- E: The capstone is one bounded workflow, not ten unrelated documents.

**Source:** Chapter 15 opening (before "What you will be able to do")

## MA-ch15.3

Check each statement that is true about the four predictions the chapter asks you to make and preserve before reading the validator. Each statement is worth 1 point (5 points total).

- [ ] A. One prediction asks what happens when `brief.md` is a symbolic link to a file outside the packet.
- [ ] B. One prediction asks how many issues an empty folder will return.
- [ ] C. One prediction asks whether ten polished files can prove that a real stakeholder consented.
- [ ] D. One prediction asks whether a five-character `brief.md` counts as present or insufficient.
- [ ] E. You should revise the predictions after reading the validator so they match what it does.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The third of the four predictions.
- B: The first of the four predictions.
- C: The fourth of the four predictions.
- D: The second of the four predictions.
- E: The instruction is to preserve the predictions.

**Source:** What you will be able to do

## MA-ch15.4

Check each statement that matches the chapter's account of the three jobs and their devices. Each statement is worth 1 point (5 points total).

- [ ] A. A build with no driver's seat is a task Claude completed and nobody chose.
- [ ] B. The evidence and audit-note artifacts belong to Drive.
- [ ] C. At capstone scale, the Check device is the claim-to-evidence graph, the reviewer audit, and the Gap Account.
- [ ] D. A build with no gate is improvised.
- [ ] E. Conduct covers the brief, data-boundary, action-surface-map, plan, gates, and pre-mortem.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Without the driver's seat nobody owns the choice to use the work.
- B: They are listed under Check.
- C: That is the sign-off.
- D: Removing the gate leaves nothing on record before Claude implements.
- E: These six pre-build artifacts are the gate.

**Source:** Three jobs, one packet

## MA-ch15.5

Check each statement that is true about what "in the wild" means for a capstone. Each statement is worth 1 point (5 points total).

- [ ] A. A real capstone requires unrestricted access to somebody else's systems.
- [ ] B. A workflow that reaches more systems demonstrates more ambition.
- [ ] C. The workflow serves a real context with a known owner, approved data, and explicit boundaries.
- [ ] D. Reality enters through consequences, constraints, and evidence.
- [ ] E. Every action added is something a person must be able to check, and that attention is finite.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It is not unrestricted access.
- B: Ambition is demonstrated through control, not surface area.
- C: This is the chapter's definition.
- D: Not through maximal autonomy.
- E: This is why scope must be narrow enough to supervise.

**Source:** "In the wild" means bounded reality

## MA-ch15.6

Check each statement that is true about the owner and consent. Each statement is worth 1 point (5 points total).

- [ ] A. You identify who can authorize the workflow as well as who benefits and who may be affected.
- [ ] B. Consent can be written as fixture text if it is clearly labeled as an example.
- [ ] C. If consultation is pending, you may proceed with private data once the pending decision is labeled.
- [ ] D. The capstone begins with a need stated by the person or team who owns the work.
- [ ] E. Claude can draft the questions you should put to the owner.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: All three are named at the start.
- B: Consent cannot be generated as fixture text.
- C: Constrain the project to synthetic or public data and label the remaining decision.
- D: Then you identify who benefits, who may be affected, and who can authorize.
- E: But nothing it writes is the owner's answer.

**Source:** "In the wild" means bounded reality

## MA-ch15.7

Check each statement that is true about non-purposes and success states in the brief. Each statement is worth 1 point (5 points total).

- [ ] A. The brief should leave out the conditions that make the result unacceptable, to keep the success state positive.
- [ ] B. The success state should be written after the run, from what the run produced.
- [ ] C. "The agent completed the task" is an inspectable success state.
- [ ] D. A non-purpose is unnecessary when the scope is already narrow.
- [ ] E. For a workflow that summarizes public course notes, a non-purpose could be that it does not publish without review.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Include conditions that make the result unacceptable.
- B: The brief is the first piece of the gate, written before Claude implements.
- C: The chapter calls it narration.
- D: Non-purposes give reviewers concrete misuse and scope-drift checks.
- E: The chapter gives this as an example.

**Source:** "In the wild" means bounded reality

## MA-ch15.8

Check each statement that is true about the stems and the order of the validator's checks. Each statement is worth 1 point (5 points total).

- [ ] A. `validate_packet` declares ten artifact stems and builds `root / (name + ".md")` for each.
- [ ] B. `sign-off` is one of the ten required stems.
- [ ] C. The containment check runs first.
- [ ] D. The presence check (the path must be a file) runs before the length check.
- [ ] E. The length check runs before containment, so a short symlink is reported as insufficient content.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: One path per stem.
- B: The sign-off ends the audit-note; it is not a stem.
- C: The order matters.
- D: Missing is reported before insufficient content.
- E: Containment runs first and reports `outside packet`.

**Source:** Tear down the packet validator

## MA-ch15.9

Check each statement that is true about the containment check. Each statement is worth 1 point (5 points total).

- [ ] A. It inspects the text of the target file for harmful instructions.
- [ ] B. The repository test links `brief.md` to `/etc/hosts` and expects `brief: outside packet`.
- [ ] C. It catches a required filename implemented as a symbolic link to an external target.
- [ ] D. It is the check that reports a missing artifact.
- [ ] E. It shows that a file inside the packet is safe to trust.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A malicious file physically inside the packet can still contain harmful instructions.
- B: This is the test the chapter describes.
- C: The resolved path must remain relative to the resolved root.
- D: The presence check reports `name: missing`.
- E: The check is about containment, not content trust.

**Source:** Tear down the packet validator

## MA-ch15.10

Check each statement that is true about the presence and length checks. Each statement is worth 1 point (5 points total).

- [ ] A. The forty-character threshold lets the validator judge whether a file is relevant to the capstone.
- [ ] B. The forty-character count includes the whitespace surrounding the text.
- [ ] C. An empty temporary directory produces ten issues, one for each required stem.
- [ ] D. A file that exists but is too short produces `name: missing`.
- [ ] E. A missing artifact produces `name: missing`.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It cannot judge relevance, truth, authorship, evidence, or quality.
- B: The check is on the stripped text.
- C: The approved research fixture observed that count.
- D: It produces `name: insufficient content`; missing is for a path that is not a file.
- E: The second check.

**Source:** Tear down the packet validator

## MA-ch15.11

Check each statement that is true about the dictionary `validate_packet` returns. Each statement is worth 1 point (5 points total).

- [ ] A. `structurally_complete` is computed as `not issues`.
- [ ] B. The `human_review` string appears only when the issues list is non-empty.
- [ ] C. A repository test confirms that "understanding" remains in the human-review message.
- [ ] D. `structurally_complete: True` means the packet's substance has been approved.
- [ ] E. The `human_review` string is a disclaimer the reader can skip.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: It is true exactly when the issues list is empty.
- B: It is part of the returned dictionary in every case.
- C: The message is part of the contract.
- D: Structural completeness deliberately stops before substantive approval.
- E: The chapter says it is part of the contract, not a disclaimer to skip.

**Source:** Tear down the packet validator

## MA-ch15.12

Check each statement that is true about why the validator is deliberately narrow. Each statement is worth 1 point (5 points total).

- [ ] A. A path resolution and a character count are weak checks because they ignore how good the prose sounds.
- [ ] B. A check worth having fails in the same way as the thing it checks.
- [ ] C. The remedy for the meaningless-packet pass is a stronger validator with a relevance score.
- [ ] D. A mechanical check is reliable exactly where it is narrow.
- [ ] E. Asking it to judge relevance would require a heuristic such as a keyword list or a score.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: That indifference is why they cannot be fooled by fluency.
- B: It should fail differently.
- C: The remedy is not a better validator.
- D: Narrowness is the point.
- E: Which fluent prose tends to satisfy.

**Source:** Tear down the packet validator

## MA-ch15.13

Check each statement that is true about the validator fixtures in the worked example. Each statement is worth 1 point (5 points total).

- [ ] A. If `brief.md` is a symlink whose target resolves outside the packet, the validator reports `brief: outside packet`.
- [ ] B. A packet containing only a five-character `brief.md` returns ten issues in total.
- [ ] C. Ten files of repeated `x` characters longer than forty produce ten insufficient-content issues.
- [ ] D. In the symlink case the presence check reports the problem, because the target is a file.
- [ ] E. With only a five-character `brief.md` present, the brief's issue is insufficient content while nine others remain missing.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Containment runs before presence.
- B: One insufficient-content issue plus nine missing issues.
- C: Every path is inside the root, a file, and over the threshold, so the packet is reported structurally complete.
- D: Containment runs first.
- E: The issue changes from missing to insufficient content.

**Source:** Worked example: missing, escaping, meaningless, and useful

## MA-ch15.14

Check each statement that is true about the ten-repeated-strings packet and what it proves. Each statement is worth 1 point (5 points total).

- [ ] A. It is the decisive counterexample that presence and length do not establish substance.
- [ ] B. It is the fluency trap at its smallest.
- [ ] C. The remedy is a better validator.
- [ ] D. A pass from the validator shows that someone has checked the packet's contents.
- [ ] E. A connected real packet that clears the validator then needs no further review.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It passes with nothing in it.
- B: It is well formed and passes.
- C: The remedy is a sentence, inside the packet, saying what was checked.
- D: The pass invites that belief, but nothing was checked beyond structure.
- E: The table says it requires claim-level review.

**Source:** Worked example: missing, escaping, meaningless, and useful

## MA-ch15.15

Check each statement that is true about a useful `evidence.md` and a useful `audit-note.md`. Each statement is worth 1 point (5 points total).

- [ ] A. Writing "tests passed" is enough for an `evidence.md`.
- [ ] B. The validator can tell a useful `evidence.md` from a long one.
- [ ] C. A useful `audit-note.md` predicts review findings before Claude critiques the packet.
- [ ] D. A useful `evidence.md` maps claims to checks that can disagree.
- [ ] E. A useful `evidence.md` records exact commands, versions, inputs, outputs, failures, and interpretations.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The chapter says it does not merely say that.
- B: It sees only that both files are long.
- C: It also records whether each was revised, defended, or acknowledged.
- D: That is what makes it evidence.
- E: It does not merely say "tests passed".

**Source:** Worked example: missing, escaping, meaningless, and useful

## MA-ch15.16

Check each statement that correctly describes one of the six pre-build artifacts. Each statement is worth 1 point (5 points total).

- [ ] A. The gates artifact is one of the six artifacts written before Claude executes anything.
- [ ] B. The plan records predicted failures, each with detection, owner, response, and residual risk.
- [ ] C. The data-boundary labels data public, synthetic, internal, personal, or unknown by the project's real policy.
- [ ] D. The action-surface-map separates capability from authority and flags external or irreversible effects.
- [ ] E. The brief states the need, consenting owner, affected people, success condition, non-purpose, decision scope, and what would make the workflow inappropriate.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Together the six pre-build artifacts are the gate.
- B: That describes the pre-mortem.
- C: Not by the label most likely to pass.
- D: It shows what the workflow can read, propose, write, send, or publish.
- E: The brief's contents.

**Source:** Ten artifacts, one argument

## MA-ch15.17

Check each statement that is true about the `plan`, `gates`, and `pre-mortem` artifacts. Each statement is worth 1 point (5 points total).

- [ ] A. The plan lays out evidence-producing steps with dependencies, stop conditions, budgets, and replanning triggers.
- [ ] B. Each pre-mortem entry has detection, owner, response, and residual risk.
- [ ] C. The gates list stale state, invalid calls, injection, and duplicate actions, each with detection and owner.
- [ ] D. The pre-mortem covers only the failure types the chapter lists.
- [ ] E. The gates bind consequential proposals to exact content and responsible decisions.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The plan's contents.
- B: It predicts failures before the build.
- C: That describes the pre-mortem.
- D: It also covers other project-specific failures.
- E: With evidence, effects, rollback limits, expiry, and what happens while review is pending.

**Source:** Ten artifacts, one argument

## MA-ch15.18

Check each statement that is true about the artifacts that record and judge the build. Each statement is worth 1 point (5 points total).

- [ ] A. A screenshot alone is enough to make the artifact reproducible.
- [ ] B. The `evidence` artifact distinguishes code inspection, deterministic fixture output, model output, human observation, and external product behavior.
- [ ] C. The `artifact` is the usable output, or a precise pointer and reproduction route.
- [ ] D. The `audit-note` ends with the Gap Account and the sign-off.
- [ ] E. The `transfer-reflection` records only what Claude did, leaving the human decision to the audit-note.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A screenshot alone is not reproducibility.
- B: The five kinds of evidence.
- C: The artifact's definition.
- D: It also records predictions, findings, responses, failed cases, and corrections.
- E: It holds the final ship, narrow, defer, or stop decision and its reason.

**Source:** Ten artifacts, one argument

## MA-ch15.19

Check each statement that is true about cross-references between the artifacts. Each statement is worth 1 point (5 points total).

- [ ] A. The pre-mortem predicts a failure that is demonstrated in the audit note.
- [ ] B. The brief's success criterion maps to the action-surface map.
- [ ] C. A validator can check these cross-references, so Claude's pointers can be accepted once it passes.
- [ ] D. Without cross-references the ten documents still form one argument.
- [ ] E. The brief's success criterion maps to evidence.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Another of the example links.
- B: It maps to evidence; the data boundary constrains the action map.
- C: A validator cannot check them; each reference is a claim to confirm by opening the target.
- D: Without links they remain ten islands.
- E: One of the chapter's example links.

**Source:** Ten artifacts, one argument

## MA-ch15.20

Check each statement that is true about the short-version gate you write before Claude implements anything. Each statement is worth 1 point (5 points total).

- [ ] A. The gate includes a wrong version of the run that your checks must catch: one that completes, reads well, and leaves the wrong state.
- [ ] B. The design section names the workflow, the owner, the approved data, and the one action that matters, and says whose choices they are.
- [ ] C. Claude can write the gate for you without defeating its purpose.
- [ ] D. The contract states what the workflow must refuse, such as counting a retrieved passage as support when it does not entail the claim.
- [ ] E. If your checks cannot tell the wrong version from the right one, the gate is finished once the tests pass.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: For example a fluent draft whose citation does not support its claim.
- B: Claude can challenge each of them; it did not make any.
- C: Claude can sharpen the gate but cannot write it for you.
- D: It also states the observable state that means done and the conditions that make the result unacceptable.
- E: Then the gate is not finished.

**Source:** The gate: Claude proposes, Python constrains

## MA-ch15.21

Check each statement that is true about the failure sentence and what the build may claim. Each statement is worth 1 point (5 points total).

- [ ] A. The build may claim that the workflow is safe once the staged failure is rejected.
- [ ] B. The failure sentence is added to the pre-mortem after the run as its closing entry.
- [ ] C. The failure sentence names the failure you will stage and what you expect each mechanism to do with it.
- [ ] D. The build may claim that the owner consents to uses beyond the brief.
- [ ] E. The failure sentence is dated and written before the run.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It may claim only a bounded local result under recorded conditions.
- B: It is the lead entry, written before the run.
- C: That is its content.
- D: Consent beyond the brief is outside what the build can claim.
- E: It is one dated sentence, written before the run.

**Source:** The gate: Claude proposes, Python constrains

## MA-ch15.22

Check each statement that is true about "Claude proposes, Python constrains." Each statement is worth 1 point (5 points total).

- [ ] A. Python holds whatever must be the same every time, such as which tools exist and whether a path stays inside the approved root.
- [ ] B. Telling Claude "do not publish" is a sufficient publication boundary.
- [ ] C. Claude does the language work: drafting, summarizing, and proposing a tool call.
- [ ] D. Every boundary you code is a case you foresaw, so an unforeseen case passes straight through.
- [ ] E. A prompt-injected source should not be able to grant itself tools.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Plus whether a proposal matches approved content and what gets recorded.
- B: A prompt is a request, not a boundary; the boundary is an application that lacks or gates the capability.
- C: The division of labor.
- D: This is why the gate also asks what a failure looks like.
- E: Which tools exist is held in the application, not in the prompt.

**Source:** The gate: Claude proposes, Python constrains

## MA-ch15.23

Check each statement that agrees with the chapter's guidance on building the controller and any live path. Each statement is worth 1 point (5 points total).

- [ ] A. The final claim is the record least likely to say more than the model request and application result support.
- [ ] B. A missing live run must never be replaced with invented output.
- [ ] C. A live Messages path should be opt-in and should identify the model actually used.
- [ ] D. Validate tool names and arguments in Python, and resolve paths before acting.
- [ ] E. Inject a callable into the controller where possible so that tests do not need network access.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It is the part most likely to say more.
- B: Live behavior is evidence about a real run under recorded conditions.
- C: Along with bounded requests, protected credentials, and recorded cost-bearing behavior.
- D: These are Python's jobs.
- E: Start offline.

**Source:** The gate: Claude proposes, Python constrains

## MA-ch15.24

Check each statement that is true about the Build It baseline. Each statement is worth 1 point (5 points total).

- [ ] A. You write your own `validate_packet` before consulting the reference, from the ten names and the three conditions.
- [ ] B. Your validator is the record of what you understood after Claude finished.
- [ ] C. You add at least two tests of your own: a meaningful success outside the demo and a failure that would matter in your capstone.
- [ ] D. You need not state what remains untested when every test passes.
- [ ] E. You can audit a containment check you have never tried to break.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Build first, then compare.
- B: It is the record of what you understood before Claude touched anything.
- C: Beyond the Practice Lab cases.
- D: The baseline includes stating what remains untested.
- E: The chapter says you cannot.

**Source:** Build It: the baseline

## MA-ch15.25

Check each statement that is true about conducting Claude Code against your gate. Each statement is worth 1 point (5 points total).

- [ ] A. You preserve your prompt, the plan, the diff, the commands, and the outputs, with the date and displayed model label.
- [ ] B. A failing test is often a gap in the gate.
- [ ] C. You give Claude the gate (the six artifacts and the test list), not your implementation.
- [ ] D. If Claude handled a boundary you missed, revising your gate violates design-first.
- [ ] E. You ask Claude to propose a deliberately wrong version and test by hand whether it still passes your checks.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: If a session failed or did not run, record that rather than substituting a fixture.
- B: Claude had only what you wrote.
- C: Then you run your tests on what it returns, yourself.
- D: That is a re-engagement; you log the reopening and its reason.
- E: If it does, your checks were too weak.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch15.26

Check each statement that is true about a controlled failure. Each statement is worth 1 point (5 points total).

- [ ] A. You preserve only the reported outcome, since the independently observed outcome is redundant.
- [ ] B. A gate you have never seen fail has not been tested.
- [ ] C. A successful happy-path run shows the gate works, because every check passed.
- [ ] D. Choose the most dramatic failure available, even if it cannot be reproduced safely.
- [ ] E. You predict the failure before running it.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Preserve the reported outcome, the independently observed outcome, and the gap between them.
- B: The chapter states this directly.
- C: A polished happy-path demo proves very little.
- D: Choose one that matters and can be reproduced safely.
- E: That prediction is the sentence you wrote in the gate.

**Source:** Controlled failure and reviewed recovery

## MA-ch15.27

Check each statement that is true about the source-grounded report example and reviewed recovery. Each statement is worth 1 point (5 points total).

- [ ] A. The plan may narrow the claim, select a different approved source, add an abstention rule, or defer.
- [ ] B. A later success is compared with the original failure and checked independently.
- [ ] C. A changed proposal after recovery skips its gate because the failure already informed it.
- [ ] D. The chapter's trace of the deadline-claim failure is a recorded run from the course fixtures.
- [ ] E. Recovery is not "ask Claude again until it passes."

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The recovery options listed.
- B: The changed proposal also goes through its gate again.
- C: It goes through its gate again.
- D: The chapter calls it a constructed illustration, not a recorded run.
- E: A human or declared policy reviews why the case failed.

**Source:** Controlled failure and reviewed recovery

## MA-ch15.28

Check each statement that is true about independent routes to checking. Each statement is worth 1 point (5 points total).

- [ ] A. A demo edited to show only success is the strongest evidence of supervision.
- [ ] B. If Python calculates a total, running the same calculation again is an independent check.
- [ ] C. If Claude drafts the claim, Python can validate source identifiers and structure while a person inspects semantic support.
- [ ] D. Failed output should be discarded to keep the record clean.
- [ ] E. Two Claude prompts that share the same context are independent checks of each other.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It hides the most valuable part of supervision.
- B: A separate derivation can check it; rerunning the same route shares its mistakes.
- C: Different routes fail differently.
- D: Preserve failed output when privacy and safety permit.
- E: They are not automatically independent.

**Source:** Controlled failure and reviewed recovery

## MA-ch15.29

Check each statement that is true about the prediction-lock and the casebook entry. Each statement is worth 1 point (5 points total).

- [ ] A. "Look at it and iterate" means re-prompting until the output looks right.
- [ ] B. The prediction is added to the entry after execution, once the result is known.
- [ ] C. A prediction-lock means writing what you expect, dated, before you observe, and never editing it afterward.
- [ ] D. A casebook entry merges the system-reported and independently observed outcomes into one result field.
- [ ] E. The learning is the gap between the prediction and what happened.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The chapter says it never means that.
- B: Item one is the prediction recorded before execution.
- C: The habit the chapter takes from Computational Skepticism for AI.
- D: They are separate items four and five of the eight-part entry.
- E: Hindsight is kept from smoothing the story.

**Source:** The miniature casebook

## MA-ch15.30

Check each statement that agrees with the chapter's guidance on recording a casebook entry. Each statement is worth 1 point (5 points total).

- [ ] A. If you expected the system to refuse and it accepted, record that.
- [ ] B. If no failure occurs, manufacture a surprising error so the casebook is more convincing.
- [ ] C. One observed miss proves a permanent limitation of every future model.
- [ ] D. If the checker correctly rejected, no explanation is needed because the rejection speaks for itself.
- [ ] E. One clean run establishes general reliability.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Honest recording of the miss.
- B: Do not manufacture a surprising error for drama.
- C: It supports only a bounded claim about this workflow, case, and check.
- D: Explain which mechanism did the work.
- E: It does not.

**Source:** The miniature casebook

## MA-ch15.31

Check each statement that agrees with the chapter's guidance on predicting the reviewer's findings. Each statement is worth 1 point (5 points total).

- [ ] A. A prediction has to forbid something.
- [ ] B. Record the displayed model label and the date.
- [ ] C. Predict three specific findings, each with an artifact location and a reason.
- [ ] D. "The review will find weak integration" is a good prediction because it will almost certainly be matched.
- [ ] E. Mark each prediction as a finding you expect to be genuine or a false positive.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Otherwise anything can match it.
- B: A later run of the reviewer may differ.
- C: Before asking for critique.
- D: It can be matched by anything, so it teaches nothing.
- E: So the reviewer's judgment can be scored later.

**Source:** Audit the reviewer

## MA-ch15.32

Check each statement that agrees with the chapter's guidance on handling the reviewer's findings. Each statement is worth 1 point (5 points total).

- [ ] A. Rejecting every finding shows independence.
- [ ] B. To defend a finding away, it is enough to say the packet already covers it.
- [ ] C. A finding without located evidence is not a finding.
- [ ] D. Accepting every finding is the safe default.
- [ ] E. Request the critique without allowing edits, and preserve the actual response.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Rejecting every finding is the mirror-image failure.
- B: Defend by citing the exact passage and explaining why the critique missed it.
- C: Locate the evidence for each row.
- D: Accepting every finding is a failure; a misreading you accept is someone else's error signed as yours.
- E: The review is one more output to evaluate.

**Source:** Audit the reviewer

## MA-ch15.33

Check each statement that agrees with the chapter's guidance on evaluating the reviewer itself. Each statement is worth 1 point (5 points total).

- [ ] A. Credit the hit rate over the specificity of your reasoning.
- [ ] B. Score each prediction as matched, partly matched, or missed.
- [ ] C. A finding can be treated as established when the reviewer states it confidently.
- [ ] D. A clean review proves the packet is sound.
- [ ] E. The course holds a measurement of how often such a review is wrong about a packet like yours.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Credit specificity of reasoning over the hit rate.
- B: The scoring scheme.
- C: Treat every finding as a hypothesis to check.
- D: A clean review is corroboration, not proof.
- E: The course holds no such measurement.

**Source:** Audit the reviewer

## MA-ch15.34

Check each statement that is true about contingent misses and structural gaps. Each statement is worth 1 point (5 points total).

- [ ] A. A second pass by the same reviewer closes a gap that comes from sharing the draft's model and context.
- [ ] B. A contingent miss is one that a better prompt, a second run, a differently built reviewer, or more evidence would close.
- [ ] C. For a contingent miss, you record it as a permanent limit of the review rather than fixing it.
- [ ] D. "Structural" means no reviewer could ever close the gap.
- [ ] E. A structural gap for this review turns on the kind of reviewer, a model that reads only your packet.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A same-model reviewer shares the blind spots.
- B: The weak version of a Gap Account.
- C: You fix it, or run the better review, and say so.
- D: It means owing to the reviewer's kind and access, not "for all time".
- E: It is recorded as structural for this review.

**Source:** The Gap Account

## MA-ch15.35

Check each statement that is true about the patterns of structural gap. Each statement is worth 1 point (5 points total).

- [ ] A. A consequence visible only from inside a relationship you answer to, such as an agreement that came with an unwritten condition.
- [ ] B. A reviewer that shares the draft's model and context shares its blind spots.
- [ ] C. An asymmetry of stakes: you will bear the consequence and the reviewer will not.
- [ ] D. A gap is permission to stop working on the final claim.
- [ ] E. A judgment grounded in domain experience the packet never stated, such as a number that is fine on paper and wrong for this site.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The first pattern.
- B: So a second pass by the same reviewer does not close the gap.
- C: The third pattern.
- D: A gap is a boundary on the final claim, not permission to give up.
- E: The second pattern.

**Source:** The Gap Account

## MA-ch15.36

Check each statement that is true about the companion book's claim and your own Gap Account. Each statement is worth 1 point (5 points total).

- [ ] A. For each gap you should name the model that is expected to close it.
- [ ] B. The companion book argues that no reviewer of any capability can reach what depends on being situated, having a stake, and being accountable.
- [ ] C. The course treats that claim as an argued position and does not ask you to agree with it or prove it.
- [ ] D. Your Gap Account claims only that this review, on this packet, did not reach this item, that repeating it would not, and that this person can.
- [ ] E. One observed miss shows that no future model could find the issue.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Name the evidence or expertise that could help and the person accountable for the decision now.
- B: It grounds this in philosophy and safety literature on correlated errors.
- C: The chapter says so directly.
- D: A smaller claim you can check.
- E: It sets a boundary for the decision now, nothing more.

**Source:** The Gap Account

## MA-ch15.37

Check each statement that is true about mapping central claims to checks. Each statement is worth 1 point (5 points total).

- [ ] A. "The workflow is safe" is probably too broad and should be decomposed.
- [ ] B. "The report is source-grounded" needs claim-to-passage inspection.
- [ ] C. "The owner consented" can be supported by text Claude drafted in the owner's voice.
- [ ] D. "The report was created" can map to file existence and read-back.
- [ ] E. File existence is enough to show that a report is source-grounded.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Into smaller claims that can be checked.
- B: File existence would not show it.
- C: It needs a real decision record, not model text.
- D: A check suited to that claim.
- E: Source-grounding needs inspection of claims against passages.

**Source:** Independent verification and outcome state

## MA-ch15.38

Check each statement that agrees with the chapter's guidance on inspecting outcome state. Each statement is worth 1 point (5 points total).

- [ ] A. State exactly what was observed.
- [ ] B. An agent can execute the planned calls while the destination remains wrong.
- [ ] C. Inspect the resulting state, not only the trajectory.
- [ ] D. A file write can succeed locally without being committed or published.
- [ ] E. A success code from a sent request shows that the intended person received it.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The standard for reporting outcomes.
- B: The trajectory looks fine but the state is not.
- C: The planned calls may all run while the destination is wrong.
- D: So a write is not a publication.
- E: The intended person may never receive it.

**Source:** Independent verification and outcome state

## MA-ch15.39

Check each statement that agrees with the chapter's guidance on building the claim-to-evidence graph. Each statement is worth 1 point (5 points total).

- [ ] A. Once Claude has drafted the graph, its edges count as verified.
- [ ] B. Claude can draft the first version quickly because it is an index-and-cross-reference task.
- [ ] C. Checking an edge is as cheap as producing it.
- [ ] D. Start with the final recommendation and break it into smaller claims until each can be checked by one or more artifacts.
- [ ] E. You decide whether each edge is real, because an edge is a claim that this evidence bears on that claim.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Checking an edge means opening its target.
- B: Drafting is cheap.
- C: Output is cheap and verification is not.
- D: The method.
- E: Edges must be verified.

**Source:** Build a claim-to-evidence graph

## MA-ch15.40

Check each statement that is true about the recommendation "Narrow the workflow to create a local source-grounded draft, retain only public fixtures for one day, and require a human before publication." Each statement is worth 1 point (5 points total).

- [ ] A. The claim that publication is gated needs no evidence because the recommendation states it.
- [ ] B. It contains at least six claims.
- [ ] C. It is a single claim, so one check of the draft is enough.
- [ ] D. One of its claims is that deletion follows the stated day boundary.
- [ ] E. One of its claims is that the draft uses approved sources.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The graph maps it to a rejected no-decision fixture.
- B: The chapter lists six.
- C: Each claim is mapped separately.
- D: The fifth listed claim.
- E: The second listed claim.

**Source:** Build a claim-to-evidence graph

## MA-ch15.41

Check each statement that is true about the rows of the claim-to-evidence table. Each statement is worth 1 point (5 points total).

- [ ] A. For "local draft exists" the evidence is the resolved path, read-back, and diff, and the residual gap is later mutation.
- [ ] B. An event trace can show no publish action inside the instrumented workflow but not every possible external channel.
- [ ] C. The residual-gap column prevents the graph from becoming decorative certainty.
- [ ] D. For "publication needs approval" the residual gap is interpretation disagreement.
- [ ] E. For "fixtures are public" the decision owner is the data owner and the residual gap is misclassification.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Row one.
- B: A limit that feeds the sign-off's "not checked" line.
- C: Every evidence route has scope.
- D: That row's gap is stolen credentials.
- E: Row four.

**Source:** Build a claim-to-evidence graph

## MA-ch15.42

Check each statement that is true about orphan nodes and circular support. Each statement is worth 1 point (5 points total).

- [ ] A. A claim with no evidence should be removed, narrowed, or marked pending.
- [ ] B. The audit note can establish that the evidence is correct by summarizing `evidence.md`, even if `evidence.md` cites the audit note.
- [ ] C. An artifact that supports no claim is harmless.
- [ ] D. Evidence cited by many claims deserves less scrutiny, because it has been reused so often.
- [ ] E. A decision with no named owner is unresolved.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: An orphan claim.
- B: That is circular support.
- C: It may be busywork.
- D: It deserves extra scrutiny; one defect can collapse several conclusions.
- E: Another orphan.

**Source:** Build a claim-to-evidence graph

## MA-ch15.43

Check each statement that agrees with the chapter's guidance on the contradiction pass and freezing the review candidate. Each statement is worth 1 point (5 points total).

- [ ] A. Resolve a contradiction by determining which artifact is authoritative, correcting dependent claims, and preserving the revision reason.
- [ ] B. Resolve a contradiction by choosing the newest document.
- [ ] C. If a consequential file changes after review, the old approval continues for the unchanged parts without new checks.
- [ ] D. Compare the brief's declared purpose with the implemented tools, and the action map with the trace.
- [ ] E. Freeze the review candidate by revision or digest so that later edits cannot masquerade as reviewed work.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Not by recency.
- B: The chapter says not to.
- C: It is a new review candidate; rerun the checks whose premises changed plus the integration checks.
- D: Two of the comparisons.
- E: The freeze.

**Source:** Build a claim-to-evidence graph

## MA-ch15.44

Check each statement that agrees with the chapter's guidance on the handoff and on reproducing it as an experiment. Each statement is worth 1 point (5 points total).

- [ ] A. The participant should try live behavior first, since it is the most informative.
- [ ] B. Each question the participant must ask marks missing transfer evidence.
- [ ] C. After revising the documentation, you can assume the fix worked without rerunning.
- [ ] D. A handoff is a seam, and seams are where risk lives.
- [ ] E. Give a bounded participant only the documented prerequisites and commands, in a sanitized environment.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: They run the offline path first; live behavior comes later and only with explicit authorization.
- B: Examples: an unstated working directory or a globally installed dependency.
- C: Rerun from a clean-enough context.
- D: A packet only its author can run has a gate with one person behind it.
- E: So hidden knowledge shows up.

**Source:** Handoff that survives the author

## MA-ch15.45

Check each statement that agrees with the chapter's guidance on recording the handoff attempt and stating exclusions. Each statement is worth 1 point (5 points total).

- [ ] A. A handover without answers to the maintenance questions is still a durable contribution if the tests pass.
- [ ] B. If only local writes were authorized, the handoff may describe the work as published once the file is written.
- [ ] C. Reproduction is an observed property of a particular handoff, not an adjective awarded to documentation.
- [ ] D. Packaging your API keys with the handoff lets the new person run the live path.
- [ ] E. Record the attempt as evidence: environment, commands, failures, questions, and revisions.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Without those answers it is a demo, not a durable contribution.
- B: It must not imply publication.
- C: The standard for claiming it.
- D: Never package API keys; say who supplies which secret and how.
- E: The record of the experiment.

**Source:** Reproduce the handoff as an experiment

## MA-ch15.46

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can write the sign-off's words fluently, so it can also supply the "not checked" content.
- [ ] B. The sign-off is the last thing the audit-note says.
- [ ] C. The chapter's template is a signature the author completes once the tests pass.
- [ ] D. The sign-off can be written from the packet's text alone, without your own record.
- [ ] E. The graph's residual-gap column, the Gap Account, and the handoff exclusions feed it.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: What was not tested is the part a model has no record of.
- B: It closes the audit-note.
- C: It is the template and the standard, not a signature.
- D: Write it from your record.
- E: They supply its "not checked" content.

**Source:** The sign-off: the last thing the evidence says

## MA-ch15.47

Check each statement that is true about the sign-off template fields. Each statement is worth 1 point (5 points total).

- [ ] A. "How" says whether the check was by hand, by a test written before reading Claude's version, by recomputation, by a check that fails differently, or with Claude's help.
- [ ] B. "Not claiming" lists the claims the packet proves.
- [ ] C. "Cleared by" can name "the team" when several people contributed.
- [ ] D. "Not checked" includes each residual gap in the graph and each Gap Account item.
- [ ] E. "Checked" names which claims in the graph were checked against which evidence.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: And says which parts Claude helped with.
- B: It lists what is not claimed, such as that the workflow is safe.
- C: It needs a named person for each consequential decision.
- D: Plus live behavior if no live run was recorded.
- E: Name them.

**Source:** The sign-off: the last thing the evidence says

## MA-ch15.48

Check each statement that is true about the sign-off's verbs, withholding, and cost. Each statement is worth 1 point (5 points total).

- [ ] A. A sign-off buys speed and deniability, at the cost of answerability.
- [ ] B. A typed name authenticates the signer.
- [ ] C. Withholding is a legitimate outcome.
- [ ] D. A passing test supports the verb "safe".
- [ ] E. "Established" or "proven" are fine verbs whenever the checks passed.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It buys legible answerability and pays in speed and deniability.
- B: A typed name does not authenticate anyone.
- C: A process whose only permitted result is "signed" is a rubber stamp.
- D: A passing test supports "tested", not "safe".
- E: Only when a criterion supports them.

**Source:** The sign-off: the last thing the evidence says

## MA-ch15.49

Check each statement that agrees with the chapter's guidance on deciding among ship, narrow, defer, and stop. Each statement is worth 1 point (5 points total).

- [ ] A. The criteria are neutral facts, so there is no need to say who chose them.
- [ ] B. Write the recommendation first and then assemble the supporting facts.
- [ ] C. Passing structure and tests does not oblige deployment.
- [ ] D. Put ship, narrow, defer, and stop into one comparison against the same criteria.
- [ ] E. Claude can draft the comparison, including doing less, but it cannot supply the weights.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The criteria express values, so say who chose them.
- B: Do not.
- C: Evidence informs the decision; it does not make it.
- D: One comparison, same criteria.
- E: The criteria express values.

**Source:** Defend the four options against the same evidence

## MA-ch15.50

Check each statement that agrees with the chapter's guidance on when to ship and when to narrow. Each statement is worth 1 point (5 points total).

- [ ] A. Narrow when a smaller action surface, data set, or audience preserves value while reducing unsupported claims.
- [ ] B. Removing automatic publication may keep most of the value and keep the artifact local.
- [ ] C. Narrowing is a failure to ship.
- [ ] D. Ship requires that owners accept their roles, consent and authority exist, and recovery is credible.
- [ ] E. Ship when the evidence supports the bounded use in the brief, not any future expansion.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A design response to evidence.
- B: An example of narrowing.
- C: It is not a failure.
- D: Conditions for shipping.
- E: The scope of a ship decision.

**Source:** Defend the four options against the same evidence

## MA-ch15.51

Check each statement that agrees with the chapter's guidance on when to defer and when to stop. Each statement is worth 1 point (5 points total).

- [ ] A. Defer when the missing evidence, consultation, expertise, or capacity could realistically be obtained, and name the concrete condition and its owner.
- [ ] B. Stop when consent cannot be obtained.
- [ ] C. Effort already spent is evidence for continuing.
- [ ] D. Stop when a simpler non-AI process dominates.
- [ ] E. An indefinite "more research is needed" is an acceptable defer.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: For example until the data owner classifies one source.
- B: One of the stop conditions.
- C: It is not.
- D: Another stop condition.
- E: It evades the decision.

**Source:** Defend the four options against the same evidence

## MA-ch15.52

Check each statement that is true about the sensitivity test. Each statement is worth 1 point (5 points total).

- [ ] A. It asks whether the recommendation would change if retention fell from a year to a day.
- [ ] B. It asks whether the recommendation would change if the external-write capability were removed.
- [ ] C. Its purpose is to confirm that the original recommendation was right.
- [ ] D. It also asks whether the recommendation would change if the reviewer backlog doubled.
- [ ] E. It asks whether the recommendation would change if the owner withdrew consent or the independent checker disagreed once.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Another counterfactual.
- B: One of the counterfactuals.
- C: It reveals which assumptions actually drive the decision.
- D: The last counterfactual listed.
- E: Further counterfactuals.

**Source:** Defend the four options against the same evidence

## MA-ch15.53

Check each statement that is true about the final recommendation. Each statement is worth 1 point (5 points total).

- [ ] A. It includes the chosen option, rejected alternatives, evidence, affected interests, conditions, owner, review date, change triggers, and who may revisit it.
- [ ] B. It contains one sentence of epistemic restraint about what the packet does not establish.
- [ ] C. The epistemic-restraint sentence weakens the recommendation, so it belongs in an appendix.
- [ ] D. Once it is signed, the decision is closed to revisiting.
- [ ] E. It names only the chosen option, because rejected alternatives clutter it.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The required contents.
- B: That sentence is often the strongest evidence the author understands the system.
- C: It is often the strongest evidence of understanding.
- D: A later source change, incident, or stakeholder objection can reopen the choice.
- E: Rejected alternatives are part of the recommendation.

**Source:** Defend the four options against the same evidence

## MA-ch15.54

Check each statement that is true about Memo A and Memo B. Each statement is worth 1 point (5 points total).

- [ ] A. Memo B is Memo A with your name added.
- [ ] B. The labeled parts include what you add that the packet could not show and why the evidence should be trusted, citing graph rows rather than Claude's confidence.
- [ ] C. Memo A is the machine's analysis, here Claude's evidence assembly and option comparison.
- [ ] D. The separation diminishes your work by showing how much Claude did.
- [ ] E. A signature without the account behind it counterfeits accountability.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Memo B is not Memo A with your name added; it carries your own account.
- B: Plus what Claude produced, why this is the right action here, and the recommendation you sign.
- C: From Conducting AI.
- D: It makes your part defensible.
- E: The chapter's reason for keeping the judgments separable.

**Source:** Write the recommendation so the judgments are separable

## MA-ch15.55

Check each statement that matches the chapter's driver's-seat table. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can draft the comparison on your criteria and argue against your preferred row; you choose the criteria and weights.
- [ ] B. For the choice and the signature, Claude drafts and signs while you review.
- [ ] C. Claude can cross-reference, run `validate_packet`, and list contradictions; you decide which artifact is authoritative and recheck a sample by hand.
- [ ] D. Claude can obtain a real decision from the owner on your behalf.
- [ ] E. Claude gives one read-only critique and also writes the Gap Account for you.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The criteria express values.
- B: Claude does nothing beyond the draft.
- C: A list of contradictions does not say which document to believe.
- D: Claude drafts the questions; you obtain a real decision from a real owner.
- E: Claude gives one critique; you predict first, judge each finding, and write the Gap Account.

**Source:** The driver's seat

## MA-ch15.56

Check each statement that is true about the three verdicts from Irreducibly Human as applied to the table. Each statement is worth 1 point (5 points total).

- [ ] A. The last two rows of the table are supervise.
- [ ] B. The first row (evidence trail and validator) is deprioritize with a spot-check.
- [ ] C. Deprioritization is not deletion.
- [ ] D. The second and third rows of the table are supervise.
- [ ] E. The three verdicts are deprioritize, supervise, and protect.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: They are protect: consent and authority, and the choice and signature.
- B: Recheck a sample by hand.
- C: You can hand Claude the claim-to-passage matrix only because you can still check a row.
- D: Comparing the options and reviewing the packet.
- E: Hand over gladly, use and audit, keep.

**Source:** The driver's seat

## MA-ch15.57

Check each statement that agrees with the chapter's guidance on recording the split in the transfer reflection. Each statement is worth 1 point (5 points total).

- [ ] A. The split is recorded in the Gap Account.
- [ ] B. If you cannot point to a transcript line or an edit that shows each, the split happened in your head and not in the record.
- [ ] C. A transcript line, a diff, or an edit you made counts as evidence of the split.
- [ ] D. Generic statements of lessons are enough if they are well written.
- [ ] E. Record one task you delegated more readily, one capability you kept practicing, and one decision you retained.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It is recorded in the transfer reflection.
- B: Evidence of the split.
- C: From the Irreducibly Human note.
- D: That is the failure "reflection without evidence".
- E: The three-part split.

**Source:** The driver's seat

## MA-ch15.58

Check each statement that agrees with the chapter's guidance on submitting the packet. Each statement is worth 1 point (5 points total).

- [ ] A. Include credentials so a reviewer can run the live path.
- [ ] B. The artifact brief checklist includes a Claude usage disclosure, source citations, a student-versus-external code estimate, the license, the style declaration, and one decision you revised after testing.
- [ ] C. Submit the ten files with exact commands, kept under learning-artifacts/week-15/.
- [ ] D. Acceptance is concrete: another student can reproduce the offline behavior and name what still needs human verification.
- [ ] E. A Progress Reel can substitute for reproducibility if it shows mechanism, failure, and recovery.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Include no credentials or restricted source material.
- B: The checklist.
- C: The submission location.
- D: The acceptance test.
- E: It cannot substitute for reproducibility.

**Source:** Ship It: submitting the packet

## MA-ch15.59

Check each statement that correctly describes a common capstone failure. Each statement is worth 1 point (5 points total).

- [ ] A. Packet completeness theater is a failure of check: ten long files pass while no central claim is reproducible.
- [ ] B. Demo-only evidence is a recording that shows success but omits commands, inputs, versions, and failed cases.
- [ ] C. Shared-check dependence is a failure of drive.
- [ ] D. Synthetic consent is a failure of conduct.
- [ ] E. Authority drift is Claude-generated stakeholder language presented as permission.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The chapter's first failure.
- B: A failure of check.
- C: It is a failure of check.
- D: Each failure is one of the three jobs left undone.
- E: That is synthetic consent; authority drift is a local-write approval described as permission to publish.

**Source:** Common capstone failures

## MA-ch15.60

Check each statement that is true about the chapter's Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. Assessment 8 asks you to add cross-references and then trust them without opening the targets.
- [ ] B. Assessment 7 asks you to design a verifier that fails differently from the production route and name one assumption they still share.
- [ ] C. The Assessments are ungraded practice that prepare the capstone evidence.
- [ ] D. Assessment 9 asks you to accept every finding the reviewer returns as genuine.
- [ ] E. Assessment 4 asks you to select five central capstone claims, point to the artifact and evidence for each, and fill in the residual-gap column for the supported ones.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: You open every target and confirm it says what the pointer says.
- B: Independent check.
- C: They do not create a second capstone.
- D: You judge each finding as genuine or a false positive.
- E: Claim-to-artifact map.

**Source:** Assessments - ungraded practice

## MA-ch15.61

Check each statement that agrees with the chapter's guidance in the Anthropics section. Each statement is worth 1 point (5 points total).

- [ ] A. "Demystifying evals for AI agents" can sharpen the distinction among tasks, trials, graders, transcripts, and outcomes.
- [ ] B. The links were checked on 2026-09-06, so their guidance is guaranteed to stay current.
- [ ] C. When you adapt one example, adopt the whole upstream stack.
- [ ] D. For adapted code, record the specific source, URL, revision or date, license, changes, and evidence for those changes.
- [ ] E. The Claude cookbooks provide Python examples you may adapt when the mechanism genuinely matches your project.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Compare it with your evidence packet.
- B: Current product guidance may change.
- C: Do not adopt an entire stack merely because it is upstream.
- D: The record to keep.
- E: Adapt, do not adopt wholesale.

**Source:** Anthropics

## MA-ch15.62

Check each statement that is true about the halt test. Each statement is worth 1 point (5 points total).

- [ ] A. If you cannot find the person who can stop the workflow and the line where that authority is written down, the review was commentary.
- [ ] B. Borrowing this test validates the rest of the regime for your project and authenticates a signature.
- [ ] C. The plain test is a named reviewer other than the builders, with authority to halt or revise.
- [ ] D. Claude's read-only critique can comment but cannot stop anything.
- [ ] E. The companion's accountability chapter lists independent review among the requirements of a working accountability regime.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The result of applying the test.
- B: It borrows one test only.
- C: The test itself.
- D: So it fails the halt test on its own.
- E: The source of the test.

**Source:** Computational Skepticism

## MA-ch15.63

Check each statement that is true about aiming predictions at the seams. Each statement is worth 1 point (5 points total).

- [ ] A. The valuable finding names a relationship between two artifacts that each look fine alone.
- [ ] B. A prediction rewritten to name two artifacts aims at the seams.
- [ ] C. A reviewer who confirms each artifact is thorough has confirmed what is cheap to confirm.
- [ ] D. The best predictions name a single artifact so they can be checked quickly.
- [ ] E. One example is a data-boundary exclusion that the action map's read capability quietly reaches around.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The seam.
- B: The chapter asks you to rewrite one prediction so it names two artifacts.
- C: Per-artifact thoroughness is the cheap check.
- D: You are asked to rewrite one prediction so it names two artifacts.
- E: The chapter's illustration.

**Source:** Conducting AI

## MA-ch15.64

Check each statement that agrees with the chapter's guidance on the thin-sentence test for the transfer reflection. Each statement is worth 1 point (5 points total).

- [ ] A. The test is applied to the transfer reflection.
- [ ] B. Mark every sentence you could have written without knowing anything Claude's summary did not already state.
- [ ] C. A fluent, well-structured reflection passes the test.
- [ ] D. Those marked sentences are the draft restated.
- [ ] E. A reflection is acceptable if every sentence could have been written from Claude's summary alone.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: That is where thin sentences restate the draft.
- B: The test.
- C: Fluency is not the criterion; knowledge beyond Claude's summary is.
- D: The reflection must carry the others.
- E: Those sentences are the draft restated; the reflection has to carry others.

**Source:** Conducting AI

## MA-ch15.65

Check each statement that agrees with the chapter's guidance on the test for honest deprioritizing. Each statement is worth 1 point (5 points total).

- [ ] A. If you cannot tell whether a row you handed to Claude is right, the sign-off's "how" line claims a check you could not have performed.
- [ ] B. If you cannot tell whether a row is right, you surrendered the task rather than deprioritized it.
- [ ] C. Pick a task you handed to Claude, such as the first-draft claim-to-passage matrix, and redo three rows by hand.
- [ ] D. The final division of labor is capable assistance joined to accountable human purpose and judgment.
- [ ] E. The final division of labor is "AI writes and a human signs."

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The consequence for the sign-off.
- B: The diagnosis.
- C: The test.
- D: The chapter's statement.
- E: It is capable assistance joined to accountable human purpose and judgment.

**Source:** Irreducibly Human

## MA-ch15.66

Check each statement that is true about "AI should" and "Human should." Each statement is worth 1 point (5 points total).

- [ ] A. AI should assemble existing evidence, run the Python packet validator, identify contradictions, and compare bounded options including doing less.
- [ ] B. Human should own the ship, narrow, defer, or stop choice.
- [ ] C. The human's answerability ends once the AI drafts the revision.
- [ ] D. Human should treat claims about irreducible human capacities as propositions the assignment requires you to prove.
- [ ] E. AI should not invent stakeholder consent, approvals, deployment decisions, or personal reflection.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The AI responsibilities.
- B: And remain answerable for revision.
- C: The human remains answerable for revision.
- D: They are argued positions, not propositions to prove.
- E: Nor confidence unsupported by the record.

**Source:** Irreducibly Human
