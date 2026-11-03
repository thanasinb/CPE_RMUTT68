# TABEE (Sydney Accord) Curriculum Design — Source-Document Review

Status: review of `source_documents/` done 2026-11-03. No curriculum files changed yet. This file records what the training documents require when designing the CPE curriculum under TABEE's Sydney Accord (ETAC) track, and the gaps found against the current CPE RMUTT 2568 structure.

Text extraction note: the PDFs' Thai text is garbled with `pdftotext`; use PyMuPDF (`pymupdf`) instead. Some slides are images only (e.g. "SA Knowledge Profile" p40–41 in the SPP workshop deck, and "Sydney Accord (SA)" p21–25 in ศ.สมศักดิ์'s deck), but the same content is in text form in `4. TABEE Preparation RMUTT_NK.pdf` p10–16.

## 1. Which accord applies, and why it matters
- TABEE accredits under two tracks: **Washington Accord (EAC)** for professional-engineer programs and **Sydney Accord (ETAC)** for "practice-oriented engineering / engineering technology / industrial technology" programs. (NK deck p1, p8; ศ.สมศักดิ์ deck p2–4)
- RMUTT's own LO Writing Manual (`LO Writing Manual TABEE PO-PI-CLO ENG RMUTT.pdf`) and `OBE3_TABEE.doc` are built on the **Sydney Accord** (SK1–SK9). The CPE program's own TABEE slides (`TABEE Preparation_หลักสูตร คอมพิวเตอร์.pptx`) also use the SA wording of the PO meanings (e.g. "ปัญหาทางวิศวกรรมทั่วไป", SK refs).
- The CPE slides plan to **submit for TABEE accreditation in academic year 2570**.
- Note: the NK deck p51 lists Council-of-Engineers degree recognition for Sydney Accord as "to be confirmed". Worth checking whether SA accreditation affects graduates' กว. licensing.

## 2. Key WA vs SA differences (IEA GA 2021, NK deck p10–16)
| Item | Washington (WA/WK/WP) | Sydney (SA/SK/SP) |
|---|---|---|
| Problem level | Complex engineering problems | **Broadly-defined** engineering problems |
| Knowledge scope | "the discipline"; WK4 "much at the forefront" | "the **sub-discipline**"; SK4 has no forefront clause |
| SK2 math | supports detailed analysis and modelling | supports detailed consideration and **use of models** |
| SK8 | research literature + critical thinking + creativity | **technological literature** + critical thinking |
| SA1 | apply to complex problems | apply to "defined and applied engineering procedures, processes, systems, or methodologies" |
| SA3 | design creative solutions | design solutions and **contribute to** design of systems |
| SA5 | **create**, select, apply tools | select and apply tools (no "create") |
| SA10 | includes economic decision-making | no economic decision-making |
| SA11 | adds adaptability to emerging tech | independent learning + critical thinking about new specialist technologies |

Knowledge-profile → PO mapping (SA): PO1, PO2 → SK1–SK4; PO3 → SK5; PO4 → SK8; PO5 → SK2, SK6; PO6 → SK9; PO8 → SK1, SK5, SK7; PO9 → SK9; PO11 → SK8. (PO7 and PO10 have no SK reference.)

## 3. Broadly-defined problem definition (SP1–SP7) — governs capstone and PO2/PO3 courses
Source: ศ.สมศักดิ์ deck p66–67 (from IEA Table 4.1).
- **SP1 (mandatory):** cannot be solved without knowledge at SK4, SK5 and/or SK6, supported by SK3, with strong emphasis on **applying developed technology**.
- SP2: conflicting technical and non-technical issues (ethics, sustainability, law, economics, society), plus consideration of future requirements.
- SP3: solvable with well-proven analysis techniques and models.
- SP4: belongs to families of familiar problems solved in well-accepted ways.
- SP5: may be partly outside standards and codes of practice.
- SP6: multiple disciplines and stakeholder groups with differing needs.
- SP7: components of systems within complex problems.
- For *complex* problems, TABEE requires at least 4 characteristics (WP1 + 3 others) (SER manual p73, p199). No equivalent SA threshold was stated explicitly. **Assume the same "SP1 + at least 3" rule** to be safe until confirmed.

