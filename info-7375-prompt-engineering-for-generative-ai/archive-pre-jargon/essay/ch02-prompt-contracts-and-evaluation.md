# Chapter 2: Prompt contracts and evaluation

## ES-ch02.1

A company deploys a policy question-answering assistant that must answer only from supplied policy documents. Its monitoring dashboard shows that 98% of responses pass a validator: the reply is valid JSON, it has an answer string and a list of document identifiers, and every identifier names a document that was supplied. A manual spot check finds that roughly one answer in five misstates the policy it cites. Explain how both figures can be true at once, what the 98% actually measures, and what additional evaluation the team needs.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the validator checks structure and identifier membership only, so a well-formed answer that contradicts its cited document still passes.
2. Says the 98% is a rate of structural and identifier compliance and should be named that way, not as accuracy or faithfulness.
3. Points out that the validator never compares the content of the answer with the text of the cited document, so a valid address can sit next to a false claim.
4. Proposes a content-level evaluation such as labeled reference answers, claim-by-claim review against sources, quote verification, entailment checks, or a calibrated judge model.
5. Recommends reporting structural pass rate and support rate as separate figures, with a defined way to handle answers that cannot be judged.

**Source:** A source identifier is an address, not an argument

## ES-ch02.2

Distinguish two questions a reviewer can ask about a citation in a generated answer: whether the cited source exists in the supplied collection, and whether that source supports the claim made. Explain how the two relate, give a concrete example in which the first is answered yes and the second no, and say who or what is suited to answer the second question and what limits apply to each candidate.

**Points:** 5

**Rubric (1 point each):**

1. States the first question as a registry or membership check and the second as a support or entailment relation between claim and source text.
2. Explains that a yes to the first makes the second answerable but does not answer it.
3. Gives a valid example, such as citing a real document whose text says something different from, or silent on, the claim.
4. Names suitable reviewers for the second question, such as a human reading the cited text, a quote-matching check, or a validated model judge.
5. Notes a limit on a model checking its own answer, namely that the generator reviewing itself is not independent, and that explanations are output to be evaluated.

**Source:** A source identifier is an address, not an argument

## ES-ch02.3

A team is adding a feature that summarizes a customer's contract and cites the clauses it relies on. Design a layered evaluation for it. Describe at least four layers, what each layer can and cannot detect, and how you would use cheap and expensive checks together.

**Points:** 5

**Rubric (1 point each):**

1. Describes a structural layer (parses, required fields, types) that is cheap and deterministic but blind to content.
2. Describes an identifier or reference layer (cited clause exists) and notes that it does not show support.
3. Describes a content-level layer such as verbatim quote matching, entailment checking, or a calibrated model judge, with its own error rate to be measured.
4. Describes sampled human review of accepted answers as the independent check against which automated layers are calibrated.
5. Explains the economics: run cheap layers on everything, spend expensive review where errors are costly, and report each layer's result separately.

**Source:** Work through the three-response experiment

## ES-ch02.4

A developer proposes tuning a prompt for a data-extraction task until the output looks good, and then writing the acceptance tests from the finished output. Explain what is wrong with this order, what the alternative order is, and what each approach does to the meaning of a later pass rate.

**Points:** 5

**Rubric (1 point each):**

1. Explains that tests written after tuning encode whatever the prompt happened to produce, so the criterion follows the output.
2. States the alternative: derive the required output and acceptance criteria from the consumer's needs first, then write and tune the prompt against them.
3. Explains that a criterion fixed before outputs exist can fail an output, whereas one fitted afterward cannot.
4. Says a pass rate under the post-hoc criterion measures agreement with the developer's own earlier judgment, not fitness for the consumer.
5. Notes that incomplete specifications are silently filled by plausible choices, so completeness of the criterion is the requester's responsibility.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.5

A colleague says: "I added 'Always obey the schema' to the system prompt, so we can skip output validation." Respond. Explain the difference between asking for a format and checking it, say what other mechanisms exist to improve compliance, and state what would still remain unchecked even if the format were guaranteed.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a prompt instruction is a request that can be ignored or misread, while a validator applies a deterministic accept or reject rule.
2. Notes that compliance rates below 100% are common and only a check detects the failures that remain.
3. Names other mechanisms, such as constrained or schema-guided decoding, examples in the prompt, or retry with the error message.
4. States that even guaranteed structure leaves content unchecked: values can be false, unsupported, or evasive.
5. Recommends validating at the boundary where the consuming program reads the output and measuring first-attempt compliance, not only final compliance.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.6

Two programs consume model output in the same company. Program P unpacks exactly three named fields and crashes on anything else. Program Q stores the whole object in a log for later exploratory analysis and benefits from extra fields the model volunteers. Should both use the same validator? Discuss the trade-off between closed key sets and tolerant key sets, give a recommendation for each program, and state who should decide.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a closed key set makes unexpected additions visible and protects consumers that assume a fixed shape.
2. Explains that a tolerant key set accepts useful extra information and avoids rejecting otherwise good responses.
3. Recommends strict key checking for P because extra fields cause crashes or silent misuse.
4. Recommends tolerance (possibly with logging of unknown keys) for Q, or a differently configured validator for each consumer.
5. Says the choice depends on the downstream job and should be made and recorded by the owner of the consumer, not defaulted from a convenient example.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.7

A grounded question-answering system must answer only from supplied documents. Its current output contract is an object with a nonblank answer and a nonempty list of supplied document identifiers. Users sometimes ask questions the documents do not answer. Explain what problem this contract creates, design a change that lets the system represent "insufficient evidence", and describe the consequences of your change for the validator, the tests, and the evaluation.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that the contract forces every response to look like a supported assertion, so an honest non-answer is indistinguishable from a factual claim.
2. Proposes an explicit representation such as a status or abstain field, a typed answer variant, or an allowed null answer with a reason.
3. Explains that the validator must be changed (and the rules for sources when abstaining decided) and treated as a new contract version.
4. Says tests must cover the new states, including a refusal that cites nothing and an attempt to abstain and assert at the same time.
5. Notes that evaluation needs unanswerable questions and separate measures for correct abstention and wrongful abstention, and that cases used to motivate the redesign become development evidence.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.8

Read this validator.

```python
import json

def ok(text, allowed):
    try:
        d = json.loads(text)
    except ValueError:
        return False
    return (isinstance(d, dict) and set(d) == {"answer", "sources"}
            and isinstance(d["answer"], str) and d["answer"].strip() != ""
            and isinstance(d["sources"], list) and len(d["sources"]) > 0
            and all(s in allowed for s in d["sources"]))
```

With allowed = {"a", "b"}, trace the inputs `not json`, `[1, 2]`, and `{"answer": "x", "sources": ["a", "c"]}`. For each, state the result, the first rule that decides it, and which later rules never run. Then name one input the function accepts that a careful reviewer might still reject.

**Points:** 5

**Rubric (1 point each):**

1. For `not json`: json.loads raises, the except clause returns False, and no shape or field rule is evaluated.
2. For `[1, 2]`: it parses, but isinstance(d, dict) is False, so the result is False and the short-circuiting and prevents key and field access.
3. For the third input: it parses, is an object with the right keys, a nonblank string answer, and a nonempty list, but "c" is not in allowed, so the final all(...) rule rejects it.
4. Notes that and-chaining with short-circuit evaluation is why order matters and why later rules never run once an earlier one fails.
5. Gives an input that passes but may be wrong in content, such as {"answer": "x", "sources": ["a"]} where the answer contradicts the document labeled a, or a placeholder answer, and explains that nothing compares content.

**Source:** What each line of the validator promises

## ES-ch02.9

A validator returns only True or False. Argue for and against this design, using a concrete scenario in which 40 of 200 responses were rejected. State what a richer return value would contain and what it would change about how the team could use the results.

**Points:** 5

**Rubric (1 point each):**

1. Gives the case for a Boolean: simple, easy to test, easy to aggregate into a pass rate.
2. Gives the case against: it discards the reason for rejection, so a maintainer cannot see what to repair.
3. Proposes returning a reason category, such as parse failure, wrong shape, missing or extra key, wrong type, or unknown identifier.
4. Explains how tallying failures by category directs repair (for example truncation versus bad identifiers) and supports diagnosis.
5. Notes that adding reasons need not change accept or reject decisions and that reporting counts by category is clearer than one rate.

**Source:** What each line of the validator promises

## ES-ch02.10

A validator accepts a response only if it is a JSON object with exactly the keys answer and sources, answer is a nonblank string, sources is a nonempty list, and every entry of sources is a string in the allowed set. The test suite has these tests: a valid object, text that is not JSON, answer equal to the integer 1, sources equal to a single unknown identifier, and an object with an extra key. Three mutated copies of the validator are made: one changes "every entry" to "at least one entry", one removes the nonblank check on answer, and one removes the nonempty-list check. Predict which mutants the tests detect, explain why, and describe the tests you would add.

**Points:** 5

**Rubric (1 point each):**

1. States that none of the three mutants is detected by the existing five tests.
2. Explains why for "at least one entry": the only unknown-identifier test has a single entry, which both versions reject.
3. Explains that no test supplies a blank answer or an empty list, so removing those checks changes no outcome.
4. Proposes tests: a list mixing known and unknown identifiers, a whitespace-only answer, and an empty sources list.
5. Concludes that passing tests show only that the exercised behaviors work, and a larger test count is not coverage; each rule needs a test that fails if the rule is deleted.

**Source:** What each line of the validator promises

## ES-ch02.11

A pipeline produced 80 responses to a citation-grounded task. The validator rejected 12 as not JSON, 6 for unknown source identifiers and 2 for extra keys. A reviewer then randomly selected 30 of the accepted responses and found 24 supported by their sources and 6 contradicted. Compute the validator acceptance rate, the supported share among the reviewed answers, and an estimate of the end-to-end proportion of the 80 that are both accepted and supported. State the assumptions behind the estimate and write one accurate sentence for a report.

**Points:** 5

**Rubric (1 point each):**

1. Computes 80 - 20 = 60 accepted, an acceptance rate of 60/80 = 75%.
2. Computes the reviewed supported share as 24/30 = 80%.
3. Estimates about 0.8 x 60 = 48 supported answers, or about 48/80 = 60% end to end.
4. States assumptions: the reviewed sample is random from the accepted answers, rejected responses are counted as failures, and the estimate carries sampling uncertainty (a standard error of about 7 points on the 80%).
5. Writes a report sentence that keeps the two measurements separate and scoped, rather than calling 75% accuracy.

**Source:** Work through the three-response experiment

## ES-ch02.12

A function computes a pass rate as accepted divided by total over a list of responses. Explain what the function should do when the list is empty, and why the obvious alternatives of returning 0 or returning 1 are poor choices. Relate your answer to how experiment reports are read.

**Points:** 5

**Rubric (1 point each):**

1. Says a rate with a zero denominator is undefined and the function should raise an error or return an explicit undefined value.
2. Explains that returning 0 can be read as a tested system that failed every case.
3. Explains that returning 1 can be read as a tested system that passed every case.
4. Notes that 0 divided by 0 raises an error in many languages and the explicit signal makes the problem visible rather than hiding it.
5. Relates this to reporting: absence of evidence should not be disguised as a performance number, and a report must always give its denominator.

**Source:** Work through the three-response experiment

## ES-ch02.13

A developer iterates on a prompt using 20 labelled questions. To keep an honest final test, they set aside 8 of the 20 as "held out". Over six rounds, they glance at the held-out failures each time to decide what to change, then report the final held-out score as independent evidence. Explain the problem and propose how to proceed from this point.

**Points:** 5

**Rubric (1 point each):**

1. Defines the purpose of a held-out set: an estimate on cases that did not influence design decisions.
2. Explains that using held-out failures to decide changes turns them into development evidence.
3. Explains the resulting bias: the held-out score is optimistically inflated because the prompt was fitted to those cases.
4. Proposes collecting or writing a fresh untouched set, or honestly relabeling and reporting the old one as development data.
5. Recommends recording what was inspected and when, freezing the revision before measuring on untouched cases, and limiting how many times the final set is used.

**Source:** A prompt revision is a hypothesis

## ES-ch02.14

You are asked to test whether adding three example input-output pairs to a prompt (few-shot prompting) improves a model's compliance with an output format and its faithfulness to supplied sources. Design the comparison. Cover what you hold fixed, what you change, how you split your cases, what you measure and how you record it.

**Points:** 5

**Rubric (1 point each):**

