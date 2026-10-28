# Chapter 2: Prompt contracts and evaluation

## ES-ch02.1

The chapter opens with a source whose only sentence is "The color is blue." (identifier s1) and a response that says the fixture says red while citing s1. Explain why this response passes the validator, and what the chapter says the failure actually is.

**Points:** 5

**Rubric (1 point each):**

1. States that the source sentence for s1 says blue while the response claims red.
2. Says the response is valid in form: well-shaped, nonblank answer, and a known identifier, so every implemented rule is satisfied.
3. Says the validator's pass does not involve any comparison between the answer and the source's content.
4. Notes that nothing crashed and the program returned exactly the result its rules required.
5. Locates the failure in the distance between what the validator checks and what a reader might assume a green result means, not in an exotic model behavior.

**Source:** Opening section (untitled introduction)

## ES-ch02.2

The chapter reports a format-pass rate of one-third for its three constructed responses. Name the three responses, say which one is accepted, and explain why calling the result an accuracy score would misname it.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the three responses: a string that is not JSON, a response citing an unknown identifier, and a properly shaped response citing a known identifier.
2. States that only the third is accepted, so the rate is one accepted out of three, 1/3.
3. Notes that the accepted response contradicts the supplied sentence, so it is accepted without being correct.
4. Explains that the rate measures acceptance by the format and identifier rules.
5. Concludes that calling it an accuracy score would misname the measurement.

**Source:** Opening section (untitled introduction)

## ES-ch02.3

The chapter calls its example "an executed, constructed counterexample, not a transcript of Claude making a mistake." Explain what that means and what the chapter says about keeping constructed strings and real model responses apart.

**Points:** 5

**Rubric (1 point each):**

1. States that the three responses were constructed by hand and no model was called.
2. States that the example was executed, so the validator's acceptance results are real results.
3. States that a locally constructed string is useful test data.
4. States that it becomes misleading only when presented as an observed model response.
5. Says that when you later compare actual prompts with Claude Code, the real responses are saved separately from these fixtures.

**Source:** Opening section (untitled introduction)

## ES-ch02.4

Chapter 1 gave three jobs: conduct, check, and drive. Explain what each becomes in this chapter and what Claude is and is not good at in this setting.

**Points:** 5

**Rubric (1 point each):**

1. Conduct: the gate becomes a contract plus an evaluation set, written for the consuming program before any prompt is tried.
2. Check: becomes the discipline of naming what a pass covers and what it leaves out.
3. Drive: becomes deciding what "acceptable" means for this consumer and this claim, which no schema holds.
4. Says Claude is strong on the near side: given a complete contract it can write the validator, enumerate malformed inputs, draft prompt variants, and tabulate pass rates.
5. Says whether an answer follows from the sentence it cites is a verification question that belongs on the far side.

**Source:** Opening section (untitled introduction)

## ES-ch02.5

A colleague proposes asking Claude whether its own answer follows from the sentence it cited, and treating a "yes" as verification. Using the chapter's argument, explain why this does not give an independent check and what kind of check the chapter wants.

**Points:** 5

**Rubric (1 point each):**

1. Says producing an answer and verifying it are different operations.
2. Says asking the generator to vouch for itself is more of the first operation, not a second opinion.
3. Says a check run by the system that produced the answer is not independent of it.
4. States the part of the argument the chapter keeps: a trustworthy check fails differently from the thing it checks.
5. Says choosing that check is a human decision, and that the book states its strongest version of the claim as a wager, not a proven fact.

**Source:** Opening section (untitled introduction)

## ES-ch02.6

Explain why the chapter says the contract must be written before the prompt. What goes wrong if you tune the prompt until the output looks right, and what role does Claude's handling of incomplete specifications play?

**Points:** 5

**Rubric (1 point each):**

1. Says the consumer's need is the only criterion that exists before an output does.
2. Says that tuning first makes the contract become whatever the output happened to look like.
3. Says that every later pass rate then measures agreement with your own habituation.
4. Says Claude implements well against a complete specification but may quietly fill an incomplete one with something plausible instead of flagging the gap.
5. Concludes that completeness is the human's job and the prompt is derived from the contract, not the other way around.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.7

The teaching contract accepts exactly two keys. A response contains answer, sources, and confidence, and all three values look reasonable. Predict the validator's result and discuss the trade-off, naming one consumer who finds the rule protective and one who finds it an obstacle.

**Points:** 5

**Rubric (1 point each):**

1. Predicts that the validator rejects the response because of the extra key.
2. Explains that a consumer assuming a fixed shape finds the rule protective, because unexpected additions become visible instead of silently ignored.
3. Explains that an exploratory analysis wanting extensible metadata finds the same rule an obstacle.
4. States the trade-off as strict predictability versus accepting some useful objects, and that it cannot be called good or bad without naming the downstream job.
5. Says this is a choice a schema cannot make for you, so you choose the contract for your consumer.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.8

