# Engine vocabulary (Godot, Unity, Unreal)

## MA-vocab.1

Candidates for a game-programming job are asked what the words scene, level and map mean in the three big engines. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unity, "scene" means a reusable object that is instanced many times, in the way a prefab is.
- [ ] B. A Godot scene can be a single weapon, a character or a whole level, so "scene" does not mean "one screen of the game".
- [ ] C. In Unity, more than one scene can be loaded at the same time, which is called additive loading.
- [ ] D. In Unreal, a level is a saved map that holds the Actors placed in one part of the world.
- [ ] E. In Godot, "level" has no special meaning to the engine; a level is a scene, often one that instances other scenes.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A Unity scene is a container of GameObjects for a level or screen; the reusable, instanced object is the prefab.
- B: A Godot scene is any saved tree of nodes, which is why one mechanism serves for small objects and whole levels.
- C: Unity can load a scene on top of the scenes already open (additive loading), which is how levels are built from several parts.
- D: In Unreal the level (map) file stores the Actors placed in it.
- E: Godot has no separate level type; any scene can serve as a level, and a level scene usually contains instances of smaller scenes.

**Source:** Scene, level and map

## MA-vocab.2

Engines package a reusable game object once and then place many copies of it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unity, a prefab is an asset that serves as a template, and each copy placed in a scene is a prefab instance that stays linked to that asset.
- [ ] B. In Unity, a prefab instance in a scene and the prefab asset are one object, so deleting the instance from the scene also deletes the asset file.
- [ ] C. In Unity, a scene and a prefab are the same kind of asset stored in the same file type, so loading a prefab replaces the current level.
- [ ] D. In Godot, a saved scene can be instantiated inside another scene, so one mechanism covers both a whole level and a reusable object such as an enemy.
- [ ] E. In Unreal, a Blueprint class is an asset that defines a custom Actor type, and each Actor placed in a level from it is an instance of that class.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The prefab asset is the template; instances in scenes are linked copies of it.
- B: The instance is a separate object in the scene; removing it leaves the asset untouched.
- C: Scenes and prefabs are different asset types; opening a prefab does not replace the level.
- D: In Godot a scene file is both the level format and the reusable-object format, and scenes can be nested.
- E: A Blueprint class is the definition; each placed copy is an instance of that class.

**Source:** Instance, prefab and blueprint class

## MA-vocab.3

A developer working in a Godot project types this to a coding agent: "Make the coin a prefab and spawn ten of them along the track." (Prefab is a Unity word.) Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Once instantiate has been called, the coin appears and runs in the game, without a parent node being needed.
- [ ] B. Instantiating the coin's loaded scene ten times yields ten separate node trees that can each be given a different position.
- [ ] C. A Godot scene plays the role a prefab plays in Unity, so the agent can reasonably read "prefab" as "a saved scene that is instanced".
- [ ] D. Godot has a built-in prefab file type, and the agent must create one before it can spawn anything in the level.
- [ ] E. Spawning ten coins means creating one coin node and ten references to it, so all ten share a single position and move together.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: An instance only becomes part of the running game after it is added as a child of a node in the scene tree.
- B: Each call to instantiate produces a fresh, independent tree of nodes.
- C: A saved Godot scene is the reusable template that Unity calls a prefab, so the word can be translated.
- D: Godot has no prefab file type; the scene file is the mechanism.
- E: Each instance is a separate node with its own position; references to one node would be the same object.

**Source:** Translating engine words in an instruction

## MA-vocab.4

A prefab-style asset (a Unity prefab, an Unreal Blueprint class or a Godot scene) for an enemy is instanced 50 times in a level. On 3 of the instances the developer changes the move speed to a different value in the instance only. Later the developer edits the move speed default in the asset itself. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding a new child object or component to the asset normally shows up in all 50 instances without editing them one by one.
- [ ] B. Instances are independent copies made at placement time, so later edits to the asset do not reach them.
- [ ] C. The 47 instances whose speed was left unchanged pick up the new default.
- [ ] D. Editing the asset once is less work and less error-prone than editing 50 copies by hand, which is the main reason for the asset and instance split.
- [ ] E. The 3 instances that carry their own speed value keep it, because an instance-level override wins over the asset's default.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Structural changes made to the template, such as an added child node or component, appear in its instances.
- B: Instances stay linked to the asset in all three engines; that link is what lets edits flow to them.
- C: Properties an instance has not overridden keep following the asset's value.
- D: Central editing of a shared template is the practical benefit of instancing instead of copy-and-paste.
- E: An override is a value stored on the instance, so it is not replaced when the default changes.

