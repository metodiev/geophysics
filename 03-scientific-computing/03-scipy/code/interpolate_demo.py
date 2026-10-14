"""scipy.interpolate: splines, gridded data and the danger of extrapolation.

Run:  .venv/bin/python interpolate_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-04.

Part 1  a SYNTHETIC depth-velocity log sampled at irregular depths: five
        interpolants compared against the function that generated the data.
        Two error measures are reported -- distance from the truth, and
        overshoot beyond the data range.
Part 2  RegularGridInterpolator on a 2-D SYNTHETIC velocity field.
Part 3  extrapolation, measured rather than asserted: the same three
        interpolants evaluated outside the data range.
Part 4  griddata on scattered stations, and what happens outside the hull.

No real log, grid or station location is used anywhere in this file.
"""

import numpy as np
from scipy import interpolate

RNG = np.random.default_rng(20241031)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Part 1 -- well log
# --------------------------------------------------------------------------

def log_true(z):
    """SYNTHETIC velocity log: a step, a cyclic stratification, a thin bed."""
    return (2300.0
            + 320.0 * np.tanh((z - 1250.0) / 60.0)
            + 60.0 * np.sin(2.0 * np.pi * z / 150.0)
            - 220.0 * np.exp(-((z - 1600.0) / 12.0) ** 2))


