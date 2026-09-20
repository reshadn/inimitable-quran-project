# English narration provenance

These recordings were synthesized locally from the accompanying English narration scripts using Kokoro-82M v1.0, the af_heart preset, and kokoro-onnx. They contain synthetic English discussion, not Qur'anic recitation. No Apple System Voice is present in these replacement files.

## Published permissions checked on 20 September 2026

- The official [Kokoro model card](https://huggingface.co/hexgrad/Kokoro-82M) declares Apache-2.0 and expressly welcomes production and commercial deployments. The inspected repository revision is `f3ff3571791e39611d31c381e3a41a3af07b4987`.
- The official [voice list](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) identifies `af_heart` as an American English preset. It belongs to the same Apache-licensed model repository.
- The [kokoro-onnx repository](https://github.com/thewh1teagle/kokoro-onnx) identifies its inference code as MIT and the Kokoro model as Apache-2.0. The conversion files came from its `model-files-v1.1` release.
- Neither the inspected model terms nor inference-code terms impose an output-publication prohibition or per-use fee. This is the basis for generating recordings for the public listening site. The project is distributing audio, not model weights or inference software.

Primary-source snapshots and the Apache and MIT license texts are retained in the `rights` folder. Generated-file and model hashes, package versions, source hashes, and technical verification are recorded in `public-metadata.json`.

## Verification and limits

Each chapter is checked for valid sample data, expected nonzero duration, AAC-LC encoding, fast-start layout, and full-file decoding without errors. No auditory review has been performed. English pronunciation of transliterated Arabic words and names may be imperfect. The original Arabic passages and citations remain available in the written edition.

Suggested site credit: "Synthetic English narration generated locally with Kokoro-82M (af_heart), an Apache-2.0 model, using the MIT-licensed kokoro-onnx runtime. This is narration of the research draft, not Qur'anic recitation."
