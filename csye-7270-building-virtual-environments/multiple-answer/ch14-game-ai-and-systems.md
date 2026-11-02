# Chapter 14: Game AI and systems

## MA-ch14.1

A developer asks a coding agent to implement a guard non-player character (NPC) as a finite state machine (FSM) instead of one large function full of nested if statements. Check each statement that is true about finite state machines. Each statement is worth 1 point (5 points total).

- [ ] A. An FSM has a defined set of states, exactly one of which is current, and rules called transitions for moving between them.
- [ ] B. Each state defines what the guard does while in it, such as patrolling or chasing, keeping the behavior for each mode in one place.
- [ ] C. An FSM lets the guard be in the Chase state and the Patrol state at the same time, which is how it blends behaviors smoothly, such as chasing while patrolling.
- [ ] D. In an FSM, the order of child nodes sets priority, and the whole structure is re-evaluated from a root node per update.
- [ ] E. A guard stuck in Search forever is usually caused by a missing or unreachable transition out of that state, easier to find with a transition table.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: States, a single current state and transitions are what define a finite state machine.
- B: Putting behavior inside states is the main structural benefit over nested conditions.
- C: A finite state machine has exactly one current state; blending behaviors needs a different design.
- D: Ordered children re-evaluated from a root describe a behavior tree, not an FSM.
- E: A stuck state is a problem with the exits from that state, and a transition table makes missing exits visible.

**Source:** Finite state machine

## MA-ch14.2

An NPC has a finite state machine with 6 states. In the worst case any state can move directly to any other, giving n x (n - 1) possible directed transitions for n states. A designer asks for a seventh state, Flee, that can be entered from every other state and can return to every other state. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With 6 states there can be up to 30 directed transitions, because each of the 6 can lead to the other 5.
- [ ] B. With a seventh state the maximum rises to 42 directed transitions, because each of the 7 can lead to the other 6.
- [ ] C. Adding Flee adds 12 transitions in the worst case: 6 leading into Flee and 6 leading out of it to the other states.
- [ ] D. Adding Flee requires editing only the new state, because existing states need no way of reaching it.
- [ ] E. A behavior tree needs the same 12 new connections to add "flee when hurt", since the other behaviors must be able to reach it.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: 6 x 5 = 30.
- B: 7 x 6 = 42.
- C: 42 - 30 = 12, which is 6 entries to Flee plus 6 exits from it.
- D: Each existing state that can be hurt needs a new exit edge into Flee, so many files or states change.
- E: In a behavior tree "flee when hurt" can be one new high-priority branch checked first, with no edges added to the other behaviors.

**Source:** Finite state machine versus behavior tree: where transition logic lives

## MA-ch14.3

A guard's behavior tree is: Selector[ Sequence[CanSeePlayer, Chase], Sequence[HasLastKnownPosition, Search], Patrol ]. Nodes are ticked from the root, left to right. A Selector stops at the first child that does not fail, and a Sequence stops at the first child that does not succeed. On this tick, CanSeePlayer returns FAILURE, HasLastKnownPosition returns SUCCESS, Search returns RUNNING, and Patrol would return RUNNING if it were ticked. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Chase is not ticked on this tick, because the first Sequence stops at its failing first child.
- [ ] B. Patrol is not ticked on this tick, because the Selector stops at the RUNNING second child.
- [ ] C. The root Selector returns RUNNING, passing up the result from the second Sequence.
- [ ] D. The first Sequence returns SUCCESS because its last child, Chase, was skipped and did not report a failure.
- [ ] E. If CanSeePlayer succeeds on the next tick and the tree restarts from the root each tick, the guard switches to Chase with no exit rule in Search.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The first Sequence stops at CanSeePlayer, which fails, so Chase is never reached.
- B: The second Sequence returns RUNNING, and a Selector stops at a child that has not failed, so Patrol is not reached.
- C: Search returns RUNNING, the second Sequence passes it up, and the Selector passes it up to the root.
- D: A Sequence that stops at a failing child returns FAILURE; skipped children do not make it succeed.
- E: The higher-priority branch is checked first on every tick, so it pre-empts Search without Search having to know.

