# Chapter 2: Probability, uncertainty and the confidence illusion

## MA-ch02.1

A forecasting service publishes these probabilities for one day: P(rain) = 0.60, P(snow) = 0.50 and P(rain or snow) = 0.70. For an unrelated question it publishes P(outage) = 0.70 and P(no outage) = 0.40. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The rain and snow figures imply P(rain and snow) = 0.40.
- [ ] B. For any two events, P(A or B) = P(A) + P(B), so the rain and snow figures should have totaled 1.10 and the published 0.70 is a mistake.
- [ ] C. A counterparty who treats the outage figures as fair betting prices could place offsetting bets that win money against the service whichever outcome occurs.
- [ ] D. The outage figures are incoherent, because an event and its complement must have probabilities that sum to 1.
- [ ] E. P(rain and snow) cannot exceed 0.50 here, because "rain and snow" is contained within the snow event.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Inclusion-exclusion gives P(rain and snow) = 0.60 + 0.50 - 0.70 = 0.40.
- B: Simple addition holds only for mutually exclusive events; rain and snow can occur together, so the sum overcounts the overlap.
- C: Prices that sum to 1.10 for a set of outcomes that must resolve to exactly 1 allow a guaranteed profit by trading the opposite side of both bets (a Dutch book).
- D: P(outage) + P(no outage) = 1.10, which violates normalization and the complement rule P(not A) = 1 - P(A).
- E: If one event is contained in another its probability cannot be larger, so P(rain and snow) <= P(snow) = 0.50; the actual value of 0.40 satisfies this.

**Source:** The three axioms

## MA-ch02.2

A triage model attaches an abnormal-lab flag to some incoming cases. In a log of past cases, 70% carry the flag, 40% turn out to be high-acuity, and 25% are both flagged and high-acuity. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P(high-acuity | no flag) is 0.15.
- [ ] B. P(high-acuity | flag) is about 0.36.
- [ ] C. Learning that a case carries the flag raises its probability of being high-acuity above the overall 0.40.
- [ ] D. With these proportions, the flag and high acuity are independent events.
- [ ] E. P(flag | high-acuity) has the same value as P(high-acuity | flag).

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: 0.15 is P(high-acuity and no flag) = 0.40 - 0.25; dividing by P(no flag) = 0.30 gives a conditional probability of 0.50.
- B: P(high-acuity | flag) = 0.25 / 0.70, about 0.357.
- C: The conditional probability 0.357 is below 0.40, so the flag is mild evidence against high acuity because it is very common.
- D: Independence would require P(both) = 0.70 x 0.40 = 0.28, but the joint is 0.25.
- E: P(flag | high-acuity) = 0.25 / 0.40 = 0.625; reversing the conditioning changes the denominator and so the value.

**Source:** Conditional probability — the probability that updates on what you know

## MA-ch02.3

An agent must complete three tool calls in order, and the task succeeds only if all three succeed. Measured separately on fresh inputs, the three calls succeed with probabilities 0.95, 0.90 and 0.90. In real runs the first call succeeds with probability 0.95; given that the first succeeded, the second succeeds with probability 0.85; given that both earlier calls succeeded, the third succeeds with probability 0.80. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Relative to the correct joint probability, the independence-based figure of about 0.77 overstates the chance of success by roughly 12 percentage points.
- [ ] B. The chain rule can be applied using only the three unconditional success rates.
- [ ] C. The probability that all three calls succeed in real runs is 0.95 x 0.85 x 0.80 = 0.646.
- [ ] D. If the three calls were independent with the separately measured rates, the probability that all succeed would be 0.95 x 0.90 x 0.90, about 0.77.
- [ ] E. Multiplying the separately measured rates (about 0.77) gives the correct probability that all three calls succeed in these runs, because the calls run in sequence.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 0.7695 - 0.646 is about 0.12, so assuming independence here would overstate success by roughly twelve points.
- B: The chain rule multiplies each step's probability conditional on the earlier steps having happened, which are different numbers from the unconditional rates.
- C: The chain rule gives P(A1) x P(A2 | A1) x P(A3 | A1, A2) = 0.95 x 0.85 x 0.80 = 0.646.
- D: Under independence the joint probability is the product of the marginals: 0.95 x 0.90 x 0.90 = 0.7695.
- E: A product of unconditional rates is the joint probability only under independence; here the later calls are less reliable once the earlier ones have run.

**Source:** The multiplication rule — building joint probabilities from conditionals

## MA-ch02.4

A fraud-screening service routes each case to one of three model versions. V1 handles 50% of cases and is wrong on 1% of them, V2 handles 30% and is wrong on 4%, and V3 handles 20% and is wrong on 10%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The overall error rate of the service is 3.7%.
- [ ] B. V1 handles the most traffic, so it produces the largest share of the service's errors.
- [ ] C. Given that a case was handled incorrectly, the probability that V3 handled it is about 0.54.
- [ ] D. The overall error rate equals the simple average (1% + 4% + 10%) / 3 = 5%, whatever the traffic shares are.
- [ ] E. If traffic were rerouted to 20% V1, 30% V2 and 50% V3 with no model changed, the overall error rate would rise to about 6.4%.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The law of total probability gives 0.5 x 0.01 + 0.3 x 0.04 + 0.2 x 0.10 = 0.037.
- B: V1's share of errors is 0.005 / 0.037, about 13.5%, because its error rate is so low.
- C: Bayes' rule gives P(V3 | error) = 0.02 / 0.037, about 0.54.
- D: The correct overall rate weights each version's error rate by its traffic share; an unweighted average ignores how often each version runs.
- E: 0.2 x 0.01 + 0.3 x 0.04 + 0.5 x 0.10 = 0.064, so routing changes alone move the system-level error rate.

**Source:** The total probability theorem — decomposing complex problems

## MA-ch02.5

