# Chapter 3: Chat, assistant, and agent

## ES-ch03.1

A user tells an AI system, "Fix this report." In one run the system lists which paragraphs should change. In a second run it reads the report file and returns a rewritten version in the chat window. In a third run it overwrites the report file with a rewritten version. All three closing messages are polished prose and nearly identical in tone. Explain what each run did in terms of stored state, why the closing messages cannot tell you which run happened, and what evidence would.

**Points:** 5

**Rubric (1 point each):**

1. The first run gives advice only; it changes nothing, and a person must still decide whether and how to apply it.
2. The second run reads the source and offers a revision that exists only as text in the conversation, so it is a proposal and the stored report is unchanged.
3. The third run mutates stored state, creating a persistent before and after that outlasts the conversation.
4. Closing prose is produced fluently whatever operation took place, so its wording or polish cannot identify the run, and narration is not evidence that an action happened.
5. Evidence has to follow the object being claimed about: a before-and-after comparison of the file (diff or hash) or a runtime record of the write is needed to support "the report was changed".

**Source:** Opening scenarios

## ES-ch03.2

An assistant is asked to summarize a folder of documents without changing any file. It reads the documents, writes an excellent summary, and then also saves a cleaned-up version over one of the originals, because a file-writing tool was available. Explain why this counts as a failure even if the cleaned-up text is better, and name the decision that was never made.

**Points:** 5

**Rubric (1 point each):**

1. The overwrite is outside the requested task; a better result does not move an action inside the scope that was asked for.
2. The request set a boundary (do not change files) in addition to an outcome (a summary), so the run met the outcome and broke the boundary.
3. Nobody decided that the system could write; the ability arrived because the tool was enabled, not through a decision.
4. A good outcome and an authorized action are separate judgments, and only the first was ever made.
5. Granting only the capabilities the task requires (read, not write) would have made the overwrite impossible, and a written boundary with a check of the files afterward would have caught it.

**Source:** Opening scenarios

## ES-ch03.3

The request "fix this report" hides at least four different requests: explain what is wrong, propose a replacement, save a new version, or alter the original. Describe how these differ in their consequences for stored state, say what happens if the requester does not specify, and evaluate the claim "text output is harmless, file changes are dangerous".

**Points:** 5

**Rubric (1 point each):**

1. Explaining and proposing leave stored state untouched; saving a new version adds a file; altering the original replaces the previous state in place.
2. The four readings differ in reversibility, since overwriting removes the before state while a new file leaves the original available for comparison and rollback.
3. If the requester does not say which reading is meant, the system resolves the ambiguity itself, possibly choosing the most consequential reading, so scope should be stated or clarified.
4. The claim is too simple because text can steer a decision (what is believed, cut or approved), so lack of a state change does not make an output inert.
5. A file edit can be trivial and fully authorized, so the useful distinction is operational: whether stored state changes and whether that change can be checked separately.

**Source:** A response and a file are different kinds of result

## ES-ch03.4

Four interfaces declare these capability sets: A = {reason}, B = {reason, read}, C = {reason, read, write}, D = {reason, read, write, send_email}. Task 1 requires {read}. Task 2 requires {read, write}. Task 3 requires {read, write, send_email}. For each task, give the missing set (required minus declared) for interface B and for interface C, and name the smallest interface that covers it. Then explain what an empty missing set does and does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Task 1: the missing set is empty for both B and C, and B is the smallest interface that covers it.
2. Task 2: the missing set is {write} for B and empty for C, so C is the smallest interface that covers it.
3. Task 3: the missing set is {send_email, write} for B and {send_email} for C, so D is the smallest interface that covers it.
4. An empty missing set means the declared capabilities cover the declared requirements, and nothing more.
5. It does not show that the target may be used, that the declaration matches the real runtime, that the task description is complete, or that the action is authorized.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.5

A function is defined as follows.

    def missing(surface_caps, required):
        return sorted(set(required) - set(surface_caps))

Explain what it returns for missing({"reason", "read"}, ["read", "read", "write", "deploy"]), why each step of the code is there, and what the function does not validate or establish.

**Points:** 5

**Rubric (1 point each):**

1. The result is ["deploy", "write"]: duplicates are removed, the declared set is subtracted, and what remains is reported.
2. Converting the requirements to a set removes duplicate labels and makes subtraction a membership question, adding no information about the task.
3. Sorting only gives a stable, readable order and does not change which capabilities are reported.
4. The function does not validate requirement labels, so an unfamiliar label such as deploy stays in the missing set, which signals "not covered" and is a different policy from rejecting unknown input.
5. The result only compares declared sets; it does not check the real runtime's permissions, the completeness of the task description or authorization, so a correct subtraction can sit on wrong inputs.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.6

A design models three interfaces as nested capability sets, each containing the one before: {reason} inside {reason, read} inside {reason, read, write}. Explain what the nesting buys, what assumption it rests on, and where real systems can break it.

**Points:** 5

**Rubric (1 point each):**

1. Nesting gives an order: any task covered by a smaller set is covered by every larger one, which makes the choice of the smallest sufficient interface a simple comparison.
2. The nesting is a design convenience in a teaching model and not a fact about real products.
3. Real systems can hold capabilities that fit no single ladder, such as an append-only logger that can write but not read, or a search tool without file access.
4. Within the model the categories are coarse: read and write say nothing about which files, accounts or fields, so scope is outside what the sets can express.
5. Labels such as chat, assistant and agent should therefore be treated as handles for explicit capability sets that must be checked in the actual runtime, not as universal product definitions.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.7

A team needs an AI system to read one policy document and produce a summary whose claims can be checked against that document. A senior engineer says: "Just give it the full agent setup with file writes; it's the most capable, so it can't go wrong." Argue for a different grant, and describe one case where the smaller grant would be the wrong choice.

**Points:** 5

**Rubric (1 point each):**

1. The task requires reading and reasoning only, so a read-only grant covers it and a write capability adds an operation the task does not need.
2. The reason to prefer the smaller grant is not distrust of the system; it is that each extra operation is another thing that must be checked afterward.
3. This applies the least-privilege principle: grant what the task needs and no more.
4. A larger grant also widens the damage from errors, misuse or injected instructions in the document.
5. Smaller is not automatically better: if the task requires a saved output file, a read-only grant cannot finish it, and the right grant is the one sufficient for the outcome, with the scope re-authorized if it changes.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.8

