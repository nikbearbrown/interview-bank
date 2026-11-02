# Chapter 4: Scenes, collision and physics

## MA-ch04.1

A designer wants a coin that disappears and adds to the score when the player touches it, while the player keeps walking straight through the coin's space without being stopped. The developer asks a coding agent for "a coin collider". Assume a 2D Godot game in which the player is a CharacterBody2D and every collision layer and mask is left at its default. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An Area2D pushes the player back slightly on contact, so designers usually keep its shape small to avoid shoving the player around.
- [ ] B. An Area2D with a collision shape on the coin, connected to its body_entered signal, gives the behaviour the designer described.
- [ ] C. "Collider" does not say whether the coin blocks the player, so the agent might build a solid body that stops the player.
- [ ] D. A clearer instruction is "a trigger area on the coin that removes it when the player enters, without blocking".
- [ ] E. A detection region needs no shape of its own, because it reports any body whose sprite overlaps the coin's sprite.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: An Area2D never pushes or blocks; it only reports overlaps (and can influence gravity or damping inside it).
- B: An Area2D reports the player's entry without blocking, and the handler can add the score and remove the coin.
- C: "Collider" is used for solid shapes and for detection regions alike, and the request never says which one the coin is.
- D: It names the role (detection region), the event (entry), the result, and the explicit non-requirement (no blocking).
- E: Detection uses the collision shape; the sprite is only a drawing and the physics engine never reads it.

**Source:** Collider versus trigger, say it to the agent

## MA-ch04.2

Engines use the single word "collision" for two different jobs. A solid collider stops or deflects other objects. A trigger (a Godot Area, a Unity collider with Is Trigger enabled, an Unreal overlap response) only reports that something is inside its region. Assume that any sensing of nearby objects is done with trigger regions, not with code queries such as a sphere overlap test. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A solid collider produces a collision response such as blocking; a trigger produces none and only reports the overlap.
- [ ] B. In Unity one collider is either solid or a trigger, so a crate that blocks and also senses a nearby player with a trigger region needs two colliders.
- [ ] C. A trigger can report only that an object entered its region; it cannot report that an object is still inside or has left.
- [ ] D. Layers and masks affect solid colliders but not triggers, so a trigger reports bodies inside its region without checking their layer.
- [ ] E. Switching a solid collider to a trigger keeps it blocking the player and adds enter events on top of the existing collision response.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Response is the difference: a collider acts on the objects it meets, a trigger leaves them alone and notifies code.
- B: One collider has one Is Trigger value, so blocking and sensing need separate collider components.
- C: Triggers also report leaving (Godot body_exited, Unity OnTriggerExit, Unreal end overlap) and can be asked who is inside right now.
- D: Layers and masks still decide what a trigger can detect; in Godot an area detects a body only if the body's layer is in the area's mask.
- E: A trigger lets other colliders pass through it, so switching to a trigger removes the blocking.

**Source:** Collider versus trigger

## MA-ch04.3

A developer tells a coding agent: "Add a wall on the right edge of the room that detects when the player touches it." The agent adds an Area2D with a rectangle collision shape and a body_entered handler that plays a bump sound. In testing the bump sound plays, but the player walks straight through the wall and out of the room. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The wall needs a solid body, in Godot a StaticBody2D with a collision shape; the Area2D can stay as a child for the sound.
- [ ] B. The Area2D does what an area does: it reports overlap and does not block, so passing through is expected.
- [ ] C. In Unity the same mistake is a wall whose collider has Is Trigger enabled where a solid collider was needed.
- [ ] D. Adding more layers to the area's collision mask will make the area block the player, because it will then scan the player's layer.
- [ ] E. The instruction never says in words that the player must be stopped, so the agent had to infer it from the word "wall"; a precise instruction would state it.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A static body supplies the blocking and the child area still supplies the touch event.
- B: Detection regions do not stop bodies; blocking needs a solid body.
- C: A Unity trigger collider lets other colliders pass through it.
- D: The mask only chooses what the area scans for; blocking comes from being a solid body, not from any mask value.
- E: "Detects when the player touches it" states the touch event only; stopping the player is at best implied by the word "wall", so the agent built what was literally written and a precise instruction names the blocking.

