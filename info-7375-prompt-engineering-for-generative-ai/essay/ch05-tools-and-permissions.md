# Chapter 5: Tools and permissions

## ES-ch05.1

A tool may read files in a small course folder. Three requests arrive: `notes.txt`, `../notes.txt`, and the name of an entry inside the folder that is actually a symbolic link to somewhere outside it. Explain why the spelling of each request is not a sufficient account of the target the filesystem will use, and say what the policy has to judge instead.

**Points:** 5

**Rubric (1 point each):**

1. Observes that all three requests are strings and that spelling alone is not a sufficient account of the target the filesystem will use.
2. Explains that `../notes.txt` asks to move to the parent before locating the file.
3. Explains that the third entry has a local name but is actually a symbolic link whose destination is outside the folder.
4. States that the policy must judge the place the name leads (the resolved target), not the string that was typed.
5. Reports the fixture outcome: the in-root target is accepted for reading, while the traversal target and the outside-pointing link are rejected.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## ES-ch05.2

The chapter reports that, in disposable directories, an in-root target was accepted for reading while a traversal target, an outside-pointing link, and an unapproved write were rejected. What do those results establish and what do they not establish? State the sentence the chapter calls its center.

**Points:** 5

**Rubric (1 point each):**

1. Names the four fixture outcomes accurately (in-root read accepted; traversal, outside-pointing link, and unapproved write rejected).
2. Says these are actual results of the local preflight function, preserved in the research output.
3. Says the results do not establish that a complete filesystem sandbox was built.
4. States the center sentence: the function returns a path and does not read or write the target.
5. Explains why this matters: a correct implementation can pass every test and still guarantee far less than its name suggests.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## ES-ch05.3

The function is called `authorize`. Describe what it actually does, explain the gap the chapter says is its subject, and name two things the word "authorize" might wrongly suggest.

**Points:** 5

**Rubric (1 point each):**

1. States what the function does: it resolves a name, compares two paths, and hands one back.
2. States that it does not read or write the target (there is no open, read_text, or write_text in the listed code).
3. Identifies the distance between the name and that description as the subject of the chapter.
4. Names at least two things the name might wrongly suggest, such as performing the operation, proving that a person approved it, or being a sandbox.
5. Notes that an implementation can be correct, with every test passing, and still guarantee far less than its name suggests.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## ES-ch05.4

Chapter 1 named three jobs: conduct, check, and drive. Say what each one looks like in this chapter at the smallest scale that still has a real boundary in it, and say who owns the grant.

**Points:** 5

**Rubric (1 point each):**

1. Conduct: the permission policy is a design constraint written before any tool is granted.
2. Conduct: the policy is enforced in the runtime, where a persuasive request cannot reach it.
3. Check: a request can pass every test and still be a bad change; containment is not a shared prefix of characters; the toy boundary guarantees less than it looks.
4. Drive: who may do what is a decision about authority, and Claude can enumerate the edge cases.
5. States that Claude does not own the grant, because it cannot know which folder is yours to expose or who answers for a write.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## ES-ch05.5

Explain how this chapter builds on Chapter 4 and Chapter 1. What did each earlier chapter leave open, and what does this chapter add?

**Points:** 5

**Rubric (1 point each):**

1. States that Chapter 4 bounded how many turns a controller may take.
2. States that a bounded controller can still request the wrong thing once.
3. States that Chapter 1 said a system prompt is a request, not a gate, and promised the gate would be built in code.
4. States that this chapter narrows what any single request may touch.
5. States that it does so with a small decision rule expressed in executable Python so that the cases that pass and fail can be examined.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## ES-ch05.6

The approved root is a folder named course. Answer the chapter's three prediction questions: should course-other pass because its name starts with the same letters; should a write inside course pass merely because the location is acceptable; should an approved execute pass? For each, name the part of the rule that decides.

**Points:** 5

**Rubric (1 point each):**

1. Says course-other should not pass, because containment is not a shared prefix of characters (the containment check decides).
2. Says a write inside course should not pass merely because the location is acceptable, because the write condition is a separate question (the write-approval check decides).
3. Says an approved execute should not pass, because the function allows only read and write (the operation vocabulary decides).
4. States that each answer comes from a different part of the rule.
5. States that keeping those parts separate is how a policy is made inspectable.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## ES-ch05.7

List what the chapter says you should be able to do by its end, including the things the rest of the book builds on.

**Points:** 5

**Rubric (1 point each):**

1. Traces a requested path to the resolved target the function uses, and distinguishes containment from string-prefix similarity.
2. Explains the observed traversal and symlink rejections and why a preflight result is not an operating-system sandbox or a completed file operation.
3. Writes the permission policy, with the wrong versions the tests must catch, before any implementation exists, then conducts Claude Code against it and runs its own tests on what comes back.
4. Writes a sign-off whose "Not checked" line names what a passing preflight leaves open.
5. Says which parts of the boundary were handed to Claude, which were kept, and why the grant itself stayed with the human.

