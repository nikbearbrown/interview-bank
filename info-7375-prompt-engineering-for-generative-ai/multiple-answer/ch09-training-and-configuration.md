# Chapter 9: Training and configuration

## MA-ch09.1

A teammate writes up an improved answer as "we trained Claude on our policies" after uploading documents and revising a system prompt. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. If the change was a prompt, the improvement lives in a text file you can diff and copy into another project.
- [ ] B. If the change was retrieval, the improvement would remain after the corpus is deleted.
- [ ] C. Prompting and retrieval change the parameters of an already configured model.
- [ ] D. Training changes parameters through an objective and an update rule.
- [ ] E. The input available during that interaction did change.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: A prompt is text you can diff and copy.
- B: Retrieval lives in a corpus and a selection step, and it disappears when the corpus does.
- C: They change the information supplied for inference, not the parameters.
- D: That is the chapter's definition of training.
- E: Something did change: the input available during that interaction.

**Source:** Chapter 9 - Training and configuration (opening)

## MA-ch09.2

A report says: "Average loss fell from 0.6931471806 to 0.0215209850 and four of four held-out points were right, so the model learned and it generalizes." Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The four-of-four held-out result shows that the model generalizes.
- [ ] B. The loss is the number the optimizer was told to lower, on the data it was shown.
- [ ] C. The "learned" half of the sentence is fine, because the parameters changed by a rule you can print.
- [ ] D. The four held-out points were drawn at random from a natural population.
- [ ] E. The unsupported half of the sentence is caused by a bug in the training code.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The second half is unsupported; four constructed points do not say that.
- B: It measures the training objective on the training pairs.
- C: The chapter accepts the first half.
- D: One person chose them around the same sign boundary as the training data.
- E: The chapter says no line of code is at fault.

**Source:** Chapter 9 - Training and configuration (opening)

## MA-ch09.3

Check each statement that is true about Chapter 1's three jobs as the chapter applies them to a change request. Each statement is worth 1 point (5 points total).

- [ ] A. Claude decides what the update was for and whether four fixtures are a fair test.
- [ ] B. Check means deciding what kind of question you are answering.
- [ ] C. Conduct means stating what should change, and how you will tell, before you change it.
- [ ] D. Drive means deciding what kind of question you are answering, because the causal question and its justification are yours.
- [ ] E. Claude will derive the gradient, write the loop, and tabulate the output more slowly than you can.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Claude will not decide those; they are yours.
- B: That describes Drive; Check is claiming only what the record supports and signing or withholding.
- C: That is the gate.
- D: That is the driver's seat.
- E: The chapter says Claude does the mechanical half faster than you can.

**Source:** Chapter 9 - Training and configuration (opening)

## MA-ch09.4

Check each statement that is true about the classifier built in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Its training data are four constructed examples.
- [ ] B. It is a transparent case of one row in a table of five things a system can change.
- [ ] C. Training it modifies Claude's weights.
- [ ] D. It has a learned weight, a learned bias, and a learned learning rate.
- [ ] E. It is a miniature language model in every relevant sense.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The data are constructed, not collected.
- B: It lets you tell the weights row from the other four.
- C: Nothing in the exercise modifies Claude's weights.
- D: The rate is a setting of the experiment; the classifier has two learned parameters.
- E: The chapter says it is not a miniature language model in every relevant sense.

**Source:** Chapter 9 - Training and configuration (opening)

## MA-ch09.5

Check each statement that is true about the two predictions the chapter asks you to write down and date before reading the reference. Each statement is worth 1 point (5 points total).

- [ ] A. One prediction is the initial probability for every point when both parameters are zero.
- [ ] B. The other is the final value of the weight after 200 steps.
- [ ] C. Beside the predictions you also write what a wrong answer would look like.
- [ ] D. The predictions can be skipped if Claude returns plausible decimals.
- [ ] E. A prediction written after you have seen the output still works as a prediction.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Stated in the chapter.
- B: It is the direction the weight should move on the first update.
- C: Stated in the chapter.
- D: A model that returns plausible decimals is no substitute for knowing which direction should reduce the loss.
- E: It then describes the output.

**Source:** Chapter 9 - Training and configuration (opening)

## MA-ch09.6

Check each statement that is true about the five objects a system change can modify. Each statement is worth 1 point (5 points total).

- [ ] A. For settings, what shows the change is both texts side by side.
- [ ] B. A prompt is instruction text and examples in a file or message you can diff.
- [ ] C. For tools, what shows the change is the configuration diff and the decision that authorized it.
- [ ] D. Weights are edited through an objective and an update rule, and the change lives in the saved parameter values.
- [ ] E. Context is which documents, passages, or records are supplied this turn, and what shows the change is the passages that actually entered the input.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: That is the evidence for a prompt; for settings it is the recorded setting for each run.
- B: Second row of the table.
- C: Fourth row of the table.
- D: First row of the table.
- E: Third row of the table.

**Source:** Name the mutable object before you change it

## MA-ch09.7

Check each statement that is true about system prompts and few-shot examples. Each statement is worth 1 point (5 points total).

- [ ] A. Few-shot examples demonstrate a pattern inside the current context.
- [ ] B. If changing a few-shot example changes the answer, the evidence supports prompt-context sensitivity under the recorded interaction.
- [ ] C. If changing a few-shot example changes the answer, the evidence supports the claim that Claude was retrained.
- [ ] D. Revising a system prompt can change behavior dramatically while the stored parameters stay untouched.
- [ ] E. A system prompt is text in the input of an interaction.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: They are input too.
- B: That is the claim the chapter allows.
- C: It supports prompt-context sensitivity, not retraining.
- D: Stated in the chapter.
- E: It is input, not a parameter.

**Source:** Name the mutable object before you change it

## MA-ch09.8

