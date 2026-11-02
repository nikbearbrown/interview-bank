# Chapter 13: Profiling and optimization

## ES-ch13.1

A developer gives a coding agent this instruction: "Make the game faster." Rewrite it as a precise set of instructions using correct performance terms, and explain what the agent could do wrongly with the original wording.

**Points:** 5

**Rubric (1 point each):**

1. Sets a measurable target on named hardware, such as a frame-time budget (16.7 ms at 60 Hz) on the target device, and asks for frame time in milliseconds rather than only FPS.
2. Requires profiling first to find the bottleneck (CPU-bound or GPU-bound, and which function or frame stage), before any code is changed.
3. Requires one change at a time, with the same scene and conditions measured before and after, using repeated runs, a warm-up period and a report of spread or percentiles rather than a single number.
4. Requires that behavior stays the same, checked by a test, and that readability and risk be weighed against the gain, stopping once the budget is met.
5. Explains the wrong outcomes the vague wording allows: optimizing something that is not the bottleneck, measuring in an editor or vsync-capped run, changing behavior, or adding complexity for no measured gain.

**Source:** Profiling workflow and instructing an agent

## ES-ch13.2

A game runs at 25 ms per frame on a target device. Explain how you would find out whether the frame is CPU-bound or GPU-bound, using experiments and profiler readings, and give two kinds of fix for each case. Explain why a fix for one kind of bottleneck does nothing for the other, and what you do after applying a fix.

**Points:** 5

**Rubric (1 point each):**

1. Defines CPU-bound (CPU-side work such as game logic, physics, culling and submitting draw calls sets the frame length) and GPU-bound (shading, fill rate and rendering work sets it), noting that in a pipeline the slower side sets frame time.
2. Describes a diagnostic experiment, such as lowering resolution (a faster frame suggests GPU pixel work, while an unchanged frame suggests the frame is not pixel-bound, which leaves the CPU or a vertex-bound GPU), or comparing CPU frame time to GPU time in a profiler to confirm.
3. Gives two CPU-side fixes such as fewer draw calls through batching or instancing, cheaper scripts or physics, updating less often, or object pooling.
4. Gives two GPU-side fixes such as reducing overdraw or fill rate, simpler shaders, lower resolution or texture compression.
5. Explains that speeding up the stage that is not the limit leaves frame time unchanged, and that after a fix the bottleneck may move, so the developer measures again.

**Source:** CPU-bound versus GPU-bound

## ES-ch13.3

A scene draws 5,000 separate small objects, each with its own draw call, and is slow on the CPU even though the total triangle count is modest. Assume each draw call costs about 4 microseconds of CPU time. Explain what a draw call is, work out how much CPU time the calls consume per frame and compare it with a 60 Hz budget, and explain how batching and instancing reduce the cost and what each one requires.

**Points:** 5

**Rubric (1 point each):**

1. Defines a draw call as a command from the CPU to the GPU to draw geometry with a given mesh, material and state.
2. Computes 5,000 x 4 microseconds = 20 ms per frame, which already exceeds the 16.7 ms budget at 60 Hz, regardless of triangle count.
3. Explains batching as combining geometry that shares a material (and a texture atlas) into fewer draw calls, and states that it requires the combined objects to share that material.
4. Explains instancing as drawing many copies of one mesh with one material in a single call with per-instance data such as transforms, and states that it needs identical mesh and material.
5. States the effect on the cost: the saving comes from submitting far fewer calls, not from drawing fewer triangles, so if the 5,000 objects became 10 draw calls the call overhead would fall from 20 ms to 10 x 4 microseconds = 40 microseconds.

**Source:** Draw calls, batching and instancing

## ES-ch13.4

A shooter creates a new bullet object for every shot and destroys it on impact, and the game stutters. A developer asks a coding agent to "pool the bullets". Explain object pooling and why it can help, describe the operations a pool needs and the per-object state that must be handled on reuse, and explain how to choose the pool size and handle a pool that runs out. Also state when pooling would not be worth it. Use 20 shots per second and a bullet lifetime of at most 3 seconds as your numbers.

**Points:** 5

**Rubric (1 point each):**

