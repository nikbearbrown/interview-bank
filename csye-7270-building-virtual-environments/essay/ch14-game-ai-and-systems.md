# Chapter 14: Game AI and systems

## ES-ch14.1

A developer gives a coding agent this instruction: "Add enemy AI to the game." Rewrite it as a precise instruction for a guard that patrols, notices the player and chases, using the correct AI terms (including how the guard moves around walls and how it avoids switching rapidly between states), and explain what the agent could build wrongly from the original wording and how you would test the result.

**Points:** 5

**Rubric (1 point each):**

1. Names the decision structure, such as a finite state machine (or behavior tree) with named states such as Patrol and Chase (a Search state is optional), and gives an explicit table of transitions with their conditions.
2. Defines perception precisely: a sight range and a line-of-sight check that walls can block (a field-of-view cone, hearing, and a remembered last known position kept in a blackboard or similar memory, are optional extras).
3. Specifies movement through pathfinding on a grid or navigation mesh with steering and obstacle avoidance, rather than moving in a straight line toward the player.
4. Prevents flicker at state boundaries, for example by using a larger radius to leave Chase than to enter it (hysteresis) or by using timers.
5. Gives a testable contract, such as exposing the current state name so a test can read it, and explains the wrong results the vague wording allows, such as an omniscient straight-line chaser that ignores walls.

**Source:** Saying it to the agent: NPC behavior

## ES-ch14.2

A game has three NPCs: (a) a door guard that patrols, chases and searches, (b) a boss with several phases and many attacks that can interrupt one another, and (c) a villager who balances hunger, tiredness and work through the day. For each, choose among a finite state machine, a behavior tree, utility AI and goal-oriented action planning (GOAP), and defend your choices. Explain how each of the four architectures makes decisions and what it costs.

**Points:** 5

**Rubric (1 point each):**

1. Explains a finite state machine (one current state, transitions on edges between states), its strength with a few distinct modes, and its cost: transitions multiply as states are added.
2. Explains a behavior tree (ticked from the root, nodes return success, failure or running, selectors and sequences, priority by order), its strength in reactive, composable branches, and a cost such as the priority ordering that must be authored and maintained.
3. Explains utility AI (scoring candidate actions from numeric considerations and picking the highest), its strength with continuous competing needs, and a cost such as scores that must be tuned and are hard to predict.
4. Explains GOAP (actions with preconditions and effects, and a planner that searches for a sequence reaching a goal) and gives its trade-off: flexible and emergent sequences, but harder to debug and more costly to run.
5. Assigns an architecture to each of the three NPCs and defends each choice consistently with the architectures as explained, using trade-offs such as designer control, debuggability, authoring effort and run-time cost, rather than naming a single best architecture; any assignment defended this way earns the point (for example a finite state machine or behavior tree for the guard, a behavior tree for the boss, utility AI or GOAP for the villager).

**Source:** FSM, behavior tree, utility AI and GOAP

## ES-ch14.3

A developer tells a coding agent: "Each frame, move the enemy toward the player." In a level with walls the enemy gets stuck against the first wall. Explain why, and describe how pathfinding fixes it. Your answer should cover the difference between a grid and a navigation mesh, how A* chooses its path and what an admissible heuristic does, how steering relates to the path, and one case where pathfinding can fail.

**Points:** 5

**Rubric (1 point each):**

1. Explains that moving straight toward the target ignores obstacles, so the enemy pushes into a wall; reaching a target around walls needs a path computed over a representation of walkable space.
2. Contrasts a grid (cells marked free or blocked, simple, many nodes) with a navigation mesh (polygons covering walkable surface, fewer nodes in open areas, baked from geometry and agent size).
3. Explains A* as a search that expands nodes by f = g + h (cost so far plus estimated remaining cost), and that an admissible heuristic, one that never overestimates, lets it return a shortest path.
4. Explains that the path is a list of waypoints, that steering follows it and handles local avoidance each frame.
5. Names a failure case to handle, such as an unreachable target, a map that has not finished building, a stale navigation mesh after geometry changes, or an agent radius that is too large for a passage.

**Source:** Pathfinding: grid, A*, navmesh and steering

## ES-ch14.4

Design how a guard NPC should see and hear the player. Explain the checks involved in sight, how hearing differs, what the guard should remember, and why an NPC that simply reads the player's position every frame is a poor design. Include one pitfall and how to avoid it.

