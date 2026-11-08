# KEY-AND-RUNS: configuration, features, frequencies, coder agreement

Pilot built 2026-11-08. Everything here comes from the files in `runs/`.

## Configuration

| Item | Value |
|---|---|
| Model that wrote the plans | `claude-sonnet-5-5` (sub-agent, alias `sonnet`; each sub-agent reported that id) |
| How plans were requested | One fresh sub-agent per prompt version. It read the prompt from a text file, wrote **10 separate attempts** in one go, told not to compare attempts, and saved a JSON array with a single Write. No data, no code execution, no iteration. **This is a sub-agent plan, not an agent harness.** |
| Prompt template | "You are a data analyst on a small team. Write the analysis plan for the task below. Format: a numbered list of at most 8 steps, one or two sentences each, no code, no preamble, no closing remarks. Task: ..." See `spec/spec.py` |
| Date | 2026-11-08 |
| Runs | 5 families x 4 versions x 10 plans = **200 plans**. Plus 10 plans for the repair demo. F4 version A: the sub-agent returned 9 plans; the tenth is from a separate fresh sub-agent (`F4A-10`). |
| Sampling settings | Defaults of the sub-agent runtime. Temperature is not controllable here and was not recorded. |
| Coder 1 | `sonnet` sub-agent per family, blind to which prompt wrote each plan (ids shuffled, variant hidden), codes all 40 plans on binary features. |
| Coder 2 | Separate `sonnet` sub-agent per family, blind, recodes 8 of the 40 plans (2 per version, random). 40 plans = 20% of 200. |
| Key rule | Observed count out of 10: LIKELY >= 7, PLAUSIBLE 2 to 6, UNLIKELY <= 1. (Matches 70% / 20-70% / below 20%, on a 10-plan sample: 2/10 = 20% is PLAUSIBLE.) |

### Known limits (read before trusting a number)

1. **The 10 plans of a version come from one sub-agent context**, so they are not 10 independent draws; they may be more varied or less varied than 10 separate calls. Single-plan sub-agents cost about 70k tokens each (about 14M tokens for 200), so I batched. A full version should sample independently (API calls, not sub-agents).
2. **Coders are the same model family as the writer.** Both coders are `sonnet`; agreement shows consistency, not truth. A human spot check of the 8 disagreements is advisable.
3. **Ten plans per cell**: a count of 5/10 has a 95% interval of roughly 2 to 8. Band edges (2 and 7) are within noise for borderline counts.
4. **The key is about this model on this day**. It will drift with model versions.

## Features per family (defined before sampling)

S = semantic (follows from what the words mean); B = behavioral (habit of the model, weighted half).

### F1: Calibration vs accuracy

Task: A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no). Your job: ___

Versions: **A** check the calibration of the predicted probabilities; **B** check the accuracy of the predicted probabilities; **C** check the discrimination of the predicted probabilities; **D** check the overconfidence of the predicted probabilities

| Feature | Definition | Type |
|---|---|---|
| a | Reliability diagram / binning: groups patients by predicted probability and compares to observed readmission rate | S |
| b | Computes a calibration-specific number: ECE, Brier score, calibration slope/intercept, or Hosmer-Lemeshow | S |
| c | Computes accuracy-style metrics (accuracy, confusion matrix, precision/recall) at a probability threshold | S |
| d | Uses an ROC curve or AUC | S |
| e | Proposes recalibration (Platt, isotonic, temperature scaling) | B |
| f | Breaks results out by patient subgroup | B |

### F2: Hold out vs cross-validate

Task: A telecom company wants a model that predicts which customers will cancel next month. You have one table of 2,000 customer rows (usage, plan, tenure, and whether the customer cancelled), collected over the last 18 months. Your job: ___

Versions: **A** hold out a test set; **B** cross-validate; **C** use nested cross-validation; **D** hold out the most recent 3 months as a test set

| Feature | Definition | Type |
|---|---|---|
| a | Sets aside a single test set that is touched only once, at the end, for the final estimate | S |
| b | Uses k-fold cross-validation (names folds / k) | S |
| c | Uses nested cross-validation or an inner loop for hyperparameter tuning separate from the outer evaluation | S |
| d | Splits by time (train on earlier months, test on later months) | S |
| e | Explicitly guards against leakage (e.g. fit preprocessing on training data only) | B |
| f | Handles class imbalance or uses stratified splits | B |

### F3: Control for the confounder vs collect more rows

Task: A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease. Your job: ___

Versions: **A** control for the confounder; **B** collect more rows; **C** randomize coffee assignment; **D** check for a collider

