# Chapter 9: Training and configuration

## ES-ch09.1

A teammate writes up an improved answer as "we trained Claude on our policies" after uploading documents and revising a system prompt. In a paragraph, say what actually changed, what the verb "trained" claims, and why that claim matters for what you maintain, audit, and pay for.

**Points:** 5

**Rubric (1 point each):**

1. States that what changed is the input available during that interaction (the uploaded documents and the revised prompt).
2. States that training changes parameters through an objective and an update rule.
3. Says a prompt change lives in a text file you can diff and copy, while a retrieval change lives in a corpus and a selection step and disappears when the corpus does.
4. States that prompting and retrieval change the information supplied to an already configured model for inference, not its parameters.
5. Explains that the verb decides what happens next: one word hides three different things to maintain, audit, and pay for.

**Source:** Chapter 9 - Training and configuration (opening)

## ES-ch09.2

A report says: "Average loss fell from 0.6931471806 to 0.0215209850 and the four held-out points were all right, so the model learned and it generalizes." Which half of the conclusion does the evidence support, and which half does it not? Justify both.

**Points:** 5

**Rubric (1 point each):**

1. Accepts that "learned" is supported, because the parameters changed by a rule you can print.
2. Rejects "generalizes" as unsupported by this evidence.
3. Explains that the loss is the number the optimizer was told to lower, on the data it was shown.
4. Notes that the four held-out points were chosen by one person around the same sign boundary as the training data.
5. Concludes that neither number says what the sentence says it does, and that no line of code is at fault.

**Source:** Chapter 9 - Training and configuration (opening)

## ES-ch09.3

Name Chapter 1's three jobs and say how each applies to a change request in this chapter. For each, say what you do and what the chapter calls the moment or place where it happens.

**Points:** 5

**Rubric (1 point each):**

