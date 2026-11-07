# Chapter 3: 3D assets and the Blender pipeline

## MA-ch03.1

A modeller makes a simple box in a 3D tool: 8 corner points, 12 straight lines joining them and 6 flat four-sided surfaces. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 8 points are vertices, the 12 lines are edges and the 6 surfaces are faces.
- [ ] B. A five-sided face is split into 3 triangles for drawing.
- [ ] C. A face is the same thing as a vertex that carries a position and a colour.
- [ ] D. Each four-sided face is drawn as two triangles, so the box has 12 triangles.
- [ ] E. The box has 6 triangles because it has 6 faces.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: These are the three basic parts of a polygon mesh.
- B: An n-sided face triangulates into n - 2 triangles, and 5 - 2 = 3.
- C: A vertex is a point; a face is a surface bounded by edges between vertices.
- D: GPUs draw triangles; a quad is split into two, and 6 x 2 = 12.
- E: Each quad face becomes two triangles, so the box has 12.

**Source:** Mesh anatomy

## MA-ch03.2

A low-poly post is an eight-sided cylinder: 8 rectangular side faces plus a single eight-sided face at each end, with no extra cuts. Triangulation splits an n-sided face into n - 2 triangles. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Removing both end caps leaves 8 triangles.
- [ ] B. The post has 24 triangles in total.
- [ ] C. The two eight-sided end caps give 12 triangles between them.
- [ ] D. Triangle count has no effect on performance, because GPUs process faces rather than triangles.
- [ ] E. The 8 side faces give 16 triangles between them.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The 8 side faces still give 16 triangles.
- B: 16 + 12 = 28.
- C: Each cap is 8 - 2 = 6 triangles, so two caps give 12.
- D: GPUs draw triangles, and more of them means more vertex and rasterisation work.
- E: Each rectangle is two triangles, and 8 x 2 = 16.

**Source:** Triangle count

## MA-ch03.3

An interviewer says: 'My modelling tool reports 8 vertices for a hard-edged cube, yet the engine's profiler reports 24 vertices for the same cube.' Check each statement that is true as an explanation. Each statement is worth 1 point (5 points total).

- [ ] A. The profiler must be wrong, because a cube has 8 vertices and engines do not add more.
- [ ] B. The 24 vertices mean the cube has 24 faces, each drawn separately by the engine.
- [ ] C. A vertex is also split where adjacent faces have different UV coordinates, such as along a UV seam.
- [ ] D. A smooth mesh whose faces share normals and UVs at a corner can share one vertex there.
- [ ] E. Three faces meet at each corner with different normals, so the GPU keeps a vertex per face: 8 x 3 = 24.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: 8 is the count of corner positions; GPU vertex data duplicates them when attributes differ.
- B: The cube still has 6 faces; the extra vertices come from duplicated corners.
- C: Different UVs at the same position require separate GPU vertices.
- D: Shared attributes allow shared vertices.
- E: A GPU vertex bundles position, normal and UV, so a corner with three normals needs three vertices.

**Source:** Vertex count in the tool versus on the GPU

## MA-ch03.4

An imported crate has several faces that look black or vanish when viewed from outside. Another crate looks flat although a normal map texture is assigned to it. The developer must name each problem correctly to a coding agent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A normal map is a texture of per-texel directions that fakes fine detail; it is not the mesh's own normals.
- [ ] B. Recalculating normals to point outward repairs inside-out faces and adds no surface detail from any texture.
- [ ] C. 'Fix the normals' and 'fix the normal map' are the same instruction, because a normal map is the mesh's own normals saved as an image.
- [ ] D. A normal is a direction perpendicular to a surface, used for lighting; inward-pointing normals can make faces dark or culled.
- [ ] E. Applying a normal map adds real triangles and vertices to the mesh, which is why the surface looks bumpy.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The mesh normals are geometry data; the normal map is image data.
- B: It corrects direction only; detail from a texture is a separate matter.
- C: One recalculates face directions on the mesh, the other repairs or replaces a texture.
- D: Lighting and culling depend on which way the face points.
- E: A normal map changes lighting per pixel and leaves the geometry unchanged.

**Source:** Normals versus normal maps

## MA-ch03.5

A coding agent builds a crate mesh and a wood texture. In the engine the texture is missing on one object that was created without unwrapping, and the wood grain looks stretched on another. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A mesh with no UV map still shows an image texture correctly, because the engine computes coordinates from the vertex positions.
- [ ] B. UV coordinates are stored inside the texture image file, next to the pixels they refer to.
- [ ] C. Stretched wood grain proves the texture image itself has too low a resolution, so a larger file is needed.
- [ ] D. Unwrapping paints the texture image onto the model; the 2D layout it produces is a by-product that can be ignored.
- [ ] E. A UV map gives each vertex a 2D (u, v) coordinate in the texture, saying which part of the image lands where on the surface.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Without UVs the renderer has no mapping from surface to image.
- B: They are stored on the mesh, as a per-vertex attribute.
- C: Stretching comes from a mismatch between UV layout and surface shape, not from the image's pixel count.
- D: Unwrapping produces the 2D layout (the UV map) itself; painting or choosing the image is a separate step.
- E: UVs are the link between a 3D surface and a 2D image.

**Source:** UV maps

## MA-ch03.6

A modeller creates a post with a metal pole and a red cloth pennant. The object has two material slots, one holding a metal material and one holding a cloth material, and every face is assigned to one of the slots. The model is exported to glTF and imported into an engine. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Renaming a slot changes nothing about how its faces look; the material it holds decides that.
- [ ] B. A material slot is a numbered position on an object that holds a material; each face uses one slot.
- [ ] C. Each extra material typically adds at least one draw call, so ten cost more to draw than one.
- [ ] D. After import, the metal and cloth faces typically become separate surfaces with their own materials.
- [ ] E. A texture and a material are the same thing, since a material is an image applied to faces.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: A slot name is a label.
- B: Faces point at slots, and slots point at materials.
- C: Surfaces with different materials generally cannot be drawn in a single call.
- D: glTF keeps one primitive per material, and engines import them as separate surfaces.
- E: A material defines how a surface is shaded and may use textures as inputs.

**Source:** Material slots

## MA-ch03.7

A developer asks a coding agent for 'a door' model. When the door is placed in a level and rotated by script, it swings about its middle instead of its edge. A crate model, 1 m tall, that the agent also built sinks halfway into the floor when placed at floor height, y = 0. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The crate sinks because its origin is at its centre: at y = 0, half of its 1 m height is below the floor.
- [ ] B. 'Make a door' already specifies where the origin goes, so the agent will place it at the hinge.
- [ ] C. The origin (pivot) is the point an object's position and rotation refer to; a swinging door needs it on the hinge edge.
- [ ] D. Moving an object's origin to a new point moves its visible geometry along with it, since the two are one thing.
- [ ] E. A door whose origin is at its centre will swing about its hinge once the script rotates the node by 90 degrees.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A 1 m crate centred on the origin extends 0.5 m below it.
- B: The phrase names the object, not its pivot, so the agent can choose any origin.
- C: Rotation happens about the origin.
- D: Tools can reposition the origin while the geometry stays where it is.
- E: Rotation about the centre keeps the centre fixed; it cannot make a door swing about its edge, whatever the angle.

**Source:** Say it to the agent: origin and pivot

## MA-ch03.8

An engine treats 1 unit as 1 metre, and its player character is 1.8 units tall. A modeller who was thinking in centimetres builds a tree 540 units tall, and the file is exported and imported with no conversion. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The quickest correct fix is to make the player character 300 times taller so the proportions match.
- [ ] B. Scaling the tree node to 0.01 in the engine is as good as fixing the mesh, because collision and physics ignore node scale.
- [ ] C. glTF stores distances in centimetres, so the engine converts the tree down on import.
- [ ] D. Units are only labels, so physics settings such as gravity behave the same for large and small models alike.
- [ ] E. The tree appears 540 m tall in the engine, which is 300 times the player's height of 1.8 m.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: That would break every other object sized in metres.
- B: Scaled nodes carry their scale into collision and anything built from them, which engines advise avoiding.
- C: glTF specifies metres for all linear distances, so nothing is converted.
- D: Physics is tuned for metre-scale objects, so wrongly sized objects behave wrongly.
- E: 540 / 1.8 = 300, and 1 unit is 1 m.

**Source:** Scale and units

## MA-ch03.9

In a modelling tool, a modeller adds a cube whose mesh is 2 m on each side and scales the object to (0.1, 0.1, 0.9) to make a pole that looks 0.2 x 0.2 x 1.8 m. The object is exported without applying transforms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Applying transforms can only be done on the engine side, because exporters cannot bake them.
- [ ] B. The mesh data still describes a 2 m cube; only the object's scale makes it look like a pole.
- [ ] C. After applying the scale, the object's scale is (1, 1, 1) and the vertices themselves are 0.2 x 0.2 x 1.8 m apart.
- [ ] D. In the engine the node carries a non-unit scale, which anything built from it, such as a collider, inherits.
- [ ] E. Applying the scale changes how the pole looks in the viewport, since the vertices move.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The step belongs in the modelling tool before export.
- B: Scale lives on the object and the vertices are unchanged.
- C: Apply bakes the object's scale into the vertex positions.
- D: The exporter writes the object scale onto the node.
- E: Apply keeps the appearance identical and changes only where the numbers are stored.

**Source:** Applying transforms

## MA-ch03.10

A modelling tool treats +Z as up, while glTF and Godot treat +Y as up. A person 1.8 m tall is modelled standing along Z. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With the exporter's up-axis conversion on, the 1.8 m height arrives along Y.
- [ ] B. Unreal Engine's editor is also Y-up, so no conversion is needed for it.
- [ ] C. Rotating each imported node by 90 degrees in the level scripts fixes the orientation at the source, so any other tool that opens the asset will also see it upright.
- [ ] D. Up axis and handedness are the same property, so fixing one fixes the other.
- [ ] E. If the exporter does no axis conversion, the person arrives lying on their side in Godot, with the 1.8 m extent along Z.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The conversion maps the tool's Z extent onto Y.
- B: Epic's documentation says the Unreal Editor uses a Z-up axis.
- C: The node rotation only hides the problem on that instance: it must be repeated wherever the model is used, and the asset's own axes, pivot and child nodes stay in the wrong frame.
- D: Handedness describes how the axes are arranged (right- or left-handed); the up axis is a separate choice.
- E: The height stays on the Z axis, which is not up in Godot.

**Source:** Up axis and handedness

## MA-ch03.11

A developer asks a coding agent to 'export the model for the engine'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. glTF 2.0 is an open interchange format: .glb is one binary file, while .gltf is a text description plus separate data files.
- [ ] B. A single glTF 2.0 asset can describe meshes, materials, textures, a skeleton and animations together, which is why it suits rigged and textured props.
- [ ] C. 'Export the model for the engine' already fixes format, up axis, scale and what to include.
- [ ] D. The OBJ format carries skeletal skinning and animation as well as geometry, which is why studios favour it.
- [ ] E. glTF carries a modelling tool's custom shader node graphs into the engine unchanged, so the looks match.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: GLB is the single-file form and glTF the text-plus-files form.
- B: glTF's scene description covers geometry, materials, textures, skins and animations, so one export can carry a whole prop.
- C: The phrase names none of them, so each is left to the agent's defaults.
- D: Godot's documentation says OBJ does not support skinning, animation, UV2 or PBR materials.
- E: glTF carries a metallic-roughness material model; tool-specific node graphs do not cross.

**Source:** glTF and GLB

## MA-ch03.12

A level contains a stone archway the player must walk through and a loose boulder the player can push. The developer asks a coding agent to give both 'accurate mesh collision'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Concave shapes are the most accurate and also the cheapest for the physics engine to process.
- [ ] B. In Godot, concave shapes are only usable on static bodies, so a pushable boulder needs a convex or primitive shape.
- [ ] C. A concave (trimesh) shape can follow the arch's opening, so the player can walk through it.
- [ ] D. A convex hull of the archway is the smallest convex shape around it, so it fills the opening and blocks the player.
- [ ] E. A roughly round boulder is usually well served by a primitive sphere or a convex hull, which cost less than a trimesh.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Godot's documentation calls them the slowest option.
- B: Godot's documentation says concave shapes work within static bodies only.
- C: Concave shapes follow the mesh's triangles exactly.
- D: A convex shape cannot have a hole or dent, so the opening disappears.
- E: Simple shapes are cheaper and adequate for a nearly convex object.

