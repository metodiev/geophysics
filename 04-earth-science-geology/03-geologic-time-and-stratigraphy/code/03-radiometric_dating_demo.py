"""Radiometric dating: concordia, discordia, and three failure modes.

Run:  .venv/bin/python 03-radiometric_dating_demo.py
Requires: NumPy.

Companion to lesson 04-03-03. The decay law itself, the half-life, the Bateman
chain and the closure-temperature equation are derived in
``02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md``; this demo
does not repeat them. It does the part that is specific to using an age in
geology:

1. Builds the U-Pb concordia curve and verifies that a synthetic rock of known
   age plots on it, to a stated tolerance.
2. Simulates a single episode of radiogenic-Pb loss, fits the resulting
   discordia chord, intersects it with the concordia curve and recovers *both*
   the crystallisation age (upper intercept) and the age of the disturbance
   (lower intercept) -- the check that the method, not the input, is right.
3. Quantifies three assumptions that a quoted age silently carries:
   (a) uncorrected common Pb -- what a small initial-daughter offset does to a
       model age;
   (b) an open system during the decay interval -- why different chronometers
       disagree;
   (c) a two-component mixing line masquerading as an isochron -- a line with a
       slope that has nothing to do with time.
4. Reports the fraction of the daughter product that must be present for a
   model age to reach a stated accuracy when the initial ratio can only be
   assumed, which is the quantitative reason laboratories measure ratios rather
   than concentrations.

Decay constants below are TABULATED, compilation-dependent values. The U-Pb
constants used here are the values in long-standing common use; different
compilations differ in the fifth significant figure, and every age in the
literature is tied to a stated set. Cite the compilation with the age.
"""

from __future__ import annotations

import numpy as np

# --------------------------------------------------------------------------
# TABULATED decay constants (common usage; compilations differ in the last
# digits -- state which compilation an age is tied to).
# --------------------------------------------------------------------------
LAMBDA_238 = 1.55125e-10   # a^-1, U-238 -> Pb-206
LAMBDA_235 = 9.8485e-10    # a^-1, U-235 -> Pb-207
LAMBDA_RB = 1.42e-11       # a^-1, Rb-87 -> Sr-87 (IUGS convention value)
MA = 1.0e6


