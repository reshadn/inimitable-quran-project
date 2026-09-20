# Inimitable Qur’an Project

A book and open research program examining Qur’anic language, inimitability, and the case for revelation. The project develops an affirmative argument while welcoming criticism, strong human-authorship explanations, and evidence that weakens particular claims.

- [Read the public draft](https://inimitable-quran-project.workspace-114686.chatgpt.site/read/)
- [Listen on your phone](https://inimitable-quran-project.workspace-114686.chatgpt.site/listen/)
- [About the project](https://inimitable-quran-project.workspace-114686.chatgpt.site/project/)
- [Submit a correction or review](https://github.com/reshadn/inimitable-quran-project/issues)

## Release status

This is research draft 0.1, not a completed book or established demonstration of divine origin. The initial manuscript and source checks were developed with AI assistance. Independent human scholarly review is pending. The release contains an opening essay and two sample chapters, approximately 6,000 words, plus a 65-record source catalog. Nine entries have bounded passage/documentation inspection, 28 have bibliographic confirmation, and 28 remain discovery leads. No full work was read in this first pass. Inclusion is not endorsement.

The corpus pilot is descriptive. No reader, expert, or recitation study has been conducted. Literary distinctiveness, excellence, universal human incapacity, and revelation are separate claims. There is no numerical score of divinity.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Arabic specialists, historians, literary scholars, statisticians, accessibility reviewers, believers, and skeptical readers are welcome. Use an issue for an evidence-backed review or analysis proposal. Use a pull request for a concrete change. Public submission is not acceptance or endorsement. The workflow is maintainer-led community review, not completed independent academic peer review.

## Repository map

- `chapters/`: manuscript source in Markdown.
- `research/`: source ledger, bibliography, claims, book plan, and proposed protocols.
- `data/`: unchanged source corpus and hash manifest.
- `analysis/`: reproducible descriptive pilot outputs.
- `audio/`: synthetic English audio, spoken transcripts, and metadata.
- `pages/`, `assets/`, `scripts/`: public website content and reproducible build.
- `tests/`: corpus integrity checks.
- `dist/`: generated public static website.

## Reproduce

Create a Python virtual environment and install `requirements.txt`. The pinned versions used in the initial environment are recorded in `requirements-lock.txt`; some platforms may need compatible package versions.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/analyze_corpus.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/build_website.py
.venv/bin/python -m http.server 8747 --directory dist
```

The source ZIP omits binary narration to keep the source download small. To build with audio, use the GitHub repository or copy the three published `.m4a` files into `audio/`. Serving locally is a preview; it does not publish. The public corpus file must remain unchanged, including its license notice.

## Licenses

Original software: [MIT](LICENSE). Original prose and documentation: [CC BY 4.0](LICENSE-CONTENT.md), to the extent rights exist. Third-party material, especially the Tanzil corpus and voice models, is excluded from these blanket grants. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Respect rights and disclose uncertainty in contributions.
