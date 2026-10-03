# Research notes (reviewed October 2026)

## Primary sources
- [GitHub Spec Kit](https://github.github.com/spec-kit/) — core Specify → Plan → Tasks → Implement → Converge process and optional quality gates.
- [Spec Kit Quickstart](https://github.github.com/spec-kit/quickstart.html) — agent-dependent command invocation and practical usage.
- [Spec Kit Agentic SDD reference](https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md) — phase responsibilities and convergence behavior.
- [AGENTS.md](https://agents.md/) — portable convention for repository-level coding-agent instructions.
- [OpenAI Cookbook: iterating development workflows](https://github.com/openai/openai-cookbook/blob/main/examples/codex/iterating-development-workflows-with-codex.md) — agent guidance, staged plans and iterative verification.
- [Diaz et al., Spec-Driven Development for Agentic Software Engineering](https://arxiv.org/abs/2609.00252) (2026) — conceptual framework for human–agent contracts and harnesses. Authors explicitly note the immature empirical evidence base.
- [Lulla et al., Impact of AGENTS.md Files](https://arxiv.org/abs/2601.20404) (2026) — empirical but limited study (10 repositories, 124 pull requests) of instruction-file impact.

## Interpretation
The site teaches a **practical synthesis**, not a formally established universal standard. Spec Kit is one concrete implementation; terminology and commands differ among tools. Additional safeguards (human approval, least privilege, threat modeling, test traceability) are engineering recommendations, not guarantees of safety. Confirm current tool documentation before running commands in a real repository.
