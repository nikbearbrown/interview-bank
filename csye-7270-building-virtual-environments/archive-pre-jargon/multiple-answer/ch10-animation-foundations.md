# Chapter 10: Animation foundations

## MA-ch10.1

A 2D developer receives character art as one PNG file containing a regular grid of equally sized drawings of the same character in successive poses. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The engine must be told the grid layout (columns and rows, or cell size), because the pixels do not mark frame boundaries.
- [ ] B. The file is a sprite sheet, and showing its cells one after another at a chosen rate gives frame-by-frame animation.
- [ ] C. A sprite sheet and a tilemap are the same thing, because both cut one image into a grid of cells that are drawn from a single texture.
- [ ] D. The PNG is itself an animation clip, because the image file records the order and the duration of each frame it contains.
- [ ] E. A texture atlas usually packs images of different sizes into one texture and keeps a table of their rectangles.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The file carries no grid metadata, so the developer or the import settings must supply columns and rows or the cell size.
- B: A sprite sheet stores the frames of an animation in one image, and playing the cells in sequence at a frame rate is frame-by-frame animation.
- C: A tilemap places reusable tiles on a level grid to build a map, while a sprite sheet's cells are poses meant to be played in sequence.
- D: An image holds only pixels; the order, timing and looping come from a frames resource or animation data that references the image.
- E: An atlas is a general packing of many images with a lookup table, whereas a classic sprite sheet relies on a regular grid of equal cells.

**Source:** Sprite sheet versus atlas versus tilemap

## MA-ch10.2

Two teams animate the same walking hero. Team 1 ships a sprite sheet of hand-drawn walk frames. Team 2 ships a 2D cutout character: separate body-part images attached to a skeleton, with a walk clip that rotates and moves the bones. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Team 2's walk clip stores the pixels of each pose, one complete image per frame, packed together with the bone data.
- [ ] B. Team 1's version needs a skeleton to play, because bones are what position each drawn frame on the screen.
- [ ] C. Team 1's animation is mostly pixels: many drawn images, plus a clip saying which image to show and when.
- [ ] D. Between frames, Team 1's animation changes which image is shown, while Team 2's changes bone transforms and so the pose of the parts.
- [ ] E. If Team 2 wants a longer walk cycle, it must redraw the body-part images for each additional pose in the cycle.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: A skeletal clip stores transform keys (rotations, positions) over time, and the part images stay the same in every pose.
- B: Frame-by-frame animation needs no skeleton, since each frame is a complete picture.
- C: A sprite-sheet clip is a sequence of references into drawn frames with timing.
- D: Frame-by-frame swaps images; skeletal animation changes bone transforms and lets the attached art follow.
- E: A new or longer clip only adds keys for the bones; the part images are reused unchanged.

**Source:** What is stored: sprite sheet versus rig

## MA-ch10.3

A sprite sheet image is 512 × 256 pixels. It is a regular grid of 64 × 64 pixel cells with no gaps, numbered from 0, left to right and row by row, starting at the top-left cell. A developer asks a coding agent to 'play the run animation from the sheet' and says nothing else about the file. The run drawings are the eight cells of the second row. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The words 'the run animation' are enough for the agent, because the image file records which cells belong to which animation.
- [ ] B. The sheet has 8 columns and 4 rows, so 32 cells in all.
- [ ] C. If the agent wrongly assumes 4 columns and 8 rows, it will cut cells of 128 × 32 pixels and show mis-sliced pictures without raising any error.
- [ ] D. Showing the eight run cells at 10 frames per second makes one loop last 1.25 seconds.
- [ ] E. Cell 19 begins at pixel x = 192, y = 128, measured from the top-left corner of the image.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A plain image has no record of animation names; the developer must say which cells form the run and in what order.
- B: 512 / 64 = 8 columns and 256 / 64 = 4 rows, giving 32 cells.
- C: A wrong grid still divides the image into cells (512 / 4 by 256 / 8 gives 128 × 32), so nothing fails but the slices are wrong.
- D: Eight frames at 10 frames per second last 8 / 10 = 0.8 seconds.
- E: Cell 19 is in column 19 mod 8 = 3 and row 19 div 8 = 2, so x = 3 × 64 = 192 and y = 2 × 64 = 128.

