"""Descriptive corpus inventory, not a test of inimitability. No network I/O."""
from pathlib import Path
import csv
import hashlib
import json
import statistics
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CASES = (1, 12, 19, 36, 55, 67, 75, 93, 103, 108, 112, 114)


def has_base_letter(token):
    # Full-sized Arabic letters present in this corpus. Small phonetic letters
    # and pause/sajdah marks do not count as stand-alone orthographic words.
    return any('\u0621' <= c <= '\u063a' or '\u0641' <= c <= '\u064a'
               or c == '\u0671' for c in token)


def lexical_tokens(text):
    return [x for x in text.split() if has_base_letter(x)]


def load_corpus():
    manifest = json.loads((ROOT / 'data/manifest.json').read_text())
    raw = (ROOT / manifest['file']).read_bytes()
    if hashlib.sha256(raw).hexdigest() != manifest['sha256']:
        raise ValueError('Raw corpus SHA-256 differs from manifest; investigate before analysis.')
    tree = ET.fromstring(raw)
    if [int(s.attrib['index']) for s in tree] != list(range(1, 115)):
        raise ValueError('Surah IDs are missing, duplicated, or reordered.')
    verses = []
    for surah in tree:
        if [int(v.attrib['index']) for v in surah] != list(range(1, len(surah) + 1)):
            raise ValueError(f'Nonsequential verse IDs in surah {surah.attrib["index"]}')
        for verse in surah:
            text = verse.attrib['text']
            if not lexical_tokens(text):
                raise ValueError('Empty or non-Arabic verse')
            verses.append({'surah': int(surah.attrib['index']),
                           'verse': int(verse.attrib['index']), 'text': text,
                           'lexical_tokens': len(lexical_tokens(text)),
                           'whitespace_fields': len(text.split())})
    if len(verses) != 6236:
        raise ValueError('Unexpected numbered verse count for the pinned text.')
    return manifest, verses


def write_csv(path, records):
    with path.open('w', newline='', encoding='utf-8') as f:
        out = csv.DictWriter(f, fieldnames=list(records[0]))
        out.writeheader()
        out.writerows(records)


