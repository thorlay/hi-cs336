"""Translate GitHub heading fragments to IDs observed on published GitBook pages."""
import json
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PAGES = json.loads((Path(__file__).parent / 'gitbook-heading-anchors.json').read_text())['pages']


@lru_cache(maxsize=None)
def headings(path):
    return {line.lstrip('#').strip() for line in path.read_text().splitlines()
            if line.startswith('#')}


def published_anchor(path, anchor):
    if not anchor:
        return anchor
    key = path.resolve().relative_to(ROOT).as_posix()
    if key not in PAGES:
        return anchor
    records = PAGES[key]
    fragment = unquote(anchor)
    if fragment not in records:
        raise ValueError(f'GitBook heading ID needs verification: {key}#{fragment}')
    record = records[fragment]
    if record['heading'] not in headings(path):
        raise ValueError(f'Stale GitBook heading mapping: {key}#{fragment}')
    return record['id']
