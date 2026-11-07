# Chapter 9: Training and configuration

## ES-ch09.1

A team uploads policy documents to an assistant product's project store and rewrites the project's system prompt. Answers improve, and a teammate writes up the result as "we trained the model on our policies." The product runs no fine-tuning job; it supplies the documents and prompt to the model with each request. Explain what actually changed, what the verb "trained" asserts, and why the distinction matters for what the team maintains, audits, and pays for.

**Points:** 5

**Rubric (1 point each):**

1. States that what changed is the input supplied to the model at request time (retrieved documents and prompt text), while the model's parameters are unchanged.
2. Defines training as updating parameters from data through an objective and an update rule, which yields a new stored set of weights.
3. Notes that a prompt change lives in a diffable text file that can be copied to another project or reverted at once, and that a document change lives in a corpus and a selection step and disappears if the corpus does.
4. Explains that the word decides what must be maintained and audited: a weights artifact with its data, objective, and settings for training, versus prompt versions and a corpus with its retrieval pipeline for the other changes.
5. Addresses cost: training needs a run, evaluation, and redeployment to reproduce, whereas prompt and corpus edits are cheap to change, so mislabeling the work misstates what it costs and what must be kept.

**Source:** Name the mutable object before you change it

## ES-ch09.2

Five kinds of thing can be changed to alter the behavior of an LLM-based system: the model's weights, the prompt, the supplied context, the tools and permissions, and the run-time sampling settings. For each, say where the change lives and what evidence shows that it changed.

**Points:** 5

**Rubric (1 point each):**

1. Weights: the change lives in the saved parameter values, and the evidence is those values together with the data, objective, learning rate, and budget that produced them.
2. Prompt: the change lives in instruction text and examples in a file or message, and the evidence is the two texts compared side by side.
3. Context: the change lives in the corpus or store and the selection step, and the evidence is the passages that actually entered the input.
4. Tools and permissions: the change lives in server code, configuration, and permission rules, and the evidence is the configuration diff plus the decision that authorized it.
5. Settings such as temperature: the change lives in run-time configuration, and the evidence is the recorded setting for each run; only the weights involve an optimizer.

**Source:** Name the mutable object before you change it

## ES-ch09.3

A product team ships four changes in one release: a rewritten system prompt, a new document in the knowledge base, a newly enabled tool, and a lower sampling temperature. Classify each change by the object it modifies and say how you would observe it. Then explain why a different output after the release does not by itself show that the model's weights changed.

**Points:** 5

**Rubric (1 point each):**

1. The rewritten system prompt modifies the prompt, and is observed by comparing the old and new texts.
2. The new document modifies the context or corpus, and is observed by checking whether its passages are selected into the input.
3. The enabled tool modifies the tools and capabilities, and is observed through the configuration diff, the tool-call logs, and the authorizing decision.
4. The lowered temperature modifies a run-time setting, and is observed through the recorded setting and repeated runs because sampling varies.
5. A changed output could come from any of these or from a model update or sampling variation, so a claim about weights needs evidence of a parameter update, not just different behavior.

**Source:** Name the mutable object before you change it

## ES-ch09.4

A user says, "The assistant followed my preferences a week later, so it must have learned from me." Give three non-training mechanisms by which behavior can persist across sessions, describe a test that separates persistence from learning, and say what a careful report should claim.

**Points:** 5

**Rubric (1 point each):**

1. Names persistence mechanisms that involve no parameter update, such as a saved system prompt re-supplied with each request, or stored memory records prepended or retrieved into the input.
2. Adds another persistent non-training change, such as retrieved documents in a workspace or permission rules in configuration.
3. States that training is identified by its mechanism, parameters updated from data through a loss-derived rule, and not by how long an effect lasts.
4. Describes the test: change one object with everything else held fixed, such as deleting the saved text and rerunning the same input, repeating runs because of sampling, and see whether the behavior goes with it.
5. Says a careful report describes the memory or context behavior observed, and avoids "learned the user" in the training sense without evidence of parameter updates.

**Source:** Persistence is not proof of training

## ES-ch09.5

A team wants to compare three ways of improving an assistant on a bounded task such as classifying support tickets: a baseline prompt, a prompt with few-shot examples, and a prompt plus retrieved context. Design the comparison. Explain how you ensure only one object changes between conditions, how you handle sampling variation, what you record, and what you can and cannot conclude.

**Points:** 5

**Rubric (1 point each):**

1. Changes only one object between conditions and holds the model, settings, and task items fixed.
2. Specifies the labeled evaluation set and writes predictions for each condition before running.
3. Handles sampling variation by repeating runs per condition and reporting the spread, rather than relying on one run.
4. Records the exact prompts, retrieved passages, model identifier, date, settings, and raw responses.
5. Limits the conclusion to how outputs respond to input changes under the recorded conditions, not to retraining of the model or to performance beyond the evaluated task.

**Source:** Persistence is not proof of training

## ES-ch09.6

A hosted assistant's answers to a fixed set of test questions change after a weekend. Explain why the output difference alone does not identify the cause, list the candidate causes, and describe the record a team should keep so that such changes can be attributed later.

**Points:** 5

**Rubric (1 point each):**

1. Lists several candidate causes: changed prompt text, different retrieved context, different tool output, a model version update, and sampling variation.
2. Explains that a before-and-after pair of outputs cannot by itself separate those causes.
3. Describes what to record for each object: both prompt texts, the corpus and the passages actually selected, the configuration diff and authorization, the settings for each run, and the model identifier.
4. Says not to invent a before state that cannot be seen, and to state which internal details remain unknown.
5. Proposes restoring each candidate one at a time and rerunning to attribute the change.

**Source:** What a production record can and cannot show

## ES-ch09.7

Three people each say their result is "reproducible": one supplies a training script with fixed data, hyperparameters, and seed; one supplies a recorded prompt and settings to replay against a hosted model; one supplies a configuration diff. Explain what reproducibility means in each case, what each depends on, and what counts as a successful repeat.

**Points:** 5

**Rubric (1 point each):**

