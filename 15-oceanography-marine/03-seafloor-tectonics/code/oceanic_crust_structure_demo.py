#!/usr/bin/env python3
"""Oceanic crust structure: head-wave travel times through an ophiolite-like
layer cake, slope-intercept inversion, the velocity-depth trade-off, and the
serpentinisation ambiguity at the Moho.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python oceanic_crust_structure_demo.py

Everything here is SYNTHETIC.  The velocity model is a chosen teaching model
built from the classic ophiolite layer sequence; it is not a measured velocity
structure, and no site, ridge or survey is referenced.  The peridotite and
serpentinite end-members are model constants of the mixing calculation in
section 5.

Geometry: source and receivers on the seafloor (an ocean-bottom refraction
geometry), so the water layer does not enter the travel-time equations.  A real
surface-source survey must add the water-path delay; the lesson states what that
correction costs.

Contents
--------
1. Forward travel times: the direct wave and three head waves, with crossovers.
2. Slope-intercept inversion of the noise-free picks (verification).
3. Monte-Carlo depth uncertainty from a 10 ms picking error.
4. The velocity-depth trade-off for layer 2A, with and without near offsets.
5. Serpentinisation of the mantle: bounds on vp, rho and Poisson ratio.
6. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching model: name, top (km), base (km), vp (km/s) ----------
LAYERS = [
    ("layer 2A pillow basalts", 0.00, 0.45, 3.00),
    ("layer 2B sheeted dykes", 0.45, 1.55, 5.20),
    ("layer 3 gabbro", 1.55, 5.55, 6.80),
]
MANTLE_VP = 8.10                   # km/s, half-space below the Moho
RHO_PERIC, VP_PERIC = 3.30, 8.10   # g/cm^3, km/s   model end-member
RHO_SERP, VP_SERP = 2.55, 5.10     # g/cm^3, km/s   model end-member
VS_PERIC, VS_SERP = 4.50, 2.60     # km/s            model end-member

# offsets (km) of the four picked first-arrival branches
BRANCH_X = [
    np.arange(1.0, 1.65, 0.2),
    np.arange(3.0, 21.0, 2.0),
    np.arange(22.0, 61.0, 4.0),
    np.arange(48.0, 121.0, 8.0),
]
LABELS = ["direct (2A)", "top of 2B", "top of layer 3", "mantle"]


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def model_arrays(layers=LAYERS, v_mantle=MANTLE_VP):
    """Layer thicknesses (km) and velocities (km/s), half-space last."""
    h = np.array([base - top for _, top, base, _ in layers], dtype=float)
    v = np.array([vp for _, _, _, vp in layers] + [v_mantle], dtype=float)
    return h, v


def intercept_through(h, v, k, upto):
    """Sum of 2 h_i cos(theta_i)/v_i for i < upto, theta_i from Snell to layer k."""
    total = 0.0
    for i in range(upto):
        sin_t = v[i] / v[k]
        if sin_t >= 1.0:
            raise ValueError("velocity inversion: layer i is faster than layer k")
        total += 2.0 * h[i] * np.sqrt(1.0 - sin_t ** 2) / v[i]
    return total


def intercept_time(h, v, k):
    """Intercept time (s) of the head wave along the top of layer k (1-based)."""
    return intercept_through(h, v, k, k)


def head_time(x, h, v, k):
    """Head-wave travel time (s) at offset x (km) for the refractor at layer k."""
    return x / v[k] + intercept_time(h, v, k)


def invert(h_true, v_true, sigma_t=0.0, rng=None):
    """Slope-intercept inversion of the picked branches.

    The direct branch fixes v[0].  Branch k fixes v[k] from its slope and the
    thickness of layer k-1 from its intercept, using the thicknesses and
    velocities already recovered -- so an error in a shallow layer propagates
    downward.
    """
    xs_d = BRANCH_X[0]
    ts_d = xs_d / v_true[0]
    if sigma_t:
        ts_d = ts_d + rng.normal(0.0, sigma_t, xs_d.size)
    v_rec = np.zeros_like(v_true)
    h_rec = h_true.copy()
    v_rec[0] = 1.0 / np.polyfit(xs_d, ts_d, 1)[0]
    for k in range(1, v_true.size):
        xs = BRANCH_X[k]
        ts = head_time(xs, h_true, v_true, k)
        if sigma_t:
            ts = ts + rng.normal(0.0, sigma_t, xs.size)
        slope, intercept = np.polyfit(xs, ts, 1)
        v_rec[k] = 1.0 / slope
        if k - 1 < h_true.size:
            over = intercept_through(h_rec, v_rec, k, k - 1)
            cos_t = np.sqrt(1.0 - (v_rec[k - 1] / v_rec[k]) ** 2)
            h_rec[k - 1] = (intercept - over) * v_rec[k - 1] / (2.0 * cos_t)
    return v_rec, h_rec


def voigt_reuss(f_a, a_a, a_b):
    """Voigt, Reuss and geometric-mean mixture values for fraction f_a of a_a."""
    f = np.asarray(f_a, dtype=float)
    voigt = f * a_a + (1.0 - f) * a_b
    reuss = 1.0 / (f / a_a + (1.0 - f) / a_b)
    return voigt, reuss, np.sqrt(voigt * reuss)


def main():
    h, v = model_arrays()
    names = [n for n, _, _, _ in LAYERS]

    section("1. The layered model and its forward travel times")
    print("  top (km)  base (km)  thickness (km)  vp (km/s)   unit")
    for name, top, base, vp in LAYERS:
        print(f"  {top:8.2f}  {base:9.2f}  {base - top:14.2f}  {vp:9.2f}   {name}")
    print(f"  Moho at {LAYERS[-1][2]:.2f} km below the seafloor; half-space vp = "
          f"{MANTLE_VP:.2f} km/s")
    print("\n  branch              refractor vp   intercept (s)   offset range (km)")
    for k in range(1, v.size):
        xs = BRANCH_X[k]
        print(f"  {LABELS[k]:18s} {v[k]:11.2f}   {intercept_time(h, v, k):13.4f}   "
              f"{xs[0]:.1f}-{xs[-1]:.1f}")
    print("\n  branch            first t (s)   last t (s)   fitted v_app (km/s)")
    for k in range(1, v.size):
        xs = BRANCH_X[k]
        ts = head_time(xs, h, v, k)
        slope = np.polyfit(xs, ts, 1)[0]
        print(f"  {LABELS[k]:18s} {ts[0]:9.4f}   {ts[-1]:10.4f}   "
              f"{1.0 / slope:8.4f} (model {v[k]:.2f})")
    print("\n  crossover distances (the offset beyond which a branch is a first")
    print("  arrival), from  t_a = t_b at two-layer intercepts:")
    for k in range(2, v.size):
        x_c = (intercept_time(h, v, k) - intercept_time(h, v, k - 1)) / \
            (1.0 / v[k - 1] - 1.0 / v[k])
        print(f"    {LABELS[k - 1]} -> {LABELS[k]}: x_c = {x_c:.3f} km")
    x_c1 = intercept_time(h, v, 1) / (1.0 / v[0] - 1.0 / v[1])
    print(f"    direct -> {LABELS[1]}: x_c = {x_c1:.3f} km")
    print("  the picked offset ranges all lie beyond their crossover, so every")
    print("  branch is a genuine first arrival in this design.")

    section("2. Slope-intercept inversion of the noise-free picks (verification)")
    v_rec, h_rec = invert(h, v, sigma_t=0.0)
    print("  unit            true v   rec v    true h   rec h      error")
    for i, name in enumerate(names):
        print(f"  {name:24s} {v[i]:6.2f}   {v_rec[i]:6.4f}   {h[i]:7.2f}   "
              f"{h_rec[i]:7.4f}   {h_rec[i] - h[i]:+9.6f}")
    print(f"  {'mantle':24s} {v[3]:6.2f}   {v_rec[3]:6.4f}")
    print(f"  Moho depth: true {h.sum():.2f} km, recovered {h_rec.sum():.4f} km")
    print("  the noise-free inversion reproduces the model exactly in v, because a")
    print("  head-wave branch is linear in offset; the thickness residuals are at")
    print("  the 1e-5 km level, i.e. round-off.")

    section("3. Monte-Carlo depth uncertainty from a 10 ms picking error")
    sigma_t, n_real = 0.010, 200
    rec = np.zeros((n_real, h.size))
    for j in range(n_real):
        _, h_j = invert(h, v, sigma_t=sigma_t, rng=RNG)
        rec[j, :] = h_j
    print(f"  {n_real} realisations, Gaussian pick error sigma = "
          f"{sigma_t * 1e3:.0f} ms")
    print("  unit            true h (km)   mean h (km)   std (km)   std/true")
    for i, name in enumerate(names):
        m, s = rec[:, i].mean(), rec[:, i].std(ddof=1)
        print(f"  {name:24s} {h[i]:10.2f}   {m:10.3f}   {s:7.3f}   {s / h[i]:8.3f}")
    tot = rec.sum(axis=1)
    print(f"  {'Moho (sum of three)':24s} {h.sum():10.2f}   {tot.mean():10.3f}   "
          f"{tot.std(ddof=1):7.3f}   {tot.std(ddof=1) / h.sum():8.3f}")
    print("  the thin top layer is the least resolvable, and the Moho total is")
    print("  better determined than any single layer.")

    section("4. The velocity-depth trade-off for layer 2A")
    sigma_t4 = 0.010
    rng4 = np.random.default_rng(7)
    ts_2b = head_time(BRANCH_X[1], h, v, 1) + rng4.normal(0.0, sigma_t4,
                                                         BRANCH_X[1].size)
    ts_d = BRANCH_X[0] / v[0] + rng4.normal(0.0, sigma_t4, BRANCH_X[0].size)
    grid_v = np.arange(2.50, 3.65, 0.05)
    grid_h = np.arange(0.20, 0.90, 0.05)

    def chi2(vv, hh, use_direct):
        h_t = h.copy()
        h_t[0] = hh
        v_t = v.copy()
        v_t[0] = vv
        r = (ts_2b - head_time(BRANCH_X[1], h_t, v_t, 1)) / sigma_t4
        if use_direct:
            r = np.concatenate([r, (ts_d - BRANCH_X[0] / vv) / sigma_t4])
        return float(r @ r)

    for use_direct in (False, True):
        chi = np.array([[chi2(vv, hh, use_direct) for hh in grid_h]
                        for vv in grid_v])
        i_min = np.unravel_index(np.argmin(chi), chi.shape)
        c_min = chi[i_min]
        sel = chi <= c_min + 1.0        # 1-sigma region in chi^2
        which = "with" if use_direct else "without"
        print(f"\n  {which} the near-offset direct branch "
              f"({BRANCH_X[0].size} picks over {BRANCH_X[0][-1] - BRANCH_X[0][0]:.1f} km):")
        print(f"    best fit v = {grid_v[i_min[0]]:.2f} km/s, h = "
              f"{grid_h[i_min[1]]:.2f} km (true {v[0]:.2f} / {h[0]:.2f}), "
              f"chi^2 = {c_min:.2f} for {BRANCH_X[1].size + (BRANCH_X[0].size if use_direct else 0)} picks")
        print(f"    admitted pairs within dchi^2 = 1: {sel.sum()} of {chi.size}")
        vs = sorted(set(round(float(grid_v[a]), 2) for a in np.where(sel)[0]))
        hs = sorted(set(round(float(grid_h[b]), 2) for b in np.where(sel)[1]))
        print("      v: " + ", ".join(f"{x:.2f}" for x in vs))
        print("      h: " + ", ".join(f"{x:.2f}" for x in hs))
        for vv in (2.70, 3.00, 3.30):
            a = int(np.argmin(np.abs(grid_v - vv)))
            b = int(np.argmin(chi[a]))
            print(f"      at v = {grid_v[a]:.2f} km/s the best h is "
                  f"{grid_h[b]:.2f} km (chi^2 {chi[a, b]:.2f})")
    print("\n  head waves alone leave a band of acceptable (v, h) pairs along which")
    print("  the velocity trades against the thickness; the near-offset direct")
    print("  arrival narrows the band.  This is why a refraction survey needs")
    print("  short offsets as well as long ones.")

    section("5. Serpentinisation of the mantle: vp, rho and Poisson ratio")
    frac = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    vp_v, vp_r, vp_g = voigt_reuss(1.0 - frac, VP_PERIC, VP_SERP)
    rho_v, rho_r, _ = voigt_reuss(1.0 - frac, RHO_PERIC, RHO_SERP)
    print("  serpentine fraction   vp Voigt   vp Reuss   vp geom   rho Voigt   rho Reuss")
    for i, f in enumerate(frac):
        print(f"  {f:19.1f}   {vp_v[i]:9.2f}   {vp_r[i]:9.2f}   {vp_g[i]:8.2f}   "
              f"{rho_v[i]:10.3f}   {rho_r[i]:10.3f}")
    target = 7.50
    f_needed = float(np.interp(target, vp_r[::-1], frac[::-1]))
    print(f"\n  Reuss-average vp falls to {target:.2f} km/s, a velocity a refraction")
    print(f"  survey would call lower crust, at {f_needed:.2f} serpentine fraction.")
    for name, vpv, vsv in (("peridotite", VP_PERIC, VS_PERIC),
                           ("serpentinite", VP_SERP, VS_SERP)):
        nu = (vpv ** 2 - 2 * vsv ** 2) / (2 * (vpv ** 2 - vsv ** 2))
        print(f"    {name:13s} vp = {vpv:.2f} km/s, vs = {vsv:.2f} km/s, "
              f"Poisson = {nu:.3f}")
    print("  the Moho is a velocity step, not a rock-type boundary: hydrated")
    print("  mantle can sit above a crust-like velocity, so vp alone cannot place")
    print("  the petrological Moho.  Vs (from the same OBS data) or a density")
    print("  from gravity is the independent constraint.")

    section("6. Worked examples used in the lesson")
    print(f"(a) intercept time of the 2B refractor: sin(theta) = v(2A)/v(2B) = "
          f"{v[0] / v[1]:.4f}, cos = {np.sqrt(1 - (v[0] / v[1]) ** 2):.4f}")
    print(f"    t_int = 2 x {h[0]:.2f} km x {np.sqrt(1 - (v[0] / v[1]) ** 2):.4f} "
          f"/ {v[0]:.2f} km/s = {intercept_time(h, v, 1):.4f} s")
    print(f"(b) travel time at x = 20 km on that branch: "
          f"{head_time(20.0, h, v, 1):.4f} s; at x = 3 km: "
          f"{head_time(3.0, h, v, 1):.4f} s")
    print(f"(c) Moho refractor intercept = {intercept_time(h, v, 3):.4f} s; "
          f"t(100 km) = {head_time(100.0, h, v, 3):.4f} s")
    print(f"(d) Moho depth below the seafloor = {h.sum():.2f} km; recovered from")
    print(f"    the noise-free inversion as {h_rec.sum():.4f} km")
    print(f"(e) serpentinite fraction for Reuss vp = {target:.2f} km/s: "
          f"{f_needed:.2f}")
    print(f"(f) Monte-Carlo Moho depth: {tot.mean():.3f} +/- "
          f"{tot.std(ddof=1):.3f} km (1 sigma)")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
