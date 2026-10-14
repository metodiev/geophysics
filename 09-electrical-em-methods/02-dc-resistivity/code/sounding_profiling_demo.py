#!/usr/bin/env python3
"""Sounding versus profiling: what a spacing sweep and a traverse each resolve.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sounding_profiling_demo.py

Everything is SYNTHETIC.  The layered models, the dip and the noise level are
chosen teaching values; no field data are used.  The profiling experiment uses a
locally one-dimensional approximation, which is stated where it is used.

Contents
--------
1. A sounding over a four-layer aquifer model, with the parameters that matter.
2. Vertical resolution: which layer parameters the sounding separates.
3. Profiling across a dipping contact in the locally 1-D approximation.
4. The lateral footprint of an array, and the smearing it causes.
5. Sounding and profiling side by side: what each is for.
"""

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

RNG = np.random.default_rng(20261014)

I_INJECT = 0.1          # A
NOISE_REL = 0.02        # 2% relative noise on dV


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def kernel_R(rhos, hs, lam):
    R = 0.0
    for i in range(len(hs) - 1, -1, -1):
        k = (rhos[i + 1] - rhos[i]) / (rhos[i + 1] + rhos[i])
        R = (k + R) * np.exp(-2.0 * lam * hs[i]) / (1.0 + k * R)
    return R


def layered_potential(rhos, hs, r, I=1.0):
    lam_max = 30.0 / min(hs)
    integrand = (lambda lam: (1.0 / (1.0 - kernel_R(rhos, hs, lam)) - 1.0)
                 * j0(lam * r))
    value, _ = quad(integrand, 0.0, lam_max, limit=600)
    return rhos[0] * I / (2.0 * np.pi) * (1.0 / abs(r) + value)


def wenner_rhoa(rhos, hs, a, I=I_INJECT):
    k = 2.0 * np.pi * a
    dV = (layered_potential(rhos, hs, a, I)
          - layered_potential(rhos, hs, 2.0 * a, I)
          - layered_potential(rhos, hs, 2.0 * a, I)
          + layered_potential(rhos, hs, a, I))
    return k * dV / I, dV