1. For the training script, a rerun should give the same parameter values given the same code, data, seed, numeric libraries, and hardware.
2. For the hosted-model replay, the result depends on the service's model version, sampling, and infrastructure, so outputs may legitimately differ and the date, model, and settings must be recorded.
3. For the configuration diff, a reader can inspect exactly what changed, but the diff does not reproduce a behavior by itself.
4. Identical output is not the only acceptable repeat; a team can define success as a metric within tolerance or a similar pass rate over repeated runs.
5. A report should name which kind of reproducibility it offers and its dependencies.

**Source:** What a production record can and cannot show

## ES-ch09.8

A one-feature classifier has a weight and a bias, turns its score into a probability with the sigmoid function, and predicts label 1 when the probability passes a threshold. Explain what the weight and the bias each do, where the decision boundary comes from, and what the probability does and does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the classifier computes a score from the feature, with the weight setting how strongly the feature moves the score and the bias shifting it.
2. Explains that the sigmoid turns the score into a number between 0 and 1 that is read as a probability.
3. Explains that the decision comes from comparing the probability with a threshold, and that with a threshold of 0.5 the boundary is where the score is zero, which the bias moves along the feature.
4. Notes that the weight captures an association in the supplied data and the probability is the model's output under its objective, not evidence of cause.
5. Notes that a number between 0 and 1 is not automatically accurate, so the probabilities have to be checked against outcomes on data not used for training.

**Source:** The model: two numbers and a squashing function

## ES-ch09.9

A classifier starts with all parameters at zero. Explain what it predicts for every input, what that implies about the loss it starts with, and how this gives a baseline for judging training and a check on the training code.

**Points:** 5

**Rubric (1 point each):**

1. States that every input receives the same prediction, a probability of 0.5, so no relationship between the feature and the label has been encoded yet.
2. Explains that the starting loss is therefore that of an uninformed fifty-fifty guesser, the same whatever the balance of the labels.
3. Treats that value as the baseline that training should drive the loss below.
4. Notes that predicting the starting loss before running gives a check on the code: a different number signals a bug.
5. Notes that beating the baseline on the training data does not show that the model will beat it on new data.

**Source:** Loss makes the objective explicit

## ES-ch09.10

A direct implementation of a formula can fail in floating point for extreme inputs even though the mathematics is right. Using the sigmoid function as an example, explain why this happens, how an equivalent rewrite can fix it, and what a unit test of the fix does and does not establish.

**Points:** 5

**Rubric (1 point each):**

1. Explains that computers hold numbers with limited range and precision, so an intermediate value can overflow or round away even when the final answer is representable.
2. Explains the example: for a very large negative score the direct formula computes a huge exponential that overflows.
3. Describes the fix: an algebraically equivalent form chosen so that only safe values are exponentiated.
4. States that a test on an extreme input shows there is no failure at that input.
5. Notes that the test does not prove correctness for other inputs or edge cases, so the claim should stay limited to the behavior that was demonstrated.

**Source:** The model: two numbers and a squashing function

## ES-ch09.11

Explain what cross-entropy loss is for a classifier that outputs probabilities and how it treats confident right and confident wrong predictions. Say why accuracy and cross-entropy can disagree and what choosing a loss decides.

**Points:** 5

**Rubric (1 point each):**

1. Describes the loss as a penalty based on the probability the model gave to the true label: small when that probability is high and large when it is low.
2. Explains that a confident wrong prediction is penalized heavily and without a fixed limit, while a confident right one costs little.
3. Explains that accuracy counts only whether each decision was right, so two models with equal accuracy can have different cross-entropy.
4. Explains that minimizing the loss rewards honest probabilities, not only correct decisions.
5. Notes that the optimizer lowers whatever objective it is given, so the loss is a choice about the task made by people.

**Source:** Loss makes the objective explicit

## ES-ch09.12

A model outputs probabilities for three examples. On one it is confidently right, on one it is mildly right, and on one it leans toward the wrong label. Explain how the average loss is formed, which example contributes most and why, and what the average does and does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Explains that each example gets its own loss and that the training objective is the average of them.
2. Identifies the example where the model leaned the wrong way as contributing the most, and the confidently right one as contributing the least.
3. Notes that a few confidently wrong predictions can dominate the average.
4. Notes that the average is the number the optimizer lowers on this data, and that it differs from the fraction of examples classified correctly.
5. Notes that the average says nothing about unseen data or about the relative costs of different errors.

**Source:** Loss makes the objective explicit

## ES-ch09.13

A team switches to a different, supposedly equivalent way of computing its loss and the reported loss changes. Explain how you would check whether the two implementations really agree and what to do about any difference.

**Points:** 5

**Rubric (1 point each):**

1. Proposes computing both on the same small inputs for which the answer can be worked out by hand.
2. Proposes including extreme inputs, such as very confident predictions, where numerical problems appear.
3. Proposes comparing within a stated tolerance, since floating-point results should not be expected to match exactly.
4. Says to treat an unexplained disagreement as a bug in one of the two until it is explained, not as noise.
5. Says to report what was tested, so the claim of equivalence is limited to those cases.

**Source:** Loss makes the objective explicit

## ES-ch09.14

Explain, in words, what the gradient of a loss is, how it is used to update a classifier's parameters, and how the direction of an update can be predicted from the data before any code is run.

**Points:** 5

**Rubric (1 point each):**

1. Describes the gradient as how the loss changes as each parameter changes; it points toward higher loss.
2. Describes the update as a small step in the opposite direction, scaled by the learning rate.
3. Explains that the gradient is computed from the training data and the current parameter values, and averaged over the examples used.
4. Gives a prediction from the data: if larger feature values go with label 1, the first update raises the weight.
5. Explains that writing the prediction down before running gives a check that does not depend on the code's output.

**Source:** Derive the first update

## ES-ch09.15

An AI assistant writes a training loop for a small classifier. After one update the loss on the training data is a little lower. Explain what one training step should do, why the lower loss does not show the code is correct, and what stronger check you would add.

**Points:** 5

**Rubric (1 point each):**

