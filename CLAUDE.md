# AI SWE Workflow

## Engineering Standards

### Project-specific guidelines
- Before starting work, look for project-specific guidelines: `CLAUDE.md`, `CONTRIBUTING.md`, `agents.md`, style guides, linter configs, `.editorconfig`.
- These take precedence over general defaults below. Follow them exactly.

### Code changes
- Minimal diffs. Change only what the task requires.
- No drive-by refactors, no cleanup that wasn't asked for.
- No premature abstractions. Three similar lines is better than a helper nobody asked for.
- Match existing project style -- indentation, naming, error handling, test patterns.
- No comments explaining what. Only comment why, and only when non-obvious.

### Error handling
- Only validate at system boundaries (user input, external APIs). Trust internal code.
- Don't add fallbacks for scenarios that can't happen.

### Testing
- Test behavior, not implementation.
- Prefer integration tests over mocks when practical.
- Use the project's existing test patterns and helpers.

### Commits and PRs
- Atomic commits: one logical change per commit.
- Commit messages: say why, not what.
- PR descriptions: summarize the change and how to test it.

## Review Standards

These standards apply to ALL review activity -- whether triggered by a built-in skill, a slash command, or any other mechanism.

### Evidence requirement
Every review finding MUST include hard proof:
- **Quote the code.** Exact file path, line number, and the relevant snippet.
- **Run tests when possible.** A test command showing failure is stronger than speculation.
- **Show, don't speculate.** "This nil check is missing" must point to the exact line.
- **No findings without evidence.** If you can't point to specific code, don't report it.

### Independent review agents
Reviews spawn **2 independent agents in parallel** with identical prompts. Two passes on the same problem minimize missed issues. Do not split focus areas between agents.

### Severity classification
- **Critical** -- blocks shipping: logic errors, data loss risks, security issues.
- **Medium** -- should fix: inconsistencies, missing edge cases, unclear code.
- **Low** -- nice to have: minor improvements, suggestions.

## Post-Review Redirect

**After any review completes** -- including a built-in review skill -- always follow up by running `/swe.review`. This ensures every review gets the full independent-agent treatment with proper evidence standards. The `/swe.review` command will aggregate any prior review findings with its own analysis.

## Commands

- `/swe.understand` -- Read code and build context before acting
- `/swe.implement` -- Make code changes step by step
- `/swe.review` -- Evaluate changes with independent review agents
- `/swe.test` -- Run tests and verify correctness
- `/swe.ship` -- Commit, push, create pull requests
