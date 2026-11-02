# Chapter 1: Scenes, nodes and signals

## MA-ch01.1

A Godot beginner is asked to explain the basic terms of the engine. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An instance is a copy of a scene that has been created as nodes, so the same scene can have many instances.
- [ ] B. The scene tree is the saved scene file on disk, which is what Godot loads when the game starts.
- [ ] C. A scene file may hold only one node, so a character made of several nodes has to be several scenes.
- [ ] D. A node is the smallest building block, and each node has a type, such as Sprite2D or Timer, that decides what it can do.
- [ ] E. A scene is a saved arrangement of nodes in a tree, stored as a file, that can be reused.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Creating nodes from a scene is called instancing, and it can be done as often as needed.
- B: The scene tree is the live hierarchy of nodes in the running game; the file holds a saved scene.
- C: A scene can contain any number of nodes arranged in a tree.
- D: Godot builds everything from nodes, and a node's type gives it its abilities.
- E: A scene is a saved tree of nodes that other scenes can reuse.

**Source:** Node, scene, instance and scene tree

## MA-ch01.2

A Godot developer has a saved scene called Character (a body, a sprite and a collision shape) and wants a Magician that is mostly the same but has an extra staff node. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Instancing Character inside a new scene copies its nodes once, so later edits to the Character file do not reach the new scene.
- [ ] B. A new scene that inherits from Character starts with its nodes, and later edits to Character flow into it.
- [ ] C. Inheriting a scene and instancing a scene are two names for the same operation, and both leave the result linked to the original.
- [ ] D. The staff node has to be added by editing the Character scene itself, which would give the other characters a staff too.
- [ ] E. An instanced scene appears in the new scene as several separate top-level nodes with no link to the file it came from.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: An instance stays linked to its scene file, so edits to the file reach the instance.
- B: An inherited scene extends its base, can add nodes of its own, and follows later changes to the base.
- C: Instancing places a scene as a node inside another scene; inheriting builds a new scene on top of a base scene.
- D: An inherited scene can add the staff without touching Character.
- E: An instance appears as one node (the root of the instanced scene) that remains linked to its source file.

**Source:** Instancing versus inheriting a scene

## MA-ch01.3

A level needs ten identical-looking enemies, each made of a body, a sprite and a timer node. A developer tells a coding agent: "Add ten enemies to the level." The agent duplicates the enemy's nodes ten times directly inside the level scene. Later the developer changes the enemy's sprite. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Ten instances of the same scene must all sit at the same position, because they share one scene file.
- [ ] B. Each of the ten copies has to be changed by hand, because they are plain nodes with no link to a shared enemy scene.
- [ ] C. Saving the enemy as its own scene and instancing it ten times in the level would let one edit of the enemy scene reach all ten.
- [ ] D. Instancing the enemy scene ten times stores ten full copies of the enemy's nodes inside the level's scene file.
- [ ] E. The instruction was precise enough: whether the agent copies nodes or instances a scene is only a matter of taste and has no effect on later maintenance.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Each instance has its own position and can be placed anywhere.
- B: Duplicated nodes are independent, so each one needs the edit.
- C: Instances stay linked to the enemy scene, so changing it updates every instance.
- D: The level's scene file records a reference to the enemy scene for each instance rather than full copies of its nodes.
- E: The choice decides whether one edit can reach all ten, so the instruction hid an important decision.

**Source:** Instancing a scene for repeated objects

## MA-ch01.4

