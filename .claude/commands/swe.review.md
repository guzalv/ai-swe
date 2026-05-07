---
name: swe.review
description: Critically evaluate code changes using independent review agents.
---

# Review

Evaluate changes before they ship. Use independent review agents for coverage.

## Process

### 1. Collect Prior Findings

Check if a review was already performed earlier in this conversation (e.g., by
a built-in review skill). If so, note those findings -- they will be included
in the agent prompt so the independent agents can verify, challenge, or extend
them. Do not discard prior work.

### 2. Identify What Changed

Determine the diff to review:
- Uncommitted changes: `git diff`
- Branch changes: `git diff main...HEAD` (adjust base branch as needed)
- PR: `gh pr diff {number}`

Get the list of changed files. Read each one to understand the full context.

### 3. Spawn Review Agents

Launch **2 review agents in parallel** using the Agent tool.

Both agents get **identical prompts**. Two independent passes on the same
problem minimize the chance of missing issues. Do not split focus areas.

**The agent prompt must be completely self-contained.** Sub-agents have zero
context from this conversation. Everything they need must be in the prompt:
the file paths, what changed, the review criteria, any project-specific
guidelines, and any prior review findings.

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

## Prior review findings

[If a prior review was performed, paste its findings here verbatim. Your job
is to independently verify these findings AND find anything they missed. If
no prior review exists, write "None -- this is the first review pass."]

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
- Run the existing test suite for affected packages. Report what passed and
  what failed. If tests fail, include the failure output.

**Production readiness**
- Hardcoded values that should be configurable?
- Timeouts, retries, limits reasonable?
- Observability (logging, metrics) for new behavior?
- Backwards compatibility concerns?

## What to skip

- Formatting nitpicks (that's for formatters).
- Refactors beyond the scope of this change.
- Personal style preferences.

## Evidence standard

Every finding MUST include hard proof. No vague claims.

- **Quote the code.** Include the exact file path, line number, and the
  relevant code snippet that shows the issue.
- **Run tests when possible.** If there is a test suite, run it and include
  the results. A claim like "this could break X" is weak -- a test command
  showing a failure is strong.
- **Show, don't speculate.** "This nil check is missing" must point to the
  exact line where a nil value can reach. "This race condition exists" must
  show the two unsynchronized access points.
- **No findings without evidence.** If you can't point to specific code or
  test output that supports a finding, don't report it.

## Prior finding verification

If prior findings were provided above, explicitly state for each one:
- **Confirmed** -- you independently found the same issue.
- **Disputed** -- you disagree, with evidence for why.
- **Cannot verify** -- you couldn't confirm or deny.

## Output

Group findings by severity:
- **Critical** -- blocks shipping: logic errors, data loss risks, security issues.
- **Medium** -- should fix: inconsistencies, missing edge cases, unclear code.
- **Low** -- nice to have: minor improvements, suggestions.

For each finding include:
1. File path and line number.
2. The relevant code snippet.
3. What the issue is and why it matters.
4. Test output if applicable.

If you find no issues, say so explicitly.
````

### 4. Synthesize Findings

After both agents return:
- Merge findings from both agents AND any prior review.
- Deduplicate overlapping issues.
- For prior findings: note which were confirmed, disputed, or unverified.
- Group by severity.
- Separate actionable from informational.

### 5. Address Findings

- **Critical**: Fix immediately. These block shipping.
- **Medium**: Fix unless the user explicitly defers.
- **Low**: Note for the user, let them decide.

Run tests after fixes to verify no regressions.

### 6. Report

Present concisely:
- What was found (grouped by severity).
- What was confirmed from prior reviews.
- What was fixed.
- What was deferred and why.
