# Foundations (probability and statistics for skeptics)

Questions on the probability and statistics that checking a claim about an AI system depends on: conditional probability and base rates, distributions, sampling and inference, data quality and missing data, and the basics of fitting and evaluating a model. Each section keeps its own heading below.

# 1. Probability, conditional probability and Bayes' theorem

## MA-1.1

A fraud team reports that its transaction classifier "catches 90% of fraud" and "wrongly flags only 4% of legitimate transactions". In the traffic being scored, 0.5% of transactions are fraudulent. Consider 100,000 transactions and assume the two rates hold exactly (90% of the fraudulent ones flagged, 4% of the legitimate ones flagged). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If 5% of transactions were fraudulent instead, with the same two rates, more than half of the flagged transactions would be fraudulent.
- [ ] B. If the false-flag rate were halved to 2%, more than 30% of flagged transactions would be fraudulent.
- [ ] C. Roughly one in ten flagged transactions would be fraudulent.
- [ ] D. About 450 fraudulent and about 3,980 legitimate transactions would be flagged.
- [ ] E. A flagged transaction has a 90% chance of being fraudulent.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 4,500 true flags and 3,800 false flags give about 54% fraudulent; a higher base rate raises the share of correct flags.
- B: With a 2% false-flag rate there would be 450 true and 1,990 false flags, about 18% fraudulent, well under 30%.
- C: 450 / (450 + 3,980) is about 10%.
- D: 0.90 × 500 = 450 and 0.04 × 99,500 = 3,980.
- E: 90% is P(flagged | fraud); the chance that a flag is correct, P(fraud | flagged), also depends on how common fraud is.

**Source:** Conditional probability, independence, Bayes

## MA-1.2

A help desk logged 1,000 tickets. Of the 300 billing tickets, 30 were escalated. Of the 700 technical tickets, 140 were escalated. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P(escalated) is 0.15, the simple average of 0.10 and 0.20.
- [ ] B. Ticket type and escalation are independent in this data.
- [ ] C. P(billing and escalated) = 0.10.
- [ ] D. P(billing | escalated) equals P(escalated | billing), which is 0.10.
- [ ] E. P(escalated | technical) = 0.20.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The overall rate weights each group's rate by its share of tickets: 0.3 × 0.10 + 0.7 × 0.20 = 0.17.
- B: Independence would need P(escalated | type) to equal P(escalated) = 0.17 for both types, but the rates are 0.10 and 0.20.
- C: The joint probability is 30 / 1,000 = 0.03; 0.10 is the conditional P(escalated | billing).
- D: Of the 170 escalated tickets 30 are billing, so P(billing | escalated) is about 0.18; swapping the conditioning event changes the number.
- E: 140 / 700 = 0.20.

**Source:** Conditional probability, independence, Bayes

## MA-1.3

Two automated checkers each miss a given defect with probability 0.10. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The probability that both checkers miss is 0.01 even if both were built with the same method and tend to miss the same defects.
- [ ] B. If the two checkers miss independently, the probability that both miss a given defect is 0.01.
- [ ] C. If the checkers miss independently, the probability that exactly one of them misses is 0.18.
- [ ] D. If P(second misses | first misses) = 1, the two misses are independent events.
- [ ] E. If the second checker only misses defects that the first checker also misses, the probability that both miss is 0.10.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Shared blind spots make the misses positively dependent, so P(both miss) is larger than 0.01.
- B: Independence means the joint probability is the product, 0.10 × 0.10.
- C: Exactly one misses: 2 × 0.10 × 0.90 = 0.18.
- D: Independence needs P(second misses | first misses) to equal P(second misses) = 0.10; a conditional probability of 1 is extreme dependence.
- E: The second checker's misses are then a subset of the first's, and both have probability 0.10, so they are the same set of defects.

**Source:** Conditional probability, independence, Bayes

## MA-1.4

