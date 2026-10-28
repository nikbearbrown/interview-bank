# 5. Softmax and temperature

## ES-5.1

Logits [1, 2, 3] give p(token 3) of about 0.867 at T = 0.5, 0.665 at T = 1.0 and 0.506 at T = 2.0. Describe the trend, state what temperature does to the distribution, and explain why a low temperature cannot make a wrong answer true.

**Points:** 5

**Rubric (1 point each):**

1. States that p(token 3) falls as T rises (0.867, 0.665, 0.506).
2. Explains that lower T sharpens and higher T flattens the distribution.
3. Notes that as T goes to 0 the choice approaches greedy and as T grows it approaches uniform.
4. States that a positive T never reorders the tokens.
5. Explains that sampling probability is not truth probability, so concentrating on a wrong top token does not make it correct.

