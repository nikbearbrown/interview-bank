# Conversion report: ch04-the-agent-loop

Old MA: 64. Old essays: 62. New MA: 36. Dropped/merged MA: 28 (merged near-duplicates, e.g. MA-ch04.8, .9, .10 into the status question; .17/.55 into trace retention; calculation and code-trace items .7, .14, .15, .52, .54, .57 removed as non-vocabulary).

Essays converted (folded into MA content): ES-ch04.1-6, 9-10, 12-14, 16-19, 21-25, 26, 28-32, 33-38, 40-41, 43-48, 50-53, 55, 56-58, 60-62 (terms and term contrasts).
NOT CONVERTED: ES-ch04.7, 8 (code tracing, procedure); ES-ch04.11, 59 (token and cost calculation); ES-ch04.15, 27, 39, 42, 49, 54 (design opinion or procedure with no distinct term).

## Agent loop and control
agent loop :: a cycle in which a model proposes an action, a program runs it, and the result is fed back until a stop
policy :: the part (the model) that proposes the next action
controller :: the program around the model that executes actions, records results and decides whether to continue
action :: what the policy proposes to do next
observation :: the result a tool returns after an action
turn :: one pass of propose, execute and observe
turn budget :: an operator-set cap on loop iterations, enforced in the harness
timeout :: a limit on elapsed time that can interrupt a call that hangs
status finished / incomplete / budget-exhausted :: finish received / action source ran out before budget / allowed turns all used without a finish
finish action :: the policy's request to stop, which does not itself verify the output
trace :: the record of actions and observations, not of reasoning
workflow vs agent :: predefined steps in code vs the model directing its own process
planning before acting :: stating intended steps for review before any tool runs
polling, backoff, deadline :: repeated status calls, growing waits between them, an elapsed-time limit

## Checking and evidence
control layer vs evidence layer :: whether the run ended vs whether the output is supported by evidence
outcome check :: a comparison of the result against a reference outside the generator
independent check :: one that does not share the generator's failure modes
claim vs evidence :: testimony from the producer vs something confirmable without it
system of record :: the authoritative place where the real state lives
sentinel value :: a placeholder value such as not found that stands for absence
fabricated completion :: a report of finishing an action that did not happen
false positive / false negative (detector) :: stop on fine behavior / missed loop
repetition detector :: a heuristic that stops or flags a run on repeated actions
grounding :: tying an answer to named evidence

## Claude API and tools
stop_reason :: tool_use (model requests a tool), end_turn (natural finish), max_tokens (cut off at the output limit)
tool_use / tool_result :: the model's request block / the harness's returned output block
parallel tool calls :: several tool_use blocks in one response
context window / prompt caching :: per-request limit on text / reuse of an unchanged prefix to cut cost
prompt injection :: instructions smuggled in through content the model reads
allowlist :: the set of actions a harness will dispatch
permission vs approval gate :: standing rule on allowed actions vs per-call human yes
idempotency key :: a token letting a service apply a repeated request once
canonical path / symbolic link / path traversal :: resolved absolute path / link pointing elsewhere / .. escaping a directory
mutation testing :: injecting deliberate faults to see whether tests catch them
specification before implementation :: writing intended exits and behavior before code exists
diff review :: reading what an assistant changed before accepting it
