# Chapter 11: Animation and interaction

## MA-ch11.1

A developer describes a platformer character's behaviour as a state machine with the states Idle, Run, Jump and Fall. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A condition compares a parameter or game value with a flag or threshold, such as 'on floor is false' or 'speed is above 0.1'.
- [ ] B. At any moment the machine is in exactly one of those states (within one layer).
- [ ] C. Run and Jump can both be active at once, because each state is a separate on/off flag.
- [ ] D. Listing the four states creates the transitions between them, so no routes need to be defined.
- [ ] E. A transition is an allowed route from one state to another, usually guarded by a condition.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Conditions test parameters or values the game supplies, and a transition fires when its condition holds.
- B: A state machine has one current state at a time, which is what separates it from a set of independent flags.
- C: Independent on/off flags are the nested-conditional approach; a state machine allows one active state.
- D: Transitions must be defined; the existence of two states does not imply a route between them.
- E: Transitions are the explicit connections that say which state may follow which.

**Source:** State machine: states, transitions, conditions

## MA-ch11.2

A character script tracks its animation with four independent boolean flags (is_jumping, is_attacking, is_crouching, is_hurt) checked in a long chain of nested if statements. An alternative is a state machine with five states (Idle, Jump, Attack, Crouch, Hurt) and 11 explicitly listed transitions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The state machine removes the need for conditions, because each state decides on its own when to change.
- [ ] B. A stuck character is harder to spot in the state machine, because its state is hidden inside nested conditionals.
- [ ] C. Four flags can combine in 16 ways, including combinations such as jumping and hurt at once that nobody designed.
- [ ] D. At any moment the machine is in one of 5 named states, so a bug report can name the state.
- [ ] E. Because 11 transitions are listed, the state machine has 11 possible states for the character.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Transitions still need conditions or events that say when a change happens.
- B: With one explicit current state, a stuck state is visible by watching that value; hidden state is the nested-flag problem.
- C: Four booleans give 2^4 = 16 combinations, and many of them describe situations nobody designed.
- D: The state is a single named value that can be logged, shown and reported.
- E: The 5 states are the possible conditions of the character; the 11 transitions are the allowed moves between them.

**Source:** Why state machines beat nested conditionals

## MA-ch11.3

In Godot, the AnimationTree node plays animation clips that are stored in an AnimationPlayer, using a graph whose root can be a state machine, a blend tree or a blend space. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A state machine has no cross-fade of its own, so a smooth change from one clip to another needs a blend tree or blend space.
- [ ] B. A state machine in the tree mixes the clips of all its states by weight at all times, even with no transition.
- [ ] C. The AnimationTree node keeps its own copy of the clips it plays, independent of the AnimationPlayer.
- [ ] D. A blend space picks its output from a position on one or two axes, mixing the clips placed near that position.
- [ ] E. 'State machine' and 'blend tree' are two names for the same kind of graph in the animation tree.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: A transition between states can carry a cross-fade time, so a state machine can change smoothly from one clip to another; blend trees and blend spaces mix clips continuously by a parameter, which is a different job.
- B: A state machine plays its current state, and mixes in another only while a cross-fade between states is under way.
- C: The tree decides how much of each clip enters the final pose, but the clips live in the AnimationPlayer.
- D: A blend space places clips at points on a line or plane and mixes the neighbours of the current position.
- E: A state machine chooses among states; a blend tree is a graph of nodes that combine inputs by weight, and they are different nodes.

**Source:** Animation tree, state machine, blend tree and blend space

## MA-ch11.4

A character should walk, jog or sprint according to how far the stick is pushed, and should also commit to a jump once it has started, even if the player releases the button. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A speed axis between walk, jog and sprint clips suits a blend space, because speed varies continuously and smoothly.
- [ ] B. A blend space can enforce that a jump that has started cannot be interrupted by movement input, as it decides clip weights.
- [ ] C. A blend space needs a transition with its own condition between neighbouring clips on its axis, like a state machine.
- [ ] D. Making one state per tiny speed step (walk_1 to walk_20) is better than a blend, because states are more precise.
- [ ] E. A jump suits a state, because it is a committed action with its own entry, exit and duration.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A blend space maps a continuous number such as speed to a mix of neighbouring clips.
- B: A blend only decides how much of each clip to show; committing to an action is the job of states and transitions.
- C: Blend spaces mix by position and need no per-pair transitions.
- D: Twenty states would need many transitions and would still jump between steps; a blend gives smooth change with one parameter.
- E: A committed action is a state with defined ways in and out.