A team will let an AI system read a folder of customer tickets and draft replies that a human will send. Write the grant specification the team should record before giving the system any access, naming the fields it should contain and filling them in for this task.

**Points:** 5

**Rubric (1 point each):**

1. Outcome and required capabilities: draft replies grounded in the tickets, which needs reading and text generation but not sending.
2. Granted capabilities with nothing wider, and an explicit list of refused operations such as sending messages or editing or deleting tickets.
3. An authorized target: the specific folder of tickets and the specific location where drafts are placed.
4. A condition that returns control to a person, such as the system proposing to send a reply, touching other data, or the request changing.
5. Evidence the reviewer will read and a pass condition that can fail, such as no send operation in the runtime record and a draft that traces to ticket content.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.9

Explain why a grant specification whose pass condition cannot fail is described as a wish rather than a control, and give an example of a plausible but weak specification and how you would repair it.

**Points:** 5

**Rubric (1 point each):**

1. A control must be able to be contradicted by some outcome; a pass condition that every outcome satisfies tests nothing.
2. A condition is testable only if it names an observable event or state, such as the absence of a write operation or an unchanged file hash.
3. A weak specification grants the widest available interface because the user wants help, and names no operation or target that would ever be refused.
4. The repair names the minimal operations needed, the operations refused and the single authorized target.
5. The repair also adds a condition that sends control back to a person and a named piece of evidence that would show a violation.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.10

People speak of an AI system's "autonomy" as a single quantity. Break it into separate dimensions, define each, and show with an example why a recommendation of "use an agent" says too little.

**Points:** 5

**Rubric (1 point each):**

1. Capability: what the system is able to do, such as reading, writing, sending or executing.
2. Control: who or what chooses the next step, a predefined program or the model itself.
3. Scrutiny: how hard the output must be checked, which depends on the work and its stakes and not only on the permissions.
4. The dimensions vary independently: a fixed pipeline can write files while a model-directed process may only read, and the same permissions can accompany both a trivial and a high-stakes task.
5. "Use an agent" leaves all three unspecified, so a good recommendation states the capability set, who directs the process, and what review the output will receive.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.11

Explain the distinction between a workflow and an agent as used in published guidance on building LLM applications. Describe one fixed workflow that writes to storage and one model-directed process that never writes, and say why a classifier that looks only at whether a write occurred cannot tell them apart.

**Points:** 5

**Rubric (1 point each):**

1. In a workflow, models and tools are orchestrated through predefined code paths chosen by the developer.
2. In an agent, the model dynamically directs its own process and tool use, deciding the next step and when to stop.
3. A fixed pipeline that extracts fields, validates them and inserts them into a database is a workflow that writes.
4. A research loop that chooses its own searches and reads results but has no write tool is model-directed without writing.
5. A write-based classifier measures capability (a write occurred) and ignores control, so it would label the first by its write and the second as a reader; the two axes need to be reported separately.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.12

A reviewer can carefully check 15 actions per hour and has 3 hours a day for review. An agent produces 40 actions per run and runs 6 times a day. Compute how many actions are produced and how many can be carefully checked per day, what fraction that is, and what the fraction becomes if the agent's output doubles. Then describe two design responses.

**Points:** 5

**Rubric (1 point each):**

1. The agent produces 240 actions per day (40 times 6) and the reviewer can check 45 per day (15 times 3).
2. The checkable fraction is 45 divided by 240, which is about 18.75%.
3. If output doubles to 480 actions with the same reviewer, the fraction falls to about 9.4%, because review capacity does not scale with generation.
4. One design response is to narrow the grant so there are fewer consequential actions to check, or to require approval only for irreversible or high-impact operations.
5. Another is to add automated or sampled checks against independent evidence and to size the grant to what a person can actually verify.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.13

Explain the difference between a declared capability set and a recorded event trace, and why a reviewer needs both. Use the example of an interface declared to have read and write capabilities whose record for a particular run lists only reason and read events.

**Points:** 5

**Rubric (1 point each):**

1. A capability set describes what a surface is declared able to do; an event trace describes what is recorded as having happened in one run.
2. The relation resembles that between a population and a sample: one shows what is available, the other a particular run.
3. For the example run, the record is consistent with no write having occurred, but the declared write capability does not show that one did.
4. The record does not prove that the system lacked the write capability, only that none was recorded in that run.
5. Whether the record is complete cannot be answered by the record itself, so the way events are captured needs separate scrutiny.

**Source:** Events, not labels: what the record can show

## ES-ch03.14

A function labels a run from its list of recorded events: "agent" if a write appears, otherwise "assistant" if a read appears, otherwise "chat"; unknown events raise an error. Explain what the label discards, and design two pairs of runs that receive the same label but call for different judgments.

**Points:** 5

**Rubric (1 point each):**

1. The label ignores order, so a read before a write and a write before a read are indistinguishable.
2. It ignores repetition, so one write and many writes receive the same label.
3. It records no target, so a write to a scratch file and an overwrite of an original document look alike.
4. It does not show whether an operation succeeded or whether it was authorized; the event is only a name.
5. A good pair would be, for example, a scratch write versus an overwrite of the source, or a single email versus three emails, with the full trace kept beside the label as the evidence.

**Source:** Events, not labels: what the record can show

## ES-ch03.15

You are redesigning an event record for an agent so that reviewers can judge what happened. Propose the fields you would add beyond an operation name, explain how they improve review, and state what the richer record still cannot establish.

**Points:** 5

**Rubric (1 point each):**

1. Add the target of each operation, so a write to a scratch file can be told from an overwrite of an original.
2. Add the status (proposed, attempted, completed) and the result reported by the runtime, so success is not assumed.
3. Add ordering, timestamps and the identity of the party that approved the operation, so sequence and authority can be reviewed.
4. Add references to independent state evidence such as before-and-after hashes, so claims can be checked against the object.
5. More fields do not make their contents true: the record is only as sound as its producer and recording boundary, and authorization and quality remain human judgments.

**Source:** Events, not labels: what the record can show

## ES-ch03.16