A teammate says "I added 'always obey the schema' to the prompt, so we do not need to validate the output." Respond using the chapter's distinction between a request and a check.

**Points:** 5

**Rubric (1 point each):**

1. Says the prompt requests behavior from the producer.
2. Says the validator checks the returned object against executable conditions.
3. Says a request can be ignored or misunderstood.
4. Says the local check has a definite acceptance rule.
5. Connects this to Chapter 1's point about the system prompt, one level up: a request is a hope and a check is a gate.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.9

The chapter gives a baseline request that asks for a JSON object with exactly two keys and a nonempty list of supplied source identifiers. Which parts of the request's intention does the validator enforce, which does it not, and why does the chapter want this asymmetry made visible now?

**Points:** 5

**Rubric (1 point each):**

1. Says the executable function enforces the output contract: exactly the two keys, a nonblank string answer, and a nonempty sources list of known identifiers.
2. Says it knows which identifiers are allowed.
3. Says it does not understand whether the answer follows from the contents of those sources.
4. Says the asymmetry should be made visible before a passing response encourages you to forget it.
5. Describes the baseline request as a proposal for an experiment, not a proven improvement.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.10

Consider the constructed response {"answer":"The sources do not say.","sources":["s1"]}. What does the reference validator do with it, why, and why do the obvious fixes (a status field, "be accurate" in the prompt) not work? What should you do if you redesign the contract?

**Points:** 5

**Rubric (1 point each):**

1. States that the validator accepts it.
2. Explains it is accepted for the same reason the false claim was: it cannot tell an honest refusal from an assertion.
3. Notes that the reference has no field for insufficient evidence.
4. Explains that adding a status field fails because the validator rejects the extra key, and that "be accurate" in the prompt does not supply a refusal state.
5. Says that whether a refusal is an acceptable answer, and how the consumer should see it, is a decision about the interface.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.11

The chapter says "none of this makes the design waterfall." Explain what it means by that, using the refusal finding, and say what you must record when a finding reopens an earlier decision.

**Points:** 5

**Rubric (1 point each):**

1. Says a finding such as the missing refusal state can reopen an earlier decision.
2. Says reopening a decision does not make the process waterfall.
3. Says the change must be recorded.
4. Names a new contract version and new tests as part of the record.
5. Says any case that guided the redesign counts as development evidence from then on.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.12

Describe the "Consumer" and "Contract" lines of the gate for the teaching example. What must each say, who decided them, and how does the contract treat text outside the JSON object?

**Points:** 5

**Rubric (1 point each):**

1. The Consumer line is one sentence naming the program that reads the answer and what it does with it.
2. For each line, you note who decided it: you, or a fixed requirement of the consumer.
3. The contract allows exactly the keys answer and sources.
4. The answer is a nonblank string, and sources is a nonempty list of strings, every one in the supplied identifier set.
5. Text outside the JSON object is a rejection, not something to repair silently, and the validator returns a decision, not a diagnosis.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.13

Describe the evaluation set the gate calls for and the rules governing the held-out list. Why must both lists be dated?

**Points:** 5

**Rubric (1 point each):**

1. States five development questions and five held-out questions.
2. States that both are listed and dated before any response is inspected.
3. States that the held-out list is sealed: not shown to Claude.
4. States that it is not used to revise the prompt until the revision is frozen.
5. Says these decisions are written down before running anything.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.14

Describe the evidence criterion the gate requires: its content, the outcomes it records, and when it must be written.

**Points:** 5

**Rubric (1 point each):**

1. States that for each question there is one sentence saying what "supported" means for it.
2. Names supported and contradicted as recorded outcomes.
3. Names "cannot be reviewed" as a third recorded outcome.
4. Connects it to Computational Skepticism for AI: record pass, fail, or unknown against a criterion fixed before you read the output.
5. Says it must be written before you know which prompt wins.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.15

The gate lists wrong versions your tests must catch and one wrong response they cannot. Name each of them and say where the uncatchable one is caught instead.

**Points:** 5

**Rubric (1 point each):**

1. Names a validator that checks only that the keys exist.
2. Names a validator that accepts a source list when any entry is known, where the contract says every entry.
3. Names a validator that skips the nonblank check.
4. Names the well-formed and wrong response, the color fixture, as the one no validator test will catch.
5. Says your evidence column must catch the color fixture.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.16

For each held-out question the gate asks for a "what a failure looks like" sentence. What must the sentence describe, when must it be written, and what does it mean if you cannot write it?

**Points:** 5

**Rubric (1 point each):**

1. Says it describes an answer that would pass the validator and fail the evidence criterion.
2. Says it is written and dated before you see a response.
3. Says that if you write it afterward you have described the output, not tested your understanding.
4. Says that if you cannot write the sentence, you do not yet know what you are checking for.
5. Says one such sentence is needed for every held-out question as part of the pass condition.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.17

