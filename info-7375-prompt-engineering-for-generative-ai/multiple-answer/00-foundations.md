# Foundations (midterm-prep sections 1-12)

Questions on the background material and the first two course ideas, in section order. Each section keeps its own heading below.

# 1. A brief history of AI

## MA-1.1

Check each statement that is historically accurate. Each statement is worth 1 point (5 points total).

- [ ] A. McCulloch and Pitts published a mathematical model of an artificial neuron in 1943.
- [ ] B. The term "artificial intelligence" comes from the proposal for the 1956 Dartmouth workshop.
- [ ] C. AI was founded as a field in 1942.
- [ ] D. AlexNet's 2012 ImageNet result is widely seen as the start of the modern deep learning boom.
- [ ] E. ChatGPT was released to the public in 2015.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The artificial neuron model is from 1943.
- B: McCarthy coined it in the 1955 proposal for the 1956 workshop.
- C: The neuron model is 1943 and the field was named in 1956; nothing founded it in 1942.
- D: That is the standard marker for the boom.
- E: ChatGPT launched in November 2022.

## MA-1.2

Check each statement that is historically accurate. Each statement is worth 1 point (5 points total).

- [ ] A. The Transformer was introduced in 2017 in "Attention Is All You Need".
- [ ] B. Turing's "Computing Machinery and Intelligence" (1950) was published before Rosenblatt's Perceptron (1958).
- [ ] C. Backpropagation was popularized in 1986 for training multi-layer networks.
- [ ] D. The LSTM (1997) was introduced before AlexNet (2012).
- [ ] E. The Perceptron (1958) was introduced after backpropagation was popularized (1986).

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Correct.
- B: 1950 comes before 1958.
- C: Rumelhart, Hinton and Williams, 1986.
- D: 1997 comes before 2012.
- E: Reversed: the Perceptron came first.

# 2. What is a model? What is a language model?

## MA-2.1

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A model is a function from inputs to outputs whose parameters are learned from data.
- [ ] B. A language model assigns probabilities to possible next tokens given the preceding tokens.
- [ ] C. A language model answers by looking up stored answers in a database of facts.
- [ ] D. Text generation is autoregressive: each chosen token is fed back as input for the next step.
- [ ] E. The model's weights are updated every time you send it a new prompt.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: output = f(input; θ).
- B: That is P(next token | previous tokens).
- C: It computes a distribution; it does not retrieve stored answers.
- D: Predict, sample, append, repeat.
- E: Inference does not update weights.

## MA-2.2

Check each statement that is true about how an LLM turns a prompt into output. Each statement is worth 1 point (5 points total).

- [ ] A. The logits are one raw score per token in the vocabulary.
- [ ] B. Softmax is applied to the logits to produce probabilities.
- [ ] C. Embeddings are produced after the softmax step.
- [ ] D. Changing a prompt, its context, or a setting is the same thing as training the model.
- [ ] E. After a token is sampled it is appended to the input and the process repeats.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Logits have length vocab_size.
- B: Softmax turns scores into a distribution.
- C: Embeddings come right after tokenization, before the Transformer layers.
- D: None of these change the weights.
- E: That is autoregressive generation.

# 3. Neural network structure and RNNs

## MA-3.1

Check each statement that is true about feedforward neural networks. Each statement is worth 1 point (5 points total).

- [ ] A. Each neuron computes an activation function applied to w · x + b.
- [ ] B. Without nonlinear activations, a stack of layers collapses into a single linear transformation.
- [ ] C. Backpropagation computes the gradients of the loss used to update the weights.
- [ ] D. A feedforward network contains a compiler that translates the network into English.
- [ ] E. In training, the loss is computed before the forward pass.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Weights, bias, then nonlinear activation.
- B: Linear composed with linear is linear.
- C: Forward pass, loss, backprop, gradient descent.
- D: No such component.
- E: The forward pass comes first; the loss measures its output.

## MA-3.2

Check each statement that is true about RNNs. Each statement is worth 1 point (5 points total).

- [ ] A. An RNN carries a hidden state from one time step to the next.
- [ ] B. An RNN processes a sequence step by step, which limits parallel training.
- [ ] C. Plain RNNs struggle with long-range dependencies because of vanishing or exploding gradients.
- [ ] D. LSTM and GRU gating eliminates the vanishing-gradient problem entirely.
- [ ] E. RNNs compute attention over all positions at once, exactly like Transformers.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: h_t depends on h_(t-1).
- B: Tokens are handled in order.
- C: Early information fades.
- D: Gating reduces it; it does not eliminate it.
- E: That describes Transformers.

# 4. Tokens

## MA-4.1

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A token can be a whole word, part of a word, a character, or punctuation.
- [ ] B. One word always equals exactly one token.
- [ ] C. Before the model sees text, it is converted into an array of integer token IDs.
- [ ] D. The context window limits how many tokens the model can process at once.
- [ ] E. "0.75 words per token" holds exactly for every language and tokenizer.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: It depends on the tokenizer.
- B: Rare or long words are split into several tokens.
- C: The array length is the number of tokens.
- D: It is the maximum length of the token array.
- E: It is an approximation for English and varies.

## MA-4.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The logits vector for next-token prediction has one entry per token in the vocabulary.
- [ ] B. The embedding matrix has shape vocab_size × d_model.
- [ ] C. A prompt of n tokens becomes an n × d_model matrix after embedding.
- [ ] D. Pricing, rate limits and context limits are measured in words.
- [ ] E. The logits vector has length equal to the number of tokens in the prompt.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Length vocab_size.
- B: Each ID selects one row.
- C: One embedding row per token.
- D: They are measured in tokens.
- E: Its length is the vocabulary size, regardless of prompt length.

# 5. Softmax and temperature

## MA-5.1

For logits [1, 2, 3] at T = 1, softmax gives about [0.090, 0.245, 0.665]. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The three probabilities sum to 1.
- [ ] B. Adding 100 to every logit changes the probabilities.
- [ ] C. Subtracting the maximum logit before exponentiating is for numerical stability and does not change the result.
- [ ] D. Lowering the temperature to 0.5 increases the probability of token 3.
- [ ] E. Changing the (positive) temperature can change which token has the highest probability.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Softmax outputs sum to 1.
- B: Softmax is shift-invariant.
- C: It prevents overflow.
- D: About 0.867 at T = 0.5.
- E: A positive T preserves order.

## MA-5.2

Check each statement that is true about temperature and sampling. Each statement is worth 1 point (5 points total).

- [ ] A. Temperature must be greater than zero in the softmax formula.
- [ ] B. As temperature grows very large, the distribution approaches uniform.
- [ ] C. Lowering temperature can fix an answer when the highest logit belongs to a wrong label.
- [ ] D. Higher temperature generally produces more varied outputs across runs.
- [ ] E. A token probability of 0.665 means there is a 66.5% chance the generated claim is factually correct.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: T divides the logits.
- B: Flatter as T increases.
- C: Lower T only concentrates more on the wrong label.
- D: A flatter distribution samples more variety.
- E: It is a sampling probability, not a truth probability.

## MA-5.3

Check each statement that is true about softmax. Each statement is worth 1 point (5 points total).

- [ ] A. Every softmax output is between 0 and 1.
- [ ] B. Softmax preserves order: the largest logit gets the largest probability.
- [ ] C. The raw logits [1, 2, 3] are already a probability distribution.
- [ ] D. With a fixed seed, sampled draws are reproducible.
- [ ] E. With a finite number of samples, observed counts match the expected counts exactly.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: By construction.
- B: Exponentiation is monotonic.
- C: They sum to 6.
- D: The seed fixes the random stream.
- E: Counts drift from expectation.

# 6. Attention and the Transformer

## MA-6.1

Check each statement that is true about self-attention. Each statement is worth 1 point (5 points total).

- [ ] A. Queries, keys and values are learned linear projections of token representations.
- [ ] B. Attention scores are computed as Q·Kᵀ divided by √d_k.
- [ ] C. Softmax over each query's scores produces weights that sum to 1.
- [ ] D. Attention on its own encodes word order, so positional information is unnecessary.
- [ ] E. In a decoder-only language model, a causal mask prevents tokens from attending to future tokens.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Q, K and V are projections.
- B: Scaled dot-product attention.
- C: Each row is normalized.
- D: Attention is order-agnostic; positional encoding is added.
- E: Tokens see only earlier tokens.

## MA-6.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The output for each token is a weighted sum of value vectors.
- [ ] B. Multi-head attention lets the model attend to different kinds of relationships in parallel.
- [ ] C. The vector for "bank" changing when "river" is nearby shows the model has understood the meaning of "bank".
- [ ] D. Surrounding tokens can influence a token's representation through attention.
- [ ] E. Attention was introduced so that the whole input must be squeezed into one fixed vector.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Weights times V.
- B: Several heads run at once.
- C: A changed vector is not evidence of understanding.
- D: That is how context changes it.
- E: Attention removes that bottleneck by letting the model look back at all positions.

