"""What a SINGLE seismometer can and cannot determine.

A single three-component station on a planetary surface measures:
   (i)  the P arrival time          tP
   (ii) the S arrival time          tS   -> hence tS - tP
   (iii) the P polarisation: an azimuth (from the two horizontal components) and
         an incidence angle (from the ratio of vertical to horizontal motion).

Model used here (STATED, and idealised): straight rays in a homogeneous
half-space with no free-surface conversion,
    tP = R / Vp ,   tS = R / Vs ,   R = sqrt(Delta^2 + h^2) ,
    incidence i = atan(Delta / h) ,
where Delta is the epicentral distance, h the source depth and R the slant range.
This is a BODY-WAVE model, valid only at distances small enough that rays are
nearly straight; at regional distances a layered model and converted phases are
required, which is exactly one of the limitations the demo measures.

Experiments
  A. The trade-off curve from (tS - tP) alone: the family of (Delta, h) that
     reproduces the measured time difference.
  B. Add the polarisation incidence angle: the family collapses -- and how
     sensitive the result is to the assumed Vp/Vs.
  C. Remove the velocity model: what is left is a one-parameter family.  Measured
     range of Delta over a plausible Vp span.
  D. Deep versus shallow: how much location information the incidence angle
     carries, as a function of Delta/h.
  E. Add a second station: the trade-off collapses with no polarisation at all.
  F. Azimuth from the horizontal components, and its noise sensitivity.

Run:  <repo>/.venv/bin/python planetary_single_station_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import brentq

# ----------------------------------------------------------------------
# MODEL inputs (chosen, not measured)
# ----------------------------------------------------------------------
VP = 6.00e3            # m/s   MODEL P-wave speed, homogeneous half-space
VS = 3.46e3            # m/s   MODEL S-wave speed (Vp/Vs = 1.734)
DELTA_TRUE = 40.0e3    # m     MODEL true epicentral distance
H_TRUE = 10.0e3        # m     MODEL true source depth
SIGMA_TP = 0.05        # s     MODEL pick uncertainty on a time difference
VP_LO, VP_HI = 3.0e3, 8.0e3    # m/s  MODEL plausible Vp range without a model

LINES = "=" * 78


def section(title: str) -> None:
    print(f"\n{LINES}\n{title}\n{LINES}")


def times(delta: np.ndarray, h: np.ndarray, vp: float = VP, vs: float = VS):
    r = np.sqrt(delta ** 2 + h ** 2)
    return r / vp, r / vs, r


def incidence_deg(delta: np.ndarray, h: np.ndarray) -> np.ndarray:
    return np.degrees(np.arctan2(delta, h))


def main() -> int:
    print("Single-station location: what one three-component record determines")
    print(f"MODEL: Vp = {VP / 1e3:.2f} km/s, Vs = {VS / 1e3:.2f} km/s "
          f"(Vp/Vs = {VP / VS:.3f})")
    print(f"       true source: Delta = {DELTA_TRUE / 1e3:.1f} km, "
          f"h = {H_TRUE / 1e3:.1f} km")
    print(f"       pick uncertainty on tS - tP: sigma = {SIGMA_TP:.3f} s")

    tp, ts, r_true = times(np.array([DELTA_TRUE]), np.array([H_TRUE]))
    dts = float(ts[0] - tp[0])
    inc_true = float(incidence_deg(np.array([DELTA_TRUE]), np.array([H_TRUE]))[0])
    print(f"  forward model: tP = {float(tp[0]):.4f} s, tS = {float(ts[0]):.4f} s, "
          f"tS - tP = {dts:.4f} s")
    print(f"                slant range R = {float(r_true[0]):.1f} m, "
          f"P incidence angle = {inc_true:.4f} deg")

    # ------------------------------------------------------------------
    section("A. (tS - tP) alone: the range-depth trade-off curve")
    delta = np.linspace(1e3, 200e3, 200000)
    for h_try in (H_TRUE,):
        tp2, ts2, _ = times(delta, np.full_like(delta, h_try))
        d2 = ts2 - tp2
        ok = np.abs(d2 - dts) <= SIGMA_TP
        print(f"  with h fixed at {h_try / 1e3:.1f} km, only Delta near "
              f"{DELTA_TRUE / 1e3:.1f} km fits.")
    # Now solve for h as a function of Delta so that the time difference matches,
    # then ask how wide the acceptable band is.
    def r_needed(d_ts: float, vp: float = VP, vs: float = VS) -> float:
        return d_ts / (1.0 / vs - 1.0 / vp)

    r_lo = r_needed(dts - SIGMA_TP)
    r_hi = r_needed(dts + SIGMA_TP)
    print(f"\n  the time difference constrains the SLANT RANGE R: "
          f"{r_lo / 1e3:.3f} to {r_hi / 1e3:.3f} km")
    print(f"  true R = {float(r_true[0]) / 1e3:.3f} km; so sigma_t = "
          f"{SIGMA_TP:.2f} s is a {100 * (r_hi - r_lo) / 2 / float(r_true[0]):.2f} % "
          f"constraint on R")
    print("\n   Delta [km]   h required [km]   to match tS - tP within sigma")
    rows = []
    for d_km in (5.0, 10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 150.0):
        d = d_km * 1e3
        with np.errstate(invalid="ignore"):
            h_req = np.sqrt(max(float(r_lo) ** 2 - d ** 2, 0.0))
        rows.append((d_km, h_req / 1e3))
        print(f"  {d_km:11.1f}   {h_req / 1e3:17.3f}")
    print("  Every one of those (Delta, h) pairs reproduces the measured time")
    print("  difference to within the pick uncertainty.  One station's S-P time is")
    print("  a RANGE measurement, and a range is a curve in the (Delta, h) plane.")

    # ------------------------------------------------------------------
    section("B. Adding the polarisation incidence angle")
    def solve_from_incidence(inc_deg: float, vp: float = VP, vs: float = VS,
                             d_ts: float = dts) -> tuple[float, float]:
        """Solve R and Delta from (tS - tP, incidence) for a given velocity model."""
        def f(d):
            h = d / np.tan(np.radians(inc_deg))
            return np.sqrt(d ** 2 + h ** 2) - r_needed(d_ts, vp, vs)
        d_sol = brentq(f, 1.0, 1e6)
        return d_sol, d_sol / np.tan(np.radians(inc_deg))

    d_sol, h_sol = solve_from_incidence(inc_true)
    print(f"  with the model velocities, the pair collapses to")
    print(f"    Delta = {d_sol / 1e3:.4f} km, h = {h_sol / 1e3:.4f} km")
    print(f"    (true {DELTA_TRUE / 1e3:.4f} km, {H_TRUE / 1e3:.4f} km)")
    print("\n  But the velocities are MODEL inputs.  Sensitivity of the distance to")
    print("  a velocity error, holding the two observations fixed:")
    print("\n   Vp/Vs error [%]   Vp [km/s]   Delta [km]   h [km]   d(Delta) [%]")
    for err in (-10.0, -5.0, -1.0, 0.0, 1.0, 5.0, 10.0):
        vs_try = VP / (VP / VS * (1.0 + err / 100.0))
        d2, h2 = solve_from_incidence(inc_true, VP, vs_try)
        print(f"  {err:16.1f}   {VP / 1e3:10.2f}   {d2 / 1e3:11.4f}   "
              f"{h2 / 1e3:8.4f}   {100 * (d2 - DELTA_TRUE) / DELTA_TRUE:11.2f}")
    vs_try = VP / (VP / VS * 1.01)
    d2, _ = solve_from_incidence(inc_true, VP, vs_try)
    print(f"  A 1 % error in Vp/Vs moves the epicentral distance by "
          f"{abs(100 * (d2 - DELTA_TRUE) / DELTA_TRUE):.2f} %.")
    print("  At 40 km that is hundreds of metres -- and the sign of the error is not")
    print("  knowable from the record.")

    # ------------------------------------------------------------------
    section("C. With no velocity model at all, one station cannot locate")
    print("  Unknowns: Delta, h, Vp, Vs (4).  Observations: tP, tS - tP, incidence")
    print("  (3).  One degree of freedom remains, so the solution is a CURVE.")
    print("\n   assumed Vp [km/s]   Vs [km/s]   Delta [km]   h [km]   implied tP [s]")
    for vp_try in (3.0e3, 4.0e3, 5.0e3, 6.0e3, 7.0e3, 8.0e3):
        ratio = VP / VS
        vs_c = vp_try / ratio
        r_use = r_needed(dts, vp_try, vs_c)
        d_use = r_use * np.sin(np.radians(inc_true))
        h_use = r_use * np.cos(np.radians(inc_true))
        print(f"  {vp_try / 1e3:19.2f}   {vs_c / 1e3:10.2f}   {d_use / 1e3:11.2f}   "
              f"{h_use / 1e3:8.2f}   {r_use / vp_try:15.4f}")
    d_lo = r_needed(dts, VP_LO, VP_LO / (VP / VS)) * np.sin(np.radians(inc_true))
    d_hi = r_needed(dts, VP_HI, VP_HI / (VP / VS)) * np.sin(np.radians(inc_true))
    print(f"\n  over Vp from {VP_LO / 1e3:.0f} to {VP_HI / 1e3:.0f} km/s the distance")
    print(f"  ranges from {d_lo / 1e3:.1f} to {d_hi / 1e3:.1f} km -- a factor of "
          f"{d_hi / d_lo:.2f} -- and EVERY one of those models")
    print("  fits the record exactly.  This is the degeneracy that makes single-station")
    print("  location a modelling problem, not a measurement.")

    # ------------------------------------------------------------------
    section("D. How much the incidence angle is worth, versus Delta/h")
    print("  For a straight ray, Delta = h tan(i), so")
    print("      dDelta/di   = h sec^2(i)         (absolute, depends on h)")
    print("      dlnDelta/di = 2 / sin(2i)        (FRACTIONAL, independent of h)")
    print("  The fractional sensitivity is MINIMISED near i = 45 degrees and grows")
    print("  towards BOTH the near-vertical (source almost directly beneath) and the")
    print("  near-horizontal (distant) limits.  Measure it:")
    print()
    print("   Delta/h   incidence [deg]   h [km]   dDelta/di [km/deg]   "
          "dlnDelta/di [%/deg]")
    for ratio in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 5.0, 10.0):
        inc = np.degrees(np.arctan2(ratio, 1.0))
        h_use = DELTA_TRUE / ratio
        abs_deriv = h_use * (1.0 / np.cos(np.radians(inc))) ** 2 * np.pi / 180.0
        frac = (2.0 / np.sin(2.0 * np.radians(inc))) * np.pi / 180.0 * 100.0
        print(f"  {ratio:8.2f}   {inc:16.2f}   {h_use / 1e3:8.2f}   "
              f"{abs_deriv / 1e3:19.3f}   {frac:19.2f}")
    print()
    print("  Two honest readings:")
    print("   - For an event at Delta ~ h (i ~ 45 deg) a 1 degree polarisation error")
    print("     costs about 3.5 % of the distance -- the best case.")
    print("   - For a near-horizontal ray (Delta >> h) it costs about 17 % per")
    print("     degree, and for a near-vertical ray (Delta << h) the distance is")
    print("     simply not determined by i at all, because Delta = h tan(i) is then")
    print("     almost independent of h.  Polarisation is thus a WEAK constraint in")
    print("     both limits, and the widely repeated claim that polarisation makes a")
    print("     single station sufficient is true only near i = 45 degrees.")

    section("E. A second station: geometry matters as much as count")
    sigma_r = SIGMA_TP / (1.0 / VS - 1.0 / VP)
    print(f"  A {SIGMA_TP * 1e3:.0f} ms pick uncertainty on tS - tP is a range")
    print(f"  uncertainty of sigma_R = sigma_t / (1/Vs - 1/Vp) = {sigma_r:.1f} m.")
    print("  Two stations separated by a baseline b give two ranges.  For a source at")
    print("  perpendicular distance d from the baseline, the two ranges differ by an")
    print("  amount whose sensitivity to d is d/r, so the perpendicular uncertainty is")
    print("      sigma_d = sigma_R * r / d .")
    print("  A source near the baseline is therefore very poorly located")
    print("  perpendicular to it, no matter how good the picks are.")
    print()
    print("   b [km]   d [km]   r [km]   sigma_d [m]   sigma_d / b")
    for b_km in (10.0, 20.0, 50.0):
        for d_km in (0.5, 1.0, 5.0, 20.0, 100.0):
            b = b_km * 1e3
            d = d_km * 1e3
            r_use = np.sqrt(d ** 2 + (b / 2.0) ** 2)
            sd = sigma_r * r_use / d
            print(f"  {b_km:7.1f}   {d_km:8.1f}   {r_use / 1e3:8.2f}   "
                  f"{sd:12.1f}   {sd / b:12.4f}")
    print()
    print("  More stations do not fix this: azimuthal COVERAGE does.  That is why")
    print("  planetary single-station experiments are supplemented by an independent")
    print("  constraint on R (a velocity model, a second phase, or a known depth),")
    print("  not by a better three-component sensor.")

    section("F. Azimuth: the part a single station DOES determine well")
    rng = np.random.default_rng(20261014)
    az_true = 137.0
    print("  The horizontal polarisation gives the azimuth directly, and the")
    print("  azimuth is not coupled to the velocity model.")
    print("\n   S/N per horizontal component   azimuth s.d. [deg]   p90 error [deg]")
    for snr in (2.0, 5.0, 10.0, 50.0, 200.0):
        sig = np.degrees(1.0 / snr) / np.sqrt(2.0)
        est = az_true + rng.normal(0.0, sig, 20000)
        sd = float(np.std(est - az_true))
        p90 = float(np.percentile(np.abs(est - az_true), 90))
        print(f"  {snr:28.1f}   {sd:19.3f}   {p90:16.3f}")
    print("  Azimuth is the one geometric quantity a single station gives cheaply,")
    print("  and it is a BACK-AZIMUTH (a ray direction), not a source location.")

    # ------------------------------------------------------------------
    section("Summary of measured quantities")
    print(f"  tS - tP constrains the slant range to "
          f"{r_lo / 1e3:.3f}-{r_hi / 1e3:.3f} km; a curve in (Delta, h).")
    print(f"  a {SIGMA_TP * 1e3:.0f} ms pick uncertainty is sigma_R = "
          f"{sigma_r:.1f} m in range")
    print(f"  with the model velocities + incidence, Delta = {d_sol / 1e3:.4f} km")
    print(f"  a 1 % Vp/Vs error moves Delta by "
          f"{abs(100 * (d2 - DELTA_TRUE) / DELTA_TRUE):.2f} %")
    print(f"  with NO velocity model, Vp in {VP_LO / 1e3:.0f}-{VP_HI / 1e3:.0f} km/s "
          f"spans Delta = {d_lo / 1e3:.1f}-{d_hi / 1e3:.1f} km (factor "
          f"{d_hi / d_lo:.2f})")
    print("  Everything above is a MODEL result for a stated straight-ray geometry.")
    print("  The structural conclusions -- range not depth, velocity-model")
    print("  dependence, weak polarisation for deep events -- follow from the")
    print("  geometry and are independent of the particular numbers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
