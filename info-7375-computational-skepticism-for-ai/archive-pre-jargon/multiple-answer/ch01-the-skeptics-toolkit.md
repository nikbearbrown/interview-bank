# Chapter 1: The skeptic's toolkit

## MA-ch01.1

A launch review for a deployed fraud-detection model hears five sentences from the team, each offered in support of the claim that the model "works in production," meaning that it meets its operating requirements for both scoring speed and fraud detection. A checkable falsifier states an observation, possible to make, that would count against the claim. Check each statement that is a checkable falsifier. Each statement is worth 1 point (5 points total).

- [ ] A. "Median scoring latency at the gateway stays under 150 ms across 30 days of production traffic; a 7-day median above 150 ms means the claim has failed."
- [ ] B. "Over 30 days, recall on confirmed fraud in a weekly random audit of 400 labelled transactions stays at or above 0.85; any week below 0.80 counts as failure."
- [ ] C. "The model performs well across the situations that matter, and the team has high confidence in it going forward based on its experience in the pilot deployment."
- [ ] D. "The model stays robust to the many unexpected shifts that production traffic, user behavior and upstream data are likely to bring in the months after launch."
- [ ] E. "If anything looks wrong in production, the team will look into it promptly and take whatever action seems appropriate, escalating to the vendor if the cause is not found within a few days."

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Speed is one of the stated operating requirements, and a latency measurement over a defined window with a stated failure threshold can be checked and can fail.
- B: It names a metric, a sample, a threshold and a window, so a specific audit result can contradict it.
- C: "Performs well" and "high confidence" are compatible with any outcome, so nothing could show them wrong.
- D: "Robust" and "unexpected" fix no metric, threshold or window, so no observation could count against the statement.
- E: A promise to investigate names no observation that would refute the model's claimed performance.

**Source:** What I mean by skepticism

## MA-ch01.2

A team says: "Adding a retrieval step makes our assistant hallucinate less." A reviewer asks them to restate the claim as an explicit prediction, with assumptions and a falsifier, to be tested on a set of 500 held-out questions. Check each statement that would be a sound part of the restatement. Each statement is worth 1 point (5 points total).

- [ ] A. Assumption: the assistant's fluent phrasing shows its answers are supported, so annotators can save time by not checking each answer against the documents.
- [ ] B. Falsifier, fixed before the run: if the unsupported-claim share with retrieval is not lower than without it on those 500 questions, judged by a significance test or margin stated in advance, the claim counts as refuted for this setup.
- [ ] C. Success criterion: the claim counts as supported if no user complains about invented facts during the first week after release, since complaints are the clearest sign of a problem.
- [ ] D. Prediction: on the same 500 held-out questions, the share of answers with a claim unsupported by the supplied documents, as judged by two annotators, will be lower with retrieval than without it.
- [ ] E. Assumption, stated so it can be inspected: the 500 questions resemble real user traffic, and the annotators' judgments of whether a claim is supported are accurate.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Whether answers are supported is exactly what the test measures, so assuming it from phrasing removes the test.
- B: An outcome that is declared in advance to count against the claim is what makes the test capable of failing.
- C: A quiet week is an unmeasured, weak signal that would occur whether or not hallucination fell.
- D: It specifies the quantity, the data, the raters and the direction of change, so it can come out wrong.
- E: Writing down representativeness and rater accuracy turns hidden premises into items someone can check.

**Source:** What I mean by skepticism

## MA-ch01.3

A vendor says its content filter "never lets through step-by-step instructions for making the listed hazardous compounds." As evidence it reports that 10,000 test prompts, written by its own staff to resemble ordinary user requests, produced no such instructions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 10,000 clean results establish that no prompt exists, written by anyone, that would get such instructions through the filter.
- [ ] B. A smaller set of prompts written by testers who are actively trying to evade the filter would likely be more informative about the claim than 10,000 ordinary-looking requests.
- [ ] C. The vendor's claim is a real, testable claim because it rules out a specific observable outcome.
- [ ] D. One failure among the 10,000 test prompts would not by itself refute a different claim, that the filter lets through fewer than 1 in 1,000 such attempts.
- [ ] E. A single prompt that gets such instructions through would refute the vendor's claim.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Any number of non-failures leaves open that some untried input fails, so confirming instances cannot prove a universal claim.
- B: Evidence is strongest when it comes from attempts designed to find the failure, since easy cases pass anyway.
- C: Because the claim forbids an observable outcome, a counterexample could in principle be found, whatever the present evidence.
- D: A rate claim is about frequency, so a single failure among many trials can be consistent with a rate under the stated bound.
- E: A universal claim of the form "never" is contradicted by one counterexample.

**Source:** What I mean by skepticism

## MA-ch01.4

An engineering manager wants her team to treat AI outputs with methodical skepticism rather than with a general attitude of suspicion. Check each practice that fits methodical skepticism, meaning a procedure that can be performed on a particular claim and whose use can be seen. Each statement is worth 1 point (5 points total).

