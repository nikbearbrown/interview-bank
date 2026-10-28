# Chapter 7: Retrieval and Cowork

## ES-ch07.1

The chapter opens with two constructed cases. In the first, a corpus contains "Office hours by appointment" and the query is "office hours". In the second, the query is "tuition refund" and the only relevant document says "fee reimbursement". For each case, say what the small retriever does and what a human reader must still ask or notice.

**Points:** 5

**Rubric (1 point each):**

1. Says that in the first case the document ranks highly because the shared words are visible to the retriever.
2. Says that even when every step worked in the first case, a human still has to ask whether "by appointment" says when to show up.
3. Says that in the second case the retriever returns nothing because its representation sees no shared token between "tuition refund" and "fee reimbursement".
4. Notes that a human reader can see the relationship the retriever misses.
5. Notes that both are constructed cases from the course's offline exercise, not measurements of a deployed system.

**Source:** Chapter 7 (opening, before the first section)

## ES-ch07.2

The research run behind this chapter records three results. State them, and then state what those results are not evidence about.

**Points:** 5

**Rubric (1 point each):**

1. States the recorded cosine of 2 / sqrt(6), approximately 0.8164965809, between "office hours" and "office hours appointment".
2. States that the run records no result for the synonym pair.
3. States that the run records deterministic ordering for tied scores.
4. States that the results come from the displayed count-vector implementation.
5. States that they are not measurements of Claude Cowork, neural embeddings, or human semantic understanding.

**Source:** Chapter 7 (opening, before the first section)

## ES-ch07.3

A colleague says: "If the retriever had dropped the one source that mattered, Claude's answer would at least sound hesitant." Using the chapter's opening, explain why this is wrong, and say what this implies for how a reviewer should start.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude will write a fluent answer from whatever reached it.
2. Says nothing Claude received says what was left out.
3. Says the sentence reads the same whether the evidence was complete or not.
4. Notes that in the second case a step quietly dropped the only source that mattered, with nothing in the output saying so.
5. Concludes that the reviewer cannot detect the omission from the prose and must examine the selection (the audit view) rather than judge the answer first.

**Source:** Chapter 7 (opening, before the first section)

## ES-ch07.4

Chapter 1 named three jobs that stay with you: conduct, check, drive. Explain what each job means for retrieval in this chapter, and why retrieval is where they bite hardest.

**Points:** 5

**Rubric (1 point each):**

1. Names the three jobs as conduct, check, and drive, and attributes them to Chapter 1.
2. Explains conduct as deciding what reaches Claude's context before the task runs.
3. Explains check as including that relevance is not entailment and that ranking turns scores into omissions.
4. Explains drive as Claude ranking and quoting while what a source means in the world is your reading.
5. Explains that retrieval bites hardest because it makes the most decisions and leaves the fewest traces.

**Source:** Chapter 7 (opening, before the first section)

## ES-ch07.5

The chapter places ranking passages by similarity in the first tier of Irreducibly Human. Explain what the machine does well there, what stays with you, and why the second of those two things cannot be skipped.

**Points:** 5

**Rubric (1 point each):**

1. Identifies ranking passages by similarity as pattern and association work in the first tier.
2. Says the machine wins in bounded, well-specified settings, and that a ten-line scoring function does it faster than a person.
3. Names the specification as what stays with you, including what counts as similar, what is eligible, and how many results.
4. Names the audit as what stays with you, including what the ranking left out and whether the winning passage says what the answer claims.
5. Explains that you cannot audit a ranking you have never computed, which is why you build and hand-calculate the system.

**Source:** Chapter 7 (opening, before the first section)

## ES-ch07.6

Chapter 6 reviewed a proposed code change against its diff and tests. Explain why Chapter 7 moves earlier in the pipeline, and why a clean review packet cannot fix a missing source.

**Points:** 5

**Rubric (1 point each):**

1. Says Chapter 6 reviewed a proposed change against its diff and tests.
2. Says Chapter 7 asks which source material reached the system that proposed the change or report.
3. Says a plausible response can be generated from an incomplete selection.
4. Says a clean review packet cannot recover a passage that was never in the corpus or was ranked out of the selected context.
5. Concludes that a source inventory and retrieval record are needed alongside the resulting prose, because debugging generation alone will not repair a missing source.

**Source:** Chapter 7 (opening, before the first section)

## ES-ch07.7

List the seven narrowing stages between a stack of documents and a sentence in a report, in order. Then say which stages leave something visible in the final prose, and what they leave.

**Points:** 5

**Rubric (1 point each):**

1. Lists all seven stages in order: eligibility, ingestion, representation, scoring and cutoff, selection into context, use, claim.
2. States that five of the seven stages leave nothing in the final prose.
3. Says the Use stage leaves a citation, if you required one.
4. Says the Claim stage leaves the verbs.
5. Explains that a citation asserts a relationship rather than showing it, so omission is silent at the layer where you read.

**Source:** What reaches Claude is the end of a chain of omissions

## ES-ch07.8

The chapter borrows a point from Computational Skepticism for AI about missing data. State the point and the central question the book asks, and explain how the chapter maps the book's join and histogram onto this retrieval system.

**Points:** 5

**Rubric (1 point each):**

