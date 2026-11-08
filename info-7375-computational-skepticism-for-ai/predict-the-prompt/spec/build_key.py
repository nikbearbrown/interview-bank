import json,sys
sys.path.insert(0,"spec"); import spec
A=json.load(open("spec/analysis.json")); FQ=A["freq"]; AG=A["agree"]
def band(n): p=n/10; return "L" if p>=.7 else ("U" if p<.2 else "P")
o=[]; w=o.append
w("""# KEY-AND-RUNS: configuration, features, frequencies, coder agreement

Pilot built 2026-11-08. Everything here comes from the files in `runs/`.

## Configuration

| Item | Value |
|---|---|
| Model that wrote the plans | `claude-sonnet-5-5` (sub-agent, alias `sonnet`; each sub-agent reported that id) |
| How plans were requested | One fresh sub-agent per prompt version. It read the prompt from a text file, wrote **10 separate attempts** in one go, told not to compare attempts, and saved a JSON array with a single Write. No data, no code execution, no iteration. **This is a sub-agent plan, not an agent harness.** |
| Prompt template | "You are a data analyst on a small team. Write the analysis plan for the task below. Format: a numbered list of at most 8 steps, one or two sentences each, no code, no preamble, no closing remarks. Task: ..." See `spec/spec.py` |
| Date | 2026-11-08 |
| Runs | 5 families x 4 versions x 10 plans = **200 plans**. Plus 10 plans for the repair demo. F4 version A: the sub-agent returned 9 plans; the tenth is from a separate fresh sub-agent (`F4A-10`). |
| Sampling settings | Defaults of the sub-agent runtime. Temperature is not controllable here and was not recorded. |
| Coder 1 | `sonnet` sub-agent per family, blind to which prompt wrote each plan (ids shuffled, variant hidden), codes all 40 plans on binary features. |
| Coder 2 | Separate `sonnet` sub-agent per family, blind, recodes 8 of the 40 plans (2 per version, random). 40 plans = 20% of 200. |
| Key rule | Observed count out of 10: LIKELY >= 7, PLAUSIBLE 2 to 6, UNLIKELY <= 1. (Matches 70% / 20-70% / below 20%, on a 10-plan sample: 2/10 = 20% is PLAUSIBLE.) |

### Known limits (read before trusting a number)

1. **The 10 plans of a version come from one sub-agent context**, so they are not 10 independent draws; they may be more varied or less varied than 10 separate calls. Single-plan sub-agents cost about 70k tokens each (about 14M tokens for 200), so I batched. A full version should sample independently (API calls, not sub-agents).
2. **Coders are the same model family as the writer.** Both coders are `sonnet`; agreement shows consistency, not truth. A human spot check of the 8 disagreements is advisable.
3. **Ten plans per cell**: a count of 5/10 has a 95% interval of roughly 2 to 8. Band edges (2 and 7) are within noise for borderline counts.
4. **The key is about this model on this day**. It will drift with model versions.

## Features per family (defined before sampling)

S = semantic (follows from what the words mean); B = behavioral (habit of the model, weighted half).
""")
for f,F in spec.FAMILIES.items():
    w(f"### {f}: {F['name']}\n\nTask: {F['task'].split(' Your job')[0]} Your job: ___\n")
    w("Versions: "+"; ".join(f"**{v}** {p}" for v,p in F["variants"].items())+"\n")
    w("| Feature | Definition | Type |\n|---|---|---|")
    for x,(d,t) in F["features"].items(): w(f"| {x} | {d} | {'S' if t=='S' else 'B'} |")
    w("")
w("## Frequencies (plans of 10 containing the feature)\n\nBand: L likely, P plausible, U unlikely.\n")
for f,F in spec.FAMILIES.items():
    w(f"### {f}: {F['name']}\n")
    w("| Version | Prompt phrase | "+" | ".join(f"{x} ({F['features'][x][1]})" for x in F["features"])+" |\n|---|---|"+"---|"*len(F["features"]))
    for v in "ABCD":
        w(f"| {v} | {F['variants'][v]} | "+" | ".join(f"{FQ[f][v][x]} {band(FQ[f][v][x])}" for x in F["features"])+" |")
    w("")