State the gate's pass condition and say what the experiment may and may not claim once it is run.

**Points:** 5

**Rubric (1 point each):**

1. Says every line of the contract must have a named test that fails if the line is deleted.
2. Says both question lists must be dated.
3. Says each held-out question must have its failure sentence.
4. Says the experiment may claim acceptance by a stated validator of recorded responses plus a separate support judgment on the claims reviewed.
5. Says it cannot claim that any answer is correct beyond those reviewed claims.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.18

How can Claude help sharpen the gate, and why can it not write the gate for you?

**Points:** 5

**Rubric (1 point each):**

1. Says you can ask Claude for a malformed input your list lacks.
2. Says you can ask Claude for a contract line your tests do not defend.
3. Says Claude cannot write the gate without defeating its purpose.
4. Says the gate is the criterion fixed before the output exists.
5. Says a criterion drafted after the outputs arrive is a description of the outputs.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.19

Trace the strings "not json" and {"answer":"x","sources":["missing"]} through validate() with allowed identifiers {"s1"}. For each, name the first boundary it fails and the rules that never ran.

**Points:** 5

**Rubric (1 point each):**

1. For "not json": json.loads raises and the exception path returns False.
2. For "not json": none of the dictionary or field checks runs.
3. For the second string: parsing and the shape checks succeed.
4. For the second string: it fails source membership because missing is not in the supplied identifier set.
5. Notes that validate() returns only False in both cases, so the reviewer must name the reason by stopping at the first relevant boundary.

**Source:** What each line of the validator promises

## ES-ch02.20

List the obligations validate() imposes on the answer and sources fields, and for each give an input that violates it.

**Points:** 5

**Rubric (1 point each):**

1. The answer must be a string, so the integer 1 fails because the function does not coerce.
2. The answer must be nonblank after strip(), so a whitespace-only answer fails.
3. The sources field must be a list.
4. The list must not be empty.
5. Every entry must be a string in source_ids, and one valid identifier cannot compensate for another invalid entry.

**Source:** What each line of the validator promises

## ES-ch02.21

The reference validator collapses every rejection into a Boolean False. Evaluate this design choice using the chapter's reasoning.

**Points:** 5

**Rubric (1 point each):**

1. Calls it an intentional simplification worth judging.
2. Gives the benefit: a Boolean is convenient for a pass rate and easy to test.
3. Gives the cost: it tells a reviewer nothing about how to repair a response.
4. Says a richer result naming the parse failure, key mismatch, wrong type, or unknown source is a reasonable extension to your own version, not a behavior of the reference.
5. Says the absence of a message is not the absence of a reason, so for each failing fixture you stop at the first relevant boundary and name it, instead of saying the output was bad.

**Source:** What each line of the validator promises

## ES-ch02.22

Describe the scratch-copy experiment the chapter proposes on the reference validator and what it shows about "the tests pass."

**Points:** 5

**Rubric (1 point each):**

1. Says to predict the result first, then check.
2. Says changing all to any in a scratch copy leaves all six tests passing.
3. Says deleting the nonblank check leaves all six tests passing, as does deleting the nonempty-source check.
4. Concludes that the contract promises three behaviors the lesson's tests never defend.
5. Concludes that "the tests pass" means they pass for the behaviors they exercise, and that additional tests should target such a gap chosen by reason, not repeat the happy path.

**Source:** What each line of the validator promises

## ES-ch02.23

Someone tells you that validate() "verifies source support." How do you respond using the chapter's argument?

**Points:** 5

**Rubric (1 point each):**

1. Says to ask them to point to the comparison between source content and answer content.
2. Says they cannot, because source_ids supplies identifiers, not passages.
3. Says the validator receives only the allowed identifier set, not the source sentence.
4. Says membership in a registry and support for a proposition are different relations.
5. Says the validator can reject an invented address such as missing but cannot decide whether the words attached to s1 support the answer.

**Source:** What each line of the validator promises

## ES-ch02.24

The chapter says the review asks two distinct questions. State them, explain how they relate, and illustrate with the color fixture.

**Points:** 5

**Rubric (1 point each):**

1. States the first question: does the referenced source exist in the supplied collection?
2. States the second question: does that source support this particular claim?
3. Says passing the first makes the second possible but does not answer it.
4. Says an address can point to a real document while the accompanying summary misstates it, as when s1 is cited for red.
5. Says the address remains useful because it gives the reviewer somewhere to look.

**Source:** A source identifier is an address, not an argument

## ES-ch02.25

Why does the chapter say the color counterexample is stronger than a vague warning about hallucination, and does it show that the validator is broken?

**Points:** 5

**Rubric (1 point each):**