**Source:** Blend space versus state

## MA-ch11.5

In Unity's Animator Controller, transitions fire when conditions on Animator parameters are met, and a script sets those parameters. Parameters can be float, int, bool or trigger. A script keeps a bool 'isGrounded' updated every frame and sets a trigger 'Attack' when the attack button is pressed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Parameters are outputs of the state machine, written by the controller back to the script to tell it what to do next.
- [ ] B. A trigger is meant for one-time events: it is reset when a transition consumes it.
- [ ] C. A trigger that no transition consumes stays set until consumed or reset by the script, so it can fire a transition late.
- [ ] D. A float such as Speed suits a condition like 'Speed is greater than 0.1' and can also drive a blend tree.
- [ ] E. A bool keeps its value until the script changes it, so a transition conditioned on isGrounded stays satisfied while it is true.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Parameters are inputs written by the script, and the controller reads them to decide transitions.
- B: A trigger is a boolean that the controller resets once a transition has consumed it.
- C: Because the reset happens on consumption, an unused trigger waits, which is why stale triggers cause late or surprise transitions.
- D: Floats feed numeric comparisons and blend tree parameters.
- E: A bool is a level: it holds its value until it is changed.

**Source:** Parameters that drive transitions

## MA-ch11.6

A game runs physics at 120 ticks per second and updates its animation graph at 60 frames per second. A held jump key makes the character land on one physics tick and jump again on the very next tick. The graph's transition conditions read 'is the character on the floor' only when the graph updates. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the landing tick and the take-off tick fall inside the same graph update, the graph does not see 'on floor' as true, so it does not register the landing.
- [ ] B. The graph updates once per two physics ticks.
- [ ] C. One fix is a transition that also reacts to the character rising while airborne, so the graph recovers from a missed landing.
- [ ] D. Engines do not let the animation graph run in the physics step, because animation updates once per rendered frame.
- [ ] E. The physics engine is wrong in this situation, because it should not let a character land and jump within one frame.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A condition sampled only at graph updates can miss a state that changes and changes back between two samples.
- B: 120 / 60 = 2 physics ticks per graph update.
- C: A transition that depends on the airborne, rising state still fires even when the landing was never sampled.
- D: Engines let the animation update run in the physics step (for example by choosing the update or callback mode), which removes the mismatch.
- E: The physics is correct; the condition is sampled less often than the state changes.

**Source:** Sampling gap between physics and animation updates

## MA-ch11.7

While a character is stunned (a Hurt state that ignores input), the player mashes the Space key. A developer tells a coding agent: 'when the player presses Space, switch to the jump state'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A precise version switches to jump when Jump is pressed, the character is on the floor and the state allows jumping.
- [ ] B. The instruction ties the state change to the key press, so the agent may jump even while the character is stunned.
- [ ] C. Input must be handled inside the animation state machine itself, because animation is where input lives and the machine owns it.
- [ ] D. Choosing animation straight from key presses keeps the animation in step with what the movement code does.
- [ ] E. Driving jump from physical state, such as leaving the floor with upward velocity, stays consistent even for a bounce-pad launch.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Naming the press plus the guarding conditions makes the transition unambiguous.
- B: A press-only condition ignores whether the character can jump now.
- C: Input is normally interpreted by gameplay code, which then sets state or parameters for the animation.
- D: A key press can be ignored or overridden by the movement code (stun, no ground), so the picture and the movement can disagree.
- E: Basing the state on what the body is doing keeps picture and movement in agreement, whatever caused the movement.

**Source:** Say it to the agent: input-driven versus state-driven change

## MA-ch11.8

A character has the states Idle, Run, Attack, Hurt and Dead. Hit reactions should interrupt an attack. Death should override every other state. Run input should not interrupt an attack. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Priority matters only if more than one state is active at once, since only simultaneous states can compete for control.
- [ ] B. With no Attack-to-Run transition, Run input is ignored during the attack, but Attack still needs an exit, such as Idle at clip end.
- [ ] C. Giving Hurt a transition out of Attack expresses 'hit reactions interrupt an attack' explicitly.
- [ ] D. A transition into Dead from all states (an Any State transition in Unity, say) expresses 'death overrides everything'.
- [ ] E. When two transitions out of the current state are both valid, the engine's ordering or priority rules pick one, so state the order.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A state machine has one active state; priority decides between several transitions that are valid at the same moment.
- B: The absence of a transition is how a machine forbids an interruption, but an exit must still exist or the state sticks.
- C: An interrupt exists only if a transition from the interrupted state to the interrupting state is defined.
- D: Any State is a special state that stands for all states, so one transition from it applies everywhere.
- E: Equal-looking choices are resolved by priority or order, and an unstated order leaves the result to chance or to the agent.