**Source:** Behavior tree: selector, sequence and tick results

## MA-ch14.4

A studio is choosing how its NPCs decide what to do. Check each statement that is true about decision architectures. Each statement is worth 1 point (5 points total).

- [ ] A. Utility AI scores each candidate action with numeric considerations, such as hunger or distance, and picks the highest score.
- [ ] B. Goal-oriented action planning (GOAP) requires the designer to author the exact order of actions for each goal in advance.
- [ ] C. GOAP describes each action by its preconditions and effects and searches for a sequence of actions that reaches a goal state.
- [ ] D. A behavior tree stores its transitions as edges between states, in the same way as a finite state machine does.
- [ ] E. A finite state machine re-ticks from a root node per update, so higher-priority behaviors pre-empt lower ones as it runs.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Utility AI picks by score, and because scores vary continuously the choice can shift gradually.
- B: GOAP's planner finds the sequence; the designer supplies actions and goals, not fixed orders.
- C: Preconditions, effects and a search over action sequences define GOAP.
- D: A behavior tree has no state-to-state edges; its logic is in the order and type of its nodes.
- E: Re-ticking from a root with ordered priority describes a behavior tree; an FSM only checks the exits of its current state.

**Source:** FSM, behavior tree, utility AI and GOAP

## MA-ch14.5

A developer needs a guard that patrols between waypoints, chases the player when it sees them, and searches the last place it saw them when the player is lost. The developer wants an instruction to a coding agent that can be built and tested without the agent guessing. An instruction counts as precise enough only if it gives, as numbers, the distances and times that a test would check. Check each instruction that is precise enough for that purpose. Each statement is worth 1 point (5 points total).

- [ ] A. "Make the guard intelligent: it should patrol between waypoints, notice the player, chase them and then search for them, react in a believable way and feel fair to play against, using the AI approach that works best, and tune the distances and timings so that the encounters feel natural and not cheap."
- [ ] B. "Build a finite state machine with the states Patrol, Chase and Search. The guard chases when it notices the player within about 10 m and searches when it loses them, then patrols again after a while. Use sensible timers, and keep the code tidy."
- [ ] C. "Build a finite state machine with states Patrol, Chase and Search. Patrol to Chase: player within 10 m and visible by a line-of-sight check. Chase to Search: player beyond 14 m or hidden for 2 s. Search to Patrol: 5 s at the last seen position. Expose the current state name as a read-only property."
- [ ] D. "Use machine learning so the guard learns to catch the player over many games, rewarding it for closing distance and for catching the player, and make sure that it does not get stuck or lose the player's trail."
- [ ] E. "Write a behavior tree whose root is a selector trying Chase first, then Search, then Patrol, with a blackboard for the last known position. Give the Chase and Search branches condition checks (Chase when the player is within 10 m), and expose the other distances and timers in the editor with the values left for the designers to fill in later."

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It names no states, conditions or test hook, so the agent decides everything and the result cannot be checked.
- B: "Loses" and "a while" are undefined, only one distance is given, "sensible timers" gives no times, and nothing lets a test read the state.
- C: It gives states, numeric transition conditions, a timer and a readable property, so it can be built and tested as written.
- D: It names no states, conditions or test hook, leaves the training setup unspecified, and promises an untestable guarantee (not getting stuck).
- E: It names the structure and gives one distance, but the other distances and every time are left for the agent to invent, so no test can say what correct behavior is; there is also no readable state to check.

**Source:** Saying it to the agent: a precise NPC behavior instruction

## MA-ch14.6

