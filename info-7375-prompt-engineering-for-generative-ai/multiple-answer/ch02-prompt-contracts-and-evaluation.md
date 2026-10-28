# Chapter 2: Prompt contracts and evaluation

## MA-ch02.1

Check each statement that is true about the color-fixture example that opens the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The program crashed when it received the red response.
- [ ] B. The fixture's one source sentence, identifier s1, is "The color is blue."
- [ ] C. A response saying the fixture says red and citing s1 passes the validator.
- [ ] D. The example is a transcript of Claude making a mistake.
- [ ] E. The failure is hidden in an exotic model behavior.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Nothing crashed; the program returned the result its rules required.
- B: That is the source text.
- C: It is well shaped and cites a known identifier.
- D: It is an executed, constructed counterexample.
- E: It sits between what the validator checks and what a green result is assumed to mean.

**Source:** Opening section (untitled introduction)

## MA-ch02.2

Check each statement that is true about the three constructed responses preserved in the research output. Each statement is worth 1 point (5 points total).

- [ ] A. The third response is properly shaped and cites a known identifier, so it passes even though its claim contradicts the supplied sentence.
- [ ] B. The format-pass rate for the three responses is one-third.
- [ ] C. The second response cites an unknown identifier.
- [ ] D. The first response is not JSON.
- [ ] E. Calling the one-third result an accuracy score would describe the measurement correctly.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Format and content are checked separately.
- B: One of the three is accepted.
- C: The identifier is not in the supplied set.
- D: It is the string "not json".
- E: It would misname the measurement; it is a format rate.

**Source:** Opening section (untitled introduction)

## MA-ch02.3

Check each statement that is true about how the chapter carries Chapter 1's three jobs to a larger boundary. Each statement is worth 1 point (5 points total).

- [ ] A. The drive is deciding what "acceptable" means for this consumer and this claim.
- [ ] B. The check becomes running more prompt variants until the pass rate stops improving.
- [ ] C. A sufficiently detailed schema can hold the decision about what counts as acceptable.
- [ ] D. At the larger boundary, what is accepted or rejected is an index chosen by a sampler.
- [ ] E. The gate becomes a contract plus an evaluation set, written for the program that will consume the answer before you try a single prompt.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: That is the part no schema holds.
- B: The check becomes naming what a pass covers and what it leaves out.
- C: The chapter says no schema holds it.
- D: In Chapter 1 a sampler chose an index; now a contract accepts or rejects a whole answer.
- E: The criterion exists before any output.

**Source:** Opening section (untitled introduction)

## MA-ch02.4

Check each statement that is true about Claude, verification, and independence. Each statement is worth 1 point (5 points total).

- [ ] A. Whether an answer follows from the sentence it cites is a formatting question that the validator can settle.
- [ ] B. The part of the solve-verify argument the chapter keeps is that a trustworthy check fails differently from the thing it checks.
- [ ] C. Asking the generator to vouch for its own answer gives you a second opinion.
- [ ] D. Given a complete contract, Claude can write the validator, enumerate malformed inputs, draft prompt variants, and tabulate pass rates.
- [ ] E. A check run by the system that produced the answer is independent of that system.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: It is a verification question.
- B: That is the claim that survives the caveat.
- C: It is more of the first operation, not a second opinion.
- D: This is the near side of the boundary.
- E: It is not independent of the generator.

**Source:** Opening section (untitled introduction)

## MA-ch02.5

Check each statement that is true about fixtures, access, and observed responses. Each statement is worth 1 point (5 points total).

- [ ] A. When you later compare actual prompts with Claude Code, you should mix the real responses into the fixture file.
- [ ] B. The exercises assume Claude Code access, as established in Chapter 1.
- [ ] C. A locally constructed string becomes misleading only when it is presented as an observed model response.
- [ ] D. The validator and constructed response set run offline in Python's standard library.
- [ ] E. Running the validator and the constructed response set requires direct API credits.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Save real responses separately from the fixtures.
- B: The chapter states this assumption.
- C: As test data it is useful.
- D: They need no direct API credits.
- E: They run offline with no credits.

**Source:** Opening section (untitled introduction)

## MA-ch02.6

Check each statement that is true about the contract you should be able to write before any prompt is tried. Each statement is worth 1 point (5 points total).

- [ ] A. It includes the evidence criterion you will apply.
- [ ] B. It states what the consuming program refuses.
- [ ] C. It is written after the prompt has been tuned, so that it matches the output you observed.
- [ ] D. It includes an evaluation set split into development and held-out cases.
- [ ] E. It states the object the consuming program accepts.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The criterion is fixed up front.
- B: The refusals are part of the contract.
- C: A contract written after tuning just describes the output.
- D: The split is part of the contract.
- E: The object is the first element.

**Source:** What you will be able to do

## MA-ch02.7

Check each statement that is true about why the contract comes before the prompt. Each statement is worth 1 point (5 points total).

- [ ] A. When a specification is incomplete, Claude can be relied on to flag the gap.
- [ ] B. If you write the prompt first and tune until the output looks right, the contract becomes whatever the output happened to look like.
- [ ] C. Claude implements well against a complete specification.
- [ ] D. The prompt should be written first and the contract derived from it.
- [ ] E. After prompt-first tuning, every later pass rate measures agreement with your own habituation.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It may quietly fill the gap with something plausible.
- B: The criterion then follows the output.
- C: Completeness is what makes it work.
- D: The prompt is derived from the contract.
- E: The criterion drifted to match the output.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.8

Check each statement that is true about the consumer's needs in the teaching contract. Each statement is worth 1 point (5 points total).