1. Says we know which check is absent.
2. Says we can trace why the response passes without speculating about model internals.
3. Says the third response satisfies every implemented condition.
4. Says the validator is not broken because it succeeds at enforcing its stated structural and identifier contract.
5. Says the validator fails only if someone misrepresents that contract as a complete evidence check.

**Source:** A source identifier is an address, not an argument

## ES-ch02.26

Who should answer the support question for a claim and its cited source? Discuss Claude's role, its limits, and what you should and should not ask for in an explanation.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude can be asked to set the two sentences side by side, and in a case this small you can verify the comparison at a glance.
2. Says that if the generator is the only reviewer of its support, you have the first opinion run twice.
3. Says a brief explanation with cited evidence makes the answer easier to inspect but is still output to evaluate.
4. Says not to request hidden chain-of-thought or treat an articulate rationale as access to an authenticated internal process.
5. Says what you need is a reviewable claim, the referenced material, and a short justification that can be checked against the material.

**Source:** A source identifier is an address, not an argument

## ES-ch02.27

Before running the three-response experiment you are told to write predictions. Give the predictions the chapter's analysis supports for the validator and for a reviewer holding the source sentence, and say how the third validator prediction should be reached.

**Points:** 5

**Rubric (1 point each):**

1. Says predictions are written before reading the results, using the identifier set {"s1"}.
2. Says the validator decision and the reviewer's judgment are predicted separately.
3. Says the third validator prediction should be based on the function, not on whether the answer is true.
4. Gives the validator sequence false, false, true.
5. Gives the review sequence: cannot be reviewed, cannot be reviewed, contradicted by s1.

**Source:** Work through the three-response experiment

## ES-ch02.28

Explain how pass_rate computes its result for the three-response fixture and what the denominator and the sample do and do not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Says each accepted response contributes one and each rejected response contributes zero.
2. Computes one acceptance among three, so 1/3, saved as 0.3333333333333333.
3. Says the denominator is the number of supplied responses and the function does not know how they were selected.
4. Says the three cases were constructed to expose three boundaries, are not a random sample, and no model was called to generate them.
5. Concludes that one-third describes acceptance of this fixture set by this validator and estimates nothing about how often a real service will make these mistakes.

**Source:** Work through the three-response experiment

## ES-ch02.29

Why does pass_rate raise an error on an empty list of responses instead of returning 0 or 1?

**Points:** 5

**Rubric (1 point each):**

1. States that with no responses the function raises an error (ValueError).
2. Explains that zero could be mistaken for a tested system that failed every case.
3. Explains that one could be mistaken for perfect performance.
4. Explains that an empty experiment has no denominator.
5. Concludes that this makes absence of evidence harder to disguise as a performance number.

**Source:** Work through the three-response experiment

## ES-ch02.30

Reproduce the chapter's table for the three responses: for each, give the validate() result, the obligation failed or passed, and the support review. Then say how the report should treat the third row.

**Points:** 5

**Rubric (1 point each):**

1. For "not json": False, failed at parsing with no later rule run, and cannot be reviewed because there is no claim to compare.
2. For the missing-identifier response: False, parsed and shaped correctly but failed source membership, and cannot be reviewed because the cited address resolves to nothing.
3. For the red response: True, passed every implemented condition, and contradicted by s1, "The color is blue."
4. Says "format accepted and evidence contradicted" is the expected report for the third row, not an inconsistent one.
5. Says not to invent one numeric evidence score to make the table symmetrical; decide how unsupported, contradicted, and cannot-be-reviewed results are represented first.

**Source:** Work through the three-response experiment

## ES-ch02.31

Explain the fluency trap and how it applies to a True from validate(), including the cost asymmetry between the validator and the support review.

**Points:** 5

**Rubric (1 point each):**

1. Defines the trap: the more fluently an output presents, the more confident you become in it and then in your own evaluation of it.
2. Says form and content are independent.
3. Says a True is a verdict in the shape of a settled question.
4. Gives the defense: define the failure condition before you read the output, test against evidence, and record pass, fail, or unknown.
5. Says the validator is the cheap check and the support review the expensive one, and the risk is reporting the cheap green as if it were the expensive one's.

**Source:** Work through the three-response experiment

## ES-ch02.32

You replace the constructed strings with real Claude responses. What stays the same, what changes, and what must you preserve?

**Points:** 5

**Rubric (1 point each):**

1. Says the same calculation applies.
2. Says the provenance changes.
3. Names what to preserve: exact prompts, source materials, interface, model label, and date.
4. Says a fixture evaluation demonstrates validator behavior.
5. Says a recorded model experiment examines returned outputs under its recorded conditions, and that both must stay distinguishable in the artifact.

**Source:** Work through the three-response experiment

## ES-ch02.33

The lesson compares a baseline prompt and a few-shot revision on five development questions with five questions held out. What does this design establish, what does it not, and how should the revision be framed and varied?

