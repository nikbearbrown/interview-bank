# CSYE 7270 exam cheat sheet and topic-selection worksheet

**Status: proposal for Nik's review — no exam topics or questions have been selected.** Updated November 3, 2026.

This is a study guide and a way to decide what belongs on the game-class exam. “Cheat sheet” means a review aid here; permission to bring notes into the exam is **not yet decided**. The worked examples below are newly written practice examples, not a released exam or confidential exam questions. Their answers are included for studying.

The course is **CSYE 7270: Building Virtual Environments**. **Nik's confirmed framework is generic across Godot, Unity, and Unreal:** understand the concepts, choose tools for the job, explain tradeoffs and integration, and use coding agents throughout. Engine names provide examples of implementations, not the organizing structure or a requirement to memorize one engine's menus. Exam inclusion, depth, weighting, and individual questions remain undecided.

**AI-assisted development is a thread through every topic.** Here MCP means Model Context Protocol. An agent can help inspect a project, propose a bounded change, invoke available tools, and collect evidence. Its actual abilities depend on the installed tools, permissions, engine version, and project. Do not assume that a connector available today or in three months exposes every operation in every engine. Students should be able to describe the desired behavior and how to check it even when tool names change.

## Start here: proposed high-level topics

1. **Game-development tools and engine choice:** what games need; options, strengths, weaknesses, and integration with Godot, Unity, and Unreal.
2. **Scenes, nodes, objects, and components:** hierarchy, transforms, reusable structures, and events.
3. **2D art:** sprites, sprite sheets, image tools, import settings, and consistency.
4. **3D assets:** meshes, modeling tools, scale, origins, export, and import.
5. **Collision and physics:** colliders, triggers, body motion, collision filtering, and simulation.
6. **Game design and rapid prototyping:** ideation, core loops, hypotheses, small prototypes, and playtesting.
7. **Textures, materials, shaders, and UVs:** information maps, rendering behavior, 3D surface-to-2D mapping, and verification.
8. **Particle effects:** what they are, when to use them, how to control them, and their cost.
9. **Animation:** sprite-sheet animation, rigs, skeletal animation, timing, and state machines.
10. **Audio:** recording, editing, mixing, and export—especially Audacity—then playback and events in the engine.
11. **Profiling:** equivalent measurement and diagnosis in all three engines.
12. **Game AI:** navigation, sensing, decisions, and native or first-party capabilities in each engine.

**Across all twelve:** precise agent instructions, MCP/tool contracts where available, scoped changes, evidence, failure recovery, and human judgment. Coding-agent workflows are not a separate topic to memorize and then forget during the art, physics, or audio questions.

The [existing question pool](../README.md) contains vocabulary, chapters 0–14, and agent-workflow supplements. Its chapter labels and some questions remain Godot-oriented; use them as source material to adapt into this generic framework, not as the final exam syllabus. The pool currently excludes chapter 15's final project. Confirm taught coverage and the midterm/cumulative boundary before selecting questions.

## Topic map: concepts, agent work, and evidence

Every row remains **undecided for exam selection**. During review mark Include / Narrow / Defer / Exclude. The generic framework is confirmed; this table does not finalize coverage.

