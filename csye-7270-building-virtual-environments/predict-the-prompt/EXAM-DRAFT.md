# CSYE 7270 — Predict the Prompt: pilot exam draft (Godot 2D platformer)

**Status: PILOT DRAFT for Bear to look at. Not for students, not committed, not pushed.**

## Executive summary
- Every item below is keyed from **observed frequencies** over 10 sampled plans per prompt (200 plans, 20 prompts, 5 jargon families), not from opinion. Bands: **LIKELY ≥70 %** (7–10 of 10), **PLAUSIBLE 20–70 %** (2–6 of 10), **UNLIKELY <20 %** (0–1 of 10).
- A "plan" here is a **sub-agent's numbered plan (≤8 steps, no code)** for a fixed Godot 4 2D platformer brief. It is **not Claude Code's plan mode**; it is a stand-in for it. Config, features, coding and agreement are in `KEY-AND-RUNS.md`. With n = 10 a count of 6/10 has a wide interval (≈31–83 %), so only items far from a band edge are keyed.
- Keys are **semantic features** (collision layer vs mask, `_physics_process` vs `_process`, coyote time, jump buffer, state machine vs blend tree, UV, normal map…). Anything that is just a habit of the model is labelled **[BEHAVIORAL]** and weighted 0.5.
- 7 item types are drafted (1 each): matching, prompt→plan MC, plausibility, feature forecasting, attribution, predict-and-explain, minimal-edit repair. Cuts (premise check failed) are listed at the end.

**Fixed project brief shown to every prompt:** a small Godot 4 2D platformer: a Player (CharacterBody2D with Sprite2D, CollisionShape2D, `player.gd`), a TileMapLayer for ground and platforms, two enemy scenes, one level scene `level_01.tscn`.

---

## Item 1 — Matching: 4 prompts → 4 plans (family: movement and collision)

Each plan below came from exactly one of the four prompts. Match them. (One prompt per plan.)

**Prompt A:** “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision mask, with movement done in _physics_process.”

**Prompt B:** “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision layer, with movement done in _physics_process.”

**Prompt C:** “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision mask, with movement done in _process.”

**Prompt D:** “Players fall through the platforms. Fix it by setting the platforms' collision mask to 2 and adding layer 2 to the player's collision mask, with movement done in _physics_process.”

**P1**
```
1. Open level_01.tscn and the TileMapLayer's physics layer settings to confirm the current collision layer and mask on the platforms and ground, and check whether the tileset actually has a physics layer with collision polygons on the platform tiles.
2. Inspect the Player's CollisionShape2D and its current collision layer and mask, and review player.gd to see how movement is currently done (including any use of move_and_slide and gravity).
3. Set the platform tiles' physics layer so the TileMapLayer sits on collision layer 2, leaving the ground's setup consistent with that decision (or noting if ground should stay on its current layer).
4. Add layer 2 to the Player's collision mask while keeping its existing mask bits, so it still collides with whatever it collided with before.
5. Move the movement logic in player.gd from the physics callback into _process as requested, keeping gravity and velocity handling intact. Flag to the developer that CharacterBody2D movement normally belongs in _physics_process, since frame-rate-dependent movement in _process can cause tunneling and jitter, and could itself be a cause of falling through platforms.
6. Check the two enemy scenes for collision layers and masks, and adjust their masks to include layer 2 if they need to stand on the platforms too.
7. Run level_01.tscn and test walking, jumping and landing on every platform, including thin one-way platforms and edges, to confirm the player no longer falls through.
8. Report the changes made, and recommend moving movement back to _physics_process if any tunneling or inconsistent behavior remains at varying frame rates.
```

