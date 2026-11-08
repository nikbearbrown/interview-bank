import json,sys,random
sys.path.insert(0,"spec"); import spec
A=json.load(open("spec/analysis.json")); C=A["codes"]; FQ=A["freq"]
R={f:{r["id"]:r for r in json.load(open(f"runs/{f}.json"))["runs"]} for f in spec.FAMILIES}
rep=json.load(open("runs/F1B_repair_demo.json"))
random.seed(11)
def band(n): p=n/10; return "LIKELY" if p>=.7 else ("UNLIKELY" if p<.2 else "PLAUSIBLE")
def task(f,v): return spec.FAMILIES[f]["task"].format(P="**"+spec.FAMILIES[f]["variants"][v]+"**")
def phrase(f,v): return spec.FAMILIES[f]["variants"][v]
def fd(f,x): return spec.FAMILIES[f]["features"][x][0]
def sem(f,x): return "semantic" if spec.FAMILIES[f]["features"][x][1]=="S" else "BEHAVIORAL"
def backing(f,v,x): return ", ".join(i for i in R[f] if i.startswith(f+v+"-") and C[f][i][x]) or "none"
def freqline(f,x,vs="ABCD"): return "; ".join(f"{v} ({phrase(f,v)}): {FQ[f][v][x]}/10" for v in vs)
def plan(pid): return "\n".join("> "+l if l.strip() else ">" for l in R[pid[:2]][pid]["plan"].strip().splitlines())
def prof(pid): f=pid[:2]; return "".join(x for x in "abcdef" if C[f][pid][x])
out=[]
w=out.append
w("""# INFO 7375 Computational Skepticism: Predict-the-Prompt exam (PILOT DRAFT)

**Status: draft for Bear to look at. Not run on students. Not committed.** Built 2026-11-08.

## How this exam works

Every question shows a prompt (or a plan) and asks what an AI analyst will do. The answer key is **not an opinion**: each prompt was sampled 10 times and the key is the observed frequency of each feature in those 10 plans. Features are grouped into bands: **LIKELY** (7 to 10 of 10), **PLAUSIBLE** (2 to 6 of 10), **UNLIKELY** (0 or 1 of 10).

All prompts have the same shape, and only the final "Your job" phrase changes between versions of a prompt:

> You are a data analyst on a small team. Write the analysis plan for the task below. Format: a numbered list of at most 8 steps, one or two sentences each, no code, no preamble, no closing remarks.
> Task: *(a short fixed dataset description)* Your job: **(the phrase that varies)**.

The "plans" are numbered analysis plans written by `claude-sonnet-5-5` run as a **sub-agent** (not an agent harness: no tools, no data, no iteration). The key is true for that model, that format, on 2026-11-08. It is a statement about what the model does, not about what a good analyst does. See `KEY-AND-RUNS.md` for configuration, feature definitions and coder agreement.

Items marked **[behavioral]** key on a habit of the model rather than something that follows from the words, and count half. Everything else is **semantic**: it follows from what the course vocabulary means.

Answer keys follow each question in a **KEY** block (strip these for a student copy). Plan ids like `F3B-06` mean family 3, variant B, run 06; the raw text is in `runs/F3.json`.

---
""")
# ---------- Section 1 matching (F3)
w("## 1. Matching: 4 prompts to 4 plans (4 points)\n")
w("**Task (shared):** "+spec.FAMILIES["F3"]["task"].split("Your job:")[0].strip()+"\n")
w("Four prompts differ only in the final phrase. Four plans (X to Z, W), each written for a different one of the prompts. Match each prompt to its plan (1 point each).\n")
picks={"A":"F3A-09","B":"F3B-06","C":"F3C-06","D":"F3D-06"}
order=list("ABCD"); random.shuffle(order)
labels=["W","X","Y","Z"]; plmap=dict(zip(order,labels))  # variant->label
nums={v:i+1 for i,v in enumerate("ABCD")}
shufp=list("ABCD"); random.shuffle(shufp)  # prompt display order
pnum={v:i+1 for i,v in enumerate(shufp)}
for v in sorted("ABCD",key=lambda v:pnum[v]): w(f"- **Prompt {pnum[v]}:** Your job: {phrase('F3',v)}.")
w("")
for lab in labels:
    v=[k for k,l in plmap.items() if l==lab][0]
    w(f"**Plan {lab}**\n\n{plan(picks[v])}\n")
