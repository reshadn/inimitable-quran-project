"""Keep the downloadable bibliography consistent with the scoped source catalog."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    catalog = json.loads((ROOT / 'research/source-catalog.json').read_text())
    entries = []
    for source in catalog['sources']:
        fields = []
        for name in ['author', 'title', 'editor', 'year', 'publisher', 'edition', 'journal', 'booktitle', 'volume', 'number', 'pages', 'doi', 'url']:
            value = source.get(name)
            if value is not None:
                value = str(value).replace('\n', ' ')
                if name == 'author': value = value.replace('; ', ' and ')
                fields.append(f'  {name} = {{{value}}}')
        note = source['status'].replace('_', ' ') + '; ' + source['limitations']
        fields.append(f'  note = {{{note}}}')
        entries.append('@' + source.get('type', 'misc') + '{' + source['id'] + ',\n' + ',\n'.join(fields) + '\n}')
    (ROOT / 'research/bibliography.bib').write_text('\n\n'.join(entries) + '\n')

if __name__ == '__main__': main()
