# Chapter 1: Scenes, nodes and signals

## ES-ch01.1

A developer tells a coding agent working in Godot: "Spawn a bullet when the player fires." Define node, scene, instance and scene tree, and use them to describe what the agent has to do to make a bullet appear and move correctly. Explain what happens if the agent leaves out the step that puts the bullet into the scene tree, and what happens to the bullet's movement if the agent adds it as a child of the player rather than as a child of the level. Then write a more precise version of the instruction.

**Points:** 5

**Rubric (1 point each):**

1. Defines the four terms accurately: a node is the basic building block with a type, a scene is a saved arrangement of nodes in a tree, an instance is a set of nodes created from a scene, and the scene tree is the live hierarchy of nodes in the running game.
2. Describes the steps: load the bullet scene as a packed scene, instantiate it to get a node tree, then add that tree as a child of a node that is already in the scene tree.
3. Explains that an instance that is never added to the tree does not appear or run: its callbacks such as _ready are not called and it is not part of the game.
4. Explains that a child inherits its parent's transform, so a bullet added under the player is carried along with the player and turns with it, whereas a bullet added under the level root moves in the level's space.
5. Gives a precise instruction that names the bullet scene, says to instance it on each shot, names the parent node to add it to, and says what position and direction to give it (in which space).

**Source:** Node, scene, instance and scene tree

## ES-ch01.2

In a Godot project, a coding agent wrote a coin script that, when the player touches the coin, runs get_parent().get_parent().add_score(10) to update the score display two levels up the tree. The same coin scene is reused in a new level that has a different tree layout, and the game now reports errors. Explain why the script broke, redesign it with a signal, and explain what the signal, the emit and the connection each do. State the usual advice about which direction calls and signals should go in a scene, and say what should happen when two sibling scenes need to cooperate.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the coin depends on the exact shape of the tree above it, so it only works where its ancestors happen to be arranged that way, and breaks when it is reused.
2. Redesigns it so the coin declares a signal (such as collected, with the value as an argument) and emits it when touched, without knowing who listens.
3. Explains that something above the coin (the level or the score display) connects a function to the signal, either in the editor or in code, and that emitting then calls the connected functions (immediately by default).
4. States the usual advice that parents call down into children they own and children announce upward with signals.
5. Explains that sibling scenes should not hold direct references to each other and that a shared ancestor should connect or mediate between them, which keeps each scene reusable.

**Source:** Signals versus direct calls

## ES-ch01.3

A coding agent produced this script for a Godot node: in _process it calls get_node("Label") to find a child, sets that child's text, and also moves the node with position.x += 5. It also loads a settings file from disk inside _process. The game runs 144 frames per second and the project's physics rate is 60 ticks per second. Explain what _ready, _process and _physics_process are each for and how many times each runs in 10 seconds in this setup, identify three problems in the agent's script, and say how to fix each.

**Points:** 5

**Rubric (1 point each):**

1. Explains that _ready runs once when the node and its children have entered the scene tree, so one-time setup such as loading the settings file and finding children belongs there.
2. Gives the counts: about 1 call of _ready, about 1440 calls of _process (once per rendered frame) and about 600 calls of _physics_process (the fixed rate) in 10 seconds.
3. Identifies the repeated settings load and the repeated node lookup every frame as wasted work, and fixes them with a one-time load and an @onready reference or a lookup in _ready.
4. Identifies position.x += 5 per frame as frame-rate dependent (720 units per second at 144 frames per second), and fixes it by expressing the speed per second and multiplying by delta, or by using the fixed-step callback for physics-driven movement.
5. Explains why the fixed-step callback is chosen for physics bodies (a constant step independent of rendering) and the per-frame callback for visuals such as label text.

**Source:** Ready, process and physics callbacks

## ES-ch01.4

A designer wants to tune enemy health, speed and damage without editing code, and several enemy types should share some base values. A coding agent has hard-coded the numbers in the enemy script. Explain what an exported variable is and what a custom Resource is in Godot, and design a setup that uses both. Describe one problem that appears when many enemies share one loaded resource and the game changes its fields while playing, and how to avoid it. Explain when in a node's start-up an exported value becomes available.

**Points:** 5

**Rubric (1 point each):**