A screening test for a condition has sensitivity 90% and specificity 95%. The condition's prevalence in the screened population is 2%. Imagine 10,000 people are screened. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Doubling the prevalence to 4% would double the proportion of positive results that are true cases.
- [ ] B. About 490 people without the condition are expected to test positive.
- [ ] C. Because the test's overall accuracy is about 95%, a person with a positive result has about a 95% chance of having the condition.
- [ ] D. Roughly 27% of the people who test positive are expected to have the condition.
- [ ] E. Raising sensitivity to 100%, with specificity unchanged, would lift the proportion of positives that are true cases above 50%.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: At 4% prevalence there are 360 true positives and 480 false positives per 10,000, a proportion of about 43%, not double 27%, because the proportion depends nonlinearly on prevalence.
- B: 9,800 people without the condition times a 5% false-positive rate is 490.
- C: Overall accuracy mixes both classes and is dominated by the many healthy people; the chance that a positive is real is a different conditional probability.
- D: True positives are 180 and false positives 490, so 180 / 670 is about 0.27.
- E: With sensitivity 100%, true positives are 200 against 490 false positives, a proportion of about 29%.

**Source:** The test that is 99% accurate, and the patient it kills

## MA-ch02.6

A rare condition affects 1 in 10,000 people. A test is described as "99% accurate" in the sense that it returns positive for 99% of people who have the condition and negative for 99% of people who do not. One person drawn at random from the population tests positive. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the test is 99% accurate in both directions, the probability that this person has the condition is about 99%.
- [ ] B. Raising sensitivity to 100%, with specificity left at 99%, would bring that probability above 10%.
- [ ] C. In 1,000,000 people, about 9,999 true cases and 99 healthy people are expected to test positive.
- [ ] D. The probability that this person has the condition is about 1%.
- [ ] E. Raising specificity to 99.9% would bring that probability to about 50%.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: 99% describes how the test behaves given the true status; the probability of the condition given a positive result also depends on the 1-in-10,000 base rate.
- B: Sensitivity 100% leaves the roughly 10,000 false positives per million unchanged, so the probability stays near 1%.
- C: The counts are reversed: about 99 true cases and about 9,999 healthy people test positive per million.
- D: P(condition | positive) = 0.0001 x 0.99 / (0.0001 x 0.99 + 0.9999 x 0.01), about 0.0098.
- E: At 99.9% specificity the probability is only about 9%; it takes roughly 99.99% specificity to reach about 50%.

**Source:** The test that is 99% accurate, and the patient it kills

## MA-ch02.7

A DNA profile found at a crime scene matches a suspect. The probability that a randomly chosen unrelated person would match is 1 in 100,000. The true source is known to be one person in a region of 1,000,000 people, each equally likely beforehand, and the suspect was identified only because a search of a database covering all 1,000,000 people returned this match. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The probability that a matching person is innocent equals the random-match probability, 1 in 100,000, because both describe the same profile.
- [ ] B. The probability that the matching suspect is the true source is about 0.09.
- [ ] C. If independent evidence had already made the suspect 50% likely to be the source, the same match would raise that probability above 0.99.
- [ ] D. A probability of about 0.09 means the match carries little evidential value.
- [ ] E. About 10 unrelated people in the region are expected to match by chance.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The random-match probability is P(match | innocent); the probability asked about is P(innocent | match), and swapping them is a transposed-conditional error.
- B: One true source plus about 10 coincidental matches gives 1 / 11, about 0.09, which Bayes' rule confirms from the prior of 1 in 1,000,000.
- C: With prior odds of 1 to 1 and a likelihood ratio of 100,000, the posterior probability is about 0.99999.
- D: The match raised the probability from 0.000001 to 0.09, a factor of about 90,000, which is strong evidence even though it is not conclusive.
- E: 999,999 unrelated people times 1 in 100,000 is about 10.

**Source:** Bayes' theorem

## MA-ch02.8

A condition has prevalence 0.1%. A test has sensitivity 95% and specificity 95%. A person tests positive. The test is then run again, and the second result is also positive. Assume that, given the person's true status, the two results are independent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. After both positive results, the probability of the condition is about 27%.
- [ ] B. If the second run reused the same specimen with the same interference as the first, treating the two positives as independent would overstate the probability of the condition.
- [ ] C. The final probability would differ if the two positive results had arrived in the opposite order, because the first result sets the prior for the second.
- [ ] D. After the first positive result alone, the probability of the condition is about 1.9%.
- [ ] E. After both positive results, the probability of the condition is 0.95 x 0.95 = 0.9025, the product of the test's sensitivity and specificity.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Each positive multiplies the odds by 0.95 / 0.05 = 19, so prior odds of about 0.001 become about 0.36, a probability near 0.265.
- B: A repeat that shares the same error source is not independent given the true status, so it adds less evidence than the independence calculation credits.
- C: Odds updates multiply, and multiplication is commutative, so the order of two positives does not change the posterior.
- D: 0.001 x 0.95 / (0.001 x 0.95 + 0.999 x 0.05) is about 0.0187.
- E: 0.95 x 0.95 ignores the prior; the posterior depends on the base rate as well as on the test's sensitivity.

**Source:** Bayes' theorem

## MA-ch02.9

A detector has sensitivity 90% and specificity 90%, measured on a labeled evaluation set. It is first deployed where 20% of cases are truly positive, and later redeployed where 2% are. Assume the detector behaves identically on positive cases and on negative cases in both places. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The share of flagged cases that are truly positive is about 0.69 at 20% prevalence and about 0.16 at 2% prevalence.
- [ ] B. A posterior probability for the new setting can be obtained by combining the detector's likelihood ratio with the new prior odds.
- [ ] C. A probability score that was calibrated in the first setting stays calibrated in the second setting without any adjustment.
- [ ] D. Sensitivity and specificity remain 90% in both deployments.
- [ ] E. The drop in the share of flagged cases that are truly positive shows the detector became worse at recognizing positive cases.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: 0.18 / (0.18 + 0.08) is about 0.69 and 0.018 / (0.018 + 0.098) is about 0.16.
- B: Posterior odds equal prior odds times the likelihood ratio (here 9), so a new base rate gives a new posterior.
- C: Calibration depends on the base rate of the population; a score tied to a 20% prior is too high when the prior is 2%.
- D: With identical behavior on each class, these class-conditional rates do not depend on prevalence.
- E: Sensitivity and specificity are unchanged by assumption; the change comes from the lower prior, not from any change in the detector.

**Source:** The false-positive structure is everywhere

## MA-ch02.10

A model's response time is measured on 25 independent requests. The sample mean is 100 ms and the sample standard deviation is 15 ms. Assume response times are roughly normal. The t critical value for a two-sided 95% interval with 24 degrees of freedom is 2.064. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. About 95% of individual future requests should fall between 93.8 ms and 106.2 ms, since that is the 95% interval computed from the sample.
- [ ] B. A 95% confidence interval for the mean response time is about 93.8 ms to 106.2 ms.
- [ ] C. A Bayesian 95% credible interval for the mean, computed from a stated prior and model, can be read as a 95% probability statement about the mean given the data.
- [ ] D. A 95% prediction interval for a single new request is wider than the confidence interval for the mean, roughly 68.4 ms to 131.6 ms.
- [ ] E. With 2,500 requests and the same mean and standard deviation, the interval for the mean narrows to about plus or minus 0.6 ms while the prediction interval stays near plus or minus 29 ms.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The interval 93.8 to 106.2 describes uncertainty about the mean, not the spread of individual requests, which has a standard deviation of 15 ms.
- B: The standard error is 15 / 5 = 3 ms, and 100 plus or minus 2.064 x 3 gives about 93.8 to 106.2.
- C: A credible interval contains the parameter with the stated posterior probability, conditional on the model and the prior, which is the interpretation many people wrongly give to a confidence interval.
- D: The prediction half-width is 2.064 x 15 x sqrt(1 + 1/25), about 31.6 ms, which adds the variability of one new observation to the uncertainty about the mean.
- E: The mean's interval shrinks with the square root of n, but individual variability (about 1.96 x 15 = 29 ms) does not shrink with more data.

**Source:** When the Central Limit Theorem politely declines to help

## MA-ch02.11

An evaluation team computes a 95% confidence interval for a model's accuracy from each of 100 independent test sets, each drawn afresh from the same population. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 95% describes how often the procedure captures the true accuracy over repeated samples, not a probability attached to any one computed interval.
- [ ] B. If each of the 100 test sets were much larger, the intervals would be narrower and the share of them containing the true accuracy would rise above 95%.
- [ ] C. If a test set of 400 items is really 40 distinct items each reworded ten times, an interval computed as if the 400 items were independent will be too narrow.
- [ ] D. A very narrow interval shows that the test set is representative of the population where the model will be deployed.
- [ ] E. A 95% interval for the difference in accuracy between two models that excludes zero corresponds to rejecting "no difference" at the 5% level in a two-sided test.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Confidence refers to the long-run coverage of the method; once computed, a given interval either contains the fixed true value or does not.
- B: Larger samples make intervals narrower, but nominal coverage stays at 95%; it does not increase.
- C: Near-duplicates are strongly correlated, so the effective sample size is closer to 40 than 400 and the true uncertainty is larger than the formula suggests.
- D: Interval width reflects sampling noise only; a biased or unrepresentative sample can give a narrow interval around the wrong value.
- E: The duality between two-sided tests and intervals means a 95% interval excluding the null value rejects it at the 5% level.

**Source:** When the Central Limit Theorem politely declines to help

## MA-ch02.12

A team observes 19 correct answers in 20 independent test items. With a uniform Beta(1, 1) prior on the model's accuracy, the posterior is Beta(20, 2), with mean 0.909 and a central 95% interval of about 0.762 to 0.988. With a different prior, Beta(50, 5), concentrated near 0.91, the posterior is Beta(69, 6), with mean 0.92 and a central 95% interval of about 0.849 to 0.970. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A credible interval and a confidence interval are the same quantity and are always numerically equal.
- [ ] B. Given the model and the uniform prior, the probability that the accuracy lies between 0.762 and 0.988 is 95%.
- [ ] C. Under the uniform prior, the posterior probability that the accuracy exceeds 0.90 is above 95%.
- [ ] D. Since the posterior mean is 0.909, the model's accuracy is known to within about one percentage point.
- [ ] E. The two intervals differ partly because a credible interval depends on the prior as well as on the data.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The two answer different questions and can differ, especially with small samples or informative priors; they roughly agree only under certain diffuse-prior conditions.
- B: A central 95% credible interval holds 95% of the posterior probability, conditional on the assumed model and prior.
- C: Under Beta(20, 2), P(accuracy > 0.90) is about 0.64, so it is far from 95%.
- D: With only 20 items the interval spans over twenty percentage points, so the accuracy is far from pinned down.
- E: The informative prior narrows the interval and moves the posterior mean, showing that the stated prior contributes to the result.

**Source:** Bayes' theorem

## MA-ch02.13

