"""Validate multiple-answer/ and essay/ files against the course format. Exit 1 on any problem."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
bad = []; ma = es = 0
for f in sorted((root/"multiple-answer").glob("*.md")):
    for blk in re.split(r"(?m)^## ", f.read_text())[1:]:
        qid = blk.split("\n",1)[0].strip(); ma += 1
        opts = re.findall(r"(?m)^- \[ \] ([A-Z])\. (.+)$", blk)
        key = re.search(r"\*\*Key:\*\* (.+)", blk)
        why = re.findall(r"(?m)^- ([A-Z]): (.+)$", blk)
        if not qid.startswith("MA-"): bad.append(f"{f.name} {qid}: bad id")
        if [o[0] for o in opts] != list("ABCDE"): bad.append(f"{f.name} {qid}: need exactly 5 options A-E, got {len(opts)}")
        if "5 points total" not in blk: bad.append(f"{f.name} {qid}: missing points line")
        k = re.findall(r"([A-E])=([TF])", key.group(1)) if key else []
        if [x[0] for x in k] != list("ABCDE"): bad.append(f"{f.name} {qid}: key must give A-E each T or F")
        if [w[0] for w in why] != list("ABCDE"): bad.append(f"{f.name} {qid}: need a Why line for each of A-E")
        if k and all(x[1]=="T" for x in k) or k and all(x[1]=="F" for x in k): bad.append(f"{f.name} {qid}: all same answer")
for f in sorted((root/"essay").glob("*.md")):
    for blk in re.split(r"(?m)^## ", f.read_text())[1:]:
        qid = blk.split("\n",1)[0].strip(); es += 1
        if not qid.startswith("ES-"): bad.append(f"{f.name} {qid}: bad id")
        if "**Points:** 5" not in blk: bad.append(f"{f.name} {qid}: must be 5 points")
        rub = re.findall(r"(?m)^(\d+)\. ", blk.split("**Rubric",1)[-1])
        if rub != ["1","2","3","4","5"]: bad.append(f"{f.name} {qid}: rubric needs exactly 5 numbered items")
print(f"{ma} multiple-answer questions, {es} essay questions, {len(bad)} problems")
print("\n".join(bad)); sys.exit(1 if bad else 0)
