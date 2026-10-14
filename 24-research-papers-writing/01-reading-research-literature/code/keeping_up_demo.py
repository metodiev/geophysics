#!/usr/bin/env python3
"""Keeping up with the literature: alert volume, filtering and attention.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python keeping_up_demo.py

Everything here is SYNTHETIC.  Publication rates, the relevance prior and the
filter performance are chosen teaching values; no feed is queried.

Sections
--------
1. Alert volume from a small set of sources.
2. A keyword filter: what it removes and what it costs.
3. Attention as a finite resource: the cap model.
4. The annual budget, and the marginal cost of one relevant paper.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC source and attention parameters (chosen teaching values) ------
SOURCES = (
    ("topical journal A", 3.0),
    ("topical journal B", 1.5),
    ("general journal C", 12.0),
    ("society newsletter", 0.4),
    ("preprint server X", 25.0),
    ("preprint server Y", 8.0),
)
RELEVANCE_PRIOR = 0.06     # fraction of new items relevant to one project
FILTER_PRECISION = 0.30    # P(relevant | alert passes the keyword filter)
FILTER_RECALL = 0.80       # P(alert passes | relevant)
MIN_PER_ALERT = 6.0        # minutes to triage one alert
WEEKLY_CAP = 25            # alerts a reader will actually open per week
WEEKS_PER_YEAR = 46.0      # working weeks


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    rates = np.array([r for _, r in SOURCES])

    section("1. Alert volume from a small set of sources")
    print("SYNTHETIC sources (chosen publication rates):")
    for name, rate in SOURCES:
        print(f"  {name:<22s} {rate:5.1f} items/day -> {rate * 7:6.1f} items/week")
    weekly = float(rates.sum() * 7.0)
    print(f"  total volume = {weekly:.0f} items/week "
          f"({weekly * WEEKS_PER_YEAR:.0f} items/year)")
    relevant_per_week = weekly * RELEVANCE_PRIOR
    print(f"  at a {RELEVANCE_PRIOR * 100:.0f} % relevance prior that is "
          f"{relevant_per_week:.1f} relevant items/week "
          f"({relevant_per_week * WEEKS_PER_YEAR:.0f}/year)")
    print(f"  reading every item at {MIN_PER_ALERT:.0f} min each = "
          f"{weekly * MIN_PER_ALERT / 60:.1f} h/week "
          f"({weekly * MIN_PER_ALERT * WEEKS_PER_YEAR / 60:.0f} h/year)")

    section("2. A keyword filter: what it removes and what it costs")
    n_items = int(round(weekly * WEEKS_PER_YEAR))
    alerts = RNG.random(n_items) < RELEVANCE_PRIOR
    n_rel = int(alerts.sum())
    p_false_pass = (1.0 - FILTER_PRECISION) / (1.0 - RELEVANCE_PRIOR) * RELEVANCE_PRIOR
    passes = np.where(alerts, RNG.random(n_items) < FILTER_RECALL,
                      RNG.random(n_items) < p_false_pass)
    kept = int(passes.sum())
    kept_rel = int((passes & alerts).sum())
    print(f"  simulated year: {n_items} items, {n_rel} relevant")
    print(f"  filter keeps {kept} items ({kept / n_items * 100:.1f} % of the volume)")
    print(f"  measured precision = {kept_rel / max(kept, 1) * 100:.1f} %, "
          f"measured recall = {kept_rel / max(n_rel, 1) * 100:.1f} %")
    print(f"  time without filter = {n_items * MIN_PER_ALERT / 60:.0f} h/year")
    print(f"  time with filter    = {kept * MIN_PER_ALERT / 60:.0f} h/year "
          f"(saving {n_items * MIN_PER_ALERT / 60 - kept * MIN_PER_ALERT / 60:.0f} h/year)")
    print(f"  relevant items missed = {n_rel - kept_rel} "
          f"({(n_rel - kept_rel) / max(n_rel, 1) * 100:.1f} % of the relevant set)")

    section("3. Attention as a finite resource: the cap model")
    for cap in (10, 25, 50, 100):
        opened = min(cap, weekly)
        print(f"  unfiltered, cap {cap:3d} alerts/week on {weekly:.0f} items: "
              f"opened fraction {opened / weekly * 100:5.1f} %, "
              f"relevant items reached {(opened / weekly) * relevant_per_week:.2f}/week")
    filtered_volume = kept / WEEKS_PER_YEAR
    precision = kept_rel / max(kept, 1)
    print(f"  after filtering the volume is {filtered_volume:.1f} items/week "
          f"(precision {precision * 100:.1f} %)")
    reach = min(WEEKLY_CAP, filtered_volume) / filtered_volume * relevant_per_week * precision
    print(f"  filtered, cap {WEEKLY_CAP} alerts/week: opened fraction "
          f"{min(WEEKLY_CAP, filtered_volume) / filtered_volume * 100:.1f} %, "
          f"relevant items reached {reach:.2f}/week")
    print(f"  -> filtering raises the relevant items reaching attention from "
          f"{25 / weekly * relevant_per_week:.2f}/week to {reach:.2f}/week: the cap,")
    print("     not the feed, is what binds, so precision buys attention.")

    section("4. The annual budget, and the marginal cost of one relevant paper")
    hours = kept * MIN_PER_ALERT / 60.0
    print(f"  filtered reading budget = {hours:.0f} h/year "
          f"({hours / WEEKS_PER_YEAR:.1f} h/week)")
    print(f"  relevant items found = {kept_rel}/year "
          f"({kept_rel / WEEKS_PER_YEAR:.1f}/week)")
    print(f"  marginal cost = {kept * MIN_PER_ALERT / max(kept_rel, 1):.1f} min per "
          f"relevant item found")
    print(f"  at {MIN_PER_ALERT:.0f} min per alert, halving the kept volume at constant")
    print(f"  recall would forgo about {kept_rel * 0.5:.0f} relevant items a year "
          f"and save {hours * 0.5:.0f} h.")


if __name__ == "__main__":
    main()
