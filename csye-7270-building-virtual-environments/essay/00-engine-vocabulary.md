# Engine vocabulary (Godot, Unity, Unreal)

## ES-vocab.1

A developer gives a coding agent this instruction for a game: "Add a global thing so the enemies chase the player every frame at speed 4." Identify at least three words or phrases in it that are too vague for an agent to implement reliably, explain what the agent could build wrong for each, and rewrite the instruction using precise engine terms. Your rewrite must settle how fast the enemies move on screens that run at different frame rates.

**Points:** 5

**Rubric (1 point each):**

1. Identifies "every frame" and "speed 4" as ambiguous and shows the consequence: 4 units per frame is 240 units per second at 60 frames per second but 576 at 144, so the speed depends on the machine, and the unit is not stated.
2. Rewrites the speed as a rate per second in stated units, so the same distance is covered per real second at 60 and at 144 frames per second.
3. Identifies "global thing" as unclear about what it is and where it lives (a script on a node in the level, a manager node, an autoload or singleton that survives scene changes) and names a wrong result, such as state that vanishes when the scene changes.
4. Names the callback that runs the movement and how it keeps the speed frame-rate independent: a per-frame callback with the step scaled by delta time, or a fixed-step callback.
5. Gives a final instruction that combines these terms, with a target, a rate in units per second, a named callback and a named location for any shared state.

**Source:** Say it to the agent: frame-rate independence and global state

## ES-vocab.2

A level contains 30 copies of a crate. The designer wants the crates in one corner to be heavier, and later wants every crate to play a new sound when hit. Explain the difference between a template asset (a Unity prefab, an Unreal Blueprint class or a Godot scene file) and an instance of it, and use the crate case to say what the designer does for each wish, what an override is, and what happens to the heavier crates if the template's default weight is changed afterwards.

**Points:** 5

**Rubric (1 point each):**

1. Defines the template asset as the single definition and an instance as a placed or spawned copy, as opposed to 30 unrelated hand-made copies.
2. Says an instance stays linked to its template, so an edit made to the template reaches the instances instead of being repeated on each copy.
3. For the sound: edits the template once (adds a component, node or sound setting to it), and all 30 instances receive it without being edited one by one.
4. For the heavy crates: changes the weight on those instances only, and calls this an override, a value stored on the instance rather than in the template.
5. Explains that when the template's default weight later changes, instances without an override follow it, while the overridden crates keep their own value until the override is reverted.

**Source:** Instance, prefab, blueprint class and overrides

## ES-vocab.3

A designer wants a health bar to float 40 units above each enemy's head and to follow the enemy as it walks, turns around, and is scaled up to become a boss. A coding agent proposes to compute the enemy's world position every frame and write it into the health bar's position. Explain local versus world (global) space, propose a better setup using parent and child objects, and say what the child's position values then mean. Explain what happens to the bar if the enemy is rotated or scaled, and how the developer should phrase the instruction so that the agent does not mix up the two spaces.

**Points:** 5

**Rubric (1 point each):**

1. Defines local space as positions measured relative to the parent and world (global) space as positions measured from the world origin, with the world position derived from the chain of parent transforms.
2. Proposes making the bar a child of the enemy with a fixed local offset, so the engine carries it along and no per-frame copying is needed.
3. Explains that the parent's rotation and scale also apply to the child's offset: a rotated enemy swings the bar around it, and a boss at scale 2 puts the bar 80 units up unless the scale is compensated or the bar is kept out of the scale.
4. Says what the child's position values then mean: they are local, measured from the parent, so the 40-unit offset stays the same while the bar's world position changes as the enemy walks.
5. Gives a precise instruction naming the parent and child, stating that the 40 units are a local offset along the enemy's up direction, and saying whether scale should be inherited.

**Source:** Local versus global space

## ES-vocab.4

Two players run the same game, one at a steady 60 frames per second and one at a frame rate that varies between 30 and 144. Explain the difference between the per-frame update loop and the fixed-step physics loop, what delta time is, and why a jump can reach a different height on the two machines if jump physics is driven by the per-frame delta. Explain what the engine does when one frame takes longer than the fixed step, and say which loop gravity belongs in and which loop camera smoothing or a UI animation belongs in.

**Points:** 5

**Rubric (1 point each):**

1. Defines a frame as one pass of the main loop that ends in a rendered image, whose duration varies, and the fixed step as a physics update of constant length run a set number of times per second, with delta time as the time since the previous call.
2. Explains frame-rate independence: per-frame motion is scaled by delta (speed expressed per second), and in the fixed-step callback the delta is constant.
3. Explains that integrating motion with a variable delta gives different arcs, collisions or tunnelling on different machines, so physics-driven motion belongs in the fixed-step callback.
4. States that after a long frame the engine runs more than one fixed step to catch up (for example about three 20 ms steps after a 60 ms frame) and that on short frames some frames run no fixed step, so the two loops do not alternate one to one.
5. Places gravity, forces and body movement in the fixed-step loop and camera smoothing, visual effects and UI animation in the per-frame loop.

**Source:** Update loop versus fixed-step loop

## ES-vocab.5

A game has a player, a HUD, an audio manager and an achievement system, and all four must react when the player picks up a coin. A junior developer makes the coin script call each of the four systems directly. Critique this design, then redesign it with the engine's event mechanism (a Godot signal, a Unity C# event or an Unreal delegate). Explain who emits, who listens and what the connection step does, name one thing that can go wrong with events, and say when a direct call is still the better choice.

**Points:** 5

**Rubric (1 point each):**

