# Chapter 10: Planning before acting

## ES-ch10.1

A planning tool validates a plan dictionary with this function:

```python
FIELDS = ("objective", "inputs", "scope", "steps", "tools", "risks", "verification", "stop")

def missing_fields(plan):
    return [f for f in FIELDS if not plan.get(f)]
```

A plan has all eight keys present, and every value is the string "x". Predict what the function returns, say what that result does and does not show about the plan, and say what the check is useful for.

**Points:** 5

**Rubric (1 point each):**

1. States that the function returns an empty list, because every value is a nonempty and therefore truthy string.
2. Says the empty list is the correct output for the rule the function implements, not a bug in the function.
3. Says the result does not show that the objective matters, the scope is safe, the risks are plausible, the verification tests the claim, or the stop condition can be observed.
4. Says the check is useful for cheaply and deterministically catching absent or false-valued entries, that is, structural omissions.
5. Says a clean form must not be presented as a trustworthy plan, so semantic review is still needed, while the check itself is not made pointless.

**Source:** What missing_fields actually checks

## ES-ch10.2

A team lead reports that 100% of the plans produced by the team's coding agent last month passed an automated completeness check: all of objective, inputs, scope, steps, tools, risks, verification and stop were present and nonempty. The lead concludes that the agent plans well and proposes letting plans run without human review. Evaluate the conclusion and say what additional evidence the team would need.

**Points:** 5

**Rubric (1 point each):**

1. Says a completeness check measures presence, so passing shows that nothing is missing and does not show that the plans are good.
2. Notes that fluent filler can satisfy a form, and that a 100% pass rate with no variation suggests the check is too weak to discriminate between good and bad plans.
3. Names properties the check cannot measure, such as whether the objective fits the need, the scope is safe, the verification tests the claim and the stop condition is observable.
4. Proposes further evidence, such as reviewers auditing a sample of plans against stated criteria, counterexample tests, the rate at which reviewers reject plans that passed, and outcomes of executed plans.
5. Recommends keeping human approval at least for state-changing actions and reporting the metric under its true name, structural completeness.

**Source:** What missing_fields actually checks

## ES-ch10.3

Three validators are proposed for a plan dictionary with eight required keys. V1 passes if every key is present in the dictionary. V2 passes if `plan.get(key)` is truthy for every key. V3 does everything V2 does and also requires the steps value to be a list of dictionaries that each have an id. Compare what the three accept and reject using three inputs: risks equal to an empty list, scope equal to the integer 0, and steps equal to the string "inspect then build". Then name two kinds of defect that none of the three can detect.

**Points:** 5

**Rubric (1 point each):**

1. Says V1 tests only for key presence, so it accepts all three inputs, including the empty list and 0.
2. Says V2 rejects the empty list and 0 because they are falsy, but accepts the string for steps, since any truthy value passes regardless of type.
3. Says V3 additionally rejects the string for steps and so catches type and shape errors that V2 cannot.
4. Notes that truthiness can misclassify legitimate falsy values such as 0 or False, so a field where those are meaningful needs explicit checks.
5. Names two defects none can detect, such as a verification that tests a proxy, a scope that permits harmful actions, or a dependency cycle or missing dependency among the steps.

**Source:** What missing_fields actually checks

## ES-ch10.4

Describe a layered review for an agent's proposed plan that has four layers: an automated structural check, a cross-field consistency review, counterexample testing and human approval. For each layer, say what kind of defect it catches that the others tend to miss, and why no single layer can replace the rest.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the structural check cheaply and deterministically catches absent or false-valued entries but cannot see meaning.
2. Explains that cross-field review finds contradictions between fields, for example verification that does not measure the objective, or steps that need tools or inputs the plan does not list.
3. Explains that counterexample testing builds concrete cases that satisfy a field's wording but fail its purpose, and asks whether the plan rejects them.
4. Explains that human approval is an accountable decision about scope, risk and authority, made by a named person, which cannot be delegated to the model that drafted the plan.
5. Explains that the layers fail differently, so passing one says little about the others, and that skipping early layers wastes scarce human attention.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.5

Explain the difference between each of these pairs, giving a concrete example from agent planning for each and the kind of check that could address it: (a) a plan field being present versus meaningful, (b) a dependency graph being acyclic versus executable, (c) an action being valid in a plan versus authorized.

**Points:** 5

**Rubric (1 point each):**

1. Explains presence versus meaning with an example, such as every field filled with a placeholder or a vague entry like "be careful".
2. Explains acyclic versus executable with an example, such as an omitted prerequisite that leaves the graph acyclic while the real order is impossible.
3. Explains valid versus authorized with an example, such as a delete step that fits the ordering but exceeds the permission the task was given.
4. Names a different kind of check for each pair: semantic or cross-field review, real-dependency and handoff review, and permission boundaries plus approval by an accountable person.
5. Explains that each structural check can be correct under its own rule while leaving the other property untested, so conflating them gives false assurance.

**Source:** Acyclic does not mean executable

## ES-ch10.6

A pipeline extracts invoice dates from scanned documents with an LLM. Its validator confirms that the output is valid JSON matching a schema and that the date string parses as a real calendar date. Ninety-nine percent of outputs pass the validator. A manual audit of 200 outputs finds that 60 contain the wrong date. Explain how both facts can be true, say what the 99% figure should be called, calculate the accuracy the audit suggests, and describe what additional evaluation is needed.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the validator checks format and parseability, not correctness, so a well-formed date can still be the wrong date.
2. Calculates that 60 wrong out of 200 is 30% wrong, so the audit suggests about 70% accuracy, far below the 99% pass rate.
3. Says the 99% should be reported as a format-validity or schema-conformance rate, not as accuracy.
4. Proposes content-level evaluation, such as a labeled reference set, comparison against the source text, or a verification model checked against human labels.
5. Notes that a sample of 200 gives an estimate with uncertainty (roughly plus or minus 6 percentage points at 95% confidence), and that the validator may remain useful as a cheap first filter.

**Source:** What missing_fields actually checks

## ES-ch10.7

A team using an LLM coding agent debates whether the agent must submit a plan for review before it changes any file. Argue for or against the requirement, covering the cost of revision, what the plan makes inspectable, and what the plan should not be expected to contain.

**Points:** 5

**Rubric (1 point each):**