1. Holds fixed everything except the examples: task wording, source material, model, settings and cases.
2. Fixes development and held-out sets before looking at results and ensures the examples are not drawn from evaluation cases.
3. States a hypothesis in advance, such as "examples will raise format compliance", and a criterion fixed beforehand.
4. Measures format validity and source support as separate outcomes, with repeated runs to account for sampling variation.
5. Records exact prompts, model identifier and date, raw responses, and failures as well as successes, and limits conclusions to the conditions tested.

**Source:** A prompt revision is a hypothesis

## ES-ch02.15

A developer reports that prompt v2 beats prompt v1, 8 of 10 correct against 5 of 10. Between the runs they added examples, changed the model version, rewrote the instructions, and replaced the question set with an easier one. Explain why the comparison cannot support the conclusion that the examples helped, and describe a design that could.

**Points:** 5

**Rubric (1 point each):**

1. Identifies confounding: several things changed at once, so the effect of any one cannot be separated.
2. Notes that a different question set means the scores are not like-for-like, and easier questions raise scores independently.
3. Notes that a model version change alone can change behavior.
4. Describes a controlled comparison changing one identifiable feature with the same cases and settings.
5. Adds that sampling noise on ten cases limits the conclusion and that a written change log makes attribution auditable.

**Source:** A prompt revision is a hypothesis

## ES-ch02.16

Prompt A passes 14 of 20 test cases and prompt B passes 17 of 20 on the same cases. Treating each case as an independent trial, the standard error of a proportion is sqrt(p(1-p)/n). Compute the standard error for each prompt and for their difference, compare the three-case gap with that noise, and explain what you would do to reach a trustworthy conclusion.

**Points:** 5

**Rubric (1 point each):**

1. Computes about 0.102 for A (p = 0.70) and about 0.080 for B (p = 0.85).
2. Notes the standard error of the difference is about 0.13 (roughly sqrt(0.0105 + 0.0064)), so the 0.15 gap is only about one standard error.
3. Concludes the data do not establish that B is better than A, since a gap of about one standard error is well within chance variation.
4. Proposes more cases (on the order of a hundred or more per prompt for a gap of this size), or a paired comparison on the same cases with repeated runs.
5. Says to report the numbers with their uncertainty and not to claim superiority, and that the comparison must also fix the other conditions.

**Source:** A prompt revision is a hypothesis

## ES-ch02.17

A teammate says that beginning every prompt with "You are an expert in the subject" improves answer quality. Design a test of this claim for a source-grounded question-answering task, and explain how you would report a positive or negative result without over-reading it.

**Points:** 5

**Rubric (1 point each):**

1. Treats the claim as a hypothesis: same prompt with and without the line, with everything else fixed.
2. Uses a fixed set of cases split into development and held-out portions, with the evidence criterion set in advance.
3. Notes that the role line adds no new source passages and does not change a structural validator, so any effect must be measured on content.
4. Repeats runs or uses enough cases to separate an effect from sampling variation.
5. Reports the observed difference with its conditions (task, model, cases, criterion) and does not let the persona label stand in for evidence or generalize beyond those conditions.

**Source:** A prompt revision is a hypothesis

## ES-ch02.18

A team asks the same model that wrote an answer to judge whether the answer is supported by the cited source, and treats a "yes" as verification. Explain why this is a weak check, what makes a check independent, and describe two stronger alternatives and one situation where a model judge is nevertheless reasonable.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the judgment is another generation by the same system and shares its blind spots, so it is not independent.
2. Says that producing an answer and verifying it are different operations, and asking for a verdict is more generation, not a second opinion.
3. Defines independence: a check that fails differently from the thing it checks.
4. Names two stronger alternatives, such as quote matching against the source, human review of a sample, or a separately validated classifier.
5. Describes a legitimate use of a model judge, namely one whose agreement with human labels on a sample has been measured, ideally from a different model family.

**Source:** A source identifier is an address, not an argument

## ES-ch02.19

You will use a language model to grade open-ended answers. Describe how you would build confidence in this judge before trusting its scores, including the known biases to control for and how you would keep the judge's verdicts honest over time.

**Points:** 5

**Rubric (1 point each):**

1. Names the need to compare judge verdicts with human labels on a sample and report their agreement.
2. Names position bias and addresses it by swapping presentation order and checking consistency.
3. Names verbosity or length bias and self-preference bias as risks, and mitigates them by controls or by using a judge from another family.
4. Specifies a clear rubric and criterion fixed in advance, with an explicit outcome for cases that cannot be determined.
5. Plans ongoing monitoring, such as periodic human spot checks and rechecking when the judge model, prompt or data changes.

**Source:** A source identifier is an address, not an argument

## ES-ch02.20

For each of three tasks, choose a primary evaluation method (code-graded, model-graded or human-graded) and justify it: (1) checking that a reply is valid JSON with required keys; (2) scoring whether a summary preserves the key facts of an article; (3) deciding whether a medical-information answer is safe to show to patients. Then explain why combining methods is common.

**Points:** 5

**Rubric (1 point each):**

1. Chooses code-graded for the JSON check and justifies it as deterministic, cheap and fully specified.
2. Chooses model-graded (with human calibration) or rubric-based human grading for summaries, because many wordings are correct and exact match fails.
3. Chooses human (expert) review for the high-stakes medical case, possibly with automated screens in front.
4. Notes the cost and speed differences among the methods.
5. Explains that layering lets cheap checks run on everything and expensive ones target risk, with each result reported separately.

**Source:** A source identifier is an address, not an argument

## ES-ch02.21

Explain why people tend to trust fluent, well-formatted model answers more than they should, and how this affects the way automated checks are interpreted. Describe two practices that counter the effect when evaluating model output.

**Points:** 5

**Rubric (1 point each):**

1. States that fluency and correctness are independent properties; smooth text can be false.
2. Explains that a green result from an automated check has a similar effect, appearing to settle a question it did not examine.
3. Describes defining the failure condition in advance, before reading the outputs, as a counter-practice.
4. Describes testing against evidence and recording outcomes as pass, fail or unknown rather than forcing a verdict.
5. Notes the cost asymmetry: generating is cheap and verifying is expensive, so verification must be planned and budgeted.

**Source:** Work through the three-response experiment

## ES-ch02.22

A report on a prompt change says only: "The revised prompt achieved a higher pass rate." List the questions a careful reader would need answered before relying on that sentence, and rewrite the sentence so that it could be audited.

