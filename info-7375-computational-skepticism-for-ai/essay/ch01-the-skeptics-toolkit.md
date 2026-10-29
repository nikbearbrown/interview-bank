# Chapter 1: The skeptic's toolkit

## ES-ch01.1

A vendor claims that its meeting-summarization assistant "saves our managers time." Explain how you would turn this plausible-sounding claim into an explicit prediction, a list of assumptions, and a falsification test. Give a concrete version of each for this claim, and say what makes the result a test rather than a description.

**Points:** 5

**Rubric (1 point each):**

1. States a prediction that names a measurable quantity, a defined population and a direction of change, for example minutes per week spent on meeting follow-up for a defined group of managers being lower with the assistant.
2. Names a comparison or baseline, such as a before-and-after measurement with a control group or a randomized or matched comparison, so that a change can be attributed to the assistant rather than to the calendar.
3. Lists assumptions that could fail and can be inspected, for example that time is measured from logs and not only from self-report, that managers do not spend the saved time re-checking inaccurate summaries, and that the trial group resembles the managers the claim is meant to cover.
4. Gives a falsifier fixed in advance with a threshold and a window, such as no reduction of at least a stated number of minutes per week over four weeks, or an increase in correction time, so that a specific result counts against the claim.
5. Explains that the criteria are set before the results are seen and that a claim compatible with every outcome, such as "saves time" with no baseline or threshold, is not testable because no result could count against it.

**Source:** What I mean by skepticism

## ES-ch01.2

Two reviewers comment on a team's claim that a classifier "generalizes well to new hospitals." Reviewer 1 writes: "I'm not convinced this will hold up in the real world." Reviewer 2 writes: "Evaluate on the three hospitals that were not in the training data, using the same labelling protocol; if AUROC at any of them falls below 0.80, I will treat the claim as refuted." Explain which comment does more for the team and why. Define what makes a falsifier checkable, and say what useful role, if any, a general expression of doubt still plays.

**Points:** 5

**Rubric (1 point each):**

1. Defines a checkable falsifier as a statement of an observation (data, metric, threshold and procedure) that would count against the particular claim, specific enough that two people would agree on whether it occurred.
2. Identifies Reviewer 2's comment as meeting this standard because it names a population, a metric, a threshold and a consequence, and notes that the claim could actually fail the test.
3. Explains that Reviewer 1's comment names no observation, so no result could satisfy it and the team can only respond by asserting confidence; it is compatible with every outcome.
4. Notes the limits of Reviewer 2's test: passing shows the claim survived this test and not that it holds everywhere, and the threshold, the choice of hospitals and the metric each need justification.
5. Gives the legitimate role of general doubt as a prompt for generating hypotheses about what could be wrong, such as differences in scanners or patient mix, which then must be converted into specific tests.

**Source:** What I mean by skepticism

## ES-ch01.3

A data scientist trains several model variants, looks at the validation results, and then writes a clear and plausible explanation of why one variant won. A colleague writes down a prediction and a decision rule before running the same comparison. Explain why the colleague's prediction is stronger evidence than the data scientist's explanation even when both agree with the data. Describe the mechanisms that weaken the after-the-fact account and the practical steps that preserve the strength of a prediction.

**Points:** 5

**Rubric (1 point each):**

1. Explains that an account built after the result can be fitted to whichever outcome occurred (hindsight), so its agreement with the data is guaranteed and carries little information.
2. Explains that a prediction made beforehand could have been wrong, so its success discriminates between the hypothesis and its alternatives; surviving a risky test is what counts as evidence.
3. Names the multiple-comparisons or forking-paths problem: many subgroups, metrics or analyses can be examined after seeing the data and some will look significant by chance, for example 20 independent tests at the 5% level give about a 64% chance of at least one hit with no true effect.
4. Describes practical steps: record the prediction, metric, threshold and analysis plan in a dated record before the run, do not edit it afterward, and append observations separately.
5. Handles exploratory findings correctly by treating post hoc patterns as hypotheses to test on new data, and by reporting which analyses were planned and which were exploratory.

