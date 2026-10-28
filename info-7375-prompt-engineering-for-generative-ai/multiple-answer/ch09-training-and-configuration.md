# Chapter 9: Training and configuration

## MA-ch09.1

A team uploads policy documents to an assistant product's project store and rewrites the project's system prompt. The assistant now answers policy questions better. The product supplies the documents and the prompt to the model at request time and runs no fine-tuning job. A teammate reports: "we trained the model on our policies." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reverting the change does not require re-running a training job.
- [ ] B. "Trained" is an accurate word for this change because the improved behavior persists across sessions.
- [ ] C. Copying the prompt text and the documents into another project that uses the same model can reproduce the improvement there.
- [ ] D. The model's parameters are unchanged by these two actions.
- [ ] E. Deleting the documents from the store would remove the document-based part of the improvement without touching the model's parameters.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A prompt or document change is undone by restoring the earlier text or corpus.
- B: Persistence comes from saved text being re-supplied; training is identified by parameter updates from an objective.
- C: Prompt text and documents are portable inputs, so the same model given the same inputs can behave similarly.
- D: Both actions only change the input supplied at inference time; no optimizer ran.
- E: Retrieved content lives in the corpus and its selection step, so removing it removes its effect while the weights stay the same.

**Source:** Name the mutable object before you change it

## MA-ch09.2

Five kinds of change can alter an LLM-based system's behavior: model weights, prompt text, supplied context, tools and permissions, and run-time sampling settings. A team proposes the edits below. Check each statement that classifies the edit correctly. Each statement is worth 1 point (5 points total).

- [ ] A. Enabling a tool server that lets the agent query a ticketing system changes which actions and information sources the system can use, with the model unchanged.
- [ ] B. Appending three sample question-and-answer pairs to the instruction text changes the model's parameters.
- [ ] C. Adding a document to a retrieval index changes what the model can see at inference time, not what the model is.
- [ ] D. Adding a rule that denies shell commands modifies the model's learned behavior.
- [ ] E. Lowering the sampling temperature from 1.0 to 0.2 is a run-time setting change; no parameter is modified.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A tool server changes capability and information access, which is a different object from the weights.
- B: In-context examples are part of the input; they demonstrate a pattern for the current request and update nothing.
- C: Retrieval changes the context supplied to a fixed model.
- D: A permission rule changes which operations the runtime allows; it is a governance control, not a change to what the model learned.
- E: Temperature changes how outputs are drawn from the model's scores at run time and leaves the stored parameters alone.

**Source:** Name the mutable object before you change it

## MA-ch09.3

A deployment configuration file contains these entries: a system prompt reading "Answer only from the provided documents", a sampling temperature of 0.2, a list of allowed tools (search_docs, read_file), and a retrieval setting that supplies the top 5 passages per query. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Editing the system prompt line changes the model's weights.
- [ ] B. Adding write_file to the list of allowed tools changes the tools and permissions the system exposes.
- [ ] C. Raising the retrieval setting from 5 passages to 8 changes how much context the model is given.
- [ ] D. Changing the temperature changes how outputs are drawn at run time, not the stored parameters.
- [ ] E. Because all four entries live in one file, every edit to the file modifies the same kind of object.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Prompt text is input to the model and is re-read on each request; it does not alter parameters.
- B: The allowed-tools list controls which actions the host exposes and permits.
- C: The number of retrieved passages determines which text enters the input.
- D: Temperature rescales the scores before sampling; the weights are not touched.
- E: A single file can hold several kinds of setting, so the object changed must be traced by what each line controls, not by the filename.

**Source:** Name the mutable object before you change it

## MA-ch09.4

An agent host enables a new tool server with read and write access to a project folder, and a developer adds a permission rule requiring human approval before any write. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Enabling the tool server expands what the system can do without changing the model.
- [ ] B. Appropriate evidence for the change is the configuration diff plus a record of who authorized it.
- [ ] C. Both changes modify the model's weights.
- [ ] D. The approval rule governs which proposed operations the runtime will carry out.
- [ ] E. Describing the approval rule as "the model learned to be careful" attributes a human governance decision to the machine.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Tooling adds capability and information sources while the model stays exactly as it was.
- B: For tool and permission changes, the diff and the authorization decision are what show what changed and why.
- C: Neither tool configuration nor a permission rule touches parameters.
- D: A permission rule sits in the runtime and decides which operations are allowed.
- E: Calling a governance change "learning" disguises a decision someone made as a property of the system.

**Source:** Name the mutable object before you change it

## MA-ch09.5

Softmax with temperature T converts logits into sampling probabilities by taking p_i proportional to exp(logit_i / T). For logits [2, 1, 0], the probabilities are about (0.665, 0.245, 0.090) at T = 1 and about (0.867, 0.117, 0.016) at T = 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Changing T alters the model's stored parameters.
- [ ] B. As T approaches 0, sampling approaches always choosing the highest-logit option.
- [ ] C. Raising T above 1 makes the distribution flatter.
- [ ] D. Lowering T from 1 to 0.5 concentrates probability on the highest-logit option.
- [ ] E. Because outputs are sampled, one run at each of two temperature settings is enough to compare how the settings behave.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Temperature is applied after the model computes its scores; no parameter changes.
- B: In the limit of T near 0 the softmax becomes greedy selection of the largest logit.
- C: A larger T shrinks the gaps between logits and spreads probability more evenly.
- D: Dividing logits by a smaller T widens the gaps, so the top option's probability rises from 0.665 to 0.867.
- E: With sampling, a single draw per condition reveals little; repeated runs are needed to see a distribution.

**Source:** Name the mutable object before you change it

## MA-ch09.6

An assistant product "remembers" that a user prefers metric units. Engineers confirm the mechanism: a note is saved in a database and prepended to the prompt of later conversations. No fine-tuning occurs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Saying the model "learned the user" in the technical sense of training is unsupported without evidence of parameter updates.
- [ ] B. The preference persisting across sessions shows that the model's weights were updated for this user.
- [ ] C. Deleting the stored note would remove the behavior without any retraining.
- [ ] D. The behavior is a result of supplying stored context, not of a parameter update.
- [ ] E. The retrieval or selection step might fail to surface the note, so the preference could be applied unreliably.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A careful report describes the memory or context behavior observed rather than claiming learning in the training sense.
- B: Several non-training mechanisms persist across sessions; persistence is not proof of training.
- C: Because the behavior comes from the stored text, removing the text removes it.
- D: The note is added to the input each time, which is context supply.
- E: Any retrieval-based memory depends on a selection step that can miss relevant records.

**Source:** Persistence is not proof of training

## MA-ch09.7

A team must adapt an LLM-based assistant to a company's policies and compares three approaches: editing the prompt, adding retrieval over a policy corpus, and fine-tuning the model. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Once passages are retrieved, the model will use them faithfully.
- [ ] B. A prompt edit can be undone by restoring the earlier text.
- [ ] C. Fine-tuning produces new parameter values that must be stored, versioned, and served.
- [ ] D. Fine-tuning on a policy document does not guarantee the model will quote it verbatim.
- [ ] E. An edit to a document in the retrieval corpus can affect the next query without any training run.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A model can ignore, misread, or contradict supplied passages, which is why faithfulness is evaluated separately.
- B: Prompt text is a diffable file that can be reverted immediately.
- C: Training yields an artifact of changed parameters that the deployment must manage.
- D: Fine-tuning shifts behavior statistically and gives no guarantee of exact recall.
- E: Corpus changes are visible as soon as the new passages are retrieved into the input.

**Source:** Name the mutable object before you change it

## MA-ch09.8

