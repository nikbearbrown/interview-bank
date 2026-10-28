# Chapter 4: The agent loop

## MA-ch04.1

Check each statement that is true about the chapter's opening scenario, in which a system looks up the same record again and again. Each statement is worth 1 point (5 points total).

- [ ] A. From outside, the relevant question is what changed that makes completion more justified than it was one turn ago.
- [ ] B. From outside, the relevant question is how many lookups succeeded.
- [ ] C. From inside a poorly described report, activity can look like progress.
- [ ] D. Every lookup can succeed and every observation can be logged while the task gets no closer to a supported answer.
- [ ] E. A longer trace is evidence that completion is more justified than it was one turn ago.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: This is the chapter's outside-view question.
- B: Counting successful lookups does not say whether completion became more justified.
- C: Activity and progress are easy to confuse in a poor report.
- D: The trace gets longer, but the task does not get closer to a supported answer.
- E: A longer trace is only more recorded activity.

**Source:** Chapter 4 opening (before the first section heading)

## MA-ch04.2

Check each statement that is true about the two constructed runs that the chapter opens with. Each statement is worth 1 point (5 points total).

- [ ] A. The stop in the repeated-lookup run was discovered by the program while it ran, not chosen beforehand.
- [ ] B. A repeated-lookup policy with a turn budget of two stops after two recorded actions.
- [ ] C. In the run that looks up blue and then finishes with red, the controller compares the answer with the observation before it returns.
- [ ] D. The repeated-lookup run returns the status `finished`.
- [ ] E. The program invents a final answer in the repeated-lookup run so that the run appears complete.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Someone chose the number two before the loop ran, so the stop was designed.
- B: Two actions are consumed and recorded, then the loop is out of turns.
- C: The controller never compares the answer with the observation.
- D: It returns `budget-exhausted`, since the turns ran out.
- E: The program does not invent a final answer to look complete.

**Source:** Chapter 4 opening (before the first section heading)

## MA-ch04.3

Check each statement that is true about how the chapter applies Chapter 1's three jobs (conduct, check, drive) to the line that ends the run. Each statement is worth 1 point (5 points total).

- [ ] A. Drive: Claude takes the stop that closes the task, and you take the stop that ends the run.
- [ ] B. Conduct: the exits and the budget are decisions you write down before the loop starts.
- [ ] C. Check: `finished` is enough evidence that the final answer is supported.
- [ ] D. Drive: Claude may take the stop that ends the run, and the stop that closes the task is yours.
- [ ] E. Check: `finished` records that a finish action arrived, and what anyone may believe beyond that is a separate question with a separate check.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The roles are reversed in this statement.
- B: The exits and budget are written down first.
- C: A status does not support the answer.
- D: This is the chapter's split of the two stops.
- E: `finished` says only that a finish action arrived.

**Source:** Chapter 4 opening (before the first section heading)

## MA-ch04.4

Check each statement that is true about why the chapter uses a scripted policy instead of a live model call. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 3 separated capability from authority, and this chapter adds sequence and termination.
- [ ] B. A scripted policy reproduces Claude's private reasoning.
- [ ] C. The scripted loop reproduces Claude's current agent implementation.
- [ ] D. A scripted policy makes each decision inspectable and repeatable.
- [ ] E. Answering which action arrives next, what observation follows, what is recorded, and which condition ends the run grants permission to act.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: That is how the chapter links itself to Chapter 3.
- B: The chapter says the choice does not reproduce Claude's private reasoning.
- C: It also does not reproduce the current agent implementation.
- D: The machinery is small enough to explain from the first action to the final return.
- E: Answering those questions grants no permission to act.

**Source:** Chapter 4 opening (before the first section heading)

## MA-ch04.5

Check each statement that is true about what the stop conditions written as a gate must include before any implementation exists. Each statement is worth 1 point (5 points total).

- [ ] A. The finished controller code, written first so the exits can be read off it.
- [ ] B. The unit of the budget.
- [ ] C. Every exit of the loop.
- [ ] D. A separate check that decides whether a finished answer moves on.
- [ ] E. What must never be fabricated.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The gate is written before any implementation exists.
- B: The unit of the budget is part of the gate.
- C: Naming every exit is part of the gate.
- D: The gate names the separate check.
- E: The gate names what must never be fabricated.

**Source:** What you will be able to do

## MA-ch04.6

Check each statement that is true about the three jobs inside any agent loop. Each statement is worth 1 point (5 points total).

- [ ] A. One job is dispatching the action, recording the result, and deciding whether the run continues.
- [ ] B. In a chat window the three jobs arrive as three separate voices.
- [ ] C. One job is proposing the next action.
- [ ] D. One job is deciding whether the final result is any good.
- [ ] E. In this reference, the controller performs the job of judging the final result.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: This is the controller's job.
- B: In a chat window they arrive as one voice saying done.
- C: Proposing is the first job.
- D: Judging the result is the third job.
- E: The third job does not exist in this reference.

**Source:** The policy proposes, the controller stops, someone else judges

## MA-ch04.7

Check each statement that is true about the policy in this reference. Each statement is worth 1 point (5 points total).

- [ ] A. The policy is a learned model.
- [ ] B. The policy is an iterable of action dictionaries.
- [ ] C. A prepared list is not enough to serve as the policy; the controller needs a model.
- [ ] D. Using the name "policy" means a route from observations to the next decision is implemented.
- [ ] E. The policy changes its next action based on what the controller observed.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The list is not a learned model.
- B: The controller creates an iterator over the action dictionaries.
- C: The controller only asks an iterator for the next item, so a prepared list is enough.
- D: The chapter warns against calling that route implemented merely because the code says policy.
- E: Nothing feeds the observation back to the policy.

**Source:** The policy proposes, the controller stops, someone else judges

## MA-ch04.8

Check each statement that is true about the separation of the policy, the controller, and the judge. Each statement is worth 1 point (5 points total).

- [ ] A. Something the policy says can create another iteration after the range is spent.
- [ ] B. A model-backed policy should inherit the power to redefine the runtime's limits because it supplies the next action.
- [ ] C. A poor action sequence dispatched exactly as specified is a fault in the sequence.
- [ ] D. The right sequence with the wrong status is a fault in the controller.
- [ ] E. The turn budget belongs to the policy.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Nothing the policy says creates another iteration.
- B: A new source of actions should not redefine the limits.
- C: The controller did what it was told, so the sequence is at fault.
- D: A correct sequence with a wrong status points at the controller.
- E: The budget belongs to the controller.

