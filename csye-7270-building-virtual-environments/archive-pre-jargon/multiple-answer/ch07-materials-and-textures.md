# Chapter 7: Materials and textures

## MA-ch07.1

In physically based rendering, a surface is described by a few separate properties. One of them is albedo (also called base colour). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Albedo is the colour a surface reflects diffusely, independent of the scene's lights; the renderer combines it with lighting.
- [ ] B. The colour a pixel shows on screen equals its albedo, because albedo is the finished colour of the surface.
- [ ] C. An albedo texture with shadows and highlights painted in will look double-shaded once the engine's lighting is applied.
- [ ] D. For a bare metal, the base colour tints the reflections, since a metal has little diffuse colour of its own.
- [ ] E. Albedo controls how blurry the surface's reflections are, with darker albedo giving sharper reflections.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Albedo is the intrinsic colour of the surface; lights, shadows and reflections are applied on top of it by the renderer.
- B: The final pixel colour also depends on light colour, light direction, shadows and reflections, so it is not the albedo alone.
- C: Baked lighting in the texture stacks with the engine's lighting, giving shadows twice and shading that does not move with the lights.
- D: In the metallic-roughness model, a metal's reflectance colour comes from the base colour.
- E: Blur of reflections is controlled by roughness.

**Source:** What is albedo

## MA-ch07.2

A developer tells a coding agent: "Make the ship's hull shinier." The hull's material currently has an albedo texture of weathered wood, metallic 0, roughness 0.8 and the default specular value. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Lowering roughness (for example from 0.8 to 0.3) makes reflections sharper and highlights tighter, which reads as shinier.
- [ ] B. Brightening the albedo texture makes the hull shinier, since lighter surfaces reflect more of the light that hits them.
- [ ] C. "Shinier" is ambiguous: glossy paint (non-metal, low roughness) and polished metal (metallic near 1, low roughness) are different looks.
- [ ] D. Raising the emission colour is the right change, because emission adds the highlights to a surface and so reads as shine.
- [ ] E. In an engine that uses smoothness instead of roughness, such as Unity's standard lit materials, shinier means lowering smoothness.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Roughness controls how blurred reflections are; lower values concentrate them into sharper highlights.
- B: Albedo changes the base colour, not how glossy the surface is.
- C: The word covers different material setups, and the agent needs to know whether metallic changes too.
- D: Emission adds light of its own regardless of the scene, so it makes the hull glow rather than reflect.
- E: Smoothness is roughly the opposite of roughness, so a shinier surface has a higher smoothness value.

**Source:** Say it to the agent: shinier means roughness, metallic or specular

## MA-ch07.3

In the metallic-roughness material model, a surface has a metallic value between 0 and 1. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Metallic controls how blurry the reflections are, so metallic 1 gives the blurriest reflections.
- [ ] B. Metallic 0 is a non-metal (dielectric) such as plastic, wood or skin; metallic 1 is a bare metal such as steel or gold.
- [ ] C. A fully metallic surface with a pure black albedo still shows bright, naturally coloured reflections of its surroundings.
- [ ] D. Intermediate metallic values mostly mark transitions, such as rust, dirt or chipped paint at the edge of a metal.
- [ ] E. Metallic and specular are two names for the same control, and raising either has the same effect.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Reflection blur is roughness.
- B: Metallic is the switch between the non-metal and metal behaviours of the model.
- C: For a metal the base colour supplies the reflection tint, so a black albedo gives almost no reflection.
- D: A real surface is metal or not at each point, so in-between values stand for mixed or partly covered areas.
- E: Specular scales the strength of reflection on non-metals, while metallic changes the kind of material.

**Source:** Metallic

## MA-ch07.4

