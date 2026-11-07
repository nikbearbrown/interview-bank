# Chapter 8: Shader verification

## MA-ch08.1

A developer asks a coding agent to change a shader that tints a character. The agent replies: "Done. The shader compiles with no errors and the existing automated tests pass." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A clean compile shows that the shader's output matches the intended look, because the compiler checks the formulas against the design document.
- [ ] B. A compile error means the shader source was rejected by the compiler, whereas a visual bug means it built and ran but drew a wrong result.
- [ ] C. A shader that multiplies a colour by the wrong factor still compiles, so a compile check cannot tell it from a correct one.
- [ ] D. If the existing tests passed both before and after the change, the change cannot have altered how anything is drawn, since a test suite covers the whole game.
- [ ] E. The agent's reply is a claim; the compile log and passing tests are evidence only for narrow things such as valid syntax and unchanged game logic.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The compiler checks syntax and types; it has no knowledge of the intended look.
- B: Rejection by the compiler is a compile error; a shader that builds but draws wrongly is a visual bug.
- C: A wrong factor is still valid code, so the compiler accepts it and nothing in the compile output differs.
- D: Tests that never inspect rendered pixels cannot see a change in drawing, so they pass whether or not the picture changed.
- E: A compile log and a test suite each cover a narrow property, so the reply asserts more than the evidence shows.

**Source:** Compile error versus visual bug

## MA-ch08.2