**Source:** What you will be able to do

## ES-ch05.8

The chapter calls its rule for grants least privilege. Explain the rule, where it comes from, and apply it to a tool that summarizes course notes.

**Points:** 5

**Rubric (1 point each):**

1. States the rule: take the lowest capability that does the step, because the most constrained tool is the one you can verify.
2. Says the rule is borrowed from Conducting AI's selection rule for capabilities, and that the book does not state it for permissions (this lesson names the permissions version).
3. Notes that the five-layer capability stack is a teaching device, not an industry standard.
4. Applies it: a notes summarizer needs to read the notes, so a write has to earn its place.
5. Explains that every operation added to the vocabulary is a capability you must later verify, so a policy of one root and two operations can be audited by a stranger while "be careful with files" cannot.

**Source:** Who may do what is decided before the code exists

## ES-ch05.9

Compare two places a permission policy can live: a sentence in the request, and a function between the request and the filesystem. Which does the chapter prefer and why?

**Points:** 5

**Rubric (1 point each):**

1. Identifies the two places: a sentence in the request (for example, stay inside the course folder) and a function that raises when a request is out of bounds.
2. Explains from Chapter 1 that a system prompt is text in a document the model is continuing, competing with every other paragraph in it.
3. Says a request for caution is a hope.
4. Says a function that raises PermissionError does not care how persuasive the request was.
5. Concludes that enforcement lives in the runtime, where text cannot reach it.

**Source:** Who may do what is decided before the code exists

## ES-ch05.10

Moving a decision into code has a benefit and a cost. State both, and say what Claude's role is and is not.

**Points:** 5

**Rubric (1 point each):**

1. States the benefit: the decision becomes checkable.
2. States the cost: the decision becomes exactly as narrow as the question you asked the code.
3. States that the function will enforce the policy you wrote and nothing else.
4. Says Claude proposes actions and a proposal is useful input to review.
5. Says Claude cannot grant itself the permission, and that this separation is the design.

**Source:** Who may do what is decided before the code exists

## ES-ch05.11

What does the chapter's policy judge, and how does the reference implementation compute it? Say what resolve() does and what it does not do.

**Points:** 5

**Rubric (1 point each):**

1. States that the policy judges the place the string leads, not the string typed.
2. Describes the computation: resolve the approved root, join the target to it, resolve the result, and compare the two.
3. States that resolve() resolves symbolic links and eliminates parent components.
4. States that this is the narrow behavior the chapter relies on.
5. States that resolve() does not turn a pathname into a handle on an object.

**Source:** A name is a request for a destination

## ES-ch05.12

Give two examples, one in each direction, showing that the spelling of a request can mislead about its destination. Include the macOS example.

**Points:** 5

**Rubric (1 point each):**

1. States that containment is a statement about the destination, not about which characters look suspicious.
2. Gives the first direction: a request can step into a subdirectory and back to its parent and still land inside the root.
3. Gives the second direction: a request with no visible parent component can lead out of the root through a link.
4. Explains that on macOS /tmp is itself a link to /private/tmp.
5. Says the demo with root /tmp/course and target notes.txt prints /private/tmp/course/notes.txt, because the function reports where the name leads, not how it was spelled.

**Source:** A name is a request for a destination

## ES-ch05.13

The reference calls resolve() without strict checking. Explain what follows from this for what a returned Path shows, and why it matters most for writes.

**Points:** 5

**Rubric (1 point each):**

1. States that resolving does not require the target to exist.
2. States that a returned Path is not evidence that anything was opened.
3. Lists existence, object type, access at the moment of use, and success as separate questions.
4. Explains that a file about to be created does not exist yet, so the preflight can accept a location it cannot inspect.
5. States that acceptance neither creates the file nor shows that its contents are valid.

**Source:** A name is a request for a destination

## ES-ch05.14

One student runs the lesson demo on macOS with root /tmp/course and target notes.txt and sees /private/tmp/course/notes.txt. A second student says the function is broken because the path differs from what was typed. A third says the output proves notes.txt was read. Evaluate both claims.

**Points:** 5

**Rubric (1 point each):**

1. Explains that on macOS /tmp is itself a link to /private/tmp, so the output is expected.
2. Rejects the second claim: the function reports where the name leads, not how it was spelled.
3. Rejects the third claim: resolve() is called without strict checking and the demo reads and writes no file.
4. States that a returned Path is not evidence that anything was opened.
5. Names existence, object type, access at the moment of use, and success as separate questions.

**Source:** A name is a request for a destination

## ES-ch05.15

According to the gate block, what must the function accept and what must it refuse? Give the entries on each list.

**Points:** 5

**Rubric (1 point each):**

1. Names the two acceptances: a contained read, and a contained write with approval.
2. Names two refusals: traversal out of the root, and an absolute path into a sibling that shares the root's name prefix.
3. Names the refusal of an in-root link whose destination is outside.
4. Names two refusals: a contained write without approval, and execute even with approval.
5. Names the refusal of an approval value that is not exactly True.

