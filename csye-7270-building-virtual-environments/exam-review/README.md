# CSYE 7270 exam cheat sheet and topic-selection worksheet

**Status: proposal for Nik's review — no exam topics or questions have been selected.** Updated November 3, 2026.

This is a study guide and a way to decide what belongs on the game-class exam. “Cheat sheet” means a review aid here; permission to bring notes into the exam is **not yet decided**. The worked examples below are newly written practice examples, not a released exam or confidential exam questions. Their answers are included for studying.

The course is **CSYE 7270: Building Virtual Environments**, in its Godot edition. The emphasis is understanding game-development terms well enough to specify a change to a coding agent, predict its behavior, and verify the result. Unity and Unreal comparisons are candidate extensions, not assumed requirements.

## Start here: what might be on the exam?

Discuss these twelve areas first. Each is still **undecided**:

1. Engine vocabulary; scenes, nodes, signals, reusable objects, and the toolchain.
2. Game art and sound assets; sprite sheets, rigs, and import requirements.
3. Blender-to-engine workflows; transforms, dimensions, origins, UVs, and export verification.
4. Collision and physics; solid bodies versus triggers, body types, layers, and masks.
5. Game design documents; player goals, mechanics, constraints, and testable requirements.
6. Shaders, materials, and textures; shader stages, uniforms, UVs, and surface properties.
7. Shader verification; controlled comparisons, timing, shared resources, and visual evidence.
8. Particle effects; emission, lifetime, bursts, trails, and rendering cost.
9. Animation and interaction; keyframes, skeletal animation, state transitions, and hit timing.
10. Audio and triggers; event wiring, buses, spatial sound, and listening checks.
11. Profiling and game AI; frame budgets, bottlenecks, navigation, and decision systems.
12. MCP and coding agents; tool contracts, permissions, project scope, failure recovery, and evidence.

The [current question pool](../README.md) covers engine vocabulary and chapters 0–14, plus five agent-workflow supplements. Chapter 15's final project is outside that pool's current scope. That boundary is a **starting proposal**, not a decision about this exam. Course coverage must be confirmed before selecting questions, especially if this is a midterm rather than a cumulative exam.

## Topic map: concepts, example prompts, and a place to decide

Every row is a candidate. Mark **Include / Narrow / Defer / Exclude** and add a reason during review. Links open existing practice material; they do not designate questions for the exam.

