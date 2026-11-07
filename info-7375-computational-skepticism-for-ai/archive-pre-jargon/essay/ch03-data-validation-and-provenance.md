# Chapter 3: Data validation and the epistemic frame of a dataset

## ES-ch03.1

A data team builds a modeling table by joining three source systems on a shared identifier. An automated report on the result shows no missing values, sensible histograms and no outliers. After deployment, the model performs noticeably worse for one customer segment. Explain how a table with no empty cells can still misrepresent the population it is meant to describe, describe the check that would have exposed the problem, and say what that check cannot tell you.

**Points:** 5

**Rubric (1 point each):**

1. Explains that rows excluded before or during assembly (by a join, filter or gap in a source) are absent rather than blank, so cell-level checks such as missing-value counts have nothing to flag.
2. Explains that the excluded rows need not be random: if they concentrate in one segment (for example because of inconsistent identifiers), the table under-represents that segment and the model is trained on a different population from the one it serves.
3. Proposes comparing row counts at every join, filter or deduplication step (any name for the check is acceptable, for example row reconciliation or a count audit), including counts per segment before and after.
4. States that the expected count has to come from outside the file (documentation, source systems or the business definition of the population), because a count is meaningful only against what was supposed to be there.
5. States the limits: reconciliation shows that rows are missing and where, not why; it cannot show that the surviving rows are accurately measured, or that populations absent from every source are covered.

**Source:** Reconstructing the epistemic frame — a working procedure

## ES-ch03.2

Two tables, orders and customers, will be joined on customer_id and the result used to train a model. Specify the audit report you would require before anyone uses the joined table: what it measures (including whether any losses are evenly spread across groups), what would trigger a flag and why, and what must be decided in advance about duplicate keys. Then say what the audit cannot establish even if every check passes.

**Points:** 5

**Rubric (1 point each):**

1. Reports key uniqueness in each table and requires a decision in advance on whether duplicate keys are an error or an intended one-to-many relationship, because duplicate keys multiply rows.
2. Reports unmatched keys on both sides (orders with no customer, customers with no order), since the two directions of loss have different meanings.
3. Reports row counts before and after for the chosen join type and requires any difference to be explained (an inner join drops unmatched rows, a left join keeps them with blanks).
4. Reports drop rates per group (region, period, segment) and flags on the worst group or on divergence from the overall rate, justifying this by the fact that a small overall loss can hide a large loss in a subgroup.
5. States the limits: passing shows only that the join is consistent with its inputs; it does not show that the sources were complete, that matching keys refer to the same entity, or that the values are accurate, which needs external expected counts and domain knowledge.

**Source:** Reconstructing the epistemic frame — a working procedure

## ES-ch03.3

A company runs an opt-in poll on its own website and finds that 82% of respondents say they would buy a new product. It wants to announce that '82% of consumers would buy it'. Using the ideas of target population, sampling frame and self-selection, critique the claim. Explain whether collecting more responses or weighting respondents by age and income would fix it, and say what evidence would make the claim more credible.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the target population (all consumers), the frame (people who visit the site and see the poll) and the respondents (those who choose to answer), identifying coverage and self-selection as separate gaps.
2. Explains that those who visit and answer are likely more interested in the company and product than typical consumers, so the bias is tied to the outcome and has a likely direction (upward).
3. Explains that more responses from the same process reduce random error but not systematic bias, so a larger sample gives a more precise wrong answer.
4. Explains that weighting by observed variables such as age and income corrects composition only if respondents resemble non-respondents within each weighting cell; it cannot correct selection on interest itself and it increases variance.
5. Proposes stronger evidence: a probability sample from a frame that covers the target population, follow-up of non-respondents with response rates reported, and attention to the gap between stated intention and actual purchase.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.4

A dataset of 20,000 loan applicants has an income column with 18% of values blank. A missingness plot shows that blanks are far more common among applicants under 25, while the blank rate does not differ noticeably by region or loan size. (a) Which of MCAR, MAR and MNAR does this pattern rule out, which would you adopt as the working assumption, and why can the pattern not settle the question? (b) Describe a handling strategy that fits your answer and one that would bias the results. (c) What would you do to probe the possibility of MNAR?

**Points:** 5

**Rubric (1 point each):**