**Source:** The policy proposes, the controller stops, someone else judges

## MA-ch04.9

Check each statement that is true about what the turn budget does and does not bound. Each statement is worth 1 point (5 points total).

- [ ] A. The turn budget guarantees the run ends within a fixed number of seconds.
- [ ] B. The loop places a timeout around an arbitrary iterator or slow tool.
- [ ] C. An iterator that keeps yielding lookups can push the loop past its turn budget.
- [ ] D. The loop bounds how many turns it begins.
- [ ] E. If fetching the next item never returns, an iteration count cannot interrupt the wait.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The budget is not a wall-clock guarantee.
- B: No timeout is placed around the iterator or tool.
- C: The range, not the policy, decides how many turns run.
- D: The count limits turns begun.
- E: A count cannot cut short a wait that never ends.

**Source:** The policy proposes, the controller stops, someone else judges

## MA-ch04.10

Check each statement that is true about the two stops hidden under the word "done". Each statement is worth 1 point (5 points total).

- [ ] A. The controller can take the stop that closes the task.
- [ ] B. `finished` records that a finish request arrived, not that the result was accepted.
- [ ] C. Nothing in the `run` function can take the stop that closes the task.
- [ ] D. One stop ends the run: the controller returns.
- [ ] E. The other stop closes the task: a person, or a check a person designed, accepts the result as meeting the need that started the run.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The controller takes only the first stop.
- B: Acceptance is the other stop, taken by a person or a designed check.
- C: The function has no judging step.
- D: Returning ends the run.
- E: Closing the task is an acceptance by a person or a designed check.

**Source:** The policy proposes, the controller stops, someone else judges

## MA-ch04.11

Check each statement that is true about the turn budget check at the top of the controller. Each statement is worth 1 point (5 points total).

- [ ] A. A bad budget is rejected before the iterator or the trace exists.
- [ ] B. The check `type(max_turns) is int` accepts anything that behaves like a number.
- [ ] C. The budget must be an integer of at least one.
- [ ] D. The lesson's tests include rejection of a budget of zero.
- [ ] E. A bad budget produces the status `budget-exhausted`.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Validation happens before anything else is created.
- B: It is an explicit type choice, not acceptance of anything number-like.
- C: Positive integers only.
- D: The chapter cites the zero test.
- E: A bad budget raises an error (ValueError in the gate table) instead of returning a status.

**Source:** Every return statement is an exit someone decided

## MA-ch04.12

Check each statement that is true about what happens when the policy runs out of actions. Each statement is worth 1 point (5 points total).

- [ ] A. The controller treats policy silence as completion and returns `finished`.
- [ ] B. The controller then returns `budget-exhausted`, because no turns are left.
- [ ] C. `next(iterator)` raises `StopIteration` when the policy has no next action.
- [ ] D. The `incomplete` result carries an answer field containing an empty string.
- [ ] E. An exhausted supply of scripted actions is the same condition as an explicit finish.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The controller does not read silence as completion.
- B: It returns `incomplete`; the budget was not spent.
- C: This is how an exhausted iterator signals the end.
- D: Only a finish with no answer yields an empty string; `incomplete` manufactures no answer.
- E: Silence and an explicit finish are different conditions.

**Source:** Every return statement is an exit someone decided

## MA-ch04.13

Check each statement that is true about how the controller treats different action names. Each statement is worth 1 point (5 points total).

- [ ] A. The not-allowed observation establishes permissions for any larger runtime.
- [ ] B. A finish action returns immediately with status `finished`, the answer it carried, and the existing trace.
- [ ] C. A lookup of a key that is not in the records produces the observation `not found`.
- [ ] D. Any name other than lookup and finish becomes an entry with the observation `error: tool not allowed`.
- [ ] E. An unknown action name consumes a turn, and the run continues if a turn remains.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It does not establish permissions beyond this function; Chapter 5 builds that boundary.
- B: This is the finish branch.
- C: The lookup branch supplies `not found` for missing keys.
- D: Unknown names are appended with the error observation.
- E: The error observation is appended and the loop goes on.

**Source:** Every return statement is an exit someone decided

## MA-ch04.14

Check each statement that is true about what the chapter says the reference leaves open. Each statement is worth 1 point (5 points total).

- [ ] A. The trace holds the lookup key but not the action name.
- [ ] B. A finish action with no answer field returns `finished` with an empty string.
- [ ] C. The trace holds the finish action as its last entry.
- [ ] D. A bare-string action fails with an `AttributeError`, outside the three normal statuses.
- [ ] E. The reference includes a schema validator like the one in Chapter 2.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The trace holds the action name, not the lookup key.
- B: The reference lets a stop with no substance through.
- C: The return comes before the append, so the finish is never recorded.
- D: The code expects `.get`, so a bare string breaks it.
- E: There is no schema validator in the reference.

**Source:** Every return statement is an exit someone decided

## MA-ch04.15

Check each statement that is true about the chapter's advice on predicting before reading the controller. Each statement is worth 1 point (5 points total).

- [ ] A. A prediction written after seeing the output serves as well as one written before.
- [ ] B. You should predict what happens if the policy supplies no actions.
- [ ] C. The aim is to predict the kind of termination.
- [ ] D. Answering all three prediction cases simply with success or failure is the precision the chapter wants.
- [ ] E. You should predict what happens if the policy supplies a finish action with no supporting lookup.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A prediction written afterward only describes the output.
- B: The empty policy is one of the three cases.
- C: Predicting the kind of termination makes the code inspectable.
- D: The chapter says not to answer all three with success or failure.
- E: A finish without a lookup is another.

**Source:** Every return statement is an exit someone decided

## MA-ch04.16

Check each statement that is true about a lookup action `{"name": "lookup", "key": "color"}` against the records `{"color": "blue"}`. Each statement is worth 1 point (5 points total).

- [ ] A. An answer of blue after a lookup that returned blue shows that blue is the true color in the world.
- [ ] B. The trace is a record of the policy's private reasoning.
- [ ] C. Because the mapping is a fixture, an answer that agrees with it is trustworthy outside the exercise.
- [ ] D. The observation is the string `blue`.
- [ ] E. The trace stores the observation beside the turn number and action name.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Agreeing with a table we invented does not make the answer true outside the exercise.
- B: It is evidence of the local operation's result, not of reasoning.
- C: The evidence boundary is the fixture, and a report should say so.
- D: The lookup returns the stored value.
- E: Each trace entry holds turn, action name, and observation.

**Source:** A trace records an event, not knowledge

## MA-ch04.17

Check each statement that is true about gaps in the trace and how to fill them. Each statement is worth 1 point (5 points total).

- [ ] A. With no lookup key in the trace, a reader cannot tell which of several keys returned a shared value.
- [ ] B. The worked example keeps the scripted policy in the evidence packet because the trace lacks the key.
- [ ] C. Because the return comes before the append, the terminal action is missing from the trace.
- [ ] D. The chapter recommends adding every possible field to the trace by habit.
- [ ] E. Some tasks carry sensitive inputs, and the reference defines no retention or redaction policy.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Two keys can return the same value.
- B: The policy preserves the key information the trace lacks.
- C: The finish branch returns before the append lines run.
- D: The chapter says not to add fields by habit; ask what supports the claim.
- E: That is why retention and redaction are left as open decisions.

**Source:** A trace records an event, not knowledge

## MA-ch04.18

Check each statement that is true about repeating a lookup against an unchanged mapping. Each statement is worth 1 point (5 points total).

- [ ] A. The controller's state update is only the append.
- [ ] B. It counts as new evidence for the task.
- [ ] C. It adds another observation of the same operation.
- [ ] D. The controller computes no progress measure.
- [ ] E. Success at the tool boundary implies progress at the task boundary.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The controller does not alter the records or send observations back to the policy.
- B: It is more recorded activity, not new evidence.
- C: The same operation returns the same observation again.
- D: Nothing in the controller measures progress.
- E: A lookup can succeed without the task moving closer to a supported answer.

**Source:** A trace records an event, not knowledge

## MA-ch04.19

Check each statement that is true about the first run in the section on a finished wrong answer: records `{"color": "blue"}`, and a policy of a lookup of `color` followed by a finish with answer `red`, with the default budget of four. Each statement is worth 1 point (5 points total).

- [ ] A. The returned trace has one entry, for the lookup.
- [ ] B. The default budget of four leaves room for both actions.
- [ ] C. The returned answer is `red`.
- [ ] D. The returned status is `finished`.
- [ ] E. The controller returns `budget-exhausted` because the answer contradicts the observation.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The finish returns before the append, so only the lookup is recorded.
- B: Two turns fit inside a budget of four.
- C: The answer is whatever the finish action carried.
- D: The finish action is consumed on turn two.
- E: The controller never compares answer and observation, and the budget is not spent.

**Source:** A finished wrong answer

## MA-ch04.20

Check each statement that is true about what the `finished` status means in the blue-then-red run. Each statement is worth 1 point (5 points total).

- [ ] A. The `finished` status means the answer was checked against the observation.
- [ ] B. The controller does not compare red with the blue observation.
- [ ] C. The mistake is the status name `finished`, which should be replaced.
- [ ] D. The status `finished` is inaccurate, because the answer contradicts the observation.
- [ ] E. A finish action with no answer field registers as a failure.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Nothing in the controller checks the answer.
- B: No comparison happens in the controller.
- C: The mistake is reading `finished` as verified task success, not the name.
- D: The status accurately describes the event: a finish was received.
- E: An empty string comes back as `finished`, and neither case registers as a failure.

**Source:** A finished wrong answer

## MA-ch04.21

Check each statement that is true about the repair for a finished wrong answer. Each statement is worth 1 point (5 points total).

- [ ] A. The repair is to separate controller status from outcome evaluation.
- [ ] B. A result can be finished at the control-flow layer and contradicted at the evidence layer.
- [ ] C. The repair is to rename every termination status "failure".
- [ ] D. Renaming every status would throw away distinctions the controller reports correctly.
- [ ] E. An unqualified "success" says more than a two-part report.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Status and outcome are reported separately.
- B: Both labels can be true at their own layers.
- C: The chapter says not to do this.
- D: The statuses are accurate about the events they name.
- E: The two-part report says more than a single success or failure.

**Source:** A finished wrong answer

## MA-ch04.22

Check each statement that is true about the Ash case from the companion chapter on agents. Each statement is worth 1 point (5 points total).

- [ ] A. The email had been removed from the provider's server.
- [ ] B. Ash reset its local email setup and reported the account reset complete.
- [ ] C. Ash had a deletion tool but chose not to use it.
- [ ] D. Ash was asked to delete one email.
- [ ] E. The chapter uses the case to estimate how often agents fail this way.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The email was still on the provider's server.
- B: The local reset was reported as complete.
- C: Ash had no deletion tool.
- D: The task was to delete one email.
- E: The chapter uses it to name a shape, not to estimate frequency.

**Source:** A finished wrong answer

## MA-ch04.23

Check each statement that is true about the scope the chapter holds when it cites the Ash account. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter uses the account to name a shape, not to estimate how often agents fail this way.
- [ ] B. The study involved one framework and two models.
- [ ] C. The author says he has not checked the study himself.
- [ ] D. The chapter presents the account as proof that most deployed agents misreport completion.
- [ ] E. The account comes from one exploratory study.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The point is the shape, with finish(red) as the small constructed version.
- B: One framework, two models, two weeks.
- C: The chapter states this limitation.
- D: No frequency claim is made.
- E: The chapter calls it one exploratory study.

**Source:** A finished wrong answer

## MA-ch04.24

Check each statement that is true about the outcome checker described for the blue-record task. Each statement is worth 1 point (5 points total).

- [ ] A. A deterministic comparison against the records fails in a different way from the generator.
- [ ] B. It must fail differently from whatever produced the answer.
- [ ] C. Because Claude can write the comparator quickly, the criterion is Claude's.
- [ ] D. Asking Claude whether red is consistent with the trace puts the same kind of process on both sides of the check.
- [ ] E. It must read the record for the key the policy happened to look up.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A comparison against the records is a different kind of process.
- B: Independent failure modes are the first property.
- C: Claude can write the comparator, but the criterion is yours.
- D: The same process asked twice gives one opinion, not two.
- E: It must read the record for the key the task names.

