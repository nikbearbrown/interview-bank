# Chapter 7: Materials and textures

## ES-ch07.1

In an interview you are asked: "What is albedo?" A developer then tells a coding agent: "Use this photo of a brick wall as the wall's colour texture." The photo was taken in strong afternoon sun and has a dark shadow across its left third. Define albedo precisely and say how it differs from the colour you see on screen. Explain what will look wrong in the game and why, and rewrite the instruction so that an agent and an artist would produce a correct result.

**Points:** 5

**Rubric (1 point each):**

1. Defines albedo (base colour) as the colour a surface reflects diffusely, independent of the lighting, and says the colour on screen is albedo combined with lights, shadows, reflections and emission.
2. Explains that the photo contains baked lighting (a cast shadow and highlights) that is not part of the surface colour, so the engine's lighting stacks on top and the shading is applied twice.
3. Describes the visible symptoms: the shadow stays fixed on the wall when lights move or in a different lit room, and the wall looks dirty or unevenly lit in a way that cannot be controlled.
4. States the fix: remove the lighting from the image (delighting) or use an evenly lit or scanned albedo.
5. Gives a rewritten instruction that names the slot (albedo or base colour) and the requirement (no baked shadows or highlights in the image).

**Source:** What is albedo

## ES-ch07.2

A developer tells a coding agent: "Make the ship's hull look like polished steel and shinier." Explain roughness, metallic and specular and what each controls. Say which of them the agent should change, and which tempting changes (albedo, emission) would be wrong and why. Then rewrite the instruction with concrete parameter targets, and say what the scene needs in order for a smooth metal to look right.

**Points:** 5

**Rubric (1 point each):**

