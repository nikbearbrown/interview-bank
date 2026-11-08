# INFO 7375 Computational Skepticism: Predict-the-Prompt exam (PILOT DRAFT)

**Status: draft for Bear to look at. Not run on students. Not committed.** Built 2026-11-08.

## How this exam works

Every question shows a prompt (or a plan) and asks what an AI analyst will do. The answer key is **not an opinion**: each prompt was sampled 10 times and the key is the observed frequency of each feature in those 10 plans. Features are grouped into bands: **LIKELY** (7 to 10 of 10), **PLAUSIBLE** (2 to 6 of 10), **UNLIKELY** (0 or 1 of 10).

All prompts have the same shape, and only the final "Your job" phrase changes between versions of a prompt:

> You are a data analyst on a small team. Write the analysis plan for the task below. Format: a numbered list of at most 8 steps, one or two sentences each, no code, no preamble, no closing remarks.
> Task: *(a short fixed dataset description)* Your job: **(the phrase that varies)**.

The "plans" are numbered analysis plans written by `claude-sonnet-5-5` run as a **sub-agent** (not an agent harness: no tools, no data, no iteration). The key is true for that model, that format, on 2026-11-08. It is a statement about what the model does, not about what a good analyst does. See `KEY-AND-RUNS.md` for configuration, feature definitions and coder agreement.

Items marked **[behavioral]** key on a habit of the model rather than something that follows from the words, and count half. Everything else is **semantic**: it follows from what the course vocabulary means.

Answer keys follow each question in a **KEY** block (strip these for a student copy). Plan ids like `F3B-06` mean family 3, variant B, run 06; the raw text is in `runs/F3.json`.

---

## 1. Matching: 4 prompts to 4 plans (4 points)

**Task (shared):** A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease.

Four prompts differ only in the final phrase. Four plans (X to Z, W), each written for a different one of the prompts. Match each prompt to its plan (1 point each).

- **Prompt 1:** Your job: collect more rows.
- **Prompt 2:** Your job: control for the confounder.
- **Prompt 3:** Your job: randomize coffee assignment.
- **Prompt 4:** Your job: check for a collider.

**Plan W**

> 1. Audit the data for completeness and plausibility, and confirm how and when each variable was measured.
> 2. Summarise coffee intake, covariates and heart disease incidence, and look at crude rates across coffee categories.
> 3. Create a causal diagram with smoking and age as confounders and exercise assessed as a confounder or mediator, so that the adjustment set is chosen on principle.
> 4. Fit the unadjusted logistic model, then the model adjusted for smoking, then the fully adjusted model, tracking how the coffee estimate moves.
> 5. Stratify on smoking status to verify the adjusted result holds within each group and to detect interaction.
> 6. Test robustness with propensity-score methods and non-linear terms for coffee dose.
> 7. Quantify potential unmeasured confounding and measurement error in self-reported smoking and coffee.
> 8. Report adjusted estimates with uncertainty, and state that even a well-adjusted observational result shows association, not proof that coffee causes heart disease.

**Plan X**

> 1. Begin by telling the researcher that collecting more rows improves precision but does not solve the confounding problem with smoking, so the collection should be designed carefully. Record this limitation in the project notes.
> 2. Examine the existing dataset: variable definitions, missingness, and the distribution of coffee, smoking, age and exercise. Identify which combinations are sparse.
> 3. Draft the collection protocol, mirroring the original variables and adding detailed smoking exposure, diet, alcohol and BMI. Make sure exposure is measured at baseline and the outcome is observed afterward.
> 4. Select the source of new records (another cohort, hospital or registry data, or a new recruitment) and obtain the necessary permissions.
> 5. Sample deliberately across smoking and coffee groups so the data contain enough non-smoking heavy coffee drinkers to separate the effects.
> 6. Validate and clean the new rows, compare them to the original sample, and combine them with a flag for origin.
> 7. Run an adjusted model, an analysis stratified by smoking status, and a check that results hold in both the old and new subsets.
> 8. Report the adjusted estimates with confidence intervals, say clearly that they show association rather than proven causation, and suggest follow-up designs that could test causality.

**Plan Y**

> 1. Be clear that I cannot randomize coffee assignment in already-collected observational data; the closest approach is statistical adjustment, and true randomization would require a new prospective trial.
> 2. Prepare the data: confirm outcome coding, define coffee categories, and handle missing values with a documented approach.
> 3. Specify a causal diagram where smoking drives both coffee drinking and heart disease, and age and exercise also act as confounders.
> 4. Compare baseline characteristics across coffee groups to demonstrate imbalance.
> 5. Estimate the coffee effect using a logistic regression adjusted for age, smoking and exercise.
> 6. Confirm with a second method, such as propensity score stratification, and examine results separately for smokers and never-smokers.
> 7. Assess robustness through an E-value, dose-response trend test and checks for reverse causation.
> 8. Report adjusted effect sizes with uncertainty and describe the findings as associations, listing residual confounding as the main limitation.

**Plan Z**

