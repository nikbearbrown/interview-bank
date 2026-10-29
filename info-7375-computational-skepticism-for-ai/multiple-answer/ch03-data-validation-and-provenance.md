# Chapter 3: Data validation and the epistemic frame of a dataset

## MA-ch03.1

An analyst receives an export of every insurance claim paid to one hospital system between 2018 and 2023: about 6 million rows, with no blank diagnosis codes. She plans to use it to estimate how common a chronic condition is among adults who live in the surrounding city. Reconstructing the frame behind a dataset means establishing who collected it, for what purpose, who is in and out, and how each variable was measured. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the data are administrative rather than survey data, they involve no measurement choices, so field names can be taken at face value without any coding documentation.
- [ ] B. Residents who are uninsured, use other hospital systems or never seek care are outside the data, so the estimate may be biased for the city.
- [ ] C. With about 6 million rows, sampling error is negligible, so the prevalence estimate is reliable for the city's adults even though only one system's claims are included.
- [ ] D. The export exists to pay claims, so who appears and which fields exist follow billing rules, not a design for measuring the city's health.
- [ ] E. A diagnosis code records what was billed, which can differ from a clinical determination, so how it was measured must be established before it is treated as the condition.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Administrative fields are defined by coding rules and reimbursement incentives, and those choices must be documented to interpret them.
- B: A prevalence estimate is only as good as the match between the people recorded and the population the claim is about.
- C: Size shrinks random error but not the systematic gap between one system's insured patients and the city's adults.
- D: Administrative data inherit the purpose of the system that produced them, and that purpose decides who is recorded and what is captured.
- E: A code is a measurement produced by billing practice; it is a proxy for the condition, not the condition itself.

**Source:** Reconstructing the epistemic frame — a working procedure

## MA-ch03.2

A team inner-joins 100,000 support tickets to a customer table on customer_id to build a modeling table, and the result has 96,000 rows. Tickets from one region (Region N, 10,000 tickets) carry customer IDs with a legacy prefix in the customer table, so 3,200 of them find no match; in the other regions, 800 of 90,000 tickets find no match for unrelated reasons. A missing-value report on the joined table shows 0.0% missing in every column. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because only 4% of rows were lost, a model trained on the table can be expected to perform about equally well in every region.
- [ ] B. The zero-missing report shows that the join lost no rows, because dropped rows would appear as blank cells.
- [ ] C. Region N lost 32% of its tickets against about 0.9% elsewhere, so the overall 4% figure hides a concentrated loss.
- [ ] D. Comparing 100,000 input rows with 96,000 output rows exposes a 4.0% loss that the missing-value report cannot see.
- [ ] E. Region N accounts for about 10% of the dropped rows, matching its 10% share of the input tickets.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Region N falls from 10% of the data to about 7.1%, and its remaining rows may differ from its lost ones, so performance there can be worse.
- B: Dropped rows are absent, not blank, so a cell-level report has nothing to flag.
- C: 3,200 of 10,000 is 32%, while 800 of 90,000 is about 0.9%; an aggregate rate can mask a severe subgroup rate.
- D: Rows removed by an inner join leave no blank cell behind, so only a before-and-after row count reveals them.
- E: Region N accounts for 3,200 of the 4,000 dropped tickets, which is 80%, far above its 10% share of the input.

**Source:** Reconstructing the epistemic frame — a working procedure

## MA-ch03.3

An orders table has six rows, one per order, with customer_id values a, a, b, c, d, d. A customers table has four rows with customer_id values a, b, b, e; the key b appears twice because of a data-entry duplicate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A full outer join returns 7 rows, the same as the left join, because the customers table contributes no unmatched keys.
- [ ] B. Asserting that customer_id is unique in the customers table before joining would have flagged the problem.
- [ ] C. An inner join on customer_id returns 4 rows: two for order key a and two for order key b.
- [ ] D. A left join returns 7 rows, one more than the orders table, because the order for b matches two customer rows.
- [ ] E. A left join from orders to customers returns 6 rows, one per order, because the left table is preserved.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Customer key e matches no order, so a full outer join adds that row and returns 8.
- B: A uniqueness check on the key catches the duplicate b before it silently inflates the output.
- C: Order key a matches one customer row twice (2 rows) and order key b matches two customer rows (2 rows); c and d match nothing.
- D: Duplicate keys on the right side multiply the matching left rows, so a left join can return more rows than the left table has.
- E: The join returns 7 rows: the single order for b matches two customer rows, so it is repeated.

**Source:** Reconstructing the epistemic frame — a working procedure

## MA-ch03.4