**Source:** The gate: write the policy before the function

## ES-ch05.16

Who owns each line of the gate, including lines that look arbitrary? Explain what role Claude may play in sharpening the gate and what it may not do.

**Points:** 5

**Rubric (1 point each):**

1. States that every line is the human's, including lines that look arbitrary, such as why exactly True and why execute is refused even with approval.
2. States that Claude may propose a refusal the human missed.
3. States that the human accepts or rejects each proposal and marks an accepted one as Claude's proposal.
4. States that the policy is kept in the human's own words.
5. Explains that Claude cannot write the gate without defeating its purpose, since the gate is where the decision about authority goes on the record and what Claude's implementation is measured against.

**Source:** The gate: write the policy before the function

## ES-ch05.17

Name the four wrong versions of the function that your tests must catch, and say what each replaces.

**Points:** 5

**Rubric (1 point each):**

1. Names containment by string prefix and states it replaces the path relation with str(path).startswith(str(base)).
2. Names textual cleanup of `..` and states it replaces resolve() with os.path.normpath.
3. Names truthy approval and states it replaces `approved is not True` with `not approved`.
4. Names the joined-but-unresolved return value and states it returns base / target instead of path.
5. States that for each variant you should predict whether the six lesson tests will fail it, then run them to see.

**Source:** The gate: write the policy before the function

## ES-ch05.18

Of the four wrong versions, how many does the six-test lesson suite catch? Name which, explain why the rest survive, and list the extra tests the chapter says close the gap.

**Points:** 5

**Rubric (1 point each):**

1. States that exactly one of the four (the string-prefix variant) is caught, by the sibling test, and three survive.
2. Names the survivors: normpath instead of resolve(), truthy approval, and returning base / target instead of the resolved path.
3. Explains that the lesson's success tests check only the final name of the returned path.
4. Explains that none of the tests builds a link and none passes an approval value other than True or absent.
5. Lists the tests that close the gaps: a symlink case, a non-Boolean approval case, and a check that the returned path is the resolved one.

**Source:** The gate: write the policy before the function

## ES-ch05.19

The chapter asks for one dated sentence about what you would see if your function were wrong, written before you run anything. Why? What does a "gate" require of a test list?

**Points:** 5

**Rubric (1 point each):**

1. States the task: write one sentence about what you would see if the function were wrong.
2. States that it must be dated before anything is run.
3. Explains that written afterward, the sentence describes the output instead of testing your understanding.
4. States that a test list that cannot tell the wrong variants from the right program is not a gate yet.
5. States that the gate moves on only when your own tests pass the implementation, run by you.

**Source:** The gate: write the policy before the function

## ES-ch05.20

Walk through the three decisions the reference function makes, in the order it makes them.

**Points:** 5

**Rubric (1 point each):**

1. First decision: the operation vocabulary, where only read and write are allowed.
2. States that execute is refused even with approval true, before the path is resolved at all.
3. States that approval is not a universal override of the allowlist.
4. Second decision: resolve the root, resolve the joined path, and require the result to be relative to the base in the path sense (so a similar-prefix sibling is not a child).
5. Third decision: for a write, `approved is True`, an exact identity comparison.

**Source:** Three decisions in eleven lines

## ES-ch05.21

Why does the reference write `approved is True` and not `if approved`? Say what the check does and does not establish.

**Points:** 5

**Rubric (1 point each):**

1. States that `is True` is an exact identity comparison.
2. States that it asks for the Boolean True and not any arbitrary truthy object.
3. Identifies this as the interface rule written in the gate.
4. States that it does not prove a human reviewed the request that produced the value.
5. Connects to the truthy-approval variant, which would accept values the gate says must be refused.

**Source:** Three decisions in eleven lines

## ES-ch05.22

What does the function return, and why does the chapter warn that the name `authorize` must not inflate what the lines implement? State what the function does and does not do with its inputs.

**Points:** 5

**Rubric (1 point each):**

1. States that the return value is the resolved path.
2. States that there is no open, read_text, or write_text in the lines.
3. States that the function checks a proposed operation under a supplied root and approval value.
4. States that it does not perform the operation.
5. States that it does not authenticate where its inputs came from.

**Source:** Three decisions in eleven lines

## ES-ch05.23

The chapter says "the pattern of the book so far" attaches to a filesystem here. List the earlier examples, state the common move, and say what happens if a caller supplies an overly broad root.

**Points:** 5

**Rubric (1 point each):**

1. States that the probability function did not validate the truth of outcome labels.
2. States that the format validator did not validate source support, and the capability classifier did not authenticate its event list.
3. States that the path check does not authenticate its approval flag.
4. States the common move: find the input the function trusts, and write down what must justify it somewhere else.
5. States that if the caller supplies an overly broad root, the containment check will enforce that broad root faithfully.

**Source:** Three decisions in eleven lines

## ES-ch05.24

Using Conducting AI's idea of a seam, identify the function's two seams and say what you must state about each.