> 1. Construct a DAG with coffee as exposure and heart disease as outcome, adding age, smoking and exercise, and justify each edge from domain knowledge. Mark timing relative to exposure.
> 2. State the collider criterion (two arrows pointing into the same node) and list every variable that could be affected by both coffee and heart disease.
> 3. Classify smoking as a confounder given that it is suspected to drive both coffee and heart disease, and explicitly check the less likely reverse story in which it is an effect of both.
> 4. Classify exercise and age similarly, noting exercise may be a mediator or downstream of disease and so a potential collider if mishandled.
> 5. Inspect how participants were sampled and whether inclusion depended on both coffee habits and health, since that would create selection collider bias.
> 6. Fit crude, singly adjusted, and fully adjusted coffee-heart disease models and stratify by smoking, looking for patterns such as an association appearing only after conditioning.
> 7. Choose an adjustment set of true confounders only and run sensitivity analyses, including an E-value, on the result.
> 8. Report the findings on colliders, the final adjustment strategy, and the inherent limits of observational causal inference.

### KEY

Answer: Prompt 1 = Plan X, Prompt 2 = Plan W, Prompt 3 = Plan Y, Prompt 4 = Plan Z.

What separates them (observed in 10 plans per prompt, semantic features):

| Feature | control for the confounder | collect more rows | randomize coffee assignment | check for a collider |
|---|---|---|---|---|
| Adjusts for smoking (regression covariate, stratification, or matching) | 10/10 | 10/10 | 10/10 | 10/10 |
| Draws a causal diagram (DAG) or lists causal assumptions explicitly | 9/10 | 0/10 | 10/10 | 10/10 |
| Proposes enlarging the sample or notes sample size / power / narrower confidence intervals | 0/10 | 10/10 | 0/10 | 0/10 |
| Proposes a randomized experiment / randomized assignment as the design | 0/10 | 4/10 | 6/10 | 0/10 |
| Names a collider or warns that conditioning on some variables can introduce bias | 3/10 | 0/10 | 0/10 | 10/10 |

Backing plans: control for the confounder -> F3A-09 (features present: abf); collect more rows -> F3B-06 (features present: ac); randomize coffee assignment -> F3C-06 (features present: abdf); check for a collider -> F3D-06 (features present: abef).

Caution for the instructor: prompts 'control for the confounder' and 'randomize coffee assignment' share the same profile except randomization (0/10 vs 6/10). The matching rests on that one feature, so the plan chosen for 'randomize' is one that shows it (F3C-06). Weak pair; swap if you want a cleaner item.

---

## 2. Prompt to most likely plan: multiple choice (2 points each)

For each prompt, choose the plan that the model is most likely to write. Each option is a real plan the model wrote for a different version of the prompt.

### Q2.1

**Task:** A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease. Your job: **collect more rows**.

**Option A**

> 1. Clean and check the data, covering missing values, outliers, and variable coding, and verify that coffee was measured before disease onset.
> 2. Present descriptive tables comparing coffee drinkers and non-drinkers on smoking, age and exercise, and heart disease rates by group.
> 3. Specify a causal model before running regressions, treating smoking as the primary confounder, age as another, and deciding with the researcher whether exercise should be adjusted for.
> 4. Run a crude logistic regression of heart disease on coffee, then add smoking, age and exercise to obtain the adjusted estimate.
> 5. Compare crude and adjusted odds ratios to show how much confounding by smoking explained the raw association.
> 6. Examine smoking-specific effects through stratified analysis and an interaction test, and explore dose-response shape.
> 7. Conduct sensitivity analyses for unmeasured confounding, including an E-value, and a second estimator such as weighting for robustness.
> 8. Report results with confidence intervals and state the limitations plainly: adjustment for measured confounders cannot establish causation from observational data.

**Option B**

> 1. Specify the causal structure in a DAG containing coffee, heart disease, age, smoking and exercise, justifying each arrow and recording which variables precede the exposure.
> 2. Apply the collider definition (a node with two incoming arrows) to find any variable caused by both coffee and heart disease or by their causes.
> 3. Evaluate smoking: it is suspected to affect both coffee and heart disease, so it is a confounder to be adjusted for; check that coffee and heart disease do not both cause smoking.
> 4. Evaluate exercise and age, labelling exercise a possible mediator or collider if it follows coffee and disease risk, and age a confounder.
> 5. Check the sampling and inclusion process for selection on both coffee use and health, which would act as a hidden collider.
> 6. Run crude, singly adjusted, and smoking-stratified models for coffee and heart disease, watching for associations that appear or reverse only after conditioning.
> 7. Use the DAG to pick an adjustment set limited to confounders, and verify with sensitivity analyses including alternative covariate sets and an E-value.
> 8. Report the collider findings, the justified adjustment, and the limits of causal claims from observational data.

**Option C**

> 1. Explain that the requested step, randomizing coffee assignment, cannot be done because participants already self-selected their coffee habits; I will use observational causal inference methods instead.
> 2. Define variables and cohort: exposure is daily coffee, outcome is heart disease within 10 years, covariates are age, smoking and exercise; document missing data.
> 3. Create a DAG and list the assumptions needed for a causal reading, mainly no unmeasured confounding and correct model form.
> 4. Produce descriptive tables and plots of coffee intake against smoking, exercise and age to reveal confounding structure.
> 5. Fit logistic regression models, first unadjusted and then adjusted for all three covariates, and compare how the coffee estimate changes.
> 6. Apply propensity score weighting or matching as an alternative and verify standardized mean differences fall below 0.1.
> 7. Perform stratified analyses by smoking status and sensitivity analysis for unmeasured confounding.
> 8. Communicate results as adjusted associations with confidence intervals, and be explicit that these data cannot prove coffee causes heart disease.

