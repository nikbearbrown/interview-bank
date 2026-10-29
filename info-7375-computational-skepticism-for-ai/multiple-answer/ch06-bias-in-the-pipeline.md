# Chapter 6: Bias, where it enters and who is responsible

## MA-ch06.1

A city wants to know what share of its residents support a transit levy. The true share is 54%: 40% of residents have a landline and 75% of them support the levy, while the other 60% have no landline and 40% of them support it. A survey firm draws a simple random sample of landline numbers only and reports the sample proportion. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding a random sample of residents without landlines and weighting the two groups 40% and 60% would give an estimate centred on 54%.
- [ ] B. The sample proportion has an expected value of 75%, so its bias is about +21 percentage points whatever the sample size.
- [ ] C. Giving the landline respondents a weight so that they count as 40% of the total repairs the estimate, because the weighted sample then matches the population's landline share.
- [ ] D. Raising the sample from 1,000 to 100,000 respondents cuts the standard error about tenfold (1.4 points to 0.14) but leaves the expected estimate at 75%.
- [ ] E. With 100,000 respondents the estimate will very likely land within one point of the true 54%, because sampling error becomes tiny.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The weights 0.4 x 75% + 0.6 x 40% give 54%, and this works only because both strata now have respondents.
- B: Only landline households can be sampled, so the expected value is their 75% support, 21 points above the 54% truth, and that offset belongs to the procedure rather than to n.
- C: With no non-landline respondents there is only one stratum to weight, so the weights cancel and the estimate stays at 75%.
- D: Standard error scales with 1/sqrt(n), so a hundredfold larger sample shrinks it tenfold, while the systematic offset is untouched.
- E: The estimate concentrates ever more tightly around 75%, not around 54%.

**Source:** What "bias" actually means

## MA-ch06.2

A hospital builds a sepsis alert from 10,000 admissions. At triage 2,000 patients are classed unstable (30% develop sepsis) and 8,000 stable (5% develop sepsis), so overall prevalence is 10%. The training data keep only patients who had a lab panel in the first six hours, which happened for 90% of stable and 20% of unstable patients. The triage class is recorded for every patient. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Weighting each retained patient by 1 divided by the probability of being retained given triage class recovers a prevalence of 10%.
- [ ] B. The same weighting would still work if retention depended on an unrecorded clinician hunch that is related to sepsis.
- [ ] C. Collecting ten times as many admissions under the same lab rule would bring the training prevalence close to 10%.
- [ ] D. The 6.3% training prevalence is the right baseline for calibrating risk scores for all admitted patients.
- [ ] E. Sepsis prevalence in the training data is about 6.3%, well below the true 10%.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Weights of 1/0.9 and 1/0.2 restore each class to its population size, giving (400 + 600) / (8,000 + 2,000) = 10%.
- B: Weighting needs a recorded variable that explains who was kept, and an unrecorded hunch gives nothing to weight on.
- C: The same retention rule yields the same skewed mix at any volume, so more data reproduces 6.3% with a smaller standard error.
- D: Deployment sees all admissions, whose true prevalence is 10%, so a baseline taken from the filtered sample is miscalibrated for them.
- E: The sample has 480 sepsis cases among 7,600 patients, which is 6.3%, because unstable patients are retained at a much lower rate.

**Source:** Ten mechanisms, distinguished

## MA-ch06.3

A lender deletes the column "group" (a protected attribute) from its training table but keeps "neighbourhood". The table covers 1,000 applicants, half living in neighbourhood N1 and half in N2. In N1, 90% of applicants belong to group B; in N2, 10% do. A manager says the model "cannot treat the groups differently, because it never sees group". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A feature that predicts group is, for that reason alone, being used unfairly, whatever else it tells the model about the outcome.
- [ ] B. Dropping neighbourhood as well guarantees that no remaining column carries information about group, since the model has nothing left to infer it from.
- [ ] C. Because the model never sees group, any difference between groups in its approval rates must reflect differences in applicants' true creditworthiness.
- [ ] D. Guessing group from neighbourhood alone would be right for 90% of applicants, against 50% for a coin flip.
- [ ] E. Auditing outcomes by group requires group labels in the audit data even though the model does not take them as input.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: A feature can predict group and also carry legitimate information about the outcome, so unfair use has to be shown by its effects rather than inferred from correlation.
- B: Other columns such as employer, school, purchase history or name can also correlate with group, so removing one proxy does not remove the signal.
- C: The model can recover much of group from neighbourhood, and the outcomes it learns from can carry group-linked patterns, so outcome differences need not reflect creditworthiness.
- D: Of 1,000 applicants, 450 + 450 are classified correctly, so neighbourhood alone recovers most of the group signal.
- E: Without recorded group membership there is no way to compute outcome rates by group, so deleting the field also removes the ability to detect disparities.

**Source:** Leverage analysis — finding the high-leverage intervention point

## MA-ch06.4

