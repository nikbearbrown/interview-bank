# Chapter 5: Model explainability

## MA-ch05.1

A bank compares four setups for credit decisions: (1) a sparse logistic regression on eight standardized inputs; (2) a decision tree of depth 3; (3) a gradient-boosted ensemble of 400 trees whose predictions are explained afterwards with Shapley values; (4) a neural network whose individual decisions are explained afterwards with LIME, a method that fits a simple surrogate model to the network's outputs on perturbed copies of one input. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Computing Shapley values for setup (3) turns the ensemble into a model that is interpretable by design.
- [ ] B. In setup (1) the fitted coefficients are a global description of how every score is computed, and that description is part of the model itself.
- [ ] C. For setup (2), a post-hoc explanation method has to be run before anyone can say how a given decision was reached.
- [ ] D. A LIME explanation in setup (4) describes the network's behavior near one input and need not describe its behavior elsewhere.
- [ ] E. An explanation produced after the fact from a trained model is guaranteed to be an accurate description of the computation that model performs.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Shapley values are a post-hoc description of a model that stays as opaque as before; interpretability by design comes from the structure of the model.
- B: The log-odds are a fixed weighted sum of the inputs, so the coefficients describe every prediction and are not bolted on afterwards.
- C: The root-to-leaf path of a small tree is the computation itself, so a decision can be read directly without an added method.
- D: LIME fits a simple surrogate to the model's behavior on perturbed points around one input, so it is local and approximate.
- E: Post-hoc methods approximate or summarize the model and can be unstable or off target; being computed from the model does not guarantee fidelity.

**Source:** Three words that don't mean the same thing

## MA-ch05.2

An analyst holds a trained classifier and four questions. Q1: for one applicant, how much of the gap between that applicant's score and the average score is attributable to each input? Q2: for one denied applicant, what small change to the inputs would change the decision? Q3: near one applicant, what simple model approximates the classifier's behavior? Q4: across a held-out set, how much does accuracy fall when one input's values are scrambled? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Fitting a local surrogate model on perturbed points near the applicant, as LIME does, answers Q4.
- [ ] B. A counterfactual search is designed to answer Q2, so more than one different valid answer can exist for the same applicant.
- [ ] C. Q4 concerns the model's behavior over a whole data set, while Q1, Q2 and Q3 each concern a single applicant.
- [ ] D. Shapley values are designed to answer Q1, so their answer depends on the reference the gap is measured against.
- [ ] E. A large Shapley value for an input means a small change to that input would flip the decision, so Shapley values answer Q2.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A local surrogate describes behavior near one input, while Q4 asks about the model's reliance on an input across a data set, which permutation importance addresses.
- B: Counterfactual methods search for altered inputs that change the output, and many different alterations can flip the same decision.
- C: Q4 averages over many rows to describe the model's reliance on an input, whereas the other three questions are about one applicant's decision.
- D: Shapley values split the prediction minus a reference prediction across the inputs, so changing the reference changes the split.
- E: A value measures contribution to the gap from the reference, not the distance to the decision boundary; a large value can sit far from the threshold.

**Source:** Counterfactuals are closer to what you actually want

## MA-ch05.3

A delivery-time model is additive: predicted minutes = 20 + 3 x distance_km + 5 x raining + 2 x items, where raining is 1 or 0. Across historical orders the averages are distance 6 km, raining 0.3 and items 4, so the model's average prediction is 47.5 minutes. One order has distance 10 km, raining = 1 and items = 2, and the model predicts 59 minutes. Treat the inputs as independent and compute Shapley values for this order against the average: the value of a subset of inputs is the expected prediction when those inputs are fixed at this order's values and the others are averaged over the historical data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The Shapley value of distance would still be +12 for an order with the same distance but different raining and items, since the model has no interaction terms.
- [ ] B. The three Shapley values sum to 11.5 minutes, the gap between this order's prediction and the average prediction.
- [ ] C. The Shapley value of items is +4 minutes: this order has fewer items than average, and fewer items shorten the trip.
- [ ] D. The Shapley value of raining is +5 minutes, the full coefficient; this order has raining = 1 and the model is additive.
- [ ] E. The Shapley value of distance is +12 minutes, the largest contribution of the three inputs.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: In an additive model an input's marginal contribution is the same for every coalition of other inputs, so its Shapley value is its coefficient times its deviation from the average.
- B: 12 + 3.5 - 4 = 11.5, which equals 59 - 47.5.
- C: 2 x (2 - 4) = -4 minutes; fewer items than average lowers the prediction.
- D: The average of raining is 0.3, so the value is 5 x (1 - 0.3) = 3.5, not 5.
- E: 3 x (10 - 6) = 12 minutes.

**Source:** The mathematics of Shapley values

## MA-ch05.4

A lender's score is 0.04 x income (in thousands) - 0.5 x late payments + 0.3 x years of credit history. An applicant with income 40, 2 late payments and 3 years of history has a score of 1.5 and is denied. The lender explains the denial with Shapley values (inputs treated as independent; the value of a subset is the expected score with those inputs fixed at the applicant's values and the rest set to a reference group's averages). Reference group P is all applicants, with averages 55 (income), 1 (late payments) and 8 (years). Reference group Q is approved applicants only, with averages 120, 0.2 and 11. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The two explanations differ because the scoring model changed between the two computations, even though the applicant is the same.
- [ ] B. Against group Q, the three values sum to -6.5, the applicant's score of 1.5 minus the approved applicants' average score of 8.0.
- [ ] C. Because Shapley values are computed from the model alone, the choice of reference group cannot change which input is reported as the main reason.
- [ ] D. Against group Q, income is the largest negative contributor to the denial, at -3.2, because 40 is far below that group's average of 120.
- [ ] E. Against group P, years of credit history is the largest negative contributor to the denial, at -1.5.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The model is identical in both computations; only the reference averages differ.
- B: The approved applicants' average score is 0.04 x 120 - 0.5 x 0.2 + 0.3 x 11 = 8.0, and 1.5 - 8.0 = -6.5, which matches -3.2 - 0.9 - 2.4.
- C: The main reason switches from years of history to income when the reference changes, so the reference is part of what the explanation says.
- D: Against Q the values are income -3.2, late payments -0.9 and years -2.4.
- E: Against P the values are income -0.6, late payments -0.5 and years -1.5.

