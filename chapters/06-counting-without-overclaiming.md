# Counting Without Overclaiming

*Research draft · 20 September 2026. The corpus inventory below is completed. The reader studies, comparisons, and mathematical displays are proposals, not reported findings. Independent methodological review remains pending.*

Imagine placing two versions of a sentence before a reader. Both mention an old man and gray hair. One makes the head the subject of blazing; the other makes gray hair the subject. We can explain why the difference matters. Could we also investigate whether other readers notice what we notice?

That question gives mathematics useful work. It can help us move from a critic’s explanation to an inspectable pattern of judgments. It can reveal when an effect depends on one passage, one interpreter, or one familiar performance. It can also clarify the limits of a comparison. Used well, measurement makes an argument more answerable to its readers.

The starting point is the linguistic question. What does this construction allow the sentence to accomplish? A count or a model becomes valuable when it helps answer that question more precisely.

## Begin with a count someone else can reproduce

Our first calculation concerns length. The project preserves one downloaded Tanzil Uthmani XML file, version 1.1, representing the Ḥafṣ reading. Its digital fingerprint identifies the exact bytes used. The script counts numbered verse text without rewriting the source file. The [data manifest](https://github.com/reshadn/inimitable-quran-project/blob/main/data/manifest.json) records the source and fingerprint; the [analysis script](https://github.com/reshadn/inimitable-quran-project/blob/main/scripts/analyze_corpus.py) records the operations.

A token here is a whitespace-separated field containing a full-sized Arabic base letter. An attached conjunction or preposition stays attached. A stand-alone pause or prostration sign is excluded. Unnumbered opening basmalas stored separately in the XML are excluded; the numbered text of 1:1 and the basmala within 27:30 remain included. These are written units, not a morphological count of independently functioning pieces.

Under that rule, the file contains 114 surahs, 6,236 numbered verses, and 77,433 orthographic tokens. Counting every whitespace field, including stand-alone signs, instead gives 81,812. The median verse has 10 tokens; the mean is approximately 12.42. The middle half lies between 6 and 16 tokens. The shortest count is 1 and the longest 128. These are descriptions of this fixed file under this rule. [CNT-01: recorded results](https://github.com/reshadn/inimitable-quran-project/blob/main/analysis/summary.json)

The gap between 77,433 and 81,812 is already instructive. A number called “the word count” can conceal a decision about what counts as a word. Neither typography nor software automatically settles a linguistic definition. Reproducibility requires the rule as well as the result.

Al-ʿAṣr has counts of 1, 4, and 9 tokens across its three verses. Its exception therefore occupies nine of fourteen tokens. That observation directs attention back to the reading: the composition gives substantial written space to the response to human loss. The interpretation comes from the content and arrangement. The number makes one aspect visible; it cannot tell us how much wisdom fourteen tokens contain.

There is no sampling-error interval around this enumeration. We counted the whole pinned file. The relevant uncertainties concern representation and definition, which can be explored by applying other justified rules and documenting what changes.

## Make the literary explanation do predictive work

Consider the proposed reading of 19:4 developed earlier. Predicating blazing of the head presents grayness as pervasive. A useful next step is to ask qualified readers a focused question: which formulation more strongly conveys grayness overtaking the head?

The alternatives must be competent Arabic. Independent reviewers would check grammatical acceptability, retained content, and unintended changes before the main study. If a reformulation sounds awkward, its poor reception cannot isolate the subtler effect of grammatical arrangement. The original and alternatives must be presented with enough surrounding context for the prayer to remain intelligible.

The same procedure should be applied to accomplished human writing. Otherwise we discover only that editing a respected text can diminish it. A comparative claim asks whether a specified contribution is more sustained, more consequential, or harder to preserve across alternatives in one selected body of writing than another. That requires comparison samples chosen for stated purposes, with their strengths intact.

For a reader, the task should remain concrete. Ask about scope of the image, clarity of the situation, or fit within the appeal. Invite an explanation alongside the response. Separate these from an overall beauty judgment. A reader who prefers a sentence may explain that preference differently from the researcher.

Our first two literary examples are teaching cases that generated the questions. They cannot also count as untouched confirmation of those questions. Later passages and independently prepared alternatives should test whether the account travels beyond its starting examples.

## Let readers differ without making them disappear

Suppose, solely as an illustration, that 40 out of 50 readers select one wording as conveying pervasive spread more strongly. The arithmetic is 80 percent. This is a toy example, not project data, a recruitment target, or a forecast.

Before interpreting that proportion, we need to know who read what. Fifty responses from one person are different evidence from responses by fifty people. Fifty people assessing one sentence tell us little about how the same effect behaves across many sentences. A strong analysis respects both sources of variation.

Mixed-effects models can represent variation associated with readers and passages together. They can also allow readers or passages to differ in their response to a manipulation. Barr, Levy, Scheepers, and Tily explain why this structure matters for generalization in language experiments. Their discussion of clustered observations and participant and item effects supplies a methodological foundation, not a ready-made verdict about this project. [CNT-02: Barr and colleagues, pp. 255–257](https://www.mit.edu/~rplevy/papers/barr-etal-2013-jml.pdf)

If responses use ordered categories, an ordinal model is a candidate. It need not assume that the distance from “slightly” to “moderately” equals the distance from “moderately” to “strongly.” The model, its assumptions, and its handling of repeated measurements should be settled through pilot work and simulation before a confirmatory study. No model compensates for poor alternatives or an unrepresentative sample.

Recognition also belongs in the record. Removing a title does not make a memorized verse anonymous. Record recognition, Arabic proficiency, relevant training, and familiarity separately. Religious commitment may be voluntarily reported when justified by the study design. Analyses can ask whether patterns differ across these backgrounds, while recognizing that statistical adjustment does not recreate an experiment in which familiarity was randomly assigned.

## Map several accomplishments together

The most interesting claim about arrangement may concern simultaneous demands. An expression can be economical while keeping its meaning precise, fitting its context, and giving sound a structural role. Compressing further may lose a necessary distinction. Explaining more explicitly may weaken the movement of a prayer.

A useful proposed display would give each version a profile rather than one grand score. Readers could inspect clarity, recoverable meaning, contextual fit, and sound contribution separately. Each measure would have its own definition and evidence. Textual observations, expert annotations, and listener responses should remain distinguishable.

This leads to a familiar mathematical idea: Pareto comparison. A version dominates another, under the chosen measures, if it is at least as good on every included dimension and better on at least one. When one version gains clarity but loses economy, the comparison exposes a tradeoff instead of concealing it inside a weighted average.

For this project, a proposed “revision map” could show which functions survive each competent alteration. The map would link every change to the reviewer’s reason and the underlying passage. A reader could move from the picture to the language, then to the disagreement about its effect.

These are proposed applications, not claims that this project invented multi-objective analysis. A frontier marks what the sampled alternatives achieve under specified criteria. Adding a stronger alternative, changing a measure, or acknowledging uncertainty can change the frontier. Being undominated in a study does not demonstrate being unreachable by every possible human composition.

## Preserve the discovery without disguising its history

Exploration is necessary. We should look for patterns in sound, syntax, thematic recurrence, and composition. But the history of a discovery changes the question we can fairly ask of it.

Suppose a researcher tries several spellings, boundaries, token rules, and ways of grouping verses before finding an arresting numerical relationship. The final pattern is one outcome of a larger search. Evaluating it as though it were the only prediction made beforehand exaggerates its evidential force.

Gelman and Loken’s discussion of the “garden of forking paths” identifies a related difficulty: analytical choices can depend on observed data even when a researcher performs only one final analysis and acts sincerely. The relevant flexibility includes potential decisions that different observations would have prompted. [CNT-03: Gelman and Loken, pp. 1–3](https://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf)

The remedy is to preserve exploration openly and reserve a separate opportunity for confirmation. State the main question, eligible materials, counting rules, outcomes, exclusions, stopping rule, and analysis before viewing the relevant results. If several confirmatory questions are tested, specify how their multiplicity will be handled. Report disappointing results alongside favorable ones.

The Center for Open Science’s guidance distinguishes exploratory work from confirmation and emphasizes reporting planned analyses and disclosing changes. A written protocol in our repository is preparation; it does not mean a study has been preregistered or independently reviewed. [CNT-04: preregistration guidance](https://www.cos.io/initiatives/prereg)

The existing verse-length inventory has already been inspected. Calling part of those same results “held out” later would not undo that exposure. New confirmation needs a defensible separation, such as independently collected responses or genuinely unexamined measurements relevant to a specified question.

## Ask what the model was built to recognize

A classifier might learn to distinguish Qur’anic passages from selected Arabic comparison texts. That can help locate stylistic regularities worth reading closely. It might identify useful combinations of features that a single frequency table misses.

It might also learn editorial spelling, topic, quotation, or a difference in period. A random split of excerpts from the same source works can make prediction easier than the intended task warrants. For claims about generalization across human authors, complete authors or works should be held out where appropriate. Qur’anic passage partitions need their own dependence assessment; they are not independent samples of different authors.

Recognition accuracy answers a discrimination question under the training and testing conditions. It does not establish beauty, communicative success, or divine origin. A computer can distinguish a newspaper from a sonnet without ranking either accomplishment. The next literary question is why the recognized features matter in context.

Likewise, comparing a passage with randomly shuffled words answers only a narrow structural question. A shuffled sequence is not the strongest available human composition. The choice of baseline partly determines how impressive a result will appear.

## Keep the final inference visible

The American Statistical Association warns against interpreting a p-value as the probability that a hypothesis is true or treating a threshold as a substitute for reasoning. It also distinguishes statistical significance from an effect’s magnitude or importance. Those principles apply directly here. A small p-value from a well-designed reader study would concern its specified statistical model, not the probability that revelation occurred. [CNT-05: ASA principles, p. 2](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf)

Bayesian reasoning can make the explanatory question explicit. Posterior odds between revelation and a human-composition account equal prior odds multiplied by a likelihood ratio, provided the probabilities are coherently specified. The ratio compares how expected the evidence would be under the two accounts.

Writing the identity supplies neither expectation. In particular, “revelation” does not automatically specify a probability distribution over possible texts or divine choices. An unspecified revelation distribution cannot yield a numerical likelihood ratio. Nor can a convenient model of ordinary writing stand in for every account of exceptional human authorship.

We can still compare explanatory strengths, identify assumptions, and ask which additional evidence would change the assessment. But we should not multiply literary, emotional, and historical observations as independent probabilities when they share sources or causes. A single construction can contribute to several measured responses without becoming several independent miracles.

The positive task is demanding and worthwhile: make a linguistic explanation precise, test it against strong alternatives, show where it holds, and make disagreement legible. Mathematics can help readers see an achievement more clearly. The further argument for revelation must explain why that achievement, together with independently supported historical and philosophical considerations, warrants the conclusion.
