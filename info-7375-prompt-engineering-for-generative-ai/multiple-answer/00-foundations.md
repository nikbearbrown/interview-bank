# Foundations (midterm-prep sections 1-12)

Questions on the background material and the first core ideas of working with generative AI, in section order. Each section keeps its own heading below.

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

- A: Vaswani and colleagues published the Transformer paper in 2017.
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
- [ ] C. Within a single forward pass, the embedding lookup happens after the softmax over the logits.
- [ ] D. Changing a prompt, its context, or a setting is the same thing as training the model.
- [ ] E. After a token is sampled it is appended to the input and the process repeats.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Logits have length vocab_size.
- B: Softmax turns scores into a distribution.
- C: Token IDs are embedded first; the logits and the softmax come at the end of the pass.
- D: None of these change the weights.
- E: That is autoregressive generation.

# 3. Neural network structure and RNNs

## MA-3.1

Check each statement that is true about feedforward neural networks. Each statement is worth 1 point (5 points total).

- [ ] A. Each neuron computes an activation function applied to w · x + b.
- [ ] B. Without nonlinear activations, a stack of layers collapses into a single linear transformation.
- [ ] C. Backpropagation computes the gradients of the loss used to update the weights.
- [ ] D. Backpropagation is the step that changes the weights, while the optimizer only computes the gradients.
- [ ] E. In training, the loss is computed before the forward pass.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Weights, bias, then nonlinear activation.
- B: Linear composed with linear is linear.
- C: Forward pass, loss, backprop, gradient descent.
- D: Reversed: backpropagation computes gradients and the optimizer uses them to update the weights.
- E: The forward pass comes first; the loss measures its output.

## MA-3.2

Check each statement that is true about RNNs. Each statement is worth 1 point (5 points total).

- [ ] A. An RNN carries a hidden state from one time step to the next.
- [ ] B. An RNN processes a sequence step by step, which limits parallel training.
- [ ] C. Plain RNNs struggle with long-range dependencies because of vanishing or exploding gradients.
- [ ] D. LSTM and GRU gating eliminates the vanishing-gradient problem entirely.
- [ ] E. Replacing a plain RNN with an LSTM removes the need to process tokens one at a time.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: h_t depends on h_(t-1).
- B: Tokens are handled in order.
- C: Early information fades or blows up as gradients pass through many steps.
- D: Gating reduces the problem; it does not eliminate it.
- E: An LSTM still updates its state step by step, so training stays sequential across time.

# 4. Tokens

## MA-4.1

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A token can be a whole word, part of a word, a character, or punctuation.
- [ ] B. A tokenizer maps each word to exactly one token.
- [ ] C. Before the model sees text, it is converted into an array of integer token IDs.
- [ ] D. The context window limits how many tokens the model can process at once.
- [ ] E. Roughly 0.75 words per token is a fixed constant that applies equally to English prose, source code and other languages.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: It depends on the tokenizer.
- B: Rare or long words are split into several tokens.
- C: The array length is the number of tokens.
- D: It is the maximum length of the token array.
- E: It is an approximation for English prose and varies with language, content and tokenizer.

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
- [ ] C. Observing that the vector for "bank" differs when "river" is nearby proves the model understands both senses of "bank".
- [ ] D. Surrounding tokens can influence a token's representation through attention.
- [ ] E. Attention was introduced to compress the whole input into a single fixed-size vector.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Weights times V.
- B: Several heads run at once.
- C: It shows the representation depends on context; whether the model handles both senses has to be tested on its behavior.
- D: That is how context changes it.
- E: The opposite: attention lets the model look back at every input position instead of relying on one fixed-size summary.

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
- [ ] C. A deterministic program with no randomness or external state gives the same output for the same code and input.
- [ ] D. A language model's mistakes are reliably flagged as errors.
- [ ] E. A sufficiently precise natural-language instruction guarantees that a model will follow it exactly, the way a compiler follows code.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Errors are silent.
- B: That is the key difference.
- C: Same code and input, no hidden state, same output.
- D: A wrong answer arrives in the same format as a right one, with no exception raised.
- E: An instruction is context for prediction, not an executed command, so even precise wording gives no guarantee.

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