- [ ] A. A response containing answer, sources, and confidence fails the validator even if all three values look reasonable.
- [ ] B. The consumer needs a nonblank answer.
- [ ] C. The consumer accepts a response whose sources list is empty, if the answer is nonblank.
- [ ] D. The contract accepts the two required keys plus arbitrary extra keys.
- [ ] E. The consumer needs the source identifiers to belong to a supplied set.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Extra keys are rejected.
- B: One of the stated needs.
- C: It needs at least one source identifier.
- D: It accepts exactly two keys.
- E: One of the stated needs.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.9

Check each statement that is true about the exact-keys rule. Each statement is worth 1 point (5 points total).

- [ ] A. A consumer that assumes a fixed shape finds the rule protective, because unexpected additions become visible instead of silently ignored.
- [ ] B. You should choose the contract for your consumer, not because a short teaching function happened to choose one.
- [ ] C. Whether to allow extra keys is a trade-off between strict predictability and accepting some useful objects.
- [ ] D. The rule is plainly correct no matter what the downstream job is.
- [ ] E. An exploratory analysis that wants extensible metadata may find the same rule an obstacle.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Visibility is the benefit.
- B: The consumer decides.
- C: The chapter frames the choice as that trade-off.
- D: You cannot call it good or bad without naming the downstream job.
- E: The same rule can be a cost.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.10

Check each statement that is true about requests versus checks. Each statement is worth 1 point (5 points total).

- [ ] A. Adding "always obey the schema" to a prompt is equivalent to checking the schema after the response arrives.
- [ ] B. The chapter's contrast between requests and checks is unrelated to Chapter 1's point about the system prompt.
- [ ] C. The prompt requests behavior from the producer, while the validator checks the returned object against executable conditions.
- [ ] D. A request can be ignored or misunderstood, whereas the local check has a definite acceptance rule.
- [ ] E. A prompt that asks for a schema guarantees that the returned object satisfies it.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The two are not equivalent.
- B: It is the same point one level up.
- C: Request versus check.
- D: Only the check is definite.
- E: A request can be ignored or misunderstood.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.11

Consider the constructed response {"answer":"The sources do not say.","sources":["s1"]}. Check each statement that is true about it. Each statement is worth 1 point (5 points total).

- [ ] A. The reference contract includes a field for insufficient evidence.
- [ ] B. Adding a status field to the object would solve the problem within the current validator.
- [ ] C. The reference validator accepts it.
- [ ] D. Writing "be accurate" in the prompt supplies a refusal state.
- [ ] E. The validator accepts it because it recognizes the answer as an honest refusal.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It has no such field.
- B: The validator rejects the extra key.
- C: It is a nonblank answer with a known source.
- D: It does not supply one.
- E: It cannot tell a refusal from an assertion.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.12

Check each statement that is true about what happens when a finding reopens an earlier design decision. Each statement is worth 1 point (5 points total).

- [ ] A. Whether a refusal is an acceptable answer is a decision about the interface.
- [ ] B. A held-out case that guided the redesign stays held-out.
- [ ] C. The record should include a new contract version and new tests.
- [ ] D. If you redesign the contract, you should record the redesign and test it as a different version.
- [ ] E. A finding like the refusal limit can reopen an earlier decision without making the design waterfall.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The chapter frames it as an interface decision.
- B: Any case that guided the redesign counts as development evidence from then on.
- C: Both are named in the chapter.
- D: A new version needs its own tests.
- E: The chapter says none of this makes the design waterfall.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.13

Check each statement that is true about the evaluation set in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. The held-out list is not shown to Claude and is not used to revise the prompt until the revision is frozen.
- [ ] B. The gate specifies five development questions and five held-out questions.
- [ ] C. The held-out list may be listed and dated after the responses are inspected, since it is sealed anyway.
- [ ] D. The held-out list may be shown to Claude while drafting, as long as the final prompt is unchanged.
- [ ] E. The evaluation set is what defines what "supported" means for each question.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The list is sealed.
- B: The sizes are stated in the gate.
- C: Both lists are dated before any response is inspected.
- D: It is sealed until the revision is frozen.
- E: The evidence criterion does that.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.14

Check each statement that is true about the evidence criterion in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. For each question, the criterion gives one sentence saying what "supported" means for it.
- [ ] B. Computational Skepticism for AI suggests recording pass or fail, with unknown folded into fail.
- [ ] C. Supported and contradicted are the only two outcomes the criterion needs.
- [ ] D. "Cannot be reviewed" is recorded as a third outcome beside supported and contradicted.
- [ ] E. The criterion is best written after you know which prompt wins, so that it reflects the winning prompt's strengths.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: That is the criterion's content.
- B: It records pass, fail, or unknown against a criterion fixed before you read the output.
- C: A third outcome is recorded.
- D: Three outcomes are recorded.
- E: Write it before you know which prompt wins.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.15

Check each statement that is true about the wrong versions the gate says your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. A validator that accepts a source list when any entry is known, where the contract says every entry, is a wrong version your tests must catch.
- [ ] B. The well-formed but wrong color-fixture response is one that your validator tests will catch.
- [ ] C. A validator that checks only that the keys exist is one of the wrong versions the gate says your tests must catch.
- [ ] D. The color-fixture response must be caught by your evidence column, not by a validator test.
- [ ] E. A validator that skips the nonblank check is a wrong version your tests must catch.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: One of the three named.
- B: No validator test will catch it; your evidence column must.
- C: One of the three named.
- D: It is well formed and wrong.
- E: One of the three named.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.16

Check each statement that is true about failure sentences, the pass condition, and what the experiment may claim. Each statement is worth 1 point (5 points total).

