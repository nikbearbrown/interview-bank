import json,re,random
S=json.load(open('runs/summary.json')); FR=S['freq']; AG=S['agreement']
P={f:{r['id']:r for r in json.load(open(f'runs/{f}.json'))['plans']} for f in ['F1','F2','F3','F4','F5']}
PR=json.load(open('prompts.json')); FE=json.load(open('features.json'))
def prompt(f,v): return PR[f]['slot'].replace('{X}',PR[f]['variants'][v])
def band(n): return 'LIKELY' if n>=7 else ('PLAUSIBLE' if n>=2 else 'UNLIKELY')
def plan(pid,w=150):
    f=pid[:2]; out=[]
    for s in P[f][pid]['plan'].split('\n'):
        s=s.strip()
        if s: out.append(s if len(s)<=w else s[:w].rsplit(' ',1)[0]+' …')
    return '\n'.join(out)
def q(block): return '\n'.join('> '+l for l in block.split('\n'))
def line(pid,rx):
    for s in P[pid[:2]][pid]['plan'].split('\n'):
        if re.search(rx,s,re.I): return s.strip()[:230]+(' …' if len(s.strip())>230 else '')
    return '(no matching line)'
def ev(f,v,feat,val,rx,k=2):
    ids=[i for i,r in P[f].items() if r['variant']==v and r['codes'][feat]==val][:k]
    return '\n'.join(f'  - `{i}`: "{line(i,rx)}"' for i in ids)
def table(f,feats,vs='ABCD'):
    h='| feature | '+' | '.join(f'{v}: {PR[f]["variants"][v]}' for v in vs)+' |\n|---|'+'---|'*len(vs)+'\n'
    for k in feats:
        t='' if FE[f][k][0]=='S' else ' [BEHAVIORAL]'
        h+=f'| `{k}`{t} | '+' | '.join(f'{FR[f][v][k]}/10 ({band(FR[f][v][k])})' for v in vs)+' |\n'
    return h
CFG='Plans sampled 2026-11-08 by Claude sub-agents (Agent tool, model alias `sonnet`), one plan per sub-agent, 10 runs per prompt.'
# ---------- EXAM ----------
rnd=random.Random(11); order=list('ABCD'); rnd.shuffle(order)  # matching: plan letters W-Z
L=dict(zip(order,'WXYZ'))
E=[]
E.append(f"""# Predict the Prompt — pilot exam draft (INFO 7375 Prompt Engineering for Generative AI)

*Draft for Bear to judge the format. 7 items, 20 points. Python and Claude only.*

**How to read this paper.** Every item shows a prompt given to an AI agent, and asks what plan the agent will write for it. The answer key is not opinion: each prompt was run 10 times and each plan was coded for yes/no features. Bands: **LIKELY** = 7–10 of 10 plans, **PLAUSIBLE** = 2–6 of 10, **UNLIKELY** = 0–1 of 10. Features are *semantic* (they follow from what the words mean) unless marked **[BEHAVIORAL]** (a habit of the model, weighted at half).

**Honesty note.** A "plan" here is the numbered plan written by a Claude sub-agent (not Claude Code plan mode) for the small fixed project below. Config: {CFG} Full details, coder agreement and all raw plans: `KEY-AND-RUNS.md`, `runs/`.

**The project every agent was given.** `tickets`, a Python 3.12 service using the Anthropic SDK. `app/triage.py` classifies a support ticket (billing / bug / how-to), drafts a reply with Claude, and saves it with `save_reply(ticket_id, text)` (a database write). `app/api.py` is a FastAPI app (`POST /triage`). `config.py` holds settings (secrets from env vars), `tests/` has pytest, `docs/` has 40 help articles. One container.

**Instruction every agent got:** write only a numbered plan, at most 8 steps; no code, no edits.

---
""")
# Q1 matching
ids={v:f'F4{v}-01' for v in 'ABCD'}
E.append("## Item 1 — Matching (4 points)\n\nFour prompts, each ending the sentence *“Build a ticket-routing agent that …”*:\n\n"+'\n'.join(f'1. **({i+1})** …{PR["F4"]["variants"][v]}.' for i,v in enumerate('ABCD'))+"\n\nBelow are four plans (shortened to the first ~150 characters of each step), each written for one of those prompts. Match each prompt (1–4) to a plan (W–Z).\n")
for letter in 'WXYZ':
    v=[k for k,x in L.items() if x==letter][0]
    E.append(f"**Plan {letter}**\n\n{q(plan(ids[v]))}\n")
