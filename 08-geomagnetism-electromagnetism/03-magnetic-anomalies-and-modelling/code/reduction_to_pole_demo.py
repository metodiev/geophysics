#!/usr/bin/env python3
"""Reduction to the pole: why a magnetic anomaly drifts sideways when the
magnetisation is not vertical, and how a spectral filter moves it back.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reduction_to_pole_demo.py

Everything here is SYNTHETIC.  The dipole, its depth, the field direction and the
noise are chosen teaching values, not measurements from any survey.  Lengths are
handled in metres internally and printed in kilometres.

Contents
--------
1. A synthetic dipole anomaly at an inclined field direction; peak displacement.
2. The Poisson identity (m.h)(f.h)(1/r) = [3(m.rhat)(f.rhat) - m.f]/r^3,
   verified in 3-D by finite differences.
3. The spectral operator O_d(k) = i k_par.d_par + |k| d_z, verified on a tapered
   grid against analytic derivatives and against the analytic anomaly.
4. The RTP filter |k|^2/(O_m O_f): identity at the pole, peak restoration at 45.
5. Peak displacement and white-noise gain versus inclination.
6. A noise test at I = 45 deg and I = 10 deg.
"""

import numpy as np
from scipy.signal.windows import tukey

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi          # H/m
C_DIP = MU0 / (4.0 * np.pi)   # T m / A
KM = 1.0e3
NT = 1.0e-9

DX = 400.0                    # grid spacing, m
NX = 160                      # 160 x 160 -> 64 x 64 km
Z0 = 3000.0                   # dipole depth, m
M_AM = 2.0                    # magnetisation, A/m (SYNTHETIC)
V_M3 = 1.0e9                  # body volume, m^3
MOMENT = M_AM * V_M3          # A m^2


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def dir_vec(incl_deg, decl_deg=0.0):
    i, d = np.radians(incl_deg), np.radians(decl_deg)
    return np.array([np.cos(i) * np.cos(d), np.cos(i) * np.sin(d), np.sin(i)])


def analytic_anomaly_T(x_m, y_m, z0_m, m_hat, f_hat):
    """Total-field anomaly of a point dipole at depth z0 below the origin."""
    r = np.sqrt(x_m ** 2 + y_m ** 2 + z0_m ** 2)
    rhat = np.stack([x_m / r, y_m / r, -z0_m / r], axis=-1)
    m_hat = np.asarray(m_hat, float)
    f_hat = np.asarray(f_hat, float)
    return C_DIP * MOMENT * (3 * (rhat @ m_hat) * (rhat @ f_hat)
                             - np.dot(m_hat, f_hat)) / r ** 3


