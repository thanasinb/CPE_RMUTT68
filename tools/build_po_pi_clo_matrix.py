"""Build CPE_RMUTT68_PO_PI_CLO_Matrix.md from the course files.

Usage (from anywhere):  python -I tools/build_po_pi_clo_matrix.py

- Parses every courses/**/*.md: CLO table rows (| <a id="cloN"></a>CLON | text | ... |)
  and the CLO->TABEE PO bullets in the HTML "PLO Mapping" table (<th>TABEE PO</th> row).
- Assigns a PI to each CLO with the rules documented in section 5 of the output
  (edit OV / FLAG below to override a single CLO).
- PLO / PO tooltip text is read from CPE_RMUTT68_Prospectus.md (#ploN anchors) and
  CPE_RMUTT68_TABEE_PO_Mapping.md (#poN anchors).
- Sections 4-5 (hand-written issues and rules) come from tools/po_pi_clo_matrix_sections.md;
  PI/PO/PLO/SK/CLO mentions in it are linked automatically.
"""
import sys, os, re, json, glob
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT = 'CPE_RMUTT68_PO_PI_CLO_Matrix.md'
SECTIONS = os.path.join('tools', 'po_pi_clo_matrix_sections.md')

def parse_courses():
    out = []
    for p in sorted(glob.glob(os.path.join('courses', '**', '*.md'), recursive=True)):
        t = open(p, encoding='utf-8').read()
        fm = dict(re.findall(r'^(\w+):\s*(.*)$', t.split('---')[1], re.M))
        clos = dict(re.findall(r'^\|\s*(?:<a id="clo\d+"></a>)?(CLO\d+)\s*\|\s*(.*?)\s*\|\s*.*\|\s*$', t, re.M))
        pomap = {}
        m = re.search(r'<tr>\s*<th>TABEE PO</th>(.*?)</tr>(.*?)</table>', t, re.S)
        if m:
            hdr = re.findall(r'<th>(PO\d+)</th>', m.group(1))
            for row in re.findall(r'<tr>(.*?)</tr>', m.group(2), re.S):
                cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
                if cells:
                    pomap[cells[0].strip()] = [hdr[i] for i, v in enumerate(cells[1:]) if '●' in v]
        out.append(dict(file=p.replace(os.sep, '/'), code=fm.get('code'), th=fm.get('name_th'), en=fm.get('name_en'),
                        credits=fm.get('credits'), type=fm.get('type'), year=fm.get('year'), sem=fm.get('semester'),
                        clos=[dict(clo=c, text=clos[c], pos=pomap.get(c, [])) for c in clos]))
    return out

