# Chapter 12: Audio and triggers

## MA-ch12.1

In Godot, a game plays background music, a menu click, and the footsteps of an enemy walking around a 3D world. The developer must decide, for each sound, whether to use a plain AudioStreamPlayer or a positional AudioStreamPlayer3D. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A plain AudioStreamPlayer plays its stream non-positionally, so how loud it is does not depend on where the camera or any other object is.
- [ ] B. For a positional player, the listener is the point whose position and orientation define what is heard; in Godot 3D it defaults to the active camera unless an explicit listener node is made current.
- [ ] C. The listener is the object that emits a positional sound, so a scene needs one listener per positional sound it plays, each placed at the sound's source.
- [ ] D. The menu click is best played from an AudioStreamPlayer3D so that it is panned and attenuated consistently with the rest of the 3D world, keeping all of the game's sounds behaving the same way.
- [ ] E. Attenuation is the drop in loudness as the distance between a positional source and the listener grows, so footsteps far from the camera are quieter than near ones.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The non-positional player ignores listener position entirely, which is why it suits music and interface sounds.
- B: A positional sound is heard relative to a listener; Godot uses the current camera unless a listener node overrides it.
- C: The listener is the receiver (the ears), and there is one active at a time, not one per sound source.
- D: A menu click has no place in the world; a positional player would make it quieter or pan it depending on where the camera happens to be.
- E: Attenuation (falloff) is exactly the distance-dependent loss of level that makes far sources quieter.

**Source:** Positional audio, listener and attenuation

## MA-ch12.2

A developer tells a coding agent: "Play a click when the button is pressed." The project is a Godot game with one scene, one Button, and the default audio setup. Check each statement that is true about what must hold for the click to actually reach the speakers. Each statement is worth 1 point (5 points total).

- [ ] A. Something must call play() on a stream player that has an audio stream assigned, in response to the button's pressed signal.
- [ ] B. Hearing the click does not prove it was routed through the bus the developer intended, because a mistake in the routing can still leave the sound audible, only on a different bus.
- [ ] C. If the player's bus, or any bus it is routed through on the way to Master, is muted, the click is silent even though the player reports that it is playing.
- [ ] D. The instruction already fixes the bus, the loudness and what happens when the button is pressed twice quickly, so a precise agent needs no further detail.
- [ ] E. Once the player's playing flag reads true after play(), an automated test has proved that the click reached the output and is audible to the user.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: A sound is started by game logic: an event (the signal) is wired to a handler that calls play on a player holding a stream.
- B: A sound can be audible while sent somewhere other than intended (for example, a misnamed bus can silently fall back to the default one), so audibility alone does not verify the wiring.
- C: Level and mute are applied along the bus chain, so a muted bus anywhere on the route removes the sound regardless of the player's state.
- D: The instruction names only an event and a sound; bus, level and overlap behavior are all left for the agent to guess.
- E: The playing flag shows only that a voice was started; it says nothing about bus routing, level, mute, or whether a person can hear it.

**Source:** Wiring a game event to a sound

## MA-ch12.3

A click sample has a peak amplitude of 0.8, where 1.0 is digital full scale (0 dBFS). In an engine, its stream player is set to -6 dB and routed to an SFX bus whose fader is at -6 dB; the SFX bus sends to a Master bus at 0 dB. Gains in decibels add along the chain, and an amplitude factor equals 10^(dB/20), so -6 dB is a factor of about 0.50 and -12 dB about 0.25. No effects are present. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The two -6 dB settings combine to -12 dB, an amplitude factor of about 0.25.
- [ ] B. The click's peak at Master is about 0.20, which is 0.8 multiplied by 0.25.
- [ ] C. The click's peak at Master is about -6 dBFS, the level of the second stage.
- [ ] D. Raising only the SFX bus fader to 0 dB would restore the sample's original peak of 0.8.
- [ ] E. A further -6 dB on any one stage would roughly halve the peak again, to about 0.10.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Decibels are logarithmic, so gains in series add (-6 + -6 = -12 dB), and 10^(-12/20) is about 0.25.
- B: 0.8 x 0.2512 is about 0.201 at the Master bus.
- C: 20 log10(0.201) is about -13.9 dBFS; -6 dBFS would correspond to a peak near 0.50.
- D: The player stage still contributes -6 dB, so the peak would be about 0.40, not 0.8.
- E: Each further -6 dB multiplies amplitude by about 0.5, so 0.20 becomes about 0.10.