1. States that you cannot compute the missingness of rows that never existed.
2. States the central question: why are there exactly N rows, and what was N supposed to be?
3. Says ingestion plays the role of the join that silently dropped records.
4. Says the score table plays the role of the histogram: precise about what arrived and silent about what did not.
5. Notes that the book's join illustration is labeled a composite of familiar failures, not a single sourced incident.

**Source:** What reaches Claude is the end of a chain of omissions

## ES-ch07.9

Use the chapter's boundary from the first tier of Irreducibly Human to explain why a retrieval ranking can be excellent and still be wrong for the task. Why is finding a passage different from deciding whether it answers the question?

**Points:** 5

**Rubric (1 point each):**

1. States that the machine is better at the pattern task as specified.
2. States that the human's remaining job is to notice when the specification is wrong or when the task only looked like a pattern task.
3. Classifies finding a passage as a pattern task.
4. States that deciding whether the passage answers the question is not a pattern task.
5. Names the specification as the query, representation, corpus, and k, and says the ranking can be excellent while that specification is wrong.

**Source:** What reaches Claude is the end of a chain of omissions

## ES-ch07.10

Run the `vector` function in your head on "Office office hours". Give the resulting Counter, say which features of the text the representation keeps and which it discards, and give one kind of task where a discarded feature would matter.

**Points:** 5

**Rubric (1 point each):**

1. Gives the Counter with office at count two and hours at count one.
2. Says the text is lowercased first and then tokenized with the regular expression.
3. Says the representation keeps frequency.
4. Says it discards word order and capitalization, so "hours office" and "office hours" receive the same vector.
5. Names a task where a discarded feature matters, such as one involving proper nouns, acronyms, or case-sensitive identifiers.

**Source:** A representation decides what can match

## ES-ch07.11

Predict how the regular expression `\b\w+\b` tokenizes "don't stop", "fee-reimbursement", and "tuition_refund". Then say what you may and may not conclude from these results about other kinds of text.

**Points:** 5

**Rubric (1 point each):**

1. Says "don't stop" becomes don, t, and stop because the apostrophe splits the contraction.
2. Says "fee-reimbursement" becomes fee and reimbursement because the hyphen splits it.
3. Says "tuition_refund" stays one token because the underscore counts as a word character.
4. Says the behavior of `\w` follows Python's regular-expression rules, not a universal linguistic analysis.
5. Says you should not infer performance for multilingual, code-heavy, or adversarial corpora without testing their actual inputs.

**Source:** A representation decides what can match

## ES-ch07.12

The chapter says the right question about a representation is not whether it is intelligent. State the question the chapter says to ask instead, and use the count vector to illustrate what a representation gains and gives up.

**Points:** 5

**Rubric (1 point each):**

1. Says representations optimize for some comparisons by making others impossible.
2. Says count vectors make shared words visible and the arithmetic transparent.
3. Says count vectors sacrifice order and synonymy.
4. States that the right question is whether the retained features are adequate for the evidence-selection task.
5. States that the second right question is whether the representation's misses are visible to the workflow.

**Source:** A representation decides what can match

## ES-ch07.13

Compute by hand the cosine similarity between "office hours" and "office hours appointment". Show the token counts, the dot product, both lengths, and the result, then say what the number does and does not establish.

**Points:** 5

**Rubric (1 point each):**

1. Gives the query counts as office 1 and hours 1, with length sqrt(2).
2. Gives the document counts as office 1, hours 1, appointment 1, with length sqrt(3).
3. Gives the dot product as 2, because office and hours each contribute one.
4. Gives the cosine as 2 / (sqrt(2) * sqrt(3)) = 2 / sqrt(6), approximately 0.8165.
5. States that the number proves a lexical relationship under this representation, not that the document answers every question involving office hours.

**Source:** Cosine from first principles

## ES-ch07.14

Claude and any library can compute a cosine instantly. Why does the chapter ask you to compute one by hand anyway?

**Points:** 5

**Rubric (1 point each):**

1. Says a score is the number people quote and nobody rechecks.
2. Says the only way to know what a score measures is to have produced it yourself.
3. Says the hand calculation is the first piece of your baseline, written before you run anything.
4. Says that if any implementation, yours or Claude's, returns a different number for the pair, you already know which one to distrust.
5. Connects this to the principle that you cannot audit a ranking you have never computed.

**Source:** Cosine from first principles

## ES-ch07.15

Define the dot product, the Euclidean length, and cosine similarity for count vectors, and explain why the dot product is normalized.

**Points:** 5

**Rubric (1 point each):**

1. Defines the dot product as the sum over tokens of the query count times the document count.
2. Says tokens absent from one side contribute zero.
3. Defines the length as the square root of the sum of squared counts.
4. Defines cosine as the dot product divided by the product of the two lengths.
5. Explains that the dot product grows with shared counted terms but also grows when vectors grow, so it is normalized by their lengths.

**Source:** Cosine from first principles

## ES-ch07.16

Predict the cosine when one vector is empty. Explain what the implementation returns, why, and what you may not conclude from the value.

**Points:** 5

**Rubric (1 point each):**

1. Says an empty vector has length zero.
2. Says the function returns 0.0 for that case.
3. Says this avoids division by zero.
4. Says the value is a convention and a design choice, not a claim that the empty query is a meaningful information request.
5. Says `retrieve` would drop such a score because only positive scores are returned.

