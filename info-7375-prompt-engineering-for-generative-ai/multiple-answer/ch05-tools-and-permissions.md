# Chapter 5: Tools and permissions

## MA-ch05.1

Check each statement that is true about the three requests described at the start of the chapter (notes.txt, ../notes.txt, and a symbolic-link entry inside the folder). Each statement is worth 1 point (5 points total).

- [ ] A. The fixture results establish that the authors built a complete filesystem sandbox.
- [ ] B. All three requests are strings, and their spelling alone is not a sufficient account of the target the filesystem will use.
- [ ] C. In the research fixture, an in-root target is accepted for reading, while a traversal target, an outside-pointing link, and an unapproved write are rejected.
- [ ] D. The request for ../notes.txt asks to move to the parent before locating the file.
- [ ] E. The symbolic-link entry is safe because its name is inside the folder.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The chapter says they do not; the function returns a path and neither reads nor writes.
- B: Spelling does not settle where the name leads.
- C: These are the preserved fixture results.
- D: The parent component moves outward before the file is located.
- E: A link's name is local, but its destination can be outside the folder.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## MA-ch05.2

Check each statement that is true about what the function `authorize` does and does not do. Each statement is worth 1 point (5 points total).

- [ ] A. A correct implementation whose tests all pass can still ship a policy that guarantees far less than its name suggests.
- [ ] B. Because the function is called authorize, a returned path shows that the file was written.
- [ ] C. It reads the target file and returns the contents.
- [ ] D. The chapter treats the name and the behavior as the same description.
- [ ] E. It resolves a name, compares two paths, and hands one back.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: This is where a recipe-follower goes wrong.
- B: An authorization result is not execution.
- C: It returns a path; it does not read or write the target.
- D: The distance between the two descriptions is the subject of the chapter.
- E: That is the chapter's description of what it does.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## MA-ch05.3

Check each statement that is true about the prediction questions posed in the opening of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. All three prediction answers come from the same single check in the rule.
- [ ] B. An approved execute operation should pass, because approval overrides the allowlist.
- [ ] C. A folder named course-other should not pass merely because its name begins with the same letters as the approved root course.
- [ ] D. A write inside course should pass merely because the location is acceptable.
- [ ] E. Keeping the parts of the rule separate is how a policy is made inspectable.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Each answer comes from a different part of the rule.
- B: The function allows only read and write; approval is not an override.
- C: Containment is not a shared prefix of characters.
- D: Location and write approval are separate questions.
- E: Separate parts can each be inspected and tested.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## MA-ch05.4

Check each statement that is true about how the chapter says to run its exercises. Each statement is worth 1 point (5 points total).

- [ ] A. Exercises use disposable material under a narrowly scoped temporary directory.
- [ ] B. The Python boundary requires a direct call to the Claude API.
- [ ] C. The scenarios are teaching fixtures, not invitations to probe someone else's files.
- [ ] D. Claude Code is replaced by the API as the assumed learning assistant for this exercise.
- [ ] E. You may disable a safeguard temporarily if that helps you complete the exercise.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Disposable temporary directories avoid touching real data.
- B: The boundary requires no direct API call.
- C: The exercises target only disposable material.
- D: Claude Code remains the assumed learning assistant through your account.
- E: The chapter says not to change institutional permissions or disable safeguards.

**Source:** Chapter 5 - Tools and permissions (opening, before the first heading)

## MA-ch05.5

Check each statement that is true about the abilities the chapter says you should have by its end. Each statement is worth 1 point (5 points total).

- [ ] A. Distinguish containment from string-prefix similarity.
- [ ] B. Write a sign-off whose "Not checked" line names what a passing preflight leaves open.
- [ ] C. Say which parts of the boundary you handed to Claude, which you kept, and why the grant itself stayed yours.
- [ ] D. Explain that a passing preflight result is an operating-system sandbox.
- [ ] E. Trace a requested path to the resolved target that the function uses.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Containment is a path relation, not a character prefix.
- B: One of the three things the rest of the book builds on.
- C: One of the three things the rest of the book builds on.
- D: You should be able to say why it is not one.
- E: Tracing the destination is the first listed ability.

**Source:** What you will be able to do

## MA-ch05.6

Check each statement that is true about least privilege and the first design decision. Each statement is worth 1 point (5 points total).

- [ ] A. The selection rule is to take the lowest capability that does the step, because the most constrained tool is the one you can verify.
- [ ] B. A tool that summarizes course notes needs, at minimum, to read them.
- [ ] C. The five-layer capability stack is a teaching device, not an industry standard.
- [ ] D. You answer the first decision by asking what the task requires, not what the tool is able to do.
- [ ] E. Conducting AI states least privilege for permissions in those words.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: This is the rule the chapter borrows.
- B: A notes summarizer is the chapter's example of a tool that needs only to read.
- C: The book itself says so, according to the chapter.
- D: Least privilege starts from what the task needs.
- E: The book does not state it for permissions; this lesson names the permissions version least privilege.

**Source:** Who may do what is decided before the code exists

## MA-ch05.7

Check each statement that is true about auditing a permission policy. Each statement is worth 1 point (5 points total).

- [ ] A. A write belongs in the default vocabulary and needs no justification.
- [ ] B. Every operation added to the vocabulary is a capability you must later verify.
- [ ] C. The first design decision is a line of Python.
- [ ] D. A policy that says "be careful with files" can be audited by a stranger.
- [ ] E. A policy of one root and two operations can be audited by a stranger in a few minutes.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A write has to earn its place.
- B: Each added operation is one more capability to verify.
- C: The first decision is what the tool may touch and what it may do.
- D: It cannot be audited by anyone.
- E: The chapter's example of an auditable policy.

**Source:** Who may do what is decided before the code exists

## MA-ch05.8

Check each statement that is true about where a permission policy can be placed. Each statement is worth 1 point (5 points total).