**P2**
```
1. Open level_01.tscn and the TileMapLayer's physics settings to confirm how the platforms currently collide and which collision layer and mask they use. Check that the tileset actually has a physics layer with collision polygons on the platform tiles, since missing shapes are a common cause of falling through.
2. Set the TileMapLayer's collision layer to layer 2 (and clear it from other layers unless ground still needs layer 1). Decide whether the ground and platforms share the TileMapLayer or need separate ones, and keep the ground's layer assignment consistent with that decision.
3. Open the Player's CharacterBody2D collision settings and add layer 2 to its collision mask, keeping any existing mask bits (such as ground) enabled. Leave the Player's own collision layer unchanged.
4. Review player.gd and confirm all movement, gravity, and the move-and-slide call happen in _physics_process rather than _process. If any movement or velocity logic sits in _process, move it into _physics_process and use the physics delta.
5. Check the two enemy scenes for masks that should also include layer 2, so enemies do not fall through the platforms either. Update them only if they walk on those platforms.
6. Verify the Player's CollisionShape2D is enabled, correctly sized, and positioned, and that no one-way or disabled-shape settings on the platform tiles undermine the fix.
7. Run level_01.tscn and test landing on, walking along, and jumping through platforms at various speeds, including fast falls, to check for tunnelling. Confirm enemies and ground still behave correctly.
8. Summarize the changes made (layer and mask settings, any movement relocation) and flag anything that did not match expectations, such as additional layers or scenes that needed adjusting.
```

**P3**
```
1. Open level_01.tscn and the TileMapLayer's TileSet to confirm which physics layer the platform tiles use and what the current collision layer and mask values are. Also check that the tiles actually have collision polygons defined.
2. Set the platforms' collision mask to 2 on the TileMapLayer's physics settings, as requested. Note that the mask controls what the platforms scan, while the layer controls what the platforms are seen as, so keep that in mind when verifying.
3. Open the Player's CollisionShape2D/CharacterBody2D properties and add layer 2 to the player's collision mask, keeping any existing mask bits (such as the ground layer) enabled.
4. Check that the platforms' collision layer is actually set to a layer the player's mask includes. If the platforms sit on layer 1 only, the new mask of 2 on the player will not detect them, so flag this to the developer rather than silently changing it.
5. Open player.gd and confirm that all movement and move_and_slide calls happen in _physics_process rather than _process. Move any movement or velocity logic there if it is elsewhere.
6. Check the enemy scenes and level_01.tscn for any collision layer or mask settings that the change could affect, and adjust only if there is a conflict.
7. Run level_01.tscn and test walking and jumping onto several platforms, confirming the player no longer falls through. Also confirm the player still collides with the ground and enemies as before.
8. Report back what was changed, any layer/mask mismatch found in step 4, and anything that still needs the developer's decision.
```

**P4**
```
1. Open level_01.tscn and the TileMapLayer's TileSet, and note the current physics layer setup and each layer's collision layer and mask values. Confirm the tiles actually have collision shapes defined on the physics layer.
2. Set the platform TileMapLayer's collision layer to layer 2 (and the ground layer too, if the developer wants it consistent). Keep layer numbering consistent with the project's layer names in Project Settings.
3. Select the Player CharacterBody2D and add layer 2 to its collision layer, keeping its existing layer bit. Check that its collision mask includes layer 2, since the mask decides what it collides with and the layer alone will not stop the fall.
4. Open player.gd and find where gravity, velocity, and move_and_slide are handled. Verify all movement and physics code runs in _physics_process rather than _process.
5. Move any movement or gravity logic found in _process into _physics_process, using the physics delta, and leave input-only or visual logic where it is.
6. Check the Player's CollisionShape2D for a valid shape with a sensible size and position, and that the TileMapLayer's physics is enabled with collision turned on.
7. Review the two enemy scenes for collision layer and mask settings, and update their masks to include layer 2 so they do not fall through the platforms either.
8. Run level_01.tscn and test landing, walking, and jumping on platforms and ground. Confirm the player no longer falls through and that nothing else regressed.
```

**Key:** A→P2, B→P4, C→P1, D→P3.

**Why it is keyable (semantic features):**

