# CSYE 7270: Building Virtual Environments (Godot edition): jargon vocabulary test

Updated 2026-11-06. The whole pool is now a **jargon vocabulary test, multiple-answer only**. The question it asks: can a student use the terms precisely, so they can talk precisely to a language model? Tested the way a French or Hindi vocabulary test is: name the exact word for a described behaviour, tell near-synonyms apart, spot the imprecise or wrong word in a prompt to an AI tool, choose the rewrite that uses the exact terms. There are **no essay questions**.

The markdown files are the source; `json/multiple-answer.json` is generated from them and includes the answers. The one-page-per-topic [glossary](GLOSSARY-jargon-midterm.md) lists every tested term.

| File | Set | Questions |
|---|---|---:|
| `00-engine-vocabulary.md` | Engine vocabulary (Godot, Unity, Unreal) | 29 |
| `01-mcp-fundamentals.md` | MCP fundamentals | 22 |
| `02-unity-agent-workflows.md` | Unity, Spark and agent workflows | 20 |
| `03-unreal-agent-workflows.md` | Unreal and agent workflows | 20 |
| `04-agent-security.md` | Agent security and local versus cloud execution | 20 |
| `05-agent-verification.md` | Agent testing, troubleshooting and engine comparisons | 19 |
| `ch00-the-toolchain.md` | Chapter 0: The toolchain | 22 |
| `ch01-scenes-nodes-and-signals.md` | Chapter 1: Scenes, nodes and signals | 25 |
| `ch02-game-art-and-sound-assets.md` | Chapter 2: Game art and sound assets | 26 |
| `ch03-3d-assets-and-the-blender-pipeline.md` | Chapter 3: 3D assets and the Blender pipeline | 27 |
| `ch04-scenes-collision-and-physics.md` | Chapter 4: Scenes, collision and physics | 32 |
| `ch05-game-design-documents-and-virtual-worlds.md` | Chapter 5: Game design documents and virtual worlds | 22 |
| `ch06-shader-foundations.md` | Chapter 6: Shader foundations | 29 |
| `ch07-materials-and-textures.md` | Chapter 7: Materials and textures | 28 |
| `ch08-shader-verification.md` | Chapter 8: Shader verification | 23 |
| `ch09-particle-effects.md` | Chapter 9: Particle effects | 23 |
| `ch10-animation-foundations.md` | Chapter 10: Animation foundations | 30 |
| `ch11-animation-and-interaction.md` | Chapter 11: Animation and interaction | 30 |
| `ch12-audio-and-triggers.md` | Chapter 12: Audio and triggers | 23 |
| `ch13-profiling-and-optimization.md` | Chapter 13: Profiling and optimization | 24 |
| `ch14-game-ai-and-systems.md` | Chapter 14: Game AI and systems | 24 |
| `j01-jargon-camera-movement.md` | Jargon test: camera movement | 10 |
| `j02-jargon-animation-movement.md` | Jargon test: animation movement | 10 |
| `j03-jargon-game-movement.md` | Jargon test: game movement | 10 |
| `j04-jargon-shaders-materials.md` | Jargon test: shaders and materials | 12 |
| `j05-jargon-sprites-rigs-colliders-states.md` | Jargon test: sprite sheets, rigs, colliders and state machines | 8 |
| `j06-jargon-from-essays.md` | Jargon test: from the essay prompts | 32 |
| `k01-compress-and-decompress.md` | Compress and decompress: a term and its checkable constraints | 29 |
| `k02-reading-agent-output.md` | Reading agent output: confident claims, scope violations, follow-ups that give evidence | 29 |
| `k03-false-friends.md` | False friends: words with two meanings or confusable neighbours | 20 |
| | **Total** | **678** |

`k01` to `k03` (added 2026-11-08) test applied use rather than recall: unpack a term into constraints, judge an agent's confident claim, and tell false friends apart. `j01` to `j06` are the jargon-first sets on camera, animation, game movement, shaders and materials, and sprite sheets, rigs, colliders and state machines. The others keep the original topics (engine vocabulary, chapters 0 to 14, agent/MCP workflows) reworded to test term use. Chapter 15 (final project) is not in the pool.

## Layout
- `multiple-answer/`: one document per set.
- `json/multiple-answer.json`: every question with its answers.
- `scripts/check_format.py` validates; `scripts/build_json.py` rebuilds the JSON. After editing: `python3 -I scripts/check_format.py && python3 -I scripts/build_json.py`.
- `archive-pre-jargon/`: the pre-conversion pool kept unchanged (366 multiple-answer questions, 175 essays including 16 jargon essays, their JSON, and the conversion brief). `SOURCES.md` still documents the supplemental agent sets.

## Rules for every question
- Exactly 5 statements (A-E), each true or false; 1 point each (5 points). Checked and true = 1; unchecked and false = 1; otherwise 0.
- Terms, not trivia: no dates, versions, menu paths, default values or API signatures.
- Every question stands alone; plain, plausible wrong statements; no absolute-word tells.
- The `source` field names the topic for instructors; it is not part of the question.

## Status
Reworded and written by AI. A blind AI reader answered the new questions without the key (agreement reported in the session notes). A game developer should read the physics, shader, audio and tool-use answers before an exam is built. Nothing here is committed to git yet.
