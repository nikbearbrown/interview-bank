# Jargon test: movement, shaders and physics (essay)

## ES-jargon.9

A designer says, "The jump feels unfair." Explain coyote time and a jump buffer: what each remembers, which player mistake each forgives, and how each is measured. Then write one exact instruction to an agent that adds both to a platformer with sensible values.

**Points:** 5

**Rubric (1 point each):**

1. Defines coyote time as a short grace window after leaving a ledge during which a jump is still allowed.
2. Defines a jump buffer as remembering a jump press just before landing and performing the jump on landing.
3. Matches mistakes: coyote time forgives a late press, the jump buffer forgives an early press.
4. States that both are measured as short durations (seconds or frames) and gives plausible values.
5. Writes an exact instruction naming both features, their durations, and the condition to reset them.

**Source:** Coyote time and jump buffer

## ES-jargon.10

Explain velocity, speed, acceleration and delta time. A character runs faster on a 144 frames per second monitor than on a 30 frames per second laptop. Diagnose the cause and write the corrected movement rule in words.

**Points:** 5

**Rubric (1 point each):**

1. Defines velocity as speed plus direction (a vector) and speed as its size.
2. Defines acceleration as the rate at which velocity changes.
3. Defines delta time as the time since the previous frame.
4. Diagnoses the bug: movement adds a fixed amount per frame, so more frames per second means more distance per second.
5. States the fix: scale per-second speed or acceleration by delta time, and run physics in a fixed timestep step.

**Source:** Delta time and frame-rate independence

## ES-jargon.11

Distinguish a collider, a trigger, a rigid body, a kinematic body and a static body. For a coin, a moving platform, a tumbling crate, a wall and the player character, name the best choice and say why.

**Points:** 5

**Rubric (1 point each):**

1. Defines a collider as the shape used for contact tests and a trigger as a volume that detects overlap without blocking.
2. Defines a rigid body as simulated by physics, a kinematic body as moved by code or animation, and a static body as not moving.
3. Chooses a trigger for the coin and gives the reason (detect, not block).
4. Chooses kinematic for the moving platform and the player (script controlled), rigid for the crate, and static for the wall, with reasons.
5. Uses the terms correctly without mixing them (for example does not say a trigger blocks).

**Source:** Body types and triggers

## ES-jargon.12

Rewrite this vague prompt using exact game-movement terms: "Make the player move nicely and the platforms work." Your rewrite should name the body type for the player and for a moving platform, the movement rules (velocity, acceleration, friction, gravity, delta time), the collision shapes, and what you would check afterward.

**Points:** 5

**Rubric (1 point each):**

1. Names a body type for the player (for example kinematic character body) and for the platform (kinematic or animatable).
2. States movement rules with velocity, acceleration or friction, and gravity.
3. Says the changes are scaled by delta time or run in the fixed timestep.
4. Names collider shapes and, where needed, a trigger area (for example a hurtbox or a pickup zone).
5. Adds checks that can be observed, such as speed at two frame rates and standing on the platform.

**Source:** Rewrite a vague movement prompt

## ES-jargon.13

Compare a vertex shader and a fragment shader, and define uniform, varying and UV. Give one effect for each stage and say how a script would change the effect while the game runs.

**Points:** 5

**Rubric (1 point each):**

1. Defines the vertex shader as running per vertex and setting positions, and the fragment shader as running per pixel and setting colour.
2. Defines a uniform as a value from game code that is the same across a draw call.
3. Defines a varying as a value passed from the vertex stage to the fragment stage and interpolated.
4. Defines UV as 2D coordinates that map a surface to a texture.
5. Gives a vertex example (wave or displacement) and a fragment example (tint or glint), and says a script sets a uniform each frame to change them.

**Source:** Shader stages and inputs

## ES-jargon.14

Explain albedo, normal map, roughness, metallic, emission and PBR to an artist who has never written a shader. Then describe a worn metal door with glowing warning lights using those terms.

**Points:** 5

**Rubric (1 point each):**

1. Defines albedo as base colour without lighting.
2. Defines a normal map as a per-pixel surface direction that fakes small bumps in lighting without moving geometry.
3. Defines roughness (sharp or blurry highlights) and metallic (how much it behaves like a metal).
4. Defines emission as self-lit colour, and PBR as a physically based set-up that behaves consistently under different lights.
5. Describes the door correctly: high metallic, medium roughness with worn spots, a normal map for dents and an emission colour for the lights.

**Source:** Material vocabulary

## ES-jargon.15

A student writes: "Use a normal map to make the lava glow and the fragment shader to move the vertices." Identify each wrong word, say what the correct term is, and rewrite the instruction. Also name which blend mode you would pick for a rising smoke effect and for a glow, and why.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that glow is emission, not a normal map.
2. Identifies that moving vertices is vertex shader work, not fragment shader work.
3. Writes a corrected instruction using emission for the glow and a vertex shader for the movement.
4. Chooses alpha blending for smoke because it mixes by opacity.
5. Chooses additive blending for a glow because it adds light to what is behind it, and explains that it brightens where layers overlap.

**Source:** Spot the wrong word in a shader prompt

## ES-jargon.16

Write a short "say it to the agent" paragraph that asks for an enemy that patrols, chases, and attacks. Use at least five exact terms from state machines, collision and animation, and explain how each term keeps the agent from guessing.

**Points:** 5

**Rubric (1 point each):**

1. Names a state machine with patrol, chase and attack states and the transitions between them.
2. Gives conditions for transitions, such as a sight trigger area and an attack range.
3. Names collision pieces, such as a hitbox for the attack and a hurtbox for taking damage, as triggers.
4. Names animation pieces, such as clips per state and a blend or transition between them.
5. Explains for at least three terms what the agent would have to guess without them.

**Source:** Say it to the agent: enemy behaviour
