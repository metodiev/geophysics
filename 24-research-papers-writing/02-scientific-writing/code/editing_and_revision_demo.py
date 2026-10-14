#!/usr/bin/env python3
"""Self-editing, revision and response to reviewers: measured edit effort.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python editing_and_revision_demo.py

Everything here is SYNTHETIC.  The manuscript is a generated word sequence, not
real prose; the cut fractions and hours per pass are chosen teaching values.

Sections
--------
1. Three revision passes and their diminishing returns.
2. How much of the text actually changes: a sequence-similarity measure.
3. Reviewer points: coverage of a response letter.
4. The cost of an unaddressed point.
"""

import difflib

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
DRAFT_WORDS = 6200
CUTS = (0.12, 0.08, 0.05)      # fraction of remaining words cut in each pass
HOURS_PER_PASS = 3.0
WORDS_PER_SENTENCE = 22
VOCAB_SIZE = 200
P_REPLACE = 0.20               # words replaced per sentence in the final version
P_DROP = 0.10                  # sentences dropped
P_REORDER = 0.05               # adjacent sentence pairs swapped
REVIEW_POINTS = (4, 5)         # points raised by each of two reviewers
P_RE_RAISE = 0.60              # P(a reviewer re-raises an unaddressed point)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def make_manuscript(n_words, rng):
    return [f"w{int(i)}" for i in rng.integers(0, VOCAB_SIZE, n_words)]


def revise(words, rng, p_replace, p_drop, p_reorder):
    out = []
    for sentence_start in range(0, len(words), WORDS_PER_SENTENCE):
        sentence = words[sentence_start:sentence_start + WORDS_PER_SENTENCE]
        if rng.random() < p_drop:
            continue
        sentence = [f"w{int(rng.integers(0, VOCAB_SIZE))}" if rng.random() < p_replace
                    else w for w in sentence]
        if len(sentence) > 1 and rng.random() < p_reorder:
            sentence[0], sentence[1] = sentence[1], sentence[0]
        out.extend(sentence)
    return out


def main():
    section("1. Three revision passes and their diminishing returns")
    words = DRAFT_WORDS
    print(f"SYNTHETIC draft: {DRAFT_WORDS} words, "
          f"{DRAFT_WORDS / WORDS_PER_SENTENCE:.0f} sentences at "
          f"{WORDS_PER_SENTENCE} words each")
    remaining = words
    for i, cut in enumerate(CUTS, start=1):
        removed = remaining * cut
        remaining -= removed
        print(f"  pass {i}: cut {cut * 100:4.0f} % = {removed:6.0f} words -> "
              f"{remaining:6.0f} words remain "
              f"({remaining / words * 100:5.1f} % of the draft), "
              f"{(removed / HOURS_PER_PASS):5.0f} words removed per hour")
    total_cut = words - remaining
    print(f"  total reduction = {total_cut:.0f} words "
          f"({total_cut / words * 100:.1f} % of the draft) in "
          f"{len(CUTS) * HOURS_PER_PASS:.0f} h")
    print(f"  words per hour, first pass {words * CUTS[0] / HOURS_PER_PASS:.0f}, "
          f"last pass {remaining * CUTS[-1] / (1 - CUTS[-1]) / HOURS_PER_PASS:.0f}")
    print("  -> the third pass removes a quarter of what the first did for the same")
    print("     effort; stop when the marginal cut stops changing the claim.")

    section("2. How much of the text actually changes: a sequence-similarity measure")
    draft = make_manuscript(DRAFT_WORDS // 2, RNG)
    final = revise(draft, RNG, P_REPLACE, P_DROP, P_REORDER)
    ratio = difflib.SequenceMatcher(None, draft, final).ratio()
    print(f"  words in the simulated draft  = {len(draft)}")
    print(f"  words in the simulated final  = {len(final)}")
    print(f"  sequence similarity (difflib ratio) = {ratio:.4f}")
    print(f"  fraction of the sequence changed = {(1 - ratio) * 100:.1f} %")
    print(f"  length change = {len(final) - len(draft):+d} words "
          f"({(len(final) - len(draft)) / len(draft) * 100:+.1f} %)")
    print(f"  chosen edit rates: replace {P_REPLACE * 100:.0f} %, drop "
          f"{P_DROP * 100:.0f} %, reorder {P_REORDER * 100:.0f} % of sentences")
    print("  -> a 'complete rewrite' that changes a fifth of the words still reads as")
    print("     the same paper; similarity is the measurable part of 'revision'.")

    section("3. Reviewer points: coverage of a response letter")
    total_points = sum(REVIEW_POINTS)
    print(f"  reviewer 1 raised {REVIEW_POINTS[0]} points, "
          f"reviewer 2 raised {REVIEW_POINTS[1]}; total {total_points}")
    for addressed in range(total_points + 1):
        coverage = addressed / total_points
        words_needed = addressed * 180
        print(f"  {addressed:2d} points addressed: coverage {coverage * 100:5.1f} %, "
              f"response length about {words_needed:4d} words "
              f"({words_needed / 250:.1f} pages at 250 words/page)")
    print("  each point costs about 180 words to address properly: state the point,")
    print("  what you changed, and where.")

    section("4. The cost of an unaddressed point")
    for addressed in (total_points, 6, 4, 0):
        unaddressed = total_points - addressed
        expected_reraise = unaddressed * P_RE_RAISE
        print(f"  {addressed} of {total_points} addressed -> {unaddressed} unaddressed, "
              f"expected re-raised in the next round = {expected_reraise:.1f}")
    print(f"  with P(re-raise) = {P_RE_RAISE:.2f}, each unaddressed point costs about")
    print("  another round of review, and a round is months of wall-clock time.")
    print("  -> addressing a point cheaply beats not addressing it expensively.")


if __name__ == "__main__":
    main()
