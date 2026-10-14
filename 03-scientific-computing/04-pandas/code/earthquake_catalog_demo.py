"""Case study: earthquake-catalogue wrangling (magnitude-frequency).

Run:  .venv/bin/python 03-scientific-computing/04-pandas/code/earthquake_catalog_demo.py
Requires: pandas (installed in the project venv).

Companion to lesson 03-04-06.

.. warning::

   **The catalogue used here is SYNTHETIC.**  It is generated in-code by
   ``synthetic_catalog.py`` and is not the USGS catalogue, not the ISC
   bulletin, and not any observation of the Earth.  The generator's input
   b-value is 1.05.  Every b-value computed below is therefore an *illustration
   of the calculation*, and a check that pandas recovers the known input --
   **it is not a geophysical result and must never be quoted as one.**

The workflow: clean -> choose a completeness magnitude -> build the cumulative
magnitude-frequency relation -> estimate b by maximum likelihood and by least
squares -> report the sensitivity to the completeness choice -> summarise rate.

Demonstrates:

1. Cleaning through the lesson-03 policy, with the row counts reported.
2. ``pd.cut`` for a binned magnitude histogram.
3. A cumulative count as an aggregation, not a loop.
4. Two independent b-value estimators and their disagreement.
5. The dominant uncertainty: the completeness magnitude, not the fit.
6. A CSV round trip through ``io.StringIO`` (no file written).
"""

from __future__ import annotations

import io

import numpy as np
import pandas as pd

import synthetic_catalog as sc


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def b_aki_utsu(mags: pd.Series, mc: float, dm: float = 0.1) -> float:
    """Maximum-likelihood b-value (Aki 1965; Utsu 1965), binned form.

    ``b = log10(e) / (mean(M) - (Mc - dm/2))``, where ``dm`` is the magnitude
    bin width the catalogue is rounded to.
    """
    m = mags[mags >= mc]
    return float(np.log10(np.e) / (m.mean() - (mc - dm / 2.0)))


def b_least_squares(mags: pd.Series, mc: float) -> tuple[float, int]:
    """Least-squares slope of log10 N(>=M) against M for M >= mc."""
    m = mags[mags >= mc]
    grid = np.round(np.arange(mc, m.max() + 0.05, 0.1), 2)
    counts = np.array([int((m >= g).sum()) for g in grid], dtype=float)
    keep = counts > 0
    x, y = grid[keep], np.log10(counts[keep])
    slope, intercept = np.polyfit(x, y, 1)
    return float(-slope), len(grid)


