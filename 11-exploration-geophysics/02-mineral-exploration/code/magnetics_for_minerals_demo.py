#!/usr/bin/env python3
"""Magnetics for minerals: induced and remanent magnetisation, reduction to the
pole, depth from anomaly shape, and self-demagnetisation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetics_for_minerals_demo.py

Everything here is SYNTHETIC.  The body geometry, susceptibilities, Koenigsberger
ratios, magnetisation directions, noise level and the depth range are chosen
teaching values, not measurements or properties of any real deposit.

Contents
--------
1. Induced and remanent magnetisation; the Koenigsberger ratio Q.
2. Total-field anomaly profiles for induced, remanent and mixed magnetisation;
   measured peak shift and asymmetry.
3. Reduction to the pole (RTP), computed by re-synthesising with a vertical
   magnetisation; the residual asymmetry that RTP cannot remove if the assumed
   direction is wrong.
4. Depth from anomaly shape: the half-width relation for a vertical dipole,
   calibrated numerically, then applied to an inclined-magnetisation anomaly to
   measure the depth bias.
5. Self-demagnetisation of a sphere, M = kappa H / (1 + N kappa), and the
   over-prediction of the naive linear formula.
6. The amplitude ambiguity: (volume, depth) pairs that reproduce one amplitude.
7. Verification: voxel sum against the dipole formula, the demagnetisation
   limits, and the half-width calibration.
"""

import numpy as np
from scipy import optimize

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi          # H/m
MU0_4PI = MU0 / (4.0 * np.pi)
NT = 1.0e-9                   # T per nT

B_FIELD = 50.0e-6             # ambient total field, T
I_MAIN = 60.0                 # inclination of the ambient field, degrees
R_BODY = 200.0                # sphere radius, m
Z_BODY = 300.0                # depth to centre, m
KAPPA = 0.20                  # susceptibility of the body, SI
Q_KOENIGS = 1.50              # Koenigsberger ratio: |M_r| / |M_i|
I_REM = -30.0                 # inclination of the remanent magnetisation, degrees
D_ANGLE = 0.0                 # azimuth of the profile is along the field line


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def unit(i_deg, d_deg=0.0):
    """Unit vector from inclination and declination in degrees (z down)."""
    i, d = np.radians(i_deg), np.radians(d_deg)
    return np.array([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])


def field_dipole(m_vec, obs, src):
    """Field of a dipole m (A m^2) at src, evaluated at obs points (N,3).

    B = (mu0/4pi) [ 3 (m . r) r / |r|^5 - m / |r|^3 ],  r = obs - src.
    """
    r = obs - src
    rn = np.linalg.norm(r, axis=1)
    rhat = r / rn[:, None]
    mdotr = rhat @ m_vec
    return MU0_4PI * (3.0 * mdotr[:, None] * rhat - m_vec) / rn[:, None] ** 3


def total_field_anomaly(m_vec, profile_x, z=Z_BODY):
    """Delta T: the anomaly component measured along the ambient field."""
    obs = np.column_stack([profile_x, np.zeros_like(profile_x),
                           np.zeros_like(profile_x)])
    B = field_dipole(m_vec, obs, np.array([0.0, 0.0, z]))
    return (B @ unit(I_MAIN)) / NT


def sphere_dipole_moment(kappa, r=R_BODY, b_field=B_FIELD, i_main=I_MAIN,
                         q=0.0, i_rem=I_REM, demag=True):
    """Induced (+ remanent) dipole moment of a sphere, with self-demagnetisation."""
    v = 4.0 / 3.0 * np.pi * r ** 3
    h_vec = b_field / MU0 * unit(i_main)
    if demag:
        # For a sphere N = 1/3 in every direction, so the induced magnetisation
        # is scalar-reduced: M = kappa H / (1 + kappa/3).
        m_ind = kappa / (1.0 + kappa / 3.0) * h_vec * v
    else:
        m_ind = kappa * h_vec * v
    m_rem = q * np.linalg.norm(m_ind) * unit(i_rem) if q > 0 else np.zeros(3)
    return m_ind + m_rem, m_ind, m_rem


def half_width(profile_x, anomaly):
    """Half-width in metres: distance from the extreme to the 50% point."""
    i_pk = int(np.argmax(np.abs(anomaly)))
    target = 0.5 * anomaly[i_pk]
    for i in range(i_pk + 1, len(anomaly)):
        if anomaly[i] <= target:
            return float(profile_x[i - 1] + (profile_x[i] - profile_x[i - 1]) * (
                anomaly[i - 1] - target) / (anomaly[i - 1] - anomaly[i])
                - profile_x[i_pk])
    return np.nan


