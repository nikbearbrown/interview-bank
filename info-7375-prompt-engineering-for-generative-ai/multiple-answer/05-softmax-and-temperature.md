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

