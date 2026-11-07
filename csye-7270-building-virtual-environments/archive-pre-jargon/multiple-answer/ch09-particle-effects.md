# Chapter 9: Particle effects

## MA-ch09.1

A technical artist describes a campfire effect to a coding agent and uses the vocabulary of particle effects. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A particle is one small element of the effect that the system creates, updates and removes over time; it carries its own state, such as age, position and velocity, and is usually drawn as a textured quad or a small mesh.
- [ ] B. Particles are separate game objects with their own scripts, which is why particle effects are expensive for the engine to run.
- [ ] C. An emitter is the source that creates particles, either steadily at some rate or in bursts.
- [ ] D. A particle system is the whole effect (spawning, simulation, drawing), and one effect can combine several emitters.
- [ ] E. Emission shape (a point, sphere, box or cone) decides where particles start, while initial velocity decides how they move; the two are separate settings.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A particle is a lightweight record with a life cycle (it is born, updated each step and removed), and it is drawn as a quad or a small mesh.
- B: Particles are data processed in bulk by one system; they are not individual objects with scripts.
- C: The emitter is where particles are born, and its rate or burst settings control when.
- D: The system covers emission, simulation and rendering, and a larger effect may use more than one emitter.
- E: Placement of births and motion after birth are independent controls.

**Source:** Particle system, emitter and particle

## MA-ch09.2

A coding agent is asked to set up how particles are emitted. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A burst spawns a stated count at one instant, whereas a continuous emission rate, such as 40 per second, spawns particles steadily.
- [ ] B. A burst is the same thing as a looping effect with a high emission rate, since both produce a large number of particles in a short time.
- [ ] C. One-shot (non-looping) means the system plays one emission cycle and then stops until triggered again; it says nothing about the count.
- [ ] D. A burst is a one-time event at the start of playback: on a looping system it fires in the first cycle, and later cycles emit only at the continuous rate.
- [ ] E. A one-shot system that also has a continuous rate keeps emitting until it is stopped by hand, because the rate stays above zero.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Rate is particles per unit time; a burst is a count delivered at a moment.
- B: A high rate spreads births over time, whereas a burst puts them all at one instant.
- C: One-shot controls how many cycles play, not how many particles each cycle spawns.
- D: A looping system starts its cycle again when its duration ends, and a burst is scheduled at a time within the cycle, so the burst fires again in every cycle.
- E: One-shot means the cycle runs once and then emission stops.

**Source:** Emission rate versus burst, and one-shot

## MA-ch09.3

A smoke emitter spawns 40 particles per second, and each particle lives exactly 1.5 seconds. The effect starts with no particles at time 0 and runs continuously. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Doubling the rate to 80 particles per second leaves the steady-state count at 60, because lifetime alone fixes how many particles are alive.
- [ ] B. Once the effect has run for more than 1.5 seconds, about 60 particles are alive at any moment (40 × 1.5).
- [ ] C. At 0.75 seconds about 60 particles are already alive, because the emitter fills its steady-state population immediately at the start.
- [ ] D. If the lifetime were cut to 0.5 seconds at the same rate, about 20 particles would be alive in the steady state.
- [ ] E. A prewarm option, which simulates the system for at least 1.5 seconds before the first visible frame, starts the effect with about 60 particles alive instead of ramping up.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The steady-state count is rate × lifetime, so doubling the rate doubles it to 120.
- B: Births per second times seconds of life gives 40 × 1.5 = 60 alive.
- C: Nothing has died yet at 0.75 s, so only 40 × 0.75 = 30 particles have been born.
- D: 40 × 0.5 = 20.
- E: Prewarm skips the ramp-up by starting from a population that has already reached steady state.

**Source:** Rate, lifetime and particle count; prewarm

## MA-ch09.4