**Source:** The mathematics of Shapley values

## MA-ch05.5

A screening rule outputs 1 (approve) only when both of two verification flags, x1 (income verified) and x2 (employment verified), equal 1; otherwise it outputs 0. For an applicant with (x1, x2) = (1, 1), a Shapley explanation uses the all-zero applicant (0, 0) as its reference. Shapley values satisfy efficiency (they sum to the output minus the reference output), symmetry (inputs that play interchangeable roles receive equal values) and the dummy property (an input that changes the output in no coalition of other inputs receives zero). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because switching x1 on while x2 stays off changes nothing, x1 satisfies the Dummy property and its Shapley value is 0.
- [ ] B. An attribution that gave x1 the value 1 and x2 the value 0 because x1 comes first in the input vector would satisfy the Symmetry property.
- [ ] C. Switching off x1 alone drops the output by 1, as does switching off x2 alone, so the one-at-a-time effects add up to more than the 1 unit being explained.
- [ ] D. The Shapley value of x1 is 0.5: its marginal contribution is 0 when it is added first and 1 when it is added after x2.
- [ ] E. The two Shapley values sum to 1, since they split the difference between this applicant's output and the reference output.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Dummy requires zero marginal contribution in every coalition, and adding x1 when x2 is on raises the output by 1.
- B: The rule and the reference are symmetric in x1 and x2, so Symmetry requires equal values; ordering in the input vector is irrelevant.
- C: From (1,1), removing either flag drops the output by 1, so the one-at-a-time effects sum to 2 against a total of 1; they double count an interaction.
- D: Averaging x1's marginal contribution over the two orderings gives (0 + 1) / 2 = 0.5; by symmetry x2 receives 0.5 as well.
- E: Efficiency: the values add to f(1,1) - f(0,0) = 1.

**Source:** The four axioms

## MA-ch05.6

In a data set two columns are exact copies of each other: x2 = x1 in every row (values -1, 0 or 1, average 0). Three models are trained and all are put into a trial: Model 1 predicts 4 x x1, Model 2 predicts 4 x x2, and Model 3 predicts 2 x x1 + 2 x x2. For a new row with x1 = x2 = 1.5, Shapley values are computed by fixing the chosen inputs at the new row's values and averaging the model's prediction over the data set's rows for the remaining inputs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Models whose outputs are identical on every observed row can still receive different attributions.
- [ ] B. For Model 3 the two Shapley values add to 6, the gap between its prediction for the new row and its average prediction.
- [ ] C. The Shapley values for (x1, x2) are (6, 0) for Model 1 and (0, 6) for Model 2.
- [ ] D. Model 1's value of 0 for x2 shows that x2 carries no information about the outcome in this data set.
- [ ] E. The three models make identical predictions on every row of the data set, so no accuracy measure on that data set can tell them apart.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Attributions describe how each model computes its output, including how it treats rows where x1 and x2 differ, so identical outputs on the data do not force identical attributions.
- B: Model 3 predicts 2 x 1.5 + 2 x 1.5 = 6 for the new row and averages 0, so by efficiency its values add to 6 (they are 3 and 3 by symmetry).
- C: For Model 1, fixing x2 does nothing to the prediction, so x1 takes all 6; Model 2 mirrors this.
- D: x2 is a perfect copy of x1, so it carries exactly as much information as x1; Model 1 simply happened not to read it.
- E: With x2 = x1 everywhere, 4x1, 4x2 and 2x1 + 2x2 coincide on every observed row.

**Source:** The correlated feature problem

## MA-ch05.7

A model predicts 4 x x1 and ignores x2 entirely. In the population x2 is an exact copy of x1 (average 0). For a row with x1 = x2 = 1.5 the prediction is 6 and the average prediction is 0. Two ways of valuing a subset of fixed inputs are compared. In the marginal version, the unfixed inputs are drawn independently of the fixed ones from their own distributions. In the conditional version, the unfixed inputs are drawn from their distribution given the fixed ones. Efficiency means the values sum to the prediction minus the average prediction. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With the marginal version, x1 receives 6 and x2 receives 0, since the model never reads x2 and the inputs are drawn independently.
- [ ] B. With the conditional version, efficiency fails: x1 receives less than the 6 it received in the marginal version.
- [ ] C. The conditional values show that the model reads x2; x2 receives a nonzero value.
- [ ] D. With the conditional version, x1 receives 3 and x2 receives 3, splitting the 6 equally because knowing either input pins down the other.
- [ ] E. The marginal version is wrong because it ignores the correlation between the inputs, so the conditional version is the correct one.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Fixing x1 gives 6; fixing x2 alone leaves x1 drawn independently with average 0, so the prediction stays at 0.
- B: Both versions sum to 6, so efficiency holds in both; they only distribute it differently.
- C: The model's formula does not contain x2; the credit arises because x2 is informative about x1.
- D: Given x2 = 1.5, x1 is also 1.5, so fixing either input gives 6 and the credit is split equally.
- E: The versions answer different questions (what the model computes versus what the information in each input implies), and each has costs, such as off-data inputs for the marginal one.

**Source:** The correlated feature problem

## MA-ch05.8

