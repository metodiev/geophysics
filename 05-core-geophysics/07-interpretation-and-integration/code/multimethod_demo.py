"""Multi-method integration: what a second dataset really buys, and when it fails.

Seven measurements of the same structure, all produced by this script:

  1. A magnetotelluric (MT) response is validated against its own exact limits --
     a half-space must return its own resistivity, and the short-period limit must
     return the top layer.
  2. The MT response of a three-layer model is inverted by grid search.  The set
     of models that fits to 1 per cent is a *curve*: conductance h/rho is
     constrained several times better than either factor.  This is the EM
     equivalent of the potential-field equivalent stratum.
  3. The conductance equivalence is shown directly: three models with equal
     conductance but thicknesses spanning a factor of four have indistinguishable
     MT responses -- and a fourth, no longer thin, breaks it.
  4. A seismic thickness measurement (independent physics: elasticity) intersects
     the MT feasible curve.  Its effect is quantified, and it is not total.
  5. A borehole conductivity measurement narrows the set further.  The basement
     resistivity is shown to be genuinely constrained, and the *sharpness* of the
     boundary is shown not to be.  Ambiguity and insensitivity are separated.
  6. A conflicting seismic pick is introduced.  The minimum MT misfit it would
     require is far outside the MT tolerance: both datasets cannot be right.
  7. A self-consistency test: the adopted model is used to predict an independent
     sounding, and the prediction fails.

All layer resistivities, thicknesses, tolerances and noise levels are SYNTHETIC.

Run:  python3 multimethod_demo.py
"""

from __future__ import annotations

import numpy as np

MU0 = 4.0e-7 * np.pi  # H/m


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def mt_rho_a(periods, layers):
    """Apparent resistivity of a 1-D layered earth for each period (s).

    `layers` is a list of (resistivity, thickness); the final thickness is ignored
    because the last layer is a half-space.
    """
    out = np.empty(len(periods))
    for j, T in enumerate(periods):
        w = 2.0 * np.pi / T
        k = np.sqrt(1j * w * MU0 / layers[-1][0])
        Z = 1j * w * MU0 / k
        for i in range(len(layers) - 2, -1, -1):
            rho_i, h_i = layers[i]
            k_i = np.sqrt(1j * w * MU0 / rho_i)
            Z_int = 1j * w * MU0 / k_i
            t = np.tanh(k_i * h_i)
            Z = Z_int * (Z + Z_int * t) / (Z_int + Z * t)
        out[j] = abs(Z) ** 2 / (w * MU0)
    return out


def log_misfit(a, b):
    return float(np.sqrt(np.mean((np.log10(a) - np.log10(b)) ** 2)))


