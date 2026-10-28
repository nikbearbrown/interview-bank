"""Build the links-only technical index: metadata + exact source locators, no question/answer text."""
import json, sys
src, out = sys.argv[1], sys.argv[2]
KEEP = ["id","topic","subtopic","section","relevant_roles","interview_category","question_type",
        "question_sha256","rights_class","flags","exact_duplicate_count","duplicate_groups"]
n = 0
with open(src) as f, open(out, "w") as o:
    for line in f:
        r = json.loads(line)
        d = {k: r.get(k) for k in KEEP}
        d["sources"] = [{k: s.get(k) for k in ("repository","path","commit","locator","url")} for s in r["sources"]]
        d["licenses"] = sorted({l.get("declared_license") or "none" for l in r.get("license_attribution", [])})
        o.write(json.dumps(d, ensure_ascii=False) + "\n"); n += 1
print(n, "records")
