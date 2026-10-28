# Chapter 13: Evaluation and approval gates

## MA-ch13.1

An autonomous coding agent pauses and shows a human reviewer a dialog that says only "The agent wants to run a command. Allow?" with Allow and Deny buttons. A security engineer proposes redesigning the request so that a yes from the reviewer actually means something. Check each statement that is true about the redesign. Each statement is worth 1 point (5 points total).

- [ ] A. The request should state what operation will occur and against which resolved target, since consequences cannot be judged without both.
- [ ] B. The request should say why the action serves the user's task, not merely that the agent is able to perform it.
- [ ] C. Showing the agent's self-reported confidence score is a sufficient substitute for describing the action, since high confidence means the action is safe.
- [ ] D. The request should say how the action could be undone, including when it cannot be undone.
- [ ] E. A long free-text paragraph written by the agent removes the need for any structured fields, because a reviewer can read it to find what matters.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: An approval is only as informative as the action and object it names; "a command" names neither.
- B: Capability does not establish intent; the purpose is what lets a reviewer notice an action that does not fit the task.
- C: Confidence is not a description of what will happen, and a model's self-assessment is not evidence about the world.
- D: Recoverability changes how much scrutiny an action deserves, and an honest "not reversible" is a key input.
- E: Unstructured prose lets omissions hide; named fields make a missing effect or rollback visible.

**Source:** A gate is not a button

## MA-ch13.2

An agent proposes "overwrite config.yaml in the project". The workspace contains ./config.yaml and ./deploy/config.yaml. ./config.yaml is a symbolic link to /etc/shared/config.yaml, a file other teams depend on. A reviewer approves after seeing only the display name "config.yaml". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The approval does not establish which file will be modified, because the display name does not identify one object.
- [ ] B. An experienced reviewer who knows the repository layout makes resolved paths unnecessary, since they can infer what each name refers to.
- [ ] C. Whatever file the agent ends up opening is covered by an approval that named "config.yaml", because the name was what the reviewer saw.
- [ ] D. Showing the resolved real path would let the reviewer see that a shared file outside the project is affected.
- [ ] E. Writing to a path that is a symbolic link modifies only the link itself and never the file it points to.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Two files share the name, and the consequential difference between them is hidden by the label.
- B: Even experts cannot see a link target that the interface does not show, and layouts change.
- C: An approval covers the object the reviewer understood; a name that fits several objects does not bind to any one of them.
- D: Resolved identities (path, account, environment) expose consequences that friendly names conceal.
- E: Opening a symlink for writing follows it and modifies the target file on POSIX systems.

**Source:** A gate is not a button

## MA-ch13.3

An agent asks for approval to send a customer-facing announcement email to 4,000 recipients. The rollback field in its request reads "undo the send". The email platform has no recall feature, and recipients' mail clients may already have downloaded the message. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Irreversible external effects are the effects that most need to be visible to the reviewer.
- [ ] B. A rollback field filled with any plausible-sounding text serves its purpose, because reviewers seldom rely on it when deciding whether to approve.
- [ ] C. When rollback is impossible, the request should make the impact and alternatives more prominent, not less.
- [ ] D. Assessing a rollback plan includes checking its assumptions: that a prior copy exists, is accessible, and that dependent effects have not occurred.
- [ ] E. The rollback claim is unreliable; an honest request would say the send cannot be undone and offer a partial remedy such as a correction message.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Once the message is out, only the pre-action decision can prevent harm.
- B: A plausible but false rollback plan is worse than an admitted gap, since it lowers the scrutiny the action needs.
- C: Absent recovery, the reviewer's decision is the last control, so the information it depends on should be unavoidable.
- D: "Restore from backup" is only valid if the backup exists, can be read, and restores the relevant state.
- E: Reassurance that does not match what the system can do misleads the reviewer on the point that matters most.

**Source:** A gate is not a button

## MA-ch13.4

An approval workflow rejects any proposal in which one of six required text fields is empty. An agent submits a proposal where all six are filled: action "do task", target "files", reason "needed", effects "none", evidence "looks good", rollback "revert". The validator accepts it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The validator checks presence only, so acceptance says nothing about whether the descriptions are adequate.
- [ ] B. Acceptance by the validator means the proposal is safe to approve, since every required field has been checked.
- [ ] C. A rule that rejects phrases such as "n/a" and "looks good" removes the need for human judgment about adequacy.
- [ ] D. Adding a minimum character length per field fully solves the problem, because longer text must contain more information.
- [ ] E. A reviewer should treat "evidence: looks good" as an unsupported claim, because it points to no artifact that can be checked.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A non-empty string can be uninformative or wrong; structural validity is a different property from substantive adequacy.
- B: The validator has no view of meaning, so safety is not something its output can claim.
- C: A blocklist catches some filler but cannot tell fluent, specific-sounding text that is wrong from text that is right.
- D: Padding with filler satisfies a length rule without adding information.
- E: Evidence is a pointer to a result someone can inspect, not an assertion that things are fine.

**Source:** A gate is not a button

## MA-ch13.5

A coding agent asks to delete the build cache directory. Its stated reason is "I have write permission to that directory." Check each statement that is true about this request. Each statement is worth 1 point (5 points total).

- [ ] A. A good reason is one the reviewer can verify, for example by pointing to the failing build the deletion is meant to fix.
- [ ] B. Having permission describes capability, not purpose, so it does not justify the action.
- [ ] C. The reason field is redundant whenever the action and target are shown, because purpose can always be inferred.
- [ ] D. A reason that merely restates the action ("delete the cache") is as informative as one linking the deletion to the user's goal.
- [ ] E. Reasons matter only for after-the-fact audit and do not help a reviewer decide now.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Verifiability is what separates a reason from a rationalization.
- B: Permissions are usually broader than intent; "I am allowed" does not say "this is wanted".
- C: Identical actions can serve opposite purposes, and an inferred purpose is a guess.
- D: Only a goal-linked reason lets the reviewer judge whether the action fits the task.
- E: A reason that does not match the task is a signal the reviewer can use before approving.

**Source:** A gate is not a button

## MA-ch13.6

A pipeline runs a unit test suite, a policy checker that flags edits outside approved directories, and an LLM-based rubric grader on an agent's proposed change. All three report green, and the dashboard shows them above an Approve button. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A passing test suite can evaluate selected behavior, but cannot establish that a destructive change is worth making.
- [ ] B. A green score from the model grader is itself the decision, because the grader was given a rubric by the team that owns the process.
- [ ] C. Each instrument produces evidence about a bounded set of properties; none of them decides whether the change should be made.
- [ ] D. Evaluation asks how well the proposal meets stated criteria; authorization asks whether a responsible person or policy permits it.
- [ ] E. A policy checker can flag an unapproved directory but cannot judge whether an exception would serve the people affected.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Tests check specified properties; whether the trade-off is acceptable is a judgment about consequences.
- B: A grader's score is evidence with its own failure modes, not an authorization.
- C: Evaluation tells you what happened or could happen against criteria; permitting the action is a separate act.
- D: These two questions are often merged on one screen, which is where gates become unreliable.
- E: Rule compliance and the value of an exception are different questions.

**Source:** Evaluation comes before authorization

## MA-ch13.7

A team evaluating an agent's new tool-use behavior first watches the agent attempt ten tasks. They then write the evaluation cases around what it did and, where its output was reasonable, adjust the expected answers to match. After the edits all ten cases pass, and the team reports "10/10". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Deciding what would count as evidence against the system before looking at its outputs keeps an evaluation able to fail.
- [ ] B. Running each of the ten tasks several more times fixes the problem, because averaging removes any bias in the cases.
- [ ] C. The adjustment is harmless as long as the ten final cases are legitimate tasks that the agent could plausibly be asked to do.
- [ ] D. The cases were shaped to fit the observed behavior, so the pass count records accommodation rather than a test that could fail.
- [ ] E. Because expected answers were adjusted only where the output was reasonable, 10/10 is a conservative estimate of quality.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Setting criteria in advance prevents the evidence from selecting its own standard.
- B: Repeats measure noise, not the bias introduced by choosing criteria after seeing outputs.
- C: Legitimate tasks can still be a biased sample if their expected answers were fitted to one system's behavior.
- D: A test whose expected result was changed to match the output could not have embarrassed the system.
- E: Adjusting toward the observed output biases results upward, not downward.

**Source:** Evaluation comes before authorization

## MA-ch13.8

An agent is asked to close inactive accounts. Its tool trace shows a single call, UPDATE accounts SET status='closed' WHERE last_login < '2025-01-01', which returned success with "42 rows affected". The agent's final message says "I closed all 99 matching accounts." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Where the fluent final message and the trace disagree, the message should be preferred because it is a summary of the whole task.
- [ ] B. The final message contradicts the trace, which reports 42 rows, so the claim of 99 is unsupported by the available evidence.
- [ ] C. A trace showing that a command ran is not the same as an observation that the intended end state exists.
- [ ] D. The trace remains useful as a record of what was attempted, but it must be kept distinct from observations of actual outcomes.
- [ ] E. A separate post-action query counting accounts in the closed state would be stronger evidence than the trace or the narration.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Fluency is not accuracy; the message is the least verified of the three artifacts.
- B: When narration and tool output disagree, the narration has no independent standing.
- C: Execution evidence and outcome evidence answer different questions.
- D: Both records matter for diagnosis; they should not be merged into a single "success" flag.
- E: An independent observation of the world can contradict the agent's account.