A screening model advances 240 of 400 applicants from group A (60%) and 120 of 300 applicants from group B (40%). A reviewer divides the lower selection rate by the higher one and compares the result with 0.8, the benchmark in a common US employment-selection screening heuristic known as the four-fifths rule. A two-proportion z-test on these counts gives z of about 5.2. For reference, if group B had only 20 applicants with 8 advanced (also 40%), the same test would give z of about 1.8, below the 1.96 needed for significance at the 5% level. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A ratio below 0.8 proves that the model uses group membership in its decisions, since the benchmark exists to detect that.
- [ ] B. A z of about 5.2 means chance variation in who happened to apply is an unlikely explanation for a gap this large.
- [ ] C. The ratio of the selection rates is about 0.67, which falls below the 0.8 benchmark.
- [ ] D. A ratio above 0.8 would show that the screening process is free of group-related disadvantage for every subgroup of applicants.
- [ ] E. With 20 group B applicants and the same 40% rate, the ratio stays 0.67 but is much weaker evidence of a real gap.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The ratio is descriptive; a gap can arise from differences between applicant pools, proxies or other causes, and says nothing by itself about whether group is used.
- B: The two-sided p-value is on the order of 10^-7, so sampling noise alone rarely produces such a gap if the underlying rates were equal.
- C: 40% divided by 60% is 0.667.
- D: The benchmark is a screening heuristic on aggregate rates; a ratio above it can coexist with disadvantage hidden in subgroups.
- E: Fewer applicants widen sampling variability, so the same ratio can fall within chance.

**Source:** Ten mechanisms, distinguished

## MA-ch06.5

An audit finds that a loan model approves 62% of group X applicants and 48% of group Y applicants. The auditors want to learn which part of the pipeline produced the 14-point gap. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Matching applicants on every observed covariate removes the influence of unobserved differences between the groups.
- [ ] B. Comparing approval rates among applicants with similar income and credit history shows whether the gap persists among comparable applicants.
- [ ] C. Re-running the model with one input held constant and measuring the change in the gap shows how much of it depends on that input.
- [ ] D. A statistically significant 14-point gap is enough on its own to identify which stage of the pipeline produced it.
- [ ] E. If the gap disappears after conditioning on a variable such as job tenure, the decision process must have treated the groups equally.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Matching balances only what was measured, and unmeasured factors can still differ and drive the gap.
- B: Stratifying on legitimate covariates is the standard first test of whether differences in qualifications account for a gap.
- C: An ablation intervenes on one component and attributes the change in the output gap to it, which narrows the candidate causes.
- D: Significance says the gap is unlikely to be noise; it does not say whether data, labels, features, model, cutoff or review produced it.
- E: The conditioning variable may itself be shaped by group, for example through earlier unequal treatment, so the gap vanishing shows only that it runs through that variable.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.6

A company advanced candidates from two groups into interviews for two roles. For role X, group A had 20 of 100 candidates advance and group B had 100 of 400. For role Y, group A had 240 of 400 advance and group B had 70 of 100. Overall, 260 of 500 group A candidates (52%) and 170 of 500 group B candidates (34%) advanced. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reversal arises because most group B candidates applied to the low-rate role while most group A candidates applied to the high-rate role.
- [ ] B. Applying the same 50/50 role mix to both groups gives about 47.5% for group B and 40% for group A.
- [ ] C. The overall rates are the correct basis for comparing the groups, since they include every candidate.
- [ ] D. The pattern cannot occur with correct counts, because a group that leads in every role must also lead overall.
- [ ] E. Group B has the higher advance rate in each role, yet group A has the higher rate overall.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Group B has 400 of its 500 candidates in role X (a 25% rate) while group A has 400 of its 500 in role Y (60%), and the overall rate is a mix-weighted average.
- B: Standardizing gives B = 0.5 x 25% + 0.5 x 70% = 47.5% and A = 0.5 x 20% + 0.5 x 60% = 40%.
- C: Which comparison is appropriate depends on the causal question, and the overall figure mixes the groups' different role choices with the process's treatment of them.
- D: A reversal is arithmetically routine when groups apply to roles in different proportions; here B leads 25% to 20% in role X and 70% to 60% in role Y.
- E: Role X is 25% against 20%, role Y is 70% against 60%, and overall it is 34% against 52%.

**Source:** How bias types compound

## MA-ch06.7

