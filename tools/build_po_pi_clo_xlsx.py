"""Build CPE_RMUTT68_PO_PI_CLO_Matrix.xlsx (formula-driven) from the same data as the .md matrix.

Usage:  python -I tools/build_po_pi_clo_xlsx.py

Reuses tools/build_po_pi_clo_matrix.py (runs it, which also regenerates the .md) for the parsed
courses, OBE3 overrides, PI assignments, flags and descriptions.
Sheets: README · PO-PI-CLO Matrix · PO1..PO11 (assessment plan per PO, IE layout) · CLO List · PI Catalog · SK
- "CLO List" is the editable source: PI, ⚑ note, CLO level, target %. The matrix and coverage rows are formulas over it.
- PO sheets are laid out at build time from the CLO List defaults; their CLO level / target / alignment cells
  look the CLO up in "CLO List" by course|CLO|PI, so a later PI change shows up as a warning on that row.
Only Excel-2007-era functions are used (LOOKUP / INDEX / MATCH / COUNTIF(S) / AVERAGEIFS / IFERROR).
"""
import os, re, runpy
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter as CL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = runpy.run_path(os.path.join(ROOT, 'tools', 'build_po_pi_clo_matrix.py'))
os.chdir(ROOT)
C, PIS, PI_DESC, SK, PO_TXT, PLO_TXT, PO_PLO, FLAG, grp, OBE3 = (G[k] for k in
    ('C', 'PIS', 'PI_DESC', 'SK', 'PO_TXT', 'PLO_TXT', 'PO_PLO', 'FLAG', 'grp', 'OBE3'))