A team ranks ways to change an assistant's behavior by how easily each change can be inspected and reversed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reverting a permission rule requires retraining, because the rule changes how the model behaves.
- [ ] B. A fine-tuned model cannot be edited line by line; reverting generally means redeploying an earlier checkpoint or retraining.
- [ ] C. A change to a retrieval corpus is reversible if the earlier corpus version is kept.
- [ ] D. Prompt text can be diffed and reverted in seconds.
- [ ] E. Since weights are the hardest object to revert, a team should prefer prompt or retrieval changes over training even when training would solve the problem better.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Permission rules are runtime configuration and can be restored from version control; no retraining is involved.
- B: Parameters are refit or restored from a saved artifact, not hand-edited.
- C: Keeping versions of the corpus makes the selection and content changes recoverable.
- D: Text under version control supports an immediate revert and a precise comparison.
- E: Training can be the right tool when behavior must be internalized; reversibility is one cost among several, not a veto.

**Source:** Name the mutable object before you change it

## MA-ch09.9

An assistant keeps replying in a house style across many sessions. An investigation finds three things in the deployment: a saved system prompt attached to the project, a memory store of user notes that is prepended to each request, and a permissions file. No fine-tuning job was ever run. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A permission rule that persists in configuration is a form of learning by the model.
- [ ] B. If behavior is stable over time, the cause must lie in the weights.
- [ ] C. The saved system prompt influences later requests by being included again as input.
- [ ] D. Training is identified by how long its effects last.
- [ ] E. Persistence across sessions is not evidence of training, because saved text is re-supplied as input on each request.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A permission rule is a runtime setting that persists, not a change in the model's parameters.
- B: Stability is equally explained by stable inputs; it does not point to weights.
- C: Saved prompt text works by being part of every request's input.
- D: Several non-training changes last; training is identified by its mechanism, a parameter update from an objective.
- E: Several non-training changes last: saved prompts, retrieved documents, memory records, permission rules.

**Source:** Persistence is not proof of training

## MA-ch09.10

A team suspects one saved instruction line is what makes an assistant refuse off-topic questions. They run the same 30 off-topic questions twice at temperature 0.8, once with the line present and once with it deleted, holding the model, the rest of the prompt, and the settings fixed. The assistant refuses 29 of 30 with the line and 6 of 30 without it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Running each condition only once would give much weaker evidence, because sampling varies from run to run.
- [ ] B. The experiment identifies which other component produces the 6 remaining refusals.
- [ ] C. Deleting the line and rerunning is an intervention on the system, which supports a causal reading better than noting that the line and the refusals co-occur.
- [ ] D. The result supports the claim that the line was holding the behavior in this setup.
- [ ] E. The drop from 29 to 6 shows the model's weights contain no refusal behavior.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: With sampling, repeated runs per condition are needed to separate an effect from run-to-run variation.
- B: Residual refusals could come from the model's own tendencies, other prompt text, or chance; the design does not isolate them.
- C: Changing one object while holding the rest fixed tests what the object does rather than what correlates with it.
- D: The behavior largely goes away when the line is removed, so the text was holding it.
- E: The weights may well contribute to refusals; the result only shows the line makes a large difference.

**Source:** Persistence is not proof of training

## MA-ch09.11

To test whether an assistant is sensitive to the choice of a few-shot example, a team runs each of two prompts 20 times at temperature 0.8 on the same question. Prompt 1 (original example) is correct in 11 runs; Prompt 2 (a different example) is correct in 17. A Fisher exact test comparing 11 of 20 with 17 of 20 gives p of about 0.08. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The data are suggestive that the example matters but are not conclusive at the conventional 0.05 level.
- [ ] B. Running each prompt only once would have been equally informative.
- [ ] C. If real, the difference supports a claim about context sensitivity for this task and setup, not about changed weights.
- [ ] D. If the difference is real, it shows the model was retrained by the new example.
- [ ] E. Doubling to 40 repetitions per condition would push p below 0.05.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A p-value near 0.08 leaves a real chance that sampling noise alone produced the gap.
- B: A single run per condition cannot separate an effect from sampling variation.
- C: The evidence concerns how outputs respond to input text under the recorded conditions.
- D: Examples in a prompt change the input; they cannot retrain the model.
- E: More runs narrow the uncertainty, but the outcome depends on what the extra runs show.

**Source:** Persistence is not proof of training

## MA-ch09.12

A hosted assistant gives a different answer on Tuesday than on Monday to the same user question. The only records are the two responses and the model's display name, which is unchanged. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Because the display name is unchanged, the model weights must be identical.
- [ ] B. The difference could come from changed prompt text, different retrieved passages, different tool output, a silent model update, or sampling variation.
- [ ] C. The report can state exactly what the Monday system state was, because the Monday answer exists.
- [ ] D. When internal details are not observable, a careful report says which details remain unknown instead of asserting a mechanism.
- [ ] E. Logging the full input, the settings, the tool results, and the model identifier for each call would allow a cautious attribution of such a change.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: A label can persist across silent updates; it is not evidence about the underlying parameters.
- B: An output difference alone does not identify which of several inputs or conditions produced it.
- C: A past output does not reveal the unrecorded inputs and conditions that produced it, so the earlier state cannot be reconstructed.
- D: Honest attribution distinguishes what was observed from what is unknown.
- E: A before-and-after record of each possible cause is what makes attribution defensible.

**Source:** What a production record can and cannot show

## MA-ch09.13

Three people each claim their result is reproducible. Person 1 supplies a short training script, the dataset, the hyperparameters, and a fixed seed, with deterministic code. Person 2 supplies a recorded prompt and sampling settings to replay against a hosted model. Person 3 supplies a configuration diff showing a permission change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Only byte-identical output counts as a successful repeat for all three kinds of reproducibility.
- [ ] B. Person 3's diff lets a reader inspect exactly what changed but does not by itself reproduce a behavior.
- [ ] C. Setting temperature to 0 makes a hosted model's output byte-identical across weeks.
- [ ] D. Person 2's replay may legitimately differ later if the hosted model is updated or sampling is stochastic.
- [ ] E. A reader can rerun Person 1's computation and expect the same parameter values, given the same code, data, numeric libraries, and hardware.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The three kinds of repeat have different dependencies, and identical output is not the only acceptable standard.
- B: A diff documents the change; observing behavior requires running the system.
- C: Providers can update models and infrastructure, and floating-point effects can still vary results even at temperature 0.
- D: A hosted service can change underneath a recorded prompt, and sampling adds variation.
- E: Deterministic computation on fixed inputs can be rerun and compared value by value.

**Source:** What a production record can and cannot show

## MA-ch09.14

A one-feature logistic classifier has weight w = 0.5 and bias b = -1. Its probability for label 1 is the sigmoid of the linear score, sigma(a) = 1 / (1 + e^(-a)), with a = w*x + b, and it predicts label 1 when the probability is at least 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For x = 4 the linear score is 1.0.
- [ ] B. At x = 0 the probability is below 0.5.
- [ ] C. At x = 2 the probability is exactly 0.5.
- [ ] D. For x = 4 the predicted probability is about 0.73.
- [ ] E. The decision boundary is at x = 4.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: a = 0.5*4 - 1 = 1.0.
- B: At x = 0 the score is -1 and sigma(-1) is about 0.27.
- C: a = 0.5*2 - 1 = 0 and sigma(0) = 0.5.
- D: sigma(1.0) is about 0.731.
- E: The boundary is where w*x + b = 0, so x = 2, not 4.

**Source:** The model: two numbers and a squashing function

## MA-ch09.15