A satisfaction survey appears as a pop-up inside a mobile app after a user completes a purchase, and it cannot be submitted unless every question is answered. The resulting file has 12,000 responses and no empty cells. The company wants to report the satisfaction of 'all customers', a group that also includes web-only customers and people who abandoned a purchase partway. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Customers who abandoned a purchase may differ in satisfaction from completers, so the average can be biased even with 12,000 responses.
- [ ] B. No empty cells means the recorded responses are complete; it says nothing about customers who never saw or never submitted the form.
- [ ] C. Because every question is mandatory, the respondents must be representative of all customers, since nobody can skip an answer and distort the results.
- [ ] D. A missing-value check on this file would flag the web-only customers as missing, since they appear nowhere in it.
- [ ] E. Collecting another 12,000 responses through the same pop-up would push the bias toward zero, since a larger sample is closer to the whole customer base.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: If inclusion is related to the outcome, a large sample reproduces the same systematic error precisely.
- B: Completeness of recorded rows is a different property from coverage of the population the rows are supposed to represent.
- C: Mandatory fields control what each respondent answers, not who is asked or who submits.
- D: People who were never recorded are not rows with blanks, so no cell-level check can detect them.
- E: More draws from the same selection process reduce random error but leave the systematic bias in place.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.5

A city has 100,000 adults: 30,000 under 30 and 70,000 aged 30 or older. Under-30s use a transit app 10 hours a month on average and the others 2 hours, so the city-wide mean is 4.4 hours. A researcher draws 1,000 people at random from a phone directory (the sampling frame) that lists 20% of the under-30s and 80% of the older adults, and everyone sampled responds. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Under-30s are about 9.7% of the directory but 30% of adults, so the expected sample mean is about 2.8 hours, below the true 4.4.
- [ ] B. Reweighting respondents so that under-30s count for 30% of the estimate would remove the bias whatever the unlisted people in each age group are like.
- [ ] C. The undercoverage matters only if the directory lists fewer than half of all adults, since otherwise the majority is represented.
- [ ] D. Enlarging the sample from 1,000 to 20,000 people drawn from the same directory would shrink the gap toward zero, since sampling error falls with sample size.
- [ ] E. Because the 1,000 people are drawn at random, the sample mean is an unbiased estimate of the city-wide mean, whatever the directory covers.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The frame holds 6,000 under-30s and 56,000 older adults, giving an expected mean of (6,000 x 10 + 56,000 x 2) / 62,000, about 2.77.
- B: Weighting corrects the age mix only if listed and unlisted people within each age group have the same average usage, which is an assumption.
- C: Coverage of 62% overall still biases the estimate because coverage differs across groups whose outcomes differ.
- D: A larger sample from the same frame converges to the frame's mean of about 2.8, not to 4.4.
- E: Random selection within a frame is unbiased only for the frame's population, which here differs from the city's.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.6

A database lists the annualized returns of investment funds that are still operating today. Ten years ago 1,000 funds were launched. Of these, 600 survive and averaged an 8% annual return over the decade; 400 have closed, and they averaged -2% over the years they existed. The database contains only the survivors. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In a hypothetical in which the same funds had instead closed at random, for reasons unrelated to their returns, the survivors would still be expected to average well above the average over all 1,000 funds.
- [ ] B. Reporting the median instead of the mean of the survivors would remove the bias.
- [ ] C. The average over all 1,000 funds was 4%, so the survivor-only average of 8% overstates it by 4 percentage points.
- [ ] D. A missing-value check on the survivor file would reveal the 400 closed funds as blank rows.
- [ ] E. The closures are related to the returns being studied, so the absent funds are not a random subset of all funds.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: If closure were independent of returns, the survivors would be a random subset of the funds and their expected average would match the all-fund average, so the gap arises only because closure is related to returns.
- B: The median of the survivors is still computed on a filtered group and still excludes the poor performers.
- C: (600 x 8 + 400 x -2) / 1,000 = 4, so excluding the closed funds raises the average.
- D: Closed funds are absent from the file, not present with blanks.
- E: Selection that depends on the outcome produces bias that the surviving rows alone cannot show.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.7

In a city of 100,000 people, disease A affects 10% and disease B affects 10%, independently of each other. A hospital admits every person who has A or B (or both) and 5% of people who have neither; assume it sees nobody else. An analyst uses the hospital's 23,050 admission records to study how A and B are related. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adjusting for age and sex in a regression on the admission records would restore the population relationship between A and B.
- [ ] B. The negative association in the admission records comes from how patients enter the dataset, not from a biological link between A and B.
- [ ] C. Analyzing ten years of admission records instead of one year would remove the artifact, since the extra records average out the distortion.
- [ ] D. In the full city population, patients with A are less likely to have B than patients without A, so the two diseases compete with each other.
- [ ] E. Among admitted patients, about 10% of those with A also have B, compared with about 69% of those without A.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The selection depends on A and B themselves, so adjusting for unrelated covariates does not undo conditioning on admission.
- B: Admission depends on having either disease, so among admitted patients, not having one disease makes the other more likely.
- C: More records collected through the same admission rule reproduce the same distortion.
- D: The diseases are independent in the population, so the chance of B is 10% whether or not a person has A.
- E: Admitted with A: 10,000, of whom 1,000 have B. Admitted without A: 9,000 with B plus 4,050 with neither, so 9,000 / 13,050 is about 69%.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.8