**Source:** Evaluation comes before authorization

## MA-ch13.9

A team reports that a file-writing agent "passed 20 of 20 evaluation cases." All 20 cases write ordinary text files into a newly created empty directory. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The result says little about symbolic links, permission errors, concurrent changes, or ".." in paths, because no case exercised them.
- [ ] B. Exclusions matter only if the agent has previously failed in those situations; otherwise they can be ignored.
- [ ] C. 20 of 20 shows the agent handles any file operation it will meet in production, since the cases passed without a single failure.
- [ ] D. The report is more interpretable if it states only the pass count, since listing excluded situations distracts readers.
- [ ] E. Adding 20 more ordinary writes would substantially improve coverage of the risky boundaries, because the sample size would double.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A pass count is only informative about the situations the cases actually cover.
- B: Absence of past failures is not evidence about conditions that were never tried.
- C: Production inputs include conditions that none of the 20 cases represent.
- D: Without the covered and excluded situations, a reader cannot tell what the pass count means.
- E: More of the same does not probe different failure modes.

**Source:** Evaluation comes before authorization

## MA-ch13.10

An evaluation set for an agent that decides whether to carry out requested file operations has 20 cases where the correct behavior is to proceed. An agent that always proceeds is scored on it. The team then adds 5 cases where the correct behavior is to refuse, and scores the same always-proceed agent again. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding refusal cases is wrong unless their share of the set matches their frequency in production.
- [ ] B. On the expanded 25-case set, the always-proceed agent scores 80% (20 of 25) because it gets only the original cases right.
- [ ] C. On the original 20 cases, the always-proceed agent scores 100%, because every correct answer is to proceed.
- [ ] D. A set without refusal cases would still reveal an indiscriminate agent, because such agents fail ordinary tasks too.
- [ ] E. A set with no should-refuse cases cannot distinguish a careful agent from a reckless one.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A set meant to expose boundary behavior may deliberately oversample rare, high-consequence cases.
- B: It fails exactly the 5 refusal cases.
- C: Every case rewards proceeding, so an indiscriminate agent looks perfect.
- D: Ordinary tasks reward proceeding, so indiscriminate agents pass them.
- E: The distinguishing behavior, declining when it should, is never exercised.

**Source:** Evaluation comes before authorization

## MA-ch13.11

After redesigning an approval screen so that details sit behind a "show more" link, a team reports: median time to approval fell from 90 seconds to 25, reviewer satisfaction rose, and task success stayed at 94%. The share of executed actions later judged invalid rose from 1% to 4%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A useful evaluation reports a portfolio that includes error and deferral rates, not one celebratory rate.
- [ ] B. Faster approvals can reflect reflexive clicking rather than a more efficient review.
- [ ] C. Unchanged task success shows the redesign is safe, because the agent completes the same share of tasks as before.
- [ ] D. The metrics pull in different directions, so a single headline number such as time to approval would mislead.
- [ ] E. The invalid-action share quadrupled, from 1% to 4%, which is consistent with reviewers catching fewer problems.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Errors and deferrals are the evidence a single success rate discards.
- B: Less time per decision can mean less attention per decision.
- C: Task success does not capture invalid actions that happen to leave the task output intact.
- D: Speed, satisfaction, success and error rates measure different things and can move oppositely.
- E: 4/1 = 4; the direction fits a less informed review, though it does not by itself prove the cause.

**Source:** Evaluation comes before authorization

## MA-ch13.12

To score free-text rollback plans, a team uses two LLM graders. Both use the same rubric prompt, which rewards "specific, step-by-step recovery instructions". The two graders agree on 96% of items. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. 96% agreement between the graders shows that their scores are accurate, since independent judges rarely agree by chance.
- [ ] B. Model graders should replace deterministic checks whenever the output is free text, because they can judge meaning.
- [ ] C. A fluent step-by-step plan that omits an irreversible side effect would be scored poorly under this rubric, since omissions are penalized.
- [ ] D. Calibration against human-labeled examples becomes unnecessary once the two graders agree with each other this closely.
- [ ] E. Agreement between graders that share a prompt and similar biases does not make them independent verifiers.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Agreement measures consistency between graders, not correctness against ground truth.
- B: Deterministic checks, where they exist, are cheaper and more reliable and should be combined with model grading.
- C: The rubric rewards the appearance of specific detail, which fluent text can supply without being correct.
- D: Only comparison with trusted labels reveals systematic error.
- E: Shared assumptions or blind spots can make two judges wrong in the same direction.

**Source:** Evaluation comes before authorization

## MA-ch13.13

A team's approval-gate prototype passes all 6 of 6 evaluation cases. A manager proposes reporting that the approval gate is "100% reliable". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With so few cases, the best report is a single pass rate with no further detail, because details add noise.
- [ ] B. Six passing cases show that the six covered properties are sufficient to establish that the approval gate is correct overall.
- [ ] C. With six independent random cases and zero failures, the 95% upper bound on the true failure rate is still about 39% (1 - 0.05^(1/6)).
- [ ] D. Six passes support reporting a reliability percentage, as long as each case was run carefully and the results were recorded.
- [ ] E. If the six cases were hand-picked to cover distinct failure modes, they still support a population-level percentage.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Listing the cases and exclusions is more informative than a percentage of a tiny set.
- B: Passing a set of tests shows only that those statements hold, not that they are the right or complete statements.
- C: A small clean sample is compatible with a high underlying error rate.
- D: Care does not turn a handful of cases into a population estimate.
- E: Hand-picked cases are not a random sample and do not estimate a rate.

**Source:** Evaluation comes before authorization

## MA-ch13.14

An agent succeeds on a given task independently with probability 0.7 on each attempt. A team evaluates it with three independent trials per task. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For an action that is harmful when it fails, "at least one success in k trials" is the better headline measure.
- [ ] B. Because a model is nondeterministic, a single trial per task is enough to characterize it.
- [ ] C. The probability of at least one success in three trials is 0.973, which is 1 minus 0.3 cubed.
- [ ] D. "At least one success" and "all trials succeed" are the same measure whenever the trials are independent.
- [ ] E. The probability of succeeding on all three trials is about 0.343, which is 0.7 cubed.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Harmful failures call for the stricter all-trials view; best-of-k hides inconsistency.
- B: One trial cannot show the variation between runs that the measures above quantify.
- C: Complement of three consecutive failures: 1 - 0.027.
- D: They differ sharply here, 0.973 versus 0.343.
- E: Independent successes multiply.

**Source:** Evaluation comes before authorization

## MA-ch13.15

Before running an evaluation, a team writes down the expected outcome for each case. After the run, case 7's actual result differs from its expected outcome. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the expectation or requirement is changed, no record of the change is needed once the final version of the test passes.
- [ ] B. Locking expectations in advance is pointless because they will need revision after the first run anyway.
- [ ] C. Failing cases should be removed from the set as unrepresentative, so that the set reflects normal operation.
- [ ] D. The expected outcome should be silently edited to match the result so that the final report is clean and consistent.
- [ ] E. The discrepancy could come from the implementation, the test expectation, or the original requirement, and each should be investigated.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Without a record, the evaluation looks as if it was always satisfied and the reason for the change is lost.
- B: The commitment is what makes a later change visible and accountable.
- C: Removing failures guarantees a passing set and destroys the evidence.
- D: A clean-looking report built on edited expectations conceals what was learned.
- E: Any of the three could be wrong, and blaming the implementation by default skips real diagnoses.

**Source:** Evaluation comes before authorization

## MA-ch13.16

Two services build the same approval request as Python dictionaries. One inserts the keys in the order action, target, reason; the other inserts them in the order reason, target, action. Each computes SHA-256 over json.dumps(request).encode(), with no sort_keys option, and the services compare digests. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Python dictionaries keep insertion order and json.dumps emits keys in that order, so the services produce different bytes and digests.
- [ ] B. The digests would match anyway, because SHA-256 hashes the meaning of the data rather than the particular bytes used to write it.
- [ ] C. Passing sort_keys=True makes the serialization independent of insertion order for JSON-compatible data.
- [ ] D. A mismatch caused by key order would reject an unchanged proposal, which is a false rejection that fails closed.
- [ ] E. A JSON object is defined by its key order, so the two requests really are different proposals that need separate decisions.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The hash is computed over bytes, and the bytes differ.
- B: A hash function sees only bytes.
- C: Sorting gives one canonical key order.
- D: Wasted re-approvals are a usability cost, not a security hole.
- E: JSON objects are unordered collections; order is a representation detail.

**Source:** Canonical content and its fingerprint

## MA-ch13.17

