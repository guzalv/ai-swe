# AI SWE

An [Ambient Code Platform](https://github.com/ambient-code/workflows) workflow for day-to-day software engineering tasks.

## What it does

Guides an AI agent through a five-phase engineering workflow:

1. **Understand** — read code, issues, PRs; build a mental model before changing anything
2. **Implement** — make changes step by step with minimal diffs, verifying as you go
3. **Review** — spawn two independent review agents on the same task for redundancy
4. **Test** — run unit/integration tests and verify against real environments when available
5. **Ship** — commit, push, create PRs, handle stacked branches

A controller skill manages phase transitions and never auto-advances without user input.

## Principles

- **Pragmatism over dogma** — do what works
- **Simplicity** — fewer files, fewer abstractions, fewer moving parts
- **Readability** — optimize for the reader
- **KISS** — complexity must justify itself
- **YAGNI** — solve today's problem today

## Project-specific guidelines

The workflow discovers and follows project-specific instructions (`agents.md`, `CONTRIBUTING.md`, style guides, linter configs) at session start. These take precedence over general defaults.

## Structure

```
.ambient/ambient.json          # Workflow metadata and system prompt
.claude/skills/controller/     # Phase orchestration
.claude/skills/understand/     # Context gathering
.claude/skills/implement/      # Code changes
.claude/skills/review/         # Independent review agents
.claude/skills/test/           # Testing and verification
.claude/skills/ship/           # Commit, push, PR creation
CLAUDE.md                      # Engineering standards
```
