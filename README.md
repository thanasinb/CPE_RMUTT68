# CPE RMUTT 2568 — Curriculum Documentation & TABEE Direct Assessment

หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมคอมพิวเตอร์ (ปรับปรุง พ.ศ. 2568)  
คณะวิศวกรรมศาสตร์ มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี

---

## วัตถุประสงค์ | Objectives

1. **สำหรับนักศึกษาที่สนใจ** — ข้อมูลหลักสูตรที่เพียงพอสำหรับการตัดสินใจสมัครเรียน
2. **สำหรับอาจารย์และกระบวนการ TABEE** — เอกสารรายวิชา CLOs และการแมป PLO สำหรับการรับรองหลักสูตร

---

## โครงสร้างไฟล์ | Repository Structure

```
├── CPE_RMUTT68_Prospectus.md        # ข้อมูลหลักสูตรสำหรับนักศึกษา (student-facing)
├── CPE_RMUTT68_PLO_CLO_Matrix.md   # ตารางแมป PLO–CLO ทุกรายวิชา
│
├── courses/
│   ├── foundation/                  # กลุ่มวิชาพื้นฐาน (11 วิชา)
│   ├── core/                        # กลุ่มวิชาบังคับ (14 วิชา)
│   ├── electives/
│   │   ├── hardware/                # กลุ่มฮาร์ดแวร์และสถาปัตยกรรม (10 วิชา)
│   │   ├── software/                # กลุ่มซอฟต์แวร์ (9 วิชา)
│   │   ├── network/                 # กลุ่มระบบเครือข่าย (6 วิชา)
│   │   └── ai/                      # กลุ่มปัญญาประดิษฐ์ (8 วิชา)
│   └── cwie/                        # กลุ่มเสริมสร้างประสบการณ์วิชาชีพ (6 วิชา)
│
├── TABEE/                           # ระบบ TABEE Direct Assessment (อยู่ระหว่างพัฒนา)
│
├── assets/                          # รูปภาพและสื่อประกอบ
└── source_documents/                # เอกสารต้นฉบับ (CPE-222.docx, CLO_v6.docx, ฯลฯ)
```

---

## รูปแบบไฟล์รายวิชา | Course File Format

แต่ละรายวิชามี YAML frontmatter สำหรับการประมวลผลอัตโนมัติ:

```yaml
---
code: 04-620-201
name_th: ปฏิบัติการควบคุมเวอร์ชัน
name_en: Version Control Laboratory
credits: 1(0-3)
type: กลุ่มวิชาพื้นฐาน
year: 2
semester: 1
plos: PLO2, PLO4, PLO5, PLO8
---
```

และมีเนื้อหา:
- คำอธิบายรายวิชา (ไทย/อังกฤษ)
- ตาราง CLOs พร้อม PLO mapping
- แผนการประเมิน

---

## มาตรฐานที่เกี่ยวข้อง | Standards

| มาตรฐาน | รายละเอียด |
| --- | --- |
| **TABEE** | Thailand Accreditation Board for Engineering Education |
| **TQF** | กรอบมาตรฐานคุณวุฒิระดับอุดมศึกษา พ.ศ. 2565 |
| **AUN-QA** | ASEAN University Network Quality Assurance |
| **CWIE** | สหกิจศึกษาและการศึกษาเชิงบูรณาการกับการทำงาน ระดับ 1 |

---

## แผนการพัฒนา | Roadmap

- [x] **Level A** — เอกสารรายวิชา (CLOs, PLO mapping, แผนการประเมิน)
- [ ] **Level B** — Spreadsheet สำหรับบันทึกคะแนนและคำนวณ CLO attainment
- [ ] **Level C** — ระบบ Claude-assisted สำหรับรายงาน TABEE อัตโนมัติ

---

## ผู้รับผิดชอบ | Maintainer

ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์  
มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี
