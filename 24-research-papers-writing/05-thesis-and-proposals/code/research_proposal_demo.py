#!/usr/bin/env python3
"""Research proposals: scoring, weighting and the sensitivity of a funding line.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_proposal_demo.py

Everything here is SYNTHETIC.  Proposals, criterion scores and the two weighting
schemes are generated with chosen parameters; no proposal or panel is analysed.

Sections
--------
1. The corpus and the criterion scores.
2. Ranking under two weighting schemes, and the proposals that flip.
3. The margin at the funding line.
4. The marginal value of one point on each criterion.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_PROPOSALS = 40
CRITERIA = ("novelty", "feasibility", "methods", "impact", "team")
WEIGHTS_SCIENCE = np.array([0.25, 0.25, 0.20, 0.20, 0.10])
WEIGHTS_IMPACT = np.array([0.15, 0.20, 0.20, 0.35, 0.10])
FUNDING_FRACTION = 0.25
SCORE_SD = 0.45            # per-criterion noise around the latent quality


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    latent = 3.0 + 0.9 * RNG.normal(0.0, 1.0, N_PROPOSALS)
    scores = np.clip(latent[:, None] + SCORE_SD * RNG.normal(0.0, 1.0,
                                                             (N_PROPOSALS, len(CRITERIA))),
                     1.0, 5.0)

    section("1. The corpus and the criterion scores")
    print(f"SYNTHETIC panel: {N_PROPOSALS} proposals, {len(CRITERIA)} criteria "
          f"scored 1-5 (half points not used)")
    print(f"  weights, science-led: "
          f"{dict(zip(CRITERIA, WEIGHTS_SCIENCE))}")
    print(f"  weights, impact-led : "
          f"{dict(zip(CRITERIA, WEIGHTS_IMPACT))}")
    print("  criterion        mean   sd   min   max")
    for j, name in enumerate(CRITERIA):
        col = scores[:, j]
        print(f"  {name:<15s} {col.mean():5.2f} {col.std(ddof=1):5.2f} "
              f"{col.min():5.1f} {col.max():5.1f}")
    print(f"  mean total score (science-led weights) = "
          f"{(scores @ WEIGHTS_SCIENCE).mean():.2f}")

    section("2. Ranking under two weighting schemes")
    score_science = scores @ WEIGHTS_SCIENCE
    score_impact = scores @ WEIGHTS_IMPACT
    n_fund = int(np.floor(FUNDING_FRACTION * N_PROPOSALS))
    funded_science = set(np.argsort(-score_science)[:n_fund])
    funded_impact = set(np.argsort(-score_impact)[:n_fund])
    flips = funded_science ^ funded_impact
    print(f"  funding line at the top {FUNDING_FRACTION * 100:.0f} % "
          f"= {n_fund} proposals")
    print(f"  proposals funded under both schemes = "
          f"{len(funded_science & funded_impact)} of {n_fund}")
    print(f"  proposals whose funded status flips = {len(flips)} "
          f"({len(flips) / n_fund * 100:.0f} % of the funded set)")
    print(f"  proposals entering the funded set under the impact-led scheme: "
          f"{sorted(int(i) for i in (funded_impact - funded_science))}")
    print(f"  proposals leaving it: "
          f"{sorted(int(i) for i in (funded_science - funded_impact))}")
    rank_corr = np.corrcoef(np.argsort(np.argsort(-score_science)),
                            np.argsort(np.argsort(-score_impact)))[0, 1]
    print(f"  Spearman rank correlation between the schemes = {rank_corr:.4f}")
    print("  -> the two schemes agree on most proposals and disagree exactly where the")
    print("     decision is made: a weighting scheme is a policy, not a technicality.")

    section("3. The margin at the funding line")
    order = np.argsort(-score_science)
    print("  rank   proposal   score (science-led)")
    for rank in range(max(0, n_fund - 2), min(N_PROPOSALS, n_fund + 2)):
        i = order[rank]
        mark = " <- last funded" if rank == n_fund - 1 else ""
        print(f"  {rank + 1:4d}   {i:8d}   {score_science[i]:.4f}{mark}")
    margin = score_science[order[n_fund - 1]] - score_science[order[n_fund]]
    print(f"  score gap at the line = {margin:.4f} points on a 5-point scale "
          f"({margin / 5 * 100:.2f} % of the range)")
    typical_shift = float(np.std(score_science - score_impact, ddof=1))
    print(f"  typical score shift between the two weightings = {typical_shift:.4f}")
    print(f"  ratio of the weighting shift to the decision margin = "
          f"{typical_shift / margin:.2f}x")
    print("  -> when the weighting shift exceeds the margin, the decision is set by the")
    print("     scheme rather than by the proposals.")

    section("4. The marginal value of one point on each criterion")
    print("  criterion        science-led weight   score gain per +1 point")
    for name, w in zip(CRITERIA, WEIGHTS_SCIENCE):
        print(f"  {name:<15s} {w:18.2f}   {w:22.2f}")
    print(f"  improving the least-weighted criterion by one point is worth "
          f"{WEIGHTS_SCIENCE.min():.2f} points; the most-weighted is worth "
          f"{WEIGHTS_SCIENCE.max():.2f}")
    print(f"  ratio = {WEIGHTS_SCIENCE.max() / WEIGHTS_SCIENCE.min():.1f}x")
    print("  -> a proposal should be improved on the criteria the panel weights most,")
    print("     which requires finding the scheme out before writing rather than after.")


if __name__ == "__main__":
    main()