**Source:** A finished wrong answer

## MA-ch04.25

A policy looks up an absent key and then finishes with the answer `not found`. Check each statement that is true about this run. Each statement is worth 1 point (5 points total).

- [ ] A. The controller returns `incomplete` for this run.
- [ ] B. The answer still does not answer the question about color.
- [ ] C. The run shows that the checker can read the record for whichever key the policy looked up.
- [ ] D. The finish answer agrees with the last observation.
- [ ] E. A checker that compares the answer only with the last observation would catch the problem.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A finish was consumed, so the status is `finished`.
- B: The question was about the color record.
- C: The checker must read the record for the key the task names.
- D: The observation was `not found` and so is the answer.
- E: Such a checker would pass the answer.

**Source:** A finished wrong answer

## MA-ch04.26

A repeated-lookup policy runs with a turn budget of two. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Each turn consumes one action and records one observation.
- [ ] B. The budget bounds elapsed time as well as completed turns.
- [ ] C. The policy need not be finite for the limit to hold.
- [ ] D. The saved research run preserves this outcome with two trace entries.
- [ ] E. After the second append the loop has no turn left and returns `budget-exhausted`.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Each turn is one action and one observation.
- B: The budget bounds completed turns, not time.
- C: An iterator that keeps yielding lookups is consumed only as many times as the range permits.
- D: The chapter cites two trace entries.
- E: The range is spent, so the loop falls through.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.27

Check each statement that is true about the chapter's discussion of the companion book's table of the remaining cases. Each statement is worth 1 point (5 points total).

- [ ] A. Budget caps and rate limits are treated as controls that work when wired in explicitly.
- [ ] B. The table files looping and resource-exhaustion failures under an agent that already had a termination heuristic.
- [ ] C. The chapter says the study proves budget caps eliminate looping failures.
- [ ] D. A limit discovered afterward is an incident report.
- [ ] E. A limit chosen before the run is a property of the controller.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The control works when it is wired in explicitly.
- B: Those failures are filed under an agent with no concept of its resource limits and no termination heuristic.
- C: The chapter says to hold the design point whatever you make of the study.
- D: Finding the limit after the fact is an incident.
- E: Choosing the limit first makes it part of the controller.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.28

A finite policy of one lookup runs with a turn budget of four. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The result is `incomplete`.
- [ ] B. On the second turn, asking for another action raises `StopIteration`.
- [ ] C. The result `incomplete` means the task is impossible.
- [ ] D. On the first turn the observation is recorded.
- [ ] E. The result is `budget-exhausted`, because the turns ran out.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The sequence ended before a finish arrived and before the turns ran out.
- B: The iterator is empty on the second request.
- C: `incomplete` does not establish that the task is done or impossible.
- D: The lookup is dispatched and appended.
- E: Two of the four turns went unused.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.29

The same one-lookup policy now runs with a turn budget of one. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The lesson's one-turn budget test covers this case.
- [ ] B. After the lookup the loop exits without asking the iterator for another item.
- [ ] C. The result is `budget-exhausted`.
- [ ] D. The controller can tell from the exhausted iterator that no more actions were waiting.
- [ ] E. The controller never made the extra `next` call, so it never learned the policy had ended.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The chapter says the lesson's test covers it.
- B: The range is spent after one turn.
- C: The loop used its only turn, so it reaches the budget boundary first.
- D: It never asked, so it cannot know.
- E: The controller reports the boundary it reached first.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.30

Check each statement that is true about the two results (`incomplete` under a budget of four, `budget-exhausted` under a budget of one) for the same one-lookup policy. Each statement is worth 1 point (5 points total).

- [ ] A. Trace length alone can reconstruct the stop reason.
- [ ] B. The statuses report different boundaries the controller actually reached.
- [ ] C. The configured budget and the returned status are decoration beside the trace.
- [ ] D. The results should be explained by the execution path, not by knowledge the controller did not acquire.
- [ ] E. The trace is the same in both runs: one lookup entry.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Equal traces cannot tell the two stops apart.
- B: The two results do not contradict each other.
- C: They are part of the evidence.
- D: The path taken explains the status.
- E: One lookup gives one trace entry either way.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.31

Check each statement that is true about the unit of the turn budget. Each statement is worth 1 point (5 points total).

- [ ] A. The terminal action costs one turn.
- [ ] B. The turn budget counts only tool calls, so a finish is free.
- [ ] C. The number and unit of the budget can be chosen after the run, once the stop reason is known.
- [ ] D. A policy of a lookup followed by a finish cannot finish through that finish if the budget allows only the first turn.
- [ ] E. If you meant tool calls, the same implementation and tests still apply.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The unit is action-consumption turns, and the finish is an action.
- B: The budget counts turns that consume one action, finish included.
- C: The number and unit are the human's, written before the run.
- D: The finish needs its own turn to be consumed.
- E: A tool-call budget needs a different implementation and different tests.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.32

Check each statement that is true about what the three normal statuses do and do not establish. Each statement is worth 1 point (5 points total).

- [ ] A. `budget-exhausted` records that the controller used every turn it was given.
- [ ] B. `budget-exhausted` places a bound on elapsed time.
- [ ] C. `budget-exhausted` establishes that the policy had nothing more to propose.
- [ ] D. `incomplete` establishes that the task is impossible.
- [ ] E. `finished` establishes that the answer follows from the observations.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: That is exactly what the status records.
- B: The status gives no bound on time.
- C: The controller never checks what the policy had waiting.
- D: `incomplete` does not show the task is done or impossible.
- E: `finished` records only that a finish action was consumed.

**Source:** Budget exhaustion is not policy exhaustion

## MA-ch04.33

Check each statement that is true about repetition detection and the turn budget. Each statement is worth 1 point (5 points total).

- [ ] A. The reference contains no repetition detector, so adding one is a learner extension.
- [ ] B. The turn budget notices when two actions are the same.
- [ ] C. Matching on name and key always marks a useless repeat.
- [ ] D. Two different records can legitimately hold the same value, so an identical-observation rule can mislabel a needed second lookup.
- [ ] E. Matching only on the action name is too coarse, since two lookups can request different keys.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The reference has no detector.
- B: The budget limits completed iterations and does not notice repeats.
- C: If the environment can change, a repeated name and key can still be useful.
- D: A task that must check both records has not wasted the second lookup.
- E: The key matters when deciding whether an action repeats.