- [ ] A. If you cannot write the failure sentence for a held-out question, you may proceed because the validator will catch the problem.
- [ ] B. The gate is finished when the validator accepts or rejects each of the three fixture responses as predicted.
- [ ] C. For each held-out question, the gate asks for one sentence describing an answer that would pass the validator and fail the evidence criterion.
- [ ] D. The experiment may claim that any answer the validator accepted is correct.
- [ ] E. Writing the failure sentence after seeing the responses is equivalent, since it still describes a failure.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Then you do not yet know what you are checking for.
- B: It needs a named test for every contract line that fails if the line is deleted.
- C: That is the failure sentence.
- D: It cannot say any answer is correct beyond the reviewed claims.
- E: Afterward you have described the output, not tested your understanding.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.17

Check each statement that is true about the order of checks in validate(). Each statement is worth 1 point (5 points total).

- [ ] A. A successfully parsed value is automatically the kind of value the contract wants.
- [ ] B. After parsing, the field values are checked first and the exact key set last.
- [ ] C. For "not json", the key-set check runs and fails.
- [ ] D. json.loads runs first and can fail before any field rule is relevant.
- [ ] E. The string "not json" is rejected at the parsing step.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The dictionary check comes next for that reason.
- B: The order is dictionary check, exact key set, then field values.
- C: None of the dictionary-field checks runs.
- D: Parsing is first.
- E: The exception path returns False.

**Source:** What each line of the validator promises

## MA-ch02.18

Check each statement that is true about the answer and sources checks. Each statement is worth 1 point (5 points total).

- [ ] A. A whitespace-only answer passes the nonblank check because it is still a string.
- [ ] B. The sources field may be a bare string such as "s1" instead of a list.
- [ ] C. The answer field may hold any JSON value, provided the key set is exactly right.
- [ ] D. The integer 1 fails as an answer even though a human could display it as text.
- [ ] E. A sources list may contain a non-string entry as long as at least one entry is a known identifier.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: strip() removes surrounding whitespace, so it fails.
- B: It must be a list.
- C: The answer must be a string.
- D: The function does not coerce.
- E: Every entry must be a string in the allowed set.

**Source:** What each line of the validator promises

## MA-ch02.19

Check each statement that is true about how validate() treats the sources list. Each statement is worth 1 point (5 points total).

- [ ] A. The expression computes the fraction of acceptable references and accepts when most are known.
- [ ] B. One valid identifier cannot compensate for another invalid entry.
- [ ] C. Every entry in sources must be a string.
- [ ] D. With allowed identifiers {"s1"}, a sources list of ["s1", "missing"] is rejected.
- [ ] E. The nonempty requirement is a condition separate from the requirement that every entry belongs to the allowed set.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It does not compute a fraction.
- B: The word "every" matters.
- C: The check includes isinstance for each entry.
- D: One invalid entry sinks the list.
- E: Deleting the nonempty check is a separate edit.

**Source:** What each line of the validator promises

## MA-ch02.20

Check each statement that is true about the Boolean return value of validate(). Each statement is worth 1 point (5 points total).

- [ ] A. A Boolean is convenient for a pass rate and easy to test.
- [ ] B. The reference collapses every rejection into False.
- [ ] C. A Boolean tells a reviewer how to repair a response.
- [ ] D. A richer result naming the parse failure, key mismatch, wrong type, or unknown source is behavior the reference already has.
- [ ] E. The absence of a message is not the absence of a reason.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: That is the upside.
- B: This is an intentional simplification.
- C: It tells the reviewer nothing about repair.
- D: It is an extension to your own version.
- E: For each failing fixture you stop at the first relevant boundary and name it.

**Source:** What each line of the validator promises

## MA-ch02.21

Check each statement that is true about the six lesson tests. Each statement is worth 1 point (5 points total).

- [ ] A. The six lesson tests include a test of the empty-experiment rule in the rate function.
- [ ] B. They exercise a valid object, invalid JSON, a wrong-typed answer, an unknown source, an extra key, and the empty-experiment rule.
- [ ] C. You are asked to predict the result before editing a scratch copy and rerunning the tests.
- [ ] D. "The tests pass" means every promised behavior of the function is defended.
- [ ] E. Each test is evidence for one behavior, not for the function as a whole.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The sixth test covers it.
- B: That is the stated list.
- C: Predict, then check.
- D: Tests pass for the behaviors they exercise.
- E: The chapter says so.

**Source:** What each line of the validator promises

## MA-ch02.22

Check each statement that is true about the three behaviors the chapter says the six lesson tests never defend. Each statement is worth 1 point (5 points total).

- [ ] A. Changing all to any leaves all six tests passing.
- [ ] B. Deleting the nonempty-source check leaves all six tests passing.
- [ ] C. The extra-key rule is one of the three behaviors the lesson's tests never defend.
- [ ] D. Deleting the nonblank check leaves all six tests passing.
- [ ] E. The rejection of invalid JSON is one of the three behaviors the lesson's tests never defend.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The every-entry rule is undefended.
- B: The nonempty rule is undefended.
- C: One of the six tests exercises an extra key.
- D: The nonblank rule is undefended.
- E: One of the six tests exercises invalid JSON.

**Source:** What each line of the validator promises

## MA-ch02.23

Check each statement that is true about what validate() receives and can decide. Each statement is worth 1 point (5 points total).

- [ ] A. The validator receives the allowed identifier set, not the source sentence.
- [ ] B. If someone says validate() verifies source support, you can point them to the final all(...) condition as the comparison of source content with answer content.
- [ ] C. One of the compact lines of validate() compares the source content with the answer content.
- [ ] D. The validator can decide whether the words attached to s1 support the answer.
- [ ] E. The validator can reject an invented address such as missing.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It gets {"s1"}, not the text.
- B: That condition checks identifier membership, not content.
- C: The source_ids argument supplies identifiers, not passages.
- D: It cannot, since it lacks the words.
- E: Membership is checkable.

**Source:** A source identifier is an address, not an argument

## MA-ch02.24

Check each statement that is true about membership and support. Each statement is worth 1 point (5 points total).

- [ ] A. A known citation entails support for the claim attached to it.
- [ ] B. Membership in a registry and support for a proposition are different relations.
- [ ] C. An address is useless once the accompanying summary misstates its source.
- [ ] D. Passing the source-existence question also answers the support question.
- [ ] E. An address can point to a real document while the accompanying summary misstates it.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Figure 2.1's point is that it does not.
- B: The chapter says so.
- C: It still gives the reviewer somewhere to look.
- D: It makes the support question possible; it does not answer it.
- E: The address stays useful as somewhere to look.

**Source:** A source identifier is an address, not an argument

## MA-ch02.25

Check each statement that is true about the accepted red response {"answer":"The fixture says red","sources":["s1"]}. Each statement is worth 1 point (5 points total).

- [ ] A. The red response's acceptance exposes an exotic model behavior.
- [ ] B. To explain why the red response passes, we have to speculate about model internals.
- [ ] C. The red response satisfies every implemented condition.
- [ ] D. The red response's acceptance shows that the validator is broken.
- [ ] E. The fact that the source sentence says blue enters the calculation.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The chapter says the failure is not hidden in an exotic model behavior.
- B: We can trace it to the missing check.
- C: Keys, answer, sources, and membership all pass.
- D: The validator enforces its stated contract.
- E: It does not enter the calculation.

**Source:** A source identifier is an address, not an argument

## MA-ch02.26

Check each statement that is true about who answers the support question. Each statement is worth 1 point (5 points total).

- [ ] A. Asking for a brief explanation with cited evidence makes an answer easier to inspect.
- [ ] B. You should request hidden chain-of-thought so you can read the model's real reasoning.
- [ ] C. An articulate rationale is access to an authenticated internal process.
- [ ] D. If the generator is also the only reviewer of its support, you have the first opinion run twice.
- [ ] E. Claude can be asked to set the claim and the source sentence side by side.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The explanation is still output to evaluate.
- B: The chapter says not to request it.
- C: Do not treat it as one.
- D: That is not independent review.
- E: For this small case you can verify the comparison at a glance.

**Source:** A source identifier is an address, not an argument

## MA-ch02.27

Check each statement that is true about how the three responses are decided by validate(). Each statement is worth 1 point (5 points total).

- [ ] A. For the second response, parsing and shape checks succeed, but missing is not in the supplied identifier set.
- [ ] B. For "not json", parsing fails and the exception path returns False.
- [ ] C. The observed acceptance sequence in the saved execution is false, true, false.
- [ ] D. For the third response, all implemented checks succeed and the result is True.
- [ ] E. For "not json", none of the dictionary-field checks runs.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: It returns False at membership.
- B: The first response.
- C: It is false, false, true.
- D: The color fixture.
- E: Parsing failed first.

**Source:** Work through the three-response experiment

## MA-ch02.28

Check each statement that is true about the pass_rate function and its result for the fixture. Each statement is worth 1 point (5 points total).

- [ ] A. The function knows how the responses were selected.
- [ ] B. Each accepted response contributes one and each rejected response contributes zero.
- [ ] C. The numerator is 2, because two of the three responses parse as JSON.
- [ ] D. The denominator is the number of supplied responses.
- [ ] E. The result is 1/3, saved in the JSON as 0.3333333333333333.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It does not.
- B: It sums the Boolean decisions.
- C: Only one response is accepted.
- D: It divides by len(responses).
- E: One acceptance among three.

**Source:** Work through the three-response experiment

## MA-ch02.29

Check each statement that is true about what the one-third result describes. Each statement is worth 1 point (5 points total).

- [ ] A. The result describes the share of the answers that are factually correct.
- [ ] B. The three cases are a random sample of Claude's production behavior.
- [ ] C. The three cases were constructed to expose three boundaries.
- [ ] D. The one-third result estimates how often a real service will make these mistakes.
- [ ] E. A model was called to generate the three cases.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It is a format rate, not accuracy.
- B: They are not a random sample.
- C: They are test cases.
- D: It estimates nothing about a real service.
- E: They are constructed strings; no model was called.

**Source:** Work through the three-response experiment

## MA-ch02.30

Check each statement that is true about pass_rate on an empty list of responses. Each statement is worth 1 point (5 points total).

- [ ] A. Returning zero could be mistaken for a tested system that failed every case.
- [ ] B. The error is a bug the chapter recommends replacing with a return value of zero.
- [ ] C. The reference refuses to assign a pass rate to an experiment with no denominator.
- [ ] D. The function raises an error.
- [ ] E. Returning one could be mistaken for perfect performance.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Zero looks like a result.
- B: The refusal is a design choice.
- C: There is nothing to divide by.
- D: It raises ValueError.
- E: One looks like a result.

**Source:** Work through the three-response experiment

## MA-ch02.31

Check each statement that is true about the chapter's table comparing validate() with the support review. Each statement is worth 1 point (5 points total).

- [ ] A. For the missing-identifier response, the support review is "cannot be reviewed" because the cited address resolves to nothing.
- [ ] B. A validate() result of True beside a review result of contradicted is the expected report for the third row.
- [ ] C. For the red response, the support review is "contradicted" by s1, "The color is blue."
- [ ] D. The missing-identifier response fails at parsing.
- [ ] E. For "not json", the support review is "cannot be reviewed" because there is no claim to compare.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: No source to read.
- B: It is not an inconsistent report.
- C: The source says blue.
- D: It parses and is shaped correctly; it fails source membership.
- E: No claim to review.

**Source:** Work through the three-response experiment

## MA-ch02.32

Check each statement that is true about the fluency trap and the cost of checking. Each statement is worth 1 point (5 points total).

