# Case-index field guide

This schema is separate from the [technical question schema](../../interview-questions/bank/schema.json). Do not concatenate the files without honoring `record_type` and `track`.

`record_type` is `case_reference`, `local_exercise`, or `historical_learning_prompt`. `id` is stable within a source edition; source revisions are carried in `source.commit` or SHA-256. `canonical_question` is null because this is a reference index, not a licensed prompt bank. `title`/`scenario` are either source titles or short editorial descriptors; `metadata_origin` distinguishes classifications from source assertions. Darden scenarios are null and reasoning skills empty because the case bodies were not reviewed.

`industry`, `case_type`, `reasoning_skills`, `format`, and optional `difficulty` support practice selection. Source difficulty triples are preserved only for Darden. Unknown format is left explicitly unspecified. Kellogg source industry labels can differ from case-title metadata and should not be treated as a universal taxonomy.

`source` provides source ID, URL, local path, content hash, observed timestamp, commit where available, and precise page/line/section locators. All PDF pages are one-based physical PDF page numbers. Darden end pages are inferred; McKinsey original retrieval L-numbers and numbered questions are retained. A source URL with a fragment is a citation, not an indication that an answer is available offline.

`rights.reuse_class` is `reference_only` for every record in this edition. `evidence` distinguishes inspected prompts, detected exhibit/solution markers, uninspected bodies and unavailable answer retrievals. `editorial_answer` is null throughout. `quality_flags` records unresolved ambiguity, historical context, source defects and dependence on earlier context. `duplicate_group_ids` links related variants, which remain separate. A lack of a duplicate group is not proof of originality.
