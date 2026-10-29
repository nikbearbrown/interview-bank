# Chapter 6: Bias, where it enters and who is responsible

## ES-ch06.1

A company wants to build a model that ranks job applicants for interview, trained on its own hiring and performance records from the past ten years. Take five different stages of the machine-learning pipeline, from the world that produced the data to the way the ranking is used. For each stage give one concrete way a disparity between groups could enter and one check that could detect it.

**Points:** 5

**Rubric (1 point each):**

1. Covers the world and history: past hiring and promotion decisions reflect earlier practices, so labels recording who was hired can encode earlier disparities even when the records are accurate; a check compares the label with an independent outcome measure or examines variation across decision-makers.
2. Covers sampling and representation: who appears in the data (applicants screened out earlier have no performance outcomes, and some groups may be thinly represented); a check compares the composition of the data with the population the model will be applied to.
3. Covers measurement, labels and features: proxies for group (postcode, school, gaps in employment) or measurement that is noisier or more biased for some groups; a check predicts group from the features or ablates a suspect feature and watches the gap.
4. Covers model, objective and evaluation: training on average loss favours the largest group and pooled metrics hide weak subgroups; a check reports disaggregated metrics with uncertainty, including intersectional groups.
5. Covers deployment and use: how cutoffs and human reviewers act on the ranking and the feedback loop in which people hired under the model generate the next training data; a check tracks outcome rates by group at each decision stage after deployment.

**Source:** Three flavors of bias, mapped to the ten types

## ES-ch06.2

A bank removes the field "gender" from the inputs of its credit-scoring model and announces: "The model never sees gender, so it cannot discriminate by gender." Evaluate this claim. Explain what could still go wrong, how you would test for it, and what the bank should do in addition.

**Points:** 5

**Rubric (1 point each):**

1. Explains that other inputs correlated with gender (occupation, spending categories, part-time work history) let a model reconstruct much of the removed information, so outcomes can still differ by gender.
2. Explains that a model learns whatever predicts its training labels, so if the labels reflect past disparities by gender the model can reproduce them through correlated inputs.
3. Describes a test for proxies, such as trying to predict gender from the remaining inputs (high accuracy means the information is present) and comparing outcomes by gender or re-scoring with suspect inputs removed.
4. Notes that correlation with gender does not by itself show improper use, because a correlated input may carry legitimate information about repayment, so inputs should be judged by their effects and by the cost of dropping them.
5. Notes that deleting the attribute also removes the ability to measure outcomes by group, so the field should be retained for auditing where the law allows, and that mitigation at other stages should be considered.

**Source:** Leverage analysis — finding the high-leverage intervention point

## ES-ch06.3

A hospital audit finds that a triage model refers 24% of patients from group X (1,200 of 5,000) to a specialist programme and 15% of patients from group Y (450 of 3,000), a ratio of 1.6, and the difference is far too large to be chance. A manager concludes: "The model is biased against group Y." Explain why the gap alone does not establish this, and design an investigation that would separate the possible causes. For each test, say what it can and cannot show.

**Points:** 5

**Rubric (1 point each):**

1. States that the gap is a descriptive measurement consistent with several causes, such as differences in clinical need, in how the data were collected, in labels, in the model, in cutoffs or in downstream review, and that its size or significance does not say which.
2. Proposes stratifying or adjusting for clinically legitimate variables (severity, diagnosis) to see whether the gap persists among comparable patients, and notes the limits: unmeasured factors, and adjustment variables that may themselves be shaped by group.
3. Proposes a matched or counterfactual comparison, such as scoring paired records that differ only in group-related inputs, and notes that it shows whether the model's output depends on those inputs but not why the populations differ, and that group often cannot be changed alone.
4. Proposes ablating or substituting one pipeline stage at a time (labels, individual features, the cutoff, the human review step) and tracking how the gap changes, to locate where it arises.
5. Reports uncertainty and alternatives: confidence intervals, a plan for subgroups, and the point that results narrow the hypotheses rather than prove a cause, with the remaining explanations stated.