Model P is evaluated on 20 test items and gets 19 right (95%). Model Q is evaluated on 1,000 items and gets 940 right (94%). Approximate 95% Wilson intervals for true accuracy are 0.764 to 0.991 for P and 0.924 to 0.953 for Q. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P's interval is wider because it rests on far fewer test items.
- [ ] B. The data are compatible with P's true accuracy being lower than Q's.
- [ ] C. Roughly four times as many test items would be needed to halve the width of Q's interval, if the observed accuracy stayed about the same.
- [ ] D. P's observed accuracy is higher than Q's, so P has been shown to be the more accurate model on the strength of a one-point gap.
- [ ] E. Doubling the number of test items for Q would halve the width of its interval, since the standard error is inversely proportional to n.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Interval width scales with 1 / sqrt(n), and P has 20 items against Q's 1,000.
- B: Q's whole interval lies inside P's, so P's true accuracy could easily be 0.90 or lower.
- C: Width shrinks with the square root of n, so halving the width requires about four times as many items.
- D: A one-point gap in observed accuracy on 20 items is well within sampling noise and does not establish a difference.
- E: Doubling n reduces the width by a factor of about sqrt(2), roughly 29%, not by half.

**Source:** When the Central Limit Theorem politely declines to help

## MA-ch02.14

A model forecasts the probability that each of five loans defaults: 0.8, 0.6, 0.3, 0.9, 0.2. The outcomes are 1, 0, 0, 1, 1, where 1 means the loan defaulted. The Brier score is the mean of the squared differences between forecast probability and outcome. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Classifying a loan as a default when its forecast is at least 0.5 gives an accuracy of 0.8 on these five loans.
- [ ] B. The single largest contribution to the total squared error comes from the 0.9 forecast.
- [ ] C. The Brier score of these forecasts is 0.228.
- [ ] D. A Brier score of 0.228 means the forecasts are off by 0.228 probability points on average.
- [ ] E. A forecaster who said 0.5 for every loan would score 0.25, so these forecasts score better than that constant.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Forecasts of 0.6 (outcome 0) and 0.2 (outcome 1) are on the wrong side of 0.5, so accuracy is 3 of 5 = 0.6.
- B: The squared errors are 0.04, 0.36, 0.09, 0.01 and 0.64; the 0.9 forecast contributes only 0.01, and the largest is the 0.2 forecast for a loan that defaulted.
- C: The sum of squared errors is 1.14, and 1.14 / 5 = 0.228.
- D: The Brier score is a mean of squares, not of absolute errors, so it is not an average miss in probability units.
- E: A constant 0.5 gives 0.25 for any outcomes, and 0.228 is lower, which is better.

**Source:** Calibration

## MA-ch02.15

Eight cases have true labels 1, 1, 1, 0, 0, 0, 1, 0. Model A gives probabilities of the positive class 0.60, 0.70, 0.55, 0.40, 0.30, 0.45, 0.35, 0.60. Model B gives 0.95, 0.90, 0.90, 0.10, 0.05, 0.10, 0.05, 0.95. Each model predicts the positive class when its probability is at least 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Model B's greater confidence on the cases it gets right gives it the better Brier score.
- [ ] B. Both models have the same accuracy, 0.75.
- [ ] C. Model B's Brier score (about 0.231) is worse than Model A's (about 0.211).
- [ ] D. Model B's log loss is higher than Model A's.
- [ ] E. Brier score separates these two models while accuracy at a 0.5 cutoff cannot.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Both models get cases 7 and 8 wrong, and B's confident errors (0.05 for a positive, 0.95 for a negative) cost far more than its gains on the correct cases.
- B: Each model errs on the seventh and eighth cases, so 6 of 8 are correct.
- C: A's squared errors average about 0.211 and B's about 0.231, because B's two confident errors cost 0.9025 each, more than its sharper correct forecasts save relative to A.
- D: Log loss punishes confident wrong answers even more heavily than Brier does, about 0.81 for B against 0.61 for A.
- E: Accuracy depends only on which side of 0.5 each forecast falls, so it cannot see the difference in confidence that the Brier score picks up.

**Source:** Calibration

## MA-ch02.16

On a test set in which 20% of cases are positive, a model's Brier score is 0.12. A reference forecaster always predicts the base rate, 0.20. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Relative to the reference forecaster, the model's Brier skill score, 1 - 0.12 / 0.16, is 0.25.
- [ ] B. Brier scores measured on test sets with different base rates can be compared directly, without a reference, as measures of model quality.
- [ ] C. A Brier score of 0.12 means that 12% of the model's forecasts were on the wrong side of 0.5.
- [ ] D. The reference forecaster has a Brier score of 0 because its forecasts are perfectly calibrated.
- [ ] E. The reference forecaster's Brier score is 0.16.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A skill score measures improvement over the reference: 1 - 0.12 / 0.16 = 0.25.
- B: The score of a trivial forecast is p(1 - p), which depends on the base rate, so a given score means different things at different base rates.
- C: The Brier score is a mean squared probability error, not an error rate at a cutoff.
- D: A constant forecast at the base rate is calibrated but has no discrimination, and its Brier score is p(1 - p), well above zero.
- E: With p = 0.20 the reference scores 0.20 x 0.80 = 0.16.

**Source:** Calibration

## MA-ch02.17

A classifier outputs the probability of the positive class for four cases: 0.9, 0.7, 0.2, 0.95. The true labels are 1, 0, 0, 0. Log loss is the mean of -ln(probability assigned to the true class), using natural logarithms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The largest single penalty comes from the 0.95 forecast on a negative case.
- [ ] B. Like the Brier score, log loss cannot exceed 1 for a binary problem.
- [ ] C. A predictor that always outputs 0.5 has log loss of about 0.69, so this classifier beats the constant predictor.
- [ ] D. The mean log loss of this classifier is about 1.13.
- [ ] E. If the classifier had output exactly 0 for a case that turned out positive, that case's log loss would be large but finite.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Per-case penalties are about 0.105, 1.204, 0.223 and 2.996, and the last is the 0.95 forecast on a negative case.
- B: Log loss is unbounded above because the penalty grows without limit as the probability given to the true class approaches 0.
- C: The classifier's 1.13 is worse than the 0.69 of the constant 0.5 predictor, so it does not beat it.
- D: (0.105 + 1.204 + 0.223 + 2.996) / 4 is about 1.132.
- E: -ln(0) is infinite, which is why implementations clip probabilities away from 0 and 1.

