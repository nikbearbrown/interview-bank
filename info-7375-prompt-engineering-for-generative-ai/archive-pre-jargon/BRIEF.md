# Conversion brief: INFO 7375 pool -> jargon vocabulary test (multiple-answer only)

Root: /Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/info-7375-prompt-engineering-for-generative-ai
Old material (read-only, never edit or delete): `archive-pre-jargon/multiple-answer/<base>.md` and `archive-pre-jargon/essay/<base>.md`. Reference model: the finished CSYE 7270 conversion at /Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/csye-7270-building-virtual-environments/multiple-answer/ (look at j03-*.md and one ch*.md for style). Course vocabulary also lives in Root/CHEAT-SHEET.md and Root/notes/mcp-exam-notes.md (read only; use for terms).

## Goal
Bear's rule: the test question is "can the student use the field's terms precisely, so they can talk precisely to a language model and to Claude Code?" Every item tests exact jargon, like a French or Hindi vocabulary test: name the exact term for a described behaviour; term to meaning; meaning to term; tell near-synonyms apart (token vs word, temperature vs top-p, system prompt vs user turn, tool_use vs tool_result, agent loop vs workflow, context window vs memory, retrieval vs fine-tuning, MCP server vs client, permission vs approval gate, eval vs test, hallucination vs error, prompt contract, diff review, planning before acting); spot the imprecise or wrong word in a prompt to Claude / Claude Code; choose the rewrite that uses the exact terms. Facts that are not vocabulary (numbers, calculations, code trivia, how-to steps, opinion) are DROPPED or reworked into a question about the term involved. No essays in the output.

## Your output
Write ONE new file `multiple-answer/<base>.md` (same base name as the old; directory under Root). Format exactly:

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
(foundations file has several `# N. section title` H1 headings; keep those, and put each question under the right one. Heading-1 lines may only be section titles.)
IDs: same id stem as the old file (e.g. MA-ch05.n; foundations MA-found.n), numbered 1..N fresh.

## Size and method
The old pool is large and heavily overlapping (about 60 MA and 60 essays per chapter, many near-duplicates). TARGET 30 to 36 new questions per chapter file (foundations: 36 to 40; j files: as assigned). Method:
1. Read the old MA and essay files for your base. List the distinct TERMS and term-contrasts they teach.
2. Write questions so every distinct term/contrast is tested at least once, with near-duplicate questions merged (dedupe). Convert the essay prompts: each essay's underlying skill that is about vocabulary or a term contrast becomes MA content (a stem naming the situation, five statements); fold several essays into one question when they cover the same contrast. Essays that are pure calculation, procedure or design opinion are listed NOT CONVERTED with reason.
3. Reword, do not copy: change framing to name-the-term, near-synonym pair, wrong word in a prompt to Claude, or best rewrite. Keep good plausible wrong statements.
4. Report dropped counts honestly: dropped = old MA that was merged into another or removed as non-vocabulary (give counts and a few ids; full id list not needed).

## House rules (strict)
- Exactly 5 statements A-E, each true or false on its own; at least 1 true and 1 false. True-counts spread: about 10% one true, 33% two, 35% three, 20% four; true answers spread over A-E (shuffle).
- Wrong statements plain and plausible: a near-synonym swapped in, a neighbouring term's meaning, a wrong stage. NO absolute-word tells in any statement: do not use only, always, never, every, all, none, any, must, cannot, entirely, solely, purely, completely, exactly one, just. ("each" is fine inside a true definition.)
- Each question stands alone. Never write "the chapter", "the course", "the book", "the lab". A reader who has used an AI chat assistant and Claude Code but not taken the class can answer from general knowledge plus the stem. A scenario states every fact it needs.
- Concepts and terms, not dates, versions, personal names, model names or numbers. Transformer internals only at overview depth (what attention is for, not the maths). No formulas to compute.
- Keys must be correct as standard usage in the field (LLM, Claude API, Claude Code, MCP). If unsure of a fact, do not use it.
- No student names, no personal names.
- Every `Why:` line explains the term in one sentence.
- Do NOT write "Each statement is worth..." twice; stem ends with that sentence once.

## Validate
Run from Root: `python3 -I scripts/check_format.py multiple-answer/<base>.md` (must say 0 problems; it counts essay as 0). Then grep statement lines (lines starting `- [ ]`) for the forbidden words (case-insensitive, whole word) and fix.

## Report
Write the report file named in your assignment (markdown): per base: old MA count, old essay count, new MA count, dropped/merged count, essays converted vs NOT CONVERTED with ids+reasons, and the comma list of terms especially tested (used to build the glossary; give each term with a one-line precise definition, as `term :: definition`, grouped under a heading of your topic). Keep it short. Reply to the caller with one line: counts.