- [ ] A. A system prompt sits outside the text the model is continuing, so no other paragraph competes with it.
- [ ] B. Enforcement lives in the runtime, where text cannot reach it.
- [ ] C. One place for a policy is a sentence in the request; another is a function between the request and the filesystem that raises when the request is out of bounds.
- [ ] D. A sentence such as "stay inside the course folder" is a gate.
- [ ] E. A function that raises PermissionError is more likely to let a request through when the request is persuasive.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A system prompt is text in a document the model is continuing, competing with every other paragraph.
- B: A runtime check cannot be talked out of its answer by text.
- C: These are the two places the chapter names.
- D: A request for caution is a hope.
- E: It does not care how persuasive the request was.

**Source:** Who may do what is decided before the code exists

## MA-ch05.9

Check each statement that is true about deterministic work and Claude's role in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A request for caution in the prompt is an adequate substitute for a comparison that has one correct answer.
- [ ] B. Whether a resolved path lies under a folder has one correct answer.
- [ ] C. This is the same move as the book's advice to route deterministic work out of the stochastic layers.
- [ ] D. Handing that question to a model borrows fluent guessing for a job a comparison does exactly.
- [ ] E. Claude keeps a role: it proposes actions, and a proposal is useful input to review.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A request for caution is a hope; a comparison does the job exactly.
- B: So it is not a matter for plausibility.
- C: Routing deterministic work out of the stochastic layers is the same move.
- D: A comparison has one right answer; a model only approximates it.
- E: Proposing is Claude's role; granting is not.

**Source:** Who may do what is decided before the code exists

## MA-ch05.10

Check each statement that is true about moving a decision into code. Each statement is worth 1 point (5 points total).

- [ ] A. Moving a decision into code makes it exactly as narrow as the question you asked the code.
- [ ] B. Separating Claude's proposal from the grant has no cost.
- [ ] C. The function will also enforce rules you meant to write but did not.
- [ ] D. Moving a decision into code makes it checkable.
- [ ] E. Claude cannot grant itself the permission; that separation is the design.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: This is the cost the chapter measures.
- B: The separation comes with a cost, which the rest of the chapter measures.
- C: It will enforce the policy you wrote and nothing else.
- D: A rule in code can be tested; a sentence in a request cannot.
- E: Claude can only propose; the grant stays with a person.

**Source:** Who may do what is decided before the code exists

## MA-ch05.11

Check each statement that is true about how the reference implementation treats a path. Each statement is worth 1 point (5 points total).

- [ ] A. The reference resolves the approved root, joins the target to it, resolves the result, and compares the two.
- [ ] B. resolve() turns a pathname into a handle on an object.
- [ ] C. Python's resolve() resolves symbolic links and eliminates parent components.
- [ ] D. This policy judges the place the string leads, not the string someone typed.
- [ ] E. A relative path means the same thing regardless of the base from which it is read.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: These are the four steps of the reference's path check.
- B: resolve() returns a path, not a handle on an object.
- C: This is the narrow behavior the chapter relies on.
- D: The destination, not the spelling, is what is judged.
- E: A relative path depends on the base.

**Source:** A name is a request for a destination

## MA-ch05.12

Check each statement that is true about why spelling is not the same as destination. Each statement is worth 1 point (5 points total).

- [ ] A. A request can step into a subdirectory and back to its parent and still land inside the root.
- [ ] B. Containment is a statement about which characters in a request look suspicious.
- [ ] C. Parent components in a path can move outward from the directory it is read from.
- [ ] D. A request with no visible parent component cannot lead out of the root.
- [ ] E. A symbolic link can only redirect a name to another entry inside the same root.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Containment is about the destination.
- B: It is a statement about the destination.
- C: That is what a .. component does.
- D: A link can lead out without any parent component.
- E: A link can redirect a name toward another location, including one outside the root.

**Source:** A name is a request for a destination

## MA-ch05.13

Check each statement that is true about resolving a path that may not exist. Each statement is worth 1 point (5 points total).

- [ ] A. The reference calls resolve() with strict checking, so a target that does not exist is rejected.
- [ ] B. A returned Path is evidence that something was opened.
- [ ] C. Acceptance of a write creates the file and shows that its contents are valid.
- [ ] D. For a write, the preflight can accept a location it cannot inspect, because the file about to be created does not exist yet.
- [ ] E. Whether the target exists is the same question as whether the operation succeeded.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It calls resolve() without strict checking.
- B: A returned Path does not show that anything was opened.
- C: Acceptance neither creates the file nor validates its contents.
- D: A file about to be created cannot be inspected yet.
- E: Existence, object type, access at the moment of use, and success are separate questions.

**Source:** A name is a request for a destination

## MA-ch05.14

A student runs the lesson's demo on macOS with root /tmp/course and target notes.txt, and it prints /private/tmp/course/notes.txt. Check each statement that is true about this output. Each statement is worth 1 point (5 points total).

- [ ] A. The function reports where the name leads, not how it was spelled.
- [ ] B. The printed path proves that notes.txt exists and was read.
- [ ] C. On macOS /tmp is a link to /private/tmp, so a resolved path starts with /private/tmp.
- [ ] D. The root was never resolved, because the printed path differs from the typed root.
- [ ] E. The differing spelling shows the function failed or was bypassed.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Resolution replaces the spelling with the destination.
- B: The demo says no file is read or written.
- C: The resolved path starts from the real location.
- D: The function resolves the root first; that is why the printed path differs.
- E: The printed path is where the name leads, which is the intended output.

**Source:** A name is a request for a destination

## MA-ch05.15

Check each statement that is true about what the chapter's gate block fixes in advance. Each statement is worth 1 point (5 points total).

- [ ] A. The gate says execute should be accepted when approval is present.
- [ ] B. The gate lets you claim a file was read or written once a proposal passes the preflight.
- [ ] C. A write needs a human approval you can name; in tests it is a simulated fixture, labeled as one.
- [ ] D. Root: one disposable directory, named in the gate.
- [ ] E. Operations: read and write, and no other operation.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Execute is refused even with approval.
- B: You may claim only that a proposal passes a preflight.
- C: Tests use a labeled, simulated approval.
- D: The gate names the one disposable directory first.
- E: The gate allows no operation beyond read and write.

**Source:** The gate: write the policy before the function

## MA-ch05.16

Check each statement that is true about what the gate says the function must accept. Each statement is worth 1 point (5 points total).

