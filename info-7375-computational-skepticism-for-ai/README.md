# INFO 7375: Computational Skepticism for AI: jargon vocabulary test

Updated 2026-11-06. The whole pool is now a **jargon vocabulary test, multiple-answer only**. The question it asks: can a student use the field's terms precisely, so they can talk precisely to a language model? It is tested the way a French or Hindi vocabulary test is: name the exact term for a described behaviour, tell near-synonyms apart (calibration vs accuracy, covariate shift vs concept drift, demographic parity vs equalized odds, provenance vs lineage), spot the imprecise or wrong word in a prompt to an AI tool, choose the rewrite that uses the exact terms. There are **no essay questions**.

The markdown files are the source; `json/multiple-answer.json` is generated from them and includes the answers. [GLOSSARY-jargon-midterm.md](GLOSSARY-jargon-midterm.md) lists every tested term with a one-line definition.

Three sets (55 questions) were added to the old pool on GitHub while this conversion was under way; they are kept as written and still need converting to the jargon style.

Scope: foundations plus chapters 1 to 7. Chapters 8 to 13 are not in the pool yet; add them as `ch08-...` files and the scripts pick them up.

| File | Set | Questions |
|---|---|---:|
| `00-foundations.md` | Foundations (probability and statistics) | 39 |
| `ch01-the-skeptics-toolkit.md` | Ch 1 The skeptic's toolkit | 38 |
| `ch02-probability-uncertainty-and-confidence.md` | Ch 2 Probability, uncertainty and confidence | 42 |
| `ch03-data-validation-and-provenance.md` | Ch 3 Data validation and provenance | 46 |
| `ch04-robustness-and-distribution-shift.md` | Ch 4 Robustness and distribution shift | 48 |
| `ch05-model-explainability.md` | Ch 5 Model explainability | 41 |
| `ch06-bias-in-the-pipeline.md` | Ch 6 Bias in the pipeline | 58 |
| `ch07-fairness-metrics.md` | Ch 7 Fairness metrics | 37 |
| `j01-jargon-probability-and-confidence.md` | Jargon test: probability and confidence | 12 |
| `j02-jargon-data-validation-and-provenance.md` | Jargon test: data validation and provenance | 12 |
| `j03-jargon-robustness-and-shift.md` | Jargon test: robustness and distribution shift | 12 |
| `j04-jargon-explainability.md` | Jargon test: explainability | 12 |
| `j05-jargon-bias-and-fairness.md` | Jargon test: bias and fairness | 14 |
| `j06-jargon-wrong-word-right-word.md` | Jargon test: wrong word, right word | 14 |
| `ch03-experiment-assumptions.md` | Ch 3 Experiment assumptions (added 2026-11-07, original wording, not yet converted) | 20 |
| `ch06-confounders.md` | Ch 6 Confounders (added 2026-11-07, original wording, not yet converted) | 20 |
| `ch06-observational-data-and-controls.md` | Ch 6 Observational data and controls (added 2026-11-07, original wording, not yet converted) | 15 |
| | **Total** | **480** |

Conversion: all 269 old multiple-answer questions were reworded (none dropped; calculation-only items were reworked into questions about the terms), 156 questions are new (from the 127 old essay prompts and the `j01` to `j06` sets).

## Layout
- `multiple-answer/`: one document per set.
- `json/multiple-answer.json`: every question with its answers.
- `scripts/check_format.py` validates; `scripts/build_json.py` rebuilds the JSON. After editing: `python3 -I scripts/check_format.py && python3 -I scripts/build_json.py`.
- `archive-pre-jargon/`: the pre-conversion pool kept unchanged (269 multiple-answer questions, 127 essays, their JSON, the old README and the conversion brief).

## Rules for every question
- Exactly 5 statements (A-E), each true or false; 1 point each (5 points). Checked and true = 1; unchecked and false = 1; otherwise 0.
- Terms, not trivia or calculation: no dates, names or arithmetic to perform.
- Every question stands alone; plain, plausible wrong statements; no absolute-word tells (one true definition keeps "missing completely at random" because it is the term's name).
- The `source` field names the topic for instructors; it is not part of the question.

## Status
Written by AI. A blind AI reader answered a sample of 96 questions without the key; result: 480 of 480 statements (96 questions) matched the key; three wordings the readers flagged as loose were tightened. A statistician should read the answers before an exam is built. Nothing here is committed to git.
