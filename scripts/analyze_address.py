"""Extract selected anchors and evaluate explicitly annotated reference pairs.

This is a manual case inventory, not an automatic iltifat detector or experiment.
"""
from pathlib import Path
from collections import Counter
import csv
import json
from analyze_corpus import load_corpus, lexical_tokens

ROOT = Path(__file__).resolve().parents[1]

# One-based lexical token indices; person and reference assignments are manual.
# The same token can carry both a subject and an object mention.
MENTIONS = [
    ('F-name', 1, 2, 2, 'named referent', 'God', 3, 'worshipper prayer', 'praise'),
    ('F-title', 1, 4, 1, 'named referent', 'God', 3, 'worshipper prayer', 'description'),
    ('F-you', 1, 5, 1, 'object', 'God', 2, 'worshipper prayer', 'direct commitment'),
    ('F-we', 1, 5, 2, 'subject', 'worshippers', 1, 'worshipper prayer', 'worship'),
    ('F-help', 1, 5, 4, 'subject', 'worshippers', 1, 'worshipper prayer', 'dependence'),
    ('F-guide', 1, 6, 1, 'implied subject of imperative', 'God', 2, 'worshipper prayer', 'petition'),
    ('F-us', 1, 6, 1, 'object suffix', 'worshippers', 1, 'worshipper prayer', 'petition'),
    ('F-favor', 1, 7, 3, 'subject', 'God', 2, 'worshipper prayer', 'continued address'),
    ('J-you', 10, 22, 3, 'object suffix', 'travelers', 2, 'outer discourse', 'addressed situation'),
    ('J-when', 10, 22, 9, 'subject', 'travelers', 2, 'outer discourse', 'addressed situation'),
    ('J-boats', 10, 22, 12, 'subject', 'boats', 3, 'outer discourse', 'sailing'),
    ('J-them', 10, 22, 13, 'prepositional object', 'travelers', 3, 'outer discourse', 'narrated situation'),
    ('J-rejoice', 10, 22, 16, 'subject', 'travelers', 3, 'outer discourse', 'rejoicing'),
    ('J-rescuer', 10, 22, 36, 'subject', 'God', 2, 'travelers quoted plea', 'rescue requested'),
    ('J-us', 10, 22, 36, 'object suffix', 'travelers', 1, 'travelers quoted plea', 'rescue requested'),
    ('J-promise', 10, 22, 39, 'subject', 'travelers', 1, 'travelers quoted plea', 'promise of gratitude'),
    ('J-rescued', 10, 23, 2, 'object suffix', 'travelers', 3, 'outer discourse', 'rescue aftermath'),
    ('J-audience', 10, 23, 13, 'possessive suffix', 'general human audience', 2, 'outer discourse', 'admonition'),
]

PAIRS = [
    ('Fatiha-description-to-address', 'F-title', 'F-you', 'selected transition'),
    ('Journey-address-to-description', 'J-when', 'J-them', 'selected transition'),
    ('Journey-quotation-boundary', 'J-them', 'J-us', 'exclusion control: different speech layer'),
    ('Journey-general-audience', 'J-rescued', 'J-audience', 'exclusion control: wider audience'),
]


def main():
    manifest, verses = load_corpus()
    by_verse = {(v['surah'], v['verse']): v for v in verses}
    mentions = []
    for ident, surah, number, position, component, referent, person, layer, function in MENTIONS:
        verse = by_verse[surah, number]
        anchor = lexical_tokens(verse['text'])[position - 1]
        assert anchor in verse['text'], f'Missing exact anchor: {ident}'
        mentions.append(dict(id=ident, verse=f'{surah}:{number}', lexical_token_index=position,
                             exact_anchor=anchor, grammatical_component_manual=component,
                             referent_manual=referent, person_manual=person,
                             speech_layer_manual=layer, discourse_role_manual=function))
    by_id = {m['id']: m for m in mentions}
    assert len(by_id) == len(mentions), 'Duplicate annotation ID'
    pairs = []
    for ident, before, after, kind in PAIRS:
        a, b = by_id[before], by_id[after]
        same_referent = a['referent_manual'] == b['referent_manual']
        same_layer = a['speech_layer_manual'] == b['speech_layer_manual']
        person_changes = a['person_manual'] != b['person_manual']
        flag = same_referent and same_layer and person_changes
        pairs.append(dict(id=ident, before=before, after=after, selection_manual=kind,
                          same_referent_under_annotation=same_referent,
                          same_layer_under_annotation=same_layer,
                          person_changes_under_annotation=person_changes,
                          meets_declared_rule=flag,
                          direction=f"{a['person_manual']}→{b['person_manual']}" if flag else None))
    data = dict(source_sha256=manifest['sha256'], updated='2026-10-08',
                status='selected textual anchors with manual annotations; no human study',
                representation='Pinned Tanzil Uthmani 1.1; one-based lexical token indices',
                scope='Complete context in chapter: 1:1–7 and 10:21–23. Mentions below are selected, not exhaustive.',
                rule='Same annotated referent and speech layer, different person. Named divine descriptions are third-person presentation by declared convention.',
                annotation_status='AI-assisted editorial proposals; independent Arabic review pending',
                mentions=mentions, preselected_pairs=pairs,
                selected_transition_direction_counts=dict(Counter(p['direction'] for p in pairs if p['meets_declared_rule'])),
                limits=['Neither token indices nor the program validate the manual reference or person assignments.',
                        'Pairs are selected illustrations, not consecutive mentions or a corpus-wide sample.',
                        'Different classical definitions may classify cases differently.',
                        'No rarity, literary superiority, reader effect, or divine origin is established.'])
    out = ROOT / 'analysis'
    (out / 'address-map.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    with (out / 'address-map.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(mentions[0]))
        writer.writeheader()
        writer.writerows(mentions)
    print(json.dumps({'mentions': len(mentions), 'preselected_pairs': len(pairs),
                      'selected_transition_direction_counts': data['selected_transition_direction_counts'],
                      'source_hash_verified': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