- [ ] A. A contained read must be accepted.
- [ ] B. Execute must be accepted when approval is present.
- [ ] C. Traversal out of the root must be accepted if the operation is a read.
- [ ] D. An approval value that is truthy but not exactly True must be accepted for a write.
- [ ] E. A contained write without approval must be accepted, since the location is acceptable.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Contained reads are on the must-accept list.
- B: Execute is refused even with approval.
- C: Traversal is listed under Must refuse.
- D: Only exactly True passes; anything else is refused.
- E: It is listed under Must refuse.

**Source:** The gate: write the policy before the function

## MA-ch05.17

Check each statement that is true about who owns the gate. Each statement is worth 1 point (5 points total).

- [ ] A. A refusal you accept from Claude should be marked as Claude's proposal.
- [ ] B. Claude is not permitted to propose a refusal you missed.
- [ ] C. The finished policy should be kept in Claude's words.
- [ ] D. Every line of the gate is yours, including lines that look arbitrary, such as why exactly True and why execute is refused even with approval.
- [ ] E. Claude can write the whole gate for you without defeating its purpose.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Marking provenance keeps the policy honest about who proposed what.
- B: Claude may propose one; you accept or reject it.
- C: It should be kept in your words.
- D: The gate records the human's decisions, even arbitrary-looking ones.
- E: It cannot write it for you without defeating its purpose.

**Source:** The gate: write the policy before the function

## MA-ch05.18

Check each statement that is true about the four wrong versions your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. Returning base / target instead of the resolved path is one of them.
- [ ] B. Every one of the four variants fails at least one of the six lesson tests.
- [ ] C. Containment by string prefix, using str(path).startswith(str(base)), is one of them.
- [ ] D. Truthy approval, replacing approved is not True with not approved, is one of them.
- [ ] E. Textual cleanup of .. with os.path.normpath instead of resolve() is one of them.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Returning the unresolved join hands the caller an unchecked path.
- B: Only the prefix variant fails; the other three pass all six.
- C: Prefix testing is the first listed wrong version.
- D: not approved accepts any truthy value, not only True.
- E: normpath cleans text but never follows links.

**Source:** The gate: write the policy before the function

## MA-ch05.19

Check each statement that is true about how the six lesson tests handle the four wrong versions. Each statement is worth 1 point (5 points total).

- [ ] A. The other three variants pass all six lesson tests.
- [ ] B. One of the six lesson tests passes an approval value that is neither True nor absent.
- [ ] C. The lesson's success tests compare the full resolved path.
- [ ] D. The sibling test fails the string-prefix variant.
- [ ] E. At least one of the six lesson tests builds a symbolic link.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Only the prefix variant is caught by any of the six tests.
- B: No lesson test passes a non-Boolean approval value.
- C: They check only the final name of the returned path.
- D: A sibling like course-other starts with the same characters as course.
- E: No lesson test creates a link.

**Source:** The gate: write the policy before the function

## MA-ch05.20

Check each statement that is true about extending the test list and the dated sentence. Each statement is worth 1 point (5 points total).

- [ ] A. A test list that cannot tell the wrong variants from the right program is not a gate yet.
- [ ] B. Writing that sentence after running the code is better, because it records the real output.
- [ ] C. The six lesson tests are enough to serve as the whole test list.
- [ ] D. You should write one sentence about what you would see if your function were wrong, and date it before you run anything.
- [ ] E. Added tests the chapter names include a symlink case, a non-Boolean approval case, and a check that the returned path is the resolved one.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: A gate that cannot reject the wrong programs proves nothing.
- B: Written afterward, it describes the output instead of testing your understanding.
- C: The gaps are why the list is longer than six.
- D: A prediction written beforehand tests understanding.
- E: These cover the gaps the six lesson tests leave.

**Source:** The gate: write the policy before the function

## MA-ch05.21

Check each statement that is true about the three decisions the reference function makes. Each statement is worth 1 point (5 points total).

- [ ] A. The first decision the function makes is the operation vocabulary.
- [ ] B. Execute is refused even with approval true, before the path is resolved at all.
- [ ] C. The second decision resolves the root and the joined path and requires the result to be relative to the base in the path sense.
- [ ] D. Approval is a universal override of the operation allowlist.
- [ ] E. The third decision concerns writes and compares the approval value with True.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Decisions are read in order of the function.
- B: The allowlist check comes first and needs no path.
- C: Containment is a relation between resolved paths.
- D: Approval does not override the operation allowlist.
- E: Only the write branch consults the approval value.

**Source:** Three decisions in eleven lines

## MA-ch05.22

Check each statement that is true about the write condition approved is True. Each statement is worth 1 point (5 points total).

- [ ] A. A passing approval check shows the approval was issued before the call and matches the request.
- [ ] B. A passing approval check shows that a human reviewed the request that produced the value.
- [ ] C. It asks for any arbitrary truthy object, not specifically the Boolean True.
- [ ] D. The approved is True check is applied to reads as well as to writes.
- [ ] E. It is an exact identity comparison.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: A Boolean carries neither fact.
- B: It does not prove a human reviewed anything.
- C: It asks for the Boolean True and not any arbitrary truthy object.
- D: It applies only when the operation is write.
- E: "is" tests identity, so only the object True matches.

**Source:** Three decisions in eleven lines

## MA-ch05.23

Check each statement that is true about the return value and what the function claims. Each statement is worth 1 point (5 points total).

- [ ] A. The function authenticates where the root and approval inputs came from.
- [ ] B. There is no open, read_text, or write_text in the listed code.
- [ ] C. The function performs the operation after authorizing it.
- [ ] D. The name authorize accurately describes a complete approval system.
- [ ] E. The return value is the resolved path.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: It does not authenticate them.
- B: No file is opened, read, or written by these lines.
- C: It does not perform the operation.
- D: The name must not inflate what the lines implement.
- E: The function hands back a path and nothing else.

**Source:** Three decisions in eleven lines

## MA-ch05.24

Check each statement that is true about seams in the function. Each statement is worth 1 point (5 points total).

