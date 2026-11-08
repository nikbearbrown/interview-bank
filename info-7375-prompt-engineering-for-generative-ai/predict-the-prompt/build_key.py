import json,itertools
S=json.load(open('runs/summary.json')); FR=S['freq']; AG=S['agreement']
PR=json.load(open('prompts.json')); FE=json.load(open('features.json'))
def band(n): return 'L' if n>=7 else ('P' if n>=2 else 'U')
o=[]
o.append("""# Key and runs — predict-the-prompt pilot

## 1. Configuration (pinned and recorded)

| item | value |
|---|---|
| date sampled | 2026-11-08 |
| plan writer | Claude sub-agent via the Claude Code `Agent` tool, `subagent_type=general-purpose`, `model="sonnet"` (alias; the tool does not return the resolved model id — the session is the Claude 5 family, so this is the Sonnet 5.x line, exact id NOT recorded) |
| how plans were requested | each sub-agent got one line: read `runs/PLAN-BRIEF.md` (project description + rules) and do the task `<prompt>`; write ONLY a numbered plan of at most 8 steps, no code/edits/commands; save it with Write to `runs/raw/<ID>.txt` and reply `done` |
| fixed project description | `runs/PLAN-BRIEF.md` (identical for all 200 runs) |
| runs | 5 families × 4 prompts × 10 = **200 plans**, none discarded, none re-run |
| launch | F1 and F2A directly (waves of ≤20, the concurrency cap); F2B–D and F3–F5 (150 plans) through two orchestrator sub-agents that spawned the plan sub-agents |
| coders | Claude sub-agents, `sonnet`; primary coder: one per family, blind (shuffled ids `P01..P40`, variant hidden, `coding/Fx-blind.md`); second coder: independent sub-agent, 8 of 40 plans per family (20%, every 5th blind id) |
| sampling parameters | **not controllable** (temperature/top-p are the harness defaults) |
| caveats | (1) a sub-agent plan, **not** Claude Code plan mode. (2) The sub-agents ran inside a Claude Code harness; their context may include the harness system prompt and the user's memory/CLAUDE.md, so this is not a clean API call. (3) Plan agents had file tools (used Read + Write only). (4) Both writers and coders are the same model family; coders could share the writers' blind spots. (5) Coders judged text, not running code. (6) Reported sub-agent usage was about 70k tokens per plan run (mostly fixed harness context). |

Reproduce: `prompts.json` (the 20 prompts), `runs/PLAN-BRIEF.md`, `features.json`, then `build_sheets.py` → coders → `analyze.py` → `build_docs.py`, `build_key.py`.

## 2. The 20 prompts
""")
for f in FR:
    o.append(f"**{f} — {PR[f]['name']}**\n")
    for v in 'ABCD': o.append(f"- {f}{v}: *{PR[f]['slot'].replace('{X}',PR[f]['variants'][v])}*")
    o.append('')
o.append("## 3. Features (S = semantic, B = behavioral; B items weighted half)\n")
for f in FE:
    o.append(f"**{f}**\n")
    for k,v in FE[f].items(): o.append(f"- `{k}` [{v[0]}]: {v[1]}")
    o.append('')
o.append("## 4. Frequencies (plans out of 10 containing the feature)\n\nBands: L ≥7, P 2–6, U ≤1.\n")
for f in FR:
    o.append(f"**{f} — {PR[f]['name']}**\n\n| feature | A | B | C | D |\n|---|---|---|---|---|")
    for k in FE[f]:
        o.append(f"| `{k}` [{FE[f][k][0]}] | "+' | '.join(f"{FR[f][v][k]} ({band(FR[f][v][k])})" for v in 'ABCD')+' |')
    o.append('')
o.append("## 5. Premise check (variant pairs with the same profile)\n\nA pair is a **duplicate** if no semantic feature changes band (L/P/U) between the two prompts *and* no count differs by more than 1. Duplicate pairs cannot be used to tell prompts apart, so items using them were cut.\n")
for f in FR:
    sem=[k for k in FE[f] if FE[f][k][0]=='S']
    for a,b in itertools.combinations('ABCD',2):
        d=[(k,FR[f][a][k],FR[f][b][k]) for k in sem if band(FR[f][a][k])!=band(FR[f][b][k]) or abs(FR[f][a][k]-FR[f][b][k])>1]
        if not d: o.append(f"- **{f}{a} ≡ {f}{b}** ({PR[f]['variants'][a]} vs {PR[f]['variants'][b]}): DUPLICATE — no semantic feature separates them.")
        elif len(d)==1: o.append(f"- {f}{a} vs {f}{b}: separated by one feature only: `{d[0][0]}` ({d[0][1]} vs {d[0][2]}).")
o.append("\n## 6. Coder agreement (second coder, 8 of 40 plans per family = 20%)\n\n| family | feature cells | agree | % | Cohen's κ (pooled) | disagreements |\n|---|---|---|---|---|---|")
tot=ag=0
for f,a in AG.items():
    tot+=a['n']; ag+=a['agree']
    dis=', '.join(f'{k} {v}' for k,v in a['per_feature'].items() if v.split('/')[0]!=v.split('/')[1]) or 'none'
    o.append(f"| {f} | {a['n']} | {a['agree']} | {a['pct']} | {a['kappa']} | {dis} |")
o.append(f"| **all** | {tot} | {ag} | {round(100*ag/tot,1)} | | |\n\nCaveat: many features sit at 0/10 or 10/10, which inflates raw agreement and can depress κ; and both coders are the same model. The one-line judgement calls the coders reported (e.g. F1 `permission_scope` coded 1 whenever the tool is limited to billing tickets; `mocks_model` only when *Claude* is mocked) were NOT yet written back into the definitions above; a v2 should add them (and the F1 coders marked `permission_scope` and `audit_log` leniently, so those two F1 columns are the least trustworthy).\n\n## 7. Files\n\n- `runs/F1.json … F5.json`: every plan with its codes. `runs/raw/*.txt`: the 200 raw plans. `runs/summary.json`: frequencies and agreement.\n- `coding/`: blind sheets, id keys, both coders' JSON.\n")
open('KEY-AND-RUNS.md','w').write('\n'.join(o))