- [ ] A. Accepting an output when it agrees with the reviewer's own recent judgments on similar cases, because that agreement shows the output is sound.
- [ ] B. Recording how a belief about the system was formed and what conditions it depends on, so that a change in those conditions can be noticed.
- [ ] C. Before reading an output, writing down what a wrong answer would look like, so that the output is judged against a criterion fixed beforehand.
- [ ] D. Declining to rely on any AI output on principle, whatever its track record, the stakes involved or the checks that have been run on it.
- [ ] E. Examining only the outputs that look strange or implausible, since fluent and polished outputs have already passed an informal quality filter.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Agreement with one's own earlier judgments is not independent of them and can repeat their mistakes.
- B: Knowing what a belief rests on is what lets its holder notice when those conditions have changed.
- C: A criterion set before the output arrives cannot be bent to fit whatever the output happens to say.
- D: Blanket rejection is a disposition, not a procedure; it ignores evidence and cannot tell good outputs from bad ones.
- E: Polish says little about correctness, and errors that look right are exactly what a strangeness filter would miss.

**Source:** What I mean by skepticism

## MA-ch01.5

A loan-scoring system outputs "default risk 0.82, decline" for an applicant. A reviewer asks what would have to be true for that score to be wrong about this applicant, intending to produce a list of conditions that can be inspected. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the applicants now arriving come from a different population than the sample used to validate the model, the validation result may not apply to this applicant.
- [ ] B. If very few applicants in the training data resemble this one, the score is an extrapolation and deserves less trust.
- [ ] C. The reviewer submitted the same application a second time and received the same score, so the score is probably right for this applicant.
- [ ] D. Writing the list of conditions settles which of them actually hold for this applicant, so no further inspection is needed once the list exists.
- [ ] E. If the income field was entered in thousands in one source system and in single units in another, the model may have seen a value 1,000 times too small.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Validation results carry over to new inputs only to the extent that those inputs resemble the validated sample.
- B: Predictions in thinly covered regions of the input space are unreliable, and whether this applicant lies in one can be checked.
- C: Reproducing a number shows the system is consistent, not that the number matches the applicant's actual risk.
- D: The list names suspects; each condition still needs its own inspection or test to learn whether it holds.
- E: A unit or data-entry error is a checkable input fault that would make the score describe the wrong applicant.

**Source:** What I mean by skepticism

## MA-ch01.6

Before running an experiment, a researcher writes in a dated file: "The new prompt will raise exact-match accuracy on the 1,000-item test set by at least 2 points. A gain below 0.5 points, or any drop, means the claim has failed." The run shows a gain of 1.2 points. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 1.2-point result lies between the stated success and failure thresholds, which shows the prediction left that case undefined.
- [ ] B. Editing the file after the run to say "at least 1 point" would preserve the evidential value of the original prediction.
- [ ] C. The 1.2-point gain satisfies the prediction, since it is above the failure threshold of 0.5 points and the direction of the effect is positive.
- [ ] D. Stating the thresholds before the run is what allows the result to count against the claim.
- [ ] E. Leaving the original entry unchanged and appending the observed result as a separate dated entry preserves what was expected beforehand.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Gains between 0.5 and 2 points were assigned no meaning, so the honest report is that the outcome was neither predicted nor ruled out.
- B: Revising a threshold after seeing the result turns a test into a description of what happened.
- C: The prediction was a gain of at least 2 points; clearing the failure threshold is not the same as meeting the prediction.
- D: A criterion fixed beforehand cannot be adjusted to fit the outcome, so the outcome is able to contradict it.
- E: An append-only record separates prediction from observation and lets others check the order of events.

**Source:** What I mean by skepticism

## MA-ch01.7

A team ships a prompt change and sees no overall gain. After looking at the results, an analyst compares 20 customer segments and reports that segment 14 improved with p = 0.03, concluding that "the change works for segment 14 because that segment uses shorter queries." Assume the 20 comparisons are independent and that, in truth, the change has no effect in any segment. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A stronger test is to state the segment 14 hypothesis and a threshold in advance and then check it on new data collected after the hypothesis was written.
- [ ] B. Because p = 0.03 is below 0.05, the segment 14 result is unlikely to be chance, regardless of how many segments were examined.
- [ ] C. A Bonferroni correction for 20 comparisons would still count p = 0.03 as significant at the 5% family-wise level, because 0.03 is below 0.05.
- [ ] D. The probability that at least one of the 20 segments shows p < 0.05 by chance alone is about 64%.
- [ ] E. The shorter-queries explanation was constructed after seeing the result, so it has not been tested against any outcome that could have contradicted it.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: A prediction made before fresh data arrive can fail, so its success is real evidence.
- B: A p-value computed for one comparison does not account for choosing the best of 20 after the fact.
- C: The corrected per-segment threshold is 0.05 / 20 = 0.0025, which 0.03 does not meet.
- D: The chance of at least one hit is 1 - 0.95^20, which is about 0.64.
- E: An account fitted to a result already seen would have been adjusted to whatever segment looked good, so agreement is guaranteed.

