# Chapter 6: Shader foundations

## MA-ch06.1

A renderer draws two opaque triangles. Triangle 1 covers 300 screen pixels. Triangle 2, drawn later and nearer to the camera, covers 100 pixels, all of which are also covered by triangle 1. Rasterization is the step that turns each triangle into fragments. Assume every fragment runs the fragment shader (no early rejection). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Rasterizing triangle 1 produces 300 fragments, each carrying interpolated values such as texture coordinates and depth.
- [ ] B. A fragment is a vertex that the vertex shader has already moved to its final screen position, ready to be coloured.
- [ ] C. The 100 pixels covered by both triangles each receive two fragments, but only the nearer one decides the pixel's colour.
- [ ] D. A fragment is a finished pixel colour that has already passed the depth test and will appear in the final image.
- [ ] E. The fragment shader runs 400 times in total for these two triangles, 300 for the first and 100 for the second.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Rasterization generates one fragment per covered screen position and fills in its values by interpolating the vertex outputs.
- B: A vertex is a corner point of a triangle; a fragment is produced for every covered screen position inside it, and there are usually far more fragments than vertices.
- C: Both triangles produce a fragment for the overlapped pixels, and with opaque surfaces the depth test lets the nearer one win; the other is wasted work (overdraw).
- D: A fragment is only a candidate: depth test, discard or blending can reject or combine it before it becomes the pixel's final colour.
- E: The shader runs once per fragment, and triangle 1 yields 300 fragments while triangle 2 yields 100, so 400 runs under the stated assumption.

**Source:** What a fragment is

## MA-ch06.2

A 2D sprite is drawn on a quad made of two triangles with four corner vertices. The quad covers exactly 64 × 64 = 4096 screen pixels. Three quarters of the sprite's texels have alpha 0 (fully transparent). Assume no multisampling and that every covered fragment runs the fragment shader. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The fragment shader runs only for the 1024 pixels whose alpha is above zero, because the others are invisible.
- [ ] B. The vertex shader runs for the four corners of the quad, not for each of the 4096 covered pixels.
- [ ] C. The GPU skips fully transparent fragments, so the cost of drawing the sprite equals the cost of its visible part only.
- [ ] D. Tinting only the visible artwork, and not the empty texels, is a vertex-shader job because it sees the whole sprite.
- [ ] E. If the sprite is drawn three times larger (192 × 192 pixels), it still has four vertices but 36,864 fragments.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Transparency does not stop a fragment from being generated; the quad covers 4096 pixels, and all 4096 run the shader, with 3072 of them simply producing alpha 0.
- B: The vertex stage runs per vertex, and a quad has four.
- C: A transparent texel still costs a shader run and, if blending is on, a blend operation; the quad's whole area is paid for.
- D: The vertex shader sees four corner points and can only hand interpolated values to the fragment stage; telling artwork from empty texels needs the texture, which is sampled per fragment.
- E: 192 × 192 = 36,864 covered pixels, while the vertex count is a property of the mesh and stays at four.

**Source:** Fragment versus vertex counts

## MA-ch06.3

Two programmable stages of the graphics pipeline are the vertex shader and the fragment shader. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The fragment shader runs once per vertex of the mesh and outputs each vertex's final position on the screen.
- [ ] B. The vertex shader runs once per vertex and normally outputs where that vertex lands, plus data for the fragment stage.
- [ ] C. A fragment shader can move one corner of a triangle, which is how a flat mesh is made to bend.
- [ ] D. For a mesh that covers much of the screen, the fragment shader runs far more often than the vertex shader, because it runs per covered pixel position and not per corner point.
- [ ] E. Sampling a texture to choose each covered pixel's colour belongs in the fragment shader.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The fragment shader runs per fragment and outputs a colour; positions are the vertex shader's output.
- B: The vertex stage processes each vertex once and typically outputs a clip-space position together with values such as UV or colour that are passed on.
- C: By the time fragments exist, the triangle's corners have already been placed; bending geometry is done by changing vertices in the vertex stage.
- D: The vertex stage runs once per vertex of the mesh, while the fragment stage runs once per rasterized fragment, and a large on-screen mesh covers many more pixel positions than it has vertices.
- E: Per-pixel decisions, such as reading a texture at an interpolated UV, are made in the fragment stage.

**Source:** Vertex shader versus fragment shader

## MA-ch06.4