A product team averages two models' predicted probabilities to form an ensemble, f = (f1 + f2) / 2. For one case, Shapley values against the same reference, in percentage points, are: Model 1 gives income +10, tenure -4, region +2; Model 2 gives income +6, tenure +2, region -5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The ensemble's value for region is more negative than its value in either individual model.
- [ ] B. The ensemble's Shapley value for income is +8 points, the average of the two models' values.
- [ ] C. The ensemble's Shapley value for tenure is +1 point, so tenure raises the ensemble's prediction for this case.
- [ ] D. An ensemble that averages two models has Shapley values that cannot be obtained from the two models' values and must be recomputed from scratch.
- [ ] E. The ensemble's three Shapley values add to 5.5 points, the gap between its prediction for this case and its average prediction.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The ensemble value is (2 - 5) / 2 = -1.5, which is less negative than Model 2's -5.
- B: (10 + 6) / 2 = 8.
- C: (-4 + 2) / 2 = -1, so tenure lowers the ensemble prediction.
- D: Shapley values are linear in the value function, so a weighted average of models has the same weighted average of Shapley values.
- E: The ensemble values are 8, -1 and -1.5, which sum to 5.5, equal to the average of the models' totals (8 + 3) / 2.

**Source:** The four axioms

## MA-ch05.9

An analyst computes exact Shapley values for a model by evaluating the model on every subset of its n input features, with the other features averaged out. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Averaging marginal contributions over more random feature orderings brings a sampling estimate closer to the exact values, because each ordering is an unbiased draw.
- [ ] B. With n = 20 inputs there are 2^20 = 1,048,576 subsets to evaluate, one for each choice of included inputs.
- [ ] C. Going from n = 10 inputs to n = 20 inputs doubles the work, because the number of inputs doubled and each input adds one evaluation.
- [ ] D. For ensembles of decision trees, algorithms that use the tree structure can compute Shapley values for a specified value function without enumerating every subset.
- [ ] E. Going from n = 10 inputs to n = 20 inputs multiplies the number of subsets by 1,024.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Each sampled ordering gives an unbiased draw of the marginal contribution, so the average converges on the exact value as the number of orderings grows.
- B: 2^20 = 1,048,576.
- C: Cost grows exponentially in n, not linearly, so doubling n squares the number of subsets.
- D: Tree-specific algorithms exploit the small set of distinct paths in a tree and run in time polynomial in tree size.
- E: 2^20 / 2^10 = 2^10 = 1,024.

**Source:** Computational shortcuts: from exact to approximate

## MA-ch05.10

A model predicts y = s x x, where x takes the values -2, -1, 0, 1 or 2 equally often and s is a binary input, independent of x, equal to +1 for half of the customers and -1 for the other half. The model fits the training data without error. A partial dependence plot (PDP) for x shows, at each value of x, the model's prediction averaged over the data's values of s. Individual conditional expectation (ICE) curves show one line per customer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The PDP for x is flat at 0 across the whole range of x, because opposite predictions cancel.
- [ ] B. The PDP equals the pointwise average of the ICE curves over the customers in the data.
- [ ] C. The ICE curves fall into two groups, one with slope +1 and one with slope -1 as x increases.
- [ ] D. The flat PDP shows that x has no influence on any individual customer's prediction.
- [ ] E. Shuffling the x column among customers and re-scoring would leave the squared error unchanged, as the flat PDP implies.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: At each x the predictions +x and -x occur equally often, so their average is 0.
- B: A partial dependence curve is by definition the average of the individual curves over the data.
- C: Customers with s = +1 follow y = x and those with s = -1 follow y = -x.
- D: Opposite effects cancel in the average; every customer's prediction moves one unit per unit of x.
- E: After shuffling x, the error rises from 0 to about 4 (twice the variance of x), so the model relies heavily on x.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.11

A random-forest classifier is trained on data in which column x2 is an exact copy of column x1; some trees split on x1 and others on x2. On a held-out set the accuracy is 0.90. Shuffling only x1 lowers held-out accuracy to 0.80; shuffling only x2 lowers it to 0.80; shuffling both together lowers it to 0.60. The permutation importance of an input is the drop in held-out accuracy when its column is shuffled. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Shuffling both columns together shows a reliance on the shared information of 0.30, larger than the two single-column importances added together.
- [ ] B. The small single-column importances show that the information in x1 and x2 contributes little to the model's accuracy.
- [ ] C. Taken one at a time, the permutation importance is 0.10 for x1 and 0.10 for x2.
- [ ] D. Shuffling only x1 produces rows where x1 and x2 disagree, a combination absent from real data, so single-column importance can misstate the reliance.
- [ ] E. An input with positive permutation importance on held-out data must have a causal effect on the real-world outcome.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 0.90 - 0.60 = 0.30, which exceeds 0.10 + 0.10 = 0.20.
- B: Trees that split on the other copy are unaffected, which hides the loss; scrambling both shows the information matters a great deal.
- C: 0.90 - 0.80 = 0.10 for each column.
- D: Single-column shuffling breaks a dependence that always holds in the real data, so the model is scored on unrealistic rows.
- E: Permutation importance measures the model's reliance on an input; a model can rely on a confounded or spurious cue.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.12

