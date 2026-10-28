# Chapter 7: Retrieval and Cowork

## MA-ch07.1

Check each statement that is true about the two constructed cases that open the chapter (the office-hours query and the tuition-refund query). Each statement is worth 1 point (5 points total).

- [ ] A. A document saying "Office hours by appointment" can rank highly for the query "office hours" because the shared words are visible to the retriever.
- [ ] B. For the query "tuition refund", when the only relevant document says "fee reimbursement", the retriever returns nothing because its representation sees no shared token.
- [ ] C. In the tuition-refund case, the retriever returns the fee-reimbursement document at a low rank with a small positive score.
- [ ] D. A human reader would also fail to see the relationship between "tuition refund" and "fee reimbursement".
- [ ] E. Both cases are presented as measurements taken from a deployed Claude Cowork system.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The first case ranks the document highly on visible shared words.
- B: In the second case the retriever returns nothing because no token is shared.
- C: The document is not returned at all, at any rank.
- D: A human reader can see the relationship.
- E: Both are constructed cases from the course's offline exercise.

**Source:** Chapter 7 (opening, before the first section)

## MA-ch07.2

Check each statement that is true about the results recorded by the research run. Each statement is worth 1 point (5 points total).

- [ ] A. The run records a cosine similarity of 2 / sqrt(6), approximately 0.8164965809, between "office hours" and "office hours appointment".
- [ ] B. The run records no result for the synonym pair.
- [ ] C. The run records deterministic ordering for tied scores.
- [ ] D. The recorded results are measurements of how Claude Cowork retrieves documents.
- [ ] E. The recorded results show how neural embeddings treat synonyms.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: This is the recorded score for the published pair.
- B: The synonym pair produces no result under the count-vector implementation.
- C: Tied scores come back in a deterministic order.
- D: They are results of the displayed implementation, not measurements of Cowork.
- E: They are not measurements of neural embeddings either.

**Source:** Chapter 7 (opening, before the first section)

## MA-ch07.3

Check each statement that is true about what happens when Claude sits downstream of a retrieval step. Each statement is worth 1 point (5 points total).

- [ ] A. In the synonym case, a step quietly dropped the only source that mattered, and nothing in the output says so.
- [ ] B. If the evidence reaching Claude is incomplete, Claude signals the gap through hedged wording in its answer.
- [ ] C. What Claude receives includes a note saying what was left out.
- [ ] D. A fluent answer built on incomplete evidence reads differently from one built on complete evidence.
- [ ] E. Once the retriever ranks the "by appointment" passage highly, no human question remains about whether it says when to show up.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The chapter describes exactly this silent drop.
- B: Claude writes a fluent answer from whatever reached it, without flagging gaps.
- C: Nothing it received says what was left out.
- D: The sentence reads the same whether the evidence was complete or not.
- E: A human still has to ask whether "by appointment" says when to show up.

**Source:** Chapter 7 (opening, before the first section)

## MA-ch07.4

Check each statement that is true about the three jobs the chapter applies to retrieval. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 1 named the three jobs that stay with you: conduct, check, drive.
- [ ] B. Retrieval is where these jobs bite hardest, because it makes the most decisions and leaves the fewest traces.
- [ ] C. Conduct means you decide what reaches Claude's context before the task runs.
- [ ] D. Check includes the points that relevance is not entailment and that ranking turns scores into omissions.
- [ ] E. Drive means Claude decides what a source means in the world.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The chapter attributes the three jobs to Chapter 1.
- B: Many decisions and few traces make retrieval the hardest case.
- C: Conduct is the pre-task decision about Claude's context.
- D: Both phrases are the chapter's statement of Check.
- E: Claude ranks and quotes; what a source means in the world is your reading.

**Source:** Chapter 7 (opening, before the first section)

## MA-ch07.5

Check each statement that is true about how Chapter 7 relates to the earlier chapters and to the assistant it assumes. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 6 reviewed a proposed code change against its diff and tests, and Chapter 7 moves earlier to ask which source material reached the system.
- [ ] B. A clean review packet can recover a passage that was ranked out of the selected context.
- [ ] C. The Python retriever runs offline with the standard library and spends no direct API credits.
- [ ] D. If you do not perform an actual interface task, you may write the output Claude Cowork would probably have produced so the packet looks complete.
- [ ] E. If you do perform an actual interface task, you should preserve its sources, prompt, output, and date.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The chapter places retrieval earlier in the pipeline than the Chapter 6 review.
- B: A review packet cannot recover a passage that was never in the corpus or was ranked out.
- C: The retriever is offline and uses the standard library only.
- D: Without a live run, keep the packet labeled as proposed rather than inventing one.
- E: Those four items are what a real interface task must preserve.

**Source:** Chapter 7 (opening, before the first section)

## MA-ch07.6

Check each statement that is true about what the chapter says you should be able to do after working through it. Each statement is worth 1 point (5 points total).

- [ ] A. Turn short text into a token-count vector.
- [ ] B. Calculate cosine similarity by hand.
- [ ] C. Predict ranking changes and explain deterministic tie-breaking.
- [ ] D. Distinguish no overlap from absence in the corpus.
- [ ] E. Certify that a selected passage supports a claim from its cosine score.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The first listed ability.
- B: Hand calculation is a listed ability.
- C: Both are listed together.
- D: The chapter lists this distinction.
- E: The chapter lists identifying a claim unsupported by selected passages, and a score is not support.

**Source:** What you will be able to do

## MA-ch07.7

Check each statement that is true about the seven narrowing stages between a stack of documents and a sentence in a report. Each statement is worth 1 point (5 points total).

- [ ] A. Eligibility, the first stage, decides which sources may be used at all.
- [ ] B. Ingestion decides whether an eligible file became text in the corpus.
- [ ] C. Representation is decided by the scoring rule and k.
- [ ] D. Use, the stage where the answer relies on shown passages, is decided by you rather than by Claude.
- [ ] E. The path has five stages.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Eligibility is set by permission and scope.
- B: Ingestion is whether the eligible file became corpus text.
- C: The vectorizer decides representation; the scoring rule and k decide scoring and cutoff.
- D: Claude decides use, while generating.
- E: There are seven stages.

**Source:** What reaches Claude is the end of a chain of omissions

## MA-ch07.8

Check each statement that is true about what the seven stages leave visible in the final prose. Each statement is worth 1 point (5 points total).

- [ ] A. Five of the seven stages leave nothing in the final prose.
- [ ] B. Use leaves a citation in the prose, if you required one.
- [ ] C. A citation shows that the cited passage supports the claim.
- [ ] D. The Claim stage shows up in the prose through its verbs.
- [ ] E. A reviewer who starts by judging the answer starts before any of the seven decisions have been made.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Eligibility, ingestion, representation, scoring and cutoff, and selection leave nothing.
- B: A citation is the only trace of Use, and only if required.
- C: A citation asserts a relationship rather than showing it.
- D: The verbs are what the Claim stage leaves.
- E: All seven decisions have already happened when you read the answer, and none is visible.

**Source:** What reaches Claude is the end of a chain of omissions

## MA-ch07.9

Check each statement that is true about the chapter's use of Computational Skepticism for AI on missing data. Each statement is worth 1 point (5 points total).

