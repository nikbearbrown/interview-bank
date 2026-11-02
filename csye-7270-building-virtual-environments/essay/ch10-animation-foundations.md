# Chapter 10: Animation foundations

## ES-ch10.1

A studio must choose between sprite-sheet (frame-by-frame) animation and rig-based (skeletal) animation for two projects: a small pixel-art platformer with one hero, and a 3D action game with twelve characters that share a humanoid body. For each project, recommend a method and defend it. Your answer should explain what each method stores, what changes from one frame to the next, and how the two differ in memory and art cost, reuse, blending, scaling and look.

**Points:** 5

**Rubric (1 point each):**

1. States what each method stores: a sprite sheet holds many drawn images (in a grid) plus data saying which to show and when, while a rig-based character holds a skeleton, art bound to it, and clips of bone transforms over time.
2. States what changes from frame to frame: the displayed image for a sprite sheet, versus the bone transforms (and therefore the pose of the attached mesh or parts) for a rig.
3. Compares memory and art cost: sprite-sheet cost grows with actions times directions times frames and each new character needs new drawings, while a rig costs more up front (model, skeleton, weights) but its clips are small and cheap to add.
4. Compares reuse, retargeting and blending: characters sharing a skeleton can share and blend clips, while drawn frames do not transfer between characters and cannot be blended into a true in-between pose.
5. Gives a defended recommendation for each project that also names the trade-offs of look and scaling (a fixed hand-drawn look and fixed pixel resolution for sprites, deformation and resolution-independent geometry for rigs).

**Source:** Sprite sheet versus rig-based animation

## ES-ch10.2

A developer types this to a coding agent: 'animate the character walking'. The project contains a character, but the developer has not said whether the art is a sprite sheet or a rigged model. Explain what is wrong with the instruction. Then rewrite it twice, once for each kind of art, using the right terms, and explain what the agent could build wrongly if it guessed, and how you would check the result.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the core ambiguity: the instruction does not say whether the art is frame-by-frame images or a skeleton with bone transforms, so the agent must guess the whole method.
2. Gives a precise sprite-sheet version covering the grid (columns and rows or cell size), which cells make the walk and in what order, the frame rate, and whether it loops.
3. Gives a precise rig version covering the skeleton or model, the named walk clip, its loop mode, whether the motion is in place or uses root motion, and the playback speed or blend with other clips.
4. Describes plausible wrong builds from a wrong guess, such as slicing a sheet with the wrong grid, rotating bones that do not exist, moving the body twice, or playing the walk once instead of looping.
5. Says how the result should be checked, for example by stating the expected observable behaviour (frame order, loop length, speed) so the developer can verify it instead of trusting the agent.

**Source:** Say it to the agent: animate the walk

## ES-ch10.3

Explain the difference between a keyframe, interpolation and easing, using a door that rotates from 0 to 90 degrees over 1 second as your example. Then explain when a developer should use an authored animation clip and when a tween created in code, and give one example of each.

**Points:** 5

**Rubric (1 point each):**

1. Defines a keyframe as an authored value at a chosen time (here 0 degrees at 0.0 s and 90 degrees at 1.0 s).
2. Defines interpolation as computing the in-between values from the keys, for example linearly reaching 45 degrees at 0.5 s.
3. Defines easing as shaping the speed profile of the interpolation (slow in, slow out, fast start) without changing the start value, the end value or the total duration.
4. Explains that an authored clip is made ahead of time, stored with the scene, and editable and scrubbable by a designer, while a tween is created in code to move a property from its current value to a target over a duration, which suits end values only known at runtime.
5. Gives a fitting example for each, such as a designed cutscene door or menu slide as a clip and a health bar easing to a new value or a camera zoom to a runtime target as a tween.

**Source:** Keyframe, interpolation, easing, clip and tween

## ES-ch10.4

Explain what a skeleton (armature), a rig, skinning and vertex weights are, and how they relate. A tester reports that when the character raises an arm, skin near the shoulder stretches in a long web toward the neck and the armpit collapses. Say which of these concepts is most likely involved, what probably went wrong, and how you would describe the problem to an artist or a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines a skeleton (armature) as a hierarchy of bones where moving a parent moves its children, and a rig as the whole posable setup, including the skeleton, the skin binding and controls or constraints.
2. Defines skinning as binding mesh vertices to bones, and vertex weights as per-vertex amounts of influence from each bone, normally summing to 1.
3. Diagnoses the problem as a weighting problem: vertices near the shoulder are influenced by the wrong bones or by too many bones, so they follow the neck or chest when the arm moves.
4. Proposes a fix such as repainting or limiting weights on those vertices and testing at extreme poses, noting that the symptom points first at the weights and that the animation clip's keys are unlikely to be the cause.
5. Describes the problem precisely, naming the bones involved, the vertices or vertex group affected, and the pose in which it appears.

**Source:** Skeleton, rig, skinning and vertex weights

## ES-ch10.5

