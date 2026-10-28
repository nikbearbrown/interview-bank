# MBA and case-interview reference track

This addition links useful MBA consulting-case material to the existing interview collection. Start with [CATALOG.md](CATALOG.md). The technical bank remains at 34,850 records; none of these case references were inserted into its question JSONL.

## What was added

- 27 Kellogg 2020 case references: title-page metadata, brief editorial scenarios, page ranges, reasoning concepts, format evidence and defects. Case prompts/interviewer guides were inspected. Solutions were not independently recomputed.
- 5 current McKinsey official practice-case references, containing 17 question sections. The source pages were inspected. Answer reveal controls and image-exhibit links exist, but their bodies/pixels were not captured in browser text retrieval.
- 15 Darden 2024–25 table-of-contents references: titles, industries, types, listed starting pages and source difficulty triples. Case bodies, reasoning skills, exhibits and solutions were not reviewed for this index. The final-page bounds are inferred from the next TOC entry.
- 115 existing local numbered exercises made discoverable, with commit-pinned line citations, short editorial descriptors and quality flags. These span 12 of the book’s 18 core chapters. One is explicitly a behavioral-answer drill. They are not 115 standalone casebook cases.
- 18 existing historical learning prompts in a separate file, not counted as cases.

All 180 records are reference-only. `bank/licensed-reuse-candidates.jsonl` is intentionally empty. No exercise prompts, solution bank or invented answers are reproduced in the consolidated index. Scenario descriptors help select a source; they are not complete practice prompts.

## Files

- [All records](bank/case-index.jsonl), [47 case references](bank/cases.jsonl), [115 local drills](bank/local-exercises.jsonl), [18 historical prompts](bank/historical-learning.jsonl)
- [Schema](bank/schema.json) and [field guide](SCHEMA.md)
- [Source manifest](provenance/source-manifest.json), [counts](provenance/statistics.json), [local file ledger](provenance/local-file-ledger.jsonl), [attachment receipt](provenance/attachment-receipt.json)
- [Related variants](bank/duplicate-groups.jsonl), [QA](QA.md), [sample receipts](provenance/qa.json), [checkpoint](provenance/checkpoint.json)
- [Additions and exclusions](ADDITIONS-AND-EXCLUSIONS.md), [general bank](../../interview-questions/CATALOG.md)

## Rights and provenance

Kellogg’s p.289 notice limits distribution to its club and requires permission for reproduction. Darden’s p.3 notice identifies proprietary material and explicitly includes AI-tool use in its restriction. Accordingly, Darden contributes only identifying TOC metadata; the collection is not a republished casebook. The two original PDFs are retained privately under `sources/` with URLs, retrieval timestamps, byte counts and SHA-256 hashes. Do not bundle those PDFs or their contents into public sites or exports without rights review. Public availability at an aggregator is not a reuse license or proof that the aggregator has redistribution permission.

The local `mba-case-studies/LICENSE.md` reserves rights to Humanitarians AI Incorporated. Its source content is referenced at the existing repository’s verified commit and exact line range. The older `case-crackers-with-llms` draft has no separately located license. `Case_Interviews/LICENSE` is CC0, but its notes include third-party book excerpts; CC0 does not establish rights to those excerpts. No items were imported from either companion repository.

McKinsey pages are official practice resources, not established open-license material. Direct downloads from this Mac timed out; successful browser text-retrieval receipts are retained instead. This is a partial text snapshot, not an offline interactive copy. The official URLs remain the source for diagrams and revealable answers. There was no access-denial bypass, sign-in, payment or downloaded-code execution.

## Extraction and deduplication

The attachment was materialized with the supported consumer-local Library helper, verified at 5,860 bytes, and read in full. It is a source guide, not a repository list. PDF metadata and case locations came from inspected contents/title/prompt pages using PyMuPDF; selected pages were rendered and visually checked. Local drills were parsed only inside explicit `## Exercises` sections, preserving decimal labels, multiline tables, lettered subparts and chapter context in source references. Historical prompts were found only under `## AI Wayback Machine`.

Stable IDs use source edition plus case number, or repository/chapter plus original exercise label. Source hashes and commits version the evidence separately. The parser found no exact normalized duplicate local drills. Three manually identified related groups retain their distinct numbers, scenario metrics, response constraints and analytical goals. Generated mirrors, drafts and references to “similar cases” do not become additional cases. No claim is made that near-duplicate detection is exhaustive across editions or uninspected books.

## Gaps and quality limits

This is a focused addition, not an exhaustive download of all books mentioned in the attachment. Its other named schools, firms and historical case titles remain leads in the exclusions document. The current McKinsey index surfaced five cases; the attachment’s sixth, GlobaPharm, was not on that page. Kellogg contains 27 cases; its separate study curriculum lists 25. Its edition explicitly removed subjective difficulty ratings. Darden’s 15 are TOC entries, not 15 independently validated solved cases.

Local chapter 14 uses exercise labels 15.1–15.6 and ambiguous relative-share percentages; exercise 15.5 asks for relative share without a competitor denominator. Firm-format and scoring claims in chapter 17 need current verification. Historical prompts’ biographical and causal claims are unverified. Kellogg has copied/incomplete sentences and older economic contexts; specific flags accompany affected records. Source answer guidance is not an endorsement of correctness.

No local dedicated exercise answer key was found. No editorial solutions were generated. Darden answers remain uninspected; McKinsey answer bodies remain uncaptured; Kellogg solution calculations remain unvalidated. Image-only details were not OCRed. There is no artificial expansion into transformers, AI agents, observability or blast-radius topics: this track covers business reasoning supported by these sources, including a small amount of data-quality/ML-asset analysis and Beautify’s AI-chatbot exhibit question.

## Resume

Read `provenance/checkpoint.json` and compare hashes before retrying after a disconnect. `scripts/compile_mba_index.py` and `scripts/mba_metadata.py` are the agent-authored compiler/metadata, saved for audit. The compiler was run from the recorded task workspace with staged inputs; do not run repository scripts. Existing repositories and technical bank snapshots remain untouched. No website integration or publication was performed.
