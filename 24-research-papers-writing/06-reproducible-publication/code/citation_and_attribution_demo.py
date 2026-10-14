#!/usr/bin/env python3
"""Citation practice and attribution: distributions, indices and the software gap.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python citation_and_attribution_demo.py

Everything here is SYNTHETIC.  Citation counts are drawn from a chosen distribution
and the attribution rates are chosen teaching values; no bibliometric database was
queried and no real paper, dataset or software package is described.

Sections
--------
1. The citation distribution: centre, spread and inequality.
2. A power-law slope from the complementary cumulative distribution.
3. Credit for data and software: what is cited and what is used.
4. The allocation question: how much credit an uncited dependency loses.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_PAPERS = 800
MEDIAN_CITATIONS = 12.0
SIGMA_LOG = 1.30
P_CITES_DATA = 0.42          # P(a paper formally cites the dataset it uses)
P_CITES_SOFTWARE = 0.35      # P(a paper formally cites the software it uses)
SOFTWARE_CITATION_RATIO = 0.25  # software-paper citations relative to a method paper


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def gini(x):
    x = np.sort(np.asarray(x, dtype=float))
    n = x.size
    return float((2 * np.sum(np.arange(1, n + 1) * x) - (n + 1) * np.sum(x))
                 / (n * np.sum(x)))


def main():
    citations = np.round(MEDIAN_CITATIONS * RNG.lognormal(0.0, SIGMA_LOG, N_PAPERS))
    citations = np.maximum(citations, 0).astype(int)

    section("1. The citation distribution: centre, spread and inequality")
    print(f"SYNTHETIC corpus: {N_PAPERS} papers, lognormal citation counts, "
          f"median {MEDIAN_CITATIONS:.0f}, log-scale sd {SIGMA_LOG:.2f}")
    print(f"  mean citations   = {citations.mean():.1f}")
    print(f"  median citations = {np.median(citations):.0f}")
    print(f"  ratio mean/median = {citations.mean() / np.median(citations):.2f}")
    print(f"  standard deviation = {citations.std(ddof=1):.1f}")
    top10 = int(np.ceil(0.10 * N_PAPERS))
    top_share = np.sort(citations)[::-1][:top10].sum() / citations.sum()
    print(f"  top 10 % of papers hold {top_share * 100:.1f} % of the citations")
    print(f"  papers with no citations = {int(np.sum(citations == 0))} "
          f"({np.mean(citations == 0) * 100:.1f} %)")
    print(f"  Gini coefficient = {gini(citations):.3f}")
    print("  -> citation counts are heavy-tailed: the mean describes no paper, and the")
    print("     shape of the tail is the phenomenon, not a nuisance.")

    section("2. A power-law slope from the complementary cumulative distribution")
    c = np.sort(citations[citations > 0])
    ccdf = 1.0 - np.arange(len(c)) / len(c)
    x = np.log(c)
    y = np.log(ccdf)
    slope, intercept = np.polyfit(x, y, 1)
    # A CCDF of the form C x^(-alpha+1) gives slope = -(alpha - 1).
    alpha = -slope + 1.0
    print(f"  papers with at least one citation: {len(c)}")
    print(f"  log-log CCDF fit: slope = {slope:.3f}, intercept = {intercept:.3f}")
    print(f"  implied exponent alpha = -slope + 1 = {alpha:.3f}")
    print(f"  fit over the range {c.min()} to {c.max()} citations")
    print("  -> the exponent is an estimate from one generated sample, not a law: a")
    print("     lognormal with this spread is not exactly a power law, and the fit")
    print("     changes if the smallest counts are excluded.  Report the range and the")
    print("     model, and do not treat the exponent as a universal constant.")

    section("3. Credit for data and software: what is cited and what is used")
    uses_data = RNG.random(N_PAPERS) < 0.85
    cites_data = uses_data & (RNG.random(N_PAPERS) < P_CITES_DATA)
    uses_software = RNG.random(N_PAPERS) < 0.95
    cites_software = uses_software & (RNG.random(N_PAPERS) < P_CITES_SOFTWARE)
    print(f"  papers using a dataset: {int(uses_data.sum())}; of those, formally")
    print(f"    citing it = {int(cites_data.sum())} "
          f"({cites_data.sum() / max(uses_data.sum(), 1) * 100:.1f} %)")
    print(f"  papers using software: {int(uses_software.sum())}; of those, formally")
    print(f"    citing it = {int(cites_software.sum())} "
          f"({cites_software.sum() / max(uses_software.sum(), 1) * 100:.1f} %)")
    print(f"  data attribution gap = "
          f"{int(uses_data.sum()) - int(cites_data.sum())} uses without a traceable")
    print(f"  citation; the software gap is {int(uses_software.sum()) - int(cites_software.sum())}")
    print(f"  modelled citations of a software paper relative to a method paper = "
          f"{SOFTWARE_CITATION_RATIO:.2f}x")
    print("  -> use without citation is the norm for infrastructure, which is why")
    print("     explicit citation practices (and persistent identifiers) matter for")
    print("     the people who maintain data and code.")

    section("4. The allocation question: how much credit an uncited dependency loses")
    mean_citations = citations.mean()
    total = citations.sum()
    print(f"  mean citations per paper = {mean_citations:.1f}, total = {int(total)}")
    for label, p_cite, ratio in (("software", P_CITES_SOFTWARE, SOFTWARE_CITATION_RATIO),
                                 ("data", P_CITES_DATA, 1.0)):
        attributed = N_PAPERS * p_cite * mean_citations * ratio
        informal = N_PAPERS * (1 - p_cite) * mean_citations * ratio
        print(f"  {label:<9s} credited citations = {attributed:8.0f} "
              f"({attributed / total * 100:5.2f} % of the corpus total); "
              f"uncredited = {informal:8.0f}")
    print("  -> the numbers are chosen, the mechanism is not: a dependency that is used")
    print("     but never cited accumulates no visible credit, and the omission is")
    print("     invisible in every citation index built from the literature.")


if __name__ == "__main__":
    main()