**Source:** What I mean by skepticism

## MA-ch01.8

An LLM assistant with no access to a company's systems is asked why a database query is slow. It replies with a well-organized, confident explanation that names a specific table and a specific configuration setting as the cause. The engineer has not looked at the database. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The clarity of the explanation is not evidence that its diagnosis matches this database.
- [ ] B. Naming a specific table and a specific setting is evidence that the assistant inspected the database, since a vague answer would not name them.
- [ ] C. Treating the explanation as a hypothesis and testing a prediction that could contradict it, such as whether rebuilding the index speeds up the query, is more informative than rereading it.
- [ ] D. A longer and more confident version of the same explanation would reduce the need to measure, because extra detail makes a wrong diagnosis less likely.
- [ ] E. Checking the query plan and the table's fragmentation statistics on the real system supplies evidence that the explanation's wording cannot.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Well-formed prose is produced by a process that does not depend on being right, so form and correctness are separate properties.
- B: With no access to the system the specifics cannot come from inspection; specificity is as easy to generate as vagueness.
- C: A hypothesis becomes evidence only when a test could have shown it wrong.
- D: More detail and more confidence change the presentation, not the evidence.
- E: A measurement on the real system is a direct observation of the thing the explanation makes a claim about.

**Source:** The fluency trap

## MA-ch01.9

An LLM is given only a table of weekly revenue and asked why revenue fell 8% last month. It writes a fluent, specific account blaming a competitor's price cut. The table would fit several other accounts equally well, such as a shift in billing dates or a holiday moved into the following month. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A coherent account that fits the data is a hypothesis, because other accounts fit the same data equally well.
- [ ] B. The mention of a particular competitor shows that the model had access to that competitor's pricing data.
- [ ] C. Obtaining the same price-cut explanation in ten of ten samples from the same model shows that the explanation is true.
- [ ] D. An account that no conceivable observation could contradict is better supported than one that makes risky predictions.
- [ ] E. Comparing the date of the competitor's price change with the date the decline began is a check that could contradict the account.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Fit to the data does not discriminate among accounts that all fit; only evidence favoring one over the others does.
- B: The model was given only revenue figures, so the competitor detail came from the model's generation habits, not from data it saw.
- C: Repetition from one source measures the stability of the model's output, not whether it matches the world.
- D: Support comes from surviving attempts at refutation, and an unrefutable account has not been tested.
- E: If the decline began before the price cut, the account fails, so the comparison is a test.

**Source:** The fluency trap

## MA-ch01.10

An LLM assistant attaches a stated confidence to each answer. An independent audit of 200 answers for which it stated confidence of at least 90% finds that 150 were correct. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 95% confidence interval for the accuracy of those 200 answers runs from roughly 69% to 81%, so a true accuracy of 90% is not plausible for this group.
- [ ] B. If the underlying model or the mix of questions changes, an earlier calibration audit may no longer describe the assistant.
- [ ] C. The observed accuracy of those answers is 75%, which is below the stated confidence.
- [ ] D. A phrase such as "I am 95% sure" from a language model is a calibrated probability by construction, because the model computes it from its own uncertainty.
- [ ] E. A calibration check compares stated confidence levels with how often the answers at those levels turn out to be correct across many answers.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The normal-approximation interval is 0.75 plus or minus about 0.06, roughly 0.69 to 0.81, which excludes 0.90.
- B: Calibration is a property of a system on a population of questions, so it can change when either one does.
- C: 150 / 200 = 0.75.
- D: Verbal confidence is generated text; whether it tracks the frequency of being right has to be measured, not assumed.
- E: Calibration means that among answers given at a stated level, about that fraction are correct, which can only be seen over many answers.

**Source:** The fluency trap

## MA-ch01.11

An analyst wants to confirm a model-written answer to "What was Company X's 2022 revenue?" and considers several second checks. Check each statement that is true about whether a second check adds independent evidence. Each statement is worth 1 point (5 points total).

- [ ] A. Looking the figure up in the company's audited annual filing is a check whose errors are unlikely to be tied to the model's errors.
- [ ] B. Two checks are independent to the extent that whatever could make one of them wrong would not also make the other wrong.
- [ ] C. Asking a different model that was trained on largely overlapping text is fully independent of the first, because the two systems come from different vendors.
- [ ] D. Asking the model "Are you sure?" and receiving "Yes" is a second check, since the confirmation was produced after the original answer.
- [ ] E. Asking the same model the question again in a fresh session and getting the same figure adds little, because repeated samples from one model can repeat the same error.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A primary document produced by a different process has its own error sources, mostly unrelated to the model's.
- B: Independence is about whether the errors of two checks are correlated, not about how many checks were run.
- C: Models trained on overlapping data and with similar methods can share the same gaps and the same mistakes.
- D: The model is reading its own answer, so its confirmation shares every assumption of the original.
- E: Resampling one system tests its consistency, and a consistent system can be consistently wrong.