1. Says revising a plan before action costs far less than repairing or rolling back work after it.
2. Says a plan exposes the objective, scope, inputs, steps, tools, verification and stopping rule while change is cheap, so others can critique them.
3. Says the plan is a public commitment to actions, not a transcript of the model's private reasoning, and a model's explanation of itself is not a reliable trace.
4. Says review only matters if someone accountable can reject or revise the plan before anything runs.
5. Names a limit, such as proportionate effort for small reversible tasks, or that plans rest on assumptions and must be revised when results contradict them.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.8

Explain how the design-by-contract idea, in which a human writes preconditions, postconditions and invariants and tests are derived from them, applies to work delegated to a coding agent. Say what the human owns, what the agent produces, and why the tests must derive from the contract and not from the agent's code.

**Points:** 5

**Rubric (1 point each):**

1. Says the human writes the contract: the required behavior, boundaries and invariants, before implementation.
2. Says the agent writes the implementation against that contract.
3. Says tests or assertions derived from the contract check the implementation independently of the agent's assumptions.
4. Says tests derived from the agent's own implementation would encode whatever it does, including its mistakes, and so would be circular.
5. Says an incomplete contract leaves gaps the agent may fill with guesses, so completeness of the contract is the human's responsibility.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.9

An agent implemented a discount rule from a written requirement. While reviewing the diff, a reviewer finds that the code rounds to the nearest cent using banker's rounding, and the requirement never said how to round. Describe how a team that plans before acting should respond, covering the requirement, the plan, the code and the record. Explain why this episode does not show that up-front planning was wasted.

**Points:** 5

**Rubric (1 point each):**

1. Says to reopen the requirement and have someone with authority decide the intended rounding explicitly, rather than accept the agent's incidental choice.
2. Says to update the plan, acceptance criteria and tests with the decision, recording the reason and keeping the earlier version.
3. Says to re-review the revised plan before continuing, and to change the code to match the decision.
4. Explains that finding a gap through a result is normal because problem and solution develop together, and what matters is that the revision is visible.
5. Explains that a reviewed first plan lets the team see which decision the evidence reopened, and that the revision costs a paragraph rather than a rollback.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.10

Compare three ways to structure an LLM system that completes multi-step tasks: (1) a fixed workflow of predefined steps, (2) plan-and-execute, in which a model writes a plan up front and an executor follows it, and (3) an adaptive loop in which the model picks each next action after seeing the last result. For each, give a task it suits and one characteristic risk, and say where human review of the plan is easiest.

**Points:** 5

**Rubric (1 point each):**

1. Describes a fixed workflow as suited to a predictable path, such as extract, classify and format, with the risk of brittleness when inputs deviate.
2. Describes plan-and-execute as suited to decomposable work such as a multi-file refactor, with the risk of a stale plan when results contradict its assumptions.
3. Describes the adaptive loop as suited to open-ended investigation where the next action depends on observations, with risks of drift, cost and compounding errors.
4. Says plan review is easiest where the full intended sequence exists before action (fixed workflow and plan-and-execute), and that adaptive loops need bounds such as scope, budgets and approval points.
5. States the common guidance to use the simplest design that works and add autonomy only where fixed paths fail.

**Source:** Anthropics

## ES-ch10.11

A developer gives a coding agent the request "add rate limiting to the API." The agent returns working code with confident commentary. Explain why this outcome is likely, why the agent may not say that the request was underspecified, and list at least four decisions the developer should settle in a plan before the agent starts.

**Points:** 5

**Rubric (1 point each):**

1. Explains that language models complete requests fluently and choose plausible defaults for unspecified details.
2. Explains that such a model does not reliably flag gaps in a specification, so confident commentary can hide choices that nobody reviewed.
3. Names at least four decisions to settle, such as the limit values, the key being limited (per user, per address, per token), where counters are stored, the response on exceeding the limit, and which endpoints are in scope.
4. Says these decisions should be written down where another person can challenge them, and reviewed before implementation.
5. Says a complete specification yields better implementations than an incomplete one, and the cost of discovering a missing decision is lowest before the build.

**Source:** Planning before acting (opening section)

## ES-ch10.12

Define a phase gate between AI work and human work in a pipeline. Then write a gate for a pipeline in which an AI drafts a summary of a clinical-trial paper for a human editor. Your gate must say what each side handles and give a condition that a person who did not build the pipeline can test.

**Points:** 5

**Rubric (1 point each):**

1. Defines a phase gate as an explicit point where the AI's work stops and a person's begins, with a specified division of tasks and a condition that must hold before output moves downstream.
2. States what the AI handles, such as drafting the summary and listing each number with its source location, and what the human handles, such as checking claims, framing and the decision to publish.
3. Writes a testable condition, such as every number in the summary appearing in the paper's tables or text with the location cited.
4. Explains that a stranger should be able to apply the condition to a sample and reach the same verdict, avoiding interpretive words such as "accurate" or "reasonable".
5. Names the route taken when the condition fails, such as returning the draft to the AI step or blocking publication.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.13

A company wants an LLM system for three tasks: (a) turn each incoming invoice PDF into a fixed set of fields and post them to a ledger, (b) investigate why a nightly data job started failing, and (c) draft a weekly report from the same five data sources each time. For each task, argue whether a fixed workflow or a model-directed agent fits better, and say what you would put in the plan for the agent task.

**Points:** 5

**Rubric (1 point each):**

1. Argues that task (a) fits a fixed workflow because its steps are known, volume is high, and deterministic validation can sit between steps.
2. Argues that task (c) fits a fixed workflow or prompt chain, because the sources and structure repeat, with a verification gate before the report goes out.
3. Argues that task (b) fits a model-directed agent, because the next action depends on what each finding reveals.
4. Says the plan for the agent task should include scope limits (read-only tools by default), a step or time budget, stop conditions, what it must report, and human approval for state-changing actions.
5. States the guidance to prefer the simplest solution that works, since autonomy costs predictability, expense and ease of review.

**Source:** Anthropics

## ES-ch10.14

Define the "error of the third kind" in the sense Kimball gave it for problem formulation, and illustrate it with an example from an AI-assisted project. Explain why a fluent answer from an AI assistant can make this error costlier, and why checking an answer against the framing it already assumes cannot detect it.

**Points:** 5

**Rubric (1 point each):**

