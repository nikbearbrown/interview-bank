# Chapter 1: Next-token prediction and sampling

## MA-ch01.1

Check each statement that is true about the chapter's opening scenario, in which the same question put to Claude twice produces two different answers. Each statement is worth 1 point (5 points total).

- [ ] A. Claude can write a fluent, confident account of why the answers differed, and that account may even be right.
- [ ] B. Two different answers show that a difference has been observed, but not yet that its cause has been isolated.
- [ ] C. "The prompt was vague," "the model was creative," and "the system was unreliable" are explanations that each identify the moving part.
- [ ] D. Claude cannot know which moving part you needed to isolate.
- [ ] E. Claude can check its own account against the machinery and put its name on the result.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The chapter says the account "may even be right."
- B: "You have observed a difference. You have not yet isolated its cause."
- C: None of those descriptions identifies the moving part.
- D: Knowing what you needed isolated is on the human side of the division of labor.
- E: It cannot check its account against the machinery or sign the result.

**Source:** Opening (before "What you will be able to do")

## MA-ch01.2

Check each statement that is true about the chapter's argument in brief. Each statement is worth 1 point (5 points total).

- [ ] A. One of the three jobs is to out-produce Claude at generating plausible candidates.
- [ ] B. Claude has a stake in whether its output is true.
- [ ] C. Claude can tell you whether its output is the thing you needed.
- [ ] D. The three jobs that stay with you are conduct, check, and drive.
- [ ] E. Claude is far better than you at producing fluent text, working code, and long lists of plausible candidates, so the chapter says not to compete with it there.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The chapter says not to compete with Claude on candidates.
- B: It "has no stake in whether any of it is true."
- C: It has no way to tell you whether the output is what you needed.
- D: Decide before it runs (conduct), check what comes back (check), sign what you keep (drive).
- E: Speed and volume are Claude's strength; the chapter says not to compete there.

**Source:** Opening (before "What you will be able to do")

## MA-ch01.3

Check each statement that is true about the distinction that both parts of the chapter serve. Each statement is worth 1 point (5 points total).

- [ ] A. A score is not a probability.
- [ ] B. A probability is not an observed frequency.
- [ ] C. Making a run repeatable makes its answer true.
- [ ] D. Making one outcome increasingly likely adds evidence that it is correct.
- [ ] E. An observed frequency is not a correctness judgment.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Scores are not yet probabilities; they must be transformed first.
- B: Assigned chance and appearing share are different quantities.
- C: Repeatability does not make an answer true.
- D: The chapter says an outcome can be made more likely "without adding any evidence that it is correct."
- E: A count of selections says nothing about correctness.

**Source:** Opening (before "What you will be able to do")

## MA-ch01.4

Check each statement that is true about how the chapter's Part 2 experiment is set up. Each statement is worth 1 point (5 points total).

- [ ] A. Part 2 shrinks the machine to three outcomes and three numbers so that every intermediate value can be inspected.
- [ ] B. The chapter's Python experiment needs an API key.
- [ ] C. The toy reproduces Claude closely enough to stand in for it.
- [ ] D. The chapter's Python experiment spends direct API credits.
- [ ] E. Public readers are told to begin with the university's Claude portal.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Nowhere for an unexplained operation to hide.
- B: It needs no API key.
- C: "The toy will not reproduce Claude, and that is its advantage."
- D: It spends no direct API credits.
- E: Enrolled Northeastern students use the portal; public readers need their own Claude Code-enabled account.

**Source:** Opening (before "What you will be able to do")

## MA-ch01.5

Check each statement that is true about the table of the three jobs. Each statement is worth 1 point (5 points total).

- [ ] A. Conduct comes from the companion book Computational Skepticism for AI.
- [ ] B. Check has the driver's seat as its device.
- [ ] C. Drive comes from the companion book Irreducibly Human.
- [ ] D. Check comes from the companion book Conducting AI.
- [ ] E. Conduct adds the question "What did I decide before Claude started, and what must be true before this output goes downstream?" and its device is the gate.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Conduct pairs with Conducting AI.
- B: Check's device is the sign-off; the driver's seat belongs to Drive.
- C: Drive pairs with Irreducibly Human.
- D: Check pairs with Computational Skepticism for AI.
- E: Conduct maps to the gate.

**Source:** Three jobs that stay yours

## MA-ch01.6

Check each statement that is true about the Conduct job. Each statement is worth 1 point (5 points total).

- [ ] A. A gate is a general preference about quality that does not need to be testable.
- [ ] B. In Conducting AI the human's job is "not to type less" but "to decide more precisely."
- [ ] C. Claude implements well from a complete specification and badly from an incomplete one.
- [ ] D. As used here, a gate is a few lines written after Claude has produced code, describing what the code happens to do.
- [ ] E. Claude will tell you which kind of specification you gave it.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A gate is "a specific, testable condition that must hold before an output moves on."
- B: This is the quoted formulation.
- C: The chapter states this directly.
- D: A gate is written before asking Claude for anything.
- E: "It will not tell you which you gave it."

**Source:** Three jobs that stay yours

## MA-ch01.7

Check each statement that is true about the Check job. Each statement is worth 1 point (5 points total).

- [ ] A. You should write down what a wrong answer would look like before you read the output.
- [ ] B. Claude's mistakes arrive fluent: the well-formed prose does the work the verification should have done.
- [ ] C. Claude should not be asked to run tests or propose counterexamples.
- [ ] D. An AI checking an AI counts as an independent second opinion.
- [ ] E. After you read the output, you should revise that note so it matches what you saw.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Writing it down first is one of the two habits.
- B: This is the chapter's account of why fluent errors persuade.
- C: The chapter says Claude can run tests and propose counterexamples; the check must still be independent.
- D: It is "the first opinion run twice."
- E: The note is not to be revised afterward.

**Source:** Three jobs that stay yours

## MA-ch01.8

Check each statement that is true about the Drive job and the baseline you build by hand. Each statement is worth 1 point (5 points total).

