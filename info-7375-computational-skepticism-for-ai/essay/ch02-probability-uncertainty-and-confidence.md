# Chapter 2: Probability, uncertainty and the confidence illusion

## ES-ch02.1

A vendor says its fraud-screening tool is "98% accurate", meaning it flags 98% of fraudulent transactions and clears 98% of legitimate ones. In the vendor's target market 0.2% of transactions (1 in 500) are fraudulent. (a) For 100,000 transactions, work out how many are flagged and how many of the flagged transactions are fraudulent. (b) Explain why the vendor's figure and your figure are both correct yet answer different questions. (c) Describe two changes that would raise the share of flags that are real fraud, and one cost of each. (d) State one operational consequence of the flag volume and what you would ask the vendor to report.

**Points:** 5

**Rubric (1 point each):**

1. Gets the counts right: 200 fraudulent transactions with 196 flagged, 99,800 legitimate with about 1,996 flagged, about 2,192 flags in total, so only about 8.9% of flags are fraud.
2. Explains that 98% is P(flag | fraud) and P(clear | legitimate), probabilities conditioned on true status, whereas the question asked is P(fraud | flag), the reverse conditional, which needs the base rate through Bayes' rule.
3. Explains the mechanism: legitimate transactions outnumber fraud by about 500 to 1, so even a 2% false-positive rate produces about ten false flags for every true one.
4. Gives two levers with a cost for each, for example raising specificity (99.9% specificity would lift the share to about 66%, at the cost of sensitivity or complexity) or screening a higher-risk subpopulation (at 2% prevalence the share is about 50%, at the cost of missing fraud outside it) or adding a second review stage.
5. Draws the operational consequence (reviewers see mostly false alarms, leading to alert fatigue and ignored real fraud) and says what to demand from a vendor: separate sensitivity and specificity and the share of flags that are real at a stated prevalence.

**Source:** The test that is 99% accurate, and the patient it kills

## ES-ch02.2

People often treat "accuracy", "discrimination" (for example AUC) and "calibration" as interchangeable ways of saying that a probabilistic classifier is good. (a) Define each of the three. (b) Give a concrete example, in numbers or by construction, of a model that is calibrated but has no discrimination, and of a model with excellent discrimination but poor calibration. (c) For each of two decisions, ranking cases for a limited number of reviewers and quoting a patient a numerical risk, say which property matters most and how you would check it.

**Points:** 5

**Rubric (1 point each):**

1. Defines accuracy at a threshold as the fraction correct after thresholding, discrimination as the ability to rank positives above negatives (AUC is the probability a random positive outscores a random negative), and calibration as agreement between stated probabilities and observed frequencies.
2. Gives a calibrated model without discrimination: always predicting the base rate (for example 0.10 at 10% prevalence) matches observed frequency overall but has AUC 0.5.
3. Gives a discriminating but miscalibrated model: any strictly increasing distortion of a perfect ranker (for example scores between 0.6 and 1.0 at 10% prevalence) keeps AUC at 1.0 while the stated probabilities are far too high.
4. Notes that accuracy at a threshold ignores the size of the probability and can be high through class imbalance alone (a majority-class baseline), so high accuracy does not establish calibration or good ranking.
5. Matches properties to decisions with checks: ranking depends on discrimination (AUC or precision at the review capacity); quoting a risk depends on calibration (reliability diagram with counts, Brier score or log loss on data from the deployment population).

**Source:** Calibration

## ES-ch02.3

Two forecasters each give a probability for 10 events, 8 of which occur. Forecaster P says 0.8 for every event. Forecaster Q says 0.99 for every event. (a) For each forecaster compute accuracy at a 0.5 cutoff, the Brier score and the log loss (natural logarithm). (b) Define a strictly proper scoring rule and explain why Brier score and log loss are strictly proper while accuracy at a cutoff is not. (c) Explain how Brier score and log loss differ in their treatment of a confident forecast that turns out wrong, and when that should influence the choice between them.

