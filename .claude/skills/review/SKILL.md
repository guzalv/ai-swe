---
name: review
description: Critically evaluate code changes using independent review agents.
---

# Review

Evaluate changes before they ship. Use independent review agents for coverage.

## Process

### 1. Identify What Changed

Determine the diff to review:
- Uncommitted changes: `git diff`
- Branch changes: `git diff main...HEAD` (adjust base branch as needed)
- PR: `gh pr diff {number}`

Get the list of changed files. Read each one to understand the full context.

### 2. Spawn Review Agents

Launch **2 review agents in parallel** using the Agent tool.

Both agents get **identical prompts**. Two independent passes on the same
problem minimize the chance of missing issues. Do not split focus areas.

**The agent prompt must be completely self-contained.** Sub-agents have zero
context from this conversation. Everything they need must be in the prompt:
the file paths, what changed, the review criteria, and any project-specific
guidelines.

Build the prompt using this template (fill in the bracketed sections):

````
You are reviewing code changes for correctness, consistency, and production
readiness. Read every changed file listed below in full, then report your
findings.

## Changed files

[list every changed file path, one per line]

## What changed

[1-3 sentence summary of what this change does and why]

## Project guidelines

[paste any project-specific guidelines discovered earlier, or write "None"]

## Review checklist

Evaluate each file against these criteria:

**Correctness**
- Does the code do what it claims?
- Off-by-one errors, nil/null risks, race conditions?
- Error paths handled correctly?
- Edge cases covered?

**Consistency**
- Follows the project's existing patterns (naming, error handling, structure)?
- No unnecessary style changes mixed with functional changes?

**Testing**
- Tests cover behavior, not implementation details?
- Edge cases tested?
- Assertions specific enough? Could tests pass for wrong reasons?

**Production readiness**
- Hardcoded values that should be configurable?
- Timeouts, retries, limits reasonable?
- Observability (logging, metrics) for new behavior?
- Backwards compatibility concerns?

## What to skip

- Formatting nitpicks (that's for formatters).
- Refactors beyond the scope of this change.
- Personal style preferences.

## Output

Group findings by severity:
- **Critical** -- blocks shipping: logic errors, data loss risks, security issues.
- **Medium** -- should fix: inconsistencies, missing edge cases, unclear code.
- **Low** -- nice to have: minor improvements, suggestions.

For each finding, include the file path, line number, what the issue is, and
why it matters. If you find no issues, say so explicitly.
````

### 3. Synthesize Findings

After both agents return:
- Merge findings and deduplicate overlapping issues.
- Group by severity.
- Separate actionable from informational.

### 4. Address Findings

- **Critical**: Fix immediately. These block shipping.
- **Medium**: Fix unless the user explicitly defers.
- **Low**: Note for the user, let them decide.

Run tests after fixes to verify no regressions.

### 5. Report

Present concisely:
- What was found (grouped by severity).
- What was fixed.
- What was deferred and why.