A Python service and a JavaScript service both hash what they believe is the same JSON approval payload and get different digests. The payload contains the number 1.0, the string "é", and a nested object whose keys are listed in a different order in each service. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. SHA-256 behaves differently across programming languages, so identical bytes can give different digests on different platforms.
- [ ] B. If both services sort their keys, no other source of disagreement remains, because key order is the only variable in JSON.
- [ ] C. Number formatting can differ between serializers (1.0 versus 1), which changes the bytes that are hashed.
- [ ] D. Reliable cross-language hashing needs a written canonicalization specification, such as RFC 8785, instead of each language's defaults.
- [ ] E. The character é can be one code point or e plus a combining accent, giving different UTF-8 bytes unless the text is normalized.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: SHA-256 is a standard function; identical bytes always give identical digests.
- B: Number formats and Unicode normalization still differ.
- C: Python's json.dumps writes 1.0 where other encoders write 1.
- D: A shared specification pins down key order, number format and escaping.
- E: Unicode has multiple equivalent encodings of the same visible text.

**Source:** Canonical content and its fingerprint

## MA-ch13.18

A developer says: "We log only the SHA-256 digest of each approval request, so the requests are protected, and the log proves who approved." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Different requests will frequently produce the same SHA-256 digest, so a matching digest is unreliable as evidence of identical content.
- [ ] B. A plain digest says nothing about who produced a record, because anyone can compute it.
- [ ] C. Attributing a decision to a person needs more than the hash, such as a digital signature or an authenticated session.
- [ ] D. Anyone who can guess the request text can compute its digest and compare, so hashing predictable content does not hide it.
- [ ] E. A SHA-256 digest of the request acts as the approver's digital signature, because only the approver's system could produce it.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Accidental collisions for SHA-256 are negligible in practice.
- B: No secret is involved in computing a SHA-256 digest.
- C: Identity needs a credential that only the signer controls.
- D: Hashing is not encryption; low-entropy inputs can be confirmed by brute force.
- E: A signature requires a private key bound to an identity; a hash has none.

**Source:** Canonical content and its fingerprint

## MA-ch13.19

Check each statement that is true about using SHA-256 to fingerprint a serialized approval request. Each statement is worth 1 point (5 points total).

- [ ] A. The digest can be decrypted with the right key to recover the original request, as with symmetric encryption.
- [ ] B. Changing one character of the input changes the digest unpredictably and completely, with no resemblance to the old value.
- [ ] C. Two requests that mean the same thing always have equal digests, however they were serialized.
- [ ] D. The digest gets longer as the request gets longer, so large proposals have larger fingerprints.
- [ ] E. The digest is 256 bits long, conventionally written as 64 hexadecimal characters, whatever the input size.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Hashing is one-way and has no key or decryption step.
- B: This is the avalanche property of cryptographic hashes.
- C: The digest depends on bytes, so different serializations of the same meaning differ.
- D: The output length is fixed at 256 bits regardless of input size.
- E: 256 bits at 4 bits per hex digit gives 64 characters.

**Source:** Canonical content and its fingerprint

## MA-ch13.20

A Python validator rejects an approval proposal when `not proposal.get(field)` is true for any of its six required fields. Consider proposals that are otherwise complete. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A required field whose value is the string "0" is accepted, because the string is non-empty.
- [ ] B. A proposal with an extra, unrequired key is rejected because the validator checks the whole dictionary.
- [ ] C. A required field containing only spaces, such as "   ", is accepted, because the string is not empty.
- [ ] D. A required field whose value is an empty list is rejected, because an empty list is falsey in Python.
- [ ] E. A required field whose value is None is rejected, because None is falsey in Python.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Any non-empty string is truthy, including "0".
- B: The check iterates over the required names only; extra keys do not affect it.
- C: A whitespace-only string is non-empty and therefore truthy.
- D: An empty list is falsey in Python, so `not []` is true.
- E: `proposal.get(field)` returns None, which is falsey.

**Source:** Canonical content and its fingerprint

## MA-ch13.21

A gate computes its fingerprint over the entire proposal dictionary, but validation requires only six named fields. After a decision is recorded against a proposal, an agent adds a seventh key, "environment": "production", and resubmits it with the old decision. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Validation of the six required fields would reject the extra key, since it is not on the list of allowed fields.
- [ ] B. If the fingerprint covered only the six named fields, adding the seventh key would leave the approval valid, a weakness.
- [ ] C. Because the extra key is part of the serialized proposal, the fingerprint changes and the old decision no longer matches.
- [ ] D. It is safe for a fingerprint to ignore unknown fields, because only declared fields can influence execution.
- [ ] E. Hashing as many extra attributes as possible has no downside, because more coverage always means more safety.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Validation only checks presence of the required names.
- B: A consequential field would then be able to change without invalidating the approval.
- C: The digest covers every serialized byte.
- D: Executors may act on any field they receive, declared or not.
- E: Volatile attributes such as timestamps or request IDs cause spurious invalidations and re-approvals.

**Source:** Canonical content and its fingerprint

## MA-ch13.22

An approval check returns true only when: the decision is a dictionary; decision.get("approved") is True (identity comparison); the approver is a string that is not blank after strip(); and the recorded fingerprint equals the fingerprint freshly computed from the proposal. Check each statement that is true about how it treats these decision records, where the recorded fingerprint matches the current proposal unless stated otherwise. Each statement is worth 1 point (5 points total).

- [ ] A. A record with approved=True whose fingerprint came from an earlier version of the proposal is rejected.
- [ ] B. A record with approved=True and approver "   " is accepted, because the approver string is not empty.
- [ ] C. A record with approved=1 is accepted, because 1 equals True in Python comparisons.
- [ ] D. A record with approved="yes" is accepted, because the string "yes" is truthy in Python.
- [ ] E. A record with approved=True, a nonblank approver "dana" and a matching fingerprint is accepted.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The recorded digest differs from the fresh digest of the current proposal.
- B: After strip() the approver is empty, so the nonblank condition fails.
- C: `1 is True` is false in Python; only the Boolean object passes.
- D: The identity comparison with True rejects the string "yes".
- E: All four conditions hold.

**Source:** The approval predicate

## MA-ch13.23

A system computes a proposal's fingerprint when the proposal is displayed to the reviewer and stores it in the decision. At execution time, the executor checks that the decision's stored fingerprint is well formed, but never recomputes it from the proposal it is about to run. Between review and execution a different component changes the target field. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The fingerprint should be recomputed from the exact proposal about to execute, at the point where the effect happens.
- [ ] B. This is a time-of-check to time-of-use gap, in which the verified state differs from the state used.
- [ ] C. The check compares the decision with itself, so it passes whatever proposal the executor actually runs.
- [ ] D. Computing the fingerprint at review time is enough, because the reviewer's screen shows what will run.
- [ ] E. Making the proposal read-only in the user interface closes the gap even if the executor receives a different object.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Binding is enforced only if the comparison uses fresh content at the effect boundary.
- B: The state verified at review time can differ from the state used at execution time.
- C: Nothing ties the stored value to the content at the moment of use.
- D: The screen shows what was displayed, not what the executor receives later.
- E: Interface-level immutability does not constrain what a separate component passes to the executor.

**Source:** The approval predicate

## MA-ch13.24

A decision record contains {"approved": true, "approver": "reviewer-1", "fingerprint": <digest matching the current proposal>}. The system's predicate checks exactly these three fields and returns true. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Nothing in the record shows that the reviewer opened, read, or understood the proposal.
- [ ] B. The record was written against exactly this proposal content, as the matching digest shows.
- [ ] C. The predicate also enforces expiry and single use, since a decision record normally includes those limits.
- [ ] D. The true result shows that a person with authority gave informed consent to this specific action.
- [ ] E. The approver string shows that an authenticated human logged in and reviewed the proposal.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A digest records which bytes the record refers to, not whether anyone looked at them.
- B: The matching digest binds the decision to the serialized proposal.
- C: Those properties need explicit fields and checks that this predicate does not have.
- D: The predicate checks the shape and content binding of a record, not the circumstances of its creation.
- E: A name field in a record can be typed by anyone or generated by a program.

**Source:** The approval predicate

## MA-ch13.25

An approval can be bound to three different things: the exact content of the proposal; the scope and time of its validity (environment, deadline, number of uses); and the person who decided, with their authority. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Content binding alone is sufficient for an irreversible action that is executed once.
- [ ] B. Content binding automatically gives the decision an expiry, because a digest changes over time.
- [ ] C. Verifying that the fingerprint matches also supplies person binding, because the digest is tied to the approver.
- [ ] D. An approval for a "deploy" action reused two weeks later in a different environment lacks scope-and-time binding.
- [ ] E. A decision filed under a name that anyone could type lacks person binding, because no identity was verified.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Content binding does not establish who decided, with what authority, or that the decision is still current.
- B: A digest has no time dimension.
- C: A digest identifies content, not who produced the record.
- D: Nothing limited when, where, or how often the decision applies.
- E: There is no authenticated identity or authority behind the name.

**Source:** The approval predicate

## MA-ch13.26