def main():
    print("SYNTHETIC catalogue: generated in-code, not an observation of the")
    print("Earth and not the USGS catalogue.  See synthetic_catalog.py.")
    print(f"Generator input b-value: {sc.B_VALUE_INPUT}; "
          f"completeness input: M >= {sc.M_MIN}.")
    print("Any b-value below is an illustration and a software check, not a")
    print("result about the Earth.")

    section("1. Cleaning, with the row counts reported")
    raw = sc.raw_catalog()
    clean = sc.clean_catalog()
    print(f"  raw rows    : {len(raw)}")
    print(f"  clean rows  : {len(clean)}")
    print(f"  removed     : {len(raw) - len(clean)}")
    reasons = {
        "duplicate event_id": int(raw["event_id"].duplicated().sum()),
        "impossible depth": int((~raw["depth_km"].isna()
                                 & ~raw["depth_km"].between(0, 700)).sum()),
        "missing magnitude": int(raw["mw"].isna().sum()),
        "magnitude below M_MIN": int((raw["mw"] < sc.M_MIN).sum()),
    }
    for name, n in reasons.items():
        print(f"    row-level reason '{name}': {n}")
    print(f"  Those reasons sum to {sum(reasons.values())}, more than the "
          f"{len(raw) - len(clean)}")
    print("  rows removed, because one duplicate report also had a missing")
    print("  magnitude -- a row can carry two defects. Counting reasons and")
    print("  counting rows are different operations, and only the row count")
    print("  tells you how much data you lost.")

    mags = clean["mw"]

    section("2. Magnitude histogram with pd.cut")
    edges = np.arange(sc.M_MIN, 5.0 + 0.1, 0.1)
    binned = pd.cut(mags, bins=edges, right=False)
    counts = binned.value_counts().sort_index()
    print(f"  {len(mags)} magnitudes binned into 0.1-wide intervals")
    print("  interval      count   cumulative N(>= lower edge)")
    for interval, n in counts.items():
        lower = interval.left
        print(f"  [{lower:.1f}, {interval.right:.1f})  {n:5d}   "
              f"{int((mags >= lower).sum()):5d}")
    print()
    for lo, hi in ((2.0, 3.0), (3.0, 4.0)):
        n_lo, n_hi = int((mags >= lo).sum()), int((mags >= hi).sum())
        ratio = n_lo / n_hi if n_hi else float("nan")
        print(f"  N(M>={lo:.1f})/N(M>={hi:.1f}) = {n_lo}/{n_hi} = {ratio:.1f}"
              f"   -> implied b ~ {np.log10(ratio):.2f}")
    print("  A b-value is the base-10 slope of that fall-off: a decade of")
    print("  magnitude multiplies the rate by 10^b. One decade gives only one")
    print("  ratio, so it constrains b but does not estimate it.")
    print()
    print("  The modal bin is used by the 'maximum curvature' method of")
    print("  estimating completeness. Here it would suggest Mc near "
          f"{counts.idxmax().left:.1f}, but the method is known to")
    print("  underestimate Mc, so it is reported as a diagnostic rather than")
    print("  adopted as the answer.")

    section("3. The cumulative magnitude-frequency relation")
    grid = np.round(np.arange(2.0, mags.max() + 0.05, 0.5), 2)
    cumulative = pd.DataFrame(
        {
            "mc_geq": grid,
            "n_geq": [int((mags >= g).sum()) for g in grid],
            "log10_n": [np.log10((mags >= g).sum()) for g in grid],
        }
    )
    print(cumulative.to_string(index=False))
    print()
    print("  A two-point read of the slope, from M = 3.0 to M = 4.0:")
    n3 = int((mags >= 3.0).sum())
    n4 = int((mags >= 4.0).sum())
    print(f"    log10(N(3.0)) = {np.log10(n3):.4f}    "
          f"log10(N(4.0)) = {np.log10(n4):.4f}")
    if n4 > 0:
        print(f"    slope over that single decade = {np.log10(n4) - np.log10(n3):.4f}"
              f"  -> b ~ {np.log10(n3) - np.log10(n4):.4f}")
    print("  (Only two events sit above M 4.0, so that decade is itself a")
    print("  small-number estimate; it is a check on the order of magnitude,")
    print("  not a measurement.)")
    print("  Two points is not an estimate; it is a sanity check that the")
    print("  order of magnitude is right before doing the regression properly.")

    section("4. b-value: two estimators, and they disagree")
    mc = 3.0
    b_mle = b_aki_utsu(mags, mc)
    b_ls, n_points = b_least_squares(mags, mc)
    n_used = int((mags >= mc).sum())
    print(f"  completeness assumed at Mc = {mc}  (a stated assumption)")
    print(f"  events with M >= {mc}: {n_used}")
    print()
    print(f"  (a) maximum likelihood (Aki-Utsu, 0.1 binning) : b = {b_mle:.4f}")
    print(f"  (b) least squares on log10 N(>=M)              : b = {b_ls:.4f}")
    print(f"      difference                                 : "
          f"{abs(b_mle - b_ls):.4f}")
    print()
    print("  The two disagree because least squares weights every magnitude")
    print("  level equally in log space, while the likelihood weights each")
    print("  event equally -- and the small-magnitude bins contain most of the")
    print("  events. They are not two measurements of one number; they answer")
    print("  slightly different questions. Report which one you used.")
    print()
    sigma = b_mle / np.sqrt(n_used)
    print(f"  Approximate standard error of the MLE, b/sqrt(N): "
          f"{sigma:.4f}  (N = {n_used})")
    print("  That is the *formal* error at a fixed Mc. It is not the dominant")
    print("  uncertainty, as the next section shows.")

    section("5. The dominant uncertainty is the completeness choice")
    rows = []
    for mc_try in (2.5, 2.8, 3.0, 3.2, 3.5):
        n = int((mags >= mc_try).sum())
        if n < 5:
            rows.append((mc_try, n, np.nan, np.nan))
            continue
        rows.append((mc_try, n, b_aki_utsu(mags, mc_try),
                     b_aki_utsu(mags, mc_try) / np.sqrt(n)))
    table = pd.DataFrame(rows, columns=["Mc", "n_events", "b_mle", "sigma_b"])
    print(table.round(4).to_string(index=False))
    print()
    spread = table["b_mle"].max() - table["b_mle"].min()
    print(f"  Range of b over Mc = 2.5 .. 3.5 : {spread:.4f}")
    print(f"  Formal 1-sigma at Mc = 3.0      : {sigma:.4f}")
    print("  The choice of Mc moves the answer by far more than the formal")
    print("  error at a fixed Mc. Quoting 'b = x +/- sigma' without stating Mc")
    print("  and demonstrating the sensitivity is therefore misleading.")
    print()
    print("  On SYNTHETIC data the generator put in b = "
          f"{sc.B_VALUE_INPUT} with completeness")
    print(f"  at M = {sc.M_MIN}. The estimates near Mc = 2.5-3.0 land close to")
    print("  that input, which is a check on the code, NOT a measurement of")
    print("  anything. No b-value in this output is a result about the Earth.")

    section("6. Rate and energy summary")
    per_year = clean.assign(year=clean["origin_time"].dt.year)
    yearly = per_year.groupby("year", observed=True).agg(
        n_events=("event_id", "count"),
        max_mw=("mw", "max"),
    )
    yearly["events_per_day"] = yearly["n_events"] / 365.25
    print(yearly.round(4).to_string())
    print()
    print(f"  mean events per year: {yearly['n_events'].mean():.1f}")
    per_region = clean.assign(
        energy_j=sc.mag_to_energy_j(clean["mw"])
    ).groupby("region", observed=True).agg(
        n_events=("event_id", "count"),
        max_mw=("mw", "max"),
        sum_energy_j=("energy_j", "sum"),
    )
    print()
    print(per_region.assign(
        sum_energy_j=per_region["sum_energy_j"].map("{:.3e}".format)
    ).to_string())
    print()
    print("  Largest event in the SYNTHETIC catalogue: "
          f"M {clean['mw'].max():.1f} on "
          f"{clean.loc[clean['mw'].idxmax(), 'origin_time'].date()} in "
          f"{clean.loc[clean['mw'].idxmax(), 'region']}.")

    section("7. A CSV round trip, in memory")
    buf = io.StringIO()
    tidy = (clean[["event_id", "origin_time", "latitude", "longitude",
                   "depth_km", "mw", "region"]]
            .head(5))
    tidy.to_csv(buf, index=False)
    text = buf.getvalue()
    print("  to_csv wrote these lines:")
    print("    " + "    ".join(text.splitlines(keepends=True)[:4]).rstrip())
    print()
    back = pd.read_csv(io.StringIO(text), parse_dates=["origin_time"])
    print(f"  read_csv recovered {len(back)} rows with dtypes:")
    print(back.dtypes.to_string())
    print()
    print("  Two things to notice. First, a CSV carries values and column")
    print("  names but no dtypes: the round trip is only faithful because we")
    print("  told read_csv which column is a date. Second, the numeric columns")
    print("  survived unchanged here, but a CSV written from a column of")
    print("  Python objects would serialise their repr and come back as text.")
    print("  A CSV is an interchange format, not a storage format.")


if __name__ == "__main__":
    main()
