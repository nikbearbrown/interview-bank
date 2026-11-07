# Chapter 12: Audio and triggers

## ES-ch12.1

A developer gives a coding agent this instruction for a Godot game: "Add a click sound when the button is pressed." Rewrite it as a precise instruction using the correct audio terms, and explain what the agent could build wrongly or leave out because of the original wording. Your answer should say what must be true for the click to actually reach the mix, not only that it plays, and how you would check it, saying what automated checks can show and what only a listener can confirm.

**Points:** 5

**Rubric (1 point each):**

1. Names the trigger precisely: the button's pressed signal is connected to a handler that calls play() on a stream player, so game logic, not the audio system, decides when the click starts.
2. Specifies the sound and its type: a short one-shot (non-looping) stream, played by a non-positional player because an interface sound has no place in the world.
3. Specifies the bus, such as an SFX bus that sends to Master, and notes that a muted or lowered bus along the route silences the click.
4. Specifies behavior the original leaves open: loudness in dB relative to the music, and what happens on rapid presses (restart the click or overlap, which is a polyphony choice).
5. Separates what automated checks can show (the handler fires, routing, level on the bus, muting) from what only a person with speakers can confirm (audible, balanced, not annoying).

**Source:** Wiring a game event to a sound

## ES-ch12.2

A designer wants two things: (a) a coin that chimes and disappears when the player touches it, while the player passes straight through, and (b) a closed door that thuds when the player runs into it and stops the player. A developer asks a coding agent for "a collider that plays a sound" for both. Explain the difference between a trigger and a collider that matters here, say which object each of the two items needs, which event should start each sound, what receives that event, where the chime's player should live given that the coin disappears, and describe one way a continuously reported overlap can produce a bad sound.

**Points:** 5

**Rubric (1 point each):**

1. States that a trigger detects overlap and reports an event without blocking movement, while a solid collider blocks and produces a collision response.
2. The coin is a trigger (an Area in Godot, a trigger collider in Unity, an overlap volume in Unreal), and the chime starts from its enter event.
3. The door is a solid collider, and the thud starts from a collision or contact event, optionally scaled by how hard the player hit it.
4. Notes that game logic (not the audio system) receives the event and calls the audio player, and that the chime's player must outlive the coin (not be its child), or removing the coin cuts the sound off.
5. Explains that a per-step overlap (stay) callback restarts the sound on every physics step while the player stands in the zone, producing a buzzing retrigger, and that starting on the enter event or guarding with a playing check avoids it.

**Source:** Trigger versus collider for events that start sounds

## ES-ch12.3

A game has music, sound effects and character voice, and a settings menu where the player can adjust each. Design the audio bus layout and explain it. Your answer should define a bus, the master bus and a bus effect, say how a menu slider should be turned into a level, and explain ducking and why putting everything on a single bus would be a poor design.

**Points:** 5

**Rubric (1 point each):**

1. Defines a bus as a channel that sounds are routed to, with its own level, mute and effects, whose output is sent to a parent bus, and the master bus as the final bus that receives everything and ends the chain.
2. Proposes separate buses such as Music, SFX and Voice that each send to Master, so each can be balanced, muted and exposed to a slider independently.
3. Explains a bus effect, such as reverb or a low-pass filter, as processing applied to every sound routed through that bus, with an example of where it would be used.
4. Explains ducking as the automatic, temporary lowering of the music while voice plays, usually by a side-chain or mix rule, returning to normal afterwards, which is different from pausing or stopping the music.
5. Explains that decibels are logarithmic, so a linear slider value must be converted to dB (with the bottom of the slider mapping to a muted or very low level), and that with a single bus none of this independent control is possible.

**Source:** Audio bus, master bus, effects and ducking

## ES-ch12.4

A developer tells a coding agent: "Make the robot's footsteps 3D." Explain what positional (spatial) audio requires, using the terms listener, attenuation and audio stream player (the Godot node that plays sound; Unity's AudioSource and Unreal's audio component play the same role). Say what the agent could get wrong, and explain why the menu click and the background music should usually not be positional.

**Points:** 5

