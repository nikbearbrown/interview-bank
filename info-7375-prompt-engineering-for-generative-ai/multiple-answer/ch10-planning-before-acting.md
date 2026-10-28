# Chapter 10: Planning before acting

## MA-ch10.1

Check each statement that is true about the plan whose eight fields all hold the single string x. Each statement is worth 1 point (5 points total).

- [ ] A. The plan is useless even though every required heading is present.
- [ ] B. The all-x object is constructed by the research script itself and is not offered as a rhetorical exaggeration.
- [ ] C. The research run that built the all-x plan also orders three steps as inspect, build, verify and rejects a dependency cycle.
- [ ] D. missing_fields reports all eight fields as missing because x is not a meaningful value.
- [ ] E. The research script passes that plan to missing_fields and the returned list is empty.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The form is complete and the content is empty.
- B: The chapter says it is not a rhetorical exaggeration.
- C: Both results are preserved in the research output.
- D: The function checks presence, not meaning.
- E: Every value is a nonempty string, so no field is missing.

**Source:** Chapter 10: Planning before acting (opening)

## MA-ch10.2

Check each statement that is true about what field checks are for, according to the opening of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Field checks catch absence and false-valued entries under a declared list.
- [ ] B. Field checks can tell whether a stop condition can actually be observed.
- [ ] C. Field checks judge whether a verification step tests the claim.
- [ ] D. A structural check earns its place by reliably rejecting structural omissions.
- [ ] E. The all-x counterexample shows that field checks are pointless.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: That is their narrow job.
- B: Observability is a semantic judgment.
- C: They cannot judge meaning.
- D: Its value is reliability on structure.
- E: The chapter says it does not make them pointless; it tells us their job.

**Source:** Chapter 10: Planning before acting (opening)

## MA-ch10.3

Check each statement that is true about how the chapter describes Conduct, Check, and Drive in a plan. Each statement is worth 1 point (5 points total).

- [ ] A. Drive: Claude can suggest framings and attack your selection, and you defend it.
- [ ] B. Check: a complete form counts as a plan, and an acyclic graph counts as an executable one.
- [ ] C. Conduct: the plan is the design that precedes implementation, and the reviewed plan is the gate.
- [ ] D. Check: you review the plan with counterexamples only after the work has run, once there are results to compare.
- [ ] E. Drive: Claude chooses the problem and the values inside it, and you ratify its choice.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Claude critiques; you decide.
- B: The chapter says neither is enough.
- C: Nothing changes until a condition you can state is met.
- D: Review with counterexamples comes before anything runs.
- E: The problem and the values are yours.

**Source:** Chapter 10: Planning before acting (opening)

## MA-ch10.4

Check each statement that is true about how the chapter sets up the build and the role of Claude Code. Each statement is worth 1 point (5 points total).

- [ ] A. The Python build runs offline and needs no direct API credits.
- [ ] B. If the interface is unavailable, preserve that fact and complete the offline construction.
- [ ] C. A plan returned by Claude Code counts as approved once it passes the field check.
- [ ] D. Chapter 9 asked whether the proposed sequence is justified and bounded; this chapter asks what object will change.
- [ ] E. If the interface is unavailable, write the plan yourself and present it as Claude-authored so the artifact looks finished.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The offline construction is the baseline.
- B: That is the stated instruction.
- C: The returned plan remains a proposal.
- D: The two are the other way around: Chapter 9 asked what object will change.
- E: Do not invent a Claude-authored plan or human approval.

**Source:** Chapter 10: Planning before acting (opening)

## MA-ch10.5

Check each statement that the chapter lists among the abilities you should have after working through it. Each statement is worth 1 point (5 points total).

- [ ] A. Identify all eight required plan fields.
- [ ] B. Explain duplicate, unknown-prerequisite, and cycle rejections.
- [ ] C. Choose an objective from candidates that genuinely agree about what success means.
- [ ] D. Write a handoff condition that only its author can apply.
- [ ] E. Say which parts of planning you handed to Claude and which you kept: the problem, the values inside it, the approval.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: It is the first listed ability.
- B: It is a listed ability.
- C: The candidates must genuinely disagree about success.
- D: The condition must be one another person can apply.
- E: This is the Drive ability.

**Source:** What you will be able to do

## MA-ch10.6

Check each statement that is true about what a plan is in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A plan is worth the most after the work has run, when its content can be confirmed.
- [ ] B. The plan is a record of Claude's private deliberation.
- [ ] C. A plan should expose the destination, allowed inputs and scope, intended steps, tools, risks, evidence, and stopping rule while change is still cheap.
- [ ] D. Planning exists to make proposed work inspectable before action.
- [ ] E. The plan is a public action contract another person can critique.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It is worth the most before anything has run.
- B: It is not hidden reasoning and need not reproduce private deliberation.
- C: That is the list the chapter gives.
- D: That is its purpose.
- E: The chapter states this directly.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.7

Check each statement that is true about the phase gate and design by contract as the chapter describes them. Each statement is worth 1 point (5 points total).

- [ ] A. In design by contract, the agent writes the contract and you write the implementation.
- [ ] B. In this chapter's sense, a plan is that contract for a single function.
- [ ] C. In design by contract, assertions or tests derived from your contract check the agent's implementation.
- [ ] D. A phase gate needs no testable condition as long as the specification of each side's work is clear.
- [ ] E. A phase gate is the explicit point where Claude's work stops and a person's begins.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: You write the contract; the agent writes the implementation.
- B: It is the contract for a whole piece of work.
- C: That is how the contract is enforced.
- D: The gate includes a testable condition that must hold before output moves downstream.
- E: That is the definition.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.8

Check each statement that is true about the Boondoggle Score as the chapter treats it. Each statement is worth 1 point (5 points total).