**Source:** Cosine from first principles

## ES-ch07.17

The query is "office hours". Compute its cosine against (a) "office hours by appointment" and (b) "office hours office hours". Explain what (b) shows about vector length.

**Points:** 5

**Rubric (1 point each):**

1. For (a), gives four tokens each with count one, so the document length is 2 and the dot product is 2.
2. For (a), gives the cosine as 2 / (sqrt(2) * 2), about 0.7071.
3. For (b), gives the counts office 2 and hours 2, with length sqrt(8).
4. For (b), gives the dot product as 4 and the cosine as 4 / (sqrt(2) * sqrt(8)) = 1.0.
5. Concludes that identical direction scores one whatever the lengths.

**Source:** Cosine from first principles

## ES-ch07.18

Read the `retrieve` function as a policy about what to leave out. Describe each thing it does in order, and say what Claude receives and does not receive as a result.

**Points:** 5

**Rubric (1 point each):**

1. Says it scores every declared document before filtering.
2. Says it removes nonpositive scores, so zero-overlap documents disappear from the returned list.
3. Says it sorts the remainder and takes at most k rows.
4. Says Claude receives what `retrieve` returns and nothing else.
5. Says the function does not return the documents it dropped or why, so a list of winners gives the same view the final prose does, one stage earlier.

**Source:** Ranking turns scores into omissions

## ES-ch07.19

Explain how `retrieve` validates k and why each part of the check is there. Include what happens with 0, a negative number, and True.

**Points:** 5

**Rubric (1 point each):**

1. Says k must be a positive integer, and that the check defines the accepted values.
2. Says a zero or negative k is rejected with an error instead of silently returning nothing.
3. Says the type check asks for exactly int.
4. Says a Boolean is not accepted.
5. Says an isinstance check would let True slip through, which is why it is a wrong version the tests must catch.

**Source:** Ranking turns scores into omissions

## ES-ch07.20

The corpus is {doc-b: "office hours", doc-a: "office hours", doc-c: "office hours extra"} and the query is "office hours". Predict what `retrieve` returns for k = 2 and k = 1, and name the components of the sort that produce that order.

**Points:** 5

**Rubric (1 point each):**

1. Says doc-a and doc-b both score 1.0 and doc-c scores about 0.8165 (2 / sqrt(6)).
2. Says the first sort key is the negative score, which puts higher similarities first.
3. Says the second sort key is the document key in ascending order, so doc-a precedes doc-b.
4. Predicts k = 2 returns doc-a then doc-b, and k = 1 returns only doc-a, omitting doc-b because its key sorts later.
5. Explains that relying on insertion or mapping order (doc-b was inserted first) would make equal-score selection harder to explain.

**Source:** Ranking turns scores into omissions

## ES-ch07.21

The query is "office hours" and k is 2. Three documents score positively: p1 "office hours", p2 "office hours appointment", and p3 "office hours appointment policy extra". Compute the three scores, state what is returned, and write the audit row for the omitted document.

**Points:** 5

**Rubric (1 point each):**

1. Gives p1 as 1.0 and p2 as about 0.8165 (2 / sqrt(6)).
2. Gives p3 as about 0.6325 (2 / sqrt(10), since it has five tokens).
3. States that p1 and p2 are returned and p3 is omitted.
4. Writes the audit row for p3 with its score and the fate "below the cutoff".
5. Explains that the omission is not proof of irrelevance, because the returned list is selected candidates under one scoring and cutoff rule, not all available evidence.

**Source:** Ranking turns scores into omissions

## ES-ch07.22

"Tuition refund" and "fee reimbursement" score zero under the chapter's retriever. Explain why, what zero means and does not mean, and what the possible failure locations are.

**Points:** 5

**Rubric (1 point each):**

1. Says the two phrases have disjoint token sets, so their dot product is zero.
2. Says the zero-score document is removed before top-k selection.
3. Says zero means no counted token overlap under this representation, not proof of irrelevance.
4. Names the possible failure locations: the source is absent from the corpus, present but phrased differently, or present with text the tokenizer represents poorly.
5. Says these are different failure locations that suggest different repairs.

**Source:** Ranking turns scores into omissions

## ES-ch07.23

A learner reports: "The top passage scored 0.99, so it answers the question." Explain, using the chapter, why a high score does not establish adequacy and what the next review must do.

**Points:** 5

**Rubric (1 point each):**

1. Says a document can repeat query terms while discussing a different policy.
2. Says it can also differ in time period or population.
3. Says lexical similarity is a candidate-selection signal, not a verdict on support.
4. Says the next review must inspect the passage against the actual claim.
5. Says precision to ten decimal places does not turn relevance into entailment.

**Source:** Ranking turns scores into omissions

## ES-ch07.24

Describe the audit view the gate asks for, and explain why it is needed when `retrieve` already returns the best documents.

**Points:** 5

**Rubric (1 point each):**

1. Says the audit view lists every document with its score.
2. Names the three fates: selected, below the cutoff, zero overlap.
3. Says `retrieve` does not return the documents it dropped or why.
4. Says a list of winners gives the same view as the final prose, one stage earlier.
5. Says that to see an omission you have to compute it.

**Source:** Ranking turns scores into omissions

## ES-ch07.25

