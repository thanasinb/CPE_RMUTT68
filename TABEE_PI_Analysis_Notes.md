# TABEE PI Fit Analysis — Working Notes

Status: analysis in progress, no files changed yet. Next step is to draft a CPE-adapted PI reference doc (not started).

## Question being investigated
Does the official RMUTT Performance Indicator (PI) catalog fit the Computer Engineering curriculum as-is, or does it need modification?

## Sources compared
- `source_documents/LO Writing Manual TABEE PO-PI-CLO ENG RMUTT.pdf` — Faculty-of-Engineering-wide PI guide with SK1–SK9 explanations, bracketed `[...]` placeholders for CLO writing, Bloom's action-verb lists.
- `source_documents/OBE3_TABEE.doc` — the blank syllabus template. Extracted its raw text with `antiword` (it's a legacy binary .doc; Read tool can't open it directly, antiword or LibreOffice can).
- `source_documents/OBE3_TABEE_example.pdf` — a filled-in example (Industrial Engineering, "Production Planning and Control" course).

**Key finding:** `OBE3_TABEE.doc`'s built-in PI table (section 3.2) is **word-for-word identical** to the LO Writing Manual's PI catalog — same 23 PI codes (PI1.1–PI11.2), same canonical Thai text. It's not a separate list; every department gets the same catalog and just checks ✓ which PIs their course addresses, then writes their own CLO in section 4. So all findings below apply to both documents.

## Overall verdict
The SK/PI skeleton (23 PIs across 11 TABEE POs) and the Bloom's K/S/A action-verb lists are discipline-agnostic and transfer to CPE cleanly. Two spots have wording clearly written from a civil/industrial-engineering vantage point and need CPE-specific rewording. One classification looks miscategorized. One is a plain template bug.

## Findings so far

### 1. SK1 natural-science bracket (affects PO1, PO2) — needs narrowing
Current bracket: `[ฟิสิกส์/กลศาสตร์/เคมี/โลกศาสตร์/ชีววิทยา]`. CPE foundation courses (Electrical Circuits, Electronics Circuits) only ever draw on ฟิสิกส์ (physics — electricity/electronics). Recommend narrowing to `[ฟิสิกส์ (ไฟฟ้า/อิเล็กทรอนิกส์/สนามแม่เหล็กไฟฟ้า)]` so CLOs don't reference sciences the program doesn't teach.

### 2. SK5 (PO3) and SK5/SK7 (PO8) sustainability language — needs CPE-specific rewording
Current wording is framed around physical/civil-engineering design criteria: ต้นทุนตลอดอายุการใช้งาน, Net Zero Carbon, ทรัพยากรกายภาพ. For CPE (software/systems/AI/embedded), the criteria that actually apply are: **cybersecurity, data privacy (PDPA), AI/algorithmic ethics & bias, digital accessibility/divide, energy efficiency of computing (data centers/AI training), e-waste from hardware, software reliability/maintainability**. None of these appear in the current wording.

### 3. PO9 professional ethics — optional addition
Generic engineer's code of ethics applies fine, but could explicitly cite CPE-specific legal frameworks: พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) and พ.ร.บ. คอมพิวเตอร์ (Computer-Related Crime Act), since these are the laws CPE graduates most likely encounter in practice.

### 4. Template bug: PI11.2 mislabeled "PO12"
Confirmed in the raw `OBE3_TABEE.doc` text (not just the filled example) — the last PI row is labeled `PO12` when TABEE only defines 11 POs. PI11.2 belongs under PO11 alongside PI11.1. This is a university-template-level bug, not CPE-specific, but must not be copied forward into the CPE reference doc.

### 5. PI 10.1 domain/level — likely misclassified
Text: "ใช้หลักการบริหารจัดการทางวิศวกรรม เพื่อบริหารโครงการวิศวกรรมที่มีสภาพแวดล้อมแบบพหุสาขาวิชา" — currently tagged **(K3-Apply)**.

- **Not Affective** — no value/attitude/ethics component (unlike PO8's "ให้ความเห็น" (A4) or PO9's "สร้างค่านิยม" (A3)).
- **Not really Cognitive K3** — K3 fits rote/formulaic technique application (e.g. "manage the project using CPM/PERT," which the official worked example actually scoped its CLO down to — that's why K3 worked there). But the PI's own wording ("บริหารโครงการ...พหุสาขาวิชา") describes a broader, sustained performed competency, not a single calculation.
- **Best fit: Psychomotor (P)** — consistent with how the *same document* classified other practiced/soft competencies: PO6 teamwork (PI6.1) → S3-Precision, PO7 communication (PI7.1/7.2) → S3-Precision. Project management belongs in the same bucket. Specifically **S3-Precision** (if scoped to running one defined PM process correctly) or **S4-Articulation** (if it's about coordinating multiple disciplines/workstreams in harmony — the "พหุสาขาวิชา" wording leans this way).

**Decision:** reclassify PI10.1 from (K3-Apply) to (S3 or S4 — Precision/Articulation) in the CPE-adapted reference.

## Next step (not yet started)
Draft a CPE-adapted PI reference document (proposed filename: `CPE_RMUTT68_TABEE_PI_Reference.md`) containing all 23 PI rows, with:
- Corrected PO11 labeling (fix the PO12 bug)
- CPE-specific SK1 bracket (physics-focused)
- CPE-specific SK5/SK7 wording (cybersecurity, data privacy, AI ethics, accessibility, energy efficiency, e-waste, reliability)
- PO9 optionally citing PDPA / Computer-Related Crime Act
- PI10.1 reclassified to Psychomotor S3/S4

No repo files have been edited as part of this analysis — this notes file is the only new file. To resume, just tell the new session to read this file.