**Source:** Sprite sheet grid and describing it to an agent

## MA-ch10.4

A game has one hero with 4 actions, each drawn in 8 facing directions with 8 frames per action per direction. Every frame is a 96 × 96 pixel image stored uncompressed at 4 bytes per pixel. A second plan uses a 3D model of the hero with a skeleton and one clip per action, and the model turns to face any direction by rotating. Ignore compression and mipmaps. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The sprite version holds 256 frames, which is 9,437,184 bytes (9 MiB) uncompressed.
- [ ] B. Choosing the skeleton plan removes the up-front art cost, because the skeleton and the clips need no authoring.
- [ ] C. Adding a ninth facing direction to the sprite version adds 8 frames to draw.
- [ ] D. Drawing each frame at 48 × 48 pixels instead would cut that to 2.25 MiB, a quarter of the size and not a half.
- [ ] E. A rig-based walk clip stores a full image for each pose of the walk.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: 4 × 8 × 8 = 256 frames, each 96 × 96 × 4 = 36,864 bytes, for 9,437,184 bytes, exactly 9 MiB.
- B: Modelling, texturing, rigging, weight painting and clip authoring are real up-front costs; they trade per-frame drawing for one-off setup.
- C: A ninth direction needs 4 actions × 8 frames = 32 new frames.
- D: Halving both sides quarters the pixel count: 256 × 48 × 48 × 4 bytes = 2.25 MiB.
- E: A skeletal clip stores transform keys per bone over time, which is far smaller than full images.

**Source:** Memory and art cost of sprite sheets versus rigs

## MA-ch10.5

A studio owns a 3D walk clip authored for Character X's skeleton. Character Y has a different mesh and different limb lengths, but a skeleton whose bones (hips, spine, arms, legs) correspond one for one to X's. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With different limb lengths, a retargeted walk can make feet slide or float, which IK or foot-contact fixes often correct.
- [ ] B. Retargeting maps a source skeleton's motion onto a target skeleton by pairing bones, so X's clip can drive Y.
- [ ] C. A sprite-sheet walk drawn for X can be reused for Y by mapping Y's bone names onto the sheet's cells.
- [ ] D. A humanoid clip cannot drive a four-legged skeleton without a custom mapping, as the bones do not correspond.
- [ ] E. Differently dressed characters that share one skeleton can share clips, because a clip stores bone motion, not pixels.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Different proportions change where the feet end up, so contact points are typically re-solved with IK.
- B: Retargeting pairs source bones with target bones so the motion transfers.
- C: A sprite sheet has no bones; its frames are drawings of one character and cannot be remapped to another.
- D: Without corresponding bones there is nothing to pair, so a manual mapping or new authoring is needed.
- E: Clips address bones by name or path, so any mesh bound to the same skeleton can play them.

**Source:** Reuse and retargeting

## MA-ch10.6

A character has a walk clip and a run clip. As the player's speed rises from walking pace to running pace, the designer wants the motion to change smoothly instead of switching abruptly. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A blend weight of 0.5 between walk and run makes the character play the result at half speed, since the weight sets the rate.
- [ ] B. For a rig-based character, the engine can blend two poses by interpolating each bone's transform, weighted by a blend value.
- [ ] C. Mixing the pixels of two sprite frames gives a ghosted double image, not an in-between pose, so sprite sheets usually switch clips.
- [ ] D. Blending suits 3D characters but not 2D cutout ones, since flat art has no bones whose transforms can be interpolated.
- [ ] E. Smooth speed changes require a separately authored clip for each intermediate speed between walking and running pace.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The blend weight mixes poses; playback speed is a separate setting.
- B: Skeletal clips are bone transforms, which can be interpolated per bone to produce an in-between pose.
- C: A cross-fade of two drawings overlays both; it does not create the drawing that lies between them.
- D: 2D skeletal (cutout) rigs have bones too, so their poses can be blended like 3D ones.
- E: Blending two clips by weight produces the intermediate motions without authoring each one.

