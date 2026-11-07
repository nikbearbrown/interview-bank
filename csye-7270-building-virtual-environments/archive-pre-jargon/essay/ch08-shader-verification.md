# Chapter 8: Shader verification

## ES-ch08.1

A coding agent submits a change to a shader with the summary: "Compiles cleanly, all existing tests pass, verified." Explain the different kinds of evidence a reviewer can ask for, ordered from weakest to strongest, and say what each one can establish and what it cannot. Include at least one thing that only a person looking at a real screen, or a run on real graphics hardware, can establish. Also say how you would treat the word "verified" in the summary.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the compile or parse check as the weakest rung: it shows the source is valid (syntax and types) and says nothing about what the shader outputs.
2. Describes checks of the shader's contract and of the code that drives it (uniform names, types and defaults, and that game code sets the right values at the right moments), which can run without a display but still say nothing about pixels.
3. Describes a calculation of what the output should be for chosen inputs, worked out on the CPU from the specification, and notes it states the expected result, not what the GPU drew (this rung and the previous one may be given in either order).
4. Describes observation: rendering a fixed test scene, capturing it and comparing pixel values or a reference image, and says that only real hardware (or a person looking at a real screen) shows the driver, precision and timing behaviour of a real device (noting that a headless run with a dummy renderer gives no pixel evidence is welcome but not required).
5. Distinguishes a claim from evidence: asks which of the agent's statements were observed and which inferred, and treats "verified" with no named check or result as an unsupported claim.

**Source:** Evidence versus a claim of success

## ES-ch08.2

A developer gives a coding agent this instruction: "Add a damage flash to the player and make sure it works." Rewrite the instruction precisely, using the correct terms, so that the result can be checked. Then explain what the agent could build wrongly, or wrongly claim, if the original wording were used.

**Points:** 5

**Rubric (1 point each):**

1. The rewrite names a shader parameter (a uniform) with a stated range and gives the output rule: at 0 the output equals the original colour exactly, at 1 it equals a named flash colour, in between a linear mix, with alpha unchanged (the point is earned when at least four of these five elements are present).
2. The rewrite states the timing in game time (seconds, from per-frame delta time) rather than in frames, gives a duration, and requires the same duration at different frame rates.
3. The rewrite states the trigger and the scope: the flash starts when the player is hit, applies to the player only, and returns to 0 when it ends.
4. The rewrite asks for specific evidence: a fixed test scene with known inputs, captured pixel values next to expected values, a check shown to fail on a known-bad version, and a report separating what was observed from what was assumed (the point is earned when at least three of these four elements are present).
5. Explains the consequences of the vague wording: the agent could count frames, mix against the wrong input, apply alpha twice, change a shared material so every sprite flashes, never reset the parameter, or report success from a clean compile alone.

**Source:** Say it to the agent: a precise shader specification

## ES-ch08.3

An agent adds a test for a fade effect by recomputing the expected value with the same formula that appears in the shader. The test passes on a change that contains a real bug. Explain why it passes, what a better oracle would be, and how the developer can show that a new check can be trusted. Explain why a check run at a single setting, such as one frame rate, can mislead, and how to avoid that.

**Points:** 5

**Rubric (1 point each):**

1. Defines a test oracle as what a test compares against, and explains why the test passes: an expected value copied from the shader's formula repeats the shader's mistake, so passing is circular.
2. Proposes an oracle written from the specification (endpoint values and the intended rule) and computed independently of the shader code.
3. Explains testing the test: run the check against a known-good and a known-bad version; it must pass the first and fail the second before its pass counts as evidence, and a failure on known-good code means the check itself may be wrong (for example a tolerance that is too tight).
4. Explains why a single setting can mislead: a correct and a wrong implementation can give the same result at that setting (for example a frame-counted fade and a time-based fade agree at exactly one frame rate).
5. Says the check should be run at several settings, chosen where right and wrong answers differ (for example 30, 60 and 144 frames per second); an illustrative worked example is welcome, such as a 33-frame counter lasting 0.55 s at 60 frames per second, 1.1 s at 30 and about 0.23 s at 144.

**Source:** Specification oracle and testing the test

## ES-ch08.4

Define local, world, view and screen space. Describe a bug caused by mixing two of them in a shader, the symptom a player or tester would see, a controlled test that would expose it, and what you would tell a coding agent to prevent it. (Any valid pair of spaces may be chosen.)

**Points:** 5

**Rubric (1 point each):**

1. Defines all four spaces correctly: local relative to the object's origin, world shared by the scene, view relative to the camera, screen as the position on the display (usually pixels).
2. Gives a concrete mixed-space bug, such as comparing a local-space position with a world-space height, combining a local normal with a world-space light direction, or using a view-space position where a world-space one is meant.
3. Describes a symptom that matches the bug chosen: for a local-versus-world mix, the effect follows the object, rotates with it or depends on where the object was placed instead of staying fixed in the world; for a view-versus-world mix, it changes as the camera moves.
4. Describes a controlled test that varies what the chosen bug depends on (moving, rotating and scaling the object for a local-versus-world mix, moving the camera for a view-versus-world mix), because a trivial transform hides the bug; a student whose bug involves normals may cite the inverse transpose under non-uniform scale as the reason the test needs a non-uniform scale.
5. Says what to tell the agent: name the space of every input and output, require the conversion (for example "convert the position to world space with the model transform before comparing") and ask for a test at a non-trivial transform.

**Source:** Coordinate spaces and mixing them up

## ES-ch08.5

A shader looks right and runs smoothly on the developer's desktop, but on a mid-range phone it shows stepping or flicker and the frame rate drops. Give four distinct possible causes involving precision, branching, fragment cost and platform differences, and explain how you would gather evidence for each rather than guessing, including on what hardware the measurements must be taken.

**Points:** 5

**Rubric (1 point each):**

1. Precision: reduced (half) precision may really be used on the phone, so large values such as time or world position lose resolution; evidence comes from forcing full precision or testing at large values and comparing.
2. Branching: a condition that differs between neighbouring pixels makes the hardware run both sides; evidence comes from timing the shader with the branch removed or its condition made uniform.
3. Fragment cost: cost is pixels covered times layers times work per pixel; evidence comes from lowering the resolution and seeing whether frame time falls noticeably (close to proportionally if the shader is fragment-bound).
4. Measurements about the phone must come from the phone with a profiler, not from the desktop, a headless run or a software renderer.
5. Platform differences: the same shader can legitimately render differently across GPUs and drivers, so captures from the phone are compared with a reference for that platform within a stated tolerance.

**Source:** Precision, branching and fragment cost on mobile

## ES-ch08.6

Design a golden-image (screenshot comparison) test process for a library of shaders. Cover what is rendered, how differences are judged, who approves a reference image, how different platforms are handled, and what a passing result does and does not prove.

**Points:** 5

**Rubric (1 point each):**

1. Specifies a fixed test scene: fixed camera, resolution, inputs, pinned clock and no randomness, so any difference comes from the shader.
2. Requires a person to review and approve each reference image, and for any later update to be reviewed, because a reference captured from a buggy build bakes the bug in.
3. Sets a tolerance (per-channel difference and the share of pixels allowed to differ) and explains the trade-off: too tight gives false failures from driver differences, too loose hides small real defects.
4. Keeps separate references per platform, graphics API or colour space, because correct output can differ between them.
5. States the limits: a pass only means the output matches the baseline for what the scene exercises, not that it is right, and the process needs a renderer that actually draws pixels (not a dummy or headless driver), with real hardware needed to say anything about real devices.

**Source:** Screenshot and golden-image comparison
