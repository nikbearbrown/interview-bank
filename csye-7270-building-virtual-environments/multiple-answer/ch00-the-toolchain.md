# Chapter 0: The toolchain

## MA-ch00.1

A developer starts a Godot editor executable from a terminal window by typing its program name followed by `--path my_game --headless`, instead of double-clicking the editor icon. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A coding agent can run the same typed command a person would, which is why the command line is a natural way for an agent to start and check a game.
- [ ] B. Accepting typed options means a separate command-line edition of the engine must be installed, because the editor application itself cannot take options.
- [ ] C. The shell is the program that reads the typed line, splits it into a program name and its arguments, and starts that program.
- [ ] D. Writing `MY_VAR=1` before the program name, as in `MY_VAR=1 godot ...`, passes a flag called MY_VAR to the engine.
- [ ] E. `--headless` is a flag: an option written after the program name that changes how this one run behaves.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Typed commands are text, so an agent can issue them, read their output and read their exit status.
- B: The same Godot executable that opens the editor also accepts command-line options; no separate edition is required.
- C: The shell interprets the typed command and launches the program; the terminal window only displays text and passes keystrokes.
- D: That syntax sets an environment variable for the started process; it is not a command-line flag.
- E: Flags are the options a command-line program accepts; they alter the behaviour of that single invocation.

**Source:** CLI, shell and flags

## MA-ch00.2

A developer runs a Godot project with the `--headless` option and a test script that drives the game for 600 frames. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A headless test can confirm that a score label is readable on screen by inspecting the frame the engine rendered.
- [ ] B. Scripts, physics and signals still run, so a test can read a counter, a label's text or which signal fired.
- [ ] C. In headless mode the engine loads the scene files but skips running game scripts, since scripts matter only when something is drawn.
- [ ] D. No window is opened and audio goes to a dummy driver, so the run produces neither picture nor sound.
- [ ] E. A headless run that exits successfully shows the game looks correct on a player's screen, since the same scene was loaded.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Headless mode draws no frame, so there are no pixels to inspect; legibility and placement need a person looking at a rendered image.
- B: Game logic is unaffected; a headless test observes state, not pixels.
- C: Scripts run normally; headless removes the window and sound, not the game logic.
- D: Headless mode means no display and no audio output.
- E: A successful exit says nothing about what is rendered.

**Source:** Headless mode

## MA-ch00.3

A test script for a game runs without a window. When it finishes, the shell reports the program's exit code. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An exit code of 0 shows that the test contained meaningful checks, since an empty test would have failed.
- [ ] B. A nonzero exit code is a sign that the program crashed; a test that deliberately reports a failed check leaves the code at 0 and signals the failure in its printed text.
- [ ] C. If a program prints error messages to its error output, its exit code must be nonzero, because the two go together.
- [ ] D. Quitting with a nonzero code when a check fails lets a script detect the failure without reading printed text.
- [ ] E. An exit code is a small integer a program hands back to the program that started it, and by convention 0 means success.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: A test with no assertions, or one that ignores engine errors, also exits 0.
- B: Test programs commonly exit nonzero on purpose when a check fails.
- C: A program can print errors and still exit 0; engines can report script errors while the test itself exits successfully.
- D: The exit code is the machine-readable verdict.
- E: This is the standard process-status convention that scripts and automation rely on.

**Source:** Exit codes

## MA-ch00.4

A headless test script in a game engine is supposed to call a quit function after its last check. It contains a bug that raises an error before the quit call is reached, and the engine keeps running its main loop with no window to close. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Running the command under a timeout utility turns a stuck test into a failure after a set number of seconds.
- [ ] B. A sensible timeout is longer than a healthy run takes, with some margin.
- [ ] C. The process can run indefinitely: nothing tells it to stop and no window exists to close.
- [ ] D. Because the script's last line calls quit, a timeout adds no protection: the quit call ends the run.
- [ ] E. A timeout speeds up a slow test by telling the engine to skip waiting between frames.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A timeout turns a hang into a detectable failure.
- B: Too short a limit kills healthy runs and creates false failures.
- C: Under the stated assumption the main loop never ends on its own.
- D: If an error stops execution before that line, the quit call is never reached.
- E: A timeout only stops the run when the limit is hit; it does not speed anything up.

**Source:** Timeouts

## MA-ch00.5

