# Chapter 2: Prompt contracts and evaluation

## MA-ch02.1

A question-answering system must answer only from supplied documents. One supplied document, with identifier doc-A, reads: "The warehouse opens at 9:00." The consumer's validator checks only that the response is a JSON object with the keys answer and cites, that answer is a nonblank string, and that every entry in cites is a supplied document identifier. The model returns {"answer": "The warehouse opens at 7:00.", "cites": ["doc-A"]}. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The response is faithful to the document it cites.
- [ ] B. A check that compares the claim with the text of doc-A would reject this response.
- [ ] C. Citing an identifier that exists shows the cited document supports the claim.
- [ ] D. The response passes the validator.
- [ ] E. Listing the allowed document identifiers as an enumeration inside a JSON schema would reject this response.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The document says 9:00 and the answer says 7:00, so the answer contradicts its source.
- B: Only a content-level comparison of claim against source text can detect the contradiction.
- C: An identifier is an address; whether the text at that address supports the claim is a separate question.
- D: The object has the right keys, a nonblank answer, and a cited identifier that was supplied, so every implemented rule is satisfied.
- E: The identifier doc-A is on the allowed list, so an identifier enumeration accepts the response.

**Source:** A source identifier is an address, not an argument

## MA-ch02.2

A prompt tells a model: "Return only a JSON object with the keys name and age." The calling code runs json.loads on whatever comes back and passes the result to a function that reads both keys. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The instruction is enforced by the runtime once the model has read it, so replies conform.
- [ ] B. A reply that parses as JSON will contain both keys.
- [ ] C. Strengthening the wording of the instruction ("you MUST comply") makes the post-response check unnecessary.
- [ ] D. Decoding constrained to a JSON schema also makes the value of age true.
- [ ] E. The model can ignore or misread the instruction, so the instruction alone does not guarantee conforming output.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: A prompt is text that conditions a sampler; nothing in the runtime forces the reply to follow it.
- B: Valid JSON can be a list, a string, or an object with other keys; parsing says nothing about required keys.
- C: Emphatic wording lowers but does not remove the failure rate, and only a check detects the failures that remain.
- D: Constrained decoding enforces structure, but the truth of a value is beyond what a schema can enforce.
- E: A prompt is a request to a probabilistic generator and can be disobeyed or misunderstood.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.3

A downstream function unpacks exactly two fields, answer and sources, from each model response and raises an exception on any other field. Validator X requires exactly those two keys. Validator Y requires those two keys and ignores any extra keys. A model returns an object with answer, sources, and a plausible-looking extra key named confidence. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The better of the two validators can be chosen without knowing what the consumer does with the object.
- [ ] B. For a consumer that crashes on unexpected fields, Validator Y is the safer choice.
- [ ] C. Validator Y accepts the response.
- [ ] D. Validator X rejects the response.
- [ ] E. Rejecting a response because of a reasonable-looking extra field only shows the validator is badly designed.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Strictness versus tolerance is a trade-off whose right answer depends on the downstream job.
- B: Y would pass the extra field through and the consumer would crash; X turns the surprise into a visible rejection.
- C: Y checks only that the required keys exist and is silent about additions.
- D: The key set is not exactly the two required keys, so X rejects.
- E: For a consumer that crashes on unexpected fields, rejecting at the boundary is the protective behavior.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.4

Two teams build a prompt that extracts invoice totals for a billing program. Team 1 writes down the required output object, the test cases, and what counts as correct before writing any prompt. Team 2 adjusts the prompt until the outputs look right to them, then writes a checker that accepts what the final prompt produces. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Team 1 should keep its criteria fixed even when outputs show them to be incomplete.
- [ ] B. Team 2's checker risks encoding whatever the prompt happened to produce rather than what the billing program needs.
- [ ] C. Team 2's pass rate on its own checker is strong evidence that the prompt meets the consumer's needs.
- [ ] D. Team 1's acceptance criterion exists independently of any particular output.
- [ ] E. Writing criteria first removes the need for a separate held-out set.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Criteria can be revised when a gap appears, provided the change is recorded as a new version.
- B: A criterion written after tuning is a description of the outputs, so passing it is close to circular.
- C: Agreement with a checker built from the outputs measures consistency with those outputs, not fitness for the consumer.
- D: A criterion fixed beforehand can fail an output; one fitted afterward cannot.
- E: Fixing criteria early addresses a different problem from overfitting to the cases used while iterating.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.5

A developer asks a coding assistant to implement a validator from one line: "the output must have an answer and a list of sources." The line does not say whether extra keys are allowed, whether the list may be empty, or what to do with a whitespace-only answer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tests written in advance for these edge cases would reveal which interpretation was chosen.
- [ ] B. Whatever interpretation it picks becomes the validator's behavior even though no one decided it.
- [ ] C. Passing the developer's one happy-path example shows the unspecified cases are handled correctly.
- [ ] D. The assistant may silently pick an interpretation for each unspecified case.
- [ ] E. The requester removes the ambiguity by stating the unspecified cases or by writing tests for them.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Edge-case tests turn silent choices into observable pass or fail results.
- B: Unspecified behavior is still behavior, and it will be exercised in production.
- C: A happy-path example exercises none of the unspecified cases.
- D: Generators fill gaps with something plausible rather than reliably flagging them.
- E: Only the requester knows what the consumer needs, so closing the gaps in the specification is theirs to do.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.6

A grounded question-answering contract requires every response to have a nonblank answer string and a nonempty list of supplied source identifiers, and nothing else. A user asks a question that the supplied sources do not address. The model replies {"answer": "The sources do not say.", "sources": ["doc-2"]}, where doc-2 is a supplied identifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The contract already gives the consumer a distinct signal whenever the system abstains.
- [ ] B. The validator cannot tell this honest non-answer apart from a factual assertion.
- [ ] C. The response is invalid because doc-2 does not contain the answer.
- [ ] D. Adding the line "be accurate" to the prompt supplies a refusal state in the output.
- [ ] E. Adding an explicit status field to represent abstention would require changing the validator and its tests, a new version of the contract.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: With no status field, an abstention and an assertion look identical to the consumer.
- B: The validator sees a nonblank string and a known identifier; it has no notion of what the sentence means.
- C: Validity here is defined by the structural rules, which this response satisfies; support is a separate judgment.
- D: An instruction to be accurate adds no output field, so the consumer still cannot see a refusal.
- E: A closed, exact-key contract rejects a new field until the contract itself is changed and retested.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.7

Before any prompt is written for a feature whose output a program will consume, a team prepares a written acceptance plan. Check each statement that is true about what belongs in such a plan. Each statement is worth 1 point (5 points total).

- [ ] A. It should name wrong implementations or outputs the tests are expected to catch, including a well-formed but unsupported answer that structural tests cannot catch.
- [ ] B. It defines in advance how a response will be judged supported by evidence, including a category for answers that cannot be judged.
- [ ] C. It names the program that consumes the output and what that program needs from it.
- [ ] D. It can be left empty until the first outputs arrive, since the format cannot be known earlier.
- [ ] E. It lists test cases and separates those used while iterating from those held back.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Listing the failures to be caught keeps the plan honest about which defects tests cover and which need content review.
- B: A pre-fixed evidence criterion, with an unknown outcome, prevents redefining success after seeing results.
- C: The consumer's needs are the only criterion that exists before any output does.
- D: The required output shape comes from the consumer, not from observing the model.
- E: A split fixed beforehand is what allows later measurement on untouched cases.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.8

