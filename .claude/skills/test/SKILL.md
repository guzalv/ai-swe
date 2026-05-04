---
name: test
description: Run tests, verify on real environments, check for regressions.
---

# Test

Verify the changes work correctly -- in unit tests, integration tests, and
when possible, against real environments.

## Process

> **Follow project-specific guidelines.** Check for `agents.md`,
> `CONTRIBUTING.md`, style guides, and linter configs discovered at session
> start. They take precedence over general defaults below.

### 1. Run Unit Tests

Run the test suite for the affected packages:

```
go test ./path/to/package/... -count=1
```

Use `-count=1` to bypass the test cache when you need fresh results.

If tests fail:
- Read the failure output carefully.
- Distinguish between test bugs and code bugs.
- Fix and re-run.

### 2. Run Broader Test Suite

If the change touches shared code (utilities, types, interfaces), run tests
for dependent packages too. Use your judgment on scope -- don't run the entire
monorepo test suite for a one-file change.

### 3. Test Against Real Environment

When a real cluster or environment is available:

**Build and deploy:**
- Build the binary from the correct base commit (match the running
  environment's version).
- Use `crane mutate` to patch a single binary into an existing container image.
- Push to a temporary registry (e.g., `ttl.sh`) and update the deployment.
- Wait for rollout to complete before testing.

**Verify behavior:**
- Check logs for expected startup behavior.
- Exercise the new feature end-to-end.
- Check metrics/observability endpoints.
- Test kill switches and configuration overrides.
- Test error paths when possible.

**Clean up:**
- Remove test artifacts from the environment.
- Restore original configuration.
- Document what was tested and what passed.

### 4. Report Results

Summarize:
- Which tests ran and passed
- What was verified manually or on a real environment
- Any test gaps worth noting

## Guidelines

- **Test behavior, not implementation.** Don't test that a function calls
  another function -- test that the observable output is correct.
- **Prefer deterministic tests.** Avoid time-dependent assertions. Use direct
  method calls instead of relying on background goroutines/timers.
- **Use large intervals for background workers in tests** (e.g., 24h ticker
  intervals) to prevent automatic execution from interfering. Call the worker
  method directly for deterministic control.
- **When testing against a cluster, verify DB compatibility.** A binary built
  from a newer commit may expect a different schema version than the running
  database.