- C (`_process`): `PROCESS_MOVEMENT` 10/10 and `PHYSICS_PROCESS` 0/10; the other three prompts give 0/10 and 10/10. Plan P1 is the one that keeps movement in `_process`.
- B (layer given instead of mask): `LAYER_PLAYER` 10/10 (0/10 in A, C, D). Plan P4 is the one that also sets the player's own layer. `PUSHBACK` 6/10 [plausible, not used for keying].
- D (platform *mask* instead of *layer*): `PLATFORM_LAYER` 1/10 vs 10/10 in A, B, C. Plan P3 never puts the platforms on a layer.
- A is the remaining plan: mask + platform layer + `_physics_process`, no player-layer change, no pushback (`PUSHBACK` 0/10).
**Backing plans:** P1 = runs/F1C.json plan 1; P2 = runs/F1A.json plan 1; P3 = runs/F1D.json plan 1; P4 = runs/F1B.json plan 3. Feature profile of all 40 plans: `KEY-AND-RUNS.md` §4.

**Scoring:** 1 point per correct pair (max 4).

---

## Item 2 — Prompt → most likely plan (MC) (family: animation)

**Prompt:** “Animate the player (idle, run, jump, fall) using an AnimationTree with a blend tree.”

Which of these plans is the one this prompt most likely produces? (All four are real plans from sibling prompts of the same family.)

**(a)**
```
1. Review player.gd and the Player scene to see how movement states (on floor, moving horizontally, rising, falling) are currently determined, and check the Sprite2D's spritesheet or frame setup (hframes/vframes or separate textures). This tells me which frames exist for idle, run, jump, and fall.
2. Add an AnimationPlayer node as a child of the Player scene, and set its root node so track paths resolve to the Sprite2D correctly.
3. Create four animations named idle, run, jump, and fall, setting appropriate lengths and loop modes (looping for idle and run, non-looping or holding the last frame for jump and fall).
4. For each animation, add a property track on the Sprite2D's frame (or texture) property and insert keyframes at the right times, using discrete/nearest update mode so frames snap rather than interpolate.
5. Optionally add keyframes for small extras like sprite offset or scale squash/stretch on jump and fall, and set the idle animation as autoplay.
6. Update player.gd to choose which animation to play each physics frame based on velocity and floor state (idle when still on floor, run when moving on floor, jump when moving upward, fall when moving downward), only calling play when the animation changes. Also handle sprite flipping based on horizontal direction.
7. Run level_01.tscn and test each transition (standing, running, jumping, walking off a ledge, landing), adjusting keyframe timing, loop settings, and the animation-selection logic for glitches like flickering or stuck animations.
8. Verify the enemy scenes and TileMapLayer are unaffected and that the Player scene saves cleanly, then save the scene.
```

**(b)**
```
1. Review player.gd and the Player scene to see how movement, jumping, and gravity are currently handled, and note which signals (velocity, is_on_floor) can drive the four animation states.
2. Prepare the sprite art for idle, run, jump, and fall, either as a spritesheet on the Sprite2D (set up frames/hframes) or as separate frames, and confirm the pixel-art import settings so it stays crisp.
3. Add an AnimationPlayer to the Player scene and create one animation per state (idle, run, jump, fall), keying the sprite frame track, setting loop modes, and choosing frame timing.
4. Add an AnimationTree node, point it at the AnimationPlayer, and set its root to an AnimationNodeStateMachine with the four animations as states.
5. Define the transitions between states (idle to run, run to idle, any grounded state to jump, jump to fall, fall to idle or run) with switch modes, conditions or expressions, and an xfade time plus an easing curve on each transition.
6. Update player.gd to activate the tree and feed it each physics frame with the inputs it needs (horizontal speed, vertical velocity, grounded state), and flip the sprite based on facing direction.
7. Playtest in level_01.tscn, checking every transition (landing, walking off ledges, jump at the apex, quick direction changes) and tuning xfade times and easing so blends feel responsive rather than floaty.
8. Clean up by removing any old direct animation-play calls from player.gd and confirming the enemy scenes and other levels are unaffected.
```

