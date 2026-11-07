# Chapter 5: Game design documents and virtual worlds

## MA-ch05.1

A team is deciding what to write down before building a 2D platformer. Check each statement about a game design document (GDD) that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A GDD should contain the source code of each mechanic, so the document and the game cannot disagree.
- [ ] B. A GDD is written once before production and then frozen, so design disagreements are settled for the whole project.
- [ ] C. If a newer GDD exists, it shows that the build in the repository already behaves as the document says.
- [ ] D. A GDD records what the game is and how it should behave, in enough detail for builders and testers to work from.
- [ ] E. A short pitch or brief states the core idea and scope; a GDD develops those decisions in detail.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: A GDD describes intended behaviour in words, tables and numbers; code is the implementation.
- B: Designs change after prototypes and playtests, and a GDD that is never revised becomes a stale artifact.
- C: A document is a promise; only running the build against the stated criteria shows it is kept.
- D: That is its purpose: a shared description that engineers and testers can act on.
- E: The brief is the compact form, and the GDD is the detailed one.

**Source:** What a GDD is

## MA-ch05.2

A team's design pillars are "fast restarts", "readable danger" and "one-button depth". Late in development someone proposes a 30-second unskippable cutscene after every death. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Make the game fun" is a strong pillar, because nobody on the team can disagree with it and it fits the whole feature list.
- [ ] B. "Enemies flash 0.4 s before an attack lands" is closer to a requirement than a pillar, because a test can check it.
- [ ] C. Design pillars are a few short statements of the experience the game must deliver, used to judge proposed features.
- [ ] D. Pillars should list the planned features in the game so that nothing is forgotten when decisions are made.
- [ ] E. The cutscene conflicts with "fast restarts", so the pillars give the team a reason to reject or change it.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A pillar that excludes nothing cannot settle any decision.
- B: Pillars guide judgement; requirements give numbers that a test can check.
- C: Pillars are a decision tool for keeping features consistent with the intended experience.
- D: A feature list is separate; pillars are few and about the experience.
- E: A proposal that works against a pillar needs a very good reason.

**Source:** Design pillars

## MA-ch05.3

In a roguelike the player enters a room, fights the enemies, picks up a reward and enters the next room. When a run ends, the player spends earned currency on permanent upgrades and starts a new run. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The core loop is the engine's update loop, the code that runs once per frame to read input and draw.
- [ ] B. In a core loop, a verb is anything the game does to the player, such as spawning an enemy or starting a timer.
- [ ] C. The core loop is the short cycle of actions the player repeats most often, here entering, fighting and collecting.
- [ ] D. Spending currency between runs belongs to a longer meta or progression loop wrapped around the core loop.
- [ ] E. The core loop is the list of all the game's features, grouped by importance and by the team that builds each.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: That is the programming game loop; the design term is about what the player repeats.
- B: A verb is an action the player chooses to perform.
- C: It is the moment-to-moment cycle that the rest of the game is built around.
- D: Loops nest: short ones inside, longer ones around them.
- E: A feature list is not a loop; a loop is a repeated cycle of player actions and feedback.

**Source:** Core loop

## MA-ch05.4

The MDA framework separates mechanics (the rules and systems the designer builds), dynamics (behaviour that emerges when players use those rules) and aesthetics (the emotional responses players have). A designer adds a rule to a shooter: the player carries at most 12 rounds and cannot pick up more than one magazine per room. Players start avoiding fights and hoarding rounds, and report feeling tense. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Avoiding fights and hoarding rounds is a dynamic: it emerges from play and is not a line in the rules.
- [ ] B. The designer can set the aesthetic directly by writing "tense" into the rules, as the designer sets the magazine limit.
- [ ] C. A playtest is how the designer finds out which dynamics and feelings a rule actually produces, because they cannot be read off the rule text.
- [ ] D. The 12-round limit is a mechanic.
- [ ] E. Tension is an aesthetic, the emotional response that the rules and the play produce.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Dynamics arise from rules meeting player choices.
- B: Aesthetics are responses of players; the designer can only shape the rules that tend to produce them.
- C: Dynamics and aesthetics emerge only when players meet the rules, so they have to be observed in play.
- D: It is a rule the designer wrote.
- E: Aesthetics are the felt experience.

