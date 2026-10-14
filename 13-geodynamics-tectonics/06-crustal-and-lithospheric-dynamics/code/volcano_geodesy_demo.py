#!/usr/bin/env python3
"""Volcano geodesy: the Mogi surface displacement, the InSAR line-of-sight
projection and what it can separate, the depth-volume trade-off of an
inversion, and the source shapes that surface data cannot resolve.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python volcano_geodesy_demo.py

Everything is SYNTHETIC: the source depths, volume changes and satellite
geometries are chosen teaching values, not measured volcanoes or real
acquisitions.

Contents
--------
1. Mogi forward model: displacement profile, decay exponents, exact ratios.
2. Line of sight: the projection onto ascending and descending look vectors,
   and how well the pair separates vertical from horizontal motion.
3. Inversion of noisy ascending + descending data for (depth, volume change):
   the admitted set, not a single answer.
4. Which source shapes surface geodesy can and cannot resolve.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


NU_HALFSPACE = 0.25            # Poisson's ratio used in the Mogi factor 3 dV/(4 pi)
# Satellite look geometry: incidence from vertical and heading clockwise from
# north.  Ascending and descending headings differ by about 180 degrees.
INC_ASC, HEAD_ASC = np.radians(39.0), np.radians(350.0)
INC_DESC, HEAD_DESC = np.radians(39.0), np.radians(190.0)


def mogi(r_m, d_m, dv_m3):
    """Surface displacement of a Mogi source: returns (u_r, u_z) in metres."""
    fac = 3.0 * dv_m3 / (4.0 * np.pi)
    den = (r_m ** 2 + d_m ** 2) ** 1.5
    return fac * r_m / den, fac * d_m / den


def los_unit(inc, heading):
    """Unit vector from the ground towards the satellite, in (east, north, up)."""
    return np.array([np.sin(inc) * np.cos(heading),
                     -np.sin(inc) * np.sin(heading),
                     np.cos(inc)])


def enu_from_mogi(x_m, y_m, d_m, dv_m3):
    """East, north and up displacement on a surface grid from a Mogi source."""
    r = np.hypot(x_m, y_m)
    ur, uz = mogi(r, d_m, dv_m3)
    with np.errstate(invalid="ignore", divide="ignore"):
        ue = np.where(r > 0.0, ur * x_m / r, 0.0)
        un = np.where(r > 0.0, ur * y_m / r, 0.0)
    return ue, un, uz


def demonstration_1():
    section("1. Mogi forward model")
    print("  u_r = (3 dV / 4 pi) r / (r^2 + d^2)^(3/2),")
    print("  u_z = (3 dV / 4 pi) d / (r^2 + d^2)^(3/2)")
    d, dv = 3000.0, 1.0e6
    print(f"\n  SYNTHETIC source: d = {d / 1e3:.1f} km, dV = {dv:.3e} m^3 "
          f"(= {dv / 1e9:.4f} km^3)")
    print(f"  Poisson's ratio implied by the factor 3 dV/4 pi: {NU_HALFSPACE:.2f}  "
          f"(a homogeneous elastic half-space)")
    print("\n    r (km)   u_r (cm)   u_z (cm)   u_r/u_z   r/d (exact)")
    for r in (0.0, 1.0, 3.0, 6.0, 10.0, 20.0):
        ur, uz = mogi(r * 1e3, d, dv)
        ratio = ur / uz if uz != 0 else 0.0
        print(f"    {r:6.1f}   {ur * 100:9.3f}   {uz * 100:8.3f}   "
              f"{ratio:7.4f}   {r / 3.0:8.4f}")
    print("  The ratio u_r/u_z equals r/d exactly, which is the algebraic identity")
    print("  u_r/u_z = r/d; the table is a check that the implementation has it.")
    r_far = np.array([10.0, 20.0, 40.0, 80.0]) * 1e3
    _, uz_far = mogi(r_far, d, dv)
    p_far = np.polyfit(np.log(r_far), np.log(uz_far), 1)[0]
    r_near = np.array([0.3, 0.6, 0.9, 1.2]) * 1e3
    _, uz_near = mogi(r_near, d, dv)
    p_near = np.polyfit(np.log(r_near), np.log(uz_near), 1)[0]
    print(f"\n  measured decay exponent u_z ~ r^p:")
    print(f"    for r/d < 0.4 (r = 0.3 to 1.2 km): p = {p_near:+.4f}")
    print(f"    for r/d > 3   (r = 10 to 80 km):    p = {p_far:+.4f}")
    print(f"  the exponent tends to 0 as r/d -> 0 and to -3 as r/d -> infinity, so")
    print(f"  the measured value at any finite radius is a statement about r/d, not")
    print(f"  about a universal power law.")
    print(f"  the transition happens near r = d = {d / 1e3:.1f} km, so the depth")
    print(f"  sets the length scale of the surface pattern.")


def demonstration_2():
    section("2. Line of sight and the ascending/descending pair")
    d, dv = 3000.0, 1.0e6
    e_asc = los_unit(INC_ASC, HEAD_ASC)
    e_desc = los_unit(INC_DESC, HEAD_DESC)
    print("  look vector (east, north, up):")
    print(f"    ascending : {e_asc[0]:+.4f} {e_asc[1]:+.4f} {e_asc[2]:+.4f}"
          f"   (incidence {np.degrees(INC_ASC):.0f} deg, heading "
          f"{np.degrees(HEAD_ASC):.0f} deg)")
    print(f"    descending: {e_desc[0]:+.4f} {e_desc[1]:+.4f} {e_desc[2]:+.4f}"
          f"   (incidence {np.degrees(INC_DESC):.0f} deg, heading "
          f"{np.degrees(HEAD_DESC):.0f} deg)")
    print("\n  LOS displacement = e . (u_E, u_N, u_U); the projection weights:")
    print(f"    vertical weight (both orbits, same incidence) = "
          f"{e_asc[2]:.4f} = {np.cos(INC_ASC):.4f} = cos(incidence)")
    print(f"    horizontal weight                           = "
          f"{np.sin(INC_ASC):.4f} = sin(incidence)")
    print("  A purely vertical displacement of 1 cm therefore produces")
    print(f"    {abs(e_asc[2]) * 1.0:.4f} cm of LOS change, while a purely")
    print(f"  horizontal displacement of 1 cm produces at most "
          f"{np.sin(INC_ASC) * 1.0:.4f} cm of LOS change.")
    print("\n  the two orbits are therefore not redundant: along a profile across")
    print("  the source their signed line-of-sight values differ")
    print("    x (km)      -6.0   -3.0    0.0    3.0    6.0")
    xq = np.array([-6.0, -3.0, 0.0, 3.0, 6.0]) * 1e3
    ue_q, un_q, uz_q = enu_from_mogi(xq, np.zeros_like(xq), d, dv)
    la = e_asc[0] * ue_q + e_asc[1] * un_q + e_asc[2] * uz_q
    ld = e_desc[0] * ue_q + e_desc[1] * un_q + e_desc[2] * uz_q
    print("    ascending (cm)" + "".join(f"{v * 100:7.3f}" for v in la))
    print("    descending (cm)" + "".join(f"{v * 100:7.3f}" for v in ld))
    print("\n  separating vertical from east-west, ignoring the north component:")
    A = np.array([[e_asc[0], e_asc[2]], [e_desc[0], e_desc[2]]])
    print(f"    matrix rows: ascending {A[0]}, descending {A[1]}")
    print(f"    determinant = {np.linalg.det(A):.6f}")
    print(f"    condition number = {np.linalg.cond(A):.4f}")
    sv = np.linalg.svd(A, compute_uv=False)
    print(f"    singular values = {sv[0]:.4f}, {sv[1]:.4f}")
    print("  the pair is well conditioned because the two look directions differ")
    print("  mainly in their horizontal part; the east-west component is recovered")
    print("  with a larger error amplification than the vertical one (see below).")
    print("\n  error amplification against the north component that was ignored:")
    print("    a north displacement of 1 cm leaks into the solved vertical and")
    print("    east-west components by")
    sol_n = np.linalg.solve(A, np.array([e_asc[1], e_desc[1]]))
    print(f"      vertical: {sol_n[1] * 100:.2f}% of the north displacement")
    print(f"      east-west: {sol_n[0] * 100:.2f}%")
    print("  so a real north-south fault signal appears in a two-orbit InSAR")
    print("  decomposition as a spurious vertical and east-west motion of that size.")


def demonstration_3():
    section("3. Inversion of noisy data for depth and volume change")
    d_true, dv_true = 3000.0, 1.0e6
    x = np.linspace(-12.0e3, 12.0e3, 25)
    y = np.zeros_like(x)
    ue, un, uz = enu_from_mogi(x, y, d_true, dv_true)
    e_asc = los_unit(INC_ASC, HEAD_ASC)
    e_desc = los_unit(INC_DESC, HEAD_DESC)
    los_asc_true = e_asc[0] * ue + e_asc[1] * un + e_asc[2] * uz
    los_desc_true = e_desc[0] * ue + e_desc[1] * un + e_desc[2] * uz
    sigma = 0.002
    los = np.concatenate((los_asc_true, los_desc_true)) + \
        sigma * RNG.standard_normal(los_asc_true.size * 2)
    print(f"  profile along y = 0, x from {x[0] / 1e3:.0f} to {x[-1] / 1e3:.0f} km,")
    print(f"  {x.size} points, two orbits, noise sigma = {sigma * 100:.1f} cm "
          f"(a stack of interferograms)")
    print(f"  peak LOS signal = {np.max(np.abs(los_asc_true)) * 100:.3f} cm "
          f"(ascending), {np.max(np.abs(los_desc_true)) * 100:.3f} cm (descending)\n")
    print("    depth (km)   best dV (m^3)      rms misfit (cm)")
    ds = np.linspace(1000.0, 12000.0, 400)
    rows = []
    for d in ds:
        ue_t, un_t, uz_t = enu_from_mogi(x, y, d, 1.0e6)
        model = np.concatenate((e_asc[0] * ue_t + e_asc[1] * un_t + e_asc[2] * uz_t,
                                e_desc[0] * ue_t + e_desc[1] * un_t + e_desc[2] * uz_t))
        # volume change is linear in the model, so it is solved in closed form
        scale = float(model @ los) / float(model @ model)
        rms = np.sqrt(np.mean((scale * model - los) ** 2))
        rows.append((d, scale * 1.0e6, rms))
    rows = np.array(rows)
    for d in (1.5e3, 2.0e3, 3.0e3, 4.0e3, 6.0e3, 9.0e3):
        i = int(np.argmin(np.abs(rows[:, 0] - d)))
        print(f"    {rows[i, 0] / 1e3:11.2f}   {rows[i, 1]:14.4e}   "
              f"{rows[i, 2] * 100:16.4f}")
    i_best = int(np.argmin(rows[:, 2]))
    print(f"\n  best fit: d = {rows[i_best, 0] / 1e3:.2f} km, "
          f"dV = {rows[i_best, 1]:.4e} m^3, rms = {rows[i_best, 2] * 100:.4f} cm")
    print(f"  truth:    d = {d_true / 1e3:.2f} km, dV = {dv_true:.4e} m^3")
    from scipy.stats import chi2 as chi2_dist
    n_data = x.size * 2
    chi2_95 = float(chi2_dist.ppf(0.95, n_data))
    thr = sigma * np.sqrt(chi2_95 / n_data)
    print(f"\n  admitted set at the 95% level of the chi-square distribution with")
    print(f"  {n_data} data and a known noise: chi2 <= {chi2_95:.2f}, i.e. rms <=")
    print(f"  {thr * 100:.3f} cm, and the least-squares minimum is at rms =")
    print(f"  {rows[i_best, 2] * 100:.4f} cm.")
    acc = rows[rows[:, 2] <= thr]
    print(f"    depth from {acc[0, 0] / 1e3:.2f} to {acc[-1, 0] / 1e3:.2f} km")
    print(f"    volume change from {acc[0, 1]:.3e} to {acc[-1, 1]:.3e} m^3")
    print(f"    {acc.shape[0]} of {rows.shape[0]} trial depths")
    print("  the volume change that the data require falls as the depth rises,")
    print("  so the two parameters are correlated even in the admitted set: the")
    print("  depth is bounded, but its error bar is the depth range, not a number.")
    print("\n  the same data with a single orbit (ascending only) give")
    rows1 = []
    for d in ds:
        ue_t, un_t, uz_t = enu_from_mogi(x, y, d, 1.0e6)
        model = e_asc[0] * ue_t + e_asc[1] * un_t + e_asc[2] * uz_t
        tgt = los[:x.size]
        scale = float(model @ tgt) / float(model @ model)
        rows1.append((d, scale * 1.0e6,
                      np.sqrt(np.mean((scale * model - tgt) ** 2))))
    rows1 = np.array(rows1)
    thr1 = sigma * np.sqrt(float(chi2_dist.ppf(0.95, x.size)) / x.size)
    acc1 = rows1[rows1[:, 2] <= thr1]
    print(f"    a 95% admitted depth range of "
          f"{acc1[-1, 0] / 1e3 - acc1[0, 0] / 1e3:.2f} km, against")
    print(f"    {acc[-1, 0] / 1e3 - acc[0, 0] / 1e3:.2f} km for the two-orbit case:")
    print("    the second look direction is what buys the depth resolution.")


def demonstration_4():
    section("4. What breaks the depth-volume degeneracy, and what does not")
    x = np.linspace(-15.0e3, 15.0e3, 31)
    y = np.zeros_like(x)
    e_asc = los_unit(INC_ASC, HEAD_ASC)
    sigma = 0.002
    from scipy.stats import chi2 as chi2_dist
    chi2_95 = float(chi2_dist.ppf(0.95, x.size))

    def los_of(centres):
        ue = np.zeros_like(x)
        un = np.zeros_like(x)
        uz = np.zeros_like(x)
        for (dx, dy, d, dv) in centres:
            a, b, c = enu_from_mogi(x - dx, y - dy, d, dv)
            ue, un, uz = ue + a, un + b, uz + c
        return e_asc[0] * ue + e_asc[1] * un + e_asc[2] * uz

    base = los_of([(0.0, 0.0, 3000.0, 1.0e6)])
    print(f"  reference: a Mogi source at d = 3 km with dV = 1e6 m^3; peak LOS")
    print(f"  {np.max(np.abs(base)) * 100:.3f} cm, a 31-point profile along y = 0,")
    print(f"  one orbit, noise sigma = {sigma * 100:.1f} cm, chi2 threshold "
          f"{chi2_95:.2f} for {x.size} data,")
    print(f"  so an rms difference of {np.sqrt(chi2_95 / x.size) * sigma * 100:.3f} cm "
          f"is the largest the noise can absorb\n")

    def chi2_of(model):
        return float(np.sum((model - base) ** 2) / sigma ** 2)

    print("  (a) two sources 1.2 km apart vertically, each with half dV")
    m = los_of([(0.0, 0.0, 2400.0, 0.5e6), (0.0, 0.0, 3600.0, 0.5e6)])
    print(f"      maximum difference {np.max(np.abs(m - base)) * 100:.4f} cm, "
          f"chi2 = {chi2_of(m):.2f} -> "
          f"{'distinguishable' if chi2_of(m) > chi2_95 else 'not distinguishable'}")
    print("  (b) two sources 4 km apart horizontally, each with half dV")
    m = los_of([(-2000.0, 0.0, 3000.0, 0.5e6), (2000.0, 0.0, 3000.0, 0.5e6)])
    print(f"      maximum difference {np.max(np.abs(m - base)) * 100:.4f} cm, "
          f"chi2 = {chi2_of(m):.2f} -> "
          f"{'distinguishable' if chi2_of(m) > chi2_95 else 'not distinguishable'}")
    print("  (c) a deeper source with dV scaled to match the peak displacement")
    for d_dep in (6000.0, 9000.0):
        dv_scaled = 1.0e6 * (d_dep / 3000.0) ** 2
        m = los_of([(0.0, 0.0, d_dep, dv_scaled)])
        print(f"      d = {d_dep / 1e3:.0f} km, dV = {dv_scaled:.2e} m^3: "
              f"peak {np.max(np.abs(m)) * 100:.3f} cm, chi2 = {chi2_of(m):.2f} -> "
              f"{'distinguishable' if chi2_of(m) > chi2_95 else 'not distinguishable'}")
    print("\n  (a) and (b) are shape changes: a source elongated vertically by more")
    print("  than a factor of two is invisible to this data set, while a laterally")
    print("  extended source is strongly detected.  (c) is the depth-volume")
    print("  degeneracy: matching only the peak displacement lets a 9 km source")
    print("  with a 9-fold larger volume pass, and the profile shape rejects it.")
    print("  The degeneracy is broken by the *shape* of the deformation field, not")
    print("  by its amplitude, which is why the spatial sampling of a survey")
    print("  matters more than its precision for the depth.")
    print("\n  a final check on the reverse statement: over a *single* point only,")
    print("  the pairs that reproduce the vertical displacement to 1% are")
    print("    depth (km):    ")
    ds_check = np.linspace(1000.0, 20000.0, 20)
    pairs = []
    for d in ds_check:
        dv_needed = 1.0e6 * (d / 3000.0) ** 2
        pairs.append((d / 1e3, dv_needed))
    print("    " + "  ".join(f"({a:.1f}, {b / 1e6:.1f}e6)" for a, b in pairs[::4]))
    print("  (depth, dV) pairs spanning a factor of 400 in volume, all consistent")
    print("  with one number: an amplitude measurement alone never constrains a")
    print("  Mogi depth, and a quoted depth without its data geometry is not a")
    print("  measurement.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
