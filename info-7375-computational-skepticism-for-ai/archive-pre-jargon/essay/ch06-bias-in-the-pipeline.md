# Chapter 6: Bias, where it enters and who is responsible

## ES-ch06.1

A company wants to build a model that ranks job applicants for interview, trained on its own hiring and performance records from the past ten years. Take five different stages of the machine-learning pipeline, from the world that produced the data to the way the ranking is used. For each stage give one concrete way a disparity between groups could enter and one check that could detect it.

**Points:** 5

**Rubric (1 point each):**

1. Covers the world and history: past hiring and promotion decisions reflect earlier practices, so labels recording who was hired can encode earlier disparities even when the records are accurate; a check compares the label with an independent outcome measure or examines variation across decision-makers.
2. Covers sampling and representation: who appears in the data (applicants screened out earlier have no performance outcomes, and some groups may be thinly represented); a check compares the composition of the data with the population the model will be applied to.
3. Covers features and measurement: proxies for group (postcode, school, gaps in employment) or measurement that is noisier or more biased for some groups; a check predicts group from the features or ablates a suspect feature and watches the gap.
4. Covers model, objective and evaluation: training on average loss favours the largest group and pooled metrics hide weak subgroups; a check reports disaggregated metrics with uncertainty, including intersectional groups.
5. Covers deployment and use: how cutoffs and human reviewers act on the ranking and the feedback loop in which people hired under the model generate the next training data; a check tracks outcome rates by group at each decision stage after deployment.

**Source:** Three flavors of bias, mapped to the ten types

## ES-ch06.2

A bank removes the field "gender" from the inputs of its credit-scoring model and announces: "The model never sees gender, so it cannot discriminate by gender." Evaluate this claim. Explain what could still go wrong, how you would test for it, and what the bank should do in addition.

**Points:** 5

**Rubric (1 point each):**

1. Explains that other inputs correlated with gender (occupation, spending categories, part-time work history) let a model reconstruct much of the removed information, so outcomes can still differ by gender.
2. Explains that a model learns whatever predicts its training labels, so if the labels themselves record past disparities by gender, a model that fits them well can reproduce those disparities whichever inputs remain.
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
5. Names the information needed (why applicants chose different products, applicant risk within products) and concludes that the data alone support a description and a conditional claim, not a verdict on bias.

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
3. Describes a check on the label itself: compare promotion rates by group among employees with similar independently measured performance (not performance as rated by the same promoters), and look at variation across decision-makers and periods.
4. Describes options with their limits (a less biased outcome measure, relabelling or reweighing, constraints that reduce reliance on group-correlated signals), each trading fit to the past against fairness, and says how much to trade is a value judgement.
5. Notes that an alternative outcome measure has its own distortions, that deployment should be monitored, and that it may be right not to automate the decision when no defensible target exists.

**Source:** Ten mechanisms, distinguished

## ES-ch06.7

A lender approves loans only for applicants whose score exceeds a cutoff, and it learns whether a borrower defaults only if the loan was granted. The lender wants to retrain its model and to estimate how many creditworthy applicants it has been turning away. Explain why the observed data are a problem, what goes wrong if the lender trains and evaluates on approved applicants only, and describe at least two ways of addressing the problem together with the limits of each.

**Points:** 5

**Rubric (1 point each):**

1. Defines the problem: outcomes are observed only for applicants who received the favourable decision, and the earlier policy made that decision, so the labelled data are a selected subset rather than a random one.
2. Explains the consequences: performance measured on approved applicants does not describe performance on rejected ones, and error rates for rejected applicants, such as how many would have repaid, cannot be computed from the data at all.
3. Describes randomized exploration (approving a small random sample of applicants below the cutoff) as producing unbiased outcomes for the rejected region, and notes its cost and ethical considerations.
4. Describes a second approach such as reject inference, bounds or sensitivity analysis, or using natural variation in decision-makers' leniency, and states its cost: reject inference and leniency designs rely on assumptions (for example no unmeasured confounding) that cannot be verified from the data, while bounds give wide intervals and sensitivity analysis depends on assumed strengths of confounding.
5. Says findings should be reported with the uncertainty that comes from the unobserved region, and that the old policy's bias carries into any model trained naively on the approved applicants.

**Source:** Ten mechanisms, distinguished