**Points:** 5

**Rubric (1 point each):**

1. Asks which check defined a pass (structural validator, reference match, reviewed support) and what it does not cover.
2. Asks how many cases and responses were involved, and how large the difference was relative to noise.
3. Asks whether the cases were used while revising the prompt, and whether the same cases were used for both versions.
4. Asks whether accepted responses remained supported, since a format gain can coincide with a content failure.
5. Provides a rewritten sentence naming validator, cases, counts, model and date, and scoping the claim to those conditions.

**Source:** What a pass rate leaves out

## ES-ch02.23

A single aggregate pass rate compresses information. Describe three things it hides or assumes, explain why each matters to a decision, and say what you would report in addition.

**Points:** 5

**Rubric (1 point each):**

1. Notes it merges different failure types (for example unparseable output versus one wrong identifier) that call for different repairs.
2. Notes it weights every case equally, ignoring that some questions or failures have much higher stakes.
3. Notes it says nothing about completeness or relevance of passing answers, such as a short, evasive but well-formed reply.
4. Notes it depends on the cases, criterion and sampling of the evaluation, so the number cannot be compared without them.
5. Recommends reporting counts by failure category, any severity weighting justified in advance, the denominator, and separate content-level results.

**Source:** What a pass rate leaves out

## ES-ch02.24

An invoice-assistant evaluation reports 95 of 100 cases passing. Of the 5 failures, 3 are cosmetic (a typo in a free-text note field) and 2 report an invoice total that is ten times too large. Argue whether a severity-weighted score would be better, how you would choose the weights, and when they should be chosen.

**Points:** 5

**Rubric (1 point each):**

1. Points out that the flat rate treats cosmetic and consequential failures as equal.
2. Argues that weights express stakes, so a weighted or tiered report (for example zero tolerance for wrong totals) better reflects risk.
3. Says weights are a policy decision to be made by whoever bears the cost of errors, with their reasoning written down.
4. Says weights must be chosen before results are seen, to avoid tuning them to favor an outcome.
5. Recommends also reporting the unweighted counts by category so the weighting can be inspected and challenged.

**Source:** What a pass rate leaves out

## ES-ch02.25

An evaluation harness receives a model reply wrapped in a Markdown code fence with an introductory sentence, and the strict JSON parser rejects it. An engineer proposes stripping the fence before scoring. Discuss whether to do this, what should be recorded, and who decides, covering both measurement integrity and the needs of the consuming program.

**Points:** 5

**Rubric (1 point each):**

1. Explains that scoring only the repaired text measures a different thing from the model's raw output.
2. Says whether the consumer will tolerate or repair such replies is a contract decision made before measurement.
3. Recommends preserving the original reply and recording any repair as a separate transformation.
4. Suggests reporting both rates (strict, and with tolerant parsing) if both behaviors matter to the consumer.
5. Notes that if repair is in production, it must be implemented in the pipeline and tested, and if a person or assistant did the repair, that should be recorded.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.26

A team writes: "The model fails to produce valid JSON in 40% of cases", based on 25 strings the team wrote by hand to exercise its validator, 10 of which were malformed. Explain what is wrong, what claim the data support, and what experiment would support the original claim.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that no model produced the strings, so the rate cannot describe any model's behavior.
2. States that 40% reflects how many malformed items whoever built the set chose to include.
3. States the supportable claim: the validator rejected 10 of the 25 constructed cases.
4. Notes constructed cases are still valuable for testing that a validator catches specific defects.
5. Describes the needed experiment: run the real model on a representative set of tasks, record raw responses with model, date and settings, and compute the rate with its denominator.

**Source:** Work through the three-response experiment

## ES-ch02.27

You have run an experiment comparing two prompts. The format validator accepted 4 of 12 baseline responses and 11 of 12 revised responses on the same twelve cases. You reviewed support claim by claim for 5 of the 11 accepted revised answers and found 4 supported and 1 contradicted. Nothing else was checked, on one model on one day. Write a short sign-off that states what was checked, how, what was not checked, and what you are not claiming, and explain your choice of verbs.

**Points:** 5

**Rubric (1 point each):**

1. States what was checked: validator decisions on the 24 recorded responses and a support review of 5 accepted revised answers.
2. States how: the validator rules and the manual claim-by-claim comparison against the sources.
3. States what was not checked: the support of the other six accepted revised answers, any baseline support review, other models, dates and wordings.
4. States what is not being claimed: that format pass equals accuracy, that the revision is better in general, that unreviewed answers are supported, or that the one contradicted answer is an isolated case.
5. Explains verb choice (computed, recorded, reviewed rather than established or proved) so the language matches the evidence, and treats an unfinished review as pending.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.28

You are using an AI assistant to help build an evaluation for a source-grounded question-answering feature. Divide the work: say what you would delegate to the assistant, what you would keep, and why. Include at least one judgment that no output schema can hold.

**Points:** 5

**Rubric (1 point each):**

1. Delegates drafting of test cases, implementing validators, enumerating malformed inputs and tabulating rates.
2. Keeps the definition of acceptable for the consumer, since stakes and consumers are outside the assistant's view.
3. Keeps the final support judgments or at least verifies them against the sources, because a check by the generating system is not independent.
4. Names a judgment a schema cannot hold, such as whether an honest "the sources do not say" is acceptable, whether extra fields are tolerated, or what level of partial support passes.
5. Explains that the person who bears the cost of a wrong accept should own the decision and sign off on the claim, and that the split should be visible in the record.

**Source:** The driver's seat: what counts as acceptable

## ES-ch02.29

Many consequential settings in an output-validation project cannot be expressed as fields in a schema or checked by a validator. Name at least four such judgments, explain why a validator cannot make them, and explain how the decisions should be recorded.

**Points:** 5

**Rubric (1 point each):**

1. Names whether extra fields are tolerated by the consumer.
2. Names whether an honest abstention such as "the sources do not say" counts as acceptable.
3. Names whether partially supported answers pass, or whether equal weighting of cases is appropriate when stakes differ.
4. Names what "the same meaning" requires when a prompt is reworded, or a similar equivalence judgment.
5. Explains that a validator enforces a decision once made but cannot make it, and the decision, its owner and its rationale should be written down before testing.

**Source:** The driver's seat: what counts as acceptable