**(c)**
```
1. Confirm the Player sprite art: check that idle, run, jump and fall frames exist (as a sprite sheet or separate frames) and note frame counts and frame rates. Decide whether the Sprite2D needs to become an AnimatedSprite2D or stay a Sprite2D driven by an AnimationPlayer.
2. Add an AnimationPlayer to the Player scene and create four animations (idle, run, jump, fall) that key the sprite frame property, with looping on for idle and run and off for jump and fall.
3. Add an AnimationTree node to the Player scene, point it at the AnimationPlayer, and set its root to a new AnimationNodeBlendTree.
4. Build the blend tree: an Animation node for each clip, a BlendSpace1D or Blend2 node that mixes idle and run by horizontal speed, and a second blend node (or a Transition node) that selects between grounded, jump and fall.
5. Add an Output node, wire the graph into it, and set the AnimationTree to active in the inspector.
6. Update player.gd to compute the blend parameters each physics frame: normalized horizontal speed for the run blend, plus is_on_floor and vertical velocity to select jump or fall, and write them to the AnimationTree parameters.
7. Handle sprite flipping by setting the sprite's flip_h from the facing direction in player.gd, and make sure the collision shape stays aligned.
8. Test in level_01.tscn by running through all four states (standing, running, jumping, falling), tune blend and transition times so there are no pops, and check that the enemy scenes are unaffected.
```

**(d)**
```
1. Read player.gd and the Player scene to learn how movement, jumping, and gravity are handled, and what signals or properties (velocity, is_on_floor) can drive the animation states.
2. Check how the Sprite2D is set up (single texture vs. sprite sheet, frame size, hframes/vframes) and confirm the art assets for idle, run, jump, and fall exist or note which are missing.
3. Add an AnimationPlayer to the Player scene and create four animations (idle, run, jump, fall), setting frame tracks on the Sprite2D, loop modes, and speeds appropriate to each.
4. Add an AnimationTree node, point it at the AnimationPlayer, and set its root to an AnimationNodeStateMachine with the four animations as states.
5. Define the transitions between states (idle to run, run to idle, any grounded state to jump, jump to fall, fall to idle or run on landing) with sensible switch modes and conditions or advance expressions.
6. Update player.gd to activate the tree, get its state machine playback, and each physics frame travel to the correct state from velocity and floor contact, also flipping the sprite based on horizontal direction.
7. Test in level_01.tscn by running the level and exercising walking, jumping, falling off ledges, and landing, watching for flicker, wrong states, or stuck transitions, and tune transitions accordingly.
8. Confirm the enemy scenes and the rest of the level are unaffected, and tidy up any unused nodes or debug output.
```

**Key: (c).**

**Frequencies (10 plans per prompt):** blend tree/blend parameter: this prompt 10/10, state-machine prompt 0/10, keyframes prompt 0/10, state-machine+easing prompt 0/10. State machine in this prompt's plans: 2/10 (vs 10/10 and 10/10 for the state-machine prompts). `AnimationTree` node: 10/10; absent (0/10) when the prompt says keyframes on an AnimationPlayer.

**Distractors and what each tests:** (a) from the *keyframes on AnimationPlayer* prompt (no AnimationTree, `ANIMTREE` 0/10); (b) from the *state machine + easing* prompt; (d) from the *state machine* prompt. (b) and (d) are the near misses: a student who confuses state machine with blend tree picks them.

**Backing plans:** (c) runs/F4B.json plan 3; (a) runs/F4C.json plan 1; (b) runs/F4D.json plan 1; (d) runs/F4A.json plan 1.

Blend-tree lines in the prompt's own plans:
- runs/F4B.json plan 1: “3. Add an AnimationTree node to the Player scene, point it at the AnimationPlayer, and set its tree root to a new AnimationNodeBlendTree.”
- runs/F4B.json plan 2: “4. Add an AnimationTree node, assign the AnimationPlayer to it, and set its tree root to an AnimationNodeBlendTree.”
- runs/F4B.json plan 3: “3. Add an AnimationTree node to the Player scene, point it at the AnimationPlayer, and set its root to a new AnimationNodeBlendTree.”

**Scoring:** 1 point.

---

## Item 3 — Plausibility: likely / plausible / unlikely (family: animation)

**Prompt:** “Animate the player (idle, run, jump, fall) using an AnimationTree with a state machine.”

Quoted phrase to reason from: **“AnimationTree with a state machine”**. Out of 10 sampled plans, label each statement LIKELY (≥7), PLAUSIBLE (2–6) or UNLIKELY (≤1).

