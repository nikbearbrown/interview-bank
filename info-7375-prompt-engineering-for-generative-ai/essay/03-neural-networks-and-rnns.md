# 3. Neural network structure and RNNs

## ES-3.1

Compare how an RNN and a Transformer handle a long sequence. Cover how each carries information, whether training can be parallelized, and what happens to long-range dependencies.

**Points:** 5

**Rubric (1 point each):**

1. RNN passes information through a hidden state, one step at a time.
2. RNN training is hard to parallelize because steps are sequential.
3. RNN long-range dependencies suffer from vanishing or exploding gradients.
4. Transformer uses attention so every position can look at every other position directly.
5. Transformer training runs in parallel; notes LSTM/GRU only reduce the RNN problem.