**Source:** Pearl's Ladder — Rungs 1 and 2

## ES-ch06.4

A lender reports approval counts for two groups across two loan products. Secured loans: group P has 70 approvals out of 100 applications and group Q has 300 out of 500. Unsecured loans: group P has 150 out of 500 and group Q has 20 out of 100. An analyst says the aggregate figures show group P is treated worse than group Q. Compute the rates, explain how the comparison can reverse once the product is considered, say which comparison should be reported and what further information you would need to decide, and state what you can and cannot conclude.

**Points:** 5

**Rubric (1 point each):**

1. Computes the rates: group P is approved for 70% of secured and 30% of unsecured applications (220 of 600, about 36.7%, overall) and group Q for 60% and 20% (320 of 600, about 53.3%, overall), so P is ahead within each product but behind overall.
2. Explains the arithmetic: each overall rate is an average of the product rates weighted by that group's application mix, and group P applies mostly for the low-approval unsecured product while group Q applies mostly for the secured one.
3. Describes a standardized comparison on a common product mix (for example a 50/50 mix gives 50% for P and 40% for Q) as a way to compare the groups on equal footing.
4. States that neither table is automatically correct: if product choice is independent of the lender's process the within-product comparison is fairer, but if the lender steers groups into products the overall gap may reflect real disadvantage that stratifying hides.
5. Names the information needed (why applicants chose different products, applicant risk within products, who set the mix) and concludes that the data alone support a description and a conditional claim, not a verdict on bias.

**Source:** How bias types compound

## ES-ch06.5

A team reports that its classifier is 96.5% accurate on a 12,000-example test set. A subgroup of 300 test examples has 36 errors (a 12% error rate, with a 95% interval of about 8.8% to 16.2%), against about 3.3% error on the other 11,700 examples. The subgroup can be split further by a second attribute into four cells of roughly 75 examples each. Explain what the headline number hides and design an evaluation that reports performance by subgroup responsibly, including how to treat the small cells.

**Points:** 5

**Rubric (1 point each):**

1. Explains that overall accuracy is a size-weighted average dominated by the large group, so a subgroup with a much higher error rate (12% against 3.3%) can sit behind an excellent headline figure.
2. Requires disaggregated metrics, including the error types that matter (false positives and false negatives), reported for each subgroup rather than only pooled.
3. Requires uncertainty on every subgroup figure and explains that cells of about 75 examples give wide intervals (a 12% error rate on 75 examples is roughly 6% to 21%), so a non-significant difference does not show parity.
4. Addresses intersections and multiplicity: crossing attributes multiplies the number of cells, small cells need more data or deliberate oversampling for the audit, and subgroups should be chosen before looking at results or corrected for multiple comparisons to limit chance findings.
5. Says the test data should resemble the deployment population and that the report should state what cannot be concluded from cells that remain too small.

**Source:** How bias types compound

## ES-ch06.6

A firm trains a model to predict who will be promoted, using ten years of its own promotion records, and finds the model is highly accurate on held-out records. In those years promotions went to one group at a higher rate than to others with comparable measured performance. Argue whether the model's accuracy is evidence that it is fair, explain why standard data-quality checks may find nothing wrong, and describe what the firm could do about the label.

**Points:** 5

**Rubric (1 point each):**

1. Explains that the label records what decision-makers did, not what ought to have happened, so a model that predicts it well reproduces past patterns and its accuracy measures fidelity to the past rather than fairness.
2. Explains that the records can be complete, correctly entered and representative and still carry the disparity, so data-quality and sampling checks do not detect it.
3. Describes a diagnostic: compare promotion rates by group among employees with similar independently measured performance, and look at variation across decision-makers or periods.
4. Describes options with their limits (a less biased outcome measure, down-weighting earlier periods, constraints that reduce reliance on group-correlated signals), each trading fit to the past against fairness, and says how much to trade is a value judgement.
5. Notes that an alternative outcome measure has its own distortions, that deployment should be monitored, and that it may be right not to automate the decision when no defensible target exists.

