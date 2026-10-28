# Chapter 3: Chat, assistant, and agent

## ES-ch03.1

In the chapter's opening, an AI system is asked to fix a report and three interactions all end with polished prose. Describe what each of the three interactions did, and explain why the final messages alone cannot tell you which one happened.

**Points:** 5

**Rubric (1 point each):**

1. The first interaction tells you which paragraphs to change (advice only).
2. The second reads the report and offers a revision grounded in that file.
3. The third saves an edited report, so it is the only one that includes a persistent file change.
4. Notes that all three can end with polished prose and that the final messages can look almost identical.
5. Concludes that they have not performed the same work, so the difference has to be established by evidence about what happened, not by the final message.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.2

A system asked to summarize a folder without changing its files reads a document, writes a good summary, and then saves a cleaned-up version over the original. Explain why this counts as a failure even if the edit is excellent, and identify the specific judgment that was never made.

**Points:** 5

**Rubric (1 point each):**

1. States that the edit is outside the task even if it might be excellent.
2. States that you followed the recipe and still got the wrong outcome.
3. Identifies the cause: nobody decided that the system could write.
4. Says the ability to write arrived with the interface rather than from a decision.
5. Distinguishes a good result from an authorized action as different judgments, noting that only the first was ever made.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.3

The chapter says its constructed scenarios expose three questions. State them, and explain why neither a product name nor a final message that says "done" answers any of them.

**Points:** 5

**Rubric (1 point each):**

1. Question 1: what could the system do (its capability).
2. Question 2: what did you let it do (what was granted or authorized).
3. Question 3: what evidence says what it did.
4. States that a product name answers none of the three, and neither does a final message that says done.
5. Notes that the scenarios are constructed, not claims about a recorded Claude session, and are used only to make the questions inspectable.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.4

Name the three jobs that stay with the human in this book and state the question each one asks in Chapter 3. For each, name the written artifact or practice the chapter ties to it.

**Points:** 5

**Rubric (1 point each):**

1. Names the three jobs: conduct, check, and drive.
2. Conduct asks how much autonomy the task needs and whether you decided that before you granted anything.
3. Ties conduct to the gate, meaning writing the decision down before the grant.
4. Check asks what the record shows happened as opposed to what the interface called itself, and ties it to the sign-off, which is what you can honestly claim from the record.
5. Drive asks who authorized the action and what keeps that decision with a person, and ties it to the driver's seat, the split of labor.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.5

Explain how Chapter 3 builds on Chapters 1 and 2, and why applying the three jobs to an action raises the stakes compared with applying them to an answer.

**Points:** 5

**Rubric (1 point each):**

1. Chapter 1: Claude is far better than you at fluent, fast, parallel production, so you do not compete with it there.
2. Chapter 1: three jobs stay with you (conduct, check, drive) because your name goes on the result.
3. Chapter 2 applied the jobs to an answer, with a contract written before the prompt.
4. Chapter 2 also required a pass that names what it passed.
5. Chapter 3 applies the jobs to an action, which raises the stakes because an action leaves a mark after the conversation ends.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.6

What status does the chapter give to the labels chat, assistant, and agent, and why does it insist on treating them as handles for explicit capability sets rather than as universal names?

**Points:** 5

**Rubric (1 point each):**

1. The labels belong to this exercise.
2. They are not a verified map of current product features.
3. They do not claim that every system bearing one of those names has the same permissions or architecture.
4. Treated as universal names, the labels turn the lesson into a vocabulary test that interfaces will outdate.
5. Treated as handles for explicit capability sets, they let you inspect an operation directly and see what the classifier throws away.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.7

The chapter extends a pattern from Chapters 1 and 2 to actions. State the earlier pattern and the three new statements the chapter adds.

**Points:** 5

**Rubric (1 point each):**

1. Earlier pattern: a probability is not a truth judgment.
2. Earlier pattern: a format pass is not source support.
3. New: capability is not authorization.
4. New: an event label is not independent proof.
5. New: a write is not necessarily dynamic agency.

**Source:** Chapter 3: Chat, assistant, and agent (opening)

## ES-ch03.8

The chapter says you should be able to write the gate before any grant is made, and to read an event trace as evidence. State what the gate must contain at minimum, and what you must say about each claim when reading a trace.

**Points:** 5

**Rubric (1 point each):**

1. The gate names the smallest capability set that finishes the task.
2. The gate names the operation that is authorized.
3. The gate names the target that is authorized.
4. The gate names the condition that sends control back to you, and it is written before any grant is made.
5. For each claim in a trace you say whether it was proposed, attempted, completed, or observed (and what no trace can show).

**Source:** What you will be able to do

## ES-ch03.9