**Source:** Interrupts and priority

## MA-ch11.9

In a playtest, after the player is hit, the character plays the Hurt animation and then freezes in its last pose, ignoring input forever. The only transition out of Hurt has the condition 'hurt_finished is true'. Nothing in the project's code ever sets hurt_finished. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. This is a stuck state: the machine sits in a state whose only exit condition stays false.
- [ ] B. Adding a second, unconditional transition from Hurt to Dead fixes the problem without side effects.
- [ ] C. Because the machine has one current state, the problem is easy to see by logging the current state, which stays Hurt.
- [ ] D. Making Hurt exit when its clip ends would remove the dependence on a flag that nobody sets.
- [ ] E. The cause must be a bug in the animation clip, because clips decide transitions.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A state with an exit condition that is never satisfied can never be left.
- B: An unconditional transition would send every hurt character to Dead, which is a new bug.
- C: The current state is one visible value, so it can be logged or shown on screen.
- D: An exit at the end of the clip, or a condition the code really sets, gives Hurt a working way out.
- E: Transitions come from the machine's conditions and parameters; a clip only supplies the pose over time.

**Source:** Edge case: stuck state

## MA-ch11.10

A developer tells a coding agent: 'when the player presses Dodge, play the dodge animation'. The animation state machine has the states Idle, Run, Attack and Dodge. No transition from Attack to Dodge exists. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The state machine will go from Attack to Dodge on its own, since both states belong to the same machine.
- [ ] B. A request for a state with no allowed route is refused, whether it comes from a trigger or a direct play call.
- [ ] C. The engine adds the missing Attack-to-Dodge transition the first time the player presses Dodge during an attack.
- [ ] D. If the agent plays the dodge clip directly, bypassing the state machine, while the machine is in Attack, the machine still reports Attack.
- [ ] E. The instruction does not say whether Dodge may cancel an attack, so the agent has to decide.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Reachability exists only through transitions that were defined.
- B: Engines differ: a call that forces a state directly (for example Animator.Play in Unity) skips transitions, while a trigger or condition needs one.
- C: Engines do not invent transitions; missing ones must be authored.
- D: A clip played outside the machine does not update the machine's recorded state, so it stays out of step with what is on screen.
- E: Whether an attack can be cancelled is a design rule that the sentence leaves unsaid.

**Source:** Edge case: impossible transition

## MA-ch11.11

An attack clip lasts 0.5 s. The player presses Attack at t = 0.00, 0.10, 0.20, 0.30 and 0.40 s. Three designs are considered: (1) ignore Attack presses while an attack is playing; (2) restart the attack on every press; (3) remember one press made during the attack and start the next attack when the first one ends. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Under (2), the swing is cut off and restarted four times, so the last swing can finish no earlier than 0.90 s.
- [ ] B. Under (3), the second attack starts at 0.10 s, as soon as the second press arrives, interrupting the first.
- [ ] C. Under (1), exactly one attack happens, starting at 0.00 s, and the other four presses are lost.
- [ ] D. Under (3), the character performs five attacks in a row, one for each press that was made.
- [ ] E. Design (1) is an input buffer, since it handles the presses that arrive during the attack.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Restarts at 0.1, 0.2, 0.3 and 0.4 s mean the final swing starts at 0.40 s and ends at 0.40 + 0.5 = 0.90 s.
- B: Under (3) the press is remembered and used when the first attack ends, at 0.50 s.
- C: The first press starts the attack, and the later presses fall inside its 0.5 s and are discarded.
- D: Only one press is remembered, so one extra attack follows, not four.
- E: Design (1) is an input lock; an input buffer is design (3), which remembers a press instead of discarding it.

**Source:** Edge case: rapid input

## MA-ch11.12

