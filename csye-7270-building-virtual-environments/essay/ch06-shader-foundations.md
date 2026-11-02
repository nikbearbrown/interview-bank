# Chapter 6: Shader foundations

## ES-ch06.1

In an interview for a graphics or technical-art role you are asked: "What is a fragment?" Answer as you would to a colleague who must give a coding agent precise instructions. Define the term, say how a fragment differs from a pixel and from a vertex, and use a concrete example with numbers (for instance a quad with four vertices, or two overlapping triangles) to show how many of each exist. Then explain one way a developer's instruction to a coding agent would change if the developer confused these terms.

**Points:** 5

**Rubric (1 point each):**

1. Defines a fragment as the candidate produced by rasterization for each screen position a triangle covers, carrying interpolated values (such as UV, colour and depth), and the unit on which the fragment (pixel) shader runs.
2. Distinguishes it from a pixel: a pixel is the final element of the output image, several fragments can compete for one pixel (overdraw), and a fragment only becomes the pixel's colour if it survives the depth and stencil tests and discard, and its colour is then combined with the framebuffer by blending.
3. Distinguishes it from a vertex: a vertex is a corner point with attributes (position, UV, colour) handled by the vertex shader, and fragment values are interpolated from the vertices.
4. Gives a consistent numeric example, for example four vertices but 4096 fragments for a quad covering 64 × 64 pixels, or 300 plus 100 fragments for overlapping triangles, showing that fragment count follows screen coverage while vertex count follows the mesh.
5. Connects the distinction to instructions: per-pixel colour effects (flash, tint, dissolve) are fragment-stage work, shape or position changes are vertex-stage work, and mixing them up sends the agent to edit the wrong stage.

**Source:** What a fragment is

## ES-ch06.2

A developer tells a coding agent: "Add a shader to the player so it looks hurt." The player is a multi-coloured 2D sprite with transparent areas around the artwork. Rewrite this instruction precisely, using the correct shader terms, so that the agent can build exactly one thing (choose one hurt effect, such as a red tint that fades out). Then explain at least three different wrong things the agent could have built from the vague version, and why each is wrong.

**Points:** 5

**Rubric (1 point each):**