Four descriptions of one agent run are available: the product's label ("autonomous agent"), the agent's own narration ("I saved the file"), the harness's event trace, and a before-and-after comparison of the file's content run by a separate script. Rank them by how much independent support each gives to the claim "the file changed", and explain what each can and cannot support.

**Points:** 5

**Rubric (1 point each):**

1. The product label comes from someone else's naming and supports at most a guess about what to expect, nothing about this run.
2. The narration supports only that something was said; it is the actor's account of itself and can be wrong or invented.
3. The event trace supports that an operation was recorded if the recording is sound, but not its target, success or authority unless those are recorded.
4. The separate before-and-after comparison is the strongest because it reads the state itself and can fail differently from the other three, for instance showing no change when the narration said saved.
5. Even the state comparison shows that something changed, not who did it or whether it was authorized; for any record, ask whether it was produced by the thing that acted or by something that watched.

**Source:** Events, not labels: what the record can show

## ES-ch03.17

An agent reports "I saved the changes to config.yaml." The harness log has a line recording a write request for config.yaml. A hash of config.yaml taken before the run and one taken after are identical. List at least three explanations consistent with all three facts and say how you would investigate.

**Points:** 5

**Rubric (1 point each):**

1. The write failed or was rejected by the runtime, so the request was attempted but never completed.
2. The write went to a different path or a copy, so config.yaml itself was never touched.
3. The write replaced the file with identical content, or another process restored it afterward, so the final hash matches.
4. The narration and the log are accounts by the actor and the harness, while the hash comparison reads the state, so the comparison outranks them as evidence about the file.
5. Investigation steps: read the runtime's return value for the write, look for other changed files or paths, check timestamps and version control history, and confirm how the hash was computed.

**Source:** Events, not labels: what the record can show

## ES-ch03.18

An agent harness records these items about an attempt to save a summary. (a) The assistant's message: "I can save this as summary.md if you like." (b) A log line: write_file(summary.md) requested. (c) A log line: write_file returned ok. (d) An engineer lists the directory and sees summary.md with the expected size. Name the status each item supports, and write the sentence a careful report may say if only (a) exists, only (a) and (b) exist, and all four exist.

**Points:** 5

**Rubric (1 point each):**

1. Item (a) supports proposed: it is an offer in prose and nothing was requested of the runtime.
2. Item (b) supports attempted: the operation was requested of the runtime, with no outcome known.
3. Item (c) supports completed, meaning the runtime reported success, which is the actor's side of the record.
4. Item (d) supports observed: someone who watched saw the changed state, which is stronger evidence than the runtime's report.
5. The report should use the verb that matches the evidence: "proposed" with only (a), "attempted" with (a) and (b), and "created and observed" only with (d), without upgrading a proposal to a completed action.

**Source:** Events, not labels: what the record can show

## ES-ch03.19

An assistant's tool can write anywhere on a shared drive, and a comparison of required against declared capabilities for the task "rename the files in /drafts" shows nothing missing. Explain why the task is still not authorized by that result, and what a proper authorization contains.

**Points:** 5

**Rubric (1 point each):**

1. The comparison only tests whether declared capabilities cover declared requirements; it takes no input about ownership, consent or permission.
2. A broad capability (writing anywhere) is not permission to modify every target, so the grant must be scoped to /drafts.
3. A proper authorization names the operation (rename), the target (files in /drafts) and the conditions or time under which it applies.
4. Authority is a decision with a record made by an accountable person; the model may propose an action but cannot supply the authorization.
5. A vague permission to "help with the files" should not quietly expand to unrelated changes, and anything outside the named scope should return control to a person.

**Source:** Capability does not confer authority

## ES-ch03.20

A read-only chat tool cannot write files. Someone concludes: "So a write would have been forbidden here." Another says: "A tool's permission screen showed 'allowed', so the action was useful." Explain what is wrong with each inference.

**Points:** 5

**Rubric (1 point each):**

1. A tool's inability to write shows only that it cannot cover a write requirement; it is a statement about feasibility.
2. It does not show that a write would have been prohibited if another authorized tool had performed it, because feasibility and permission answer different questions.
3. Treating a technical limit as a policy judgment lets a limitation pass as a decision that nobody made.
4. A permission being granted shows only that someone allowed the action; it says nothing about whether the action is useful or well designed.
5. Proposed action, authority, execution and quality review are four distinguishable things, and one approval or capability flag is not a certificate for all of them.

**Source:** Capability does not confer authority

## ES-ch03.21

An engineer clicks "Approve" on a prompt asking whether an AI system may apply a patch it proposed. Explain which questions that click answers and which it leaves open, and describe the evidence needed for each.

**Points:** 5

**Rubric (1 point each):**

1. The click addresses authority: a named person allowed a specific operation on a specific target.
2. It does not show that the patch is correct or good; quality needs review of the patch, tests and checks against requirements.
3. It does not show that the patch was applied as proposed; execution needs a runtime result or an observed change in the code.
4. It does not show that the target matched what the engineer thought they were approving, which is why the prompt should display operation and target.
5. Keeping proposal, authority, execution and quality review separate lets each fail independently and be examined independently.

**Source:** Capability does not confer authority

## ES-ch03.22

A test harness for an AI agent answers "approved" to every permission request so that control flow can be tested. Explain when this is legitimate, what a report must say about it, and why inventing an approver's name would be a serious fault.

**Points:** 5

**Rubric (1 point each):**

1. Using an auto-approver to exercise the control flow is a legitimate test technique, because the test concerns what the system does after approval.
2. The run and the permission evidence must be labelled as simulated so no reader mistakes it for a person's decision.
3. An auto-approver replies instantly and nobody has weighed the action, so its approval is not consent and does not satisfy an accountability requirement.
4. Writing a plausible human name invents evidence and falsifies the record, whatever the intention.
5. Where permission evidence is absent, the report should say absent or pending so the gap remains visible.

**Source:** Capability does not confer authority

## ES-ch03.23

A specification says: a write anywhere in an event list gives "agent"; a read and no write gives "assistant"; otherwise "chat"; an unknown event name must raise an error. Describe two plausible wrong implementations, the smallest test case that exposes each, and why a suite of happy-path cases can pass all of them.

**Points:** 5

**Rubric (1 point each):**

