# Conversion report: 00-foundations (id stem MA-found)

- Old MA: 39. Old essays: 25. New MA: 39 (target 36-40). check_format: 0 problems; forbidden-word grep on statements: clean.
- True-count spread: 1 true x4, 2 true x13, 3 true x14, 4 true x8. True positions spread across A-E.
- Dropped or merged old MA: about 14. Merged: MA-2.4 into new 2.3 (retrieval vs fine-tuning); MA-4.5 and 4.4 into new 12 (embedding closeness); MA-4.2 and 4.6 sharing; MA-6.2 into 6.1 (contextual representation); MA-11.2 reworked into agent vs workflow. Dropped as non-vocabulary or numeric: MA-4.7 (compression claim), MA-5.1 and 5.3 (arithmetic on logits), MA-9.1 (division-of-labour how-to, reworked into the prompt-contract and plan/diff questions), MA-10.3 partly, MA-12.3 numeric item.
- Essays converted (by order in old file) into MA content: spam filter rules vs learned (1.1), prompt-to-token pipeline (2.2), news analyst and cutoff (2.3), transformer parts (3.1), encoder vs decoder (3.2), feedforward (3.3), embedding essays (4.3, 4.4), attention and bank (6.1), parallelism (6.3), positional encoding (6.2), programming language vs model (7.x), functions as checkers (8.x), gate design (9.1, 9.2), format vs factual validity (10.1), repeat-run reliability (10.2), agent loop (11.1 to 11.3), solve-verify (12.1), fluency and falsifiability (12.2, 12.3). Added from the brief's term list: system prompt vs user turn, tool_use vs tool_result, MCP server vs client, prompt contract, planning before acting, diff review, hallucination vs error, eval vs test.
- NOT CONVERTED: essay on embedding sizes and logits shape for a 50,000-token vocabulary (calculation); essay on temperature trend for logits [1,2,3] (calculation, the vocabulary part is covered by temperature items); essay on reading time for 300 billion training tokens (pure calculation).

## Terms tested
### Foundations
rule-based system :: a system whose output comes from conditions a person wrote by hand
generalization :: a learned model's ability to give sensible output on inputs beyond its training examples
overfitting :: fitting training examples so closely that performance on new inputs is poor
self-supervised pretraining :: training on raw text where the next token is the label, with no human labelling
scaling :: increasing data, parameters and computation together
fine-tuning :: further training of a pretrained model on narrower data, which changes the weights
model / weights :: a learned function; its learned parameters
training vs inference :: weights are adjusted in training; they are fixed while producing output
knowledge cutoff :: the point after which the training data holds no events
context / context window :: the tokens the model can take in at one time; not memory across conversations
retrieval :: adding source text to the context; it changes what the model sees, not the weights
logits :: raw unnormalized score for each token in the vocabulary
softmax :: step converting logits to probabilities that sum to one
temperature :: scaling of logits before softmax: low sharpens, high flattens
top-p (nucleus) sampling :: sampling from the smallest set of tokens whose probabilities reach p
greedy decoding :: choosing the highest-probability token at each step
sampling / seed :: drawing the next token at random by probability; a seed makes the draws reproducible
autoregressive :: each generated token is appended to the input for the next step
token / token ID :: unit of text from the tokenizer; integer label for it
vocabulary :: the tokenizer's list of tokens
embedding / embedding dimension :: dense vector for a token, learned in training; the length of that vector
one-hot vector :: vector as long as the vocabulary with a single 1
self-attention :: weighted mixing of information from tokens in the context
encoder vs decoder :: encoder builds representations of a whole input; decoder generates left to right from earlier tokens
feedforward network (MLP) :: layered nonlinear map applied to each token's vector
positional encoding :: position information added so order matters
system prompt vs user turn :: standing instructions for a conversation vs one message from the user
pure function / unit test :: deterministic function without side effects; check of a function against an expected output
acceptance gate :: a check or human decision an output has to pass before it is accepted
prompt contract :: a statement of task, constraints, output form and acceptance checks
planning before acting / diff review :: stating steps before editing; reading line-level changes before accepting
JSON / schema / factual validity :: parses; has the right fields and types; true
held-out cases :: cases kept apart from those used to revise a prompt
eval vs test :: scored over many cases for a nondeterministic system vs deterministic expectation
policy / controller / observation :: model that proposes; program that executes and enforces limits; result returned
agent vs workflow :: model chooses its steps in a loop vs a path fixed in code
permission vs approval gate :: rule on allowed actions vs human confirmation before an action
tool_use / tool_result :: model's request to call a tool; the output returned to the model
MCP server / client :: provider of tools or resources; the part of the host that connects to it
solve-verify asymmetry :: checking a solution is often easier than finding it
hallucination :: fluent output that states something false or unsupported
falsifiable :: a claim for which an observation that would show it wrong can be named