1. Defines the error of the third kind as giving a right answer to the wrong problem.
2. Gives a sound example, such as building an accurate model for the wrong target, or optimizing a metric that does not serve the actual need.
3. Explains that polished, internally consistent output carries an authority that the question never earned and so reduces scrutiny of the framing.
4. Explains that an audit measured against the assumed framing is not independent of it, so it cannot reveal that the framing is wrong.
5. Proposes a remedy, such as writing candidate formulations that differ in what counts as success before planning, and checking them against stakeholders.

**Source:** Formulate before you plan

## ES-ch10.15

Explain how an early, usually tacit framing of a problem (what design researchers call a primary generator) shapes which solutions a team can see, and why it matters whether a person or an LLM supplies the first framing. Describe a procedure for using an LLM in problem framing that keeps independent judgment.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the first idea of what a problem is really about decides which solutions come to mind and which stay invisible.
2. Says that having some first framing is unavoidable, so what matters is naming it.
3. Says that if the LLM supplies the first framing it becomes the default anchor, presented as neutral analysis.
4. Describes a procedure: write your own candidate framings first, then ask the LLM to extend and attack them.
5. Says candidates should be compared with explicit criteria set independently of any one framing, and that the model's framing is not wrong by construction but needs comparison.

**Source:** Formulate before you plan

## ES-ch10.16

A team must decide what "improve search" means for an online store. Candidate formulations are: (X) raise the click-through rate on result pages; (Y) raise the share of queries for which a human-labeled relevant item appears in the top three results; (Z) raise purchases per search session. State a test for whether candidate formulations are really distinct. Then construct one result that counts as success under X but not under Y, and one that counts as success under Y but not under Z, and explain what this shows.

**Points:** 5

**Rubric (1 point each):**

1. States the test: formulations are distinct if they would require different solutions even to test, and if one solution satisfies all of them they are one formulation reworded.
2. Constructs a result that succeeds on X but fails Y, such as sensational result titles or promoted items that attract clicks while labeled-relevant items fall out of the top three.
3. Constructs a result that succeeds on Y but fails Z, such as better relevance for informational queries with no change in purchases, or relevant items that are unavailable or unattractive to buy.
4. Explains that disagreement on constructed results shows the formulations are different problems with different measurements and solutions.
5. Says the team must then choose with explicit criteria and state whose interests the chosen formulation centers and which it leaves out.

**Source:** Formulate before you plan

## ES-ch10.17

A team scores candidate problem formulations only on cost, time and technical feasibility. Explain what is wrong with this, which criteria should be added, and why the criteria should be written before any candidate is scored.

**Points:** 5

**Rubric (1 point each):**

1. Explains that cost, time and feasibility alone select the most tractable formulation, which is not necessarily the most important one.
2. Adds a salience criterion: if this is solved, does it address what matters in this situation.
3. Adds a criterion about whose interests the formulation centers and decenters.
4. Explains that criteria written before scoring cannot be tuned afterward to favor a preferred option.
5. Says the criteria encode values and need a named owner, and that an AI can draft candidates but should not make the value selection.

**Source:** Formulate before you plan

## ES-ch10.18

A team chose, from three formulations of a bug-fix task, the one that restores the documented behavior for all callers, over one that only makes the failing test pass and one that teaches a junior developer the cause. Write the short statement a plan should contain to make this a defended selection, and explain why silence about the alternatives is a problem.

**Points:** 5

**Rubric (1 point each):**

1. States which formulation was chosen and why.
2. Names what the choice leaves out, such as the junior developer's understanding or the narrow test-only view.
3. Says how or where the omitted interest is handled, for example in a separate step, or states that it is accepted as not served.
4. Explains that silence hides a value judgment and prevents others from challenging it.
5. Says the selection must carry into the objective, scope, verification and stop fields, since otherwise the plan drifts from its stated purpose.

**Source:** Formulate before you plan

## ES-ch10.19

Describe what an LLM can usefully contribute to formulating a problem and what should stay with a human. Give a concrete example of each, and explain why the model cannot take over the human part.

**Points:** 5

**Rubric (1 point each):**

1. Names model contributions: extending the candidate list, finding a result that passes one formulation and fails another, and attacking the selection.
2. Gives a concrete example of such a contribution.
3. Names human responsibilities: certifying that formulations differ in the domain, choosing between interests, and owning the decision.
4. Explains that these require situated knowledge, values and accountability, and that a model has no name to put on the decision.
5. Says the model's critiques are proposals to be verified against the actual artifacts, not conclusions.

**Source:** Formulate before you plan

## ES-ch10.20

A plan for an agent has eight fields: objective, inputs, scope, steps, tools, risks, verification and stop. Choose any four of the fields. For each one, state the question the field is meant to answer, write an entry that fills the field without doing any work, and write an entry that a reviewer could challenge.

**Points:** 5

**Rubric (1 point each):**

1. For the first chosen field, states the question it answers and contrasts a vacuous entry with a challengeable one (for example scope: "be careful" versus named paths, permitted operations and excluded systems).
2. For the second chosen field, does the same with a correct question and a clear contrast.
3. For the third chosen field, does the same with a correct question and a clear contrast.
4. For the fourth chosen field, does the same with a correct question and a clear contrast.
5. Explains that a challengeable entry gives a reviewer something concrete to disagree with, whereas a vacuous entry would pass a presence check and still do no work.

**Source:** The eight fields are eight questions

## ES-ch10.21

An agent is asked to "clean up the customer database." Its first plan reads: objective, "improve data quality"; inputs, "the database"; scope, "be careful"; steps, "clean the data"; tools, "SQL"; risks, "some data may be affected"; verification, "check the result"; stop, "when finished." Identify what is wrong with each field and rewrite any four of them so that a reviewer could challenge them.

**Points:** 5

**Rubric (1 point each):**

1. Observes that every field is nonempty, yet none states an observable outcome, a boundary, a source or a check.
2. Rewrites the objective as an outcome that can be tested, such as removing duplicate customer records that match on a defined key while deleting no other data.
3. Rewrites the scope with named tables, permitted and forbidden operations, and excluded systems, for example working on a copy or forbidding deletes without approval.
4. Rewrites the verification with exact checks, such as a duplicate-detection query returning zero rows, row counts reconciled against a backup, and a sample compared by hand.
5. Rewrites the stop, tools or risks with completion, halt and defer exits, the operations the tool may and may not perform, or each risk tied to a mitigation and owner.

**Source:** The eight fields are eight questions

## ES-ch10.22

Describe four consistency checks a reviewer should make across the fields of a plan, for example objective against verification. For each, give a concrete contradiction that a presence check would not catch.

