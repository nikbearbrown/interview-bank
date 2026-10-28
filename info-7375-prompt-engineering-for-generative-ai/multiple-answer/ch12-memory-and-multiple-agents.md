# Chapter 12: Memory and multiple agents

## MA-ch12.1

Check each statement that is true about the opening scenario, where the newest entry in a shared memory says the light is red and carries a source label and a version number. Each statement is worth 1 point (5 points total).

- [ ] A. A source label plus a version number shows the entry was checked against the world.
- [ ] B. Implementing optimistic concurrency without a mistake guarantees the memory holds no wrong claims.
- [ ] C. In the executed fixture the version check accepted "red" because it judged red to be correct.
- [ ] D. The version check protected the history from one kind of overwrite.
- [ ] E. A write can pass the write protocol exactly as designed and still be unverified.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Neither field looks at the world.
- B: You can still own a wrong claim that is numbered, attributed, and safe to read.
- C: It compared versions only and did not look at the world.
- D: It rejected a later write based on a stale version.
- E: The opening says the entry passed the protocol and is also unverified.

**Source:** Chapter 12 - Memory and multiple agents (opening)

## MA-ch12.2

Check each statement that is true about why shared memory is a hazard when Claude sessions are the workers. Each statement is worth 1 point (5 points total).

- [ ] A. Because Claude sessions work in parallel at a volume no team matches, one unchecked note can be read, summarized, cited, and acted on by several workers before anyone looks.
- [ ] B. The chapter names three jobs for the human: conduct, check, and drive.
- [ ] C. Once an observation becomes memory, later work inherits it, mistakes included.
- [ ] D. The chapter's remedy is to review notes faster than the sessions can produce them.
- [ ] E. A second copy of the model supplies the independent judgment that a single session lacks.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: This is where Claude's strength turns into the hazard.
- B: The opening calls these the book's three jobs.
- C: Stated directly in the opening.
- D: "You do not fix that by out-working them."
- E: A second copy of the model does not give you that judgment.

**Source:** Chapter 12 - Memory and multiple agents (opening)

## MA-ch12.3

Check each statement that is true about the prediction exercise that precedes the first section. Each statement is worth 1 point (5 points total).

- [ ] A. One of the four predictions asks whether a process restart preserves the stored records.
- [ ] B. The answers are kept unedited, because mismatches are evidence about your initial model and not failures to hide.
- [ ] C. The predictions are written down and dated before reading further.
- [ ] D. One of the four predictions asks what version a missing key returns.
- [ ] E. The predictions are revised after running the code so the record shows only correct answers.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: The four concern the missing-key version, two workers writing after reading version zero, mutating a returned list, and whether a nonblank source proves origin.
- B: That is the stated reason.
- C: The chapter asks you to predict four results and date them.
- D: It is the first of the four.
- E: The chapter says to keep them unedited.

**Source:** Chapter 12 - Memory and multiple agents (opening)

## MA-ch12.4

Check each statement that is true about the Memory class in this chapter. Each statement is worth 1 point (5 points total).

- [ ] A. The class automatically gives a model the stored records whenever it runs.
- [ ] B. The store holds what the model understood about each fact.
- [ ] C. The class provides semantic recall through embedding search over stored records.
- [ ] D. In this implementation memory is a record store in which a key indexes a Python dictionary.
- [ ] E. Claude remembers what earlier workers wrote through this class.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: A model receives only whatever text your application puts into its context.
- B: A record is external state that holds exactly what you decided it would hold.
- C: There is no semantic recall, embedding search, or learned representation.
- D: The class is a dictionary and a lock.
- E: Claude remembers nothing through the class.

**Source:** Memory is stored state, not recollection

## MA-ch12.5

Check each statement that is true about reading a key that has never been written. Each statement is worth 1 point (5 points total).

- [ ] A. The read returns a constructed default with version 0, value None, and source None.
- [ ] B. Version zero means no stored write has yet advanced the record.
- [ ] C. A downstream worker should distinguish "no record" from "the recorded value is unknown" if the domain needs the difference.
- [ ] D. Reading an absent key raises an exception.
- [ ] E. Version zero means a fact exists whose value is None.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: That is the stated default.
- B: It is an API state.
- C: The convention must not quietly become ontology.
- D: It returns the default record.
- E: It does not mean that.

**Source:** Memory is stored state, not recollection

## MA-ch12.6

Check each statement that is true about what an existing record stores. Each statement is worth 1 point (5 points total).

- [ ] A. The store prompts the developer to decide whether to add a creation time, signature, or verification status.
- [ ] B. The source field is caller-supplied text describing provenance.
- [ ] C. The author identity can be inferred from the source string.
- [ ] D. The version field is a local revision counter.
- [ ] E. The record includes an expiry time that the store can enforce.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Each absent field is a decision nobody made, and nothing in the store prompts anyone to ask.
- B: It records claimed provenance but does not prove it.
- C: None of the absent fields can be inferred from the fields that exist.
- D: It counts revisions of the record locally, nothing more.
- E: No expiry time is stored.

**Source:** Memory is stored state, not recollection

## MA-ch12.7

Check each statement that is true about the read method. Each statement is worth 1 point (5 points total).

- [ ] A. A restart loses the dictionary.
- [ ] B. The lock and deep copy together make the class a distributed database.
- [ ] C. Code that touches the records dictionary directly is still protected by the lock.
- [ ] D. If a caller appends to a returned list, a later read still sees the unchanged stored list.
- [ ] E. The read method holds a process-local lock and returns a deep copy.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The records live in process memory.
- B: Neither mechanism does.
- C: It bypasses the lock.
- D: The repository test executes that boundary.
- E: The lock guards the read and the deep copy isolates the caller.

**Source:** Memory is stored state, not recollection

## MA-ch12.8

Check each statement that is true about optimistic concurrency control as the chapter describes it. Each statement is worth 1 point (5 points total).

- [ ] A. Stale work may need to be discarded, reconsidered, or merged.
- [ ] B. A worker reads a version and works on the assumption that the record will not change.
- [ ] C. At commit time the worker supplies the version it read, and the store compares it with current state.
- [ ] D. "Optimistic" means the store locks the record for the whole of the worker's work.
- [ ] E. On a mismatch the store can tell you whether to discard, reconsider, or merge the stale work.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: That is the stated trade-off.
- B: That is the optimistic assumption.
- C: The write method takes an expected version.
- D: Workers proceed without locking for the whole of their work.
- E: The store cannot tell you which.

**Source:** Revision boundaries and optimistic concurrency

## MA-ch12.9

Check each statement that is true about why the version comparison happens inside the lock. Each statement is worth 1 point (5 points total).

- [ ] A. The lock makes the check-and-replace atomic across processes, restarts, and machines.
- [ ] B. Comparing inside the lock lets the store decide whether the new value is true.
- [ ] C. With an unguarded check, the stale writer would still be rejected, so the lock is a formality.
- [ ] D. With comparison and write as separate unguarded steps, two threads could both compare against version zero before either writes.
- [ ] E. In that race both threads could write version one, and the second would silently overwrite the first.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Only among threads sharing the same object.
- B: The check is about versions, not truth.
- C: The unguarded version lets a silent overwrite through.
- D: The race the lock removes.
- E: Both passed the same stale comparison, so the later write replaced the earlier one without error.

**Source:** Revision boundaries and optimistic concurrency

## MA-ch12.10

Check each statement that is true about the revision boundary. Each statement is worth 1 point (5 points total).