- [ ] A. The book's point is that you cannot compute the missingness of rows that never existed.
- [ ] B. The book's central question is why there are exactly N rows, and what N was supposed to be.
- [ ] C. The join that silently dropped differently formatted identifiers is presented as a single sourced incident.
- [ ] D. In the chapter's analogy, the score table plays the role of the join.
- [ ] E. In the chapter's analogy, a score table is precise about what arrived and silent about what did not.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The chapter quotes this as the point it keeps returning to.
- B: The N question is the move the chapter borrows.
- C: The illustration is labeled a composite of familiar failures, not a single sourced incident.
- D: Ingestion is the join; the score table is the histogram.
- E: That is how the chapter describes the score table.

**Source:** What reaches Claude is the end of a chain of omissions

## MA-ch07.10

Check each statement that is true about the boundary the chapter draws using the first tier of Irreducibly Human. Each statement is worth 1 point (5 points total).

- [ ] A. Finding a passage is a pattern task, where the machine is better at the task as specified.
- [ ] B. The human's remaining job ends once the machine has finished the pattern task.
- [ ] C. Deciding whether a found passage answers the question is also a pattern task.
- [ ] D. Retrieval is specified by your query, representation, corpus, and k.
- [ ] E. A ranking can be excellent only if the specification behind it is right.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The book states the boundary this way for the first tier.
- B: The human notices when the specification is wrong or the task only looked like a pattern task.
- C: Deciding whether a passage answers the question is not a pattern task.
- D: Those four items are the specification.
- E: The ranking can be excellent while the specification is wrong.

**Source:** What reaches Claude is the end of a chain of omissions

## MA-ch07.11

Check each statement that is true about what the count-vector representation keeps and discards. Each statement is worth 1 point (5 points total).

- [ ] A. "Office office hours" becomes a mapping in which office has count two and hours has count one.
- [ ] B. "hours office" and "office hours" receive the same vector.
- [ ] C. "Office" and "office" are separate coordinates because capitalization is preserved.
- [ ] D. Most coordinates are zero, so the implementation stores only the tokens that appear.
- [ ] E. Discarding word order is a failure that occurs after retrieval.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The text is lowercased and the occurrences are counted.
- B: Frequency is kept and word order is discarded.
- C: The text is lowercased first, so capitalization is discarded.
- D: Only tokens that appear are stored.
- E: It is a consequence of the information the representation retains, not a failure after retrieval.

**Source:** A representation decides what can match

## MA-ch07.12

Check each statement that is true about tokenization with the regular expression `\b\w+\b`. Each statement is worth 1 point (5 points total).

- [ ] A. An apostrophe splits "don't" into don and t.
- [ ] B. A hyphen splits "fee-reimbursement" into fee and reimbursement.
- [ ] C. An underscore does not split a token, because it counts as a word character.
- [ ] D. The behavior of `\w` follows Python's regular-expression rules, not a universal linguistic analysis.
- [ ] E. The chapter's tokenization results can be assumed to hold for multilingual and code-heavy corpora.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The chapter traces "don't stop" into don, t, stop.
- B: The hyphen is not a word character.
- C: The underscore counts as a word character, so it splits nothing.
- D: The chapter says this explicitly.
- E: Do not infer performance for such corpora without testing their actual inputs.

**Source:** A representation decides what can match

## MA-ch07.13

Check each statement that is true about the limits of the count-vector representation and of the test `vector("Hi HI")["hi"] == 2`. Each statement is worth 1 point (5 points total).

- [ ] A. The test checks both lowercasing and counting for one case.
- [ ] B. The test proves that capitalization is irrelevant to meaning.
- [ ] C. Count vectors sacrifice word order and synonymy in exchange for visible overlap and transparent arithmetic.
- [ ] D. The right question about a representation is whether it is intelligent.
- [ ] E. Performance on adversarial corpora can be inferred from the chapter's short English fixtures.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: It checks both behaviors, but only for one case.
- B: It does not show that capitalization never matters.
- C: Those are the stated trade-offs of count vectors.
- D: The right question is whether the retained features suit the evidence-selection task and whether the misses are visible.
- E: Such inference needs testing on the actual inputs.

**Source:** A representation decides what can match

## MA-ch07.14

A learner tokenizes "Don't stop, don't STOP" with the chapter's `vector` function (lowercase, then `\b\w+\b`, then Counter). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The resulting Counter has don with count 2.
- [ ] B. The resulting Counter has "don't" as a single key.
- [ ] C. The resulting Counter has stop with count 2.
- [ ] D. The resulting Counter has t with count 2.
- [ ] E. The resulting Counter keeps the comma and the apostrophe as tokens.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The text yields don twice.
- B: The apostrophe splits the contraction into don and t.
- C: stop and STOP lowercase to the same token.
- D: Each "don't" contributes one t.
- E: Punctuation is not captured by `\w+`.

**Source:** A representation decides what can match

## MA-ch07.15

Check each statement that is true about the dot product and vector length used for cosine similarity. Each statement is worth 1 point (5 points total).

- [ ] A. The dot product multiplies matching coordinates and sums the products.
- [ ] B. Tokens absent from one side contribute that token's count from the other side to the sum.
- [ ] C. The dot product shrinks as vectors grow, which is why it is normalized.
- [ ] D. The implementation normalizes the dot product by the vectors' lengths.
- [ ] E. The Euclidean length of q is the sum of its counts.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: That is the definition given for q . d.
- B: Tokens absent from one side contribute zero.
- C: The dot product also grows when vectors grow.
- D: Cosine divides by both lengths.
- E: The length is the square root of the sum of squared counts.

**Source:** Cosine from first principles

## MA-ch07.16

Check each statement that is true about the published example: the query "office hours" against the document "office hours appointment". Each statement is worth 1 point (5 points total).

- [ ] A. The query's length is the square root of 2.
- [ ] B. The document's length is the square root of 3.
- [ ] C. The dot product is 2.
- [ ] D. The cosine is 2 / sqrt(6), approximately 0.8165.
- [ ] E. The dot product is 3, because the document has three tokens.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Two tokens with count one each give sqrt(2).
- B: Three tokens with count one each give sqrt(3).
- C: office and hours each contribute one.
- D: 2 / (sqrt(2) * sqrt(3)) = 2 / sqrt(6).
- E: Only shared tokens contribute to the dot product, so it is 2.

**Source:** Cosine from first principles

## MA-ch07.17

Check each statement that is true about what the hand calculation of 2 / sqrt(6) does and does not establish. Each statement is worth 1 point (5 points total).

- [ ] A. It establishes a lexical relationship under this representation.
- [ ] B. It proves that the document answers every question involving office hours.
- [ ] C. The Stanford information-retrieval text supports the normalized dot-product formulation used here.
- [ ] D. The Stanford text turns this small implementation into a complete production retrieval system.
- [ ] E. If an implementation disagrees with your hand-calculated score for this pair, you should trust the implementation over your arithmetic.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The chapter says it proves a lexical relationship under this representation.
- B: It does not show the document answers every question about office hours.
- C: The source supports the formulation.
- D: Our use remains a small lexical example.
- E: A differing implementation, yours or Claude's, is the one to distrust.

**Source:** Cosine from first principles

## MA-ch07.18

A query is "office hours". Check each statement that is true about its cosine against the documents named. Each statement is worth 1 point (5 points total).

- [ ] A. Against "office hours by appointment" (four tokens, each count one), the dot product is 2.
- [ ] B. Against "office hours by appointment", the cosine is 2 / (sqrt(2) * 2), about 0.7071.
- [ ] C. Against "office hours office hours" (office 2, hours 2), the cosine is 1.0, because identical direction scores one whatever the lengths.
- [ ] D. Against "office" alone, the cosine is 0.5.
- [ ] E. Against "hours office", the cosine is lower than against "office hours" because the word order differs.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: office and hours each contribute one.
- B: The document length is sqrt(4) = 2, giving 2 / (1.414 * 2).
- C: The dot product is 4 and the lengths are sqrt(2) and sqrt(8), so the cosine is 4 / 4.
- D: The dot product is 1 and the lengths are sqrt(2) and 1, so the cosine is about 0.7071.
- E: Order is discarded, so "hours office" scores 1.0, the same as "office hours".

**Source:** Cosine from first principles

## MA-ch07.19

Check each statement that is true about what the `retrieve` function does. Each statement is worth 1 point (5 points total).

- [ ] A. It calculates every document's score before filtering.
- [ ] B. It returns the dropped documents together with the reason each was dropped.
- [ ] C. It takes the top k rows first and removes nonpositive scores afterwards.
- [ ] D. It always returns exactly k rows when the corpus holds at least k documents.
- [ ] E. It scores only the documents that share at least one token with the query.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The function scores every declared document and filters afterwards.
- B: The function does not return what it dropped or why.
- C: Nonpositive scores are removed before the top-k slice.
- D: It returns at most k rows, and only positive scores.
- E: Every document is scored; zero-overlap ones then score zero and are removed.

**Source:** Ranking turns scores into omissions

## MA-ch07.20

Check each statement that is true about how `retrieve` validates k. Each statement is worth 1 point (5 points total).

- [ ] A. A zero or negative k is rejected instead of silently returning nothing.
- [ ] B. A Boolean k is accepted because True equals 1.
- [ ] C. The type check asks for exactly int.
- [ ] D. An isinstance check would let True slip through as a valid k.
- [ ] E. A k of 0 returns an empty list without raising an error.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The function raises a ValueError for a k below 1.
- B: A Boolean is not accepted.
- C: The check is `type(k) is not int`.
- D: That is why the gate lists the isinstance check as a wrong version.
- E: A zero k is rejected with an error.

**Source:** Ranking turns scores into omissions

## MA-ch07.21

Check each statement that is true about how `retrieve` sorts its results. Each statement is worth 1 point (5 points total).

- [ ] A. The negative score in the sort key puts higher similarities first.
- [ ] B. The document key breaks ties in ascending order.
- [ ] C. Relying on incidental mapping order for ties makes equal-score selection easier to explain.
- [ ] D. Ties are broken by descending document key.
- [ ] E. The sort uses a single key, the score.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The first sort key is the negated score.
- B: The second sort key is the document key, ascending.
- C: Incidental mapping order would make equal-score selection harder to explain.
- D: The tie-break is ascending, not descending.
- E: The sort uses two keys.

**Source:** Ranking turns scores into omissions

## MA-ch07.22

Check each statement that is true about top-k selection among positive matches. Each statement is worth 1 point (5 points total).

- [ ] A. Top-k introduces an exclusion even among documents with positive scores.
- [ ] B. With k equal to one, a second relevant document can be omitted because another score is larger.
- [ ] C. With k equal to one, a second relevant document can be omitted because its tie-break key comes later.
- [ ] D. The returned list is selected candidates under a particular scoring and cutoff rule.
- [ ] E. The returned list is all the available evidence.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The cutoff removes some positive matches.
- B: A larger competing score pushes it out.
- C: An equal score with a later key also loses.
- D: That is how the chapter describes the returned list.
- E: The returned list is not all available evidence.

**Source:** Ranking turns scores into omissions

## MA-ch07.23

Check each statement that is true about the synonym miss between "tuition refund" and "fee reimbursement". Each statement is worth 1 point (5 points total).

- [ ] A. The two phrases have disjoint token sets under this vectorizer, so their dot product is zero.
- [ ] B. A human reader can see the relationship even though the retriever cannot.
- [ ] C. The zero-score document is excluded before top-k selection.
- [ ] D. A zero score is proof that the document is irrelevant.
- [ ] E. With a large enough k, the retriever would return the zero-score document.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: No token is shared, so the dot product is zero.
- B: This is the opening contrast between human and retriever.
- C: Nonpositive scores are removed before the k cutoff.
- D: Zero means no counted token overlap, not irrelevance.
- E: Zero-score documents are filtered out whatever k is.

**Source:** Ranking turns scores into omissions

## MA-ch07.24

Check each statement that is true about what a high similarity score does and does not show. Each statement is worth 1 point (5 points total).

- [ ] A. A document can repeat the query's terms while discussing a different policy, time period, or population.
- [ ] B. A high score therefore does not prove that the passage is adequate.
- [ ] C. Lexical similarity is a verdict on whether a passage answers the claim.
- [ ] D. A high score lets the next review skip reading the passage.
- [ ] E. A score precise to ten decimal places settles the question of support.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Repeated terms do not guarantee the same policy, period, or population.
- B: The chapter says a high score does not prove adequacy.
- C: It is a candidate-selection signal, not a verdict.
- D: The next review must inspect the passage against the actual claim.
- E: Precision of the score does not turn relevance into support.

**Source:** Ranking turns scores into omissions

## MA-ch07.25

Check each statement that is true about the audit view and what `retrieve` leaves out. Each statement is worth 1 point (5 points total).

- [ ] A. A list of winners gives you the same view the final prose does, one stage earlier.
- [ ] B. The audit view lists every document with its score.
- [ ] C. Each document's fate in the audit view is one of selected, below the cutoff, or zero overlap.
- [ ] D. A fate of "rejected by Claude" is one of the audit view's three outcomes.
- [ ] E. You can see an omission by reading the ranked list of winners alone.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Winners alone hide the omissions, as the prose does.
- B: The gate asks for every document with its score.
- C: Those are the three fates the gate names.
- D: The three fates do not include a Claude rejection.
- E: To see an omission you have to compute it.

**Source:** Ranking turns scores into omissions

## MA-ch07.26

A corpus is {a: "office hours appointment", b: "hours office", c: "office", d: "appointment only"}, the query is "office hours", and k is 2. Check each statement that is true of the audit view. Each statement is worth 1 point (5 points total).

- [ ] A. Document b is selected with a score of 1.0.
- [ ] B. Document a is selected with a score of about 0.8165.
- [ ] C. Document c has a positive score of about 0.7071 and its fate is "below the cutoff".
- [ ] D. Document d has the fate "zero overlap".
- [ ] E. Document c's omission shows that it is irrelevant to the query.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: "hours office" has the same vector as the query.
- B: dot 2, lengths sqrt(2) and sqrt(3), giving 2 / sqrt(6).
- C: dot 1 over sqrt(2) * 1 is about 0.7071, and it falls outside the top two.
- D: "appointment only" shares no token with the query.
- E: Omission is not proof of irrelevance; c simply scored below the cutoff.

**Source:** Ranking turns scores into omissions

## MA-ch07.27

Check each statement that is true about the synonym map as a repair for the synonym miss. Each statement is worth 1 point (5 points total).

- [ ] A. The tempting repair for a paraphrase miss is a synonym map applied before vectorization.
- [ ] B. The decision hidden in a synonym map is who gets to say that two words mean the same thing.
- [ ] C. Mapping tuition to fee is safe in every sentence.
- [ ] D. Proposing a map is Claude's work, while deciding whether to adopt it is yours.
- [ ] E. Expanding both queries and documents leaves counts and vector lengths unchanged.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The chapter names the synonym map as the tempting repair.
- B: That is the decision the repair hides.
- C: Fee is not interchangeable with tuition in every sentence.
- D: Whether two words are interchangeable is a fact about policy and population, so you decide.
- E: Expanding both sides can change counts and vector lengths.

