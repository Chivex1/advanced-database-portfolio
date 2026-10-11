# Cursor project rules

## Git push (always)

When the user asks to **push** (or publish commits to GitHub):

1. Read `GITHUB_TOKEN` from the repo-root `.env` file (never print, log, or commit the token).
2. Push with HTTPS using that token, e.g.  
   `https://x-access-token:${GITHUB_TOKEN}@github.com/<owner>/<repo>.git`  
   targeting the current branch (usually `main`).
3. Do **not** rely on interactive `gh` / credential-manager prompts in this environment.
4. Never stage or commit `.env`.
5. After a successful push, confirm with `git status -sb` (branch should not be ahead).

If `GITHUB_TOKEN` is missing or GitHub returns auth errors, tell the user to refresh the PAT in `.env` — do not invent credentials.
