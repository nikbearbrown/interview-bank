# Conversion brief: INFO 7375 pool -> jargon vocabulary test (multiple-answer only)

Root: /Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/info-7375-computational-skepticism-for-ai
Old material (read-only, never edit or delete): `archive-pre-jargon/multiple-answer/<base>.md` and `archive-pre-jargon/essay/<base>.md`.
Style models (read first): `/Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/csye-7270-building-virtual-environments/multiple-answer/j06-jargon-from-essays.md` and `ch04-scenes-collision-and-physics.md`.

## Goal
Bear's rule: the test question is "can the student use the field's terms precisely, so they can talk precisely to a language model?" Tested like a French or Hindi vocabulary test: name the exact term for a described behaviour or situation; tell near-synonyms apart (calibration vs accuracy vs discrimination, covariate shift vs concept drift vs label shift, demographic parity vs equalized odds vs predictive parity, provenance vs lineage, validation vs verification, confidence interval vs credible interval, p-value vs posterior probability, sensitivity vs specificity vs precision, explanation vs interpretability, feature importance vs causal effect, sampling bias vs selection bias vs measurement bias, and the real pairs in the old material); spot the imprecise or wrong word in a prompt to an AI tool or analyst; choose the rewrite that uses exact terms. Calculations, derivations, procedures, and facts that are not vocabulary are DROPPED or reworked into a question about the term involved (a question may use a tiny number only to describe a situation whose answer is a term, never to make the student calculate). No essays in the output.

## Format (exactly)
```
# <same H1 title as the old file>

## MA-<id>.<n>

<stem ending with: Check each statement that is true. Each statement is worth 1 point (5 points total).>

- [ ] A. ...
- [ ] B. ...
- [ ] C. ...
- [ ] D. ...
- [ ] E. ...

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: ...
- B: ...
- C: ...
- D: ...
- E: ...

**Source:** <short topic label>
```
IDs: same stem as the old file (MA-found.n for 00-foundations? use the id stem the old file uses, e.g. MA-ch02.n), numbered 1..N fresh.

## Work
1. Convert every old MA question: keep its topic and terms, reword so it tests precise term use. Reword, do not copy-paste.
2. Convert the matching essay file: every essay prompt's underlying skill becomes 1 (sometimes 2) new MA questions where it bears vocabulary. Essays that are pure calculation/procedure/argument with no term skill: list as NOT CONVERTED with reason.
3. Drop old MA questions that test only calculation or facts; list each dropped id and reason. Prefer reworking to dropping.
4. Cover every term in the old material somewhere.

## House rules (strict)
- Exactly 5 statements A-E, each true or false on its own; at least 1 true and 1 false. True counts spread: about 10% one true, 33% two, 35% three, 20% four across the file; true answers spread over A-E.
- Wrong statements plain and plausible: a near-synonym swapped in, a neighbouring term's meaning, a wrong stage. NO absolute-word tells in any statement: do not use only, always, never, every, all, none, any, must, cannot, entirely, solely, purely, completely, exactly one. ("each" is fine inside a true definition.)
- Each question stands alone. Never write "the chapter", "the course", "the book", "the lab", "the lesson". A reader who knows the field but did not take the class can answer from general knowledge plus the stem.
- Concepts and terms, not dates, names, trivia. No personal names (Bayes' rule, Simpson's paradox are term names and fine).
- Plain, short statements. Keys must be correct under standard usage in statistics/ML; if unsure of a fact, do not use it.
- Every `Why:` line explains the term in one sentence.

## Validate
From Root: `python3 -I scripts/check_format.py multiple-answer/<file>.md` must say 0 problems. Grep your file's statement lines for the forbidden absolute words and fix them.

## Report
Write the report file named in your assignment (markdown): per file: old MA count, new MA count, reworded count, dropped ids+reasons, essay count, essays converted (how many new MA), essays NOT CONVERTED with reasons, and a comma list of the terms tested (for the glossary). Reply to the caller with one line: counts.