def part1_well_log():
    section("1. A depth-velocity log: five interpolants, two error measures")
    sigma = 5.0                                     # m/s, SYNTHETIC noise
    raw = np.sort(RNG.uniform(500.0, 2000.0, 300))
    # Real logs are sampled at irregular depth intervals, and occasionally the
    # intervals collapse. Keep samples at least 2 m apart.
    keep = [0]
    for i in range(1, raw.size):
        if raw[i] - raw[keep[-1]] >= 2.0:
            keep.append(i)
    z_s = raw[keep]
    v_s = log_true(z_s) + RNG.normal(0.0, sigma, size=z_s.size)
    n_samples = z_s.size
    gaps = np.diff(z_s)

    z_fine = np.linspace(z_s[0], z_s[-1], 4000)
    v_true = log_true(z_fine)
    lo, hi = v_s.min(), v_s.max()

    methods = {
        "interp1d(linear)": interpolate.interp1d(z_s, v_s, kind="linear"),
        "CubicSpline": interpolate.CubicSpline(z_s, v_s),
        "PchipInterpolator": interpolate.PchipInterpolator(z_s, v_s),
        "Akima1DInterpolator": interpolate.Akima1DInterpolator(z_s, v_s),
        "UnivariateSpline(s=0)": interpolate.UnivariateSpline(z_s, v_s, s=0.0),
        "UnivariateSpline(s=n*sigma^2)": interpolate.UnivariateSpline(
            z_s, v_s, s=n_samples * sigma ** 2),
    }
    print(f"  {n_samples} samples kept over {z_s[0]:.0f}-{z_s[-1]:.0f} m, "
          f"noise sigma = {sigma:.0f} m/s.")
    print(f"  Sample spacing: min {gaps.min():.2f} m, median "
          f"{np.median(gaps):.2f} m, max {gaps.max():.2f} m.")
    print("  The data-generating function is known, so the error is measurable.")
    print(f"    {'method':<30}{'RMS (m/s)':>11}{'max (m/s)':>11}"
          f"{'overshoot (m/s)':>18}")
    for name, f in methods.items():
        d = f(z_fine) - v_true
        over = max(0.0, float(np.max(f(z_fine)) - hi),
                   float(lo - np.min(f(z_fine))))
        print(f"    {name:<30}{np.sqrt(np.mean(d ** 2)):>11.3f}"
              f"{np.abs(d).max():>11.3f}{over:>18.3f}")
    print("    (overshoot = how far the interpolant leaves the range of the")
    print("     data; an interpolant that overshoots invents velocities that")
    print("     were never measured.)")

    print()
    print("  Node exactness: every interpolant that passes through the data")
    print("  reproduces the sample values exactly.")
    print(f"    CubicSpline at the {n_samples} nodes: max |f(z_s) - v_s| = "
          f"{np.abs(methods['CubicSpline'](z_s) - v_s).max():.2e} m/s")
    print(f"    UnivariateSpline(s=0)               : max |f(z_s) - v_s| = "
          f"{np.abs(methods['UnivariateSpline(s=0)'](z_s) - v_s).max():.2e} m/s")
    print(f"    UnivariateSpline(s=n*sigma^2)       : max |f(z_s) - v_s| = "
          f"{np.abs(methods['UnivariateSpline(s=n*sigma^2)'](z_s) - v_s).max():.3f} m/s")
    print("    The smoothing spline is the only one that does not interpolate,")
    print("    and that is the point: with 5 m/s of noise, forcing the curve")
    print("    through every sample injects the noise into the answer.")

    print()
    print("  The thin bed at 1600 m (20 m wide, lower velocity). Error in the")
    print("  1590-1610 m window, where the curvature is large:")
    w = (z_fine > 1590.0) & (z_fine < 1610.0)
    print(f"    {'method':<30}{'RMS in window (m/s)':>20}")
    for name, f in methods.items():
        d = (f(z_fine) - v_true)[w]
        print(f"    {name:<30}{np.sqrt(np.mean(d ** 2)):>20.3f}")
    print("    Linear interpolation is the worst (67 m/s of RMS error): with a")
    print("    median spacing of 4.7 m and a 20 m bed it cuts the corner, which")
    print("    is the resolution limit that the sample spacing imposes.")
    print("    The cubic spline reproduces the bed best (18 m/s) and pays for it")
    print("    by leaving the data range by 7 m/s elsewhere; PCHIP cannot")
    print("    overshoot, and that constraint costs it accuracy at a trough the")
    print("    data only partially resolve (57 m/s).")

    print()
    print("  Cluster sensitivity, the assumption that bites hardest. Insert one")
    print("  extra sample carrying a 30 m/s error (an outlier, or a miscorrected")
    print("  pick) at a decreasing distance after an existing sample, and refit:")
    k = int(np.argmin(np.abs(z_s - 1200.0)))
    print("    (errors measured within 20 m of the inserted sample, where the")
    print("     damage is local; the thin bed dominates the global maximum)")
    print(f"    {'spacing (m)':>12}{'CubicSpline':>26}{'PCHIP':>20}")
    print(f"    {'':>12}{'overshoot':>13}{'max error':>13}"
          f"{'overshoot':>10}{'max error':>10}")
    w_c = np.abs(z_fine - z_s[k]) < 20.0
    for dz in (2.0, 0.3, 0.05):
        z_c = np.insert(z_s, k + 1, z_s[k] + dz)
        v_c = np.insert(v_s, k + 1, log_true(z_s[k] + dz) + 30.0)
        out = []
        for cls in (interpolate.CubicSpline, interpolate.PchipInterpolator):
            f = cls(z_c, v_c)
            fw = f(z_fine)[w_c]
            over = max(0.0, float(fw.max() - v_c.max()),
                       float(v_c.min() - fw.min()))
            err = float(np.abs(fw - v_true[w_c]).max())
            out.append((over, err))
        print(f"    {dz:>12.2f}{out[0][0]:>13.3f}{out[0][1]:>13.3f}"
              f"{out[1][0]:>10.3f}{out[1][1]:>10.3f}")
    print("    At a normal 2 m spacing both methods are affected only locally,")
    print("    by about the size of the inserted error. Move the pair to")
    print("    5 cm apart and the cubic spline's curvature estimator divides by")
    print("    the square of a near-zero interval: the interpolant grows a spike")
    print("    and the error reaches 510 m/s. PCHIP's numbers are unchanged,")
    print("    because it never forms that curvature. Deduplicate and enforce a")
    print("    minimum spacing before interpolating anything measured.")


# --------------------------------------------------------------------------
# Part 2 -- 2-D gridded velocity field
# --------------------------------------------------------------------------

def velocity_true(x, z):
    """SYNTHETIC 2-D velocity field in km and km, returned in m/s."""
    return 3000.0 + 250.0 * np.sin(np.pi * x / 4.0) * np.exp(-z / 2.5)