1. Explains that an exported variable is exposed to the editor so that each instance can carry its own value that can be edited in the Inspector without opening the script.
2. Explains that a custom Resource is a data container that extends the resource type and is saved as a file, so that several nodes or scenes can point at the same tuning data.
3. Designs the setup, for example a stats Resource with exported fields, saved per enemy type, with an exported slot of that type on the enemy so the designer chooses the file in the Inspector.
4. Describes the shared-state pitfall: loading the same resource gives every user the same in-memory copy, so changing health on it during play changes it for every enemy; the fix is to keep runtime state such as current health in the node, or to make a separate copy per enemy.
5. States that exported values are assigned after the object is created and its _init has run but before _ready, so _ready can read the designer's values while _init sees only the defaults.

**Source:** Exported variables and resources

## ES-ch01.5

In a Godot game, players on a French AZERTY keyboard say that the WASD-style movement feels wrong, and clicking the Resume button on the pause menu also makes the character fire a shot. A coding agent had read the Space key and the W, A, S and D keys directly and handled the mouse in _input. Explain both bugs using the ideas of input actions, physical versus labelled keys, and the order in which input reaches nodes and the GUI. Describe the fix for each and write a precise instruction for the agent.

**Points:** 5

**Rubric (1 point each):**

1. Explains that input actions in the Input Map name an intent and map it to bindings, so the code asks about the action and not about a particular key, and bindings can then be changed without editing code.
2. Explains the AZERTY problem: a binding by printed key label sends the movement keys to different physical positions on other layouts, whereas a binding by physical key position keeps the same hand shape, which is why physical keys suit WASD-style controls.
3. Explains the click-through bug: _input sees events before the GUI, so a click that the Resume button also uses is seen by the gameplay code as a shot.
4. Fixes it by handling gameplay events in _unhandled_input, which receives only events that no Control has consumed.
5. Writes a precise instruction that names the actions and their physical bindings, says to handle fire in _unhandled_input, and says what to test (a click on the button must not fire).

**Source:** Input actions and input callbacks

## ES-ch01.6

A Godot game has three requirements: when an alarm rings every guard in the level must go on alert, the player's score must survive the move from the level scene to a game-over scene, and a door must open when its lock child has been picked. For each requirement choose between a group, an autoload and a signal, and justify the choice. Give one risk or limit of each mechanism, and for each requirement say what specific failure follows if the wrong mechanism is used (for example, if the score is kept in a script on a node of the level scene).

**Points:** 5

**Rubric (1 point each):**

1. Chooses a group for the alarm: guards add themselves to a named group and one call on the scene tree calls the alert method on every member, so the alarm needs no list of references.
2. Chooses an autoload for the score: an autoload node is added under the root before the main scene and stays through scene changes, whereas data kept in a level node is freed with the level, so the score would read zero.
3. Chooses a signal for the door: the lock child emits a signal when picked and the parent connects to it, so the child does not depend on its parent's type.
4. Gives a risk or limit for each: group names are plain strings, so a misspelling silently matches nothing; an autoload is global state that hides dependencies and must not be freed at runtime; a signal does nothing until something is connected to it.
5. Explains that choosing the wrong mechanism costs a specific failure, such as a stale list of guards, a lost score, or a lock that only works inside one kind of parent.

**Source:** Groups, autoloads and signals

## ES-ch01.7

A coding agent summarised Godot behaviour in five claims. Evaluate each one as correct or incorrect and correct the wrong ones. (1) "_ready runs every time a node is added to the scene tree." (2) "Emitting a signal that nothing is connected to raises an error." (3) "An autoload is freed when the current scene is replaced and recreated for the next scene." (4) "queue_free() removes the node at the end of the current frame, so the node can still be used until then." (5) "@export var speed stores one speed value in the script, and every instance of the scene shares it."

**Points:** 5

**Rubric (1 point each):**

1. Marks claim 1 incorrect: _ready is called once for each node, when the node and its children have entered the tree, and is called again only if it is requested again.
2. Marks claim 2 incorrect: emitting a signal with no connected functions is allowed and simply calls nothing.
3. Marks claim 3 incorrect: autoloads are children of the root that are loaded before the main scene and persist across scene changes, and they must not be freed at runtime.
4. Marks claim 4 correct: queue_free defers deletion to the end of the frame, so the node is still accessible until then.
5. Marks claim 5 incorrect: @export exposes the variable to the editor, and each instance of the scene can carry its own value, with the script supplying only the default.

**Source:** Checking claims about Godot behaviour
