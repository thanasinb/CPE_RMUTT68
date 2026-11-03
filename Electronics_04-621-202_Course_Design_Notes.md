# 04-621-202 Electronics Circuits for Computer Engineering — Working Notes

Status: analysis + course design in progress, in-repo `.md` files not yet touched for this course. Nothing written into the actual `.doc` yet — everything below is a recommendation pending your go-ahead.

Source file under review: `source_documents/OBE 3_TABEE_04-621-202_Electronics_Thanasin Bunnam.doc` (real, in-progress OBE3-TABEE syllabus for this course, git-ignored — not version controlled, so edits to it are not recoverable via git).

Reference materials checked: `source_documents/Electronics/` (Lectures/Labs/Books) — contains prior teaching material mixing the basic Electrical Circuits course (Ohm's law, Kirchhoff, Thevenin, RC/AC — chap00-09) and this Electronics course's actual scope (Diode, BJT, Op-amp — chap16-18, LAB6-9). No MOS/CMOS material exists yet.

## 1. Document completion status (as of this review)
- Sections 1–3 (general info, PLO↔PO↔PI mapping, PI↔CLO table) substantially filled.
- Only CLO1 and CLO2 are actually drafted; CLO3–CLO7 in the doc were placeholder dots, now analyzed below.
- Section 4 (weekly teaching plan, assessment %, rubric) still blank template rows — this is what the "10-week course design" below is meant to fill.
- Section 5 (textbooks/resources) still blank.

## 2. Structural bugs / discrepancies found (carried from `TABEE_PI_Analysis_Notes.md`)
- **PO12 bug**: PI11.2 is mislabeled "PO12" in both the master template (`OBE3_TABEE.doc`) and this course file — TABEE only defines 11 POs. Confirmed present, unfixed, in this real course document too.
- **PI10.1 domain discrepancy**: master template tags PI10.1 as `(K3-Apply)`; this course file already independently uses `(A4-Organizing & Conceptualizing)` instead — neither matches the notes' proposed fix (S3/S4-Psychomotor). Unresolved judgment call.
- PO3 (PI3.1, sustainability/design), PO4, PO8, PO10, PO11 are checked as relevant in Section 2 but **no CLO addresses them** — either those POs shouldn't be checked for this course, or more CLOs are needed. Not yet resolved.

## 3. CLO K/S/A domain/level analysis (verified against the doc's own Bloom's action-verb table)

| CLO | Text (gloss) | Current draft tag | Correct tag | Recommended PI |
|---|---|---|---|---|
| CLO1 | Explain semiconductor properties/device principles | K2 | **K2-Understanding ✓ correct** | PI1.1 (SK1, natural science) — already assigned, correct |
| CLO2 | Explain semiconductor circuit principles | K2 | **K2-Understanding ✓ correct** | **PI1.3** (SK3, engineering fundamentals) — recommend changing from PI1.1 |
| CLO3 | Apply/use semiconductor devices | K6 (wrong) | **K3-Applying** | **PI1.4** (SK4) — PI column currently blank |
| CLO4 | Analyze electronic circuits | K5 (wrong) | **K4-Analyzing** | **PI2.4** (SK4) — PI column currently blank |
| CLO5 | Use tools/software correctly and safely | S3 | **S3-Precision ✓ correct** | **PI5.2** — near-verbatim match |
| CLO6 | Honesty, ethics, discipline, punctuality | A3 | **A3-Valuing ✓ defensible** | **PI9.1** — near-verbatim match |
| CLO7 | Teamwork + communicate/express opinions | A4 | defensible but **structurally conflicts** — spans 3 PIs (PI6.1 teamwork, PI7.1 Thai comm, PI7.2 English comm, all S3-Precision at PI level) | **Needs splitting** — doc's own rule says one CLO can't answer >1 PI |

Two clear numeric errors to fix: **CLO3 (K6→K3)** and **CLO4 (K5→K4)** — verbs literally listed under K3/K4 in the doc's own reference table, current tags look like copy-paste leftovers.

Recommended CLO7 split:
- CLO7a: "ทำงานร่วมกับผู้อื่นที่มีความหลากหลายได้อย่างมีประสิทธิภาพ" → PI6.1, S3-Precision
- CLO7b: "สื่อสารภาษาไทย/อังกฤษได้อย่างมีประสิทธิภาพ" → PI7.1 and/or PI7.2, S3-Precision

Note: within PO3, **PI3.1 is the only indicator** (no PI3.x family) — confirmed no PI3.2 exists in either this file or the master template. PI3.1 (K6-Create, sustainability/design-tradeoffs) does not fit CLO3 at all; PI1.4 remains the right match.

## 4. Section "1. แนวคิดการจัดการเรียนรู้ Concept of Learning Management" — recommended checkboxes
Teaching format confirmed: 2 hr lecture + 3 hr practice/labsheet, done in **pairs**, with **hands-on equipment**.

Recommend checking:
1. **การเรียนโดยใช้ปัญหาเป็นฐาน (Problem-based Learning)** — labsheets are circuit-analysis/design problems
2. **การเรียนผ่านประสบการณ์ (Experiential Learning)** — hands-on equipment work
3. **การเรียนรู้ร่วมกัน (Collaborative Learning)** — paired work without formal role division (use "Cooperative Learning" instead only if roles get formally split, e.g. one operates equipment while the other records)

Not yet written into the `.doc` — user has not confirmed go-ahead, and the file is git-ignored/unversioned so a backup should be made first if edited.

## 5. 10-week course design (final revised version, pending write-up into Section 4.2)

**Objective driving this design**: prepare students to design their own microcontroller dev board (Arduino-like) or interfacing circuits (e.g. controllable voltage divider for battery measurement) for the year-4 capstone project. User's own expertise is VLSI — wanted a CMOS chapter added (reframed as practical GPIO/logic-level interfacing rather than abstract VLSI-flow content, to keep it both relevant to the objective and true to the user's specialty).

