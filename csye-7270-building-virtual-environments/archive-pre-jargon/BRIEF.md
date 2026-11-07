# Conversion brief: pool -> jargon vocabulary test (multiple-answer only)

Root: /Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/csye-7270-building-virtual-environments
Old material (read-only, never edit or delete): `archive-pre-jargon/multiple-answer/<base>.md` and `archive-pre-jargon/essay/<base>.md` (essay may be absent for a base).

## Goal
Bear's rule: the test question is "can the student use the terms precisely, so they can talk precisely to a language model?" So every item tests exact jargon: pick the exact word for a described behaviour, tell apart near-synonyms, term to meaning, meaning to term, spot the imprecise or wrong word in a prompt to an AI coding or art tool, choose the rewrite that uses the exact terms. Facts that are not vocabulary (numbers, procedures, tool trivia, how-to steps, design opinion) are DROPPED or reworked into a vocabulary question about the term involved. No essays in the output.

## Your output
For each base name assigned, write ONE new file `multiple-answer/<base>.md` (same base name as the old file; directory is under Root). Format (exactly as the old MA files; look at one old file and at `multiple-answer/j03-jargon-game-movement.md` for the style):

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
IDs: use the same id stem as the old file (e.g. MA-ch04.n, MA-vocab.n, MA-mcp.n, MA-unity.n, MA-unreal.n, MA-security.n, MA-verification.n), numbered 1..N fresh in the new file. Do not reuse old numbers deliberately.

## Work
1. Convert every old MA question: keep its topic and its terms, reword so it tests precise term use. You may keep good statements, but change the stem/framing to jargon (near-synonym pairs, wrong word in a prompt, name-the-behaviour). Reword, do not copy-paste if the old one tests a fact.
2. Convert the essay content (the matching essay file) into additional MA questions wherever the essay is about vocabulary (defining/contrasting terms, rewriting a vague prompt with exact words, spotting wrong words). Typically 1 new MA per vocabulary-bearing essay, sometimes 2. Essays that are not about vocabulary (pure procedure, design justification, calculation) are listed as NOT CONVERTED with the reason.
3. Drop old MA questions that test only facts; list each dropped id and the reason. Prefer reworking to dropping.
4. Cover terms thoroughly: each term in the old material should still be tested somewhere.

## House rules (strict)
- Exactly 5 statements A-E, each true or false on its own; at least 1 true and 1 false. Aim for true counts spread: about 10% one true, 33% two, 35% three, 20% four across your file; true answers spread over A-E (shuffle).
- Wrong statements must be plain and plausible: a near-synonym swapped in, a neighbouring term's meaning, a wrong stage. NO absolute-word tells in any statement: do not use only, always, never, every, all, none, any, must, cannot, entirely, solely, purely, completely, exactly one. ("each" is fine inside a true definition.)
- Each question stands alone. Never write "the chapter", "the course", "the book", "the lab". A reader who has used a game engine but not taken the class can answer from general knowledge plus the stem.
- Concepts and terms, not dates, versions, names, menu paths, default values or API signatures. Engine names are allowed when the term differs by engine (Godot, Unity, Unreal).
- Plain, short statements. Keys must be correct as standard usage in Godot/Unity/Unreal/Blender; if you are unsure of a fact, do not use it.
- No full student names, no personal names.
- Every `Why:` line explains the term, in one sentence.

## Validate
Run from Root: `python3 -I scripts/check_format.py multiple-answer/<base>.md` (must say 0 problems). Also grep your file for the forbidden absolute words in statement lines and fix them.

## Report
Write the report file named in your assignment, in markdown: per base name: old MA count, new MA count, reworded count, dropped count with ids and reasons, essays count, essays converted (how many new MA), essays NOT CONVERTED with ids and reasons, and the list of terms newly or especially tested (comma list, used to build the glossary). Keep it short. Reply to the caller with only one line: counts.