- [ ] A. It places a testable handoff condition between each Claude task and each human task.
- [ ] B. It lays out the prompts for Claude in dependency order.
- [ ] C. It lists the human's actions in the same dependency order.
- [ ] D. The chapter treats it as an externally validated diagnostic.
- [ ] E. The five sorting questions attached to it have no external validation behind them that the author knows of.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is its third part.
- B: That is one of its parts.
- C: That is its second part.
- D: It says to treat it as a heuristic, not a diagnostic.
- E: The chapter says so.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.9

Check each statement that is true about revising a plan. Each statement is worth 1 point (5 points total).

- [ ] A. "Design first" means that once reviewed, the plan must not change.
- [ ] B. In the discount-rule example, auditing the diff shows rounding was never specified, which reopens the requirement.
- [ ] C. The chapter's claim is that you should plan everything first.
- [ ] D. A plan is a controlled state with versions.
- [ ] E. When a result contradicts an assumption, you keep the plan unchanged and note the surprise in the result.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Design first is not design frozen.
- B: The instruction is to log it and go back.
- C: The claim is narrower: the first version should exist and be reviewed before Claude changes anything.
- D: The chapter says so.
- E: You revise the plan and record the reason.

**Source:** The plan is the design, and the review is the gate

## MA-ch10.10

Check each statement that is true about choosing the problem before planning. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter credits the phrase "error of the third kind" to Allyn Kimball, 1957.
- [ ] B. A perfectly ordered plan can optimize the wrong objective.
- [ ] C. The error of the third kind is a wrong answer to the right problem.
- [ ] D. The cost of the wrong objective is highest when Claude executes it clumsily, because errors then show.
- [ ] E. A polished, internally checked answer to the wrong question carries authority the question never earned.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: It cites that attribution.
- B: Order does not fix a wrong choice of problem.
- C: It is a right answer to the wrong problem.
- D: The cost is highest when Claude executes it fluently.
- E: That is why fluency raises the cost.

**Source:** Formulate before you plan

## MA-ch10.11

Check each statement that is true about asking Claude to frame the problem first. Each statement is worth 1 point (5 points total).

- [ ] A. If you have not named your anchor before Claude supplies its own, its anchor becomes yours by default.
- [ ] B. The chapter presents the claim that a text-continuing system tends toward the modal framing as a theorem on which the practice depends.
- [ ] C. The book argues that a system trained to continue text tends toward the common and likely, so its framing is the modal one.
- [ ] D. Auditing Claude's framing afterward is safe because the audit stays independent of that framing.
- [ ] E. Jane Darke's primary generator is a first, usually tacit idea of what the problem is really about.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: It arrives dressed as neutral analysis.
- B: It says the practice survives without it.
- C: The chapter presents this as an argument about tendencies.
- D: The audit comes too late because you check against the framing the output already assumes.
- E: It decides which solutions you can see.

**Source:** Formulate before you plan

## MA-ch10.12

Check each statement that is true about candidate formulations and the distinctness test. Each statement is worth 1 point (5 points total).

- [ ] A. A model's statement that two formulations are distinct replaces the test.
- [ ] B. Candidates should differ in what counts as success, not in wording.
- [ ] C. Two formulations are distinct if they would require different solutions even to test.
- [ ] D. If one solution satisfies both formulations, they are one formulation in two outfits.
- [ ] E. Constructing results that one formulation accepts and another rejects is how you test whether the formulations differ.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: You certify distinctness in your context by constructing results.
- B: The chapter says so.
- C: That is the test.
- D: They are the same problem.
- E: The chapter tests candidates by constructing results.

**Source:** Formulate before you plan

## MA-ch10.13

In the plus-one regression a function should return its input plus one but returns the input minus one. Formulation A is that the single failing test, input two, goes green. B is that the declared plus-one behavior is restored without changing anything outside the learner module and its test. C is that the learner can explain the bug. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A patch that returns the constant 3, applied without diagnosing the cause, passes formulation B.
- [ ] B. A patch that returns the constant 3 passes formulation A.
- [ ] C. A correct x + 1 patch accepted unread passes formulation A but fails formulation B.
- [ ] D. For input five the declared plus-one behavior requires 6, while a patch that always returns 3 gives 3.
- [ ] E. A correct x + 1 patch that Claude wrote and you accepted unread passes formulation C.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: For input five it returns 3, not 6.
- B: For input two the declared answer is 3.
- C: It passes B; it fails C.
- D: Five plus one is six.
- E: The learner cannot explain it, so C fails.

**Source:** Formulate before you plan

## MA-ch10.14

Check each statement that is true about choosing among formulations. Each statement is worth 1 point (5 points total).

- [ ] A. The most tractable framing is the one that best serves the people affected.
- [ ] B. If every criterion is about cost, time, and buildability, you have built a machine that selects the most tractable framing.
- [ ] C. It is acceptable to write the constraint set after seeing how each candidate scores, as long as it is documented.
- [ ] D. The constraint set should be written before you score anything.
- [ ] E. The book adds salience and whose interests the framing centers and decenters to the criteria.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It is the framing Claude would have picked unasked.
- B: Feasibility-only criteria favor tractability.
- C: It must be written before you score anything.
- D: Writing it first stops criteria being fitted to a favorite.
- E: These go beyond feasibility.

**Source:** Formulate before you plan

## MA-ch10.15

Check each statement that is true about the values decision in the plus-one example. Each statement is worth 1 point (5 points total).

- [ ] A. The values decision comes after the formulation, once the objective is fixed.
- [ ] B. One of the three formulations centers everyone, so choosing it leaves no one out.
- [ ] C. Formulation B centers the maintainers and callers of the function.
- [ ] D. Formulation C centers the maintainers and callers of the function.
- [ ] E. Formulation A centers whoever reads the test report.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It sits inside the formulation, not after it.
- B: None centers everyone.
- C: The chapter states this.
- D: C centers the learner; B centers maintainers and callers.
- E: The chapter states this.