**Points:** 5

**Rubric (1 point each):**

1. Finds that accuracy at 0.5 is 0.8 for both forecasters, so it cannot distinguish the calibrated forecaster from the overconfident one.
2. Computes Brier scores of 0.160 for P and about 0.196 for Q, and log losses of about 0.500 for P and about 0.929 for Q, so P is better on both.
3. Defines a proper scoring rule as one whose expected score is optimized by reporting one's true belief, and a strictly proper rule as one for which only the true belief is optimal.
4. Explains that Brier score and log loss are strictly proper (reporting 0.8 is the unique best report when 80% of events occur) while accuracy at a cutoff is not strictly proper because any report on the correct side of 0.5 scores equally, so it neither rewards honesty nor penalizes overstatement; absolute error is improper (its expected value is minimized by reporting 0 or 1).
5. Contrasts the penalty for a confident miss: a single wrong forecast of 0.99 costs 0.98 in Brier score (bounded by 1) but about 4.6 in log loss, which is unbounded as the probability given to the outcome approaches 0, so log loss suits settings where confident errors are very costly and Brier score is less dominated by single extreme errors.

**Source:** Calibration

## ES-ch02.4

A classifier's predicted probabilities on 1,000 test cases are grouped into five bins. For each bin the table gives the number of cases, the mean predicted probability and the observed fraction of positives: (300, 0.10, 0.13), (200, 0.30, 0.38), (200, 0.50, 0.47), (150, 0.70, 0.58), (150, 0.90, 0.72). (a) Compute the expected calibration error (ECE) and the maximum calibration error. (b) Describe in words what pattern the table shows. (c) Show that the ECE depends on how the bins are drawn by recomputing it with a single bin for all 1,000 cases, and give further reasons an ECE figure alone should not decide whether a model is acceptable.

**Points:** 5

**Rubric (1 point each):**

1. Computes the ECE as the count-weighted mean absolute gap, 0.3 x 0.03 + 0.2 x 0.08 + 0.2 x 0.03 + 0.15 x 0.12 + 0.15 x 0.18 = 0.076, and the maximum calibration error as 0.18.
2. Reads the pattern: low probabilities are understated (observed rates above predictions at 0.10 and 0.30) and high probabilities are overstated (observed rates well below predictions at 0.70 and 0.90), so the probabilities are too extreme, with clear overconfidence at the top.
3. Shows binning dependence: with one bin the mean prediction is 0.43 and the observed rate 0.404, so ECE falls to 0.026 because gaps of opposite sign cancel; merging bins can only keep or lower ECE.
4. Notes sampling noise: each bin's observed rate has a standard error of roughly 0.02 to 0.04 at these counts, and even a perfectly calibrated model has a positive expected ECE at finite sample size that grows with the number of bins.
5. Recommends complements: a reliability diagram with bin counts and intervals, Brier score or log loss, equal-count bins as a check, subgroup and time slices, and attention to the probability range that drives decisions rather than a single pass-fail threshold on ECE.

**Source:** Calibration

## ES-ch02.5

A team asks a language model to answer 1,000 factual questions and to append "Confidence: N%" to each answer. The team wants to know whether those percentages can be treated as the probability that the answer is correct. Design the evaluation: what data and labels to collect, how to analyze them, what sample size issues and sources of error matter, and what the results would and would not let you conclude.

**Points:** 5

**Rubric (1 point each):**

