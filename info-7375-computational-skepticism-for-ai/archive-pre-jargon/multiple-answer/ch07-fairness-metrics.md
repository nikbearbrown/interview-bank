# Chapter 7: Fairness metrics

## MA-ch07.1

A binary classifier outputs a decision Ŷ (1 means the favorable decision) for people whose true outcome is Y (1 means the person actually qualifies). People belong to group a or group b. Check each statement that is true about standard group fairness criteria. Each statement is worth 1 point (5 points total).

- [ ] A. Predictive parity requires the precision of favorable decisions, P(Y=1 | Ŷ=1, group), to be equal across groups.
- [ ] B. Equalized odds requires both the true-positive rate and the false-positive rate to be equal across groups.
- [ ] C. Equal opportunity requires the false-positive rate, P(Ŷ=1 | Y=0, group), to be equal across groups, with no condition on people who qualify.
- [ ] D. Equalized odds implies equal opportunity, because equal true-positive rates are one of its two components.
- [ ] E. Demographic (statistical) parity requires P(Ŷ=1 | group) to be equal across groups, without conditioning on Y.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Predictive parity compares positive predictive value (precision) across groups.
- B: Equalized odds is the conjunction of true-positive-rate parity and false-positive-rate parity.
- C: Equal opportunity is parity of the true-positive rate, P(Ŷ=1 | Y=1, group); false-positive parity is a separate condition.
- D: Equal opportunity asks only for the true-positive half, so anything that satisfies equalized odds satisfies it.
- E: It constrains the rate of favorable decisions alone, whatever the people's true outcomes.

**Source:** Three definitions

## MA-ch07.2

A lender's model approves (Ŷ=1) or declines loan applicants. On held-out data, Y=1 means the applicant would have repaid. Group P (1,000 applicants): 240 approved who would repay, 60 approved who would not repay, 160 declined who would repay, 540 declined who would not repay. Group Q (1,000 applicants): 120 approved who would repay, 160 approved who would not repay, 80 declined who would repay, 640 declined who would not repay. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The ratio of approval rates (Q over P) is about 0.93, above a 0.8 screening convention.
- [ ] B. The true-positive rate is 0.60 in both groups, so equal opportunity holds.
- [ ] C. Equalized odds holds in these data.
- [ ] D. Because the true-positive rates match, approval precision also matches across groups.
- [ ] E. Among applicants who would not repay, the approval rate in group Q is twice that in group P.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Approval rates are 0.30 for P and 0.28 for Q, and 0.28/0.30 = 0.93.
- B: 240/400 = 0.60 in P and 120/200 = 0.60 in Q.
- C: Equal true-positive rates are only half of equalized odds, and the false-positive rates differ (0.10 versus 0.20).
- D: Precision also depends on the base rate and the false-positive rate; it is 240/300 = 0.80 in P and 120/280, about 0.43, in Q.
- E: False-positive rates are 160/800 = 0.20 for Q and 60/600 = 0.10 for P.

**Source:** Three definitions

## MA-ch07.3

A recruiting model flags applicants (Ŷ=1) for an interview; Y=1 means the applicant was later rated qualified. Group M (500 applicants): 170 flagged and qualified, 30 flagged and not qualified, 80 not flagged but qualified, 220 not flagged and not qualified. Group N (500 applicants): 60 flagged and qualified, 140 flagged and not qualified, 40 not flagged but qualified, 260 not flagged and not qualified. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because demographic parity holds, the groups must have similar false-positive rates.
- [ ] B. Equal flag rates show the two groups contain the same share of qualified applicants.
- [ ] C. The precision of flags is higher in group N than in group M.
- [ ] D. The false-positive rate in group N (0.35) is nearly three times that in group M (0.12).
- [ ] E. Both groups are flagged at the same rate, 0.40, so demographic parity holds exactly.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Demographic parity ignores true outcomes, so error rates can differ freely; here they are 0.12 and 0.35.
- B: Qualified shares are 250/500 = 0.50 in M and 100/500 = 0.20 in N; the flag rate also depends on the error rates.
- C: Precision is 170/200 = 0.85 in M and 60/200 = 0.30 in N.
- D: 140/400 = 0.35 and 30/250 = 0.12, a ratio of about 2.9.
- E: 200/500 = 0.40 in each group.

**Source:** Three definitions

## MA-ch07.4

A model predicts which patients need follow-up care (Ŷ=1); Y=1 means the patient actually needed it. Group A (1,000 patients): 400 flagged who needed it, 100 not flagged who needed it, 50 flagged who did not, 450 not flagged who did not. Group B (1,000 patients): 160 flagged who needed it, 40 not flagged who needed it, 80 flagged who did not, 720 not flagged who did not. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equalized odds holds: the true-positive rate is 0.80 and the false-positive rate is 0.10 in both groups.
- [ ] B. Demographic parity must also hold here, because equalized odds holds and the error rates are identical in the two groups.
- [ ] C. Even if every group B patient who needed follow-up were flagged, lifting B's flag rate to 0.45 would require a false-positive rate of at least about 0.31 in B.
- [ ] D. The gap in flag rates (0.45 versus 0.24) is explained by different shares of patients who needed follow-up, not by different error rates.
- [ ] E. The precision of flags is the same in both groups, since the true-positive and false-positive rates match.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 400/500 and 160/200 are both 0.80; 50/500 and 80/800 are both 0.10.
- B: Flag rate is base rate × TPR + (1 − base rate) × FPR, so equal TPR and FPR still give different flag rates when base rates differ (0.50 versus 0.20).
- C: B needs 450 flags, only 200 patients needed follow-up, so at least 250 of the other 800 must be flagged: 250/800 = 0.3125.
- D: The error rates are identical across groups, so only the 50% versus 20% need rates can produce the gap.
- E: Precision is 400/450, about 0.89, in A and 160/240, about 0.67, in B.

