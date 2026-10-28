# 6. Attention and the Transformer

## MA-6.1

Check each statement that is true about self-attention. Each statement is worth 1 point (5 points total).

- [ ] A. Queries, keys and values are learned linear projections of token representations.
- [ ] B. Attention scores are computed as Q·Kᵀ divided by √d_k.
- [ ] C. Softmax over each query's scores produces weights that sum to 1.
- [ ] D. Attention on its own encodes word order, so positional information is unnecessary.
- [ ] E. In a decoder-only language model, a causal mask prevents tokens from attending to future tokens.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Q, K and V are projections.
- B: Scaled dot-product attention.
- C: Each row is normalized.
- D: Attention is order-agnostic; positional encoding is added.
- E: Tokens see only earlier tokens.

## MA-6.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The output for each token is a weighted sum of value vectors.
- [ ] B. Multi-head attention lets the model attend to different kinds of relationships in parallel.
- [ ] C. The vector for "bank" changing when "river" is nearby shows the model has understood the meaning of "bank".
- [ ] D. Surrounding tokens can influence a token's representation through attention.
- [ ] E. Attention was introduced so that the whole input must be squeezed into one fixed vector.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Weights times V.
- B: Several heads run at once.
- C: A changed vector is not evidence of understanding.
- D: That is how context changes it.
- E: Attention removes that bottleneck by letting the model look back at all positions.

