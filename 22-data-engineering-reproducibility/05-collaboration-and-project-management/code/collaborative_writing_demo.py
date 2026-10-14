#!/usr/bin/env python3
"""Collaborative writing: conflict rates in prose and LaTeX, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python collaborative_writing_demo.py

Everything here is SYNTHETIC.  The documents and their edits are generated with chosen
parameters; the conflict model is the line-overlap model of the version-control
lesson applied to a manuscript.  No real manuscript was parsed.

Sections
--------
1. Two manuscripts and their diff sizes: prose paragraphs against one sentence per line.
2. Conflict probability versus how far apart two edits are.
3. Concurrent editors: the probability that a given editing session conflicts.
4. Formatting choices that change the conflict rate, and their cost.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC manuscript model (chosen, not measured) ----------------------
WORDS = 8000               # words in the manuscript
WORDS_PER_LINE = 12        # wrapped paragraphs
CONTEXT = 3                # diff context lines
TRIALS = 20000
N_EDITORS = 4


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def conflict_probability(separation, context, edit_lines, trials, rng):
    a_len = np.clip(rng.poisson(edit_lines, size=trials), 1, None)
    a_start = rng.integers(0, 10_000, size=trials)
    gap = (a_start + separation) - (a_start + a_len)
    return float((gap <= 2 * context).mean())


def main():
    section("1. Two manuscripts and their diff sizes")
    paragraphs = WORDS / 120.0                       # ~120 words per paragraph
    lines_wrapped = WORDS / WORDS_PER_LINE
    lines_sentence = WORDS / 18.0                    # ~18 words per sentence
    print(f"SYNTHETIC manuscript: {WORDS} words (chosen)")
    print(f"  hard-wrapped paragraphs : {lines_wrapped:>7.0f} lines "
          f"({paragraphs:.0f} paragraphs)")
    print(f"  one sentence per line   : {lines_sentence:>7.0f} lines")
    print(f"  ratio of diff sizes     = "
          f"{lines_sentence / lines_wrapped:.2f}x")
    print("  -> a line-based merge sees a rewrapped paragraph as a whole-line")
    print("     change; sentence-per-line makes the same edit local")

    section("2. Conflict probability versus separation")
    print("  separation (lines) | wrapped prose | sentence per line")
    for sep in (0, 5, 10, 20, 40):
        p_wrapped = conflict_probability(sep, CONTEXT, 6, TRIALS, RNG)
        p_sentence = conflict_probability(sep, CONTEXT, 1.5, TRIALS, RNG)
        print(f"  {sep:>18d} | {p_wrapped:>13.3f} | {p_sentence:>17.3f}")
    print("  -> sentence-per-line shortens the edit region, so two edits conflict")
    print("     over a much smaller distance; neither format is 'better', but the")
    print("     conflict rate is a consequence of the format")

    section("3. Concurrent editors")
    print(f"  {N_EDITORS} editors, {WORDS} words, two sessions per week each")
    sessions = N_EDITORS * 2
    print("  separation (lines) | pairwise P | P(a session conflicts with any)")
    for sep in (5, 10, 20, 50):
        p_pair = conflict_probability(sep, CONTEXT, 6, TRIALS, RNG)
        p_any = 1.0 - (1.0 - p_pair) ** (sessions - 1)
        print(f"  {sep:>18d} | {p_pair:>10.3f} | {p_any:>31.3f}")
    print("  -> conflict is a function of proximity, not of the number of editors:")
    print("     just beyond one edit length it is negligible, and just inside it is")
    print("     near-certain. The lever is the edit region's size, not the tool")

    section("4. Formatting choices and their cost")
    rows = [
        ("one sentence per line", "fewer, smaller conflicts",
         "diffs are noisier to read in a browser"),
        ("semantic line breaks", "sections stay reviewable",
         "an unfamiliar convention for co-authors"),
        ("one file per section", "conflicts are rare",
         "cross-references need care; fewer whole-document tools"),
        ("track changes in a word processor", "reviewer comfort",
         "not versionable, not mergeable, no reproducible history"),
    ]
    print("  choice                        | benefit               | cost")
    for name, benefit, cost in rows:
        print(f"  {name:<29} | {benefit:<21} | {cost}")
    print("  -> choose the format for the merge behaviour the team can maintain,")
    print("     and write the convention in the repository's contribution notes")


if __name__ == "__main__":
    main()