**Option D**

> 1. Restate the goal so the team is aligned: more rows are being collected to support the question of whether coffee causes heart disease, and the new data must address smoking confounding rather than only add volume. Note that adding rows to a confounded dataset leaves the bias unchanged.
> 2. Review the current dataset for data quality, missing values, how coffee intake was self-reported, and follow-up completeness over the 10 years. List the gaps the new rows should fill.
> 3. Define a data collection protocol identical to the original, covering the same eligibility, the same coffee measurement, the same outcome definition and the same follow-up length. Add detailed smoking history fields (never, former, current, pack-years).
> 4. Identify and approach sources for additional adults, such as another cohort study, health records or a new recruitment drive, and obtain ethics and data-use approvals.
> 5. Target a sample that includes enough non-smoking coffee drinkers and enough smoking non-coffee drinkers, since those groups break the link between the two exposures.
> 6. Clean and harmonize the new rows, then merge with the original 5,000 and compare the two groups on baseline characteristics.
> 7. Fit a logistic or Cox regression with coffee as the exposure and age, smoking and exercise as adjustments, and repeat within smoking strata. Check whether results are consistent across the original and new rows.
> 8. Report the adjusted association with uncertainty and clearly describe the limits: residual confounding and reverse causation remain, so causal claims should be hedged.

### KEY

**Answer: Option D** (the plan written for this prompt).

Deciding feature: *Proposes enlarging the sample or notes sample size / power / narrower confidence intervals* (semantic). Frequency across 10 plans per prompt version: A (control for the confounder): 0/10; B (collect more rows): 10/10; C (randomize coffee assignment): 0/10; D (check for a collider): 0/10.

Options: Option A = F3A-10 (written for 'control for the confounder'); Option D = F3B-02 (written for 'collect more rows'); Option C = F3C-05 (written for 'randomize coffee assignment'); Option B = F3D-09 (written for 'check for a collider').
Backing plans for the key feature: F3B-01, F3B-02, F3B-03, F3B-04, F3B-05, F3B-06, F3B-07, F3B-08, F3B-09, F3B-10.


### Q2.2

**Task:** A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025. Your job: **check for label shift**.

**Option A**

> 1. Define success: decide whether fraud prevalence in 2025 differs from 2023 enough to matter, under the label-shift assumption that P(x|y) is unchanged. 2. Estimate the 2025 fraud rate from the two labeled weeks with an interval and compare it against the 2023 rate. 3. Test representativeness of the labeled window by comparing its amount, merchant category, device type, and country mix to the unlabeled 2025 transactions, and think about seasonality in early January. 4. Audit the labels themselves: chargeback and investigation lag may mean the two-week window is under-confirmed, so look at 2023 to learn how long confirmation takes and what share is eventually found. 5. Apply a label-shift estimator to the full unlabeled 2025 set, using the model's score outputs and 2023 holdout error rates, to get an estimate of prevalence for the whole year and compare with the labeled-window rate. 6. Verify the invariance assumption where possible by comparing class-conditional feature distributions between years on the labeled data, and check for covariate shift or new fraud tactics separately. 7. Assess impact by recomputing precision, recall, and calibration on the labeled window, then project them under the estimated 2025 prevalence with importance weights and see if the threshold needs changing. 8. Present the estimated shift, intervals, assumptions, and recommendations, including a plan for more labels and periodic monitoring.

**Option B**

> 1. Split the problem: what can be checked without labels (inputs, scores) and what needs labels (accuracy, concept drift), given only two labeled weeks.
> 2. Sanity-check feature encodings and distributions for pipeline changes between years.
> 3. Compute PSI and KS or chi-square per feature between 2023 training data and 2025, and flag categories absent from training.
> 4. Compare score histograms and alert volume between periods, using matched calendar windows.
> 5. Fit a domain classifier to find jointly shifted features.
> 6. Score the labeled fortnight: PR-AUC, recall at the operating threshold, calibration, with bootstrap intervals.
> 7. Assess whether those two weeks are typical, and slice by country, device type and merchant category.
> 8. Report findings with confidence levels and recommend sampling and labeling more 2025 data before any retraining decision.

**Option C**

> 1. Specify the hypothesis: the joint distribution of amount, merchant category, device type and country in 2025 differs from 2023, and define what size of difference would be material for the model.
> 2. Profile both datasets, reconcile feature definitions, and note external events (new product launches, regional expansion) that might legitimately change the mix.
> 3. Run univariate tests per feature and report PSI, KS or chi-square, and visual comparisons, prioritizing practical magnitude over significance.
> 4. Perform a multivariate check with a domain classifier, and complement it with a two-sample test on embeddings or pairwise combinations such as country by device.
> 5. Evaluate whether 2025 inputs fall outside the model's training support by checking unseen categories and amounts beyond the 2023 range.
> 6. Compare predicted fraud rate and score histograms between years to see whether the shift changes model behavior.
> 7. Assess performance on the labeled first two weeks, comparing with 2023 validation metrics with bootstrapped intervals, and explicitly treat this as weak evidence because of the small number of positives.
> 8. Conclude with whether covariate shift is present, how severe, what cannot be determined without more labels, and recommended follow-up such as stratified labeling of drifted segments.

