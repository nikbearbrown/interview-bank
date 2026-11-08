# INFO 7375: Prompt Engineering for Generative AI: jargon vocabulary test

Updated 2026-11-08. The whole pool is now a **jargon vocabulary test, multiple-answer only**. The question it asks: can a student use the field's terms precisely, so they can talk precisely to a language model and to Claude Code? It is tested like a French or Hindi vocabulary test: name the exact term for a described behaviour, tell near-synonyms apart, spot the imprecise word in a prompt to Claude, choose the rewrite that uses the exact terms. There are **no essay questions**.

The markdown files are the source; `json/multiple-answer.json` is generated from them and includes the answers. The [glossary](/Users/bear/Documents/CoWork/bear-textbooks/books/interview-bank/info-7375-prompt-engineering-for-generative-ai/GLOSSARY-jargon-midterm.md) lists every tested term.

| File | Set | Questions |
|---|---|---:|
| `00-foundations.md` | Foundations (midterm-prep sections 1-12) | 39 |
| `ch01-next-token-prediction-and-sampling.md` | Chapter 1: Next-token prediction and sampling | 36 |
| `ch02-prompt-contracts-and-evaluation.md` | Chapter 2: Prompt contracts and evaluation | 35 |
| `ch03-chat-assistant-agent.md` | Chapter 3: Chat, assistant, and agent | 36 |
| `ch04-the-agent-loop.md` | Chapter 4: The agent loop | 36 |
| `ch05-tools-and-permissions.md` | Chapter 5: Tools and permissions | 36 |
| `ch06-claude-code-and-diff-review.md` | Chapter 6: Claude Code and diff review | 36 |
| `ch07-retrieval-and-cowork.md` | Chapter 7: Retrieval and Cowork | 36 |
| `ch08-mcp-from-scratch.md` | Chapter 8: MCP from scratch | 36 |
| `ch09-training-and-configuration.md` | Chapter 9: Training and configuration | 35 |
| `ch10-planning-before-acting.md` | Chapter 10: Planning before acting | 36 |
| `ch11-tool-use-and-verification.md` | Chapter 11: Tool use and verification | 36 |
| `ch12-memory-and-multiple-agents.md` | Chapter 12: Memory and multiple agents | 36 |
| `ch13-evaluation-and-approval-gates.md` | Chapter 13: Evaluation and approval gates | 36 |
| `ch14-governance-and-ethics.md` | Chapter 14: Governance and ethics | 36 |
| `ch15-supervised-capstone.md` | Chapter 15: Supervised capstone | 36 |
| `j01-jargon-sampling-and-tokens.md` | Jargon test: sampling and tokens | 12 |
| `j02-jargon-prompt-structure-and-contracts.md` | Jargon test: prompt structure and contracts | 12 |
| `j03-jargon-agents-and-tools.md` | Jargon test: agents and tools | 12 |
| `j04-jargon-retrieval-and-training.md` | Jargon test: retrieval, fine-tuning and configuration | 12 |
| `j05-jargon-mcp.md` | Jargon test: MCP | 14 |
| `j06-jargon-evaluation-and-governance.md` | Jargon test: evaluation, approval gates and governance | 14 |
| `j07-jargon-prompts-to-claude-code.md` | Jargon test: saying it exactly to Claude Code | 16 |
| `k01-compress-and-decompress.md` | Fluency: a term and its checkable conditions | 37 |
| `k02-reading-agent-output.md` | Fluency: reading confident agent claims, plans and diffs | 35 |
| `k03-false-friends.md` | Fluency: terms with two meanings or confusable neighbours | 26 |
| | **Total** | **767** |

`k01` to `k03` (added 2026-11-08) go beyond vocabulary: unpack a term into checkable conditions, judge a confident agent claim against evidence, and pick the meaning that fits a context. A blind AI reader answered 14 questions from each file without the key and matched all 42 (210 of 210 statements).

`j01` to `j07` are new jargon-first sets (sampling and tokens, prompt structure and contracts, agents and tools, retrieval and training, MCP, evaluation and governance, saying it exactly to Claude Code). The foundations and chapter files keep the original topics reworded to test term use; essay skills are folded into them.

## Conversion counts
- Before: 989 multiple-answer questions and 943 essay prompts. Now: 767 multiple-answer questions (669 before the k sets), 0 essays.
- Old chapter and foundations MA were merged or dropped as near-duplicates or non-vocabulary facts: see the per-file `scripts/convert-report-*.md` (agents' counts are approximate).
- Essays not converted (calculation, code tracing, procedure, design opinion) are listed in those reports.

## Layout
- `multiple-answer/`: one document per set. `json/multiple-answer.json`: every question with its answers.
- `scripts/check_format.py` validates; `scripts/build_json.py` rebuilds the JSON. After editing: `python3 -I scripts/check_format.py && python3 -I scripts/build_json.py`.
- `archive-pre-jargon/`: the pre-conversion pool kept unchanged (989 MA, 16 essay files, their JSON, and `BRIEF.md`, the conversion brief).
- `CHEAT-SHEET.md` and `notes/` are unchanged apart from a glossary link.

## Rules for every question
- Exactly 5 statements (A-E), each true or false; 1 point each (5 points). Checked and true = 1; unchecked and false = 1; otherwise 0.
- Terms, not trivia: no dates, names, or numbers to compute. Transformer internals only at overview depth.
- Every question stands alone; plain, plausible wrong statements; no absolute-word tells.
- The `source` field names the topic for instructors; it is not part of the question.

## Status
Reworded and written by AI. A blind AI reader answered a sample of the questions without the key (agreement in the session notes). The instructor has not reviewed the answers. Nothing here is committed to git yet.
