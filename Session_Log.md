# Session Log

Running log of work done with Claude Code in this repo, kept in git so it carries over between machines. Claude's own memory is per-PC and does not sync. Load it on another PC with /recall-state.

## Current State
_Last saved: 2026-11-11 22:11 by DESKTOP-P9E7MNF_

### Active work
- **Sub-PLOs (done, commit `1f294ad`):** PLO4 and PLO8 are replaced in **all** CLO mappings by sub-PLOs, so each TABEE PO maps to exactly one PLO:
  - PLO4.1→PO2, PLO4.2→PO4, PLO8.1→PO6, PLO8.2→PO7, PLO8.3→PO10.
  - The full breakdown (parent PLO4/PLO8 text unchanged, in bold, with ↳ sub-rows and a TABEE PO column) is in `CPE_RMUTT68_Prospectus.md` §3. Anchors are `#plo4-1` … `#plo8-3`.
  - Changed together: the 64 course files (`plos:` frontmatter, CLO-table links, PLO responsibility table, HTML PLO Mapping header, TABEE PO table), `CPE_RMUTT68_PLO_CLO_Matrix.md`, `CPE_RMUTT68_TABEE_PO_Mapping.md`, `README.md`, and `tools/build_po_pi_clo_matrix.py` (`PO_PLO` now uses string keys like `'4.1'`; it asserts 13 PLO anchors in the Prospectus).
  - The YLO table (Prospectus §4) was deliberately left at parent level (PLO4, PLO8). `Old_PLO.md` and `PO_Mapping_Review/` are historical and were not changed.
  - The one-off migration script was not kept in the repo; it must not be re-run.
- **TABEE assessment rules for the program committee (COET + ETAC SER-writing docs):** analysis done → `TABEE_COET_Documents_Notes.md`.
  - §1–10 cover the COET folder (WA-based): criteria checklist, direct/indirect rules, capstone, Course Portfolio, site visit, IAB, and 12 CPE gaps.
  - §11 covers `source_documents/เอกสาร SER Writing/`: `2. ETAC Seminar SER Preparation_NTK.pdf` and `2._ETAC_SER_รายงานประเมินตนเองของสถาบันการศึกษา.docx` (the ETAC SER template CPE should use). **ETAC rules override the WA docs where they differ.**
  - Key ETAC rules: credits ≥120 total / ≥45 engineering / ≥24 GE, no math/science minimum; ≥210 h industrial practice; 1 PI ↔ exactly 1 SK; lean matrix (only courses that assess); per-PO/per-year assessment-plan table; **PI achievement = weighted sum, total indirect weight ≤ ½ of one direct weight** (IE example: 0.45×56% + 0.45×66% + 0.10×70% = 61.9% vs 60% target); 3-level CQI (lecturer / committee / IAB-IAC); example PEV document requests.
- **TABEE PO–PI–CLO matrix (draft):** `CPE_RMUTT68_PO_PI_CLO_Matrix.md` and `CPE_RMUTT68_PO_PI_CLO_Matrix.xlsx` cover all 64 courses (294 CLOs).
  - **CLO→PI sources:**
    - For the **6 courses with a filled OBE3-TABEE** (04-621-101, 04-621-202, 04-622-201, 04-624-201, 04-000-301, 04-622-302), CLOs, PIs, CLO levels and targets come from the lecturer's OBE3 (tagged "(OBE3)").
    - All other courses use Claude's draft rules (matrix §5) on top of the CLO→PO mapping in the course files.
  - **The `.md` contains:**
    - the PI catalog with taxonomy levels and the SK1–SK9 table;
    - the matrix;
    - coverage against TABEE minimums;
    - **§3.1, a generated comparison of each OBE3 with its course file**;
    - issues (§4) and the proposed direct-assessment courses (§4.5).
    - Every PLO/PO/PI/SK/CLO is a link with a hover tooltip.
  - **The `.xlsx`** (sheets: README · PO-PI-CLO Matrix · **PO1–PO11** · CLO List · PI Catalog · SK) is formula-driven:
    - The editable inputs on the CLO List sheet are PI, ⚑ note, CLO level and target %.
    - The PO1–PO11 sheets follow IE's per-PO layout. Each PI lists its direct rows (Y/N to use; §4.5 proposals start as Y) and 2 indirect rows (Student Exit Survey and Co-op Employer Survey).
    - They also have a CLO-level vs PI-level check, an attainment % input and a PI summary row.
    - Excel recalculated all 3,542 formulas with 0 errors, and the matrix values match the `.md`.
  - **Current coverage:**
    - ❌ 4.1, 7.2, 8.1, 8.2, 11.2.
    - ⚠️ 2.1 and 2.2 (1 of 2 required courses).
    - Everything else ✅.
  - **Don't hand-edit generated files.** Rebuild in this order:
    1. `python -I tools/extract_obe3.py` (only after OBE3 PDFs change; it needs the `source_documents/` PDFs and writes `tools/obe3_clo_pi.json`);
    2. `python -I tools/build_po_pi_clo_matrix.py` (the `.md`);
    3. `python -I tools/build_po_pi_clo_xlsx.py` (the `.xlsx`, which also rebuilds the `.md`).
    - Edit the §4–5 text in `tools/po_pi_clo_matrix_sections.md`. Override single-CLO draft PIs in `OV`/`FLAG` in the matrix script.
    - Rebuilding the `.xlsx` **overwrites edits made inside it**. Once the committee starts editing the workbook, treat it as the master copy.
- **Sydney Accord curriculum review:** done. Findings and gaps are in `TABEE_Sydney_Accord_Curriculum_Notes.md`.
- **CPE-specific PI catalog analysis:** not started beyond analysis. See `TABEE_PI_Analysis_Notes.md`. Proposed output: `CPE_RMUTT68_TABEE_PI_Reference.md`.
- **04-621-202 Electronics redesign:** see `Electronics_04-621-202_Course_Design_Notes.md`. The OBE3 PDF now shows CLO3 at K3 and CLO4 at K4, so some fixes from those notes have already been applied in the `.doc`.

### Open decisions (waiting on user)
0. **🔴 Which curriculum/cohorts does the 2570 submission assess?** TABEE needs ≥2 graduating classes, and the CPE 2568 curriculum has no graduates by 2570. The ETAC IE example reports AY2568 PO data from "(63)" courses (2563 curriculum), i.e. the graduating cohorts' curriculum. Options: (a) submit 2570 on the previous CPE curriculum's courses/CLOs and build a second matrix for it; (b) ask TABEE about provisional/new-program accreditation; (c) delay submission until the 2568 curriculum has 2 graduating classes. Claude asked; no answer yet. Details in `TABEE_COET_Documents_Notes.md` §3 and §11.
1. **Update the course `.md` files to match the 6 OBE3s**, so repo CLOs agree with the lecturers' syllabi? Claude asked and has no answer yet. The differences are in matrix §3.1:
   - Software Engineering adds a new CLO1, drops the old CLO1–2 and renumbers the rest;
   - 04-000-301 has 3 entirely new CLOs;
   - Electronics CLO1–2 are shortened.
2. **Software Engineering course code:** the OBE3 says 04-622-301, but the curriculum and repo say 04-622-302 (04-622-301 is Full-stack Web). Which is right? Mapped in `tools/extract_obe3.py` `DOC_TO_REPO`.
3. **Approve or adjust the PI assignments**, both the draft ones and the OBE3-sourced ones. Should a PI column then be added to each course file's CLO table?
4. **Close the coverage gaps (matrix §4.1):**
   - 4.1, 7.2 and 11.2 could all go into 04-620-301 Seminar;
   - 8.1 and 8.2 need CLOs that ask students to judge impacts (04-620-302/401, 04-621-201/202);
   - 2.1: also map 04-621-201 CLO4;
   - 2.2: keep 04-622-201 CLO4 at PI2.2 (the OBE3 moved it to 4.2), or add another CLO.