- [ ] A. You build small things by hand in order to out-type Claude.
- [ ] B. Irreducibly Human puts the reason in one line: you cannot audit what you do not know.
- [ ] C. You choose the question, justify the assumptions, and own the decision.
- [ ] D. The split of work is by task, not by a slogan about who is smarter.
- [ ] E. Building by hand acquires the baseline that makes conducting possible.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: "You are not trying to out-type Claude."
- B: The chapter attributes the line to Irreducibly Human.
- C: These are the human's tasks in Drive.
- D: The chapter says so explicitly.
- E: The baseline is what makes conducting possible.

**Source:** Three jobs that stay yours

## MA-ch01.9

Check each statement that is true about the car picture. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter calls the car picture complete.
- [ ] B. Confidence and correctness come from the same place, so high confidence signals correctness.
- [ ] C. In the car picture, Claude chooses the destination and you supply the speed.
- [ ] D. The driver needs to understand the engine well enough to hear a knock that makes no sound.
- [ ] E. A car's failures are loud; Claude's failures are quiet.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: "Good and incomplete."
- B: The chapter says they "come from different places."
- C: "The car does not choose the destination. You do."
- D: This is the chapter's conclusion about the driver.
- E: Engine knocks and dashboard lights versus quiet failure.

**Source:** Three jobs that stay yours

## MA-ch01.10

Check each statement that is true about "The unfinished script" and the loop around the model. Each statement is worth 1 point (5 points total).

- [ ] A. When you send a message to Claude, one component answers your question and a loop around it only formats the reply.
- [ ] B. Once retrieval, tools, permissions, and approval gates are added, they no longer need to be checked.
- [ ] C. Nothing in the loop reads a document, checks an answer key, or knows whether the growing text is true.
- [ ] D. The chapter calls the procedure of rebuilding the missing half only an analogy for a chatbot, not a description of one.
- [ ] E. One component is repeatedly answering the question of what plausibly comes next in the text.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: No component in the system is answering your question.
- B: Every such attempt is something you design and then check.
- C: This is the machine's boundary.
- D: "That procedure is not an analogy for a chatbot. It is a description of one."
- E: A loop turns those answers into something that reads like a reply.

**Source:** The unfinished script

## MA-ch01.11

Check each statement that is true about tokens. Each statement is worth 1 point (5 points total).

- [ ] A. A prompt that asks for an exact character count asks the machine to reason about a unit it does not natively see.
- [ ] B. A space is usually its own separate token.
- [ ] C. The chapter's illustrative table splits the five words into eleven tokens.
- [ ] D. The split shown in the table is the output of a particular real tokenizer.
- [ ] E. The machine predicts tokens, not words.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Characters are not the model's native unit.
- B: A space is usually part of the token that follows it.
- C: Un/believ/ably/comma, Paris, costs, 1/comma/200, euros/period gives eleven.
- D: The split is "illustrative, not the output of any particular tokenizer."
- E: Tokens are fragments from a fixed vocabulary.

**Source:** One question, asked over and over

## MA-ch01.12

Check each statement that is true about what happens inside a prediction step. Each statement is worth 1 point (5 points total).

- [ ] A. Absurd continuations get small shares rather than being excluded.
- [ ] B. Each vocabulary entry selects a vector of learned numbers called an embedding.
- [ ] C. The output for one step is a single token.
- [ ] D. The output is a number for every token in the vocabulary, arranged so the numbers are nonnegative and sum to one.
- [ ] E. A word that spans three tokens takes three steps to finish.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: "Nothing is excluded; things are merely ranked."
- B: Inside the model a token is a vector, not text.
- C: The output is a number for every token, not a token.
- D: This is the description of the output.
- E: Nothing in the loop treats a word as a unit.

**Source:** One question, asked over and over

## MA-ch01.13

Check each statement that is true about Figure 1.2 and `Paris` after `The capital of France is`. Each statement is worth 1 point (5 points total).

- [ ] A. The ordering describes the training corpus and not the world.
- [ ] B. The distribution ranks continuations of a string.
- [ ] C. A high probability for `Paris` is the output of a lookup against an atlas.
- [ ] D. The agreement between the model and an atlas here is a fact about the corpus, not a mechanism that guarantees agreement in the next case.
- [ ] E. Its shape was fixed by fitting parameters to a body of text.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The figure caption says exactly this.
- B: That is the caption's argument.
- C: It reports how the phrase tends to continue in the corpus.
- D: This is the chapter's load-bearing distinction.
- E: Parameters were fit to text.

**Source:** One question, asked over and over

## MA-ch01.14

Check each statement that is true about how a chat works under the interface. Each statement is worth 1 point (5 points total).

- [ ] A. Roles are text in a document that the machine is completing.
- [ ] B. The model's job is to continue that string.
- [ ] C. Roles are modes that the software switches into.
- [ ] D. The most plausible continuation of a string ending in `Assistant:` is an assistant-sounding reply.
- [ ] E. Under the interface, a chat is a single string with role markers.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Roles are text, not modes.
- B: The model continues the string.
- C: Roles are not modes.
- D: That is why the model produces a reply.
- E: A chat is one string with markers.

**Source:** The transcript is the whole trick

## MA-ch01.15

Check each statement that is true about the system prompt and about memory. Each statement is worth 1 point (5 points total).

- [ ] A. If a rule matters, placing it in the system prompt is sufficient enforcement.
- [ ] B. Only your newest message is resupplied each turn.
- [ ] C. Chapter 7 treats context as something you simply have.
- [ ] D. A system prompt is a request, not a gate.
- [ ] E. The model remembers your last conversation.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Enforcement belongs in the runtime that wraps the model.
- B: The entire transcript is resupplied every turn; what feels like memory is a growing string.
- C: Chapter 7 treats context as something you engineer rather than have.
- D: It is a paragraph competing for influence with every other paragraph.
- E: The model does not remember your last conversation.

**Source:** The transcript is the whole trick

## MA-ch01.16

Check each statement that is true about the "continue this text" prompt (the support-call transcript). Each statement is worth 1 point (5 points total).

- [ ] A. You should save the result with the exact prompt, your prediction, and the date.
- [ ] B. The prompt asks for the mechanism without the costume of an assistant reply.
- [ ] C. You should write down what you expect Claude to do, in one sentence, and date it, before pasting the prompt.
- [ ] D. The later comparison against a normal request is worth just as much if the prediction is written after you see the result.
- [ ] E. The saved result is later compared against a normal request.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Those are the three things to save.
- B: It asks Claude to continue the string as literal text.
- C: Write the prediction first.
- D: The comparison "is only worth anything if the prediction was written first."
- E: The chapter says it is compared against a normal request later.