PI_CAT = OBE3['pi_catalog']                        # full PI text + level (from the OBE3-TABEE template)
OUT = 'CPE_RMUTT68_PO_PI_CLO_Matrix.xlsx'
# TABEE PO meanings (Sydney Accord wording), from "TABEE Preparation_หลักสูตร คอมพิวเตอร์.pptx" (workshop 21 เม.ย. 69)
PO_FULL = {
 1: 'ความรู้ทางด้านวิศวกรรม และพื้นฐานทางคณิตศาสตร์ และวิทยาศาสตร์: สามารถประยุกต์ความรู้ทางด้านคณิตศาสตร์ วิทยาศาสตร์ พื้นฐานทางด้านวิศวกรรม และความรู้เฉพาะทางวิศวกรรม เพื่อนิยามและใช้ ขั้นตอนวิธี กระบวนการ ระบบงานหรือวิธีการทางวิศวกรรม (ตามแบบความรู้ SK1-SK4)',
 2: 'การวิเคราะห์ปัญหาทางวิศวกรรม: สามารถระบุ ตั้งสมการ วิจัย สืบค้น และวิเคราะห์ปัญหาทางวิศวกรรมทั่วไป เพื่อให้ได้ข้อสรุปของปัญหาที่มีนัยสำคัญ โดยใช้หลักการทางวิศวกรรม เครื่องมือวิเคราะห์และอุปกรณ์ อย่างเหมาะสมตามสาขาและ/หรือแขนงของความชำนาญ (ตามแบบความรู้ SK1-SK4)',
 3: 'การออกแบบและพัฒนาเพื่อหาคำตอบของปัญหา: สามารถพัฒนาหาคำตอบของปัญหาในการปฏิบัติวิชาชีพวิศวกรรม หรือปัญหาทางเทคโนโลยีวิศวกรรมทั่วไป และมีส่วนช่วยออกแบบระบบ ชิ้นงาน หรือกระบวนการ ตามความจำเป็นและเหมาะสม โดยคำนึงถึงข้อกำหนดด้านสังคม วัฒนธรรม ความปลอดภัย การอนามัยและสิ่งแวดล้อม มาตรฐานการปฏิบัติวิชาชีพ และการพัฒนาที่ยั่งยืน อาทิ มูลค่าตลอดวัฏจักรชีวิต การปลดปล่อยคาร์บอนสุทธิเป็นศูนย์ และประเด็นทางสิ่งแวดล้อมต่าง ๆ ที่เกี่ยวข้อง (ตามแบบความรู้ SK5)',
 4: 'การพิจารณาตรวจสอบ: สามารถตรวจสอบ วินิจฉัย ประเมินผล งานและปัญหาทางวิศวกรรมทั่วไป ซึ่งครอบคลุมถึงการตั้งสมมติฐาน การหาข้อมูล การทดลอง การวิเคราะห์ การแปลความหมายข้อมูล สังเคราะห์ข้อมูล ข้อสนเทศ และออกแบบ เพื่อให้ได้ผลสรุปที่ถูกต้องตามหลักเหตุผล (ตามแบบความรู้ SK8)',
 5: 'การใช้เครื่องมือทันสมัย: สามารถเลือก และประยุกต์ใช้เทคนิควิธี ทรัพยากร อุปกรณ์เครื่องมือทางวิศวกรรมและเทคโนโลยีสารสนเทศที่เหมาะสมและทันสมัย ในการทำงานและแก้ไขปัญหาทางวิศวกรรมทั่วไป รวมถึงการทำการทดลอง การจำลองแบบ และการพยากรณ์ผลการแก้ไขปัญหาทางวิศวกรรม โดยคำนึงถึงข้อกำหนดและข้อจำกัดของเครื่องมือและอุปกรณ์เหล่านั้น (ตามแบบความรู้ SK2 และ SK6)',
 6: 'การทำงานร่วมกันเป็นทีม: สามารถทำงานร่วมกับผู้อื่นที่มีความหลากหลายในสหสาขาวิชาได้อย่างมีประสิทธิภาพ สามารถทำงานในฐานะสมาชิกของกลุ่มและผู้นำกลุ่มในรูปแบบต่าง ๆ ได้ (ตามแบบความรู้ SK9)',
 7: 'การติดต่อสื่อสาร: สามารถติดต่อสื่อสารเป็นภาษาไทยและภาษาอังกฤษในงานวิศวกรรม วิชาชีพอื่น และบุคคลทั่วไปได้อย่างมีประสิทธิผลทั้งด้วยวาจา ด้วยการเขียนรายงาน การเสนอผลงาน การเขียนและอ่านแบบทางวิศวกรรม ตลอดจนสามารถออกคำสั่งและรับคำสั่งงานได้อย่างชัดเจน',
 8: 'ความรับผิดชอบของวิศวกรต่อโลก: มีความเข้าใจและความรับผิดชอบต่อการปฏิบัติวิชาชีพวิศวกรรมทั่วไป รวมถึงและการใช้เทคโนโลยีทางวิศวกรรม ในบริบทของสังคม เศรษฐกิจ สิ่งแวดล้อม การพัฒนาที่ยั่งยืน และกรอบของกฎหมาย รวมทั้งสามารถประเมินผลกระทบของการแก้ไขปัญหาทางวิศวกรรมทั่วไป ที่มีต่อสังคม สิ่งแวดล้อม และการพัฒนาที่ยั่งยืนด้วย (ตามแบบความรู้ SK1, SK5, SK7)',
 9: 'จรรยาบรรณวิชาชีพ: มีความเข้าใจและยึดมั่นในจรรยาบรรณแห่งวิชาชีพ และยึดถือตามกรอบมาตรฐานการปฏิบัติวิชาชีพ ที่สอดคล้องกับกฎหมายทั้งในประเทศและต่างประเทศ เข้าใจถึงความหลากหลายทางสังคม (ตามแบบความรู้ SK9)',
 10: 'การบริหารงานวิศวกรรม: มีความรู้และความเข้าใจหลักการบริหารงานวิศวกรรม และสามารถประยุกต์ใช้หลักการบริหารในงานของตน ในฐานะผู้ร่วมทีมและผู้นำทีมเพื่อบริหารจัดการโครงการวิศวกรรมที่มีสภาพแวดล้อมและการทำงานที่มีความหลากหลายสาขาวิชาชีพ',
 11: 'การเรียนรู้ตลอดชีพ: ตระหนักถึงความจำเป็น และมีความสามารถในการเรียนรู้ตลอดชีพและพัฒนาตนเองอย่างต่อเนื่อง อาทิ การเรียนรู้ตลอดชีพและการพัฒนาตนเอง การปรับตัวต่อเทคโนโลยีใหม่ ๆ การคิดวิเคราะห์ ที่เกี่ยวข้องกับความเปลี่ยนแปลงของเทคโนโลยี (ตามแบบความรู้ SK8)',
}
INDIRECT = ['Student Exit Survey', 'Co-op Employer Survey']
DEFAULT_TARGET = 60   # OBE3 template: "ควรกำหนดไม่ต่ำกว่า 60%"

FONT = 'Tahoma'  # professional sans-serif with full Thai glyph support
def f(**k): return Font(name=FONT, size=k.pop('size', 10), **k)
BLUE = f(color='0000FF')
def fill(c): return PatternFill('solid', start_color=c, end_color=c)
F_HDR, F_GRP, F_IN, F_REQ, F_SEP, F_SUM = fill('D9E1F2'), fill('FCE4D6'), fill('FFFF00'), fill('E2EFDA'), fill('00B0F0'), fill('E2EFDA')
thin = Side(style='thin', color='BFBFBF'); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
CENTER = Alignment(horizontal='center', vertical='center', wrap_text=True)
WRAP = Alignment(vertical='top', wrap_text=True)
def note(text, w=320, h=120):
    c = Comment(text, 'TABEE draft'); c.width, c.height = w, h; return c
def style_input(cell): cell.fill = F_IN; cell.font = BLUE

GROUPS = [('foundation', 'กลุ่มวิชาพื้นฐาน'), ('core', 'กลุ่มวิชาบังคับ'), ('cwie', 'กลุ่มเสริมสร้างประสบการณ์ในวิชาชีพ'),
          ('electives/ai', 'กลุ่มวิชาเลือก: AI'), ('electives/hardware', 'กลุ่มวิชาเลือก: Hardware'),
          ('electives/network', 'กลุ่มวิชาเลือก: Network'), ('electives/software', 'กลุ่มวิชาเลือก: Software')]
