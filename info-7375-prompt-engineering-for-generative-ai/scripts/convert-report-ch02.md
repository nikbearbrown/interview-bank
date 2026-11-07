# Conversion report: ch02-prompt-contracts-and-evaluation (MA-ch02)

- Old MA: 64. Old essays: 61. New MA: 35.
- Dropped/merged MA: 29 (e.g. MA-ch02.9, 11, 14, 15 Python all/any, bool/int, strip, json.loads trivia; 26, 46, 47, 38, 50, 58 arithmetic on standard error, rates and chained probability; 16 merged with 27; 3 merged with 5).
- Essays converted into MA content: ES-ch02.1, 2, 4, 5, 6, 7, 9, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 50, 54, 55, 56, 57, 59, 60, 61 (folded into the 35 questions by shared contrast).
- NOT CONVERTED: ES-ch02.3 (design of a layered eval, design opinion), 8 and 58 (read-and-trace code), 10 (test-suite design exercise), 11, 12, 16, 40, 46, 48, 49, 52, 53 (calculation or statistics procedure), 27 and 34 (report-writing and procedure), 47 (Python pitfalls trivia), 51 (design of a model-comparison test).

## Terms especially tested

### Prompt contracts and evaluation
- output contract :: a written statement, made before the prompt, of the output a consuming program accepts
- validator :: code that checks one response against fixed rules and accepts or rejects it
- prompt template :: reusable text sent to the model (not the checking code)
- JSON mode :: provider setting that guarantees syntactically valid JSON, not particular keys
- schema-constrained decoding :: generation restricted to tokens that keep the output conforming to a supplied schema
- strict vs lenient validator :: strict rejects unexpected keys; lenient ignores them
- parse error / wrong shape / key mismatch / wrong type / bad value :: ordered categories of validator failure
- structural validity vs grounding :: well-formed output vs content supported by the supplied sources
- citation vs support :: an identifier that exists vs a source whose text backs the claim
- partial support :: some claims in an answer supported and others not
- abstention :: declining to answer when evidence is insufficient
- hallucination :: fluent content the supplied evidence does not support (vs a format error)
- ungrounded :: not traceable to supplied evidence
- eval :: a measurement of a prompt over a set of cases
- test case / test set / pass rate / metric :: one input with its criterion / the list of cases / fraction accepted / summary number
- code-graded, model-graded, human-graded :: scored by a program, by a model, by a person
- LLM-as-judge; position bias, verbosity bias, self-preference :: model scoring; favouring first-shown, longer, or own-family text
- judge calibration :: measuring a grader's agreement with a standard such as human labels
- development set vs held-out set :: data used to revise a prompt vs data kept unseen until the revision is frozen
- leakage / contamination :: evaluation items reaching the prompt or tuning
- few-shot prompting :: including worked input-output examples in the prompt
- overfitting; Goodhart's law :: fitting tuning cases at the cost of new inputs; a measure that becomes the target stops measuring the goal
- controlled comparison, confound, baseline :: change one thing at a time; entangled explanations; the unchanged reference run
- temperature, sampling noise :: randomness of token sampling; run-to-run variation in a score
- role prompt (persona line) :: prompt text assigning the model a role
- provenance, raw response, audit trail :: where data came from; the unedited reply; a record another person can reconstruct from
- constructed vs observed data :: hand-written test strings vs replies returned by a model
- model alias vs pinned snapshot :: a moving name vs a fixed version
- selective reporting; change log :: leaving out failures; dated entries naming what changed and why
- first-attempt vs final pass rate; severity :: pass rate before vs after retries; how harmful a failure is
- truncation, stop reason :: a reply cut off at the output limit; the API field saying why generation ended
- tool call, allowlist, least privilege, approval gate :: structured request to run a tool; permitted-action list; narrowest access needed; human confirmation before an action
- undetermined outcome :: a third verdict for answers that cannot be judged
- inter-rater agreement; kappa :: consistency between reviewers; chance-corrected agreement
- mutation testing; edge case :: deleting a rule to test whether tests notice; boundary input such as an empty list
- diff review; planning before acting :: reading the changes an assistant made; having it propose a plan before editing
- calibration (of stated confidence) :: stated confidence matching observed accuracy
