"""Exact written-token inventory plus explicitly manual reading annotations.

No acoustic data, significance test, or comparative literary score is computed.
"""
from pathlib import Path
import csv
import json
from collections import Counter
from analyze_corpus import load_corpus, lexical_tokens

ROOT = Path(__file__).resolve().parents[1]
# Approximate ending-word transliterations for a Hafs verse-end stop.
# These annotations are not generated from spelling and await expert review.
ANNOTATIONS = [
    (1, 'ḍuḥā', 'ā', 'oath'),
    (2, 'sajā', 'ā', 'oath'),
    (3, 'qalā', 'ā', 'reassurance'),
    (4, 'ūlā', 'ā', 'promise'),
    (5, 'tarḍā', 'ā', 'promise'),
    (6, 'āwā', 'ā', 'remembered provision'),
    (7, 'hadā', 'ā', 'remembered provision'),
    (8, 'aghnā', 'ā', 'remembered provision'),
    (9, 'taqhar', 'r', 'prohibition'),
    (10, 'tanhar', 'r', 'prohibition'),
    (11, 'ḥaddith', 'th', 'positive instruction'),
]


def main():
    manifest, verses = load_corpus()
    by_id = {(v['surah'], v['verse']): v for v in verses}
    rows = []
    for number, ending, terminal, function in ANNOTATIONS:
        verse = by_id[93, number]
        words = lexical_tokens(verse['text'])
        rows.append(dict(verse=f'93:{number}', written_tokens=len(words),
                         final_written_token=words[-1],
                         approximate_pausal_ending_manual=ending,
                         terminal_sound_manual=terminal,
                         discourse_function_manual=function))
    data = {
        'source_sha256': manifest['sha256'],
        'status': 'descriptive extraction with manual annotations; not an experiment',
        'representation': 'Pinned Tanzil Uthmani 1.1, Hafs; numbered verses only',
        'token_rule': 'Reuse analyze_corpus.lexical_tokens; attached clitics retained',
        'annotation_status': 'Editorial proposals; independent Arabic and recitation review pending',
        'economy_cases': [{'verse': f'{s}:{v}', 'written_tokens': by_id[s, v]['lexical_tokens']}
                          for s, v in [(2, 178), (2, 179), (93, 3)]],
        'surah_93': rows,
        'surah_93_total_written_tokens': sum(r['written_tokens'] for r in rows),
        'terminal_label_counts': dict(Counter(r['terminal_sound_manual'] for r in rows)),
        'limits': ['Labels are not an exhaustive rhyme classification.',
                   'No recordings or listeners were analyzed.',
                   'Discourse groupings are interpretations, not discovered ground truth.',
                   'Counts do not demonstrate rarity, excellence, inimitability, or origin.']
    }
    out = ROOT / 'analysis'
    (out / 'close-reading-observations.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    with (out / 'duha-verse-observations.csv').open('w') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    print(json.dumps({'surah_93_written_tokens': data['surah_93_total_written_tokens'],
                      'terminal_label_counts': data['terminal_label_counts'],
                      'source_hash_verified': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