**Source:** Mechanics, dynamics and aesthetics

## MA-ch05.5

Two requirements arrive for the same game. One says: "The player can interact with the world." The other says: "The player can jump, dash and grapple." A player verb is an action the player can choose to perform. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Health regeneration is a player verb because it happens often during play and affects the outcome.
- [ ] B. "Interact with the world" is too vague to build from, since it names no input, no target and no change of state.
- [ ] C. Each listed verb still needs an input, a rule for what changes, and feedback the player can perceive.
- [ ] D. Jump, dash and grapple are player verbs because the player chooses when to do each.
- [ ] E. A game's verbs are fixed by its genre, so choosing them is not a design decision for the team.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The player does not choose it; it is a system rule.
- B: An agent cannot tell what to implement from it.
- C: A verb becomes buildable when input, effect and feedback are stated.
- D: Verbs are chosen actions.
- E: Choosing and limiting verbs is a central design choice.

**Source:** Player verbs

## MA-ch05.6

A team plans three builds: a weekend prototype of the core mechanic with placeholder boxes, a vertical slice, and a minimum viable product (MVP). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A prototype exists to answer a design question, such as whether the mechanic is fun, and may be thrown away.
- [ ] B. A vertical slice is a rough, whole-game version in which the full set of levels exists but none is polished.
- [ ] C. A prototype is only valid if it uses final art and audio, since otherwise players cannot judge it.
- [ ] D. An MVP contains the whole feature roadmap, built at its first usable quality, so nothing planned is left out.
- [ ] E. An MVP is the prototype with a nicer menu and some sound added to it.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Prototypes are tools for learning, not products.
- B: That describes a horizontal pass; a vertical slice is a thin portion built to near-final quality across art, audio, UI and rules.
- C: Placeholder art is normal for a prototype; the question is about the mechanic.
- D: Minimum means only what the game needs to be releasable and to teach the team from players.
- E: An MVP is a complete, releasable game with the minimum feature set, not a polished prototype.

**Source:** Prototype, vertical slice and MVP

## MA-ch05.7

Four weeks before a deadline, a team has one working level. A teammate proposes online co-op, a crafting system and ten new enemy types. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Scope is what a team commits to deliver by a date, and cutting a feature is a legitimate way to protect the date.
- [ ] B. An out-of-scope list records decided non-goals, which makes such proposals easier to decline.
- [ ] C. Scope creep means any change to the design made after a prototype exists, whether or not it affects the deadline.
- [ ] D. A feature should be accepted whenever it would improve the game; cost and schedule do not enter the decision.
- [ ] E. Scope creep is harmless when each added feature is small, because small features cost no schedule time.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Scope, schedule and quality trade against each other, and cutting is one of the levers.
- B: A written non-goal turns a repeated argument into a settled decision.
- C: Scope creep is uncontrolled growth of the commitment without matching changes to time or resources.
- D: Scope decisions weigh the benefit against cost and the date.
- E: Many small additions add up, and each needs design, building and testing.

**Source:** Scope and scope creep

## MA-ch05.8

A game studio has a level designer and a worldbuilder. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A level can be well designed with almost no worldbuilding, as in an abstract puzzle room.
- [ ] B. Worldbuilding is the same as level design done at a larger scale, so a map of the world is a level.
- [ ] C. Worldbuilding establishes the setting (places, history, rules, cultures) and can inform levels without being a layout.
- [ ] D. Worldbuilding is finished when the tile layout of the first level is drawn and the map is approved.
- [ ] E. Level design arranges space, obstacles, enemies and pacing so that the player's verbs are tested in sequence.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Level quality depends on verbs, pacing and teaching, not on lore.
- B: A world map describes the setting; a level is a playable arrangement.
- C: Setting and layout are different jobs that influence each other.
- D: A tile layout is level work; the setting can still be undefined.
- E: It is the design of playable spaces.

**Source:** Level design versus worldbuilding

## MA-ch05.9