GROUP_TH = dict(GROUPS)
REQUIRED = {'foundation', 'core', 'cwie'}

# proposed direct-assessment CLOs per PI = table 4.5 of the .md sections file
PROPOSED = {}
for line in open(os.path.join('tools', 'po_pi_clo_matrix_sections.md'), encoding='utf-8'):
    m = re.match(r'\| (\d+\.\d+) \| (.*?) \|', line)
    if m and m.group(1) in PIS:
        PROPOSED[m.group(1)] = set(re.findall(r'(04-\d{3}-\d{3}) (CLO\d+)', m.group(2)))

wb = Workbook()
# ======================================================================= CLO List (editable source)
cl = wb.active; cl.title = 'CLO List'
HEAD = ['รหัสวิชา', 'ชื่อวิชา', 'กลุ่ม', 'CLO', 'ผลลัพธ์การเรียนรู้ (CLO)', 'TABEE PO', 'PI (แก้ไขได้)', 'หมายเหตุ ⚑ (แก้ไขได้)',
        'ที่มา', 'ระดับ CLO (แก้ไขได้)', 'เกณฑ์ % (แก้ไขได้)', 'Key', 'Label', 'Cumulative', 'KeyCLO']
COL = {h: i + 1 for i, h in enumerate(HEAD)}
cl.append(HEAD)
rows = []
for c in sorted(C, key=lambda c: (list(GROUP_TH).index(grp(c)), c['code'])):
    for x in c['clos']:
        for po, pi in zip(x['pos'], x['pis']):
            rows.append(dict(code=c['code'], th=c['th'], grp=GROUP_TH[grp(c)], clo=x['clo'], text=x['text'], po=po, pi=pi,
                             flag=FLAG.get((c['code'], x['clo']), ''), src='OBE3' if x.get('src') == 'OBE3' else 'ร่างเสนอ',
                             lvl=x.get('clo_level', ''), target=x.get('target', DEFAULT_TARGET)))
N = len(rows); LAST = N + 1
for i, r in enumerate(rows, start=2):
    vals = [r['code'], r['th'], r['grp'], r['clo'], r['text'], r['po'], r['pi'], r['flag'], r['src'], r['lvl'], r['target']]
    for j, v in enumerate(vals, start=1): cl.cell(i, j, v)
    cl.cell(i, 12, f'=A{i}&"|"&G{i}')                                                  # Key = course|PI
    cl.cell(i, 13, f'=D{i}&IF(COUNTIFS($A$2:$A${LAST},A{i},$D$2:$D${LAST},D{i})>1,"†","")&IF(H{i}<>"","⚑","")')
    prev = f'IFERROR(LOOKUP(2,1/($L$1:L{i-1}=L{i}),$N$1:N{i-1})&" ","")' if i > 2 else '""'
    cl.cell(i, 14, f'={prev}&M{i}')                                                    # CLOs so far for this Key
    cl.cell(i, 15, f'=A{i}&"|"&D{i}&"|"&G{i}')                                         # KeyCLO = course|CLO|PI
    for j in (7, 8, 10, 11): style_input(cl.cell(i, j))
for j, w in enumerate([12, 34, 22, 7, 70, 9, 10, 40, 10, 10, 10, 16, 9, 18, 22], start=1):
    cl.column_dimensions[CL(j)].width = w
for cell in cl[1]: cell.font = f(bold=True); cell.fill = F_HDR; cell.alignment = CENTER; cell.border = BOX
for row in cl.iter_rows(min_row=2, max_row=LAST):
    for cell in row:
        if cell.column not in (7, 8, 10, 11): cell.font = f()
        cell.alignment = WRAP; cell.border = BOX
cl.freeze_panes = 'E2'; cl.auto_filter.ref = f'A1:O{LAST}'
dv = DataValidation(type='list', formula1='"' + ','.join(PIS) + '"', allow_blank=True, error='เลือก PI จากแคตตาล็อก 23 ข้อ', errorTitle='PI ไม่ถูกต้อง')
LEVELS = 'K1,K2,K3,K4,K5,K6,S1,S2,S3,S4,S5,A1,A2,A3,A4,A5'
dvl = DataValidation(type='list', formula1=f'"{LEVELS}"', allow_blank=True)
cl.add_data_validation(dv); dv.add(f'G2:G{LAST}'); cl.add_data_validation(dvl); dvl.add(f'J2:J{LAST}')
for col in 'LMNO': cl.column_dimensions[col].hidden = True
cl['G1'].comment = note('แก้ไขได้ (พื้นเหลือง ตัวอักษรน้ำเงิน): เลือก PI ของแต่ละแถว CLO–PO แล้วตาราง Matrix และ Coverage จะคำนวณใหม่อัตโนมัติ\nค่าเริ่มต้น: ตาม OBE3 ของอาจารย์ (ที่มา = OBE3) หรือร่างเสนอตามกฎในหัวข้อ 5 ของไฟล์ .md')
cl['H1'].comment = note('ใส่ข้อความเมื่อถ้อยคำ/ระดับ CLO ไม่สอดคล้องกับ PO/PI ที่แมป แล้วตาราง Matrix จะแสดง ⚑')
cl['J1'].comment = note('ระดับ Bloom ของ CLO (K1–K6 / S1–S5 / A1–A5) ตาม OBE3 หัวข้อ 4; ว่าง = ยังไม่ได้กำหนด')
cl['K1'].comment = note('เกณฑ์การบรรลุผลลัพธ์การเรียนรู้ของรายวิชา (%) ผู้สอนกำหนดเอง; OBE3 แนะนำไม่ต่ำกว่า 60%')