In hospital records, patients given a new drug recovered at a lower overall rate than untreated patients (66% against 76%), yet the drug group did better within each severity level: mild 90% against 85%, severe 60% against 40%. Of the 200 mild patients, 40 received the drug; of the 200 severe patients, 160 did. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Standardizing both groups to a 50/50 severity mix gives 75% recovery with the drug and 62.5% without.
- [ ] B. Stratifying on blood pressure measured after dosing would remove part of the drug's effect if the drug works partly by lowering it.
- [ ] C. Assigning the drug at random would break the link between severity and treatment, removing that distortion from the overall comparison.
- [ ] D. Whenever a reversal like this appears, the stratified table is the correct one, whatever the causal relationships among the variables.
- [ ] E. Severity influences both who receives the drug and who recovers, which makes it a confounder of the overall comparison.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Drug: 0.5 x 90% + 0.5 x 60% = 75%; no drug: 0.5 x 85% + 0.5 x 40% = 62.5%.
- B: Conditioning on a post-treatment mediator blocks a path along which the treatment effect travels.
- C: Randomization makes treatment independent of severity and of other prior factors, measured or not, in expectation.
- D: A variable that is a consequence of the treatment (a mediator) or a collider can distort a stratified comparison, so the right table depends on the causal structure.
- E: Doctors gave the drug mostly to severe patients, who recover less often, so the drug group's overall rate is dragged down.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.8

A classifier is tested on 10,000 images: 9,500 from group A, on which accuracy is 95%, and 500 from group B, on which accuracy is 70%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Pooled accuracy equals the simple average of the two group accuracies, 82.5%.
- [ ] B. Group B's error rate is about three times group A's.
- [ ] C. Pooled accuracy on the test set is 93.75%.
- [ ] D. A pooled accuracy of 93.75% implies that every group's accuracy is at least 93.75%.
- [ ] E. Pooled accuracy would still exceed 90% if the classifier were wrong on every group B image.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It is an average weighted by group size, so the large group dominates.
- B: 30% against 5% is a factor of six.
- C: (9,500 x 0.95 + 500 x 0.70) / 10,000 = 9,375 / 10,000.
- D: A pooled figure is an average, so one group can sit well below it when another sits above it.
- E: 9,025 correct out of 10,000 is 90.25%.

**Source:** How bias types compound

## MA-ch06.9

On a test set, group A has 2,000 examples with 160 errors (8.0%) and group B has 40 examples with 6 errors (15.0%). A 95% Wilson interval for group B's error rate runs from about 7.1% to 29.1%, and a Fisher exact test of the difference between the two error rates gives p = 0.13. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because 15% is higher than 8%, the model is worse on group B than on group A.
- [ ] B. The non-significant test shows that the two groups have the same error rate.
- [ ] C. Group B's interval includes group A's observed 8.0%, so these data do not rule out equal error rates.
- [ ] D. Collecting 160 group B examples that also show a 15% error rate would leave the interval about as wide as it is now.
- [ ] E. Merging group B into one pool with group A and reporting a single error rate of about 8.1% settles the uncertainty about group B.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: With only 40 examples the observed difference is compatible with chance, so the point estimate alone does not establish a higher error rate.
- B: Failing to reject is not evidence of equality; with 40 examples the test has little power to detect even sizeable differences.
- C: 8.0% lies between 7.1% and 29.1%.
- D: Quadrupling n roughly halves the width of an interval for a proportion.
- E: Pooling averages group B into a figure dominated by group A and hides exactly the subgroup in question.

**Source:** How bias types compound

## MA-ch06.10

An auditor tests a model for an error-rate gap in each of 20 independent subgroups, using a 5% significance level for every test. Suppose the model truly performs identically in all 20 subgroups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If no subgroup is flagged, the model is shown to perform equally well in all of them.
- [ ] B. The expected number of subgroups flagged by chance is 1.
- [ ] C. A subgroup found by searching through many possible splits after seeing the data is weaker evidence of a real gap than one chosen in advance.
- [ ] D. The probability that at least one subgroup is flagged by chance is 5%, since each test has a 5% false-flag rate.
- [ ] E. The probability that at least one subgroup is flagged by chance is about 64%.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A null result may reflect low power in small subgroups, which is not evidence of equality.
- B: Twenty tests at a 5% rate give 20 x 0.05 = 1.
- C: Post hoc searching multiplies the number of implicit tests and inflates false findings.
- D: The 5% applies per test; across 20 independent tests the chance of at least one false flag is much larger.
- E: One minus 0.95 raised to the 20th power is 0.64.

**Source:** How bias types compound

## MA-ch06.11

A face-attribute classifier is tested on 2,000 images, with 500 images in each combination of gender (men, women) and skin tone (lighter, darker). The error counts out of 500 are: lighter-skinned men 5, darker-skinned men 105, lighter-skinned women 55, darker-skinned women 55. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An audit by gender alone would report an 11% error rate for men and 11% for women.
- [ ] B. The error rate for darker-skinned men is 21%, which is 21 times the 1% rate for lighter-skinned men.
- [ ] C. With 10 binary attributes there are about 100 intersectional subgroups to evaluate.
- [ ] D. Because error rates are equal across men and across women, error rates must also be equal across the four combinations.
- [ ] E. When an intersectional cell has too few examples to estimate error precisely, that cell should be dropped from the audit.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Men have 110 errors in 1,000 images and women have 110 errors in 1,000 images.
- B: 105/500 = 21% and 5/500 = 1%.
- C: There are 2^10 = 1,024 combinations, and the number grows multiplicatively with each added attribute.
- D: The marginal equality masks wide cell-level differences, from 1% to 21%.
- E: Dropping it hides subgroups that may be most affected; the right response is to report the wide uncertainty or to collect more data.