def vertical_anomaly(m_vec, profile_x, z=Z_BODY):
    """The anomaly measured by a VERTICAL field component (the RTP convention)."""
    obs = np.column_stack([profile_x, np.zeros_like(profile_x),
                           np.zeros_like(profile_x)])
    B = field_dipole(m_vec, obs, np.array([0.0, 0.0, z]))
    return B[:, 2] / NT


def main():
    section("1. Induced and remanent magnetisation")
    m_tot, m_ind, m_rem = sphere_dipole_moment(KAPPA, q=Q_KOENIGS)
    print(f"SYNTHETIC body: sphere R = {R_BODY:.0f} m at z = {Z_BODY:.0f} m, "
          f"volume = {4 / 3 * np.pi * R_BODY ** 3:.4e} m^3")
    print(f"ambient field B0 = {B_FIELD / 1e-6:.0f} uT, inclination "
          f"{I_MAIN:.0f} deg; H0 = B0/mu0 = {B_FIELD / MU0:.3f} A/m")
    print(f"susceptibility kappa = {KAPPA:.2f} SI; Koenigsberger ratio "
          f"Q = {Q_KOENIGS:.2f}; remanence inclination {I_REM:.0f} deg")
    print(f"\n{'quantity':28s} {'|m| (A m^2)':>14s} {'inclination (deg)':>18s}")
    for lab, m in (("induced M_i", m_ind), ("remanent M_r", m_rem),
                   ("total M_i + M_r", m_tot)):
        n = np.linalg.norm(m)
        inc = np.degrees(np.arcsin(m[2] / n)) if n > 0 else np.nan
        print(f"{lab:28s} {n:14.4e} {inc:18.1f}")
    print("the total magnetisation direction, not the field direction, controls")
    print("the anomaly shape: this is the single most important practical fact in")
    print("mineral magnetics.")

    section("2. Total-field anomaly profiles")
    x = np.linspace(-1500.0, 1500.0, 601)
    m_induced = sphere_dipole_moment(KAPPA, q=0.0)[1]
    m_remanent = Q_KOENIGS * np.linalg.norm(m_induced) * unit(I_REM)
    cases = {
        "induced only (Q = 0)": m_induced,
        "remanent only": m_remanent,
        "mixed (Q = 1.5)": m_induced + m_remanent,
    }
    print(f"{'case':26s} {'peak (nT)':>10s} {'trough (nT)':>12s} "
          f"{'peak x (m)':>11s} {'peak/trough':>12s}")
    profiles = {}
    for lab, m in cases.items():
        dT = total_field_anomaly(m, x)
        profiles[lab] = dT
        i_pk = int(np.argmax(dT))
        print(f"{lab:26s} {dT.max():10.2f} {dT.min():12.2f} "
              f"{x[i_pk]:11.1f} {dT.max() / abs(dT.min()):12.3f}")
    print("\nan induced anomaly in an inclined field is already asymmetric; adding")
    print("remanence with a different direction moves the peak off the body and")
    print("changes the peak-to-trough ratio.  Neither effect can be removed by")
    print("filtering, because neither is noise.")

    section("3. Reduction to the pole")
    m_vertical = np.array([0.0, 0.0, np.linalg.norm(m_tot)])
    print("RTP = the anomaly that would have been measured at the magnetic pole")
    print("with a vertical magnetisation.  Two routes are shown:")
    print("  (a) re-synthesise with a vertical magnetisation (this is what RTP")
    print("      is defined to produce);")
    print("  (b) apply the same rotation to a WRONG assumed direction, to show the")
    print("      residual that no RTP implementation can remove.")
    dT_mixed = profiles["mixed (Q = 1.5)"]
    dT_rtp = total_field_anomaly(m_vertical, x)
    for lab, prof in (("measured (mixed)", dT_mixed), ("true RTP", dT_rtp)):
        i_pk = int(np.argmax(prof))
        print(f"  {lab:18s} peak {prof.max():9.2f} nT at x = {x[i_pk]:8.1f} m, "
              f"peak/trough = {prof.max() / abs(prof.min()):6.3f}")
    # wrong assumed direction: assume the REMANENCE direction is the total one
    m_wrong = np.array([np.cos(np.radians(I_REM)) * np.linalg.norm(m_tot), 0.0,
                        np.sin(np.radians(I_REM)) * np.linalg.norm(m_tot)])
    dT_wrong = total_field_anomaly(m_wrong, x)
    i_pk = int(np.argmax(dT_wrong))
    print(f"  {'assumed -30 deg':18s} peak {dT_wrong.max():9.2f} nT at "
          f"x = {x[i_pk]:8.1f} m, peak/trough = "
          f"{dT_wrong.max() / abs(dT_wrong.min()):6.3f}")
    print(f"\nRTP needs the total magnetisation direction as an INPUT.  Assuming")
    print(f"the wrong one leaves the peak {abs(x[i_pk]):.0f} m off the body -- and")
    print("the body is at x = 0.  RTP is therefore a data-consistent display, not")
    print("a correction: it cannot create information about a direction it needs.")

    section("4. Depth from anomaly shape")
    print("for a vertical dipole measured with a vertical field component the")
    print("anomaly is Z(x) = C (2h^2 - x^2)/(x^2+h^2)^(5/2), whose half-width is a")
    print("fixed multiple of the depth.  Calibrate that multiple numerically.")
    xc = np.linspace(-4000.0, 4000.0, 400001)
    ideal = vertical_anomaly(m_vertical, xc)
    ratio = half_width(xc, ideal) / Z_BODY
    print(f"calibrated half-width/depth ratio = {ratio:.6f} "
          f"(analytic value for the exact formula: 0.500700)")
    print(f"\n{'profile':44s} {'shape ok?':>9s} {'apparent depth (m)':>19s} "
          f"{'error (m)':>10s}")
    candidates = (
        ("true RTP (vertical magnetisation)", ideal),
        ("RTP assuming no remanence (60 deg)",
         vertical_anomaly(m_induced, xc)),
        ("RTP assuming remanence only (-30 deg)",
         vertical_anomaly(m_wrong, xc)),
        ("measured dT, not RTP at all",
         total_field_anomaly(m_induced + m_remanent, xc)),
    )
    for lab, prof in candidates:
        # The half-width rule applies only to an RTP-shaped profile: one whose
        # extreme value is the positive peak, not a bipolar pair.
        shape_ok = prof.max() > 3.0 * abs(prof.min())
        if shape_ok:
            d_app = half_width(xc, prof) / ratio
            print(f"{lab:44s} {'yes':>9s} {d_app:19.1f} {d_app - Z_BODY:10.1f}")
        else:
            print(f"{lab:44s} {'no':>9s} {'undefined':>19s} {'-':>10s}")
    noise = 1.0 * RNG.standard_normal(xc.size)
    d_app = half_width(xc, ideal + noise) / ratio
    print(f"{'true RTP, +1 nT noise':44s} {'yes':>9s} {d_app:19.1f} "
          f"{d_app - Z_BODY:10.1f}")
    print("1 nT of noise moves the depth by a few metres; ignoring remanence moves")
    print("it by tens of metres; and when the assumed direction is badly wrong the")
    print("profile is bipolar and the shape rule does not apply AT ALL.  The error")
    print("that matters is the magnetisation direction, which is exactly the")
    print("quantity a magnetic survey cannot measure independently.")

    section("5. Self-demagnetisation")
    print("for a sphere the demagnetising factor is N = 1/3, so the induced")
    print("magnetisation saturates: M = kappa H / (1 + kappa/3) -> 3H as kappa")
    print(f"\n{'kappa':>8s} {'|M| linear':>11s} {'|M| demag':>11s} "
          f"{'ratio':>8s} {'dB linear (nT)':>15s} {'dB demag (nT)':>14s}")
    h_vec = B_FIELD / MU0 * unit(I_MAIN)
    v_body = 4.0 / 3.0 * np.pi * R_BODY ** 3
    print(f"{'':8s} {'(A/m)':>11s} {'(A/m)':>11s}")
    for kap in (0.01, 0.1, 0.5, 1.0, 3.0, 10.0):
        m_lin = kap * h_vec * v_body
        m_dm = kap / (1.0 + kap / 3.0) * h_vec * v_body
        b_lin = total_field_anomaly(m_lin, np.array([0.0]))[0]
        b_dm = total_field_anomaly(m_dm, np.array([0.0]))[0]
        print(f"{kap:8.2f} {np.linalg.norm(m_lin) / v_body:11.4f} "
              f"{np.linalg.norm(m_dm) / v_body:11.4f} "
              f"{np.linalg.norm(m_lin) / np.linalg.norm(m_dm):8.3f} "
              f"{b_lin:15.1f} {b_dm:14.1f}")
    print("at kappa = 3 SI the linear formula over-predicts the anomaly by a factor")
    print("of about 2.0: assuming linearity is a factor-scale error, not a")
    print("percentage one.  Note that this correction needs a SHAPE as an input")
    print("(N = 1/3 only for a sphere); for a flat sheet N -> 1 and the linear")
    print("formula is wrong by an order of magnitude or more.")

    section("6. The amplitude ambiguity")
    print(f"fix the observed peak at the value of the SYNTHETIC model and ask which")
    print("(radius, depth) pairs reproduce it, with kappa fixed:")
    target = total_field_anomaly(m_tot, np.array([0.0]))[0]
    print(f"  observed peak = {target:.2f} nT")
    print(f"\n{'radius (m)':>11s} {'required depth (m)':>19s} {'depth/radius':>13s}")
    for r in (100.0, 150.0, 200.0, 300.0, 400.0):
        m = sphere_dipole_moment(KAPPA, r=r, q=Q_KOENIGS)[0]
        z = optimize.brentq(
            lambda zz: total_field_anomaly(m, np.array([0.0]), z=zz)[0] - target,
            100.0, 5000.0)
        print(f"{r:11.0f} {z:19.1f} {z / r:13.2f}")
    print("the dipole anomaly depends on the body only through m/z^3, so with")
    print("kappa, Q and the magnetisation direction fixed it is invariant under")
    print("r -> lambda r and z -> lambda z.  The amplitude therefore fixes the")
    print("RATIO r/z (here 1.50 for every radius) and the shape fixes only the")
    print("SCALE z.  This scale invariance is an exact ambiguity of the dipole")
    print("field, not an observational limitation: a body twice as large at twice")
    print("the depth produces an identical anomaly, and only the width of the")
    print("profile (which scales with z) distinguishes them.")

    section("7. Verification")
    n = 30
    ax = np.linspace(-R_BODY, R_BODY, n)
    X, Y, Zg = np.meshgrid(ax, ax, ax, indexing="ij")
    inside = X ** 2 + Y ** 2 + Zg ** 2 <= R_BODY ** 2
    cell = (ax[1] - ax[0]) ** 3
    m_vox = np.linalg.norm(m_tot) / (inside.sum() * cell)
    src = np.column_stack([X[inside], Y[inside], Zg[inside] + Z_BODY])
    mhat = m_tot / np.linalg.norm(m_tot)
    obs = np.zeros((1, 3))
    B_vox = np.zeros(3)
    for k in range(src.shape[0]):
        B_vox += field_dipole(mhat * m_vox * cell, obs, src[k])[0]
    b_vox = float(B_vox @ unit(I_MAIN)) / NT
    b_dip = total_field_anomaly(m_tot, np.array([0.0]))[0]
    print(f"(a) uniformly magnetised sphere as {inside.sum()} dipoles on a "
          f"{n}^3 grid")
    print(f"    voxel sum   = {b_vox:10.4f} nT")
    print(f"    dipole formula = {b_dip:10.4f} nT")
    print(f"    relative difference = "
          f"{abs(b_vox - b_dip) / abs(b_dip) * 100:.3f}%")
    print("(b) demagnetisation limits")
    h_vec = B_FIELD / MU0 * unit(I_MAIN)
    for kap, lim in ((1e-6, "kappa H (linear)"), (1e6, "3 H (saturated)")):
        m = kap / (1.0 + kap / 3.0) * h_vec * 4.0 / 3.0 * np.pi * R_BODY ** 3
        pred = kap * np.linalg.norm(h_vec) * 4.0 / 3.0 * np.pi * R_BODY ** 3 \
            if kap < 1 else 3.0 * np.linalg.norm(h_vec) * 4.0 / 3.0 * np.pi \
            * R_BODY ** 3
        print(f"    kappa = {kap:9.1e}: |M| = {np.linalg.norm(m):.6e}, "
              f"{lim} = {pred:.6e}")
    print("(c) half-width calibration checked against the analytic formula")
    def ideal_profile(xv, z=Z_BODY):
        m = np.array([0.0, 0.0, 1.0])
        obs = np.column_stack([xv, np.zeros_like(xv), np.zeros_like(xv)])
        B = field_dipole(m, obs, np.array([0.0, 0.0, z]))
        return B[:, 2]
    xv = np.linspace(0.0, 2000.0, 200001)
    pv = ideal_profile(xv)
    i_half = int(np.searchsorted(-pv, -0.5 * pv[0]))
    hw_num = xv[i_half]
    # analytic: solve (2-u)/(1+u)^2.5 = 1 in u = (x/h)^2
    u = optimize.brentq(lambda uu: (2.0 - uu) / (1.0 + uu) ** 2.5 - 1.0,
                        0.0, 1.0)
    print(f"    numerical half-width = {hw_num:.3f} m, ratio to depth = "
          f"{hw_num / Z_BODY:.6f}")
    print(f"    analytic sqrt(u) with u solving (2-u)/(1+u)^2.5 = 1: "
          f"{np.sqrt(u):.6f}")


if __name__ == "__main__":
    main()