**Source:** Overrides on instances

## MA-vocab.5

A candidate is asked how objects get behaviour in each of the three engines. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unreal, an Actor can be placed in a level or spawned during play, and its location, rotation and scale come from its root component.
- [ ] B. In Unity, a GameObject has a Transform, and features such as rendering, physics and scripts are added to it as components.
- [ ] C. In Godot, the idiom for giving one object several unrelated abilities is to attach several components to a single node, as with Unity's GameObjects.
- [ ] D. In Unity, a GameObject that only holds scripts can exist without a Transform, because the Transform is added only when something needs a position.
- [ ] E. In Unreal, the base Actor Component type carries a transform and can be attached to other components in a hierarchy.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: An Unreal Actor has no transform of its own; it takes one from its root component.
- B: Every GameObject has a Transform; other behaviour comes from components.
- C: Godot combines behaviour by arranging nodes in a tree and instancing scenes; its own documentation says its nodes do not work like components in some other engines.
- D: A GameObject cannot exist without a Transform.
- E: The transform and attachment belong to Scene Components; the plain Actor Component is not tied to a place in the world.

**Source:** Node, GameObject, Actor and component

## MA-vocab.6

Games need labels so that code can find or filter objects such as enemies. Engines give those labels different rules. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding a group or tag to an object only helps code look it up; by itself it changes neither how the object looks nor how it moves.
- [ ] B. In Godot, a group is a collision rule that decides which objects physically touch each other, so adding a node to a group changes what it can hit.
- [ ] C. In Unity, a GameObject has exactly one tag, so one object cannot carry the tags "Enemy" and "Flying" at the same time.
- [ ] D. In Godot, a node can belong to several groups at once, and the scene tree can list the members of a group or call a method on all of them.
- [ ] E. In Unity, a GameObject's tag and its layer are two names for the same property, so setting one also sets the other.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A label has no built-in effect on rendering or physics.
- B: Collision filtering uses layers and masks; groups are lookup labels.
- C: Unity gives each GameObject a single tag (and a single layer).
- D: Groups work like tags with many allowed per node, and the scene tree can list a group's members or call a method on all of them.
- E: Tags and layers are separate properties; layers are used for filtering such as rendering and physics, tags for lookup.

**Source:** Groups, tags and layers

## MA-vocab.7

In a 2D game a parent object sits at world position (200, 50) with no rotation and a scale of 1. A child object has a local position of (100, 0), meaning 100 units along the parent's own x axis. Assume the engine builds the child's world position by scaling its local position by the parent's scale, then rotating it by the parent's rotation, then adding the parent's position. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the parent moves to (500, 50) and nothing else changes, the child's local position becomes (400, 0) so that the child stays in place in the world.
- [ ] B. If the parent is scaled to 2 on both axes and the child's local position is left unchanged, the child's world position is (400, 50).
- [ ] C. Setting the child's local position to (0, 0) puts the child at the world origin.
- [ ] D. If the parent is rotated 90 degrees so that its own x axis points along the world's +y direction, with no scaling, the child's world position becomes (300, 150).
- [ ] E. With the parent unrotated and unscaled, the child's world position is (300, 50).

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A local position is stored relative to the parent and does not change when the parent moves; the child's world position becomes (600, 50).
- B: Scaling doubles the offset to (200, 0), and adding the parent's position gives (400, 50).
- C: A local position of (0, 0) is the parent's own origin, so the child sits at the parent's world position (200, 50).
- D: The local offset (100, 0) is turned into (0, 100), so the child's world position is (200, 150), not (300, 150).
- E: The world position is the parent's position plus the local offset: (200 + 100, 50 + 0).

**Source:** Local versus global space

## MA-vocab.8