**Source:** Collider versus trigger, say it to the agent

## MA-ch04.4

Godot's 2D physics offers several node types, and the choice decides who is responsible for movement and for the response to contact. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A RigidBody2D is moved by the engine's simulation, so it is normally driven with forces or impulses, not by writing its position each frame.
- [ ] B. An Area2D detects bodies and areas that overlap its shape, can locally override gravity or damping, and does not block anything.
- [ ] C. A CharacterBody2D is pulled down by the engine's gravity, like a RigidBody2D, so a platformer player built on it needs no gravity code.
- [ ] D. A StaticBody2D takes part in collision but is not moved by collisions or forces, which suits walls and floors.
- [ ] E. A CharacterBody2D detects collisions but leaves the response to your code, usually through move_and_slide or move_and_collide.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The class reference warns that changing its transform or velocity very often can give unpredictable behaviour.
- B: Detection and influence are its jobs; it is not a solid object.
- C: A CharacterBody2D has collision detection but no physics simulation; gravity must be added to its velocity in code.
- D: Static bodies are fixed obstacles that other bodies collide with.
- E: It is the code-driven body type: you decide the movement and, with move_and_collide, the response.

**Source:** Godot physics body types

## MA-ch04.5

Unity sorts colliders by how they are driven. A static collider has a collider and no Rigidbody. A dynamic body has a Rigidbody with Is Kinematic off. A kinematic body has a Rigidbody with Is Kinematic on. A designer plans an elevator platform whose position is set by code each physics step. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A kinematic body is not moved by forces or collisions; code moves it, and it can push dynamic bodies in its path.
- [ ] B. The elevator should be dynamic (Is Kinematic off), because dynamic is the setting for bodies that are moved by code rather than by physics.
- [ ] C. A kinematic Rigidbody still satisfies Unity's Rigidbody requirement for trigger events.
- [ ] D. An elevator whose motion is scripted from outside the simulation is a kinematic body in this scheme.
- [ ] E. A dynamic body is moved by the physics engine in response to gravity, forces and collisions.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Kinematic bodies are driven from outside the simulation but still act on dynamic bodies they run into.
- B: Dynamic bodies are the ones the simulation moves; code-driven motion is the kinematic case.
- C: Unity's trigger rule asks for a Rigidbody on at least one object, and kinematic ones qualify.
- D: Code- or animation-driven motion is the kinematic case.
- E: Dynamic means the simulation owns the body's motion.

**Source:** Static, kinematic and dynamic bodies

## MA-ch04.6

A developer asks a coding agent for a 2D platformer player in Godot. The agent builds the player as a CharacterBody2D. In _physics_process it adds gravity * delta to velocity.y, sets velocity.x from input, calls move_and_slide(), and allows a jump only while is_on_floor() is true. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Multiplying velocity by delta before calling move_and_slide() is also required, because movement must be scaled by the frame time.
- [ ] B. The agent should have put this code in _process, because the movement has to be updated once per rendered frame.
- [ ] C. The agent could have used a RigidBody2D and overwritten its position each frame to get the same result, since the engine handles that case well.
- [ ] D. The gravity line is needed because a CharacterBody2D is not simulated by the engine; nothing pulls it down unless the code changes its velocity.
- [ ] E. After a landing, move_and_slide() updates the body's velocity itself, for example removing the downward part when the body rests on a floor.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: move_and_slide() applies the time step itself, so scaling velocity by delta again would make movement far too slow.
- B: Collision movement belongs in the fixed-rate physics callback; the per-frame callback runs at a variable rate.
- C: The documentation warns that changing a rigid body's transform very often leads to unpredictable behaviour.
- D: Character bodies have collision detection but no physics, so gravity is the developer's job.
- E: The class documentation says it adjusts velocity on collision, such as resetting vertical speed after landing.

**Source:** Character body movement

## MA-ch04.7

