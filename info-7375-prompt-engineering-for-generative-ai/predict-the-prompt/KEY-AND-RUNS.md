# Key and runs — predict-the-prompt pilot

## 1. Configuration (pinned and recorded)

| item | value |
|---|---|
| date sampled | 2026-11-08 |
| plan writer | Claude sub-agent via the Claude Code `Agent` tool, `subagent_type=general-purpose`, `model="sonnet"` (alias; the tool does not return the resolved model id — the session is the Claude 5 family, so this is the Sonnet 5.x line, exact id NOT recorded) |
| how plans were requested | each sub-agent got one line: read `runs/PLAN-BRIEF.md` (project description + rules) and do the task `<prompt>`; write ONLY a numbered plan of at most 8 steps, no code/edits/commands; save it with Write to `runs/raw/<ID>.txt` and reply `done` |
| fixed project description | `runs/PLAN-BRIEF.md` (identical for all 200 runs) |
| runs | 5 families × 4 prompts × 10 = **200 plans**, none discarded, none re-run |
| launch | F1 and F2A directly (waves of ≤20, the concurrency cap); F2B–D and F3–F5 (150 plans) through two orchestrator sub-agents that spawned the plan sub-agents |
| coders | Claude sub-agents, `sonnet`; primary coder: one per family, blind (shuffled ids `P01..P40`, variant hidden, `coding/Fx-blind.md`); second coder: independent sub-agent, 8 of 40 plans per family (20%, every 5th blind id) |
| sampling parameters | **not controllable** (temperature/top-p are the harness defaults) |
| caveats | (1) a sub-agent plan, **not** Claude Code plan mode. (2) The sub-agents ran inside a Claude Code harness; their context may include the harness system prompt and the user's memory/CLAUDE.md, so this is not a clean API call. (3) Plan agents had file tools (used Read + Write only). (4) Both writers and coders are the same model family; coders could share the writers' blind spots. (5) Coders judged text, not running code. (6) Reported sub-agent usage was about 70k tokens per plan run (mostly fixed harness context). |

Reproduce: `prompts.json` (the 20 prompts), `runs/PLAN-BRIEF.md`, `features.json`, then `build_sheets.py` → coders → `analyze.py` → `build_docs.py`, `build_key.py`.

## 2. The 20 prompts

**F1 — Tool use: permission gate vs approval gate**

- F1A: *Give the triage agent an `issue_refund(ticket_id, amount)` tool, protected by a permission gate.*
- F1B: *Give the triage agent an `issue_refund(ticket_id, amount)` tool, protected by an approval gate.*
- F1C: *Give the triage agent an `issue_refund(ticket_id, amount)` tool, protected by a rate limit.*
- F1D: *Give the triage agent an `issue_refund(ticket_id, amount)` tool, protected by an audit log.*

**F2 — Retry: idempotent vs plain**

- F2A: *Make the Claude call and the `save_reply` write in `app/triage.py` more reliable by adding an idempotent retry.*
- F2B: *Make the Claude call and the `save_reply` write in `app/triage.py` more reliable by adding a plain retry.*
- F2C: *Make the Claude call and the `save_reply` write in `app/triage.py` more reliable by adding a circuit breaker.*
- F2D: *Make the Claude call and the `save_reply` write in `app/triage.py` more reliable by adding a timeout.*

**F3 — Retrieval vs facts in the prompt**

- F3A: *Make the reply drafter answer from the help articles by retrieving the relevant articles for each ticket.*
- F3B: *Make the reply drafter answer from the help articles by putting all 40 articles in the system prompt.*
- F3C: *Make the reply drafter answer from the help articles by putting a short policy summary in the system prompt.*
- F3D: *Make the reply drafter answer from the help articles by giving Claude a search tool for the articles.*

**F4 — Planning before acting**

- F4A: *Build a ticket-routing agent that plans before acting.*
- F4B: *Build a ticket-routing agent that acts step by step with no planning step.*
- F4C: *Build a ticket-routing agent that plans before acting and gets a human to approve the plan.*
- F4D: *Build a ticket-routing agent that reflects on each result before taking the next step.*

**F5 — Eval with acceptance criteria vs 'make sure it works'**

- F5A: *For the ticket classifier: write an eval with acceptance criteria.*
- F5B: *For the ticket classifier: make sure it works.*
- F5C: *For the ticket classifier: write unit tests.*
- F5D: *For the ticket classifier: try it on a few examples.*

## 3. Features (S = semantic, B = behavioral; B items weighted half)

**F1**

