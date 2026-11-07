# Chapter 4: Robustness and distribution shift

## ES-ch04.1

A linear classifier scores an input x with s(x) = w·x + b over d input values, and an attacker may change each value by at most ε in either direction (an L∞ budget). (a) Derive the largest change in the score the attacker can cause and say which change achieves it. (b) Explain, with a numerical example, why small changes to each value can matter more as the number of input values grows, and what this suggests for deep networks that are only piecewise linear. (c) State one thing this linear picture does not explain about adversarial vulnerability.

**Points:** 5

**Rubric (1 point each):**

1. States that the change in score is w·δ and that, with |δ_i| ≤ ε, it is maximized by δ_i = ε·sign(w_i), giving a largest change of ε·Σ|w_i| = ε‖w‖₁.
2. Explains that Σ|w_i| grows with the number of input values when typical weight magnitude is fixed, so a change tiny in every coordinate can add up to a decisive shift, with a correct numerical example (for instance d = 1000, |w_i| = 0.02, ε = 0.01 gives 0.2).
3. Contrasts with a random direction of the same length, where contributions largely cancel and the typical shift is smaller by a factor of about √d, or notes that an attacker limited by Euclidean length r gains at most r‖w‖₂ rather than ε‖w‖₁.
4. Extends the argument to piecewise-linear networks: they are locally linear, so the sign of the input gradient of the loss gives an effective direction, a one-step gradient-sign attack uses it, and iterating with projection gives stronger attacks.
5. Names a limit of the linear account, such as that it does not explain why some models trained on the same data are more vulnerable than others, the role of data structure and low-variance directions, or why robustness trades against clean accuracy.

**Source:** The linearity hypothesis

## ES-ch04.2

A vendor's product sheet says its traffic-sign recognizer is "robust to adversarial attacks and 97% accurate." You are asked to turn this claim into one that could be shown false. List what the claim must specify, explain why each item matters, and describe how you would report the evaluation so that a reader can see what was and was not tested.

**Points:** 5

**Rubric (1 point each):**

1. Requires the set of allowed perturbations, such as the norm and size of the change, physical patches or transformations, and natural corruptions, because "robust" without a stated set has no input that would count as a failure.
2. Requires the attacker's knowledge and capability (white-box, query-only, transfer) and the attack's strength and adaptivity (steps, restarts, awareness of any defense), since weak attacks yield optimistic numbers.
3. Requires reporting clean accuracy and accuracy under each stated perturbation, with sample sizes or confidence intervals, and comparison with an undefended baseline, since robustness can be bought with clean accuracy.
4. Requires a separate axis for natural distribution shift (lighting, weather, camera changes, new regions), because robustness to constructed perturbations does not imply robustness to natural shift or the reverse.
5. Calls for a profile or table plus a residual-risk statement of perturbation types and shifts that were not tested, and notes that failing to find failures in a finite test is not proof of safety, so monitoring and a trigger for human review are needed.

**Source:** Towards honest robustness disclosure

## ES-ch04.3

Explain how adversarial training works, what it costs, and what it does not provide. Then say what else you would do before relying on an adversarially trained model in a safety-relevant application.

**Points:** 5

**Rubric (1 point each):**

1. Describes the min–max structure: an inner maximization finds a high-loss perturbation inside the allowed set (for example by multi-step projected gradient ascent) and an outer minimization updates the weights to reduce the loss on those perturbed inputs.
2. States costs: roughly K + 1 forward-backward passes per batch for a K-step inner attack, and a typical loss of clean accuracy relative to ordinary training.
3. States that protection is tied to the threat model used in training (norm, budget, attack type) and transfers imperfectly to other norms, larger budgets, patches or natural shifts.
4. States that the resulting robustness is empirical, not a proof, since stronger or adaptive attacks may lower the measured accuracy, and mentions robust overfitting or the need to evaluate robust accuracy on held-out data and stop early.
5. Lists follow-up steps such as testing with strong adaptive attacks under several threat models, using certification or verification for narrow high-stakes properties, testing natural shift, monitoring in production, a human-review fallback and documenting residual risk.

**Source:** Adversarial training and its scaling limits

## ES-ch04.4

Compare empirical robustness estimates (accuracy under the strongest attack you can run) with certified robustness (a proof that no perturbation in a stated set changes the prediction). For each, say what a reported number means, in which direction it can be wrong, and what its main limits are. Use randomized smoothing or a formal verifier as your example of a certificate. Recommend how to use them together.

**Points:** 5

**Rubric (1 point each):**