**Points:** 5

**Rubric (1 point each):**

1. Says it is a manageable classroom experiment.
2. Says ten questions do not establish broad reliability.
3. Says a fixed evaluation set is what makes an improvement measurable, since without one "better" is a feeling.
4. Says the revision is a hypothesis: predict a specific failure it might address, and treat the idea that examples will help as a testable proposal rather than a result.
5. Says the revision should differ in a way you can describe, because changing examples, task, source material, persona, and questions at once makes any difference hard to attribute.

**Source:** A prompt revision is a hypothesis

## ES-ch02.34

Scenario: a developer tunes a prompt over several rounds, looking at the held-out questions each time to decide what to change, and then reports the held-out score as independent evidence. Using the chapter, explain the problem and a proper way to proceed.

**Points:** 5

**Rubric (1 point each):**

1. Says a held-out case that has guided a choice has changed its role and is development evidence now.
2. Says this is bookkeeping, not a moral failing.
3. Says the change should be recorded.
4. Says that if another untouched check is needed, a new evaluation should be designed.
5. Says the old cases must not be relabeled to keep calling the final score independent.

**Source:** A prompt revision is a hypothesis

## ES-ch02.35

Why does the chapter ask you to preserve development failures and to specify the evidence criterion before you see which prompt performs better?

**Points:** 5

**Rubric (1 point each):**

1. Says to preserve development failures rather than showing only the final success.
2. Says that otherwise you may tighten or relax what a pass means to favor the output you prefer.
3. Notes that the executable format rule is one fixed criterion.
4. Says the support review needs an equally explicit question, such as whether each stated claim is supported by the supplied material.
5. Says the support criterion needs a documented way to handle insufficient evidence.

**Source:** A prompt revision is a hypothesis

## ES-ch02.36

A colleague reports that adding "You are an expert" made answers better. How should the claim be handled according to the chapter?

**Points:** 5

**Rubric (1 point each):**

1. Says a persona is a hypothesis to test.
2. Says it adds no supporting passage to the source collection.
3. Says it changes none of the validator's checks.
4. Says that if it helps on your cases, you describe the observed difference and the conditions.
5. Says the role label must not certify the answer before the evidence review begins.

**Source:** A prompt revision is a hypothesis

## ES-ch02.37

What can Claude Code do for the experiment, what four items must you keep visibly separate, and how should you label an experiment you have not run?

**Points:** 5

**Rubric (1 point each):**

1. Says Claude Code can organize the experiment, run your local validator, draft candidate prompts, and challenge your interpretation.
2. Names the proposed prompt as one of the four items.
3. Names the actual returned text and the executable acceptance result as two more.
4. Names your evidence judgment as the fourth.
5. Says an unrun comparison should be labeled a proposed experiment, because a complete-looking table with invented outputs is worse than an honest plan.

**Source:** A prompt revision is a hypothesis

## ES-ch02.38

A report says only "The revised prompt achieved a higher pass rate." List the questions the chapter says a reader would need answered before using that number.

**Points:** 5

**Rubric (1 point each):**

1. Asks which validator produced it.
2. Asks which cases and how many responses were used.
3. Asks whether the cases were used during revision.
4. Asks whether the accepted responses remained supported.
5. Asks whether a formatting improvement coincided with an evidence failure.

**Source:** What a pass rate leaves out

## ES-ch02.39

Explain three things a single pass rate compresses or assumes: failure categories, weighting, and completeness.

**Points:** 5

**Rubric (1 point each):**

1. Says a non-JSON response and a response with one unknown source identifier both contribute zero, though their repairs differ.
2. Says counting failures is useful for summary, while preserving categories is useful for diagnosis, and the experiment record can keep the detail the function does not return.
3. Says every response is weighted equally, and the reference has no notion of which question or claim matters more.
4. Says equal weighting is simple and transparent but not a discovered fact, and another policy should be justified openly instead of hidden in the aggregate.
5. Says a format pass does not establish completeness, since a nonblank answer can be short, irrelevant, or evasive.

**Source:** What a pass rate leaves out

## ES-ch02.40

What is the chapter's practical test for whether a reported number is meaningful, and what does it call the chapter's strongest demonstration?

**Points:** 5

**Rubric (1 point each):**

1. States the test: could a reader reconstruct how the reported number was produced?
2. Says that if so, the statistic has a mechanical meaning even if its scope is narrow.
3. Says that if not, the number may be functioning as decoration.
4. Says none of this is a reason to abandon the check; name it accurately and pair it with the review the task needs.
5. Names the strongest demonstration as a correctly interpreted mixed result: two known failures rejected, one semantically false claim accepted, and all three outcomes explained.

**Source:** What a pass rate leaves out

## ES-ch02.41