**Source:** Three definitions

## MA-ch07.5

A resume-screening tool advanced 180 of 600 applicants in group X and 168 of 400 applicants in group Y. A reviewer computes the ratio of the lower group's advance rate to the higher group's advance rate and flags any ratio below 0.8 for further review (a screening convention, not a verdict). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The ratio shows how many qualified applicants were missed in each group.
- [ ] B. The ratio is about 0.71, so the screen is flagged under the convention.
- [ ] C. Had group X's advance rate been 0.34 (a ratio of about 0.81), the screen would pass the convention, which would show the process is free of discrimination.
- [ ] D. Being flagged under the convention shows that the screen is unlawful.
- [ ] E. A gap of 12 percentage points with samples of 600 and 400 applicants is the sort of difference chance alone would plausibly produce between groups with identical true rates.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The ratio compares selection rates only and uses no information about who was qualified.
- B: 0.30/0.42 = 0.714, which is below 0.8.
- C: Passing a ratio threshold does not rule out discrimination, which can exist above the threshold or act through other mechanisms.
- D: A ratio below 0.8 is a heuristic that triggers further review; it does not itself establish a legal violation.
- E: A two-proportion z-test gives z of about 3.9 (pooled rate 0.348), far beyond what chance produces at these sample sizes.

**Source:** Each metric is a values claim

## MA-ch07.6

A bank's model flags transactions (Ŷ=1) for manual review, which delays the customer, so being flagged is the burden. Over a month, 12% of customers in group R were flagged and 20% in group S. An analyst computes a disparate-impact ratio (lower group rate divided by higher group rate) and compares it with a 0.8 convention that is meant to be applied to the rate of the favorable outcome. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Computed on the rates of not being flagged, the ratio is also 0.60, since the two framings describe the same gap.
- [ ] B. Computed on flag rates, the ratio is 0.60.
- [ ] C. The gap between the groups is 12 percentage points on the flag rate but only 8 points on the rate of not being flagged, because the two outcomes differ.
- [ ] D. Because not being flagged is the favorable outcome here, the ratio that matches the convention is about 0.91.
- [ ] E. The same data can pass or fail the 0.8 convention depending on which outcome is called favorable, so the analyst must state that choice.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Not-flagged rates are 0.88 and 0.80, and 0.80/0.88 is about 0.91.
- B: 0.12/0.20 = 0.60.
- C: The two rates are complements, so the gap is 8 points either way (0.20 − 0.12 = 0.88 − 0.80).
- D: The convention is stated on favorable-outcome rates, which here are the not-flagged rates.
- E: A ratio of 0.60 fails and a ratio of 0.91 passes, so the verdict flips with the framing.

**Source:** Each metric is a values claim

## MA-ch07.7

A risk model outputs a probability score, and people with a score of at least 0.5 are flagged. Among flagged people the score takes only two values, 0.6 and 0.9. Group A: 300 flagged people scored 0.6, of whom 180 had the positive outcome, and 100 scored 0.9, of whom 90 had it. Group B: 100 flagged people scored 0.6, of whom 40 had the positive outcome, and 300 scored 0.9, of whom 230 had it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In group B, people who scored 0.9 had the positive outcome about 77% of the time, so the score overstates their risk.
- [ ] B. If a score were calibrated within each group, precision among flagged people would have to be equal across groups.
- [ ] C. Among flagged people the positive-outcome rate is 0.675 in both groups, so predictive parity holds at this cutoff.
- [ ] D. Because predictive parity holds at the cutoff, the score is calibrated within each group.
- [ ] E. Calibration within groups requires that, at each score value, the observed positive rate matches the score in every group.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: 230/300 = 0.767, below the stated 0.9.
- B: Under calibration, precision among flagged people equals their average score, which depends on each group's mix of scores and so can differ.
- C: (180+90)/400 = 0.675 in A and (40+230)/400 = 0.675 in B.
- D: Group B's observed rates (0.40 at score 0.6, about 0.77 at score 0.9) do not match its scores, although its overall precision equals A's.
- E: That is the definition: among people given score s, a fraction s should have the positive outcome, in each group.

**Source:** Three definitions

## MA-ch07.8

