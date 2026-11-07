# Chapter 13: Profiling and optimization

## MA-ch13.1

A team reports performance in frames per second, but the engineers work in frame time, where frame time in milliseconds is 1000 divided by FPS. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A drop from 60 FPS to 50 FPS costs about 3.3 ms of extra time on each frame.
- [ ] B. A drop of 5 FPS, from 30 to 25, costs about 6.7 ms per frame, more than the 3.3 ms lost going from 60 to 50.
- [ ] C. Equal drops in FPS, such as 5 FPS starting from 60 or from 30, correspond to equal increases in frame time.
- [ ] D. A 60 Hz target leaves a budget of about 16.7 ms for all the work in a frame.
- [ ] E. A 144 Hz display target leaves a budget of about 14.4 ms, the refresh rate divided by ten.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: 1000/50 = 20.0 ms against 1000/60 = 16.7 ms, a difference of about 3.3 ms.
- B: 1000/25 = 40.0 ms against 1000/30 = 33.3 ms, a difference of about 6.7 ms, even though the FPS drop is smaller.
- C: FPS is the reciprocal of frame time, so the same FPS loss costs more milliseconds at low frame rates than at high ones.
- D: 1000/60 is about 16.7 ms, the time available to finish everything.
- E: 1000/144 is about 6.9 ms; 14.4 ms would correspond to roughly 69 FPS.

**Source:** Frame time versus FPS

## MA-ch13.2

In a capture of 100 consecutive frames, 98 frames took 10 ms and 2 frames took 50 ms. The game targets 60 Hz, a budget of 16.7 ms per frame. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The mean frame time of the capture is 10.8 ms, well under the 16.7 ms budget.
- [ ] B. The 99th percentile frame time is 50 ms, so it exposes the hitches that the mean hides.
- [ ] C. Because the mean of 10.8 ms is under the 16.7 ms budget, the game will feel smooth.
- [ ] D. Each of the two slow frames overshoots the 60 Hz budget by about 33 ms.
- [ ] E. Removing the two slow frames from the capture would raise the mean frame time above 11 ms.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: (98 x 10 + 2 x 50) / 100 = 10.8 ms.
- B: Sorted, the 99th and 100th values are 50 ms, so the 99th percentile catches the stutters while the mean (10.8) and the 95th percentile (10) do not.
- C: An average can sit well under budget while individual frames miss it, and players see the misses as stutter.
- D: 50 ms minus the 16.7 ms budget is about 33 ms of overshoot per slow frame.
- E: Without the slow frames every remaining frame is 10 ms, so the mean falls to 10.0 ms.

**Source:** Frame time distribution, mean versus worst frame

## MA-ch13.3

A game runs at 22 ms per frame on a target phone, with vertical sync off. The developer lowers the render resolution to half the width and half the height (a quarter of the pixels) and frame time stays at 22 ms. Then the developer halves the number of AI-controlled characters and frame time drops to 15 ms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The first result suggests the frame is CPU-bound rather than limited by pixel work on the GPU.
- [ ] B. The first result shows that fill rate is the bottleneck, since the frame time did not change when the pixel count did.
- [ ] C. If pixel work on the GPU limited the frame, lowering the resolution should have shortened it.
- [ ] D. Because resolution had no effect, it proves that draw calls are not a problem.
- [ ] E. The drop to 15 ms proves that AI code is the only cost in the frame and nothing else needs attention.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Changing pixel count did nothing, so the time is being spent elsewhere, most likely on the CPU side.
- B: Fill-rate limits would have improved when the pixel count fell by 75 percent.
- C: Resolution is the standard experiment for separating pixel-bound GPU work from CPU work.
- D: Draw-call overhead is CPU work and does not change with resolution, so the experiment cannot rule it out.
- E: A 7 ms saving shows AI is a large part of the frame, not that nothing else costs time.

**Source:** CPU-bound versus GPU-bound

## MA-ch13.4

In a renderer where the main thread, the render thread and the GPU work as a pipeline, a frame takes about as long as the slowest of the three. Per-frame times are: main thread 14 ms, render thread 6 ms, GPU 9 ms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Frame time is about 14 ms, roughly 71 FPS.
- [ ] B. Cutting GPU time from 9 ms to 4.5 ms leaves frame time at about 14 ms.
- [ ] C. Cutting main-thread time by 4 ms, to 10 ms, brings frame time to about 10 ms, roughly 100 FPS.
- [ ] D. Cutting render-thread time from 6 ms to 3 ms brings frame time to about 11 ms.
- [ ] E. Because the three stages add up to 29 ms, the game runs at about 34 FPS.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The slowest stage, the main thread at 14 ms, sets the pace, and 1000/14 is about 71 FPS.
- B: The GPU was not the longest stage, so speeding it up changes nothing while the main thread is the bottleneck.
- C: With the main thread at 10 ms the slowest stage becomes the GPU at 9 ms, so the frame takes max(10, 6, 9) = 10 ms.
- D: The render thread is not the slowest stage, so cutting it leaves the frame at 14 ms.
- E: In a pipeline the stages overlap in time, so frame time is the longest stage and not their sum.

