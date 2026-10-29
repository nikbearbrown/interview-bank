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

A simple classifier computes a score from a feature, converts the score to a probability with the sigmoid function, and predicts label 1 when the probability is at least 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The sigmoid function turns any score into a number between 0 and 1.
- [ ] B. A larger score gives a larger probability of label 1.
- [ ] C. A probability between 0 and 1 is, for that reason alone, an accurate estimate of how likely the label is.
- [ ] D. Predicting label 1 when the probability is at least 0.5 is the same as predicting label 1 when the score is at least 0.
- [ ] E. A score of exactly 0 gives a probability of exactly 0.5.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The sigmoid squashes the whole range of scores into the interval from 0 to 1.
- B: The sigmoid is increasing, so a larger score gives a larger probability.
- C: Lying between 0 and 1 is a property of the formula; whether the probabilities match real frequencies has to be checked against outcomes.
- D: A score of 0 maps to a probability of exactly 0.5, so the two ways of stating the rule agree.
- E: The sigmoid of 0 is 0.5, which is why a probability threshold of 0.5 corresponds to a score threshold of 0.

**Source:** The model: two numbers and a squashing function

## MA-ch09.15

A classifier's parameters are all set to zero before training. It is then evaluated on labeled data in which 70 percent of the examples have label 1. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. It gives the same probability, 0.5, for every example.
- [ ] B. Its predictions do not depend on the feature value.
- [ ] C. Its average loss at this point equals the loss of always answering "fifty-fifty", a baseline that training should beat.
- [ ] D. It starts with a probability of 0.7 for every example because 70 percent of the labels are 1.
- [ ] E. A training loss that falls below this starting value shows that the model fits the training data better than a fifty-fifty guesser does.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: With every parameter at zero the score is zero for every input, and the sigmoid of zero is 0.5.
- B: The parameters that connect the feature to the output are all zero, so the feature has no effect yet.
- C: An uninformed 50/50 guesser is the reference point that a trained model must improve on.
- D: Setting parameters to zero does not encode the label balance; the model has not looked at the labels yet.
- E: Training loss measures fit to the training data, so falling below the baseline means a better fit there; it says nothing about new data.

**Source:** The model: two numbers and a squashing function

## MA-ch09.16

A programmer implements the sigmoid function with a direct formula. On a very large negative score the function fails because an intermediate number is too large for the computer to represent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Computers store numbers with limited range and precision, so a formula that is correct on paper can fail for extreme inputs.
- [ ] B. A mathematically equivalent rewrite of the formula can avoid the failure.
- [ ] C. A passing test on ordinary inputs shows that the function works for every input.
- [ ] D. If a function returns a number without raising an error, the number must be correct.
- [ ] E. Testing extreme inputs is unnecessary if ordinary inputs pass.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Overflow and rounding come from the finite size of the number format, not from a mistake in the mathematics.
- B: An equivalent form can be arranged so that only safe values are computed.
- C: Ordinary inputs do not exercise the extreme cases where such failures occur.
- D: Floating-point code can return a wrong number silently, for example after a value rounds away.
- E: Extreme and edge-case inputs are where numerical problems show up, so passing on ordinary inputs is not enough.

**Source:** The model: two numbers and a squashing function

## MA-ch09.17

A one-feature classifier has a weight and a bias. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The sign of the weight determines whether a larger feature value pushes the probability of label 1 up or down.
- [ ] B. The bias shifts where along the feature the decision changes from one label to the other.
- [ ] C. With the bias fixed at zero, the boundary is forced to the point where the feature is zero, so some data cannot be separated well.
- [ ] D. The weight and bias are chosen by the person using the model rather than found from data.
- [ ] E. A positive weight shows that the feature causes label 1.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A positive weight pushes the score up as the feature grows; a negative weight pushes it down.
- B: Changing the bias moves the boundary without changing how steeply the score responds to the feature.
- C: Without a bias, the score is zero, and so the boundary lies, at a feature value of zero whatever the data look like.
- D: The weight and bias are the parameters that training adjusts to fit the data.
- E: A weight describes an association in the training data; it does not show that changing the feature would change the label.

**Source:** The model: two numbers and a squashing function

## MA-ch09.18