Assume 365 equally likely birthdays and people whose birthdays are independent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If birthdays cluster on certain dates instead of being uniform, a shared birthday becomes less likely than in the uniform case.
- [ ] B. P(at least two share a birthday) equals 1 minus P(all birthdays are different).
- [ ] C. With 23 people the probability that at least two share a birthday is above 50%.
- [ ] D. With 30 people the probability that at least two share a birthday is about 30/365, roughly 8%.
- [ ] E. In a group of 23, the probability that one particular person shares a birthday with at least one of the other 22 is also above 50%.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Unequal birthday frequencies raise the chance of a match; the uniform case is the least likely to produce one.
- B: This is the complement rule, and it is how the probability is computed.
- C: The probability is about 50.7% at 23 people, which give 253 pairs.
- D: With 30 people the probability is about 71%; the number of pairs (435), not the number of people, drives it.
- E: For one named person the chance is 1 − (364/365)^22, about 6%; the 50% figure is about any two people in the group.

**Source:** Counting

## MA-1.5

A mail filter's statistics: 30% of all messages are spam. The word "urgent" appears in 60% of spam messages and in 10% of legitimate messages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If spam were only 5% of messages, the same word would give P(spam | "urgent") of about 0.24.
- [ ] B. P(spam | "urgent") is about 0.72.
- [ ] C. P(spam | "urgent") is 0.60, because the word appears in 60% of spam.
- [ ] D. Prior odds of 3 to 7 multiplied by the likelihood ratio give posterior odds of about 2.6 to 1.
- [ ] E. The likelihood ratio for "urgent" (spam versus legitimate) is 6.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: 0.05 × 0.6 = 0.03 and 0.95 × 0.1 = 0.095, so 0.03 / 0.125 = 0.24.
- B: 0.18 / (0.18 + 0.07) = 0.72.
- C: 0.60 is P("urgent" | spam), the reverse conditional; the base rate and the word's frequency in legitimate mail change the answer.
- D: (3/7) × 6 is about 2.57, which corresponds to a probability of 0.72.
- E: 0.60 / 0.10 = 6.

**Source:** Conditional probability, independence, Bayes

# 2. Random variables and distributions

## MA-2.1

An agent retries a failing tool call before giving up. Let X be the number of retries in one run, with P(X=0) = 0.50, P(X=1) = 0.30, P(X=2) = 0.15 and P(X=3) = 0.05. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Over 1,000 independent runs the total number of retries will be exactly 750.
- [ ] B. The standard deviation of X is about 0.89.
- [ ] C. Var(2X + 1) = 2 × Var(X) + 1.
- [ ] D. E[X] = 0.75.
- [ ] E. The most likely value of X is also its expected value.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The expected total is 750, but the actual total varies from run to run (a standard deviation of about 28).
- B: E[X²] = 1.35, so Var(X) = 1.35 − 0.5625 = 0.7875 and the standard deviation is about 0.89.
- C: Adding a constant does not change the variance and multiplying by 2 multiplies it by 4, so Var(2X + 1) = 4 Var(X) = 3.15.
- D: 0(0.50) + 1(0.30) + 2(0.15) + 3(0.05) = 0.75.
- E: The most likely value is 0 (probability 0.5); the mean of 0.75 is not even a possible value.

**Source:** Expected value and spread

## MA-2.2

X is a continuous random variable that is uniformly distributed on the interval from 0 to 0.5 (for example, a measured delay in seconds). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The cumulative distribution function reaches 1 at x = 0.5 and stays at 1 beyond it.
- [ ] B. E[X] = 0.25.
- [ ] C. P(X = 0.25) = 2.
- [ ] D. The density equals 2 everywhere on the interval, and a density value above 1 is allowed.
- [ ] E. P(0.1 ≤ X ≤ 0.2) = 0.2.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: P(X ≤ x) cannot rise above 1, and all the probability lies at or below 0.5.
- B: By symmetry the mean is the midpoint of the interval, 0.25.
- C: For a continuous variable the probability of any single exact value is 0; the density value 2 is not a probability.
- D: The density must integrate to 1 over a width of 0.5, so it is 2; a density is not a probability and can exceed 1.
- E: Probability is the area under the density: 2 × 0.1 = 0.2.

**Source:** Random variables

## MA-2.3

