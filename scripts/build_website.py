"""Build the public, static reading edition. Run from the repository root."""
from pathlib import Path
import html
import json
import re
import shutil
import subprocess
import sys
import zipfile
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
BASE = 'https://inimitable-quran-project.workspace-114686.chatgpt.site'
REPO = 'https://github.com/reshadn/inimitable-quran-project'
NAV = [('Read', '/read/'), ('Listen', '/listen/'), ('Project', '/project/'), ('Contribute', '/contribute/'), ('Research', '/research/')]

def nav(active=''):
    return '<header><div class="header-inner"><a class="brand" href="/">Inimitable Qur’an Project<small>An open inquiry into language & revelation</small></a><nav class="nav" aria-label="Main navigation">' + ''.join(f'<a href="{url}"' + (' aria-current="page"' if label == active else '') + f'>{label}</a>' for label, url in NAV) + '</nav></div></header>'

def page(path, title, body, active='', extra=''):
    destination = OUT / path.strip('/') / 'index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    canonical = BASE + '/' + (path.strip('/') + '/' if path.strip('/') else '')
    destination.write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#173c34"><title>{html.escape(title)} | Inimitable Qur’an Project</title><meta name="description" content="Read the developing book, listen to English narration, inspect the sources, and contribute to an open investigation of Qur’anic language and inimitability."><link rel="canonical" href="{canonical}"><link rel="stylesheet" href="/assets/site.css"></head><body><a class="skip" href="#main">Skip to content</a>{nav(active)}<main id="main">{body}</main><footer><p>Public research draft 0.1 · 20 September 2026<br>AI-assisted initial manuscript. Independent human scholarly review pending.<br>Original project prose: CC BY 4.0. Code: MIT. Third-party material retains its own terms.</p><div class="footer-links"><a href="{REPO}">Source repository</a><a href="/contribute/">Contribute</a><a href="/licenses/">Licenses</a></div></footer>{extra}</body></html>''')

def render(path):
    content = markdown.markdown(path.read_text(), extensions=['tables', 'fenced_code', 'footnotes'])
    def rewrite(match):
        target = match.group(1)
        if target.startswith(('https:', 'http:', '#', '/', 'mailto:')):
            return match.group(0)
        local = (path.parent / target).resolve()
        try:
            return 'href="/' + html.escape(str(local.relative_to(ROOT))) + '"'
        except ValueError:
            raise ValueError(f'Link outside source tree: {target}')
    content = re.sub(r'href="([^"]+)"', rewrite, content)
    return re.sub(r'<table>(.*?)</table>', r'<div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable table"><table>\1</table></div>', content, flags=re.S)