C = parse_courses()
PIS = ['1.1','1.2','1.3','1.4','2.1','2.2','2.3','2.4','3.1','4.1','4.2','5.1','5.2','6.1','7.1','7.2','8.1','8.2','8.3','9.1','10.1','11.1','11.2']
# PO -> PLO, 1:1 via the sub-PLOs PLO4.1-4.2 and PLO8.1-8.3 (Prospectus §3)
PO_PLO = {1:'1',2:'4.1',3:'2',4:'4.2',5:'5',6:'8.1',7:'8.2',8:'3',9:'6',10:'8.3',11:'7'}
PI_DESC = {
'1.1':('SK1','ประยุกต์หลักการวิทยาศาสตร์ธรรมชาติ (ฟิสิกส์) ในขั้นตอน/กระบวนการ/ระบบทางวิศวกรรม'),
'1.2':('SK2','ใช้คณิตศาสตร์ การวิเคราะห์เชิงตัวเลข สถิติ วิทยาการคอมพิวเตอร์ เพื่อพิจารณาหรือใช้แบบจำลอง'),
'1.3':('SK3','ประยุกต์หลักการพื้นฐานทางวิศวกรรม'),
'1.4':('SK4','ใช้ความรู้เฉพาะทางวิศวกรรม'),
'2.1':('SK1','วิเคราะห์ปัญหาที่กำหนดไว้อย่างกว้าง ๆ ด้วยเครื่องมือทางวิทยาศาสตร์ธรรมชาติ'),
'2.2':('SK2','วิเคราะห์ปัญหาฯ ด้วยคณิตศาสตร์ สถิติ วิทยาการคอมพิวเตอร์/สารสนเทศ'),
'2.3':('SK3','วิเคราะห์ปัญหาฯ ด้วยเครื่องมือพื้นฐานทางวิศวกรรม'),
'2.4':('SK4','วิเคราะห์ปัญหาฯ ด้วยเครื่องมือความรู้เฉพาะทางวิศวกรรม'),
'3.1':('SK5','ออกแบบแนวทางแก้ปัญหา/ระบบ/ชิ้นงาน โดยคำนึงถึงความปลอดภัย ต้นทุนตลอดอายุ Net Zero สังคม สิ่งแวดล้อม'),
'4.1':('SK8','ค้นหา สืบค้น คัดเลือกข้อมูลจากมาตรฐาน ฐานข้อมูล เอกสารวิชาการ'),
'4.2':('SK8','ออกแบบและดำเนินการทดลองเพื่อให้ได้ข้อสรุปที่ถูกต้อง'),
'5.1':('SK2, SK6','เลือกใช้เทคนิค ทรัพยากร เครื่องมือวิศวกรรม/IT โดยคำนึงถึงข้อจำกัด'),
'5.2':('SK6','ปฏิบัติการใช้เครื่องมือเทคโนโลยีทางวิศวกรรมได้อย่างถูกต้อง'),
'6.1':('SK9','ทำงานร่วมกับผู้อื่นที่มีความหลากหลายได้อย่างมีประสิทธิภาพ'),
'7.1':('—','สื่อสารภาษาไทยได้อย่างมีประสิทธิภาพ'),
'7.2':('—','สื่อสารภาษาอังกฤษได้อย่างมีประสิทธิภาพ'),
'8.1':('SK1','ให้ความเห็นเกี่ยวกับผลกระทบต่อการพัฒนาที่ยั่งยืน ฯลฯ จากความรู้วิทยาศาสตร์ธรรมชาติ'),
'8.2':('SK5','ให้ความเห็นเกี่ยวกับผลกระทบฯ จากความรู้ด้านทรัพยากร สิ่งแวดล้อม ต้นทุนตลอดวงจรชีวิต Net Zero'),
'8.3':('SK7','ให้ความเห็นเกี่ยวกับผลกระทบฯ จากความรู้บทบาทของเทคโนโลยีในสังคม'),
'9.1':('SK9','สร้างค่านิยมที่สอดคล้องกับจรรยาบรรณวิชาชีพและบรรทัดฐานการปฏิบัติงาน'),
'10.1':('—','ใช้หลักการบริหารจัดการทางวิศวกรรมเพื่อบริหารโครงการแบบพหุสาขาวิชา'),
'11.1':('SK8','เรียนรู้ด้วยตนเองในการค้นคว้าเอกสารเกี่ยวกับเทคโนโลยีปัจจุบัน'),
'11.2':('SK8','วิพากษ์เทคโนโลยีเฉพาะทางใหม่ ๆ ของสาขาวิชา'),
}
# course-specific PI overrides (knowledge-profile level for PO1/PO2, sustainability for PO8)
OV = {('04-621-201','CLO1'):'1.1',('04-621-201','CLO2'):'1.1',('04-621-202','CLO1'):'1.1',('04-621-202','CLO2'):'1.3',
      ('04-622-201','CLO1'):'1.2',('04-622-201','CLO2'):'1.2',('04-622-201','CLO4'):'2.2',
      ('04-624-201','CLO1'):'2.2',('04-624-201','CLO3'):'2.2',
      ('04-622-308','CLO2'):'8.2'}
FLAG = {}
def grp(c):
    f = c['file'].split('/'); return f[1] if f[1] != 'electives' else 'electives/' + f[2]
def assign(c, x):
    code, clo, t = c['code'], x['clo'], x['text']; g = grp(c); res = []
    for po in x['pos']:
        n = int(po[2:]); o = OV.get((code, clo))
        if o and o.split('.')[0] == str(n): res.append(o); continue
        if n == 1: res.append('1.3' if g == 'foundation' else '1.4')
        elif n == 2: res.append('2.3' if g == 'foundation' else '2.4')
        elif n == 3: res.append('3.1')
        elif n == 4: res.append('4.2')
        elif n == 5: res.append('5.1' if 'เลือก' in t else '5.2')
        elif n == 6: res.append('6.1')
        elif n == 7: res.append('7.1')
        elif n == 8: res.append('8.3')
        elif n == 9: res.append('9.1')
        elif n == 10: res.append('10.1')
        elif n == 11: res.append('11.2' if re.search('วิพากษ์|วิจารณ์', t) else '11.1')
    return res
