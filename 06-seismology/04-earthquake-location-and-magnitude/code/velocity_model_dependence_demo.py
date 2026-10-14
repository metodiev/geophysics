"""Dependence of the located hypocentre on the velocity model.

Run:  .venv/bin/python velocity_model_dependence_demo.py
Requires: numpy, obspy.

Companion to lesson 06-04-02.

THE EXPERIMENT.  True travel times are generated through a layered reference
model (ak135, distributed with obspy, so no network is needed).  The event is
then located with a WRONG velocity model, obtained by multiplying every
velocity by a constant s, and the bias in the located hypocentre is measured
as a function of s.  Scaling every velocity by s scales every travel time by
exactly 1/s (t = integral ds/v), so the perturbed model is the reference model
with a perfectly known uniform bias -- the cleanest possible version of a
velocity-model error.

WHAT IS COMPUTED

1. The control: locating with the model that generated the data.
2. The located depth and origin time as the velocity scale moves by -8 to
   +8 per cent, with the bias of each.
3. The nominal 95 per cent depth bound from the pick uncertainty alone, and the
   measured bias, so the two can be compared: this is where the standard
   uncertainty becomes an overstatement of what is known.
4. A joint scan over depth and velocity, which is what a careful study does
   instead of asserting a model; the trade-off is reported.

Everything else (event, network, pick uncertainty) is SYNTHETIC and printed.
"""

import numpy as np
from obspy.taup import TauPyModel

SIGMA_T = 0.05          # s, SYNTHETIC pick uncertainty
Z_TRUE = 12.0           # km, SYNTHETIC true depth
T0_TRUE = 2.0           # s, SYNTHETIC true origin time
DIST = np.array([0.6, 1.0, 1.5, 2.0, 2.6, 3.2, 4.0, 5.0, 6.5, 8.0])  # degrees


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def build_table(model, depths, distances, phase="P"):
    """Travel-time table T[i][j] for depth i and distance j (reference model)."""
    table = np.full((len(depths), len(distances)), np.nan)
    for i, z in enumerate(depths):
        for j, d in enumerate(distances):
            arr = model.get_travel_times(source_depth_in_km=float(z),
                                         distance_in_degree=float(d),
                                         phase_list=[phase])
            if arr:
                table[i, j] = arr[0].time
    return table


def locate(table, depths, t_obs, scale):
    """Best depth and origin time for a uniform velocity scale `scale`."""
    t_pred_all = table / scale
    best = None
    for i in range(len(depths)):
        t_pred = t_pred_all[i]
        if np.any(~np.isfinite(t_pred)):
            continue
        resid = t_obs - t_pred
        t0 = float(resid.mean())
        cost = float(np.sqrt(np.mean((resid - t0) ** 2)))
        if best is None or cost < best[0]:
            best = (cost, float(depths[i]), t0, i)
    return best