**Source:** Calibration

## MA-ch02.18

An analyst believes an event has true probability 0.7 and will report a probability p. Compare four scoring rules by expected score: Brier score, log loss, absolute error |p - y| (where y = 1 if the event occurs and 0 otherwise), and accuracy at a 0.5 cutoff (a report counts as correct if it is on the right side of 0.5). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Under Brier score, expected loss is minimized by reporting 0.7.
- [ ] B. Under absolute error, expected loss is minimized by reporting 0.7.
- [ ] C. Under log loss, expected loss is minimized by reporting 0.7.
- [ ] D. Under accuracy at a 0.5 cutoff, reporting 0.7 earns a higher expected score than reporting 0.99.
- [ ] E. A rule is strictly proper if its expected loss is minimized only by reporting one's true belief, and accuracy at a cutoff meets this definition.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The expected Brier score 0.7(1 - p)^2 + 0.3p^2 is minimized at p = 0.7.
- B: Expected absolute error is 0.7(1 - p) + 0.3p = 0.7 - 0.4p, which falls all the way to p = 1, so it rewards exaggeration.
- C: Expected log loss is minimized at the true probability, which is the defining property of a proper rule.
- D: Both reports fall on the same side of 0.5 and are correct with probability 0.7, so they earn the same expected score.
- E: Many different reports earn the same expected accuracy, so honesty is not uniquely rewarded and the rule is not strictly proper.

**Source:** Calibration

## MA-ch02.19

A classifier scores four positive cases at 0.9, 0.8, 0.6 and 0.55 and four negative cases at 0.7, 0.5, 0.4 and 0.3. Define AUC as the probability that a randomly chosen positive case scores higher than a randomly chosen negative case, with ties counting one half. Predict positive when the score is at least 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Replacing every score by its square leaves the AUC unchanged.
- [ ] B. The AUC is 0.875, since 14 of the 16 positive-negative pairs are ranked correctly.
- [ ] C. An AUC of 0.875 means the classifier is correct on 87.5% of cases at the 0.5 cutoff used for predictions.
- [ ] D. Accuracy at the 0.5 cutoff is 0.75.
- [ ] E. Adding many more negative cases with the same score distribution as the existing negatives would leave the expected AUC unchanged.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: AUC depends only on the ordering of scores, and squaring is strictly increasing on non-negative numbers.
- B: The only misordered pairs are the positive 0.6 against the negative 0.7 and the positive 0.55 against the negative 0.7, so 14 of 16 are correct.
- C: AUC is a ranking measure; accuracy at a cutoff is a separate quantity that depends on the threshold.
- D: At the 0.5 cutoff the negatives scored 0.7 and 0.5 are called positive, so 6 of 8 cases are correct.
- E: AUC compares the positive and negative score distributions and does not depend on the class proportions in the sample.

**Source:** Calibration

## MA-ch02.20

A disease has 10% prevalence. Model M1 outputs 0.10 for every patient. Model M2 outputs a score between 0.60 and 1.00 for every patient, and every patient with the disease scores above every patient without it. Model M3 outputs well-calibrated probabilities and has an AUC of 0.85. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. M2's high AUC means its scores can be read directly as probabilities of disease for individual patients.
- [ ] B. M1 is calibrated in aggregate but has an AUC of 0.5, so it cannot separate patients.
- [ ] C. M1 would be preferred over M3 for deciding which patients to examine first, because M1's probabilities match the prevalence exactly.
- [ ] D. M2 has an AUC of 1.0 yet its scores are badly calibrated for a 10% prevalence.
- [ ] E. Applying a strictly increasing rescaling to M2's scores, fitted on labeled data, could bring its probabilities much closer to the observed frequencies without changing its AUC.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: AUC measures ranking only; M2's scores of at least 0.6 for patients in a population with 10% disease are far too high as probabilities.
- B: Predicting the base rate for everyone matches the observed frequency overall but gives no way to rank patients.
- C: Prioritizing patients requires a ranking, which M1 cannot supply and M3 can.
- D: Perfect ranking is consistent with scores that bear no honest relation to the actual frequency of disease.
- E: A strictly increasing map preserves the order of scores, so AUC is unchanged while the stated probabilities can be brought much closer to the observed frequencies (exact calibration with perfectly separated classes would need values of 0 and 1, which a strictly increasing map cannot give, so the fit is approximate).

**Source:** Calibration

## MA-ch02.21

A reliability diagram for a binary classifier uses four bins of 400 cases each. For each bin it shows the pair (mean predicted probability, observed fraction of positives): (0.15, 0.22), (0.45, 0.47), (0.75, 0.62), (0.95, 0.80). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the observed rates rise with the predicted probability, the probabilities are shown to be calibrated.
- [ ] B. The 0.02 gap in the second bin is smaller than the standard error of an observed rate of about 0.47 from 400 cases, which is roughly 0.025.
- [ ] C. In the lowest bin the event occurs more often than predicted, so the model understates risk there.
- [ ] D. The diagram shows the model is miscalibrated by a similar amount in every bin, so one constant shift would repair it.
- [ ] E. In the two highest bins the predicted probabilities exceed the observed rates, a sign of overconfidence at high predicted risk.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A rising curve shows the model ranks cases sensibly, but calibration requires the points to lie near the diagonal, which they do not at the ends.
- B: The standard error is sqrt(0.47 x 0.53 / 400), about 0.025, so a gap of 0.02 is within ordinary sampling variation.
- C: An observed rate of 0.22 against a mean prediction of 0.15 means positives are more common than the model says there.
- D: The gaps are about 0.07, 0.02, 0.13 and 0.15, so the miscalibration is small in the middle and large at the ends.
- E: At 0.75 and 0.95 the observed rates are 0.62 and 0.80, below the predictions, which is the signature of overconfidence.