**Source:** What I mean by skepticism

## ES-ch01.4

An engineer asks an LLM why a deployed model's accuracy fell from 91% to 84% last month. The LLM, which was given only those two numbers, answers with a polished, confident, three-paragraph explanation blaming a "seasonal shift in input vocabulary." The engineer is tempted to report this to management as the cause. Explain what evidence the claim "a seasonal vocabulary shift caused the drop" needs, what the explanation does and does not supply, and how you would test it.

**Points:** 5

**Rubric (1 point each):**

1. Explains that polished form is not evidence about content, since fluent text can be produced for true and false claims alike, and that the model saw only two numbers so its specifics cannot come from the system's data.
2. States that a causal claim needs evidence that distinguishes it from alternatives such as a data pipeline change, a labelling change, a shift in class mix, an upstream bug or a change in the evaluation set.
3. Proposes concrete checks that could contradict the explanation, such as comparing input vocabulary between the two months, breaking errors down by slice, and confirming that labels and metric computation were unchanged.
4. Proposes an intervention or counterfactual test, such as adapting the model to the new vocabulary and seeing whether accuracy recovers, with the prediction stated before the test is run.
5. Describes honest reporting: the explanation is an unverified hypothesis until a test supports it, and the report should say what was checked and what was not.

**Source:** The fluency trap

## ES-ch01.5

A team builds a pipeline in which one language model drafts summaries of legal clauses and a second language model, from a different vendor, "verifies" each summary by reading the clause and the summary and replying "correct" or "incorrect." The team reports that the verifier agrees with the drafter on 97% of summaries and concludes that the summaries are verified. Critique this conclusion, and describe how you would build a check whose agreement would mean something.

**Points:** 5

**Rubric (1 point each):**

1. Notes that agreement between two models measures agreement and not correctness, since neither is ground truth and both can be wrong in the same way.
2. Explains how shared assumptions weaken independence: overlapping training data, similar architectures and failure modes, the same input read in the same way, and a verifier that sees the drafter's summary and may anchor on it, so their errors are correlated.
3. Points out that 97% agreement means little without knowing how the verifier performs on summaries known to be wrong, and proposes measuring its sensitivity on a labelled or deliberately corrupted set.
4. Proposes a check grounded outside the models, such as domain experts reviewing a random sample against the source clause, a labelled dataset with known answers, or programmatic checks that extracted dates, amounts and clause numbers match the source text.
5. States that independence is a matter of degree that has to be argued, that the check's measured error rates and sample should be reported, and that a named person remains responsible for the conclusion.

**Source:** The solve-verify asymmetry

## ES-ch01.6

An automation agent reports: "I rotated the API keys for all 14 services and revoked the old ones." A manager is ready to close the security ticket. Explain the difference between the agent's report and the state of the world it describes, then design a verification procedure that does not rely on the agent's own account. Say what that procedure can and cannot establish.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the report, which is something the agent produced and may reflect only that commands were issued or returned success, from the real state of what each service accepts.
2. Lists ways the report could be wrong, such as services that were missed or silently failed, new keys not deployed to dependent systems, old keys still valid because revocation lagged or failed, and a service list that is itself incomplete.
3. Designs checks against actual state, such as attempting to authenticate with each old key and confirming rejection, confirming that the new keys work, reading each service's key list or audit log, and reconciling the 14 against an independently maintained inventory.
4. Notes that the checks draw on sources independent of the agent, such as service-side logs and a separately obtained inventory, and are run against the live system and not a copy or a summary.
5. States the limits: the checks cover the services and keys examined at the time they were run, copies of old keys or unlisted services remain unaddressed, and the result should be recorded as what was verified and what remains unknown, with a named person closing the ticket.

**Source:** The slice

