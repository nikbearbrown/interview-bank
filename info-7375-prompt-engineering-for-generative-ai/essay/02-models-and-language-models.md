# 2. What is a model? What is a language model?

## ES-2.1

Trace what happens between typing a prompt and receiving the first generated token, naming each stage. Then explain why sending a prompt does not change the model's weights.

**Points:** 5

**Rubric (1 point each):**

1. Text is split into tokens and mapped to integer token IDs.
2. Token IDs are looked up as embeddings.
3. Transformer layers produce logits, one score per vocabulary token.
4. Softmax converts logits to probabilities and one token is sampled.
5. States that a prompt is input to inference, not training, so weights stay fixed.