**Points:** 5

**Rubric (1 point each):**

1. Describes objective against verification, with a contradiction such as a check that confirms a file exists when the objective is that the code behaves correctly.
2. Describes steps against inputs, tools and scope, with a contradiction such as a step that reads data the inputs and scope do not authorize, or a step needing a capability the tools lack.
3. Describes risks against mitigations, owners and stop triggers, with a contradiction such as a listed risk that no step, owner or trigger addresses.
4. Describes a fourth check, such as a late change of objective against earlier risk and verification analysis, or an edge against the handoff it requires.
5. Explains that fields that are individually nonempty can still contradict each other, and that cross-field review is what turns separate entries into one argument.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.23

An agent's plan lists a shell tool with write access to a whole repository and network access, although its steps only read files and run tests. Explain the difference between capability and authority, say what is wrong with this plan, and say how the plan should handle a later discovery that fixing the bug requires editing a file outside the declared scope.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes capability, what a tool can do, from authority, what the task is permitted to do.
2. Says the tools should match the steps (least privilege), and that unneeded write and network capability expands the risk surface for errors or injected instructions.
3. Says authority should be enforced at runtime by permissions or a sandbox and not only stated in the plan text.
4. Says the out-of-scope edit should halt the work and send the plan back for revision and approval by an accountable person before the edit.
5. Says the expansion should not be disguised as an implementation detail, and the revision and its reason should be recorded.

**Source:** The eight fields are eight questions

## ES-ch10.24

Classify each of the following parts of a plan as something an AI can reasonably draft for human review or as a decision that stays with a person, and justify each classification: the step list, the tools list, the objective, the risks the organization will accept, who has authority to stop the work, and any widening of scope.

**Points:** 5

**Rubric (1 point each):**

1. Classifies the step list as draftable by an AI for review, since the person can revise a draft.
2. Classifies the tools list as draftable but checked against the steps and scope.
3. Keeps the objective with the person, because it depends on what the work is for and whose interests it serves.
4. Keeps risk acceptance, the authority to stop, and any widening of scope with a person, because they are authority decisions that need a named decider.
5. States the principle: assign by task, not by a blanket claim; AI drafts and challenges, while a summary of evidence is not a decision with a name on it.

**Source:** The eight fields are eight questions

## ES-ch10.25

A plan's risks field reads "data loss, wrong output, cost overrun." Explain what is missing, and then rewrite the field for an agent that migrates a customer table to a new schema, giving for each risk a trigger, a mitigation and an owner.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the risks are not tied to any action, trigger, mitigation or owner, so they change nothing about how the work proceeds.
2. Rewrites data loss with a mitigation such as a backup and a trial run on a copy, and a trigger such as a row-count mismatch that halts the work.
3. Rewrites wrong output with a check such as comparing sampled records between old and new tables, and a trigger that sends the work back to diagnosis.
4. Rewrites cost overrun with a budget and a defer exit, and gives each risk a real owner such as a named role, not the model or an invented person.
5. Notes that some risks may be explicitly accepted, and that an unowned or untriggered risk is a defect of the plan.

**Source:** The eight fields are eight questions

## ES-ch10.26

A function orders plan steps by repeatedly removing, in one batch sorted by id, every step whose prerequisites have all been removed:

```python
def topo_order(steps):
    graph = {}
    for s in steps:
        if s["id"] in graph:
            raise ValueError("Duplicate step")
        graph[s["id"]] = set(s.get("after", []))
    if any(deps - graph.keys() for deps in graph.values()):
        raise ValueError("Unknown prerequisite")
    result = []
    while graph:
        ready = sorted(k for k, d in graph.items() if not d)
        if not ready:
            raise ValueError("Dependency cycle")
        for k in ready:
            result.append(k)
            del graph[k]
        for d in graph.values():
            d.difference_update(ready)
    return result
```

It is called with seven steps: ingest and config have no prerequisites; parse requires ingest; validate requires parse and config; index requires validate; notify requires index; audit requires parse. Trace the function. Give the list it returns, the steps removed in each round and the number of rounds, show another valid order that the function does not return, and explain why it returned the one it did.

**Points:** 5

**Rubric (1 point each):**

1. Gives the returned list: config, ingest, parse, audit, validate, index, notify.
2. Gives the rounds: {config, ingest}, {parse}, {audit, validate}, {index}, {notify}, which is five rounds.
3. Explains that config precedes ingest and audit precedes validate because ids are sorted within a ready batch.
4. Gives another valid order, such as ingest, config, parse, validate, audit, index, notify, showing that the order is not unique.
5. Explains that sorting is a tie-break that makes output deterministic and does not show that the returned order is best.

**Source:** Dependencies are directed obligations

## ES-ch10.27

An ordering function for plan steps can fail in three different ways: a duplicate step id, an unknown prerequisite, and a dependency cycle. Explain what defect each failure represents, give an input that triggers each, and say how the remedies differ. Then explain why the unknown-prerequisite check should run before the main ordering loop.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a duplicate id makes two steps indistinguishable, with an input such as two steps both named "test", and that the remedy is to rename or merge them.
2. Explains that an unknown prerequisite refers to work that does not exist, with an input such as "verify" requiring an undefined "test", and that the remedy is to define the step or correct the reference.
3. Explains that a cycle means steps wait on each other, with an input such as a requires b and b requires a, and that the remedy is to redefine the steps or their obligations.
4. Says that the three remedies differ and should not be conflated.
5. Explains that without the earlier check a step with a nonexistent prerequisite would never become ready and would be misreported as a cycle.

**Source:** Dependencies are directed obligations

## ES-ch10.28

A Python function builds each step's prerequisites with `set(step.get("after", []))`. A user writes the step `{"id": "verify", "after": "build"}` and a step with id "build" exists. Predict the outcome, explain the cause at the Python level, say whether the resulting error message helps, and propose two ways to prevent the problem.

**Points:** 5

**Rubric (1 point each):**

1. Predicts an error reporting an unknown prerequisite, not a successful ordering.
2. Explains that iterating a string yields its characters, so `set("build")` is the set of the five letters b, u, i, l, d.
3. Says the message misleads, since it points at a missing prerequisite and not at the wrong type of the value.
4. Proposes validating the type, for example raising a clear TypeError unless the value is a list or tuple.
5. Proposes a second safeguard, such as normalizing a lone string to a one-element list, using a schema or type checker, or adding a test for this input.