In Godot every collision object has a collision layer (the layers it is in) and a collision mask (the layers it scans). Use the rule: object A can detect object B only if B is in a layer that A scans. A game puts walls on layer 1, the player on layer 2, enemies on layer 3 and coins on layer 4. Each coin is an Area2D on layer 4 whose mask scans layer 2 only. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The coin's own layer, 4, is what lets other objects find the coin: only objects whose masks include layer 4 can detect it.
- [ ] B. A coin detects the player, because the player is in layer 2, which the coin's mask scans.
- [ ] C. Layer and mask are two views of one setting, so moving the coin from layer 4 to layer 5 also changes which layers it scans.
- [ ] D. If the coin's mask were set to 0, the coin would stop detecting anything.
- [ ] E. A coin also detects enemies that touch it, because an area reports the bodies that overlap it.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Layer says where an object appears; a scanner must include that layer in its mask.
- B: The coin scans layer 2 and the player is in it.
- C: They are independent fields: layer is where the object appears, mask is what it scans.
- D: A mask of 0 scans no layers.
- E: Enemies are in layer 3, which the coin does not scan, so they are not reported.

**Source:** Collision layers versus masks

## MA-ch04.8

In the Godot editor collision layers are numbered 1 to 32. In scripts, collision_layer and collision_mask hold a bitmask integer in which layer n has the value 2^(n-1): layer 1 is 1, layer 2 is 2, layer 3 is 4, layer 4 is 8, and values add up when several layers are set. A project names layer 1 World, layer 2 Player, layer 3 Pickups and layer 4 Hazards. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A mask of 0 means the object scans the full layer range, because no layer is excluded.
- [ ] B. Writing collision_layer = 4 in a script puts the object on layer 3 (Pickups), not on layer 4 (Hazards).
- [ ] C. A player mask that scans World and Hazards (layers 1 and 4) is the integer 9.
- [ ] D. A mask that scans only Hazards (layer 4) is the integer 4 in a script, the same number the editor shows for that layer.
- [ ] E. A mask of 6 scans layers 1 and 5, because 1 + 5 = 6.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A mask of 0 scans no layers at all.
- B: The integer 4 is the bit value of layer 3.
- C: 1 + 8 = 9.
- D: The editor shows layer numbers but a script stores bit values; layer 4 has the value 8, and the integer 4 is layer 3 (Pickups).
- E: Values add, not layer numbers: 6 = 2 + 4, which is layers 2 and 3 (Player and Pickups).

**Source:** Layer numbers versus bit values

## MA-ch04.9

A top-down game has walls on layer 1, the player (a CharacterBody2D) on layer 2 and enemies (RigidBody2D) on layer 3. All masks, the player's and the enemies', are still at the Godot default, which scans layer 1 only. The designer wants enemies to bounce off walls and off the player but to pass through one another. The developer writes to the agent only: "make the enemies not collide with each other". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A precise instruction names the layers: enemies in layer 3 with a mask that scans layers 1 and 2 but not 3.
- [ ] B. With the enemies on layer 3 and all masks left at that default, enemies and player would not collide with each other either.
- [ ] C. Disabling the enemies' collision shapes meets the request, since a body with no shape cannot collide with other enemies.
- [ ] D. In Unity the equivalent is to untick the World/Enemy pair in the Layer Collision Matrix, which stops enemies colliding with each other.
- [ ] E. Making the enemies much heavier meets the request, because a heavy enemy cannot be pushed by another enemy.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Enemies that scan walls and the player but not their own layer meet both but not each other.
- B: Neither the enemies' mask nor the player's mask includes the other's layer, so nothing links them.
- C: It also removes collisions with walls and the player, which the designer still wants.
- D: The matching change is unticking the Enemy/Enemy pair; unticking World/Enemy lets enemies pass through walls.
- E: Mass changes the response to a collision, not whether a collision is detected.

**Source:** Layers and masks, say it to the agent

## MA-ch04.10