"Fix this report" hides four requests. Name them, and explain why the chapter makes choosing among them the first decision, before any choice of interface.

**Points:** 5

**Rubric (1 point each):**

1. Request 1: explain what is wrong.
2. Request 2: propose a replacement.
3. Request 3: save a new version.
4. Request 4: alter the original.
5. Each has a different scope and consequence for state, a system will pick one if you do not, and everything you grant and review follows from the decision.

**Source:** A response and a file are different kinds of result

## ES-ch03.10

A student summarizes this section as "text is harmless and files are dangerous." Correct this using the chapter's three hypotheticals and its operational distinction.

**Points:** 5

**Rubric (1 point each):**

1. In the first hypothetical the output is advice, and someone must still decide whether to apply it.
2. The second adds source access and the third adds a mutation, meaning a stored artifact changes.
3. Text can steer a decision, so it is not simply harmless.
4. A file edit can be trivial and well authorized, so it is not simply dangerous.
5. The distinction is operational: a persistent change creates a before and an after that you can check separately from the final explanation, so a proposed revision and a saved revision are different deliverables.

**Source:** A response and a file are different kinds of result

## ES-ch03.11

A system replies "Here is how to fix the paragraph" and shows new text. A colleague then writes in the status log, "The paragraph in the specified file has changed." Using the chapter, say what the transcript supports, what it does not, and what would support the colleague's claim.

**Points:** 5

**Rubric (1 point each):**

1. The transcript supports a claim about the proposal.
2. It says nothing about where, or whether, the text was written.
3. The two statements are different claims, and the second needs evidence about the file.
4. The evidence has to follow the object whose state is being claimed (the file, not the explanation).
5. A persistent change creates a before and an after, so a check of the file's state can be made separately from the final explanation.

**Source:** A response and a file are different kinds of result

## ES-ch03.12

Write the chapter's acceptance statement for the folder-summary task, and explain how it treats a system's offer to save a separate cleaned-up draft.

**Points:** 5

**Rubric (1 point each):**

1. Requirement: inspect the specified source.
2. Requirement: return a source-grounded summary.
3. Boundary: leave the source files unchanged.
4. Notes that reading is needed and writing the originals is not.
5. Treats the offer to save a separate draft as a proposed change of scope for you to evaluate, not something the original request already included.

**Source:** A response and a file are different kinds of result

## ES-ch03.13

What does the chapter's symbolic teaching program let you explain, what does it not demonstrate, and why does the chapter still start there?

**Points:** 5

**Rubric (1 point each):**

1. It represents operations symbolically and does not touch a real folder.
2. That is enough to explain a capability comparison.
3. It is not enough to demonstrate filesystem safety, so the small set function must not be credited with protections it does not implement.
4. Chapter 5 builds a path and permission check.
5. Starting symbolically forces you to name the operations before a complicated runtime surrounds them; if you cannot say whether the task needs a write, a larger tool stack will only make an ambiguous request easier to execute.

**Source:** A response and a file are different kinds of result

## ES-ch03.14

An assistant's answer mentions a report and sounds well informed. Explain why you should not log a read event on that basis, and what you should do instead in a real run.

**Points:** 5

**Rubric (1 point each):**

1. A response can use text already in the conversation without performing any new read.
2. You should not infer a read event from an answer that merely mentions a document.
3. Decide in advance what you will count as a read event.
4. In a real run, record how the document arrived.
5. Record what evidence shows the operation.

**Source:** A response and a file are different kinds of result

## ES-ch03.15

Describe the three teaching surfaces in the chapter's SURFACES dictionary, what the strings stand for, and two reasons the chapter gives for not over-reading the dictionary.

**Points:** 5

**Rubric (1 point each):**

1. chat is {reason}, assistant is {reason, read}, and agent is {reason, read, write}.
2. reason stands for response-level processing, read for access through the modeled reading capability, and write for a modeled ability to change state.
3. Inserting a string into a set creates no access; the program stores a declared description that later functions compare.
4. The sets are nested, which is a design convenience and not a theorem about real interfaces.
5. Real interfaces can have capabilities that fit no single ladder.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.16

Define R, C, and the missing set M, state what an empty M does and does not mean, and give two ways a correct subtraction can still mislead.

**Points:** 5

**Rubric (1 point each):**

1. R is the set of capabilities the task requires and C is the set declared for a surface.
2. M = R minus C, the requirements that do not appear in the surface.
3. An empty M means the declared set covers the declared requirements.
4. A correct subtraction can sit on an incomplete task description or on an inaccurate account of the runtime.
5. The arithmetic authenticates neither the task description nor the runtime account.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.17