A one-feature logistic classifier is initialized with weight 0 and bias 0, then evaluated on 100 labeled examples, 70 with label 1 and 30 with label 0, whose feature values range between -5 and 5. It predicts label 1 when the probability is at least 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The initial average loss would be lower than 0.693 because 70% of the labels are 1.
- [ ] B. Every example receives predicted probability 0.5.
- [ ] C. The average binary cross-entropy is ln 2, about 0.693.
- [ ] D. Accuracy at this point is 70%.
- [ ] E. At this point the prediction does not depend on the feature value.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The loss is the same for both labels at p = 0.5, so label balance does not change it.
- B: With w = 0 and b = 0 every score is 0, and sigma(0) = 0.5.
- C: Each example's loss is -ln(0.5) for either label, so the average is 0.693.
- D: The at-least-0.5 rule predicts 1 for every example, which is right for the 70 positives.
- E: The score w*x + b is 0 whatever x is.

**Source:** The model: two numbers and a squashing function

## MA-ch09.16

In IEEE double precision, math.exp(709) is about 8.2e307, while math.exp(710) raises an overflow error. A programmer writes sigmoid(x) = 1 / (1 + math.exp(-x)) and calls sigmoid(-1000). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Using 1/(1+e^(-x)) for x >= 0 and e^x/(1+e^x) for x < 0 computes the same function while avoiding the huge exponential.
- [ ] B. For moderate inputs such as x = 2 the two-branch version gives materially different probabilities from the naive formula.
- [ ] C. A passing test that sigmoid(-1000) is approximately 0 proves correctness for every input type and floating-point edge case.
- [ ] D. The call fails because exp(1000) overflows.
- [ ] E. The true value of sigmoid(-1000) is exactly 0.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Multiplying numerator and denominator by e^x rewrites the same quantity using only a small exponent for negative x.
- B: The branches are algebraically identical, so they differ only by rounding for ordinary inputs.
- C: One test covers one behavior; it says nothing about NaN, infinities, or other types.
- D: With x = -1000 the naive code evaluates exp(1000), which exceeds the largest double.
- E: The sigmoid is strictly positive; double precision merely rounds its value to 0.0.

**Source:** The model: two numbers and a squashing function

## MA-ch09.17

A one-feature logistic model has weight w = -1.5 and bias b = 3. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The location of the boundary does not depend on the bias.
- [ ] B. At x = 0 the predicted probability for label 1 is above 0.9.
- [ ] C. At x = 3 the model predicts label 0.
- [ ] D. The probability of label 1 increases as x increases.
- [ ] E. The decision boundary, where the probability is 0.5, is at x = 2.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The boundary is x = -b/w, so changing b moves it.
- B: At x = 0 the score is 3 and sigma(3) is about 0.953.
- C: At x = 3 the score is -1.5 and sigma(-1.5) is about 0.18, below 0.5.
- D: The weight is negative, so the score and probability fall as x rises.
- E: The boundary solves -1.5x + 3 = 0, which gives x = 2.

**Source:** The model: two numbers and a squashing function

## MA-ch09.18

A fitted logistic regression has a weight of 0.7 on a feature x. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Each one-unit increase in x adds 0.7 to the log-odds of label 1.
- [ ] B. Each one-unit increase in x multiplies the odds of label 1 by 0.7.
- [ ] C. The change in probability per unit of x is the same at every value of x.
- [ ] D. The weight shows that x causes label 1.
- [ ] E. Each one-unit increase in x raises the probability of label 1 by 0.7.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The model is linear in log-odds, so the weight is the log-odds change per unit.
- B: The log-odds rise by 0.7, so the odds are multiplied by e^0.7, about 2.01, not by 0.7.
- C: Through the sigmoid, the same step in x moves probability most near 0.5 and least near 0 or 1.
- D: A fitted weight describes an association in the training data and does not identify a cause.
- E: Probabilities are bounded by 1 and change nonlinearly; the weight does not add to the probability.

**Source:** The model: two numbers and a squashing function

## MA-ch09.19

A logistic model has weight w = 2 and bias b = -3. Its score is a = w*x + b, its probability is sigma(a), and its decision is label 1 when the probability is at least a chosen threshold. For a probability threshold of 0.8, the score threshold is ln 4, about 1.386. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With threshold 0.5 the decision boundary is at x = 1.5.
- [ ] B. Because the sigmoid is increasing, thresholding the probability is the same as thresholding the score.
- [ ] C. At x = 1.5 the predicted probability is 0.75.
- [ ] D. Raising the probability threshold to 0.8 with the same parameters moves the boundary to about x = 2.19.
- [ ] E. Training updates the threshold along with the weight and bias.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The score is zero when 2x - 3 = 0, so x = 1.5.
- B: A monotonic function preserves order, so each probability threshold corresponds to one score threshold.
- C: At x = 1.5 the score is 0, so the probability is 0.5.
- D: The score must reach 1.386, so x = (1.386 + 3)/2, about 2.19.
- E: The threshold is a decision rule chosen outside the fitting loop.

**Source:** Score, probability, and decision are three layers

## MA-ch09.20

A one-feature classifier predicts whether a job will run long from its input size x; long jobs mostly have x above 5 and short jobs mostly have x below 5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The boundary is where w*x + b = 0 because the sigmoid of 0 is 0.5.
- [ ] B. If the data are mirror-image symmetric around zero, the learned bias can stay near zero, which shows a bias term is unnecessary.
- [ ] C. On mirror-image symmetric data, removing one point or flipping one label can move the learned bias away from zero.
- [ ] D. With w = 0.8 and b = -4 the boundary is at x = 3.2.
- [ ] E. With the bias fixed at 0, the decision boundary is forced to x = 0, so a boundary near 5 cannot be represented.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Probability 0.5 corresponds to a score of 0.
- B: Symmetric data can hide the need for a bias; it is needed whenever the relationship is not centered at zero.
- C: A small asymmetry changes the error balance that keeps the bias near zero.
- D: The boundary is x = -b/w = 4/0.8 = 5, not 3.2.
- E: Without a bias, w*x = 0 only at x = 0.

**Source:** Score, probability, and decision are three layers

## MA-ch09.21

A binary logistic model gives score a = 2 for an example. The usual loss is -y*ln(p) - (1-y)*ln(1-p) with p = sigma(a), where sigma(2) is about 0.8808. An algebraically equivalent score-based form is max(a, 0) - y*a + ln(1 + e^(-|a|)). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For label 0 the loss is about 2.127.
- [ ] B. The two forms give different values, which is why the score-based one is preferred.
- [ ] C. At this score, a label-0 example has a smaller loss than a label-1 example.
- [ ] D. The score-based form avoids taking the log of a probability that has rounded to exactly 0 or 1 when |a| is large.
- [ ] E. For label 1 the loss is about 0.127.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: -ln(1 - 0.8808) is about 2.127.
- B: The forms are algebraically equivalent; the second is chosen for numerical safety.
- C: A positive score favors label 1, so a label-0 example is penalized more (2.127 versus 0.127).
- D: It never forms p or 1-p, so large scores do not push a log argument to zero.
- E: -ln(0.8808) is about 0.127.

**Source:** Loss makes the objective explicit

## MA-ch09.22

A float64 implementation computes p = 1/(1 + exp(-a)) for score a = 40 and label y = 0, then evaluates -ln(1 - p). In double precision, e^(-40) is about 4.2e-18, which is below the spacing of numbers near 1, so 1 + e^(-40) rounds to 1.0 and p is exactly 1.0. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The naive computation ends up evaluating ln(0).
- [ ] B. The score-based form max(a,0) - y*a + ln(1 + e^(-|a|)) returns about 40 here.
- [ ] C. The true loss for this example is about 40.
- [ ] D. Clipping p to the range [1e-15, 1-1e-15] before taking logs would return about 34, a capped value that is no longer the true loss.
- [ ] E. A loss of about 40 means the model assigned a probability near 0.5 to the correct label.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: With p exactly 1.0, 1 - p is 0 and its logarithm is undefined or negative infinity.
- B: With a = 40 and y = 0 the formula gives 40 + ln(1 + e^-40), about 40.
- C: The loss is ln(1 + e^40), which is about 40.
- D: The clipped 1 - p is on the order of 1e-15, and -ln of that is roughly 34, so clipping changes the value.
- E: A loss near 40 means the correct label was given a probability of roughly e^-40, far below 0.5.

