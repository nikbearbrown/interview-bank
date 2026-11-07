# Conversion report: ch12-memory-and-multiple-agents

- Old MA: 61. Old essay: 60. New MA: 36. Dropped/merged: 25 old MA (e.g. MA-ch12.4 aliasing, .8 retry arithmetic, .9 bool/int type check, .18 and .21 probability sums, .54 and .55 sampling/reviewer arithmetic, .27 shared-information bias folded into anchoring item, .53 folded into permissions item).
- Essays converted (folded into MA items where they teach a term or contrast): ES-ch12.1-3, 5-7, 10-17, 19-25, 27-28, 30-33, 35, 37-40, 42-47, 49-52, 54, 56-60.
- Essays NOT CONVERTED: ES-ch12.4 (Python aliasing code detail), 8 (attempt-count calculation), 9 (Python bool/int trivia), 18 and 20 (probability computation), 26 (team procedure design opinion), 29 (privacy tension, policy opinion), 34 (assistant timeline, folded only as hallucination item), 36 (test-design procedure), 41 (cost calculation), 48 (score calculation), 53 (sampling calculation), 55 (reviewer-catch calculation).

## Terms especially tested
### Memory and retrieval
stateless :: a model call keeps no information between calls beyond the text in its context window
context window :: the text the model sees in one call
memory :: stored state outside the model that application code can place into the prompt
retrieval :: selecting which stored items go into the prompt
embedding :: a vector representing the meaning of a text so similar texts are close
semantic search :: ranking stored items by closeness of meaning to a query
exact-key lookup :: reading a record by matching its key string
working memory :: what is in the context window during the current step
episodic memory :: records of specific past events and interactions
semantic memory :: general facts not tied to one event
procedural memory :: skills and how-to instructions
recency / importance / relevance :: scores for how recent, how generally significant, and how task-fitting a memory is
compaction :: summarizing a conversation near the context limit and continuing from the summary
structured note-taking :: writing notes to storage outside the context window for later retrieval
delegation to sub-agents :: sub-agents work in their own context windows and return condensed results
fine-tuning :: training that changes model weights, unlike storing a note
### Concurrency and records
version / expected version :: a counter of committed writes, and the version a writer read
compare-and-set :: a write applied only if the expected version equals the current version
stale write :: a write whose expected version is older than the current version
optimistic concurrency control :: proceed freely and check for conflict at commit
pessimistic locking :: prevent conflict by making others wait for a lock
race condition :: a fault whose outcome depends on how concurrent operations interleave
atomic operation :: a check-and-update that other threads cannot interleave
thread-safe :: correct under concurrent threads of one process, not across servers
lost update :: a later write replacing an earlier one it never saw
granularity :: how much state shares one key and one version counter
superseded / version chain :: a newer reviewed version replaces an older one that stays in history
last-writer-wins / first-writer-wins :: policies that keep the latest or earliest committed value
### Evidence and provenance
valid vs verified :: valid passed the store's rules; verified was checked against evidence
provenance :: record of where a claim came from and how it was derived
lineage :: chain of derivation from the original source
circular reporting :: claims citing each other until they look like corroboration
freshness :: how recent an observation is
event / observation / ingestion time, ingestion lag :: when it happened, when it was seen, when it was stored, and the delay between the last two
valid-until :: time by which evidence needs renewing
hallucination :: generated content not supported by the input
anchoring :: being pulled toward the first view seen
### Safety and coordination
prompt injection :: instruction-like text in input that the model may follow
input boundary :: separation of untrusted data from trusted instructions
allowlist / least privilege :: narrow, pre-set limits on what a tool or worker may do
permission vs approval gate :: a standing rule vs a human sign-off before a specific action
quarantine :: retain a record but exclude it from prompts
side effect / idempotency key :: a change outside the agent's store, and a key that makes a repeated request apply once
role contract :: handoff stating inputs, task, tools, output format and escalation
handoff :: point where work and claims pass between agents
orchestrator vs worker :: the agent that splits and combines work vs the agent that does a subtask
budget / escalation path :: cap on resources, and a route to a named human
proposal queue :: holding area for unreviewed candidate facts
premortem vs postmortem :: imagine failure before launch vs review an incident after
sign-off statement :: what was checked, how, what was not checked, what is not claimed
end-to-end evaluation / error propagation :: measuring the chain's final output; wrong output feeding the next stage