def main():
    manifest, verses = load_corpus()
    out = ROOT / 'analysis'
    out.mkdir(exist_ok=True)
    rows = [{k: v for k, v in row.items() if k != 'text'} for row in verses]
    write_csv(out / 'verse-lengths.csv', rows)
    surahs = []
    for sid in range(1, 115):
        group = [r for r in rows if r['surah'] == sid]
        counts = [r['lexical_tokens'] for r in group]
        surahs.append({'surah': sid, 'verses': len(group), 'lexical_tokens': sum(counts),
                       'mean_tokens_per_verse': round(statistics.mean(counts), 4),
                       'median_tokens_per_verse': statistics.median(counts),
                       'editorial_case': sid in CASES})
    write_csv(out / 'surah-summary.csv', surahs)
    counts = [r['lexical_tokens'] for r in rows]
    q1, _, q3 = statistics.quantiles(counts, n=4, method='inclusive')
    summary = {'status': 'descriptive inventory; no inferential test or comparison corpus',
               'source_sha256': manifest['sha256'], 'surahs': len(surahs), 'verses': len(verses),
               'orthographic_tokens': sum(counts),
               'whitespace_fields': sum(r['whitespace_fields'] for r in rows),
               'mean_tokens_per_verse': statistics.mean(counts),
               'median_tokens_per_verse': statistics.median(counts),
               'q1': q1, 'q3': q3, 'min_tokens': min(counts), 'max_tokens': max(counts),
               'asr_verse_token_counts': [r['lexical_tokens'] for r in rows if r['surah'] == 103],
               'numbering_policy': 'Only numbered aya text attributes. Unnumbered opening basmalas excluded; 1:1 and basmala within 27:30 retained.',
               'token_policy': 'Whitespace fields containing a full-sized Arabic base letter; attached clitics remain attached; stand-alone pause and sajdah marks excluded.',
               'limitations': ['Not morphological word counts.', 'One pinned Hafs representation.',
                              'No rarity, superiority, origin, or population inference.',
                              'Whole-corpus descriptive exposure recorded before future study design.']}
    (out / 'summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    # Figures depict exact finite-corpus counts, so sampling-error intervals
    # would mislead. Tokenization/edition sensitivity is documented separately.
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'svg.fonttype': 'none'})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.4), gridspec_kw={'width_ratios': [1.4, 1]})
    ax1.hist(counts, bins=range(0, max(counts) + 6, 5), color='#196e64', edgecolor='white')
    ax1.set_yscale('log')
    ax1.set(xlabel='Orthographic tokens per numbered verse', ylabel='Number of verses (log scale)',
            title='Length distribution across the pinned text')
    bars = ax2.bar(['103:1', '103:2', '103:3'], summary['asr_verse_token_counts'], color=['#a9c4bd', '#668f85', '#196e64'])
    ax2.bar_label(bars, padding=4)
    ax2.set_ylim(0, 11)
    ax2.set(ylabel='Orthographic tokens', title='Al-Asr: 1, 4, and 9 written tokens')
    fig.suptitle('A description of textual length, not a measure of literary quality', fontsize=15, y=1.01)
    fig.text(.02, .015, 'Source: Tanzil Uthmani 1.1, Hafs. 6,236 numbered verses. Attached clitics retained.\nUnnumbered basmalas and stand-alone recitation marks excluded. No comparison corpus.', fontsize=9, color='#444444')
    fig.tight_layout(rect=(0, .10, 1, .97))
    fig.savefig(out / 'length-overview.svg', bbox_inches='tight')
    fig.savefig(out / 'length-overview.png', dpi=170, bbox_inches='tight')
    plt.close(fig)
    md = f'''# Descriptive pilot: what is being counted?

Executed against the pinned Tanzil Uthmani 1.1 file. This is a descriptive inventory, not a statistical demonstration of inimitability.

| Quantity | Observed value |
|---|---:|
| Surahs | {summary['surahs']} |
| Numbered verses | {summary['verses']:,} |
| Orthographic tokens under the stated rule | {summary['orthographic_tokens']:,} |
| All whitespace fields, including stand-alone signs | {summary['whitespace_fields']:,} |
| Median tokens per verse | {summary['median_tokens_per_verse']:g} |
| Mean tokens per verse | {summary['mean_tokens_per_verse']:.2f} |
| Interquartile interval | {q1:g}–{q3:g} |
| Minimum and maximum tokens per verse | {min(counts)} and {max(counts)} |
| Al-ʿAṣr, verse by verse | 1, 4, 9 |

![Corpus length distribution and al-Asr verse lengths](length-overview.svg)

## Interpretation

The final verse contains nine of the fourteen orthographic tokens in al-ʿAṣr under this rule. That describes space devoted to the exception. It does not by itself demonstrate semantic density or superiority. A token beginning with an attached conjunction remains one written token even though grammatical analysis may separate multiple morphemes.

The difference between all whitespace fields and lexical tokens demonstrates why a counting rule matters. Stand-alone pause or sajdah signs are not lexical words. The raw text is preserved without alteration; the filter is applied only in memory. We export numeric measurements, not a modified Qur’an.

The histogram uses a logarithmic vertical axis to keep rare long verses visible. It does not imply that short or long verses are better. There are no confidence intervals because these are enumerations of a fixed finite file, not estimates from a random sample. Representation and counting uncertainty require sensitivity analysis, not a sampling-error band.

## Reproduction and scope

Run `.venv/bin/python scripts/analyze_corpus.py`. The script checks the SHA-256 digest, sequential surah and verse identifiers, nonempty Arabic text, and the numbered-verse total before calculating results. CSV outputs retain verse IDs and both count definitions.

Only `aya` text attributes are counted. Unnumbered opening basmalas stored in separate attributes are excluded. The numbered basmala at 1:1 and text within 27:30 are retained. The twelve editorial surahs do not constitute a random sample. No human judgments, comparison texts, morphology corpus, acoustic data, or alternative canonical readings have been analyzed in this pilot.

All descriptive verse-length data have now been inspected by this project. They cannot subsequently be portrayed as untouched holdout data for a length hypothesis. A later confirmatory study must disclose this prior exposure.

Source: [Tanzil download](https://tanzil.net/download/), [text types](https://tanzil.net/docs/Quran_Text_Types), [reading provenance](https://tanzil.net/docs/FAQ), [license](https://tanzil.net/docs/Text_License). See `data/manifest.json` for the exact URL, retrieval time, and hash.
'''
    (out / 'pilot-report.md').write_text(md)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