**Source:** Ten mechanisms, distinguished

## ES-ch06.7

A lender approves loans only for applicants whose score exceeds a cutoff, and it learns whether a borrower defaults only if the loan was granted. The lender wants to retrain its model and to estimate how many creditworthy applicants it has been turning away. Explain why the observed data are a problem, what goes wrong if the lender trains and evaluates on approved applicants only, and describe at least two ways of addressing the problem together with the limits of each.

**Points:** 5

**Rubric (1 point each):**

1. Defines the problem: outcomes are observed only for applicants who received the favourable decision, and the earlier policy made that decision, so the labelled data are a selected subset rather than a random one.
2. Explains the consequences: performance measured on approved applicants does not describe performance on rejected ones, and error rates for rejected applicants, such as how many would have repaid, cannot be computed from the data at all.
3. Describes randomized exploration (approving a small random sample of applicants below the cutoff) as producing unbiased outcomes for the rejected region, and notes its cost and ethical considerations.
4. Describes a second approach such as reject inference, bounds or sensitivity analysis, or using natural variation in decision-makers' leniency, and states that these rely on assumptions (for example no unmeasured confounding) that cannot be verified from the data.
5. Says findings should be reported with the uncertainty that comes from the unobserved region, and that the old policy's bias carries into any model trained naively on the approved applicants.

**Source:** Ten mechanisms, distinguished

## ES-ch06.8

A city uses a system that sends inspectors to the neighbourhoods with the most violations recorded last quarter. Two neighbourhoods have the same true violation rate, but one starts with more recorded violations. Explain how the system's decisions affect its own future data, what happens to the two neighbourhoods' records over time, why collecting more data does not correct this, and how the city could detect and break the loop.

**Points:** 5

**Rubric (1 point each):**

1. Explains the mechanism: violations are recorded where inspectors look, so the number recorded depends on inspection effort as well as on the true rate, and sending inspectors by past records makes new records reflect past allocation.
2. Explains the outcome: the initial imbalance is self-confirming, equal true rates still produce records that show the heavily inspected area as worse, and an allocation rule that rewards the leader more than proportionally makes the gap grow.
3. Explains that more data from the same process cannot correct it, because every new record is shaped by the allocation, so the estimate stays biased even as it becomes more precise.
4. Describes detection: compare the records with a measurement independent of inspector presence (complaints, surveys, random inspections) and check whether recorded rates track effort, for example by looking at rates per inspection hour.
5. Describes ways to break the loop: randomized or exploratory allocation of some effort, normalizing counts by effort, limits on how far allocation follows past records, and periodic audits.

**Source:** Leverage analysis — finding the high-leverage intervention point

## ES-ch06.9

A screening model selects 40% of applicants from group A and 20% from group B. The team wants to narrow this gap. Describe how a pre-processing, an in-processing and a post-processing approach would each work, the main limitation of each, and the circumstances in which none of the three would address the real problem.

**Points:** 5

**Rubric (1 point each):**

1. Describes a pre-processing approach (reweighing or resampling the training examples, relabelling, or removing or transforming features) and its limitation: it changes the data the model sees but does not guarantee fair predictions or correct inaccurate labels for individuals.
2. Describes an in-processing approach (a fairness penalty or constraint in the training objective, or adversarial training) and its limitation: it needs group information during training, gives up some agreement with the training labels, and satisfies only the chosen criterion.
3. Describes a post-processing approach (group-specific cutoffs or adjusted scores) and its limitation: it works with any trained model but treats applicants with the same score differently by group, needs group at decision time, and leaves the learned scores unchanged.
4. Identifies when none work: when the disparity comes from a biased label, from measurement of differing quality across groups, or from the downstream process (reviewers, cutoffs, feedback), because these methods operate on the model's fit to the labels and the metrics.
5. States that the choice should follow a diagnosis of where the gap arises, that the effect must be checked on held-out data with uncertainty, and that improving one metric can worsen others.

**Source:** Leverage analysis — finding the high-leverage intervention point

