# Chapter 10: Planning before acting

## ES-ch10.1

A plan has all eight fields set to the single string x. Predict what missing_fields returns for it, say what that result does and does not show about the plan, and say what the check is for.

**Points:** 5

**Rubric (1 point each):**

1. States that missing_fields returns an empty list because every field is bound to a nonempty (truthy) string.
2. Says the empty list is the correct result for the rule the function implements, not a bug.
3. Says the result does not show that the objective matters, the scope is safe, a risk is plausible, the verification tests the claim, or the stop condition is observable.
4. Says the check's job is to catch absence and false-valued entries under a declared list, that is, structural omissions.
5. Says this does not make field checks pointless; trouble begins when a clean form is presented as a trustworthy plan.

**Source:** Chapter 10: Planning before acting (opening)

## ES-ch10.2

The chapter says Claude implements well against a complete specification and badly against an incomplete one. Explain what Claude will and will not tell you about this, which decisions determine whether a build goes well, and what a plan is in the chapter's terms. Why is reviewing the plan the gate?

**Points:** 5

**Rubric (1 point each):**

1. States that Claude will not tell you which kind of specification, complete or incomplete, you gave it.
2. Names at least four of the decisions made before the build: which problem, which boundary, which order, which evidence between steps, which point to stop.
3. Defines a plan as those decisions written down where another person can challenge them.
4. States that reviewing the plan is the gate.
5. Explains that because these decisions are made before the build, the written plan is the place where another person can still say no.

**Source:** Chapter 10: Planning before acting (opening)

## ES-ch10.3

Chapter 1 named three jobs that stay with you. State what Conduct, Check, and Drive look like in this chapter's planning work.

**Points:** 5

**Rubric (1 point each):**

1. Conduct: the plan is the design that precedes implementation, and the reviewed plan is the gate, so nothing changes until a condition you can state is met.
2. Check: a plan predicts action and a result records it, so a complete form is not a plan and an acyclic graph is not an executable one.
3. Check: you review the plan with counterexamples before anything runs.
4. Drive: the choice of problem, and the values inside that choice, are yours.
5. Drive: Claude can suggest framings and attack your selection, and you defend it.

**Source:** Chapter 10: Planning before acting (opening)

## ES-ch10.4

The chapter's Python build is offline, yet it also uses Claude Code. Explain what part Claude Code plays, what status its returned plan has, and what you must do if the interface is unavailable.

**Points:** 5

**Rubric (1 point each):**

1. States that the Python build runs offline and needs no direct API credits.
2. Says Claude Code can propose or critique a plan through the assumed course account.
3. Says the returned plan remains a proposal.
4. Says that if the interface is unavailable you preserve that fact and complete the offline construction.
5. Says you must not invent a Claude-authored plan or a human approval to make the artifact look finished.

**Source:** Chapter 10: Planning before acting (opening)

## ES-ch10.5

A classmate says a plan should reproduce Claude's reasoning in full. Using the chapter, explain what a plan is, what it should expose, and why it is worth the most before anything has run.

**Points:** 5

**Rubric (1 point each):**

1. Says the plan is not hidden reasoning and need not reproduce private deliberation.
2. Describes the plan as a public action contract another person can critique.
3. Says it exposes the destination, allowed inputs and scope, intended steps, tools, risks, evidence, and stopping rule.
4. Says it is worth the most before anything has run because a revision costs a paragraph there and a rollback later.
5. Says a plan nobody reviewed is a draft however complete its form, so the review is the gate.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.6

Define a phase gate as Conducting AI uses the term, and explain how design by contract expresses the same idea. In this chapter's sense, what is a plan?

**Points:** 5

**Rubric (1 point each):**

1. Defines a phase gate as the explicit point where Claude's work stops and a person's begins.
2. Says the gate is stated as a specification of what each side handles.
3. Says it also includes a testable condition that must hold before the output moves downstream.
4. Explains that in design by contract you write the contract and the agent writes the implementation.
5. Says assertions or tests derived from your contract check the implementation, and that a plan is that contract for a whole piece of work.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.7

Describe the Boondoggle Score at the level the chapter does, how much weight the chapter places on its sorting questions, and how the eight fields relate to it.

**Points:** 5

**Rubric (1 point each):**

1. Says the Score lays out the prompts for Claude in dependency order.
2. Says it lists the human's actions in the same order.
3. Says it places a testable handoff condition between each Claude task and each human task.
4. Notes that it is the author's own instrument and that the five sorting questions have no external validation that the author knows of.
5. Says to treat the Score as a heuristic, not a diagnostic, and that the eight fields are a smaller instrument, this course's own review tool.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.8

A teammate says "design first" means freezing the plan before work starts. Respond using the chapter's reasoning about how problem and solution develop, what you do when a result contradicts the plan, and the chapter's narrower claim.

**Points:** 5

**Rubric (1 point each):**

1. Cites the design research that problem and solution develop together, so a move in the solution space can surprise you and force a reframing of the problem.
2. Says a plan is a controlled state with versions.
3. Says that when a result contradicts an assumption, you revise the plan and record the reason rather than pushing forward on a stale one.
4. Uses the discount-rule example: auditing the diff shows rounding was never specified, which reopens the requirement, and the instruction is to log it and go back.
5. States the narrower claim: the first version of the plan should exist and be reviewed before Claude changes anything, so that when evidence reopens a decision you can see which decision it was.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.9