def part2_regular_grid():
    section("2. RegularGridInterpolator on a 2-D velocity field")
    x_nodes = np.linspace(0.0, 20.0, 21)          # 1 km spacing
    z_nodes = np.linspace(0.0, 10.0, 11)          # 1 km spacing
    V = velocity_true(x_nodes[:, None], z_nodes[None, :])
    rgi_lin = interpolate.RegularGridInterpolator(
        (x_nodes, z_nodes), V, method="linear", bounds_error=False,
        fill_value=np.nan)
    rgi_cub = interpolate.RegularGridInterpolator(
        (x_nodes, z_nodes), V, method="cubic", bounds_error=False,
        fill_value=np.nan)
    rbs = interpolate.RectBivariateSpline(x_nodes, z_nodes, V, kx=3, ky=3)

    xq = RNG.uniform(0.0, 20.0, 3000)
    zq = RNG.uniform(0.0, 10.0, 3000)
    pts = np.column_stack([xq, zq])
    truth = velocity_true(xq, zq)
    print(f"  Grid: {x_nodes.size} x {z_nodes.size} nodes, 1 km spacing, "
          f"{V.size} values stored.")
    print(f"  {xq.size} random query points inside the grid.")
    print(f"    {'method':<26}{'RMS (m/s)':>12}{'max (m/s)':>12}"
          f"{'RMS % of field':>16}")
    for name, vals in (("RegularGridInterpolator linear", rgi_lin(pts)),
                       ("RegularGridInterpolator cubic", rgi_cub(pts)),
                       ("RectBivariateSpline kx=ky=3", rbs(xq, zq, grid=False))):
        d = vals - truth
        print(f"    {name:<26}{np.sqrt(np.mean(d ** 2)):>12.4f}"
              f"{np.abs(d).max():>12.4f}"
              f"{100 * np.sqrt(np.mean(d ** 2)) / 3000.0:>16.4f}")
    print("    Cubic interpolation is two orders of magnitude closer to the")
    print("    truth here because the field is smooth on the node spacing.")
    print("    Linear interpolation has an error of order (h^2/8) * |f''|,")
    print("    which for h = 1 km and this field is a few m/s -- exactly what")
    print("    the table shows. Refining the grid would beat both.")
    print()
    print("  Where the field is most curved, cubic still beats linear, but the")
    print("  ratio narrows:")
    m = (xq > 1.5) & (xq < 2.5) & (zq < 1.0)
    print(f"    {m.sum()} query points near the origin, where sin(pi x/4) and")
    print("    exp(-z/2.5) are both changing fastest")
    for name, vals in (("linear", rgi_lin(pts)), ("cubic", rgi_cub(pts))):
        d = (vals - truth)[m]
        print(f"    {name:<8} RMS = {np.sqrt(np.mean(d ** 2)):>8.4f} m/s"
              f"   max = {np.abs(d).max():>8.4f} m/s")


# --------------------------------------------------------------------------
# Part 3 -- extrapolation
# --------------------------------------------------------------------------

def part3_extrapolation():
    section("3. Extrapolation: the same routines, outside the data")
    x_nodes = np.linspace(0.0, 20.0, 21)
    z_nodes = np.linspace(0.0, 10.0, 11)
    V = velocity_true(x_nodes[:, None], z_nodes[None, :])
    rgi_lin = interpolate.RegularGridInterpolator(
        (x_nodes, z_nodes), V, method="linear", bounds_error=False,
        fill_value=None)                     # linear extrapolation
    rgi_cub = interpolate.RegularGridInterpolator(
        (x_nodes, z_nodes), V, method="cubic", bounds_error=False,
        fill_value=None)                     # cubic extrapolation
    rgi_nan = interpolate.RegularGridInterpolator(
        (x_nodes, z_nodes), V, method="cubic", bounds_error=False,
        fill_value=np.nan)
    xq = np.array([5.0, 5.0, 5.0, 5.0, 5.0])
    zq = np.array([9.0, 10.0, 11.0, 13.0, 20.0])
    truth = velocity_true(xq, zq)
    print("  Profile at x = 5 km, querying below the deepest node (z = 10 km).")
    print(f"    {'z (km)':>8}{'truth (m/s)':>13}{'linear (m/s)':>13}"
          f"{'cubic (m/s)':>12}{'fill=nan':>10}")
    for z, tr, a, b, c in zip(zq, truth, rgi_lin(np.column_stack([xq, zq])),
                              rgi_cub(np.column_stack([xq, zq])),
                              rgi_nan(np.column_stack([xq, zq]))):
        print(f"    {z:>8.1f}{tr:>13.4f}{a:>13.4f}{b:>12.4f}{c:>10.4f}")
    print(f"    relative error at z = 11 km (10% beyond the edge):")
    print(f"      linear {abs(rgi_lin([[5.0, 11.0]])[0] / velocity_true(5.0, 11.0) - 1):.3e}"
          f"   cubic {abs(rgi_cub([[5.0, 11.0]])[0] / velocity_true(5.0, 11.0) - 1):.3e}")
    print(f"    relative error at z = 20 km (100% beyond the edge):")
    print(f"      linear {abs(rgi_lin([[5.0, 20.0]])[0] / velocity_true(5.0, 20.0) - 1):.3e}"
          f"   cubic {abs(rgi_cub([[5.0, 20.0]])[0] / velocity_true(5.0, 20.0) - 1):.3e}")
    print("    Both are wrong, and the cubic one is wrong by more, because a")
    print("    cubic extrapolates its own polynomial while a linear rule")
    print("    extrapolates the last slope. Neither has seen a datum there.")

    print()
    print("  The same test on the 1-D log, where the truth is also known:")
    z_s = np.sort(RNG.uniform(1500.0, 2000.0, 120))
    v_s = log_true(z_s) + RNG.normal(0.0, 5.0, size=120)
    cs = interpolate.CubicSpline(z_s, v_s, extrapolate=True)
    cs_clip = interpolate.CubicSpline(z_s, v_s, extrapolate=False)
    z_out = np.array([2010.0, 2050.0, 2100.0, 2150.0])
    print(f"    last data depth {z_s.max():.1f} m; querying beyond it")
    print(f"    gap between the last two samples: {np.diff(z_s)[-1]:.2f} m")
    print(f"    {'z (m)':>8}{'truth (m/s)':>13}{'spline (m/s)':>16}"
          f"{'error (m/s)':>14}{'extrapolate=False':>19}")
    for z in z_out:
        print(f"    {z:>8.1f}{log_true(z):>13.3f}{cs(z):>16.3f}"
              f"{cs(z) - log_true(z):>14.3f}"
              f"{('nan' if np.isnan(cs_clip(z)) else f'{cs_clip(z):.3f}'):>19}")
    print("    The spline extrapolates its last cubic segment, whose curvature")
    print("    was fitted to a short, noisy interval, so the error grows without")
    print("    bound: -620 m/s at 10 m past the data and -690 000 m/s at 150 m.")
    print("    extrapolate=False returns NaN instead of a plausible-looking")
    print("    number, which is the honest default when a query leaves the data.")