A model outputs probability scores that take one of three values: 0.2, 0.5 or 0.8. Expected calibration error (ECE) is the sum over score values of (share of people with that score) × |observed positive rate − score|. Group A (1,000 people): score 0.2, 500 people, 105 positive; score 0.5, 300 people, 147 positive; score 0.8, 200 people, 158 positive. Group B (1,000 people): score 0.2, 400 people, 120 positive; score 0.5, 300 people, 165 positive; score 0.8, 300 people, 225 positive. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equal ECE in the two groups would imply equal true-positive rates.
- [ ] B. Pooling both groups into one ECE calculation gives about 0.04, which hides that group B's calibration error is several times group A's.
- [ ] C. With bins of 200 to 500 people, a gap of 0.01 in group A is within what sampling noise could produce.
- [ ] D. ECE is about 0.01 for group A and about 0.07 for group B.
- [ ] E. In group B, people with score 0.2 had a positive rate below 0.2, so the score overstates their risk and a decision-maker would be too cautious about them.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: ECE measures agreement between scores and outcome frequencies; true-positive rates depend on how scores are turned into decisions and on who actually has the outcome.
- B: Pooled bins have observed rates 0.25, 0.52 and 0.766, giving ECE of about 0.037, while the group values are 0.01 and 0.07.
- C: The standard error of an observed rate near 0.2 to 0.5 from 200 to 500 people is roughly 0.02 to 0.03.
- D: A: (500×0.01 + 300×0.01 + 200×0.01)/1000 = 0.01. B: (400×0.10 + 300×0.05 + 300×0.05)/1000 = 0.07.
- E: Their observed rate is 120/400 = 0.30, above 0.2, so the score understates their risk.

**Source:** Three definitions

## MA-ch07.9

Group 1 has a base rate (share of people with the positive outcome) of 0.5 and group 2 has a base rate of 0.3. A binary classifier is reported to have precision (positive predictive value) of 0.75 and a false-positive rate of 0.10 in both groups. Take these as exact population values. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If both groups instead had base rate 0.4, equal precision of 0.75 and equal false-positive rate of 0.10 would still require different true-positive rates.
- [ ] B. The same precision and false-positive rate can be achieved in both groups with a true-positive rate of 0.50 in both.
- [ ] C. Collecting more labeled data and training a more flexible model would bring the two true-positive rates together while holding precision and false-positive rate fixed.
- [ ] D. In this example the group with the higher base rate has the higher true-positive rate.
- [ ] E. Bayes' rule implies the true-positive rates must be about 0.30 in group 1 and 0.70 in group 2.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: With equal base rates the same relation gives equal true-positive rates, 0.10 × 3 × (0.6/0.4) = 0.45 in both.
- B: A true-positive rate of 0.5 would give precision of about 0.83 in group 1 and 0.68 in group 2, not 0.75 in both.
- C: The relation is arithmetic on population rates; with these precision and false-positive values the true-positive rates are pinned at 0.30 and 0.70 whatever the model.
- D: Group 1, with base rate 0.5, has the lower true-positive rate (0.30 versus 0.70).
- E: Precision odds equal base-rate odds × TPR/FPR, so TPR = 0.10 × 3 × (1−p)/p, which is 0.30 for p = 0.5 and 0.70 for p = 0.3.

**Source:** The arithmetic — the actual proof, not a gesture

## MA-ch07.10

Two groups have base rates of 0.5 and 0.2. Consider two classifiers: (i) one that approves every person in both groups regardless of features, and (ii) a perfect classifier that approves exactly the people who have the positive outcome. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Classifier (i) satisfies predictive parity.
- [ ] B. Classifier (ii) satisfies equalized odds and predictive parity but violates demographic parity.
- [ ] C. Classifier (i) satisfies equalized odds, because its true-positive rate and its false-positive rate are both 1 in each group.
- [ ] D. Because classifier (i) satisfies two of the three criteria, it is a useful way of resolving the conflict between them without giving up predictive value.
- [ ] E. Classifier (i) satisfies demographic parity.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Its precision equals each group's base rate, 0.5 versus 0.2.
- B: Perfect prediction gives TPR 1, FPR 0 and precision 1 in both groups, but selection rates equal the unequal base rates.
- C: Approving everyone gives TPR = FPR = 1 in every group, so the rates match.
- D: It carries no information about individuals, so it avoids the conflict only by being useless as a predictor.
- E: Both groups are approved at rate 1.

**Source:** The arithmetic — the actual proof, not a gesture

## MA-ch07.11

A lender scores applicants and approves anyone whose score is at or above a cutoff. On held-out data, group G has 1,000 people who would repay and 1,000 who would not; group H has 400 who would repay and 1,600 who would not. The table gives, for each cutoff, how many of each kind score at or above it.

