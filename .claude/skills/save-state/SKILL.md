---
name: save-state
description: Save the current working state of this repo (work done, in-progress analysis, open decisions, concerns, requirements, next steps) into Session_Log.md and commit + push it, so the work can be resumed on another PC with /recall-state. Use when the user says "save state", "save progress", "I'm switching PCs", "wrap up for today", or similar.
---

# save-state

Goal: record everything a fresh Claude session on a **different PC** needs to continue seamlessly. That PC will have none of this conversation, none of Claude's auto-memory (memory is per-PC and per-Windows-user and does not sync), and possibly different tools installed. Git is the only shared channel. `source_documents/` is git-ignored, so nothing inside it travels through git.

## Steps

### 1. Gather facts (don't rely on memory of the conversation alone)
Run these in parallel:
- `git status --short` and `git log --oneline -15`
- `git fetch` then `git status -sb`, to see whether local is behind or ahead of `origin/main`
- List root-level working-notes files: `*_Notes.md`, `Session_Log.md`
- Read the current `Session_Log.md` so you update it rather than duplicate it

Then review this conversation and collect:
- **Done:** files created or changed, commits made (hashes), decisions the user confirmed.
- **In progress:** analysis or drafts not finished, and which notes file holds the details.
- **Open decisions:** things waiting on the user's approval, phrased as questions, with the options and Claude's recommendation if one was given.
- **Concerns / risks:** bugs found, inconsistencies, things not yet verified, and edits to non-versioned files (e.g. `.doc` files in `source_documents/`, which have no git backup).
- **Requirements / constraints learned:** user preferences, formatting rules, accreditation rules, and anything not already in `CLAUDE.md` that a new session must respect.
- **Environment notes:** tool quirks discovered (e.g. `pdftotext` garbles Thai, so use PyMuPDF; `antiword` for `.doc`), and machine-specific config that will NOT exist on other PCs.
- **Next steps:** an ordered list, with the most likely next action first.

If something important lives only in this conversation (analysis results, tables, drafts) and not yet in any file, write it into the relevant `*_Notes.md` file, or create a new topic notes file at the repo root. `Session_Log.md` should **point to** notes files, not duplicate their content.

### 2. Update `Session_Log.md`
Keep this structure. Create the file if it's missing.

```markdown
# Session Log

Running log of work done with Claude Code in this repo, kept in git so it carries over between machines. Claude's own memory is per-PC and does not sync. Load it on another PC with /recall-state.

## Current State
_Last saved: YYYY-MM-DD HH:MM by <PC name from `hostname`>_

### Active work
- <topic>: <one-line status> → details in `<notes file>`

### Open decisions (waiting on user)
1. ...

### Concerns / risks
- ...

### Requirements & constraints to respect
- ...

### Environment notes
- ...

### Next steps
1. ...

## History
### YYYY-MM-DD (<hostname>)
- <what was done this session, commits with hashes>

### <older entries kept unchanged below>
```

Rules:
- **Overwrite** the `## Current State` section completely, so it always reflects *now*. Drop items that are resolved.
- **Prepend** a new dated entry under `## History`, newest first. Never delete older history entries. If an older log has no `Current State` / `History` split, move its existing dated entries under `## History` as they are.
- Use absolute dates (convert "today" or "yesterday"). Get the hostname with `hostname`.
- Be specific: file paths, course codes, commit hashes, PO/PI numbers. Vague entries ("worked on PIs") are useless on the other PC.
- Keep Thai terms as they appear in the source documents.

### 3. Commit and push
- Stage `Session_Log.md`, all root-level `*_Notes.md` files, and any repo files changed this session that the user wants kept. Do **not** stage `.claude/settings.local.json` or anything git-ignored.
- If unrelated or half-finished changes are in the working tree, list them and ask the user whether to include them. Don't sweep them in silently.
- Commit message: `Save session state: <short topic summary>`, ending with the attribution trailer required by the current session instructions.
- If local is behind `origin/main`, run `git pull --rebase` before pushing. On a conflict in `Session_Log.md`, merge both sides by hand: keep both History entries, rebuild Current State from both, and then continue.
- Push to `origin main`. If the push fails (auth or network), tell the user the state is committed locally but NOT synced, and show the command to retry.

### 4. Report to the user
A short summary: what was saved, the commit hash, whether the push succeeded, and the top 1–3 next steps. Remind them that the other PC should run `/recall-state`, which also pulls.