A model answers each of 20 test prompts correctly with probability 0.8, independently, so the number of correct answers is Binomial(20, 0.8). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The probability that all 20 answers are correct is about 1.2%.
- [ ] B. The probability of at least 18 correct answers is about 0.5, because 18 is close to the mean of 16.
- [ ] C. If many of the 20 prompts are near-duplicates, the number correct would vary more than the binomial variance of 3.2 suggests.
- [ ] D. The expected number correct is 16 and the variance is 3.2.
- [ ] E. The probability of exactly 16 correct answers is 0.80.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 0.8^20 is about 0.0115.
- B: P(X ≥ 18) is about 0.21; 18 is more than one standard deviation (1.79) above the mean.
- C: Positively correlated outcomes violate independence and make the count more variable than the binomial formula says.
- D: The mean is np = 16 and the variance is np(1−p) = 20 × 0.8 × 0.2 = 3.2.
- E: 16 is the mean, but the probability of exactly 16 is C(20,16) × 0.8^16 × 0.2^4, about 0.22.

**Source:** Probability distributions

## MA-2.4

Request latency for a service is modeled as a normal distribution with mean 200 ms and standard deviation 40 ms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. About one third of requests would be faster than 160 ms.
- [ ] B. If real latencies are fat-tailed but have the same mean and standard deviation, the fraction of requests over 280 ms must still equal the fraction this normal model predicts.
- [ ] C. A 360 ms request is a 4-standard-deviation event that the model expects about once per 1,000 requests.
- [ ] D. About 2.3% of requests would take longer than 280 ms.
- [ ] E. About 95% of requests would fall between 120 ms and 280 ms.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: 160 ms is one standard deviation below the mean (z = −1), which has about 16% below it, roughly one in six.
- B: Tail mass depends on the whole shape of the distribution, not just the mean and standard deviation, so the fraction beyond 280 ms can differ from the normal model's figure (in either direction).
- C: z = 4 has an upper tail of about 3 in 100,000, roughly one request in 31,600.
- D: 280 ms is z = 2 and the upper tail beyond it is about 2.3%.
- E: 120 ms and 280 ms are 2 standard deviations on either side, which contain about 95.4%.

**Source:** Probability distributions

## MA-2.5

A team sets an alert threshold at the mean plus a multiple of the standard deviation and wants to know how often values would exceed it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A two-sided "six-sigma" failure probability of about 2 in a billion, computed from the normal curve, remains valid when the real distribution is fat-tailed with the same mean and standard deviation.
- [ ] B. For any distribution with finite variance, at most 1/9 (about 11%) of its probability lies more than 3 standard deviations from the mean.
- [ ] C. A Student t distribution with 3 degrees of freedom, rescaled to a standard deviation of 1, has about 1.4% of its probability beyond 3 standard deviations, around five times the normal figure.
- [ ] D. For a standard Cauchy distribution, the average of 1,000 independent observations is no more concentrated than a single observation.
- [ ] E. For a normal distribution about 0.27% lies beyond 3 standard deviations, so the distribution-free bound of 1/9 is loose in that case.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The normal tail figure depends on the normal shape; heavier tails put far more probability at extreme distances.
- B: This is Chebyshev's inequality, P(|X − μ| ≥ kσ) ≤ 1/k², which needs only a finite variance.
- C: The two-sided tail beyond 3 SD is about 1.38% for this t distribution against 0.27% for the normal.
- D: The mean of n independent standard Cauchy variables is itself standard Cauchy, so averaging does not help (there is no finite mean).
- E: The normal tail beyond 3 SD is about 0.27%, much smaller than the worst-case 11% that Chebyshev allows.

**Source:** Probability distributions

# 3. Sampling, the central limit theorem and inference

## MA-3.1

