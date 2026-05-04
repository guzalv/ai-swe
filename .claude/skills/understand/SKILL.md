---
name: understand
description: Build a thorough understanding of code, issues, PRs, or systems before making changes.
---

# Understand

Build a clear mental model of the problem before writing any code.

## When to Use

- Starting work on an unfamiliar area of the codebase
- Reviewing a PR or set of PRs
- Investigating a bug report or incident
- Before any non-trivial implementation

## Process

> **Follow project-specific guidelines.** Check for `agents.md`,
> `CONTRIBUTING.md`, style guides, and linter configs discovered at session
> start. They take precedence over general defaults below.

### 1. Gather Context

Start with what the user provides (issue URL, PR link, code path, description),
then expand outward:

- **Read the relevant code.** Don't skim -- read the actual functions, types,
  and call sites. Use `file:line` references when discussing specific code.
- **Check git history.** `git log` and `git blame` reveal why code is the way
  it is. Recent changes are especially relevant.
- **Read tests.** Tests document intended behavior better than comments.
- **Check related issues/PRs.** Use `gh` CLI to pull context from GitHub.

### 2. Map the Problem

For bug fixes:
- What is the expected behavior vs actual behavior?
- What changed recently that might have caused this?
- What is the minimal reproduction path?

For features:
- What exists today? What needs to change?
- What are the boundaries of the change? Which files, packages, layers?
- Are there existing patterns to follow?

For PRs/code review:
- What is the PR trying to accomplish?
- Read every file in the diff, not just the ones that look interesting.
- Check for: correctness, edge cases, test coverage, naming, consistency with
  codebase patterns.

### 3. Identify Risks and Questions

- What could go wrong with the obvious approach?
- What assumptions are being made?
- What questions should be answered before proceeding?
- Are there cross-cutting concerns (migrations, backwards compatibility,
  performance)?

### 4. Present Findings

Summarize concisely:
- **What you found** -- the key facts, not a play-by-play of your exploration
- **What needs to change** -- specific files, functions, behaviors
- **Open questions** -- things you couldn't determine from the code alone
- **Recommended approach** -- if you have one, with the main tradeoff

## Output

No artifacts required. This phase produces understanding, not files.
Present findings directly in conversation.

## Guidelines

- Prefer depth over breadth. Understanding 3 files well beats skimming 20.
- Use the Agent tool with `subagent_type: "Explore"` for broad codebase
  exploration that would take more than 3 queries.
- Don't propose solutions until you've finished understanding the problem.
- If the codebase has documentation (CLAUDE.md, README, docs/), read it.