**Source:** dB scale and gain staging

## MA-ch12.4

A game has Music, SFX and Voice buses that each send to Master, and a settings menu with one volume slider per bus. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Separate buses for music and effects let the player lower the music without changing how loud the effects are, since each bus has its own level.
- [ ] B. Muting the SFX bus also silences everything on the Music bus, because both ultimately feed the same Master bus.
- [ ] C. Muting Master silences only sounds that are played directly on Master; sounds on the Music and SFX buses still come through.
- [ ] D. A reverb effect placed on the SFX bus processes each sound routed to that bus and does not touch sounds routed only to the Music bus.
- [ ] E. A settings slider that runs from 0.0 to 1.0 can be passed straight to a bus as a decibel value and will behave like a linear volume knob, since 1.0 means full volume and 0.0 means silence.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Each bus is an independent control point, which is the main reason to split a mix into groups.
- B: Buses that feed a common parent do not affect each other; muting SFX removes only what is routed through SFX.
- C: Master is the end of the chain, so muting it silences everything routed to it, directly or through child buses.
- D: Effects belong to a bus and apply to everything that passes through that bus.
- E: Decibels are logarithmic, so a linear slider value should be converted to dB; passing 0 to 1 as dB would span only 1 dB near full level.

**Source:** Audio bus, master bus and effects

## MA-ch12.5

A designer says: "When a character speaks, the music should get quieter, then come back up when the speech ends." The developer passes this to a coding agent as "pause the music during dialogue". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Ducking is the automatic, temporary lowering of one group of sounds while another is active.
- [ ] B. Pausing the music satisfies the designer's request, because a paused track and a ducked track sound the same to the player.
- [ ] C. Ducking can be driven by a side-chain, where an effect on the music bus reacts to the level of the voice signal.
- [ ] D. Ducking requires the music and the voice to be played by the same stream player node, so that one can lower the other.
- [ ] E. Calling stop() on the music and later play() again resumes the track from the position where it stopped.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Ducking is a temporary, automatic level reduction that restores itself, which is what the designer described.
- B: A paused track is silent and frozen; a ducked track keeps playing quietly and continues in time.
- C: Side-chain compression is the usual way to make one bus's level depend on another's.
- D: Music and voice normally sit on different buses and players; ducking works across them.
- E: Stopping discards the playback position, so a later play() starts from the beginning unless a start position is given.

**Source:** Ducking

## MA-ch12.6

A designer wants a chime to play when the player walks into a glowing zone, while the player keeps walking through the zone without being blocked. A developer asks a coding agent for "a zone collider that plays a chime". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The zone must be a trigger (an Area in Godot, a trigger collider in Unity, an overlap volume in Unreal), which reports overlap as an event and does not block.
- [ ] B. A solid collider is the right choice, because it reports contact events and also lets the player pass through while the chime plays.
- [ ] C. The chime should be started from the zone's enter event, which fires when the overlap begins, rather than from code that checks for overlap on each frame.
- [ ] D. The zone should be limited, by collision layers or filtering, to the objects that are meant to trigger the chime, so that enemies or projectiles passing through do not play it.
- [ ] E. Once a chime player is placed inside the zone, the audio system detects the player's overlap itself and plays the chime with no further code.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A trigger observes overlap and raises an event; it does not push back on the objects that enter it.
- B: A solid collider blocks the player; passing through is the defining behavior of a trigger.
- C: The enter event fires once per entry, which is the moment the chime should start.
- D: A zone reports every object that overlaps it unless its detection is filtered, so layers or masks decide which objects count and an unfiltered zone plays the chime for things the designer did not mean.
- E: Audio never decides when to play; game logic detects the overlap and calls the player.

**Source:** Trigger versus collider for events that start sounds

## MA-ch12.7

