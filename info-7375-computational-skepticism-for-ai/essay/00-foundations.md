# Foundations (probability and statistics for skeptics)

Questions on the probability and statistics that checking a claim about an AI system depends on: conditional probability and base rates, distributions, sampling and inference, data quality and missing data, and the basics of fitting and evaluating a model. Each section keeps its own heading below.

# 1. Probability, conditional probability and Bayes' theorem

## ES-1.1

A school adopts a detector that labels essays as "AI-written" or "human-written". The vendor says it is "98% accurate", meaning that it flags 98% of AI-written essays and wrongly flags 2% of human-written essays. A teacher receives a flag on one essay. (a) Compute the probability that a flagged essay really is AI-written when 5% of essays are AI-written, and again when 0.5% are, showing your counts for 10,000 essays. (b) Explain why the vendor's figure does not answer the teacher's question. (c) State what else the teacher should know before acting on a flag.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes P(flagged | AI-written) = 0.98 from P(AI-written | flagged); these are different conditional probabilities and the vendor's figure is the first, not the second.
2. At 5% AI-written essays: 500 AI essays give 490 true flags and 9,500 human essays give 190 false flags, so 490 of 680 flags (about 72%) are correct.
3. At 0.5% AI-written essays: 50 AI essays give 49 true flags and 9,950 human essays give 199 false flags, so only 49 of 248 flags (about 20%) are correct.
4. Explains that the base rate (how common AI-written essays are) drives how trustworthy a flag is, so the same detector has very different reliability in different settings.
5. Names what is needed before acting: the base rate in that population, whether the false-flag rate differs across groups of writers, and corroborating evidence, treating a flag as a reason to look closer rather than as proof.

**Source:** Conditional probability, independence, Bayes

## ES-1.2

A forensic team searches a database of 2,000,000 people for matches to a face image from a crime scene. The system declares a match for a person who is not the source with probability 1 in 10,000, and it always matches the true source. Assume the true source is in the database. A prosecutor says: "The chance this match is a coincidence is 1 in 10,000, so there is a 99.99% chance this person is the source." Evaluate the statement with numbers, name the error, and say what additional evidence changes the conclusion.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the error as transposing a conditional: 1 in 10,000 is P(match | not the source), not P(not the source | match).
2. Computes the expected number of coincidental matches: about 2,000,000 × 1/10,000 = 200 other people matched, in addition to the true source.
3. Concludes that, with nothing else singling the person out, the chance a given matched person is the source is about 1 in 201, roughly 0.5%, not 99.99%.
4. Explains that searching a large database multiplies the opportunities for a coincidence, so the size of the search matters, and a narrower search changes the result (about 1 in 21 for a 200,000-person search).
5. Says independent evidence about the person (location, other identification, additional features) raises the prior odds, and that the correct combination is prior odds multiplied by the likelihood ratio.

**Source:** Conditional probability, independence, Bayes

## ES-1.3

Two models are evaluated on a mix of easy and hard questions. Correct answers out of questions asked: Model A scored 95 of 100 on easy questions and 300 of 900 on hard questions. Model B scored 900 of 1,000 on easy questions and 20 of 100 on hard questions. A report says "Model B is far more accurate: 83.6% against 39.5%". (a) Compute each model's accuracy on easy questions, on hard questions and overall. (b) Explain what is happening and whether the report's conclusion follows. (c) Say what comparison would be fair and what determines which breakdown to trust.

**Points:** 5

**Rubric (1 point each):**

1. Computes correctly: Model A is 95% on easy, 33.3% on hard and 39.5% overall; Model B is 90% on easy, 20% on hard and 83.6% overall.
2. Observes that Model A is better on both easy and hard questions yet worse overall, a reversal known as Simpson's paradox.
3. Explains the mechanism: overall accuracy is a weighted average of group accuracies with weights set by each model's mix of questions (A mostly hard, B mostly easy).
4. Concludes the headline figure confounds model quality with question difficulty; a fair comparison runs both models on the same questions or standardizes both to a common mix.
5. Notes that the right breakdown depends on the causal story, here that difficulty is a property of the question that affects the outcome and was unevenly assigned, so the stratified comparison is the one to trust.

**Source:** Conditional probability, independence, Bayes

# 2. Random variables and distributions

## ES-2.1