**Rubric (1 point each):**

1. Explains that positional audio computes a sound's level and left-right placement from the position of the source relative to a listener.
2. Identifies the listener as the point that stands in for the player's ears, typically the active camera, and notes that one is active at a time per scene or viewport; an agent could leave it on the wrong object so everything is quiet or mis-panned.
3. Explains attenuation (falloff) as the loss of level with distance, optionally with a maximum distance beyond which the source is inaudible.
4. Says the sound source must be attached to the robot so it moves with it (a positional player that follows the node), and that the positional player type is chosen instead of the plain one.
5. Explains that interface sounds and music have no location in the world, so a positional player would make them quieter or panned depending on the camera; they use the non-positional player.

**Source:** Positional audio, listener and attenuation

## ES-ch12.5

Explain why a rhythm game should judge hits against the audio clock rather than accumulate frame time. Your answer should cover the audio mixing block, output latency and what happens when a hit sound is started, and then say what an automated test that runs with no sound device can and cannot establish about the game.

**Points:** 5

**Rubric (1 point each):**

1. Explains that frame time varies with rendering load and runs on a different clock from the audio hardware, so time built from accumulated frame deltas drifts from the music being heard.
2. Explains that audio is mixed in blocks on its own clock, so the reported playback position advances in coarse steps and may be smoothed with another clock between updates.
3. Defines output latency as the delay between a sample being mixed and being heard, and says it should be compensated for or made adjustable, since the judgment should match what the player hears.
4. Says a sound begins at a mixing boundary, not at the instant play() is called, so a hit sound can be slightly late.
5. Says a test with no output device can check logic, routing, triggering and levels on a bus, but cannot prove the sound is audible, pleasant or lined up with the beat as heard, which needs a person with speakers or headphones.

**Source:** Audio time versus frame time

## ES-ch12.6

A developer's automated test for a hit sound asserts that the stream player's playing property is true right after the hit event and prints PASS. A reviewer says the test proves very little. Explain what the test does establish and what it does not, and list at least four additional checks, automated or by a person, that would make the evidence stronger.

**Points:** 5

**Rubric (1 point each):**

1. States what the test shows: the hit event reached the handler and play() was called on that player at that moment, so the trigger path is wired.
2. States that it does not show which bus the sound went to or whether a muted or lowered bus swallows it.
3. States that the test is a single yes/no reading of the player's own flag, with no measurement of level or timing, so a true flag does not show that the sound ever reached the output.
4. Lists additional checks: a negative case (a miss stays silent), muting the bus removes the sound at Master, behavior on pause and on restart, and measuring the signal on the bus rather than reading a flag.
5. States that audibility, balance against the music and sync with the beat can only be judged by a person listening on real hardware.

**Source:** Verifying audio triggering and routing

## ES-ch12.7

A shooter needs three sounds: a rapid gunshot (10 per second, each with an audible tail of 0.5 s), a rain ambience that plays for the whole level, and a car horn that honks while a key is held. For each, decide whether it should be a one-shot or a looping sound and what polyphony it needs. Explain polyphony, what a single-voice player does when triggered rapidly, what the developer should do when every voice is in use, and what the developer should watch for at a loop point.

**Points:** 5

**Rubric (1 point each):**

1. Defines a one-shot as a sound that plays through once per trigger and stops, and a loop as a sound that repeats until stopped.
2. Defines polyphony as the number of voices (simultaneous instances) a player can sound at once, and explains that a single-voice player cuts off the oldest sound when triggered again, so rapid shots would chop each other's tails.
3. Computes or reasons that the gunshots need about 5 overlapping voices (10 shots per second multiplied by a 0.5 s tail) to let every tail finish, and treats the gunshot as a one-shot.
4. Treats the rain as a looping ambience whose loop points must be seamless (no click or audible gap at the seam), and gives a reasonable choice for the horn: a loop that starts on key down and stops on key up, or a one-shot per press, with the reason.
5. Notes that more voices cost mixing work, so a polyphony limit and a rule for which voice to drop (oldest or quietest) are a design decision.

**Source:** One-shot, looping and polyphony
