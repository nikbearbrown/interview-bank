# Chapter 7: Fairness metrics

## ES-ch07.1

Two groups of applicants have base rates (shares with the positive outcome) of 0.5 and 0.2. A classifier has the same true-positive rate (0.8) and the same false-positive rate (0.1) in both groups. (a) Compute the precision (positive predictive value) of the classifier's positive predictions in each group. (b) Using Bayes' rule, explain why equal true-positive and false-positive rates cannot be combined with equal precision when base rates differ, and state the conditions under which the conflict disappears.

**Points:** 5

**Rubric (1 point each):**

1. Computes precision of about 0.89 in the group with base rate 0.5 (0.4/(0.4+0.05)) and about 0.67 in the group with base rate 0.2 (0.16/(0.16+0.08)).
2. Writes Bayes' rule for precision, or its odds form: the odds of a positive outcome given a positive prediction equal the prior (base-rate) odds times the likelihood ratio TPR/FPR.
3. Observes that equal TPR and FPR give equal likelihood ratios, so precision then moves with the base rate and cannot be equal when base rates differ.
4. States that this is arithmetic about population rates, not a defect of any algorithm or of the data, so more data or a better learner does not remove it; the conflict is over which criterion to prefer.
5. Gives the conditions under which the conflict disappears: equal base rates, or a classifier with no false positives such as a perfect one.

**Source:** The arithmetic — the actual proof, not a gesture

## ES-ch07.2

A hospital uses a model to flag patients for a care-management program (flag means Ŷ=1; Y=1 means the patient later had an avoidable admission). On held-out data, Group G (500 patients): 84 flagged with an avoidable admission, 30 flagged without, 66 not flagged with an avoidable admission, 320 not flagged without. Group H (300 patients): 48 flagged with an avoidable admission, 42 flagged without, 12 not flagged with an avoidable admission, 198 not flagged without. (a) For each group compute the flag rate, true-positive rate, false-positive rate and precision. (b) State which of demographic parity (use a screening convention that a ratio of flag rates below 0.8 is a violation), equal opportunity, equalized odds and predictive parity hold approximately. (c) Explain what else you would need before calling the model fair or unfair.

**Points:** 5

**Rubric (1 point each):**

1. Group G: flag rate 0.228, true-positive rate 0.56 (84/150), false-positive rate about 0.086 (30/350), precision about 0.74 (84/114).
2. Group H: flag rate 0.30, true-positive rate 0.80 (48/60), false-positive rate 0.175 (42/240), precision about 0.53 (48/90).
3. Judges each criterion: the flag-rate ratio is 0.228/0.30 = 0.76, below 0.8; the true-positive rates (0.56 versus 0.80) fail equal opportunity; the false-positive rates fail equalized odds; the precisions (0.74 versus 0.53) fail predictive parity; none holds.
4. Notes the base rates differ (0.30 in G, 0.20 in H) and that with an imperfect classifier these criteria cannot all be met together, so correcting one will move the others, and the gaps alone do not show a defect or intent.
5. Names what is needed before a verdict: the cost of a missed patient versus an unneeded enrollment and who bears each, sampling uncertainty given the group sizes, the validity of the outcome label, and an accountable person to choose the criterion.

**Source:** Three definitions

## ES-ch07.3

An independent analyst reports that a risk tool's false-positive rate is 45% for group X and 20% for group Y. The vendor answers that the tool is equally well calibrated for both groups: among people given any particular risk score, the proportion who experience the outcome is the same in X and Y. The base rate of the outcome is higher in group X. Both statements are accurate. (a) Explain how both can be true. (b) Say what kind of disagreement this is and what would and would not resolve it. (c) Say what information you would give the body that must decide whether to keep using the tool, who should make and record that decision, and what should be monitored afterwards.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the two claims as different criteria: false-positive-rate parity (rates conditional on the true outcome) versus calibration within groups (outcomes conditional on the score).
2. Explains with Bayes' rule or the odds identity that with unequal base rates and an imperfect tool, equal score meaning (equal precision or calibration) forces unequal error rates, so both claims can hold together.
3. Characterizes the dispute as one about which criterion to prioritize, a value question about who bears which errors, and says more data or more modeling would confirm the numbers without settling it.
4. Lists what the decision-maker needs: the harm to a person of a false positive versus a false negative in this setting, the size of each gap with its uncertainty, how the outcome label was measured, and alternatives such as other cutoffs, other tools or human review.
5. States that the decision belongs to the parties accountable for the deployment, should be made and recorded with reasons rather than defaulted to the vendor's chosen metric, and the traded-away criterion should keep being monitored.