## ES-ch06.8

A city uses a system that sends inspectors to the neighbourhoods with the most violations recorded last quarter. Two neighbourhoods have the same true violation rate, but one starts with more recorded violations. Explain how the system's decisions affect its own future data, what happens to the two neighbourhoods' records over time, why collecting more data does not correct this, and how the city could detect and break the loop.

**Points:** 5

**Rubric (1 point each):**

1. Explains the mechanism: violations are recorded where inspectors look, so the number recorded depends on inspection effort as well as on the true rate, and sending inspectors by past records makes new records reflect past allocation.
2. Explains the outcome: although the true rates are equal, the recorded imbalance persists (if inspectors are allocated in proportion to past records) or widens (if the allocation favours the leader more than proportionally), so the heavily inspected area keeps looking worse.
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
4. Identifies when none work well: when the labels are inaccurate for individuals (aggregate adjustment cannot repair individual errors), when measurement quality differs across groups, or when the gap arises in the downstream process (reviewers, cutoffs, feedback), because these methods act on the model's fit to the labels and the chosen metrics, not on the process that produced the gap.
5. States that the choice should follow a diagnosis of where the gap arises, that the effect must be checked on held-out data with uncertainty, and that improving one metric can worsen others.

**Source:** Leverage analysis — finding the high-leverage intervention point

## ES-ch06.10

A hospital system deploys a risk-prediction product built by a vendor, trained on a dataset assembled by a third party and labelled by clinicians at another institution. After deployment, patients from one group are found to be flagged less often at the same level of illness. Explain how responsibility should be mapped across the parties, what documentation would make that mapping inspectable (and what each document should contain), and what role an independent audit plays.

**Points:** 5

**Rubric (1 point each):**

1. Maps decisions to the parties who control them (data collection, labelling, model training, the cutoff and use in care, monitoring) and explains that accountability follows control, with the deploying hospital remaining accountable for its use of the tool.
2. Describes dataset documentation (for example a datasheet) covering how and why the data were collected, who is and is not represented, how and by whom labels were produced, known gaps and recommended uses; equivalent documents are accepted.
3. Describes model documentation (for example a model card) covering intended and out-of-scope uses, the evaluation data, performance broken down by subgroup with uncertainty, and known limitations; equivalent documents are accepted.
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
5. Describes remedies and their limits: recalibrate or replace the device, apply a validated correction to the readings, or use group-aware cutoffs, noting that correction and recalibration need gold-standard comparison data.

**Source:** Three flavors of bias, mapped to the ten types

## ES-ch06.14

A company's salary-recommendation model predicts salaries for women that are on average 8% lower than for men. When an audit compares predictions among employees at the same job level, the gap shrinks to 2%. Job level was assigned by promotion decisions made before the model was built. Explain what each figure answers, whether adjusting for job level is appropriate, what a "change only the group and hold everything else fixed" test can and cannot show, and what you would conclude.

**Points:** 5

**Rubric (1 point each):**

1. States that the 8% figure compares average predictions without conditioning (the association between group and prediction) and the 2% figure compares predictions among people at the same job level, so they answer different questions.
2. Explains that job level may be a mediator: if earlier promotion decisions were influenced by group, comparing within level removes the part of the gap that flows through those decisions and can understate disadvantage.
3. States that whether job level is a legitimate reason for pay differences (so the 2% is the relevant figure) or a channel of the disparity (so the 8% matters) is settled by causal assumptions and a normative judgement, not by the data alone.
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
5. Says the company should pin the model version where the provider offers that, re-run the audit when the provider changes the model, and keep records of tests and decisions so the assignment of responsibility can be checked later.

**Source:** A limit case: when the leverage is upstream of your pipeline — and who owns it then

## ES-ch06.16

A retailer wants to know whether giving customers a discount coupon (yes or no) keeps them from leaving (stays or leaves). Use this question to explain the three rungs of Pearl's ladder (association, intervention, counterfactual), giving one binary-outcome question the retailer could ask at each rung. Then explain why most machine learning sits on the first rung and what that means for how a model's output should be used.

**Points:** 5

**Rubric (1 point each):**

