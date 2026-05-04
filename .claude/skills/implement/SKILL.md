---
name: implement
description: Make code changes step by step, verifying as you go.
---

# Implement

Write the code. Work incrementally, verify each step, keep changes minimal.

## Process

> **Follow project-specific guidelines.** Check for `agents.md`,
> `CONTRIBUTING.md`, style guides, and linter configs discovered at session
> start. They take precedence over general defaults below.

### 1. Plan the Change

Before writing code:
- List the files that need to change and what changes each needs.
- Identify the order of changes (dependencies between files).
- If the change is complex (more than ~5 files), use TodoWrite to track steps.

If the approach isn't obvious, present 2-3 options to the user with tradeoffs
before implementing. A sentence each is enough.

### 2. Make Changes

Work step by step:

- **One logical change at a time.** Don't change 5 things and hope they all
  work.
- **Follow existing patterns.** Match the project's naming, error handling,
  test style, and file organization. Read neighboring code before writing new
  code.
- **Minimal diffs.** Only change what the task requires. No drive-by refactors,
  no speculative features, no "while I'm here" cleanups.
- **No unnecessary abstractions.** Three similar lines is better than a
  premature helper function. Don't design for hypothetical future requirements.
- **No unnecessary comments.** Only comment why, never what. If removing the
  comment wouldn't confuse a future reader, don't write it.
- **No unnecessary error handling.** Don't validate things that can't be wrong.
  Don't add fallbacks for impossible scenarios. Trust internal code.

### 3. Verify as You Go

After each meaningful change:

- **Run the relevant tests.** `go test ./path/to/package/...` or equivalent.
  Don't wait until the end.
- **Check compilation/type checking.** Catch errors early.
- **Read your own diff.** Would you approve this in code review?

### 4. Handle Review Feedback

When the user provides review feedback:

- Read all feedback items before starting fixes.
- Answer any questions the user asked.
- Implement all requested changes.
- Run tests after all changes are applied.
- Present the complete set of changes, not one at a time.

### 5. Report Results

Summarize what changed:
- Files modified and why
- Tests that were run and their results
- Anything surprising or worth noting

## Guidelines

- **Build from the right base.** If deploying to a cluster, verify the binary
  is compatible with the running environment (DB versions, API versions, etc.).
- **Use `crane mutate` for container image patching** when you need to test a
  single binary change against a running cluster without a full image build.
- **Use environment variables** for runtime configuration that needs to differ
  between environments.
- **When adding helpers to test frameworks** (e.g., new orchestrator methods),
  follow the existing patterns exactly -- same retry strategy, same error
  handling, same naming conventions.