A learner proposes mapping tuition to fee and refund to reimbursement before vectorization to fix the synonym miss. Explain why this is called a dangerous repair, and how the chapter says to treat it.

**Points:** 5

**Rubric (1 point each):**

1. Says the map changes the representation and can make the constructed document overlap with the rewritten query.
2. Says it creates new opportunities for false positives.
3. Says fee is not interchangeable with tuition in every sentence.
4. Says reimbursement may describe repayment for expenses unrelated to a refund policy.
5. Says to treat the repair as a hypothesis and evaluate it on both useful matches and misleading matches.

**Source:** The synonym miss and a dangerous repair

## ES-ch07.26

Claude proposes a synonym map in seconds. Explain who proposes and who decides, why, and what you must record when you adopt it.

**Points:** 5

**Rubric (1 point each):**

1. Says proposing is Claude's work and deciding is yours.
2. Says whether two words are interchangeable is a fact about the policy and population the words describe, not about the words.
3. Says a proposal does not enter the vector until you encode it.
4. Says you record the exact map, whether it applies to queries, documents, or both, and its provenance.
5. Notes that applying the map only to the query creates an asymmetry, while expanding both sides can change counts and vector lengths.

**Source:** The synonym miss and a dangerous repair

## ES-ch07.27

The query is "tuition refund eligibility" and the document is "fee reimbursement for travel". Compute the cosine before and after applying the map tuition-to-fee and refund-to-reimbursement to the query only, and say what the change does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Gives the cosine before the map as 0.0, because the two texts share no token.
2. Gives the mapped query as "fee reimbursement eligibility".
3. Gives the dot product as 2 (fee and reimbursement) with lengths sqrt(3) and sqrt(4).
4. Gives the cosine after the map as 2 / sqrt(12), about 0.5774.
5. States that the rise does not mean the travel document answers the tuition-refund question, and labels it a constructed counterexample rather than evidence about a real university rule.

**Source:** The synonym miss and a dangerous repair

## ES-ch07.28

Explain the tension between recall and review burden, and say who prices it and what the chapter does and does not establish about thresholds.

**Points:** 5

**Rubric (1 point each):**

1. Says more recall can return more potentially useful material.
2. Says more recall can also return more distractors.
3. Says more restrictive matching can omit paraphrases.
4. Says the balance depends on the downstream task and on the cost of missing versus reviewing candidates, and that cost is the task owner's to price.
5. Says the chapter does not establish one universal threshold, and that an abstention rule faces the same problem.

**Source:** The synonym miss and a dangerous repair

## ES-ch07.29

A selected passage says office hours are available by appointment. A generated answer says they occur every Tuesday at two. Use this to explain the difference between relevance and entailment.

**Points:** 5

**Rubric (1 point each):**

1. Says retrieval asks which documents are similar enough under a rule to inspect first.
2. Says evidence review asks whether a selected passage supports a specific claim.
3. Says the passage is relevant to office hours.
4. Says the Tuesday-at-two claim is an unsupported addition because the passage does not supply the time.
5. Says the second question cannot be collapsed into the first merely because the score is precise.

**Source:** Relevance and entailment are separate checks

## ES-ch07.30

Describe how to review a generated answer claim by claim, and explain why a document-level citation is not enough.

**Points:** 5

**Rubric (1 point each):**

1. Says to quote or identify the exact source passage within the permitted material.
2. Says to state the answer claim.
3. Says to record whether the passage supports, contradicts, or does not resolve the claim.
4. Says a document-level citation is not support for every sentence in a paragraph.
5. Distinguishes "has a source identifier" from "is supported by that source".

**Source:** Relevance and entailment are separate checks

## ES-ch07.31

Why is it a problem if the process that wrote a sentence also vouches for its citation? Describe what Claude can contribute to the support check and what stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Says it gives you the first opinion run twice.
2. Says Claude can quote the passage.
3. Says Claude can propose a label and hunt for the sentence that would change it, saving you the search.
4. Says the label that goes in the table is the one you gave after reading the original.
5. Says that when you disagree with Claude's label, you write down the sentence that decides it.

**Source:** Relevance and entailment are separate checks

## ES-ch07.32

The chapter borrows a line from Irreducibly Human about when a human correction adds signal. Explain the line, give one weak and one strong way to write an override of Claude's label, and say what the chapter warns about the line's origin.

**Points:** 5

**Rubric (1 point each):**

1. Says a human correction adds signal when it names what the machine misses in this kind of case.
2. Says it adds noise when it is a wordless hunch.
3. Gives "I read it differently" as a weak override that is not a check.
4. Gives a strong override such as "This sentence names the term but not the date".
5. Notes that the book draws the line for validated imaging systems and statistical forecasts, not source labeling, so it is a discipline for writing overrides, not evidence about Claude.

**Source:** Relevance and entailment are separate checks

## ES-ch07.33

The format contract from Chapter 2 can require source identifiers. Explain what that does and does not guarantee, and what the correct output may be when the selected context is insufficient.

**Points:** 5

**Rubric (1 point each):**

1. Says requiring source identifiers is useful for traceability.
2. Says "has a source identifier" is a different obligation from "is supported by that source".
3. Says a structural pass names only the obligation it passed.
4. Says that when the selected context is insufficient, the correct result may be an abstention or a request for another source.
5. Says not to fill the gap with a plausible answer and cite the nearest passage, and that the task packet should specify how insufficiency is represented.

