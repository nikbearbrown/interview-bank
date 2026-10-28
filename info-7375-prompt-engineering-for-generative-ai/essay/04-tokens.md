# 4. Tokens

## ES-4.1

A model has a vocabulary of 50,000 tokens and an embedding size of 768. A prompt is tokenized into 12 tokens. Give (a) the size of the token ID array, (b) the size of the embedded input matrix, and (c) the size of the logits vector for the next-token prediction. Explain why (c) does not depend on the prompt length.

**Points:** 5

**Rubric (1 point each):**

1. (a) The token ID array has length 12.
2. (b) The embedded input is 12 × 768.
3. (c) The logits vector has length 50,000.
4. Explains logits give one score for every vocabulary token, so length is vocab_size.
5. Notes the context window limits the token array length, not the logits length.