A pressure plate should play a click when the player steps on it. The agent wired the click to a trigger callback that runs on every physics step while an overlap persists (the kind of event Unity calls OnTriggerStay). Physics runs at 50 steps per second. Players report a buzzing, machine-gun click whenever they stand on the plate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A per-step overlap callback fires about 50 times a second while the player stands on the plate, restarting the click at 20 ms intervals.
- [ ] B. Starting the click from the enter event instead plays it once, when the overlap begins; an exit event marks when the player leaves.
- [ ] C. Raising the player's polyphony so the restarted clicks overlap instead of cutting each other off fixes the cause of the buzzing.
- [ ] D. Making the click file longer fixes the problem, because a longer sound keeps playing and is not restarted so often by the trigger callback.
- [ ] E. A trigger can only report that an overlap is ongoing; it has no event that marks the moment the overlap starts or ends.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: 50 steps per second means one callback every 20 ms for as long as the overlap lasts, each restarting the sound.
- B: Enter and exit events mark the transitions, so a one-time sound belongs on enter.
- C: More voices would let all 50 per second overlap, which treats the symptom and makes it louder and noisier.
- D: The trigger still fires every step; a longer file is simply restarted just as often.
- E: Triggers report entering, staying and exiting; the enter event marks the start of the overlap.

**Source:** Trigger events versus continuous overlap

## MA-ch12.8

A developer asks a coding agent: "Make the engine hum loop while the car drives, and make the horn honk once per button press." The project is Godot. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Godot, whether a sound loops is a property of the audio stream resource, not of the player node that plays it.
- [ ] B. A hum recorded with a fade-out at its end makes a good loop, because the fade hides the join between the end and the start.
- [ ] C. "One-shot" describes a sound that may be triggered only once in an entire play session, after which its player is disabled.
- [ ] D. Looping the hum by calling play() again from the finished handler is seamless, so it is better than the stream's own loop setting.
- [ ] E. Creating a new player node for each honk needs no clean-up, because a node that has finished its job leaves the scene on its own.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Godot's loop settings live on the stream (for example the WAV loop mode), while the player node only plays what it is given.
- B: A fade-out dips the volume once per pass, so the hum would pulse audibly; a clean loop ends at the same level and phase at which it begins.
- C: One-shot means the sound plays through once per trigger and then stops; it can be triggered again later.
- D: Restarting after finished goes through the mixer's block timing and can leave an audible gap that a built-in loop does not.
- E: A node stays in the scene after its sound ends; removing it, or reusing it from a pool, is the job of the developer's code.

**Source:** One-shot versus looping

## MA-ch12.9

In an engine whose stream player cuts off its oldest voice when play() is called beyond its maximum polyphony, a 60 ms click is triggered at t = 0 ms, t = 40 ms and t = 80 ms on the same player. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With a maximum polyphony of 1, the first click is cut off at 40 ms, after only 40 of its 60 ms.
- [ ] B. With a maximum polyphony of 1, all three clicks play their full 60 ms because each trigger starts a new voice.
- [ ] C. With a maximum polyphony of 2, none of the three clicks is cut off.
- [ ] D. With a maximum polyphony of 2, there is an instant at which three voices are sounding at once.
- [ ] E. With a maximum polyphony of 4, the click triggered at 80 ms ends at 120 ms.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The second trigger at 40 ms exceeds the single voice and cuts off the first, which would have run until 60 ms.
- B: With one voice, each new play() replaces the running click, so the first two are truncated.
- C: The clicks occupy 0-60, 40-100 and 80-140 ms, and never more than two overlap, so two voices suffice.
- D: At any instant at most two of the three intervals overlap, so three voices are never needed.
- E: The third click starts at 80 ms and lasts 60 ms, so it ends at 140 ms.

**Source:** Polyphony

## MA-ch12.10