## ES-ch02.30

A team wants to know whether its question-answering prompt is robust to rewording. Design a test using three paraphrases of one question. Say what must stay invariant, what may vary, what you will compare, and how to handle the results.

**Points:** 5

**Rubric (1 point each):**

1. Specifies that paraphrases keep every fact and requirement fixed, changing only wording.
2. Decides in advance what must remain invariant (facts, constraints, structure of the answer) and what may vary (tone, organization, phrasing).
3. Compares format validity, claim content and source support as separate dimensions.
4. Notes that different wording in an answer is not automatically a failure, and that a change in only one dimension is a different finding from a change in claims.
5. Notes that if the paraphrase results are used to revise the prompt, those paraphrases become development evidence and a new untouched check is needed.

**Source:** Computational Skepticism

## ES-ch02.31

An agent that can modify files returns a tool call {"tool": "delete_file", "path": "/data/reports"} which passes validation against the tool-call schema. Explain why passing the schema does not make the action acceptable, what controls should surround execution, and how the change from "text" to "action" alters what an evaluation must cover.

**Points:** 5

**Rubric (1 point each):**

1. Explains that schema validity establishes shape and types only and says nothing about whether the action is permitted or wise.
2. Names authorization controls enforced outside the model: permissions, allowlists, least privilege, scoped credentials.
3. Names human approval or confirmation for destructive or irreversible actions, and dry-run or reversible operations.
4. Explains that evaluation must now include the consequence of acting, such as tests of what could happen if the call is executed.
5. Notes that logs and an audit trail should record the requested and the executed action.

**Source:** From acceptable text to consequential action

## ES-ch02.32

You give an AI coding assistant a written contract and a list of tests, but not your own implementation, and ask it to write a validator. Describe how you would evaluate what it returns, including how you would find weaknesses in your own tests, and why you would write a baseline yourself first.

**Points:** 5

**Rubric (1 point each):**

1. Runs your own tests on the assistant's code rather than relying on its tests.
2. Treats a failing test as possibly revealing a gap in the contract or tests, not only a bug in the code.
3. Compares behaviors against your baseline, looking for boundaries it handled that you missed or ignored.
4. Asks for plausible-but-wrong implementations and checks whether the tests catch each one.
5. Explains that building a baseline first gives an independent reference and means you can explain and audit the logic.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch02.33

You must judge whether model answers are "supported" by supplied sources. Explain why the definition of supported, including what happens when the sources are insufficient, should be fixed before reading any answers, what outcomes the criterion should allow, and what can go wrong otherwise.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a criterion defined after seeing outputs can drift to favor the preferred outcome.
2. Defines supported precisely, for example each factual claim entailed by the cited passages.
3. Allows three outcomes: supported, contradicted, and cannot be determined, and does not count unknowns as passes.
4. Specifies handling for partial support and for answers that decline to answer.
5. Recommends independent annotators or a calibration check, and recording agreement.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.34

For each held-out question, a team writes in advance one sentence describing a response that would pass the structural validator and still fail the evidence criterion. Explain the purpose of this practice, give two example sentences for a question about a company's refund policy, and say what it means if a team cannot write them.

**Points:** 5

**Rubric (1 point each):**

1. Explains the purpose: forces thought about how the structural check could be satisfied while the content is wrong.
2. Explains that it must be written before seeing responses, otherwise it only describes the output.
3. Gives a valid example such as a correctly formed answer citing the refund document but stating a wrong time window.
4. Gives a second valid example such as a correctly formed answer that asserts a detail (payment method) not in the document.
5. Says that inability to write such sentences suggests the evidence criterion is not understood and the evaluation is not ready.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.35

About 4% of a service's JSON replies fail to parse. Inspection shows each failing reply stops partway through a list, and the API reports that generation ended because the maximum output length was reached. Diagnose the problem, propose remedies, and explain how you would instrument the pipeline so the cause is visible.

**Points:** 5

**Rubric (1 point each):**

1. Diagnoses truncation by the output-length limit rather than a failure to understand the format.
2. Notes that rewording the format instructions would not address this cause.
3. Proposes raising the output limit, requesting shorter answers, or restructuring the task into smaller outputs.
4. Proposes recording the stop reason with each response and classifying parse failures by cause.
5. Adds that failures should be reported by category, and that truncated replies must not be silently repaired and counted as passes.

**Source:** What each line of the validator promises

## ES-ch02.36

A pipeline validates each response and, on failure, resends the request with the error message appended, up to two more times. Out of 100 requests, 60 pass on the first attempt, 25 of the 40 failures pass on a retry, and 15 still fail. Compute the first-attempt and final pass rates, explain how each should be used, and discuss the costs and risks of retry loops.

**Points:** 5

**Rubric (1 point each):**

1. Computes the first-attempt rate of 60% and the final rate of 85%.
2. Explains the first-attempt rate describes how well the prompt elicits compliant output, while the final rate describes the system's delivered behavior.
3. Notes retries add cost and latency and may need a bounded number of attempts.
4. Notes that passing after a retry is still only a structural pass and says nothing about whether the content is supported.
5. Recommends reporting both rates and the failure categories, and examining the 15 persistent failures.

**Source:** What a pass rate leaves out

## ES-ch02.37

Compare three ways of getting structured output from a model: asking in the prompt, using a provider's JSON mode, and using schema-constrained decoding. Explain what each guarantees, what none of them guarantees, and why a validator and a content evaluation are still needed.

**Points:** 5

**Rubric (1 point each):**

1. Says prompting guarantees nothing; the model may ignore or misread the format request.
2. Says JSON mode guarantees syntactically valid JSON but not the required keys or types.
3. Says schema-constrained decoding guarantees conformance to the schema's structure and types.
4. Says none guarantees truth or support: a correctly typed field can hold a false claim, and rules comparing a field to external material fall outside a schema.
5. Explains that local validation covers rules and versions the provider does not enforce, and held-out evaluation measures content quality.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.38

A developer runs a prompt once at temperature 1.0 on fifty questions and reports 46 correct. Explain what is missing from that report, why a single run can mislead when comparing prompts, and how to design runs to separate prompt effects from sampling variation.

**Points:** 5

**Rubric (1 point each):**