Explain the error of the third kind and why its cost is highest when Claude executes a plan fluently. Say why choosing the problem comes before filling in the eight fields.

**Points:** 5

**Rubric (1 point each):**

1. Defines the error of the third kind as a right answer to the wrong problem.
2. Attributes the phrase, as Conducting AI uses it, to Allyn Kimball in 1957.
3. Says a perfectly ordered plan can optimize the wrong objective.
4. Says a polished, internally checked answer to the wrong question carries authority the question never earned.
5. Says the first decision in a plan, which problem it is for, is not in any of the eight fields.

**Source:** Formulate before you plan

## ES-ch10.10

Why not simply ask Claude to frame the problem first? Use the idea of a primary generator and explain what goes wrong with auditing afterward.

**Points:** 5

**Rubric (1 point each):**

1. Says the book argues that a system trained to continue text tends toward the common and likely, so its framing is the modal one, and that this is an argument about tendencies, not a theorem.
2. Defines the primary generator (Jane Darke) as a first, usually tacit idea of what this is really about that decides which solutions you can see.
3. Says you cannot start without one.
4. Says that if you have not named yours before Claude supplies its own, its anchor becomes yours by default, dressed as neutral analysis.
5. Says the audit then comes too late because you would be checking the output against the framing it already assumes.

**Source:** Formulate before you plan

## ES-ch10.11

State the distinctness test. Then apply it: in the plus-one regression, a patch returns the constant 3 and is applied without diagnosing the cause. Score it against formulation A (the input-two test goes green), B (the declared plus-one behavior restored without changing anything outside the learner module and its test), and C (the learner can explain the bug).

**Points:** 5

**Rubric (1 point each):**

1. States the test: would the two formulations require different solutions even to test; if one solution satisfies both, they are one formulation in two outfits.
2. Says the constant-3 patch passes A because input two gives 3.
3. Says it fails B because input five gives 3, not 6.
4. Says it fails C because the cause was never diagnosed, so the learner cannot explain it.
5. Concludes that this result separates A from B, and that formulations that disagree about whether a result succeeded are separate problems.

**Source:** Formulate before you plan

## ES-ch10.12

A correct x + 1 patch that Claude wrote is accepted by you without reading it. Score it against formulations A, B, and C of the plus-one regression, say which pair of formulations it separates, and say what the result implies about the interest formulation B leaves out.

**Points:** 5

**Rubric (1 point each):**

1. Says it passes A because the input-two test goes green.
2. Says it passes B because the declared plus-one behavior is restored within scope.
3. Says it fails C because the learner cannot explain the bug.
4. Says this result separates B from C.
5. Notes that B centers maintainers and callers and decenters the learner's understanding, so the plan should say so, for example by assigning a separate step to the learner's understanding.

**Source:** Formulate before you plan

## ES-ch10.13

Why must the constraint set for choosing among formulations be written before you score anything, and why is feasibility alone not enough? Name the two criteria the book adds.

**Points:** 5

**Rubric (1 point each):**

1. Says the constraint set is written before you score anything.
2. Says that if every criterion is about cost, time, and buildability, you have built a machine that selects the most tractable framing.
3. Says the most tractable framing is the one Claude would have picked unasked.
4. Names salience as an added criterion: if this is solved, does it address what matters here?
5. Names whose interests the framing centers and decenters as the other added criterion.

**Source:** Formulate before you plan

## ES-ch10.14

In the plus-one regression, say whose interests each of the three formulations centers. Then write one sentence that defends a selection and explain why silence about what was left out is a different thing.

**Points:** 5

**Rubric (1 point each):**

1. Says formulation A centers whoever reads the test report.
2. Says formulation B centers the maintainers and callers of the function.
3. Says formulation C centers the learner.
4. Says none centers everyone, so choosing one is choosing whom the plan does not serve, and the plan should say so.
5. Gives a defended selection such as "I chose B; it decenters the learner's understanding, which a separate step addresses" and calls silence about what was left out a laundered selection; the values decision sits inside the formulation, not after it.

**Source:** Formulate before you plan

## ES-ch10.15

Divide the formulation work between you and Claude. What can Claude do, what can it not do, and why does the practice not depend on settling the philosophical question about models?

**Points:** 5

**Rubric (1 point each):**

1. Says Claude can add candidates you missed.
2. Says Claude can find a result that passes one formulation and fails another.
3. Says Claude can attack your selection.
4. Says Conducting AI argues that a model cannot certify distinctness in your domain or make the values selection because both need situated judgment and a name on the decision, and that the chapter reads this as an argument, not a measurement.
5. Says the practice is to write your candidates first, let Claude extend and criticize them, and defend the one you pick, including what it leaves out; someone answers for the choice and Claude has no name to put there.

**Source:** Formulate before you plan

## ES-ch10.16

Explain what it means for a plan to have drifted from its purpose, and how carrying the selected formulation into the plan prevents it. Use formulation B of the plus-one regression as the example.

**Points:** 5

**Rubric (1 point each):**