1. Establishes an independent ground truth for each answer (graded against verified references, with a plan for ambiguous items) so that the stated confidence is compared with real correctness rather than with the model's own judgment.
2. Collects (stated confidence, correct or not) pairs, groups them by stated value (noting that verbalized numbers cluster at a few round values), computes the observed accuracy for each group, and examines a reliability diagram, a calibration error and a proper score such as Brier score or log loss.
3. Addresses sample size and variability: enough cases per group to give intervals narrow enough to be informative, repeated runs because outputs can vary, and fixed, recorded prompt wording and settings with a check of sensitivity to rewording.
4. Separates discrimination from calibration (does higher stated confidence track higher accuracy, for example by AUC for correct versus incorrect) and compares against baselines such as a constant base-rate accuracy or confidence derived from token probabilities or agreement across samples.
5. States the limits of any conclusion: results hold for this model version, prompt format and question distribution; they do not carry over to other domains or versions without re-checking; any recalibration map fitted on one set of questions must be validated on fresh questions.

**Source:** Calibration

## ES-ch02.6

An engineer writes: "We timed 25 requests. The mean was 100 ms and the standard deviation was 15 ms. The 95% interval is 93.8 to 106.2 ms, so there is a 95% chance that the next request will take between 93.8 and 106.2 ms." (a) Identify what the interval actually describes and what is wrong with the conclusion. (b) Compute the interval that does answer the engineer's question, assuming roughly normal times; the t critical value with 24 degrees of freedom is 2.064. (c) Explain how a Bayesian credible interval differs from both.

**Points:** 5

**Rubric (1 point each):**

1. Identifies 93.8 to 106.2 as the 95% confidence interval for the population mean, 100 plus or minus 2.064 x 15 / sqrt(25), which expresses uncertainty about the average and not the spread of individual requests.
2. Explains the error in the conclusion: individual requests vary with a standard deviation of 15 ms, so only about a third of them (roughly 32%) would fall inside that narrow range.
3. Computes the prediction interval, 100 plus or minus 2.064 x 15 x sqrt(1 + 1/25), about 68.4 to 131.6 ms, and notes that it does not shrink to zero with more data because individual variability remains.
4. States the correct frequentist meaning of the confidence level: across repeated samples the method captures the true mean 95% of the time, which is not the probability that this computed interval contains it and not a statement about the next observation.
5. Explains that a credible interval is a posterior probability statement about the parameter given a model and prior, so it depends on the prior, and can numerically resemble the confidence interval when the prior is diffuse or the data dominate.

**Source:** When the Central Limit Theorem politely declines to help

## ES-ch02.7

A team reports "our classifier is 96% accurate" after it classified 48 of 50 test items correctly, and says this beats a competitor's published figure of 92%, which came from a different, larger test set. (a) Give an approximate 95% interval for the team's true accuracy and say whether the data support the claim. (b) Roughly how many test items would be needed to estimate accuracy to within plus or minus 2 percentage points if the true accuracy is near 96%? (c) Name two sources of error that no sampling interval accounts for. (d) Describe how the two systems should be compared fairly.

**Points:** 5

**Rubric (1 point each):**

1. Computes an interval of roughly 86% to 99% (Wilson about 0.865 to 0.989; exact about 0.863 to 0.995) and notes that the competitor's 92% lies inside it.
2. Concludes that the data do not establish superiority: 96% is a point estimate from 50 items with wide uncertainty, a four-point gap is within sampling noise, and the competitor's figure has its own uncertainty and a different test set.
3. Sizes the test: n is about 1.96 squared x 0.96 x 0.04 / 0.02 squared, roughly 370 items (about 1,480 for plus or minus 1 point); interval width falls with the square root of n, and with unknown accuracy the conservative figure is about 2,400.
4. Names non-sampling errors such as an unrepresentative test set, near-duplicate items or leakage from training data, label noise, choosing the model or threshold after seeing the test set, and shift between test data and deployment.
5. Proposes a better comparison design: evaluate both systems on the same items and analyze paired differences with an interval, with the test set and metric fixed in advance.

**Source:** When the Central Limit Theorem politely declines to help

## ES-ch02.8

A loan-approval vendor's dashboard shows each applicant's "probability of repayment" to one decimal place, for example 92.7%, and the vendor argues that this precision shows the model is rigorous. Evaluate the argument. Say what evidence would be needed before an analyst treated 92.7% as a probability, and what else the analyst should check before relying on it to make decisions.