A fitted classifier has a positive weight on a feature x. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In the training data, larger values of x went with label 1 more often.
- [ ] B. The size of the weight does not depend on the units in which x is measured.
- [ ] C. The weight shows that raising x would cause label 1 to become more likely.
- [ ] D. Weights on features measured in different units can be compared directly as measures of importance.
- [ ] E. A weight fitted in one population necessarily holds in a different population.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A positive weight means the fitted relationship slopes toward label 1 as x grows.
- B: Measuring x in millimeters instead of meters changes the weight by a factor of a thousand without changing the predictions.
- C: A weight is an association in the data; it does not show what would happen if x were changed.
- D: Weights depend on the scale of their features, so raw weights are not a fair comparison of importance.
- E: A fitted relationship can change when the population changes, so it has to be tested there.

**Source:** The model: two numbers and a squashing function

## MA-ch09.19

A classifier outputs probabilities, and the decision is label 1 when the probability passes a threshold the team chooses. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Raising the threshold makes the classifier label fewer examples as 1.
- [ ] B. Changing the threshold changes the probabilities the model outputs.
- [ ] C. Training sets the best threshold automatically, so the team does not need to decide it.
- [ ] D. The best threshold depends on the costs of the two kinds of error.
- [ ] E. Two classifiers that output the same probabilities can make different decisions if their thresholds differ.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: A higher bar means fewer examples clear it.
- B: The threshold is applied after the probabilities are computed and leaves them unchanged.
- C: The threshold is a decision about costs and uses, made by people; training does not choose it.
- D: If a missed positive costs much more than a false alarm, a lower threshold is usually better.
- E: Decisions come from probabilities plus a threshold, so a different threshold gives different decisions.

**Source:** Score, probability, and decision are three layers

## MA-ch09.20

A one-feature classifier predicts whether a job will run long from its input size. Long jobs mostly have large sizes and short jobs mostly have small sizes, with the dividing point near 5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A model with a bias term can place its decision boundary near 5.
- [ ] B. A model with the bias fixed at zero cannot place its boundary near 5, because its boundary is forced to a feature value of 0.
- [ ] C. If a toy dataset happens to be symmetric around zero, that shows a bias term is never needed.
- [ ] D. For a sigmoid classifier, the boundary is where the score equals zero.
- [ ] E. Removing a single training point can never move the fitted boundary.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The bias lets the score cross zero at a feature value other than zero.
- B: With no bias the score is zero at a feature value of zero, so the boundary sits there.
- C: One symmetric toy dataset says nothing about the general case; most real data are not centered at zero.
- D: A score of zero corresponds to a probability of 0.5, the usual decision point.
- E: The fitted parameters depend on all of the training data, so changing one point can move the boundary.

**Source:** Score, probability, and decision are three layers

## MA-ch09.21

A classifier outputs a probability for each example, and a loss function turns each prediction into a penalty that training tries to reduce. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A loss function states, in a single number, what counts as a better or a worse prediction.
- [ ] B. Cross-entropy penalizes a confident wrong prediction much more than an uncertain wrong one.
- [ ] C. Accuracy and cross-entropy always rank two models in the same order.
- [ ] D. A loss that is easy to compute is therefore a good measure of what the application needs.
- [ ] E. Choosing the loss is a decision about what the model is asked to do, made by people.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The loss is the explicit objective: whatever it rewards, training pushes toward.
- B: Cross-entropy grows steeply as the probability given to the true label approaches zero.
- C: Accuracy ignores how confident the predictions were, so models can rank differently under the two measures.
- D: Convenience does not make a loss fit the purpose; the loss has to reflect what matters in use.
- E: The optimizer lowers whatever it is given, so the choice of objective belongs to the people who set the task.

**Source:** Loss makes the objective explicit

## MA-ch09.22

Two classifiers have the same accuracy on the same test data. One gives confident probabilities, mostly right but with a few confidently wrong. The other gives cautious probabilities. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Their cross-entropy losses can differ even though their accuracy is the same.
- [ ] B. A few confidently wrong predictions can raise the average loss a great deal.
- [ ] C. Equal accuracy means the two models are equally good for every use.
- [ ] D. Cross-entropy takes the probabilities into account, while accuracy looks only at the final decisions.
- [ ] E. A model with a low average loss on the training data can still have a higher loss on new data.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Equal counts of right and wrong decisions can hide differences in how confident the predictions were.
- B: The penalty for a wrong prediction grows steeply with confidence, so a few such cases can dominate the average.
- C: Which model is better depends on the use, for example whether the probabilities themselves are relied on.
- D: That is the difference between a probability-aware measure and one that only counts decisions.
- E: Training loss measures fit to the training data; new data can behave differently.