**Source:** Build It: the baseline that lets you audit the plan

## ES-ch10.29

Explain why, in a finite dependency graph in which every prerequisite names an existing step, a nonempty set of remaining steps with none ready must contain a cycle. Then explain what changes if one prerequisite names a step that does not exist.

**Points:** 5

**Rubric (1 point each):**

1. Explains that if no remaining step is ready, each remaining step has an unfinished prerequisite among the remaining steps.
2. Explains that following prerequisite links from step to step must eventually revisit a step because the graph is finite.
3. Concludes that the revisited step lies on a cycle, so none of the steps on it can ever start.
4. Explains that a nonexistent prerequisite also prevents a step from becoming ready, but without any cycle, so it is a different defect.
5. Concludes that references must be validated before the ordering loop so that each defect gets its own accurate message and remedy.

**Source:** Dependencies are directed obligations

## ES-ch10.30

Five plan steps are ordered by a function that removes all ready steps in each round and sorts their ids within the round. Step a has no prerequisites. Steps b, c and d each require a. Step e requires b, c and d. State the returned order and the number of rounds, count the valid orderings, and explain what the tie-break does and does not mean.

**Points:** 5

**Rubric (1 point each):**

1. States the returned order: a, b, c, d, e.
2. States that there are three rounds: {a}, {b, c, d}, {e}.
3. States that there are six valid orderings, because b, c and d can appear in any of 3! = 6 orders between a and e.
4. Explains that the sorted tie-break makes output deterministic and reproducible, which helps testing and comparison.
5. Explains that it does not show that alphabetical execution is best, nor that b, c and d may safely run at the same time.

**Source:** Dependencies are directed obligations

## ES-ch10.31

Two steps in a plan graph have no declared dependency between them and become ready together. One regenerates a search index in place, and the other runs an evaluation that reads that index. Explain why an ordering function treats them as independent, why that is wrong in practice, and what constraints would fix it. Say also whether every parallel-ready pair is unsafe.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the function sees only the declared edges and does not know that both steps touch the same resource.
2. Explains the hazard: the evaluation may read a partially written or stale index and produce misleading results.
3. Proposes a fix, such as adding an edge so evaluation follows regeneration, regenerating into a new copy and switching, or locking.
4. States that parallel readiness means no declared dependency, not proof that concurrent execution is safe, and that resource and authority conflicts lie outside the graph unless added.
5. States that many parallel-ready pairs are safe, such as two independent read-only checks, so the conclusion is not that all parallelism is unsafe.

**Source:** Dependencies are directed obligations

## ES-ch10.32

Design six tests for a function that orders plan steps. Each step is a dictionary with an id and an optional list under "after". The function returns ids with all ready steps taken in sorted order each round, and raises ValueError for a duplicate id, an unknown prerequisite or a cycle. For each test give the input and the expected result and say why it is a useful boundary case.

**Points:** 5

**Rubric (1 point each):**

1. Includes the empty input with expected result an empty list, as the smallest boundary.
2. Includes a dependency chain listed in reverse, with the expected result in dependency order, to show that input order does not decide output order.
3. Includes independent steps with expected result in sorted id order, to show the deterministic tie-break.
4. Includes a duplicate id and an unknown prerequisite as separate tests expecting different errors, because the defects and remedies differ.
5. Includes a self-dependency and a two-step mutual dependency expecting the cycle error.

**Source:** Build It: the baseline that lets you audit the plan

## ES-ch10.33

A plan lists the steps "load data", "train model" and "evaluate model". Its author forgot to declare that "train model" requires "load data". An ordering function reports no error. Explain why no error appears, how the plan might still be impossible to run, and what practices help find omitted dependencies.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the function orders only the arrows that were declared, and with no arrow between two steps any order is accepted.
2. Explains that acyclic means only that some order satisfies the declared arrows, not that the arrows match reality.
3. Describes the consequence: training might run before the data exists, or on stale data, and fail or silently produce a bad result.
4. Proposes practices, such as asking of each step what inputs it needs and which step produces them, walking through the plan by hand, or constructing a state where prerequisites are done but a needed artifact is absent.
5. Says to add a handoff condition that states what the earlier step must deliver, and not only another arrow.

**Source:** Acyclic does not mean executable

## ES-ch10.34

Construct a plan for an agent that is acyclic and has every field filled, yet exceeds the authority the agent was given. Explain why it passes structural checks, give at least three reasons a reviewer should reject it, and say which control could stop it even if the review failed.

**Points:** 5

**Rubric (1 point each):**

1. Gives a concrete plan, for example "free disk space" with steps inspect, delete old backups and verify, each depending on the one before.
2. Explains that it passes because every field is nonempty and the dependency graph has no cycle, and neither check looks at what the actions do.
3. Gives at least three reasons to reject it, such as exceeding scope, irreversible deletion, no approval for a destructive step, or a verification that does not test the claim.
4. Names a control that could stop it anyway, such as runtime permissions, a sandbox, a deny-list of destructive operations, or a required human approval prompt.
5. States that valid is not the same as authorized, and that no structural check can supply authorization.

**Source:** Acyclic does not mean executable

## ES-ch10.35

A plan declares that implementation requires review and that review requires implementation, so ordering fails with a dependency-cycle error. Explain what the cycle reveals, why simply deleting one edge is the wrong response, and show a revised set of steps and the resulting order.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the cycle reveals one word, review, doing two jobs with different inputs.
2. Explains that deleting an edge makes the error disappear without asking what each step needs, and may hide an unclear definition.
3. Shows revised steps: plan review, implementation, and result review.
4. Distinguishes the jobs: plan review approves a proposed method, and result review evaluates the actual output using evidence.
5. States the resulting order, plan review then implementation then result review, and notes that running the ordering function on the revised steps confirms there is no cycle.

**Source:** Acyclic does not mean executable

## ES-ch10.36

A plan declares that "review" comes after "run tests". Explain what that declaration does and does not say. Then write a handoff condition for the edge that a reviewer who did not run the tests could apply, saying what the test step must hand over and what happens if the evidence is inadequate.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the declaration gives order and does not define the object handed from one step to the next.
2. Specifies the handoff contents: the exact commands run, their exit statuses and output, and an identification of the code version that was tested, such as a diff hash.
3. Says the evidence should come from the test runner, not from the model's description of it.
4. Explains that the reviewer can then check whether the commands correspond to what the plan proposed and whether the evidence matches the current code.
5. Defines the failure route: if the evidence is missing or the tests fail, the work returns to implementation or stops pending diagnosis, and does not proceed as if review were approval.

