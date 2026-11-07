# Chapter 3: 3D assets and the Blender pipeline

## ES-ch03.1

A developer tells a coding agent: 'Make me a barrel in Blender and put it in my game so the player can bump into it.' Rewrite this as a precise instruction using the correct terms, and explain what could come back wrong from the original wording.

**Points:** 5

**Rubric (1 point each):**

1. Gives the size in metres and the up axis (for example a stated height and width, with +Y up in the engine), so scale and orientation are not guessed.
2. Specifies the origin or pivot location (for example the centre of the base so the barrel stands on the floor at y = 0) and that scale and rotation are applied before export.
3. States a triangle budget, the material count and names, and the export format (for example .glb) with the settings that matter.
4. Specifies the collision: a simple separate shape (primitive or convex) with its size, and says whether the barrel is static or moving, rather than 'collision' in general.
5. Lists concrete failures of the original wording, such as the wrong size, lying on its side, sinking into the floor or an expensive or missing collider.

**Source:** Say it to the agent: prop request rewrite

## ES-ch03.2

A model looks right in the modelling tool but arrives in Godot too large, lying on its side, rotating about the wrong point, or carrying an odd scale. Explain, using the terms units, up axis, origin (pivot) and applying transforms, what can cause each symptom and what number you would check to confirm each cause. Also say why looking at the model on screen is not enough to catch these problems.

**Points:** 5

**Rubric (1 point each):**

1. Too large or too small: the engine reads 1 unit as 1 metre while the model was built in other units; checks the bounding box size in metres against the intended size.
2. Lying on its side: the modelling tool's up axis (Z) differs from the engine's (Y) and the export did not convert; checks which axis carries the height in the imported bounding box.
3. Odd scale: the object's scale was never applied, so the mesh data is a different size from what it looks like and the node carries a non-unit scale; checks the node scale is (1, 1, 1) and the mesh size is correct.
4. Rotating about the wrong point: the origin is not where the use needs it, such as at a hinge; checks the hinge position relative to the origin.
5. Explains why a model can look right on screen while one of these numbers is wrong, so the numbers must be measured and not only looked at.

**Source:** Why imported models arrive wrong

## ES-ch03.3

A level in a Godot project contains a stone archway the player walks through, a rock the player cannot move, and a crate the player can push. For each, choose a collision shape and justify it using the terms convex, concave (trimesh), primitive shape, static body and moving body. Explain what goes wrong if the agent is simply told to 'use the mesh as collision'.

**Points:** 5

**Rubric (1 point each):**

1. Defines convex (no dents or holes; every line between two inside points stays inside) and concave or trimesh (follows the mesh triangles exactly), and primitive shapes such as box, sphere and capsule.
2. Chooses a concave or several convex pieces for the archway so the opening stays passable, noting a single convex hull would fill the opening and block the player.
3. Chooses a shape for the immovable rock with a stated reason: a concave shape is acceptable because the body is static, though a convex hull or a primitive is cheaper and equally adequate; and notes that in Godot concave shapes are usable only on static bodies and are the slowest option.
4. Chooses a primitive or convex shape for the pushable crate, since a moving body cannot use a trimesh in Godot and simple shapes are cheaper.
5. Explains what 'use the mesh as collision' risks: an expensive trimesh on a moving body that the engine may not support or that wastes processing, a hull that blocks the archway, or fussy detail that catches the player, and that collision geometry is a separate, simpler design choice from the visual mesh.

**Source:** Collision shape choice

## ES-ch03.4

A coding agent can drive Blender in two ways: through an MCP server connected to an open Blender window, or by writing a Python script that uses bpy and running Blender without a window. Explain what an MCP server lets an agent do, compare the two approaches, and say which you would choose for making a prop that must be regenerated later and why. Include one safety concern.

**Points:** 5

**Rubric (1 point each):**