| Candidate area | Concepts and tool options | Agent-assisted practice prompt and verification | Existing practice material |
|---|---|---|---|
| Tools and engines | Authoring versus runtime; Godot, Unity, Unreal; external editors, version control, export/build tools | Ask an agent to inventory requirements and integrations; defend a tool choice and prove a small end-to-end handoff. | [Vocabulary](../multiple-answer/00-engine-vocabulary.md), [Ch. 0](../essay/ch00-the-toolchain.md) |
| Scenes and nodes | Hierarchies, objects/components, local/world transforms, instances, events | Specify a switch and door; have the agent inspect references, make one bounded change, and show which instance responds. | [Ch. 1](../essay/ch01-scenes-nodes-and-signals.md) |
| 2D art | Sprites, sprite sheets, atlas regions, pivots, alpha; pixel/raster/vector editors and generation | Specify a walk sheet's frame dimensions, ordering, pivot, timing, and transparency; verify cropping and visible motion after import. | [Ch. 2](../essay/ch02-game-art-and-sound-assets.md) |
| 3D assets | Meshes, modeling/sculpting tools such as Blender or Maya; scale, origin, topology and export | Ask for a measured prop and an explicit export contract; verify dimensions, orientation, and geometry in the receiving engine. | [Ch. 3](../essay/ch03-3d-assets-and-the-blender-pipeline.md) |
| Physics and triggers | Collision shapes, simulated/code-driven motion, overlap versus blocking, filtering and time steps | Have an agent build a nonblocking pickup; check intended entrants, one-time scoring, and absence of blocking. | [Ch. 4](../multiple-answer/ch04-scenes-collision-and-physics.md) |
| Ideation and prototyping | Paper prototypes, grayboxing, GDD, core loop, hypotheses, constraints | Ask for three mechanic variations and one tiny prototype; change one variable and collect playtest evidence before adding polish. | [Ch. 5](../essay/ch05-game-design-documents-and-virtual-worlds.md) |
| Textures, materials, shaders and UVs | 2D data maps, surface parameterization, shader stages, material parameters, normal/roughness maps | Ask the agent to diagnose a stretched checkerboard and a shared flash effect; inspect UVs, parameter scope, timing and rendering. | [Ch. 6](../essay/ch06-shader-foundations.md), [Ch. 7](../essay/ch07-materials-and-textures.md), [Ch. 8](../essay/ch08-shader-verification.md) |
| Particles | Emitters, rate, lifetime, bursts, trails, spaces, transparency and overdraw | Specify sparks as visual feedback; verify the trigger, duration, count and frame cost rather than accepting a screenshot alone. | [Ch. 9](../essay/ch09-particle-effects.md) |
| Animation and state | Frame sequences, keyframes, rigs, skin weights, clips, transitions and interrupts | Ask the agent to synchronize a swing and damage window; test repeated input, interruption, and return to idle. | [Ch. 10](../essay/ch10-animation-foundations.md), [Ch. 11](../essay/ch11-animation-and-interaction.md) |
| Audio and Audacity | Record/import, trim, fades, level control, loops, export; engine playback, buses and spatial sound | Give the agent an editing/export brief and event contract; inspect the exported file and listen in-game for clicks, clipping and duplicate playback. | [Ch. 12](../essay/ch12-audio-and-triggers.md) |
| Profiling | Frame time, CPU/GPU work, allocations, physics and rendering; each engine's measurement tools | Ask the agent to capture a baseline, identify a bottleneck, change one cause, and repeat the same test on the target device. | [Ch. 13](../essay/ch13-profiling-and-optimization.md) |
| Game AI | Sensing, decisions, pathfinding, steering, behavior trees/state machines; engine versus package capability | Ask the coding agent to assemble a patrol/chase behavior using verified capabilities; test perception loss, unreachable goals and state recovery. | [Ch. 14](../essay/ch14-game-ai-and-systems.md) |

Use the [MCP](../multiple-answer/01-mcp-fundamentals.md), [security](../essay/04-agent-security.md), [verification](../essay/05-agent-verification.md), [Unity](../essay/02-unity-agent-workflows.md), and [Unreal](../essay/03-unreal-agent-workflows.md) banks to add relevant workflow questions **inside these topics**. Examples: inspect before retrying an uncertain scene edit, keep an asset conversion inside its allowed folder, and distinguish a successful import call from a correct animated character.

## Revised framework: what tools do you need to build games?

Start with the game and the team: 2D or 3D, visual style, player interactions, target devices, performance budget, collaboration needs, existing skills, and resources. Then identify the capabilities needed. A small game may use one tool for several jobs; a larger project may need specialized tools. Naming products alone is not an explanation of a development workflow.