**Points:** 5

**Rubric (1 point each):**

1. Describes sight as three checks: distance within range, direction inside a field-of-view cone (the dot product of facing and direction to target compared with the cosine of the half-angle), and a line-of-sight test such as a raycast that walls can block.
2. Describes hearing as an event with a position and loudness that NPCs within hearing range react to, often reduced by distance or obstacles, rather than a continuous scan.
3. Describes memory: the last known position or sound location is stored (for example in a blackboard), drives a Search behavior, and expires after a time.
4. Explains that reading the player's position directly makes the NPC omniscient and unfair, breaks stealth gameplay, and removes the point of perception, which exists to limit what the NPC knows.
5. Names a pitfall with a remedy: flicker at the edge of the sight range (fixed with hysteresis), the cost of casting rays every frame (reduce or stagger the checks), or tuning for fairness through playtesting.

**Source:** Perception: sight, hearing and the blackboard

## ES-ch14.5

A developer says: "Our level generator is random, so we cannot test it." Critique this claim. Explain how a seed, determinism and noise work in procedural generation, how constraints and a validator make generated content playable, and what such a validator can and cannot establish.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a pseudo-random generator is deterministic given its seed, so the same seed with the same algorithm produces the same output, and tests can fix seeds and compare results.
2. States what reproducibility requires: all randomness drawn from one seeded generator in a stable order, no clock-based seeds, and awareness that a change in the engine's generator can change results across versions, so data that must persist should be stored.
3. Explains coherent noise (Perlin, simplex or value noise, optionally with several octaves) as smooth variation that suits terrain, in contrast to white noise, which looks like static.
4. Explains constraints and validation: playability rules such as reachability from the player's real jump limits, generate-and-test (reject and re-roll) versus constructive generation, testing many seeds and hand-built bad cases, and keeping a safety margin.
5. Limits what the validator proves: it is a model of the game's rules, so it cannot show that a level is fun or that its model matches the real physics, and human playtests remain necessary.

**Source:** Procedural generation: seed, noise, determinism and constraints

## ES-ch14.6

Explain reinforcement learning at an overview level using an NPC example, defining agent, environment, reward and policy. Describe how reward design can go wrong, how training differs from using the trained NPC in a game, and when a designer would choose reinforcement learning over a scripted state machine or behavior tree.

**Points:** 5

**Rubric (1 point each):**

1. Defines agent (the NPC that acts), environment (the world and its rules that respond to actions), reward (a numeric feedback signal) and policy (the rule mapping observations to actions) with a concrete example.
2. Explains that the agent learns by trial and error from reward rather than from labeled correct answers.
3. Explains that reward design is hard: a reward can be too sparse to learn from, and an agent can exploit a loophole that scores well without doing what the designer meant (reward hacking), so shaping needs care and the result must be inspected.
4. Distinguishes training (many simulated episodes, costly, needs a fast simulator) from deployment (the trained policy typically runs as a fixed decision function in the game, with no learning during play).
5. Compares with scripted AI: RL suits behavior that is hard to hand-script, but designers cannot directly author or easily debug it or guarantee its behavior, so a state machine or behavior tree is the better choice when control and predictability matter.

**Source:** Reinforcement learning overview

## ES-ch14.7

A designer wants a crowd of 100 pedestrians that walk to destinations and avoid bumping into each other. Explain how steering behaviors (such as seek, arrive, separation and obstacle avoidance) and pathfinding divide the work, how the behaviors are combined, what emergent behavior is, and why emergent results are hard to guarantee.

**Points:** 5

**Rubric (1 point each):**

1. Defines steering behaviors as per-frame adjustments to an agent's velocity or force toward a goal or away from hazards, naming examples such as seek, arrive (slow down near the target), separation and obstacle avoidance.
2. Explains the division of labor: pathfinding provides the global route around static obstacles, while steering follows the route and reacts locally to moving things such as other pedestrians.
3. Explains that several steering outputs are combined, for example by a weighted sum, and that the weights are tuned to give the desired balance.
4. Defines emergent behavior as global patterns, such as lanes forming in a crowd, that arise from local rules and interactions without being coded directly.
5. Explains why it is hard to guarantee: outcomes are sensitive to parameters and conditions and cannot be predicted without simulation, so they need testing, measurement and playtesting, and can include unwanted cases such as jams or deadlocks.

**Source:** Steering behaviors and emergent behavior