# ======================================================================= Matrix
mx = wb.create_sheet('PO-PI-CLO Matrix', 0)
FC = 3
mx['A1'], mx['A2'], mx['A3'] = 'PLO', 'TABEE PO', 'PI'
mx['B1'] = 'ตาราง PO–PI–CLO (ร่างเสนอ) แก้ไข PI ได้ที่แผ่นงาน "CLO List"'
for k, p in enumerate(PIS):
    col = FC + k; po = int(p.split('.')[0]); plo = PO_PLO[po]
    a, b, c3 = mx.cell(1, col, f'PLO{plo}'), mx.cell(2, col, f'PO{po}'), mx.cell(3, col, p)
    a.comment = note(f'PLO{plo}: {PLO_TXT[plo]}'); b.comment = note(f'PO{po}: {PO_FULL[po]}', 380, 160)
    c3.comment = note(f"PI{p} ({PI_CAT.get(p, {}).get('level', '')}): {PI_CAT.get(p, {}).get('text', PI_DESC[p][1])}", 380, 140)
    c3.number_format = '@'
for r in (1, 2, 3):
    for col in range(1, FC + len(PIS)):
        cell = mx.cell(r, col); cell.font = f(bold=True); cell.fill = F_HDR; cell.alignment = CENTER; cell.border = BOX
mx['B1'].alignment = Alignment(vertical='center', wrap_text=True)
r = 4; ranges = {}
for g, label in GROUPS:
    mx.cell(r, 1, label).font = f(bold=True)
    for col in range(1, FC + len(PIS)): mx.cell(r, col).fill = F_GRP; mx.cell(r, col).border = BOX
    r += 1; start = r
    for c in sorted([c for c in C if grp(c) == g], key=lambda c: c['code']):
        mx.cell(r, 1, c['code']); mx.cell(r, 2, f"{c['th']} {c['credits']}" + (' (OBE3)' if 'obe3' in c else ''))
        mx.cell(r, 2).comment = note(f"{c['code']} {c['en']} {c['credits']}\nไฟล์: {c['file']}" +
                                     (f"\nCLO/PI ตาม OBE3: {c['obe3']['file']}" if 'obe3' in c else ''), 320, 80)
        for k in range(len(PIS)):
            L = CL(FC + k)
            mx.cell(r, FC + k, f"=IFERROR(LOOKUP(2,1/('CLO List'!$L$2:$L${LAST}=$A{r}&\"|\"&{L}$3),'CLO List'!$N$2:$N${LAST}),\"\")")
        for col in range(1, FC + len(PIS)):
            cell = mx.cell(r, col); cell.font = f(size=9) if col >= FC else f(); cell.border = BOX
            cell.alignment = CENTER if col >= FC else Alignment(vertical='center')
        r += 1
    ranges[g] = (start, r - 1)
r += 1
mx.cell(r, 1, 'ความครอบคลุม PI (รายวิชาที่นักศึกษาทุกคนต้องเรียน)').font = f(bold=True)
for col in range(1, FC + len(PIS)): mx.cell(r, col).fill = F_REQ
r += 1
R_MIN, R_REQ, R_EL, R_ST = r, r + 1, r + 2, r + 3
for rr, t in {R_MIN: 'ขั้นต่ำ direct (TABEE)', R_REQ: 'จำนวนรายวิชาบังคับที่ครอบคลุม', R_EL: 'จำนวนวิชาเลือกที่ครอบคลุม', R_ST: 'สถานะ'}.items():
    mx.cell(rr, 2, t).font = f(bold=True)
