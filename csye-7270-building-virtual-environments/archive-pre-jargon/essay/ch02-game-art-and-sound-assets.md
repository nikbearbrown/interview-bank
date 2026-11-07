# Chapter 2: Game art and sound assets

## ES-ch02.1

A developer tells a coding agent and an image generator: 'Make me a cool pixel-art enemy with a walk animation for my platformer, plus a jump sound and some background music that I can ship.' Rewrite this as a precise specification using the correct terms, and explain what would likely come back wrong from the original wording.

**Points:** 5

**Rubric (1 point each):**

1. Fixes the on-screen size and viewport (for example 'reads as 32 pixels tall in a 640 x 360 game'), one facing direction and the view (side view), and a limited palette.
2. Specifies the animation layout: frame count, equal cells, the same scale and baseline in every frame, delivered as a sprite sheet PNG with an alpha channel rather than a baked background or a JPEG.
3. Separates the audio: a one-shot jump effect and a looping music track cut on a bar boundary with no fade-out, with the file kind and sample rate stated (lossless for the effect, compressed acceptable for long music).
4. Asks for a provenance record: the tool and version, the prompt and settings, the licence terms, any reference images with their licences, and the edits made.
5. Names concrete failures of the original wording, such as wrong size or perspective, no transparency, blurred or off-grid pixels, uneven frames, a non-looping track, or an asset that cannot legally ship.

**Source:** Say it to the agent: asset request rewrite

## ES-ch02.2

Pixel art looks crisp in an image viewer but smeared when it is enlarged in the running game. Explain the cause using the terms texture filtering (nearest and linear), scale and import settings. Say how you would fix it, what can still look wrong at some window sizes, and how you would check the result.

**Points:** 5

**Rubric (1 point each):**

1. Explains that linear filtering blends neighbouring texels when a texture is enlarged, while nearest filtering takes the single closest texel so hard pixel edges survive.
2. Gives the fix as setting nearest filtering where the engine reads it (on the node or as the project default) and notes the difference in scope, rather than regenerating the art at a higher resolution.
3. Covers import settings: lossless compression for pixel art because lossy or hardware compression shows artifacts on small images, and mipmaps off unless the camera zooms far out.
4. Points out that a non-integer scale with nearest filtering gives uneven pixel widths (for example 2.5 times makes some pixels 2 and others 3 screen pixels wide) and that whole-number scales avoid it.
5. Describes a check in the running game at several window sizes and notes the source must really be on a pixel grid, since a smoothed or JPEG-compressed source cannot be fixed by filtering.

**Source:** Blurry pixel art

## ES-ch02.3

Explain the difference between a sprite sheet, a texture atlas, a tileset and a tilemap: what each contains and what uses it. Then, for two situations (a walking character with eight frames, and a cave level built from forty reusable wall and floor pieces), say which of the four terms you would use in an instruction to a coding agent and what you would specify.

**Points:** 5

**Rubric (1 point each):**

1. Defines a sprite sheet as one image holding animation frames, usually in equal cells of a grid, played in order to animate a sprite.
2. Defines a texture atlas as many separate images, often of different sizes, packed into one texture with a record of each rectangle, used mainly to cut texture switches and draw calls.
3. Defines a tileset as a library of reusable equal-sized tiles and a tilemap as the grid of level cells that each reference a tile from that library.
4. For the walking character, chooses a sprite sheet and specifies frame count, cell size, a shared baseline, alpha, and that playback speed is set in the engine.
5. For the cave, chooses a tileset painted into a tilemap, specifies tile size, tile types and matching edges, and explains that asking only for 'a tilemap' is ambiguous because it could return one fixed picture.

**Source:** Sprite sheet, atlas, tileset, tilemap

## ES-ch02.4

A game needs a short coin-pickup sound, a looping ambient track and a three-minute music piece. For each, choose the kind of file and the playback behaviour you would specify to a coding agent, using the terms sample rate, lossless versus lossy, loop, one-shot, sound effect versus music and polyphony. Explain your choices and one way each could go wrong.

**Points:** 5

**Rubric (1 point each):**