1. Defines the mechanisms (MCAR independent of everything, MAR dependent on observed data, MNAR dependent on the missing value itself) and states that dependence on age, an observed variable, rules out MCAR and makes MAR the natural working assumption, with MNAR still possible.
2. Explains that the observed data cannot distinguish MAR from MNAR, because whether blanks depend on income itself (within age groups) involves values that were not recorded, so the assumption must be argued from how income was collected.
3. Proposes a handling strategy consistent with MAR, such as multiple or model-based imputation using age and other predictors (or analysis stratified by age), with the uncertainty carried through to the results.
4. Names a biased alternative, such as dropping all blank rows or filling with the overall mean, which ignores that missingness depends on age, distorts the under-25 group and shrinks variance.
5. Describes MNAR probes: ask the data owner how income was collected and who skips it, compare with an external source for a subsample, follow up on a sample of non-responders, and run a sensitivity analysis under different assumptions about the missing incomes.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## ES-ch03.5

A team must treat a numeric predictor that has 15% blank values before fitting a regression. They are choosing among (i) dropping rows with any blank, (ii) filling blanks with the column mean, and (iii) multiple imputation. Compare the three: what each assumes about why values are missing, what each does to the mean, the spread, relationships with other variables and the reported uncertainty, and when you would choose each. Say what you would report to readers.

**Points:** 5

**Rubric (1 point each):**

1. States that dropping rows (complete-case analysis) is unbiased under MCAR but loses data and precision, and can be biased otherwise, for example when missingness depends on the outcome (in a regression) or on the missing values or related variables (for estimates such as means).
2. States that mean filling assumes MCAR, leaves the mean unchanged but shrinks the variance and attenuates correlations and coefficients, and gives standard errors that are too small because filled values are treated as observed.
3. States that multiple imputation assumes MAR given the variables in the imputation model, draws several plausible values, analyzes each completed dataset and pools the results so the uncertainty includes imputation variability.
4. States that none of the three is sufficient if the mechanism is MNAR, which calls for sensitivity analysis and domain reasoning, and gives an explicit rule for choosing among them (for example by the assumed mechanism, the share missing and the availability of informative auxiliary variables).
5. Specifies reporting: the share missing in each column, the assumed mechanism and why, the method used, how many rows were affected, and results under at least one alternative treatment.

**Source:** Missing data and imputation

## ES-ch03.6

A team trains a content-moderation classifier on 50,000 posts, each labeled once as harmful or not harmful by a crowd worker. In a pilot, two workers independently label the same 500 posts and obtain a Cohen's kappa of 0.55. Explain what this number says, how the disagreement should affect the way the team trains the model and, especially, how it evaluates it, what steps they should take to improve label quality, and what they should report alongside the results.

**Points:** 5

**Rubric (1 point each):**

1. Explains that kappa measures agreement beyond what chance would produce and that 0.55 is only moderate, so a substantial share of labels are inconsistent.
2. Notes that disagreement can come from ambiguous guidelines, genuinely ambiguous posts, annotator error or legitimate differences in judgment, and that telling these apart requires reading the disagreements, not just the statistic.
3. Explains the evaluation consequence: random noise in single test labels depresses measured accuracy and compresses differences between models, so the measured score is capped by label reliability, and test labels deserve more care than training labels.
4. Names training and labeling remedies: several labels per item with aggregation or soft labels, adjudication of disagreements, clearer guidelines with examples, annotator training and gold-standard check items.
5. Specifies reporting: agreement by category and annotator group, the guideline and annotator pool used, and uncertainty in the evaluation, with attention to whether disagreement is systematic for particular groups or topics.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.7

A model that predicts hospital readmission reports 0.98 AUC on its held-out set, while published models for the same task reach about 0.70. Describe at least four distinct ways in which the evaluation could be inflated by information unavailable in deployment or by overlap between training and test data. For each, give a check that would confirm or rule it out, and say what you would conclude if the score drops sharply once the problem is fixed.

**Points:** 5

**Rubric (1 point each):**

1. Gives a first leakage mechanism with a check that confirms or rules it out; for example target leakage, a feature recorded after or caused by the outcome (such as a billing code, lab result or diagnosis recorded during the readmission stay), checked by comparing each feature's timestamp with the prediction time and ablating or inspecting the most influential features.
2. Gives a second, different mechanism with a check; for example entity overlap, where several rows per patient fall on both sides of the split, checked by counting shared patient identifiers and re-splitting by patient.
3. Gives a third, different mechanism with a check; for example duplicates and near-duplicates across the split, checked by exact and fuzzy matching between test and training rows or nearest-neighbor distances.
4. Gives a fourth, different mechanism with a check; for example procedure leakage (scaling, imputation, feature selection or target encoding fitted on all data before splitting, or hyperparameters tuned on the test set), checked by reading the pipeline order and confirming the test set is used once, or time leakage from a random split of temporal data, checked by a split in which training precedes testing.
5. Concludes that a sharp drop in the score once the problem is fixed means the original figure was an artifact and the lower number is the credible estimate.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.8