**Source:** The synonym miss and a dangerous repair

## MA-ch07.28

A learner maps tuition to fee and refund to reimbursement in the query only. The query is "tuition refund eligibility" and the document is "fee reimbursement for travel". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Before the mapping, the cosine is 0.0, because the two texts share no token.
- [ ] B. After the mapping, the query is "fee reimbursement eligibility" and the cosine is about 0.5774.
- [ ] C. The rise in the score shows that the travel document answers the tuition-refund eligibility question.
- [ ] D. When you encode such a map, you should record the exact map and whether it applies to queries, documents, or both.
- [ ] E. This example is evidence about a real university's refund rule.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: No token is shared before the mapping.
- B: dot 2, lengths sqrt(3) and sqrt(4), so 2 / sqrt(12), about 0.5774.
- C: Literal mapped overlap can rise while the policy question stays unanswered.
- D: The map is data that influences the result and needs provenance.
- E: It is a constructed counterexample, not evidence about a real rule.

**Source:** The synonym miss and a dangerous repair

## MA-ch07.29

Check each statement that is true about the tension between recall and review burden. Each statement is worth 1 point (5 points total).

- [ ] A. More recall can also return more distractors.
- [ ] B. More restrictive matching reduces the chance of omitting paraphrases.
- [ ] C. The cost of missing material versus reviewing extra candidates is the task owner's to price.
- [ ] D. The chapter establishes one universal threshold that balances this tension.
- [ ] E. Recall can be raised without any added review burden.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: More returned material includes more distractors.
- B: More restrictive matching can omit paraphrases.
- C: That cost belongs to the task owner.
- D: The chapter does not establish a universal threshold.
- E: More returned material means more to review.

**Source:** The synonym miss and a dangerous repair

## MA-ch07.30

Check each statement that is true about relevance and entailment. Each statement is worth 1 point (5 points total).

- [ ] A. Retrieval asks which documents are similar enough, under a rule, to inspect first.
- [ ] B. Evidence review asks whether a selected passage supports a specific claim.
- [ ] C. A passage saying office hours are by appointment is irrelevant to office hours.
- [ ] D. That passage supplies the "every Tuesday at two" time in a generated answer.
- [ ] E. The review question can be collapsed into the retrieval question when the score is precise to ten decimal places.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Retrieval selects what to inspect first.
- B: Evidence review checks support for a claim.
- C: The passage is relevant to office hours.
- D: The passage does not give the Tuesday time, so that is an unsupported addition.
- E: The second question cannot be collapsed into the first.

**Source:** Relevance and entailment are separate checks

## MA-ch07.31

Check each statement that is true about claim-by-claim evidence review. Each statement is worth 1 point (5 points total).

- [ ] A. The review works claim by claim.
- [ ] B. For each claim, you quote or identify the exact source passage within the permitted material.
- [ ] C. For each claim, you record whether the passage supports, contradicts, or does not resolve it.
- [ ] D. A document-level citation counts as support for every sentence in a paragraph.
- [ ] E. A cited claim needs checking only at the paragraph level.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The chapter prescribes claim-by-claim review.
- B: The passage must be identified exactly.
- C: Those are the three outcomes to record.
- D: A document-level citation is not support for every sentence.
- E: Paragraph-level checking can hide an unsupported part.

**Source:** Relevance and entailment are separate checks

## MA-ch07.32

Check each statement that is true about who runs the support check. Each statement is worth 1 point (5 points total).

- [ ] A. If the process that wrote the sentence also vouches for its citation, you have the first opinion run twice.
- [ ] B. Claude can quote the passage, propose a label, and hunt for the sentence that would change the label.
- [ ] C. The label that goes in the table is the one Claude proposed, because it saw the sentence first.
- [ ] D. When you disagree with Claude's label, noting that you read it differently is enough.
- [ ] E. When you disagree with Claude, you defer to it because it processed more text.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Self-vouching is one opinion counted twice.
- B: That saves you the search.
- C: The table label is the one you gave after reading the original.
- D: You write down the sentence that decides it.
- E: The chapter assigns the final label to you.

**Source:** Relevance and entailment are separate checks

## MA-ch07.33

Check each statement that is true about overriding Claude's label, following the discipline borrowed from Irreducibly Human. Each statement is worth 1 point (5 points total).

- [ ] A. A human correction adds signal whenever the human disagrees with the machine.
- [ ] B. A human correction adds noise when it is a wordless hunch.
- [ ] C. The book draws its line specifically for source labeling.
- [ ] D. "I read it differently" counts as a check.
- [ ] E. "This sentence names the term but not the date" is a well-formed override.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A correction adds signal when it names what the machine misses in this kind of case.
- B: A wordless hunch adds noise.
- C: The book draws it for validated imaging systems and statistical forecasts.
- D: The chapter says "I read it differently" is not a check.
- E: It names exactly what the passage lacks.

**Source:** Relevance and entailment are separate checks

## MA-ch07.34

Check each statement that is true about source identifiers and insufficient evidence. Each statement is worth 1 point (5 points total).

- [ ] A. The format contract from Chapter 2 can require source identifiers.
- [ ] B. "Has a source identifier" is a different obligation from "is supported by that source".
- [ ] C. A structural pass shows that the cited source supports the claim.
- [ ] D. When the selected context is insufficient, the correct result may be an abstention or a request for another source.
- [ ] E. When the selected context is insufficient, you should fill the gap with a plausible answer and cite the nearest passage.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A source-identifier requirement is useful for traceability.
- B: The identifier is structure; support is substance.
- C: A structural pass names only the obligation it passed.
- D: An abstention or request for another source can be the correct output.
- E: The chapter warns against filling the gap and citing the nearest passage.

**Source:** Relevance and entailment are separate checks

## MA-ch07.35

Check each statement that is true about supplying an entire corpus versus a bounded selection. Each statement is worth 1 point (5 points total).

- [ ] A. More text can include the missing evidence.
- [ ] B. More text can also contain contradictions and irrelevant material.
- [ ] C. More text can expose more content than a bounded task should.
- [ ] D. Context selection is an engineering and data-governance decision.
- [ ] E. Supplying the entire corpus is automatically superior to a selection.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The whole corpus may hold what a selection missed.
- B: It can also add contradictions and distractors.
- C: A bounded task may not warrant exposing everything.
- D: The chapter frames selection as engineering and governance.
- E: The chapter says supplying everything is not automatically superior.

**Source:** Relevance and entailment are separate checks

## MA-ch07.36

Check each statement that is true about Anthropic's context-engineering article as the chapter uses it. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter says the article was checked during the research pass on 2026-09-06.
- [ ] B. The article discusses context as a designed collection of instructions, tools, data, and history.
- [ ] C. The chapter cites the article to claim that its count vectors implement Claude's context mechanisms.
- [ ] D. The chapter closes by asking you to compare deliberate context selection with supplying an entire corpus, and to record what your selection retains and omits.
- [ ] E. The chapter says lexical counts are the same thing as neural embeddings.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The research-pass check date is given in the chapter.
- B: That is how the chapter summarizes the article.
- C: It is for comparing selection strategies, not for that claim.
- D: This is the closing Anthropics task.
- E: The chapter says not to imply that lexical counts are neural embeddings.