A lender approved 40,000 of 100,000 past applicants using a fixed rule on a legacy score. Repayment outcomes exist only for approved applicants, and 6% of them defaulted. The lender will train a new model on the 40,000 approved loans and use it to score all future applicants, including those the legacy rule would have rejected. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The missing outcomes for rejected applicants are missing completely at random, because a fixed rule rejected them.
- [ ] B. The training data have no outcomes in the score range the old rule rejected, so predictions there are extrapolation.
- [ ] C. The 6% default rate describes approved applicants, not all 100,000 applicants.
- [ ] D. Accuracy measured on the 40,000 approved loans is an unbiased estimate of accuracy on all applicants.
- [ ] E. Approving a small random share of applicants below the old cutoff would yield outcomes in that range, at a cost to the lender.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Missingness is determined by the legacy score, which is related to risk, so it is not independent of the data.
- B: A model cannot be checked against data it never saw; behavior outside the observed range is an assumption.
- C: Approval was based on a score related to risk, so the approved group is not a random sample of applicants.
- D: Evaluation on a selected subset reflects that subset only; the rejected region is untested.
- E: Randomized exploration is the standard way to obtain unbiased labels where a decision rule would otherwise hide them.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.9

A dataset has blank values in several columns. The standard missingness mechanisms are MCAR (missing completely at random), MAR (missing at random, given the observed data) and MNAR (missing not at random). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If younger respondents skip an income question more often and, within each age group, skipping is unrelated to income, the missingness is MNAR because it is related to age.
- [ ] B. Readings lost because a sensor's battery fails at random moments, unrelated to the quantity being measured, are an example of MCAR.
- [ ] C. Statistical tests on the observed data alone can confirm that missingness is MAR rather than MNAR, as long as the sample is large enough.
- [ ] D. Patients who skip a final visit because the condition measured there has become severe, leaving that measurement blank, are an example of MNAR.
- [ ] E. If high earners skip an income question because of how much they earn, the missingness is MAR, since income is related to the other columns.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Dependence on an observed variable such as age, with nothing further tied to the unobserved value, is MAR; MNAR requires dependence on the unobserved value itself.
- B: When the chance of a value being missing is independent of both observed and unobserved data, the mechanism is MCAR.
- C: MAR and MNAR differ in how missingness depends on unobserved values, and the observed data cannot reveal that dependence.
- D: The reason the value is missing is the value itself, which is the defining feature of MNAR.
- E: Missingness driven by the unobserved value itself is MNAR, whatever other columns correlate with income.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.10

A survey of 1,000 people asks for annual income. In the population, 600 people earn 40 (thousand) and 400 earn 100, so the true mean is 64. Each low earner skips the question with probability 0.10 and each high earner with probability 0.50. Averaged over many repetitions, 740 people answer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. About 26% of income values are expected to be missing.
- [ ] B. High earners are expected to make up about 27% of the answers, against 40% of the population.
- [ ] C. The expected mean of the answers is about 56.2, below the true 64.
- [ ] D. Filling each blank with the mean of the answers gives an expected overall mean near 64.
- [ ] E. If skipping depended only on an observed column such as job title and not on income itself, analyzing within job-title groups could remove much of the bias.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Expected skips are 60 + 200 = 260 of 1,000.
- B: 200 of 740 answers come from high earners, which is about 27%, so they are under-represented among respondents.
- C: Expected answers are 540 low earners and 200 high earners: (540 x 40 + 200 x 100) / 740 is about 56.2.
- D: Filling with the answers' own mean leaves the overall mean at about 56.2.
- E: Missingness that depends only on observed variables is MAR, and conditioning on those variables can correct it.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.11

A numeric column has 10 rows. Six are observed (30, 35, 40, 45, 50, 100) and four are missing. An analyst fills the four blanks with the observed mean and then computes statistics on all 10 rows. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A standard error computed on the filled column treats ten values as real observations and is therefore too small.
- [ ] B. The mean of the column stays at 50, because the filled values equal the mean of the observed ones.
- [ ] C. Mean imputation leaves the correlation between this column and other columns unchanged, since the mean is a neutral value.
- [ ] D. Filling the four blanks with the observed median (42.5) instead would also leave the mean at 50.
- [ ] E. The sample standard deviation falls from about 25.5 to about 19.0, even though no real data were added.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Only six values carry information; the filled values add no new information but increase the apparent sample size.
- B: Adding four copies of the mean leaves the sum divided by the count unchanged.
- C: Filled rows sit at the mean of this column regardless of the other columns, which pulls correlations toward zero.
- D: Filling with 42.5 gives a mean of 47.0, because the median differs from the mean in a skewed column.
- E: The sum of squared deviations stays 3,250 while the divisor grows from 5 to 9, so the variance drops from 650 to about 361.

**Source:** Missing data and imputation

## MA-ch03.12