**Source:** Bottleneck and pipelined frame time

## MA-ch13.5

A scene has 1,000 small props, each drawn with its own draw call, and the frame is slow on the CPU. Another scene has one mesh of 1,000,000 triangles drawn with a single draw call and runs fast. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A draw call is a command from the CPU to the GPU to draw some geometry using a particular set of state, such as a mesh and a material.
- [ ] B. Each draw call carries CPU overhead, so many small draw calls can cost more CPU time than one large one with more triangles.
- [ ] C. The slow scene must contain more triangles in total, since the number of triangles is what mostly determines how long the CPU takes to prepare a frame.
- [ ] D. Merging draw calls reduces GPU shading cost in proportion, because the GPU then has fewer commands to process.
- [ ] E. Draw-call overhead comes from the GPU hardware, so a call costs about the same whichever graphics API or engine submits it.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A draw call is how the CPU submits a batch of geometry plus the state needed to draw it.
- B: Validation and state changes make each call cost CPU time, which is why call count matters apart from triangle count.
- C: The slow scene need not have more triangles at all (the props can be small and few-sided), because triangle count is only one cost and per-call overhead can dominate when there are many small objects.
- D: Draw calls are mostly CPU and submission cost; shading cost depends on pixels covered, which merging calls does not reduce.
- E: The overhead is mostly CPU-side validation and driver work, which differs between APIs and engines, which is why newer APIs were designed to lower it.

**Source:** Draw call

## MA-ch13.6

A forest scene has 2,000 trees that use the same mesh and the same material, and 40 rocks that each use a different mesh and a different material. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Instancing can draw all 2,000 trees in one draw call, because they share a mesh and material and differ only in per-instance data like position.
- [ ] B. Instancing can also combine the 40 rocks into one draw call, because instancing works on groups of objects with different meshes and materials.
- [ ] C. Batching merges geometry that shares a material into fewer draw calls, but merging copies of one mesh into a single large mesh stores the vertex data of each copy, using more memory.
- [ ] D. Giving each of the 2,000 trees its own unique material makes them easier to batch, because each tree can then be tuned separately.
- [ ] E. Sprites that show different images can still share one material and be batched if the images are packed into a single texture atlas.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Instancing draws many copies of one mesh with one material, with per-instance values such as transform supplied alongside.
- B: Different meshes and materials cannot be drawn as instances of one mesh, so the rocks remain separate.
- C: Merging copies into one mesh cuts calls but stores each copy's geometry separately, so memory use rises.
- D: A unique material per tree breaks any grouping by material and makes the draw count worse.
- E: An atlas lets different images live in one texture, so objects using different pictures can share a material.

**Source:** Batching versus instancing

## MA-ch13.7

A developer tells a coding agent: "The grass is slow. Use instancing." The grass is 50,000 blades, each currently a separate scene node with its own mesh and material resource. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For the instruction to work, the agent must set up one shared blade mesh, one shared material, and a per-instance list of transforms.
- [ ] B. The saving from instancing comes mainly from submitting one draw call for many copies of the mesh, not from drawing fewer triangles.
- [ ] C. Instancing lowers the pixel-shading cost of the grass, since the copies are drawn together in one call.
- [ ] D. Because instancing removes thousands of draw calls, it will speed up the grass, so the agent can apply it and move on without comparing frame times.
- [ ] E. The instruction is precise enough on its own, because "instancing" implies the agent will also add level of detail and culling for each blade.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Instancing needs one mesh and material shared by all copies, plus per-copy data, so the existing per-node resources must be replaced.
- B: Every copy still has its triangles processed; what shrinks is the per-call CPU overhead of submitting 50,000 separate draws.
- C: Drawing copies together saves submission overhead, but every visible pixel of every blade is still shaded, so grass that is slow because of overdraw or shader cost stays slow.
- D: The benefit depends on the platform and on where the time goes (if the grass is slow from shading or overdraw, fewer draw calls will not help), so the change is justified by before and after measurements.
- E: Instancing is a way of drawing many copies in one call; deciding which copies to draw (level of detail, culling) is a separate matter that the instruction would have to request.

