#!/usr/bin/env python3
"""Public engagement and media: what survives compression and retelling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python public_and_media_demo.py

Everything here is SYNTHETIC.  The number of retelling steps, the loss rate per
step, the correction reach and the spin rate are chosen teaching values; no press
release, article or broadcast was analysed.

Sections
--------
1. Compression: from a paper to a press release to a headline.
2. Retelling: how qualifiers and numbers survive four steps.
3. Correction reach: what happens after the error is fixed.
4. Spin: what changes between the paper and the release.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
QUALIFIERS_IN_RELEASE = 6
QUALIFIER_LOSS_PER_STEP = 0.35
NUMBER_LOSS_PER_STEP = 0.20
N_STEPS = 4
RELEASE_WORDS = 250
HEADLINE_WORDS = 12
CORRECTION_REACH = 0.20
N_RELEASE_CLAIMS = 100
P_CAUSAL_ADDED = 0.22          # P(a causal verb added in the release or headline)
P_HEDGE_REMOVED = 0.31         # P(a hedge removed)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. Compression: from a paper to a press release to a headline")
    print(f"SYNTHETIC paper: 6000 words; press release: about {RELEASE_WORDS} words; "
          f"headline: about {HEADLINE_WORDS} words")
    print(f"  release retains {RELEASE_WORDS / 6000 * 100:.1f} % of the paper's words")
    print(f"  headline retains {HEADLINE_WORDS / 6000 * 100:.2f} % of the paper, and "
          f"{HEADLINE_WORDS / RELEASE_WORDS * 100:.1f} % of the release")
    print(f"  a 6000-word paper compressed to {HEADLINE_WORDS} words is a ratio of "
          f"{6000 // HEADLINE_WORDS}:1")
    print(f"  the uncertainty sentence of the abstract (~25 words) becomes "
          f"{25 * HEADLINE_WORDS / RELEASE_WORDS:.1f} words at headline density")
    print("  -> at that ratio, a sentence carries a claim or a caveat, never both.")
    print("     Decide in advance which sentence you would keep.")

    section("2. Retelling: how qualifiers and numbers survive four steps")
    print(f"  release contains {QUALIFIERS_IN_RELEASE} uncertainty qualifiers and "
          f"1 headline number")
    print("  steps completed   qualifiers surviving   number surviving   both survive")
    q = QUALIFIERS_IN_RELEASE
    p_number = 1.0
    for step in range(N_STEPS + 1):
        both = (q > 0) and (p_number > 0.5)
        print(f"  {step:15d}   {q:19.2f}   {p_number * 100:14.0f} %   "
              f"{'yes' if both else 'no'}")
        q *= (1.0 - QUALIFIER_LOSS_PER_STEP)
        p_number *= (1.0 - NUMBER_LOSS_PER_STEP)
    q_final = QUALIFIERS_IN_RELEASE * (1 - QUALIFIER_LOSS_PER_STEP) ** N_STEPS
    p_num_final = (1 - NUMBER_LOSS_PER_STEP) ** N_STEPS
    print(f"  survival after {N_STEPS} steps: qualifiers {q_final:.2f} of "
          f"{QUALIFIERS_IN_RELEASE}, number {p_num_final * 100:.1f} %")
    print(f"  a specific qualifier survives all steps with probability "
          f"{(1 - QUALIFIER_LOSS_PER_STEP) ** N_STEPS * 100:.1f} % each")
    print(f"  probability that both the number and at least one qualifier survive = "
          f"{p_num_final * (1 - (1 - (1 - QUALIFIER_LOSS_PER_STEP) ** N_STEPS) ** QUALIFIERS_IN_RELEASE) * 100:.1f} %")
    print("  -> put the caveat inside the claim sentence: a qualifier in a separate")
    print("     sentence is the first thing the retelling drops.")

    section("3. Correction reach: what happens after the error is fixed")
    print(f"  modelled correction reach = {CORRECTION_REACH * 100:.0f} % of the "
          f"original audience")
    for audience in (1000, 100000, 1000000):
        reached = audience * CORRECTION_REACH
        remaining = audience - reached
        print(f"  audience {audience:9d}: correction reaches {reached:9.0f}, "
              f"{remaining:9.0f} retain the original claim only")
    print("  ratio of people who see the correction to people who saw the error = "
          f"{CORRECTION_REACH:.2f}")
    print("  -> the error is the durable artefact, which is the practical argument")
    print("     for submitting the release to the scientist before publication, and")
    print("     for the strongest claim you can defend, not the most interesting one.")

    section("4. Spin: what changes between the paper and the release")
    causal_added = RNG.random(N_RELEASE_CLAIMS) < P_CAUSAL_ADDED
    hedge_removed = RNG.random(N_RELEASE_CLAIMS) < P_HEDGE_REMOVED
    either = causal_added | hedge_removed
    print(f"  synthetic corpus: {N_RELEASE_CLAIMS} claim pairs "
          f"(paper sentence, release sentence)")
    print(f"  causal verb added in the release      = {int(causal_added.sum())} "
          f"({causal_added.mean() * 100:.1f} %)")
    print(f"  hedge removed in the release          = {int(hedge_removed.sum())} "
          f"({hedge_removed.mean() * 100:.1f} %)")
    print(f"  both changes                          = "
          f"{int((causal_added & hedge_removed).sum())} "
          f"({(causal_added & hedge_removed).mean() * 100:.1f} %)")
    print(f"  at least one change (spin)            = {int(either.sum())} "
          f"({either.mean() * 100:.1f} %)")
    print(f"  claims unchanged                      = {int((~either).sum())} "
          f"({(~either).mean() * 100:.1f} %)")
    print("  -> spin is usually two small edits that compound: a stronger verb and a")
    print("     dropped hedge.  Both are checkable by comparing the two sentences")
    print("     side by side, which is a ten-minute task before publication and")
    print("     impossible afterwards.")


if __name__ == "__main__":
    main()