**Points:** 5

**Rubric (1 point each):**

1. Argues that displayed precision is a formatting choice and says nothing about validity: any model can print any number of digits, and the real uncertainty (sampling error, model error) is far larger than the last digit.
2. Explains that the number means something only if it is calibrated: among past applicants scored near 92.7%, about 93% repaid, shown by a reliability diagram or calibration error computed from labeled outcomes.
3. Requires that the evidence come from data resembling the current applicant population and period, and that calibration be rechecked over time because base rates and inputs shift.
4. Asks for supporting detail: how many cases lie behind each score range (a claim near 92.7% needs enough cases), a proper score such as Brier score or log loss compared with a trivial baseline, and calibration within subgroups rather than only in aggregate.
5. Looks beyond the probability to the decision: the costs of approving a loan that defaults versus declining one that would repay, and the possibility of rare, very large losses that an average figure hides.

**Source:** From Boolean to probabilistic — and why the move is harder than it looks

## ES-ch02.9

A disease has prevalence 0.1%. A diagnostic test has sensitivity 95% and specificity 95%. (a) A person chosen at random from the screened population tests positive. What is the probability that they have the disease? Show your reasoning with counts or Bayes' rule. (b) The test is repeated and is positive again. Under what assumption can you update by multiplying likelihood ratios, and what is the new probability? (c) Describe a realistic situation in which that assumption fails and say what follows for the posterior. (d) What would you recommend after a first positive result?

**Points:** 5

**Rubric (1 point each):**

1. Gets the first-positive probability of about 1.9% using counts (per 100,000 people: 95 true positives and 4,995 false positives) or Bayes' rule, and explains that the low base rate dominates.
2. Updates correctly: the posterior from the first result becomes the prior for the second, each positive multiplies the odds by the likelihood ratio 0.95 / 0.05 = 19, and two positives give about 27% (three would give about 87%).
3. States the assumption needed: the two results are conditionally independent given the person's true status, so errors are not shared.
4. Gives a case where it fails (the same specimen, the same assay or the same interfering substance causing both false positives) and explains that the second positive is then much less informative than independence implies, so the posterior is overstated.
5. Recommends confirmation with an independent test, ideally one that works by a different mechanism, rather than diagnosing from a single screening positive.

**Source:** Bayes' theorem

## ES-ch02.10

In a court case an expert testifies: "The chance that an innocent person would match this DNA profile is 1 in 100,000, so the chance that the defendant is innocent is 1 in 100,000." The defendant was identified by searching a database that covers all 1,000,000 possible sources, each equally likely beforehand, and the true source is one of them. Identify the error in the testimony, compute the probability that the defendant is the source given the match, and explain what the match does establish. Then explain why the same error appears when people read automated alerts.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the transposed conditional: 1 in 100,000 is P(match | innocent), whereas the court needs P(innocent | match), and the two are different quantities that need the prior to connect.
2. Computes the probability that the defendant is the source: about 10 innocent people in 1,000,000 are expected to match by chance alongside the one true source, equivalently Bayes' rule with a prior of 1 in 1,000,000, giving about 1 in 11, roughly 0.09.
3. States that the probability the defendant is innocent is therefore about 0.91, not 1 in 100,000.
4. Explains that the match is still strong evidence (a likelihood ratio of about 100,000 raised the probability from 0.000001 to 0.09) and that with other independent evidence the same match could give a probability near certainty.
5. Generalizes: reading an alert's false-positive rate as the probability that a flagged case is harmless, or its detection rate as the probability that a flagged case is real, makes the same error and requires the base rate.

**Source:** Bayes' theorem

## ES-ch02.11