A developer tells a coding agent: "Raise the platform by 100 units." The agent must edit position values in three different engines. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unreal, positive z points up, so raising an Actor means adding to its z.
- [ ] B. In Unity the vertical axis is y with positive y pointing up, so subtracting 100 from a GameObject's y raises it.
- [ ] C. In Godot's 2D space the y axis points down the screen, so raising a 2D node by 100 pixels means subtracting 100 from its y position.
- [ ] D. A distance of 100 units is the same real-world length in Unity and Unreal by default, because both treat one unit as one metre.
- [ ] E. In Unreal, y is the vertical axis, so raising an Actor means adding 100 to its y.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Unreal is z-up, so adding to z raises the Actor.
- B: In Unity positive y is up, so subtracting from y lowers the object.
- C: Godot 2D uses screen-style coordinates in which y grows downward, so "up" means a smaller y.
- D: Unity's convention is one unit per metre, but Unreal's unit is a centimetre, so 100 units is 100 cm in Unreal.
- E: Unreal's vertical axis is z, not y.

**Source:** Axis conventions and units

## MA-vocab.9

A 2D game draws into a viewport that is 640 pixels wide and 360 pixels high. The camera is centred on world position (1000, 500), is not rotated, and shows one world unit per viewport pixel (zoom 1). Screen position (0, 0) is the top-left corner of the viewport, and y grows downward in both screen space and world space. A developer tells a coding agent: "Move the player to where I click." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent can use the raw click position as the player's target, because screen coordinates and world coordinates are the same thing.
- [ ] B. A click at screen position (0, 0) corresponds to world position (680, 320).
- [ ] C. A click at the centre of the viewport, screen position (320, 180), corresponds to world position (320, 180).
- [ ] D. After the camera zooms in by a factor of 2, so that objects appear twice as large, a click at screen position (0, 0) corresponds to world position (840, 410).
- [ ] E. A precise instruction asks the agent to convert the click from screen coordinates to world coordinates using the camera, and then move the player to that world position.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Screen coordinates are measured in the viewport; world coordinates are positions in the game world, and the camera relates them.
- B: The viewport's top-left corner is half a viewport (320, 180) away from the camera centre, so it is (1000 - 320, 500 - 180) = (680, 320).
- C: The viewport centre is where the camera looks, which is world (1000, 500).
- D: At zoom 2 the viewport covers 320 by 180 world units, so the top-left corner is (1000 - 160, 500 - 90) = (840, 410).
- E: Naming the two spaces and the conversion removes the guess that would otherwise put the player at the wrong place.

**Source:** Screen space versus world space

## MA-vocab.10

Check each statement about frames, ticks and delta time. Each statement is worth 1 point (5 points total).

- [ ] A. The delta passed to a per-frame callback is a fixed 1/60 s, because 60 frames per second is the standard rate that games are built to run at.
- [ ] B. A tick is one update step of a subsystem such as physics, while a frame is one pass of the main loop ending in a rendered image, so the counts can differ.
- [ ] C. Frame rate is the number of fixed physics steps that run each second, which is why the two numbers match.
- [ ] D. Delta time is the time elapsed since the previous call of the update callback, usually measured in seconds.
- [ ] E. In Godot, the delta passed to the physics callback follows the fixed physics rate, so it does not stretch when a rendered frame takes longer than usual.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The per-frame delta varies with how long each frame took on that machine.
- B: Physics ticks and rendered frames are counted separately and need not be equal in number.
- C: Frame rate counts rendered frames per second; the fixed-step rate is a separate setting and the two need not be equal.
- D: Delta is the elapsed time between consecutive calls, which lets movement be scaled by real time.
- E: Godot's physics callback runs at a fixed rate and its delta follows that rate rather than the length of the last rendered frame.

**Source:** Frame, tick and delta time

## MA-vocab.11