**Source:** Convex versus concave collision

## MA-ch03.13

A character model has 30,000 triangles, including a cape, a sword and a hat plume. A developer tells a coding agent: 'use the model's mesh as its collider'. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Godot, a trimesh collider is a poor fit for a moving character: concave shapes are slow and work only on static bodies.
- [ ] B. A collider should match the visible silhouette, so the cape and sword block the player as they look.
- [ ] C. A collider is sized from what should feel solid, such as a capsule around the body, even if the cape extends outside it.
- [ ] D. 'A capsule collider 0.4 m in radius and 1.8 m tall' is more precise because it states shape and size.
- [ ] E. The collision shape is a separate thing from the visible mesh and may be far simpler than it.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Godot's documentation restricts concave shapes to static bodies and calls them the slowest.
- B: Matching every protrusion makes the character catch on scenery and costs more.
- C: Collision is about gameplay fairness, not the visible outline.
- D: It names the shape and its dimensions, removing the guess.
- E: Collision geometry is authored or chosen separately from the visual mesh, and simple shapes are the norm.

**Source:** Collider is not the visual mesh

## MA-ch03.14

A scene shows 50 identical trees of 12,000 triangles each (600,000 triangles in all). Up close the detail matters; far away the trees are small on the screen. A developer asks a coding agent to add levels of detail (LOD), with a 1,500-triangle version for distant trees. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If 40 trees are far enough to use the 1,500-triangle version, they cost 60,000 triangles instead of 480,000.
- [ ] B. LOD keeps several versions of a mesh with decreasing triangle counts; the engine picks one by distance or screen size.
- [ ] C. The lower-detail meshes are free: they add nothing to the project's storage or load time.
- [ ] D. Switching between LOD versions is not noticeable to the player, because the versions are built to match.
- [ ] E. LOD cuts the triangles processed per tree but does not by itself reduce the number of trees drawn.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: 40 x 1,500 = 60,000 and 40 x 12,000 = 480,000.
- B: That is the definition of level of detail.
- C: Each extra version is more data that has to be stored and loaded.
- D: A visible pop can occur when the engine switches versions.
- E: Each visible tree is still drawn once, just with a smaller mesh.

**Source:** Level of detail

## MA-ch03.15

A developer wants a coding agent to produce a crate model reproducibly. The agent writes a Python file that uses Blender's built-in Python API, bpy, and runs Blender with no window (background mode) to execute it as one step of an automated build. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An automated build step can judge whether the script step succeeded from the error text in the log; the process's exit status adds nothing to that.
- [ ] B. If the script finishes without an error, the exported model is correct, since the script produced it.
- [ ] C. bpy is Blender's Python interface, so a script can build, modify and export scenes without anyone clicking.
- [ ] D. A script can be reviewed, diffed and rerun to regenerate the asset; live clicks leave no such record.
- [ ] E. Background mode means the script cannot read the mesh or write files, because there is no window.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The log text and the process's exit status are two separate signals; an automated step reads the exit status as its machine-checkable verdict, and a program can print an error and still exit with status 0, so the status has to be checked as well.
- B: A script can run cleanly and still encode a wrong assumption about size, axes or scale.
- C: Scripts call the same operations the interface does.
- D: A script is a reproducible, reviewable recipe.
- E: Background mode runs the same data operations and exports without an interface.

**Source:** Scripting Blender with bpy

## MA-ch03.16