for c in C:
    for x in c['clos']:
        t = x['text'].replace('สามารถ', '').replace('นักศึกษา', '').strip()
        k = (c['code'], x['clo'])
        if 'PO3' in x['pos'] and re.match(r'(อธิบาย|บรรยาย|เข้าใจ|แยกแยะ)', t) and 'ประยุกต์' not in t and 'ออกแบบ' not in t:
            FLAG[k] = 'แมป PO3 (PI3.1 = ออกแบบ, K6) แต่ใช้คำกริยาระดับต่ำกว่าการออกแบบ (อธิบาย/เข้าใจ/แยกแยะ)'
        if 'PO2' in x['pos'] and re.match(r'(อธิบาย|บรรยาย)', t):
            FLAG[k] = 'แมป PO2 (PI2.x = วิเคราะห์, K4) แต่ใช้คำกริยา "อธิบาย"'
FLAG[('04-620-401','CLO1')] = 'เป็นการส่งรายงาน/ปริญญานิพนธ์ ซึ่งตรงกับ PO7 (สื่อสาร) มากกว่า PO8 (ผลกระทบต่อโลก)'
FLAG[('04-620-301','CLO3')] = '"ปรับตัวและแก้ไขสถานการณ์" ไม่ใช่การเรียนรู้ด้วยตนเองจากเอกสารเทคโนโลยี (PI11.1) โดยตรง'
FLAG[('04-622-302','CLO5')] = '"นำเสนอเป็นแผนภาพ" ใกล้เคียง PO7 (สื่อสาร) มากกว่า PO5 (เครื่องมือ)'
for c in C:
    for x in c['clos']: x['pis'] = assign(c, x); x['src'] = 'draft'

# ---- lecturer-confirmed data from filled OBE3-TABEE syllabi (tools/extract_obe3.py) overrides the draft ----
OBE3 = json.load(open(os.path.join('tools', 'obe3_clo_pi.json'), encoding='utf-8')) if os.path.exists(os.path.join('tools', 'obe3_clo_pi.json')) else {'pi_catalog': {}, 'courses': {}}
PI_LEVEL = {p: v['level'] for p, v in OBE3['pi_catalog'].items()}
def lv_num(s): return int(s[1]) if s and len(s) > 1 and s[1].isdigit() else None
def level_issue(pi_lv, clo_lv):
    """Compare a CLO's taxonomy level with its PI's level (catalog). Returns '' when aligned."""
    if not pi_lv or not clo_lv: return ''
    if pi_lv[0] != clo_lv[0]: return f'โดเมนต่างจาก PI ({clo_lv} เทียบกับ {pi_lv[:2]})'
    if lv_num(clo_lv) < lv_num(pi_lv): return f'ระดับต่ำกว่า PI ({clo_lv} < {pi_lv[:2]})'
    return ''
import difflib
def norm(s):
    """Compare Thai text ignoring PDF artefacts: spaces/line breaks, dropped tone/vowel marks, ํา vs ำ, a leading 'สามารถ'."""
    s = re.sub(r'\s+', '', s).replace('ํา', 'ำ').replace('ํ', '')
    s = re.sub('[ัิ-ฺ็-๎]', '', s)
    return s[len('สามารถ'):] if s.startswith('สามารถ') else s
def similarity(a, b):
    na, nb = norm(a), norm(b)
    short, long_ = sorted((na.removesuffix('ได'), nb.removesuffix('ได')), key=len)
    if len(short) >= 10 and short in long_: return 0.9          # one is a shortened form of the other
    return difflib.SequenceMatcher(None, na, nb).ratio()
