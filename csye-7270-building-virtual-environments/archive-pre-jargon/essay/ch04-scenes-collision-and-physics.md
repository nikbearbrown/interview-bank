# Chapter 4: Scenes, collision and physics

## ES-ch04.1

A developer gives a coding agent this instruction for a 2D Godot game: "Add a collider to the shield pickup so that the player can collide with it and get the shield." Explain the two different things the word "collide" could mean here, what the agent could build wrongly, and then rewrite the instruction precisely using the terms collider, trigger (area), layer and mask. State one observable result that would show the pickup works.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes a solid collider, which blocks or deflects other bodies and produces a collision response, from a trigger or area, which only reports that an overlap began or ended and blocks nothing, and identifies that the pickup should be the detection kind the player can walk through (a Godot Area2D, a Unity trigger collider, or an Unreal overlap), not a solid obstacle.
2. Names a plausible wrong build: a solid body that stops or pushes the player so it cannot be collected, or a detection region whose layer and mask never see the player so nothing fires.
3. The rewrite specifies a detection-only region with its own collision shape, an event on the player's entry that gives the player the shield (removing the pickup afterwards is optional), and an explicit statement that it must not block movement.
4. The rewrite assigns the pickup its own layer and sets the scanning side's mask so that only the player is detected.
5. States one observable result that shows the pickup works, such as the player passing through the pickup and the shield state being set once.

**Source:** Collider versus trigger, say it to the agent

## ES-ch04.2

A teammate says "collider, trigger and raycast are all just ways of finding out that two things touched". Write a correction. For each of the three, say what it is, what it does and does not do, and give one gameplay use. Then name the corresponding term for the trigger in Godot, Unity and Unreal, and state one rule for choosing between them when briefing a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. A collider is a solid shape whose contacts produce a collision response (blocking, sliding, pushing); it does not merely report.
2. A trigger is a non-blocking region that reports entering and leaving to code (and staying, by asking which objects are inside now or through a stay event in engines that have one); it applies no response.
3. A raycast is a query along a line that returns the first thing hit (or nothing) at that moment; it is not a physical body (it may be run through a node or a direct physics query, but it is a question, not an obstacle), has no width, and does not block, push or notify anything.
4. Half a point if all three uses are fitting, such as a wall or floor (collider), a pickup or damage zone (trigger), and line of sight or a hitscan shot (raycast); half a point for naming the trigger's engine terms: Godot Area, Unity trigger collider, Unreal overlap.
5. States a sound selection rule, such as: if it must stop things use a solid collider, if it must notify when something is inside use a trigger, if it must ask a question about the space along a line use a raycast, and the brief should say which.

**Source:** Collider, trigger and raycast

## ES-ch04.3

A 2D game has walls, a player, enemies, player bullets, enemy bullets and coins. The design requires: the player is blocked by walls; enemies are blocked by walls but pass through one another; player bullets hit enemies but not the player or coins; enemy bullets hit the player; coins are detected only by the player. Design the collision layers and masks, explain the difference between a layer and a mask, and explain why writing the numbers into code needs care. Assume Godot, and say why leaving every object on the default layer would be unsuitable.

**Points:** 5

**Rubric (1 point each):**

1. Defines a layer as the layer or layers an object appears in, and a mask as the layers it scans for contacts; detection runs from the scanner's mask to the other object's layer.
2. Gives every type that another object must scan or ignore its own layer (for example walls, player, enemies and coins, with bullets on one shared layer or split into player and enemy bullets) rather than leaving everything on the engine's default layer.
3. Sets masks that satisfy the five rules, for example enemies scan walls but not the enemy layer, player bullets scan enemies only, enemy bullets scan the player, and coins are detected only by the player: either the player (or its pickup area) scans the coin layer, or the coin's detector scans the player's layer, and either direction is accepted if no other object can detect coins (the rules do not require enemies and the player to collide, so a design may include or omit that contact).
4. Explains why the default is unsuitable: with everything on one layer and scanning that layer, everything collides with everything, which is why explicit settings are needed.
5. Explains that in code layers are bitmask integers, so layer n has the value 2 to the power n minus 1 (layer 3 is 4), so a layer number written as a bit value selects the wrong layer; functions that take layer numbers avoid this.