A guard enters Chase from any other state when the player is within 10 m, and leaves Chase (entering Search) only when the player is farther than 14 m. The player's distance at five consecutive decisions is 9, 11, 9, 11 and 9 m. A second guard uses a single radius of 10 m both to enter Chase and to leave it for Search: it enters Chase from any other state when the player is within 10 m and enters Search from Chase as soon as the player is farther than 10 m. Both guards start in Patrol. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The two-radius guard is in Chase after all five decisions and does not leave it, because 11 m is not beyond 14 m.
- [ ] B. The single-radius guard is in Search after the second decision, because 11 m is outside its 10 m radius.
- [ ] C. The single-radius guard stays in Chase through all five decisions, because it only leaves Chase when the player is out of sight.
- [ ] D. The gap between 10 m and 14 m is called hysteresis, and its purpose is to make the guard move faster.
- [ ] E. After first entering Chase, the two guards change state the same number of times over the five decisions.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The first decision (9 m) enters Chase, and 11 m is not beyond 14 m, so the guard stays.
- B: At 11 m the single-radius guard is outside its 10 m radius and leaves Chase.
- C: It leaves Chase at 11 m and re-enters at 9 m, so it alternates.
- D: Hysteresis means different thresholds for entering and leaving a state; its purpose is to prevent flickering at the boundary.
- E: The two-radius guard makes no further changes, while the single-radius guard changes four more times.

**Source:** Hysteresis in NPC state changes

## MA-ch14.7

Check each statement that is true about steering behaviors and pathfinding for an NPC. Each statement is worth 1 point (5 points total).

- [ ] A. Pathfinding computes a route through the level as a list of points; steering turns it into per-frame motion by adjusting velocity.
- [ ] B. For seek with velocity (2, 0), a target straight along +y and maximum speed 4, desired velocity is (0, 4) and the steering change is (-2, 4).
- [ ] C. Seek alone is enough to get an NPC around a wall that stands between it and its target, because steering knows the layout of the level.
- [ ] D. Arrive is seek that slows down as it nears the target, so the NPC stops on it instead of overshooting.
- [ ] E. Pursue steers toward the target's current position, which is the same thing as seek, since the target is a point in space.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Pathfinding is the global planning step, and steering is the local, per-frame motion that follows it.
- B: Desired velocity is the direction to the target at maximum speed, (0, 4); subtracting the current (2, 0) gives (-2, 4).
- C: Seek heads straight toward the target and has no knowledge of walls, so it pushes into the wall.
- D: Arrive reduces speed inside a slowing radius so the NPC stops at the target.
- E: Pursue predicts where a moving target will be and steers toward that point, whereas seek steers toward where the target is now.

**Source:** Steering behaviors versus pathfinding

## MA-ch14.8

A developer asks a coding agent to make a flock of 200 birds. Each bird follows three local rules: steer away from very close neighbors (separation), match the heading of neighbors (alignment), and steer toward the average position of nearby neighbors (cohesion). No code describes the shape of the flock. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The coordinated movement of the flock is emergent behavior: it arises from simple local rules and is not written down as a global behavior.
- [ ] B. Because the rules are simple, the exact shape of the flock can be predicted without running the simulation.
- [ ] C. Each bird only needs to look at nearby neighbors; no central controller directs the flock.
- [ ] D. Changing the weight of one rule, such as cohesion, can change the flock's overall behavior a lot, so emergent systems need tuning and playtesting.
- [ ] E. Emergent behavior means the AI is defective, because it does something the designer did not code directly, so the rules must have been wrong.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Global patterns that come from local interactions, not from code that describes them, are what emergent behavior means.
- B: Simple rules can produce complex outcomes that are hard to predict without simulation.
- C: Each bird uses only local information, which is why the behavior scales to many birds.
- D: Parameter weights shape the collective result, so designers must test and tune.
- E: Emergence is often the goal, as in flocks and crowds; it is only a defect when the result is unwanted.

**Source:** Steering behaviors and emergent behavior

## MA-ch14.9

A developer needs enemies to navigate a level with walls and furniture. Check each statement that is true about grids, A* and navigation meshes. Each statement is worth 1 point (5 points total).