A constructed task requires both read and write. Compute the missing set for chat, assistant, and agent, and say what the resulting table lets you check and what it does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. chat is missing read and write.
2. assistant is missing write.
3. agent is missing nothing (an empty set).
4. Every cell can be reconstructed from the sets, so you can point at the required operation and check whether it appears in the declared set.
5. The table answers only that narrow question; it gives no sense that one interface is more agentic and does not say any write is authorized.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.18

Using the chapter's missing function, compute the result for the requirement list ['write', 'read', 'read', 'delete'] on each of the three surfaces, and explain what the unfamiliar label does and how this differs from the way classify treats unknown names.

**Points:** 5

**Rubric (1 point each):**

1. chat returns ['delete', 'read', 'write'] (sorted).
2. assistant returns ['delete', 'write'].
3. agent returns ['delete'].
4. The duplicate read is removed by set conversion, and delete stays in the result because requirement labels are not validated, which is a usable signal that the declared surfaces do not cover the task.
5. classify rejects an unknown event with an error, whereas missing validates only the surface name, so the two functions have different policies.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.19

A task only needs to read a source. Which of the chapter's surfaces would you choose, and why is that choice not a matter of distrusting the larger surface?

**Points:** 5

**Rubric (1 point each):**

1. A read-only inspection requires read, not write.
2. In the nested model assistant covers the requirement (empty missing set).
3. agent would also cover read but adds a write capability the task does not need.
4. The reason is not that the larger surface is untrustworthy; the task simply does not need its extra operation.
5. Every operation you grant is one more thing you must be able to check afterward.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.20

Explain the Conducting AI reflex the chapter borrows for choosing capability, quote the phrase it uses about the human's job, and say what status the book's five-layer stack has.

**Points:** 5

**Rubric (1 point each):**

1. Quotes the phrase: the human's job is "not to type less" but "to decide more precisely".
2. The reflex is to select the lowest capability the step requires.
3. The reason is that the more constrained tool is easier to verify.
4. The five-layer capability stack is the author's teaching device and not an industry standard.
5. In this chapter the reflex becomes a document you write before the grant, which is the gate.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.21

You are asked to summarize one named report file without changing it. Write the gate for this task using the chapter's gate headings, with a concrete entry for each.

**Points:** 5

**Rubric (1 point each):**

1. Outcome: a summary whose claims can be checked against the source.
2. Required and Granted: reason and read, with nothing wider.
3. Refused: write, anywhere; Authorized target: the one source file named in the task.
4. Back to me if: the system proposes saving anything, touching a second file, or changing the request.
5. Evidence and Passes if: the recorded events and a before-and-after listing; no write in the events, an identical listing, and every sentence of the summary traced to a passage.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.22

Which parts of the gate can Claude help with, which part can it not write, and why does the chapter insist that a gate must contain a case that can fail?

**Points:** 5

**Rubric (1 point each):**

1. Claude can sharpen the gate by hunting for the case you missed, such as whether a temporary file counts as a write.
2. Claude cannot write the gate for you without defeating its purpose.
3. The gate is where the decision goes on the record before the grant makes the decision by default.
4. A gate with no failing case is a wish.
5. The plausible but wrong gate grants agent because that surface is available and the request says to help; the test is whether the gate names an operation and a target that would be refused.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.23

"Smaller is not automatically better." Explain this with the chapter's example, and say what to do when you widen the scope after seeing the work.

**Points:** 5

**Rubric (1 point each):**

1. A response-only interface may be unable to produce what the task needs.
2. If you authorized a file change and expect it to exist, returning advice alone is incomplete.
3. When you widen the scope, rewrite the gate.
4. Date the new version, keep the old one, and authorize again.
5. Sufficient autonomy means matching the outcome, not minimizing the tool set whatever the work; design first does not mean freeze the design.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.24

The chapter says three things hide inside the word autonomy. Name and define them, say how many of them the classifier measures, and explain why "use an agent" is a weak recommendation.

**Points:** 5

**Rubric (1 point each):**

1. Capability is what the system may do, which is what this chapter's sets represent.
2. Control is who or what chooses the next operation (Building effective agents distinguishes predefined workflows from systems where the model directs its own process).
3. Scrutiny is how hard the output must be checked, which depends on the work and not on the permissions.
4. The classifier measures only one of the three.
5. "Use an agent" is shorter and says less than a recommendation that keeps a sentence for each of the three.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.25

Explain the volume trap the chapter borrows from Irreducibly Human, the status the chapter gives the claim, and how it shapes what a gate contains.

**Points:** 5

**Rubric (1 point each):**

1. Generation scales with the machine, but verification does not.
2. The more you grant, the more there is to check, and your attention does not grow with it.
3. The chapter treats it as an argument about review capacity, not as a result it measured.
4. That is why the gate names the evidence you will read and not only the operations you allow.
5. It supports preferring the smaller grant, since every added operation is more to review.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.26