**Source:** Blending

## MA-ch10.7

A game ships on 1080p and 4K screens. The art lead compares a sprite sheet drawn at 64 × 64 pixels per frame with a skeletal 3D character that is drawn from its mesh each frame. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 3D character is drawn from its mesh at screen resolution, so its sharpness is not locked to a fixed frame pixel size.
- [ ] B. Switching a magnified pixel-art sprite to linear filtering makes its edges crisper by sharpening each pixel boundary.
- [ ] C. To gain real detail at 4K, a sprite sheet's frames must be redrawn or re-exported at the larger size.
- [ ] D. A 2D cutout rig built from bitmap parts is resolution independent, because bones rescale the bitmaps without loss.
- [ ] E. Showing 64 × 64 sprite frames larger than drawn magnifies their pixels, which look blocky (nearest) or blurry (linear).

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Geometry is rasterized for the current screen each frame, so only the textures stay at a fixed resolution.
- B: Linear filtering blends neighbouring pixels, which softens edges; nearest-neighbour keeps them crisp.
- C: New detail cannot be invented by scaling; the frames must be authored or exported at the higher resolution.
- D: The parts are still bitmaps with a fixed pixel size, so enlarging them softens or blocks them just like a sprite.
- E: A sprite frame holds a fixed number of pixels, so enlarging it either shows the pixel blocks or smooths them into blur.

**Source:** Resolution and scaling

## MA-ch10.8

An animator wants a cartoon character to squash flat on landing and to show a drawn smear on a fast punch. A separate 3D character must bend an elbow without the mesh pinching. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A rig reuses one set of art and only changes its pose, so an unmodelled shape such as a smear needs extra deformation.
- [ ] B. A skinned mesh can take any silhouette a hand-drawn frame can, because bones can move vertices anywhere the animator wants.
- [ ] C. Rotating the rigid body parts of a 2D cutout character around joints can open gaps or overlaps at the joints.
- [ ] D. Hand-drawn frames can take any shape, including squash and smear, because each frame is an independent picture.
- [ ] E. Skinning with vertex weights lets one mesh bend smoothly at a joint instead of splitting into rigid pieces.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A rig changes pose, not the underlying shapes; effects like smears need extra tools such as blend shapes or swapped parts.
- B: The silhouette is limited by the mesh, its weights and the bone motion, so arbitrary drawn shapes are not available.
- C: Rigid parts rotating about a joint do not stay joined at the edges, so artists hide the joint or use deformation.
- D: Each drawn frame is free-form, which is why exaggerated shapes are easy in frame-by-frame work.
- E: Skinning blends the influence of neighbouring bones on shared vertices, producing a smooth bend.

**Source:** Fixed look versus deformation

## MA-ch10.9

A producer lists four animation methods in a planning document: frame-by-frame, cutout, procedural and tweening. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A procedural animation is a fixed recording, so its pose does not change with the terrain it plays on.
- [ ] B. Tweening computes in-between values of a property from a start to an end value over a duration, often with easing.
- [ ] C. Procedural animation is the name for any animation authored by keys on a timeline in an animation editor.
- [ ] D. Frame-by-frame animation depends on a skeleton to move its pieces, with roughly one bone for each drawn piece of the figure.
- [ ] E. Cutout animation needs a fresh drawing of the whole figure for the next pose, which is why its memory use is high.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Procedural motion responds to conditions such as terrain or forces, so it can differ from one playback to the next.
- B: That is what a tween does: it generates the in-between values for a property between two endpoints.
- C: Keys on a timeline describe authored animation; procedural animation is computed at runtime from rules, physics or targets.
- D: Frame-by-frame animation swaps whole drawings and needs no skeleton.
- E: Cutout animation moves separate reusable pieces, such as limbs and a head, instead of redrawing the whole figure.

