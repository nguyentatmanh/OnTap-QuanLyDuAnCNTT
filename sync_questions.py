"""Validate the editable bank and embed it in the standalone application."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
bank = json.loads((ROOT / 'questions.json').read_text(encoding='utf-8'))
assert isinstance(bank, list) and bank, 'Question bank must be a nonempty array.'
ids = [q['id'] for q in bank]
assert all(isinstance(i, int) and i > 0 for i in ids), 'IDs must be positive integers.'
assert len(set(ids)) == len(ids), 'Duplicate question IDs.'
for q in bank:
    assert q['topic'] in {'SPM', 'SCRUM', 'UML'}, q['id']
    assert q['status'] in {'supported', 'conditional', 'missing'}, q['id']
    assert [o['letter'] for o in q['options']] == list('ABCD'), q['id']
    assert all(o['text'].strip() for o in q['options']), q['id']
    if q['status'] == 'supported':
        assert q['key'] in 'ABCD' and len(q['key']) == 1, q['id']
    elif q['status'] == 'conditional':
        assert q['key'] in {'A*', 'B*', 'C*', 'D*'}, q['id']
    else:
        assert q['key'] == '—', q['id']
    for field in ['question', 'answer', 'explain', 'eliminate', 'note']:
        assert isinstance(q[field], str) and q[field].strip(), (q['id'], field)
    assert q['sources'], q['id']
    for source in q['sources']:
        assert isinstance(source['text'], str) and source['text'], q['id']
        href = source.get('href')
        assert href is None or href.startswith(('https://', 'tai-lieu/')), (q['id'], href)

html_path = ROOT / 'index.html'
html = html_path.read_text(encoding='utf-8')
pattern = r'(<script type="application/json" id="question-bank">)[\s\S]*?(</script>)'
encoded = json.dumps(bank, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html, count = re.subn(pattern, lambda m: m[1] + encoded + m[2], html)
assert count == 1, 'Could not find exactly one embedded bank.'
html_path.write_text(html, encoding='utf-8')
print(f'Validated and embedded {len(bank)} questions.')