In Godot, a scene has a root node called Main with one child called Player, and Player has one child called Sprite. Every node has a script that prints its own name from _enter_tree and from _ready when the scene is added to the running tree. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A script on Main can rely, in its own _ready, on Player and Sprite having already been through their _ready.
- [ ] B. The _enter_tree of Sprite prints before the _enter_tree of Player.
- [ ] C. The _enter_tree of Main prints before the _enter_tree of Player and of Sprite.
- [ ] D. The _enter_tree of Player prints before the _ready of Sprite.
- [ ] E. The _ready of Sprite prints before the _ready of Player.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Main's _ready is called last, after Player and Sprite are ready.
- B: The parent's _enter_tree runs first, so Player precedes Sprite.
- C: A node's _enter_tree is called before that of its children, so the root comes first.
- D: _ready for Sprite needs Sprite to be in the tree, and Player entered the tree before its child did.
- E: Godot's documentation says a node's _ready is called after its children's.

**Source:** Enter-tree and ready order

## MA-ch01.5

A Godot project has its physics rate set to 60 ticks per second, and the engine can always keep up with that rate. The game renders a steady 144 frames per second for 10 seconds after loading. A test script puts a counter that adds 1 in each of three callbacks of one node: _ready, _process and _physics_process. Use these figures. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The _physics_process counter is about 1440, because both repeating callbacks run once per rendered frame.
- [ ] B. After the 10 seconds the _physics_process counter is about 600.
- [ ] C. After the 10 seconds the _ready counter is 1.
- [ ] D. After the 10 seconds the _process counter is about 1440.
- [ ] E. If the display dropped to 30 frames per second, the _physics_process counter would fall to about 300 over the same 10 seconds.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The physics callback follows the fixed physics rate, not the rendered frames.
- B: _physics_process runs at the fixed physics rate: 60 per second times 10 seconds is 600.
- C: _ready is called once per node unless it is requested again.
- D: _process runs once per rendered frame: 144 frames per second times 10 seconds is 1440.
- E: The physics rate does not depend on the frame rate, so the count stays near 600 (about two ticks per frame).

**Source:** Ready, process and physics callbacks

## MA-ch01.6

A coding agent writes this at the top of a Godot script that is attached to a node with a child named Label: var label = $Label. The script then sets label.text inside _process. When the scene starts, the console reports that the node was not found, and the game later fails because label is null. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A member variable's initializer runs when the script instance is created, before the node's children are available, so the lookup can fail.
- [ ] B. The right fix is to repeat the lookup inside _process, because a child node is not found until the game loop is running.
- [ ] C. The lookup fails because Godot cannot find children by name, so the script must refer to them by number.
- [ ] D. Assigning the child in _init, the constructor, is an equivalent fix, because the node's children exist by the time it runs.
- [ ] E. Marking the variable @onready defers its initialization until right before _ready runs, when the child exists.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Godot's documentation says sub-nodes can only be obtained once _ready is called.
- B: Looking up the node every frame wastes work and is not needed; one lookup at ready time is enough.
- C: Children are found by name or path; the problem is when the lookup happens.
- D: _init runs when the object is created, before the node has entered the tree and before its children are ready.
- E: The documentation says @onready defers the variable's initialization until _ready is called.

**Source:** onready and the null child reference

## MA-ch01.7

Check each statement about GDScript and how a script relates to a node. Each statement is worth 1 point (5 points total).

- [ ] A. Variables declared at the top of a script are shared among the nodes that use that script, like a single global.
- [ ] B. A script that begins with extends Node2D adds behaviour to a node of that type and can use the properties and methods that Node2D provides.
- [ ] C. GDScript is indentation-based and looks like Python, but it is a separate language made for Godot, and Python does not run the scripts.
- [ ] D. Attaching a script to one node gives the other nodes of the same type in the project the same behaviour.
- [ ] E. A script can declare a signal with the signal keyword, and other scripts can connect functions to it.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Member variables belong to each script instance, so each node has its own.
- B: The extends line names the node type the script builds on, so its members are available in the script.
- C: GDScript borrows Python-like syntax but has its own interpreter inside the engine; a script is never run by Python.
- D: A script is attached to the particular node (or nodes) it is assigned to, not to every node of that type.
- E: The signal keyword defines a signal that other objects can react to.

**Source:** GDScript and scripts on nodes

## MA-ch01.8