for c in C:
    o = OBE3['courses'].get(c['code'])
    if not o: continue
    for x in c['clos']: FLAG.pop((c['code'], x['clo']), None)   # draft wording flags no longer apply
    c['repo_clos'] = c['clos']; c['obe3'] = o
    c['clos'] = []
    used = set()
    for r in o['clos']:
        # match each OBE3 CLO to the most similar CLO in the repo course file (numbering can differ)
        best = max(((similarity(r['text'], x['text']), x) for x in c['repo_clos'] if x['clo'] not in used),
                   key=lambda t: t[0], default=(0, None))
        match = best[1] if best[0] >= 0.6 else None
        if match: used.add(match['clo'])
        same = match is not None and (norm(match['text']) == norm(r['text']) or best[0] >= 0.97)
        notes = []
        cat_lv = PI_LEVEL.get(r['pi'], '')
        if cat_lv and r['pi_level'] != cat_lv[:2]: notes.append(f"ระดับ PI ใน OBE3 ({r['pi_level']}) ไม่ตรงกับแคตตาล็อก ({cat_lv[:2]})")
        li = level_issue(cat_lv, r['clo_level'])
        if li: notes.append('CLO ' + li)
        if notes: FLAG[(c['code'], r['clo'])] = '; '.join(notes)
        # same wording -> keep the repo's clean text (PDF text has broken spacing / missing marks)
        c['clos'].append(dict(clo=r['clo'], text=match['text'] if same else r['text'], pos=['PO' + r['pi'].split('.')[0]],
                              pis=[r['pi']], src='OBE3', clo_level=r['clo_level'], target=r['target'],
                              repo_match=match, repo_same=same, anchor=(match['clo'].lower() if match else '')))

GROUPS = [('foundation','กลุ่มวิชาพื้นฐาน'),('core','กลุ่มวิชาบังคับ'),('cwie','กลุ่มเสริมสร้างประสบการณ์ในวิชาชีพ'),
          ('electives/ai','กลุ่มวิชาเลือก: AI'),('electives/hardware','กลุ่มวิชาเลือก: Hardware'),
          ('electives/network','กลุ่มวิชาเลือก: Network'),('electives/software','กลุ่มวิชาเลือก: Software')]
# ---- link helpers (descriptions read from the repo files so tooltips stay in sync) ----
PROS = open('CPE_RMUTT68_Prospectus.md', encoding='utf-8').read()
PLO_TXT = {n.replace('-', '.'): t.strip().strip('*') for n, t in
           re.findall(r'<a id="plo([\d-]+)"></a>\**PLO[\d.]+\** \| (.*?) \|', PROS)}