| Capability needed | Options to compare | Strengths, weaknesses, and the handoff to test |
|---|---|---|
| Design and specification | Written GDD, diagrams, spreadsheets, paper or engine prototypes | Documents make intent explicit but do not demonstrate play; prototypes expose behavior but can hide assumptions. Carry requirements and acceptance checks into the engine. |
| Images, UI, and textures | Raster/vector editors, pixel-art tools, texture-painting tools, generative-image tools; examples include Krita, Photoshop, and Blender | Direct editing gives control; generation can supply candidate assets but may need cleanup and consistency checks. Deliver supported images with appropriate resolution, transparency, color/data interpretation, and reuse rights. |
| Models, rigs, and animation | Blender, Maya, procedural modeling, engine modeling/animation tools | External authoring can provide detailed control and reusable source assets; export introduces another boundary. Check mesh topology, units, axes, rig, animation, UVs, and which materials survive. An offline render does not establish runtime performance. |
| Sound and music | Recording, audio editors, DAWs, synthesis/generation; examples include Audacity and REAPER | Editing and mixing give control over timing and layers; a finished audio file does not provide gameplay triggers or adaptive behavior. Export an engine-supported format, then check looping, buses, spatial playback, and runtime cost. |
| Gameplay, rendering, and interaction | Godot, Unity, Unreal; scripts, visual scripting, engine systems, or plugins | Engine systems reduce the amount to build, but impose object models, APIs, and rendering conventions. Compare the specific project's needs and team skills, then test a representative playable slice. |
| Coding and automation | IDEs, command-line tools, coding agents, editor scripting, MCP bridges | Automation can repeat edits and checks; generated code and tool calls still require review. An editor plugin needs the right engine API and version; an MCP connection does not translate one engine's object model into another's. |
| Collaboration, testing, and delivery | Version control, asset storage, issue tracking, profilers, automated tests, playtesting, build tools | Text diffs help code review; large binary art assets need a deliberate storage/merge workflow. Automated tests cover defined behavior; play and listening checks cover experience. Verify builds on the intended device, not just in the editor. |

The examples name possible categories and tools, not a required shopping list. Evaluate the chosen tool's actual output and integration, rather than assuming every feature transfers because an export button exists.

### Compare the engines against the same requirements

These are reasoned tradeoffs to discuss, not a ranking or a claim that one engine cannot make a particular genre. Capability facts are supported by the linked official documentation; project suitability is an inference to test with a prototype.

| Engine | Strengths to consider | Weaknesses or costs to consider | External-tool fit |
|---|---|---|---|
| Godot | Integrated 2D/3D workflows and an open-source engine can suit a team that values inspecting and adapting its tools. | The team still has to learn Godot's scene/resource model; an export dependency or unsupported target workflow can outweigh a convenient editor. Verify the required platform and plugin support. | Godot recommends glTF for 3D scenes. Its direct `.blend` workflow invokes Blender to export glTF, so it requires Blender on the importing machine; native-file convenience adds a dependency. [Engine overview](https://docs.godotengine.org/en/stable/about/introduction.html), [3D formats](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html), [export setup](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html). |
| Unity | C# scripting can fit a C#-experienced team; configurable rendering pipelines offer choices for different rendering requirements. | Pipeline choice brings compatibility work: assets and shaders must match it. Existing C# skills help, but do not eliminate learning Unity's APIs or rewriting code from another engine. | Check the selected importer, packages, and render pipeline. A texture image may remain useful while its original material/shader implementation needs rebuilding. [C# workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-get-started.html), [render-pipeline compatibility](https://docs.unity3d.com/6000.1/Documentation/Manual/srp-setting-render-pipeline-asset.html). |
| Unreal | Blueprint supports visual behavior authoring and iteration; C++ provides lower-level control and integration with external systems. The two can be combined. | Large Blueprint graphs can become difficult to manage; C++ adds programming and build complexity. Blueprint execution overhead matters in some workloads, so profile before rewriting. | Import supported source assets into Unreal assets and inspect the result. External art is different from an Unreal Blueprint or engine-specific plugin: those behaviors require Unreal's systems or a port. [Blueprint/C++ tradeoffs](https://dev.epicgames.com/documentation/en-us/unreal-engine/coding-in-unreal-engine-blueprint-vs-cplusplus), [asset import](https://dev.epicgames.com/documentation/unreal-engine/importing-assets-directly-into-unreal-engine?lang=en-US). |

### Explain why a tool fits — or why it does not

For each handoff, identify **the output → the receiving interface → what survives → what needs adaptation → a verification check**. Distinguish an unsupported feature from a whole tool being unusable.

- **Asset interchange:** A Blender mesh can fit through a supported exporter/importer. Check scale, axes, UVs, rig and animation after import. A procedural authoring setup may need to be baked into geometry/textures or reconstructed; do not assume a file carries every authoring feature.
- **Format limits:** Godot's documented OBJ path does not carry skeletons or animations. Thus OBJ can be a poor choice for an animated character even when it is adequate for a static prop. Choosing a richer supported format changes the fit; the problem is not “Blender cannot work with the engine.” [Godot format limits](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html).
- **Materials and code:** A reusable image or mesh is different from a shader graph, Blueprint, Godot script, or Unity component. Engine APIs and render-pipeline conventions determine whether behavior must be translated, rebuilt, or replaced.
- **Plugins and automation:** Check engine/version support, installation dependencies, target-platform support, available operations, and access scope. A bridge that can edit one editor is not automatically a bridge for all three engines.
- **Technical versus practical fit:** A technically importable asset may still exceed the frame budget, fail visual requirements, or be impractical to maintain. Explain the particular constraint and test it with an exported playable build.