A developer asks a coding agent: "Make the enemy move right 5 pixels every frame." The agent writes position.x += 5 in the per-frame update function. The game is then tested on one screen where the loop runs at 60 frames per second and on another where it runs at 144 frames per second. Use these figures. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. At 60 frames per second the enemy moves 300 pixels per second, and at 144 frames per second it moves 720 pixels per second.
- [ ] B. The enemy moves more slowly on the 144 frames-per-second screen, because each frame lasts a shorter time and so the 5-pixel step covers less time.
- [ ] C. Asking for "move right at 300 pixels per second" and writing position.x += 300 * delta gives the same on-screen speed at 60 and at 144 frames per second.
- [ ] D. Running position.x += 5 in a fixed-step callback that runs 60 times per second gives 300 pixels per second on both screens.
- [ ] E. Replacing the step with 5 * delta gives 300 pixels per second at 60 frames per second and 720 at 144, because delta makes the step scale with the frame rate.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 5 pixels times 60 frames is 300 per second, and 5 times 144 is 720 per second.
- B: More frames per second means more 5-pixel steps per second, so the enemy is faster, 2.4 times as fast.
- C: A speed in pixels per second multiplied by the elapsed time per frame covers the same distance per second at any frame rate.
- D: The fixed-step callback runs 60 times per second regardless of display rate, so 5 pixels per step is 300 per second everywhere.
- E: Each frame moves 5 * delta pixels, and the deltas of the frames in one second add up to one second, so the enemy covers only 5 pixels per second at either rate.

**Source:** Frame-rate independence

## MA-vocab.12

An interviewer asks why movement that involves the physics engine belongs in the engine's fixed-step callback (Unity's FixedUpdate, Godot's _physics_process) rather than in the per-frame callback (Update, _process). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The physics engine advances the world in fixed-size steps, so forces and velocities applied in the callback tied to that step line up with the simulation.
- [ ] B. In Godot, the physics callback is the right place for purely cosmetic effects such as a flickering light, because it runs more often than the per-frame callback.
- [ ] C. Physics driven by the variable per-frame delta depends on how fast the machine renders, so the same input can give different results on different machines.
- [ ] D. Putting movement in the fixed-step callback makes the on-screen frame rate constant, because the physics step no longer varies from frame to frame.
- [ ] E. The per-frame callback is forbidden from changing any object's position, so all movement code has to live in the fixed-step callback.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Fixed-size steps keep the simulation's time unit constant and match the rate at which the engine integrates motion.
- B: The physics callback runs at a fixed rate that can be lower or higher than the frame rate; it is not "more often", and cosmetic effects belong in the per-frame callback.
- C: A varying step makes collisions and jump heights less repeatable between machines.
- D: Frame rate depends on rendering and load; the fixed step only decouples physics from it.
- E: Nothing forbids moving objects in the per-frame callback; it is simply the wrong place for physics-driven motion.

**Source:** Update loop versus fixed-step loop

## MA-vocab.13

A game's fixed-step callback is set to run 50 times per second, so one step is 20 ms. Rendering is not capped, and the engine catches up by running extra steps when a frame is long. Use these figures. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. At 100 rendered frames per second, the fixed-step callback runs once per rendered frame.
- [ ] B. A single frame that takes 60 ms to render is followed by about 3 fixed steps to catch up.
- [ ] C. At 100 rendered frames per second, the step length shrinks to 10 ms so that each fixed step lines up with one frame.
- [ ] D. At 25 rendered frames per second, the fixed-step callback runs 25 times per second, once per rendered frame.
- [ ] E. When three catch-up steps run after a 60 ms frame, each call of the fixed-step callback receives a delta of 60 ms.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: At 100 frames per second a frame lasts 10 ms, half a step, so the fixed step runs on about every second frame.
- B: 60 ms of elapsed time divided by the 20 ms step is 3 steps.
- C: The step length is a fixed setting and does not change with the frame rate.
- D: The fixed step still runs 50 times per second, which is about 2 steps per frame at 25 frames per second.
- E: Each call receives the step length, 20 ms; running it three times covers the 60 ms.

**Source:** Fixed-step catch-up

## MA-vocab.14

