#!/usr/bin/env python3
"""Peer review: reviewer agreement, aggregation and the effect of one outlier.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python peer_review_practice_demo.py

Everything here is SYNTHETIC.  Proposals, qualities, reviewer biases and noise are
generated with chosen parameters; no real review data exist in this repository.

Sections
--------
1. The review panel: scores, spread and reviewer bias.
2. How much of the score variance is between proposals, and how much between reviewers.
3. Aggregation: means, ranks and the effect of one harsh reviewer.
4. Ranking stability under reviewer-normalised scores.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC panel parameters (chosen teaching values) --------------------
N_PROPOSALS = 40
N_REVIEWERS = 4
QUALITY_SD = 0.8            # sd of true quality on the 1-5 score scale
REVIEWER_BIAS = np.array([-0.45, 0.10, 0.35, -0.10])   # additive, chosen
REVIEW_NOISE_SD = 0.55      # within-reviewer noise
FUNDING_FRACTION = 0.25     # top quartile funded


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def spearman(a, b):
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def main():
    quality = 3.0 + QUALITY_SD * RNG.normal(0.0, 1.0, N_PROPOSALS)
    scores = (quality[:, None] + REVIEWER_BIAS[None, :]
              + REVIEW_NOISE_SD * RNG.normal(0.0, 1.0, (N_PROPOSALS, N_REVIEWERS)))
    scores = np.clip(np.round(scores * 2) / 2, 1.0, 5.0)   # half-point step

    section("1. The review panel: scores and reviewer bias")
    print(f"SYNTHETIC panel: {N_PROPOSALS} proposals, {N_REVIEWERS} reviewers each, "
          f"1-5 scale (half-point steps)")
    print(f"  true quality: mean {quality.mean():.2f} +/- {quality.std(ddof=1):.2f} "
          f"(1 s.d. across proposals)")
    for j in range(N_REVIEWERS):
        print(f"  reviewer {j + 1}: mean score {scores[:, j].mean():.2f} "
              f"(bias {REVIEWER_BIAS[j]:+.2f}), sd {scores[:, j].std(ddof=1):.2f}")
    per_proposal_sd = scores.std(axis=1, ddof=1)
    spread = scores.max(axis=1) - scores.min(axis=1)
    print(f"  mean within-proposal spread (sd across the {N_REVIEWERS} reviewers) = "
          f"{per_proposal_sd.mean():.2f} points")
    print(f"  mean range within a proposal = {spread.mean():.2f} points")
    print(f"  proposals where two reviewers differ by >= 2 points = "
          f"{int(np.sum(spread >= 2.0))} of {N_PROPOSALS} "
          f"({np.mean(spread >= 2.0) * 100:.1f} %)")

    section("2. Variance decomposition: proposals versus reviewers")
    grand = scores.mean()
    ss_between = N_REVIEWERS * float(np.sum((scores.mean(axis=1) - grand) ** 2))
    ss_within = float(np.sum((scores - scores.mean(axis=1, keepdims=True)) ** 2))
    ms_between = ss_between / (N_PROPOSALS - 1)
    ms_within = ss_within / (N_PROPOSALS * (N_REVIEWERS - 1))
    icc = (ms_between - ms_within) / (ms_between + (N_REVIEWERS - 1) * ms_within)
    print(f"  mean square between proposals = {ms_between:.3f}")
    print(f"  mean square within proposals  = {ms_within:.3f}")
    print(f"  intraclass correlation ICC(1) = {icc:.3f}")
    print(f"  so {icc * 100:.1f} % of the score variance is attributable to the")
    print(f"  proposal and {(1 - icc) * 100:.1f} % to reviewers and noise")
    print("  -> with ICC = 1 the panel agrees perfectly; with ICC = 0 the score is")
    print("     reviewer opinion.  Averaging more reviewers raises the aggregate's")
    print("     reliability by the Spearman-Brown relation, not the ICC.")

    section("3. Aggregation: means, ranks and the effect of one harsh reviewer")
    mean_all = scores.mean(axis=1)
    harshest = int(np.argmin(REVIEWER_BIAS))
    mean_drop = np.delete(scores, harshest, axis=1).mean(axis=1)
    n_fund = int(np.floor(FUNDING_FRACTION * N_PROPOSALS))
    funded_all = set(np.argsort(-mean_all)[:n_fund])
    funded_drop = set(np.argsort(-mean_drop)[:n_fund])
    print(f"  dropping reviewer {harshest + 1} (mean bias {REVIEWER_BIAS[harshest]:+.2f})")
    print(f"  mean score shift across proposals = "
          f"{(mean_drop - mean_all).mean():+.3f} points")
    print(f"  proposals funded in both rankings = {len(funded_all & funded_drop)} of "
          f"{n_fund}")
    print(f"  proposals whose funded status flips = "
          f"{len(funded_all ^ funded_drop)}")
    print(f"  Spearman rank correlation, all four vs three reviewers = "
          f"{spearman(mean_all, mean_drop):.4f}")
    print("  -> the panel mean is robust in rank but not in level: the funding line")
    print("     moves with the composition of the panel.")

    section("4. Ranking stability under reviewer-normalised scores")
    z = (scores - scores.mean(axis=0, keepdims=True)) / scores.std(axis=0, ddof=1,
                                                                  keepdims=True)
    mean_z = z.mean(axis=1)
    print(f"  Spearman correlation, raw means vs reviewer-normalised means = "
          f"{spearman(mean_all, mean_z):.4f}")
    decile_raw = np.argsort(np.argsort(-mean_all)) // max(1, N_PROPOSALS // 10)
    decile_z = np.argsort(np.argsort(-mean_z)) // max(1, N_PROPOSALS // 10)
    moved = int(np.sum(decile_raw != decile_z))
    print(f"  proposals changing decile after normalisation = {moved} of "
          f"{N_PROPOSALS} ({moved / N_PROPOSALS * 100:.1f} %)")
    print(f"  reviewer means after normalisation = "
          f"{np.round(z.mean(axis=0), 4)}")
    print("  -> normalisation removes level differences between reviewers; it cannot")
    print("     remove differences in how they read the same proposal.")


if __name__ == "__main__":
    main()