- [ ] A. The store works out the revision boundary automatically from the values written.
- [ ] B. A version number guards one key.
- [ ] C. If one decision reads three keys, all three version numbers can be current while the decision is stale.
- [ ] D. If two locations share one key, a single conflict covers both.
- [ ] E. A current version on a key shows that a plan built from that key and a separate document is still current.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: It is a choice you make before any worker runs.
- B: It says nothing about other keys.
- C: A per-key version cannot see cross-key staleness.
- D: A shared key means a shared version, so one conflict covers both locations.
- E: A version says nothing about the document a plan was built from.

**Source:** Revision boundaries and optimistic concurrency

## MA-ch12.11

Check each statement that is true about the input checks in the write method. Each statement is worth 1 point (5 points total).

- [ ] A. True is accepted as expected version 1 because Booleans behave as integers.
- [ ] B. The source must be a string containing something besides whitespace.
- [ ] C. The expected version must have exact type int, which rejects Python Booleans.
- [ ] D. The checks validate that the source identifies a real, current document.
- [ ] E. A source of three spaces passes the check because it is a string.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The exact-type check rejects it.
- B: A blank source raises an error.
- C: Booleans otherwise behave as integers.
- D: They are input-shape boundaries only.
- E: Whitespace-only sources are rejected.

**Source:** Revision boundaries and optimistic concurrency

## MA-ch12.12

Check each statement that is true about the constructed two-worker trace in the worked example. Each statement is worth 1 point (5 points total).

- [ ] A. A's successful write is a verified observation.
- [ ] B. Changing A's source label from "unverified-observation" to "authoritative-sensor" would authenticate a sensor.
- [ ] C. The trace is constructed: the chapter chose the key, values, and sources, and no recorded run produced it.
- [ ] D. Worker A's write of "red" with expected=0 on a fresh store succeeds and returns 1.
- [ ] E. Worker B's later write with expected=0 raises ValueError("Stale memory version").

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It is a successful write only.
- B: The class trusts caller-written provenance as data.
- C: Stated before the trace.
- D: Current version 0 equals the expected int 0.
- E: The current version is one at commit time.

**Source:** Worked example: two workers, one key

## MA-ch12.13

Check each statement that is true about the incident timeline table for the two workers. Each statement is worth 1 point (5 points total).

- [ ] A. Step 3 establishes that B's premise conflicts with the current revision.
- [ ] B. Step 1 establishes only local absence at read time.
- [ ] C. Step 5, where a human checks the evidence, is performed inside the store.
- [ ] D. Step 2 establishes that the claim "red" is correct.
- [ ] E. Step 4, where a reviewer reads version 1, establishes whether the claim is true.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: The stale error.
- B: The default read of a missing key.
- C: It happens outside the store.
- D: It establishes that A's update committed.
- E: It shows current process-local state.

**Source:** Worked example: two workers, one key

## MA-ch12.14

Check each statement that is true about the executed sequential fixture on the key claim. Each statement is worth 1 point (5 points total).

- [ ] A. The fixture was built so that red is the wrong value, and nothing in the store was told that.
- [ ] B. The accepted step-2 write carried the source label "unverified source label".
- [ ] C. The fixture shows how the store behaves under real concurrent load.
- [ ] D. The rejected step-3 write carried value blue with source s1 at expected version 1.
- [ ] E. If blue were the stale value and red the correction, the store would behave differently.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The version check never receives any information about which value is right.
- B: A label that names no source.
- C: It is sequential and shows version behavior, not contention.
- D: It was rejected as a stale version.
- E: It would behave identically.

**Source:** Worked example: two workers, one key

## MA-ch12.15

Check each statement that is true about what should happen after the stale rejection. Each statement is worth 1 point (5 points total).

- [ ] A. The rejection shows that the stale worker's value is the wrong one.
- [ ] B. Blindly rereading and retrying is the recommended response because it satisfies concurrency control.
- [ ] C. The conflict might mean A corrected B, A is wrong, they observed at different times, or the key collapses two locations into one name.
- [ ] D. The conflict is a signal to go back to a decision.
- [ ] E. The storage mechanism cannot answer what should happen next.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The version check decides order, not merit.
- B: It satisfies concurrency control while ignoring what the conflict means.
- C: These are the interpretations the chapter offers.
- D: Not a prompt to retry.
- E: Whether to withdraw, merge, or reopen a decision is outside the store.

**Source:** Worked example: two workers, one key

## MA-ch12.16

Check each statement that is true about writing the failure down before running the stale-writer fixture. Each statement is worth 1 point (5 points total).

- [ ] A. The sentence is dated and not revised afterward.
- [ ] B. The sentence says what a wrong coordinator would do, such as retry at the fresh version, keep whichever write arrived last, or swallow the exception and log success.
- [ ] C. Passing a test is not the same as supporting a claim.
- [ ] D. The sentence may be edited after the run to match what happened.
- [ ] E. The gap between the sentence and the result is what you are learning from.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: The gap between sentence and result is the lesson.
- B: These are the chapter's examples.
- C: The chapter calls this the trap.
- D: Do not revise it afterward.
- E: Writing the failure first makes the surprise measurable.

**Source:** Check: what each guard establishes

## MA-ch12.17

Check each statement that is true about the guards in the chapter's table of what each establishes. Each statement is worth 1 point (5 points total).

- [ ] A. The lock establishes that check-and-replace is atomic among threads sharing this object.
- [ ] B. The expected-version check establishes that the new value is true.
- [ ] C. The expected-version check establishes that the writer's premise matched current state at commit.
- [ ] D. Deep copy on read establishes that the stored value is valid.
- [ ] E. The lock establishes atomicity across processes, restarts, and machines.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: That is its entry in the table.
- B: It does not.
- C: That is its entry in the table.
- D: It prevents aliasing, nothing more.
- E: It does not.

**Source:** Check: what each guard establishes

## MA-ch12.18

Check each statement that is true about the remaining rows of the chapter's table of guards. Each statement is worth 1 point (5 points total).

- [ ] A. The version counter establishes commit order for one key.
- [ ] B. A nonblank source string establishes that someone supplied attribution.
- [ ] C. A nonblank source string establishes that the source exists, says this, or is current.
- [ ] D. Two sessions agreeing establishes two independent routes to the claim.
- [ ] E. The version counter establishes when anything was observed.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: That is what it establishes.
- B: That is what it establishes.
- C: It does not.
- D: It shows only that two runs produced similar text.
- E: It does not.

**Source:** Check: what each guard establishes

## MA-ch12.19

Check each statement that is true about freshness and the version counter. Each statement is worth 1 point (5 points total).

- [ ] A. A newer claim can be a newer mistake.
- [ ] B. A version counter establishes the time of observation.
- [ ] C. A timestamp proves that a claim is accurate.
- [ ] D. Freshness is defined relative to a use.
- [ ] E. A version counter orders a record's local history.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Recency says nothing about whether the observation was correct.
- B: It does not.
- C: Even a timestamp does not prove accuracy.
- D: The same age can be fine for a draft and stale for a train board.
- E: That is its job.

**Source:** Check: what each guard establishes / Freshness is not truth

## MA-ch12.20

Check each statement that is true about expiry and freshness policy. Each statement is worth 1 point (5 points total).

- [ ] A. Expiry tells you whether the refreshed observation is correct.
- [ ] B. Yesterday's building address is too old to use even in a draft.
- [ ] C. Storing observed_at, valid_until, and source_id separately lets the application flag a record outside its interval.
- [ ] D. One expiry interval suits every record, because the policy does not depend on consequence.
- [ ] E. A train departure board may be stale after seconds.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It says only when evidence must be refreshed.
- B: It may be current enough for a draft.
- C: Separate fields let code test the interval; they still do not validate the observation.
- D: Expiry policy is tied to consequence.
- E: The chapter's example of a short freshness window.