## ES-ch01.7

A product manager says: "We ran 300 randomly sampled production-like requests through the new triage model and saw zero serious errors. The serious-error rate is zero, so we can ship." The system will handle about 200,000 requests per month. Respond to this argument with appropriate statistical reasoning, including a numerical bound, and say what additional information you would need before deciding.

**Points:** 5

**Rubric (1 point each):**

1. States that zero observed failures in a finite sample does not establish a zero rate, because no finite sample can confirm that failures are absent.
2. Gives a quantitative bound: with 0 failures in 300 independent trials, the one-sided 95% upper bound on the failure rate is about 3/300, or 1%.
3. Translates the bound to volume: a rate of up to 1% across 200,000 monthly requests is consistent with the data and would mean up to about 2,000 serious errors per month, so the decision depends on the tolerable rate and the severity.
4. Questions representativeness, since the bound holds only for the population sampled and assumes independent trials, and rare subgroups, adversarial inputs and post-launch shift are not covered.
5. Recommends next steps, such as targeted stress tests aimed at likely failures, a staged rollout with monitoring and a stopping threshold stated in advance, and a stricter requirement where errors are severe.

**Source:** What I mean by skepticism

## ES-ch01.8

A claims department adopts a model that drafts 5,000 decision letters a day. A trained reviewer needs about 6 minutes to check one letter against the claim file. Discuss the relationship between the cost of generating and the cost of verifying outputs like these, why ignoring it creates risk, and how you would design a verification plan under a limited reviewer budget. State the limits of any general claim you make about generating versus verifying costs.

**Points:** 5

**Rubric (1 point each):**

1. Explains that producing a letter is cheap and fast while checking it requires a trained person reading against the file, and computes that full review would take about 5,000 x 6 minutes, or 500 reviewer-hours per day.
2. Hedges the principle: for some problems verification is cheaper than production, such as multiplying given factors or running a test, while for others no cheap check exists, so the relationship depends on the task and on whether a ground truth is available.
3. Explains the risk of not budgeting for checking: unchecked outputs look fine by default, and errors accumulate at scale until they surface as harm.
4. Designs a plan with risk tiering (full review of high-stakes letters), random sampling with a stated detection target (for example about 150 letters per day to have a 95% chance of catching at least one error when the error rate is 2%), automated checks on fields that can be checked mechanically, and escalation when sampled error rates rise.
5. Notes that sampling estimates the error rate without verifying the unsampled letters, that the plan should state what is covered and what is not, that a named owner accepts the residual risk, and that using another model to check does not remove the need for a ground-truth anchor.

**Source:** The solve-verify asymmetry

## ES-ch01.9

A company wants an AI agent to prepare and submit changes to production prices. Management says "a human approves every change," and the plan is a single Approve button shown beside the agent's own summary of the change. Explain what is missing for the approval to carry real responsibility, and design the approval step so that a named person can be accountable for the decision.

**Points:** 5

**Rubric (1 point each):**

1. Identifies that an approval is meaningful only if the approver sees what will change, such as a concrete before-and-after difference and its scope, and not only the agent's summary of it.
2. Requires that the approver has the knowledge, the authority to refuse and the time to review, and flags rubber-stamping and over-reliance on automated suggestions when volume is high.
3. Specifies a named accountable person or role recorded with each decision, so that responsibility does not dissolve into the system, and states that an AI component cannot be held answerable for the choice.
4. Specifies the evidence shown to the approver: checks run against actual state, such as a preview computed from the real price table, a statement of what was not checked, and how the change can be rolled back, with a record of what was shown, who approved and when.
5. Explains that the decision to approve, revise or stop stays with the human, including stopping when a check is unknown or fails, and that approval rates, review time and rejection rates are monitored to detect superficial review.

**Source:** The Five Supervisory Capacities

## ES-ch01.10