**Source:** Loss makes the objective explicit

## MA-ch09.23

A model outputs probabilities for label 1 on three examples: 0.9 (true label 1), 0.2 (true label 0), and 0.5 (true label 1). Use natural logs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The average loss equals the misclassification rate at threshold 0.5.
- [ ] B. The p = 0.5 example has the largest of the three losses, about 0.693.
- [ ] C. The p = 0.2, label-0 example has a loss of about 1.61.
- [ ] D. The average loss over the three examples is about 0.34.
- [ ] E. The p = 0.9 example has a binary cross-entropy loss of about 0.105.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Loss is a continuous measure of confidence in the right label, not a count of errors.
- B: -ln(0.5) is 0.693, larger than 0.105 and 0.223.
- C: For label 0 the loss is -ln(1 - 0.2) = -ln(0.8), about 0.223; 1.61 is -ln(0.2), which would apply to a true label of 1.
- D: (0.105 + 0.223 + 0.693) / 3 is about 0.341.
- E: -ln(0.9) is about 0.105.

**Source:** Loss makes the objective explicit

## MA-ch09.24

Two models predict the probability of label 1 for the same example whose true label is 1. Model P outputs 0.01 and Model Q outputs 0.4. Use natural logs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Cross-entropy for a label-1 example is bounded above by 1.
- [ ] B. Model P's cross-entropy loss, about 4.6, is more than five times Model Q's, about 0.92.
- [ ] C. A prediction of 0.99 for this example would have a loss of about 0.01.
- [ ] D. At threshold 0.5 both models are wrong, so accuracy treats the two predictions as equally bad.
- [ ] E. As the probability assigned to the true class approaches 0, the loss grows without bound.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The loss -ln(p) is unbounded as p approaches 0.
- B: -ln(0.01) is 4.61 and -ln(0.4) is 0.92, a ratio of about 5.0.
- C: -ln(0.99) is about 0.01, since a confident correct answer costs almost nothing.
- D: Both probabilities fall below 0.5, so both count as one error.
- E: Cross-entropy punishes confident wrong answers without limit.

**Source:** Loss makes the objective explicit

## MA-ch09.25

Binary cross-entropy for label y and predicted probability p is -y*ln(p) - (1-y)*ln(1-p). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For a label-1 example it reduces to -ln(1-p).
- [ ] B. Minimizing the average of this loss over a dataset maximizes the Bernoulli likelihood of the observed labels.
- [ ] C. For p = sigma(a), its derivative with respect to the score a is p - y.
- [ ] D. Mean squared error between p and y has the same derivative with respect to the score.
- [ ] E. It equals the zero-one error.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: With y = 1 the second term vanishes, leaving -ln(p).
- B: Cross-entropy is the negative log-likelihood of independent Bernoulli labels.
- C: The sigmoid and the log-loss combine so that the score derivative is the prediction error.
- D: The squared-error derivative carries an extra factor p(1-p), which shrinks when predictions saturate.
- E: Cross-entropy is continuous and graded, while zero-one error counts mistakes.

**Source:** Loss makes the objective explicit

## MA-ch09.26

One training example has feature x = 3 and label y = 0. The model has w = 0.2 and b = 0.1, with p = sigma(w*x + b). Recall that the derivative of the binary logistic loss with respect to the score a = w*x + b is p - y. Here a = 0.7 and p is about 0.668. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The derivative of the loss with respect to b is about 0.67.
- [ ] B. A gradient descent step with a positive learning rate will increase w.
- [ ] C. The derivatives with respect to w and b are equal because both parameters multiply the same error.
- [ ] D. The loss for this example is about 0.40.
- [ ] E. The derivative of the loss with respect to w is about 2.00.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The score changes by 1 per unit of b, so dL/db = p - y, about 0.67.
- B: The gradient is positive, and descent subtracts it, so w decreases.
- C: The weight's derivative carries the extra factor x = 3, so the two differ.
- D: For label 0 the loss is -ln(1 - 0.668), about 1.10.
- E: By the chain rule dL/dw = (p - y)*x = 0.668*3, about 2.00.

**Source:** Derive the first update

## MA-ch09.27

Training data as (x, y) pairs: (0, 0), (1, 0), (2, 1). A model starts at w = 0 and b = 0 with p = sigma(w*x + b), uses the average binary logistic loss, and takes one full-batch gradient descent step with learning rate 0.6. The per-example derivative with respect to the score is p - y. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The bias does not move on this step because the errors sum to zero.
- [ ] B. The averaged weight gradient is about -0.167.
- [ ] C. The three initial errors p - y are 0.5, 0.5, and -0.5.
- [ ] D. The average loss after the step is higher than the initial 0.693.
- [ ] E. After the step, w is 0.1 and b is -0.1.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The errors sum to +0.5, so the bias gradient is +0.167 and b moves.
- B: The sum of error times x is 0 + 0.5 - 1.0 = -0.5, and dividing by 3 gives -0.167.
- C: Every prediction is 0.5, so the errors are 0.5 - y for each label.
- D: The loss falls to about 0.661 after a correctly signed step.
- E: w = 0 - 0.6*(-0.167) = 0.1 and b = 0 - 0.6*(0.167) = -0.1.

**Source:** Derive the first update

## MA-ch09.28

Training data as (x, y) pairs: (-1, 1), (1, 0), (2, 0), so larger x goes with label 0. A model starts at w = 0, b = 0, uses the average binary logistic loss and the error p - y, and takes one full-batch gradient descent step with a positive learning rate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The averaged weight gradient is about +0.67, so w decreases on the first step.
- [ ] B. After the first step, b is positive.
- [ ] C. The averaged bias gradient is 0, so b stays at 0.
- [ ] D. The first step makes w positive because the model must raise probabilities for positive x.
- [ ] E. The initial average loss is below ln 2 because the label-0 points have larger x.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Errors are -0.5, 0.5, 0.5; weighted by x they sum to 2.0, and the mean is 0.667.
- B: The bias gradient is positive and descent subtracts it, so b becomes negative.
- C: The errors sum to 0.5, giving a bias gradient of about +0.167.
- D: The positive-x points carry label 0, so the weight must fall, not rise.
- E: At w = 0 and b = 0 every probability is 0.5, so the initial loss is ln 2 whatever the data.

**Source:** Derive the first update

## MA-ch09.29

Before running an AI-written training script, a student writes down, with the date: "On the first update the weight should move in the positive direction and the bias should not move; if the weight moves negative or the bias moves, a sign or a feature factor in the gradient is wrong." The student reasoned this from the labels and the signs of the features. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A prediction that states what a wrong result would look like can be falsified by the output.
- [ ] B. A prediction written after reading the output only describes the output.
- [ ] C. Plausible-looking decimals from the script confirm the gradient code is correct.
- [ ] D. A prediction made before the run gives a check that does not depend on the script's output.
- [ ] E. Predicting the direction of the first update requires running the code.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A claim with a stated failure condition risks being wrong, which is what makes it a test.
- B: After seeing the output, any story fits it, so it can no longer test anything.
- C: Numbers that look reasonable can still come from a sign error or a missing factor.
- D: Reasoning done in advance is an independent route to compare against the code.
- E: The direction follows from the labels, the feature signs, and the sign of the gradient formula.

**Source:** Derive the first update

## MA-ch09.30