def main():
    OUT.mkdir(exist_ok=True)
    for directory in ['assets', 'audio', 'research', 'analysis', 'data', 'chapters']:
        shutil.copytree(ROOT / directory, OUT / directory, dirs_exist_ok=True, ignore=shutil.ignore_patterns('__pycache__', '*.aiff', '*.pyc'))
    meta = json.loads((ROOT / 'audio/metadata.json').read_text())
    tracks = meta['chapters']
    chapters = sorted((ROOT / 'chapters').glob('*.md'))
    descriptions = ['An invitation to inspect the language before deciding what its origin might be.', 'Grammar, metaphor, and prayer in Qur’an 19:4, read alongside al-Jurjānī.', 'The oath, warning, exception, and mutual counsel in the complete surah al-ʿAṣr.']
    cards = '<div class="cards">' + ''.join(f'''<article class="card"><p class="eyebrow">{'Opening essay' if i == 0 else 'Sample chapter ' + str(i)}</p><h3>{html.escape(t['title'])}</h3><p>{descriptions[i]}</p><div class="meta">{t['duration_label']} audio · Working draft</div><div class="card-links"><a href="/read/{t['slug']}/">Read the chapter →</a><a href="/listen/#chapter-{i+1}">Listen</a></div></article>''' for i,t in enumerate(tracks)) + '</div>'
    notice = '<p class="notice">This is the first manuscript package: an opening essay and two sample chapters, approximately 6,000 words. The full book and proposed studies are still in development. Independent scholarly review is pending.</p>'
    page('', 'Read, listen, and examine the evidence', f'''<section class="hero"><p class="eyebrow">The Qur’an Examined · A book being written in public</p><h1>Begin with the language.</h1><p class="lead">What does the Qur’an accomplish with words? What would a fair comparison require? And what does the evidence tell us about its claim to revelation?</p><div class="actions"><a class="button" href="/read/">Read the book</a><a class="button secondary" href="/listen/">Listen on your phone</a></div>{notice}</section><section aria-label="Available chapters">{cards}</section><section class="two-col"><div><p class="eyebrow">Open research</p><h2>An argument you can inspect.</h2><p>Read Arabic alongside working translations. Follow the sources. Separate what the text does from judgments about excellence and the further inference to revelation.</p><a href="/research/">Explore the sources and data →</a></div><div><p class="eyebrow">Community review</p><h2>Help make the case stronger.</h2><p>Corrections, strong counterarguments, Arabic analysis, and reproducible methods are welcome. Agreement with the conclusion is not a condition of contributing.</p><a href="/project/">About the open-source project →</a></div></section>''')
    page('read', 'Read the book', f'<section class="hero"><p class="eyebrow">The reading edition</p><h1>The Qur’an Examined</h1><p class="lead">Language, meaning, and the case for revelation.</p>{notice}<div class="actions"><a class="button" href="/read/{tracks[0]["slug"]}/">Start reading</a><a class="button secondary" href="/downloads/The_Quran_Examined_Manuscript.md" download>Download manuscript</a></div></section>{cards}<section class="two-col"><div><h2>The book ahead</h2><p>The planned flagship moves from individual expressions to complete compositions, fair comparisons, historical evidence, and the case for revelation.</p><a href="/research/book-map.md">Read the proposed book map</a></div><div><h2>Review a chapter</h2><p>Bring a correction, a competing reading, or a better source. Each accepted change will remain traceable in the repository.</p><a href="/contribute/">How to contribute</a></div></section>', 'Read')
    for i,(source, track) in enumerate(zip(chapters,tracks)):
        previous = f'<a href="/read/{tracks[i-1]["slug"]}/">← Previous chapter</a>' if i else '<a href="/read/">← Contents</a>'
        following = f'<a href="/read/{tracks[i+1]["slug"]}/">Next chapter →</a>' if i+1<len(tracks) else '<a href="/contribute/">Discuss this draft →</a>'
        page('read/'+track['slug'], track['title'], f'<div class="reading-tools"><a href="/read/">Contents</a><a href="/listen/#chapter-{i+1}">Listen · {track["duration_label"]}</a><a href="{REPO}/issues/new?template=review.yml">Suggest a correction</a></div><article class="prose">{render(source)}</article><nav class="chapter-nav" aria-label="Chapter navigation">{previous}{following}</nav>', 'Read')
    playlist = '<ol class="playlist">' + ''.join(f'<li><button class="track" type="button" aria-current="{str(i==0).lower()}"><span>{html.escape(t["title"])}<small>{"Opening essay" if i==0 else "Sample chapter " + str(i)}</small></span><span class="duration">{t["duration_label"]}</span></button></li>' for i,t in enumerate(tracks)) + '</ol>'
    page('listen', 'Listen on your phone', f'''<section class="hero"><p class="eyebrow">The audio edition</p><h1>Take the inquiry with you.</h1><p class="lead">Listen to the opening essay and two sample chapters. Choose a chapter, then press play.</p><p class="small">Synthetic English narration of the draft. This is not Qur’anic recitation. Arabic quotations and detailed citations are available in the reading edition. Transcripts adapt tables for speech. Pronunciations have not had a human listening review.</p></section><section class="player" aria-label="Chapter audio player"><p class="eyebrow" id="track-number">1 / 3</p><h2 id="track-title">{tracks[0]['title']}</h2><audio id="audio" controls preload="metadata" src="/audio/{tracks[0]['filename']}"><a href="/audio/{tracks[0]['filename']}">Download audio</a></audio><div class="player-options"><label for="speed">Speed <select id="speed"><option value="0.85">0.85×</option><option value="1" selected>1×</option><option value="1.15">1.15×</option><option value="1.3">1.3×</option><option value="1.5">1.5×</option></select></label><label><input type="checkbox" id="continuous" checked> Play next chapter</label></div><p id="playback-status" class="small" aria-live="polite">Ready. Use the play control to listen.</p><div class="card-links"><a id="download" href="/audio/{tracks[0]['filename']}" download>Download audio</a><a id="transcript" href="/audio/{tracks[0]['script_filename']}">Spoken transcript</a><a id="read-chapter" href="/read/{tracks[0]['slug']}/">Read chapter</a></div></section>{playlist}<section class="section"><p class="small">For offline listening, download a chapter and open it in your phone’s audio player. Browser background playback depends on your phone and browser. Reading and listening do not require an account.</p><noscript><p>JavaScript is off. Use these direct audio links:</p><ul>{''.join(f'<li><a href="/audio/{t["filename"]}">{html.escape(t["title"])}</a></li>' for t in tracks)}</ul></noscript></section>''', 'Listen', '<script type="application/json" id="audio-data">'+json.dumps(tracks,ensure_ascii=False).replace('</',r'<\/')+'</script><script src="/assets/listen.js" defer></script>')
    page('project', 'About the open-source project', '<article class="prose">'+render(ROOT/'pages/about.md')+'<h2>Start with one contribution</h2><p><a href="/contribute/">Read the contribution guide</a>, <a href="'+REPO+'/issues">browse the review discussions</a>, or <a href="/downloads/project-source.zip">download the source package</a>.</p></article>', 'Project')
    page('contribute', 'Contribute and peer review', '<article class="prose">'+render(ROOT/'pages/contributing.md')+f'<div class="actions"><a class="button" href="{REPO}/issues/new?template=review.yml">Submit a review</a><a class="button secondary" href="{REPO}/issues/new?template=proposal.yml">Propose an analysis</a></div><p class="small">GitHub requires an account to submit an issue or pull request. All submissions and review discussions are public. Reading this website requires no account.</p></article>', 'Contribute')
    page('licenses', 'Licenses and attribution', '<article class="prose">'+render(ROOT/'LICENSE-CONTENT.md')+render(ROOT/'THIRD_PARTY_NOTICES.md')+'</article>')
    subprocess.run([sys.executable, str(ROOT/'scripts/build_reader.py')],check=True,stdout=subprocess.DEVNULL)
    research = (ROOT/'outputs/The_Quran_Examined_Research_Edition.html').read_text()
    research = research.replace('Local reading edition','Public research draft').replace('The Qur’an Examined | First research edition','Research | Inimitable Qur’an Project')
    research = research.replace('<body>', '<body><nav aria-label="Project navigation" style="padding:14px 24px;display:flex;gap:22px;flex-wrap:wrap;font-size:14px"><a href="/">Inimitable Qur’an Project</a><a href="/read/">Read</a><a href="/listen/">Listen</a><a href="/project/">Project</a><a href="/contribute/">Contribute</a></nav>')
    research = research.replace('<h1>Begin with<br>the language.</h1>','<h1>Inspect the<br>evidence.</h1>')
    (OUT/'research/index.html').write_text(research)
    downloads = OUT/'downloads'; downloads.mkdir(exist_ok=True)
    shutil.copy(ROOT/'outputs/The_Quran_Examined_Manuscript.md',downloads)
    for name in ['LICENSE','LICENSE-CONTENT.md','THIRD_PARTY_NOTICES.md','README.md','CONTRIBUTING.md','CHANGELOG.md']:
        shutil.copy(ROOT/name,downloads)
    with zipfile.ZipFile(downloads/'project-source.zip','w',zipfile.ZIP_DEFLATED) as archive:
        for directory in ['chapters','research','analysis','data','scripts','pages','assets','tests']:
            for source in sorted((ROOT/directory).rglob('*')):
                if source.is_file() and '__pycache__' not in str(source) and source.suffix != '.pyc':
                    archive.write(source,source.relative_to(ROOT))
        for pattern in ['*.txt', '*.md']:
            for source in (ROOT/'audio').glob(pattern): archive.write(source,source.relative_to(ROOT))
        archive.write(ROOT/'audio/metadata.json','audio/metadata.json')
        for source in (ROOT/'audio/rights').rglob('*'):
            if source.is_file(): archive.write(source,source.relative_to(ROOT))
        for name in ['LICENSE','LICENSE-CONTENT.md','THIRD_PARTY_NOTICES.md','README.md','CONTRIBUTING.md','CHANGELOG.md','requirements.txt','requirements-lock.txt']:
            archive.write(ROOT/name,name)
    urls = [BASE+'/',*[BASE+p for _,p in NAV],*[BASE+'/read/'+t['slug']+'/' for t in tracks]]
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+url+'</loc></url>' for url in urls)+'</urlset>')
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n')
    print(json.dumps({'pages':len(list(OUT.rglob('index.html'))),'chapters':len(chapters),'audio_files':len(list((OUT/'audio').glob('*.m4a')))},indent=2))

if __name__ == '__main__': main()
