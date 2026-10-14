#!/usr/bin/env python3
"""Gravity for minerals: body shapes, the depth rule that is exact, the slab and
free-air corrections, regional removal, and the excess-mass invariant.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_for_minerals_demo.py

Everything here is SYNTHETIC.  Density contrasts, geometries, station spacing,
noise, the regional functions and the drill-hole densities are chosen teaching
values, not measurements or properties of any real deposit.

Contents
--------
1. Two body shapes: the sphere (1/z^2) and the infinite horizontal cylinder
   (1/z), with the anomaly formulas derived from the potential.
2. Anomaly amplitudes for three deposit classes in one common geometry.
3. The exact depth rule of the cylinder: half-width at half-maximum = depth, and
   the bias produced by using a sphere rule on a cylinder anomaly.
4. Free-air and Bouguer slab corrections, computed from standard constants.
5. Regional removal: how the fitted regional order changes the residual
   amplitude and the depth it implies.
6. The excess-mass invariant from Gauss's law, and its window sensitivity.
7. Verification: point-mass superposition against the line-mass formula, the
   excess-mass integral against the analytic value, and the sphere/cylinder
   power laws.
"""

import numpy as np
from scipy import optimize

RNG = np.random.default_rng(20261014)

G_NEWTON = 6.67430e-11        # m^3 kg^-1 s^-2
MGAL = 1.0e-5                 # m/s^2 per mGal
G_STANDARD = 9.80665          # m/s^2, standard gravity
R_EARTH = 6.371e6             # m, mean Earth radius

R_BODY = 100.0                # radius of the cylinder and sphere models, m
Z_BODY = 200.0                # depth to centre or axis, m
CONTRASTS = {                 # SYNTHETIC density contrasts vs host, kg/m^3
    "chromite": 800.0,
    "massive sulphide": 600.0,
    "iron ore (hematite-rich)": 900.0,
}
RHO_SURVEY = 2670.0           # reduction density for the Bouguer slab, kg/m^3


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def sphere_mgal(drho, r=R_BODY, z=Z_BODY):
    """Buried sphere: dg = (4/3) pi G drho r^3 / z^2."""
    return (4.0 / 3.0 * np.pi * G_NEWTON * drho * r ** 3 / z ** 2) / MGAL


def cylinder_mgal(drho, r=R_BODY, z=Z_BODY):
    """Infinite horizontal cylinder: dg = 2 pi G drho r^2 / z."""
    return 2.0 * np.pi * G_NEWTON * drho * r ** 2 / z / MGAL


def cylinder_profile(drho, x, r=R_BODY, z=Z_BODY):
    """2-D horizontal cylinder: dg(x) = 2 G lambda z / (x^2 + z^2)."""
    lam = drho * np.pi * r ** 2          # mass per unit length, kg/m
    return 2.0 * G_NEWTON * lam * z / (x ** 2 + z ** 2) / MGAL


def sphere_profile(drho, x, r=R_BODY, z=Z_BODY):
    """Profile of a sphere: dg(x) = (4/3) pi G drho r^3 z / (x^2+z^2)^1.5."""
    return ((4.0 / 3.0 * np.pi * G_NEWTON * drho * r ** 3 * z)
            / (x ** 2 + z ** 2) ** 1.5) / MGAL


def half_width_at_half_max(x, profile):
    """Distance from the peak to the 50% point, in metres."""
    i_pk = int(np.argmax(profile))
    target = 0.5 * profile[i_pk]
    for i in range(i_pk + 1, len(profile)):
        if profile[i] <= target:
            return float(x[i - 1] + (x[i] - x[i - 1]) * (
                profile[i - 1] - target) / (profile[i - 1] - profile[i])
                - x[i_pk])
    return np.nan