A level has an icy floor on which the player should slide and a rubber ball that should bounce back up almost to the height it was dropped from. A designer asks a coding agent to "make the floor slippery and the ball bouncy". A physics material holds surface properties such as friction and bounce; in Godot's PhysicsMaterial, friction runs from 0 (frictionless) to 1 and bounce runs from 0 (no bounce) to 1 (full bounciness). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Slippery" maps to low friction and "bouncy" maps to high bounce, both set on physics materials.
- [ ] B. The floor looks like polished ice because it has a glossy render material, and that glossy material is what makes the player slide.
- [ ] C. The ball bounces because its collider is round; a box-shaped collider given the same bounce value would not rebound.
- [ ] D. Bounciness comes from how light the body is, so to get a bouncier ball the designer should lower its mass rather than raise its bounce value.
- [ ] E. The icy floor should also get a high bounce value, because a surface that lets a body keep its speed while sliding must give back its energy on impact too.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Friction near 0 lets bodies slide and bounce near 1 returns almost all the impact energy.
- B: Contact behaviour comes from a physics material; a glossy render material changes only how the surface is drawn.
- C: The rebound comes from the bounce value of the contact, not from the collider's outline; a box with the same value rebounds as well.
- D: Bounce is a contact property set on a physics material; mass only sets how hard the body is to accelerate and is a separate property.
- E: Sliding is governed by friction and rebound by bounce; the two are set independently, so a slippery floor can have no bounce at all.

**Source:** Physics material

## MA-ch04.11

A raycast asks the physics world: starting from an origin and going in a direction for a given length, what is the first thing the ray hits? In Godot a ray query returns a dictionary describing one hit, or an empty dictionary when nothing is hit, and by default it does not report Area nodes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A basic ray query reports only the first hit along its path, so a wall between two points hides anything behind it from the ray.
- [ ] B. With default settings a ray passing through a coin's Area2D reports the coin, the same way it reports a wall.
- [ ] C. A ray has width, so it reports the objects inside a narrow cone around the line as well as those on it.
- [ ] D. A hitscan weapon, whose shot lands instantly with no travelling bullet, is usually built on a raycast.
- [ ] E. A raycast from an enemy's eyes to the player tests line of sight, because it finds the first solid thing along the line.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The result describes a single nearest hit.
- B: Areas are not hit unless the query is told to collide with areas.
- C: A ray is an infinitely thin line; checking an area needs a shape query.
- D: The shot is an instant line test from the muzzle along the aim direction.
- E: If the first hit is the player, nothing solid is in between.

**Source:** Raycast

## MA-ch04.12

A bomb must damage every enemy within 3 metres of it, in any direction. A developer tells a coding agent: "cast rays from the bomb to find enemies near it". An overlap query (a shape query) asks which objects overlap a given shape, such as a sphere, at this moment. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A sphere query of radius 3 m around the bomb returns the objects inside that region.
- [ ] B. An area's list of overlapping bodies is refreshed at the moment a body is moved in code, so it is up to date within the same frame.
- [ ] C. After the region query, a ray from the bomb to one enemy can check whether a wall stands between them.
- [ ] D. One ray from the bomb is enough, because a ray finds the nearest object in the whole area around it.
- [ ] E. A shape query can find only trigger regions, because solid bodies are handled by the ray query instead.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A shape query returns all matching overlaps, not just the first.
- B: The list is updated once during the physics step, not when objects are moved.
- C: Region query for who is near, ray for what is in between.
- D: A ray covers one line; a region of 3 metres needs a shape query or many rays.
- E: Shape queries test against colliders in general, filtered by layer, and return solid bodies as well.

**Source:** Overlap query versus raycast

## MA-ch04.13

A bullet with a circular collider of radius 2 px is a RigidBody2D travelling at 1,200 px/s in a game whose physics runs at 60 steps per second. Continuous collision detection is off, so overlaps are tested only at the position the body has after each step. A thin wall is 6 px thick. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Doubling the wall to 12 px guarantees the bullet is stopped, since the wall is then thicker than the bullet is wide.
- [ ] B. This failure is called tunnelling, and it comes from testing discrete positions instead of the path travelled between them.
- [ ] C. Tunnelling happens because a fast body's collision layer stops being recognised by the wall's mask.
- [ ] D. Continuous collision detection tests the path swept during a step, at extra cost per body.
- [ ] E. At 20 px per step, the bullet can jump from one side of a 6 px wall to the other without overlapping it at a tested position.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The bullet still moves 20 px per step, more than 12 + 4 = 16 px, so it can still skip over the wall.
- B: Nothing checks the space between two steps.
- C: Layers do not depend on speed; the wall is simply never tested against the bullet between steps.
- D: It is slower but more precise, and thin-wall misses affect fast, small bodies.
- E: 1,200 / 60 = 20 px per step against 6 + 4 = 10 px of overlap window.