**Source:** The COMPAS case — the theorem in public

## ES-ch07.4

Explain the principle of individual fairness (similar individuals should be treated similarly) and why it needs a similarity metric. Illustrate with two loan applicants who have identical income, credit history and debt but different postal codes: show how two reasonable choices of similarity metric give opposite verdicts on whether different decisions for them are acceptable, and say what each choice assumes. Then explain one practical difficulty in auditing individual fairness and one way group fairness criteria and individual fairness can disagree.

**Points:** 5

**Rubric (1 point each):**

1. States the principle in a usable form: the difference in how two people are treated (for example their outcome distributions) should be bounded by a task-relevant distance between them.
2. Explains that without a similarity metric the principle says nothing, because someone must specify which differences between people are relevant to the task.
3. Shows that a metric ignoring postal code makes the two applicants similar and so requires like treatment, while a metric that counts postal-code distance permits different treatment, giving opposite verdicts for the same model.
4. States what each metric assumes: ignoring postal code assumes location is irrelevant to the task (or only a proxy for something that should not count), counting it assumes location carries task-relevant information; either is a value judgment and can build in historical inequity, so it needs accountable review rather than a default.
5. Names a practical difficulty (all pairs are costly to check and need outcome distributions, so audits sample similar pairs and depend on the metric) and a disagreement (a model can meet group parity yet treat near-identical people differently, or be individually consistent yet show group disparity).

**Source:** Beyond group metrics: individual fairness

## ES-ch07.5

A company states: "Our hiring model is fair because it never sees applicants' gender." Evaluate this claim. Describe how the model could still produce gender-disparate outcomes, what tests you would run to check, and what you would recommend.

**Points:** 5

**Rubric (1 point each):**

1. Explains proxies: features correlated with gender, such as wording, career gaps or activities, can let a model reconstruct the removed attribute, so outcomes can still differ by gender.
2. States that fairness is judged by outcomes rather than by which inputs were used: in frameworks that recognize disparate impact a facially neutral practice can still be challenged, so "never sees gender" is not a defense.
3. Describes tests: keep gender in the evaluation data, apart from model inputs, and compute selection rates, error rates and calibration by gender with uncertainty; also check whether gender can be predicted from the model's inputs or scores.
4. Names a second route to gender-disparate outcomes besides proxies: training labels that record past hiring decisions or ratings can carry earlier bias, and unequal representation or data quality across groups can make the model's errors fall unevenly, neither of which depends on the model seeing gender.
5. Recommends concrete steps: choose which fairness criterion matters for the harm involved, measure it, mitigate within legal limits, document the choice and its trade-offs, and monitor after deployment.

**Source:** Fairness through awareness vs. unawareness

## ES-ch07.6

A lender approves applicants whose score is at or above a cutoff. Group S has 600 people who would repay and 1,400 who would not; group T has 300 who would repay and 700 who would not. The table gives, for each cutoff, the number of each kind with score at or above it.

| Cutoff | S would repay | S would not | T would repay | T would not |
|---|---|---|---|---|
| 0.5 | 480 | 420 | 210 | 245 |
| 0.6 | 420 | 280 | 165 | 140 |
| 0.7 | 330 | 140 | 105 | 56 |

Compare (i) a single cutoff of 0.6 for both groups with (ii) a cutoff of 0.6 for S and 0.5 for T. Compute the true-positive rate and false-positive rate for each group under each option, explain why neither option equalizes both rates, discuss the costs and objections to each, and say what you would recommend or ask before deciding.

**Points:** 5

**Rubric (1 point each):**