**Source:** The transcript is the whole trick

## MA-ch01.17

Check each statement that is true about where the model's parameters come from. Each statement is worth 1 point (5 points total).

- [ ] A. The pretraining procedure is told what is true.
- [ ] B. The parameters were never set by hand.
- [ ] C. The parameters start random, so the model starts by producing noise.
- [ ] D. Current systems have hundreds of billions of continuous parameter values.
- [ ] E. The pretraining target is what the corpus did next.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: "Nothing in this loop is told what is true."
- B: The chapter says they "were never set by hand."
- C: They are adjusted from random starting values.
- D: The chapter gives "hundreds of billions" for current systems.
- E: The true token is whatever followed in the text.

**Source:** Where the numbers come from

## MA-ch01.18

Check each statement that is true about pretraining. Each statement is worth 1 point (5 points total).

- [ ] A. A passage is taken, the next token is hidden, and the model's distribution is compared with the token that actually followed.
- [ ] B. Backpropagation is not used in pretraining.
- [ ] C. Backpropagation nudges only a few parameters and leaves the rest fixed.
- [ ] D. The second stage adjusts the parameters using only the next token in the corpus, with no human judgments.
- [ ] E. Pretraining produces something that behaves like an assistant.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: That is the described loop.
- B: Backpropagation is how the parameters are nudged in this stage.
- C: It nudges every parameter slightly.
- D: In the second stage people say which replies they prefer.
- E: It "completes internet text rather than something that behaves like an assistant."

**Source:** Where the numbers come from

## MA-ch01.19

Check each statement that is true about preference tuning and correctness. Each statement is worth 1 point (5 points total).

- [ ] A. This divergence follows from the objective rather than being a scandal about any company's process.
- [ ] B. Where approval and correctness diverge, the training signal follows approval.
- [ ] C. Approval and correctness are the same target.
- [ ] D. A confident, well-organized, wrong answer is exactly what a rater who does not know the answer can prefer.
- [ ] E. Approval and correctness overlap heavily, since raters generally prefer accurate answers.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The chapter says it "follows from the objective."
- B: The signal follows approval.
- C: They are "different targets."
- D: A rater without the answer can approve a fluent wrong one.
- E: Raters generally prefer accurate answers.

**Source:** Where the numbers come from

## MA-ch01.20

Check each statement that is true about the GPT-3 figures used as an anchor. Each statement is worth 1 point (5 points total).

- [ ] A. The reported total training compute is 3.14 x 10^23 floating-point operations.
- [ ] B. GPT-3 has 175 billion parameters.
- [ ] C. GPT-3 was trained on roughly 300 billion tokens.
- [ ] D. The figures of later frontier models are always published.
- [ ] E. GPT-3 is a useful anchor because its details were published.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The reported total training compute is a published figure (Brown et al., 2020).
- B: 175 billion parameters is a published detail (Brown et al., 2020).
- C: Roughly 300 billion training tokens is a published detail.
- D: Later models' figures "are frequently undisclosed."
- E: That is the stated reason for using it.

**Source:** Scale, in units you can check

## MA-ch01.21

Check each statement that is true about the "thousands of years to read it" derivation. Each statement is worth 1 point (5 points total).

- [ ] A. Three hundred billion tokens at about 0.75 words per token is 225 billion words.
- [ ] B. The answer moves by more than a thousand years depending on a reading rate nobody stated.
- [ ] C. Reading nonstop at 250 words per minute gives about 1,711 years.
- [ ] D. The headline figure is a measurement.
- [ ] E. Reading at 150 words per minute takes more years than reading at 250 words per minute.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: 300 billion times 0.75 is 225 billion.
- B: The spread runs from 1,711 to 2,852 years.
- C: The recorded output is 1,711 years.
- D: It is "a division," not a measurement.
- E: At 150 wpm it is 2,852 years.

**Source:** Scale, in units you can check

## MA-ch01.22

Check each statement that is true about the compute comparison. Each statement is worth 1 point (5 points total).

- [ ] A. A reader who cannot tell the two sentences apart cannot audit either.
- [ ] B. 3.2 x 10^24 operations is about the same as GPT-3's reported budget.
- [ ] C. The "over 100 million years" claim requires roughly 3.2 x 10^24 operations.
- [ ] D. The "over 100 million years" claim and the 9.95-million-year claim are the same claim about the same model.
- [ ] E. At one billion operations per second by hand, GPT-3's reported training compute would take about 9.95 million years.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The chapter says so.
- B: It is about ten times GPT-3's budget.
- C: That budget gives over 100 million years.
- D: They are claims about different models.
- E: This is the chapter's computed figure.

**Source:** Scale, in units you can check

## MA-ch01.23

Check each statement that is true about the transformer and the two jobs inside a prediction step. Each statement is worth 1 point (5 points total).

- [ ] A. A feed-forward network takes each token's context-informed vector and moves it toward scores for the next token.
- [ ] B. Attention and the feed-forward network are fitted with two separate objectives.
- [ ] C. Self-attention is the learned part that gives each token its context.
- [ ] D. Earlier models walked through text one position at a time, while a transformer takes the whole context at once.
- [ ] E. Someone wrote down what attention should look for.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That is the prediction job.
- B: Both are fitted together by the single next-token objective.
- C: Attention decides which other tokens to read from.
- D: Parallelism is the relevant property here.
- E: Those weights came out of the fit, like every other parameter.

**Source:** Inside one prediction step

## MA-ch01.24

Check each statement that is true about the chapter's caution on Figure 1.4a ("Two learned parts on one stream"). Each statement is worth 1 point (5 points total).

- [ ] A. PaLM uses what its authors call parallel layers.
- [ ] B. In the paper's design, "in parallel" means the two parts compute simultaneously within a layer.
- [ ] C. Each sub-layer is wrapped in a residual connection, so its output is added to its input.
- [ ] D. In the paper's design, inside each layer attention comes first and the feed-forward network second.
- [ ] E. The chapter claims that Claude uses the parallel arrangement.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The chapter names PaLM as a later model that does this.
- B: Read it as two learned components sharing one stream, not simultaneous computation.
- C: Each sub-layer is wrapped in a residual connection, so its output is added to its input.
- D: This is the order described for the paper.
- E: The chapter makes no claim about any deployed model, Claude included.