w("## Coder agreement (second coder recoded 8 plans per family)\n\n| Family | Cells | Agreement | Cohen's kappa | Disagreements (plan, feature, coder 1, coder 2) |\n|---|---|---|---|---|")
tc=ta=0
for f in spec.FAMILIES:
    a=AG[f]; tc+=a["cells"]; ta+=a["agree"]
    w(f"| {f} | {a['cells']} | {a['agree']}/{a['cells']} = {a['pct']:.1%} | {a['kappa']:.2f} | "+("; ".join(f"{r} {x} ({p},{q})" for r,x,p,q in a["disagreements"]) or "none")+" |")
w(f"\n**Overall: {ta}/{tc} cells agree = {ta/tc:.1%}.** Disagreements are all on a single feature in a single plan; none changes a band at 10 plans except where noted below. Coder 1 is used for all frequencies; no adjudication was done. Note the kappa is computed on a small sample with many always-present features, so treat it as indicative only.\n")
w("""Effect of disagreements on bands: F1C-02 and F1C-06 (feature a, reliability diagram, 'discrimination' prompt): coder 2 says 0 where coder 1 says 1. If coder 2 is right the count falls from 5/10 to 3/10, still PLAUSIBLE. F3C-07, F3C-09 and F3B-01 (feature d, randomization): if coder 2 is right, 'randomize coffee assignment' drops from 6/10 to 4/10 (still PLAUSIBLE) and 'collect more rows' from 4/10 to 3/10 (still PLAUSIBLE). F2C-02 (feature a) and F5B-08 (feature e, behavioral): no band change.

## Premise check: do altered prompts give different profiles?

A pair of prompt versions is *distinguishable* if some **semantic** feature differs by at least 4 plans of 10. Result:

| Family | Indistinguishable pairs (cut) | Weakly distinguishable | Clean |
|---|---|---|---|
| F1 calibration | A=B=D (calibration, accuracy, overconfidence) | none | C (discrimination) vs the rest |
| F2 holdout | A=B (hold out vs cross-validate) | none | the rest |
| F3 confounder | none | A vs C (only randomization, 0 vs 6); A vs D (only collider, 3 vs 10) | B vs everything |
| F4 provenance | A=C (provenance = lineage) | B vs D (only checksum 9 vs 0) | A vs B, A vs D, B vs C, C vs D |
| F5 shift | none | A vs B (only fraud rate, 0 vs 4); B vs D (4 vs 0) | C vs everything; A vs D (domain classifier 10 vs 5) |

Cuts: the F1 'calibration vs accuracy' item, the F2 'hold out vs cross-validate' item, the F4 'provenance vs lineage' item. Pairs were kept in items only when listed as clean or flagged weak in the item key.

### Features that fire in every version (cannot discriminate)
F4 c, d, f; F5 c; F1 e and f in versions A, B, D. These are listed in the tables above but are used in no item.

## Repair demo

Prompt F1B ('check the accuracy of the predicted probabilities') plus the sentence "Report accuracy at a 0.5 threshold, not calibration." (9 words). 10 plans in `runs/F1B_repair_demo.json`, coded by one blind coder (not double-coded): c (accuracy at threshold) **10/10**, a (reliability diagram) 0/10, b (calibration number) 0/10, d (ROC/AUC) 0/10.

## Cost, in runs

| Step | Sub-agents | Approx tokens |
|---|---|---|
| Probe (1 single-plan agent, discarded) | 1 | 70k |
| Sampling 200 plans | 20 (+1 extra plan for F4A) | about 1.5M |
| Coding | 10 | about 0.8M |
| Repair demo (sampler, an extra 2-plan sampler by mistake, coder) | 3 | about 0.2M |
| **Total** | **35** | **about 2.6M** |

## Files

- `runs/F1.json` to `runs/F5.json`: 40 plans each, with the full prompt text, model, date.
- `runs/F1B_repair_demo.json`: repair-protocol demo.
- `spec/spec.py` (families, versions, features), `spec/analysis.json` (codes, frequencies, agreement), `spec/analyze.py`, `spec/build_docs.py`, `spec/build_key.py`.
""")
open("KEY-AND-RUNS.md","w").write("\n".join(o))