1. Under the single cutoff of 0.6: S has true-positive rate 0.70 and false-positive rate 0.20, T has 0.55 and 0.20, so false-positive rates match but there is a 15-point true-positive gap.
2. Under cutoffs 0.6 for S and 0.5 for T: both true-positive rates are 0.70, but the false-positive rates are 0.20 for S and 0.35 for T, so the gap moves to the false-positive rate.
3. Explains that among the tabulated cutoffs no pair equalizes both rates because group T's score is less informative (at a false-positive rate of 0.20, T's true-positive rate is 0.55 versus S's 0.70), so exact equality would require degrading S's decisions in some way (for example by randomizing some of them) at a cost in accuracy.
4. Names objections: option (ii) gives people with the same score different decisions depending on group, which individual-level arguments and some legal regimes treat as problematic; option (i) is group-blind but approves qualified applicants in T less often (0.55 versus 0.70).
5. Recommends choosing by the harm of each error type with an accountable decision-maker, considering improving the score for T (better data or features) rather than only moving cutoffs, and monitoring both rates and precision after deployment.

**Source:** The toolkit and what it cannot do

## ES-ch07.7

A product manager says: "Fairness constraints always cost accuracy, so we should ship the most accurate model and treat fairness as a nice-to-have." Evaluate this claim. In your answer, say when a real tradeoff arises and when it does not, give a small numerical illustration, explain what choosing the most accurate model implicitly decides, and describe how you would present the tradeoff to a decision-maker.

**Points:** 5

**Rubric (1 point each):**

1. Identifies when a real tradeoff arises: for demographic parity when base rates differ and labels are accurate, a perfect predictor violates parity so meeting it forces errors; for equalized odds when no perfect classifier exists and the available scores are less informative for one group, equalizing means degrading that group's decisions.
2. Shows the cost is not universal: with equal base rates, or for criteria that a perfect classifier meets (such as equalized odds) when such a classifier is possible, no loss is forced, and when labels are noisy or biased against a group, accuracy measured on those labels is itself distorted.
3. Gives a valid numerical illustration, for example two equal groups with base rates 0.6 and 0.3, where a perfect classifier selects at 0.6 and 0.3 and any classifier forced to equal selection rates has accuracy at most 0.85.
4. Explains that maximizing accuracy is itself a choice: it weights all errors equally and lets error rates fall unevenly across groups, deciding by default who bears which mistakes.
5. Describes presenting the tradeoff as a frontier, with metrics at several cutoffs or constraint strengths and the cost stated as extra false positives and false negatives per 1,000 by group, so accountable decision-makers choose a point.

**Source:** Each metric is a values claim

## ES-ch07.8

A health system will use a model to flag patients for a limited care-coordination program. A patient who is truly high-need but not flagged is likely to be hospitalized; a flagged patient who is not high-need takes a program slot that could have gone to someone else, with little harm to that patient. The base rate of high-need patients is 30% in group X and 15% in group Y, partly because group X has had less access to primary care. Candidate criteria are demographic parity, equal opportunity (equal true-positive rates), equalized odds and predictive parity (equal precision). Choose a criterion or combination, defend the choice by reference to the harms and the people affected, state what you give up, and say what evidence would make you change your mind.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the dominant harm (missed high-need patients) and who bears it, and links the chosen criterion to it, for example equal opportunity, or equalized odds if the cost of wasted slots also matters.
2. States what is given up and why: if error rates are equalized, flag rates follow the base rates (for example about 0.31 versus 0.205 at a true-positive rate of 0.8 and a false-positive rate of 0.1), so demographic parity and precision parity are given up; equalizing flag rates instead would mean flagging more non-high-need patients in group Y.
3. Addresses the base-rate difference: because it partly reflects unequal access to care, whether and how to redress it through allocation is a policy question rather than only a statistical one, and the chosen criterion changes who receives the limited slots.
4. States what would change the choice: evidence on the relative costs of the two errors, a change in program capacity, a finding that labels are biased, or subgroup results with their uncertainty.
5. Says the choice is a value decision to be made and recorded by accountable parties (clinical leadership, ethics review, affected communities) and followed by monitoring of the chosen and traded-away metrics by group.

**Source:** The defense as deliverable

## ES-ch07.9

A regulator requires that credit-scoring models satisfy equalized odds across a protected attribute. A lender asks whether this settles the fairness question for its model. Explain what the requirement fixes, what it leaves open, and what difficulties arise in measuring it.

**Points:** 5

**Rubric (1 point each):**