**Source:** The solve-verify asymmetry

## MA-ch01.12

Two reviewers inspect the same batch for a certain defect. Each reviewer catches any given defect with probability 0.8. Consider one defect in the batch. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the two reviewers miss independently, the probability that at least one of them catches the defect is 0.84.
- [ ] B. With three reviewers whose misses are independent, the probability that all three miss the defect is 0.016.
- [ ] C. If the two reviewers miss defects independently of each other, the probability that both miss this defect is 0.04.
- [ ] D. If the two reviewers have identical blind spots, so that each misses exactly the defects the other misses, the probability that at least one of them catches the defect is 0.96.
- [ ] E. The probability that at least one of the two reviewers catches the defect can be found as 0.96 from the 0.8 detection rate alone, whatever the relationship between their misses.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The probability that at least one catches it is 1 - 0.04 = 0.96, not 0.84.
- B: 0.2 x 0.2 x 0.2 = 0.008, so 0.016 is wrong.
- C: For independent misses, 0.2 x 0.2 = 0.04.
- D: With identical blind spots the second reviewer adds nothing, so the probability stays at 0.8.
- E: The benefit of a second reviewer depends on how correlated the two reviewers' errors are, not just on each one's detection rate.

**Source:** The solve-verify asymmetry

## MA-ch01.13

A team generates answers to 500 customer-support questions with a language model M and then grades each answer pass or fail by prompting the same model M as a judge. They report a 94% pass rate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 94% figure is a measurement of how many of the answers are correct.
- [ ] B. A judge that shares the generator's blind spots can accept an answer for the same mistaken reason the generator produced it.
- [ ] C. Language-model judges have been reported to favor outputs that resemble their own, so a self-graded score may be inflated.
- [ ] D. Replacing M with a larger model as judge removes the shared-error problem.
- [ ] E. Having a second run of M grade the same 500 answers and finding that its grades match the first run's would show that the 94% pass rate is accurate.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: It is the rate at which the judge says pass; how well that tracks correctness has to be measured against independent labels.
- B: Errors that come from the same knowledge gaps or the same misreading are not caught by a checker with those gaps.
- C: Self-preference in model-based grading has been observed, which biases self-graded results upward.
- D: A larger model may be better, but it can still share training data, framing and failure modes with the generator.
- E: Agreement between two runs of the same system measures consistency, which a consistently wrong judge also shows.

**Source:** The solve-verify asymmetry

## MA-ch01.14

A reporter finds the statistic "62% of firms have adopted technology X" in five news articles, each citing a different outlet. Tracing the citations back, all five come from a single press release by a vendor that sells X; the release gives no sample size, sampling method or question wording. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The more outlets repeat the figure, the more likely it is to be accurate, since each outlet decided independently to publish it.
- [ ] B. A survey whose methods are published can be trusted without further checks on how it was designed or carried out.
- [ ] C. The five articles amount to one piece of evidence, not five, because they share a single origin.
- [ ] D. Independent confirmation would require a source that collected its own data by a separate process.
- [ ] E. The vendor's commercial interest in the result is enough, by itself, to show that the figure is false.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Repetition spreads a claim without testing it.
- B: Published methods make checking possible; they do not show the survey was well designed or carried out.
- C: Copies of one claim are not separate observations; their errors are perfectly correlated.
- D: A separate sample, collected and analyzed separately, is what can corroborate or contradict the original figure.
- E: A motive to inflate is a reason to look harder, but whether the figure is true depends on how it was produced.

**Source:** The solve-verify asymmetry

## MA-ch01.15

A data-migration job writes "Migrated 12,000 rows to the new table: SUCCESS" to its log and exits with status code 0. An engineer then runs a row count directly on the destination table and gets 11,400. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The exit status of 0 establishes that the destination table is complete, since the job would otherwise have reported an error.
- [ ] B. Even if the destination count had been 12,000, matching counts would not by themselves show that the row contents were copied correctly.
- [ ] C. The log line is a statement produced by the process under review, while the destination count is a direct observation of the resulting state.
- [ ] D. The destination holds 5% fewer rows than the log reports.
- [ ] E. Because the job exited with status 0, the discrepancy can be set aside without looking at the missing rows.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A zero exit status means the process did not signal an error; it does not describe the state of the data.
- B: Rows can be duplicated, truncated or altered while the total stays the same, so a count checks one property only.
- C: A report generated by the system being checked is a claim about the world, not an observation of it.
- D: 12,000 - 11,400 = 600, and 600 / 12,000 = 5%.
- E: A direct observation that contradicts the report calls for investigating the difference, not explaining it away.