- [ ] A. The fluency trap is that the more fluently an output presents, the more confident you become in it and then in your own evaluation of it.
- [ ] B. Form and content are linked, so a more fluent output is more likely to be correct.
- [ ] C. If verification is not budgeted, it still happens informally.
- [ ] D. Form and content are independent.
- [ ] E. The support review is the cheap check and the validator is the expensive one.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The chapter's definition.
- B: They are independent.
- C: If it is not budgeted it does not happen.
- D: Fluent form says little about content.
- E: The validator is the cheap check.

**Source:** Work through the three-response experiment

## MA-ch02.33

Check each statement that is true about the classroom comparison of a baseline prompt and a revision. Each statement is worth 1 point (5 points total).

- [ ] A. Ten questions establish broad reliability.
- [ ] B. Five additional questions are held out.
- [ ] C. Without a fixed evaluation set, "better" is a feeling.
- [ ] D. The lesson compares a baseline prompt and a few-shot revision on five development questions.
- [ ] E. A fixed evaluation set is what makes an improvement measurable.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: They define a manageable classroom experiment only.
- B: The held-out set is reserved.
- C: The chapter says so.
- D: Five dev questions.
- E: The chapter says so.

**Source:** A prompt revision is a hypothesis

## MA-ch02.34

Check each statement that is true about treating a revision as a hypothesis. Each statement is worth 1 point (5 points total).

- [ ] A. Hypothesizing that examples will help the output shape is a testable proposal.
- [ ] B. A controlled comparison requires pretending the rest of the world is fixed.
- [ ] C. You should predict a specific failure that the revision might address.
- [ ] D. Adding examples counts as an improvement because it sounds like established practice.
- [ ] E. If you change examples, task, source material, persona, and questions at once, any observed difference becomes hard to attribute.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: It is a proposal, not a result.
- B: It requires recording what you changed and limiting the explanation.
- C: State the target failure first.
- D: That is a proposal, not a result.
- E: Change something you can describe.

**Source:** A prompt revision is a hypothesis

## MA-ch02.35

Check each statement that is true about development and held-out questions. Each statement is worth 1 point (5 points total).

- [ ] A. If you need another untouched check, you can relabel the old held-out set as independent.
- [ ] B. A held-out case that guided a choice is a moral failing that voids the experiment.
- [ ] C. Showing only the final success is enough, since development failures can be discarded.
- [ ] D. Once a held-out case has guided a choice, it is development evidence.
- [ ] E. Development questions are available while you revise.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Design a new evaluation instead.
- B: It is bookkeeping.
- C: Preserve the failures too.
- D: Its role has changed.
- E: They guide revision.

**Source:** A prompt revision is a hypothesis

## MA-ch02.36

Check each statement that is true about personas. Each statement is worth 1 point (5 points total).

- [ ] A. A persona is a hypothesis to test.
- [ ] B. "You are an expert" changes none of the validator's checks.
- [ ] C. If a persona helps on your cases, the role label can certify the answer before the evidence review.
- [ ] D. If a persona helps on your cases, you should describe the observed difference and the conditions.
- [ ] E. "You are an expert" adds a supporting passage to the source collection.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It is not a certificate of support.
- B: The checks are fixed.
- C: Describe the observed difference and its conditions instead.
- D: Describe the difference; do not let the label certify the answer.
- E: It adds none.

**Source:** A prompt revision is a hypothesis

## MA-ch02.37

Check each statement that is true about running the experiment with Claude Code. Each statement is worth 1 point (5 points total).

- [ ] A. If you have not run the comparison, your artifact should say proposed experiment.
- [ ] B. Keep the proposed prompt, the actual returned text, the executable acceptance result, and your evidence judgment visibly separate.
- [ ] C. Claude Code can organize the experiment, run your local validator, draft candidate prompts, and challenge your interpretation.
- [ ] D. The actual returned text can be folded into the proposed prompt in the record.
- [ ] E. A complete-looking results table with invented outputs is better than an incomplete plan.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Honest labeling.
- B: Four things.
- C: Its stated role.
- D: They are kept separate.
- E: It is worse than an honest plan.

**Source:** A prompt revision is a hypothesis

## MA-ch02.38

A report says only "The revised prompt achieved a higher pass rate." Check each statement that is true about what the chapter says is missing. Each statement is worth 1 point (5 points total).

- [ ] A. A reader needs to know which validator produced the higher pass rate.
- [ ] B. Nothing material is missing, because a higher pass rate speaks for itself.
- [ ] C. A reader needs to know whether the accepted responses remained supported.
- [ ] D. A reader needs to know which cases were used and how many responses there were.
- [ ] E. A reader needs to know whether the cases were used during revision.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Which validator is the first question.
- B: Without those details the number is hard to use.
- C: Format acceptance is not support.
- D: Both are unstated.
- E: A held-out role may have changed.

**Source:** What a pass rate leaves out

## MA-ch02.39

Check each statement that is true about what the pass rate compresses or ignores. Each statement is worth 1 point (5 points total).

- [ ] A. A format pass establishes that the answer is complete.
- [ ] B. A non-JSON response and a response with one unknown source identifier both contribute zero.
- [ ] C. Equal weighting is a discovered statement that every case has equal importance.
- [ ] D. The reference weights each question by how consequential its claim is.
- [ ] E. A non-JSON response and a response with one unknown source identifier require different repairs even though they contribute equally to the pass rate.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A nonblank answer can be short, irrelevant, or evasive.
- B: Different failures, same total.
- C: It is simple and transparent only.
- D: It weights every response equally.
- E: One needs valid JSON, the other a known identifier.

**Source:** What a pass rate leaves out

## MA-ch02.40

Check each statement that is true about the chapter's practical test for a reported number. Each statement is worth 1 point (5 points total).

