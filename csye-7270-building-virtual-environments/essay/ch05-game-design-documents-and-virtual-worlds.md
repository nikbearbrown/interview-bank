# Chapter 5: Game design documents and virtual worlds

## ES-ch05.1

A designer hands a coding agent this requirement: "The checkpoint should feel responsive and reset the player quickly." Explain why a stranger could not test it, then rewrite it as acceptance criteria that a person who has never met the designer could turn into tests. Your criteria must show how you handle quantities, tolerances, time, how each state is reached, and what must not change.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the untestable words ("feel responsive", "quickly") and explains that they are judgements without a quantity, so two testers could disagree about pass or fail.
2. Names quantities with units and a tolerance, for example a respawn position within 0.2 m or 8 px of a named marker.
3. Gives time as a stated limit with a stated basis, for example within 2 physics ticks, 120 frames at a stated fixed rate, or 0.5 seconds at a stated tick rate (a game-clock basis is one example), not "quickly".
4. States how each state is reached: by real input actions or by a clearly labelled direct write of game state.
5. Lists what must not change, such as existing behaviour and the existing tests, which must still pass.

**Source:** Acceptance criteria

## ES-ch05.2

A developer writes this instruction to a coding agent: "Create a boolean called shielded and a Timer node called ShieldTimer set to 3.0 seconds, and connect the pickup's area_entered signal in code." The designer actually cares that the player is protected for three seconds after collecting a pickup. Distinguish a specification from an implementation, explain what is wrong with the instruction as written, and rewrite it as a specification that is measurable and covers at least one edge case. Say when an implementation constraint is legitimate.

**Points:** 5

**Rubric (1 point each):**

1. Defines a specification as the observable behaviour that must hold, and an implementation as the mechanism chosen to achieve it (nodes, variables, signals).
2. Explains what is wrong: the instruction fixes names and mechanisms but never states the behaviour the designer wants, so a build that follows it can still be wrong, and a test cannot be written from it.
3. Rewrites as behaviour: after collecting a pickup, enemy contact deals no damage for 3.0 s, and after 3.0 s contact damages again.
4. Makes the 3.0 s measurable (a tolerance or a tick count) and states an explicit rule for at least one edge case, such as a second pickup during the window (restart, extend or ignore are all acceptable if stated) or expiry while an enemy overlaps.
5. Names a legitimate implementation constraint, such as an architectural rule the project already follows, a file the agent may edit, or something that must not change, and says these belong beside the behaviour, not in place of it.

**Source:** Spec versus implementation

## ES-ch05.3

A studio pitches a 2D stealth puzzle game with thirty levels. Define a prototype, a vertical slice and a minimum viable product (MVP), say what each would contain for this game, and say what question each build is meant to answer. Then explain how confusing them leads to scope problems.

**Points:** 5

**Rubric (1 point each):**

1. Defines a prototype as a quick build that tests one design question, with placeholder art, which may be thrown away.
2. Defines a vertical slice as a thin portion of the game built to near-final quality across art, audio, UI and mechanics, to show the whole game can reach that standard.
3. Defines an MVP as the smallest complete game that can be released and tested with real players, containing only the features it needs.
4. Applies each build to the stealth game with concrete content (for example: one room with a guard and hiding; one finished level with final art and sound; a handful of levels with menus and saving) and states the question each answers (is it fun, can we build the whole to this standard, will players want it); full point for content and a question for all three builds, half a point if two of the three are covered.
5. Explains a scope problem from confusion, such as polishing a prototype, treating the slice as the product, or adding roadmap features to the MVP, which grows scope and delays learning.

**Source:** Prototype, vertical slice and MVP

## ES-ch05.4

Three weeks before a deadline, a team's design pillars are "tight controls", "readable levels" and "short sessions", and its scope list has twelve levels. Teammates propose online leaderboards, a branching story with cutscenes, and procedurally generated levels. Explain scope and scope creep, show how pillars and an out-of-scope list help the team decide, and describe the options and records a good lead would use.

**Points:** 5

**Rubric (1 point each):**

1. Defines scope as the commitment of features and content for a date, and scope creep as growth of that commitment without matching changes in time or resources.
2. Uses the pillars as filters, giving a verdict for each of the three proposals and arguing it from a pillar (for example the branching story with cutscenes conflicts with "short sessions" and the generated levels risk "readable levels"); any verdict is accepted if it is argued from a pillar or from cost.
3. Names the levers available: cut, defer, swap one feature for another of equal cost, or move the date, and explains that accepting without trade is creep.
4. Explains that an out-of-scope list records decisions already made so they are not re-argued, and that each proposal gets an estimate of cost before a decision.
5. Describes recording the decision and reason, so that a rejected idea becomes a post-release candidate rather than a lost argument.

**Source:** Scope creep and pillars

## ES-ch05.5

A designer wants a stealth meter that fills while an enemy can see the player. Using mechanics, dynamics and aesthetics, trace what the designer builds and what emerges, explain why the designer cannot set the aesthetic directly, and show how to turn the mechanic into a precise requirement a coding agent can build and a test can check.

**Points:** 5

**Rubric (1 point each):**

1. Defines mechanics as rules and systems the designer builds, dynamics as behaviour that emerges when players use them, and aesthetics as the emotional responses of players.
2. Identifies the meter and its fill rule as the mechanic, and gives plausible dynamics such as players hugging cover, waiting for patrol gaps, or rushing between blind spots.
3. Identifies aesthetics such as tension and the satisfaction of slipping past, and explains why the designer cannot set them directly: they are the players' own responses, so the designer can only shape the rules that tend to produce them.
4. Explains that a playtest is needed to find which dynamics and feelings a rule produces, because they cannot be read from the rule.
5. Writes the mechanic as numbers and observable results, such as fill rate per second while seen, decay rate when unseen, the threshold at which enemies attack, and a test that checks these values.

**Source:** Mechanics, dynamics and aesthetics

## ES-ch05.6

A coding agent reports that a new level is finished and all its tests pass. Explain what passing automated tests can and cannot establish about the level, what a playtest can show that a test cannot, and design a verification plan with three automated criteria and two playtest questions. Include one way to check that the tests would actually fail if the level were broken.

**Points:** 5

**Rubric (1 point each):**

1. States that passing tests establish only the specific conditions they check, such as reachability, counts or timings, and not whether the level is fun, readable or fair.
2. Explains that a playtest with real players can show whether they understand what to do, notice cues and enjoy the level, which no automated test decides.
3. Gives three testable automated criteria with quantities, tolerances or time boxes, for example that the exit is reachable by ordinary input within a set number of frames and that the hazard count and positions match the specification.
4. Gives two playtest questions, such as where players hesitate or fail repeatedly, and whether they can say what the goal was without being told.
5. Describes a way to check the tests are meaningful, such as breaking the level on purpose (blocking the exit or changing a value) and confirming that the test fails.

**Source:** Playtest versus automated test
