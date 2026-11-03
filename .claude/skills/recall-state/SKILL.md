---
name: recall-state
description: Load the saved working state of this repo (written by /save-state into Session_Log.md and the *_Notes.md files) so work can continue on this PC. Pulls the latest from git first. Use at the start of a session, or when the user says "recall", "where were we", "continue my work", "load state", or similar.
---

# recall-state

Goal: rebuild enough context for this session to continue the user's work as if it were the same conversation, on a PC that may have no Claude memory of it.

## Steps

### 1. Sync from git first
- `git status --short`. If there are local uncommitted changes, note them and **don't** pull over them blindly.
- `git fetch`, then `git status -sb`.
  - **Behind, clean tree:** `git pull --ff-only`.
  - **Behind, dirty tree or diverged:** tell the user and ask before pulling, stashing or rebasing.
  - **Ahead:** mention that this PC has unpushed commits; another PC may be missing them.
- If the fetch fails (offline or auth), continue with the local copy and warn that the state may be stale.

### 2. Read the saved state
- Read `Session_Log.md` in full. `## Current State` is the authoritative summary, and the newest `## History` entry says what happened last.
- Read **every** notes file that Current State points to, plus any other root-level `*_Notes.md`. These hold the detailed analysis: tables, recommendations, drafts.
- `git log --oneline -15` to confirm the commits the log mentions, and to spot commits made after the last save (work done without saving state).
- Skim `CLAUDE.md` and `README.md` only if needed for orientation. Don't re-read the whole repo.

### 3. Check this PC's environment
- `hostname`: compare with the hostname in "Last saved by". If it differs, flag the machine-specific notes from the log as **not present here**, such as permission rules or memory.
- Check that tools named in Environment notes exist (e.g. `python -c "import pymupdf"`, `which antiword pdftotext`). Report anything missing and how to install it.
- Check that `source_documents/` exists here. It's git-ignored and arrives through another channel (e.g. OneDrive/SharePoint sync), so warn if it's missing or if specific files the notes depend on are absent.

### 4. Present the recap
Keep it scannable:
1. **Last session:** date, PC, one-line summary.
2. **Done:** key results and commits.
3. **In progress:** each active topic with its notes file.
4. **Waiting on you:** the open decisions, numbered, with options and the recommendation.
5. **Concerns:** risks to keep in mind.
6. **Sync/environment status:** pull result, unpushed or uncommitted work, missing tools or files.
7. **Suggested next step:** the first item from Next steps, with 1–2 alternatives.

End by asking which item to continue with. Don't start on any item until the user picks one.

### 5. While working afterwards
- Treat the "Requirements & constraints" in the log as binding, alongside `CLAUDE.md`.
- If the notes and the actual files disagree (e.g. someone edited a course file on another PC), trust the files, and point out the discrepancy.
- Before the user stops or switches PCs, suggest running `/save-state`.