A developer wants a grenade explosion in a 2D game. The first prompt to a coding agent is "add an explosion effect". A second prompt reads: "add a one-shot burst of 40 particles at the grenade's position, each living 0.6 seconds, launched outward in all directions at 150 to 300 pixels per second, no gravity, shrinking to zero size and fading to transparent over its life". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The first prompt is acceptable, because "explosion" is a standard term with a settled meaning across engines, so the agent will build what is expected.
- [ ] B. The second prompt fixes burst versus continuous, count, lifetime, speed range, direction spread, gravity and over-life changes, so two agents would build a burst with nearly the same timing and motion.
- [ ] C. The second prompt is still ambiguous about whether the 40 particles appear at once or are spread over the 0.6 seconds.
- [ ] D. The first prompt leaves the agent free to build a looping emitter that keeps spraying after the grenade has gone off.
- [ ] E. Adding "and make it look cool" to the second prompt would improve the agent's accuracy, because it tells the agent the intended result.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: "Explosion" names no count, lifetime, speed, direction or loop behaviour, so the agent has to guess each one.
- B: Each property that defines when particles appear and how they move is given a value or a rule; texture, colour and blend mode are still open, but they do not change the timing or the motion.
- C: "Burst" means all particles are born at one instant.
- D: Without "one-shot", looping versus playing once is the agent's choice.
- E: An adjective that cannot be measured adds no constraint and no check.

**Source:** Say it to the agent: "an explosion" versus a precise burst

## MA-ch09.5

In a 2D game, gravity acts on particles at 98 pixels per second squared, downward. A particle is launched straight up at 150 pixels per second and lives 0.6 seconds. Measured upward, its velocity is 150 − 98t pixels per second and its height above the start is 150t − ½ · 98 · t² pixels. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A larger spread, meaning a wider cone of launch directions, makes each particle leave the emitter faster.
- [ ] B. At 0.6 seconds the particle is about 72 pixels above its start.
- [ ] C. At 0.6 seconds its vertical velocity is still upward, about 91 pixels per second.
- [ ] D. It would reach its highest point at about 1.5 seconds, so it does not start to fall during its 0.6-second life.
- [ ] E. Initial velocity sets the starting speed and direction, while gravity is a constant acceleration that keeps changing velocity; a particle launched at zero velocity still ends up moving.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Spread widens the range of launch directions; the launch speed is set by the initial velocity, not by the spread.
- B: 150 × 0.6 − ½ × 98 × 0.36 = 90 − 17.64 = 72.36 pixels.
- C: 150 − 98 × 0.6 = 91.2 pixels per second, still positive.
- D: The peak comes when 150 − 98t = 0, at t of about 1.53 seconds.
- E: Velocity changes by the acceleration each second, so zero starting velocity does not mean zero motion.

**Source:** Initial velocity, spread and gravity

## MA-ch09.6

A particle has a lifetime of 0.6 seconds. Its scale curve falls linearly from 1.0 at birth to 0.0 at death, and its colour ramp fades alpha linearly from 1.0 to 0.0. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A curve or ramp over lifetime is indexed by seconds, so the same curve would reach 0 at 1.0 second for lifetimes of 0.6 and 1.2 seconds.
- [ ] B. At an age of 0.15 seconds, the scale and the alpha are both 0.75.
- [ ] C. If the lifetime were changed to 1.2 seconds, then at an age of 0.3 seconds the scale would again be 0.75, because the curve stretches over the longer life.
- [ ] D. A colour ramp sets the colour a particle has at birth; fading during its life needs a script that updates it as the particle ages.
- [ ] E. Curves and ramps are read by normalised age (age divided by lifetime, 0 to 1), so they work unchanged for particles with different lifetimes.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The curve is read by fraction of life, so its end always falls at the particle's death.
- B: 0.15 / 0.6 = 0.25 of the life, and 1 − 0.25 = 0.75 for a linear fall.
- C: 0.3 / 1.2 = 0.25 of the life, which gives the same 0.75.
- D: A colour ramp is sampled across the whole life, which is how fades are made without code.
- E: Using age divided by lifetime lets one curve serve particles of any length of life.

