# Pilot spec: families, one-phrase variants, binary features. Written BEFORE any sampling.
TEMPLATE = ("You are a data analyst on a small team. Write the analysis plan for the task below. "
 "Format: a numbered list of at most 8 steps, one or two sentences each, no code, no preamble, no closing remarks.\n\nTask: {task}")
FAMILIES = {
 "F1": {"name":"Calibration vs accuracy",
  "task":"A hospital has a model that outputs a predicted probability of 30-day readmission for each patient. You have 12,000 patients, each with the model's predicted probability and the true outcome (readmitted yes/no). Your job: {P}.",
  "variants":{"A":"check the calibration of the predicted probabilities","B":"check the accuracy of the predicted probabilities","C":"check the discrimination of the predicted probabilities","D":"check the overconfidence of the predicted probabilities"},
  "features":{
   "a":["Reliability diagram / binning: groups patients by predicted probability and compares to observed readmission rate","S"],
   "b":["Computes a calibration-specific number: ECE, Brier score, calibration slope/intercept, or Hosmer-Lemeshow","S"],
   "c":["Computes accuracy-style metrics (accuracy, confusion matrix, precision/recall) at a probability threshold","S"],
   "d":["Uses an ROC curve or AUC","S"],
   "e":["Proposes recalibration (Platt, isotonic, temperature scaling)","B"],
   "f":["Breaks results out by patient subgroup","B"]}},
 "F2": {"name":"Hold out vs cross-validate",
  "task":"A telecom company wants a model that predicts which customers will cancel next month. You have one table of 2,000 customer rows (usage, plan, tenure, and whether the customer cancelled), collected over the last 18 months. Your job: build and evaluate a churn model, and {P}.",
  "variants":{"A":"hold out a test set","B":"cross-validate","C":"use nested cross-validation","D":"hold out the most recent 3 months as a test set"},
  "features":{
   "a":["Sets aside a single test set that is touched only once, at the end, for the final estimate","S"],
   "b":["Uses k-fold cross-validation (names folds / k)","S"],
   "c":["Uses nested cross-validation or an inner loop for hyperparameter tuning separate from the outer evaluation","S"],
   "d":["Splits by time (train on earlier months, test on later months)","S"],
   "e":["Explicitly guards against leakage (e.g. fit preprocessing on training data only)","B"],
   "f":["Handles class imbalance or uses stratified splits","B"]}},
 "F3": {"name":"Control for the confounder vs collect more rows",
  "task":"A health researcher has observational data on 5,000 adults: daily coffee consumption, whether each developed heart disease within 10 years, and age, smoking status and exercise level. She wants to know whether coffee drinking causes heart disease. Smoking is suspected to be associated with both coffee and heart disease. Your job: {P}.",
  "variants":{"A":"control for the confounder","B":"collect more rows","C":"randomize coffee assignment","D":"check for a collider"},
  "features":{
   "a":["Adjusts for smoking (regression covariate, stratification, or matching)","S"],
   "b":["Draws a causal diagram (DAG) or lists causal assumptions explicitly","S"],
   "c":["Proposes enlarging the sample or notes sample size / power / narrower confidence intervals","S"],
   "d":["Proposes a randomized experiment / randomized assignment as the design","S"],
   "e":["Names a collider or warns that conditioning on some variables can introduce bias","S"],
   "f":["Runs a sensitivity analysis for unmeasured confounding (e.g. E-value)","B"]}},
 "F4": {"name":"Validate provenance vs schema",
  "task":"A bank received a CSV of 40,000 loan applications from a third-party data vendor to train a credit-scoring model. You have the file and a one-page data dictionary. Your job, before any modelling: {P}.",
  "variants":{"A":"validate the provenance of the data","B":"validate the schema of the data","C":"validate the lineage of the data","D":"validate the statistical distributions of the data"},
  "features":{
   "a":["Asks where the data came from: who collected it, how, under what consent/licence, vendor sourcing","S"],
   "b":["Checks file integrity / chain of custody (checksum, hash, signed delivery)","S"],
   "c":["Checks column names, types, nullability or allowed values against the data dictionary","S"],
   "d":["Checks value ranges, outliers or distribution shapes","S"],
   "e":["Traces or requests the transformations the vendor applied (processing history between source and file)","S"],
   "f":["Counts duplicates or missing values","B"]}},
 "F5": {"name":"Covariate shift vs concept drift",
  "task":"A payments company trained a fraud-detection model on 2023 transactions (features: amount, merchant category, device type, country). The model is now being scored on 2025 transactions. Confirmed-fraud labels exist for only the first two weeks of 2025. Your job: {P}.",
  "variants":{"A":"check for covariate shift","B":"check for concept drift","C":"check for label shift","D":"check for drift"},
  "features":{
   "a":["Compares feature distributions between 2023 and 2025 (histograms, KS test, PSI)","S"],
   "b":["Trains a classifier to tell 2023 from 2025 rows, or estimates importance weights","S"],
   "c":["Measures model performance on the labelled 2025 weeks, or compares the feature-to-fraud relationship across years","S"],
   "d":["Compares the overall fraud rate / class prior between years","S"],
   "e":["Proposes retraining, reweighting or a rolling training window","B"],
   "f":["Proposes ongoing monitoring or alerts","B"]}},
}
def prompt(fam, v): 
    f=FAMILIES[fam]; return TEMPLATE.format(task=f["task"].format(P=f["variants"][v]))