**Source:** Instancing and what it requires

## MA-ch13.8

A 1920 x 1080 screen (2,073,600 pixels) is covered by 8 full-screen semi-transparent smoke layers. Each layer is shaded in full for every pixel, with no early rejection. The game targets 60 FPS. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The layers cause about 16.6 million fragment shader invocations per frame.
- [ ] B. At 60 FPS that is about 1.0 billion fragment shader invocations per second.
- [ ] C. The overdraw factor is about 8, meaning each screen pixel is shaded about 8 times per frame.
- [ ] D. Cutting from 8 layers to 2 layers reduces the fragment work by about one third.
- [ ] E. Overdraw is a cost on the CPU, so it shows up when the CPU is waiting on the GPU.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: 2,073,600 pixels x 8 layers = 16,588,800 fragments per frame.
- B: 16,588,800 x 60 = 995,328,000, about one billion per second.
- C: Overdraw measures how many times the average pixel is shaded; eight full layers give a factor of 8.
- D: Two layers is a quarter of eight, so the work falls by about 75 percent, to about 4.1 million per frame.
- E: Overdraw is shading work on the GPU (a fill-rate cost), not CPU work.

**Source:** Overdraw and fill rate

## MA-ch13.9

A mobile scene has only 200 draw calls and spends 4 ms of CPU time per frame, yet runs at 14 FPS because 12 full-screen semi-transparent fog planes overlap. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Fill rate, the pixel shading work, is the likely limit, so cutting draw calls alone will not help much.
- [ ] B. Merging all twelve fog planes into one mesh removes the overdraw, since only one object is then drawn.
- [ ] C. Frustum culling would remove the fog planes and fix the problem, since most of them overlap each other.
- [ ] D. Adding level-of-detail meshes to the fog planes would fix the problem, since LOD reduces the cost of drawing distant objects.
- [ ] E. Using higher-resolution fog textures would fix the problem, since sharper textures need fewer layers to look dense.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The CPU side is cheap here, so the GPU is the limit, and each pixel is shaded about twelve times.
- B: Merged geometry still covers the same pixels twelve times, so every pixel is still shaded for every layer.
- C: The planes are inside the view, so frustum culling keeps them.
- D: The planes are already minimal geometry; the cost is the number of pixels shaded, not triangles.
- E: Larger textures add memory and sampling cost without reducing the layers shaded.

**Source:** Overdraw versus draw calls

## MA-ch13.10

A 3D game draws a city. Check each statement that is true about culling. Each statement is worth 1 point (5 points total).

- [ ] A. Frustum culling skips objects that lie wholly outside the camera's view volume.
- [ ] B. Occlusion culling skips objects that are inside the view volume but hidden behind other geometry.
- [ ] C. Frustum culling alone still submits a building hidden behind a large wall if the building is inside the camera's view volume.
- [ ] D. Culling decides what not to draw, so it lowers the draw calls and shading work spent on the culled objects.
- [ ] E. Backface culling removes entire objects that are behind the camera, which is why frustum culling is rarely needed.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: A view frustum is the volume the camera can see; objects wholly outside it cannot appear.
- B: Occlusion culling tests visibility against other geometry, not just the view volume.
- C: Being in the frustum is not the same as being visible, which is the gap occlusion culling fills.
- D: A culled object is not submitted, saving the calls and pixel work it would have caused.
- E: Backface culling discards individual triangles facing away from the camera; objects behind the camera are handled by frustum culling.

**Source:** Culling (frustum and occlusion)

## MA-ch13.11

A character model has three versions: 20,000 triangles for close-ups, 5,000 for mid-range and 1,000 for the distance. Check each statement that is true about level of detail (LOD). Each statement is worth 1 point (5 points total).

- [ ] A. The engine switches to a cheaper version as the object gets farther away or smaller on screen.
- [ ] B. At a distance, using the 1,000-triangle version reduces the vertex and triangle processing for each character drawn.
- [ ] C. Storing all three versions takes more memory than storing only the 20,000-triangle version.
- [ ] D. Visible popping when the version switches can be reduced by cross-fading between versions or by tuning the switch distances.
- [ ] E. With LOD in place, culling is no longer needed, since distant objects are cheap and cost nothing to draw.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: LOD swaps in simpler representations according to distance or screen size.
- B: Fewer triangles and vertices means less geometry work for each distant character.
- C: Each extra version is additional mesh data kept in memory.
- D: Cross-fades and well-chosen transition distances hide the swap from the player.
- E: Cheap is not free; objects outside the view or hidden still cost work unless culled.