A technical artist sets up three surfaces in the metallic-roughness model. Rubber ball: metallic 0, roughness 0.9. Chrome sphere: metallic 1, roughness 0.05. Glossy plastic toy: metallic 0, roughness 0.2, default specular. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The chrome sphere shows a sharp, mirror-like reflection of its surroundings.
- [ ] B. The rubber ball shows sharp reflections, since roughness 0.9 means a very smooth surface.
- [ ] C. The plastic toy's highlights are tinted by its albedo, as a metal's reflections are.
- [ ] D. Setting the rubber ball's metallic to 1 while leaving roughness at 0.9 would turn it into a mirror.
- [ ] E. Raising the chrome sphere's roughness to 0.9 would make its reflection sharper.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Metallic 1 with roughness near 0 gives a near-mirror finish.
- B: A roughness of 0.9 blurs reflections almost completely; it is a rough surface.
- C: Highlights on a non-metal are mostly untinted (whitish), while the diffuse body takes the albedo colour.
- D: It would become a dull, blurred metal, because roughness 0.9 still smears the reflections.
- E: Higher roughness spreads and blurs the reflection, the opposite of sharpening it.

**Source:** Roughness, metallic and specular compared

## MA-ch07.5

A brick wall has two supporting images: a height map (greyscale, white = high, black = low) and a tangent-space normal map (a mostly purple-blue colour image). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Both can make a flat surface shade as if it had bumps without adding any triangles.
- [ ] B. A normal map stores a surface direction in each texel, with red, green and blue encoding the x, y and z of a vector.
- [ ] C. A normal map changes the silhouette of the wall seen at a grazing angle, so the bricks stick out of its outline as real geometry would.
- [ ] D. A height map used for bump mapping gives the slope between neighbouring texels, from which a shading normal can be derived.
- [ ] E. Real displacement, which changes the silhouette, needs enough vertices (a dense mesh or tessellation); normal and bump maps only change shading.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Both alter the normal used in lighting, so the surface reacts to light as if it were uneven.
- B: A normal map is a vector image: each texel's three channels encode a direction.
- C: The geometry's outline is unchanged, so at a grazing angle the edge of the wall still looks straight.
- D: Bump mapping derives a normal from how the height changes between texels.
- E: Actually moving the surface requires geometry to move; parallax tricks only fake depth.

**Source:** Normal map versus height or bump map

## MA-ch07.6

A developer downloads a wood-floor texture pack with the files floor_albedo.png, floor_normal.png, floor_roughness.png and floor_ao.png, and tells a coding agent: "Put the wood floor texture on the floor mesh." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The instruction is complete, since the word "texture" already tells a coding agent which of the four images goes in which slot.
- [ ] B. If floor_normal.png is put in the albedo slot, the floor is tinted blue-purple but also keeps the bumps, since the image still carries the surface directions.
- [ ] C. The instruction is too vague: it does not say which file belongs in which slot, so the agent may put an image in the wrong slot.
- [ ] D. If floor_albedo.png is put in the normal slot, the floor still shows the wood colouring, because the picture's colours are drawn from whichever slot it is in.
- [ ] E. A greyscale roughness image placed in the albedo slot still acts as roughness, because the engine looks at what an image contains to decide how to use it.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: "Texture" names four different kinds of image here, each belonging to a different quantity.
- B: In the albedo slot the image is read only as colour, so the floor turns blue-purple and gets no bumps from it.
- C: Naming the slot for each file, or at least saying which file is which kind of map, removes the guesswork.
- D: A colour picture in the normal slot is read as directions, so the wood colours do not appear and the shading is noisy and wrong.
- E: Engines read an image according to the slot it is assigned to, not according to what it looks like.

**Source:** Say it to the agent: which image goes in which slot

## MA-ch07.7

A tangent-space normal map stores a direction in each texel. Each 8-bit channel value c (0 to 255) is converted to a vector component by n = 2 × (c / 255) − 1, with red as x, green as y and blue as z. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The texel (128, 128, 255) decodes to about (0.5, 0.5, 1.0), a direction tilted well away from the surface normal.
- [ ] B. The texel (128, 128, 255) decodes to about (0, 0, 1), straight out of the surface, so that texel shades as flat.
- [ ] C. Because the vectors are in tangent space, the map must be re-baked each time the object rotates in the scene.
- [ ] D. Tangent space means the vectors are relative to the surface (x along U, y along V, z along its normal), so the map survives rotation.
- [ ] E. A normal map looks mostly purple-blue because most texels are near (128, 128, 255): most of the surface points almost straight out.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: 2 × (128/255) − 1 is about 0.004, not 0.5, so the first two components are near zero.
- B: The decoded vector is (0.004, 0.004, 1.0), essentially the unperturbed surface normal.
- C: The vectors are stored relative to the surface, so rotating the object does not invalidate the map.
- D: Expressing directions in the surface's own frame is what makes a tangent-space map reusable on any orientation or deformation.
- E: Blue is z, which is near full for slight slopes, and red and green sit near the middle value 128.