- [ ] A. In a multi-step workflow, risk sits less inside any one tool than at the seam where one step's output is handed to the next on trust.
- [ ] B. The root and the approval value are inputs that come in to this function.
- [ ] C. For each seam you state what is passed, what it is trusted to be, and how that trust was earned.
- [ ] D. The returned path is a seam, because it goes out to whatever uses it.
- [ ] E. If the caller supplies an overly broad root, the containment check will reject it.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Conducting AI's point, as the chapter reports it.
- B: Root and approval are accepted on trust, not verified.
- C: These three questions make trust at a seam inspectable.
- D: The caller decides what to do with the returned path.
- E: It will enforce that broad root faithfully.

**Source:** Three decisions in eleven lines

## MA-ch05.25

Check each statement that is true about containment and absolute targets. Each statement is worth 1 point (5 points total).

- [ ] A. Placing a root variable before a target expression forces the target inside the root.
- [ ] B. The reference decides containment by comparing the characters of the two path strings.
- [ ] C. A string test asking whether the target starts with the text naming course confuses the two directories.
- [ ] D. A target inside course-other must not be accepted under a policy that allows only course.
- [ ] E. When the second operand of a pathlib join is absolute, it is treated as relative to the first operand.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: An absolute target discards the root.
- B: It asks about a relation between resolved paths.
- C: course-other begins with the letters of course but is not inside it.
- D: A sibling directory is outside the approved root.
- E: The first operand is discarded.

**Source:** Containment is not a shared prefix

## MA-ch05.26

Check each statement that is true about the symbolic-link fixture. Each statement is worth 1 point (5 points total).

- [ ] A. The symlink result is only a description, because no fixture with a link was actually executed.
- [ ] B. The link is rejected because its name looks suspicious.
- [ ] C. A policy written in terms of visible names would catch the outside-pointing link.
- [ ] D. The research script creates a symbolic link inside a temporary root that points outside it.
- [ ] E. Showing the rejection required reading the outside file to see where the link points.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It is an executed fixture, preserved in the research script and its output.
- B: It is rejected because its resolved destination fails containment.
- C: Names alone would not reveal the outside destination.
- D: The fixture builds a link whose destination is outside the root.
- E: No read of the outside file is needed.

**Source:** The symlink that leaves the folder

## MA-ch05.27

Check each statement that is true about testing the parent-component route and the link route. Each statement is worth 1 point (5 points total).

- [ ] A. A directory listing can show a local entry whose destination is elsewhere.
- [ ] B. Because both routes end at the same containment question, one test of either route is enough.
- [ ] C. The parent-component route and the link route should be tested separately.
- [ ] D. A string pattern that catches .. also catches an outside-pointing link.
- [ ] E. The two routes differ in mechanism but end at the same containment question.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A listing shows names, not where links lead.
- B: They should be tested separately.
- C: The mechanisms differ, so one test cannot stand in for the other.
- D: Neither string pattern covers the other.
- E: Both routes are decided by the same containment relation.

**Source:** The symlink that leaves the folder

## MA-ch05.28

Check each statement that is true about the time boundary between the check and a later use. Each statement is worth 1 point (5 points total).

- [ ] A. If the caller uses the returned resolved path, replacing the original link entry need not redirect it.
- [ ] B. The function checks and returns; a later caller may open a file.
- [ ] C. The reference binds the check and the operation into one indivisible act.
- [ ] D. The research run attempts to prove resistance to changes by another process.
- [ ] E. Every swap of the link entry defeats this function.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The resolved path is a different name from the link entry.
- B: The check and a later open are separate events.
- C: The check and a later open are separate acts.
- D: The run tests a stable fixture, not concurrent changes.
- E: It would be wrong to claim that.

**Source:** The symlink that leaves the folder

## MA-ch05.29

Check each statement that is true about the returned path as the second seam. Each statement is worth 1 point (5 points total).

- [ ] A. A careless caller can check one path and then open the original, unchecked target.
- [ ] B. The teaching function can force callers to use its result.
- [ ] C. A call named authorize earlier in a program shows that a later open is covered.
- [ ] D. In the laundering shape, something unverified takes on the look of something verified because it passed near a reassuring step.
- [ ] E. The failure at the returned-path seam needs a race between the check and the open.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Nothing forces the caller to open the checked path.
- B: The function only returns a path; callers decide what to open.
- C: Follow the value that reaches the open call, not the presence of the word.
- D: A reassuring-looking call makes an unchecked value look checked.
- E: A careless caller can fail without any timing change.

**Source:** The symlink that leaves the folder

## MA-ch05.30

Check each statement that is true about what the limits on the symlink result mean. Each statement is worth 1 point (5 points total).

- [ ] A. In a constructed, stable fixture the function rejected an outside-pointing destination, and that is a result you can report.
- [ ] B. The rejection shows the function resists replacement of the link by another process.
- [ ] C. Because the result has limits, the test accomplished nothing.
- [ ] D. The honest gap is that this is a preflight pathname check that returns a pathname and establishes nothing about the later access.
- [ ] E. Protection against every later mutation is a separate item to document.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The result is bounded to the stable fixture that was run.
- B: The chapter says that is not shown.
- C: The limits locate the rejection; they do not erase it.
- D: The check says nothing about what happens at open time.
- E: Resistance to later changes was not tested and is documented separately.

**Source:** The symlink that leaves the folder

## MA-ch05.31

Check each statement that is true about reads and writes in this policy. Each statement is worth 1 point (5 points total).

- [ ] A. In this policy a contained read does not need a separate approval flag, and a contained write does.
- [ ] B. Which operations need a human is a judgment about consequences that is yours to make for each task.
- [ ] C. The approved root must already reflect the task's data boundary.
- [ ] D. An in-root read passing is a statement that every file under any root is appropriate to read, upload, or disclose.
- [ ] E. A read changes nothing in the filesystem, but what it exposes cannot be un-exposed once it has left the folder.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: This is the exercise's deliberate rule about consequences.
- B: The chapter calls this a judgment about consequences.
- C: If the root is too broad, correct code enforces a wrong policy.
- D: It is a deliberate rule for the exercise, not that statement.
- E: A read cannot be taken back once data leaves the folder.

**Source:** Read and write are different authority questions

## MA-ch05.32

Check each statement that is true about the delegation chapter and the approved root. Each statement is worth 1 point (5 points total).

