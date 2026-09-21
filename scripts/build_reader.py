"""Build a portable, offline reading edition from source Markdown and data."""
from pathlib import Path
import base64
import html
import json
import re
import os
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'


def render(path, prefix):
    source = path.read_text()
    content = markdown.markdown(source, extensions=['tables', 'fenced_code', 'footnotes'])
    def local_link(match):
        target = match.group(1)
        if target.startswith('/read/'):
            entries = json.loads((ROOT / 'research/reading-order.json').read_text())['chapters']
            slug = target.removeprefix('/read/').strip('/')
            for index, entry in enumerate(entries):
                if entry['slug'] == slug:
                    return f'href="#chapter-{index}"'
        if target.startswith('/research/'):
            return 'href="' + html.escape(os.path.relpath(ROOT / target.lstrip('/'), OUT)) + '"'
        if target.startswith(('https:', 'http:', '#', 'mailto:', '/')):
            return match.group(0)
        destination = path.parent / target
        return 'href="' + html.escape(os.path.relpath(destination, OUT)) + '"'
    content = re.sub(r'href="([^"]+)"', local_link, content)
    # Scope footnote IDs across separately rendered documents.
    content = content.replace('id="fn', f'id="{prefix}-fn').replace('href="#fn', f'href="#{prefix}-fn')
    content = re.sub(r'<table>(.*?)</table>', r'<div class="table-wrap"><table>\1</table></div>', content, flags=re.S)
    if path.name == 'pilot-report.md':
        encoded = base64.b64encode((ROOT / 'analysis/length-overview.svg').read_bytes()).decode()
        content = content.replace('src="length-overview.svg"', 'src="data:image/svg+xml;base64,' + encoded + '"')
    return f'<article id="{prefix}" class="prose">{content}</article>'