An analyst must decide how to handle blanks in a numeric column. Assume she knows the mechanism that produced them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the blanks are MCAR, dropping every row with a blank leaves the estimated mean unbiased, though it uses fewer rows and widens the interval.
- [ ] B. For a categorical column, filling blanks with the column mean is a standard choice.
- [ ] C. Multiple imputation creates several completed datasets and pools the results, so the final uncertainty reflects the imputation.
- [ ] D. If the largest values are the ones that go missing because they are large, dropping those rows leaves the mean unbiased, since the remaining values are real measurements.
- [ ] E. If blanks depend on an observed column (MAR), imputing from that column, for example within groups, can reduce the bias that dropping rows would introduce.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Under MCAR the complete rows are a random subset of all rows, so deletion costs precision but not accuracy.
- B: A mean of categories is meaningless; the most frequent class or a model-based imputation is used instead.
- C: Variation across the completed datasets is combined with within-dataset variance to avoid overstating precision.
- D: The remaining rows are a truncated subset of the distribution, so their mean is systematically too low.
- E: Conditioning on the variable that drives missingness lets the imputation model reflect the missing rows' likely values.

**Source:** Missing data and imputation

## MA-ch03.13

A patient table stores age as an integer and uses -999 for 'unknown'. Eight rows have ages 34, 41, 29, -999, 52, 47, -999, 38. A type check confirms the column is entirely integer, and no range check was written. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A summary table showing a minimum of -999 for an age column would reveal the sentinel.
- [ ] B. Replacing -999 with 0 gives a mean that is a defensible estimate of the patients' average age.
- [ ] C. The mean computed over all eight values, sentinels included, is about -219.6.
- [ ] D. Excluding the two sentinel rows gives a mean of about 40.2 for the six recorded ages.
- [ ] E. The mean of 40.2 is guaranteed to equal the average age of all eight patients.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: An impossible minimum for an age column is a standard sign of a placeholder value.
- B: Zero is itself an invalid age here and pulls the mean down to about 30.1, which is not the average of any real ages.
- C: The sum is 241 - 1,998 = -1,757, and -1,757 / 8 is about -219.6.
- D: The six recorded ages sum to 241, and 241 / 6 is about 40.2.
- E: The two unknown ages could be anything, and whether they are like the recorded ones depends on why they are unknown.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.14

A pipeline validates a merged patient table against a schema: age is an integer from 0 to 120, weight is a number from 20 to 400, and admission_date and discharge_date are dates. Every row passes. Hospital X records weight in kilograms and hospital Y in pounds, and the table has no unit column. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because every value lies inside 20 to 400, the question of whether the weights are comparable is settled.
- [ ] B. A discharge date earlier than the admission date can pass a date-type check, yet a cross-field rule would flag it.
- [ ] C. Both hospitals' weights can satisfy the declared range while differing systematically by a factor of about 2.2.
- [ ] D. Adding an explicit unit column and validating its values against a list of allowed units would make the mismatch visible.
- [ ] E. Comparing the weight distribution by hospital would likely expose the unit mismatch.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A range check tests plausibility of individual values, not consistency of units across sources.
- B: Type validity concerns each value alone; relationships between fields need their own rules.
- C: One kilogram is about 2.2 pounds, and ordinary adult weights fit inside 20 to 400 in either unit.
- D: Recording and checking the unit turns an implicit assumption into a testable field.
- E: A group-wise check shows one source shifted by a constant factor even when the pooled distribution looks plausible.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.15

A table has 5,000 rows. In the age column, 400 values are missing (NaN), 50 are 0 or negative, and 4,550 are positive. An analyst writes df[df['age'] > 0], intending to remove only the 50 invalid ages. In pandas, comparing NaN with a number using >, <, <= or == gives False, and using != gives True. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 400 rows with missing age are removed silently, with no error or warning.
- [ ] B. The filter returns 4,550 rows, not the 4,950 the analyst intended to keep.
- [ ] C. Writing df[df['age'] != 0] instead would also remove the 400 rows with missing age, because NaN fails the comparison.
- [ ] D. Printing the row count before and after the step would have shown 5,000 becoming 4,550 and prompted the question of why 450 rows vanished, not 50.
- [ ] E. If the missing ages are concentrated in one customer segment, the filter removes that segment's rows disproportionately.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The comparison is valid Python and pandas code, so nothing signals that rows with missing values were dropped.
- B: NaN > 0 is False, so the 400 missing-age rows are removed along with the 50 invalid ones.
- C: NaN != 0 evaluates to True, so those rows would be kept (and the negative ages would also be kept).
- D: A count mismatch against the expected result is the cheapest check for a silent drop.
- E: Dropping on a column that is missing for one segment shifts the segment mix of the table.

**Source:** Reconstructing the epistemic frame — a working procedure

## MA-ch03.16

A table has one row per hospital visit: 6,000 rows from 2,000 patients, with a patient_id column and a visit_id column that is unique per visit. To 'remove duplicates', an analyst keeps the first visit for each patient_id, leaving 2,000 rows. Each visit row carries its own label, 'readmitted within 30 days'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Deduplicating on patient_id is correct because a patient is the same person at every visit, so later visits carry no information.
- [ ] B. Keeping only each patient's first visit is guaranteed to leave the readmission rate unchanged.
- [ ] C. Rows that repeat the same patient_id and visit_id are the true duplicates to remove.
- [ ] D. The step removes 4,000 rows that are distinct visits, not repeated copies of the same record.
- [ ] E. After the step every patient counts once, whereas before patients with more visits counted more, so the table describes a different population of rows.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Later visits carry new events and outcomes; sameness of the person does not make the visits redundant.
- B: First visits and later visits can have different readmission rates, so the rate generally changes.
- C: A duplicate is a repeated record of one event, which the combination of both identifiers captures.
- D: Rows with the same patient_id but different visit_id describe different events.
- E: Deduplicating on an entity key changes the unit of analysis and the weighting of frequent users.