**Source:** How bias types compound

## MA-ch06.12

Two neighbourhoods, X and Y, each have 10,000 residents, and in each of them 10% commit an offence in a given year. Police patrol X heavily, so 60% of offences there lead to an arrest; in Y only 30% do. A team trains a model to predict "arrested in the next year" from past records. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Recorded arrest rates are 6% in X and 3% in Y even though offending rates are equal.
- [ ] B. A model that is calibrated to the arrest label will, on average, score residents of X about twice as high as residents of Y.
- [ ] C. Adding more years of arrest records produced by the same patrol pattern would shrink the gap between X and Y.
- [ ] D. High accuracy at predicting arrests shows that the model identifies offenders equally well in both neighbourhoods.
- [ ] E. Using victim-reported offences as the outcome, which depends less on patrol patterns, could reduce the distortion but has its own reporting biases.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: 10% x 60% = 6% and 10% x 30% = 3%.
- B: The base rate of the arrest label is 6% against 3%, a ratio of two.
- C: More records from the same process estimate the same distorted rates more precisely; the offset remains.
- D: Accuracy is measured against the arrest label, and that label's relationship to offending differs by neighbourhood.
- E: Changing the label to a measure less tied to enforcement intensity reduces dependence on patrol patterns.

**Source:** The dataset as epistemic artifact

## MA-ch06.13

A hospital program enrols patients whose predicted annual cost is at least 7 units, as a stand-in for health need. Need is spread evenly across levels 1 to 10 in two groups of equal size. Group A faces no access barriers, so cost equals need; group B faces barriers, so cost is 0.7 times need. The model predicts cost perfectly for everyone. "High need" means level 7 or above. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. All of group A's high-need patients are enrolled, compared with a quarter of group B's.
- [ ] B. The disparity arises because the model predicts cost less accurately for group B than for group A.
- [ ] C. Deleting the group indicator from the model's features would equalize enrolment of high-need patients.
- [ ] D. Replacing the label with a direct clinical measure of need would target the intended construct, though it may carry its own distortions.
- [ ] E. Because cost is predicted accurately, it is a valid measure of health need for both groups.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Group A levels 7 to 10 cost 7 to 10 and are all enrolled; in group B only level 10 reaches a cost of 7.
- B: The model is assumed perfect; the problem is that cost measures need differently in the two groups.
- C: Enrolment follows predicted cost, and cost itself understates group B's need, so removing the group column does not change what the label measures.
- D: The mismatch is between the label and the construct, and a measure closer to the construct reduces it.
- E: Predictive accuracy for a label says nothing about whether the label measures the construct of interest.

**Source:** Three flavors of bias, mapped to the ten types

## MA-ch06.14

A lender approved 4,000 of 10,000 applicants under its scoring policy; 200 of the approved applicants defaulted (5.0%). As an experiment, it approved a random sample of 200 of the 6,000 denied applicants, and 24 of them defaulted (12.0%, with a margin of about 4.5 points either side). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Under the original policy the default outcome of a denied applicant is never observed, because no loan is issued.
- [ ] B. Training a new model on approved applicants only and testing it on held-out approved applicants gives an unbiased estimate of its performance on the full pool.
- [ ] C. The 5.0% default rate among approved applicants is the default rate for the whole applicant pool.
- [ ] D. Because the denied applicants were chosen by the old policy, a random sample of them cannot be representative of the denied group.
- [ ] E. Combining the approved group's rate with the experimental estimate for denied applicants suggests that about 9.2% of the whole pool would default.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Outcomes exist only for those who receive the favourable decision, so labels are selectively observed.
- B: Training and test data both come from the selected subgroup, so the estimate says nothing reliable about the denied region.
- C: The approved group was selected by the score and contains the applicants least likely to default.
- D: A random draw from the denied group represents that group, whatever process put its members there.
- E: (200 + 0.12 x 6,000) / 10,000 = 9.2%.

**Source:** Ten mechanisms, distinguished

## MA-ch06.15

Two districts have the same true incident rate. Each cycle, 1,000 patrol hours are divided between them, and the number of incidents recorded in a district is proportional to the patrol hours it receives. The first cycle splits hours 600 and 400 between districts 1 and 2. In every later cycle hours are split in proportion to the incidents recorded in the previous cycle. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Each district's recorded count is an unbiased estimate of its true incident rate, because the counts come from real events.
- [ ] B. Setting aside some patrol hours for randomly chosen districts, or measuring incidents independently of patrol presence, would let the data reveal the equal rates.
- [ ] C. If all hours instead go to the district with more recorded incidents each cycle, district 2 records zero incidents from the second cycle on.
- [ ] D. Under this rule the split stays at 600 and 400 in every cycle, although the true rates are equal.
- [ ] E. Given enough cycles, the recorded counts will converge to equal as the system accumulates more and more data.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The counts depend on how many incidents are observed, which depends on patrol hours, so they favour the heavily patrolled district.
- B: Random or independent measurement breaks the link between past records and where observation happens.
- C: With no patrol hours no incidents are recorded there, and the data then appear to confirm that district 2 has none.
- D: Recorded incidents are proportional to patrol hours, so allocating in proportion to records reproduces the same shares.
- E: The records reflect where patrols went rather than where incidents occur, so the 60/40 split is a fixed point that never corrects.