1. Explains that accuracy under a given attack is an upper bound on true worst-case accuracy in that perturbation set, since failing to find an adversarial example does not prove none exists, and that weak, non-adaptive attacks or gradient masking inflate it.
2. Explains that certified accuracy counts only inputs for which a proof exists, so it is a lower bound on true robust accuracy, and that incomplete verifiers or loose certificates can understate robustness.
3. Notes that both statements hold only inside a stated perturbation set, such as an L2 radius or L∞ budget, and say nothing about other norms, larger budgets or natural shift, and that a certificate for one norm does not automatically cover another (an L2 radius R covers L∞ size ε only if ε√d ≤ R).
4. Names practical limits of certificates, such as many noise samples per prediction and a probabilistic guarantee for randomized smoothing, clean-accuracy loss at large noise levels, and verification that scales poorly to large models or open-ended specifications.
5. Recommends reporting both, since certified ≤ true ≤ attack-measured brackets the truth, using stronger adaptive attacks to lower the upper bound and better methods to raise the lower bound, and reserving certification for narrow, high-stakes properties.

**Source:** Certified defenses — what "guaranteed" means and costs

## ES-ch04.5

A model that reads chest X-rays scores 94% on a held-out test set drawn from the same three hospitals used for training. The hospital is visible in image markers and is strongly correlated with disease prevalence. Explain how the model could score well for the wrong reason, how you would test whether it does, and what you would change in the data or the training if you find it does.

**Points:** 5

**Rubric (1 point each):**

1. Explains shortcut learning: a feature that predicts the label in the training collection without being related to the disease (a hospital marker or scanner trait) is available to, and often exploited by, models that minimize training loss, and a random held-out split from the same sources has the same correlation, so it does not expose the shortcut.
2. Proposes baselines that use only the shortcut (the marker, or the image with the lung region masked) and compares them with 94%; if they come close, the score is weak evidence that the model reads pathology.
3. Proposes external evaluation on a new hospital and per-site or per-group results, including accuracy within each site-label combination, rather than one pooled figure.
4. Proposes intervention tests that add, remove or swap the marker while holding the image content fixed and check whether predictions move, noting that saliency maps alone are weak evidence.
5. Proposes remedies such as removing or randomizing markers, rebalancing or reweighting site-label groups, collecting data from more sites or group-robust training, and re-testing externally, while acknowledging that other site-specific cues may remain.

**Source:** What adversarial examples actually expose

## ES-ch04.6

Define covariate shift, label (prior) shift and concept shift. For each, give a concrete example, say how you would detect it in a deployed model, and say how you would evaluate or correct performance under it. Then say what could go wrong with these approaches.

**Points:** 5

**Rubric (1 point each):**

1. Defines all three correctly (P(x) changes with P(y | x) fixed; P(y) changes with P(x | y) fixed; P(y | x) changes) and gives a fitting example of each.
2. For covariate shift, describes detection by comparing input distributions (two-sample tests, a domain classifier, drift statistics), notes that detected shift may not hurt accuracy, and describes evaluation by importance weighting or by slicing performance over the shifted region, with the caveats of needing support overlap and of high-variance weights.
3. For label shift, describes estimating the new class frequencies from predicted-class counts and the confusion matrix or from a labeled sample, adjusting posteriors or thresholds by the prior ratio, and notes that true and false positive rates stay fixed while precision changes.
4. For concept shift, notes that it is invisible in inputs alone, so detection needs outcome labels or proxies, usually with a label delay, and that responses include retraining, recency weighting or windowing.
5. Gives caveats: real shifts mix types, which distribution is invariant cannot be verified from unlabeled data alone, drift monitors run many tests and need multiple-comparison control, and monitoring needs a trigger and an owner.

**Source:** Distribution shift

## ES-ch04.7

A team iterates on a model for six months, checking the same 2000-example test set after every change (about 300 times), and then reports the final test accuracy as the accuracy to expect in production. Explain why that number is likely optimistic, describe two other ways an evaluation can leak, and describe an evaluation protocol that would give a trustworthy estimate.

**Points:** 5

**Rubric (1 point each):**