- [ ] A. A grid and a navigation mesh are two ways of representing walkable space, while A* is a search algorithm that can run on either.
- [ ] B. A navigation mesh covers walkable surface with polygons, so open floor needs far fewer nodes than a grid: 128 x 128 is 16,384 cells.
- [ ] C. A navigation mesh is baked from level geometry and the agent's size, so it must be rebuilt when static geometry changes.
- [ ] D. A larger agent radius shrinks the walkable area of the navigation mesh so the agent's body does not clip walls.
- [ ] E. A* is a representation of walkable space, in the same sense that a grid is, since both are used to store the level and A* does so as a graph of nodes.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Grid and navmesh describe the space; A* is the algorithm that searches over a graph built from either.
- B: A grid stores one node per cell (128 x 128 = 16,384), while a navmesh stores polygons, so open areas are cheap.
- C: The mesh is generated from geometry, so it goes stale when walls move unless it is updated.
- D: Navigation meshes are shrunk by the agent radius so a path keeps the body clear of obstacles.
- E: A* is a search method, not a data structure for the world.

**Source:** Pathfinding: grid, A* and navmesh

## MA-ch14.10

On an empty grid, an NPC at (0, 0) wants to reach (7, 5). A* picks nodes by f = g + h, where g is the cost so far and h is a heuristic estimate of the remaining cost. An admissible heuristic never overestimates the true remaining cost. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With 4-direction movement at cost 1 per step, the Manhattan distance of 12 equals the true cost and is admissible.
- [ ] B. With 8-direction movement (diagonal about 1.414) the true cost is about 9.07, so the Manhattan distance of 12 overestimates and is not admissible.
- [ ] C. An admissible heuristic lets A* return a shortest path.
- [ ] D. Setting h to zero everywhere makes A* behave like Dijkstra's algorithm, which expands nodes by cost so far with no sense of direction.
- [ ] E. A heuristic that overestimates lets A* find shorter paths faster, because it pushes the search toward the goal.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Without obstacles a 4-direction path needs 7 + 5 = 12 steps, matching the Manhattan distance exactly.
- B: Five diagonal steps plus two straight ones cost about 5 x 1.414 + 2 = 9.07, which is below 12.
- C: If h never overestimates, A* cannot skip past the best route.
- D: With h = 0, f equals g, which is Dijkstra's ordering.
- E: Overestimating can make A* faster but it can return a longer path, because it may expand the wrong nodes first.

**Source:** A* and heuristics

## MA-ch14.11

In Godot, a developer says to a coding agent: "Use a NavigationAgent2D so the enemy walks to the player." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent computes the path; the body's own movement code, such as a CharacterBody2D velocity, must follow the next path position.
- [ ] B. Once the agent has computed a path to the target, the enemy counts as having arrived, so its movement code can stop.
- [ ] C. The navigation system applies new navigation data a step after it is added, not instantly, so a path requested in the same frame the level is built can come back empty.
- [ ] D. Calling get_next_path_position() once when the target is set is enough, because the path does not need updating afterwards.
- [ ] E. NavigationAgent2D moves its parent body along the path by itself each physics frame, so no movement code is needed in the enemy's script.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The class reference says the calculation can be used by the parent node to move it; the parent does the moving.
- B: Having a path is not the same as having arrived; the body still has to move along the path, and arrival is judged by how close the body has actually come to the target.
- C: The navigation system batches changes and synchronises them at the end of the physics frame rather than at that instant, so a query made before that can find no path because the map is still empty or not updated.
- D: get_next_path_position() is meant to be called once every physics frame to keep the path logic updated.
- E: The agent does not move the body, so without movement code nothing moves.

**Source:** Navigation agent usage in Godot

## MA-ch14.12

A guard faces along unit vector f. Its vision is a cone with a total field of view of 90 degrees (45 degrees to each side of f) and a range of 12 m. For a unit vector d pointing from the guard to a target, the target is inside the cone angle when dot(f, d) is greater than cos(45 degrees), about 0.707. Target X is 8 m away and 30 degrees off f. Target Y is 8 m away and 60 degrees off f. Target Z is 20 m away straight ahead. Assume there are no walls. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The guard sees X, which is inside the cone and within range.
- [ ] B. Y is inside the cone because it is within the 12 m range and nothing blocks the view.
- [ ] C. Y is outside the cone, because dot(f, d) is about 0.5, which is less than 0.707.
- [ ] D. The guard sees Z because it is straight ahead, in the middle of the cone.
- [ ] E. A complete sight check also needs a line-of-sight test such as a raycast, since cone and range ignore walls.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: cos(30 degrees) is about 0.866, above 0.707, and 8 m is within 12 m, so X is seen.
- B: Being within range is necessary but not sufficient; the angle must also be inside the cone.
- C: cos(60 degrees) is 0.5, below the cone threshold, so Y is outside the field of view.
- D: Z is centered in the cone but 20 m exceeds the 12 m range.
- E: Range and angle say nothing about obstacles, so a raycast or similar test is needed for walls to block sight.