**Source:** Formulate before you plan

## MA-ch10.16

Check each statement that is true about dividing the formulation work between you and Claude. Each statement is worth 1 point (5 points total).

- [ ] A. You should write your candidates first, then let Claude extend and criticize them.
- [ ] B. Claude should write the candidates first so that you can react to them.
- [ ] C. Someone answers for centering the maintainer over the learner, and Claude has no name to put there.
- [ ] D. Claude can make the values selection, because weighing interests is something it does quickly.
- [ ] E. Claude can find a result that passes one formulation and fails another.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: This keeps its anchor from becoming yours.
- B: Its anchor would become yours by default.
- C: That is why the selection stays with you.
- D: The selection needs situated judgment and a name on the decision.
- E: This is a real contribution.

**Source:** Formulate before you plan

## MA-ch10.17

Check each statement that is true about the FIELDS tuple. Each statement is worth 1 point (5 points total).

- [ ] A. Its names are objective, inputs, scope, steps, tools, risks, verification, and stop.
- [ ] B. One of its names is approval.
- [ ] C. It declares eight names.
- [ ] D. The code can only see whether each name is bound to a value; a reviewer asks the question each name stands for.
- [ ] E. One of its names is owner.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is the list in the reference.
- B: Approval is a gate condition, not one of the eight fields.
- C: They run from objective to stop.
- D: That is the split between code and reviewer.
- E: There is no such field.

**Source:** The eight fields are eight questions

## MA-ch10.18

Check each statement that is true about the question each field asks. Each statement is worth 1 point (5 points total).

- [ ] A. Inputs asks what outcome is stated so that someone can tell whether it happened.
- [ ] B. Scope asks what may change and what must stay untouched.
- [ ] C. Verification asks what observation will support the completion claim.
- [ ] D. Risks asks only whether any risk exists.
- [ ] E. Tools asks only which tool is used, so the entry "Claude Code" fills it well.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: That is the objective question.
- B: It is the scope question in the table.
- C: It is the verification question in the table.
- D: It asks how the work could cause harm, error, or misleading evidence, and what each risk triggers.
- E: That entry fills the field and does nothing; the field asks which capability, why, and which operation stays under human approval.

**Source:** The eight fields are eight questions

## MA-ch10.19

Check each statement that is true about the entries the chapter lists for the eight fields. Each statement is worth 1 point (5 points total).

- [ ] A. The entry "Be careful" fills the scope field and does nothing.
- [ ] B. The entry "Stop after all scoped tests pass and the named reviewer accepts the current diff" fills the stop field and does nothing.
- [ ] C. The entry "An exact command, an expected invariant, or a source comparison" fills the verification field and does nothing.
- [ ] D. The entry "Stop when done" fills the stop field and does nothing.
- [ ] E. The entry "Improve the code" fills the objective field and does nothing.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: It names no paths, operations, or exclusions.
- B: That is the entry a reviewer can challenge.
- C: That is the entry a reviewer can challenge.
- D: It names no observable exit.
- E: It cannot be challenged.

**Source:** The eight fields are eight questions

## MA-ch10.20

Check each statement that is true about how missing_fields decides that a field is missing. Each statement is worth 1 point (5 points total).

- [ ] A. A value of False counts as missing.
- [ ] B. The integer 0 counts as present because it is a real value.
- [ ] C. An empty string counts as missing.
- [ ] D. A field set to None counts as present because the key exists.
- [ ] E. It uses plan.get, so a field name that is absent from the plan counts as missing.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: False is false-valued.
- B: Zero is false-valued, so it counts as missing.
- C: An empty string is false-valued.
- D: None fails the truth-value check.
- E: plan.get returns None for an absent name.

**Source:** What missing_fields actually checks

## MA-ch10.21

Check each statement that is true about what missing_fields does and does not do. Each statement is worth 1 point (5 points total).

- [ ] A. It explains why an inadequate value is inadequate.
- [ ] B. It requires each field to hold a particular type, such as a list for steps.
- [ ] C. It rejects plans that contain extra keys.
- [ ] D. A nonempty list, string, dictionary, or even an unrelated truthy value can pass.
- [ ] E. Its output is a dictionary that maps each missing field to a reason.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It does not.
- B: It requires no particular type for any field.
- C: It does not reject extra keys.
- D: Only truthiness matters.
- E: Its output is an ordered list of names with no reasons.

**Source:** What missing_fields actually checks

## MA-ch10.22

Check each statement that is true about the value and limits of the presence check. Each statement is worth 1 point (5 points total).

- [ ] A. The check is deterministic and cheap.
- [ ] B. A richer validator could catch more structural defects but still could not decide whether the command tests the right claim.
- [ ] C. Because it is blind to meaning, it should be dropped in favor of human review alone.
- [ ] D. The right use is to clear the easy failures so that human attention goes to the hard ones.
- [ ] E. It fails differently from a reviewer: it never gets tired and never notices meaning.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The chapter says so.
- B: It cannot decide whether the objective serves the right person either.
- C: The chapter says to use it to clear the easy failures.
- D: That is the stated use.
- E: Its failure mode complements a reviewer's.

**Source:** What missing_fields actually checks

## MA-ch10.23

Check each statement that is true about steps as a graph of directed obligations. Each statement is worth 1 point (5 points total).