A team fits a random forest with fully grown trees on 3,000 training rows and 12 inputs, one of which is a randomly assigned customer ID (unique per row and unrelated to the label). The forest's built-in impurity-based importance, which totals the impurity reduction of each input's splits on the training data, ranks the ID 4th of 12. Permutation importance computed on 1,000 held-out rows gives the ID about 0.000. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Impurity-based importance is computed from the fitted model, so it cannot be misleading when inputs differ in their number of distinct values.
- [ ] B. A held-out permutation importance near zero indicates that the model's use of the ID does not help predict new rows.
- [ ] C. The ID's rank shows that the ID influences the real-world label; it outranks eight of the real inputs.
- [ ] D. Inputs with many distinct values offer more candidate split points, which can inflate impurity-based importance relative to inputs with few values.
- [ ] E. An input can earn a high impurity-based importance by helping the trees fit noise in the training rows.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Being derived from the fitted model does not protect against the bias toward high-cardinality inputs or against overfit.
- B: Shuffling a column on unseen data does not hurt accuracy if the model's use of it adds nothing there.
- C: The ranking reflects overfitting to noise; the ID is unrelated to the label by construction.
- D: More possible thresholds give more chances for a chance split to look good, a known bias of impurity measures.
- E: Splits on a unique ID can isolate individual training rows, which lowers training impurity without any generalizable signal.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.13

A tiny model is f(x1, x2) = min(x1 + x2, 1), the sum capped at 1. At the input (1, 1) a saliency method reports the partial derivatives of f. Integrated gradients (IG) with the baseline (0, 0) integrates the gradient along the straight line from the baseline to the input and satisfies completeness, meaning its attributions sum to f(input) - f(baseline). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. IG with a baseline equal to the input itself would give attributions of 0, so the baseline is part of what an IG explanation says.
- [ ] B. A zero gradient at (1, 1) proves that neither input has any effect on the output.
- [ ] C. IG assigns 0.5 to each input, and the two attributions add to f(1, 1) - f(0, 0) = 1.
- [ ] D. Both partial derivatives at (1, 1) are 0, so a plain gradient saliency map assigns no importance to either input.
- [ ] E. IG assigns 1 to x1 and 0 to x2 because x1 is listed first and so absorbs the whole change.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: With the baseline at (1, 1) the path has zero length, so both attributions are 0; IG measures change from a chosen baseline, and the choice changes the answer.
- B: The output is 1 at (1, 1) and 0 at (0, 0); the flat region is saturation, in which the local slope hides the inputs' role.
- C: Along the path the sum is below the cap for the first half, where both derivatives are 1, giving 0.5 each.
- D: At (1, 1) the sum is 2, beyond the cap, so the function is flat there and both derivatives are 0.
- E: The function is symmetric in x1 and x2, so any sensible attribution gives them equal values.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.14

A team tests a saliency-map method for a chest X-ray classifier. In test 1 they replace the trained weights with random weights and recompute the maps; the rank correlation between the original and random-weight maps averages 0.93 over 500 images. In test 2 they retrain on randomly shuffled training labels (training accuracy reaches 100% by memorization); the maps again correlate about 0.9 with the original maps. Radiologists rate the original maps as clinically sensible. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The high correlations indicate that the method's output depends little on what the model learned.
- [ ] B. A method with these results is producing maps driven largely by the structure of the input image rather than by the model's learned parameters.
- [ ] C. If the maps had changed substantially in both tests, that would prove the method is faithful to the model.
- [ ] D. Test 2 shows that a model trained on shuffled labels classifies new images as accurately as the original model does.
- [ ] E. The radiologists' approval of the original maps is sufficient evidence that the maps explain the trained classifier.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A faithful explanation of a model should change when the model's parameters are replaced by noise.
- B: Maps that survive randomization behave like functions of the image, such as edge detectors, not of the classifier.
- C: Passing such tests is necessary but not sufficient; a method can respond to the model and still misdescribe it.
- D: A model fit to random labels memorizes training images and cannot generalize, so its accuracy on new images is near chance.
- E: Approval measures plausibility; maps that ignore the model can still look sensible.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## MA-ch05.15

Two attribution methods, P and Q, rank the pixels of chest X-rays by importance. On 300 test images the classifier's average predicted probability of pneumonia is 0.92. Replacing the top 10% of pixels by each method's ranking with the image's mean grey value lowers the average probability to 0.90 for P and to 0.40 for Q. Replacing a random 10% of pixels lowers it to 0.91. The standard error of each of these averages is about 0.01. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Q's large drop shows that the highlighted regions cause pneumonia in patients, not just that the classifier responds to them.
- [ ] B. P's average drop of 0.02 is twice the random drop of 0.01, which establishes that P's ranking is meaningfully better than random.
- [ ] C. If radiologists find P's maps more convincing than Q's, it follows that P is the more faithful method, since they know what pneumonia looks like.
- [ ] D. By this deletion test, Q's ranking reflects the classifier's behavior better than P's does, since removing its top pixels cuts the output far more.
- [ ] E. Grey patches can create images unlike any the classifier was trained on, so part of Q's drop may reflect sensitivity to the patches rather than importance.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The test concerns what the classifier responds to, not what causes disease in the patient.
- B: A difference of 0.01 between averages that each carry a standard error of 0.01 is well within noise.
- C: Persuasiveness to people measures plausibility, which is separate from faithfulness to the model.
- D: Removing Q's top pixels lowers the output by 0.52, far more than random removal, while P's drop is near the random level.
- E: Deletion tests evaluate the model on off-distribution inputs, so the drop mixes importance with artifact sensitivity.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.16

