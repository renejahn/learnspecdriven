# Learn Spec-Driven Development

A dependency-free, interactive learning website about **spec-driven development (SDD) with agentic software engineering**.

## Run locally

Requires Python 3.9+.

```sh
./serve.sh
# or: python3 serve.py
```

Your default browser opens automatically at http://localhost:8000. For headless environments or if you do not want the browser opened, use `NO_BROWSER=1 ./serve.sh`. Override the port with `PORT=9000 ./serve.sh`.

## Learn

The site includes six lessons, a workflow map, a practical example, a reusable specification template, a short knowledge quiz, and curated references. Progress is stored locally in the browser.

## Project layout

- `index.html` — accessible, responsive learning experience
- `styles.css` — visual design
- `app.js` — lesson navigation, quiz and local progress
- `serve.py`, `serve.sh` — minimal local HTTP server
- `docs/example-spec.md` — worked feature specification
- `docs/references.md` — research links and caveats
- `AGENTS.md` — guidance for coding agents

No install or build step required. The server is intended for **local development**, not production deployment.

## Source-backed learning

Lesson-specific links appear beneath each lesson. The workflow is explicitly a Spec Kit-inspired example, not a universal or independently proven standard. The [research notes](docs/references.md) distinguish documented tool behavior from recommended engineering practices.

## Worked human–agent dialogues

Each lesson includes a fictional, illustrative four-turn conversation following one consistent task-export feature. These are teaching examples, **not transcripts of a real agent execution or evidence that commands were run**. The examples cover specification, clarification, planning, task decomposition, scoped implementation and evidence-based review.