A game uses an input buffer of 0.15 s. After an attack, the player may start the next attack at t = 0.50 s, when recovery ends. A press of Attack is remembered for 0.15 s after it is pressed and is used if an attack becomes available within that time. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Input buffering shortens the attack clip so that the next attack comes sooner.
- [ ] B. A press at t = 0.40 s starts the next attack at t = 0.50 s.
- [ ] C. Lengthening the buffer to 0.5 s makes the controls more precise with no downside.
- [ ] D. A press at t = 0.52 s starts an attack immediately, because an attack is already available when the press arrives and nothing needs to be remembered.
- [ ] E. A press at t = 0.30 s starts the next attack at t = 0.50 s.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A buffer changes when a remembered press is used, not how long the clip lasts.
- B: The press is remembered until 0.55 s, which is after the attack becomes available at 0.50 s, so it is used then.
- C: A long buffer lets old presses fire later and queues attacks the player did not mean, which makes controls feel unresponsive and unpredictable.
- D: The attack is already available at 0.52 s, so the press is used at once without being remembered; the buffer only matters for presses made before 0.50 s.
- E: The press expires at 0.45 s, before the attack is available at 0.50 s, so it is lost.

**Source:** Input buffering

## MA-ch11.13

A dash lasts 0.2 s and has a cooldown of 1.5 s measured from the moment the dash starts. The player presses Dash at t = 0.0, 1.0, 1.6 and 2.0 s. A press is used at once if a dash is allowed and is otherwise discarded (there is no buffering). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A cooldown and an animation lock are the same thing, since both only block actions while an animation is playing.
- [ ] B. The press at 2.0 s is rejected by the cooldown, which runs until 3.1 s, even though the second dash animation has already ended.
- [ ] C. Exactly two dashes happen, starting at 0.0 s and 1.6 s.
- [ ] D. The press at 1.0 s is rejected because the first dash is still in progress.
- [ ] E. With a 0.15 s input buffer, the press at 1.0 s would start a dash at 1.5 s.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A cooldown is a minimum time between uses and can outlast the animation, while a lock blocks action only while the animation plays.
- B: The second dash ran from 1.6 s to 1.8 s, but the cooldown lasts until 1.6 + 1.5 = 3.1 s.
- C: The first dash starts at 0.0 s and the cooldown ends at 1.5 s, so 1.0 s is rejected and 1.6 s is accepted; its cooldown then runs to 3.1 s, so 2.0 s is rejected.
- D: The first dash ended at 0.2 s; the press at 1.0 s is rejected by the cooldown.
- E: The buffered press would expire at 1.15 s, before the dash is allowed again at 1.5 s.

**Source:** Cooldown versus animation lock versus buffer

## MA-ch11.14

Players complain that jumping 'doesn't work' when they press Jump a few milliseconds after running off a ledge, and also when they press it just before landing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Coyote time allows a jump for a brief grace period after the character has left the ground.
- [ ] B. Coyote time is the delay between the button press and the start of the jump animation.
- [ ] C. Both techniques change the physics of the jump, making it higher or longer than normal.
- [ ] D. Jump buffering is another name for coyote time, as both forgive a late press.
- [ ] E. The coyote window starts when the player presses Jump, and the jump is performed if the character lands before that window runs out.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Coyote time forgives a press that arrives just after the character walked off an edge.
- B: Press-to-animation delay is input latency, which is a different problem.
- C: Both are tolerance windows for input timing and leave the jump's physics alone.
- D: Jump buffering remembers a press made just before landing; coyote time forgives a press made just after leaving the ground.
- E: The coyote window starts when the character leaves the ground; a window that starts at the button press and waits for landing is jump buffering.

**Source:** Input leniency: coyote time and jump buffering

## MA-ch11.15

A sword swing clip is 0.6 s long. The designer needs (a) the damage hitbox on from 0.20 s to 0.35 s, (b) a sound at 0.20 s, and (c) the character to return to Idle when the swing ends. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Events keyed at 0.20 s and 0.35 s are evaluated only if the game draws a frame at exactly those times.
- [ ] B. Keying the hitbox's enabled property on and off in the clip is another way to get (a).
- [ ] C. Item (c) reacts to the clip finishing, commonly handled by a 'finished' signal or an end-of-state transition.
- [ ] D. If the swing's playback speed is doubled, a code timer set to 0.20 s still lines up with the clip's events, since both are measured in seconds.
- [ ] E. Items (a) and (b) sit at moments inside the clip, which is what animation events (calls keyed on the timeline) are for.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Events are evaluated when the playhead passes their time during an update, so exact frame times are not required.
- B: A property track in the clip can enable and disable the hitbox directly, with the timing stored in the clip.
- C: Completion of a clip or state is normally signalled by a finished signal or an end-of-state transition.
- D: At double speed the clip reaches its 0.20 s mark after 0.10 s of real time, so a 0.20 s timer fires late.
- E: Events run code at keyed times, which is how in-clip moments such as a hit window or a sound are timed.