A developer clones a game project from a repository. The repository holds source images, audio and scenes, plus small per-asset settings files, but not the engine's generated cache folder. The developer's setup script first runs the engine once in import mode and only then runs tests. In Godot terms, check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The cache folder is normally kept out of version control because it is generated and can be rebuilt.
- [ ] B. Importing rewrites the source image files in place, recompressing their pixels to save disk space.
- [ ] C. If the import step is skipped, the missing cache proves the repository was cloned incorrectly or is corrupted.
- [ ] D. Import converts source assets into the engine's runtime formats and stores them in the cache folder.
- [ ] E. The per-asset settings files recording how each asset is imported belong in the repository.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Godot's documentation advises against committing the cache and says it reimports automatically when it is missing.
- B: Import writes converted copies into the cache and leaves the source file alone.
- C: A fresh clone lacks the cache by design; the engine just has not built it yet.
- D: Godot does not use the raw PNG or WAV at runtime; it uses the imported copy.
- E: Godot's documentation says to commit the .import files because they hold important metadata.

**Source:** Import step

## MA-ch00.6

A coding agent has edited several files in a project that is tracked in a repository. Before accepting anything, the developer wants to know exactly what changed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reading the diff before committing is unnecessary when the agent's own report lists the files it changed.
- [ ] B. A repository is the project's files together with the recorded history of its earlier versions.
- [ ] C. A diff shows, line by line, how one version differs from another, such as the working files versus the last commit.
- [ ] D. A commit pushes the change to a shared server so teammates receive it immediately.
- [ ] E. A diff with only a few changed lines proves the change works, because a diff lists only lines that ran successfully.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The report is a claim; stray files, edited documents or weakened tests show up only in the diff.
- B: Version history is what lets 'what changed?' have an exact answer.
- C: A diff is the exact record of added, removed and changed lines.
- D: A commit records a snapshot in local history; sharing is a separate push step.
- E: A diff records what changed, not whether the changed code behaves correctly.

**Source:** Repository, diff and commit

## MA-ch00.7

A developer lets a coding agent run shell commands without asking whenever they match an allow rule. To save time, the developer writes one rule matching any command that starts with `env` and another matching any command that starts with the game engine's program name. The engine can run a script file given on its command line, and that script may start other programs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A permission prompt is a chance to review the command or script, not a formality to click through.
- [ ] B. A rule allowing one exact command with fixed arguments is a narrower boundary than a wildcard on the program name.
- [ ] C. A broad engine rule also allows any code in a script the agent wrote, including code that starts other programs.
- [ ] D. An allow rule limits what an allowed program may do internally once it is running, for example which files it opens.
- [ ] E. `env` runs the command given as its arguments, so an `env` rule also allows the program that follows it.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The prompt is the point where a human can catch a command broader than intended.
- B: The fewer variations a rule matches, the less it grants.
- C: An allow rule bounds which program starts, not what a script run by that program does.
- D: Allow rules decide which commands start without asking; they do not constrain a running program's behaviour.
- E: `env NAME=value program ...` starts the named program, so the rule is as wide as 'run anything'.

**Source:** Permissions and allowlists

## MA-ch00.8

A coding agent runs in a sandbox that lets it write only inside the project folder. During an import step the engine prints an error that it cannot save its own settings file, which lives in the user's home directory, yet the import still produces a usable project. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Running in a sandbox confirms that the code the agent writes is correct, because the agent could not reach anything outside the project folder.
- [ ] B. A sandbox is a technical limit on what a process may read, write or reach.
- [ ] C. A sandbox and a permission prompt are the same mechanism under two names, one for editors and one for terminals.
- [ ] D. The error fits a sandbox blocking a write outside the project folder while writes inside it succeed.
- [ ] E. Inside this sandbox the agent can still delete project files, including test output it produced earlier.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: A sandbox limits damage; it says nothing about whether the code does what was asked.
- B: Sandboxes restrict capabilities at the operating-system level, independent of the agent's intentions.
- C: A prompt asks a human before a command runs; a sandbox enforces limits on what any running command can touch.
- D: The settings file is outside the project folder; the project cache is inside it.
- E: The sandbox allows writes inside the workspace, and deletion is a kind of write.

**Source:** Sandbox

## MA-ch00.9

