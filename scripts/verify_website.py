"""Validate public files and core browser behavior before release."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json
import os
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
BASE = os.environ.get('SITE_TEST_URL', 'http://127.0.0.1:8747').rstrip('/')

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls = []
    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key,value in attrs if key in ('href','src') and value)

def main():
    failures=[]
    for source in DIST.rglob('*.html'):
        parser=Links(); parser.feed(source.read_text())
        for target in parser.urls:
            url=urlparse(target)
            if url.scheme or url.netloc or not url.path: continue
            dest=(DIST / unquote(url.path.lstrip('/'))) if url.path.startswith('/') else (source.parent / unquote(url.path))
            if dest.is_dir(): dest=dest/'index.html'
            if not dest.exists(): failures.append(f'{source.relative_to(DIST)} -> {target}')
    assert not failures, failures
    meta=json.loads((DIST/'audio/metadata.json').read_text())
    edition=json.loads((ROOT/'research/reading-order.json').read_text())
    catalog=json.loads((ROOT/'research/source-catalog.json').read_text())
    assert len(list((DIST/'audio').glob('*.m4a')))==len(meta['chapters'])
    assert {c['slug'] for c in meta['chapters']}=={c['slug'] for c in edition['chapters']}, 'Every published chapter needs its promised narration'
    assert 'Samantha' not in json.dumps(meta), 'Private voice metadata must not be published'
    routes=['/','/read/','/listen/','/project/','/contribute/','/licenses/','/research/'] + ['/read/'+c['slug']+'/' for c in edition['chapters']]
    errors=[]
    with sync_playwright() as p:
        browser=p.chromium.launch()
        for width,height in [(1440,1000),(390,844)]:
            page=browser.new_page(viewport={'width':width,'height':height})
            page.on('pageerror',lambda error:errors.append(str(error)))
            for route in routes:
                result=page.goto(BASE+route)
                assert result.status==200,(route,result.status)
                assert page.locator('h1').count()>=1,route
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),route
            page.goto(BASE+'/listen/#chapter-2')
            audio=page.locator('#audio')
            page.wait_for_function('document.querySelector("audio").readyState >= 1')
            assert 'The Head Ablaze' in page.locator('#track-title').inner_text()
            assert audio.evaluate('(a)=>a.duration')>100
            page.locator('#speed').select_option('1.3')
            assert audio.evaluate('(a)=>a.playbackRate')==1.3
            page.locator('.track[data-slug="02-time-and-mutual-responsibility"]').click()
            page.wait_for_function('document.querySelector("audio").currentTime > 0')
            assert 'Time and Mutual' in page.locator('#track-title').inner_text()
            audio.evaluate('(a)=>a.currentTime=600')
            page.wait_for_function('document.querySelector("audio").currentTime > 600.2 && !document.querySelector("audio").seeking',timeout=25000)
            audio.evaluate('(a)=>a.pause()')
            page.goto(BASE+'/listen/#06-counting-without-overclaiming')
            page.wait_for_function('document.querySelector("audio").readyState >= 1')
            assert 'Counting Without Overclaiming' in page.locator('#track-title').inner_text()
            page.locator('.track[data-slug="06-counting-without-overclaiming"]').click()
            page.wait_for_function('document.querySelector("audio").currentTime > 0')
            audio.evaluate('(a)=>a.currentTime=180')
            page.wait_for_function('document.querySelector("audio").currentTime > 180.2 && !document.querySelector("audio").seeking',timeout=25000)
            audio.evaluate('(a)=>a.pause()')
            page.goto(BASE+'/research/')
            page.locator('[data-panel="sources"]').click()
            page.locator('#status-filter').select_option('discovery_lead')
            assert page.locator('#source-list .source-card').count()==catalog['counts']['discovery_lead']
            assert page.locator('#evidence-list .source-card').count()==38
            page.locator('[data-panel="lab"]').click()
            page.locator('#surah-select').select_option('103')
            assert '14' in page.locator('#surah-details').inner_text()
            page.close()
        browser.close()
    assert not errors,errors
    print(json.dumps({'routes':len(routes),'viewports':[1440,390],'local_links':'passed','audio_load_and_playback':'passed','source_filter_and_surah_selector':'passed','script_errors':errors},indent=2))

if __name__=='__main__': main()
