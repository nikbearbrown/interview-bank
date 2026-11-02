# Chapter 2: Game art and sound assets

## MA-ch02.1

A game developer wants the vocabulary for 2D art straight before instructing a coding agent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A texture is image data applied to a surface or drawn; a sprite uses a texture, but the words are not synonyms.
- [ ] B. A sprite is a 2D image, or one frame of one, drawn as an object in the game scene.
- [ ] C. A 32 x 48 pixel image has a resolution of 32 by 48 pixels, which is 1,536 pixels in all.
- [ ] D. The same 32 x 32 sprite appears larger when the viewport is scaled up, so file pixels and on-screen size differ.
- [ ] E. Resolution is the shape of an image, such as 16:9, while aspect ratio is its total pixel count in millions.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Texture names the image data, sprite names the thing drawn from it.
- B: A sprite is the drawn 2D object; its pixels come from a texture.
- C: 32 x 48 = 1,536.
- D: On-screen size depends on the scale applied at display time, not on the file's pixel dimensions alone.
- E: The two are swapped: resolution is the pixel dimensions, aspect ratio is the width-to-height proportion.

**Source:** Sprite, texture, resolution

## MA-ch02.2

An image generator returns a reference picture of 1,024 x 873 pixels. The game is drawn in a 640 x 360 viewport (a 16:9 shape, ratio about 1.78). The developer wants to place the picture in the game. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Stretching it to exactly 640 x 360 distorts it: its ratio is about 1.17 and the viewport's about 1.78.
- [ ] B. A 40-pixel-tall sprite takes up about a quarter of this viewport's height, so it would dominate the screen.
- [ ] C. Enlarging a low-resolution picture by interpolation adds real detail that was missing from the original.
- [ ] D. Fitting the picture inside 640 x 360 without stretching gives exactly 640 x 360 pixels, because the viewport sets the size.
- [ ] E. Fitting the picture inside 640 x 360 without stretching gives an image about 422 pixels wide and 360 tall.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: 1,024 / 873 is about 1.17 and 640 / 360 is about 1.78, so non-uniform scaling changes the proportions.
- B: 40 / 360 is about 11 percent, closer to one ninth than one quarter.
- C: Interpolation creates more pixels but not more information; the added detail is guessed, not recovered.
- D: Keeping the ratio leaves unused space on one axis; only a stretched copy fills both dimensions exactly.
- E: The scale factor is 360 / 873, about 0.412, so the width becomes 1,024 x 0.412, about 422.

**Source:** Resolution and aspect ratio

## MA-ch02.3

A developer asks an image generator for a character sprite 'on a transparent background' and receives a file named hero.jpg. In the engine the sprite appears inside a white rectangle. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Setting the sprite node's opacity to 50 percent makes the white rectangle transparent while the character stays opaque.
- [ ] B. JPEG has no alpha channel, so a .jpg file cannot hold transparency no matter what the prompt asked.
- [ ] C. A white background painted into the pixels is content, not transparency; remove it and save as PNG or another format with alpha.
- [ ] D. After removing a white background by colour, light fringe pixels can remain around the character's edge.
- [ ] E. A pixel with an alpha of 255 in an 8-bit channel is fully transparent and shows nothing of its colour.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Node opacity fades the whole image, character and white background alike.
- B: Godot's documentation notes that JPEG does not support transparency.
- C: Transparency needs an alpha value per pixel, which PNG stores and JPEG does not.
- D: Anti-aliased edge pixels are a blend of the character and the old background, so a colour key misses them.
- E: 255 is fully opaque; 0 is fully transparent.

**Source:** Alpha and transparency

## MA-ch02.4

