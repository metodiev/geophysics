#!/usr/bin/env python3
"""Formulating answerable research questions: specificity and its consequences.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_questions_demo.py

Everything here is SYNTHETIC.  Questions are represented as four binary content
flags with chosen probabilities; no real research question is analysed.

Sections
--------
1. The four elements of an answerable question.
2. How many study designs a vague question is consistent with.
3. Two-rater agreement on a "falsifiable" judgement, with Cohen's kappa.
4. What specificity costs the reader in false starts.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_QUESTIONS = 400
ELEMENTS = {
    "measurable quantity": 0.82,
    "comparison or reference": 0.61,
    "stated scope (where/when)": 0.55,
    "mechanism or reason": 0.44,
}
RATER1_SENS = 0.88     # P(rater 1 says falsifiable | it is)
RATER1_SPEC = 0.85
RATER2_SENS = 0.85
RATER2_SPEC = 0.88
COST_PER_FALSE_START_DAYS = 14.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def kappa(a, b):
    """Cohen's kappa for two binary ratings."""
    po = float(np.mean(a == b))
    pa1, pb1 = float(a.mean()), float(b.mean())
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    return po, pe, (po - pe) / (1 - pe)


def main():
    elements = {name: RNG.random(N_QUESTIONS) < p for name, p in ELEMENTS.items()}
    n_present = np.sum([elements[name] for name in ELEMENTS], axis=0)

    section("1. The four elements of an answerable question")
    print(f"SYNTHETIC corpus: {N_QUESTIONS} question phrasings, four content elements")
    for name, p in ELEMENTS.items():
        print(f"  {name:<28s} chosen {p * 100:5.1f} %  measured "
              f"{elements[name].mean() * 100:5.1f} %  "
              f"({int(elements[name].sum())} / {N_QUESTIONS})")
    print(f"  mean number of elements present = {n_present.mean():.2f} of 4 "
          f"+/- {n_present.std(ddof=1):.2f}")
    answerable = (elements["measurable quantity"] & elements["comparison or reference"]
                  & elements["stated scope (where/when)"])
    print(f"  questions with quantity + comparison + scope = {int(answerable.sum())} "
          f"({answerable.mean() * 100:.1f} %)")
    print("  -> the mechanism element is the least common and the least necessary:")
    print("     answering 'why' is a result, not a prerequisite.")

    section("2. How many study designs a vague question is consistent with")
    # CHOSEN model: a question missing k of the four elements is consistent with
    # 2^k candidate designs, because each missing element can be resolved in a
    # direction that changes the design.
    designs = 2.0 ** (4 - n_present)
    print("  missing elements   questions   mean candidate designs")
    for missing in range(5):
        mask = (4 - n_present) == missing
        if mask.sum() == 0:
            continue
        print(f"  {missing}                  {int(mask.sum()):4d}       "
              f"{designs[mask].mean():8.1f}")
    print(f"  overall mean number of candidate designs = {designs.mean():.1f}")
    print(f"  median = {np.median(designs):.1f}, maximum = {designs.max():.0f}")
    print("  -> specificity does not restrict the science; it restricts the number of")
    print("     studies the sentence could be describing, which is what makes a")
    print("     proposal reviewable.")

    section("3. Two-rater agreement on a 'falsifiable' judgement")
    is_falsifiable = answerable
    r1 = np.where(is_falsifiable, RNG.random(N_QUESTIONS) < RATER1_SENS,
                  RNG.random(N_QUESTIONS) < (1 - RATER1_SPEC))
    r2 = np.where(is_falsifiable, RNG.random(N_QUESTIONS) < RATER2_SENS,
                  RNG.random(N_QUESTIONS) < (1 - RATER2_SPEC))
    po, pe, k = kappa(r1, r2)
    perfect = kappa(is_falsifiable, is_falsifiable)
    print(f"  truth: {int(is_falsifiable.sum())} of {N_QUESTIONS} are fully specified "
          f"({is_falsifiable.mean() * 100:.1f} %)")
    print(f"  rater 1 says falsifiable: {r1.mean() * 100:.1f} %; "
          f"rater 2: {r2.mean() * 100:.1f} %")
    print(f"  observed agreement P_o = {po:.4f}")
    print(f"  chance agreement    P_e = {pe:.4f}")
    print(f"  Cohen's kappa          = {k:.4f}")
    print(f"  kappa of a perfect rater against itself = {perfect[2]:.4f} (the ceiling)")
    print(f"  kappa between rater 1 and the truth     = "
          f"{kappa(r1, is_falsifiable)[2]:.4f}")
    print("  -> kappa near " f"{k:.2f} is modest agreement; a coding protocol with")
    print("     worked examples is what lifts it, not more raters.")

    section("4. What specificity costs the reader in false starts")
    print(f"  modelled cost of resolving one candidate design = "
          f"{COST_PER_FALSE_START_DAYS:.0f} days")
    print(f"  expected false-start effort per question = "
          f"{(designs.mean() - 1.0) * COST_PER_FALSE_START_DAYS:.1f} days")
    for target in (1.0, 1.5, 2.0):
        print(f"  to reach a mean of {target:.1f} candidate designs the question must "
              f"specify "
              f"{np.ceil(4 - np.log2(target)):.0f} of the 4 elements")
    print("  -> writing one more clause into the question is worth about two weeks of")
    print("     misdirected work per unresolved element.")


if __name__ == "__main__":
    main()