In shader vocabulary, a uniform is a value supplied from outside the shader that is identical for every invocation in one draw, and a varying (also called an interpolant) is a value the vertex stage outputs and the fragment stage receives interpolated across the triangle. A developer needs (1) one enemy's health ratio, set by game code, to control a health-bar fill, and (2) a gradient that goes smoothly from 0 at the left edge of a quad to 1 at the right edge. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The health ratio is a natural uniform: it comes from game code and is the same for all fragments of that draw.
- [ ] B. The left-to-right gradient is a natural varying: corner values 0 and 1 are interpolated for each fragment.
- [ ] C. A fragment shader can assign a new value to a uniform so that later fragments of the same draw see it.
- [ ] D. A varying has a single value per triangle, copied unchanged across the triangle's fragments, so it cannot produce a gradient.
- [ ] E. Changing a uniform's value from game code forces the shader to be recompiled before the next frame.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A uniform is the channel through which game code hands a per-draw value to the shader, and every fragment sees the same value.
- B: Interpolating the corner values across the triangle gives each fragment its own position along the gradient.
- C: Uniforms are read-only inside the shader; invocations run independently and cannot pass results to each other that way.
- D: The defining property of a varying is the opposite: it is interpolated, so it differs from fragment to fragment.
- E: Uniform values are simply uploaded as data; the compiled program does not change when a value does.

**Source:** Uniform versus varying

## MA-ch06.5

A game scrolls the camera across a 4000 × 1080 pixel background sprite on a 1920 × 1080 screen. A developer asks a coding agent for a vignette, meaning darkening toward the edges of what the player sees, applied by a fragment shader on the background sprite. The agent can compute the darkness from the sprite's UV coordinates or from the pixel's screen coordinates. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A vignette computed from the background sprite's UV stays locked to the edges of the display as the camera scrolls.
- [ ] B. UV coordinates describe a position on the sprite's own surface, running from 0 to 1 across the 4000-pixel-wide image.
- [ ] C. Because the background scrolls, screen coordinates scroll with it: the display pixel in the top-left corner has a different screen coordinate each frame.
- [ ] D. A vignette meant to hug the edges of what the player sees should use the pixel's screen position (SCREEN_UV in Godot).
- [ ] E. Screen space is the 3D coordinate system of the whole scene, with the camera at the origin and units in metres.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: UV is attached to the image, so a UV-based vignette darkens the image's own far edges and slides along with the scroll.
- B: UV is a coordinate on the textured surface, normalised to the range 0 to 1 over that surface.
- C: A screen coordinate names a fixed place in the output image, so the top-left display pixel is always at the same coordinate; what changes is which part of the background is drawn there.
- D: Screen-space coordinates are tied to the display, so the darkening stays at the display edges however the camera moves.
- E: That describes view space; screen space is the 2D coordinate system of the output image.

**Source:** UV versus screen space

## MA-ch06.6

Blending combines a new fragment's colour with the colour already in the framebuffer using result = new × α + old × (1 − α). The background pixel is blue, (0, 0, 1). Two translucent layers cover it, each with α = 0.5: a red layer, (1, 0, 0), and a green layer, (0, 1, 0). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If red is drawn first and green second, the pixel ends at (0.25, 0.5, 0.25).
- [ ] B. If green is drawn first and red second, the pixel ends at the same (0.25, 0.5, 0.25).
- [ ] C. Alpha testing produces smooth, partially transparent fades along the edge of a cut-out.
- [ ] D. Alpha testing (keep or discard each fragment by a threshold) avoids the order dependence but has only all-or-nothing transparency.
- [ ] E. A window pane that should show the scene dimly through it is better made with alpha testing than with blending.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Red over blue gives (0.5, 0, 0.5); green over that gives (0.25, 0.5, 0.25).
- B: Green over blue gives (0, 0.5, 0.5); red over that gives (0.5, 0.25, 0.25), so blending depends on draw order.
- C: A tested fragment is either kept at full strength or dropped, so edges are hard and may look jagged.
- D: Because each fragment is kept or discarded outright, nothing is blended, and the result does not depend on the order of drawing, but there are no in-between opacities.
- E: Dim see-through glass needs partial opacity, which only blending provides.

**Source:** Alpha blending versus alpha test

## MA-ch06.7

Godot has a 2D shader type (shader_type canvas_item) and a 3D shader type (shader_type spatial). Check each statement that is true about Godot. Each statement is worth 1 point (5 points total).