A strict consumer expects each raw response to be a JSON document. A model's reply is a Markdown code fence containing {"answer": "42", "sources": ["a"]}, introduced by one sentence of prose. A teammate deletes the sentence and the fence by hand and scores the cleaned string as a pass. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Whether the consumer should tolerate fenced replies is a contract decision to make before measuring.
- [ ] B. Scoring only the cleaned version measures something different from what the model produced.
- [ ] C. Keeping both the original and the cleaned text in the record lets a reader see what the model emitted.
- [ ] D. Cleaning the reply is harmless to the measurement because the JSON inside is identical.
- [ ] E. Running json.loads on the original reply raises an error.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Tolerance changes what counts as acceptable, so it must be decided as part of the acceptance rule.
- B: The cleaned string reflects a human repair, so its pass says nothing about unrepaired model output.
- C: Preserving the original keeps the observation distinct from the transformation applied to it.
- D: The part that was removed is exactly what made the consumer's strict parse fail.
- E: Prose and backticks are not valid JSON, so strict parsing fails.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.9

A validator checks sources with the Python expression mode(s in allowed for s in sources), where allowed = {"a", "b"} and mode is either all or any. It is called with sources = ["a", "zzz"] and, separately, with sources = []. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With mode = all, the input ["a", "zzz"] is rejected.
- [ ] B. With mode = all, the input [] is accepted.
- [ ] C. Using all makes a separate nonempty-list check unnecessary.
- [ ] D. With mode = any, the input [] is accepted.
- [ ] E. With mode = any, the input ["a", "zzz"] is accepted.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: all requires every entry to be allowed, and "zzz" is not.
- B: all over an empty sequence is vacuously True, so an empty list passes unless something else rejects it.
- C: Because all is True on an empty list, emptiness has to be rejected by a check of its own.
- D: any over an empty sequence is False, so an empty list is rejected by any.
- E: any returns True when at least one entry is allowed, and "a" is allowed.

**Source:** What each line of the validator promises

## MA-ch02.10