A character walks down uneven stairs, and its authored walk clip makes the feet hover above some steps and sink into others. Explain forward and inverse kinematics, why the clip alone fails here, and how you would fix it with IK. Then write the instruction you would give a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines forward kinematics as computing the end position (the foot) from joint rotations down a chain, and inverse kinematics as taking a target position for the end of the chain and solving for the joint rotations that reach it.
2. Explains the failure: the keyed rotations know nothing about the stair surface, so the foot goes where the keys put it.
3. Describes the fix: find the ground under each foot (for example with a ray or shape cast) and set the foot as an IK target for its leg chain.
4. Describes how the IK is applied: layered on top of the authored clip and not replacing it, with the hips height adjusted so that both feet can reach their targets.
5. Writes an instruction that names the leg chains (hip, knee, ankle), the knee direction (a pole or hint), the target source, when the IK applies, and how strongly it blends with the clip.

**Source:** Forward versus inverse kinematics

## ES-ch10.6

A developer tells a coding agent: 'make the character walk forward at 3 metres per second using the walk clip'. The walk clip was authored so that the root bone travels 1.2 metres forward in each 1.0 second loop. Explain root motion and in-place animation, say what could go wrong with this instruction, and rewrite it precisely.

**Points:** 5

**Rubric (1 point each):**

1. Defines root motion as applying the root bone's movement in the clip to the character's position in the world, and in-place animation as a clip that poses the limbs without moving the character, leaving travel to code or physics.
2. Identifies the double-movement risk: if the code moves the body at 3 m/s and root motion is also applied, the character moves about 4.2 m/s.
3. Identifies the foot-sliding risk: if root motion is ignored and code moves at 3 m/s, the feet were planted for 1.2 m per loop, so they slide unless the playback speed or blend is changed.
4. Rewrites the instruction by choosing one authority, for example an in-place walk, code-set speed of 3 m/s, and playback speed scaled to match, or root motion as the authority with code reading it.
5. Gives the rewrite its numbers: the 3 m/s target, the clip's 1.2 m per 1.0 s loop, and the playback-speed factor of 3 / 1.2 = 2.5 that the agent should apply, so that nothing is left for it to guess.

**Source:** Root motion versus in-place animation

## ES-ch10.7

A script moves a platform by 2 units every time the engine draws a frame, and a tester finds that the platform is much faster on a 144 frames per second monitor than on a 60 frames per second one. Explain why, with numbers, how to fix it, and what frame-rate independence means for animation clips and for sprite-sheet frame rates. Write the instruction you would give a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the movement is tied to the number of frames drawn, so the speed is 2 × 60 = 120 units per second at 60 frames per second and 2 × 144 = 288 units per second at 144.
2. Fixes it by defining the speed in units per second and multiplying by the time elapsed since the previous frame (delta time).
3. Defines frame-rate independence as results that depend on elapsed time and not on how many frames were drawn, which does not require locking the frame rate.
4. Explains that clips advance by time and have a playback speed scale, and that a sprite sheet's frame rate is the animation's own rate (for example 12 drawn frames per second shown across several rendered frames), separate from the rendering rate.
5. Writes an instruction that states the speed in units per second, requires scaling by delta time (or using the engine's fixed physics step), and forbids per-frame increments.

**Source:** Playback speed and frame-rate independence

## ES-ch10.8

A designer wants a sword swing's damage hitbox to be on only during the part of the swing where the blade is sweeping, and a whoosh sound to play at the start of that part. Explain what an animation event (a method track) is, why putting these on the clip is usually better than starting timers in code, and what can still go wrong. Write the instruction you would give a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines an animation event or method track as a function call keyed at a time on the clip's timeline, run when playback reaches that time.
2. Explains the benefit: the timing travels with the clip, so it stays aligned when the playback speed changes, the clip is retimed, or the clip is replaced, and a designer can move it without editing code.
3. Explains the weakness of code timers: they run on their own clock, independent of the clip's playback speed and of interruptions, so they drift from the visuals and duplicate timing knowledge in two places.
4. Names what can still go wrong, such as events firing on the update in which the playhead crosses the key (possibly a frame late), or never firing if the clip is cancelled early, so the hitbox must also be turned off when the state is exited or interrupted.
5. Writes an instruction that names the clip, the times or phases, the functions to call, and what must happen on cancel or interrupt.

**Source:** Animation events and hitbox timing

## ES-ch10.9

Playtesters say two things about a character: its run cycle 'hitches' once per loop, and switching from walk to run 'pops'. Explain the likely causes in each case and the fixes, for a sprite-sheet character and for a rig-based character. Then write the instruction you would give a coding agent to fix the loop.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the usual loop-seam cause: the last frame duplicates the first or does not lead naturally into it, so a pose repeats or jumps at the seam.
2. Gives fixes for the loop: drop the duplicated frame or adjust the end pose, and for a rig make the start and end values match with an appropriate loop mode.
3. Explains the pop on switching as an instant cut between two different poses.
4. Gives the fix for the pop: for a rig, cross-fade or blend the bone transforms over a short time or use a blend by speed, and for a sprite sheet, which cannot blend frames into a true in-between pose, switch at a matching point in the cycle or add transition frames.
5. Writes a precise instruction for the loop, such as the exact frames to play, the frame rate, and the loop mode, so the agent does not choose them.

**Source:** Loops, blending and clip switching