Check each statement that is true about retrieval, MCP servers, and permission rules. Each statement is worth 1 point (5 points total).

- [ ] A. An MCP server changes the actions and information the host exposes.
- [ ] B. Retrieval decides which source passages enter the context.
- [ ] C. In Chapter 7's implementation, adding a document changes the model.
- [ ] D. A permission rule changes which proposed operations the runtime allows.
- [ ] E. A system cannot become more capable through tooling unless the model itself changes.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Chapter 8.
- B: Stated in the chapter.
- C: It changes what inference can see and nothing about the model.
- D: Stated in the chapter.
- E: A system can become more capable through tooling while the model stays exactly as it was.

**Source:** Name the mutable object before you change it

## MA-ch09.9

Check each statement that is true about permission changes and settings. Each statement is worth 1 point (5 points total).

- [ ] A. An MCP server changes the model's parameters so that it can use new actions.
- [ ] B. A permission rule retrains the model so that it stops proposing disallowed operations.
- [ ] C. A tool or permission change leaves the system's capability and governance unchanged.
- [ ] D. Calling a permission change "learning" turns a human governance decision into something that sounds like a property of the machine.
- [ ] E. A setting such as temperature fits the model's parameters to new data.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It changes capability and governance; the model is unchanged.
- B: It changes which proposed operations the runtime allows; the model is untouched.
- C: Both change capability and governance.
- D: That is the chapter's objection.
- E: A setting changes how an output is drawn from scores; it does not fit anything.

**Source:** Name the mutable object before you change it

## MA-ch09.10

Check each statement that is true about how the chapter orders the five objects. Each statement is worth 1 point (5 points total).

- [ ] A. The ordering that helps is by reversibility and inspectability.
- [ ] B. The chapter ranks weights as the best row to change.
- [ ] C. Training can be expensive, unnecessary, or out of reach.
- [ ] D. Prompting and retrieval are often the right tool for task-specific behavior.
- [ ] E. Parameters you can only refit sit at the end that is easiest to reverse.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Stated in the chapter.
- B: None of this ranks the rows.
- C: Stated in the chapter.
- D: Stated in the chapter.
- E: Text you can diff and revert in a second is the easy end.

**Source:** Name the mutable object before you change it

## MA-ch09.11

A configuration file holds several entries, and you are asked what it changed. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. For Claude, interface and configuration details are best taken from the model's own description of itself.
- [ ] B. You should trace the object, not the filename.
- [ ] C. A configuration file can hold several kinds of setting at once.
- [ ] D. Using Claude Code gives you the access needed to claim knowledge of Claude's proprietary weights.
- [ ] E. A file named "config" can be assumed to change only settings.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Take them from current official documentation.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Claim no access to proprietary weights or private training procedures.
- E: Its entries may belong to different rows.

**Source:** Name the mutable object before you change it

## MA-ch09.12

Several non-training changes persist after the interaction that made them. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A saved prompt influences later requests by updating the model's parameters.
- [ ] B. Training is identified by its mechanism, not by later influence.
- [ ] C. A saved system prompt remains in a project without any training having happened.
- [ ] D. A retrieved document remains in a workspace without any training having happened.
- [ ] E. "It stuck" is a valid test for whether the system learned.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: It influences them by being included again as input.
- B: Stated in the chapter.
- C: Persistence is not proof of training.
- D: Same point.
- E: Several non-training changes persist, so it cannot be the test.

**Source:** Persistence is not proof of training

## MA-ch09.13

A product remembers a user's preferences in later sessions. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Without evidence of parameter updates, you describe the memory or context behavior you observed.
- [ ] B. The system may retrieve stored preferences or prepend them to the context.
- [ ] C. You may say the model "learned the user" in the technical sense used here once the preferences persist.
- [ ] D. Remembering preferences across sessions is itself evidence that the model's weights changed.
- [ ] E. Personalization is a different case from saved prompts and retrieved documents.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: That needs evidence of parameter updates.
- D: Persistence is not proof of training.
- E: The chapter says it is the same case.

**Source:** Persistence is not proof of training

## MA-ch09.14

Check each statement that is true about the intervention test that separates training from other changes. Each statement is worth 1 point (5 points total).

- [ ] A. For a Claude interaction, you remove the saved text and run the same input again; if the behavior goes with it, the text was holding it.
- [ ] B. In the toy, setting w and b back to zero removes the learned boundary.
- [ ] C. With sampling in play, you run each condition repeatedly rather than once.
- [ ] D. The test is an intervention on your own system: change one object and hold the rest fixed.
- [ ] E. Asking what correlates with the improvement is the same move as intervening on the system.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated in the chapter.
- B: The learned boundary is gone, whatever else you did.
- C: One run per condition shows little; Chapter 1's repeated runs apply.
- D: Stated in the chapter.
- E: The chapter distinguishes the two.

**Source:** Persistence is not proof of training

## MA-ch09.15

Check each statement that is true about the before-and-after record the chapter asks you to keep. Each statement is worth 1 point (5 points total).

- [ ] A. An observed output difference usually identifies the mechanism uniquely.
- [ ] B. For tools, keep the configuration diff and the authorized decision.
- [ ] C. For a prompt, keep both texts.
- [ ] D. For retrieval, the corpus alone is enough; the selected passages need not be recorded.
- [ ] E. For training, keep the parameter values and the data, objective, rate, and budget that produced them.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Usually it does not.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Keep the corpus and the selected passages.
- E: Stated in the chapter.

**Source:** What a production record can and cannot show

## MA-ch09.16

Check each statement that is true about attributing a change and reproducing a result. Each statement is worth 1 point (5 points total).