A single-use approval is enforced like this: step 1 reads the decision's "used" flag; if it is false, the action runs; step 2 afterwards sets the flag to true. Two workers receive the same valid decision at nearly the same moment. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Checking and marking the decision as used must be one atomic step, such as a compare-and-set, transaction, or unique constraint.
- [ ] B. Reading the flag twice with a short delay in between closes the gap, because the second read sees the other worker's update.
- [ ] C. Both workers can read used=false before either sets it, so the action may run twice.
- [ ] D. A matching fingerprint alone limits nothing about how many times the same decision is presented.
- [ ] E. Hashing the decision a second time before running prevents the duplicate, because the second hash would differ.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Atomicity removes the gap that two concurrent workers exploit.
- B: A delay shortens, but does not eliminate, the window for a race.
- C: Check and update are separate steps with a gap between them.
- D: Content binding says what was approved, not how often it may be used.
- E: A second hash does not change who sees the flag as false.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.27

A decision stores its expiry as "2026-03-01 17:00" with no time zone, and the checking code calls the system clock inside the predicate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Expiry matters only for decisions that are never used, because once a decision has been used it can no longer be exercised.
- [ ] B. Passing the current time into the check as a parameter lets tests assert behavior just before and after the deadline without waiting.
- [ ] C. Storing the expiry as an unambiguous instant, such as UTC, and stating whether the deadline itself is valid avoids boundary disputes.
- [ ] D. The deadline is ambiguous, because servers in different zones can interpret the same local time as different instants.
- [ ] E. A predicate that takes the time as an argument cannot be used in production, because callers could then supply any time.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Expiry limits how long an unused decision can be exercised.
- B: Injecting the clock makes boundary tests deterministic.
- C: A comparison policy needs both a time basis and a rule for equality.
- D: A zone-less timestamp does not identify a single moment.
- E: The production caller supplies its trusted clock reading as the argument.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.28

At 09:00 a reviewer approves exporting a dataset, with the approval valid for 24 hours. At 11:00 the dataset is reclassified as restricted. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An approval obtained after its premises have expired is acceptable as long as the fingerprint matches.
- [ ] B. New evidence or changed premises can make an approval stale before its stated deadline passes.
- [ ] C. Revocation withdraws a still-unexpired decision, and the execution-time check should consult revocation state.
- [ ] D. Including the data classification in the bound proposal would make a changed classification force re-review.
- [ ] E. The approval remains fully valid until 09:00 the next day, because validity is purely a matter of time.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A matching fingerprint says the content is unchanged, not that the premises still hold.
- B: Expiry is not just a timer; the basis for the decision may have disappeared.
- C: A withdrawal that is never checked at the effect boundary has no effect.
- D: Binding a relevant attribute turns its change into a content mismatch.
- E: Reclassification changes what the reviewer would have approved.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.29

A team adds revocation to its approval system. Check each statement that is true about a sound design. Each statement is worth 1 point (5 points total).

- [ ] A. The design should specify what happens to work that has already started when a revocation arrives.
- [ ] B. Revoking a decision means deleting its record, which keeps the log clean and avoids confusion about its status.
- [ ] C. The execution-time check must consult revocation state at the effect boundary, not only at review time.
- [ ] D. A revocation record should say who revoked, under what authority, and which decision or proposal it affects.
- [ ] E. The original decision should be preserved in the audit trail and marked as withdrawn, not erased.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Without a rule, in-flight actions are handled inconsistently.
- B: The audit trail should show that a decision existed and was withdrawn.
- C: A revocation that is not checked where the action happens is advisory only.
- D: Withdrawals are consequential decisions and need accountability of their own.
- E: History remains inspectable after revocation.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.30

A reviewer approves "ALTER TABLE users ADD COLUMN plan text" against the staging database. The identical SQL text is later submitted against the production database with the old decision attached. The proposal fields contain only the SQL text. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The environment is operational detail that does not belong in an approval request, which should describe only the action.
- [ ] B. The fingerprint matches because the text is identical, so a content-only gate accepts it although the environment was never part of the proposal.
- [ ] C. Matching SQL text means the risk is identical, so the approval should transfer to the production database.
- [ ] D. Include the identities whose change should force reconsideration and no others; over-binding causes spurious re-approvals.
- [ ] E. Identifiers such as the resolved target, account, environment, repository revision, and data classification are candidates for binding.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The environment is one of the most important facts for judging the effect of an action.
- B: Binding is only as semantic as what the proposal includes.
- C: Running on production data has consequences staging does not.
- D: Choosing which identities matter is a judgment about consequence.
- E: These attributes determine the actual consequences.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.31

A single-use approval authorizes one database migration. The executor claims the decision and starts the migration, but the process crashes halfway. An operator proposes simply retrying using the same decision. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the fingerprint still matches, the system has nothing else to check before the retry.
- [ ] B. Recording "claimed or in progress" separately from "completed" lets the team make a deliberate decision about retrying.
- [ ] C. The crash proves the original approval was invalid, because a valid approval would have allowed completion.
- [ ] D. A decision authorizes one bounded attempt, and a partially applied state may differ from the state the reviewer assessed.
- [ ] E. Retrying with the same decision is always appropriate, because the approved content has not changed.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Use constraints, expiry, revocation, and current state still matter.
- B: A single used flag cannot distinguish a crash from success.
- C: A failure during execution says nothing about whether the approval was valid.
- D: The reviewer judged effects and rollback from the starting state, not from a half-finished one.
- E: Unchanged content does not guarantee the premises, effects, or rollback assumptions still hold.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.32

An agent's request proposes to rotate production API credentials, and the rollback field reads "restore the old keys". The old keys will be revoked by the provider as part of the rotation, and services that cached them will fail until redeployed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Dependent effects, such as services that fail while using cached keys, belong in the effects field.
- [ ] B. The rollback claim assumes that the old keys remain valid after rotation, which is false in this situation.
- [ ] C. A reviewer-facing request should state that full rollback is not possible and describe the recovery path, such as issuing new keys.
- [ ] D. Because the operation is scripted, a successful exit code establishes that the rollback works.
- [ ] E. A rollback field is satisfied by any statement that sounds reasonable to the person filling it in.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Downstream impact is part of what the reviewer is approving.
- B: A rollback plan is only valid if its prerequisites survive the action.
- C: Admitting a gap is more useful than inventing reassurance.
- D: Exit codes report that a command ran, not that its recovery assumptions hold.
- E: The field is only useful if it is true and testable.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.33

Four edits are made to an approved proposal before it executes: (1) its keys are re-ordered; (2) whitespace in the serialized JSON is changed; (3) the target path changes from "/srv/app/report.md" to "/srv/other/report.md"; (4) the environment attribute changes from "staging" to "production". The approval gate fingerprints a canonical serialization of the full proposal. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Edits (1) and (2) are representation changes, so a good canonical form keeps the fingerprint unchanged and no new approval is needed.
- [ ] B. Edit (3) changes the object acted on, so the fingerprint changes and the old decision no longer applies.
- [ ] C. Edit (4) changes the environment, so the fingerprint changes and a new decision is needed.
- [ ] D. All four edits should keep the old approval valid, because the action name is unchanged and the action name is what was approved.
- [ ] E. All four edits should invalidate the approval, because any byte change must be treated as a new proposal.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Forcing re-approval over formatting wastes reviewer attention.
- B: A different target is a different proposal.
- C: The environment is part of what was approved.
- D: The action name is only one part of what the reviewer judged.
- E: Normalizing representation noise is the purpose of canonicalization.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.34

An approval flow is attacked in three ways: (i) an attacker steals a reviewer's login and approves a proposal; (ii) a junior contractor with no authority over the data approves a data release; (iii) an overworked reviewer clicks Approve on a proposal without opening its evidence. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Case (ii) is a failure of authority, addressed by a registry mapping actions or data to roles that may approve them.
- [ ] B. Case (iii) is a failure of comprehension and attention, which interface design, workload limits and review practice affect more than cryptography does.
- [ ] C. If the approver field is non-empty, all three cases are excluded, because a name implies a verified person.
- [ ] D. A content fingerprint on the decision prevents all three cases, because it ties the decision to the approver's login.
- [ ] E. Case (i) is a failure of authenticated identity, addressed by controls such as strong authentication and signed decisions.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Being able to click is different from having the right to decide.
- B: No hash can show that a human read the material.
- C: A non-empty name field is easy to fill falsely and says nothing about authority or attention.
- D: The fingerprint only ties the decision to content.
- E: The record would look right but the wrong person created it.

**Source:** The approval predicate

## MA-ch13.35