fd, fc_, fw = ranges['foundation'], ranges['core'], ranges['cwie']
cw301 = [i for i in range(fw[0], fw[1] + 1) if mx.cell(i, 1).value == '04-000-301'][0]
opt = (cw301 + 1, fw[1])
el = [ranges[g] for g, _ in GROUPS if g.startswith('electives')]
for k, p in enumerate(PIS):
    L = CL(FC + k); po = int(p.split('.')[0])
    mx.cell(R_MIN, FC + k, 2 if po <= 3 else 1).font = BLUE
    mx.cell(R_REQ, FC + k, f'=COUNTIF({L}{fd[0]}:{L}{fd[1]},"?*")+COUNTIF({L}{fc_[0]}:{L}{fc_[1]},"?*")'
                           f'+COUNTIF({L}{cw301},"?*")+IF(COUNTIF({L}{opt[0]}:{L}{opt[1]},"?*")={opt[1]-opt[0]+1},1,0)')
    mx.cell(R_EL, FC + k, '=' + '+'.join(f'COUNTIF({L}{a}:{L}{b},"?*")' for a, b in el))
    mx.cell(R_ST, FC + k, f'=IF({L}{R_REQ}>={L}{R_MIN},"✅",IF({L}{R_REQ}>0,"⚠️","❌"))')
    for rr in (R_MIN, R_REQ, R_EL, R_ST):
        cell = mx.cell(rr, FC + k); cell.alignment = CENTER; cell.border = BOX
        if rr != R_MIN: cell.font = f(bold=(rr == R_ST))
mx.cell(R_MIN, 2).comment = note('เกณฑ์ TABEE (ศ.สมศักดิ์ / คู่มือ SER): PO1–3 ต้องมี direct ≥ 2 ต่อ PI, PO4–11 ต้องมี direct ≥ 1 ต่อ PI (และ indirect ≥ 1 / ≥ 2 ตามลำดับ)')
mx.cell(R_REQ, 2).comment = note('นับรายวิชา (ไม่ใช่จำนวน CLO) ในกลุ่มพื้นฐาน + กลุ่มบังคับ + 04-000-301 และนับรูปแบบ CWIE เป็น 1 วิชา เฉพาะเมื่อทุกรูปแบบ (04-000-302/303/401/402/403) ครอบคลุม PI นั้น ไม่นับวิชาเลือก')
mx.cell(R_ST + 2, 2, '✅ ผ่านขั้นต่ำ · ⚠️ มีแต่ไม่ถึงขั้นต่ำ · ❌ ไม่มีรายวิชาบังคับรองรับ  |  † = CLO เดียวหลาย PO (ควรแยก) · ⚑ = ข้อสังเกต (ดูหมายเหตุใน CLO List) · (OBE3) = CLO/PI ตาม OBE3 ของอาจารย์').font = f(size=9, italic=True)
mx.column_dimensions['A'].width = 12; mx.column_dimensions['B'].width = 46
for k in range(len(PIS)): mx.column_dimensions[CL(FC + k)].width = 8.5
mx.freeze_panes = mx.cell(4, FC)

# ======================================================================= PO1..PO11 (assessment plan per PO)
PH = ['TABEE PO', 'PI', 'ระดับ PI', 'รายวิชาที่รับผิดชอบ', 'ประเภท', 'CLO', 'ผลลัพธ์การเรียนรู้ (CLO)', 'ระดับ CLO',
      'ความสอดคล้องกับระดับ PI', 'ใช้ประเมิน (Y/N)', 'เกณฑ์ (%)', 'CLO Attainment (%)', 'ผล', 'ผู้รับผิดชอบรายวิชา',
      'ที่มา CLO/PI', 'Noted', 'KeyCLO']
