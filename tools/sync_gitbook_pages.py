"""Refresh GitBook's existing slugs from the authored textbook; preserve public URLs."""
from pathlib import Path
import re
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_NAMES = [
 '00-prerequisites-and-notation.md', '01-overview-tokenization.md',
 '02-pytorch-resource-accounting.md', '03-architectures.md',
 '04-linear-attention-moe.md', '05-gpu-flashattention.md',
 '06-kernels-triton.md', '07-distributed-primitives.md',
 '08-zero-hybrid-parallelism.md', '09-scaling-laws.md', '10-inference.md',
 '11-scaling-practice.md', '12-evaluation.md', '13-data-sources.md',
 '14-data-processing.md', '15-sft-rlhf-dpo.md', '16-rlvr-grpo.md',
 '17-multimodality.md', '18-daniel-selsam-material-gap.md',
 '19-dan-fu-inference-codesign.md',
]

def main():
    book = ROOT / 'textbook'
    mapping = {(book/'README.md').resolve(): book/'README.md',
               (book/CHAPTER_NAMES[0]).resolve(): book/CHAPTER_NAMES[0]}
    for n in list(range(1,18))+[18,19]:
        source = book / CHAPTER_NAMES[n]
        candidates = list(book.glob(f'{n+1:02d}-l{n:02d}*.md'))
        if len(candidates) != 1:
            raise ValueError((source, candidates))
        mapping[source.resolve()] = candidates[0]
    extras = [
      ('sources/textbook-evidence.md','21-'), ('sources/README.md','22-'),
      ('sources/transcripts.md','23-'), ('sources/spring2025-reference.md','24-'),
      ('study-plan.md','25-'), ('assignments/README.md','26-'),
      ('labs/README.md','27-'), ('templates/experiment-log.md','28-'),
      ('templates/lecture-note.md','29-'),
    ]
    for source,prefix in extras:
        candidates=[p for p in book.glob(prefix+'*.md') if p.name not in CHAPTER_NAMES]
        if len(candidates)!=1:raise ValueError((source,candidates))
        mapping[(ROOT/source).resolve()] = candidates[0]
    mapping[(ROOT/'sources/transcript-audit.md').resolve()] = book/'30-transcript-audit.md'
    mapping[(ROOT/'sources/three-way-audit.md').resolve()] = book/'31-three-way-audit.md'
    audit_files=sorted((ROOT/'sources/three-way').glob('*.md'))
    for i,source in enumerate(audit_files,32):
        mapping[source.resolve()]=book/f'{i:02}-{source.stem}.md'
    # Read all source files before writing, including the two in-place pages.
    texts={p:p.read_text() for p in mapping}
    texts[(book/'README.md').resolve()] = (book/'index.md').read_text()
    homepage = None
    for source,target in mapping.items():
        def rewrite(m):
            link=m[1]
            if '://' in link or link.startswith('#'):return m[0]
            raw,sep,anchor=link.partition('#')
            path=(source.parent/unquote(raw)).resolve()
            if not path.exists():raise ValueError((source,link))
            if path in mapping:
                dest=quote(mapping[path].name)
            else:
                dest='https://github.com/thorlay/hi-cs336/blob/main/'+quote(path.relative_to(ROOT).as_posix())
            return ']('+dest+(sep+anchor if sep else '')+')'
        rendered=re.sub(r'\]\(([^)]+)\)',rewrite,texts[source])
        if target!=source or target.name=='README.md':target.write_text(rendered.rstrip()+'\n')
        if target.name=='README.md':homepage=rendered
    # Keep the old index URL usable while making the real homepage the index.
    legacy=list(book.glob('00-cs336-spring-2026-*.md'))
    for p in legacy:p.write_text(homepage.rstrip()+'\n')
    entries=[]
    for source,target in mapping.items():
        title=texts[source].splitlines()[0].removeprefix('# ').strip()
        entries.append(f'* [{title}]({target.name})')
    (book/'SUMMARY.md').write_text('# 阅读目录\n\n'+'\n'.join(entries)+'\n')
    print(f'Updated {len(mapping)} GitBook pages; chapter order corrected.')

if __name__=='__main__':main()