A team's six unit tests for an approval check all pass: (1) a valid decision is accepted; (2) re-ordering the proposal's keys does not change the fingerprint; (3) changing the target field causes rejection; (4) a decision with no approver is rejected; (5) a decision with approved=False is rejected; (6) the fingerprint is 64 hexadecimal characters. Three alternative implementations also pass all six tests. X fingerprints only the six named proposal fields. Y tests `if decision.get("approved")` instead of requiring the Boolean True. Z checks that a decision is unused and marks it used in two separate steps. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Mutants that pass the suite show carelessness by the implementers rather than weakness in the tests.
- [ ] B. A test that adds an extra field to an approved proposal and expects rejection would catch X; a test using approved="no" would catch Y.
- [ ] C. The suite is too weak, because X, Y and Z are wrong in ways none of the six tests detect.
- [ ] D. Catching Z requires a test that interleaves two consumers of the same decision, because the flaw is a race.
- [ ] E. Passing all six tests demonstrates that the original implementation is correct, since each test covers a distinct requirement.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A mutant that survives is by definition a behavior the tests failed to specify.
- B: Each test targets the specific weakness the mutant introduces.
- C: Passing tests show that the tested statements hold, not that the implementation is right.
- D: Single-threaded tests cannot expose a gap between check and update.
- E: Six tests cannot establish that six statements are the right or complete statements.

**Source:** Write the approval predicate before anything is approved

## MA-ch13.36

Before running the tests on a new approval gate, an engineer writes and dates one sentence describing what the output would look like if the approval gate approved something it should not. Check each statement that is true about this practice. Each statement is worth 1 point (5 points total).

- [ ] A. If the prediction turns out wrong, it should be rewritten to match what happened so the record is consistent.
- [ ] B. A prediction written after seeing the output is as informative as one written before it, since both describe the same result.
- [ ] C. The sentence is unnecessary when the tests are automated, since the test results already say what failed.
- [ ] D. Writing the failure criterion beforehand lets the check surprise the engineer instead of confirming whatever appears.
- [ ] E. Predictions should be kept vague so that they cannot turn out wrong and embarrass the engineer later.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The recorded miss is information about the engineer's understanding.
- B: After the fact, a prediction can only describe what was seen, so it cannot turn out wrong.
- C: The sentence defines what a failure would mean; automation only runs checks.
- D: A prediction made first is falsifiable.
- E: A vague prediction cannot fail, which defeats its purpose.

**Source:** Write the approval predicate before anything is approved

## MA-ch13.37

A team writes the specification of an approval gate before any code exists. Check each item that belongs in that specification. Each statement is worth 1 point (5 points total).

- [ ] A. Rules for how long, where and how often a decision may be used, and how it is withdrawn.
- [ ] B. A statement that the approver's trust in the AI system is high enough to skip review of low-effort cases.
- [ ] C. A named decision owner, expressed as a role that can be asked, not "the team".
- [ ] D. An evaluation set that includes cases designed to make the proposal fail, not only to pass.
- [ ] E. The approval predicate: the exact conditions under which a decision authorizes one attempt.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: These govern where, how long, and whether a decision can be used.
- B: Trust in the proposer is not a gate condition and undermines the approval gate's purpose.
- C: Accountability needs someone specific.
- D: A set that cannot embarrass the proposal does not evaluate it.
- E: The predicate is the core contract the code and tests must satisfy.

**Source:** Write the approval predicate before anything is approved

## MA-ch13.38

A developer asks an AI coding assistant to write both an approval check and its unit tests from a one-sentence description. All the tests pass, and the developer reports the approval gate as verified. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tests written by the same model that wrote the implementation can share its blind spots, so passing them is weak evidence.
- [ ] B. AI-written tests are invalid by nature and should be discarded, whatever they check and however they were reviewed.
- [ ] C. Asking the assistant for a deliberately wrong version that still passes the tests is a cheap way to find gaps in the tests.
- [ ] D. Acceptance criteria written by the accountable person before implementation give an independent standard to test against.
- [ ] E. Once the tests pass, reading the implementation is unnecessary, because the tests encode every requirement.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The same misunderstanding can appear in both the code and the tests.
- B: Generated tests can be useful; the issue is their independence, not their origin.
- C: A surviving wrong version proves the tests do not constrain that behavior.
- D: Independence is what makes a check informative.
- E: Passing tests do not reveal behaviors they do not cover.

**Source:** Write the approval predicate before anything is approved

## MA-ch13.39

An AI assistant returns an implementation that adds decision IDs, deadlines, revocation and single-use consumption to an approval check. A reviewer inspects the diff for places where consequential decisions are hidden. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the assistant's own explanation describes the logic correctly, reading the diff is optional, since the explanation was produced from the code.
- [ ] B. Only variable names and comments need review, because the behavior of the code is described there.
- [ ] C. Where the current time is read matters, because it decides whether expiry can be tested and whether callers can influence it.
- [ ] D. Where a used decision is recorded matters, including whether checking and recording happen as a single atomic step.
- [ ] E. The reviewer should confirm that earlier strictness was not weakened, for example that approved must still be exactly True.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: An explanation is another output of the system under review, not independent evidence.
- B: Names and comments are claims; behavior is in the logic.
- C: A hidden clock read makes boundaries hard to test and can be a manipulation point.
- D: A separate check and record leaves a race.
- E: Feature additions often relax earlier checks.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch13.40

A team designs the screen on which a human reviews an agent's proposed action. Check each statement that is true about a sound design. Each statement is worth 1 point (5 points total).

- [ ] A. Approve should be pre-selected to speed up the common case, because most proposals end up approved.
- [ ] B. The action and the target should appear first, before secondary details such as evidence and rollback.
- [ ] C. Differences from a previously reviewed version should be highlighted, for example "target changed from A to B; prior approval invalid".
- [ ] D. Showing a friendly summary while the fingerprint covers hidden fields is acceptable, since the hash protects the content.
- [ ] E. Collapsing irreversible effects behind an expandable panel is fine as long as the information remains available.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A default selection biases the decision toward yes.
- B: The reviewer's first need is to see what will happen to what.
- C: Reviewers notice changes more reliably when they are surfaced.
- D: A decision binds to bytes the reviewer never meaningfully inspected.
- E: The most consequential facts should be unavoidable, not optional.

**Source:** The approval interface is part of the control

## MA-ch13.41

A review dialog shows a large green "Continue" button beside a small gray "refuse" link, and a message "Approve within 60 seconds or the job fails!" generated by the agent that submitted the request. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The countdown message is a legitimate priority signal because the agent knows its own work best.
- [ ] B. Requiring a written reason for refusing but not for approving is neutral, since both are recorded decisions.
- [ ] C. Offering a "defer" option in addition to approve and refuse adds noise and should be removed.
- [ ] D. The visual weighting of the green button over the gray link nudges the reviewer toward approval.
- [ ] E. The design is fine as long as the refuse option exists somewhere on the screen.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: A proposer's urgency claims serve the proposer and are not independent evidence of urgency.
- B: Extra effort to refuse biases the decision toward approval.
- C: Deferral is a real outcome when evidence is insufficient or authority is unclear.
- D: Unequal prominence is a standard dark pattern that undermines genuine choice.
- E: Availability in principle differs from availability in practice.

**Source:** The approval interface is part of the control

## MA-ch13.42

A proposal's evidence field is the URL of a test report on a shared drive. The fingerprint covers the proposal text, including the URL. After the reviewer approves, someone overwrites the report at the same URL with a different result. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Binding only the proposal text leaves a substitution path, because the evidence can change while the fingerprint stays the same.
- [ ] B. A decision should bind to the representation the reviewer saw together with any immutable artifacts it references.
- [ ] C. Since the fingerprint still matches, the evidence is unchanged and the approval remains informed.
- [ ] D. The URL being in the proposal means the evidence is automatically trustworthy, since the reviewer could open it.
- [ ] E. Referencing the evidence by an immutable identifier, such as a content hash or version ID, binds the decision to what the reviewer saw.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The URL is stable; the content behind it is not.
- B: Otherwise the reviewer approved something different from what executes.
- C: A fingerprint of the URL string says nothing about the document behind it.
- D: A reference is not the content, and its target may change.
- E: Immutable references keep the evidence from changing silently.

**Source:** The approval interface is part of the control

## MA-ch13.43

At execution time, an executor recomputes a proposal's fingerprint and finds that it differs from the one in the stored approval decision. Check each statement that is true about appropriate responses. Each statement is worth 1 point (5 points total).

- [ ] A. Block the action, show the reviewer which fields changed, and return the proposal to review.
- [ ] B. Overwrite the stored fingerprint with the new value so the next check passes.
- [ ] C. Ask the model whether the old approval probably still applies, and proceed if it agrees.
- [ ] D. Treat the old decision as authority for the new proposal when the action name is unchanged, since the reviewer chose that action.
- [ ] E. Proceed if the agent classifies the difference as minor, since it understands its own change best.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A changed proposal is a new object that needs a new decision.
- B: That would manufacture an approval for content nobody reviewed.
- C: The proposer's model has an interest in proceeding and is not an authority.
- D: The reviewer decided on content that has since changed, so the decision cannot cover it.
- E: The party seeking approval should not decide what counts as minor.

**Source:** The approval interface is part of the control

## MA-ch13.44

