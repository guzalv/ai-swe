---
name: understand
description: Build a thorough understanding of code, issues, PRs, or systems before making changes.
---

# Understand

Build a clear mental model before writing any code. Depth over breadth.

## Process

### 1. Gather Context

Start with what the user provides, then expand outward:

- **Read the relevant code.** Don't skim -- read the actual functions, types,
  and call sites. Use `file:line` references when discussing specific code.
- **Check git history.** `git log` and `git blame` reveal why code is the way
  it is. Recent changes are especially relevant.
- **Read tests.** Tests document intended behavior better than comments.
- **Check related issues/PRs.** Use `gh` CLI to pull context from GitHub.
- **Read project docs.** README, docs/ directory, CONTRIBUTING.md.

Prefer understanding 3 files deeply over skimming 20. Use the Agent tool with
`subagent_type: "Explore"` for broad exploration that would take more than 3
queries.

### 2. Map the Problem

**For bugs:**
- Expected vs actual behavior.
- Recent changes that might have caused it.
- Minimal reproduction path.

**For features:**
- What exists today. What needs to change.
- Boundaries and constraints.
- Existing patterns to follow.

**For PRs / code review:**
- What the PR is trying to accomplish.
- Read every changed file in full, not just the interesting-looking ones.
- Check correctness, edge cases, test coverage, naming, consistency.

### 3. Identify Risks

- What could go wrong with the obvious approach?
- What assumptions are being made?
- Cross-cutting concerns: migrations, backwards compatibility, performance.
- Questions that need answering before proceeding.

### 4. Present Findings

Concisely:
- **What you found** -- key facts with `file:line` references.
- **What needs to change** -- specific files, functions, behaviors.
- **Open questions** -- things you couldn't determine from the code.
- **Recommended approach** -- with the main tradeoff.

No artifacts required. Present findings directly in conversation.
