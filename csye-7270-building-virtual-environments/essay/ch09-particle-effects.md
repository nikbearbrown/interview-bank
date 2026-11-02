# Chapter 9: Particle effects

## ES-ch09.1

In a 2D game, a developer tells a coding agent: "Add an explosion when the grenade hits." Rewrite this instruction precisely, using the correct particle-effect terms, and explain what the agent could build wrongly if it were given only the original wording.

**Points:** 5

**Rubric (1 point each):**

1. Specifies a one-shot burst with a stated particle count born at one instant, rather than a looping emitter with a continuous rate.
2. Gives a lifetime in seconds and defines the motion: an initial speed range, a spread (range of launch directions) and gravity (or none).
3. Specifies the changes over lifetime, such as a scale curve to zero and a colour or alpha ramp that fades to transparent, read by normalised age.
4. Says where and when it plays, covering at least three of these four: at the grenade's position on the hit event; in world coordinates; as an object that is not hidden or destroyed with the grenade; with a size, texture or colour that makes each particle visible.
5. Names what the vague wording leaves open (looping forever, wrong position, particles too small or faint to see, no fade, never replaying on the next hit).

**Source:** Say it to the agent: "an explosion" versus a precise burst

## ES-ch09.2

A smoke effect must never have more than 240 particles alive at once. (a) Explain how emission rate, lifetime and the number of live particles are related. (b) With a lifetime of 3 seconds and continuous emission, what is the highest rate that stays within the limit? (c) A developer instead fires a burst of 100 particles every 0.5 seconds, each living 1.2 seconds. Work out the average and the peak number of live particles, and say whether the limit is met. (d) Describe two ways to fix the problem, and say what you would tell the coding agent.

**Points:** 5

**Rubric (1 point each):**

1. States that the steady-state live count is emission rate times lifetime (births per second times seconds of life).
2. Computes the maximum continuous rate for a 3-second lifetime: 240 / 3 = 80 particles per second.
3. Computes the average for the burst case: (100 / 0.5) × 1.2 = 240 live particles.
4. Shows the peak is higher than the average: just after a burst three bursts overlap (ages 0, 0.5 and 1.0 seconds), giving 300 particles, so the limit is exceeded even though the average equals it.
5. Gives two fixes with their effect (for example a burst of 80, giving a peak of 240, or a lifetime of 0.9 seconds so at most two bursts overlap, giving 200) and tells the agent to treat the limit as a hard cap on peak live particles and to test the peak.

**Source:** Rate, lifetime and particle count

## ES-ch09.3

A game has two effects. Effect 1 is ambient snowfall with 30,000 flakes that never affect gameplay. Effect 2 is 60 sparks from a collected coin, and each spark that touches the player adds to the score. Explain the difference between CPU particles and GPU particles, choose a kind for each effect, and defend each choice. Say what other factors you would check before settling the choice.

**Points:** 5

**Rubric (1 point each):**

1. Defines the difference: CPU particles run the per-particle update on the CPU, GPU particles run it in shaders on the graphics card; both are drawn by the GPU.
2. Chooses GPU particles for the snow: the count is large, the effect is cosmetic, and no script needs per-particle state.
3. Handles the scoring sparks by keeping the gameplay out of the particle system (separate gameplay objects or checks do the touching and scoring, with particles used only for the look), because per-particle gameplay logic needs particle state that GPU particles do not give cheaply; CPU particles are also accepted where the student notes that this works only if the engine lets scripts read per-particle state.
4. Explains cost: CPU simulation cost grows roughly in proportion to particle count, while GPU simulation moves that cost to the graphics card; drawing cost (fill rate, overdraw) is paid in both.
5. Names checks before settling: target hardware support (CPU particles run on a wider range of devices), whether the engine offers a needed feature only on one kind, and measuring on the target device.

**Source:** CPU versus GPU particles

## ES-ch09.4

Explain why a screen full of large, transparent smoke particles can be expensive even when there are only a few hundred of them. Define overdraw, give a numerical illustration of how the fragment count is found, and list four ways to reduce the cost. Say how you would confirm the cost on a phone.

**Points:** 5

**Rubric (1 point each):**