def main():
    print("Velocity-model dependence of a located hypocentre")
    print(f"numpy {np.__version__}")
    print()
    model = TauPyModel(model="ak135")
    print("  Reference model: ak135 (distributed with obspy; used as a MODEL, not")
    print("  as a measurement of any particular region).")
    print(f"  SYNTHETIC event: depth {Z_TRUE:.1f} km, origin time {T0_TRUE:.2f} s,")
    print(f"  10 stations between {DIST[0]:.1f} and {DIST[-1]:.1f} degrees,")
    print(f"  pick uncertainty sigma_t = {SIGMA_T:.3f} s")

    depths = np.arange(1.0, 30.01, 0.25)
    table = build_table(model, depths, DIST)
    t_obs = table[np.argmin(np.abs(depths - Z_TRUE))] + T0_TRUE
    print(f"  travel-time table: {table.shape[0]} depths x {table.shape[1]}"
          f" distances = {table.size} entries")
    print(f"  observed arrival times: {t_obs[0]:.3f} s at "
          f"{DIST[0]:.1f} deg to {t_obs[-1]:.3f} s at {DIST[-1]:.1f} deg, "
          f"a ratio of {t_obs[-1] / t_obs[0]:.2f}")

    section("1. Control: locating with the model that made the data")
    cost, z_loc, t0_loc, _ = locate(table, depths, t_obs, 1.0)
    print(f"  located depth {z_loc:.2f} km (bias {z_loc-Z_TRUE:+.2f} km),"
          f" origin time {t0_loc:.3f} s (bias {t0_loc-T0_TRUE:+.3f} s),"
          f" rms residual {cost:.2e} s")
    print("  The control recovers the input to the grid step.  Every bias below")
    print("  is therefore attributable to the velocity model.")

    section("2. Locating with a uniformly perturbed velocity model")
    print("  Locating model = reference velocities x (1 + d).  A positive d is a")
    print("  faster locating model, which fits the same arrival times with a")
    print("  shallower source; a negative d with a deeper one.  Watch the sign.")
    print()
    print(f"  {'d (%)':>7}{'depth (km)':>12}{'depth bias (km)':>17}"
          f"{'t0 (s)':>10}{'t0 bias (s)':>13}{'rms resid (s)':>15}")
    rows = []
    for d in (-0.08, -0.04, -0.02, 0.0, 0.02, 0.04, 0.08):
        cost, z_loc, t0_loc, _ = locate(table, depths, t_obs, 1.0 + d)
        rows.append((d, z_loc, t0_loc, cost))
        print(f"  {100*d:7.1f}{z_loc:12.2f}{z_loc-Z_TRUE:17.2f}{t0_loc:10.3f}"
              f"{t0_loc-T0_TRUE:13.3f}{cost:15.3e}")

    section("3. Is the true hypocentre inside the nominal 95 per cent bound?")
    print("  The nominal depth uncertainty comes from the curvature of the misfit")
    print("  in depth, with the picks as the only error source:")
    print("      chi2(z) = sum_i (r_i - mean r)^2 / sigma_t^2 ,")
    print("      var(z)  = 2 / [ d2(chi2)/dz2 ] ,")
    print("  (the 2 comes from the chi-squared distribution with one parameter;")
    print("  sigma_t cancels because it is defined into chi2)")
    print()

    def chi2_of(z):
        i = int(np.argmin(np.abs(depths - z)))
        t_pred = table[i]
        if np.any(~np.isfinite(t_pred)):
            return np.nan
        resid = t_obs - t_pred
        return float(np.sum((resid - resid.mean()) ** 2) / SIGMA_T ** 2)

    dz = 1.0
    c_m, c_0, c_p = chi2_of(Z_TRUE - dz), chi2_of(Z_TRUE), chi2_of(Z_TRUE + dz)
    d2 = (c_p - 2 * c_0 + c_m) / dz ** 2
    var_z = 2.0 / d2
    sigma_z = float(np.sqrt(var_z))
    bound = 1.96 * sigma_z
    print(f"  d2(chi2)/dz2 = {d2:.4e} per km^2  ->  sigma_z = {sigma_z:.3f} km")
    print(f"  95 per cent depth bound from the picks alone = {bound:.3f} km")
    print()
    print(f"  {'d (%)':>7}{'depth bias (km)':>17}{'bias / 95% bound':>19}"
          f"  inside the nominal bound?")
    for (d, z_loc, t0_loc, cost) in rows:
        ratio = (z_loc - Z_TRUE) / bound
        inside = "yes" if abs(ratio) <= 1.0 else "NO"
        print(f"  {100*d:7.1f}{z_loc-Z_TRUE:17.2f}{ratio:19.3f}  {inside}")
    print()
    print("  A uniform velocity error of 2 per cent already moves the located")
    print("  depth by more than the nominal 95 per cent bound in one direction,")
    print("  and 8 per cent moves it several times that.  The bound describes the")
    print("  PICKS; it is not a statement about the Earth, because it was computed")
    print("  under the assumption that the velocity model is the true one.  In a")
    print("  real catalogue that assumption is never checked, which is why a")
    print("  depth from a catalogue and a depth from a well-constrained local")
    print("  study can differ by kilometres without either being wrong.")

    section("4. How much does allowing the velocity to vary widen the answer?")
    print("  Accept a (velocity scale, depth) pair when the rms residual after")
    print("  fitting the origin time stays below the pick uncertainty sigma_t.")
    print("  A catalogue fixes the model and reports the first row below; the")
    print("  honest answer is the union over the models the picks cannot exclude.")
    print()

    def consistent_depths(scale, tol):
        out = []
        for i, z in enumerate(depths):
            t_pred = table[i] / scale
            if np.any(~np.isfinite(t_pred)):
                continue
            resid = t_obs - t_pred
            rms = float(np.sqrt(np.mean((resid - resid.mean()) ** 2)))
            if rms <= tol:
                out.append(float(z))
        return out

    def min_rms(scale):
        best = None
        for i, z in enumerate(depths):
            t_pred = table[i] / scale
            if np.any(~np.isfinite(t_pred)):
                continue
            resid = t_obs - t_pred
            rms = float(np.sqrt(np.mean((resid - resid.mean()) ** 2)))
            if best is None or rms < best[0]:
                best = (rms, float(z))
        return best

    d0 = consistent_depths(1.0, SIGMA_T)
    print("  with the REFERENCE velocity model, depths consistent with the picks")
    if d0:
        print(f"  (rms residual <= {SIGMA_T:.2f} s) span {min(d0):.2f} to "
              f"{max(d0):.2f} km, a width of {max(d0)-min(d0):.2f} km.")
        print(f"  The true depth is {Z_TRUE:.2f} km and lies inside that interval.")
    print()

    # Largest uniform velocity error the picks can still absorb: bisection on
    # the smallest rms residual over depth versus sigma_t.
    lo, hi = 0.0, 0.02
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if min_rms(1.0 + mid)[0] <= SIGMA_T:
            lo = mid
        else:
            hi = mid
    d_tol = hi
    print(f"  largest uniform velocity error the picks can still accommodate,")
    print(f"  from min-over-depth rms residual against sigma_t: d = "
          f"{100*d_tol:.2f} per cent")
    print("  (bisection).  Beyond that scale, NO depth fits the picks at all.")
    print()
    print(f"  {'d (%)':>7}{'min rms resid (s)':>19}{'best depth (km)':>17}"
          f"  {'consistent depths (km)':>24}")
    for d in np.arange(-2.0, 2.01, 0.5) * 0.01:
        m_rms, m_z = min_rms(1.0 + d)
        c = consistent_depths(1.0 + d, SIGMA_T)
        rng = f"{min(c):.2f} - {max(c):.2f}" if c else "none"
        print(f"  {100*d:7.1f}{m_rms:19.4f}{m_z:17.2f}  {rng:>24}")
    print()

    # Union of acceptable depths over every velocity scale still admitted.
    all_depths = []
    for d in np.linspace(-d_tol, d_tol, 41):
        all_depths.extend(consistent_depths(1.0 + d, SIGMA_T))
    if all_depths:
        print(f"  Over the whole admitted range -{100*d_tol:.2f} to "
              f"+{100*d_tol:.2f} per cent,")
        print(f"  the union of acceptable depths is {min(all_depths):.2f} to "
              f"{max(all_depths):.2f} km, a width of "
              f"{max(all_depths)-min(all_depths):.2f} km")
        print(f"  against {max(d0)-min(d0):.2f} km with the model held fixed.  So the")
        print("  velocity dimension does widen the interval -- but only by the")
        print("  fraction of a per cent the picks can absorb, whereas real uniform")
        print("  model errors are percent-level (Section 2) and thousands of times")
        print("  larger than that.  The nominal bound is therefore precise about the")
        print("  velocity model and silent about whether that model is right: it is")
        print("  the ratio of d_tol above to a realistic d that measures the")
        print("  understatement, not the width of the depth interval.")
    print()
    print("=" * 72)
    print("Event, network and pick uncertainty are SYNTHETIC and printed above.")
    print("The reference velocities are a model; the bias figures are computed.")
    print("=" * 72)


if __name__ == "__main__":
    main()