**Source:** Leverage analysis — finding the high-leverage intervention point

## MA-ch06.16

A training set has 1,000 examples: group A has 360 positive and 240 negative labels, and group B has 120 positive and 280 negative labels. A reweighing scheme gives each combination of group and label the weight P(group) x P(label) / P(group and label), where each P is the share of the training set. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Training on the reweighted data guarantees equal selection rates for the two groups on new data.
- [ ] B. Group B's positive examples each count 1.6 times as much as an average example.
- [ ] C. After weighting, the positive-label rate is 48% in both groups.
- [ ] D. Reweighing addresses the association between group and label in the training sample, not whether each individual's label is accurate.
- [ ] E. Computing the weights requires knowing each training example's group, even if the group is never given to the model as an input.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Weights make group and label independent in the training sample; the learned model's predictions on new data can still differ by group.
- B: P(B) x P(positive) / P(B and positive) = 0.4 x 0.48 / 0.12 = 1.6.
- C: Group A gives 288 / (288 + 312) = 0.48 and group B gives 192 / (192 + 208) = 0.48.
- D: Weights change how much each row counts, while the label on each row remains as recorded.
- E: The weights depend on P(group), so group membership must be recorded for the training rows even when the model never uses it as a feature.

**Source:** Ten mechanisms, distinguished

## MA-ch06.17

Two groups of 1,000 applicants each receive integer scores from 1 to 5 from a model. Counts at scores 1 to 5 are 100, 200, 300, 250, 150 for group A and 300, 300, 200, 150, 50 for group B. Under a single cutoff, applicants scoring 4 or 5 are selected. A proposal would instead select scores 4 and 5 in group A and scores 3, 4 and 5 in group B. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If group B's lower scores reflect biased labels, the proposal equalizes selection rates without making the scores a valid measure.
- [ ] B. The proposal changes the scores the model assigns to each applicant, because the cutoffs are part of the scoring.
- [ ] C. Under the proposal both groups have a 40% selection rate, yet a group B applicant scoring 3 is selected and a group A applicant scoring 3 is not.
- [ ] D. Under the single cutoff, 40% of group A and 20% of group B are selected.
- [ ] E. The proposal can be carried out without knowing an applicant's group at decision time, since the scores already encode it.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Post-processing acts on outputs and leaves the learned score relationships, and any bias in them, in place.
- B: Only the cutoff applied to the scores changes; the scores themselves are untouched.
- C: Group B selects 200 + 150 + 50 = 400, and group A at score 3 falls below its cutoff.
- D: Group A has 250 + 150 = 400 selected and group B has 150 + 50 = 200.
- E: A different cutoff for each group requires knowing which group an applicant belongs to when deciding.

**Source:** The dataset as epistemic artifact

## MA-ch06.18

A résumé-ranking model trained on a firm's past hiring decisions selects group B candidates less often than group A candidates with the same measured experience. The team considers reweighing the training data, adding a fairness penalty to the training loss, setting score cutoffs separately by group, and changing how human reviewers use the ranking. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reweighing the training data guarantees equal selection rates in the final decisions, whatever happens after training.
- [ ] B. If most of the disparity arises when reviewers override the model's rankings, changes to the training data will remove most of it.
- [ ] C. A drop in agreement with the historical hiring decisions after mitigation shows that the mitigated model has become worse at identifying strong candidates.
- [ ] D. Setting cutoffs by group leaves what the model learned from past decisions unchanged and changes only how scores are acted on.
- [ ] E. A mitigation applied at one stage of the pipeline makes checks at the later stages unnecessary once it has been validated.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It adjusts the training sample only; cutoffs, reviewers and the learner's behaviour can still produce unequal rates.
- B: A disparity created at review lies outside the reach of the training data.
- C: The historical decisions are the thing under suspicion, so lower agreement with them can reflect less copying of past skew rather than lower quality.
- D: Post-processing modifies decisions, not the learned scores.
- E: Disparity can enter or return at later stages such as cutoffs and review, so each stage needs its own check.

**Source:** Leverage analysis — finding the high-leverage intervention point

## MA-ch06.19