key1=', '.join(f'({i+1}) → {L[v]}' for i,v in enumerate('ABCD'))
E.append(f"""**KEY:** {key1}.  
**Why these are distinguishable (frequencies, 10 plans each):**

{table('F4',['separate_plan_step','human_plan_approval','reflect_or_replan','iteration_cap'])}
The “no planning step” prompt is the only one with 0/10 separate plan steps; “human approves the plan” is the only one with 10/10 plan approval; “reflects on each result” is the only one with 10/10 reflect/replan. Backing plans shown above: `F4A-01`, `F4B-01`, `F4C-01`, `F4D-01` (all 40 in `runs/F4.json`).  
*Scoring: 1 point per correct pair.*

---
""")
# Q2 MC
mc=[('F3A','A'),('F3B','B'),('F3C','C'),('F3D','D')]
mcorder=list('ABCD'); random.Random(5).shuffle(mcorder); M=dict(zip(mcorder,'abcd'))
E.append(f"""## Item 2 — Prompt → most likely plan (2 points)

**Prompt:** *“{prompt('F3','B')}”*

Which plan is the one most likely to be produced? (Plans shortened.)

""")
for letter in 'abcd':
    v=[k for k,x in M.items() if x==letter][0]
    E.append(f"**({letter})**\n\n{q(plan(f'F3{v}-01',130))}\n")
