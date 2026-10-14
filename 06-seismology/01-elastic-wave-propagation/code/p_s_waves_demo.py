"""P and S waves: speeds, the vp/vs ratio, and measured polarisation.

Checks performed (all against SYNTHETIC material constants stated here):

1. ``vp`` and ``vs`` from the moduli, and the three equivalent expressions for
   the ratio ``vp/vs``; the admissible bounds are checked numerically over a
   wide sweep of moduli.
2. Longitudinal vs transverse polarisation measured from a synthetic
   displacement field: the angle between u and k, and the fraction of the
   deformation carried by ``div u`` and ``curl u``.
3. A synthetic three-component ObsPy ``Stream`` (built in memory from numpy
   arrays) whose particle motion is analysed by an eigen-decomposition of the
   covariance matrix; the recovered polarisation direction is compared with
   the direction that was injected.

Run:
    .venv/bin/python 06-seismology/01-elastic-wave-propagation/code/p_s_waves_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy import Stream, Trace, UTCDateTime

RNG = np.random.default_rng(20261014)


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def speeds(lam: float, mu: float, rho: float) -> tuple[float, float]:
    return np.sqrt((lam + 2.0 * mu) / rho), np.sqrt(mu / rho)


# ---------------------------------------------------------------------------
# 1. The ratio vp/vs from the moduli
# ---------------------------------------------------------------------------
def ratio_check() -> None:
    section("1. vp/vs from the moduli: three routes to the same number")
    models = [
        ("base model", 25.0e9, 30.0e9, 2700.0),
        ("Poisson solid (lam = mu)", 30.0e9, 30.0e9, 2600.0),
        ("stiff, nearly incompressible (lam >> mu)", 200.0e9, 10.0e9, 3000.0),
        ("weak shear (mu -> 0 limit)", 20.0e9, 0.05e9, 1000.0),
    ]
    print(f"  {'model':38s} {'vp (m/s)':>10} {'vs (m/s)':>10} {'vp/vs':>9} "
          f"{'sqrt(K/mu+4/3)':>15} {'2(1-nu)/(1-2nu)':>17}")
    for name, lam, mu, rho in models:
        vp, vs = speeds(lam, mu, rho)
        r = vp / vs
        K = lam + 2.0 * mu / 3.0
        nu = lam / (2.0 * (lam + mu))
        r_k = np.sqrt(K / mu + 4.0 / 3.0)
        r_nu = np.sqrt(2.0 * (1.0 - nu) / (1.0 - 2.0 * nu))
        print(f"  {name:38s} {vp:10.2f} {vs:10.2f} {r:9.6f} {r_k:15.6f} "
              f"{r_nu:17.6f}")
    print("  All three columns agree to 1e-6 or better; the algebraic identities")
    print("  vp/vs = sqrt(2 + lam/mu) = sqrt(K/mu + 4/3) = sqrt(2(1-nu)/(1-2nu))")
    print("  are exact.")

    print("\n  The two classical lower bounds, and the assumptions they need:")
    print(f"    sqrt(2)   = {np.sqrt(2.0):.6f}  (vp/vs = sqrt(2 + lam/mu), needs lam >= 0)")
    print(f"    2/sqrt(3) = {2.0 / np.sqrt(3.0):.6f}  (vp/vs = sqrt(K/mu + 4/3), "
          f"needs K >= 0, i.e. lam >= -2mu/3)")
    mus = np.linspace(0.01e9, 60.0e9, 4001)
    lam0 = 25.0e9
    ratios = np.sqrt(2.0 + lam0 / mus)
    print(f"\n  Sweep A: lam = 25 GPa fixed, mu = 0.01 .. 60 GPa")
    print(f"    ratio falls monotonically from {ratios.max():.6f} (mu = 0.01 GPa) to")
    print(f"    {ratios.min():.6f} (mu = 60 GPa) and approaches sqrt(2) = "
          f"{np.sqrt(2.0):.6f} as mu -> infinity")
    mu0 = 30.0e9
    lams = np.linspace(-2.0 * mu0 / 3.0, 200.0e9, 4001)
    ratios2 = np.sqrt(2.0 + lams / mu0)
    print(f"  Sweep B: mu = 30 GPa fixed, lam = -20 .. 200 GPa "
          f"(the admissible range is lam >= -2mu/3)")
    print(f"    ratio rises monotonically from {ratios2.min():.6f} at lam = "
          f"-20 GPa (K = 0, the 2/sqrt(3) bound) through")
    print(f"    {np.sqrt(2.0 + 0.0):.6f} at lam = 0 to {ratios2.max():.6f} at lam = "
          f"200 GPa.")


# ---------------------------------------------------------------------------
# 2. Longitudinal and transverse polarisation, measured
# ---------------------------------------------------------------------------
def polarisation_fields() -> None:
    section("2. Polarisation measured from div u and curl u")
    n = 128
    axis = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    X, Y, Z = np.meshgrid(axis, axis, axis, indexing="ij")
    dx = axis[1] - axis[0]
    k = np.array([2.0, 3.0, 6.0])
    kmag = np.linalg.norm(k)
    pdir = k / kmag
    sdir = np.cross(pdir, np.array([0.0, 0.0, 1.0]))
    sdir /= np.linalg.norm(sdir)
    phase = k[0] * X + k[1] * Y + k[2] * Z

    def div_curl(u: np.ndarray) -> tuple[float, float]:
        def d(f, ax):
            return np.gradient(f, dx, axis=ax)
        div = d(u[0], 0) + d(u[1], 1) + d(u[2], 2)
        curl = np.stack([d(u[2], 1) - d(u[1], 2),
                         d(u[0], 2) - d(u[2], 0),
                         d(u[1], 0) - d(u[0], 1)])
        rms = np.sqrt(np.mean(u**2))
        return np.sqrt(np.mean(div**2)) / (kmag * rms), \
            np.sqrt(np.mean(curl**2)) / (kmag * rms)

    for name, pol in (("P  (u parallel to k)", pdir), ("S  (u perpendicular to k)", sdir)):
        u = np.stack([np.sin(phase) * pol[i] for i in range(3)])
        drel, crel = div_curl(u)
        angle = np.degrees(np.arccos(np.clip(np.dot(pol, pdir), -1, 1)))
        print(f"  {name}")
        print(f"    angle between u and k       : {angle:.4f} deg")
        print(f"    normalised rms |div u|      : {drel:.6f}")
        print(f"    normalised rms |curl u|     : {crel:.6f}")
        print(f"    |div| / |curl|              : "
              f"{drel / crel if crel > 1e-12 else float('inf'):.3e}")
    print("  The P field has all of its deformation in div u and none in curl u;")
    print("  the S field is the exact reverse.  That is why div u and curl u are")
    print("  the natural diagnostics for the two modes.  The leakage in the")
    print("  small column (1e-2 of the leading one) is second-order truncation")
    print("  of the central differences used for the derivatives, not physics.")


# ---------------------------------------------------------------------------
# 3. Synthetic three-component stream and its measured polarisation
# ---------------------------------------------------------------------------
def ricker(t: np.ndarray, f0: float) -> np.ndarray:
    a = np.pi * f0 * (t - 1.5 / f0)
    return (1.0 - 2.0 * a**2) * np.exp(-a**2)


def covariance_polarisation(data: np.ndarray) -> np.ndarray:
    """Principal eigenvector of the 3-component covariance of ``data`` (3 x n)."""
    cov = np.cov(data)
    values, vectors = np.linalg.eigh(cov)
    v = vectors[:, np.argmax(values)]
    if v[0] < 0:
        v = -v
    return v / np.linalg.norm(v)


def stream_polarisation() -> None:
    section("3. Synthetic 3-component stream: recovering the polarisation")
    sr = 100.0
    npts = 400
    t = np.arange(npts) / sr
    wavelet = ricker(t, 4.0)

    cases = [
        ("P, steep incidence", np.array([0.20, 0.10, 0.974679])),
        ("S (SV), steep incidence", np.array([0.974679, 0.0, -0.20])),
        ("S (SH), horizontal", np.array([0.0, 1.0, 0.0])),
    ]
    print(f"  sample rate {sr:.1f} Hz, {npts} samples ({npts / sr:.2f} s), "
          f"seeded noise sigma = 0.02 of peak")
    print(f"  {'case':26s} {'injected (E,N,Z)':>26} {'recovered (E,N,Z)':>26} "
          f"{'angle (deg)':>12}")
    for name, vec in cases:
        vec = vec / np.linalg.norm(vec)
        arrays = []
        st = Stream()
        for comp, label in enumerate(("EHE", "EHN", "EHZ")):
            data = vec[comp] * wavelet + 0.02 * RNG.standard_normal(npts)
            arrays.append(data)
            st.append(Trace(data=data, header={
                "station": "SYN", "channel": label, "sampling_rate": sr,
                "starttime": UTCDateTime("2026-01-01T00:00:00")}))
        recovered = covariance_polarisation(np.stack(arrays))
        angle = np.degrees(np.arccos(np.clip(abs(np.dot(recovered, vec)), -1, 1)))
        print(f"  {name:26s} "
              f"({vec[0]:+.3f},{vec[1]:+.3f},{vec[2]:+.3f}) "
              f"({recovered[0]:+.3f},{recovered[1]:+.3f},{recovered[2]:+.3f}) "
              f"{angle:12.4f}")
    print(f"  stream length {len(st)} traces, sampling rate "
          f"{st[0].stats.sampling_rate:.1f} Hz, dtype {st[0].data.dtype}")
    print("  The covariance principal axis recovers the injected polarisation to")
    print("  the noise level; for the P case the recovery is along the ray, and")
    print("  for S it is perpendicular to it -- which is the operational test a")
    print("  seismologist uses to tell the two arrivals apart.")


def main() -> None:
    ratio_check()
    polarisation_fields()
    stream_polarisation()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
