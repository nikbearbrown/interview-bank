# Chapter 11: Animation and interaction

## ES-ch11.1

A teammate tracks a character's animation with four boolean flags (is_jumping, is_attacking, is_crouching, is_hurt) and a long chain of nested if statements. Explain what a state machine is (states, transitions and conditions) and why replacing the flags with one is useful. Cover how it changes reasoning, bugs and testing, using the four-flag example.

**Points:** 5

**Rubric (1 point each):**

1. Defines a state machine as a set of named states with exactly one current state at a time, transitions that are the allowed routes between states, and conditions or parameters that decide when a transition fires.
2. Shows the flag problem with numbers: four independent booleans give 2^4 = 16 combinations, many of them meaningless (for example jumping, crouching and hurt together), whereas a state machine has only the states that were designed.
3. Explains that transitions are explicit, so what can follow what is written down and unlisted routes cannot happen, which is easier to reason about than a web of nested conditions.
4. Explains that bugs become visible: the current state is a single named value that can be logged or shown, so a stuck state or a wrong transition can be seen.
5. Explains testing: states and transitions can be enumerated, so each allowed transition (and the absence of forbidden ones) can be exercised, and a missing exit can be found by inspection.

**Source:** State machines versus nested conditionals

## ES-ch11.2

A developer tells a coding agent: 'make the character animate when it moves'. The project has idle, walk, run and jump clips. Explain what the instruction leaves open and what the agent could get wrong. Then rewrite it as a precise specification of a state machine.

**Points:** 5

**Rubric (1 point each):**

1. Identifies open questions about the conditions: what counts as moving (a speed threshold), the speed at which walk becomes run, and whether airborne movement counts.
2. Identifies open questions about the structure: which states exist, which transitions exist between them, and what happens to states not mentioned (for example jump and fall).
3. Identifies open questions about presentation: cross-fade or cut, the length of the cross-fade, whether each clip loops or plays once, and interrupt behaviour.
4. Writes a precise specification in the form of rows, each giving from-state, to-state, condition (with numbers), cross-fade time and whether it may interrupt, and says that unlisted transitions must not exist.
5. Names plausible wrong builds from the vague version, such as flicker between walk and run around one speed, a landing that plays the idle pose in mid-air, or clips that never loop.

**Source:** Say it to the agent: specifying a state machine

## ES-ch11.3

A character needs these behaviours: it walks, jogs or sprints according to how far the stick is pushed; it jumps and falls; and it swings a sword that cannot be interrupted by movement. Explain how the words 'state machine', 'blend space', 'blend tree' and 'animation tree' relate, then design which behaviours should be states and which should be blends, and say how you would describe the design to a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines a state machine as a graph in which one state is active at a time and transitions move between states, and a blend tree as a graph of nodes that mixes clips according to parameters.
2. Defines a blend space as mixing clips by a continuous position on one or two axes, and explains that an animation tree is the whole graph that plays clips through such nodes (called an Animator Controller in Unity or an Animation Blueprint in Unreal; any equivalent name is accepted), in which these parts can be nested (for example a state that holds a blend), so a state machine is one part of it and not a synonym for all of it.
3. Assigns walk, jog and sprint to a blend driven by a speed parameter, because speed varies continuously and the result should change smoothly.
4. Assigns jump, fall and the sword swing to states with defined transitions, because they are committed actions with their own entry, exit and interruption rules (the swing having no transition from movement input).
5. Describes the design to an agent precisely, naming the states, the parameter that drives the blend and its range, the transitions with conditions, and the nesting (for example a ground state containing the speed blend).

**Source:** Animation tree, state machine, blend tree and blend space

## ES-ch11.4

A game runs physics at 120 ticks per second and updates its animation graph at 60 frames per second. With the jump key held, the character lands on one tick and jumps again on the next, and the animation graph stays in its 'fall' state while the character rises. Explain why this happens and why it happens only sometimes. Describe two fixes and a test that would catch it reliably.

**Points:** 5

**Rubric (1 point each):**

1. Explains the sampling mismatch: 120 / 60 = 2 physics ticks per graph update, and the graph reads the floor condition only at its own update.
2. Explains that when the landing tick and the take-off tick fall inside one graph update, the graph never sees 'on floor', so it does not register the landing and stays in fall.
3. Explains why it is intermittent: it depends on which of the two ticks in a graph update the landing falls on, which depends on earlier timing.
4. Describes two fixes, such as a transition that reacts to rising while airborne, running the graph in the physics step, or pushing the state change from the movement code at the moment it happens.
5. Describes a test that drives real input (holding the jump key), checks the animation state against the physical state, and runs the sequence at both tick offsets so that the unlucky timing cannot be missed.

**Source:** Parameters, conditions and update timing

## ES-ch11.5