**Source:** Tangent space and normal decoding

## MA-ch07.8

A wooden crate has an ambient occlusion (AO) texture that is white where light reaches freely and dark in the creases between planks. The crate sits in a scene lit by one strong directional light plus a dim ambient light. Assume the engine applies the AO texture to ambient light only, which is the default behaviour in Godot and matches the glTF 2.0 specification. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The AO texture is a shadow cast by the directional light, so it moves when the light rotates.
- [ ] B. The AO texture and screen-space ambient occlusion (SSAO) are the same effect, so enabling both changes nothing.
- [ ] C. AO approximates how much ambient light reaches each point, so creases receive less of it, as in a real crevice.
- [ ] D. Because the AO texture does not dim the directional light, the creases look only slightly different from a version without AO.
- [ ] E. The AO texture holds colour, so it should be imported as sRGB colour data like the albedo texture.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: AO is baked into the material and does not depend on the position of a light.
- B: The texture is authored in advance, while SSAO is a post-process computed from the depth buffer each frame; using both can darken creases twice.
- C: Ambient occlusion models how enclosed a point is, and so how much indirect light can reach it.
- D: With AO limited to ambient light, the strong direct light still lights the creases fully.
- E: AO is a single-channel data image whose values are used as numbers, so it is read as linear.

**Source:** Ambient occlusion

## MA-ch07.9

A designer gives a lamp mesh an emission colour so that it appears to glow. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Emission adds colour to the surface's final appearance independent of scene lighting, so the lamp still glows in a dark room.
- [ ] B. In a basic real-time renderer with no global illumination, an emissive mesh also lights the nearby walls the way a point light does.
- [ ] C. Emission values above 1.0 are meaningless, because colours cannot exceed 1.0 on a modern display pipeline.
- [ ] D. To light nearby surfaces, the developer needs a light source or a global-illumination feature that treats emissive surfaces as lights.
- [ ] E. Emission is another name for albedo at a higher brightness, so a brighter albedo would glow the same way.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Emission is added to the lit result, so it is not dimmed by darkness.
- B: Emission only affects the pixels of the emissive surface itself, unless a global-illumination feature reads it.
- C: High-dynamic-range rendering allows values above 1.0, which are what bloom or glow effects pick up.
- D: Lighting neighbours needs a real light or a feature that treats emissive surfaces as light sources.
- E: Albedo is reflected colour that depends on lighting; emission is light the surface gives off.

**Source:** Emission

## MA-ch07.10

PBR (physically based rendering) is the standard way modern engines describe materials. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. PBR requires a photorealistic art style, so stylised or cartoon games cannot use it and have to use a different material system.
- [ ] B. PBR does not require ray tracing; it is a way of describing surfaces and light that works in ordinary rasterizing renderers.
- [ ] C. PBR describes a surface by properties such as base colour, roughness and metallic that stay meaningful under different lighting.
- [ ] D. Energy conservation is a PBR principle: a surface cannot reflect more light than it receives, so rougher highlights are wider and dimmer.
- [ ] E. "Physically based" refers to the model of light and surface; artists still tune values by eye rather than measuring real objects.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: PBR is a way to organise material parameters, and stylised games commonly use it with non-realistic textures.
- B: PBR materials are used in rasterizers; ray tracing is a separate rendering technique.
- C: Separating the surface description from the lighting is the main benefit of PBR.
- D: When a highlight is spread over a wider area, it is also dimmer, because the same light energy is distributed.
- E: The values are authored or tuned; the model only constrains how they combine.

**Source:** PBR

## MA-ch07.11