## ES-ch06.10

A hospital system deploys a risk-prediction product built by a vendor, trained on a dataset assembled by a third party and labelled by clinicians at another institution. After deployment, patients from one group are found to be flagged less often at the same level of illness. Explain how responsibility should be mapped across the parties, what documentation would make that mapping inspectable (and what each document should contain), and what role an independent audit plays.

**Points:** 5

**Rubric (1 point each):**

1. Maps decisions to the parties who control them (data collection, labelling, model training, the cutoff and use in care, monitoring) and explains that accountability follows control, with the deploying hospital remaining accountable for its use of the tool.
2. Describes a datasheet for the dataset: how and why the data were collected, who is and is not represented, how and by whom labels were produced, known gaps and recommended uses.
3. Describes a model card for the model: intended and out-of-scope uses, the evaluation data, performance broken down by subgroup with uncertainty, and known limitations.
4. Describes an independent audit: the auditor can access or query the model and data, reproduces the reported numbers, tests subgroups the developer did not choose, and records the model version evaluated.
5. States the limits: documents are disclosures that can be incomplete or out of date, they do not make a system fair, and they must be kept current and used in procurement and monitoring decisions for responsibility to be inspectable.

**Source:** A limit case: when the leverage is upstream of your pipeline — and who owns it then

## ES-ch06.11

A classifier has a true positive rate of 75% and a false positive rate of 10% in each of two groups. The base rate (the share who are truly positive) is 20% in group 1 and 40% in group 2. Compute the positive predictive value (the share of flagged people who are truly positive) in each group. Then explain what this shows about trying to equalize error rates and positive predictive value at the same time, state the conditions under which the conflict disappears, and say who should decide how to resolve it.

**Points:** 5

**Rubric (1 point each):**

