# Quality checks

Validated 34,850 records and 2,447 downloaded source files (237,283,424 bytes).

All 66 sampled question locators matched the saved source text after the documented normalization. Samples span every repository contributing records. See [sample receipts](provenance/qa-samples.json).

Known-wrong source answers: **1,304 records**. Same prompt with distinct code/image context: **58 groups**, preserved as variants.

## Checks

- unique_ids: True
- statistics_agree: True
- licensed-reuse-candidates_count: True
- reference-only_count: True
- all_sample_locators_match: True
- inline_code_preserved: True
- full_primary_dataset_extracted: True
- parquet_questions_and_followups: True
- react_main_bank_coverage: True
- no_career_advice_index_prompts: True
- context_variants_preserved: True

## Human sample review

Sample review identified and corrected Unicode JSONL splitting, an unmatched React Markdown fence, false questions from contribution/career guidance, accidental substring topic matches, stripped inline code, and context-blind duplicate merging. This review does not certify every source answer or every taxonomy assignment.

Near-duplicate suggestions remain unmerged and unreviewed. Source answers and teaching headings remain explicitly unverified. Automated classification can still require correction.