A developer tells a coding agent: 'when the player presses Space, switch to the jump state'. The character also has Hurt and Dead states. Explain what is wrong with driving the state from the key press, rewrite the instruction precisely, say what else could drive the jump state instead of the key press, and explain how interrupts and priority should be specified for hit reactions and death.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a press-only condition ignores whether the character can jump now, so jump may start while the character is stunned, airborne or dead.
2. Rewrites the transition with guards: Jump pressed, character on the floor and the current state allowing a jump.
3. Explains the alternative of driving animation from the physical state (leaving the floor with upward velocity) so that picture and movement agree even when the jump has another cause, such as a bounce pad.
4. Explains how to specify interrupts: Hurt can interrupt Attack by an explicit transition, Dead overrides every state (for example by a transition from any state or a rule evaluated first), and a missing transition forbids an interruption.
5. Explains that when several transitions are valid at the same moment the order or priority must be stated, since otherwise the engine or the agent chooses.

**Source:** Input-driven change, interrupts and priority

## ES-ch11.6

Describe three edge cases that commonly break a character's animation state machine: a stuck state, an impossible (missing) transition, and rapid input. For each, give the symptom a player sees, the likely cause, a fix, and a way to test for it.

**Points:** 5

**Rubric (1 point each):**

1. Describes the stuck state: the symptom is a character frozen in a pose, and the cause is a state whose exit condition never becomes true (for example a flag nobody sets).
2. Describes the impossible transition: the symptom depends on the engine and call (the request is ignored, the state is forced directly, or the recorded state and the picture disagree), and the cause is a requested change that has no defined route.
3. Describes rapid input: the symptom is that repeated presses restart the action, stack up or are lost, and the cause is that no rule says what a press during the action should do.
4. Gives a fix for each case, stated precisely enough to instruct an agent: an exit tied to the clip end or to a condition the code really sets; a decision on whether the transition should exist, then adding or forbidding it explicitly; and a deliberately chosen policy for presses (ignore during the action, restart, or remember one press with a buffer).
5. Describes tests that use real input and check the state: log the current state over time, check that every state except a deliberate end state has an exit, and replay fast presses and check the result.

**Source:** Edge cases: stuck state, impossible transition, rapid input

## ES-ch11.7

Define input buffering, cooldown and coyote time, and explain how each differs from the others. A game uses a 0.15 s input buffer, the next attack becomes available at t = 0.50 s, and the player presses Attack at t = 0.30 s, 0.40 s and 0.52 s. Treat each press separately, as if the other two had not happened, and say what happens at each press. Then explain the trade-off in choosing the buffer length.

**Points:** 5

**Rubric (1 point each):**

1. Defines input buffering as remembering a press made slightly too early so it is used when the action becomes available, and cooldown as a minimum time between uses of an action.
2. Defines coyote time as a brief grace period after leaving the ground in which a jump is still accepted, and distinguishes it from buffering (forgiving late input versus early input) and from cooldown (restricting repeated use).
3. Works out the press at 0.30 s: it expires at 0.45 s, before 0.50 s, so it is lost.
4. Works out the presses at 0.40 s and 0.52 s, each taken on its own: 0.40 s is remembered until 0.55 s and starts the attack at 0.50 s, and 0.52 s starts an attack immediately because it is already available.
5. Explains the trade-off: too short a buffer drops presses and feels unresponsive, while too long a buffer queues unintended actions and feels sluggish or random, so the length is a design choice that should be stated in the instruction.

**Source:** Input buffering, cooldown and coyote time

## ES-ch11.8

A melee attack clip has startup, active and recovery phases. Explain how animation events (or property tracks) should control the attacker's hitbox, and how the enemy's hurtbox fits in. Cover damaging an enemy only once per swing, what must happen if the attack is interrupted in the middle of its active phase, and what you would tell a coding agent to build.

**Points:** 5

**Rubric (1 point each):**

1. Defines a hitbox as the attacker's damaging region and a hurtbox as the defender's vulnerable region, both normally detection shapes, with layers or masks keeping a character from hurting itself.
2. Explains that the hitbox is enabled only during the active phase, switched on and off by events or a property track in the clip, so its timing follows the animation and playback speed.
3. Explains that without a record of targets already hit, a hitbox that overlaps for several updates damages the same enemy repeatedly, so each swing keeps a list of enemies it has hit.
4. Explains that if the attack is interrupted before the 'off' event, the event never fires, so leaving or interrupting the state must also turn the hitbox off.
5. Writes an instruction naming the clip, the active window (frames or times), the hitbox and hurtbox roles and layers, the once-per-swing rule and the cleanup on interrupt.

**Source:** Hitbox and hurtbox timing with animation events

## ES-ch11.9

A project already has a gameplay state machine in code. A coding agent is asked to 'add an animation state machine' and builds a second, separate machine that tracks its own states from the player's input. Explain what can go wrong, how you would instruct the agent instead, how you would test the result, and what that test cannot tell you.

**Points:** 5

**Rubric (1 point each):**

1. Explains that two machines with their own rules and timing can disagree, so the picture shows one state while gameplay is in another.
2. Explains the single-source-of-truth design: gameplay state is the authority, and the animation machine reads it through parameters or events and does not decide gameplay outcomes such as damage.
3. Writes the instruction precisely, naming the existing states, the parameter or signal that carries each, which transitions the animation machine has, and a rule that it must not read raw input.
4. Describes a test that drives real input, compares the animation state with the gameplay state over time, and checks forbidden transitions.
5. Names what such a test does not establish, namely whether the motion looks and feels right, which still needs a person to play and judge.

**Source:** Single source of truth for character state
