# Conversion report: ch03-chat-assistant-agent (MA-ch03)

- Old MA: 63. Old essays: 61. New MA: 36 (true-counts: 2 one, 12 two, 16 three, 6 four).
- Dropped/merged: 27 old MA. Merged near-duplicates (e.g. MA-ch03.1/3/56 into proposed vs completed state; .21/.22/.23 into proposed/attempted/completed/observed; .4/.47/.53 into self-report vs independent evidence; .38 variants). Dropped as non-vocabulary: capability-set arithmetic and code (MA-ch03.6, .7, .15, .16, .18, .28, .49, .50), documentation how-to (.58, .59, .31, .32).
- Essays: converted by folding into MA: fix-the-report scope, summarize-without-changing, workflow vs agent, simplest solution, declared vs recorded, label limits, proposed/attempted/completed, authorization vs capability, approval vs quality, auto-approver, fail closed/open, idempotent retries, prompt injection, reversibility, approval fatigue, agent loop and stopping, audit log, independent verification, read-only risk, review levels, test-first with AI. NOT CONVERTED (calculation, procedure or design opinion): the essays on missing-set computation, review-capacity arithmetic, random-sample bound, capability-set counting, classifier implementation tests, experiment design for chat vs agent, division of labor, recommendation writing, "agents are riskier" evaluation.

## Terms especially tested

### Chat, assistant, agent
chat :: text-in, text-out system with no tools for acting on the outside world
agent :: model that uses tools, usually in a loop, to take actions toward a goal
workflow :: predefined code paths orchestrate the model and tools; code controls the sequence
model-directed (agentic) control :: the model chooses the next step and when to stop
capability :: an operation the system is able to perform with its tools
control :: which party (code or model) chooses the next step
scrutiny :: how closely output has to be checked, set by the stakes
tool_use :: the model's structured request to call a named tool with arguments (not execution)
tool_result :: outcome of the tool run, sent back to the model by the application
agent loop :: cycle of choose action, execute, observe, decide whether to continue
iteration budget (stop condition) :: harness-enforced limit on loop cycles
guardrail :: a check around the model that limits damage when a step goes wrong
context window :: the text the model can use when it responds

### Permissions and authorization
permission / authorization :: a decision, by someone with authority, of what may be done, where and under what conditions
least privilege :: grant the smallest capability set that completes the task
scope :: the named target and limits of a grant
allowlist / denylist :: list of permitted vs forbidden items; allowlist refuses the unrecognized
path normalization :: resolving .. and links to the real location before checking
fail closed / fail open :: refuse vs allow by default on unrecognized input
approval gate :: pause before a step until a person decides
approval fatigue :: reduced attention to prompts when they are frequent
prompt injection :: instructions planted in content the model processes
exfiltration :: private data leaving through an outbound channel
side effect :: change beyond the returned value
idempotent :: repeating the operation leaves the same end state
dry run / plan mode :: show intended changes without applying them
snapshot (checkpoint) :: copy taken before a write to allow comparison and restore

### Evidence and review
self-report (narration) :: the system's own account of what it did
proposed / attempted / completed / observed :: offered in text / request issued / runtime reported success / state looked at independently
diff :: lines added and removed between two versions
audit log (append-only) :: harness-written record of actions with target, result and approver
declared capabilities vs trace :: what is possible vs what a particular run did
automation complacency :: monitoring falls as automation seems reliable
fabricated record :: invented fact, such as naming an approver who did not approve
simulated approval :: test-harness auto-approval, not a human decision
grant specification :: outcome, capabilities, refused operations, target, escalation condition, evidence, pass condition
escalation condition :: when control returns to a person