**Option D**

> 1. Restate the task: detect whether the relationship between transaction features and fraud has changed since 2023, with the key constraint that only the first two weeks of 2025 have confirmed labels.
> 2. Verify the 2025 labels and the time windows: confirm the definition of confirmed fraud, estimate how many frauds are likely still undiscovered even in those weeks, and note the sample size.
> 3. Obtain a comparable 2023 reference window and compute the model's metrics there, so the comparison controls for time of year.
> 4. Measure the 2025 labeled performance (PR-AUC, recall at the production threshold, false-positive rate) and compare with the reference using confidence intervals.
> 5. Check calibration drift by comparing predicted probability vs observed fraud rate in score bins for both periods.
> 6. Analyze data-level drift on the full 2025 set: PSI per feature, new merchant categories or countries, shifts in device type mix, and shifts in the score distribution.
> 7. Determine whether any performance drop can be explained by input-distribution changes (reweighting analysis) or whether it persists, suggesting concept drift, and look at which segments drive it.
> 8. Communicate the result with its scope: conclusive only for early 2025, suggestive for later months, and propose labeled spot-checks of later periods.

### KEY

**Answer: Option A** (the plan written for this prompt).

Deciding feature: *Compares the overall fraud rate / class prior between years* (semantic). Frequency across 10 plans per prompt version: A (check for covariate shift): 0/10; B (check for concept drift): 4/10; C (check for label shift): 10/10; D (check for drift): 0/10.

Options: Option C = F5A-06 (written for 'check for covariate shift'); Option D = F5B-06 (written for 'check for concept drift'); Option A = F5C-06 (written for 'check for label shift'); Option B = F5D-06 (written for 'check for drift').
Backing plans for the key feature: F5C-01, F5C-02, F5C-03, F5C-04, F5C-05, F5C-06, F5C-07, F5C-08, F5C-09, F5C-10.

Note: 4 of 10 plans for 'concept drift' also compare fraud rates (F5B). The distractor from that prompt was chosen from the 6 that do not, so the item is solvable, but a careful student can say 'concept drift' produces the feature 40% of the time and 'label shift' 100%.


### Q2.3

**Task:** A telecom company wants a model that predicts which customers will cancel next month. You have one table of 2,000 customer rows (usage, plan, tenure, and whether the customer cancelled), collected over the last 18 months. Your job: build and evaluate a churn model, and **hold out the most recent 3 months as a test set**.

**Option A**

> 1. Define the outcome as cancellation in the coming month, and verify the data collection design to rule out leakage and to see whether customers repeat across rows.
> 2. Clean and profile the table, noting missingness, outliers, and the churn proportion.
> 3. Carry out exploratory analysis linking churn to plan, tenure, and usage, and derive helpful features.
> 4. Split data into training and a locked test set, using time order to simulate future prediction if dates exist.
> 5. Build baselines: a naive majority-class predictor and a logistic regression.
> 6. Train one or two more flexible models and cross-validate on the training set (stratified folds, or rolling-origin folds for time), fitting all preprocessing within each fold and tuning hyperparameters there.
> 7. Evaluate with imbalance-aware metrics (PR-AUC, recall, precision), assess calibration, and choose a threshold from retention costs.
> 8. Run the single final test evaluation, report results with intervals, and describe caveats and monitoring recommendations.

**Option B**

> 1. Verify the dataset: 2,000 rows, 18 months, unique customer identifiers, and what the cancelled column represents. Flag any columns that leak the outcome, such as cancellation reason or final-month usage of customers who had already left.
> 2. Carve out the last 3 months as the test set by date and leave it untouched. Never let random shuffling mix test-period rows into training.
> 3. Examine the training data for missing values, skew and outliers, and measure the churn rate, expecting an imbalanced target.
> 4. Construct features from usage, plan and tenure, and apply preprocessing inside a cross-validation pipeline so each fold fits its own imputers and scalers.
> 5. Compare a simple logistic regression, a decision tree or random forest, and a gradient-boosted model using expanding-window validation on the 15 training months. Prefer the simpler model unless the complex one clearly wins.
> 6. Judge models with PR-AUC, recall and precision at the chosen threshold, and calibration plots, as accuracy would reward predicting that nobody leaves.
> 7. After freezing the model, threshold and features, evaluate on the held-out months once. Report intervals and compare with the baseline and with the validation results.
> 8. Report findings and caveats plainly: the test window is short and has few churners, so conclusions are tentative. Recommend monitoring and retraining as more data arrives.

**Option C**

> 1. Define the problem and label: one row per customer, churn within the next month, and check that predictors reflect only what was known beforehand.
> 2. Split the data before doing anything else, holding out roughly 20% as a test set stratified on churn (or the most recent months, if timestamps exist), and treat it as off limits.
> 3. Inspect the training set for missing data, duplicates, odd values, and class imbalance, noting the overall churn rate.
> 4. Eliminate leakage candidates and create useful features from usage, plan, and tenure, wrapping imputation, scaling, and encoding in a pipeline fit on training folds.
> 5. Train a baseline and two or three candidate models, tuning with stratified cross-validation on the training data only, and keep the tuning budget small to limit overfitting to a 2,000-row sample.
> 6. Compare models on PR-AUC, recall and precision at several thresholds, and calibration, not accuracy.
> 7. Pick the final model and a threshold that matches the retention team's capacity and the cost tradeoff, then refit on the full training set.
> 8. Score the test set once, report with bootstrap confidence intervals, list the strongest predictors, and flag limitations including the short history and potential drift.

