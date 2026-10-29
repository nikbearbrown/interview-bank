# Foundations (midterm-prep sections 1-12)

Questions on the background material and the first core ideas of working with generative AI, in section order. Each section keeps its own heading below.

# 1. A brief history of AI

## ES-1.1

A team can build a spam filter in two ways: by writing rules by hand (for example, flag any message that contains a listed phrase), or by training a model on thousands of messages labeled spam or not spam. Compare how each approach fails, and say what a person still has to decide in both cases.

**Points:** 5

**Rubric (1 point each):**

1. States that the rule-based filter's behavior comes only from the rules a person wrote, so every decision can be traced to a rule.
2. States that the rule-based filter fails on messages its rules did not anticipate, such as a spammer rewording a listed phrase, and must be extended by hand.
3. States that the trained model infers patterns from the labeled examples and can flag messages that no rule described, if they resemble the training data.
4. States that the trained model fails where its data is unrepresentative, outdated or mislabeled, and that its errors are harder to trace to a single cause.
5. States that in both cases a person must decide what counts as correct and check the filter against that standard on messages it has not seen.

# 2. What is a model? What is a language model?

## ES-2.1

Trace what happens between typing a prompt and receiving the first generated token, naming each stage. Then explain why sending a prompt does not change the model's weights.

**Points:** 5

**Rubric (1 point each):**

1. Text is split into tokens and mapped to integer token IDs.
2. Token IDs are looked up as embeddings.
3. Transformer layers produce logits, one score per vocabulary token.
4. Softmax converts logits to probabilities and one token is sampled.
5. States that a prompt is input to inference, not training, so weights stay fixed.

# 3. Inside a transformer: encoder, decoder, context and prediction

## ES-3.1

Describe the two main parts of a transformer language model and what each contributes to producing the next token. Then explain what this structure does not include that a reader evaluating the output might assume it does.

**Points:** 5

**Rubric (1 point each):**

1. Explains that self-attention updates each token's representation using information from the other tokens in the context, so a token's representation depends on its surroundings.
2. Explains that the prediction step converts the final representation into a score for each possible next token and then into probabilities, from which the next token is chosen.
3. Notes that text is produced one token at a time, with each chosen token added to the context for the next prediction.
4. States that nothing in this structure checks the output against the world; the model produces text that is likely given its context and training.
5. Draws the consequence for evaluation: fluent, confident output is not evidence of truth, so claims that matter need independent checking.

## ES-3.2

Explain what an encoder and a decoder are in a transformer, how they differ in what they can see and what they produce, and which you would expect to use for (a) classifying a customer email as urgent or not urgent and (b) writing a reply to it.

**Points:** 5

**Rubric (1 point each):**

1. States that an encoder reads a whole input and produces a context-aware representation of each token, using self-attention over the input.
2. States that a decoder produces output one token at a time, each prediction using the tokens before it, with each chosen token added to the context.
3. States the difference in what they can see: an encoder can use tokens on both sides of a position, while a decoder cannot use later tokens when it predicts.
4. Matches the tasks: classifying a complete email fits an encoder, whose representation is read out as a label, and writing a reply fits a decoder, alone or with an encoder reading the email.
5. Notes that neither part checks its output against the world, so both the classification and the reply need evaluation on held-out examples or against sources.

# 4. Tokens and input embeddings

## ES-4.1

A model has a vocabulary of 50,000 tokens and an embedding size of 768. A prompt is tokenized into 12 tokens. Give (a) the size of the token ID array, (b) the size of the embedded input matrix, and (c) the size of the logits vector for the next-token prediction. Explain why (c) does not depend on the prompt length.

**Points:** 5

**Rubric (1 point each):**

1. (a) The token ID array has length 12.
2. (b) The embedded input is 12 × 768.
3. (c) The logits vector has length 50,000.
4. Explains logits give one score for every vocabulary token, so length is vocab_size.
5. Notes the context window limits the token array length, not the logits length.

## ES-4.2

Explain what an input embedding is and how it is produced from a token. Use the words "dog" and "cat" to explain why related words may end up with nearby embeddings, and say what that nearness does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Defines an input embedding as a learned vector of numbers that represents a token, selected by the token's ID from a table, and learned in training together with the rest of the model rather than written by hand.
2. Explains that "dog" and "cat" occur in similar contexts in the training text, for example near words about pets, feeding and walking, and that training pulls tokens that fit similar contexts toward similar vectors.
3. States that no person labeled the two words as related; the closeness comes from how the words were used in the text.
4. States that the input embedding depends only on the token, and that attention later revises each token's vector using the surrounding context.
5. States that nearness reflects similar use in the training text, not verified similarity of meaning, and can carry associations and biases from that text, so claims about what it shows need testing.

# 5. Softmax and temperature

## ES-5.1

