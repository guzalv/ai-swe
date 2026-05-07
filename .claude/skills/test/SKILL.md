---
name: test
description: Run tests, verify on real environments, check for regressions.
---

# Test

Verify changes work correctly through automated tests and manual verification.

## Standards

- **Test behavior, not implementation.** Tests should survive refactors.
- **Prefer integration tests over mocks** when practical.
- **Use the project's existing test patterns** and helpers.
- **Deterministic tests.** Avoid time-dependent assertions.

## Process

### 1. Run Unit Tests

- Run tests for affected packages. Use flags to bypass test cache when needed
  (e.g., `-count=1` for Go, `--no-cache` for others).
- Read failure output carefully -- distinguish test bugs from code bugs.
- Fix and re-run.

### 2. Run Broader Test Suite

- If the change touches shared code, run tests for dependent packages.
- Use judgment on scope -- more shared code means a wider test net.

### 3. Verify in Real Environment (when available)

- Build and deploy from the correct base.
- Exercise the feature end-to-end.
- Check logs and metrics.
- Test error paths when possible.
- Clean up test artifacts.

### 4. Report

- Which tests ran and passed.
- What was verified manually or on a real environment.
- Test gaps worth noting.
