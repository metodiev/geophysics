#!/usr/bin/env python3
"""Academic careers: citation distributions, the h-index and its insensitivity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cv_and_career_demo.py

Everything here is SYNTHETIC.  The citation counts are generated from a chosen
distribution; no bibliometric database was queried and no real person's record is
used.

Sections
--------
1. A citation distribution and its inequality.
2. The h-index and what it is insensitive to.
3. Career length: how the metrics grow with years.
4. A hiring rubric and its sensitivity to weights.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_PAPERS = 60
MEDIAN_CITATIONS = 18.0
SIGMA_LOG_CITATIONS = 1.25
YEARS = (5, 10, 15, 20, 25)
PAPERS_PER_YEAR = 3.0
RUBRIC = {"publications": 0.30, "funding": 0.20, "teaching": 0.20,
          "service": 0.10, "fit": 0.20}
RUBRIC_ALT = {"publications": 0.20, "funding": 0.15, "teaching": 0.35,
              "service": 0.10, "fit": 0.20}


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def h_index(citations):
    c = np.sort(np.asarray(citations, dtype=float))[::-1]
    ranks = np.arange(1, c.size + 1)
    return int(np.max(np.where(c >= ranks)[0] + 1)) if np.any(c >= ranks) else 0


def gini(x):
    x = np.sort(np.asarray(x, dtype=float))
    n = x.size
    return float((2 * np.sum((np.arange(1, n + 1)) * x) - (n + 1) * np.sum(x))
                 / (n * np.sum(x)))


def main():
    citations = MEDIAN_CITATIONS * RNG.lognormal(0.0, SIGMA_LOG_CITATIONS, N_PAPERS)
    citations = np.round(citations).astype(int)

    section("1. A citation distribution and its inequality")
    print(f"SYNTHETIC record: {N_PAPERS} papers, lognormal citation counts with "
          f"median {MEDIAN_CITATIONS:.0f} and log-scale sd {SIGMA_LOG_CITATIONS:.2f}")
    total = int(citations.sum())
    print(f"  total citations = {total}")
    print(f"  mean per paper  = {citations.mean():.1f}; "
          f"median = {np.median(citations):.0f}")
    print(f"  ratio mean/median = {citations.mean() / np.median(citations):.2f}")
    top10 = int(np.ceil(0.10 * N_PAPERS))
    top_share = np.sort(citations)[::-1][:top10].sum() / total
    print(f"  top 10 % of papers ({top10} papers) hold {top_share * 100:.1f} % "
          f"of the citations")
    print(f"  papers with zero or one citation = "
          f"{int(np.sum(citations <= 1))} of {N_PAPERS} "
          f"({np.mean(citations <= 1) * 100:.1f} %)")
    print(f"  Gini coefficient = {gini(citations):.3f}")
    print("  -> citations are dominated by a minority of papers; any single-number")
    print("     summary of a record is a summary of that inequality.")

    section("2. The h-index and what it is insensitive to")
    h0 = h_index(citations)
    print(f"  h-index = {h0} (a record where {h0} papers have at least {h0} "
          f"citations each)")
    inflated = citations.copy()
    inflated[np.argmax(inflated)] += 100
    print(f"  adding 100 citations to the most-cited paper: h = {h_index(inflated)} "
          f"(unchanged)")
    spread = np.concatenate([citations, np.full(N_PAPERS, 5)])
    print(f"  adding {N_PAPERS} papers with 5 citations each (a doubling of volume): "
          f"h = {h_index(spread)} (unchanged), total citations = {int(spread.sum())}")
    doubled = np.concatenate([citations, citations])
    print(f"  duplicating every paper (the same work counted twice): "
          f"h = {h_index(doubled)} (up from {h0})")
    print(f"  ratio of h to the number of papers = {h0 / N_PAPERS:.3f}")
    print(f"  for comparison, total citations = {total}, and h^2 = {h0 ** 2} "
          f"({h0 ** 2 / total * 100:.0f} % of the total)")
    print("  -> h is insensitive to the very highly cited paper and sensitive to the")
    print("     mid-range; it measures a floor, not a peak or a sum.")

    section("3. Career length: how the metrics grow with years")
    print("  years   papers   h-index   h/sqrt(papers)   total citations   "
          "citations per paper")
    for years in YEARS:
        n = int(PAPERS_PER_YEAR * years)
        sample = MEDIAN_CITATIONS * RNG.lognormal(0.0, SIGMA_LOG_CITATIONS, n)
        sample = np.round(sample).astype(int)
        h = h_index(sample)
        print(f"  {years:5d} {n:8d} {h:9d} {h / np.sqrt(n):16.2f} "
              f"{int(sample.sum()):17d} {sample.mean():19.1f}")
    print(f"  with a constant publication rate of {PAPERS_PER_YEAR:.0f} papers per")
    print("  year, h grows roughly as the square root of the publication count for a")
    print("  lognormal citation distribution; the growth is sublinear in time.")
    print("  -> comparing h across career stages compares exposure time, not quality;")
    print("     divide by years or compare within a cohort.")

    section("4. A hiring rubric and its sensitivity to weights")
    rng = np.random.default_rng(7)
    n_candidates = 12
    criterion_scores = {k: np.clip(3.0 + 1.0 * rng.normal(0.0, 1.0, n_candidates),
                                  1.0, 5.0) for k in RUBRIC}
    for label, rubric in (("default", RUBRIC), ("teaching-weighted", RUBRIC_ALT)):
        total_score = sum(rubric[k] * criterion_scores[k] for k in rubric)
        order = np.argsort(-total_score)
        print(f"  ranking under the {label} rubric: "
              f"{[int(i) for i in order[:5]]}")
        print(f"    top score {total_score[order[0]]:.3f}, "
              f"score at rank 5 {total_score[order[4]]:.3f}, "
              f"last {total_score[order[-1]]:.3f}")
    default_score = sum(RUBRIC[k] * criterion_scores[k] for k in RUBRIC)
    alt_score = sum(RUBRIC_ALT[k] * criterion_scores[k] for k in RUBRIC_ALT)
    moved = int(np.sum(np.argsort(np.argsort(-default_score))
                       != np.argsort(np.argsort(-alt_score))))
    print(f"  candidates changing rank between the two rubrics = {moved} of "
          f"{n_candidates}")
    print(f"  largest single weight = {max(RUBRIC.values()):.2f} "
          f"(publications); least = {min(RUBRIC.values()):.2f} (service)")
    print("  -> as with proposals, the rubric is a policy choice; a candidate should")
    print("     know which criteria a department weights before preparing a case.")


if __name__ == "__main__":
    main()
