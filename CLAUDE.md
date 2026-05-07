# AI SWE Workflow

## Commands

- `/swe.understand` -- Read code and build context before acting
- `/swe.implement` -- Make code changes step by step
- `/swe.review` -- Evaluate changes with independent review agents
- `/swe.test` -- Run tests and verify correctness
- `/swe.ship` -- Commit, push, create pull requests

## Post-Review Redirect

**After any review completes** -- including a built-in review skill -- always follow up by running `/swe.review`. This ensures every review gets the full independent-agent treatment with proper evidence standards. The `/swe.review` command will aggregate any prior review findings with its own analysis.
