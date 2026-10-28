# 7. Programming languages vs language models

## ES-7.1

Contrast a programming language with a language model on three points: how input is interpreted, whether output is deterministic, and how errors show up. State the key nuance about where an LLM runs.

**Points:** 5

**Rubric (1 point each):**

1. Programming language input is a formal grammar interpreted exactly; a language model takes ambiguous natural language.
2. Programs are deterministic for the same input; language model outputs are sampled and can vary at T > 0.
3. Program errors are explicit; language model errors are silent and fluent.
4. States that an LLM is itself a program doing arithmetic on CPUs/GPUs.
5. Explains that the difference is how the instruction is interpreted: executed exactly vs used as context for prediction.