- [ ] A. If the root holds material the workflow should not touch, the policy is wrong for that task however correct the code.
- [ ] B. The score should be used as a number rather than a question.
- [ ] C. The Computational Skepticism delegation chapter asks of each sub-task whether the action can be undone.
- [ ] D. The approved root is chosen after the code is written, because the code reveals what it should hold.
- [ ] E. That chapter's five-question score has external validation.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The code can be right while the policy is wrong.
- B: Use it as a question, not as a number.
- C: Undoability matters for deciding what to delegate.
- D: The root is part of the policy, decided before the code exists.
- E: It is the author's own instrument with no external validation.

**Source:** Read and write are different authority questions

## MA-ch05.33

Check each statement that is true about the write condition and containment. Each statement is worth 1 point (5 points total).

- [ ] A. A report that says a test wrote x because the returned path ends in x confuses an authorization result with execution.
- [ ] B. A contained write is rejected unless the approval value is exactly True.
- [ ] C. The same target can be accepted for reading and rejected for writing without inconsistency.
- [ ] D. A write proposal that is accepted should be reported as a completed write.
- [ ] E. Passing the containment check can substitute for the write condition.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A returned path is an authorization result, not an operation.
- B: The write condition is checked after containment passes.
- C: Location and write approval are separate questions.
- D: Accepted proposal is the right phrase.
- E: Passing containment cannot substitute for the second.

**Source:** Read and write are different authority questions

## MA-ch05.34

Check each statement that is true about what the approval flag represents in this model. Each statement is worth 1 point (5 points total).

- [ ] A. The flag is a signature.
- [ ] B. If you place True in a fixture, you should label it a simulated approval input and not attribute it to a person.
- [ ] C. The flag is an identity check on the approver.
- [ ] D. The flag is a record that someone saw the precise change.
- [ ] E. The flag is a decision supplied from outside the function.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: It is a supplied Boolean, not a signature.
- B: A fixture True is simulated and should be labeled so.
- C: It checks nothing about who approved.
- D: It does not show that anyone saw the precise change.
- E: The function consumes the flag; it does not produce the decision.

**Source:** Read and write are different authority questions

## MA-ch05.35

Check each statement that is true about the standard a handoff condition must meet. Each statement is worth 1 point (5 points total).

- [ ] A. A Boolean fails that standard the way "the human reviews it" does.
- [ ] B. Challenge item 11 asks you to build a richer approval record.
- [ ] C. A handoff condition is worth having only if a stranger can read it, observe the system, and decide whether it was met.
- [ ] D. A richer approval record authenticates its own contents.
- [ ] E. A richer condition names the operation, the target, and the approver, was issued before the call, and has a target that matches the request.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A reader can see the value but cannot tell whether anyone decided anything.
- B: Item 11 is the exercise on richer approval records.
- C: The companion book's standard, as the chapter states it.
- D: Nothing here authenticates its contents.
- E: These features let a stranger test whether the condition was met.

**Source:** Read and write are different authority questions

## MA-ch05.36

Check each statement that is true about the scope of an approval. Each statement is worth 1 point (5 points total).

- [ ] A. Approval for a disposable draft is not approval to overwrite an original.
- [ ] B. Approval for one target is not a license over a directory.
- [ ] C. The surrounding process must bind its decision to the actual operation and target.
- [ ] D. A model can produce its own independent human approval by writing the word approved.
- [ ] E. The source of an approval value matters as much as its type.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Approval attaches to a specific operation and target.
- B: A directory is a much wider scope than one file.
- C: Otherwise one approval could be stretched over other changes.
- D: A model writing the word approved is not an independent human approval.
- E: A True from the wrong source is still only a Boolean.

**Source:** Read and write are different authority questions

## MA-ch05.37

Check each statement that is true about a human in the loop. Each statement is worth 1 point (5 points total).

- [ ] A. Applying this to grants is the companion book's own claim.
- [ ] B. The companion chapter calls this drift a character flaw.
- [ ] C. If approval is requested for every small step, the answer can drift toward yes.
- [ ] D. A human in the loop is automatically a control.
- [ ] E. When checking is expensive, the cost structure pushes a supervisor toward accepting.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The chapter marks it as the author's reading.
- B: It calls it economics acting on attention, not a character flaw.
- C: Frequent requests wear down careful checking.
- D: Costly checking pushes supervisors toward accepting, so a human is not automatically a control.
- E: Checking costs effort, so approving becomes the easy default.

**Source:** Read and write are different authority questions

## MA-ch05.38

Check each statement that is true about the operation allowlist. Each statement is worth 1 point (5 points total).

- [ ] A. You should let write stand for anything a tool might execute.
- [ ] B. The policy refuses operations outside its allowlist even with approval set.
- [ ] C. If your task needs another operation, you should change the policy deliberately and review the new risk and tests.
- [ ] D. An approved execute is allowed because execute is a kind of write.
- [ ] E. A small vocabulary is useful only while its entries stay specific enough to enforce.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Do not stretch write to mean anything a tool might execute.
- B: Approval cannot override the vocabulary.
- C: A new operation means new risks and new tests.
- D: Execute is outside the allowlist.
- E: Vague entries cannot be enforced.

**Source:** Read and write are different authority questions

## MA-ch05.39

Check each statement that is true about the rows of the boundary matrix. Each statement is worth 1 point (5 points total).

- [ ] A. An escaping traversal raises PermissionError because the resolved target fails containment.
- [ ] B. A contained write without approval raises PermissionError, showing containment does not waive write approval.
- [ ] C. A contained read returns a path, which shows the proposal passes the displayed preflight.
- [ ] D. A contained write with a True fixture returning a path shows that a person approved it.
- [ ] E. Execute raises PermissionError because the resolved path fails containment.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Traversal fails the containment relation.
- B: Containment does not substitute for write approval.
- C: The contained read passes every check.
- D: It shows a simulated approval input satisfies the check.
- E: Execute fails on the operation allowlist, before any path is resolved.

**Source:** Work through the boundary matrix

## MA-ch05.40

Check each statement that is true about reading the matrix rows as branches. Each statement is worth 1 point (5 points total).

