#!/usr/bin/env python3
"""GPR in archaeology, forensics and utility mapping: hyperbola geometry,
target amplitude, the Rayleigh regime, lateral resolution and migration.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_archaeology_forensics_demo.py

All models and data in this module are SYNTHETIC.  The permittivities, targets,
depths, target sizes, pick errors and noise are chosen teaching values, not
measurements from any site, excavation or forensic case.  Physical constants and
standard material permittivities are labelled as such.

Contents
--------
1. A point target: the diffraction hyperbola, and what a fit recovers from a
   long and a short aperture (Monte Carlo on the picking error).
2. Reflection coefficients for the targets a utility or forensic survey looks
   for, in one soil.
3. Small targets in the Rayleigh regime: the cubic size dependence and the
   dynamic range it demands.
4. Lateral resolution: the first Fresnel zone at three frequencies and depths.
5. Kirchhoff migration of a synthetic hyperbola with the right and the wrong
   velocity: focus quality, measured.
6. The depth error of a wrong overburden velocity, which is linear in v.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458        # m/ns (exact)
EPS_SOIL = 9.0              # SYNTHETIC soil permittivity of the teaching site
F0_GHZ = 0.5                # SYNTHETIC antenna centre frequency, GHz
Z_TARGET_M = 1.50           # SYNTHETIC target depth
SIGMA_PICK_NS = 0.20        # SYNTHETIC pick standard deviation


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def v_of_eps(eps):
    return C_M_NS / np.sqrt(eps)


def reflection_coeff(eps1, eps2):
    return (np.sqrt(eps1) - np.sqrt(eps2)) / (np.sqrt(eps1) + np.sqrt(eps2))


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def fit_hyperbola(x_m, t_ns):
    """Least squares fit of t^2 = 4 x^2 / v^2 + t0^2.  Returns (v, z)."""
    m, c = np.polyfit(x_m ** 2, t_ns ** 2, 1)
    v = 2.0 / np.sqrt(m)
    z = np.sqrt(c) * v / 2.0
    return v, z


def main():
    v_true = v_of_eps(EPS_SOIL)
    section("1. The diffraction hyperbola: what an aperture can buy")
    print(f"SYNTHETIC target at {Z_TARGET_M:.2f} m in a soil with eps_r = "
          f"{EPS_SOIL:.1f} -> v = {v_true:.4f} m/ns")
    print(f"apex two-way time = 2 z / v = {2 * Z_TARGET_M / v_true:.2f} ns")
    for aperture in (2.00, 0.50):
        x = np.linspace(-aperture, aperture, 41)
        t_clean = 2.0 * np.sqrt(x ** 2 + Z_TARGET_M ** 2) / v_true
        n_real = 4000
        vs = np.empty(n_real)
        zs = np.empty(n_real)
        for i in range(n_real):
            t_noisy = t_clean + RNG.normal(0.0, SIGMA_PICK_NS, x.size)
            vs[i], zs[i] = fit_hyperbola(x, t_noisy)
        rho = float(np.corrcoef(vs, zs)[0, 1])
        print(f"\n  aperture +/-{aperture:.2f} m, pick error "
              f"{SIGMA_PICK_NS:.2f} ns:")
        print(f"    velocity: mean {vs.mean():.4f} m/ns, standard deviation "
              f"{vs.std():.4f} m/ns ({vs.std() / vs.mean() * 100:.1f}%)")
        print(f"    depth   : mean {zs.mean():.4f} m, standard deviation "
              f"{zs.std():.4f} m ({zs.std() / zs.mean() * 100:.1f}%)")
        print(f"    correlation coefficient between the pair: {rho:+.3f}")
    print("\n  A short aperture turns the pair into one number: velocity and")
    print("  depth trade against each other almost perfectly, and only the apex")
    print("  time is well constrained.  That is why a velocity picked from a")
    print("  single hyperbola must be quoted with the aperture it came from.")

    section("2. Target reflection coefficients in one soil")
    print(f"  host soil eps_r = {EPS_SOIL:.1f}; R = (sqrt(e1)-sqrt(e2)) / (sum)")
    print("  target                   eps_r    R        power (dB)   note")
    for name, eps, note in (("metal (perfect conductor)", 1.0e9,
                             "R -> -1; the extreme limit"),
                            ("air-filled void", 1.0, "strong, of either sign"),
                            ("water-filled void", 80.1, "sign inverted"),
                            ("plastic pipe (solid)", 2.6, "weak, no interior"),
                            ("concrete (dry)", 6.0, "weak")):
        r = reflection_coeff(EPS_SOIL, eps)
        print(f"  {name:24s} {eps:8.1f}  {r:+7.3f}  {20 * np.log10(abs(r)):11.1f}   {note}")
    print("\n  The utility that matters is not the pipe MATERIAL but what fills")
    print("  the pipe: a plastic pipe with air inside is a strong air/soil")
    print("  contact, while a plastic pipe full of water in wet soil is nearly")
    print("  invisible.  The measured contrast is a property of the whole")
    print("  target-host pair, never of the target alone.")

    section("3. Small targets: the Rayleigh regime")
    print("  For a body much smaller than the wavelength the scattered")
    print("  amplitude scales as (volume) x f^2, i.e. as a^3 for a fixed shape.")
    print("  radius (m)   relative amplitude   dB   ")
    a_ref = 0.04
    for a in (0.01, 0.02, 0.04, 0.08):
        amp = (a / a_ref) ** 3
        print(f"  {a:10.2f}   {amp:18.4f}   {20 * np.log10(amp):+5.1f}")
    print("  Halving the radius costs 18 dB: 8 times in amplitude, 64 times in")
    print("  power.  A 1 cm target is 36 dB weaker than a 4 cm one.  Detection")
    print("  is therefore a dynamic-range question long before it is a")
    print("  resolution question, and a small target can be resolved in")
    print("  principle while being far below the noise.")

    section("4. Lateral resolution: the first Fresnel zone radius")
    print("  r_f = sqrt(lambda z / 2) with lambda = v / f in the soil")
    print("  f (MHz)   z (m)   lambda (m)   r_f (m)")
    for f_mhz in (250.0, 500.0, 1000.0):
        lam = v_true / (f_mhz * 1e-3)
        for z in (0.5, 1.5, 3.0):
            print(f"  {f_mhz:7.0f}   {z:5.1f}   {lam:10.3f}   "
                  f"{np.sqrt(lam * z / 2.0):7.3f}")
    print("  The Fresnel zone is the footprint that contributes to one echo, not")
    print("  the minimum separation of two resolvable targets; the separation")
    print("  limit is the same order but is a different number, and it depends")
    print("  on the contrast and the noise as well as on lambda.")

    section("5. Kirchhoff migration with the right and the wrong velocity")
    nt, nx = 1000, 121
    dt_ns = 0.05
    t = np.arange(nt) * dt_ns
    x = np.linspace(-3.0, 3.0, nx)
    d = np.zeros((nt, nx))
    for j, xj in enumerate(x):
        tj = 2.0 * np.sqrt(xj ** 2 + Z_TARGET_M ** 2) / v_true
        d[:, j] = ricker(t, tj, F0_GHZ)
    print(f"  synthetic section: {nt} samples at {dt_ns:.2f} ns, {nx} traces at "
          f"{x[1] - x[0]:.3f} m")
    print("  v_mig (m/ns)   depth of max (m)   peak amplitude   half-width (m)")
    for v_mig in (0.08, v_true, 0.12):
        img = np.zeros((nt, nx))
        for j0, x0 in enumerate(x):
            for j, xj in enumerate(x):
                t_mig = np.sqrt(t ** 2 + 4.0 * (xj - x0) ** 2 / v_mig ** 2)
                img[:, j0] += np.interp(t_mig, t, d[:, j], left=0.0, right=0.0)
        img /= nx
        i_apex = int(np.argmax(img[:, nx // 2]))
        amp = img[i_apex, nx // 2]
        row = img[i_apex, :]
        above = np.where(row >= 0.5 * amp)[0]
        width = (above[-1] - above[0]) * (x[1] - x[0]) if above.size > 1 else 0.0
        print(f"  {v_mig:12.4f}   {i_apex * dt_ns * v_mig / 2.0:16.3f}   "
              f"{amp:14.4f}   {width:14.3f}")
    print("  The apex time is set by the DATA and cannot be changed by the")
    print("  migration velocity, so a wrong velocity moves the depth linearly")
    print("  and simultaneously broadens and weakens the focus.  Focus quality")
    print("  is therefore a velocity diagnostic, and the depth is the same")
    print("  number the velocity just moved.")

    section("6. Depth error from the overburden velocity")
    t0 = 2.0 * Z_TARGET_M / v_true
    print(f"  measured apex time {t0:.2f} ns; true depth {Z_TARGET_M:.2f} m at "
          f"v = {v_true:.4f} m/ns")
    print("  assumed v (m/ns)   reported depth (m)   error (m)   error (%)")
    for v_ass in (0.070, 0.080, 0.090, 0.100, v_true, 0.110):
        z_rep = v_ass * t0 / 2.0
        print(f"  {v_ass:16.4f}   {z_rep:18.2f}   {z_rep - Z_TARGET_M:+9.2f}   "
              f"{(z_rep / Z_TARGET_M - 1.0) * 100:+8.1f}")
    print("\n  z = v t / 2 is exactly linear in v.  A depth reported without its")
    print("  velocity carries a fractional error equal to the velocity error,")
    print("  and the velocity error is the one nobody can see on the section.")


if __name__ == "__main__":
    main()