A scene contains 2000 enemies. Each enemy's per-frame update function takes 0.01 ms of CPU time, and one frame at 60 frames per second has a budget of 16.67 ms. Use these figures. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Halving the enemy count to 1000 would still leave the enemy updates above the 16.67 ms budget.
- [ ] B. The enemies' update functions alone take 20 ms per frame, which exceeds the 16.67 ms budget.
- [ ] C. Reacting to an event when something changes, instead of checking each frame, removes the per-frame cost for objects that are idle.
- [ ] D. If the enemy updates were the only cost, the game could run at no more than 50 frames per second.
- [ ] E. Switching off the per-frame callback on the 1500 enemies that are idle would leave 5 ms of enemy work per frame.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: 1000 enemies cost 10 ms, which is below 16.67 ms.
- B: 2000 times 0.01 ms is 20 ms.
- C: An event-driven design only runs code when something happens, so idle objects cost nothing per frame.
- D: 20 ms per frame corresponds to 1000 / 20 = 50 frames per second at best.
- E: 500 remaining enemies times 0.01 ms is 5 ms.

**Source:** Cost of per-frame callbacks

## MA-vocab.15

Most engines give an object a hook that runs once when it is ready to be used (Godot's _ready, Unity's Start, Unreal's BeginPlay) and a hook that runs repeatedly (Godot's _process, Unity's Update, Unreal's Tick). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unity, Start is called before the script's first frame update, and only if the script instance is enabled.
- [ ] B. Because a start hook runs only once, it cannot be used to begin repeating behaviour such as a looping timer.
- [ ] C. A per-frame hook is the right place to build the player's starting inventory, because it keeps retrying until it succeeds.
- [ ] D. In Godot, _ready is called again each time a node is removed from the scene tree and added back.
- [ ] E. In Godot, a parent's _ready runs after the _ready of its children, so the parent can rely on its children being set up.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Unity's reference says Start is called before the first frame update only if the script instance is enabled.
- B: A once-only hook can start a timer or any repeating process; it simply starts it once.
- C: Setup placed in a per-frame hook is repeated every frame or needs a guard flag; setup belongs in the once-only hook.
- D: _ready is called only once per node unless request_ready is used.
- E: Godot's documentation says children's _ready callbacks are triggered first and the parent's afterwards.

**Source:** Start hook versus per-frame hook

## MA-vocab.16

Godot calls it a signal, Unity programmers use C# events or UnityEvent, and Unreal has delegates and Event Dispatchers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In all three, the code that announces an event does not need to name the objects that react to it.
- [ ] B. A callback is a function that a listener hands over so that the announcing object can call it when the event happens.
- [ ] C. Signals, events and delegates hold the message in a queue until each listener checks it once per frame.
- [ ] D. In Godot, emitting a signal that nothing is connected to is not an error; it calls nothing.
- [ ] E. In Godot, a listener can connect to a signal on any node it can get a reference to; a parent and child relationship is not required.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Listeners register themselves, so the announcer stays unaware of who is listening.
- B: The callback is the function passed to the signal, event or delegate.
- C: Listeners are called by the announcer when the event happens; by default a Godot signal calls its connected functions immediately, and deferring is an option the connection must request.
- D: Godot's documented error case for emitting is an unknown signal, not an empty list of listeners.
- E: A connection links a signal to a callable on any object; the tree layout does not restrict it.

**Source:** Signal, event, delegate and callback

## MA-vocab.17

A developer wants the health bar (HUD) to redraw when the player takes damage. The requirements for the coding agent are that the player's code must not need to know the HUD exists and that the HUD must not check the player every frame. Check each statement that is true: a statement is true only if the request it quotes meets both requirements. Each statement is worth 1 point (5 points total).

- [ ] A. "Give the player a reference to the HUD and have the player call the HUD's redraw function when it takes damage."
- [ ] B. "In the HUD's per-frame update function, read the player's health and redraw if it changed."
- [ ] C. "Have the player emit a health-changed signal, and have the HUD connect to it and redraw in the handler."
- [ ] D. "Have the HUD declare a signal, and have the player connect to it and emit it whenever health changes."
- [ ] E. "Store health in a global variable that the player writes and the HUD reads in its per-frame update function."

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The player must hold a reference to the HUD, which breaks the first requirement.
- B: This polls the player every frame, which breaks the second requirement.
- C: The player only announces the change and the HUD listens, so neither requirement is broken.
- D: The player has to reference the HUD to connect to and emit its signal, which breaks the first requirement.
- E: The HUD still reads the shared value on every frame, which breaks the second requirement.

