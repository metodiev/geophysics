"""Deep time: compressing Earth history, and the uncertainty of an interval.

Run:  .venv/bin/python 01-deep_time_demo.py
Requires: NumPy.

Companion to lesson 04-03-01. This demo does *not* assert any boundary age of
the geologic time scale: boundary ages are properties of a specific, dated
version of an authoritative chart and change between versions. What it does do
is quantify four things that a chart cannot show you:

1. How an anchor age is compressed onto everyday scales (a day, a year, a
   metre), which is the arithmetic behind every "Earth history in 24 hours"
   graphic -- and why those graphics are only as good as the input age.
2. Ratio arithmetic: how many human-scale intervals fit into deep time, and
   why the answer has to be read on a logarithmic scale to mean anything.
3. Uncertainty propagation on the *difference* of two ages, which is what a
   duration actually is. A duration can be far better determined than the ages
   it is built from, but only if the errors are correlated -- and this demo
   shows the size of that effect.
4. The resolution limit of a linear time axis, which is the geometric reason
   deep time is unintuitive: on a linear axis long enough to hold the age of
   the Earth, all of recorded history is thinner than a wavelength of light.

Every anchor age below is labelled TABULATED and printed with the uncertainty
that must accompany it. Anchor ages of this kind differ between compilations in
their last quoted digit; the lesson requires you to cite the compilation.

The script:

1. Prints the anchor ages with absolute and relative uncertainty.
2. Compresses each anchor onto a 24 h clock, a calendar year, a 100 m walk and
   a 1 m bar.
3. Counts human-scale intervals inside an anchor (ratio and log10 of ratio).
4. Propagates uncertainty through a duration, for independent and correlated
   errors, and reports the duration uncertainty for each case.
5. Reports the resolution of a linear axis, and the size of recorded history on
   it, in metres, millimetres and micrometres.
6. Prints the structural hierarchy of the time scale (names and counts only)
   and the depth of the nesting, with no ages attached.
"""

from __future__ import annotations

import math

import numpy as np

# --------------------------------------------------------------------------
# TABULATED anchor ages.  These are commonly quoted values; every one of them is
# compilation-dependent and carries a published uncertainty.  They are anchors
# for the arithmetic below, not results of this script.
# --------------------------------------------------------------------------

YEAR = 3.15576e7  # s, Julian year (365.25 d) -- a definition, exact

ANCHORS = (
    # name, age (a), 1-sigma uncertainty (a), provenance note
    ("Earth (oldest Solar System solids)", 4.567e9, 1.0e6,
     "TABULATED; commonly quoted meteorite isochron age"),
    ("Earth (accretion/age of the planet)", 4.54e9, 5.0e7,
     "TABULATED; commonly quoted 4.54 +/- 0.05 Ga"),
    ("Universe (cosmic microwave background)", 1.38e10, 2.0e7,
     "TABULATED; commonly quoted 13.8 Ga"),
)

# Human-scale intervals.  Nominal, deliberately round numbers: the point is the
# order of magnitude of the ratio, not the last digit of the input.
INTERVALS = (
    ("recorded history (writing)", 5.0e3, 0.0),
    ("a human lifetime", 80.0, 0.0),
    ("one century", 100.0, 0.0),
    ("one million years", 1.0e6, 0.0),
)


def fmt(x: float) -> str:
    """Compact fixed-point formatting for the printed tables."""
    if x == 0:
        return "0"
    if abs(x) >= 1e5 or abs(x) < 1e-3:
        return f"{x:.4e}"
    return f"{x:.4f}"


def section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def anchors_table() -> None:
    section("1. Anchor ages, with the uncertainty that must travel with them")
    print(f"{'anchor':<40}{'age (a)':>13}{'+/- (a)':>13}{'rel. unc.':>12}")
    for name, age, sigma, _note in ANCHORS:
        print(f"{name:<40}{age:>13.4e}{sigma:>13.2e}{sigma / age:>12.2%}")
    print()
    for name, age, sigma, note in ANCHORS:
        print(f"  {name}: {note}")
        print(f"    A 1 per cent error in this age is {0.01 * age:.3e} a "
              f"= {0.01 * age / 1e6:.2f} Ma. That is the size of the tolerance "
              f"you are accepting when you do not carry the uncertainty.")


