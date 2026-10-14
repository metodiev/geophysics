#!/usr/bin/env python3
"""Poster design: legibility at distance, capacity and dwell time.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python posters_demo.py

Everything here is SYNTHETIC.  Text heights, viewing distances, the legibility
angle, the words-per-area density and the dwell-time model are chosen teaching
values; no poster was measured.

Sections
--------
1. Text height and the maximum viewing distance.
2. Poster area: how many words fit, and at what size.
3. Dwell time and how many viewers a session can serve.
4. What is actually read: text role versus engagement.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
LEGIBILITY_ANGLE = 0.0085     # rad; the minimum subtended angle for comfortable reading
POSTER_WIDTH_MM = 841.0       # A0 portrait width
POSTER_HEIGHT_MM = 1189.0     # A0 portrait height
TEXT_ROLES = (("title", 36.0), ("section heading", 20.0),
              ("body", 10.0), ("caption", 8.0))
VIEW_DISTANCES = (0.5, 1.0, 1.5, 2.0, 3.0)
WORDS_PER_SQM = 420.0         # chosen body-text density
SESSION_MINUTES = 90.0
MEAN_DWELL_MINUTES = 2.0
TRAFFIC_PER_SESSION = 300


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. Text height and the maximum viewing distance")
    print("SYNTHETIC poster model: text heights, viewing distances and reading rates")
    print("are chosen teaching values; no poster or session was measured.")
    print(f"  legibility rule: text subtends at least {LEGIBILITY_ANGLE:.4f} rad "
          f"({np.degrees(LEGIBILITY_ANGLE):.2f} degrees)")
    print("  text role        height (mm)   max viewing distance (m)")
    for name, height_mm in TEXT_ROLES:
        max_distance = (height_mm / 1000.0) / LEGIBILITY_ANGLE
        print(f"  {name:<15s} {height_mm:9.1f}   {max_distance:22.2f}")
    print(f"  at a {VIEW_DISTANCES[2]:.1f} m standing distance the minimum readable "
          f"height is "
          f"{VIEW_DISTANCES[2] * LEGIBILITY_ANGLE * 1000:.1f} mm")
    print("  -> a caption set at 8 mm is legible only to about "
          f"{(8.0 / 1000.0) / LEGIBILITY_ANGLE:.1f} m; the crowd never gets that close,")
    print("     which is why captions are the first text to become decoration.")

    section("2. Poster area: how many words fit")
    area_m2 = POSTER_WIDTH_MM * POSTER_HEIGHT_MM / 1e6
    total_words = area_m2 * WORDS_PER_SQM
    print(f"  poster size = {POSTER_WIDTH_MM:.0f} x {POSTER_HEIGHT_MM:.0f} mm "
          f"= {area_m2:.2f} m^2 (A0)")
    print(f"  at {WORDS_PER_SQM:.0f} words/m^2 the poster holds about "
          f"{total_words:.0f} words of body text")
    for role, height_mm in TEXT_ROLES:
        words = area_m2 * WORDS_PER_SQM * (10.0 / height_mm) ** 2
        print(f"  if the body text were set at {height_mm:4.0f} mm the capacity would "
              f"be {words:6.0f} words")
    print(f"  a paper's abstract is about 250 words: the poster holds "
          f"{total_words / 250:.1f} abstracts' worth of text")
    print("  -> the budget is not prose; it is a title, three to five claims, and")
    print("     figures.  Text beyond about "
          f"{total_words:.0f} words will not be read at all.")

    section("3. Dwell time and how many viewers a session can serve")
    capacity = SESSION_MINUTES / MEAN_DWELL_MINUTES
    print(f"  session = {SESSION_MINUTES:.0f} min, mean dwell "
          f"{MEAN_DWELL_MINUTES:.0f} min per interested viewer")
    print(f"  maximum engaged viewers if the poster is never free = {capacity:.0f}")
    engaged = cap = min(capacity, 0.5 * capacity)
    print(f"  realistic engagement (poster free half the time) = {cap:.0f} viewers")
    print(f"  foot traffic modelled at {TRAFFIC_PER_SESSION} passers-by")
    print(f"  so the engaged fraction of traffic = "
          f"{cap / TRAFFIC_PER_SESSION * 100:.1f} %")
    print("  -> a poster that demands 5 minutes of reading engages nobody; the")
    print(f"     {MEAN_DWELL_MINUTES:.0f}-minute design is what the format supports.")

    section("4. What is actually read: text role versus engagement")
    rng = RNG
    n_visitors = int(TRAFFIC_PER_SESSION * 0.30)   # chosen: those who slow down
    reads_title = np.ones(n_visitors, dtype=bool)
    reads_figures = rng.random(n_visitors) < 0.70
    reads_headings = rng.random(n_visitors) < 0.45
    reads_body = rng.random(n_visitors) < 0.18
    reads_captions = rng.random(n_visitors) < 0.35
    print(f"  modelled {n_visitors} viewers who stop for at least a moment:")
    for label, flag in (("title", reads_title), ("figures", reads_figures),
                        ("section headings", reads_headings),
                        ("captions", reads_captions), ("body text", reads_body)):
        print(f"    {label:<17s} {int(flag.sum()):3d} viewers "
              f"({flag.mean() * 100:5.1f} %)")
    print(f"  a viewer who reads only the title and the figures is "
          f"{np.mean(reads_title & reads_figures) * 100:.1f} % of the audience")
    print("  -> design for the title-and-figures reader: every figure needs a")
    print("     self-contained caption (see lesson 24-02-06), because the caption is")
    print("     read more often than the paragraph that explains it.")


if __name__ == "__main__":
    main()
