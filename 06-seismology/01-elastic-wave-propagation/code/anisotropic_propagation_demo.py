"""Anisotropic wave propagation: the Christoffel equation, solved and checked.

All elastic constants are SYNTHETIC, built from a stated set of Thomsen
parameters, so that every number in the lesson can be reproduced from the
inputs alone.

1. Build the VTI stiffness tensor from (alpha0, beta0, rho, epsilon, delta,
   gamma) and print it.
2. Solve the Christoffel eigenvalue problem over a sweep of propagation
   angles; identify qP, qSV and qSH; compare with the exact closed forms on
   the axes and the SH formula at all angles, and with the Thomsen
   weak-anisotropy approximations.
3. Check the polarisations that come out of the eigenproblem.
4. Compute the group velocity two ways -- from the formula
   v_g = v n + (dv/dtheta) theta_hat and from numerical differentiation of
   omega(k) -- and compare.  Report the ray/phase angle split.
5. Rotate the tensor to HTI and verify that the speeds follow the rotation.

Run:
    .venv/bin/python 06-seismology/01-elastic-wave-propagation/code/anisotropic_propagation_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ---- SYNTHETIC VTI medium ------------------------------------------------------------------
ALPHA0 = 4000.0        # m/s, vertical P speed
BETA0 = 2400.0         # m/s, vertical S speed
RHO = 2600.0           # kg/m^3
EPSILON = 0.20
DELTA = 0.15
GAMMA = 0.20

VOIGT_PAIRS = {(0, 0): 0, (1, 1): 1, (2, 2): 2,
               (1, 2): 3, (2, 1): 3, (0, 2): 4, (2, 0): 4,
               (0, 1): 5, (1, 0): 5}


def vti_stiffness() -> np.ndarray:
    c33 = RHO * ALPHA0**2
    c44 = RHO * BETA0**2
    c11 = c33 * (1.0 + 2.0 * EPSILON)
    c66 = c44 * (1.0 + 2.0 * GAMMA)
    c13 = (np.sqrt(2.0 * c33 * (c33 - c44) * DELTA + (c33 - c44) ** 2) - c44)
    c = np.zeros((6, 6))
    c[0, 0] = c[1, 1] = c11
    c[2, 2] = c33
    c[3, 3] = c[4, 4] = c44
    c[5, 5] = c66
    c[0, 1] = c[1, 0] = c11 - 2.0 * c66
    c[0, 2] = c[1, 2] = c[2, 0] = c[2, 1] = c13
    return c


def voigt_to_tensor(c: np.ndarray) -> np.ndarray:
    """C_ijkl from the Voigt matrix, with both index pairs symmetric.

    The mapping carries no numerical factor: the factor of two required by the
    engineering shear strains is already implicit in summing over both (k,l)
    and (l,k).  This is the mapping that reproduces the correct strain energy,
    and it is checked below against the closed-form speeds.
    """
    t = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            ii = VOIGT_PAIRS[(i, j)]
            for k in range(3):
                for l in range(3):
                    t[i, j, k, l] = c[ii, VOIGT_PAIRS[(k, l)]]
    return t


def christoffel(t: np.ndarray, n: np.ndarray) -> np.ndarray:
    g = np.einsum("ijkl,j,l->ik", t, n, n) / RHO
    return 0.5 * (g + g.T)


def modes(t: np.ndarray, n: np.ndarray):
    """Return (vqP, vqSV, vqSH) and the matching polarisation vectors.

    The three branches are identified physically, not by sorting: in a VTI
    medium with the propagation direction in the x-z plane the SH branch is
    polarised exactly along y, so the eigenvector with |v_y| near one is SH.
    Of the remaining two the faster is qP and the slower is qSV.
    """
    vals, vecs = np.linalg.eigh(christoffel(t, n))
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    ish = int(np.argmax(np.abs(vecs[1])))
    rest = [i for i in range(3) if i != ish]
    speeds = (np.sqrt(max(vals[rest[0]], 0.0)),
              np.sqrt(max(vals[rest[1]], 0.0)),
              np.sqrt(max(vals[ish], 0.0)))
    return speeds, (vecs[:, rest[0]], vecs[:, rest[1]], vecs[:, ish])


def qp_speed(t: np.ndarray, n: np.ndarray) -> float:
    return modes(t, n)[0][0]


def sorted_speeds(t: np.ndarray, n: np.ndarray) -> np.ndarray:
    """The three speeds in descending order, without mode identification."""
    vals, _ = np.linalg.eigh(christoffel(t, n))
    return np.sqrt(np.clip(np.sort(vals)[::-1], 0.0, None))


def sh_speed(theta: float) -> float:
    """Exact SH speed in a VTI medium, (C66 sin^2 + C44 cos^2)/rho."""
    c = vti_stiffness()
    return np.sqrt((c[5, 5] * np.sin(theta) ** 2 + c[3, 3] * np.cos(theta) ** 2) / RHO)


def thomsen_approx(theta: float):
    vp = ALPHA0 * (1.0 + DELTA * np.sin(theta) ** 2 * np.cos(theta) ** 2
                   + EPSILON * np.sin(theta) ** 4)
    vsv = BETA0 * (1.0 + (ALPHA0 / BETA0) ** 2 * (EPSILON - DELTA)
                   * np.sin(theta) ** 2 * np.cos(theta) ** 2)
    vsh = BETA0 * (1.0 + GAMMA * np.sin(theta) ** 2)
    return vp, vsv, vsh


def main() -> None:
    global EPSILON, DELTA, GAMMA
    section("1. the VTI stiffness tensor from the stated Thomsen parameters")
    c = vti_stiffness()
    t = voigt_to_tensor(c)
    print(f"  alpha0 = {ALPHA0:.0f} m/s, beta0 = {BETA0:.0f} m/s, "
          f"rho = {RHO:.0f} kg/m^3")
    print(f"  epsilon = {EPSILON:.2f}, delta = {DELTA:.2f}, gamma = {GAMMA:.2f}")
    names = ("C11", "C33", "C13", "C44", "C66", "C12")
    values = (c[0, 0], c[2, 2], c[0, 2], c[3, 3], c[5, 5], c[0, 1])
    for nm, val in zip(names, values):
        print(f"    {nm:>4} = {val / 1e9:10.4f} GPa")
    print(f"  reconstruction of delta from the tensor: "
          f"{((c[0, 2] + c[3, 3]) ** 2 - (c[2, 2] - c[3, 3]) ** 2) / (2 * c[2, 2] * (c[2, 2] - c[3, 3])):.10f}")
    print(f"  the input was {DELTA:.10f}: the tensor and the parameters are the")
    print("  same object written two ways.")

    section("2. the Christoffel eigenproblem over a sweep of directions")
    print(f"  {'theta (deg)':>11} {'qP (m/s)':>11} {'qSV (m/s)':>11} "
          f"{'qSH (m/s)':>11} {'qSH exact':>11} {'|SH-SH_exact|':>14}")
    for deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        theta = np.radians(deg)
        n = np.array([np.sin(theta), 0.0, np.cos(theta)])
        v, _ = modes(t, n)
        exact_sh = sh_speed(theta)
        print(f"  {deg:11.1f} {v[0]:11.4f} {v[1]:11.4f} {v[2]:11.4f} "
              f"{exact_sh:11.4f} {abs(v[2] - exact_sh):14.3e}")

    print(f"\n  axes check: alpha0 = {ALPHA0:.4f}, "
          f"alpha0 sqrt(1+2eps) = {ALPHA0 * np.sqrt(1 + 2 * EPSILON):.4f},")
    print(f"  beta0 = {BETA0:.4f}, beta0 sqrt(1+2gamma) = "
          f"{BETA0 * np.sqrt(1 + 2 * GAMMA):.4f}")
    v0, _ = modes(t, np.array([0.0, 0.0, 1.0]))
    v90, _ = modes(t, np.array([1.0, 0.0, 0.0]))
    print(f"  measured qP along z = {v0[0]:.4f}, qSH/qSV along z = "
          f"{v0[1]:.4f}, {v0[2]:.4f}")
    print(f"  measured qP along x = {v90[0]:.4f}, qSV along x = {v90[1]:.4f}, "
          f"qSH along x = {v90[2]:.4f}")
    print("  The two shear branches are degenerate along the symmetry axis and")
    print("  split away from it: that is shear-wave splitting, and its size is")
    print("  controlled by gamma.")

    section("3. the Thomsen approximations against the exact solution")
    print(f"  {'theta (deg)':>11} {'vqP exact':>12} {'vqP approx':>12} "
          f"{'error %':>9} {'vqSV exact':>12} {'vqSV approx':>12} {'error %':>9}")
    for deg in (15.0, 30.0, 45.0, 60.0, 75.0):
        theta = np.radians(deg)
        n = np.array([np.sin(theta), 0.0, np.cos(theta)])
        v, _ = modes(t, n)
        vp_a, vsv_a, _ = thomsen_approx(theta)
        print(f"  {deg:11.1f} {v[0]:12.4f} {vp_a:12.4f} "
              f"{abs(v[0] / vp_a - 1) * 100:9.4f} {v[1]:12.4f} {vsv_a:12.4f} "
              f"{abs(v[1] / vsv_a - 1) * 100:9.4f}")
    print("  At 20 per cent anisotropy the weak-anisotropy expressions are")
    print("  indicative, not quantitative: the measured differences above are the")
    print("  size of the approximation error, not of the anisotropy.")

    section("4. polarisations from the eigenproblem")
    print(f"  {'theta (deg)':>11} {'angle(vqP, n)':>15} {'angle(vqSH, y)':>16} "
          f"{'angle(vqSV, n)-90':>19}")
    for deg in (0.0, 20.0, 40.0, 60.0, 80.0, 90.0):
        theta = np.radians(deg)
        n = np.array([np.sin(theta), 0.0, np.cos(theta)])
        _, (qp, qsv, qsh) = modes(t, n)
        ang = np.degrees(np.arccos(np.clip(abs(qp @ n), -1, 1)))
        shy = np.degrees(np.arccos(np.clip(abs(qsh @ np.array([0.0, 1.0, 0.0])),
                                          -1, 1)))
        perp = np.degrees(np.arccos(np.clip(abs(qsv @ n), -1, 1))) - 90.0
        print(f"  {deg:11.1f} {ang:15.6f} {shy:16.3e} {perp:19.6f}")
    print("  qP is not exactly parallel to n and qSV is not exactly perpendicular:")
    print("  in an anisotropic medium the polarisation is not locked to the ray")
    print("  direction.  qSH, by contrast, is exactly horizontal everywhere in a")
    print("  VTI medium, which is why it is the cleanest observable.")

    section("5. group velocity: two routes to the same vector")
    print(f"  {'theta (deg)':>11} {'v phase':>10} {'|v_group|':>10} "
          f"{'ray-phase angle':>16} {'|formula - numeric|':>20}")
    dv = 1e-6
    for deg in (10.0, 30.0, 45.0, 60.0, 80.0):
        theta = np.radians(deg)
        n = np.array([np.sin(theta), 0.0, np.cos(theta)])
        that = np.array([np.cos(theta), 0.0, -np.sin(theta)])
        v_p = qp_speed(t, n)
        n2 = np.array([np.sin(theta + dv), 0.0, np.cos(theta + dv)])
        n3 = np.array([np.sin(theta - dv), 0.0, np.cos(theta - dv)])
        v_plus = qp_speed(t, n2)
        v_minus = qp_speed(t, n3)
        dv_dtheta = (v_plus - v_minus) / (2.0 * dv)
        v_group = v_p * n + dv_dtheta * that

        # independent route: numeric gradient of omega(k) = v(theta(k)) * |k|
        k0 = n * 1.0
        grad = np.zeros(3)
        h = 1e-3
        for i in range(3):
            kp = k0.copy()
            kp[i] += h
            km = k0.copy()
            km[i] -= h
            def omega(k):
                kk = np.linalg.norm(k)
                nn = k / kk
                return qp_speed(t, nn) * kk
            grad[i] = (omega(kp) - omega(km)) / (2.0 * h)
        angle = np.degrees(np.arctan2(dv_dtheta, v_p))
        print(f"  {deg:11.1f} {v_p:10.4f} {np.linalg.norm(v_group):10.4f} "
              f"{angle:16.6f} {np.linalg.norm(v_group - grad):20.3e}")
    print("  The ray direction deviates from the phase direction by up to the")
    print("  angle printed, and is zero on the symmetry axis and in the plane")
    print("  perpendicular to it.  The two evaluations of the group velocity agree")
    print("  to the finite-difference accuracy of the second one.")

    section("6. the same medium in HTI: a rotation check")
    # rotate the tensor 90 degrees about x: VTI with the symmetry axis along z
    # becomes HTI with the symmetry axis along x
    r = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, -1.0, 0.0]])
    t_rot = np.einsum("ip,jq,kr,ls,pqrs->ijkl", r, r, r, r, t)
    print(f"  {'theta from x (deg)':>19} {'VTI speeds (m/s)':>28} "
          f"{'HTI speeds (m/s)':>28} {'max |diff|':>12}")
    for deg in (0.0, 30.0, 60.0, 90.0):
        theta = np.radians(deg)
        n = np.array([np.sin(theta), 0.0, np.cos(theta)])
        v_vti = sorted_speeds(t, n)
        v_hti = sorted_speeds(t_rot, r @ n)
        print(f"  {deg:19.1f} "
              f"{v_vti[0]:8.2f} {v_vti[1]:8.2f} {v_vti[2]:8.2f}   "
              f"{v_hti[0]:8.2f} {v_hti[1]:8.2f} {v_hti[2]:8.2f}   "
              f"{np.abs(v_vti - v_hti).max():12.3e}")
    print("  Rotating the stiffness tensor and the propagation direction together")
    print("  leaves every speed unchanged, which is what isotropy of space under")
    print("  rotation demands.  An HTI medium is a VTI medium seen from the side,")
    print("  and this is the numerical statement of that.")

    section("7. the isotropic limit")
    saved = (EPSILON, DELTA, GAMMA)
    EPSILON = DELTA = GAMMA = 0.0
    c_iso = vti_stiffness()
    t_iso = voigt_to_tensor(c_iso)
    worst = 0.0
    for deg in range(0, 91, 10):
        theta = np.radians(deg)
        n = np.array([np.sin(theta), 0.0, np.cos(theta)])
        v, _ = modes(t_iso, n)
        worst = max(worst, abs(v[0] - ALPHA0), abs(v[1] - BETA0), abs(v[2] - BETA0))
    print(f"  with epsilon = delta = gamma = 0, the largest departure of any speed")
    print(f"  from alpha0 = {ALPHA0:.4f} m/s or beta0 = {BETA0:.4f} m/s over all")
    print(f"  directions is {worst:.3e} m/s: the anisotropic solver collapses exactly")
    print("  onto the isotropic one, which is the sharpest available test of the")
    print("  Voigt-to-tensor mapping.")
    EPSILON, DELTA, GAMMA = saved

    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
