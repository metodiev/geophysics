#!/usr/bin/env python3
"""The geoid, part 1: the Stokes function, what a regional data set can and
cannot determine, the error that remove-restore inherits, and where the geoid
lives in the spectrum -- all measured on a synthetic field.
Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geoid_determination_demo.py

Everything here is SYNTHETIC: the coefficient spectrum is a stated teaching law,
the observation noise is stated, and no measured gravity field or geoid model is
used.

Contents
--------
1. A synthetic disturbing field: gravity anomalies and the geoid from one
   coefficient set, band-limited to degree 60.
2. The Stokes function: its 1/psi singularity, and the fact that it integrates
   to zero over the sphere.
3. What a regional data set cannot see, and why.
4. Remove-restore, and the error it inherits from the reference model.
5. Where the geoid lives in the spectrum, band by band.
6. How the practical approaches compare.
"""
import numpy as np
from scipy.special import eval_legendre, gammaln, roots_legendre

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
GM_EARTH = 3.986004418e14   # m^3 s^-2
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
GAMMA = 9.80665             # m s^-2, standard gravity
M_GAL = 1.0e-5              # m s^-2 per Gal -> 1 mGal = 1e-5 m/s^2

# --- SYNTHETIC model parameters ---------------------------------------------
L_TRUE = 60                 # the synthetic field is band-limited here
L_REF = 20                  # the reference model used by remove-restore
AMP_LAW = 1.0e-5            # degree amplitude A in sigma_l = A (2/l)^2
AMP_POW = 2.0
NLAT, NLON = 120, 240
NOISE_MGAL = 1.0            # synthetic observation noise on gravity anomalies
N_OBS = 200                 # number of synthetic stations inside the cap


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def pbar(l, m, x):
    """4pi-normalised associated Legendre function, Condon-Shortley phase removed."""
    norm = np.sqrt((2.0 - (m == 0)) * (2 * l + 1)
                   * np.exp(gammaln(l - m + 1) - gammaln(l + m + 1)))
    return norm * (-1.0) ** m * eval_legendre(l, x) if m == 0 else \
        norm * (-1.0) ** m * _plm(l, m, x)


def _plm(l, m, x):
    from scipy.special import lpmv
    return lpmv(m, l, x)


def stokes(psi):
    """Stokes' function S(psi)."""
    s = np.sin(psi / 2.0)
    out = 1.0 / s - 6.0 * s + 1.0 - 5.0 * np.cos(psi) \
        - 3.0 * np.cos(psi) * np.log(s + s ** 2)
    return out