**Source:** Check: what each guard establishes / Freshness is not truth

## MA-ch12.21

Check each statement that is true about the clocks a record might need. Each statement is worth 1 point (5 points total).

- [ ] A. A broken source cannot supply a fresh claim, because freshness is checked at write time.
- [ ] B. Revision time, observation time, event time, ingestion time, and expiration time answer different questions.
- [ ] C. The version counter doubles as the observation time of the record.
- [ ] D. A single field called timestamp invites later code to pick the most convenient meaning.
- [ ] E. Once an expiry time is stored, naming the other clocks separately is unnecessary.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A broken source can provide fresh falsehoods all day.
- B: The chapter says to name the clocks.
- C: It orders commits, not observations.
- D: The reason for separating the clocks.
- E: The different clocks answer different questions.

**Source:** Check: what each guard establishes / Freshness is not truth

## MA-ch12.22

Check each statement that is true about the source field. Each statement is worth 1 point (5 points total).

- [ ] A. The class requires a source because unattributed memory is hard to audit.
- [ ] B. A required source guarantees every record can be traced to a document that exists.
- [ ] C. Practical provenance might include a stable source identifier, a retrieval date, the exact supporting passage, and a transformation record.
- [ ] D. The code verifies that a syllabus produced the office location named in a source string.
- [ ] E. The source is only a nonblank string.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The stated reason.
- B: It does not verify that the source exists.
- C: Each element supports an audit of where the value came from.
- D: It does not.
- E: Nothing more is checked.

**Source:** Check: what each guard establishes / A source label is a place to put provenance

## MA-ch12.23

Check each statement that is true about derived values and authentication. Each statement is worth 1 point (5 points total).

- [ ] A. A signed message makes the claim in it true.
- [ ] B. If an agent summarizes a source, the record should preserve that the value is a derived summary.
- [ ] C. Authentication is a separate layer from recording provenance.
- [ ] D. Concurrency control, provenance rules, and domain verification should be merged into one check.
- [ ] E. A model's paraphrase can be stored as if it were source text, since the source string covers it.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: It may show who produced the bytes but does not make the claim true.
- B: So a model's paraphrase is not mistaken for source text.
- C: The chapter calls it another layer.
- D: Keep the jobs separate so you can test each.
- E: Preserve that it is a derived summary.

**Source:** Check: what each guard establishes / A source label is a place to put provenance

## MA-ch12.24

Check each statement that is true about three jobs the chapter says to keep separate. Each statement is worth 1 point (5 points total).

- [ ] A. A nonblank-source rule decides whether the claim is true.
- [ ] B. Domain verification evaluates support.
- [ ] C. Provenance rules reject missing attribution.
- [ ] D. The version check evaluates whether a claim is supported by its source.
- [ ] E. Concurrency control rejects stale versions.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It only rejects missing attribution.
- B: It asks whether the evidence supports the claim, which the store never does.
- C: It enforces that some attribution exists.
- D: That is domain verification.
- E: It orders commits and rejects premises that are out of date.

**Source:** Check: what each guard establishes / A source label is a place to put provenance

## MA-ch12.25

Check each statement that is true about the cascade pattern. Each statement is worth 1 point (5 points total).

- [ ] A. The chapter reports cascade frequencies as rates to plan around.
- [ ] B. Checking each worker in isolation is enough to detect a cascade.
- [ ] C. A cascade requires the first worker to be wrong with high probability.
- [ ] D. In a cascade a second worker conditions on a first worker's output, a third on the second's, and so on.
- [ ] E. By the end, the system's error is governed by how errors compound across the chain.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Look for the patterns; do not read them as rates.
- B: That tells you little about it.
- C: The chapter says wrong with some small probability.
- D: The chain structure.
- E: Per-worker accuracy does not capture compounding along the chain.

**Source:** The handoff is where claims gain authority

## MA-ch12.26

Check each statement that is true about authority laundering. Each statement is worth 1 point (5 points total).

- [ ] A. The pattern comes from a large controlled trial that measured its rate.
- [ ] B. Tracking provenance across workers addresses the pattern.
- [ ] C. The data takes on the standing of the channel it arrived through.
- [ ] D. Limiting what a single worker may access prevents the pattern.
- [ ] E. A worker passes data to another as a legitimate output, and the receiver cannot verify where it came from.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It comes from an exploratory study of one framework, two frontier models, two weeks.
- B: Seeing the origin across hand-offs is what lets a receiver check the claim.
- C: The definition.
- D: It does not prevent it.
- E: The definition.

**Source:** The handoff is where claims gain authority

## MA-ch12.27

Check each statement that is true about the constructed lineage in which note-7 (source s1) leads to summary-A, summary-B, and a report that cites summary-B. Each statement is worth 1 point (5 points total).

- [ ] A. summary-B counts as a confirmation of note-7 because it is a separate document.
- [ ] B. The lineage records 0 independent confirmations of note-7 and 1 lineage.
- [ ] C. Version history proves the claim in the note.
- [ ] D. The report citing summary-B adds an independent confirmation.
- [ ] E. Ten summaries of one wrong note are one lineage, not ten confirmations.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: It derives from summary-A, which derives from note-7.
- B: The chain note-7, summary-A, summary-B, report is a single path.
- C: It proves the order of commits, not the claim.
- D: It remains the same lineage.
- E: Repeating a derived claim adds copies, not independent routes to it.

**Source:** The handoff is where claims gain authority

## MA-ch12.28

Check each statement that is true about shared notes as an input boundary. Each statement is worth 1 point (5 points total).

- [ ] A. Inserting stored text into a later prompt turns the record store into a possible instruction channel.
- [ ] B. Version checks preserve instruction-like text and deep copies protect it from accidental mutation, but neither decides whether it is evidence, data, or an instruction.
- [ ] C. A prompt warning is an authorization system.
- [ ] D. Deep copying a note neutralizes instruction-like text in it.
- [ ] E. The stored prose of a note decides what the note may cause.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Stored text re-enters the prompt, where it can be read as an instruction.
- B: Preserving and copying text is different from classifying it.
- C: It is not.
- D: It only prevents accidental mutation.
- E: The application decides.

**Source:** The handoff is where claims gain authority / Shared notes are an input boundary

## MA-ch12.29

Check each statement that is true about controls for shared notes. Each statement is worth 1 point (5 points total).

- [ ] A. Delimit shared notes from application instructions.
- [ ] B. Preserve the provenance of shared notes.
- [ ] C. A quarantine state deletes suspicious records so they cannot be read.
- [ ] D. Validate proposed actions at execution time.
- [ ] E. Once the prompt warns the model about notes, the tool boundary no longer has to reject out-of-scope operations.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Separating the channels keeps stored prose from being read as the application's instructions.
- B: Knowing where a note came from is needed to weigh it.
- C: It keeps them out of prompt construction without deleting what an incident review needs.
- D: The tool boundary, not the note, decides what may actually happen.
- E: The tool boundary must still reject operations outside scope.

**Source:** The handoff is where claims gain authority / Shared notes are an input boundary

## MA-ch12.30

Check each statement that is true about what Claude does in the chapter's split between coordinating and deliberating. Each statement is worth 1 point (5 points total).

- [ ] A. Claude keeps the original outputs and summarizes disagreement without flattening it.
- [ ] B. Claude owns the final decision because it holds all the original outputs.
- [ ] C. Claude holds the initial interpretation formed before the synthesis.
- [ ] D. Claude weighs what a conflict means for the stakes.
- [ ] E. Claude routes tasks and compares artifacts.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Preserving originals keeps disagreement visible.
- B: The decision has a human owner whose name goes on it.
- C: Humans hold it.
- D: Humans do.
- E: Routing and comparing are mechanical coordination tasks.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.31

Check each statement that is true about what humans do in the split. Each statement is worth 1 point (5 points total).

- [ ] A. Humans weigh what a conflict means for the stakes, hear dissent, and decide.
- [ ] B. Humans bring local knowledge the shared notes never contained.
- [ ] C. Humans preserve dissent by averaging it into smooth prose.
- [ ] D. Humans hold the initial interpretation formed before the synthesis.
- [ ] E. The decision is owned by the coordinator session, whose name goes on it.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: These are judgments about stakes that belong to a named owner.
- B: A synthesis cannot contain what nobody wrote into the notes.
- C: The practice is to preserve dissent rather than average it away.
- D: It must exist before the synthesis can anchor it.
- E: The decision has a human owner.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.32

Check each statement that is true about independence among Claude sessions. Each statement is worth 1 point (5 points total).

- [ ] A. A reviewer who sees the researcher's conclusion first may anchor on it.
- [ ] B. Independence is a design question about failure correlation: would the two routes fail for the same reason?
- [ ] C. Two sessions may share a model, training influences, tool configuration, source corpus, and prompt author.
- [ ] D. Two copies of a model count as independent judgments as long as each has a different prompt.
- [ ] E. Role labels such as "researcher" and "reviewer" make two sessions independent.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Seeing the conclusion first can anchor the reviewer.
- B: Independence concerns whether failures are correlated.
- C: These shared factors are what undermine independence.
- D: Copies are not independence.
- E: Role labels do not manufacture independence.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.33

Check each statement that is true about how agreement between automated checks can fail to be independent. Each statement is worth 1 point (5 points total).

- [ ] A. A reviewer who sees the researcher's conclusion first is more independent for having more context.
- [ ] B. Two agents retrieving from one incomplete corpus can agree for the same cause.
- [ ] C. Agreement between two sessions on the same passages counts as two confirmations if their roles differ.
- [ ] D. A deterministic checker is independent of specification errors because it is code.
- [ ] E. A Python checker written from the same mistaken specification ratifies the mistake deterministically.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Anchoring is the risk.
- B: A shared incomplete corpus gives both agents the same blind spot.
- C: Role differences do not create independence.
- D: It inherits the mistaken specification.
- E: A deterministic checker repeats whatever the specification gets wrong.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.34

Check each statement that is true about Condorcet's jury theorem and the sequencing practice as the chapter uses them. Each statement is worth 1 point (5 points total).

- [ ] A. Without independence the theorem says nothing.
- [ ] B. The sequencing practice is to collect initial judgments before showing a synthesis, then deliberate with sources visible and preserve dissent.
- [ ] C. The chapter relies on "invisible groupthink" as an established finding.
- [ ] D. The book argues that showing the synthesis first preserves variety.
- [ ] E. As the book retells it, the theorem rests on two assumptions: the voters are independent and each is better than chance.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The theorem's guarantee depends on independence.
- B: Variety must be captured before a synthesis can collapse it.
- C: It flags the label as a hypothesis and does not rely on it.
- D: Reversing the order collapses variety before it can do any work.
- E: Both assumptions must hold for many judgments to beat one.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.35

Check each statement that is true about role contracts. Each statement is worth 1 point (5 points total).

- [ ] A. In the reviewer example any "cannot tell" verdict goes to the coordinator, who routes it to the named human reviewer.
- [ ] B. A role contract is bounded by inputs, outputs, tools, budget, and escalation.
- [ ] C. In the reviewer example the verdicts are limited to pass or fail.
- [ ] D. In the reviewer example the tools are read only, with no writes to memory.
- [ ] E. "Review the work" is not a role contract.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Escalation reaches a named human rather than being settled by the model.
- B: Vague roles like 'review the work' bound none of these.
- C: They are supported, unsupported, or cannot tell.
- D: The reviewer can read but cannot change memory or files.
- E: The chapter says so directly.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.36

Check each statement that is true about preserving disagreement and about a solo learner. Each statement is worth 1 point (5 points total).

- [ ] A. A solo learner writes a dated initial interpretation before reading any Claude synthesis.
- [ ] B. A solo learner can skip the initial interpretation because Claude's synthesis covers it.
- [ ] C. You must not fabricate teammates.
- [ ] D. The coordinator keeps the original outputs so synthesis cannot erase disagreement.
- [ ] E. Two model personas count as two people for independent review.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The solo form of the same rule.
- B: The interpretation must come first.
- C: Only real people count as teammates.
- D: The originals are the evidence of disagreement.
- E: They are not two people.

**Source:** Multiple workers: Claude coordinates, humans deliberate

## MA-ch12.37

Check each statement that is true about integration and the re-engagement trigger. Each statement is worth 1 point (5 points total).

- [ ] A. The re-engagement trigger comes from the Computational Skepticism companion.
- [ ] B. Integration holds the parts at once so a finding in one can reach backward and reopen another.
- [ ] C. A re-engagement trigger is an event: a locatable moment when you noticed something that made an earlier decision unsafe and went back.
- [ ] D. "Stay flexible" is an acceptable form of re-engagement trigger.
- [ ] E. Sequencing runs the parts one after another and then writes a summary.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It comes from Conducting AI.
- B: That backward reach is what makes it integration.
- C: A locatable event can be written down and checked.
- D: The trigger is an event, not an attitude.
- E: It is sequential work followed by a summary.

**Source:** Integration is not sequencing

## MA-ch12.38

Check each statement that is true about triggers that reopen earlier decisions. Each statement is worth 1 point (5 points total).

- [ ] A. A stale-version exception is the only kind of trigger that matters.
- [ ] B. Before any worker runs you need to decide only what the record holds.
- [ ] C. A newer source, a reviewer's correction, and a failed spot check are triggers the store cannot raise.
- [ ] D. Triggers from outside the store are less consequential than the stale-version exception.
- [ ] E. A stale-version exception is a trigger the store raises on its own.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It is only one kind.
- B: You also decide what events reopen what, and who notices.
- C: They come from outside the store.
- D: The more consequential ones come from outside.
- E: The version check inside the store is something it can raise itself.

**Source:** Integration is not sequencing

## MA-ch12.39

Check each statement that is true about why a gate that includes reopening conditions is not waterfall. Each statement is worth 1 point (5 points total).

- [ ] A. The plan from Chapter 10 is revised automatically when its evidence is gone.
- [ ] B. Design-first does not mean freeze the design.
- [ ] C. A plan without reopening conditions is already a gate.
- [ ] D. The chapter recommends a waterfall process in which the design is frozen before workers start.
- [ ] E. The gate written before the prompt includes the conditions under which you will reopen it.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Without reopening conditions it stays in force.
- B: The design stays open to new evidence.
- C: The reopening conditions make it a gate rather than a plan.
- D: The chapter says this is not waterfall.
- E: Reopening conditions are what make it a gate rather than a plan.

**Source:** Integration is not sequencing

## MA-ch12.40

Check each statement that is true about the course-schedule simulation in which record version three says an assignment closes Friday, a researcher finds an official schedule saying Monday but has not written it, and an explainer worker is generating Friday-facing instructions. Each statement is worth 1 point (5 points total).

