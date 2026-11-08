# predict-the-prompt (INFO 7375 Computational Skepticism): PILOT

Built 2026-11-08. Draft only: not run on students, not committed, no existing file touched.

## What was built
- `EXAM-DRAFT.md`: a 41-point paper with 8 item types: matching (prompts to plans), prompt to most likely plan (MC), plausibility (likely/plausible/unlikely), feature forecasting (banded scoring), attribution, predict-and-explain, minimal-edit repair (with run protocol), plus the cut list. Every item has a KEY block with the answer, observed frequencies and backing plan ids.
- `KEY-AND-RUNS.md`: configuration, 30 feature definitions, all frequency tables, coder agreement, premise check, cost.
- `runs/F1.json` to `runs/F5.json`: 200 raw plans with prompts. `runs/F1B_repair_demo.json`: 10 plans for the repair item.
- `spec/`: families, features and scripts (`python3 spec/analyze.py`, `build_docs.py`, `build_key.py`) so the exam and key regenerate from the data.

Design: 5 families (calibration; hold-out vs cross-validation; confounder; provenance vs schema; covariate shift vs concept drift) x 4 one-phrase versions x 10 plans, written by `claude-sonnet-5-5` sub-agents, coded on binary features by blind sub-agent coders (second coder on 20%: 97.5% cell agreement).

## What was cut (premise check)
- Calibration vs accuracy: the model treats 'accuracy of the predicted probabilities' as calibration. Identical plans for calibration, accuracy and overconfidence. Cut as a keyed item; kept as a teaching item.
- Hold out vs cross-validate: identical profiles. Cut.
- Provenance vs lineage: identical profiles. Cut.
- Weak pairs (flagged, not used as pairs): concept drift vs covariate shift, schema vs statistical distributions, control-the-confounder vs randomize.
- Fairness (demographic parity vs equalized odds) was not piloted; it is the first family to add.

## Honest limits
- Sub-agent plans, not an agent harness. 10 plans per version came from one context, so they are not 10 independent draws.
- Same-model coders; 8 disagreements not adjudicated by a human.
- 10 plans per cell: band edges are noisy. The key describes this model on this date only.

## Cost
35 sub-agents, about 2.6M tokens (see `KEY-AND-RUNS.md`). Single-plan sub-agents would be about 14M for 200 plans.

## What a full version needs
1. Independent sampling (API calls, 30+ plans per version, temperature recorded) instead of batches from one context.
2. More families (fairness, explainability, robustness, bias in the pipeline) and 6 to 8 versions each, so more pairs survive the premise check.
3. Rewrite versions that failed (use phrases the model separates: 'discrimination', 'nested', 'label shift', 'schema' vs 'provenance').
4. Human adjudication of coder disagreements; a second coder model family.
5. Rerun the key when the model changes; keep a student-safe copy with KEY blocks stripped.
6. A repair-item grading budget (about 150k tokens per student edit).