1. One wrong version labels by the final event only; the list [write, reason] exposes it, because the specification says "agent" and it would say "chat".
2. A second wrong version treats an unknown event name as harmless reasoning; a list containing an unknown name exposes it by expecting an error.
3. A third wrong version tests for a read before testing for a write, so any list containing both is labelled "assistant"; a case that contains both a read and a write exposes it.
4. A happy-path suite whose only mixed case ends in a write, such as [reason, read, write], cannot separate the real rule from the final-event rule, so it can pass wrong versions.
5. A suite is evidence only to the extent that it could have failed; if the tests cannot tell a wrong version from the right one, the specification and tests are not finished.

**Source:** Build It: your own classifier, then the second half of the gate

## ES-ch03.24

A team lead says: "Our classifier throws an error on any unknown event name, so our agent can't perform unrecorded or dangerous operations." Evaluate this statement and describe what must be designed separately before anyone can rely on the trace.

**Points:** 5

**Rubric (1 point each):**

1. Validating a vocabulary checks names in a list; it does not check what the operating system or runtime actually did.
2. A program can perform an operation and leave it out of the list, so the classifier cannot detect unrecorded actions.
3. Rejecting an event called delete_everything does not prevent deletion in a real runtime; it only refuses a string.
4. A system that relies on a trace needs a recording boundary whose design and integrity are examined separately, such as a harness that logs every call itself.
5. Real enforcement requires permission checks at the point of execution, and an independent state check to catch operations that escaped the record.

**Source:** Build It: your own classifier, then the second half of the gate

## ES-ch03.25

A developer has written a specification and tests for a small function and wants an AI coding assistant to implement it. Describe what the developer should hand over, what they should do with the result, and how failures should be used.

**Points:** 5

**Rubric (1 point each):**

1. Provide the specification and the tests, not the developer's own implementation, so the comparison between the two stays informative.
2. Run the tests yourself rather than relying on the assistant's report that they pass, because that report is narration.
3. Compare the result with your own baseline implementation and name a behavior where they differ, either a boundary the assistant handled that you missed or one it ignored.
4. A failing test often marks a gap in the specification, since the assistant can only act on what was written and unstated behavior is its free choice.
5. Ask the assistant for a deliberately wrong version that still passes your tests; if it succeeds, the tests were too weak.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.26

Design an experiment that compares how one small task is handled by a plain chat, a chat with an uploaded source, and a coding agent in a throwaway repository. State what you would record, how you would handle interfaces you cannot run, and what conclusions you could not draw.

**Points:** 5

**Rubric (1 point each):**

1. Write the task's grant first: required and granted capabilities, authorized target and what is refused.
2. Record for each setup the interface, the available operations and permission settings actually used, and how the source reached the model (pasted, attached, or read by a tool).
3. Capture evidence of state, such as files before and after, and keep proposed actions apart from executed ones.
4. Mark any setup that cannot be run as not run, and label any constructed trace as constructed; do not manufacture results.
5. Do not conclude that one product is universally better or safer, or that observed capabilities are permanent, since the evidence covers only these runs under these assumptions.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.27

A report includes some event traces that were recorded from real runs and some that the report's writer composed by hand to illustrate a point. Explain why these must be labelled differently, and describe what an honest mix looks like.

**Points:** 5

**Rubric (1 point each):**

1. A recorded trace is evidence of what happened in a run, while a constructed trace is a reasoning aid that shows what a rule would do.
2. Presenting a constructed trace as recorded misleads the reader about what was observed.
3. Each trace should carry its provenance explicitly, such as observed, derived from code by inspection, or hypothetical.
4. An honest mix is usable because the labels let the reader weigh each piece correctly, while an invented completion is not.
5. Code reasoning and executed runs both teach, but only an executed run is an observation, and the report should keep the two distinct.

**Source:** Use It: conduct Claude Code, then compare interfaces

## ES-ch03.28

You must sign off on a comparison that says an AI system's contract summary was reliable. Your evidence is a harness event record and one before-and-after check of the contract file. Write the key elements of an honest sign-off and explain how you would handle claims you cannot support.

**Points:** 5

**Rubric (1 point each):**

1. State what was checked and how: the event record and the file comparison, and whether by hand, by a script you wrote or with an assistant's help.
2. State what was not checked: that the summary is faithful to the contract, that the record was complete, and any interface not run.
3. State what is not being claimed, such as that any system is safe or that a label proves a permission.
4. Use verbs that match the evidence (recorded, observed, computed, tested), and treat a claim of authorization as needing an identifiable approver and a specific operation.
5. If the record does not support the claim, narrow it or withhold the signature, which is an honest result, and note which parts the assistant contributed.

**Source:** Ship It: the action-surface comparison

## ES-ch03.29

Describe a sensible division of labor between a person and an AI assistant on a task that sets up and audits an agent's permissions. For each of these five tasks say who should do it and why: saying what the task requires, computing missing sets, implementing a classifier from a specification, checking what happened, and authorizing a write.

**Points:** 5

**Rubric (1 point each):**

1. Saying what the task requires: the person chooses scope because the meaning of the request lives in their situation, and the assistant can list readings or ask what "fix" means.
2. Computing missing sets: the assistant can compute instantly, but the person should predict first so the output can be judged.
3. Implementing from a specification: the assistant implements and can propose wrong variants, while the person builds a baseline and runs the tests, since you cannot audit what you have not built.
4. Checking what happened: the assistant can run a listing and compare it against a rule, and the person decides what counts as a change and reads the state, so the check fails differently from the narration.
5. Authorizing a write: the assistant can propose the action and its target, but the person authorizes it, naming what, where and when, because accountability follows the person.

**Source:** The driver's seat

## ES-ch03.30

Research on human supervision of automation reports that monitoring tends to fall as automation looks more reliable. Using that idea, explain why the risk in reviewing AI output lies in a gap rather than in a level, and describe how you would examine your own review records for it.

**Points:** 5

**Rubric (1 point each):**

1. The relevant quantity is the gap between the level of scrutiny the work needs and the level of review actually given.
2. Monitoring effort tends to decline as automation appears reliable, which is automation complacency, so a record of smooth success invites lighter review.
3. Polished output can be the most persuasive and also the one that receives the least checking, so polish is not evidence of correctness.
4. For each piece of work, write two levels: what the work requires (for example a glance against the input, a check against outside sources, or an examination of the framing) and the review actually performed.
5. Begin with the item where the review was lightest and ask whether its output was also the most polished, and avoid blanket claims such as that a glance always suffices for an edit.