- [ ] A. A stale-version exception is raised as soon as the researcher finds the new schedule.
- [ ] B. It is not a version conflict, because only one new proposal exists.
- [ ] C. The explainer worker's Friday-facing instructions will be rejected by the store.
- [ ] D. It is a dependency conflict between ongoing work and new evidence.
- [ ] E. No version check can see it.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Nothing has been written yet.
- B: Only one proposal exists, so no two writes conflict.
- C: The store sees no conflicting write.
- D: The explainer's work depends on a value the new evidence challenges.
- E: Version checks compare writes, and no competing write has been made.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.41

Check each statement that is true about the incident states in the course-schedule simulation. Each statement is worth 1 point (5 points total).

- [ ] A. The researcher's evidence moves the assumption directly to superseded.
- [ ] B. The previous record becomes superseded as soon as the researcher finds the evidence.
- [ ] C. A coordinator needs only the two states success and failure.
- [ ] D. Downstream tasks whose correctness depends on the closing date move to paused.
- [ ] E. Work moves to resumed as soon as the new version is committed, before affected work is regenerated.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It moves it to challenged; superseded comes after human review.
- B: Only after a named human reviews the source and the Monday date applies.
- C: It needs richer states such as active, challenged, paused, reviewed, superseded, and resumed.
- D: Their premise, the Friday date, is now challenged.
- E: Resumed comes only after regeneration.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.42

Check each statement that is true about the dependency map in the incident example. Each statement is worth 1 point (5 points total).

- [ ] A. Memory correctness at the key is not workflow correction everywhere the value traveled.
- [ ] B. Version numbers order the records, but the dependency map says what must pause.
- [ ] C. Committing the corrected value to the key regenerates downstream outputs automatically.
- [ ] D. The store's version history identifies every output that depended on a given version.
- [ ] E. Without a dependency map the store can accept the correction while Friday instructions already produced keep circulating.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Fixing the record does not fix outputs already produced.
- B: Ordering and dependency are different information.
- C: The store does not do that.
- D: The dependency map does that job.
- E: The store has no knowledge of where the value was used.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.43

Check each statement that is true about reconstructing an incident from logs. Each statement is worth 1 point (5 points total).

- [ ] A. Missing events are marked as gaps.
- [ ] B. A fluent reconstruction of the missing events makes the replay complete.
- [ ] C. If logs show a worker read sometime before version four but not the returned version, the version is recorded as unknown.
- [ ] D. Claude can be relied on to flag fragments that do not fit when it reconstructs an incident.
- [ ] E. A replay that marks what is unknown has failed.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Mark gaps as gaps.
- B: Do not fill missing events with fluent reconstruction.
- C: Do not guess a number the logs do not preserve.
- D: It will write a coherent account including fragments that do not fit.
- E: A replay that marks what is unknown is the desired detection evidence.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.44

Check each statement that is true about a second worker whose Monday update arrives with expected=3 after the reviewer has committed version four. Each statement is worth 1 point (5 points total).

- [ ] A. The write fails because it is based on a stale version.
- [ ] B. Version conflict is a merge algorithm that combines the two proposals.
- [ ] C. The write succeeds because its proposal is correct.
- [ ] D. The stale worker must reread, compare the semantic changes, and either withdraw or create a new reviewable proposal.
- [ ] E. Retrying automatically at version four would be unsafe.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The current version is four.
- B: It is not a merge algorithm.
- C: The version check does not judge correctness.
- D: The approved value may differ in meaning from the stale proposal.
- E: The human-approved value may carry a qualification the proposal lacks.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.45

Check each statement that is true about the Re-engagement Log. Each statement is worth 1 point (5 points total).

- [ ] A. Entries may describe plausible events the fixture did not produce, to keep the log complete.
- [ ] B. Orderly sections are enough evidence that the work reached backward.
- [ ] C. Each entry records only the version read and the final decision.
- [ ] D. This course adopts the companion book's grading of the log.
- [ ] E. It consists of discrete entries proving that the work reached backward.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Write entries only for events that happened.
- B: The log exists because sections can look orderly without reaching back.
- C: It also records the evidence, the owner, what paused, and what allowed resuming.
- D: It takes the idea, not the grading.
- E: The log exists to show events, not tidy structure.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.46

Check each statement that is true about duplicate actions and the memory store. Each statement is worth 1 point (5 points total).

- [ ] A. Consequential tools need idempotency keys or coordination at the action boundary.
- [ ] B. If two workers both send the same email, rejecting a stale memory update afterward does not undo the effect.
- [ ] C. Duplicate action is distinct from duplicate writes.
- [ ] D. A stale-version rejection in the store prevents the duplicate email from being sent.
- [ ] E. Memory is the action system.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Protection must sit where the action occurs.
- B: The effect already happened outside the store.
- C: A rejected write does not reverse an external action.
- D: It cannot undo or prevent the external effect.
- E: Memory is not the action system.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.47

Check each statement that is true about retention and replay. Each statement is worth 1 point (5 points total).

- [ ] A. Redaction preserves interpretability automatically.
- [ ] B. Redacting every value costs nothing for replay.
- [ ] C. You define what is stored, for how long, who can read it, and how deletion works.
- [ ] D. Retention and replay do not compete.
- [ ] E. Complete prompts and tool results aid incident review but may hold private information.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Redaction must be designed to preserve interpretability.
- B: If every value becomes [REDACTED] the trace may no longer show why a decision occurred.
- C: Each is a policy decision about retained traces.
- D: Retention competes with replay.
- E: That is why retention is a tradeoff.

**Source:** Integration is not sequencing / Tear down a complete incident state machine

## MA-ch12.48

Check each statement that is true about the gate. Each statement is worth 1 point (5 points total).

- [ ] A. Next to each item you write who decided it: you, or a suggestion of Claude's that you accepted.
- [ ] B. Claude can write the gate for you without defeating its purpose.
- [ ] C. The gate is written before Claude implements anything, and Claude's work is tested against it.
- [ ] D. The chapter starts one layer earlier than choosing what memory text to place in the prompt, by asking what record must exist so that reliance can be audited.
- [ ] E. Claude can sharpen the gate if you ask it for the trigger you missed.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: It records which decisions were yours.
- B: The gate is where your understanding of the stakes goes on the record.
- C: That order makes the gate a test target for Claude's work.
- D: Auditable reliance comes before prompt contents.
- E: Claude's challenge is useful; its authorship of the gate is not.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.49

Check each statement that is true about the fuller teaching record with fields such as source_id, verification, and valid_until. Each statement is worth 1 point (5 points total).

- [ ] A. Every added field creates a validation problem.
- [ ] B. A richer schema helps by itself, even when code and policy do not enforce the meanings.
- [ ] C. It is a design sketch, not output from the current implementation.
- [ ] D. A verification value of "human-reviewed" shows that a human reviewed the record.
- [ ] E. A valid_until of None has one unambiguous meaning.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Each new field needs rules for who sets it and what it means.
- B: It helps only when they do.
- C: Its fields are not produced by the current class.
- D: Who may set it is itself a policy question.
- E: The chapter asks what None means for expiry.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.50

Check each statement that is true about the three separations in the design of the record. Each statement is worth 1 point (5 points total).

- [ ] A. Facts are not instructions: render {"due_day": "Monday"} as a quoted claim with provenance.
- [ ] B. A stored fact may be rendered into the system instruction channel once it comes from a reviewed version.
- [ ] C. Proposed is not accepted: a research worker should often write to a proposal queue.
- [ ] D. "Shared" means every worker sees every record.
- [ ] E. A reviewer checks meaning after the coordinator commits against the expected version.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Never into the system instruction channel.
- B: Never into the system instruction channel.
- C: A reviewer checks meaning before a coordinator commits.
- D: Reads follow purpose.
- E: The reviewer checks before the coordinator commits.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.51