1. The rewritten instruction names the shader kind (a 2D sprite shader, such as Godot's canvas_item shader, or the equivalent unlit 2D shader in another engine) and the stage (fragment), because the change is to colour, not to geometry.
2. It specifies the control: a float uniform from 0 to 1 and, for a tint, a target colour written in RGBA components from 0 to 1, with the output colour mixed toward the target by that amount (any other single, fully specified effect is accepted).
3. It states that alpha must be preserved so transparent texels stay transparent, and that at 0 the sprite looks exactly as before.
4. It says who drives the effect: game code sets a uniform at the moment of the hit, either a progress value that returns to 0 over a duration in seconds or a hit time that the shader compares with engine time, rather than relying on a bare global clock or a frame count.
5. It names at least three plausible wrong builds and why they fail, for example a vertex shader that wobbles the mesh, a colour multiplier that cannot reach the target colour, a permanent tint, opaque output that fills the transparent area with a box, or a shared material that tints every sprite.

**Source:** Say it to the agent: precise wording for an effect

## ES-ch06.3

For each of these four requests, decide whether the main work belongs in the vertex stage or the fragment stage, and justify the choice: (a) a flag waving on a mesh with many vertices, (b) an enemy dissolving into holes that follow a noise pattern, (c) a character squashing and stretching when it lands, (d) horizontal scanlines drawn over the whole screen. Explain what data flows from the vertex stage to the fragment stage, and why the cost of each stage differs for a large on-screen object.

**Points:** 5

**Rubric (1 point each):**

1. Waving flag: vertex stage, because it displaces vertex positions; it is only as detailed as the vertex count, so a coarse mesh would need subdividing or a fragment-stage distortion of the sampling coordinate instead.
2. Dissolve: fragment stage, because the keep-or-discard decision is made per pixel by comparing a noise sample with a threshold, which a per-vertex stage cannot do.
3. Squash and stretch: vertex stage (or an object transform), because it changes the shape of the geometry rather than the colour of pixels.
4. Scanlines: fragment stage using the pixel's screen-space position, because the pattern must vary per output pixel independent of the mesh's own UV.
5. Half a point for explaining the data flow: the vertex stage runs once per vertex and passes interpolated values (varyings such as UV) onward; half a point for the cost: the fragment stage runs once per covered pixel, so for a large object fragment work greatly outnumbers vertex work.

**Source:** Vertex shader versus fragment shader

## ES-ch06.4

A game needs four visuals: a chain-link fence, a ghost, a window pane in a building, and an enemy that dissolves away. Explain the difference between alpha blending and alpha testing (discard), and choose the better technique for each visual. Include how each technique behaves with draw order, what the edges look like, and one cost or limitation of each. Support the draw-order point with a small calculation or example.

**Points:** 5

**Rubric (1 point each):**

1. Defines alpha blending: the new fragment's colour is mixed with what is already in the framebuffer according to alpha (new × α + old × (1 − α)), allowing partial transparency.
2. Defines alpha testing or discard: a fragment is kept or dropped by comparing alpha (or a noise value) with a threshold, with no in-between opacity, so edges are hard and may look jagged.
3. Explains draw order: blending is order-dependent (a short calculation such as red over blue then green differing from green over blue then red), so translucent objects are normally sorted far to near, while alpha-tested fragments need no sorting.
4. Matches the visuals sensibly: fence (alpha test), ghost and window glass (blending, since they need partial transparency), dissolve (discard against a noise threshold, possibly with a blended soft edge).
5. States a cost or limitation of each: blending adds overdraw and sorting problems; discard has a performance cost on some GPUs because it can defeat depth optimisations.

**Source:** Alpha blending versus alpha test

## ES-ch06.5

A developer asks a coding agent for a "damage pulse": when a sprite takes a hit, a red tint should appear at full strength and fade to nothing over 0.4 seconds. The agent first writes a shader that uses the engine's global time value as its clock and then a version where a counter lowers a value by a fixed amount each rendered frame. Explain why both designs fail, and design a correct one. Cover what a uniform is, who sets it, how the duration stays the same at 30 and 144 frames per second, and what happens if several sprites (for example enemies) that share one material are hit at different times.

**Points:** 5

**Rubric (1 point each):**

1. Defines a uniform as a value set from outside the shader (game code), identical for all invocations of a draw, and says it is the contract through which game events reach the shader.
2. Explains why global engine time fails for an event-triggered effect: it counts from engine start, not from the hit, so the effect would play once at startup or at an arbitrary phase.
3. Explains why a per-frame decrement fails: the duration is a number of frames, so it lasts longer at 30 fps than at 144 fps (for example 12 frames is 0.4 s at 30 fps but about 0.083 s at 144 fps).
4. Gives a correct design: game code measures elapsed seconds since the hit (or stores the hit time), computes a progress value from 0 to 1, and sets a uniform that the shader uses to mix the tint, ending at exactly 0.
5. Addresses sharing: a uniform set on a material shared by several objects changes all of them, so a per-object copy of the material or a per-instance parameter is needed to pulse only the hit object.

**Source:** Uniforms, time and frame-rate independence

## ES-ch06.6

Trace one textured mesh through the rendering pipeline from the moment game code decides to draw it until a pixel changes colour on screen. Name the stages in order and say for each whether it runs on the CPU or GPU and whether developers program it or configure it. Explain where a fragment can still be rejected after the fragment shader has run, and what that means for performance.

**Points:** 5

**Rubric (1 point each):**

1. The CPU side prepares the work: the game submits the mesh's vertex data, textures, uniform values and a draw command (draw call) to the GPU.
2. The vertex shader runs per vertex on the GPU, is programmable, and outputs a position (clip space) and values to pass on, such as UV.
3. Mapping to the screen and rasterization are fixed-function: they decide which pixel positions each triangle covers and produce a fragment for each, with interpolated values.
4. The fragment shader runs per fragment, is programmable, samples textures and outputs a colour and alpha, and may discard.
5. Depth and stencil tests and blending are configurable fixed-function steps that decide whether and how the output is written to the framebuffer, so a fragment can run the shader and still be rejected, which is wasted work (overdraw).

**Source:** Render pipeline overview

## ES-ch06.7

A developer tells a coding agent: "Make the character sprite look metallic and shiny." The game is 2D. Explain the difference between a 2D canvas shader and a 3D spatial shader in terms of what each one writes and who computes the final lighting, say what goes wrong with the instruction as worded, and rewrite it so the agent builds a convincing 2D result.

**Points:** 5

**Rubric (1 point each):**

1. A 2D canvas shader works in 2D coordinates, and its fragment stage writes the final output colour of each pixel (typically starting from vertex colour times texture colour), as used for sprites, UI and tiles.
2. A 3D spatial shader works on meshes with 3D transforms, and its fragment stage sets material properties (albedo, roughness, metallic, emission, alpha) that the engine's lighting model turns into the final colour.
3. Explains the consequence: physically based terms such as roughness and metallic have no meaning in a 2D canvas shader, so "metallic" is ambiguous and an agent may try a 3D material on a sprite or invent parameters that do nothing.
4. Offers a feasible 2D approach, for example a moving highlight band computed from UV and time and masked by the sprite's alpha, a lit sprite using a normal map and 2D lights, or a colour ramp, and states that these fake the look.
5. Gives a rewritten instruction that names the shader kind and stage, the inputs (UV, time or a uniform), the mask (preserve alpha), and the intended look (for example a diagonal highlight sweeping every two seconds).

**Source:** 2D canvas shader versus 3D spatial shader

## ES-ch06.8

A developer asks a coding agent for "flowing water" on a flat 2D tile that uses a 128 × 128 texture. Explain what UV coordinates are, what texture sampling does, and how a scrolling effect is made in a fragment shader. Specify the instruction you would give the agent so that it sets the sampler's repeat and filtering correctly, and describe two visible faults that appear if those settings are wrong.

**Points:** 5

**Rubric (1 point each):**

1. Defines UV as 2D coordinates that map points on a surface to positions in a texture (normally 0 to 1), and texture sampling as reading the texture's colour at a UV, where one pixel of the texture is a texel.
2. Explains scrolling: add an offset proportional to time to the UV before sampling, with a speed in UV units per second (for example 0.25 per second repeats the pattern every 4 seconds).
3. Says the texture must be seamless and the wrap mode must be repeat, otherwise the offset UVs run past 0 to 1 and the edge texels are smeared (clamp) or a visible seam appears.
4. Chooses filtering deliberately: linear filtering for smooth water, nearest for crisp pixel art, and notes that sampling between texels with the wrong filter gives blur or shimmer.
5. Gives a precise instruction naming the stage (fragment), the clock (engine time is fine here because the flow is continuous), the speed uniform, the repeat and filter settings, and the seamless-texture requirement.

**Source:** UV and texture sampling