| Candidate area | Study concepts | Example topic to discuss | Practice source | Decision |
|---|---|---|---|---|
| Vocabulary and toolchain | Engine, editor, runtime, scene instance, resource; code change versus working game | What evidence shows an agent changed the intended project and that the change works? | [Vocabulary](../multiple-answer/00-engine-vocabulary.md), [Ch. 0](../essay/ch00-the-toolchain.md) | Undecided |
| Scenes, nodes, and signals | Composition, parent/child transforms, reusable scenes, event communication | Explain how a switch can notify a door without embedding all door behavior in the switch. | [Ch. 1](../essay/ch01-scenes-nodes-and-signals.md) | Undecided |
| Art and sound assets | Sprite versus sprite sheet; dimensions, transparency, loops, consistency, provenance | Turn “make a character” into a usable sprite-sheet specification. | [Ch. 2](../essay/ch02-game-art-and-sound-assets.md) | Undecided |
| Blender and 3D assets | Mesh, material, UV, origin, local/world transform, scale, rig, export | A prop looks correct in Blender but is huge in the game. What should be measured and checked? | [Ch. 3](../essay/ch03-3d-assets-and-the-blender-pipeline.md) | Undecided |
| Collision and physics | Trigger versus blocker; static, simulated, and code-controlled bodies; layer versus mask | Specify a pickup that detects the player, adds score once, and never blocks movement. | [Ch. 4](../multiple-answer/ch04-scenes-collision-and-physics.md) | Undecided |
| Game design documents | Core loop, mechanics, player feedback, constraints, acceptance criteria | Replace “make combat fun” with a bounded interaction and checks; identify what still needs human playtesting. | [Ch. 5](../essay/ch05-game-design-documents-and-virtual-worlds.md) | Undecided |
| Shader foundations | Vertex versus fragment work; uniforms; UV; elapsed time; alpha | Choose shader stages for bending a mesh and coloring a dissolve edge. | [Ch. 6](../essay/ch06-shader-foundations.md) | Undecided |
| Materials and textures | Shader versus material; albedo, roughness, metallic, normal maps; shared resources | Why does a normal map change the lighting response without changing the silhouette? | [Ch. 7](../essay/ch07-materials-and-textures.md) | Undecided |
| Shader verification | Baseline, fixed camera, controlled inputs, event timing, per-instance state | The shader compiles. What would still be needed to show the intended enemy flashes at the intended time? | [Ch. 8](../essay/ch08-shader-verification.md) | Undecided |
| Particles | Emission rate, lifetime, one-shot burst, local/world space, transparency and overdraw | Why can a small number of large transparent smoke particles be expensive? | [Ch. 9](../essay/ch09-particle-effects.md) | Undecided |
| Animation foundations | Keyframes, interpolation, tracks, skeletal animation, forward/inverse kinematics | Explain how an animation clip and a gameplay hit window should agree. | [Ch. 10](../essay/ch10-animation-foundations.md) | Undecided |
| State and interaction | States, transition conditions, priority, interruptibility, event timing | What happens if the character takes damage during an attack? Specify and test that transition. | [Ch. 11](../essay/ch11-animation-and-interaction.md) | Undecided |
| Audio | Trigger event, audio stream/player, mixer bus, spatial attenuation, clipping | A sound file loads but no hit is audible. Trace the event-to-output path. | [Ch. 12](../essay/ch12-audio-and-triggers.md) | Undecided |
| Profiling | Frame time versus FPS; CPU/GPU bottlenecks; controlled measurement | At a target of 60 FPS, does a measured 20 ms frame meet the budget? What should be investigated next? | [Ch. 13](../essay/ch13-profiling-and-optimization.md) | Undecided |
| Game AI | State machine, behavior tree, sensing, path planning, steering | A guard has a path to the player. What else is needed for it to decide when and how to chase? | [Ch. 14](../essay/ch14-game-ai-and-systems.md) | Undecided |
| MCP fundamentals | Host/client/server roles; tools, resources, prompts; discovery and schemas | A tool reports success. Which parts of the requested game behavior remain unverified? | [MCP](../multiple-answer/01-mcp-fundamentals.md) | Undecided |
| Agent security and recovery | Least privilege, untrusted input, checkpoints, idempotency, uncertain results | A create-object call times out. Why might retrying immediately create duplicates? | [Security](../essay/04-agent-security.md), [Verification](../essay/05-agent-verification.md) | Undecided |
| Unity/Unreal comparison | Shared concepts versus engine-specific object models; instance versus shared asset | Translate one behavioral requirement between engines without pretending their APIs are identical. | [Unity](../essay/02-unity-agent-workflows.md), [Unreal](../essay/03-unreal-agent-workflows.md) | Undecided; optional extension |

## Compact concept cheat sheet

| Remember | Explain the distinction |
|---|---|
| Scene / instance / resource | A saved scene can be instantiated repeatedly. A shared resource can affect several objects when edited. Check whether a change is intended for one instance or all users of the resource. |
| Node / signal | Nodes organize behavior and scene structure. A signal communicates an event; a connected receiver decides how to respond. |
| Sprite sheet / skeletal rig | A sprite sheet stores image frames. A rig defines bones and relationships used to pose a character or deform a mesh. |
| Mesh / material / texture | A mesh supplies geometry; a material configures rendering; a texture supplies sampled data. A texture need not contain color. |
| Origin / transform / coordinate space | An origin is a reference point. Position, rotation, and scale are transforms. Local values are relative to a parent; world values describe placement in the scene. |
| Collider / trigger | Blocking and overlap detection are different requirements. In Godot an Area detects overlaps; a solid physics body supplies blocking behavior. |
| Collision layer / mask | A layer describes membership; a mask selects layers to detect. For an Area detecting a body, the body's layer must be included in the Area's mask. |
| Static / rigid / character body | Static bodies suit fixed obstacles; rigid bodies are simulation-driven; character bodies are code-controlled. Do not assume character gravity is automatic. |
| Vertex / fragment shader | Vertex work can change mesh positions. Fragment work computes surface output for fragments. A normal map affects shading, not the mesh silhouette. |
| Uniform / varying | A uniform is supplied from outside the shader for a draw. A varying carries values between shader stages, normally interpolated across a primitive. |
| Albedo / roughness / metallic / normal | Albedo provides base surface color; roughness controls microfacet scattering; metallic changes the material response; normal data changes the shading direction. |
| Alpha blending / discard | Blending mixes with the existing image and makes ordering relevant. Discard removes fragments; it does not create partial transparency. |
| Animation / state machine | Animation changes values over time. A state machine decides which behavior is active and which transitions are allowed. |
| Path planning / steering / decision | A path identifies a route; steering controls movement along or around it; decision logic chooses a goal or action. |
| MCP / model / permissions | MCP describes an integration interface. A model proposes actions. Operating-system and application controls determine what those actions can access; the protocol alone is not a sandbox. |
| Success / evidence | A successful tool response is evidence about that call. Inspect state, run relevant checks, and play or listen where needed before claiming the feature works. |