- [ ] A. In a canvas_item fragment function, the shader writes the pixel's final colour directly, starting from the sprite's own texture colour.
- [ ] B. Setting ROUGHNESS in a canvas_item fragment function gives the sprite a glossy PBR look that responds to 2D lights.
- [ ] C. A spatial fragment function sets material properties (ALBEDO, ROUGHNESS, METALLIC), and the engine's lighting makes the final colour.
- [ ] D. Both shader types can define a vertex() function that runs once per vertex.
- [ ] E. The shader type is chosen for the look wanted rather than for what is being drawn, so a spatial shader can be assigned to a 2D sprite to give it 3D-style shading.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A 2D fragment function decides the drawn colour itself; its colour variable begins as the texture colour (times the vertex colour) and whatever it holds at the end is what is drawn.
- B: There is no ROUGHNESS in a canvas_item shader, and 2D drawing has no PBR lighting model for it to feed.
- C: A spatial shader describes the surface and lets the built-in renderer do the shading.
- D: vertex(), fragment() and light() exist for both spatial and canvas_item shaders.
- E: The shader type follows the kind of object drawn: Godot's documentation describes canvas_item shaders as drawing 2D elements and spatial shaders as shading 3D objects.

**Source:** 2D canvas shader versus 3D spatial shader

## MA-ch06.8

In a shader a colour is four floats (red, green, blue, alpha), normally written in the range 0.0 to 1.0, where alpha 0.0 is fully transparent. A pixel has the colour (0.2, 0.4, 0.6, 1.0). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Multiplying the red, green and blue channels by white, (1, 1, 1), turns the pixel white because white is the brightest colour.
- [ ] B. Mixing 25 percent of the way toward white, mix(colour, white, 0.25), gives (0.4, 0.55, 0.7) in red, green and blue.
- [ ] C. Multiplying red, green and blue by (1.0, 0.5, 0.5) gives (0.2, 0.2, 0.3): red unchanged, green and blue halved.
- [ ] D. In an 8-bit image 255 corresponds to 1.0, so the 8-bit colour (255, 128, 0) corresponds to roughly (1.0, 0.50, 0.0).
- [ ] E. Writing the 8-bit numbers (255, 128, 0) into float channels would clamp to yellow (1, 1, 0) on an ordinary 8-bit target, not orange.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Multiplying by 1 leaves each channel unchanged, so multiplying by white changes nothing; a flash toward white needs mixing or adding.
- B: mix gives old × 0.75 + 1 × 0.25 per channel: 0.15 + 0.25, 0.30 + 0.25 and 0.45 + 0.25.
- C: 0.2 × 1.0, 0.4 × 0.5 and 0.6 × 0.5.
- D: 128 / 255 is about 0.50, so the 8-bit triple maps to the float triple above.
- E: 255 and 128 are both far above 1.0 and clamp to full intensity, giving yellow instead of orange.

**Source:** Colour as RGBA in 0 to 1

## MA-ch06.9

A developer wants an enemy sprite to flash entirely white for a few frames when it is hit. The sprite is a multi-coloured texture on a quad. The developer is deciding how to word the request to a coding agent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Setting the sprite's colour multiplier (modulate in Godot) to white pushes the colours of the artwork up to white for the flash.
- [ ] B. In the fragment shader, mix the output colour toward white by a 0-to-1 uniform called flash_amount, keeping alpha unchanged; the script drives it.
- [ ] C. "Change the vertex positions" would send the agent to the vertex stage, which moves corners and cannot recolour the artwork.
- [ ] D. If the instruction omits alpha, an agent may output opaque white for each fragment, turning transparent surroundings into a white rectangle.
- [ ] E. A shader cannot do this, so the agent has to swap in an all-white copy of the texture for a few frames, then swap back.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A multiplier of white is 1 in every channel, which leaves the colours unchanged.
- B: It names the stage (fragment), the operation (mix toward white), the control (a uniform from 0 to 1), the constraint (alpha untouched) and who drives it (the script).
- C: The vertex stage positions geometry; recolouring every pixel is a fragment-stage job.
- D: The quad covers many fully transparent texels; overwriting their alpha makes the box visible.
- E: A fragment shader can mix any output colour toward white with no extra texture.

**Source:** Say it to the agent: hit flash

## MA-ch06.10