Contrast capability sets with event traces. Which does the classifier consume, and what analogy from Chapter 1 does the chapter use?

**Points:** 5

**Rubric (1 point each):**

1. Capability sets describe what a surface is declared able to do.
2. Event traces describe what is recorded as having happened.
3. The analogy is the Chapter 1 relation between a distribution (what is available) and a sample (a particular run).
4. The classifier consumes a list of event names, not the capability table.
5. A capability set therefore cannot tell you what a particular run did; only a record of that run can.

**Source:** Events, not labels: what the record can show

## ES-ch03.27

Apply the classify function by hand to ['write', 'reason'], ['reason', 'read', 'read'], [], and ['reason', 'delete']. Give each result and name the branch or rule responsible.

**Points:** 5

**Rubric (1 point each):**

1. ['write', 'reason'] gives agent, because a write anywhere takes precedence.
2. ['reason', 'read', 'read'] gives assistant, because there is a read and no write.
3. [] gives chat, by inspection, through the default branch.
4. ['reason', 'delete'] raises ValueError (unknown event) because delete is outside the allowed set.
5. Notes that each result is a category under the rule and does not prove how much reasoning occurred.

**Source:** Events, not labels: what the record can show

## ES-ch03.28

List what classification by presence discards and give an example where the lost information would matter in a real review.

**Points:** 5

**Rubric (1 point each):**

1. Order: a write at the start and a write at the end both trigger the write branch.
2. Repetition: one read and several reads share a label.
3. Targets: a write could be a disposable draft or an overwritten original and the label cannot tell them apart.
4. Authority, evidence quality, and whether the logged event really happened are also discarded.
5. Keep the original trace beside the label because the label is lossy and the trace is the evidence; the compression suits teaching but would be reckless in a real review.

**Source:** Events, not labels: what the record can show

## ES-ch03.29

"The function trusts the list it is given." Explain what this means for a claim that a file was written, and how an input contract differs from forensics.

**Points:** 5

**Rubric (1 point each):**

1. An event string does not prove the operation succeeded.
2. If someone supplies write, classify returns the write-based label without looking at any filesystem.
3. That is an input contract, not forensics.
4. Keep the original trace beside the label.
5. A claim that a file was written needs evidence about the file's state, such as a before-and-after listing.

**Source:** Events, not labels: what the record can show

## ES-ch03.30

The chapter lists four descriptions of one run. Name them in order, say what each can and cannot support, and say why the order matters.

**Points:** 5

**Rubric (1 point each):**

1. The label (a product name) can support a guess about what to expect but nothing about this run.
2. The narration can support that something was said but not that it happened.
3. The event trace can support that an operation was recorded if the recording is sound, but not targets, success, or authority unless they are recorded.
4. The folder state before and after can support that something changed or did not, but not who did it or whether it was authorized.
5. The order runs from top to bottom as growing independence from the system's own account of itself.

**Source:** Events, not labels: what the record can show

## ES-ch03.31

A system's final message says "I saved the edited report." The event trace contains a write, but a before-and-after listing of the folder is identical. Which evidence do you trust for a claim about the file, and what can you still not conclude?

**Points:** 5

**Rubric (1 point each):**

1. For a claim about a file the state check is the strongest of the four descriptions.
2. It fails differently from the others: it can show no change when the narration said saved.
3. Concludes that the listing does not support the claim that the file changed, whatever the narration and the trace say.
4. The listing cannot show who did something or whether it was authorized.
5. Claude can run the listing and compare it with your rule but cannot vouch for its own action; ask who produced each record, the thing that acted or something that watched.

**Source:** Events, not labels: what the record can show

## ES-ch03.32

Define the four verbs the chapter uses for a write in a trace. Then label each step: (a) a reply offers to save the file; (b) the runtime is asked to write; (c) the runtime reports success; (d) you list the folder and see the changed file.

**Points:** 5

**Rubric (1 point each):**

1. Proposed means a response offers the write, so step (a) is proposed.
2. Attempted means the operation was requested of the runtime, so step (b) is attempted.
3. Completed means the runtime reported success, so step (c) is completed.
4. Observed means you saw the changed state, so step (d) is observed.
5. A report should say which verb its evidence supports, because the first three are not the fourth.

**Source:** Events, not labels: what the record can show

## ES-ch03.33

Predict the classifier labels for the chapter's three constructed traces ['reason'], ['reason', 'read', 'reason'], and ['reason', 'read', 'write']. For each, state what evidence is still needed before a report could make a stronger claim.

**Points:** 5

**Rubric (1 point each):**