**Source:** Layers and masks

## ES-ch04.4

A jump written in the per-frame update callback reaches a slightly different height on a 30 frames-per-second machine than on a 144 frames-per-second machine, and fast objects sometimes pass through thin walls. Explain what a fixed time step is, why physics and collision movement belong in the fixed-step callback (Godot's _physics_process, Unity's FixedUpdate), and what goes wrong with a variable step. Finish with one precise sentence you would give a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines a fixed time step: the physics simulation advances in equal increments of game time (for example 1/60 s) regardless of how often frames are drawn.
2. Explains that the per-frame callback runs at a variable rate, and that the engine may run zero, one or several physics steps per rendered frame to keep the physics clock steady.
3. Explains the consequence of a variable step: integration with different step sizes gives different jump arcs and contact results, so behaviour depends on frame rate.
4. Explains that long steps let fast bodies move farther than a thin obstacle is thick and so skip it (tunnelling), and that a constant step makes behaviour reproducible and testable.
5. Gives a precise instruction naming the callback, such as "apply gravity and call the character body's movement function only inside the physics-process callback, and use the physics step's delta".

**Source:** Fixed time step

## ES-ch04.5

In a game whose physics runs at 60 steps per second, a bullet (a RigidBody2D with a circular collider 6 px across) travels at 900 px/s toward a wall that is 8 px thick. Continuous collision detection is off. The bullet usually stops at the wall but occasionally passes through it. Use arithmetic to explain why, define tunnelling and continuous collision detection, and compare three remedies with one cost each.

**Points:** 5

**Rubric (1 point each):**

1. Computes the step distance, 900 / 60 = 15 px per physics step.
2. Shows the arithmetic that makes a miss possible: the bullet overlaps the wall only while its centre is within 8 + 6 = 14 px of range, which is smaller than the 15 px spacing between tested positions, so some bullets land on both sides without ever overlapping.
3. Defines tunnelling as a fast body passing through a thin obstacle because overlap is tested only at discrete positions, and explains it happens only for some bullets because it depends on where the tested positions fall relative to the wall.
4. Defines continuous collision detection as testing the path swept during a step instead of only the end position, and notes it costs more per body, so it is turned on for fast, small bodies.
5. Compares remedies with a cost for each, such as continuous collision detection (cost per body), a raycast from the previous to the new position or a hitscan design (more code, no physical bullet), and thicker walls or a higher physics rate (art constraint or global cost).

**Source:** Tunnelling and continuous collision detection

## ES-ch04.6

A developer must brief a coding agent on a 2D platformer. For each of these, choose a body type (static body, kinematic body, dynamic or rigid body, character body, or trigger region) and justify the choice, saying whether it blocks: the level floor, an elevator platform moved by code, the player, a pushable crate, a spike strip that hurts on contact, and a health pickup. Give Godot and Unity names where you can.

**Points:** 5

**Rubric (1 point each):**

1. Explains the distinction in terms of who moves the object: static is never moved, kinematic is moved by code or animation, dynamic is moved by the physics simulation, and a character body is moved by code with collision detection and no simulation.
2. Assigns the floor to a static body (Godot StaticBody2D, Unity static collider) that blocks, and the elevator to a kinematic body moved by code or animation (Godot AnimatableBody2D, Unity kinematic Rigidbody) that blocks and, when moved, affects other bodies in its path (pushing them or carrying a body that stands on it).
3. Assigns the player to a character body (Godot CharacterBody2D, with gravity and jump written in code) and the crate to a dynamic body (Godot RigidBody2D) that the simulation pushes and moves.
4. Assigns the health pickup to a trigger region (Godot Area2D, Unity trigger collider) that detects the player and does not block.
5. Handles the spikes sensibly, either as a detection region or hitbox that reports contact and does not block, or as a solid spike block that also damages (a static body plus a damage region); either choice earns the point if the answer says which and whether it blocks.