**Source:** Relevance and entailment are separate checks; Anthropics

## MA-ch07.37

Check each statement that is true about the retriever's contract in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. Cosine of count vectors is never negative.
- [ ] B. `retrieve` returns only positive scores, best first, equal scores in key order, at most k rows.
- [ ] C. The audit view returns only the selected rows.
- [ ] D. The retriever may claim that a passage is relevant in the sense a reader means.
- [ ] E. The retriever may claim that its ranking is complete and that the top passage is supported.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Counts are nonnegative, so the cosine cannot go below zero.
- B: That is the contract's statement of the return value.
- C: The audit view returns every document with its score and one of three fates.
- D: It may claim only a ranking of overlap under one representation.
- E: It may not claim completeness or support.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.38

Check each statement that is true about the wrong versions your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. Sorting worst-first is a wrong version that must fail at least one test.
- [ ] B. Breaking ties by insertion order is a wrong version that must fail at least one test.
- [ ] C. Checking k with `isinstance` so that True slips through is a wrong version that must fail at least one test.
- [ ] D. Dropping the zero filter is a wrong version that must fail at least one test.
- [ ] E. Using Counter to count tokens is one of the listed wrong versions.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Worst-first sorting is on the list.
- B: Insertion-order ties are on the list.
- C: The Boolean slip-through is on the list.
- D: So is dropping the zero filter.
- E: Counter is part of the reference design, not a wrong version.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.39

Check each statement that is true about the lesson's six tests, as the gate reads them. Each statement is worth 1 point (5 points total).

- [ ] A. The relevance test has a single positive-scoring document, so best-first and worst-first sorts return the same thing.
- [ ] B. Several of the six tests have two equal scores, so tie-breaking is already covered.
- [ ] C. The invalid-k test uses zero, which an `isinstance` check also rejects.
- [ ] D. No test makes k smaller than the number of positive matches.
- [ ] E. The way to confirm these gaps is to mutate a copy of the reference.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A single positive document cannot distinguish the sort directions.
- B: No test has two equal scores.
- C: Zero fails under both type checks, so it does not catch the isinstance version.
- D: No test truncates positive matches.
- E: The chapter says to confirm by mutating a copy.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.40

Check each statement that is true about the expected-source list in half two of the gate. Each statement is worth 1 point (5 points total).

- [ ] A. For each source, the list gives a title or identifier, an owner, a version or date, and why it is authorized.
- [ ] B. The list also gives the number of items you expect the corpus to hold.
- [ ] C. The list is written before you ingest anything.
- [ ] D. The list is dated.
- [ ] E. You should ask Claude what a corpus for this task should contain before you write your own list.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Those four fields are named.
- B: The expected item count carries the row-count question.
- C: Writing it before ingestion is the point.
- D: The list is dated so the comparison later is honest.
- E: You should not ask Claude before you have written yours.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.41

Check each statement that is true about why you should not ask Claude for the expected-source list first. Each statement is worth 1 point (5 points total).

- [ ] A. Claude's answer would be built from the task description you gave it, the same material you are trying to check.
- [ ] B. Asking Claude first is acceptable as long as you review its list afterwards.
- [ ] C. A fluent AI-generated frame carries extra information about missing sources because the AI has seen broader documentation.
- [ ] D. The list is mostly clerical, so Claude can write it and you can edit it.
- [ ] E. Claude can write the list without defeating its purpose.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The frame would come from the same description you are checking.
- B: The chapter says not to ask before you have written yours.
- C: The book's warning is that such a frame contains no information, since the AI started from the same documentation.
- D: The list is where your understanding of the task goes on the record.
- E: Claude cannot write it without defeating it.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.42

Check each statement that is true about the claims list and the evidence rules in half two of the gate. Each statement is worth 1 point (5 points total).

- [ ] A. The claims list has one sentence per question the report must answer.
- [ ] B. Each claim should be small enough for a single passage to support or not.
- [ ] C. A sentence containing "and" is acceptable if one passage supports both halves.
- [ ] D. The row labels (supported, contradicted, insufficient, not reviewed) are defined before you see a report.
- [ ] E. The row labels are defined after you see the report so they fit what it says.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: One sentence per question.
- B: Claims must be single-passage sized.
- C: The rule is that a sentence with an "and" is split.
- D: Defining labels first keeps them honest.
- E: Defining them afterward would tailor them to the report.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.43

Check each statement that is true about the evidence-row labels and who may use them. Each statement is worth 1 point (5 points total).

- [ ] A. Supported means a quoted passage states the claim, within its scope, date, and population.
- [ ] B. Insufficient means the nearest passage contradicts the claim.
- [ ] C. A row may be marked supported by whoever wrote the report.
- [ ] D. When the sources do not say, the report must say so and not fill the gap.
- [ ] E. Not reviewed is the label for a row whose passage contradicts the claim.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Scope, date, and population are part of the definition.
- B: Insufficient means on topic but not resolving the claim, with the missing piece named.
- C: The person who read the original authorized source may mark a row supported.
- D: The report must say the sources do not say.
- E: A contradicting passage gets the contradicted label.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.44

Check each statement that is true about the abstention rule "refuse when no document scores above zero". Each statement is worth 1 point (5 points total).

- [ ] A. It avoids answering from an empty selection in the synonym fixture.
- [ ] B. Positive overlap can still be insufficient, so the rule establishes no support.
- [ ] C. Raising the threshold never excludes a useful short passage.
- [ ] D. The rule is a complete substitute for human review.
- [ ] E. You need to write only the case the rule wrongly lets through.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: With no positive score, the rule refuses in the synonym fixture.
- B: A positive-scoring but insufficient passage passes the rule.
- C: Raising the threshold excludes some useful short passages.
- D: Review remains; the chapter asks what review is left.
- E: You also write the case a stricter threshold wrongly refuses, and what review remains.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.45

Check each statement that is true about what the packet may claim and about reopening the gate. Each statement is worth 1 point (5 points total).

- [ ] A. The packet may say: under this corpus and these rules, these claims were supported by these passages.
- [ ] B. The packet may call itself comprehensive without checking its inventory.
- [ ] C. Claude can sharpen the gate by pointing out a claim that is not small enough.
- [ ] D. Claude can write the expected-source list without defeating its purpose.
- [ ] E. If ingestion turns up an unlisted source, you keep the original dated list and add the revision with its reason.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: That is the bounded claim the chapter allows.
- B: "Comprehensive" needs an inventory that justifies the word.
- C: Claude can also flag rules with no failing case and insufficiencies with no row.
- D: Claude cannot write that list without defeating it.
- E: Design first is not design frozen; the revision is added with its reason.

**Source:** The gate: write the source list and the evidence rules first

## MA-ch07.46

Check each statement that is true about the Build It section. Each statement is worth 1 point (5 points total).

- [ ] A. You write your own version before opening the reference solution, as your baseline.
- [ ] B. You calculate the office-hours example by hand before running it.
- [ ] C. You preserve the tokens, counts, dot product, norms, and final score, not a lone decimal.
- [ ] D. You may describe the passing test total as complete retrieval coverage.
- [ ] E. A synonym map belongs in the reference version so its provenance is clear.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The baseline records what you understood before Claude touched anything.
- B: The hand calculation comes first.
- C: A lone decimal makes the mechanism harder to audit.
- D: The chapter says not to describe the total as complete retrieval coverage.
- E: A synonym map stays in the learner version.