A neural network classifier assigns probability 0.95 to its predicted class on a validation set, but is correct on only 80% of those cases. (a) Is this overconfidence or underconfidence, and how would you display it? (b) Temperature scaling replaces the predicted probability sigma(z), where z is the logit and sigma the logistic function, by sigma(z / T) for a single T fitted on held-out data. Show what happens to a case with logit z = 3 when T = 2, and find the T that maps it to 0.80. (c) Explain what temperature scaling cannot change and when the fix fails.

**Points:** 5

**Rubric (1 point each):**

1. Identifies overconfidence (stated 0.95 above observed 0.80) and says it appears as a reliability diagram point below the diagonal at high confidence.
2. Describes temperature scaling as dividing logits by one parameter T fitted on held-out data (typically minimizing log loss), with T > 1 softening probabilities toward 0.5.
3. Computes the example: sigma(3) is about 0.953, sigma(1.5) with T = 2 is about 0.818, and T of about 2.16 gives 0.80.
4. Explains that dividing by T preserves the ordering of cases, so AUC and the predictions at a 0.5 cutoff (hence accuracy at 0.5) are unchanged and only the stated confidence is rescaled.
5. States the limits: it fits average calibration on the data it was fitted on; one parameter cannot fix class-specific or subgroup miscalibration or a shifted population; it must be fitted on data separate from the evaluation set and rechecked over time.

**Source:** Calibration

## ES-ch02.12

A hospital can follow up flagged patients at $20 each. A missed positive costs $400. A model sorts 1,000 patients into three groups with calibrated probabilities: group 1 has 700 patients with positive rate 0.01, group 2 has 200 patients with positive rate 0.06, and group 3 has 100 patients with positive rate 0.30. (a) Derive the probability cutoff that minimizes expected cost. (b) Compute the expected total cost per 1,000 patients of four policies: follow up nobody, follow up group 3 only, follow up groups 2 and 3, and follow up everyone. (c) Explain why a 0.5 cutoff is the wrong choice here. (d) Suppose group 2's true positive rate is actually 0.03 although the model still reports 0.06. What is the consequence, and what does it show about the role of calibration?

**Points:** 5

**Rubric (1 point each):**

1. Derives the cutoff: follow up when the expected cost of missing, 400p, exceeds the follow-up cost 20, so p > 20 / 420, about 0.048.
2. Computes the costs: nobody $19,600, group 3 only $9,600, groups 2 and 3 $8,800, everyone $20,000, so following up groups 2 and 3 is best.
3. Explains that no group has a probability above 0.5, so a 0.5 cutoff follows up nobody and costs $19,600, more than double the optimum, because a criterion that counts errors equally ignores that a miss costs twenty times a follow-up.
4. Shows the effect of miscalibration: with group 2's true rate at 0.03, following up groups 2 and 3 costs $8,800 while following up group 3 alone costs $7,200, a waste of $1,600 (about 22%), so a cost-derived cutoff is only valid if the stated probabilities equal true frequencies.
5. Notes that the cutoff and the best policy move with the cost ratio and the base rate, so costs and prevalence should be examined for uncertainty and calibration rechecked on deployment data and by subgroup.

**Source:** Synthesis — four questions that prevent most deployment disasters

## ES-ch02.13

A screening classifier was validated at a prevalence of 20% and found to have sensitivity 90% and specificity 90%. It is later deployed in a population where the prevalence is 2%; assume its sensitivity and specificity are unchanged in the new population. (a) Compute the share of flagged cases that are truly positive at each prevalence. (b) Explain what changed and what did not, and whether the model got worse. (c) Explain why the model's own output scores would not alert anyone to the problem. (d) Describe the kinds of shift that can occur and a monitoring plan that would catch them, relating this to the general limits of relying on a past track record.

**Points:** 5

**Rubric (1 point each):**

