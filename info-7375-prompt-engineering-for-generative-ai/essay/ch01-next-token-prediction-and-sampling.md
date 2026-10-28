# Chapter 1: Next-token prediction and sampling

## ES-ch01.1

You ask Claude the same question twice. The first answer is short; the second has a different example, a different qualification, and perhaps a different conclusion. A colleague says, "The prompt was vague." In a short paragraph, explain what has and has not been established at this point, and what Claude's own fluent explanation of the difference can and cannot contribute.

**Points:** 5

**Rubric (1 point each):**

1. States that a difference between two outputs has been observed.
2. States that the cause (the moving part) has not been isolated, and that labels such as "the prompt was vague," "the model was creative," or "the system was unreliable" do not identify it.
3. Notes that Claude can write a fluent, confident account of why the answers differed, and that the account may even be right.
4. Notes that Claude cannot check its own account against the machinery, or know which moving part you needed to isolate.
5. Concludes that the account is a hypothesis for the human to test, not a result.

**Source:** Opening (before "What you will be able to do")

## ES-ch01.2

State the chapter's argument in brief: what Claude is better at than you, what it lacks, and which three jobs stay with you. Explain each job in one phrase.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude is far better at producing fluent text, working code, and long lists of plausible candidates, at a speed and volume no person matches, so you should not compete with it there.
2. Says Claude has no stake in whether its output is true and no way to tell you whether it is the thing you needed.
3. Names the three jobs as conduct, check, and drive.
4. Explains conduct and check correctly: decide where Claude goes before it runs, and check what comes back.
5. Explains drive as signing your name to what you keep (owning the decision and the split of work).

**Source:** Opening (before "What you will be able to do")

## ES-ch01.3

The chapter says "a score is not a probability, a probability is not an observed frequency, and an observed frequency is not a correctness judgment." Give one concrete example from the Part 2 experiment for each of the three links in that chain.

**Points:** 5

**Rubric (1 point each):**

1. Score versus probability: the scores [1, 2, 3] are an ordering (they sum to six), not chances, and must be transformed before they are probabilities.
2. Probability versus frequency: for example, the assigned probability of about 0.665 for outcome two at temperature one versus the observed 630 of 1,000 (0.63).
3. Frequency versus correctness: a count such as 849 is a count of an index selected in a constructed experiment and says nothing about whether an answer is correct.
4. States that one outcome can be made increasingly likely without adding any evidence that it is correct.
5. States that a run can be made repeatable without making its answer true.

**Source:** Opening (before "What you will be able to do")

## ES-ch01.4

Why does the chapter shrink the machine to three outcomes and three numbers instead of experimenting on Claude directly, and what must you not conclude from the toy?

**Points:** 5

**Rubric (1 point each):**

1. Says the toy is small enough that every intermediate value can be inspected.
2. Says there is nowhere for an unexplained operation to hide.
3. Says the toy will not reproduce Claude, and that this is its advantage.
4. Says the experiment's numbers come from an offline program (no API key, no direct API credits), not from a fabricated conversation with Claude.
5. Says the sign-off should not claim that the experiment models a Claude setting.

**Source:** Opening (before "What you will be able to do"); Ship It: a report that survives a skeptical reader

## ES-ch01.5

Explain the Conduct job. Say what Claude does well and badly, what the human decides, what a gate is, and what a gate contains.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude implements well from a complete specification and badly from an incomplete one, and will not tell you which you gave it.
2. Says the human's job is "not to type less" but "to decide more precisely": design, constraints, and gates.
3. Defines a gate as a specific, testable condition that must hold before an output moves on.
4. Says a gate is written before asking Claude for anything.
5. Lists the gate's contents: what the thing must do, what it must refuse, and the test that would fail a plausible but wrong version.

**Source:** Three jobs that stay yours

## ES-ch01.6

Explain the Check job: why Claude's errors are hard to see, the two habits the chapter prescribes, and why asking Claude to check its own output is not enough.

**Points:** 5

**Rubric (1 point each):**

1. Says Claude's mistakes arrive fluent, so well-formed prose does the work that verification should have done.
2. Names habit one: write down what a wrong answer would look like before reading the output.
3. Says that note must not be revised afterward.
4. Names habit two: keep the check independent of the thing checked.
5. Explains that an AI checking an AI is "the first opinion run twice," so although Claude can run tests and propose counterexamples, your name is on the result.

**Source:** Three jobs that stay yours

## ES-ch01.7

The book is about a tool that writes code faster than you do, yet it asks you to build small things by hand. Explain why, using the chapter's account of the Drive job.

**Points:** 5

**Rubric (1 point each):**

1. Says the purpose is not to out-type Claude.
2. Says building by hand acquires the baseline that makes conducting possible.
3. Cites the line that you cannot audit what you do not know (Irreducibly Human).
4. Describes the split by task: Claude can draft, compute, retrieve, test, and challenge; you choose the question, justify the assumptions, and own the decision.
5. Gives the chapter's sequence: build the small mechanism, write the gate, conduct Claude against it, check what comes back, sign only what the record supports.

**Source:** Three jobs that stay yours

## ES-ch01.8

The chapter calls the car picture "good and incomplete." Explain where the picture works and where it needs a caveat.

**Points:** 5

