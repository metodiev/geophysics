#!/usr/bin/env python3
"""Abstracts and titles: what a fixed word budget can carry.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python writing_abstracts_titles_demo.py

Everything here is SYNTHETIC.  Abstracts and titles are modelled as sets of
binary content flags and token counts; no abstract is read or reproduced.

Sections
--------
1. Abstract length and the effect of a hard word limit.
2. Content flags: what an abstract states, and how structure changes it.
3. Hedging and spin: claim strength against the reported result.
4. Titles: concreteness scores and the vague-title rate.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_ABSTRACTS = 400
MEAN_TOKENS = 248.0
SD_TOKENS = 44.0
WORD_LIMIT = 250
P_STRUCTURED = 0.60
# P(flag | abstract is structured), P(flag | unstructured)
FLAGS = {
    "context": (0.92, 0.88),
    "gap": (0.55, 0.41),
    "method": (0.95, 0.71),
    "quantitative result": (0.86, 0.69),
    "uncertainty": (0.52, 0.34),
    "implication": (0.88, 0.79),
}
P_FORGETS_UNCERTAINTY_IF_NOT_SIGNIFICANT = 0.35
TITLE_FLAGS = {
    "names the object": 0.91,
    "names the method": 0.74,
    "names the region or setting": 0.68,
    "states the scope or scale": 0.39,
}


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    tokens = RNG.normal(MEAN_TOKENS, SD_TOKENS, N_ABSTRACTS).clip(120.0, 420.0)
    structured = RNG.random(N_ABSTRACTS) < P_STRUCTURED

    section("1. Abstract length and the effect of a hard word limit")
    print(f"SYNTHETIC abstracts: {N_ABSTRACTS}, mean {tokens.mean():.0f} tokens "
          f"+/- {tokens.std(ddof=1):.0f}")
    print(f"  median length = {np.median(tokens):.0f} tokens; "
          f"90th percentile = {np.percentile(tokens, 90):.0f}")
    over = tokens > WORD_LIMIT
    print(f"  longer than the {WORD_LIMIT}-word limit = {int(over.sum())} "
          f"({over.mean() * 100:.1f} %)")
    excess = float(np.sum(tokens[over] - WORD_LIMIT))
    print(f"  total excess words to cut = {excess:.0f} "
          f"(mean {excess / max(over.sum(), 1):.0f} words per over-length abstract)")
    print(f"  length if truncated naively at {WORD_LIMIT}: "
          f"{tokens.clip(max=float(WORD_LIMIT)).mean():.0f} tokens")
    print("  -> a limit is a budget: cutting the tail of every sentence costs more")
    print("     information than cutting one whole sentence.")

    section("2. Content flags: what an abstract states, and how structure changes it")
    flags = {name: np.where(structured, p_s, p_u) for name, (p_s, p_u) in FLAGS.items()}
    stated = {name: RNG.random(N_ABSTRACTS) < p for name, p in flags.items()}
    print("  content flag             structured   unstructured   difference")
    for name in FLAGS:
        a = stated[name][structured].mean()
        b = stated[name][~structured].mean()
        print(f"  {name:<24s} {a * 100:8.1f} %  {b * 100:10.1f} %  "
              f"{(a - b) * 100:+8.1f} pp")
    score = np.mean([stated[name] for name in FLAGS], axis=0)
    print(f"  content score (0-1) = {score.mean():.3f} +/- {score.std(ddof=1):.3f}")
    print(f"  structured abstracts   = {score[structured].mean():.3f}")
    print(f"  unstructured abstracts = {score[~structured].mean():.3f}")
    print(f"  difference = {(score[structured].mean() - score[~structured].mean()) * 100:+.1f} "
          f"percentage points of content score")
    print("  -> structure forces the author to answer a fixed list of questions;")
    print("     its measured effect here is a few points, not a transformation.")

    section("3. Hedging and spin: claim strength against the reported result")
    significant = RNG.random(N_ABSTRACTS) < 0.72
    states_uncertainty = stated["uncertainty"] & ~(
        (~significant) & (RNG.random(N_ABSTRACTS) < P_FORGETS_UNCERTAINTY_IF_NOT_SIGNIFICANT))
    print(f"  abstracts reporting a significant result = {significant.mean() * 100:.1f} %")
    print(f"  abstracts stating uncertainty, all       = "
          f"{stated['uncertainty'].mean() * 100:.1f} %")
    print(f"  abstracts stating uncertainty, after spin = "
          f"{states_uncertainty.mean() * 100:.1f} %")
    print(f"  non-significant abstracts that omit any uncertainty language = "
          f"{np.mean((~significant) & (~states_uncertainty)) * 100:.1f} %")
    print(f"  ratio of uncertainty language, significant vs not = "
          f"{states_uncertainty[significant].mean() / states_uncertainty[~significant].mean():.2f}")
    print("  -> uncertainty language is not distributed evenly: it appears where it")
    print("     is least needed and disappears where it matters most.")

    section("4. Titles: concreteness scores and the vague-title rate")
    title_flags = {name: RNG.random(N_ABSTRACTS) < p for name, p in TITLE_FLAGS.items()}
    tscore = np.mean([title_flags[name] for name in TITLE_FLAGS], axis=0)
    print("  title element                  present in")
    for name, p in TITLE_FLAGS.items():
        print(f"  {name:<30s} {title_flags[name].mean() * 100:6.1f} % of titles")
    print(f"  mean concreteness score = {tscore.mean():.3f} "
          f"+/- {tscore.std(ddof=1):.3f}")
    complete = np.all([title_flags[name] for name in TITLE_FLAGS], axis=0)
    vague = ~np.any([title_flags[name] for name in TITLE_FLAGS], axis=0)
    print(f"  titles naming all four elements = {complete.mean() * 100:.1f} %")
    print(f"  titles naming none of them      = {vague.mean() * 100:.1f} %")
    print(f"  titles naming the object but not the method = "
          f"{np.mean(title_flags['names the object'] & ~title_flags['names the method']) * 100:.1f} %")
    print("  -> a title that names object, method and scope is retrievable by a")
    print("     reader who has not yet read the abstract; the rest are advertisements.")


if __name__ == "__main__":
    main()