Two implementations of full-batch gradient descent for logistic regression on N = 50 examples differ in one line. Version M divides the summed per-example gradients by N. Version S does not divide. Both use learning rate 0.1. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Version S takes steps 50 times larger than Version M.
- [ ] B. Version S is equivalent to Version M with a learning rate of 5.0.
- [ ] C. Doubling the dataset doubles the size of Version S's step but not Version M's.
- [ ] D. A test that only checks that the training loss decreased cannot reliably tell the two versions apart.
- [ ] E. Version S's step points in a different direction from Version M's.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The sum is N times the mean, so the step is multiplied by 50.
- B: 0.1 times 50 equals 5.0 applied to the mean gradient.
- C: The sum grows with N while the mean does not.
- D: A too-large step can still reduce the loss early on, so a "loss fell" test may pass.
- E: Scaling a vector by a positive constant leaves its direction unchanged.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.31

Training data as (x, y) pairs: (-3, 0), (-1, 0), (1, 1), (3, 1). A model starts at w = 0, b = 0 and takes a full-batch step with learning rate 0.5. A correct implementation uses mean((p - y)*x) for the weight and mean(p - y) for the bias. A buggy version also uses mean((p - y)*x) for the bias. At the start p is 0.5 for every example. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The correct bias gradient at the start is 0, so b stays at 0 after the first step.
- [ ] B. The bug can only be detected by examining final held-out accuracy.
- [ ] C. The buggy version moves b because the data are asymmetric around zero.
- [ ] D. The buggy bias gradient at the start is -1.0, so b moves to 0.5.
- [ ] E. The derivative of the loss with respect to the bias includes a factor of x.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The errors are 0.5, 0.5, -0.5, -0.5, which sum to zero.
- B: A test of the exact first-step values would catch the bug without any held-out data.
- C: The data are symmetric; the movement comes from the extra x factor, which stops the errors cancelling.
- D: The x-weighted errors are -1.5, -0.5, -0.5, -1.5, whose mean is -1.0, and 0 - 0.5*(-1.0) = 0.5.
- E: The score changes by 1 per unit of bias, so the bias derivative is just the error.

**Source:** The gate: say what should change before you change it

## MA-ch09.32

To check a hand-derived gradient of a loss L(w), a developer compares it with the central finite difference [L(w+h) - L(w-h)] / (2h) for a small h. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The central difference does not use the derivative formula being checked.
- [ ] B. Agreement within tolerance shows the analytic gradient matches the derivative of the loss function as coded.
- [ ] C. Shrinking h toward 1e-16 keeps improving the accuracy of the estimate.
- [ ] D. Agreement shows the loss function is the right objective for the application.
- [ ] E. For a smooth loss, the central difference error shrinks roughly with h squared, while a one-sided difference shrinks roughly with h.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: It only evaluates the loss at two nearby points, so it fails differently from the algebra.
- B: Both quantities describe the same coded objective, so agreement confirms the derivation.
- C: Subtracting nearly equal numbers loses digits, so very small h adds round-off error.
- D: If the objective is wrong for the task, derivative and finite difference still agree.
- E: Taylor expansion shows the odd terms cancel in the central difference.

**Source:** Derive the first update

## MA-ch09.33

For a single example with x = 2, y = 1, and b = 0, the loss as a function of the weight is L(w) = ln(1 + e^(-2w)). A developer estimates the derivative at w = 0 with h = 0.01. The central difference [L(h) - L(-h)]/(2h) is about -1.0000, and the one-sided difference [L(h) - L(0)]/h is about -0.995. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The central difference is within 0.0001 of the exact derivative.
- [ ] B. The exact derivative at w = 0 is -0.5.
- [ ] C. Increasing h to 0.1 makes the one-sided estimate more accurate.
- [ ] D. The negative sign means L increases as w increases.
- [ ] E. The one-sided difference is off by about 0.05.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The central estimate agrees with -1 to many decimal places.
- B: The derivative is (p - y)*x = (0.5 - 1)*2 = -1, not -0.5.
- C: The one-sided error grows roughly in proportion to h; at h = 0.1 the estimate is about -0.95.
- D: A negative derivative means L decreases as w increases.
- E: The one-sided estimate of -0.995 differs from -1 by about 0.005, not 0.05.

**Source:** Derive the first update

## MA-ch09.34

Gradient descent minimizes L(w) = w^2, whose gradient is 2w, starting from w = 1 with learning rate r. Each step gives w <- (1 - 2r)w. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With r = 0.1 the iterates fall steadily: 1, 0.8, 0.64, and so on.
- [ ] B. With r = 0.5 the iterate reaches the minimizer w = 0 in one step.
- [ ] C. With r = 0.9 the iterates converge without ever changing sign.
- [ ] D. With r = 1.0 the iterates alternate between 1 and -1 forever.
- [ ] E. With r = 1.1 the iterates diverge, growing in magnitude by a factor of 1.2 each step.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The multiplier 1 - 0.2 = 0.8 shrinks the iterate without changing sign.
- B: The multiplier 1 - 1 = 0 sends w to 0 at once.
- C: The multiplier is -0.8, so the sign flips each step even though the magnitude shrinks.
- D: The multiplier is -1, so the magnitude never shrinks.
- E: The multiplier is -1.2, which has magnitude above 1.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.35

Consider the learning rate in gradient descent for a logistic classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A very small rate can make progress too slow within a limited step budget.
- [ ] B. The rate is a setting of the experiment: the update rule changes the weight and bias but never the rate.
- [ ] C. Picking the rate by looking at accuracy on the final test set turns the test set into tuning data.
- [ ] D. Reducing the rate is the usual remedy when training makes progress too slowly.
- [ ] E. A rate that works well for one dataset is safe for every dataset.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Tiny steps may not get far enough in the budget.
- B: The rate scales the gradient but is chosen by the practitioner, not learned.
- C: Once a choice depends on a set, that set is development data and its estimate is optimistic.
- D: Slow progress usually calls for a larger rate or better-scaled features; a smaller rate slows it further.
- E: The stable range depends on the loss surface and the feature scales.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.36

A training function runs exactly 500 updates at a fixed learning rate, with no convergence test, and returns the final parameters. The final average training loss is 0.04. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If held-out accuracy looks poor, extending training until it looks good keeps the held-out set a clean test.
- [ ] B. On linearly separable data with no regularization, training loss reaches exactly zero after enough steps.
- [ ] C. Deciding the budget before the run protects against stopping at a flattering point.
- [ ] D. A final loss of 0.04 does not show that 500 steps was the right budget.
- [ ] E. A fixed step budget and early stopping on a validation loss are the same stopping criterion.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Tuning on the held-out set turns it into development data.
- B: Logistic loss approaches zero as weights grow but is positive for every finite weight.
- C: A budget fixed beforehand cannot be tuned to the observed result.
- D: The number of updates is a choice, and a low loss does not validate it.
- E: The first stops by count, the second by observed validation performance.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.37

A one-feature logistic model with the bias fixed at 0 is fit to a single example x = 1, y = 1 using the loss ln(1 + e^(-w)). The loss is about 0.313 at w = 1, about 0.0067 at w = 5, and about 0.000045 at w = 10. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A loss of 0.000045 means the model will be 99.9955% accurate on future data.
- [ ] B. Adding an L2 penalty on w would give a finite minimizer.
- [ ] C. At w = 5 the model's probability for label 1 on this example is about 0.993.
- [ ] D. Gradient descent on this problem has no finite minimizer.
- [ ] E. The loss keeps decreasing as w increases and approaches, but never reaches, 0.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Training loss on one example says nothing about accuracy on new data.
- B: The penalty grows with w and balances the shrinking loss, so a minimum appears at finite w.
- C: sigma(5) is about 0.9933, consistent with a loss of -ln(0.9933), about 0.0067.
- D: Since the loss keeps falling, no finite w is optimal.
- E: The loss is positive for every finite w but falls toward zero as w grows.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.38