An engineer runs 400 independent evaluation prompts and 320 pass (an observed pass rate of 0.80). Treat the prompts as an independent random sample and use the normal approximation, with 1.96 for a 95% interval. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The standard error of the observed pass rate is 0.02.
- [ ] B. With 400 prompts, the standard error would be smaller if the observed rate were 0.50 instead of 0.80.
- [ ] C. A 95% confidence interval for the true pass rate is about 0.76 to 0.84.
- [ ] D. Cutting the margin of error to ±1 percentage point would need about 1,600 prompts.
- [ ] E. Running 800 prompts at the same observed rate would cut the margin of error in half.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: √(0.8 × 0.2 / 400) = 0.02.
- B: √(p(1−p)/n) is largest at p = 0.5, giving 0.025 here, which is larger than 0.02.
- C: 0.80 ± 1.96 × 0.02 gives 0.761 to 0.839.
- D: The present margin is about ±3.9 points; a margin of ±1 point needs about 1.96² × 0.16 / 0.01² ≈ 6,150 prompts.
- E: The standard error scales with 1/√n, so doubling n shrinks it by a factor of about 1.41; halving it takes four times as many prompts.

**Source:** Central limit theorem

## MA-3.2

An A/B test compares a new answer-ranking feature with the old one, with 20,000 users per arm. Conversion is 10.0% in the control arm and 10.6% in the treatment arm. A two-sided test of equal conversion rates gives p = 0.048. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. There is a 4.8% probability that the feature has no effect.
- [ ] B. If the feature had no effect, a difference at least this large would arise in about 4.8% of repeated experiments.
- [ ] C. With the same observed rates but only 2,000 users per arm, the p-value would still be below 0.05.
- [ ] D. There is a 95.2% probability that the feature truly raises conversion.
- [ ] E. The small p-value shows that the effect is large.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A p-value is computed assuming no effect; it is not the probability that the no-effect hypothesis is true.
- B: This is the definition of a p-value: the probability, assuming no effect, of data at least as extreme as observed.
- C: With ten times fewer users the standard error is about three times larger and the same gap gives a p-value near 0.5.
- D: The p-value does not give the probability that the alternative is true; that would need a prior and a different calculation.
- E: The observed gap is 0.6 percentage points; with large samples even small effects can give small p-values.

**Source:** Statistical inference, estimation and hypothesis testing

## MA-3.3

A research group screens 200 independent hypotheses. Exactly 20 of them are true effects and 180 are true nulls. Each test uses significance level 0.05, and the tests of the true effects have power 0.80. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the significance level is 0.05, about 95% of the significant results are real effects.
- [ ] B. About 64% of the significant results are real effects.
- [ ] C. Raising the power of every test to 100% (a Type II error rate of 0) would make every significant result a real effect.
- [ ] D. About 25 significant results are expected, of which about 16 are real effects and 9 are false positives.
- [ ] E. If only 4 of the 200 hypotheses were true effects (same significance level and power), roughly a quarter of the significant results would be real.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The significance level is the Type I error rate (false positives among true nulls), not the share of significant results that are real; that share depends on the base rate of true effects.
- B: 16 / 25 = 0.64.
- C: With full power the 20 true effects are detected, but the 180 nulls still yield about 9 false positives, so about 69% are real.
- D: Power 0.8 × 20 = 16 detections and 0.05 × 180 = 9 false positives.
- E: Then 3.2 true detections and 9.8 false positives, so 3.2 / 13 is about 25% real.

**Source:** Statistical inference, estimation and hypothesis testing

## MA-3.4

A team tests 20 independent prompt variants against a baseline, each with a two-sided test at significance level 0.05. Suppose that, unknown to the team, none of the variants truly differs from the baseline. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The expected number of variants reaching p < 0.05 is 1.
- [ ] B. Requiring p < 0.0025 (that is, 0.05 / 20) for each test keeps the chance of at least one false positive at or just under 5%.
- [ ] C. The probability that at least one of the 20 variants reaches p < 0.05 is about 5%.
- [ ] D. The Benjamini–Hochberg procedure controls the probability of making any false discovery, in the same way as the Bonferroni correction.
- [ ] E. If only the best variant is reported, and its raw p-value is below 0.05, the p-value is a valid measure of evidence even when the other 19 tests are not mentioned.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: 20 × 0.05 = 1 expected false positive.
- B: 1 − (1 − 0.0025)^20 is about 4.9%, the Bonferroni guarantee.
- C: The chance of at least one false positive is 1 − 0.95^20, about 64%.
- D: Benjamini–Hochberg controls the false discovery rate (the expected share of false findings among discoveries), a weaker guarantee than controlling any false positive.
- E: Choosing the best of 20 results after the fact means a raw p-value understates how easily chance produces such a result.

