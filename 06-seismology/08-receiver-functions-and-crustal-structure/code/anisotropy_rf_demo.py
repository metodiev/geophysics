#!/usr/bin/env python3
"""Anisotropy versus dipping structure in receiver functions: what one station
can and cannot separate.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python anisotropy_rf_demo.py

SYNTHETIC.  The anisotropy percentage and layer thickness are chosen teaching
values, not measurements.

Contents
--------
1. Transverse-component RF amplitude versus back-azimuth for a hexagonal
   (anisotropic) layer: the 180-degree (two-lobed) signature.
2. Shear-wave splitting delay from the same layer.
3. A dipping isotropic interface: its transverse signature contains a
   360-degree term.
4. The ambiguity: with a realistic, clustered set of back-azimuths, the two
   models fit the same data almost equally well.  At a single azimuth they are
   indistinguishable.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC anisotropic layer ---------------------------------------------
VS_ISO = 3.60          # km/s isotropic S speed
GAMMA = 0.040          # 4.0% shear anisotropy (fast/slow ratio ~ 1.08)
L_KM = 35.0            # layer thickness, km
PHI_FAST = 30.0        # degrees, fast-axis azimuth


def main():
    print("=" * 70)
    print("1. Anisotropic layer: transverse RF amplitude versus back-azimuth")
    print("=" * 70)
    vs_fast = VS_ISO * (1.0 + GAMMA)
    vs_slow = VS_ISO * (1.0 - GAMMA)
    print(f"SYNTHETIC layer: vs_iso = {VS_ISO:.2f} km/s, anisotropy = "
          f"{GAMMA * 100:.1f}% -> vs_fast = {vs_fast:.3f}, vs_slow = {vs_slow:.3f} km/s")
    print("P-to-S conversion in an anisotropic layer puts signal on the transverse")
    print("component.  For a single hexagonal layer the amplitude follows")
    print("    A(phi) = A0 * sin(2 (phi - phi_fast)).")
    print("   back-azimuth phi (deg)   A(phi)/A0")
    phis = np.arange(0.0, 360.0, 30.0)
    A0 = 0.08
    for phi in phis:
        a = A0 * np.sin(2.0 * np.radians(phi - PHI_FAST))
        print(f"   {phi:20.0f}   {a / A0:+13.4f}")
    print("  Period 180 degrees (two-lobed): zero near the fast and slow axes,")
    print("  maximum at 45 degrees to them.")

    print("\n" + "=" * 70)
    print("2. Shear-wave splitting from the same layer")
    print("=" * 70)
    dt_split = L_KM * (1.0 / vs_slow - 1.0 / vs_fast)
    print(f"  splitting delay = L (1/v_slow - 1/v_fast)")
    print(f"                  = {L_KM:.1f} km * ({1/vs_slow:.6f} - "
          f"{1/vs_fast:.6f}) s/km")
    print(f"                  = {dt_split:.3f} s")
    print(f"  The splitting delay depends on L and the anisotropy TOGETHER:")
    print(f"  doubling the layer and halving the anisotropy gives the same {dt_split:.3f} s")
    print(f"  from L = {2*L_KM:.0f} km and {GAMMA/2*100:.1f}%.")
    dt_split2 = 2 * L_KM * (1.0 / (VS_ISO * (1 - GAMMA / 2)) - 1.0 / (VS_ISO * (1 + GAMMA / 2)))
    print(f"  check: L = {2*L_KM:.0f} km, anisotropy {GAMMA/2*100:.1f}% -> "
          f"{dt_split2:.3f} s")

    print("\n" + "=" * 70)
    print("3. A dipping isotropic interface also produces transverse energy")
    print("=" * 70)
    print("  A Moho dipping by angle alpha produces a transverse RF whose")
    print("  azimuthal dependence contains a 360-degree term, approximately")
    print("    B(phi) = c1 * cos(phi - phi_dip) + c2 * sin(2 (phi - phi_fast)).")
    print("  We choose SYNTHETIC coefficients c1 = 0.06, c2 = 0.03, dip azimuth 110 deg.")
    c1, c2, phi_dip = 0.06, 0.03, 110.0

    def dip_model(phi):
        return (c1 * np.cos(np.radians(phi - phi_dip))
                + c2 * np.sin(2 * np.radians(phi - PHI_FAST)))

    def aniso_model(phi):
        return A0 * np.sin(2 * np.radians(phi - PHI_FAST))

    print("   phi (deg)   dip model   anisotropy model")
    for phi in (0, 45, 90, 135, 180, 225, 270, 315):
        print(f"   {phi:9.0f}   {dip_model(phi):+9.4f}   {aniso_model(phi):+16.4f}")

    print("\n" + "=" * 70)
    print("4. The ambiguity, measured as a design-matrix condition number")
    print("=" * 70)
    print("  Fit  M c = obs  with basis [cos phi, sin phi, cos 2phi, sin 2phi].")
    print("  The cos/sin 2phi columns are the anisotropy terms; the cos/sin phi")
    print("  columns are the dip terms.  If M is ill-conditioned, the fit cannot")
    print("  separate them.")

    def design(phi_deg):
        r = np.radians(phi_deg)
        return np.column_stack([np.cos(r), np.sin(r),
                                np.cos(2 * r), np.sin(2 * r)])

    phi_cluster = np.arange(95.0, 136.0, 10.0)      # 5 clustered azimuths
    phi_full = np.arange(0.0, 360.0, 10.0)          # 36 azimuths
    for label, phis_ in (("clustered 95-135 deg", phi_cluster),
                         ("full 0-350 deg", phi_full)):
        M = design(phis_)
        print(f"   {label:22s}: condition number of M = {np.linalg.cond(M):10.1f}")

    # Monte Carlo: how well is the SPURIOUS dip term determined?
    print("\n  Monte Carlo (200 noise realisations), data from pure anisotropy")
    print("  A(phi) = 0.08 sin(2(phi - 30 deg)); we ask how much 1-phi (dip) term")
    print("  the fit needs, and how unstable that inferred dip is:")
    sigma = 0.012
    for label, phis_ in (("clustered", phi_cluster), ("full", phi_full)):
        M = design(phis_)
        c1s = []
        for _ in range(200):
            obs = A0 * np.sin(2 * np.radians(phis_ - PHI_FAST)) \
                + sigma * RNG.standard_normal(phis_.size)
            c, *_ = np.linalg.lstsq(M, obs, rcond=None)
            c1s.append(np.hypot(c[0], c[1]))        # amplitude of the 1-phi term
        print(f"   {label:10s}: inferred 1-phi amplitude = "
              f"{np.mean(c1s):.4f} +/- {np.std(c1s):.4f}")
    print("  With a clustered azimuth range the 1-phi (dip) amplitude is large and")
    print("  unstable: the data cannot tell a dip from anisotropy.  With full")
    print("  coverage the 1-phi amplitude collapses toward zero (the truth).")

    print("\n  At a SINGLE back-azimuth the two models are exactly degenerate:")
    phi1 = 110.0
    a_aniso = A0 * np.sin(2 * np.radians(phi1 - PHI_FAST))
    a_dip = dip_model(phi1)
    print(f"   phi = {phi1:.0f} deg: anisotropy gives {a_aniso:+.4f}, "
          f"dip model gives {a_dip:+.4f}, ratio = {a_dip / a_aniso:.3f}")
    print("   One number cannot constrain two models.")

    print("\n" + "=" * 70)
    print("5. What a single station can claim")
    print("=" * 70)
    print("  Transverse energy with 180-degree periodicity is CONSISTENT with")
    print("  anisotropy but is not proof of it: a dipping interface, or a")
    print("  combination, can also produce it.  The defensible statements are:")
    print("   - a minimum splitting delay, if the fast axis is constrained;")
    print("   - an apparent fast-axis azimuth, which may be biased by structure;")
    print("   - NOT a unique (thickness, anisotropy, dip) triple from one station.")


if __name__ == "__main__":
    main()
