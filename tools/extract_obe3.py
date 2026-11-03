"""Extract lecturer-confirmed CLO -> PI data from filled OBE3-TABEE syllabi into tools/obe3_clo_pi.json.

Usage:  python -I tools/extract_obe3.py
Reads source_documents/OBE 3_TABEE_*.pdf (git-ignored; synced via OneDrive/SharePoint) and writes a
small tracked JSON so the matrix builders work on PCs without the PDFs. Needs PyMuPDF (pymupdf).

Per syllabus it takes section 4 "ผลลัพธ์การเรียนรู้ระดับรายวิชา (CLOs) ที่สอดคล้องกับ PI, TABEE PO ..."
rows:  PI | PI level | CLO | CLO text | CLO level | target %
plus course code/name from section 1 and the responsible lecturer (อาจารย์ผู้รับผิดชอบรายวิชา).
It also stores the PI catalog (full text + level) from the first syllabus that has one.
"""
import os, re, sys, glob, json
import pymupdf
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'source_documents')
OUT = os.path.join(ROOT, 'tools', 'obe3_clo_pi.json')

# Legacy Thai fonts store shifted tone/vowel marks in the Private Use Area (U+F700-F71A); map them back.
THAI_PUA = dict(zip(range(0xF700, 0xF71B), 'ฐิีึื่้๊๋์'
                                             '่้๊๋์ญัํ็'
                                             '่้๊๋์ฺุู'))
def text_of(path):
    d = pymupdf.open(path)
    t = '\n'.join(p.get_text() for p in d).translate(THAI_PUA)
    t = t.replace('ํา', 'ำ')   # ํ + า  ->  ำ
    t = re.sub(r'OBE 3-TABEE-\s*RMUTT\s*\S+\s*\|\s*P a g e', ' ', t)
    return ' '.join(t.split())

# OBE3 files whose course code differs from the repo's course file for the same course
DOC_TO_REPO = {
    '04-622-301': ('04-622-302', 'ไฟล์ OBE3 ระบุรหัส 04-622-301 แต่เป็นวิชาวิศวกรรมซอฟต์แวร์ ซึ่งในหลักสูตร (repo) คือ 04-622-302; '
                                 '04-622-301 ในหลักสูตรคือ Full-stack Web Development'),
}
courses, catalog = {}, {}
for f in sorted(glob.glob(os.path.join(SRC, 'OBE 3_TABEE_*.pdf'))):
    t = text_of(f); name = os.path.basename(f)
    code = re.sub(r'(\d{2})-?(\d{3})-?(\d{3})', r'\1-\2-\3', re.search(r'TABEE_(04-?\d{3}-?\d{3})', name).group(1))
    repo_code, code_note = DOC_TO_REPO.get(code, (code, ''))
    k = t.find('รับผิดชอบรายวิชา')
    lec = re.match(r'รับผิดชอบรายวิชา\s+(.*?)\s+(?:E-mail:|อีเมล:|\S+@)', t[k:k + 200]) if k >= 0 else None
    i = t.find('ที่สอดคล'); i = t.find('PI, TABEE PO', i)
    j = t.find('CLO 1 ข', i)
    sec = t[i:j if j > 0 else i + 8000]
    ms = list(re.finditer(r'PI ?(\d+\.\d)\s+([KSA]\d)\s+CLO ?(\d+)\s+(.*?)\s+([KSA]\d)\s+(\d+)\s*%', sec))
    clos = []
    for n, m in enumerate(ms):
        # CLO text that continues past a page break lands after the "60%" cell; append it
        tail = sec[m.end(): ms[n + 1].start() if n + 1 < len(ms) else len(sec)]
        tail = re.split(r'หมายเหตุ|PI\s+K/S/A', tail)[0].strip()
        text = (m.group(4).strip() + (' ' + tail if tail and len(tail) < 150 else '')).strip()
        clos.append(dict(clo='CLO' + m.group(3), pi=m.group(1), pi_level=m.group(2), text=text,
                         clo_level=m.group(5), target=int(m.group(6))))
    courses[repo_code] = dict(file=name, code_in_doc=code, code_note=code_note,
                         lecturer=lec.group(1).strip() if lec else None, clos=clos)
    # PI catalog: keep the copy with the most Thai tone marks (some PDFs drop ่ ้ ์ when extracted)
    k = t.find('PI 1.1 '); cat = {}
    for pm in re.finditer(r'PI ?(\d+\.\d) (.*?)\(([KSA]\d-[^)]*)\)', t[k:t.find('4. ผลลัพธ์', k)] if k >= 0 else ''):
        txt = re.sub(r'^PI ?\d+\.\d\s*', '', ' '.join(pm.group(2).split()))
        txt = re.sub(r'\s*TABEE PO เลือก (?:✓ )?PI ข้อความ\s*', ' ', txt)  # table header repeated at a page break
        cat.setdefault(pm.group(1), dict(text=txt.strip(), level=pm.group(3)))
    score = lambda c: sum(v['text'].count('้') + v['text'].count('์') for v in c.values())
    if len(cat) == 23 and score(cat) > score(catalog): catalog = cat
    print(f"{code}  {len(clos)} CLOs  {name}")
json.dump(dict(source='source_documents/OBE 3_TABEE_*.pdf', pi_catalog=catalog, courses=courses),
          open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('PI catalog entries:', len(catalog), '->', os.path.relpath(OUT, ROOT))
