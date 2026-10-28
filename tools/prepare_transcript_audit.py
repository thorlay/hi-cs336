"""Preserve timed subtitle lines AND untimed continuation lines for a review pass.
Outputs contain user-provided source text and stay in the ignored outputs directory.
This prepares evidence; it does not certify semantic coverage.
"""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]

def parse(text):
    records=[]
    stamp=None
    for line in text.splitlines():
        line=line.strip()
        if not line:continue
        m=re.match(r'^(\d+:\d+(?::\d+)?)(?:\s+(.*))?$',line)
        if m:
            stamp=m[1]
            if m[2]:records.append({'time':stamp,'text':m[2]})
        else:
            if stamp is None:raise ValueError('Untimed text before the first timestamp')
            if records and records[-1]['time']==stamp:records[-1]['text']+=' '+line
            else:records.append({'time':stamp,'text':line})
    return records

def main():
    out=ROOT/'outputs'/'transcript-audit-full';out.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for p in sorted((ROOT/'sources/raw/transcripts-spring2026').glob('*.txt')):
        raw=p.read_text();records=parse(raw)
        continuations=sum(bool(l.strip()) and not re.match(r'^\d+:\d+(?::\d+)?(?:\s|$)',l.strip()) for l in raw.splitlines())
        # Validate preservation against every source text line, including continuations.
        expected=[]
        for line in raw.splitlines():
            line=line.strip()
            if not line:continue
            expected.append(re.sub(r'^\d+:\d+(?::\d+)?(?:\s+|$)','',line).strip())
        assert ' '.join(' '.join(expected).split())==' '.join(' '.join(r['text'] for r in records).split()),p
        (out/p.name).write_text('\n'.join(f"{r['time']} {r['text']}" for r in records)+'\n')
        manifest.append({'file':p.name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'untimed_continuation_lines':continuations,'source_text_preserved':True,'semantic_review_complete':continuations==0})
    # Review status belongs in the human-authored report, not a parser inference.
    for item in manifest:item.pop('semantic_review_complete')
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Prepared {len(manifest)} full transcripts; retained {sum(x["untimed_continuation_lines"] for x in manifest)} untimed continuation lines.')
if __name__=='__main__':main()