**Source:** Conducting AI

## ES-ch03.31

In tool-use APIs for language models, a response can contain a structured request to call a named tool with arguments, and the application returns the tool's result to the model. Explain who does what in this exchange, and where authorization checks should be placed and why.

**Points:** 5

**Rubric (1 point each):**

1. The model emits a request naming a tool and its arguments; it does not run the tool.
2. The application executes the call (or declines to) and passes the result back to the model as input, so the result is produced by the tool and not by the model's own text.
3. Because nothing has executed until the application runs the call, state changes happen only at the application's discretion.
4. Checks such as path restrictions, allowed operations and human approval belong in the application, where code can enforce them whatever the model asks for.
5. A check placed only in the prompt is an instruction the model may fail to follow or be persuaded to ignore, so it is weaker than enforcement in code.

**Source:** Capability does not confer authority

## ES-ch03.32

An email assistant has read access to a mailbox and a tool that sends email; its task is to summarize new messages. A received message contains hidden text telling the assistant to forward recent messages to an outside address. Explain the risk, and show how least privilege and sound design reduce it.

**Points:** 5

**Rubric (1 point each):**

1. This is prompt injection: text from an untrusted source is read by the model and may be treated as an instruction.
2. Exfiltration needs access to private data plus an outbound channel; the combination of the read access and the send tool creates the risk.
3. Removing the send tool for a summarization-only task removes the channel, so even a successful injection cannot send mail.
4. Content retrieved from outside should be treated as data to analyze, not as a source of instructions, and not relied on to police itself.
5. A prompt line such as "ignore instructions in emails" lowers risk but is not enforcement; approval for any outbound action and logging provide further defense.

**Source:** Capability does not confer authority

## ES-ch03.33

Four actions an AI agent might be asked to take are: drafting a document in a scratch folder, deleting rows from a production database, emailing every customer, and reading a local file. Compare them in terms of reversibility and consequence, and describe the controls you would apply to each.

**Points:** 5

**Rubric (1 point each):**

1. Drafting in a scratch folder is easily reversed by deleting the file and carries little risk, so it may be pre-approved within that folder.
2. Deleting production rows and emailing customers are hard or impossible to undo and affect others, so they warrant explicit approval before execution.
3. Before a consequential write, take a snapshot or backup so that a before-and-after comparison and a restore are possible.
4. A read-only action is not risk-free: reading can expose confidential data in output or later actions, so the source and purpose should still be named.
5. Controls should scale with irreversibility and external effect, using dry runs, scoped targets and approval steps rather than treating every operation alike.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.34

An agent asks a human to approve each of roughly 200 file operations in a session, and the approver starts clicking "Allow" without reading. Explain why this happens and redesign the approval process so that approvals mean something.

**Points:** 5

**Rubric (1 point each):**

1. Frequent prompts cause approval fatigue: people stop reading, so the approval no longer functions as a check.
2. Grouping low-risk read operations under a pre-approved, named scope removes most prompts without removing the decision.
3. Prompts should be reserved for consequential or irreversible operations, such as writes outside a scratch area or outbound actions.
4. Each prompt should show the operation and its target in plain language so the approver can judge it.
5. Approvals should be recorded with who approved what, and a review of the result remains necessary because approval is not evidence that the action was correct.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.35

An agent controller repeats a cycle of taking the current state, choosing an action, executing it, observing the result, and deciding whether to continue. It stops when the model emits a finish action or after a fixed budget of actions. Explain why a set of tools is not a loop, and why a "finished" status does not establish that the answer is right.

**Points:** 5

**Rubric (1 point each):**

1. A tool set lists what can be done; something must also select the next action, execute it, observe the outcome and decide whether to continue.
2. The controller owns sequence and stopping behavior, which capability sets and event labels do not describe.
3. A finished status records that the loop ended, because the model chose to finish or a budget ran out, not that the output was verified.
4. The model can emit finish after a wrong answer, so correctness needs a separate check against sources or a reference.
5. A fixed action budget bounds the number of steps whatever the model decides, but it does not make the steps correct, and authority boundaries and source checks are still required.

**Source:** The next operation needs a controller

## ES-ch03.36

You are designing the stopping rules for an autonomous agent that works through a task by repeatedly calling tools. List the stops you would build into the controller, explain which belong to the controller rather than to the model, and say how the final status should be reported.

**Points:** 5

**Rubric (1 point each):**

1. A hard cap on the number of actions or amount of spend, enforced by the controller, so a loop cannot run unbounded whatever the model decides.
2. A time or cost limit and detection of repeated or stalled actions, so a loop that makes no progress is stopped.
3. A stop when an action falls outside the granted scope, handing control back to a person instead of letting the model continue.
4. The model can request to finish, but acceptance of that request, and any checks on the result, should be decided by the controller or a person.
5. The final status should distinguish finished by the model, stopped by a budget and stopped by a scope violation, and should not imply that any of them verified correctness.

**Source:** The next operation needs a controller

## ES-ch03.37

A status report states: "The agent safely updated the configuration and verified the change; everything passed." The evidence consists of the agent's closing message saying it had updated and checked the file, and a harness log line recording a write request. There is no comparison of the file's state. Rewrite the report's claims at the strength the evidence supports, and explain each change.

**Points:** 5

**Rubric (1 point each):**

1. "Safely" is an unsupported judgment, since nothing in the evidence shows that the action stayed in scope or that the change was appropriate.
2. "Updated" should become "attempted" or "reported as completed by the agent", because only a request was logged and the narration is the actor's own account.
3. "Verified" should be dropped or attributed: the agent's own statement of verification is not independent checking.
4. "Everything passed" should name what was run and by whom, or be removed if no such record exists.
5. The report should state what would be needed to strengthen it, such as a before-and-after state comparison and the runtime's return value for the write.

**Source:** Events, not labels: what the record can show

## ES-ch03.38

A reviewer wants to follow a single claim in a report back to its basis. Describe the chain a well-built record should let them follow from the task to the claim, and what is lost when a link is missing.