| Cutoff | G would repay | G would not | H would repay | H would not |
|---|---|---|---|---|
| 0.4 | 900 | 500 | 340 | 720 |
| 0.5 | 800 | 350 | 280 | 480 |
| 0.6 | 700 | 250 | 220 | 320 |
| 0.7 | 550 | 150 | 140 | 160 |

Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With a single cutoff of 0.6, the true-positive rate is 0.70 in G and 0.55 in H.
- [ ] B. Using cutoff 0.6 for G and 0.5 for H makes both the true-positive rates and the false-positive rates equal across the two groups, so equalized odds holds.
- [ ] C. Under cutoffs of 0.6 for G and 0.5 for H, an applicant in G and an applicant in H who both score 0.55 receive different decisions.
- [ ] D. Even if both groups had identical true-positive rates and identical false-positive rates, their base rates (0.5 versus 0.2) would still leave the precision of approvals unequal.
- [ ] E. Using cutoff 0.6 for G and 0.5 for H makes the precision of approvals about equal in the two groups, since the true-positive rates match.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: 700/1000 = 0.70 and 220/400 = 0.55.
- B: True-positive rates are both 0.70, but false-positive rates are 250/1000 = 0.25 for G and 480/1600 = 0.30 for H.
- C: The G applicant is declined (0.55 < 0.6) and the H applicant is approved (0.55 ≥ 0.5), the individual-level objection to group-specific cutoffs.
- D: Precision odds equal base-rate odds × TPR/FPR, so identical rates with base-rate odds of 1 and 0.25 give unequal precision (for example TPR 0.70 and FPR 0.25 give about 0.74 versus 0.41); in the table the gap is wider (0.74 versus 0.37) partly because H's false-positive rate is also higher.
- E: Precision is 700/950, about 0.74, for G and 280/760, about 0.37, for H.

**Source:** The toolkit and what it cannot do

## MA-ch07.12

Two equal-sized groups have true base rates of 0.6 and 0.3, and the recorded labels are exactly correct. A perfect classifier predicts every label correctly. Here demographic parity means equal selection rates in the two groups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Any classifier with equal selection rates in the two groups must have overall accuracy of at most 0.85.
- [ ] B. Reaching demographic parity here means moving some decisions away from the true labels in one group or both.
- [ ] C. The perfect classifier satisfies equalized odds but violates demographic parity.
- [ ] D. The perfect classifier's selection rates are 0.6 and 0.3, a ratio (lower over higher) of 0.5.
- [ ] E. Demographic parity can be reached here without adding misclassifications, since the recorded outcomes are correct.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: If both groups are selected at rate s, their error rates are at least |0.6 − s| and |0.3 − s|, which average at least 0.15, so accuracy is at most 0.85.
- B: Closing the gap in selection rates means moving decisions away from the true labels in one or both groups.
- C: It has TPR 1 and FPR 0 in both groups, while its selection rates equal the unequal base rates.
- D: A perfect classifier selects exactly those with the positive outcome, and 0.3/0.6 = 0.5.
- E: Any move toward equal selection rates departs from the true labels, so errors rise, to at least 0.15 of people.

**Source:** Each metric is a values claim

## MA-ch07.13

A lender removes the field recording applicants' ethnicity from its model's inputs but keeps postal code, first name and school attended. The company concludes that outcomes cannot differ by ethnicity. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Without the field in the model, no one can measure group-level error rates.
- [ ] B. A rule that never uses the protected attribute cannot be found to have disparate impact in legal frameworks that recognize it.
- [ ] C. Dropping the field guarantees equal false-positive rates across ethnic groups.
- [ ] D. Postal code and similar fields can correlate with ethnicity, so the model may still produce outcomes that differ by ethnic group.
- [ ] E. Keeping the field in the evaluation data, while excluding it from the model's inputs, lets analysts audit outcomes by group.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Group labels can be kept in the evaluation data, apart from the model's inputs, and used to compute rates by group.
- B: Disparate-impact doctrine concerns facially neutral practices that burden a group, so a rule can be neutral on its face and still be challenged.
- C: Removing an input guarantees nothing about error rates, which depend on how outcomes and the remaining features relate to group.
- D: Proxies can carry much of the information in the removed attribute, so group-correlated outcomes can persist.
- E: Auditing needs the attribute at evaluation time even when the model is not allowed to use it.

**Source:** Fairness through awareness vs. unawareness

## MA-ch07.14

Individual fairness in its Lipschitz form requires that for any two people x and y, the distance between their outcome distributions is at most a task-specific distance d(x, y) between the people. A scoring system gives each person a probability of approval, so the distance between two people's outcome distributions is the absolute difference of their approval probabilities. Four people have approval probabilities M(x1) = 0.70, M(x2) = 0.55, M(x3) = 0.60 and M(x4) = 0.20, and pairwise distances d(x1,x2) = 0.10, d(x1,x3) = 0.30, d(x1,x4) = 0.50, d(x2,x3) = 0.35, d(x2,x4) = 0.40, d(x3,x4) = 0.45. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Whether the pair (x1, x2) counts as a violation depends on the similarity distance chosen, not only on the model's outputs.
- [ ] B. The pair (x1, x4) violates the condition, because their outputs differ by as much as their distance.
- [ ] C. The pair (x1, x2) violates the condition.
- [ ] D. If x1 and x2 belong to different demographic groups, the violation shows a group-level disparity in approval rates.
- [ ] E. Changing M(x1) to 0.62, with all other values unchanged, would remove the violation without creating a new one.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: With d(x1,x2) = 0.20 the same outputs satisfy the condition.
- B: Their outputs differ by exactly 0.50, equal to d(x1,x4), and the condition allows equality.
- C: Their outputs differ by 0.15, which exceeds d(x1,x2) = 0.10.
- D: The condition compares individual pairs; one violating pair says nothing about the groups' overall approval rates.
- E: The gaps become 0.07 (limit 0.10), 0.02 (limit 0.30) and 0.42 (limit 0.50).