**Points:** 5

**Rubric (1 point each):**

1. Says that in a multi-step workflow the risk sits less inside any one tool than at the seam where one step's output is handed to the next on trust.
2. Says that for each seam you state what is passed, what it is trusted to be, and how that trust was earned.
3. Identifies the incoming seam: the root and the approval value come in.
4. Identifies the outgoing seam: the path goes out.
5. Applies the three questions to at least one seam, for example that the approval value is passed in and trusted to be a decision, but nothing in the function earns that trust.

**Source:** Three decisions in eleven lines

## ES-ch05.25

Two sibling directories, course and course-other, sit under a disposable parent, and the policy allows only course. Explain why a string test fails, and what happens when the target is absolute.

**Points:** 5

**Rubric (1 point each):**

1. States that a target inside course-other must not be accepted under a policy allowing only course.
2. Explains that a string test asking whether the target starts with the text naming course confuses the two directories.
3. States that the reference asks about a relation between resolved paths instead.
4. States that when the second operand of a pathlib join is absolute, the first operand is discarded.
5. Concludes that placing a root before a target expression does not force the target inside it, so the function inspects the combined result.

**Source:** Containment is not a shared prefix

## ES-ch05.26

Trace authorize("/tmp/course", "/tmp/course-other/x", "read") through the reference function, and say what a startswith-based version would do instead.

**Points:** 5

**Rubric (1 point each):**

1. States that "read" is in the vocabulary, so the first decision passes.
2. States that joining an absolute target discards the root, so the combined path is the target itself, which lies under course-other.
3. States that the resolved path is not relative to the resolved base (on macOS the /private/tmp form), so containment fails.
4. States the result: PermissionError (path escapes the data boundary); the write condition does not apply to a read.
5. States that a startswith version would wrongly accept it because the text begins the same way, which is why the sibling test fails that variant.

**Source:** Containment is not a shared prefix

## ES-ch05.27

Describe what to record for a hand trace of one request, and why recording only the original string and the word "denied" is not enough.

**Points:** 5

**Rubric (1 point each):**

1. Says to record the root argument and its resolved base as separate values.
2. Says to record the target argument and the resolved combined path.
3. Says to record whether containment passed.
4. Explains that with only the original string and the word denied, a reviewer cannot see why the boundary fired.
5. Explains that temporary directories get a different name each run, so label them by role (approved root, outside sibling, target, resolved destination); the invariant is the containment relationship, not a random suffix.

**Source:** Containment is not a shared prefix

## ES-ch05.28

Describe the symbolic-link fixture and what its rejection shows about the difference between "the name is inside the folder" and "the resolved target is inside the folder".

**Points:** 5

**Rubric (1 point each):**

1. States that the research script creates a symbolic link inside a temporary root that points outside it.
2. States that the link's name is local but its destination is not.
3. States that when the function resolves the target and tests containment, the request is rejected.
4. States that no read of the outside file is needed to demonstrate this.
5. Explains that a policy written in terms of visible names would miss the link, because a directory listing can show a local entry whose destination is elsewhere.

**Source:** The symlink that leaves the folder

## ES-ch05.29

State precisely what gap remains between the function's check and a later use of the path. Do not overclaim in either direction.

**Points:** 5

**Rubric (1 point each):**

1. States that the function checks and returns, and a later caller may open a file.
2. States that the reference does not bind the check and the operation into one indivisible act.
3. States that the research run does not attempt to prove resistance to changes by another process.
4. States that if the caller uses the returned resolved path, replacing the original link entry need not redirect it, so it would be wrong to claim every swap defeats the function.
5. States the honest gap: it is a preflight pathname check that returns a pathname and establishes nothing about the later access.

**Source:** The symlink that leaves the folder

## ES-ch05.30

A program calls authorize(root, name, "read") early on and, many lines later, calls open(name) with the original unchecked name. Evaluate the claim "the program authorizes its file reads."

**Points:** 5

**Rubric (1 point each):**

1. States that the returned path is the second seam and the failure here needs no race at all.
2. States that a careless caller can check one path and then open the original, unchecked target.
3. States that the teaching function cannot force anyone to use its result.
4. Identifies the laundering shape: something unverified takes on the look of something verified because it passed near a reassuring step.
5. States that a reviewer should follow the value that reaches the open call, not the presence of the word authorize.

**Source:** The symlink that leaves the folder

## ES-ch05.31

Your fixture shows the function rejecting a stable outside-pointing link. What can you honestly report from it, and what can you not claim?

**Points:** 5

**Rubric (1 point each):**

1. States that in a constructed, stable fixture the function rejected an outside-pointing destination, and that is the result you can report.
2. States that the limits locate the result and do not erase it.
3. States that protection against every later mutation is a separate item to document.
4. States that the research run does not attempt to prove resistance to changes by another process.
5. Says not to pretend the test accomplished nothing, and not to present it as proof against every concurrent scenario.

**Source:** The symlink that leaves the folder

## ES-ch05.32