def compression_table() -> None:
    section("2. Compressing an anchor onto everyday scales")
    scales = (
        ("24 h clock", 86400.0, "s"),
        ("calendar year", 1.0, "year"),
        ("100 m walk", 100.0, "m"),
        ("1 m bar", 1.0, "m"),
    )
    earth = ANCHORS[1][1]
    print(f"{'anchor':<40}{'scale':<14}{'full scale':>14}{'1 Ma of history':>20}")
    for name, age, _sigma, _note in ANCHORS:
        for scale_name, scale_span, unit in scales:
            per_ma = scale_span * 1e6 / age
            print(f"  {name:<38}{scale_name:<14}{fmt(scale_span) + ' ' + unit:>14}"
                  f"{fmt(1e6 * scale_span / age) + ' ' + unit:>20}")
        print()
    # The canonical sentences, computed rather than asserted.
    seconds_per_ma = 86400.0 * 1e6 / earth
    print(f"  On the 24 h clock, 1 Ma of Earth history is "
          f"{seconds_per_ma:.2f} s.")
    print(f"  1 h of that clock is {earth / 24.0:,.3e} a = "
          f"{earth / 24.0 / 1e6:,.2f} Ma of Earth history.")
    print(f"  1 min of that clock is {earth / 1440.0:,.3e} a = "
          f"{earth / 1440.0 / 1e6:,.2f} Ma of Earth history.")
    print(f"  1 s of that clock is {earth / 86400.0:,.3e} a.")
    print(f"  On the calendar-year compression, 1 Ma of Earth history is "
          f"{YEAR * 1e6 / earth:.2f} s; 1 day of that calendar is "
          f"{earth / 365.25 / 1e6:,.2f} Ma of Earth history.")


def ratio_arithmetic() -> None:
    section("3. How many human-scale intervals fit inside an anchor")
    earth = ANCHORS[1][1]
    print(f"{'interval':<28}{'length (a)':>13}{'count in Earth age':>22}{'log10':>10}")
    for name, length, _ in INTERVALS:
        count = earth / length
        print(f"  {name:<26}{length:>13.4e}{count:>22.4e}{math.log10(count):>10.2f}")
    print()
    logs = [math.log10(earth / length) for _, length, _ in INTERVALS]
    print("  Read the log10 column, not the count column: the counts span "
          f"{min(logs):.2f} to {max(logs):.2f} orders of magnitude, a factor of "
          f"{10 ** (max(logs) - min(logs)):.1f}, which is why a linear mental "
          "model of deep time fails.")
    for name, length, _ in INTERVALS:
        print(f"  If the Earth age is one day, {name} is "
              f"{86400.0 * length / earth:.3e} s.")


def duration_uncertainty() -> None:
    section("4. The uncertainty of a duration, not of an age")

    # SYNTHETIC example ages, chosen for the arithmetic, not read from any chart.
    t_top = 400.0e6
    t_base = 500.0e6
    sigma = 5.0e6  # 1 per cent of a 500 Ma age
    duration = t_base - t_top

    independent = math.sqrt(sigma ** 2 + sigma ** 2)
    perfectly_correlated = 0.0
    rho = 0.75
    rho_75 = math.sqrt(sigma ** 2 + sigma ** 2 - 2 * rho * sigma * sigma)

    print("  SYNTHETIC inputs (chosen for the arithmetic; not a chart reading):")
    print(f"    top of interval  t1 = {t_top:.1e} a +/- {sigma:.1e} a")
    print(f"    base of interval t2 = {t_base:.1e} a +/- {sigma:.1e} a")
    print(f"    duration            = {duration:.1e} a")
    print()
    print(f"{'error model':<34}{'sigma(duration) (a)':>22}{'relative':>12}")
    for label, value in (
        ("independent (rho = 0)", independent),
        ("correlated, rho = 0.75", rho_75),
        ("fully correlated (rho = 1)", perfectly_correlated),
    ):
        print(f"  {label:<32}{value:>22.4e}{value / duration:>12.2%}")
    print()
    print("  The two boundary ages each carry 1.00 per cent relative "
          "uncertainty, yet the duration can carry 0.00 to 1.41 per cent: "
          "a duration is a *difference*, and correlated errors cancel in a "
          "difference. Any statement about a rate (a sedimentation rate, a "
          "cooling rate) divides one difference by another and inherits both "
          "uncertainties.")