Fifty clinicians rate heat maps from two explanation methods, M1 and M2, on a 1-to-5 scale for whether the highlighted regions "make clinical sense". M1 averages 4.6 and M2 averages 3.1. The underlying classifier is accurate on a held-out set. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A classifier that relies on a spurious cue can have a faithful explanation that looks implausible to clinicians, because it points at the cue.
- [ ] B. The ratings measure how plausible the explanations look to people, which is different from whether they reflect what the classifier computes.
- [ ] C. Since the classifier is accurate, the method whose maps look more sensible must be the more faithful one; accurate models use sensible cues.
- [ ] D. Faithfulness can be probed by changing the input the way an explanation says matters and checking whether the model's output changes as predicted.
- [ ] E. Tuning an explanation generator to maximize clinician ratings can raise its plausibility while lowering its faithfulness.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: If the model uses a spurious cue, a faithful explanation will point at the cue, which clinicians will rate as nonsensical.
- B: Human ratings test whether an explanation fits expectations, not whether it tracks the model's computation.
- C: An accurate model can be right for reasons that clinicians would reject, and an unfaithful explanation can be written to look sensible.
- D: Intervening on the highlighted features and observing the output is a direct test of whether the explanation matches the model's behavior.
- E: An objective that rewards agreement with human expectations can be met by showing what people expect rather than what the model used.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## MA-ch05.17

A hospital trains a model on historical records to predict 30-day mortality for patients with a lung infection. In those records, patients with a history of asthma were sent straight to intensive care and had lower observed mortality than other patients. The model assigns lower predicted risk to patients with asthma, and a Shapley explanation gives the asthma input a value of -6 percentage points for those patients. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The Shapley value shows that having asthma protects patients from dying of the infection.
- [ ] B. Refitting the model with more data collected under the same admission policy would remove the problem.
- [ ] C. The Shapley value accurately reports that the model lowers its predicted risk because of the asthma input.
- [ ] D. The attribution supports a rule that sends patients with asthma to a general ward because the model rates them lower risk.
- [ ] E. The pattern could come from treatment decisions recorded in the data, so it need not reflect anything about asthma itself.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: An association learned from observational data does not show an effect of the condition on the outcome.
- B: More data from the same policy reproduces the same confounded association with greater confidence.
- C: Shapley values describe the model's own accounting, and that accounting does assign lower risk through this input.
- D: Removing the intensive care that produced the low mortality could reverse the pattern, and the model never saw patients treated that way.
- E: Care given because of the condition is a confounding path from the condition to the outcome.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.18

A lender approves an application when score >= 40, where score = income (in thousands of dollars) + 5 x years employed - 10 x missed payments. An applicant with income 38, 2 years employed and 2 missed payments has score 28 and is denied. A counterfactual explanation looks for a changed set of inputs that would flip the decision. Treat the applicant's record of missed payments as accurate and not open to change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. There is exactly one smallest counterfactual, so the explanation is unique and the applicant can be given a single answer.
- [ ] B. Raising income to 50 and changing nothing else flips the decision.
- [ ] C. Whether "raise income by 12" or "add 3 years" counts as closer depends on how a dollar change is weighted against a year, a modeling choice.
- [ ] D. Removing both missed payments would flip the decision, but given that the record is fixed, that is not a change the applicant can make.
- [ ] E. Adding exactly 2 years of employment and changing nothing else flips the decision; each year adds 5 points.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Several different minimal changes also work, for example income +12, years +3, or income +7 with years +1, so the closest one depends on the distance used.
- B: 50 + 10 - 20 = 40, which meets the threshold.
- C: Distance across features measured in dollars, years and counts requires a chosen weighting, and the choice determines which counterfactual is nearest.
- D: With no missed payments the score would be 48, but with an accurate, unchangeable record a past missed payment cannot be undone.
- E: 38 + 20 - 20 = 38, still below 40.

**Source:** Counterfactuals are closer to what you actually want

## MA-ch05.19

A lender gives each denied applicant a counterfactual: the smallest change to the applicant's inputs, measured by Euclidean distance on standardized features, that makes the model approve. For one applicant the returned counterfactual changes age from 24 to 31, years with the current employer from 1 to 6, and nothing else. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the lender retrains its model next quarter, the applicant is still assured of approval after making the stated changes.
- [ ] B. Adding five years of tenure is an action the applicant can take immediately; tenure is within their control.
- [ ] C. Because the counterfactual changes only two features, it describes a state the applicant could reach with nothing else changing.
- [ ] D. A smallest-change counterfactual that relies on a change of age cannot be acted on, but it is evidence that the decision is sensitive to age.
- [ ] E. The change that is smallest in standardized Euclidean distance is the cheapest route for the applicant to reach approval.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: A counterfactual describes the current model; a retrained model or moved threshold can make the same changes insufficient.
- B: Tenure grows only as time passes, so a five-year change is not available now.
- C: Tenure and age move together with income and other inputs in real life, so holding everything else fixed may describe a state that cannot be reached.
- D: Age cannot be changed by the applicant, yet a smallest-change counterfactual that moves age shows the model's output moves with age, which is relevant to fairness review.
- E: Euclidean distance on standardized features is a convenience, not a measure of the time, money or effort the applicant must spend.

**Source:** Counterfactuals are closer to what you actually want

## MA-ch05.20

LIME explains a prediction by fitting a simple model to the classifier's outputs on randomly perturbed copies of the input. It is run five times on the same input of a deterministic text classifier, each time with a different random seed. The top-3 features in runs 1 to 5 are {f1, f2, f3}, {f1, f2, f4}, {f1, f3, f5}, {f2, f3, f4} and {f1, f2, f3}. The Jaccard overlap of two sets is the size of their intersection divided by the size of their union. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Runs 2 and 3 have a Jaccard overlap of 0.2, because they share one feature out of five distinct ones.
- [ ] B. The variation across runs shows that the classifier returns different outputs for the same input.
- [ ] C. Choosing the run whose features look most sensible to the analyst is a sound way to settle the disagreement.
- [ ] D. Each of features f1, f2 and f3 appears in the top 3 of exactly four of the five runs, and no feature appears in all five.
- [ ] E. Drawing more perturbed samples in each run typically reduces the run-to-run variation of the explanation, because the surrogate is fitted to random samples.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: {f1, f2, f4} and {f1, f3, f5} share only f1, and their union is {f1, f2, f3, f4, f5}, so the overlap is 1/5 = 0.2.
- B: The classifier is deterministic; the variation comes from LIME's random sampling of perturbed points.
- C: Picking the run that matches expectations imports the analyst's prior and hides the instability; the agreement across runs is the finding to report.
- D: Feature f1 is in runs 1, 2, 3 and 5; f2 is in runs 1, 2, 4 and 5; f3 is in runs 1, 3, 4 and 5.
- E: The surrogate is an estimate fitted to random samples, and more samples reduce its sampling variance.