| Feature | Definition | Type |
|---|---|---|
| a | Adjusts for smoking (regression covariate, stratification, or matching) | S |
| b | Draws a causal diagram (DAG) or lists causal assumptions explicitly | S |
| c | Proposes enlarging the sample or notes sample size / power / narrower confidence intervals | S |
| d | Proposes a randomized experiment / randomized assignment as the design | S |
| e | Names a collider or warns that conditioning on some variables can introduce bias | S |
| f | Runs a sensitivity analysis for unmeasured confounding (e.g. E-value) | B |

### F4: Validate provenance vs schema

Task: A bank received a CSV of 40,000 loan applications from a third-party data vendor to train a credit-scoring model. You have the file and a one-page data dictionary. Your job: ___

Versions: **A** validate the provenance of the data; **B** validate the schema of the data; **C** validate the lineage of the data; **D** validate the statistical distributions of the data

| Feature | Definition | Type |
|---|---|---|
| a | Asks where the data came from: who collected it, how, under what consent/licence, vendor sourcing | S |
| b | Checks file integrity / chain of custody (checksum, hash, signed delivery) | S |
| c | Checks column names, types, nullability or allowed values against the data dictionary | S |
| d | Checks value ranges, outliers or distribution shapes | S |
| e | Traces or requests the transformations the vendor applied (processing history between source and file) | S |
| f | Counts duplicates or missing values | B |

### F5: Covariate shift vs concept drift

Task: A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025. Your job: ___

Versions: **A** check for covariate shift; **B** check for concept drift; **C** check for label shift; **D** check for drift

| Feature | Definition | Type |
|---|---|---|
| a | Compares feature distributions between 2023 and 2025 (histograms, KS test, PSI) | S |
| b | Trains a classifier to tell 2023 from 2025 rows, or estimates importance weights | S |
| c | Measures model performance on the labelled 2025 weeks, or compares the feature-to-fraud relationship across years | S |
| d | Compares the overall fraud rate / class prior between years | S |
| e | Proposes retraining, reweighting or a rolling training window | B |
| f | Proposes ongoing monitoring or alerts | B |

## Frequencies (plans of 10 containing the feature)

Band: L likely, P plausible, U unlikely.

### F1: Calibration vs accuracy

| Version | Prompt phrase | a (S) | b (S) | c (S) | d (S) | e (B) | f (B) |
|---|---|---|---|---|---|---|---|
| A | check the calibration of the predicted probabilities | 10 L | 10 L | 0 U | 0 U | 10 L | 10 L |
| B | check the accuracy of the predicted probabilities | 10 L | 10 L | 0 U | 0 U | 10 L | 10 L |
| C | check the discrimination of the predicted probabilities | 5 P | 0 U | 7 L | 10 L | 0 U | 10 L |
| D | check the overconfidence of the predicted probabilities | 10 L | 10 L | 0 U | 0 U | 10 L | 10 L |

### F2: Hold out vs cross-validate

| Version | Prompt phrase | a (S) | b (S) | c (S) | d (S) | e (B) | f (B) |
|---|---|---|---|---|---|---|---|
| A | hold out a test set | 10 L | 10 L | 0 U | 0 U | 10 L | 10 L |
| B | cross-validate | 10 L | 9 L | 2 P | 3 P | 10 L | 10 L |
| C | use nested cross-validation | 0 U | 10 L | 10 L | 5 P | 10 L | 10 L |
| D | hold out the most recent 3 months as a test set | 10 L | 0 U | 0 U | 10 L | 10 L | 5 P |

### F3: Control for the confounder vs collect more rows

| Version | Prompt phrase | a (S) | b (S) | c (S) | d (S) | e (S) | f (B) |
|---|---|---|---|---|---|---|---|
| A | control for the confounder | 10 L | 9 L | 0 U | 0 U | 3 P | 10 L |
| B | collect more rows | 10 L | 0 U | 10 L | 4 P | 0 U | 7 L |
| C | randomize coffee assignment | 10 L | 10 L | 0 U | 6 P | 0 U | 10 L |
| D | check for a collider | 10 L | 10 L | 0 U | 0 U | 10 L | 9 L |

### F4: Validate provenance vs schema

| Version | Prompt phrase | a (S) | b (S) | c (S) | d (S) | e (S) | f (B) |
|---|---|---|---|---|---|---|---|
| A | validate the provenance of the data | 10 L | 10 L | 10 L | 10 L | 9 L | 10 L |
| B | validate the schema of the data | 0 U | 9 L | 10 L | 10 L | 0 U | 10 L |
| C | validate the lineage of the data | 10 L | 10 L | 10 L | 10 L | 10 L | 10 L |
| D | validate the statistical distributions of the data | 0 U | 0 U | 10 L | 10 L | 0 U | 10 L |

### F5: Covariate shift vs concept drift