1. Explains adaptive reuse and selection: choosing among many versions using the test set makes the final score partly a product of fitting that set's noise, so the test set has become a validation set and the estimate is biased upward, more so with more looks and a smaller test set.
2. Describes a leak through preprocessing or selection, such as normalization, imputation or feature selection fitted on all data (including labels) before the split.
3. Describes a second leak, such as duplicates or near-duplicates or the same entity on both sides of the split, temporal leakage from a random split of time-ordered data, features that encode the label, or benchmark contamination in pretraining data.
4. Describes a protocol with separate training, validation and untouched test sets, with the test set used once or a few times (or freshly collected), splits that match deployment (by time or by group), and preprocessing fitted inside training folds, with nested cross-validation when data are scarce.
5. Calls for reporting a confidence interval that reflects test size and disclosing how many comparisons were made, and notes that even a clean test estimates performance only on the sampling distribution, so deployment shift needs monitoring.

**Source:** Resampling and validation

## ES-ch04.8

A team runs 400 independent test cases, drawn at random from the expected usage of a system, and observes zero failures. Their report calls the failure rate "effectively zero". Evaluate this claim. Compute an approximate 95% upper confidence bound on the failure rate, say how many failure-free trials would be needed to bound the rate below 0.1%, and state the conditions under which the bound is valid and the ways it can mislead.

**Points:** 5

**Rubric (1 point each):**

1. States that zero observed failures does not show a true rate of zero: the data are compatible with positive rates, for example a 1% rate would produce no failures in 400 trials with probability about 1.8%.
2. Gives the bound: by the rule of three, about 3/400 = 0.75% at 95% confidence (the exact value from (1 − p)^400 = 0.05 is about 0.746%).
3. Gives the requirement for 0.1%: about 3000 failure-free trials (n ≈ ln 0.05/ln 0.999 ≈ 2995), and notes that the bound shrinks in proportion to 1/n, so a tenfold smaller bound needs about ten times the trials.
4. States the conditions: independent draws from the distribution of interest, with clustered or near-duplicate cases reducing the effective sample size, and notes that the bound does not cover inputs outside the sampling distribution such as rare, shifted or adversarial inputs, or a test set reused after tuning.
5. Ties the bound to the decision: it should be compared with the tolerable failure rate, a ceiling of 0.75% may be unacceptable for severe events, and the report should state the bound and the sampling conditions rather than "zero".

**Source:** Towards honest robustness disclosure

## ES-ch04.9

A support-ticket classifier reports about 93% overall accuracy. Broken down by customer segment, three large segments (together 95% of tickets) average 94.5% and one small segment (5% of tickets) scores 60%. Explain how the overall figure can hide this, what you would report and decide on, what could cause the pattern, and what limits any fix will face.

**Points:** 5

**Rubric (1 point each):**

1. Shows that overall accuracy is a weighted average dominated by large groups: 0.95 × 94.5% + 0.05 × 60% ≈ 92.8%, so a segment at 60% barely moves it, and the overall figure would only fall to about 91% if that segment's share doubled to 10%.
2. Calls for reporting per-segment and worst-group accuracy with sample sizes and confidence intervals (small groups give wide intervals), and for basing the decision on consequences for the worst-affected group, not only the average.
3. Gives plausible causes, such as underrepresentation in training data, different label noise or a different input-label relationship in that segment, or reliance on cues that fail for it.
4. Gives mitigations such as collecting more data for the segment, reweighting or oversampling, group-robust objectives that minimize the worst group's loss, segment-specific thresholds or models, or human review for that segment.
5. States limits: group labels are needed at evaluation (and sometimes training), gains for one group may cost average accuracy, overlapping groups multiply and cannot all be enumerated, and improving known groups does not cover unknown ones.

**Source:** Towards honest robustness disclosure

## ES-ch04.10

Distinguish robustness to natural perturbations (sensor noise, lighting changes, typos, a new population) from robustness to worst-case perturbations (inputs chosen by an optimizer within a budget). Explain why neither implies the other, give a high-dimensional argument for why random noise is a poor substitute for worst-case search, and design an evaluation plan for a deployed image classifier that covers both.

**Points:** 5

**Rubric (1 point each):**

1. Defines natural perturbation as arising from the world or a shift in the data-generating process and worst-case perturbation as the loss-maximizing change inside a stated perturbation set, which makes the second depend on a threat model.
2. Explains that neither implies the other: an adversarially trained model can still degrade under natural shifts its training budget did not cover, and a model robust to noise or corruptions can be broken by small optimized changes.
3. Gives the high-dimensional argument: for a linear score the worst-case direction aligns with the weights, so at a given L2 length r it shifts the score by about r‖w‖₂ whereas a random direction of the same length shifts it by about r‖w‖₂/√d, roughly √d times less (an L∞ budget ε gives a worst-case shift of ε‖w‖₁, larger than the shift from a random direction of the same L2 length by a factor ‖w‖₁/‖w‖₂, which is at most √d).
4. Plans the natural axis: held-out data from other conditions or times, corruption tests, slice and worst-group metrics with confidence intervals, and monitoring of deployment inputs for drift.
5. Plans the worst-case axis: a stated threat model, strong adaptive multi-step attacks under several norms and budgets, black-box or transfer checks, and certification where feasible, reported as a profile with clean accuracy and residual risk.