1. Explains that direct calls couple the coin to four systems: it needs a reference to each, must change when a system is added or removed, and cannot be reused or tested alone.
2. Redesigns it so the coin (or player) emits a "coin collected" event, and each system registers its own callback; the emitter does not name its listeners, and data such as the coin value can travel as an argument.
3. Explains the connect step: a listener registers a function with the signal, event or delegate, and emitting runs the registered functions (immediately by default in Godot and in C# events).
4. Names a pitfall, such as a listener that was destroyed but never unsubscribed (a stale registration), reliance on the order in which listeners run, or an event that nothing listens to.
5. Says a direct call is better when a parent commands a child it owns, when there is a single known target, or when a return value is needed, and that events suit announcing what already happened.

**Source:** Signal, event and delegate versus direct call

## ES-vocab.6

A game must support keyboard and gamepad, let players rebind controls, treat jumping as a single press, and treat running as a held button. Explain what an input action is and how it differs from a raw key or button, describe how polling and event-driven input differ and which fits each of the two controls, and explain what could go wrong if a coding agent is told only "jump when the player presses space". Write the precise version of that instruction.

**Points:** 5

**Rubric (1 point each):**

1. Defines an input action as a named intent (such as jump) that is mapped to one or more bindings, as opposed to code that checks a particular key or button.
2. Explains the benefits: players can rebind without code changes, keyboard and gamepad feed the same action, and the game code stays the same across devices.
3. Distinguishes polling (ask for the current state during an update, which suits a held run button) from event callbacks (called once when the input occurs, which suits one-shot actions), and says which of the two controls each fits: the held run button to polling, the single jump press to an event or one-shot query.
4. Explains the problem with the vague phrase: it hard-codes one key, ties the game to one device, and does not say whether holding the key should repeat the jump.
5. Gives a precise instruction: define an action named jump bound to the Space key and a gamepad button, react once per press (a just-pressed query, which is true only on the frame or tick the press began, or an event callback), and define a separate run action read as a held state.

**Source:** Input action versus raw key

## ES-vocab.7

A game must keep the player's score, the settings and the music player alive as the game moves from one level to the next. Explain what a singleton is for (a Godot autoload, a Unity object kept with DontDestroyOnLoad, or the persistent Game Instance in Unreal), why a developer should not put everything there, and name two alternatives. Say what a developer should ask the agent for instead of "make it global".

**Points:** 5

**Rubric (1 point each):**

1. Explains the purpose: an object (a Godot autoload, a Unity object kept with DontDestroyOnLoad, or the Unreal Game Instance) that lives for the whole run, outlives scene or level changes and is reachable from anywhere, such as score, settings, or music that must not restart.
2. Gives downsides of state that is reachable from anywhere: hidden dependencies, and values that any code can change.
3. Gives downsides for testing and start-up: harder isolated testing, and ordering and initialization problems.
4. Names two alternatives, such as passing data to the next scene during the switch, a data asset or resource shared by reference, saving to disk, or events that announce changes.
5. Gives a precise instruction that states what data is held, how long it lives (survives scene changes), who may change it and how others read it, instead of the word "global".

**Source:** Singleton and autoload

## ES-vocab.8

A developer tells a coding agent "send my tester the game". The agent zips the project folder and reports that the task is done. Using the terms editor, running game and exported build, explain what is wrong with that, give three things that can differ between playing in the editor and playing a build, and write a precise instruction.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the editor (the tool the game is made in, including editor-only code), the running game (started from the editor or command line with the engine present) and an exported build (a standalone package for a target platform).
2. Explains that a zipped project folder is source material that needs the engine, and often an import step, to run, so it is not a build the tester can open.
3. Gives three real differences: editor-only code is absent, some files are excluded or filtered by export settings, and platform settings, performance or debug features differ from the editor run.
4. Names the step and its prerequisites: exporting in Godot (which needs export templates installed), building in Unity, packaging in Unreal, each for a chosen target platform.
5. Gives a precise instruction naming the target platform and configuration, the output location, and a check that launches the built artifact itself instead of the editor and reports the evidence.

**Source:** Editor, runtime and build

## ES-vocab.9

A developer who knows Unity starts working on a Godot project and later on an Unreal project. Give a mapping for at least six terms or ideas from Unity into Godot and Unreal terms (for example prefab, component, ScriptableObject, C# event, FixedUpdate and InputAction), and explain two places where the mapping is only approximate. Say why an agent told to "do it the Unity way" could build the wrong thing in the other engines.

**Points:** 5

**Rubric (1 point each):**

1. Maps the template and instance idea correctly: Unity prefab, Godot scene instanced into another scene, Unreal Blueprint class with placed instances.
2. Maps the loops correctly: FixedUpdate to Godot's physics callback, Update to Godot's per-frame callback and to Unreal's per-frame Tick; saying that Unreal's default per-frame Tick has no direct equivalent of FixedUpdate, and that physics substepping or an optional asynchronous physics mode is the nearest, also earns the point.
3. Maps events, data assets and input correctly: C# event or UnityEvent to Godot signal to Unreal delegate or Event Dispatcher; ScriptableObject to Godot Resource to Unreal Data Asset; InputAction to a Godot Input Map action to an Enhanced Input action.
4. Explains at least two imperfect mappings, such as Godot nodes not behaving like Unity components, an Unreal Actor taking its transform from a root component, or a Godot scene doing the work of both a Unity scene and a prefab.
5. Explains the risk for an agent: a literal translation, such as adding components to a Godot node or creating a prefab file, builds something the target engine does not have or does not use.

**Source:** Cross-engine vocabulary mapping
