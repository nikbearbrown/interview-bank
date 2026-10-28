# 4. Tokens

## MA-4.1

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A token can be a whole word, part of a word, a character, or punctuation.
- [ ] B. One word always equals exactly one token.
- [ ] C. Before the model sees text, it is converted into an array of integer token IDs.
- [ ] D. The context window limits how many tokens the model can process at once.
- [ ] E. "0.75 words per token" holds exactly for every language and tokenizer.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: It depends on the tokenizer.
- B: Rare or long words are split into several tokens.
- C: The array length is the number of tokens.
- D: It is the maximum length of the token array.
- E: It is an approximation for English and varies.

## MA-4.2

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The logits vector for next-token prediction has one entry per token in the vocabulary.
- [ ] B. The embedding matrix has shape vocab_size × d_model.
- [ ] C. A prompt of n tokens becomes an n × d_model matrix after embedding.
- [ ] D. Pricing, rate limits and context limits are measured in words.
- [ ] E. The logits vector has length equal to the number of tokens in the prompt.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Length vocab_size.
- B: Each ID selects one row.
- C: One embedding row per token.
- D: They are measured in tokens.
- E: Its length is the vocabulary size, regardless of prompt length.