**Source:** LIME, in a different shape

## MA-ch05.21

LIME fits a weighted linear model to a classifier's outputs on synthetic points sampled around one input, giving more weight to points near that input. For one input, the linear model's weighted R-squared on the synthetic points is 0.31. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An R-squared of 0.31 means the surrogate reproduces little of the classifier's variation near this input, so its coefficients describe the model weakly there.
- [ ] B. Because LIME can be applied to any classifier, its coefficients are faithful to the classifier whatever the R-squared, so no fidelity check is needed.
- [ ] C. Independently perturbed synthetic points can be unlike real data, so the classifier's outputs on them may not reflect its behavior on real inputs.
- [ ] D. A high R-squared would show that the coefficients also apply to inputs far from this one; a linear fit holds everywhere once it fits well.
- [ ] E. A narrower neighborhood generally lets a linear model fit the classifier's local behavior better, at the price of a smaller region.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: R-squared is the share of the (weighted) variation in the classifier's outputs that the surrogate captures; 0.31 is low.
- B: Applicability to any model does not mean the local approximation is good; fidelity has to be measured for each explanation.
- C: Independent perturbation can create unrealistic combinations on which the classifier extrapolates unpredictably.
- D: A local fit says nothing about regions where a nonlinear model behaves differently.
- E: Smooth functions are closer to linear over small regions, though a smaller region also means fewer points carry weight and less is explained.

**Source:** LIME, in a different shape

## MA-ch05.22

A vendor wraps a lending model in a router. A detector, trained to tell real applications from the synthetic points that perturbation-based explainers such as LIME and KernelSHAP generate by perturbing features independently, flags 95% of synthetic points correctly. Inputs that look real go to model 1, which uses a sensitive attribute; inputs flagged as synthetic go to model 2, which ignores it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Two perturbation-based explainers that sample in a similar way and agree provide independent confirmation that the deployed system is harmless.
- [ ] B. The router works only if the vendor knows the explainer's random seed; the detector must anticipate the exact points the explainer generates.
- [ ] C. Comparing the outputs of several different perturbation-based explainers tests the deployed system on the inputs the router treats as real.
- [ ] D. This shows that explanation methods are uninformative for every purpose, because any explainer can be fooled in this way.
- [ ] E. Most of the explainer's queries are answered by model 2, so its explanation can show the sensitive attribute as unimportant.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Both explainers query off-distribution points that the router recognizes, so their agreement shares the same blind spot.
- B: The detector learns the statistical signature of perturbed points, not a particular seed.
- C: Perturbation-based explainers generate the synthetic points the router detects, so adding more of them does not exercise the path real applications take.
- D: A weakness of one query pattern does not make explanations useless; it shows they must be checked against the model's behavior on real inputs.
- E: The explainer sees the system's behavior on perturbed points, which the router sends to the innocuous model.

**Source:** LIME, in a different shape

## MA-ch05.23

A language model is evaluated on 1,000 multiple-choice questions. Researchers add the line "A colleague believes the answer is C" to each question. On 200 questions the model's answer changes to C only when the line is present. On 50 of those 200 the model's written step-by-step reasoning mentions the colleague's opinion; on the other 150 it does not, and presents what reads as an independent derivation of C. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A check of this kind needs an intervention on the inputs; the text of the reasoning alone cannot supply it, however detailed.
- [ ] B. In 75% of the answer-changing cases, the written reasoning leaves out a factor that the intervention shows changed the answer.
- [ ] C. The result shows that a model's written reasoning is uninformative for every purpose.
- [ ] D. Reading the written reasoning is a valid substitute for an intervention experiment, because a model reports what influenced it.
- [ ] E. A fluent, step-by-step justification that supports the final answer is, by itself, good evidence that those steps are what produced the answer.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Whether stated reasons track actual influences is a causal question, and answering it takes a controlled change to the input.
- B: 150 of the 200 switches, which is 75%, carry no mention of the hint.
- C: Reasoning can still help catch errors and give checkable steps; the finding concerns its reliability as a record of what influenced the answer.
- D: The experiment found influences that the text did not report, which is exactly what makes reading the text insufficient.
- E: Text can be generated to fit an answer after the fact, so fluency and coherence do not show the steps were causal.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## MA-ch05.24

Researchers train a linear probe on a language model's layer-12 activations to predict whether a sentence's subject is singular or plural. The probe reaches 97% accuracy on held-out sentences. A control probe trained to predict a label assigned at random to each word type reaches 55%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The result shows that the singular-or-plural information is linearly decodable from the layer-12 activations.
- [ ] B. Changing the activations along the probe's direction and checking whether verb agreement changes would show whether the information is used.
- [ ] C. A probe that is a large nonlinear network can reach high accuracy by learning the task itself, which is why control tasks are used.
- [ ] D. A control probe near chance suggests the probe is not reaching 97% merely by memorizing arbitrary labels.
- [ ] E. The result proves that the model uses that information when it produces its output; a probe at 97% could not succeed otherwise.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Held-out accuracy of 97% means the label can be read off the activations by a linear function.
- B: An intervention on the representation tests whether downstream behavior depends on it, which decodability cannot.
- C: A high-capacity probe can solve the task by itself from weak signals, so accuracy then says less about the activations.
- D: A probe able to memorize arbitrary labels would score well on the control task; 55% suggests it cannot do so.
- E: Information being present is different from the model using it; the model may ignore a variable that is nonetheless decodable.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## MA-ch05.25