Check each statement that is true about the first row of the trigger table, in which a newer official schedule contradicts version 3 of due_day. Each statement is worth 1 point (5 points total).

- [ ] A. The owner is the explainer worker.
- [ ] B. Resuming requires a reviewed version to be committed and each paused task to reread it.
- [ ] C. The work that pauses is any task rendering due_day into instructions.
- [ ] D. Work resumes once the researcher's proposal is accepted by the store.
- [ ] E. The earlier decision it reopens is which source counts as authoritative for deadlines.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The owner is the named course-staff reviewer.
- B: Rereading ensures paused work uses the reviewed value.
- C: Only work that renders the value is affected.
- D: A reviewed version must be committed.
- E: Which source is authoritative is the decision a newer schedule reopens.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.52

Check each statement that is true about the second row of the trigger table, in which a stale-version exception hits a key an active task read. Each statement is worth 1 point (5 points total).

- [ ] A. The resume condition is that the coordinator retries at the fresh version.
- [ ] B. Every task in the system pauses.
- [ ] C. The only permitted resolution is for the reviewer to commit.
- [ ] D. The earlier decision it reopens is the assumption that the key was stable during the task.
- [ ] E. The owner is the coordinator, then the decision owner.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Both proposals and evidence are preserved and a reviewer decides.
- B: Only that task's writes and any action depending on it pause.
- C: The reviewer may also reject with a recorded reason.
- D: A stale exception shows the key changed during the task.
- E: The coordinator notices first and the decision owner decides.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.53

Check each statement that is true about the wrong implementations your tests must catch. Each statement is worth 1 point (5 points total).

- [ ] A. A store whose read returns the stored list passes every version test, and the copy-isolation test catches it.
- [ ] B. A coordinator that retries stale writes at the fresh version passes "the write was rejected."
- [ ] C. The retrying coordinator also passes "the proposal was preserved and a reviewer decided."
- [ ] D. A passing threaded test proves the absence of the unlocked-comparison fault.
- [ ] E. A store that compares the version outside the lock passes every sequential test.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Version tests never mutate a returned list.
- B: But it fails the preservation test.
- C: It fails that one.
- D: It can provoke the fault but cannot prove its absence.
- E: Sequential tests cannot expose a race between check and write.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.54

Check each statement that is true about what the record may claim and about moving output downstream. Each statement is worth 1 point (5 points total).

- [ ] A. The record may claim that a named reviewer committed this version.
- [ ] B. Workers may act on a record once Claude reports that its tests passed.
- [ ] C. The record may claim that the value is true.
- [ ] D. An item you cannot write a test for can simply be dropped from the gate.
- [ ] E. The record may claim commit order for one key within one process.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A named reviewer's commit is the human step the record can attest.
- B: The stale-write test must pass, every trigger row needs an owner and resume condition, and the replay must mark gaps.
- C: It may not.
- D: It belongs in the sign-off's "not checked" line.
- E: That is all the version counter orders.

**Source:** The gate: design the record and the triggers before the prompt

## MA-ch12.55

Check each statement that is true about the Build It stage. Each statement is worth 1 point (5 points total).

- [ ] A. Your version is the baseline: the record of what you understood before Claude touched anything.
- [ ] B. The six tests are best read together as "the code works".
- [ ] C. The six tests are read as six distinct questions, including the default for a missing key and the isolation of a returned copy.
- [ ] D. The demo and tests need an API key because they call Claude.
- [ ] E. You write your own Memory in learning-artifacts/week-12/ before opening the reference.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: You measure Claude's version against it.
- B: They are six distinct questions.
- C: Each test isolates one behavior.
- D: They run offline.
- E: Building first gives you a baseline to audit against.

**Source:** Build It: the baseline that lets you audit

## MA-ch12.56

Check each statement that is true about the tests and extensions in Build It. Each statement is worth 1 point (5 points total).

- [ ] A. You should change several inputs at once to cover more cases per run.
- [ ] B. You should read the reference implementation before writing your own so you know the target.
- [ ] C. You can audit a version check you have never broken by reading it carefully.
- [ ] D. An expiry field with a rejected-when-expired test forces the question of what "expired" means.
- [ ] E. You add a meaningful success outside the demo and a failure that would matter in your capstone.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Change one input at a time so a difference has an identifiable cause.
- B: Build before consulting reference.
- C: You cannot audit one you have never broken.
- D: Why it is a good extension.
- E: The two tests the lesson asks for.

**Source:** Build It: the baseline that lets you audit

## MA-ch12.57

Check each statement that is true about handing the work to Claude Code. Each statement is worth 1 point (5 points total).

- [ ] A. You give Claude your gate (the contract, the trigger table, the test list) and not your implementation.
- [ ] B. Claude's report that your tests passed is sufficient.
- [ ] C. A failing test is a flaw in Claude to be fixed without revisiting your gate.
- [ ] D. The harness pauses a task when a stale exception hits a key it depends on, preserves both proposals, and does not resume until a reviewed version is committed and the task rereads it.
- [ ] E. The harness may resume the paused task automatically once the stale exception clears.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Claude works from the gate rather than your solution.
- B: You run your tests on what it returns, yourself.
- C: A failure is often a gap in your gate.
- D: The harness encodes the gate's pause-and-resume rule.
- E: Nothing resumes until a reviewed version is committed and reread.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch12.58

Check each statement that is true about the three things to do with Claude's result. Each statement is worth 1 point (5 points total).

- [ ] A. A boundary Claude handled that you missed is a reason to revise your gate.
- [ ] B. If Claude's version passes all your tests, no comparison with your baseline is needed.
- [ ] C. A failing test is often a gap in your gate, which Claude could not see because it had only what you wrote.
- [ ] D. You compare Claude's implementation with your baseline and name one difference in behavior.
- [ ] E. If a deliberately wrong version from Claude still passes your tests, your test list was too weak.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: That is a gap in the gate, not in the code.
- B: The comparison is still part of the exercise.
- C: Claude sees only what you wrote.
- D: Naming a difference forces you to compare behavior.
- E: A weak test list lets wrong versions pass.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch12.59

Check each statement that is true about the multi-agent half of Use It. Each statement is worth 1 point (5 points total).

- [ ] A. Proposed updates go through a coordinator, and conflicts are recorded rather than resolved by last-writer-wins.
- [ ] B. You write your initial interpretation after reading the synthesis so you can see the disagreements.
- [ ] C. If the two sessions agree, you ask what they shared before counting the agreement as anything.
- [ ] D. If a session failed or did not run, you substitute a fixture and record it as that session's output.
- [ ] E. The sessions work as researcher and reviewer on sanitized fixtures, each with a bounded role contract and preserved source IDs.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A coordinator surfaces conflicts instead of overwriting.
- B: Write and date it before reading any synthesis.
- C: A shared model, prompts, or sources can explain agreement.
- D: Record that it failed rather than substituting a fixture.
- E: Bounded roles and source IDs keep the handoff auditable.

**Source:** Use It: conduct Claude Code against your gate

## MA-ch12.60

Check each statement that is true about the premortem. Each statement is worth 1 point (5 points total).