1. Notes that sampling at nonzero temperature makes outputs vary from run to run.
2. Notes that a single run cannot reveal how much of a score is luck.
3. Proposes several repeated runs per prompt and reporting the spread, not just a mean.
4. Notes that temperature zero reduces but does not guarantee identical outputs on hosted systems.
5. Recommends recording sampling settings and model identifier and using enough cases that the difference exceeds the noise.

**Source:** A prompt revision is a hypothesis

## ES-ch02.39

You are assembling the evaluation cases for a document-grounded question-answering feature. Describe the kinds of cases you would include, how you would divide them, and what each kind tells you. Explain how the composition of the set changes what the pass rate means.

**Points:** 5

**Rubric (1 point each):**

1. Includes answerable questions of varied difficulty and phrasing drawn from realistic usage.
2. Includes unanswerable questions to test abstention instead of fabrication.
3. Includes adversarial or boundary cases (conflicting passages, near-miss wording, malformed inputs) designed to expose specific failures.
4. Divides cases into development and held-out sets before looking at outputs, with the split recorded.
5. Explains that the rate depends on the mix: easy or hand-picked cases inflate it, extreme cases deflate it, and only a representative sample supports claims about real usage.

**Source:** A prompt revision is a hypothesis

## ES-ch02.40

A grounded system answers 42 of 50 answerable questions correctly, wrongly abstains on 5 and answers 3 incorrectly. On 25 unanswerable questions it abstains on 20 and fabricates answers to 5. Compute the relevant rates and explain why a single overall figure is a poor summary for this system.

**Points:** 5

**Rubric (1 point each):**

1. Computes 84% accuracy on answerable questions (with 10% wrongful abstention and 6% wrong answers).
2. Computes 80% correct abstention (20% fabrication) on unanswerable questions.
3. Computes the overall correct behavior as 62 of 75, about 83%.
4. Explains that the overall figure hides the 20% fabrication rate on unanswerable questions, the failure users may care about most.
5. Recommends reporting separate rates for the categories (answerable accuracy, wrongful abstention, correct abstention, fabrication) and weighting by consequence.

**Source:** What a pass rate leaves out

## ES-ch02.41

A model answer states two claims: "Employees may carry over five vacation days" and "Unused days are paid out when an employee leaves." It cites one policy document, which supports the first claim and says nothing about payouts. Explain how to judge this answer, why a single correct citation is not enough, and how a team should decide whether partially supported answers pass.

**Points:** 5

**Rubric (1 point each):**

1. Decomposes the answer into separate claims and compares each with the cited passage.
2. Concludes the first claim is supported and the second is unsupported, so the answer is partly supported.
3. Explains that topical relevance or a valid citation does not establish entailment of every claim.
4. Explains that whether partial support passes is a policy decision that depends on the consumer and the cost of an unsupported claim.
5. Recommends recording the decision rule in advance and reporting counts of fully, partly, and unsupported answers.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.42

To make answers easier to audit, a team asks a model to include a short justification quoting the supporting text from the source. Explain what this makes possible, what it does not guarantee, and how you would treat the justification during evaluation. Address the question of whether a fluent rationale reveals how the model actually reached its answer.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a quoted span can be checked mechanically for verbatim presence in the source and gives a reviewer a place to look.
2. Explains that a genuine quote can still be irrelevant, out of context, or not entailing the claim.
3. Treats the justification as output to be evaluated, not as evidence.
4. States that a fluent rationale is generated text and is not a reliable account of the process that produced the answer.
5. Recommends requiring a reviewable claim, the referenced material and a short justification that can be checked against that material.

**Source:** A source identifier is an address, not an argument

## ES-ch02.43

A team's prompt-tuning log consists of entries such as "improved prompt" and "v3, better". Explain why this is inadequate, what a useful log entry contains, and what else should be preserved so another person can reconstruct and audit the experiment.

**Points:** 5

**Rubric (1 point each):**

1. Explains that vague entries do not say what changed, so effects cannot be attributed.
2. States that each entry names the specific instruction, example or boundary changed and why it was expected to matter.
3. Includes what the results on the development cases showed, including failures.
4. Preserves exact prompts, source material, model identifier, settings, date, and raw responses before any edits.
5. Keeps the baseline intact, separates constructed test strings from real model outputs, and records any assistance or repair as a transformation.

**Source:** Ship It: an experiment another person can audit

## ES-ch02.44

A prompt revision does not improve the pass rate on the development set, and some engineers want to leave it out of the report. Argue for or against omitting it, and explain what a well-documented negative result contributes.

**Points:** 5

**Rubric (1 point each):**

1. Argues that omitting it creates a biased picture of what was tried and what works.
2. Explains that a negative result tells others what not to repeat and narrows the hypothesis space.
3. Notes that failures show remaining risks and failure modes.
4. Explains that a complete trail supports credibility of the reported successes.
5. Recommends reporting the change, the hypothesis, the cases, the results and an honest scope for the conclusion.

**Source:** A prompt revision is a hypothesis

## ES-ch02.45

A grader marks a free-form summary correct only if it exactly equals a reference summary. Explain why this is a poor grader for summaries, in what cases exact matching is the right choice, and describe two better ways to score summaries along with how you would check them.

**Points:** 5

**Rubric (1 point each):**

1. Explains that many different wordings express the same content, so exact match scores correct paraphrases as errors.
2. Gives cases where exact match fits: classification labels, numbers, IDs, or any output with a single acceptable string.
3. Describes rubric-based scoring by humans against fixed criteria.
4. Describes model-graded scoring against a rubric, or semantic similarity methods, with their limits.
5. Describes checking graders against human labels and measuring agreement before trusting scores.

**Source:** A source identifier is an address, not an argument

## ES-ch02.46

Two reviewers independently label 50 answers as supported or contradicted against their sources. Reviewer 1 marks 35 supported and Reviewer 2 marks 34 supported. They both mark 30 supported, and both mark 11 contradicted. Compute the raw agreement and Cohen's kappa (observed agreement minus chance agreement, divided by one minus chance agreement). Interpret the result and explain what the team should do next.

**Points:** 5

**Rubric (1 point each):**

1. Computes observed agreement as (30 + 11) / 50 = 0.82.
2. Computes chance agreement as 0.70 x 0.68 + 0.30 x 0.32 = 0.572.
3. Computes kappa as (0.82 - 0.572) / (1 - 0.572), about 0.58.
4. Interprets this as moderate agreement, noting raw agreement overstates reliability because much agreement is expected by chance.
5. Recommends reviewing the 9 disagreements to find ambiguity in the criterion, sharpening it, or using adjudication, and then relabeling.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.47