A training routine returns a "history" list containing exactly two numbers: the loss before the first update and the loss after the last. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Recording loss only on the training set is enough to choose a stopping point.
- [ ] B. Two values do not form a learning curve.
- [ ] C. From these two values one cannot tell whether the loss fell steadily, oscillated, or spiked and recovered.
- [ ] D. The two values show the run was numerically stable throughout.
- [ ] E. A final value below the initial value proves the loss decreased at every step.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Training loss usually keeps falling, so choosing where to stop needs a separate validation signal.
- B: A curve needs the loss at many steps.
- C: The endpoints are consistent with many different paths.
- D: Stability concerns every step, and only the endpoints were recorded.
- E: Endpoints say nothing about the intermediate steps.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.39

For a logistic classifier, the weight gradient for one example is (p - y)*x, while the bias gradient is (p - y). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The bias gradient depends on the feature value x.
- [ ] B. Weight steps scale with the magnitude of the feature, so features in the thousands can need a smaller learning rate than features near 1.
- [ ] C. Rescaling a feature from meters to millimeters leaves the optimal weight unchanged.
- [ ] D. A rate that works for x in [0, 1] will work unchanged for x in [0, 1000].
- [ ] E. Standardizing features to zero mean and unit variance usually lets a single learning rate work across features.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The bias gradient is the mean error with no x factor.
- B: A large x multiplies the error, so the weight update can overshoot at a rate fine for small x.
- C: Multiplying the feature by 1000 requires dividing the optimal weight by 1000.
- D: A thousandfold larger feature gives much larger weight steps, which can destabilize training.
- E: Comparable scales give comparable gradient magnitudes.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.40

A dataset has N = 1,000 examples. Full-batch gradient descent uses all 1,000 examples per update. Minibatch stochastic gradient descent uses randomly shuffled batches of 100. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With minibatches of 100, each update uses a gradient computed from all 1,000 examples.
- [ ] B. The gradient from a randomly drawn minibatch is a noisy but unbiased estimate of the full-batch gradient.
- [ ] C. One pass over the data with batch size 100 performs 100 updates.
- [ ] D. A trainer that uses full batches, never shuffles, and never adapts its rate represents every aspect of large-scale training.
- [ ] E. Minibatch gradients have lower variance than full-batch gradients.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Each update sees only its 100 examples.
- B: The average over a random subset has expectation equal to the full average.
- C: 1,000 / 100 = 10 batches, so a pass performs 10 updates.
- D: A simple full-batch loop omits shuffling, minibatches, and adaptive rates, so the analogy is limited.
- E: A minibatch gradient is a noisier estimate with higher variance than the full-batch gradient; its benefit is cheaper updates.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.41

A student tries learning rates 0.01, 0.1, 1, and 10 on the same data, and reports only the run with the lowest final training loss. The rate-10 run diverged to NaN and was left out of the write-up. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The run with the lowest final training loss is the right one to deploy without further evaluation.
- [ ] B. Choosing the evaluation criterion after seeing the results is fine as long as the chosen run is labeled.
- [ ] C. Dropping the diverged run is acceptable because failures are not informative.
- [ ] D. Omitting the diverged run hides information about the method's sensitivity to the rate.
- [ ] E. Holding the data and initial parameters fixed across runs makes the comparison meaningful.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Lowest training loss can reflect overfitting and says nothing about unseen data.
- B: Picking the criterion after the fact turns a comparison into a search for the most attractive run.
- C: Failed runs show where the method breaks, and reports should keep them.
- D: A divergence at a large rate is a finding about stability.
- E: Changing only the rate isolates its effect.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.42

A one-feature classifier is trained from w = 0, b = 0 on (-2, 0), (-1, 0), (1, 1), (2, 1) and learns a positive weight. Now every label is flipped: (-2, 1), (-1, 1), (1, 0), (2, 0). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The learned weight should become negative.
- [ ] B. The first update moves w in the same direction as in the original run.
- [ ] C. The learned bias should become clearly negative.
- [ ] D. The initial loss is higher than in the original run.
- [ ] E. By the symmetry sigma(-a) = 1 - sigma(a), the final training loss should match the original run's.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Larger x now goes with label 0, so a negative weight reduces the loss.
- B: The gradient sign reverses, so w moves the opposite way.
- C: The data stay symmetric about zero, so the bias stays near zero.
- D: At w = 0 and b = 0 every probability is 0.5, so the initial loss is ln 2 in both runs.
- E: Flipping labels and negating w maps one problem exactly onto the other.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.43

An engineer sets aside four evaluation points before training and never passes them to the training function. The engineer chose them near the same decision boundary as the training points, and the trained model classifies all four correctly at threshold 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the engineer uses these four points to choose a learning rate, they become development data and are no longer an independent test.
- [ ] B. A broader performance claim needs a justified sampling process, a task definition, and a larger evaluation.
- [ ] C. The result supports "these four points are classified correctly" but not "the model generalizes."
- [ ] D. "Held out" here describes how the points were handled: they were not used for fitting.
- [ ] E. The four points are a random sample of the deployment population.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Once a set guides a choice, later results on it are no longer independent of that choice.
- B: Population claims need an explicit sampling design and enough data to estimate error.
- C: Four hand-built points support a narrow claim about those points only.
- D: Being held out is a statement about procedure, not about representativeness.
- E: Points chosen by the engineer around the training pattern are not a random sample of any population.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.44

A team has 200 evaluation examples and measures 82% accuracy (164 correct). Later, 50 of those examples are accidentally copied into the training set and the model is retrained. Suppose the model now answers all 50 copied examples correctly, while its accuracy on the other 150 examples stays at 82% (123 correct). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 150 untouched examples can no longer give a usable estimate of accuracy on unseen data.
- [ ] B. A rise in reported accuracy from 82% to 86.5% would reflect better generalization.
- [ ] C. The 50 copied examples no longer measure performance on unseen data.
- [ ] D. Reporting 86.5% as unseen-data accuracy is acceptable if the leak is disclosed in a footnote.
- [ ] E. Accuracy on the full 200 would now read 86.5%.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Those 150 were never trained on, so they still estimate unseen-data accuracy.
- B: The rise comes from memorized training examples; nothing about unseen data changed.
- C: The model was fit on them, so correct answers there are expected regardless of generalization.
- D: A footnote does not fix an inflated number; the clean estimate is the 150-example result or a rebuilt split.
- E: (123 + 50) / 200 = 173/200 = 0.865.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.45

A team trains a classifier, tries 12 combinations of learning rate and step count, picks the combination with the highest accuracy on their single evaluation set, and reports that accuracy as the model's expected performance. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reported accuracy is likely to be optimistic relative to fresh data.
- [ ] B. After the choice is made, the final estimate should come from data that played no role in any choice.
- [ ] C. Using a separate development set for choosing settings and a test set consulted once for the final estimate addresses the problem.
- [ ] D. The evaluation set has become development data.
- [ ] E. A development set can be reused for any number of selections without its estimate becoming biased.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The winner is selected partly for lucky noise on that set, so its score overstates its true performance.
- B: Only data untouched by any decision gives an unbiased final estimate.
- C: Splitting the roles keeps the final estimate independent of the selection.
- D: Choosing among settings by their score on a set makes that set part of tuning.
- E: Every selection made on a set adds some optimism to its estimate.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.46

