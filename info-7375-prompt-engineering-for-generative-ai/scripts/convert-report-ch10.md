# Conversion report: ch10-planning-before-acting (MA-ch10)

- Old MA: 65. Old essays: 61. New MA: 36 (true-counts: 4 one, 12 two, 13 three, 7 four).
- Dropped/merged MA: 29 (the Python truthiness/missing_fields items MA-ch10.1-7 merged into 3; the ordering-function code and topological-order items MA-ch10.26-38 merged into 5; handoff, stop, risk, sign-off near-duplicates merged; code-trivia items such as MA-ch10.29, .62 dropped as non-vocabulary).
- Essays converted: folded into the MA content above wherever the skill is a term contrast (structural completeness vs semantic review, claim vs evidence, scope vs tools, halt vs defer, workflow vs agent, error of the third kind, primary generator, acyclic vs executable, approval gate vs permission).
- Essays NOT CONVERTED: those that are pure procedure or design opinion (writing a full plan for a named scenario, designing a pipeline's handoff document, ranking a team's checklist) and calculation-style ordering/trace essays; not itemised id by id (ES-ch10.1-61 reviewed as a group).

## Terms especially tested (planning before acting)

plan fields (objective, inputs, scope, steps, tools, risks, verification, stop) :: the eight questions a plan answers: aim, starting material, what may change, ordered actions, permitted capabilities, ways to fail, evidence of success, exits
structural completeness :: every plan field is present and nonempty; says nothing about meaning
semantic review :: judging whether field contents are meaningful, consistent and adequate
cross-field review :: comparing fields with one another to find contradictions (objective vs verification, steps vs scope, steps vs inputs)
truthy / falsy :: whether a value counts as true in a boolean test; empty list, 0 and None are falsy
schema validation :: checking form (parse, keys, types), not factual correctness
grounding :: support of a claim by a source
proxy :: a stand-in observation that does not measure the claim
scope :: boundary of what may change and what stays untouched
tools (field) :: capabilities the agent may call, and which operations stay under approval
completion / halt / defer :: the three stop exits: success condition met; stop because continuing crosses a boundary; pause and pass the decision to a named owner
turn limit vs finish action :: effort bound vs the agent's signal of completion
incomplete status :: honest report at a limit, partial artifacts preserved
refusal path :: workflow preserves state and reports what blocks the next transition
progress :: a change in the evidence or the decision state
prediction vs record :: plan states expected observations beforehand; result records what happened
proposal vs approval :: plan returned by a model vs an act by an accountable person
approval gate :: point where work waits for a person's decision
permission prompt :: asks whether one tool action may run
plan mode (Claude Code) :: read-only analysis that presents a plan for approval before edits
plan-and-execute vs adaptive loop :: full plan first, then run; vs choosing each action after the previous observation
workflow vs agent :: predefined code paths vs model-directed process and tool use
replanning :: revising a plan with a recorded reason when evidence contradicts an assumption
error of the third kind :: solving the wrong problem correctly (not Type I or Type II)
primary generator / anchor :: early, often unstated idea of what a problem is about that shapes visible solutions
formulation / candidate formulations :: the framing of the problem and the alternatives compared
salience criterion :: asks whether solving the problem addresses what matters
tractable :: easy to build or measure
precondition / postcondition / invariant :: what holds before a call / after it / throughout
dependency / prerequisite / edge :: a directed obligation between steps; the step that must come first; the arrow between them
topological order :: ordering in which each step follows all its prerequisites
ready batch :: steps whose declared prerequisites are done
hidden dependency :: shared resource or real need not declared in the graph
duplicate id / unknown prerequisite / dependency cycle :: three structural ordering errors
acyclic does not mean executable :: a loop-free graph can still omit a real dependency
testable condition :: one a stranger can apply by observation
claim vs evidence :: what the agent says vs what a reviewer can inspect (command, exit status, output, code version)
failure route :: planned next transition when an edge condition fails
counterexample :: a plan that meets a field's wording but fails its purpose
sign-off :: written record of what was checked, how, what was not checked, what is not claimed, and sign or withhold