1. Defines rung 1 as association, the probability of an outcome given an observation, P(leaves | coupon), and gives a coupon example such as "do customers with coupons leave less often?"
2. Defines rung 2 as intervention, P(leaves | do(coupon)), what happens if the retailer sets the coupon rather than observes it, and distinguishes it from conditioning: observing a coupon holder can be entangled with why they received it, while setting it cuts those ties.
3. Defines rung 3 as a counterfactual about one specific case, such as "would this customer, who received no coupon and left, have stayed with one?", and notes that it requires reasoning about an outcome that was not observed.
4. Explains that most machine learning fits conditional probabilities from observed data, which is rung 1, and that this is enough for prediction when new cases resemble the training cases.
5. States the consequence: a predictive feature is not a lever, so acting on a model's output (changing a feature, setting a policy) needs experimental or causal evidence and a check that the population has not shifted; the model alone does not say what would happen if the retailer intervened.

**Source:** Pearl's Ladder — Rungs 1 and 2

## ES-ch06.17

A bank has 100,000 customers: 20,000 are engaged (active in its app in the last month) and 80,000 are not. It emailed 28,000 customers about a new credit card, 18,000 engaged and 10,000 not engaged. Among the engaged, 11.5% of the emailed and 10% of the non-emailed signed up. Among the non-engaged, 3.5% of the emailed and 2% of the non-emailed signed up. A manager reports that emailed customers signed up at 8.6% against 2.2% for the rest and concludes that the email works. Compute and explain the rung 1 comparison, draw the causal diagram that explains why it is misleading, show the rung 2 estimate, and describe the experiment that would give the same answer without any adjustment.

**Points:** 5

**Rubric (1 point each):**

1. Computes the raw comparison: 2,420 sign-ups out of 28,000 emailed (about 8.6%) against 1,600 out of 72,000 not emailed (about 2.2%), a difference of about 6.4 points, and identifies it as an association (rung 1).
2. Draws or describes the causal diagram: engagement points to both the email (the bank targeted engaged customers) and to sign-up, in addition to any arrow from the email to sign-up, so engagement is a common cause that confounds the raw gap.
3. Computes the stratified estimate: 11.5% against 10% among the engaged and 3.5% against 2% among the non-engaged, a 1.5-point effect in each group and 1.5 points overall when weighted by group size, and notes that the raw gap overstates the effect about fourfold.
4. Describes a randomized test: a coin flip decides who is emailed, which cuts the arrow from engagement to the email, and would be expected to give about 5.1% against 3.6% sign-up (a 1.5-point lift) in a population like this one.
5. States the assumptions behind the adjustment: engagement is the only common cause, it is measured, and emailed and non-emailed customers within each group are otherwise equivalent; unmeasured causes would remain a problem for adjustment but not for randomization.

**Source:** Pearl's Ladder — Rungs 1 and 2

## ES-ch06.18

A hospital wants to know whether a follow-up phone call after discharge (yes or no) reduces 30-day readmission (yes or no). It asks: "For the patients who were called, what would have happened if they had not been called?" Explain why this counterfactual question is at heart a data problem, how a comparison group is used to answer it, what makes a comparison group valid, and what remains uncertain even with a good one.

**Points:** 5

**Rubric (1 point each):**

1. Explains that each patient is observed under only one condition, called or not called, so the outcome without the call is missing for every called patient and cannot be measured directly.
2. Explains that the missing outcome is estimated from other patients who were not called, which stand in for the called patients, so the quality of the answer depends on how well the comparison group matches.
3. Describes ways to build a valid comparison: randomized assignment of calls, or matching, stratifying or weighting on measured variables (age, diagnosis, prior admissions) so the groups are equivalent on them.
4. States the key assumption: the groups must be equivalent on everything that affects readmission, including variables not measured (such as understanding of discharge instructions); matching on measured variables does not guarantee this, and the data alone cannot confirm it; randomization is stronger because it balances unmeasured factors in expectation.
5. Notes what remains uncertain: the result is an average for a group, not a certain statement about one patient, and requires overlap (called and uncalled patients of every kind), and further assumptions about how individuals respond are needed to say anything about a single patient.

**Source:** Pearl's Ladder — Rung 3, opened

## ES-ch06.19