**Source:** Build It: preserve the scoring path

## MA-ch07.47

Check each statement that is true about conducting Claude Code against your gate. Each statement is worth 1 point (5 points total).

- [ ] A. You give Claude Code the contract, the test list, and the audit-view specification, not your implementation.
- [ ] B. You run your tests on what it returns, yourself.
- [ ] C. A failing test is often a gap in your gate, which Claude cannot see because it has only what you wrote.
- [ ] D. You give Claude your implementation so it can match your baseline.
- [ ] E. If Claude's report says the tests pass, you may skip running them.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Those three items come from the gate.
- B: Running the tests yourself is part of the instruction.
- C: Claude sees only what the gate says.
- D: Your implementation is withheld; your baseline is what you compare against.
- E: Accepting the report's last sentence is what the chapter warns against.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## MA-ch07.48

Check each statement that is true about what to do with the result Claude Code returns. Each statement is worth 1 point (5 points total).

- [ ] A. Note which of your tests failed, if any.
- [ ] B. Compare its implementation with your baseline and name one difference in behavior.
- [ ] C. Ask Claude to propose a deliberately wrong version that still passes your tests, and check by hand whether it does.
- [ ] D. If the wrong version does pass your tests, your list was too weak, and you found that out cheaply.
- [ ] E. When Claude critiques your representation, accept its suggestions if they are fluent.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Failing tests point at gate gaps.
- B: A named difference is either a revision to the gate or a missed defect.
- C: The wrong-version check tests your test list.
- D: That is the stated payoff.
- E: The chapter says to verify every suggestion against the displayed mechanism.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## MA-ch07.49

Check each statement that is true about building the corpus and the packet. Each statement is worth 1 point (5 points total).

- [ ] A. You build the corpus from material you are authorized to use, recording source identity, version or date, and inclusion criteria.
- [ ] B. You may upload restricted material if the interface can accept it, because the interface enforces the boundary.
- [ ] C. The data boundary from Chapter 5 is relaxed for Cowork tasks.
- [ ] D. Who may read what is a decision people make, not one the interface makes.
- [ ] E. Inclusion criteria are optional when the corpus is small.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Those fields are the stated record.
- B: Do not upload restricted material merely because the interface can accept it.
- C: The Chapter 5 boundary remains in force.
- D: The chapter says exactly this.
- E: The inclusion criteria are part of the record regardless of size.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## MA-ch07.50

Check each statement that is true about running retrieval and responding to missing evidence. Each statement is worth 1 point (5 points total).

- [ ] A. You inspect both selected and omitted candidates, using the audit view.
- [ ] B. You compare the inventory with the expected-source list you dated before ingestion.
- [ ] C. For each required answer claim, you identify whether sufficient evidence appears in the selected context.
- [ ] D. If evidence is missing, you revise the query, representation, corpus, or task scope.
- [ ] E. Revising the final prose is enough to resolve an evidence problem.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Omitted candidates are visible only in the audit view.
- B: The comparison is the point of dating the list.
- C: Sufficiency is judged claim by claim.
- D: The repairs are upstream of the prose.
- E: Revising the prose alone leaves the evidence problem in place.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## MA-ch07.51

Check each statement that is true about running the task through Claude Cowork. Each statement is worth 1 point (5 points total).

- [ ] A. You preserve the actual interface details and output.
- [ ] B. The chapter cannot claim which internal retrieval steps the product used.
- [ ] C. Comparing your packet with the interface task proves the interface uses the same retrieval as your retriever.
- [ ] D. If the interface is unavailable, you ship the offline corpus, retrieval results, and proposed packet, and mark the generation portion not run.
- [ ] E. If the interface is unavailable, you must use direct API credits to complete the assessment.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Real details and output must be kept.
- B: The chapter makes no claim about Cowork internals.
- C: The comparison is an observed workflow, not proof of internal equivalence.
- D: This is the stated fallback.
- E: The mechanics remain assessable without direct API spending.

**Source:** Use It: conduct Claude Code, then build a bounded Cowork task packet

## MA-ch07.52

Check each statement that is true about debugging an unsupported final claim in the order information moves. Each statement is worth 1 point (5 points total).

- [ ] A. When a final claim is unsupported, you start upstream rather than rewriting the answer repeatedly.
- [ ] B. You start at the Claim stage and work backward to the corpus.
- [ ] C. You preserve the score of a document that fell below k rather than pretending it was never considered.
- [ ] D. Debugging ends when every stage has produced a green marker.
- [ ] E. Debugging ends when the stated conclusion matches the actual evidence.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The stages from the opening table give the order of inspection.
- B: The chapter says to start at the top, with eligibility.
- C: A below-k score is part of the record.
- D: Green markers are not the stopping condition.
- E: That is the stated end of debugging.

**Source:** Ship It: the source-grounded task packet (Debug the pipeline in the order information moves)

## MA-ch07.53

Check each statement that is true about the first four rows of the debugging table (Eligibility, Ingestion, Representation, Scoring and cutoff). Each statement is worth 1 point (5 points total).

- [ ] A. An eligibility failure is a source excluded by a permission or scope decision, which retrieval cannot legally repair.
- [ ] B. An ingestion failure looks like a skipped file format or the wrong folder being read.
- [ ] C. The reference implementation demonstrates the ingestion step.
- [ ] D. A better prompt after retrieval can repair a representation failure such as the synonym case.
- [ ] E. If a larger k brings in the missing evidence, there is no added review burden to record.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The claim may need narrowing instead.
- B: Those are the table's examples of ingestion failure.
- C: The reference starts from a constructed dictionary and never demonstrates this step.
- D: No prompt after retrieval repairs a representation that shares no coordinate.
- E: A larger k adds review burden, which you record.

**Source:** Ship It: the source-grounded task packet (Debug the pipeline in the order information moves)

## MA-ch07.54

Check each statement that is true about the last three rows of the debugging table (Selection into context, Use, Claim). Each statement is worth 1 point (5 points total).

- [ ] A. Use is the first stage where rewriting the answer helps.
- [ ] B. Once the source is in context and Claude embellishes it, no separate support review is needed.
- [ ] C. A selection-into-context failure is when another filter or a manual choice narrowed what the retriever returned.
- [ ] D. At the Claim stage, the repair belongs to the author of the retriever.
- [ ] E. A claim failure looks like a summary that calls the report comprehensive or verified.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Before Use, rewriting the answer cannot help.
- B: Support is still a separate review.
- C: The table asks whether what Claude saw is what the retriever returned.
- D: The Claim stage belongs to whoever signs.
- E: That is the table's example of a claim failure.

**Source:** Ship It: the source-grounded task packet (Debug the pipeline in the order information moves)

## MA-ch07.55

Check each statement that is true about chunking. Each statement is worth 1 point (5 points total).

- [ ] A. The reference treats each dictionary value as a complete document, so it does not implement chunking.
- [ ] B. A claim and its qualification can fall in adjacent chunks, so retrieving only the claim-shaped fragment can make a passage look stronger than its source.
- [ ] C. A large chunk can dilute lexical overlap with unrelated terms and lower its normalized score.
- [ ] D. Chunk overlap is free completeness.
- [ ] E. A generated citation to chunk-7 is easy to audit even if the packet does not connect it to a document and passage.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The chapter says the reference does not implement chunking.
- B: Splitting can hide the qualification.
- C: Unrelated terms enlarge the vector length and lower the cosine.
- D: Overlap duplicates tokens and candidates and influences ranking and context volume.
- E: Chunk identifiers must preserve source identity and location.