A reliability team monitors the daily count of model failures and sets an alert at "mean plus 3 standard deviations". Their dashboard says the alert fires by chance on only about 0.13% of days (about 1 day in 740), based on the normal curve. A reviewer objects that this assumes a normal distribution. (a) Show where the 0.13% comes from. (b) Give a distribution-free statement, with its number, about how much probability can lie more than 3 standard deviations from the mean. (c) Explain why fat tails make the normal figure unreliable and what the team should do instead.

**Points:** 5

**Rubric (1 point each):**

1. Shows the 0.13% as the normal upper-tail probability P(Z > 3) ≈ 0.00135, about 1 day in 740.
2. Gives Chebyshev's inequality: for any distribution with finite variance, at most 1/k² = 1/9 (about 11%) of the probability lies more than 3 standard deviations away in either direction, a loose worst-case guarantee compared with the normal's 0.27%.
3. Explains that the true figure depends on the tail shape, for example a Student t with 3 degrees of freedom rescaled to unit standard deviation puts about 1.4% beyond 3 standard deviations, around five times the normal value.
4. Explains that standard-deviation thresholds are calibrated only if the tail shape is right, so fat tails (and clustered failures) produce more alerts and larger extremes than the normal curve predicts.
5. Proposes using the data's own tail: examine histograms or quantile-quantile plots of the tail, set thresholds from empirical quantiles or extreme-value methods, use robust statistics, and track the real false-alarm rate.

**Source:** Probability distributions

## ES-2.2

An autonomous agent completes a task by making 500 tool calls. Each call fails with probability 0.002 (a 99.8% per-call success rate), independently of the others, and a single failed call ruins the run. A manager calls 99.8% reliability "basically perfect". (a) Compute the expected number of failed calls per run and the probability that a run has no failure, and name the distribution and a convenient approximation. (b) What per-call failure probability would be needed for 95% of runs to succeed? (c) Explain how the independence assumption affects these numbers.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the number of failures as Binomial(500, 0.002) with mean 1 and variance about 1.
2. Computes P(no failure) = 0.998^500 ≈ 0.37, so about 63% of runs fail at least once, and notes that a Poisson distribution with mean 1 gives nearly the same value (e^−1 ≈ 0.368).
3. Concludes that high per-call reliability does not imply high per-run reliability, because small failure probabilities compound over many steps.
4. For 95% run success, solves (1 − p)^500 ≥ 0.95 to get p of about 0.0001 (roughly 1 in 10,000), about 20 times better than 0.002.
5. Explains that independence is an assumption: with the same per-call rate, positively correlated failures (a shared cause such as a down service) make runs with at least one failure less frequent but failures clustered, so the independent calculation can be wrong in either direction for run-level reliability.

**Source:** Probability distributions

# 3. Sampling, the central limit theorem and inference

## ES-3.1

A team tests whether a new retrieval step improves a 0 to 100 answer-quality rating, with 20 rated tasks per arm and a standard deviation of about 9.8 points in each arm. The mean rating improves by 4.0 points; the standard error of the difference is 3.1 points, the two-sided p-value is 0.20, and the 95% confidence interval for the improvement is about −2.1 to +10.1 points. The team concludes "the retrieval step has no effect". (a) Explain what a p-value of 0.20 does and does not mean. (b) Critique the conclusion using the interval and the idea of statistical power. (c) State what the team should do to learn whether the step helps.

**Points:** 5

**Rubric (1 point each):**

1. States that p = 0.20 means a gap at least this large would arise about 20% of the time by chance if there were no true effect; it is not the probability that the null hypothesis is true and not a measure of effect size.
2. Explains that failing to reject the null is not evidence of no effect (absence of evidence is not evidence of absence), because the test may simply lack the ability to detect a real effect (a Type II error).
3. Uses the interval: −2.1 to +10.1 includes zero but also includes sizable benefits and small harms, so the data are compatible with a large effect and the study is inconclusive.
4. Uses power: with 20 per arm and a standard deviation near 10 points, a true 4-point benefit would be detected only about a quarter of the time, so a non-significant result is expected even if the effect is real.
5. Recommends pre-specifying the smallest effect that matters and collecting more data (about 95 per arm for roughly 80% power to detect 4 points at this variability), or using an equivalence test if the claim is "no meaningful effect".

**Source:** Statistical inference, estimation and hypothesis testing

## ES-3.2

