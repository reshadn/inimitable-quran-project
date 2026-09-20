# Measuring without overstating

*Protocol development document, version 0.1 · 16 September 2026. No human data have been collected. This document has not been preregistered.*

## A question before a measure

The research question is not whether the Qur’an receives a sufficiently high number. It is whether specified linguistic choices perform identifiable functions, whether those functions survive fair comparison, and what explanatory weight the findings deserve. Literary achievement includes relationships that cannot be reduced to frequency counts. Measurement will supplement close reading.

This document separates three stages: a completed descriptive inventory, proposed pilot studies, and later confirmatory studies. The latter cannot be specified responsibly in full until qualified specialists test whether the materials and measures are usable. The pilot-to-confirmation decisions below must be recorded before confirmatory data collection.

## Domain map

| Domain | Observable or annotatable object | Proposed question | Principal confound or limit |
|---|---|---|---|
| Lexicon | Word forms, roots, collocations | Does a choice distinguish a relevant meaning? | Root frequency is not semantic precision. |
| Morphology | Inflection, derivation, grammatical features | What does a form contribute in context? | The same form can perform different functions. |
| Syntax | Dependencies, word order, ellipsis | Which relations change under reformulation? | Annotation may be disputed. |
| Semantics | Contextually licensed propositions and inferences | What is communicated explicitly and implicitly? | Meaning-unit coding is interpretive. |
| Pragmatics | Address, presupposition, speech acts | How does the expression act upon a discourse situation? | Reconstructed context is uncertain. |
| Metaphor | Domain mappings and grammatical realization | Does grammar alter the image’s scope? | A vivid image need not have one effect for every reader. |
| Sound | Endings, phonological sequences, acoustic measures | How does recurrence support recognition or structure? | Orthography is not an audio signal. |
| Discourse | Reference, transitions, repeated phrases | What binds local units into a whole? | Familiarity can supply coherence. |
| Composition | Boundaries, parallel units, nested structures | Does a proposed organization outperform alternatives? | Flexible segmentation can manufacture patterns. |
| Narrative | Selection, pacing, perspective, retelling | What changes when a story is arranged differently? | Comparators need their own context. |
| Translation | Aligned renderings and explanations | What is preserved, lost, or added? | Translation quality is not Arabic quality. |
| Cognition | Comprehension, inference, delayed recall | Do specified choices affect understanding or memory? | Prior exposure, literacy, and language proficiency. |
| Recitation | Text and multiple performances | Which response belongs to text versus delivery? | Performance conventions are not freely interchangeable. |
| Ethics and address | Reasons, obligations, reciprocal relations | How is moral responsibility expressed? | Moral truth is not decided by literary ratings. |
| Reception | Documented responses in dated sources | What did particular readers report? | Selection, transmission, and institutional prestige. |
| Transmission | Manuscripts, readings, textual witnesses | Which expression existed in which witness? | Surviving witnesses do not exhaust the past. |
| Historical setting | Dated evidence for opportunities and conventions | Which authorship hypotheses remain plausible? | Later biography requires source criticism. |
| Philosophical explanation | Premises and their dependence | What further inference to revelation is justified? | No automatic likelihood model for revelation. |

Numerical and scientific-miracle claims require their own dossiers. Before evaluating a numerical coincidence, specify the unit, spelling, inclusion rules, search space, and independently justified prediction. Do not select a rule because it gives a desired number. Before evaluating a scientific interpretation, establish the linguistic and historical meaning independently of the later discovery. Neither domain contributes a result to this release.

## What has actually been calculated

The descriptive pilot enumerates one pinned Tanzil representation of the Ḥafṣ reading. It counts numbered verses and whitespace-separated units containing full-sized Arabic letters. Attached clitics remain attached. Stand-alone pause signs are excluded, as are unnumbered opening basmalas stored in separate XML attributes. The numbered text at 1:1 and within 27:30 remains included.

