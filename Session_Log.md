# Session Log

Running log of work done with Claude Code in this repo, kept in git so it carries over between machines. Claude's own memory is per-PC and does not sync. Load it on another PC with /recall-state.

## Current State
_Last saved: 2026-11-03 20:38 by Hedwig_

### Active work
- **TABEE PO–PI–CLO matrix (draft):** `CPE_RMUTT68_PO_PI_CLO_Matrix.md` covers all 64 courses and 295 CLOs.
  - The CLO→PO links come from the course files. The CLO→PI choices are Claude's proposal, following the rules in §5 of that file, and still need committee review.
  - It includes a coverage table against the TABEE direct/indirect minimums, issues (§4) and a proposed course for each PI's direct assessment (§4.5).
- **Sydney Accord curriculum review:** source documents have been reviewed. Findings and gaps in the CPE 2568 structure are in `TABEE_Sydney_Accord_Curriculum_Notes.md`.
- **CPE-specific PI catalog analysis:** not started beyond analysis. See `TABEE_PI_Analysis_Notes.md`. Proposed output file: `CPE_RMUTT68_TABEE_PI_Reference.md`.
- **04-621-202 Electronics course redesign:** CLO K/S/A and PI fixes, a 10-week plan and a bibliography are drafted but not yet written into the `.doc`. See `Electronics_04-621-202_Course_Design_Notes.md`.

### Open decisions (waiting on user)
1. **Approve or adjust the PI assignments** in `CPE_RMUTT68_PO_PI_CLO_Matrix.md`. Once approved, should a PI column be added to each course file's CLO table?
2. **How to close the PI coverage gaps in required courses:**
   - No required course covers 2.1, 4.1, 4.2, 7.2, 8.1, 8.2 or 11.2. PI1.2 has 1 course where it needs 2.
   - Claude's proposal (matrix §4.1): add CLOs to 04-620-301 Seminar (4.1, 7.2, 11.2), 04-620-302 (4.2, 8.2), 04-620-401 (PO3, PO4), 04-621-201/202 (2.1, 8.1) and 04-622-302 (10.1).
3. **Capstone structure.** Pre-Project 04-620-303 is 1(0-3) in Y3/S2. Project 04-620-401 is 3(1-6) in Y4/S2, with Y4/S1 taken by co-op. TABEE wants 2 consecutive semesters in year 4. Options:
   - justify the gap in the self-evaluation report (SER);
   - restructure the courses; or
   - count CWIE / 04-000-402 as capstone evidence.
4. **Split the 18 CLOs that cover more than one PO** (marked †, mostly PO6+PO7, plus PO2+PO4)? Also reword the 13 CLOs marked ⚑ whose wording doesn't fit their PO.
5. **Electronics 04-621-202** (from earlier sessions):
   - write the CLO/PI fixes, the Learning Management checkboxes, the 10-week plan and the bibliography into the `.doc`;
   - approve the CLO7 split.
   - Note: the matrix uses PI2.3 for CLO4, while the Electronics notes suggested PI2.4.
6. **PI10.1 domain:** K3-Apply, A4 or S3/S4. This affects the CPE PI reference document.
7. **Update Prospectus §12** to state the Sydney Accord / ETAC track and list the 11 TABEE POs?

### Concerns / risks
- PO4 has no CLO in any required course; every PO4 CLO is in an elective. This blocks the direct-assessment minimums.
- PO8 CLOs talk about "applying to other disciplines", but none asks students to judge impacts (ให้ความเห็นเกี่ยวกับผลกระทบ), which is what every PO8 PI requires.
- 04-620-401 (Project) has no PO3 or PO4 CLO. TABEE requires the capstone to assess PO2, 3, 4, 6, 7 and 8.
- To submit in 2570, TABEE needs at least 2 consecutive years of PO assessment data, so collection must start by 2568–2569.
- Template bug: `OBE3_TABEE.doc` labels PI11.2 as "PO12". It belongs under PO11.
- It isn't confirmed whether broadly-defined problems need at least 4 SP characteristics; complex problems need 4. It also isn't confirmed whether the Council of Engineers recognises Sydney Accord degrees for licensing (the NK deck says "to be confirmed").
- `source_documents/` is git-ignored. Edits to `.doc` files there have no backup, so back up before editing.

### Requirements & constraints to respect
- Follow `CLAUDE.md`:
  - course types are กลุ่มวิชาศึกษาทั่วไป, กลุ่มวิชาพื้นฐาน, กลุ่มวิชาบังคับ, กลุ่มวิชาเลือก and กลุ่มเสริมสร้างประสบการณ์ในวิชาชีพ;
  - the credit format is X(Y-Z).
- The program targets **TABEE under the Sydney Accord (ETAC)**, using SK1–SK9 and broadly-defined problems. Submission is planned for academic year 2570.
- Use the RMUTT LO Writing Manual's PI catalog (PI1.1–PI11.2, 23 PIs), not the WA-style PI numbering from ศ.สมศักดิ์'s slides.
- Rule: **one CLO answers only one PI.**
- Minimum assessments per PI:
  - PO1–3: at least 2 direct + 1 indirect.
  - PO4–11: at least 1 direct + 2 indirect.
  - Count only courses that every student takes.
- PO→PLO mapping: PO1→PLO1, PO2→PLO4, PO3→PLO2, PO4→PLO4, PO5→PLO5, PO6/PO7/PO10→PLO8, PO8→PLO3, PO9→PLO6, PO11→PLO7.
- Tables: the user prefers compact tables that fit one line per row, so drop a column rather than let it wrap.