- [ ] A. The ordering function decides which arrows exist.
- [ ] B. If step verify has after: [build], then build must appear before verify.
- [ ] C. Verify may be called ready as soon as build has been scheduled.
- [ ] D. Steps are best treated as a flat list.
- [ ] E. The ordering function can only order the arrows you declared.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: You decide which arrows exist.
- B: That is the directed obligation.
- C: It is ready only when build has produced what verify needs.
- D: The chapter says steps are not a list; they are a graph.
- E: It has no other knowledge.

**Source:** Dependencies are directed obligations

## MA-ch10.24

Check each statement that is true about the order function's validation errors. Each statement is worth 1 point (5 points total).

- [ ] A. A missing prerequisite and a mutual dependency between two present steps have the same remedy.
- [ ] B. A missing prerequisite is just a cycle reported with a different message.
- [ ] C. A dependency naming an id that is absent from the graph raises Unknown prerequisite.
- [ ] D. If verify depends on test but test is absent, the plan references nonexistent work.
- [ ] E. Duplicate ids are rejected because one key could not unambiguously represent two steps.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The remedies differ.
- B: A missing prerequisite is not a cycle.
- C: The code checks this before ordering.
- D: The chapter gives this example.
- E: The graph is keyed by step id.

**Source:** Dependencies are directed obligations

## MA-ch10.25

Check each statement that is true about the ordering loop in order. Each statement is worth 1 point (5 points total).

- [ ] A. The function runs the steps and establishes that their descriptions are useful.
- [ ] B. Ready ids stay in the graph so that later steps can still see them.
- [ ] C. If the graph is nonempty but has no ready step, the function raises Dependency cycle.
- [ ] D. Each pass finds all steps whose prerequisite sets are empty; these are the ready steps.
- [ ] E. The ready ids are returned in the order they were inserted into the graph.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: It does neither.
- B: They are removed and deleted from the remaining prerequisite sets.
- C: The remaining dependencies contain a cycle.
- D: That is how readiness is defined.
- E: They are sorted for deterministic output.

**Source:** Dependencies are directed obligations

## MA-ch10.26

Check each statement that is true about the research example and ties within a batch. Each statement is worth 1 point (5 points total).

- [ ] A. A self-dependency is the smallest example of a cycle and appears in the tests.
- [ ] B. Alphabetical order is evidence that alphabetical execution is best.
- [ ] C. When several steps are ready at once, alphabetical id order decides which appears first within that batch.
- [ ] D. The alphabetical tie-break says only that, under the supplied relations, those steps do not depend on one another.
- [ ] E. In the research example inspect has no prerequisites, build comes after inspect, and verify comes after build, giving the order inspect, build, verify.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The step can never become ready.
- B: It is not evidence of that.
- C: It is a convention for determinism.
- D: It carries no further claim.
- E: The chapter states this.

**Source:** Dependencies are directed obligations

## MA-ch10.27

Check each statement that is true about what an acyclic graph does and does not show. Each statement is worth 1 point (5 points total).

- [ ] A. Three steps a, b, and c with no dependencies make the function raise an error because nothing orders them.
- [ ] B. The graph also confirms that the declared prerequisites are the real ones.
- [ ] C. An omitted dependency can make the graph acyclic while the work remains impossible in that order.
- [ ] D. An arrow defines the handoff object passed from one step to the next.
- [ ] E. The graph answers whether there is an order in which every declared prerequisite comes first.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It returns them in sorted order.
- B: It is silent on that.
- C: The graph cannot see what a step needs in the world.
- D: It says one step comes after another; it does not define the handoff object.
- E: That is its one question.

**Source:** Acyclic does not mean executable

## MA-ch10.28

Check each statement that is true about a plan that is acyclic but unsafe. Each statement is worth 1 point (5 points total).

- [ ] A. A cycle check cannot reject the delete step as unsafe.
- [ ] B. Inspect, delete, verify is a valid ordering if represented without a cycle.
- [ ] C. Planning before acting means automatically executing any valid graph.
- [ ] D. Semantic review must compare each action with scope, authority, and consequence.
- [ ] E. The graph has no operation allowlist and no approval model.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A cycle check only looks at declared prerequisites.
- B: Graph validity is structural.
- C: It does not.
- D: That is the review the graph cannot do.
- E: It cannot compare actions with authority.

**Source:** Acyclic does not mean executable

## MA-ch10.29

Check each statement that is true about cycles and how to resolve them. Each statement is worth 1 point (5 points total).

- [ ] A. Removing the inconvenient edge is the recommended way to resolve a cycle.
- [ ] B. A cycle can reveal that two steps were poorly defined.
- [ ] C. Plan review approves a proposed method, and result review evaluates actual output.
- [ ] D. If implementation needs review and review needs a completed implementation, one overloaded word is doing two jobs.
- [ ] E. Renaming the obligations gives the sequence result review, implementation, plan review.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The chapter says not to resolve every cycle by removing an edge.
- B: Removing an edge may hide that.
- C: They are different obligations.
- D: The word review covers two obligations.
- E: It gives plan review, then implementation, then result review.

**Source:** Acyclic does not mean executable

## MA-ch10.30

Check each statement that is true about testable handoff conditions. Each statement is worth 1 point (5 points total).

- [ ] A. "Reviewed" and "reasonable" are testable because reviewers know what they mean.
- [ ] B. Five reviewers given the condition "reviewed" will converge on the same checks because the word is familiar.
- [ ] C. Computational Skepticism's chapter on delegation claims that delegation is a contract, not a partition of labor.
- [ ] D. "Looks good" is a handoff condition.
- [ ] E. Testable means someone who did not build the pipeline can read the condition, observe the system, and decide whether it holds.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Five reviewers will do five different things and all call it reviewing.
- B: They will do five different things.
- C: The handoff condition is its load-bearing clause.
- D: The chapter says it is not.
- E: That is the standard.

**Source:** Evidence belongs on the edges