**Source:** Animation events versus finished signals

## MA-ch11.16

In a melee game, the player's sword and an enemy both need collision shapes. A developer asks a coding agent for 'a collider on the sword and one on the enemy'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. 'Collider' does not say which shape deals damage and which receives it, or whether either blocks movement.
- [ ] B. A sword's hitbox is typically enabled for part of the swing, while the enemy's hurtbox stays on while it can be hurt.
- [ ] C. The hurtbox must be a solid collider that physically stops the sword, so the blade cannot pass through the enemy.
- [ ] D. The sword's damage-dealing region is a hitbox, and the enemy's region that can receive damage is a hurtbox.
- [ ] E. Without layer or mask filtering, a character's hitbox could overlap its own hurtbox and hurt its owner.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: 'Collider' names neither role nor behaviour, so the agent has to guess both.
- B: Hitboxes are switched on for the active frames of an attack, while hurtboxes stay on while the target is vulnerable.
- C: Hitbox and hurtbox are usually detection shapes (areas or triggers) that report overlaps without blocking.
- D: A hitbox is the attacker's damaging region and a hurtbox is the defender's vulnerable region.
- E: Layers and masks decide which shapes can detect each other, and without them a body's own boxes overlap.

**Source:** Hitbox versus hurtbox

## MA-ch11.17

An attack clip runs at 60 updates per second and lasts 27 updates (numbered 0 to 26, which is 0.45 s). Its hitbox is enabled from update 6 through update 14, inclusive, and disabled for the rest of the clip. An enemy stays inside the hitbox for the whole active window. The game applies damage on every update in which the hitbox overlaps an enemy hurtbox, unless the attack records which enemies it has already hit. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The hitbox is active for 9 updates, which is 0.15 s.
- [ ] B. Recording already-hit enemies means the hitbox must switch off after its first overlap.
- [ ] C. If the attack does not record enemies already hit, one swing can damage this enemy up to 9 times.
- [ ] D. Startup (before the hitbox turns on) is 6 updates, or 0.1 s, and recovery (after it turns off) is 12 updates, or 0.2 s.
- [ ] E. Leaving the hitbox on for all 27 updates would not change how fair the attack feels, provided damage is counted once.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Updates 6 through 14 inclusive are 14 − 6 + 1 = 9 updates, and 9 / 60 = 0.15 s.
- B: The attack remembers which targets were hit and can keep the hitbox on for other enemies.
- C: Damage on every overlapping update gives 9 hits over a 9-update window.
- D: Updates 0 to 5 are 6 (0.1 s) and updates 15 to 26 are 12 (0.2 s), which with the 9 active updates make 27.
- E: A hitbox active during startup and recovery hurts enemies when the blade is not visibly there, which feels unfair.

**Source:** Hitbox timing: startup, active, recovery

## MA-ch11.18

A developer tells a coding agent: 'make the character animate when it moves'. The project has idle, walk, run and jump clips. Check each statement that is true about what the instruction leaves open. Each statement is worth 1 point (5 points total).

- [ ] A. The word 'moves' fixes an exact condition, so two agents would build the same machine.
- [ ] B. It does not say whether moving through the air counts, or what to play while jumping or falling.
- [ ] C. It does not say whether the jump clip loops or plays once.
- [ ] D. It does not say at which speeds walking gives way to running.
- [ ] E. It does not say whether clips should cross-fade or cut, or how long a cross-fade lasts.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: 'Moves' leaves thresholds, directions and priorities undefined, so different agents will make different choices.
- B: 'Moves' does not distinguish movement on the ground from movement in the air.
- C: Looping versus one-shot playback is a per-clip decision the sentence leaves out.
- D: The speed threshold between walk and run is a number the sentence never gives.
- E: Blend behaviour and length are not mentioned, so the agent chooses them.

**Source:** Say it to the agent: make the character animate when it moves

## MA-ch11.19