Useful calculations, with assumptions stated:

- **Frame budget:** `1000 / target FPS` milliseconds. At 60 FPS, the budget is about **16.67 ms**; 20 ms per frame corresponds to **50 FPS**.
- **Time-based progress:** `clamp(elapsed_seconds / duration_seconds, 0, 1)`. A fixed number of rendered frames has different durations at different frame rates.
- **Steady-state particle estimate:** `emission rate × lifetime`, for constant emission, fixed lifetime, and no extra cap or early removal. At 80 particles/second and 1.5 seconds, expect about **120 live particles** after startup. This estimates count, not GPU time.
- **Scale example:** if the supplied import contract uses 1 world unit = 1 meter, a 2-meter prop should measure 2 world units. State the unit contract instead of assuming every engine/importer shares one.

When answering a scenario, use: **name the concept → state the intended behavior → explain the mechanism → give a check → identify what the check cannot prove**.

## Worked practice examples — not selected exam questions

The question bank uses five-point multiple-answer questions and five-point essays. For multiple-answer items, each of five statements is independently true or false: checking a true statement or leaving a false statement unchecked earns one point. A wrong choice earns zero for that statement. Essays use five rubric items. These are the bank's existing conventions; the actual exam's format, length, and scoring remain undecided.

### Example A — collision and a precise agent request

**Scenario:** In a Godot 2D game, a checkpoint should activate when the player enters it, without blocking the player. The player is on layer 2 and enemies are on layer 3. The checkpoint is an Area2D with a collision shape and a mask that scans only layer 2. Assume normal overlap monitoring and a correctly connected handler.

Mark every true statement:

- [ ] A. The Area2D can detect the player without physically blocking it.
- [ ] B. Its mask includes enemies on layer 3 merely because their sprites overlap it.
- [ ] C. Its own layer and its detection mask describe different things.
- [ ] D. A useful test checks entry, absence of blocking, and the resulting checkpoint state.
- [ ] E. A visible checkpoint image is sufficient; collision detection does not need a shape.

<details>
<summary>Practice key and explanations</summary>

**A=T, B=F, C=T, D=T, E=F.** An Area senses overlaps rather than blocking. The mask scans the player's layer, not the enemy layer. Layer membership and detection selection are separate. Behavior must be observed, and a sprite is not a substitute for the physics shape.

</details>

### Example B — shader timing and shared state

**Scenario:** An enemy should flash red for 0.5 seconds when hit. An agent subtracts a fixed amount from the flash strength each rendered frame and writes that strength onto a material shared by all enemies.

**Prompt:** Explain the two design problems and propose a repair and a verification plan.

<details>
<summary>Practice rubric — five points</summary>

1. Fixed per-frame changes make duration depend on frame rate.
2. Measure seconds since the hit, compute clamped progress, and drive the fade from that value.
3. A parameter change on the shared material can affect other enemies.
4. Use an appropriate per-instance parameter or an independent material where required; define what another hit does to the timer.
5. Compare timing at two frame rates and hit two enemies at different times; verify duration, independence, and return to the baseline appearance. Compilation alone does not demonstrate those properties.

</details>

### Example C — profiling and particles

**Scenario:** A target is 60 FPS. A repeatable scene measures 20 ms per frame. Smoke emits 80 particles per second, each lasting 1.5 seconds; assume constant emission, steady state, and no early removal or limiting cap.

Mark every true statement:

- [ ] A. The target frame budget is about 16.67 ms.
- [ ] B. A 20 ms frame meets the 60 FPS target.
- [ ] C. About 120 smoke particles are alive at steady state under the stated assumptions.
- [ ] D. The count alone proves that smoke is the bottleneck.
- [ ] E. A controlled before/after measurement can help test whether a smoke change improves frame time.

<details>
<summary>Practice key and explanations</summary>

**A=T, B=F, C=T, D=F, E=T.** `1000 / 60 ≈ 16.67`; `1000 / 20 = 50 FPS`; `80 × 1.5 = 120`. Count does not establish cost: screen coverage, shaders, overdraw, and other work matter. Compare equivalent scenes and identify the measured CPU/GPU work before assigning cause.

</details>

### Example D — animation and interaction

**Scenario:** An attack animation lasts 0.6 seconds. The game design requires damage only between 0.2 and 0.3 seconds. Taking damage interrupts the attack. An interrupted attack must not keep damaging nearby enemies.

**Prompt:** Describe the state transition and the checks you would ask an agent to implement.

<details>
<summary>Practice rubric — five points</summary>