**Points:** 5

**Rubric (1 point each):**

1. The task and the requested outcome, including any boundary such as "do not alter the source", are stated first.
2. The grant follows from the task: what capabilities were required, which were granted, and which operations were refused.
3. The record shows what was proposed, attempted, completed and observed, with the permission evidence for any state change.
4. The claim is then stated with a verb that matches the record and with a note of what was not checked.
5. If a link is missing, such as no permission evidence or no state check, the claim has to be narrowed or marked absent or pending, because a reader cannot recover the missing step.

**Source:** Ship It: the action-surface comparison

## ES-ch03.39

After seeing an assistant's summary of a document it was allowed only to read, the user asks, "Great, now also fix the typos in the source file." Explain what has changed, why the earlier authorization does not cover it, and how the record should handle it.

**Points:** 5

**Rubric (1 point each):**

1. The new request adds a write operation on the source, which is a change of scope and not a continuation of the original task.
2. The earlier grant named reading that file, so the new operation was never authorized and a good first result does not extend it.
3. The person should revise the grant to name the operation (edit), the target (that file) and the conditions, and authorize it explicitly.
4. The revised grant should be dated and the earlier version kept, so the record shows what was decided at each point.
5. Because a write creates a before and after, take a snapshot of the file first and check the result against it afterward.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.40

Design an audit log for an AI agent's actions so that a later reviewer can rely on it. State who or what should write the log, what each entry should contain, and what protections the log needs.

**Points:** 5

**Rubric (1 point each):**

1. The log should be written by the harness or runtime that executes the calls, not by the model as part of its reply, so it is independent of the model's account.
2. Each entry should record the operation, its target and arguments, the time, who or what approved it, and the result returned by the runtime.
3. The log should be append-only or tamper-evident, so after-the-fact editing is hard to hide.
4. Entries should include denied and failed attempts as well as successes, since refusals are evidence of the boundary working.
5. A log is still a record and not proof of completeness: absence of an entry is weak evidence, so important claims also need an independent state check.

**Source:** Events, not labels: what the record can show

## ES-ch03.41

Explain the principle that the system that acted should not be the sole verifier of its own action. Give two examples of verification that are independent of the agent and two that look independent but are not.

**Points:** 5

**Rubric (1 point each):**

1. Independence means the check can fail differently from the account being checked, so it can contradict the narration.
2. Independent: a script run by the reviewer that lists or hashes the real files before and after the run, compared against a rule written in advance.
3. Independent: a harness log written by the runtime that executes the calls, or a version-control diff of the affected files.
4. Looks independent but is not: asking the same model whether its edit worked, which shares the failure modes of the account being checked.
5. Looks independent but is not: a second model instance that reads only the first model's narration, which has no more access to the state than the first did.

**Source:** Events, not labels: what the record can show

## ES-ch03.42

A company asks you to recommend how to set up an AI system to answer questions from a set of internal policy documents and, when asked, save a short summary file to a shared folder. A colleague proposes: "Use an agent." Write a recommendation that is more useful than that, covering the dimensions that should be decided.

**Points:** 5

**Rubric (1 point each):**

1. Capability: read access to the policy documents and write access limited to the one summary location, with no other operations granted.
2. Control: whether a fixed workflow suffices (retrieve, answer, save) or the model must choose steps, preferring the simpler option unless it demonstrably falls short.
3. Scrutiny: who checks answers against the source documents and how heavily, given the stakes of policy answers.
4. Authorization and evidence: who authorizes the save, what target is named, and which record and file comparison show what happened.
5. The recommendation is stated under its assumptions and does not claim that any product is universally better or safer.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.43

A manager writes "clean up the quarterly report" and gets back an unexpected outcome. Describe how the request could have been written, or how the system could have responded, to avoid a wrong reading of the intended scope.

**Points:** 5

**Rubric (1 point each):**

1. State the type of result wanted: an explanation of problems, a proposed rewrite, a new saved version, or an in-place change.
2. State the boundary, such as whether the original may be changed, and the single target that is in scope.
3. State what should send control back, such as a proposal to save anything or to touch another file.
4. A well-behaved system should ask a clarifying question when several readings differ in consequence, instead of choosing the most consequential one.
5. A saved separate draft that the system offers is a proposed change of scope for the person to evaluate, not something the original request already included.

**Source:** A response and a file are different kinds of result

## ES-ch03.44

An assistant can answer questions about a document in three ways: the user pastes the text into the chat, the user attaches the file through the interface, or the assistant calls a file-reading tool. Explain why a summary produced by each route may look the same and what record each leaves, and why it matters when you claim the document was read.

**Points:** 5

**Rubric (1 point each):**

1. A model can use text already in its context without any new read operation, so an informed-sounding answer does not prove a read took place.
2. Pasting leaves the text in the conversation transcript and no tool call.
3. Attaching leaves a record in the interface of what was supplied, which depends on that product's handling of files.
4. A tool read leaves a recorded read operation naming the target, which is the most direct evidence that a read occurred.
5. A claim should state which route was used and what evidence shows it, and a symbolic trace should be an explicit abstraction of the actual record and not a guess.

**Source:** A response and a file are different kinds of result

## ES-ch03.45

A specification for a summarizing task says "no writes". During the run the tool creates a temporary cache file and writes a log entry. Discuss how the specification should be clarified, why this kind of edge case should be found before the grant, and how it affects the pass condition.

**Points:** 5

**Rubric (1 point each):**

1. The specification should say whether caches, temporary files and logs count as writes, because in the plain sense they are.
2. If they are permitted, the specification should name a location for them, so the permission stays tied to a target.
3. Finding the edge case before the grant turns it into a rule, while finding it afterward turns it into a dispute.
4. The pass condition should be stated so it can fail, such as "no write outside the named scratch location and the source file unchanged".
5. An assistant can help hunt for such cases, but the decision on which writes are acceptable belongs to the person writing the specification.

**Source:** Capability does not confer authority

## ES-ch03.46

Product A is marketed as an "Agent" but runs in a sandbox that permits only reading. Product B is marketed as an "Assistant" and has shell access with write permission. Explain what a team should do instead of choosing by name, and what limits apply to the capability facts they collect.

**Points:** 5

**Rubric (1 point each):**