**Source:** Statistical inference, estimation and hypothesis testing

## MA-3.5

A study reports that a reranking change improved accuracy by 2.0 percentage points, with a standard (frequentist) 95% confidence interval of 0.5 to 3.5 points. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 90% interval computed from the same data would be narrower than this one.
- [ ] B. If the same procedure were repeated on many independent samples, about 95% of the intervals it produced would contain the true improvement.
- [ ] C. A two-sided test of "no improvement" at the 5% level would reject, because the interval excludes 0.
- [ ] D. About 95% of individual queries improved by an amount between 0.5 and 3.5 points.
- [ ] E. There is a 95% probability that the true improvement lies between 0.5 and 3.5 points.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A lower confidence level uses a smaller multiplier, so the interval is narrower.
- B: That long-run coverage is the meaning of a 95% confidence interval.
- C: A 95% interval that excludes zero corresponds to rejecting zero at the 5% level (two-sided).
- D: The interval concerns the average improvement, not the spread of individual changes, which is much wider.
- E: Once computed, a given interval either contains the true value or does not; the 95% describes the procedure, not this particular interval.

**Source:** Statistical inference, estimation and hypothesis testing

## MA-3.6

Consider the sample mean of n independent, identically distributed observations from a right-skewed population with finite variance (for example, task completion times). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For an exponential population (skewness 2), the sample mean has skewness 2/√n, about 0.89 at n = 5 and 0.2 at n = 100.
- [ ] B. The sample mean has standard deviation σ/√n, and its distribution approaches a normal distribution as n grows.
- [ ] C. A sample of about 30 is a common rule of thumb for the normal approximation, but heavily skewed or outlier-prone populations can need far more.
- [ ] D. As n grows, a histogram of the individual observations becomes bell-shaped.
- [ ] E. If the observations are strongly positively correlated, for example many near-copies of the same item, the standard error σ/√n understates the real uncertainty.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The skewness of a mean of n independent exponentials is 2/√n, which falls toward 0 as n grows.
- B: This is the central limit theorem for independent, identically distributed data with finite variance.
- C: The n ≈ 30 figure is a guideline, not a theorem, and skew or extreme values slow convergence.
- D: The data keep the population's shape; it is the distribution of the sample mean that becomes bell-shaped.
- E: Correlated observations carry less information than n independent ones, so the effective sample size is smaller than n.

**Source:** Central limit theorem

## MA-3.7

A tutoring app shows a satisfaction survey to its 1.25 million users. A total of 50,000 users (4%) respond, and 92% of respondents say they are satisfied. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If non-respondents averaged 80% satisfaction, satisfaction among all users would be about 80.5%.
- [ ] B. A 4% response rate is harmless when the number of respondents is as large as 50,000.
- [ ] C. The standard error reflects random variation among respondents but not the effect of who chose to respond.
- [ ] D. A random sample of 500 users, nearly all of whom respond after follow-up, could give a less biased estimate than the 50,000 volunteers, even though its standard error is larger.
- [ ] E. The margin of error of about ±0.24 points shows that satisfaction among all 1.25 million users lies between 91.8% and 92.2%.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 0.04 × 0.92 + 0.96 × 0.80 = 0.8048.
- B: A large number of volunteers shrinks the standard error but does not remove selection bias, which depends on the response mechanism.
- C: Standard errors measure chance variation; they cannot detect a systematic difference between responders and non-responders.
- D: Bias can dominate error; a smaller probability sample with high response avoids the self-selection that the volunteer sample cannot fix.
- E: The margin describes sampling variation only and holds under random sampling; self-selection can shift the result by far more than 0.24 points.

**Source:** Statistical inference, estimation and hypothesis testing

# 4. Exploratory data analysis, data quality and missing data

## MA-4.1