w("### KEY\n")
w("Answer: "+", ".join(f"Prompt {pnum[v]} = Plan {plmap[v]}" for v in sorted("ABCD",key=lambda v:pnum[v]))+".\n")
w("What separates them (observed in 10 plans per prompt, semantic features):\n")
w("| Feature | control for the confounder | collect more rows | randomize coffee assignment | check for a collider |\n|---|---|---|---|---|")
for x in "abcde": w(f"| {fd('F3',x)} | "+" | ".join(f"{FQ['F3'][v][x]}/10" for v in "ABCD")+" |")
w("\nBacking plans: "+"; ".join(f"{phrase('F3',v)} -> {picks[v]} (features present: {prof(picks[v])})" for v in "ABCD")+".\n")
w("Caution for the instructor: prompts 'control for the confounder' and 'randomize coffee assignment' share the same profile except randomization (0/10 vs 6/10). The matching rests on that one feature, so the plan chosen for 'randomize' is one that shows it (F3C-06). Weak pair; swap if you want a cleaner item.\n\n---\n")
# ---------- Section 2 MC
w("## 2. Prompt to most likely plan: multiple choice (2 points each)\n")
w("For each prompt, choose the plan that the model is most likely to write. Each option is a real plan the model wrote for a different version of the prompt.\n")
mcs=[("F3","B",{"A":"F3A-10","B":"F3B-02","C":"F3C-05","D":"F3D-09"},"c","M1"),
     ("F5","C",{"A":"F5A-06","B":"F5B-06","C":"F5C-06","D":"F5D-06"},"d","M2"),
     ("F2","D",{"A":"F2A-05","B":"F2B-07","C":"F2C-08","D":"F2D-06"},"d","M3")]
for k,(f,v,pk,x,name) in enumerate(mcs,1):
    w(f"### Q2.{k}\n\n**Task:** "+task(f,v)+"\n")
    o=list("ABCD"); random.shuffle(o); lm=dict(zip(o,"ABCD"))  # variant->option letter
    for L in "ABCD":
        vv=[a for a,b in lm.items() if b==L][0]
        w(f"**Option {L}**\n\n{plan(pk[vv])}\n")
    w("### KEY\n")
    w(f"**Answer: Option {lm[v]}** (the plan written for this prompt).\n")
    w(f"Deciding feature: *{fd(f,x)}* ({sem(f,x)}). Frequency across 10 plans per prompt version: {freqline(f,x)}.\n")
    w("Options: "+"; ".join(f"Option {lm[a]} = {pk[a]} (written for '{phrase(f,a)}')" for a in "ABCD")+".")
    w("Backing plans for the key feature: "+backing(f,v,x)+".\n")
    if name=="M2": w("Note: 4 of 10 plans for 'concept drift' also compare fraud rates (F5B). The distractor from that prompt was chosen from the 6 that do not, so the item is solvable, but a careful student can say 'concept drift' produces the feature 40% of the time and 'label shift' 100%.\n")
    if name=="M3": w("Note: options A-type ('hold out a test set') and B-type ('cross-validate') have the same profile (see cut list), so the item keys on the time split, which only the 'most recent 3 months' prompt produces (10/10 vs 0 to 3/10).\n")
    w("")
w("---\n")
# ---------- Section 3 plausibility
w("## 3. Plausibility: likely, plausible or unlikely? (1 point; adjacent band 0.5)\n")
w("For each prompt, say whether the statement about the plan is LIKELY (7+ of 10 plans), PLAUSIBLE (2 to 6) or UNLIKELY (0 to 1). Quote the phrase in the prompt that drives your answer.\n")
pl=[("F2","D","x","d","The plan splits train and test by time, earlier months for training, later for test."),
    ("F3","B","x","a","The plan adjusts for smoking."),
    ("F3","B","x","d","The plan proposes a randomized experiment."),
    ("F1","C","x","b","The plan computes a calibration number (ECE, Brier score or calibration slope)."),
    ("F4","B","x","a","The plan asks who collected the data and under what consent or licence."),
    ("F5","D","x","b","The plan trains a classifier to tell 2023 rows from 2025 rows, or estimates importance weights."),
    ("F1","B","x","c","The plan computes accuracy or a confusion matrix at a probability threshold.")]