**Source:** Reconstructing the epistemic frame — a working procedure

## MA-ch03.17

Two annotators independently label 200 items as 'toxic' or 'not toxic'. Both say toxic on 70 items, only the first says toxic on 20, only the second says toxic on 10, and both say not toxic on 100. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Observed agreement between the two annotators is 85%, since they agree on 170 of 200 items.
- [ ] B. The 30 disagreements prove the labeling guideline is flawed, since nothing else could explain them.
- [ ] C. Kappa is higher than observed agreement because it adds credit for agreement expected by chance.
- [ ] D. Cohen's kappa is about 0.69, noticeably lower than the raw agreement of 85%.
- [ ] E. Expected chance agreement is 50%, because with two labels any two annotators agree half the time.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: (70 + 100) / 200 = 0.85.
- B: Disagreement can also come from ambiguous items, annotator error or legitimate differences in judgment.
- C: Kappa subtracts chance agreement, so it is lower than raw agreement here (0.69 versus 0.85).
- D: (0.85 - 0.51) / (1 - 0.51) is about 0.694.
- E: Chance agreement depends on each annotator's rate of using each label; here 45% and 40% toxic give 0.45 x 0.40 + 0.55 x 0.60 = 51%.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.18

A binary classifier has true accuracy 92% on a population. The test labels come from an annotator who flips the correct label on a random 10% of items, independently of what the classifier does. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Suppose the annotator's flips, contrary to the independence stated above, fell mostly on items the model gets wrong; measured accuracy could then exceed the true accuracy.
- [ ] B. Measured accuracy is higher than true accuracy because the noisy labels add extra correct matches.
- [ ] C. A second model with true accuracy 93% would show an expected measured advantage of about 0.8 points over the first, not 1 point.
- [ ] D. The same true difference between two models is harder to detect with noisy labels than with clean labels.
- [ ] E. The expected accuracy measured against the noisy labels is 83.6%.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Correlated errors make the model agree with wrong labels; if all 8% of the model's errors were flipped and the other 2% of flips hit correct items, measured accuracy would be 0.92 - 0.02 + 0.08 = 98%.
- B: With accuracy above 50% and independent symmetric noise, measured accuracy is lower than the true value.
- C: Measured accuracy is 84.4% versus 83.6%; independent symmetric noise scales true differences by 1 - 2 x 0.10 = 0.8.
- D: The measured gap shrinks while sampling variability does not, so the signal-to-noise ratio falls.
- E: 0.92 x 0.90 + 0.08 x 0.10 = 0.836: correct predictions are marked wrong when the label is flipped, and wrong ones are marked right.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.19

A model predicts whether a subscriber will cancel within the next 30 days. Features include tenure, plan type, recent logins and cancellation_survey_sent, a flag set by an automated email that goes out at the moment a subscriber cancels. The model scores 0.99 AUC on a random hold-out. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A feature that is strongly associated with the label and has no missing values is safe to keep, since it clearly carries predictive information.
- [ ] B. cancellation_survey_sent is produced by the outcome being predicted, so it is not available when the prediction is needed.
- [ ] C. Removing the flag and re-evaluating is a reasonable check; a large drop would be consistent with the earlier score coming from leakage.
- [ ] D. The 0.99 AUC on a random hold-out shows the model will perform about as well on live subscribers.
- [ ] E. A random hold-out split would have detected the leak, because leaked rows would be kept apart from the training rows.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Strong association and completeness say nothing about whether the feature exists at prediction time.
- B: A feature set after the event cannot be known at prediction time; using it is target leakage.
- C: An ablation isolates how much of the performance depended on the suspect feature; a large drop is consistent with leakage, though a legitimately strong predictor would also cause one, so the timing of the flag is what establishes the leak.
- D: The hold-out contains the same leaked flag, so the score measures the leak rather than predictive skill.
- E: A random split puts the leaked flag in both partitions, so it cannot reveal a leak.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.20

A chest-X-ray model is trained on 20,000 images from 5,000 patients, four images per patient. The images are split at random by image: 16,000 for training and 4,000 for testing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Splitting by patient, so that all four images of a patient fall on the same side, prevents this overlap.
- [ ] B. About 99% of test images are expected to have at least one training image from the same patient.
- [ ] C. If the 4,000 test images were also used repeatedly to choose hyperparameters, the final test score would remain an unbiased estimate.
- [ ] D. The resulting test accuracy likely overstates performance on patients the model has never seen.
- [ ] E. Because test images are never used to update the model's weights, the test set cannot be contaminated.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A group-level split keeps each entity entirely in training or entirely in testing.
- B: The chance that all three other images of a patient land in the test set is about 0.2^3 = 0.8%, so 99.2% have a training sibling.
- C: Repeated selection on the test set fits the choices to it, so the final score is optimistic.
- D: Images of the same patient share anatomy and acquisition traits that a model can recognize, which is not generalization to new patients.
- E: Contamination also arises when near-identical or same-entity data sit in training, whatever happens to the weights.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.21