Two developers ask a coding agent for the same feature, a score counter in a two-player paddle game. Developer X writes: 'add a nice score system'. Developer Y writes a request that lists the observable behaviour (a point goes to the right player when the ball leaves through the left edge), what must not change (paddle and ball behaviour), which files to read first, how to run the existing checks, and 'show me the real command output; do not commit'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Stating what must not change helps, because an agent that is not told may alter related behaviour while it works.
- [ ] B. Adding adjectives such as 'robust' and 'clean' to X's request would turn it into a precise spec, because they describe the quality wanted.
- [ ] C. Y's request works as a spec: required behaviour, limits and a way to check the result.
- [ ] D. Asking for real command output instead of a summary matters: a description is a claim, output can be inspected.
- [ ] E. X's request leaves the agent to choose where the score is shown, which event changes it and what counts as finished.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Explicit limits keep the change bounded.
- B: Adjectives add mood, not checkable behaviour or constraints.
- C: A spec makes 'done' decidable; a bare prompt does not.
- D: Output can be checked against a rerun; a summary cannot.
- E: Every unstated decision is a place where the agent can build something other than what was meant.

**Source:** Prompt versus spec

## MA-ch00.10

Yesterday a developer spent an hour in one long session teaching a coding agent how to run a project's checks, which need a special flag. Today the developer starts a new session in the same repository and says only: 'run the checks and fix what fails'. No instruction file in the repository mentions the flag. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent will remember the flag, because the same underlying model is being used and the project is the same.
- [ ] B. The new session starts without yesterday's conversation; the agent knows only what it is given or can read.
- [ ] C. A larger context window would let the agent recall yesterday's session, since more of the past could be kept.
- [ ] D. If the agent runs the checks without the flag and they fail, the failure is evidence that the game itself is broken.
- [ ] E. Because language models know many projects, the agent can deduce the missing flag from the project's name alone.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Using the same model does not carry over a past session's content.
- B: An agent's context is the text available to it now, and a fresh session starts without earlier conversations.
- C: Size is not the issue; yesterday's text is simply not in today's context.
- D: The failure may come from running the checks the wrong way, which is a different problem from a broken game.
- E: A project-specific flag has to be written down or discovered; a name does not reveal it.

**Source:** Context

## MA-ch00.11

A developer asks a coding agent to add a pause feature to a game: pressing the pause key stops the ball, and pressing it again resumes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An acceptance test checks the agreed behaviour from the outside, the way a player would exercise it.
- [ ] B. A test that sets the game's 'paused' variable to true directly and then checks that it is true is a strong acceptance test of the pause key.
- [ ] C. A stronger test sends the pause key through normal input handling, then checks the ball's position stays put.
- [ ] D. If the new test fails, loosening its checks until it passes gives the same evidence as a pass of the original checks.
- [ ] E. The agent should take the acceptance test's expected results from what its finished code does, so that the test fits what was built.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Acceptance is judged on observable behaviour, not on how the code is written.
- B: It never exercises the key press, so it would pass even if the key were not connected to anything.
- C: It follows the real chain from input to observable state.
- D: A weakened test certifies less; the original failure is the information that matters.
- E: Expected results copied from what the code does can only confirm the code; they should come from the required behaviour, stated independently of the implementation.

**Source:** Acceptance tests

## MA-ch00.12

A coding agent finishes a change to a game and reports: 'Done. All tests pass.' The developer thinks about what each thing they could look at actually establishes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A diff shows exactly which lines changed but does not show that the changed code behaves correctly.
- [ ] B. A passing automated test with the time step pinned shows the tested state is right under that scripted input; it does not show the game is fun or readable.
- [ ] C. Once one person has played the game for five minutes, the change counts as verified for other players and machines.
- [ ] D. The agent's report is a claim; running the same command yourself and seeing the same output is evidence.
- [ ] E. If the agent also pastes the test output, the developer can treat the result as verified without rerunning anything, because the text was copied from the run.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A diff describes the change, not its correctness.
- B: A test bounds what it can speak to: the state it reads, under the inputs it feeds.
- C: A single playtest shows one person's experience on one machine.
- D: Evidence is something the developer can reproduce and inspect, not something the agent asserts.
- E: Output may come from a differently configured run or be selective; reproducing it yourself is the check.

**Source:** Done claim versus evidence

## MA-ch00.13