**Source:** Distribution shift

## ES-ch04.11

You must test a toxicity classifier for a comment platform before launch, beyond its overall test accuracy. Design a stress-test suite that includes slice-based evaluation, invariance tests and counterfactual (minimal-pair) tests. For each, say what it would catch and what a pass does and does not establish, and explain how you would avoid fooling yourself given the number of tests you run.

**Points:** 5

**Rubric (1 point each):**

1. Describes slice-based evaluation on predefined subsets (dialect, topic, length, language, identity terms, negation, quoted or reclaimed uses) with per-slice metrics, sample sizes and intervals, because averages hide pockets of failure.
2. Describes invariance tests that apply label-preserving edits (typos, case, whitespace, paraphrase, neutral name or identity-term swaps) and expect unchanged output, notes that failures expose dependence on surface cues, and notes that each edit must be checked to preserve the label (name or identity-term swaps may be filed here or as counterfactual tests, provided the expected behavior, unchanged or flipped, is stated).
3. Describes counterfactual or minimal-pair tests where a small edit should change the output in a specified direction (adding negation, removing an insult; identity-term swaps also count here when the expected behavior is stated), which reveals reliance on keywords rather than meaning.
4. States that passing a finite suite shows behavior only on those tests, that the tests encode their designers' assumptions, and that a pass does not prove invariance or understanding.
5. Describes statistical hygiene: many slices produce chance extremes, so slices found by searching should be treated as hypotheses to confirm on fresh data, and the model should not be tuned on the stress suite and then evaluated on it as clean evidence.

**Source:** Cross-domain transfer — the same structure in different clothes

## ES-ch04.12

A company says its image classifier "understands" what a pedestrian is, citing 99% accuracy on a large test set. Without taking a position on what understanding is in general, describe what evidence about the classifier's behavior would be needed to support the narrower claim that it bases its decisions on the features that make something a pedestrian, explain why each kind of evidence is informative, and state what such evidence still could not establish.

**Points:** 5

**Rubric (1 point each):**

1. Explains that high accuracy on a test set from the same source is consistent with reliance on accompanying cues (crosswalk, background, time of day) and cannot separate intended from incidental features.
2. Calls for stability under label-preserving changes (lighting, pose, clothing, background, small bounded perturbations), because a decision based on the intended features should not change with them.
3. Calls for sensitivity to meaningful interventions: predictions should change in the expected direction when a pedestrian is removed, added or occluded, tested with counterfactual edits that vary one factor at a time.
4. Calls for performance on shifted and rare conditions and on subgroups (other cities, sensors, weather, unusual poses) with worst-group results, not only an average.
5. States limits: finite tests give evidence about the conditions tested and not proof, behavior alone does not establish what is represented internally, saliency or other explanations are not proof of reliance, and humans must specify which features count as the right ones.

**Source:** What adversarial examples actually expose

## ES-ch04.13

A lender deploys a default-prediction model on tabular applicant data, and applicants learn which fields move the score. Explain how adversarial robustness differs here from the image case, define a sensible threat model, and describe how you would change the model, the features and the evaluation to resist gaming.

**Points:** 5

**Rubric (1 point each):**

1. Explains that tabular changes are discrete and bound by feasibility (debt cannot exceed what is possible, values must be non-negative, fields depend on one another), so unconstrained gradient attacks create impossible records and the real threat is strategic edits to feasible fields.
2. Classifies features as immutable, costly to change or cheap to change, and builds the threat model on what an applicant can change, at what cost and whether the lender verifies it.
3. Distinguishes features that cause repayment from proxies that merely correlate with it: cheap, non-causal proxies can be gamed so the score rises while risk does not, whereas genuinely improving a causal feature (for example paying down balances) lowers real risk, though misreporting a causal feature remains possible unless it is verified.
4. Proposes design changes such as favoring verified and causally relevant features, removing or down-weighting cheap proxies, monotonicity constraints and input verification.
5. Proposes evaluation by searching over feasible costed edits and simulating best-response behavior, and notes that deployment itself changes the data (the relationship between features and default can drift), so monitoring and a retraining plan are required.

**Source:** Cross-domain transfer — the same structure in different clothes

