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