A script on a coin scene has the line @export var value: int = 1. The coin scene is instanced three times in a level. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A value set in the Inspector on an exported variable is stored with the scene, so it is still there when the scene is saved, closed and reopened.
- [ ] B. @export makes the variable global to the whole project, so changing it on one instance changes all the instances of the scene.
- [ ] C. An exported value can be changed at runtime only by editing the script file, because exports are fixed when the project is saved.
- [ ] D. The value shows up in the Inspector for each instance and can be set differently on each without editing the script.
- [ ] E. A variable that is not marked @export is hidden from other scripts, because only exported variables are visible outside their script.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Exported properties are saved in the scene file, which is how the editor can reopen the scene with the values that were set.
- B: Exported variables are still per-instance members; export only exposes them to the editor.
- C: Code can assign an exported variable like any other member while the game runs.
- D: Exporting exposes a variable to the editor, so each instance can carry its own value.
- E: Exporting concerns the editor, not access; other scripts can read ordinary members.

**Source:** Exported variables

## MA-ch01.9

A developer tells a coding agent: "Let the designer tune the player's run speed and jump height without touching code." Each statement below describes a way the agent could carry out the instruction. Check each statement that does what the developer asked. Each statement is worth 1 point (5 points total).

- [ ] A. Put the numbers in a custom Resource saved as a file, so that several characters can share one tuning file.
- [ ] B. Put the numbers in @export variables on the player's script so they appear in the Inspector.
- [ ] C. Leave the numbers as constants at the top of the player script and tell the designer which line to edit.
- [ ] D. Export a variable of a custom Resource type on the player so the designer can pick which tuning file a given player uses.
- [ ] E. Store the numbers by adding the player to a group named after each value.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A custom Resource with exported fields is a data file the designer can edit and share.
- B: Exported variables can be edited in the Inspector without opening the script.
- C: Editing a line in the script is touching code.
- D: An exported Resource slot lets the designer assign a tuning file in the Inspector.
- E: A group is a label for finding nodes; it cannot hold numeric values.

**Source:** Exported variables and custom resources

## MA-ch01.10

Three enemy instances each use @export var stats: EnemyStats, where EnemyStats is a custom Resource saved as a file with a health field set to 100. All three instances point at the same saved file. During play a script lowers stats.health by 30 on one enemy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A Resource is a node, so each of the three enemies adds it to the scene tree as a child.
- [ ] B. The saved resource file is rewritten with 70 as soon as the value changes.
- [ ] C. Loading the same resource path returns the same in-memory copy, so all three enemies see health 70.
- [ ] D. Marking the field with @export gives each enemy its own copy of the resource.
- [ ] E. Only the damaged enemy's stats change, because each enemy gets its own copy of the file's data.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A Resource is a data container, not a node, and it is never added to the scene tree.
- B: A change in memory is not written back to the file unless the game saves the resource.
- C: Godot's documentation says that loading a resource already in memory returns the same copy every time, so the change is visible to all users.
- D: Export exposes the slot to the editor; it does not copy the resource.
- E: Users of one loaded resource share it; there is no per-enemy copy unless one is made.

**Source:** Shared resources

## MA-ch01.11

A Godot scene has a Door node with a child Lock, and a Player node elsewhere in the level. The Lock should tell the Door when it has been picked, and the Door should then unlock itself. A reviewer judges the wiring by the usual advice for scene design: calls go down the tree to children, and signals go up. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The Door may call a method on its child Lock directly, because a parent knowing its child is the normal direction for a direct call.
- [ ] B. Under that advice it is acceptable for the Lock to call get_parent().open() directly, since this works without any connection.
- [ ] C. With the signal approach the Lock can be reused in a scene that has no Door, because it does not depend on what listens.
- [ ] D. The Lock declares an unlocked signal and emits it, and the Door connects to that signal and reacts.
- [ ] E. When two sibling scenes must cooperate, the usual advice is for a shared ancestor to connect or mediate them, not for one to hold a reference to the other.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A parent that owns a child may call methods on it.
- B: The advice sends information up with signals; a direct upward call makes the Lock assume its parent is a Door with an open method, which breaks when the Lock is reused elsewhere.
- C: Signals do not require a particular listener, so the Lock works wherever it is placed.
- D: The child announces what happened and the parent decides what to do.
- E: Godot's scene-organization advice says siblings should not reference each other directly and an ancestor should mediate.

