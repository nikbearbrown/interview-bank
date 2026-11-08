# KEY-AND-RUNS — configuration, features, frequencies, agreement (pilot)

## 1. Configuration (record of how the plans were made)
- **Date:** 2026-11-08. **Plans:** 5 families × 4 prompts × 10 = **200**. Each prompt = base prompt **A** + three altered prompts **B/C/D**, each differing from A by one phrase (edit recorded in every `runs/*.json` as `edit_from_base`).
- **Plan generator:** a fresh Claude Code **sub-agent per plan** (Agent tool, `subagent_type: general-purpose`, `model: "sonnet"`). The harness did **not report the resolved model id**, so the exact version is unrecorded; the generating session itself ran as claude-sonnet-5-5. Do not cite a version for the plans.
- **How plans were requested:** each sub-agent read a one-prompt job file (`Project (fixed): a small Godot 4 2D platformer. Scene tree: a Player (CharacterBody2D with Sprite2D, CollisionShape2D, script player.gd), a TileMapLayer for ground and platforms, two enemy scenes, and one level scene level_01.tscn. The developer asks: "<prompt>". Write the plan you would follow… numbered list, AT MOST 8 steps, 1-2 sentences per step, NO code. Plan only.`), then saved the plan with the Write tool. Default sampling parameters (temperature etc. are **not controllable or recorded** through the sub-agent interface).
- **This is a sub-agent plan, not Claude Code plan mode.** Plan mode has repo access, tool reads and an approval step; these plans were written without seeing any project files, so they hedge ("open level_01.tscn and check…") far more than a repo-aware plan would.
- **Order:** samples were launched interleaved (sample k of all 20 prompts in one batch, 10 batches) to avoid order or time-of-day effects within a prompt.
- Every plan contained exactly 8 numbered steps (checked), 186–295 words.
- **Cost:** 200 plan runs + 10 coder runs = **210 sub-agent runs**. Harness-reported usage ≈69k tokens per plan run (almost all fixed agent overhead; the plan itself is ~330 tokens) and ≈74–97k per coder run: **≈14.7M tokens total**.

## 2. Prompts

### F1 — Movement and collision