A team adopts a design principle for an LLM-based system: let the model generate, and let ordinary code check. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A function's failures surface as explicit, inspectable errors rather than as fluent wrong text.
- [ ] B. A schema validator that rejects a model response with a missing required field is an example of a function acting as a checker.
- [ ] C. The principle means the model should be removed and replaced entirely by hand-written code.
- [ ] D. A checker implemented as a pure function can return different results on repeated calls with the same input.
- [ ] E. Because a function-based check is deterministic, passing it proves the output is correct.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: An exception or failed assertion says what broke and where, unlike a plausible-sounding wrong answer.
- B: Validators, unit tests, arithmetic recomputation and permission checks are all functions applied to model output.
- C: The model still does the fuzzy work (drafting, interpreting vague input); code checks what can be specified exactly.
- D: A pure function returns the same output for the same input by definition.
- E: A check establishes only what it tests; a response can satisfy every check and still be wrong in a way no check examines.

# 9. Division of labor and acceptance gates

## MA-9.1

A student is using an AI coding assistant to build a small program whose behavior they must be able to defend. Check each statement that describes a sound way to divide the work between the student, who is accountable for the result, and the assistant. Each statement is worth 1 point (5 points total).

- [ ] A. Writing down the expected behavior, and tests that would fail a plausible but wrong version, before asking the assistant to implement it.
- [ ] B. Asking the assistant to tabulate or reformat raw results that the student has already collected.
- [ ] C. Asking the assistant what the experiment shows and copying its conclusion into the report without checking it against the data.
- [ ] D. Letting the assistant write the tests that judge its own implementation, without reading them.
- [ ] E. Predicting the outcome of an experiment before running it, so the result can contradict the prediction.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Tests written first define "correct" independently of the implementation, so a wrong version can be caught.
- B: Mechanical reformatting of data you already hold is low risk and easy to verify by comparison.
- C: What the evidence supports is a judgment for the accountable person, and a fluent conclusion can overreach the data.
- D: Tests written by the thing under test can encode the same misunderstanding as the code, so they prove little.
- E: A prior prediction lets a surprise expose a bug or a misunderstanding.

## MA-9.2

A gate is a check or human decision that an output must pass before it is accepted or acted on. Check each statement that is true about gates for model outputs. Each statement is worth 1 point (5 points total).

- [ ] A. A gate is meaningful only if it is capable of rejecting an output.
- [ ] B. A model's own stated confidence is a sufficient gate.
- [ ] C. A gate that compares answers against an authoritative source can stop a false answer that the model repeats consistently.
- [ ] D. Writing a rule in the system prompt enforces it as reliably as a check implemented in the code around the model.
- [ ] E. A gate that has accepted every output so far can be assumed to be working.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A check that cannot reject anything gives false assurance.
- B: A model can state high confidence in a wrong answer; confidence is not independent evidence.
- C: An external reference does not care how consistent or fluent the answer is.
- D: A system prompt is a request the model may fail to follow; enforcement belongs in code outside the model.
- E: Never rejecting may mean the outputs were all good or that the check cannot fail; test it against known-bad outputs.

## MA-9.3

A model is asked the same factual question 20 times. At a low temperature (0.2) it returns the same wrong answer every time. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The repetition shows the output is stable, not that it is correct.
- [ ] B. Lowering the temperature to 0 would make the answer correct.
- [ ] C. Checking the answer against an authoritative source would expose the error.
- [ ] D. Agreement across 20 runs is strong evidence of correctness, because errors would be random and would not repeat.
- [ ] E. A reference answer or retrieved source is a stronger basis for accepting the answer than agreement among runs.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Consistency is a property of the sampling, not of the facts.
- B: Lower temperature concentrates probability on the model's top choice; it adds no knowledge, so a wrong top choice stays wrong.
- C: An independent reference can contradict the answer however stable it is.
- D: Errors from training data or from how the model ranks continuations are systematic, so they repeat.
- E: Agreement among runs of one model measures repeatability; a reference measures correctness.

# 10. Format validity versus factual validity

## MA-10.1

A model must answer from supplied sources and return JSON like {"answer": "...", "cites": ["src-7"]}. A validator checks three things: the output parses as JSON, the required fields have the right types, and every cited identifier appears in the supplied source list. A response passes the validator. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The pass does not show that the claim in "answer" is true.
- [ ] B. The pass does not show that the cited source supports the answer; it shows only that the cited identifier exists.
- [ ] C. A response with malformed JSON could still pass, since the validator examines content rather than syntax.
- [ ] D. A 100% pass rate on this validator over a test set shows that answer accuracy is 100%.
- [ ] E. Measuring accuracy would need a content-level check, such as comparison with reference answers, an entailment test or human review.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The validator examines structure, not truth; a well-formed response can state something false.
- B: A valid identifier can point to a source that says something different from the answer.
- C: Parsing is the first thing the validator checks, so malformed JSON fails.
- D: A pass rate measures only what the validator checks, which here is format and identifier existence.
- E: Accuracy is a statement about content, so it needs a check that looks at content.

## MA-10.2