A developer must tell a coding agent how four states (Idle, Run, Jump, Fall) connect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. 'Connect the states sensibly' leaves it to the agent to decide which transitions exist.
- [ ] B. The instruction should also say which states may be interrupted and by what, because otherwise the agent decides.
- [ ] C. A diagram of arrows between the states is as precise as a table, because the arrows carry the conditions.
- [ ] D. Naming the four states without conditions is enough, because the conditions follow from the names.
- [ ] E. A list with one row per allowed transition (from state, to state, condition, cross-fade time) leaves an agent nothing to decide about which transitions exist, when each one fires or how long each one blends.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Without a list, the set of transitions is the agent's guess.
- B: Interrupt rules (who may cut whom) are design decisions that need to be stated.
- C: Arrows show which routes exist but not when they fire, so conditions and blend times are still missing.
- D: Names such as Fall do not say whether the condition is velocity, floor contact or something else.
- E: Each row fixes both ends, the trigger and the blend, so those three things are fully specified; loop settings and interrupt rules are separate decisions that still need their own lines.

**Source:** Say it to the agent: specifying transitions

## MA-ch11.20

A designer says: 'the attack can be cancelled into a dodge, but not into another attack, until its recovery phase starts'. The attack clip has startup, active and recovery phases. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. This describes a cancel window: a span of the attack during which another action may interrupt it.
- [ ] B. By this rule, an Attack press during the active phase should start a second attack at once, since attacks chain freely.
- [ ] C. The window should follow the clip's own time or events, not fixed seconds in code, so it tracks playback speed changes.
- [ ] D. Animation events at phase boundaries could set flags such as 'can_cancel' that transition conditions read.
- [ ] E. The sentence gives no times or frames for where the phases begin and end, so the agent needs them or events that mark them.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A cancel window is the portion of an action during which interruption is permitted.
- B: The rule says the attack cannot be cancelled into another attack before recovery starts.
- C: Clip-time markers scale with playback speed, while fixed seconds in code drift away from the visuals.
- D: Events let the clip mark phase changes, and conditions on the resulting flags control which transitions are allowed.
- E: Phase boundaries are numbers or markers the sentence leaves out.

**Source:** Say it to the agent: cancel windows and interrupts

## MA-ch11.21

A project already has a gameplay state machine in code (Idle, Move, Attack, Hurt). A coding agent is asked to 'add an animation state machine' and builds a second, separate machine in the animation tree that tracks its own Idle, Move, Attack and Hurt states from the player's input. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The two machines can disagree, for example when gameplay says Hurt while the animation is still in Attack.
- [ ] B. Making gameplay the one authority fixes a Hurt state whose exit transition does not fire, because animation and gameplay can then no longer disagree about it.
- [ ] C. A safer design makes gameplay state the single authority and lets the animation machine read it, say through a parameter.
- [ ] D. A second machine reading the same inputs agrees with the first, because identical inputs produce identical states.
- [ ] E. The animation machine should decide whether damage is dealt, because it knows when the hit animation ends.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Two machines with their own rules and timing can fall out of step.
- B: One authority removes the disagreement between the two machines, not a state whose exit does not fire; that state stays in the gameplay machine, so stuck states still need design and testing.
- C: One source of truth for state keeps picture and gameplay in agreement.
- D: Different rules, timing and sampling can give different states from the same inputs.
- E: Damage is a gameplay decision; animation should present state, not decide outcomes.

**Source:** Single source of truth for state

## MA-ch11.22

A team wants automated tests for a character's animation state machine. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A test should set the state variable straight to the target state, because driving real input only tests the engine's input system.
- [ ] B. A test can press the real jump action and then check the current state, instead of writing the state directly.
- [ ] C. A passing state test proves that the motion looks right to players and also feels good to play.
- [ ] D. With a finite list of states and transitions, a test can check each listed transition and that unlisted ones do not happen.
- [ ] E. Checking that each state except a deliberate end state has an exit can find stuck-state errors before anyone plays.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Writing the state directly skips the transition logic that the test is meant to check.
- B: Driving real input exercises the conditions and transitions that connect input to state.
- C: A test checks state and behaviour; whether motion looks right is judged by watching it.
- D: States and transitions are enumerable, so each allowed route and each forbidden one can be exercised.
- E: A state with no exit is a static property of the graph that a check can find without playing.

**Source:** Testing state machines