## MA-ch10.31

Check each statement that is true about the symlink plan and its edges. Each statement is worth 1 point (5 points total).

- [ ] A. For the run to review edge, the handoff can require the exact commands, exit statuses, output, and a current diff hash or version description.
- [ ] B. Its steps run inspect, test, fixture, run, review.
- [ ] C. For the fixture to test edge, the handoff can require resolved paths proving both locations are disposable and the destination lies outside the approved subdirectory while remaining inside the temporary parent.
- [ ] D. The symlink plan adds one denial test to the Chapter 5 learner permission function.
- [ ] E. The plan permits editing the course reference.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The reviewer can then check the checks against the proposal.
- B: The order is inspect, fixture, test, run, review.
- C: This lets another student predict what the test exercises.
- D: That is the running hypothetical.
- E: The course reference is something it may not touch.

**Source:** Evidence belongs on the edges

## MA-ch10.32

Check each statement that is true about who produces the evidence on an edge. Each statement is worth 1 point (5 points total).

- [ ] A. An AI describing its own check is the first opinion run twice.
- [ ] B. Claude's sentence describing its own check counts as the evidence for the edge.
- [ ] C. On the run to review edge, the exit status and output come from the test runner.
- [ ] D. A test runner's output is weaker evidence than Claude's summary of it because the runner cannot explain itself.
- [ ] E. An edge needs evidence that fails the same way as the thing it certifies.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: It adds no independence.
- B: It is not that evidence.
- C: The runner, not Claude, produces them.
- D: The runner fails differently from the model, which is what the edge needs.
- E: It needs evidence that fails differently.

**Source:** Evidence belongs on the edges

## MA-ch10.33

Check each statement that is true about the five Boondoggle sorting questions. Each statement is worth 1 point (5 points total).

- [ ] A. How fluent the sequence diagram looks is one of the five sorting questions.
- [ ] B. How cheap the output is to verify is one of the five sorting questions.
- [ ] C. Whether the step will leave a trail you can review is one of the five sorting questions.
- [ ] D. Whether the action can be undone is one of the five sorting questions.
- [ ] E. Whether the input is ordinary or a tail case is one of the five sorting questions.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A fluent diagram cannot make an unsafe transition acceptable.
- B: The chapter lists verification cost among the five.
- C: The trail is one of the two that do most of the work here.
- D: Reversibility is one of the two that do most of the work here.
- E: The chapter lists it among the five.

**Source:** Evidence belongs on the edges

## MA-ch10.34

Check each statement that is true about which edges need the most evidence. Each statement is worth 1 point (5 points total).

- [ ] A. If the learner workspace is under version control, a new test can be reverted from the diff, so its edge needs evidence but not a human gate.
- [ ] B. A command that writes outside the fixture can be reverted from the diff like a new test.
- [ ] C. A command that writes outside the fixture, or deletes, gets a hard human approval or falls outside the scope.
- [ ] D. Evidence should be attached to read-only edges first.
- [ ] E. The cheapness of verification and the fluency of the diagram do most of the work in deciding which edges need the most evidence.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The change is reversible.
- B: It cannot be reverted from a diff.
- C: It cannot be undone.
- D: State-changing edges come first.
- E: Reversibility and the trail do most of the work here.

**Source:** Evidence belongs on the edges

## MA-ch10.35

Check each statement that is true about the two-team scenario from the delegation chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A clear map shows that the decisions inside it are good.
- [ ] B. The team whose documentation specified each handoff could be reviewed on substance.
- [ ] C. The team with documented handoffs was approved automatically.
- [ ] D. The team that wrote "the loan officer reviews" was tabled because nobody could say what its pipeline did.
- [ ] E. A clear map can be reviewed.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The chapter says it does not.
- B: The map was reviewable.
- C: The chapter says only that it could be reviewed on substance.
- D: The handoff was not specified.
- E: That is what the scenario shows.

**Source:** Evidence belongs on the edges

## MA-ch10.36

Check each statement that is true about the three exits of a stop field. Each statement is worth 1 point (5 points total).

- [ ] A. Halt names the conditions under which the work is finished.
- [ ] B. "When it looks good" is an acceptable completion exit.
- [ ] C. A turn budget and a finish action answer the same question as the stop field.
- [ ] D. Completion names the observable task outcome.
- [ ] E. The stop field asks who decides, on what evidence, that the work is over or must not continue.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Halt names conditions under which action stops before completion.
- B: The chapter says it is not an exit.
- C: They answer different questions; the stop field answers a third.
- D: For code, that includes a targeted regression, existing tests, and a reviewed diff.
- E: That is the third question.

**Source:** Stop conditions and refusal paths

## MA-ch10.37

Check each statement that is true about the defer exit. Each statement is worth 1 point (5 points total).

- [ ] A. Partial artifacts should be discarded when a time or turn limit is reached so that the record stays clean.
- [ ] B. Reaching a time or turn limit yields an incomplete status, never a fabricated final result.
- [ ] C. The defer exit should name the partial artifacts to preserve and who decides whether to resume.
- [ ] D. Reaching a turn limit is evidence that the task is complete.
- [ ] E. A time or turn limit bounds effort without proving success.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: They are preserved.
- B: The status must be honest.
- C: Both are required.
- D: It is not evidence of success.
- E: Reaching a limit says nothing about whether the task succeeded.

**Source:** Stop conditions and refusal paths

## MA-ch10.38

Check each statement that is true about who owns each exit. Each statement is worth 1 point (5 points total).

- [ ] A. An automated test can decide whether a newly discovered risk changes scope.
- [ ] B. A summary is a decision with a name on it.
- [ ] C. Each exit needs an owner.
- [ ] D. A person must decide whether a newly discovered risk changes scope.
- [ ] E. A human decision can be handed to Claude because it can summarize the evidence well.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: A person must decide that.
- B: A summary is not a decision with a name on it.
- C: Every exit must name who decides.
- D: That decision cannot be automated.
- E: The chapter says not to hand it over.