A bank buys a credit-risk model from a vendor. The vendor trained it on records bought from a data broker, with "repaid" and "defaulted" labels taken from another lender's earlier approval history. The bank chooses the approval cutoff and sends borderline cases to loan officers. An audit finds a large approval gap between two groups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Buying the model from a vendor moves responsibility for the outcomes of the bank's lending decisions to the vendor.
- [ ] B. Tracing the largest source of disparity to its step and naming who controls it lets the fix be directed to someone able to make it.
- [ ] C. The vendor should be held accountable for documenting what the training data contain and what the model has and has not been validated for.
- [ ] D. The bank is accountable for its choice of cutoff and for how loan officers use the model's output, because it controls those steps.
- [ ] E. Assigning accountability for a disparity requires identifying an individual engineer who intended harm or acted negligently.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The bank makes the lending decisions and cannot contract away accountability for them.
- B: Remedies fail when aimed at a party with no control over the step where the disparity is created.
- C: A deployer cannot judge fitness for use without this information from the party that built the model.
- D: Accountability tracks control: the party that can change a decision point owns the consequences of how it is set.
- E: Accountability can be assigned to roles and organizations that control a step in the pipeline, with no finding of intent.

**Source:** A limit case: when the leverage is upstream of your pipeline — and who owns it then

## MA-ch06.20

A datasheet for a dataset records how and why data were collected, who is and is not represented, how labels were produced, and recommended uses. A model card states a model's intended uses, its evaluation data, and its performance broken down by relevant subgroups. An external audit is an evaluation by a party independent of the developer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A datasheet's account of how labels were produced lets a team judge whether they measure what the model is meant to predict.
- [ ] B. Publishing a model card that lists the model's metrics shows that the model is fair to the groups it will affect.
- [ ] C. A model card reporting subgroup performance with confidence intervals shows where the model is weaker and how well that is known.
- [ ] D. An external audit is more informative when the auditor can access the model and data and reproduce the reported numbers.
- [ ] E. Stating which uses are out of scope lets reviewers judge whether a deployment went beyond what the developer evaluated.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Label provenance is key evidence on whether the target is a valid measure.
- B: A model card is a disclosure; it can report poor subgroup performance and does not by itself make the model fair or its contents correct.
- C: Disaggregated metrics and their uncertainty make weaknesses and data limits inspectable.
- D: Independence plus reproducibility lets an audit check claims instead of accepting them.
- E: An explicit scope statement turns a vague expectation into something a deployment can be checked against.

**Source:** A limit case: when the leverage is upstream of your pipeline — and who owns it then

## MA-ch06.21

A model is evaluated on a benchmark that is 90% group A and 10% group B, with accuracy of 95% on group A and 75% on group B. It will be deployed on a population that is 50% group A and 50% group B. Assume each group's accuracy in deployment equals its benchmark accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy on the benchmark is 93%.
- [ ] B. Expected accuracy in deployment is also 93%, because each group's accuracy is unchanged.
- [ ] C. Weighting each group's benchmark accuracy by its deployment share predicts about 85% accuracy without any new data.
- [ ] D. Doubling the benchmark's size while keeping its 90/10 composition would reveal the mismatch with deployment.
- [ ] E. A reported accuracy figure is a property of the model alone and does not depend on who is tested.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: 0.9 x 95% + 0.1 x 75% = 93%.
- B: Overall accuracy depends on the mix of groups tested, and the mix changed.
- C: 0.5 x 95% + 0.5 x 75% = 85%.
- D: A larger sample of the same composition narrows noise but cannot show how the model does on a different mix.
- E: It describes the model's performance on a particular population.

**Source:** How bias types compound

## MA-ch06.22

Outcome y depends on a feature x differently in two groups. In group A, y = 2x. In group B, y = 2x + 6. Each group has 11 points, with x = 0, 1, ..., 10. A single least-squares line is fitted to all 22 points; it comes out as y = 2x + 3, with R-squared of about 0.82. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A misfit of this kind arises only when one group is much larger than the other.
- [ ] B. Collecting many more points from the same two groups will move the pooled intercept to the correct value for both.
- [ ] C. An R-squared of 0.82 shows that the pooled line fits each group well.
- [ ] D. Because the mean residual over all 22 points is zero, residual diagnostics on the pooled data cannot reveal a group-specific misfit.
- [ ] E. The pooled line overpredicts every group A case by 3 and underpredicts every group B case by 3.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Here the groups are equal in size and the pooled line still misfits both.
- B: More data from the same groups estimates the same compromise line more precisely; no single intercept fits both.
- C: R-squared summarizes the pooled fit; every point here misses by 3, and the shared slope hides the group-specific offset.
- D: Residuals split by group show a consistent -3 for group A and +3 for group B.
- E: At any x the line gives 2x + 3, while group A's true value is 2x and group B's is 2x + 6.

**Source:** How bias types compound

## MA-ch06.23