You evaluated a speech-to-text system for a clinic. You tested it on 120 recordings, all made in a quiet room by 6 native English speakers, and it transcribed 114 correctly (95%) under your scoring rule. You did not test noisy environments, non-native accents, or medical terms beyond a short list. Write the claims you can and cannot support, and explain why a verification report should state what was and was not checked. Include how you would label the status of the untested conditions.

**Points:** 5

**Rubric (1 point each):**

1. States the supportable claim narrowly: in quiet rooms, with these 6 native speakers and these recordings, 114 of 120 (95%) were transcribed correctly under the stated scoring rule, and notes that so few speakers limits generalization even within that group.
2. Notes statistical uncertainty: 114 of 120 carries a 95% interval of roughly 90% to 98%, so the figure should not be presented as precise.
3. Says the untested conditions (noise, accents, vocabulary) must be reported as unknown or not evaluated, not as passing or assumed acceptable, because no failures were seen where nothing was tested.
4. Explains the purpose: readers will make decisions from the report, omitted limits transfer risk to people who do not know about them, and an honest scope lets others judge whether the evidence applies to their setting.
5. Recommends a report format with scope, method, sample, criteria fixed beforehand, results, a pass, fail or not-tested status for each condition, and next tests, using wording that does not imply the whole system was verified.

**Source:** Skepticism as a team practice

## ES-ch01.11

A hospital system trains a model to rank patients for a care-coordination program, using each patient's past-year healthcare cost as the training label on the reasoning that costlier patients are sicker. Explain how the label can come apart from the goal. Distinguish the two ways a measure and a goal can diverge (a stand-in that never tracked the goal, and a measure that tracked it and later stopped), and describe the checks that address each.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the measure (cost) and the goal (health need) and explains why cost is only a partial stand-in, since spending depends on access, insurance, referral patterns and treatment intensity, so patients with the same illness can differ in cost.
2. Names Goodhart's law or proxy optimization: ranking or optimizing on the stand-in can exploit the parts of it that are unrelated to the goal.
3. Describes divergence from the start (a proxy with weak construct validity) and the pre-deployment check, comparing the label with direct measures of the goal, such as clinical indicators, and comparing groups at the same score.
4. Describes divergence that opens after deployment, from policy changes, population change or behavior that responds to the measure, and that it is caught only by repeated checks against fresh direct outcome data.
5. Gives the remedy of changing the label to a quantity closer to the goal, or combining quantities, and states what the replacement costs, such as more data, delay or noise, instead of only patching features.

**Source:** What you measure and what you care about

## ES-ch01.12

A credit-risk model has been accurate for two years, and the team argues that this record shows it will stay accurate. Explain the problem with that argument, then design a post-deployment monitoring plan that would detect when past performance stops predicting future performance. Specify what you would monitor, how you would decide that something is wrong, and what you would do about it.

**Points:** 5

**Rubric (1 point each):**

1. Explains the induction problem: past success supports future success only if the conditions that produced it persist, no number of past correct predictions guarantees the next, and a stable data distribution is an assumption.
2. Identifies kinds of shift, including covariate shift (inputs change), concept shift (the relationship between inputs and outcomes changes), population change, and feedback from the model's own decisions.
3. Monitors inputs against the training or validation data using a stated statistic and threshold, such as the population stability index, as an early warning, and explains that input monitoring does not show that accuracy has fallen.
4. Monitors outcomes against realized results, by segment and with thresholds and windows set in advance, and notes limits such as the delay before credit outcomes are known and the missing outcomes for applicants who were declined.
5. Defines actions: alerts to a named owner, human review, a fallback or retraining, a stopping rule, and re-validation after any known change.

**Source:** What I mean by skepticism

## ES-ch01.13

