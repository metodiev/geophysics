#!/usr/bin/env python3
"""Figures and captions: self-containment, ink and legibility.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python figures_and_captions_demo.py

Everything here is SYNTHETIC.  Captions are modelled as sets of binary elements
and the ink values are chosen teaching values; no figure is drawn.

Sections
--------
1. Caption elements and the self-containment rate.
2. The separated-figure test: how many figures survive on their own?
3. Data-ink ratios of common chart types.
4. Colour: distinguishable steps and greyscale survival.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
N_FIGURES = 240
ELEMENTS = {
    "names the variable": (0.86, 0.92),
    "states the unit": (0.62, 0.71),
    "identifies panels": (0.71, 0.80),
    "states n or a statistic": (0.48, 0.55),
}
P_MULTIPANEL = 0.55
# chart type -> (total ink, data ink), both in chosen arbitrary units per point
INK = {
    "bar chart": (1.00, 0.62),
    "box plot": (0.80, 0.60),
    "dot plot": (0.55, 0.45),
    "line with error bars": (0.70, 0.50),
    "pie chart": (1.20, 0.35),
}
N_COLOUR_LEVELS = 10
N_DISTINGUISHABLE = 6
P_COLOURBLIND_SAFE = 0.55
P_SURVIVES_GREYSCALE = 0.68


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    multipanel = RNG.random(N_FIGURES) < P_MULTIPANEL
    present = {}
    for name, (p_simple, p_multi) in ELEMENTS.items():
        p = np.where(multipanel, p_multi, p_simple)
        present[name] = RNG.random(N_FIGURES) < p

    section("1. Caption elements and the self-containment rate")
    print(f"SYNTHETIC corpus: {N_FIGURES} figures, "
          f"{multipanel.mean() * 100:.1f} % multi-panel")
    for name, p in ELEMENTS.items():
        print(f"  {name:<26s} present in {present[name].mean() * 100:5.1f} % of captions")
    score = np.mean([present[name] for name in ELEMENTS], axis=0)
    print(f"  caption completeness score = {score.mean():.3f} "
          f"+/- {score.std(ddof=1):.3f} (0-1)")
    print(f"  captions with all four elements = "
          f"{np.all([present[name] for name in ELEMENTS], axis=0).mean() * 100:.1f} %")
    print(f"  captions with none of the four  = "
          f"{np.all([~present[name] for name in ELEMENTS], axis=0).mean() * 100:.1f} %")

    section("2. The separated-figure test: how many figures survive on their own?")
    standalone = np.all([present[name] for name in ELEMENTS], axis=0)
    print(f"  figures interpretable without the text (variable + unit + panels + "
          f"statistics) = {int(standalone.sum())} / {N_FIGURES} = "
          f"{standalone.mean() * 100:.1f} %")
    weakest = min(ELEMENTS, key=lambda k: present[k].mean())
    print(f"  weakest element = '{weakest}' "
          f"(present in {present[weakest].mean() * 100:.1f} %)")
    print(f"  if '{weakest}' were present in every caption, the standalone rate would "
          f"become "
          f"{np.all([present[name] if name != weakest else np.ones(N_FIGURES, bool) for name in ELEMENTS], axis=0).mean() * 100:.1f} %")
    print("  -> the standalone rate is governed by the weakest element, exactly as")
    print("     the joint reporting rate is governed by the weakest reported item.")

    section("3. Data-ink ratios of common chart types")
    print("  chart type             total ink   data ink   data-ink ratio")
    for name, (total, data) in INK.items():
        print(f"  {name:<22s} {total:8.2f} {data:10.2f} {data / total:14.2f}")
    ratios = {name: data / total for name, (total, data) in INK.items()}
    best = max(ratios, key=ratios.get)
    worst = min(ratios, key=ratios.get)
    print(f"  highest data-ink ratio: {best} ({ratios[best]:.2f})")
    print(f"  lowest  data-ink ratio: {worst} ({ratios[worst]:.2f})")
    print(f"  ratio between them = {ratios[best] / ratios[worst]:.2f}x")
    print("  -> for the same data, the ink varies by a factor above 2; the ink is a")
    print("     choice, and unlabelled ink is decoration.")

    section("4. Colour: distinguishable steps and greyscale survival")
    print(f"  colour scale with {N_COLOUR_LEVELS} levels; "
          f"{N_DISTINGUISHABLE} reliably distinguishable")
    print(f"  fraction of the intended scale that carries distinct information = "
          f"{N_DISTINGUISHABLE / N_COLOUR_LEVELS * 100:.1f} %")
    colourblind_safe = RNG.random(N_FIGURES) < P_COLOURBLIND_SAFE
    survives = RNG.random(N_FIGURES) < P_SURVIVES_GREYSCALE
    print(f"  colourblind-safe palettes = {colourblind_safe.mean() * 100:.1f} % of figures")
    print(f"  encoding survives greyscale printing = {survives.mean() * 100:.1f} %")
    print(f"  figures with at least one readability failure (either) = "
          f"{np.mean(~(colourblind_safe & survives)) * 100:.1f} %")
    print(f"  figures with both failures = "
          f"{np.mean(~colourblind_safe & ~survives) * 100:.1f} %")
    print("  -> redundancy (colour plus shape or line style) is what makes a figure")
    print("     survive colour-blind readers, greyscale printing and photocopying.")


if __name__ == "__main__":
    main()