**Source:** Evidence belongs on the edges

## ES-ch10.37

A team's handoff condition between an AI-drafted contract summary and a lawyer's review reads: "The summary has been checked and is accurate and complete." Explain why this condition is not testable, describe a procedure for turning it into a testable one, and rewrite it.

**Points:** 5

**Rubric (1 point each):**

1. Defines testable: someone who did not build the pipeline can read the condition, observe the system and decide whether it holds.
2. Identifies the interpretive words, "checked", "accurate" and "complete", which have no stated criterion, so different people would apply them differently.
3. Describes the procedure: write the condition, mark each interpretive word, replace each with a criterion, give it to a person who did not write it to apply to a sample case, and repeat if they cannot decide.
4. Gives a rewrite with observable criteria, such as each figure in the summary matching the contract text with a section reference, every clause on an agreed list of key terms appearing, and no flagged item left unresolved.
5. Notes that judgments requiring expertise, such as whether a clause governs a given situation, should be assigned to a named qualified reviewer instead of being hidden inside a vague word.

**Source:** Evidence belongs on the edges

## ES-ch10.38

An agent finishes a task and reports, "I ran the tests and everything passes." Explain why this statement is weaker evidence than a test runner's own output, what it means for evidence to be independent of the thing it certifies, and what a handoff condition should require instead.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the statement is the agent's description of a check, which can be mistaken, incomplete or invented, whereas the runner's output is produced by executing the code and can be inspected.
2. Explains that independent evidence fails differently from the thing it certifies, so its errors are not correlated with the errors being checked.
3. Explains that asking the same model to review its own output repeats one opinion twice and shares its blind spots.
4. Notes that a model's explanation of its own reasoning is a plausible story and not a verified trace of its computation.
5. States that the handoff should require artifacts such as the exact command, exit status, output and a code version identifier, produced by the runner, together with a defined failure route.

**Source:** Evidence belongs on the edges

## ES-ch10.39

A coding agent working in a version-controlled repository has these steps: add a new unit test file; modify an existing function; run a script that deletes a directory outside the repository; post a summary to a team chat channel. Rank the steps by how much evidence and approval their handoffs need, using reversibility, the cost of being wrong, the ease of verification and whether a reviewable trail exists, and justify your ranking.

**Points:** 5

**Rubric (1 point each):**

1. States the criteria: reversibility, cost of error, ease of verifying the output, and whether a trail exists for review.
2. Ranks the deletion outside the repository as needing the most, because it cannot be reverted from a diff and the cost of error is high, so it needs hard human approval or exclusion from scope.
3. Ranks the chat post as needing strong control, because it is externally visible and cannot be reliably unsent.
4. Ranks modifying the function as moderate, because the diff makes it reversible and tests can verify it, while the new test file is lowest, needing evidence but not necessarily a gate.
5. States the principle of attaching evidence conditions to state-changing edges first, and that a tidy sequence diagram does not make an unsafe transition acceptable.

**Source:** Evidence belongs on the edges

## ES-ch10.40

Describe what a plan should say about what happens when a handoff condition fails. Illustrate with three cases: a targeted test fails, a source document needed for a claim is unavailable, and a halt condition is triggered.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a plan written only for success pressures every observation into forward motion, so failure routes must be stated.
2. For the failed test, routes the work back to implementation or to diagnosis, and does not treat the next step, review, as approval.
3. For the missing source, says to shrink the claim or mark it unresolved, and not to substitute a plausible input or fill the field with plausible text.
4. For the triggered halt, says to stop, preserve state, and report why it stopped, what evidence was available, and what decision would allow safe resumption.
5. Says that an identical retry is not a route unless something has changed, and that the options are diagnose, revise the plan or defer.

**Source:** Stop conditions and refusal paths

## ES-ch10.41

Handoff conditions differ in who can apply them. Give an example of a condition any competent non-author can apply, one that only a qualified reviewer can apply, and one that only its author can apply. Explain what to do about each when designing a pipeline.

**Points:** 5

**Rubric (1 point each):**

1. Gives a condition any non-author can apply, such as "the test command exits with status 0".
2. Gives a condition needing a qualified reviewer, such as whether a cited regulation actually governs the proposed change.
3. Gives an author-only condition, such as "the design feels sound", and says it is not yet a usable handoff condition.
4. Says to rewrite author-only conditions until a stranger can apply them, and to assign domain conditions to a named qualified reviewer.
5. Says to mark each condition with who can apply it, and to reserve scarce qualified review for the edges where an error costs the most.

**Source:** Computational Skepticism

## ES-ch10.42

An agent runs the test suite, then makes one more edit, then reports the earlier test results to the reviewer. Explain the problem and describe what a handoff should include to prevent it.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the evidence describes an earlier version of the code, which the reviewer may take to describe the current version.
2. Says the handoff should include an identifier of the code that was tested, such as a commit or diff hash, along with the results.
3. Says the reviewer should check that the identifier matches the code under review.
4. Says any change after a test run requires rerunning the checks, and the handoff should record the commands and when they were run.
5. Notes that a bare statement that review follows the run gives order without correspondence between what ran and what is reviewed.

**Source:** Evidence belongs on the edges

## ES-ch10.43

Write the stop field for an agent that is asked to upgrade a library dependency in a project, with completion, halt and defer exits. For each exit say who decides and what evidence they use. Explain why "stop when done" is inadequate.

**Points:** 5

**Rubric (1 point each):**

1. Gives an observable completion exit, such as the build and existing tests passing, the targeted check passing and a named reviewer accepting the diff.
2. Gives halt conditions, such as a change outside the permitted files, missing authorization, a failed independent check, or restricted input.
3. Gives a defer exit tied to a resource limit, with an incomplete status, preserved partial work and a named person who decides whether to resume.
4. Names owners: an automated check can halt on a failing assertion, while a person decides whether a newly found risk changes the scope.
5. Explains that "stop when done" has no observable condition, cannot be applied by someone else, and invites repeated activity and unsupported completion claims.

**Source:** Stop conditions and refusal paths

## ES-ch10.44

An agent run is limited to 40 steps. Explain what reaching the limit does and does not show, what status the run should report, and what should be preserved. Contrast a resource limit with a finish action.

**Points:** 5