A reviewer is assigned a proposal to export a dataset containing customer data. The reviewer understands the proposal fully but has no authority over that data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reviewer should approve to avoid blocking the project and flag any concerns afterwards, since approvals can be undone.
- [ ] B. Deferring with documented unresolved gaps is a successful outcome for the approval gate, not a failure.
- [ ] C. Refusal and deferral should be recorded as outcomes of the process, not treated as errors in it.
- [ ] D. A gate should provide a path to escalate to someone with authority, so the reviewer need not impersonate an approver.
- [ ] E. A reviewer's full understanding of a proposal does not by itself confer authority to approve it.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Approval given to avoid friction converts the approval gate into a ritual.
- B: The approval gate worked: it prevented an unsupported yes.
- C: Treating them as failures pressures people to approve.
- D: Authority and understanding are different properties.
- E: Authority comes from role and ownership, not from comprehension.

**Source:** The approval interface is part of the control

## MA-ch13.45

Autonomous agents submit 5 proposals per hour for human review. One reviewer can carefully review 2 proposals per hour. Nothing is dropped, and no proposal is approved without review. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Showing the reviewer less detail so that 5 can be reviewed per hour solves the capacity problem.
- [ ] B. Doubling the reviewer's speed to 4 per hour would stop the backlog from growing, since the review rate would nearly match arrivals.
- [ ] C. Three reviewers at 2 per hour each would match the arrival rate of 5 per hour.
- [ ] D. The backlog grows by 3 proposals per hour, since 5 arrive and only 2 can be carefully reviewed.
- [ ] E. After 4 hours, 12 proposals are waiting, because 20 have arrived and 8 have been reviewed.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It changes the quality of review, not the capacity for careful review.
- B: 5 arrivals minus 4 reviews still adds 1 per hour.
- C: 3 x 2 = 6, which is at least 5.
- D: Arrival minus service rate.
- E: 4 x 3 = 12.

**Source:** Human attention is a finite gate resource

## MA-ch13.46

Five proposals are pending. A is a reversible local formatting change. B sends material to an external recipient. C changes a production target. D duplicates B's effect. E depends on C being approved first. One reviewer has capacity to review two carefully in this period. Check each statement that is true about a sound queue policy. Each statement is worth 1 point (5 points total).

- [ ] A. A should be auto-approved to clear the queue, since it is reversible and affects only local files.
- [ ] B. The priority should follow the urgency labels the proposing agents attach to their own work.
- [ ] C. B and C should be prioritized, because their effects are external or high-impact.
- [ ] D. D should be detected as a likely duplicate of B and held rather than reviewed separately.
- [ ] E. E can be reviewed independently of C, because each proposal is separate.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Only a separately authorized low-risk policy can approve A without review.
- B: Self-assigned urgency is unvalidated and serves the proposer.
- C: Review effort should follow consequence.
- D: Approving a duplicate wastes review capacity and may double the effect.
- E: E depends on C, so deciding it first is premature.

**Source:** Human attention is a finite gate resource

## MA-ch13.47

Proposals now arrive faster than reviewers can examine them, and the backlog is growing. Check each statement that is true about responses consistent with good oversight practice. Each statement is worth 1 point (5 points total).

- [ ] A. Narrow what the agents are allowed to attempt so fewer proposals need review.
- [ ] B. Add qualified reviewers so that careful review capacity rises with the volume of proposals.
- [ ] C. Trim the information shown to reviewers so that they can click through proposals faster.
- [ ] D. Treat a proposal as approved if no reviewer has responded within a fixed period, to keep work moving.
- [ ] E. Pause intake of new proposals until the backlog is back under control.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Reducing scope reduces the volume that requires human judgment.
- B: Capacity is raised without lowering the quality of each review.
- C: Less information per decision degrades judgment rather than raising capacity.
- D: Silence is the absence of a decision.
- E: Limiting inflow preserves review quality.

**Source:** Human attention is a finite gate resource

## MA-ch13.48

A pipeline lets an action proceed when any one of these is true: no reviewer has responded within 30 minutes; the agent reports confidence above 0.95; or an automated evaluation score is at least 90%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A self-reported confidence of 0.95 can serve as authorization because the model is well calibrated.
- [ ] B. A timeout is the absence of a decision, not consent, however long the reviewer has been silent.
- [ ] C. A pre-authorized, narrowly defined standing policy for a low-risk class differs from treating silence as consent.
- [ ] D. A 90% evaluation score authorizes the action, because it shows the change meets the team's quality bar.
- [ ] E. Auto-proceeding on timeout is acceptable for destructive actions if reviewers were notified.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Calibration is unestablished here, and confidence is not an authorization in any case.
- B: Failing to answer does not constitute permission.
- C: The policy is a deliberate, accountable decision made in advance.
- D: A score is evidence about performance on a set of cases, not a decision by someone with authority.
- E: Notification is not consent, and irreversibility raises the need for an explicit decision.

**Source:** Human attention is a finite gate resource

## MA-ch13.49

A team finds that its reviewers approve 99.6% of proposals with a median review time of 8 seconds, and a dashboard ranks reviewers by throughput. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Ranking reviewers by throughput will improve the quality of oversight by rewarding efficient reviewers.
- [ ] B. More prompts always mean more oversight, because each prompt is another chance to catch a problem.
- [ ] C. Refusal and deferral rates should be tracked alongside approval rates, not only approvals.
- [ ] D. A 99.6% approval rate proves that the agent is reliable and that the proposals were good.
- [ ] E. A near-universal approval rate may reflect habituation, so the team should check whether reviewers have real options, evidence and support to say no.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Rewarding speed trains the approval gate toward ceremony.
- B: Past the available attention, additional prompts produce habituation.
- C: A gate that never says no or later is not demonstrating oversight.
- D: The rate describes decisions, not whether the decisions were informed or the proposals correct.
- E: High agreement can be a symptom of rubber-stamping.

**Source:** Human attention is a finite gate resource

## MA-ch13.50

Reviewers keep receiving nearly identical, low-consequence proposals, such as formatting changes in documentation inside a sandbox repository. The team considers replacing individual approvals for this class with a standing policy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The policy should be accompanied by monitoring and a defined way to revoke it if problems appear.
- [ ] B. The exclusions should be tested, meaning cases just outside the class must still be routed to a reviewer.
- [ ] C. The agent can set the policy's scope, because it knows which of its proposals are routine.
- [ ] D. The policy should extend automatically to adjacent classes as they come to look similar.
- [ ] E. The class should be defined precisely, so it is clear which proposals fall inside it.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A standing authorization needs a way to detect problems and withdraw it.
- B: The edge of the policy is where errors occur.
- C: Scope is a governance decision owned by accountable people, not the proposer.
- D: Extending scope without review is how standing policies drift.
- E: Vague boundaries let consequential changes slip in.

**Source:** Human attention is a finite gate resource

## MA-ch13.51

A team wants to improve the quality of human review in its approval process. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Once an action is approved, its outcome is operations' concern and not part of gate design.
- [ ] B. Inspect approvals that were later reversed to learn what the reviewer lacked at the time.
- [ ] C. An unexpected outcome that turned out harmless needs no change to the evaluation set.
- [ ] D. Average time per decision is a reliable measure of the quality of review, since careful review takes longer.
- [ ] E. Compare effects predicted in proposals with outcomes actually observed after the actions ran.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The approval gate's design should respond to what happens after approval.
- B: Reversals are informative failures of the approval gate.
- C: Unexpected behavior of any kind is a reason to update the next evaluation set.
- D: Time can fall because reviewers click reflexively.
- E: Prediction errors show where review or evidence was inadequate.

**Source:** Human attention is a finite gate resource

## MA-ch13.52

A team adopts agents that produce 10 times as many proposals per day, going from 20 to 200, while the reviewers can still carefully review 20 per day. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. At most 10% of the proposals can receive careful review, since 20 of the 200 fit within capacity.
- [ ] B. The other 90% can be checked to the same standard by skimming them quickly, since most are routine.
- [ ] C. If the unreviewed proposals proceed anyway, the extra output is effectively unverified.
- [ ] D. Review capacity should be treated as a design constraint that is measured or declared, not left implicit.
- [ ] E. Speeding up generation also speeds up verification, because the same model can be asked to review the proposals.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 20 divided by 200 is 0.10.
- B: Skimming is a different, weaker review.
- C: Generation scaled up but verification did not.
- D: Throughput limits determine which controls are actually feasible.
- E: A model checking its own family's output does not supply the independent human judgment that authorization requires.

**Source:** Human attention is a finite gate resource

## MA-ch13.53

A marketing manager is asked to approve an agent's proposed database migration. The proposal is well written and every claim sounds reasonable. The migration contains a subtle locking problem that will cause an outage. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding the agent's explanation of why the migration is safe makes it verifiable by a non-expert.
- [ ] B. The proposal should be routed to a reviewer who has the expertise to audit it, or to a specialist.
- [ ] C. Fluent, confident text is a reliable signal that a proposal is correct, because errors usually look awkward.
- [ ] D. Judging whether a claim is credible depends on the reviewer's own domain knowledge, so errors outside it tend to pass.
- [ ] E. A careful reading by any experienced manager will catch database-specific errors, whatever their own specialty.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The explanation is another claim the reviewer cannot check.
- B: Matching reviewer to proposal is part of gate design.
- C: Fluency is independent of correctness.
- D: A reviewer cannot detect problems that they lack the background to recognize.
- E: General experience does not substitute for domain expertise.