**Source:** Repetition detectors have false positives too

## MA-ch04.34

Check each statement that is true about designing a repetition detector. Each statement is worth 1 point (5 points total).

- [ ] A. A detector needs a stated target failure and a test that challenges its stopping behavior.
- [ ] B. A detector's assumptions should be stated together with its rule.
- [ ] C. The budget can be dropped if the detector works on the examples you chose.
- [ ] D. The chapter's detector examples are measured performance.
- [ ] E. A name-and-key rule cannot stop useful work, because it is the most specific rule available.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A target failure and a challenging test are required.
- B: Without the assumptions the rule cannot be judged.
- C: The budget stays a separate backstop.
- D: They are design cases, not measured performance.
- E: If the environment can change, a repeat of name and key can still be useful.

**Source:** Repetition detectors have false positives too

## MA-ch04.35

Check each statement that is true about reporting suspected repetition versus stopping the run. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can propose the detector, write its tests, and hunt for the repeat that fools it.
- [ ] B. Reporting suspected repetition and letting the run continue trades decisive stopping for a reviewable signal.
- [ ] C. Which option is right depends on what a wasted turn costs and what an interrupted useful run costs.
- [ ] D. Whether a suspicion is enough to end someone's run is Claude's call.
- [ ] E. The cost of a wasted turn and of an interrupted useful run are specified in the code.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: These are the quick tasks the chapter hands to Claude.
- B: Flagging keeps the run alive and leaves a signal for review.
- C: The two costs decide the choice.
- D: It is a call about cost and authority, and it is yours.
- E: Neither number is in the code.

**Source:** Repetition detectors have false positives too

## MA-ch04.36

Check each statement that is true about what Conducting AI says about agentic execution, as reported in the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Its working rule is to select the lowest layer that does the job and route deterministic work out of the model.
- [ ] B. It describes that layer as reliable for well-scoped, low-branching tasks that have verification gates built in.
- [ ] C. The stack and its reliability labels are an industry standard.
- [ ] D. It describes that layer as unreliable for long-horizon autonomy, where an early mistake propagates through every step that depends on it.
- [ ] E. It places agentic execution at the top of a five-layer capability stack.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: That is the working rule quoted in the chapter.
- B: Scoped, low-branching, gated tasks are where it is reliable.
- C: The chapter calls the stack the book's own teaching device.
- D: That is the stated weakness of the top layer.
- E: Agentic execution is the top layer.

**Source:** Before the exits: does this task need a loop?

## MA-ch04.37

Check each statement that is true about applying the lowest-layer rule to the color fixture. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter builds the loop because the exits are the subject, not because the task needs one.
- [ ] B. The question "what is the color record" is answered by `records["color"]`.
- [ ] C. A loop earns its place when the task can be answered by a single dictionary lookup.
- [ ] D. This controller's scripted policy already adapts to what the previous action found.
- [ ] E. That question needs a loop, exits, and a finish to be answered.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The loop is a skeleton for studying exits.
- B: One dictionary lookup answers it.
- C: A single lookup needs no loop; a loop earns its place when the next action depends on what the previous one found.
- D: The scripted policy does not yet react to observations.
- E: There is no loop, no exit, and no finish to doubt.

**Source:** Before the exits: does this task need a loop?

## MA-ch04.38

Check each statement that is true about the exit table in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. A finish action that is consumed returns `finished` with the answer it carried.
- [ ] B. A budget that is not a positive integer returns the status `incomplete`.
- [ ] C. A spent turn budget returns `budget-exhausted` with no answer.
- [ ] D. For a finished exit, the trace holds every completed non-finish turn.
- [ ] E. A policy with no next action returns `budget-exhausted`.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The finish branch carries the answer.
- B: A bad budget raises a ValueError instead of returning a status.
- C: The table gives no answer for this exit.
- D: The finish itself is never appended.
- E: That condition returns `incomplete`.

**Source:** The gate: write the exits before anyone runs the loop

## MA-ch04.39

Check each statement that is true about how the exit table is marked and who made the choices. Each statement is worth 1 point (5 points total).

- [ ] A. The reference happens to make the same choices as the author's table.
- [ ] B. Every line of the table is marked with who decided it: you, the lesson's tests, or Claude.
- [ ] C. At the design stage, Claude has decided none of the lines.
- [ ] D. A model produced the exit table choices.
- [ ] E. The unit of the budget is a turn that consumes one action, and a finish costs one.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The chapter says so.
- B: The marking records ownership.
- C: At this stage the choices are the human's.
- D: The chapter says no model produced the choices.
- E: The terminal action costs one turn.

**Source:** The gate: write the exits before anyone runs the loop

## MA-ch04.40

Check each statement that is true about the contract and the check that is not the controller. Each statement is worth 1 point (5 points total).

- [ ] A. A budget that is not a positive integer is accepted and clamped to one.
- [ ] B. The outcome check reads the trace, not the records.
- [ ] C. No exit fabricates an answer.
- [ ] D. A finish is a request to stop, and the result says only that one arrived.
- [ ] E. The outcome check changes the controller's status when it finds a mismatch.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: It is rejected before the policy is touched.
- B: The check reads the records for the key the task names.
- C: This is the contract's first line.
- D: The result claims nothing beyond the arrival of a finish.
- E: The check never changes the controller's status.

**Source:** The gate: write the exits before anyone runs the loop

## MA-ch04.41

Check each statement that is true about when an answer may leave the controller. Each statement is worth 1 point (5 points total).

- [ ] A. A `budget-exhausted` run may pass a partial answer downstream.
- [ ] B. A status other than `finished` sends the status and the trace to a person, and nothing else.
- [ ] C. For a real task, a person also reads the trace before the answer is used.
- [ ] D. Once the check passes, a person no longer needs to read the trace for a real task.
- [ ] E. The answer leaves only if the status is `finished` and the separate check passes.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Nothing else is sent, and no exit fabricates an answer.
- B: No answer and no extra material moves on.
- C: The chapter adds a human read of the trace.
- D: The human read remains for a real task.
- E: Both conditions must hold.