A 32 x 32 pixel-art sprite is shown in a game at four times its size (128 x 128 screen pixels). At its original size it looks crisp, but in the running game its edges look blurry and smeared. The developer asks a coding agent to fix it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Nearest filtering takes the colour of the single closest texel, so enlarged pixel art keeps hard edges.
- [ ] B. The right fix is to regenerate the sprite at a higher resolution and keep the same filtering, since extra pixels resist blur.
- [ ] C. The instruction 'make it sharper' tells the agent that the texture filter should be set to nearest.
- [ ] D. Linear filtering blends neighbouring texels when a texture is enlarged, which softens hard pixel edges into blur.
- [ ] E. A filter mode set as the project-wide default applies to each sprite that does not set its own, while a mode set on one sprite applies only to that sprite.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Nearest samples one texel per screen pixel, producing blocks.
- B: More pixels still get blended by linear filtering; the cause is the sampling mode, not the source size.
- C: The word does not name the setting; the agent may sharpen the image file or change something else.
- D: Linear filtering interpolates between neighbouring texels.
- E: Scope follows where the setting is placed: a default covers everything that does not override it, and a setting on one sprite covers only that sprite (in Godot 4 this is the node's texture filter, which can inherit the project default).

**Source:** Nearest versus linear filtering

## MA-ch02.5

A pixel-art game is drawn in a 640 x 360 viewport with nearest filtering, and the window shows it scaled up to fill the screen. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A non-integer scale is harmless to pixel art as long as nearest filtering is on.
- [ ] B. In a 1,600 x 900 window the scale is 2.5, so some source pixels cover 2 screen pixels and others 3.
- [ ] C. In a 1,280 x 720 window the scale is exactly 2, so each source pixel becomes a 2 x 2 block of screen pixels.
- [ ] D. Switching to linear filtering removes the uneven pixel widths at a non-integer scale with no other change to the look.
- [ ] E. In a 1,366 x 768 window the scale is exactly 2 in both directions.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Nearest filtering makes the unevenness visible as pixels of different widths.
- B: 1,600 / 640 = 900 / 360 = 2.5; nearest filtering rounds each pixel to a whole number of screen pixels.
- C: 1,280 / 640 = 720 / 360 = 2.
- D: Linear filtering hides the unevenness by blurring everything.
- E: 1,366 / 640 is about 2.13 and 768 / 360 is about 2.13, neither a whole number.

**Source:** Integer scaling of pixel art

## MA-ch02.6

A developer is deciding which of four things to ask a coding agent to create or use: a sprite sheet, a texture atlas, a tileset and a tilemap. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A sprite sheet is one image holding the frames of an animation, typically in a regular grid of equal cells.
- [ ] B. An atlas packs many separate images, often of different sizes, into one texture with a record of each rectangle.
- [ ] C. A tilemap is the image file holding all the tile artwork, and a tileset is the painted level layout.
- [ ] D. A sprite sheet and a tileset can both be a single PNG laid out as a grid; they differ in how the engine uses the cells.
- [ ] E. A tileset is a library of reusable tiles; a tilemap is the level grid whose cells each reference one of them.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: This is the usual meaning, and the engine slices it into frames.
- B: Its purpose is to reduce texture switching so more sprites can be drawn together.
- C: The two terms are swapped.
- D: A sheet's cells are played in order as frames, while a tileset's cells are placed individually on the map.
- E: The tileset supplies the pieces and the tilemap places them.

**Source:** Sprite sheet, atlas, tileset, tilemap

## MA-ch02.7

A designer wants to paint cave levels quickly with 16 x 16 pixel tiles for floor, wall, ceiling and corners, so a 40 x 22 cell room can be painted with a brush. The designer tells a coding agent: 'make me a cave tilemap'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The artwork the designer needs is a tileset; 'tilemap' names the painted grid, not the library of tile art.
- [ ] B. 'Make me a cave tilemap' is precise enough, because the agent can infer tile size, tile count and edge rules from the word 'cave'.
- [ ] C. A precise request gives tile size (16 x 16), the tile types, matching edges, and one PNG with transparency in a grid.
- [ ] D. The tile size can be left out of the request, because the engine works it out from the image.
- [ ] E. The wording could be met by one 640 x 352 pixel painting of a finished room that cannot be rearranged.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The reusable tile images are the tileset.
- B: Nothing in the phrase fixes tile size, which tiles exist or how edges match.
- C: Each element removes a guess the agent would otherwise make.
- D: The engine has to be told the size of one tile to cut the image into tiles.
- E: 40 x 16 = 640 and 22 x 16 = 352; a single picture of that size matches the words but not the need.

**Source:** Say it to the agent: tileset or tilemap

## MA-ch02.8

An image generator is asked for a four-frame walk cycle 'in one row' and returns a single image of 800 x 200 pixels. The developer slices it as a grid of 4 columns and 1 row and plays the cells in order. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The playback speed of the walk cycle is stored in the image file as part of its pixel data.
- [ ] B. A frame count of 4 confirms that the four figures are four poses of one character.
- [ ] C. If the character's feet sit at a different height in each cell, the animation bobs even though each frame looks fine alone.
- [ ] D. Equal slicing gives correct frames whether or not the generator spaced the figures evenly, because each figure ends up centred in its cell.
- [ ] E. Equal slicing gives four cells of 200 x 200 pixels.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Speed is set in the engine, for example as frames per second on the animation.
- B: A count says how many cells there are, not whether the figures are the same creature.
- C: Frames must share a baseline and scale to play as one motion.
- D: Slicing cuts at fixed positions; unevenly spaced figures get cut apart or shifted.
- E: 800 / 4 = 200 wide and the height stays 200.

**Source:** Sprite sheet frame layout

## MA-ch02.9

An interviewer asks why a 2D game with 64 sprites, each a separate 32 x 32 image file, can run better after the images are packed into one 256 x 256 atlas. Check each statement that is true about a sound answer. Each statement is worth 1 point (5 points total).

- [ ] A. An atlas stores fewer pixels in total than the separate images it replaces, which is why it saves memory.
- [ ] B. The 64 sprites of 32 x 32 add up to 65,536 pixels, exactly the area of a 256 x 256 atlas, so the atlas has no room left for padding.
- [ ] C. Packing sprites into an atlas changes their on-screen size, so the sprites must be redrawn at the new scale.
- [ ] D. Sprites sharing one texture can often be batched into fewer draw calls, with no texture switch between them.
- [ ] E. Without padding, linear filtering or scaling can pull colour from a neighbouring sprite and bleed at the edges.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Padding and unused space can make it larger; the gain is fewer state changes, not fewer pixels.
- B: 64 x 32 x 32 = 65,536 = 256 x 256.
- C: An atlas changes where pixels are stored, not how large the sprite is drawn.
- D: Fewer texture switches allow batching.
- E: Sampling near a sprite's edge can read the next sprite's pixels.

**Source:** Why atlases help

## MA-ch02.10

A developer generates a 256 x 256 grass image to repeat across a large ground plane and will tell a coding agent to turn on repeat (tiling) for it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An image that looks good as a single picture will therefore look right when repeated across a surface.
- [ ] B. A seamless (tileable) texture is one whose opposite edges match, so repeated copies show no visible join.
- [ ] C. Making the image tileable requires making it smaller than 256 x 256, so the edges can be blended.
- [ ] D. A seamless texture shows no visible repetition across a large area, however large the area is.
- [ ] E. The way to test tileability is to view a single copy at full size, since a seam can only exist at the image's edge.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Nothing about a single view guarantees the edges line up with their copies.
- B: Seamlessness is a property of the image's edge content.
- C: Tileability depends on matching edges, not on image size.
- D: Without a visible join the pattern can still repeat noticeably when distinctive features recur.
- E: A seam is the join between copies, so test with copies placed side by side.

**Source:** Seamless and tileable textures

## MA-ch02.11

A pixel-art game restricts all art to a 16-colour palette. An image generator is asked for an enemy sprite 'using only these 16 colours', and the returned file is opened in a script that counts its distinct colours. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Counting distinct colours and testing each against the palette is a check a script can do.
- [ ] B. Smoothed or anti-aliased edges introduce in-between colours that are not in the palette, so a count above 16 is likely.
- [ ] C. An indexed-colour image stores a palette plus an index per pixel, so editing palette entries recolours the sprite without changing the index data.
- [ ] D. A palette is a fixed set of colours the art draws from, and using one palette across assets helps them look like they belong together.
- [ ] E. An image generator reliably honours 'only these 16 colours', so counting the colours in the result is unnecessary.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: It is an exact, automatable test.
- B: Blended edge pixels are extra colours.
- C: That separation is what makes palette swaps cheap.
- D: A shared palette is a main source of visual consistency in pixel art.
- E: Generators approximate such constraints; the count is a check that costs nothing.

**Source:** Palette

## MA-ch02.12

In Godot, a PNG added to a project is converted by an importer, and its import settings (such as compression mode and mipmaps) are stored in a small text file next to it; that file holds the choices made for this image, which the engine cannot work out from the PNG alone. A developer asks a coding agent to 'make the sprite crisp'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The small settings file next to the PNG is created by the engine on import, so it can be left out of version control without losing the choices made for the sprite.
- [ ] B. For 2D pixel art, hardware (VRAM) texture compression is the recommended setting because it makes textures smaller with no visible cost.
- [ ] C. Turning on mipmaps sharpens a sprite that is drawn at its native size.
- [ ] D. 'Make the sprite crisp' is precise enough to tell the agent which filter, compression and mipmap settings to change.
- [ ] E. At runtime the engine uses the imported copy, so changing import settings changes the result without editing the PNG.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The file records the choices made for the image, which cannot be recovered from the PNG alone, so a clone without it falls back to default import settings; it belongs in version control with the asset.
- B: Godot's documentation recommends lossless for pixel art and says VRAM compression shows noticeable artifacts in 2D.
- C: Mipmaps are pre-shrunk copies for drawing something smaller; they add memory and do not sharpen.
- D: The phrase names a result, not the settings; the agent may change the wrong ones or the image itself.
- E: Import settings act between the source file and the game.

**Source:** Import settings

## MA-ch02.13

A sound effect is stored as uncompressed (PCM) audio with 16 bits per sample, 2 channels (stereo) and 44,100 samples per second. It lasts 10 seconds. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Converting to mono at the same rate and bit depth reduces the data to 441,000 bytes.
- [ ] B. A 5 kHz tone can be captured at 8,000 samples per second, since 5,000 is below 8,000.
- [ ] C. The highest frequency this sample rate can represent is half of it, 22,050 Hz.
- [ ] D. The data size is 44,100 x 2 bytes x 2 channels x 10 s = 1,764,000 bytes.
- [ ] E. Raising the sample rate to 88,200 samples per second makes the sound louder.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: One channel halves the size to 882,000 bytes, not 441,000.
- B: The limit at 8,000 samples per second is 4,000 Hz, so a 5 kHz tone cannot be represented correctly.
- C: A sampled signal can represent frequencies up to half the sample rate.
- D: 16 bits is 2 bytes per sample per channel.
- E: Sample rate sets how finely time is sampled and the highest frequency, not the level.

**Source:** Sample rate and audio size

## MA-ch02.14

A model generates an 8-bar music track at 120 beats per minute in 4/4 time to loop behind a level, and the developer wants it to loop with no audible gap or jump. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. At 120 BPM in 4/4, eight bars last 16 seconds, which is 705,600 samples at 44,100 Hz.
- [ ] B. Cutting the loop at a bar line, not an arbitrary point, keeps the rhythm unbroken across the join.
- [ ] C. A track that sounds smooth when played once from start to end is guaranteed to loop seamlessly.
- [ ] D. A fade-out baked into the end of the file does not matter, because the loop restarts at full volume.
- [ ] E. A sharp jump between the last and first sample can cause an audible click at the loop point.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: 8 bars x 4 beats = 32 beats at 2 beats per second = 16 s; 16 x 44,100 = 705,600.
- B: A loop that ends mid-bar shifts the beat on every repeat.
- C: A single play never exercises the join between end and start.
- D: The fade makes an audible dip followed by a jump back up at each repeat.
- E: An abrupt jump in value is heard as a click.

**Source:** Audio loops

## MA-ch02.15

A developer is choosing file formats and playback behaviour for a short coin-pickup effect and a three-minute background track. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Lossless audio (WAV, FLAC) keeps all samples; lossy audio (Ogg Vorbis, MP3) discards detail for good.
- [ ] B. FLAC is a lossy format, because any compressed audio file has thrown some detail away.
- [ ] C. An effect is usually short, event-triggered and may overlap itself; music is long and usually loops.
- [ ] D. Converting one lossy file to another lossy format at the same bit rate loses nothing extra, since the rate is unchanged.
- [ ] E. Once a track is saved as a lossy file, the original uncompressed audio can be rebuilt exactly from it.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Lossy encoding trades information for size.
- B: Compressed does not mean lossy; FLAC compresses without discarding anything.
- C: These differences drive format and playback choices.
- D: Each lossy encoding discards more detail, so quality degrades with every generation.
- E: The discarded detail is gone, so only an approximation can be rebuilt.

**Source:** SFX versus music; lossless versus lossy

## MA-ch02.16

A game routes sound effects to a bus named SFX and music to a bus named Music. Both feed a Master bus that goes to the speakers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A bus whose volume is set to 0 dB is silent, because zero means no signal is passed on.
- [ ] B. Raising the SFX bus by 6 dB multiplies the amplitude of the effects on it by 6, which is why small steps are safe.
- [ ] C. A bus is a channel audio passes through on the way to the output; its volume and effects apply to all sources routed to it.
- [ ] D. Lowering the Music bus by 6 dB cuts the amplitude of all music to roughly half and leaves the SFX bus unchanged.
- [ ] E. If loud sounds sum past the digital maximum at the Master output, the result clips and distorts.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: 0 dB means no change in level (unity gain); silence is a very large negative value.
- B: 6 dB is a factor of about 2; adding 12 dB gives about 4.
- C: Godot's documentation describes a bus as a place audio is channelled through before playback.
- D: A 6 dB change is about a factor of 2 in amplitude, and only sources routed to that bus are affected.
- E: Simultaneous sounds sum, and the sum can exceed the maximum representable level.

**Source:** Audio buses and decibels

## MA-ch02.17

In a platformer, the coin pickup sound is played by one audio player node limited to a single simultaneous voice. When the player grabs three coins within 0.15 seconds, the sound is heard as one clipped blip. A developer asks a coding agent to 'make the coin sound better'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Allowing more simultaneous voices on the player lets overlapping copies of the sound be heard together.
- [ ] B. With a limit of one voice, each new play request cuts off the sound still playing, which explains the clipped blip.
- [ ] C. Playing the sound once when the player first touches a coin, rather than repeatedly during the overlap, makes the cut-off worse.
- [ ] D. 'Make the coin sound better' tells the agent that the real problem is the limit on simultaneous voices.
- [ ] E. Making the audio file louder fixes the clipped blip, because the sound will survive being cut off.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Raising polyphony is the direct fix.
- B: Exceeding the voice limit drops the oldest playing sound.
- C: Triggering on the transition into overlap reduces repeated play calls.
- D: The phrase names no problem; the agent may re-edit or replace the sound file.
- E: Loudness is unrelated to voices being cut off.

**Source:** Say it to the agent: polyphony

## MA-ch02.18

A studio is reviewing sprites produced by an image generator for a pixel-art game. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A smoothed, JPEG-compressed picture of pixel-art-looking creatures can be turned into clean pixel art by shrinking it with linear filtering.
- [ ] B. A generated picture can look like pixel art while its 'pixels' are several source pixels wide and blurred, so it sits on no exact grid.
- [ ] C. 'Pixel art' means an image with a retro colour scheme, however it was made.
- [ ] D. Pixel art is authored at a low resolution on a grid, with each pixel placed deliberately.
- [ ] E. Pixel art is normally shown at a whole-number scale with nearest filtering so each art pixel stays a crisp block.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Shrinking blends the artifacts into the result and does not restore a clean grid.
- B: The look of blocky pixels does not guarantee a true pixel grid.
- C: The term describes how the image is built, not only how it looks.
- D: Control over individual pixels is what defines the style.
- E: Uneven scaling or blending destroys the intended pixel shapes.

**Source:** Pixel art

## MA-ch02.19

A developer is shipping a game that uses an AI-generated sprite and an AI-generated music track. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A generating tool's terms can restrict use, for example to non-commercial work, so read them before shipping.
- [ ] B. Having written the prompt gives the developer full copyright in the output, in the countries where the game is sold.
- [ ] C. An unrecorded reference image can leave its licence doubt attached to anything generated from it.
- [ ] D. Provenance is the record of an asset's origin: tool and version, prompt and settings, terms, edits and references.
- [ ] E. A provenance record helps regenerate or replace an asset later, since it holds the prompt and settings.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Some models and services carry non-commercial terms.
- B: Ownership of generated output depends on the tool's terms and the jurisdiction, and prompts alone may not suffice.
- C: A result derived from an unknown reference inherits the doubt about the reference.
- D: A provenance log is the evidence trail for an asset.
- E: Recorded settings make an asset reproducible and replaceable.

**Source:** Licence and provenance