1. Conduct: states what should change, and how you will tell, before you change it.
2. Identifies that Conduct moment as the gate.
3. Check: claims only what the record supports, and signs or withholds.
4. Identifies that Check moment as the sign-off.
5. Drive: decides what kind of question is being answered, because the causal question and its justification are yours (the driver's seat).

**Source:** Chapter 9 - Training and configuration (opening)

## ES-ch09.4

Describe the classifier built in this chapter in two or three sentences, then state three things the chapter says the exercise does not do or is not.

**Points:** 5

**Rubric (1 point each):**

1. Describes a one-feature binary logistic classifier with two learned parameters, a weight and a bias.
2. Mentions the four constructed training examples, the sigmoid, the binary logistic loss, and gradient descent.
3. States that nothing in the exercise modifies Claude's weights.
4. States that nothing in the exercise exposes Claude's logits, optimizer, or training data.
5. States that it is not a miniature language model in every relevant sense and not a fine-tune of anything, but a transparent case of one row in a table of five.

**Source:** Chapter 9 - Training and configuration (opening)

## ES-ch09.5

The chapter asks you to write and date two predictions before reading the reference. State the two predictions, with the correct answer for this toy, and explain why the timing matters.

**Points:** 5

**Rubric (1 point each):**

1. The initial probability for every point when both parameters are zero is one-half.
2. The weight should move in the positive direction on the first update, reasoned from the labels and the signs of the features.
3. Adds that you also write what a wrong answer would look like.
4. Explains that a prediction written after you have seen the output describes the output.
5. Says a model that returns plausible decimals is no substitute for knowing which direction should reduce the loss.

**Source:** Chapter 9 - Training and configuration (opening)

## ES-ch09.6

Name the five objects a system change can modify. For each, say what you edit and where the change lives.

**Points:** 5

**Rubric (1 point each):**

1. Weights: parameters edited through an objective and an update rule, living in the saved parameter values.
2. Prompt: instruction text and examples, living in a file or message you can diff.
3. Context: which documents, passages, or records are supplied this turn, living in the corpus or store and the selection step.
4. Tools: which actions and information sources the host exposes and which are permitted, living in server code, configuration, and permission rules.
5. Settings: how outputs are drawn at run time (temperature is the example), living in run-time configuration.

**Source:** Name the mutable object before you change it

## ES-ch09.7

Which of the five rows involves an optimizer, and what can someone outside the people who train Claude observe about it? Given that limit, why does the chapter build a toy classifier?

**Points:** 5

**Rubric (1 point each):**

1. States that only the weights row involves an optimizer.
2. States that for Claude nobody outside the people who train it can watch that row change.
3. Notes that the course does not claim otherwise.
4. Explains that the toy lets you watch the weights row change once, completely.
5. Explains that this lets you recognize the other four rows by contrast, without leaning on metaphor.

**Source:** Name the mutable object before you change it

## ES-ch09.8

A colleague rewrites a system prompt and Claude's behavior changes dramatically. Another colleague changes one few-shot example and the answer changes. For each, say what the evidence supports and what it does not.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the system prompt as text in the input of an interaction.
2. States that behavior can change dramatically while the stored parameters stay untouched.
3. Identifies few-shot examples as input that demonstrates a pattern inside the current context.
4. Says the few-shot result supports prompt-context sensitivity under the recorded interaction.
5. Says neither result supports a claim that Claude was retrained.

**Source:** Name the mutable object before you change it

## ES-ch09.9

Explain what retrieval, an MCP server, and a permission rule each change, and say why calling a permission change "learning" is a problem.

**Points:** 5

**Rubric (1 point each):**

1. Retrieval decides which source passages enter the context; adding a document changes what inference can see and nothing about the model.
2. An MCP server changes the actions and information the host exposes.
3. A permission rule changes which proposed operations the runtime allows.
4. Both change capability and governance: a system can become more capable through tooling while the model stays exactly as it was.
5. Calling a permission change "learning" turns a human governance decision into something that sounds like a property of the machine.

**Source:** Name the mutable object before you change it

## ES-ch09.10

Does the chapter rank the five objects? If not, say what ordering it calls useful, and give two statements it makes about when training is or is not the right tool.

**Points:** 5

**Rubric (1 point each):**

1. States that the chapter does not rank the rows.
2. States that prompting and retrieval are often the right tool for task-specific behavior.
3. States that training can be expensive, unnecessary, or out of reach.
4. Names the useful ordering as reversibility and inspectability.
5. Places text you can diff and revert in a second at one end and parameters you can only refit at the other.

**Source:** Name the mutable object before you change it

## ES-ch09.11

A single configuration file contains a temperature value and a permission rule for a tool. What does "trace the object, not the filename" mean here, and where should details about Claude's interface and configuration come from?

**Points:** 5

**Rubric (1 point each):**

1. States that a configuration file can hold several kinds of setting at once.
2. Classifies the temperature value as a setting (run-time configuration of how outputs are drawn).
3. Classifies the permission rule as belonging to the tools row (what is permitted).
4. Concludes that the filename does not tell you which object changed, so you trace the object.
5. Says Claude interface and configuration details come from current official documentation, and that you claim no access to proprietary weights or private training procedures.

**Source:** Name the mutable object before you change it

## ES-ch09.12

A saved system prompt, a retrieved document, a permission rule, and a memory record all persist after the interaction that made them. Why can't "it stuck" be the test for learning, and what does identify training?

**Points:** 5

**Rubric (1 point each):**

1. Names at least three of the four persistent non-training changes.
2. Says "it stuck" cannot be the test, because several non-training changes persist.
3. States that training is identified by its mechanism, not by later influence.
4. Gives the toy as direct implementation evidence: train returns w and b after using labels and a loss-derived gradient.
5. Explains that a saved prompt influences later requests by being included again as input, so both have durable effects through different routes in the software.

**Source:** Persistence is not proof of training

## ES-ch09.13

A product remembers a user's preferences from one session to the next. How should you describe this behavior, and what would you need before saying the model "learned the user"?

**Points:** 5

**Rubric (1 point each):**

1. Says the system may retrieve stored preferences or prepend them to the context.
2. Says that without evidence of parameter updates you describe the memory or context behavior you observed.
3. Says "learned the user" in the technical sense used here requires evidence of parameter updates.
4. Identifies personalization as the same case as saved prompts and retrieved documents: persistence is not proof of training.
5. Proposes a test: remove the stored preferences, hold the rest fixed, rerun the same input, and see whether the behavior goes with them.

**Source:** Persistence is not proof of training

## ES-ch09.14

Design the test that shows whether a saved piece of text, rather than anything else, is responsible for a Claude behavior. Say what you change, what you hold fixed, how many runs you use and why, and how this differs from asking what correlates with the improvement.

**Points:** 5

**Rubric (1 point each):**

1. Changes one object (removes the saved text) and holds the rest fixed.
2. Runs the same input again.
3. States that if the behavior goes with the text, the text was holding it.
4. Explains that with sampling in play one run per condition shows little, so repeated runs (Chapter 1) apply.
5. Explains this is an intervention (doing something to the system and watching what follows), not a question about what correlates with the improvement.

**Source:** Persistence is not proof of training

## ES-ch09.15

For each change you make, you keep a before and an after. Say what to keep for training, a prompt, retrieval, and tools, and explain why an observed output difference alone does not identify the mechanism.

**Points:** 5

**Rubric (1 point each):**

1. Training: the parameter values and the data, objective, rate, and budget that produced them.
2. Prompt: both texts.
3. Retrieval: the corpus and the selected passages; tools: the configuration diff and the authorized decision.
4. Says an output difference usually does not uniquely identify the mechanism, since it could come from prompt text, retrieved context, tool output, model version, or sampling conditions.
5. Says the surrounding record is what lets you attribute the change cautiously.

**Source:** What a production record can and cannot show

## ES-ch09.16

A teammate reruns a task after adding a few-shot example and also after the service quietly moves to a newer model version. The answers improve and the teammate writes that the new example fixed the problem. Using the chapter, explain what the record cannot show and how to repair the comparison.

**Points:** 5

**Rubric (1 point each):**

1. Notes that model version is one of the things that could produce a different answer, alongside prompt text, retrieved context, tool output, and sampling conditions.
2. States that an output difference usually does not uniquely identify the mechanism.
3. Says the comparison should change one object and hold the rest fixed.
4. Says repeated runs per condition are needed because sampling is in play.
5. Says the supportable claim concerns inputs under the recorded interaction, not a change to Claude's weights, and that the surrounding record lets you attribute cautiously.

**Source:** What a production record can and cannot show

## ES-ch09.17

A hosted service shows you only a current model label and a response. What may you say about its before state, and what kinds of reproducibility could you offer for a result?

**Points:** 5

**Rubric (1 point each):**

1. States that you do not invent a before state you cannot see.
2. Says which internal details remain unknown.
3. Notes that the toy is useful because its state is completely visible, and that this should teach restraint where it is not.
4. Names kinds of reproducibility: rerun the Python training from supplied data, replay a prompt under recorded but aging service conditions, or inspect a configuration diff.
5. Says each kind has different dependencies and that identical output is not the only acceptable repeat.

**Source:** What a production record can and cannot show

## ES-ch09.18

For the one-feature classifier, write the score and the sigmoid. Compute the score, the probability, and the loss for the training points when w = 0 and b = 0, and say what the result shows about what the model has encoded.

**Points:** 5

**Rubric (1 point each):**

1. Writes the score as a = wx + b and the sigmoid as 1 / (1 + e^(-a)).
2. Shows that at w = 0 and b = 0 every score is zero regardless of x.
3. Shows that since e^0 = 1 the sigmoid is one-half, so the initial prediction is one-half for all four training points.
4. States that the loss for either label is negative log one-half, about 0.6931471806, so the average is the same value.
5. Concludes that the model has not yet encoded any relationship between feature sign and label.

**Source:** The model: two numbers and a squashing function

## ES-ch09.19

The reference sigmoid uses two branches, one for x >= 0 and one for x < 0. Explain what the negative branch does and why, and say exactly what the lesson test of sigmoid(-1000) does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. States that the negative branch computes e / (1 + e) with e = exp(x).
2. States that it rewrites the same mathematical quantity.
3. Explains that it avoids evaluating an unnecessarily large positive exponential when x is very negative.
4. States that the test checks that sigmoid of negative one thousand is approximately zero without overflow.
5. Says this is evidence for the demonstrated numeric behavior, not a promise about arbitrary types or all floating-point edge cases.

**Source:** The model: two numbers and a squashing function

## ES-ch09.20

After training, the learned weight is positive. Say what a positive weight does to positive and to negative inputs, and what it does not mean. Then say which parts of the chapter's evidence come from a cited source and which from local execution.

**Points:** 5

**Rubric (1 point each):**

1. A positive weight makes positive x values produce positive scores and probabilities above one-half.
2. Negative x values produce probabilities below one-half when the bias stays near zero.
3. This geometry matches the constructed labels.
4. The parameter does not learn a word meaning or a causal relationship; it fits the relationship represented in the supplied pairs.
5. The cited logistic-regression chapter draft supports the weighted-input and sigmoid mechanism, while the numerical results come from the local implementation and an independent calculation.

**Source:** The model: two numbers and a squashing function

## ES-ch09.21

Write the Change and Objective lines of the gate for the toy, and explain why the chapter says the objective is a choice.

**Points:** 5

**Rubric (1 point each):**

1. Change: weights only, the two numbers w and b, starting from zero.
2. States that the prompt, context, tools, settings, and Claude's own weights are not in play.
3. Objective: the average binary logistic loss on the four training pairs, and nothing else.
4. States that "better" means lower on this objective on these pairs, which is the only thing the run may be called.
5. Explains that the optimizer lowers whatever you give it, so the objective is a choice made in the gate.

**Source:** The gate: say what should change before you change it

## ES-ch09.22

Write the Held-out and Stop rule lines of the gate. What one claim can the held-out set support, and what do you do if the budget must change?

**Points:** 5

**Rubric (1 point each):**

1. Fixes four held-out pairs now, never passed to train, and lists them or says they are fixed in advance.
2. Says they share the training data's sign pattern, so they can support one claim: these four fixtures are classified correctly at threshold one-half.
3. Stop rule: exactly 200 updates at rate 0.2, from a zero start.
4. No stopping early because the loss looks flat, and no extra steps because the held-out result looks bad.
5. If the budget must change, reopen the gate and write down why, treating any evaluation points already seen as development data.

**Source:** The gate: say what should change before you change it

## ES-ch09.23

After 200 steps, a teammate sees that the held-out result looks bad, adds 100 more steps, and reports the new held-out result as the result. Evaluate this against the gate in the chapter.

**Points:** 5

**Rubric (1 point each):**

1. Says the gate forbids extra steps because the held-out result looks bad.
2. Says that if the budget must change, the gate is reopened and the reason written down; reopening is a logged act.
3. Says the held-out points have now guided a choice, so they have become development data.
4. Says the new held-out result is no longer an independent use of those points.
5. Says an independent evaluation should be built if the claim requires one, and the change of role recorded.

**Source:** The gate: say what should change before you change it

## ES-ch09.24

The gate promises tests that catch three wrong versions of the program. Name them, say what each does, and say what it means if your tests cannot tell them from the right program.

**Points:** 5

**Rubric (1 point each):**

1. Summing the gradient instead of averaging makes the first step four times too large (0.6 instead of 0.15) while the loss still falls.
2. Copying the x factor into the bias update makes b move on the first step although the symmetric data say it should not.
3. Letting a held-out point into the training list makes the "held-out" result stop meaning anything.
4. States that if the tests cannot tell these from the right program, the gate is not finished.
5. Notes that because the summed version's loss still falls, watching the loss alone would not catch it.

**Source:** The gate: say what should change before you change it

## ES-ch09.25

Write a dated failure sentence for the first update and say why it must be written before the run. Then state what this experiment may claim, what it may not, and the pass condition.

**Points:** 5

**Rubric (1 point each):**

1. Failure sentence: if the first update is right, w moves positive and b stays at zero; if w moves negative, or b moves, a sign or an x factor is wrong.
2. Says it is written and dated before the run, because written after reading the output it only describes the output.
3. May claim: the parameters were updated by this rule, training loss on four pairs fell, and four constructed points were classified correctly.
4. May not claim: generalization, calibration, a change to Claude, or any cause.
5. Pass condition: every test written from the gate passes on the code, and every sentence in the report fits inside the "may claim" line.

**Source:** The gate: say what should change before you change it

## ES-ch09.26

Claude can write the loop in seconds. Explain which parts of the gate it cannot choose for you, why, and what it can do for the gate instead.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the objective, the held-out set, and the stop rule as human decisions.
2. Explains that none can be derived from the data, because the data have no opinion about what "better" should mean.
3. Says that for the toy these are the author's choices (no model produced them) and for a real change request they are yours.
4. Says Claude can sharpen the gate by proposing the wrong version and the test that catches it.
5. Explains that if Claude chose the objective, your report would be a statement about someone else's objective.

**Source:** The gate: say what should change before you change it

## ES-ch09.27

Give the ordinary binary cross-entropy for predicted probability p and the stable expression the reference evaluates from the score a. Say how the reference uses it and why the stable form is used.

**Points:** 5

**Rubric (1 point each):**

1. Gives -y log(p) - (1 - y) log(1 - p).
2. Gives max(a, 0) - y*a + log(1 + e^(-|a|)).
3. States that the reference averages this value across the data.
4. Explains that the stable form avoids computing logarithms of probabilities rounded too close to zero or one for large scores.
5. States that it is a numerically safer route to the same logistic objective for the accepted finite inputs.

**Source:** Loss makes the objective explicit

## ES-ch09.28

A student describes the training function's history as the learning curve and says the loss function is safe on any input. Correct both statements using the chapter.

**Points:** 5

**Rubric (1 point each):**

1. States that history appends only the initial and the final loss.
2. States that two values are not a learning curve.
3. Says that if you add full history, you must state that your version changed the implementation.
4. States that the loss function assumes nonempty data because training validates that before calling it.
5. States that invoked directly on an empty list it would divide by zero, so describe guarantees at the call boundary that actually exists.

**Source:** Loss makes the objective explicit

## ES-ch09.29

Using the training data [(-2, 0), (-1, 0), (1, 1), (2, 1)] at w = 0, b = 0 and rate 0.2, compute by hand the four errors, the four weight-gradient contributions, the average weight and bias gradients, and the new w and b.

**Points:** 5

**Rubric (1 point each):**

1. Errors (prediction minus label) are 0.5, 0.5, -0.5, -0.5.
2. Weight contributions (p - y)x are -1.0, -0.5, -0.5, -1.0.
3. They sum to -3, so the average weight gradient is -0.75.
4. The errors sum to zero, so the average bias gradient is zero.
5. New w = 0 - 0.2(-0.75) = 0.15, and b stays at zero.

**Source:** Derive the first update

## ES-ch09.30

State the derivative of the logistic loss with respect to the score for one example, show how it gives the weight and bias gradient contributions, and explain in words why the first weight update should be positive.

**Points:** 5

**Rubric (1 point each):**

1. The derivative with respect to the score is prediction minus label, the error e.
2. Because the score is wx + b, the weight contribution is e times x and the bias contribution is e.
3. Gradient descent subtracts the learning rate times the gradient.
4. Since the average weight gradient at the start is negative, subtracting it moves w up.
5. Increasing a positive weight pushes positive examples toward label one and negative examples toward label zero.

**Source:** Derive the first update

## ES-ch09.31

Describe the central finite-difference check of the weight gradient at zero, give the value it should approximate, and say what agreement does and does not establish.

**Points:** 5

**Rubric (1 point each):**

1. Evaluates the loss at a small positive and a small negative perturbation and divides the difference by twice the perturbation.
2. Gives approximately -0.74999999999, agreeing with the analytic -0.75.
3. Says agreement within the tolerance checks the analytic expression at this point and fails differently from the derivation, because it never uses the derivative formula.
4. Says it is an independent calculation, not an independent dataset, reviewer, or causal source.
5. Says that if logistic loss is the wrong objective the derivative and finite difference still agree, because whether it is the objective you meant is the gate's question.

**Source:** Derive the first update

## ES-ch09.32

Describe what the training function validates and what each step does, name three things it does not do, and state what the existing tests do and do not show about the result after 200 steps.

**Points:** 5

**Rubric (1 point each):**

1. Validates that labels are zero or one, features are finite, steps is a positive integer, and the rate is positive and finite.
2. Initializes both parameters to zero and records the initial loss; each step builds errors from the current parameters, averages the gradient contributions, and updates weight and bias.
3. Does not shuffle, use minibatches, or adapt the rate: it is batch gradient descent on the complete declared dataset.
4. After 200 steps the weight is about 3.1669517461, the bias is effectively zero, and the training loss is 0.0215209850.
5. The existing tests check that the loss fell and the weight is positive; passing them does not show the optimizer behaves under every dataset or rate.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.33

A classmate says the 0.15 first step is what the data demand. Respond using the chapter. Then compute the first step at rate 0.1 and at rate 0.4, and say what the chapter does and does not establish about choosing a rate.

**Points:** 5

**Rubric (1 point each):**

1. Explains that 0.15 is the average gradient -0.75 scaled by the rate 0.2 you chose, so it does not arise from the data alone.
2. Computes the first step as 0.075 at rate 0.1 and 0.3 at rate 0.4.
3. States that the rate is supplied to train and never updated: it is a setting of the experiment, not a learned parameter.
4. States that a very large rate can overshoot or become unstable on some data, and a very small one makes limited-step progress slow.
5. States that the research establishes no safe universal range, so you test chosen values on declared fixtures and do not write an optimization theorem from one decreasing-loss run.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.34

The demo runs exactly 200 steps. What does that number mean, what does the function lack, and how should you run a fair comparison of rates or step counts?

**Points:** 5

**Rubric (1 point each):**

1. States that 200 is the demo setting, not a discovered natural stopping point.
2. States that the function runs exactly that many updates, with no convergence test, validation-based early stopping, or best-checkpoint selection.
3. States that a lower final training loss shows what happened after the configured loop, not that the budget was right.
4. Says to hold the data and initial parameters fixed and keep every result, including runs that behave badly.
5. Says to choose evaluation criteria before looking for the most attractive run, otherwise the comparison becomes a search whose selection is hidden.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.35

Reverse all four training labels and keep the features. Compute the first-step average weight gradient and the new weight at rate 0.2, and say what the chapter predicts about the preferred weight direction. Then explain what happens to the separation between fit and evaluation if the held-out points are duplicated into the training data.

**Points:** 5

**Rubric (1 point each):**

1. Computes the weight contributions with reversed labels as +1.0, +0.5, +0.5, +1.0, which average to +0.75.
2. Computes the new weight as 0 - 0.2(0.75) = -0.15.
3. States that the preferred weight direction should reverse (negative rather than positive).
4. States that duplicating the evaluation points into the training data contaminates the separation between fit and held-out assessment.
5. States that apparent improvement on those points becomes hard to interpret, because the optimizer has already used them.

**Source:** The loop, its rate, and its stop rule

## ES-ch09.36

With the trained parameters, the held-out predicted probabilities for x = -3, -0.5, 0.5, and 3 are about 0.00007478, 0.17030378, 0.82969622, and 0.99992522. Apply the threshold, state the result, state the strongest claim the chapter allows from it, and say what a broader claim would need.

**Points:** 5

**Rubric (1 point each):**

1. Applies the threshold at one-half and predicts labels 0, 0, 1, 1.
2. States that all four held-out labels are correct.
3. Says "held out" means only that the points were not passed into the training function, a statement about how they were handled.
4. States the allowed claim: the trained parameters classified four separately specified sign-pattern fixtures correctly; "the model generalized" is too broad because the points were designed around the same sign boundary and are not representative of a natural population.
5. Says a broader performance claim needs a justified sampling process, a task definition, and a larger evaluation.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.37

You use the held-out result to decide whether to change the number of steps. What has happened to the held-out set, what should you record, and how many roles for data do you now need?

**Points:** 5

**Rubric (1 point each):**

1. Says that once the held-out set guides a choice (a rate, a step count, or a decision to keep going) it has become development data.
2. Says its next use is no longer independent.
3. Says to record the change of role when it happens.
4. Says to build an independent evaluation if the claim requires one.
5. Says that once you tune anything you need three roles: training, a development set to tune against, and a held-out set you touch once.

**Source:** Held-out means separately specified, not magically representative

## ES-ch09.38

Suppose label one means "escalate this message to a person," and a missed escalation is far worse than a false alarm. Training loss falls. What does that establish, what does it not, and what should the gate have named?

**Points:** 5

**Rubric (1 point each):**

1. States that lower training loss shows the update rule reduced the objective on the pairs it was shown.
2. States that it does not establish fit to pairs it was not shown, which is what the held-out set is for.
3. States that it does not establish that the objective was the right one, which no dataset can establish.
4. Explains that logistic loss penalizes errors by how confident the model was in the wrong direction, not by what each error costs, so a lower loss can sit beside the wrong behavior.
5. Says the gate should have named the costs of the two errors, and the report should say "training loss decreased" rather than "better."

**Source:** What a lower loss claims

## ES-ch09.39

Distinguish score, probability, and decision in the toy classifier. Say what produces each, and what happens when you move the threshold.

**Points:** 5

**Rubric (1 point each):**

1. The score wx + b comes from the parameters.
2. The probability comes from the sigmoid.
3. The decision comes from a threshold, here one-half.
4. The threshold is a choice you made and training never saw; moving it moves the decisions with identical parameters.
5. You record all three layers and know which one a claim is about.

**Source:** Score, probability, and decision are three layers

## ES-ch09.40

The learned bias is extremely close to zero. Explain why, why it would be a mistake to conclude that bias is unnecessary, and where the decision boundary sits.

**Points:** 5

**Rubric (1 point each):**

1. Notes that the data are symmetric: each negative feature with label zero has a positive partner with label one.
2. Notes that at the origin the errors sum to zero, so the first bias update is zero.
3. States that across training the symmetry keeps the learned bias extremely close to zero in the recorded run.
4. Says bias shifts the decision boundary whenever the relationship is not centered at zero, and that removing one point or changing one label can break the symmetry.
5. States that the boundary sits where wx + b = 0, because sigmoid zero is one-half, so with positive w and nearly zero b it lies near x zero.

**Source:** Score, probability, and decision are three layers

## ES-ch09.41

The held-out probabilities are more extreme farther from zero (0.99992522 at x = 3 versus 0.82969622 at x = 0.5). A teammate says this shows the model's confidence is well calibrated. Respond using the chapter.

**Points:** 5

**Rubric (1 point each):**

1. States that more extreme probabilities farther from zero are an observed property of this fitted curve under the learned positive weight, on selected points.
2. States that this is not evidence that the confidence is calibrated.
3. Notes that a model's probability is tied to its mechanism and objective.
4. Explains that calibration means matching observed frequencies, which takes a calibration study on suitable labeled data.
5. States that four sign fixtures cannot support a calibration claim.

**Source:** Score, probability, and decision are three layers

## ES-ch09.42

x counts the reminder emails a student opened in the first month, y records whether they passed, and the fitted weight is positive. Contrast "what label will the model assign to a student who opened four emails?" with "if we require every student to open the emails, will more of them pass?" and say what evaluating the function at a larger x does and does not tell you.

**Points:** 5

**Rubric (1 point each):**

1. Says the first question is about the model, and evaluating the fitted function answers it.
2. Says the second question is about the world, and the function answers a different question.
3. Says evaluating at a larger x gives the model's response to a changed input, not the course's response to a changed behavior.
4. Names at least three other sources of the association: opening helps, students already on track open more (reverse arrow), a third factor such as motivation or free time, or a sample of only students who stayed enrolled.
5. Says a positive weight cannot tell you which source you have, because each is consistent with it.

**Source:** Decide what kind of question you are asking

## ES-ch09.43

Explain how acting on a prediction can undermine it, and why a causal sentence about the chapter's four training pairs would be a story rather than a finding.

**Points:** 5

**Rubric (1 point each):**

1. States that acting on a prediction can change the process that generated the data.
2. States that a model fit to a period in which nobody acted on its flags can say little about what happens once people do.
3. States that the four constructed pairs were chosen to make the gradient visible.
4. States that they contain no information about any process in the world.
5. Concludes that a causal sentence about them is a story attached to a fixture.

**Source:** Decide what kind of question you are asking

## ES-ch09.44

Name the three rungs of Pearl's ladder as the chapter gives them, state the one-line version of what the ladder implies for prediction, and say what the limit does and does not claim.

**Points:** 5

**Rubric (1 point each):**

1. Names association (what goes with what), intervention (what happens if I do this), and counterfactual (what would have happened to this case had we done otherwise).
2. States that prediction is not identification: interventional and counterfactual answers generally cannot be recovered from purely observational data without structural assumptions that did not come from the data.
3. Says the limit is about information, about what observational data can yield, and is not a proof that no machine architecture could ever reason causally.
4. Says someone must supply and defend the causal assumptions, and that more data, confident intuition, or a fluent explanation does not supply them.
5. Says observational data can support a causal claim under assumptions you state and defend.

**Source:** Decide what kind of question you are asking

## ES-ch09.45

In the causal part of the chapter, what can Claude do, what does it lack, and what judgment stays with you?

**Points:** 5

**Rubric (1 point each):**

1. Claude can write causal diagram notation, list the confounders it can think of, work out what follows from a stated structure, and run the code.
2. Its fluent paragraphs about confounding exist because such text is abundant in what such systems learn from, and fluency about causation is not identification of it.
3. It lacks your study design, how the data were collected, and the domain facts about your students.
4. It has nothing riding on the decision.
5. The identification judgment (choosing the variables and asserting the structure you are prepared to defend) stays with the person who will act.

**Source:** What is Claude's here, and what is yours

## ES-ch09.46

State the working rule the chapter gives for deciding, before you hand Claude the algebra, what kind of question a stakeholder is asking, and say how the chapter's report is meant to show you drew that line.

**Points:** 5

**Rubric (1 point each):**

1. Write one sentence saying whether the question is "what will the model say" or "what happens if we act."
2. Also write who decided.
3. Notes the book's observation that deciding whether the question is causal is itself a causal judgment.
4. States that the report ends with one predictive claim the fixture supports and one intervention claim it does not establish.
5. States that the pair is the evidence that you drew the line.

**Source:** What is Claude's here, and what is yours

## ES-ch09.47

Describe the order of work in Build It, and say what you do if your first-step weight does not equal 0.15.

**Points:** 5

**Rubric (1 point each):**

1. Implements sigmoid and tests zero, a large negative input, and a symmetry you can justify; implements the stable loss and calculates the origin by hand.
2. Implements one gradient step before writing the full loop.
3. Reads the six lesson tests before the reference and predicts the direction and rejection cases.
4. If the value differs from 0.15, inspects averaging, signs, and use of the current parameters.
5. Does not adjust the expected result until the discrepancy is explained, because it came from the hand derivation, the independent route.

**Source:** Build It: the baseline that lets you audit

## ES-ch09.48

In Build It you change the update to sum the gradient instead of averaging. Compute the first step at rate 0.2 for the toy data, say what three predictions you write before running it, and explain why a lower final loss would not show the code is right.

**Points:** 5

**Rubric (1 point each):**

1. Computes the summed first-step gradient as -3, so the step is 0.2 x 3 = 0.6, four times the reference 0.15.
2. Names the three predictions: which of the six lesson tests will fail, how far the first step lands from 0.15, and whether the final loss after 200 steps is higher or lower than 0.0215209850.
3. Notes that tests 03 and 04 check only that the loss fell and that the weight is positive, so they cannot tell the summed version from the averaged one.
4. Notes that the loss still falls in the summed version.
5. Says that whatever number appears at step 200, a lower number does not show the update rule is right.

**Source:** Build It: the baseline that lets you audit

## ES-ch09.49

You hand Claude Code your gate. Say what you give it, what you do with what it returns, and how the three follow-up checks work.

**Points:** 5

**Rubric (1 point each):**

1. Gives it the gate (change, objective, held-out list, stop rule, and test list) but not your implementation.
2. Runs your own tests on what it returns, yourself.
3. Notes which tests failed, since a failure is often a gap in the gate (for example, early stopping you never asked for means your stop rule had a hole).
4. Compares its implementation with your baseline and names one difference in behavior, such as keeping held-out points out of training, how the average is computed, or recording more than two losses.
5. Asks Claude to propose a deliberately wrong version that still passes your tests and checks by hand whether it does; if it does, the test list was too weak.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch09.50

What must you preserve from a Claude Code session, what do you do if the session failed or did not run, and why can't Claude judge whether your tests are enough?

**Points:** 5

**Rubric (1 point each):**

1. Preserves the prompt, the plan, the diff, the commands, and the outputs.
2. Records the date and displayed model label.
3. If a session failed or did not run, records that.
4. Does not substitute a fixture for the missing session.
5. States that whether your tests are enough cannot be judged by the system they are testing.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch09.51

Design the chapter's second task, which touches Claude's behavior: what conditions do you prepare, what rule governs them, what do you write first, what do you record, and what do you say about what is being changed?

**Points:** 5

**Rubric (1 point each):**

1. Prepares a baseline prompt, a few-shot prompt, and a retrieved-context condition on the same bounded task.
2. Changes only one object between conditions.
3. Writes a prediction for each condition first.
4. If run, records the actual responses, interface, date, and displayed model label; if not run, labels the design proposed.
5. States that these conditions change inputs, not Claude's weights.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch09.52

List what the Ship It report must contain, including how it separates mathematical success from decision authority.

**Points:** 5

**Rubric (1 point each):**

1. Includes loss history, before and after parameters, held-out results, and a comparison of parameter learning, prompt changes, and context changes.
2. Preserves the training data and evaluation points, and records the interpreter, step count, rate, initial values, final values, and threshold.
3. Says which results came from the lesson and which from your extension.
4. Includes a table with mutable object, mechanism, persistence, evidence, and remaining limits, keeping permissions and tools separate from model parameters.
5. Ends with one predictive claim supported by the actual toy evaluation and one intervention claim it does not establish.

**Source:** Ship It: the comparison report and its sign-off

## ES-ch09.53

Fill in the "Not checked" and "Not claiming" lines of the sign-off for this chapter's work, and explain why the "Not checked" line matters when Claude drafts the sign-off.

**Points:** 5

**Rubric (1 point each):**

1. Not checked includes data beyond the four training and four held-out fixtures, and other rates, step counts, or starts.
2. Not checked also includes calibration of the probabilities, any change to Claude itself, and any real-world effect of changing x.
3. Not claiming includes that the model generalizes, that lower training loss means better, and that any input causes any outcome.
4. Says the "Not checked" line is the one an AI-written sign-off omits, because the system that wrote it has no record of what you did not do.
5. Says you write the sign-off from your own record, and that withholding is an honest result if the evidence does not support signing.

**Source:** Ship It: the comparison report and its sign-off

## ES-ch09.54

Choose the right verb for each claim and justify it: "lowered the objective on four pairs," "learned," "generalizes," and "causes." What is the rule for choosing?

**Points:** 5

**Rubric (1 point each):**

1. "Lowered the objective on four pairs" describes what the optimizer did.
2. "Learned" describes a parameter change, which is accurate here.
3. "Generalizes" needs a criterion you have not run.
4. "Causes" needs assumptions the fixture cannot supply.
5. The rule: choose verbs to match the evidence, since a pass names the obligation it passed and no more.

**Source:** Ship It: the comparison report and its sign-off

## ES-ch09.55

Using the driver's seat table, say for (a) deciding whether the question is prediction or intervention and (b) deciding what the result supports: what Claude should do, what you should do, and why it stays with you. Then say what the report must record about the split.

**Points:** 5

**Rubric (1 point each):**

1. (a) Claude can draft a diagram, list confounders, and compute under a stated model.
2. (a) You decide which kind of question it is, justify the assumptions, and get domain evidence, because the assumptions are not in the data and you are the one who acts.
3. (b) Claude can flag an overclaim.
4. (b) You choose the verb and sign, because your name is on the claim.
5. The report records one task delegated and one judgment retained, with a transcript line or edit showing each; otherwise the split happened in your head and not in the record.

**Source:** The driver's seat

## ES-ch09.56

Classify these four proposed changes by the object each modifies and say how you would observe each: a rewritten system prompt, a new document in a workspace, a newly enabled tool, and a lowered temperature. What may you not conclude if the only evidence is a different output?

**Points:** 5

**Rubric (1 point each):**

1. Rewritten system prompt: the prompt, observed by comparing both texts.
2. New document in a workspace: the context, observed through the passages that actually entered the input.
3. Newly enabled tool: the tools, observed through the configuration diff and the decision that authorized it.
4. Lowered temperature: a setting, observed through the recorded setting for each run.
5. States that if the only evidence is a different output, you should not jump to a claim about changed weights.

**Source:** Verify and reflect

## ES-ch09.57

List the checks the chapter asks you to run when you verify your work, including what to do with the words "history" and "generalization" and with your strongest causal verb.

**Points:** 5

**Rubric (1 point each):**

1. Runs the demo, the lesson tests, your gradient check, and the held-out calculation.
2. Recomputes the first update independently and preserves exact outputs rather than reconstructing them after reading the expected values.
3. Checks every use of "history": two loss values are initial and final, not a full curve.
4. Checks every use of "generalization": four designed points are separate fixtures, not evidence of population performance.
5. Inspects the strongest causal verb (association or intervention?) and narrows the claim if the data and design cannot support it.

**Source:** Verify and reflect

## ES-ch09.58

The chapter says the most useful reflection is local. Name the four distinctions it suggests you may have collapsed, say what you do about them, and state what it says about mechanism labels.

**Points:** 5

**Rubric (1 point each):**

1. Names the four distinctions: training and context; lower loss and better; held-out and representative; prediction and intervention.
2. Says to name the calculation or the one-object test that separated them again.
3. Says mechanism labels should make evidence easier to inspect, and that when they hide the mutable object they have become branding.
4. Says to ask of any change which component changed, who changed it, and what evidence records the transformation.
5. Says that if those questions stay unanswered, you use a narrower description until the mechanism is known.

**Source:** Verify and reflect

## ES-ch09.59

Describe what Conduct, Check, and Drive looked like at this chapter's scale, in terms of what you did.

**Points:** 5

**Rubric (1 point each):**

1. Conducted: wrote the change, the objective, the held-out list, and the stop rule before the loop ran.
2. Conducted: tested Claude's version against those items.
3. Checked: wrote "training loss decreased" when that was all that was measured.
4. Checked: let neither persistence nor a good-looking prompt stand in for training.
5. Drove: handed Claude the algebra and the loop, kept the question of whether this was prediction or intervention, and signed or withheld.

**Source:** What you can now explain

## ES-ch09.60

State the "AI should" and "Human should" responsibilities the chapter gives for the prediction-versus-intervention question, and say what the chapter does and does not take from the companion passage.

**Points:** 5

**Rubric (1 point each):**

1. AI should inspect calculations, run bounded experiments, tabulate predictions, and challenge assumptions.
2. AI can compute consequences under an explicitly stated model and propose candidate confounders, and should label assumptions as assumptions instead of presenting a plausible story as established causation.
3. Human should decide whether the task asks for prediction or intervention, and justify the outcome and causal assumptions.
4. Human should obtain relevant domain evidence and own the decision to act; human intuition is not sufficient causal proof either.
5. The chapter uses the passage's information boundary, not a claim that a particular machine architecture can never represent causal reasoning.

**Source:** Irreducibly Human

## ES-ch09.61

Write the form the chapter gives for an intervention claim, and explain what it means if you can or cannot fill in its provisos. Then explain why changing x in the fitted Python function does not measure a real-world effect, and what in the record shows who wrote the assumptions.

**Points:** 5

**Rubric (1 point each):**

1. Gives the form: "if I change x by doing D, the outcome changes by about this much, provided P, Q, and R."
2. If you can fill in P, Q, and R, you have found the assumptions to defend and the evidence to go and get.
3. If you cannot, you have a prediction.
4. Changing x in the fitted function measures the model's response, not necessarily the effect of changing a real-world variable.
5. Points to the transcript line or the edit showing that you, not Claude, wrote the sentence that names the assumptions.

**Source:** Irreducibly Human