A validator must ensure that a field called count is an integer, that a field called answer is a nonblank string, and that the reply is a single JSON object with no duplicate keys. Using Python's json.loads and isinstance, list at least four pitfalls an implementer should anticipate, and say how to handle each.

**Points:** 5

**Rubric (1 point each):**

1. Notes that bool is a subclass of int in Python, so true passes isinstance(value, int) unless bool is excluded explicitly.
2. Notes that json.loads accepts NaN and Infinity by default and that floats such as 3.0 are not integers.
3. Notes that duplicate keys are silently resolved (the last wins) and need object_pairs_hook to detect.
4. Notes that a parsed value may not be an object at all (list, string, number), so the shape check must precede indexing, and the validator should return a rejection rather than raise.
5. Notes whitespace-only strings pass a plain truthiness check unless stripped, and that each pitfall needs its own test.

**Source:** What each line of the validator promises

## ES-ch02.48

On 400 responses, a structural validator accepted 300 and rejected 100. A reviewer then judged content on all 400. Among the 300 accepted, 36 were unsupported by their sources. Among the 100 rejected, 15 would have been supported had the format been acceptable. Compute: the share of accepted responses that were supported, the total number of unsupported responses, the share of unsupported responses that the validator caught, and the share of rejections that were of unsupported content. Say what these numbers imply about the validator's usefulness.

**Points:** 5

**Rubric (1 point each):**

1. Computes 264 of 300 accepted responses supported, or 88%.
2. Computes 36 + 85 = 121 unsupported responses in total.
3. Computes that the validator rejected 85 of the 121 unsupported responses, about 70%.
4. Computes that 85 of the 100 rejections (85%) were of unsupported content, and 36 of 121 unsupported responses (about 30%) passed.
5. Concludes the validator provides real but incomplete protection: it filters most bad content incidentally, yet cannot be treated as a content check, and it also rejects some good content.

**Source:** Work through the three-response experiment

## ES-ch02.49

A team cannot afford to review every accepted answer by hand, so it will review a random sample. It expects roughly 10% of accepted answers to be unsupported and wants to estimate the true rate to within plus or minus 3 percentage points at about 95% confidence. Using n = z^2 p(1-p) / e^2 with z = 1.96, compute the sample size, explain what each term means, and discuss how the plan changes if the team samples only the answers that look doubtful.

**Points:** 5

**Rubric (1 point each):**

1. Computes n = 1.96^2 x 0.1 x 0.9 / 0.03^2, about 385.
2. Explains p as the expected proportion, e as the margin of error, and z as the confidence multiplier.
3. Notes that with p near 0.5 the required sample is larger (about 1,068 for +-3 points) and that the formula assumes random sampling.
4. Explains that sampling only doubtful answers gives a biased estimate of the overall rate, though it may be useful for finding failure modes.
5. Notes that a smaller sample gives a wider interval, so results must be reported with their uncertainty and the sampling method.

**Source:** What a pass rate leaves out

## ES-ch02.50

A team optimizes its prompt for two weeks until a format validator accepts all 30 of its test cases, and then reports that output quality is excellent. Explain what is wrong with the inference, using the ideas of overfitting and of a metric becoming a target. Propose how to obtain a trustworthy estimate.

**Points:** 5

**Rubric (1 point each):**

1. Explains that cases used for iteration will look good by construction, so 100% on them is not evidence for new inputs.
2. Explains that optimizing against a fixed validator can satisfy the validator without satisfying the underlying goal.
3. States the principle that a measure that becomes a target ceases to be a good measure.
4. Notes that the validator says nothing about content support or relevance.
5. Proposes evaluating on untouched cases, adding content-level checks, and reporting the estimate with its scope and uncertainty.

**Source:** A prompt revision is a hypothesis

## ES-ch02.51

A vendor announces that a newer model version is "better" than the previous one for your document question-answering task. Describe how you would test this claim for your own use, including what you hold fixed, which evidence criterion you use, and how you present the result.

**Points:** 5

**Rubric (1 point each):**

1. Runs both versions on the same cases, prompts, source materials and settings.
2. Fixes the evidence criterion and the split between development and held-out cases before looking at outputs.
3. Measures format compliance and source support separately, plus abstention behavior on unanswerable questions.
4. Repeats runs or uses enough cases to distinguish a difference from sampling variation.
5. Records model identifiers and dates, reports failures by category, and limits the conclusion to the task and conditions tested.

**Source:** A prompt revision is a hypothesis

## ES-ch02.52

A prompt passes all 30 of 30 test cases. A manager concludes that the failure rate is zero. Explain why zero failures in 30 trials does not mean a failure rate of zero, compute an approximate 95% upper bound on the failure rate using the rule of three (3 divided by n), and discuss what else the manager needs before accepting reliability.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a finite sample can show no failures even if a nonzero failure rate exists.
2. Computes the rule-of-three upper bound as 3/30 = 10%.
3. States that the exact one-sided 95% bound is about 9.5%, so a true failure rate near 10% is still consistent with the data.
4. Notes that the cases must also be representative, and that passing a structural check says nothing about content.
5. Recommends more cases, content-level review, and reporting the bound rather than "zero".

**Source:** What a pass rate leaves out

## ES-ch02.53

A workflow chains ten model steps, each of which succeeds independently with probability 0.98. Compute the probability that all ten succeed, and compare it with a per-step probability of 0.95. Explain why per-step pass rates can mislead about end-to-end reliability, and name the assumption behind your calculation and how it could fail.

**Points:** 5

**Rubric (1 point each):**

1. Computes 0.98 to the tenth power, about 0.82.
2. Computes 0.95 to the tenth power, about 0.60.
3. Explains that failure probabilities compound across steps, so apparently high step reliability yields modest end-to-end reliability.
4. States the independence assumption and how correlated failures or dependent steps would change the result.
5. Recommends measuring end-to-end success directly, and adding checkpoints, validation between steps or retries to improve it.

**Source:** What a pass rate leaves out

## ES-ch02.54

A contract asks the model to return a self-reported confidence between 0 and 1 with each answer. Explain what a validator can and cannot check about this field, how you would test whether the numbers are meaningful, and how you would decide whether to use them in a downstream decision.