- [ ] A. A different answer could come from prompt text, retrieved context, tool output, model version, or sampling conditions.
- [ ] B. If a service exposes only the current model label and a response, you should say which internal details remain unknown.
- [ ] C. Identical output is not the only acceptable repeat.
- [ ] D. Another reader can rerun the Python training from supplied data, replay a prompt under recorded but aging service conditions, or inspect a configuration diff, and each has different dependencies.
- [ ] E. You may reconstruct a plausible before state for the part you cannot see.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is why the surrounding record matters.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Those are the kinds of reproducibility the chapter names.
- E: Do not invent a before state you cannot see.

**Source:** What a production record can and cannot show

## MA-ch09.17

At w = 0 and b = 0, check each statement that is true about the classifier a = wx + b, followed by the sigmoid. Each statement is worth 1 point (5 points total).

- [ ] A. Every score is zero regardless of x.
- [ ] B. Sigmoid zero is one-half, since e^0 = 1.
- [ ] C. The linear score is a = wx + b.
- [ ] D. The initial predictions for the label-one points are higher than for the label-zero points.
- [ ] E. The returned value is interpreted as the probability of label zero.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Both parameters are zero.
- B: 1 / (1 + 1) = 0.5.
- C: Definition.
- D: All four initial predictions are 0.5.
- E: It is read as the probability for label one.

**Source:** The model: two numbers and a squashing function

## MA-ch09.18

Check each statement that is true about the two-branch sigmoid in the reference implementation. Each statement is worth 1 point (5 points total).

- [ ] A. It avoids evaluating an unnecessarily large positive exponential when x is very negative.
- [ ] B. The negative branch rewrites the same mathematical quantity.
- [ ] C. The lesson test checks that sigmoid of negative one thousand is approximately zero without overflow.
- [ ] D. For negative x the two-branch code computes a different function from 1 / (1 + e^(-x)).
- [ ] E. The lesson test of sigmoid(-1000) is a promise about arbitrary types and all floating-point edge cases.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Stated in the chapter.
- B: e / (1 + e) with e = exp(x).
- C: Stated in the chapter.
- D: It is the same quantity written differently.
- E: It is evidence for the demonstrated numeric behavior only.

**Source:** The model: two numbers and a squashing function

## MA-ch09.19

Check each statement that is true about what the weight in this classifier means. Each statement is worth 1 point (5 points total).

- [ ] A. With a positive learned weight and the bias near zero, negative x values produce probabilities below one-half.
- [ ] B. The numerical results in the chapter come from the logistic-regression chapter draft it cites.
- [ ] C. The weight learns a causal relationship between feature sign and label.
- [ ] D. The weight learns a word meaning.
- [ ] E. A positive learned weight makes positive x values produce positive scores and probabilities above one-half.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Stated in the chapter.
- B: The cited source supports the mechanism; the numbers come from the local implementation and an independent calculation.
- C: It fits the relationship represented in the supplied pairs, not a causal one.
- D: It fits the relationship represented in the supplied pairs.
- E: Stated in the chapter.

**Source:** The model: two numbers and a squashing function

## MA-ch09.20

Check each statement that is true about the Change and Objective lines of this chapter's gate. Each statement is worth 1 point (5 points total).

- [ ] A. The Objective is the average binary logistic loss on the four training pairs, and nothing else.
- [ ] B. Claude's own weights are in play in a limited way.
- [ ] C. The prompt, context, tools, and settings are not in play.
- [ ] D. "Better" in this gate means higher accuracy on the held-out pairs.
- [ ] E. The Change is weights only: w and b, starting from zero.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Stated in the gate.
- B: They are not in play at all.
- C: Stated in the gate.
- D: "Better" means lower on this objective on these pairs.
- E: Stated in the gate.

**Source:** The gate: say what should change before you change it

## MA-ch09.21

Check each statement that is true about the Held-out and Stop rule lines of the gate. Each statement is worth 1 point (5 points total).

- [ ] A. You may add extra steps if the held-out result looks bad.
- [ ] B. The held-out pairs are fixed in advance and never passed to train.
- [ ] C. You may stop early if the loss looks flat.
- [ ] D. The stop rule is 200 updates at rate 0.2 starting from the trained parameters.
- [ ] E. The held-out pairs follow a different sign pattern from the training data.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The gate forbids extra steps for that reason.
- B: Stated in the gate.
- C: The gate forbids stopping early because the loss looks flat.
- D: The start is zero.
- E: They share the training data's sign pattern by construction.

**Source:** The gate: say what should change before you change it

## MA-ch09.22

Check each statement that is true about the three wrong versions the gate says your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. Summing the gradient over the examples instead of averaging makes the first step four times too large while the loss still falls.
- [ ] B. If your tests cannot tell these from the right program, the gate is not finished.
- [ ] C. Letting a held-out point into the training list makes the "held-out" result stop meaning anything.
- [ ] D. The summed version is easy to detect because its loss rises on the first step.
- [ ] E. Copying the x factor into the bias update makes b move on the first step although the symmetric data say it should not.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Its loss still falls.
- E: Stated in the chapter.

**Source:** The gate: say what should change before you change it

## MA-ch09.23

Check each statement that is true about the failure sentence and the pass condition. Each statement is worth 1 point (5 points total).

- [ ] A. The gate passes when every test you wrote from it passes on the code and every sentence in your report fits inside the "may claim" line.
- [ ] B. The failure sentence is written and dated before the run.
- [ ] C. If the first update is right, w moves positive and b stays at zero.
- [ ] D. If the first update is right, b moves by 0.15.
- [ ] E. If w moves negative on the first update, the training labels must be wrong.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: That is the pass condition.
- B: Written after you read the output, it describes the output.
- C: Stated in the example.
- D: The bias stays at zero on the first step.
- E: The chapter says a sign or an x factor is wrong.

**Source:** The gate: say what should change before you change it

## MA-ch09.24

Check each statement that this experiment may claim, according to the chapter's "may claim" line. Each statement is worth 1 point (5 points total).