**Source:** Signals versus direct calls

## MA-ch01.12

A Godot script declares signal health_changed(new_value) and emits it from several places. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. By default the connected functions run immediately during the emit call, unless the connection was made in deferred mode.
- [ ] B. Connecting a function in the editor's Signals dock and connecting it in code are two ways of making the same kind of connection.
- [ ] C. If no function is connected when the signal is emitted, Godot raises a runtime error and stops the script.
- [ ] D. Emitting the signal with an argument sends that value to each connected function.
- [ ] E. Declaring the signal in the script makes it part of that node's interface, so other scripts and the editor can connect functions to it.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Godot's reference describes deferred connections as the ones that run at the end of the frame rather than instantly, so the others run at once.
- B: Both ways link a signal to a function, whether done through the dock or with connect in code.
- C: Emitting a signal that has no listeners simply calls nothing.
- D: The arguments given when emitting are passed to the connected functions.
- E: A declared signal can be connected to from other scripts or from the editor.

**Source:** Signal mechanics

## MA-ch01.13

A coding agent builds player controls in a Godot project. The developer's instruction was: "Make Space jump and A and D move." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reading the Space key directly in the movement code is as flexible as using an action, because the Input Map only renames keys.
- [ ] B. Input.is_action_just_pressed for jump is true only on the frame or tick the press began, while is_action_pressed stays true while the action is held.
- [ ] C. A binding by physical key position stays at the same keyboard position on other layouts, while a binding by the printed character follows that character to a new position.
- [ ] D. An action can have only one input event, so keyboard and gamepad controls need separate actions that the code checks one by one.
- [ ] E. A precise version defines input actions, such as jump, move_left and move_right, in the Input Map, and has the code read those actions.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: An action can be rebound and can carry several bindings without code changes; a hard-coded key cannot.
- B: Godot's reference describes just-pressed as true when the user has started pressing the action in the current frame or physics tick.
- C: Physical key codes refer to the key's location, which is why they are recommended for WASD-style controls.
- D: An action is a grouping of zero or more input events, so one action can respond to a key and a gamepad button.
- E: Naming the actions in the Input Map separates the intent from the keys.

**Source:** Input actions

## MA-ch01.14

A Godot game has a pause menu made of Control nodes (buttons) that can open over the gameplay. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. No node can mark an event as consumed, so the nodes in the tree see the events that the engine receives.
- [ ] B. _unhandled_input receives only events not consumed by _input or by a GUI Control, so gameplay code there ignores a click a menu button used.
- [ ] C. _unhandled_input is called before _input, so it is the place to filter events early, before any other node sees them.
- [ ] D. _input is called before GUI processing, so it can see all events, including those that a menu button would use.
- [ ] E. Polling Input.is_action_pressed inside _process is blocked while a menu is open, because the GUI consumes the action first.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: An event can be marked as handled, which stops it from reaching later nodes.
- B: The documentation recommends _unhandled_input for gameplay events because it lets the GUI intercept events first.
- C: The order is the other way: _input comes first and _unhandled_input only gets what is left.
- D: _input runs before GUI processing and can filter events before the GUI sees them.
- E: Polling reads the current state of the action and is not affected by whether a Control consumed the event.

**Source:** Input callbacks and the GUI

## MA-ch01.15