1. Names do not reliably indicate capabilities; they are labels chosen by someone else and can mislead in either direction.
2. The team should list the operations actually enabled in the specific runtime, with the permission settings in force, and compare them with the task's requirements.
3. Product A's sandbox means it cannot satisfy a write requirement despite its name, and Product B's shell access means it can write despite its name.
4. The capability facts hold for the version and settings observed, so they should be recorded with the date and not assumed to be permanent product specifications.
5. Even accurate capability facts do not settle authorization, control or the scrutiny required, which are separate decisions.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.47

A manager claims: "AI agents are riskier than chat assistants." Evaluate the claim: say what it gets right, what it hides, and what factors actually determine the risk of a deployment.

**Points:** 5

**Rubric (1 point each):**

1. The claim is partly right because systems that can act on external state can cause consequences that a response-only system cannot.
2. It hides that a response-only system can still mislead a decision, leak data in its output or be steered by untrusted content.
3. Risk depends on capability: which operations are enabled, on which targets, and how reversible they are.
4. Risk depends on control and scrutiny: who chooses the steps, whether actions are bounded and approved, and how heavily outputs are reviewed for the stakes involved.
5. A read-only agent and a write-capable agent on the same task differ in risk, so the label alone predicts little.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.48

A trace labelled by presence of event types shows [read, write, write, write] for a run in which each write sent an email, and [read, write] for a run in which the single write sent one email. Explain what the label misses, what can go wrong when operations are retried, and how a better record or design would help.

**Points:** 5

**Rubric (1 point each):**

1. The label ignores repetition, so one email and three emails look the same, and the count has to come from the trace.
2. After an ambiguous failure, retrying a non-idempotent operation (sending a message, appending a line) can duplicate its side effects.
3. Idempotent operations such as setting a value to a fixed number can be retried safely, because repeating them leaves the same state.
4. An event name records that an operation was named, not that it was delivered or succeeded, so a count of events is not a count of effects.
5. Better design records the result of each attempt, uses idempotency keys or checks state before retrying, and keeps the full trace beside the label.

**Source:** Events, not labels: what the record can show

## ES-ch03.49

Workflow one records [write, read]: it saves a draft file and then reads it back to check it. Workflow two records [read, write]: it reads a source and then saves a summary. A presence-based labeler gives both the same label. Explain what the labeler cannot tell a reviewer about sequence, and give two judgments that depend on order.

**Points:** 5

**Rubric (1 point each):**

1. The labeler ignores order, so a read before a write and a write before a read look identical.
2. Order shows dependence: in workflow two the write could have used what the read returned, while in workflow one it could not.
3. A read after a write can be a verification step that checks what was actually stored, which is evidence that the labeler discards.
4. Order matters for side effects and for approvals, for example whether a check or an approval occurred before an irreversible action.
5. A reviewer should therefore keep the ordered trace and not rely on the label alone.

**Source:** Events, not labels: what the record can show

## ES-ch03.50

An AI agent is permitted to write only inside /work/out/. It receives a request to write to /work/out/../secrets.txt. Explain how a naive path check could allow the write, how to enforce the restriction properly, and why the restriction cannot live only in the agent's instructions.

**Points:** 5

**Rubric (1 point each):**

1. A check that tests whether the path string starts with "/work/out/" passes, even though the path resolves outside the folder.
2. The path should be normalized or resolved to its real location, including ".." segments and symbolic links, before it is compared with the allowed folder.
3. An allow list that refuses anything not explicitly permitted is safer than a deny list, which misses targets nobody anticipated.
4. The check must run in code that executes the operation, so it holds however the model's output is phrased.
5. An instruction in the prompt is a request to the model and not a constraint on the tool, so it cannot be the only control.

**Source:** Capability does not confer authority

## ES-ch03.51

Two components handle unfamiliar input differently. A labeler raises an error on an unknown event name, and a missing-capabilities function keeps an unknown requirement label in its result. Explain failing closed versus failing open, the reasoning behind each behavior here, and the cost of failing closed.

**Points:** 5

**Rubric (1 point each):**

1. Failing closed means refusing or flagging input the system does not understand, instead of allowing it to proceed.
2. Treating an unknown event as harmless would hide activity that might be a write, which is failing open.
3. Keeping an unknown requirement in the missing set reports the task as not covered, which is a cautious reading of something no one declared.
4. The two behaviors differ in mechanism, an error versus a flagged result, but both avoid silent acceptance.
5. Failing closed can block legitimate work until the vocabulary is updated, and that cost is accepted because an unchecked unknown operation costs more.

**Source:** Build It: your own classifier, then the second half of the gate

## ES-ch03.52

A developer writes tests for a classifier, then finds that one test fails against an AI assistant's implementation even though the assistant followed the written specification. Explain what this can indicate and what the developer should do.

**Points:** 5

**Rubric (1 point each):**

1. The assistant could act only on what was written, so the failing test may mark a behavior the developer assumed but never stated.
2. The developer should check whether the test or the specification is wrong before blaming the implementation.
3. If the specification was incomplete, the fix is to add the missing rule to the specification and then to the tests.
4. Writing the tests before reading the implementation matters, because tests written afterward tend to encode what the code does.
5. The developer should run the tests personally and not rely on the assistant's report that they passed.

**Source:** Build It: your own classifier, then the second half of the gate

## ES-ch03.53

Explain why the act of authorizing an action cannot be handed back to the system that wants to perform it, and what a legitimate approval needs to contain.

**Points:** 5

**Rubric (1 point each):**

1. The system that wants to act has a conflict of interest when deciding whether it may, which removes the check that approval is meant to provide.
2. A policy sentence or a promise by the actor is not a check by someone else.
3. A second model instance given the same context shares the same information and blind spots and carries no accountability.
4. Accountability follows the people whose files, data and names are affected, so an identifiable person must make the decision.
5. A legitimate approval names the operation, the target and the conditions, and is recorded with who decided and when.

**Source:** Capability does not confer authority

## ES-ch03.54

An assistant has read access to a folder of employee records and is asked to summarize recent project updates. Its declared capabilities cover the task. Identify the questions that remain open and why they cannot be answered by the capability comparison.

**Points:** 5

**Rubric (1 point each):**