**Source:** Level of detail

## MA-ch13.12

A developer tells a coding agent: "Pool the bullets." Currently each shot creates a new bullet object and destroys it on impact. At 20 shots per second the game stutters periodically. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Object pooling creates bullets in advance and reuses them: one is taken from the pool on firing and returned on impact.
- [ ] B. A pooled bullet must be fully reset on reuse (position, velocity, timers, hit flags), or state from its last use leaks into the new shot.
- [ ] C. Pooling removes the need to decide what happens when the pool has no free bullet left, since the pool has enough bullets.
- [ ] D. Pooling avoids repeated allocation and destruction, which with garbage collection also means less garbage to clean up.
- [ ] E. Idle bullets in a pool cost nothing while they wait, since an object that is not in use takes up no memory and no processing time at all.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The pool trades creating and destroying objects for acquiring and releasing existing ones.
- B: Reused objects keep whatever state they had, so a missed reset makes a shot behave like the previous one.
- C: A pool has a fixed size, so the code needs a policy for exhaustion, such as growing, skipping the shot or recycling the oldest.
- D: Less allocation means less short-lived garbage and fewer collection pauses where a collector is used.
- E: Pooled objects still occupy memory and may cost processing unless they are disabled.

**Source:** Object pooling

## MA-ch13.13

A game written in a language with a tracing garbage collector allocates a small temporary list every frame. After ten seconds, players see a brief freeze about once every few seconds. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Garbage is memory that was allocated and is no longer referenced, which the collector later reclaims.
- [ ] B. Collection can interrupt the game for part of a frame at times the developer does not control, which shows as a hitch.
- [ ] C. Making the temporary list larger removes the freezes, because the collector then runs less often.
- [ ] D. Lowering the display refresh rate fixes the cause of the freezes, because frames then arrive less often and the collector has more time.
- [ ] E. A faster GPU reduces collection pauses, because the freezes happen at the moment the frame is drawn.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Garbage is unreachable allocated memory awaiting reclamation by the collector.
- B: The collector runs when it decides to, and its work can take time out of a frame, which shows as a spike.
- C: A larger list creates more garbage per frame, which makes collection more frequent or longer.
- D: The refresh rate does not control allocation; the freezes come from allocation and collection.
- E: Collection runs on the CPU and manages CPU-side memory, so GPU speed does not change it.

**Source:** Garbage collection

## MA-ch13.14

A 2048 x 2048 texture with four 8-bit channels (RGBA, 4 bytes per pixel) is uploaded to the GPU uncompressed. Take 1 MiB as 1,048,576 bytes. A full mipmap chain adds about one third on top of the base level (1 + 1/4 + 1/16 + ... = 4/3). A GPU-compressed format stores the same image at 1 byte per pixel. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The base level occupies 16 MiB (2048 x 2048 x 4 bytes).
- [ ] B. With a full mipmap chain, the uncompressed texture occupies about 21.3 MiB.
- [ ] C. In the compressed format with a full mipmap chain, it occupies about 5.3 MiB.
- [ ] D. A 100 KB PNG file of this image occupies only about 100 KB of GPU memory.
- [ ] E. Halving both dimensions to 1024 x 1024 reduces the uncompressed base level to a quarter, 4 MiB.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: 2048 x 2048 x 4 bytes = 16,777,216 bytes = 16 MiB.
- B: 16 MiB x 4/3 is about 21.3 MiB.
- C: 2048 x 2048 x 1 byte = 4 MiB, and times 4/3 is about 5.3 MiB.
- D: A PNG is compressed for storage on disk; the GPU needs the pixels in a format it can sample, so its size in memory follows the format, not the file.
- E: Memory scales with pixel count, so halving each dimension leaves a quarter: 1024 x 1024 x 4 = 4 MiB.

**Source:** Texture memory

## MA-ch13.15

A developer compares two implementations of a system. Version A's mean frame time (ms) in five separate runs was 8.4, 8.0, 8.2, 8.1 and 8.3. Version B's was 7.9, 8.5, 7.6, 8.4 and 8.2. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Both versions have a median of 8.2 ms across their five runs.
- [ ] B. B's mean (8.12 ms) is only 0.08 ms below A's (8.2 ms), far less than B's own spread of 7.6 to 8.5 ms, so the runs do not show B is faster.
- [ ] C. The right conclusion from these numbers is that B is about 1 percent faster, since its mean is lower, so the team should switch.
- [ ] D. More repeated runs would help show whether any real difference exists beyond run-to-run variance.
- [ ] E. Frames from the first seconds after launch, while shaders compile and caches fill, should usually be excluded as warm-up.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Sorted, A is 8.0, 8.1, 8.2, 8.3, 8.4 and B is 7.6, 7.9, 8.2, 8.4, 8.5; the middle value is 8.2 in both.
- B: Variation between runs of the same code is larger than the gap between the means, so the difference is within noise.
- C: Reporting a 1 percent gain would claim an effect the data cannot distinguish from chance.
- D: More repetitions shrink the uncertainty and show whether a consistent difference exists.
- E: Start-up work is not representative of steady-state cost, so it is normally discarded before measuring.