PW = [9, 7, 13, 34, 9, 7, 52, 9, 22, 10, 9, 12, 10, 26, 10, 26, 18]
yn = DataValidation(type='list', formula1='"Y,N"', allow_blank=False)
LIST = "'CLO List'"
req_courses = sorted([c for c in C if grp(c) in REQUIRED], key=lambda c: (list(GROUP_TH).index(grp(c)), c['code']))
po_sheets = []
for po in range(1, 12):
    ws = wb.create_sheet(f'PO{po}'); po_sheets.append(ws); ws.add_data_validation(yn)
    pis = [p for p in PIS if int(p.split('.')[0]) == po]; plo = PO_PLO[po]
    ws['A1'] = f'แผนการประเมิน TABEE PO{po} (Direct / Indirect Assessment)'; ws['A1'].font = f(bold=True, size=12)
    ws['A2'], ws['B2'] = f'TABEE PO{po}', PO_FULL[po]
    ws['A3'], ws['B3'] = f'PLO{plo}', PLO_TXT[plo]
    rr = 4
    for p in pis:
        ws.cell(rr, 1, f'PI{p}'); ws.cell(rr, 2, f"PI {p} {PI_CAT.get(p, {}).get('text', PI_DESC[p][1])} ({PI_CAT.get(p, {}).get('level', '')})"); rr += 1
    ws.cell(rr, 1, 'เกณฑ์ผ่าน PI (%)').font = f(bold=True)
    tgt = ws.cell(rr, 3, DEFAULT_TARGET); style_input(tgt); TGT = f'$C${rr}'
    tgt.comment = note('ระดับความสำเร็จที่คาดหวังของ PI (ค่าเฉลี่ย CLO attainment ของการประเมิน direct ที่เลือกใช้) — หลักสูตรกำหนด; ค่าเริ่มต้น 60% ตามข้อแนะนำใน OBE3')
    for row in ws.iter_rows(min_row=2, max_row=rr):
        for cell in row:
            if not cell.font.bold and cell.fill.start_color.rgb != 'FFFFFF00': cell.font = f()
            cell.alignment = Alignment(vertical='top', wrap_text=False)
    rr += 2
    for j, h in enumerate(PH, start=1):
        cell = ws.cell(rr, j, h); cell.font = f(bold=True); cell.fill = F_HDR; cell.alignment = CENTER; cell.border = BOX
    hdr_row = rr; rr += 1
    for p in pis:
        lv = PI_CAT.get(p, {}).get('level', '')
        block = []
        for c in req_courses:
            for x in c['clos']:
                if p in x['pis']: block.append((c, x))
        prop = PROPOSED.get(p, set())
        start = rr
        for c, x in block:
            use = 'Y' if (not prop or (c['code'], x['clo']) in prop) else 'N'
            lect = c['obe3']['lecturer'] if 'obe3' in c else ''
            vals = [f'PO{po}', p, lv, f"{c['code']} {c['th']}", 'Direct', x['clo'], x['text'], None, None, use, None, None, None,
                    lect, 'OBE3' if x.get('src') == 'OBE3' else 'ร่างเสนอ', '', f"{c['code']}|{x['clo']}|{p}"]
            for j, v in enumerate(vals, start=1): ws.cell(rr, j, v)
            k = f'$Q{rr}'
            ws.cell(rr, 8, f'=IFERROR(INDEX({LIST}!$J$2:$J${LAST},MATCH({k},{LIST}!$O$2:$O${LAST},0))&"","")')
            ws.cell(rr, 11, f'=IFERROR(INDEX({LIST}!$K$2:$K${LAST},MATCH({k},{LIST}!$O$2:$O${LAST},0)),"")')
            ws.cell(rr, 9, f'=IF(ISNA(MATCH({k},{LIST}!$O$2:$O${LAST},0)),"⚠ PI ใน CLO List ถูกเปลี่ยน",'
                           f'IF(OR(H{rr}="",C{rr}=""),"",IF(LEFT(H{rr},1)<>LEFT(C{rr},1),"โดเมนต่างจาก PI",'
                           f'IF(VALUE(MID(H{rr},2,1))>=VALUE(MID(C{rr},2,1)),"✓","ระดับต่ำกว่า PI"))))')
            ws.cell(rr, 13, f'=IF(OR(L{rr}="",K{rr}=""),"",IF(L{rr}>=K{rr},"บรรลุ","ไม่บรรลุ"))')
            for j in (10, 12, 14, 16): style_input(ws.cell(rr, j))
            yn.add(f'J{rr}')
            rr += 1
        for s in INDIRECT:
            vals = [f'PO{po}', p, lv, s, 'Indirect', '', 'แบบสอบถามที่ถามถึง PO นี้โดยตรง (ไม่ใช่ความพึงพอใจทั่วไป)', '', '', 'Y', None, None, None, '', '', '', '']
            for j, v in enumerate(vals, start=1): ws.cell(rr, j, v)
            ws.cell(rr, 4).font = f(color='0070C0')
            ws.cell(rr, 13, f'=IF(OR(L{rr}="",K{rr}=""),"",IF(L{rr}>=K{rr},"บรรลุ","ไม่บรรลุ"))')
            for j in (10, 11, 12, 14, 16): style_input(ws.cell(rr, j))
            yn.add(f'J{rr}')
            rr += 1
        end = rr - 1
        # PI summary row
        need = 2 if po <= 3 else 1
        E, J, Lc = (f'{col}{start}:{col}{end}' for col in 'EJL')
        ws.cell(rr, 1, f'สรุป PI{p}')
        ws.cell(rr, 4, f'="Direct ที่ใช้ "&COUNTIFS({E},"Direct",{J},"Y")&" / ขั้นต่ำ {need} · Indirect ที่ใช้ "&COUNTIFS({E},"Indirect",{J},"Y")&" / ขั้นต่ำ {1 if po <= 3 else 2}"')
        ws.cell(rr, 5, f'=IF(AND(COUNTIFS({E},"Direct",{J},"Y")>={need},COUNTIFS({E},"Indirect",{J},"Y")>={1 if po <= 3 else 2}),"✅",IF(COUNTIFS({E},"Direct",{J},"Y")>0,"⚠️","❌"))')
        ws.cell(rr, 11, '=' + TGT)
        ws.cell(rr, 12, f'=IFERROR(AVERAGEIFS({Lc},{E},"Direct",{J},"Y"),"")')
        ws.cell(rr, 13, f'=IF(L{rr}="","",IF(L{rr}>={TGT},"บรรลุ","ไม่บรรลุ"))')
        ws.cell(rr, 7, 'ค่าเฉลี่ย CLO Attainment ของ Direct ที่ใช้ (Y) เทียบกับเกณฑ์ผ่าน PI')
        for row in ws.iter_rows(min_row=start, max_row=rr, max_col=len(PH) - 1):
            for cell in row:
                cell.border = BOX
                if cell.row == rr: cell.fill = F_SUM; cell.font = f(bold=True)
                elif cell.font.color is None or cell.font.color.rgb in (None, 'FF000000'):
                    if not (cell.fill and cell.fill.start_color.rgb == 'FFFFFF00'): cell.font = f()
                cell.alignment = CENTER if cell.column in (1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 15) else WRAP
        rr += 1
        for j in range(1, len(PH)): ws.cell(rr, j).fill = F_SEP
        rr += 1
    for j, w in enumerate(PW, start=1): ws.column_dimensions[CL(j)].width = w
    ws.column_dimensions['Q'].hidden = True
    ws.freeze_panes = ws.cell(hdr_row + 1, 5)
    ws.cell(hdr_row, 10).comment = note('Y = ใช้ผลนี้ประเมิน PI (ค่าเริ่มต้นตามข้อเสนอในหัวข้อ 4.5 ของไฟล์ .md); N = ไม่ใช้ เช่น มีรายวิชาอื่นที่เหมาะกว่า')
    ws.cell(hdr_row, 12).comment = note('ร้อยละของนักศึกษาที่บรรลุเกณฑ์ของ CLO นี้ (ผู้สอนกรอกหลังประเมินผล)')
    ws.cell(hdr_row, 9).comment = note('เทียบระดับ CLO กับระดับของ PI ในแคตตาล็อก: ✓ = เท่ากันหรือสูงกว่า · ระดับต่ำกว่า PI · โดเมนต่างจาก PI (K/S/A)\n"⚠ PI ใน CLO List ถูกเปลี่ยน" = แถวนี้สร้างจากค่าเดิม ให้สร้างไฟล์ใหม่หรือย้ายแถวเอง')