A school district builds a model to identify students who need extra academic support. Because 'need' is hard to measure, the training label is whether the student received a failing grade the next term. Explain the difference between a measurement and the construct it stands for, give at least two ways this label can diverge from need, describe how you could test the size of the gap, and say what high accuracy on the label does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the construct (need for support) from the recorded measurement (a failing grade) and says the measurement is shaped by more than need.
2. Gives a divergence in which students who need support are labeled 0, for example students who struggle but pass or who are already receiving support.
3. Gives a divergence in which the label is 1 for reasons other than need for academic support, or in which the relationship between need and label differs across schools or groups.
4. Describes a test of the gap: compare the label with an independent measure of need (assessments, counselor review of a sample) and compare agreement by school or group.
5. States that high accuracy shows the model predicts the proxy well, not that the proxy measures need, and that acting on it can reproduce existing grading patterns; suggests multiple indicators, human review or redefining the label.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.9

A fraud model was trained on transactions from 2019 to 2021 and deployed in 2024, and its alert precision has been declining. Explain the assumption behind training on that window, distinguish covariate shift, concept drift and a change in the base rate, say how each can be detected, and propose a monitoring and retraining plan, including a difficulty in getting labels to evaluate the live model.

**Points:** 5

**Rubric (1 point each):**

1. States the assumption that the process generating future data resembles the process that generated the training window, and that a dataset is a snapshot of one period, not a permanent description.
2. Distinguishes covariate shift (input distribution changes, detectable without labels by comparing feature distributions), concept drift (the input-output relationship changes, seen as lower performance on labeled data) and base-rate change (prevalence of fraud shifts, detected from the rate of labeled fraud, the alert rate or the score prevalence over time).
3. Proposes an operational monitoring plan: tracking by segment, with thresholds that trigger an investigation, and an owner or review schedule.
4. Identifies the label difficulty: fraud labels arrive late (for example through chargebacks) and exist mainly for transactions that were flagged or investigated, so live performance is measured with delay and selection bias; mitigates with audited random samples.
5. Proposes a retraining plan: scheduled and triggered retraining on recent data, validation that trains on earlier periods and tests on later ones, and recording the training window with each model version.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.10

A data engineer reports: 'The data passed validation. Every column has the right type, no value is null, and all values are within their allowed ranges.' Explain why this does not establish that the data are correct, give four concrete kinds of error that can pass such checks, and describe the additional checks that would find them.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes validity (conforming to declared formats and ranges) from correctness (corresponding to what actually happened), and says schema checks test only the former.
2. Gives sentinel or default values (0, -999, 1900-01-01) that are valid in type and range, found by looking for spikes in frequency tables and checking the meaning of special values.
3. Gives unit, scale or encoding mismatches between sources (kilograms and pounds, cents and dollars, time zones), found by comparing distributions by source.
4. Gives cross-field, temporal or duplicate inconsistencies (discharge before admission, totals that do not add up, stale or repeated records), found by relational rules and duplicate checks.
5. Gives plausible-but-wrong entries or missing populations, found by tracing sampled records to their source, comparing with an independent source and running checks per group.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.11

A lender wants to train a default-prediction model. Repayment outcomes exist only for applicants who were approved under an old scoring rule, but the new model will score every applicant. Explain what is wrong with training and evaluating on the approved applicants alone, and describe at least three ways the lender could reduce the problem, including what each one assumes or costs, and say what you would claim about the model and what you would monitor after launch.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the training sample was selected using a variable related to the outcome, so the model learns relationships only within the approved range and the approved default rate is not the default rate of applicants.
2. Explains that evaluation on approved loans says nothing reliable about the rejected region, where the model is extrapolating, so reported accuracy cannot be assumed to hold for the full applicant pool.
3. Notes that the selection is known and observable (the old score), so within the approved range reweighting or modeling on that score can correct for it, but if approval followed a fixed cutoff there are no approved applicants in the rejected region to reweight toward, so statistical adjustment alone cannot recover outcomes that were never observed.
4. Names remedies with their price or assumption: randomly approving a small share below the cutoff (costly, but unbiased), reject-inference methods (rest on untestable assumptions), external performance data on rejected applicants, bounds or sensitivity analysis.
5. Says that, whatever is done, the model's claims should be limited to the population it was validated on, and its performance monitored after launch, particularly on applicants who would previously have been rejected.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.12

Your team inherits a training table from another group. One column, customer_value, has no blanks and a clean distribution, and the documentation says only that it was 'computed upstream'. Describe the questions you would ask about this column before using it as a model input, what you would do if the source systems cannot be reached, and how a datasheet for the table would help the next team.

**Points:** 5

**Rubric (1 point each):**