A screening device reads each person's true value plus Gaussian noise. True values are 6 for people who have a condition and 4 for people who do not; half of each group has the condition. A reading above 5 is classified as positive. The noise standard deviation is 1 for group A and 2 for group B. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The gap shows that the classifier learned a group-specific decision rule from the training examples.
- [ ] B. Applying the same cutoff to both groups is consistent with unequal error rates, so identical rules need not mean identical error burdens.
- [ ] C. Accuracy is about 84% for group A and about 69% for group B, although the same rule classifies both.
- [ ] D. Collecting more labelled training rows measured with the same device would be expected to remove the gap.
- [ ] E. The false-negative rate is about 16% for group A and about 31% for group B.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A single cutoff is applied to everyone; the difference comes from measurement noise.
- B: The cutoff is the same but the noisier measurement makes errors more frequent in group B.
- C: Accuracy is one minus the error rate, 1 - 0.159 and 1 - 0.309.
- D: More rows from the same noisy instrument leave each reading just as noisy; improving the measurement or accounting for the noise is what helps.
- E: A positive person is missed when the noise pushes the reading to 5 or below, which has probability 0.159 for sd 1 and 0.309 for sd 2.

**Source:** Three flavors of bias, mapped to the ten types

## MA-ch06.24

A classifier has a true positive rate of 80% and a false positive rate of 20% in each of two groups. The share of truly positive people (the base rate) is 30% in group 1 and 50% in group 2. Positive predictive value (PPV) is the share of flagged people who are truly positive. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. PPV is about 63% in group 1 and 80% in group 2.
- [ ] B. If both groups had the same 40% base rate, the same error rates would give both groups a PPV of about 73%.
- [ ] C. For a classifier with the same true positive rate and the same nonzero false positive rate in two groups, PPV is higher in the group with the higher base rate.
- [ ] D. The PPV gap shows that the classifier is being applied incorrectly in the group with the lower base rate.
- [ ] E. Group 1's flagging rule could be changed so that its PPV rises to group 2's 80% while its true and false positive rates stay equal to group 2's.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Group 1 gives 0.24 / (0.24 + 0.14) = 0.63 and group 2 gives 0.40 / (0.40 + 0.10) = 0.80.
- B: 0.32 / (0.32 + 0.12) = 0.727.
- C: PPV = p x TPR / (p x TPR + (1 - p) x FPR), which increases with the base rate p when TPR and FPR are fixed and positive.
- D: The gap follows arithmetically from equal error rates and unequal base rates; no misapplication is needed.
- E: With rates held at 80% and 20%, group 1's PPV is fixed at 63% by its 30% base rate, so reaching 80% requires different error rates.

**Source:** The dataset as epistemic artifact

## MA-ch06.25

A model approves 30% of group A applicants and 18% of group B applicants, a 12-point gap. The same applicants are scored again with the postcode input replaced by a single constant value, and approval rates become 29% and 26%, a 3-point gap. Group membership is not an input to the model. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because group membership is not an input, the remaining 3-point gap must come from the model using group directly.
- [ ] B. Since the gap shrank, the original 12-point gap can be disregarded as an artifact of one feature and left out of the audit.
- [ ] C. The result shows that postcode causes group differences in approval outcomes in the real world, which is why the gap closed.
- [ ] D. Replacing postcode removed 9 of the 12 points, so most of the model's output disparity depends on that input.
- [ ] E. The test intervenes on a model input rather than on applicants' lives, so it speaks to how the model uses information.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Other inputs that correlate with group can carry the remaining gap.
- B: The gap is a real property of the model's decisions, and a feature that contributes to it is part of what needs explaining.
- C: The test intervenes on a model input; it shows how the model works and says nothing about why applicants in different groups differ.
- D: Three quarters of the gap, (12 - 3) / 12, vanished when the input was neutralized.
- E: It tests whether the output depends on one input, which is a statement about the model.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.26

Group A makes up 90% of the data and group B 10%. Three candidate models have error rates (group A, group B) of M1: 5%, 30%; M2: 6%, 20%; M3: 3%, 45%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Switching from M3 to M2 would raise the average error by more than one percentage point.
- [ ] B. Average error weights the two groups equally, whatever their share of the data.
- [ ] C. An objective that minimizes average error is neutral between the groups, because it applies one formula to everyone.
- [ ] D. Choosing the model with the lowest average error selects M3, which has the highest group B error rate of the three.
- [ ] E. M2 has both the lowest average error and the lowest worst-group error of the three models.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The increase is 0.2 points, from 7.2% to 7.4%.
- B: It weights each group by its share of the data, 90% and 10%.
- C: Errors on the larger group count nine times as much, so the objective favours performance there.
- D: Average errors are 7.5% for M1, 7.4% for M2 and 7.2% for M3.
- E: M2's worst-group error (20%) is the lowest, but its average (7.4%) is higher than M3's (7.2%).

**Source:** Leverage analysis — finding the high-leverage intervention point

## MA-ch06.27