- **F1A** (base): “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision mask, with movement done in _physics_process.”
- **F1B** ('to the player's collision mask' -> 'to the player's collision layer'): “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision layer, with movement done in _physics_process.”
- **F1C** ('_physics_process' -> '_process'): “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision mask, with movement done in _process.”
- **F1D** ('putting the platforms on collision layer 2' -> 'setting the platforms' collision mask to 2'): “Players fall through the platforms. Fix it by setting the platforms' collision mask to 2 and adding layer 2 to the player's collision mask, with movement done in _physics_process.”

### F2 — Jump feel

- **F2A** (base): “Make the jump feel forgiving: add 0.1 s of coyote time and a 0.1 s jump buffer.”
- **F2B** ('coyote time' -> 'a double jump'): “Make the jump feel forgiving: add a double jump and a 0.1 s jump buffer.”
- **F2C** ('a 0.1 s jump buffer' -> 'variable jump height'): “Make the jump feel forgiving: add 0.1 s of coyote time and variable jump height.”
- **F2D** ('0.1 s of coyote time' -> '2 s of coyote time'): “Make the jump feel forgiving: add 2 s of coyote time and a 0.1 s jump buffer.”

### F3 — Camera

- **F3A** (base): “Add a follow camera with a deadzone so small player movements do not move the view.”
- **F3B** ('a deadzone so small player movements do not move the view' -> 'look-ahead in the facing direction'): “Add a follow camera with look-ahead in the facing direction.”
- **F3C** ('a deadzone so small player movements do not move the view' -> 'screen shake on hard landings'): “Add a follow camera with screen shake on hard landings.”
- **F3D** ('a deadzone' -> 'drag margins' (synonym control)): “Add a follow camera with drag margins so small player movements do not move the view.”

### F4 — Animation

- **F4A** (base): “Animate the player (idle, run, jump, fall) using an AnimationTree with a state machine.”
- **F4B** ('a state machine' -> 'a blend tree'): “Animate the player (idle, run, jump, fall) using an AnimationTree with a blend tree.”
- **F4C** ('an AnimationTree with a state machine' -> 'keyframes on an AnimationPlayer'): “Animate the player (idle, run, jump, fall) using keyframes on an AnimationPlayer.”
- **F4D** (append 'and easing on the transitions' to base phrase): “Animate the player (idle, run, jump, fall) using an AnimationTree with a state machine and easing on the transitions.”

### F5 — Shader and material

- **F5A** (base): “Give the ground tiles a material that uses a normal map so they react to the 2D lights.”
- **F5B** ('a normal map' -> 'roughness'): “Give the ground tiles a material that uses roughness so they react to the 2D lights.”
- **F5C** ('uses a normal map so they react to the 2D lights' -> 'scrolls by shifting the UV over time'): “Give the ground tiles a material that scrolls by shifting the UV over time.”
- **F5D** ('uses a normal map so they react to the 2D lights' -> 'tints them by multiplying the albedo'): “Give the ground tiles a material that tints them by multiplying the albedo.”

## 3. Features (binary; judged from the plan text alone; coders never saw the prompt or variant)
Code 1 only if the plan explicitly does/states it; mentioning a term in order to say *not* to do it, or to say it is prevented, = 0.

**F1 — Movement and collision**

- `MASK_PLAYER`: The plan says the PLAYER's collision MASK should include (be set to include) the platform layer.
- `LAYER_PLAYER`: The plan changes the PLAYER's collision LAYER (sets it or adds a layer to it) as part of the fix.
- `PLATFORM_LAYER`: The plan puts the platforms/tilemap on a specific collision layer (sets the platform's own layer).
- `PHYSICS_PROCESS`: The plan says movement / move_and_slide belongs in (or should be confirmed in/moved to) _physics_process.
- `PROCESS_MOVEMENT`: The plan puts or keeps movement code in _process (as the intended place, not merely as a mistake to remove).
- `PUSHBACK`: The plan explicitly says part of the request is wrong, unnecessary or confused, or deliberately deviates from it (e.g. 'rather than', 'actually', 'instead').

**F2 — Jump feel**

- `COYOTE`: Implements coyote time: a short grace timer after walking off a ledge during which a jump is still allowed.
- `BUFFER`: Implements a jump buffer: remembers a jump press made shortly before landing and fires it on landing.
- `VARJUMP`: Implements variable jump height (releasing the jump button early cuts the upward velocity).
- `DOUBLEJUMP`: Implements a double jump / extra air jump counter.
- `VALUE_FLAG`: The plan comments that a requested duration is too long/unusual, or uses a smaller value than the one requested, or advises a typical range.
- `TUNING_STEP`: [BEHAVIORAL] The plan includes a playtesting / tuning step or exposes values as tunable (exported) parameters.

**F3 — Camera**

- `CAMERA2D`: Adds a Camera2D node (as child of the player or following it).
- `DEADZONE`: Uses a deadzone / drag margins (camera stays still for small player movement).
- `LOOKAHEAD`: Implements look-ahead: camera offset ahead of the player by facing direction or velocity.
- `SHAKE`: Implements screen shake (random/decaying offset or trauma) triggered by an event.
- `SMOOTHING`: Enables camera position smoothing / lerped following.
- `LIMITS`: [BEHAVIORAL] Sets camera limits to the level bounds.

**F4 — Animation**

- `ANIMTREE`: Uses an AnimationTree node.
- `STATE_MACHINE`: Uses an AnimationNodeStateMachine / state machine with named animation states and transitions (idle/run/jump/fall).
- `BLEND`: Uses a BlendSpace, BlendTree or blend parameter (e.g. blending idle/run by speed).
- `KEYFRAMES`: Authors keyframed animation tracks in an AnimationPlayer (keyframes on properties such as sprite frame/position).
- `EASING`: Mentions easing curves, transition curves or crossfade/blend times on transitions.
- `SCRIPT_DRIVEN`: [BEHAVIORAL] A script drives the animation each frame from velocity / is_on_floor (sets parameters or calls travel/play).

**F5 — Shader and material**

- `CANVAS_ITEM`: Uses a canvas_item shader or ShaderMaterial/CanvasItemMaterial for 2D (explicitly 2D/canvas_item context).
- `NORMAL_MAP`: Uses a normal map texture (e.g. via CanvasTexture normal) for lighting.
- `LIGHT2D`: Adds or ensures a Light2D/PointLight2D/DirectionalLight2D in the scene.
- `UV_SCROLL`: Scrolls/shifts the UV (offset by TIME) in a shader.
- `ALBEDO_TINT`: Tints by multiplying a colour (albedo/COLOR/modulate multiply).
- `PBR_FLAG`: The plan notes that roughness / albedo / PBR-material terms belong to 3D (spatial) shaders and are unavailable or must be mapped to different 2D equivalents.

## 4. Frequencies (count of 10 plans, coder 1) and bands
Band: L = likely (≥7), P = plausible (2–6), U = unlikely (≤1). n = 10, so ±1–2 plans of sampling noise; treat 2/10 and 7/10 as edge cases.

### F1 — Movement and collision

| Feature | F1A | F1B | F1C | F1D |
|---|---|---|---|---|
| `MASK_PLAYER` | 10 (L) | 10 (L) | 10 (L) | 10 (L) |
| `LAYER_PLAYER` | 0 (U) | 10 (L) | 0 (U) | 0 (U) |
| `PLATFORM_LAYER` | 10 (L) | 10 (L) | 10 (L) | 1 (U) |
| `PHYSICS_PROCESS` | 10 (L) | 10 (L) | 0 (U) | 10 (L) |
| `PROCESS_MOVEMENT` | 0 (U) | 0 (U) | 10 (L) | 0 (U) |
| `PUSHBACK` | 0 (U) | 6 (P) | 9 (L) | 0 (U) |

### F2 — Jump feel

| Feature | F2A | F2B | F2C | F2D |
|---|---|---|---|---|
| `COYOTE` | 10 (L) | 0 (U) | 10 (L) | 10 (L) |
| `BUFFER` | 10 (L) | 10 (L) | 0 (U) | 10 (L) |
| `VARJUMP` | 0 (U) | 0 (U) | 10 (L) | 0 (U) |
| `DOUBLEJUMP` | 0 (U) | 10 (L) | 0 (U) | 0 (U) |
| `VALUE_FLAG` | 0 (U) | 0 (U) | 0 (U) | 10 (L) |
| `TUNING_STEP` | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

### F3 — Camera

| Feature | F3A | F3B | F3C | F3D |
|---|---|---|---|---|
| `CAMERA2D` | 10 (L) | 10 (L) | 10 (L) | 10 (L) |
| `DEADZONE` | 10 (L) | 2 (P) | 2 (P) | 10 (L) |
| `LOOKAHEAD` | 0 (U) | 10 (L) | 2 (P) | 0 (U) |
| `SHAKE` | 0 (U) | 0 (U) | 10 (L) | 0 (U) |
| `SMOOTHING` | 10 (L) | 10 (L) | 10 (L) | 9 (L) |
| `LIMITS` | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

### F4 — Animation

| Feature | F4A | F4B | F4C | F4D |
|---|---|---|---|---|
| `ANIMTREE` | 10 (L) | 10 (L) | 0 (U) | 10 (L) |
| `STATE_MACHINE` | 10 (L) | 2 (P) | 0 (U) | 10 (L) |
| `BLEND` | 0 (U) | 10 (L) | 0 (U) | 0 (U) |
| `KEYFRAMES` | 8 (L) | 6 (P) | 10 (L) | 7 (L) |
| `EASING` | 3 (P) | 7 (L) | 3 (P) | 10 (L) |
| `SCRIPT_DRIVEN` | 10 (L) | 10 (L) | 10 (L) | 10 (L) |

### F5 — Shader and material

| Feature | F5A | F5B | F5C | F5D |
|---|---|---|---|---|
| `CANVAS_ITEM` | 4 (P) | 10 (L) | 10 (L) | 10 (L) |
| `NORMAL_MAP` | 10 (L) | 10 (L) | 0 (U) | 0 (U) |
| `LIGHT2D` | 10 (L) | 10 (L) | 0 (U) | 0 (U) |
| `UV_SCROLL` | 0 (U) | 0 (U) | 10 (L) | 0 (U) |
| `ALBEDO_TINT` | 0 (U) | 0 (U) | 0 (U) | 10 (L) |
| `PBR_FLAG` | 0 (U) | 10 (L) | 0 (U) | 10 (L) |

## 5. Coder agreement
- **Coder 1** coded all 200 plans (5 coder-1 sub-agents, one per family, plans in shuffled order with hashed ids). **Coder 2** (5 separate fresh sub-agents, same model parameter, same written definitions) independently recoded a random **40 plans (20 %)**, 8 per family.
- **Item-level agreement: 235/240 = 97.9%; Cohen's κ = 0.96** (pooled over all features; features are mostly 0/1-imbalanced so κ is the more honest number). Plans where all 6 features agree: 36/40.
- Disagreements (5):

  - F1C plan 8, `PHYSICS_PROCESS`: coder1=0, coder2=1
  - F1D plan 8, `PUSHBACK`: coder1=0, coder2=1
  - F1C plan 9, `PHYSICS_PROCESS`: coder1=0, coder2=1
  - F3C plan 4, `DEADZONE`: coder1=0, coder2=1
  - F3C plan 4, `LOOKAHEAD`: coder1=0, coder2=1
- **Caveats:** both coders are the same model family as the plan generator (not human coders); no human has coded any plan yet. Agreement is high partly because the features are explicit and the plans are short. Coder 1 (family F1) reported it wrote its JSON with a small Python formatting script instead of the Write tool, a protocol deviation that does not change the codes. A crude keyword check (does the term appear at all?) agrees with coder 1 on only 78.5 % of cells; the gap is plans that *mention* a term in order to forbid it (e.g. “so coyote time never grants a double jump”) or discuss it conditionally, which is what the coding rule counts as 0. I spot-read ten of those mismatches and the coder was consistent with the rule.
- **Variance note:** in 9 of the 20 prompts all ten plans have the *same* 6-feature profile, and in 19 of 20 at least 6 of 10 share one profile. At this prompt length and brevity, plan content is close to deterministic, so very few features land in the PLAUSIBLE band. A full version needs longer, more ambiguous prompts (see README).

## 6. Raw plans
`runs/<family><variant>.json` (20 files): `prompt`, `edit_from_base`, `config`, and 10 `plans` each `{n, text}`. Per-plan feature codes are in `codings.json` (coder 1 and coder 2, keyed by hashed plan id) with the id→(family, variant, n) map `plan-ids.json`.