**Source:** Scale and colour over lifetime

## MA-ch09.7

Engines offer particle systems that simulate on the CPU and others that simulate on the GPU. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The CPU or GPU setting decides who draws the particles: CPU particles are drawn by the CPU and GPU particles by the GPU.
- [ ] B. A GPU particle system updates its particles in shaders on the graphics card, so very large counts are practical, but scripts cannot cheaply read each particle's state.
- [ ] C. GPU particles cannot use textures or blending modes, because those features belong to the CPU side of the engine.
- [ ] D. A CPU particle system updates all particles on the CPU each frame, so its simulation cost rises roughly in proportion to the particle count.
- [ ] E. A CPU particle system does not depend on the graphics card for its simulation, so it is the usual fallback on hardware with weak GPU compute support.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Both kinds are drawn by the GPU; the setting decides where the simulation (the per-particle update) runs.
- B: On the GPU the update is data-parallel and fast, but the particle data stays on the graphics card.
- C: Textures and blending belong to drawing, which both kinds share.
- D: CPU simulation is per-particle work on the CPU, so more particles take more CPU time.
- E: GPU simulation needs the graphics hardware to run the update, whereas CPU simulation needs nothing special, so it runs on a wider range of devices.

**Source:** CPU versus GPU particles

## MA-ch09.8

A game must run on an older phone. Effect 1 is 80 sparks per hit, and each spark must apply a gameplay rule (it damages any enemy it touches). Effect 2 is ambient snowfall with 20,000 flakes that never affect gameplay. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Effect 2 suits GPU particles: the count is large and no script needs the flakes' state.
- [ ] B. Because 80 sparks cost almost nothing on the CPU, 20,000 CPU-simulated flakes would cost almost nothing too, since particles are cheap.
- [ ] C. Effect 1 suits CPU particles, or ordinary gameplay objects with particles used only for the look, because per-particle gameplay logic needs state on the CPU.
- [ ] D. Hardware support can tip the choice: CPU particle systems run on a wider range of devices, which matters on old phones.
- [ ] E. Both effects must use the same kind of particle node so that they can be drawn in one draw call and share one material.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A large cosmetic effect is the case GPU simulation is built for.
- B: 20,000 / 80 = 250 times as many particles, and CPU cost grows with count.
- C: Gameplay rules run in scripts on the CPU, which wants the particle state there or a separate gameplay object.
- D: Older devices may lack good GPU compute, so a CPU system can be the safe choice.
- E: Different node types do not have to share a draw call, and nothing about the effects requires it.

**Source:** Choosing CPU or GPU particles

## MA-ch09.9

A spaceship flies across the screen at 300 pixels per second. Two particle effects are attached to it: an engine exhaust, whose particles should trail behind the ship as it moves, and a shield shimmer, whose particles should stay around the ship and move with it. Each particle lives 1 second. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In world coordinates, a particle born 1 second ago has been left about 300 pixels behind the ship's current position, ignoring the particle's own velocity.
- [ ] B. If the exhaust were set to local coordinates, particles born at the tail would be carried along with the ship, so no trail would form.
- [ ] C. The local-versus-world setting makes a visible difference even when the emitter stays still, because it changes how the particles' positions are stored.
- [ ] D. Local coordinates suit the shield shimmer, because its particles move with the emitter's transform.
- [ ] E. With world coordinates a particle keeps the position where it was born while the emitter moves, so the exhaust leaves a trail.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The ship has moved 300 pixels per second × 1 second, while the particle has stayed where it was born.
- B: In local space a particle's position is relative to the emitter, so it travels with the ship.
- C: With a stationary emitter both settings give the same positions; the difference shows only when the emitter moves.
- D: Particles in local space stay attached to the ship, which is what a shield needs.
- E: World-space particles are no longer tied to the emitter after birth.

**Source:** Local versus world coordinates

## MA-ch09.10