A material pack contains five images: albedo, normal map, roughness, ambient occlusion and emission colour. Colour images are normally stored in the sRGB encoding, and the renderer decodes them to linear values before lighting math. Data images hold numbers that must be used as stored. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Albedo is colour and should be flagged or imported as sRGB, so it is decoded to linear for lighting.
- [ ] B. The normal map, roughness and ambient occlusion images are all colour images and should be flagged as sRGB, like albedo.
- [ ] C. Emission colour is colour, authored like albedo, and should be treated as sRGB.
- [ ] D. A roughness image is data: its stored value is the number the shading uses, so an sRGB decode would change the number.
- [ ] E. A wrong colour-space flag raises no error, so the developer should tell the agent which maps are colour and which are data.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Albedo is a picture of a colour as seen by people, so it is stored in sRGB.
- B: These three are data maps and must be read linearly; they are images only because that is how the data is stored.
- C: Emission is a colour and is authored like albedo.
- D: A data value of 0.5 should stay 0.5; decoding it as sRGB turns it into about 0.22.
- E: Because nothing fails visibly, the instruction to the agent needs to say which map is which.

**Source:** Colour textures versus data textures

## MA-ch07.12

A roughness map has a uniform mid-grey value of 128 out of 255 (about 0.50), meant to read as roughness 0.50. The texture is wrongly imported as an sRGB colour texture, so the renderer applies the sRGB-to-linear decode to it. For an input of 0.502 that decode gives about 0.216. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The error is invisible, because the decoded number is the same mid-grey.
- [ ] B. The surface is shaded with a roughness of about 0.22 instead of 0.50, so it looks glossier than intended.
- [ ] C. If a mid-grey albedo (128/255) were wrongly treated as linear data instead of sRGB colour, the surface would come out darker than intended.
- [ ] D. The correct fix is to multiply the roughness in the shader by about 2.3.
- [ ] E. Importing the roughness map as linear data would use 0.502 unchanged, as authored.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The decode changes the number from about 0.50 to about 0.22, which changes the look.
- B: Lower roughness means sharper, stronger reflections, so the surface looks glossier.
- C: Treating sRGB as linear skips the decode, so 0.502 is used instead of 0.216 and the surface looks brighter and washed out.
- D: The sRGB curve is not a constant factor, and a multiplier would be a hack; the correct fix is the import flag.
- E: A linear import uses the stored value as the number, which is what a data map needs.

**Source:** sRGB versus linear decoding

## MA-ch07.13

A long tiled floor uses a high-contrast checker texture of 2048 × 2048 texels stored as RGBA8 (4 bytes per texel, 16 MiB for the base level). Far from the camera the floor shimmers and crawls as the camera moves. A coding agent is asked to fix the shimmering and turns on mipmaps, a chain of precomputed half-size copies (1024 × 1024, 512 × 512, and so on down to 1 × 1). The full chain, including the base level, occupies about 21.3 MiB. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Mipmaps make the texture look sharper when the camera is very close to the floor, because extra levels add detail.
- [ ] B. For distant floor where many texels fall in one screen pixel, the GPU reads a smaller pre-averaged level, which removes much of the shimmer.
- [ ] C. The mip chain adds about one third to the texture's memory (16 MiB becomes about 21.3 MiB).
- [ ] D. Enabling mipmaps replaces the full-size level, so the texture no longer has its 2048 × 2048 detail up close.
- [ ] E. A 2D sprite drawn at its native size is not shrunk, so it gets little benefit from mipmaps.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Close up, the full-size level is used, so mipmaps change nothing about magnification.
- B: Averaging in advance avoids the aliasing that comes from sampling a few texels out of many.
- C: 1 + 1/4 + 1/16 + ... approaches 4/3 of the base size; 16 MiB × 4/3 is about 21.3 MiB.
- D: The base level stays in the chain and is still used where the surface is large on screen.
- E: Mipmaps help only when a texture is minified, and a native-size sprite is not.

**Source:** Mipmaps

## MA-ch07.14