1. States that one step should change the parameters slightly in the direction that lowers the training loss.
2. States that the loss on the same data should fall slightly after the step if the learning rate is small enough.
3. Explains that the direction of each parameter's change can be predicted from the data.
4. Explains that buggy code can also lower the loss, for example by taking a wrong-sized step, so a decrease is necessary evidence but not sufficient.
5. Proposes comparing the first step with a hand-worked expected value on a tiny dataset.

**Source:** Derive the first update

## ES-ch09.16

A developer's training code sums the per-example gradients instead of averaging them. Explain what difference this makes, why the training loss still goes down, and how a test could catch the mistake.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a summed gradient is N times the average, so it acts like a learning rate N times larger.
2. Notes that the direction is unchanged, so the loss still falls, perhaps even faster at first.
3. Concludes that a lower loss after an update does not show the code is correct.
4. Explains that the step grows with the dataset size, so the code can overshoot or diverge and its behavior depends on N.
5. Proposes a test that asserts the first-step parameters worked out by hand, or compares against a numerical check of the average loss.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.17

Describe how to check a hand-derived gradient numerically. State what the check establishes, what it cannot catch, and why making the step size smaller and smaller is not the answer.

**Points:** 5

**Rubric (1 point each):**

1. Describes the check: change a parameter slightly up and down, recompute the loss each time, and compare the estimated slope with the formula's value within a tolerance.
2. Notes that the check does not use the derivative formula, so it can catch algebra, sign or missing-factor errors.
3. States that it cannot catch a wrong objective or an error in the loss function itself, because both routes use the same coded loss.
4. Explains that very tiny steps make the estimate noisy because of the computer's limited precision, so a moderate step is used.
5. Recommends pairing it with a hand-computed expected value, so the code is checked by more than one independent route.

**Source:** Derive the first update

## ES-ch09.18

Describe what happens to gradient descent on a simple bowl-shaped loss as the learning rate is raised from very small to very large, and say what this suggests about choosing a learning rate for a real model.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a very small rate makes steady but slow progress and may not finish within the step budget.
2. Explains that a moderate rate can reach the minimum quickly.
3. Explains that a larger rate overshoots and oscillates around the minimum, and that a rate that is too large makes the loss grow and training diverge.
4. States that the safe limit depends on the shape of the loss and the scale of the features, which are not known in advance for a real model.
5. Concludes that there is no universal safe rate: test candidate rates on declared validation data and report all runs, including divergent ones.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.19

A training run has a fixed budget of 200 updates and no convergence test. Discuss what a low final training loss does and does not tell you about that budget, how to choose a stopping rule responsibly, and what happens on linearly separable data without regularization.

**Points:** 5

**Rubric (1 point each):**

1. States that a low final loss shows what the configured loop achieved, not that 200 updates was the right budget.
2. Names alternatives to a fixed count: a tolerance on loss change, early stopping on validation loss, or choosing the best checkpoint.
3. Says the rule should be fixed before looking at held-out results, since changing it after seeing them tunes to that set.
4. Explains that on separable data without regularization the loss keeps falling as the weights grow, so a lower loss is not convergence, and regularization or early stopping is needed.
5. Recommends recording the loss at each step, with validation loss, so the shape of the run can be seen.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.20

A student compares four learning rates by training with each and reporting the best result. Describe how to run and report such a comparison without turning it into a search for an attractive number.

**Points:** 5

**Rubric (1 point each):**

1. Holds the data, initial parameters, and step budget fixed and varies only the rate.
2. Fixes the evaluation criterion in advance and applies it to development data rather than training loss alone.
3. Keeps and reports every run, including those that diverge.
4. Reports the selection process: how many settings were tried, the criterion, and that the selected score is optimistic until confirmed on fresh test data.
5. Explains the risk otherwise: a final number is presented without the selection that produced it, so the comparison becomes a search.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.21

An engineer sets aside four evaluation points before training and never passes them to the training function. The engineer chose them near the same decision boundary as the training points, and the trained model classifies all four correctly. Write the claim this evidence supports, the claims it does not support, and what a broader claim would require.

**Points:** 5

**Rubric (1 point each):**

1. Explains that "held out" describes how the points were handled, that is, not used for fitting.
2. States the supported claim: these four constructed points are classified correctly at the stated threshold.
3. Lists claims not supported, such as generalization to a real population, calibration, or robustness.
4. States that a broader claim needs a justified sampling process, a task definition, and a larger evaluation with its uncertainty.
5. Notes that if the points later guide a choice, they become development data and are no longer an independent test.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.22

A team finds that 50 of its 200 evaluation examples were also in the training data. Before the leak, accuracy was 82% (164 of 200). After retraining with the leak, suppose all 50 copied examples are right and the other 150 stay at 82% (123 correct). Explain the reported number, how to detect and fix such leakage, and how to report the result honestly.

**Points:** 5

**Rubric (1 point each):**

1. Computes the reported accuracy as (123 + 50) / 200 = 86.5% and attributes the 4.5-point rise to memorization rather than better generalization.
2. Explains that the leaked items measure recall of training data, not performance on unseen data.
3. Notes that the 150 untouched examples still estimate unseen-data accuracy at 82%.
4. Describes detection and repair: check for exact and near duplicates across splits, split before preprocessing, rebuild the split, and retrain.
5. Says the report should disclose the leak and give the clean estimate rather than presenting 86.5%.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.23

Explain why tuning a model or prompt needs three data roles rather than two, what each role is used for, and what goes wrong when a single evaluation set is used to choose among 12 configurations.

**Points:** 5

**Rubric (1 point each):**

1. Assigns the roles: training data fit the parameters, a development set is tuned against (settings, prompts, stopping), and a test set is used once for the final estimate.
2. Explains that choosing among configurations by their score on a set turns that set into development data.
3. Explains that the winning score is optimistic because the winner was selected partly for favorable noise.
4. Notes that a development set loses independence with every reuse, so it may need to be refreshed.
5. Says to record the change of role when it happens and to build an independent evaluation if the claim requires one.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.24