**Source:** Stop conditions and refusal paths

## MA-ch10.39

Check each statement that is true about refusal paths. Each statement is worth 1 point (5 points total).

- [ ] A. In the symlink plan, a required edit to the course reference instead of the learner copy is a scope stop.
- [ ] B. A plan written only for success pressures every observation into forward motion.
- [ ] C. In the symlink plan, a resolved target outside the disposable parent is a reason to continue cautiously.
- [ ] D. In the symlink plan, a failed existing test routes back to diagnosis.
- [ ] E. Refusal means the workflow preserves its state and reports what blocks the next transition.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The reference is out of scope.
- B: That is why refusal paths are added.
- C: It is a hard stop.
- D: It does not route to approval.
- E: That is the chapter's meaning of refusal.

**Source:** Stop conditions and refusal paths

## MA-ch10.40

Check each statement that is true about refusal outputs and uncertainty. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can grant permission that the user or the institution has not given.
- [ ] B. A refusal needs outputs: why the step stopped, what evidence was available, and what decision would allow safe resumption.
- [ ] C. If the same check fails again with no new evidence, the next step is an identical retry.
- [ ] D. An unexplained halt is easy to tell from a crashed workflow.
- [ ] E. Every uncertainty is a block.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: It can help search approved sources or propose a smaller task, but it cannot grant permission.
- B: The chapter lists these three.
- C: The next step is diagnosis, revising the plan, or deferring.
- D: It is hard to tell apart, which is why outputs are needed.
- E: Missing information obtainable within scope differs from a decision that needs new authority.

**Source:** Stop conditions and refusal paths

## MA-ch10.41

Check each statement that is true about a plan as a prediction and a result as a record. Each statement is worth 1 point (5 points total).

- [ ] A. The steps predict what will be done, the verification field predicts what you will observe if it worked, and the stop field predicts which events end the work.
- [ ] B. If the plan is edited after the run to match the run, it has become a description of the result.
- [ ] C. The plan and the result are best kept as one document that you keep up to date.
- [ ] D. A result is a record of what happened.
- [ ] E. You should write what a wrong outcome would look like after you read the result.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Each is a prediction.
- B: The review that justified acting is gone.
- C: The habit worth building is keeping them apart.
- D: It is a different document from the plan.
- E: You write it before and do not revise it afterward.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.42

Check each statement that is true about reviewing the plan against itself. Each statement is worth 1 point (5 points total).

- [ ] A. If no step writes, a write-capable tool is unnecessary.
- [ ] B. Objective against verification asks whether the check measures the outcome the objective names.
- [ ] C. An available tool is automatically permitted for the task because the environment makes it available.
- [ ] D. If a step needs a capability the tools field lacks, the plan is feasible but incomplete.
- [ ] E. A test that confirms a file exists establishes that its contents implement the behavior.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Steps are reviewed against tools.
- B: That is the first cross-field review.
- C: Capability does not create authority.
- D: The plan is infeasible.
- E: It does not.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.43

Check each statement that is true about the remaining cross-field reviews. Each statement is worth 1 point (5 points total).

- [ ] A. The risks review states which risks are accepted, which trigger a mitigation, and which trigger deferral.
- [ ] B. A bare id relation between two steps gives order without correspondence.
- [ ] C. Ownership of a risk should not be assigned to a fictitious human.
- [ ] D. Claude can serve as the signer of a human decision.
- [ ] E. A late change to the objective can invalidate earlier risk and verification analysis.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Each risk needs a stated consequence.
- B: The handoff object must be defined.
- C: The chapter says not to.
- D: Claude should not be used as the signer.
- E: Versions are preserved and the review rerun.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.44

Check each statement that is true about the counterexamples the chapter describes. Each statement is worth 1 point (5 points total).

- [ ] A. An objective can be specific but wrong for the stakeholder.
- [ ] B. Scope can be precise but authorize too much.
- [ ] C. A stop condition can be observable but trigger only after harm has occurred.
- [ ] D. A realistic counterexample is incoherent or empty, like the all-x plan.
- [ ] E. Verification can be executable but test a proxy.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is a realistic counterexample.
- B: That is a realistic counterexample.
- C: That is a realistic counterexample.
- D: Realistic counterexamples resemble plans people accept.
- E: That is a realistic counterexample.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.45

Check each statement that is true about writing counterexamples before approval. Each statement is worth 1 point (5 points total).

- [ ] A. A pre-mortem with executable consequences proves the plan cannot fail.
- [ ] B. When prerequisites are technically complete but the receiving step lacks a needed artifact, add another arrow.
- [ ] C. For safe writing, construct an out-of-scope path, since an in-scope path is already safe.
- [ ] D. Claude decides which counterexamples are plausible here, since it has no stake in the outcome.
- [ ] E. For source grounding, construct a valid citation that does not support the claim.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: It shows only that identified failure modes shaped the design.
- B: Add the handoff condition, not another arrow.
- C: The counterexample is an in-scope path with an unapproved operation.
- D: Which are plausible is your call.
- E: The chapter gives this example.

**Source:** Review before action: a plan predicts, a result records

## MA-ch10.46

Check each statement that is true about the symlink-plan gate in the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The scope allows changing the course reference.
- [ ] B. The inputs are the learner code, existing tests, pathlib documentation, and a temporary-directory fixture.
- [ ] C. The objective is to demonstrate rejection of an outside-pointing symlink in a disposable fixture without accessing unrelated data.
- [ ] D. The scope allows changing the learner implementation freely.
- [ ] E. The tools field includes a direct API call.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The course reference is something it may not touch.
- B: That is the inputs entry.
- C: That is the objective entry.
- D: It allows it only if evidence requires it.
- E: It states no direct API call.