# 7. Programming languages vs language models

## MA-7.1

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Code in a programming language follows a formal grammar and is interpreted unambiguously.
- [ ] B. Invalid syntax in a program produces an explicit error.
- [ ] C. A language model accepts ambiguous natural language and still produces an output.
- [ ] D. A language model runs outside the computer's normal instruction execution.
- [ ] E. The same prompt can produce different outputs when sampling at temperature above 0.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Formal grammar.
- B: Syntax errors and exceptions are explicit.
- C: It always produces something.
- D: It is ordinary arithmetic on CPUs and GPUs.
- E: Outputs are sampled.

## MA-7.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A language model's wrong answer can look as fluent as a right one.
- [ ] B. A program executes your instruction exactly, while a language model treats your prompt as context for predicting tokens.
- [ ] C. A deterministic program gives the same output for the same code and input.
- [ ] D. A language model's mistakes are reliably flagged as errors.
- [ ] E. At temperature above 0, a language model's output is deterministic.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Errors are silent.
- B: That is the key difference.
- C: Deterministic.
- D: They are not flagged.
- E: Sampling makes it probabilistic.

# 8. The strength of functions

## MA-8.1

Check each statement that is a strength of a well-written pure function compared with a language model. Each statement is worth 1 point (5 points total).

- [ ] A. Same input gives the same output.
- [ ] B. Behavior can be checked with unit tests.
- [ ] C. It can be composed with other functions and reused.
- [ ] D. It interprets vague, ambiguous instructions gracefully.
- [ ] E. It performs exact arithmetic and comparisons.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Deterministic.
- B: Testable.
- C: Composable.
- D: That is the language model's strength.
- E: Exact.

## MA-8.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A function's failures surface as explicit, inspectable errors.
- [ ] B. The course's design rule is to let the model generate and let functions check.
- [ ] C. The Chapter 1 probabilities() and sample() functions and the Chapter 2 JSON contract validator are examples of functions that check.
- [ ] D. The course builds mechanisms as Python functions so that Claude is not used at all.
- [ ] E. A pure function may return different outputs for the same input.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: An exception says what broke and where.
- B: Validators, schema checks, softmax, path policies.
- C: Course examples.
- D: Claude is used for the fuzzy parts.
- E: Same input gives the same output by definition.

# 9. Chapter 1: Division of Labor and The Gate

## MA-9.1

Under the course's division of labor, check each statement describing a task that belongs to the human. Each statement is worth 1 point (5 points total).

- [ ] A. Predicting the effect of temperature before running the code.
- [ ] B. Building the first version of the implementation.
- [ ] C. Deciding what the experimental result does and does not support.
- [ ] D. Organizing the observed sampling results into a table.
- [ ] E. Explaining one failure case without Claude supplying the answer.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The human predicts.
- B: The human builds the first version.
- C: The human decides.
- D: AI can organize the observed results.
- E: The human explains it.

## MA-9.2

Check each statement that is true about a working "gate". Each statement is worth 1 point (5 points total).

- [ ] A. A gate is capable of rejecting an output.
- [ ] B. A gate can rely on the model's stated confidence.
- [ ] C. A gate can stop a consistently repeated false answer.
- [ ] D. A gate is a check or a human decision placed before acceptance or action.
- [ ] E. A check that passes every output is a useful gate.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A check that cannot reject is not a gate.
- B: Model confidence is not a gate.
- C: That is Chapter 1's design question.
- D: Definition.
- E: It cannot reject anything.

## MA-9.3

Check each statement that is true about Chapter 1. Each statement is worth 1 point (5 points total).

- [ ] A. A repeatable answer can still be wrong.
- [ ] B. Lowering the temperature gets a consistently false answer through a real gate.
- [ ] C. AI should help diagnose Python errors after your first attempt.
- [ ] D. You should record what you delegated and what you did with the time saved.
- [ ] E. Training that rewards human approval cannot favor confident-sounding answers over correct ones.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Consistency is not correctness.
- B: A real gate still rejects it.
- C: Part of the AI side of the split.
- D: Record the split.
- E: It can.

# 10. Chapter 2: The three-response experiment and what the green cannot distinguish

## MA-10.1

A JSON schema validator passes (green). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The green cannot distinguish a true claim from a false claim in a correctly structured response.
- [ ] B. The green cannot distinguish a source ID that supports the claim from a valid source ID that does not.
- [ ] C. The green cannot distinguish malformed JSON from well-formed JSON.
- [ ] D. The green cannot distinguish a response with an extra unexpected field from one without.
- [ ] E. A green result tells you the claim is factually valid.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It checks structure, not truth.
- B: It checks the ID is valid, not that it supports the claim.
- C: That is exactly what it catches.
- D: Schema validity catches extra fields.
- E: Factual validity is a separate check.