- [ ] A. A statistic with a narrow scope has no mechanical meaning.
- [ ] B. The chapter's strongest demonstration is a high pass rate on held-out cases.
- [ ] C. The test is whether a reader could reconstruct how the number was produced.
- [ ] D. A number that a reader cannot reconstruct still carries mechanical meaning as long as it is high.
- [ ] E. The chapter concludes that the format check should be abandoned.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: If a reader can reconstruct it, it has mechanical meaning even if narrow.
- B: It is a correctly interpreted mixed result, not a spectacular success rate.
- C: Reconstructability.
- D: It may be functioning as decoration.
- E: It says to name the check accurately and pair it with review.

**Source:** What a pass rate leaves out

## MA-ch02.41

Check each statement that is true about building your first validator. Each statement is worth 1 point (5 points total).

- [ ] A. Decide how failure will be represented only after Claude has written its version.
- [ ] B. Your own version is the record of what you understood before Claude touched anything.
- [ ] C. Begin with a framework or another model call.
- [ ] D. Write it from the stated contract, not from the reference.
- [ ] E. The standard-library version is short enough for you to explain completely, and that explanation is the capability being built.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Decide it before you implement the checks.
- B: It is also the instrument for measuring Claude's version.
- C: Do not begin with either.
- D: Build before reference.
- E: The explanation is the point.

**Source:** Build It: your validator is the baseline

## MA-ch02.42

Check each statement that is true about extending the six lesson tests. Each statement is worth 1 point (5 points total).

- [ ] A. Add tests that defend the lines the six tests leave open.
- [ ] B. Prove a test works by running it against a scratch copy with that line removed.
- [ ] C. For each added test, state the defect it exposes and one different defect that could still survive it.
- [ ] D. Predict each lesson test's result only after you have read the reference.
- [ ] E. A larger test count means better coverage.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The gaps are the target.
- B: It must fail there.
- C: No test catches everything.
- D: Read the six tests before the reference and predict each result.
- E: A larger test count is not coverage.

**Source:** Build It: your validator is the baseline

## MA-ch02.43

Check each statement that is true about the valid-but-unsupported response in the Build It section. Each statement is worth 1 point (5 points total).

- [ ] A. You should deliberately construct the valid-but-unsupported response.
- [ ] B. If you extend the interface with a status field, keep it as a separate version and test the extension.
- [ ] C. After modifying the reference, you may cite its old tests as validating the new behavior.
- [ ] D. If your implementation rejects it, inspect why: perhaps you added a semantic rule, or its structure does not match the contract.
- [ ] E. The goal is to distinguish an added check from a mistaken explanation of the existing one.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: It tests your understanding of the limits.
- B: Document benefit and migration cost.
- C: The old tests do not validate it.
- D: Find the reason.
- E: It is not to force every learner implementation to share the reference's limits.

**Source:** Build It: your validator is the baseline

## MA-ch02.44

Check each statement that is true about handing Claude Code your gate and checking what comes back. Each statement is worth 1 point (5 points total).

- [ ] A. A failing test is often a gap in your gate, because Claude had only what you wrote.
- [ ] B. If a wrong validator survives your tests, your tests are enough.
- [ ] C. You give Claude the gate, meaning the contract, the test list, and the fixtures, and not your validator.
- [ ] D. Claude's report that all tests pass settles whether your tests are enough.
- [ ] E. If all your tests pass on Claude's validator, there is no need to compare it with your baseline.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The gap is yours to fix.
- B: A surviving wrong version is a hole in your gate.
- C: Your validator stays back as the baseline.
- D: The system under test cannot judge that.
- E: You should name one difference in behavior.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch02.45

Check each statement that is true about running the experiment and its follow-up in Use It. Each statement is worth 1 point (5 points total).

- [ ] A. You ask for a short explanation and cited evidence, not hidden chain-of-thought.
- [ ] B. If a session failed or did not run, you may substitute a fixture transcript for it.
- [ ] C. You give Claude the baseline prompt and the few-shot revision on the same five development questions.
- [ ] D. You reveal the held-out questions only when your revision is frozen, and record that you did.
- [ ] E. Claude's agreement with your written explanation is a second source for the sentence in the fixture.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Evidence you can check.
- B: Record that it failed; do not substitute a fixture.
- C: Same questions for both.
- D: The seal is kept.
- E: Its agreement is not a second source.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch02.46

Check each statement that is true about preserving responses in the artifact. Each statement is worth 1 point (5 points total).

- [ ] A. If surrounding prose makes the strict contract fail, remove the prose and score the repaired string as though it arrived that way.
- [ ] B. If Claude helped with a repair, record that as a transformation, not as part of the original run.
- [ ] C. Preserve each response before editing or repairing it.
- [ ] D. A reply introduced by a sentence fails json.loads.
- [ ] E. Record the original and the repaired version with their roles separated.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: That misrepresents the observation.
- B: Attribute honestly.
- C: Keep the original.
- D: Surrounding prose breaks parsing.
- E: Two records.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.47

Check each statement that is true about the artifact and its change log. Each statement is worth 1 point (5 points total).

- [ ] A. The artifact contains baseline and revised prompts, development and held-out cases, raw responses, validation results, and a change log.
- [ ] B. Its purpose is to let another reader reconstruct both the mechanics and your decisions.
- [ ] C. "Improved prompt" is an adequate change log entry.
- [ ] D. You keep the baseline intact and name the change in the next version.
- [ ] E. A revision that did not help is an uninformative result.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The stated list.
- B: Auditability.
- C: Name which instruction, example, or boundary changed.
- D: Version discipline.
- E: It is still informative when the trail is intact.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.48

Check each statement that is true about the integrated evidence review. Each statement is worth 1 point (5 points total).