1. Says the selection should be carried into the objective, scope, verification, and stop fields.
2. Says drift is when the selection lives only in introductory prose while the checks measure something else.
3. Applies it to B: the objective names the restored plus-one behavior within the learner module and its test, the scope excludes other files, and the verification tests the behavior beyond the single input-two case.
4. Says a defended selection also names what the chosen formulation leaves out.
5. Says the values decision sits inside the formulation and so must be reflected in the fields, not left after it.

**Source:** Formulate before you plan

## ES-ch10.17

List the eight required plan fields in the order the reference declares them. Explain what the code can see versus what a reviewer asks, and give the question for at least three fields.

**Points:** 5

**Rubric (1 point each):**

1. Lists objective, inputs, scope, steps, tools, risks, verification, and stop, in that order.
2. Says the code can only see whether a name is bound to a value.
3. Says a reviewer asks the question each name stands for.
4. Gives a correct question for at least three fields, for example objective: what outcome, stated so someone can tell whether it happened; scope: what may change and what must stay untouched; verification: what observation will support the completion claim.
5. Says each field is a place where a decision was made or was not.

**Source:** The eight fields are eight questions

## ES-ch10.18

For each of these entries, name the field it fills, explain why it passes missing_fields but fails review, and rewrite one of them so that a reviewer can challenge it: "Be careful", "Research", "Claude Code", "There may be risks".

**Points:** 5

**Rubric (1 point each):**

1. Maps the entries to fields correctly: "Be careful" to scope, "Research" to steps, "Claude Code" to tools, "There may be risks" to risks.
2. Says all four pass missing_fields because they are nonempty, truthy values.
3. Says they fail review because nobody can challenge them or tell whether they were done (no paths or exclusions, no output or finished test, no operations or approval boundary, no mitigation, owner, or stop trigger).
4. Rewrites at least one as a challengeable entry, for example scope as file paths, permitted operations, excluded systems, and output destinations, or tools as the tool, the reason, and the operations it may and may not perform.
5. States that this is the difference between a field that is present and a field that has a job.

**Source:** The eight fields are eight questions

## ES-ch10.19

Predict what missing_fields returns for a plan built with keys in this order: stop is False, verification is "run the learner tests", risks is 0, tools is None, steps is ["inspect", "fix"], scope is "learner test file only", inputs is [], and objective is "Fix the plus-one bug". Explain your reasoning and say what the result does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Gives the result ['inputs', 'tools', 'risks', 'stop'].
2. Explains the truth-value rule: absent and false-valued entries are missing, so an empty list, None, zero, and False all fail.
3. Says the list follows the order of the FIELDS tuple, not the order of the keys in the dictionary.
4. Identifies objective, scope, steps, and verification as passing because they hold nonempty truthy values.
5. Says the result does not show that the passing entries are meaningful, since the single string x would pass equally.

**Source:** What missing_fields actually checks

## ES-ch10.20

Argue that a check blind to meaning is still worth running, and say how to use it. Include the pattern from earlier chapters that the all-x plan repeats.

**Points:** 5

**Rubric (1 point each):**

1. Says the check is deterministic and cheap.
2. Says it fails differently from a reviewer: it never gets tired and never notices meaning.
3. Says to use it to clear the easy failures so that human attention goes to the hard ones.
4. Names at least two of the earlier-chapter examples: a strict format validator can pass false content, a permission flag can be true without authenticating a person, a plan-presence checker can pass empty language.
5. Says to keep the signal narrow instead of expecting one empty list to certify the artifact.

**Source:** What missing_fields actually checks

## ES-ch10.21

Explain why the chapter says steps are a graph and not a list. Use "verify has after: [build]" to explain what an arrow means, and say who decides which arrows exist and what the ordering function can and cannot do.

**Points:** 5

**Rubric (1 point each):**

1. Says steps are a graph and each arrow is an obligation.
2. Says that if verify has after: [build], then build must appear before verify.
3. Says verify may not be called ready until build has produced what verify needs.
4. Says you decide which arrows exist.
5. Says the function can only order the arrows you declared.

**Source:** Dependencies are directed obligations

## ES-ch10.22

For each of duplicate, unknown-prerequisite, and cycle, give a minimal plan that triggers it, the error order raises, and why the cases need different remedies. Why is a missing prerequisite not a cycle?

**Points:** 5

**Rubric (1 point each):**

1. Duplicate: two steps with the same id; rejected with Duplicate step because one key cannot unambiguously represent two steps.
2. Unknown prerequisite: for example verify depends on test but test is absent; rejected with Unknown prerequisite because the plan references nonexistent work.
3. Cycle: two present steps depend on each other, or one depends on itself; neither can become ready, so Dependency cycle is raised.
4. Says a missing prerequisite is not a cycle and the remedies differ.
5. Says duplicates and unknown prerequisites are checked before the ordering loop begins, while the cycle is detected inside it when the graph is nonempty but has no ready step.

**Source:** Dependencies are directed obligations

## ES-ch10.23

Trace order on these steps: z has no prerequisites, b comes after z, a comes after z, and final comes after both a and b. Give the output and describe what each pass of the loop does.

**Points:** 5

**Rubric (1 point each):**