**Source:** The slice

## MA-ch01.16

A nightly backup job has written "backup completed" to its log and exited with status 0 on each of the last 400 nights. The goal is that the data can be restored after a loss. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A restore test that passed once, when the system was set up, shows that every later backup is restorable.
- [ ] B. A steadily growing backup file size shows that the backups can be restored, since the files hold more data each night.
- [ ] C. Restoring a recent backup into a scratch environment and comparing it with the source is a direct check of the property that matters.
- [ ] D. Exit status 0 on 400 consecutive nights shows that the backups are restorable, since errors would have changed the status.
- [ ] E. The "backup completed" line is independent confirmation, since it was written after the backup files were created.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Configuration, data and software change over time, so a past test says nothing certain about later backups.
- B: Size can grow while the data are corrupted, incomplete or unreadable.
- C: A restore into a clean environment tests the outcome that matters rather than a report about the process.
- D: Exit status describes whether the job raised an error, not whether the files can be restored.
- E: The line is written by the same job whose correctness is in question, so it reports the job's own belief.

**Source:** The slice

## MA-ch01.17

A developer says her patch fixes a bug in which exporting a customer record crashes when the customer's name contains an apostrophe. She adds a test that exports a record for "Olivia Smith" and shows that it passes after the patch. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Her explanation of why the patch should work is evidence that it does work, since she wrote the code and understands it best.
- [ ] B. A test that uses a name with an apostrophe, fails on the old code and passes on the patched code would be evidence that the patch addresses this bug.
- [ ] C. A passing result on her own machine shows that the deployed build is fixed, since it runs the same source code.
- [ ] D. The test would also have passed before the patch, so it cannot tell a patched build from an unpatched one.
- [ ] E. Seeing no new crash reports for a day after release establishes that the fix is correct, because the bug would otherwise recur.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A reason to expect success is a prediction, not an observation of success.
- B: A test that fails before and passes after is the kind of observation that distinguishes a fix from no fix.
- C: Her machine and the deployed system can differ, so the check must be made against the thing that actually runs.
- D: A test that cannot fail on the broken version does not discriminate between broken and fixed.
- E: A day without reports is weak evidence, since rare inputs may not have occurred in that time.

**Source:** What I mean by skepticism

## MA-ch01.18

A safety evaluation runs a chatbot on 100 prompts drawn at random from expected production traffic and records 0 harmful responses. Treat the prompts as independent trials with a fixed probability of a harmful response. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Roughly 3,000 clean trials would be needed to bring the 95% upper bound on the harm rate down to about 0.1%.
- [ ] B. If the true harm rate were 2%, observing 0 harmful responses in 100 prompts would still happen about 13% of the time.
- [ ] C. The result describes prompts like those that were sampled and says little about prompts written specifically to provoke harm.
- [ ] D. The result shows that the true harm rate is below 1%, since no harmful response was observed in the sample.
- [ ] E. A one-sided 95% upper confidence bound on the harm rate is about 3%.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The rule of three gives an upper bound of 3 / 3,000 = 0.1%.
- B: 0.98^100 is about 0.13, so a clean run is quite possible at a 2% rate.
- C: A bound holds for the population that was sampled; adversarial inputs come from a different distribution.
- D: At a true rate of 1% the chance of 0 harms in 100 trials is about 37%, so the data do not rule it out.
- E: With zero events in n trials the 95% upper bound is about 3 / n (the "rule of three"), here 3 / 100.

**Source:** What I mean by skepticism

## MA-ch01.19

A static-analysis tool finds each instance of a certain class of vulnerability independently with probability 0.6 and raises no false alarms. Of modules like the one under review, 20% contain exactly one instance and 80% contain none. The tool reports nothing for this module. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Given the clean report, the probability that the module contains the vulnerability is about 9%.
- [ ] B. The clean report shows that the module is free of this vulnerability class, because the tool raises no false alarms.
- [ ] C. If the module contains one instance, the chance of a clean report is 0.4.
- [ ] D. If the tool were unable to detect this vulnerability class at all, a clean report would carry no information about it.
- [ ] E. A module with two separate instances, each found independently with probability 0.6, would produce a clean report with probability 0.16.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: By Bayes' rule, 0.2 x 0.4 / (0.2 x 0.4 + 0.8 x 1) = 0.08 / 0.88, about 0.091.
- B: A clean report lowers the probability of a flaw from 20% but does not reduce it to zero.
- C: The instance is missed with probability 1 - 0.6 = 0.4.
- D: A tool that cannot see a class of flaw returns the same clean report whether or not the flaw is present.
- E: Both instances must be missed, giving 0.4 x 0.4 = 0.16.

**Source:** What I mean by skepticism

## MA-ch01.20