A Godot level has 12 guard nodes spread across several scenes. When an alarm rings, every guard must switch to alert mode. A developer proposes using a group named guards. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A group is only a name attached to nodes; adding a node to it does not move the node or change its parent in the scene tree.
- [ ] B. The code that rings the alarm needs a list of references to all 12 guards, kept up to date by hand.
- [ ] C. One call on the scene tree can then call an alert method on each member of the group.
- [ ] D. Each guard can add itself to the group in its _ready, or it can be added through the editor's Groups dock.
- [ ] E. A node can belong to more than one group, so a guard could also be in a group named enemies.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A group is a tag used to find and address nodes; the nodes stay where they are in the tree.
- B: Avoiding such a hand-kept list is the point of a group; the tree finds the members.
- C: The scene tree can call a method on all members of a group with a single call.
- D: Groups can be assigned in the editor or with add_to_group in code.
- E: A node can belong to as many groups as needed.

**Source:** Groups

## MA-ch01.16

A project registers one script as an autoload. A developer inspects the live scene tree while the game is playing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The autoload node is added after the main scene has finished loading.
- [ ] B. The safe way to reset an autoload is to call queue_free on it and let the engine recreate it.
- [ ] C. The autoload node appears as a child of the root of the tree, ahead of the current scene.
- [ ] D. Scripts can reach an autoload only through get_node with an absolute path, and cannot refer to it by the name it was registered with.
- [ ] E. Autoload nodes are added before the main scene is loaded, so the main scene's scripts can reach them from their first callbacks.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The documentation says autoloads are added to the root viewport before any other scenes are loaded.
- B: The documentation warns that an autoload must not be freed with free or queue_free at runtime, or the engine will crash.
- C: Godot's documentation says autoloads are children of the root and come first, with the current scene as the last child.
- D: In GDScript an autoload can be referenced by its registered name.
- E: Because they are loaded first, the main scene can use them straight away.

**Source:** Autoloads in the scene tree

## MA-ch01.17

A script contains get_node("UI/Panel/ScoreLabel") inside _process, so the lookup runs on every frame. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A node can be given a unique name in its scene, and %Name then reaches it from within that scene, wherever the node sits.
- [ ] B. Looking up the same node by path 60 times a second repeats work that can be done once, by storing the reference when the node is ready.
- [ ] C. Renaming or moving the Panel node does not affect a hard-coded path, because paths follow nodes to their new place.
- [ ] D. A path that starts with a slash, such as /root/Main/UI, is resolved relative to the node that calls get_node.
- [ ] E. If the path does not lead to a node, get_node returns an empty node object and no error appears, so mistakes are silent.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Setting a node's unique name makes it reachable by %Name from the scene that owns it.
- B: A reference held in a variable avoids repeating the lookup.
- C: A hard-coded path breaks when a node on that path is renamed or moved.
- D: A path starting at the root is absolute; relative paths do not start with a slash.
- E: Godot's reference says that when the path does not point to a valid node, get_node generates an error and returns null.

**Source:** Finding nodes and unique names

## MA-ch01.18

A bullet node in a Godot game must be removed when it hits a wall. Check each statement about doing it. Each statement is worth 1 point (5 points total).

- [ ] A. Once queue_free() has been called, the bullet's other callbacks in the same frame can no longer run.
- [ ] B. Calling queue_free() twice on the same node is an error, because the second call finds the node already queued.
- [ ] C. free() deletes the node immediately, so code that still holds a reference to it and uses it afterwards can fail.
- [ ] D. queue_free() queues the node for deletion at the end of the current frame, and until then the node can still be accessed.
- [ ] E. Freeing the bullet with queue_free() also frees all of its child nodes.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The node is only deleted at the end of the frame, so its callbacks can still run until then.
- B: The reference says it is safe to call queue_free more than once.
- C: free removes the object at once, and old references to it become invalid.
- D: Godot's reference says queue_free queues the node for deletion at the end of the frame and that it can still be accessed before then.
- E: The reference says freeing a node also frees all of its children.

**Source:** Freeing nodes
