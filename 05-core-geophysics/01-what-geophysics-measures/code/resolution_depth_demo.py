"""Resolution versus depth: the trade-off measured, not asserted.

Two claims are tested numerically for the gravity field of point sources:

  (a) the WIDTH of an anomaly grows in proportion to source depth, so the
      lateral resolution of a potential-field survey degrades linearly with
      depth (measured exponent reported); and
  (b) two equal sources separated by s at depth d become indistinguishable
      below a separation that is itself proportional to d (measured).

Both are properties of the 1/r^2 kernel and its harmonic decay, not of any
instrument, though the noise floor sets the depth at which (b) bites.

All sources are SYNTHETIC: point masses of stated size at stated depths.

Run:  python3 resolution_depth_demo.py
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11  # m^3 kg^-1 s^-2 (CODATA 2018, NIST)
MGAL = 1.0e-5    # m/s^2 per mGal


def gz_point(masses, xs, depth, x_obs):
    """Sum of vertical point-mass anomalies on a line of stations."""
    total = np.zeros_like(x_obs)
    for m, x_s in zip(masses, xs):
        r = np.hypot(x_obs - x_s, depth)
        total += G * m * depth / r**3
    return total


def half_width(mass, depth, n=20001):
    """Distance from the peak at which the anomaly falls to half its peak."""
    span = 20.0 * depth
    x = np.linspace(-span, span, n)
    g = gz_point([mass], [0.0], depth, x)
    peak = g[n // 2]
    half = peak / 2.0
    idx = np.where(g >= half)[0]
    return x[idx[-1]] - x[idx[0]]


def min_resolvable_separation(depth, mass=1.0e10, threshold=0.01, n=20001):
    """Smallest s at which the midline still shows a dip of > threshold.

    Criterion: resolvable if the anomaly at the midpoint between the two
    sources falls at least `threshold` (a fraction) below the two off-centre
    peaks.  This is a stated, arbitrary but reproducible convention.
    """
    lo, hi = 1.0e-3 * depth, 10.0 * depth
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        x = np.linspace(-4.0 * depth, 4.0 * depth, n)
        g = gz_point([mass, mass], [-mid / 2, mid / 2], depth, x)
        g_mid = gz_point([mass, mass], [-mid / 2, mid / 2], depth,
                         np.array([0.0]))[0]
        g_peak = float(np.max(g))
        dip = 1.0 - g_mid / g_peak
        if dip >= threshold:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    mass = 1.0e10  # kg, SYNTHETIC point mass

    section("1. Anomaly width scales with depth")
    print("   depth(m)   half-width(m)   hw/depth")
    depths = np.array([100.0, 200.0, 400.0, 800.0, 1600.0])
    hws = np.array([half_width(mass, d) for d in depths])
    for d, hw in zip(depths, hws):
        print(f"  {d:9.0f}   {hw:13.3f}   {hw/d:8.5f}")
    slope = np.polyfit(np.log(depths), np.log(hws), 1)[0]
    analytic = 2.0 * np.sqrt(2.0 ** (2.0 / 3.0) - 1.0)
    print(f"  measured log-log slope d(log hw)/d(log depth) = {slope:.6f}")
    print(f"  closed form: g(x)/g(0) = 1/2  =>  hw = {analytic:.6f} * depth")
    print(f"  measured hw/depth = {hws[0]/depths[0]:.6f} ; relative diff = "
          f"{abs(hws[0]/depths[0] - analytic)/analytic:.3e}")
    print("  The exponent is 1 to within numerical precision: width is")
    print("  directly proportional to depth.  Doubling the depth halves the")
    print("  lateral resolution.  No instrument can escape this; it is in")
    print("  the kernel.")

    section("2. Minimum resolvable separation scales with depth")
    print("   depth(m)    s_min(m)    s_min/depth")
    seps = []
    for d in depths:
        s = min_resolvable_separation(float(d), mass=mass)
        seps.append(s)
        print(f"  {d:9.0f}   {s:10.3f}   {s/d:11.5f}")
    seps = np.array(seps)
    slope2 = np.polyfit(np.log(depths), np.log(seps), 1)[0]
    print(f"  measured log-log slope d(log s_min)/d(log depth) = {slope2:.6f}")
    print("  Two sources must be separated by a fixed fraction of their depth")
    print("  to be separately visible.  This is the classical 'depth rule'.")
    print("  (The fraction depends on the detectability threshold chosen).")

    section("3. Noise converts the trade-off into a hard depth limit")
    peak = G * mass / (100.0**2) / MGAL
    print(f"  SYNTHETIC point mass {mass:.1e} kg at 100 m: "
          f"peak g_z = {peak:.4f} mGal")
    print("   depth(m)   peak(mGal)   peak/noise (noise=0.01 mGal)")
    for d in depths:
        p = G * mass / (d**2) / MGAL
        print(f"  {d:9.0f}   {p:9.5f}   {p/0.01:20.2f}")
    print("  Amplitude decays as 1/depth^2 while width grows as depth.  The")
    print("  information content of the anomaly therefore falls as roughly")
    print("  1/depth^3 once the noise floor is reached.  This is why deep")
    print("  targets need large contrasts, big arrays, or long integration.")

    print("\nSUMMARY: resolution and depth are not independent knobs.  The")
    print("physics fixes their product; the survey design only chooses where")
    print("on that trade-off to sit.")


if __name__ == "__main__":
    main()