**Source:** Inside one prediction step

## MA-ch01.25

Check each statement that is true about queries, keys, and values. Each statement is worth 1 point (5 points total).

- [ ] A. The token's new vector is the weighted mix of the keys.
- [ ] B. Every token produces a query, a key, and a value.
- [ ] C. Dividing by the square root of the key length keeps the scores from growing so large that the softmax saturates.
- [ ] D. A softmax turns the comparison scores into weights that sum to one.
- [ ] E. A token's query is compared with the key of every token it is allowed to see.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: It is the weighted mix of the values.
- B: This is the paper's formulation.
- C: That is the role of the scaling term.
- D: It is the same normalization Part 2 builds by hand.
- E: A close match scores high.

**Source:** Self-attention: each token chooses what to read from

## MA-ch01.26

Check each statement that is true about the `bank` attention table. Each statement is worth 1 point (5 points total).

- [ ] A. The weights in the table were measured from a real model.
- [ ] B. Each row of weights sums to one.
- [ ] C. In "She sat by the river bank," `bank` puts the most weight on `river` (0.60).
- [ ] D. Different neighbors give `bank` different weights, so the vector that leaves attention differs between the two sentences.
- [ ] E. In "She paid at the savings bank," `bank` puts the most weight on `savings` (0.55).

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The numbers "are constructed to show the idea, not measured from any model."
- B: Both rows sum to 1.00.
- C: Highlighted weight in the first row.
- D: Same token, different neighbors, different weights.
- E: Highlighted weight in the second row.

**Source:** Self-attention: each token chooses what to read from

## MA-ch01.27

Check each statement that is true about the three precise points the chapter makes on attention. Each statement is worth 1 point (5 points total).

- [ ] A. What is learned is the set of projections that produce queries, keys, and values.
- [ ] B. The attention weights in the table are stored in the model.
- [ ] C. In the paper's encoder, every token can read every other.
- [ ] D. A token that is generating text reads only itself and the tokens before it.
- [ ] E. The original runs eight attention functions in parallel, called heads.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Projections are the learned part.
- B: Weights are recomputed for each new input.
- C: The masking applies in the decoder, not the encoder.
- D: The decoder masks later positions.
- E: Each head has its own learned projections.

**Source:** Self-attention: each token chooses what to read from

## MA-ch01.28

Check each statement that is true about direct access in attention and what an attention weight shows. Each statement is worth 1 point (5 points total).

- [ ] A. An attention weight shows why the model answered as it did.
- [ ] B. Direct access is what let the paper's model do without recurrence and convolution.
- [ ] C. A heat map of attention is a hypothesis to test, not an explanation.
- [ ] D. The first token and the hundredth are one comparison apart.
- [ ] E. Distance weakens the link in attention the way it does in a model that reads one position at a time.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A weight shows where one head read, not why the model answered.
- B: The chapter cites the paper (section 3.5).
- C: The chapter's warning.
- D: Every visible token is compared directly with the current one.
- E: Distance does not weaken the link in the same way.

**Source:** Self-attention: each token chooses what to read from

## MA-ch01.29

Check each statement that is true about the feed-forward network. Each statement is worth 1 point (5 points total).

- [ ] A. It is applied to each token's vector separately and identically.
- [ ] B. In the paper's base model, the vector has 512 numbers and the hidden layer has 2,048.
- [ ] C. The ReLU sets every positive value to zero.
- [ ] D. It lets tokens exchange information with each other.
- [ ] E. It is two linear transformations with a ReLU between them.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: It is position-wise.
- B: Those are the base-model sizes given.
- C: It sets every negative value to zero.
- D: Attention already did that; this layer never lets tokens talk.
- E: FFN(x) = max(0, xW1 + b1)W2 + b2.

**Source:** The feed-forward network: an ordinary neural network

## MA-ch01.30

Check each statement that is true about the chapter's toy feed-forward example. Each statement is worth 1 point (5 points total).

- [ ] A. After the ReLU, the hidden values are [3, 5, 0, 0, 6, 3, 0, 0].
- [ ] B. Because the same weights run on every position, this layer is how tokens talk to each other.
- [ ] C. The hidden layer has four numbers.
- [ ] D. The output has eight numbers, one per hidden value.
- [ ] E. The weights were fitted to data.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The raw hidden values are [3, 5, 0, -1, 6, 3, -3, -2], and the four non-positive ones become zero.
- B: The same weights run on every position separately, so tokens never talk here.
- C: The input has four numbers; the hidden layer has eight.
- D: The output is (8, 7, 5, -1): four numbers, the size of the input.
- E: "They are not fitted"; the weights were chosen to make the arithmetic visible.

**Source:** The feed-forward network: an ordinary neural network

## MA-ch01.31

Check each statement that is true about putting the pieces together. Each statement is worth 1 point (5 points total).

- [ ] A. The vector for `bank` after `river` ends up somewhere different from the vector for `bank` after `savings`.
- [ ] B. Each token stays as text during the pass, because the fitting procedure works on text.
- [ ] C. Attention and the feed-forward layer are applied once and not repeated.
- [ ] D. The normalization that turns scores into a distribution is out of reach at the toy scale.
- [ ] E. The vector at the final position becomes one score per vocabulary token, and those scores are normalized into a distribution.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Attention revises vectors by context.
- B: Each token becomes a list of numbers, because the fitting procedure only works on continuous values.
- C: Both operations repeat, layer after layer.
- D: The final arrow is in reach; Part 2 builds it.
- E: That is the end of the pass.

**Source:** Putting the pieces together

## MA-ch01.32

Check each statement that is true about explaining a model's behavior. Each statement is worth 1 point (5 points total).

