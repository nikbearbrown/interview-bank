# 3. Neural network structure and RNNs

## MA-3.1

Check each statement that is true about feedforward neural networks. Each statement is worth 1 point (5 points total).

- [ ] A. Each neuron computes an activation function applied to w · x + b.
- [ ] B. Without nonlinear activations, a stack of layers collapses into a single linear transformation.
- [ ] C. Backpropagation computes the gradients of the loss used to update the weights.
- [ ] D. A feedforward network contains a compiler that translates the network into English.
- [ ] E. In training, the loss is computed before the forward pass.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Weights, bias, then nonlinear activation.
- B: Linear composed with linear is linear.
- C: Forward pass, loss, backprop, gradient descent.
- D: No such component.
- E: The forward pass comes first; the loss measures its output.

## MA-3.2

Check each statement that is true about RNNs. Each statement is worth 1 point (5 points total).

- [ ] A. An RNN carries a hidden state from one time step to the next.
- [ ] B. An RNN processes a sequence step by step, which limits parallel training.
- [ ] C. Plain RNNs struggle with long-range dependencies because of vanishing or exploding gradients.
- [ ] D. LSTM and GRU gating eliminates the vanishing-gradient problem entirely.
- [ ] E. RNNs compute attention over all positions at once, exactly like Transformers.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: h_t depends on h_(t-1).
- B: Tokens are handled in order.
- C: Early information fades.
- D: Gating reduces it; it does not eliminate it.
- E: That describes Transformers.