POM = open('CPE_RMUTT68_TABEE_PO_Mapping.md', encoding='utf-8').read()
PO_TXT = {int(n): t.strip() for n, t in re.findall(r'<a id="po(\d+)"></a>\*\*PO\d+\*\* \| (.*?) \|', POM)}
assert len(PLO_TXT) == 13 and set(PO_PLO.values()) <= set(PLO_TXT) and len(PO_TXT) == 11, (len(PLO_TXT), len(PO_TXT))
SK = {
 'SK1': ('Natural and Social Sciences', 'ความเข้าใจทฤษฎีด้านวิทยาศาสตร์ธรรมชาติอย่างเป็นระบบที่เหมาะสมกับสาขาและ/หรือแขนงของความชำนาญทางวิศวกรรม และการตระหนักถึงด้านสังคมศาสตร์ที่เกี่ยวข้อง', 'A systematic, theory-based understanding of the natural sciences applicable to the sub-discipline and awareness of relevant social sciences'),
 'SK2': ('Mathematics', 'แนวคิดทางคณิตศาสตร์ การวิเคราะห์เชิงตัวเลข การวิเคราะห์ข้อมูล สถิติ วิทยาการคอมพิวเตอร์และวิทยาการสารสนเทศ เพื่อสนับสนุนการพิจารณาอย่างละเอียด และการใช้แบบจำลองที่เหมาะสมกับสาขาและ/หรือแขนงของความชำนาญทางวิศวกรรม', 'Conceptually-based mathematics, numerical analysis, data analysis, statistics and formal aspects of computer and information science to support detailed consideration and use of models applicable to the sub-discipline'),
 'SK3': ('Engineering Fundamentals', 'ความรู้และทฤษฎีเชิงระบบในการวางหลักเกณฑ์พื้นฐานทางวิศวกรรมที่กำหนดในแต่ละสาขาและ/หรือแขนงของความชำนาญทางวิศวกรรม', 'A systematic, theory-based formulation of engineering fundamentals required in an accepted sub-discipline'),
 'SK4': ('Specialist Knowledge', 'กรอบทฤษฎีและองค์ความรู้เฉพาะทางวิศวกรรมในแต่ละสาขาและ/หรือแขนงของความชำนาญทางวิศวกรรม', 'Engineering specialist knowledge that provides theoretical frameworks and bodies of knowledge for an accepted sub-discipline'),
 'SK5': ('Engineering Design and Operations', 'ความรู้ที่สนับสนุนการออกแบบและการดำเนินงานทางวิศวกรรมโดยใช้เทคโนโลยีในการปฏิบัติวิชาชีพ ครอบคลุมถึงการใช้ทรัพยากรอย่างมีประสิทธิภาพ ผลกระทบต่อสิ่งแวดล้อม ต้นทุนตลอดวงจรชีวิต การนำทรัพยากรกลับมาใช้ใหม่ คาร์บอนสุทธิเป็นศูนย์ และแนวคิดอื่นที่เกี่ยวข้อง', 'Knowledge, including efficient resource use, environmental impacts, whole-life cost, re-use of resources, net zero carbon, and similar concepts, that supports engineering design and operations using the technologies of a practice area'),
 'SK6': ('Engineering Technologies', 'ความรู้เกี่ยวกับเทคโนโลยีทางวิศวกรรมที่เหมาะสมกับสาขาและ/หรือแขนงของความชำนาญทางวิศวกรรม', 'Knowledge of engineering technologies applicable in the sub-discipline'),
 'SK7': ('Role of Engineering in Society', 'ความรู้เกี่ยวกับบทบาทของเทคโนโลยีในสังคม และประเด็นที่เกี่ยวข้องกับการประยุกต์ใช้เทคโนโลยีวิศวกรรม เช่น ความปลอดภัยสาธารณะ และการพัฒนาอย่างยั่งยืน', 'Knowledge of the role of technology in society and identified issues in applying engineering technology, such as public safety and sustainable development'),
 'SK8': ('Technological Literature', 'การค้นคว้าทางเอกสารเกี่ยวกับเทคโนโลยีปัจจุบันของสาขาวิชา และตระหนักถึงความสำคัญของการคิดเชิงวิพากษ์', 'Engagement with the current technological literature of the discipline and awareness of the power of critical thinking'),
 'SK9': ('Ethics and Conduct', 'ความรู้เกี่ยวกับจรรยาบรรณวิชาชีพวิศวกรรม ความรับผิดชอบ และแนวทางการปฏิบัติที่ได้รับการยอมรับ ตระหนักถึงความหลากหลายตามชาติพันธุ์ เพศ อายุ ข้อจำกัดทางกายภาพ และปฏิบัติด้วยความเข้าใจ เคารพ และทัศนคติที่ก่อให้เกิดความมีส่วนร่วม', 'Ethics, inclusive behavior and conduct. Knowledge of professional ethics, responsibilities, and norms of engineering practice. Awareness of the need for diversity by reason of ethnicity, gender, age, physical ability etc. with mutual understanding and respect, and of inclusive attitudes'),
}
def tip(s): return s.replace('"', "'").replace('|', '/')
def pid(p): return 'pi' + p.replace('.', '-')
def lplo(n): return f'[PLO{n}](CPE_RMUTT68_Prospectus.md#plo{n.replace(".", "-")} "{tip(PLO_TXT[n])}")'
def lpo(n): return f'[PO{n}](CPE_RMUTT68_TABEE_PO_Mapping.md#po{n} "{tip(PO_TXT[n])}")'
def lpi(p): return f'[PI{p}](#{pid(p)} "{tip(PI_DESC[p][1])}")'
def lsk(s): return f'[{s}](#{s.lower()} "{tip(SK[s][0])}")'
def lclo(c, x):
    note = FLAG.get((c['code'], x['clo']))
    src = f" (OBE3, {x['clo_level']}, เกณฑ์ {x['target']}%)" if x.get('src') == 'OBE3' else ''
    t = f"{x['text']} [{', '.join(x['pos'])}]{src}" + (f' ⚑ {note}' if note else '')
    anchor = x['anchor'] if x.get('src') == 'OBE3' else x['clo'].lower()   # OBE3 CLO -> matched course-file CLO
    return f"[{x['clo']}]({c['file']}{'#' + anchor if anchor else ''} \"{tip(t)}\")"