- [ ] A. Each row needs only a control and a residual risk.
- [ ] B. "Monitor for stale memory" is an operational control.
- [ ] C. It covers stale reads, prompt injection in shared notes, duplicate actions, privacy retention, and an incident replay.
- [ ] D. A control that detects a failure removes the need to test recovery.
- [ ] E. Each control has its own failure, so the residual risk is recorded beside the mitigation.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Each row needs a trigger, owner, evidence, response, and recovery condition.
- B: It is not operational.
- C: The five failures named.
- D: Test recovery, not only detection.
- E: No control is perfect, so its failure mode is recorded.

**Source:** Ship It: the premortem and the sign-off

## MA-ch12.61

Check each statement that is true about the rows of the premortem table. Each statement is worth 1 point (5 points total).

- [ ] A. For privacy retention, the detection evidence is an effect log showing two executions.
- [ ] B. For stale reads, the detection evidence is a stale exception on a key an active task read.
- [ ] C. For prompt injection in shared notes, a residual risk is a quarantine nobody reviews.
- [ ] D. For duplicate actions, the control is an idempotency boundary at the external action and a residual risk is a key scoped wrongly.
- [ ] E. For incident replay, the control is a quarantine state for suspicious records.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: That belongs to duplicate actions.
- B: That is the premortem's evidence for stale reads.
- C: A quarantine that no one reviews fails silently.
- D: Duplicate actions are controlled at the external action.
- E: That belongs to prompt injection.

**Source:** Ship It: the premortem and the sign-off

## MA-ch12.62

Check each statement that is true about testing recovery in the premortem. Each statement is worth 1 point (5 points total).

- [ ] A. A workflow that always accepts the newest proposal has automated last-writer-wins behind a review-shaped ceremony.
- [ ] B. Testing detection of the stale conflict is sufficient, because recovery follows from detection.
- [ ] C. "Deleted from this dictionary" may be reported as "deleted everywhere" once a deletion test passes.
- [ ] D. You also test the opposite decision, where the reviewer rejects the change with a recorded reason.
- [ ] E. You create the stale conflict, pause a dependent fixture, commit the reviewed replacement, and prove the task rereads before resuming.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Without a rejection path, review is only ceremony.
- B: Test recovery, not only detection.
- C: Deleted from this dictionary must not become deleted everywhere.
- D: Rejection must be a real option.
- E: Recovery is tested, not just detection.

**Source:** Ship It: the premortem and the sign-off

## MA-ch12.63

Check each statement that is true about the sign-off. Each statement is worth 1 point (5 points total).

- [ ] A. The "Not checked" line does the work.
- [ ] B. A fluent Claude draft of the sign-off can be signed as written.
- [ ] C. If your evidence does not support signing, withholding is an honest result.
- [ ] D. The contents of "Not checked" must come from your own record, not the template.
- [ ] E. An AI-written sign-off leaves out the "Not checked" line because the system that wrote it has no record of what you did not do.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Its contents come from your record of what you did not do.
- B: Write it from your record.
- C: Claiming more than the record supports repeats the chapter's failure.
- D: The template's items are examples only.
- E: Only you know what you did not check.

**Source:** Ship It: the premortem and the sign-off

## MA-ch12.64

Check each statement that is true about the sign-off template. Each statement is worth 1 point (5 points total).

- [ ] A. Its "Checked" line should list only the behaviors Claude reported as passing.
- [ ] B. Its "Not claiming" example includes that the stale write was rejected.
- [ ] C. Its "Not checked" example says deletion in backups was verified.
- [ ] D. Its "Not checked" example includes contention under real concurrent load because the fixtures are sequential.
- [ ] E. Its "Not claiming" example includes that two sessions agreeing is independent confirmation.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It names behaviors checked by your own tests.
- B: The rejection is something you observed.
- C: Deletion in backups is listed as not checked.
- D: As in the template.
- E: As in the template.

**Source:** Ship It: the premortem and the sign-off

## MA-ch12.65

Check each statement that is true about the first two rows of the driver's-seat table. Each statement is worth 1 point (5 points total).

- [ ] A. Claude should challenge them by proposing the trigger or failure you missed.
- [ ] B. You build your baseline after Claude's implementation arrives.
- [ ] C. Which earlier decision a finding reopens depends on stakes that Claude can state for you.
- [ ] D. Claude should implement the store fast, run your tests, and propose a wrong version that passes.
- [ ] E. You write the record, the revision boundary, and the triggers first and name an owner for each.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Claude's role is to challenge, not author.
- B: You build your own baseline first.
- C: It depends on stakes only you can state.
- D: Speed is Claude's strength; auditing is yours.
- E: Only you can state the stakes behind them.

**Source:** The driver's seat

## MA-ch12.66

Check each statement that is true about the remaining rows of the driver's-seat table. Each statement is worth 1 point (5 points total).

- [ ] A. In parallel research and review you form an initial interpretation before the synthesis and bring context the notes lack.
- [ ] B. In resolving a conflict between proposals you decide: commit, reject with a reason, or leave it unresolved.
- [ ] C. Claude should decide the conflict because it laid out both proposals and their evidence.
- [ ] D. Because two sessions are available, you can skip your own initial interpretation.
- [ ] E. Claude should choose the verbs for what the replay supports and sign it.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Your judgment is not a product of the shared model.
- B: The decision has an owner whose name goes on it.
- C: The decision has a human owner.
- D: Two sessions share a model, prompts, and sources.
- E: You choose the verbs and sign or withhold.

**Source:** The driver's seat

## MA-ch12.67

Check each statement that is true about recording the split between delegation and judgment. Each statement is worth 1 point (5 points total).

- [ ] A. The replay should list only the tasks you delegated.
- [ ] B. A timestamp on the AI summary alone shows when your interpretation was formed.
- [ ] C. You need a transcript line or timestamp showing your initial interpretation came before the AI summary.
- [ ] D. Remembering that you formed your interpretation first is sufficient evidence.
- [ ] E. The incident replay records one task you delegated and one judgment you retained.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: It also records a retained judgment.
- B: You need evidence of your own interpretation's timing.
- C: Otherwise the split happened in your head, not in the record.
- D: The split must be in the record.
- E: The split must be visible in the record.

**Source:** The driver's seat

## MA-ch12.68

Check each statement that is true about how the chapter says to verify the work. Each statement is worth 1 point (5 points total).

- [ ] A. A passing suite establishes universal reliability.
- [ ] B. A passing suite establishes only the tested behavior.
- [ ] C. Verification begins with a claim small enough to test, such as a stale write being rejected or a blank source being refused.
- [ ] D. Preserving commands and outputs is optional once the tests pass.
- [ ] E. A passing suite is permission to act on a record.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: It does not.
- B: Not universal reliability or permission to act.
- C: Small claims are testable.
- D: Preserve the commands, outputs, and your interpretation.
- E: It is not.

**Source:** Verify and reflect

## MA-ch12.69

Check each statement that is true about the words used in the premortem's strongest sentence. Each statement is worth 1 point (5 points total).

- [ ] A. "Rejected" describes an observed exception.
- [ ] B. The premortem may say "verified" as soon as a write is committed.
- [ ] C. To reflect on a rejection, read Claude's explanation first and then paraphrase it.
- [ ] D. "Committed" describes an observed write.
- [ ] E. "Verified" requires a criterion the store never receives.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: It describes what you observed, not a judgment.
- B: Committed does not mean verified.
- C: Explain without reading Claude's explanation.
- D: It describes an observed write, not truth.
- E: No such criterion enters the store.

**Source:** Verify and reflect

## MA-ch12.70

Check each statement that is true about the distinctions the chapter says a learner may have collapsed. Each statement is worth 1 point (5 points total).