A team evaluates 40 prompt variants against a baseline on the same benchmark, each with a two-sided test at significance level 0.05, and treats the 40 tests as independent. The best variant has p = 0.03 and the team announces "a statistically significant improvement". (a) If none of the variants truly differs from the baseline, how many significant results would you expect, and what is the probability of at least one? (b) Explain why the announced p-value is misleading and what per-test threshold a Bonferroni correction would use. (c) Describe two ways to handle the problem.

**Points:** 5

**Rubric (1 point each):**

1. Computes the expected number of false positives, 40 × 0.05 = 2, and the probability of at least one, 1 − 0.95^40 ≈ 0.87.
2. Explains that the announced p-value was picked as the smallest of 40, so "a 3% chance of arising by luck" no longer applies; the chance that the smallest of 40 null p-values is 0.03 or lower is 1 − 0.97^40 ≈ 0.70.
3. Gives the Bonferroni threshold 0.05 / 40 = 0.00125 per test, which p = 0.03 does not meet (the adjusted p-value is 40 × 0.03, capped at 1).
4. Names a correction: Holm, or Benjamini–Hochberg to control the false discovery rate, or pre-registering a single primary comparison before looking.
5. Recommends confirming the winning variant on fresh held-out data with one pre-specified test, and reporting how many variants were tried together with effect sizes and intervals.

**Source:** Statistical inference, estimation and hypothesis testing

## ES-3.3

A team runs 300 independent test prompts against a safety filter and all 300 pass. The report states "the failure rate is 0%". (a) Explain what the data do and do not show about the true failure rate. (b) Using the "rule of three" or an exact calculation, give the 95% upper bound on the failure rate. (c) How many failure-free tests would be needed to claim a failure rate below 0.1% with 95% confidence? (d) State an assumption behind these calculations.

**Points:** 5

**Rubric (1 point each):**

1. Explains that zero failures in a sample does not show a true rate of zero, because a rare failure is easily missed (a true failure rate of 1% would produce no failures in 300 tests about 5% of the time, 0.99^300 ≈ 0.049).
2. Gives the rule of three: with n tests and no failures, the 95% upper confidence bound on the failure rate is about 3/n, so about 1% for n = 300 (exact value 1 − 0.05^(1/300) ≈ 0.99%).
3. Computes that an upper bound of 0.1% needs about 3 / 0.001 = 3,000 failure-free tests (the exact calculation gives about 2,995).
4. States an assumption: the tests are independent, representative draws from the inputs the system will actually see, so inputs not covered by the test set, near-duplicate prompts or adversarial cases are not covered by the bound.
5. Rewrites the claim in a defensible form: no failures in 300 tests, so the failure rate is below about 1% with 95% confidence for inputs like those tested.

**Source:** How many tests is enough?

# 4. Exploratory data analysis, data quality and missing data

## ES-4.1

A hospital estimates 30-day readmission from follow-up calls. Of 1,000 discharged patients, the calls reach 820, so 18% of outcomes are missing. Suppose, unknown to the analyst, that 300 patients were in poor health with 50% readmitted and 700 were in good health with 10% readmitted, and that the calls reached 40% of the poor-health patients and all of the good-health patients. (a) Compute the true readmission rate and the rate the analyst sees among those reached. (b) Classify the missingness (MCAR, MAR or MNAR) in two cases: health status is recorded for every patient, and missingness depends on whether the patient was readmitted with no recorded proxy. (c) Say what the analyst should do in each case and why dropping rows or mean imputation does not fix it.

**Points:** 5

**Rubric (1 point each):**

1. Computes the true rate (300 × 0.5 + 700 × 0.1) / 1,000 = 22% and the observed rate 130 / 820 ≈ 15.9%, an understatement of about 6 points.
2. Defines the three types: MCAR (missingness unrelated to any variable), MAR (depends only on observed variables) and MNAR (depends on the missing value itself even after accounting for observed variables).
3. With health status recorded, missingness depends on an observed variable (MAR), so weighting or imputing within health strata can recover the 22%.
4. When missingness depends on the outcome with no proxy (MNAR), the observed data cannot reveal or correct it; the analyst needs sensitivity analysis, intensive follow-up of a random sample of non-responders, or outside data.
5. Explains that complete-case analysis and mean imputation implicitly assume missing completely at random, so they reproduce the biased 15.9% and overstate precision; keep missingness indicators and report how much is missing.

**Source:** Missing data and imputation

## ES-4.2

