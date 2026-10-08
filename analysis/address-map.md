# Reference map: selected shifts of address

8 October 2026. Editorial annotation inventory accompanying Chapter 7, Shifts of Address. This is not a corpus-wide detection method or a reader experiment.

## Reproduce and inspect

Run `python scripts/analyze_address.py` from the repository root, with the project dependencies available. The existing `load_corpus` function verifies the raw Tanzil file against its pinned SHA-256 before extraction.

[JSON inventory](address-map.json). [CSV mention table](address-map.csv). [Corpus manifest](../data/manifest.json). [Chapter sources](../research/sources-address.json).

The chapter prints all of 1:1–7 and 10:21–23. The inventory selects 18 mentions from that context. It does not annotate every word, pronoun, clause, or rhetorical change. One-based indices use the existing lexical-token rule: attached clitics remain attached, and stand-alone recitation signs are excluded. An anchor is a complete unchanged lexical token. A token may contain several reference-bearing components, so two rows can share an anchor without duplicating the same mention.

## Annotation decisions

Each row identifies a grammatical component within the anchor, a proposed referent, person, speech layer, and discourse role. All five labels are manual editorial proposals. The program verifies the extraction and computes comparisons using those labels. It does not independently establish their accuracy.

Person is coded 1, 2, or 3. A named divine referent, including the title at 1:4, is assigned third-person presentation for this operational rule. This follows the convention discussed in Ibn ʿĀshūr's commentary on 1:5; it is not a claim that every named expression is a third-person pronoun. An imperative's implied addressee can carry a second-person assignment even when no independent pronoun is written.

The worshipper prayer in al-Fātiḥa is one represented speech layer. In 10:22, the outer discourse and the travelers' quoted plea are separate layers. These are textual voice labels, not hypotheses about the number of authors. The boats are distinguished from the travelers in the sailing construction. The general human audience addressed in 10:23 is labelled separately from the narrated travelers; overlap in membership does not justify assigning numerical identity without further argument.

## A declared comparison rule

For mentions **a** and **b**, with manual labels **r** (referent), **p** (person), and **s** (speech layer), define a flag:

`T(a,b) = 1 if r(a)=r(b), s(a)=s(b), and p(a)≠p(b); otherwise 0.`

Two pairs were selected as illustrations before executing the program: F-title → F-you and J-when → J-them. The inventory also records two exclusion controls: J-them → J-us crosses a quoted-speech boundary, and J-rescued → J-audience extends to a wider audience. These pairs are not automatically adjacent mentions. They are declared comparison points, selected using the literary discussion.

Under these supplied annotations, the two illustrative pairs meet the rule. Their directions are 3→2 and 2→3. Both controls receive zero. These outputs are consequences of the declared annotations, not independent discoveries supporting the interpretation. Alternative assignments and broader rhetorical definitions may change the classification. No global frequency or significance test is appropriate for these deliberately selected cases.

## Review and prospective measurement

Before any study, an independent Arabic reviewer should check the anchors, components, referents, and speech layers. Multiple reviewers should annotate independently under a written manual, with disagreements preserved before adjudication. No inter-annotator agreement has been measured for this inventory.

A future reader protocol should separate reference comprehension, perceived coherence, and literary preference. Document recognition and familiarity. Review manipulated passages for grammatical competence and naturalness. Model repeated judgments by reader and passage rather than treating every answer as an independent person. Those are design requirements, not completed analyses.

No human participant data, acoustic data, comparative superiority, novelty, universal incapacity, or probability of revelation is reported.