Describe how the chapter wants you to build your first validator and why it should be done before consulting the reference or Claude.

**Points:** 5

**Rubric (1 point each):**

1. Says to write it from the stated contract, not from the reference.
2. Says to make the parsing boundary explicit and decide how a failure will be represented before implementing the shape, answer, and identifier checks.
3. Says not to begin with a framework or another model call.
4. Says the standard-library version is short enough to explain completely, and that explanation is the capability being built.
5. Says your version records what you understood before Claude touched anything and is the instrument for measuring Claude's version.

**Source:** Build It: your validator is the baseline

## ES-ch02.42

How should you extend the six lesson tests, and what must you do to show that a new test is meaningful?

**Points:** 5

**Rubric (1 point each):**

1. Says to read the six lesson tests before the reference and predict each result.
2. Says to add tests that defend the lines the six leave open.
3. Says to state the defect each test exposes.
4. Says to state one different defect that could still survive it, and to prove the test works by running it against a scratch copy with that line removed.
5. Says a larger test count is not coverage.

**Source:** Build It: your validator is the baseline

## ES-ch02.43

Your own validator rejects the "valid but unsupported" color-fixture response. What does the chapter tell you to do and conclude, and how should an extension such as a status field be handled?

**Points:** 5

**Rubric (1 point each):**

1. Says to inspect why it was rejected.
2. Says perhaps you accidentally added a semantic rule, or perhaps the response's structure does not match the contract.
3. Says the goal is to distinguish an added check from a mistaken explanation of the existing one, not to force every implementation to share the reference's limits forever.
4. Says an extended interface with a status field or diagnostic object should be a separate, tested version, documenting benefit and migration cost.
5. Says you must not modify the reference and then cite its old tests as validating the new behavior.

**Source:** Build It: your validator is the baseline

## ES-ch02.44

Describe what you hand Claude Code in the Use It exercise and what three things you do with the result.

**Points:** 5

**Rubric (1 point each):**

1. Says you give it the gate, meaning the contract, the test list, and the fixtures, and not your validator.
2. Says you run your tests on what it returns yourself.
3. Says a failing test is often a gap in your gate, because Claude had only what you wrote.
4. Says to compare its validator with your baseline and name one difference in behavior.
5. Says to ask Claude for three plausible-but-wrong validators and run your tests against them; a survivor is a hole in your gate, and whether your tests are enough cannot be judged by the system they are testing.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch02.45

Describe how you run and review the prompt comparison in Use It, from the questions given to Claude through to the held-out questions.

**Points:** 5

**Rubric (1 point each):**

1. Says to give Claude the baseline prompt and the few-shot revision on the same five development questions.
2. Says to ask for a short explanation and cited evidence, not hidden chain-of-thought.
3. Says to save failures as well as successes.
4. Says to run your validator on every response and then do the support review yourself, claim by claim, against the source text, using the criterion you wrote in the gate.
5. Says to reveal the held-out questions only when your revision is frozen, and to record that you did.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch02.46

After writing your explanation of the results, you ask Claude which claim in it is stronger than the executed check. How should you treat the answer, and what must you preserve from the session?

**Points:** 5

**Rubric (1 point each):**

1. Says the purpose is to find a claim in your explanation that is stronger than the executed check.
2. Says you inspect Claude's criticism yourself.
3. Says an AI reviewer can surface a useful issue.
4. Says its agreement is not a second source for the sentence in the fixture.
5. Says to preserve the actual transcript (prompts, plan, diff, commands, outputs, date, displayed model label) and to record a failed or unrun session rather than substituting a fixture.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch02.47

Claude's reply arrives wrapped in a code fence and introduced by a sentence, so the strict contract fails. How should this be handled in the experiment record, and whose decision is whether to tolerate such replies?

**Points:** 5

**Rubric (1 point each):**

1. Says the text wrapped in a code fence or introduced by a sentence fails json.loads.
2. Says to preserve each response before editing or repairing it.
3. Says not to remove the prose and score the repaired string as though it arrived that way.
4. Says to record the original and the repaired version with their roles separated, and to record Claude's help with the repair as a transformation, not as part of the original run.
5. Says whether the consumer should tolerate such replies is a contract decision made in the gate, not a convenience to grant after the fact.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.48

What does the Ship It artifact contain, and what should its change log say?

**Points:** 5

**Rubric (1 point each):**

1. Names the contents: baseline and revised prompts, development and held-out cases, raw responses, validation results, and a change log.
2. Says its purpose is to let another reader reconstruct both the mechanics and your decisions.
3. Says to keep the baseline intact and name the change in the next version.
4. Says "Improved prompt" is not a change log; state which instruction, example, or boundary changed, why you expected it to matter, and what the development results showed.
5. Says a revision that did not help is still an informative result when the trail is intact.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.49