1. Gives the output z, a, b, final.
2. First pass: z is the only ready step; it is appended and removed from the graph and from the remaining prerequisite sets.
3. Second pass: a and b are both ready; they are sorted and appended as a, then b.
4. Third pass: final is ready and is appended, and the graph is empty so the loop ends.
5. Notes that alphabetical order within a batch is a convention and not evidence that alphabetical execution is best; it says only that a and b do not depend on one another.

**Source:** Dependencies are directed obligations

## ES-ch10.24

Consider three steps with ids a, b, and c and no dependencies. What does order return, and what does that not tell you? Give two ways an acyclic graph can still describe work that cannot be done.

**Points:** 5

**Rubric (1 point each):**

1. Says order returns a, b, c in sorted order.
2. Says the function has no knowledge of what each step requires in the world.
3. Says an omitted dependency can make the graph acyclic while the work remains impossible in that order.
4. Says a step can depend on a predecessor whose output is too vague to use; "review after build" is coherent but the reviewer needs a diff, test results, and acceptance criteria.
5. Says an arrow says one step comes after another but does not define the handoff object.

**Source:** Acyclic does not mean executable

## ES-ch10.25

A plan orders inspect, delete, verify without a cycle. Explain why it is a valid ordering yet should not be executed automatically, and say which checks in this chapter cannot catch the problem.

**Points:** 5

**Rubric (1 point each):**

1. Says it is a valid ordering because the graph has no cycle.
2. Says the graph has no operation allowlist and no approval model.
3. Says semantic review must compare each action with scope, authority, and consequence.
4. Says planning before acting does not mean automatically executing any valid graph; the plan creates a review surface that should expose the action early enough for a person or runtime boundary to reject it.
5. Says the structural checks (missing_fields and order) are not responsible for catching it, since neither compares an action with scope or authority.

**Source:** Acyclic does not mean executable

## ES-ch10.26

Implementation needs review, and review needs a completed implementation. Diagnose this cycle, give the resolved sequence, and explain why you should not just remove an edge.

**Points:** 5

**Rubric (1 point each):**

1. Diagnoses that one overloaded word, review, is doing two jobs.
2. Distinguishes plan review, which approves a proposed method, from result review, which evaluates actual output.
3. Gives the resolved sequence plan review, then implementation, then result review.
4. Says not to resolve every cycle by removing an edge because a cycle can reveal that two steps were poorly defined.
5. Says to ask what each step actually needs as input before touching an arrow.

**Source:** Acyclic does not mean executable

## ES-ch10.27

A handoff condition reads "the code was reviewed and looks reasonable." Explain why it fails the chapter's test, give the procedure for repairing it, and give a replacement that passes.

**Points:** 5

**Rubric (1 point each):**

1. States the test: someone who did not build the pipeline can read the condition, observe the system, and decide whether it holds.
2. Says "reviewed" and "reasonable" fail because five reviewers will do five different things and all call it reviewing.
3. Gives the procedure: write the condition, circle every interpretive word, and replace each with a criterion.
4. Says to hand it to someone who did not write it and ask them to apply it to a sample case, going again if they cannot decide.
5. Offers a replacement naming observable items, such as exact commands, exit statuses, output, and a current diff hash or version description, rather than "looks good".

**Source:** Evidence belongs on the edges

## ES-ch10.28

For the symlink plan (one denial test for the Chapter 5 learner permission function, with steps inspect, fixture, test, run, review), write the handoff conditions for the run to review edge and the fixture to test edge.

**Points:** 5

**Rubric (1 point each):**

1. For run to review, requires the exact commands.
2. For run to review, requires exit statuses and output.
3. For run to review, requires a current diff hash or version description, so the reviewer can determine whether the checks correspond to the proposal.
4. For fixture to test, requires resolved paths proving that both locations are disposable.
5. For fixture to test, requires that the destination lies outside the approved subdirectory while remaining inside the temporary parent, so another student can predict what the test exercises.

**Source:** Evidence belongs on the edges

## ES-ch10.29

On the run to review edge, why is Claude's sentence about the test not the evidence? Say who produces the evidence, what an edge needs, and what failure behavior an edge should define.

**Points:** 5

**Rubric (1 point each):**

1. Says the exit status and output come from the test runner.
2. Says an AI describing its own check is the first opinion run twice.
3. Says an edge needs something that fails differently from the thing it certifies, which Chapter 11 builds out.
4. Says that if the targeted test fails, you do not proceed as though review means approval; you return to implementation or stop pending diagnosis.
5. Says that if source authorization is missing, you do not improvise a replacement input.

**Source:** Evidence belongs on the edges

## ES-ch10.30

Name the five Boondoggle sorting questions and use them to decide which edges of the symlink plan need the most evidence. Contrast adding a new test with a command that writes outside the fixture.

**Points:** 5

**Rubric (1 point each):**

1. Names the five questions: how cheap the output is to verify, what being wrong costs, whether this is an ordinary input or a tail case, whether the action can be undone, and whether the step will leave a trail you can review.
2. Says reversibility and the trail do most of the work here.
3. Says a new test in a version-controlled workspace can be reverted from the diff, so its edge needs evidence but not a human gate.
4. Says a command that writes outside the fixture, or deletes, cannot be reverted from a diff, so it gets a hard human approval or falls outside the scope.
5. Says evidence is attached to state-changing edges first, and that a fluent sequence diagram cannot make an unsafe transition acceptable.