5. **Is PI4.2 really assessed by 04-624-201 CLO3?** That CLO is about designing formal-language models, while PI4.2 is designing and running experiments. If not, PO4's direct assessment rests only on 04-622-201 CLO4.
6. **Capstone structure:** Pre-Project 04-620-303 is 1(0-3) in Y3/S2 and Project 04-620-401 is 3(1-6) in Y4/S2, with co-op in Y4/S1. Should the program justify the gap, restructure the courses, or count CWIE as capstone evidence? Separately, 04-620-401 has no PO3 or PO4 CLO.
7. **Split the CLOs marked † and reword those marked ⚑?** For OBE3 courses, the level problems are listed in matrix §3.1.
8. **Electronics `.doc` write-up** (from earlier sessions), and the PI10.1 domain question (K3 / A4 / S3–S4).
9. **Update Prospectus §12** to state the Sydney Accord / ETAC track?
10. **Indirect assessment:** adopt IE's model of 2 program-wide surveys (Student Exit Survey and Co-op Employer Survey) for every PI? The questions must target each PO.
11. **Make the workbook's PI attainment % formula-driven** using the ETAC weighting rule (indirect total ≤ ½ of one direct)? Currently a plain input on the PO1–PO11 sheets. Claude offered; no answer yet.
12. **Make a committee-facing page/doc from `TABEE_COET_Documents_Notes.md` §10 (12 gaps)?** Offered, not accepted.
13. **18 CLOs map to more than one sub-PLO**, which breaks "one CLO → one PLO". They are kept as they were (shown as e.g. `PLO8.1, PLO8.2`):
    - PLO4.1 + 4.2: 04-624-302 CLO5, 04-621-403 CLO3, 04-621-404 CLO3, 04-622-307 CLO4, 04-622-401 CLO5.
    - PLO8.1 + 8.2: the 13 standard "teamwork + communication" CLOs (e.g. 04-620-303 CLO6, 04-620-401 CLO6, 04-621-302 CLO6, 04-000-302/303/401/402 CLO4).
    - 04-620-302 CLO6 maps to all of PLO8.1, 8.2 and 8.3.
    - Options: Claude proposes a split or a single sub-PLO per CLO, or flag them ⚑ for the lecturers. Claude asked; no answer yet.

### Concerns / risks
- **OBE3 quality problems** (matrix §3.1):
  - CLO levels below the PI level: PI3.1 (K6) gets K3 CLOs from 04-621-202, 04-624-201 and 04-622-302; PI1.1 (K3) gets K2 from Electronics CLO1–2; PI9.1 (A3) gets A1 from 04-622-302 CLO5 and 04-000-301 CLO2.
  - PI levels typed incorrectly: Electronics PI2.1 as K5 and PI6.1 as A4; Data Structure PI1.2 as K4.
  - 04-000-301 CLO1 is A2 but is mapped to PI7.1 (S3).
- **PO4 and PO10 are thin at PLO level:** PLO4.2 has only the 5 shared CLOs above, and PLO8.3 has only 04-620-302 CLO6. This matches the PO-PI-CLO coverage gaps.
- PO8 CLOs talk about "applying to other disciplines", but none asks students to judge impacts (ให้ความเห็นเกี่ยวกับผลกระทบ).
- To submit in 2570, at least 2 consecutive years of PO assessment data are needed, so collection must start by 2568–2569. **Combined with open decision 0, the current 2568-curriculum matrix may not be what gets assessed in 2570.**
- Annual TABEE cycle: SER due week 1 of May → visit Nov–Dec → decision March → result May.
- Capstone must show PO2/3/4/6/7; 04-620-401 has no PO3/PO4 CLO. Co-op can count as capstone evidence (SER item 5-1.6) only with an equivalence plan, judged against the broadly-defined definition.
- Template bug: `OBE3_TABEE.doc` labels PI11.2 as "PO12". It belongs under PO11.
- Unconfirmed:
  - whether broadly-defined problems need a minimum number of characteristics (the Manual lists 8 broadly-defined characteristics, which differ from SP1–SP7, and states no minimum);
  - whether the Council of Engineers recognises Sydney Accord degrees for licensing.
- `source_documents/` is git-ignored. Back up `.doc` files before editing them.

### Requirements & constraints to respect
- Follow `CLAUDE.md`: the course types listed there, and the credit format X(Y-Z).
- The program targets **TABEE under the Sydney Accord (ETAC)**, with submission planned for academic year 2570.
- Use the RMUTT PI catalog (PI1.1–PI11.2, 23 PIs; texts and levels from the OBE3-TABEE template, stored in `tools/obe3_clo_pi.json` `pi_catalog`). Don't use the WA-style numbering.
- **One CLO answers only one PI.**
- Minimum assessments per PI:
  - PO1–3: at least 2 direct + 1 indirect.
  - PO4–11: at least 1 direct + 2 indirect.
  - Count only courses every student takes.