A flag is drawn as a flat quad with only 4 vertices (two triangles). A developer asks a coding agent: "Make the flag ripple in the wind with a shader." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A vertex-shader displacement with a sine of time can only move the four corners, so it needs a subdivided mesh to look like a ripple.
- [ ] B. A fragment-shader approach can ripple the picture on the same quad by offsetting the sampling coordinate by a sine of position and time.
- [ ] C. The vertex approach changes the flag's outline; the UV-offset approach keeps the rectangle and shifts only the picture inside it.
- [ ] D. In the UV-offset approach the fragment shader moves the quad's vertices to their new places, which is what makes the picture ripple.
- [ ] E. A continuous ripple can use the engine's global time (TIME in Godot), because it does not have to start at a particular event.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Vertex displacement can only be as detailed as the vertex count; four corner points give a tilt or shear, not a wave.
- B: Distorting the sampling coordinate per fragment shifts which texel each pixel shows, giving a ripple without extra geometry.
- C: Moved vertices change the shape that gets rasterized; sampling changes leave the covered area unchanged.
- D: Fragment shaders never move vertices; they decide the colour of fragments the quad already produces.
- E: A looping effect with no start moment can read global time directly; only event-triggered effects need a value from game code.

**Source:** Say it to the agent: vertex versus fragment for a ripple

## MA-ch06.11

A developer asks a coding agent: "When the player is hit, run a 0.4 second flash starting at the moment of the hit." The agent writes, in a Godot shader, flash = 1.0 - clamp(TIME / 0.4, 0.0, 1.0), where TIME is the engine's global time in seconds since the engine started. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. TIME restarts from zero at each hit, so the flash plays correctly on repeated hits without any extra code.
- [ ] B. The flash plays once right after the engine starts, then the expression stays at 0, so later hits show nothing.
- [ ] C. A fix is a uniform set by game code, such as the time of the last hit or a progress value animated from 0 to 1.
- [ ] D. The shader can detect by itself that a hit happened in game logic, because it runs each time a frame is drawn.
- [ ] E. Saying "driven by a uniform that game code sets at the hit" tells the agent where the event knowledge lives.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: TIME counts from engine start and is not reset by game events.
- B: After 0.4 seconds of engine time the clamp saturates at 1.0, so flash stays at 0 forever.
- C: Game code knows when the hit occurred, and a uniform is how it passes that to the shader.
- D: A shader only sees its inputs; game events reach it only through uniforms, textures or vertex data.
- E: Naming the uniform and who sets it prevents the agent from guessing that the shader can know about events.

**Source:** Say it to the agent: time as a uniform

## MA-ch06.12

A developer asks a coding agent for a one-pixel white outline around the opaque shapes of a sprite. The sprite texture is 64 × 64 texels and is drawn on a quad. Each fragment-shader invocation runs independently. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A fragment cannot read the final colour that a neighbouring fragment computed in the same draw.
- [ ] B. The outline can be made by a vertex shader that moves each pixel of the sprite one step outward and recolours it.
- [ ] C. One texel is 1/64 in UV units here, so the outline can sample the sprite's alpha at offsets of ±1/64 in u and v.
- [ ] D. A fragment that is transparent but has an opaque neighbouring sample can be coloured white to form the outline.
- [ ] E. If the artwork touches the quad's edge, outline pixels outside the quad cannot be drawn, because no fragments exist there.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Invocations are independent, so effects that need neighbours sample an already-available texture, not another fragment's output.
- B: The vertex stage handles vertices, not pixels; it cannot move individual pixels.
- C: UV runs 0 to 1 over 64 texels, so one texel is 1/64.
- D: Checking the sprite's own alpha at neighbouring offsets is the standard way to find pixels just outside a shape.
- E: Fragments exist only where the geometry covers the screen, so the quad needs padding around the artwork.

**Source:** Say it to the agent: neighbour sampling

## MA-ch06.13

A developer asks a coding agent for a dissolve effect: an enemy sprite breaks into holes that follow a noise pattern as a uniform called dissolve goes from 0 to 1, until the sprite is gone. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Discarding fragments gives smooth, partially transparent hole edges, because discarded pixels fade out gradually.
- [ ] B. Discarding a fragment has no performance cost, since the fragment is thrown away before it is drawn.
- [ ] C. Comparing a noise sample with the dissolve uniform and discarding fragments below it gives sharp-edged holes that follow the noise.
- [ ] D. A smooth alpha fade near the threshold is independent of draw order, because the fade is computed in the shader.
- [ ] E. A discarded fragment writes nothing, so the pixel keeps what was already drawn at that position.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A discarded fragment is dropped entirely, so edges are hard; smooth edges need partial alpha and blending.
- B: Godot's documentation warns that discard has a performance cost because it prevents the depth prepass from being effective.
- C: This is the usual noise-threshold dissolve: the decision is per fragment.
- D: Partial alpha is blended with what is behind it, and blending depends on the order of drawing.
- E: Discard means nothing is written for that fragment.