A test presses the 'up' key for exactly 600 frames and then checks that a paddle has reached the top wall. The paddle's movement is speed times delta, where delta is the real time since the previous frame. With no change to the code or the test, it passes on 7 of 10 runs on a busy laptop and on 10 of 10 runs on an idle one. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A test that passes ten times in a row is proven deterministic, since ten identical results rule out chance.
- [ ] B. Seeding the random number generator is enough to remove this variation, because the variation must come from randomness.
- [ ] C. This test is flaky: its outcome varies between runs with no change to the code or the test.
- [ ] D. A plausible cause: frame length varies with machine load, so 600 frames span different amounts of game time.
- [ ] E. Re-running the test until it passes and keeping that run is a sound fix for the variation.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Ten passes are consistent with a failure that is merely rare or load-dependent.
- B: The unpinned quantity here is frame timing, which a random seed does not control.
- C: That is the definition of flakiness.
- D: The test counts frames while the game advances in seconds.
- E: It hides the variation instead of removing its cause.

**Source:** Flaky versus deterministic tests

## MA-ch00.14

A game moves a paddle at 240 units per second by adding 240 times delta each frame, where delta is the game time that one frame represents. A test holds the 'up' key for exactly 150 frames and then reads how far the paddle moved. The engine is started with an option that forces a fixed frame rate, so every frame represents exactly 1/fps seconds of game time, whatever the machine is doing; the engine does not pause between frames to match the wall clock. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With a fixed 120 frames per second and the same 150 frames, the paddle moves 300 units.
- [ ] B. Because the frame length is pinned to 1/fps seconds, the test takes as many real seconds to run as the game time it simulates.
- [ ] C. With a fixed 60 frames per second the paddle moves 600 units (150 frames at 4 units per frame).
- [ ] D. If the test holds the key for 2.5 seconds of game time instead, the paddle moves 600 units at both 60 and 120 fps.
- [ ] E. Forcing the frame rate makes a frame-counting test repeatable, because each frame is the same game time on all machines.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: 150 frames is 1.25 s of game time, and 240 x 1.25 = 300.
- B: Game time per frame is pinned, but the engine does not wait on the wall clock, so the run takes as long as the machine needs and can finish far faster or slower than the game time it simulates.
- C: Each frame is 1/60 s, so 150 frames is 2.5 s and 240 x 2.5 = 600.
- D: Measuring game time instead of frames removes the dependence on frame rate; at 120 fps that means 300 frames.
- E: Pinning the time step removes the machine-dependent quantity.

**Source:** Fixed frame rate in tests

## MA-ch00.15

A developer wants a coding agent to fix a bug in a game and to prove the fix. Several instructions are being considered. Check each statement that is true about whether the quoted instruction is precise enough to be checked. Each statement is worth 1 point (5 points total).

- [ ] A. 'Make sure it all works now.' This is checkable, because 'works' covers the test, the build and how the game feels.
- [ ] B. 'Do not commit; leave the changes uncommitted so I can read the diff.' This keeps acceptance with the developer.
- [ ] C. 'Do what it takes to get the test suite green.' This is precise, because 'green' is a measurable state.
- [ ] D. 'If an existing test fails, report which and stop; do not edit tests.' This blocks the shortcut of rewriting a failing test.
- [ ] E. 'Run the regression test headless at a fixed 60 fps; it must exit 0; paste the command and its full output.' This fixes conditions, pass criterion and evidence.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The word has no pass condition; each person and each agent can read it differently.
- B: It separates making the change from accepting it.
- C: The state is measurable, but the instruction permits weakening or deleting tests to reach it.
- D: It forbids the cheapest way to turn red into green without fixing anything.
- E: Each element can be verified by rerunning the command.

**Source:** Say it to the agent: checkable instructions

## MA-ch00.16

A studio is deciding whether a coding agent can work directly on its game's scene files. One engine saves scenes as human-readable text; another saves its main scene format as binary files that cannot be read as text. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A binary scene file is stored without history in version control, so a bad change to it has to be repaired by hand rather than reverted.
- [ ] B. A binary scene can be reviewed with an ordinary text diff as clearly as a text one, since a diff works on any file.
- [ ] C. Because a text scene is readable, an agent that edits it by hand can tell that the engine will load the edited scene correctly by re-reading the file.
- [ ] D. An agent can judge what a binary image looks like by reading its file bytes as text in a terminal.
- [ ] E. A text scene shows up in a version-control diff line by line, so a reviewer sees which node or property changed.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Version control stores and versions binary files fine, so changes can be reverted; what it cannot do is show a readable line diff of them.
- B: A line-based diff of binary data is not human-readable.
- C: A hand-edited scene can read as well-formed text and still fail to load, for example through a wrong reference or id; the engine is the judge of whether it loads.
- D: Pixel content is not recoverable by reading bytes as characters.
- E: Text formats are what line-based diffs are built for.

**Source:** Text versus binary project files