Of 800 students who used a tutoring app, 600 passed a course (75%); of 1,200 who did not, 700 passed (about 58%). A university wants to know whether the app helps students pass. Describe three different causal stories that could produce this association, say what each predicts if the university set app use by force for a group of students, and explain how an experiment would tell the stories apart.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the association (75% against about 58%, a gap of about 17 points) as a rung 1 finding that does not by itself show cause.
2. Describes three stories: the app helps students pass (X causes Y); students who are already doing well are more likely to use the app (Y causes X, or prior success causes use); a third factor such as motivation or study habits causes both app use and passing.
3. States what each predicts under an intervention: if the app helps, assigning students to use it raises pass rates; if the arrow runs the other way, or a common cause drives both, assigning use leaves the pass rate unchanged.
4. Explains that setting use by force, ideally by random assignment, cuts the arrows into app use, so the difference in pass rates between the assigned groups reflects the app and not who chose it.
5. Notes practical limits: the experiment estimates an average effect for the students and conditions tested, possible non-compliance (assigned students not using the app), and that if an experiment is impossible, adjustment for measured common causes needs the explicit assumption that none are missing.

**Source:** Pearl's Ladder — Rungs 1 and 2

## ES-ch06.20

A company screened 200 applicants from each of two groups. It advanced 30 of the group A applicants (15%) and 60 of the group B applicants (30%). An analyst says the screening is biased against group A. Using Pearl's three rungs, explain what this finding does and does not show, describe a test that would answer a rung 2 question about the screening step, describe the counterfactual question a fairness claim about one applicant would raise, and explain what data would be needed to answer it.

**Points:** 5

**Rubric (1 point each):**

1. Computes the rung 1 gap: 15% against 30%, a difference of 15 points and a ratio of 0.5, and explains that this is an association; it does not show why the rates differ.
2. Lists several explanations consistent with the gap, such as differences in the applicant pools or qualifications, in how information was recorded, in the model or the reviewers, or in the cutoff, so that the gap alone does not locate the cause.
3. Describes a rung 2 test: an audit in which matched applications that are identical except for the group signal (such as the name) are submitted, or the screening rule is run on records with that input changed; differences in outcomes then reflect the screening step's response to that input.
4. States the rung 3 question for one applicant: would this person, who was not advanced, have been advanced had she been in the other group, with everything else about her held the same, and notes that it concerns an outcome that did not occur.
5. Explains that answering it requires comparison cases believed to be equivalent in every way that matters other than group, which is an assumption that cannot be fully verified; group often cannot be changed alone, so the answer depends on what is held fixed, and results should be reported as estimates with limits.

**Source:** Pearl's Ladder — Rungs 1 and 2

## ES-ch06.21

A coin lands heads with probability 0.7. A tiger beats a mouse in about 99% of fights. Two groups of people differ in how often they work in a certain occupation. Use these three cases to explain two different meanings of the word bias: a tilt in a process, and the bias of an estimator. Then explain how the definition a person should use depends on the problem, using three questions: describing the world, judging a number, and deciding about a person.

**Points:** 5

**Rubric (1 point each):**

1. Defines bias as a tilt in the world: a process whose probabilities depart from a symmetric or reference value, such as P(heads) = 0.7 against 0.5, P(tiger wins) near 0.99, or P(occupation | group A) differing from P(occupation | group B); notes that this is descriptive and neutral, not harmful by definition.
2. Defines the bias of an estimator as E[estimate] - true value, a property of a measurement process relative to a target, and shows that an estimate of 0.7 for the coin has bias zero while a constant estimate of 0.5 has bias -0.2.
3. Explains how the two connect: the world's tilt is the target (the true value), so an accurate estimate of a strong tilt is unbiased, and a skewed sample can give a biased estimate of a real tilt; a tilt in the world is not an estimator bias.
4. Maps the three questions to definitions: describing the world uses the tilt, such as P(A | B) against P(A | not B); judging a number uses estimator bias; deciding about a person asks whether the tilt is relevant and causally linked to the decision.
5. Gives a reason why the same tilt can be fine for one question and a problem for another, such as a size advantage in a fight being relevant to who wins a fight but not to who should be hired, or a group gap that arises from a past process versus one that arises from a rule.

**Source:** What "bias" actually means

## ES-ch06.22