**Source:** Say it to the agent: dissolve with discard

## MA-ch06.14

A developer wants requests to a coding agent to land in the right shader stage. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Turn the whole level black-and-white when the player dies" is a fragment-stage job, since it recolours each pixel.
- [ ] B. "Squash and stretch the character's mesh when it lands" is a fragment-stage job, since it changes how the character looks.
- [ ] C. "Draw horizontal scanlines over the screen" is a vertex-stage job, because lines are geometry.
- [ ] D. "Swap the character's palette" is a vertex-stage job, because the palette belongs to the whole object.
- [ ] E. "Make the grass blades sway at their tips" is a vertex-stage job when each blade is a mesh with vertices that can be displaced.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Desaturating means changing the final colour of every pixel, which is what the fragment stage decides.
- B: Squash and stretch changes the shape of the geometry, which is done by moving vertices (or transforming the object).
- C: Scanlines are a pattern in screen position computed per pixel, not extra geometry.
- D: A palette swap changes the colour looked up per pixel, so it belongs to the fragment stage.
- E: Swaying tips are a displacement of vertex positions, weighted toward the tips.

**Source:** Say it to the agent: choosing the stage

## MA-ch06.15

A developer tells a coding agent: "Use a shader to shrink the boss to half size so the player can slip under its attacks." The boss has a collision shape that is separate from its sprite. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Physics queries read the pixels the shader outputs to decide what overlaps, so a shrunken image shrinks the hit area.
- [ ] B. Vertex positions changed in a shader are written back to the node's transform, so the physics body moves too.
- [ ] C. If the shader discards the lower half of the sprite's fragments, the collision shape shrinks to match what remains.
- [ ] D. A shader changes how the boss is drawn, but not the size or position of its collision shape.
- [ ] E. For the player to slip under, the instruction must say to change the collision shape (or body scale) in game code.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Collision is computed from shapes, not from rendered pixels.
- B: Shader output stays on the GPU as image data and never updates game-side transforms.
- C: Discarding fragments only changes what is displayed; the collision shape is untouched.
- D: Rendering and physics are separate systems, and a shader belongs only to the first.
- E: Gameplay consequences live in game code, so the instruction must name the collision change explicitly.

**Source:** Say it to the agent: shaders do not change gameplay

## MA-ch06.16

An interviewer asks a candidate to explain why shaders run on the GPU and what they cannot do. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A GPU runs the same small program over many vertices or fragments at once, which suits colouring millions of pixels.
- [ ] B. Data a shader needs, such as the player's position, arrives through uniforms or textures set from the CPU side.
- [ ] C. A shader can print a debug line and read a variable of a game script directly, as long as the variable is a number.
- [ ] D. A frame can be CPU-bound or GPU-bound: limited by game logic and draw preparation, or by shading work, whichever is slower.
- [ ] E. Moving a calculation from a script into a fragment shader makes the game faster, because the GPU is faster than the CPU.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Parallel execution of one small program over many independent items is what GPUs are built for.
- B: Shaders have no access to game objects; the CPU passes values in.
- C: A shader has no print function and no access to script variables; the only output is the colour or position it writes.
- D: Both processors work on each frame, and the slower one sets the frame time.
- E: A fragment shader runs per covered pixel, so a calculation that was cheap once per object can become expensive millions of times per frame.

**Source:** GPU versus CPU work

## MA-ch06.17

A simplified view of how a 3D mesh becomes pixels is this chain: vertex data, vertex shader, mapping to the screen, rasterization, fragment shader, depth and stencil tests plus blending, framebuffer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Rasterization is a programmable stage that developers write in the shader language, like the vertex and fragment stages.
- [ ] B. The fragment shader runs before rasterization to decide which pixels a triangle covers, and rasterization then fills them in.
- [ ] C. Blending happens before the fragment shader, because it must know which colours are already in the framebuffer.
- [ ] D. Rasterization turns each triangle into fragments for the covered pixel positions, with the vertex outputs interpolated.
- [ ] E. The vertex shader's output is already in screen pixels, so no conversion is needed before rasterization.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: In the standard pipeline, rasterization is fixed-function hardware that developers configure but do not program.
- B: The fragment shader only runs on fragments that rasterization has already produced.
- C: Blending uses the fragment shader's output colour, so it comes after the shader, using what is already stored.
- D: Producing covered positions and interpolating the vertex outputs for them is exactly what rasterization does.
- E: The vertex shader typically outputs clip-space positions, which the pipeline converts to screen positions before rasterization.