1. States that the requirement fixes the criterion (equal true-positive and false-positive rates across groups), which moves the choice of criterion from the lender to the regulator but does not make the other decisions.
2. Lists decisions left open: how close counts as equal (tolerance), which groups and intersections, which cutoff, what outcome definition and time window, and what happens when sample sizes are small.
3. Names measurement difficulties: outcomes such as repayment are observed only for approved applicants (selective labels), so rates for declined applicants must be estimated; the group attribute may be unavailable or inferred; the outcome label may be imperfect.
4. Explains that equalized odds generally cannot coexist with equal precision or calibration within groups when base rates differ, so the lender still accepts and should document trade-offs against other criteria.
5. Adds that measuring compliance is not a one-off: it must be monitored on live data with uncertainty and drift in mind.

**Source:** Who should have decided

## ES-ch07.10

A vendor's audit report says: "On a held-out set, true-positive and false-positive rates differ by less than 2 points across the three demographic groups in our data, so the system is fair." List the assumptions this conclusion rests on and explain how each could fail.

**Points:** 5

**Rubric (1 point each):**

1. Label validity: the recorded outcome may measure something other than what matters (for example enforcement or past decisions rather than behavior), so parity on the recorded outcome is not parity on the real quantity.
2. Group definitions: three coarse categories may hide intersectional subgroups, and group labels may be missing, self-reported inconsistently or inferred with error.
3. Sampling uncertainty: a difference below 2 points means little without group sizes and confidence intervals, and small groups can hide large gaps.
4. One criterion only: parity of true-positive and false-positive rates says nothing about selection rates, precision or calibration, which can differ and may matter more for the harm at stake, and the criteria generally cannot all hold.
5. Context: a held-out set is not live use, so cutoff changes, population shift, feedback effects and the fairness of the prediction task itself, as affected people see it, are outside what the number shows.

**Source:** The persistent limits

## ES-ch07.11

In an audit of a fraud model, 2,000 legitimate transactions from customer group A included 240 that were incorrectly flagged, and 150 legitimate transactions from group B included 30 that were incorrectly flagged. (a) Compute the false-positive rate for each group and the difference. (b) Compute an approximate 95% confidence interval for the difference and a test of the difference, showing the formulas you use. (c) State what you conclude, what you do not conclude, and what the small size of group B implies for claims about other, smaller groups.

**Points:** 5

**Rubric (1 point each):**

1. Computes false-positive rates of 0.12 for A and 0.20 for B, a difference of 0.08.
2. Computes a standard error of about 0.033 (the square root of (0.2×0.8/150 + 0.12×0.88/2000)) and an approximate 95% interval for the difference of roughly 0.01 to 0.15.
3. Computes a two-proportion z statistic of about 2.4 (unpooled, consistent with the interval; two-sided p about 0.017) or about 2.85 (pooled rate 270/2150; p about 0.004), and says this is evidence that the true rates differ.
4. Interprets correctly: chance is an unlikely explanation for the gap, but its size is imprecisely known because group B is small, and the test says nothing about why the gap exists or whether it is unfair, nor about other criteria.
5. Explains that smaller or intersectional groups give wider intervals, that failing to find a significant gap is not evidence of equality, that many subgroup comparisons inflate false alarms, and that more data or pre-planned sample sizes are needed.

**Source:** The persistent limits

## ES-ch07.12

Describe counterfactual fairness for a decision about one person. Using a causal model in which a protected attribute A influences a credential E, which is an input to a predictor, explain (a) the question counterfactual fairness asks and how it differs from asking whether error rates are equal across groups; (b) the steps for evaluating it for one person; (c) what it requires that group metrics do not; and (d) one way to make a predictor satisfy it and a cost of doing so.

**Points:** 5

**Rubric (1 point each):**

1. States the question: would this person's prediction have had the same distribution had their protected attribute been different, with their background circumstances held fixed; this is an individual-level causal question, unlike group-level observed error rates.
2. Describes the steps: infer the person's background factors from what was observed (abduction), set the attribute to the alternative value (action), and propagate through the causal model to see the prediction (prediction).
3. Says it requires a causal model of how the variables are generated, which observational data alone cannot supply because different structures fit the same data, and the verdict is relative to the assumed model.
4. Gives a remedy such as using only variables not causally downstream of the protected attribute, or removing the attribute's influence from them, and names a cost: lost predictive information and the need to decide which influences to remove.
5. Notes that it also requires deciding which causal paths from the protected attribute count as unfair, a value judgment the causal graph does not make and that group metrics never ask for.

**Source:** Causal fairness: what the data cannot tell you

## ES-ch07.13