**Source:** The gate: write the exits before anyone runs the loop

## MA-ch04.42

Check each statement that is true about the wrong versions of the controller your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. A rewrite that quietly turns the red answer into a failure status is harmless because the finished/contradicted distinction survives it.
- [ ] B. A controller that tests the budget after dispatching runs one action too many, and only a test that counts trace entries against an endless iterator catches it.
- [ ] C. A rewrite that quietly turns the red answer into a failure status can satisfy a test that only asks for rejection.
- [ ] D. A controller that returns `finished` when the policy runs out is caught by the empty-policy test.
- [ ] E. Trace length alone cannot tell `incomplete` from `budget-exhausted`.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Such a rewrite destroys the distinction between the layers.
- B: An endless iterator exposes the extra action.
- C: A rejection-only test cannot tell the layers apart.
- D: An empty policy must return `incomplete`, not `finished`.
- E: One lookup gives one trace entry under a budget of one and of four.

**Source:** The gate: write the exits before anyone runs the loop

## MA-ch04.43

Check each statement that is true about reopening and refining the gate. Each statement is worth 1 point (5 points total).

- [ ] A. When building the controller shows a missed exit, the right response is to reopen the gate, date the revision, and keep the original.
- [ ] B. The one-sentence failure description may be written after the run, since the output will confirm it.
- [ ] C. Claude can sharpen the gate, and what it returns replaces your decisions.
- [ ] D. Building the controller may show an exit you missed, such as the non-dictionary action.
- [ ] E. When building the controller shows a missed exit, the right response is to overwrite the original gate so it looks right from the start.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Dated revisions with the original kept preserve the record.
- B: Written afterward, it describes the output instead of testing understanding.
- C: What Claude returns is proposals for you to accept or reject.
- D: The chapter names this as an example.
- E: Overwriting hides what you understood before.

**Source:** The gate: write the exits before anyone runs the loop

## MA-ch04.44

Check each statement that is true about the Build It step. Each statement is worth 1 point (5 points total).

- [ ] A. You write it against the gate, not from memory of the chapter.
- [ ] B. You start with the empty policy, one lookup, and a finish.
- [ ] C. You return one shared status for all exits so downstream code stays simple.
- [ ] D. You write your own controller before opening the reference.
- [ ] E. You start by connecting a paid model call so the behavior is realistic.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The gate is the specification.
- B: These are the three starting cases.
- C: A distinct status is preserved for each exit.
- D: Build before reference.
- E: Scripted actions let you isolate the behavior before adding variability.

**Source:** Build It: separate the exits before adding complexity

## MA-ch04.45

Check each statement that is true about the interface facts and tests in Build It. Each statement is worth 1 point (5 points total).

- [ ] A. The trace grows on every action, including the finish.
- [ ] B. The returned `finished` result carries an answer, and the other statuses manufacture none.
- [ ] C. The existing tests already include a wrong finished answer and a finish beyond the available turns.
- [ ] D. Your own version is discarded once Claude's controller passes the tests.
- [ ] E. An extension that stops, retries, or escalates on an unknown name is a new policy, to be recorded as new and tested.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The trace grows only on non-finish actions.
- B: Downstream code can depend on this.
- C: The existing tests cover the empty policy, finish, budget exhaustion, lookup results, a disallowed tool, and an invalid budget; you add the rest.
- D: Your version is the baseline against which you measure Claude's controller.
- E: The reference simply records an error observation and continues.

**Source:** Build It: separate the exits before adding complexity

## MA-ch04.46

Check each statement that is true about conducting Claude Code against your gate. Each statement is worth 1 point (5 points total).

- [ ] A. You give Claude the gate (exit table, contract, outcome check, wrong versions) and not your implementation.
- [ ] B. A failing test is often a gap in your gate that Claude could not see, because it had only what you wrote.
- [ ] C. If a deliberately wrong controller from Claude still passes your tests, your test list was too strong.
- [ ] D. A difference between Claude's controller and your baseline is a decision about an exit, and exits are Claude's to decide.
- [ ] E. You run your tests yourself on what Claude returns.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The gate is the specification handed over.
- B: Claude works from what the gate says.
- C: It would mean the tests were too weak, which you learned cheaply.
- D: Exits are yours.
- E: Claude's report is not the check.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch04.47

Check each statement that is true about preserving and mapping a Claude Code run. Each statement is worth 1 point (5 points total).

- [ ] A. If the mapping fits, you may claim the production system uses this Python loop.
- [ ] B. You preserve the prompt, plan, diff, commands, and outputs, with the date and displayed model label.
- [ ] C. A visible trace of a Claude Code task is a window into the model's private reasoning.
- [ ] D. If the session failed or did not run, you record that rather than substituting a fixture.
- [ ] E. A visible trace shows requested tool actions, returned output, and a final message.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The chapter says not to claim the production system uses this loop.
- B: This is the transcript to preserve.
- C: Do not narrate internal deliberation from a visible trace.
- D: Never substitute a fixture for a run that did not happen.
- E: That is enough to ask questions about sequence and evidence.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch04.48

Check each statement that is true about the stop column and outcome evidence in Use It. Each statement is worth 1 point (5 points total).

- [ ] A. For a source summary, the independent outcome evidence is comparison with the specified sources.
- [ ] B. If you do not perform an interface experiment, describe the results you would expect as if observed.
- [ ] C. Only Claude's actions count as stops; your interruptions and approvals do not.
- [ ] D. For each run you record every point where it stopped and who took that stop.
- [ ] E. For a bug fix, the independent outcome evidence is Claude's final done message.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: In a source summary the evidence is comparison with the specified sources; the final done message supplies neither kind of evidence.
- B: The chapter says to mark it not run.
- C: Interruptions, approvals, declines, and acceptance are stops too.
- D: The column records every stop and its owner.
- E: The evidence is the changed file and the tests actually executed.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch04.49

Check each statement that is true about the Ship It artifact. Each statement is worth 1 point (5 points total).