**Source:** Loss makes the objective explicit

## MA-ch09.23

Binary cross-entropy compares the probability a model gave to the true label with the outcome. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the model gives a probability near 1 to the true label, the loss is near 0.
- [ ] B. If the model gives a probability near 0 to the true label, the loss is very large.
- [ ] C. The loss can never be negative.
- [ ] D. A loss of exactly 0 can be reached by a model that assigns 0.5 to every example.
- [ ] E. The loss is the same thing as the fraction of predictions that are wrong.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A confident correct prediction costs almost nothing.
- B: The penalty grows steeply as the true label is given less and less probability.
- C: Probabilities lie between 0 and 1, so the penalty is never below zero.
- D: A model that says fifty-fifty about everything has a fixed, clearly positive loss.
- E: The fraction wrong ignores confidence; cross-entropy does not.

**Source:** Loss makes the objective explicit

## MA-ch09.24

A team trains a probability classifier with a smooth loss such as cross-entropy rather than by directly maximizing accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy changes in jumps as the parameters change slightly, while a smooth loss changes gradually.
- [ ] B. A smooth loss tells training which direction to nudge the parameters.
- [ ] C. Minimizing the training loss is the same objective as maximizing accuracy on new data.
- [ ] D. A smooth loss is computed from the examples, so it depends on the data.
- [ ] E. A model with a low training loss can still perform poorly on data it was not trained on.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A tiny change in a parameter usually flips no decisions, so accuracy gives training no gradual signal.
- B: A smooth loss has a slope that points toward better parameters.
- C: Training loss measures fit to the training data; performance on new data is a separate question.
- D: The loss is a function of the examples and the current parameters.
- E: Fitting the training data closely does not guarantee good behavior elsewhere.

**Source:** Loss makes the objective explicit

## MA-ch09.25

A classifier reaches a low loss on a dataset. Check each statement that is true about what that low loss does and does not show. Each statement is worth 1 point (5 points total).

- [ ] A. It says nothing about whether the labels in that dataset were correct.
- [ ] B. It says nothing about whether the dataset resembles the data the model will meet in use.
- [ ] C. It shows that the model's reasoning matches a human's.
- [ ] D. Different loss functions always lead to the same trained model from the same data.
- [ ] E. It shows that the objective was the right one for the application.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A model can fit mislabeled data well, and the loss will not reveal the mistakes.
- B: Loss is measured on the data at hand; a different population can behave differently.
- C: Loss measures how well the outputs fit the labels, not how the model arrives at them.
- D: The loss defines what training pushes toward, so different choices give different models.
- E: Whether the objective suits the application is a judgment made outside the loss.

**Source:** Loss makes the objective explicit

## MA-ch09.26

In gradient descent, the gradient tells how the loss changes as each parameter changes, and an update moves the parameters a small step. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The gradient points in the direction in which the loss increases fastest.
- [ ] B. An update moves the parameters in the opposite direction, to lower the loss.
- [ ] C. A single update is guaranteed to lower the loss on every individual training example.
- [ ] D. The gradient is a fixed property of the model that does not depend on the training data.
- [ ] E. The size of an update does not depend on the learning rate.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The gradient is the direction of steepest increase.
- B: Descent means stepping against the gradient.
- C: An update is chosen to lower the average loss; individual examples can get worse.
- D: The gradient depends on both the data and where the parameters currently are.
- E: The learning rate scales the step; a larger rate gives a larger update.

**Source:** Derive the first update

## MA-ch09.27

A classifier starts with all parameters at zero, and in its training data larger feature values go with label 1. Check each statement that is true about the first training update. Each statement is worth 1 point (5 points total).

- [ ] A. The first update should raise the weight.
- [ ] B. If every label were flipped, the first update would move the weight in the opposite direction.
- [ ] C. The direction of the first update can be predicted from the data before running any code.
- [ ] D. After the first update, the model is guaranteed to classify every training example correctly.
- [ ] E. The first update leaves the weight unchanged because the starting probabilities are all 0.5.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Larger features go with label 1, so a larger weight lowers the loss.
- B: Reversing the labels reverses the relationship the update is pulling toward.
- C: The direction follows from how the labels relate to the feature, which can be reasoned out in advance.
- D: One small step improves the fit but does not make every prediction right.
- E: The starting probabilities are all 0.5, but the errors against the labels are not zero, so the update is not zero.