**Source:** Human attention is a finite gate resource

## MA-ch13.54

An approval screen shows only the first 30 characters of any target, followed by an ellipsis. An agent proposes writing to /srv/app/exports/archive/2026/../../../private/keys.txt, which the operating system resolves to /srv/app/private/keys.txt. The screen displays "/srv/app/exports/archive/2026/…". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Truncation is harmless because the full path is included in the fingerprint, so any change would be detected.
- [ ] B. Resolving the path to its canonical form before display would show the true target.
- [ ] C. Lookalike Unicode characters, such as a Cyrillic letter for a Latin one, are another way a displayed name can differ from the real identifier.
- [ ] D. Training reviewers to expand every path manually fixes the design problem, since the information remains available to them.
- [ ] E. The reviewer cannot see the part of the path that determines the final location, so the approval would not be informed.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A hash over text the reviewer never saw does not make the reviewer informed.
- B: Normalization collapses ".." segments and reveals where the write will land.
- C: Visually identical strings can be different byte sequences.
- D: Relying on vigilance to compensate for hidden information moves the burden to the person least able to carry it.
- E: The truncated text suggests an archive folder, while the real target is a private file.

**Source:** The approval interface is part of the control

## MA-ch13.55

A review interface parses the raw JSON text {"target":"report.md","target":"/etc/passwd"} using a parser that keeps the first value of a repeated key, and shows the reviewer "report.md". The backend that executes the action parses the same text with Python's json.loads. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Hashing the raw text guarantees that both parsers interpret it the same way, because the bytes being parsed are identical.
- [ ] B. The reviewer and the executor can see different targets even though both read the same text.
- [ ] C. Python's json.loads keeps the last value of a repeated key, so the backend would use "/etc/passwd".
- [ ] D. The JSON standard requires every parser to keep the last value, so the backend's behavior is the only correct one.
- [ ] E. Rejecting documents that contain duplicate keys at ingestion removes this ambiguity.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A digest identifies bytes; it does not make parsers agree on their meaning.
- B: Different parsers resolve duplicate keys differently, creating a parsing differential.
- C: By default, later duplicates overwrite earlier ones in Python's decoder.
- D: The standard leaves behavior for duplicate names unspecified and says names should be unique.
- E: A strict parser makes one interpretation the only one.

**Source:** Canonical content and its fingerprint

## MA-ch13.56

An engineer is drafting a written sign-off for an evaluated approval gate. Check each item that belongs in a useful sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. What was tested, with the specific checks, the criteria and the results obtained.
- [ ] B. Who cleared which gate, naming a person or role per decision who can be asked about it.
- [ ] C. Verbs worded at the strength of the evidence, so "passed a stated test" is distinguished from "believe safe".
- [ ] D. A closing statement that the system is safe for production use, so readers know the final conclusion.
- [ ] E. What was not tested, including conditions not probed and known failure modes not reached.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The reader needs to know what evidence exists.
- B: Answerability requires someone specific.
- C: Overstated verbs create false assurance.
- D: A sign-off states what was established; a blanket safety claim exceeds the evidence.
- E: A list of only what passed reads as a clean bill of health and hides where harm may lie.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.57

An engineer gives an AI assistant no test logs or notes and asks it to write the sign-off statement for the validation work she just finished. The assistant returns a fluent, well-structured paragraph that names a reviewer and states that a full review took place. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The fluent structure suggests the assistant checked the validation work before writing the paragraph.
- [ ] B. The remaining risk is only stylistic, such as tone and formatting of the paragraph.
- [ ] C. Naming a reviewer in the statement makes it trustworthy, because a named person can be held to account.
- [ ] D. The paragraph has the form of a sign-off but nothing behind it, unless the assistant was given the actual record.
- [ ] E. She can sign it if the content sounds plausible and matches what she remembers doing.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Structure is not verification.
- B: The risk is that the statement is empty of substantive claims.
- C: A name in a generated paragraph is not evidence that the person reviewed anything.
- D: A language model cannot know what was tested or skipped unless told.
- E: Plausibility is not the standard; a signature asserts facts she can support.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.58

A company requires a sign-off from the test lead before each release. In two years the lead has signed every release, and the process has no recorded way to decline or defer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Withholding a sign-off is a process failure that the process should work to minimize.
- [ ] B. Having a signature on the release proves that a full review took place before it shipped.
- [ ] C. The signer's authority to withhold or defer is essential for a sign-off to mean anything.
- [ ] D. Because a person signed, accountability for every gap rests wholly on that person, with no organizational owner needed.
- [ ] E. If the only permitted outcome is "signed", the process is a rubber stamp that hides missing review behind a name.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Treating non-approval as failure pressures people to manufacture certainty.
- B: A signature shows that someone put their name on a statement.
- C: Real assurance requires a real possibility of refusal.
- D: Governance should name organizational owners and escalation paths rather than placing all consequence on the signer.
- E: A signature that cannot be withheld carries no information.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.59

The engineer who built a validation gate sits down to write its sign-off and finds that she wants to write "no known issues." Check each statement that is true about practices that counter ownership bias. Each statement is worth 1 point (5 points total).

- [ ] A. For each untested item, say whether it was skipped because it was out of scope or because time ran out.
- [ ] B. The builder is best placed to sign, since she knows the system best, so independent review adds little.
- [ ] C. Require a minimum number of entries, such as three, in the "not tested" section.
- [ ] D. Ask whether any untested condition is the region where harm would most likely occur.
- [ ] E. If she cannot think of any untested conditions, the approval gate is fully verified and the sign-off can say so.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The reason affects how much weight the omission deserves.
- B: Knowing a system well is compatible with, and can increase, bias in assessing it.
- C: A forced list pushes against the pull toward a clean bill.
- D: Omissions matter most where consequences are largest.
- E: Being unable to list gaps usually means she has not looked hard enough.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.60

An organization introduces named sign-offs for high-risk automated actions. A year later it reviews the effects. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Named sign-offs have no effect on release speed, because the signature is a quick formality.
- [ ] B. Such a regime supports legible answerability: after a failure one can find who signed and what they did and did not warrant.
- [ ] C. An anonymous sign-off provides the same answerability as a named one, as the statement still exists.
- [ ] D. The cost includes speed and deniability, because someone must be willing to be named and "what did we not test?" arrives as friction.
- [ ] E. A digital signature on the sign-off proves that the signer read and understood the evidence.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Documenting limits and naming signers takes effort and can delay release.
- B: Written, attributable claims make accountability possible.
- C: Without a name, nobody can be asked about the claim.
- D: Accountability trades convenience for clarity.
- E: A signature can strengthen identity evidence without proving comprehension.

**Source:** Attestation: what the signer states, and the right to withhold

## MA-ch13.61

Check each statement that is true about the order of events in a sound approval workflow for an agent's proposed action. Each statement is worth 1 point (5 points total).

- [ ] A. Scoped evaluation, and the recording of what it does not cover, happens before the proposal is frozen and fingerprinted.
- [ ] B. The fingerprint, expiry, revocation, and use constraints are rechecked at execution, just before the effect.
- [ ] C. The actual outcome is observed after execution and stored as a separate record linked to the decision.
- [ ] D. If a proposal changes after approval, only the executor's check needs to be rerun, because the evaluation remains valid.
- [ ] E. The fingerprint should be computed after the reviewer clicks Approve, from the form's current state, so that last-second edits are captured.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The reviewer needs evidence and exclusions in front of them when deciding.
- B: Conditions can change between decision and use.
- C: Approval permits an attempt; the result must be checked independently.
- D: The evidence was about the previous proposal and must be re-evaluated for the new one.
- E: The fingerprint must be fixed before review so the reviewer approves exactly what is later checked.

**Source:** Where the approval step sits in the build so far

## MA-ch13.62

An approved action runs, its fingerprint check passes at execution, and a post-action check shows that the file contains the wrong content. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The proposal fingerprint, the effect evidence and the post-action check should be separate linked records.
- [ ] B. Approval permits a bounded attempt; it does not guarantee that the intended result occurs.
- [ ] C. The decision record should be amended to say that the outcome was correct, so the record is consistent.
- [ ] D. Because the fingerprint matched at execution, the outcome must have been correct, since the right proposal was run.
- [ ] E. The post-action check replaces the need for any pre-action evaluation, since it measures the real result.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Merging them hides which of the three failed.
- B: Authorization is about permission, not outcome.
- C: The outcome contradicts that claim and records should not be edited to match hopes.
- D: A match shows the executed proposal equals the approved one, not that execution had the intended effect.
- E: The checks serve different times and purposes.

**Source:** Where the approval step sits in the build so far

## MA-ch13.63