A team's test suite passes on its code. To learn what a pass means, they inject 50 small deliberate faults into the code, one at a time, each confirmed to change the program's behavior on some input that can occur, and rerun the suite for each. The suite fails (detects the fault) for 31 of the 50. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Injecting known faults is a way to measure whether a checking method can detect faults at all.
- [ ] B. The pass on the unmodified code shows that the code contains no faults.
- [ ] C. The suite detected 62% of the injected faults.
- [ ] D. The 19 undetected faults point to behavior that the suite does not check.
- [ ] E. A detection rate of 62% on injected faults means that 62% of real defects would be caught.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Seeding faults of known type lets one count how many the checker catches, which a clean run cannot reveal.
- B: A suite passes whenever the faults present are ones it does not test for.
- C: 31 / 50 = 0.62.
- D: A fault that changes behavior without failing any test marks behavior the tests do not examine.
- E: Real defects may differ in kind from the injected ones, so the rate transfers only roughly.

**Source:** What I mean by skepticism

## MA-ch01.21

Consider the general relationship between the effort needed to produce an answer and the effort needed to check it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For some problems, such as factoring a large integer, checking a proposed answer by multiplication is much cheaper than finding the factors by any known classical method.
- [ ] B. Because a language model produces an output in milliseconds, checking that output must take longer than producing it.
- [ ] C. For a claim such as "this long summary faithfully reflects the source record," a short mechanical certificate that settles correctness generally exists.
- [ ] D. How costly it is to verify an AI output depends on whether a cheap check, such as a test, a lookup or an independent ground truth, is available for that kind of output.
- [ ] E. If a workflow budgets no effort for checking, unchecked outputs accumulate and, absent other signals, look like successes.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Verifying a factorization takes one multiplication, while no efficient classical method for finding factors is known.
- B: How fast something is produced does not determine how hard it is to check; some outputs are cheap to verify.
- C: Faithfulness to a long record usually needs a knowledgeable reader, not a quick mechanical test.
- D: The cost of checking is a property of the task and of what reference is available, so it varies from one output type to another.
- E: An output that nobody examined has no visible defects, so it passes by default.

**Source:** The solve-verify asymmetry

## MA-ch01.22

A model drafts 2,000 contract summaries a day at negligible cost. A lawyer needs 10 minutes to check one summary against its contract. Suppose 2% of summaries contain a material error, errors occur independently across summaries, and a lawyer who checks a summary always spots a material error in it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A random sample of 150 summaries has at least a 95% chance of containing at least one erroneous summary.
- [ ] B. Checking a random 5% sample would take about 33 lawyer-hours per day.
- [ ] C. Checking every summary would take about 333 lawyer-hours per day.
- [ ] D. A random sample of 100 summaries has at least a 95% chance of containing at least one erroneous summary.
- [ ] E. A random sample of 150 summaries in which no error is found proves, with certainty, that the error rate is below 2%.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: 1 - 0.98^150 is about 0.952, just above 95%.
- B: 5% of 2,000 is 100 summaries, which is 1,000 minutes, about 17 hours.
- C: 2,000 x 10 minutes = 20,000 minutes, which is about 333 hours.
- D: The chance of at least one error is 1 - 0.98^100, about 0.87, below 95%.
- E: A clean sample of 150 is evidence against a high rate but cannot rule out a 2% rate with certainty, since a 2% rate would give no errors in 150 about 5% of the time (0.98^150 is about 0.048).

**Source:** The solve-verify asymmetry

## MA-ch01.23

A support team rewards agents, and the AI assistant that drafts their replies, for average handle time. After six months, average handle time has fallen from 11 minutes to 7, while the share of customers who contact support again within a week about the same issue has risen from 14% to 26%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The pattern illustrates Goodhart's law: when a measure becomes a target, it tends to stop being a good measure.
- [ ] B. Because handle time and resolution moved together before the incentive was introduced, they must still move together now.
- [ ] C. The fall in handle time is itself good evidence that more customers are getting their problems solved, since each call is resolved faster.
- [ ] D. The repeat-contact rate is a more direct indicator of the outcome the team cares about than handle time is.
- [ ] E. Handle time was adopted as a stand-in for "customers get their problem solved," and once the stand-in is rewarded the relationship between the two can break.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Once the measure is rewarded, behavior changes in ways that separate it from what it was meant to indicate.
- B: A past correlation is not a guarantee, especially when the incentive itself changes behavior.
- C: Faster closure can come from ending conversations early, which would also raise repeat contacts, as the data show.
- D: A returning customer with the same issue is closer to an unresolved problem than a short call is to a solved one.
- E: Optimizing a proxy puts pressure on the parts of it that are unrelated to the underlying aim.

**Source:** What you measure and what you care about

## MA-ch01.24