**Source:** Tunnelling and continuous collision detection

## MA-ch04.14

A developer asks a coding agent for three behaviours: a crate that is knocked away when a bomb explodes next to it, a rocket that speeds up for as long as its engine burns, and a paddle that must move at exactly 300 px/s while a key is held. In physics terms a force acts over time and produces acceleration, an impulse is an instantaneous change of momentum applied once, and velocity is a body's current speed with direction. In Godot's RigidBody2D, apply_force is meant to be applied every physics update and apply_impulse is time-independent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Setting a body's velocity to 300 px/s and applying an impulse are the same operation.
- [ ] B. A force is a faster impulse: both change the body's position directly and leave its velocity alone.
- [ ] C. The crate's knock-back is best modelled by one impulse applied at the moment of the explosion.
- [ ] D. A constant force applied over several steps makes the rocket's velocity grow steadily, until drag or a collision changes that.
- [ ] E. The rocket's engine is best modelled by one impulse applied at launch, because an impulse keeps accelerating a body for as long as it exists.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Setting velocity replaces the current motion with an exact value; an impulse adds to it.
- B: Both change velocity (momentum), not position directly.
- C: A one-time impact is the use case for an impulse.
- D: Constant force means constant acceleration.
- E: One impulse changes velocity once; sustained thrust needs a force applied over time.

**Source:** Force, impulse and velocity

## MA-ch04.15

A designer asks a coding agent to "move the platform right at 100 pixels per second" and, separately, to "teleport the player to the checkpoint". The player is a CharacterBody2D. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Velocity exists only on RigidBody2D; a CharacterBody2D has no velocity property.
- [ ] B. A velocity of (100, 0) and a velocity of (-100, 0) are the same velocity because they have the same speed.
- [ ] C. Writing the player's position directly moves it without the engine checking the path in between, so a destination that overlaps a wall can leave the player embedded in it.
- [ ] D. Adding a small amount to position in the physics callback and setting velocity before move_and_slide() are equivalent, because both make the body slide along walls.
- [ ] E. Velocity is a vector with a speed and a direction, measured as distance per unit time, whereas position says where the body is.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: CharacterBody2D has a velocity property that move_and_slide() reads and updates.
- B: They have equal speed but opposite directions, so they are different velocities.
- C: A direct position write is a teleport with no sweep and no response.
- D: Writing position does not run collision handling; move_and_slide() does.
- E: Velocity is a rate of change of position, with direction.

**Source:** Velocity versus position

## MA-ch04.16

Collision handling has two stages: detection (are two shapes overlapping, and where) and response (what the engine or your code then does about it). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For a RigidBody2D the engine only detects contact; the developer writes the code that stops the body at a wall.
- [ ] B. Detection and response are one inseparable step in a physics engine, so an overlap cannot be detected without a response being applied.
- [ ] C. move_and_collide() stops at the first contact and returns the details for your code to handle; move_and_slide() applies a sliding response.
- [ ] D. A bouncing ball's bounciness belongs to detection, because detection decides how fast the ball leaves.
- [ ] E. A trigger performs detection and then stops the body once it overlaps, the way a wall would.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The simulation supplies the response for rigid bodies.
- B: Triggers and overlap queries detect without any response.
- C: One leaves the response to you, the other supplies the common slide response.
- D: Bounce affects the response, the speed returned after contact; detection only finds the contact.
- E: A trigger only reports; it applies no blocking response.

**Source:** Collision detection versus collision response

## MA-ch04.17