- S1. The plan uses an `AnimationTree` node.
- S2. The plan builds a blend tree / blend parameter (e.g. blending idle↔run by speed).
- S3. The plan has the author keyframe animation clips (AnimationPlayer tracks) for idle/run/jump/fall.
- S4. The plan mentions easing curves or crossfade times on the transitions.
- S5. [BEHAVIORAL] A script sets the animation each frame from velocity / `is_on_floor()`.

**Key and frequencies:**

| Statement | Observed (of 10) | Key | Weight |
|---|---|---|---|
| S1 | 10/10 | LIKELY | 1 |
| S2 | 0/10 | UNLIKELY | 1 |
| S3 | 8/10 | LIKELY | 1 |
| S4 | 3/10 | PLAUSIBLE | 1 |
| S5 | 10/10 | LIKELY | 0.5 (behavioral) |

**Backing plans (runs/F4A.json):**

- S1:
  - runs/F4A.json plan 1: “4. Add an AnimationTree node, point it at the AnimationPlayer, and set its root to an AnimationNodeStateMachine with the four animations as states.”
  - runs/F4A.json plan 2: “4. Add an AnimationTree node to the Player scene, point it at the AnimationPlayer, and set its root to an AnimationNodeStateMachine.”
- S2:
  (none have it)
- S3:
  - runs/F4A.json plan 1: “3. Add an AnimationPlayer to the Player scene and create four animations (idle, run, jump, fall), setting frame tracks on the Sprite2D, loop modes, and speeds appropriate to each.”
  - runs/F4A.json plan 2: “3. Add an AnimationPlayer to the Player scene and create four animations (idle, run, jump, fall) that key the Sprite2D frame, with looping set on idle and run and not on jump and fall.”
  without it:
  - runs/F4A.json plan 4: “2. Gather or create the sprite frames for idle, run, jump and fall, and decide whether to animate the Sprite2D via frame/region tracks or switch to an AnimatedSprite2D; keep the existing CollisionShape2D unchanged.”
  - runs/F4A.json plan 8: “2. Add an AnimationPlayer to the Player scene and create four animations (idle, run, jump, fall) that drive the Sprite2D's texture/frame properties, with looping set for idle and run and non-looping for jump and fall.”
- S4:
  - runs/F4A.json plan 3: “8. Run level_01.tscn to test each state (standing, running both directions, jumping, falling off a ledge, landing), watch for flicker or stuck states, and tune transition conditions and blend times.”
  - runs/F4A.json plan 4: “6. Configure each transition's switch mode, advance condition or expression, and a short crossfade, so grounded/velocity checks decide changes and Jump-to-Fall triggers at the apex when vertical velocity turns positive.”
  without it:
  - runs/F4A.json plan 1: “(no line matches; see the plan in the run file)”
  - runs/F4A.json plan 2: “(no line matches; see the plan in the run file)”
- S5:
  - runs/F4A.json plan 1: “1. Read player.gd and the Player scene to learn how movement, jumping, and gravity are handled, and what signals or properties (velocity, is_on_floor) can drive the animation states.”
  - runs/F4A.json plan 2: “1. Inspect player.gd and the Player scene to learn how movement, jumping, and gravity are currently handled, and which signals or properties (velocity, is_on_floor) can drive animation state.”

**Scoring:** exact band = full weight; adjacent band (e.g. says LIKELY, key PLAUSIBLE) = half weight; two bands off = 0. S4 is the only PLAUSIBLE statement (3/10 = 30 %): it is the discriminating one. Note S4 sits at 30 %, comfortably inside the band, but a rerun could plausibly give 2–5.

---

## Item 4 — Feature forecasting: fraction of 10 plans (family: movement and collision)

**Prompt:** “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision layer, with movement done in _physics_process.”

Note the prompt sets the player's collision **layer**, not the **mask**. For each feature, forecast how many of 10 plans will do it (integer 0–10).

- F-a. The plan changes the player's own collision LAYER.
- F-b. The plan sets the PLAYER's collision MASK to include the platforms.
- F-c. The plan keeps/moves movement in `_physics_process`.
- F-d. The plan explicitly flags part of the request as wrong, unnecessary or confused.
- F-e. The plan puts movement in `_process`.