def axis_resolution() -> None:
    section("5. The resolution of a linear time axis")
    earth = ANCHORS[1][1]
    for bar in (1.0, 4.54, 100.0):
        per_mm = bar * earth / (1000.0 * 1.0)
        print(f"  A {bar:g} m linear bar for the Earth age: 1 mm = "
              f"{per_mm:.3e} a = {per_mm / 1e6:.2f} Ma")
    bar = 4.54
    recorded = INTERVALS[0][1]
    size = recorded / earth * bar
    print()
    print(f"  On a 4.54 m bar, all of recorded history "
          f"({recorded:.0f} a) occupies {size * 1e3:.4f} mm = "
          f"{size * 1e6:.3f} micrometres.")
    print(f"  A printed line is about 0.1 mm wide, i.e. "
          f"{0.1e-3 / bar * earth:.3e} a of Earth history -- roughly "
          f"{0.1e-3 / bar * earth / 1e6:.2f} Ma.")
    print("  This is the geometric reason a linear time axis is useless for deep "
          "time: the Phanerozoic and the Precambrian cannot be shown at the same "
          "linear scale with any resolution in the younger part.")


def hierarchy() -> None:
    section("6. The hierarchy of the time scale (names and counts only)")
    # NAMES ONLY.  No boundary ages are attached, because they belong to a
    # specific version of the chart.
    eons = ["Hadean", "Archean", "Proterozoic", "Phanerozoic"]
    eras_phanerozoic = ["Paleozoic", "Mesozoic", "Cenozoic"]
    periods = {
        "Paleozoic": ["Cambrian", "Ordovician", "Silurian", "Devonian",
                      "Carboniferous", "Permian"],
        "Mesozoic": ["Triassic", "Jurassic", "Cretaceous"],
        "Cenozoic": ["Paleogene", "Neogene", "Quaternary"],
    }
    print(f"  eons: {len(eons)} -> {', '.join(eons)}")
    print(f"  eras of the Phanerozoic eon: {len(eras_phanerozoic)} -> "
          f"{', '.join(eras_phanerozoic)}")
    total_periods = 0
    for era, plist in periods.items():
        total_periods += len(plist)
        print(f"    periods of the {era:<10}: {len(plist):>2} -> "
              f"{', '.join(plist)}")
    print()
    print(f"  levels below eon: era, period, epoch, age (chron).")
    print(f"  Phanerozoic eon = {len(eras_phanerozoic)} eras = "
          f"{total_periods} periods; each period is further divided into "
          f"epochs and each epoch into ages.")
    print("  The nesting is a hierarchy of *names*, and every boundary in it is "
          "defined by a physical reference point (a GSSP) or a numeric age "
          "(a GSSA), not by its duration. The chart that assigns ages to those "
          "boundaries is revised; the hierarchy of names is stable.")


def main() -> None:
    print("=" * 78)
    print("Deep time: compression, ratio arithmetic and interval uncertainty")
    print("=" * 78)
    anchors_table()
    compression_table()
    ratio_arithmetic()
    duration_uncertainty()
    axis_resolution()
    hierarchy()
    print()
    print("=" * 78)
    print("Every anchor age above is a TABULATED, compilation-dependent value.")
    print("Nothing here is a computed age of a rock; no boundary age of the")
    print("time scale is asserted. Read them from a dated version of the chart.")
    print("=" * 78)


if __name__ == "__main__":
    main()