A pneumonia classifier is trained on chest X-rays pooled from two hospitals. Hospital 1 contributes 5,000 images, 60% of which show pneumonia. Hospital 2 contributes 5,000 images, 10% of which show pneumonia. Each image carries a small scanner tag in a corner that identifies the hospital, and attribution maps from the trained classifier highlight the tag on most images. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Measuring accuracy within each hospital, and on images from a third hospital, helps check whether the classifier is relying on the tag.
- [ ] B. A rule that always predicts "no pneumonia" would score 90% accuracy on the pooled data, since most images are negative.
- [ ] C. A rule that predicts pneumonia exactly when the image comes from Hospital 1 would score 75% accuracy on the pooled data.
- [ ] D. The attribution on the tag proves that the classifier contains no information about the lungs and relies on nothing else.
- [ ] E. An overall accuracy of 85% would rule out reliance on the tag, because 85% exceeds the 75% that the tag alone can give.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Within one hospital the tag carries no information, so a collapse in accuracy within hospitals or at a new site indicates reliance on it.
- B: Pooled prevalence is (3,000 + 500) / 10,000 = 35%, so always predicting negative scores 65%.
- C: Correct on 60% of Hospital 1 (the positives) and 90% of Hospital 2 (the negatives): (3,000 + 4,500) / 10,000 = 0.75.
- D: Attribution to the tag shows the classifier uses it, not that it uses nothing else.
- E: A model can use the tag and real lung evidence together, so beating the tag-only score does not show the tag is unused.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## MA-ch05.26

An autonomous operations agent is told to "delete the customer's record". It runs a command that sets deleted = true on the row in the primary database, then reports: "The customer record has been deleted." The database keeps flagged rows for 30 days and nightly backups keep the row for 90 days. The customer wanted the data to be unrecoverable. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Asking the agent afterwards why it said "deleted" will reliably produce an account that states the retention periods.
- [ ] B. A fluent and confident report makes it unnecessary to check the state of the system; a model that writes well knows what it did.
- [ ] C. Querying the database and the backups and checking the retention settings is a verification that the agent's report cannot supply by itself.
- [ ] D. The report can be accurate about the system's own state flag and still mislead a reader who takes "deleted" to mean "no longer recoverable".
- [ ] E. A feature-attribution method applied to the agent's model would have flagged the mismatch between the agent's wording and the customer's meaning.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: A generated explanation reflects what the model produces when prompted, and can omit facts it never represented.
- B: Fluency is a property of the text, not evidence about the world.
- C: The claim is about the state of the world, so it is checked against that state, not against the agent's description of it.
- D: The word "deleted" has a narrow technical meaning inside the system and a stronger meaning to the customer; the report resolves the ambiguity silently.
- E: Attribution shows which inputs shaped the output; it does not compare the output's meaning with what the reader will understand.

**Source:** Back to Ash

## MA-ch05.27

A hospital buys a sepsis-risk model. The contract says "every prediction must be accompanied by an explainable reason". The vendor publishes the full weights of its 60-million-parameter neural network and supplies, for each patient, the five inputs with the largest Shapley values. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Whether an explanation is adequate depends on who reads it and what decision they must make with it, so one explanation can suit a developer and fail a patient.
- [ ] B. Because Shapley values add up exactly to the prediction minus the reference prediction, they establish that the risk would fall if the top input were changed.
- [ ] C. Replacing the network with a short scoring rule a clinician can follow step by step would give an explanation that approximates the model, just as the vendor's list does.
- [ ] D. Meeting the contract's wording means a bedside nurse can use the reason to decide what to do for the patient.
- [ ] E. Publishing all the weights gives access to the model's internals but does not by itself let a clinician predict what the model will do for a new patient.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The same attribution can be useful to a developer and useless to a patient; adequacy is relative to the reader and the purpose.
- B: Efficiency makes the values sum correctly; it says nothing about what would happen if an input were changed.
- C: For a short scoring rule the rule itself is the model, so reading it involves no approximation.
- D: A list of influential inputs says what moved a number, not what action is clinically appropriate.
- E: Inspecting millions of parameters does not produce a working mental model of behavior on new cases.

**Source:** Three words that don't mean the same thing

## MA-ch05.28

To explain a gradient-boosted credit model, an analyst fits a depth-4 decision tree to imitate it, training the tree on the black-box model's decisions and not on the true repayment outcomes. On 2,000 held-out applicants the tree agrees with the black box's decision for 88% of them. Among the 200 applicants under 25, the agreement is 61%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Agreement with the true repayment outcomes is the correct measure of how faithful the tree is to the black box's decisions.
- [ ] B. For the 200 applicants under 25, the tree's decision differs from the black box's for 122 of them, about 61% of that group.
- [ ] C. Because the tree was trained to match the black box, perfect agreement would still not show that the black box is right about applicants.
- [ ] D. Agreement among the applicants aged 25 or over is 85%, in line with the overall figure of 88% and well above the 61% for the youngest.
- [ ] E. An overall agreement of 88% means the tree is a reliable description of the black box for every subgroup, including the youngest.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Fidelity is agreement with the black box's outputs; agreement with outcomes measures accuracy, which is a different property.
- B: Agreement is 61%, so 122 of the 200 agree and 78 differ; 122 is the number of agreements.
- C: A surrogate trained on model outputs describes the model, and the model can be wrong about the world.
- D: The tree agrees on 1,760 of 2,000 overall and on 122 of the 200 young applicants, so 1,638 of 1,800 others, which is 91%.
- E: Overall agreement can hide a poor match for a subgroup, here 61% for applicants under 25.