def main() -> None:
    periods = np.logspace(-2, 3, 21)   # SYNTHETIC: 0.01 s to 1000 s
    rho1, h1 = 100.0, 100.0            # SYNTHETIC overburden
    rho2_true, h2_true = 10.0, 300.0   # SYNTHETIC target layer
    rho3 = 500.0                       # SYNTHETIC basement
    truth = mt_rho_a(periods, [(rho1, h1), (rho2_true, h2_true), (rho3, np.inf)])

    section("1. Validation of the MT forward operator against exact limits")
    ra = mt_rho_a(periods, [(50.0, 1.0e6)])
    print(f"half-space rho = 50 ohm m -> max relative error in rho_a = "
          f"{np.max(np.abs(ra / 50.0 - 1.0)):.2e}")
    short = np.logspace(-6, -5, 6)
    two = mt_rho_a(short, [(50.0, 100.0), (5.0, 1.0e6)])
    print(f"two-layer, T = 1e-6 to 1e-5 s: rho_a = {two.min():.4f} to "
          f"{two.max():.4f} ohm m (top layer is 50)")
    at_0p01 = mt_rho_a(periods, [(50.0, 100.0), (5.0, 1.0e6)])[0]
    print(f"at T = 0.01 s the same model returns {at_0p01:.2f} ohm m: the skin")
    print("depth (the 503 sqrt(rho T) rule) already exceeds the 100 m layer, so "
          "the\nshort-period limit is not reached.  Resistivity resolution is read "
          "off a\nsounding curve in exactly this way.")

    section("2. The MT feasible set for a three-layer earth")
    h2s = np.linspace(80.0, 900.0, 200)
    rho2s = np.logspace(0.4, 2.6, 200)
    rows = []
    for h2 in h2s:
        for r2 in rho2s:
            trial = mt_rho_a(periods, [(rho1, h1), (r2, h2), (rho3, np.inf)])
            mis = log_misfit(trial, truth)
            if mis < 0.01:
                rows.append((h2, r2, mis))
    feas = np.array(rows)
    cond = feas[:, 0] / feas[:, 1]
    print(f"models searched                = {h2s.size * rho2s.size}")
    print(f"models within 1 per cent       = {feas.shape[0]}")
    print(f"thickness range                = {feas[:, 0].min():.0f} to "
          f"{feas[:, 0].max():.0f} m   (truth {h2_true:.0f} m)")
    print(f"resistivity range              = {feas[:, 1].min():.2f} to "
          f"{feas[:, 1].max():.2f} ohm m   (truth {rho2_true:.2f})")
    print(f"conductance h/rho along the set= {cond.min():.1f} to {cond.max():.1f} m "
          f"ohm^-1   (truth {h2_true / rho2_true:.1f})")
    spread_h = 100 * (feas[:, 0].max() - feas[:, 0].min()) / feas[:, 0].mean()
    spread_c = 100 * (cond.max() - cond.min()) / cond.mean()
    print(f"relative spread of thickness   = {spread_h:.1f} per cent")
    print(f"relative spread of conductance = {spread_c:.1f} per cent")
    print("The feasible set is a curve.  Thickness and resistivity each vary about "
          f"{spread_h / spread_c:.1f} times\nas much as their product; the data "
          "constrain the conductance, and the factors\nonly as well as the curve "
          "is narrow.")

    section("3. Direct conductance equivalence, and where it breaks")
    bp = np.logspace(1, 3, 9)
    ref = mt_rho_a(bp, [(rho1, h1), (1.0, 50.0), (rho3, np.inf)])
    for h2, r2 in ((50.0, 1.0), (100.0, 2.0), (200.0, 4.0), (1000.0, 20.0)):
        trial = mt_rho_a(bp, [(rho1, h1), (r2, h2), (rho3, np.inf)])
        print(f"h2 = {h2:6.0f} m, rho2 = {r2:5.1f} ohm m, conductance = "
              f"{h2 / r2:5.1f} m/ohm : log-RMS vs the 50 m / 1 ohm model = "
              f"{log_misfit(trial, ref):.4f}")
    print("The first three share a conductance of 50 m/ohm and agree to 0.002 in\n"
          "log10 (0.5 per cent): a factor of four in thickness, essentially\n"
          "invisible.  The fourth has the same conductance but is no longer thin\n"
          "compared with the skin depth, and the equivalence fails sixfold.\n"
          "Equivalence is a regime, not a law.")

    section("4. A seismic thickness (independent physics) intersects the set")
    h_seis, sigma_seis = 300.0, 15.0   # SYNTHETIC pick and uncertainty, m
    keep = np.abs(feas[:, 0] - h_seis) < sigma_seis
    print(f"seismic thickness = {h_seis:.0f} +/- {sigma_seis:.0f} m")
    print(f"MT models compatible           = {keep.sum()} of {feas.shape[0]}")
    print(f"thickness range after intersection = {feas[keep, 0].min():.0f} to "
          f"{feas[keep, 0].max():.0f} m")
    print(f"resistivity range after intersection = {feas[keep, 1].min():.2f} to "
          f"{feas[keep, 1].max():.2f} ohm m")
    narrowing = ((feas[:, 1].max() - feas[:, 1].min())
                 / (feas[keep, 1].max() - feas[keep, 1].min()))
    spread_h_seis = (100 * (feas[keep, 0].max() - feas[keep, 0].min())
                     / feas[keep, 0].mean())
    print(f"thickness spread falls from {spread_h:.1f} to {spread_h_seis:.1f} per "
          "cent")
    print(f"resistivity range narrowed by a factor of {narrowing:.1f}, not "
          "collapsed.")
    print("Elasticity and electromagnetism are physically independent, which is why "
          "this\nis a joint constraint rather than a re-weighting.  But note how "
          "little it buys on\nresistivity: because the MT feasible set is already a "
          "curve, a thickness\nconstraint mostly trims its ends.  A second dataset "
          "is worth most when its\nsensitivity is *transverse* to the first's.")

    section("5. A borehole conductivity measurement, and what remains")
    rho_bh, sigma_bh = 10.0, 1.0       # SYNTHETIC core/log value, ohm m
    keep2 = keep & (np.abs(feas[:, 1] - rho_bh) < sigma_bh)
    print(f"borehole resistivity = {rho_bh:.1f} +/- {sigma_bh:.1f} ohm m")
    print(f"models surviving all three constraints = {keep2.sum()}")
    print(f"thickness range = {feas[keep2, 0].min():.0f} to "
          f"{feas[keep2, 0].max():.0f} m; rho2 range = "
          f"{feas[keep2, 1].min():.2f} to {feas[keep2, 1].max():.2f} ohm m")
    fix_h = float(feas[keep2, 0].mean())
    fix_rho = float(feas[keep2, 1].mean())

    print("\nsensitivity of the response to the basement, at fixed 100/10/300 m:")
    for factor in (2.0, 0.5):
        alt = mt_rho_a(periods, [(rho1, h1), (rho2_true, h2_true),
                                 (rho3 * factor, np.inf)])
        print(f"  basement resistivity x{factor:3.1f}: max change in rho_a = "
              f"{100 * np.max(np.abs(alt / truth - 1.0)):6.2f} per cent")
    print("The basement is genuinely constrained: a factor of two in basement "
          "resistivity\nmoves the response by tens of per cent at the longest "
          "periods.  Being\nunresolved is not the same as being invisible.")

    print("\nboundary sharpness, at fixed conductivity above and below:")
    for ramp in (25.0, 100.0, 200.0):
        n = 20
        mids = (np.arange(n) + 0.5) / n
        rho_ramp = 10.0 * (rho3 / 10.0) ** mids
        graded = ([(rho1, h1), (rho2_true, h2_true - ramp / 2)]
                  + [(float(r), ramp / n) for r in rho_ramp] + [(rho3, np.inf)])
        print(f"  transition zone {ramp:5.0f} m thick: log-RMS vs a sharp boundary "
              f"= {log_misfit(mt_rho_a(periods, graded), truth):.4f}")
    print("A 25 m transition is indistinguishable from a sharp boundary at the 1 "
          "per cent\ntolerance; a 100 m transition already misfits by 3 per cent.  "
          "So MT constrains\nthe transition to be thinner than roughly 50 m -- it "
          "does not prove the boundary\nis sharp, and on a fault or an "
          "unconformity the difference matters.")

    section("6. A conflicting seismic pick: both datasets cannot be right")
    h_bad = 150.0
    mis = [log_misfit(mt_rho_a(periods, [(rho1, h1), (r2, h_bad), (rho3, np.inf)]),
                      truth) for r2 in rho2s]
    print(f"seismic pick h2 = {h_bad:.0f} m; best achievable MT log-misfit over "
          f"all rho2 = {min(mis):.4f}")
    print("MT tolerance in these synthetic data = 0.0100 (1 per cent)")
    print(f"required misfit / tolerance = {min(mis) / 0.01:.1f}")
    print("Nothing MT can tolerate produces a 150 m layer.  One dataset is wrong, "
          "or one\nmodel is wrong, or both.  Integration does not manufacture "
          "agreement; it\nexposes disagreement, which is more useful and much less "
          "comfortable.")

    section("7. Self-consistency test: does the model predict an independent "
            "observation?")
    print(f"adopted model: h2 = {fix_h:.1f} m, rho2 = {fix_rho:.2f} ohm m")
    h_true_new = 420.0
    truth2 = mt_rho_a(periods, [(rho1, h1), (rho2_true, h_true_new), (rho3, np.inf)])
    pred2 = mt_rho_a(periods, [(rho1, h1), (fix_rho, fix_h), (rho3, np.inf)])
    print(f"a nearby sounding has a {h_true_new:.0f} m layer instead of "
          f"{h2_true:.0f} m")
    print(f"model prediction vs that sounding: log-RMS = "
          f"{log_misfit(pred2, truth2):.4f}")
    print("The model interpolates its own data and fails to predict the "
          "neighbouring\nsounding, because the layer is not laterally uniform and "
          "the 1-D model was an\nassumption.  A prediction test like this is the "
          "cheapest available check and\nis almost never run.")


if __name__ == "__main__":
    main()