# ======================================================================= PI Catalog & SK
pc = wb.create_sheet('PI Catalog')
pc.append(['PI', 'TABEE PO', 'หัวข้อ PO', 'PLO', 'ข้อความ PLO', 'แบบความรู้', 'ระดับ (Taxonomy)', 'ข้อความ PI (OBE3-TABEE)'])
for p in PIS:
    po = int(p.split('.')[0]); plo = PO_PLO[po]
    pc.append([p, f'PO{po}', PO_TXT[po], f'PLO{plo}', PLO_TXT[plo], PI_DESC[p][0], PI_CAT.get(p, {}).get('level', ''),
               PI_CAT.get(p, {}).get('text', PI_DESC[p][1])])
pc.append([]); pc.append(['หมายเหตุ: PI11.2 อยู่ภายใต้ PO11 (ไฟล์ต้นแบบ OBE3_TABEE.doc พิมพ์ผิดเป็น "PO12") · ข้อความและระดับ PI จากแบบฟอร์ม OBE3-TABEE'])
for j, w in enumerate([7, 9, 34, 7, 46, 11, 16, 70], start=1): pc.column_dimensions[CL(j)].width = w
sk = wb.create_sheet('SK')
sk.append(['SK', 'หมวด', 'คำอธิบาย (ไทย)', 'Definition (IEA 2021)', 'PI ที่ใช้'])
for s, (name, th, en) in SK.items():
    sk.append([s, name, th, en, ', '.join(p for p in PIS if s in PI_DESC[p][0].replace(' ', '').split(','))])
sk.append([]); sk.append(['ที่มา: IEA Graduate Attributes and Professional Competencies 2021; LO Writing Manual TABEE PO-PI-CLO ENG RMUTT'])
for j, w in enumerate([6, 28, 60, 60, 16], start=1): sk.column_dimensions[CL(j)].width = w
for ws in (pc, sk):
    for cell in ws[1]: cell.font = f(bold=True); cell.fill = F_HDR; cell.alignment = CENTER; cell.border = BOX
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.font = f(); cell.alignment = WRAP
            if cell.value is not None and ws.cell(1, cell.column).value: cell.border = BOX
    ws.freeze_panes = 'B2'