- [ ] A. Increasing x causes label one.
- [ ] B. The probabilities are calibrated.
- [ ] C. The classifier generalizes.
- [ ] D. The run changed Claude.
- [ ] E. Four constructed points were classified correctly.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: It may not claim any cause.
- B: It may not claim calibration.
- C: The experiment may not claim generalization.
- D: It may not claim a change to Claude.
- E: That is one of the three permitted claims.

**Source:** The gate: say what should change before you change it

## MA-ch09.25

Check each statement that is true about why the gate's lines cannot be delegated. Each statement is worth 1 point (5 points total).

- [ ] A. For a real change request, the objective can be left implicit until after the run.
- [ ] B. Claude can choose the objective for you without changing whose objective the report states.
- [ ] C. For the toy, a model produced the gate's lines.
- [ ] D. None of the gate's lines can be derived from the data, because the data have no opinion about what "better" should mean.
- [ ] E. Claude cannot help with the gate at all.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The objective, held-out set, and stop rule are the items most often left implicit, and they must be written first.
- B: Then your report would be a statement about someone else's objective.
- C: They are the author's choices; no model produced them.
- D: Stated in the chapter.
- E: Claude can sharpen the gate by proposing the wrong version and the test that catches it.

**Source:** The gate: say what should change before you change it

## MA-ch09.26

Check each statement that is true about the loss used in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The stable form is a different objective from the ordinary logistic one.
- [ ] B. The reference averages the loss across the data.
- [ ] C. The reference evaluates an equivalent stable expression from the score a: max(a, 0) - y*a + log(1 + e^(-|a|)).
- [ ] D. The stable form avoids computing logarithms of probabilities rounded too close to zero or one for large scores.
- [ ] E. The ordinary binary cross-entropy for probability p is -y log(p) - (1 - y) log(1 - p).

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It is a numerically safer route to the same objective.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: That is why it is safer numerically.
- E: Stated in the chapter.

**Source:** Loss makes the objective explicit

## MA-ch09.27

Check each statement that is true about the initial loss and the history list. Each statement is worth 1 point (5 points total).

- [ ] A. The history list records the loss at every step.
- [ ] B. At the origin the average loss equals negative log one-half, because all four examples share the same prediction.
- [ ] C. Two recorded values are not a learning curve.
- [ ] D. Called directly on an empty list, the loss function returns zero.
- [ ] E. At the origin the loss for either label is negative log one-half, about 0.6931471806.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It appends only the initial and the final loss.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: It would divide by zero; training validates nonempty data before calling it.
- E: Prediction is 0.5 for every point.

**Source:** Loss makes the objective explicit

## MA-ch09.28

Check each statement that is true about the gradient at the origin for the data [(-2, 0), (-1, 0), (1, 1), (2, 1)]. Each statement is worth 1 point (5 points total).

- [ ] A. For logistic loss, the derivative with respect to the score for one example is prediction minus label.
- [ ] B. The contribution to the weight gradient is e times x, where e is prediction minus label.
- [ ] C. The average bias gradient is -0.75.
- [ ] D. With rate 0.2 the new weight is 0 - 0.2(-0.75) = 0.15.
- [ ] E. The four weight contributions are -1.0, -0.5, -0.5, -1.0, which sum to -3 and average to -0.75.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: The errors sum to zero, so the average bias gradient is zero.
- D: Gradient descent subtracts rate times gradient.
- E: -3 / 4 = -0.75.

**Source:** Derive the first update

## MA-ch09.29

Check each statement that is true about checking the gradient by finite difference. Each statement is worth 1 point (5 points total).

- [ ] A. The result at zero is approximately -0.74999999999.
- [ ] B. A central finite difference evaluates the loss at a small positive and a small negative perturbation and divides the difference by twice the perturbation.
- [ ] C. The finite-difference check is an independent dataset.
- [ ] D. The finite-difference check fails differently from the derivation, because it never uses the derivative formula.
- [ ] E. If logistic loss is the wrong objective for your task, the finite difference will disagree with the derivative.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It agrees with the analytic -0.75.
- B: Stated in the chapter.
- C: It is an independent calculation, not an independent dataset.
- D: Stated in the chapter.
- E: Both describe the objective you wrote, so they still agree.

**Source:** Derive the first update

## MA-ch09.30

Check each statement that is true about what the independent gradient check (the finite difference) covers. Each statement is worth 1 point (5 points total).

- [ ] A. The check is an independent reviewer of whether the objective is right.
- [ ] B. A passing finite-difference check shows the optimizer will behave under every dataset.
- [ ] C. The check compares the gradient with the loss function, and nothing more.
- [ ] D. Agreement confirms that logistic loss is the objective you meant.
- [ ] E. The check is an independent calculation.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It is not an independent reviewer or causal source.
- B: It checks one gradient at one point.
- C: Stated in the chapter.
- D: Whether it is the objective you meant is the gate's question.
- E: Stated in the chapter.

**Source:** Derive the first update

## MA-ch09.31

Check each statement that is true about the training function and its loop. Each statement is worth 1 point (5 points total).

- [ ] A. It is batch gradient descent on the complete declared dataset, without minibatches or an adaptive rate.
- [ ] B. Each step builds errors from the current parameters, averages the gradient contributions, and updates weight and bias.
- [ ] C. It shuffles the examples each step.
- [ ] D. Labels must be zero or one and features must be finite.
- [ ] E. It returns the parameters plus a two-value loss list.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: It does not shuffle.
- D: Stated in the validation description.
- E: Stated in the chapter.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.32

After 200 steps at rate 0.2, check each statement that is true about the recorded run. Each statement is worth 1 point (5 points total).

