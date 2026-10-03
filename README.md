# Learn Spec-Driven Development

A dependency-free, interactive learning website about **spec-driven development (SDD) with agentic software engineering**.

## Run locally

Requires Python 3.9+.

```sh
./serve.sh
# or: python3 serve.py
```

Open http://localhost:8000. Override the port with `PORT=9000 ./serve.sh`.

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