A 2048 × 2048 albedo texture is a 3 MB PNG file on disk. Kept as plain RGBA8 in video memory (32 bits per texel) its base level takes 16 MiB. A GPU block-compressed format that stores 8 bits per texel would take 4 MiB for the same base level. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 3 MB PNG tells you little about video memory use: kept uncompressed on the GPU, it still occupies 16 MiB.
- [ ] B. Block-compressed GPU formats are lossless, so image quality is identical to the PNG and nothing is traded away.
- [ ] C. Block-compressed textures can stay compressed in video memory, because the GPU decodes them on the fly when sampling.
- [ ] D. A normal map can be compressed with the same format and settings as an albedo texture with no concern for artefacts.
- [ ] E. At 8 bits per texel, the base level takes 4 MiB, a quarter of the 32-bits-per-texel size.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Lossless file formats such as PNG shrink the file on disk, but the GPU needs the decoded texels unless a GPU format is used.
- B: Block compression is lossy and can show banding or blocky artefacts, especially on smooth gradients.
- C: This is why block compression reduces video memory and bandwidth, not just disk size.
- D: Small errors in normal vectors show up as lighting artefacts, so engines offer dedicated normal-map compression.
- E: 2048 × 2048 × 8 bits is 4 MiB, one quarter of the 16 MiB at 32 bits.

**Source:** Texture compression and video memory

## MA-ch07.15

A texture is sampled when a screen pixel maps to a spot that lies between texel centres or covers many texels. Engines offer these filtering modes: nearest (point), bilinear, trilinear and anisotropic. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Nearest takes the single closest texel, so a magnified texture looks blocky but keeps hard edges, which suits pixel art.
- [ ] B. Bilinear filtering blends the four closest texels of one mip level to give smooth magnification.
- [ ] C. Trilinear filtering also blends between two adjacent mip levels, which hides the seam where the level in use changes.
- [ ] D. Anisotropic filtering adds no extra texture reads, so it costs nothing compared with bilinear filtering.
- [ ] E. Anisotropic filtering mainly improves surfaces seen at shallow angles, such as a floor stretching away from the camera.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Nearest filtering keeps each texel as a hard block.
- B: Bilinear interpolation uses the four texels around the sample point.
- C: Blending two mip levels removes the visible banding between them.
- D: Anisotropic filtering takes extra samples along the stretched direction, so it costs more than the simpler modes.
- E: Surfaces at a shallow angle cover a stretched patch of texture, which plain mipmapping blurs and anisotropic filtering keeps sharper.

**Source:** Texture filtering

## MA-ch07.16

A floor is 8 m wide and uses a seamless 512 × 512 texel brick texture. With UV scale 1 the texture is stretched once across the 8 m. A developer asks a coding agent: "make the bricks smaller." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A UV scale of 4 leaves the floor's texel density, the number of texels per metre of surface, at 64, because the image is still 512 × 512 texels.
- [ ] B. A UV scale of 4 makes the texture four times larger in memory, because four copies of it are now drawn on the floor.
- [ ] C. A UV scale of 4 repeats the texture four times across the width: each repeat covers 2 m, so bricks look four times smaller.
- [ ] D. A UV scale of 4 makes the floor mesh four times as large, because scaling the mapping scales the geometry too.
- [ ] E. For the repeats to look right the texture must be seamless and the wrap mode must be repeat; with clamp, edge texels smear.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Density counts texels per metre of surface: 512 texels over 8 m is 64 per metre at scale 1, and at scale 4 there are 2048 texels over 8 m, which is 256 per metre.
- B: UV scale changes how coordinates are mapped, not the texture's size in memory.
- C: Multiplying the UVs by 4 fits four copies across the same surface, each 8 / 4 = 2 m wide.
- D: UV scale changes the mapping on the mesh and leaves the mesh itself alone.
- E: Repeating requires a seamless image so no joins show, and a repeat wrap mode so coordinates beyond 1 wrap around.

**Source:** Tiling and UV scale

## MA-ch07.17

A forest scene has three tree meshes. All three use the same bark shader program, but each tree's material has a different bark texture and a different tint value. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A shader is the program that computes how a surface is drawn; a material bundles a shader with its values and textures.
- [ ] B. A texture is a kind of material, so the scene contains three shaders, one per texture.
- [ ] C. Because they share one shader, the three trees share one material, so changing the tint on one changes all three.
- [ ] D. The scene has three materials that all point at the same shader program.
- [ ] E. One bark texture could also be used by several different materials at once.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The shader is the code; the material holds the shader plus its parameter values and texture bindings.
- B: A texture is image data that a material uses, not a kind of material, and the scene has only one shader.
- C: Each tree has its own material with its own parameter values, so changing one material does not affect the others.
- D: Three different parameter and texture sets means three materials, all pointing at the same program.
- E: Textures are shared resources that any number of materials can reference.