**Option D**

> 1. Frame the task precisely: predict next-month cancellation from pre-period features, one row per customer. Check class imbalance, missing values, duplicates, and potential leakage columns.
> 2. Run exploratory checks of churn against plan, tenure and usage, and clean obvious errors.
> 3. Choose metrics before looking at results: PR-AUC, precision and recall at the operating point, and a calibration plot, with accuracy only reported for context.
> 4. Establish baselines with a prior-only model and an L2 logistic regression.
> 5. Use nested cross-validation to avoid optimistic bias: stratified inner folds tune each model's hyperparameters, stratified outer folds score the tuned models, and every data transformation lives inside the training portion of each fold. Repeat the outer loop several times since the sample is small.
> 6. Compare the model families on identical outer splits and record the mean and spread of each metric, then pick the model that is best or simplest within the noise.
> 7. Inspect errors and drift: segment results by tenure and plan, and compare performance on early versus late months of the 18-month window.
> 8. Report the nested estimate with uncertainty, the threshold recommendation, the main drivers, and the limits of the sample, then refit the chosen configuration on all data.

### KEY

**Answer: Option B** (the plan written for this prompt).

Deciding feature: *Splits by time (train on earlier months, test on later months)* (semantic). Frequency across 10 plans per prompt version: A (hold out a test set): 0/10; B (cross-validate): 3/10; C (use nested cross-validation): 5/10; D (hold out the most recent 3 months as a test set): 10/10.

Options: Option C = F2A-05 (written for 'hold out a test set'); Option A = F2B-07 (written for 'cross-validate'); Option D = F2C-08 (written for 'use nested cross-validation'); Option B = F2D-06 (written for 'hold out the most recent 3 months as a test set').
Backing plans for the key feature: F2D-01, F2D-02, F2D-03, F2D-04, F2D-05, F2D-06, F2D-07, F2D-08, F2D-09, F2D-10.

Note: options A-type ('hold out a test set') and B-type ('cross-validate') have the same profile (see cut list), so the item keys on the time split, which only the 'most recent 3 months' prompt produces (10/10 vs 0 to 3/10).


---

## 3. Plausibility: likely, plausible or unlikely? (1 point; adjacent band 0.5)

For each prompt, say whether the statement about the plan is LIKELY (7+ of 10 plans), PLAUSIBLE (2 to 6) or UNLIKELY (0 to 1). Quote the phrase in the prompt that drives your answer.

**Q3.1.** Prompt: *"Your job: hold out the most recent 3 months as a test set"* (task: A telecom company wants a model that predicts which customers will cancel next month. You have one table of 2,000 customer rows (usage, plan, tenure, and whether the customer cancelled), collected over the last 18 months.)

Statement: {st}

**Q3.2.** Prompt: *"Your job: collect more rows"* (task: A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease.)

Statement: {st}

**Q3.3.** Prompt: *"Your job: collect more rows"* (task: A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease.)

Statement: {st}

**Q3.4.** Prompt: *"Your job: check the discrimination of the predicted probabilities"* (task: A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no).)

Statement: {st}

**Q3.5.** Prompt: *"Your job: validate the schema of the data"* (task: A bank received a CSV of 40,000 loan applications from a third-party data vendor to train a credit-scoring model. You have the file and a one-page data dictionary.)

Statement: {st}

**Q3.6.** Prompt: *"Your job: check for drift"* (task: A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025.)

Statement: {st}

**Q3.7.** Prompt: *"Your job: check the accuracy of the predicted probabilities"* (task: A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no).)

Statement: {st}

### KEY

| Q | Quoted phrase | Statement feature | Observed | Band | Type | Backing plans | Other versions of the prompt |
|---|---|---|---|---|---|---|---|
| 3.1 | "hold out the most recent 3 months as a test set" | Splits by time (train on earlier months, test on later months) | 10/10 | LIKELY | semantic | F2D-01, F2D-02, F2D-03, F2D-04, F2D-05, F2D-06, F2D-07, F2D-08, F2D-09, F2D-10 | A:0, B:3, C:5, D:10 |
| 3.2 | "collect more rows" | Adjusts for smoking (regression covariate, stratification, or matching) | 10/10 | LIKELY | semantic | F3B-01, F3B-02, F3B-03, F3B-04, F3B-05, F3B-06, F3B-07, F3B-08, F3B-09, F3B-10 | A:10, B:10, C:10, D:10 |
| 3.3 | "collect more rows" | Proposes a randomized experiment / randomized assignment as the design | 4/10 | PLAUSIBLE | semantic | F3B-01, F3B-05, F3B-07, F3B-09 | A:0, B:4, C:6, D:0 |
| 3.4 | "check the discrimination of the predicted probabilities" | Computes a calibration-specific number: ECE, Brier score, calibration slope/intercept, or Hosmer-Lemeshow | 0/10 | UNLIKELY | semantic | none | A:10, B:10, C:0, D:10 |
| 3.5 | "validate the schema of the data" | Asks where the data came from: who collected it, how, under what consent/licence, vendor sourcing | 0/10 | UNLIKELY | semantic | none | A:10, B:0, C:10, D:0 |
| 3.6 | "check for drift" | Trains a classifier to tell 2023 from 2025 rows, or estimates importance weights | 5/10 | PLAUSIBLE | semantic | F5D-02, F5D-04, F5D-06, F5D-08, F5D-10 | A:10, B:7, C:10, D:5 |
| 3.7 | "check the accuracy of the predicted probabilities" | Computes accuracy-style metrics (accuracy, confusion matrix, precision/recall) at a probability threshold | 0/10 | UNLIKELY | semantic | none | A:0, B:0, C:7, D:0 |