**Rubric (1 point each):**

1. Says a limit bounds effort and does not show that the task succeeded.
2. Says the run should report an incomplete or deferred status and not a fabricated final result.
3. Says partial artifacts and state should be preserved.
4. Says a named person should decide whether to resume, revise or abandon.
5. Contrasts the two: a finish action is a claim that the task is complete, to be checked against completion evidence, while the limit only answers how much effort is allowed.

**Source:** Stop conditions and refusal paths

## ES-ch10.45

Explain what refusal means for an agentic workflow, name four situations that should trigger it, and describe what a useful refusal report contains.

**Points:** 5

**Rubric (1 point each):**

1. Defines refusal as the workflow preserving its state and reporting what blocks the next transition.
2. Names four triggers, such as missing authority, unavailable evidence, an out-of-scope change, a failed independent check, or restricted input.
3. States that the report should say why the step stopped, what evidence was available and what decision would allow safe resumption.
4. Explains that an unexplained halt is hard to tell from a crash.
5. Separates blocks from uncertainty that can be resolved in scope: the agent may search approved sources or propose a smaller task, but cannot grant itself permission it has not been given.

**Source:** Stop conditions and refusal paths

## ES-ch10.46

An agent has run the same failing command five times with no changes between runs and keeps saying it will try again. Explain why this is not progress, what a plan's stop field should say about it, and what the agent should do instead.

**Points:** 5

**Rubric (1 point each):**

1. Explains that identical attempts with no change in code, inputs or hypothesis yield no new evidence.
2. States that activity becomes progress only when it changes the evidence or the decision state.
3. Allows the exception that repeated runs can be deliberate when nondeterminism is suspected, in which case outcomes are recorded across runs.
4. Says the stop field should cap identical retries and route to diagnosis, plan revision or deferral.
5. Says the agent should report what failed, what was tried and what decision or information is needed.

**Source:** Stop conditions and refusal paths

## ES-ch10.47

A deadline approaches, and a team's plan for reviewing an AI-generated analysis produces several hundred review items for a single reviewer. Explain why such a plan is a problem even if it is complete, how to prioritize, and how to handle the deadline honestly.

**Points:** 5

**Rubric (1 point each):**

1. Explains that human attention is a bounded resource, so a plan with hundreds of unprioritized items is practically unauditable.
2. Proposes prioritizing by consequence, such as cost of error, reversibility and difficulty of verifying the item.
3. Proposes sampling or automating checks for low-risk items, and stating which items need human judgment.
4. Says a deadline can justify a reduced objective if the reduction is disclosed.
5. Says skipped verification is not acceptable without disclosure, and the claim should be limited to what was verified.

**Source:** Stop conditions and refusal paths

## ES-ch10.48

An agent is blocked in two ways: it lacks documentation that exists in an approved source, and it lacks permission to modify a production configuration. Explain how a plan should treat each situation and why they should not be handled by the same rule.

**Points:** 5

**Rubric (1 point each):**

1. Treats the missing documentation as information obtainable within scope, so the agent may search the approved source.
2. Treats the missing permission as a need for new authority, which only the party that holds it can grant.
3. Says the agent must not grant itself permission, however good its reason.
4. Says the agent may propose a smaller task that avoids the restricted action.
5. Explains that one block is resolved by looking and the other by a decision, and that the plan should record what was blocked and which decision is needed instead of filling the gap with an assumption.

**Source:** Stop conditions and refusal paths

## ES-ch10.49

Explain the difference between a plan as a prediction and a result as a record. Say what goes wrong if the plan is edited after the run to match what happened, and what should be written before the run.

**Points:** 5

**Rubric (1 point each):**

1. States that a plan predicts what will be done and observed, while a result records what happened.
2. Explains that editing the plan afterward to match the run turns it into a description of the result.
3. Explains that it also erases the review that justified acting, and the chance to learn from the gap.
4. Says to write beforehand, with a date, the expected observations and what a wrong outcome would look like, and not to revise that note afterward.
5. Says a plan may legitimately change when evidence contradicts it, if the change is a new version with the reason recorded and the original preserved.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.50

Describe the practice of writing a counterexample before approving a plan. Give two counterexamples for different fields of a plan, explain what each shows, and explain what passing the counterexamples does and does not prove.

**Points:** 5

**Rubric (1 point each):**

1. Describes the practice: imagine a case that satisfies a field's wording but fails its purpose, and check whether the plan rejects it.
2. Gives a first counterexample with its field, such as a citation that is well formed but does not support the claim, against a source-grounding check.
3. Gives a second counterexample with its field, such as a path inside the permitted scope paired with an unapproved operation such as deletion.
4. Explains what each shows: the verification or scope rule is too weak, and the plan should be revised until it rejects the case.
5. Says that rejecting identified counterexamples shows those failure modes shaped the design, not that the plan cannot fail.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.51

A plan's objective is "ensure the report generator never emits negative totals." Its verification entry is "run the generator once on the sample file and confirm that it exits without error." Evaluate the match between objective and verification and rewrite the verification.

**Points:** 5

**Rubric (1 point each):**

1. Says exiting without error is a proxy that does not show the absence of negative totals.
2. Says one sample run cannot support a claim about "never", since it covers only that input.
3. Says the plan should name what the proxy can and cannot reject.
4. Rewrites the verification to assert that totals are non-negative, using tests with edge cases such as refunds that exceed charges, or property-based tests over generated inputs.
5. Suggests an independent check, such as comparison with a reference computation, and keeping the claim limited to the inputs actually tested.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.52

During execution, a test result contradicts an assumption on which an approved plan rested. Describe how a team should handle it, covering the agent's action, the plan, the review and the record. Explain how this differs from treating the plan as a frozen specification.

**Points:** 5

**Rubric (1 point each):**

1. Says the agent should halt or report the contradiction and not push on with a stale plan.
2. Says the plan should be revised as a new version, with the reason recorded and the original preserved.
3. Says the revised version should be reviewed and approved again before work continues.
4. Says earlier risk and verification analysis should be rerun if the objective or scope changed.
5. Explains that a plan is a versioned object and not a frozen specification, and that having a reviewed first version lets the team see which decision the evidence reopened.

**Source:** The plan is the design, and the review is the gate

## ES-ch10.53

Explain how to use an AI assistant to generate counterexamples to a plan, what the human reviewer must still decide, and why rejected counterexamples should be kept.

**Points:** 5