A team compares 30 prompt variants on the same 100 questions. Suppose every variant truly has 70% accuracy and observed scores vary only by chance. By the binomial distribution, the expected best observed score among 30 such variants is about 79%, and the best is at or above 75% in over 99% of repeated experiments. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Trying more variants reduces the overstatement.
- [ ] B. Reporting the top variant's score would overstate its true accuracy.
- [ ] C. The best variant's observed score is an unbiased estimate of its own true accuracy.
- [ ] D. The expected overstatement in this setup is roughly 9 percentage points.
- [ ] E. Re-scoring only the winner on fresh questions gives a less biased estimate.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: More candidates raise the expected maximum of noise, which increases the overstatement.
- B: The maximum of many noisy scores is above the average, and all variants truly score 70%.
- C: Selecting the maximum creates an upward bias.
- D: Expected best about 79% against a true 70% is about 9 points.
- E: Fresh questions have not influenced the selection, so the winner's score on them is not inflated by it.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.47

A classifier gets 4 of 4 held-out points right. Another classifier gets 40 of 40 right on a different test set. If a classifier's true accuracy were p, the chance of a perfect score on n points is p^n. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. After 4 of 4 correct, a true accuracy of 60% is still plausible, since 0.6^4 is about 0.13.
- [ ] B. A perfect score on any finite test set proves the true error rate is zero.
- [ ] C. A perfect score on 40 points is no stronger evidence of high accuracy than a perfect score on 4 points.
- [ ] D. Getting 4 of 4 correct demonstrates that accuracy is above 95%.
- [ ] E. After 40 of 40 correct, a true accuracy of 90% is about as plausible as it was after 4 of 4 correct.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A 13% chance of a perfect score is far from negligible.
- B: Finite samples only bound the error rate; they never prove it is zero.
- C: More points shrink the range of accuracies compatible with a perfect score.
- D: A true accuracy of 95% would give 4 of 4 about 81% of the time, so 4 of 4 cannot rule it out.
- E: 0.9^4 is about 0.66 while 0.9^40 is about 0.015, so the longer perfect run makes 90% far less plausible.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.48

Six held-out examples have predicted probabilities of label 1 and true labels as follows: (0.90, label 1), (0.80, label 1), (0.40, label 1), (0.35, label 0), (0.20, label 0), (0.10, label 0). A prediction is label 1 when the probability is at least the chosen threshold. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A threshold of 0.38 classifies all six correctly.
- [ ] B. Changing the threshold leaves the model's parameters unchanged.
- [ ] C. Accuracy at threshold 0.3 is higher than at 0.5.
- [ ] D. Accuracy at threshold 0.5 is 5 of 6.
- [ ] E. Every positive example has a higher probability than every negative one, so the ranking is perfect (AUC of 1).

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: At 0.38 the 0.40 positive is caught and 0.35 stays negative.
- B: The threshold is a decision rule applied after scoring; the parameters are untouched.
- C: At 0.3 the 0.35 negative becomes a false positive, giving 5 of 6, the same as at 0.5.
- D: At 0.5 the 0.40 positive is missed and the other five are right.
- E: The lowest positive score (0.40) exceeds the highest negative score (0.35).

**Source:** Score, probability, and decision are three layers

## MA-ch09.49

A classifier decides whether to escalate a message to a human. A missed escalation (false negative) costs 20 units and an unnecessary escalation (false positive) costs 1 unit. On 1,000 messages at threshold 0.5, Model A makes 10 false negatives and 40 false positives and has average log loss 0.30. Model B makes 25 false negatives and 10 false positives and has average log loss 0.28. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Model A's total cost is 240 units and Model B's is 510 units.
- [ ] B. Lower log loss implies lower expected cost.
- [ ] C. Threshold 0.5 is the cost-optimal threshold for calibrated probabilities here.
- [ ] D. If probabilities are calibrated, minimizing expected cost means escalating when the probability exceeds 1/21, about 0.048.
- [ ] E. Model B makes more total errors than Model A.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Model A costs 10*20 + 40*1 = 240; Model B costs 25*20 + 10*1 = 510.
- B: Log loss weights errors by confidence, not by the real cost of each kind of error.
- C: Unequal error costs move the optimal threshold far below 0.5.
- D: Escalate when p*20 > (1-p)*1, which gives p > 1/21.
- E: Model B makes 35 errors against Model A's 50.

**Source:** What a lower loss claims

## MA-ch09.50

A model assigns probability 0.9 to each of 1,000 test items, and 600 of those items are actually positive. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A model trained with cross-entropy loss will be well calibrated without further checks.
- [ ] B. Among these items the observed positive rate is 0.6, so the model is overconfident there.
- [ ] C. The model's accuracy at threshold 0.5 could still be high.
- [ ] D. Checking calibration requires labeled data grouped by predicted probability.
- [ ] E. A handful of correct predictions with extreme probabilities shows that the model is calibrated.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Cross-entropy training does not guarantee calibration, especially under overfitting or distribution shift.
- B: A calibrated model would be right about 90% of the time at probability 0.9.
- C: Accuracy depends only on which side of the threshold predictions fall, not on how confident they are.
- D: A reliability analysis compares predicted probabilities with observed frequencies in groups.
- E: Calibration is a statement about frequencies over many cases; a few correct predictions cannot establish it.

**Source:** Score, probability, and decision are three layers

## MA-ch09.51

A report on a small experiment gives these facts: average training loss fell from 0.69 to 0.11 over the run; six separately specified held-out points, built from the same pattern as the training data, were all classified correctly at threshold 0.5. Check each statement that the evidence supports. Each statement is worth 1 point (5 points total).

- [ ] A. Training loss decreased from 0.69 to 0.11 under the stated procedure.
- [ ] B. The predicted probabilities are calibrated.
- [ ] C. The model generalizes to new real-world data.
- [ ] D. Increasing the feature by one unit causes the outcome to change in the real world.
- [ ] E. The six held-out points were classified correctly.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: That is exactly what was measured.
- B: Calibration needs a labeled sample large enough to compare probabilities with frequencies.
- C: Six constructed points of the same pattern cannot establish performance on a real population.
- D: A fitted association does not identify what happens when a real-world variable is changed.
- E: That is the recorded held-out result.

**Source:** What a lower loss claims

## MA-ch09.52

A logistic model fit to historical records of an online class has a positive weight on x, the number of reminder emails a student opened in the first month, for the label "passed." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A third factor such as motivation could raise both email opening and passing.
- [ ] B. Evaluating the function at a larger x answers what would happen to pass rates if the class required students to open emails.
- [ ] C. The positive weight is consistent with students who are already on track opening more emails.
- [ ] D. Collecting ten times more records from the same observational source would settle whether opening emails helps students pass.
- [ ] E. For a student with x = 4, evaluating the fitted function answers what label the model will assign.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A common cause produces a positive weight without any effect of the emails.
- B: The function's response to a changed input is not the world's response to a changed behavior.
- C: Reverse causation produces the same positive association.
- D: More data from the same source reduces noise but cannot remove confounding or reverse causation.
- E: A prediction question about the model is answered by evaluating the fitted function.

**Source:** Decide what kind of question you are asking

## MA-ch09.53

Judea Pearl's ladder of causation separates association, intervention, and counterfactual questions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Do patients who take drug X recover more often than those who do not?" is an association question.
- [ ] B. Predicting the label of a new record with a fitted classifier is an intervention question.
- [ ] C. "If we give drug X to everyone in this clinic, will the recovery rate rise?" is an intervention question.
- [ ] D. Interventional answers can generally be recovered from purely observational data without further assumptions.
- [ ] E. "Would this particular patient have recovered had she not taken X?" is a counterfactual question.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: It asks what goes with what in observed data.
- B: Prediction is an association-level task, answered from the fitted pattern.
- C: It asks what happens if the treatment is imposed.
- D: Interventional claims need causal assumptions or randomization that the data alone do not supply.
- E: It asks what would have happened to a specific case under a different action.

