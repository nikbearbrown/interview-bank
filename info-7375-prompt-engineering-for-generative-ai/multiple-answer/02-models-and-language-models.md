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