**Source:** Evidence belongs on the edges

## ES-ch10.31

In the delegation chapter's two-team scenario, one team documented each handoff and the other wrote "the loan officer reviews." Say what happened to each team and what the scenario does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Says the team whose documentation specified each handoff could be reviewed on substance.
2. Says the team that wrote "the loan officer reviews" was tabled because nobody could say what its pipeline did.
3. Says a clear map can be reviewed.
4. Says a clear map does not show that the decisions inside it are good.
5. Connects the scenario to the source's claim that delegation is a contract, not a partition of labor, whose handoff condition must be testable.

**Source:** Evidence belongs on the edges

## ES-ch10.32

Replace the stop entry "Stop when done" for a bounded task such as revising a document with required sections and source checks. Give the three exits, an example condition for each, and who owns each.

**Points:** 5

**Rubric (1 point each):**

1. Completion names an observable outcome, for a document such as required sections, source checks, and a named decision.
2. Halt names conditions under which action stops before completion, such as out-of-scope files, missing authorization, restricted inputs, a failed independent check, or an unresolved dependency.
3. Defer is what a resource budget such as a time or turn limit produces, and yields an incomplete status.
4. Gives each exit an owner: an automated test can halt on a failing assertion, and a person decides whether a newly discovered risk changes scope.
5. Says "Stop when done" and "when it looks good" are not exits, since the stop field asks who decides, on what evidence, that the work is over or must not continue.

**Source:** Stop conditions and refusal paths

## ES-ch10.33

An agent reaches its turn limit after finishing three of five steps and reports "Done." Evaluate this using the chapter's account of the defer exit.

**Points:** 5

**Rubric (1 point each):**

1. Says a time or turn limit bounds effort without proving success.
2. Says reaching one yields an incomplete status, never a fabricated final result, so "Done" is wrong.
3. Says the report should preserve the partial artifacts.
4. Says the plan should name who decides whether to resume.
5. Distinguishes defer, which a resource budget produces, from halt, which names conditions such as out-of-scope files or missing authorization.

**Source:** Stop conditions and refusal paths

## ES-ch10.34

A teammate lets Claude decide whether a newly discovered risk widens the scope, because Claude summarized the evidence well. Respond using the chapter.

**Points:** 5

**Rubric (1 point each):**

1. Says each exit needs an owner.
2. Says a person must decide whether a newly discovered risk changes scope.
3. Says a summary is not a decision with a name on it.
4. Says Claude can help search approved sources or propose a smaller task but cannot grant permission the user or the institution has not given.
5. Says not every uncertainty is a block, since missing information obtainable within scope differs from a decision that needs new authority.

**Source:** Stop conditions and refusal paths

## ES-ch10.35

Why add refusal paths to a plan? Give three examples from the symlink plan and say what a refusal must report.

**Points:** 5

**Rubric (1 point each):**

1. Says a plan written only for success pressures every observation into forward motion.
2. Defines refusal as the workflow preserving its state and reporting what blocks the next transition.
3. Gives the hard stop: a resolved target outside the disposable parent.
4. Gives the scope stop (a required edit to the course reference instead of the learner copy) and the diagnosis route (a failed existing test goes back to diagnosis, not approval).
5. Says a refusal must report why the step stopped, what evidence was available, and what decision would allow safe resumption, since an unexplained halt looks like a crashed workflow.

**Source:** Stop conditions and refusal paths

## ES-ch10.36

Besides turns and time, the chapter names further resources that bound a plan. Name them, say what the plan should do about each, and say what a deadline can and cannot justify.

**Points:** 5

**Rubric (1 point each):**

1. Names the optional live API call and says it is labeled separately and requires explicit authorization.
2. Says this chapter's offline work needs no live API call.
3. Names human attention as a resource and says a plan that produces hundreds of review items without prioritization is structurally complete and practically unauditable.
4. Says the plan should state what needs human judgment.
5. Says a deadline can justify a reduced objective but does not make skipped verification acceptable without disclosure.

**Source:** Stop conditions and refusal paths

## ES-ch10.37

Explain "a plan predicts, a result records." Say what each of steps, verification, and stop predicts, what habit the chapter asks for, and what goes wrong if the plan is edited after the run.

**Points:** 5

**Rubric (1 point each):**

1. Says steps predict what will be done, verification predicts what you will observe if it worked, and stop predicts which events end the work.
2. Says a result is a record of what happened and the two are different documents to keep apart.
3. Says to write the prediction first and date it.
4. Says to write what a wrong outcome would look like before reading the result and not to revise that note afterward.
5. Says that editing the plan after the run to match it turns it into a description of the result and loses the review that justified acting; the gap between plan and record is what you learn.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.38

Describe two cross-field reviews: objective against verification, and steps against inputs, tools, and scope. Give an example of each failing.

**Points:** 5

**Rubric (1 point each):**