**Points:** 5

**Rubric (1 point each):**

1. States the validator can check type and range (a number between 0 and 1) but not whether the number is meaningful.
2. Defines calibration: among answers stated with confidence near c, a fraction near c should be correct.
3. Describes a test: bin the answers by stated confidence and compare each bin's stated confidence with its observed accuracy using labeled data.
4. Notes that language models' self-reports can be overconfident and may not generalize across tasks.
5. Says the field should not be used as a substitute for independent verification unless calibration has been demonstrated on held-out data.

**Source:** A source identifier is an address, not an argument

## ES-ch02.55

Two teams build checks for model answers that will be shown to customers. One answers questions about movie trivia and the other about drug interactions. Explain how the stakes should shape the acceptance rule, the checks, and the amount of human review in each case, and who should decide.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the cost of a wrongly accepted answer drives how much independent verification is justified.
2. Describes stricter acceptance (every claim supported, abstention encouraged) and more human review for the drug interaction case.
3. Describes lighter acceptance and sampling-based review for trivia, accepting some error.
4. Notes that acceptable risk is a judgment about consequences, not something a validator can compute.
5. Says the decision belongs to those who bear the consequences, recorded before testing, rather than chosen to make results look good.

**Source:** The driver's seat: what counts as acceptable

## ES-ch02.56

A team constructs a single response that is well formed, cites a supplied document identifier, and contradicts that document. Explain what this single example demonstrates and what it does not, why it is more informative than a general warning about hallucination, and why it does not show the validator is broken.

**Points:** 5

**Rubric (1 point each):**

1. Explains that one counterexample refutes the claim that passing the validator implies the answer is supported.
2. States that it says nothing about how often such failures occur.
3. Explains that it identifies precisely which check is absent, so the pass can be traced to rules rather than speculation about model internals.
4. Explains that the validator does its stated job and the error lies in reading its pass as more than it covers.
5. Recommends keeping the structural check, naming its scope and adding a content-level evaluation.

**Source:** A source identifier is an address, not an argument

## ES-ch02.57

You run an experiment that includes some hand-written test strings and some real responses from a model. Explain how to label and keep them apart in your records, why the distinction matters for the claims you can make, and what must be preserved about the real responses.

**Points:** 5

**Rubric (1 point each):**

1. Explains that hand-written strings demonstrate validator behavior but are not observations of a model.
2. Explains that rates over constructed cases reflect how whoever built the set composed it and cannot be quoted as model behavior.
3. Explains that recorded model outputs support claims limited to their recorded conditions.
4. Requires preserving the exact prompts, source materials, model identifier, settings, and date for real responses.
5. Requires keeping both kinds in clearly separate files or columns so a reader cannot confuse them.

**Source:** Work through the three-response experiment

## ES-ch02.58

A validator is tested on three prepared inputs: (1) the text `not json`; (2) `{"answer": "x", "sources": ["missing"]}` where only "doc1" is a supplied identifier; (3) `{"answer": "Delivery takes 10 days", "sources": ["doc1"]}` where doc1 says "Delivery takes 3 days." The validator checks parsing, exact keys, types, a nonblank answer, a nonempty list and identifier membership. Draw up a table with, for each input, the validator's decision, the obligation that failed or passed, and a content-support review. Then say how the report should present the third row.

**Points:** 5

**Rubric (1 point each):**

1. Input 1: rejected at parsing, with no later rule applied; the support review is "cannot be reviewed" because there is no claim.
2. Input 2: rejected at identifier membership after parsing and shape checks succeed; support review is "cannot be reviewed" because the address resolves to nothing.
3. Input 3: accepted because every implemented rule is satisfied.
4. Input 3 support review: contradicted by doc1, which states 3 days.
5. Presents the third row as format accepted and content contradicted, an expected result rather than an inconsistency, and does not collapse the two columns into one score.

**Source:** Work through the three-response experiment

## ES-ch02.59

A contract says a response must be a JSON object with an answer string, a list of source identifiers, and no other keys. List the separate obligations the validator imposes, in the order they should be checked, and for each give an input that violates it and the reason the order matters.

**Points:** 5

**Rubric (1 point each):**

1. Parsing: input such as an unclosed brace is rejected before any field rule applies.
2. Shape: a parsed list or string is not an object and must be rejected before key access.
3. Keys: a missing key or extra key fails the exact-key rule.
4. Field types and content: a non-string answer, a blank answer, or a non-list sources value fails the field rules.
5. Source rules: an empty list or an identifier not in the supplied set fails, and the order matters because later rules assume earlier ones hold (indexing a non-object would raise).

**Source:** What each line of the validator promises

## ES-ch02.60

You are asked to prepare, before any prompt is written, an acceptance plan for a feature in which a model answers customer questions from a product manual and a program displays the result. Write out the items the plan should contain and say why each is needed before prompting begins.

**Points:** 5

**Rubric (1 point each):**

1. Names the consuming program and what it needs, with the exact output object it accepts and the inputs it refuses.
2. Defines the evaluation set, including answerable and unanswerable questions, split into development and held-out portions and dated before results.
3. Defines the evidence criterion for support, with outcomes supported, contradicted, and cannot be determined, fixed in advance.
4. Lists wrong implementations or wrong outputs the tests must catch, including a well-formed but unsupported answer that structural tests cannot catch.
5. States a pass condition for the plan itself and the claims the eventual experiment may and may not make.

**Source:** The gate: write the contract for the consumer first

## ES-ch02.61

A model is asked to answer from a document. In one test the same question is asked twice, with wording that differs only in tone. In answer A the facts match the document, and in answer B one number is changed. Both are well formed and cite the right document. Explain what an evaluation of robustness to rewording should conclude about each, what dimension changed in each case, and what it should not conclude.

**Points:** 5

**Rubric (1 point each):**

1. Says robustness testing asks what should stay the same when wording changes but the task does not.
2. Treats answer A as acceptable variation: tone or organization changed while facts and obligations stayed fixed.
3. Treats answer B as a failure: an altered fact violates the invariant even though the format passes.
4. Says the dimensions (format, content, support) should be compared separately, so that a change in B is visible as a content change.
5. Does not conclude broad claims about model understanding from a few paraphrases, and treats paraphrases used to revise the prompt as development evidence.

**Source:** Computational Skepticism
