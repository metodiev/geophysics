#!/usr/bin/env python3
"""Survey geometry: fold, offsets, and the resolution-versus-depth trade-off.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geometry_fold_demo.py

Contents
--------
1. Fold is MEASURED, not asserted: source and receiver positions are generated,
   common midpoints (CMPs) are computed and binned, and the number of traces per
   bin is counted for several receiver counts.
2. The offset distribution (fold versus offset) for the same geometry.
3. Fresnel-zone resolution versus depth for a stated dominant wavelength.
4. The two-body separation limit for a potential field: two equal point masses at
   depth h, separated by s, with the measured midpoint-to-peak ratio used to decide
   whether the pair is resolvable.
"""

import numpy as np

G = 6.67430e-11
MGAL = 1.0e-5


def cmp_fold(n_channels: int, dx: float, shot_interval: float, bin_size: float,
             n_shots: int):
    """Build a split-spread geometry and return (fold per bin, offset per trace).

    Source is at the centre of each spread; receivers sit at
    +-(dx/2), +-(3dx/2), ... from the source.  CMP = (source + receiver)/2.
    """
    offsets = dx / 2.0 + dx * np.arange(n_channels // 2)
    offsets = np.concatenate([-offsets[::-1], offsets])
    midpoints = np.array([])
    half_offsets = np.array([])
    for shot in range(n_shots):
        s = shot * shot_interval
        m = (s + s + offsets) / 2.0
        midpoints = np.concatenate([midpoints, m])
        half_offsets = np.concatenate([half_offsets, np.abs(offsets)])
    lo, hi = midpoints.min(), midpoints.max()
    edges = np.arange(lo, hi + bin_size, bin_size)
    counts, _ = np.histogram(midpoints, bins=edges)
    # Only interior bins are fully populated; report the modal (full) fold.
    interior = counts[1:-1] if counts.size > 2 else counts
    return int(np.max(interior)), half_offsets, interior


def sphere_gz(x, mass, depth):
    return G * mass * depth / (x ** 2 + depth ** 2) ** 1.5 / MGAL


def main() -> None:
    # --- 1. Measured fold ----------------------------------------------------
    dx = 20.0            # m, receiver spacing            (SYNTHETIC)
    shot_interval = 20.0  # m, source advances one station (SYNTHETIC)
    bin_size = 10.0      # m, CMP bin = dx/2              (SYNTHETIC)
    print("1. Measured CMP fold (split spread, dx = %.0f m, shot step = %.0f m,"
          % (dx, shot_interval))
    print("   CMP bin = %.0f m, 400 shots)" % bin_size)
    print(f"   {'channels N':>11}{'max offset (m)':>16}{'fold (traces/bin)':>19}")
    for n_channels in (24, 48, 96, 192):
        fold, half_offsets, interior = cmp_fold(n_channels, dx, shot_interval,
                                                bin_size, 400)
        print(f"   {n_channels:>11}{half_offsets.max():>16.0f}{fold:>19.1f}")
    print("   -> fold grows linearly with the number of live channels, and so does")
    print("      the maximum offset; they are not independent knobs.")

    # --- 2. Fold along the line: the end taper ------------------------------
    n_channels = 96
    fold, half_offsets, interior = cmp_fold(n_channels, dx, shot_interval, bin_size, 400)
    ramp_bins = int(np.sum(interior < fold))
    per_end = ramp_bins / 2.0
    predicted_ramp_m = (n_channels * dx / 2.0) - shot_interval
    print("\n2. Fold along the line, measured bin by bin (N = %d, %d bins)"
          % (n_channels, interior.size))
    print(f"   bins at full fold ({fold:.0f})            = "
          f"{int(np.sum(interior == fold))} of {interior.size}"
          f" ({np.sum(interior == fold)/interior.size*100:.1f} %)")
    print(f"   bins below full fold                 = {ramp_bins}"
          f" ({per_end:.1f} per end)")
    print(f"   measured ramp length per end         = {per_end*bin_size:.0f} m of "
          f"midpoint axis")
    print(f"   predicted ramp = N dx/2 - shot step  = {predicted_ramp_m:.0f} m")
    idx = np.flatnonzero(interior < fold)[:6]
    print("   measured fold at the start of the ramp = "
          + " ".join(str(int(interior[i])) for i in idx))
    print("   -> coverage ramps from 1 trace to full fold over almost the whole")
    print("      half-spread length at each end; those bins cannot be carried at")
    print("      full fold and stack more poorly.")
    print("   NOTE: in this idealised constant-geometry split spread the OFFSET")
    print("   distribution is uniform, so fold is always N/2. Real 3-D")
    print("   templates have strongly non-uniform offset and azimuth coverage.")
    print("   measured offset range: %.0f m to %.0f m, %d distinct offsets"
          % (half_offsets.min(), half_offsets.max(), np.unique(half_offsets).size))

    # --- 3. Fresnel zone versus depth ---------------------------------------
    lam = 100.0   # m, dominant wavelength from a SYNTHETIC 2500 m/s, 25 Hz event
    print("\n3. Fresnel-zone radius sqrt(lambda h / 2), lambda = %.0f m" % lam)
    print(f"   {'depth (m)':>11}{'radius (m)':>13}{'diameter (m)':>14}")
    for h in (200.0, 500.0, 1000.0, 2000.0):
        r = np.sqrt(lam * h / 2.0)
        print(f"   {h:>11.0f}{r:>13.1f}{2 * r:>14.1f}")
    print("   -> the horizontal resolution of a seismic image degrades as the")
    print("      square root of depth, at fixed wavelength.")

    # --- 4. Two-body separation limit for gravity ---------------------------
    print("\n4. Measured two-body separation limit (equal point masses, depth h)")
    depth = 300.0
    mass = 1.0e10                      # kg, SYNTHETIC
    x = np.linspace(-3000.0, 3000.0, 120001)
    print(f"   depth h = {depth:.0f} m, each body {mass:.1e} kg")
    print(f"   {'separation (m)':>16}{'s/h':>7}{'peak (mGal)':>13}"
          f"{'midpoint/peak':>15}{'resolvable':>12}")
    for s in (0.25 * depth, 0.5 * depth, 1.0 * depth, 2.0 * depth, 3.0 * depth):
        g = sphere_gz(x - s / 2, mass, depth) + sphere_gz(x + s / 2, mass, depth)
        saddle = float(g[np.argmin(np.abs(x))] / g.max())
        single = sphere_gz(x, 2 * mass, depth)
        rms2 = float(np.sqrt(np.mean((g - single) ** 2)))
        print(f"   {s:>16.0f}{s/depth:>7.2f}{g.max():>13.4f}"
              f"{saddle:>15.3f}{('yes' if saddle < 0.999 else 'NO'):>12}"
              f"  (rms misfit to a single body {rms2:.4f} mGal)")
    # Measure the critical separation: where the midpoint stops being a maximum.
    # Analytic condition: the curvature of the summed profile at x = 0 vanishes
    # when the separation equals the depth, so s_crit = h.
    seps = np.linspace(0.90 * depth, 1.10 * depth, 4001)
    crit = None
    for s in seps:
        g = sphere_gz(x - s / 2, mass, depth) + sphere_gz(x + s / 2, mass, depth)
        if float(g[np.argmin(np.abs(x))] / g.max()) < 0.99999:
            crit = s
            break
    print(f"   measured critical separation s_crit  = {crit:.2f} m "
          f"=> s_crit/h = {crit/depth:.4f}")
    print(f"   analytic s_crit = h                  = {depth:.2f} m => 1.0000")
    print("   -> the two bodies merge into one anomaly when their separation")
    print("      falls below about ONE body depth. No processing recovers a pair")
    print("      that the physics has already merged into a single field.")


if __name__ == "__main__":
    main()