1. Explains that an MCP server exposes tools the agent can discover and call, with the server relaying calls to the target application and returning results, while the model itself stays outside.
2. Explains that bpy is Blender's Python API and that a script run in background mode builds and exports an asset with no window.
3. Compares them: MCP suits exploring a scene or one-off fixes and leaves a transcript of calls, while a script is a file that can be reviewed, diffed and rerun to regenerate the asset.
4. Chooses the script for a prop that must be regenerated, because the recipe is a file that can be rerun to give the same asset.
5. Names a safety concern, such as tools that run generated code in Blender without guards, a connection that anyone who can reach it can use, or remote generation services that cost money, and says to keep it local and approved.

**Source:** MCP versus scripting Blender

## ES-ch03.5

A scene has 50 trees, each a 12,000-triangle mesh with two materials. Explain the parts of a mesh (vertex, edge, face, triangle), how triangle count is worked out, why the vertex count a profiler reports can be higher than the count in the modelling tool, and how level of detail (LOD) and fewer materials reduce cost. Give the arithmetic for one example.

**Points:** 5

**Rubric (1 point each):**

1. Defines vertex (point), edge (line between two vertices) and face (surface bounded by edges), and says GPUs draw triangles, with an n-sided face giving n - 2 triangles.
2. Works out a triangle count correctly for an example, such as a box having 6 quads and so 12 triangles, or the 50 trees totalling 600,000 triangles.
3. Explains that vertices are duplicated on the GPU where normals or UVs differ, as at a hard edge or UV seam, so a cube's 8 vertices can appear as 24.
4. Explains LOD as several versions of decreasing triangle counts chosen by distance, so far objects cost fewer triangles; a second calculation is not required, but one such as 40 distant trees at 1,500 triangles costing 60,000 instead of 480,000 earns the point.
5. Explains that each additional material typically adds at least one draw call, so merging materials where the look allows it reduces draw calls even when triangle count is unchanged.

**Source:** Mesh cost, LOD and materials

## ES-ch03.6

Three symptoms appear on imported models: some faces are black or invisible from outside; a texture looks stretched or is missing; and one object has far more draw calls than expected. Explain, using the terms normals, UV map and material slot, what each term means, which symptom each most likely causes, and how you would phrase the fix to a coding agent.

**Points:** 5

**Rubric (1 point each):**

1. Defines normals as direction vectors perpendicular to the surface used for lighting and culling, and links black or vanishing faces to inward-pointing normals.
2. Phrases the fix for normals precisely, for example 'recalculate the normals so they point outward', rather than 'fix the shading'.
3. Defines a UV map as the per-vertex 2D coordinates linking surface to image, and links missing or stretched textures to absent or poorly laid-out UVs, fixed by unwrapping.
4. Defines a material slot as a position holding a material to which faces are assigned, and links many draw calls to many slots or materials on one object.
5. Gives a precise fix phrase for the slot problem (for example reduce the object to a stated number of materials, merging slots that share a look).

**Source:** Diagnosing normals, UVs and material slots

## ES-ch03.7

An agent reports that an exported prop 'looks right'. Design a short list of measurements, taken after import into the engine and run headless, that would check the prop is the intended size, orientation, scale, pivot, materials and collision. For each check say what number you read and what failure it would catch, then say what a headless check cannot establish.

**Points:** 5

**Rubric (1 point each):**

1. Checks size and orientation by reading the bounding box in metres and comparing it with the intended extents, catching wrong units or a prop lying on its side.
2. Checks scale by confirming the node scale is (1, 1, 1) and the mesh itself has the right size, catching unapplied transforms.
3. Checks the pivot by reading the lowest point relative to the origin (for example zero at the base), catching a prop that sinks or floats.
4. Checks materials by listing the material names or count on the imported surfaces, and collision by reading the shape type and size and confirming it is simple and sits where expected.
5. States what remains for a person: how it looks under the game's lighting, whether it reads as intended, whether the collider feels fair, and anything in the render that numbers cannot show.

**Source:** Verifying an asset by measuring