1. The labels are chat, assistant, and agent respectively.
2. First trace: it does not establish that the source was read; evidence is needed on whether required source access occurred through any recorded route.
3. Second trace: it is consistent with the read-only boundary, but it does not say which source was read or whether the summary follows it.
4. Third trace: the classifier reports a write category, not a violation; evidence is needed on what changed, whether the write succeeded, and whether it was authorized.
5. "This trace is safe" and "this trace is unsafe" are both over-claims on three strings, and writing the over-claim sentence first is how you catch yourself making one.

**Source:** One task, three constructed traces

## ES-ch03.34

The chapter says the published research run directly checks some results and not others. Which are which, and why does it insist on keeping recorded execution and code reasoning distinct?

**Points:** 5

**Rubric (1 point each):**

1. The traces are constructed, not recordings from current Claude products.
2. The published research run directly checks the read classification and the missing-capability comparison.
3. The other trace labels are derivations from the displayed function and proposed cases for your own run.
4. Both kinds of evidence teach, but only one is an observed run.
5. The missing-set results are preserved in the worked-example output under chapters.03.

**Source:** One task, three constructed traces

## ES-ch03.35

Suppose you explicitly ask for a separate summary file in a disposable learner directory. What changes in the required set, what does not change about the target, and what does this show about the three-capability model?

**Points:** 5

**Rubric (1 point each):**

1. The required set would include writing.
2. A write-capable surface could be sufficient.
3. The target still matters: a new draft in the authorized directory is not permission to overwrite the source.
4. The three-capability model cannot express that restriction.
5. This is the payoff of a small model: it shows the moment a label becomes too coarse, where adding confidence will not help and you need more information and a more specific boundary.

**Source:** One task, three constructed traces

## ES-ch03.36

An empty missing set tells you something and fails to tell you much more. State what it says, name at least three facts it does not establish, and explain why reading the result more enthusiastically will not help.

**Points:** 5

**Rubric (1 point each):**

1. It says the declared surface covers the declared requirements.
2. It does not say that you own the target.
3. It does not say that affected people consented.
4. It does not say that the source may be uploaded or that a write is appropriate.
5. None of those facts is an input to the subtraction, so more enthusiastic reading cannot recover them.

**Source:** Capability does not confer authority

## ES-ch03.37

What is authority in the chapter's sense, who makes it, and what must it name? Apply this to the request "help with a report".

**Points:** 5

**Rubric (1 point each):**

1. Authority is a decision with a record, and a person makes it.
2. It names the allowed source, the output location, and the operation requested.
3. If the request is read-only, record that; if an edit is authorized, identify the target.
4. A vague permission to help with a report should not quietly become permission to change unrelated files.
5. The model can propose an action, including a well-chosen one, and you authorize it, saying what, where, and when.

**Source:** Capability does not confer authority

## ES-ch03.38

Does this chapter's code enforce permissions? Give the chapter's evidence, say where permission checking is built, and say how you should describe a capability inventory in your report.

**Points:** 5

**Rubric (1 point each):**

1. States that the chapter does not implement a permission engine.
2. Evidence: the functions take no permission inputs.
3. Chapter 5 builds a narrow runtime check in Python.
4. Do not present a capability inventory as if it enforced a policy.
5. Authority remains a decision with a record that a person makes, not something inferred from the sets.

**Source:** Capability does not confer authority

## ES-ch03.39

Explain the reciprocal mistake of treating inability as prohibition, and name the four things the chapter says to keep distinguishable.

**Points:** 5

**Rubric (1 point each):**

1. If the teaching chat surface lacks writing, that shows only that it cannot cover a write requirement.
2. It does not show that a write would have been forbidden had another authorized tool performed it.
3. Feasibility and permission answer different questions, and mixing them lets a technical limit pass as a moral judgment.
4. A permission request does not prove the proposed action is useful, since you can authorize a draft that turns out to be poor.
5. The four things are the proposed action, the authority, the execution, and the quality review, and one approval or capability flag is not a certificate for all four.

**Source:** Capability does not confer authority

## ES-ch03.40

What should the permission column of your artifact say, and what must you avoid doing when permission evidence is weak or missing?

**Points:** 5

**Rubric (1 point each):**

1. It is written in plain language.
2. It can say that a constructed scenario stipulates a read-only request, or that you authorized a specific disposable write.
3. Do not invent an approver.
4. Do not treat a simulated person in a fixture as real consent.
5. If permission evidence is absent, write absent or pending, because the record's integrity depends on keeping the gap visible.

**Source:** Capability does not confer authority

## ES-ch03.41

The second half of the gate is a contract with tests. State the five claims of the contract and give the smallest test case that exposes a classifier keyed on the final event.

**Points:** 5