E.append(f"""**KEY:** ({M['B']}). The prompt says *all 40 articles in the system prompt*; 10/10 plans for it load the full text, 10/10 check the token budget, 10/10 use prompt caching only in 0/10 … see table.

{table('F3',['all_articles_in_prompt','retrieval_index','token_budget','prompt_caching','cite_or_abstain'])}
The distractors are real plans from the three altered prompts (retrieve per ticket / short policy summary / search tool). Note the distractors for “retrieve” and “search tool” have the same profile (10/10 retrieval index), so the item is built to ask about the *all-articles* prompt, where only one plan fits. Backing: `F3B-01` (key), `F3A-01`, `F3C-01`, `F3D-01` (distractors); all 40 in `runs/F3.json`.  
*Scoring: 2 points for the key; 0 otherwise.*

---
""")
# fix sloppy sentence
E[-1]=E[-1].replace("10/10 plans for it load the full text, 10/10 check the token budget, 10/10 use prompt caching only in 0/10 … see table.",f"{FR['F3']['B']['all_articles_in_prompt']}/10 plans load the full text of all articles into the prompt, {FR['F3']['B']['token_budget']}/10 check the token budget, {FR['F3']['B']['prompt_caching']}/10 add prompt caching.")
# Q3 plausibility
E.append(f"""## Item 3 — Plausibility (4 points)

The prompts below end *“Make the Claude call and the `save_reply` write in `app/triage.py` more reliable by adding …”*. For each statement about the plans, write LIKELY, PLAUSIBLE or UNLIKELY (how many of 10 plans?). Each statement quotes the phrase that matters.

a. With **“a plain retry”**: the plan makes the `save_reply` write safe to repeat (idempotency key, upsert, or unique constraint).  
b. With **“a timeout”**: the plan also adds retries with exponential backoff.  
c. With **“a timeout”**: the plan adds a circuit breaker (open/half-open state).  
d. With **“a circuit breaker”**: the plan includes the breaker state machine.

**KEY and frequencies:**

| | prompt phrase | feature | observed | band |
|---|---|---|---|---|
| a | a plain retry | `idempotency` | {FR['F2']['B']['idempotency']}/10 | {band(FR['F2']['B']['idempotency'])} |
| b | a timeout | `backoff_jitter` | {FR['F2']['D']['backoff_jitter']}/10 | {band(FR['F2']['D']['backoff_jitter'])} |
| c | a timeout | `circuit_breaker` | {FR['F2']['D']['circuit_breaker']}/10 | {band(FR['F2']['D']['circuit_breaker'])} |
| d | a circuit breaker | `circuit_breaker` | {FR['F2']['C']['circuit_breaker']}/10 | {band(FR['F2']['C']['circuit_breaker'])} |

Evidence (sampled plans):

- a. `F2B` (plain retry), idempotency present:
{ev('F2','B','idempotency',1,'idempoten|upsert|unique|dedup')}
- b. `F2D` (timeout), backoff present in 4 plans, e.g.:
{ev('F2','D','backoff_jitter',1,'backoff|jitter')}
- c. `F2D` (timeout): none of the 10 plans mention a breaker (e.g. `F2D-01` step list in `runs/F2.json`).
- d. `F2C` (circuit breaker):
{ev('F2','C','circuit_breaker',1,'breaker|half-open')}

Teaching point for (a): the prompt said *plain* retry, yet every plan notices that `save_reply` is a database write and adds idempotency. The word “plain” did not stop it; the project description (“a database write”) did. *Scoring: 1 point each.*

---
""")
# Q4 forecast
E.append(f"""## Item 4 — Feature forecasting (6 points)

**Prompt:** *“{prompt('F5','B')}”*

Ten agents each wrote a plan for this prompt. For each feature, predict **how many of the 10 plans** contain it.

a. The plan states a **numeric pass/fail threshold** for the classifier (for example “accuracy ≥ 90%”).  
b. The plan computes **per-class metrics** (confusion matrix, per-category precision/recall).  
c. **[BEHAVIORAL, half weight]** The plan **mocks or stubs the Claude client** so tests make no live API calls.

**KEY:** a = {FR['F5']['B']['numeric_threshold']}/10, b = {FR['F5']['B']['per_class_metrics']}/10, c = {FR['F5']['B']['mocks_model']}/10.

For comparison, the sibling prompt *“{prompt('F5','A')}”* gives a = {FR['F5']['A']['numeric_threshold']}/10, b = {FR['F5']['A']['per_class_metrics']}/10, c = {FR['F5']['A']['mocks_model']}/10.

{table('F5',['numeric_threshold','per_class_metrics','mocks_model','labeled_dataset','automated_gate'],'AB')}
Backing plans for b (4 plans have it):
{ev('F5','B','per_class_metrics',1,'confusion|per-class|per class|precision|recall|per category')}

Backing plan for a (none has it; a typical `F5B` plan, shortened):

{q(plan('F5B-02',140))}

*Scoring (banded): a and b: exact or within ±1 → 2 points; within ±2 → 1 point; otherwise 0. c: the same bands but worth 1 point maximum (half weight).*

---
""")
# Q5 attribution
E.append(f"""## Item 5 — Attribution (2 points)

Here is a plan written for the prompt *“{prompt('F4','C')}”*

{q(plan('F4C-01',150))}

Steps 4 and 5 add a pending record and an approve/reject endpoint. **Quote the words of the prompt that caused these steps.** Then say what would happen to them if those words were deleted.

**KEY:** The clause *“and gets a human to approve the plan”*. Without it (prompt: “{prompt('F4','A')}”) the approval step disappears: `human_plan_approval` {FR['F4']['A']['human_plan_approval']}/10 instead of {FR['F4']['C']['human_plan_approval']}/10, while the separate planning step stays ({FR['F4']['A']['separate_plan_step']}/10 vs {FR['F4']['C']['separate_plan_step']}/10). So “plans before acting” causes the planning stage; the human clause causes the gate. Backing: `F4C-01` (shown), `F4A-01`, plus counts in `runs/F4.json`.  
*Scoring: 1 point for quoting the clause, 1 point for predicting that the planning step survives but the gate goes.*

---
""")
# Q6 predict & explain
E.append(f"""## Item 6 — Predict and explain (3 points)

Two prompts both end *“Give the triage agent an `issue_refund(ticket_id, amount)` tool, protected by …”*: (i) **“a rate limit”** and (ii) **“an audit log”**. In how many of 10 plans for each will a **human approve or reject a refund before it executes**? Predict a band for each, then explain the difference in two sentences.

**KEY:** (i) rate limit: {FR['F1']['C']['human_approval']}/10 → {band(FR['F1']['C']['human_approval'])}; (ii) audit log: {FR['F1']['D']['human_approval']}/10 → {band(FR['F1']['D']['human_approval'])}.  
A rate limit is read as a *sufficient control* for the stated risk (too many refunds), so the plans build caps and a rate limiter and stop there. A log only records after the fact, so the plans add an approval threshold of their own anyway (“Protect the tool beyond logging …”). *Explanation is a hypothesis about why; the frequencies are the measured part.*

Evidence:
{ev('F1','D','human_approval',1,'beyond logging|approval|pending',2)}
- `F1C-08` (rate limit): "{line('F1C-08','rate limit')}"

Also note what did **not** differ: with **“a permission gate”** vs **“an approval gate”** the plans were the same ({FR['F1']['A']['human_approval']}/10 vs {FR['F1']['B']['human_approval']}/10 human approval, {FR['F1']['A']['permission_scope']}/10 vs {FR['F1']['B']['permission_scope']}/10 permission scope). The course’s distinction did not survive sampling, so no item asks students to predict it (see `README.md`, cut list).  
*Scoring: 1 point per correct band; 1 point for an explanation that says rate limit = sufficient control vs log = after-the-fact.*

---
""")
# Q7 repair
E.append(f"""## Item 7 — Minimal-edit repair (4 points)

**Prompt A (given):** *“{prompt('F5','B')}”*

Across 10 runs this prompt produced **0/10** plans with a numeric pass/fail threshold and {FR['F5']['B']['per_class_metrics']}/10 with per-class metrics. **Edit the prompt (change, add or delete at most 12 words in total)** so that at least **8 of 10** new plans contain a numeric threshold. Submit your edited prompt.

**Grading by running (protocol).** For each submission: (1) count the changed words by word-level diff (>12 → 0 points); (2) paste the edited prompt after the fixed project brief (`runs/PLAN-BRIEF.md`), run 10 independent plan agents with the same configuration as the exam (see `KEY-AND-RUNS.md`); (3) a coder agent given the definition of `numeric_threshold` marks each plan 0/1; a human spot-checks any score of 6–9; (4) score: ≥8/10 → 4 points, 5–7 → 2 points, 2–4 → 1 point, ≤1 → 0.

**Reference repair (already run):** replace *“make sure it works”* with *“write an eval with acceptance criteria”* (6 words changed). That prompt (family variant A) scored **{FR['F5']['A']['numeric_threshold']}/10** threshold, {FR['F5']['A']['per_class_metrics']}/10 per-class metrics, {FR['F5']['A']['automated_gate']}/10 automated gate. Backing plan:

{q(plan('F5A-01',150))}

Other repairs a student might try (e.g. “accuracy ≥ 90%”) were **not** run in this pilot; they would be graded by the protocol above.

---

**Answer-sheet summary:** Item 1 = {key1}; Item 2 = ({M['B']}); Item 3 = a LIKELY, b PLAUSIBLE, c UNLIKELY, d LIKELY; Item 4 = a {FR['F5']['B']['numeric_threshold']}, b {FR['F5']['B']['per_class_metrics']}, c {FR['F5']['B']['mocks_model']}; Item 6 = (i) UNLIKELY, (ii) LIKELY.
""")
open('EXAM-DRAFT.md','w').write('\n'.join(E))
print('ok')