Logits [1, 2, 3] give p(token 3) of about 0.867 at T = 0.5, 0.665 at T = 1.0 and 0.506 at T = 2.0. Describe the trend, state what temperature does to the distribution, and explain why a low temperature cannot make a wrong answer true.

**Points:** 5

**Rubric (1 point each):**

1. States that p(token 3) falls as T rises (0.867, 0.665, 0.506).
2. Explains that lower T sharpens and higher T flattens the distribution.
3. Notes that as T goes to 0 the choice approaches greedy and as T grows it approaches uniform.
4. States that a positive T never reorders the tokens.
5. Explains that sampling probability is not truth probability, so concentrating on a wrong top token does not make it correct.

# 6. Self-attention, positional encoding and the Transformer

## ES-6.1

Explain in plain language what self-attention does for a token in a sentence. Then explain what it does and does not show when a model's vector for "bank" differs between "river bank" and "bank account", and what kind of evidence would show that the model handles both senses.

**Points:** 5

**Rubric (1 point each):**

1. States that self-attention lets each token take in information from other tokens in the context, giving some more weight than others.
2. States that the weights are computed from the sentence itself, so which tokens matter depends on the context.
3. States that the differing vector shows the representation depends on context.
4. States that a context-dependent vector is not by itself evidence that the model understands either sense.
5. Says that behavioral tests, such as choosing the right sense of "bank" on new sentences, are needed to show it.

## ES-6.2

Explain why parallelism matters for transformers at internet scale, both in training on very large text collections and in serving very many users. Say what is still sequential, and what all of this implies for cost, speed and the evaluation of outputs.

**Points:** 5

**Rubric (1 point each):**

1. Explains that during training the whole text is available, so the predictions for all positions can be computed in the same pass instead of one position after another.
2. Explains that this suits parallel hardware such as GPUs, which is what makes training on internet-scale text across many chips practical in time and cost.
3. Explains that generation stays sequential: each new token depends on the tokens before it, so a longer reply takes more steps and takes longer to arrive.
4. Explains that a service handles many users by running many requests together in batches, which raises throughput and lowers the cost per request, at some cost in waiting time.
5. Draws an evaluation consequence: batching and parallel hardware can produce tiny numerical differences between runs, so comparisons should record the setup and repeat runs instead of relying on a single one.

## ES-6.3

Explain why a transformer needs positional encoding when it already has self-attention, what positional encoding adds, and what this implies for how you would test a prompt.

**Points:** 5

**Rubric (1 point each):**

1. Explains that self-attention weighs tokens by their content and on its own carries no information about order, so the same words in any order would be treated alike.
2. Gives an example in which order changes meaning, such as "dog bites man" and "man bites dog".
3. Explains that positional encoding adds position information to each token's representation so the model can use order, and that this is part of the model's design rather than something the user supplies.
4. Notes that having position information does not guarantee equal use of information wherever it appears, so the placement and order of instructions and facts in a prompt can change the output.
5. Proposes testing a prompt under reordered variants and repeated runs, and limiting conclusions to the arrangements that were tested.

# 7. Programming languages vs language models

## ES-7.1

Contrast a programming language with a language model on three points: how input is interpreted, whether output is deterministic, and how errors show up. Then state what the two have in common in how they are ultimately executed on a computer.

**Points:** 5

**Rubric (1 point each):**

1. Programming language input is a formal grammar interpreted exactly; a language model takes ambiguous natural language.
2. Programs are deterministic for the same input; language model outputs are sampled and can vary at T > 0.
3. Program errors are explicit; language model errors are silent and fluent.
4. States that an LLM is itself a program doing arithmetic on CPUs/GPUs.
5. Explains that the difference is how the instruction is interpreted: executed exactly vs used as context for prediction.

# 8. The strength of functions

## ES-8.1

A common design principle for LLM systems is to let the model generate and let ordinary functions check. Explain the principle, give two properties of functions that make them good checkers, and give one concrete example of a function checking a model's output.

**Points:** 5

**Rubric (1 point each):**

1. States the principle: the model generates (drafts, interprets vague input) and deterministic code verifies what can be specified exactly.
2. Names one property that makes functions good checkers (for example deterministic, exact, testable).
3. Names a second property (for example composable, explicit contracts, inspectable failures).
4. Gives a concrete example (a schema validator, unit tests, recomputing arithmetic, looking up a cited source, a file-path allow-list).
5. Explains why the model's own judgment of its output is not an independent check: errors are fluent and silent, and the same blind spots can affect both generation and review.

# 9. Division of labor and acceptance gates

## ES-9.1

A gate is a check or human decision that an output must pass before it is accepted or acted on. A model repeatedly gives the same false answer to a factual question, even at low temperature. Design a gate for this case: say what it checks, who or what makes the decision, and why repeating the answer and lowering the temperature do not help it pass.

