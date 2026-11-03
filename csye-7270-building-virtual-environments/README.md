# CSYE 7270: Building Virtual Environments (Godot edition)

Midterm and interview question pool in exam format, with supplemental cross-engine agent-development sets. The markdown files are the source; the JSON files are generated from them for the website and include the answers.

## Scope and emphasis

The pool covers every area of the course except the final project: the cross-engine vocabulary plus chapters 0 to 14 (toolchain, scenes and nodes, game art and sound assets, 3D assets, collision and physics, game design documents, shaders, materials and textures, shader verification, particles, animation, state machines, audio and triggers, profiling, game AI).

It is **terminology first**. Working with a coding agent means saying exactly what you want, and a student who cannot say exactly what a collider is versus a trigger, a sprite sheet versus a rig, a vertex shader versus a fragment shader, albedo versus a normal map, or a state machine versus nested conditionals will write a vague instruction and get the wrong thing built. Many questions are written as "say it to the agent" scenarios. The terms are the ones a studio expects a candidate to know in Godot, Unity or Unreal interviews. Chapter 15 (the final project) is not in the pool.

This is a pool to draw an exam from, not an exam. A midterm is a selection of questions from it.

Five supplemental sets extend the pool with MCP fundamentals, Unity/Spark and Unreal workflows, security, local versus cloud execution, troubleshooting, testing and engine comparisons. They are foundation sets rather than new course chapters, so the existing chapter numbering and final-project exclusion remain intact. Questions progress from foundational concepts through applied scenarios to advanced design and recovery problems; the instructor-facing `source` field records that emphasis. Product research and source-to-question mappings are in [MCP and agent workflow sources](SOURCES.md), checked November 3, 2026.

| Set | Multiple-answer | Essay |
|---|---:|---:|
| Engine vocabulary (Godot, Unity, Unreal) | 24 | 9 |
| MCP fundamentals | 12 | 8 |
| Unity, Spark and agent workflows | 12 | 8 |
| Unreal and agent workflows | 12 | 8 |
| Agent security and local versus cloud execution | 12 | 8 |
| Agent testing, troubleshooting and engine comparisons | 12 | 8 |
| Chapter 0: The toolchain | 16 | 6 |
| Chapter 1: Scenes, nodes and signals | 18 | 7 |
| Chapter 2: Game art and sound assets | 19 | 7 |
| Chapter 3: 3D assets and the Blender pipeline | 19 | 7 |
| Chapter 4: Scenes, collision and physics | 23 | 9 |
| Chapter 5: Game design documents and virtual worlds | 16 | 6 |
| Chapter 6: Shader foundations | 20 | 8 |
| Chapter 7: Materials and textures | 20 | 8 |
| Chapter 8: Shader verification | 17 | 6 |
| Chapter 9: Particle effects | 18 | 7 |
| Chapter 10: Animation foundations | 22 | 9 |
| Chapter 11: Animation and interaction | 22 | 9 |
| Chapter 12: Audio and triggers | 16 | 7 |
| Chapter 13: Profiling and optimization | 18 | 7 |
| Chapter 14: Game AI and systems | 18 | 7 |
| **Total** | **366** | **159** |

## Layout

- `multiple-answer/00-engine-vocabulary.md`, `01-mcp-fundamentals.md` through `05-agent-verification.md`, plus `multiple-answer/ch00-...ch14-*.md`: one document per set, many questions each.
- `essay/` : same.
- `json/multiple-answer.json` and `json/essay.json`: every question with its answer data (below).
- `scripts/check_format.py` validates the markdown; `scripts/build_json.py` rebuilds the JSON.
- `SOURCES.md` records dated research, authoritative references, question mappings and the supplemental sets' validation scope.

After editing a markdown file: `python3 -I scripts/check_format.py && python3 -I scripts/build_json.py`.

## The rules for every question

- **Concepts and terms, not trivia.** No dates, versions, release years, menu paths, default values or exact API signatures. A term is tested for what it means and how it differs from its neighbour.
- **Every question stands alone.** Someone who has used a game engine but never took the course can answer it from general knowledge plus what the stem says. No question refers to the course, its book, its labs or its projects.
- **Engine names are used** (Godot, Unity, Unreal) because the subject is engine vocabulary; where engines differ, the statement says which engine it is about.
- **Balance.** True-statement counts follow the spread of the other banks (about 11, 33, 35 and 21 percent for one, two, three and four true), true answers are spread across A to E, and false statements do not carry absolute-word giveaways.
- The `source` field names the topic area for instructors; it is not part of the question.

## Multiple-answer (5 points)

Exactly 5 statements (A-E), each true or false on its own. The student checks the statements they believe are true. 1 point per statement: **checked and true = 1; unchecked and false = 1; checked and false = 0; unchecked and true = 0.**

JSON per question: `id`, `chapter` (0-14, or null for vocabulary and supplemental foundation sets), `group`, `section`, `source`, `stem`, and `statements`: five objects with `label`, `text`, `correct` (true/false) and `explanation`. Foundation questions keep their set title in `section`; the shared `chapters.foundations` heading retains its original vocabulary title for compatibility.

## Essay (5 points)

Short essay scored on a rubric of exactly 5 items, 1 point each. The rubric is the answer key. JSON per question: `id`, `chapter`, `group`, `section`, `source`, `prompt`, and `rubric`.

Question IDs: `MA-vocab.n` / `ES-vocab.n` for the vocabulary set, `MA-chNN.n` / `ES-chNN.n` for chapter sets. Supplemental IDs use `MA-mcp.n`, `MA-unity.n`, `MA-unreal.n`, `MA-security.n`, `MA-verification.n`, and the corresponding `ES-` prefixes. Existing IDs and question content are preserved.

## How the original pool was built and checked

Sixteen sets were written in parallel from the field's terms, using the course chapters only to see scope, and engine facts were checked against the Godot, Unity and Unreal documentation; facts that could not be confirmed were left out. Every number in a scenario was recomputed in code. Reviewers who had not seen the keys then answered every multiple-answer question and reviewed every essay rubric; they matched the keys on 1,529 of 1,530 statements, flagged wording problems (trivia, ambiguity, giveaways, outside knowledge), and the findings were fixed. The revised questions were checked blind a second time. The writers, editors and reviewers are all AI, so a game developer should read the physics, audio and shader answers before they are used in an exam.

## Supplemental expansion

The expansion adds 60 multiple-answer questions (300 statements with explanations) and 40 essays (200 rubric points), taking the pool from 425 to 525 questions. It uses original scenarios and current primary documentation, with hypothetical tool contracts stated in the questions rather than invented vendor API claims. No release dates, menu paths or exact command signatures are tested. The new multiple-answer questions have 1, 2, 3 or 4 true statements in counts of 6, 20, 22 and 12 respectively (10%, 33.3%, 36.7%, 20%).

The supplemental content was reviewed for answer/rubric consistency and validated with the existing format checker, JSON regeneration, unique-ID and source/JSON parity checks, original-question preservation checks, numeric recomputation and diff inspection. The original pool's blind-review statistics above do not apply to these additions. No Unity/Unreal editor integration was executed as part of this content update; the scenarios are assessment material, not certified integration tests.