**Source:** Cutout, procedural, tween and frame-by-frame

## MA-ch10.10

An animator keys a door's rotation to 0 degrees at 0.0 s and to 90 degrees at 1.0 s, and sets nothing else. The game renders 60 frames per second and the engine uses linear interpolation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The clip stores 60 rotation values, one for each rendered frame in that second.
- [ ] B. With only two keys, the door jumps from 0 to 90 degrees, since nothing is keyed in between.
- [ ] C. A display refreshing twice as often needs the clip to be re-authored with twice as many keys.
- [ ] D. At t = 0.5 s the door's rotation is 45 degrees, halfway between the two keyed values.
- [ ] E. The two keys are keyframes, and the engine computes the values between them as the clip plays.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The clip stores two keys; values for rendered frames are computed from time when the clip plays.
- B: Interpolation produces every value between the keys, so intermediate angles are shown.
- C: Values are sampled from time, so any display rate works with the same keys.
- D: Linear interpolation halfway between 0 and 90 degrees gives 45 degrees.
- E: A keyframe is an authored value at a chosen time, and interpolation fills in the in-betweens.

**Source:** Frame, keyframe and interpolation

## MA-ch10.11

A menu panel slides from x = 0 to x = 300 pixels over 0.5 s. With linear motion, the fraction of the distance covered at time t is t / 0.5. With a quadratic ease-out, it is 1 − (1 − t / 0.5)². Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With linear motion the panel is at x = 150 when t = 0.25 s, halfway through the move.
- [ ] B. With the ease-out the panel is at x = 225 when t = 0.25 s, three quarters of the way there.
- [ ] C. With the ease-out the panel moves fastest at the start and slows to a stop at the end of the move.
- [ ] D. The ease-out finishes before the linear version, because it covers more distance early.
- [ ] E. The ease-out changes the final position, since only linear motion ends at x = 300.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: At t = 0.25 s the linear fraction is 0.5, so x = 150.
- B: The ease-out fraction is 1 − (1 − 0.5)² = 0.75, so x = 225.
- C: The curve's slope starts at 1,200 pixels per second (against 600 for linear) and falls to 0 at the end.
- D: Easing reshapes the speed profile only; both versions finish at 0.5 s.
- E: Both curves reach a fraction of 1 at t = 0.5 s, so both end at x = 300.

**Source:** Easing

## MA-ch10.12

A developer sets up a door that opens, using an engine with an animation player node and animation clips. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If a track's target is renamed or moved, the track may no longer find it and silently animate nothing.
- [ ] B. A timeline is the time axis on which a clip's keys sit, and scrubbing it moves a playhead to preview values.
- [ ] C. The animation player plays clips: it advances time, applies values to targets, and handles looping and speed.
- [ ] D. A clip is data: tracks, each bound to a target such as a node property or a bone, with keys along time.
- [ ] E. A clip can animate only one property of one object, so a door needs one clip for each property.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Tracks refer to targets by path or name, so a changed path can leave a track pointing at nothing without failing loudly.
- B: The timeline is where keys are placed in time, and the playhead shows the current time.
- C: The player node applies a clip's values to its targets over time.
- D: A clip is a resource of tracks and keys; it does nothing until something plays it.
- E: A clip commonly holds many tracks, each animating a different property or object.

**Source:** Clip, timeline and animation player

## MA-ch10.13