A researcher builds a map of startups from a public directory. Of 3,167 startups on the map, 2,123 are in Region R (67%). The researcher expected Region R to have more startups than any other region but not this large a share, and suspects the data. Describe how to investigate: how an expectation differs from a check, which equation describes how the directory could skew the share, how to trace the source, what independent evidence would help, and what the fix would be.

**Points:** 5

**Rubric (1 point each):**

1. States that the map shows P(Region R | listed), which equals P(Region R | is a startup) only if being listed is independent of region, and that an expectation is a hypothesis to check, not a standard: an expectation can itself be biased.
2. Gives the selection relationship: with S = 1 for listed and Y = 1 for in Region R, E[Y | S = 1] - E[Y] = Cov(S, Y) / E[S]; no association between listing and region means no skew, and the covariance sets the size of the skew.
3. Describes tracing the source: count rows by where they came from (for example accelerator lists located in Region R), compute the Region R share within each source and outside the suspect source, and look for how listing rules favor some startups.
4. Describes independent evidence: a sample from a source not built from the same lists (such as business registrations or a random sample), compared on the Region R share, with the caveat that each source has its own coverage gaps.
5. Describes the fix: weighting works only on recorded variables and only if every kind of startup had some chance of being listed; where the source never recorded some startups, the fix is upstream in collection, and the result should be reported as the share among listed startups with the skew stated.

**Source:** Ten mechanisms, distinguished

## ES-ch06.23

A poll of 1,000 likely voters, treated as a simple random sample, finds candidate A at 48% and candidate B at 47%. A headline says "A leads." Compute the margin of error on a share, explain why the margin on the lead is larger, say how likely it is that A is truly ahead, state how many respondents would be needed to resolve a one-point lead with 80% power at 5% significance, and explain what the margin of error does not cover.

**Points:** 5

**Rubric (1 point each):**

1. Computes the margin on a share: 1.96 x sqrt(0.25 / 1,000), about 3.1 percentage points.
2. Explains that the standard error of the lead is sqrt((p1 + p2 - d squared) / n), about 3.1 points, so its 95% margin is about 6 points, roughly double, because one candidate's gain is the other's loss.
3. States that a one-point lead is well inside that margin, and that the chance A is truly ahead is about 63% (z = 0.32), close to a coin flip, so the headline overstates the evidence.
4. Gives the sample size for 80% power: about (1.96 + 0.84) squared x 0.95 / 0.01 squared, roughly 75,000 respondents, and notes that halving the margin takes four times the sample.
5. Explains that the margin covers random sampling error only: not who is left out of the frame, non-response, question wording, or weighting that cuts the effective sample size, so a poll with a tiny margin can still be wrong.

**Source:** Ten mechanisms, distinguished

## ES-ch06.24

In a population of 500,000 women and 500,000 men, 600 women and 1,400 men are data scientists. A separate professional league, by its rules, has only male players. A manager says: "The gap in data science is bias, and so is the gap in the league." Using conditional probabilities, explain what the numbers show, what the equations can and cannot tell us, where each gap enters, and which fairness checks apply.

**Points:** 5

**Rubric (1 point each):**

1. Computes and reads the conditional probabilities: P(data scientist | woman) = 0.12% and P(data scientist | man) = 0.28%, a ratio of about 0.43; P(woman | data scientist) = 30% is a different quantity; and for the league the rates are 0 and a small positive number, a ratio of 0.
2. Explains that these are tilts in the world and in the data, descriptive of how the groups differ, and that the equations do not say whether a gap is legitimate or caused by group membership.
3. Contrasts where each gap enters: the league's gap is created by a rule, so a model predicting membership can be accurate and the question belongs to the rule's owner; the occupation gap passes through several stages (who enters the field, how people are hired and titled, history), and a model trained on past outcomes can carry it forward.
4. Applies the rungs: P(Y | group) is a rung 1 association; whether group causes the outcome through a review step is a rung 2 question that can be tested by changing what the reviewer sees; whether one person would have been hired had she been in the other group is a rung 3 question.
5. States the fairness checks and their conflict: demographic parity compares selection rates; equalized odds compares error rates among the qualified and unqualified; calibration compares score meaning; when base rates differ, a perfect predictor satisfies equalized odds and calibration but not demographic parity, so the choice of criterion depends on the decision and its harms.

**Source:** Pearl's Ladder — Rungs 1 and 2