**Source:** Perception: sight cone, range and line of sight

## MA-ch14.13

A guard hears a thrown bottle break 15 m away and out of sight. Designers want the guard to walk to the sound's origin and then return to patrolling. The agent stores the noise position in a blackboard entry named last_known_position. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A blackboard is shared memory that behavior nodes read and write, such as last_known_position, so one node can record what another uses.
- [ ] B. Hearing is usually modelled as an event with a position and loudness that nearby NPCs may react to, not a continuous scan.
- [ ] C. The blackboard is the logic that decides whether the guard searches or patrols, based on what is stored in it.
- [ ] D. If the guard can read the player's position directly from the player object at all times, it is perceiving the player fairly and nothing is being cheated.
- [ ] E. A stored noise position remains valid after the guard has checked it, so the guard does not need to clear or expire it.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A blackboard is a store of facts that nodes share, which decouples the node that senses from the node that acts.
- B: A noise event carries a location and loudness, and listeners within hearing range react to it.
- C: The decision logic lives in the states or tree; the blackboard only holds data.
- D: Reading the player's position directly makes the NPC omniscient, which is why perception systems limit what an NPC can know.
- E: Knowledge goes stale, so it should expire or be cleared once the guard has checked it or a timer runs out.

**Source:** Perception, hearing and the blackboard

## MA-ch14.14

A developer asks an agent for "random terrain". The agent fills a height array by giving every cell an independent random number, and the result looks like static. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Independent random values per cell are white noise: neighboring cells are unrelated, so there are no smooth hills.
- [ ] B. Coherent noise, such as Perlin, simplex or value noise, returns similar values for nearby coordinates and so gives smooth variation.
- [ ] C. Adding more octaves (layers of noise at higher frequency and lower amplitude) mostly removes detail and makes the terrain smoother.
- [ ] D. Coherent noise needs a separate seed per coordinate to give smooth results.
- [ ] E. Coherent noise gives a different value each time the same coordinate is sampled, so terrain built from it cannot be repeated unless the whole height array is saved.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: White noise has no correlation between neighbors, which is why it looks like static.
- B: Coherent noise is smooth by construction, which makes it suited to terrain and clouds.
- C: Extra octaves add finer detail on top of the broad shapes, so the terrain gets more detailed, not smoother.
- D: One seed defines the whole noise field; per-coordinate seeds would break its smoothness.
- E: Noise is a deterministic function of its inputs and seed, so the same coordinate returns the same value.

**Source:** Procedural generation: noise

## MA-ch14.15

A level generator is expected to produce the same level whenever it is given seed 7, and players share seeds with each other. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Seed 7 gives the same level only if all randomness comes from the seeded generator, drawn in the same order, with an unchanged algorithm.
- [ ] B. Seeding from the current clock time keeps levels reproducible, because the clock reading is consistent from run to run.
- [ ] C. Adding a new random call for decorations before the layout code only changes the decorations, and the layout stays the same.
- [ ] D. A seed gives identical levels across engine updates, since the same seed means the same algorithm in the new version.
- [ ] E. A seed makes the output unpredictable, which is why it is called a seed, as in something that grows unpredictably.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A pseudo-random sequence is fixed by its seed, so reproduction depends on using the same generator and drawing values in the same order.
- B: A time-based seed differs on every run, so it gives a different level each time.
- C: An extra draw shifts every later value in the sequence, so the layout changes too.
- D: An engine's generator algorithm is an implementation detail that can change, so data that must persist should be stored, not only the seed.
- E: A seed makes pseudo-random output deterministic and repeatable, not unpredictable.