A team scores 30 prompt variants on the same 100 questions. Suppose every variant truly has 70% accuracy; by the binomial distribution the expected best observed score is about 79%, and the best is at or above 75% in over 99% of repeated experiments. Explain what this means for a team that reports the top variant's score and how to report honestly.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the maximum of many noisy estimates is biased upward (the winner's curse).
2. States the magnitude: about 9 points of apparent improvement arise even though no variant is better.
3. Notes that trying more variants raises the expected maximum, so the number of variants tried must be reported.
4. Recommends confirming the winner on fresh questions that played no role in selection.
5. Recommends reporting intervals and sample size, and not claiming improvements from small differences between variants.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.25

A classifier gets 4 of 4 right on a small hand-built test set, and another gets 40 of 40 right. Using the fact that a classifier with true accuracy p gets a perfect score on n independent points with probability p^n (0.6^4 is about 0.13, 0.9^4 about 0.66, 0.95^4 about 0.81; 0.9^40 about 0.015, 0.95^40 about 0.13), evaluate whether true accuracies of 60%, 90%, and 95% are compatible with each result, and say what each result supports.

**Points:** 5

**Rubric (1 point each):**

1. Concludes that after 4 of 4, accuracies of 60%, 90%, and 95% are all plausible, with perfect-score probabilities of 0.13, 0.66, and 0.81.
2. Concludes that after 40 of 40, 60% is essentially ruled out and 90% is unlikely (about 0.015), while 95% remains plausible (about 0.13).
3. Notes that a perfect run bounds the error rate only loosely, roughly 3/n at 95% confidence.
4. Notes that more points narrow the plausible range, and that hand-built points do not sample any population anyway.
5. Says to report results with their uncertainty and never to equate a perfect small-sample score with 100% accuracy.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.26

A classifier decides whether to escalate a message to a human. A missed escalation costs 20 units and an unnecessary escalation costs 1 unit. On 1,000 messages at threshold 0.5, Model A makes 10 missed escalations and 40 unnecessary ones and has average log loss 0.30; Model B makes 25 missed and 10 unnecessary and has average log loss 0.28. Which model is better for the business, and what does this show about training loss as a measure of "better"? What should the objective or evaluation include?

**Points:** 5

**Rubric (1 point each):**

1. Computes the total costs: Model A is 10*20 + 40*1 = 240 and Model B is 25*20 + 10*1 = 510.
2. Observes that Model B has the lower log loss and fewer total errors (35 versus 50) yet the higher cost.
3. Explains that log loss weights errors by the confidence of the prediction, not by what each error costs, so it does not encode the business objective.
4. Proposes making the cost part of the objective or evaluation, for example weighted loss, a cost-based threshold, or an expected-cost metric.
5. Concludes that "better" is a task-level judgment, and that a falling training loss supports only the claim that training loss decreased.

**Source:** What a lower loss claims

## ES-ch09.27

For a classifier with calibrated probabilities, a missed positive costs 20 units and a false alarm costs 1 unit. Derive the probability threshold that minimizes expected cost, and discuss what changes if the probabilities are not calibrated.

**Points:** 5

**Rubric (1 point each):**

1. Writes the expected cost of predicting positive as (1-p)*1 and of predicting negative as p*20.
2. Derives that predicting positive is better when 20p > 1-p, so p > 1/21, about 0.048.
3. Notes that with equal costs the threshold is 0.5 and that it moves with the cost ratio.
4. States that this requires calibrated probabilities; if the model is over- or under-confident, the threshold must be chosen empirically on development data.
5. Notes that the threshold is a decision rule applied after scoring, so moving it changes decisions without changing the model's parameters.

**Source:** Score, probability, and decision are three layers

## ES-ch09.28

A model assigns probability 0.9 to each of 1,000 test items and 600 turn out positive. In a second evaluation, items are grouped by predicted probability: a group with mean prediction 0.2 (400 items, observed positive rate 0.10), a group at 0.5 (300 items, observed rate 0.45), and a group at 0.9 (300 items, observed rate 0.60). Explain what calibration is, say what the first case shows, compute the weighted average gap between predicted and observed rates for the second, and explain why a few correct extreme-probability predictions do not show calibration.

**Points:** 5

**Rubric (1 point each):**

1. Defines calibration: among items given probability p, about a fraction p should be positive.
2. Identifies the first case as overconfidence, with an observed rate of 0.6 against a stated 0.9.
3. Computes the weighted gap as (400*0.10 + 300*0.05 + 300*0.30) / 1000 = 0.145.
4. Explains that checking calibration needs enough labeled data in each probability group, for example a reliability diagram.
5. Notes that accuracy at a threshold can be high while calibration is poor, and that extreme probabilities on a few cases say nothing about frequencies.

**Source:** Score, probability, and decision are three layers

## ES-ch09.29

Distinguish the score, the probability, and the decision in a logistic classifier. Say what produces each, which of them training changes, and what happens when the threshold moves. Use w = 2, b = -3 with thresholds 0.5 and 0.8 (the score threshold for probability 0.8 is ln 4, about 1.386).

**Points:** 5

**Rubric (1 point each):**

1. States that the score is w*x + b from the parameters, the probability is the sigmoid of the score, and the decision applies a threshold to the probability.
2. States that training adjusts the parameters, while the threshold is chosen outside training.
3. Computes the boundary at x = 1.5 for threshold 0.5 and x = (1.386 + 3)/2, about 2.19, for threshold 0.8, with identical parameters.
4. Notes that the sigmoid is monotonic, so thresholding the probability is equivalent to thresholding the score.
5. Says to record all three layers and know which one a claim is about.

**Source:** Score, probability, and decision are three layers

## ES-ch09.30

Explain the role of the bias term in a one-feature classifier. Why might a learned bias come out near zero on one symmetric toy dataset, and why would it be a mistake to conclude that the bias can be dropped?

**Points:** 5

**Rubric (1 point each):**

1. States that the bias shifts where the decision boundary lies along the feature; without it the boundary is fixed at a feature value of zero.
2. Notes that data not centered at zero need a bias, or the boundary cannot be placed where the data call for it.
3. Explains that on symmetric data the pushes on the bias cancel, so the learned bias stays near zero.
4. Notes that removing a point or flipping a label breaks the symmetry and moves the bias.
5. Warns against generalizing from one symmetric toy dataset to the claim that biases are unnecessary.