**Source:** Relevance and entailment are separate checks

## ES-ch07.34

A teammate says: "Just give Claude the whole corpus; more text is always safer." Respond using the chapter, including how the Anthropic context-engineering article is meant to be used.

**Points:** 5

**Rubric (1 point each):**

1. Says more text can include the missing evidence.
2. Says more text can also contain contradictions, irrelevant material, and more content than a bounded task should expose.
3. Says context selection is an engineering and data-governance decision.
4. States the goal as sufficient, authorized evidence with an inspectable selection path.
5. Says the article treats context as a designed collection of instructions, tools, data, and history, and is used to compare selection strategies, not to claim count vectors implement Claude's context mechanisms.

**Source:** Relevance and entailment are separate checks; Anthropics

## ES-ch07.35

Summarize half one of the gate: the design decisions, the contract, and what the retriever may claim.

**Points:** 5

**Rubric (1 point each):**

1. States the design: count vectors over lowercase `\b\w+\b` tokens, cosine as the score, zero scores dropped before the cutoff, ties broken by document key, default k of two.
2. Says the design is written down so the decisions are on your record and not inherited defaults.
3. States the contract: cosine is never negative, identical direction scores one, and an empty side scores 0.0 as a convention.
4. States that `retrieve` returns only positive scores, best first, equal scores in key order, at most k rows, and refuses a k that is not a positive integer.
5. States that the retriever may claim only a ranking of overlap under one representation, not relevance in a reader's sense, support, or completeness.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.36

The gate lists wrong versions of the retriever that your tests must catch. Name five of them and explain how to confirm that your tests really catch them.

**Points:** 5

**Rubric (1 point each):**

1. Names sorting worst-first.
2. Names breaking ties by insertion order.
3. Names checking k with isinstance so that True slips through.
4. Names two more from: ignoring k beyond a fixed size, dropping the normalization, dropping the zero filter.
5. Says to confirm by mutating a copy of the reference, and that a wrong version that survives means the gate is not finished.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.37

The gate says to read the lesson's six tests against your list of wrong versions before trusting them. Describe the gaps the chapter finds and why each lets a wrong version through.

**Points:** 5

**Rubric (1 point each):**

1. Says the relevance test has a single positive-scoring document.
2. Explains that best-first and worst-first sorts return the same thing for a single document.
3. Says no test has two equal scores, so insertion-order ties go unnoticed.
4. Says the invalid-k test uses zero, which an isinstance check also rejects, so the Boolean slip-through goes unnoticed.
5. Says no test makes k smaller than the number of positive matches, so ignoring k goes unnoticed.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.38

Describe the expected-source list in half two of the gate: what it contains, when it is written, and why you should not ask Claude to write it first.

**Points:** 5

**Rubric (1 point each):**

1. Lists the contents: title or identifier, owner, version or date, why each source is authorized, and the number of items expected.
2. Says it is written before you ingest anything.
3. Says it is dated.
4. Says Claude's answer would be built from the task description you gave it, the same material you are trying to check.
5. Says the book warns that a fluent AI-generated frame contains no information, because the AI started from the same documentation you did.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.39

Explain how to write the claims list and the evidence rules in the gate, including the four row labels and who may mark a row supported.

**Points:** 5

**Rubric (1 point each):**

1. Says the claims list has one sentence per question the report must answer.
2. Says each claim must be small enough for a single passage to support or not, and a sentence with an "and" is split.
3. Defines supported as a quoted passage stating the claim, within its scope, date, and population.
4. Names the other labels: contradicted, insufficient (on topic but unresolved, with the missing piece named), and not reviewed.
5. Says the person who read the original authorized source may mark a row supported, and that when the sources do not say, the report must say so.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.40

The abstention rule "refuse when no document scores above zero" is proposed. Explain what it does well, where it fails in both directions, and what the gate asks you to write.

**Points:** 5

**Rubric (1 point each):**

1. Says it avoids answering from an empty selection in the synonym fixture.
2. Says positive overlap can still be insufficient, so the rule establishes no support.
3. Says raising the threshold excludes some useful short passages.
4. Says the gate asks for the positive-scoring case the rule wrongly lets through and the case a stricter threshold wrongly refuses.
5. Says the gate also asks what review remains.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.41

The chapter says "design first is not design frozen". Explain what you do if ingestion turns up a source you did not list, or a listed source is absent, and what the packet may claim at the end.

**Points:** 5

**Rubric (1 point each):**

1. Says the finding reopens the gate.
2. Says you keep the original list, dated.
3. Says you add the revision with its reason.
4. Says the gap between what you expected and what you found is the most informative thing the exercise produces.
5. Gives the allowed claim form, "under this corpus and these rules, these claims were supported by these passages", and says not to call the packet comprehensive unless the inventory justifies the word.

**Source:** The gate: write the source list and the evidence rules first

## ES-ch07.42

Describe the Build It sequence and say why you write your own version before opening the reference.

**Points:** 5

**Rubric (1 point each):**