- [ ] A. The bias is substantially nonzero.
- [ ] B. The training loss after 200 steps is about 0.5877.
- [ ] C. The weight is approximately 3.1669517461.
- [ ] D. Passing the existing lesson tests shows the optimizer would behave well under every dataset or rate.
- [ ] E. The existing tests check held-out accuracy.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The bias is effectively zero.
- B: That is the average loss after the first step; after 200 steps it is 0.0215209850.
- C: Stated in the chapter.
- D: They do not show that.
- E: They check that the loss fell and that the weight is positive.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.33

Check each statement that is true about the learning rate in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. A very large rate can overshoot or become unstable on some data.
- [ ] B. The first step, 0.15, does not arise from the data alone; it is the average gradient -0.75 scaled by a rate you chose.
- [ ] C. The research establishes a safe universal range for the rate.
- [ ] D. The rate is a learned parameter.
- [ ] E. A different positive rate would take a different step.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: It establishes no safe universal range.
- D: It is a setting of the experiment, never updated by train.
- E: Stated in the chapter.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.34

Check each statement that is true about the step count and about comparing runs. Each statement is worth 1 point (5 points total).

- [ ] A. The training function stops when it detects convergence.
- [ ] B. A lower final training loss shows the step budget was right.
- [ ] C. When comparing rates or step counts you should hold the data and initial parameters fixed.
- [ ] D. It is acceptable to report only the best run, if you label it as the result.
- [ ] E. Two hundred is the demo setting, not a discovered natural stopping point.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It has no convergence test, early stopping, or best-checkpoint selection.
- B: It shows what happened after the configured loop only.
- C: Stated in the chapter.
- D: Keep every result, including runs that behave badly; otherwise the comparison becomes a search.
- E: Stated in the chapter.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.35

Check each statement that is true about the two practice cases of reversing labels and duplicating evaluation points. Each statement is worth 1 point (5 points total).

- [ ] A. Duplicating the evaluation points into the training data contaminates the separation between fit and held-out assessment.
- [ ] B. If you reverse the labels, the preferred weight direction should reverse.
- [ ] C. The practice cases are designed so that memorizing the published positive weight is enough to pass them.
- [ ] D. If you reverse the labels, the preferred weight direction should stay positive.
- [ ] E. After duplication, apparent improvement on those points is easy to interpret.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: They test whether you understand the relationship rather than memorized it.
- D: It should reverse.
- E: It becomes hard to interpret, because the optimizer has already used them.

**Source:** The loop, its rate, and its stop rule

## MA-ch09.36

Check each statement that is true about the held-out evaluation of the trained parameters. Each statement is worth 1 point (5 points total).

- [ ] A. Thresholding at one-half predicts all four labels correctly.
- [ ] B. Being held out makes the points representative of a natural population.
- [ ] C. "Held out" is a statement about how the points were handled.
- [ ] D. For the held-out points x = -3, -0.5, 0.5, and 3, the predicted probabilities are approximately 0.00007478, 0.17030378, 0.82969622, and 0.99992522.
- [ ] E. The demo function returns a held-out evaluation.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Stated in the chapter.
- B: They were designed around the same sign boundary as the training examples.
- C: They were not passed into the training function.
- D: Stated in the chapter, for x = -3, -0.5, 0.5, 3.
- E: It returns training parameters and initial and final training loss.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.37

Check each statement that is true about what four correct held-out labels support. Each statement is worth 1 point (5 points total).

- [ ] A. Designing the held-out points around the same sign boundary makes them a harder test than the training data.
- [ ] B. They support the claim that the model generalized.
- [ ] C. A broader performance claim needs a justified sampling process, a task definition, and a larger evaluation.
- [ ] D. They establish performance on a natural population.
- [ ] E. They support the claim that the trained parameters classified four separately specified sign-pattern fixtures correctly.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It means they cannot support more than the narrow claim.
- B: That is too broad.
- C: Stated in the chapter.
- D: They establish behavior on these four constructed points only.
- E: That matches the evidence.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.38

Check each statement that is true about the lifespan of a held-out set. Each statement is worth 1 point (5 points total).

- [ ] A. The change of role should be recorded when it happens.
- [ ] B. The toy has two roles, training and held-out.
- [ ] C. Once a held-out set has guided a choice, its next use is no longer independent.
- [ ] D. Once you tune anything, two roles are still enough.
- [ ] E. Once a held-out set guides a choice, such as a rate, a step count, or a decision to keep going, it has become development data.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: You then need training, a development set, and a held-out set you touch once.
- E: Stated in the chapter.

**Source:** Held-out means separately specified, not magically representative

## MA-ch09.39

Check each statement that is true about what lower training loss claims. Each statement is worth 1 point (5 points total).

- [ ] A. Lower training loss establishes that the model is better.
- [ ] B. Lower training loss establishes that the update rule reduced the objective on the pairs it was shown.
- [ ] C. Lower training loss does not establish that the objective was the right one.
- [ ] D. Lower training loss establishes that the probabilities are calibrated.
- [ ] E. Lower training loss does not establish fit to pairs it was not shown.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: "Better" is a claim about the task, and the task is not in the loss.
- B: Stated in the chapter.
- C: No dataset can establish that for you.
- D: Calibration needs a separate study.
- E: That is what the held-out set is for.

**Source:** What a lower loss claims

## MA-ch09.40

Suppose label one means "escalate this message to a person," and a missed escalation is far worse than a false alarm. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The loss already weights a missed escalation more heavily because it is worse.
- [ ] B. Binary logistic loss penalizes each error by how confident the model was in the wrong direction.
- [ ] C. You should write "training loss decreased" when that is what you measured.
- [ ] D. A lower loss can sit comfortably beside the wrong behavior.
- [ ] E. The missing measure is one the gate should have named: the costs of the two errors.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It penalizes by confidence, not by what each error costs you.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Stated in the chapter.
- E: Stated in the chapter.

**Source:** What a lower loss claims

## MA-ch09.41

