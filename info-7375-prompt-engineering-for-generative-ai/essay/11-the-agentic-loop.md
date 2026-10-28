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

