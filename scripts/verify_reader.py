"""Check real reader interactions, local links, and narrow viewport layout."""
from pathlib import Path
import json
from urllib.parse import urlparse, unquote
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / 'outputs/The_Quran_Examined_Research_Edition.html'
QA = ROOT / 'outputs/qa'
QA.mkdir(exist_ok=True)
results = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    for width, height, label in [(1440, 1000, 'desktop'), (390, 844, 'mobile')]:
        page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=1)
        page.emulate_media(reduced_motion='reduce')
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.goto(FILE.as_uri())
        page.screenshot(path=str(QA / f'{label}-cover.png'))
        assert page.locator('#book').is_visible()
        page.locator('a[href="#chapter-1"]').click()
        page.screenshot(path=str(QA / f'{label}-chapter.png'))
        for panel in ['dossier', 'lab', 'sources', 'book']:
            page.locator(f'button[data-panel="{panel}"]').click()
            assert page.locator('#'+panel).is_visible()
            overflow = page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1')
            assert not overflow, f'{label}/{panel}: document overflow'
            if panel == 'lab':
                page.select_option('#surah-select', '19')
                assert '98 verses' in page.locator('#surah-details').inner_text()
                page.select_option('#surah-select', '103')
                assert '14 written tokens' in page.locator('#surah-details').inner_text()
                page.screenshot(path=str(QA / f'{label}-lab.png'))
            if panel == 'sources':
                assert page.locator('#source-list .source-card').count() == 65
                page.select_option('#status-filter', 'passage_inspected')
                assert page.locator('#source-list .source-card').count() == 9
                page.locator('#source-search').fill('Jurj')
                assert page.locator('#source-list .source-card').count() == 1
                page.locator('#source-search').fill('no-source-matches-this')
                assert page.locator('#source-list .source-card').count() == 0
                page.locator('#source-search').fill('')
                page.select_option('#status-filter', 'all')
                assert page.locator('#evidence-list .source-card').count() == 12
                assert page.locator('#claim-list .claim-card').count() == 18
                assert 'undefined' not in page.locator('#sources').inner_text()
                page.screenshot(path=str(QA / f'{label}-sources.png'))
        broken = []
        for href in page.locator('a[href]').evaluate_all('(els)=>els.map(e=>e.href)'):
            u=urlparse(href)
            if u.scheme=='file' and not Path(unquote(u.path)).exists():
                broken.append(href)
        assert not broken, broken
        assert not errors, errors
        results.append({'viewport': label, 'width': width, 'height': height,
                        'panels': 'all four pass', 'source_filters': 'pass', 'surah_selector': 'pass',
                        'document_overflow': False, 'broken_local_links': broken, 'runtime_errors': errors})
        page.close()
    browser.close()
(QA / 'reader-checks.json').write_text(json.dumps(results, indent=2)+'\n')
print(json.dumps(results, indent=2))