1. Defines roughness (how blurred reflections are, 0 mirror-like and 1 fully blurred) and metallic (non-metal versus bare metal, where a metal's reflections take the base colour as their tint).
2. Defines specular (strength of reflection on non-metals) and states which controls the agent should change: "shinier" steel is done by lowering roughness and raising metallic toward 1, and specular is not the control for a metal.
3. Explains why the tempting changes are wrong: a lighter albedo makes the surface lighter, not glossier, and emission makes it glow rather than reflect.
4. Rewrites the instruction with concrete targets for the parameters (for example metallic near 1, roughness around 0.2 to 0.3, base colour a steel grey).
5. Says that a smooth metal needs an environment or reflection source in the scene to have anything to reflect.

**Source:** Say it to the agent: shinier means roughness, metallic or specular

## ES-ch07.3

An artist asks a coding agent to "add depth to the stone wall with a normal map", and also expects the stones to stick out of the wall's outline at an outside corner. Explain what a normal map is, how it differs from a height or bump map, and what a tangent-space normal map means. Say what a normal map can and cannot do for this wall, what the agent should do about the outline, and name two ways the normal map can be set up wrong and how each one looks.

**Points:** 5

**Rubric (1 point each):**

1. Defines a normal map as an image storing a surface direction per texel (red, green, blue as x, y, z) that changes how light shades the surface without changing the geometry.
2. Contrasts it with a height or bump map, a greyscale elevation image from which slopes (or parallax or displacement) are derived, and notes only real displacement moves vertices.
3. Explains tangent space: directions are stored relative to the surface (x along U, y along V, z out of the surface), so the map works on any orientation, and a flat texel is the pale blue (128, 128, 255).
4. States that a normal map cannot change the silhouette, so stones sticking out at the corner need real geometry, tessellated displacement, or a parallax effect that only fakes depth.
5. Names two setup errors with their appearance, for example a flipped green channel (the engine expects the opposite Y convention) so bumps look like dents under light from above, or the map imported as sRGB colour so lighting is tilted and wrong.

**Source:** Normal map versus height or bump map

## ES-ch07.4

Explain the difference between colour textures and data textures, and what sRGB and linear mean for them. Classify these five images: albedo, normal map, roughness, ambient occlusion, emission colour. For two of the wrong-flag mistakes, predict what the result looks like and give at least one number. Explain why this kind of mistake is hard to notice, and what the developer should say to a coding agent to prevent it.

**Points:** 5

**Rubric (1 point each):**

1. Explains that colour images are stored in sRGB (steps spaced for human vision) and must be decoded to linear before lighting math, while data images store the numbers themselves and must be read as they are.
2. Classifies correctly: albedo and emission colour are colour (sRGB); normal map, roughness and ambient occlusion are data (linear).
3. Predicts the look of two wrong-flag mistakes and gives at least one number, for example a roughness value 0.50 decoded as sRGB becomes about 0.22 so the surface looks too glossy, a normal map decoded as sRGB tilts a flat surface by tens of degrees, or an albedo read as linear looks washed out and too bright.
4. Explains why the mistake is hard to notice: nothing fails or warns, the material still renders, and the result looks plausible but wrong in a way that depends on lighting.
5. Gives the instruction: say explicitly which maps are colour and which are data, ask the agent to set and report the colour-space import flag of each, and check the result under controlled lighting.

**Source:** Colour textures versus data textures

## ES-ch07.5

A mobile 3D game has a long cobblestone road. Players see the road shimmer in the distance, and the game runs out of video memory on low-end phones. The scene uses 40 textures of 2048 × 2048 texels in RGBA8 (4 bytes per texel, 16 MiB each at the base level). Explain what mipmaps, texture filtering and texture compression are, and which of them address which problem. Calculate the memory before and after your proposed settings (a mip chain adds a third; assume a block-compressed format at 8 bits per texel), and state one cost of each choice.

**Points:** 5

**Rubric (1 point each):**

1. Defines the three terms: mipmaps (a chain of pre-averaged half-size copies of a texture), texture filtering (how a value is computed between texels or over many texels: nearest, bilinear, trilinear, anisotropic) and block compression (a GPU format that stays compressed in video memory, unlike PNG or JPEG file size on disk).
2. Says which addresses which problem: the shimmer is minification aliasing (many texels per pixel in the distance), fixed by mipmaps with trilinear or anisotropic filtering, while the video-memory problem is addressed by compression, and mipmaps by themselves add memory.
3. Calculates the memory before: 40 × 16 MiB = 640 MiB at the base level (accepted as the starting figure, since a shimmering scene probably has no mipmaps yet), and about 853 MiB once full mip chains are added (one third more).
4. Calculates the memory after compression: 4 MiB per texture, 160 MiB for the 40 at the base level, about 213 MiB with mip chains.
5. States one cost per choice: mipmaps add about 33 percent memory, block compression is lossy (banding, artefacts, special handling for normal maps), and anisotropic filtering costs extra sampling time.

**Source:** Mipmaps, filtering and compression

## ES-ch07.6

A game has 40 enemies that share one mesh and one shader. The designer wants four colour variants, and a hit flash that affects only the enemy that was just hit. A coding agent was told: "Make a red version of the enemy material and flash the hit enemy." Define shader, material, texture and material instance. Design how the four variants and the single-enemy flash should be built, explain what happens if the agent edits the shared material, and map the idea to at least two engines.

**Points:** 5

**Rubric (1 point each):**

1. Defines shader (the program), material (a shader plus parameter values and texture bindings assigned to a mesh), texture (image data a material reads) and material instance (a variant of a material that overrides parameters without a new shader program); the point is earned when at least three of the four definitions are correct.
2. Designs the variants as four materials or instances that share the one shader (and textures where possible), differing only in parameters such as tint.
3. Designs the hit flash as a per-object change: a per-object copy or dynamic instance, or a per-instance parameter, so only the hit enemy changes.
4. Explains the failure of the vague instruction: editing the shared material changes all 40 enemies at once because they all reference the same resource.
5. Maps the idea of a shared material versus a per-object copy, instance or parameter to at least two engines (for example Unity's shared versus per-renderer material, Unreal's constant versus dynamic material instances, Godot's duplicated material or per-instance shader uniform); exact API names are not required.

**Source:** Material instances

## ES-ch07.7

A level has a 20 m × 20 m concrete floor and 30 small props (crates, barrels, signs), each with its own small texture. A developer tells a coding agent: "make the floor texture bigger and put all the prop textures together." Explain tiling, UV scale, texel density and seamless textures, and why "bigger" is ambiguous. Explain what a texture atlas is, what it gains, and two things that go wrong when textures are packed into one. Calculate the texel density for a 1024-texel texture stretched once across the floor and for the same texture repeated 10 times across it.

**Points:** 5

**Rubric (1 point each):**

1. Explains tiling as repeating a seamless texture across a surface by scaling the UVs with a repeat wrap mode, and why a non-seamless texture shows joins.
2. Explains that "bigger" is ambiguous: bigger features (fewer repeats), a larger-resolution texture, or more repeats, each with a different effect on look and memory.
3. Calculates texel density correctly: 1024 texels over 20 m is about 51 texels per metre (blurry), and 10 repeats give 10,240 texels over 20 m, which is 512 per metre, at the cost of visible repetition.
4. Defines a texture atlas as many images packed into one texture with each mesh's UVs addressing its own region, so the props can share one material and reduce state changes and draw calls.
5. Names two problems of atlases: filtering and mipmaps bleed colour between neighbouring regions unless padded, and hardware repeat cannot tile a sub-region of an atlas; also acceptable are wasted space or the need to remap every prop's UVs.

**Source:** Tiling, UV scale and atlases

## ES-ch07.8

A developer reports to a coding agent: "The metal shield material is pure black, the crevice ambient occlusion has no effect, and the glowing crystal does not light the cave wall. The textures must be broken, so regenerate them." The scene has one directional light, no environment lighting or reflection source, and the ambient light is set to zero. Critique this diagnosis. Explain what each symptom really says about metal, ambient occlusion and emission, and describe the instruction and test you would give the agent instead.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a metal has no diffuse colour and shows only reflections, so with nothing to reflect (no environment or reflection probe) it looks black apart from the highlight of the light, which is a lighting problem and not a texture problem.
2. Explains that ambient occlusion by default affects only ambient light, so with ambient at zero and a strong direct light there is nothing for it to darken; it needs ambient or environment light, or a setting that lets it affect direct light, or a separate screen-space effect.
3. Explains that emission only makes the emissive surface itself glow, and that lighting the cave wall needs an actual light or a global-illumination technique that treats emissive surfaces as sources.
4. States the general principle that physically based materials are judged under stated lighting, so the same textures can look right or wrong depending on the scene.
5. Proposes a better instruction and test: place the material in a neutral lit environment (for example an environment map or reflection probe), compare it with the current scene, and regenerate textures only if they are still wrong.

**Source:** Materials under lighting