for k,(f,v,_,x,st) in enumerate(pl,1):
    w(f"**Q3.{k}.** Prompt: *\"Your job: {phrase(f,v)}\"* (task: "+spec.FAMILIES[f]["task"].split(" Your job")[0].strip()+")\n\nStatement: {st}\n")
w("### KEY\n")
w("| Q | Quoted phrase | Statement feature | Observed | Band | Type | Backing plans | Other versions of the prompt |\n|---|---|---|---|---|---|---|---|")
for k,(f,v,_,x,st) in enumerate(pl,1):
    n=FQ[f][v][x]
    w(f"| 3.{k} | \"{phrase(f,v)}\" | {fd(f,x)} | {n}/10 | {band(n)} | {sem(f,x)} | {backing(f,v,x)} | "+", ".join(f"{u}:{FQ[f][u][x]}" for u in "ABCD")+" |")
w("""
Two teaching points hidden in this section. Q3.2: 'collect more rows' still produces smoking adjustment 10/10, because the task text names the confounder: **the scenario drives the plan, the phrase shifts its emphasis**. Q3.7: 'check the accuracy of the predicted probabilities' produces **zero** accuracy-at-threshold steps: the model reads accuracy-of-probabilities as calibration (see predict-and-explain 6.2).

---
""")
# ---------- Section 4 forecasting
w("## 4. Feature forecasting: how many of 10 plans? (2 points; behavioral item 1 point)\n")
w("Give a number from 0 to 10. Scoring: within 1 of the observed count = full credit; otherwise right band (LIKELY / PLAUSIBLE / UNLIKELY) = half credit; else 0.\n")
fc=[("F1","C","a"),("F3","C","d"),("F5","B","d"),("F5","D","b"),("F2","D","f")]
for k,(f,v,x) in enumerate(fc,1):
    tag=" **[behavioral]**" if sem(f,x)=="BEHAVIORAL" else ""
    w(f"**Q4.{k}.**{tag} Prompt: *\"Your job: {phrase(f,v)}\"* (task: "+spec.FAMILIES[f]["task"].split(" Your job")[0].strip()+f")\n\nOf 10 plans, how many will include: *{fd(f,x)}*?\n")
w("### KEY\n")
w("| Q | Feature | Observed (of 10) | Band | Full-credit range | Type | Backing plans |\n|---|---|---|---|---|---|---|")
for k,(f,v,x) in enumerate(fc,1):
    n=FQ[f][v][x]
    w(f"| 4.{k} | {fd(f,x)} | **{n}** | {band(n)} | {max(0,n-1)} to {min(10,n+1)} | {sem(f,x)} | {backing(f,v,x)} |")
w("\nThese are mid-band items on purpose: a feature the model produces 10 times out of 10 tests vocabulary, but only a mid-band feature tests whether the student can judge how strongly a phrase pulls. Caution: a count of 5 or 6 from 10 plans has a standard error near 1.6, so the full-credit range is about one standard error wide.\n\n---\n")
# ---------- Section 5 attribution
w("## 5. Attribution: which prompt wrote this plan? (2 points)\n")
w("Given the plan, name the prompt most likely to have produced it (all four prompts share the same task). Give your reason in one sentence.\n")
at=[("F2","F2C-07","Q5.1"),("F5","F5B-09","Q5.2")]
for f,pid,q in at:
    w(f"### {q}\n\n**Task:** "+spec.FAMILIES[f]["task"].split(" Your job")[0].strip()+" Your job: ___\n")
    for v in "ABCD": w(f"- Prompt {v}: {phrase(f,v)}")
    w(f"\n{plan(pid)}\n")
