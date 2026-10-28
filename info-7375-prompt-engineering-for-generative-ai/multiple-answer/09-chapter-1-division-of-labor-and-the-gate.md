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