A text dataset has 10,000 rows. Exactly 800 distinct records each appear twice as byte-identical rows, and the other 8,400 rows appear once. A random 80/20 split by row puts 8,000 rows in training and 2,000 in testing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Removing exact duplicates before splitting prevents this particular overlap between training and test rows.
- [ ] B. Exact-match deduplication also removes texts that differ only by trailing whitespace or capitalization.
- [ ] C. Train-test duplicates inflate scores only for neural networks; a nearest-neighbor classifier is unaffected.
- [ ] D. About 256 duplicate pairs are expected to straddle the split, so roughly 13% of test rows have an exact copy in the training set.
- [ ] E. The dataset contains 9,200 distinct records, since 800 of them are each counted twice in the 10,000 rows.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: With one copy of each record, no record can appear on both sides.
- B: Byte-exact comparison treats such texts as different, so near-duplicates need normalization or similarity matching.
- C: A nearest-neighbor model finds the identical training row and copies its label, so it benefits from leakage at least as much.
- D: Each pair straddles with probability about 2 x 0.8 x 0.2 = 0.32, giving 800 x 0.32 = 256 pairs and 256 / 2,000 = 12.8% of test rows.
- E: 8,400 records appear once and 800 appear twice, so 8,400 + 800 = 9,200.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.22

A screening dataset has 10,000 cases, of which 200 (2%) are positive. A classifier has recall 80% and a false-positive rate of 5%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the classifier's accuracy exceeds 90%, accuracy is an adequate summary of its usefulness here.
- [ ] B. A test set rebuilt to be 50% positive gives the best estimate of the precision the classifier will have at 2% prevalence.
- [ ] C. The classifier's precision is about 80%, equal to its recall.
- [ ] D. A rule that predicts 'negative' for every case has accuracy 98%, higher than this classifier's.
- [ ] E. The classifier's accuracy is 94.7%, with 9,470 of the 10,000 cases classified correctly.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Accuracy is dominated by the majority class; recall, precision and the baseline are needed.
- B: Precision depends on prevalence; on a 50% positive set it would be about 94%, far above the deployment value.
- C: It flags 160 true positives plus 490 false positives, so precision is 160 / 650, about 25%.
- D: 9,800 of 10,000 cases are negative, so the trivial rule beats 94.7% while detecting nothing.
- E: True positives 160 and true negatives 9,310 give 9,470 correct out of 10,000.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.23

A health system builds a model to choose patients for a care-management program, using next-year healthcare spending as the training label. Two groups, A and B, each have 10,000 patients, and 1,000 in each group have the highest illness burden. Group B faces access barriers, so at a given illness burden its patients generate less spending. The program enrolls the 2,000 patients with the highest predicted spending: 1,400 from A and 600 from B. Among the 1,000 highest-illness patients in each group, 870 in A and 520 in B are enrolled. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. 87% of Group A's highest-illness patients are enrolled, against 52% of Group B's.
- [ ] B. A larger share of enrolled B patients (about 87%) than of enrolled A patients (about 62%) are among the highest-illness, consistent with B needing to be sicker to reach the same predicted spending.
- [ ] C. The model can predict spending accurately and still enroll fewer of Group B's sickest patients, because spending only proxies illness burden.
- [ ] D. Removing the group indicator from the features guarantees equal enrollment of equally ill patients from both groups.
- [ ] E. A high R-squared for predicting spending shows that spending is a valid measure of illness burden for both groups.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: 870 / 1,000 = 87% and 520 / 1,000 = 52%.
- B: 520 / 600 = 86.7% and 870 / 1,400 = 62.1%; a group whose spending understates need must be sicker to clear the same threshold.
- C: Accuracy on the label does not establish that the label tracks the construct, especially when the gap differs by group.
- D: The bias sits in the label, which is also correlated with other features, so dropping the indicator does not remove it.
- E: Predictive fit to the label says nothing about whether the label measures the intended construct equally for each group.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.24

A model is trained on data from 2019 to 2021 and run in 2024. A numeric feature is split into four bins. The share of training rows in the bins is 25%, 35%, 25% and 15%; the share of 2024 rows is 15%, 30%, 30% and 25%. The population stability index, PSI = sum over bins of (live share - train share) x ln(live share / train share), is about 0.119. Common rules of thumb call PSI below 0.1 stable and 0.1 to 0.25 a moderate shift. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. PSI is zero only when the binned live shares equal the binned training shares.
- [ ] B. Because 0.119 is below 0.25, the model's accuracy in 2024 is guaranteed to match its accuracy on 2019-2021 data.
- [ ] C. The 2024 feature distribution differs from the training distribution, and this can be detected without any outcome labels.
- [ ] D. The 0.1 and 0.25 cut-offs are derived statistical thresholds above which a model's accuracy is certain to fall.
- [ ] E. If every feature's distribution were unchanged, the model's accuracy could not have changed.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Each term (live - train) x ln(live / train) is nonnegative and equals zero only when the two shares are equal.
- B: PSI summarizes one feature's shift; accuracy also depends on other features and on whether the input-output relationship changed.
- C: Covariate shift is a statement about inputs, so comparing feature distributions needs no labels.
- D: They are conventions used to prioritize investigation, not guarantees about performance.
- E: The relationship between inputs and the outcome can change (concept drift) even when the inputs look the same.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.25