1. Defines overdraw as the same screen pixel being shaded more than once by overlapping surfaces, and gives the fragment count as pixels covered per particle times the number of particles (for example 150 quads of 200 × 200 pixels give 6,000,000 fragment-shader runs).
2. Explains why transparency is costly: stacked transparent layers cannot be rejected early by the depth test, and each must be blended in turn onto the pixel, whereas hidden opaque surfaces can be skipped.
3. Notes that cost grows with the square of particle size (doubling width and height quadruples the fragments) and that transparent corners of a quad are still shaded.
4. Lists four levers, such as fewer particles, smaller particles, shorter lifetime (live count is rate times lifetime), a quad shape that hugs the visible puff, or lower-resolution rendering of the effect.
5. Says to confirm the cost by measuring on the target phone with a GPU profiler or an overdraw view rather than estimating.

**Source:** Overdraw

## ES-ch09.5

In a 2D game a rocket flies around the screen. A developer tells a coding agent: "Attach two particle effects to the rocket, an exhaust and a glowing aura." The exhaust should leave a trail behind the rocket; the aura should stay around it. Explain local versus world coordinates, say which one each effect needs, describe what would happen if they were swapped, and rewrite the instruction precisely.

**Points:** 5

**Rubric (1 point each):**

1. Defines local coordinates (particle positions are relative to the emitter's transform, so they move and rotate with it) and world coordinates (a particle keeps its position in the scene once it is born).
2. Chooses world coordinates for the exhaust, because particles stay where they were born as the rocket moves, which forms the trail.
3. Chooses local coordinates for the aura, because its particles must move with the rocket.
4. Describes the swap: an exhaust in local coordinates is carried along as a rigid plume with no trail, and an aura in world coordinates is left behind and smears across the screen.
5. Rewrites the instruction so that each effect names its coordinate space (and ideally its rate, lifetime and parent), and explains that the vague wording leaves the space to the agent's default.

**Source:** Local versus world coordinates

## ES-ch09.6

A 3D game needs a campfire with flames and sparks, and a column of dark smoke above it. Explain additive blending and alpha blending, say which each effect should use, and justify the choices. Explain what billboarding is and why the particles here need it, and describe how you would state these choices to a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines alpha blending (result mixes particle and background by alpha, so drawing order matters) and additive blending (particle light is added to the background, so order does not matter).
2. Chooses additive blending for flames and sparks, because overlap brightens toward white and no sorting is needed; notes that colours are clamped, so many overlapping particles can burn out to white.
3. Chooses alpha blending for the dark smoke, because smoke must cover and darken what is behind it; adding a dark colour adds almost nothing, so additive smoke would be invisible.
4. Defines billboarding (flat quads turned each frame to face the camera) and explains why these particles need it: a flat flame or smoke quad would otherwise be seen edge-on as a thin line from some angles.
5. States the choices to the coding agent as explicit settings for each emitter (blend mode and billboarding, and for example rate, lifetime and colour ramp) rather than leaving them to defaults.

**Source:** Additive blending and billboarding

## ES-ch09.7

A coding agent adds a death effect and reports: "Test passes: the burst is emitting after the hit." The test was run headless, with no window and no graphics card. Explain what that result does and does not establish. Separate visual intent, engine state and measured cost, say which of them the test can reach, and describe how you would verify the other parts, including how random numbers should be handled in the tests.

**Points:** 5

**Rubric (1 point each):**

1. Separates three things: visual intent (what the effect should look like), state (what the engine reports, such as emitting, position and a finished signal) and cost (what the effect takes from the frame).
2. Says a headless test can reach state: whether the effect starts, where it is, whether it is visible in the tree, whether it ends and whether it plays again on a second hit.
3. Lists things "emitting" does not show, such as a hidden or destroyed parent, an off-screen position, zero alpha, the wrong layer, particles too small to see, or a burst that fires only once (any valid example counts).
4. Explains that headless runs measure CPU simulation at most; GPU simulation and drawing (fill rate, overdraw) need a real GPU on the target hardware with a profiler, and a person must look at the screen for the appearance.
5. Explains how random numbers are handled in the tests: fix the random seed and the time step so a burst repeats exactly and a failure can be reproduced.

**Source:** Particle effects: evidence versus a claim of success