**Source:** Ship It: the source-grounded task packet (Chunk boundaries create another representation)

## MA-ch07.56

Check each statement that is true about the claim-to-source evidence table. Each statement is worth 1 point (5 points total).

- [ ] A. It needs more columns than claim and citation.
- [ ] B. It adds the exact supporting passage or stable location, a reviewer judgment, and a note about scope or missing qualification.
- [ ] C. An insufficient row is actionable evidence: narrow the sentence, retrieve more material, or abstain.
- [ ] D. You should not force every row into supported merely because the report is supposed to be complete.
- [ ] E. If the table cannot represent a gap, the reviewer is freed to report one.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The chapter says it needs more than claim and citation columns.
- B: Those are the added columns.
- C: Insufficient rows point to a next action.
- D: Forcing every row to supported hides gaps.
- E: A table that cannot represent a gap pressures the reviewer to hide one.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## MA-ch07.57

For the office-hours hypothetical, a supplied sentence says office hours are available by appointment. Check each statement that is true about the claims in the evidence table. Each statement is worth 1 point (5 points total).

- [ ] A. "Appointments are mentioned" is supported by the supplied sentence.
- [ ] B. "Appointments occur Tuesday at two" is insufficient because the time is absent.
- [ ] C. A paragraph-level judgment is better because it shows the grounded and invented parts together.
- [ ] D. Atomic claims make visible that one part of a paragraph is grounded while another is invented.
- [ ] E. "Appointments occur Tuesday at two" is contradicted by the supplied sentence.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The sentence states that appointments are mentioned.
- B: The passage does not give a day or time.
- C: A paragraph-level judgment could conceal that one part is invented.
- D: Atomic claims are what expose the mix.
- E: The sentence is silent on the time; it does not contradict it.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## MA-ch07.58

Check each statement that is true about the provenance of passages and about reviewing the table. Each statement is worth 1 point (5 points total).

- [ ] A. A string entered by the learner is a constructed fixture.
- [ ] B. A passage copied from a real policy needs an authorized source, a version or retrieval date where relevant, and enough location information to revisit it.
- [ ] C. Constructed fixtures and real passages should not be merged in one table without labeling the roles.
- [ ] D. You ask Claude to label each row first, then check its labels yourself.
- [ ] E. If another reviewer needs surrounding text you did not record, the record should improve.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A learner-typed string is a fixture.
- B: Real passages need a traceable source.
- C: The chapter says not to merge the roles unlabeled.
- D: You label each row yourself first, then ask Claude for the sentence that would change your label.
- E: That is the stated test of whether the record is enough.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## MA-ch07.59

Check each statement that is true about the selection record behind a report. Each statement is worth 1 point (5 points total).

- [ ] A. You preserve the query that actually produced the selection.
- [ ] B. If a revised query retrieves better evidence, its success is attributed to the original run.
- [ ] C. You record any synonym a human supplied after seeing the failure.
- [ ] D. The source collection and the context finally shown to Claude can differ, for example twenty items in the corpus, two returned, and one received.
- [ ] E. Without a selection record, blaming the generator for missing information is always justified.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The query behind the selection is part of the record.
- B: A revised query's success cannot be attributed to the original run; keep both and label the revision.
- C: Human-supplied synonyms must be recorded.
- D: Each narrowing between collection and context should be named.
- E: Without a record, a reviewer may blame the generator for information the workflow never supplied.

**Source:** Ship It: the source-grounded task packet (Build an evidence table that can say no)

## MA-ch07.60

Check each statement that is true about accountable context and the omitted or insufficient case. Each statement is worth 1 point (5 points total).

- [ ] A. The result is accountable context, not maximal context.
- [ ] B. The packet should include at least one omitted or insufficient case.
- [ ] C. The packet should explain whether a missing source was absent from the corpus, scored zero, or fell below k.
- [ ] D. Maximal context is the goal of the packet.
- [ ] E. A packet containing only the passages that made the answer look good can still reveal the selection boundary.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Enough authorized material, a record of what was left out, and a route to say the evidence is insufficient.
- B: That case shows the selection boundary.
- C: Those are the three locations of a missing source.
- D: The chapter says the result is not maximal context.
- E: Such a packet cannot reveal the selection boundary.

**Source:** Ship It: the source-grounded task packet (The packet, assembled)

## MA-ch07.61

Check each statement that is true about how the packet's parts relate. Each statement is worth 1 point (5 points total).

- [ ] A. The corpus inventory shows what was eligible.
- [ ] B. The retrieval record shows what the algorithm selected.
- [ ] C. The task packet shows what Claude was permitted and asked to use.
- [ ] D. The evidence table connects claims back to exact passages and records gaps.
- [ ] E. The dated expected-source list is placed at the end, after the conclusions.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The inventory is the eligible collection.
- B: The retrieval record is the algorithm's selection.
- C: The packet fixes Claude's permissions and request.
- D: The table is the claim-to-passage link.
- E: The expected-source list sits in front of all of them.

**Source:** Ship It: the source-grounded task packet (The packet, assembled)

## MA-ch07.62

Check each statement that is true about the verbs in the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. "Retrieved" describes what the selection rule returned.
- [ ] B. "Quoted" describes what you copied.
- [ ] C. "Supported" describes a claim and a passage you actually compared.
- [ ] D. "Verified" and "comprehensive" need no more than this packet offers.
- [ ] E. A passage the retriever returned can be called "supported" when its score is high.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Retrieval is the selection rule's output.
- B: Quoting is copying.
- C: Support requires an inspected comparison.
- D: Those words need more than this packet offers, unless you did the work behind them.
- E: A retrieved passage is not thereby a supporting one.

**Source:** Ship It: the source-grounded task packet (The packet, assembled)

## MA-ch07.63

Check each statement that is true about the sign-off template. Each statement is worth 1 point (5 points total).

- [ ] A. The "Not checked" line does the work.
- [ ] B. An AI-written sign-off handles the "Not checked" line well because Claude keeps a record of every file it failed to load.
- [ ] C. If your evidence does not support signing, you sign and add a caveat.
- [ ] D. The sign-off may say the report is verified if Claude's tests passed.
- [ ] E. The "How" line need not say which parts were done with Claude's help.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The chapter says this line carries the sign-off.
- B: An AI-written sign-off leaves it out, because the system has no record of sources you never opened or the file that failed to load.
- C: If your evidence does not support signing, you withhold.
- D: "Verified" needs more than this packet offers.
- E: The template says to name the parts done with Claude's help.

**Source:** Ship It: the source-grounded task packet (The packet, assembled)

## MA-ch07.64

Check each statement that is true about the driver's-seat table. Each statement is worth 1 point (5 points total).

- [ ] A. For listing a folder, scoring and ranking every document, and quoting candidate passages, Claude should do it fast and show every score.
- [ ] B. For that work, you should read the full audit view, not only the winners.
- [ ] C. For the expected-source list, Claude writes the first draft and you review it.
- [ ] D. For a synonym map, a chunk size, or a larger k, Claude proposes with cases that might break it, and you decide and record where each came from.
- [ ] E. For which sources may be used, Claude decides after flagging restricted material.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Ranking is the part to hand over.
- B: Omissions are invisible in a list of winners, so reading what was left out is yours.
- C: You write the list first, from the task; Claude may propose missing-source questions afterward.
- D: Whether two terms are interchangeable is a fact about the policy and population.
- E: Authorization is a decision people make.