A system gives benefit scores to eight people. Generalized entropy with parameter 2 is GE(2) = half the squared coefficient of variation, ½(σ/μ)², with σ the population standard deviation and μ the mean. Group P has scores 0.9, 0.8, 0.7, 0.8 and group Q has scores 0.4, 0.3, 0.5, 0.4. (a) Compute the overall mean and GE(2). (b) Compute the between-group component, defined as GE(2) after replacing each person's score by their group's mean score, and the within-group component as the remainder. (c) Say which component dominates and what kind of remedy that suggests. (d) Give two limitations of this measure as a fairness measure.

**Points:** 5

**Rubric (1 point each):**

1. Computes the mean 0.6, population variance 0.045 and GE(2) = ½ × 0.045/0.36 = 0.0625.
2. Computes the between-group component using group means 0.8 and 0.4, giving GE(2) = 0.0556.
3. Gets the within-group component as 0.0625 − 0.0556 = 0.0069, so about 89% of the inequality is between groups.
4. Concludes that the disparity is mainly between groups and suggests group-level remedies (examining the process that gives Q lower scores, reweighting or cutoff adjustment) before examining inconsistent treatment of similar individuals inside groups.
5. Gives limitations: it needs a numeric benefit that someone must define, it shows how much and where inequality lies but not why (it is not causal), and the parameter choice sets whose differences count more.

**Source:** The Generalized Entropy Index

## ES-ch07.14

A university's admissions tool selects 30 of 100 applicants in group X and 30 of 100 applicants in group Y, so the selection rates are equal. In group X, 50 applicants meet the admission standard and all 30 selected meet it. In group Y, 20 applicants meet the standard, and the tool selected all 20 of them plus 10 who do not. (a) Which of demographic parity, equal opportunity, equalized odds and predictive parity hold or fail? Compute the rates. (b) Compute the probability that an applicant who meets the standard is selected in each group and explain what this shows. (c) Explain what individual fairness would require, what it needs, and how the tool could be revised.

**Points:** 5

**Rubric (1 point each):**

1. Shows demographic parity holds (0.30 in each group) and computes false-positive rates of 0 (X) and 10/80 = 0.125 (Y) and precisions of 1.00 and 0.67, so equalized odds and predictive parity fail.
2. Computes that a qualified applicant is selected with probability 0.60 in X (30/50) and 1.00 in Y (20/20), the true-positive rates, so equal opportunity fails and equally qualified people face different chances even though group selection rates are equal.
3. Explains that parity is an aggregate property blind to who is selected within a group; here it is achieved by passing over qualified applicants in one group and admitting unqualified ones in the other.
4. States that individual fairness would require similar (equally qualified) applicants to be treated similarly, which needs a similarity metric specifying the relevant qualifications, and that the tool violates it.
5. Proposes a revision, such as one rule applied to everyone based on qualification, accepting the group selection rates that result or addressing disparities upstream, and notes this trades demographic parity for individual consistency, a value choice.

**Source:** Beyond group metrics: individual fairness

## ES-ch07.15

A team wants to reduce a gap in true-positive rates between two groups in a trained lending model. Describe one pre-processing, one in-processing and one post-processing approach, giving a concrete technique for each, what each needs (data, access to the group attribute, retraining) and a main limitation. Then explain what none of these methods can fix, and how you would choose among them.

**Points:** 5

**Rubric (1 point each):**

1. Pre-processing: a technique that changes the training data (reweighting, resampling, relabeling or transforming features), which needs group labels at training time and whose limitation is that it works indirectly and may not hit the target metric.
2. In-processing: a technique that changes the training objective (a fairness penalty or constraint, or adversarial debiasing), which needs retraining and control of the training code, with a usual accuracy trade-off.
3. Post-processing: a technique that adjusts decisions on a frozen model (group-specific cutoffs or score adjustment), which needs the group attribute at decision time and invites objections that equal scores get different decisions.
4. States that none can fix mismeasured or biased labels, missing data or structural conditions upstream of the data, and none can satisfy all fairness criteria at once when base rates differ; they implement a chosen criterion.
5. Gives selection factors: legal limits, access to the model and data, the target criterion, acceptable accuracy loss and auditability, followed by evaluation by group with uncertainty before and after, and documentation of trade-offs.

**Source:** The toolkit and what it cannot do
