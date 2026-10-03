# Evidence and research notes (reviewed 3 October 2026)

The site teaches a practical **Spec Kit-inspired** workflow. It is not a claim that a universal SDD standard exists or that SDD guarantees better outcomes. The descriptions below distinguish documented functionality from advice.

## Sources mapped to claims

1. **[Spec Kit methodology](https://github.github.com/spec-kit/)** — GitHub's core Specify → Plan → Tasks → Implement → Converge process; clarification and quality gates are optional.
2. **[Spec Kit quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md)** — Specifications focus on what and why; planning addresses technology; checks and human review occur throughout.
3. **[Spec Kit agentic reference](https://github.github.com/spec-kit/reference/agentic-sdd.html)** — Clarification, task breakdown, consistency analysis and convergence.
4. **[AGENTS.md](https://agents.md/)** — Project-local agent instructions for setup, style, tests and conventions.
5. **[OpenAI Codex safety](https://openai.com/index/running-codex-safely/)** — Tool permissions, boundaries, approvals and auditability for coding agents.
6. **[OpenAI Codex introduction](https://openai.com/index/introducing-codex/)** — Agent ability to work on code and importance of human review and test results.
7. **[OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/iterating-development-workflows-with-codex.md)** — Observed vs reported evidence; record failed and skipped checks explicitly.

## Lesson evidence map

- **Why specs matter:** Spec Kit describes carrying requirements and artifacts through implementation; Codex describes agent code editing and the need to validate generated changes (sources 1 and 6).
- **Write testable intent:** Spec Kit recommends specifying *what* and *why*, resolving ambiguity and checking requirements before implementation (sources 2 and 3).
- **Plan the work:** Spec Kit separates technical plans and dependency-ordered tasks from product intent (sources 2 and 3).
- **Guide coding agents:** AGENTS.md provides repository-level instructions; Codex safety guidance documents permission boundaries and human approval (sources 4–6).
- **Converge on evidence:** Spec Kit's converge phase assesses implementation against artifacts; OpenAI's engineering workflow distinguishes actual test evidence from reported or skipped checks (sources 3, 6 and 7).
- **Operate & improve:** Iteration and recorded evidence are process recommendations synthesized from Spec Kit and OpenAI Cookbook (sources 1 and 7), not proven universal laws.

## Important limitations

- The six boxes on the website adapt Spec Kit's five core stages by including optional **Clarify** as a distinct step. Spec Kit also provides optional checklist and analysis gates and a one-time constitution.
- The example CSV specification is a teaching artifact, not a production-ready security review or a tested feature. Requirements for spreadsheet formula injection, authorization and limits must be validated for each application.
- Agents and integrations differ in command names, capabilities and permissions. Read the latest official documentation.
- Links are evidence for **documented process and product behavior**, not empirical proof of performance gains. No numerical productivity claims are made.