A continuous-integration machine has no graphics card. It runs the game engine in headless mode, where (as with Godot's `--headless` option) the display driver is a dummy and no pixels are drawn. A second option on the same machine is a software renderer, which executes the rasterization on the CPU and does produce an image. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A headless run that reports no errors proves that the shader's output colours are correct, since a shader with wrong colours would raise an error.
- [ ] B. A headless run can check game logic that feeds a shader, such as which value a script writes to a shader parameter each frame.
- [ ] C. A frame time measured on the software renderer predicts the frame time on players' graphics cards, since both execute the same shader code.
- [ ] D. With a dummy display driver the shader still executes, on the CPU, so a headless timing of a heavy fragment shader reflects its GPU cost.
- [ ] E. An image from a software renderer can check colours, but it may differ from a real GPU's image in precision, filtering or driver behaviour.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A dummy driver draws nothing, so "no errors" says nothing about what the shader outputs, and wrong colours raise no error.
- B: Script-to-parameter logic runs on the CPU and does not need a display, so a headless test can observe it.
- C: The software renderer runs on a CPU with a different execution model, so its speed does not transfer to a GPU.
- D: With a dummy driver no fragments are shaded at all, so fragment work is absent from the measurement.
- E: A software renderer is a different implementation of the same pipeline, so small output differences from real hardware are expected.

**Source:** What headless and software rendering can show

## MA-ch08.3

A team verifies a shader change with a golden-image test. A fixed test scene is rendered at 1280 × 720 (921,600 pixels), captured, and compared with an approved reference image. A pixel counts as different when any channel differs by more than 2 (out of 255). The test fails if more than 0.5 percent of the pixels are different, which is 4,608 pixels. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A wrong-coloured block of 60 × 60 pixels (3,600 pixels) on an otherwise identical capture passes this test, even though it is a real defect.
- [ ] B. Tightening the rule to 0.25 percent (2,304 pixels) would make the same 60 × 60 block fail.
- [ ] C. If the reference image was captured from a buggy build and approved without anyone looking at it, the test will still report that bug when it runs.
- [ ] D. A pass on a scene that does not draw the part of the shader that changed shows that the change is correct, because nothing differed from the reference.
- [ ] E. The per-channel tolerance of 2 keeps tiny rounding or driver differences from failing the test, and it also makes the test blind to very small real colour shifts.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: 3,600 pixels is below the 4,608-pixel limit, so a visible defect can hide under a percentage threshold.
- B: 0.25 percent of 921,600 is 2,304, and 3,600 exceeds it, so the block would now fail.
- C: A reference that contains the bug makes the buggy output match it, so the test passes and the bug is baked in.
- D: A scene that does not exercise the changed code gives identical output before and after, which proves nothing about that code.
- E: A tolerance trades false failures against sensitivity; a shift smaller than the tolerance cannot be seen.

**Source:** Screenshot and golden-image comparison

## MA-ch08.4

An agent has rewritten a shader that tints a sprite when the character is damaged and reports: "Verified, it works." The developer wants evidence, not a claim. Check each request that is a sound way to get it. Each statement is worth 1 point (5 points total).

- [ ] A. "Confirm once more that you are sure it works, and explain in detail why you believe the tint is correct."
- [ ] B. "Say which of your statements you observed in a run and which you inferred from reading the code."
- [ ] C. "Add a comment at the top of the shader recording that it was verified, with today's date and your name."
- [ ] D. "Render a fixed test scene at tint amounts 0, 0.5 and 1, capture it, and report pixel values at known points beside the values the specification predicts."
- [ ] E. "Run the compile check again and paste the output line that reports no errors, so that we have it in the log."

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Repeating and explaining a belief is still a claim, and an explanation from reading code is not an observation.
- B: Separating observed from inferred shows which statements rest on evidence and which only on reasoning.
- C: A comment records an assertion and cannot confirm anything about the output.
- D: Controlled inputs with measured outputs placed beside predicted values are an observation that can contradict the claim.
- E: Rerunning the same compile check can only repeat the same result, so it adds no new information.

**Source:** Evidence versus a claim of success

## MA-ch08.5

Shader code works with positions and directions in several coordinate spaces. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Local (object or model) space measures positions from the object's own origin and axes, so a vertex keeps the same local position when the object moves or rotates.
- [ ] B. World space is shared by all objects in the scene; moving a position from local to world space applies the object's transform.
- [ ] C. Screen space is the same thing as texture coordinates (UV): both run from 0 to 1 across the mesh, so a screen position can be read directly as a UV.
- [ ] D. View (camera or eye) space measures positions relative to the camera, which sits at the origin.
- [ ] E. If the camera has only been moved and not rotated, a point's view-space position still differs from its world-space position.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Local coordinates are stored with the mesh and do not change when the object's transform changes.
- B: The model transform is exactly the step that carries local positions into the shared world.
- C: UV coordinates are per-vertex texture coordinates, whereas screen space says where a fragment lands on the display, usually in pixels.
- D: View space is defined relative to the camera, which is why it changes whenever the camera moves.
- E: Moving the camera shifts every point's view-space position by the camera's offset, so the two spaces do not coincide.

**Source:** Coordinate spaces: local, world, view, screen

## MA-ch08.6

A coding agent writes a fragment shader for a flood line: everything below a height of 0.5 in the world should be drawn darker, as if water stood at that level. The agent takes each fragment's height from the vertex position exactly as the mesh stores it and compares it with 0.5, with no transformation. The prop is a crate 2 units tall whose origin is at its centre, so its stored heights run from −1 to +1. The crate stands on a platform so that its centre is at world height 10. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The crate is not darkened at all, because it stands at world height 10, far above the flood line of 0.5, and the shader is meant to affect only low objects.
- [ ] B. The stored vertex position is in local space, so the shader compares height measured from the crate's own centre with 0.5, not height in the level.
- [ ] C. Moving this one crate to world height 0 would make the effect correct for the props across the level, because the flood line is then at the right height.
- [ ] D. Converting the position to view space instead would give a fixed flood line, because view space does not depend on where the camera is.
- [ ] E. If the crate is turned upside down, the darkened band ends up at its top in the world, because the stored heights turn with the object.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The shader never leaves local space, so the lower three quarters of the crate (stored heights −1 to 0.5) are darkened wherever it stands.
- B: Mesh-supplied positions are local, and comparing them with a world-space value mixes two spaces.
- C: That would hide the bug for one crate only; props at other heights, rotated or scaled, would still be wrong.
- D: View space is measured from the camera, so the flood line would move every time the camera moved.
- E: Stored heights rotate with the object, so the region where they are below 0.5 turns upside down with it.

**Source:** Mixing coordinate spaces

## MA-ch08.7

A surface runs along the direction t = (1, 1, 0) and has the normal n = (1, −1, 0), so t · n = 0 and the two are perpendicular. The object is then scaled non-uniformly by (1, 4, 1), making it four times taller. A vertex shader carries the surface direction through the model matrix and gets t′ = (1, 4, 0). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Carrying n through the same model matrix gives n′ = (1, −4, 0), which is not perpendicular to t′, because t′ · n′ = 1 − 16 = −15.
- [ ] B. Carrying n through the inverse transpose of the matrix gives (1, −0.25, 0), which is perpendicular to t′, because t′ · n′ = 1 − 1 = 0.
- [ ] C. The model matrix gives correct normals under a non-uniform scale, so the inverse transpose is a mathematical convenience that can be skipped.
- [ ] D. If an object is only rotated or scaled equally on all axes, the model matrix followed by normalizing gives a normal with the right direction.
- [ ] E. Normalizing a normal after the model matrix has been applied repairs its direction under non-uniform scale, because normalizing removes the distortion.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The model matrix stretches the normal's y component the same way it stretches the surface, which tilts it out of perpendicular.
- B: The inverse transpose scales the normal's y component by 1/4 and keeps it perpendicular to the transformed surface.
- C: Under non-uniform scale the model matrix does not preserve perpendicularity, which is exactly why normals need the inverse transpose.
- D: A rotation or a uniform scale keeps angles, so only the length changes and normalizing fixes it.
- E: Normalizing changes length only; the direction (1, −4, 0) is still not perpendicular to t′.

**Source:** Normals and non-uniform scale

## MA-ch08.8

Shading languages let a variable be declared in full precision (32-bit float) or half precision (16-bit float). Half-precision values are spaced 1/1024 apart between 1 and 2, exactly 1 apart between 1024 and 2048, and exactly 2 apart between 2048 and 4096; the largest half-precision value is 65,504. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Half precision is fine for world positions in the thousands of units, because its range reaches 65,504 and range is what matters for a position.
- [ ] B. Half precision is usually adequate for colours in the range 0 to 1, where an error of about 0.001 is not visible.
- [ ] C. A half-precision variable can hold the value 3001 exactly, since 3001 is well inside the format's range.
- [ ] D. A half-precision variable holding 1500 stays at 1500 when 0.4 is added, because values there are 1 apart and 1500.4 rounds back.
- [ ] E. Half precision can be applied to a shader's variables as a routine speed-up, with no need to compare the picture afterwards, because the digits it loses are small.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The range is enough but the spacing at 3,000 is 2 units, so positions can only land on every second unit.
- B: Between 0.5 and 1 the spacing is about 0.0005, far below what an eye can see in a colour.
- C: Between 2048 and 4096 only even integers are representable, so 3001 rounds to 3000 or 3002.
- D: A change smaller than half the spacing is lost when the sum is rounded.
- E: The lost digits are small for colours but not for large values (at 3,000 the spacing is 2 units), so the picture can change; any speed-up also depends on the hardware, so the change has to be checked against the picture.

**Source:** Precision: float versus half

## MA-ch08.9

A scrolling-water effect looks smooth on the developer's desktop. On a mid-range phone, after the game has run for a while, the texture starts to move in visible jumps. The shader computes the texture offset as elapsed time × 0.1 and keeps it in a half-precision variable. By the time the jumps appear the offset has reached 10.0, where half-precision values are spaced 1/128 (0.0078125) apart. The water texture is 512 texels wide. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The smooth result on the desktop shows the shader is correct, because the same source ran there and produced the right motion.
- [ ] B. Near an offset of 10.0 the smallest representable change is 0.0078125, which is 4 texels of a 512-texel texture, so the motion advances in jumps.
- [ ] C. Switching to a larger texture, such as 1024 texels wide, would remove the jumps, because the jumps are measured in texels.
- [ ] D. Raising the frame rate would remove the jumps, because they come from how often the frame is drawn.
- [ ] E. A sound fix is to compute the offset in full precision, or to reduce it to its fractional part before storing it in half precision.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A desktop GPU may compute everything at full precision whatever the declaration says, so the bug can be invisible there.
- B: 0.0078125 × 512 = 4 texels, so the offset can only move in steps of 4 texels.
- C: The step in texture-coordinate units is unchanged, so on a 1024-texel texture the jump would grow to 8 texels.
- D: The jumps come from the spacing of representable values at that magnitude, not from how often the frame is drawn.
- E: Keeping the value small, or computing it at full precision, removes the coarse spacing.

**Source:** Precision symptoms on a phone

## MA-ch08.10

A GPU runs the fragment shader for neighbouring pixels together in lockstep groups (called warps, wavefronts or SIMD groups, depending on the vendor). A fragment shader contains an `if` whose two sides are each expensive, for example one side samples several textures and does long arithmetic. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. When the condition differs from pixel to pixel within a group, an `if` still saves time compared with computing both results and blending them, because each pixel runs the side it takes and skips the other.
- [ ] B. If all pixels in a group take the same side of the `if`, the group can run only that side and skip the other.
- [ ] C. If pixels in the same group disagree about the condition, the hardware runs both sides for that group with the non-participating pixels switched off.
- [ ] D. A condition computed from a value that differs from pixel to pixel, such as noise, is as cheap as a condition taken from a uniform.
- [ ] E. A condition taken from a uniform, which is constant across the whole draw, cannot make pixels in a group disagree.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Where pixels in a group disagree, the group runs both sides, so there is no saving, and computing both results and blending can be no slower.
- B: With a coherent condition the group follows a single path and the other side costs nothing.
- C: Divergence within a group forces both paths to execute in lockstep, with results masked.
- D: Per-pixel conditions can diverge within a group, so they can cost far more than a uniform-based one.
- E: Every pixel reads the same uniform value, so all of them take the same side.

**Source:** Branching cost on a GPU

## MA-ch08.11

A shader declares a uniform named `flash_amount` with a default of 0.0. A script sets it to 1.0 on one enemy when that enemy is hit. In play, all 12 enemies, which share a single material, flash at once. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The declared default is the value each object using the material has until something overrides it.
- [ ] B. The problem is a shader compile error, which would have been reported when the shader loaded, so the shader source must be fixed.
- [ ] C. A material is a shared asset: all objects that reference the same material see a change made to that material's parameter.
- [ ] D. Giving each enemy its own copy of the material, or using a per-instance parameter feature (such as Godot's instance uniforms on 3D nodes or Unity's material property blocks), limits the flash to the enemy hit.
- [ ] E. A reviewer should ask what the shader draws when no script has touched the parameter, because that default is what each object starts with.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A uniform's declared default applies to every user of the material until a parameter value replaces it.
- B: The shader compiled and ran; the symptom comes from where the parameter value is stored, not from invalid code.
- C: One material instance means one set of parameter values, so a write through any user is seen by all of them.
- D: Per-object materials or per-instance parameters give each enemy its own value of `flash_amount`.
- E: The unset state is the case most objects are in most of the time, so the default must itself be a correct look.

**Source:** Default uniform values and shared materials

## MA-ch08.12

A damage flash fades out over 33 frames, counted by adding 1 to an integer once per rendered frame. The design says the fade should last 0.55 seconds. The developer checks it only at 60 frames per second. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Passing the check at 60 frames per second shows that the fade is independent of the frame rate, since 60 is the usual rate.
- [ ] B. At 30 frames per second the fade lasts 1.1 seconds.
- [ ] C. Driving the fade from elapsed game time (the sum of each frame's delta time) makes its length independent of the frame rate, apart from one-frame granularity.
- [ ] D. At 144 frames per second the fade lasts about 1.3 seconds, because more frames per second means more time passes.
- [ ] E. At exactly 60 frames per second, 33 frames last 0.55 seconds, so there a frame counter and the design agree.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: At 60 frames per second a 33-frame counter and a 0.55 s clock are the same function, so that rate cannot tell them apart.
- B: 33 / 30 = 1.1 seconds.
- C: Accumulated delta time measures real game time, so the fade ends at the same moment at any frame rate.
- D: 33 / 144 is about 0.23 seconds, so the fade is shorter, not longer.
- E: 33 / 60 = 0.55 seconds, which is why a check at that single rate passes.

**Source:** Frame count versus game time

## MA-ch08.13

An agent writes a new automated check for a shader's behaviour and runs it against the changed code. It passes, and the agent reports that the change is verified. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent wrote the change and the check as two separate pieces of code, so a pass confirms the change independently of the agent's own assumptions.
- [ ] B. Running the same check ten more times against the same changed code adds confidence that the check can detect the bug.
- [ ] C. The check becomes evidence about the change once it has been shown to fail on a known-bad version and to pass on a known-good one.
- [ ] D. A check that passes on the known-bad version as well as on the known-good one still supports the change under review, because it passed on that change too.
- [ ] E. When a check fails on a version known to be good, the fault lies in that version, because the check encodes what the design requires.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Separate files do not make separate assumptions: both came from the same author, so they can share the same mistake.
- B: Repeating a run against one version cannot show whether the check would notice a bug if there were one.
- C: A check that separates known-bad from known-good output carries information about the change; one that has not been shown to do so carries none.
- D: A check that cannot tell good from bad passes whatever the change does, so its pass on the change means nothing.
- E: A failure on known-good code often means the check is wrong, for example a tolerance that is too tight, so the check must be examined as well as the code.

**Source:** Testing the test

## MA-ch08.14

A shader should move its colour from a base colour toward a flash colour by an amount between 0 and 1: output = base + (flash − base) × amount, with alpha unchanged. A test oracle is whatever a test compares a result against. An agent's shader contains a mistake in that formula, yet the agent's test passes, because the test computes its expected values by copying the formula from the shader. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An oracle copied from the code under test is preferable, since it follows changes to the code without extra maintenance.
- [ ] B. An oracle written from the specification (amount 0 gives the base, amount 1 gives the flash colour, a straight line between) would have caught the mistake.
- [ ] C. For base (0.8, 0.4, 0.3), flash (0.1, 0.2, 0.3) and amount 0.5, the specification gives (0.45, 0.30, 0.30), computable on the CPU without running the shader.
- [ ] D. A CPU calculation of the specification replaces the need to look at what the GPU actually drew, because both follow the same arithmetic.
- [ ] E. An oracle written from the specification stays valid when the shader is rewritten; one copied from the implementation is valid only while that implementation lasts.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A copied formula repeats the code's mistakes, so it can never disagree with the code.
- B: An independent statement of the rule disagrees with a wrong formula and exposes it.
- C: 0.8 + (0.1 − 0.8) × 0.5 = 0.45, 0.4 + (0.2 − 0.4) × 0.5 = 0.30, and blue is 0.3 at both ends.
- D: The model says what the screen should show, not what the GPU produced, so only observation closes that gap.
- E: A specification does not depend on how the shader is written, whereas a copy of the code does.

**Source:** Specification oracle and CPU model

## MA-ch08.15

A game renders at 1920 × 1080, which is 2,073,600 pixels. After the scene is drawn, three full-screen translucent layers are drawn on top of it: fog, a damage vignette and a colour grade. Each layer runs a fragment shader once for every pixel it covers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Together the three layers run the fragment shader 6,220,800 times per frame (3 × 2,073,600).
- [ ] B. Rendering the same frame at 3840 × 2160 multiplies each layer's invocations by 4, to 8,294,400.
- [ ] C. A layer's cost depends mainly on how many triangles its mesh has, so a full-screen layer drawn as two triangles is almost free.
- [ ] D. Combining the three effects into one full-screen pass shades each pixel once instead of three times, although that one shader does more work per pixel.
- [ ] E. For a 20,000-vertex mesh covering a 1080p screen, the fragment stage runs about 104 times as often as the vertex stage, so a linearly varying value is cheaper computed per vertex.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: 3 × 2,073,600 = 6,220,800 invocations per frame.
- B: 3840 × 2160 = 8,294,400, exactly four times 2,073,600.
- C: Fragment cost follows the number of pixels covered, and two triangles can cover the whole screen.
- D: One pass means one invocation per pixel instead of three, at the price of a heavier shader.
- E: 2,073,600 / 20,000 is about 104, and interpolation of a linear value gives the same result at that lower frequency.

**Source:** Fragment cost and overdraw

## MA-ch08.16

While reviewing an agent's shader change, a developer prepares controlled inputs: test values chosen so that the correct output and the wrong output are far apart and easy to compute. Two suspected mistakes are alpha being applied twice and a flipped vertical texture coordinate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A test texture that is red along the top and blue along the bottom exposes a vertical flip; a texture identical top to bottom could not.
- [ ] B. A fully opaque test pixel (alpha 1.0) is the best input for exposing alpha applied twice, because it gives the cleanest colour reading.
- [ ] C. A texture that is symmetric from top to bottom is as good as an asymmetric one for exposing a flipped coordinate, since the arithmetic is the same either way.
- [ ] D. A vertical flip turns the picture through 180 degrees, so left and right are swapped as well as top and bottom.
- [ ] E. A shader that multiplies colour by alpha and is then drawn with ordinary alpha blending applies alpha twice: white at alpha 0.5 over black gives 0.25, not 0.5.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A flip swaps top and bottom, which is only visible if top and bottom differ.
- B: Multiplying by an alpha of 1.0 changes nothing, so doubling it is invisible.
- C: A texture that looks the same upside down looks the same flipped, so it hides the bug.
- D: A vertical flip is a mirror in the vertical direction only; left and right keep their places.
- E: 1.0 × 0.5 = 0.5 is already premultiplied, and the blend then multiplies by 0.5 again to give 0.25.

**Source:** Plausible-but-wrong changes and controlled inputs

## MA-ch08.17

A developer must give a coding agent a specification for a character's hit flash, precise enough that the result can be checked against it on any device, whatever its frame rate. Check each instruction that meets that bar. Each statement is worth 1 point (5 points total).

- [ ] A. "Add a flash amount from 0 to 1 (0 leaves the incoming colour as it is, 1 gives (0.15, 0.21, 0.29), values in between are a linear mix, alpha unchanged), and after a hit let it fall from 1 to 0 over 33 rendered frames."
- [ ] B. "Add a flash amount from 0 to 1 that pushes the player's colour toward (0.15, 0.21, 0.29), and after a hit let it fall from 1 to 0 over 0.55 seconds of game time."
- [ ] C. "Add a flash amount from 0 to 1: at 0 the output equals the incoming colour, at 1 it equals (0.15, 0.21, 0.29), in between a linear mix, alpha unchanged. After a hit the amount jumps to 1 and then returns to 0, so the player looks normal again."
- [ ] D. "Add a flash amount from 0 to 1: at 0 the output equals the incoming colour exactly, at 1 it equals (0.15, 0.21, 0.29), in between a linear mix, alpha unchanged. After a hit it falls from 1 to 0 over 0.55 seconds of game time."
- [ ] E. "Add a flash amount from 0 to 1: at 0 the output equals the incoming colour, at 1 it equals a strong red, in between a linear mix, alpha unchanged. After a hit it falls from 1 to 0 over 0.55 seconds of game time."

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: A duration counted in rendered frames lasts a different time at each frame rate, so it cannot be checked against one fixed duration on every device.
- B: It names a colour and a duration but never says what the output is at any amount, so there is no expected pixel value to compare with.
- C: With no duration the fade could take any time and still count as correct, so the timing cannot be checked.
- D: It fixes the endpoints, the in-between rule, alpha and the timing in game time, so each can be tested with chosen inputs.
- E: "A strong red" is not a value, so no captured pixel can be compared with the flash colour.

**Source:** A precise specification to hand an agent