## Compact concept cheat sheet

| Remember | Generic meaning and useful distinctions |
|---|---|
| Scene / hierarchy / instance | A scene or level organizes objects, relationships and settings. A reusable definition can produce instances. Engines package these concepts differently; changing a shared definition can affect more than one instance. |
| Node / object / component | A node is an element in a tree or graph. Scene-hierarchy elements and shader/behavior-graph nodes are different uses of that word. Engines may attach behavior as components rather than representing every behavior as a scene node. |
| Events | One object reports something happened; another responds. Godot signals, Unity events/callbacks and Unreal delegates/events are engine examples, not identical APIs. |
| Sprite / sprite sheet / atlas | A sprite displays a 2D image or image region. A sprite sheet contains multiple regions, often animation frames. An atlas packs regions for reuse/rendering; not every atlas is an animation. |
| Mesh / transform | A mesh contains geometry. Transforms specify position, rotation and scale in a coordinate space. The origin affects operations such as rotation; local coordinates depend on a parent. |
| Texture / material / shader | A **2D texture is a sampled map of information**: color, roughness, a mask, encoded normals, or other data. A **material** describes how a surface is rendered, supplying parameters/textures and selecting or defining shading behavior. A **shader** is the computation used to produce that behavior. A material is not itself just a 2D map. Engines package material graphs and shader programs differently. |
| XYZ / UV | XYZ locates geometry in 3D; UV addresses a 2D texture. Unwrapping assigns surface corners to 2D coordinates, creating islands and seams. This is a surface parameterization, not one universal XYZ-to-UV formula. A shared 3D position can have different UVs at a seam. |
| Collider / trigger | A collider provides a shape for collision queries or simulation. Solid contact can block/respond; a trigger/overlap region reports interaction without that blocking response. The visible mesh or sprite need not equal the collision shape. |
| Motion and filtering | Distinguish static obstacles, physics-simulated bodies and deliberately code-driven movement. Filters choose which pairs interact. Layers/masks, collision matrices, and channels/responses express related ideas with different rules; consult the chosen engine. |
| Physics update | The simulation advances in steps, integrating motion and resolving constraints/contacts. Rendering and simulation rates can differ. Specify movement ownership and avoid having simulation and custom code fight over the same transform. |
| Shader stages / parameters | Vertex work can move vertices; fragment/pixel work computes surface output. Parameters can connect gameplay events to rendering. Shared material state must be distinguished from per-instance state. |
| Normal map / geometry | A normal map changes shading directions; it does not by itself change the silhouette. Displacement actually changes geometry when the chosen rendering approach supports it. |
| Particle effect | Many lightweight elements evolve under emission and lifetime rules to depict smoke, sparks, dust, trails or magic. It can provide feedback without simulating every physical detail; collision/damage must be specified separately if needed. |
| Animation / rig / skinning | Animation changes properties over time. A rig provides a structure and controls for posing; a skeleton is a bone hierarchy. Skin weights determine how bones influence mesh vertices. A rig alone does not provide motion. |
| Sprite animation / skeletal animation | Sprite animation displays successive image regions. Skeletal animation poses bones and may deform a weighted mesh. They have different authoring and export requirements; neither eliminates timing or gameplay-state logic. |
| State machine | States describe allowed modes of behavior; transitions define when modes change. It can drive gameplay or animation, but an animation-state graph is not automatically a complete NPC decision system. |
| Audio asset / playback | An audio file holds samples. Engine playback determines when, where and how it is heard, including routing, level, spatialization and overlap. Editing the file does not wire the game event. |
| Game AI / coding agent | Game AI selects or executes behavior during play. A coding agent helps develop the game. Neither requires the other, and navigation or a behavior tree does not imply a live LLM. |