def cell(c, pi):
    return ' '.join(lclo(c, x) + ('†' if len(x['pos']) > 1 else '') + ('⚑' if (c['code'], x['clo']) in FLAG else '')
                    for x in c['clos'] if pi in x['pis'])
REQ = [c for c in C if grp(c) in ('foundation', 'core')]
CW301 = [c for c in C if c['code'] == '04-000-301']
CWOPT = [c for c in C if grp(c) == 'cwie' and c['code'] != '04-000-301']
EL = [c for c in C if grp(c).startswith('electives')]
def has(c, p): return any(p in x['pis'] for x in c['clos'])
cov = {}
for p in PIS:
    po = int(p.split('.')[0]); need = 2 if po <= 3 else 1
    rc = [c['code'] for c in REQ + CW301 if has(c, p)]
    if all(has(c, p) for c in CWOPT): rc.append('CWIE (ทุกรูปแบบ)')
    cov[p] = dict(need=need, req=rc, el=sum(has(c, p) for c in EL))

L = []
A = L.append
A('# PO–PI–CLO Matrix | CPE RMUTT 2568 (TABEE, Sydney Accord)\n')
A('> [Prospectus](CPE_RMUTT68_Prospectus.md) · [PLO–CLO Matrix](CPE_RMUTT68_PLO_CLO_Matrix.md) · [TABEE PO Mapping](CPE_RMUTT68_TABEE_PO_Mapping.md) · [Course Index](Course_Index.md)\n')
A('> **สถานะ: ร่างเสนอ (Draft) รอคณะกรรมการหลักสูตรพิจารณา**')
A('> - **CLO → PO** นำมาจากตาราง PLO Mapping ในไฟล์รายวิชาแต่ละไฟล์ (ข้อมูลปัจจุบันของหลักสูตร)')
A('> - **CLO → PI** เป็นข้อเสนอที่กำหนดตามกฎในหัวข้อที่ 5 เพราะไฟล์รายวิชายังไม่ได้ระบุ PI')
A('> - รูปแบบตารางอ้างอิงตัวอย่าง "PO-PI-CLO Matrix" ของหลักสูตรวิศวกรรมอุตสาหการ (IE) และใช้แคตตาล็อก PI 23 ข้อจาก *LO Writing Manual TABEE PO-PI-CLO ENG RMUTT*\n')
A('**สัญลักษณ์**')
A('- `CLOn` คือ CLO ที่รายวิชาใช้ประเมิน PI นั้น')
A('- `†` คือ CLO เดียวรับผิดชอบหลาย PO ซึ่งขัดกฎ 1 CLO : 1 PI จึงควรแยก CLO')
A('- `⚑` คือ ถ้อยคำ CLO ไม่สอดคล้องกับ PO/PI ที่แมปไว้ (ดูหัวข้อที่ 4)\n')
A('**ลิงก์:** คลิก PLO / PO / PI / SK / CLO เพื่อเปิดคำอธิบาย หรือวางเมาส์ค้างไว้เพื่อดูคำอธิบายโดยย่อ (tooltip)\n')
A('---\n\n## 1. แคตตาล็อก PI และแบบความรู้ (SK)\n')
A('### 1.1 PI (23 ข้อ)\n')
A('| PI | TABEE PO | PLO | แบบความรู้ | ระดับ (Taxonomy) | ความหมายโดยย่อ |\n| --- | :---: | :---: | :---: | :---: | --- |')
for p in PIS:
    po = int(p.split('.')[0])
    sks = ', '.join(lsk(s.strip()) if s.strip().startswith('SK') else s for s in PI_DESC[p][0].split(','))
    A(f'| <a id="{pid(p)}"></a>**PI{p}** | {lpo(po)} | {lplo(PO_PLO[po])} | {sks} | {PI_LEVEL.get(p, '')} | {PI_DESC[p][1]} |')