Particles can be combined with the background in different ways. In alpha blending the result is particle colour × alpha + background × (1 − alpha). In additive blending the result is background + particle colour × alpha. Colours run from 0 (black) to 1 (full intensity), and results above 1 are clamped to 1. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Over black, pure red then pure blue at alpha 0.5 each give (0.25, 0, 0.5) with alpha blending, and blue then red give (0.5, 0, 0.25), so order matters.
- [ ] B. A black particle drawn additively darkens the background by covering it, so black smoke can be made with additive blending.
- [ ] C. Two additive particles give the same result in either drawing order, because addition does not depend on order.
- [ ] D. Additive blending suits fire, sparks and glows, because overlap brightens toward white; it is a poor fit for dark smoke, which would add nothing.
- [ ] E. Three additive particles that each contribute 0.25 over a background of 0.30 give 1.05 on screen, because additive results are not limited.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Red first gives (0.5, 0, 0) and then blue gives (0.25, 0, 0.5); the reverse order gives (0.5, 0, 0.25).
- B: Adding a black colour adds 0, so the background is unchanged; additive blending can only brighten.
- C: The sum background + a + b is the same in both orders.
- D: Overlapping additive particles accumulate light, which fits emissive effects but not dark, opaque-looking smoke.
- E: 0.30 + 3 × 0.25 = 1.05, which is clamped to 1.0.

**Source:** Additive versus alpha blending

## MA-ch09.11

A 3D game draws each smoke particle as a flat textured quad. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In a 2D game with a flat orthographic camera, billboarding is what keeps the quads facing the screen, so it must be switched on.
- [ ] B. Without billboarding, a flat quad seen exactly edge-on shrinks to a thin line or disappears, which breaks the illusion of a puff.
- [ ] C. A particle drawn as a mesh is also a billboard, because particles are drawn facing the camera, as quads or meshes.
- [ ] D. A billboard is a quad that is turned each frame to face the camera, so the particle shows the same flat shape from any angle.
- [ ] E. A billboarded particle cannot spin about the view direction, because the camera fixes its orientation.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: With a flat orthographic 2D camera the quads already face the screen, so nothing needs to be turned.
- B: A flat quad has no thickness, so from the side it has almost no area to draw.
- C: A mesh particle keeps its 3D shape and orientation; it is the alternative to a billboard.
- D: Turning toward the camera each frame is what billboarding means.
- E: A billboard can still spin about the view direction, which is how rotation over lifetime works for flat particles.

**Source:** Billboarding

## MA-ch09.12

A 1080p frame has 1920 × 1080 = 2,073,600 pixels. A smoke effect uses 150 particles, each drawn as a 200 × 200 pixel quad, and all the quads lie inside a 400 × 400 pixel region of the screen. The smoke texture is a round puff that fills the largest circle inside its square quad, and the rest of the quad is fully transparent. Every pixel of a quad is shaded, including the transparent ones. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Making each quad 100 × 100 pixels would halve the total fragment count, to 3,000,000, because each side is halved.
- [ ] B. Averaged over the 160,000-pixel region, each pixel is shaded 37.5 times (6,000,000 / 160,000), assuming all quads lie inside the region.
- [ ] C. Because 6,000,000 is more than the 2,073,600 pixels of the screen, the effect must cover the whole screen.
- [ ] D. About 21 percent of each quad's area is transparent corner outside the round puff, yet those pixels are still shaded.
- [ ] E. The effect runs the fragment shader 6,000,000 times per frame (150 × 40,000).

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Area scales with the square of the side, so 100 × 100 gives 150 × 10,000 = 1,500,000, a quarter.
- B: 6,000,000 shaded fragments spread over 160,000 pixels is 37.5 layers on average.
- C: The fragments pile up in a 160,000-pixel region, not across the whole screen.
- D: The circle fills π/4 (about 78.5 percent) of the square, so about 21.5 percent is empty corner.
- E: Each quad covers 200 × 200 = 40,000 pixels, and 150 quads give 6,000,000 invocations.

**Source:** Overdraw