A data engineer merges three source tables of loan applications into one table of 4,800,000 rows; the sources held 5,000,000 applications in total. The checks pass: no nulls, correct types, values in valid ranges, and means and standard deviations in line with last quarter. The engineer declares the dataset "clean". It later emerges that all 200,000 missing applications came from one region with 1,000,000 applications, where the default rate is 12% against 3% elsewhere. (a) Compute the overall and regional losses and the overall default rate before and after the loss, assuming the dropped rows were typical of their region. (b) Explain why the checks that passed could not detect the problem. (c) Name three further checks or practices that would have caught it and say what each examines.

**Points:** 5

**Rubric (1 point each):**

1. Computes an overall loss of 200,000 / 5,000,000 = 4% and a regional loss of 200,000 / 1,000,000 = 20%.
2. Computes the default rate falling from 4.8% to 4.5% (216,000 of 4,800,000), a shift small enough to pass for ordinary quarter-to-quarter variation.
3. Explains that checks on nulls, types, ranges and summary statistics examine only the rows present, so a row that never arrived leaves no trace; a passing check shows only that the property tested holds.
4. Names row reconciliation: compare counts per source, per stage and per group before and after each join or merge against what was expected.
5. Names two further practices, such as repeating the checks within each subgroup (region), comparing against an independent control total, and plotting distributions by group, together with domain knowledge about what the counts should be.

**Source:** Statistical checks: test the data before you trust it

# 5. Modeling basics: fit, overfitting and evaluation

## ES-5.1

A vendor says its screening model is "99.3% accurate" at flagging a rare condition. On a test set of 100,000 cases, 800 are positive. The model flags 300 cases, of which 200 are truly positive. An alternative model flags 3,000 cases and catches 600 of the positives. (a) Build the confusion matrix for the first model and compute accuracy, precision, recall and F1. (b) Compare it with a trivial baseline. (c) Explain which metrics the decision should rest on, and compare the two models when a missed positive costs 500 and a false alarm costs 10.

**Points:** 5

**Rubric (1 point each):**

1. Gives TP 200, FP 100, FN 600, TN 99,100 and computes accuracy 99.3%, precision 200/300 ≈ 67%, recall 200/800 = 25% and F1 ≈ 0.36.
2. Notes that a baseline that flags nothing scores 99,200 / 100,000 = 99.2% accuracy, so 99.3% is barely better than doing no detection, because accuracy is dominated by the majority class.
3. Explains that the decision should rest on metrics that respect the rare class, such as recall (here 600 of 800 positives are missed), precision and the precision-recall trade-off, not accuracy.
4. Computes expected cost = 500 × misses + 10 × false alarms: 301,000 for the first model, 124,000 for the alternative (200 misses, 2,400 false alarms) and 400,000 for flagging nothing, so the alternative wins despite lower accuracy (97.4%) and precision (20%).
5. Explains that the operating point should be chosen to minimize expected cost or meet a recall target on validation data, noting that with calibrated probabilities the cost-minimizing cutoff is 10 / (10 + 500) ≈ 2% and that the deployment base rate matters.

**Source:** Classification, logistic regression and metrics

## ES-5.2

A team tunes a classifier by trying 200 hyperparameter configurations and scoring each on the same fixed test set of 500 labeled examples. The best configuration scores 85% accuracy and the team reports "85% expected accuracy in production". Suppose, hypothetically, that all 200 configurations truly have 80% accuracy. (a) Explain why the best score is still expected to exceed 80%, and estimate the size of the effect using the standard error of a single score. (b) Describe a protocol that avoids the problem. (c) List two other ways the 85% could be inflated.

**Points:** 5

**Rubric (1 point each):**

1. Computes the standard error of one score, √(0.8 × 0.2 / 500) ≈ 1.8 percentage points, so identical configurations still differ by chance.
2. Explains that taking the maximum of 200 noisy scores selects luck (selection bias, the winner's curse): the expected best of 200 is about 2.7 standard errors above the truth, roughly 84 to 85% here.
3. States that the test set was used for model selection and is therefore no longer an independent estimate.
4. Proposes tuning on a separate validation set or by cross-validation (or nested cross-validation), then using the test set once for the chosen model and reporting an interval (about ±3.5 points at 500 examples).
5. Names two other inflations: leakage from preprocessing or feature selection done on all data before splitting, duplicate or near-duplicate examples across splits, or a test distribution that differs from production.

**Source:** Resampling and validation