1. Defines pooling as creating objects in advance and reusing them instead of creating and destroying them, and explains the benefit: less allocation cost and, where a garbage collector is used, less garbage and fewer collection hitches.
2. Describes acquire and release operations, and that an inactive pooled object is hidden and has processing and collision disabled.
3. Requires a full reset of reused objects (position, velocity, timers, ownership, hit flags) so stale state does not leak into the next use.
4. Sizes the pool from peak demand, about 20 x 3 = 60 bullets alive at once, plus margin, and gives a policy for exhaustion such as growing the pool, skipping the shot or recycling the oldest bullet.
5. States when pooling would not be worth it: when a profile shows no spawn, destroy or collection cost, or when the objects are few or long-lived; naming costs such as idle memory, extra complexity or releasing an object twice is welcome but not required.

**Source:** Object pooling and garbage collection

## ES-ch13.5

A developer says: "I ran it once and version B was 20 percent faster than version A, so we are switching." Critique this claim, then describe a sound way to benchmark the two versions and say what you would be entitled to claim afterward.

**Points:** 5

**Rubric (1 point each):**

1. Explains that a single run cannot separate a real effect from run-to-run noise (other processes, thermal effects, scheduling), so the benchmark should be repeated and the spread reported.
2. Requires a warm-up period to be discarded, since start-up work such as shader compilation, caching and loading is not steady-state cost.
3. Requires identical conditions: same build type (release, not an editor or debug build), same hardware, same scene and inputs, vertical sync off or frame work measured directly, and only one variable changed.
4. Says to measure frame time in milliseconds and report mean or median plus a percentile or worst frame, not FPS alone, because averages hide hitches.
5. Limits the claim to what was measured: the hardware and workload tested, with a check that behavior is identical, and a judgment of whether the gain matters against the frame budget.

**Source:** Benchmark method: warm-up, repetition, variance

## ES-ch13.6

A teammate wants to rewrite a gameplay system into a more complex data layout to save an estimated 0.2 ms per frame. The game targets 60 Hz and currently takes 12 ms per frame on the target device. Decide whether to approve the rewrite, using the idea of premature optimization and the frame budget, and say under what conditions you would change your answer.

**Points:** 5

**Rubric (1 point each):**

1. Defines premature optimization as optimizing before measurement shows a need, so the effort may not target a real bottleneck.
2. Uses the arithmetic: the 60 Hz budget is 16.7 ms and the game uses 12 ms, leaving about 4.7 ms of headroom, so 0.2 ms is about 1 percent of the budget and does not change whether the game meets its target.
3. Names the costs of the rewrite: complexity, readability, bug risk and maintenance burden.
4. Gives conditions that would justify it: a profile on the target hardware showing it is a hotspot, a projected increase in load (more entities), a weaker target device, or a frame budget that is currently exceeded.
5. Gives a clear decision (do not approve the rewrite now) and notes that the 0.2 ms saving is only an estimate that would have to be measured before it counts.

**Source:** Premature optimization and frame budget

## ES-ch13.7

A mobile game uses 40 textures of 2048 x 2048 pixels, each RGBA with 4 bytes per pixel and a full mipmap chain (which adds a third on top of the base level), stored uncompressed on the GPU. The game runs out of memory on the target phone. Calculate the texture memory, explain why the size of the image files on disk is not the number that matters, and propose and compare ways to reduce it. Take 1 MiB as 1,048,576 bytes.

**Points:** 5

**Rubric (1 point each):**

1. Computes one texture as 2048 x 2048 x 4 = 16 MiB, about 21.3 MiB with the mipmap chain, and the 40 textures as about 853 MiB.
2. Explains that a PNG or JPEG on disk is compressed for storage, while the GPU needs pixels in a samplable format, so memory depends on resolution, bytes per pixel and format rather than the file size.
3. Proposes GPU texture compression, noting that a format at 1 byte per pixel cuts each texture to about 5.3 MiB (about 213 MiB in total).
4. Proposes reducing resolution where detail is not visible, since halving each dimension leaves a quarter of the memory (1024 x 1024 compressed is about 1.33 MiB each, about 53 MiB in total), and other options such as packing textures into atlases, sharing textures, or streaming.
5. Compares the options by their quality cost: compression can introduce visible artifacts, and lower resolution loses detail wherever it is seen.

**Source:** Texture memory