**Source:** Beyond group metrics: individual fairness

## MA-ch07.15

Check each statement that is true about individual fairness (similar individuals should be treated similarly) and its relation to group fairness criteria. Each statement is worth 1 point (5 points total).

- [ ] A. Checking all pairs of individuals becomes expensive for large populations, so audits often sample pairs.
- [ ] B. A model can satisfy demographic parity while treating two near-identical people very differently.
- [ ] C. A model can treat similar people alike under a chosen metric and still show different selection rates between groups.
- [ ] D. Individual fairness can be evaluated from per-group confusion matrices alone, since they contain every person's outcome.
- [ ] E. The choice of similarity metric is a technical detail that does not affect the fairness conclusion, since any reasonable metric agrees.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The number of pairs grows quadratically with the population.
- B: Parity constrains group rates; it does not limit which individuals within a group receive the favorable decision.
- C: If the groups differ on features the metric counts as relevant, consistent treatment of similar people coexists with unequal group rates.
- D: It needs a notion of which individuals are similar and a comparison of their treatment, which group-level matrices average away.
- E: Different metrics give different verdicts on the same pair; deciding which differences between people are relevant is a substantive judgment.

**Source:** Beyond group metrics: individual fairness

## MA-ch07.16

In a causal model of a loan decision, a protected attribute A influences an education credential E, and E is an input to a predictor Ŷ. Unobserved background factors U also influence E. A predictor is counterfactually fair for an individual if its prediction would have had the same distribution had A taken a different value, with that individual's background factors U held fixed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A predictor that takes E as an input is in general not counterfactually fair here, because changing A changes E.
- [ ] B. Judging counterfactual fairness requires assumptions about the causal structure; observed data alone does not settle it.
- [ ] C. Counterfactual fairness implies equalized odds, because a predictor that ignores the protected attribute's effects must have equal error rates.
- [ ] D. Which paths from A to the prediction are acceptable is a value judgment that the causal graph does not supply.
- [ ] E. A predictor using only variables not causally downstream of A is counterfactually fair with respect to this model.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: With U fixed, a different A produces a different E, which moves the prediction.
- B: Different causal structures can produce the same observed distribution while implying different counterfactuals.
- C: It is an individual-level causal condition and places no constraint on error rates conditional on the true outcome.
- D: The graph shows which paths exist; whether a path through a credential is legitimate is a normative question.
- E: Its inputs do not change when A is changed counterfactually, so neither does its output.

**Source:** Causal fairness: what the data cannot tell you

## MA-ch07.17

A system allocates a benefit b_i to each of eight people. Generalized entropy with parameter 2 is GE(2) = (1/N) Σ ½[(b_i/μ)² − 1], where μ is the mean benefit; this equals half the squared coefficient of variation (population standard deviation divided by the mean, squared). Group P has benefits 0.2, 0.8, 0.2, 0.8 and group Q has benefits 0.5, 0.5, 0.5, 0.5. The between-group component is GE(2) computed after replacing each person's benefit by their group's mean benefit; the within-group component is the remainder. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Most of GE(2) comes from the between-group component.
- [ ] B. A comparison of the two groups' mean benefits would show no group-level disparity.
- [ ] C. GE(2) for the eight people is 0.09.
- [ ] D. Doubling every person's benefit would double GE(2).
- [ ] E. Because the group means are equal, the benefits are distributed fairly and no further inequality analysis is needed.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Both group means are 0.5, so the between-group component is 0 and all of GE(2) is within-group.
- B: The means are 0.5 and 0.5.
- C: The mean is 0.5 and the population variance is 0.045, so GE(2) = ½ × 0.045/0.25 = 0.09.
- D: GE depends on b_i/μ, so multiplying all benefits by a constant leaves it unchanged.
- E: Members of group P receive very unequal benefits (0.2 versus 0.8), a large within-group inequality that group means hide.

**Source:** The Generalized Entropy Index

## MA-ch07.18

A risk tool assigns each person a score in [0, 1]. Assume the two groups have different base rates (0.4 and 0.2) and that the score is imperfect, meaning it does not separate all positives from all negatives. Three properties are of interest: (1) calibration within groups, meaning among people with a given score the positive rate equals the score in each group; (2) equal average score among actual positives in the two groups; (3) equal average score among actual negatives in the two groups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The conflict is a property of the groups' base rates and the score's imperfection, not of any particular learning algorithm.
- [ ] B. The result implies that calibration within groups cannot hold in any form, even for a single group considered alone.
- [ ] C. Gathering more labeled data does not remove the conflict; it only makes the group rates better estimated.
- [ ] D. If the two groups had equal base rates, a score with the same distribution in both groups could satisfy all three properties.
- [ ] E. Under these assumptions, properties (1), (2) and (3) cannot all hold.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The argument uses only population rates, so any scoring method with these properties is subject to it.
- B: Calibration within groups can hold by itself; the result says it cannot be combined with both balance properties under these assumptions.
- C: The impossibility concerns the population quantities themselves.
- D: With equal base rates and identical joint distributions of score and outcome, calibration and both balance conditions hold together.
- E: With unequal base rates and an imperfect score, calibration within groups forces the average scores among positives or among negatives to differ.