- [ ] A. In the traversal row the containment branch fires because the operation vocabulary is violated.
- [ ] B. The execute row fails after the path has been resolved.
- [ ] C. The link row ends in a different branch from the traversal row.
- [ ] D. The contained read shows that the target exists and was read.
- [ ] E. The contained read passes all three checks.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The operation vocabulary is satisfied; the resolved target escapes.
- B: It fails first, without resolving anything.
- C: Both end in the containment branch, by different routes.
- D: It shows only that the proposal passed preflight.
- E: Operation allowed, containment holds, and no write condition applies.

**Source:** Work through the boundary matrix

## MA-ch05.41

Check each statement that is true about the unapproved write case and the status of the matrix. Each statement is worth 1 point (5 points total).

- [ ] A. That case proves location and operation authority are separate.
- [ ] B. The lesson tests, rather than the research fixture, add the Boolean-approved write and the rejection of execute.
- [ ] C. The matrix maps implemented conditions to observed or directly tested results.
- [ ] D. The matrix is a security certification.
- [ ] E. The unapproved contained write passes the first two checks and fails the third.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The same location passes for reading and fails for writing.
- B: The research fixture covers the first four rows of behavior.
- C: Each row ties a condition to a result that was actually observed.
- D: It maps conditions to tested results and certifies nothing.
- E: Operation and location are fine; only the approval is missing.

**Source:** Work through the boundary matrix

## MA-ch05.42

Check each statement that is true about how to build your own version. Each statement is worth 1 point (5 points total).

- [ ] A. You start by giving a tool broad filesystem access to see whether it behaves politely.
- [ ] B. You read the six lesson tests before the reference and predict which rule produces each result, not just accept or reject.
- [ ] C. Your own version is the baseline: the record of what you understood before Claude touched anything.
- [ ] D. If an unapproved write passes in your version, check that your write condition is independent of containment.
- [ ] E. You implement the allowlist, path resolution, containment check, and write condition against a disposable fixture.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The chapter says not to begin that way.
- B: Predicting the rule, not just the outcome, shows understanding.
- C: Your baseline is what you measure Claude's version against.
- D: Write approval must not be implied by containment.
- E: These are the four parts of the preflight.

**Source:** Build It: make denials explainable

## MA-ch05.43

Check each statement that is true about designing the tests for your own version. Each statement is worth 1 point (5 points total).

- [ ] A. To test a later check, you let the earlier checks pass.
- [ ] B. A suite of denial cases alone is enough to show that the policy works.
- [ ] C. A single proposal combining an unknown operation, an escaping path, and missing approval is the best test, since it exercises every check.
- [ ] D. Each test should be narrow enough to explain.
- [ ] E. Fixture cleanup should use broad deletion commands.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Otherwise an earlier failure hides the later check.
- B: A policy that rejects everything passes a denial-only suite and fails the authorized task.
- C: It does not say which boundary you meant to test.
- D: A narrow test points to the rule it exercises.
- E: Cleanup goes through the temporary-directory lifecycle.

**Source:** Build It: make denials explainable

## MA-ch05.44

Check each statement that is true about handing the gate to Claude Code. Each statement is worth 1 point (5 points total).

- [ ] A. Claude Code is opened on real production files so the results are realistic.
- [ ] B. You ask for an implementation that may use whichever third-party libraries are convenient.
- [ ] C. A statement from Claude that the tests passed is your evidence.
- [ ] D. You hand Claude Code your own implementation and ask it to confirm that it is correct.
- [ ] E. You give Claude Code your policy block and your test list, not your implementation.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: It is opened on disposable fixtures.
- B: The request is for the standard library only.
- C: It is Claude's report, not your evidence.
- D: You give it the policy and the tests, not the implementation.
- E: The policy and tests are the specification; the implementation is Claude's job.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch05.45

Check each statement that is true about the three things to do with what Claude returns. Each statement is worth 1 point (5 points total).

- [ ] A. A failing test is often a gap in the gate, which Claude cannot see because it has only what you wrote.
- [ ] B. Every variant that survives your test list is a gap in the list.
- [ ] C. Claude can see gaps in your gate because it reads your whole project.
- [ ] D. You apply the variants from your gate to its function one at a time.
- [ ] E. You compare its function with your baseline and name one difference in behavior, not in line count or style.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Claude sees only the gate you wrote, so gate gaps are invisible to it.
- B: The list failed to distinguish a wrong version from the right one.
- C: Claude has only what you wrote down.
- D: A variant that survives is a wrong program your tests cannot detect.
- E: Behavior differences can reveal a missed boundary or a missed case.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch05.46

Check each statement that is true about the independence of checks. Each statement is worth 1 point (5 points total).

- [ ] A. A checker that fails the same way as the first adds verification.
- [ ] B. A second checker reduces error only to the degree that it fails differently from the first.
- [ ] C. A generated assurance that the code is secure can be accepted as stated if all of Claude's tests pass.
- [ ] D. Tests Claude writes for the function Claude wrote share its reading of your policy.
- [ ] E. Cases Claude adds should be treated as proposals: read each, run it, decide.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It adds agreement, not verification.
- B: Independent failure modes are what make a second check useful.
- C: It should be narrowed to the conditions the tests demonstrate.
- D: Same author, same reading, same blind spots.
- E: A proposal is not evidence until you have run and judged it.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch05.47

Check each statement that is true about the transcript and the comparison with a real permission system. Each statement is worth 1 point (5 points total).

- [ ] A. You preserve the transcript: prompt, plan, diff, commands, and outputs, with the date and displayed model label.
- [ ] B. Inspecting the permission configuration in your Claude Code environment is authorization to change university settings.
- [ ] C. If the session failed or did not run, you record that rather than substituting a fixture.
- [ ] D. Product details change, so the chapter's Boolean should not be substituted for a current product policy.
- [ ] E. Anthropic's Claude Code permissions documentation describes runtime permission rules.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The transcript is the record of what actually happened.
- B: Inspection is for comparison, not for changing settings.
- C: Substituting a fixture would misreport what ran.
- D: The Boolean models a small preflight, not a product's rules.
- E: It is the primary source the chapter compares against.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch05.48

Check each statement that is true about the five limits the chapter lists. Each statement is worth 1 point (5 points total).