A producer tells a developer that a character 'needs a rig'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The skeleton is visible geometry that draws the character's body on screen in the final game.
- [ ] B. A skeleton (armature) is a hierarchy of bones in which moving a parent bone moves its children.
- [ ] C. A rig is the full posable setup: skeleton, skin binding and often controls such as IK handles.
- [ ] D. A skeleton alone holds no walking motion; a walk is a separate clip keying bone transforms over time.
- [ ] E. Skinning binds mesh vertices to bones so that the mesh follows the bones when they move.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Bones are not rendered by default; the mesh or parts are what appear on screen.
- B: Bones are parented in a hierarchy so that a shoulder rotation carries the arm with it.
- C: 'Rig' names the whole setup that makes a character posable and animatable.
- D: A skeleton only holds the structure and pose; motion comes from clips, code or solvers that change its transforms.
- E: Skinning ties vertices to bones with weights so that bone motion deforms the mesh.

**Source:** Skeleton, armature, rig and skinning

## MA-ch10.14

Under linear blend skinning, a vertex's final displacement is the weighted sum of the displacements that each influencing bone would give it. A vertex near an elbow is influenced by the upper-arm bone with weight 0.75 and the forearm bone with weight 0.25. In one pose, the upper-arm bone alone would move this vertex by (+10, 0) units and the forearm bone alone would move it by (0, +20) units from its rest position. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The vertex moves by (7.5, 5.0).
- [ ] B. Painting vertex weights changes the keys stored in the animation clip.
- [ ] C. Vertex weights are one number per bone for the whole mesh, so a bone pulls the elbow and the wrist equally.
- [ ] D. If the weights were changed to 1.0 for the upper arm and 0.0 for the forearm, the vertex would move by (10, 0), following the upper arm rigidly.
- [ ] E. A vertex's weights are normally kept so that they sum to 1, which they do here.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: 0.75 × (10, 0) + 0.25 × (0, 20) = (7.5, 0) + (0, 5) = (7.5, 5.0).
- B: Weights belong to the skin binding; clip keys are separate data that move the bones.
- C: Weights are stored per vertex, so each vertex has its own mix of bone influences.
- D: With all the weight on one bone, the vertex copies that bone's displacement.
- E: Normalized weights sum to 1 so that the blended result stays on the scale of the bones' motion; 0.75 + 0.25 = 1.

**Source:** Skinning and vertex weights

## MA-ch10.15

A character walks down uneven stairs. The animator keyed each leg's hip, knee and ankle rotations in the walk clip. The programmer wants each foot to rest on the actual surface of every step. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With only keyed rotations, the foot lands wherever the keys put it, so on unseen steps it can hover or sink.
- [ ] B. Adding IK to the legs means the authored clip is no longer used for them, since IK computes the leg poses itself.
- [ ] C. A target farther than the chain's total length can be reached if the joint rotations are solved precisely.
- [ ] D. Inverse kinematics takes a target for the end of a chain, such as a foot, and solves the joint rotations.
- [ ] E. Forward kinematics starts from the target position of the foot and works backward to find the hip rotation.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Keyed rotations know nothing about the stairs, so foot height follows the clip and not the surface.
- B: IK is usually layered on top of the clip to adjust the legs, while the clip still drives the rest of the pose.
- C: Rotation cannot lengthen bones, so a target beyond reach is only approached with the chain fully extended.
- D: IK works from a desired end position to joint angles.
- E: That describes IK; forward kinematics starts from joint rotations and computes where the foot ends up.

**Source:** Forward versus inverse kinematics

## MA-ch10.16

A walk clip's root bone travels 1.2 m forward during each 1.0 s loop. A developer tells a coding agent 'make the character walk forward when I press up' and does not say whether the clip's root motion is used. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Root motion lets gameplay code choose any walking speed without making the feet slide, as the clip adapts.
- [ ] B. A clip authored in place carries root translation, which root motion can extract and apply to the body.
- [ ] C. In-place animation moves the character through the world by itself, because the changing pose carries the root bone forward.
- [ ] D. Root motion means the clip is played in place, without moving the character through the world, so the root bone stays at the origin.
- [ ] E. If root motion moves the character and code also moves the body, the character covers the distance twice.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The feet are planted for the distance the clip covers, so any other speed from code makes them slide.
- B: A clip authored in place has no root translation, so there is nothing to extract.
- C: An in-place clip poses the limbs but leaves the character's position to code or physics.
- D: Root motion is the opposite: the root bone's movement in the clip is applied to the character's position.
- E: Two sources of forward movement add up, so the character moves faster than either alone intends.

