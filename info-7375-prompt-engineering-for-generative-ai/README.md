# INFO 7375: Prompt Engineering for Generative AI

Exam-format questions. The markdown files are the source; the JSON files are generated from them for the website and include the answers.

## Layout

- `multiple-answer/00-foundations.md` plus `multiple-answer/ch01-...ch15-*.md`: one document per chapter, many questions each.
- `essay/00-foundations.md` plus `essay/ch01-...ch15-*.md`: same.
- `json/multiple-answer.json` and `json/essay.json`: every question with its answer data (below).
- `scripts/check_format.py`: validates the markdown. `scripts/build_json.py`: rebuilds the JSON.

After editing a markdown file: `python3 -I scripts/check_format.py && python3 -I scripts/build_json.py`.

## The rule for every question

A question tests the topic, never whether the student read the chapter. Anyone who knows the topic, without having read the chapter, must be able to answer it. So no question refers to "the chapter", "the book", "the lab" or a chapter-only example, name, number or rule. A scenario states every fact it needs. A term the chapter coined is replaced by the standard term or defined in the stem. The `source` field names the chapter section where the topic is taught; it is a pointer for instructors and is not part of the question.

## Multiple-answer (5 points)

Exactly 5 statements (A-E), each true or false on its own. The student checks the statements they believe are true. 1 point per statement: **checked and true = 1; unchecked and false = 1; checked and false = 0; unchecked and true = 0.**

JSON per question: `id`, `chapter` (1-15, or null for foundations), `group`, `section`, `source`, `stem`, and `statements`: five objects with `label`, `text`, `correct` (true/false) and `explanation`.

## Essay (5 points)

Short essay scored on a rubric of exactly 5 items, 1 point each. The rubric is the answer key.

JSON per question: `id`, `chapter`, `group`, `section`, `source`, `prompt`, and `rubric`: five objects with `point` (1-5) and `text`.

Question IDs: `MA-<section>.<n>` / `ES-<section>.<n>` for foundations, `MA-chNN.<n>` / `ES-chNN.<n>` for chapters.