**Source:** Score, probability, and decision are three layers

## ES-ch09.31

A one-feature classifier trained from zero on symmetric data in which larger feature values go with label 1 learns a positive weight and a bias near zero. Predict, with reasons, what happens to the learned weight, bias, boundary and final training loss if every label is flipped, and say how you would verify the prediction.

**Points:** 5

**Rubric (1 point each):**

1. Predicts that the learned weight becomes negative, since larger feature values now go with label 0.
2. Predicts that, because the data remain symmetric about zero, the bias stays near zero and the boundary stays near a feature value of zero.
3. Explains that flipping the labels mirrors the problem, so the final training loss should match the original run.
4. Notes that the starting predictions and the starting loss are the same in both runs, because nothing has been learned yet.
5. Says to verify by running both and comparing, with the prediction written down before the run.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.32

Explain how feature scale affects the training of a classifier by gradient descent, and say what to do about it.

**Points:** 5

**Rubric (1 point each):**

1. Notes that the weight's update scales with the feature value, while the bias's update has no feature factor.
2. Explains that large features produce large weight steps and can destabilize a fixed learning rate, while small features make progress slow.
3. Recommends standardizing features to zero mean and unit variance so one learning rate works across features.
4. Notes that changing units rescales the best weight inversely, leaving predictions unchanged if training converges.
5. Says to compute the standardization statistics on the training data and apply the same transform to held-out data, to avoid leakage.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.33

Compare full-batch gradient descent, minibatch stochastic gradient descent, and single-example stochastic gradient descent: how each estimates the gradient, the cost per update, and the noise. Then explain what is lost when a teaching implementation uses only full batches.

**Points:** 5

**Rubric (1 point each):**

1. Describes full-batch descent as using the exact average gradient, which is deterministic but costly per update on large data.
2. Describes minibatch descent as using a noisy but unbiased estimate, with cheaper updates, more updates per pass over the data, and batches that map well onto parallel hardware.
3. Describes single-example descent as the noisiest, often needing a smaller rate or averaging.
4. Notes that gradient noise and shuffling affect the optimization path and can influence how well the model generalizes.
5. Says a full-batch teaching loop is easy to trace but omits shuffling, minibatches and adaptive rates, so analogies to large-scale training are limited.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.34

A training routine returns only two numbers as its loss "history": the loss before the first update and the loss after the last. Say what you cannot conclude from them, what should be recorded instead, and what patterns you would look for.

**Points:** 5

**Rubric (1 point each):**

1. States that two values are not a learning curve.
2. Notes that they cannot show whether the loss fell steadily, oscillated, or spiked and recovered.
3. Recommends recording training loss at each step or every few steps, plus validation loss.
4. Names diagnostic patterns: divergence or NaN suggesting too high a rate, a plateau suggesting convergence or too low a rate, and training loss falling while validation loss rises suggesting overfitting.
5. Says to name outputs honestly, and not to call two endpoints a history or a curve.

**Source:** What a production record can and cannot show

## ES-ch09.35

Explain why cross-entropy is usually preferred to squared error for training a classifier that outputs probabilities, in terms of what happens to training when the model is confidently wrong.

**Points:** 5

**Rubric (1 point each):**

1. States that with cross-entropy the training signal stays strong when the model is confidently wrong.
2. States that with squared error on a squashed output the signal nearly vanishes when the output is saturated, so training stalls exactly when the model is most wrong.
3. Explains that the squashing function flattens at the extremes and squared error does not undo that.
4. Notes that cross-entropy corresponds naturally to treating labels as random outcomes with probabilities.
5. Concludes that the choice of objective affects how training behaves, not only the number that is reported.

**Source:** Loss makes the objective explicit

## ES-ch09.36

A support team wants an assistant to follow a new refund policy. Compare fine-tuning, prompt editing, retrieval over a policy document, and tool or permission changes by what each changes, how quickly it can be changed and reverted, how it can be audited, and when each is the right choice.

**Points:** 5

**Rubric (1 point each):**

1. Fine-tuning changes the weights, needs data, a training run, evaluation, and a new artifact to version and deploy.
2. Prompt editing changes text that is diffable and revertible at once, within the limits of the context window.
3. Retrieval lets a corpus update take effect without training, depends on the quality of the selection step, and suits knowledge that changes.
4. Tool and permission changes alter capability and governance, and are audited through a configuration diff and an authorization record.
5. Says there is no universal ranking; choose by reversibility, inspectability, cost, and the behavior needed (for example changing facts suit retrieval, and a consistent style might justify fine-tuning).

**Source:** Name the mutable object before you change it

## ES-ch09.37

A vendor says its assistant "learns each user." What would you ask to decide whether this is parameter learning or stored context, and what would you tell users about it?

**Points:** 5

**Rubric (1 point each):**

1. Asks how preferences are stored and used, whether prepended or retrieved into the input or used to update parameters.
2. Proposes a test: delete the stored records, rerun the same input, and see whether the behavior disappears.
3. Notes that per-user parameter learning would imply per-user weights or adapters, a training job, and data-handling obligations.
4. Notes that context supply implies visible and deletable records and possible selection failures.
5. Says the claim should describe the observed memory behavior and avoid "learned" in the training sense without evidence of parameter updates.

**Source:** Persistence is not proof of training

## ES-ch09.38

Explain why enabling a tool or changing a permission rule is a different kind of change from changing the model, and why describing such a change as "the model learned" is a problem.

**Points:** 5

**Rubric (1 point each):**

1. States that tools change capability: which actions and information sources the system can use.
2. States that permission rules change which proposed operations the runtime allows.
3. Notes that the model itself is unchanged by either.
4. Explains that calling it learning relabels a human governance decision as a machine property, hiding who decided and what should be audited.
5. Names the evidence: the configuration diff and the authorizing decision, and notes that tool outputs enter the context and can change answers.

**Source:** Name the mutable object before you change it

## ES-ch09.39