In this policy a contained read needs no approval flag. Explain why that rule is deliberate but is not a blanket statement, and what must already be true of the approved root.

**Points:** 5

**Rubric (1 point each):**

1. States that an in-root read passes without a separate approval flag as a deliberate rule for the exercise.
2. States that this is not a statement that every file under any root is appropriate to read, upload, or disclose.
3. Explains that a read changes nothing in the filesystem but what it exposes cannot be un-exposed once it has left the folder.
4. States that the approved root must already reflect the task's data boundary, and that if it holds material the workflow should not touch, the policy is wrong however correct the code.
5. Mentions the delegation chapter's question about whether an action can be undone, and that its five-question score is the author's own instrument with no external validation, so it is used as a question and not as a number.

**Source:** Read and write are different authority questions

## ES-ch05.33

The same in-root target `report.txt` is proposed once for reading and once for writing, with no approval supplied either time. What does the function do in each case? Then explain why the outcome is not inconsistent and what a "True" in a later test would and would not show.

**Points:** 5

**Rubric (1 point each):**

1. States that the read returns a path.
2. States that the write raises PermissionError.
3. Explains that containment and write approval are separate questions, and passing containment cannot substitute for the second.
4. States that the same target can be accepted for reading and rejected for writing without inconsistency.
5. Explains that an accepted write proposal with True is an authorization result, not execution, and the fixture True is a simulated approval input, not a person's consent.

**Source:** Read and write are different authority questions

## ES-ch05.34

What does the approval flag represent in this model, and what does it not represent? How should you label a True in a test fixture, and who must supply the real decision?

**Points:** 5

**Rubric (1 point each):**

1. States that the flag is a decision supplied from outside the function.
2. States that it is not a user interface, a signature, an identity check, or a record that someone saw the precise change.
3. States that a True in a fixture should be labeled a simulated approval input and not attributed to a person.
4. States that a model can propose an action and explain why, but does not get to produce its own independent human approval by writing the word approved.
5. States that the source of the approval value matters as much as its type.

**Source:** Read and write are different authority questions

## ES-ch05.35

Explain the standard the chapter applies to handoff conditions, why a Boolean fails it, and what a richer approval record would contain. What problem does the richer record still leave open?

**Points:** 5

**Rubric (1 point each):**

1. States the standard: a handoff condition is worth having only if a stranger can read it, observe the system, and decide whether it was met.
2. Explains that a Boolean fails the way "the human reviews it" does: a reader sees the value but cannot tell whether anyone decided anything.
3. States that the richer condition names the operation, the target, and the approver.
4. States that it was issued before the call and its target matches the request.
5. States that even then it only moves the unsolved problem, because nothing here authenticates the record's contents.

**Source:** Read and write are different authority questions

## ES-ch05.36

A person approved writing a disposable draft. The program then overwrites the original file and writes several other files in the same directory, citing that approval. Evaluate.

**Points:** 5

**Rubric (1 point each):**

1. States that approval for a disposable draft is not approval to overwrite an original.
2. States that approval for one target is not a license over a directory.
3. States that the surrounding process must bind its decision to the actual operation and target.
4. States that the source of the approval value matters as much as its type.
5. States that approvals should be rare, specific, and tied to the actual change.

**Source:** Read and write are different authority questions

## ES-ch05.37

Is a human in the loop automatically a control? Use the companion chapter's argument and the chapter's own extension of it to grants, and say how to design approvals.

**Points:** 5

**Rubric (1 point each):**

1. States that a human in the loop is not automatically a control.
2. States that when checking is expensive, the cost structure pushes a supervisor toward accepting.
3. States that the companion chapter calls this economics acting on attention, not a character flaw.
4. States that extending it to grants is the chapter author's reading and not the book's claim.
5. States that if approval is requested for every small step the answer can drift toward yes, so approvals should be rare, specific, and tied to the actual change.

**Source:** Read and write are different authority questions

## ES-ch05.38

For each of the six proposals in the boundary matrix, state the result and what it establishes.

**Points:** 5

**Rubric (1 point each):**

1. Contained read: a path is returned; the proposal passes the displayed preflight (not that the target exists or was read).
2. Escaping traversal and outside-pointing link: PermissionError because the resolved target or destination fails containment.
3. Contained write with no approval: PermissionError, showing containment does not waive write approval.
4. Contained write with a True fixture: a path is returned; a simulated approval input satisfies this check.
5. Execute: PermissionError; approval cannot override the operation allowlist, and it fails first without resolving any path.

**Source:** Work through the boundary matrix

## ES-ch05.39

Is the boundary matrix a security certification? State what it is, which sources exercise which rows, and what a reader should do with it.

**Points:** 5

**Rubric (1 point each):**

1. States that the matrix is not a security certification.
2. States that it maps implemented conditions to observed or directly tested results.
3. States that another reader can use it to locate the relevant branch and decide what question their application still has to answer.
4. States that the research fixture exercises an in-root read, traversal, an outside-pointing symlink, and a write without approval.
5. States that the lesson tests add the Boolean-approved write and the rejection of execute.