**Source:** Calibration

## MA-ch02.22

A classifier's top-label confidence on 1,000 test cases is grouped into four bins. For each bin the table gives the number of cases, the mean stated confidence and the observed accuracy: (500, 0.60, 0.58), (300, 0.80, 0.70), (150, 0.92, 0.80), (50, 0.99, 0.78). The expected calibration error (ECE) is the count-weighted mean of the absolute gap between mean confidence and accuracy across bins. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Mean stated confidence (about 0.73) exceeds overall accuracy (about 0.66), so the classifier is overconfident on average.
- [ ] B. The ECE is about 0.07.
- [ ] C. An ECE of about 0.07 means the classifier's predictions are wrong about 7% of the time on these cases.
- [ ] D. The bin with the largest gap, 0.21, makes the largest contribution to the ECE, since the ECE is dominated by its worst bin.
- [ ] E. Averaging the four bin gaps without weighting gives the same value as the count-weighted ECE.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The weighted mean confidence is 0.7275 and accuracy is 0.659, so on average confidence is about 7 points too high.
- B: The weighted gaps are 0.010, 0.030, 0.018 and 0.0105, which sum to 0.0685.
- C: ECE measures the gap between confidence and accuracy, not the error rate; the error rate here is about 34%.
- D: The 50-case bin contributes only 0.0105 because it has few cases; the 300-case bin contributes the most at 0.030.
- E: The unweighted mean of the gaps (0.02, 0.10, 0.12, 0.21) is about 0.11, while the count-weighted ECE is about 0.0685.

**Source:** Calibration

## MA-ch02.23

A model's 200 test predictions in the range 0.5 to 1.0 consist of 100 cases predicted at 0.60, of which 80 are positive, and 100 cases predicted at 0.90, of which 70 are positive. The expected calibration error (ECE) is the count-weighted mean absolute gap between mean predicted probability and observed frequency within bins. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. ECE values computed with different numbers of bins are directly comparable as measures of the same quantity.
- [ ] B. Splitting bins into finer sub-bins can only lower the measured ECE, because each sub-bin is more homogeneous.
- [ ] C. The single-bin ECE of 0 shows the model is well calibrated across this range of predictions.
- [ ] D. If the 0.60 cases and the 0.90 cases are placed in separate bins, the ECE is 0.20.
- [ ] E. If all 200 cases fall in one bin covering 0.5 to 1.0, that bin has mean prediction 0.75 and observed frequency 0.75, giving an ECE of 0.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The ECE changes with the number and placement of bins, so values from different binning schemes measure different things.
- B: Refining the bins can only keep ECE the same or raise it, because averaging within a bin lets opposite-signed gaps cancel.
- C: The single-bin value arises from cancellation: the model is underconfident at 0.60 and overconfident at 0.90 by equal amounts.
- D: The gaps are |0.6 - 0.8| = 0.2 and |0.9 - 0.7| = 0.2, and the equal weights give an ECE of 0.20.
- E: The pooled mean prediction is (0.6 + 0.9) / 2 = 0.75 and the pooled frequency is 150 / 200 = 0.75, so the gap is zero.

**Source:** Calibration

## MA-ch02.24

A forecaster is perfectly calibrated by construction: a case predicted at p has an event probability of exactly p, and predictions are spread roughly evenly across 0 to 1. Its expected calibration error (ECE) is estimated on a finite test set using 10 equal-width bins. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The expected measured ECE is greater than zero at any finite test set size.
- [ ] B. With 100 test cases, a measured ECE of about 0.08 would be unsurprising for this forecaster.
- [ ] C. Reporting an ECE without the test set size and the binning scheme is enough for others to compare it with another model's ECE.
- [ ] D. The expected measured ECE decreases as the test set grows.
- [ ] E. Using 20 bins instead of 10 on the same 100 test cases would, on average, lower the measured ECE.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Observed frequencies fluctuate around their expectations, and absolute gaps do not average to zero, so the estimate is biased upward even for a perfectly calibrated model.
- B: Random scatter in small bins gives a typical ECE near 0.10 at this size, so 0.08 does not indicate miscalibration.
- C: The ECE depends strongly on how many bins are used and how many cases there are, so both must be reported.
- D: Sampling noise in each bin falls roughly with the square root of the bin size, so measured ECE shrinks toward the true value as n grows.
- E: More bins mean fewer cases per bin and more noise in each observed frequency, which raises the average measured gap.

**Source:** Calibration

## MA-ch02.25

A classifier reports top-class confidence of 0.90 for every one of 1,000 held-out cases. Group X contributes 500 cases, 80% of which are classified correctly. Group Y contributes the other 500, all of which are classified correctly. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The pooled reliability diagram has a single point, at confidence 0.90 and accuracy 0.90, which lies on the diagonal.
- [ ] B. Confidence is too high for group X and too low for group Y.
- [ ] C. Because the pooled data are calibrated, each group is calibrated, since the group errors average out.
- [ ] D. A single global rescaling of confidence fitted on the pooled data would find nothing to correct and leave both group-level gaps in place.
- [ ] E. Pooled calibration guarantees that a decision rule based on confidence is equally reliable for both groups.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Every case has confidence 0.90 and the pooled accuracy is (400 + 500) / 1,000 = 0.90.
- B: Group X has accuracy 0.80 against stated confidence 0.90, and group Y has accuracy 1.00 against 0.90.
- C: Opposite-signed errors in the two groups cancel in the pooled data, so aggregate calibration does not imply group-level calibration.
- D: The pooled data already match the stated confidence, so a one-parameter fit would leave it unchanged and the group gaps would remain.
- E: A confidence of 0.90 means an 80% hit rate for one group and 100% for the other, so decisions based on it are not equally reliable.