A('\n> PI11.2 อยู่ภายใต้ **PO11** (ไฟล์ต้นแบบ `OBE3_TABEE.doc` พิมพ์ผิดเป็น "PO12")\n')
A('### 1.2 แบบความรู้ (Knowledge Profile) ตาม Sydney Accord\n')
A('ที่มา: IEA Graduate Attributes and Professional Competencies 2021 และ *LO Writing Manual TABEE PO-PI-CLO ENG RMUTT*\n')
A('| SK | หมวด | คำอธิบาย (ไทย) | Definition (IEA 2021) | PI ที่ใช้ |\n| --- | --- | --- | --- | --- |')
for s, (name, th, en) in SK.items():
    used = ', '.join(lpi(p) for p in PIS if s in PI_DESC[p][0].replace(' ', '').split(','))
    A(f'| <a id="{s.lower()}"></a>**{s}** | {name} | {th} | {en} | {used} |')
A('')
A('---\n\n## 2. ตาราง PO–PI–CLO\n')
hdr = ['| รายวิชา | ' + ' | '.join(lplo(PO_PLO[int(p.split(".")[0])]) for p in PIS) + ' |',
       '| --- | ' + ' | '.join(':---:' for _ in PIS) + ' |',
       '| **TABEE PO** | ' + ' | '.join(lpo(int(p.split(".")[0])) for p in PIS) + ' |',
       '| **PI** | ' + ' | '.join(f'[{p}](#{pid(p)} "{tip(PI_DESC[p][1])}")' for p in PIS) + ' |']
for g, label in GROUPS:
    cs = sorted([c for c in C if grp(c) == g], key=lambda c: c['code'])
    A(f'### {label}\n'); L.extend(hdr)
    for c in cs:
        A(f"| [{c['code']}]({c['file']}) {c['th']} {c['credits']}{' **(OBE3)**' if 'obe3' in c else ''} | " + ' | '.join(cell(c, p) for p in PIS) + ' |')
    A('')
A('---\n\n## 3. ความครอบคลุมของ PI เทียบกับเกณฑ์ TABEE\n')
A('**เกณฑ์ขั้นต่ำต่อ PI** (ศ.สมศักดิ์ และคู่มือ SER)')
A('- PO1–3: direct อย่างน้อย 2 ครั้ง และ indirect อย่างน้อย 1 ครั้ง')
A('- PO4–11: direct อย่างน้อย 1 ครั้ง และ indirect อย่างน้อย 2 ครั้ง')
A('- ต้องประเมินให้ครบทุก PI\n')
A('**วิธีนับ:** นับเฉพาะรายวิชาที่นักศึกษาทุกคนต้องเรียน คือกลุ่มพื้นฐาน กลุ่มบังคับ และ 04-000-301 ส่วนรูปแบบ CWIE จะนับก็ต่อเมื่อ *ทุกรูปแบบ* ครอบคลุม PI นั้น ไม่นับวิชาเลือก เพราะวิชาเลือกไม่ได้ประเมินนักศึกษาทุกคน\n')
A('| PI | ขั้นต่ำ direct | รายวิชาบังคับที่ครอบคลุม | จำนวน | วิชาเลือกที่ครอบคลุม | สถานะ |\n| --- | :---: | --- | :---: | :---: | :---: |')
for p in PIS:
    v = cov[p]; n = len(v['req']); st = '✅' if n >= v['need'] else ('⚠️' if n else '❌')
    A(f"| {lpi(p)} | {v['need']} | {', '.join(v['req']) or '—'} | {n} | {v['el']} | {st} |")