Two teams report models that score well on their validation metrics but fail the goal the metric was meant to serve. Team 1 trained a model to predict each patient's past healthcare spending as a stand-in for medical need. Team 2 built a demand forecaster whose error was low for two years; a new competitor then changed customers' buying habits, and its error has been rising since. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Team 1's problem would disappear if the model were retrained more often on newer data with the same stand-in label, because the newer data reflect current patients.
- [ ] B. In Team 2, the metric tracked the goal when it was validated, so a one-time review at launch would have found nothing wrong with the measure.
- [ ] C. In Team 1, the metric and the goal were mismatched from the start, and comparing the stand-in with direct measures of need before deployment could have revealed it.
- [ ] D. Team 2's problem can be avoided by validating more thoroughly on the original historical data before launch, using more folds and more years.
- [ ] E. A strong validation result at launch is enough to show that the metric will still track the goal a year later, provided the model is unchanged.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: More recent data with the same flawed label reproduces the same gap between label and goal.
- B: A relationship that held at launch and later changed cannot be detected by examining launch-time data.
- C: A label that never tracked the goal is a design-time flaw that a direct comparison with the goal can expose.
- D: The failure arose from a change in the world after launch, which the original data cannot contain.
- E: A measure's link to the goal can erode as conditions or behavior change, so it has to be checked again.

**Source:** What you measure and what you care about

## MA-ch01.25

A delivery-time predictor was within its stated margin on 98% of 50,000 orders during a year of normal operation. The company then opens a new region with a different road network, and the model's inputs now come from that region. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. No number of past correct predictions logically guarantees that the next prediction will be right.
- [ ] B. Comparing the input distribution in the new region with the training data can flag a shift, but only comparing predictions with realized delivery times shows whether accuracy fell.
- [ ] C. The year of correct predictions is evidence about future accuracy to the extent that future cases resemble the past ones.
- [ ] D. The model's own output confidence will necessarily fall when it meets inputs from the new region, signaling that its predictions are less reliable.
- [ ] E. Accuracy is a property of a model together with the cases it is applied to, not of the model alone.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Induction from past cases is probabilistic support, never a guarantee.
- B: A changed input distribution is a warning sign; whether outputs have become wrong is settled by comparing predictions with outcomes.
- C: Inductive support depends on the future being like the sample from which the track record came.
- D: A model has no built-in mechanism to notice that its inputs have moved, and can stay confident on unfamiliar data.
- E: The same model can be highly accurate on one population and poor on another.

**Source:** What I mean by skepticism

## MA-ch01.26

A pneumonia classifier is trained and tested on a pooled set of chest X-rays from two hospitals. Hospital A contributed 1,000 images, of which 800 show pneumonia; hospital B contributed 1,000 images, of which 100 show pneumonia. Each image carries a scanner tag identifying its hospital, and the tag is visible to the model. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An accuracy of 85% on the pooled set shows that the model is reading features of the lungs and not just the scanner tag.
- [ ] B. Testing on a third hospital whose scanners and patients were absent from training is a stronger check for reliance on the tag than the pooled held-out set.
- [ ] C. Predicting "pneumonia" for every image from hospital A and "no pneumonia" for every image from hospital B would score 85% accuracy on this pooled set.
- [ ] D. Within hospital A alone, a rule that predicts pneumonia for every image would be correct on only 20% of images, since it ignores everything about the patients.
- [ ] E. Randomly splitting the pooled images into training and test sets removes the hospital confound from the evaluation.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A shortcut that uses the scanner tag, which correlates with disease prevalence, produces the same score without any reading of the lungs.
- B: A new site breaks the correlation between tag and disease that the model may have exploited.
- C: The rule is right on 800 of 1,000 from A and 900 of 1,000 from B, so 1,700 of 2,000, which is 85%.
- D: Within A the rule predicts pneumonia for all images, and 800 of 1,000 do show pneumonia, so it is right on 80%.
- E: Both halves of a random split share the same tag-to-prevalence relationship, so the confound remains in the test set.

**Source:** The slice

## MA-ch01.27

A company's release pipeline lets an AI reviewer approve routine configuration changes proposed by an AI agent. The approval record reads "Approved by ReviewBot." One of the approved changes causes an outage. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A person who approves several hundred AI-proposed changes a day, a few seconds each, is exercising meaningful review of each change.
- [ ] B. A record of who approved what, and when, supports later review of decisions even though it does not prevent errors.
- [ ] C. Responsibility for the decision shifts to the AI reviewer because it performed the review.
- [ ] D. An approval attributed only to a software component leaves no identifiable person who accepted the risk and can explain the decision.
- [ ] E. Naming a human approver adds oversight when that person can see what will change and has the practical ability to stop the change.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: At that volume and speed the approver cannot examine each change, so the approval is nominal.
- B: Audit trails make it possible to reconstruct what happened and to learn from it.
- C: A software component cannot be held answerable, so responsibility stays with the people who deployed and relied on it.
- D: Accountability needs someone who can answer for the decision and who had the authority to make it.
- E: An approver who cannot see the effect or cannot say no is not providing a check.