### Environment notes
- **Thai PDF text:** `pdftotext` garbles it, so use PyMuPDF (`import pymupdf`) instead. Some slides are images only.
- **Legacy `.doc` files:** read them with `antiword -m UTF-8.txt`.
- **Python:** use `python -I`. If printing Thai to the console fails with a cp1252 error, call `sys.stdout.reconfigure(encoding="utf-8")` (`-I` ignores `PYTHONIOENCODING`).
- **Bash heredocs** containing Thai and quotes broke once. Write scripts with the Write tool instead.
- **The matrix can be regenerated** by parsing the course files: CLO tables plus the `<tr><th>TABEE PO</th>` HTML row in each file's PLO Mapping table. The generator script was in a scratchpad and was not kept; the rules it used are in matrix §5.
- **Project skills** `/save-state` and `/recall-state` live in `.claude/skills/` and are tracked in git.
- **Git in a OneDrive/SharePoint-synced folder:** commits can fail with `unable to append to '.git/logs/refs/heads/main'`. Fix it with `git config windows.appendAtomically false`. This is set in this clone's `.git/config` and must be set again in each new clone.
- **Git identity:** Hedwig has no git `user.name` or `user.email` set. Commits there used `git -c user.name=thanasin -c user.email=thanasin.b@gmail.com commit ...`, matching the earlier commits. The user can set it permanently with `git config --global user.name/user.email`.
- **Other PC only:** a Read-permission rule for the memory folder (`C:\Users\ADMIN\...`) exists only in that PC's `~/.claude/settings.json`. This PC (Hedwig, user `tolbo`) has no such rule and no project memory.
- `source_documents/LINE/` holds phone screenshots, e.g. `S__8339462_0.jpg`, which is IE's "CLO-PLO Matrix IE" Excel sheet, the model for the PO–PI–CLO matrix.

### Next steps
1. Review the matrix with the committee and decide the gap fixes (open decisions 1–4).
2. Once approved, add a PI column to each course file's CLO table, and split or reword the CLOs marked † and ⚑.
3. Draft `CPE_RMUTT68_TABEE_PI_Reference.md` (CPE-adapted PI catalog; see `TABEE_PI_Analysis_Notes.md`).
4. Update Prospectus §12 to name the Sydney Accord / ETAC track.
5. Continue the Electronics 04-621-202 write-up into the `.doc`.

## History
### 2026-11-03 (Hedwig)
- Recalled the previous state from `Session_Log.md` and the two untracked notes files.
- Reviewed all `source_documents/` training material for Sydney Accord curriculum design: the SPP and ศ.สมศักดิ์ workshop decks, the NK deck, the SER manual and the capstone deck. Wrote `TABEE_Sydney_Accord_Curriculum_Notes.md`, covering:
  - WA vs SA differences and the SP1–SP7 problem characteristics;
  - Criterion 5 rules (SA: up to 5 years, no math/science credit minimum);
  - assessment minimums and capstone rules;
  - 6 gaps in the CPE 2568 structure.
- Created the project skills `.claude/skills/save-state/SKILL.md` and `.claude/skills/recall-state/SKILL.md`. Restructured this log into Current State and History.
- Reviewed `source_documents/LINE/S__8339462_0.jpg` (IE's PO-PI-CLO Matrix sheet), then built `CPE_RMUTT68_PO_PI_CLO_Matrix.md` in the same layout and linked it from `README.md`, `Course_Index.md`, `CPE_RMUTT68_PLO_CLO_Matrix.md` and `CPE_RMUTT68_TABEE_PO_Mapping.md`.
- Committed for the first time: `TABEE_PI_Analysis_Notes.md` and `Electronics_04-621-202_Course_Design_Notes.md`, both carried over from earlier sessions.

### 2026-09-08

**Done, committed and pushed to `origin/main`:**

- Created `Course_Index.md` at the repo root. It links all 64 course `.md` files under `courses/`, grouped by category (Foundation, Core, Electives × AI/Hardware/Network/Software, CWIE), with Thai/English names and credits from each file's YAML frontmatter.
- Linked `Course_Index.md` from `CPE_RMUTT68_Prospectus.md` in two places: the §3 PLO reference line and the top of §8 (Core Courses).
- Iterated on table formatting per feedback. The Foundation, Core and CWIE tables first had a "ชั้นปี/ภาค" (year/semester) column; it kept wrapping onto two lines even after compacting the text, so the column was dropped. All category tables now use the same 4-column layout (code, Thai name, English name, credits).
- Commits: `ca73d6f` (add Course_Index.md), `9b1a74c` (compact year/sem format, superseded), `70ca2ed` (drop ชั้นปี/ภาค column, current state).

**Still open / untracked (not part of this session's work, carried over from earlier):**

- `Electronics_04-621-202_Course_Design_Notes.md` and `TABEE_PI_Analysis_Notes.md` remain untracked at the repo root. They are pending notes on the 04-621-202 course redesign and the TABEE PI catalog analysis. Neither has been written into the real `.doc` files yet (those live under `source_documents/`, outside git). See these files for full details.

**Machine-specific config (does NOT carry over to other PCs):**

- On this PC, added a permission rule to `~/.claude/settings.json` that allows `Read` access to this project's Claude auto-memory folder (under `C:\Users\ADMIN\.claude\projects\...\memory\`) without prompting. This setting is local to this Windows profile. It won't exist on other PCs, and Claude's auto-memory is also per-PC (not synced through git), so a fresh machine starts without either. This log file is the portable substitute.