| Version | Prompt phrase | a (S) | b (S) | c (S) | d (S) | e (B) | f (B) |
|---|---|---|---|---|---|---|---|
| A | check for covariate shift | 10 L | 10 L | 10 L | 0 U | 6 P | 4 P |
| B | check for concept drift | 10 L | 7 L | 10 L | 4 P | 0 U | 5 P |
| C | check for label shift | 10 L | 10 L | 10 L | 10 L | 0 U | 6 P |
| D | check for drift | 10 L | 5 P | 10 L | 0 U | 6 P | 4 P |

## Coder agreement (second coder recoded 8 plans per family)

| Family | Cells | Agreement | Cohen's kappa | Disagreements (plan, feature, coder 1, coder 2) |
|---|---|---|---|---|
| F1 | 48 | 46/48 = 95.8% | 0.91 | F1C-02 a (1,0); F1C-06 a (1,0) |
| F2 | 48 | 47/48 = 97.9% | 0.95 | F2C-02 a (0,1) |
| F3 | 48 | 45/48 = 93.8% | 0.87 | F3C-07 d (1,0); F3C-09 d (1,0); F3B-01 d (1,0) |
| F4 | 48 | 48/48 = 100.0% | 1.00 | none |
| F5 | 48 | 47/48 = 97.9% | 0.95 | F5B-08 e (0,1) |

**Overall: 233/240 cells agree = 97.1%.** Disagreements are all on a single feature in a single plan; none changes a band at 10 plans except where noted below. Coder 1 is used for all frequencies; no adjudication was done. Note the kappa is computed on a small sample with many always-present features, so treat it as indicative only.

Effect of disagreements on bands: F1C-02 and F1C-06 (feature a, reliability diagram, 'discrimination' prompt): coder 2 says 0 where coder 1 says 1. If coder 2 is right the count falls from 5/10 to 3/10, still PLAUSIBLE. F3C-07, F3C-09 and F3B-01 (feature d, randomization): if coder 2 is right, 'randomize coffee assignment' drops from 6/10 to 4/10 (still PLAUSIBLE) and 'collect more rows' from 4/10 to 3/10 (still PLAUSIBLE). F2C-02 (feature a) and F5B-08 (feature e, behavioral): no band change.

## Premise check: do altered prompts give different profiles?

A pair of prompt versions is *distinguishable* if some **semantic** feature differs by at least 4 plans of 10. Result:

| Family | Indistinguishable pairs (cut) | Weakly distinguishable | Clean |
|---|---|---|---|
| F1 calibration | A=B=D (calibration, accuracy, overconfidence) | none | C (discrimination) vs the rest |
| F2 holdout | A=B (hold out vs cross-validate) | none | the rest |
| F3 confounder | none | A vs C (only randomization, 0 vs 6); A vs D (only collider, 3 vs 10) | B vs everything |
| F4 provenance | A=C (provenance = lineage) | B vs D (only checksum 9 vs 0) | A vs B, A vs D, B vs C, C vs D |
| F5 shift | none | A vs B (only fraud rate, 0 vs 4); B vs D (4 vs 0) | C vs everything; A vs D (domain classifier 10 vs 5) |

Cuts: the F1 'calibration vs accuracy' item, the F2 'hold out vs cross-validate' item, the F4 'provenance vs lineage' item. Pairs were kept in items only when listed as clean or flagged weak in the item key.

### Features that fire in every version (cannot discriminate)
F4 c, d, f; F5 c; F1 e and f in versions A, B, D. These are listed in the tables above but are used in no item.

## Repair demo

Prompt F1B ('check the accuracy of the predicted probabilities') plus the sentence "Report accuracy at a 0.5 threshold, not calibration." (9 words). 10 plans in `runs/F1B_repair_demo.json`, coded by one blind coder (not double-coded): c (accuracy at threshold) **10/10**, a (reliability diagram) 0/10, b (calibration number) 0/10, d (ROC/AUC) 0/10.

## Cost, in runs

| Step | Sub-agents | Approx tokens |
|---|---|---|
| Probe (1 single-plan agent, discarded) | 1 | 70k |
| Sampling 200 plans | 20 (+1 extra plan for F4A) | about 1.5M |
| Coding | 10 | about 0.8M |
| Repair demo (sampler, an extra 2-plan sampler by mistake, coder) | 3 | about 0.2M |
| **Total** | **35** | **about 2.6M** |

## Files

- `runs/F1.json` to `runs/F5.json`: 40 plans each, with the full prompt text, model, date.
- `runs/F1B_repair_demo.json`: repair-protocol demo.
- `spec/spec.py` (families, versions, features), `spec/analysis.json` (codes, frequencies, agreement), `spec/analyze.py`, `spec/build_docs.py`, `spec/build_key.py`.
