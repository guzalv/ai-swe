---
name: swe.implement
description: Make code changes step by step, verifying as you go.
---

# Implement

Write code. Work incrementally, verify each step, keep changes minimal.

## Standards

Follow these unless project-specific guidelines say otherwise:

- **Minimal diffs.** Change only what the task requires.
- **No drive-by refactors.** No cleanup that wasn't asked for.
- **No premature abstractions.** Three similar lines beats a helper nobody asked for.
- **Match existing style.** Indentation, naming, error handling, test patterns --
  match what's already there. Read surrounding code before writing.
- **No unnecessary comments.** Only comment why, and only when non-obvious.
- **Trust internal code.** Only validate at system boundaries (user input,
  external APIs). Don't add fallbacks for impossible scenarios.

## Process

### 1. Plan the Change

- List files that need changes and what each needs.
- Identify order and dependencies between files.
- Use TodoWrite for complex changes (more than ~5 files).
- If the approach isn't clear, present 2-3 options with tradeoffs.

### 2. Make Changes

One logical change at a time:

- Follow existing patterns exactly.
- Read neighboring code before editing -- match its style.
- Keep diffs minimal. If a line doesn't need to change, don't touch it.
- Run relevant tests after each meaningful change.
- Check compilation / type checking.

### 3. Verify

- Read your own diff critically. Would you approve this in review?
- Run the full relevant test suite.
- Check for unintended side effects.

### 4. Handle Review Feedback

When the user or review agents provide feedback:

- Read all feedback before starting fixes.
- Answer any questions.
- Implement all requested changes.
- Run tests after all changes are applied.
- Present the complete set of changes, not one at a time.

### 5. Report

- Files modified and why.
- Tests run and results.
- Anything surprising or noteworthy.