1. Says objective against verification asks whether the check measures the outcome the objective names.
2. Gives an example such as a test confirming a file exists not establishing that its contents implement the behavior, and says that if the check is a proxy you name what it can and cannot reject.
3. Says every step needs information it is authorized to use.
4. Says that if no step writes, a write-capable tool is unnecessary, and that a step needing a capability the tools field lacks makes the plan infeasible.
5. Says an available tool can still be forbidden for this task, because capability does not create authority.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.39

Describe the remaining cross-field reviews: risks against mitigations, owners, and stops; edges against handoff objects; and final scope against revisions.

**Points:** 5

**Rubric (1 point each):**

1. Says risks should state which are accepted, which trigger a mitigation, and which trigger deferral.
2. Says not to assign ownership to a fictitious human or use Claude as the signer of a human decision.
3. Says that for edges you ask what exactly a step such as run produces for review, since a bare id relation gives order without correspondence.
4. Says a late change to the objective can invalidate earlier risk and verification analysis.
5. Says to preserve versions and rerun the relevant review rather than keeping stale supporting fields, because reopening the plan is a normal event with a recorded reason.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.40

Describe four kinds of realistic counterexample and the practice of writing one before approval. Give two examples of constructing a counterexample.

**Points:** 5

**Rubric (1 point each):**

1. Says an objective can be specific but wrong for the stakeholder.
2. Says verification can be executable but test a proxy.
3. Says scope can be precise but authorize too much, and risks can be detailed but disconnected from action.
4. Says a stop condition can be observable but trigger only after harm has occurred.
5. Says to write one counterexample before approval and ask whether the plan rejects it, for example a valid citation that does not support the claim, or an in-scope path with an unapproved operation.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.41

Divide the counterexample work between Claude and you, and explain why to keep the rejected counterexamples. What does a pre-mortem of this kind not prove?

**Points:** 5

**Rubric (1 point each):**

1. Says Claude generates counterexamples quickly and in volume, and that work is worth handing over because it has no stake in the outcome.
2. Says which counterexamples are plausible here, and which risks deserve load-bearing checks, is your call.
3. Says you preserve rejected counterexamples when their dismissal reveals an assumption.
4. Says to keep the original counterexample beside the revised plan, or the final version will look inevitable and hide the failure it was built to stop.
5. Says the pre-mortem does not prove the plan cannot fail; it shows that identified failure modes shaped the design before the system acted.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.42

For the symlink plan's gate, state the objective, what may and may not change, the steps in order, the tools, and two of its risks with their mitigations.

**Points:** 5

**Rubric (1 point each):**

1. States the objective: demonstrate rejection of an outside-pointing symlink in a disposable fixture, without accessing unrelated data.
2. States the scope: may change the learner test file, and the learner implementation only if evidence requires it; may not touch the course reference, real personal files, institutional settings, or publication.
3. Gives the steps in order: inspect, fixture, test, run, review, and the tools: Python, Claude Code for review assistance, the local test runner, and no direct API call.
4. Names at least two risks: targeting a real file, reporting a stable fixture as race resistance, or editing the reference.
5. Names the mitigations: a temporary directory, explicit path inspection, and diff review.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.43

State the symlink plan's stop field (all three exits) and its dated "predicts" line, and say what result would show the plan was wrong.

**Points:** 5

**Rubric (1 point each):**

1. Completion: the fixture demonstrates the rejection, existing tests pass, the diff stays within scope, and the report limits its claim to the stable preflight case.
2. Halt: any command targets material outside the disposable arrangement, or scope must expand without review.
3. Defer, keeping partial artifacts, if a needed source is unavailable.
4. The predicts line is dated before the run: the new test passes, existing tests still pass, and the diff lists only allowed files.
5. A failing existing test or an out-of-scope file in the diff means the plan was wrong and it reopens.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.44

When the symlink plan is encoded and run through missing_fields and order, what comes back, how does that compare with the all-x plan, and what separates the two plans?

**Points:** 5

**Rubric (1 point each):**

1. Says missing_fields returns an empty list, the same as for the all-x plan.
2. Says order returns inspect, fixture, test, run, review.
3. Says the output is the same for different plans and only the review described in the chapter separates them.
4. Says the plan can still be wrong, since the learner code may differ from the reference or the documentation may have changed.
5. Says the improvement over all-x is not longer prose but that another person can predict the actions and challenge the evidence.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.45

State the first three conditions that must hold before a plan goes downstream, and explain why missing_fields alone is not enough.

**Points:** 5

**Rubric (1 point each):**

1. States that the objective was chosen from at least three candidates that pass the distinctness test pairwise.
2. States that the plan names one interest the choice leaves out.
3. States that missing_fields returns an empty list and the cross-field review found no field contradicting another, and that neither alone is enough.
4. States that order returns an order.
5. States that every state-changing edge carries an evidence condition a stranger can apply and a failure route.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.46

State the last three conditions for clearing a plan, explain why the sixth cannot be filled by Claude, and say whether passing the gate freezes the plan.

**Points:** 5

**Rubric (1 point each):**

1. Condition four: the stop field has completion, halt, and defer exits, each with an owner.
2. Condition five: you wrote one counterexample before approval and the plan rejects it, or you revised the plan until it did.
3. Condition six: a named person has approved it, with a date; if nobody has, the status is pending and nothing consequential runs.
4. Says approval is a person's act and a sentence from Claude saying "approved" records nothing.
5. Says the gate does not freeze the plan: it fixes the version Claude implements against, and a result that contradicts the plan reopens it so the revised version goes through the gate again.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.47