A model flags 20% of applicants in each of two groups for adverse action, and a human reviewer then upholds 50% of the flags in group A and 80% in group B. The final adverse-action rate is the share of all applicants whose flag is upheld. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The gap in upheld rates may partly reflect real differences between the flagged cases, which should be examined before judging reviewers.
- [ ] B. The different upheld rates alone establish that reviewers are prejudiced against group B.
- [ ] C. Final adverse-action rates are 10% for group A and 16% for group B.
- [ ] D. Comparing the flag rate, upheld rate and final rate by group at each stage shows where the disparity arises.
- [ ] E. Equal flag rates for the two groups guarantee equal final outcomes for the two groups.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Without comparing like cases, rate differences cannot be attributed to reviewer behaviour.
- B: The flagged cases may differ in true risk, so the rates call for investigation but do not establish motive.
- C: 20% x 50% = 10% and 20% x 80% = 16%.
- D: A stage-by-stage breakdown localizes the step at which rates diverge.
- E: The review step can create or remove disparity after the model has produced equal flag rates.

**Source:** Leverage analysis — finding the high-leverage intervention point

## MA-ch06.28

A text-generating model screens résumés and answers "shortlist" or "reject" for each. Auditors build 200 pairs of résumés that are identical except for a first name signalling group A or group B. Each résumé was submitted once with the model's sampling randomness switched on, so repeating a submission could give a different answer. Results: shortlisted in both résumés of the pair, 90; in neither, 68; only the group A name, 30; only the group B name, 12. Shortlisting rates are 60% for group A names and 51% for group B names. An exact sign test on the 30 against 12 discordant pairs gives p of about 0.008. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The test result shows that the model was trained on discriminatory hiring data and learned to copy it.
- [ ] B. The 90 pairs shortlisted for both names and the 68 rejected for both add nothing to the comparison of the two names.
- [ ] C. Because each pair differs only in the name, differences in qualifications cannot explain the 30-to-12 split.
- [ ] D. Run-to-run randomness in the model's answers makes the 30-to-12 split uninterpretable as evidence.
- [ ] E. Because outputs vary between runs, repeating each pair several times would better estimate each name's shortlisting probability.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The test shows that outputs depend on the name; the origin of that dependence in training data, tuning or prompt is a separate question.
- B: Only the discordant pairs differ between the names, so only they enter the paired test.
- C: Matching by construction removes the qualification confounder within the tested résumés.
- D: Randomness is already part of the null distribution: with no name effect the 42 discordant pairs would split about evenly, and the test gives p of about 0.008.
- E: Repetitions average out sampling randomness within each pair.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.29

Two annotators label 100 clinical notes as positive or negative for a condition. Both say positive for 85 notes and both say negative for 5; each is alone in saying positive for 5 notes. Each annotator labels 90% of notes positive. Cohen's kappa is (observed agreement - chance agreement) / (1 - chance agreement). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Chance agreement is about 82%, which gives a kappa of about 0.44.
- [ ] B. Raw agreement is the better statistic here, because chance agreement is irrelevant when one category dominates.
- [ ] C. A high kappa shows that the labels measure the condition accurately, since the annotators agree on them.
- [ ] D. If kappa falls sharply once annotators are blinded to a patient's earlier diagnosis, the unblinded labels were probably shaped by it.
- [ ] E. Kappa is about 0.90, the same as the raw agreement, since kappa simply restates the share of matching labels.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Chance agreement is 0.9 x 0.9 + 0.1 x 0.1 = 0.82, so kappa = (0.90 - 0.82) / 0.18 = 0.44.
- B: Chance agreement is largest exactly when one category dominates, which is when raw agreement misleads.
- C: Annotators can agree with each other and still share the same systematic error, so agreement shows consistency rather than validity.
- D: Agreement that depends on seeing a cue indicates annotators are following the cue rather than assessing the note independently.
- E: Kappa corrects raw agreement for agreement expected by chance, and here that correction is large.

**Source:** Ten mechanisms, distinguished

## MA-ch06.30

A skin-lesion classifier has a 12% error rate on images of darker skin and 4% on lighter skin in a held-out test set labelled by the same process as the training data. Darker-skin images are 8% of the training set. A balanced audit set, labelled by an independent expert panel using biopsy results, shows the same 12% against 4% gap. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the audit labels came from an independent process, the gap is not an artifact of how the original test labels were made.
- [ ] B. Adding many more darker-skin images to the training set is certain to close the gap, as those images are the scarce input.
- [ ] C. The 8% share of darker-skin images establishes that under-representation is the cause of the gap.
- [ ] D. Because the audit labels were independent, differences in image quality between skin tones are ruled out as a cause.
- [ ] E. The persistence of the gap shows that the training labels were accurate for both skin tones.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The original test labels shared a source with the training labels and could share its errors, whereas independent labels remove that explanation for the measured gap.
- B: The gap may come from label quality or measurement differences that more images of the same kind would not change.
- C: Under-representation is consistent with the gap but has not been tested; label quality, image quality and lesion appearance could also contribute.
- D: Independent labelling does not control for how the images were captured, which can still differ by group.
- E: A model trained on skewed labels would also show a gap against correct labels, so the audit cannot distinguish that case from under-representation.

**Source:** Three flavors of bias, mapped to the ten types