**Source:** The arithmetic — the actual proof, not a gesture

## MA-ch07.19

A pretrial risk tool labels each person high-risk or low-risk. An analyst finds that among people who were not re-arrested, 45% of group X and 20% of group Y were labeled high-risk. The vendor replies that among people labeled high-risk, 60% of both groups were re-arrested, and that the groups' re-arrest base rates are 0.5 for X and 0.3 for Y. Take all figures as exact. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The analyst's finding by itself shows that the tool uses group membership as an input.
- [ ] B. The analyst's figures and the vendor's figures can both be correct at the same time.
- [ ] C. The disagreement is a factual one that more data would settle by showing which set of figures is correct.
- [ ] D. If the tool were adjusted until the false-positive rates matched while precision stayed equal, the false-negative rates would have to differ.
- [ ] E. Equal precision of the high-risk label means wrongly labeled people in the two groups bear the same burden.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A tool that never sees group membership can still show different error rates through correlated features and differing base rates.
- B: They measure different quantities, error rates conditional on the true outcome and precision conditional on the tool's output, and with unequal base rates they can differ in this way.
- C: Both statements are already accurate; the dispute is over which criterion should take priority.
- D: Equal precision and equal false-positive rate force the true-positive rates apart when base rates differ and the tool is imperfect.
- E: The false-positive rates are 0.45 and 0.20, so non-re-arrested people in X are labeled high-risk far more often.

**Source:** The COMPAS case — the theorem in public

## MA-ch07.20

An organization must choose which group fairness criterion to prioritize for two systems. System one is a cancer-screening aid: a missed case can be fatal, and a false alarm leads to an inexpensive follow-up test. System two flags benefit claims as suspected fraud: a flagged person's payments are frozen during review. Check each statement that is a sound argument about choosing criteria. Each statement is worth 1 point (5 points total).

- [ ] A. For the screening aid, comparing false-negative rates (equivalently, true-positive rates) across groups targets the main harm.
- [ ] B. Demographic parity is the right criterion for both systems whenever base rates differ, since base rates are irrelevant to harm.
- [ ] C. For the fraud flag, comparing false-positive rates across groups targets the harm that matters most.
- [ ] D. Which criterion to prioritize can be derived from the confusion matrices alone, without knowing who bears the cost of each kind of error.
- [ ] E. The criterion that gives the highest overall accuracy is the right one for both systems, since accuracy summarizes every error.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The costliest error is a missed case, and equal true-positive rates ask that this error not fall more heavily on one group.
- B: Equal selection rates ignore who is harmed by which error, and base-rate differences change what equal rates would mean.
- C: A wrongly flagged person bears the cost, and the false-positive rate measures how often that happens to people who did nothing wrong.
- D: The matrices give rates, but the choice depends on the cost of each error type to the people affected.
- E: Overall accuracy weights all errors equally and says nothing about which group bears which error.

**Source:** Each metric is a values claim

## MA-ch07.21

A team has built a loan-approval model by minimizing overall log loss and is now deciding how to report fairness. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Choosing which error rates to equalize trades one group's harms against another's, so accountable people should make and record the choice.
- [ ] B. If a regulator requires a specific metric, decisions remain open, such as which groups to compare and what tolerance counts as equal.
- [ ] C. A tool that computes every fairness metric can identify which metric is correct for the deployment, since the best one scores highest.
- [ ] D. If the model passes the chosen metric, there is no need to document which other criteria were traded away, since the chosen one was met.
- [ ] E. Because the loss function never mentions groups, minimizing overall log loss has no bearing on how errors are distributed across groups.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A value-laden trade-off should be owned by someone with authority and accountability, with reasons on the record.
- B: A named metric fixes the formula but not its application.
- C: Metrics describe consequences; choosing among them depends on values and on who bears the costs.
- D: Passing one criterion can mean others fail, and affected parties and reviewers need to know what was given up.
- E: Minimizing an average loss over all examples weights every example equally, which determines which errors the model tolerates and so how error rates fall across groups, whether or not anyone chose it.

**Source:** Who should have decided

## MA-ch07.22

A model predicts whether a person will be arrested within two years. An audit finds equal true-positive and false-positive rates across two neighborhoods, measured against arrest records. Suppose one neighborhood is patrolled much more heavily, so the same behavior is more likely to lead to an arrest there. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Using different cutoffs per neighborhood would correct the measurement problem by rebalancing who is flagged.
- [ ] B. A metric on this label measures agreement with arrest patterns, which reflect enforcement as well as behavior.
- [ ] C. The audit certifies that neither neighborhood is disadvantaged by the tool, since the error rates are equal.
- [ ] D. Equal error rates against recorded arrests do not establish equal error rates against actual offending.
- [ ] E. An independent measure of the behavior would let the team estimate how far the arrest label departs from it.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Cutoffs change decisions, not how the recorded outcome relates to behavior; the measurement problem remains.
- B: The model is scored on matching the recorded outcome, not on matching the behavior the outcome stands in for.
- C: It certifies parity with respect to a label that may itself encode the disparity.
- D: If arrest probability given behavior differs by neighborhood, the recorded outcome measures something different in each.
- E: A second measure gives a check on the recorded outcome's validity.