**Source:** Static, kinematic, dynamic and character bodies

## ES-ch04.7

A melee game needs a sword attack. Design the collision setup using the terms hitbox, hurtbox and body collider. Say which of the three are solid and which are detection regions, how layers and masks keep the player from hitting themselves, when the hitbox should be active, how to make sure each enemy is damaged at most once per swing, and give the one-paragraph instruction you would give the coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines the three terms: in the melee convention the hitbox deals damage during an attack and the hurtbox receives it (the reverse naming used in shooters is accepted if it is stated and applied consistently), and the body collider is the solid shape that blocks movement.
2. States that the body collider is solid while the hitbox and hurtbox are detection regions (areas or triggers) that report overlap and do not block.
3. Uses layers and masks so the sword's hitbox scans the enemies' hurtbox layer and not the player's own; the hurtbox may be on a layer separate from the body collider, or share one layer if the answer states how double hits are prevented.
4. Activates the hitbox only for the damaging frames of the swing, and records which targets were already hit in this swing so each is damaged at most once.
5. The agent instruction is precise: it names the three shapes, their layers and masks, the active frames, the once-per-swing rule, and one checkable result such as an enemy losing exactly the damage amount a single time.

**Source:** Hitbox and hurtbox

## ES-ch04.8

A developer asks a coding agent for three behaviours: a crate knocked away by an explosion, a rocket that accelerates while its engine burns, and a character that moves left or right at 200 px/s while a key is held. For each, choose force, impulse or setting velocity, and body type, and justify. Explain why applying an impulse from a per-frame callback is a bug.

**Points:** 5

**Rubric (1 point each):**

1. Defines the terms: a force acts over time and produces acceleration, an impulse is an instantaneous change in momentum applied once, and velocity is the current speed with direction, which can be set directly.
2. Models the explosion knock-back as one impulse on a dynamic (rigid) body (optionally noting that the same impulse changes a heavier body's velocity less, since change in velocity is impulse divided by mass).
3. Models the rocket's thrust as a force applied on every physics step while the engine burns, giving steady acceleration until drag or collision intervenes.
4. Moves the character by setting its velocity, and says who owns the motion: a character body (Godot CharacterBody2D with move_and_slide) fits because it is not simulated and the code owns its motion; a kinematic body, or a rigid body whose linear velocity is set directly, is also accepted if the answer justifies it.
5. Explains that an impulse applied once per rendered frame is applied a different number of times per second on different machines, so the total push depends on the frame rate; continuous effects belong in forces in the fixed-step callback.

**Source:** Force, impulse and velocity

## ES-ch04.9

A game gives the player a 3-second invulnerability power-up. Enemy damage is applied in a handler connected to the "body entered" signal of the player's detection area. In testing, an enemy that is already overlapping the player when the invulnerability ends does not hurt the player until it leaves and re-enters. Explain the cause in terms of enter events versus the set of current overlaps, propose two fixes, and describe a test that would catch the bug.

**Points:** 5

**Rubric (1 point each):**

1. Explains that an enter event fires once when an overlap begins, and nothing new begins when the invulnerability ends, so an overlap that started earlier stays unreported.
2. Distinguishes an event (a change) from a query (the current state): the engine can be asked which bodies overlap now.
3. Proposes a first fix: when the invulnerability ends, query the current overlapping bodies and apply damage to any enemy found.
4. Proposes a second fix, such as polling the overlap list every physics step for damage logic, or using a stay event where the engine has one, so damage does not depend on a one-time entry.
5. Describes a deterministic test: place an enemy overlapping the player, let the power-up expire at a fixed frame rate, and assert damage within a stated number of physics steps, noting a casual playtest could miss the case.

**Source:** Enter events versus current overlaps