**Source:** Signals versus polling and direct calls

## MA-vocab.18

A Unity script subscribes one of its methods to a C# event on a long-lived manager object. The script's GameObject is later destroyed without the script unsubscribing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Event systems keep only weak references to subscribers, so a long-lived emitter drops a destroyed subscriber without needing an unsubscribe call.
- [ ] B. The manager's list of subscribers still holds the destroyed script's method, so the next time the event is raised the call can be made on an object that no longer exists.
- [ ] C. The engine queues the event until the start of the next frame, by which time the destroyed object has been cleaned up and no error follows.
- [ ] D. The usual remedy is symmetrical: subscribe when the object is enabled and unsubscribe when it is disabled or destroyed.
- [ ] E. In Godot, when a node whose method is connected to a signal is freed, the engine removes that connection, so the emitter does not keep calling the freed node.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: A C# event holds a normal reference to each subscriber, so a missing unsubscribe causes stale calls and keeps the object reachable.
- B: A C# event keeps a reference to each subscribed method, so a stale subscription stays in the list.
- C: A C# event calls its subscribers in the line that raises it; nothing is queued.
- D: Pairing subscribe and unsubscribe with the object's enable and disable (or destroy) is the standard discipline.
- E: Godot removes the connections of a freed object, as both emitter and receiver.

**Source:** Event lifetime and unsubscribing

## MA-vocab.19

A studio interview asks why engines offer input actions instead of letting game code read raw keys. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because game code asks about the action, a player can rebind the key without any game code changing.
- [ ] B. Hard-coding a check for the Space key in the movement code is the preferred way to support rebinding, since the key is then easy to find.
- [ ] C. An input action is a named intent, such as "jump", that is mapped to one or more physical inputs like a keyboard key or a gamepad button.
- [ ] D. Unity's Input System actions, Unreal's Enhanced Input actions and Godot's Input Map actions are three engine-specific forms of this same idea.
- [ ] E. Polling asks for an action's current state on each update, while an event callback is called once for each input event as it arrives.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Rebinding changes the mapping, not the code that reads the action.
- B: A hard-coded key defeats rebinding and ties the code to one device.
- C: The action is the game-level meaning, and bindings tie it to devices.
- D: Each engine maps named actions to bindings, under different names and tools.
- E: Polling reads state when asked; an event callback is pushed to the code when the input happens.

**Source:** Input action versus raw key

## MA-vocab.20

Developers use "asset" and "resource" loosely. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An asset, in the everyday sense, is a file in the project folder such as a PNG, a WAV or a mesh, which the engine imports before using it.
- [ ] B. Unity's ScriptableObject and Unreal's Data Asset fill a similar role: a data-only asset that many objects can read, independent of any object in a level.
- [ ] C. A Godot Resource is a data container that does nothing on its own; nodes use resources to do their work.
- [ ] D. In Godot, loading the same resource path twice returns two independent copies, because each load reads the file again, so changing one does not affect the other.
- [ ] E. In Godot, a Resource and a Node are interchangeable: both can be placed in the scene tree and both receive the per-frame callback.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Source files are imported by the editor, and the engine uses the imported form at runtime.
- B: Both are data assets that exist independently of objects in a level, though they are not identical features.
- C: Godot's documentation calls resources data containers that do nothing on their own.
- D: Godot's documentation says loading a resource that is already in memory returns the same copy every time.
- E: Only nodes live in the scene tree and get per-frame callbacks; a resource is just data.

**Source:** Asset versus resource

## MA-vocab.21