**Source:** LIME, in a different shape

## MA-ch05.29

A lender removes race from the inputs of its approval model and keeps zip code, which is correlated with race in the applicant population. Shapley explanations for denials show a large value for zip code and no value for race, since race is not an input. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The absence of any attribution to race does not show that approval decisions are independent of race, because correlated inputs can carry the same information.
- [ ] B. Removing zip code and retraining guarantees that the new model has no dependence on race, since the proxy is gone.
- [ ] C. Comparing outcomes such as approval and error rates across groups is a direct way to look for disparities that attribution lists would not reveal.
- [ ] D. Because race is not an input, approval rates cannot differ between racial groups, whatever the other inputs are.
- [ ] E. A large Shapley value for zip code on its own establishes that the lender is discriminating on race.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A model can reproduce group differences through correlated inputs even when the group label itself is absent.
- B: Other correlated inputs can carry the same information, so removing one proxy does not guarantee independence.
- C: Outcome rates by group are measured directly on decisions, independent of how the model is explained.
- D: Group differences in outcomes can arise from proxies and from differences in the data, whether or not the label is an input.
- E: A large value shows the model uses zip code; whether that use amounts to discrimination is a further question about proxies, justification and effects.

**Source:** The correlated feature problem

## MA-ch05.30

A logistic regression for loan default uses two nearly duplicate inputs, balance_today and balance_yesterday, with correlation 0.99. On the full data the coefficients are +4.8 and -4.1. On two bootstrap resamples they are (+1.2, -0.5) and (-3.1, +3.8). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The model's predictions can stay similar across resamples even though the coefficients differ, because the data pin down the sum more tightly than each coefficient.
- [ ] B. Penalizing the coefficients (ridge) or combining the two inputs into one would make the interpretation more stable.
- [ ] C. The individual coefficients are unstable across resamples, while their sum (0.7 in each fit) is stable.
- [ ] D. The negative coefficient on balance_yesterday in the full fit shows that a higher balance yesterday lowers default risk.
- [ ] E. Reading a coefficient as the effect of changing one input "holding the others fixed" is unreliable when the other inputs cannot realistically be held fixed.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Predictions depend mainly on the sum for nearly identical inputs, which the data constrain well.
- B: A ridge penalty shares weight across the pair and merging them removes the redundancy, both of which stabilize what the coefficients say.
- C: 4.8 - 4.1 = 0.7, 1.2 - 0.5 = 0.7 and -3.1 + 3.8 = 0.7, while each coefficient moves widely and changes sign.
- D: With near-duplicates the sign of one coefficient is set by how it offsets the other, not by an independent effect.
- E: In nearly duplicate inputs one cannot change without the other, so the "holding fixed" comparison does not occur in the data.

**Source:** Three words that don't mean the same thing

## MA-ch05.31

A team plans several uses for feature attributions (such as Shapley values) computed from a trained model on its validation data. Check each statement that is true about what the attributions can support. Each statement is worth 1 point (5 points total).

- [ ] A. For regulatory review, a list of the top three inputs for each decision shows whether the model treats demographic groups differently.
- [ ] B. For trust, a user's increased confidence after reading an explanation is evidence that the model is more accurate than was thought.
- [ ] C. For debugging, heavy attribution to an input the team did not expect the model to use is a lead worth investigating for leakage or a shortcut.
- [ ] D. For safety sign-off, a clean-looking attribution pattern across 1,000 validation cases shows that the model will perform well on a population it has not seen.
- [ ] E. For recourse, the attribution values alone tell an applicant which actions would change the decision and how large the actions must be.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Per-decision lists do not compare outcomes across groups; disparities are found by measuring outcomes group by group.
- B: Users' confidence can rise with a fluent explanation whether or not the model is correct, so it is not evidence of accuracy.
- C: Surprising weight on an input is cheap evidence of a data problem and points to where to look.
- D: Attributions describe the model on the data used; they do not measure performance under distribution shift.
- E: Attributions say what contributed to a score, not which feasible changes would flip it; that takes a counterfactual with actionable constraints.

**Source:** What SHAP is, and what SHAP isn't

## MA-ch05.32

A trial randomizes 100 clinicians to each of two arms. Arm 1 sees an AI recommendation only. Arm 2 sees the recommendation plus a feature-attribution explanation. Each clinician handles one case on which the AI's recommendation is wrong. In arm 1, 46 of 100 clinicians follow the wrong recommendation; in arm 2, 58 of 100 do. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because a 95% interval for the difference includes 0, the data show that the explanation has no effect on whether clinicians follow wrong advice.
- [ ] B. A 95% interval for the difference runs from about -2 to +26 points, so these data do not establish that the explanation raises following of wrong advice.
- [ ] C. The observed difference is 12 percentage points, in the direction of more following of wrong advice when the explanation is shown.
- [ ] D. If the 12-point difference is real, it would show that the explanation is an inaccurate description of the model's behavior.
- [ ] E. With 400 clinicians per arm and the same proportions, the 95% interval would run from about +5 to +19 points.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: An interval that includes 0 is also consistent with sizeable effects; it shows the data are inconclusive, not that the effect is absent.
- B: The standard error is sqrt(0.46 x 0.54/100 + 0.58 x 0.42/100) = 0.070, giving 0.12 +/- 1.96 x 0.070, about -0.017 to +0.257.
- C: 58% - 46% = 12 points.
- D: Higher reliance on a wrong recommendation describes user behavior; an explanation can be accurate about the model and still persuade people to over-trust it.
- E: The standard error falls to 0.035, giving 0.12 +/- 0.069, about +0.051 to +0.189.

**Source:** Three words that don't mean the same thing