- [ ] A. "The model decided X because Y" is, absent interpretability evidence, a measurement of the system.
- [ ] B. Researchers designed the operations, not the behavior.
- [ ] C. A fluent self-explanation from Claude can be treated as a trace of what happened.
- [ ] D. The builders can read off why a particular prediction was made by inspecting the parameters.
- [ ] E. Claude will tell such stories fluently if you ask it to explain its own answer.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: It is "a story about a system rather than a measurement of one."
- B: Behavior emerges from how the parameters were fitted.
- C: Treat such explanations as hypotheses to test, never as a trace.
- D: "Nobody, including its builders, can read off why a particular prediction was made."
- E: The chapter warns that it will.

**Source:** Putting the pieces together

## MA-ch01.33

Check each statement that is true about the stochastic parrot argument. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter settles the dispute in favor of the critics.
- [ ] B. "It's just autocomplete" is a stronger claim than the paper's.
- [ ] C. The argument comes from Bender, Gebru, McMillan-Major, and Shmitchell, and says a model stitches together linguistic form with no access to meaning.
- [ ] D. The conceptual half holds that meaning is a relation between form and something outside language.
- [ ] E. The empirical half is the claim that meaning cannot be reached by a system trained on form alone.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: "This book does not settle it."
- B: The phrase is weaker than the paper's claim.
- C: This is the outline of the claim.
- D: This is the conceptual half (Bender and Koller).
- E: That is the conceptual half; the empirical half concerns consequences such as training costs, unauditable corpora, and unearned trust.

**Source:** Stochastic parrots

## MA-ch01.34

Check each statement that is true about how the chapter treats the stochastic parrot dispute. Each statement is worth 1 point (5 points total).

- [ ] A. Critics say the conceptual half settles by stipulation what ought to be investigated.
- [ ] B. Defenders reply that internal structure is not grounded reference.
- [ ] C. Systems that merely replayed observed sequences would still generalize to strings absent from training.
- [ ] D. Critics cite probing work suggesting that internal representations track non-linguistic structure.
- [ ] E. The chapter asks you to take a position on machine understanding in order to accept its main claim.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The critics' complaint.
- B: The defenders' reply.
- C: Such systems "would not generalize," yet these demonstrably do.
- D: The critics' evidence.
- E: "You do not need a position on machine understanding."

**Source:** Stochastic parrots

## MA-ch01.35

Check each statement that is true about the version of the claim this chapter stands behind. Each statement is worth 1 point (5 points total).

- [ ] A. What you need first is a settled verdict on whether Claude understands.
- [ ] B. You need a position on machine understanding to accept the claim.
- [ ] C. The mechanism ranks continuations, and ranking a continuation highly is not evidence that it is true.
- [ ] D. You must believe Claude is hollow in order to check its work.
- [ ] E. An answer key is not among the arguments of the transformation that turns scores into probabilities.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: What you need is a gate before it runs and a check after.
- B: No such position is needed.
- C: This is the stated claim.
- D: You need not believe Claude is hollow to check its work.
- E: Look at the inputs and notice no answer key is among them.

**Source:** Stochastic parrots

## MA-ch01.36

Check each statement that is true about what Part 1 gives you and what it leaves open. Each statement is worth 1 point (5 points total).

- [ ] A. The parameters and architecture changed between two runs of the same question.
- [ ] B. Roles are text rather than modes.
- [ ] C. Attention supplies the prediction while the feed-forward network supplies the context.
- [ ] D. Part 1 already explains why the same question gets different answers on two runs.
- [ ] E. Training targets a key of correct answers.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The parameters and architecture did not change; something else moved, which Part 2 isolates.
- B: Part 1 lists this among the things you can now say.
- C: Swapped: attention supplies context and the feed-forward network supplies prediction.
- D: "You cannot yet say what this implies about the variation you observe."
- E: Training targets observed text and rater preference rather than truth.

**Source:** What Part 1 gives you, and what it leaves with you

## MA-ch01.37

Check each statement that is true about the design of the Part 2 experiment and what it may claim. Each statement is worth 1 point (5 points total).

- [ ] A. The constructed scores are [1, 2, 3].
- [ ] B. These choices were produced by a model.
- [ ] C. A failure sentence written after reading the output describes the output rather than testing your understanding.
- [ ] D. The experiment may claim that the outcome with the highest probability is correct.
- [ ] E. The temperatures are 0.5, 1, and 2, with a sample of 1,000 draws and seed 7.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Part of the stated design.
- B: "These are my choices; no model produced them."
- C: Write it before, and date it.
- D: The experiment gives a distribution over three indices and counts of draws; "it cannot say that any outcome is correct."
- E: Those are the stated choices.

**Source:** The gate: write the experiment before you run it

## MA-ch01.38

Check each statement that is true about the contract in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. Equal scores get equal probabilities.
- [ ] B. The function accepts a temperature of zero.
- [ ] C. Sampling with the same seed repeats.
- [ ] D. A larger score never gets a smaller probability at positive temperature.
- [ ] E. Probabilities are nonnegative and sum to one.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The contract says equal scores get equal probabilities.
- B: The function refuses an empty list, a nonfinite score, and a zero, negative, or nonfinite temperature.
- C: The contract ends with: sampling with the same seed repeats.
- D: Ordering is preserved.
- E: The contract begins: probabilities are nonnegative and sum to one.

**Source:** The gate: write the experiment before you run it

## MA-ch01.39

Check each statement that is true about the wrong versions your tests must catch and about Claude's role in the gate. Each statement is worth 1 point (5 points total).

- [ ] A. If your tests cannot tell the wrong versions from the right program, the gate is nonetheless finished.
- [ ] B. Claude can write the gate for you without defeating its purpose.
- [ ] C. If you pair the probabilities with the wrong labels, the sum is still one.
- [ ] D. Claude can sharpen the gate.
- [ ] E. If you reinitialize the generator on every draw, one repeatability test might still pass.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: If your tests cannot tell the wrong versions from the right program, "the gate is not finished."
- B: The gate is where your understanding goes on the record.
- C: A sum check alone does not catch mislabeled probabilities.
- D: The chapter says so.
- E: A fresh generator each draw can still repeat.

**Source:** The gate: write the experiment before you run it

## MA-ch01.40

Check each statement that is true about why [1, 2, 3] is not yet three chances. Each statement is worth 1 point (5 points total).