w("### KEY\n")
# Q5.1
w("""**Q5.1: answer C, 'use nested cross-validation'** (the true source is F2C-07). Nested cross-validation / an inner tuning loop appears in 10/10 plans for C and in 0/10 (A), 2/10 (B) and 0/10 (D) for the others. Likelihood ratio favours C over B 5 to 1; posterior (equal prior) about 83%.

**Q5.2: answer C, 'check for label shift' is the most probable source, but the true source is B, 'check for concept drift'** (F5B-09). Using the four semantic features: this plan compares feature distributions (a), trains a domain classifier (b), measures performance on the labelled 2025 weeks (c) and compares the fraud rate (d). Fraud-rate comparison appears in 10/10 label-shift plans, 4/10 concept-drift plans and 0/10 for 'covariate shift' and 'drift'; the domain classifier appears 10/10 (A), 7/10 (B), 10/10 (C), 5/10 (D). Likelihood for C is 1.0 x 1.0, for B 0.7 x 0.4 = 0.28, for A and D 0. Posterior (equal prior): C 78%, B 22%. Award full credit for C with a reason that cites the fraud-rate step, and ALSO full credit for B if the student shows the 22% reasoning; this item is meant to teach that attribution is a probability, not a verdict.
""")
w("Backing plans: nested CV: "+backing("F2","C","c")+". Fraud-rate comparison under label shift: "+backing("F5","C","d")+"; under concept drift: "+backing("F5","B","d")+".\n\n---\n")
# ---------- Section 6 predict and explain
w("## 6. Predict and explain (4 points each: 2 prediction, 2 mechanism)\n")
w("Before seeing any plan, (a) predict which of the listed features the plan will contain and which it will not, and (b) explain **which word or phrase in the prompt** causes each difference you predict.\n")
w("### Q6.1\n\n**Task:** "+task("F3","B")+"\n\nFeatures to judge: (i) adjusts for smoking; (ii) draws a causal diagram or lists causal assumptions; (iii) proposes a larger sample or discusses power; (iv) proposes a randomized experiment.\n")
w("### Q6.2\n\n**Task:** "+task("F1","B")+"\n\nFeatures to judge: (i) reliability diagram / binning predicted vs observed; (ii) a calibration number (ECE, Brier, slope); (iii) accuracy or confusion matrix at a threshold; (iv) ROC / AUC.\n")
w("### KEY\n")
w("**Q6.1** observed: (i) "+f"{FQ['F3']['B']['a']}/10"+" (ii) "+f"{FQ['F3']['B']['b']}/10"+" (iii) "+f"{FQ['F3']['B']['c']}/10"+" (iv) "+f"{FQ['F3']['B']['d']}/10"+f". For comparison with 'control for the confounder': (i) {FQ['F3']['A']['a']}/10, (ii) {FQ['F3']['A']['b']}/10, (iii) {FQ['F3']['A']['c']}/10, (iv) {FQ['F3']['A']['d']}/10. Backing: (i) {backing('F3','B','a')}; (iii) {backing('F3','B','c')}; (iv, 4/10) {backing('F3','B','d')}.\n")
w("""Mechanism, full credit needs both halves: (1) smoking adjustment is **context-driven**: the task text says smoking is suspected of being associated with both, so the plan controls for it even though the prompt says to collect more rows; (2) the sample-size/power step is **phrase-driven** ('collect more rows') and the causal diagram is **phrase-driven** the other way: 'control for the confounder' calls up the causal vocabulary (diagram 9/10) and 'collect more rows' does not (0/10). Randomization is plausible (4/10), not likely. A student who predicts 'it will ignore smoking because the prompt only asked for more rows' loses the prediction points; a student who predicts a causal diagram loses them too.
""")
w(f"**Q6.2** observed for 'accuracy of the predicted probabilities': (i) {FQ['F1']['B']['a']}/10 (ii) {FQ['F1']['B']['b']}/10 (iii) {FQ['F1']['B']['c']}/10 (iv) {FQ['F1']['B']['d']}/10. For 'calibration': (i) {FQ['F1']['A']['a']}, (ii) {FQ['F1']['A']['b']}, (iii) {FQ['F1']['A']['c']}, (iv) {FQ['F1']['A']['d']}. For 'discrimination': (i) {FQ['F1']['C']['a']}, (ii) {FQ['F1']['C']['b']}, (iii) {FQ['F1']['C']['c']}, (iv) {FQ['F1']['C']['d']}. Backing (i)+(ii) under 'accuracy': {backing('F1','B','a')}.\n")
w("""Mechanism: the model reads *accuracy of the predicted probabilities* as **calibration**, because a probability is 'accurate' to the extent that events predicted at 30% happen about 30% of the time. The plan for 'accuracy' is the same as the plan for 'calibration' and for 'overconfidence' (reliability diagram and calibration number both 10/10, confusion matrix 0/10). Only 'discrimination' moves the plan to ROC/AUC (10/10) and a threshold metric (7/10). Full credit: predicts reliability diagram, no confusion matrix, and says the word *probabilities* decides it. A student who has memorised 'accuracy is not calibration' as a vocabulary fact will predict the confusion matrix and be wrong, which is exactly what this item is for: the model's reading is the *right* reading of that phrase, and the vague phrase in the prompt was the student's.

---
""")
# ---------- Section 7 repair
w("## 7. Minimal-edit repair (3 points, graded by running)\n")
w(f"**Prompt as it stands:** {task('F1','B')}\n\nObserved: 10/10 plans build a reliability diagram and a calibration number; **0/10** compute accuracy or a confusion matrix at a threshold. You want a plan that reports **classification accuracy at a probability threshold**. Add or change **at most 12 words** to the prompt (do not delete the task description) so that at least 7 of 10 plans do.\n")
w("### KEY and run protocol\n")
n=rep["freq"]
w(f"""**Reference edit (9 words, appended):** *"Report accuracy at a 0.5 threshold, not calibration."* Run result, 10 plans: accuracy/confusion matrix at threshold **{n['c']}/10** (was 0/10); reliability diagram {n['a']}/10 (was 10/10); calibration number {n['b']}/10 (was 10/10). Plans: `runs/F1B_repair_demo.json`.

**Run protocol for grading a student edit:**
1. Check the edit is at most 12 words and the original task sentence is intact. If not, 0.
2. Run the edited prompt 10 times in 10 fresh contexts with the same sampler (here: a fresh sub-agent per batch, 10 separate attempts, `claude-sonnet-5-5`, no tools).
3. A blind coder (not told the student's edit) marks feature c ('accuracy-style metrics at a probability threshold') in each plan using the definition in `KEY-AND-RUNS.md`.
4. Score: **7 to 10 plans = 3 points; 4 to 6 = 1.5; 0 to 3 = 0.** Feature c must be present; the student need not suppress the calibration plan.
5. Cost: one batch plus one coding pass per student answer, about 150k tokens. For a class, grade a random 20% of edits by running, and pre-run the 5 most common edits.
6. The pass threshold is a prediction made *before* running: the student may also be asked to state the expected count, and gets the +0.5 bonus if within 1.

---
""")
w("## 8. Scoring summary\n\n| Section | Items | Points each | Total |\n|---|---|---|---|\n| 1 Matching | 4 pairs | 1 | 4 |\n| 2 Most likely plan | 3 | 2 | 6 |\n| 3 Plausibility | 7 | 1 | 7 |\n| 4 Forecasting | 5 (1 behavioral at half) | 2 | 9 |\n| 5 Attribution | 2 | 2 | 4 |\n| 6 Predict and explain | 2 | 4 | 8 |\n| 7 Repair | 1 | 3 | 3 |\n| **Total** | | | **41** |\n")
w("""## 9. Items cut by the premise check

An item was cut when altered versions of the prompt produced the same feature profile (no semantic feature differing by 4 or more plans of 10). Full detail in `KEY-AND-RUNS.md`.

- **Calibration vs accuracy (family 1): cut.** 'calibration', 'accuracy of the predicted probabilities' and 'overconfidence' produced identical profiles (all semantic features within 0 plans of each other). The planned 'calibration vs accuracy' item cannot be keyed. Kept as predict-and-explain 6.2 and plausibility 3.7 *because* the failure is informative. Only 'discrimination' differs.
- **Hold out a test set vs cross-validate (family 2): pair cut.** The two prompts differ by at most 1 plan on every semantic feature. Both write a held-out test set plus k-fold tuning. Items use 'nested' and 'most recent 3 months' instead.
- **Provenance vs lineage (family 4): pair cut.** Identical profiles (10/10 on provenance questions, chain of custody and processing history for both). Provenance vs schema and schema vs lineage are separable.
- **Family 4 'validate the statistical distributions' vs 'validate the schema': weak.** They differ only in the checksum feature (0/10 vs 9/10); not used in any item.
- **Covariate shift vs concept drift (family 5): weak.** The two prompts differ on one feature only: fraud-rate comparison 0/10 vs 4/10. They are not used as a matching pair. 'covariate shift' vs 'label shift' is separable (0 vs 10) and used in 2.2 and 5.2.
- **Saturated features dropped from keys:** F4 c, d, f (10/10 in every version), F5 c (10/10 in every version), F1 e and f (identical in three of four versions). Features that every prompt triggers cannot discriminate prompts.
""")
open("EXAM-DRAFT.md","w").write("\n".join(out))
print(len("\n".join(out).split()))