1. Says your own version is your baseline: the record of what you understood before Claude touched anything.
2. Says you implement `vector`, verify the count for repeated mixed-case text, and calculate the office-hours cosine by hand before running it.
3. Says you preserve the tokens, counts, dot product, norms, and final score rather than a lone decimal.
4. Says you implement retrieval with positive-score filtering and deterministic sorting, and add a tie test, the synonym miss, and the tests the lesson's six leave open.
5. Says you should not describe the total as complete retrieval coverage, and any synonym map stays in your learner version with its provenance.

**Source:** Build It: preserve the scoring path

## ES-ch07.43

Describe how you conduct Claude Code against your gate, including what you give it, what you do with the result, and what you preserve.

**Points:** 5

**Rubric (1 point each):**

1. Says you give it the contract, the test list, and the audit-view specification, not your implementation.
2. Says you run your tests on what it returns, yourself.
3. Says a failing test is often a gap in your gate, which Claude cannot see because it has only what you wrote.
4. Says you preserve the transcript: prompt, plan, diff, commands, outputs, date, and displayed model label.
5. Says that if a session failed or did not run, you record that rather than substituting a fixture.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## ES-ch07.44

After Claude Code returns an implementation, the chapter asks for a comparison with your baseline and a deliberately wrong version. Explain how to read each outcome.

**Points:** 5

**Rubric (1 point each):**

1. Says a boundary Claude handled that you missed is a revision to your gate.
2. Says a boundary Claude silently ignored is a defect your tests failed to catch.
3. Says you ask Claude to propose a deliberately wrong version that still passes your tests.
4. Says you check by hand whether it does, and that if it does, your list was too weak and you found out cheaply.
5. Says you verify every suggestion Claude makes about your representation against the displayed mechanism.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## ES-ch07.45

Explain what the task packet must contain and how the corpus should be built, including the limit on what you may upload.

**Points:** 5

**Rubric (1 point each):**

1. Says the task packet names the goal, permitted sources, output format, exclusions, and acceptance checks.
2. Says it states how the selected passages were obtained.
3. Says the corpus is built from material you are authorized to use, recording source identity, version or date, and inclusion criteria.
4. Says not to upload restricted material merely because the interface can accept it.
5. Says that, under the Chapter 5 data boundary, who may read what is a decision people make, not one the interface makes.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## ES-ch07.46

You run retrieval and discover that a required answer claim has no sufficient evidence in the selected context. Describe what the chapter tells you to do, and what it tells you not to do.

**Points:** 5

**Rubric (1 point each):**

1. Says to inspect both selected and omitted candidates using the audit view.
2. Says to compare the inventory with the expected-source list dated before ingestion.
3. Says to identify, for each required claim, whether sufficient evidence appears in the selected context.
4. Says to revise the query, representation, corpus, or task scope.
5. Says not to revise the final prose alone and assume the evidence problem disappeared.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## ES-ch07.47

You may run your task packet through Claude Cowork. Explain what you must preserve, what you may not claim, and what to do if the interface is unavailable.

**Points:** 5

**Rubric (1 point each):**

1. Says to preserve actual interface details and output.
2. Says the chapter cannot claim which internal retrieval steps the product used.
3. Says to compare your explicit packet and evidence table with the interface task as an observed workflow, not as proof of internal equivalence.
4. Says that if the interface is unavailable, you ship the offline corpus, retrieval results, and proposed packet.
5. Says to mark the generation portion not run, with no fabricated results or direct API spending.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## ES-ch07.48

A report contains a claim that the evidence does not support. Using the chapter's debugging table, describe the order in which you investigate, the first stage where rewriting the answer helps, and when debugging ends.

**Points:** 5

**Rubric (1 point each):**

1. Says to start upstream rather than rewriting the answer repeatedly, beginning at the top with eligibility.
2. Gives the order of the remaining stages: ingestion, representation, scoring and cutoff, selection into context, use, claim.
3. Says to preserve the score of a document that fell below k rather than pretending it was never considered.
4. Identifies use as the first stage where rewriting the answer helps, and says support is still a separate review.
5. Says debugging ends when the stated conclusion matches the actual evidence, not when every stage has produced a green marker.

**Source:** Ship It: the source-grounded task packet (Debug the pipeline in the order information moves)

## ES-ch07.49

For the first five stages of the debugging table (eligibility, ingestion, representation, scoring and cutoff, selection into context), say what a failure looks like and whose repair it is. Which of the five does the reference implementation never demonstrate?

**Points:** 5

**Rubric (1 point each):**

1. Says an eligibility failure is a source excluded by a permission or scope decision, which retrieval cannot legally repair, and the claim may need narrowing.
2. Says an ingestion failure is a skipped format or the wrong folder read, and that the reference starts from a constructed dictionary and never demonstrates ingestion.
3. Says a representation failure is the synonym case where the vectors share no coordinate, and no prompt after retrieval repairs it.
4. Says a scoring and cutoff failure is a positive-overlap document ranked below the cutoff, and that a larger k adds review burden to record.
5. Says a selection-into-context failure is another filter or manual choice narrowing what Claude saw, which you record by naming each narrowing.

**Source:** Ship It: the source-grounded task packet (Debug the pipeline in the order information moves)

## ES-ch07.50

The chapter says its seven-stage decomposition is "not a claim that production systems implement these modules". Explain what the decomposition is, and what you can still record when an interface's internals are unavailable.

**Points:** 5

**Rubric (1 point each):**