**Source:** Render pipeline overview

## MA-ch06.18

A mobile game draws a 1920 × 1080 screen (2,073,600 pixels). A full-screen translucent fog sprite is drawn, then a second full-screen translucent glow sprite on top, then the UI. Each full-screen layer runs the fragment shader for every pixel it covers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The two full-screen layers together cost 4,147,200 fragment-shader runs per frame, before the UI.
- [ ] B. Making the fog layer's shader simpler reduces its cost even though the number of covered pixels stays the same.
- [ ] C. Because the glow sprite is mostly transparent, the GPU skips low-alpha fragments, so its cost follows the visible glow.
- [ ] D. Rendering the fog layer at half the width and half the height cuts its fragment count to a quarter, 518,400.
- [ ] E. Overdraw means the same screen pixel is shaded by more than one fragment in a frame; here each pixel has at least two.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: 2 × 2,073,600 = 4,147,200.
- B: Per-fragment cost is the shader's work times the fragment count, so either factor can be reduced.
- C: Low alpha does not stop the shader from running; the full area is shaded and blended.
- D: Halving both dimensions leaves 960 × 540 = 518,400 pixels, a quarter of 2,073,600.
- E: Each pixel receives a fog fragment and a glow fragment, which is overdraw.

**Source:** Fragment cost and overdraw

## MA-ch06.19

A fragment shader reads a texture with texture(tex, uv). The texture is a 16 × 16 pixel-art icon drawn on a quad that covers 128 × 128 screen pixels. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Enlarging the icon eight times with linear filtering still leaves the texels as crisp blocks, because filtering matters when a texture is shrunk, not when it is enlarged.
- [ ] B. UV coordinates count texels, so the centre of the 16 × 16 icon is at uv (8, 8).
- [ ] C. A uv of (1.25, 0.5) lies outside the texture, so the lookup has no colour to return and the pixel is left undrawn.
- [ ] D. Nearest filtering is the better choice for a smooth water texture, because it returns the single most accurate texel instead of a blur.
- [ ] E. If the icon fills the quad and is sampled with nearest filtering, each texel (one pixel of the texture image) appears as a flat 8 × 8 block of screen pixels, since 128 / 16 = 8.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Linear filtering blends neighbouring texels whenever a lookup falls between texel centres, which is what happens when a small texture is enlarged, so the blocks blur; nearest filtering keeps them crisp.
- B: UV is normalised to 0 to 1 across the whole texture, so the centre is (0.5, 0.5) regardless of the texture's size in texels.
- C: Sampling outside 0 to 1 is legal: the sampler's wrap mode (such as repeat or clamp) decides which texel comes back, so a colour is still returned.
- D: Nearest filtering gives blocky results that suit pixel art; a smooth texture such as water looks better with linear filtering, which blends neighbouring texels.
- E: 128 / 16 = 8 screen pixels per texel along each axis, and nearest filtering returns a single texel's colour for all of them.

**Source:** Texture sampling

## MA-ch06.20

A hit flash fades from 1.0 to 0.0. Version A, driven by game code, lowers it by 1/12 on every rendered frame. Version B sets it to 1.0 − elapsed_seconds / 0.4, where elapsed_seconds is accumulated from the time each frame took. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Version A lasts 0.4 seconds at 30 frames per second and 0.2 seconds at 60 frames per second.
- [ ] B. At 144 frames per second Version A lasts about 0.083 seconds.
- [ ] C. Version A lasts the same wall-clock time at 30 and 144 frames per second, because the shader runs once per frame.
- [ ] D. Version B lasts noticeably longer at 30 frames per second than at 144.
- [ ] E. Version B is frame-rate independent because it measures elapsed seconds instead of counting frames.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Twelve frames last 12/30 = 0.4 s at 30 fps and 12/60 = 0.2 s at 60 fps.
- B: 12/144 is about 0.083 s.
- C: A frame-counted fade lasts a number of frames, so its duration changes with the frame rate.
- D: Version B ends when 0.4 s have elapsed, which does not depend on how many frames are drawn.
- E: Using accumulated time makes the duration a fixed number of seconds.

**Source:** Frame-rate independence of time-driven effects