A game keeps the player's inventory in one globally reachable object: a singleton in Unity, an autoload in Godot, or an object held by the persistent Game Instance in Unreal. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Godot, replacing the current scene also frees the autoload nodes, which are then recreated for the new scene along with its nodes.
- [ ] B. Such an object is useful mainly because it outlives any one scene or level, so what it stores survives scene changes.
- [ ] C. Registering a script as an autoload makes the engine refuse to create a second copy of it, which is what makes it a true singleton.
- [ ] D. Because any code can reach it, a function that quietly reads the global is harder to test alone than one handed the inventory as a parameter.
- [ ] E. In Unity, a manager object that sits in the first scene stays alive when another scene is loaded in its place, because manager objects are kept across scene loads by default.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Godot's documentation says autoloads are always loaded, no matter which scene is running.
- B: Lifetime beyond the current scene is the reason to put shared state in such an object.
- C: Godot's documentation says an autoload can still be instanced more than once if the user wants.
- D: A hidden dependency on a global makes a function depend on state its signature does not show.
- E: Unity destroys the objects of the scene being replaced unless they are explicitly marked to survive the load.

**Source:** Singleton and autoload

## MA-vocab.22

A developer asks a coding agent for "a global score counter" in a Godot game that has a title scene, a level scene and a game-over scene. The agent puts the counter in a script on the root node of the level scene. When the game reaches the game-over scene, the score reads zero. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Registering the script as an autoload would keep it alive from startup through each scene change.
- [ ] B. Marking the variable with @export keeps its value when the game switches scenes.
- [ ] C. The score variable was freed along with the level scene's nodes when the game switched to another scene.
- [ ] D. The cause is that GDScript resets number variables to zero when a new scene is loaded.
- [ ] E. A way to avoid a global is to pass the score along to the next scene as the scenes are switched.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: An autoload is a node placed under the root before the main scene and kept through scene changes.
- B: @export exposes a variable to the editor and saves its value in the scene; it does not extend its lifetime.
- C: A variable in a script lives only as long as the node it belongs to, and the level scene's nodes were removed.
- D: GDScript does not reset variables; the object holding the variable was removed.
- E: The vague word "global" hid a design choice; handing the value to the next scene is a legitimate alternative to a global.

**Source:** Say "autoload", not "global"

## MA-vocab.23

Check each statement about the editor, a running game and a built (exported or packaged) game. Each statement is worth 1 point (5 points total).

- [ ] A. A game that runs correctly when started from the editor will also run correctly in a built version, so testing the build adds little.
- [ ] B. Code written to extend the editor, such as Unity code that uses the UnityEditor namespace, cannot be used in a built player.
- [ ] C. Producing a standalone game is a separate step from running it in the editor, and engines give that step different names, such as export, build or package.
- [ ] D. In Unity, edits made to scene objects while the editor is in Play mode are kept when Play mode stops.
- [ ] E. In Godot, the editor on its own is enough to export a project to another platform; no separately installed runtime files for that platform are needed.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Builds can differ from editor runs in included files, platform settings and performance, so a successful editor run does not replace testing the build.
- B: Editor-only code does not exist in the player, so it must be kept out of the built game.
- C: Running in the editor and producing a standalone game are different steps, and each engine names the second one in its own way.
- D: Changes made to scene objects in Play mode are discarded when Play mode ends.
- E: Godot's documentation says export templates, the prebuilt runtime for each target platform, must be installed before a project can be exported.

**Source:** Editor, runtime and build

## MA-vocab.24

A developer tells a coding agent: "Ship the game to my tester." The agent starts the project from the command line, sees it run, and reports that it is done. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Ship" is precise enough, because it is the engines' own name for the export step and the tester's platform can be taken to match the developer's.
- [ ] B. Because the game ran on the agent's machine, the agent has already produced a standalone file that the tester can open without the engine installed.
- [ ] C. The tester's machine needs the editor installed to run the result of an export, because the exported game is opened through the editor.
- [ ] D. The exported game is made from the same project folder, so any file the game loads when run from the editor is also present in the build.
- [ ] E. Running the project from the editor or command line is not a build, so the instruction should name the export step and the target platform.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The engines call the step export, build or packaging, not "ship", and the tester's platform is not stated, so the word leaves the target open.
- B: Running from the command line launches the project with the engine; it creates no standalone game.
- C: A built game is meant to run without the editor.
- D: The editor run reads the project folder directly, while an export includes only the files its settings select (Godot, for example, leaves out files whose names begin with a period), so a file can load in the editor and be missing from the build.
- E: Running a project and exporting it are different steps, and an exported build needs a chosen target.

**Source:** Ship, run and export