def main():
    section("1. Two body shapes and their depth behaviour")
    print("potential -> attraction, for two ideal bodies:")
    print("  sphere, centre at depth z:      M = (4/3) pi r^3 drho,  "
          "dg = G M / z^2")
    print("  infinite horizontal cylinder:   lambda = pi r^2 drho per unit")
    print("                                  length,  dg = 2 G lambda / z")
    rho_s = 2.67e3
    print(f"\nthe factor-2 difference in the 1/z power is not a detail:")
    print(f"{'z (m)':>8s} {'sphere (mGal)':>14s} {'cylinder (mGal)':>16s} "
          f"{'ratio':>8s}")
    for z in (100.0, 200.0, 400.0, 800.0):
        s = sphere_mgal(600.0, z=z)
        c = cylinder_mgal(600.0, z=z)
        print(f"{z:8.0f} {s:14.4f} {c:16.4f} {c / s:8.2f}")
    print("the cylinder decays as 1/z and the sphere as 1/z^2.  For equal anomaly")
    print("amplitude at equal radius, solve for the depths:")
    for z_s in (100.0, 200.0, 400.0):
        a = sphere_mgal(600.0, z=z_s)
        f = lambda zc: cylinder_mgal(600.0, z=zc) - a
        if f(20000.0) < 0.0:
            z_c = optimize.brentq(f, 1.0, 20000.0)
            print(f"  sphere at {z_s:5.0f} m -> cylinder at {z_c:7.1f} m "
                  f"(factor {z_c / z_s:5.2f})")
    print("the factor grows without bound: with 1/z versus 1/z^2 there is no")
    print("fixed 'twice as deep' rule, and any such rule depends on the noise")
    print("threshold as well as the geometry.  Which formula applies is a")
    print("statement about the body's ASPECT RATIO, not about the method.")

    section("2. Anomaly amplitudes for three deposit classes")
    print(f"common geometry: radius {R_BODY:.0f} m, depth {Z_BODY:.0f} m "
          f"(SYNTHETIC contrasts)")
    print(f"{'class':26s} {'drho (kg/m3)':>13s} {'sphere (mGal)':>14s} "
          f"{'cylinder (mGal)':>16s}")
    for name, drho in CONTRASTS.items():
        print(f"{name:26s} {drho:13.0f} {sphere_mgal(drho):14.3f} "
              f"{cylinder_mgal(drho):16.3f}")
    print("the chromite contrast is the largest and the massive sulphide body")
    print("depends on its sulphide content: in practice the density contrast of a")
    print("massive sulphide body spans a wide range, and that range is the largest")
    print("single uncertainty in a gravity target model.")

    section("3. The cylinder's exact depth rule, and the bias from using the "
            "sphere rule")
    x = np.linspace(-2000.0, 2000.0, 400001)
    prof_c = cylinder_profile(600.0, x)
    hw = half_width_at_half_max(x, prof_c)
    print("for the cylinder, dg(x)/dg(0) = z^2/(x^2+z^2) exactly, so the")
    print("half-width at half-maximum is x_1/2 = z with no calibration at all:")
    print(f"    measured half-width = {hw:.3f} m for a true depth of "
          f"{Z_BODY:.0f} m  (ratio {hw / Z_BODY:.6f})")
    prof_s = sphere_profile(600.0, x)
    hw_s = half_width_at_half_max(x, prof_s)
    # For the sphere the half-width ratio is a fixed number; calibrate it.
    ratio_s = hw_s / Z_BODY
    print(f"for the sphere the ratio is a constant, {ratio_s:.6f} "
          f"(x_1/2 = z sqrt(2^(2/3)-1) = {np.sqrt(2 ** (2 / 3) - 1):.6f} z)")
    print("\nnow apply the sphere rule to a cylinder anomaly (a model error):")
    print(f"    inferred depth = {hw / ratio_s:.1f} m instead of {Z_BODY:.0f} m "
          f"-> error {hw / ratio_s - Z_BODY:+.1f} m "
          f"({(hw / ratio_s / Z_BODY - 1) * 100:+.1f}%)")
    print("half-width rules are only as good as the shape assumption, and the")
    print("shape is what a single profile constrains least.")

    section("4. Free-air and Bouguer slab corrections (standard constants)")
    fa_gradient = 2.0 * G_STANDARD / R_EARTH
    print(f"free-air gradient = 2 g / a = 2({G_STANDARD:.5f})/({R_EARTH:.4e})")
    print(f"                  = {fa_gradient:.6e} s^-2 = "
          f"{fa_gradient / MGAL:.4f} mGal/m")
    print("(the conventional reference-ellipsoid value is 0.3086 mGal/m; the")
    print("difference is the latitude dependence of the normal gradient)")
    print("\nBouguer slab: an infinite flat sheet of thickness t and density rho")
    print("produces the exact vertical attraction 2 pi G rho t, so")
    print(f"{'rho (kg/m3)':>12s} {'slab (mGal/m)':>15s} {'100 m relief (mGal)':>20s}")
    for rho in (2200.0, 2670.0, 3000.0):
        slab = 2.0 * np.pi * G_NEWTON * rho / MGAL
        print(f"{rho:12.0f} {slab:15.4f} {slab * 100:20.2f}")
    slab = 2.0 * np.pi * G_NEWTON * RHO_SURVEY / MGAL
    print(f"\nfor 100 m of relief: free-air = {fa_gradient / MGAL * 100:.2f} mGal,")
    print(f"Bouguer slab at {RHO_SURVEY:.0f} kg/m3 = {slab * 100:.2f} mGal, net = "
          f"{fa_gradient / MGAL * 100 - slab * 100:.2f} mGal")
    print("the two corrections are both large and nearly cancel: a 100 m terrain")
    print("step produces a residual of a few mGal, which is why a 0.02 mGal")
    print("levelling tolerance demands that the height of every station be known")
    print("to a few tens of centimetres.")

    section("5. Regional removal: the residual is a choice")
    xr = np.linspace(-4000.0, 4000.0, 801)
    drho = 600.0
    anom = cylinder_profile(drho, xr, r=120.0, z=250.0)
    regional = 0.0045 * xr + 0.6          # SYNTHETIC linear regional, mGal
    observed = anom + regional + 0.02 * RNG.standard_normal(xr.size)
    print("observed profile = SYNTHETIC cylinder anomaly + a linear regional + "
          "0.02 mGal noise")
    fitted = {order: np.polyval(np.polyfit(xr, observed, order), xr)
              for order in (0, 1, 2, 3)}
    print(f"\n{'regional order':>15s} {'residual peak (mGal)':>21s} "
          f"{'half-width (m)':>15s} {'implied depth (m)':>18s}")
    for order, fit in fitted.items():
        resid = observed - fit
        hwr = half_width_at_half_max(xr, resid)
        i_pk = int(np.argmax(resid))
        interior = 0 < i_pk < resid.size - 1
        if np.isnan(hwr) or not interior:
            print(f"{order:15d} {resid.max():21.4f} {'undefined':>15s} "
                  f"{'undefined':>18s}")
        else:
            print(f"{order:15d} {resid.max():21.4f} {hwr:15.1f} {hwr:18.1f}")
    print("order 0 (a constant) leaves the linear regional in the residual, so the")
    print("residual has no closed maximum and no depth can be extracted at all.")
    print("the residual amplitude moves by tens of per cent and the implied depth")
    print("by tens of metres, purely as a function of the polynomial order chosen")
    print("to represent 'the regional'.  The residual is not measured; it is")
    print("defined by subtracting a model, and a depth that depends on it must be")
    print("reported with the regional model attached.")

    section("6. The excess-mass invariant")
    print("Gauss's law applied to the vertical attraction gives, for a 2-D body")
    print("(a profile across an infinite strike length),")
    print("    lambda = (1/2 pi G) integral dg dx    [mass per unit length],")
    print("which needs neither the shape nor the depth.  For a 3-D body the same")
    print("law needs a MAP, not a profile: the surface integral over the plane is")
    print("     integral integral dg dA = 2 pi G M.")
    lam_true = drho * np.pi * 120.0 ** 2
    print(f"\ntrue excess mass per unit length = pi R^2 drho = "
          f"{lam_true:.6e} kg/m")
    print(f"{'window (km)':>12s} {'integral (mGal m)':>18s} "
          f"{'lambda (kg/m)':>16s} {'ratio to true':>14s}")
    for half in (500.0, 1000.0, 2000.0, 4000.0):
        sel = np.abs(xr) <= half
        integral = float(np.trapezoid(anom[sel], xr[sel]))
        lam_int = integral * MGAL / (2.0 * np.pi * G_NEWTON)
        print(f"{2 * half / 1000:12.1f} {integral:18.2f} {lam_int:16.6e} "
              f"{lam_int / lam_true:14.4f}")
    print("the recovered mass converges as the window grows, because the 1/z tail")
    print("of the cylinder decays slowly; truncating too early UNDERESTIMATES it.")
    print("\nthe same integral for a buried SPHERE profile is not a mass at all:")
    print("    integral dg dx = 2 G M / z,   so a profile gives M/z, not M --")
    print("    the same mass-depth trade-off as the amplitude.")
    m_true = 600.0 * 4.0 / 3.0 * np.pi * 120.0 ** 3
    print(f"{'window (km)':>12s} {'integral (mGal m)':>18s} "
          f"{'2 G M/z (mGal m)':>18s} {'ratio':>8s}")
    exact_3d = 2.0 * G_NEWTON * m_true / 250.0 / MGAL
    for half in (1000.0, 2000.0, 4000.0):
        sel = np.abs(xr) <= half
        integral = float(np.trapezoid(
            sphere_profile(600.0, xr, r=120.0, z=250.0)[sel], xr[sel]))
        print(f"{2 * half / 1000:12.1f} {integral:18.2f} {exact_3d:18.2f} "
              f"{integral / exact_3d:8.4f}")
    print("so the shape-free invariant exists for 2-D bodies from a profile, and")
    print("for 3-D bodies only from a map.  This is the price of the extra")
    print("dimension: the third dimension has to be measured, not estimated.")

    section("7. Verification")
    # (a) point-mass superposition of a finite line mass vs the 2-D formula.
    print("(a) a finite line of point masses, length L, versus the 2-D formula")
    print(f"{'L (km)':>8s} {'centre (mGal)':>14s} {'2 pi G rho R^2/z (mGal)':>24s} "
          f"{'ratio':>8s}")
    lam = 600.0 * np.pi * 100.0 ** 2
    xp = np.array([0.0])
    for L in (2000.0, 5000.0, 20000.0, 100000.0):
        n = 4001
        ax = np.linspace(-L / 2, L / 2, n)
        dx = L / (n - 1)
        # attraction of line elements at depth z, observed at the origin
        g = np.sum(G_NEWTON * lam * dx * Z_BODY
                   / (xp[:, None] ** 2 + ax[None, :] ** 2 + Z_BODY ** 2) ** 1.5,
                   axis=1)
        exact = 2.0 * np.pi * G_NEWTON * 600.0 * 100.0 ** 2 / Z_BODY
        print(f"{L / 1000:8.0f} {g[0] / MGAL:14.4f} {exact / MGAL:24.4f} "
              f"{g[0] / exact:8.4f}")
    print("    convergence to the 2-D result as the line lengthens is the check")
    print("    that the cylinder formula is the long-line limit of point masses.")
    # (b) excess-mass integral against the analytic value
    sel = np.abs(xr) <= 4000.0
    lam_num = (float(np.trapezoid(anom[sel], xr[sel])) * MGAL
               / (2.0 * np.pi * G_NEWTON))
    print(f"(b) excess-mass integral over a 8 km window: "
          f"{lam_num:.6e} kg/m vs analytic {lam_true:.6e} kg/m, "
          f"ratio {lam_num / lam_true:.6f}")
    print(f"    the 2-D profile of a 3-D body instead gives 2GM/z: "
          f"{float(np.trapezoid(sphere_profile(600.0, xr, r=120.0, z=250.0)[sel], xr[sel])):.2f}"
          f" mGal m vs {2.0 * G_NEWTON * m_true / 250.0 / MGAL:.2f} mGal m")
    # (c) power laws
    zz = np.array([100.0, 200.0, 400.0, 800.0])
    ps = np.array([sphere_mgal(600.0, z=z) for z in zz])
    pc = np.array([cylinder_mgal(600.0, z=z) for z in zz])
    print(f"(c) fitted exponents: sphere "
          f"{np.polyfit(np.log(zz), np.log(ps), 1)[0]:.6f} (expect -2), "
          f"cylinder {np.polyfit(np.log(zz), np.log(pc), 1)[0]:.6f} (expect -1)")
    # (d) the analytic half-width of the sphere anomaly
    print(f"(d) sphere half-width/depth measured {ratio_s:.6f} against the "
          f"analytic sqrt(2^(2/3)-1) = {np.sqrt(2 ** (2 / 3) - 1):.6f}")


if __name__ == "__main__":
    main()