A game runs on three machines that render 30, 60 and 144 frames per second. Its physics runs on a fixed time step of 1/60 s. A studio asks candidates why movement that collides belongs in the fixed-step callback (Godot's _physics_process, Unity's FixedUpdate) and not in the per-frame callback. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Putting the movement in the per-frame callback is fine as long as it is multiplied by delta, so the choice of callback is only a matter of style.
- [ ] B. Each physics step covers the same amount of game time, so jump arcs and collision results are essentially the same on all three machines, apart from how smooth the picture looks.
- [ ] C. A variable step is preferred for physics, because larger steps on slow machines make the simulation more precise.
- [ ] D. The engine can run zero, one or several physics steps for one rendered frame, so the two callbacks are not called equally often.
- [ ] E. With a variable step, a long frame becomes a long step in which a fast body can travel farther than a thin wall is thick, and tunnel through it.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Scaling by delta fixes speed but not collision tests, jump arcs or contact timing, which still vary with the step size.
- B: A constant step removes frame rate from the simulation.
- C: Larger steps make the simulation less accurate and more likely to miss contacts.
- D: Physics catches up or waits to keep its own clock steady.
- E: Long steps skip over thin obstacles.

**Source:** Fixed time step

## MA-ch04.18

In a melee action game a developer tells a coding agent: "when the sword hits the enemy, damage it". The designer wants the team to use three terms in the melee convention: a hitbox is a region that deals damage during an attack, a hurtbox is a region on a character that receives damage, and a body collider is the solid shape that blocks movement. In this game one swing is meant to damage a given enemy once. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The sword's hitbox should be active only during the frames of the swing in which the blade can hurt.
- [ ] B. Each enemy normally has a solid body collider that blocks movement and a separate hurtbox region that receives hits.
- [ ] C. On the enemy, the region that registers an incoming sword hit is its hitbox, and the sword carries the hurtbox.
- [ ] D. A hit is registered when a hitbox overlaps a hurtbox, which is detection, so neither region needs to block movement.
- [ ] E. "Hits the enemy" leaves repeats open; because one swing is meant to damage an enemy once, a precise instruction states that limit.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: An always-on hitbox would damage things the blade is not near.
- B: Blocking and receiving damage are different jobs, so they use different shapes.
- C: The roles are the other way round: the sword carries the hitbox that deals damage, and the enemy carries the hurtbox that receives it.
- D: Both are usually detection regions (areas or triggers).
- E: Overlap lasts several ticks, so without a rule one swing could hit many times.

**Source:** Hitbox versus hurtbox

## MA-ch04.19

A platformer has ledges the player can jump up through from below, then stand on, and drop through when pressing down. In Godot 2D this is a collision shape with one-way collision enabled, which makes the shape collide on one side only. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Enabling one-way collision on a shape that belongs to an Area2D has no effect, because areas do not block anything.
- [ ] B. Dropping through can be done by letting the player briefly stop colliding with the ledge, for example by turning off that shape for a moment.
- [ ] C. The ledge is still a solid collider; it blocks from one side only, normally the top.
- [ ] D. A one-way platform is a trigger that detects the player from below and lifts the player onto it.
- [ ] E. A ledge on a layer that the player's mask does not scan gives the same result, since the player can pass through from below.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The documentation says one-way collision has no effect on a child of an Area2D.
- B: A short collision pause lets the player fall past it.
- C: One-way platforms are solid from one direction and open from the other.
- D: It is a solid collider; triggers do not lift or block anything.
- E: The player would pass through from above as well and would never stand on it.

**Source:** One-way platform

## MA-ch04.20