- [ ] A. The list expresses an ordering in which the third entry is largest.
- [ ] B. Dividing scores by their sum would fail on negative scores.
- [ ] C. The scores sum to six.
- [ ] D. Dividing each score by six is the transformation implemented in the lesson.
- [ ] E. The list already expresses chances.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It is an ordering.
- B: The chapter says so.
- C: 1 + 2 + 3 = 6.
- D: That would be a different transformation.
- E: "It does not yet express chances."

**Source:** Three scores are not yet three chances

## MA-ch01.41

Check each statement that is true about the softmax formula and what it guarantees. Each statement is worth 1 point (5 points total).

- [ ] A. Changing a positive temperature can make a smaller score the largest probability.
- [ ] B. The probability of outcome i is the exponential of z_i divided by T, divided by the sum of the same quantity over all outcomes.
- [ ] C. For positive T, the ordering of the scores survives the transformation.
- [ ] D. If an implementation gives the smallest score the largest probability, the ordering prediction gives you a reason to suspect an error such as negated score differences.
- [ ] E. The probabilities summing to one shows that the inputs were sensible and the outcome labels true.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: It changes concentration but cannot do that.
- B: This is the displayed formula.
- C: Dividing by T and exponentiating preserve order; the total is shared.
- D: An explanation becomes a debugging instrument.
- E: It is a statement about the transformation, not about the inputs or labels.

**Source:** Three scores are not yet three chances

## MA-ch01.42

Check each statement that is true about the shifted scores for [1, 2, 3] at temperature one. Each statement is worth 1 point (5 points total).

- [ ] A. Subtracting the maximum changes the intended distribution.
- [ ] B. The weights are approximately 0.135335, 0.367879, and 1.
- [ ] C. The weights sum to approximately 1.503215.
- [ ] D. After subtracting the maximum, the largest exponent is zero, so its exponential is one.
- [ ] E. The shifted scores are [-2, -1, 0].

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: "We have changed the intermediate weights, not the intended distribution."
- B: exp(-2), exp(-1), exp(0).
- C: 0.135335 + 0.367879 + 1.
- D: The largest exponent becomes zero and the others are no larger than one.
- E: Subtract the maximum, 3.

**Source:** The subtraction that changes nothing important

## MA-ch01.43

Check each statement that is true about why subtracting the maximum is allowed. Each statement is worth 1 point (5 points total).

- [ ] A. The test file proves that every numeric input is handled.
- [ ] B. The large shared offset carries information about relative preference.
- [ ] C. The common factor exp(-m/T) cancels between numerator and denominator.
- [ ] D. For equal large scores [1000, 1000], the lesson expects [0.5, 0.5].
- [ ] E. The computer needs large intermediate exponentials in order to express a ratio.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: It is "evidence for this concrete case, not a proof."
- B: It carries no information about relative preference.
- C: That is the algebra.
- D: Shifting gives [0, 0], then [1, 1], then [0.5, 0.5].
- E: "The computer does not need large intermediate exponentials to express a ratio."

**Source:** The subtraction that changes nothing important

## MA-ch01.44

Check each statement that is true about the input checks and the sum check. Each statement is worth 1 point (5 points total).

- [ ] A. A negative temperature is harmless because it leaves the ordering alone.
- [ ] B. A function is partly defined by what it refuses to compute.
- [ ] C. The sum check should use exact equality, because the arithmetic is exact.
- [ ] D. A sum close to one shows that the ordering is right.
- [ ] E. Claude writes the boundary checks unprompted, even if your gate does not demand them.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A negative temperature would reverse the ordering.
- B: The chapter states this.
- C: Floating-point arithmetic has limits, so the check uses approximate equality.
- D: It shows one property only; it does not show ordering, equal-score handling, rejection, or sampling.
- E: Claude writes the happy path unprompted and the boundary only if your gate demands it.

**Source:** The subtraction that changes nothing important

## MA-ch01.45

Check each statement that is true about the probability ratio between two outcomes. Each statement is worth 1 point (5 points total).

- [ ] A. The ratio of p_i to p_k equals exp of (z_i - z_k) divided by T.
- [ ] B. A larger T brings the ratio closer to one.
- [ ] C. Normalization cancels out of the ratio.
- [ ] D. If z_i exceeds z_k, a smaller positive T increases the ratio.
- [ ] E. Temperature changes the ordering of the outcomes.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: This is the displayed ratio.
- B: A larger T shrinks the exponent toward zero.
- C: The shared total divides out.
- D: A smaller T makes the exponent larger.
- E: The transformation changes relative concentration, not ordering.

**Source:** Temperature is a concentration control, not a fact checker

## MA-ch01.46

Check each statement that is true about the temperature table for scores [1, 2, 3]. Each statement is worth 1 point (5 points total).

- [ ] A. At T = 2, outcome 2 is no longer the favorite.
- [ ] B. At T = 0.5, outcome 2 receives about 0.867.
- [ ] C. Outcome 0 receives more probability at T = 0.5 than at T = 2.
- [ ] D. Predicting only which outcome wins captures most of what the experiment shows.
- [ ] E. At T = 2, outcome 2 receives about 0.506.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The largest score remains the favorite throughout.
- B: 0.8668133322.
- C: It receives 0.0159 at T = 0.5 and 0.186 at T = 2.
- D: The winner stays the same, so predicting it misses most of the experiment.
- E: 0.5064803911.

**Source:** Temperature is a concentration control, not a fact checker

## MA-ch01.47

Check each statement that is true about the chapter's hypothetical in which the independently checked answer is label zero. Each statement is worth 1 point (5 points total).

- [ ] A. In the hypothetical, the transformation fails to work as designed.
- [ ] B. Temperature is a concentration control, not a fact checker.
- [ ] C. No change in concentration can supply information the program never receives.
- [ ] D. Lowering temperature concentrates selection on label two, which is wrong under the stipulated answer key.
- [ ] E. The chapter reports the hypothetical as an observed Claude error.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The transformation works as designed; the failure is treating its preference as a truth guarantee.
- B: This is the section's heading.
- C: The program never receives an answer key.
- D: Label two has the largest score.
- E: "Do not report this as an observed Claude error."

**Source:** Temperature is a concentration control, not a fact checker

## MA-ch01.48

