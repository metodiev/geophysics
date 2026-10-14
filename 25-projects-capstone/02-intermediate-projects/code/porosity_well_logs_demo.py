#!/usr/bin/env python3
"""Intermediate project 5: porosity from well logs, with the uncertainty and the
systematic bias that a wrong matrix assumption produces.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python porosity_well_logs_demo.py

Everything here is SYNTHETIC.  The log values are drawn from chosen distributions
with chosen uncertainties; no well, no log and no core measurement is used.

Sections
--------
1. Two porosity estimators from two logs, and their random uncertainties.
2. Combining the two estimates by inverse-variance weighting.
3. The systematic error from a wrong matrix density.
4. A reconciled porosity with a stated budget.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_SAMPLES = 10
DEPTH_TOP = 2000.0         # m
DEPTH_STEP = 1.0           # m

RHO_MA = 2.65              # sandstone matrix density, g/cm^3
RHO_MA_WRONG = 2.71        # limestone matrix used by mistake
RHO_F = 1.00               # fluid density, g/cm^3
DT_MA = 55.5               # sandstone matrix transit time, microseconds/ft
DT_MA_LIME = 47.5          # limestone matrix transit time, microseconds/ft
DT_F = 189.0               # fluid transit time, microseconds/ft

SIGMA_RHO = 0.02           # density-log uncertainty, g/cm^3
SIGMA_DT = 2.0             # sonic-log uncertainty, microseconds/ft


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    depth = DEPTH_TOP + DEPTH_STEP * np.arange(N_SAMPLES)
    rho_b = 2.32 + SIGMA_RHO * RNG.standard_normal(N_SAMPLES)
    dt = 78.0 + SIGMA_DT * RNG.standard_normal(N_SAMPLES)

    section("1. Two estimators, two logs")
    print(f"SYNTHETIC logs: {N_SAMPLES} samples from {depth[0]:.0f} to "
          f"{depth[-1]:.0f} m")
    print(f"  density log: {rho_b.mean():.4f} +/- {rho_b.std(ddof=1):.4f} g/cm^3 "
          f"(log uncertainty {SIGMA_RHO:.2f})")
    print(f"  sonic log:   {dt.mean():.4f} +/- {dt.std(ddof=1):.4f} "
          f"microseconds/ft (log uncertainty {SIGMA_DT:.1f})")
    phi_d = (RHO_MA - rho_b) / (RHO_MA - RHO_F)
    phi_s = (dt - DT_MA) / (DT_F - DT_MA)
    print(f"  phi from density  = (rho_ma - rho_b)/(rho_ma - rho_f), "
          f"rho_ma = {RHO_MA:.2f}, rho_f = {RHO_F:.2f}")
    print(f"    mean {phi_d.mean() * 100:.3f} p.u., sample sd "
          f"{phi_d.std(ddof=1) * 100:.3f} p.u., SEM "
          f"{phi_d.std(ddof=1) / np.sqrt(N_SAMPLES) * 100:.3f} p.u.")
    print(f"  phi from sonic (Wyllie) = (dt - dt_ma)/(dt_f - dt_ma), "
          f"dt_ma = {DT_MA:.1f}, dt_f = {DT_F:.1f}")
    print(f"    mean {phi_s.mean() * 100:.3f} p.u., sample sd "
          f"{phi_s.std(ddof=1) * 100:.3f} p.u., SEM "
          f"{phi_s.std(ddof=1) / np.sqrt(N_SAMPLES) * 100:.3f} p.u.")

    section("2. Combining by inverse-variance weighting")
    sigma_phi_d = SIGMA_RHO / (RHO_MA - RHO_F)
    sigma_phi_s = SIGMA_DT / (DT_F - DT_MA)
    sem_d = sigma_phi_d / np.sqrt(N_SAMPLES)
    sem_s = sigma_phi_s / np.sqrt(N_SAMPLES)
    w_d, w_s = 1.0 / sem_d ** 2, 1.0 / sem_s ** 2
    phi_w = (w_d * phi_d.mean() + w_s * phi_s.mean()) / (w_d + w_s)
    sigma_w = 1.0 / np.sqrt(w_d + w_s)
    print(f"  per-sample propagated uncertainties:")
    print(f"    sigma(phi_density) = {SIGMA_RHO:.2f}/{RHO_MA - RHO_F:.2f} = "
          f"{sigma_phi_d * 100:.3f} p.u.")
    print(f"    sigma(phi_sonic)   = {SIGMA_DT:.1f}/{DT_F - DT_MA:.1f} = "
          f"{sigma_phi_s * 100:.3f} p.u.")
    print(f"  standard error of each MEAN over {N_SAMPLES} samples:")
    print(f"    {sem_d * 100:.3f} p.u. and {sem_s * 100:.3f} p.u.")
    print(f"  weights: density {w_d / (w_d + w_s) * 100:.1f}%, "
          f"sonic {w_s / (w_d + w_s) * 100:.1f}%")
    print(f"  weighted porosity = {phi_w * 100:.3f} p.u. "
          f"+/- {sigma_w * 100:.3f} p.u. (random only)")
    discrep = abs(phi_d.mean() - phi_s.mean())
    print(f"  the two estimators differ by {discrep * 100:.3f} p.u., "
          f"{discrep / np.sqrt(sem_d ** 2 + sem_s ** 2):.1f} times their")
    print(f"  combined standard error: the difference is SYSTEMATIC, not noise.")

    section("3. The systematic error from a wrong matrix")
    dphi_drho_ma = (rho_b.mean() - RHO_F) / (RHO_MA - RHO_F) ** 2
    shift = (RHO_MA_WRONG - RHO_MA) * dphi_drho_ma
    phi_wrong = (RHO_MA_WRONG - rho_b.mean()) / (RHO_MA_WRONG - RHO_F)
    print(f"  sensitivity dphi/drho_ma = (rho_b - rho_f)/(rho_ma - rho_f)^2 "
          f"= {dphi_drho_ma:.4f} per g/cm^3")
    print(f"  using rho_ma = {RHO_MA_WRONG:.2f} instead of {RHO_MA:.2f} "
          f"shifts porosity by")
    print(f"    +{shift * 100:.3f} p.u. (first order), "
          f"{phi_wrong * 100:.3f} p.u. vs {phi_d.mean() * 100:.3f} p.u. (exact)")
    print(f"  the shift is {abs(shift) / sigma_w:.1f} times the random uncertainty")
    phi_s_lime = (dt.mean() - DT_MA_LIME) / (DT_F - DT_MA_LIME)
    print(f"  sonic with limestone dt_ma = {DT_MA_LIME:.1f}: "
          f"{phi_s_lime * 100:.3f} p.u. vs {phi_s.mean() * 100:.3f} p.u. "
          f"({(phi_s_lime - phi_s.mean()) * 100:+.3f} p.u.)")

    section("4. A reconciled porosity with a stated budget")
    total = np.sqrt(sigma_w ** 2 + shift ** 2)
    print(f"  porosity = {phi_w * 100:.2f} p.u.")
    print(f"    random (log precision) = {sigma_w * 100:.2f} p.u.")
    print(f"    systematic (matrix)    = {abs(shift) * 100:.2f} p.u.")
    print(f"    combined               = {total * 100:.2f} p.u.")
    print(f"  budget: the matrix assumption dominates "
          f"({(shift / total) ** 2 * 100:.0f}% of the combined variance)")
    print("  -> more log passes do not shrink the dominant term; only an")
    print("     independent mineralogy constraint does.")


if __name__ == "__main__":
    main()
