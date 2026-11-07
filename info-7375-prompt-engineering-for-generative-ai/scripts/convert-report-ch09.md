# Conversion report: ch09-training-and-configuration (MA-ch09)

- Old MA: 61. Old essays: 61. New MA: 35 (0 problems on check_format).
- Dropped/merged: 26 old MA (about 20 near-duplicates merged into term-contrast questions, e.g. ch09.14-18 sigmoid/weight/bias/threshold into one; ch09.26-38 gradient/learning-rate/loss-history items into three; ch09.43-47 eval-set/leakage/selection merged; plus non-vocabulary calculation items ch09.5, 48, 49, 54 reduced to the term involved or dropped).
- Essays converted into MA content: ES-ch09.1-7, 8-13, 14-20, 21-25, 29, 33, 34, 35-41, 42-45, 46-48, 49-50, 52-55, 57-61 (the vocabulary or term-contrast skill folded into the matching question).
- NOT CONVERTED: ES-ch09.26, 27 (cost-threshold calculation), ES-ch09.9, 10 (zero-init loss value, floating-point derivation: procedure/calculation), ES-ch09.32 (feature scaling how-to), ES-ch09.51, 56 (report-writing and step-by-step procedure).

## Terms tested
weights :: learned numeric parameters of a model, changed only by training
prompt :: instruction text sent with a request
system prompt :: standing instruction supplied with each request
context :: text supplied to the model in a request, including retrieved passages
retrieval :: fetching passages into context at request time, without changing weights
fine-tuning :: continued training that updates weights
memory :: stored notes re-supplied in later prompts, not weight change
tool :: capability the host exposes to the model
permission :: host rule on what an agent may do
approval gate :: pause until a human confirms an action
sampling setting :: decoding control such as temperature or top-p
temperature :: rescales logits; lower is sharper, higher is flatter
top-p :: samples from the smallest token set whose probabilities add to p
logit :: unnormalized score before softmax
seed :: initializer that makes pseudo-random choices repeatable
reproducibility :: others can re-run and obtain the same result
ablation :: remove one component and measure the effect
few-shot example :: worked input/output pair placed in the prompt
parameter vs hyperparameter :: learned value vs chosen setting
learning rate :: size of each gradient step
gradient :: slope of the loss with respect to a parameter
epoch / batch / minibatch :: full pass / data used for one update / small random subset
convergence / stopping rule :: loss stops improving / criterion for ending training
loss function / cross-entropy :: penalty on predictions; punishes confident wrong answers
sigmoid / weight / bias / threshold :: score-to-probability map / feature influence / shift / decision cutoff
false positive / false negative :: negative called positive / positive called negative
precision vs recall :: share of predicted positives correct / share of actual positives found
calibration :: stated probabilities match observed frequencies
training / validation / test data :: fit / tune / final estimate
data leakage :: evaluation data influencing training
multiple comparisons :: best of many noisy scores is biased upward
numerical gradient check :: finite-difference test of a derivative
association / intervention / counterfactual :: rungs of the ladder of causation
confounder / Simpson's paradox :: variable affecting both cause and outcome / reversal on pooling
distribution shift / feedback loop :: changed data after deployment / predictions altering future data
pre-specification :: plan and prediction fixed before results
diff review :: human reading of a change
identification :: argument that a causal effect is estimable from data