A developer sets an agent's permissions to allow any command that matches the pattern "npm run *" without prompting. A repository the agent works in defines an npm script named "cleanup" that runs rm -rf ~/projects. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Pattern-level approval binds to the form of the command, not what the script does, so the destructive script runs unprompted.
- [ ] B. Because the developer wrote the rule, every package.json the agent encounters can be treated as trusted.
- [ ] C. Permission rules make sandboxing and other controls unnecessary, since the rules already limit what runs.
- [ ] D. Pattern approval is equivalent to approving each command's contents individually, because the pattern covers only known scripts.
- [ ] E. Narrower allow rules, such as specific script names, together with deny rules for destructive commands reduce exposure.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The pattern cannot see the script's contents.
- B: Repositories can contain scripts written by others, including untrusted ones.
- C: Layered controls cover cases a single permission rule misses.
- D: Approving a prefix approves every possible continuation.
- E: Smaller grants and explicit denials limit blast radius.

**Source:** A gate is not a button

## MA-ch13.64

A team lists tasks in an approval workflow and decides which should be done by an AI assistant and which should remain with a person. Check each statement that is true about an appropriate split. Each statement is worth 1 point (5 points total).

- [ ] A. Running every checker and grouping the resulting traces for the reviewer is suitable for the assistant.
- [ ] B. Deciding to approve, refuse, defer or escalate, within the person's authority, stays with a person.
- [ ] C. Deciding which identities, beyond the named fields, should force a new decision if they change is suitable for the assistant.
- [ ] D. Drafting the structured proposal and flagging the fields it could not fill is suitable for the assistant.
- [ ] E. The cases that can embarrass the proposal should be chosen after seeing the assistant's results.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Mechanical collection of evidence is what automation does well.
- B: Authority and accountability attach to a person.
- C: That is a judgment about consequence that belongs with the accountable person.
- D: This is preparation work that saves time and exposes gaps.
- E: Cases chosen after the fact record accommodation.

**Source:** The driver's seat

## MA-ch13.65

An engineer is told that a prototype approval check has been built: it fingerprints the proposal and verifies that an approved flag and a nonblank approver string are present. Check each statement that is true about what must still be added before relying on it in production. Each statement is worth 1 point (5 points total).

- [ ] A. Expiry, revocation and single-use consumption, enforced where the action happens.
- [ ] B. Audit logging with access control, retention rules and an incident-response path.
- [ ] C. Authenticated identity for the approver, because a name string can be typed by anyone.
- [ ] D. Nothing further is needed because SHA-256 is a secure hash and the content binding is therefore strong.
- [ ] E. A registry or policy stating who has authority to approve which actions.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The prototype has no time or use limits.
- B: Production use requires accountability and handling for failures.
- C: Identity must come from a credential only the approver controls.
- D: The hash secures content identity only; it does not address identity, authority, time, or use.
- E: Authority is a separate property from identity.

**Source:** Ship It: a gate design that survives a skeptical reader

## MA-ch13.66

A team measures four things about an approval workflow: (1) whether the agent completed its tasks; (2) whether its actions complied with the organization's policy; (3) how much time and effort reviewers spent; and (4) whether a person with authority approved each consequential action. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. These are four separate questions, and a high value on one says little about the others.
- [ ] B. A high task-success rate implies that the actions complied with policy.
- [ ] C. Policy compliance by automated check amounts to human authorization.
- [ ] D. Low reviewer burden shows that decisions were well informed, since reviewers had less to read.
- [ ] E. Reporting only task success is adequate because the other three follow from it.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Each captures a distinct property.
- B: An agent can complete tasks by violating policy.
- C: A checker can flag violations but cannot give consent on anyone's behalf.
- D: Burden can fall because information was hidden or reviewers click reflexively.
- E: None of the others is implied by task success.

**Source:** Evaluation comes before authorization

## MA-ch13.67

A student's approval-gate project tests its code with a hard-coded decision record whose approver field reads "simulated-reviewer". The code binds the decision to a fingerprint of the proposal and the tests pass. Check each statement that is true about what the project may honestly claim. Each statement is worth 1 point (5 points total).

- [ ] A. It may claim that approval is authenticated, since the approver field is nonblank.
- [ ] B. It may claim that the code binds a decision record to exact proposal content under a simulated approver, and nothing about any person's review.
- [ ] C. It may claim that the proposal is safe, since the content-binding tests pass.
- [ ] D. It may claim that the proposal was reviewed and approved, since a decision record exists and the tests pass.
- [ ] E. It may present the simulated record as evidence of stakeholder agreement, if it is labeled with a reviewer's role.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A literal string is not an authenticated identity.
- B: A hard-coded test record shows that the mechanism works; it is not a decision by anyone.
- C: Binding says nothing about the proposal's safety.
- D: A generated record is not a review.
- E: Inventing stakeholder agreement misrepresents the record, whatever the label.

**Source:** Ship It: a gate design that survives a skeptical reader

## MA-ch13.68

An executor must check a stored approval decision before running an action, but the approval service it calls is unavailable and the request times out. Check each statement that is true about how the executor should behave. Each statement is worth 1 point (5 points total).

- [ ] A. It should proceed, since the outage is not the agent's fault.
- [ ] B. It should refuse to run the action and keep it queued until a decision can be verified.
- [ ] C. It should fall back to checking only that an approval record exists, without verifying its fingerprint.
- [ ] D. It should use the most recent approval for a similar action as a stand-in.
- [ ] E. It should ask the agent to confirm that approval was previously granted and proceed on its answer.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: An unverifiable check is not a pass.
- B: An authorization check that cannot be completed must fail closed.
- C: A weaker check defeats the binding the approval gate relies on.
- D: A different action's approval does not authorize this one.
- E: The party seeking approval cannot vouch for it.

**Source:** Scope, expiry, revocation, and replay

## MA-ch13.69

A deployment tool shows a reviewer a "plan" of the changes it will make. At apply time, the tool re-runs its planning step against the live environment and applies whatever it computes then. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Saving the reviewed plan as an artifact and applying exactly that artifact ties the execution to what was approved.
- [ ] B. Binding approval to a fingerprint of the saved plan lets the apply step detect any modification of it.
- [ ] C. Re-planning at apply time is safe, because the same tool computes both plans.
- [ ] D. The reviewer approved one computed plan, but the change applied is a different, freshly computed one that nobody reviewed.
- [ ] E. If the live state has drifted since the plan was made, the saved plan should be rejected and a new plan reviewed instead of silently adapted.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The artifact is the object of the decision.
- B: A digest over the plan content detects changes after review.
- C: The same tool can compute different results from different inputs.
- D: Approval and execution are not tied to the same artifact.
- E: A plan computed against a different state is a different proposal.

**Source:** Where the approval step sits in the build so far

## MA-ch13.70

Of 250 agent proposals, reviewers approved 180, refused 40 and deferred 30. Of the 180 approved proposals, 9 were later reversed because the outcome was wrong. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reversal rate among approved proposals is 20% (9 of 45).
- [ ] B. The deferral rate is 12% (30 of 250).
- [ ] C. The refusal rate is 16% (40 of 250).
- [ ] D. Among approved proposals, the reversal rate is 5% (9 of 180).
- [ ] E. The approval rate is 72% (180 of 250).

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: There is no group of 45 here; the denominator is the 180 approved proposals.
- B: 30/250 = 0.12.
- C: 40/250 = 0.16.
- D: 9/180 = 0.05.
- E: 180/250 = 0.72.

**Source:** Evaluation comes before authorization

## MA-ch13.71

An automated risk screen flags 30 of 250 proposals as risky. Of the 30 flagged, 24 are truly risky; across all 250 proposals, 40 are truly risky. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The screen's recall is 60% (24 of 40 truly risky proposals were flagged).
- [ ] B. The screen's recall is 80%, because 24 of the 30 flagged were truly risky.
- [ ] C. The screen missed 6 risky proposals.
- [ ] D. Because precision is high, unflagged proposals can skip human review.
- [ ] E. The screen's precision is 80% (24 of 30 flagged are truly risky).

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Recall is true positives divided by actual positives.
- B: That figure is precision; recall uses all truly risky proposals as the denominator.
- C: Six is the number of false alarms (30 - 24); the number missed is 40 - 24 = 16.
- D: Sixteen risky proposals went unflagged, so the unflagged group still contains risk.
- E: Precision is true positives divided by flagged items.

**Source:** Evaluation comes before authorization

## MA-ch13.72

An agent's request to rotate a production credential lists the rollback as "restore the previous credential from the secrets vault". Before the request goes to a reviewer, the team wants to evaluate that rollback claim. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If rehearsal shows only partial recovery is possible, the request should say so.
- [ ] B. The check should confirm that the previous credential is still stored and not purged or rotated away at the provider.
- [ ] C. A well-written rollback description is sufficient evidence that rollback will work.
- [ ] D. The evaluation should look for effects that restoring does not undo, such as requests rejected during the gap.
- [ ] E. The restore procedure can be rehearsed in a sandbox to see whether it works end to end.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: An honest partial rollback beats an unsupported complete one.
- B: The plan depends on an artifact that may no longer exist.
- C: Fluent text can describe a procedure that fails when attempted.
- D: Restoration to a prior state is not the same as undoing consequences.
- E: A rehearsal tests the claim instead of trusting it.

**Source:** Scope, expiry, revocation, and replay