**Source:** The gate: a reviewed plan, before Claude implements

## MA-ch10.47

Check each statement that is true about the stop and predicts entries in the symlink-plan gate. Each statement is worth 1 point (5 points total).

- [ ] A. The plan defers, keeping partial artifacts, if a needed source is unavailable.
- [ ] B. The plan halts if any command targets material outside the disposable arrangement or scope must expand without review.
- [ ] C. The plan finishes when the fixture demonstrates the rejection, existing tests pass, the diff stays within scope, and the report limits its claim to the stable preflight case.
- [ ] D. A failing existing test means the plan was wrong and reopens it.
- [ ] E. The predicts line is written after the run so that it can match what happened.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is its defer exit.
- B: That is its halt exit.
- C: That is its completion exit.
- D: That is the predicts line.
- E: It is dated before the run.

**Source:** The gate: a reviewed plan, before Claude implements

## MA-ch10.48

Check each statement that is true about running missing_fields and order on the encoded gate plan. Each statement is worth 1 point (5 points total).

- [ ] A. order returns inspect, fixture, test, run, review.
- [ ] B. Passing both checks shows the gate plan is right.
- [ ] C. missing_fields returns the same empty list the all-x plan produced.
- [ ] D. The improvement over the all-x plan is that another person can predict the actions and challenge the evidence.
- [ ] E. The same output from different plans is separated only by the review the chapter describes.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Each step is after the one before.
- B: The plan can still be wrong, for example if the learner code differs from the reference.
- C: Every field is present.
- D: That is the stated improvement.
- E: The checks cannot tell them apart.

**Source:** The gate: a reviewed plan, before Claude implements

## MA-ch10.49

Check each statement that is true about the first three conditions for clearing a plan to go downstream. Each statement is worth 1 point (5 points total).

- [ ] A. The plan names one interest the choice leaves out.
- [ ] B. An empty missing_fields result alone is enough to clear the plan.
- [ ] C. The objective was chosen from at least three candidates that pass the distinctness test pairwise.
- [ ] D. Every state-changing edge needs a human gate regardless of whether the action is reversible.
- [ ] E. Choosing the objective from two candidates is enough if they pass the distinctness test.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: That is part of condition one.
- B: Neither the check nor the cross-field review alone is enough.
- C: That is part of condition one.
- D: A reversible new test needs evidence but not a human gate.
- E: The condition is at least three candidates.

**Source:** The gate: a reviewed plan, before Claude implements

## MA-ch10.50

Check each statement that is true about the last three conditions and what happens after the gate. Each statement is worth 1 point (5 points total).

- [ ] A. Once the gate is passed, the plan is frozen even if a result later contradicts it.
- [ ] B. If nobody has approved the plan, its status is pending and nothing consequential runs.
- [ ] C. The stop field has completion, halt, and defer exits, each with an owner.
- [ ] D. The gate fixes the version Claude implements against.
- [ ] E. You wrote one counterexample before approval and the plan rejects it, or you revised the plan until it did.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A contradicting result reopens it.
- B: That is the stated rule.
- C: That is condition four.
- D: It does not freeze the plan, but it fixes the version being implemented.
- E: That is condition five.

**Source:** The gate: a reviewed plan, before Claude implements

## MA-ch10.51

Check each statement that is true about the Build It stage. Each statement is worth 1 point (5 points total).

- [ ] A. Your version is the baseline: the record of what you understood before Claude touched anything.
- [ ] B. The six tests cover empty order, dependency order, self-cycle, unknown prerequisite, duplicate id, and empty plan.
- [ ] C. You read the six tests first and predict the results.
- [ ] D. You read Claude's version first and then rewrite it in your own words.
- [ ] E. You implement missing_fields and order in your learner workspace before you open the reference.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It is also the instrument you measure Claude's version against.
- B: The chapter lists them.
- C: The prediction comes before the run.
- D: The build comes before the reference.
- E: You cannot audit an ordering you have never computed.

**Source:** Build It: the baseline that lets you audit the plan

## MA-ch10.52

Check each statement that is true about the Use It sequence. Each statement is worth 1 point (5 points total).

- [ ] A. You let Claude Code start implementing and review the diff afterward.
- [ ] B. You ask Claude to critique your plan and then accept each criticism it makes.
- [ ] C. At the planning stage, what returns from Claude Code is an approved plan.
- [ ] D. First you do the formulation work yourself: three candidates, the pairwise results, the selection, and the interest it leaves out.
- [ ] E. You then give Claude Code the bounded objective and the exclusions and ask for a plan in the eight fields, saying explicitly that it should change no file yet.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It acts only after the gate passes.
- B: You check each criticism against the plan and the code yourself.
- C: It is a proposal.
- D: That comes before asking Claude for a plan.
- E: What returns is a proposal.

**Source:** Use It: conduct Claude Code against the plan

## MA-ch10.53

Check each statement that is true about judging Claude Code's account and keeping the record. Each statement is worth 1 point (5 points total).

- [ ] A. Claude's account of why it chose a step is a story about the system, not a trace of it.
- [ ] B. You judge the plan by how well it is argued.
- [ ] C. You preserve the transcript: your prompt, the plan, each revision, the diff, the commands and outputs, the date, and the displayed model label.
- [ ] D. If Claude Code is unavailable, you invent a plausible session transcript and label it as illustrative.
- [ ] E. You judge the plan by what it commits to.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Chapter 1 argued this.
- B: You judge it by what it commits to.
- C: That is the record.
- D: You label the plan as your constructed artifact, record that the session did not run, and do not invent its output or an approval.
- E: A commitment can be checked; an argument can merely persuade.

