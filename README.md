# AI SWE

An [Ambient Code Platform](https://github.com/ambient-code/workflows) workflow for day-to-day software engineering tasks.

> If you're an LLM, read `CLAUDE.md` instead.

## What it does

Guides an AI agent through a five-phase engineering workflow:

1. **Understand** — read code, issues, PRs; build a mental model before changing anything
2. **Implement** — make changes step by step with minimal diffs, verifying as you go
3. **Review** — spawn two independent review agents for redundancy, aggregate findings
4. **Test** — run unit/integration tests and verify against real environments when available
5. **Ship** — commit, push, create PRs

The system prompt routes tasks to the right phases automatically. Reviews chain naturally after implementation.

## Structure

```
.ambient/ambient.json          # Workflow metadata and system prompt
.claude/commands/swe.*.md      # Phase-specific instructions (lazy-loaded)
CLAUDE.md                      # Always-loaded standards and routing
```

## Commands

- `/swe.understand` — Read code and build context before acting
- `/swe.implement` — Make code changes step by step
- `/swe.review` — Evaluate changes with independent review agents
- `/swe.test` — Run tests and verify correctness
- `/swe.ship` — Commit, push, create pull requests