- [ ] A. A committed write is the same as a verified claim.
- [ ] B. Rejected is not the same as resolved.
- [ ] C. Attributed is not the same as authenticated.
- [ ] D. Newer is not the same as truer.
- [ ] E. Agreeing is not the same as independent.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: "Committed" is an observed write; "verified" requires a criterion the store never receives.
- B: A rejection leaves the underlying question open.
- C: A source string is not authentication.
- D: Recency does not establish truth.
- E: Agreement can share a cause.

**Source:** Verify and reflect

## MA-ch12.71

Check each statement that is true about the Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. The Lesson 12 knowledge check is answered before reading the feedback.
- [ ] B. In the conflict-reproduction Assessment you may fabricate an agent conversation to dramatize the sequence.
- [ ] C. You preserve predictions, exact commands, outputs, and revisions.
- [ ] D. The knowledge check is a separately graded question bank.
- [ ] E. The Assessments are practice, not graded assignments.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: That keeps it self-review.
- B: Do not fabricate an agent conversation.
- C: Predictions and revisions are the evidence.
- D: It remains self-review.
- E: They are self-review, not grades.

**Source:** Assessments - ungraded practice

## MA-ch12.72

Check each statement that is true about specific Assessments. Each statement is worth 1 point (5 points total).

- [ ] A. In the injection-boundary Assessment you record one remaining attack surface.
- [ ] B. In the expiry-extension Assessment you test a valid record, an expired record, and a malformed time boundary.
- [ ] C. In the fresh-falsehood Assessment you write an incorrect fixture value using the current expected version and explain why acceptance is correct concurrency behavior but insufficient validation.
- [ ] D. In the re-engagement replay Assessment you present the scenario as real.
- [ ] E. In the independent-deliberation Assessment you may invent dissent if the humans all agree.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Boundaries leave residual attack surface.
- B: Three cases test the policy and its edge.
- C: The fixture shows concurrency correctness is not validation.
- D: Label it a simulation unless it happened.
- E: Do not invent dissent.

**Source:** Assessments - ungraded practice

## MA-ch12.73

Check each statement that is true about what the capabilities summary says you did. Each statement is worth 1 point (5 points total).

- [ ] A. Checked: you validated the handoff and the source rather than each worker on its own.
- [ ] B. A stale-write error is a prompt to retry.
- [ ] C. Checked: you counted derived repetitions as one lineage and wrote down what you did not test.
- [ ] D. Conducted: you wrote the record, the revision boundary, and the triggers, each with an owner and a resume condition, before Claude implemented anything.
- [ ] E. Drove: you gave Claude the coordination and the parallel work and kept the initial judgment and the decision.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Checking looks at handoffs and sources.
- B: It is a signal to reopen a human decision.
- C: Checking means counting lineages, not copies, and listing the untested.
- D: Conducting means the gate comes first.
- E: Driving means delegating the work but not the judgment.

**Source:** Capabilities summary

## MA-ch12.74

Check each statement that is true about the Anthropics section. Each statement is worth 1 point (5 points total).

- [ ] A. Claude Code through the course account is enough for the exercise.
- [ ] B. Product architecture and recommendations do not change, so the pages need no revisiting.
- [ ] C. The two Anthropic engineering accounts provide upstream guidance about delegation, coordination, and context management.
- [ ] D. This chapter's Memory class represents Anthropic's internal storage.
- [ ] E. Direct API credits are required for the exercise.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Direct API credits are optional and explicit.
- B: They can change; revisit the primary pages.
- C: They are upstream references for comparison.
- D: Do not infer that.
- E: Claude Code through the course account is enough.

**Source:** Anthropics

## MA-ch12.75

Check each statement that is true about the identity-confusion pattern. Each statement is worth 1 point (5 points total).

- [ ] A. The study is exploratory, so the pattern is something to test for and not a rate.
- [ ] B. A good control is to tag every record with its writer and run.
- [ ] C. The store's source field prevents this pattern because it records who wrote the note.
- [ ] D. In the study, an agent read its own earlier messages in a shared channel and took them for a second instance of itself.
- [ ] E. A worker reading back its own earlier note counts as one outside confirmation.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It is a pattern, not a measured frequency.
- B: A writer-and-run tag lets you detect a worker's own evidence.
- C: A source string is not a writer-and-run tag.
- D: A model can misread its own messages as another instance's.
- E: Count it as zero confirmations.

**Source:** Computational Skepticism

## MA-ch12.76

Check each statement that is true about the Conducting AI diagnostic. Each statement is worth 1 point (5 points total).

- [ ] A. Confirming that each section is internally sound is where checking pays most.
- [ ] B. You should create a trigger for every idle piece of evidence to complete the exercise.
- [ ] C. The diagnostic is to look for evidence that sits in the document and changes nothing.
- [ ] D. In the constructed example, three streams of analysis converged on one site while a fourth, a labor analysis, sat idle until the analyst pulled it back into conflict.
- [ ] E. Evidence that moved nothing is either rightly irrelevant, and you can say why, or a trigger that was available and not pulled.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The seams are where checking pays.
- B: Do not create a trigger to complete the exercise.
- C: Idle evidence suggests a missed reopening.
- D: Convergence of three felt like confirmation while a fourth stream stayed idle.
- E: Both outcomes require you to say which.

**Source:** Conducting AI

## MA-ch12.77

Check each statement that is true about the hidden-profile test and the shared-information bias. Each statement is worth 1 point (5 points total).

- [ ] A. A solo learner may describe two model personas as independent human reviewers.
- [ ] B. If every fact was shared, either nobody held anything private or the synthesis flattened it.
- [ ] C. If every fact was shared, the synthesis is confirmed accurate.
- [ ] D. In the hidden-profile test you mark each fact behind the final decision as shared or held.
- [ ] E. The shared-information bias is groups spending their time on what every member already holds and failing to pool what only one knows.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Two model personas are not two people.
- B: Either explanation requires follow-up.
- C: It may mean the synthesis flattened held information.
- D: Marking exposes what only one person knew.
- E: Groups over-discuss shared knowledge.

**Source:** Irreducibly Human

## MA-ch12.78

Check each statement that is true about the AI should and Human should split. Each statement is worth 1 point (5 points total).

- [ ] A. AI should treat a fresh revision as verified truth.
- [ ] B. Humans should form an initial interpretation before seeing the synthesis.
- [ ] C. AI should label model agreement as human consensus.
- [ ] D. AI should execute bounded research and review tasks, retain source identifiers, compare revisions, and surface conflicts.
- [ ] E. Python should enforce the expected-version rule and preserve reproducible state transitions.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The chapter says AI should not treat a fresh revision as verified truth.
- B: The initial interpretation must predate the synthesis.
- C: The chapter says AI should not label model agreement as human consensus.
- D: These are bounded, checkable tasks.
- E: Deterministic code does the enforcement.

**Source:** Irreducibly Human

## MA-ch12.79

Check each statement that is true about the bridge from Chapter 12 to Chapter 13. Each statement is worth 1 point (5 points total).

- [ ] A. Chapter 13 asks what must happen when even one consequential byte changes.
- [ ] B. Memory gives the next worker permission to rely on the record.
- [ ] C. Chapter 13 moves from proposal identity back to revision identity.
- [ ] D. The premortem and sign-off are left behind in Chapter 13.
- [ ] E. An approval gate is immune to a valid-looking record that says more than anyone checked.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: It asks what happens when even one consequential byte of the evaluated artifact changes.
- B: It gives a record, not permission.
- C: It moves from revision identity to proposal identity.
- D: Carry them forward.
- E: It is another place that can happen.

**Source:** Forward bridge