def main():
    idx = (np.arange(NX) - NX / 2) * DX
    X, Y = np.meshgrid(idx, idx, indexing="ij")
    r_plane = np.sqrt(X ** 2 + Y ** 2 + Z0 ** 2)
    kx = 2 * np.pi * np.fft.fftfreq(NX, d=DX)
    KXG, KYG = np.meshgrid(kx, kx, indexing="ij")
    kmag = np.sqrt(KXG ** 2 + KYG ** 2)
    nz = kmag > 0

    # A separable flat-top (Tukey) window: 1 over the central 50% of the grid.
    w1 = tukey(NX, alpha=0.5)
    W = np.outer(w1, w1)
    flat = (np.abs(X) < 15.0 * KM) & (np.abs(Y) < 15.0 * KM)

    def O_dir(d_hat):
        return 1j * (KXG * d_hat[0] + KYG * d_hat[1]) + kmag * d_hat[2]

    def ft2(f):
        return np.fft.fft2(f) * DX ** 2

    def ift2(F):
        return np.fft.ifft2(F) / DX ** 2

    section("1. A synthetic dipole anomaly at an inclined field direction")
    I_FIELD = 45.0
    f_45 = dir_vec(I_FIELD, 0.0)
    m_45 = dir_vec(I_FIELD, 0.0)
    print(f"SYNTHETIC dipole: M = {M_AM:.2f} A/m, V = {V_M3 / KM ** 3:.2f} km^3, "
          f"moment = {MOMENT:.3e} A m^2, depth {Z0 / KM:.1f} km")
    print(f"field inclination {I_FIELD:.1f} deg, declination 0 deg; "
          f"magnetisation parallel to the field (induced)")
    dT45 = analytic_anomaly_T(X, Y, Z0, m_45, f_45)
    dT90 = analytic_anomaly_T(X, Y, Z0, dir_vec(90.0), dir_vec(90.0))
    ij = np.unravel_index(np.argmax(dT45), dT45.shape)
    ij90 = np.unravel_index(np.argmax(dT90), dT90.shape)
    closed90 = C_DIP * 2 * MOMENT / Z0 ** 3
    print(f"peak dT = {dT45.max() / NT:.3f} nT at (N, E) = "
          f"({idx[ij[0]] / KM:+.1f}, {idx[ij[1]] / KM:+.1f}) km")
    print(f"source at (0, 0, {Z0 / KM:.1f} km): peak displacement = "
          f"{np.hypot(idx[ij[0]], idx[ij[1]]) / KM:.1f} km (grid spacing "
          f"{DX / KM:.1f} km)")
    print(f"same source at the pole (I = 90 deg): peak {dT90.max() / NT:.3f} nT, "
          f"displacement {np.hypot(idx[ij90[0]], idx[ij90[1]]) / KM:.1f} km")
    print(f"  closed form (mu0/4pi) 2 m / z0^3 = {closed90 / NT:.3f} nT")

    section("2. The Poisson identity, verified in 3-D by finite differences")
    print("claim: (m.h)(f.h)(1/r) = [3(m.rhat)(f.rhat) - m.f] / r^3")
    d = dir_vec(60.0)
    for h_km in (0.20, 0.10, 0.05, 0.025):
        h = h_km * KM
        n = int(2.0 * KM / h) + 1          # x, y, z all inside +/-1 km
        ax = (np.arange(n) - (n - 1) / 2) * h
        XX, YY, ZZ = np.meshgrid(ax, ax, ax, indexing="ij")
        rr = np.sqrt(XX ** 2 + YY ** 2 + (ZZ - Z0) ** 2)   # closest approach 2 km
        g = 1.0 / rr
        gx = np.gradient(g, h, axis=0, edge_order=2)
        gy = np.gradient(g, h, axis=1, edge_order=2)
        gz = np.gradient(g, h, axis=2, edge_order=2)
        gxx = np.gradient(gx, h, axis=0, edge_order=2)
        gxy = np.gradient(gx, h, axis=1, edge_order=2)
        gxz = np.gradient(gx, h, axis=2, edge_order=2)
        gyy = np.gradient(gy, h, axis=1, edge_order=2)
        gyz = np.gradient(gy, h, axis=2, edge_order=2)
        gzz = np.gradient(gz, h, axis=2, edge_order=2)
        D = (d[0] * d[0] * gxx + 2 * d[0] * d[1] * gxy + 2 * d[0] * d[2] * gxz
             + d[1] * d[1] * gyy + 2 * d[1] * d[2] * gyz + d[2] * d[2] * gzz)
        rhat = np.stack([XX / rr, YY / rr, (ZZ - Z0) / rr], axis=-1)
        ana = (3 * (rhat @ d) * (rhat @ d) - 1.0) / rr ** 3
        sl = (slice(2, -2),) * 3               # drop the outermost stencil layer
        print(f"   h = {h_km:.3f} km: max |FD - analytic| / max|analytic| = "
              f"{np.max(np.abs(D[sl] - ana[sl])) / np.max(np.abs(ana[sl])):.3e}")
    print("   the source sits 3 km below the sampled volume, so no stencil touches it:")
    print("   the error falls as h^2, as a second-order difference should.")

    section("3. The spectral operator, verified on a tapered grid")
    print("O_d(k) = i (kx dx + ky dy) + |k| dz   (dz is positive: the field decays")
    print("with depth above the source)")
    flat_shell = flat & (r_plane > 1.0 * KM) & (r_plane < 8.0 * KM)
    wg = W * (1.0 / r_plane)
    dz_spec = ift2(O_dir(np.array([0.0, 0.0, 1.0])) * ft2(wg)).real
    dz_ana = Z0 / r_plane ** 3
    err_dz = (np.max(np.abs(dz_spec[flat_shell] - dz_ana[flat_shell]))
              / np.max(np.abs(dz_ana[flat_shell])))
    print(f"   d/dz of the tapered 1/r field: max |error| / max|analytic| over the")
    print(f"   1-8 km shell = {err_dz:.3e}")
    dT_spec = ift2(O_dir(m_45) * O_dir(f_45) * ft2(wg)).real * (C_DIP * MOMENT)
    rel = np.max(np.abs(dT_spec[flat] - dT45[flat])) / np.abs(dT45).max()
    print(f"   composite O_m O_f on 1/r vs the analytic anomaly: max |difference| = "
          f"{rel:.3e} of the peak")
    print("   this one check exercises the Poisson identity, the operator symbol and")
    print("   the units of the whole construction at once.  The residual is dominated")
    print("   by the finite aperture: the 1/r spectrum decays only as 1/|k|, so the")
    print("   grid and the taper, not the operator, set the accuracy.")

    section("4. The RTP filter |k|^2/(O_m O_f)")
    O_m = O_dir(m_45)
    O_f = O_dir(f_45)
    rtp = np.zeros_like(kmag, dtype=complex)
    rtp[nz] = kmag[nz] ** 2 / (O_m[nz] * O_f[nz])
    Om90, Of90 = O_dir(dir_vec(90.0)), O_dir(dir_vec(90.0))
    rtp90 = np.zeros_like(kmag, dtype=complex)
    rtp90[nz] = kmag[nz] ** 2 / (Om90[nz] * Of90[nz])
    print(f"   at the pole the filter is the identity: max |RTP - 1| over k != 0 = "
          f"{np.max(np.abs(rtp90[nz] - 1.0)):.3e}")
    dT_rtp = ift2(rtp * ft2(W * dT45)).real
    ijr = np.unravel_index(np.argmax(dT_rtp), dT_rtp.shape)
    print(f"   at I = 45 deg the data peak sits {np.hypot(idx[ij[0]], idx[ij[1]]) / KM:.1f} km "
          f"from the source, at {dT45.max() / NT:.3f} nT")
    print(f"   after RTP the peak is at {np.hypot(idx[ijr[0]], idx[ijr[1]]) / KM:.2f} km, "
          f"{dT_rtp[ijr] / NT:.3f} nT")
    dev = np.max(np.abs(dT_rtp[flat] - dT90[flat])) / np.abs(dT90).max()
    print(f"   RTP result vs the analytic pole anomaly in the flat region: "
          f"max |difference| = {dev:.3e} of the peak")
    print(f"   peak amplitude error = {(dT_rtp[ijr] - closed90) / closed90 * 100:+.2f}%")

    section("5. Peak displacement and white-noise gain versus inclination")
    print("   I (deg)   peak dT (nT)   displacement (km)   RTP white-noise gain")
    for I in (90.0, 75.0, 60.0, 45.0, 30.0, 20.0, 15.0, 10.0, 5.0):
        fh, mh = dir_vec(I), dir_vec(I)
        filt = np.zeros_like(kmag, dtype=complex)
        filt[nz] = kmag[nz] ** 2 / (O_dir(mh)[nz] * O_dir(fh)[nz])
        dTi = analytic_anomaly_T(X, Y, Z0, mh, fh)
        iji = np.unravel_index(np.argmax(dTi), dTi.shape)
        gain = np.sqrt(np.mean(np.abs(filt[nz]) ** 2))
        print(f"   {I:6.0f}   {dTi.max() / NT:11.3f}   "
              f"{np.hypot(idx[iji[0]], idx[iji[1]]) / KM:17.1f}   {gain:19.2f}")
    print("   the gain is the RMS of the filter on white noise: 1 at the pole and")
    print("   growing without bound as I -> 0, because RTP divides by the direction")
    print("   cosines of the magnetisation and of the field.")

    section("6. A noise test")
    noise_rms = 0.10  # nT, SYNTHETIC
    noisy = dT45 / NT + noise_rms * RNG.standard_normal(dT45.shape)
    for I in (45.0, 10.0):
        fh, mh = dir_vec(I), dir_vec(I)
        filt = np.zeros_like(kmag, dtype=complex)
        filt[nz] = kmag[nz] ** 2 / (O_dir(mh)[nz] * O_dir(fh)[nz])
        out = ift2(filt * ft2(W * noisy * NT)).real / NT
        print(f"   RTP at I = {I:4.1f} deg: peak / background rms in the flat region = "
              f"{np.max(out[flat]) / np.std(out[flat]):7.2f}")
    print(f"   the un-filtered input has peak/noise = {dT45.max() / NT / noise_rms:.1f} at I = 45 deg")

    section("7. Summary for the lesson")
    print(f"  moment {MOMENT:.3e} A m^2, depth {Z0 / KM:.1f} km, grid spacing {DX / KM:.1f} km")
    print(f"  peak at I = 90 deg: {dT90.max() / NT:.3f} nT, displacement "
          f"{np.hypot(idx[ij90[0]], idx[ij90[1]]) / KM:.1f} km")
    print(f"  peak at I = 45 deg: {dT45.max() / NT:.3f} nT, displacement "
          f"{np.hypot(idx[ij[0]], idx[ij[1]]) / KM:.1f} km")
    print(f"  RTP peak displacement {np.hypot(idx[ijr[0]], idx[ijr[1]]) / KM:.2f} km, "
          f"amplitude error {(dT_rtp[ijr] - closed90) / closed90 * 100:+.2f}%")
    print("  RTP is the identity at I = 90 deg and unbounded as I -> 0 deg")


if __name__ == "__main__":
    main()