**Source:** The persistent limits

## MA-ch07.23

In an audit sample, 300 of 400 truly qualified applicants in group A were approved (true-positive rate 0.75) and 24 of 40 truly qualified applicants in group B were approved (true-positive rate 0.60). Approximate 95% intervals for the true-positive rate are 0.71 to 0.79 for A and 0.45 to 0.74 for B. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The interval for B is wider than A's because B's true-positive rate is lower.
- [ ] B. A non-significant result for the small group shows that the two groups have equal true-positive rates, since no difference was detected.
- [ ] C. Testing many small subgroups at the 5% level makes it likely some gap looks significant by chance.
- [ ] D. A 15-point gap in the point estimates is enough to conclude with certainty that the true rates differ, since it is large.
- [ ] E. The interval for B is wide, so B's true-positive rate is estimated imprecisely.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Width depends mainly on sample size (40 versus 400); a rate nearer 0.5 widens it only slightly.
- B: Low power means a real gap can go undetected; absence of evidence of a gap is not evidence of equality.
- C: With many comparisons, false positives accumulate unless the analysis accounts for multiple testing.
- D: Sampling variation can produce a gap of this size, especially with 40 observations; the conclusion carries uncertainty.
- E: With only 40 qualified applicants the standard error is large.

**Source:** The persistent limits

## MA-ch07.24

A screening tool's selection rates, with 500 people in each of four cells, are: women in the north 0.50, women in the south 0.30, men in the north 0.30, men in the south 0.50. A reviewer flags any ratio of lowest rate to highest rate below 0.8. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Passing the check on gender and the check on region separately implies the check on gender-by-region will also pass.
- [ ] B. The ratio of the lowest to the highest of the four cell rates is 0.6, which is flagged under the convention.
- [ ] C. Women overall and men overall are both selected at 0.40, and the north and the south are both at 0.40.
- [ ] D. Checking intersections as well as single attributes multiplies the number of groups, so cells become small and estimates noisy.
- [ ] E. Since the single-attribute comparisons show no gap, no subgroup can be disadvantaged within either attribute's categories.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: This example passes both margins and fails the cells.
- B: 0.30/0.50 = 0.60, below 0.8.
- C: Each margin averages one 0.50 cell and one 0.30 cell.
- D: The number of cells multiplies with each attribute while the sample is split among them.
- E: Disparities can cancel in the margins and appear only in the combinations.

**Source:** The persistent limits

## MA-ch07.25

Practitioners distinguish pre-processing, in-processing and post-processing methods for reducing group disparities in a classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reweighting training examples so that group-and-label combinations are balanced is a pre-processing method.
- [ ] B. Group-specific cutoffs applied to a frozen model's scores require the group attribute at decision time.
- [ ] C. Adversarial debiasing, where a second network tries to predict the group from the model's representation, is an in-processing method.
- [ ] D. Any of the three families can remove bias built into the recorded labels without further information about how those labels were produced, because they adjust the data or the decisions.
- [ ] E. Any method that leaves both the training data and the trained model unchanged and adjusts only the final decisions is a post-processing method.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It changes the data the model is trained on, before training.
- B: The cutoff to apply depends on which group the person is assigned to.
- C: It alters the training objective rather than the data or the final decisions.
- D: These methods act on data, objective or decisions; they cannot know that a label is mismeasured unless that is learned some other way.
- E: Post-processing is defined by acting on the model's outputs after training, with the data and the model itself left as they were.

**Source:** The toolkit and what it cannot do

## MA-ch07.26

A classifier has a true-positive rate of 0.80 and a false-positive rate of 0.10 in both group 1 and group 2. At validation both groups had base rate 0.30. After deployment, group 2's base rate rises to 0.50, while the classifier's true-positive and false-positive rates in each group stay the same. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. After the shift, precision of positive predictions is about 0.77 in group 1 and about 0.89 in group 2.
- [ ] B. After the shift, the ratio of selection rates (group 1 over group 2) falls to about 0.69.
- [ ] C. Equalized odds stops holding after the shift because the base rate changed.
- [ ] D. Because true-positive and false-positive rates are unchanged, no group metric needs rechecking after the shift.
- [ ] E. Precision parity was robust to the change in base rate.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Group 1: 0.24/(0.24+0.07) = 0.77. Group 2: 0.40/(0.40+0.05) = 0.89.
- B: Selection rates are 0.31 and 0.45, and 0.31/0.45 = 0.69.
- C: Equalized odds is defined by rates conditional on the true outcome, and those are unchanged.
- D: Selection rates and precision shifted, so other criteria must be re-measured on live data.
- E: Precision depends on the base rate, and moved from equal (0.77 in both) to unequal.

**Source:** The defense as deliverable

## MA-ch07.27