Explain what temperature does when sampling from a language model. For logits [3, 1, 0] the softmax probabilities are about (0.844, 0.114, 0.042) at T = 1, (0.980, 0.018, 0.002) at T = 0.5, and (0.629, 0.231, 0.140) at T = 2. Use them to describe the effect, say why a single run is insufficient for comparing two settings, and say why temperature is not a training change.

**Points:** 5

**Rubric (1 point each):**

1. States that logits are divided by T before the softmax.
2. Describes lower T as sharpening (0.844 rising to 0.980) and higher T as flattening.
3. Notes that T approaching 0 becomes greedy choice of the top token and large T approaches uniform sampling.
4. States that the parameters are unchanged and that temperature is a run-time setting to be recorded for each run.
5. Explains that sampling is random, so comparing settings requires repeated runs per setting.

**Source:** Name the mutable object before you change it

## ES-ch09.40

A logistic model fit to historical records of an online class has a positive weight on x, the number of reminder emails a student opened in the first month, for the label "passed." A dean proposes requiring every student to open the emails and expects pass rates to rise. Explain why the fitted model cannot tell whether the policy will work, give several explanations for the positive weight, and say what evidence would be needed.

**Points:** 5

**Rubric (1 point each):**

1. Separates the two questions: what label the model will assign at a given x is a prediction question, while what happens if students are required to open emails is an intervention question.
2. Explains that evaluating the function at a larger x gives the model's response to a changed input, not the class's response to a changed behavior.
3. Offers competing explanations for the positive weight: the emails help, students who are already on track open more emails (reverse causation), a common cause such as motivation or free time, or selection of students who stayed enrolled.
4. Names the evidence needed: a randomized trial or pilot, or a study design with explicitly defended causal assumptions and domain evidence.
5. Recommends stating the claim with its provisos, in the form "if we change x by doing D, the outcome changes by about this much, provided P, Q, and R."

**Source:** Decide what kind of question you are asking

## ES-ch09.41

Describe the three rungs of Pearl's ladder of causation with a medical example of each, and say which rung a standard supervised classifier answers and what limits movement up the ladder.

**Points:** 5

**Rubric (1 point each):**

1. Describes association as what goes with what, for example comparing recovery rates between patients who did and did not take a drug.
2. Describes intervention as what happens if we do something, for example giving the drug to everyone in a clinic.
3. Describes the counterfactual as what would have happened to this particular patient had they not taken the drug.
4. Places a supervised classifier at the association (prediction) rung.
5. Explains that interventional and counterfactual answers generally cannot be recovered from observational data alone without causal assumptions, and that more data does not supply those assumptions.

**Source:** Decide what kind of question you are asking

## ES-ch09.42

Two treatments were assigned by clinicians. In mild cases, X succeeded in 8 of 10 and Y in 70 of 90. In severe cases, X succeeded in 30 of 90 and Y in 2 of 10. Pooled, X succeeded in 38 of 100 and Y in 72 of 100. Explain how the pooled comparison can reverse the within-group comparison, what additional information you would need to decide which treatment is better, and why the right comparison depends on causal structure.

**Points:** 5

**Rubric (1 point each):**

1. Computes the within-group rates: mild 80% versus about 78%, severe about 33% versus 20%, so X is better in both groups.
2. Notes the pooled reversal: 38% for X versus 72% for Y.
3. Explains the cause: X was given mostly to severe cases (90 of its 100), severity strongly affects outcome, so severity confounds the pooled comparison.
4. Explains that stratifying is right if severity is a confounder, but pooling can be right if the grouping variable is a consequence of the treatment, so the choice needs causal assumptions that the table cannot supply.
5. Notes that randomized assignment of treatment would break the link between severity and assignment.

**Source:** Decide what kind of question you are asking

## ES-ch09.43

A model that flags at-risk students was fit on a year in which nobody acted on its flags. Next year advisors contact every flagged student. Explain why the model's predictions may not describe the new year and how the team could evaluate the effect of the contact.

**Points:** 5

**Rubric (1 point each):**

1. Explains that acting on predictions changes the process that generates the data, so a model fit before anyone acted may not describe the world afterwards.
2. Notes that flagged students who pass after contact may reflect a successful intervention, not model error.
3. Warns that refitting on post-intervention outcomes without recording who was contacted conflates prediction with the intervention's effect.
4. Proposes a design to evaluate the contact: randomize or hold out a comparison group of flagged students who are not contacted, and record who is contacted.
5. Notes that high accuracy on historical data gives no protection against feedback from the model's own use.

**Source:** Decide what kind of question you are asking

## ES-ch09.44

A researcher has a large observational dataset on job-training participation and later wages. Explain under what conditions a causal claim about the program could be defended, which threats must be addressed, and how a randomized experiment differs.

**Points:** 5

**Rubric (1 point each):**

1. Names confounding and self-selection, such as motivation affecting both participation and wages, as the central threats.
2. Explains that random assignment breaks the link between assignment and pre-existing differences in expectation.
3. Explains that an observational causal claim needs explicit assumptions, such as no unmeasured confounding given covariates, or a natural experiment, instrument, or difference-in-differences design, argued with domain evidence.
4. Notes that more data reduces variance but does not remove bias from confounding.
5. Recommends stating the claim with its provisos and testing sensitivity to violations of the assumptions.

**Source:** Decide what kind of question you are asking

## ES-ch09.45

An analyst asks a language model for help with a causal question about an observational dataset. Say what the model can and cannot reliably contribute, and explain who should own the identification judgment and why.

**Points:** 5

**Rubric (1 point each):**

1. Lists what the model can do: propose candidate confounders, write notation for a causal diagram, compute consequences under a structure the analyst states, and run code.
2. States that fluent text about causation is not identification of a causal effect in this dataset.
3. Notes that the model does not know the study design, data collection, or domain facts unless they are supplied and verified.
4. Explains that the person who will act on the result owns the identification judgment, choosing the variables and defending the assumed structure, since the model bears no consequences.
5. Says the model's assumptions should be labeled as assumptions rather than presented as established causation.

**Source:** What is Claude's here, and what is yours

## ES-ch09.46

A report on a small experiment states: average training loss fell from 0.69 to 0.11; six separately specified held-out points of the same pattern as the training data were all classified correctly. State the strongest claims this evidence supports, and list three claims it does not support with reasons.

