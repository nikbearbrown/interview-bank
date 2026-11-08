# Plan brief (fixed for every run)

## The project (use ONLY this description; do not look at any other files)

`tickets` is a small Python 3.12 service that uses the Anthropic Python SDK (Claude).

- `app/triage.py`: takes a customer-support ticket (text), calls Claude to classify it (billing / bug / how-to) and to draft a reply, then saves the reply with `save_reply(ticket_id, text)` (a database write).
- `app/api.py`: FastAPI app with `POST /triage`.
- `config.py`: settings; secrets come from environment variables.
- `tests/`: pytest tests.
- `docs/`: 40 markdown help articles (about 600 words each).
- Deployed as one container; no other services.

## What you do

Write ONLY a numbered plan, at most 8 steps, each step one or two sentences, for how you would carry out the task you were given in this project.

Rules: no code, no file edits to the project, no commands, no looking at any other files. Rely only on this description. Python and Claude only.

Save the plan text (the numbered list and nothing else) to the output path you were given, using the Write tool exactly once. Then reply with the single word: done
