"""Build a GitBook import archive with readable page names; exclude source transcripts/PDFs."""
from pathlib import Path
import re
import zipfile
from urllib.parse import quote, unquote
from sync_gitbook_pages import CHAPTER_NAMES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs' / 'cs336-gitbook-textbook.zip'

def main():
    files = [ROOT / 'textbook' / 'index.md']
    files += [ROOT / 'textbook' / name for name in CHAPTER_NAMES]
    files += [ROOT / p for p in [
        'sources/textbook-evidence.md', 'sources/README.md',
        'sources/transcripts.md', 'sources/spring2025-reference.md',
        'study-plan.md', 'assignments/README.md', 'labs/README.md',
        'templates/experiment-log.md', 'templates/lecture-note.md',
        'sources/transcript-audit.md',
    ]]
    names = {}
    for i, path in enumerate(files):
        title = path.read_text().splitlines()[0].removeprefix('# ').strip()
        title = re.sub(r'[\\/:*?"<>|]', ' ', title)
        names[path.resolve()] = f'{i:02d} {title}.md'
    names[(ROOT / 'textbook' / 'README.md').resolve()] = names[(ROOT / 'textbook' / 'index.md').resolve()]
    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            text = path.read_text()
            def rewrite(match):
                target = match[1]
                if '://' in target or target.startswith('#'):
                    return match[0]
                raw, sep, anchor = target.partition('#')
                resolved = (path.parent / unquote(raw)).resolve()
                if not resolved.exists():
                    raise ValueError(f'Broken link in {path}: {target}')
                if resolved in names:
                    dest = quote(names[resolved])
                else:
                    dest = 'https://github.com/thorlay/cs336/blob/main/' + quote(resolved.relative_to(ROOT).as_posix())
                return '](' + dest + (sep + anchor if sep else '') + ')'
            text = re.sub(r'\]\(([^)]+)\)', rewrite, text)
            archive.writestr(names[path.resolve()], text)
    print(f'{OUT} ({len(files)} pages)')

if __name__ == '__main__':
    main()