Check each statement that is true about score, probability, and decision. Each statement is worth 1 point (5 points total).

- [ ] A. The score wx + b comes from the parameters.
- [ ] B. The decision comes from a threshold, here one-half, which you chose.
- [ ] C. Moving the threshold moves the decisions while the parameters stay identical.
- [ ] D. The probability comes from the sigmoid.
- [ ] E. Training chose the threshold.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Stated in the chapter.
- E: Training never saw the threshold.

**Source:** Score, probability, and decision are three layers

## MA-ch09.42

Check each statement that is true about the symmetry of the constructed data and the bias. Each statement is worth 1 point (5 points total).

- [ ] A. The near-zero learned bias shows that bias is unnecessary.
- [ ] B. Each negative feature with label zero has a positive partner with label one.
- [ ] C. Bias shifts the decision boundary whenever the relationship is not centered at zero.
- [ ] D. The decision boundary sits where wx + b = 0, because sigmoid zero is one-half.
- [ ] E. At the origin the errors sum to zero, so the first bias update is zero.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The chapter warns against that conclusion.
- B: That is the symmetry.
- C: Stated in the chapter.
- D: Stated in the chapter.
- E: Stated in the chapter.

**Source:** Score, probability, and decision are three layers

## MA-ch09.43

Check each statement that is true about the held-out probabilities and calibration. Each statement is worth 1 point (5 points total).

- [ ] A. Held-out values farther from zero get more extreme probabilities under the learned positive weight.
- [ ] B. Whether a probability matches observed frequencies takes a calibration study on suitable labeled data.
- [ ] C. Probabilities growing more extreme away from zero is an observed property of this fitted curve on selected points.
- [ ] D. Probabilities growing more extreme away from zero is evidence that the confidence is calibrated.
- [ ] E. Four sign fixtures can support a calibration claim.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Compare x = 3 (0.99992522) with x = 0.5 (0.82969622).
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: It is not evidence of calibration.
- E: They cannot.

**Source:** Score, probability, and decision are three layers

## MA-ch09.44

Suppose x counts the reminder emails a student opened in the first month, y records whether they passed, and a fitted weight is positive. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. "For a student who opened four emails, what label will the model assign?" is answered by evaluating the fitted function.
- [ ] B. The number at a larger x is the model's response to a changed input.
- [ ] C. Answering the first question requires a causal study.
- [ ] D. Evaluating the function at a larger x gives the course's response to a changed behavior.
- [ ] E. "If we require every student to open the emails, will more of them pass?" asks about the world, so the function answers a different question.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: That asks about the model.
- B: Stated in the chapter.
- C: It requires only evaluating the function.
- D: It gives the model's response to a changed input.
- E: Stated in the chapter.

**Source:** Decide what kind of question you are asking

## MA-ch09.45

In the same email hypothetical, check each statement that is true about possible sources of a positive weight. Each statement is worth 1 point (5 points total).

- [ ] A. The positive weight tells you which of the possible sources of the association is the true one.
- [ ] B. A third factor, such as motivation or free time, might raise both opening and passing.
- [ ] C. Students who are already on track might open more emails, so the arrow runs the other way.
- [ ] D. The sample might contain only students who stayed enrolled.
- [ ] E. Opening the emails might help students pass.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Each is consistent with a positive weight, so the weight cannot tell you.
- B: A possible source.
- C: A possible source.
- D: A possible source.
- E: A possible source.

**Source:** Decide what kind of question you are asking

## MA-ch09.46

Check each statement that is true about acting on predictions and about the four constructed pairs. Each statement is worth 1 point (5 points total).

- [ ] A. The four constructed pairs contain information about a real process.
- [ ] B. A model fit to a period in which nobody acted on its flags can say little about what happens once people do.
- [ ] C. Acting on a prediction can change the process that generated the data.
- [ ] D. A causal sentence about the four pairs is a finding.
- [ ] E. The four pairs were collected from a real course.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: They contain no information about any process in the world.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: It is a story attached to a fixture.
- E: They are constructed and are not a study.

**Source:** Decide what kind of question you are asking

## MA-ch09.47

Check each statement that is true about Judea Pearl's ladder as the chapter uses it. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter treats the limit as a proof that no machine architecture could ever reason causally.
- [ ] B. The chapter claims observational data can never support a causal claim.
- [ ] C. Intervention asks what happens if I do this.
- [ ] D. Counterfactual asks what would have happened to this case had we done otherwise.
- [ ] E. Association asks what goes with what.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The limit is about information, and the book warns against the stronger claim.
- B: It can, under assumptions you state and defend.
- C: Second rung.
- D: Third rung.
- E: First rung.

**Source:** Decide what kind of question you are asking

## MA-ch09.48

Check each statement that is true about "prediction is not identification" in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Someone must supply and defend the causal assumptions.
- [ ] B. A model's fluent explanation can supply the causal assumptions.
- [ ] C. Interventional and counterfactual answers generally cannot be recovered from purely observational data without structural assumptions that did not come from the data.
- [ ] D. Observational data can support a causal claim under assumptions you state and defend.
- [ ] E. More data supplies the causal assumptions.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Stated in the chapter.
- B: Neither a confident intuition nor a fluent explanation does.
- C: Stated in the chapter.
- D: Stated in the chapter.
- E: More data does not supply them.

**Source:** Decide what kind of question you are asking

## MA-ch09.49

Check each statement that is true about the division of labor in the causal part of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can list the confounders it can think of for a given setup.
- [ ] B. Claude can work out what follows if you assume a stated structure.
- [ ] C. Claude can write the notation for a causal diagram.
- [ ] D. Claude has your study design, how the data were collected, and the domain facts about your students.
- [ ] E. The identification judgment stays with the person who will act.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: It does not have those.
- E: Stated in the chapter.

**Source:** What is Claude's here, and what is yours