**Rubric (1 point each):**

1. missing sorts and removes duplicates.
2. An unknown surface is refused and an unknown event is refused.
3. A write anywhere yields agent, and a read without a write yields assistant.
4. A final-event classifier agrees with the real one for ['reason', 'read', 'write'] but differs for ['write', 'reason'].
5. A test list without that second case would pass the wrong version; a classifier that treats an unknown event as reason would pass every happy-path test, so each wrong version needs its own smallest exposing case.

**Source:** Build It: your own classifier, then the second half of the gate

## ES-ch03.42

Does a test showing that the classifier rejects an event named delete-everything show that deletion is prevented? Explain, and say what must be designed separately if a system relies on a trace.

**Points:** 5

**Rubric (1 point each):**

1. No: the function validates its vocabulary, not operating-system calls.
2. The test shows only that the classifier refuses an unknown name.
3. It does not show that a program cannot perform an operation and leave it out of the list.
4. Event validation assumes something about where the events come from.
5. A system that relies on a trace must design and check that recording boundary separately.

**Source:** Build It: your own classifier, then the second half of the gate

## ES-ch03.43

Describe how you conduct Claude Code in the Use It exercise: what you give it, what you withhold, what you do with the result, and what a failing test often means.

**Points:** 5

**Rubric (1 point each):**

1. Hand Claude the gate, the contract, and the test list, and not your implementation.
2. Ask for an implementation that satisfies the contract and passes your tests.
3. Run your tests yourself on what it returns.
4. A failed test often marks a gap in your gate, which Claude cannot see because it only has what you wrote.
5. Compare its classifier with your baseline and name one difference: a boundary it handled that you missed, or one it silently ignored.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.44

Why does the chapter ask you to have Claude propose a deliberately wrong classifier that passes your tests, and what do you conclude if it does pass?

**Points:** 5

**Rubric (1 point each):**

1. You ask Claude to propose a deliberately wrong classifier that still passes your tests.
2. You check by hand whether it actually passes.
3. If it does pass, your tests were too weak.
4. You found that out cheaply.
5. You also ask what the classifier cannot infer and verify each answer against the code; missing targets, permission fields, and success results are directly inspectable.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.45

Describe the three-interface comparison the chapter asks you to perform, including what you write first, what you record about each run, and how you handle a run you cannot restrict to reading.

**Points:** 5

**Rubric (1 point each):**

1. The same small task goes through Claude chat, Claude with an uploaded source, and Claude Code in a disposable Python repository.
2. Write the task's gate first, including what you grant.
3. Record the interface and the operations actually available in your run, and do not assume a permanent capability assignment from a name.
4. Record the permission settings you used; if you cannot restrict a run to reading, record it as a run in which write was granted.
5. It is an experiment for you to perform and document, not a result the chapter supplies, using harmless material and a narrow task.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.46

Why must you record how the source was supplied, and how do you keep the proposed apart from the executed in an experiment that includes a write?

**Points:** 5

**Rubric (1 point each):**

1. The source may have been pasted into the conversation, attached through the interface, or read by a tool.
2. Routes that produce similar answers leave different observation records.
3. Your symbolic trace should be an explicit abstraction of the record, not a guess that the system must have read because the answer sounds informed.
4. For a write, make the target a disposable learner artifact, give the authorization yourself, and record files before and after.
5. A response may offer to save a file, ask permission, or explain a command without running it, and none of those is the completed write a trace stipulates.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.47

One of the three interfaces is unavailable to you. What does the chapter tell you to do with its row, what can you still run, and when is a mix of observed and hypothetical records acceptable?

**Points:** 5

**Rubric (1 point each):**

1. Mark its row not run and say what is missing.
2. Do not manufacture the row.
3. You can still run the offline classifier on constructed traces, labeled constructed.
4. An honest mix of observed and hypothetical records is usable when the provenance is explicit.
5. An invented completion is not usable.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.48

What must a useful row of the action-surface comparison contain, and what must a reader be able to do with it?

**Points:** 5

**Rubric (1 point each):**

1. It names the source and the requested outcome.
2. It names the granted and observed capabilities.
3. It records what was proposed and what changed.
4. It records the permission evidence and what supports each entry.
5. Another reader can follow the row from task to gate, from gate to record, and from record to claim; the target is not an implementation detail because it decides whether the action stayed in scope.

**Source:** Ship It: the action-surface comparison

## ES-ch03.49

What kind of conclusion should the comparison draw, and what must it not claim? Include what to do if you revise the required capability set.

**Points:** 5

**Rubric (1 point each):**

