# Foundations (midterm-prep sections 1-12)

Questions on the background material and the first two course ideas, in section order. Each section keeps its own heading below.

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

Describe the steps of scaled dot-product attention, softmax(Q·Kᵀ / √d_k)·V, and explain what the √d_k does. Then explain why the changing vector for "bank" in "river bank" versus "bank account" does not show the model understood either sense.

**Points:** 5

**Rubric (1 point each):**

1. Scores every query against every key with a dot product.
2. Divides by √d_k to keep scores in a stable range.
3. Applies softmax so each row of weights sums to 1.
4. Outputs a weighted sum of the value vectors.
5. States that context changing a representation is not evidence of understanding.

# 7. Programming languages vs language models

## ES-7.1

Contrast a programming language with a language model on three points: how input is interpreted, whether output is deterministic, and how errors show up. State the key nuance about where an LLM runs.

**Points:** 5

**Rubric (1 point each):**

1. Programming language input is a formal grammar interpreted exactly; a language model takes ambiguous natural language.
2. Programs are deterministic for the same input; language model outputs are sampled and can vary at T > 0.
3. Program errors are explicit; language model errors are silent and fluent.
4. States that an LLM is itself a program doing arithmetic on CPUs/GPUs.
5. Explains that the difference is how the instruction is interpreted: executed exactly vs used as context for prediction.

# 8. The strength of functions

## ES-8.1

Explain the course's design rule "let the model generate, and let functions check." Give two properties of functions that make them good checkers and one concrete example from the course.

**Points:** 5

**Rubric (1 point each):**

1. States the rule: the model generates and functions check.
2. Names one property (e.g. deterministic, testable, exact).
3. Names a second property (e.g. composable, explicit contracts, inspectable failures).
4. Gives a course example (probabilities(), sample(), JSON contract validator, path policy).
5. Explains why a model should not check its own output (language model errors are silent).

# 9. Chapter 1: Division of Labor and The Gate

## ES-9.1

Define "the gate" in the course's sense and design one for this case: a model repeatedly gives the same false answer at low temperature. Say what the gate checks, who or what decides, and why repetition and low temperature do not help the answer pass.

**Points:** 5

**Rubric (1 point each):**

1. Defines the gate as the checkpoint an output must pass before being accepted or acted on.
2. States the gate must be able to reject an output.
3. Specifies a concrete check or human decision (not model confidence).
4. Explains that repeating the answer shows consistency, not correctness.
5. Explains that lowering temperature only makes the false answer more likely and does not change whether it passes.

## ES-9.2

The notes say a model was trained on 300 billion tokens. Using 0.75 words per token and a reading speed of 250 words per minute, estimate how many years of continuous reading that is. Show the steps and say which assumption moves the answer most.

**Points:** 5

**Rubric (1 point each):**

1. Converts tokens to words: 300B × 0.75 = 225 billion words.
2. Converts to minutes: 225B ÷ 250 = 900 million minutes.
3. Converts to years: about 1,700 years (1,711 with continuous reading).
4. Names the reading rate as an assumption that changes the answer by over a thousand years.
5. Notes the continuous, no-breaks assumption and that 0.75 words per token is approximate.

# 10. Chapter 2: The three-response experiment and what the green cannot distinguish

## ES-10.1

A response passes a JSON validator. Name the three kinds of validity, say which the validator checks and which it cannot, and give an example of a response that is green yet wrong.

**Points:** 5

**Rubric (1 point each):**

1. Names JSON validity, schema validity and factual validity.
2. States the validator covers JSON and schema validity.
3. States it cannot tell a true claim from a false one.
4. Gives a concrete green-but-wrong example (valid structure and source ID, false claim).
5. States a format-pass rate is not an accuracy score.

## ES-10.2

Describe the three-response experiment: what you do, what you record, and what agreement across the three responses does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Sends the same evidence-based prompt three times.
2. Records exact prompt, outputs, model label, date and interface.
3. Compares factual correctness separately from surface variation.
4. States agreement shows consistency, not verification.
5. Notes that three identical answers can all be wrong and temperature is not configurable everywhere.

# 11. The agentic loop

## ES-11.1

Describe the agentic loop step by step, separating the policy from the controller. Explain why stopping is not always success and why a bounded loop still needs permissions.

**Points:** 5

**Rubric (1 point each):**

1. Lists the loop: state, policy chooses an action, controller executes it, result becomes an observation, state updates, repeat.
2. Distinguishes the policy (proposes) from the controller (runs the loop, enforces limits).
3. Names the stopping conditions: goal met or budget exhausted.
4. Explains that stopping may mean the budget ran out, not success.
5. Explains that a bounded loop can still take one unauthorized action, so permissions are needed.

# 12. Solve-verify asymmetry, fluency, and falsifiability

## ES-12.1

Explain solve-verify asymmetry using one example, then explain how the course uses it to design a generate-then-check workflow and where the advantage breaks down.

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