Format: 2 hr lecture + 3 hr practice/week, 10 teaching weeks, 10 chapters, pairs, hands-on.

| Week | Chapter Title (TH / EN) | Lecture (2 hr) | Practice (3 hr, pair work) | CLOs |
|---|---|---|---|---|
| 1 | เครื่องมือวัดทางอิเล็กทรอนิกส์ / Electronic Instruments & Measurement | Multimeter, power supply, oscilloscope, safety | Equipment familiarization | CLO5, 6, 7 |
| 2 | หลักการสารกึ่งตัวนำ / Semiconductor Materials & PN Junction | PN junction theory | Basic PN junction I-V measurement | CLO1 |
| 3 | ไดโอดและวงจรป้องกัน / Diode Characteristics & Protection Circuits | Diode models, rectification, reverse-polarity/flyback protection | Build a battery reverse-polarity protection circuit | CLO1,2,3 |
| 4 | แหล่งจ่ายกำลังสำหรับบอร์ดไมโครคอนโทรลเลอร์ / Power Supply Design for MCU Boards | Battery input, linear regulator IC (e.g. AMS1117/7805) | Build a regulated 5V/3.3V rail from a battery | CLO3,4,5 |
| 5 | ทรานซิสเตอร์บีเจทีและการขับโหลด / BJT: Biasing & Load-Switching | BJT biasing, BJT as a switch | Drive an LED/relay from a low-power control signal | CLO1,2,3,4 |
| 6 | มอสเฟตและวงจรแบ่งแรงดันแบบควบคุมได้ / MOSFET Power Switching & Controllable Voltage Divider | MOSFET as a power switch | Build the switched voltage-divider battery-measurement circuit (user's exact stated example) | CLO1,2,3,4 |
| 7 | ซีมอสและการเชื่อมต่อสัญญาณดิจิทัล / CMOS & Digital I/O Interfacing | GPIO logic levels, drive current, pull-up/down, 3.3V/5V level shifting | Test GPIO drive limits, build a simple level-shifter | CLO1,2,3,4,5 |
| 8 | วงจรขยายปฏิบัติการสำหรับสัญญาณเซนเซอร์ / Op-amp Signal Conditioning (+ brief current mirror) | Op-amp buffer/amplifier for sensor signals; current mirror mentioned briefly as a constant-current bias concept | Build an op-amp buffer/amp stage feeding an ADC input | CLO2,3,4 |
| 9 | วงจรกำเนิดสัญญาณนาฬิกาสำหรับไมโครคอนโทรลเลอร์ / Oscillator Circuits for MCU Clocking | Crystal oscillator basics | Build/verify a crystal oscillator circuit | CLO3,4 |
| 10 | การออกแบบแผงวงจรและการบูรณาการ / PCB Design, Connectors & Board Integration (capstone) | PCB layout basics, header/connector selection | Pair capstone: design + lay out a small interfacing board using this semester's circuits | CLO3,4,6,7 |

Design rationale (for continuity):
- Original plan (before this revision) taught BJT/MOS as classic analog amplifier design (CE/CC/CB small-signal analysis) and a standalone current-mirror week, plus a CMOS week framed around VLSI design-flow + logic gates. That was flagged as (a) not well aligned to the dev-board/interfacing objective and (b) too dense pacing-wise (4 back-to-back new-transistor-family weeks with no breathing room, several weeks packing 3 sub-topics into one 5-hr slot).
- Revision fixes both: reframes BJT/MOS around switching/driving loads (simpler than full amplifier analysis, and the actually-needed skill for interfacing), merges current mirror into the op-amp week as a brief mention instead of a dedicated week, reframes CMOS around practical GPIO electrical characteristics instead of abstract VLSI flow, and turns Week 10 into a synthesis capstone rather than 3 new topics + a project.
- Course-description coverage check: equipment✓(1), semiconductor✓(2), diode✓(3), BJT✓(5), MOS✓(6), CMOS added✓(7, new), op-amp✓(8), current mirror✓(8, merged), power supply✓(4), oscillator✓(9), sockets/connectors✓(10), PCB design✓(10). All CLOs (1–7) covered across the plan.

## Next steps (not started)
1. Decide whether to write the CLO K/S/A + PI corrections (Section 3 above) into the actual `.doc`.
2. Decide whether to check the 3 Learning Management boxes (Section 4 above) into the actual `.doc`.
3. Decide whether to write the 10-week plan (Section 5) into Section 4.2 of the `.doc`, or draft it into a `courses/foundation/04_621_202_Electronics_Circuits_for_Computer_Engineering.md` file first for review.
4. Resolve the CLO7 split (two CLOs replacing one) — affects total CLO count and the CLO/PLO/PI tables throughout Section 3–4 of the doc.
5. Resolve the PI10.1 domain discrepancy (K3-Apply vs A4-Organizing) — affects the CPE-wide PI reference doc mentioned in `TABEE_PI_Analysis_Notes.md`, not just this course.
6. Decide whether to write the bibliography (Section 6 below) into Section 5 (textbooks/resources) of the `.doc`, and in which citation style (APA drafted below; IEEE numbered also common for TABEE docs).
7. Note: `source_documents/` is git-ignored — any edit to the `.doc` itself has no git history; back up before editing.

## 6. Textbook/resource analysis (`source_documents/Electronics/Books/`, 16 PDFs)

Verified against actual PDF title/copyright pages (not just filenames) via `pdftotext`. One filename-driven mistake caught and corrected during this: `electronic-devices-by-floyd-8th-edition.pdf` and `electronic-devices-by-floyd-9th-edition.pdf` are **not** two editions of the same book — the "8th edition" file is actually *Electronics Fundamentals: Circuits, Devices, and Applications* by Floyd & Buchla (a broader combined basic-circuits+devices text), while the "9th edition" file is Floyd's solo *Electronic Devices* (device-focused, matches this course better).

**Main textbook recommendation:** Floyd, T. L. (2012). *Electronic devices* (9th ed., Electron flow version). Prentice Hall. — matches the course's diode/BJT/MOSFET/op-amp device-level scope and CLO1/CLO2 (K2-Understanding) level, technology-program style fits the 2hr lecture + 3hr hands-on practice format better than a pure analytical EE text.

**Supplementary — practical/hands-on (recommended, aligned with dev-board/interfacing objective):**
- Scherz, P., & Monk, S. (2016). *Practical electronics for inventors* (4th ed.). McGraw-Hill Education.
- Horowitz, P., & Hill, W. (2015). *The art of electronics* (3rd ed.). Cambridge University Press.
- Platt, C. (2009). *Make: Electronics* (1st ed.). O'Reilly Media.
- Platt, C. (2014). *Make: More electronics*. O'Reilly Media.
- Cathey, J. J. (2002). *Schaum's outline of theory and problems of electronic devices and circuits* (2nd ed.). McGraw-Hill.

**Reference — advanced/instructor background only (not student-assigned, doesn't match the practical/interfacing scope):**
- Sedra, A. S., Smith, K. C., Chan Carusone, T., & Gaudet, V. (2020). *Microelectronic circuits* (8th ed.). Oxford University Press. (epub + solutions-manual PDFs in the folder are companions to this, not separate citations)
- Weste, N. H. E., & Harris, D. (2011). *CMOS VLSI design: A circuits and systems perspective* (4th ed.). Addison-Wesley/Pearson. (relevant only if Week 7's CMOS content goes deeper than the planned practical-GPIO reframe — user's own VLSI-background reference)
- Razavi, B. (2017). *Design of analog CMOS integrated circuits* (2nd ed.). McGraw-Hill Education. (same caveat as above)
- Floyd, T. L., & Buchla, D. L. (2014). *Electronics fundamentals: Circuits, devices, and applications* (8th ed.). Pearson Education.

**Not a good fit — basic circuit theory, belongs to the prerequisite course, not this one (matches `Lectures/elec-chap00-09`, not `chap16-18`):**
- Alexander, C. K., & Sadiku, M. N. O. (2017). *Fundamentals of electric circuits* (6th ed.). McGraw-Hill Education.
- Dorf, R. C., & Svoboda, J. A. (2014). *Introduction to electric circuits* (9th ed.). John Wiley & Sons.
- Nahvi, M., & Edminister, J. A. (2018). *Schaum's outline of electric circuits* (7th ed.). McGraw-Hill Education.
- If cited at all, list under a "prerequisite knowledge" note rather than this course's Section 5 textbook list.

To resume, tell the new session to read this file (and `TABEE_PI_Analysis_Notes.md` for the broader PI-catalog-fit analysis this course work builds on).