A developer connects a coding agent to Blender through an MCP server and a Blender add-on, so the agent can act on a Blender window that is open. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A conversation of MCP tool calls is as easy to regenerate and review as a script file, since each call is logged.
- [ ] B. The server relays tool calls to Blender, which carries them out and returns results; the model does not run inside Blender.
- [ ] C. MCP gives the agent modelling skill that the underlying model did not already have, by teaching it Blender.
- [ ] D. MCP is a standard way for an agent to discover and call tools that a separate program exposes.
- [ ] E. An unguarded run-code tool lets anything that reaches the connection run code as the user, so keep it local and trusted.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Live tool calls leave a transcript, while a script is a single artifact that can be diffed and rerun.
- B: The model stays in the agent; Blender executes the requested actions.
- C: MCP supplies access to actions and results, not new capability in the model.
- D: MCP defines how tools are listed and invoked.
- E: Executing generated code without checks is a real exposure.

**Source:** What an MCP server lets an agent do

## MA-ch03.17

An agent reports that an exported prop 'looks right'. The developer wants numbers a headless test can check after the model is imported into the engine. The prop should be 0.2 x 1.8 x 0.2 m (width, height, depth, with Y up), sit on the floor when placed at y = 0, be at unit scale, and have two materials named PostMetal and PennantRed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The lowest point of the mesh should sit at y = 0 relative to the node when the origin was set at the base.
- [ ] B. The node's scale should be (1, 1, 1); a 2 m cube wearing scale (0.1, 0.9, 0.1) would look right yet fail.
- [ ] C. The mesh's bounding box should measure (0.2, 1.8, 0.2) m; (0.2, 0.2, 1.8) would mean it lies on its side.
- [ ] D. Passing all of these checks shows the prop looks good under the game's lighting and reads as a post.
- [ ] E. The names of the imported surfaces' materials can be listed and compared with the two expected names.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: That is what makes the prop stand on the floor when placed at y = 0.
- B: Looking right and carrying the right numbers are different things.
- C: The extents reveal which axis the height ended up on.
- D: These checks measure geometry and names; appearance needs a person looking at a render.
- E: Material names cross in glTF and can be asserted.

**Source:** Verifying an asset by measuring

## MA-ch03.18

A developer needs a crate and compares several requests to a coding agent. Check each statement that is true about how clearly the request specifies the asset. Each statement is worth 1 point (5 points total).

- [ ] A. 'Make the crate about the right size' is as precise as the full request, because the engine works in metres.
- [ ] B. 'Low-poly crate, 1 x 1 x 1 m, origin at base centre, under 200 triangles, scale applied, one material, .glb, +Y up' settles what the agent would guess.
- [ ] C. 'Export it with the usual settings' is precise, since exporters share the same defaults for axes, scale and included data.
- [ ] D. 'Keep the triangle count under 200' is checkable by reading the exported mesh's triangle count.
- [ ] E. 'Add a collision shape' is enough, because the agent will pick a cheap convex or primitive shape.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The phrase gives no number, so the engine's units do not settle the size.
- B: Each phrase removes a decision the agent would otherwise make.
- C: Defaults differ between tools and versions, so the phrase leaves them open.
- D: It names a number that a test can read.
- E: It could just as well add an expensive trimesh or none that suits.

**Source:** Say it to the agent: a precise asset request

## MA-ch03.19

A developer moves between engines and wants the collision vocabulary straight. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. In Unreal, simple collision uses primitives and convex hulls, while complex collision is the object's per-triangle trimesh.
- [ ] B. An Unreal object that must be physically simulated should use complex collision so that it matches its visible shape exactly.
- [ ] C. Unreal's simple collision corresponds roughly to primitive or convex shapes, and complex to concave (trimesh).
- [ ] D. In Unreal, the simple and complex collision of an object are the same shape, because both are taken from the visible mesh.
- [ ] E. In Unreal and in Godot alike, exact per-triangle collision is the costly kind and primitives or convex hulls are the cheap kind.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: This is how Epic's documentation divides the two.
- B: Simulated bodies rely on simple collision shapes (primitives or convex hulls), not on the exact triangle mesh.
- C: The mapping holds: shapes without dents versus the exact triangle mesh.
- D: Simple collision is made of primitives or convex hulls, while complex collision is the per-triangle mesh; they usually differ.
- E: Testing against every triangle costs more than testing against a primitive or hull; Godot's documentation calls concave shapes the slowest option, and Unreal pairs cheap simple shapes with the exact complex mesh.

**Source:** Collision vocabulary across engines