1. It recommends an interface for a stated task under stated assumptions.
2. An example: the read-enabled teaching surface is sufficient for the no-write summary, while a separately authorized saved draft needs writing.
3. It must not proclaim that one product is universally better or safer, because the evidence does not cover that.
4. If you revise the required capability set after inspecting the task, keep both versions and say why.
5. That revision is a learning event and not an embarrassment to erase.

**Source:** Ship It: the action-surface comparison

## ES-ch03.50

Reproduce the fields of the sign-off template, and explain what the Not checked line is for and how the verbs in the sign-off should be chosen.

**Points:** 5

**Rubric (1 point each):**

1. The fields are Checked, How, Not checked, Not claiming, and Signed or withheld.
2. The How field offers by hand, a test written before reading the reference, a listing you ran yourself, or with Claude's help (say which parts).
3. The Not checked line does the work, for example whether any trace was complete, whether any summary was faithful, and any interface not run.
4. Use verbs that match the evidence (recorded, observed, computed, tested); an observed state change and a recorded event are not the same claim, and "authorized" needs a named person and a named operation.
5. If the record does not support signing, withholding is an honest result; Claude's contribution is recorded too.

**Source:** Ship It: the action-surface comparison

## ES-ch03.51

According to the driver's seat table, who does what when a write must be authorized, and why does this stay with the person? Why is a fluent permission request or a fixture's approval not enough?

**Points:** 5

**Rubric (1 point each):**

1. Claude should propose the action and its target.
2. You authorize it, naming what, where, and when.
3. Authority and accountability follow the person whose files and name these are.
4. A model can ask for permission fluently and a fixture can supply an approval instantly.
5. Neither is a person deciding: the model proposes, you authorize.

**Source:** The driver's seat

## ES-ch03.52

Take the driver's seat rows for implementing the classifier from your contract and for checking what happened. For each, state what Claude should do, what you should do, and why it stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Implementing: Claude implements the classifier from your contract and proposes a wrong version that passes.
2. Implementing: you build your baseline and run your tests, because you cannot audit what you have not built.
3. Checking: Claude runs the listing and compares it to your rule.
4. Checking: you decide what counts as a change and read the state.
5. The check stays with you because it must fail differently from the narration.

**Source:** The driver's seat

## ES-ch03.53

Describe the verify step: what you run, which cases you add and what each must name, and what you do with the strongest claim in your comparison.

**Points:** 5

**Rubric (1 point each):**

1. Run the demo, the six lesson tests, and your additional cases, explaining each result and its route through the code.
2. Add a successful case outside the demo.
3. Add a failure that would matter in your capstone.
4. Name the defect each case is designed to expose and say how another defect could survive both.
5. Find evidence for the strongest claim (such as a file changed or an action authorized) outside the classifier, and narrow the claim if you cannot.

**Source:** Verify and reflect

## ES-ch03.54

After building the classifier, what does the chapter ask you to reflect on? Include what the classification discarded and the distinctions you may have collapsed in your first reading of "fix this report".

**Points:** 5

**Rubric (1 point each):**

1. The classification discarded sequence, repetition, targets, results, and authority.
2. A summary should make a large record easier to navigate and not become an excuse to throw away the evidence needed to evaluate it.
3. Revisit your first reading of "fix this report": did you hear advice, a draft, or an edit, and did the stated scope support it?
4. The code can calculate missing capabilities perfectly while the task model is wrong.
5. Ask which distinction you collapsed (capability and authority, label and trace, or proposed and executed) and name the record that separated them again.

**Source:** Verify and reflect

## ES-ch03.55

Assessment item 1 asks for a hand calculation and a change of requirement. Do it: for a read-and-write task give the missing set on each surface, then change the requirement to read only, say which recommendation changes, and state the assumption that makes the sets nested.

**Points:** 5

**Rubric (1 point each):**

1. For read and write: chat is missing read and write, assistant is missing write, and agent is missing nothing.
2. For read only: chat is missing read, and assistant and agent are missing nothing.
3. The recommendation changes: for the read-only task assistant is sufficient, whereas the read-and-write task needs agent.
4. The nesting assumption is that everything in chat is in assistant and everything in assistant is in agent.
5. That nesting is a design convenience and not a universal product taxonomy.

**Source:** Assessments - ungraded practice

## ES-ch03.56

Item 4 asks you to construct two event lists with the same categories in different orders. Give an example pair, state their labels, describe a workflow where order would matter, and write the test that exposes a classifier keyed on the final event.

**Points:** 5

**Rubric (1 point each):**

1. Gives a valid pair using the same events in different orders, such as ['write', 'reason'] and ['reason', 'write'].
2. States that both lists receive the label agent because classification by presence ignores order.
3. Describes a hypothetical workflow in which order matters and names the extra evidence a report would need to show the sequence.
4. Writes the test: ['write', 'reason'] should be classified agent, which a classifier keyed on the final event would fail.
5. Notes that ['reason', 'read', 'write'] alone would not expose that wrong version because both give agent.