1. Asks what produced the column: a raw measurement or the output of a model or formula, who built it, from which inputs, parameters and version.
2. Asks whether information that exists only at or after the outcome time went into it, and what time window defined it, so its availability at prediction time can be checked.
3. Asks about future change: who owns the upstream computation and whether it can be changed without notice, how its assumptions could drift, and what happens to the model if it changes silently.
4. If the sources are unreachable, records the opacity as a finding, treats the column as unverified, tests sensitivity by modeling with and without it, and checks its behavior by group and over time.
5. Explains that a datasheet records how the data were produced, processed and meant to be used (for example motivation, composition, collection, preprocessing, uses and maintenance), so the next team can see what was assumed.

**Source:** Hidden assumptions that hide in plain sight

## ES-ch03.13

You present a data validation report to a deployment review board. The automated exploratory report is clean: no missing values, reasonable distributions, no outliers. Your own investigation found that the training data include only customers who completed onboarding, while the deployed model will also score customers who abandoned onboarding partway. A board member asks, 'The report is clean, so why is that not enough to approve?' Write the response you would give, including what you are and are not claiming and what evidence or changes you would ask for.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the clean report shows the recorded rows are well formed and plausible, not that they represent the population on which the model will run.
2. Names the selection gap: completers are a filtered subset, abandoners may differ in features and outcomes, so performance on them is untested and could differ, possibly for the worse.
3. Sizes, or asks for, the abandoned segment's share of deployment decisions and the cost of errors there, so the risk is sized instead of assumed.
4. Asks for evidence or a change: label and evaluate a sample of abandoners (for example in a pilot or shadow mode), or restrict the model's scope so those customers are routed to review, with monitoring by segment.
5. Lists what was not checked (coverage of the deployment population, label validity) and gives a conditional recommendation, not a bare yes or no.

**Source:** Reconstructing the epistemic frame — a working procedure

## ES-ch03.14

An engineer proposes giving an AI coding assistant read access to the source databases and letting it carry out the whole data audit for a new modeling project, including writing the dataset documentation. Decide which parts of a data audit you would delegate with light checking, which you would delegate but verify, and which you would keep with a human, giving reasons based on how errors in each part would show up. Respond to the objection that a sufficiently capable assistant could do all of it.

**Points:** 5

**Rubric (1 point each):**

1. Places mechanical, checkable computations (row counts, type and range checks, missingness tables, histograms, outlier flags, duplicate counts) in the light-checking category, because errors show in the output and rerunning is cheap; a different placement defended by how errors would show up also earns credit.
2. Places interpretations (why values are missing, whether a distribution is normal for the domain, suggested imputation, explanations of anomalies, drafts of documentation) in the verify category, since they read plausibly but depend on collection context that must be confirmed with data owners or tests; a different defended placement also earns credit.
3. Keeps with a human the decisions about what the dataset is supposed to represent, what the expected counts are, which populations matter and what risk is acceptable, which depend on purpose and stakes and not on computation; a different defended placement also earns credit.
4. Notes that fluent documentation can look complete without containing information the human did not supply, so style is not evidence of correctness.
5. Answers the objection by separating capability from verification: access to systems does not reveal undocumented upstream decisions, the intended population or the stakes, independent checking remains needed, and the delegable set may grow as tools improve.

**Source:** Strategic delegation in EDA

## ES-ch03.15

A validation report for a tabular dataset consists of histograms of each numeric column, a table of missing-value counts, a correlation heatmap of the numeric columns, and a line chart of record counts by month. For each of these four, explain what it can reveal and one specific thing it cannot. Then explain why a heatmap is a poor way to judge whether a correlation of 0.43 differs from 0.51, and what you would use instead.

**Points:** 5

**Rubric (1 point each):**

1. Histograms can reveal shape, spikes at sentinel values, impossible values and bimodality, but cannot explain why a shape arises or show which rows are absent or how the sample was selected.
2. Missing-value counts reveal blanks per column but cannot reveal rows excluded before the file existed, or the mechanism (MCAR, MAR or MNAR) that produced the blanks.
3. A correlation heatmap reveals strong linear association but misses nonlinear dependence (y = x^2 over a symmetric range gives a correlation near zero), can be driven by outliers and says nothing about causation.
4. A line chart of record counts reveals gaps, drops and level shifts, but cannot identify the cause (outage or real change) or the affected subgroup without breaking the counts down by source or group.
5. Explains that color intensity is decoded less accurately than position along a common scale, so small differences are hard to judge, and that a heatmap shows no sample size or confidence interval, so whether 0.43 differs from 0.51 depends on n; uses printed values with confidence intervals, or a dot chart with error bars, instead.

**Source:** A chart is an argument — and the argument is in the encoding
