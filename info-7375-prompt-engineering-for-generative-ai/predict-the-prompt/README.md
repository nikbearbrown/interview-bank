# predict-the-prompt — pilot (INFO 7375 Prompt Engineering for Generative AI)

Built 2026-11-08. Nothing committed or pushed. No existing files were edited.

## What was built

A pilot of "predict the prompt" exams whose answer key comes from sampling, not opinion.

- `EXAM-DRAFT.md` — the exam paper: 7 items (matching, prompt→plan MC, plausibility, feature forecasting, attribution, predict-and-explain, minimal-edit repair), 20 points. Every item shows key, frequencies and backing plans.
- `KEY-AND-RUNS.md` — pinned configuration, the 20 prompts, features, frequency tables, premise check, coder agreement.
- `runs/` — `F1.json … F5.json` (each plan with its feature codes), `runs/raw/*.txt` (200 raw plans), `PLAN-BRIEF.md` (the fixed project description given to every run), `summary.json`.
- `coding/` — blind coding sheets, id keys, both coders' output. `prompts.json`, `features.json`, and the four scripts (`build_sheets.py`, `analyze.py`, `build_docs.py`, `build_key.py`) regenerate everything.

Five prompt families, each a base prompt with one phrase swapped across four variants: tool use gate (permission / approval / rate limit / audit log), retry (idempotent / plain / circuit breaker / timeout), retrieval vs facts in the prompt, planning before acting, and eval with acceptance criteria vs "make sure it works".

## What was cut (premise check)

A pair of prompts is cut as a discriminator when no semantic feature separates it.

- **Permission gate vs approval gate (F1A/F1B): identical.** 10/10 plans for both add a human approval path and a pending-refund queue. The course's headline contrast did not survive sampling, so no item asks it. (Finding in itself.)
- **Audit log (F1D) ≡ permission gate and approval gate (F1A, F1B).** Plans for "audit log" add approval thresholds on their own. Only the rate-limit prompt (F1C) differs, on one feature (human approval 0/10). F1 is used only for the Item 6 contrast.
- **Idempotent retry vs plain retry (F2A/F2B): identical.** Every plan notices `save_reply` is a database write and adds idempotency even for "plain retry". Used in Item 3a as a surprise instead of a contrast.
- **Retrieval vs search tool (F3A/F3D): identical** (10/10 retrieval index both). Item 2 asks only about the "all articles in the prompt" prompt, where one plan fits.
- Cut by design: no matching item for F1, F2 or F3 (each has a duplicate pair); matching uses F4, the only family with four distinguishable variants. The "context window vs memory file" family from the brief was not built (five families only).
- Features that are 10/10 or 0/10 in every variant (e.g. tests, `tool_schema`, `amount_limit`, `edge_case_coverage`) were not keyed. The behavioral ones (mocked tests) appear only in Item 4c at half weight.

## Coder agreement

Second coder on 20% (8 of 40 plans per family): 238 of 240 feature cells agree (99.2%); κ 0.94–1.0 per family. Caveats in `KEY-AND-RUNS.md` §6: many features are all-0/all-1, both coders are the same model, and F1's `permission_scope`/`audit_log` coding is lenient.

## Cost

- 200 plan runs (one sub-agent each, `sonnet`, about 70k reported tokens each, mostly fixed harness context), plus 10 coder runs (5 primary, 5 second) and 2 orchestrator sub-agents. No run discarded. 40 plans (20%) were independently double-coded.
- Wall-clock: roughly an hour, mostly the cap of 20 concurrent sub-agents.
- Known weakness found: launching 200 sub-agents directly floods the parent session with notifications; use an orchestrator sub-agent that spawns them.

## Honest limits

- A plan here is a sub-agent plan, not Claude Code plan mode. Sampling parameters are harness defaults; the exact model id was not returned by the tool.
- Keys depend on the project description. Changing it (for example, saying nothing about `save_reply` being a database write) would change F2.
- Item 6's explanation of why (rate limit read as a sufficient control, a log as insufficient) is a hypothesis; the frequencies are the measured part.
- Item 7: only one repair (a 6-word replacement) was run; student repairs would be graded by running 10 plans each.

## What a full version needs

1. Replace "sub-agent plan" with real Claude Code plan-mode runs, or the API with a pinned model id and temperature; record the resolved model id.
2. 20–30 runs per prompt (10 gives ±15 points of noise at the band edges; edge counts such as 7/10 or 2/10 should not be keyed).
3. Redesign F1/F2/F3 prompts so the course's contrasts actually bite (e.g. drop the project's mention that `save_reply` is a database write, or name different stakes), then re-run the premise check; pre-register which variants must differ.
4. A different model family as second coder, and a human audit of 10% of the codes; write the coders' judgement calls back into the feature definitions.
5. Item 7 graded by an automated run harness (diff counter, 10 plan runs, coder agent); a repair bank pre-run on 5–10 candidate edits.
6. Build the other two courses' families on the same harness; budget roughly 200 sub-agent runs per 5 families at 10 runs.
7. Decide how often to re-key: models change, so each exam version should be stamped with date + model and re-sampled before reuse.