## MA-ch09.50

Check each statement that is true about Claude's writing on causation and about deciding whether a question is causal. Each statement is worth 1 point (5 points total).

- [ ] A. Claude writes fluent paragraphs about confounding because text about confounding is abundant in what such systems learn from.
- [ ] B. Before you hand Claude the algebra, you write one sentence saying whether the question is "what will the model say" or "what happens if we act," and who decided.
- [ ] C. Fluency about causation is identification of it.
- [ ] D. Deciding whether a question is causal at all is a clerical step with no causal judgment in it.
- [ ] E. Claude has nothing riding on the decision.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated as the working rule.
- C: It is not.
- D: The book's observation is that this decision is itself a causal judgment.
- E: Stated in the chapter.

**Source:** What is Claude's here, and what is yours

## MA-ch09.51

Check each statement that is true about the Build It stage. Each statement is worth 1 point (5 points total).

- [ ] A. If your value differs from 0.15, you adjust the expected result to match your code.
- [ ] B. If your first-step weight differs from 0.15, you inspect averaging, signs, and use of the current parameters.
- [ ] C. You read the six lesson tests after the reference implementation.
- [ ] D. The expected result came from your hand derivation, which is the independent route.
- [ ] E. You implement one gradient step before writing the full loop.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Do not adjust the expected result until the discrepancy is explained.
- B: Stated in the chapter.
- C: You read them before the reference.
- D: Stated in the chapter.
- E: Stated in the chapter.

**Source:** Build It: the baseline that lets you audit

## MA-ch09.52

Check each statement that is true about the summed-gradient wrong version in Build It. Each statement is worth 1 point (5 points total).

- [ ] A. Tests 03 and 04 check only that the loss fell and that the weight is positive.
- [ ] B. Tests 03 and 04 can tell the summed version from the averaged one.
- [ ] C. If the summed version ends at a lower loss at step 200, that shows the code is right.
- [ ] D. Before running it, you predict which of the six lesson tests will fail.
- [ ] E. Its first step is four times as large as the reference's.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Stated in the chapter.
- B: The chapter asks what they can distinguish, because both versions have a falling loss and a positive weight.
- C: The chapter asks what a lower number can tell you about whether the code is right.
- D: One of the three predictions.
- E: 0.6 instead of 0.15.

**Source:** Build It: the baseline that lets you audit

## MA-ch09.53

Check each statement that is true about conducting Claude Code against your gate. Each statement is worth 1 point (5 points total).

- [ ] A. You give Claude Code the gate (change, objective, held-out list, stop rule, and test list) but not your implementation.
- [ ] B. You run your own tests on what Claude returns.
- [ ] C. If Claude adds early stopping you never asked for, that shows your stop rule had no hole.
- [ ] D. Whether your tests are enough can be judged by the system they are testing.
- [ ] E. A failing test is often a gap in your gate that Claude could not see, because it had only what you wrote.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: It shows your stop rule had a hole.
- D: It cannot.
- E: Stated in the chapter.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch09.54

Check each statement that is true about the three things to do with Claude Code's result and the transcript. Each statement is worth 1 point (5 points total).

- [ ] A. You ask Claude to propose a deliberately wrong version that still passes your tests, and check by hand whether it does.
- [ ] B. If a session failed or did not run, you may substitute a fixture for it.
- [ ] C. If the deliberately wrong version passes your tests, your test list was strong enough.
- [ ] D. You need preserve only the final code, not the prompt, plan, or commands.
- [ ] E. You compare its implementation with your baseline and name one difference in behavior.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Record that it failed or did not run.
- C: Then your test list was too weak.
- D: Preserve the prompt, plan, diff, commands, and outputs, with the date and displayed model label.
- E: Stated in the chapter.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch09.55

Check each statement that is true about the second task, which touches Claude's behavior. Each statement is worth 1 point (5 points total).

- [ ] A. You write your prediction for each condition first.
- [ ] B. If you do not run the conditions, you label the design proposed.
- [ ] C. You change only one object between conditions.
- [ ] D. These conditions change Claude's weights.
- [ ] E. You prepare a baseline prompt, a few-shot prompt, and a retrieved-context condition on the same bounded task.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Stated in the chapter.
- B: Stated in the chapter.
- C: That is the one-object-at-a-time test.
- D: They change inputs, not Claude's weights.
- E: Stated in the chapter.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch09.56

Check each statement that is true about what the Ship It report contains. Each statement is worth 1 point (5 points total).

- [ ] A. Its table has mutable object, mechanism, persistence, evidence, and remaining limits, keeping permissions and tools separate from model parameters.
- [ ] B. It may report the loss history as a full learning curve.
- [ ] C. It ends with two predictive claims supported by the toy evaluation.
- [ ] D. It says which results came from the lesson and which from your extension.
- [ ] E. It records the interpreter, step count, rate, initial values, final values, and threshold.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Stated in the chapter.
- B: The demo records two values, initial and final.
- C: It ends with one predictive claim and one intervention claim the evaluation does not establish.
- D: Stated in the chapter.
- E: Stated in the chapter.

**Source:** Ship It: the comparison report and its sign-off

## MA-ch09.57

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. A pass names the obligation it passed, and no more.
- [ ] B. The "Not claiming" line includes that lower training loss means better.
- [ ] C. The template is a signature you can sign as written.
- [ ] D. The "Not checked" line is the one an AI-written sign-off omits, because the system that wrote it has no record of what you did not do.
- [ ] E. If your evidence does not support signing, you must sign anyway and add caveats.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Stated in the chapter.
- B: It is in the template.
- C: It is a template, not a signature.
- D: Stated in the chapter.
- E: Withholding is an honest result.

**Source:** Ship It: the comparison report and its sign-off

## MA-ch09.58

