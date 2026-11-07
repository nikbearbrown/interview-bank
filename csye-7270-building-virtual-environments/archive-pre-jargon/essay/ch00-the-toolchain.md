# Chapter 0: The toolchain

## ES-ch00.1

A developer types this to a coding agent working in a game project: 'Add a score to my two-player paddle game and make sure everything still works.' Rewrite the request as a precise instruction, using the right terms for behaviour, constraints, checks and evidence, and include a new test for the score. Then explain at least three different things the agent could build or report wrongly because of the original wording.

**Points:** 5

**Rubric (1 point each):**

1. States the required behaviour in observable terms (for example a point goes to a named player when the ball leaves through a named edge, and where both scores are displayed) instead of 'a score'.
2. Fences off what must not change (such as paddle movement, ball speed and bounce rules) and says which files not to edit; naming files to read first is optional.
3. Says exactly how the checks are run so that anyone can repeat them from the command line (for example headless, with the frame rate pinned, under a time limit, with exit code 0 as the pass condition), and asks for the real command output rather than a summary; any equivalent repeatable check that returns its evidence earns the point.
4. Requires a new test that exercises the real behaviour and checks observed state (for example by driving the game through its normal input events); a clearly labelled direct placement of the ball or paddles for setup is acceptable, but the score being asserted must not be written directly.
5. Names at least three ways the original wording could go wrong, such as 'works' meaning only 'it runs', a test weakened to pass, edits to unrelated behaviour, or a flaky run reported as a pass.

**Source:** Say it to the agent: vague request rewrite

## ES-ch00.2

A regression test for a game passes on one laptop and fails on another, and sometimes fails then passes on the same laptop with no change to the code. The test presses keys for a fixed number of frames. The game moves objects by speed times delta, where delta is the real time since the previous frame. Explain what 'flaky' means, why this test is flaky, and two different ways to make it deterministic. Say what you would check before concluding that the game code is at fault.

**Points:** 5

**Rubric (1 point each):**

1. Defines a flaky test as one whose result varies with no change to the code or the test, and a deterministic test as one that gives the same result every run from the same code and inputs.
2. Explains the mismatch: the test counts frames, but the game advances by delta seconds, and frame duration depends on load and hardware, so the same frame count covers different amounts of game time.
3. Gives the first fix: run the engine with a fixed frame rate so every frame represents the same game time, whatever the machine does.
4. Gives the second fix: express the test in game seconds (hold the key for a stated amount of game time) instead of counting rendered frames.
5. Says what to check first: reproduce under the pinned configuration, change one variable at a time, repeat runs and compare recorded numbers.

**Source:** Flaky tests and fixed frame rate

## ES-ch00.3

A coding agent reports 'Done, all tests pass.' For each of the following, say what it shows and what it does not show: the agent's report; a diff of the changes; a clean import and parse check; a passing automated headless test with the time step pinned; a person playing the game; a build running on the target platform. Then say which you would require before accepting the change and why.

**Points:** 5

**Rubric (1 point each):**

1. Treats the agent's report as a claim that shows only that the agent produced a message, and says why the developer's own rerun is evidence.
2. Says a diff shows exactly which lines changed but not that the change works, and a clean import and parse check shows only that files load and scripts parse, not that behaviour is right.
3. Says a passing headless test with a pinned time step shows the tested state is right under that scripted input, while not covering look, feel, readability or unscripted inputs.
4. Says a person playing shows what one person experiences on one machine, and a build running on the target shows the game survives packaging, not that anyone wants to play it.
5. Names a justified minimum, for example reading the diff, rerunning the pinned test oneself and checking that no test was weakened, plus a human playtest for anything about feel.

**Source:** Done claim versus evidence

## ES-ch00.4

A developer wants a coding agent to import a game project and run its headless tests, but not to run arbitrary commands. Three options are on the table: (a) an allow rule for any command starting with the engine's program name; (b) allow rules for exact commands with fixed arguments; (c) running everything in a sandbox that can write only inside the project folder. Explain the difference between a permission grant and a sandbox, assess each option, and describe what the developer should still do personally.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the two: an allow rule decides which commands run without asking a human, while a sandbox technically limits what any running process can read, write or reach.
2. Judges (a) as wide: an engine that can run a script file can run whatever code that script contains, including starting other programs, so a program-name rule is not a boundary on behaviour.
3. Judges (b) as narrower and easier to reason about, while noting that an exact-match rule is narrow and may need updating when the command changes, and that rules should grant only what the developer can read and understand.
4. Judges (c) as limiting damage outside the folder but not inside it: the agent can still delete or overwrite project files and its own evidence, and legitimate writes outside the folder can fail with errors.
5. Says the developer should still read new commands and scripts before approving them, and review the diff before committing.

**Source:** Permissions and sandbox

## ES-ch00.5

A coding agent ran a project's regression test the wrong way, the test failed, and the agent gave a confident but wrong explanation. After the developer added a short section to a standing instruction file in the repository, the same request produced a correct run. Explain what 'context' means for an agent, why a standing instruction file helps, what that section should contain, and what it cannot do.

**Points:** 5

**Rubric (1 point each):**

1. Defines context as the text available to the agent now (instructions, files it has read, command output), limited in size, with a new session starting without earlier conversations.
2. Explains that project-specific facts such as how to run tests, required flags and setup steps cannot be known unless written down, so the agent guesses and may produce a plausible but wrong run.
3. Lists what the section should contain: exact commands, required options (for example headless and a pinned frame rate), setup steps such as the import step, the expected result (exit code, expected numbers), a time limit, and which outputs to keep.
4. Says the file should also state what must stay a human decision or must not be edited.
5. Says a fluent explanation is not evidence and the instruction file does not guarantee identical design choices across runs, so the developer still verifies by their own run and reads the diff.

**Source:** Context and instruction files

## ES-ch00.6

A developer wants to verify, without opening a window, that a score label shows the correct number after the ball leaves the left edge of a game. Design the test: how it starts the game, how it drives it, what it reads, how it reports its result to a script, and how it guards against hanging. Then name two things this test cannot establish.

**Points:** 5

**Rubric (1 point each):**

1. Loads the real game scene and drives it without shortcuts, either with the game's normal input events or by letting the real game play until the ball leaves, rather than writing the score or the ball's position directly.
2. Reads observable state: the score counter and the score label's text, compares them with the number of edge events it counted, and pins the time step so the run is repeatable.
3. Reports through the exit code (0 for pass, nonzero for fail) plus a readable report.
4. Guards against hanging by calling quit explicitly at the end and running the command under a time limit.
5. Names two limits, such as how the number actually looks when rendered (legibility, placement, overlap with other objects), how the game feels or whether the serve is fair, and behaviour under inputs or machines the test did not cover.

**Source:** Headless test design
