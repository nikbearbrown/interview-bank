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

