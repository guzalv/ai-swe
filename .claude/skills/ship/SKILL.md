---
name: ship
description: Commit, push, and create pull requests.
---

# Ship

Commit the changes, push to remote, and create a pull request.

## Process

> **Follow project-specific guidelines.** Check for `agents.md`,
> `CONTRIBUTING.md`, style guides, and linter configs discovered at session
> start. They take precedence over general defaults below.

### 1. Prepare Commit

Before committing:
- Run `git status` to see all changed files.
- Run `git diff` to review the full diff one more time.
- Verify no secrets, credentials, or large binaries are staged.
- Verify no unintended files are included.

### 2. Commit

- Stage specific files by name (avoid `git add -A` or `git add .`).
- Write a commit message that says **why**, not what:
  - First line: imperative, under 72 characters
  - Body: context, motivation, what alternative was considered
- One logical change per commit. If the work has distinct parts, make separate
  commits.

### 3. Push

- Push to the correct remote branch.
- If pushing to a PR branch, use the branch naming convention the project uses.
- If the branch has been rebased, use `--force-with-lease` (never bare
  `--force`).
- If pushing to a stacked PR, rebase dependent branches and push them too.

### 4. Create Pull Request

Use `gh pr create` with:

```
gh pr create --title "short title" --body "$(cat <<'EOF'
## Summary
- What changed and why (1-3 bullets)

## Test plan
- [ ] How to verify this works

Generated with AI assistance
EOF
)"
```

- Title: under 70 characters, says what the PR does
- Body: summary of changes + test plan
- Link related issues

### 5. Handle Stacked PRs

If the change spans multiple PRs:
- Push each branch in order (base first).
- Rebase dependent branches onto updated base branches.
- Resolve merge conflicts carefully -- understand what each side contributes
  before choosing.
- Force-push dependent branches with `--force-with-lease`.

## Guidelines

- **Never push to main/master without explicit user instruction.**
- **Never amend published commits** unless the user explicitly asks.
- **Always create new commits** rather than amending, especially after hook
  failures.
- **If auth fails**, ask the user to provide credentials rather than guessing
  at workarounds.