**Source:** Derive the first update

## MA-ch09.28

In training a simple classifier, the weight's update depends on the feature value and the error, while the bias's update depends on the error alone. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A larger feature value produces a larger change to the weight's update, other things equal.
- [ ] B. The bias's update does not scale with the feature value.
- [ ] C. Rescaling a feature from meters to millimeters leaves the best weight unchanged.
- [ ] D. A learning rate that works for features near 1 will work unchanged for features in the thousands.
- [ ] E. Standardizing features never changes how large the weight updates are.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The weight's gradient is multiplied by the feature, so large features give large steps.
- B: The bias multiplies nothing, so its update has no feature factor.
- C: Changing units rescales the best weight inversely, so the best weight changes.
- D: Features in the thousands make weight steps very large, which can destabilize a rate chosen for small features.
- E: Features on a common scale lead to updates of comparable size, which does change the update sizes.

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

Two implementations of gradient descent differ in one line: one averages the per-example gradients over the dataset and the other sums them. Both use the same learning rate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The summed version takes larger steps as the dataset grows, for the same learning rate.
- [ ] B. The two versions point in the same direction.
- [ ] C. The summed version is equivalent to the averaged version with a larger learning rate.
- [ ] D. A test that only checks that the training loss decreased can reliably tell the two versions apart.
- [ ] E. The scaling of the gradient affects whether training is stable.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A sum grows with the number of examples, while an average does not.
- B: Multiplying a gradient by a positive constant does not change its direction.
- C: Summing multiplies the averaged gradient by the number of examples, which acts like a larger learning rate.
- D: Both versions can lower the loss, so a decrease does not reveal which is which.
- E: A step that is too large can overshoot or diverge, so the scaling matters for stability.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.31

A student's trainer has a bug: it updates the bias using the feature value as well as the error, which is the weight's update rule. The loss still goes down during training. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A final accuracy number alone may not reveal the bug.
- [ ] B. Working out by hand what the first update should do, before running the code, could expose the bug.
- [ ] C. Because the loss goes down, the code must be correct.
- [ ] D. A unit test of the update itself cannot catch the bug, because the loss still goes down.
- [ ] E. The bug can be found only by examining held-out accuracy.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A model with a wrongly trained bias can still look acceptable on a summary number.
- B: A prediction made before the run is a check that does not depend on the code's output.
- C: A decreasing loss is necessary evidence, not sufficient; buggy updates can still lower it.
- D: A test that compares the update with a hand-worked case catches it directly; the decreasing loss does not hide it from such a test.
- E: Tests of the update itself catch it directly; held-out accuracy is neither the only nor the best route.

**Source:** The gate: say what should change before you change it

## MA-ch09.32

To check a hand-derived gradient, a developer estimates the slope numerically by changing a parameter slightly up and down, recomputing the loss each time, and comparing the estimate with the formula. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The numerical estimate does not use the derivative formula being checked.
- [ ] B. Agreement within a tolerance shows the formula matches the slope of the loss as coded.
- [ ] C. Making the change smaller and smaller always improves the estimate, with no limit.
- [ ] D. Agreement shows that the loss is the right objective for the application.
- [ ] E. A check like this is cheap enough to run on a few inputs before trusting AI-written gradient code.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The estimate comes from evaluating the loss itself, so it is an independent route.
- B: If the two agree, the formula is consistent with the coded loss.
- C: With a very tiny change the computer's limited precision makes the estimate noisy, so a moderate size is used.
- D: The check covers the gradient, not whether the loss is what the application needs.
- E: The check needs only a few loss evaluations per parameter.

**Source:** Derive the first update

## MA-ch09.33

A developer's numerical check disagrees with a gradient formula on one input. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The formula, the loss code or the numerical check itself could be at fault.
- [ ] B. A disagreement can be set aside until the model's accuracy has been measured.
- [ ] C. Whether a disagreement matters has nothing to do with its size.
- [ ] D. The formula must be correct because an AI assistant produced it.
- [ ] E. Because the loss decreases during training, the disagreement can be ignored.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Any of the three can be wrong, and the disagreement does not say which.
- B: An unexplained disagreement is a bug until it is explained; accuracy measured later does not settle it.
- C: Small differences can come from limited numerical precision, so the size relative to a tolerance matters.
- D: A source does not make code correct; the check exists because AI-written code can be wrong.
- E: A decreasing loss does not show the gradient is right.