Check each statement that is true about choosing verbs for the claim in the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. "Causes" is supported once the held-out points are classified correctly.
- [ ] B. "Better" is acceptable whenever training loss decreased.
- [ ] C. "Lowered the objective on four pairs" describes what the optimizer did.
- [ ] D. "Learned" overclaims here, because the parameters changed only by hand.
- [ ] E. "Generalizes" needs a criterion you have not run.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It needs assumptions the fixture cannot supply.
- B: Write "training loss decreased" when that is all you measured.
- C: Stated in the chapter.
- D: "Learned" describes a parameter change, and that is accurate here.
- E: Stated in the chapter.

**Source:** Ship It: the comparison report and its sign-off

## MA-ch09.59

Check each statement that is true about the driver's seat table. Each statement is worth 1 point (5 points total).

- [ ] A. For the objective, held-out set, and stop rule, you write them first and Claude challenges them.
- [ ] B. For prediction or intervention, Claude decides which kind of question it is.
- [ ] C. For which object changed, you choose the object you may change and run the one-at-a-time test.
- [ ] D. For what the result supports, Claude chooses the verb and signs.
- [ ] E. For the derivation and the loop, Claude derives, writes, and runs, while you reproduce the first step by hand and by finite difference.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Second row.
- B: You decide, justify the assumptions, and get domain evidence.
- C: Third row.
- D: You choose the verb and sign; your name is on the claim.
- E: First row.

**Source:** The driver's seat

## MA-ch09.60

Four proposed changes are a rewritten system prompt, a new document in a workspace, a newly enabled tool, and a lowered temperature. Check each statement that is true according to the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The lowered temperature modifies the weights.
- [ ] B. The newly enabled tool modifies the tools.
- [ ] C. The rewritten system prompt modifies the prompt.
- [ ] D. If the only evidence is a different output, you may claim changed weights.
- [ ] E. The new document in the workspace modifies the context.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It modifies a run-time setting.
- B: Evidence is the configuration diff and the authorizing decision.
- C: Both texts side by side show it.
- D: Do not jump to a claim about changed weights.
- E: Evidence is the passages that entered the input.

**Source:** Verify and reflect

## MA-ch09.61

Check each statement that is true about the checks the chapter asks you to run when you verify your work. Each statement is worth 1 point (5 points total).

- [ ] A. Four designed points count as evidence of population performance.
- [ ] B. You recompute the first update independently.
- [ ] C. You preserve exact outputs rather than reconstructing them after reading the expected values.
- [ ] D. You check every use of the words "history" and "generalization."
- [ ] E. You narrow the claim if the data and design cannot support it.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: They are separate fixtures.
- B: Stated in the chapter.
- C: Stated in the chapter.
- D: Stated in the chapter.
- E: Stated in the chapter.

**Source:** Verify and reflect

## MA-ch09.62

Check each statement that is true about the ungraded Assessments at the end of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. In the one-update Assessment you also write the version that sums instead of averaging and name the lesson tests that cannot tell the two apart.
- [ ] B. In the prediction-versus-intervention Assessment you must prove the causal claim.
- [ ] C. In the finite-difference Assessment you claim the check would catch a wrong objective.
- [ ] D. You write predictions before execution.
- [ ] E. The Assessments carry no points.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Assessment 4.
- B: You write one supported predictive claim and one unsupported causal claim, and name the assumptions the latter needs.
- C: You state one thing the check would not catch.
- D: Stated in the Assessments.
- E: They are ungraded practice.

**Source:** Assessments - ungraded practice

## MA-ch09.63

Check each statement that is true about what you can now explain at the end of the chapter. Each statement is worth 1 point (5 points total).

- [ ] A. You can reproduce the first-step values by two routes, the derivative and a finite difference.
- [ ] B. You drove by handing Claude the question of whether the problem was one of prediction or intervention.
- [ ] C. Behavioral change alone is enough to identify the mechanism.
- [ ] D. You conducted by asking Claude to write the gate for you.
- [ ] E. Evaluation data stay held out even after they guide a choice.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Stated in the chapter.
- B: You kept that question.
- C: It does not identify the mechanism.
- D: You wrote the change, objective, held-out list, and stop rule before the loop ran.
- E: Once they guide a choice they stop being held out.

**Source:** What you can now explain

## MA-ch09.64

Check each statement that is true about the Irreducibly Human note on AI and human responsibilities. Each statement is worth 1 point (5 points total).

- [ ] A. Humans should hand the decision to act to the AI once its explanation is fluent.
- [ ] B. Human intuition is sufficient causal proof.
- [ ] C. The chapter uses the companion passage to claim no machine architecture can represent causal reasoning.
- [ ] D. AI should inspect calculations, run bounded experiments, tabulate predictions, and challenge assumptions.
- [ ] E. AI can compute consequences under an explicitly stated model and propose candidate confounders.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Humans own the decision to act.
- B: Human intuition is not sufficient causal proof either.
- C: It uses the information boundary, not that claim.
- D: Stated in the chapter.
- E: Stated in the chapter.

**Source:** Irreducibly Human

## MA-ch09.65

The chapter ends by asking you to state your intervention claim with provisos. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If you can fill in P, Q, and R, you have found the assumptions to defend and the evidence to go and get.
- [ ] B. Changing x in the fitted Python function measures the effect of changing the real-world variable.
- [ ] C. You point to the transcript line or edit showing that you, not Claude, wrote the sentence naming the assumptions.
- [ ] D. If you cannot fill in P, Q, and R, you still have a supported causal claim.
- [ ] E. The form is "if I change x by doing D, the outcome changes by about this much, provided P, Q, and R."

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Stated in the chapter.
- B: It measures the model's response, not necessarily the real-world effect.
- C: Stated in the chapter.
- D: Then you have a prediction.
- E: Stated in the chapter.

**Source:** Irreducibly Human