1. Says it is a decomposition of the artifact you can inspect.
2. Says it does not claim production systems implement these modules.
3. Says a real interface may combine operations.
4. Says a real interface may keep internals unavailable.
5. Says you can still record the source boundary, visible inputs, selected context when exposed, output, and your independent evidence review.

**Source:** Ship It: the source-grounded task packet (Debug the pipeline in the order information moves)

## ES-ch07.51

The reference treats each dictionary value as a complete document. Explain what changes if you add chunking, covering the risks at chunk boundaries, the effect of chunk size and overlap on ranking, and the identifiers you need.

**Points:** 5

**Rubric (1 point each):**

1. Says adding chunks introduces a selection decision before cosine ranking, and it is yours.
2. Says a claim and its qualification can fall in adjacent chunks, so retrieving only the claim-shaped fragment can make a passage look stronger than its source.
3. Says a large chunk can dilute lexical overlap with unrelated terms and lower its normalized score.
4. Says chunk overlap can reduce some boundary misses but duplicates tokens and candidates and influences ranking and context volume, so the choice is recorded.
5. Says chunk identifiers must preserve source identity and location, because a citation to chunk-7 is hard to audit otherwise.

**Source:** Ship It: the source-grounded task packet (Chunk boundaries create another representation)

## ES-ch07.52

Describe a harmless chunking experiment the chapter suggests, and say what conclusion the chapter wants you to draw from it and what conclusion it does not.

**Points:** 5

**Rubric (1 point each):**

1. Describes a corpus example with two adjacent sentences, one stating a policy and the next naming an exception.
2. Says to compare retrieval when the two sentences stay together and when they are split.
3. Says to state whether the answer still needs the omitted qualification.
4. Says the reviewer needs enough surrounding text to see whether a qualification was cut away.
5. Says these are hypotheses to test on declared text, not reasons to assert that one chunk size is correct.

**Source:** Ship It: the source-grounded task packet (Chunk boundaries create another representation)

## ES-ch07.53

Design the claim-to-source evidence table the chapter describes. State its columns, how it must treat rows that lack support, and why.

**Points:** 5

**Rubric (1 point each):**

1. Says it needs more than claim and citation columns.
2. Lists the added columns: the exact supporting passage or stable location, a reviewer judgment, and a note about scope or missing qualification.
3. Says the judgment distinguishes supported, contradicted, insufficient, and not reviewed, as defined in the gate.
4. Says an insufficient row is actionable evidence: narrow the sentence, retrieve more material, or abstain.
5. Says that if the table cannot represent a gap, it pressures the reviewer to hide one, so rows are not forced into supported.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## ES-ch07.54

Using the office-hours hypothetical, show how atomic claims and row provenance work in the evidence table.

**Points:** 5

**Rubric (1 point each):**

1. Labels "appointments are mentioned" as supported by the supplied sentence.
2. Labels "appointments occur Tuesday at two" as insufficient because the time is absent.
3. Explains that a paragraph-level judgment could conceal that one part is grounded while another is invented.
4. Says a string entered by the learner is a constructed fixture.
5. Says a passage copied from a real policy needs an authorized source, a version or retrieval date where relevant, and enough location information to revisit it, and the roles are not merged unlabeled.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## ES-ch07.55

Explain the two disciplines that keep the packet honest about what produced a selection: preserving the query, and distinguishing the source collection from the context finally shown to Claude.

**Points:** 5

**Rubric (1 point each):**

1. Says to preserve the query that actually produced the selection.
2. Says a revised query may retrieve better evidence but its success cannot be attributed to the original run.
3. Says to keep both queries, label the revision, and record any synonym a human supplied after seeing the failure.
4. Gives the collection-versus-context example: the corpus may hold twenty items, the retriever may return two, and the interface may receive one.
5. Says a complete selection record names each narrowing, and without it a reviewer may blame the generator for information the workflow never supplied.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## ES-ch07.56

The chapter says the result is "accountable context", not maximal context. Define it, explain how the packet's parts relate, and say what case the packet must include.

**Points:** 5

**Rubric (1 point each):**

1. Defines accountable context as enough authorized material to support the bounded answer, an explicit record of what was left out, and a route for saying the evidence is insufficient.
2. Says the corpus inventory shows what was eligible and the retrieval record shows what the algorithm selected.
3. Says the task packet shows what Claude was permitted and asked to use, and the evidence table connects claims to exact passages and records gaps.
4. Says the dated expected-source list sits in front of all of them.
5. Says the packet must include at least one omitted or insufficient case, explaining whether the source was absent from the corpus, scored zero, or fell below k.

**Source:** Ship It: the source-grounded task packet (The packet, assembled)

## ES-ch07.57

Write the sign-off the chapter describes in prose: what each verb may and may not claim, what the "Not checked" line is for, and when you withhold.

**Points:** 5

**Rubric (1 point each):**

1. Says "retrieved" describes what the selection rule returned and "quoted" describes what you copied.
2. Says "supported" describes a claim and a passage you actually compared.
3. Says "verified" and "comprehensive" need more than this packet offers unless you did the work behind them.
4. Says the "Not checked" line does the work, and that an AI-written sign-off leaves it out because the system has no record of the sources you never opened or the file that failed to load.
5. Says you write the sign-off from your record, and if your evidence does not support signing, you withhold.

**Source:** Ship It: the source-grounded task packet (The packet, assembled)

