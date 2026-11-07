# Conversion report: ch01-next-token-prediction-and-sampling (MA-ch01)

- Old MA: 61. Old essay: 60. New MA: 36 (true-count spread: 3 one, 14 two, 12 three, 7 four).
- Dropped/merged MA: 25 (non-vocabulary calculations and code trivia removed: MA-ch01.12 reading-time sum, .13 6ND compute, .14 GPU memory, .41/.42 binomial and standard error, .43/.44 sampler code and counts, .40 sampler code; near-duplicates merged: .33-.37 temperature family into 2 questions, .31/.32/.37/.55 softmax into 2, .53/.61 into 1, .45/.47 seed).
- Essays converted into MA content (folded into the 36): ES-ch01.1-3, 5-9, 11, 16-23, 25-26, 29, 32-37, 43-47, 51-52, 54-55, 57-58, 60.
- NOT CONVERTED: ES-ch01.4 (cost calculation), 10 (perplexity calculation), 12 (gradient step walkthrough, procedure), 13 (reading-time calculation), 14 (compute calculation), 15 (memory calculation), 24 (attention cost scaling calculation), 27 and 28 (design and latency calculation, term parts covered), 30, 31 (softmax computation and proof), 38, 39 (statistical calculation), 40, 41, 42 (experiment and test design, procedure), 48 (sequence probability calculation), 49, 50 (opinion on "stochastic parrot" and "autocomplete"), 53 (prompt-writing procedure), 56 (energy arithmetic), 59 (majority-vote probability calculation).

## Terms tested (term :: definition)

### Tokens and context
token :: a unit of text the tokenizer produces (a word, a fragment of a word, or punctuation)
tokenizer :: the component that converts text to token IDs from a fixed vocabulary and back
vocabulary :: the inventory of token pieces the tokenizer can emit
context window :: the maximum number of tokens a model can take in on one call, shared by prompt and reply
parameters (weights) :: the learned numbers in the model, fixed during inference
stateless API :: a service that keeps no conversation between calls, so the caller resends the history
max_tokens :: a setting that caps the number of output tokens, counted in tokens not words
embedding :: a learned vector of numbers representing a token

### Architecture
attention :: the mechanism that mixes information across token positions
feed-forward step :: the per-token transformation inside a layer using learned parameters
positional information :: information added so the model can tell word order
interpretability :: the study of what a model's internal parts compute
attention weight :: how much one token draws on another in a layer, not a causal explanation

### Generation and decoding
autoregressive :: choosing each token given the tokens before it, including the model's own earlier output
logits :: the raw per-token scores the model outputs before normalization
softmax :: the function that turns scores into non-negative probabilities summing to one
temperature :: a setting that rescales logits before softmax, sharpening or flattening the distribution
top-k :: truncation to the k highest-probability tokens
top-p (nucleus) :: truncation to the smallest set of top tokens whose cumulative probability reaches p
greedy decoding :: picking the highest-probability token at each step
sampling :: drawing the next token at random in proportion to its probability
beam search :: keeping several candidate sequences and favouring high overall sequence probability
seed :: a value fixing the random-number stream used in sampling
time to first token :: the delay before the first generated token appears
streaming :: showing tokens as they are generated
overflow :: a number too large to represent, which becomes infinity

### Training and behaviour
pretraining :: training a base model on next-token prediction over a large corpus
base model :: a pretrained model that continues text and does not yet follow instructions
instruction tuning :: further training on instruction and response examples
preference tuning :: further training on human comparisons of replies
sycophancy :: tendency to agree with the user over the facts
loss :: the negative log of the probability assigned to the true next token
perplexity :: a summary of average per-token uncertainty; lower fits the text better
causal masking :: hiding later tokens during training so the model cannot copy the target
training cutoff :: the point after which the training data holds no text
retrieval :: fetching documents at call time and placing them in the prompt
fine-tuning :: changing the parameters by training further on new data

### Reliability
hallucination :: fluent output that is false or unsupported by a source
prompt injection :: untrusted input text that tries to override the developer's instructions
calibration :: stated confidence matching how often answers are right
verbalized confidence :: a confidence number the model writes as generated text
token probability :: the probability assigned to a generated token
repeatability vs correctness :: the same output each time is not the same as a correct output
