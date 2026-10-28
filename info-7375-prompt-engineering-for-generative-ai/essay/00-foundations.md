# Foundations (midterm-prep sections 1-12)

Questions on the background material and the first core ideas of working with generative AI, in section order. Each section keeps its own heading below.

# 1. A brief history of AI

## ES-1.1

Put these four in chronological order and give the year of each: the Transformer paper, Rosenblatt's Perceptron, Turing's "Computing Machinery and Intelligence", backpropagation popularized for multi-layer networks. Then explain in one or two sentences why "AI was founded in 1943" is a mix-up.

**Points:** 5

**Rubric (1 point each):**

1. Turing's paper is placed first and dated 1950.
2. The Perceptron is placed second and dated 1958.
3. Backpropagation popularized is placed third and dated 1986.
4. The Transformer paper is placed fourth and dated 2017.
5. Explains that 1943 is the artificial neuron model while AI as a named field dates to 1956 (Dartmouth).

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

# 3. Neural network structure and RNNs

## ES-3.1

Compare how an RNN and a Transformer handle a long sequence. Cover how each carries information, whether training can be parallelized, and what happens to long-range dependencies.

**Points:** 5

**Rubric (1 point each):**

1. RNN passes information through a hidden state, one step at a time.
2. RNN training is hard to parallelize because steps are sequential.
3. RNN long-range dependencies suffer from vanishing or exploding gradients.
4. Transformer uses attention so every position can look at every other position directly.
5. Transformer training runs in parallel; notes LSTM/GRU only reduce the RNN problem.

# 4. Tokens

## ES-4.1

A model has a vocabulary of 50,000 tokens and an embedding size of 768. A prompt is tokenized into 12 tokens. Give (a) the size of the token ID array, (b) the size of the embedded input matrix, and (c) the size of the logits vector for the next-token prediction. Explain why (c) does not depend on the prompt length.

**Points:** 5

**Rubric (1 point each):**

1. (a) The token ID array has length 12.
2. (b) The embedded input is 12 × 768.
3. (c) The logits vector has length 50,000.
4. Explains logits give one score for every vocabulary token, so length is vocab_size.
5. Notes the context window limits the token array length, not the logits length.

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

# 6. Attention and the Transformer

## ES-6.1

Describe the steps of scaled dot-product attention, softmax(Q·Kᵀ / √d_k)·V, and explain what the √d_k does. Then explain what it does and does not show when the vector for "bank" differs between "river bank" and "bank account", and what kind of evidence would be needed to claim the model handles both senses.

**Points:** 5

**Rubric (1 point each):**

1. Scores every query against every key with a dot product.
2. Divides by √d_k to keep scores in a stable range as the dimension grows.
3. Applies softmax so each row of weights sums to 1, then outputs a weighted sum of the value vectors.
4. States that the differing vector shows the representation depends on context.
5. States that a context-dependent vector is not by itself evidence of understanding either sense, and that behavioral tests (for example word-sense disambiguation on held-out sentences) are needed.

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