Two teaching points hidden in this section. Q3.2: 'collect more rows' still produces smoking adjustment 10/10, because the task text names the confounder: **the scenario drives the plan, the phrase shifts its emphasis**. Q3.7: 'check the accuracy of the predicted probabilities' produces **zero** accuracy-at-threshold steps: the model reads accuracy-of-probabilities as calibration (see predict-and-explain 6.2).

---

## 4. Feature forecasting: how many of 10 plans? (2 points; behavioral item 1 point)

Give a number from 0 to 10. Scoring: within 1 of the observed count = full credit; otherwise right band (LIKELY / PLAUSIBLE / UNLIKELY) = half credit; else 0.

**Q4.1.** Prompt: *"Your job: check the discrimination of the predicted probabilities"* (task: A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no).)

Of 10 plans, how many will include: *Reliability diagram / binning: groups patients by predicted probability and compares to observed readmission rate*?

**Q4.2.** Prompt: *"Your job: randomize coffee assignment"* (task: A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease.)

Of 10 plans, how many will include: *Proposes a randomized experiment / randomized assignment as the design*?

**Q4.3.** Prompt: *"Your job: check for concept drift"* (task: A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025.)

Of 10 plans, how many will include: *Compares the overall fraud rate / class prior between years*?

**Q4.4.** Prompt: *"Your job: check for drift"* (task: A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025.)

Of 10 plans, how many will include: *Trains a classifier to tell 2023 from 2025 rows, or estimates importance weights*?

**Q4.5.** **[behavioral]** Prompt: *"Your job: hold out the most recent 3 months as a test set"* (task: A telecom company wants a model that predicts which customers will cancel next month. You have one table of 2,000 customer rows (usage, plan, tenure, and whether the customer cancelled), collected over the last 18 months.)

Of 10 plans, how many will include: *Handles class imbalance or uses stratified splits*?

### KEY

| Q | Feature | Observed (of 10) | Band | Full-credit range | Type | Backing plans |
|---|---|---|---|---|---|---|
| 4.1 | Reliability diagram / binning: groups patients by predicted probability and compares to observed readmission rate | **5** | PLAUSIBLE | 4 to 6 | semantic | F1C-02, F1C-04, F1C-06, F1C-08, F1C-10 |
| 4.2 | Proposes a randomized experiment / randomized assignment as the design | **6** | PLAUSIBLE | 5 to 7 | semantic | F3C-01, F3C-02, F3C-04, F3C-06, F3C-07, F3C-09 |
| 4.3 | Compares the overall fraud rate / class prior between years | **4** | PLAUSIBLE | 3 to 5 | semantic | F5B-02, F5B-04, F5B-09, F5B-10 |
| 4.4 | Trains a classifier to tell 2023 from 2025 rows, or estimates importance weights | **5** | PLAUSIBLE | 4 to 6 | semantic | F5D-02, F5D-04, F5D-06, F5D-08, F5D-10 |
| 4.5 | Handles class imbalance or uses stratified splits | **5** | PLAUSIBLE | 4 to 6 | BEHAVIORAL | F2D-02, F2D-04, F2D-07, F2D-08, F2D-10 |

These are mid-band items on purpose: a feature the model produces 10 times out of 10 tests vocabulary, but only a mid-band feature tests whether the student can judge how strongly a phrase pulls. Caution: a count of 5 or 6 from 10 plans has a standard error near 1.6, so the full-credit range is about one standard error wide.

---

## 5. Attribution: which prompt wrote this plan? (2 points)

Given the plan, name the prompt most likely to have produced it (all four prompts share the same task). Give your reason in one sentence.

### Q5.1

**Task:** A telecom company wants a model that predicts which customers will cancel next month. You have one table of 2,000 customer rows (usage, plan, tenure, and whether the customer cancelled), collected over the last 18 months. Your job: ___

- Prompt A: hold out a test set
- Prompt B: cross-validate
- Prompt C: use nested cross-validation
- Prompt D: hold out the most recent 3 months as a test set

> 1. Examine the table to understand the churn label's timing, class balance, missing data, and any duplicates; confirm no column is recorded after cancellation.
> 2. Preprocess within a reusable pipeline: impute missing values, encode plan, scale usage variables, and create tenure and usage-trend features.
> 3. Specify metrics ahead of time: PR-AUC, recall at the top-k customers the retention team can contact, and calibration.
> 4. Train a baseline logistic regression and a majority-class dummy for comparison.
> 5. Apply nested cross-validation: the inner stratified loop searches hyperparameters for each candidate (logistic regression, random forest, gradient boosting), the outer stratified loop produces the performance estimate, and the whole pipeline is refit per fold to prevent leakage.
> 6. Compare candidates on the outer folds with paired differences and intervals; if differences are small, prefer the simpler model.
> 7. Test temporal robustness by checking how scores change when evaluation folds come from later months than training folds.
> 8. Summarize the final model's estimated performance, calibration, top drivers, and caveats, and refit on all 2,000 rows for use.