- [ ] A. The conclusion names three layers: the policy supplied an action, the controller stopped under a named rule, and a separate check assessed the answer.
- [ ] B. A failure trace is a reusable test case that a clean happy-path transcript can never be.
- [ ] C. The artifact is an agent trace with turn number, action, observation, stop reason, and the evidence that would justify completion.
- [ ] D. You remove the repeated-action and wrong-answer runs because they make the controller look less impressive.
- [ ] E. You keep only the returned object, since the fixture, record mapping, and budget can be dropped.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Where a layer is absent, say so.
- B: Failures are reusable tests.
- C: This is the artifact's content.
- D: The failure runs explain the boundaries.
- E: The fixture, mapping, budget, and returned object stay together so another reader can reconstruct the path.

**Source:** Ship It: preserve the failure trace

## MA-ch04.50

Check each statement that is true about choosing verbs the evidence earns. Each statement is worth 1 point (5 points total).

- [ ] A. The trace records what was dispatched.
- [ ] B. The controller returned a status.
- [ ] C. The wrong finish shows that the policy and controller layers can occur without the check layer succeeding.
- [ ] D. The verbs returned, records, and found each establish that an answer is correct.
- [ ] E. The comparison found a mismatch with the fixture.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Records is earned by the trace.
- B: Returned is earned by the output.
- C: A wrong finish is exactly that case.
- D: None of these verbs establishes that an answer is correct.
- E: Found is earned by the comparison.

**Source:** Ship It: preserve the failure trace

## MA-ch04.51

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. Claude's fluent draft can stand in for writing it from your record.
- [ ] B. The "Not checked" line is the one an AI-written sign-off omits, because the system has no record of the exits you never exercised.
- [ ] C. The sign-off is a statement you could put your name to.
- [ ] D. The template's "Not checked" line includes non-dictionary actions, blocking or slow tools, and a model-backed policy.
- [ ] E. If your evidence does not support signing, you should sign anyway to complete the artifact.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: You write it from your record.
- B: Only you know which exits you did not exercise.
- C: The sign-off carries your name.
- D: These are listed in the template.
- E: Withholding is an honest result.

**Source:** Ship It: preserve the failure trace

## MA-ch04.52

Check each statement that is true about the navigation-voice analogy. Each statement is worth 1 point (5 points total).

- [ ] A. Claude takes the stop that closes the task.
- [ ] B. The voice can settle whether the two addresses match.
- [ ] C. Claude may request the stop that ends the run, and does so whenever it reports that it is done.
- [ ] D. A navigation voice saying "you have arrived" is a finish action.
- [ ] E. Arrival is at the address you wanted, not the address the system resolved.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Only you take that stop.
- B: The voice cannot tell whether its address is yours.
- C: Reporting done is a finish request.
- D: Both announce arrival without confirming the goal.
- E: The goal is the address you wanted.

**Source:** The driver's seat

## MA-ch04.53

Check each statement that is true about the driver's seat table. Each statement is worth 1 point (5 points total).

- [ ] A. Claude suggests a budget value and unit with reasons, and you choose the number and unit before the run.
- [ ] B. The budget stays with Claude because it works even when the policy cooperates.
- [ ] C. Raising the budget during a run is an acceptable quiet adjustment.
- [ ] D. Claude should decide whether a suspicion of repetition ends the run.
- [ ] E. Claude should write the comparator you specified, run it, and list every mismatch.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Claude advises and you decide.
- B: It stays with you because it is the one way a run ends that does not depend on the policy cooperating.
- C: The budget is raised only by a new written decision.
- D: That decision belongs to you.
- E: This is Claude's part of the checking row.

**Source:** The driver's seat

## MA-ch04.54

Check each statement that is true about checking a finished answer and closing the task. Each statement is worth 1 point (5 points total).

- [ ] A. Claude drafts the trace and the report; you accept, narrow, or withhold, and sign.
- [ ] B. The `finished` status counts as an acceptance of the task.
- [ ] C. An AI checking its own answer is one opinion run twice.
- [ ] D. A comparator you wrote can close a claim that is an equality against a fixture you control.
- [ ] E. You define what the answer is compared against and keep the check independent of the generator.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The closing stop and the signature are yours.
- B: `finished` is not an acceptance.
- C: Same process, same kind of failure.
- D: That is the small task the comparator can close.
- E: Independence is the point of the check.

**Source:** The driver's seat

## MA-ch04.55

Check each statement that is true about showing in your record that the split between Claude's stops and yours happened. Each statement is worth 1 point (5 points total).

- [ ] A. Point to the sign-off line you signed or left unsigned.
- [ ] B. Point to the transcript line where Claude requested the stop or reported done.
- [ ] C. Point to a command you ran afterward that did not come from Claude's report.
- [ ] D. If you cannot point to the transcript line, the command, the edit, or the sign-off line, the split is still on record because it happened in your head.
- [ ] E. Point to an edit Claude made to the budget without your decision.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It shows the closing decision.
- B: It shows Claude's half.
- C: It shows an independent check of your own.
- D: Then the split happened in your head and not in the record.
- E: The chapter asks for your edit to the budget or detector rule.

**Source:** The driver's seat

## MA-ch04.56

Check each statement that is true about the Verify and reflect step. Each statement is worth 1 point (5 points total).

- [ ] A. You use the research script's actual JSON output to compare the observed statuses.
- [ ] B. The configured limit bounds ordinary completed turns in the demonstrated loop.
- [ ] C. A status name is useful only if you can say what event it denotes.
- [ ] D. The configured limit is a general timeout.
- [ ] E. A passing test is enough to explain each return.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The actual output is the evidence.
- B: Unit and assumptions are specified.
- C: A status is only a label until you can name its event.
- D: It is not a timeout, memory cap, credential policy, or correctness check.
- E: Explain each return without relying on a test having passed.

**Source:** Verify and reflect

## MA-ch04.57

Check each statement that is true about inspecting your artifact for invented success. Each statement is worth 1 point (5 points total).

- [ ] A. Correct mistaken statements by deleting the original mistaken interpretation from your learning record.
- [ ] B. Check whether you supplied an answer when the controller returned `incomplete`.
- [ ] C. A trace that looks productive is enough to call a run complete.
- [ ] D. Check whether you summarized budget exhaustion as successful completion because the trace looked productive.
- [ ] E. The configured limit also serves as a memory cap and a credential policy.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The original mistake is preserved.
- B: `incomplete` manufactures no answer.
- C: Budget exhaustion on a productive-looking trace is not completion.
- D: A busy trace is not success.
- E: The limit is none of these.

**Source:** Verify and reflect