## MA-ch09.13

Many large transparent particles cost more than the same number of small or opaque ones. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Halving the lifetime at the same emission rate doubles the number of live particles, because particles are replaced twice as often.
- [ ] B. Doubling each particle's width and height doubles its fragment cost, because the size has doubled.
- [ ] C. Opaque surfaces can be rejected by the depth test when something nearer is already drawn, whereas stacked transparent particles must each be blended in turn.
- [ ] D. Making the texture more transparent everywhere (lower alpha) reduces the number of fragments shaded, because transparent pixels are skipped.
- [ ] E. Overdraw is cheap on mobile GPUs, because tile-based rendering hides the cost of blending.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Live particles equal rate × lifetime, so halving the lifetime halves the count.
- B: Doubling both sides quadruples the area, and so the fragment count.
- C: The depth test can skip hidden opaque fragments, but transparent layers cannot be skipped because each contributes to the result.
- D: Transparent fragments are still shaded and blended; lower alpha only changes the result, not the number of fragments.
- E: Fill rate is a main constraint on mobile, and transparent overdraw is one of its most common costs.

**Source:** Why transparent particles cost more

## MA-ch09.14

A burst effect gives each particle a random speed and direction. Assume the effect takes one simulation step per rendered frame, so the length of a step follows the frame rate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Fixing the seed makes the burst identical at 30 and 144 frames per second, because the random numbers no longer depend on time.
- [ ] B. A random seed is the starting value of a pseudo-random generator; the same seed and draw order give the same numbers, so tests fix it to repeat a burst.
- [ ] C. In shipped games a fixed seed is normally left on, so that explosions look identical, because variation counts as a flaw in a finished effect.
- [ ] D. Determinism needs only a fixed seed; the size of each time step and the order in which random numbers are drawn do not affect the outcome.
- [ ] E. An effect that is given a fixed random seed will look different each time it is played, because the random numbers are drawn fresh from the clock.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The seed fixes the random numbers, but positions also depend on the time step, so different frame rates can give different results.
- B: Seeding makes the generator's output a repeatable sequence, which is what a test needs.
- C: Production effects usually use a varying seed so that repeated bursts do not look copied.
- D: Different time steps or a different order of draws change the outcome even with the same seed.
- E: The same seed gives the same sequence of random numbers, so each play looks the same; variation between plays needs a different seed each time.

**Source:** Determinism and random seeds

## MA-ch09.15

A developer needs a campfire in a 3D game and gives a coding agent one of two prompts. Prompt 1: "make the fire look good". Prompt 2: "a looping emitter, 80 particles per second, lifetime 0.8 seconds, world-space coordinates, additive blending, billboarded quads, initial upward velocity 1.5 to 2.5 metres per second with a small spread, a colour ramp from yellow to transparent red, and scale shrinking to zero over life". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Prompt 2 implies about 64 live particles in the steady state (80 × 0.8).
- [ ] B. On a torch the player carries, world-space coordinates would let the flames trail behind as the player moves.
- [ ] C. "Looping" in Prompt 2 means the emitter keeps emitting until it is stopped, as a campfire should.
- [ ] D. Prompt 1 specifies the same effect as Prompt 2, because the agent already knows what a campfire looks like.
- [ ] E. "Billboarded quads" tells the agent to turn each particle toward the camera, so a flame seen from any side does not become an edge-on line.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Steady-state count is rate × lifetime, 80 × 0.8 = 64.
- B: World-space particles are left behind when the emitter moves, which gives flames weight and motion.
- C: A looping emitter restarts its cycle again and again, so the fire does not stop on its own.
- D: Prompt 1 fixes no rate, lifetime, blending, space or colour, so different agents would build different fires.
- E: Billboarding keeps flat particles facing the camera.

**Source:** Say it to the agent: a precise looping effect

## MA-ch09.16