def main():
    OUT.mkdir(exist_ok=True)
    edition = json.loads((ROOT / 'research/reading-order.json').read_text())
    chapters = [ROOT / entry['file'] for entry in edition['chapters']]
    book = ''.join(render(p, 'chapter-' + str(i)) for i, p in enumerate(chapters))
    research_files = ['edition-0.2.md', 'source-dossier.md', 'charter.md', 'book-map.md', 'methods-and-studies.md']
    research = ''.join(render(ROOT / 'research' / name, 'research-' + str(i)) for i, name in enumerate(research_files))
    pilot = render(ROOT / 'analysis/pilot-report.md', 'pilot')
    catalog = json.loads((ROOT / 'research/source-catalog.json').read_text())
    summary = json.loads((ROOT / 'analysis/summary.json').read_text())
    import csv
    with (ROOT / 'analysis/surah-summary.csv').open() as f:
        surahs = list(csv.DictReader(f))
    evidence = []
    for filename in sorted(p.name for p in (ROOT / 'research').glob('sources-*.json')):
        doc = json.loads((ROOT / 'research' / filename).read_text())
        evidence.extend(doc['sources'])
    ledger = json.loads((ROOT / 'research/claim-ledger.json').read_text())
    words = sum(len(p.read_text().split()) for p in chapters)
    data = json.dumps({'catalog': catalog, 'summary': summary, 'surahs': surahs, 'evidence': evidence, 'claims': ledger}, ensure_ascii=False).replace('</', '<\\/')
    css = (ROOT / 'scripts/reader.css').read_text()
    js = (ROOT / 'scripts/reader.js').read_text()
    nav = ''.join(f'<a href="#chapter-{i}">{html.escape(p.read_text().splitlines()[0].lstrip("# "))}</a>' for i,p in enumerate(chapters))
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Qur’an Examined | Expanded research edition</title><style>{css}</style></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="cover"><div class="eyebrow">THE QUR’AN EXAMINED · RESEARCH EDITION 02</div><h1>Begin with<br>the language.</h1><p class="deck">Language, meaning, and the case for revelation.<br>An invitation to inspect the evidence.</p><div class="cover-meta">20 September 2026 <span>•</span> Working manuscript <span>•</span> Local reading edition</div></header>
<nav class="tabs" aria-label="Reading sections"><button data-panel="book" aria-current="page">Read the manuscript</button><button data-panel="dossier">Research dossier</button><button data-panel="lab">Explore the data</button><button data-panel="sources">Sources & claims</button></nav>
<main id="main"><section id="book" class="panel"><div class="intro-grid"><div><p class="eyebrow">EXPANDED MANUSCRIPT</p><h2>Read closely.<br>Follow the argument.</h2><p>An opening essay and {len(chapters)-1} chapters, approximately {words:,} words including notes. The chapters separate textual observation, interpretation, evaluation, and the further question of origin.</p></div><aside><strong>What is ready</strong><p>Source-linked drafts, an initial bibliography, and a reproducible corpus inventory.</p><strong>What remains</strong><p>Independent Arabic review, stronger comparative evidence, original reader studies, and the full manuscripts.</p></aside></div><div class="chapter-links">{nav}</div>{book}</section>
<section id="dossier" class="panel" hidden><div class="section-head"><p class="eyebrow">RESEARCH PROGRAM</p><h2>Evidence before conclusions.</h2><p>Source coverage, editorial architecture, and proposed studies. Protocol drafts are not completed experiments.</p></div>{research}</section>
<section id="lab" class="panel" hidden><div class="section-head"><p class="eyebrow">REPRODUCIBLE DESCRIPTIVE PILOT</p><h2>Count precisely.<br>Interpret carefully.</h2><p>This is one pinned representation of the Ḥafṣ reading. None of the measurements below is a score of beauty or divinity.</p></div><div class="stats"><div><strong>{summary['surahs']}</strong><span>surahs</span></div><div><strong>{summary['verses']:,}</strong><span>numbered verses</span></div><div><strong>{summary['orthographic_tokens']:,}</strong><span>defined written tokens</span></div></div><div class="explorer"><label for="surah-select">Inspect a surah</label><select id="surah-select"></select><div id="surah-details" aria-live="polite"></div><p class="small">Written tokens retain attached clitics. Unnumbered opening basmalas and stand-alone recitation signs are excluded. A count is not a measure of semantic richness.</p></div>{pilot}</section>
<section id="sources" class="panel" hidden><div class="section-head"><p class="eyebrow">SOURCE TRANSPARENCY</p><h2>Know what has been read.</h2><p>The bibliography includes inspected passages, verified catalogue records, and unverified research leads. These are different levels of coverage, not equal votes for a conclusion.</p></div><div class="filters"><label>Search the bibliography<input id="source-search" type="search" placeholder="Author, title, or research domain"></label><label>Verification status<select id="status-filter"><option value="all">All records</option><option value="passage_inspected">Passage inspected</option><option value="catalog_confirmed">Catalogue confirmed</option><option value="discovery_lead">Discovery lead</option></select></label></div><p id="source-count" aria-live="polite"></p><div id="source-list"></div><h2>Chapter evidence records</h2><p>These may overlap with the bibliography. Do not add the record counts as if they were unique independent sources.</p><div id="evidence-list"></div><h2>Initial claim ledger</h2><p>These are bounded claims, proposed tests, and unresolved inferences. A linked source supports only the inspected scope recorded with it.</p><div id="claim-list"></div></section></main>
<footer>Research edition 0.2 · No human studies conducted · No comparative superiority established in this release<br>Corpus attribution: <a href="https://tanzil.net/">Tanzil Project</a>. The original file and its full notice are preserved in the source package.</footer>
<script type="application/json" id="research-data">{data}</script><script>{js}</script></body></html>'''
    (OUT / 'The_Quran_Examined_Research_Edition.html').write_text(doc)
    manuscript = '# The Qur’an Examined\n\n## Expanded research edition 0.2\n\n20 September 2026. Draft for review.\n\n' + '\n\n---\n\n'.join(p.read_text() for p in chapters)
    manuscript = manuscript.replace('](/read/', '](https://inimitable-quran-project.workspace-114686.chatgpt.site/read/').replace('](/research/', '](https://inimitable-quran-project.workspace-114686.chatgpt.site/research/')
    (OUT / 'The_Quran_Examined_Manuscript.md').write_text(manuscript)
    print(json.dumps({'html': str(OUT / 'The_Quran_Examined_Research_Edition.html'), 'manuscript_words_including_notes': words, 'bibliography_records': len(catalog['sources']), 'chapter_source_records': len(evidence)}, indent=2))


if __name__ == '__main__':
    main()