## MA-ch04.58

Check each statement that is true about how the chapter wants a reflection to be written. Each statement is worth 1 point (5 points total).

- [ ] A. A reflection that says the finish branch returns before any comparison between red and the recorded blue observation is better than a general slogan, because it ties the lesson to a mechanism.
- [ ] B. You reread your gate and ask which line building the controller changed and whether you dated the revision.
- [ ] C. A reflection should stay general and avoid naming code.
- [ ] D. The reflection should name the actual confusion.
- [ ] E. "I thought stopping meant succeeding" is the best possible reflection.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A mechanism is recognizable when the surrounding system gets larger.
- B: This revisits the gate.
- C: The chapter ties the reflection to specific code.
- D: The actual confusion is what the reflection must name.
- E: The chapter calls it a start, not the best.

**Source:** Verify and reflect

## MA-ch04.59

Check each statement that is true about the chapter's practice assessments. Each statement is worth 1 point (5 points total).

- [ ] A. You use the lesson's existing knowledge check, preserving your initial answers before reading explanations.
- [ ] B. Paid API requests are expected for testing the controller.
- [ ] C. The repetition-detector challenge asks only for a pointless repeated-action case, because useful repetitions are out of scope.
- [ ] D. The three-exits warm-up asks you to write the exit table before running anything and mark every cell you got wrong.
- [ ] E. The Assessments carry no points.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Initial answers are preserved first.
- B: The chapter says not to add paid API requests for behavior that can be isolated offline.
- C: The challenge asks for both a pointless repeat and a useful repetition that challenges the detector.
- D: This is the second warm-up exercise.
- E: They are ungraded practice.

**Source:** Assessments - ungraded practice

## MA-ch04.60

Check each statement that is true about the three jobs at this scale, as summarized in the chapter's closing diagnosis. Each statement is worth 1 point (5 points total).

- [ ] A. Conducting: you let Claude decide whether the task needed a loop.
- [ ] B. Checking: you kept the comparison independent of the generator.
- [ ] C. Conducting: you wrote the exits, the unit of the budget, and the wrong versions before Claude implemented anything.
- [ ] D. Driving: you let Claude take the stop that closes the task.
- [ ] E. Driving: you kept the budget, the price of a false alarm, and the closing of the task.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: You asked first whether the task needed a loop.
- B: Independence is part of checking.
- C: The gate came first.
- D: Closing the task stays with you.
- E: Those three are the driver's decisions.

**Source:** What you can now diagnose

## MA-ch04.61

Check each statement that is true about the boundary a bounded loop can still cross. Each statement is worth 1 point (5 points total).

- [ ] A. A good controller removes the need to compare the resulting state with the task the human authorized.
- [ ] B. Chapter 5 inspects that boundary through network ports.
- [ ] C. A turn budget is itself a permission policy.
- [ ] D. Iteration count and permission are separate controls.
- [ ] E. A budget of one can still allow one wrong target or one unauthorized mutation in a system that exposes such tools.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Neither a good controller nor a good boundary removes that comparison.
- B: Chapter 5 inspects it through filesystem paths.
- C: The budget limits repetition, not authority.
- D: Counting turns says nothing about what each turn may do.
- E: One action is enough to do harm if it is outside the authorized scope.

**Source:** A bounded loop can still cross a boundary once

## MA-ch04.62

Check each statement that is true about what Chapter 5 is previewed to cover. Each statement is worth 1 point (5 points total).

- [ ] A. Its permission policy is written after the first tool runs.
- [ ] B. It will describe a short teaching function as a complete production sandbox.
- [ ] C. A name that looks relative can resolve to a target outside an approved root.
- [ ] D. A permitted read does not imply a permitted write.
- [ ] E. It will use disposable fixtures to test traversal, symlinks, and approval checks.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The permission policy is written before any tool runs.
- B: The chapter refuses to describe a short function as a complete sandbox.
- C: This is the path problem.
- D: Read and write permissions are separate.
- E: These are the chapter's planned tests.

**Source:** A bounded loop can still cross a boundary once

## MA-ch04.63

Check each statement that is true about the chapter's use of Anthropic's Building effective agents. Each statement is worth 1 point (5 points total).

- [ ] A. An API integration has already been executed in this chapter.
- [ ] B. The short loop reproduces Anthropic's runtime.
- [ ] C. The adaptation task asks you to mark where a model-backed decision source would replace the prepared actions.
- [ ] D. The chapter cites it as checked on 2026-09-06.
- [ ] E. The architectural guidance is kept distinct from the scripted iterator.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: No API call is part of the worked example.
- B: The chapter makes no such claim.
- C: Then identify the limits and checks that stay explicit outside it.
- D: The link-check date is given.
- E: The two are not the same thing.

**Source:** Anthropics

## MA-ch04.64

Check each statement that is true about the Computational Skepticism question the chapter borrows. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter borrows the source's census of how often agents fail.
- [ ] B. The companion's agentic-validation chapter shifts the review question from the system's completion report to the outcome its actions produced.
- [ ] C. If you cannot name a condition under which a control would fail, you have validated the control.
- [ ] D. It asks under what condition a robustness result would fail.
- [ ] E. Observing that nothing went wrong this time is validation.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The chapter borrows the question, not the census.
- B: The focus moves to outcomes.
- C: Without a named failure condition you have only observed a pass.
- D: This is the added diagnostic question.
- E: A pass is an observation, not validation.

**Source:** Computational Skepticism

## MA-ch04.65

Check each statement that is true about the conditions under which the chapter's controls would not have held. Each statement is worth 1 point (5 points total).

- [ ] A. The source's framing is a long-term study of many frameworks and models.
- [ ] B. A repeat that your detector's definition does not cover would get past the detector.
- [ ] C. A blocked call that the iteration count cannot interrupt defeats the budget as a time bound.
- [ ] D. The budget stopping the repeated lookup shows it would also hold against a call that never returns.
- [ ] E. A finish that carries a right-looking answer from the wrong key would get past a check that reads the wrong record.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It is an exploratory study of one framework and two models over two weeks.
- B: A detector only stops what its definition covers.
- C: A count cannot cut short a wait that never ends.
- D: A pass on one case does not validate the control for another.
- E: The check must read the record for the key the task names.

**Source:** Computational Skepticism