In a game, an enemy is destroyed the instant it is hit. A one-shot burst effect is a child of the enemy object in the scene hierarchy. During testing, a log line confirms "burst started", yet players never see the burst. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The log line "burst started" proves that the burst was drawn on screen, because the effect cannot start without being drawn.
- [ ] B. A one-shot burst plays again on the next hit without any further action, because the effect resets itself after finishing.
- [ ] C. A common fix is to spawn the effect as its own object in the world, at the enemy's position, so that it outlives the enemy.
- [ ] D. Switching from CPU particles to GPU particles would make the burst visible, because GPU particles are not tied to a parent.
- [ ] E. A burst parented to the enemy can be cut off or hidden the instant the enemy is destroyed or hidden, because children go with their parent.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A log line records that the effect started, not that anything was visible.
- B: A one-shot effect plays one cycle and stays finished until it is restarted or spawned again.
- C: A separate effect object has its own lifetime, independent of the enemy.
- D: The cause is the parent-child relationship, not where the simulation runs.
- E: Destroying, hiding or deactivating a parent removes or hides its children too.

**Source:** Triggering and parenting an effect

## MA-ch09.17

An agent measures particle cost in a headless run (no window and no graphics card; the renderer is a dummy that draws nothing) with 50,000 particles of each kind. GPU-simulated particles cost 0.002 ms per frame and CPU-simulated particles cost 1.6 ms per frame. The frame budget at 60 frames per second is 16.67 ms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 1.6 ms for CPU particles is about 9.6 percent of a 60-frames-per-second frame budget (1.6 / 16.67).
- [ ] B. The 0.002 ms figure shows that GPU particles are nearly free on a real graphics card, because the same code ran in the test.
- [ ] C. The CPU figure is meaningless because nothing about a headless run resembles real play, so it cannot be used even as an estimate.
- [ ] D. The GPU figure is a valid prediction for a phone because the code being run is identical to what the phone will run.
- [ ] E. The headless run drew nothing, so it cannot see the cost of drawing the particles, including overdraw.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: 1.6 / 16.67 is about 0.096.
- B: The dummy renderer does no GPU work, so the number is a property of the instrument, not of GPU particles.
- C: CPU simulation really ran on the CPU, so its figure is a usable estimate, to be re-measured on target hardware.
- D: Identical code does not mean identical cost, because the GPU work was never done in the headless run.
- E: Drawing, fill rate and overdraw exist only when a real renderer runs, so this measurement does not include them.

**Source:** Particle cost: evidence versus claim

## MA-ch09.18

In Godot, a developer working on a 2D game asks a coding agent for a death burst using a GPU particle node and its process material (the object that holds speed, direction, spread, gravity and over-life settings). The agent sets the count, the lifetime and a wide spread, and leaves everything else at its defaults. In a test the node reports that it is emitting, yet players see almost nothing. Godot's documentation says that a particle node with no texture draws each particle as a square of 1 × 1 pixels, and that the process material is shared by 2D and 3D particle nodes and has a flag, Disable Z, that stops particles from moving on the z axis. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The node reporting that it is emitting shows the effect was drawn at a visible size, since emitting means particles are on screen.
- [ ] B. With no texture assigned, each particle is a single pixel, which is almost invisible on a typical screen.
- [ ] C. A wide spread in a 2D game keeps the particles' motion inside the visible screen plane, because the game itself is 2D.
- [ ] D. Giving the particles a texture is possible only by switching to the CPU particle node, since GPU nodes draw plain squares.
- [ ] E. Because the material is shared with 3D, the developer should tell the agent to enable Disable Z, so no velocity goes into the axis a 2D view does not show.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: "Emitting" is a state flag and says nothing about particle size or visibility.
- B: By the documentation, a null texture gives 1 × 1 pixel squares.
- C: The material is also built for 3D, so part of each velocity can point along the z axis, where a 2D view cannot show it.
- D: GPU particle nodes also take a texture; the texture is an ordinary property of the node.
- E: The flag removes the z component of motion, which a 2D game needs.

**Source:** Say it to the agent: details a 2D particle node needs