# ======================================================================= README
rd = wb.create_sheet('README', 0)
lines = [
    ('PO–PI–CLO Matrix และแผนการประเมิน | CPE RMUTT 2568 (TABEE, Sydney Accord)', dict(bold=True, size=14)),
    ('สถานะ: ร่างเสนอ (Draft) รอคณะกรรมการหลักสูตรพิจารณา', dict(bold=True, color='C00000')),
    ('', {}),
    ('แผ่นงาน', dict(bold=True)),
    ('• PO-PI-CLO Matrix: ตารางรายวิชา × PI (รูปแบบเดียวกับ "PO-PI-CLO Matrix" ของหลักสูตร IE) พร้อมแถวความครอบคลุมเทียบเกณฑ์ TABEE ด้านล่าง', {}),
    ('• PO1–PO11: แผนการประเมินรายผลลัพธ์ (รูปแบบเดียวกับแผ่นงาน PO1–PO11 ของหลักสูตร IE): ต่อ PI แสดงรายวิชาบังคับที่ประเมินแบบ Direct + แบบสอบถาม 2 ชุด (Indirect) และแถวสรุป', {}),
    ('• CLO List: CLO ทุกข้อ 1 แถวต่อ 1 คู่ CLO–PO เป็นข้อมูลต้นทางของตาราง Matrix', {}),
    ('• PI Catalog / SK: ข้อความและระดับของ PI 23 ข้อ และแบบความรู้ SK1–SK9', {}),
    ('', {}),
    ('ช่องที่แก้ไขได้ (พื้นเหลือง ตัวอักษรน้ำเงิน)', dict(bold=True)),
    ('• CLO List: PI · หมายเหตุ ⚑ · ระดับ CLO · เกณฑ์ %  (ตาราง Matrix และสถานะคำนวณใหม่ทันที)', {}),
    ('  ตัวอย่าง: แถว 04-620-401 | CLO2 | PO2 → เปลี่ยน PI จาก 2.4 เป็น 2.3 แล้ว CLO2 จะย้ายคอลัมน์ในตาราง Matrix ทันที', dict(italic=True)),
    ('• PO1–PO11: เกณฑ์ผ่าน PI (%) ด้านบน · ใช้ประเมิน (Y/N) · CLO Attainment (%) · ผู้รับผิดชอบรายวิชา · Noted · เกณฑ์ของแถว Indirect', {}),
    ('  ตัวอย่าง: PO1 › PI1.1 › 04-621-201 CLO1 → กรอก CLO Attainment 72 แล้วช่อง "ผล" จะแสดง "บรรลุ" และแถวสรุป PI1.1 จะคำนวณค่าเฉลี่ย', dict(italic=True)),
    ('• ห้ามแก้ไขเซลล์ที่เป็นสูตร (ตาราง Matrix, แถวสรุป, ระดับ CLO/เกณฑ์/ความสอดคล้องใน PO1–PO11)', {}),
    ('• แถวในแผ่นงาน PO1–PO11 ถูกสร้างตาม PI ใน CLO List ณ เวลาสร้างไฟล์ ถ้าเปลี่ยน PI ภายหลัง แถวเดิมจะแสดง "⚠ PI ใน CLO List ถูกเปลี่ยน" ให้สร้างไฟล์ใหม่หรือย้ายแถวเอง', {}),
    ('', {}),
    ('สัญลักษณ์', dict(bold=True)),
    ('• † = CLO เดียวรับผิดชอบหลาย PO (ขัดกฎ 1 CLO : 1 PI ควรแยก CLO) · ⚑ = ข้อสังเกต (ถ้อยคำ/ระดับไม่สอดคล้อง) · (OBE3) = CLO/PI ตาม OBE3 ที่อาจารย์กรอก', {}),
    ('• สถานะ: ✅ ผ่านขั้นต่ำ · ⚠️ มีแต่ไม่ถึงขั้นต่ำ · ❌ ไม่มีรายวิชาบังคับรองรับ', {}),
    ('', {}),
    ('ที่มาของข้อมูล', dict(bold=True)),
    ('• CLO และการแมป CLO → PO: ไฟล์รายวิชาใน courses/ · สำหรับรายวิชาที่มีไฟล์ OBE3-TABEE ที่อาจารย์กรอกแล้ว ใช้ CLO/PI/ระดับ/เกณฑ์ตาม OBE3 (tools/obe3_clo_pi.json)', {}),
    ('• CLO → PI ของรายวิชาอื่น: ร่างเสนอตามกฎในหัวข้อ 5 ของ CPE_RMUTT68_PO_PI_CLO_Matrix.md', {}),
    ('• ข้อความ/ระดับ PI: แบบฟอร์ม OBE3-TABEE · SK: IEA Graduate Attributes 2021 · ความหมาย TABEE PO: TABEE Preparation_หลักสูตร คอมพิวเตอร์ (อบรม 21 เม.ย. 69)', {}),
    ('• เกณฑ์ direct/indirect: เอกสารอบรม ศ.สมศักดิ์ และคู่มือ SER (TABEE) · Indirect 2 ชุดต่อ PI ตามรูปแบบของหลักสูตร IE (Student Exit Survey, Co-op Employer Survey)', {}),
    ('• สร้างโดย tools/build_po_pi_clo_xlsx.py (การสร้างใหม่จะเขียนทับการแก้ไขในไฟล์นี้)', {}),
]
for i, (t, st) in enumerate(lines, start=1): rd.cell(i, 1, t).font = f(**st)
rd.column_dimensions['A'].width = 160
# sheet order: README, Matrix, PO1..PO11, CLO List, PI Catalog, SK
order = ['README', 'PO-PI-CLO Matrix'] + [f'PO{i}' for i in range(1, 12)] + ['CLO List', 'PI Catalog', 'SK']
wb._sheets = [wb[n] for n in order]
wb.active = 0
wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print('saved', OUT, '| CLO-PO rows:', N, '| PO sheets:', len(po_sheets))