A score is perfectly calibrated within each of two groups. In group 1, 60% of people have score 0.2 and 40% have score 0.7. In group 2, 80% have score 0.2 and 20% have score 0.7. People with a score of at least 0.5 are flagged. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The base rates are 0.40 in group 1 and 0.30 in group 2.
- [ ] B. The true-positive rates at the 0.5 cutoff are equal in the two groups, because calibration makes the scores mean the same.
- [ ] C. The false-positive rates at the 0.5 cutoff are equal in the two groups, because the score is calibrated in both.
- [ ] D. Among people who actually have the positive outcome, the average score is about 0.55 in group 1 and about 0.43 in group 2.
- [ ] E. The two groups are flagged at equal rates, because the score is calibrated in both groups.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Under calibration, the base rate is the average score: 0.6×0.2 + 0.4×0.7 = 0.40 and 0.8×0.2 + 0.2×0.7 = 0.30.
- B: They are 0.28/0.40 = 0.70 in group 1 and 0.14/0.30 ≈ 0.47 in group 2.
- C: They are 0.12/0.60 = 0.20 in group 1 and 0.06/0.70 ≈ 0.09 in group 2.
- D: Weighting by outcome probability gives 0.22/0.40 ≈ 0.55 and 0.13/0.30 ≈ 0.43.
- E: Flag rates are 0.40 in group 1 and 0.20 in group 2.

**Source:** The arithmetic — the actual proof, not a gesture

## MA-ch07.28

A hospital tests a language-model assistant that triages patient messages as urgent or not and states its own confidence in words (for example, "I am 90% sure this is urgent"). The team wants to know whether the assistant's stated confidence means the same thing for patients writing in English and for patients writing in other languages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the assistant says "about 90% sure" equally often for both groups, that shows its stated confidence is calibrated in each group.
- [ ] B. A calibration check by group can be done without any outcome labels, by comparing stated confidence across groups.
- [ ] C. Hedged wording in the assistant's replies is good evidence that its stated numbers are calibrated.
- [ ] D. A confidence a language model states in words is a claim to test against outcomes, not an established probability.
- [ ] E. A calibration check done for one model version and prompt remains valid after either is changed.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Calibration compares stated confidence with observed outcomes; how often a number is stated says nothing about that.
- B: The check needs the true outcome to compare against the stated confidence within each group.
- C: Tone is not evidence of calibration; only agreement with observed frequencies is.
- D: Fluent statements of confidence need not track how often the model is right.
- E: Changing the model or the prompt can change the confidence statements, so the check must be repeated.

**Source:** Three definitions

## MA-ch07.29

General legal and ethical frameworks for decisions made with algorithms distinguish different kinds of unequal treatment. Check each statement that is true in general terms. Each statement is worth 1 point (5 points total).

- [ ] A. Satisfying one statistical fairness metric establishes legal compliance, since the metric measures whether the system is fair.
- [ ] B. A ratio of 0.8 between group selection rates is a bright-line legal test in every jurisdiction, not merely a rule of thumb.
- [ ] C. Using different cutoffs for protected groups to reduce a disparity can itself raise disparate-treatment concerns in some jurisdictions.
- [ ] D. In some legal regimes a practice with disparate impact can be justified by a legitimate need and is then checked for less discriminatory alternatives.
- [ ] E. Disparate treatment concerns decisions that differ by protected attribute; disparate impact concerns neutral-looking practices with disproportionate effects.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Legal compliance depends on the applicable law and its facts, not on any single metric.
- B: It is a rule of thumb used in some settings, not a universal legal standard.
- C: Explicit group-based decision rules can be restricted even when the aim is to reduce a disparity.
- D: Disparate impact is not automatically unlawful; justification and the availability of alternatives enter the analysis.
- E: That is the standard distinction between the two doctrines.

**Source:** Causal fairness: what the data cannot tell you

## MA-ch07.30

A risk model flags people (Ŷ=1) for an intervention; Y=1 means the person truly needed it. Group A (1,000 people): 400 flagged who needed it, 100 flagged who did not, 0 not flagged who needed it, 500 not flagged who did not. Group B (1,000 people): 300 flagged who needed it, 0 flagged who did not, 100 not flagged who needed it, 600 not flagged who did not. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equal accuracy means the two groups bear the same cost from the model's mistakes.
- [ ] B. Group B's true-positive rate is 1.0 and group A's is 0.75.
- [ ] C. Accuracy is 0.90 in both groups, so accuracy parity holds.
- [ ] D. Equalized odds holds, since the groups have equal accuracy and equal numbers of errors.
- [ ] E. Every error in group A is a false positive and every error in group B is a false negative.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: An unneeded intervention and a missed need can differ greatly in cost, so equal error counts do not mean equal burden.
- B: The values are swapped: group A's is 400/400 = 1.0 and group B's is 300/400 = 0.75.
- C: (400+500)/1000 = 0.90 and (300+600)/1000 = 0.90.
- D: True-positive rates are 1.0 and 0.75, and false-positive rates are about 0.17 and 0.
- E: Group A has 100 false positives and 0 false negatives; group B has 0 false positives and 100 false negatives.

**Source:** Three definitions