- **Lecturers' OBE3 data takes precedence over Claude's draft rules** (the user asked to use the OBE3s).
- PO→PLO mapping is 1:1: PO1→PLO1, PO2→PLO4.1, PO3→PLO2, PO4→PLO4.2, PO5→PLO5, PO6→PLO8.1, PO7→PLO8.2, PO8→PLO3, PO9→PLO6, PO10→PLO8.3, PO11→PLO7.
- **Map CLOs only to sub-PLOs, never to parent PLO4 or PLO8** (the user's instruction). Keep the parent texts only in the Prospectus §3 breakdown table.
- Tables: the user prefers compact tables that fit one line per row.
- The user wanted Excel output modeled on IE's "CLO-PLO Matrix IE" workbook (photos in `source_documents/LINE/`, e.g. S__8339462–64).

### Environment notes
- **Thai PDF text:** use PyMuPDF, not `pdftotext`.
  - Some PDFs (the Manoch OBE3s) store tone marks as Private Use Area glyphs (U+F700–F71A). `tools/extract_obe3.py` maps them back (`THAI_PUA`).
  - Line breaks in PDFs insert spaces into Thai text, so compare text with `norm()` in the matrix script.
- **Legacy `.doc` files:** read them with `antiword -m UTF-8.txt`.
- **Python:** use `python -I`, and call `sys.stdout.reconfigure(encoding="utf-8")` before printing Thai.
- **DESKTOP-P9E7MNF:** has a git identity (thanasin), PyMuPDF 1.28, openpyxl 3.1.5, antiword, and Excel 16 through COM. Iterating over every cell through COM made Excel disconnect (`RPC_E_DISCONNECTED`). What works: open the workbook, `CalculateFull()`, `Save()` in Excel, then scan the cached values with openpyxl (`data_only=True`). `core.autocrlf=true` prints LF→CRLF warnings on every `git` command; they are harmless (the files are LF in the repo).
- **Excel on Hedwig:** Excel 16 is available through COM (PowerShell `New-Object -ComObject Excel.Application`). It was used to recalculate the workbook and scan for errors. LibreOffice is **not** installed, so the xlsx skill's `recalc.py` can't run.
- **Bash heredocs** with Thai and quotes broke once. Write scripts with the Write tool, and don't paste emoji like ⚠️ into Python `str.replace` from a heredoc (the variation selector didn't match).
- **Anchors:** CLO rows in course files start with `<a id="cloN"></a>`; PO rows in `CPE_RMUTT68_TABEE_PO_Mapping.md` have `<a id="poN"></a>`; PLO anchors (`#ploN`) are in the Prospectus.
- **Project skills** `/save-state` and `/recall-state` live in `.claude/skills/`.
- **Git (OneDrive folder):**
  - set `git config windows.appendAtomically false` (repo-local, already set in this clone);
  - Hedwig has no git identity, so commit with `git -c user.name=thanasin -c user.email=thanasin.b@gmail.com commit ...`;
  - pushes can take more than 2 minutes while OneDrive syncs.
- **Other PC only:** a memory-folder Read permission (`C:\Users\ADMIN\...`). Hedwig (user `tolbo`) has no project memory.

### Next steps
0. Resolve open decision 13 (the 18 CLOs mapped to more than one sub-PLO). This also affects coverage for PO4 and PO10.
1. Get the answer to open decision 0 (curriculum/cohorts for 2570). If (a), collect the previous CPE curriculum's course list and CLOs and build a second PO-PI-CLO matrix with the same tools.
2. Optionally add the ETAC weighted PI-attainment formula to `tools/build_po_pi_clo_xlsx.py` (open decision 11), and align the matrix with ETAC's "1 PI ↔ 1 SK" and lean-matrix rules.
3. Get answers to open decisions 1–2 (sync course files with OBE3s; Software Engineering code). If the user agrees, update the 6 course `.md` files and rebuild.
4. Review the matrix, workbook and §3.1 findings with the committee, and decide the gap fixes (open decisions 3–7).
5. As more OBE3s are collected, put them in `source_documents/` as `OBE 3_TABEE_<code>_<name>.pdf` and run the 3 tools in order.
6. Draft `CPE_RMUTT68_TABEE_PI_Reference.md`, update Prospectus §12, and continue the Electronics `.doc` write-up.