def concordia(t_a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (206Pb*/238U, 207Pb*/235U) on the concordia curve."""
    x = np.expm1(LAMBDA_238 * t_a)
    y = np.expm1(LAMBDA_235 * t_a)
    return x, y


def age_238(x: np.ndarray, common: float = 0.0) -> np.ndarray:
    """Model age from 206Pb*/238U, with an uncorrected common-Pb offset."""
    return np.log1p(x + common) / LAMBDA_238


def age_235(y: np.ndarray, common: float = 0.0) -> np.ndarray:
    return np.log1p(y + common) / LAMBDA_235


def line_coefficients(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """Ordinary least-squares fit y = m x + c (for the discordia chord)."""
    m, c = np.polyfit(x, y, 1)
    return float(m), float(c)


def intersect_line_concordia(m: float, c: float, t_grid: np.ndarray) -> list[float]:
    """Ages where the concordia curve crosses the line y = m x + c.

    The crossing function is the residual g(t) = y_c(t) - (m x_c(t) + c); a sign
    change brackets an intercept, and bisection refines it. Done numerically
    rather than in closed form because the line is generally not solvable for t.
    """
    x_c, y_c = concordia(t_grid)
    g = y_c - (m * x_c + c)
    roots: list[float] = []

    def g_at(t: float) -> float:
        xt, yt = concordia(np.array([t]))
        return float(yt[0] - (m * xt[0] + c))

    for i in range(len(t_grid) - 1):
        gi, gj = g[i], g[i + 1]
        if gi == 0.0:
            roots.append(float(t_grid[i]))
            continue
        if gi * gj >= 0.0:
            continue
        lo, hi = float(t_grid[i]), float(t_grid[i + 1])
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if gi * g_at(mid) <= 0.0:
                hi = mid
            else:
                lo = mid
        roots.append(0.5 * (lo + hi))
    return roots


def part_one() -> None:
    print()
    print("1. Concordia: a rock of known age plots on the curve")
    print("-" * 70)
    t_true = 1000.0 * MA
    x, y = concordia(np.array([t_true]))
    back_238 = age_238(x)[0]
    back_235 = age_235(y)[0]
    print(f"  synthetic crystallisation age      {t_true / MA:,.2f} Ma")
    print(f"  206Pb*/238U                        {x[0]:.8f}")
    print(f"  207Pb*/235U                        {y[0]:.8f}")
    print(f"  age recovered from 206Pb*/238U     {back_238 / MA:,.6f} Ma "
          f"(residual {back_238 - t_true:.3e} a)")
    print(f"  age recovered from 207Pb*/235U     {back_235 / MA:,.6f} Ma "
          f"(residual {back_235 - t_true:.3e} a)")
    print("  Both residuals are at the round-off floor: the concordia curve and "
          "the age equation are inverses of each other by construction, so a "
          "non-zero residual would be an algebraic error, not a geological one.")

    t_grid = np.array([50.0, 100.0, 250.0, 500.0, 1000.0, 1800.0, 2700.0,
                       3600.0, 4400.0]) * MA
    xg, yg = concordia(t_grid)
    print()
    print(f"{'t (Ma)':>10}{'206/238':>14}{'207/235':>14}{'207/206':>12}")
    for t, xi, yi in zip(t_grid, xg, yg):
        print(f"  {t / MA:>8,.0f}{xi:>14.4f}{yi:>14.4f}{yi / xi:>12.4f}")
    print("  The 207Pb/206Pb ratio is nearly constant for young rocks and grows "
          "with age for old ones; this is why the two decay chains together "
          "give an internal consistency test and one chain alone does not.")


def part_two() -> None:
    print()
    print("2. Discordia: Pb loss, and recovering both ages from one chord")
    print("-" * 70)
    t_true = 1800.0 * MA       # SYNTHETIC crystallisation age
    t_loss = 300.0 * MA        # SYNTHETIC age of the disturbance
    x_true, y_true = concordia(np.array([t_true]))
    x_loss, y_loss = concordia(np.array([t_loss]))

    # Complete derivation of the discordia family, because the bookkeeping of U
    # decay is where this is usually got wrong.  With U(t) = U0 exp(-lambda t),
    # a sample that crystallised t_true ago, lost a fraction f of its radiogenic
    # Pb at t_loss, and has been closed since, has
    #     x_now = (exp(lambda t_true) - 1) - f (exp(lambda t_true) - exp(lambda t_loss))
    # because the radiogenic Pb present at t_loss is expressed as a ratio to the
    # U *remaining now*.  Hence x_now = x_true - f (x_true - x_loss): the family
    # lies exactly on the chord between concordia(t_true) and concordia(t_loss),
    # with f = 0 concordant at t_true and f = 1 concordant at t_loss.
    losses = np.array([0.0, 0.1, 0.25, 0.4, 0.6, 0.8, 1.0])
    x_obs = x_true[0] - losses * (x_true[0] - x_loss[0])
    y_obs = y_true[0] - losses * (y_true[0] - y_loss[0])
    print(f"  SYNTHETIC true age {t_true / MA:,.0f} Ma, disturbance at "
          f"{t_loss / MA:,.0f} Ma")
    print(f"{'Pb lost':>9}{'206/238':>13}{'207/235':>13}{'apparent t (Ma)':>18}")
    for f, xi, yi in zip(losses, x_obs, y_obs):
        print(f"  {f:>7.2f}{xi:>13.6f}{yi:>13.6f}{age_238(np.array([xi]))[0] / MA:>18,.1f}")
    print("  The single-chain age collapses towards the disturbance age as Pb "
          "is lost: an uncorrected discordant analysis reports the disturbance, "
          "not the rock.")

    m, c = line_coefficients(x_obs, y_obs)
    residual = np.max(np.abs((m * x_obs + c) - y_obs))
    print()
    print(f"  discordia fit:  207/235 = {m:.6f} * (206/238) + {c:.6f}")
    print(f"  max chord residual over the {len(losses)} analyses: "
          f"{residual:.3e} (a single-stage loss gives a mathematically exact line)")

    t_grid = np.linspace(1.0e4, 4.6e9, 400000)
    roots = intersect_line_concordia(m, c, t_grid)
    roots_ma = sorted(r / MA for r in roots)
    print(f"  intersections with concordia: "
          f"{', '.join(f'{r:,.2f}' for r in roots_ma)} Ma")
    if len(roots_ma) >= 2:
        upper, lower = roots_ma[-1], roots_ma[0]
        print(f"  upper intercept {upper:,.2f} Ma vs true age "
              f"{t_true / MA:,.2f} Ma   -> error "
              f"{upper - t_true / MA:+,.3f} Ma")
        print(f"  lower intercept {lower:,.2f} Ma vs disturbance "
              f"{t_loss / MA:,.2f} Ma -> error {lower - t_loss / MA:+,.3f} Ma")
        print("  Two ages come out of one chord, and neither was an input: the "
              "discordia is the internal test that makes U-Pb a dating system "
              "rather than a ratio-to-age conversion.")

    # What the same data would report if the analysis assumed no disturbance.
    print()
    print("  If the same analyses were used as single chronometer ages and "
          "averaged naively, they would report:")
    t_app = age_238(x_obs) / MA
    print(f"    mean of the seven 206/238 ages = {t_app.mean():,.1f} Ma, "
          f"spread {t_app.max() - t_app.min():,.1f} Ma")
    print(f"    true age = {t_true / MA:,.1f} Ma; error "
          f"{t_app.mean() - t_true / MA:+,.1f} Ma "
          f"({(t_app.mean() - t_true / MA) / (t_true / MA):+.1%})")


def part_three_a() -> None:
    print()
    print("3a. Assumption: the initial daughter product is zero")
    print("-" * 70)
    print("  An uncorrected common-Pb contribution adds to the measured ratio "
          "and inflates the apparent age.")
    t_true = 1000.0 * MA
    x_true = concordia(np.array([t_true]))[0][0]
    print(f"  SYNTHETIC true 206Pb*/238U = {x_true:.6f} for "
          f"{t_true / MA:,.0f} Ma")
    print(f"{'common-Pb offset':>18}{'206/238 meas.':>15}{'app. age (Ma)':>15}"
          f"{'error (Ma)':>13}")
    for offset in (0.0, 0.002, 0.005, 0.01, 0.02):
        t_app = age_238(np.array([x_true]), common=offset)[0]
        print(f"  {offset:>16.3f}{x_true + offset:>15.6f}{t_app / MA:>15,.1f}"
              f"{t_app / MA - t_true / MA:>+13,.1f}")
    print(f"  An offset of 0.01 in the ratio -- a few per cent of it -- moves a "
          f"1000 Ma age by "
          f"{age_238(np.array([x_true]), common=0.01)[0] / MA - 1000:,.0f} Ma.")
    young = concordia(np.array([100.0 * MA]))[0][0]
    d_old = age_238(np.array([x_true]), common=0.01)[0] / MA - 1000.0
    d_young = age_238(np.array([young]), common=0.01)[0] / MA - 100.0
    print(f"  The offset is a constant added to the ratio, so its effect on the "
          f"age is relatively larger for young rocks: the same offset shifts a "
          f"100 Ma age by {d_young:,.1f} Ma "
          f"({d_young / 100.0:,.1%} of its age) against "
          f"{d_old / 1000.0:,.1%} at 1000 Ma.")
    print("  Every U-Pb age is therefore either corrected for common Pb by "
          "measuring a non-radiogenic Pb isotope, or reported with the "
          "correction and its uncertainty stated.")


def part_three_b() -> None:
    print()
    print("3b. Assumption: the system stayed closed")
    print("-" * 70)
    t_true = 500.0 * MA
    x_true = concordia(np.array([t_true]))[0][0]
    print(f"  SYNTHETIC true age {t_true / MA:,.0f} Ma, true 206Pb*/238U = "
          f"{x_true:.6f}")
    print(f"{'lost/added fraction of 238U':>30}{'apparent age (Ma)':>20}"
          f"{'error (Ma)':>13}")
    for frac in (-0.10, -0.05, 0.0, 0.05, 0.10):
        # A deficit of parent looks like excess daughter: x_meas = x/(1-f).
        x_meas = x_true / (1.0 + frac)
        t_app = age_238(np.array([x_meas]))[0]
        print(f"  {frac:>+28.2f}{t_app / MA:>20,.1f}"
              f"{t_app / MA - t_true / MA:>+13,.1f}")
    print("  A 5 per cent parent loss moves the age by tens of millions of "
          "years in this example. That is the size of the disagreement that "
          "sends a sample back to the laboratory: when two chronometers in the "
          "same rock disagree by more than their uncertainties, the assumption "
          "that failed is closure, and the disagreement is the evidence.")


def part_three_c() -> None:
    print()
    print("3c. Assumption: the line is an isochron, not a mixing line")
    print("-" * 70)
    # Two-component mixing.  Reservoir A and B have parent/daughter and
    # daughter-isotope ratios; mixtures lie on a perfect straight line.
    A = np.array([0.20, 0.7110])
    B = np.array([0.90, 0.7600])
    fractions = np.linspace(0.0, 1.0, 9)
    x = A[0] + fractions * (B[0] - A[0])
    y = A[1] + fractions * (B[1] - A[1])
    m, c = line_coefficients(x, y)
    t_mix = np.log1p(m) / LAMBDA_RB
    print(f"  SYNTHETIC end members  x (Rb/Sr)   A = {A[0]:.2f}, B = {B[0]:.2f}")
    print(f"                         y (Sr87/86) A = {A[1]:.4f}, B = {B[1]:.4f}")
    print(f"  {len(fractions)} mixtures give a perfect line: slope = {m:.6f}, "
          f"intercept = {c:.6f}")
    print(f"  r^2 = {np.corrcoef(x, y)[0, 1] ** 2:.8f} -- an isochron-fit "
          "statistic cannot distinguish this from an isochron.")
    print(f"  'Age' read from the slope with lambda_Rb: {t_mix / MA:,.1f} Ma")
    print("  That number is a property of the two end-member compositions and "
          "of nothing else: neither end member has an age of its own in this "
          "construction. The diagnostic is geological, not statistical:")
    print("    - mixing lines pass through the composition of the end members,")
    print("    - they correlate with an element ratio that has no business in "
          "the isochron (e.g. 1/Sr),")
    print("    - and adding a third end member bends the line.")
    third = np.array([0.55, 0.7450])
    xs = np.concatenate([x, [third[0]]])
    ys = np.concatenate([y, [third[1]]])
    res3 = ys - (m * xs + c)
    print(f"  With a third component added, the maximum departure from the "
          f"two-component line is {np.max(np.abs(res3)):.5f} in "
          f"Sr87/Sr86, which is far above a modern measurement precision.")
    print("  Quantitative versions of this test exist and are the subject of "
          "isotope-geochemistry coursework; the point here is that a line is "
          "not evidence of an age until the mixing hypothesis is excluded.")


def part_four() -> None:
    print()
    print("4. How much daughter product must be present for a model age?")
    print("-" * 70)
    print("  A model age assumes an initial daughter/daughter-isotope ratio. "
          "The error that a wrong assumption produces shrinks as the radiogenic "
          "daughter dominates the total.")
    t_true = 300.0 * MA
    assumed_initial = 0.7040     # what the analyst assumes
    true_initial = 0.7060        # what the rock actually had (SYNTHETIC spread)
    x_axis = np.array([0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 4.00])
    # isochron: y = r0 + x (exp(lambda t) - 1); model age assumes r0_assumed.
    slope_true = np.expm1(LAMBDA_RB * t_true)
    y = true_initial + slope_true * x_axis
    wrong_slope = (y - assumed_initial) / x_axis
    t_model = np.log1p(wrong_slope) / LAMBDA_RB
    print(f"  SYNTHETIC: true age {t_true / MA:,.0f} Ma, true initial ratio "
          f"{true_initial:.4f}, assumed {assumed_initial:.4f}")
    print(f"{'Rb/Sr':>9}{'Sr87/86':>11}{'model age (Ma)':>17}{'error (Ma)':>13}")
    for xi, yi, ti in zip(x_axis, y, t_model):
        print(f"  {xi:>7.2f}{yi:>11.4f}{ti / MA:>17,.1f}"
              f"{ti / MA - t_true / MA:>+13,.1f}")
    print("  At the highest parent/daughter ratio the model age is within a few "
          "per cent; at the lowest it is wrong by a large multiple of the age. "
          "The reason to measure parent/daughter ratios -- and to fit an "
          "intercept rather than assume one -- is visible in the right-hand "
          "column, and it is why a single low-ratio analysis cannot carry an "
          "age no matter how precise the mass spectrometry is.")


def main() -> None:
    print("=" * 76)
    print("Radiometric dating: concordia, discordia and the assumptions ledger")
    print("=" * 76)
    part_one()
    part_two()
    part_three_a()
    part_three_b()
    part_three_c()
    part_four()
    print()
    print("=" * 76)
    print("All decay constants above are TABULATED values that differ between")
    print("compilations; cite the compilation with every age. All ages used as")
    print("inputs above are SYNTHETIC, constructed to exercise the method. No")
    print("age of a named rock unit is asserted anywhere in this script.")
    print("=" * 76)


if __name__ == "__main__":
    main()