**Rubric (1 point each):**

1. Says nobody races a car, so you should not compete with Claude at pattern and association work.
2. Says the car does not choose the destination; you do.
3. Says a car's failures are loud (the engine knocks, the dashboard lights up) while Claude's failures are quiet.
4. Says confidence and correctness come from different places, so Claude's confident tone is not evidence of correctness.
5. Says the driver must understand the engine well enough to hear a knock that makes no sound.

**Source:** Three jobs that stay yours

## ES-ch01.9

Describe the loop that turns a machine that continues text into a chatbot, and state what the loop does and does not contain.

**Points:** 5

**Rubric (1 point each):**

1. Describes the loop: feed in the text so far, take a candidate for the next fragment, append it, feed the longer text back, and repeat until the machine proposes an ending.
2. Says no component answers your question; one component repeatedly answers what plausibly comes next in this text.
3. Says nothing in the loop reads a document, checks an answer key, or knows whether the growing text is true.
4. Says retrieval, tools, permissions, and approval gates arrive later as attempts to supply what the loop lacks.
5. Says every one of those attempts is something you design and then check.

**Source:** The unfinished script

## ES-ch01.10

Using the chapter's illustrative table (Unbelievably, Paris, costs, 1,200, euros), explain what a token is and why a request for an exact character count is awkward for the machine.

**Points:** 5

**Rubric (1 point each):**

1. Says the machine predicts tokens, which are fragments from a fixed vocabulary, not words.
2. Says a common word may be one token and a rare word several (for example `unbelievable` in three pieces).
3. Says a space is usually part of the token that follows it, and that numbers and punctuation split too (for example, 1,200 splits into three tokens: the digit 1, a comma, and 200).
4. Says the five words became eleven tokens and that the split is illustrative, not the output of any particular tokenizer.
5. Says a character count asks the machine to reason about a unit it does not natively see.

**Source:** One question, asked over and over

## ES-ch01.11

Describe what goes into and what comes out of one prediction step, including what an embedding is and what is (and is not) excluded from the output.

**Points:** 5

**Rubric (1 point each):**

1. Says each vocabulary entry selects a vector of learned numbers (an embedding), and that operations after that work on vectors.
2. Says the output is a number for every token in the vocabulary (tens of thousands), not a single token.
3. Says the numbers are nonnegative and sum to one.
4. Says every candidate gets a share, including absurd ones; nothing is excluded, things are merely ranked.
5. Says what is predicted at each step is one token, not a word or a fact (a word spanning three tokens takes three steps).

**Source:** One question, asked over and over

## ES-ch01.12

A model gives `Paris` a high probability after `The capital of France is`. A student says the model "looked it up in an atlas." Explain what the number actually reports and why its agreement with an atlas is not a guarantee for the next case.

**Points:** 5

**Rubric (1 point each):**