### Q5.2

**Task:** A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025. Your job: ___

- Prompt A: check for covariate shift
- Prompt B: check for concept drift
- Prompt C: check for label shift
- Prompt D: check for drift

> 1. Clarify what we are testing: whether P(fraud | features) has shifted from 2023 to 2025, distinct from changes in feature distributions or overall fraud rate, with labels available only for the first two weeks of 2025.
> 2. Audit the labeled 2025 window for number of positives, label maturity and seasonal peculiarities, since small or immature labels will inflate apparent performance changes.
> 3. Evaluate the model on a matched-season 2023 holdout to set the expected performance and its sampling variability.
> 4. Evaluate on labeled 2025 and compare metrics with uncertainty, including ranking quality, performance at the deployed threshold, and calibration.
> 5. Quantify covariate and score drift on all of 2025 data using PSI and distribution tests, plus a classifier that tries to tell 2023 from 2025 rows.
> 6. Disentangle causes: reweight 2023 to the 2025 feature distribution, compare observed vs expected performance, and check whether fraud base rate alone explains the changes.
> 7. Use proxy monitors for the unlabeled period such as alert rate, score distributions over time and chargeback arrivals, labeling them clearly as indirect evidence.
> 8. Report a verdict scoped to the evidence, noting that drift in the unlabeled months is unverified, and recommend a labeled audit sample.

### KEY

**Q5.1: answer C, 'use nested cross-validation'** (the true source is F2C-07). Nested cross-validation / an inner tuning loop appears in 10/10 plans for C and in 0/10 (A), 2/10 (B) and 0/10 (D) for the others. Likelihood ratio favours C over B 5 to 1; posterior (equal prior) about 83%.

**Q5.2: answer C, 'check for label shift' is the most probable source, but the true source is B, 'check for concept drift'** (F5B-09). Using the four semantic features: this plan compares feature distributions (a), trains a domain classifier (b), measures performance on the labelled 2025 weeks (c) and compares the fraud rate (d). Fraud-rate comparison appears in 10/10 label-shift plans, 4/10 concept-drift plans and 0/10 for 'covariate shift' and 'drift'; the domain classifier appears 10/10 (A), 7/10 (B), 10/10 (C), 5/10 (D). Likelihood for C is 1.0 x 1.0, for B 0.7 x 0.4 = 0.28, for A and D 0. Posterior (equal prior): C 78%, B 22%. Award full credit for C with a reason that cites the fraud-rate step, and ALSO full credit for B if the student shows the 22% reasoning; this item is meant to teach that attribution is a probability, not a verdict.

Backing plans: nested CV: F2C-01, F2C-02, F2C-03, F2C-04, F2C-05, F2C-06, F2C-07, F2C-08, F2C-09, F2C-10. Fraud-rate comparison under label shift: F5C-01, F5C-02, F5C-03, F5C-04, F5C-05, F5C-06, F5C-07, F5C-08, F5C-09, F5C-10; under concept drift: F5B-02, F5B-04, F5B-09, F5B-10.

---

## 6. Predict and explain (4 points each: 2 prediction, 2 mechanism)

Before seeing any plan, (a) predict which of the listed features the plan will contain and which it will not, and (b) explain **which word or phrase in the prompt** causes each difference you predict.

### Q6.1

**Task:** A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease. Your job: **collect more rows**.

Features to judge: (i) adjusts for smoking; (ii) draws a causal diagram or lists causal assumptions; (iii) proposes a larger sample or discusses power; (iv) proposes a randomized experiment.

### Q6.2

**Task:** A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no). Your job: **check the accuracy of the predicted probabilities**.

Features to judge: (i) reliability diagram / binning predicted vs observed; (ii) a calibration number (ECE, Brier, slope); (iii) accuracy or confusion matrix at a threshold; (iv) ROC / AUC.

### KEY

**Q6.1** observed: (i) 10/10 (ii) 0/10 (iii) 10/10 (iv) 4/10. For comparison with 'control for the confounder': (i) 10/10, (ii) 9/10, (iii) 0/10, (iv) 0/10. Backing: (i) F3B-01, F3B-02, F3B-03, F3B-04, F3B-05, F3B-06, F3B-07, F3B-08, F3B-09, F3B-10; (iii) F3B-01, F3B-02, F3B-03, F3B-04, F3B-05, F3B-06, F3B-07, F3B-08, F3B-09, F3B-10; (iv, 4/10) F3B-01, F3B-05, F3B-07, F3B-09.

Mechanism, full credit needs both halves: (1) smoking adjustment is **context-driven**: the task text says smoking is suspected of being associated with both, so the plan controls for it even though the prompt says to collect more rows; (2) the sample-size/power step is **phrase-driven** ('collect more rows') and the causal diagram is **phrase-driven** the other way: 'control for the confounder' calls up the causal vocabulary (diagram 9/10) and 'collect more rows' does not (0/10). Randomization is plausible (4/10), not likely. A student who predicts 'it will ignore smoking because the prompt only asked for more rows' loses the prediction points; a student who predicts a causal diagram loses them too.

