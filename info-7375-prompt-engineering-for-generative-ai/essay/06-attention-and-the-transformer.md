# 6. Attention and the Transformer

## ES-6.1

Describe the steps of scaled dot-product attention, softmax(Q·Kᵀ / √d_k)·V, and explain what the √d_k does. Then explain why the changing vector for "bank" in "river bank" versus "bank account" does not show the model understood either sense.

**Points:** 5

**Rubric (1 point each):**

1. Scores every query against every key with a dot product.
2. Divides by √d_k to keep scores in a stable range.
3. Applies softmax so each row of weights sums to 1.
4. Outputs a weighted sum of the value vectors.
5. States that context changing a representation is not evidence of understanding.