1. Says the distribution ranks continuations of a string.
2. Says its shape was fixed by fitting parameters to a body of text.
3. Says the number reports how the phrase tends to continue in the corpus the model was fit to.
4. Says it is not the output of a lookup against an atlas.
5. Says the agreement is a fact about the corpus, not a mechanism that guarantees agreement in the next case (the chapter's load-bearing distinction).

**Source:** One question, asked over and over

## ES-ch01.13

The chapter shows a chat as `System:`, `User:`, and `Assistant:` lines. Explain how a model that only continues text can hold a conversation, and give the two consequences the chapter draws.

**Points:** 5

**Rubric (1 point each):**

1. Says the model is handed a single string with role markers that looks like a conversation.
2. Says the most plausible continuation of a string ending in `Assistant:` is an assistant-sounding reply, and that roles are text, not modes.
3. Consequence one: a system prompt is a request, not a gate; it competes with every other paragraph in the document.
4. Says enforcement of a rule that matters belongs in the runtime that wraps the model (permissions in code), not in the preamble.
5. Consequence two: the model does not remember your last conversation; the whole transcript is resupplied every turn, so long conversations behave differently.

**Source:** The transcript is the whole trick

## ES-ch01.14

Describe the "continue this text" support-call exercise: what you do before you paste the prompt, what the prompt asks Claude to do, and why the order of steps matters.

**Points:** 5

**Rubric (1 point each):**

1. Says to write down in one sentence what you expect Claude to do, and date it, before pasting.
2. Says the prompt asks Claude not to answer as an assistant but to continue the string as literal text.
3. Describes this as getting the mechanism without the costume.
4. Says to save the result with the exact prompt, the prediction, and the date.
5. Says the later comparison against a normal request is only worth anything if the prediction was written first.

**Source:** The transcript is the whole trick

## ES-ch01.15

Describe how pretraining sets the model's parameters, and say what its objective does and does not contain.

**Points:** 5

**Rubric (1 point each):**

1. Says the parameters (hundreds of billions of values) start random, so the model starts by producing noise, and were never set by hand.
2. Describes the loop: take a passage, hide the next token, get the model's distribution, and compare it with the token that actually followed.
3. Says backpropagation nudges every parameter slightly so the true token gets a little more probability and everything else a little less.
4. Says this is repeated across an enormous corpus.
5. Says nothing in the loop is told what is true; the target is what the corpus did next, so pretraining yields something that completes internet text rather than behaves like an assistant.

**Source:** Where the numbers come from

## ES-ch01.16

Explain what the second training stage targets and why that is not the same as correctness. Say why this is the first reason the checking stays with you.

**Points:** 5

**Rubric (1 point each):**

1. Describes the stage: people are shown candidate replies and asked which they prefer, and those judgments shift the parameters.
2. Says approval and correctness overlap heavily because raters generally prefer accurate answers.
3. Says they are different targets, and where they diverge the training signal follows approval.
4. Gives the example: a confident, well-organized, wrong answer is what a rater who does not know the answer can prefer.
5. Says this follows from the objective (not a scandal about any company's process), and that the machine was shaped to produce what looks right to a reader, who is you.

**Source:** Where the numbers come from

## ES-ch01.17

A speaker says it would take a person thousands of years to read GPT-3's training text. Using 300 billion tokens and 0.75 words per token, work out the number of words and the reading time in minutes at 250 words per minute, and report the chapter's year figures for 250, 200, and 150 words per minute. Then say what the headline figure hides.

**Points:** 5

**Rubric (1 point each):**

1. Computes 225 billion words (300 billion x 0.75).
2. Computes 9 x 10^8 minutes at 250 words per minute (225 billion / 250), about 1,711 years.
3. Reports about 2,139 years at 200 words per minute and about 2,852 years at 150.
4. Says the answer moves by more than a thousand years depending on a reading rate nobody stated, so the headline is a division with a hidden parameter, not a measurement.
5. Says the comparison is still useful as an illustration (more text than a person could read in many lifetimes), and that finding hidden parameters in impressive numbers is a skill the course keeps asking for.

**Source:** Scale, in units you can check

## ES-ch01.18

A speaker says GPT-3's training compute would take "over 100 million years" at one billion operations per second. Using the chapter's figures, evaluate the claim.

**Points:** 5

**Rubric (1 point each):**

1. States GPT-3's reported total training compute as 3.14 x 10^23 floating-point operations (Brown et al.).
2. Says at one billion operations per second that takes about 9.95 million years.
3. Says "over 100 million years" requires roughly 3.2 x 10^24 operations.
4. Says that is about ten times GPT-3's budget (3.2 x 10^24 / 3.14 x 10^23 is about 10.2), plausible for later systems but a different claim about a different model.
5. Says both sentences can be true but are not the same sentence, and a reader who cannot tell them apart cannot audit either.

**Source:** Scale, in units you can check

## ES-ch01.19

Explain what makes the transformer practical at scale, and distinguish the two jobs that self-attention and the feed-forward network each do.

**Points:** 5

**Rubric (1 point each):**

1. Says the transformer takes the whole context at once, while earlier models walked through text one position at a time (parallelism).
2. Says the context job is done by self-attention, which decides for each token which other tokens to read from.
3. Says the prediction job is done by a feed-forward network, which takes each token's context-informed vector and moves it toward scores for the next token.
4. Says both are made of parameters fitted together by the single next-token objective.
5. Says nobody wrote down what attention should look for; those weights came out of the fit like every other parameter.

**Source:** Inside one prediction step

## ES-ch01.20

Figure 1.4a draws attention and the feed-forward network as two learned parts sharing one stream. What caution does the chapter attach to the drawing, and what does it refuse to claim about Claude?

**Points:** 5

**Rubric (1 point each):**

1. Says that in the paper's design, inside each layer, attention comes first and the feed-forward network second.
2. Says each sub-layer is wrapped in a residual connection, so its output is added to its input.
3. Says "in parallel" should be read as two learned components sharing one stream, not as simultaneous computation.
4. Says some later published models (for example PaLM, with "parallel layers") do compute the two side by side.
5. Says the book makes no claim about which arrangement any deployed model, Claude included, uses.

**Source:** Inside one prediction step

## ES-ch01.21

Describe how a token gets context in self-attention, naming the three vectors each token produces and the steps from comparison to new vector.

**Points:** 5

**Rubric (1 point each):**

1. Says every token produces a query, a key, and a value.
2. Says a token's query is compared with the key of every token it is allowed to see, and a close match scores high.
3. Says a softmax turns the scores into weights that sum to one.
4. Says the token's new vector is the weighted mix of the values.
5. Gives or explains the scaling term: dividing by the square root of the key length keeps the scores from growing so large that the softmax saturates.

**Source:** Self-attention: each token chooses what to read from

## ES-ch01.22

Using the chapter's `bank` table, explain how attention gives the same token different vectors in different sentences, and describe what kind of numbers the table contains and where such weights live in a real model.

**Points:** 5

**Rubric (1 point each):**

1. Says in "She sat by the river bank" `bank` puts the most weight on `river` (0.60), and in "She paid at the savings bank" on `savings` (0.55).
2. Says same token, different neighbors, different weights, so the vector leaving attention differs.
3. Says each row of weights sums to one.
4. Says the numbers are constructed to show the idea and were not measured from any model.
5. Says the weights are not stored anywhere; they are recomputed for each new input (what is learned are the projections).

**Source:** Self-attention: each token chooses what to read from

## ES-ch01.23

The chapter adds three precise points about attention and a warning about interpreting it. State them.

**Points:** 5

**Rubric (1 point each):**

1. Says what is learned is the set of projections that produce queries, keys, and values, not the weights in the table.
2. Says a token that is generating text reads only itself and the tokens before it (later positions are masked in the decoder), whereas in the paper's encoder every token can read every other.
3. Says the original runs eight attention functions (heads) in parallel, each with its own learned projections, so a real layer holds many weight tables.
4. Says every visible token is compared directly with the current one, so the first and hundredth tokens are one comparison apart; distance does not weaken the link, which let the paper do without recurrence and convolution.
5. Warns that an attention weight shows where one head read, not why the model answered; a heat map is a hypothesis to test, not an explanation.

**Source:** Self-attention: each token chooses what to read from

## ES-ch01.24

In the chapter's toy feed-forward example (x = [2, -1, 1, 3], a hidden layer of eight numbers), the hidden values before the ReLU are [3, 5, 0, -1, 6, 3, -3, -2]. Give the values after the ReLU, say how many were zeroed, and explain what this layer does and does not do.

**Points:** 5

**Rubric (1 point each):**

1. Gives [3, 5, 0, 0, 6, 3, 0, 0] as the values after the ReLU.
2. Says four of the eight hidden values are not positive, so four become zero (ReLU sets negative values to zero).
3. Says the output is (8, 7, 5, -1): a 4-number vector in, an 8-number hidden layer, and back to 4 numbers.
4. Says the same weights run on every position separately, so this layer never lets tokens talk to each other; attention already did that.
5. Says W1 and W2 are what training adjusts (where patterns from the corpus are stored), while the toy's weights were chosen to make arithmetic visible, not fitted.

**Source:** The feed-forward network: an ordinary neural network

## ES-ch01.25

Walk through the four things that happen in one pass of the model, ending in a distribution over the vocabulary.

**Points:** 5

**Rubric (1 point each):**

1. Says each token becomes a list of numbers, because the fitting procedure only works on continuous values.
2. Says attention lets the lists read each other and revise themselves according to context (`bank` after `river` ends up differently from `bank` after `savings`).
3. Says a feed-forward layer adds patterns stored during training.
4. Says both operations repeat, layer after layer.
5. Says the vector at the final position is turned into one score per vocabulary token, and those scores are normalized into a distribution.

**Source:** Putting the pieces together

## ES-ch01.26

Claude is asked, "Why did you give that answer?" and replies fluently with a reason. What status should you give that reply, and why? Use the chapter's account of how model behavior arises.

**Points:** 5

**Rubric (1 point each):**

1. Says researchers designed the operations, not the behavior.
2. Says behavior emerges from how the parameters were fitted.
3. Says nobody, including the builders, can read off why a particular prediction was made.
4. Says "the model decided X because Y," absent interpretability evidence, is a story about a system rather than a measurement of one.
5. Says to treat Claude's fluent self-explanation as a hypothesis to test, never as a trace of what happened.

**Source:** Putting the pieces together

## ES-ch01.27

Summarize the stochastic parrot argument and its two halves.

**Points:** 5

**Rubric (1 point each):**

1. Attributes the argument to Bender, Gebru, McMillan-Major, and Shmitchell and states the claim: a model stitches together linguistic form according to probabilistic information, with no access to meaning.
2. Says fluency is not comprehension, and that the coherence you perceive is supplied largely by you because humans attribute intent to well-formed text.
3. Describes the conceptual half (Bender and Koller): meaning is a relation between form and something outside language, which a system trained on form alone cannot reach.
4. Describes the empirical half: costs of training at scale, the impossibility of auditing web-scale corpora, and the harms of deploying systems whose fluency invites unearned trust.
5. Says conflating the two halves is the usual mistake.

**Source:** Stochastic parrots

## ES-ch01.28

A classmate dismisses Claude with "it's just autocomplete" and says that settles the stochastic parrot debate. Respond using the chapter's account of the dispute.

**Points:** 5

**Rubric (1 point each):**

1. Gives the critics' view: the conceptual half settles by stipulation what ought to be investigated, and probing work suggests internal representations track non-linguistic structure.
2. Gives the defenders' reply: internal structure is not grounded reference, and the empirical half stands however the philosophy resolves.
3. Says the book does not settle the dispute.
4. Says "it's just autocomplete" is weaker than the paper's claim.
5. Says systems that merely replayed observed sequences would not generalize to strings absent from training, as these demonstrably do.

**Source:** Stochastic parrots

## ES-ch01.29

State the version of the skeptical claim that this chapter stands behind, and explain why you do not need a position on machine understanding to accept it.

**Points:** 5

**Rubric (1 point each):**

1. States that the mechanism ranks continuations, and ranking a continuation highly is not evidence that it is true.
2. Says to look at what the transformation receives as input and notice that an answer key is not among its arguments.
3. Says no position on machine understanding is needed.
4. Says you need not believe Claude is hollow to check its work, nor that it understands to use it.
5. Says what you need is a gate before it runs and a check after.

**Source:** Stochastic parrots

## ES-ch01.30

Part 1 ends by noting that if you ask the same question twice and the answers differ, "something else moved." What did not move, and what does the Part 2 toy show can differ even when the distribution is fixed?

**Points:** 5

**Rubric (1 point each):**

1. Says the parameters did not change between runs.
2. Says the architecture did not change between runs.
3. Says Part 1 cannot yet say what the variation implies.
4. Says in the toy, selection from a fixed distribution produces different observed counts; the seed changes the selected sequence under otherwise fixed conditions.
5. Distinguishes this from temperature, which changes the weights, and from count, which changes how many observations are collected.

**Source:** What Part 1 gives you, and what it leaves with you

## ES-ch01.31

Write the contract for the Part 2 probability-and-sampling function as the chapter states it.

**Points:** 5

**Rubric (1 point each):**

1. Probabilities are nonnegative and sum to one.
2. A larger score never gets a smaller probability at positive temperature.
3. Equal scores get equal probabilities.
4. The function refuses an empty list, a nonfinite score, and a temperature that is zero, negative, or nonfinite.
5. Sampling with the same seed repeats.

**Source:** The gate: write the experiment before you run it

## ES-ch01.32

The chapter's gate asks for a sentence about what a failure would look like and a statement of what the experiment may claim. Explain both, and say what role Claude may play in writing the gate.

**Points:** 5

**Rubric (1 point each):**

1. Says to write one sentence about what you would see if the program were wrong, and to date it.
2. Says that if written after reading the output, it describes the output rather than testing your understanding.
3. Says the experiment may claim only a distribution over three indices and counts of draws.
4. Says it cannot say that any outcome is correct.
5. Says Claude can sharpen the gate but cannot write it for you without defeating its purpose, because the gate is where your understanding goes on the record and what you test Claude's implementation against.

**Source:** The gate: write the experiment before you run it

## ES-ch01.33

A student proposes turning [1, 2, 3] into probabilities by dividing each score by 6. Compute that result and say why the chapter does not use this rule.

**Points:** 5

**Rubric (1 point each):**

1. Computes the result as about [0.167, 0.333, 0.500], noting that the scores sum to six and the result sums to one.
2. Says it is a different transformation from the one implemented in the lesson.
3. Says it would fail on negative scores.
4. Says the chapter is explaining a particular mechanism, not inventing any normalization that happens to work on one positive list.
5. Describes the actual mechanism: exponentiate score differences, then divide by the total weight, because an exponential turns any finite real input into a positive weight.

**Source:** Three scores are not yet three chances

## ES-ch01.34

Explain why, for positive temperature, the ordering of the scores survives the transformation, and how that prediction can serve as a debugging instrument.

**Points:** 5

**Rubric (1 point each):**

1. Says dividing by a positive T preserves score order.
2. Says the exponential preserves the order again.
3. Says every weight is divided by the same positive total.
4. Says changing a positive temperature can change how strongly the largest score dominates but cannot make a smaller score the largest probability.
5. Says that if an implementation gives the smallest score the largest probability, you have reason to suspect an error such as negated differences or wrongly paired labels.

**Source:** Three scores are not yet three chances

## ES-ch01.35

For scores [1, 2, 3] at temperature 1, compute by hand the shifted scores, the three weights (to three decimals), the total weight, and the three probabilities (to three decimals).

**Points:** 5

**Rubric (1 point each):**

1. Shifted scores are [-2, -1, 0] (subtract the maximum, 3).
2. Weights are about 0.135, 0.368, and 1.000.
3. Total weight is about 1.503.
4. Probabilities are about 0.090, 0.245, and 0.665.
5. Notes that the probabilities sum to one and that outcome two (score three) is the favorite.

**Source:** The subtraction that changes nothing important

## ES-ch01.36

Show algebraically why subtracting the maximum score before exponentiating leaves the distribution unchanged, and say what the choice buys the computer.

**Points:** 5

**Rubric (1 point each):**

1. Writes the shifted numerator as exp(z_i/T) times exp(-m/T), where m is the maximum score.
2. Writes the shifted denominator as exp(-m/T) times the sum of exp(z_j/T).
3. Says the common factor cancels, so the intended distribution is unchanged and only the intermediate weights change.
4. Says that after subtracting, the largest exponent is zero (its exponential is one) and the others are no larger than one, so large intermediate exponentials are not needed.
5. Uses the [1000, 1000] test (shifted to [0, 0], then [1, 1], then [0.5, 0.5]) and says it is evidence for this concrete case, not a proof for every numeric input.

**Source:** The subtraction that changes nothing important

## ES-ch01.37

The reference function raises an error for an empty list, a nonfinite logit, and a zero, negative, or nonfinite temperature. Give the chapter's reason for each refusal and explain why the refusals are where a human's decisions live.

**Points:** 5

**Rubric (1 point each):**

1. Empty list: it offers no outcome to normalize.
2. Zero temperature: it makes the division invalid.
3. Negative temperature: it would reverse the ordering the chapter just relied on.
4. Nonfinite logits are refused because the logits must be finite.
5. Says Claude writes the happy path unprompted and the boundary only if your gate demands it, so the refusals are where the human's decisions live.

**Source:** The subtraction that changes nothing important

## ES-ch01.38

Your test checks that the returned probabilities sum to approximately one, and it passes. What does this test show and not show? Why does the check use approximate equality?

**Points:** 5

**Rubric (1 point each):**

1. Says the check uses approximate equality because floating-point arithmetic has limits.
2. Says a sum close to one shows one property only.
3. Says it does not show the ordering is right.
4. Says it does not show equal scores get equal probabilities or that an invalid temperature is rejected.
5. Says it does not show that sampling consumes the probabilities correctly, so the claim should be narrower than the slogan "numerically stable."

**Source:** The subtraction that changes nothing important

## ES-ch01.39

Using the ratio p_i / p_k = exp((z_i - z_k) / T), compute the ratio of outcome two (score 3) to outcome one (score 2) at T = 0.5, 1, and 2, and explain what the trend says about temperature.

**Points:** 5

**Rubric (1 point each):**

1. At T = 1 the ratio is exp(1), about 2.718.
2. At T = 0.5 the ratio is exp(2), about 7.389.
3. At T = 2 the ratio is exp(0.5), about 1.649.
4. Says a smaller positive T makes the exponent larger and the ratio larger, while a larger T brings the ratio closer to one.
5. Says normalization cancels out of the ratio, so temperature changes relative concentration, which explains the effect without a slogan about creativity.

**Source:** Temperature is a concentration control, not a fact checker

## ES-ch01.40

For scores [1, 2, 3], which temperature, 0.5 or 2, gives more probability to outcome two, and which gives more to outcome zero? Answer using the chapter's table, and say what stays fixed across the table.

**Points:** 5

**Rubric (1 point each):**

1. Says T = 0.5 gives outcome two more (about 0.867 versus about 0.506).
2. Says T = 2 gives outcome zero more (about 0.186 versus about 0.016).
3. Says the largest score remains the favorite throughout, with its share moving from about 87 percent to about 51 percent.
4. Says the ordering is fixed, and that predicting only the winner misses most of the experiment.
5. Says scores, ordering, and transformation stay fixed while temperature changes, so nothing in the operation supplies evidence about the meaning of any selected answer.

**Source:** Temperature is a concentration control, not a fact checker

## ES-ch01.41

The chapter constructs a hypothetical in which the three labels are proposed answers and the independently checked answer is label zero. Explain what happens when temperature is lowered, and what this does and does not show.

**Points:** 5

**Rubric (1 point each):**

1. Identifies the hypothetical as explicitly constructed, with the answer key stipulated as label zero.
2. Says lowering temperature concentrates selection on label two, which is wrong under that key.
3. Says the transformation works as designed; the failure is treating its preference as a truth guarantee.
4. Says this must not be reported as an observed Claude error.
5. Says no change in concentration can supply information the program never receives.

**Source:** Temperature is a concentration control, not a fact checker

## ES-ch01.42

A classmate says, "Low temperature means the model picks the highest-scored answer." Respond using the chapter's interface and counts.

**Points:** 5

**Rubric (1 point each):**

1. Says low temperature is not the same as choosing the largest score directly.
2. Says this interface rejects zero temperature rather than switching to a deterministic mode.
3. Cites the T = 0.5 counts: the top outcome was selected 849 of 1,000 times, with 133 and 18 for the others, so it is concentrated but not exclusive.
4. Says the point is not a promise about any Claude setting.
5. Says even if the top score were always selected, that would be concentration, not correctness.

**Source:** Temperature is a concentration control, not a fact checker

## ES-ch01.43

At T = 1 the chapter assigns about 0.66524 to outcome two, and the seed-7 run recorded 630 of 1,000. Compute the expected count and the observed share, and explain why the gap is not automatically a bug.

**Points:** 5

**Rubric (1 point each):**

1. Computes the expected count as about 665.24.
2. Says an expected count of 665.24 cannot be an observed count because counts are integers.
3. Gives the observed share as 0.63 against an assigned probability of about 0.66524, and says both belong in the report because they answer different questions (what chance was assigned, what fraction appeared).
4. Says one gap does not make the sampler broken; you need an acceptance criterion appropriate to the experiment.
5. Notes that the existing reproducibility test checks that the same call returns the same counts, not agreement with every theoretical proportion.

**Source:** A distribution is not the sample you happened to see

## ES-ch01.44

The chapter's counts table is: T = 0.5: 18, 133, 849; T = 1: 102, 268, 630; T = 2: 202, 329, 469. Say what the table shows about temperature and what it does not show.

**Points:** 5

**Rubric (1 point each):**

1. Notes that each row totals 1,000.
2. Says outcome zero's count rises (18, 102, 202) and outcome two's falls (849, 630, 469) as temperature rises, as the distribution flattens.
3. Says the outcome with the highest score had the highest count at every temperature.
4. Says counts are evidence of the recorded executions, not exact expressions of the theoretical probabilities (for example 102 observed against about 90 expected for outcome zero at T = 1).
5. Says a count of an index selected in a constructed experiment does not show that any answer is correct.

**Source:** A distribution is not the sample you happened to see

## ES-ch01.45

A small sample returns a dictionary with no key for outcome zero. What does that mean, how should a report handle it, and what should you not conclude?

**Points:** 5

**Rubric (1 point each):**

1. Says the dictionary has no key for an outcome never selected.
2. Says a missing key means no recorded selections.
3. Says missing counts should be retrieved or reported as zero.
4. Says it does not mean removal from the probability model; "not observed in this run" differs from "not a possible outcome."
5. Gives an illustration, such as outcome zero having a positive assigned probability (about 0.016 at T = 0.5) even if it is never drawn.

**Source:** A distribution is not the sample you happened to see

## ES-ch01.46

A teammate says, "Our fixed-seed run is reliable because it reproduces every time." Respond using the chapter's account of the seed.

**Points:** 5

**Rubric (1 point each):**

1. Says a seed lets you return to a particular experiment while debugging.
2. Says the seed gives the sample no factual status.
3. Says that if a fixed sequence repeatedly selects the hypothetically wrong label, repeatability preserves the mistake.
4. Says a result you can reproduce on demand is still only as true as what produced it (the fluent wrong answer in miniature).
5. Says the reproducibility test shows repeatability, not agreement with correctness or with every theoretical proportion.

**Source:** A distribution is not the sample you happened to see

## ES-ch01.47

Prompt 1 asks Claude the same one-sentence question in four conversations. Explain why four separate new conversations are required and what you record.

**Points:** 5

**Rubric (1 point each):**

1. Says sending it four times in one conversation is wrong because the transcript grows, which changes the input.
2. Says to open four separate new conversations and send the prompt once in each.
3. Says to record all four and note what is stable (the claim, roughly) and what moves (examples, hedges, clause order).
4. Says this is the counts table, one level up.
5. Says to write your prediction first and save the actual responses with the date and displayed model label, never a remembered summary.

**Source:** First prompts: the same experiment, one floor up

## ES-ch01.48

Prompt 2 asks "What is the capital of Australia?" with the instruction to answer with one word, no punctuation and no explanation. Predict what happens to the spread of answers compared with prompt 1, explain why, and say what the result does not show.

**Points:** 5

**Rubric (1 point each):**

1. Says it uses the same procedure: four fresh conversations.
2. Says the spread of answers should shrink compared with prompt 1.
3. Says a constrained format leaves fewer high-probability continuations to choose among, so the answers converge.
4. Says this is the closest thing to lowering temperature without a temperature control.
5. Says it made the answer more repeatable and no more true.

**Source:** First prompts: the same experiment, one floor up

## ES-ch01.49

Prompt 3 asks Claude for a specific quantitative finding from a peer-reviewed paper on spaced repetition and for its confidence that the citation is real. Explain what you do next and what the exercise teaches.

**Points:** 5

**Rubric (1 point each):**

1. Says the prompt asks for authors, year, and the exact number, then a separate confidence rating that the citation is real.
2. Says you must check the citation yourself.
3. Says the response was fluent and well-formed whatever you find.
4. Says the ranking machinery produced a confident-looking string and confidence was never one of its inputs.
5. Says Claude cannot be the independent check on its own citation, because the process that made it would be vouching for it.

**Source:** First prompts: the same experiment, one floor up

## ES-ch01.50

Describe prompt 4 (Claude as a reviewer of your reasoning): when to use it, what it asks, and why it withholds a verdict.

**Points:** 5

**Rubric (1 point each):**

1. Says to use it only after you have written your own prediction and reasoning.
2. Says the prompt tells Claude not to say whether you are right.
3. Says it asks Claude to name the single assumption your reasoning depends on most.
4. Says it asks Claude to describe an input that would make it fail.
5. Says withholding the verdict is deliberate because you want the boundary case, not the grade; Claude challenges and you decide.

**Source:** First prompts: the same experiment, one floor up

## ES-ch01.51

Describe the Build It step: what you write before opening the reference, what you explain, how you test it, and what you compare afterward.

**Points:** 5

**Rubric (1 point each):**

1. Says to write your implementation in the learner workspace before opening the reference solution.
2. Says to start with the probability transformation on a short list whose ordering you can inspect by eye.
3. Says to explain each intermediate quantity (shifted score, weight, total, probability) and what would count as an impossible value for it.
4. Lists the lesson's six boundary checks: sum near one, equal large scores, temperature comparison, repeatable sampling, rejection of zero temperature, and rejection of an infinite score.
5. Says your own version is the baseline, and that you compare it with the reference and name a difference in behavior, not in line count or style.

**Source:** Build It: the baseline that lets you audit

## ES-ch01.52

Describe the Use It step, in which you conduct Claude Code against your gate: what you hand over, what you do with the result, and the three things the chapter asks you to do afterward.

**Points:** 5

**Rubric (1 point each):**

1. Says to give Claude the gate (the contract and the test list), not your implementation.
2. Says you run your tests on what it returns, yourself.
3. Says to note which tests failed, since a failing test is often a gap in your gate that Claude cannot see.
4. Says to compare its implementation with your baseline and name one behavioral difference (a boundary it handled that you missed, or one it silently ignored).
5. Says to ask Claude for a deliberately wrong version that still passes your tests and check by hand whether it does; if it does, your test list was too weak.

**Source:** Use It: conduct Claude Code against your gate

## ES-ch01.53

A reviewer sees an outcome-two count of 849 in your report and asks whether that proves the answer is correct. Write the reply the report should make easy, and state a claim the report may make.

**Points:** 5

**Rubric (1 point each):**

1. Says 849 is a count of an index selected in a constructed experiment.
2. Says correctness would need an answer key or a source check tied to a meaningful claim.
3. Offers a bounded claim such as: in the recorded local run, decreasing temperature from two to one-half concentrated the assigned probability on the largest score.
4. Says the sample counts are recorded separately from that claim.
5. Says the report begins with the prediction written before running, preserved even if wrong, because replacing it with the correct answer destroys the comparison.

**Source:** Ship It: a report that survives a skeptical reader

## ES-ch01.54

Describe the sign-off template and explain why it should be written from your own record rather than drafted by Claude.

**Points:** 5

**Rubric (1 point each):**

1. Names the template's lines: Checked, How, Not checked, Not claiming, and Signed or withheld.
2. Says Claude can draft its words in seconds and the draft will be fluent, so you write it from your record.
3. Says the "Not checked" line does the work, and an AI-written sign-off never includes it because the system has no record of what you did not do.
4. Gives examples of what belongs in "Not checked" or "Not claiming," such as inputs outside your tests, other Python versions, correctness of any outcome, or that this models a Claude setting.
5. Says that if your evidence does not support signing, withholding is an honest result.

**Source:** Ship It: a report that survives a skeptical reader

## ES-ch01.55

Using the driver's-seat table, explain who does what for the tasks "Explaining a surprising output" and "Saying what the result supports," and how the sampling report should show the split.

**Points:** 5

**Rubric (1 point each):**

1. For explaining a surprising output: Claude proposes hypotheses.
2. For explaining a surprising output: you test each against the code and the input, because an explanation from the system under test is a story, not a trace.
3. For saying what the result supports: Claude flags an overclaim.
4. For saying what the result supports: you choose the verb and sign, because your name is on the claim.
5. Says the report should record one delegated task and one retained judgment, each pointing to a transcript line or an edit; otherwise the split happened in your head and not in the record.

**Source:** The driver's seat

## ES-ch01.56

Describe how the chapter wants you to verify and reflect on your work, including the difference between "recorded," "computed," and "established correctness."

**Points:** 5

**Rubric (1 point each):**

1. Says verification begins with a claim small enough to test, such as shifted and direct formulations agreeing on moderate inputs, rejection of an invalid temperature, or repetition of a seeded call.
2. Says to name which claim each check addresses.
3. Says the worked-example script and its JSON do not substitute for your own prediction and implementation.
4. Says "recorded" describes an observation, "computed" a calculation, and "established correctness" requires a criterion the sampler never receives.
5. Says the reflection is which distinction you originally collapsed (scores and probabilities, probabilities and frequencies, or repeatability and truth) and the input or calculation that separated them again.

**Source:** Verify and reflect

## ES-ch01.57

The chapter's last Assessment asks what would transfer from the three-outcome experiment to a real Claude interaction. Which conclusions does the toy support, which questions about Claude need other evidence, and what kinds of evidence does the chapter name?

**Points:** 5

**Rubric (1 point each):**

1. Says the toy supports conclusions about a distribution over three indices and counts of draws.
2. Says it cannot say that any outcome is correct.
3. Says questions about a real Claude interaction need documented interface details.
4. Says they also need actual transcripts and independently checked sources.
5. Says the evidence plan should be designed without running paid requests, and should not claim the toy models a Claude setting.

**Source:** Assessments - ungraded practice

## ES-ch01.58

Suppose a response is stable, repeatable, and neatly formatted, yet claims the source says red when the source says blue. Explain why the sampler cannot catch this, what Chapter 2 builds in response, and the mistake it warns against.

**Points:** 5

**Rubric (1 point each):**

1. Says the response may still be unacceptable despite being stable, repeatable, and neatly formatted.
2. Says the sampler cannot reject the mismatch because it never receives the source's meaning as a condition to check.
3. Says Chapter 2 builds a contract around an answer: required fields, types, source identifiers, and an evaluation set.
4. Says structure earns its place by rejecting specific failures, and the mistake is asking it to reject failures it was never written to recognize.
5. States the question Chapter 2 adds: when the program says an answer passed, exactly which obligation did it pass?

**Source:** The next boundary

## ES-ch01.59

Apply the Computational Skepticism note to one sentence of your sampling report that contains a probability. What do you do, and what does the note claim and not claim?

**Points:** 5

**Rubric (1 point each):**

1. Says the probabilities in this chapter concern selection among constructed indices, not the chance that an answer is true.
2. Says to state the event to which the sentence's probability refers (for example, "the sampler selects outcome two").
3. Says not to quietly replace that event with "outcome two is correct."
4. Says the companion book's diagnostic is to keep confidence claims separate from observed correctness.
5. Says the note contributes an auditing question and does not claim that a calibration study was run.

**Source:** Computational Skepticism

## ES-ch01.60

Using the chapter's Irreducibly Human note, state what AI should and what the human should do in this chapter's work, and what to do if you cannot explain unaided why a repeatable sample can select a wrong answer.

**Points:** 5

**Rubric (1 point each):**

1. Says AI should help diagnose errors after your first attempt.
2. Says AI should suggest boundary cases, run authorized checks, and organize actual results.
3. Says AI should label hypothetical examples, distinguish proposed explanations from observations, and not invent your initial prediction.
4. Says the human should make the prediction, build the initial mechanism, explain the transformation and one rejection case, and decide what the evidence supports.
5. Says that if you cannot explain it unaided, you should take another pass through the three numbers rather than write a more elaborate prompt that conceals the gap.

**Source:** Irreducibly Human
