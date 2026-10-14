#!/usr/bin/env python3
"""Seminars, qualifying exams and thesis defence: coverage and timing.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seminar_and_defence_demo.py

Everything here is SYNTHETIC.  Question areas, their weights, the preparation curve
and the answer timings are chosen teaching values; no exam was observed.

Sections
--------
1. The question space: eight areas and the questions worth preparing.
2. Coverage from a preparation set, and its diminishing returns.
3. Timing: how many questions fit in a defence.
4. The risk that remains: what the preparation does not cover.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
AREAS = (
    ("motivation and context", 0.10),
    ("method choice", 0.18),
    ("data and sampling", 0.15),
    ("uncertainty and error", 0.14),
    ("assumptions and limitations", 0.16),
    ("alternatives and competitors", 0.11),
    ("reproducibility and code", 0.08),
    ("significance and implications", 0.08),
)
N_PREPARED_QUESTIONS = 24
N_LIKELY_QUESTIONS = 60
DEFENCE_MINUTES = 45.0
TALK_MINUTES = 15.0
QUICK_ANSWER_MIN = 1.5
TYPICAL_ANSWER_MIN = 3.5
LONG_ANSWER_MIN = 5.0


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. The question space: eight areas and their weights")
    weights = np.array([w for _, w in AREAS])
    print(f"SYNTHETIC model: {N_LIKELY_QUESTIONS} plausible questions across "
          f"{len(AREAS)} areas")
    print(f"  total weight = {weights.sum():.2f}")
    print("  area                        weight   questions per defence")
    for name, w in AREAS:
        print(f"  {name:<27s} {w * 100:5.1f} % {w * N_LIKELY_QUESTIONS / 8:12.1f}")
    hardest = max(AREAS, key=lambda item: item[1])
    print(f"  largest area: {hardest[0]} ({hardest[1] * 100:.0f} % of likely questions)")
    print("  -> preparation should be proportional to weight, not to comfort: the")
    print("     areas you can talk about are usually not the ones you will be asked.")

    section("2. Coverage from a preparation set, and its diminishing returns")
    print("  prepared questions   area coverage (modelled 1 - exp(-n/12))")
    for n in (4, 8, 12, 16, 20, 24, 32, 48):
        coverage = 1.0 - np.exp(-n / 12.0)
        print(f"  {n:18d}   {coverage * 100:28.1f} %")
    coverage_24 = 1.0 - np.exp(-N_PREPARED_QUESTIONS / 12.0)
    print(f"  at {N_PREPARED_QUESTIONS} prepared questions coverage is "
          f"{coverage_24 * 100:.1f} %; going to {2 * N_PREPARED_QUESTIONS} adds only "
          f"{(1 - np.exp(-2 * N_PREPARED_QUESTIONS / 12)) * 100 - coverage_24 * 100:.1f} "
          f"percentage points")
    print("  -> prepare answers by area, not by question: the tenth question in an")
    print("     area teaches almost nothing new, the first two teach most of it.")

    section("3. Timing: how many questions fit in a defence")
    question_minutes = DEFENCE_MINUTES - TALK_MINUTES
    print(f"  defence {DEFENCE_MINUTES:.0f} min = {TALK_MINUTES:.0f} min talk + "
          f"{question_minutes:.0f} min questions")
    for label, per_answer in (("quick answers", QUICK_ANSWER_MIN),
                              ("typical answers", TYPICAL_ANSWER_MIN),
                              ("long answers", LONG_ANSWER_MIN)):
        spoken = question_minutes * 130.0
        print(f"  {label:<16s} at {per_answer:.1f} min each -> "
              f"{question_minutes / per_answer:4.1f} questions answered, "
              f"{spoken:.0f} words of talking either way")
    print(f"  at typical pace the panel asks {question_minutes / TYPICAL_ANSWER_MIN:.0f} "
          f"questions; the examiners know this and allocate their questions")
    print("  -> practising short answers raises the number of questions you can")
    print("     answer well from "
          f"{question_minutes / LONG_ANSWER_MIN:.0f} to "
          f"{question_minutes / TYPICAL_ANSWER_MIN:.0f}.")

    section("4. The risk that remains: what preparation does not cover")
    rng = RNG
    draws = rng.choice(len(AREAS), size=8, p=weights)
    asked = np.bincount(draws, minlength=len(AREAS))
    print("  a simulated panel of 8 questions drawn from the area weights:")
    for i, (name, _) in enumerate(AREAS):
        print(f"    {name:<27s} {int(asked[i])} question(s)")
    uncovered = [AREAS[i][0] for i in range(len(AREAS)) if asked[i] > 0 and i >= 6]
    print(f"  areas asked that are often under-prepared: {uncovered}")
    p_any_rare = 1.0 - (1.0 - (AREAS[6][1] + AREAS[7][1])) ** 8
    print(f"  probability that at least one of the two least-prepared areas appears in "
          f"8 questions = {p_any_rare * 100:.1f} %")
    print("  -> the low-weight areas are not negligible at the scale of one defence;")
    print("     two prepared sentences per area remove most of the exposure.")


if __name__ == "__main__":
    main()