**Source:** Seed and determinism

## MA-ch14.16

A generator places platforms for a side-scrolling level with random gaps. Playtesters sometimes meet levels they cannot finish because a gap is wider than the player's jump. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A validator that checks reachability using the measured jump limits can detect unfinishable levels, which the generator can re-roll.
- [ ] B. A constructive approach limits each gap, by construction, to the jump distance minus a safety margin.
- [ ] C. Using exactly the measured jump limits with no safety margin is the safest choice, because it matches the true physics of the player's jump exactly.
- [ ] D. Making the generator more random reduces the number of unfinishable levels, since variety spreads out the bad cases.
- [ ] E. A validator is needed only when the generator uses noise, since other generators cannot produce bad levels.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Checking each output against a playability rule and discarding failures is generate-and-test.
- B: Building within the player's limits makes an impossible gap unrepresentable.
- C: With no margin, levels that need frame-perfect jumps or differ slightly from the model pass the validator but frustrate players.
- D: More randomness gives more varied gaps, which if anything produces more unreachable ones.
- E: Any generator can emit an unplayable level, so validation is needed regardless of the randomness source.

**Source:** Procedural generation: constraints and validation

## MA-ch14.17

A team trains an NPC with reinforcement learning (RL) to cross a grid and reach a goal. The NPC gets +1 for reaching the goal, -1 for falling into a pit, and -0.01 for each step. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The NPC is the agent, and the grid world with its rules is the environment.
- [ ] B. The policy is the rule that maps what the agent observes to the action it takes, and training adjusts it to increase the total reward collected.
- [ ] C. The reward is the agent's current location on the grid, which tells it where it is.
- [ ] D. Training needs a labeled dataset giving the correct move for the cells of the grid, which the NPC learns to imitate during training and later during play.
- [ ] E. The small penalty on each step makes shorter paths to the goal earn more total reward.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The agent acts, and everything it acts on and receives observations from is the environment.
- B: A policy is the decision rule, and RL improves it by trial and error to collect more reward.
- C: Location is part of the state or observation; reward is the numeric feedback signal.
- D: RL learns from reward received by acting, not from labeled examples of correct moves.
- E: Each extra step costs 0.01, so a shorter route to the same goal earns more total reward.

**Source:** Reinforcement learning: agent, environment, reward, policy

## MA-ch14.18

An RL agent reaches a goal in 8 steps. The first seven steps each give a reward of -0.01, and the eighth gives +1.0. The return is the sum over steps t = 0, 1, 2, ... of gamma^t times the reward at step t, with gamma = 0.95. A Q-learning update is Q <- Q + alpha x (r + gamma x max Q' - Q). Take Q = 0.5, alpha = 0.1, r = -0.01, gamma = 0.95 and max Q' = 0.8. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The discounted return of the 8-step route is about 0.64, well below the undiscounted sum of about 0.93.
- [ ] B. A 10-step route to the same goal, with nine -0.01 penalties and +1.0 on the tenth step, has a lower discounted return, about 0.56.
- [ ] C. The target value r + gamma x max Q' equals 0.75, which is larger than the current Q of 0.5.
- [ ] D. After the update Q becomes about 0.525, a small move toward the target because alpha is 0.1.
- [ ] E. With gamma = 0 the agent values a reward 8 steps away as much as an immediate reward, since nothing is discounted.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Seven penalties discounted plus 0.95^7 x 1.0 = 0.698 gives about 0.638.
- B: The goal reward is discounted by 0.95^9 (about 0.63) and two more penalties accrue, giving about 0.556.
- C: -0.01 + 0.95 x 0.8 = 0.75.
- D: The error is 0.75 - 0.5 = 0.25, and Q becomes 0.5 + 0.1 x 0.25 = 0.525.
- E: With gamma = 0 every future reward is multiplied by zero, so only the immediate reward counts.

**Source:** Reinforcement learning: return and Q-learning update