- [ ] A. Time and filesystem state: the function makes a later open atomic with the check.
- [ ] B. Meaning: the function inspects the diff of an approved write.
- [ ] C. Data policy: the preflight includes a destination-channel policy and content classification.
- [ ] D. Authentication: the function has no independent account of who supplied the root or the approval value.
- [ ] E. Coverage: the function protects nothing that bypasses it.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The check and the open are not made atomic.
- B: It never looks at the content of a diff.
- C: The preflight has no such data policy.
- D: The root and approval value are trusted inputs.
- E: Anything that bypasses authorize is unprotected.

**Source:** What the toy boundary cannot guarantee

## MA-ch05.49

Check each statement that is true about the authentication and time limits. Each statement is worth 1 point (5 points total).

- [ ] A. A trustworthy workflow needs a real source for the approval decision and a scope that corresponds to the proposed action.
- [ ] B. A True fixture satisfies the Boolean check and proves nothing about consent.
- [ ] C. Rejecting one stable outside-pointing link proves resistance to every concurrent scenario.
- [ ] D. You should not claim a race exploit was executed unless you performed and recorded a safe test of one.
- [ ] E. This lesson implements a real approval source and scope.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: This lesson supplies neither, so none can be assumed.
- B: A fixture True is simulated, so it shows no consent.
- C: One stable link says nothing about concurrent changes.
- D: A race claim needs a recorded safe test behind it.
- E: Neither an approval source nor a scope is implemented.

**Source:** What the toy boundary cannot guarantee

## MA-ch05.50

Check each statement that is true about the meaning and data-policy limits. Each statement is worth 1 point (5 points total).

- [ ] A. The function judges whether an approved write's output serves the user's purpose.
- [ ] B. Permission answers whether the proposal satisfies a boundary, while review answers whether the proposed content is acceptable.
- [ ] C. A contained file may hold restricted information that a later step discloses somewhere inappropriate.
- [ ] D. An approved write can contain a bad change.
- [ ] E. A root is a description of every data obligation attached to the files inside it.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The function never judges whether the output serves the purpose.
- B: These are separate questions, and the next chapter takes up the second.
- C: Location does not settle data obligations; the preflight has no destination-channel policy.
- D: The function does not inspect a diff, so a bad change can pass.
- E: A root is one useful boundary, not that description.

**Source:** What the toy boundary cannot guarantee

## MA-ch05.51

Check each statement that is true about how to write the "Not checked" line. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter lists eleven limits that a passing preflight leaves open.
- [ ] B. Precision lets protections accumulate without one small protection impersonating the whole system.
- [ ] C. The limits are a reason for vague helplessness.
- [ ] D. A fluent list of limitations is as easy for Claude to produce as a fluent claim of security.
- [ ] E. For your artifact, each limit should be tied to what you actually did about it: inspected, tested, or left alone.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The chapter lists five limits.
- B: Each limit is stated narrowly, so protections can add up honestly.
- C: None of this is a reason for vague helplessness.
- D: Fluency is cheap; tying each limit to your own actions is not.
- E: A limit without a record of what you did is just a list.

**Source:** What the toy boundary cannot guarantee

## MA-ch05.52

Check each statement that is true about the artifact you ship. Each statement is worth 1 point (5 points total).

- [ ] A. NEU grading logistics stay outside this chapter, and learner changes stay separate from the reference.
- [ ] B. It states the approved root, allowed operations, approval owner or simulated approval source, denial cases, and actual test results.
- [ ] C. A preflight-only experiment is incomplete unless a file is actually written.
- [ ] D. If a later file operation was not performed, the artifact should omit that fact.
- [ ] E. The artifact is your gate, as run.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Course logistics are kept separate from the chapter's content.
- B: These are the items the artifact must contain.
- C: It is complete on its own terms when its stated task was to test preflight behavior.
- D: The record must show what was and was not done.
- E: The artifact reports the gate as actually run, not as intended.

**Source:** Ship It: a permission policy with evidence

## MA-ch05.53

Check each statement that is true about the evidence record. Each statement is worth 1 point (5 points total).

- [ ] A. You state one decision you revised after testing, with your original prediction and the result that changed it.
- [ ] B. The artifact does not need a denial connected to your capstone.
- [ ] C. For tests, the source of each approval value is recorded as a simulated fixture.
- [ ] D. You record whether the function returned or raised and which branch decided.
- [ ] E. For each proposal, you preserve the requested target and the role its resolved destination played.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Revision after testing shows the prediction was actually tested.
- B: It should include at least one denial that matters to your eventual capstone.
- C: Test approvals are never attributed to a person.
- D: The branch shows which rule decided.
- E: A reviewer can then see why each decision was made.

**Source:** Ship It: a permission policy with evidence

## MA-ch05.54

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. A fluent draft of the sign-off from Claude can be signed as written.
- [ ] B. If your evidence does not support signing, withholding is an honest result.
- [ ] C. The line Claude will not write honestly is the one about what you did not test.
- [ ] D. The "Not checked" line lists the refusals your tests passed.
- [ ] E. The "Not claiming" line says you are not claiming that anyone approved anything.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Only your record shows what you did not test.
- B: A sign-off that claims more than the record supports is the failure the chapter warns about.
- C: Claude cannot know what you did not test; only your record can say.
- D: The "Checked" line does; "Not checked" lists what remains open.
- E: The template lists what you are not claiming.

**Source:** Ship It: a permission policy with evidence

## MA-ch05.55

Check each statement that is true about how the chapter divides the work between Claude and you. Each statement is worth 1 point (5 points total).

- [ ] A. For choosing the root and the operation vocabulary, you decide the smallest root and vocabulary that suffices.
- [ ] B. For edge cases, you write the first list yourself, then choose which of Claude's proposals become tests.
- [ ] C. Claude can approve its own request when the evidence is strong.
- [ ] D. For saying what a pass establishes, Claude chooses the verb and signs.
- [ ] E. For the approver, you name the approver and the scope and make the grant.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Only you know what is in the folder.
- B: The first list is your understanding on the record.
- C: Authority and accountability are a person's.
- D: You choose the verb and sign or withhold.
- E: Authority and accountability belong to a person.