**Source:** Material versus shader versus texture

## MA-ch07.18

Twenty enemy nodes share a single material resource. A developer asks a coding agent: "make the enemy that was just hit turn red." The agent changes the colour parameter on the shared material, and all twenty enemies turn red. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The agent edited the shared material, so all objects that use it change; the change is not per object.
- [ ] B. A fix is to give the hit enemy its own material copy or instance, or a per-object parameter (in Godot, a per-instance shader uniform).
- [ ] C. When several nodes reference one material resource, editing the material through one node's reference changes only that node, because each node keeps a private copy.
- [ ] D. Making a per-object copy of a material compiles a brand-new shader program for each enemy, which is why copies are costly.
- [ ] E. A material instance, a child that inherits a parent material and overrides only parameter values, reuses the parent's shader program, so changing its parameters does not require compiling a new shader.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A material is a shared resource; objects reference it, and editing it affects all references.
- B: Per-object materials or per-instance parameters make the change local to one enemy.
- C: A reference points at the one shared resource, so an edit made through any node's reference changes what all of them draw; only a real copy isolates one node.
- D: A copy shares the same shader program and differs only in its parameter values.
- E: An instance differs from its parent only in parameter values, so it shares the parent's compiled shader and changing the values needs no recompile.

**Source:** Material instances and shared materials

## MA-ch07.19

An artist packs sixteen 256 × 256 prop textures into one 1024 × 1024 texture atlas (4 × 4 cells). Each prop's UV coordinates are changed to address its own cell. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Props that share the atlas can share one material, which can reduce material and texture switches and draw calls.
- [ ] B. Hardware texture repeat can still tile one prop's cell, because the sampler wraps at the cell edge.
- [ ] C. The atlas makes each prop's texture sharper, since it is part of a larger, higher-resolution image.
- [ ] D. A texture atlas is the same thing as a mipmap chain, since both hold several images in one texture.
- [ ] E. With filtering and mipmaps, colours from neighbouring cells can bleed across a border unless each cell is padded.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: One material and one texture can serve many meshes, so fewer state changes are needed when drawing them.
- B: Wrapping happens at the edge of the whole texture, not of a cell, so a cell cannot be tiled by hardware repeat.
- C: Each prop keeps its own resolution of 256 × 256; packing does not add detail.
- D: An atlas holds different images side by side; a mip chain holds the same image at decreasing sizes.
- E: Filtering reads texels near a border, which may belong to the next cell, so padding is needed.

**Source:** Texture atlas

## MA-ch07.20

To save memory and texture reads, some pipelines pack three greyscale maps into the red, green and blue channels of one image. One common arrangement, called ORM (or ARM), is red = ambient occlusion, green = roughness, blue = metallic. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A packed ORM image can be dropped into any engine's mask-map slot unchanged, since the channel order is standardised.
- [ ] B. In an engine that uses smoothness instead of roughness, the green channel can be used as it is, with no inversion.
- [ ] C. A packed image holds data, not colour, so it should be read as linear rather than sRGB, or the values are altered.
- [ ] D. Packing replaces three separate texture reads with one read that returns all three values.
- [ ] E. If the roughness lookup reads the blue channel by mistake, glossiness follows the metallic map instead of the roughness map.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Channel layouts differ between pipelines, so a packed texture usually has to be repacked for a different engine's slot.
- B: Smoothness is roughly 1 minus roughness, so the channel would have to be inverted.
- C: Its channels are numbers used by the shading model, which a colour decode would corrupt.
- D: One texture sample returns all three values at once, which saves memory bandwidth and texture slots.
- E: A wrong channel binding gives plausible-looking but wrong values, with roughness taking the metallic map's pattern.

**Source:** Channel-packed textures (ORM)