- `tool_schema` [S]: Defines issue_refund as a Claude tool with an input schema / passes it in the tools parameter (a tool_use flow).
- `human_approval` [S]: A human approves or rejects a specific refund before it executes (pending queue, approval step, review endpoint).
- `permission_scope` [S]: Restricts WHO or WHICH tickets can use the tool: allowlist, roles, verified accounts, scopes, tool only exposed to some requests.
- `amount_limit` [S]: Limits on refund size or frequency: per-refund cap, daily total, rate limit, max refunds per ticket.
- `audit_log` [S]: Records refund attempts/decisions in a log or audit table.
- `mocked_tests` [B]: Adds pytest tests that mock the Claude client or the tool.

**F2**

- `backoff_jitter` [S]: Retry waits grow between attempts (exponential backoff) and/or include jitter.
- `idempotency` [S]: Makes repeated save_reply writes safe: idempotency key, upsert, unique constraint, dedupe check.
- `transient_only` [S]: Retries only transient errors (429, 5xx, overloaded, timeout, connection) and explicitly not client errors such as 400/401.
- `circuit_breaker` [S]: Includes open/half-open/closed breaker state that stops calls after repeated failures.
- `explicit_timeout` [S]: Sets an explicit per-request or overall timeout value.
- `failure_tests` [B]: Adds tests that simulate failures (mocked errors) to exercise the retry/breaker/timeout.

**F3**

- `retrieval_index` [S]: Builds or uses a search/retrieval step (embeddings, vector store, BM25, keyword index) to select a SUBSET of articles per ticket.
- `all_articles_in_prompt` [S]: Places the full text of all or most articles in the prompt.
- `token_budget` [S]: Counts or estimates tokens, or checks the context-window limit, for what goes into the prompt.
- `prompt_caching` [S]: Uses prompt caching (cache_control) for the static article/policy content.
- `cite_or_abstain` [S]: Reply must cite article ids/titles, or must say it does not know / escalates when the articles do not cover the ticket.
- `eval_or_tests` [B]: Adds tests or an eval for the drafter's answers.

**F4**

- `separate_plan_step` [S]: A distinct planning stage (its own model call or phase) produces a plan before any action is executed.
- `structured_plan` [S]: The plan is a structured object (JSON/schema/list of typed steps) that code parses.
- `human_plan_approval` [S]: A human reviews/approves the plan before execution.
- `reflect_or_replan` [S]: After step results, the agent reflects, checks, or revises the plan/next step.
- `iteration_cap` [S]: A max-steps / iteration / budget limit on the agent loop.
- `tests` [B]: Adds pytest tests (mocked Claude) for the agent.

**F5**

- `labeled_dataset` [S]: Builds or collects a labeled set of tickets with expected categories.
- `numeric_threshold` [S]: States a numeric pass/fail threshold (e.g. accuracy >= 90%, max confusions).
- `per_class_metrics` [S]: Computes per-class precision/recall, a confusion matrix, or targeted category-confusion checks.
- `automated_gate` [S]: The eval/test runs automatically and fails a build/exit code (CI, pytest assertion, script exit status) when the bar is missed.
- `edge_case_coverage` [S]: Deliberately includes edge cases/ambiguous/adversarial tickets or a held-out split.
- `mocks_model` [B]: Mocks or stubs Claude so no live API call is made.

## 4. Frequencies (plans out of 10 containing the feature)

Bands: L ≥7, P 2–6, U ≤1.

**F1 — Tool use: permission gate vs approval gate**

| feature | A | B | C | D |
|---|---|---|---|---|
| `tool_schema` [S] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |
| `human_approval` [S] | 10 (L) | 10 (L) | 0 (U) | 10 (L) |
| `permission_scope` [S] | 9 (L) | 9 (L) | 10 (L) | 10 (L) |
| `amount_limit` [S] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |
| `audit_log` [S] | 10 (L) | 9 (L) | 10 (L) | 10 (L) |
| `mocked_tests` [B] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

**F2 — Retry: idempotent vs plain**

| feature | A | B | C | D |
|---|---|---|---|---|
| `backoff_jitter` [S] | 10 (L) | 10 (L) | 7 (L) | 4 (P) |
| `idempotency` [S] | 10 (L) | 10 (L) | 9 (L) | 10 (L) |
| `transient_only` [S] | 10 (L) | 10 (L) | 7 (L) | 0 (U) |
| `circuit_breaker` [S] | 0 (U) | 0 (U) | 10 (L) | 0 (U) |
| `explicit_timeout` [S] | 10 (L) | 9 (L) | 9 (L) | 10 (L) |
| `failure_tests` [B] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

**F3 — Retrieval vs facts in the prompt**