**Source:** The driver's seat

## MA-ch05.56

Check each statement that is true about recording the split between what you delegated and what you kept. Each statement is worth 1 point (5 points total).

- [ ] A. The root and the vocabulary stay with Claude because only Claude knows what is in the folder.
- [ ] B. Each must point to a transcript line, a diff, or an edit you made.
- [ ] C. Implementation is delegated to Claude, but you run your tests on what it returns and compare it with your baseline.
- [ ] D. You record one task you delegated and one judgment you retained.
- [ ] E. If you cannot point to them, the split happened in your head and not in the record.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Only you know what is in the folder, whose it is, and what disclosure would cost.
- B: Pointers make the claim checkable.
- C: Claude writes the function fast; you run the tests and compare.
- D: The record shows the split, not just a claim of it.
- E: Without a pointer, nothing in the record shows the split.

**Source:** The driver's seat

## MA-ch05.57

Check each statement that is true about verifying and auditing your work. Each statement is worth 1 point (5 points total).

- [ ] A. Safe should be read as secure against every attack once the tests pass.
- [ ] B. The research script demonstrates the stable symlink and traversal cases in disposable directories.
- [ ] C. You run the demo and the six tests, then your additional fixture cases.
- [ ] D. The research script is evidence that every security property has been tested.
- [ ] E. authorize may mean a preflight decision or a complete approval system, so the noun and verb should be audited.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It should be replaced with the event and condition that occurred.
- B: Disposable directories keep the cases safe to run.
- C: The commands are given in the verification section.
- D: It is evidence for those cases only.
- E: Ambiguous words hide which event and condition occurred.

**Source:** Verify and reflect

## MA-ch05.58

Check each statement that is true about the distinctions the closing reflection asks you to consider. Each statement is worth 1 point (5 points total).

- [ ] A. The reflection asks you to rate the function's security on a numeric scale.
- [ ] B. The reflection asks whether you collapsed the spelling of a path into its destination.
- [ ] C. The reflection asks whether you collapsed a location into an authority.
- [ ] D. The reflection asks whether you collapsed a preflight into a performed operation.
- [ ] E. The reflection asks whether you collapsed a Boolean into a human act.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It asks which distinction you originally collapsed and which case separated them again.
- B: A path's spelling and its destination can differ.
- C: Being inside the root is not permission to act.
- D: A preflight is not a performed operation.
- E: A True in a script is not a person's decision.

**Source:** Verify and reflect

## MA-ch05.59

Check each statement that is true about the chapter's Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. Item 9 asks for a caller design that checks a path but later uses a different unchecked value.
- [ ] B. Item 6 asks you to claim you demonstrated resistance to concurrent filesystem changes.
- [ ] C. Item 10 asks you to present a speculative sequence as an observed exploit.
- [ ] D. The Assessments carry no points.
- [ ] E. Item 7 says a function that rejected every proposal could pass a denial-only suite yet fail the intended workflow.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: It shows why a call named authorize does not cover a later open.
- B: Item 6 forbids claiming resistance to concurrent changes.
- C: The assessment says not to present speculation as observed.
- D: They are ungraded practice.
- E: Denial-only suites cannot detect an over-strict policy.

**Source:** Assessments - ungraded practice

## MA-ch05.60

Check each statement that is true about the independence of operation, location, and write approval. Each statement is worth 1 point (5 points total).

- [ ] A. A returned Path is a completed file operation.
- [ ] B. A Boolean approval fixture is a human act.
- [ ] C. An allowed operation can target an outside location.
- [ ] D. A True approval cannot override an operation outside the allowlist.
- [ ] E. A contained target can fail the write condition.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A path is not an operation.
- B: A Boolean is not a person's decision.
- C: Operation and location are independent checks.
- D: The allowlist is checked first and approval cannot widen it.
- E: Location passing does not satisfy the write condition.

**Source:** What you can now defend

## MA-ch05.61

Check each statement that is true about the three jobs as they appeared in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Driving: you handed Claude the implementation and the list of edge cases.
- [ ] B. Driving: you handed Claude the root, the vocabulary, the approver, and the verb.
- [ ] C. Checking: you ran the tests yourself and tried variants Claude did not write.
- [ ] D. Conducting: you wrote the policy and the wrong versions your tests had to fail before Claude wrote a line.
- [ ] E. Conducting: the enforcement sat in the prompt, where careful wording could adjust it.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Implementation and edge-case listing are delegated; authority is not.
- B: You kept the root, vocabulary, approver, and verb.
- C: Running them yourself makes the evidence yours, not Claude's report.
- D: The policy and wrong versions come before any implementation.
- E: It sat in code, where a request's wording could not change it.

**Source:** What you can now defend

## MA-ch05.62

Check each statement that is true about authorized changes. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 6 turns to evidence-based review of a change.
- [ ] B. Permission without quality review can authorize a mistake.
- [ ] C. A permission boundary should inspect the diff of an approved write.
- [ ] D. Quality without permission can produce an excellent change to the wrong thing.
- [ ] E. A proposed write can pass every check in the chapter, be performed under real, appropriately scoped approval, and still have contents that are not good.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The chapter's closing hands the quality question to Chapter 6.
- B: A permitted write may still be a wrong one.
- C: It never inspects the diff and should not be asked to.
- D: Quality without scope is aimed at the wrong target.
- E: Permission never asks whether the contents are good.

**Source:** An authorized change can still be a bad change

## MA-ch05.63

Check each statement that is true about the comparison with Claude Code permissions. Each statement is worth 1 point (5 points total).

- [ ] A. The relevant connection is runtime enforcement.
- [ ] B. The teaching function reproduces the product's safeguards.
- [ ] C. The comparison should encourage bypassing a boundary to make the demonstration more dramatic.
- [ ] D. Requesting caution in prose is not the same as constraining tool actions through permission rules.
- [ ] E. You inspect the available configuration without changing institutional settings, and mark unavailable information as uninspected.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Executable rules mediate actions; prose does not.
- B: It is only a preflight illustration.
- C: It should sharpen your permission policy instead.
- D: A request for caution in prose does not constrain actions.
- E: The comparison is read-only and honest about gaps.

**Source:** Anthropics