**Source:** Calibration

## MA-ch02.26

A forecaster states a 90% interval for each of 20 independent questions and later counts how many intervals contain the true value. Assume that, if the forecaster is well calibrated, each interval has a 90% chance of containing the truth, independently of the others. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the intervals are well calibrated, the expected number that contain the true value is 18.
- [ ] B. Hitting 17 of 20 would be strong evidence that the intervals are miscalibrated, since 17 is below the expected 18.
- [ ] C. A result of 14 of 20 shows that the intervals are too wide to be informative.
- [ ] D. A result of 14 or fewer of 20 would be rare for a well-calibrated forecaster, with a probability of about 1%.
- [ ] E. A well-calibrated forecaster must hit exactly 18 of 20, since the long-run hit rate is 90%.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The expected count is 20 x 0.90 = 18.
- B: For a calibrated forecaster, P(17 or fewer) is about 0.32, so 17 hits is entirely ordinary.
- C: Intervals that miss the truth too often are too narrow, which means the forecaster was overconfident.
- D: Under a binomial model with n = 20 and p = 0.9, P(X <= 14) is about 0.011.
- E: Even a perfectly calibrated forecaster would hit exactly 18 only about 29% of the time, because the count is random.

**Source:** The calibration baseline

## MA-ch02.27

A binary classifier outputs the probability sigma(z) from a logit z, where sigma is the logistic function. Temperature scaling replaces it with sigma(z / T), where T > 0 is a single number fitted on held-out data. For one case with z = 3, sigma(3) is about 0.953. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A value of T fitted on validation data from last year restores calibration after the population the model sees changes.
- [ ] B. With T = 2, that case's probability becomes about 0.82.
- [ ] C. Dividing by a positive T changes which cases receive a probability above 0.5.
- [ ] D. Temperature scaling can repair a classifier whose ranking of cases is poor.
- [ ] E. Because dividing the logit by T preserves the ordering of cases, the classifier's AUC is unchanged by any T > 0.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A single parameter fitted to one distribution does not track later changes in the population, and calibration can go stale silently.
- B: sigma(3 / 2) = sigma(1.5), which is about 0.818.
- C: Dividing a logit by a positive number never changes its sign, so cases above 0.5 stay above 0.5 and predicted classes are unchanged.
- D: Temperature scaling changes only the stated confidence, not the ordering of cases, so it cannot improve ranking.
- E: sigma(z / T) is a strictly increasing function of z, and AUC depends only on the ordering of scores.

**Source:** Calibration

## MA-ch02.28

A clinic can follow up a flagged patient at a cost of $20. A positive case that is missed costs $400. A model gives each patient a probability of being positive. For statements A, B, D and E, assume the probabilities are calibrated (statement C considers miscalibrated probabilities). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 0.5 cutoff minimizes expected cost, as it minimizes the number of classification errors.
- [ ] B. Following up whenever the probability exceeds about 0.048 minimizes expected cost.
- [ ] C. If the model's probabilities are miscalibrated, the cutoff of about 0.048 still minimizes expected cost, because the cutoff depends only on the cost ratio.
- [ ] D. A patient with a calibrated probability of 0.10 should be followed up even though most such patients are negative.
- [ ] E. If the cost of a missed case fell to $100, the cost-minimizing cutoff would rise.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Minimizing error count weights both mistakes equally, but here a miss costs twenty times as much as a follow-up.
- B: Following up costs $20 and not following up costs 400p in expectation, so follow up when 400p > 20, that is p > 20 / 420, about 0.048.
- C: The cutoff is valid only if the stated probabilities equal the true frequencies; otherwise the wrong patients cross the cutoff.
- D: At p = 0.10 the expected cost of not following up is $40, which exceeds the $20 follow-up cost.
- E: The cutoff is the follow-up cost divided by the total of both costs, 20 / 120 = 0.167, which is higher than 0.048.

**Source:** Synthesis — four questions that prevent most deployment disasters

## MA-ch02.29

A language model answers 800 factual questions and appends a stated confidence to each answer. On the 400 answers where it wrote 95%, 288 were correct. On the 400 answers where it wrote 70%, 232 were correct. Correctness was judged against verified references. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 95% group is more accurate than the 70% group, so the stated numbers still carry some information about which answers are more likely to be right.
- [ ] B. Verbalized confidences cannot be corrected using held-out labeled data, so they must be discarded rather than recalibrated.
- [ ] C. Among answers stated at 95%, the observed accuracy is 72%, so the stated confidence overstates reliability by about 23 points.
- [ ] D. A precise stated figure such as 95% shows that the model computed a 95% probability internally before writing it.
- [ ] E. Because the model writes the number in fluent text, the stated confidences can be treated as calibrated probabilities.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Accuracy of 72% against 58% on 400 answers each is a difference far larger than sampling noise, so the ordering of the stated values is informative even though their levels are wrong.
- B: Stated confidences can be treated as a score and mapped to observed accuracy using labeled held-out data, then validated on fresh data.
- C: 288 / 400 = 0.72 against a stated 0.95, a gap of 23 points.
- D: A generated number is text produced by the model and does not by itself show that a probability of that size was computed or that it matches any frequency.
- E: Fluency is not evidence of calibration; the observed accuracies of 72% and 58% are well below the stated 95% and 70%.

**Source:** Calibration

## MA-ch02.30

A team wants to check whether the confidence scores emitted by a deployed classifier can be read as probabilities. Check each statement that is true about a sound way to check. Each statement is worth 1 point (5 points total).

