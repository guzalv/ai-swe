---
name: swe.ship
description: Commit, push, and create pull requests.
---

# Ship

Commit, push, and create pull requests.

## Standards

- **Atomic commits.** One logical change per commit.
- **Explain why, not what.** The diff shows what changed.
- **Stage specific files.** Never `git add -A` or `git add .`.
- **Never push to main/master** without explicit user instruction.
- **Never amend published commits** unless the user explicitly asks.
- **Never skip hooks** (`--no-verify`).

## Process

### 1. Prepare

- Run `git status` and `git diff` to verify changes.
- Check for secrets, credentials, large binaries, unintended files.

### 2. Commit

- Stage specific files by name.
- Write a commit message that explains why, not what.
- Create new commits -- don't amend unless user asks.

### 3. Push

- Push to the correct remote branch.
- Use `--force-with-lease` if rebased (never bare `--force`).

### 4. Create Pull Request

Use `gh pr create`:
- Title under 70 chars.
- Body with summary (what and why) and test plan.
- Link related issues.

### 5. Stacked PRs (if applicable)

- Push branches in order (base first).
- Rebase dependent branches.
- Use `--force-with-lease` for rebased branches.

If auth fails, ask the user for credentials.
