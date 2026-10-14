#!/usr/bin/env python3
"""Principles of clear scientific writing: sentence-level measurements.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_principles_demo.py

Everything here is SYNTHETIC.  Sentences are modelled statistically; no text is
read or reproduced.  The syllable and passive rates are chosen teaching values.

Sections
--------
1. Sentence length distribution and its tail.
2. Readability: the Flesch reading-ease formula on the synthetic corpus.
3. Nominalisations and passives per 100 sentences / 100 words.
4. What one revision pass buys: splitting the long sentences.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC style parameters (chosen teaching values) ---------------------
N_SENTENCES = 500
MEDIAN_WORDS = 22.0        # median sentence length, words
SIGMA_LOG_WORDS = 0.45     # lognormal spread of sentence length
MEAN_SYLLABLES = 1.55      # syllables per word, technical prose
SD_SYLLABLES = 0.12
P_PASSIVE = 0.25           # fraction of sentences with a passive construction
P_NOMINALISATION = 0.06    # nominalisations per word
LONG_SENTENCE = 30.0       # words above which a sentence is "long"
FRE_READABLE = 60.0        # Flesch reading ease above which prose is plain


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    words = MEDIAN_WORDS * RNG.lognormal(0.0, SIGMA_LOG_WORDS, N_SENTENCES)
    words = np.clip(words, 5.0, 80.0)
    syllables_per_word = RNG.normal(MEAN_SYLLABLES, SD_SYLLABLES, N_SENTENCES)
    fre = 206.835 - 1.015 * words - 84.6 * syllables_per_word

    section("1. Sentence length distribution and its tail")
    print(f"SYNTHETIC prose: {N_SENTENCES} sentences, median length chosen as "
          f"{MEDIAN_WORDS:.0f} words")
    print(f"  mean sentence length   = {words.mean():.1f} words "
          f"+/- {words.std(ddof=1):.1f} (1 s.d.)")
    print(f"  median sentence length = {np.median(words):.1f} words")
    print(f"  90th percentile        = {np.percentile(words, 90):.1f} words")
    long_frac = float(np.mean(words > LONG_SENTENCE))
    print(f"  sentences longer than {LONG_SENTENCE:.0f} words = "
          f"{int(np.sum(words > LONG_SENTENCE))} "
          f"({long_frac * 100:.1f} %)")
    print(f"  words living in those long sentences = "
          f"{int(words[words > LONG_SENTENCE].sum())} of {int(words.sum())} "
          f"({words[words > LONG_SENTENCE].sum() / words.sum() * 100:.1f} % of all words)")
    print("  -> the long quarter of sentences carries two fifths of the prose:")
    print("     edit the tail first, because that is where the words are.")

    section("2. Readability: the Flesch reading-ease formula")
    print(f"  syllables per word = {syllables_per_word.mean():.3f} "
          f"+/- {syllables_per_word.std(ddof=1):.3f}")
    print(f"  mean Flesch reading ease = {fre.mean():.1f} "
          f"+/- {fre.std(ddof=1):.1f} (dimensionless score)")
    print(f"  median Flesch reading ease = {np.median(fre):.1f}")
    print(f"  sentences above a plain-prose score of {FRE_READABLE:.0f}: "
          f"{np.mean(fre > FRE_READABLE) * 100:.1f} %")
    print(f"  sentences below 30 (hard reading): {np.mean(fre < 30) * 100:.1f} %")
    print("  -> the formula is sensitive to both length and syllables: at 1.55")
    print("     syllables/word, ten extra words cost about ten score points.")

    section("3. Nominalisations and passives per 100 sentences / 100 words")
    passive = RNG.random(N_SENTENCES) < P_PASSIVE
    nominalisations = RNG.poisson(P_NOMINALISATION, int(words.sum()))
    print(f"  passive constructions = {int(passive.sum())} in {N_SENTENCES} sentences "
          f"= {passive.mean() * 100:.1f} per 100 sentences")
    print(f"  nominalisations = {int(nominalisations.sum())} in {int(words.sum())} words "
          f"= {nominalisations.mean() * 100:.1f} per 100 words")
    print(f"  words per nominalisation = {words.sum() / max(nominalisations.sum(), 1):.1f}")
    print("  -> both rates are informative only against a target; state the target,")
    print("     because passive voice is correct whenever the agent is unknown.")

    section("4. What one revision pass buys: splitting the long sentences")
    words_after = np.concatenate([words[words <= LONG_SENTENCE],
                                  words[words > LONG_SENTENCE] / 2.0,
                                  words[words > LONG_SENTENCE] / 2.0])
    syllables_after = np.concatenate([
        syllables_per_word[words <= LONG_SENTENCE],
        syllables_per_word[words > LONG_SENTENCE],
        syllables_per_word[words > LONG_SENTENCE]])
    fre_after = 206.835 - 1.015 * words_after - 84.6 * syllables_after
    print(f"  before: {N_SENTENCES} sentences, mean {words.mean():.1f} words, "
          f"mean reading ease {fre.mean():.1f}")
    print(f"  after : {words_after.size} sentences, mean {words_after.mean():.1f} words, "
          f"mean reading ease {fre_after.mean():.1f}")
    print(f"  opening a long sentence changes the mean reading ease by "
          f"{fre_after.mean() - fre.mean():+.1f} points "
          f"({(fre_after.mean() - fre.mean()) / fre.mean() * 100:+.1f} %)")
    print(f"  sentences longer than {LONG_SENTENCE:.0f} words remaining: "
          f"{int(np.sum(words_after > LONG_SENTENCE))} (was "
          f"{int(np.sum(words > LONG_SENTENCE))})")
    print("  -> one structural pass removes the entire tail; no single word choice does.")
    print(f"  clipped-word artefact check: max words before "
          f"{words.max():.0f}, max after {words_after.max():.0f} (split only)")


if __name__ == "__main__":
    main()