- [ ] A. Collect labeled outcomes from data that resemble the population the classifier will serve, not only from the training distribution.
- [ ] B. Report the number of cases in each confidence bin alongside the observed rate, since sparse bins give noisy estimates.
- [ ] C. Repeat the check separately for subgroups and for different time periods, because an aggregate can hide offsetting errors and calibration can drift.
- [ ] D. After fitting a recalibration map, judge the recalibrated model on the same labeled data used to fit it, which gives an honest estimate of calibration.
- [ ] E. Use a proper score such as the Brier score or log loss as a complement to binned plots, since it does not depend on the choice of bins.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Calibration is a property of a model on a population, so it must be measured on data that resemble where the scores will be used.
- B: Counts reveal which bins can support a conclusion; a bin with a handful of cases can show a large gap by chance.
- C: Pooled data can look calibrated while subgroups are not, and a model calibrated at one time can degrade as inputs or base rates change.
- D: Evaluating on the fitting data overstates quality because the map was tuned to it; a separate held-out set is needed.
- E: Brier score and log loss use every prediction without binning, so they avoid the arbitrariness of bin choice.

**Source:** Calibration

## MA-ch02.31

A loan dashboard shows each decision with a model score such as "87.3% likely to repay." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reporting 87.3% rather than 87% shows that the estimate is accurate to a tenth of a point or better.
- [ ] B. A high AUC ensures that a score of 87.3% corresponds to an 87.3% repayment rate among loans given that score.
- [ ] C. A score calibrated on last year's loans will still be calibrated after the share of loans that repay changes substantially.
- [ ] D. Because the model outputs a number labeled as a probability, 87.3% of loans given this score will repay.
- [ ] E. What gives "87%" its meaning is the observed repayment rate among past loans with similar scores, measured on data resembling the deployment population.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The number of digits displayed is a formatting choice; the real uncertainty, from sampling and from model error, is far larger than the last digit.
- B: AUC measures ranking, and a model can rank well while its stated levels are systematically too high or too low.
- C: A change in the base rate or in the inputs moves the relationship between score and outcome, so old calibration can fail.
- D: A label on an output does not make it a calibrated probability; the match between score and frequency must be shown with outcome data.
- E: Calibration is established by comparing stated scores with realized frequencies on comparable data.

**Source:** From Boolean to probabilistic — and why the move is harder than it looks

## MA-ch02.32

A classifier was validated and found calibrated on data from 2024. In 2026 the user population has changed in ways nobody documented. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The classifier's confidence scores can look unchanged while real-world accuracy falls.
- [ ] B. A calibration curve measured on 2024 data guarantees calibration on 2026 data, provided the model weights are unchanged.
- [ ] C. Comparing stated probabilities with realized outcomes, once labels arrive, is the most direct way to detect that calibration has decayed.
- [ ] D. Monitoring only inputs can detect some harmful shifts without labels but cannot reveal a change in the input-outcome relationship when the inputs look the same.
- [ ] E. If overall accuracy is unchanged, calibration must also be unchanged, since both measure agreement with outcomes.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A model computes confidence from its inputs under the assumptions it learned, so scores can stay high and fluent while the world has moved.
- B: A calibration curve describes the population it was measured on; nothing guarantees the same relationship in a different population.
- C: Outcomes are the quantity the probabilities claim to predict, so comparing the two measures calibration directly.
- D: Input monitoring needs no labels but sees only what the inputs look like, so a shift in the outcome relationship at fixed inputs passes undetected.
- E: Accuracy can stay constant while stated confidence rises or falls relative to it, so a shift in calibration does not require a shift in accuracy.

**Source:** Hume's induction problem, re-translated as distribution shift

## MA-ch02.33

A deployed model's mistakes have this cost distribution: 99.9% of mistakes cost $1 and 0.1% cost $5,000, independently of each other. An audit samples 500 mistakes at random. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The expected cost per mistake is about $6.
- [ ] B. The median cost per mistake, $1, is an adequate summary of the risk this model poses to the organization.
- [ ] C. There is about a 61% chance that the 500 sampled mistakes contain no $5,000 mistake.
- [ ] D. In audits with no $5,000 mistake, the sample average is $1 and a standard-error interval computed from the sample has zero width and excludes the true mean.
- [ ] E. Reporting the frequency and size of the largest losses is needed in addition to the mean.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: 0.999 x $1 + 0.001 x $5,000 = $5.999.
- B: The median ignores the rare $5,000 losses that make up most of the expected cost.
- C: 0.999 raised to the 500th power is about 0.606.
- D: When every sampled cost is $1 the sample standard deviation is zero, so a normal-approximation interval collapses to $1 and misses the true mean of about $6.
- E: With a rare, severe tail, a mean or median alone hides the exposure; tail frequency and size must be reported.

**Source:** When the Central Limit Theorem politely declines to help

## MA-ch02.34

Independent draws X1, ..., Xn come from a standard Cauchy distribution, whose tails are so heavy that its mean is undefined and its variance is infinite. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For any independent and identically distributed data, quadrupling the sample size halves the standard error of the mean.
- [ ] B. Averaging more draws concentrates the sample mean ever more tightly around 0, the center of symmetry, as it does for normal data.
- [ ] C. The average of n such draws has the same distribution as a single draw, for every n.
- [ ] D. The usual central limit theorem for the sample mean requires, among other conditions, finite variance.
- [ ] E. If observations are strongly positively correlated, sigma / sqrt(n) understates the sampling variability of the mean even when the variance is finite.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The standard error formula sigma / sqrt(n) requires a finite variance; for heavy-tailed data with infinite variance it does not apply.
- B: The sample mean of Cauchy draws does not settle down as n grows; a single extreme draw can move it a long way.
- C: The Cauchy distribution is stable under averaging, so the mean of n independent standard Cauchy draws is again standard Cauchy.
- D: The classical theorem assumes independent observations with finite variance; with infinite variance the normalized mean does not approach a normal distribution.
- E: Positive correlation makes the observations carry less independent information than n independent ones, so the true variance of the mean is larger than sigma squared over n.

**Source:** When the Central Limit Theorem politely declines to help