**Source:** Work through the boundary matrix

## ES-ch05.40

A student's version of authorize accepts the sibling-prefix case and also accepts an unapproved contained write. Diagnose each defect and say how the student should have reasoned about the tests beforehand.

**Points:** 5

**Rubric (1 point each):**

1. Says that the sibling-prefix case passing suggests a string test was used where a path relation was needed.
2. Says the fix is to compare resolved paths by a path relation (such as is_relative_to).
3. Says that an unapproved write passing suggests the write condition is not independent of containment.
4. Says the student should have predicted not just accept or reject but which rule produces each result.
5. Says the student should have read the six lesson tests before the reference and treated their own version as the baseline.

**Source:** Build It: make denials explainable

## ES-ch05.41

Give the chapter's advice on designing a test suite for the boundary, including why a denial-only suite is not enough.

**Points:** 5

**Rubric (1 point each):**

1. States that each test should be narrow enough to explain.
2. Explains that a proposal combining an unknown operation, an escaping path, and missing approval does not say which boundary you meant to test.
3. States that to test a later check, the earlier ones should pass.
4. Explains that a policy that rejects everything passes a denial-only suite and fails the authorized task, so a meaningful success outside the demo must be added.
5. States that fixtures should be disposable, outside the allowed root need not mean a real personal or system file, and cleanup goes through the temporary-directory lifecycle, not broad deletion commands.

**Source:** Build It: make denials explainable

## ES-ch05.42

What do you hand to Claude Code at this stage, what do you ask for, and why is Claude's statement that the tests passed not evidence?

**Points:** 5

**Rubric (1 point each):**

1. States that you give Claude Code your policy block and your test list, not your implementation.
2. States that you ask for an implementation of authorize(root, target, operation, approved=False) that uses only the standard library and satisfies the policy.
3. States that you work in your learner workspace on disposable fixtures.
4. States that you run your tests yourself.
5. States that a statement from Claude that they passed is Claude's report, not your evidence.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch05.43

Claude returns an implementation. Describe the three things the chapter says to do with it.

**Points:** 5

**Rubric (1 point each):**

1. First: note which of your tests failed, if any, and decide whether the gate or the code is wrong and write down which.
2. Explains that a failing test is often a gap in the gate, which Claude cannot see because it has only what you wrote.
3. Second: compare its function with your baseline and name one difference in behavior, not in line count or style.
4. Explains that the difference may be a boundary you missed (revising the gate) or a case your tests never covered (a defect your tests failed to catch).
5. Third: apply the variants from your gate to its function one at a time, and treat every variant that survives your tests as a gap in the test list.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch05.44

Why are tests that Claude writes for its own function weaker evidence than your tests written first? Use the chapter's argument about independence.

**Points:** 5

**Rubric (1 point each):**

1. States that tests Claude writes for the function Claude wrote share its reading of your policy.
2. States that a second checker reduces error only to the degree that it fails differently from the first.
3. States that a checker that fails the same way adds agreement, not verification.
4. States that your tests, written first, and the variants you built by hand fail differently from its implementation.
5. Says to treat each case Claude adds as a proposal (read it, run it, decide) and to narrow a generated assurance of security to the conditions the tests demonstrate.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch05.45

The lesson asks you to compare your toy with a real permission boundary. Describe how to do this safely and honestly, and what you must record.

**Points:** 5

**Rubric (1 point each):**

1. States that the comparison is read-only: inspecting the permission configuration is not authorization to change university settings or disable protections.
2. States that Anthropic's Claude Code permissions documentation describes runtime permission rules, and the useful point is that executable rules mediate actions rather than prompt prose.
3. States that the function models only a small path-and-operation preflight and does not reproduce the product's permission system, and that the Boolean must not substitute for a current product policy.
4. States that if configuration access is unavailable, that part is marked not inspected, with no guessed rules, invented screenshot, or protection reported as enabled from memory.
5. States that the transcript is preserved (prompt, plan, diff, commands, outputs, date, displayed model label), and a failed or missing session is recorded as such rather than replaced by a fixture.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch05.46

Name the four events the chapter says are not interchangeable even when they occur in one workflow, and explain why you would not add a write to a task that does not need one.

**Points:** 5

**Rubric (1 point each):**

1. Names passing preflight as one event.
2. Names receiving runtime permission as one event.
3. Names performing the operation and reviewing the diff as the other two.
4. States that occurring in one workflow does not make them interchangeable.
5. States that if no write is needed, you should not add one for effect.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch05.47

Name and briefly describe the five things a passing preflight leaves open.

**Points:** 5

**Rubric (1 point each):**

1. Coverage: the function protects nothing that bypasses it.
2. Authentication: the function has no independent account of who supplied the root or the approval value.
3. Time and filesystem state: the check is not made atomic with a later open and does not freeze the path components.
4. Meaning: an approved write can contain a bad change, and the function does not inspect a diff.
5. Data policy beyond location: a contained file may hold restricted information that a later step discloses, and the preflight has no destination-channel policy, retention schedule, or content classification.

