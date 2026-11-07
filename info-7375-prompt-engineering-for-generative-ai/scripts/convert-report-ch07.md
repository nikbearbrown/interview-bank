# Conversion report: ch07-retrieval-and-cowork (MA-ch07)

- Old MA: 65. Old essay: 60. New MA: 36. Dropped/merged: 29 old MA (calculation/code trivia such as MA-ch07.4, .5 numbers, .9-.11 sort/validation code, .14-.16 metric arithmetic, .38-.39 chunk arithmetic, .59-.60; near-duplicates merged such as .23/.24/.41, .25/.26, .35/.36, .42/.43).
- Essays converted into MA content (vocabulary or term contrasts): ES-ch07.1-2, 6-9, 10, 11, 15, 16-17, 19-20, 22-24, 26-32, 34-36, 38-40, 43-45, 47-49, 53-55, 58, 59-60.
- NOT CONVERTED (calculation, procedure, code or design opinion): ES-ch07.3, 4, 5, 12, 13, 14, 18 (design comparison), 21, 25 (workflow, partly folded into spec/tests question), 33 (spec drafting), 37, 41, 42, 44 (RRF arithmetic; concept kept), 46, 50, 51, 52, 56, 57.

## Retrieval and grounding vocabulary tested
bag of words :: unordered counts of tokens; order discarded
token :: unit a tokenizer produces; need not be a dictionary word
tokenizer :: splits text into tokens
case folding :: lowercasing so capital and lowercase forms merge
term frequency :: count of a term in a document
inverse document frequency :: weight that is higher for terms found in fewer documents
BM25 :: lexical ranking function building on tf-idf with saturation and length normalization
cosine similarity :: dot product divided by vector lengths; angle between vectors
length normalization :: dividing by vector length so long documents do not win on size
lexical retrieval :: matching by shared words
dense retrieval :: matching by meaning using embeddings
embedding :: learned vector representing meaning
vocabulary mismatch :: query and document use different words for the same idea
stemming :: reducing word forms toward a common root
query expansion / synonym map :: adding related terms to the query
query rewriting :: model rewrites the user question into a search query
hybrid search :: combining lexical and dense retrieval
reciprocal rank fusion :: merging ranked lists by rank position
reranking :: reordering candidates with a second model
top-k / cutoff / tie-break :: count limit, score threshold, deterministic ordering rule
audit view :: per-document score and fate listing
precision@k, recall@k, MRR :: share of results relevant, share of relevant found, reward for early first hit
relevance vs entailment :: topical closeness vs logical support
grounding / faithfulness :: claims supported by sources
hallucination :: fluent content unsupported by sources
citation validity vs accuracy :: marker points to a real passage vs passage supports the claim
abstention :: declining to answer when evidence is insufficient
claim decomposition, claim-to-source table, supported/contradicted/insufficient/not reviewed :: evidence review
ingestion, corpus, source manifest, coverage gap :: loading and completeness checks
chunk, chunk overlap :: retrieval unit; repeated text at boundaries
provenance :: record of source and version
context window :: text a model can take in per request
retrieval vs fine-tuning :: change the prompt vs change the weights
access control, indirect prompt injection, least privilege :: security terms
spec, tests first, diff review :: working with a coding assistant