Lava should hurt the player once every 0.5 s for as long as the player stands in it. The developer wrote "the lava hurts the player when they touch it", and the agent built the lava as an Area2D whose body_entered handler subtracts 1 health. In testing, the player jumps in, loses 1 health once, and then stands in the lava taking no more damage. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The build is correct as written, because "hurts the player when they touch it" means a single hit on contact.
- [ ] B. A fix is a 0.5 s timer that asks which bodies currently overlap the lava and damages each of them.
- [ ] C. body_entered runs once when an overlap begins, so standing still inside the lava produces no further enter events.
- [ ] D. Making the lava's shape bigger would produce repeated enter events while the player stands inside.
- [ ] E. Connecting the same handler to body_exited fixes it, because exit events fire repeatedly while the player stays inside.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The designer wants damage every 0.5 s while inside; the instruction left once-versus-repeatedly unsaid, which is how a single-hit build arose.
- B: Polling the current overlap list repeats the check while the overlap lasts.
- C: The signal reports the start of the overlap only.
- D: Size does not change that entry is a single event.
- E: Exit fires once when the player leaves.

**Source:** Enter events versus continuous overlap

## MA-ch04.21

Three engines name the same idea differently: a region that reports which objects are inside it without blocking them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unreal both objects' responses count: if one is set to Ignore the other's type, no overlap is reported even though the other is set to Overlap.
- [ ] B. In all three engines the region must have a visible mesh or sprite, because detection is done on the drawn pixels.
- [ ] C. In Godot an area detects a body only if the body's collision layer is among the layers in the area's collision mask.
- [ ] D. A detection region finds objects through its collision shape, so a region whose shape has been switched off reports nothing even when objects are inside it.
- [ ] E. In Godot this is an Area2D or Area3D, in Unity a collider with Is Trigger enabled, and in Unreal a collision component whose response to the other object's type is Overlap.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Whether two objects block, overlap or ignore each other depends on both of them; with one side set to Ignore, no overlap events fire.
- B: Detection uses collision shapes; the drawing is irrelevant.
- C: Layer says where an object appears; the area's mask says what it scans.
- D: Detection is computed from collision shapes, so a shape that is switched off takes no part and the region has nothing to report.
- E: Each engine has a non-blocking detection region under its own name.

**Source:** Trigger across engines

## MA-ch04.22

A developer tells a coding agent: "only let the player jump when touching the ground". The player is a CharacterBody2D in Godot. Candidate approaches are is_on_floor(), a short raycast pointing down from the feet, and a small Area2D sensor at the feet. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A feet sensor made from an Area2D detects solid ground only if the area's mask scans the layer the ground is on.
- [ ] B. A ray cast from the feet that returns an empty result means the player is standing on the ground.
- [ ] C. "Touching" is ambiguous: contact with a wall or a ceiling is also touching, so the instruction should say that the contact surface must count as floor.
- [ ] D. is_on_floor() is true whenever the body's shape is anywhere inside a floor shape, since it tests plain overlap.
- [ ] E. is_on_floor() describes the result of the most recent move_and_slide() call, so it reflects the last physics step's movement.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Areas report only bodies whose layer is in their mask.
- B: An empty result means the ray hit nothing, so there is no ground within its length.
- C: Floor, wall and ceiling are different contact surfaces.
- D: It reports contact found by the last move, classified by the surface direction, not an overlap test.
- E: It is updated by move_and_slide() and is not a live overlap test.

**Source:** Ground check, say it to the agent

## MA-ch04.23

A developer replaces a character's sprite with a larger, more detailed drawing and asks a coding agent to "update the character art". Afterwards the character's arms poke into walls, and enemy attacks seem to hit empty air beside the drawing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The physics engine reads the sprite's transparent pixels, so the empty areas of the drawing do not collide.
- [ ] B. Characters are usually given simple shapes such as capsules because they are cheaper to test and move more steadily.
- [ ] C. Scaling the sprite node also scales a sibling collision shape, because they belong to the same character.
- [ ] D. The collision shape is separate from the sprite, so replacing the art does not resize it.
- [ ] E. A debug view (in Godot, Visible Collision Shapes) draws the shapes at runtime and exposes such a mismatch.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Transparency is a rendering property; collision comes from shapes.
- B: Primitive shapes are fast to test and avoid snagging on small details.
- C: A sibling shape is unaffected by the sprite's own scale; only a shared parent's scale reaches both.
- D: Physics reads shapes, not pictures.
- E: Seeing the shape over the art shows where they disagree.

**Source:** Collision shape versus art