- [ ] A. In your task, a passage may support only part of an answer.
- [ ] B. You take one accepted answer and compare each meaningful claim with the supplied source material.
- [ ] C. A limited conclusion might be that a revision changed format acceptance on the recorded cases while leaving a source-support failure unresolved.
- [ ] D. One correct citation can stand in for a claim-by-claim explanation.
- [ ] E. You mark unsupported content separately from formatting status.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Partial support occurs.
- B: Claim by claim.
- C: It tells the next person what to reuse and what is risky.
- D: It must not stand in.
- E: Two separate columns.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.49

Check each statement that is true about the sign-off template. Each statement is worth 1 point (5 points total).

- [ ] A. The Not claiming field lists the things you do claim, such as that the format pass rate measures accuracy.
- [ ] B. It has fields for Checked, How, Not checked, Not claiming, and Signed or withheld.
- [ ] C. If the support review is unfinished, you write pending.
- [ ] D. Withholding your name is a failed result.
- [ ] E. The Not checked field can list held-out cases you tuned against.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It lists what you are not claiming.
- B: Those are the five fields.
- C: A missing review must not be hidden.
- D: The chapter calls withholding an honest result.
- E: Tuned-against cases are not independent.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.50

Check each statement that is true about the judgments in this chapter that no schema field can hold. Each statement is worth 1 point (5 points total).

- [ ] A. Whether the consumer tolerates extra keys is a judgment no schema field can hold.
- [ ] B. The validator can make these judgments if it is given a stricter schema.
- [ ] C. Whether "the sources do not say" is an acceptable answer is a judgment no schema field can hold.
- [ ] D. Whether equal weighting is right when one question carries the stakes is a judgment no schema field can hold.
- [ ] E. Claude has the consumer, the stakes, and the person who bears the cost of a wrong accept in the files it reads.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The validator can enforce it but not make it.
- B: It can only enforce a decision once made.
- C: An interface decision.
- D: A policy judgment.
- E: None of that is in the files unless you put it there.

**Source:** The driver's seat: what counts as acceptable

## MA-ch02.51

Check each statement that is true about the division of labor in the chapter's table. Each statement is worth 1 point (5 points total).

- [ ] A. For saying what the pass rate supports, Claude chooses the verb and signs.
- [ ] B. Claude should challenge the contract by finding an input it admits that the consumer cannot handle.
- [ ] C. Claude should decide what the consumer needs and what acceptable means.
- [ ] D. To judge whether an answer is supported, Claude makes the call and you accept its verdict.
- [ ] E. Claude should choose the one feature that changes, and the lists can be fixed after you look.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: You choose the verb and sign or withhold.
- B: You decide first and record who decided each line.
- C: That line belongs to you.
- D: You make the call, claim by claim, against the source.
- E: You choose the feature and fix the lists before looking.

**Source:** The driver's seat: what counts as acceptable

## MA-ch02.52

Check each statement that is true about why these tasks stay with you. Each statement is worth 1 point (5 points total).

- [ ] A. A check run by the generator is an independent second opinion.
- [ ] B. "Supported" is Claude's definition to supply.
- [ ] C. If you cannot point to a transcript line or an edit showing a delegated task and a retained judgment, the record is still sufficient.
- [ ] D. The development/held-out split is a promise about what you will not look at, and only you can keep it.
- [ ] E. The consumer, the stakes, and who bears a wrong accept are outside the files Claude sees.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It is the first opinion run twice.
- B: It is your definition.
- C: The split then happened in your head, not in the record.
- D: A promise, not a setting.
- E: Hence the first row is yours.

**Source:** The driver's seat: what counts as acceptable

## MA-ch02.53

Check each statement that is true about the verify-and-reflect work. Each statement is worth 1 point (5 points total).

- [ ] A. A report can be incomplete and honest.
- [ ] B. You should ask which strings you constructed and which came from an actual Claude interaction.
- [ ] C. Your own execution should be labeled as your run, with its own environment record.
- [ ] D. If the same function calculates every rate, provenance does not change what you can conclude.
- [ ] E. Rerun the constructed three-response experiment and explain why its one-third result is a format rate.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It becomes misleading when a missing review is replaced with an automated pass.
- B: Provenance changes what you can conclude.
- C: The research script and saved output are the reference evidence for the published example.
- D: The chapter says these distinctions change what you can conclude.
- E: The rate is not accuracy.

**Source:** Verify and reflect

## MA-ch02.54

Check each statement that is true about the Challenge-level assessment that asks you to design an insufficiency state. Each statement is worth 1 point (5 points total).

- [ ] A. You explain who decides whether a refusal counts as an acceptable answer.
- [ ] B. You compare the simplicity you lose with the ambiguity you remove.
- [ ] C. You propose, in a separate learner version, an explicit way to represent insufficient source evidence.
- [ ] D. You explain how the change affects the exact-key and nonempty-source rules.
- [ ] E. You may claim the reference already supports your new interface.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: A consumer or interface decision.
- B: The trade-off.
- C: A separate version.
- D: The old rules interact with the new state.
- E: You must not claim it.

**Source:** Assessments - ungraded practice

## MA-ch02.55

Check each statement that is true about the assessment that builds a legitimate address with an illegitimate claim. Each statement is worth 1 point (5 points total).

- [ ] A. You merge the two results into one score.
- [ ] B. You construct a short source and an answer that cites its valid identifier while contradicting its content.
- [ ] C. You may present the example as something Claude actually said.
- [ ] D. You explain why the two results differ.
- [ ] E. You preserve the executable decision and a separate evidence judgment using supported, contradicted, and cannot be reviewed.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Keep them separate.
- B: A color-fixture analogue.
- C: Keep it explicitly constructed.
- D: Membership versus support.
- E: Two columns.

**Source:** Assessments - ungraded practice

## MA-ch02.56

Check each statement that is true about the assessment on repairing a failing response. Each statement is worth 1 point (5 points total).

