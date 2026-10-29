# INFO 7375: Computational Skepticism for AI

Midterm question pool in exam format. The markdown files are the source; the JSON files are generated from them for the website and include the answers.

## Scope

Foundations (the probability and statistics the course assumes) plus the first seven chapters, which the syllabus groups as claims, probability and data provenance (chapters 1 to 3) and robustness, explanation, bias and fairness (chapters 4 to 7). Chapters 8 to 13 (agents, delegation, visualization, uncertainty communication, accountability, limits) are not in this pool yet; add them as `ch08-...` to `ch13-...` files and the same scripts pick them up.

This is a pool to draw an exam from, not an exam. A midterm is a selection of questions from it.

| Set | Multiple-answer | Essay |
|---|---:|---:|
| Foundations (probability and statistics) | 27 | 12 |
| Ch 1 The skeptic's toolkit | 31 | 15 |
| Ch 2 Probability, uncertainty and the confidence illusion | 34 | 15 |
| Ch 3 Data validation and provenance | 32 | 15 |
| Ch 4 Robustness and distribution shift | 32 | 16 |
| Ch 5 Model explainability | 32 | 15 |
| Ch 6 Bias in the pipeline | 30 | 15 |
| Ch 7 Fairness metrics | 30 | 15 |
| **Total** | **248** | **118** |

## Layout

- `multiple-answer/00-foundations.md` plus `multiple-answer/ch01-...ch07-*.md`: one document per chapter, many questions each.
- `essay/00-foundations.md` plus `essay/ch01-...ch07-*.md`: same.
- `json/multiple-answer.json` and `json/essay.json`: every question with its answer data (below).
- `scripts/check_format.py`: validates the markdown. `scripts/build_json.py`: rebuilds the JSON.

After editing a markdown file: `python3 -I scripts/check_format.py && python3 -I scripts/build_json.py`.

## The rule for every question

A question tests the topic, never whether the student read the chapter. Anyone who knows the topic, without having read the chapter, must be able to answer it. So no question refers to "the chapter", "the book", "the lab" or a chapter-only example, name, number or rule. A scenario states every fact it needs. A term the book coined is replaced by the standard term or defined in the stem. Where the book makes a contestable or unproven claim, the question tests the general principle instead of the claim. The `source` field names the chapter section where the topic is taught; it is a pointer for instructors and is not part of the question.

## Multiple-answer (5 points)

Exactly 5 statements (A-E), each true or false on its own. The student checks the statements they believe are true. 1 point per statement: **checked and true = 1; unchecked and false = 1; checked and false = 0; unchecked and true = 0.**

JSON per question: `id`, `chapter` (1-13, or null for foundations), `group`, `section`, `source`, `stem`, and `statements`: five objects with `label`, `text`, `correct` (true/false) and `explanation`.

## Essay (5 points)

Short essay scored on a rubric of exactly 5 items, 1 point each. The rubric is the answer key.

JSON per question: `id`, `chapter`, `group`, `section`, `source`, `prompt`, and `rubric`: five objects with `point` (1-5) and `text`.

Question IDs: `MA-<section>.<n>` / `ES-<section>.<n>` for foundations, `MA-chNN.<n>` / `ES-chNN.<n>` for chapters.

## How the pool was built

Each chapter's questions were written from the topic, using the chapter and its lesson only to see the scope, and checked against the standard definitions in the field. Every number in a scenario was recomputed in code. The sources it drew on for coverage: the course's probability-and-statistics reference, the lesson knowledge checks, and the topics a large third-party interview bank covers for statistics and machine learning (topics only; no third-party question text is reused). That bank is thin on this course's distinctive material (calibration, explanation versus the appearance of explanation, fairness tradeoffs), so most of those questions come from the field, not from it.

Where the manuscript has competing drafts or a contestable claim, the questions avoid it. In particular, predictive parity (equal precision) and score calibration are treated as distinct, and fairness impossibility results are stated with their assumptions.
