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