## ES-ch04.14

A company uses a language model with a fixed instruction to label customer emails as urgent or not urgent. Design an evaluation of the labeler's robustness to wording and formatting changes (in the instruction, in the emails, or both), including how you would handle randomness in the outputs and how you would report results. Then explain how an adversarial email differs from a merely differently worded one.

**Points:** 5

**Rubric (1 point each):**

1. Builds a set of meaning-preserving variants of the instruction and/or the inputs (paraphrase, synonyms, formatting, whitespace, ordering, politeness), checked by reviewers to preserve the correct label.
2. Measures accuracy under each variant, the best-to-worst spread, and the share of items whose label stays the same across variants, with confidence intervals so that differences can be compared with sampling error.
3. Handles randomness: with stochastic decoding, repeats each condition several times to separate sampling variance from variance due to wording, or fixes the decoding settings and states them.
4. Reports the mean and worst case across variants rather than the best wording picked on the test data, with variants fixed in advance and any prompt tuning done on separate validation data.
5. Explains that an adversarial email is written or optimized to cause a wrong label or action (for example by embedding instructions to the model), which exploits the mixing of instructions and data, needs its own threat model and adaptive testing, and is not covered by passing paraphrase tests; mitigations include isolating untrusted text, limiting privileges and human review.

**Source:** Prompt sensitivity — the LLM-specific version of this problem

## ES-ch04.15

A paper reports a new defense for an image classifier with 88% accuracy under a one-step gradient-sign attack and 87% under a 10-step attack at the same L∞ budget, and claims state-of-the-art robustness. A reviewer notices that the defense includes random input transformations and a non-differentiable step, and finds that a black-box transfer attack from a surrogate model lowers accuracy to 35% at the same budget. Evaluate the claim: explain what the pattern of numbers suggests, which further experiments you would require, and what claim could responsibly be made.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the red flags: a black-box attack beating the white-box attacks, non-differentiable and random components, and almost no extra damage from ten steps, all pointing to gradient masking, so the high figures reflect attack failure and not insensitivity of the model.
2. Applies the upper-bound logic: accuracy under any real attack is an upper bound on worst-case accuracy, so the 35% result already shows worst-case accuracy at this budget is at most 35%, and the 88% claim is refuted under the paper's own threat model.
3. Requires adaptive attacks designed with knowledge of the defense (approximating the non-differentiable step with a differentiable one, averaging over the randomness), more steps and random restarts, and query-based black-box attacks.
4. Requires sanity checks and fuller reporting: accuracy should fall toward zero as the budget grows, results across several budgets and norms should be reported, and the minimum over all attacks with confidence intervals should be the headline.
5. States the claim that could be supported: robust accuracy is bounded by the lowest value found across a listed attack suite, reported with that suite and the residual risks, with any stronger claim requiring certification or verification.

**Source:** The robustness toolkit — what each tool does and what it costs

## ES-ch04.16

A team can deploy either a standard classifier (95% clean accuracy, 0% accuracy under a worst-case perturbation of fixed budget) or an adversarially trained one (85% clean accuracy, 50% under the same attack). Defend a deployment choice for each of two settings: (a) a spam filter where some senders actively craft evasive messages, and (b) a photo-tagging feature in a personal app with no adversary. State what further information you would want.

**Points:** 5

**Rubric (1 point each):**

1. States that the threat model decides which metric matters: in (a) adversaries probe and adapt, so worst-case accuracy is relevant, while in (b) there is no adversary, so clean accuracy and robustness to natural shift matter more.
2. Quantifies the trade: if a fraction f of inputs is attacked and the rest are clean, expected accuracy is 0.95(1 − f) for the standard model and 0.85(1 − f) + 0.5f for the robust one, which cross at f = 1/6 ≈ 17%, so the robust model wins when more than about one input in six is attacked at that budget.
3. Notes that neither number stands alone: the attack figure is an upper bound that depends on attack strength and budget realism, and the clean-accuracy cost may fall on particular slices.
4. Commits to a choice for each setting that follows from the stated threat model (for (a), either the robust model or the standard model with frequent retraining on new evasions can be defended if the adaptive-attacker issue is addressed; for (b), typically the standard model with natural-shift testing), and notes that in (a) adversaries adapt so static robustness decays, calling for retraining on new evasions, monitoring or human review.
5. Lists information to gather: realistic attacker budgets and share of adversarial traffic, relative costs of false positives and false negatives, per-slice and natural-shift accuracy, and compute and maintenance costs.

**Source:** Adversarial training and its scaling limits