A survey records age for every respondent and asks for income, which some respondents leave blank. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Whether the blank incomes are missing not at random can be confirmed from the observed values alone.
- [ ] B. Mean imputation gives an unbiased estimate of average income when higher earners skip the question because of their income.
- [ ] C. If higher earners tend to skip the question because of how much they earn, income is missing not at random.
- [ ] D. If older respondents skip the question more often, and within each age group skipping is unrelated to income, income is missing at random given age.
- [ ] E. If the blanks come from a random server glitch unrelated to anything measured, income is missing completely at random.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Missing-not-at-random depends on the very values that are unobserved, so the observed data cannot confirm it; it takes outside knowledge or assumptions.
- B: The observed incomes are then too low on average, and filling blanks with their mean keeps that bias.
- C: Missingness that depends on the value being reported is missing not at random.
- D: Missingness that depends only on an observed variable (age) is missing at random, and adjusting for age can correct it.
- E: Missingness unrelated to any variable is missing completely at random.

**Source:** Missing data and imputation

## MA-4.2

A column has 10 rows. Five values are observed (10, 20, 30, 40, 50) and five are missing. An analyst fills each blank with the observed mean (30) and treats all 10 rows as real data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Filling the blanks with the median instead would preserve the original sample variance.
- [ ] B. The standard error of the mean computed from the 10 filled rows (about 3.3) is a fair measure of the uncertainty.
- [ ] C. The mean of the column stays at 30.
- [ ] D. Mean imputation is a safe default whenever many values are missing, whatever the reason for the missingness.
- [ ] E. The sample variance falls from 250 to about 111.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Any single constant added at the center lowers the variance; filling with the median (here also 30) gives the same result as the mean.
- B: The five invented values add no information; the honest standard error rests on five observations (about 7.1), so 3.3 overstates precision.
- C: Adding values equal to the mean leaves the mean unchanged.
- D: Mean imputation shrinks spread and distorts correlations, and it biases results when missingness depends on the missing value.
- E: The sum of squared deviations stays 1,000 but is now divided by 9 instead of 4: 111.1 against 250.

**Source:** Missing data and imputation

## MA-4.3

Eleven response times in seconds are 12, 13, 14, 14, 15, 15, 16, 18, 18, 19 and 120. The median is 15, the first and third quartiles are 14 and 18, the mean is about 24.9 and the sample standard deviation is about 31.6. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Whether to keep the 120 depends on how it arose, since it might be a genuine rare event such as a timeout.
- [ ] B. The mean of 24.9 seconds is a typical response time for this data.
- [ ] C. By the 1.5 × IQR rule the upper fence is 24, so 120 is flagged.
- [ ] D. A value flagged as an outlier by the 1.5 × IQR rule should be deleted automatically.
- [ ] E. Without the 120, the mean would be about 15.4 and the sample standard deviation about 2.3, while the median would stay at 15.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The decision depends on the data-generating process, such as a recording error versus a real slow request.
- B: Ten of the eleven values lie between 12 and 19; the single large value pulls the mean up to 24.9.
- C: IQR = 18 − 14 = 4 and 18 + 1.5 × 4 = 24; 120 is far above it.
- D: The rule flags values for inspection; deleting a real extreme observation can bias the analysis.
- E: The median is resistant to one extreme value; the mean and the standard deviation are not.

**Source:** Descriptive statistics and EDA

## MA-4.4

A pipeline joins an orders table to a customer table. The orders table has 50,000 rows; the joined table has 47,500. All 2,500 dropped rows belong to one region that had 10,000 orders. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The region's share of the data fell from 20% to about 15.8%.
- [ ] B. Range and type checks on the 47,500 remaining rows can all pass even though rows are missing.
- [ ] C. Comparing row counts per region before and after the join would reveal the loss.
- [ ] D. Because only 5% of rows are missing, any statistic computed on the joined table is within 5% of its true value.
- [ ] E. The join lost 5% of rows overall but 25% of the affected region's rows.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The region goes from 10,000 / 50,000 = 20% to 7,500 / 47,500, about 15.8%.
- B: Checks on present rows only test those rows; rows that never arrived leave nothing to flag.
- C: A by-group reconciliation of counts across the join exposes the concentrated loss that the overall total hides.
- D: The lost rows can differ systematically from the rest; if they were all the positive cases, a positive rate of 5% could drop to 0%.
- E: 2,500 / 50,000 = 5% overall and 2,500 / 10,000 = 25% for the region.