**Source:** What the toy boundary cannot guarantee

## ES-ch05.48

Explain the authentication limit and the time-and-state limit, and say what you must not claim about each.

**Points:** 5

**Rubric (1 point each):**

1. States that the function has no independent account of who supplied the root or the approval value.
2. States that a True fixture satisfies the Boolean check and proves nothing about consent.
3. States that a trustworthy workflow needs a real source for the decision and a scope corresponding to the proposed action, and that this lesson implements neither.
4. States that the path is checked before use and the function does not make a later open atomic with the check or freeze the path components.
5. States that rejecting one stable outside-pointing link does not prove resistance to every concurrent scenario, and that you must not claim a race exploit was executed unless you performed and recorded a safe test.

**Source:** What the toy boundary cannot guarantee

## ES-ch05.49

Explain the meaning limit and the data-policy limit, and how each relates to what a root is.

**Points:** 5

**Rubric (1 point each):**

1. States that an approved write can contain a bad change.
2. States that the function does not inspect a diff, run a program, or judge whether the output serves the user's purpose.
3. States that permission answers whether the proposal satisfies a boundary and review answers whether the proposed content is acceptable.
4. States that a contained file may hold restricted information and a later step may disclose it somewhere inappropriate.
5. States that a root is one useful boundary, not a description of every data obligation, since the preflight has no destination-channel policy, retention schedule, or content classification.

**Source:** What the toy boundary cannot guarantee

## ES-ch05.50

Claude can produce a fluent list of limitations in seconds. Explain how the chapter wants you to write the "Not checked" line so that it is more than a fluent list, and what attitude the limits should not produce.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the question that writes the line: what does a passing preflight leave open?
2. States that a fluent list of limitations is as easy for Claude to produce as a fluent claim of security.
3. States that each limit should be tied to what you actually did about it: inspected, tested, or left alone.
4. States that none of this is a reason for vague helplessness, because the function has a well-defined educational job that the fixture shows it doing.
5. States that precision lets protections accumulate without one small protection impersonating the whole system.

**Source:** What the toy boundary cannot guarantee

## ES-ch05.51

What must the shipped artifact contain, and what must it record for each proposal?

**Points:** 5

**Rubric (1 point each):**

1. States that the artifact is the gate, as run.
2. Lists the approved root, allowed operations, approval owner or simulated approval source, denial cases, and actual test results.
3. States that for each proposal it preserves the requested target and the role its resolved destination played, and records whether the function returned or raised and which branch decided.
4. States that it includes one decision the student revised after testing, with the original prediction and the result that changed it.
5. States that if a later file operation was not performed, the artifact says so, and a preflight-only experiment is complete on its own terms if its stated task was to test preflight behavior.

**Source:** Ship It: a permission policy with evidence

## ES-ch05.52

Your capstone saves a draft under an approved directory. Say how the artifact should connect a denial to the capstone, how approvals must be recorded, and what you may not claim.

**Points:** 5

**Rubric (1 point each):**

1. States that the artifact should include at least one denial that matters to the capstone, connected narrowly.
2. Says the write-approval and target checks are relevant to saving a draft under an approved directory.
3. Says they do not show that the draft is correct or the capstone secure, and that the supported claim and the next check it needs should be named.
4. States that each approval value's source is recorded: "simulated fixture" for tests, or the relevant real authorization without exposing private information for an actual action.
5. States that a Boolean in a script must never become a claim that a named person approved something, because the evidence record must not invent the human act it is supposed to document.

**Source:** Ship It: a permission policy with evidence

## ES-ch05.53

Write or describe the sign-off for your permission policy and preflight function. Which line will Claude not write honestly, and when is withholding the right result?

**Points:** 5

**Rubric (1 point each):**

1. Checked: names the refusals and acceptances tested (traversal, sibling prefix, outside-pointing link, unapproved write, execute with approval, non-Boolean approval).
2. How: says whether through tests written before reading the reference, hand traces, or with Claude's help (saying which cases it proposed and which were kept).
3. Not checked: includes changes between check and use, whether any caller uses the returned path, who supplied any approval value, and the content of any write.
4. Not claiming: that this is a sandbox, that anyone approved anything (every approval in the tests is a simulated fixture), and that a returned path means a file was read or written.
5. Says the line about what you did not test is the one Claude will not write honestly, and that if the evidence does not support signing, withholding is an honest result.

**Source:** Ship It: a permission policy with evidence

## ES-ch05.54

Describe how the chapter divides each of five tasks between Claude and the human, and give the reason each stays with the human.

**Points:** 5

**Rubric (1 point each):**