A('\n✅ ผ่านขั้นต่ำ · ⚠️ มีแต่ไม่ถึงขั้นต่ำ · ❌ ไม่มีรายวิชาบังคับรองรับ\n')
# ---- generated: OBE3 data vs repo course files ----
OC = [c for c in C if 'obe3' in c]
if OC:
    A('---\n\n## 3.1 ข้อมูลจาก OBE3-TABEE ที่อาจารย์กรอกแล้ว\n')
    A(f'รายวิชาที่มีไฟล์ OBE3 ใน `source_documents/` ({len(OC)} วิชา) ใช้ CLO และ PI ตามที่อาจารย์ผู้รับผิดชอบกำหนดใน OBE3 **แทนร่างเสนอ** '
      '(แถวที่มีป้าย **(OBE3)** ในตาราง) ข้อมูลถูกดึงด้วย `tools/extract_obe3.py` ไปเก็บที่ `tools/obe3_clo_pi.json`\n')
    for c in OC:
        o = c['obe3']
        A(f"### {c['code']} {c['th']}\n")
        A(f"ไฟล์: `{o['file']}`" + (f" · อาจารย์ผู้รับผิดชอบ: {o['lecturer']}" if o['lecturer'] else ''))
        if o.get('code_note'): A(f"\n> ⚠️ {o['code_note']}")
        A('\n| CLO (OBE3) | ผลลัพธ์การเรียนรู้ (OBE3) | PI | ระดับ CLO | เกณฑ์ | ในไฟล์รายวิชา: PO → PI ร่างเสนอ | ข้อสังเกต |\n'
          '| --- | --- | :---: | :---: | :---: | --- | --- |')
        for x in c['clos']:
            r = x['repo_match']
            if r:
                old = f"{r['clo']}: {', '.join(r['pos'])} → {', '.join(r['pis'])}" + ('' if x['repo_same'] else f" (ถ้อยคำต่างกัน: {r['text']})")
            else:
                old = '— (ไม่มี CLO ที่ตรงกันในไฟล์รายวิชา)'
            A(f"| {lclo(c, x)} | {x['text']} | {lpi(x['pis'][0])} | {x['clo_level']} | {x['target']}% | {old} | {FLAG.get((c['code'], x['clo']), '')} |")
        matched = {x['repo_match']['clo'] for x in c['clos'] if x['repo_match']}
        extra = [x for x in c['repo_clos'] if x['clo'] not in matched]
        if extra: A('\nCLO ในไฟล์รายวิชาที่ไม่มีใน OBE3: ' + '; '.join(f"{x['clo']} ({', '.join(x['pos'])}) {x['text']}" for x in extra))
        renum = any(x['repo_match'] and x['repo_match']['clo'] != x['clo'] for x in c['clos'])
        if renum: A('\n> ⚠️ ลำดับเลข CLO ใน OBE3 ไม่ตรงกับไฟล์รายวิชา')
        A('')
BYCODE = {c['code']: c for c in C}
LINK = re.compile(r'\[[^\]]*\]\([^ )]*(?: "[^"]*")?\)')
def linkify(s):
    # protect existing links (incl. tooltip text), then link CLO / PI / PO / SK / PLO mentions
    keep = []
    def stash(m): keep.append(m.group(0)); return f'\x00{len(keep)-1}\x00'
    s = LINK.sub(stash, s)
    def clo(m):
        c = BYCODE.get(m.group(1)); x = c and next((x for x in c['clos'] if x['clo'] == 'CLO' + m.group(3)), None)
        return m.group(0) if not x else m.group(1) + m.group(2) + stash_str(lclo(c, x))
    def stash_str(t): keep.append(t); return f'\x00{len(keep)-1}\x00'
    s = re.sub(r'(04-\d{3}-\d{3})( \| | )CLO(\d+)', clo, s)
    s = re.sub(r'^\| (\d+\.\d+) \|', lambda m: '| ' + stash_str(lpi(m.group(1))) + ' |' if m.group(1) in PIS else m.group(0), s, flags=re.M)
    s = re.sub(r'(?<![\w#\[/])PI(\d+\.\d+)', lambda m: stash_str(lpi(m.group(1))) if m.group(1) in PIS else m.group(0), s)
    s = re.sub(r'(?<![\w#\[/])PLO(\d+(?:\.\d+)?)\b', lambda m: stash_str(lplo(m.group(1))) if m.group(1) in PLO_TXT else m.group(0), s)
    s = re.sub(r'(?<![\w#\[/])PO(\d+)\b', lambda m: stash_str(lpo(int(m.group(1)))) if int(m.group(1)) in PO_TXT else m.group(0), s)
    s = re.sub(r'(?<![\w#\[/])SK(\d)\b', lambda m: stash_str(lsk('SK' + m.group(1))) if 'SK' + m.group(1) in SK else m.group(0), s)
    return re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], s))
if os.path.exists(SECTIONS):
    tail = open(SECTIONS, encoding='utf-8').read()
    out = []
    for line in tail.split('\n'):
        out.append(line if line.startswith('#') else linkify(line))
    L.append('\n'.join(out))
open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(f"Wrote {OUT}: {len(C)} courses, {sum(len(c['clos']) for c in C)} CLOs")
for p in PIS:
    v = cov[p]; print(f"PI{p}: required {len(v['req'])}/{v['need']}, electives {v['el']}")