**Source:** Statistical checks: test the data before you trust it

## MA-4.5

Check each statement that is true about summarizing data with statistics and plots. Each statement is worth 1 point (5 points total).

- [ ] A. If X takes the values −3, −2, −1, 0, 1, 2, 3 and Y = X², the Pearson correlation between X and Y is 0 even though Y is fully determined by X.
- [ ] B. Pearson correlation is resistant to extreme points: a single outlier cannot change it by much.
- [ ] C. A tall spike of values at exactly 0 in a measurement that should be continuous is often a sign of a default or missing-value code.
- [ ] D. Datasets with identical means, variances and correlation can have very different scatter plots, which is why plots are examined in addition to summary numbers.
- [ ] E. A Pearson correlation of 0.9 in observational data shows that X causes Y.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The relationship is symmetric and nonlinear, so the linear correlation is exactly 0.
- B: One far-away point can move Pearson's r from near 0 to near 1, or the reverse.
- C: A spike at an exact value usually reflects how the data were recorded, not a natural measurement.
- D: Different shapes can share the same summary statistics, so numbers alone can hide structure that a plot shows.
- E: Correlation measures association; confounding, reverse causation or selection can produce it without causation.

**Source:** Descriptive statistics and EDA

# 5. Modeling basics: fit, overfitting and evaluation

## MA-5.1

A classifier for a rare event is evaluated on 100,000 cases, 1,000 of which are truly positive. The counts at three decision thresholds are below. Treat a missed positive as costing 20 units and a false alarm as costing 1 unit.

| Threshold | True positives | False positives |
|---|---|---|
| 0.3 | 900 | 3,000 |
| 0.5 | 800 | 800 |
| 0.7 | 500 | 100 |

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The F1 score is highest at threshold 0.5.
- [ ] B. Total cost is lowest at threshold 0.5.
- [ ] C. At threshold 0.7, 83% of the actual positives are caught.
- [ ] D. From threshold 0.3 to threshold 0.7, recall falls and precision rises.
- [ ] E. Accuracy ranks the three thresholds in the same order as total cost does.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: F1 is about 0.367, 0.615 and 0.625 for thresholds 0.3, 0.5 and 0.7, so it is highest at 0.7.
- B: Costs are 100 × 20 + 3,000 = 5,000 at 0.3; 200 × 20 + 800 = 4,800 at 0.5; 500 × 20 + 100 = 10,100 at 0.7.
- C: 83% is the precision at 0.7 (500 of 600 flagged); recall is 500 / 1,000 = 50%.
- D: Recall goes 0.90, 0.80, 0.50 and precision goes 0.23, 0.50, 0.83.
- E: Accuracy is 96.9%, 99.0% and 99.4%, so it prefers 0.7, which has the highest cost.

**Source:** Classification, logistic regression and metrics

## MA-5.2

Polynomial regressions of degree 1, 3, 9 and 15 are fit to 40 training points. Errors (root mean squared error) are measured on the training points and on 40 held-out points.

| Degree | Training error | Held-out error |
|---|---|---|
| 1 | 4.1 | 4.3 |
| 3 | 2.2 | 2.5 |
| 9 | 0.4 | 3.9 |
| 15 | 0.05 | 11.2 |

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For the degree-15 model, more training data or a penalty on large coefficients would be expected to reduce the held-out error.
- [ ] B. The problem with degree 15 is that the model is too rigid.
- [ ] C. On these data, degree 3 has the lowest held-out error.
- [ ] D. Degree 15 is the best model because it has the lowest training error.
- [ ] E. Degree 1 is underfitting: both of its errors are high and close together.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: More data constrains a flexible model, and regularization limits its effective flexibility; both reduce variance.
- B: A training error of 0.05 against 11.2 held out is the signature of an overly flexible model fitting noise.
- C: 2.5 is the smallest held-out error among the four.
- D: Training error always falls as flexibility rises; it does not measure performance on new data.
- E: A model that is too simple has high error on both sets, with little gap between them.

**Source:** Regularization, model selection, bias and variance

## MA-5.3