Why does the chapter have you implement missing_fields and order before opening the reference? Describe what you do with the six tests and what your version is for.

**Points:** 5

**Rubric (1 point each):**

1. Says you cannot audit an ordering you have never computed.
2. Says you implement both functions in your learner workspace before opening the reference.
3. Says you read the six tests first and predict the results, naming at least four of the cases (empty order, dependency order, self-cycle, unknown prerequisite, duplicate id, empty plan).
4. Says your version is the baseline, the record of what you understood before Claude touched anything.
5. Says it is the instrument you measure Claude's version against.

**Source:** Build It: the baseline that lets you audit the plan

## ES-ch10.48

The chapter asks you to hand the all-x plan's steps value to order and predict the result before running it. Make the prediction from the code and explain what it shows about the two checks.

**Points:** 5

**Rubric (1 point each):**

1. Says the all-x plan's steps value is the single string x, not a list of step dictionaries.
2. Says order iterates over it and reads an id from each item, so it cannot read the value and fails with an error (a TypeError in Python) instead of returning an order.
3. Says the presence check passed the plan while the ordering function may not be able to read it.
4. Says the two checks are each correct under their own rule and neither is responsible for the other's assumptions.
5. Says you predict before you run, and that a structural pass from one check does not mean the plan is ready for the next.

**Source:** Build It: the baseline that lets you audit the plan

## ES-ch10.49

In a plan with steps inspect, build, and verify, the step verify is given after "build" as a bare string instead of the list ["build"]. Predict what order raises, say whether its message points at the real cause, and give the fix.

**Points:** 5

**Rubric (1 point each):**

1. Says set("build") produces a set of single characters, not a set containing the id build.
2. Says none of those characters is a step id, so order raises Unknown prerequisite.
3. Says the message misleads: it suggests a step is missing from the plan although build exists.
4. Says the real cause is that after has the wrong type, a string instead of a list, which order does not check.
5. Gives the fix: pass after as a list, ["build"], and trace the error to unknown dependency rather than saying ordering failed generically.

**Source:** Build It: the baseline that lets you audit the plan

## ES-ch10.50

Describe the three-stage sequence for conducting Claude Code against the plan: what you do before asking Claude, what you do with what comes back, and when Claude may act.

**Points:** 5

**Rubric (1 point each):**

1. Stage one: do the formulation work yourself (three candidates, pairwise results, the selection, and the interest it leaves out) before asking Claude.
2. Gives Claude Code the bounded objective and the exclusions and asks for a plan in the eight fields, saying explicitly that it should change no file yet; what returns is a proposal.
3. Stage two: reviews it as a stranger by running your own missing_fields and order, doing the cross-field review and counterexamples, and checking each of Claude's criticisms yourself.
4. Stage three: only after the gate passes does Claude Code act on the approved version, one step at a time.
5. Holds it to the plan: the stop conditions are what its diff and commands are checked against, and if a halt condition fires the plan stops there and the record says so.

**Source:** Use It: conduct Claude Code against the plan

## ES-ch10.51

Why should you judge a plan by what it commits to rather than how well it is argued? Say what you preserve from the session and what you do if Claude Code is unavailable.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude's account of why it chose a step is a story about the system, not a trace of it (Chapter 1).
2. Says to judge the plan by what it commits to, not by how well it is argued.
3. Says to preserve the prompt, the plan, each revision, the diff, the commands and outputs, the date, and the displayed model label.
4. Says that if Claude Code is unavailable you label the plan as your constructed artifact and record that the session did not run.
5. Says you do not invent Claude Code's output or an approval.

**Source:** Use It: conduct Claude Code against the plan

## ES-ch10.52

List what the reviewed-plan artifact must contain and how it handles versions, validation results, and approval.

**Points:** 5

**Rubric (1 point each):**

1. Says the artifact brief asks for the proposed plan, validation failures, human revisions, stop conditions, and the final approved scope.
2. Says to preserve versions rather than replacing the initial proposal.
3. Says to include the field-validation result and dependency order, but not as semantic approval.
4. Says to add a review table covering items such as objective fit, source and tool boundaries, risk ownership, evidence, handoff conditions, and decision status.
5. Says Claude can draft and critique but the human approval must come from a person, and if approval is pending the plan remains pending.

**Source:** Ship It: the reviewed plan

## ES-ch10.53

Fill in the sign-off for a plan review: name each line of the template, say what goes in it, and explain why the sign-off claims less than a result's sign-off would.

**Points:** 5

**Rubric (1 point each):**

1. Says "Checked" lists the missing_fields and order results, which fields were cross-checked against which, and the counterexamples and whether the plan rejects them.
2. Says "How" says whether by hand, by tests written before reading the reference, or with Claude as critic (saying which of its criticisms you verified yourself).
3. Says "Not checked" names, for example, whether the objective serves anyone beyond your own reading, cases you did not imagine, and anything after the plan runs; this line does the work.
4. Says "Not claiming" names that the plan will succeed, that it is safe beyond the disposable fixture, and that Claude's critique found every flaw, and the last line is signed or withheld.
5. Says the sign-off says only that the plan survived the review described, not that the work succeeded (Chapter 11 writes that), and that withholding is honest when the evidence does not support signing.

