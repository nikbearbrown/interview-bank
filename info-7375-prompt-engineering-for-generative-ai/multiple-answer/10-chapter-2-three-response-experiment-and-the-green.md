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