An engineer sends one factual-question prompt to a model three times and reads three answers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Three identical answers prove the answer is correct.
- [ ] B. Three answers that differ in wording are not automatically a failure, because phrasing and factual correctness are separate questions.
- [ ] C. To make the check reproducible, the engineer should record the exact prompt, the outputs, the model name and version, the date and the sampling settings.
- [ ] D. Factual correctness should be judged against an independent reference, separately from how much the wording varies.
- [ ] E. Because every chat interface exposes the temperature setting, the sampling settings do not need to be recorded.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Consistency is not verification; a model can repeat the same error.
- B: Three differently worded answers can all be correct.
- C: Without those details no one can reproduce or audit the observation.
- D: Wording variation and correctness are two different questions with two different measures.
- E: Many interfaces do not expose temperature, and defaults change between models and versions, so the settings in force should be written down.

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

An agent loop works like this: a policy (the model) proposes the next action, a controller (the program around it) executes the action, the result comes back as an observation, and the state is updated. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Each action's result becomes an observation that updates the state used for the next decision.
- [ ] B. A cap on the number of steps is best enforced by the controller, not left to the policy's own judgment.
- [ ] C. If the loop stops because it reached its step limit, the task has succeeded.
- [ ] D. Repeating the same search several times with the same result counts as progress toward the goal.
- [ ] E. A step or budget limit is still needed when the model has been told in its prompt to stop when it is finished.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: State, action, observation, update, repeat.
- B: The policy can loop, misjudge that it is done or ignore an instruction; a limit in the surrounding program does not depend on the model complying.
- C: Hitting the limit means the budget ran out, which says nothing about whether the goal was met.
- D: A repeated action with an unchanged observation adds no new information.
- E: An instruction in the prompt is a request, not enforcement, so the limit has to exist outside the model.

## MA-11.2

Two systems use the same model. System X takes a question and returns text. System Y can call a search tool, read files and run shell commands in a loop until a goal is met or a step budget is exhausted. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The main difference between X and Y is that Y can take actions whose results feed back into its next decision.
- [ ] B. Y qualifies as an agent only if a human approves every single action.
- [ ] C. Capping Y at 20 steps guarantees it cannot take an unauthorized action.
- [ ] D. Whether Y counts as an agent depends mainly on the product's marketing name rather than on what it can do.
- [ ] E. Restricting Y to read-only tools changes what its mistakes can cost, even though the loop itself is unchanged.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The action surface and the feedback from its results are what separate Y from a text-in, text-out system.
- B: Autonomy varies; many agents act without per-action approval, and approval is a design choice.
- C: A single step can already be unauthorized, so a step cap limits duration, not the kind of action; permissions are needed.
- D: Judge a system by its capabilities and the consequences of its actions, not by what it is called.
- E: A read-only tool set cannot modify or delete anything, so errors are cheaper to recover from.

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

- A: Checking each row, column and box is quick, while finding the solution requires search.
- B: Tests, validators, source lookup.
- C: It disappears when verifying is as hard as solving.
- D: It is not independent.
- E: E.g. judging a long novel argument with no ground truth.

## MA-12.2

Check each statement that is true about fluency. Each statement is worth 1 point (5 points total).

- [ ] A. A smooth, grammatical answer is good evidence that the claim in it is correct.
- [ ] B. Training that rewards human approval can favor confident-sounding answers.
- [ ] C. A confident tone is a calibrated measure of how likely the answer is to be true.
- [ ] D. Asking a model to state its confidence as a percentage gives a number that reliably matches how often it is right.
- [ ] E. A fabricated citation can read exactly like a real one.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Fluency is a property of the language, not evidence about the facts.
- B: Raters often prefer confident, agreeable answers, and training on that preference can reward them over correct ones.
- C: Tone is not tied to the probability of being right.
- D: Stated confidence is often miscalibrated unless it has been checked against outcomes.
- E: Authors, titles and formats can all be generated plausibly, so the look of a citation says nothing about whether it exists.

## MA-12.3

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "This function returns a sorted list for every input in test set X" is falsifiable as stated.
- [ ] B. "The model is intelligent in its own way" is falsifiable as stated.
- [ ] C. "For logits [1, 2, 3], lowering temperature to 0.5 raises token 3's probability above 0.8" is falsifiable as stated.
- [ ] D. "The new prompt is better" is falsifiable as stated.
- [ ] E. A claim is falsifiable if you can say what observation would show it is wrong.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A single failing input would refute it.
- B: No observation could show it wrong.
- C: And true: about 0.867.
- D: Better at what, measured how, on which cases?
- E: That is the criterion Popper proposed for separating testable claims from untestable ones.