**Key and frequencies (runs/F1B.json):**

| | Observed | Band |
|---|---|---|
| F-a `LAYER_PLAYER` | 10/10 | LIKELY |
| F-b `MASK_PLAYER` | 10/10 | LIKELY |
| F-c `PHYSICS_PROCESS` | 10/10 | LIKELY |
| F-d `PUSHBACK` | 6/10 | PLAUSIBLE |
| F-e `PROCESS_MOVEMENT` | 0/10 | UNLIKELY |

**What the key shows:** the model does *not* follow the layer/mask swap literally. It adds the platform layer to the player's **mask** in 10/10 plans, and **also** changes the player's own layer in 10/10, so a student who forecasts “the plan will copy the prompt” (mask 0) or “the plan will correct it silently” (layer 0) is wrong in a different way. 6/10 plans additionally *say so* (F-d), the only PLAUSIBLE feature.

**Backing plans:**
- runs/F1B.json plan 3: “1. Open level_01.tscn and the TileMapLayer's TileSet, and note the current physics layer setup and each layer's collision layer and mask values. Confirm the tiles actually have collision shapes defined on the physics layer.”
- runs/F1B.json plan 5: “1. Open level_01.tscn and the TileMapLayer's TileSet to confirm which physics layer the platform tiles currently use and whether the platform tiles actually have collision polygons painted on them.”
- runs/F1B.json plan 1: “1. Open level_01.tscn and the TileMapLayer node to confirm how the platforms are currently set up and which collision layer and mask they use.”

**Scoring (banded):** per feature, 1 point if the forecast is in the observed band, 0.5 if one band away, else 0. Because F-d is 6/10 and a 10-run rerun could give 4–8, **accept 4–8 as full credit** for F-d. F-b is the only feature a student can only get by knowing how layer/mask actually pair, which is the point of the item.

---

## Item 5 — Attribution: which prompt produced this plan? (family: jump feel)

Prompts (one phrase differs):

- **A** “Make the jump feel forgiving: add 0.1 s of coyote time and a 0.1 s jump buffer.”
- **B** “Make the jump feel forgiving: add a double jump and a 0.1 s jump buffer.”
- **C** “Make the jump feel forgiving: add 0.1 s of coyote time and variable jump height.”
- **D** “Make the jump feel forgiving: add 2 s of coyote time and a 0.1 s jump buffer.”

**Plan:**
```
1. Read player.gd in full to learn how gravity, ground detection, jump input, and velocity are currently handled, and note any existing timers or state flags.
2. Check whether the requested 2 s coyote time is a typo, since typical values are about 0.1 to 0.2 s and 2 s would allow jumping long after leaving a ledge; confirm with the developer or, if unreachable, implement it as an easily changed exported value and flag the concern.
3. Add two tunable exported settings to the Player script (coyote time and jump buffer time) so they can be adjusted in the Inspector without editing logic.
4. Implement coyote time by starting a countdown whenever the player is on the floor and letting it run down once airborne, treating the player as "grounded enough to jump" while it remains above zero; clear it immediately when a jump is performed so it cannot cause a double jump.
5. Implement the jump buffer by starting a 0.1 s countdown when the jump button is pressed, and performing the jump as soon as the player is grounded (or within coyote time) while that countdown is still active, then clearing it.
6. Make sure normal jump behaviors still work: variable jump height on button release, jumping while grounded, and no extra jump when falling after a jump has already been used.
7. Run level_01.tscn and test the cases: jumping just after walking off a ledge, pressing jump just before landing, pressing jump too early or too late, and a repeated tap on the ground, adjusting values as needed.
8. Review the finished change for edge cases such as moving platforms, enemy bounces, and any other code that sets velocity or jump state, then summarize the changes for the developer.
```

**Key: D** (the 2 s coyote prompt).