**Points:** 5

**Rubric (1 point each):**

1. States the supported claims: the parameters were updated by the stated procedure, the training loss decreased from 0.69 to 0.11, and the six held-out points were classified correctly.
2. Rejects "the model generalizes," because six constructed points of the same pattern do not sample a real population.
3. Rejects "the probabilities are calibrated," because calibration needs a labeled sample large enough to compare probabilities with frequencies.
4. Rejects any causal claim that changing the feature changes a real-world outcome, because a fitted association does not identify an intervention effect.
5. Chooses verbs to match the evidence, such as "lowered the objective on the training pairs" instead of "generalizes."

**Source:** What a lower loss claims

## ES-ch09.47

A team is changing a classifier used to escalate messages to a human, and an AI coding assistant is available. Divide the work between the assistant and the responsible engineer, and explain which parts must stay with the engineer and why.

**Points:** 5

**Rubric (1 point each):**

1. Keeps the objective with the engineer: what "better" means, including the relative costs of missed and unnecessary escalations.
2. Keeps the evaluation set and the stopping rule with the engineer, decided before running.
3. Keeps with the engineer the decision of whether the stakeholder's question is a prediction or an intervention question, and the defense of any causal assumptions.
4. Delegates to the assistant derivations, code, runs, and tabulation, and has it challenge the plan and propose wrong versions, with the engineer verifying through independent routes.
5. Explains that the engineer signs or withholds the final claim because the engineer is accountable for it and the data hold no opinion about the objective.

**Source:** What is Claude's here, and what is yours

## ES-ch09.48

Before changing a model or prompt, a team writes down a plan. List what the plan should contain, and explain how it should be handled if results disappoint.

**Points:** 5

**Rubric (1 point each):**

1. Includes the objective: what "better" means and the metric that will be reported.
2. Includes the evaluation set, specified separately from the data used for tuning and fixed before results are seen.
3. Includes the stopping rule or budget.
4. Includes a description of what failure looks like, written before the run, and the wrong versions of the implementation that the tests must catch.
5. States that revising the plan is allowed but must be logged, that evaluation points already seen become development data, and that the claims must stay within what the plan supports.

**Source:** The gate: say what should change before you change it

## ES-ch09.49

Design three tests for a logistic-regression trainer that would catch these bugs: (a) the gradient is summed instead of averaged, (b) the feature value is multiplied into the bias update, and (c) evaluation points are included in the training list. For each, state the input and the assertion, and explain why a test that only checks that the loss decreased misses them.

**Points:** 5

**Rubric (1 point each):**

1. For (a), uses a small hand-solvable dataset and asserts the exact first-step parameters, which would be N times too large with a summed gradient.
2. For (b), uses data symmetric about zero and asserts that the bias stays at 0 after the first step, since the errors cancel.
3. For (c), asserts that the evaluation set and training set are disjoint, by identity or by duplicate check.
4. Explains that a "loss decreased" test passes for all three, because each can still reduce training loss.
5. Adds a mutation check: write each wrong version deliberately and confirm that the tests fail on it.

**Source:** The gate: say what should change before you change it

## ES-ch09.50

An AI assistant has produced a logistic-regression trainer and a set of tests for it. Describe how you would verify the work independently, and why tests written by the same assistant are not enough.

**Points:** 5

**Rubric (1 point each):**

1. Writes a dated prediction before running, such as the direction of the first update, with a statement of what a wrong result would look like.
2. Hand-derives the first-step numbers and compares them with the code's output.
3. Runs a finite-difference gradient check against the analytic gradient.
4. Explains that tests written by the same author from the same understanding may share a misreading, so add tests from your own specification and ask for a deliberately wrong version to see whether the tests reject it.
5. States that when the hand value and the code disagree, the disagreement must be explained, not resolved by changing the expected value to match the code.

**Source:** Build It: the baseline that lets you audit

## ES-ch09.51

Draft the closing section of a report on a small training experiment. State what such a section should list under what was checked, how it was checked, what was not checked, and what is not being claimed, and give an example of each. Explain why the "not checked" part matters.

**Points:** 5

**Rubric (1 point each):**

1. Lists the claims checked and the checks used, such as a hand-computed first update, a finite-difference check, and a held-out evaluation.
2. States how each check was done: by hand, by a test written before reading the code, by recomputation, or with an AI assistant's help, naming which parts.
3. Lists what was not checked, such as other datasets, rates, and step counts, calibration, or any real-world effect.
4. Lists claims not being made, such as that the model generalizes, that lower training loss means better, or that any input causes an outcome.
5. Explains that the not-checked part matters because only the person who did the work knows what was not done, and that withholding sign-off is an honest result when the evidence is insufficient.

**Source:** Ship It: the comparison report and its sign-off

## ES-ch09.52

Explain why a dated prediction should be written before running AI-generated training code. Then write a falsifiable prediction for the first gradient descent update of a one-feature logistic classifier from zero parameters on the pairs (-1, 1), (1, 0), (2, 0), giving the direction of the weight and bias changes with reasons.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a prediction written after seeing the output only describes the output.
2. Says a useful prediction states what a wrong result would look like, so it can be falsified.
3. Notes that all initial probabilities are 0.5, so the errors p - y are -0.5, 0.5, and 0.5.
4. Predicts that the averaged weight gradient is positive (about +0.67), so the weight moves negative, since larger x goes with label 0.
5. Predicts that the averaged bias gradient is positive (about +0.17), so the bias moves negative, and that a different sign points to a sign error or a missing feature factor.

**Source:** Derive the first update

## ES-ch09.53

Distinguish four claims about a trained classifier: "the model learned," "the model fits its training data," "the model generalizes," and "the model is useful." For each, say what evidence supports it and why a stronger claim cannot be inferred from a weaker one.

**Points:** 5

**Rubric (1 point each):**