Check each statement that is true about the sampling function. Each statement is worth 1 point (5 points total).

- [ ] A. The probability function returns a recipe for selection, not a thousand outcomes.
- [ ] B. The count changes how many observations you collect.
- [ ] C. The selected choices are outcome indices, not logit values.
- [ ] D. The sampler creates a local pseudorandom generator.
- [ ] E. The seed changes the weights.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Sampling is a separate function.
- B: Count is the number of draws.
- C: The indices are the outcomes.
- D: It builds a generator from the seed.
- E: Temperature changes the weights; the seed changes the selected sequence.

**Source:** A distribution is not the sample you happened to see

## MA-ch01.49

Check each statement that is true about expected and observed counts at temperature one for outcome two. Each statement is worth 1 point (5 points total).

- [ ] A. The observed share is 0.63, against an assigned probability of about 0.66524, and both numbers belong in the report.
- [ ] B. The observed counts are exact expressions of the theoretical probabilities.
- [ ] C. The observed count in the saved seed-seven run is 630.
- [ ] D. The expected count over 1,000 draws is about 665.24.
- [ ] E. An expected count of 665.24 could itself be an observed count.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: They answer different questions: assigned chance and observed fraction.
- B: They are "evidence of the recorded executions, not exact expressions."
- C: Recorded in the counts table.
- D: 1,000 times 0.6652409558.
- E: A count is an integer.

**Source:** A distribution is not the sample you happened to see

## MA-ch01.50

Check each statement that is true about the counts table (T = 0.5: 18, 133, 849; T = 1: 102, 268, 630; T = 2: 202, 329, 469). Each statement is worth 1 point (5 points total).

- [ ] A. Outcome 2's count falls as temperature rises from 0.5 to 2.
- [ ] B. At T = 1, outcome 0's count is exactly 90, which is 1,000 times its probability.
- [ ] C. Each row of counts totals 1,000.
- [ ] D. The outcome with the highest score had the highest count at all three temperatures.
- [ ] E. Outcome 0's count rises as temperature rises from 0.5 to 2.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: 849, then 630, then 469.
- B: The count is 102, not 90; sampling gives a count, not 1,000 times the probability.
- C: Each row sums to 1,000.
- D: 849, 630, and 469 are the largest in their rows.
- E: 18, then 102, then 202.

**Source:** A distribution is not the sample you happened to see

## MA-ch01.51

Check each statement that is true about reading a gap between assigned and observed proportions, and about the returned dictionary. Each statement is worth 1 point (5 points total).

- [ ] A. Before calling the sampler broken because of one gap, you need an acceptance criterion appropriate to the experiment.
- [ ] B. The existing reproducibility test checks agreement with every theoretical proportion.
- [ ] C. The existing reproducibility test checks that the same call returns the same counts.
- [ ] D. A missing key in the returned dictionary means no recorded selections.
- [ ] E. A missing key means the outcome was removed from the probability model.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Do not pronounce the sampler broken from one gap.
- B: The test does not check that.
- C: That is repeatability.
- D: Retrieve missing counts as zero.
- E: Not selected is not the same as not possible.

**Source:** A distribution is not the sample you happened to see

## MA-ch01.52

Check each statement that is true about the seed. Each statement is worth 1 point (5 points total).

- [ ] A. A seed gives the sample factual status.
- [ ] B. Reproducibility establishes correctness.
- [ ] C. A result you can reproduce on demand is still only as true as what produced it.
- [ ] D. A seed lets you return to a particular experiment while debugging.
- [ ] E. If a fixed sequence repeatedly selects the hypothetically wrong label, repeatability preserves the mistake.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It gives "no factual status."
- B: Repeatable does not mean true.
- C: This is the fluent wrong answer in miniature.
- D: That is its use.
- E: The seed repeats whatever was selected.

**Source:** A distribution is not the sample you happened to see

## MA-ch01.53

Check each statement that is true about the four first prompts as a group. Each statement is worth 1 point (5 points total).

- [ ] A. You should save only the final answer, without the date or the displayed model label.
- [ ] B. A remembered summary may stand in for a transcript.
- [ ] C. Prompt 1 should be sent four times in a single conversation.
- [ ] D. Claude does not expose a seed to you.
- [ ] E. Each prompt changes several variables at once so that you see the whole system.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Save the actual responses with the date and displayed model label.
- B: Never substitute a remembered summary for a transcript.
- C: Use four separate new conversations; the transcript grows and changes the input.
- D: So you run the comparison you can run.
- E: Each prompt isolates one variable and produces a record you can keep.

**Source:** First prompts: the same experiment, one floor up

## MA-ch01.54

Check each statement that is true about prompts 1 and 2 (the shuffled deck and the capital of Australia). Each statement is worth 1 point (5 points total).

- [ ] A. Prompt 2 is the closest thing you have to lowering temperature without a temperature control.
- [ ] B. Prompt 1 is the counts table, one level up.
- [ ] C. Convergence in prompt 2 makes the answer more true.
- [ ] D. In prompt 1, you note what is stable (roughly the claim) and what moves (examples, hedges, clause order).
- [ ] E. In prompt 2, a constrained format leaves fewer high-probability continuations, so the answers converge.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The chapter says so.
- B: The chapter says so.
- C: It made the answer "more repeatable and no more true."
- D: That is what to record.
- E: That explains the smaller spread.

**Source:** First prompts: the same experiment, one floor up

## MA-ch01.55

Check each statement that is true about prompt 3 (fluency without support). Each statement is worth 1 point (5 points total).

- [ ] A. The response was fluent and well-formed whatever you find when you check the citation.
- [ ] B. You are expected to check the citation yourself.
- [ ] C. It asks for one specific quantitative finding from a peer-reviewed spaced-repetition paper, with authors, year, and exact number.
- [ ] D. Claude can be the independent check on its own citation.
- [ ] E. Confidence was one of the inputs to the ranking machinery.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Fluency does not depend on support.
- B: "Now check the citation yourself."
- C: That is the prompt.
- D: The process that made the citation would be vouching for it.
- E: "Confidence was never one of its inputs."

**Source:** First prompts: the same experiment, one floor up

## MA-ch01.56

Check each statement that is true about prompt 4 (Claude as a reviewer of your reasoning). Each statement is worth 1 point (5 points total).