**Rubric (1 point each):**

1. Says an assistant can generate many counterexamples quickly and has no stake in the outcome.
2. Says the reviewer judges which are plausible in context and which risks deserve checks.
3. Says each counterexample should be checked against the actual plan and not accepted on the assistant's say-so.
4. Says rejected counterexamples should be kept with reasons because a dismissal can expose an assumption, and the original counterexample should be kept beside the revised plan so the final version does not look inevitable.
5. Says the exercise does not prove the plan cannot fail, because the set is finite and may share the model's blind spots.

**Source:** Review before action: a plan predicts, a result records

## ES-ch10.54

An agent's plan ends with the line "Status: approved." Explain why this line is not an approval, what a valid approval record contains, and what the status should be if no qualified person has approved.

**Points:** 5

**Rubric (1 point each):**

1. Explains that approval is an act by an accountable person, and text produced by the model records nothing about that act.
2. States that a valid record names the approver and date, the version reviewed, and the scope approved.
3. States that without a qualified approver the status is pending and nothing consequential runs.
4. Says a model can summarize the evidence for the decision, but a summary is not a decision with a name on it.
5. Says approval fixes the version being implemented, and a result that contradicts the plan reopens it.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.55

Describe the structure of a sign-off on a reviewed plan, listing the lines it should contain, and explain why its claim is smaller than that of a sign-off on an executed result. Explain why a sign-off drafted by a model is a risk.

**Points:** 5

**Rubric (1 point each):**

1. Lists lines such as what was checked, how, what was not checked, what is not claimed, and signed or withheld.
2. Explains that a plan sign-off says the plan survived the described review and does not say the work succeeded.
3. Explains that a sign-off on a result needs the record of what actually ran.
4. Explains that the "not checked" line prevents over-trust, and that withholding a signature is an honest outcome when evidence does not support signing.
5. Explains that a model drafts fluent text quickly, but fluency is not evidence of review, so the statement should be written from the reviewer's own record.

**Source:** Ship It: the reviewed plan

## ES-ch10.56

A team proposes this rule: an agent's plan may be executed if (1) an automated check finds all eight required fields present and (2) its dependency graph is acyclic. Critique the rule and propose a better one with at least five conditions.

**Points:** 5

**Rubric (1 point each):**

1. Critiques the rule: both checks are structural, so they say nothing about meaning, safety, evidence or authority.
2. Adds a condition for cross-field semantic review of the plan, for example objective against verification.
3. Adds evidence conditions and failure routes on state-changing handoffs.
4. Adds a stop field with completion, halt and defer exits, each with an owner, and at least one counterexample the plan is shown to reject.
5. Adds approval by a named person with a date, fixing the version that runs, and reopening the plan if a result contradicts it.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.57

Two teams propose AI-assisted pipelines for screening job applications. Team 1 documents each stage's output and the condition under which each handoff may occur. Team 2 writes only "a recruiter reviews the AI's shortlist." Compare the two proposals, explain why the first can be reviewed and the second cannot, and explain what a clear map does not show.

**Points:** 5

**Rubric (1 point each):**

1. Says Team 1's proposal can be reviewed on its substance because stated handoffs can be examined and disputed.
2. Says Team 2's proposal cannot be assessed because "reviews" has no criterion and nobody can say what the recruiter checks.
3. Explains that delegation is a contract and not merely a division of labor, and that its handoff conditions must be testable.
4. Explains that a clear map does not show that the decisions inside it are good, since criteria and bias still need examination.
5. Suggests improving Team 2's proposal by stating what the recruiter checks, a sampling audit, a failure route and a named owner.

**Source:** Evidence belongs on the edges

## ES-ch10.58

An AI assistant proposed the following plan for a coding agent:

```text
objective: Improve test coverage
inputs: the repo
scope: the repository
steps: write (after run), run (after write), report (no prerequisites)
tools: shell with full filesystem access
risks: bugs
verification: tests pass
stop: when coverage is good
approved_by: assistant
```

Review it. Identify at least five distinct problems, say which could be caught by a structural check and which only by semantic review, and state what you would require before approval.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the cycle between write and run, and says a dependency check catches it, while a field-presence check does not, because every field is nonempty.
2. Identifies that the objective has no measurable target and that "tests pass" does not verify coverage, which is a semantic mismatch.
3. Identifies that the scope and tools are too broad for the steps and carry no permitted operations or exclusions.
4. Identifies that the stop condition is not observable, the risks are vague, and report lacks a declared dependency on the work it reports.
5. Identifies that "approved_by: assistant" is not a valid approval, and requires revision, review and approval by a named person before anything runs.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.59

A colleague argues: "Our planner agent produces plans that pass a field-presence check and a dependency-ordering check every time, so we can execute them automatically." Write a response.

**Points:** 5

**Rubric (1 point each):**

1. Explains that both checks are structural and narrow, and a plan can be useless or unsafe and still pass.
2. Names what they do not test: meaning, authority, evidence quality and safety of the actions.
3. Proposes additional layers: semantic and cross-field review, counterexamples, and runtime permission boundaries for state-changing actions.
4. Says consequential actions need approval by a named person, while automation may be reasonable for low-risk reversible actions with bounds.
5. Proposes measuring plan quality, for example by auditing samples, tracking the rate at which reviewers reject passing plans, and comparing outcomes, and reporting the structural pass rate under its true name.

**Source:** The gate: a reviewed plan, before Claude implements

## ES-ch10.60

Design a plan-review process for a team that uses a coding agent for routine bug fixes in a version-controlled repository. Specify what the engineer writes before the agent starts, what the agent may draft, what automated checks run, what a reviewer examines, who approves, what the agent may do without approval, and when work stops or the plan reopens.

**Points:** 5

**Rubric (1 point each):**

1. Has the engineer write the objective, scope boundary and acceptance tests before the agent starts, so the key decisions are not left to the agent.
2. Lets the agent draft steps, the tools list and candidate counterexamples, and runs automated structural and ordering checks on the plan.
3. Has a reviewer perform cross-field and counterexample review and confirm evidence conditions and failure routes on state-changing handoffs.
4. Requires a named approver with a date, and limits the agent without approval to reversible, in-scope actions, with runtime permissions guarding destructive or out-of-scope operations.
5. Defines completion, halt and defer exits with owners, and reopens the plan, recording the version and reason, whenever a result contradicts it.

**Source:** The gate: a reviewed plan, before Claude implements
