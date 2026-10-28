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