- [ ] A. You attribute the repaired text to the original run.
- [ ] B. If Claude helped repair the response, you record that as a transformation.
- [ ] C. You run the validator on each version and describe precisely what changed.
- [ ] D. Scoring only the corrected version answers the same question as scoring the original.
- [ ] E. You make a corrected version of a failing fixture or recorded response and keep both versions.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That would misattribute it.
- B: Not as the original run.
- C: A before-and-after record.
- D: It answers a different question.
- E: Both are evidence.

**Source:** Assessments - ungraded practice

## MA-ch02.57

Check each statement that is true about the assessment on tuning against supposedly held-out cases, and about the Assessments generally. Each statement is worth 1 point (5 points total).

- [ ] A. You describe a hypothetical revision process in which a developer repeatedly tunes against the supposedly held-out cases.
- [ ] B. You propose a revised record and evaluation plan that acknowledges what was inspected.
- [ ] C. You solve the problem by simply renaming the same final score independent evidence.
- [ ] D. You identify the point at which the held-out label becomes misleading.
- [ ] E. No paid API experiment is required to practice the contract mechanics in these Assessments.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A scenario exercise.
- B: Honest bookkeeping.
- C: The chapter says not to.
- D: Once the cases guide choices.
- E: The chapter says so.

**Source:** Assessments - ungraded practice

## MA-ch02.58

Check each statement that is true about the assessment on meaning-preserving changes. Each statement is worth 1 point (5 points total).

- [ ] A. If you run the prompts, you compare format, claim content, and support separately.
- [ ] B. If you only design the test, you may label it a completed experiment.
- [ ] C. You prepare three paraphrases of one task while keeping its intended facts and obligations fixed.
- [ ] D. You predict what should remain invariant and what may legitimately vary, and say who decided where that line falls.
- [ ] E. Different wording in an answer is automatically a failure of the intended task.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Three columns.
- B: Label it as a design.
- C: Same task, different wording.
- D: The line is a decision.
- E: It is not automatically a failure.

**Source:** Assessments - ungraded practice

## MA-ch02.59

Check each statement that is true about what you can now inspect in the validator. Each statement is worth 1 point (5 points total).

- [ ] A. The right response to the color fixture is to dismiss automated checks.
- [ ] B. Parsing, object shape, exact keys, answer type, nonblank content, source-list type, nonempty membership, and allowed identifiers are separate obligations.
- [ ] C. You can explain a rejected response by locating the failed condition.
- [ ] D. You can say which of those obligations the lesson's tests defend and which they leave open.
- [ ] E. The right response to the color fixture is to accept automated checks without question.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Keep the structural check, name its scope, and add the evidence review.
- B: Each has its own job.
- C: Not a general impression of quality.
- D: The gap analysis.
- E: Neither blind acceptance nor dismissal.

**Source:** What you can now inspect

## MA-ch02.60

Check each statement that is true about what the three jobs look like at this scale. Each statement is worth 1 point (5 points total).

- [ ] A. You conducted by writing the contract, the evaluation set, and the evidence criterion before any prompt was tried.
- [ ] B. You checked by treating a passing validator result as sufficient evidence of support.
- [ ] C. You conducted by tuning the prompt first and then writing the contract to match.
- [ ] D. You drove by signing the sign-off that Claude drafted without checking it against your record.
- [ ] E. You drove by handing Claude the definition of acceptable.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The criterion came first.
- B: You named the obligation each pass covered and kept format and support apart.
- C: The contract comes first.
- D: You write it from your record and sign or withhold.
- E: That stays with you.

**Source:** What you can now inspect

## MA-ch02.61

Check each statement that is true about the move from accepting text to taking action. Each statement is worth 1 point (5 points total).

- [ ] A. Passing an output contract establishes permission to perform the requested action.
- [ ] B. The chapter says Chapter 3's capability classifier is a complete taxonomy of AI systems.
- [ ] C. A mode label is no more an authorization policy than a source identifier is proof of support.
- [ ] D. If a later system can read files, write changes, or request a tool call, a correctly shaped answer sits near an action boundary.
- [ ] E. The current consumer accepts or rejects a response object and does not execute the answer.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It does not.
- B: Resist treating its names as complete.
- C: The same kind of mistake.
- D: The stakes rise.
- E: It has no action.

**Source:** From acceptable text to consequential action

## MA-ch02.62

Check each statement that is true about the Anthropics closing section. Each statement is worth 1 point (5 points total).

- [ ] A. Anthropic's Prompt evaluations course includes separate material on human-, code-, and model-graded evaluations.
- [ ] B. The chapter says to adopt the upstream evaluation approach without needing further evidence.
- [ ] C. The repository overview was checked on 2026-09-06.
- [ ] D. The few lines of this chapter's validator reproduce the upstream evaluation system.
- [ ] E. Older model identifiers, additional tools, and API-based examples in the upstream material become requirements for this exercise.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The three kinds are distinguished.
- B: You explain what evidence would justify adopting it and what it would still not establish.
- C: The link-check date is recorded.
- D: Do not infer that.
- E: They do not become requirements.

**Source:** Anthropics

## MA-ch02.63

Check each statement that is true about the Computational Skepticism note on prompt sensitivity. Each statement is worth 1 point (5 points total).

- [ ] A. Meaning-preserving changes are a diagnostic question: what should stay the same when expression changes but the intended task does not.
- [ ] B. What carries over between domains is one shared attack mechanism.
- [ ] C. The exercise proves a broad theory of model understanding.
- [ ] D. If you use the paraphrases to revise the prompt, they have become development evidence.
- [ ] E. The book's example pairs "List the key points of this document" with "What are the main takeaways from this document?"

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The note's central question.
- B: Only the diagnostic question carries over.
- C: It proves no such theory.
- D: The held-out boundary applies.
- E: Stability under such a rephrase is the property worth testing.

**Source:** Computational Skepticism