A model trained to detect a disease from chest X-rays reaches 94% accuracy on a held-out test set drawn from the same hospitals as its training data, but only 71% at a new hospital. Explain what might account for the gap, with reference to the difference between what the model's output reports and the clinical reality it is meant to reflect. Describe how you would test your explanations.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the output, a label produced by a statistical model from image pixels, from the thing it is meant to track, disease in the patient, and notes that high held-out accuracy shows only that the label can be predicted from inputs like the training data.
2. Identifies shortcut learning or spurious correlation: confounders such as scanner type, markers, patient positioning, text tags or hospital-specific prevalence that correlate with the label at the training hospitals but not elsewhere.
3. Notes that a random held-out split from the same sources shares those confounders and so cannot reveal reliance on them, which is why external validation at a new site or another out-of-distribution test is needed.
4. Proposes diagnostics that could contradict the shortcut explanation, such as stratifying results by hospital or scanner, masking or cropping the suspect regions, and training a model that sees only the confounding feature to see whether it predicts the label.
5. Names other candidate causes, such as differences in labelling, in the patient population or disease spectrum, and in image processing, and says each should be tested instead of accepting the first plausible account.

**Source:** The slice

## ES-ch01.14

A team adds an automated AI reviewer that scans pull requests for security flaws. In its first month the reviewer reports no security issues in any of 400 pull requests, and a manager concludes that the code base is secure. Explain what this negative finding does and does not establish, and describe how you would measure whether the reviewer can find the flaws it is supposed to find.

**Points:** 5

**Rubric (1 point each):**

1. States that "no findings" depends on two things, whether flaws exist and whether the reviewer would detect them, so a clean report is uninformative until the detection rate is known.
2. Illustrates with numbers or reasoning, for example that a reviewer catching 60% of flaws leaves a 40% chance of a clean report on a flawed pull request, that the probability of a flaw after a clean report depends on the prior flaw rate and the detection rate and is not zero, and that a reviewer unable to detect a class of flaw says nothing about that class.
3. Proposes measuring sensitivity by seeding known flaws, or replaying known past vulnerabilities, into held-out pull requests and counting how many are flagged by class of flaw, and also measuring the false alarm rate.
4. Addresses coverage: which languages, files, flaw categories and parts of the change the reviewer examines, with everything outside its scope listed as not checked.
5. Concludes that the manager's claim goes beyond the evidence and offers a defensible statement of the form "the reviewer flagged none; its measured detection rate on seeded flaws of these classes was X," with human or independent review of the highest-risk code.

**Source:** What I mean by skepticism

## ES-ch01.15

A team uses a language model to grade 200 chatbot answers as pass or fail, and it passes 180 of them (90%). To check the judge, people with domain knowledge relabel a random sample of 50 of the 200 answers. In that sample the judge and the people cross-tabulate as follows: judge pass and human pass, 37; judge pass and human fail, 8; judge fail and human fail, 4; judge fail and human pass, 1. Interpret these results. State what the 90% pass rate does and does not tell you, compute the relevant rates from the table, and recommend what to do next.

**Points:** 5

**Rubric (1 point each):**

1. States that 90% is the judge's pass rate, a statement by the checking instrument and not a measurement of correctness, which requires an independent reference such as the human labels.
2. Computes from the table: agreement is 41 of 50 (82%), the humans passed 38 of 50 (76%) against the judge's 90%, and of the 45 judge passes 8 (about 18%) were human fails.
3. Computes the judge's sensitivity to failures: of the 12 answers the humans failed, the judge flagged 4 (33%), so it is lenient and misses most bad answers, and its errors are not random.
4. Notes the uncertainty from a sample of 50, with a 95% interval for the human pass rate of roughly 63% to 86%, the need for the sample to be random for any extrapolation, and that human raters can also be checked for agreement with each other.
5. Recommends reporting the human-labelled estimate with its interval instead of the judge's number, enlarging the labelled sample, studying the kinds of errors the judge accepts, revising the judge and re-measuring its agreement with humans, and keeping a person responsible for decisions that depend on the score.

**Source:** The solve-verify asymmetry