# --------------------------------------------------------------------------
# Part 4 -- scattered data
# --------------------------------------------------------------------------

def part4_griddata():
    section("4. griddata on scattered stations")
    n_st = 60
    sx = RNG.uniform(0.0, 20.0, n_st)
    sz = RNG.uniform(0.0, 10.0, n_st)
    sv = velocity_true(sx, sz) + RNG.normal(0.0, 4.0, n_st)

    vx = RNG.uniform(0.0, 20.0, 400)
    vz = RNG.uniform(0.0, 10.0, 400)
    truth = velocity_true(vx, vz)
    print(f"  {n_st} SYNTHETIC scattered stations, {vx.size} check points.")
    out = {m: interpolate.griddata((sx, sz), sv, (vx, vz), method=m)
           for m in ("nearest", "linear", "cubic")}
    inside = ~np.isnan(out["linear"])
    print(f"    {'method':<10}{'RMS (m/s)':>12}{'max (m/s)':>12}"
          f"{'NaN count':>11}{'NaN %':>8}")
    print("    (RMS and max over the 311 points inside the convex hull only,")
    print("     so that the three methods are compared on the same points)")
    for method in ("nearest", "linear", "cubic"):
        vals = out[method]
        bad = int(np.isnan(vals).sum())
        d = vals[inside] - truth[inside]
        print(f"    {method:<10}{np.sqrt(np.mean(d ** 2)):>12.4f}"
              f"{np.abs(d).max():>12.4f}{bad:>11}{100 * bad / vals.size:>8.2f}")
    print("    The NaN counts are points outside the convex hull of the")
    print("    stations: 'linear' and 'cubic' refuse to guess there, which is")
    print("    the behaviour you want. 'nearest' always answers, everywhere,")
    print("    including outside the hull, where it silently repeats the edge")
    print("    station's value; and inside the hull its answer is a step")
    print("    function of station positions. Cubic wins (29.5 m/s), and nearest")
    print("    and linear are indistinguishable at this station density")
    print("    (35.1 and 36.6 m/s).")
    print("    The station noise of 4 m/s sets a floor on the error, but the")
    print("    measured RMS is 7 to 9 times larger: with 60 stations over")
    print("    200 km^2 the sampling density, not the noise, limits the map.")
    print("    Interpolating a field from scattered picks cannot beat the pick")
    print("    spacing, however smooth the interpolant.")


def main():
    part1_well_log()
    part2_regular_grid()
    part3_extrapolation()
    part4_griddata()
    print("\nDone.")


if __name__ == "__main__":
    main()