**Source:** Root motion versus in-place animation

## MA-ch10.17

A hand-drawn run cycle has 8 frames shown at 12 frames per second in a looping clip. The artist drew frame 8 as an exact copy of frame 1 so that the cycle 'closes'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A ping-pong mode (forward, then backward) is a good substitute for a run cycle because reversed footsteps look the same as forward ones.
- [ ] B. Removing the duplicate frame leaves 7 distinct frames, so one cycle lasts about 0.58 s at 12 frames per second.
- [ ] C. On each loop, frame 8 is followed by frame 1, so the same drawing shows on two consecutive frames, a small hitch.
- [ ] D. At 12 frames per second, each frame stays on screen for about 12 ms before the next one.
- [ ] E. For a seamless loop, the last frame of a clip must be an exact copy of the first frame, so no pose is skipped.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A run cycle is not symmetric in time, so playing it backward makes the feet step the wrong way.
- B: 7 frames at 12 frames per second last 7 / 12 ≈ 0.583 s.
- C: With the last frame equal to the first, the loop repeats one pose for two frames in a row.
- D: Each frame lasts 1 / 12 s, about 83 ms.
- E: A seamless loop needs the pose after the last frame to lead naturally into the first; a duplicated end frame causes a repeated pose.

**Source:** Loops and the loop seam

## MA-ch10.18

Script 1 turns a fan blade by adding 3 degrees every time the engine draws a frame. Script 2 turns it by 180 degrees per second multiplied by the time since the previous frame (delta time). Both run on a machine drawing 30 frames per second and on one drawing 120. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Script 2 turns the blade at about 180 degrees per second on both machines, scaled by elapsed time.
- [ ] B. Frame-rate independence requires the game to be locked to one constant frame rate, such as 60.
- [ ] C. A clip played with a playback speed scale of 2 takes twice as long to finish as at normal speed.
- [ ] D. Script 1 turns the blade four times faster on the 120 frames per second machine than on the 30 one.
- [ ] E. On the 30 frames per second machine, Script 1 turns the blade at 90 degrees per second.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Multiplying a per-second rate by delta time gives the same movement per second whatever the frame rate.
- B: Frame-rate independence means results do not depend on the frame rate, which is achieved by scaling with elapsed time and not by locking the rate.
- C: A speed scale of 2 makes the clip play twice as fast, so it finishes in half the time.
- D: At 120 frames per second Script 1 turns 3 × 120 = 360 degrees per second, which is 4 times 90.
- E: 3 degrees × 30 frames per second = 90 degrees per second.

**Source:** Playback speed and frame-rate independence

## MA-ch10.19

A sword swing clip lasts 0.6 s. The designer wants the damage hitbox on from 0.20 s to 0.35 s and a whoosh sound at 0.20 s. Option 1 starts a 0.20 s timer in code when the swing begins. Option 2 puts animation events (a method-call track) in the clip at 0.20 s and 0.35 s. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Using events means the hitbox times have to be changed by editing code, not in the animation editor.
- [ ] B. At 1.5 times playback speed, Option 2's events stay aligned with the swing, while Option 1's timer does not.
- [ ] C. An animation event calls a function when playback passes its keyed time, so the timing travels with the clip.
- [ ] D. If the swing is cancelled at 0.10 s, the 0.20 s event of Option 2 still fires, because events are scheduled when the clip starts.
- [ ] E. Events fire at exactly 0.2000 s on the real-world clock, even at a low frame rate, because they are timer-based.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The time is a key on the clip, so it can be moved in the animation editor without touching code.
- B: Events live in clip time, which scales with playback speed, while a code timer counts real time.
- C: An event is keyed on the clip's own timeline and runs when playback reaches it.
- D: Events are reached by playback; a clip stopped before 0.20 s never gets there, so cleanup such as turning the hitbox off must also happen on cancel.
- E: Events are checked each animation update, so they fire on the update in which the playhead crosses the key, which can be a frame later.