A validator enforces the contract "a JSON object with exactly the keys title (a nonblank string) and tags (a list of strings)". It receives three inputs. Input 1 is {"title": "Report", "tags": ["x"] with the closing brace missing. Input 2 is ["title", "tags"]. Input 3 is {"title": 7, "tags": ["x"]}. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Input 2 would be accepted by a check that only requires json.loads to succeed.
- [ ] B. Input 1 fails at parsing, so no field rule is applied to it.
- [ ] C. Input 3 parses to an object with the right keys and fails on a field type.
- [ ] D. The three failures are best described identically as "bad formatting" for the purpose of diagnosis.
- [ ] E. Input 2 parses successfully but is the wrong kind of value for the contract.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A parse-only check accepts any syntactically valid JSON value, including a list.
- B: A syntax error stops processing at the parser, before any structural or field rule is reached.
- C: The keys match, but title must be a string and 7 is an integer.
- D: Parser, shape and type failures point to different repairs and should be distinguished.
- E: A list is valid JSON but not an object, so the shape rule rejects it.

**Source:** What each line of the validator promises

## MA-ch02.11

A validator treats a string field as nonblank when bool(value.strip()) is True in Python. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Without the strip() call, the value "   " would still be rejected.
- [ ] B. The value "n/a" fails the check because it is a placeholder.
- [ ] C. The value "   " (three spaces) fails the check.
- [ ] D. Passing the check shows the answer is relevant to the question asked.
- [ ] E. The value "0" passes the check.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A string of spaces is a nonempty string and is truthy, so without strip() it would pass.
- B: Any visible characters pass; the check does not recognize placeholders.
- C: Stripping leaves an empty string, which is falsy.
- D: Nonblank is a property of the characters, not of relevance, correctness or completeness.
- E: The string "0" is nonempty after stripping, and nonempty strings are truthy even when they look like zero.

**Source:** What each line of the validator promises

## MA-ch02.12

A validator accepts a response only if it parses as a JSON object with exactly the keys answer and sources; answer is a nonblank string; sources is a nonempty list; and every entry of sources is a string in the allowed set {"a", "b"}. The test suite has five tests: (1) a valid object with sources ["a"]; (2) text that is not JSON; (3) answer equal to the integer 1; (4) sources equal to ["zzz"]; (5) an object with an additional key. Three mutated copies of the validator are made. M1 replaces "every entry" with "at least one entry". M2 deletes the nonblank part of the answer check but keeps the string-type check. M3 deletes the nonempty-list check but keeps the every-entry check. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. M1 still passes all five tests.
- [ ] B. M2 still passes all five tests.
- [ ] C. Adding a test with sources ["a", "zzz"] would distinguish M1 from the original.
- [ ] D. Passing all five tests shows the original validator implements the specification.
- [ ] E. M3 still passes all five tests.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Test 4 has a single unknown entry, which "at least one" also rejects, so the mutant is not exposed.
- B: No test supplies a blank answer, so deleting that check changes no test outcome.
- C: The mixed list is accepted by "at least one" and rejected by "every entry", so the outcomes differ.
- D: Tests defend only the behaviors they exercise; three lines of the specification are undefended here.
- E: No test supplies an empty list, so the deletion goes unnoticed.

**Source:** What each line of the validator promises

## MA-ch02.13

A validator returns only True or False. A maintainer wants to understand why 30 of 200 responses failed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A Boolean alone does not tell the maintainer which rule rejected a response.
- [ ] B. Adding reason codes means the validator now accepts a different set of responses.
- [ ] C. A Boolean is easy to aggregate into a pass rate.
- [ ] D. Two failures that both count as zero in the pass rate call for the same repair, since the rate treats them alike.
- [ ] E. Returning a reason such as parse error, key mismatch, wrong type or unknown source would let failures be tallied by category.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The Boolean collapses every rejection into one symbol, discarding the reason.
- B: Labeling the reason for a rejection can leave the accept-or-reject decision untouched.
- C: Summing True values and dividing by the count gives a rate directly.
- D: A non-JSON reply and a single bad identifier both score zero but are repaired differently.
- E: A categorical reason preserves information a pass rate throws away.

**Source:** What each line of the validator promises

## MA-ch02.14

A validator must ensure that the field count is an integer, and implements this with isinstance(value, int) after parsing with json.loads. In Python, bool is a subclass of int. The inputs are {"count": true}, {"count": 3}, {"count": 3.0} and {"count": "3"}. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The input with "3" passes the isinstance check.
- [ ] B. Adding "and not isinstance(value, bool)" would reject the input with true.
- [ ] C. The input with 3 passes the isinstance check.
- [ ] D. The input with true passes the isinstance check.
- [ ] E. The input with 3.0 passes the isinstance check.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A quoted number parses to a string.
- B: Excluding bool explicitly rejects True and False while still accepting ordinary integers.
- C: JSON 3 parses to the integer 3.
- D: A JSON true parses to Python True, which is an instance of int.
- E: JSON 3.0 parses to a float, which is not an instance of int.

**Source:** What each line of the validator promises

## MA-ch02.15

A validator relies on Python's json.loads with default settings to parse replies. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The bare token NaN is rejected as invalid.
- [ ] B. For an object with a duplicated key, the later value silently replaces the earlier one.
- [ ] C. A reply consisting only of the number 7 parses successfully, so a separate shape check is still needed.
- [ ] D. A reply with a trailing comma inside an object raises a JSONDecodeError.
- [ ] E. A string quoted with single quotes is accepted as a JSON string.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Python's parser accepts NaN and Infinity by default, an extension beyond the JSON standard.
- B: Python keeps the last occurrence of a duplicated key without any warning.
- C: Any JSON value parses, including a bare number, so shape must be checked after parsing.
- D: Trailing commas are not permitted in JSON, and the standard parser raises an error.
- E: JSON strings must use double quotes; single quotes raise an error.

**Source:** What each line of the validator promises

## MA-ch02.16

A service asks a model for a JSON object with a long free-text answer field. About 6% of replies fail to parse. Inspection shows that each failing reply ends in the middle of a string, and the API response reports that generation stopped because the maximum output length was reached. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Rewording the schema description in the prompt is the only possible remedy.
- [ ] B. Truncation by the output limit is a plausible explanation for these parse failures.
- [ ] C. Recording the stop reason would let the pipeline separate truncation from other kinds of format failure.
- [ ] D. Raising the output limit or asking for shorter answers could reduce this failure.
- [ ] E. These failures show the model does not understand JSON.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The cause is length, not wording, so changing the schema description may not help at all.
- B: A reply cut off mid-string cannot be valid JSON, and the reported stop reason matches.
- C: The stop reason distinguishes an incomplete reply from a complete but malformed one.
- D: Giving the answer room, or shortening it, addresses the mechanism that is cutting the reply.
- E: The same model produces valid JSON on shorter replies; the failure is mechanical, not conceptual.

**Source:** What each line of the validator promises

## MA-ch02.17

A pipeline validates each response and, on failure, resends the request with the validator's error message appended, up to two further attempts. Over 100 requests, 70 pass on the first attempt, 20 of the 30 failures pass on a retry, and 10 still fail after the retries. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reporting only the final 90% fairly describes how reliably the model follows the contract in a single try.
- [ ] B. Retries add cost and latency.
- [ ] C. The final pass rate after retries is 80%.
- [ ] D. A response that passes after a retry is thereby shown to be supported by its sources.
- [ ] E. The first-attempt pass rate is 70%.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The final rate hides that 30% of single attempts failed; first-pass and final rates answer different questions.
- B: Each retry is another model call, so spend and wait time rise.
- C: 70 first-attempt passes plus 20 recovered by retries gives 90 of 100, not 80.
- D: The validator checks structure; passing after a retry says nothing about whether the content is supported.
- E: 70 of 100 requests passed without any retry.

**Source:** What a pass rate leaves out

## MA-ch02.18

A provider offers a "JSON mode", in which output is guaranteed to be syntactically valid JSON, and a schema-constrained mode, in which output is guaranteed to conform to a supplied JSON schema. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A rule such as "the quoted span must appear in the supplied source text" can be expressed directly in a JSON schema.
- [ ] B. Schema-constrained output cannot contain a wrong value in a correctly typed field.
- [ ] C. Output that is syntactically valid JSON need not contain the keys the consumer requires.
- [ ] D. With schema-constrained output, the cited sources can be assumed to support the claims.
- [ ] E. Using schema-constrained output makes held-out evaluation of answer quality unnecessary.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A schema validates one document in isolation and cannot reference external source text.
- B: A schema constrains types and structure; a correctly typed field can still hold a false value.
- C: Valid syntax means the text parses; any object, list or scalar qualifies.
- D: Support is a relation between a claim and external text, which a schema does not model.
- E: Structure and quality are different properties, and quality still has to be measured on cases the prompt was not tuned on.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.19

A response states two claims in one answer: (1) "The refund window is 30 days" and (2) "Refunds are paid in cash." It cites one supplied document, which reads: "Refunds can be requested within 30 days of purchase." The document says nothing about how refunds are paid. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Judging the answer requires comparing each claim with the cited text separately.
- [ ] B. Because the citation is valid for claim 1, the whole answer counts as supported.
- [ ] C. Claim 2 is not supported by the cited document.
- [ ] D. Because the document is about refunds, claim 2 is supported by implication.
- [ ] E. Claim 1 is supported by the cited document.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A multi-claim answer needs a claim-by-claim comparison, because support can be partial.
- B: One correct citation cannot stand in for the support of every claim in the answer.
- C: Nothing in the document mentions cash or any payment method.
- D: Topical relevance is not entailment; a document about refunds does not support an unstated payment method.
- E: The document states the 30-day window directly.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.20

To check a model's answer, a team sends the same model the answer and the source and asks "Is this answer supported by the source?" The model replies "Yes." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reply is new model output that itself needs evaluation.
- [ ] B. A model asked to review its own answer is as independent as a second reviewer would be.
- [ ] C. Only the model that wrote an answer is qualified to judge it, since only it knows what it meant.
- [ ] D. Because the model said yes, the error rate of this check is known to be zero.
- [ ] E. A check built on a different mechanism, such as matching a quoted span against the source, a human reviewer, or a separately validated classifier, fails differently from the generator.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A verdict from a model is another generation, not ground truth.
- B: The same model shares its training and blind spots, so its review is not a second, independent opinion.
- C: A judge is trusted because its agreement with a standard has been measured, and independence comes from a different failure profile, not from authorship.
- D: A single "yes" gives no information about how often such judgments are wrong.
- E: Independence comes from a different failure profile, which is what makes a check informative.

**Source:** A source identifier is an address, not an argument

## MA-ch02.21

Evaluation methods are commonly grouped as code-graded (a program checks the output), model-graded (another model scores the output) and human-graded. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Model-graded evaluation can scale to open-ended outputs, but its agreement with human judgments needs to be checked.
- [ ] B. Checking that a response parses as JSON with the required keys is naturally code-graded.
- [ ] C. Exact string comparison with a reference is a good grader for free-form summaries.
- [ ] D. Human grading is the cheapest and fastest of the three.
- [ ] E. Different methods are often combined, each used on a different aspect of the same output.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A model judge handles outputs no program can score, but it must be calibrated against human labels.
- B: Structure and key presence are deterministic properties a program can test.
- C: Many different wordings are equally good summaries, so exact match scores correct paraphrases as wrong.
- D: Human review is typically the slowest and most expensive method.
- E: Cheap programmatic checks for form, plus judged or human review for content, is a standard layering.

**Source:** A source identifier is an address, not an argument

## MA-ch02.22

A team uses a language model to choose the better of two candidate answers. Check each statement that is true about known risks of such judges. Each statement is worth 1 point (5 points total).

- [ ] A. Judge verdicts can vary from run to run when sampling is used, so repeated judging may be needed.
- [ ] B. Once the judge's scores look plausible, comparing them with human labels is unnecessary.
- [ ] C. A judge can favor whichever answer is shown first, so swapping the order and checking consistency is a useful control.
- [ ] D. A judge can favor longer answers independent of their quality.
- [ ] E. A judge can rate text from its own model family more favorably.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Sampled judgments are not deterministic, so their variation should be measured.
- B: Plausible-looking scores say nothing about agreement with the standard you care about, which has to be measured.
- C: Position bias is documented, and order swapping exposes it.
- D: Verbosity bias is a documented tendency of model judges.
- E: Self-preference has been observed and is a reason to use a judge from a different family or to calibrate.

**Source:** A source identifier is an address, not an argument

## MA-ch02.23

A team has 100 labelled questions and splits them into a development set and a held-out set. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Development cases may be inspected and used to revise the prompt.
- [ ] B. A held-out score stays an unbiased estimate no matter how many prompt variants were chosen by comparing their held-out scores.
- [ ] C. A held-out case is still held out after its failure has been used to decide a prompt change.
- [ ] D. If the held-out set has been used for tuning, relabeling it as untouched restores its status.
- [ ] E. Held-out cases should be shown to the prompt author early so they know what to optimize for.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The point of a development set is to learn from it.
- B: Selecting among many variants using the held-out score biases it upward, which is a form of overfitting.
- C: Once a case has influenced a decision, it has become development evidence.
- D: Status depends on what influenced decisions, not on a label; only fresh data restores an untouched check.
- E: Seeing the cases early turns them into development data; they should stay unseen until the revision is frozen.

**Source:** A prompt revision is a hypothesis

## MA-ch02.24

A team adds three example input-output pairs to a prompt (few-shot prompting). Afterward they notice that one of the examples is also one of the 10 questions in their held-out set. The revised prompt scores 10/10 on the held-out set and the baseline prompt scores 7/10. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 10/10 result cannot be taken as clean evidence that the revision helps.
- [ ] B. Near-paraphrases of held-out questions placed in the prompt can also contaminate the held-out measurement.
- [ ] C. The three-question gap shows that the examples improved the model's format discipline.
- [ ] D. Removing the leaked item and rescoring both prompts on the remaining 9 questions gives a cleaner, though smaller, comparison.
- [ ] E. The prompt now contains the answer to one held-out question, so that item no longer measures generalization.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Part of the gain may come from the leaked item, and the size of that part is unknown.
- B: Overlap in content, not only identical items, can leak answers and inflate the score.
- C: Nothing in the data attributes the gap to format discipline rather than to the leaked item or to noise.
- D: Dropping contaminated items and rescoring both versions on the same remaining set restores a like-for-like comparison.
- E: An item whose answer is in the prompt tests recall of the prompt, not skill on unseen cases.

**Source:** A prompt revision is a hypothesis

## MA-ch02.25

Prompt v1 scored 5/10 on a question set and prompt v2 scored 8/10. Between the two runs, the developer added two examples, switched to a newer model version, rewrote the task description, and replaced several questions with easier ones. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A controlled comparison changes one identifiable feature and holds the rest fixed.
- [ ] B. Because the score rose, the added examples must be the cause.
- [ ] C. Changing the question set means 5/10 and 8/10 are not a like-for-like comparison.
- [ ] D. A written log of each change helps a later reader see what could explain the difference.
- [ ] E. It is not possible to tell which change produced the difference.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Isolating one change is what lets an observed difference be attributed to it.
- B: A rise accompanied by several simultaneous changes cannot be pinned on any one.
- C: Easier questions raise scores on their own, independent of the prompt.
- D: A change log makes the candidate explanations visible and auditable.
- E: Four changes overlap, so effects are confounded.

**Source:** A prompt revision is a hypothesis

## MA-ch02.26

Prompt A scores 7/10 and prompt B scores 8/10 on the same ten questions. Treat each question as an independent pass-or-fail trial. For a true pass probability of 0.75, the standard error of a proportion measured over n trials is sqrt(0.75 x 0.25 / n), which is about 0.137 for n = 10 and about 0.043 for n = 100. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The data show that B is reliably better than A.
- [ ] B. Evaluating on 100 questions at the same rate would shrink the standard error to about 1.4 percentage points.
- [ ] C. With ten questions, the standard error is roughly 14 percentage points.
- [ ] D. Evaluating more questions would not change the standard error, which depends only on the pass probability.
- [ ] E. The one-question difference (10 percentage points) is larger than the standard error.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A difference smaller than the sampling noise cannot establish which prompt is better.
- B: At n = 100 the standard error is about 4.3 points, a threefold reduction and not tenfold.
- C: 0.137 is about 14 points.
- D: Standard error falls with the square root of the number of trials.
- E: Ten points is smaller than the standard error of about 14 points.

**Source:** A prompt revision is a hypothesis

## MA-ch02.27

A developer runs a prompt once at temperature 0.8 on ten questions and reports 9/10 correct. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A second run may produce different outputs and a different score.
- [ ] B. Run-to-run sampling noise is negligible compared with real prompt effects.
- [ ] C. Repeating the run several times adds no information beyond a single run.
- [ ] D. A single run suffices because output is a deterministic function of the prompt.
- [ ] E. Setting the temperature to 0 makes the outputs of a hosted model identical on every run.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Sampling at non-zero temperature draws different tokens on different runs.
- B: On small sets, noise can be as large as the effects being compared.
- C: Repeated runs show how much of a score is sampling noise.
- D: At temperature above zero, the output is a random draw, not a fixed function of the prompt.
- E: Greedy decoding reduces variation, but hosted systems do not promise bit-identical outputs.

**Source:** A prompt revision is a hypothesis

## MA-ch02.28

A teammate claims that starting a prompt with "You are an expert analyst" makes answers more accurate because experts are accurate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An observed difference should be reported together with its conditions (cases, model, criterion) rather than credited to the role line.
- [ ] B. The role line supplies new supporting facts that the model can use.
- [ ] C. The role line is an untested hypothesis until it is compared with the same prompt without it on fixed cases.
- [ ] D. If it helps on one test set, the improvement carries over to other tasks and models.
- [ ] E. A persona line changes what a code validator checks about the output.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Reporting conditions tells a reader what the result does and does not cover.
- B: A role label adds no source passages or facts.
- C: Any prompt change is a hypothesis, and only a comparison on fixed cases can support it.
- D: Effects found on one set of cases, one model and one criterion need not transfer.
- E: A validator checks the returned object against fixed rules, whatever persona text produced it.

**Source:** A prompt revision is a hypothesis

## MA-ch02.29

After testing a revised prompt on 10 development cases, a developer's write-up lists only the 8 cases that improved and omits the other 2. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reporting failures harms credibility, so they should be left out.
- [ ] B. Showing only successes prevents readers from assessing which failure modes remain.
- [ ] C. Omitting the cases that did not improve overstates the result.
- [ ] D. A change-log entry that names the specific instruction changed, and why, lets a later reader reconstruct what differed.
- [ ] E. A revision that fails to help is still an informative result when the trail is intact.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Disclosing failures is what makes the reported successes believable.
- B: Failures are where the remaining risk shows.
- C: Selective reporting inflates apparent effectiveness.
- D: Specific entries make the candidate explanations for a difference visible.
- E: A documented negative result tells others what not to repeat.

**Source:** A prompt revision is a hypothesis

## MA-ch02.30

Two plans are proposed for judging whether answers are "supported" by their sources. Plan 1 fixes the definition of supported, including how to handle cases where the sources are insufficient, before any outputs are seen. Plan 2 defines it after seeing which prompt produced the more fluent answers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A two-outcome criterion is more informative than one that adds a cannot-be-determined outcome, because it forces a decision.
- [ ] B. Fixing the criterion before seeing outputs reduces the flexibility available to bias the conclusion.
- [ ] C. Answers that cannot be determined should be counted as supported when they read fluently.
- [ ] D. Plan 2 lets the definition drift toward whatever favors the preferred prompt.
- [ ] E. Plan 1 eliminates all disagreement between reviewers.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: An unknown outcome keeps unverifiable answers from being forced into pass or fail.
- B: Committing in advance removes a source of unconscious or motivated adjustment.
- C: Fluency is not evidence; unverified answers should be reported as unverified.
- D: A threshold adjusted after seeing results can be tuned until the expected winner wins.
- E: A pre-fixed definition reduces ambiguity but reviewers can still read a case differently.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.31

Reviewers tend to rate answers that read smoothly and confidently as more trustworthy. Check each statement that is true about this tendency and how to counter it. Each statement is worth 1 point (5 points total).

- [ ] A. Writing down the failure condition before reading any output helps counter it.
- [ ] B. A green result from an automated check removes the need for a content review.
- [ ] C. A confident, well-formatted answer deserves more trust than a hesitant one.
- [ ] D. Fluency and factual correctness are separate properties of an output.
- [ ] E. Verifying outputs costs more than producing them, so verification is often under-budgeted.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: A criterion fixed in advance resists being bent by how persuasive an answer reads.
- B: An automated check covers only what it tests; content support needs its own review.
- C: Confidence of presentation is not evidence of accuracy.
- D: Fluent text can be false, and awkward text can be right.
- E: Generation is cheap and checking is not, so checks that are not planned for tend not to happen.

**Source:** Work through the three-response experiment

## MA-ch02.32

A report says only: "The revised prompt achieved a higher pass rate." Check each statement that is true about what a reader cannot tell from that sentence. Each statement is worth 1 point (5 points total).

- [ ] A. A gain in format compliance could coincide with a loss of factual support, and the sentence would not reveal it.
- [ ] B. The number of cases is irrelevant to interpreting the claim.
- [ ] C. The reader cannot tell whether the baseline was run on the same cases.
- [ ] D. The reader cannot tell what the pass criterion was.
- [ ] E. The reader cannot tell whether the cases had been used while revising the prompt.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Aggregate pass rates compress different kinds of failure into one number.
- B: A rate over 5 cases and a rate over 500 carry very different weight.
- C: A comparison is only meaningful when both versions face the same cases.
- D: "Pass" depends entirely on which checks were applied.
- E: Cases used for tuning inflate the result, so their status matters.

**Source:** What a pass rate leaves out

## MA-ch02.33

An experiment compared two prompts on the same 10 fixed cases. The format validator accepted 6 of 10 baseline responses and 10 of 10 revised responses. The team then reviewed support, claim by claim against the sources, for 4 of the 10 revised answers and found all 4 supported. Nothing else was checked, on one model on one date. Check each statement that the evidence justifies. Each statement is worth 1 point (5 points total).

- [ ] A. The 6 unreviewed revised answers can be reported as supported because they passed the validator.
- [ ] B. The revised prompt is better than the baseline in general.
- [ ] C. The 4 reviewed revised answers were supported by their sources.
- [ ] D. On these 10 cases, the revised prompt passed the format validator more often than the baseline.
- [ ] E. The revised answers are accurate.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Passing a structural validator is not a support judgment, so those six remain unreviewed.
- B: Ten cases, one model and one date cannot support a general claim.
- C: Those four were checked claim by claim and found supported.
- D: 10 of 10 against 6 of 10 on the same cases is a recorded difference in validator acceptance.
- E: Only four answers were reviewed, so accuracy of the set is not established.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.34

To test robustness, a team writes three paraphrases of one question, keeping every fact and requirement the same, and runs each against the same prompt. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Answers that word the same facts differently show that the prompt is not robust.
- [ ] B. Comparing format validity, claim content and support separately shows which dimension moved.
- [ ] C. What must stay invariant under rewording can be decided after seeing the results.
- [ ] D. After the paraphrase results are used to revise the prompt, those paraphrases remain untouched held-out evidence.
- [ ] E. Differences in tone or sentence structure in the answers may be acceptable variation, while an altered fact is not.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Many different wordings can satisfy the same task; what must hold fixed is the facts and obligations.
- B: A change in format alone is a different finding from a change in claim content.
- C: Deciding afterward lets the line be drawn to fit the observations.
- D: Once results guide a revision, the cases have become development evidence.
- E: The invariant is the intended meaning and obligations, not the surface wording.

**Source:** Computational Skepticism

## MA-ch02.35

An agent emits the tool call {"tool": "delete_file", "path": "/data/reports"} and the call validates against the tool-call schema. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Passing schema validation shows the call is well formed.
- [ ] B. Authorization should be enforced by permissions and allowlists outside the model's output.
- [ ] C. Passing schema validation does not establish that the agent is permitted to delete that path.
- [ ] D. A schema-valid tool call is safe to execute.
- [ ] E. Even for a schema-valid call, destructive actions benefit from human confirmation or a reversible mechanism.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The call has the expected fields and types.
- B: Least-privilege access and allowlists enforce limits whatever the model emits.
- C: A schema describes shape; permission is a separate policy question.
- D: Well-formed and safe are different properties, and a well-formed call can still be destructive.
- E: Approval and undo mechanisms address consequences that no schema can judge.

**Source:** From acceptable text to consequential action

## MA-ch02.36

A developer gives an AI coding assistant a contract and a list of tests, but not the developer's own validator. The assistant returns an implementation, and the developer runs the developer's own tests on it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Once an assistant is available, writing a baseline implementation first is wasted effort.
- [ ] B. A failing test may reveal a gap in the contract or the tests, not only a defect in the assistant's code.
- [ ] C. Passing tests that the assistant wrote itself shows the developer's tests are redundant.
- [ ] D. The assistant's own tests passing is sufficient evidence of correctness.
- [ ] E. The assistant can judge, from the same context, whether the tests are adequate, so no independent check is needed.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A baseline written first gives an independent reference and shows what you understood before the assistant contributed.
- B: The assistant works only from what it was given, so its mistakes can trace back to incomplete specifications.
- C: Tests written by the same party share its assumptions and do not replace independent tests.
- D: Tests written by the same party that wrote the code share its assumptions.
- E: Adequacy of the tests is the thing under question, and a system cannot be the only judge of tests on its own work.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch02.37

A team is building evaluation cases for a grounded question-answering feature, where answers must come only from supplied documents. Check each statement that is true about sound case design. Each statement is worth 1 point (5 points total).

- [ ] A. Adversarial boundary cases and a random sample of live traffic answer the same question, so their pass rates can be pooled freely.
- [ ] B. Dozens of near-duplicate cases carry as much information as the same number of diverse cases.
- [ ] C. A set drawn only from the very hardest cases estimates typical production behavior.
- [ ] D. A set containing only easy, clean cases produces a flattering pass rate that may not predict real use.
- [ ] E. Including questions the supplied documents cannot answer tests whether the system abstains instead of inventing.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Boundary cases probe worst-case behavior while traffic samples estimate typical frequency; pooling them blurs both.
- B: Near-duplicates mostly repeat the same test and add little independent evidence.
- C: Typical behavior requires a sample that resembles typical use, not only extremes.
- D: Case difficulty drives the rate, so easy cases overstate reliability.
- E: Unanswerable questions are the only way to observe abstention behavior.

**Source:** A prompt revision is a hypothesis

## MA-ch02.38

A grounded question-answering test set has 20 answerable questions and 10 unanswerable ones. On the 20 answerable questions the system answers 17 correctly, wrongly abstains on 2, and answers 1 incorrectly. On the 10 unanswerable questions it abstains on 6 and gives a made-up answer on 4. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Overall, 23 of 30 cases (about 77%) show the intended behavior.
- [ ] B. Accuracy on the answerable questions is 85%.
- [ ] C. The system abstains correctly on 60% of the unanswerable questions.
- [ ] D. The single overall figure of about 77% would hide that 40% of the unanswerable questions received a fabricated answer.
- [ ] E. The overall abstention rate across all 30 cases is 6 of 30, or 20%.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: 17 correct answers plus 6 correct abstentions is 23 of 30, which is 76.7%.
- B: 17 of 20 is 0.85.
- C: 6 of 10 is 0.60.
- D: 4 of 10 unanswerable questions got fabricated answers, a fact the aggregate conceals.
- E: Abstentions total 2 (wrongful) plus 6 (correct), which is 8 of 30, or about 27%.

**Source:** What a pass rate leaves out

## MA-ch02.39

A grader scores a free-form summary as correct only when it exactly equals a reference summary string. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An exact-match accuracy of 0% proves the model's summaries are all factually wrong.
- [ ] B. Rubric scoring by a trained human or a validated model grader is a more appropriate way to score summaries.
- [ ] C. Normalizing case and whitespace before comparing can change which responses count as matches.
- [ ] D. Exact matching suits closed-form outputs such as a label from a fixed set or a single number.
- [ ] E. A correct paraphrase of the reference would be scored as wrong.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Zero exact matches can occur when every summary is accurate but worded differently.
- B: Graders that tolerate paraphrase fit tasks with many acceptable outputs, provided they are validated.
- C: Normalization can turn a mismatch into a match, so it affects scores.
- D: When there is exactly one acceptable string, equality is a precise grader.
- E: Many distinct wordings convey the same content, and string equality accepts only one.

**Source:** A source identifier is an address, not an argument

## MA-ch02.40

A team wants a prompt experiment that another person could audit. Check each statement that is true about what the record should contain. Each statement is worth 1 point (5 points total).

- [ ] A. The model's name alone is enough, because a model's behavior does not change over time.
- [ ] B. Label hand-constructed test strings separately from responses actually returned by a model.
- [ ] C. Record the exact prompts, the source materials, the model identifier and the date.
- [ ] D. Preserve each raw response before any editing or repair.
- [ ] E. Overwrite the baseline prompt with each revision so that a single current file remains.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Hosted models are updated and aliases can be re-pointed, so the date and exact identifier matter.
- B: The two kinds of data support different claims and must stay distinguishable.
- C: Without the inputs and conditions, a result cannot be reproduced or interpreted.
- D: Edits made before saving destroy the observation that was actually made.
- E: An intact baseline is what each revision is compared against.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.41

A team hand-writes 20 responses, some malformed and some contradicting their sources, to exercise a validator. The validator rejects 7. The report then states: "The model fails the format requirement 35% of the time." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 35% describes the hand-written set, not the behavior of any model.
- [ ] B. If the strings resemble real model outputs, the report may legitimately describe them as observed model outputs.
- [ ] C. Hand-constructed test data has no value.
- [ ] D. The 35% would be the same whichever mix of malformed and valid strings the person building the set chose.
- [ ] E. A defensible statement is that the model fails the format requirement 35% of the time.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: No model produced these strings, so no model rate can be read from them.
- B: Resemblance does not change provenance; presenting constructed text as observed output is misleading.
- C: Constructed cases are valuable for testing that a validator catches specific defects.
- D: Whoever builds the set chooses how many malformed items to include, which sets the rate by design.
- E: No model produced the strings; the supportable statement is that the validator rejected 7 of 20 constructed responses.

**Source:** Work through the three-response experiment

## MA-ch02.42

A team iterates on a prompt for two weeks until their format validator accepts all 30 of their test cases. They report that output quality is now perfect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 100% rate on the cases used for iteration reliably predicts the rate on new inputs.
- [ ] B. A measure that becomes the sole target tends to stop being a good measure of the underlying goal.
- [ ] C. Testing on a set kept untouched during iteration would give a less biased estimate.
- [ ] D. The result shows that no unsupported answers can be present among the 30.
- [ ] E. Optimizing against a fixed validator cannot overfit, because the validator is deterministic.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Cases used for tuning will look good by construction.
- B: This is Goodhart's law, and it applies directly to optimizing against a single metric.
- C: Untouched data restores the independence a fair estimate needs.
- D: A format validator says nothing about whether claims are supported.
- E: Repeated tuning finds prompts that satisfy the checker, whether or not they serve the underlying goal.

**Source:** A prompt revision is a hypothesis

## MA-ch02.43

A team finds that its output contract has no way to express "insufficient evidence", so it adds a status field to the object and reruns its earlier cases. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The new version's pass rate can be compared with the old version's on the same cases without any caveat.
- [ ] B. Old tests passing validates the new behavior.
- [ ] C. The change can be made silently if it raises the pass rate.
- [ ] D. The change should be recorded as a new version of the contract.
- [ ] E. Cases that guided the redesign remain untouched held-out evidence.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The two versions apply different rules, so their rates measure different things.
- B: Tests written for the earlier rules do not exercise the new field.
- C: Undisclosed changes make results impossible to interpret, whatever they do to the rate.
- D: Behavior has changed, so the contract is a different specification.
- E: Cases that influenced a design decision have become development evidence.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.44

A team divides work on an evaluation between a human and an AI assistant. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because an assistant can err, none of its work on an evaluation (drafts, code or tests) is of any use.
- [ ] B. Deciding what counts as acceptable depends on stakes and downstream costs that the assistant may not see.
- [ ] C. An assistant can draft test cases, implement a validator from a specification, and propose malformed inputs.
- [ ] D. Because assistants write fluent explanations, their support judgments need no review.
- [ ] E. The assistant, not the person, should own the acceptance decision because it computes faster.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Delegating drafting and computation while retaining judgment is a reasonable division.
- B: The consumer, the stakes and the cost of error usually live outside the files the assistant reads.
- C: Drafting and enumerating are tasks at which assistants are fast and useful.
- D: Fluency is not evidence, and an assistant's verdict is itself an output to check.
- E: Ownership follows who bears the consequences, not who computes fastest.

**Source:** The driver's seat: what counts as acceptable

## MA-ch02.45

To make answers inspectable, a team asks the model to add a short justification that quotes the supporting passage from the supplied source. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A quoted span can be checked mechanically for whether it appears verbatim in the source.
- [ ] B. Asking for a quoted passage makes the answer easier to audit.
- [ ] C. A fluent justification is evidence of the model's actual internal reasoning process.
- [ ] D. The justification is itself output that must be evaluated.
- [ ] E. A quote that appears in the source supports the claim it is attached to.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Substring matching against the source is a deterministic check.
- B: A reviewer can go straight to the quoted location instead of searching the source.
- C: A generated explanation is more text; it is not a window into the computation that produced the answer.
- D: A justification can be wrong, misleading or irrelevant like any other output.
- E: A real quote can be taken out of context or be about something else.

**Source:** A source identifier is an address, not an argument

## MA-ch02.46

A team cannot afford a human review of every accepted answer. From 1,000 accepted answers it reviews a random sample of 50 and finds 4 contradicted by their sources. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With only 50 reviewed, the estimate is imprecise, with a standard error of roughly 4 percentage points.
- [ ] B. The point estimate for the whole set is about 80 contradicted answers.
- [ ] C. Reviewing a larger random sample would narrow the uncertainty of the estimate.
- [ ] D. Because the validator accepted all 1,000, none of the unreviewed 950 can be contradicted.
- [ ] E. The sample proportion of contradicted answers is 8%.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The standard error is sqrt(0.08 x 0.92 / 50), about 0.038.
- B: 8% of 1,000 is 80.
- C: Standard error shrinks as the sample grows.
- D: Acceptance by a structural validator carries no information about whether a claim is contradicted.
- E: 4 divided by 50 is 0.08.

**Source:** What a pass rate leaves out

## MA-ch02.47

A prompt succeeds on any given trial with probability 0.9, and trials are independent. Evaluating its reliability on a workflow that must succeed on five consecutive runs, a team computes 0.9 x 0.9 x 0.9 x 0.9 x 0.9, which is about 0.59. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Independence of trials is an assumption that may fail for real workloads.
- [ ] B. If success per run rose to 0.95, the chance of five in a row would be about 95%.
- [ ] C. The 59% figure applies to any workflow with 5 steps regardless of whether the steps depend on each other.
- [ ] D. A 90% per-run success rate can look reliable on a single run and still be unreliable over a chain of runs.
- [ ] E. The chance of five successes in a row is about 59%.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Correlated failures, shared causes, or inputs that are hard in the same way break independence.
- B: 0.95 to the fifth power is about 0.77, not 0.95.
- C: The calculation assumes independent steps with equal success probability; dependence changes the answer.
- D: Failure probabilities compound across repeated or chained use.
- E: 0.9 to the fifth power is 0.59.

**Source:** What a pass rate leaves out

## MA-ch02.48

A pipeline checks each model answer in layers: (1) the reply parses as JSON with the required keys; (2) every cited identifier belongs to the supplied set; (3) any quoted span appears verbatim in the cited source; (4) a model judge scores whether the claim follows from the source; (5) a human reviews a random sample of passing answers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An answer that passes layers 1 through 4 has been established to be correct.
- [ ] B. Layer 4 covers meaning and, being a model, needs no calibration against human labels.
- [ ] C. Layer 3 can reject a fabricated quotation but cannot tell whether a genuine quotation was used in a misleading way.
- [ ] D. Layer 5 is unnecessary once layer 4 exists, because two automated checks are as good as human review.
- [ ] E. Layers 1 and 2 are cheap and deterministic but cannot detect a claim that contradicts its source.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Passing automated layers narrows risk without proving correctness.
- B: A model judge's error rate has to be estimated against human labels.
- C: Verbatim matching verifies the quote exists, not that its use is fair.
- D: A sampled human review is the independent check against which automated judges are calibrated.
- E: Structure and identifier membership say nothing about content.

**Source:** Work through the three-response experiment

## MA-ch02.49

Two reviewers independently label 20 answers as "supported" or "contradicted" against their sources. They agree on 17 of the 20. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Disagreements often indicate the criterion for "supported" is ambiguous and needs sharpening.
- [ ] B. The raw agreement is 85%.
- [ ] C. When two reviewers disagree, the correct label is whichever the more fluent reviewer chose.
- [ ] D. Cohen's kappa corrects observed agreement for agreement expected by chance.
- [ ] E. Raw agreement is the same quantity as chance-corrected agreement.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Systematic disagreement usually traces to an under-specified rule.
- B: 17 of 20 is 0.85.
- C: Disagreements are resolved by a defined procedure such as adjudication or a clearer criterion, not by style.
- D: Kappa is defined as observed agreement minus chance agreement, scaled by the maximum possible beyond chance.
- E: With two labels, a substantial share of agreement can occur by chance alone, so the quantities differ.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.50

On 200 responses, a structural validator accepted 140 and rejected 60. A careful reviewer then judged content for all 200. Among the 140 accepted, 21 were unsupported by their sources. Among the 60 rejected, 9 would have been supported had the format been acceptable. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The validator's acceptance rate of 70% (140 of 200) is a measure of the proportion of supported answers.
- [ ] B. Of the 60 rejected responses, 40% had supported content.
- [ ] C. 15% of the accepted responses were unsupported even though they passed.
- [ ] D. Because the validator rejected some good content, it should be removed.
- [ ] E. 119 of the 140 accepted responses (85%) were supported.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Acceptance rate measures structural compliance; the supported share among accepted is a separate figure.
- B: 9 of 60 is 15%, not 40%.
- C: 21 of 140 is 0.15.
- D: A validator that guards the consumer's contract still has value; rejection of well-supported but malformed content is the cost of strictness and may be addressed by repair or retry.
- E: 140 minus 21 is 119, and 119 over 140 is 0.85.

**Source:** Work through the three-response experiment

## MA-ch02.51

A contract asks the model to include a self-reported confidence number between 0 and 1 with each answer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Confirming that the number lies between 0 and 1 checks the format but not whether it is calibrated.
- [ ] B. Language models' self-reported confidence can be overconfident.
- [ ] C. Averaging the stated confidence over all answers and comparing it with overall accuracy gives a coarse calibration check.
- [ ] D. A stated confidence of 0.9 means the answer is correct about 90% of the time.
- [ ] E. Calibration can be assessed by grouping answers by stated confidence and comparing each group's stated confidence with its observed accuracy.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A range check confirms form, not meaning.
- B: Overconfidence in model-reported probabilities is widely observed.
- C: Mean stated confidence against overall accuracy is the simplest calibration comparison, though bins give more detail.
- D: A stated number carries that meaning only if it has been shown to be calibrated.
- E: Reliability diagrams compare stated and observed accuracy within bins.

**Source:** A source identifier is an address, not an argument

## MA-ch02.52

A baseline prompt produced responses where the format validator accepted 6 of 10, and 5 of those 6 were judged supported by their sources. A revision with examples was accepted on 9 of 10, and 6 of those 9 were judged supported. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reporting only the format acceptance rates would give the complete picture of the comparison.
- [ ] B. The number of responses both accepted and supported fell from 6 to 5 of 10.
- [ ] C. The share of accepted responses that were supported fell from about 83% to about 67%.
- [ ] D. Format acceptance rose from 60% to 90%.
- [ ] E. The format gain alone shows the revision made answers more faithful to their sources.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Two columns, format and support, tell a different story than either one alone.
- B: Accepted-and-supported responses rose from 5 to 6 of 10.
- C: 5/6 is 83% and 6/9 is 67%.
- D: 6/10 is 60% and 9/10 is 90%.
- E: Format compliance is a different property; here the supported share among accepted fell.

**Source:** Work through the three-response experiment

## MA-ch02.53

For each held-out question, a team writes, before any model response exists, one sentence describing an answer that would pass its format validator and still fail its evidence criterion. Check each statement that is true about this practice. Each statement is worth 1 point (5 points total).

- [ ] A. If the sentence is written after seeing the response, it describes the output instead of testing the team's understanding.
- [ ] B. It forces the team to think about how its automated check could be fooled.
- [ ] C. The sentence should be based on the model's actual response to that question.
- [ ] D. Being unable to write the sentence suggests the team does not yet know what it is checking for.
- [ ] E. The sentence is paperwork with no bearing on the quality of the evaluation.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Hindsight descriptions are fitted to what happened and so test nothing.
- B: Anticipating a passing-but-wrong answer exposes the gap between structure and content.
- C: Basing it on the response defeats the purpose of writing it in advance.
- D: Not being able to imagine a failure means the evidence criterion is not yet understood.
- E: Pre-stated failures sharpen the evidence criterion and make the evaluation harder to game.

**Source:** The gate: write the contract for the consumer first

## MA-ch02.54

A report on 100 cases states that 90 pass. Among the 10 failures, 8 are cosmetic (a stray space in a field) and 2 are responses that tell a customer a wrong refund amount. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A single pass rate weights the cosmetic failures and the wrong-refund failures equally.
- [ ] B. A 90% pass rate means 90% of the answers were correct.
- [ ] C. Reporting failures by category lets readers see which failures matter.
- [ ] D. Equal weighting is a policy choice that can be replaced by severity weights.
- [ ] E. Severity weights should be chosen after seeing which prompt wins, so the better prompt is rewarded.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Each failure subtracts one case regardless of its consequence.
- B: Pass rate measures acceptance by the stated checks, not correctness.
- C: A breakdown shows that most failures here are harmless and two are consequential.
- D: Which failures count most is a decision about stakes, not a discovered fact.
- E: Weights chosen after results can be fitted to favor an outcome and should be set beforehand.

**Source:** What a pass rate leaves out

## MA-ch02.55

A single constructed response is shown to pass a checker while violating the property the checker was meant to protect. Check each statement that is true about what such a constructed counterexample establishes. Each statement is worth 1 point (5 points total).

- [ ] A. A single such example is enough to refute the claim "passing this check implies the property."
- [ ] B. It shows that passing the checker does not by itself guarantee the property.
- [ ] C. It shows how often the failure occurs in real use.
- [ ] D. It is a demonstration of a logical gap, not a frequency estimate.
- [ ] E. It shows the checker is broken, since a correct checker would have rejected such a response.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A universal implication is refuted by any single counterexample.
- B: The example proves the check is not sufficient for the property.
- C: One handpicked case carries no information about frequency.
- D: Its force is logical: one counterexample defeats a universal claim.
- E: The checker may perform exactly the job it was specified for; the error lies in over-reading what its pass means.

**Source:** Work through the three-response experiment

## MA-ch02.56

A function pass_rate(responses, validator) returns the number of accepted responses divided by the number of responses. Check each statement that is true about the input of an empty list. Each statement is worth 1 point (5 points total).

- [ ] A. Returning 1.0 could be misread as perfect performance.
- [ ] B. An experiment with zero cases has a pass rate of 100% by mathematical convention.
- [ ] C. Returning 0.0 could be misread as a tested system that failed every case.
- [ ] D. Raising an error, or returning an explicit "undefined" value, signals that there is no evidence.
- [ ] E. In Python, 0 / 0 evaluates to 0.0.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: One implies tests were run and all passed.
- B: A rate with an empty denominator is undefined; vacuous truth applies to universal statements, not to ratios.
- C: Zero implies tests were run and failed.
- D: An undefined result keeps "no data" from posing as a performance figure.
- E: Dividing zero by zero raises ZeroDivisionError in Python.

**Source:** Work through the three-response experiment

## MA-ch02.57

A validator is written as follows: it parses the reply, then reads data["answer"] and data["sources"] directly, and only afterward checks that data is a dictionary. It is called with the reply [1, 2], then with "abc" (a JSON string), then with 5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A validator that crashes on a malformed reply is behaving correctly, since a crash also signals rejection.
- [ ] B. Reading data["answer"] from the string "abc" raises a TypeError in Python.
- [ ] C. Reading data["answer"] from the list [1, 2] raises a TypeError in Python.
- [ ] D. Reading data["answer"] from the integer 5 returns None.
- [ ] E. Checking that the parsed value is a dictionary before indexing avoids these exceptions.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A validator should return a rejection for any input; an unhandled exception can halt the pipeline or be mistaken for a different failure.
- B: Strings are indexed by integers, so a string key raises TypeError.
- C: Lists cannot be indexed with a string key.
- D: Integers are not subscriptable, so the access raises TypeError.
- E: A type check first lets the function return a rejection cleanly.

**Source:** What each line of the validator promises

## MA-ch02.58

A reviewer checks 20 answers against their sources, using three outcomes: supported, contradicted, and cannot be determined. The counts are 12 supported, 5 contradicted and 3 cannot be determined. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Counting the 3 undetermined answers as supported is a neutral way to resolve them.
- [ ] B. The share of all 20 that were established as supported is 60%.
- [ ] C. If every undetermined answer were later found supported, the share would be 75%.
- [ ] D. Reporting only the single supported percentage is as informative as reporting all three counts.
- [ ] E. If every undetermined answer were later found contradicted, the share would fall below 60%.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Counting unknowns as supported inflates the result in the direction the reviewer may prefer.
- B: 12 of 20 is 0.60.
- C: 12 plus 3 is 15 of 20, which is 0.75.
- D: The three counts show the established result and the size of the unresolved remainder.
- E: The supported count would remain 12 of 20, so the share would stay at 60%.

**Source:** Work through the three-response experiment

## MA-ch02.59

A team ran the same prompt against a hosted model alias in March and again in June. Its validator acceptance rate on the same 40 cases was 36/40 in March and 31/40 in June. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A gap of five cases out of 40 can be dismissed as certainly meaningless.
- [ ] B. The March rate was 90% and the June rate was 77.5%.
- [ ] C. Recording only the model family name is enough to interpret such a difference.
- [ ] D. Because the prompt and cases were identical, any difference must be caused by random sampling alone.
- [ ] E. The 12.5-point difference proves that the provider degraded the model.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A 12.5-point gap on 40 cases is neither clearly noise nor clearly real, so it calls for investigation rather than dismissal.
- B: 36/40 is 0.90 and 31/40 is 0.775.
- C: An exact model identifier and run date are needed to interpret changes over time.
- D: Model changes, infrastructure changes and sampling noise are all candidate explanations.
- E: The data are consistent with a model change, with sampling noise, or with both; they do not prove either.

**Source:** Ship It: an experiment another person can audit

## MA-ch02.60

A team must choose which checks to run on model answers that will be shown to customers. Check each statement that is true about choosing checks by stakes. Each statement is worth 1 point (5 points total).

- [ ] A. Different consumers of the same output may reasonably set different acceptance rules.
- [ ] B. The more costly a wrongly accepted answer is, the more independent content-level verification is justified.
- [ ] C. The acceptance threshold should be determined by whichever value makes the current pass rate look best.
- [ ] D. A strictness threshold such as "every claim must be supported" versus "most claims" is a decision about acceptable risk.
- [ ] E. A cheap structural check alone is adequate at any consequence level, since structural acceptance implies the answer is good.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A hobby tool and a medical tool, for example, tolerate different risk.
- B: Verification effort should scale with the consequence of an error.
- C: Choosing thresholds to flatter results defeats the purpose of having a threshold.
- D: How much unsupported content is tolerable is a risk judgment, not a technical fact.
- E: A structural check accepts well-formed false answers, which is dangerous when errors are costly.

**Source:** The driver's seat: what counts as acceptable

## MA-ch02.61

A validator is run on three prepared strings: (1) text that is not JSON; (2) an object that parses, has the right keys and types, and cites an identifier that was not supplied; (3) an object that parses, has the right keys and types, and cites a supplied identifier but makes a claim that contradicts the source. It accepts only the third. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The validator accepts 1 of 3 strings, so the acceptance rate on this set is 1/3.
- [ ] B. The second string is rejected at the identifier-membership rule.
- [ ] C. The first string is rejected at parsing, before any field rule is applied.
- [ ] D. Calling 1/3 an accuracy score would misname what was measured.
- [ ] E. The accepted string is the only one that is correct.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: One accepted out of three is a rate of 0.333.
- B: Parsing, shape and types succeed, and the unsupplied identifier fails the membership rule.
- C: A syntax failure ends processing at the parser.
- D: The rate measures acceptance by structural rules, which the contradicted claim passes.
- E: The accepted string contradicts its source, so it is the one that is wrong in content.

**Source:** Work through the three-response experiment

## MA-ch02.62

A prompt includes three example input-output pairs showing correctly formatted answers. Check each statement that is true about few-shot examples in an evaluation. Each statement is worth 1 point (5 points total).

- [ ] A. Examples taken from the evaluation cases are harmless to the measurement.
- [ ] B. Examples can also anchor content, causing the model to copy details from an example into its answers.
- [ ] C. Higher format compliance implies the answers are more faithful to their sources.
- [ ] D. The order and choice of examples can change the model's outputs.
- [ ] E. Whether examples raise format compliance is a hypothesis to be tested on fixed cases.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Examples drawn from the evaluation cases leak the answers and contaminate the result.
- B: Models can reproduce surface features and facts from examples.
- C: Format compliance and source faithfulness are independent properties.
- D: Sensitivity to example selection and order is well documented.
- E: Few-shot prompting is common practice but its benefit on a given task must be measured.

**Source:** A prompt revision is a hypothesis

## MA-ch02.63

A team requires that each of its contract's rules have a test that fails if that rule is deleted. Check each statement that is true about this practice. Each statement is worth 1 point (5 points total).

- [ ] A. Deleting a rule in a scratch copy and rerunning the tests shows whether any test notices the deletion.
- [ ] B. A test that passes both with and without a rule defends nothing about that rule.
- [ ] C. Once every rule has such a test, the validator reflects what the consumer needs.
- [ ] D. It checks that tests defend each behavior the contract promises, not merely that tests exist.
- [ ] E. Coverage of the contract is measured by the number of tests.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Deliberately breaking code and observing the tests is the idea behind mutation testing.
- B: A test insensitive to a rule's presence provides no evidence about that rule.
- C: The tests defend the contract as written; whether the contract matches the consumer's needs is a separate judgment.
- D: Coverage is measured per behavior, not by test count.
- E: Many tests can exercise the same few behaviors and leave others undefended.

**Source:** Build It: your validator is the baseline

## MA-ch02.64

A validator is given the set of allowed source identifiers but not the text of the sources. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. It can determine whether the cited text supports the answer.
- [ ] B. It can reject a citation of an identifier that was never supplied.
- [ ] C. The inputs a check receives limit what it is able to decide.
- [ ] D. Giving the validator the source text would be enough by itself to make it judge support, without any new comparison logic.
- [ ] E. Membership in a registry of identifiers and support for a proposition are different relations.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Without the source text, there is nothing to compare the answer against.
- B: Set membership is computable from the identifier list alone.
- C: A function cannot decide on information it never receives.
- D: Access to text is necessary but not sufficient; a comparison procedure such as quote matching or entailment judging is also required.
- E: An identifier can exist while the text behind it says something else.

**Source:** A source identifier is an address, not an argument