1. Distinguishes the roles: the coin is a short, event-triggered one-shot that may overlap itself, while the ambient track is a long loop and the music piece is long and streamed, either looping or played once as the answer states.
2. Chooses formats with reasons: uncompressed or lossless for short effects, a lossy file for long music to save space, optionally with a lossless master kept for re-export.
3. Explains sample rate as samples per second that limits the highest representable frequency to half the rate and raises file size when higher, and that it does not change loudness.
4. Specifies the ambient loop properly: matching start and end with loop points set so the join is not heard, no baked fade-out, and a listening check across the join; if the answer loops the music piece too, the same applies with a length that falls on a bar boundary, and a piece played once needs no loop point.
5. Handles rapid coin pickups: a single voice cuts off the earlier sound, so allow overlapping voices (polyphony) so quick pickups are all heard.

**Source:** Audio formats and playback

## ES-ch02.5

A student ships a game with an AI-generated sprite that was made by giving the generator a reference picture whose source and licence were never recorded, and an AI-generated music track from a tool whose terms the student never read. Explain what 'provenance' means for a generated asset, why recording it matters, which risks the student has created, and what a good asset log contains.

**Points:** 5

**Rubric (1 point each):**

1. Defines provenance as the documented origin and history of an asset: the tool and version, the prompt and settings, the date, the inputs and references, the edits and where it is used.
2. Gives reasons to record it: the asset can be reproduced or replaced, the person's own contribution (selection and edits) can be shown, and a problem can be traced after the fact.
3. Identifies the reference risk: an unknown-source picture can taint the result, and the uncertainty cannot be cleared unless the source is traced or the asset is replaced.
4. Identifies the terms risk: a tool's terms can restrict use (for example non-commercial limits or attribution duties), and ownership of purely generated output is not automatic and varies by country.
5. Lists a useful log entry: asset ID, tool or model and version, exact prompt and settings, references with their licences, the terms or a link, the edits made, the final file and where it is used.

**Source:** Licence and provenance

## ES-ch02.6

A developer wants a grass texture to cover a large ground surface using a 256 x 256 image. Explain what 'seamless' (tileable) means, how to check an image for it, why a seamless texture can still look wrong over a large area, and what to tell a coding agent so that the engine repeats it correctly.

**Points:** 5

**Rubric (1 point each):**

1. Defines seamless as the opposite edges of the image matching, so copies placed side by side show no visible join, and notes this is a property of the image content that an engine setting cannot create.
2. Describes the check: lay copies side by side (for example 3 x 3) and look along the joins, since a single copy can look fine and still fail.
3. Explains visible repetition: distinctive features recurring at a regular spacing form a pattern even without a seam, and names a mitigation such as blending in variation, a second texture or larger source images.
4. Tells the agent to set the texture to repeat rather than clamp, and says what goes wrong otherwise (edge pixels stretch instead of the image repeating).
5. Tells the agent to state how many times the texture repeats across the surface (the tiling scale), so the 256 x 256 image is neither stretched over the whole ground nor repeated too finely.

**Source:** Seamless and tileable textures

## ES-ch02.7

A game has background music, sound effects, spoken dialogue and interface clicks, and a settings menu with separate volume sliders for music and effects. Design the audio bus layout. Explain what a bus is, where each slider should act, what decibels measure, how you keep the mix from clipping, and what it means to duck the music under dialogue.

**Points:** 5

**Rubric (1 point each):**

1. Defines a bus as a channel that audio is routed through before output, where volume and effects apply to every source routed to it, with a master bus at the end.
2. Proposes separate buses (for example Music, SFX, Dialogue, UI) feeding the master, and has each slider set the volume of its own bus so music and effects can be changed independently.
3. Explains decibels as a logarithmic, relative scale where 0 dB is no change and about 6 dB is a factor of two in amplitude.
4. Explains clipping: simultaneous sounds add, so the sum can pass the digital maximum and distort, and the master level is kept under it with headroom.
5. Defines ducking as automatically lowering the music bus while dialogue plays and restoring it afterwards so that speech stays intelligible.

**Source:** Audio buses, decibels and ducking
