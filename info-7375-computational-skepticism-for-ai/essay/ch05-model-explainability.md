# Chapter 5: Model explainability

## ES-ch05.1

A data scientist at a subscription company trains a gradient-boosted model to predict which customers will cancel within 90 days. A Shapley-value summary shows that "months since signup" has the largest average attribution, with longer tenure pushing the predicted cancellation probability down. The data scientist writes in a memo: "Tenure drives churn. If we give new customers a free six-month extension, they will stay." Evaluate this reasoning. Explain what the attribution does establish, why it does not support the proposed action, and what evidence would.

**Points:** 5

**Rubric (1 point each):**

1. States that the attribution describes how the fitted model's prediction depends on the input relative to a reference, which is a fact about the model's behavior and not a causal effect in the world.
2. Explains that the model learned an association from observational data: long-tenured customers differ from new ones (survivors, plan type, satisfaction), so tenure can stand in for other causes of staying.
3. Notes that a free extension is an intervention on the customer's situation and is not the same variable as time elapsed since signup, so the model's dependence on tenure says nothing about what an extension would do.
4. Names the evidence that would support the action: a randomized experiment, or a credible causal design with confounders addressed, measuring cancellation and cost with and without the extension.
5. States what the attribution is good for here (generating hypotheses, checking the model's behavior for sense, spotting leakage) and concludes that the memo's claim remains a hypothesis until tested.

**Source:** What SHAP is, and what SHAP isn't

## ES-ch05.2

A vendor claims that its saliency-map method for an image classifier "shows exactly what the model looks at", and offers as evidence that a panel of doctors found the maps reasonable. Design an evaluation that would test whether the maps are faithful to the model. For each test you propose, say what you would do, what result would count against the vendor's claim, and what the test cannot show. Also explain why the doctors' ratings do not answer the question.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes plausibility (judged by people) from faithfulness (reflecting what the model computes), and explains that doctors' ratings test the former: a faithful map of a model that uses a spurious cue can look wrong, and an unfaithful map can look right.
2. Proposes replacing the trained weights with random ones (fully or layer by layer) and checking that the maps change substantially; maps that stay similar do not depend on what the model learned.
3. Proposes training on shuffled labels, or a similar data randomization, and comparing the resulting maps with those of the real model.
4. Proposes a deletion or insertion test, removing or revealing the top-ranked regions and comparing the change in the model's output with the change from random regions, while noting that masked images are off-distribution.
5. States the limits: passing these tests is necessary but not sufficient, none shows causal relevance in the real world, and the method should be compared with alternatives and checked on planted cues whose ground truth is known.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## ES-ch05.3

A hospital's readmission model is additive: predicted risk (%) = 4 + 0.3 x age + 2.5 x prior admissions - 1.5 x follow-up visits in the last year. A patient aged 80 with 3 prior admissions and 0 follow-up visits has a predicted risk of 35.5%. Explain this prediction with Shapley values, treating the inputs as independent and valuing a subset of inputs as the expected prediction when those inputs are fixed at the patient's values and the others are set to a reference group's averages. Use two reference groups. Group 1 is all adult patients, averaging age 55, 1 prior admission and 2 follow-up visits. Group 2 is patients aged 75 to 85, averaging age 80, 2 prior admissions and 1 follow-up visit. Compute the three Shapley values for each reference group and check them against the model's predictions. Explain why age is the top reason against one reference and not the other, and say which reference you would use and how you would present the result to a clinician.

**Points:** 5

**Rubric (1 point each):**

1. Shows that in an additive model with independent inputs each Shapley value equals the coefficient times the patient's deviation from the reference average.
2. Against group 1 gives age +7.5, prior admissions +5.0 and follow-up visits +3.0, summing to +15.5, the gap between 35.5% and the group's average prediction of 20.0%.
3. Against group 2 gives age 0, prior admissions +2.5 and follow-up visits +1.5, summing to +4.0, the gap between 35.5% and the group's average prediction of 31.5%.
4. Explains that an attribution answers "compared with what?": against all adults age is the main reason because the patient is older, against peers of the same age it explains nothing, and the model has not changed.
5. Recommends choosing the reference that matches the clinical question, stating it with every explanation, and checking how the conclusion changes under other references.

**Source:** The mathematics of Shapley values

## ES-ch05.4

Two teams train models for the same lending task on the same data. Team 1 uses a gradient-boosted tree model and team 2 a regularized logistic regression. Both reach a test AUC of 0.86 (the difference is within sampling noise) and the two models make the same decision for 94% of applicants. Team 1's Shapley-based ranking puts total_debt first; team 2's ranking puts monthly_payments first. The two inputs have a correlation of 0.9. A manager asks which ranking identifies "the true driver" of lending outcomes and wants to publish one. Explain why both rankings can be accurate descriptions of their models while neither identifies a true driver, what you would do to produce a more defensible statement about importance, and what the report should say.

**Points:** 5

**Rubric (1 point each):**

1. Explains that many different models can fit the data about equally well, so predictive accuracy does not select among them, and that an attribution is a property of one fitted model.
2. Explains that with strongly correlated inputs a model can substitute one for the other, so credit shifts between them according to the algorithm, the regularization and the random seed rather than the world.
3. Says that neither ranking establishes a causal driver of repayment; that takes causal knowledge or an experiment.
4. Proposes concrete checks: repeating across seeds, bootstrap resamples and several model classes, and attributing to the group of correlated inputs together (for example by permuting them jointly), then comparing the results.
5. Says what to report: that the ranking is not unique, which model each ranking describes, how stable it was, and the group-level finding, rather than a single "true driver".

**Source:** The correlated feature problem

## ES-ch05.5

A lender must tell denied applicants what they could do to be approved. A data scientist proposes to return, for each denied applicant, the closest approved input found by an optimizer (Euclidean distance on standardized features) and to tell the applicant to change to those values. Critique this proposal. Identify at least four distinct ways the returned counterfactual can be useless or harmful as advice, and propose a design change for each.

**Points:** 5

**Rubric (1 point each):**

1. Notes that the search can change immutable or sensitive inputs (age, sex, past events) or move one-way inputs (a past missed payment cannot be removed, tenure only grows with time), so constraints on what may change must be built in; a result that needs an immutable input also signals that the model relies on it.
2. Notes that distance in standardized units is not the applicant's cost or effort, and proposes a cost function reflecting effort and time and offering several diverse options.
3. Notes that inputs are correlated or causally linked, so a point reached by changing a few inputs while holding the rest fixed may not be reachable, and proposes plausibility or causal-consistency constraints.
4. Notes that the counterfactual describes the current model and threshold, which can change with retraining or policy, and proposes stating a validity period and re-checking or committing to it.
5. Notes that flipping the model's output is not evidence that the applicant would repay and that advice can encourage gaming of proxies, and proposes tracking the outcomes of applicants who follow the advice.

**Source:** Counterfactuals are closer to what you actually want

## ES-ch05.6

A team's skin-lesion classifier scores AUC 0.95 in internal validation but 0.78 at a new clinic. Attribution maps on internal images concentrate on a ruler and on ink marks that clinicians often add near lesions they find suspicious. Describe how you would use explanations to investigate, how you would confirm a suspected shortcut with methods that do not rely on the explanation, and how you would fix the problem and verify the fix.

**Points:** 5

**Rubric (1 point each):**

1. Uses attributions across many images, not one, to form a hypothesis about which regions or features carry weight, split by correct and incorrect cases and by class.
2. Confirms by an intervention that does not rely on the explanation: removing or inpainting the markers, adding them to benign images, and measuring how predictions and accuracy change, and comparing accuracy on images with and without markers.
3. Checks provenance: how marker presence relates to the label in the training data (marked cases were more often suspicious or biopsied) and how that differs at the new clinic, stratifying by site and device.
4. Proposes fixes such as removing or masking the cue, rebalancing or collecting data where the cue is uncorrelated with the label, augmentation, or training that penalizes reliance on it, followed by retraining.
5. Verifies on an external site and on cue-swapped test sets, re-inspects the attributions, and notes that an explanation is a lead rather than proof because other shortcuts may remain.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## ES-ch05.7

A company deploys a language model that writes step-by-step reasoning before answering in a medical-coding task, and plans to show that reasoning to auditors as the explanation of why each code was chosen. Evaluate whether the written reasoning can serve as an explanation of the model's decision. Describe an experiment that tests it, and say what the auditors can and cannot conclude from the text.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes a rationale that reads plausibly from a faithful account of the factors that produced the output, noting that the reasoning is itself generated text and not a readout of the model's computation.
2. Describes an intervention experiment: change or add a factor in the input (for example a hint or an irrelevant cue), see whether the answer changes, and see whether the reasoning mentions the factor.
3. Describes a second test, such as corrupting or removing steps of the reasoning and checking whether the answer changes, or checking whether the answer is stable when the reasoning is regenerated.
4. States what auditors can use the reasoning for (finding errors, checking cited rules against sources, making steps reviewable) and what they cannot conclude (that it lists all influences or shows the absence of bias).
5. Recommends verifying the claims in the reasoning against source documents and outcome data, and not treating the text as evidence of what caused the decision.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## ES-ch05.8

A city agency will use a model to prioritize housing-inspection visits, and the decisions affect landlords and tenants. A vendor offers (a) a gradient-boosted model with AUC 0.88 and post-hoc Shapley explanations, and (b) a scoring rule with seven integer-weighted checks and AUC 0.86. Argue for the option you would adopt and the evidence you would demand before deciding. Address the accuracy gap, the reliability of the explanations, auditability, and what would change your decision.

**Points:** 5

**Rubric (1 point each):**

1. Asks whether the 0.02 AUC gap is real and matters: compares the options on the same held-out data with uncertainty (for example bootstrap intervals) and on an operational metric such as violations found in the top-k visits, not AUC alone.
2. Notes that for the scoring rule the model is its own exact explanation, so reviewers, tenants and landlords can check, contest and correct it, whereas a post-hoc explanation describes a model that remains opaque and can be approximate, unstable or misleading with correlated inputs.
3. Notes that neither option's explanations show that decisions are fair or correct, so both need outcome audits across neighborhoods and groups and monitoring for drift.
4. Gives the case for the complex model if its operational advantage is large and important, with conditions such as validation, monitoring, and keeping the simple rule as a benchmark or fallback.
5. States what would change the decision: a larger operational gap, evidence that the simple rule fails in subgroups, legal requirements for reasons, or the results of a stability analysis of the explanations.

**Source:** Three words that don't mean the same thing

## ES-ch05.9

A manager runs LIME, which explains a prediction by fitting a simple model to the classifier's outputs on randomly perturbed copies of the input, twice on the same input of a deterministic classifier and gets different top features. She asks: "Which explanation is correct?" Answer her question. Explain what the output actually is, what causes the variation, and the procedure you would follow to give her a reliable characterization of the classifier's local behavior on this input.

**Points:** 5

**Rubric (1 point each):**

1. Says neither run is "the" correct explanation: each is one random estimate from a fit to randomly sampled perturbed points, so the question assumes a single true answer that the method does not return.
2. Names sources of variation: random sampling of perturbed points, the number of samples, the neighborhood width or kernel, feature discretization, and regularization of the surrogate, while the classifier itself is deterministic.
3. Describes repeating the run with many seeds and more samples until it is stable, quantifying agreement (for example top-k overlap or rank correlation), and reporting coefficients with their spread.
4. Describes checking the surrogate's local fidelity (weighted R-squared on the neighborhood), its sensitivity to the neighborhood width, and whether the perturbed points are realistic.
5. Describes checking the explanation against the classifier by applying the suggested changes to the real model and comparing outputs, and cautions against picking the run that looks most sensible.

**Source:** LIME, in a different shape

## ES-ch05.10

A team must give a regulator a feature-importance report for a random-forest model of loan default. Three tools are available: the forest's built-in impurity-based importance, permutation importance on held-out data, and the mean absolute Shapley value over the held-out set. Compare what each measures, name a failure mode of each, and propose a protocol that makes the report defensible. State what the report can and cannot claim.

**Points:** 5

**Rubric (1 point each):**

1. Describes impurity-based importance as the total impurity reduction from splits on training data, and names its failure modes: it can reward fitting noise, it favors inputs with many distinct values, and it says nothing about generalization.
2. Describes permutation importance as the drop in held-out performance when a column is shuffled (the model's reliance), and notes that correlated inputs distort it through unrealistic shuffled rows and shared credit, which permuting correlated groups together mitigates.
3. Describes mean absolute Shapley value as the average size of an input's contribution to predictions relative to a reference, noting that it depends on the reference and value function, measures influence on outputs rather than on accuracy, and splits credit among correlated inputs.
4. Proposes a protocol: held-out data, repeated runs or bootstrap for variability, a random noise column as a null benchmark, grouping of correlated inputs, reporting more than one measure with their disagreements, and documenting the model, reference and settings.
5. States the limits: all three describe the fitted model's dependence and not causal importance in the world, so claims about real-world drivers need causal evidence.

**Source:** What SHAP is, and what SHAP isn't

## ES-ch05.11

A proposed rule would require that any automated decision denying someone a benefit be accompanied by "a clear explanation of the main factors". A vendor proposes to satisfy it by printing the three inputs with the largest Shapley values for each decision. Evaluate whether this serves the purposes such a rule would have: understanding the decision, contesting it and correcting errors, acting to change the outcome, and detecting discrimination. For each purpose say what the list does or does not supply and what would need to be added.

**Points:** 5

**Rubric (1 point each):**

1. For understanding: notes that attributions are relative to a reference and depend on the model, so the person needs plain-language statements of the main factors with the values used, and that adequacy depends on the audience.
2. For contesting and correcting: notes that showing which recorded values drove the decision lets a person spot a wrong input and request correction, but does not show whether the model's logic is sound.
3. For acting to change the outcome: notes that a list of contributions is not recourse, and that the person also needs counterfactual information restricted to changes they can make and the size of change needed.
4. For detecting discrimination: notes that per-decision top-three lists cannot reveal proxy effects or group disparities, which need outcome audits by group and tests with matched cases.
5. Notes that the list may be approximate or unstable, can omit interactions and correlated inputs, and recommends adding counterfactuals, documentation of the method and a route to human review.

**Source:** Three words that don't mean the same thing

## ES-ch05.12

A model's expected output given each subset of three inputs is: no inputs, 50; A alone, 60; B alone, 55; C alone, 50; A and B, 75; A and C, 60; B and C, 55; all three, 75. (a) Compute the Shapley values of A, B and C. (b) Check them against the total to be explained. (c) Explain what the result shows about C and about the interaction between A and B. (d) Explain why one-at-a-time effects (the change from adding each input alone to the empty set) would give a misleading picture here.

**Points:** 5

**Rubric (1 point each):**

1. Gives the Shapley values A = 15, B = 10 and C = 0, with a method: the average of marginal contributions over the six orderings, or the coalition weights 1/3, 1/6, 1/6 and 1/3.
2. Checks that 15 + 10 + 0 = 25 = 75 - 50, the output with all inputs minus the output with none (efficiency).
3. Explains that C never changes the output in any coalition, so it is a dummy input and receives 0.
4. Explains that A and B together add 10 beyond their separate effects (10 and 5, against a joint gain of 25) and that the Shapley value splits that synergy equally, 5 to each.
5. Explains that the one-at-a-time effects (10, 5 and 0) sum to 15 and miss the synergy, and that an attribution based on a single ordering would give A and B different shares depending on which is added first.

**Source:** The four axioms

## ES-ch05.13

A hospital wants to know whether showing feature-attribution explanations next to an AI risk score helps clinicians decide better. Design the study. Specify the arms, the outcome measures, which results you would analyze separately, how you would handle sample size and uncertainty, and what results would lead you not to deploy the explanations.

**Points:** 5

**Rubric (1 point each):**

1. Specifies randomized arms: at least the AI score alone and the AI score with the explanation, preferably with a no-AI control, with random assignment and an analysis plan fixed in advance.
2. Includes cases on which the AI is right and cases on which it is wrong, and reports decision accuracy separately for each so that overreliance on wrong advice is visible.
3. Measures reliance and calibration, for example agreement with the AI, changes of mind, clinician confidence compared with accuracy, and time taken.
4. Handles the statistics: justifies the sample size for the effect of interest, reports confidence intervals for differences in proportions, accounts for clustering by clinician and case, and does not read a non-significant result as no effect.
5. States decision criteria in advance: do not deploy if explanations raise following of wrong advice or fail to improve accuracy beyond the score alone, since confidence without accuracy is unwarranted trust.

**Source:** Model Explainability: Distinguishing Explanation from the Appearance of Explanation

## ES-ch05.14

An auditor receives from a lender a set of Shapley and LIME reports for 1,000 loan decisions. The reports were generated by the lender, show zero importance for a sensitive attribute, and have consistent top features. The lender offers them as proof that its model does not use the attribute. Explain how this evidence could mislead, including by deliberate design, and describe what the auditor should do instead.

**Points:** 5

**Rubric (1 point each):**

1. Notes that the reports were generated, and possibly selected, by the party being audited, with its own reference and settings, and cannot be tied to the deployed model without access.
2. Notes that perturbation-based explainers query unrealistic points and that a deployed system can be built to behave differently on them, so the reports can be made to look clean.
3. Notes that zero attribution to an attribute (for example because it is excluded from the inputs) does not rule out dependence through correlated proxies.
4. Proposes testing the deployed system directly: matched pairs of realistic applications that differ in the attribute or its proxies, and outcome and error rates by group on real decisions.
5. Proposes independent replication with the auditor's own explainers and settings, access to the model and its logs, and comparison of the explanations with measured behavior.

**Source:** LIME, in a different shape

## ES-ch05.15

A colleague argues: "SHAP, which assigns each input its Shapley value, is the only attribution method that satisfies efficiency (attributions sum to the prediction minus a baseline prediction), symmetry (interchangeable inputs get equal values), dummy (an input that never matters gets zero) and additivity (attributions for a sum of two models are the sums of their attributions), so it is the uniquely correct way to explain a model's predictions." Evaluate the argument. Say where it is valid, where it overreaches, and what the word "correct" hides.

**Points:** 5

**Rubric (1 point each):**

1. States the valid core: for a given value function (a rule assigning a payoff to each subset of inputs), the Shapley allocation is the unique one satisfying the four properties.
2. Points out that the uniqueness is conditional on the value function: marginal versus conditional sampling and the choice of reference distribution give different attributions for the same model, and the axioms do not choose among them.
3. Points out that the properties describe a fair split of a total and do not guarantee that the split answers the user's question, such as causal effect, recourse or which inputs to collect.
4. Gives examples where all four properties hold and the output still misleads: credit split between duplicate inputs, interaction credit divided equally, attributions that do not predict the effect of changing an input, and approximations used when exact computation is infeasible.
5. Concludes that "uniquely correct" overreaches: the accurate claim is that it uniquely satisfies these properties for a stated value function, and that usefulness must be judged against the purpose and audience.

**Source:** The four axioms