A claims dataset covers 60 months and should hold about 10,000 records per month. A count-by-month plot shows about 5,000 records in each of three consecutive months and about 10,000 in every other month. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Counts by source system or site over the same months would help separate a collection outage from a real change in activity.
- [ ] B. Duplicating records from adjacent months to fill the gap restores the missing information, because neighboring months have similar patients.
- [ ] C. The total shortfall is 2.5% of the expected 600,000 records, so it can be ignored whatever its cause.
- [ ] D. A drop in counts is a finding only if it coincides with a known external event; an unexplained drop is just noise in the series.
- [ ] E. The plot shows that something changed but not why; an outage, a policy change and a real drop in activity would all produce it.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: An outage affects specific feeds, while a real change in behavior shows across sources.
- B: Copies of other months' rows add no information about the missing months and distort the distribution.
- C: A small total can hide a large loss in a subgroup or period, and the dip may reflect a changed population.
- D: An unexplained drop is itself a finding that needs an explanation, whether or not an event is known.
- E: A count series reports a finding without identifying its cause.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.26

Datasheet proposals for datasets ask questions grouped under motivation, composition, collection process, preprocessing, uses, distribution and maintenance. A team is deciding how much to rely on a datasheet written by a dataset's creators. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Preprocessing questions record transformations such as filtering, joining or relabeling that the final numbers no longer show.
- [ ] B. A completed datasheet verifies that the dataset is free of sampling and labeling bias, because each answer is checked against the data.
- [ ] C. Maintenance information, such as who updates the data and which version is current, affects whether a result can be reproduced later.
- [ ] D. A datasheet from the creators replaces the user's own exploratory checks, because the creators know the data best and wrote down its limits.
- [ ] E. Answers about collection process and intended purpose help a user judge whether the dataset suits a different purpose.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Documented processing steps let users see what was done to the data before they received it.
- B: A datasheet documents claims and choices; it does not test the data for bias.
- C: A result tied to an unversioned, changing dataset cannot be re-derived.
- D: Documentation can be incomplete or out of date, so users still check the data against what it says.
- E: Fitness for use depends on how and why the data were gathered, and those facts are rarely visible in the table itself.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.27

A training table has a column risk_score with no blanks and a smooth, plausible histogram. A colleague says it was produced by an earlier team's scoring model, which was trained on data that included part of the period now being used for evaluation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the upstream model saw outcomes from the evaluation period, its score as a feature can leak information about the evaluation labels.
- [ ] B. Documenting which model version, inputs and training window produced the column is part of recording its provenance.
- [ ] C. If the upstream team retrains its model, the column's meaning and distribution can change even though the raw inputs did not.
- [ ] D. The column is a prediction by another model, not a raw measurement, so it carries that model's assumptions and errors.
- [ ] E. The absence of blanks and a plausible histogram establish that the column measures what its name says, so no further documentation is needed.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Information about the outcomes flows through the score into the new model's inputs.
- B: Lineage lets a later user judge availability at prediction time and reproduce the column.
- C: A feature defined by a model changes when the model changes.
- D: Derived features inherit the choices and mistakes of whatever produced them.
- E: Completeness and a plausible shape are properties of the values and say nothing about what produced them.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.28

A sample of 20 values is: 50, 52, 48, 51, 49, 50, 53, 47, 50, 51, 49, 50, 52, 48, 50, 51, 49, 50, 100, 105. Its mean is 55.25, its sample standard deviation is about 16.2, and its quartiles are Q1 = 49 and Q3 = 51.25. The IQR rule flags values below Q1 - 1.5 x IQR or above Q3 + 1.5 x IQR. The z-score rule flags values with |z| above 3. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The z-score rule flags 105 but not 100, because the two extreme values inflate the mean and standard deviation used to compute z.
- [ ] B. In any sample of 10 values, no value can have |z| above 3 when z uses the sample standard deviation, so the rule can never flag anything there.
- [ ] C. The IQR rule can decide whether a flagged value is a data-entry error, because it does not depend on the mean.
- [ ] D. The IQR rule flags both 100 and 105.
- [ ] E. A flagged value should be deleted because outliers always represent errors.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: z is about 3.06 for 105 and 2.75 for 100; extremes contaminate the very statistics the rule relies on, which masks the smaller one.
- B: The largest possible |z| is (n - 1) / sqrt(n), which is about 2.85 for n = 10.
- C: Robustness helps detect candidates, but whether a value is an error is a question about how it was recorded.
- D: The fences are about 45.6 and 54.6, and only 100 and 105 fall outside them.
- E: A flagged value may be a legitimate extreme; the decision to remove, cap or keep it needs domain knowledge.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.29