1. Computes about 0.69 at 20% prevalence (per 1,000 cases: 180 true positives and 80 false positives) and about 0.155 at 2% (18 true positives and 98 false positives).
2. Explains that, with sensitivity and specificity unchanged, only the prior changed, so the model did not degrade as a classifier but its flags are now mostly false, and any probability score tied to the old prior is now too high.
3. Explains that a score is computed from the inputs under assumptions learned in training and does not itself register a change in the population, so scores and dashboards can look unchanged while real-world performance falls.
4. Names kinds of shift with an example of each, such as prior (base-rate) shift, covariate shift in the inputs, concept drift in the relationship between inputs and outcomes, and changes in how measurements are made.
5. Proposes monitoring: track realized outcomes on a labeled sample, watch input distributions, recompute calibration and the share of flags that are real over time, recalibrate or re-weight priors, and state the conditions a track record depended on, since past performance supports predictions only while those conditions hold.

**Source:** Hume's induction problem, re-translated as distribution shift

## ES-ch02.14

An autonomous agent ends each task by reporting "complete". In the current task mix, 70% of tasks truly succeed. The agent reports "complete" on 98% of the tasks that succeed and on 60% of the tasks that fail. (a) Given that the agent reports "complete", what is the probability that the task actually succeeded? (b) How does the answer change on a harder task mix in which only 30% of tasks succeed? (c) What would the agent's false-"complete" rate on failed tasks need to be for the report to be strong evidence of success, say above 95% at the 70% base rate? (d) How would you measure these quantities in practice?

**Points:** 5

**Rubric (1 point each):**

1. Applies Bayes' rule: 0.7 x 0.98 / (0.7 x 0.98 + 0.3 x 0.6) = 0.686 / 0.866, about 0.79.
2. Interprets the likelihood ratio 0.98 / 0.6, about 1.6: the report moves belief only from 0.70 to 0.79 because failed tasks also end with "complete", so the report is weak evidence of success.
3. Shows the dependence on the base rate: with 30% of tasks succeeding the same report gives only about 0.41, so the report should not be trusted on hard tasks.
4. Shows what makes a report informative: the false-"complete" rate would need to fall to about 12% or lower to exceed 95% (at 10% the probability is about 0.96), meaning the report must distinguish success from failure.
5. Describes measurement: check outcomes independently of the agent's report on a sample, estimate both conditional rates including the rate on failures, give intervals for them, and stratify by task difficulty and by number of steps.

**Source:** Bayes' theorem

## ES-ch02.15

A deployed model's mistakes have this cost distribution: 99.9% of mistakes cost $1 and 0.1% cost $5,000, independently of each other. An audit samples 500 mistakes, finds that every one cost $1, and reports: "average cost per mistake is $1.00 with no variation, so our estimate is precise." (a) Compute the true mean cost and the probability that a 500-mistake audit shows no catastrophic mistake. (b) Explain what is wrong with the team's confidence, and what the central limit theorem does and does not guarantee here. (c) What should the team report instead? Include the bound on the catastrophic-mistake rate that 0 events in 500 supports.

**Points:** 5

**Rubric (1 point each):**

1. Computes the true mean as about $6.00 (0.999 x $1 + 0.001 x $5,000) and the probability of no $5,000 mistake in 500 as 0.999 to the power 500, about 0.61 (the expected number of catastrophic mistakes is only 0.5).
2. Explains that a sample with no variation gives a zero-width interval, but the absence of rare events in a sample is not their absence in the population, so the apparent precision is an artifact.
3. States that the central limit theorem needs independent observations with finite variance, and that convergence to normality can be very slow when rare large values dominate the mean, so the sample must be large relative to 1 divided by the rare event's probability (here about 1,000 or more).
4. Gives the bound: 0 events in 500 supports only an upper limit of about 3/500 = 0.6% (about 95% confidence) on the catastrophic rate, six times the true 0.1% rate, which would correspond to an expected cost near $30 per mistake.
5. Recommends tail-aware reporting and design: report the frequency and size of the largest losses and high quantiles rather than only the mean, use scenario or worst-case analysis, and use targeted or stratified sampling and adversarial testing to find rare severe cases.

**Source:** When the Central Limit Theorem politely declines to help