**Source:** Benchmark method: warm-up, repetition, variance

## MA-ch13.16

A developer reports: "The game shows a steady 60 FPS, so it has plenty of headroom." The display refreshes at 60 Hz with vertical sync on, the measurement was taken inside the editor with debugging tools attached, and it was taken on a fast development PC rather than the target phone. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. With vertical sync on, frame rate is capped at the refresh rate, so 60 FPS does not show whether frames take 4 ms or 16 ms.
- [ ] B. Measurements from an editor session or a debug build can differ from a release build, because of extra checks and tool overhead.
- [ ] C. A fast development PC performs the same as the target phone, so the result transfers directly to the device.
- [ ] D. A steady 60 FPS proves that each frame uses exactly 16.7 ms of CPU work, since a locked frame rate means the frames take the full budget.
- [ ] E. Turning vertical sync off would make the game slower, because the display would then be waiting on it.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A frame that finishes early waits for the next refresh, so the FPS number hides how much time is left over.
- B: Editors and debug builds add work that a shipped build does not, so release builds on the target are the honest test.
- C: Different hardware has different CPU, GPU and memory limits, so measurements must be taken on the device being targeted.
- D: The cap means the frame can take less than the budget and still show 60 FPS.
- E: Vertical sync waits on the display and does not make the work faster; turning it off only removes the cap and exposes the real frame time.

**Source:** Measurement pitfalls: vsync, build type, hardware

## MA-ch13.17

A 60 Hz game has a budget of 16.7 ms per frame and currently takes 20 ms. A profiler shows: physics 8 ms, one function update_minimap 1 ms, and everything else 11 ms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Making update_minimap twice as fast saves only 0.5 ms, small compared with the roughly 3.3 ms that must be saved to reach the budget.
- [ ] B. Making physics four times faster would cut the frame to about 14 ms, inside the budget.
- [ ] C. Making update_minimap infinitely fast would bring the game under budget on its own.
- [ ] D. The 3.3 ms to be saved should be shared out in roughly equal parts across physics, update_minimap and the remaining 11 ms of work, since each of them adds to the frame time.
- [ ] E. Because update_minimap is the easiest function to change, the best first step is to rewrite it, and the larger costs can be looked at afterwards if the budget is still missed.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Halving a 1 ms function saves 0.5 ms, about 3 percent of the frame.
- B: Physics falls from 8 to 2 ms, saving 6 ms, and 20 - 6 = 14 ms.
- C: Removing the whole 1 ms still leaves 19 ms, above 16.7 ms.
- D: update_minimap costs 1 ms in total, so it cannot supply an equal 1.1 ms share; the saving has to come mostly from the large items, physics and the remaining work.
- E: Effort belongs where the measured time is: update_minimap offers at most 1 ms of the 3.3 ms needed and cannot meet the goal alone, while physics at 8 ms offers far more, and ease of change does not alter that.

**Source:** Bottleneck and premature optimization

## MA-ch13.18

A developer is learning to use a profiler. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A profiler records where time or memory goes during a run, such as per function or frame stage, to find hot spots.
- [ ] B. Recording in a profiler's most detailed mode does not change how fast the game runs, so the frame times it reports can be quoted as the game's normal speed.
- [ ] C. A profiler's report points to the fix as well as to the slow part, so the developer's job is to carry out what the report indicates.
- [ ] D. A capture of a single frame taken at a busy moment is enough to find the bottleneck of a game whose load changes during play.
- [ ] E. A profiler reports how long the CPU spends in each function, but time spent on the GPU is not measured directly and has to be guessed from the frame rate.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Showing where time is spent is the purpose of a profiler.
- B: Detailed profiling adds overhead and slows the program, which is why absolute times from a profiled run should not be quoted as normal speed.
- C: A profiler shows data; deciding what it means and what to change is the developer's work.
- D: One frame can be unrepresentative, so captures should span a representative stretch of play.
- E: GPU profiling tools exist in the major engines and report GPU time separately from CPU time.

**Source:** Profiler