**Frequencies:** a plan that pushes back on or shrinks the coyote duration (`VALUE_FLAG`): D 10/10; A 0/10, B 0/10, C 0/10. Coyote + buffer together (A and D share this profile): A 10/10, D 10/10; B (double jump) and C (variable height) differ on `DOUBLEJUMP`/`VARJUMP` (10/10 and 10/10, 0 elsewhere). So the *only* thing separating A from D is the duration comment, which is exactly the point: the student has to notice 2 s is not a coyote window.

**Backing plans:** this plan = runs/F2D.json plan 1.
- runs/F2D.json plan 1: “2. Check whether the requested 2 s coyote time is a typo, since typical values are about 0.1 to 0.2 s and 2 s would allow jumping long after leaving a ledge; confirm with the developer or, if unreachable, implement it as an easily changed exported value and fl”
- runs/F2D.json plan 2: “2. Flag that 2 s of coyote time is far longer than the usual 0.1-0.2 s and would feel like floaty air-jumping. Ask the developer to confirm, and make the value an exported variable so it is easy to tune.”

**Scoring:** 1 point for D; 0 otherwise. Wrong answers A (the base prompt) is the near miss.

---

## Item 6 — Predict and explain (family: movement and collision)

**Prompt:** “Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision mask, with movement done in _process.”

**Predict** what the plan will do about `_process` / `_physics_process`, and what it will say about it. **Then explain** in 2–3 sentences, in Godot terms, *why* the plan reacts that way.

**Key (observed over 10 plans, runs/F1C.json):**

- Moves/keeps movement in `_process` as instructed: 10/10 → LIKELY. Rewrites it into `_physics_process` (follows the physics tick instead of the prompt): coder 1 0/10, **but coder 2 coded 2 of the 8 recoded plans (plans 8 and 9) as 1** because they tell the developer to *move it back* to `_physics_process` later, so treat this feature as **UNLIKELY (0–2/10)** and do not key on the exact count.
- Flags the `_process` choice as risky or wrong (`PUSHBACK`): 9/10 → LIKELY. Compare with the correct-tick prompt A: pushback 0/10.
- Platform layer + player mask still set (the collision part of the prompt is followed): 10/10 and 10/10.

**Explanation rubric (3 points):** 1 = `CharacterBody2D`/`move_and_slide` and physics collision are stepped on the fixed physics tick; `_process` runs once per rendered frame with a variable delta. 1 = names the consequence (tunnelling through thin platforms, jitter, framerate-dependent speed). 1 = notes the plan *complies but warns* instead of silently fixing. Explanations that claim `_process` “cannot” move a body, or that confuse the tick with collision *layers*, get 0 on that criterion.

**Backing plans:**
- runs/F1C.json plan 1: “5. Move the movement logic in player.gd from the physics callback into _process as requested, keeping gravity and velocity handling intact. Flag to the developer that CharacterBody2D movement normally belongs in _physics_process, since frame-rate-dependent mov”
- runs/F1C.json plan 2: “5. Open player.gd and move the movement logic from its current callback into _process, as the developer requested. Keep the move-and-slide call and gravity handling together so behavior stays consistent.”
- runs/F1C.json plan 3: “5. Update player.gd so movement runs in _process as requested, keeping the move-and-slide call and gravity handling there. Note that physics bodies are normally moved in _physics_process, so flag to the developer that this may cause jitter or inconsistent coll”

**Scoring:** prediction 2 points (movement stays in `_process` = 1, plan flags it = 1), explanation 3 points, total 5.

---

## Item 7 — Minimal-edit repair, graded by running (family: movement and collision)

**Prompt:**
> Players fall through the platforms. Fix it by putting the platforms on collision layer 2 and adding layer 2 to the player's collision mask, with movement done in _process.

**Problem:** in the sampled plans for this prompt, movement is *not* put on the physics tick (`PHYSICS_PROCESS` 0–2/10, see Item 6) and 9/10 plans push back. **Edit the prompt in ≤12 words (word-level insert/delete/replace count) so that ≥7/10 fresh plans keep the platform-layer and player-mask fix AND put movement in `_physics_process` without pushing back.**