1. For "learned," cites a change in parameter values produced by the update rule, which can be inspected directly.
2. For "fits the training data," cites a low training loss on the pairs the optimizer saw.
3. For "generalizes," requires evaluation on independent data drawn from the target distribution, reported with uncertainty.
4. For "is useful," requires task-level metrics tied to the real costs of errors, calibration where probabilities are used, and evidence from deployment conditions.
5. Explains that each stronger claim needs its own evidence, and that lower training loss alone cannot establish generalization or usefulness.

**Source:** What a lower loss claims

## ES-ch09.54

An engineer says: "After adding the policy PDF, accuracy on our 100-question set rose from 61% to 74%, so the model has learned the policy." Critique the claim and say what the engineer can legitimately claim and how to strengthen the evidence.

**Points:** 5

**Rubric (1 point each):**

1. Explains that adding a document supplies information in the input and does not train the model, and that removing the document should remove the gain.
2. Proposes checking which passages were retrieved and running an ablation with the document removed.
3. Warns that if the prompt or retrieval was tuned on the same 100 questions, those questions are development data, so a separate untouched test set is needed.
4. Notes that sampling and the sample size give uncertainty of several points on 100 questions, so repeated runs and an interval are needed.
5. States a defensible claim: with the document supplied, accuracy on this set was 74% versus 61% without it, under recorded conditions.

**Source:** Persistence is not proof of training

## ES-ch09.55

A team spends two weeks revising a prompt against the same 50 test questions and then reports the final score as the prompt's accuracy. Explain why the score is optimistic and how to restructure the process.

**Points:** 5

**Rubric (1 point each):**

1. Explains that revisions were chosen by their effect on those questions, so the set became development data.
2. Notes the risk of overfitting to the particular questions, for example by adding rules aimed at specific failures.
3. Recommends separating a development set for iteration from a test set that is locked and used once.
4. Recommends reporting all attempts and the run-to-run variation, not just the best result.
5. Notes that when a test set has been exposed it should be refreshed or replaced if an independent estimate is required.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.56

Describe the steps of training a simple classifier by gradient descent, including checking the inputs, choosing starting values, the repeated update, and what is recorded, and identify which choices are design decisions rather than learned quantities.

**Points:** 5

**Rubric (1 point each):**

1. Describes validating the inputs: labels are valid, features are finite, the number of steps is a positive integer and the learning rate is positive and finite.
2. Describes initializing the parameters, for example at zero, and recording the initial loss.
3. Describes each step: compute predictions, compare them with the labels, average the gradient contributions, and move the parameters against the gradient by the learning rate times the gradient.
4. Describes recording the final loss after the step budget and returning the parameters.
5. Identifies the learning rate, step budget, initialization, objective and data split as design decisions, not quantities the loop learns.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.57

Explain precisely what the statement "training loss decreased from 0.69 to 0.02" establishes and what it leaves open, addressing unseen data, the choice of objective, and the correctness of the code.

**Points:** 5

**Rubric (1 point each):**

1. States that it establishes that the update rule reduced the objective on the pairs it was shown.
2. States that it does not establish fit to unseen data, which requires held-out evaluation.
3. States that it does not establish that the objective was the right one for the task, which no dataset can settle.
4. Notes that it does not show the code is correct, since a bug such as an oversized step can lower the loss as well or faster.
5. Concludes that the report should say "training loss decreased" when that is what was measured.

**Source:** What a lower loss claims

## ES-ch09.58

A stakeholder asks, "If we raise the price by 10%, how many customers will we lose?" and offers a churn model fit on historical data. Decide whether this is a prediction or an intervention question, and explain what the model can and cannot tell you and what evidence would answer the question.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the question as interventional: it asks what happens if the company changes the price.
2. Explains that the churn model describes the association between historical features, including past prices, and churn.
3. Notes that past price changes may have been confounded, for example applied to certain segments or during special events, and that reverse causation is possible.
4. Proposes evidence: a randomized price test, a defended quasi-experimental design, or an estimate of price sensitivity under stated assumptions.
5. Says the model can help design or simulate scenarios under explicit assumptions, and the answer should be stated with its provisos.

**Source:** Decide what kind of question you are asking

## ES-ch09.59

Explain why a report on AI-assisted work should show which task was delegated to the assistant and which judgment the human retained, and what evidence of that split should exist.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the person whose name is on the claim is accountable for it.
2. Gives examples of delegated work (derivations, code, tabulation) versus retained judgment (objective, evaluation set, kind of question, assumptions).
3. Names evidence of the split, such as transcript lines, diffs, and commits showing who wrote what.
4. Notes that if the split is not in the record, it happened only in someone's head and cannot be audited.
5. Notes that an AI-drafted sign-off tends to omit what was not checked, because the system has no record of what the human did not do.

**Source:** The driver's seat

## ES-ch09.60

A fitted classifier has a positive weight on a feature x. Explain what the weight says, why the same change in x does not always change the predicted probability by the same amount, and why the weight alone does not show that x causes the outcome.

**Points:** 5

**Rubric (1 point each):**

1. States that a positive weight means larger values of x went with a higher predicted chance of label 1 in the training data, other features held fixed.
2. Notes that the size of the weight depends on the units in which x is measured.
3. Explains that the probability responds nonlinearly through the sigmoid, so the same change in x moves it most near the middle and least near 0 or 1.
4. Notes that the weight describes the data the model was fit on and may not hold in a different population.
5. Explains that the weight is an association and does not identify the effect of intervening on x.

**Source:** The model: two numbers and a squashing function

## ES-ch09.61

Explain why classifiers are trained with a smooth loss such as cross-entropy rather than directly maximizing accuracy, and say how accuracy and other decision metrics should still be used.

**Points:** 5

**Rubric (1 point each):**

1. Explains that accuracy at a threshold is piecewise constant in the parameters, so its gradient is zero almost everywhere and gives no update signal.
2. Explains that cross-entropy is smooth and graded, rewarding small improvements in confidence in the right label.
3. Notes that cross-entropy corresponds to maximum likelihood for Bernoulli labels.
4. States that the optimizer lowers whatever objective it is given, so the objective is a choice that should reflect the task.
5. Says accuracy, cost-based metrics, and calibration are reported as separate evaluation measures on independent data, and that a decreasing training loss does not guarantee they improve.

**Source:** Loss makes the objective explicit