1. Root and operation vocabulary: Claude lists what the task might touch; the human decides the smallest root and vocabulary, because only the human knows what is in the folder and what disclosure would cost.
2. Approver: Claude drafts candidate approval records and says what each cannot prove; the human names the approver and scope and makes the grant, because Claude cannot approve its own request.
3. Edge cases: Claude proposes cases such as links, absolute targets, siblings, unknown operations, and non-Boolean approval; the human writes the first list and chooses which become tests.
4. Implementation: Claude writes it fast; the human runs the tests and compares with the baseline, because you cannot audit a boundary you never built or broke.
5. What a pass establishes: Claude flags an overclaim; the human chooses the verb and signs or withholds, because the human's name is on the claim.

**Source:** The driver's seat

## ES-ch05.55

A student's artifact says "I delegated the implementation and kept the judgment" but points to no transcript line, diff, or edit. Evaluate the claim using the chapter's standard.

**Points:** 5

**Rubric (1 point each):**

1. States that the artifact must record one task delegated and one judgment retained.
2. States that each must point to a transcript line, a diff, or an edit the student made.
3. Concludes that without those pointers the split happened in the student's head and not in the record.
4. Notes that authority and accountability are a person's, so retained judgments such as naming the approver should be traceable.
5. Notes that a delegated implementation should be traceable to the student's own tests run on what Claude returned and a comparison with the student's baseline.

**Source:** The driver's seat

## ES-ch05.56

The chapter asks you to audit the artifact's nouns and verbs. Explain this audit with three examples and the integration question it adds.

**Points:** 5

**Rubric (1 point each):**

1. Asks whether authorize means a preflight decision or a complete approval system.
2. Asks whether read means permission to read or a completed read.
3. Asks whether safe means contained under this root or secure against every attack.
4. Says to replace each ambiguous word with the event and condition that occurred.
5. States the integration question: if another function receives the returned Path, it must still use the checked target consistently, handle real operation failures, and keep the review boundaries in place.

**Source:** Verify and reflect

## ES-ch05.57

Name the four distinctions the closing reflection says you may have collapsed, and explain what the chapter means by calling the most useful reflection local.

**Points:** 5

**Rubric (1 point each):**

1. Names the spelling of a path versus its destination.
2. Names a location versus an authority.
3. Names a preflight versus a performed operation.
4. Names a Boolean versus a human act.
5. Says the reflection asks you to name the distinction you originally collapsed and the specific case that separated them again.

**Source:** Verify and reflect

## ES-ch05.58

Challenge item 11 asks for a richer approval record. Describe what the record should contain, how a caller should use it, the test you should add, and what remains unsolved.

**Points:** 5

**Rubric (1 point each):**

1. States that the record names the operation and target, not only a Boolean.
2. States that its handoff condition is written so a stranger could decide from the record alone whether it was met.
3. States that the caller checks correspondence between the record and the actual request.
4. States that a mismatched-target test is added, with simulated approvals labeled as such.
5. States that the identity problem remains unsolved, because adding fields does not authenticate their contents.

**Source:** Assessments - ungraded practice

## ES-ch05.59

Using the chapter's closing summary, explain how operation, location, and write approval are independent of one another, and what a returned Path and a True fixture do not mean.

**Points:** 5

**Rubric (1 point each):**

1. Gives an example that an allowed operation can target an outside location.
2. Gives an example that a contained target can fail the write condition.
3. Gives an example that a True approval cannot override an operation outside the allowlist.
4. States that a returned Path is not a completed file operation.
5. States that a Boolean approval fixture is not a human act, and that this precision protects the evidence trail from describing a preflight result as though a person approved and a tool executed the proposal.

**Source:** What you can now defend

## ES-ch05.60

Suppose a write passes every check in this chapter and is performed under a real, appropriately scoped approval. What has still not been asked, why can't the permission boundary ask it, and what does Chapter 6 do next?

**Points:** 5

**Rubric (1 point each):**

1. States that whether the new contents are any good has still not been asked.
2. States that the permission boundary should not be asked because it never inspects the diff.
3. States that Chapter 6 turns to evidence-based review of a change, comparing an incorrect implementation, an inadequate patch, and a correct patch on constructed inputs.
4. States that the review keeps apart a proposed edit, tests actually run, and a human decision about acceptability.
5. States that permission without quality review can authorize a mistake while quality without permission can produce an excellent change to the wrong thing.

**Source:** An authorized change can still be a bad change

## ES-ch05.61

How does the chapter connect its operation allowlist to Claude Code permissions, and how should the comparison be carried out?

**Points:** 5

**Rubric (1 point each):**

1. States that the Python allowlist is compared with Claude Code permissions as documented (checked for the research packet on 2026-09-06).
2. States that the connection is runtime enforcement: requesting caution in prose is not the same as constraining tool actions through permission rules.
3. States that the teaching function is only a preflight illustration, not a reproduction of the product's safeguards.
4. States that you inspect the configuration available in your course environment without changing institutional settings, and document one enforceable boundary and one question the path function cannot answer.
5. States that unavailable information is marked uninspected, and the comparison should sharpen the policy and not encourage bypassing a boundary to make a demonstration more dramatic.

**Source:** Anthropics
