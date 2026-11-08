# predict-the-prompt — CSYE 7270 pilot (Godot 2D platformer)

Pilot draft of a "predict the prompt" exam for CSYE 7270 Building Virtual Environments. The answer key comes from **sampling the model** (10 plans per prompt), not opinion. Not committed, not pushed. Existing files in the parent folder were not touched.

## Read in this order
1. `EXAM-DRAFT.md` — the exam: 7 items (matching, prompt→plan MC, plausibility, feature forecasting, attribution, predict-and-explain, minimal-edit repair), each with key, frequencies and backing plans.
2. `KEY-AND-RUNS.md` — configuration, the 30 features, frequency tables for all 20 prompts, coder agreement.
3. `runs/*.json` — all 200 raw plans (`F1A.json` … `F5D.json`), prompt and one-phrase edit included.
4. `codings.json`, `plan-ids.json` — per-plan feature codes (coder 1 for all 200; coder 2 for 40) and the id map.

## What was built
- 5 families (movement/collision, jump feel, camera, animation, shader/material) × 4 prompts (base + 3 one-phrase edits) × 10 plans = **200 plans**, each from a fresh sub-agent (`model: sonnet`; resolved id not reported by the harness). A "plan" is a sub-agent's ≤8-step numbered plan with no code; **it is not Claude Code plan mode** and the agents saw no project files.
- 6 binary features per family, mostly semantic (layer vs mask, `_physics_process` vs `_process`, coyote time, jump buffer, variable jump, double jump, state machine vs blend tree, keyframes, easing, deadzone/look-ahead/shake, normal map, UV, albedo, PBR-vs-2D). Behavioral/habit features are labelled `[BEHAVIORAL]` and half-weighted.
- Coder 1 (blind to prompt) coded all 200; coder 2 recoded a random 40 (20 %): **235/240 = 97.9 % agreement, κ = 0.96** (5 disagreements, listed in KEY-AND-RUNS §5).
- 7 exam items drafted from 3 families' worth of the data (F1 collision ×4, F2 jump ×1, F4 animation ×2). F5 and F3 are keyed but have no drafted item.

## What was cut (premise check)
- **Camera: "drag margins" prompt = "deadzone" prompt** (identical feature profile). Camera has 3 distinguishable prompts, so no camera matching item.
- Non-discriminating features (≈10/10 or 0/10 in every prompt): player `MASK_PLAYER` (the model silently corrects a layer/mask swap), `TUNING_STEP`, `CAMERA2D`/`SMOOTHING`/`LIMITS`, `SCRIPT_DRIVEN`.
- Edge features (2/10) left unkeyed. Full list in EXAM-DRAFT.md ("Cuts").

## Honest limits
- **Almost deterministic output.** 9 of 20 prompts gave an identical feature profile in all 10 plans. With one-sentence prompts the banded key is mostly 10/10 or 0/10; PLAUSIBLE items are rare (only a handful: F4A easing 3/10, F5A canvas_item 4/10, F1B pushback 6/10).
- n = 10 per prompt: 2/10 and 7/10 are band-edge cases. Coder 2 contested F1C `PHYSICS_PROCESS` (0 vs 2 of 10), which is why Item 6 does not key on that count.
- Plans were written without repo access, so they hedge ("open the scene and check…") unlike real plan mode. Do not claim these match Claude Code plan-mode behavior.
- Sampling settings are not exposed by the sub-agent interface; model version unrecorded.
- Coders are the same model family as the generator; no human has coded or reviewed the keys. Coder 1 for F1 used a Python formatting script rather than Write (disclosed; codes unaffected).
- Run cost: **210 sub-agent runs ≈ 14.7M tokens** (≈69k per plan run, mostly fixed agent overhead). Mostly agent overhead, not plan content; a leaner runner should cut it a lot (not measured).

## What a full version needs
1. **Longer, more ambiguous prompts** (or a repo-aware agent) so plans vary and the PLAUSIBLE band gets populated; 20+ plans per prompt so band edges are stable.
2. **Real Claude Code plan mode** on a small checked-in Godot project, so the exam can honestly say "plan mode".
3. Direct API sampling with recorded model id, temperature, seed policy, for cheap reruns and for the repair item's grading protocol.
4. Human coding of at least a 20 % subsample; recode keys when the model version changes (keys expire).
5. A second and third item per family and a CSYE-wide pool; F3 camera needs one more distinct prompt (e.g. "screen shake" vs "camera limits").
6. Verify the repair item by actually running student edits (protocol in Item 7).