A rhythm game must judge whether a tap landed within 50 ms of a beat in the music. The first version advances a song-time variable by delta (the duration of the last frame) every frame. A second version asks the audio system for the music player's playback position. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Frame delta varies with rendering load, so song time summed from it can drift away from the audio actually playing.
- [ ] B. Audio is mixed in blocks on its own clock, so its reported position is coarse and may need correcting for output latency.
- [ ] C. The audio playback position is exact to the sample when read and already includes device delay, so no latency compensation is needed.
- [ ] D. Judging taps against the audio clock, corrected for latency, tracks what the player actually hears better than accumulated delta does.
- [ ] E. Calling play() on a hit sound in the same frame as the tap guarantees the sound is heard exactly on the beat.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The game loop and the audio hardware run on different clocks, so summed frame times slowly disagree with the music.
- B: Mixing happens in chunks and the output device adds delay, so the raw position is an approximation of what is heard.
- C: The position updates per mixed block and ignores device latency, so it is not exact to the sample when read.
- D: The audio clock is the one the music follows, which is why it is the reference for timing judgments.
- E: Playback begins at the next mix boundary and then passes through output latency, so the start is slightly late.

**Source:** Audio time versus frame time

## MA-ch12.11

A positional audio source follows an inverse-distance law: amplitude is proportional to 1/distance, with 0 dB at 1 m from the listener. A decibel level is 20 log10 of the amplitude ratio. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. At 2 m from the listener the level is about -6 dB, since the amplitude is halved.
- [ ] B. Moving the source from 4 m to 8 m lowers the level by about 6 dB, because each doubling halves the amplitude.
- [ ] C. At 10 m the amplitude is one tenth of its value at 1 m, which works out to -20 dB.
- [ ] D. At 16 m the level is about -24 dB, which is four doublings of distance away from 1 m.
- [ ] E. Under this law the sound reaches exactly zero at some finite distance, so no maximum distance is needed.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Amplitude 0.5 corresponds to 20 log10(0.5), about -6.02 dB.
- B: Each doubling of distance halves the amplitude, which is always about -6 dB.
- C: Amplitude 0.1 gives 20 log10(0.1) = -20 dB.
- D: 16 m is four doublings from 1 m, and four times -6.02 dB is about -24.1 dB.
- E: An inverse law gets smaller forever but never reaches zero, which is why engines add a maximum distance beyond which the sound is cut off.

**Source:** Attenuation and falloff

## MA-ch12.12

A game plays an explosion when an enemy dies. The agent attached a stream player as a child of the enemy node. In the enemy's code it calls play() on that player and immediately frees the enemy node. Players hear nothing, or a clipped pop. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Freeing a node also frees its children, including the stream player, which ends its sound.
- [ ] B. Playing the explosion from a node that outlives the enemy, such as a scene-level audio manager or a self-freeing short-lived player, avoids the cut-off.
- [ ] C. Raising the player's volume fixes the problem, because the sound is only too quiet to notice and the node still exists to play it.
- [ ] D. Having the enemy emit a "died" signal once, and letting an audio handler respond to that signal, separates the enemy's lifetime from the sound's lifetime.
- [ ] E. Checking "health <= 0" every frame and playing the explosion whenever it is true is equivalent to a death signal, since both start the sound when the enemy dies.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Children live and die with their parent, so the sound disappears when the enemy is freed.
- B: The player must belong to something that survives the enemy for as long as the sound lasts.
- C: The sound is not quiet, it is being destroyed; more volume does not bring it back.
- D: An event fires once and decouples who reacts from who died, which is the standard way to wire a game event to a sound.
- E: Polling is true on every frame the condition holds, so the explosion would be restarted repeatedly rather than started once.

**Source:** Wiring a game event to a sound

## MA-ch12.13

Audio designers want to change the footstep sounds without asking programmers to edit code. Gameplay code asks for a cue named "footstep_stone" and the audio data decides which recordings play. Check each statement that is true about cues. Each statement is worth 1 point (5 points total).

- [ ] A. A cue is a named request for a sound event; which recordings it maps to can change without changing gameplay code.
- [ ] B. A cue can pick among several recordings and vary pitch or volume slightly, which reduces the repetitive feel of footsteps.
- [ ] C. A cue is a bus that other sounds are routed through, letting the designers set the level and effects of the footstep recordings together.
- [ ] D. Unreal's Sound Cue asset is an example: a node graph that combines and modifies sounds, played by reference rather than by hard-coding a file.
- [ ] E. The same gameplay event can request different cues in different situations, such as stone or grass, so the cue name carries the situation.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A cue separates "what happened" from "which files play", so designers can retune sound without code changes.
- B: Variation inside a cue is a standard way to avoid listener fatigue from repeated identical samples.
- C: A bus is a mixing and routing channel; a cue is a named sound event that plays on some bus.
- D: Epic describes a Sound Cue as a node graph that encapsulates sound design tasks, which fits the cue idea.
- E: Choosing the cue name from game state, such as the surface under the foot, is how one event produces varied sounds.