- [ ] A. Withholding the verdict is deliberate: you want the boundary case, not the grade.
- [ ] B. You use it once you have written your own prediction.
- [ ] C. The prompt asks Claude to tell you whether you are right.
- [ ] D. Claude decides whether your reasoning is sound.
- [ ] E. The prompt asks Claude to name the assumption your reasoning depends on most and describe an input that would make it fail.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The chapter says so.
- B: The prediction comes first.
- C: It says "Do not tell me whether I am right."
- D: "It challenges; you decide."
- E: That is the request.

**Source:** First prompts: the same experiment, one floor up

## MA-ch01.57

Check each statement that is true about Build It and Use It. Each statement is worth 1 point (5 points total).

- [ ] A. The difference to name between your version and the reference is one of line count or style.
- [ ] B. You write your implementation in the learner workspace before opening the reference solution.
- [ ] C. A failing test is often a gap in your gate, which Claude cannot see because it only has what you wrote.
- [ ] D. When using Claude Code, you give it the gate (contract and test list), not your implementation.
- [ ] E. You run your tests on what Claude returns, yourself.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Name "a difference in behavior, not in line count or style."
- B: Your own version is the baseline.
- C: The gate is all Claude has.
- D: Claude should work from the gate alone.
- E: The check is yours.

**Source:** Build It: the baseline that lets you audit; Use It: conduct Claude Code against your gate

## MA-ch01.58

Check each statement that is true about the sampling report. Each statement is worth 1 point (5 points total).

- [ ] A. It begins with the prediction you wrote before running, preserved even if wrong.
- [ ] B. A report that quietly replaces the prediction with the correct answer destroys the comparison that makes the exercise informative.
- [ ] C. Its value is that another reader can connect the table to inputs, code, execution conditions, and a claim.
- [ ] D. The Claude transcripts from the first-prompts experiment go in the same table as the sampling results.
- [ ] E. A missing link can let a polished presentation conceal an experiment that is difficult to interpret.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The prediction goes first.
- B: Preserve the original prediction.
- C: The report's purpose.
- D: Keep them "as a separate record."
- E: The chapter says so.

**Source:** Ship It: a report that survives a skeptical reader

## MA-ch01.59

Check each statement that is true about the reviewer who sees an outcome-two count of 849. Each statement is worth 1 point (5 points total).

- [ ] A. Correctness would need an answer key or a source check tied to a meaningful claim.
- [ ] B. The suggested claim says that decreasing temperature from two to one-half concentrated the assigned probability on the largest score.
- [ ] C. 849 proves the answer is correct.
- [ ] D. 849 is a count of an index selected in a constructed experiment.
- [ ] E. The suggested claim treats the sample counts as the same thing as the assigned probabilities.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: That is the missing evidence.
- B: That is the quoted claim.
- C: It proves nothing about correctness.
- D: It is an index count in a constructed run.
- E: The claim says the counts are "recorded separately."

**Source:** Ship It: a report that survives a skeptical reader

## MA-ch01.60

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. The "Not checked" line does the work, and an AI-written sign-off never includes it because the system has no record of what you did not do.
- [ ] B. The template has the lines Checked, How, Not checked, Not claiming, and Signed or withheld.
- [ ] C. If your evidence does not support signing, withholding is an honest result.
- [ ] D. You may adopt Claude's fluent draft instead of writing the sign-off from your own record.
- [ ] E. The "Not claiming" line states that the experiment models a Claude setting.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The chapter says so.
- B: Those are the template lines.
- C: The chapter says so.
- D: Claude can draft words in seconds, but you write it from your record.
- E: It says you are not claiming that.

**Source:** Ship It: a report that survives a skeptical reader

## MA-ch01.61

Check each statement that is true about the driver's-seat table. Each statement is worth 1 point (5 points total).

- [ ] A. For explaining a surprising output, Claude proposes hypotheses and you test each against the code and the input.
- [ ] B. For saying what the result supports, Claude chooses the verb and signs.
- [ ] C. For a first implementation, Claude implements first and you build your own baseline afterward.
- [ ] D. For the contract and the test list, you write them first and Claude challenges them.
- [ ] E. For the arithmetic of a derivation, Claude computes and you name the assumption the number hides.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: An explanation from the system under test is a story, not a trace.
- B: You choose the verb and sign; Claude flags an overclaim.
- C: You build your own baseline first.
- D: The contract is your understanding on the record.
- E: A number does not say what it assumed.

**Source:** The driver's seat

## MA-ch01.62

Check each statement that is true about the next boundary and the end-of-chapter summary. Each statement is worth 1 point (5 points total).

- [ ] A. The sampler can reject an answer that claims the source says red when the source says blue.
- [ ] B. Structure earns its place by rejecting specific failures; the mistake is asking it to reject failures it was never written to recognize.
- [ ] C. The toy is not a metaphor for the last step of a real model; it is that step, at a scale you can print.
- [ ] D. Chapter 2 builds a contract around an answer, with required fields, types, source identifiers, and an evaluation set.
- [ ] E. Chapter 2 adds the question of exactly which obligation the program passed when it said an answer passed.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The sampler never receives the source's meaning as a condition to check.
- B: The chapter says so.
- C: The chapter says so.
- D: That is the plan for Chapter 2.
- E: That is the question Chapter 2 adds.

**Source:** What you can now explain; The next boundary

## MA-ch01.63

Check each statement that is true about the Computational Skepticism and Irreducibly Human notes. Each statement is worth 1 point (5 points total).

- [ ] A. The note claims that the chapter ran a calibration study.
- [ ] B. "Human should" be required to type every character unaided.
- [ ] C. "AI should" write your initial prediction for you.
- [ ] D. In this chapter the probabilities concern selection among constructed indices, not the chance that an answer is true.
- [ ] E. You should state the event to which a probability refers, and not replace "the sampler selects outcome two" with "outcome two is correct."

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It "contributes an auditing question, not a claim that we ran a calibration study."
- B: "The protected work is not typing every character unaided."
- C: AI "should not invent your initial prediction."
- D: The chapter says so.
- E: That is the exercise the note sets.

**Source:** Computational Skepticism; Irreducibly Human