**Source:** Decide what kind of question you are asking

## MA-ch09.54

Two treatments, X and Y, were assigned by clinicians. Success counts for mild cases: X succeeded in 8 of 10, Y in 70 of 90. For severe cases: X succeeded in 30 of 90, Y in 2 of 10. Pooled over all patients, X succeeded in 38 of 100 and Y in 72 of 100. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Within severe cases, X has the higher success rate (about 33% versus 20%).
- [ ] B. The pooled result differs from the within-group results because X was given mostly to severe cases and severity strongly affects the outcome.
- [ ] C. Within mild cases, X has the higher success rate (80% versus about 78%).
- [ ] D. Pooled over all patients, X's success rate (38%) is lower than Y's (72%).
- [ ] E. The pooled comparison is the right one for choosing a treatment because it uses all of the patients.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: 30/90 is 33.3% and 2/10 is 20%.
- B: X's pool is 90% severe cases, which have low success for either treatment.
- C: 8/10 is 80% and 70/90 is 77.8%.
- D: 38/100 against 72/100.
- E: Which comparison is right depends on the causal structure; here severity drives both assignment and outcome, so the pooled rate is misleading.

**Source:** Decide what kind of question you are asking

## MA-ch09.55

A model that flags at-risk students was fit on a year in which nobody acted on its flags. The next year advisors contact every flagged student, and the model is later refit on that year's outcomes. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Refitting on the new year's data without recording who was contacted mixes the prediction task with the effect of the intervention.
- [ ] B. The relationship between features and outcomes can change once people act on flags, so the first model's accuracy may not carry over.
- [ ] C. The first-year fit tells directly how much advisor contact will raise pass rates.
- [ ] D. If the model is accurate on historical data, acting on it cannot change the process that generated the data.
- [ ] E. Flagged students who pass after being contacted may reflect the success of the contact rather than errors in the model.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Without records of the intervention, the new labels confound the original pattern with the response to contact.
- B: Acting on predictions alters the process that produced the data the model learned from.
- C: A model fit when nobody acted contains no information about what acting does.
- D: Historical accuracy gives no protection against feedback from the model's own use.
- E: A pass after contact is consistent with a helpful intervention, so it is not clear evidence the flag was wrong.

**Source:** Decide what kind of question you are asking

## MA-ch09.56

A researcher wants to learn whether a job-training program causes higher wages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A regression coefficient on participation equals the causal effect whenever R-squared is high.
- [ ] B. Random assignment makes participation independent of pre-existing differences between people, in expectation.
- [ ] C. An unmeasured variable that affects both participation and wages can bias the observational estimate.
- [ ] D. Observational data can support a causal claim when the assumptions are stated and defended.
- [ ] E. A very large observational dataset with many recorded covariates is enough for an unbiased causal estimate.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A good fit measures prediction quality, not causal identification.
- B: Randomization breaks the link between assignment and confounders.
- C: An omitted common cause creates a spurious or distorted association.
- D: Methods such as adjustment, instruments, and natural experiments work under explicit assumptions.
- E: Size does not remove bias from unmeasured confounders or selection.

**Source:** Decide what kind of question you are asking

## MA-ch09.57

An analyst asks a language model to help with a causal question about an observational dataset. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The analyst remains responsible for defending the assumptions they act on.
- [ ] B. The model knows how the dataset was collected even if nobody has told it.
- [ ] C. Fluent text about confounding is evidence that the model has identified the causal effect in this dataset.
- [ ] D. The model can work out what follows under a causal structure the analyst stipulates.
- [ ] E. The model can list candidate confounders drawn from patterns in the text it has seen.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The person who acts on the conclusion must justify the causal assumptions.
- B: Study design and data collection details come only from the people who hold them.
- C: Fluency about causation is not identification of it in a particular dataset.
- D: Computing consequences under a stated model is within reach, and the result is conditional on the stated structure.
- E: Candidate confounders can be proposed from general knowledge and prompted for.

**Source:** What is Claude's here, and what is yours

## MA-ch09.58

A team is changing a classifier that decides which messages to escalate to a human, with an AI coding assistant available. Check each statement about tasks that should stay with the accountable person. Each statement is worth 1 point (5 points total).

- [ ] A. Typing out the training loop.
- [ ] B. Running the unit tests.
- [ ] C. Asserting the causal assumptions the team will defend when acting on the result.
- [ ] D. Deciding what "better" means for the task, such as how much a missed escalation costs relative to a false alarm.
- [ ] E. Deciding whether the stakeholder's question is "what will the model say" or "what happens if we act."

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Writing code is delegable as long as its output is checked by an independent route.
- B: Executing tests is mechanical work; what stays with the person is judging whether the tests are enough.
- C: Whoever acts on the conclusion must supply and defend the causal assumptions.
- D: The objective expresses values about the task that the data cannot supply.
- E: Choosing between a prediction question and an intervention question determines what evidence is relevant.

**Source:** What is Claude's here, and what is yours

## MA-ch09.59

Before running any experiment that changes a system, a team writes down the objective, the held-out evaluation set, and the stopping rule. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Fixing the evaluation set before seeing results prevents choosing flattering test cases afterwards.
- [ ] B. Extending training after a poor held-out result leaves the held-out set a clean test.
- [ ] C. Pre-specifying helps only for experiments that involve training, not for prompt changes.
- [ ] D. If the plan must change after a disappointing result, the held-out points already seen can still serve as an untouched test.
- [ ] E. The data themselves determine what counts as "better."

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Choosing test cases after the fact lets the answer shape the question.
- B: Adjusting the run in response to the held-out result makes that set part of the tuning.
- C: Any change evaluated against evidence benefits from criteria written down before the result.
- D: Points that have been seen and have influenced a decision are development data.
- E: Data contain no opinion about the objective; people choose what to optimize.

**Source:** The gate: say what should change before you change it

## MA-ch09.60

A test suite for a logistic-regression trainer checks only (1) that the average loss after training is lower than before and (2) that the learned weight is positive on positively correlated data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A bug that accidentally includes held-out points in the training list would be caught by these two tests.
- [ ] B. Passing both tests shows the optimizer behaves correctly for all datasets and rates.
- [ ] C. Writing a deliberately wrong version is unnecessary if the tests pass on the correct implementation.
- [ ] D. A test asserting the exact weight after one step at a stated rate, derived by hand, would catch an implementation that sums instead of averaging the gradient.
- [ ] E. An implementation that sums instead of averaging the gradient would likely still pass both tests.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Leakage changes what the evaluation means, not whether the loss fell or the weight is positive.
- B: Two checks on one dataset say nothing about other data or rates.
- C: Passing on correct code does not show the tests would fail on wrong code.
- D: The summed version's first step is N times too large and would miss the hand-derived value.
- E: A step that is too large can still lower the loss and still make the weight positive.

**Source:** The gate: say what should change before you change it

## MA-ch09.61

An AI assistant writes a gradient function and, in the same session, writes a unit test that compares the function against the function's own earlier output. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A hand-derived expected value for one update provides a check that does not depend on the code.
- [ ] B. When the hand value and the code disagree, the hand value should be changed to match the code.
- [ ] C. When one author writes both the function and its test from the same understanding, a shared misreading is impossible.
- [ ] D. A test that compares code to its own earlier output can pass even if both are wrong.
- [ ] E. Agreement between the derivative and a finite-difference estimate shows that the objective matches the application's goal.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: An independent derivation can fail differently from the code.
- B: The disagreement must be explained; adjusting the expected value to fit the code removes the check.
- C: A single misunderstanding can corrupt both artifacts the same way.
- D: The test measures consistency with itself, not correctness.
- E: Both quantities describe the objective as coded; whether it is the right objective is a separate question.

**Source:** Derive the first update
