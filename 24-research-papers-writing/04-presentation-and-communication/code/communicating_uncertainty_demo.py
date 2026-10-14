#!/usr/bin/env python3
"""Communicating uncertainty: intervals, likelihood language and decision loss.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python communicating_uncertainty_demo.py

Everything here is SYNTHETIC.  The decision problem, the loss function and the
misinterpretation rates are chosen teaching values.  The likelihood phrases and
their probability ranges follow the convention used in IPCC assessment reports;
they are quoted as a stated scale, not as measurements.

Sections
--------
1. From an interval to a statement: what a credible interval supports.
2. Likelihood language: the width of each phrase, and the ambiguity it leaves.
3. A decision problem: point estimate versus interval-aware rule.
4. Framing: the same number, two readings.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC parameters (chosen teaching values) --------------------------
# Likelihood scale as used in IPCC assessment reports (stated convention).
LIKELIHOOD = (
    ("virtually certain", 0.99, 1.00),
    ("extremely likely", 0.95, 1.00),
    ("very likely", 0.90, 1.00),
    ("likely", 0.66, 1.00),
    ("about as likely as not", 0.33, 0.66),
    ("unlikely", 0.00, 0.33),
    ("very unlikely", 0.00, 0.10),
    ("extremely unlikely", 0.00, 0.05),
)
THRESHOLD = 3.0            # decision threshold on the quantity
POINT_ESTIMATE = 3.6
INTERVAL = (2.4, 4.8)      # 90 % credible interval
LOSS_WRONG = 10.0          # cost of acting when the true value is below threshold
LOSS_MISSED = 6.0          # cost of not acting when the true value is above
N_SIMS = 20000
P_INVERT_FREQUENCY = 0.28  # chosen: P(a lay reader inverts "1 in 10" framing)
P_INVERT_PERCENT = 0.11    # chosen: P(a lay reader inverts "10 %" framing)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. From an interval to a statement")
    lo, hi = INTERVAL
    print(f"SYNTHETIC estimate: point value {POINT_ESTIMATE:.1f}, "
          f"90 % credible interval [{lo:.1f}, {hi:.1f}]")
    print(f"  interval width = {hi - lo:.1f} units "
          f"({(hi - lo) / POINT_ESTIMATE * 100:.0f} % of the point estimate)")
    print(f"  the interval includes the decision threshold {THRESHOLD:.1f}: "
          f"{lo <= THRESHOLD <= hi}")
    print(f"  so the data are consistent with acting and with not acting; a statement")
    print(f"  of the form 'the value is {POINT_ESTIMATE:.1f}' discards the decision.")
    for level, z in (("90 %", 1.645), ("95 %", 1.960), ("99 %", 2.576)):
        se = (hi - lo) / (2 * 1.645)
        half = z * se
        print(f"  {level} interval: half-width {half:.2f} units -> "
              f"[{POINT_ESTIMATE - half:.2f}, {POINT_ESTIMATE + half:.2f}]")
    print(f"  the 95 % interval is {1.960 / 1.645:.2f}x the 90 % one, so the choice of")
    print("  level is a choice about how much of the range to report")
    print("  -> widening the interval is not extra caution; it is a different claim.")

    section("2. Likelihood language: the width of each phrase")
    print("  phrase                     probability range      width (points)")
    for name, low, high in LIKELIHOOD:
        print(f"  {name:<26s} [{low * 100:5.1f} %, {high * 100:5.1f} %]"
              f" {((high - low) * 100):16.1f}")
    widths = {name: high - low for name, low, high in LIKELIHOOD}
    print(f"  narrowest phrase: extremely unlikely "
          f"({widths['extremely unlikely'] * 100:.0f} points)")
    print(f"  widest phrase:    likely ({widths['likely'] * 100:.0f} points)")
    ratio = widths["likely"] / widths["extremely unlikely"]
    print(f"  ratio of ambiguity between them = {ratio:.1f}x")
    print("  -> 'likely' spans a third of the probability range: it is a statement")
    print("     about ordering, not about probability.  Give the number as well.")

    section("3. A decision problem: which rule, and decided by what")
    from math import erf, sqrt

    se = (INTERVAL[1] - INTERVAL[0]) / (2 * 1.645)
    normal_cdf = lambda x: 0.5 * (1.0 + erf(x / sqrt(2.0)))
    lo_z = (INTERVAL[0] - POINT_ESTIMATE) / se
    print(f"  posterior standard error implied by the 90 % interval = {se:.3f} units")
    print(f"  losses: acting when the truth is below the threshold costs "
          f"{LOSS_WRONG:.0f} units; not acting when it is above costs "
          f"{LOSS_MISSED:.0f} units")
    for losses in ((10.0, 6.0), (20.0, 6.0)):
        l_wrong, l_missed = losses
        p_star = l_wrong / (l_wrong + l_missed)
        print(f"\n  loss pair ({l_wrong:.0f}, {l_missed:.0f}): act only if "
              f"P(above) > {p_star:.3f}")
        print("   estimate   P(above)   optimal   loss if point rule   loss if "
              "interval-lower-bound rule")
        for mean in (2.6, 3.0, 3.2, 3.4, 3.6, 4.0, 4.4):
            p_above = normal_cdf((mean - THRESHOLD) / se)
            loss_if_act = (1 - p_above) * l_wrong
            loss_if_not = p_above * l_missed
            optimal = "act" if loss_if_act < loss_if_not else "wait"
            point_act = mean > THRESHOLD
            interval_act = (INTERVAL[0] > THRESHOLD)
            loss_point = loss_if_act if point_act else loss_if_not
            loss_interval = loss_if_act if interval_act else loss_if_not
            print(f"  {mean:8.2f}   {p_above:8.3f}   {optimal:<7s}   "
                  f"{loss_point:18.3f}   {loss_interval:29.3f}")
    print("\n  -> the point rule and the interval rule are both fixed rules; the")
    print("     optimal decision changes with the loss pair.  When mistakes are")
    print("     expensive relative to missed opportunities, the same estimate leads to")
    print("     a different recommendation, which is why the loss ratio belongs in the")
    print("     document rather than in the reader's head.")

    section("4. Framing: the same number, two readings")
    print(f"  framing A: 'a 10 % chance of exceeding the threshold' -> modelled "
          f"misinterpretation {P_INVERT_PERCENT * 100:.0f} %")
    print(f"  framing B: 'a 1 in 10 chance of exceeding the threshold' -> modelled "
          f"misinterpretation {P_INVERT_FREQUENCY * 100:.0f} %")
    ratio = P_INVERT_FREQUENCY / P_INVERT_PERCENT
    print(f"  ratio of misinterpretation rates = {ratio:.2f}x")
    print(f"  in an audience of 200, the difference in misreadings is about "
          f"{200 * (P_INVERT_FREQUENCY - P_INVERT_PERCENT):.0f} people")
    print("  -> these rates are chosen teaching values, not measurements; the point")
    print("     is that framing is a design variable.  Test the sentence on someone")
    print("     who is not in the field before publishing it.")


if __name__ == "__main__":
    main()