**Engine vocabulary examples:** Godot groups Nodes into reusable scenes; Unity uses Scenes containing GameObjects with Components and reusable Prefabs; Unreal places Actors with Components into Levels and can define reusable Actor behavior in Blueprint classes. A Godot scene can fill roles that Unity separates into scene and prefab. A Blueprint graph node is not a Godot scene-tree node. Preserve the requirement when translating, rather than matching words blindly. [Godot concepts](https://docs.godotengine.org/en/stable/getting_started/introduction/key_concepts_overview.html), [Unity GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html), [Unreal Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine).

### Textures, materials, shaders, and the UV handoff

A texture can be more than a picture: a grayscale roughness map describes surface variation; an RGB normal map encodes directions; packed channels can hold different masks. Interpret color textures and data textures appropriately. Some textures are cubes or volumes; this topic's **2D information map** refers to the common 2D case, not every texture type.

A simple surface workflow is **mesh XYZ and face corners → UV layout → sample texture at UV → material/shader uses the values → rendered surface**. UV coordinates are often arranged within 0–1, but can extend outside it; wrapping/clamping settings determine sampling behavior. Not all shaders need UVs: world-space or triplanar approaches are alternatives. Use a checkerboard to inspect stretching, seams, orientation and relative texel density before judging a finished texture.

**Agent workflow:** inspect the mesh and existing UV sets; propose seams and an unwrap or a projection; preserve a copy; export and reimport; compare the same checkerboard and camera in the receiving engine. Verify texture-channel assignments and material parameters. A successful import does not prove the authored material transferred. [Unity shader terminology](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-introduction.html), [Blender UV concepts](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/introduction.html).

### Ideation and rapid prototyping

Start with a player-facing hypothesis: “Can a player recognize the safe platform before the jump?” Generate a few alternatives, choose one uncertainty, and build the smallest playable test with placeholder art. Set a time budget and an observation to collect. Compare variants, record what happened, and decide whether to iterate, discard, or expand. A GDD records decisions and constraints; it need not become a long document before the first test.

**Agent workflow:** ask for alternatives and a bounded graybox implementation, specify what must stay fixed, and review the diff. The agent can implement and instrument a prototype; human playtesting still judges clarity, feel and fun. Evidence should distinguish “the jump is reachable” from “players understood it.”

### Audio tools, especially Audacity

Use **Audacity** to record/import sound, trim unwanted sections, arrange clips, apply fades and level changes, and export an audio file. Save the editable project separately from the exported runtime asset. A DAW such as REAPER is another option for arranging and mixing; engine audio tools handle runtime events and routing. Choose based on the task and handoff rather than treating an editor project file as a playable game asset. [Audacity editing](https://support.audacityteam.org/basics/audacity-editing), [exporting audio](https://support.audacityteam.org/basics/saving-and-exporting-projects).

For a loop, inspect both the boundary and the repeated sound: trimming at a plausible point is not proof of a seamless loop. Check fades/crossfades where appropriate, clipping, silence, channel layout, and the target import format. Loudness adjustment cannot restore detail already destroyed by clipping.

**Agent workflow:** specify the desired duration, event, channels and output; use only available audio automation, scripts or an installed bridge, without assuming Audacity ships an MCP server. Review destructive edits, export, inspect the actual output, and listen. Then wire and test playback in each engine's equivalent audio player/source/component and mixer/bus system. Verify one event produces the intended sound once, the loop repeats cleanly, and positional audio behaves as specified.

### Profiling in all three engines

Use the same method everywhere: define a target device and frame budget; make a repeatable scene; capture representative frames; identify CPU, GPU, memory, physics or audio work; change one suspected cause; repeat and check both performance and behavior. Compare like-for-like builds, resolutions and settings, and account for profiling overhead. Faster average FPS alone can hide frame spikes.

| Engine example | Documented tools | What to ask the agent for and what to verify |
|---|---|---|
| Godot | Standard Profiler for script/physics and frame timings; Visual Profiler for rendering CPU/GPU work. The standard profiler's documentation says it does not profile C# scripts; use an appropriate external C# profiler for that code. | Capture the relevant measurement, identify which subsystem it covers, and preserve a baseline. Do not treat Visual Profiler rendering CPU time as all CPU work. [Profiler](https://docs.godotengine.org/en/stable/tutorials/scripting/debug/the_profiler.html), [Visual Profiler](https://docs.godotengine.org/en/stable/tutorials/scripting/debug/debugger_panel.html). |
| Unity | Unity Profiler modules and rendering analysis tools; platform GPU profilers where appropriate. | Capture CPU/memory and relevant rendering evidence for the target; record enabled modules and overhead. Do not assume GPU counters are available on every platform/backend. [Analysis tools](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/analyze-your-project.html), [Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-activate.html). |
| Unreal | Unreal Insights trace capture and analysis, including Timing Insights CPU/GPU tracks. | Save a trace, attribute expensive work, and repeat the same workload after a change. Verify trace settings and the build/platform, rather than presenting an editor screenshot as a target-device benchmark. [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine). |

### Game AI already available: engine core, first-party packages, and custom behavior

Here **native/core** means part of the engine; **first-party package/plugin** means supplied by its vendor but potentially requiring installation or enablement. Neither label guarantees that a feature is active in a particular project. Checked against official documentation on **November 3, 2026**; learn the capability and verify the installed version rather than memorize version numbers.

| Engine | Verified facilities and scope | What the developer and coding agent still supply |
|---|---|---|
| Godot | Core AStar pathfinding and NavigationServer/navigation agents support navigation meshes, paths and avoidance; 2D and 3D facilities exist. | Define goals, sensing, decisions and movement integration. Do not infer a built-in general behavior-tree authoring system from the navigation API. Implement the decision logic or inspect a specific add-on before relying on it. [3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html), [2D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_2d.html). |
| Unity | Engine navigation APIs plus the first-party **AI Navigation** package for NavMesh workflows. The separate first-party **Behavior** package supplies behavior graphs and task orchestration; it is not a claim that every Unity project has that package installed. | Install/check compatible packages, configure navigation, author tasks and decision data, and connect behavior to gameplay and animation. Navigation does not decide what the character wants. [AI Navigation](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html), [Behavior graphs](https://docs.unity3d.com/Packages/com.unity.behavior@1.0/manual/behavior-graph.html). |
| Unreal | Engine/first-party systems include Navigation, Behavior Trees, AI Perception, StateTree, Environment Query System (EQS), and AI debugging tools. Check project/plugin enablement for the chosen systems. | Configure sensing and navigation; author tasks, states, transitions and query criteria. These systems provide mechanisms, not a finished game's goals or automatically correct behavior. [Unreal AI systems](https://dev.epicgames.com/documentation/en-us/unreal-engine/artificial-intelligence-in-unreal-engine). |

A **navigation mesh** describes traversable space; pathfinding chooses a route; local avoidance adjusts motion around nearby agents; sensing supplies observations; a state machine or behavior tree organizes decisions. These are related layers, not synonyms. An animation state machine does not automatically replace a decision system. Learned policies, inference runtimes and generative NPC dialogue are additional choices with their own integration requirements; ordinary game AI does not require them.

**Agent workflow:** inventory what is installed, implement one bounded behavior using its actual APIs, and test controlled situations: visible/hidden target, reachable/unreachable goal, interruption, repeated entry, and recovery. Require evidence of the transitions and resulting gameplay, not just a successful tool call or a moving character.

Useful calculations, with assumptions stated:

- **Frame budget:** `1000 / target FPS` milliseconds. At 60 FPS, the budget is about **16.67 ms**; 20 ms per frame corresponds to **50 FPS**.
- **Time-based progress:** `clamp(elapsed_seconds / duration_seconds, 0, 1)`. A fixed number of rendered frames has different durations at different frame rates.
- **Steady-state particle estimate:** `emission rate × lifetime`, for constant emission, fixed lifetime, and no extra cap or early removal. At 80 particles/second and 1.5 seconds, expect about **120 live particles** after startup. This estimates count, not GPU time.
- **Scale example:** if the supplied import contract uses 1 world unit = 1 meter, a 2-meter prop should measure 2 world units. State the unit contract instead of assuming every engine/importer shares one.

When answering a scenario, use: **name the concept → state the intended behavior → explain the mechanism → give a check → identify what the check cannot prove**.

## Worked practice examples — not selected exam questions

The question bank uses five-point multiple-answer questions and five-point essays. For multiple-answer items, each of five statements is independently true or false: checking a true statement or leaving a false statement unchecked earns one point. A wrong choice earns zero for that statement. Essays use five rubric items. These are the bank's existing conventions; the actual exam's format, length, and scoring remain undecided.

### Example A — generic collision requirements and an agent contract

**Scenario:** An agent is asked to build a checkpoint in any of the three engines. The stated contract is: a trigger volume detects members of the Player category, ignores the Enemy category, activates the checkpoint once, and does not block movement. Assume the engine-specific trigger prerequisites are correctly configured. Its collision shape is separate from its visible artwork.

Mark every true statement:

- [ ] A. Overlap detection and physical blocking are different requirements.
- [ ] B. An enemy's overlapping image overrides the specified collision filter.
- [ ] C. The agent must translate the contract into the chosen engine's filtering and event rules.
- [ ] D. A useful test checks the player, an enemy, repeated entry, and absence of blocking.
- [ ] E. Seeing the checkpoint artwork proves that its trigger volume is configured correctly.

<details>
<summary>Practice key and explanations</summary>

**A=T, B=F, C=T, D=T, E=F.** Detection need not block. Visual overlap does not replace collision filtering. The behavioral contract is portable but its API implementation differs. Tests must cover allowed and excluded entrants, repeat behavior, and physical response; artwork alone proves none of those.

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

**Scenario:** An agent profiles a repeatable scene in the chosen engine on a specified target device. The target is 60 FPS; the scene measures 20 ms per frame. Smoke emits 80 particles per second, each lasting 1.5 seconds; assume constant emission, steady state, and no early removal or limiting cap.

Mark every true statement:

- [ ] A. The target frame budget is about 16.67 ms.
- [ ] B. A 20 ms frame meets the 60 FPS target.
- [ ] C. About 120 smoke particles are alive at steady state under the stated assumptions.
- [ ] D. The count alone proves that smoke is the bottleneck.
- [ ] E. A controlled before/after measurement can help test whether a smoke change improves frame time.

<details>
<summary>Practice key and explanations</summary>

**A=T, B=F, C=T, D=F, E=T.** `1000 / 60 ≈ 16.67`; `1000 / 20 = 50 FPS`; `80 × 1.5 = 120`. Count does not establish cost: screen coverage, shaders, overdraw, and other work matter. Compare equivalent scenes and identify the measured CPU/GPU work before assigning cause. The agent should retain a trace or measurement capture from the appropriate Godot, Unity, or Unreal profiler, state what it measures, and repeat the test after a controlled change.

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

### Example E — scene editing through a tool with an uncertain result

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

**Prompt:** Explain why navigation alone is insufficient. Ask a coding agent to inspect which relevant facilities are present in a Godot, Unity, or Unreal project, then propose one implementation and a small test plan. Distinguish core features, first-party packages, and custom logic.

<details>
<summary>Practice rubric — five points</summary>

1. Distinguish finding a route from deciding whether to chase, and distinguish runtime game AI from the coding agent doing the implementation.
2. Identify a documented navigation/decision option for the chosen engine and verify installation/enablement; define patrol and chase states plus return/search behavior if needed.
3. Define what detection and losing the player mean, including the supplied delay.
4. Handle unreachable goals or a missing route without claiming successful pursuit.
5. Test acquisition, loss, reacquisition, and an obstructed/unreachable target; assess movement and transitions as well as path output.

</details>

### Example G — choose a game-development workflow and defend its engine fit

**Scenario:** A small team is building a 3D exploration game for desktop computers. It needs a rigged character, painted textures, interactive doors, ambient audio, and a repeatable performance test. One teammate knows C#, another can model in Blender, and a third prefers visual behavior authoring. The team has a Blender character with a procedural material, a sound editor's project file, and an existing Unity gameplay component. It has not chosen an engine. You may state additional assumptions, but cannot assume all assets and code import unchanged.

**Prompt:** Identify the capabilities and tool categories needed, including how a coding agent would assist and verify each handoff. Compare Godot, Unity, and Unreal against this team's needs, give a strength and a drawback for each, and defend a choice. Trace how the external character, material, sound, and gameplay code would enter the chosen engine. Identify at least two cases requiring export, baking, adaptation, or replacement, explain why, and propose checks. Explain what would change if the team switched to either other engine.

<details>
<summary>Proposed practice rubric — five points; no single engine is the required answer</summary>

1. Maps the game's requirements to design, asset creation, animation, audio, gameplay, collaboration, testing, and delivery capabilities; chooses plausible tool options with reasons.
2. Compares all three engines against the same requirements and team skills, including a supported strength and a cost for each; avoids unsupported claims that an engine is universally best or cannot make this genre.
3. Gives a concrete character/material handoff: appropriate supported format, rig/animation checks, and baking or rebuilding unsupported procedural material features as needed.
4. Distinguishes editable sound-project source from an exported audio asset, and engine-specific gameplay code from portable data; explains the changes required by each receiving engine's formats or APIs.
5. Defends the engine choice and a bounded agent-assisted validation plan: inspect the actual available tools, import and reopen assets, play the character/door interaction, listen to audio, measure an equivalent scene on target hardware, and check the exported build. Names at least one result that would cause the team to reconsider its choice.

</details>

### Example H — texture information and surface mapping

**Scenario:** An agent imports a model whose geometry has the intended dimensions. A checkerboard looks stretched on one face. The model has a roughness texture and a normal texture. The agent proposes fixing the stretching by increasing the mesh's world-space scale and says the normal texture will repair the silhouette.

**Prompt:** Distinguish texture, material and shader; explain XYZ versus UV; diagnose both proposed fixes and describe a safer check.

<details>
<summary>Proposed practice rubric — five points</summary>

1. Defines the texture as sampled information, the material as rendering configuration/behavior with inputs, and the shader as computation; explains that roughness and normals are data, not just color pictures.
2. Distinguishes 3D surface geometry from its 2D parameterization; explains that seams can give one 3D position different UV coordinates.
3. Investigates UV distortion, texture transform and sampling rather than altering an already-correct physical size to conceal a surface-mapping problem.
4. Explains that a normal map changes shading directions but does not itself repair or change mesh silhouette.
5. Has the agent preserve the baseline, inspect and adjust the relevant UV/material data, reimport, and compare a checkerboard at fixed camera and object dimensions; checks channels and shading separately.

</details>

### Example I — sprite animation, Audacity, and a rapid prototype

**Scenario:** A team wants to learn whether players recognize a jump boost. It has a four-frame sprite sheet, a rough sound recording, and a graybox level. A coding agent is available through a limited editor bridge; no audio-editing tool is exposed by that bridge.

**Prompt:** Propose a small prototype and an asset workflow, including what to do in Audacity, what the agent can actually automate, and what evidence would justify keeping the design.

<details>
<summary>Proposed practice rubric — five points</summary>

1. States a player-facing hypothesis and a small playable test, using placeholders and avoiding unrelated polish or mechanics.
2. Specifies sheet regions, frame order, consistent pivot and timing; distinguishes displaying sprite frames from posing a skeletal rig.
3. Describes trimming/editing the sound in Audacity, level/fade checks, saving editable source and exporting a supported runtime audio file; listens to the exported result.
4. Uses the agent only through verified capabilities, or separately established automation; does not invent an audio tool. Specifies the gameplay event, animation/sound synchronization and prevention of duplicate triggers.
5. Tests actual gameplay and collects player observations, separating correct technical execution from whether the boost is understood; compares one controlled variation before deciding to keep, change or discard it.

</details>

## Decisions to make together before assembling an exam

- [ ] Confirm whether this is a midterm or cumulative exam, and the last taught chapter/topic.
- [ ] Mark each topic-map row Include, Narrow, Defer, or Exclude; specify boundaries for broad rows.
- [ ] Confirm the agent/MCP concepts students have been taught and weave relevant contracts, permission boundaries, evidence and recovery into each selected subject.
- [ ] Apply the confirmed generic framework throughout: use Godot, Unity and Unreal as examples, and state engine-specific premises when required. Decide comparison depth and topic weights; no engine-specific setup trivia is required by this proposal.
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
- [Course chapter map](https://github.com/nikbearbrown/csye-7270-building-virtual-environments/blob/0240fcd07d6d8443c8a3de8d02f50ff9fbcdba4e/chapters/README.md) and [module map](https://github.com/nikbearbrown/csye-7270-building-virtual-environments/blob/0240fcd07d6d8443c8a3de8d02f50ff9fbcdba4e/modules/README.md): provide the original course progression, which this guide reorganizes into generic concepts. These course materials label themselves review drafts; they are evidence of the proposed curriculum, not proof of what has been taught or approved for examination.
- [MCP and agent-workflow sources](../SOURCES.md): research context and mappings for the supplementary pool. Product versions, beta status, exact commands, and port numbers are not proposed memorization topics here.

**Review note:** Drafted with Codex from the repository materials; the whole guide was revised at Nik's direction on November 3, 2026 to use generic concepts and integrated agent workflows. Official documentation was checked for engine capabilities, profiling, UVs and Audacity; no new engine or audio-tool integration was executed. The nine worked examples are original practice scenarios for this review sheet. Their arithmetic, keys, and rubrics were checked during preparation, but Nik must review subject coverage and wording before adopting any question for an exam.
