# Third-party notices

## Qur’anic text and linguistic sources

The unchanged `data/raw/tanzil-uthmani-1.1.xml` was obtained from the [Tanzil Project](https://tanzil.net/). Its complete copyright notice and distribution conditions are preserved inside the file. Tanzil permits verbatim copying and distribution with attribution and its notice; changing the supplied text is not allowed under the stated terms. This corpus is excluded from the project's general prose and code licenses. Analysis outputs describe that pinned file and do not replace its text.

Arabic quotations in chapters are identified by passage. Working English renderings are identified as original project translations and need independent specialist review. Cited classical editions, modern books and articles, external translations, and websites retain their respective rights. Links and brief attributed quotations do not place those works under the project license. Full copyrighted scans are not included.

## Synthetic narration

Audio is a synthetic English reading adaptation, not Qur’anic recitation. The release uses Kokoro-82M with the af_heart preset. The [official model card](https://huggingface.co/hexgrad/Kokoro-82M) identifies the model as Apache-2.0; [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) identifies its wrapper as MIT and its model as Apache-2.0. Generation is local. Model weights and the engine are not distributed with the website. Audio metadata records the generation method and verification scope. Do not imply a human narrator, an endorsement by the voice-model creators, or verified Qur’anic pronunciation.

The project does not apply its blanket content license to third-party voice or model rights. This notice does not grant rights to extract, impersonate, or redistribute a voice model. Apple system-voice recordings were not used in this public release.

## Software

The static build uses Python-Markdown. The analytical scripts use dependencies listed in `requirements.txt` and `requirements-lock.txt`; each dependency retains its license. Dependencies are installed separately rather than vendored into this repository. No third-party tracking or advertising scripts are included by the project. Hosting providers and external services, including GitHub, operate under their own policies.
