# Economy and sound: a bounded inventory

This release adds exact written-token counts for the passages discussed in Chapters 5 and 6, alongside **manual** sound and discourse annotations for Qur’an 93. It contains no acoustic measurements, human judgments, comparison corpus, or significance tests.

Run `python scripts/analyze_close_readings.py` from the repository. The script imports the existing corpus loader and token rule, verifies the raw input against `data/manifest.json`, and writes [JSON](close-reading-observations.json) and [CSV](duha-verse-observations.csv).

## What was computed

| Passage | Written tokens under the existing rule |
|---|---:|
| 2:178 | 37 |
| 2:179 | 8 |
| 93:3 | 5 |
| Complete numbered verses of surah 93 | 40 |

Surah 93, verse by verse: **1, 3, 5, 5, 4, 4, 3, 3, 4, 4, 4**. Attached conjunctions and suffixes remain attached. Unnumbered opening basmalas and stand-alone recitation marks are excluded. Counts do not measure meanings or literary quality.

## What was annotated

| Verses | Editorial discourse label | Approximate terminal sound at a verse-end stop |
|---|---|---|
| 1–2 | Oath | ā |
| 3 | Reassurance | ā |
| 4–5 | Promise | ā |
| 6–8 | Remembered provision | ā |
| 9–10 | Prohibition | r |
| 11 | Positive instruction | th |

The terminal labels yield 8 occurrences of ā, 2 of r, and 1 of th. These are counts of declared annotations. The program does **not** infer phonetic realization from Arabic spelling, discover discourse functions, or confirm the annotator’s interpretation. No claim is made about every reading tradition. Approximate pausal transliterations require independent specialist checking.

Several discourse transitions occur without a change in terminal label. The shift at verse 9 coincides with a move to instruction under the proposed reading, but this single selected case cannot establish that rhyme generally encodes discourse boundaries. A later study must record prior exposure to these observations and cannot present the same case as an untouched confirmatory sample.

The final written tokens in the CSV are unchanged extracts from the pinned text. Source: [Tanzil Project](https://tanzil.net/), Uthmani 1.1. Full attribution and original notice are preserved in `data/raw/tanzil-uthmani-1.1.xml` and `THIRD_PARTY_NOTICES.md`. The raw corpus is unchanged; no normalized Qur’an text is exported.

The chapter interpretations and manual annotations are original project proposals. Code verification is not scholarly validation. No superiority or divine-origin conclusion is encoded in these files.
