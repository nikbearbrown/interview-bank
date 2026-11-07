# Conversion report: ch11-tool-use-and-verification (MA-ch11)

Old MA: 60. Old essays: 61. New MA: 36. Dropped/merged: 24 old MA (merged into related questions or removed as non-vocabulary; e.g. MA-ch11.5/6/7 numeric edge cases folded into one boolean/NaN/infinity question, 9 and 47 compound-error arithmetic dropped, 10 currency, 34/54 folded into trace and idempotency questions, 12 to 17 folded into dispatcher, error-result, identifier questions).

Essays converted (skill folded into MA content): ES-ch11.1-2, 7-9, 11-13, 16, 18-19, 21-26, 27-31, 33, 36-38, 40-42, 43, 45-46, 49, 52-55, 57, 60-61.
NOT CONVERTED: ES-ch11.3 (specification design, procedure), 4-5 and 10 (design opinion), 6 (argument, covered by determinism vs correctness question), 14-15 (covered in stub and stop_reason questions, procedure), 17, 20, 34-35, 39, 44, 47 and 48 (calculation: 0.98^12 and escape rates), 50-51, 56 (test-case design), 58-59 (table-building design).

## Terms tested
### Tool use and verification
tool definition :: name, description and input schema advertised to the model; describes a tool, does not run it
input schema :: JSON Schema description of a tool's arguments; guides generation, does not enforce
tool_use block :: assistant-side structured request to run a named tool with arguments (a tool call)
tool_result block :: user-side message block returning a tool's output, linked by tool_use_id
tool_use_id :: identifier tying a result to its request; establishes correspondence, not correctness
stop_reason (end_turn, tool_use, max_tokens) :: field saying why a response ended: natural completion, waiting on a tool, or truncation
dispatcher :: application code mapping a requested tool name to an operation
allowlist :: closed set of permitted operations; separate from argument rules
strict validation vs coercion :: reject mismatched input vs silently convert it
path traversal / canonical path :: escaping an approved directory with .. or links / the resolved real location
error result (is_error) :: tool_result flagged as a failure so the model can repair the call
workflow vs agent loop :: fixed code-directed sequence vs model-directed repeated tool calls
turn limit (iteration cap) :: bound on model requests; bounds cost, not progress
deterministic vs correct :: repeatable output vs right output
stub (scripted response) :: injected fake client; tests control logic, not model behaviour
repetition vs corroboration :: rerunning the same path vs a check that fails differently
shared assumption :: premise that agreeing checks both depend on
falsifiable claim / detection power :: claim an observation could contradict / ability of a check to fail on a real fault
hallucination :: fluent, specific, ungrounded generated content such as a fake citation
grounding :: answer claims traceable to and supported by a cited source
similarity vs support :: embedding closeness is relevance, not entailment
overclaim / scope of claim :: report stronger than the evidence (saved, deleted, deployed, current)
stale evidence / provenance :: out-of-date result; dates and versions recorded with a check
approval gate vs permission rule :: human checkpoint on one call vs standing policy on what may run
idempotency / idempotency key :: repeat gives same effect / token marking a retry as the same request
indirect prompt injection / least privilege :: instructions hidden in read content / narrow granted authority
sign-off :: closing statement of what was checked, how, and what is not claimed; tested vs verified
contract and tests first :: specification and tests written before the implementation is requested
negative case :: evidence of a rejection, showing a check can say no
trace / redaction :: record of calls for audit / masking sensitive fields
MCP server vs client :: provider of tools vs consumer inside the host application