A data scientist has 60 examples and 5,000 features. The features are pure noise and the labels are independent coin flips. Procedure X picks the 20 features most correlated with the label using all 60 examples, then runs 5-fold cross-validation of a logistic regression on those 20 features, and reports 92% accuracy. Procedure Y repeats the feature selection inside each training fold only. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Using 10 folds or leave-one-out cross-validation in Procedure X would remove the problem.
- [ ] B. On new data, the model from Procedure X would be expected to be right about 92% of the time.
- [ ] C. Procedure X's 92% is optimistic because the held-out labels influenced which features were chosen.
- [ ] D. Procedure Y would be expected to report accuracy near 50% on average.
- [ ] E. Fitting any label-dependent step, such as target encoding, on the whole dataset before splitting causes the same kind of leakage.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The selection step has already used every label, so the number of folds does not change the leak.
- B: The 92% reflects leakage; with noise features the model should be right about half the time on new data.
- C: Choosing the features that happen to correlate with all labels, including the held-out ones, builds the test answers into the model.
- D: With no real signal, an honest evaluation of a fair-coin task should give roughly 50% accuracy, up to chance variation.
- E: Any step that sees the held-out labels before evaluation contaminates the estimate; such steps belong inside each training fold.

**Source:** Resampling and validation

## MA-5.4

A logistic regression predicts whether an account is flagged: log-odds of being flagged = −2.0 + 0.9 × x, where x is the number of prior incidents. Use e^(−2.0) ≈ 0.135 and e^(0.9) ≈ 2.46. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For an account with x = 1 the predicted probability of being flagged is about 0.25.
- [ ] B. The increase in predicted probability from x = 1 to x = 2 is the same as from x = 0 to x = 1.
- [ ] C. Each additional prior incident multiplies the predicted probability of being flagged by 2.46.
- [ ] D. Each additional prior incident multiplies the odds of being flagged by about 2.46.
- [ ] E. For an account with x = 0 the predicted probability of being flagged is about 0.12.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Odds are 0.135 × 2.46 ≈ 0.33, so the probability is 0.33 / 1.33 ≈ 0.25.
- B: The probabilities are about 0.12, 0.25 and 0.45, so the steps are about 0.13 and 0.20; the probability effect depends on where you start.
- C: The coefficient acts on the odds, not the probability: 0.12 becomes about 0.25, not 0.29.
- D: exp(0.9) ≈ 2.46 is the odds ratio per extra incident.
- E: At x = 0 the odds are 0.135, so the probability is 0.135 / 1.135, about 0.12.

**Source:** Classification, logistic regression and metrics

## MA-5.5

A scorer assigns probabilities of being positive to nine cases. The four positives scored 0.9, 0.8, 0.7 and 0.4. The five negatives scored 0.6, 0.5, 0.3, 0.2 and 0.1. The AUC is the probability that a randomly chosen positive is scored above a randomly chosen negative. Log loss for one case is −ln of the probability the model gave to the outcome that occurred. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The AUC of this scorer is 0.90.
- [ ] B. An AUC of 0.90 guarantees that cases scored near 0.9 turn out to be positive about 90% of the time.
- [ ] C. If cases are predicted positive when the score is above 0.5, 90% of the nine cases are classified correctly.
- [ ] D. Replacing every score with its cube would leave the AUC unchanged.
- [ ] E. Giving probability 0.99 to an outcome that does not occur costs about 4.6 in log loss, about five times as much as giving 0.6 to it.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: 18 of the 20 positive-negative pairs are ranked correctly (only 0.4 loses, to 0.6 and 0.5), so AUC = 18 / 20 = 0.90.
- B: AUC measures ranking, not calibration; a well-ranked scorer can still have scores that do not match observed frequencies.
- C: Above 0.5, three positives and one negative are flagged and one positive is missed, so 7 of 9 (78%) are correct.
- D: AUC depends only on the ranking of the scores, and cubing keeps the order.
- E: The outcome that occurred had been given probability 0.01, so the loss is −ln 0.01 ≈ 4.6, against −ln 0.4 ≈ 0.92 when the model had said 0.6; confident errors are punished heavily.

**Source:** Classification, logistic regression and metrics
