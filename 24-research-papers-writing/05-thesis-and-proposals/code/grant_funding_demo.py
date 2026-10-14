#!/usr/bin/env python3
"""Grant funding: success rates, review noise and the decision band.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grant_funding_demo.py

Everything here is SYNTHETIC.  Panel sizes, funding rates, reviewer noise, revision
gains and preparation costs are chosen teaching values; no funding scheme is
analysed.

Sections
--------
1. The scheme: applications, funding rate and the success boundary.
2. Review noise: how wide the band of uncertain decisions is.
3. Resubmission: expected submissions to one award.
4. Cost per funded project.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_APPLICATIONS = 400
N_PANEL_MEMBERS = 12
FUNDING_RATE = 0.20
REVIEW_NOISE_SD = 0.55        # per-reviewer score noise, on a 1-5 scale
QUALITY_SD = 0.75
DAY_PER_APPLICATION = 20.0    # days of work per application
P_FIRST = 0.12                # P(success) for a first submission
P_RESUBMIT = 0.22             # P(success) for a revised resubmission
BAND_Z = 1.645                # band defined at 90 %


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. The scheme: applications, funding rate and the boundary")
    quality = 3.5 + QUALITY_SD * RNG.normal(0.0, 1.0, N_APPLICATIONS)
    reviews = quality[:, None] + REVIEW_NOISE_SD * RNG.normal(
        0.0, 1.0, (N_APPLICATIONS, N_PANEL_MEMBERS))
    panel_score = reviews.mean(axis=1)
    n_funded = int(np.floor(FUNDING_RATE * N_APPLICATIONS))
    cutoff = np.sort(panel_score)[::-1][n_funded - 1]
    print(f"SYNTHETIC scheme: {N_APPLICATIONS} applications, {N_PANEL_MEMBERS} "
          f"reviews each, funding rate {FUNDING_RATE * 100:.0f} %")
    print(f"  true quality: mean {quality.mean():.2f} "
          f"+/- {quality.std(ddof=1):.2f} (1 s.d.)")
    print(f"  panel score: mean {panel_score.mean():.2f}, "
          f"sd {panel_score.std(ddof=1):.2f}")
    print(f"  funded = {n_funded}; score at the boundary = {cutoff:.4f}")
    print(f"  reviews per application = {N_PANEL_MEMBERS}; "
          f"total reviews = {N_APPLICATIONS * N_PANEL_MEMBERS}")
    se_of_mean = REVIEW_NOISE_SD / np.sqrt(N_PANEL_MEMBERS)
    print(f"  standard error of a panel mean = {REVIEW_NOISE_SD:.2f}/sqrt("
          f"{N_PANEL_MEMBERS}) = {se_of_mean:.4f}")
    print("  -> the boundary is a number on a noisy scale, and its position is set by")
    print("     the funding rate, not by the proposals.")

    section("2. Review noise: how wide the band of uncertain decisions is")
    band = BAND_Z * se_of_mean
    inside = np.abs(panel_score - cutoff) <= band
    print(f"  90 % band around the boundary = +/- {band:.4f} points")
    print(f"  applications inside the band = {int(inside.sum())} "
          f"({inside.mean() * 100:.1f} % of all applications)")
    print(f"  funded applications inside the band = "
          f"{int(np.sum(inside & (panel_score >= cutoff)))} of {n_funded}")
    print(f"  rejected applications inside the band = "
          f"{int(np.sum(inside & (panel_score < cutoff)))}")
    print(f"  rank correlation between true quality and panel score = "
          f"{np.corrcoef(quality, panel_score)[0, 1]:.4f}")
    print("  -> inside the band, the decision is closer to a coin toss than to a")
    print("     judgement; outside it, the panel is discriminating.")
    print(f"  with {N_PANEL_MEMBERS} reviewers the band is {band:.3f} points; "
          f"halving it needs {4 * N_PANEL_MEMBERS} reviewers")

    section("3. Resubmission: expected submissions to one award")
    print(f"  P(success) for a first submission    = {P_FIRST:.2f}")
    print(f"  P(success) for a revised resubmission = {P_RESUBMIT:.2f}")
    for p, label in ((P_FIRST, "first-submission rate always"),
                     (P_RESUBMIT, "revised resubmission rate always")):
        print(f"  expected submissions to one award, {label:<34s} = "
              f"{1 / p:5.1f}")
    combined = 1.0 / (P_FIRST + P_RESUBMIT) * 2
    print(f"  mixed scheme (first then revisions): expected submissions = "
          f"{combined:.1f}")
    print(f"  expected applications before a first award, at the observed overall rate "
          f"{FUNDING_RATE:.2f} = {1 / FUNDING_RATE:.1f}")
    print("  -> a 20 % funding rate means five applications per award on average, which")
    print("     is the number to plan a career and a workload against.")

    section("4. Cost per funded project")
    total_days = N_APPLICATIONS * DAY_PER_APPLICATION
    print(f"  effort = {N_APPLICATIONS} applications x {DAY_PER_APPLICATION:.0f} days "
          f"= {total_days:.0f} person-days")
    print(f"  per funded project = {total_days / n_funded:.0f} person-days of writing")
    print(f"  as person-years at 220 working days = "
          f"{total_days / n_funded / 220:.1f}")
    print(f"  the successful applications consume "
          f"{n_funded * DAY_PER_APPLICATION:.0f} days; the rest "
          f"({total_days - n_funded * DAY_PER_APPLICATION:.0f} days) is the cost of")
    print("  the process")
    print("  -> this is an argument for triage: a candidate who can predict the panel's")
    print("     decision should not spend twenty days on a proposal that will not be")
    print("     reviewed fairly, and should spend them on the resubmission instead.")


if __name__ == "__main__":
    main()