Describe the integrated evidence review and the kind of limited conclusion the chapter suggests you write.

**Points:** 5

**Rubric (1 point each):**

1. Says to take one accepted answer and compare each meaningful claim with the supplied source material.
2. Says to mark unsupported content separately from formatting status.
3. Notes that in a real task a passage may support only part of an answer.
4. Says one correct citation must not stand in for a claim-by-claim explanation.
5. Gives an example conclusion: a revision changed format acceptance on the recorded cases while leaving a particular source-support failure unresolved, which tells the next person what to reuse and what remains risky.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.50

Describe the sign-off template: its fields, what the Not checked and Not claiming lines might contain, and why it should be written from your record rather than from Claude's draft.

**Points:** 5

**Rubric (1 point each):**

1. Names the fields: Checked, How, Not checked, Not claiming, and Signed or withheld.
2. Gives example Not checked items such as held-out cases you tuned against or claims in answers you did not review.
3. Gives example Not claiming items such as that the format pass rate measures accuracy or that the revision is better in general.
4. Says Claude can draft the words quickly and the draft will be fluent, so you write from your record.
5. Says this is a template, not a signature.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.51

Explain how to choose the verbs in a sign-off and what to do if the support review is unfinished.

**Points:** 5

**Rubric (1 point each):**

1. Says the rate was computed and the decisions were recorded.
2. Says support was reviewed for the claims you reviewed.
3. Says nothing was established beyond that.
4. Says an unfinished support review should be written as pending.
5. Says a missing review silently replaced by an automated pass is the failure the chapter is about, and withholding your name is an honest result.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.52

Name at least three judgments in this chapter that no schema field can hold, and explain why the validator and Claude cannot settle them.

**Points:** 5

**Rubric (1 point each):**

1. Names at least three of: whether the consumer tolerates extra keys; whether "the sources do not say" is acceptable; whether one correct citation plus one unsupported claim passes; whether equal weighting is right; what "the same meaning" requires.
2. Says the validator can enforce a decision once made but has no way to make it.
3. Says Claude can lay out the options and the consequences of each quickly.
4. Says Claude lacks the consumer, the stakes, and a person who bears the cost of a wrongly accepted answer.
5. Says none of that is in the files Claude reads unless you put it there.

**Source:** The driver's seat: what counts as acceptable

## ES-ch02.53

Take two rows of the chapter's division-of-labor table, "Judge whether an answer is supported" and "Draft prompts and tabulate pass rates." For each, say what Claude does, what you do, and why the row stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Support row: Claude lays the claim beside the source and proposes a verdict.
2. Support row: you make the call, claim by claim, against the source itself.
3. Support row: it stays with you because a check run by the generator is the first opinion run twice, and "supported" is your definition.
4. Drafting row: Claude drafts variants, runs the validator, and tabulates, while you choose the one feature that changes and fix the development and held-out lists before looking.
5. Drafting row: it stays with you because the split is a promise about what you will not look at, and only you can keep it.

**Source:** The driver's seat: what counts as acceptable

## ES-ch02.54

The chapter asks you to record one task you delegated and one judgment you retained. What is the test for whether that record is adequate, and who is accountable for the pass-rate claim?

**Points:** 5

**Rubric (1 point each):**

1. Says to record one delegated task in the experiment.
2. Says to record one retained judgment.
3. Says you should be able to point to the transcript line or the edit that shows each.
4. Says that if you cannot, the split happened in your head and not in the record.
5. Says that for what the pass rate supports, Claude flags an overclaim but you choose the verb and sign or withhold, because your name is on the claim.

**Source:** The driver's seat: what counts as acceptable

## ES-ch02.55

Describe the provenance questions the chapter asks you to answer in Verify and reflect, and the reflection question it calls most useful.

**Points:** 5

**Rubric (1 point each):**

1. Says to rerun the three-response experiment and explain why its one-third result is a format rate.
2. Says to label your own execution as your run, with its own environment record.
3. Asks which strings you constructed and which came from an actual Claude interaction.
4. Asks which questions guided revision and which were still held out when you inspected the result.
5. Names the most useful reflection as local: which distinction did you collapse (source membership and source support, format rate and accuracy, development case and held-out case), and which counterexample separated them again.

**Source:** Verify and reflect

## ES-ch02.56

Warm-up exercise: you test malformed JSON, a parsed value of the wrong shape, and an object with the correct keys but a wrong field type. For each, say what the first relevant rule is and explain the difference between a parser failure and a contract failure.

**Points:** 5

**Rubric (1 point each):**

1. Malformed JSON fails at json.loads, the parsing step.
2. A parsed value of the wrong shape fails at the check that it is a dictionary or has the exact key set.
3. An object with the correct keys but a wrong field type, such as an integer answer, fails at the field-type check.
4. Explains that a parser failure means the text never became an object, while a contract failure means a parsed object violates a stated rule.
5. Says each result should be explained by naming the first relevant rule, not merely called bad formatting.