**Source:** Ship It: the source-grounded task packet (The driver's seat)

## MA-ch07.65

Check each statement that is true about recording the split between delegated work and retained judgment. Each statement is worth 1 point (5 points total).

- [ ] A. The packet records one task you delegated and one judgment you retained.
- [ ] B. If you cannot point to a transcript line or an edit that shows each, the split happened in your head and not in the record.
- [ ] C. A statement of the split is enough without any evidence.
- [ ] D. Only the delegated task needs evidence.
- [ ] E. The evidence is the recomputed cosine score of the office-hours pair.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The chapter asks for one of each.
- B: Evidence must be pointable.
- C: The evidence is concrete: transcript, dated list, and differing labels.
- D: Both the delegated task and the retained judgment need evidence.
- E: The evidence is the transcript, the dated expected-source list, and the rows where labels differed.

**Source:** Ship It: the source-grounded task packet (The driver's seat)

## MA-ch07.66

Check each statement that is true about the Verify and reflect section. Each statement is worth 1 point (5 points total).

- [ ] A. You recalculate one cosine score independently.
- [ ] B. You preserve the interpreter and the input corpus rather than reporting a score without its representation.
- [ ] C. You compare the expected-source list with the inventory and write the gap in one sentence.
- [ ] D. You rewrite the expected-source list to match what you found.
- [ ] E. You audit a claim only against the selected chunk, since that is the retrieved evidence.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: One independent recalculation is the check.
- B: A score without its representation is not auditable.
- C: The gap is the learning.
- D: The chapter says not to rewrite the list to match.
- E: Audit against the original source, since chunk boundaries can omit qualifications.

**Source:** Verify and reflect

## MA-ch07.67

Check each statement that is true about the Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. The Assessments are ungraded practice and carry no points.
- [ ] B. In the zero-length warm-up, you predict the cosine with one empty vector and explain the returned value without calling an empty query meaningful.
- [ ] C. In the tie-order exercise, you write the wrong version that orders ties by insertion and show which of your tests fails on it.
- [ ] D. In the top-k exercise, an omitted result is treated as proof of irrelevance.
- [ ] E. The paired lesson's knowledge check is graded.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The chapter calls them ungraded practice.
- B: The returned 0.0 is a convention, not a finding.
- C: The wrong version should fail a test.
- D: The exercise records the omitted result as an audit row and explains why omission is not proof of irrelevance.
- E: The chapter says the Assessments carry no points.

**Source:** Assessments - ungraded practice

## MA-ch07.68

The query is "office hours". Document d1 is "office hours appointment" and document d2 is "office hours". A learner adds the term "appointment" to the query, making it "office hours appointment". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Before the change, d2 scores 1.0 and d1 scores about 0.8165.
- [ ] B. After the change, d1 scores 1.0.
- [ ] C. After the change, d2 scores about 0.8165, because its dot product stays 2 while the query's length changes.
- [ ] D. After the change, the ranking of d1 and d2 is the same as before.
- [ ] E. After the change, the dot product of d2 with the new query is 3.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: d2 is identical to the query; d1 gives 2 / sqrt(6).
- B: The new query equals d1's vector, so the cosine is 3 / (sqrt(3) * sqrt(3)).
- C: The dot product stays 2, but the query length grows to sqrt(3), giving 2 / (sqrt(3) * sqrt(2)).
- D: The order reverses: d1 now ranks above d2.
- E: Only office and hours are shared, so the dot product is 2.

**Source:** Assessments - ungraded practice

## MA-ch07.69

The corpus is {doc-b: "office hours", doc-a: "office hours", doc-c: "office hours extra"}, inserted in that order, and the query is "office hours". Check each statement that is true of `retrieve`. Each statement is worth 1 point (5 points total).

- [ ] A. doc-a and doc-b both score 1.0.
- [ ] B. With k equal to 1, `retrieve` returns doc-a.
- [ ] C. With k equal to 2, `retrieve` returns doc-b then doc-a, following insertion order.
- [ ] D. With k equal to 3, doc-c is excluded because its score equals the others.
- [ ] E. With k equal to 1, doc-b is returned because it was inserted first.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Both are identical in direction to the query.
- B: The tie is broken by ascending key, and "doc-a" sorts first.
- C: Ties are broken by key, so doc-a comes first.
- D: doc-c scores about 0.8165 and is returned third.
- E: Insertion order does not decide ties.

**Source:** Assessments - ungraded practice

## MA-ch07.70

Check each statement that is true about what the chapter says you can now trace. Each statement is worth 1 point (5 points total).

- [ ] A. A zero-overlap document may be semantically related.
- [ ] B. A high-overlap document may still be insufficient.
- [ ] C. The score and the support review have different jobs.
- [ ] D. Facts A and B contradict each other.
- [ ] E. If the prose is wrong, the failure began in generation.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The synonym pair is the example.
- B: A passage can repeat terms and still not support the claim.
- C: One ranks candidates; the other judges support.
- D: The chapter says it is not a contradiction.
- E: The packet lets a reviewer diagnose whether the failure began in ingestion, representation, ranking, generation, or interpretation.

**Source:** What you can now trace

## MA-ch07.71

Check each statement that is true about the bridge from retrieval to Chapter 8. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 8 builds a minimal Model Context Protocol server state machine.
- [ ] B. It traces initialization, tool discovery, request identifiers, and error results.
- [ ] C. It separates protocol compatibility from trust and authorization.
- [ ] D. The question to carry forward is who decided what reaches Claude, and where is that written down.
- [ ] E. A compatible message is an authorized one, just as a high score is support.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is Chapter 8's stated build.
- B: Those are the traced steps.
- C: Compatibility is not trust or authorization.
- D: The closing question is about context decisions and their record.
- E: Just as a high score is not support, a compatible message is not an authorized one.

**Source:** A protocol connects capabilities

## MA-ch07.72

Check each statement that is true about the access-boundary assumption from the companion Computational Skepticism chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A dataset's effective reach is its schema plus whatever its contents reference.
- [ ] B. The claim is sharpest for self-contained tables such as sensor readings.
- [ ] C. You apply it by asking whether a passage quotes, links, or defers to a document that is not on your source list.
- [ ] D. If a passage defers to an unlisted document, the passage can still be read as complete.
- [ ] E. The dependency on an unlisted document is recorded in the packet as a resolved item.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: That is the assumption.
- B: It is sharpest for reference-rich material such as email and weak for a self-contained sensor table.
- C: That is the application to one passage in your corpus.
- D: The passage cannot be read as complete without that document.
- E: The dependency belongs in the packet as an unresolved item.

**Source:** Computational Skepticism

## MA-ch07.73

Check each statement that is true about the row-trace step. Each statement is worth 1 point (5 points total).

- [ ] A. You follow one answer passage back to its original source.
- [ ] B. Where the original is unreachable, you document the opacity.
- [ ] C. Documented opacity counts as a failure of the procedure.
- [ ] D. You record which of "not retrieved", "not in the corpus", and "not true" you could establish and which you could not.
- [ ] E. The two diagnostics are a measurement of this retriever and corpus.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The trace starts from an answer passage.
- B: Documenting opacity is the instruction.
- C: The chapter counts opacity as a finding, not a failure.
- D: Those are the three claims to separate.
- E: They are two questions for the packet, not a measurement of the retriever or corpus.

**Source:** Computational Skepticism
