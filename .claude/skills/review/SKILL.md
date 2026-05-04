---
name: review
description: Critically evaluate code changes using independent review agents.
---

# Review

Critically evaluate the changes before they ship. Use independent review agents
for thorough coverage.

## Process

### 1. Spawn Independent Review Agents

Launch **2 review agents in parallel** using the Agent tool. Each agent should:

- Receive the full list of changed files
- Review independently (no shared context between agents)
- Report findings with severity levels (critical, medium, low)

Give both agents the **exact same task, context, and instructions**. The point
of two agents is redundancy -- two independent passes on the same problem
minimize the chance of missing issues. Do not split focus areas between them.

Each agent prompt must be self-contained -- include the file paths, what
changed, and what to look for. The agent has no context from this conversation.

### 2. Synthesize Findings

After both agents complete:
- Merge their findings, deduplicate overlapping issues
- Group by severity
- Identify which findings need action vs which are informational

### 3. Address Findings

For each actionable finding:
- **Critical**: Fix immediately. These block shipping.
- **Medium**: Fix unless the user explicitly decides to defer.
- **Low**: Note for the user, let them decide.

After fixing, run tests to verify fixes don't introduce regressions.

### 4. Report

Present a concise summary:
- What the review agents found (grouped by severity)
- What was fixed
- What was deferred and why

## What Good Review Looks For

### Correctness
- Does the code do what it claims to do?
- Are there off-by-one errors, nil pointer risks, race conditions?
- Are error paths handled correctly?

### Consistency
- Does the code follow the project's existing patterns?
- Are names consistent with the rest of the codebase?
- Is the error handling style consistent?

### Testing
- Are the tests testing behavior or implementation?
- Are edge cases covered?
- Are test assertions specific enough?
- Could tests pass for the wrong reasons?

### Production Readiness
- Are there hardcoded values that should be configurable?
- Are timeouts, retries, and limits reasonable?
- Is there observability (logging, metrics) for new behavior?
- Are there backwards compatibility concerns?

### What Review Does NOT Do
- Nitpick formatting (that's what formatters are for)
- Suggest refactors beyond the scope of the change
- Impose personal style preferences