**Source:** Assessments - ungraded practice

## ES-ch02.57

Application exercise: construct a short source with identifier s2 saying "The meeting is on Tuesday." and an answer that says Wednesday while citing s2. What does a validator like the chapter's do, what does the evidence review say, and how should you record and label the example?

**Points:** 5

**Rubric (1 point each):**

1. Says the response satisfies the same implemented conditions as the color fixture (if well shaped and s2 is in the allowed set), so the validator accepts it.
2. Says the evidence review records it as contradicted, since the source says Tuesday.
3. Explains that the results differ because source membership and source support are different relations.
4. Says to preserve the executable decision and the evidence judgment separately.
5. Says to keep the example explicitly labeled as constructed, not presented as something Claude actually said.

**Source:** Assessments - ungraded practice

## ES-ch02.58

Challenge exercise: design an explicit way to represent insufficient source evidence in a separate learner version. What must you address, and what must you not claim?

**Points:** 5

**Rubric (1 point each):**

1. Says the design lives in a separate learner version.
2. Says to explain who decides whether a refusal counts as an acceptable answer.
3. Says to explain how the change affects the exact-key and nonempty-source rules.
4. Says to state what the consumer must now handle and which tests are needed.
5. Says not to claim the reference already supports the new interface, and to compare the simplicity lost with the ambiguity removed.

**Source:** Assessments - ungraded practice

## ES-ch02.59

Challenge exercise: you prepare three paraphrases of one task. What must you decide before running anything, what do you compare if you run them, and why is different wording in an answer not automatically a failure?

**Points:** 5

**Rubric (1 point each):**

1. Says to keep the intended facts and obligations fixed across the three paraphrases.
2. Says to predict what should remain invariant and what may legitimately vary.
3. Says to say who decided where that line falls.
4. Says that if you run the prompts you compare format, claim content, and support separately, and that if you only design the test you label it as such.
5. Says different wording in an answer is not automatically a failure of the intended task.

**Source:** Assessments - ungraded practice

## ES-ch02.60

List the separate obligations the chapter says you can now name in the validator and explain the right response to the color fixture.

**Points:** 5

**Rubric (1 point each):**

1. Names at least six of: parsing, object shape, exact keys, answer type, nonblank content, source-list type, nonempty membership, allowed identifiers.
2. Says you can say which of them the lesson's tests defend and which they leave open.
3. Says you can explain a rejected response by locating the failed condition and propose a targeted test.
4. Says the right response to the color fixture is neither blind acceptance nor dismissal of automated checks.
5. Says to keep the structural check, name its scope, and add the evidence review the task requires.

**Source:** What you can now inspect

## ES-ch02.61

The current consumer only accepts or rejects a response object. Explain how the chapter says the stakes change when a later system can read files, write changes, or request a tool call.

**Points:** 5

**Rubric (1 point each):**

1. Says the current consumer does not execute the answer.
2. Says a correctly shaped answer then sits near an action boundary.
3. Says passing an output contract does not establish permission to perform the requested action.
4. Says a mode label is no more an authorization policy than a source identifier is proof of support.
5. Says the question changes from "Can my program consume this object?" to "What could happen if it does?", with Chapter 3's gate being how much autonomy is sufficient, chosen before the capability is granted.

**Source:** From acceptable text to consequential action

## ES-ch02.62

The chapter points to Anthropic's Prompt evaluations course. How should you use it, what must you not infer, and what is the follow-up task?

**Points:** 5

**Rubric (1 point each):**

1. Says the course includes separate material on human-, code-, and model-graded evaluations.
2. Says to use that separation to compare your small executable format check with the source-support judgment it leaves outside its scope.
3. Says not to infer that the chapter's few lines reproduce the upstream evaluation system.
4. Says older model identifiers, additional tools, and API-based examples in the upstream material do not become requirements.
5. Says to choose one upstream evaluation approach, state which question it could help investigate, what evidence would justify adopting it, and what it would still not establish.

**Source:** Anthropics

## ES-ch02.63

Explain the Computational Skepticism note on prompt sensitivity: the diagnostic question, the book's example, and the limit on what carries over between domains.

**Points:** 5

**Rubric (1 point each):**

1. States the diagnostic question: what should stay the same when expression changes but the intended task does not.
2. Gives the example pair: "List the key points of this document" and "What are the main takeaways from this document?"
3. Says stability under that kind of rephrase is the property worth testing.
4. Says what carries over between domains is the diagnostic question, not one shared attack mechanism, and that the exercise proves no broad theory of model understanding.
5. Says that paraphrases used to revise the prompt become development evidence, and that skepticism here is a precise question attached to a record, not a general instruction to distrust every answer.

**Source:** Computational Skepticism
