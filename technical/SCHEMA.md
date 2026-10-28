# Field guide

One JSON object per UTF-8 line. `id` is stable for a normalized prompt/options/context combination. `sources` retains every exact-match occurrence; `locator.row` is one-based data-row indexing, `locator.line` is one-based text-line indexing, `notebook_cell` is zero-based, `pdf_page` is one-based, workbook locations use sheet/cell, and Anki locations use note IDs.

`canonical_question` is null for reference-only material. `display_label` then supplies topic and location. `question_text_status` distinguishes normalized source wording, editorial title adaptations, and rights-withheld text. `question_context_fingerprint` prevents materially different code/image variants from merging. Source-specific question hashes allow audit without copying withheld text.

`source_answers` contains unverified source context or external references, not editorial truth. `source_correctness_label` preserves explicit dataset labels. `status: source_marked_wrong` must never be treated as a correct answer. `editorial_answer` is null; no unsupported answer key was invented.

`rights_class` and `license_attribution` are per-record/source assessments based on declarations. They do not grant new rights. `flags`, `ambiguity_flags`, and `outdated_flags` preserve uncertainties. `relevant_roles` and taxonomy are inferred and require review for high-stakes use.

Categories distinguish technical, behavioral, case, and professional-skill-assessment material. A scenario question can remain technical; a case-study section is classified as case. General skills are included because they occur in the supplied assessment source. Near-duplicate groups are suggestions, not merges.


<!-- mba-case-track-v1 -->
## MBA and case-interview track

A separate [case-interview catalog](../case-interviews/case-bank/CATALOG.md) now indexes 47 case references (including 15 Darden TOC-only entries), 115 existing local exercises, and 18 historical learning prompts. These reference-only records do not change the technical bank counts. See its [schema](../case-interviews/case-bank/SCHEMA.md), [rights and limitations](../case-interviews/case-bank/README.md), and [QA](../case-interviews/case-bank/QA.md).
