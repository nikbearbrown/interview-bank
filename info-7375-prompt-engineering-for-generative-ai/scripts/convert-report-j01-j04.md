# Report: new jargon sets j01 to j04

All four files are newly written (not conversions): old MA 0, old essays 0, nothing dropped or NOT CONVERTED. Terms drawn from CHEAT-SHEET and a skim of the archived MA files.

## j01-jargon-sampling-and-tokens.md
New MA: 12; true-counts: [3, 2, 3, 4, 2, 3, 1, 2, 4, 3, 2, 4]

Terms tested:

- token :: a chunk of text (word, part of a word, or punctuation) that a model reads and writes
- vocabulary :: the fixed list of tokens a model can read and produce
- embedding :: a vector of numbers for a token, placed so tokens used in similar contexts are close
- token ID :: a numeric label for a token with no meaning of its own
- logits :: raw scores, one per vocabulary token, before softmax
- softmax :: the step that turns logits into probabilities that add up to one
- temperature :: a sampling setting that sharpens (low) or flattens (high) the probabilities
- top-k :: sampling only among the k most probable tokens
- top-p :: sampling only among the smallest set of top tokens whose probabilities add up to p
- greedy decoding :: picking the highest-probability token at each step
- determinism :: the same input and settings give the same output
- context window :: the span of tokens a model can take in and use in one request
- memory :: stored information put back into the context in later requests
- stop sequence :: a string that ends generation when it appears
- max tokens :: a cap on the number of tokens generated
- next-token prediction :: giving a probability for the next token from the tokens so far
- autoregressive generation :: sampling a token, appending it and repeating

## j02-jargon-prompt-structure-and-contracts.md
New MA: 12; true-counts: [2, 3, 4, 3, 2, 1, 4, 3, 2, 2, 3, 4]

Terms tested:

- system prompt :: standing instructions and role placed in the context before the conversation
- user turn :: one message from the person in the conversation
- role :: the label of a message's source: system, user or assistant
- persona :: a character or voice a prompt asks the model to adopt
- zero-shot :: a prompt that gives an instruction with no worked examples
- few-shot :: a prompt that includes a small number of example input-output pairs
- instruction :: text that says what to do
- example :: a sample input and output that shows what a good result looks like
- delimiter :: a marker such as quotes or tags that separates parts of a prompt
- output format / schema :: the stated fields, names and types the answer should have
- prompt contract :: a prompt stating task, inputs, constraints, output format and how the result is checked
- acceptance criterion :: a testable condition an output has to meet to be accepted
- constraint :: a limit placed on the output or the work
- chain of thought :: intermediate reasoning written out before the answer
- final answer :: the part of the output meant for the user or program
- prompt injection :: instructions hidden in content the model reads to steer it
- jailbreak :: a user prompt that tries to get the model past its own safety rules
- planning before acting :: showing a plan for approval before making changes

## j03-jargon-agents-and-tools.md
New MA: 12; true-counts: [3, 2, 4, 2, 3, 1, 2, 3, 4, 3, 2, 4]

Terms tested:

- chat :: a back-and-forth of messages in which the model returns text
- assistant :: a chat model given a role and instructions to help; it may or may not use tools
- agent :: a system that takes actions through tools and uses the results to choose the next step
- agent loop :: the cycle in which the model proposes an action, the controller runs it, and the observation is fed back
- workflow :: steps fixed in advance by code, though a step may call a model
- controller :: the program around the model that runs actions and feeds back results
- tool definition :: a tool's name, description and parameters shown to the model
- tool schema :: the shape of a tool's arguments: field names and types
- tool_use :: the model's request to call a named tool with arguments
- tool_result :: the outcome the program sends back after running the tool
- permission :: a rule on whether an action is allowed, asked about or denied
- sandbox :: a restricted environment that limits what an action can reach
- observation :: the result of an action fed back to the model
- stop condition :: a rule that ends the loop
- step budget :: the maximum number of loop steps allowed
- subagent :: an agent given a narrower task by another agent, often with its own context
- orchestrator :: an agent that assigns work to others and combines the results

## j04-jargon-retrieval-and-training.md
New MA: 12; true-counts: [2, 3, 4, 3, 2, 1, 4, 3, 2, 2, 3, 4]

Terms tested:

- retrieval :: looking up relevant passages and adding them to the prompt so the model sees them
- fine-tuning :: continuing training on a targeted set so the weights change
- RAG :: retrieval-augmented generation: retrieve passages, add them to the prompt, then generate
- chunk :: a piece of a document cut to a size that can be indexed and retrieved
- embedding :: a vector representing the meaning of a chunk or query
- vector search :: finding chunks whose vectors are nearest to the query's vector
- grounding :: tying an answer to supplied source material
- citation :: a pointer to the source passage behind a claim
- pretraining :: the first, broad training stage on very large text
- inference :: using a trained model to produce output with weights unchanged
- base model :: the model after pretraining, before instruction tuning
- instruction-tuned model :: a base model trained further on instructions and good responses
- parameters (weights) :: values learned during training
- hyperparameters :: settings chosen by people that control a training run
- configuration :: settings and files that shape how a model is run, outside the weights
- weights :: the learned numbers saved in the model file
