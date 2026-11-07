# Jargon test: camera and animation (essay)

## ES-jargon.1

A producer types this to a coding agent: "Make the camera swoop in on the boss, then pan back out to show the arena." Explain what is imprecise or wrong in the wording. Then rewrite the instruction using exact camera terms for two readings: one where the camera body moves, and one where only the lens changes. Say what the viewer would see differently between the two.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that "pan" is the wrong word for moving back out, since a pan is a rotation on the spot and does not change position.
2. Names "swoop in" as vague and replaces it with an exact move: a dolly in (camera body moves forward along its view direction), possibly with an orbit or a curved path.
3. Gives a rewrite for the camera-body reading using dolly in and dolly out, with a duration and easing.
4. Gives a rewrite for the lens reading using a zoom (field of view or focal length narrows and then widens) with the camera position unchanged.
5. Explains the difference seen: a dolly changes parallax between near and far objects, while a zoom magnifies the same view without that shift.

**Source:** Rewrite a vague camera prompt

## ES-jargon.2

Define each of these terms in one or two sentences, and give one example of when a game camera would use it: deadzone, look-ahead, screen shake, camera limits.

**Points:** 5

**Rubric (1 point each):**

1. Defines a deadzone as a screen region where the target can move without the camera moving, and gives a use such as avoiding camera motion on small player movements.
2. Defines look-ahead as shifting the framing toward the direction of travel, and gives a use such as showing more of the level ahead of a fast runner.
3. Defines screen shake as a brief, decaying random offset of camera position or rotation, and gives a use such as an explosion or hit.
4. Defines camera limits (bounds) as clamps that keep the camera from showing space outside the level, and gives a use such as level edges.
5. Uses each term in its own sense without mixing them up (for example, does not describe the deadzone as shake or limits as smoothing).

**Source:** Camera framing vocabulary

## ES-jargon.3

A student says, "A zoom and a dolly are the same: both make the subject bigger." Correct this using exact terms. Explain what each changes on the camera, what the viewer sees in each case, and name one situation where each is the better choice.

**Points:** 5

**Rubric (1 point each):**

1. States that a zoom changes the lens (field of view or focal length) and the camera does not move.
2. States that a dolly moves the camera body along its view direction and changes the field of view not at all.
3. Explains that a dolly changes perspective and parallax between near and far objects, while a zoom keeps the same viewpoint and only magnifies.
4. Names a situation where a zoom suits (for example a fast scope or sniper view, or a UI-style punch-in) and one where a dolly suits (for example moving through a space so depth is felt).
5. Uses the terms consistently throughout, including "field of view" for the lens angle.

**Source:** Zoom versus dolly

## ES-jargon.4

Write the exact words you would give a coding agent to build a 2D platformer follow camera that feels smooth. Use at least five precise camera terms (for example follow, smoothing or damping, deadzone, look-ahead, camera limits, screen shake) and say what value or behaviour you want for each.

**Points:** 5

**Rubric (1 point each):**

1. Names a follow camera that tracks the player and states the target.
2. Sets smoothing (damping) with a value or behaviour, such as trailing slightly and catching up in a fraction of a second.
3. Sets a deadzone with a size or behaviour, so small movements do not move the camera.
4. Sets look-ahead with a distance or direction rule, and camera limits at the level bounds.
5. Uses the terms correctly and adds a way to check the result, such as stating the observable behaviour (no jitter, no view outside the level).

**Source:** Follow-camera tuning words

## ES-jargon.5

Explain the difference between a keyframe, interpolation, easing and a tween, using a door that opens from 0 to 90 degrees in one second as the example. Then say when you would author a clip and when you would write a tween in code.

**Points:** 5

**Rubric (1 point each):**

1. Defines a keyframe as a stored value at a specific time, such as 0 degrees at 0 seconds and 90 degrees at 1 second.
2. Defines interpolation as computing the in-between values between keyframes.
3. Defines easing as the shape of the speed over time (for example slow start, fast finish), without changing the end values.
4. Defines a tween as a code-driven interpolation of a property over a duration, usually with an easing setting.
5. Says when each tool fits: authored clips for designed, reusable motion on a rig or sprite, and tweens for quick procedural effects such as a UI pop-up.

**Source:** Keyframe, interpolation, easing and tween

## ES-jargon.6

A student writes: "Animate the sprite sheet with bones and use IK to cut it into frames." Identify the wrong words and explain each. Then write a correct instruction for a sprite-sheet character and a correct instruction for a rigged 3D character, each with exact terms.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that bones do not belong to a sprite sheet, which is a grid of image frames.
2. Identifies that IK is a technique that solves joint angles to reach a target, and does not cut anything into frames.
3. Gives a correct sprite-sheet instruction naming the grid (columns and rows or cell size), which frames and in what order, frame rate, and loop.
4. Gives a correct rigged-character instruction naming the rig or skeleton, the clip, loop mode, and in-place versus root motion.
5. Notes that mixing the two methods in a prompt can make the agent guess, and says how to state the method up front.

**Source:** Spot the wrong word in an animation prompt

## ES-jargon.7

Explain root motion and in-place animation. A student's walking character slides over the floor and also travels twice as far as expected. Diagnose the problem with exact terms and write the instruction that fixes it.

**Points:** 5

**Rubric (1 point each):**

1. Defines root motion as movement baked into the clip that drives the character's root through the world.
2. Defines in-place animation as a clip that keeps the root still while script code supplies the travel.
3. Diagnoses double movement: the clip uses root motion while the script also moves the body at walking speed.
4. Diagnoses sliding as a mismatch between the travel speed and the speed of the feet in the clip.
5. Writes a precise fix, such as use an in-place clip and let the script move the body, or use root motion and remove the script movement, and match speed to the clip.

**Source:** Root motion diagnosis

## ES-jargon.8

Compare a state machine and a blend tree for a 3D character who idles, walks, runs, jumps and lands. Say which tool handles which job, define a transition and a parameter, and write one sentence each that you would give an agent to build the locomotion blend and the jump logic.

**Points:** 5

**Rubric (1 point each):**

1. Defines a state machine as named states with transitions between them, one active at a time.
2. Defines a blend tree as a weighted mix of clips driven by a parameter such as speed.
3. Assigns the idle, walk and run mix to a blend tree on speed, and jump and land to states with transitions.
4. Defines a transition as a rule with a condition (for example "on the ground changes to false") and a parameter as a named value the logic reads.
5. Gives two precise agent instructions that name the parameter, the clips and the transition conditions.

**Source:** State machine versus blend tree