## ES-ch07.58

Choose two rows from the driver's-seat table and, for each, say what Claude should do, what you should do, and why it stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Correctly describes Claude's role in the first chosen row, such as doing the ranking fast and showing every score, or implementing the retriever from the contract.
2. Correctly describes your role in that row, such as reading the full audit view rather than only the winners, or building your own baseline first and running your tests on its version.
3. Gives the chapter's reason for that row, such as omissions being invisible in a list of winners, or that you cannot audit a ranking you never computed.
4. Correctly describes Claude's and your roles in the second chosen row, such as Claude proposing a synonym map, chunk size, or larger k with cases that might break it while you decide and record where each came from, or Claude proposing a label while you label first from the original.
5. Gives the chapter's reason for the second row, such as that interchangeability is a fact about the policy and population and not the words, or that what the source means in the world, its scope, date, and who it governs, is your reading.

**Source:** Ship It: the source-grounded task packet (The driver's seat)

## ES-ch07.59

The chapter asks you to record one task you delegated and one judgment you retained. What evidence counts, and what does it mean if you cannot produce it?

**Points:** 5

**Rubric (1 point each):**

1. Says the packet records one delegated task and one retained judgment.
2. Names the Claude Code transcript showing what you gave it as evidence.
3. Names the dated expected-source list and its comparison with the inventory as evidence.
4. Names the rows where your label differed from Claude's proposal, or where you changed your mind, as evidence.
5. Says that if you cannot point to the transcript line or the edit that shows each, the split happened in your head and not in the record.

**Source:** Ship It: the source-grounded task packet (The driver's seat)

## ES-ch07.60

Describe the Verify and reflect tasks: the expected-source gap, the claim audit, and the vocabulary check.

**Points:** 5

**Rubric (1 point each):**

1. Says you recalculate one cosine score independently and preserve the interpreter and input corpus rather than reporting a score without its representation.
2. Says you compare the expected-source list with the inventory and write the gap in one sentence (a source expected and not found, one found and not expected, or neither).
3. Says you do not rewrite the list to match, because the gap is the learning.
4. Says you audit one claim against the original source, not only the selected chunk, because chunk boundaries can omit qualifications, and revise or remove the claim if it exceeds the passage.
5. Says "relevant" should refer to a scoring or human topical judgment you can describe, and "supported" to a claim-evidence relationship you actually inspected, and they are not swapped because both sound favorable.

**Source:** Verify and reflect

## ES-ch07.61

The query is "office hours". Document d1 is "office hours appointment" and d2 is "office hours". Predict and compute what happens to both scores and to the ranking when "appointment" is added to the query, and explain how the dot product and norm each change.

**Points:** 5

**Rubric (1 point each):**

1. Gives the scores before the change: d2 is 1.0 and d1 is about 0.8165.
2. Gives d1 after the change as 1.0 (dot product 3, both lengths sqrt(3)).
3. Gives d2 after the change as about 0.8165 (dot product 2, lengths sqrt(3) and sqrt(2)).
4. States that the ranking reverses so d1 ranks above d2.
5. Explains that the query's length changes for both documents, while the dot product changes only for d1 (from 2 to 3) and stays 2 for d2.

**Source:** Assessments - ungraded practice

## ES-ch07.62

The closing section describes what you can now trace and what the three jobs look like in this chapter. Explain why a zero-overlap document can be relevant and a high-overlap document insufficient, and how the packet shows you did conduct, check, and drive.

**Points:** 5

**Rubric (1 point each):**

1. Says a zero-overlap document may be semantically related, and a high-overlap document may still be insufficient.
2. Says this is not a contradiction, because the score and the support review have different jobs.
3. Says conducting means you wrote the retriever's contract, the tests that must fail the wrong versions, and a dated list of expected sources before Claude implemented or ranked anything.
4. Says checking means you refused to let a high score stand in for support and traced what was excluded before treating a selected passage as sufficient.
5. Says driving means you handed Claude the scoring, implementation, and quoting while keeping the list of what should exist, the label on each claim, and the choice to narrow or abstain, and you signed or withheld.

**Source:** What you can now trace

## ES-ch07.63

Explain the access-boundary assumption from the companion Computational Skepticism chapter and how the chapter tells you to apply it to a passage in your corpus.

**Points:** 5

**Rubric (1 point each):**

1. States that a dataset's effective reach is its schema plus whatever its contents reference.
2. Says the claim is sharpest for reference-rich material such as email.
3. Says it is weak for a self-contained table of sensor readings.
4. Says to check whether a passage quotes, links, or defers to a document that is not on your source list.
5. Says that if it does, the passage cannot be read as complete without that document, and the dependency belongs in the packet as an unresolved item.

**Source:** Computational Skepticism

## ES-ch07.64

Explain the row-trace step and what the chapter says to do when the original source is unreachable.

**Points:** 5

**Rubric (1 point each):**

1. Says to follow one answer passage back to its original source.
2. Says that where the original is unreachable, you document the opacity.
3. Says the chapter counts documented opacity as a finding and not a failure of the procedure.
4. Says to record which of "not retrieved", "not in the corpus", and "not true" you could establish and which you could not.
5. Says these are two questions for the packet and not a measurement of this retriever or corpus.

**Source:** Computational Skepticism