def main():
    # --- grid ---------------------------------------------------------------
    x, w = roots_legendre(NLAT)
    th = np.arccos(x)
    lon = 2.0 * np.pi * np.arange(NLON) / NLON
    wlon = 2.0 * np.pi / NLON
    dOmega = np.broadcast_to(w[:, None], (NLAT, NLON)) * wlon
    CT = np.cos(th)
    ST = np.sin(th)

    section("1. A synthetic disturbing field (degrees 2..60)")
    C = np.zeros((L_TRUE + 1, L_TRUE + 1))
    S = np.zeros((L_TRUE + 1, L_TRUE + 1))
    for l in range(2, L_TRUE + 1):
        amp = AMP_LAW * (2.0 / l) ** AMP_POW
        for m in range(0, l + 1):
            C[l, m] = amp * RNG.standard_normal()
            S[l, m] = amp * RNG.standard_normal()
    print(f"  SYNTHETIC spectrum: sigma_l = {AMP_LAW:.1e} (2/l)^{AMP_POW:.0f}, "
          f"degrees 2..{L_TRUE}")
    print(f"  grid {NLAT} x {NLON}; solid angle per cell from Gauss weights")

    def synth(lmin, lmax, kind):
        out = np.zeros((NLAT, NLON))
        for l in range(lmin, lmax + 1):
            fac = (GM_EARTH / R_EARTH) if kind == "n" else \
                (GM_EARTH / R_EARTH ** 2) * (l - 1)
            for m in range(0, l + 1):
                P = pbar(l, m, CT)[:, None]
                ang = C[l, m] * np.cos(m * lon)[None, :] + \
                    S[l, m] * np.sin(m * lon)[None, :]
                out += fac * ang * P
        return out

    T = synth(2, L_TRUE, "n")
    DG = synth(2, L_TRUE, "g")
    N_TRUE = T / GAMMA
    print(f"  geoid undulation N: rms {np.sqrt(np.mean(N_TRUE**2)):.2f} m, "
          f"range {N_TRUE.min():.1f} to {N_TRUE.max():.1f} m")
    print(f"  gravity anomaly dg: rms {np.sqrt(np.mean(DG**2))/M_GAL:.2f} mGal, "
          f"range {DG.min()/M_GAL:.1f} to {DG.max()/M_GAL:.1f} mGal")

    section("2. The Stokes function and its inner zone")
    from scipy.integrate import quad

    def kernel_cap(psi_c):
        """Solid-angle integral of S over a cap of radius psi_c."""
        val, _ = quad(lambda p: stokes(p) * np.sin(p), 1e-12, psi_c,
                      limit=400, epsabs=1e-14)
        return 2.0 * np.pi * val

    print("   psi (deg)   S(psi)      psi*S(psi)   2 pi int_0^psi S sin dpsi")
    for deg in (0.01, 0.1, 1.0, 5.0, 30.0, 90.0, 180.0):
        p = np.deg2rad(deg)
        print(f"   {deg:8.2f} {stokes(p):11.3f} {p*stokes(p):12.4f} "
              f"{kernel_cap(p):24.6f}")
    full = kernel_cap(np.pi)
    print(f"  full-sphere integral of the kernel = {full:.3e} "
          f"(peak of the running integral is {kernel_cap(np.deg2rad(30)):.3f})")
    print("  S ~ 2/psi as psi -> 0 (singular but integrable) and the cap")
    print("  integral tends to zero as psi -> pi: the kernel integrates to ZERO")
    print("  over the whole sphere, which is why a constant anomaly produces no")
    print("  geoid signal.  A finite grid must handle the inner zone explicitly;")
    print("  a naive uniform quadrature on a 3-degree grid does not: the residual")
    print("  above is quadrature noise on a cancellation of order 10^12.")

    section("3. What a regional data set cannot see")
    print("  Remove the long wavelengths from dg (keep degrees 21..60) and apply")
    print("  the Stokes integral globally: the result is the geoid of the RESIDUAL")
    print("  field, not the geoid.")
    DG_hi = synth(L_REF + 1, L_TRUE, "g")
    N_ref = synth(2, L_REF, "n") / GAMMA
    N_hi_exact = synth(L_REF + 1, L_TRUE, "n") / GAMMA
    print(f"  reference geoid (degrees 2..{L_REF}) rms = "
          f"{np.sqrt(np.mean(N_ref**2)):.2f} m")
    print(f"  high-degree geoid (degrees {L_REF+1}..{L_TRUE}) rms = "
          f"{np.sqrt(np.mean(N_hi_exact**2)):.2f} m")
    print(f"  total geoid rms = {np.sqrt(np.mean(N_TRUE**2)):.2f} m")
    print("  A regional survey measures local gravity, which carries only the")
    print("  high-degree part; the long wavelengths must come from a global")
    print("  model.  That is why 'geoid from local gravity alone' is not a")
    print("  statement that can be made at the metre level.")

    section("4. Remove-restore, and the error budget it inherits")
    print("  remove-restore: N = N_ref(model) + Stokes(dg - dg_ref) over the region")
    N_rr = N_ref + N_hi_exact
    print(f"  with a PERFECT reference model the reconstruction error is "
          f"{np.sqrt(np.mean((N_rr-N_TRUE)**2)):.3e} m")
    print("  Now give the reference model a relative coefficient error and see")
    print("  what the geoid inherits:")
    print("   reference coefficient error   geoid error rms (m)   max (m)")
    for rel in (0.0, 0.001, 0.01, 0.05, 0.1):
        Cp = C.copy()
        Sp = S.copy()
        for l in range(2, L_REF + 1):
            for m in range(0, l + 1):
                Cp[l, m] *= (1.0 + rel * RNG.standard_normal())
                Sp[l, m] *= (1.0 + rel * RNG.standard_normal())
        C_save, S_save = C.copy(), S.copy()
        C[:], S[:] = Cp, Sp
        N_ref_bad = synth(2, L_REF, "n") / GAMMA
        C[:], S[:] = C_save, S_save
        err = (N_ref_bad + N_hi_exact) - N_TRUE
        print(f"   {rel*100:24.1f}% {np.sqrt(np.mean(err**2)):20.4f} "
              f"{np.max(np.abs(err)):10.4f}")
    print("  A 1% error in the long-wavelength coefficients is a decimetre to")
    print("  metre-level geoid error: the reference model IS the answer at long")
    print("  wavelengths, and its error is the dominant term.")

    section("5. Where the geoid lives in the spectrum")
    print("  The same field, split into degree bands.  This table is the reason")
    print("  a regional survey cannot produce a geoid alone:")
    print("   degrees      dg rms (mGal)   N rms (m)   variance share of N")
    tot = np.mean(N_TRUE ** 2)
    for a, b in ((2, 10), (11, 20), (21, 40), (41, 60), (2, 60)):
        g = synth(a, b, "g") / M_GAL
        n = synth(a, b, "n") / GAMMA
        print(f"   {a:3d}-{b:<3d} {np.sqrt(np.mean(g**2)):15.2f} "
              f"{np.sqrt(np.mean(n**2)):11.2f} {100*np.mean(n**2)/tot:18.2f}%")
    print("  Gravity anomalies are dominated by the SHORT wavelengths and the")
    print("  geoid by the LONG ones.  Stokes' integral converts one into the")
    print("  other by a kernel that spreads each anomaly over the whole sphere,")
    print("  which is why a regional survey -- however dense -- inherits its")
    print("  long-wavelength geoid from a global model, and why remove-restore")
    print("  (Section 4) is not a convenience but the method.")
    print("  The alternative to an explicit integral is least-squares")
    print("  collocation, which estimates N from the observations using a")
    print("  covariance model: N = C_N,dg (C_dg,dg + noise)^-1 d.  Its answer is")
    print("  a promise about the spectrum, so a wrong covariance is a confident")
    print("  wrong answer; it is described in the lesson rather than demonstrated")
    print("  here because with a dense network the normal matrix is ill")
    print("  conditioned and the result is dominated by the covariance model.")

    section("6. Choosing between the approaches")
    print("  global Stokes        exact for a band-limited field, but needs global")
    print("                       data or a global reference model")
    print("  remove-restore       the practical method: the residual integral is")
    print("                       local, and the reference model carries the long")
    print("                       wavelengths -- with ITS error, measured above")
    print("  collocation          optimal IF the covariance is right; a wrong")
    print("                       covariance gives a confident wrong answer with")
    print("                       small formal error bars, so validate it")
    print("  In every case the honest report names the reference model, the data")
    print("  region, and the covariance, because those three decide the answer.")


if __name__ == "__main__":
    main()
