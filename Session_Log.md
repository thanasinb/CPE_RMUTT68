# Session Log

Running log of work done with Claude Code in this repo, kept here (git-tracked) so it carries over between machines — Claude's own memory system is per-PC and does not sync.

## 2026-09-08

**Done, committed and pushed to `origin/main`:**

- Created `Course_Index.md` at repo root — links to all 64 course `.md` files under `courses/`, grouped by category (Foundation, Core, Electives × AI/Hardware/Network/Software, CWIE), with Thai/English names and credits pulled from each file's YAML frontmatter.
- Linked `Course_Index.md` from `CPE_RMUTT68_Prospectus.md` in two places: the §3 PLO reference line and the top of §8 (Core Courses).
- Iterated on table formatting per feedback: originally included a "ชั้นปี/ภาค" (year/semester) column in the Foundation/Core/CWIE tables; it kept wrapping onto two lines even after compacting the text, so the column was dropped entirely. All category tables now use the same 4-column layout (code, Thai name, English name, credits).
- Commits: `ca73d6f` (add Course_Index.md), `9b1a74c` (compact year/sem format — superseded), `70ca2ed` (drop ชั้นปี/ภาค column — current state).

**Still open / untracked (not part of this session's work, carried over from earlier):**

- `Electronics_04-621-202_Course_Design_Notes.md` and `TABEE_PI_Analysis_Notes.md` remain untracked at repo root — pending notes on the 04-621-202 course redesign and the TABEE PI catalog analysis. Neither has been written into the real `.doc` files yet (those live under `source_documents/`, outside git). See these files directly for full details.

**Machine-specific config (does NOT carry over to other PCs):**

- On this PC, added a permission rule to `~/.claude/settings.json` allowlisting `Read` access to this project's Claude auto-memory folder (under `C:\Users\ADMIN\.claude\projects\...\memory\`) without prompting. This setting is local to this Windows profile — it won't exist on other PCs, and Claude's auto-memory itself is also per-PC (not git-synced), so a fresh machine starts without either. This log file is the portable substitute.