**Source:** Cue

## MA-ch12.14

In Godot, a pause menu sets the scene tree to paused. A developer asks a coding agent: "The menu's click should still sound while paused, the music should resume where it left off when unpaused, and pressing restart should reload the level." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A stream player in the default process mode pauses its stream when the tree pauses and resumes when it unpauses.
- [ ] B. A menu-click player will play normally while the tree is paused without any change to its process mode, as it is a short sound.
- [ ] C. After the level scene is reloaded, music players that lived in the old scene keep playing from their previous position.
- [ ] D. A sound that must survive a scene reload is best attached to the scene being reloaded, so it is reloaded with everything else.
- [ ] E. Calling stop() on the music when pausing and play() when unpausing resumes it from where it stopped, as the stream remembers its position.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Godot's audio nodes pause their streams with the tree and resume them automatically afterwards.
- B: A player that follows the paused tree is paused too; a pause-menu sound needs a player whose process mode keeps it running.
- C: Reloading a scene frees the old players and creates new ones, so music restarts unless it lives outside the reloaded scene.
- D: Anything attached to the reloaded scene is destroyed with it; surviving a reload requires living outside it, for example in an autoload.
- E: Stop discards the position, so play() starts from the beginning; pausing the stream is what preserves it.

**Source:** Pause, restart and the lifecycle of a player

## MA-ch12.15

A cave region should add reverb to sound effects while the player is inside. The agent enables a reverb effect on the SFX bus from the cave trigger's enter event and disables it from the exit event. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Enter and exit events must be paired; if an exit is missed or the zone is disabled with the player inside, the reverb can stay on.
- [ ] B. Because the reverb sits on the SFX bus, it also colors the music, which is played on the separate Music bus.
- [ ] C. The bus effect applies to all sounds routed through the SFX bus while it is enabled, including effects triggered far outside the cave.
- [ ] D. The cave trigger must block the player's movement, or its exit event will not fire when the player leaves.
- [ ] E. Reverb on a bus is the same thing as positional attenuation, since both change a sound's character depending on where the player is.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A toggle driven by two events is only correct if both arrive, so robust code re-derives the state from where the player is.
- B: Only sounds routed through the SFX bus are processed; the Music bus is untouched.
- C: A bus effect is not positional, so it colors all SFX, wherever they originate.
- D: A trigger detects overlap without blocking, and still reports both entering and leaving.
- E: Reverb adds reflections to a bus; attenuation lowers a source's level with distance from the listener; they are different mechanisms.

**Source:** Trigger zones, bus effects and event pairs

## MA-ch12.16

A developer moves between engines and must give a coding agent the right term for each audio idea. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unity, an AudioClip is the imported sound and an AudioSource is the component that plays it.
- [ ] B. Unity's AudioListener acts like a microphone, and a scene should have only one.
- [ ] C. Unity's Audio Mixer groups play the role that buses play in Godot: routing, per-group level and effects.
- [ ] D. In Unreal, Play Sound 2D applies distance attenuation from the player's location, so it is meant for sounds that belong in the world.
- [ ] E. In Unreal, Play Sound at Location is fire-and-forget at a point and does not follow an actor, so a sound that must follow a moving enemy needs an attached audio component instead.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Unity separates the sound asset (AudioClip) from the component that plays it (AudioSource).
- B: The listener is the receiver, and Unity documents that a scene works properly with just one.
- C: Mixer groups accept inputs, apply effects and levels, and send a single output, matching a bus.
- D: Play Sound 2D plays without attenuation and is intended for interface sounds.
- E: Play Sound at Location does not travel with any actor; Spawn Sound Attached creates a component that does.

**Source:** Engine vocabulary mapping for audio