1. Whether the contents may be sent to a third-party model or service depends on policy and consent, not on the tool's ability to read.
2. Whether the task needs personal data at all, and whether a narrower source could be named, is a scoping decision.
3. Whether the people in the records agreed to this use is a fact about people and cannot be derived from a capability set.
4. Even read-only access can expose confidential content in the output, so the output's destination matters.
5. The authorization should name the allowed source, the purpose and the output location, and be recorded by an accountable person.

**Source:** Capability does not confer authority

## ES-ch03.55

A script lists the names and sizes of files in a folder before and after an AI agent's run, and the two listings are identical. Evaluate what this does and does not show about whether the agent changed the files, and propose a stronger check.

**Points:** 5

**Rubric (1 point each):**

1. Identical names and sizes are consistent with no change but also with an overwrite by text of equal length, so content may have changed.
2. Comparing content hashes is stronger, because identical hashes mean identical content for the files covered.
3. Neither check sees changes outside the folder inspected or a change that was made and then restored.
4. A state check can show that something changed, not who did it or whether it was authorized.
5. Because a failed or blocked write attempt also leaves the folder unchanged, identical states do not show that no write was attempted; the runtime log addresses that.

**Source:** Events, not labels: what the record can show

## ES-ch03.56

An operations team audits a random sample of 30 of an agent's actions, drawn from a very large stream, and finds no violations. A manager says: "So the violation rate is zero." Explain what the sample does and does not show, give an approximate bound, and say what would be needed to support a much tighter claim.

**Points:** 5

**Rubric (1 point each):**

1. A sample cannot prove the rate is exactly zero; it can only bound the rate, and the bound depends on the sample size.
2. With zero violations in 30 random draws, an approximate 95% upper bound on the rate is about 10% by the rule of three (3 divided by 30), or about 9.5% exactly.
3. If the true rate were 5%, the chance of seeing no violations in 30 draws is about 21%, so a clean sample is weak evidence.
4. Tightening the bound to about 1% would need roughly 300 random draws with no violations.
5. The draw must be random; actions chosen by the agent or by convenience do not support the bound.

**Source:** Verify and reflect

## ES-ch03.57

Published guidance for building LLM applications advises finding the simplest solution that works and adding complexity only when needed. Explain what that means when choosing among a single model call, a fixed workflow and an autonomous agent, and the trade-offs of agents.

**Points:** 5

**Rubric (1 point each):**

1. Start with a single well-prompted call, possibly with retrieval, and add structure only when measured results show a gap.
2. Use a fixed workflow when the steps are known in advance, because it is more predictable, testable and cheaper than letting a model choose the steps.
3. Consider an agent for open-ended problems where the number and order of steps cannot be predicted.
4. Agents trade added latency and cost for flexibility, and errors can compound across steps.
5. Because of that autonomy, agents warrant testing in sandboxed environments and guardrails, with stopping conditions and human checkpoints.

**Source:** The gate: choose the autonomy before you grant the capability

## ES-ch03.58

A system has four possible capabilities: read, write, execute and network. A task requires read and execute. Count the possible capability sets, list those that cover the task, and explain what this implies about modeling interfaces as one nested ladder.

**Points:** 5

**Rubric (1 point each):**

1. There are 16 possible capability sets, since each of four capabilities is in or out (2 to the 4th power).
2. Exactly four sets cover the task: {read, execute}, {read, execute, write}, {read, execute, network}, and all four.
3. The smallest sufficient set is {read, execute}; adding write or network gives sets that are sufficient but carry operations the task does not need.
4. A nested chain of sets over four capabilities can contain at most five sets, so a single ladder cannot represent most of the 16.
5. Real interfaces combine capabilities in many ways, so the sets and the missing-set comparison must be checked against the actual runtime.

**Source:** Capabilities as sets: the grant, written down

## ES-ch03.59

A simple classifier takes a recorded list of event names (reason, read, write) and labels the run chat, assistant or agent. Before running three such traces through it, a student writes the predicted label for each and, for each trace, the over-claim a careless report would make. Explain why this practice is useful and give an example for a trace that contains only a reason event, then one containing a read, then one containing a write.

**Points:** 5

**Rubric (1 point each):**

1. A prediction fixed in advance can be contradicted, which reduces the room to explain results away afterward.
2. Writing the over-claim first provides a ready test for the later report.
3. For a reason-only trace, an over-claim is that the source was reviewed; the trace does not show that any source was read.
4. For a trace with a read, an over-claim is that the summary follows the source or that the run was safe; the record says only that a read was recorded.
5. For a trace with a write, an over-claim is that the source was damaged or that the action was unauthorized; the label is a category and the specific target and permission must be compared with the grant.

**Source:** One task, three constructed traces

## ES-ch03.60

Define three levels of review of AI output: comparing the output with the input it was given, checking it against sources outside the interaction, and examining the framing it supplies. Assign a level to each task and justify it: fixing typos in a paragraph, answering a factual question about a regulation, and proposing which problem a team should work on. Then say where the risk lies.

**Points:** 5

**Rubric (1 point each):**

1. Fixing typos can usually be reviewed by comparing output with input, since the changes can be seen directly.
2. A factual claim about a regulation must be checked against outside sources because the output supplies information the input did not contain.
3. Proposing the problem to work on needs examination of the framing itself, since the output sets the question rather than answering one.
4. The risk lies in the gap between the level the work needs and the level the review actually gives, such as a glance at a factual answer.
5. The needed level depends on the work and its stakes, not on the permissions granted, so the same permissions can accompany any of the three.

**Source:** Conducting AI

## ES-ch03.61

A student claims, "The agent never modified any file," on the basis of a harness event log with no write entries. Describe how they should find evidence outside the log, and how to word the claim if no independent evidence can be found.

**Points:** 5

**Rubric (1 point each):**

1. The log is a record produced by a system under review, and its completeness cannot be established by the log itself.
2. Independent evidence includes a before-and-after comparison of the relevant files or directories, a version-control diff, or filesystem audit records.
3. The comparison should use content hashes and cover the whole scope in which a write could have occurred.
4. If no independent evidence is available, the claim should be narrowed to "no write was recorded in the harness log".
5. The narrowed claim should state what was not checked, such as completeness of the log and files outside the examined scope.

**Source:** Verify and reflect