Four datasets of 11 (x, y) points each have the same mean of x (9), the same mean of y (about 7.5), the same variances, the same Pearson correlation (about 0.82) and the same least-squares line y = 3 + 0.5x. In the fourth dataset, ten of the eleven x values equal 8 and one equals 19. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In the fourth dataset the point at x = 19 alone determines the fitted slope; without it, x has no variation and the correlation is undefined.
- [ ] B. For x = -5, -4, ..., 5 and y = x^2, the Pearson correlation is exactly 0 even though y is a deterministic function of x.
- [ ] C. Identical summary statistics do not imply similar scatter plots; plotting can reveal curvature or influential points that statistics hide.
- [ ] D. A correlation of about 0.82 in all four datasets indicates that each relationship is roughly a straight line with random scatter around it.
- [ ] E. A correlation heatmap of Pearson coefficients is enough to detect nonlinear dependence between columns, since strong dependence always produces a large coefficient.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The other ten points share x = 8, so only the lone high-x point separates the slope from zero variation.
- B: The relationship is symmetric and nonlinear, so the linear association cancels out.
- C: Summary numbers discard shape, which is why four very different point clouds can share them.
- D: Pearson correlation summarizes linear association but is produced equally by curved patterns and by one extreme point.
- E: A heatmap of Pearson coefficients can show near-zero for strongly dependent but nonlinear pairs.

**Source:** The procedural EDA pass — what it sees, and what it structurally cannot

## MA-ch03.30

A table has 10,000 rows. Group B has 500 rows, 200 of which have a blank income; group A has 9,500 rows, 95 of which have a blank income. A quality gate flags any column whose overall missing rate exceeds 5%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. About 68% of all blank incomes are in group B, which makes up only 5% of the rows.
- [ ] B. Group B's missing rate for income is 40%, against 1% for group A.
- [ ] C. Dropping all rows with a blank income is safe, because it removes under 3% of the rows.
- [ ] D. Missingness concentrated in one group is consistent with the values being missing completely at random.
- [ ] E. The overall missing rate for income is 2.95%, so the 5% gate does not flag the column.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: 200 of 295 blanks is about 67.8%, concentrated in a group with 500 of 10,000 rows.
- B: 200 / 500 = 40% and 95 / 9,500 = 1%.
- C: It would remove 40% of group B, changing the group mix and possibly biasing any result about B.
- D: If the chance of a blank depends on group, which is observed, the mechanism is not MCAR.
- E: (200 + 95) / 10,000 = 2.95%, below the 5% threshold.

**Source:** Statistical checks: test the data before you trust it

## MA-ch03.31

A support-ticket table has columns ticket_id, category and body. An analytics tool is granted access to all three columns and to nothing else. The body column is free text in which customers sometimes paste phone numbers, partial card numbers and links to documents held in other systems. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the tool can follow links in body, its effective data scope can extend to documents that the access policy never mentioned.
- [ ] B. The tool can reveal exactly what the schema lists, so a review of the three columns' types and permissions covers the exposure.
- [ ] C. The same concern applies equally to a table of numeric temperature readings that contains no text or references.
- [ ] D. Column-level permissions do not limit what sensitive information appears inside the text of a column that is permitted.
- [ ] E. Scanning free text for patterns such as phone numbers, and listing the references it contains, is a check that type-and-permission validation does not provide.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: References inside data turn a bounded table into an entry point to other data.
- B: Free text can carry identifiers and pointers that the schema does not describe.
- C: A self-contained numeric table has little content that points beyond itself; the concern is greatest for reference-rich data.
- D: Permissions apply to columns as units, not to the content within them.
- E: Content-level inspection finds what structural validation cannot see.

**Source:** The access assumption — and where the boundary really lives

## MA-ch03.32

Before modeling on a dataset it did not create, a team plans an audit. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The audit is finished once the automated checks on types, ranges, missingness and duplicates all pass, because those cover the main data-quality dimensions.
- [ ] B. A report that says 'no issues found' is as informative as one that lists the checks run, the checks not run and their limits, since both reach the same conclusion.
- [ ] C. Following a few randomly chosen records back to their source systems is unnecessary when documentation exists, since the documentation already describes them.
- [ ] D. Writing down the expected row count, time span and population before opening the data keeps a mismatch from being explained away afterward.
- [ ] E. When the source systems cannot be reached, the audit should assume the supplied documentation is accurate and complete, because nothing better is available.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Those checks read the data as recorded and cannot detect missing populations, invalid proxies or wrong expectations.
- B: Without the scope of the checks, a reader cannot tell what 'no issues' covers.
- C: Tracing a record can reveal transformations, drops and recodings that documentation omits or has not kept up with.
- D: A prior expectation gives the observed numbers something to be compared against, preventing hindsight rationalization.
- E: Unverifiable documentation is a risk to record, not a reason to trust it; the opacity itself is a finding.

**Source:** Reconstructing the epistemic frame — a working procedure
