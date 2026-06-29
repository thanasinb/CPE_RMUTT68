# TABEE Direct Assessment — CPE RMUTT 2568

โฟลเดอร์นี้สำหรับระบบ TABEE Direct Assessment (Level C — อนาคต)

## โครงสร้างที่วางแผนไว้

\\\
TABEE/
├── assessment_records/     ← คะแนนนักศึกษารายวิชา รายปีการศึกษา
├── attainment_reports/     ← รายงานผล CLO/PLO attainment รายปี
└── improvement_plans/      ← แผนปรับปรุงจากผลการประเมิน
\\\

## กระบวนการ TABEE Direct Assessment

1. อาจารย์ผู้สอนบันทึกคะแนนแต่ละ CLO ลงใน assessment_records/
2. ระบบคำนวณ CLO attainment ต่อ PLO
3. สร้างรายงาน attainment_reports/ อัตโนมัติ
4. บันทึกแผนปรับปรุงใน improvement_plans/

*(ระบบนี้อยู่ระหว่างการพัฒนา — ปัจจุบันอยู่ที่ Level A)*