A designer gives a coding agent this requirement for a 2D platformer with 32 px tiles: "The jump should feel snappy and reach a good height." The intent is that a jump from the floor rises 96 px (3 tiles) at its highest point. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The criterion should state the starting situation, such as the player standing on the floor, because the same jump input gives a different result from the air.
- [ ] B. A testable version names a quantity and unit: the highest point is 96 px above the starting height.
- [ ] C. Adding "and the jump should be fun" makes the criterion more testable, because it states the designer's goal and gives the agent something to aim for.
- [ ] D. A tolerance such as 4 px is needed, since physics steps are discrete and the apex seldom lands on exactly 96 px.
- [ ] E. "Snappy" and "a good height" cannot be checked by a stranger, so they are not acceptance criteria.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A test needs a defined starting state; without it, two testers can set up different situations and disagree about pass or fail.
- B: Quantity and unit remove guessing.
- C: It adds a judgement that no automated test can decide.
- D: A tolerance defines what counts as a pass.
- E: A stranger cannot write a pass or fail test from them.

**Source:** Acceptance criteria

## MA-ch05.10

A team writes acceptance criteria in the form "given a starting situation, when an action happens, then an observable result follows". Check each statement that is true, where a statement counts as true when it is a criterion that a stranger could turn into a pass or fail test without asking the designer anything. Each statement is worth 1 point (5 points total).

- [ ] A. Enemies should be hard but fair, so that players feel challenged without feeling cheated, with each attack telegraphed clearly enough to dodge.
- [ ] B. Given 3 health, when the player first touches a spike, then health becomes 2 and spike contact is ignored for 1.0 s.
- [ ] C. The game should handle damage well, giving the player a fair and satisfying response when they are hit.
- [ ] D. Given the player is on the floor, when the player presses jump, then within 0.1 s the player is moving upward.
- [ ] E. The menu opens quickly and looks good on the screen sizes the game supports, including very small ones.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Hard and fair are opinions that need playtesting.
- B: It names the starting state, the trigger, exact results and a duration.
- C: "Well" is a judgement with no observable result.
- D: It states the situation, the action, an observable result and a time limit.
- E: "Quickly" and "good" are not measurable as written.

**Source:** Given-when-then criteria

## MA-ch05.11

Two instructions are written for the same shield pickup. Instruction X: "Add a Timer node named ShieldTimer set to 3.0 s, store the state in a boolean called shielded, and connect area_entered in code." Instruction Y: "After the player touches a shield pickup, enemy contact deals no damage for 3.0 s; touching a second pickup restarts the 3.0 s; once 3.0 s have passed, enemy contact deals damage again." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because Y states behaviour, a test can check it without knowing which node or variable the agent used.
- [ ] B. Y is a behavioural specification (what must be true) and X is implementation detail (how it is built).
- [ ] C. Reading the code is enough to recover what the designer intended, because the code is the final design.
- [ ] D. A specification should name node types and variable names so that the agent has no freedom.
- [ ] E. If the implementation is later rewritten, a behavioural test written from Y should still apply.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Behaviour is observable regardless of the internals.
- B: A spec states observable behaviour; implementation names the mechanism.
- C: Code shows what the game does, not what it was meant to do.
- D: Naming the mechanism ties the work to one design and hides the behaviour that matters.
- E: Tests tied to behaviour survive refactoring.

**Source:** Spec versus implementation

## MA-ch05.12

A coding agent reports: "Shield pickup finished; all tests pass." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An automated test checks specific conditions, such as the shield lasting 180 physics ticks, and can be rerun.
- [ ] B. A playtest can replace automated tests, because people notice the errors a test would find, even rare ones.
- [ ] C. Shortening the shield to 0.5 s on purpose and watching the test fail checks that the test measures what it claims.
- [ ] D. A passing automated test shows the feature is fun, since the test was written from the design and covers the whole feature.
- [ ] E. A playtest can reveal whether players notice the shield, understand it and enjoy it; a test cannot.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Repeatable, exact checks are what automation offers.
- B: People miss rare, exact-timing cases that scripted tests catch.
- C: A test that still passes on a broken build is not measuring the feature.
- D: A test checks stated conditions, not enjoyment.
- E: Comprehension and enjoyment need people.

**Source:** Playtest versus automated test

## MA-ch05.13

A designer writes to a coding agent: "Make the boss hard." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Hard" is a judgement, not a build instruction; it must become parameters and be confirmed by playtesting.
- [ ] B. Multiplying the boss's health by ten is the obvious reading of "hard", so the agent can proceed without asking.
- [ ] C. Once the numbers are written down, an automated threshold test can show whether the boss is hard enough for players.
- [ ] D. "Attack interval 1.2 s, damage 2 of 5 hearts, 0.4 s wind-up" is a requirement that a test can check.
- [ ] E. Adjectives like "hard" belong in the acceptance criteria because the team will understand them.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Parameters can be built and tested; the judgement is confirmed with players.
- B: Hard could mean fast, accurate, numerous or punishing; health alone may only make the fight longer.
- C: A test can confirm the numbers; only players can say whether the result is hard enough.
- D: It gives quantities and times a test can read.
- E: Shared understanding is not a stranger-testable criterion.

**Source:** Vague requirement, say it to the agent

## MA-ch05.14

A designer's requirement for a checkpoint reads: "When the player reaches the checkpoint flag, dying should send them back there." The developer wants an agent to build it and a test to check it, so the precise instruction given to the agent covers the behaviour, the test and the limits on the change. Check each statement that is true about details that instruction should add. Each statement is worth 1 point (5 points total).

- [ ] A. What happens if the player re-enters the flag after it has activated can be left out, because the sentence already defines the behaviour.
- [ ] B. How the test puts the game into each state it checks, such as playing through with real input or setting the state directly, because a shortcut skips part of the path a player would take.
- [ ] C. What must not change, such as existing movement behaviour and the existing tests, which must still pass.
- [ ] D. What counts as reaching the flag: for example, the player's body entering a trigger region of a stated size, activating once.
- [ ] E. Where "back there" is, with a unit and a tolerance, such as within 8 px of a named respawn marker.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Repeat entry is a common edge case that an unstated rule leaves to chance.
- B: Playing through proves the whole path works; setting state directly proves only the step being checked, so the route should be stated.
- C: Invariants protect behaviour the change should not touch.
- D: "Reaches" has to become an observable event.
- E: A location without a tolerance cannot be tested.

**Source:** Writing a precise requirement

## MA-ch05.15

A developer instructs a coding agent: "Add a double jump. Do not change run speed, gravity or the camera. Edit only player.gd and a new test file. If a criterion cannot be met, stop and report which one instead of loosening it." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Stop and report instead of loosening" guards against the agent making a criterion or a test weaker so that it passes.
- [ ] B. Naming the files the agent may edit limits the change to a surface that a reviewer can read in full.
- [ ] C. "Do not change run speed, gravity or the camera" states invariants: things that must stay true after the change.
- [ ] D. Invariants make a requirement untestable, because they add conditions beyond the feature itself, which a test cannot cover.
- [ ] E. These constraints are implementation detail and belong in code comments, not in the instruction, because the agent reads the code anyway.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It closes the easy route to a false pass.
- B: A small change surface is easier to review.
- C: Invariants fence off existing behaviour.
- D: They make it more testable, since existing behaviour can be re-checked.
- E: They are requirements on the work and must be in the instruction to bind the agent.

**Source:** Invariants and scope of an instruction

## MA-ch05.16

A team on a desktop computer scopes a touch version and a networked version of its game. It has no phone and no second machine. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A feature that cannot be verified on the available hardware should be deleted from the design document.
- [ ] B. Mouse-emulated touch can show that the game responds to touch events, but not that the game feels right on a phone's screen.
- [ ] C. A desktop simulator of a headset is enough to prove that the movement is comfortable in virtual reality.
- [ ] D. Two copies of the game on one computer, talking over the loopback address, show that the game works over the internet with packet loss.
- [ ] E. The scoping note should describe both versions as working, since the code for them exists.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: It should stay, marked as unverified, so the gap is visible.
- B: An emulation tests event handling, not real hands and screen.
- C: Comfort depends on the real device and the person wearing it.
- D: Loopback has no real network distance, loss or latency.
- E: Code existing is not evidence of working on the target.

**Source:** Scoping platforms honestly
