"""Build json/multiple-answer.json and json/essay.json from the markdown question files.

The markdown files are the source of truth; JSON is generated and always includes the answers
(statement keys and reasons for multiple-answer, the rubric for essay).
Run: python3 -I scripts/build_json.py   (then python3 -I scripts/check_format.py)
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COURSE = "INFO 7375: Prompt Engineering for Generative AI"

SCORING = {
    "multiple-answer": {
        "points": 5,
        "rule": "Five statements, each true or false, 1 point each. The student checks the statements they believe are true. "
                "A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0.",
    },
    "essay": {
        "points": 5,
        "rule": "Short essay scored against a rubric of five items, 1 point each.",
    },
}


def file_order(path):
    name = path.name
    if name.startswith("00-"):
        return (0, name)
    return (1, name)


def chapter_of(path):
    m = re.match(r"ch(\d+)-", path.name)
    return int(m.group(1)) if m else None


def parse_title(text):
    m = re.search(r"(?m)^# (.+)$", text)
    return m.group(1).strip() if m else ""


def split_blocks(text, prefix):
    """Return (section_title, id, body) for each '## <prefix>-' block; the section is the latest '# ' heading."""
    heads = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"(?m)^(#{1,2} .+)$", text)]
    section = ""
    blocks = []
    for i, (start, end, line) in enumerate(heads):
        if line.startswith("## "):
            qid = line[3:].strip()
            nxt = heads[i + 1][0] if i + 1 < len(heads) else len(text)
            if qid.startswith(prefix + "-"):
                blocks.append((section, qid, text[end:nxt].strip("\n")))
        else:
            section = line[2:].strip()
    return blocks


def source_of(body):
    m = re.search(r"\*\*Source:\*\* (.+)", body)
    return m.group(1).strip() if m else None


def parse_ma(path, text):
    chapter = chapter_of(path)
    questions = []
    for section, qid, body in split_blocks(text, "MA"):
        stem = body.split("\n- [ ]", 1)[0].strip()
        stem = re.sub(r"\s*Each statement is worth 1 point \(5 points total\)\.?$", "", stem).strip()
        opts = re.findall(r"(?m)^- \[ \] ([A-E])\. (.+)$", body)
        key = dict(re.findall(r"([A-E])=([TF])", re.search(r"\*\*Key:\*\* (.+)", body).group(1)))
        why_part = body.split("**Why:**", 1)[1]
        why = dict(re.findall(r"(?m)^- ([A-E]): (.+)$", why_part))
        questions.append({
            "id": qid,
            "type": "multiple-answer",
            "points": 5,
            "chapter": chapter,
            "group": "chapter" if chapter else "foundations",
            "section": (None if chapter else section) or None,
            "source": source_of(body),
            "stem": stem,
            "statements": [
                {"label": l, "text": t, "correct": key[l] == "T", "explanation": why[l]}
                for l, t in opts
            ],
        })
    return questions


def parse_es(path, text):
    chapter = chapter_of(path)
    questions = []
    for section, qid, body in split_blocks(text, "ES"):
        prompt = body.split("**Points:**", 1)[0].strip()
        rubric_part = body.split("**Rubric", 1)[1]
        items = re.findall(r"(?m)^(\d+)\. (.+)$", rubric_part)
        questions.append({
            "id": qid,
            "type": "essay",
            "points": 5,
            "chapter": chapter,
            "group": "chapter" if chapter else "foundations",
            "section": (None if chapter else section) or None,
            "source": source_of(body),
            "prompt": prompt,
            "rubric": [{"point": int(n), "text": t} for n, t in items],
        })
    return questions


def build():
    out_dir = ROOT / "json"
    out_dir.mkdir(exist_ok=True)
    result = {}
    for kind, prefix, parser in (("multiple-answer", "MA", parse_ma), ("essay", "ES", parse_es)):
        qs = []
        chapters = {}
        for path in sorted((ROOT / kind).glob("*.md"), key=file_order):
            text = path.read_text()
            ch = chapter_of(path)
            chapters[str(ch) if ch else "foundations"] = parse_title(text)
            qs += parser(path, text)
        doc = {"course": COURSE, "type": kind, "scoring": SCORING[kind], "count": len(qs),
               "chapters": chapters, "questions": qs}
        (out_dir / f"{kind}.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
        result[kind] = len(qs)
    return result


if __name__ == "__main__":
    print(build())