**Source:** Derive the first update

## MA-ch09.34

Gradient descent is run on a simple bowl-shaped loss with different learning rates. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A very small learning rate makes steady but slow progress.
- [ ] B. A moderate learning rate can reach the minimum quickly.
- [ ] C. A learning rate that is too large can overshoot the minimum and bounce around it.
- [ ] D. A learning rate that is large enough can make the loss grow instead of shrink.
- [ ] E. A learning rate that works well on one problem will work on every problem.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Small steps move steadily and may not finish within a limited step budget.
- B: A well-chosen step can land close to the minimum in few updates.
- C: Too large a step jumps past the minimum.
- D: Past a limit, each step overshoots by more than it gains, and training diverges.
- E: The safe range depends on the shape of the loss and the scale of the features, which differ between problems.

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

A classifier is trained on data that it can separate perfectly. With no penalty on the size of the weights, training keeps increasing the weight, and the loss keeps shrinking toward zero but never reaches it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The training loss can keep decreasing without limit.
- [ ] B. A very small training loss shows that the model will be accurate on future data.
- [ ] C. Adding a penalty on the size of the weights can give training a stopping point.
- [ ] D. A very small training loss does not show that the data were correctly labeled.
- [ ] E. Training has to be stopped by a rule chosen in advance, such as a step budget or a validation loss.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: On separable data, larger weights always give more confident correct predictions and a smaller loss.
- B: Training loss measures fit to the training data, not performance on future data.
- C: A penalty makes very large weights costly, so the best weights are finite.
- D: A model can fit incorrectly labeled data just as well; the loss does not reveal label errors.
- E: Without a natural stopping point, the stopping rule has to be decided beforehand, not by looking at a flattering result.

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

A team reports a training experiment. Some of its choices are learned from the data and others are settings chosen by people. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The weights and bias are learned from the data.
- [ ] B. The learning rate, the number of steps and the decision threshold are settings chosen by people.
- [ ] C. Settings such as the learning rate can be left out of the report if the code is shared.
- [ ] D. Two runs that differ only in the learning rate are the same experiment.
- [ ] E. The data and the code alone are enough to reproduce a trained model without stating the settings.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Training adjusts these parameters to fit the examples.
- B: These are design decisions that the training loop does not learn.
- C: A reader cannot judge or reproduce a result without the settings that produced it, even with the code.
- D: Changing a setting changes the experiment and can change the trained parameters.
- E: Without the settings, the same data and code can give a different model.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.40

A model is trained with small random batches of the data per update, instead of the whole data set per update. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Each update's gradient is a noisy estimate of the gradient computed on the full data.
- [ ] B. Minibatch gradients require more computation per update than full-data gradients.
- [ ] C. Gradients from small batches are less noisy than gradients from the full data set.
- [ ] D. A trainer that uses the full data set for every update and never shuffles represents large-scale training.
- [ ] E. At internet scale, the whole data set is normally processed in every update.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A sample of the data gives an estimate of the full-data gradient that varies from batch to batch.
- B: A batch needs less computation than the full data set, and batches map well onto parallel hardware.
- C: Estimating from fewer examples adds noise, not less of it.
- D: Large-scale training uses batches, shuffling and other devices that a full-batch teaching loop omits.
- E: Training sets of internet scale are far too large to process in every single update.

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

A classifier is trained on data in which larger feature values go with label 1 and learns a positive weight. Every label is then flipped and the classifier is retrained from the same starting point. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The learned weight should become negative.
- [ ] B. The first update moves the weight in the same direction as in the original run.
- [ ] C. The final fit should be about as good as in the original run.
- [ ] D. If the retrained weight stayed positive, the code would still be correct.
- [ ] E. This test shows that the model's accuracy on new data is high.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The relationship between the feature and the label is reversed.
- B: The first update follows the labels, so it moves the other way.
- C: Flipping labels mirrors the problem, so the achievable fit is the same.
- D: The expected answer is known in advance, so a different result points to a bug.
- E: The test checks the code's behavior on a mirror problem; it says nothing about new data.

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