1. Distinguish the attack animation from the gameplay state and damage window.
2. Enable damage only during the specified window while the attack remains active.
3. Define an attack-to-hurt transition and close the damage window immediately when interrupted.
4. Specify permitted behavior for repeated input and restarting an attack, rather than leaving it implicit.
5. Test before, during, and after the window, including an interruption within it and a later new attack; inspect both visible animation and actual damage events.

</details>

### Example E — MCP, an uncertain outcome, and verification

**Scenario:** An agent calls an editor tool to create one checkpoint. The request times out. The tool contract does not promise that a timeout means the edit was rolled back, and repeating the call can create another object.

Mark every true statement:

- [ ] A. The timeout proves that no checkpoint was created.
- [ ] B. Inspecting the intended project and scene can help determine whether the edit happened.
- [ ] C. An immediate blind retry can create duplicates.
- [ ] D. An MCP connection automatically restricts the server to a safe project folder.
- [ ] E. Once the outcome is resolved, the checkpoint still needs behavior and persistence checks.

<details>
<summary>Practice key and explanations</summary>

**A=F, B=T, C=T, D=F, E=T.** The outcome is uncertain until checked. Inspect before retrying a non-idempotent edit. Permission and filesystem boundaries depend on the deployment. Verify the checkpoint's behavior and that the intended saved scene retains it after reopening.

</details>

### Example F — game AI and an acceptance test

**Scenario:** A guard should patrol, chase only after detecting the player, and return to patrol after losing the player for a specified delay. A navigation system can produce paths through walkable space.

**Prompt:** Explain why navigation alone is insufficient, and specify a small test plan.

<details>
<summary>Practice rubric — five points</summary>

1. Distinguish finding a route from deciding whether to chase.
2. Define patrol and chase states, plus a return/search behavior if the design needs one.
3. Define what detection and losing the player mean, including the supplied delay.
4. Handle unreachable goals or a missing route without claiming successful pursuit.
5. Test acquisition, loss, reacquisition, and an obstructed/unreachable target; assess movement and transitions as well as path output.

</details>

## Decisions to make together before assembling an exam

- [ ] Confirm whether this is a midterm or cumulative exam, and the last taught chapter/topic.
- [ ] Mark each topic-map row Include, Narrow, Defer, or Exclude; specify boundaries for broad rows.
- [ ] Decide how much of the newly added MCP, security, and recovery material students have actually been taught.
- [ ] Decide whether Unity/Unreal appear only as conceptual comparisons, as fully specified scenarios, or not at all.
- [ ] Choose the balance of terminology, applied debugging, calculations, and design/verification explanations.
- [ ] Decide duration, question count, total points, and whether to retain the bank's five-point formats. No values are fixed here.
- [ ] Decide whether notes, this sheet, engine access, documentation, calculators, or AI tools are allowed. Publishing a study guide does not grant exam-time permission.
- [ ] Set topic weights only after scope is agreed; ensure weights total 100% and the workload fits the allotted time.
- [ ] Review every proposed question for ambiguity, assumed engine behavior, adequate scenario information, and an answerable rubric.
- [ ] Separate the eventual selected exam and answer key from this public practice document; this README remains a study/proposal artifact.

Suggested discussion sequence: choose **coverage first**, then **depth and format**, then **particular questions**. For each included topic, ask for a definition, one common confusion, a concrete behavior, and evidence that distinguishes success from failure.

## Sources and current pool

This README adds a review aid; it does not edit the question pool or change course grading policy.

- [Question-pool README](../README.md): scope, formats, counts, and validation limits. At source commit [`f5c04c5`](https://github.com/nikbearbrown/interview-bank/tree/f5c04c50773b323e474489d45228e61552375682/csye-7270-building-virtual-environments), the pool contains **366 multiple-answer questions and 159 essays (525 total)**. The latest addition supplies 60 multiple-answer questions and 40 essays about MCP and agent workflows.
- [Course chapter map](https://github.com/nikbearbrown/csye-7270-building-virtual-environments/blob/0240fcd07d6d8443c8a3de8d02f50ff9fbcdba4e/chapters/README.md) and [module map](https://github.com/nikbearbrown/csye-7270-building-virtual-environments/blob/0240fcd07d6d8443c8a3de8d02f50ff9fbcdba4e/modules/README.md): identify the Godot course and its conceptual progression. These course materials label themselves review drafts; they are evidence of the proposed curriculum, not proof of what has been taught or approved for examination.
- [MCP and agent-workflow sources](../SOURCES.md): research context and mappings for the supplementary pool. Product versions, beta status, exact commands, and port numbers are not proposed memorization topics here.

**Review note:** Drafted with Codex from the repository materials. The six worked examples are original practice scenarios for this review sheet. Their arithmetic, keys, and rubrics were checked during preparation, but Nik must review subject coverage and wording before adopting any question for an exam.