The raw XML is unchanged and hashed. Results are numeric tables keyed to surah and verse, with an exact definition and a reproducible script. These are finite-file descriptions. No hypothesis test, human-authorship classification, semantic-density score, or probability of revelation has been computed. [Tanzil representation documentation](https://tanzil.net/docs/Quran_Text_Types), [reading provenance](https://tanzil.net/docs/FAQ)

The Quranic Arabic Corpus provides a basis for later morphology work. Its documentation describes annotation and verification, but the entire annotation dataset has not been imported or independently audited here. The live download page requests a contact email; this release does not submit one. [Dukes and Habash](https://aclanthology.org/L10-1190/), [download conditions](https://corpus.quran.com/download/)

## Study A: expression, function, and controlled alternatives

**Primary pilot question:** can independent qualified readers reliably identify a specified semantic or discourse difference between an original passage and a competent alternative?

Begin with 19:4 and al-ʿAṣr as teaching pilots. They are familiar, deliberately selected passages. They are not independent confirmatory evidence for a general claim because the hypotheses were motivated by them.

For each item, record its communicative purpose, preserved core content, targeted linguistic change, grammatical acceptability, and unintended changes. Two independent Arabic reviewers must check each alternative; disagreements remain in the record. A variant that is ungrammatical or removes core content cannot be used as evidence that subtler arrangement is superior.

Pair the method with alterations of accomplished human writing. Include alternatives proposed as improvements and allow a comparator to use different techniques. Do not force every competitor to reproduce Qur’anic vocabulary, rhyme, theology, or structure. Choose broad communicative purposes before selecting the finalists, and apply the same evaluation to both sources.

Collect separate ratings of clarity, meaning preservation, contextual fit, economy, and sound contribution, plus written explanations. A proposed pilot instrument uses ordered responses with explicit verbal anchors, and allows “cannot judge.” Final scale and anchors will be fixed after cognitive interviews, not retrospectively optimized for favorable results.

Presentation order is randomized and balanced. Recognition, memorization, Arabic proficiency, relevant scholarly training, and voluntarily disclosed religious commitment are recorded separately. Famous passages cannot be assumed blind. Readers and passages are generally crossed; alternative versions are nested within source passages. The confirmatory model design will consider random slopes for manipulations repeated within readers or passages, subject to identifiability and prespecified diagnostics.

The primary confirmatory contrast will concern a preregistered target function rather than an overall beauty score. An ordinal mixed-effects model is a candidate analysis, with reader and passage effects and an original-versus-alternative term. A comparative claim additionally requires a prespecified contrast between alteration effects across the Qur’anic and human-composition samples. An alteration effect within the Qur’an alone does not establish a comparative advantage. Model family, estimand, exclusion rules, and handling of recognition will be finalized through pilot review and simulation before confirmation. Recognition effects are observational and will not be described as experimentally caused. Claims of equivalence require a justified margin and sufficient precision; failure to detect a difference is not evidence of equality.

**Weakening outcomes:** competent alternatives preserve the target function as well or improve it; effects disappear under balanced familiarity; raters cannot agree on the proposed distinction; or the same vulnerability to modification is equally present in strong human controls.

## Study B: comprehension and retention

Test Arabic specialists, proficient nonspecialists, and English readers using explained translations in separate analyses. Translation responses cannot be pooled as direct measures of Arabic performance.

Use content questions whose answers can be independently justified from the materials, including plausible distractors. Score literal recall separately from inferential comprehension. Immediate and delayed retention must use a prespecified interval and attrition policy. The pilot will assess item difficulty and ceiling effects, with final questions kept out of the main comparative analysis.

For the translation cohort, randomize whether a linguistic explanation accompanies a rendering. This can estimate an explanation’s effect on comprehension. It cannot establish that the Arabic text itself has an experimentally isolated effect. Familiarity and prior belief remain recorded, and no participant is evaluated as a better or worse believer.

Sample size will be chosen through simulation using pilot estimates of variability and clustering, a prespecified smallest effect worth discussing, and a precision target. Do not select a convenient total and portray it as sufficient. If recruitment cannot meet the target, narrow the study or label its conclusions exploratory.

## Study C: recitation and sound

Separate written-text judgments from recorded performance. Use licensed recordings or specifically consented recordings by multiple qualified performers. Document passage, reading, reciter, duration, amplitude processing, pauses, and familiarity. Randomize order and standardize playback conditions where feasible.

Do not manipulate sacred recitation into an artificial style and treat the resulting disadvantage as a fair literary control. Where comparable performance is not defensible, analyze performance conditions separately. Emotional response, perceived beauty, comprehension, and recall are distinct endpoints. An emotional response does not verify a grammatical claim or establish revelation.

Reciter and passage variation must enter the analysis. A single admired reciter versus a flat recording of a human text would confound the text with its performance.

## Mathematical explanations for readers

**Paired changes.** For a defined measurement, `Δ = original − alternative`. Show the distribution across readers and passages, not only a grand average. If the outcome is ordinal, display category probabilities or paired preference proportions rather than assuming equal intervals between labels.

**Several objectives.** Let a profile contain clarity, economy, contextual fit, and sound contribution. Under specified comparable measures, a profile dominates another only when it is no worse on every included dimension and better on at least one. Display uncertainty and the effect of changing criteria. A Pareto frontier is relative to the sampled alternatives and measurements. It is not proof of unique or unreachable achievement.

**Meaning per token.** An exploratory ratio could divide independently coded, recoverable propositions by orthographic tokens. The numerator is not a natural constant: coders may split or merge propositions, and implication depends on context. First publish the coding manual and agreement. Never equate this ratio with the full meaning or value of a verse.

**Explanatory inference.** Posterior odds equal prior odds multiplied by a likelihood ratio when the relevant probabilities are coherently specified. This identity cannot supply the missing likelihood of a particular divine choice. Use it to expose assumptions, not manufacture an impressive probability. Correlated evidence must not be multiplied as if independent.

**Structural nulls.** A shuffled text is a limited control for an explicitly defined structural feature. It is not a model of the strongest human author. Any permutation test must state which elements are exchangeable and which dependencies it preserves. If no meaningful null can be justified, use descriptive comparisons instead.

## Protections against misleading inference

Before confirmation, freeze the corpus and source-selection procedure, main hypotheses, item eligibility, primary outcomes, model, exclusions, stopping rule, missing-data approach, and multiplicity correction. Use an exploratory appendix for later questions. Report all registered outcomes, including those that weaken the argument. A local draft is not a completed preregistration. [Center for Open Science](https://www.cos.io/initiatives/prereg)

For a small set of confirmatory hypotheses, choose and justify a familywise correction such as Holm before collecting outcomes. For broad discovery, report the full search and an appropriate false-discovery procedure if assumptions permit. Neither a threshold nor its failure replaces effect size, uncertainty, context, and replication. A p-value is not the probability that revelation or human authorship is true. [American Statistical Association statement](https://magazine.amstat.org/blog/2016/03/07/pvalue-mar16/)

Hold out complete source works or authors where appropriate, not random verses from the same work on both sides of a stylometry split. Audit topic and quotation leakage. Analyze later texts influenced by the Qur’an separately. Do not multiply the nominal sample size by treating dependent tokens or repeated judgments as independent authors.

## Consent, governance, and readiness

Human studies require informed consent, a qualified study lead, an appropriate ethics determination, a data-retention policy, a recruitment scope and budget, and authorization before contacting or paying participants. Store participant identity separately from analysis data. Collection of religious commitment is optional and must be justified; report only suitably aggregated or de-identified results.

Current readiness: source and protocol development only. The present AI-assisted drafts are not independent expert review. No external registry entry, recruitment, commissioned comparison, or paid study exists. The next methodological milestone is a reviewed pilot instrument and source-matched comparator shortlist.