**Source:** The Five Supervisory Capacities

## MA-ch01.28

Reviewers must approve or reject each of 5,000 AI recommendations before it takes effect. They approve 4,850 (97%) and reject 150, spending a median of 4 seconds per item. An independent audit of all 5,000 recommendations finds that 400 (8%) were wrong. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Requiring a human click on every item guarantees that each recommendation received independent verification.
- [ ] B. Had the reviewers rejected 400 recommendations (8%), they would have caught every wrong one, since the rejection count would match the error count.
- [ ] C. At least 250 of the 400 wrong recommendations were approved.
- [ ] D. A high approval rate combined with very short review times is consistent with approvals that do not reflect examination, though the two facts do not prove it.
- [ ] E. The 97% approval rate shows that 97% of the recommendations were correct, since reviewers approve only what they have judged sound.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: A click records a decision; it does not show that anything was independently checked.
- B: Rejecting the right number of items says nothing about whether the rejected ones were the wrong ones.
- C: Only 150 items were rejected in total; even if all were correct catches, 400 - 150 = 250 wrong items passed.
- D: Over-reliance on automated suggestions is a documented tendency, and speed plus agreement is a pattern it produces, though other explanations exist.
- E: Reviewers approving an item is not evidence that it is correct, as the audit shows.

**Source:** The Five Supervisory Capacities

## MA-ch01.29

A test report reads: "Tested 40 of 40 sample invoices: all processed correctly. Not tested: handwritten scans, invoices in languages other than English, behavior under production load." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because every sampled invoice passed, the report may state that the failure rate on all invoice types is zero.
- [ ] B. The 40-of-40 result supports claims about invoices like those sampled and does not extend to the untested categories.
- [ ] C. Since the tool has not failed on handwritten scans, they can be recorded as passing.
- [ ] D. Listing what was not tested is part of an honest account, since it marks the limits of what the passing result supports.
- [ ] E. A record that allows "unknown" as a status, separate from "pass" and "fail", preserves information that a two-state record would lose.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Zero failures in a finite sample of one kind of input does not establish a zero rate, still less for other kinds.
- B: A sample supports conclusions about the population it was drawn from, not about different kinds of input.
- C: A tool cannot fail on inputs it was never run on, so no failure there is not evidence of success.
- D: Readers rely on a report to decide what to trust, and a stated scope lets them judge whether it applies to their case.
- E: "Not examined" and "examined and fine" call for different actions, and merging them hides which is which.

**Source:** Skepticism as a team practice

## MA-ch01.30

A vendor reports that its fine-tuned model reached 91% accuracy on a benchmark test set. Behind that number are eight training runs that differ only in random seed, with test accuracies of 91, 84, 85, 86, 85, 83, 87 and 84 percent. The vendor reported the best run, chosen by looking at test accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Choosing the best run by its test score means the number was selected using the test set, which biases it upward as an estimate for new data.
- [ ] B. The reported 91% is a fair estimate of the accuracy a new training run with a different seed would reach.
- [ ] C. The spread of accuracies across seeds is noise that a buyer can ignore, since the mean already summarizes the runs.
- [ ] D. The mean accuracy of the eight runs is about 85.6%.
- [ ] E. Reporting the best seed is honest as long as the 91% figure was actually observed on the benchmark test set.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Selecting the maximum of several noisy estimates on the same data overstates what to expect on fresh data.
- B: A typical new run would land near the mean of the runs, not at the maximum.
- C: The spread, about 2.5 points in standard deviation, shows how much results depend on chance and is part of what the evidence says.
- D: The eight values sum to 685, and 685 / 8 is about 85.6.
- E: A figure can be literally observed and still misrepresent expected performance when the selection is not disclosed.

**Source:** Skepticism as a team practice

## MA-ch01.31

A deployment team wants its skeptical checks to happen reliably rather than depend on whether an individual engineer remembers to be careful that day. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adding a checklist item such as "are live inputs represented in the data the model was validated on?" turns a general worry into something that can be inspected.
- [ ] B. Setting the failure condition and metric threshold in a monitoring alert before launch removes the need for someone to remember to ask the question later.
- [ ] C. Once checks are written into the process, no one needs to understand what they are for, since the process will apply them correctly.
- [ ] D. A check is more useful when a named person has the authority to hold a release if it fails.
- [ ] E. Even with checks in the process, someone still has to review whether the checks continue to test the right thing as the system and its use change.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A specific question with a yes or no answer can be assigned, answered and audited.
- B: A pre-set alert applies the criterion automatically, whether or not anyone is thinking about it.
- C: Checks applied without understanding go stale or are satisfied in form while missing their purpose.
- D: A check that cannot stop or delay anything records a problem without anyone being able to act on it.
- E: A check that was well aimed at launch can drift away from the real risk as conditions change.

**Source:** Skepticism as a team practice