**Source:** Animation events and method tracks

## MA-ch10.20

A project contains one image file, hero.png. A developer types to a coding agent: 'animate the character walking', without saying what kind of art hero.png holds. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The word 'walking' tells the agent how many frames the walk has and in which order the cells are numbered.
- [ ] B. Walking is a looping action at a standard pace, so the instruction needs no mention of looping or speed.
- [ ] C. If the agent assumes the image is rigged, it may rotate bone nodes that do not exist or invent body parts.
- [ ] D. From those words alone the agent cannot tell whether to slice frames from a grid or drive bone transforms, so it may guess wrong.
- [ ] E. A precise version says hero.png is a 6 × 1 sprite sheet of 64 × 64 frames, played as a looping walk at 10 fps.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Frame count is a property of the art, not of the word 'walking'.
- B: Whether a clip loops and how fast it plays are settings the agent would otherwise choose by default.
- C: Applying skeletal techniques to flat frames produces code that targets things that do not exist.
- D: Sprite-sheet and rig-based animation are built differently, and the sentence names neither.
- E: It states the art type, grid, frame size, loop and rate, leaving little to guess.

**Source:** Say it to the agent: animate the walk

## MA-ch10.21

In a 3D game the character must reach for a cup that the player can place anywhere on a table. The project has one authored reach clip, keyed to reach straight ahead at a fixed height. A developer tells a coding agent: 'play a reach animation toward the cup'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A precise instruction asks for inverse kinematics on the arm chain with the cup's position as target, layered on an idle clip.
- [ ] B. Blending several authored reach clips with a blend space is another approach, but it covers only positions between those clips.
- [ ] C. A target alone leaves the elbow direction ambiguous, so the instruction may name the chain's bones and elbow hint.
- [ ] D. The authored clip reaches only the one place it was keyed for, so it cannot follow a cup placed elsewhere.
- [ ] E. Asking for forward kinematics makes the hand go to the cup, because forward kinematics starts from the target position.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: IK solves joint rotations from a target position, and it can be applied on top of other animation.
- B: A blend space interpolates between the authored poses, so it cannot reach outside their range.
- C: Many joint configurations reach the same point, so the elbow direction (a pole or hint) and the chain's bones need to be specified.
- D: Keyed rotations are fixed data and know nothing about where the cup is.
- E: Forward kinematics computes the hand position from joint rotations; it does not take a target.

**Source:** Say it to the agent: reaching with IK

## MA-ch10.22

A developer asks a coding agent for two effects. Effect 1 is a pause panel that slides in from the left over 0.25 s, which the designer wants to scrub and retime on a timeline. Effect 2 is a health bar that eases from its current width to a new width every time the player is hit, where the new width is not known in advance. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Effect 2 suits a tween created in code when the hit happens, because its end value only exists at runtime.
- [ ] B. Effect 1 suits an authored clip, since its values are known ahead and a designer wants to edit them.
- [ ] C. A tween is authored as keys in the scene file so that a designer can scrub it on a timeline in the editor.
- [ ] D. Easing applies only to authored clips; a tween has no easing setting and moves at constant speed to its target.
- [ ] E. A tween takes a duration and an easing curve, so the word 'smoothly' should be replaced by those values.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A tween interpolates from the current value to a target supplied when it is created.
- B: A clip is authored ahead of time, stored with the scene and editable and scrubbable by designers.
- C: A tween is created and run from code, and it is not stored as editable keys.
- D: Tweens normally accept an easing curve like clips do.
- E: 'Smoothly' leaves duration and curve to the agent; naming them removes the guess.

**Source:** Say it to the agent: tween versus clip