**Q6.2** observed for 'accuracy of the predicted probabilities': (i) 10/10 (ii) 10/10 (iii) 0/10 (iv) 0/10. For 'calibration': (i) 10, (ii) 10, (iii) 0, (iv) 0. For 'discrimination': (i) 5, (ii) 0, (iii) 7, (iv) 10. Backing (i)+(ii) under 'accuracy': F1B-01, F1B-02, F1B-03, F1B-04, F1B-05, F1B-06, F1B-07, F1B-08, F1B-09, F1B-10.

Mechanism: the model reads *accuracy of the predicted probabilities* as **calibration**, because a probability is 'accurate' to the extent that events predicted at 30% happen about 30% of the time. The plan for 'accuracy' is the same as the plan for 'calibration' and for 'overconfidence' (reliability diagram and calibration number both 10/10, confusion matrix 0/10). Only 'discrimination' moves the plan to ROC/AUC (10/10) and a threshold metric (7/10). Full credit: predicts reliability diagram, no confusion matrix, and says the word *probabilities* decides it. A student who has memorised 'accuracy is not calibration' as a vocabulary fact will predict the confusion matrix and be wrong, which is exactly what this item is for: the model's reading is the *right* reading of that phrase, and the vague phrase in the prompt was the student's.

---

## 7. Minimal-edit repair (3 points, graded by running)

**Prompt as it stands:** A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no). Your job: **check the accuracy of the predicted probabilities**.

Observed: 10/10 plans build a reliability diagram and a calibration number; **0/10** compute accuracy or a confusion matrix at a threshold. You want a plan that reports **classification accuracy at a probability threshold**. Add or change **at most 12 words** to the prompt (do not delete the task description) so that at least 7 of 10 plans do.

### KEY and run protocol

**Reference edit (9 words, appended):** *"Report accuracy at a 0.5 threshold, not calibration."* Run result, 10 plans: accuracy/confusion matrix at threshold **10/10** (was 0/10); reliability diagram 0/10 (was 10/10); calibration number 0/10 (was 10/10). Plans: `runs/F1B_repair_demo.json`.

**Run protocol for grading a student edit:**
1. Check the edit is at most 12 words and the original task sentence is intact. If not, 0.
2. Run the edited prompt 10 times in 10 fresh contexts with the same sampler (here: a fresh sub-agent per batch, 10 separate attempts, `claude-sonnet-5-5`, no tools).
3. A blind coder (not told the student's edit) marks feature c ('accuracy-style metrics at a probability threshold') in each plan using the definition in `KEY-AND-RUNS.md`.
4. Score: **7 to 10 plans = 3 points; 4 to 6 = 1.5; 0 to 3 = 0.** Feature c must be present; the student need not suppress the calibration plan.
5. Cost: one batch plus one coding pass per student answer, about 150k tokens. For a class, grade a random 20% of edits by running, and pre-run the 5 most common edits.
6. The pass threshold is a prediction made *before* running: the student may also be asked to state the expected count, and gets the +0.5 bonus if within 1.

---

## 8. Scoring summary

| Section | Items | Points each | Total |
|---|---|---|---|
| 1 Matching | 4 pairs | 1 | 4 |
| 2 Most likely plan | 3 | 2 | 6 |
| 3 Plausibility | 7 | 1 | 7 |
| 4 Forecasting | 5 (1 behavioral at half) | 2 | 9 |
| 5 Attribution | 2 | 2 | 4 |
| 6 Predict and explain | 2 | 4 | 8 |
| 7 Repair | 1 | 3 | 3 |
| **Total** | | | **41** |

## 9. Items cut by the premise check

An item was cut when altered versions of the prompt produced the same feature profile (no semantic feature differing by 4 or more plans of 10). Full detail in `KEY-AND-RUNS.md`.

- **Calibration vs accuracy (family 1): cut.** 'calibration', 'accuracy of the predicted probabilities' and 'overconfidence' produced identical profiles (all semantic features within 0 plans of each other). The planned 'calibration vs accuracy' item cannot be keyed. Kept as predict-and-explain 6.2 and plausibility 3.7 *because* the failure is informative. Only 'discrimination' differs.
- **Hold out a test set vs cross-validate (family 2): pair cut.** The two prompts differ by at most 1 plan on every semantic feature. Both write a held-out test set plus k-fold tuning. Items use 'nested' and 'most recent 3 months' instead.
- **Provenance vs lineage (family 4): pair cut.** Identical profiles (10/10 on provenance questions, chain of custody and processing history for both). Provenance vs schema and schema vs lineage are separable.
- **Family 4 'validate the statistical distributions' vs 'validate the schema': weak.** They differ only in the checksum feature (0/10 vs 9/10); not used in any item.
- **Covariate shift vs concept drift (family 5): weak.** The two prompts differ on one feature only: fraud-rate comparison 0/10 vs 4/10. They are not used as a matching pair. 'covariate shift' vs 'label shift' is separable (0 vs 10) and used in 2.2 and 5.2.
- **Saturated features dropped from keys:** F4 c, d, f (10/10 in every version), F5 c (10/10 in every version), F1 e and f (identical in three of four versions). Features that every prompt triggers cannot discriminate prompts.