## MA-10.2

Check each statement that is true about the three-response experiment. Each statement is worth 1 point (5 points total).

- [ ] A. Three identical responses prove the answer is correct.
- [ ] B. Variation in wording is not automatically a failure.
- [ ] C. You should record the exact prompt, all outputs, model label, date and interface.
- [ ] D. Factual correctness should be judged separately from surface variation.
- [ ] E. Temperature can be set in every Claude interface.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Consistency is not verification.
- B: Three different wordings can all be correct.
- C: Needed for reproducibility.
- D: Two different questions.
- E: Settings differ by model and interface.

## MA-10.3

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A format-pass rate measures how often the answers are factually correct.
- [ ] B. JSON validity, schema validity and factual validity are different checks.
- [ ] C. A passing test suite establishes only the behavior it tests.
- [ ] D. Held-out cases should be kept separate from the cases used to revise the prompt.
- [ ] E. When treating a prompt as an experimental intervention, you should change one feature at a time.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A format-pass rate is not an accuracy score.
- B: Parses, right fields and types, true and supported.
- C: Not universal reliability.
- D: Do not change the test after inspecting results.
- E: Isolate the effect.

# 11. The agentic loop

## MA-11.1

Check each statement that is true about an agentic loop. Each statement is worth 1 point (5 points total).

- [ ] A. Each action produces an observation that updates the state for the next step.
- [ ] B. The policy and the controller are different pieces.
- [ ] C. The loop should have a turn or budget limit.
- [ ] D. When the loop stops, the task has succeeded.
- [ ] E. Repeating the same search several times counts as progress.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: State, action, observation, update.
- B: The policy proposes; the controller runs the loop.
- C: Bound the loop.
- D: It may have exhausted its budget.
- E: Repeating the same action is not progress.

## MA-11.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Whether a system is an agent depends on the actions it can take, not on its product name.
- [ ] B. The policy proposes the next action and the controller executes it and enforces limits.
- [ ] C. A bounded loop cannot take an unauthorized action.
- [ ] D. The loop stops when the goal is met or the budget runs out.
- [ ] E. The difference between a chat system and an agent is the action surface.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Judge by capabilities and consequences.
- B: Different roles.
- C: It can still do one unauthorized thing, hence permissions.
- D: Two stopping conditions.
- E: What it can actually do.

# 12. Solve-verify asymmetry, fluency, and falsifiability

## MA-12.1

Check each statement that is true about solve-verify asymmetry. Each statement is worth 1 point (5 points total).

- [ ] A. Checking a completed Sudoku is easier than solving one.
- [ ] B. It suggests generating with a model and verifying with a cheap independent check.
- [ ] C. The asymmetry holds equally for every task.
- [ ] D. Asking the same model to confirm its own answer is an independent verification.
- [ ] E. When verifying is as hard as solving, the advantage disappears.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Classic example.
- B: Tests, validators, source lookup.
- C: It disappears when verifying is as hard as solving.
- D: It is not independent.
- E: E.g. judging a long novel argument with no ground truth.

## MA-12.2

Check each statement that is true about fluency. Each statement is worth 1 point (5 points total).

- [ ] A. A fluent answer is not necessarily a correct one.
- [ ] B. Training that rewards human approval can favor confident-sounding answers.
- [ ] C. A confident tone is a calibrated measure of how likely the answer is to be true.
- [ ] D. A wrong answer can be just as fluent as a right one.
- [ ] E. Fluency is evidence that an answer is correct.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Fluency is not evidence of correctness.
- B: Confidence can beat correctness.
- C: It is not calibrated.
- D: Smooth, grammatical, confident either way.
- E: It is not.

## MA-12.3

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "This function returns a sorted list for every input in test set X" is falsifiable as stated.
- [ ] B. "The model is intelligent in its own way" is falsifiable as stated.
- [ ] C. "For logits [1, 2, 3], lowering temperature to 0.5 raises token 3's probability above 0.8" is falsifiable as stated.
- [ ] D. "The new prompt is better" is falsifiable as stated.
- [ ] E. A claim is falsifiable if you can say what observation would show it is wrong.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A failing input would refute it.
- B: No observation could show it wrong.
- C: And true: about 0.867.
- D: Better at what, measured how, on which cases?
- E: Popper.