**Points:** 5

**Rubric (1 point each):**

1. Defines a gate as a check or human decision an output must pass before it is accepted or acted on.
2. States a gate must be able to reject outputs, and that it should be tested against known-bad outputs.
3. Specifies a concrete check or human decision based on independent evidence (comparison with an authoritative source or reference answer, expert review), not the model's confidence.
4. Explains that repeating the answer shows consistency, not correctness.
5. Explains that lowering the temperature only concentrates probability on the model's top choice, so it does not change whether the answer is true or whether it passes the check.

## ES-9.2

A model is trained on 300 billion tokens. Assume 0.75 words per token and a reading speed of 250 words per minute, read continuously with no breaks. Estimate how many years it would take one person to read the training data. Show the steps and say which assumption you would most want to check, and why.

**Points:** 5

**Rubric (1 point each):**

1. Converts tokens to words: 300B × 0.75 = 225 billion words.
2. Converts to minutes: 225B ÷ 250 = 900 million minutes.
3. Converts to years: about 1,700 years (roughly 1,711 to 1,712 depending on the year length used).
4. Names an assumption and shows how it scales the answer (for example a reader at half the speed needs twice the years, and a reader who reads 8 hours a day needs about three times as many).
5. Notes that 0.75 words per token is an approximation that varies by language and tokenizer, or that continuous reading is unrealistic.

# 10. Format validity versus factual validity

## ES-10.1

A model must answer from supplied sources and return JSON with an answer and a list of cited source identifiers. A validator checks only that the output parses as JSON, matches the expected schema (required fields and types), and cites identifiers that exist in the supplied list. Name the three kinds of validity at stake, say which the validator checks and which it cannot, and give an example of a response that passes but is wrong.

**Points:** 5

**Rubric (1 point each):**

1. Names JSON validity, schema validity and factual validity.
2. States the validator covers JSON and schema validity (and that the cited identifier exists).
3. States it cannot tell a true claim from a false one, or a source that supports the claim from one that does not.
4. Gives a concrete passing-but-wrong example (valid structure and an existing source identifier, but an answer that contradicts the source or is false).
5. States that a pass rate on this validator is not an accuracy score, and that content-level evaluation (reference answers, entailment checks or human review) is needed.

## ES-10.2

An engineer wants to know whether a model answers a factual question reliably, so they send the identical prompt three times and read the three responses. Describe what they should record, how they should judge the three responses, and what agreement among the three does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Records the exact prompt, all three outputs, the model name and version, the date, the interface and the sampling settings.
2. Judges factual correctness against an independent reference, separately from surface variation in wording.
3. Notes that differences in wording are not automatically a failure.
4. States that agreement shows consistency (repeatability), not verification or correctness.
5. Notes that three identical answers can all be wrong because of systematic error, that three samples is a small sample, and that some interfaces do not let the user set the sampling settings.

# 11. The agentic loop

## ES-11.1

An agent loop has a policy (the model, which proposes the next action) and a controller (the program around it, which executes actions, returns the results and enforces limits). Describe the loop step by step, explain why the loop stopping is not always success, and explain why a loop with a step limit still needs permissions.

**Points:** 5

**Rubric (1 point each):**

1. Lists the loop: state, policy chooses an action, controller executes it, result becomes an observation, state updates, repeat.
2. Assigns proposing actions to the policy and executing actions and enforcing limits to the controller.
3. Names the stopping conditions: goal met or budget exhausted.
4. Explains that stopping may mean the budget ran out, not that the task succeeded.
5. Explains that a bounded loop can still take one unauthorized or harmful action within its limit, so permissions are needed.

# 12. Solve-verify asymmetry, fluency, and falsifiability

## ES-12.1

Explain solve-verify asymmetry using one example, then explain how a designer can use it to build a generate-then-check workflow with a language model and where the advantage breaks down.

**Points:** 5

**Rubric (1 point each):**

1. States that checking an answer is often cheaper than producing it.
2. Gives a valid example (Sudoku, factoring and multiplying back).
3. Describes generating with the model and verifying with an independent check (tests, validators, source lookup).
4. States that asking the same model "are you sure?" is not independent.
5. States the advantage disappears when verifying is as hard as solving.

## ES-12.2

Explain why fluency is not evidence of correctness, and why "The prompt is better" is not yet a falsifiable claim. Rewrite it so that it is falsifiable.

**Points:** 5

**Rubric (1 point each):**

1. States fluency means smooth, confident-sounding and a wrong answer can be equally fluent.
2. States that confident tone is not a calibrated probability of being right.
3. Explains that a falsifiable claim says what observation would show it wrong.
4. Explains that "better" is unspecified (at what, measured how, on which cases).
5. Gives a falsifiable rewrite naming a metric, a case set and a threshold.