1. Computes a positive predictive value of about 65.2% for group 1 and about 83.3% for group 2 (0.15 / 0.23 and 0.30 / 0.36).
2. Explains the mechanism: PPV depends on the base rate as well as on the error rates, PPV = p x TPR / (p x TPR + (1 - p) x FPR), so equal TPR and FPR with different base rates give different PPV.
3. Shows that equalizing PPV would require different error rates (for example, keeping TPR at 75%, group 2's FPR would have to rise to about 26.7%), so the criteria cannot all hold together.
4. States the assumptions: the conflict arises when base rates differ and the classifier is imperfect, and it disappears when base rates are equal or the classifier is perfect.
5. Says the choice among criteria is a values decision about which errors are more costly and who bears them, to be made and documented by accountable parties with affected people consulted, and notes that unequal base rates may themselves reflect measurement or historical distortions worth examining.

**Source:** The dataset as epistemic artifact

## ES-ch06.12

A vendor makes three claims about its hiring model. (1) "Bias is not a concern because the model was trained on 20 million records." (2) "The model has 94% accuracy for every group on held-out data from our own pipeline, so it is fair." (3) "We tested one fairness metric and the model passes." Critique each claim and say what evidence would actually support a claim of fairness.

**Points:** 5

**Rubric (1 point each):**

1. Critiques claim 1: bias in the statistical sense is a systematic offset of an estimate from its target, which does not shrink with sample size, so more data from the same biased process only makes the biased estimate more precise.
2. Critiques claim 2: held-out data from the same pipeline shares the same sampling, labelling and measurement distortions, so equal accuracy shows consistency with the pipeline rather than with the world or the intended outcome.
3. Notes that equal accuracy across groups can coexist with different false-positive and false-negative rates, different selection rates and unequal harms, so accuracy parity does not cover the errors that matter.
4. Critiques claim 3: passing one metric shows only that one criterion holds, criteria can conflict when base rates differ so the choice must be justified by the harms of the deployment, and passing says nothing about labels or downstream use.
5. States what would support a fairness claim: an audit set with independently produced labels, disaggregated errors with intervals, intersectional cells, examination of the labels and of the deployment process, and outcome monitoring after deployment.

**Source:** What "bias" actually means

## ES-ch06.13

A screening programme flags a patient for follow-up if a device reading is below 92. In both groups the true values are normally distributed with mean 94 and standard deviation 3. For group A the device reads the true value accurately. For group B it reads 2 units too high. Compute the share of each group that is flagged and the share of group B's patients with a true value below 92 who are flagged. Explain what kind of error this is, why more data or a better classifier on the readings will not fix it, how it could be detected, and what could be done.

**Points:** 5

**Rubric (1 point each):**

1. Computes that about 25.2% of group A is flagged and about 9.1% of group B, and that only about 36% of group B patients whose true value is below 92 are flagged (all of the corresponding group A patients are flagged).
2. Identifies this as measurement bias: the instrument errs systematically for one group, so the recorded value is a distorted measure of the quantity of interest and the same cutoff does not mean the same thing in both groups.
3. Explains that more data of the same kind, or a better model trained on the same readings, reproduces the offset, because the distortion is in the inputs rather than in the learning.
4. Describes detection: compare the device readings with an independent gold-standard measurement within each group and look at residual patterns by group, rather than relying on the readings alone.
5. Describes remedies and their limits: recalibrate or replace the device, apply a validated correction to the readings, or use group-aware cutoffs, all of which need gold-standard data and a named owner of the instrument.

**Source:** Three flavors of bias, mapped to the ten types

## ES-ch06.14

A company's salary-recommendation model predicts salaries for women that are on average 8% lower than for men. When job level is added as a control, the gap shrinks to 2%. Job level was assigned by promotion decisions made before the model was built. Explain what each figure answers, whether controlling for job level is appropriate, what a "change only the group and hold everything else fixed" test can and cannot show, and what you would conclude.

**Points:** 5

**Rubric (1 point each):**

1. States that the 8% figure compares average predictions without conditioning (the association between group and prediction) and the 2% figure compares predictions among people at the same job level, so they answer different questions.
2. Explains that job level may be a mediator: if earlier promotion decisions were influenced by group, controlling for it removes the part of the gap that flows through those decisions and can understate disadvantage, whereas if level is an independent and legitimate reflection of qualifications the 2% is the more relevant figure.
3. States that which paths are acceptable is settled by causal assumptions and a normative judgement, not by the data alone.
4. Explains that a "change only group" test is an intervention on the model's input or on an assumed causal model, that it shows whether the output depends on group-related inputs, and that holding other features fixed can be incoherent when they are consequences of group.
5. Concludes that neither number alone establishes discrimination or its absence, recommends reporting both with their assumptions, and notes that evidence about the real-world cause needs further design such as audit studies, natural experiments or examination of the promotion process.

**Source:** Pearl's Ladder — Rungs 1 and 2

## ES-ch06.15

A company deploys a customer-support assistant built on a language model that it licenses from a provider. Testers find that the assistant's answers differ in quality and tone across groups of customers in ways that the company's own prompts, data and code do not explain. Explain how the company should investigate, what it can and cannot do if the cause lies in the provider's model, and how responsibility should be divided.

**Points:** 5

**Rubric (1 point each):**

1. Describes an investigation of the assistant as a black box: paired prompts that differ only in group-related content, disaggregated evaluation on the company's own traffic, and repeated runs because outputs vary from run to run.
2. Says to separate the paths: check whether the company's prompts, retrieved content and post-processing contribute (by ablating or replacing them) before attributing the difference to the provider's model.
3. Lists the company's options if the cause lies upstream (switch or add providers, constrain the scope of use, add checks or human review on outputs, or decline to deploy for sensitive decisions) and notes each option's limits, for example that filters catch only what they can detect.
4. Assigns responsibility by control: the company remains accountable for deploying the assistant and for the outcomes of its use, while the provider is accountable for documenting model behaviour, known limitations and changes, and contracts should secure access and notice.
5. Says the company should pin the model version, re-run the audit when the provider changes the model, and keep records of tests and decisions so the assignment of responsibility can be checked later.

**Source:** A limit case: when the leverage is upstream of your pipeline — and who owns it then