## History
### 2026-11-11 (DESKTOP-P9E7MNF)
- Recalled state with `/recall-state` (first session on this PC; it was already in sync with `origin/main`).
- At the user's request, split PLO4 (PO2 + PO4) and PLO8 (PO6 + PO7 + PO10) into sub-PLOs PLO4.1–4.2 and PLO8.1–8.3, one PO each.
  - The user chose to replace the parent PLOs with the sub-PLOs everywhere a CLO is mapped, and to keep the full breakdown in the PLO list (Prospectus §3).
  - The sub-PLO wording follows the RMUTT PI texts; PLO8.2 adds "ทั้งภาษาไทยและภาษาอังกฤษ" to cover PI7.2.
- The CLO→sub-PLO assignment came from the per-PO ticks already in each course's HTML PLO Mapping table (added in July, `fdbf80e`). The conversion covered all 295 CLOs with no inconsistencies.
- Rebuilt the PO-PI-CLO `.md` and `.xlsx`. Excel recalculated the workbook: 3,542 formulas, 0 errors.
- Found 18 CLOs that map to more than one sub-PLO, and that PO4 and PO10 have very few CLOs (open decision 13).
- Commit `1f294ad` (pushed).

### 2026-11-04 (Hedwig)
- Recalled state with `/recall-state`.
- Reviewed the TABEE documents in `source_documents/` COET folder from the program-committee perspective (criteria, assessment rules, capstone, Course Portfolio, site visit, IAB). Wrote `TABEE_COET_Documents_Notes.md` §1–10, including 12 gaps for CPE.
- Reviewed `source_documents/เอกสาร SER Writing/` (ETAC seminar deck by รศ.ดร.ณฐา + ETAC SER template). Added §11 (WA vs ETAC differences, 9 concrete ETAC rules, IE's use of 2563-curriculum data) and updated the §4 Criterion 5 row.
- Raised the curriculum-version problem (open decision 0).
- Extraction used PyMuPDF for PDFs and zipfile+regex for the `.docx`; extracted text lived only in the session scratchpad (not kept).

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
- Commits `28f1862` and `b88af03` (the latter records the git identity and OneDrive reflog workarounds).
- Added links with hover tooltips for every PLO, PO, PI, SK and CLO in the matrix (1,133 links, all checked):
  - added `<a id="cloN"></a>` anchors to 295 CLO rows in all 64 course files;
  - added `<a id="poN"></a>` anchors to `CPE_RMUTT68_TABEE_PO_Mapping.md`;
  - added the SK1–SK9 table as matrix §1.2.
- Moved the generator into the repo: `tools/build_po_pi_clo_matrix.py` and `tools/po_pi_clo_matrix_sections.md`. Its output is byte-identical to the committed matrix.
- Commit `6821103` (linked matrix and in-repo generator).
- Built the Excel workbook `CPE_RMUTT68_PO_PI_CLO_Matrix.xlsx` with `tools/build_po_pi_clo_xlsx.py`. It's formula-driven (CLO List → matrix and coverage) and was checked in Excel through COM.
- Reviewed IE's PO1 sheet (`source_documents/LINE/S__8339463_0.jpg` and `S__8339464_0.jpg`). Each PI has its direct courses plus Student Exit Survey and Co-op Employer Survey as indirect rows, with an attainment % column. Added PO1–PO11 sheets in the same layout.
- The user added 6 filled OBE3 PDFs to `source_documents/`. Added `tools/extract_obe3.py` → `tools/obe3_clo_pi.json` (PI catalog with levels, plus each course's CLO/PI/level/target/lecturer).
- The matrix now uses the OBE3 data for those courses, and the generated §3.1 compares each OBE3 with its course file (CLOs matched by text similarity). Updated §4.1, §4.3, §4.4 and §4.5 in `tools/po_pi_clo_matrix_sections.md` for the new coverage.

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