**Source:** Assessments - ungraded practice

## ES-ch03.57

Item 7 asks for an explicitly hypothetical record containing a proposed edit, a permission request, and a completed edit with a before-and-after observation. Give each part a verb and say which parts justify a write event under the trace definition.

**Points:** 5

**Rubric (1 point each):**

1. The proposed edit is labeled proposed.
2. The permission request is a request, not a completed write.
3. The completed edit is labeled completed (the runtime reported success).
4. The before-and-after observation is labeled observed.
5. Only the completed edit justifies a write event; the proposal and the permission request do not, and no real person's approval may be invented.

**Source:** Assessments - ungraded practice

## ES-ch03.58

Item 9 asks you to construct a scenario in which the missing set is empty but the proposed write exceeds the stated task. Explain why the set calculation still succeeds, what permission question is left open, and what revision could proceed.

**Points:** 5

**Rubric (1 point each):**

1. The scenario has a surface that covers the declared requirements (an empty missing set) while the proposed write goes beyond the stated task.
2. The calculation still succeeds because it compares only declared requirements with declared capabilities.
3. The open question is whether this specific operation on this specific target is authorized.
4. The workflow can be revised to proceed within the existing scope or to return the decision to a person.
5. Claude could draft the revision, but the act of authorizing cannot be handed to it, and good intentions do not create authorization.

**Source:** Assessments - ungraded practice

## ES-ch03.59

Item 10 asks for two hypothetical systems whose names suggest the wrong capability set. Describe how you would approach it, and explain why a write-capable predefined workflow and a model-directed process can look the same to this classifier.

**Points:** 5

**Rubric (1 point each):**

1. Designs two hypothetical systems whose names suggest an operation set different from the one they actually have.
2. Describes each system's actual operation set rather than relying on the name.
3. Classifies constructed events for each system using the lesson rule.
4. The classifier sees only which operation categories appear, so the two kinds of system receive the same label if the same categories appear.
5. Keeps architecture (control) and action capability as separate axes.

**Source:** Assessments - ungraded practice

## ES-ch03.60

Item 11 asks for a richer event representation. What fields should it add, how does it improve review, and what can it still not do?

**Points:** 5

**Rubric (1 point each):**

1. It adds a target.
2. It adds proposed-versus-executed status.
3. It adds outcome evidence.
4. Adding fields does not make their contents true, so it still cannot authenticate them.
5. Identify one check at the recording boundary and one judgment that remains outside the data structure.

**Source:** Assessments - ungraded practice

## ES-ch03.61

Why does the chapter say that a set of tools is not a loop, and how does Chapter 4 extend the lesson that capability is not authority?

**Points:** 5

**Rubric (1 point each):**

1. Something must take the current state, select an action, execute it, observe the result, and decide whether to continue.
2. Chapter 4 makes that controller visible in Python.
3. The controller is given a finite action budget.
4. In the trace a finish action produces a finished status even when the final answer is wrong, so a terminal state does not establish correctness.
5. Your action-surface comparison tells you which operations the controller might request; the loop adds sequence and stopping behavior but does not erase the need for source checks and authority boundaries.

**Source:** The next operation needs a controller

## ES-ch03.62

How does the Anthropics note compare Building effective agents with the chapter's event-presence rule, and what two hypothetical systems does it ask you to describe?

**Points:** 5

**Rubric (1 point each):**

1. The upstream workflow-versus-agent distinction concerns how the process is directed.
2. The chapter's classifier concerns which simplified operation categories appear.
3. They answer different questions.
4. You describe one hypothetical predefined workflow that writes and one model-directed process that does not need to write.
5. You explain why the teaching rule alone cannot distinguish their control structures, without claiming the model reproduces Anthropic's implementation.

**Source:** Anthropics

## ES-ch03.63

Describe the three levels of scrutiny in the Conducting AI note, the two levels you record per row, and the claim the book makes about risk.

**Points:** 5

**Rubric (1 point each):**

1. Level I is a glance at the output against its input, level II is checking against sources outside the interaction, and level III is examining the framing the output supplies.
2. The levels (copy-editor, research-assistant, supercollaborator) are the author's teaching framework, not a measured product ranking and not chat, assistant, and agent under other names.
3. For each row you write the level of the work and the level of review you actually gave.
4. The risk is never the level itself but the gap between the level of the work and the level of the review.
5. The book cites Parasuraman and Manzey (2010) for the finding that monitoring falls as automation looks more reliable, so you start with the row where your review was lightest and ask whether its output was also the most polished.

**Source:** Conducting AI