def main():
    section("1. A sounding over a four-layer aquifer model")
    # SYNTHETIC teaching model: dry sand over an aquifer over a clay aquitard
    # over bedrock.
    rhos = [200.0, 30.0, 5.0, 500.0]
    hs = [4.0, 6.0, 8.0]
    print("  SYNTHETIC model (rho in ohm m, h in m):")
    print(f"    layer 1 dry sand       rho = {rhos[0]:6.1f}, h = {hs[0]:5.1f}")
    print(f"    layer 2 aquifer        rho = {rhos[1]:6.1f}, h = {hs[1]:5.1f}")
    print(f"    layer 3 clay aquitard  rho = {rhos[2]:6.1f}, h = {hs[2]:5.1f}")
    print(f"    half-space bedrock     rho = {rhos[3]:6.1f}")
    spacings = np.array([1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 30.0, 50.0,
                         80.0, 120.0])
    print(f"  Wenner sounding, I = {I_INJECT:.2f} A:")
    print("     a (m)    rho_a (ohm m)    dV (mV)    noise on rho_a (2%)")
    curve = []
    for a in spacings:
        ra, dv = wenner_rhoa(rhos, hs, a)
        curve.append(ra)
        print(f"  {a:8.1f} {ra:16.2f} {dv * 1e3:11.4f} "
              f"{ra * NOISE_REL:18.3f}")
    curve = np.array(curve)
    print("  the curve falls to the aquifer minimum, rises over the clay, and")
    print("  climbs toward the bedrock: each layer is one feature of the curve.")
    for lab, r in (("top layer", rhos[0]), ("aquifer", rhos[1]),
                   ("clay", rhos[2]), ("bedrock", rhos[3])):
        print(f"    {lab:<10s} rho = {r:6.1f} ohm m; closest rho_a on the "
              f"curve = {curve[np.argmin(np.abs(curve - r))]:7.2f} "
              f"at a = {spacings[np.argmin(np.abs(curve - r))]:6.1f} m")

    section("2. Vertical resolution: a thin layer against a thick one")
    print("  replace the 6 m aquifer by a layer of the same rho but different")
    print("  thickness, and see how well the sounding separates them.")
    print("     h_aquifer (m)   rho_a at a=12 (ohm m)   difference from 6 m")
    ref = wenner_rhoa(rhos, [4.0, 6.0, 8.0], 12.0)[0]
    for h_a in (2.0, 4.0, 6.0, 8.0, 12.0):
        ra = wenner_rhoa(rhos, [4.0, h_a, 8.0], 12.0)[0]
        print(f"  {h_a:15.1f} {ra:23.2f} {(ra - ref) / ref * 100:20.2f}%")
    print("  a 2 m aquifer and a 4 m aquifer differ at a = 12 m by about the")
    print(f"  {NOISE_REL * 100:.0f}% noise level; the sounding detects the aquifer")
    print("  long before it can measure its thickness.")

    section("3. Profiling across a dipping contact (locally 1-D)")
    print("  SYNTHETIC model: a two-layer ground, rho_1 = 200 ohm m over")
    print("  rho_2 = 20 ohm m, with the interface at depth")
    print("    z(x) = 4 m + 0.20 (x - 100 m)")
    print("  The traverse uses the LOCALLY 1-D approximation: at each position")
    print("  the array sees a layered model with the local thickness.  This is")
    print("  an approximation, not an exact 2-D solution; it is used to show")
    print("  where the apparent edge moves, not to predict amplitudes.")
    x_contact_m = 100.0 - 4.0 / 0.20      # where z(x) = 0
    print(f"  the interface reaches the surface at x = {x_contact_m:.1f} m")
    print("\n     x (m)   true z(x)    rho_a, a=2   rho_a, a=5   rho_a, a=10")
    for x in np.arange(80.0, 120.1, 5.0):
        z = 4.0 + 0.20 * (x - 100.0)
        if z <= 0.0:
            row = [200.0, 200.0, 200.0]
        else:
            row = [wenner_rhoa([200.0, 20.0], [z], a)[0] for a in (2.0, 5.0, 10.0)]
        print(f"  {x:7.1f} {z:10.2f} {row[0]:12.2f} {row[1]:12.2f} "
              f"{row[2]:12.2f}")
    print("  at every position the LONG spacing shows the larger drop here,")
    print("  because it samples deeper where the conductor is nearer; what it")
    print("  pays is a wider footprint, which section 4 quantifies.")

    section("4. Lateral footprint of the array, and the smearing it causes")
    # The lateral footprint is the array sensitivity integrated over depth and
    # over the direction across the line.  It is computed from the analytic
    # kernel of a homogeneous half-space, integrated over y and z.
    a = 5.0
    A_p, B_p, M_p, N_p = -1.5 * a, 1.5 * a, -0.5 * a, 0.5 * a

    def quiet(x):
        if abs(x - A_p) < 1e-6 or abs(x - B_p) < 1e-6 or abs(x - M_p) < 1e-6 \
                or abs(x - N_p) < 1e-6:
            return 0.0

        def inner(yy, zz):
            if zz < 1e-3:
                return 0.0

            def grad(xe):
                dx, dy = x - xe, yy
                r2 = dx * dx + dy * dy + zz * zz
                return np.array([-dx, -dy, -zz]) / r2 ** 1.5
            return (grad(A_p) - grad(B_p)) @ (grad(M_p) - grad(N_p))

        val, _ = quad(lambda zz: quad(lambda yy: inner(yy, zz), -60.0, 60.0,
                                      limit=200)[0], 0.0, 60.0, limit=200)
        return val

    dV_wenner = 200.0 * I_INJECT / (2.0 * np.pi * a)   # on a 200 ohm m half-space
    xs = np.arange(-40.0, 40.5, 1.0)
    foot = np.array([quiet(x) for x in xs])
    # h_raw(x) = integral of S_rho over y and z.  Its integral over x is fixed
    # by the kernel normalisation: integral S_rho dV = V/(2 rho), so
    # integral h_raw dx = V/(2 rho) * 8 pi^2 / I.
    norm = np.trapezoid(foot, xs)
    print(f"  integral of the raw kernel over the whole half-space = "
          f"{norm:.4e},")
    print("  and V/(2 rho) * 8 pi^2 / I for this array = "
          f"{dV_wenner / (2 * 200.0) * 8 * np.pi ** 2 / I_INJECT:.4e}")
    foot = foot / norm
    print(f"  Wenner a = {a:.1f} m: footprint h(x) = integral of S_rho dy dz,")
    print(f"  normalised so that integral h dx = 1 "
          f"(raw integral = {norm:.6e})")
    print("     x (m)      h(x) (1/m)")
    for x, h in zip(xs[::4], foot[::4]):
        print(f"  {x:8.1f} {h:14.6f}")
    # smear a step change: smoothed(x) = integral h(u) rho(x - u) du, with u the
    # array-relative coordinate.  This is the linear (Born) answer and shows the
    # loss of edge sharpness directly.
    print("\n  convolving a step change in rho (200 -> 20 ohm m at x = 0):")
    step = np.where(xs < 0.0, 200.0, 20.0)
    smear = np.array([np.trapezoid(foot * np.interp(x - xs, xs, step), xs)
                      for x in xs])
    print("     x (m)   true rho   smoothed rho")
    for x, t, sm in zip(xs[::4], step[::4], smear[::4]):
        print(f"  {x:8.1f} {t:10.1f} {sm:14.2f}")
    target_lo = 0.9 * 200.0 + 0.1 * 20.0     # 182
    target_hi = 0.1 * 200.0 + 0.9 * 20.0     # 38
    def crossing(level):
        """First x where the smoothed curve falls through a level."""
        idx = int(np.nonzero(smear < level)[0][0])
        x0, x1 = xs[idx - 1], xs[idx]
        s0, s1 = smear[idx - 1], smear[idx]
        return x0 + (level - s0) * (x1 - x0) / (s1 - s0)

    xlo, xhi = crossing(target_lo), crossing(target_hi)
    print(f"  the 10-90% width of the smoothed step is {xhi - xlo:.1f} m,")
    print("  against a zero-width true step.  A lateral contact is smeared over")
    print("  a distance of the order of the array aperture, and no processing")
    print("  recovers wavelengths the array never measured.")
    print("  Note also the negative sidelobes at x = +-4 m in the footprint:")
    print("  the array has small regions where adding resistivity LOWERS the")
    print("  apparent resistivity, so an edge can overshoot before it settles.")

    section("5. Sounding and profiling side by side")
    print("  sounding:  fixed centre, varying spacing -> vertical profile")
    print("             one dimension, and it assumes lateral uniformity")
    print("  profiling: fixed spacing, moving centre -> lateral variation at")
    print("             one approximate depth, smeared over the array length")
    print("  a real survey does both, and the classic failure is to read a")
    print("  lateral change as a depth change: moving an array across a")
    print("  conductive body lowers rho_a exactly as a deeper conductor does.")


if __name__ == "__main__":
    main()