**Source:** Use It: conduct Claude Code against the plan

## MA-ch10.54

Check each statement that is true about the Ship It artifact. Each statement is worth 1 point (5 points total).

- [ ] A. The artifact brief asks for the proposed plan, validation failures, human revisions, stop conditions, and the final approved scope.
- [ ] B. The field-validation result and the dependency order are included as semantic approval.
- [ ] C. The final version replaces the initial proposal so that there is one clean plan.
- [ ] D. If approval is pending, the plan remains pending.
- [ ] E. The artifact is the reviewed plan.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: These are its listed contents.
- B: They are included, but not as semantic approval.
- C: Versions are preserved rather than replacing the initial proposal.
- D: Claude cannot supply the approval.
- E: It is the chapter's deliverable.

**Source:** Ship It: the reviewed plan

## MA-ch10.55

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter's template is a signature.
- [ ] B. The sign-off says the work succeeded.
- [ ] C. The "Not checked" line does the work.
- [ ] D. Withholding is an honest result when the evidence does not support signing.
- [ ] E. The sign-off should be drafted by Claude because it can write fluent words quickly.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The chapter says it is the template, not a signature.
- B: It says only that the plan survived the review described.
- C: It records what the review did not cover.
- D: The sign-off allows approved, returned for revision, or withheld.
- E: Write it from your record; fluency is not evidence.

**Source:** Ship It: the reviewed plan

## MA-ch10.56

Check each statement that is true about the driver's-seat table. Each statement is worth 1 point (5 points total).

- [ ] A. Approval, wider scope, and stopping on a new risk: Claude decides and records it.
- [ ] B. Evidence conditions on edges: Claude proposes candidates, and you apply the stranger test and mark who can apply each.
- [ ] C. Drafting steps, tools, and order: Claude drafts and runs the ordering, and you build missing_fields and order yourself first, then revise the draft.
- [ ] D. Framing the problem: Claude adds candidates you missed, and you write your candidates first, certify they differ, and select one.
- [ ] E. Counterexamples: you generate many quickly, and Claude judges which are plausible here.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: You decide and record it.
- B: A condition only its author can apply is not yet a handoff.
- C: You cannot audit an ordering you have never computed.
- D: Selection centers some interests and decenters others.
- E: Claude generates; you judge plausibility.

**Source:** Ship It: the reviewed plan

## MA-ch10.57

Check each statement that is true about the verify and reflect step. Each statement is worth 1 point (5 points total).

- [ ] A. You name which claim each check addresses and trace each error to duplicate, unknown dependency, or cycle rather than saying ordering failed generically.
- [ ] B. You check whether your graph omits real dependencies or invents unnecessary ones.
- [ ] C. Two steps that are both ready under the function can safely run concurrently.
- [ ] D. You preserve at least one unsafe or useless plan that still passes the structural checks.
- [ ] E. Planning is valuable when it merely predicts the steps you already took.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The tracing is part of the check.
- B: The function cannot do this for you.
- C: Parallel readiness means no declared dependency, not proof that concurrent execution is safe.
- D: It shows what the structure cannot catch.
- E: It is valuable when revision happens before the cost of action.

**Source:** Verify and reflect

## MA-ch10.58

Check each statement that is true about the closing sections on Chapter 11 and the Anthropics comparison. Each statement is worth 1 point (5 points total).

- [ ] A. The final answer may skip the chain from plan to tool result to independent check.
- [ ] B. The Anthropics section asks you to explain whether the task needs a fixed sequence or model-directed choices.
- [ ] C. Chapter 11 follows one planned tool request through validation, dispatch, result association, and independent checking.
- [ ] D. A tool result supplies evidence about what did happen, while a plan says what should happen.
- [ ] E. The eight fields come from Anthropic's Building effective agents guidance.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: It must not skip that chain.
- B: That is its comparison question.
- C: The plan is carried forward as the prediction.
- D: They are different kinds of record.
- E: The eight fields remain this course's own review instrument.

**Source:** A plan predicts action; a result records it

## MA-ch10.59

Check each statement that is true about the Computational Skepticism refinement of testability. Each statement is worth 1 point (5 points total).

- [ ] A. A condition only its author can apply has not yet become a handoff condition.
- [ ] B. An acyclic graph makes the handoff trustworthy.
- [ ] C. You should leave edge conditions untiered so that every condition counts equally.
- [ ] D. Whether a cited clause really governs the change is a condition any non-author can apply.
- [ ] E. Testability is graded: some conditions any non-author can apply, while others only a qualified reviewer can.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It fails the stranger test.
- B: It orders work; it does not make the handoff trustworthy.
- C: Mark each with its tier.
- D: Only a qualified reviewer can apply it.
- E: That is the refinement.

**Source:** Computational Skepticism

## MA-ch10.60

Check each statement that is true about the Conducting AI practices the chapter adds. Each statement is worth 1 point (5 points total).

- [ ] A. Applying the change-the-actor move to your plan means asking whether the binding constraint is the test, the function, or the caller's expectation.
- [ ] B. The three moves are cited research, so their outputs need no further test.
- [ ] C. One move for producing candidates that really differ is to zoom out until the original metric becomes a symptom.
- [ ] D. The appendix's companion check is to mark every constraint in your scope field as real or assumed and test one you suspect is assumed.
- [ ] E. One move for producing candidates that really differ is to change the actor by asking whose constraint actually binds.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The chapter poses that question.
- B: They are the book's own scaffolds, so every output gets the distinctness test.
- C: It is one of the three moves.
- D: If none ever turns out to be assumed, you are not looking.
- E: It is one of the three moves.

**Source:** Conducting AI