## 4. Criterion 5 (curriculum) requirements
- **Duration:** SA programs must be ≤ 5 academic years. **No minimum credits required for mathematics and basic science** (WA requires them). (ศ.สมศักดิ์ deck p115)
- SER manual p188 lists ≥ 30 credits math/science, ≥ 45 credits engineering, and ≥ 24 credits GE (per สป.อว.). These read as the WA/general rule; under SA the math/science minimum does not apply. CPE already meets the engineering and GE minimums: 111 major credits and 24 GE.
- The SER must show the study plan with prerequisite chains aligned to outcomes (Table 5.2), plus coverage of each knowledge area.
- Must show courses that address the problem level. **At least 2 courses in the curriculum must involve solving the target-level problems.** PO2 and PO3 each need **≥ 2 direct assessments from such courses**.

## 5. Criterion 3/4 assessment rules (affect course selection in curriculum design)
- Every one of the 11 POs must have PIs, and each PI must be assigned to courses/CLOs for assessment.
- **PO1–PO3:** min **2 direct + 1 indirect** per PI. **PO4–PO11:** min **1 direct + 2 indirect** (or 2 direct + 1 indirect). Each PO has ≥ 3 assessments in total. (ศ.สมศักดิ์ deck p80; SER manual p117)
- Need ≥ 2 consecutive academic years of PO assessment results before submission, which means data collection must start by **2568–2569** to submit in 2570.
- Indirect-assessment questionnaires must target each PO, not general satisfaction.

## 6. Capstone Design Project requirements
Sources: ศ.สมศักดิ์ deck p118–122, SER manual p200–204, Capstone deck (อ.จิรวัฒน์).
- Should be in **year 4** and integrate years 1–3.
- **Two courses in consecutive semesters** (so there are 2 direct assessments).
- **Teams of 3–5** students, so teamwork and communication can be assessed.
- Real professional or industry problems; **avoid research-style projects**; require **≥ 2 engineering sub-areas**; include soft-skill, environmental and sustainability content.
- Topic screening process: each project must be shown, in a checklist table, to meet the problem-characteristic criteria.
- Assessed by a **committee of ≥ 2**, not only the advisor; include an industry assessor when the topic comes from industry.
- Keep evidence for **every** project, not samples. Report individual student performance.
- Capstone must assess at least **PO2, PO3, PO4, PO6, PO7, PO8**; it may also cover PO5, PO9, PO10 and PO11.

## 7. Gaps found in the current CPE RMUTT 2568 structure
1. **Capstone placement and sequence.** Current capstone pair: `04-620-303` Pre-Project **1(0-3)** in Y3/S2 → `04-620-401` Project **3(1-6)** in Y4/S2, with **Y4/S1 = Cooperative Education 6(0-40)**. Problems:
   - The two courses are not consecutive semesters; co-op sits between them.
   - Pre-Project is in year 3, not year 4.
   - Pre-Project is only 1 credit, which is thin for a full direct assessment of PO2/PO3.
   Options: justify the co-op gap in the SER; move or strengthen Pre-Project; or count `04-000-402 Industry Special Problem` / co-op as part of the capstone evidence.
2. **Team size.** Need to confirm that Project groups are 3–5 students. Pairs or individual projects would fail the PO6/PO7 assessment design.
3. **Second "problem-level" course.** TABEE wants ≥ 2 courses at broadly-defined level for PO2/PO3 direct assessment. Candidates: `04-620-302` Computer System Integration Laboratory, `04-622-302` Software Engineering, `04-621-302` IoT.
4. **Sample capstone topics** in the CPE slides (rice-paddy water-level control with GHG reduction; flood-level alert for communities) fit SP1, SP2 and SP6 well. Write them up with an SP checklist table as the model.
5. **Prospectus §12** describes TABEE only generically ("Student Outcomes …"). It should state the **Sydney Accord / ETAC** track and list the 11 TABEE POs.
6. **PO7 and PO10 have no SK anchor.** That's fine per SA, but their PIs still need a direct-assessment course each.

## 8. Relationship to other notes
- `TABEE_PI_Analysis_Notes.md`: CPE-specific rewording of SK1/SK5/SK7 and the PI10.1 reclassification. The SA definitions above confirm SK-based wording is the right base.
- PI numbering differs between sources: ศ.สมศักดิ์ uses WA-style examples (`PI 2.4.1` … with TK), while the RMUTT LO manual uses PI1.1–PI11.2 with SK. **Follow the RMUTT manual.**

## Next steps (not started)
1. Decide how to fix or justify the capstone sequence (gap 1).
2. Choose the second broadly-defined-problem course and the 2-direct-assessment courses for every PO1–PO3 PI.
3. Build a PI → course → CLO assessment plan table (direct/indirect counts per PI).
4. Update Prospectus §12 with the Sydney Accord track.
5. Confirm with the faculty or TABEE whether broadly-defined problems also require ≥ 4 SP characteristics.