| feature | A | B | C | D |
|---|---|---|---|---|
| `retrieval_index` [S] | 10 (L) | 0 (U) | 0 (U) | 10 (L) |
| `all_articles_in_prompt` [S] | 0 (U) | 10 (L) | 0 (U) | 0 (U) |
| `token_budget` [S] | 0 (U) | 10 (L) | 0 (U) | 0 (U) |
| `prompt_caching` [S] | 0 (U) | 10 (L) | 5 (P) | 0 (U) |
| `cite_or_abstain` [S] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |
| `eval_or_tests` [B] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

**F4 — Planning before acting**

| feature | A | B | C | D |
|---|---|---|---|---|
| `separate_plan_step` [S] | 10 (L) | 0 (U) | 10 (L) | 0 (U) |
| `structured_plan` [S] | 10 (L) | 0 (U) | 10 (L) | 0 (U) |
| `human_plan_approval` [S] | 0 (U) | 0 (U) | 10 (L) | 0 (U) |
| `reflect_or_replan` [S] | 3 (P) | 0 (U) | 3 (P) | 10 (L) |
| `iteration_cap` [S] | 5 (P) | 10 (L) | 3 (P) | 10 (L) |
| `tests` [B] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

**F5 — Eval with acceptance criteria vs 'make sure it works'**

| feature | A | B | C | D |
|---|---|---|---|---|
| `labeled_dataset` [S] | 10 (L) | 10 (L) | 0 (U) | 9 (L) |
| `numeric_threshold` [S] | 10 (L) | 0 (U) | 0 (U) | 0 (U) |
| `per_class_metrics` [S] | 10 (L) | 4 (P) | 0 (U) | 0 (U) |
| `automated_gate` [S] | 10 (L) | 10 (L) | 10 (L) | 3 (P) |
| `edge_case_coverage` [S] | 10 (L) | 10 (L) | 10 (L) | 10 (L) |
| `mocks_model` [B] | 3 (P) | 10 (L) | 10 (L) | 3 (P) |

## 5. Premise check (variant pairs with the same profile)

A pair is a **duplicate** if no semantic feature changes band (L/P/U) between the two prompts *and* no count differs by more than 1. Duplicate pairs cannot be used to tell prompts apart, so items using them were cut.

- **F1A ≡ F1B** (a permission gate vs an approval gate): DUPLICATE — no semantic feature separates them.
- F1A vs F1C: separated by one feature only: `human_approval` (10 vs 0).
- **F1A ≡ F1D** (a permission gate vs an audit log): DUPLICATE — no semantic feature separates them.
- F1B vs F1C: separated by one feature only: `human_approval` (10 vs 0).
- **F1B ≡ F1D** (an approval gate vs an audit log): DUPLICATE — no semantic feature separates them.
- F1C vs F1D: separated by one feature only: `human_approval` (0 vs 10).
- **F2A ≡ F2B** (an idempotent retry vs a plain retry): DUPLICATE — no semantic feature separates them.
- **F3A ≡ F3D** (retrieving the relevant articles for each ticket vs giving Claude a search tool for the articles): DUPLICATE — no semantic feature separates them.
- F4B vs F4D: separated by one feature only: `reflect_or_replan` (0 vs 10).

## 6. Coder agreement (second coder, 8 of 40 plans per family = 20%)

| family | feature cells | agree | % | Cohen's κ (pooled) | disagreements |
|---|---|---|---|---|---|
| F1 | 48 | 48 | 100.0 | 1.0 | none |
| F2 | 48 | 47 | 97.9 | 0.94 | transient_only 7/8 |
| F3 | 48 | 48 | 100.0 | 1.0 | none |
| F4 | 48 | 48 | 100.0 | 1.0 | none |
| F5 | 48 | 47 | 97.9 | 0.95 | automated_gate 7/8 |
| **all** | 240 | 238 | 99.2 | | |

Caveat: many features sit at 0/10 or 10/10, which inflates raw agreement and can depress κ; and both coders are the same model. The one-line judgement calls the coders reported (e.g. F1 `permission_scope` coded 1 whenever the tool is limited to billing tickets; `mocks_model` only when *Claude* is mocked) were NOT yet written back into the definitions above; a v2 should add them (and the F1 coders marked `permission_scope` and `audit_log` leniently, so those two F1 columns are the least trustworthy).

## 7. Files

- `runs/F1.json … F5.json`: every plan with its codes. `runs/raw/*.txt`: the 200 raw plans. `runs/summary.json`: frequencies and agreement.
- `coding/`: blind sheets, id keys, both coders' JSON.