**Reference repair (verified by running):** replace `_process` with `_physics_process` (1 word replaced). That is prompt A of this family: 10 runs gave `PHYSICS_PROCESS` 10/10, `PROCESS_MOVEMENT` 0/10, `PUSHBACK` 0/10, `PLATFORM_LAYER` 10/10, `MASK_PLAYER` 10/10 (runs/F1A.json).

**Run protocol (grader):**
1. Check the edit is ≤12 words from the original (word-level edit distance).
2. Run **10 fresh sub-agent plans** with the same configuration (same model parameter, same job template with only the developer line replaced, one agent per plan, ≤8 numbered steps, no code, no tools except Write).
3. Code each plan with the five features `PLATFORM_LAYER`, `MASK_PLAYER`, `PHYSICS_PROCESS`, `PROCESS_MOVEMENT`, `PUSHBACK` using the definitions in `KEY-AND-RUNS.md` §3 (a second coder recodes 20 %).
4. **Pass** if `PHYSICS_PROCESS` ≥7/10, `PUSHBACK` ≤2/10, and `PLATFORM_LAYER` and `MASK_PLAYER` each ≥7/10. **Partial** (half credit) if `PHYSICS_PROCESS` ≥7/10 but pushback is 3–6/10 or one of the collision features drops to 4–6/10. Else 0.
5. Edits that delete the instruction entirely may pass the first conditions but fail `PLATFORM_LAYER`/`MASK_PLAYER`, which is intended.

**Backing plans (the broken prompt):**
- runs/F1C.json plan 1: “5. Move the movement logic in player.gd from the physics callback into _process as requested, keeping gravity and velocity handling intact. Flag to the developer that CharacterBody2D movement normally belongs in _physics_process, since frame-rate-dependent mov”
- runs/F1C.json plan 2: “5. Open player.gd and move the movement logic from its current callback into _process, as the developer requested. Keep the move-and-slide call and gravity handling together so behavior stays consistent.”

---

## Cuts (premise check: altered prompts gave the same or a saturated feature profile)

- **F3 variant D (“drag margins”) vs A (“deadzone”).** Same profile: DEADZONE 10/10 vs 10/10, LOOKAHEAD 0/0, SHAKE 0/0, SMOOTHING 10/10 vs 9/10. The model treats them as synonyms (Godot's drag margins *are* the deadzone), which is correct. **Cut** every item that tries to tell A from D; the camera family has only 3 distinguishable prompts, so **no camera matching item** (needs 4). Camera is kept only as an explicit synonym control.
- **F1 `MASK_PLAYER` as a discriminating feature.** 10/10 in all four prompts, including the one that never mentions the mask (B) and the one where the platform mask is set instead (D). **Cut** as a discriminator; used only in Item 4 as the surprise (the model silently adds the mask).
- **F1 B “prompt B omits the mask → plans omit it” item.** Premise false: the model corrects the layer/mask swap in 10/10 plans. **Cut.**
- **F2 `TUNING_STEP` [BEHAVIORAL].** 10/10 in all 40 plans (every plan ends with a playtest/tuning step). Saturated habit. **Cut.**
- **F3 `CAMERA2D`, `SMOOTHING`, `LIMITS` [LIMITS behavioral].** ≈10/10 in all four camera prompts (SMOOTHING 9/10 in D). **Cut** as features.
- **F4 `SCRIPT_DRIVEN` [BEHAVIORAL].** 10/10 in all four animation prompts. Used only as a half-weight statement in Item 3.
- **F3 DEADZONE in B/C (2/10) and LOOKAHEAD in C (2/10); F4 STATE_MACHINE in B (2/10).** Sit exactly on the 20 % band edge with n = 10, so a rerun can flip them. **Not keyed.**
- **F5 shader family (items).** Data collected and keyed in `KEY-AND-RUNS.md` but **no F5 item drafted** in this pilot: the four prompts are cleanly separable (A vs B on PBR_FLAG 0/10 vs 10/10 and CANVAS_ITEM 4/10 vs 10/10; B vs D on NORMAL_MAP 10/10 vs 0/10 and ALBEDO_TINT 0/10 vs 10/10; C on UV_SCROLL 10/10 only), so an F5 matching/MC item is ready for the full version.