**Source:** Ship It: the reviewed plan

## ES-ch10.54

Using the driver's-seat table, say for each of five tasks what Claude should do and what you should do, and explain why one of them stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Framing the problem: Claude adds candidates you missed and finds a result that passes one formulation and fails another; you write candidates first, certify they differ, and select one.
2. Drafting steps, tools, and order: Claude drafts and runs the ordering; you build missing_fields and order yourself first, then revise.
3. Evidence conditions on edges: Claude proposes candidates; you apply the stranger test and mark who can apply each.
4. Counterexamples: Claude generates many, fast; you judge which are plausible here and keep the rejected ones.
5. Approval, wider scope, stopping on a new risk: Claude summarizes the evidence; you decide and record it, because authorization is a person's act and a summary is not a decision.

**Source:** Ship It: the reviewed plan

## ES-ch10.55

The artifact must record one task you delegated and one judgment you retained. What evidence does the chapter suggest pointing to, and what does it say if the transcript shows Claude choosing the objective and you ratifying it?

**Points:** 5

**Rubric (1 point each):**

1. Says to record one task delegated and one judgment retained.
2. Names the formulation you declined, and what it would have served, as possible evidence.
3. Names a counterexample Claude proposed that you rejected, and why, as possible evidence.
4. Names the approval line only you could write as possible evidence.
5. Says that if Claude chose the objective and you ratified it, the split ran the other way and you should say so.

**Source:** Ship It: the reviewed plan

## ES-ch10.56

List what you run and review in the Verify step, say what parallel readiness does and does not mean, and describe the reflection the chapter asks for.

**Points:** 5

**Rubric (1 point each):**

1. Says to run the demo, the lesson tests, the all-x counterexample, and your graph cases, naming which claim each check addresses.
2. Says to trace each error to duplicate, unknown dependency, or cycle rather than saying ordering failed generically.
3. Says to review every field for meaning, authority, and evidence, and preserve at least one unsafe or useless plan that still passes the structural checks.
4. Says parallel readiness means no declared dependency, not proof that concurrent execution is safe, and to check whether the graph omits real dependencies or invents unnecessary ones.
5. Says to compare initial and revised objectives, name the decision that changed and what moved it, and name which distinction you had collapsed (presence and meaning, order and executability, valid and authorized).

**Source:** Verify and reflect

## ES-ch10.57

Summarize what you can defend after this chapter: the boundary of the presence check, the standing of a plan, and how the three jobs of conduct, check, and drive show up in the work.

**Points:** 5

**Rubric (1 point each):**

1. Says every plan remains a proposal until its responsible review and authorization are actually recorded.
2. Says an empty missing list does not certify plan quality, and that you can trace topological ordering and tell duplicates, unknown prerequisites, and cycles apart.
3. Conducted: chose the problem from candidates that disagreed about success, wrote the plan and its gate before Claude changed anything, and put evidence on the edges and owners on the exits.
4. Checked: treated the plan as a prediction, wrote a counterexample before approval, and refused to let a structural pass stand in for a meaningful plan.
5. Drove: let Claude draft and attack, kept the objective, the values inside it, and the approval, and signed or withheld; and a flawless graph can execute the wrong problem.

**Source:** What you can now defend

## ES-ch10.58

What comparison does the Anthropics section ask for, what question should you answer, and what must you not claim about the eight fields?

**Points:** 5

**Rubric (1 point each):**

1. Says to compare the dependency graph with Building effective agents.
2. Says to compare the bounded workflow with Claude Code best practices.
3. Says to explain whether the task needs a fixed sequence or model-directed choices.
4. Notes that the links were checked 2026-09-06.
5. Says the eight fields remain this course's own review instrument and are not attributed to Anthropic.

**Source:** Anthropics

## ES-ch10.59

The Computational Skepticism section refines the testability standard used in the body. State the refinement, what you must do with each edge condition, and what it says about an acyclic graph.

**Points:** 5

**Rubric (1 point each):**

1. Says testability is graded.
2. Says some conditions any non-author can apply, while others only a qualified reviewer can, such as whether a cited clause really governs the change.
3. Says to mark each edge condition in your plan with its tier and say so in the artifact.
4. Says a condition only its author can apply has not yet become a handoff condition.
5. Says an acyclic graph orders work but does not make the handoff trustworthy.

**Source:** Computational Skepticism

## ES-ch10.60

Name the three moves the Conducting AI section offers for producing candidate formulations that really differ, say how much weight the chapter puts on them, and describe the appendix's companion check on constraints.

**Points:** 5

**Rubric (1 point each):**

1. Names zooming out until the original metric becomes a symptom.
2. Names zooming in on a load-bearing sub-case.
3. Names changing the actor by asking whose constraint actually binds, applied here as whether the binding constraint is the test, the function, or the caller's expectation.
4. Says the moves are the book's own scaffolds, not cited research, so every output gets the distinctness test.
5. Describes the companion check: mark every constraint in the scope field as real or assumed and test one you suspect is assumed; if none ever turns out to be, you are not looking.

**Source:** Conducting AI
