# AI SWE Workflow

## Engineering Standards

### Code changes
- Minimal diffs. Change only what the task requires.
- No drive-by refactors, no cleanup that wasn't asked for.
- No premature abstractions. Three similar lines is better than a helper nobody asked for.
- Match existing project style -- indentation, naming, error handling, test patterns.
- No comments explaining what. Only comment why, and only when non-obvious.

### Error handling
- Only validate at system boundaries (user input, external APIs). Trust internal code.
- Don't add fallbacks for scenarios that can't happen.
- Don't wrap errors that are already clear enough.

### Testing
- Test behavior, not implementation.
- Prefer integration tests over mocks when practical.
- Use the project's existing test patterns and helpers.

### Commits and PRs
- Atomic commits: one logical change per commit.
- Commit messages: say why, not what.
- PR descriptions: summarize the change and how to test it.

## Process

### Before writing code
1. Understand the problem. Read the relevant code. Check git history for context.
2. If the approach isn't obvious, propose options to the user before implementing.
3. If the task is complex, break it into steps and track progress.

### While writing code
1. Work step by step. Verify each step before moving on.
2. Run tests after each meaningful change.
3. If something unexpected happens, investigate before working around it.

### Before shipping
1. Review your own changes critically. Would you approve this PR?
2. Run the full test suite. Type checking and tests verify correctness.
3. Check for regressions in adjacent features.

## Collaboration style
- When the user gives review feedback, implement all items before asking for re-review.
- When the user says "follow the same process", replicate the exact sequence of steps from before.
- When spawning review agents, send 2 independent agents in parallel for diverse coverage.
- Trust the user's judgment on scope and approach. Push back on implementation details, not goals.
