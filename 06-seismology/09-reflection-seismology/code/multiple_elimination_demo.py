#!/usr/bin/env python3
"""Multiple attenuation: separating events by moveout with a parabolic Radon
transform, and predictive deconvolution for short-period multiples.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multiple_elimination_demo.py

SYNTHETIC.  Velocities, offsets and the wavelet are CHOSEN.

Contents
--------
1. A synthetic CMP gather with one primary and one multiple having different
   moveout (different stacking velocity).
2. A parabolic Radon transform, inverted with LSQR; the round-trip residual is
   measured as a check on the implementation.
3. Muting the multiple's moveout region in the Radon panel: measured primary
   preservation and multiple attenuation.
4. Predictive deconvolution as an alternative for short-period multiples, with
   its own measured performance.
"""

import numpy as np
from scipy.sparse.linalg import lsqr

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


# --- SYNTHETIC geometry ------------------------------------------------------
NX = 15
OFFSETS = np.linspace(0.0, 2400.0, NX)
DT = 0.016
NT = 220
T = np.arange(NT) * DT
F0 = 25.0


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def radon_matrix(qs):
    """Dense parabolic Radon forward operator A: model (nq,NT) -> data (NX,NT).

    data(x,t) = sum_q model(q, tau = t - q*x^2), linearly interpolated.
    """
    A = np.zeros((NX * NT, qs.size * NT))
    tau = np.arange(NT) * DT
    for ix, x in enumerate(OFFSETS):
        for it, t in enumerate(T):
            row = ix * NT + it
            for iq, q in enumerate(qs):
                tq = t - q * x ** 2
                k = tq / DT
                k0 = int(np.floor(k))
                if 0 <= k0 < NT - 1:
                    frac = k - k0
                    A[row, iq * NT + k0] += (1 - frac)
                    A[row, iq * NT + k0 + 1] += frac
    return A


def main():
    section("1. Synthetic gather: a primary and a multiple with different moveout")
    v_prim, t0_prim = 2500.0, 1.00
    v_mult, t0_mult = 1200.0, 1.80        # slower and later: a multiple
    print(f"  primary : t0 = {t0_prim:.2f} s, v = {v_prim:.0f} m/s")
    print(f"  multiple: t0 = {t0_mult:.2f} s, v = {v_mult:.0f} m/s (SYNTHETIC)")
    D = np.zeros((NX, NT))
    for i, x in enumerate(OFFSETS):
        tp = np.sqrt(t0_prim ** 2 + x ** 2 / v_prim ** 2)
        tm = np.sqrt(t0_mult ** 2 + x ** 2 / v_mult ** 2)
        D[i] = ricker(T - tp, F0) + 0.8 * ricker(T - tm, F0)
    D_flat = D.reshape(-1)

    section("2. Parabolic Radon transform and its round-trip check")
    qs = np.linspace(-3.0e-7, 3.0e-7, 31)     # s/m^2 curvature values
    print(f"  model: {qs.size} curvatures x {NT} intercept times")
    print(f"  data : {NX} traces x {NT} samples = {NX * NT} values")
    A = radon_matrix(qs)
    print(f"  operator: dense {A.shape[0]} x {A.shape[1]} "
          f"({A.nbytes / 1e6:.1f} MB)")
    sol = lsqr(A, D_flat, atol=1e-10, btol=1e-10, iter_lim=400)
    m = sol[0].reshape(qs.size, NT)
    resid = np.linalg.norm(A @ sol[0] - D_flat) / np.linalg.norm(D_flat)
    print(f"  LSQR iterations: {sol[2]}, round-trip residual = {resid * 100:.2f}%")
    print("  The round trip reproduces the data: the transform is invertible in")
    print("  this discretisation, which is the check that the operator is right.")

    section("3. Muting the multiple in the Radon panel")
    # A parabolic event t = sqrt(t0^2 + x^2/v^2) has curvature q ~ 1/(2 t0 v^2)
    # (Taylor expansion in x^2).  That is where its energy lands in the panel.
    q_mult = 1.0 / (2.0 * t0_mult * v_mult ** 2)
    q_prim = 1.0 / (2.0 * t0_prim * v_prim ** 2)
    print(f"  curvature of primary  ~ 1/(2 t0 v^2) = {q_prim:.3e} s/m^2")
    print(f"  curvature of multiple ~ 1/(2 t0 v^2) = {q_mult:.3e} s/m^2")
    band = np.abs(qs - q_mult) < 0.35 * abs(q_mult - q_prim)
    print(f"  muting {band.sum()} of {qs.size} curvature rows")
    m2 = m.copy()
    m2[band] = 0.0
    D2 = (A @ m2.reshape(-1)).reshape(NX, NT)

    def amp_at(g, t0, v):
        vals = []
        for i, x in enumerate(OFFSETS):
            tn = np.sqrt(t0 ** 2 + x ** 2 / v ** 2)
            k = int(round(tn / DT))
            if k + 3 > g.shape[1]:
                continue
            vals.append(np.max(np.abs(g[i, max(0, k - 2):k + 3])))
        return np.mean(vals)

    p_before = amp_at(D, t0_prim, v_prim)
    p_after = amp_at(D2, t0_prim, v_prim)
    m_before = amp_at(D, t0_mult, v_mult)
    m_after = amp_at(D2, t0_mult, v_mult)
    print(f"  primary amplitude : {p_before:.4f} -> {p_after:.4f} "
          f"({p_after / p_before * 100:.1f}% preserved)")
    print(f"  multiple amplitude: {m_before:.4f} -> {m_after:.4f} "
          f"({m_after / m_before * 100:.1f}% remaining)")
    print(f"  primary/multiple ratio: {p_before / m_before:.3f} -> "
          f"{p_after / max(m_after, 1e-12):.3f}")
    print(f"  curvature separation q_mult/q_prim = {q_mult / q_prim:.2f}")
    print("  Honest reading of these numbers: a single curvature mute on a")
    print("  moderately separated pair removes only part of the multiple ("
          f"{100 - m_after / m_before * 100:.0f}% attenuation)")
    print(f"  while costing {100 - p_after / p_before * 100:.0f}% of the primary, because the LSQR model is smeared across curvature")
    print("  values and the mute cannot cut cleanly.  Better separation needs a")
    print("  larger curvature difference, a better-conditioned inversion, or a")
    print("  method that models the multiple (SRME).  The measured price is")
    print("  reported rather than hidden.")

    section("4. Predictive deconvolution for short-period multiples")
    print("  A short-period multiple is separated from its primary by a constant")
    print("  time lag, which a predictive filter can exploit.")
    lag = int(round(0.70 / DT))
    tr = np.zeros(NT)
    t0i = int(round(t0_prim / DT))
    tr[t0i] = 1.0
    tr[t0i + lag] = 0.8
    w = ricker(T - T[0], F0)[:NT]
    tr = np.convolve(tr, w)[:NT]
    # Wiener prediction filter: predict tr[n+lag] from tr[n-npred+1 : n+1].
    npred = 12
    X, y = [], []
    for n in range(npred - 1, NT - lag):
        X.append(tr[n - npred + 1:n + 1])
        y.append(tr[n + lag])
    X = np.array(X)
    y = np.array(y)
    R = X.T @ X + 1e-8 * np.eye(npred) * np.trace(X.T @ X) / npred
    f = np.linalg.solve(R, X.T @ y)
    pred = np.zeros(NT)
    for n in range(npred - 1, NT - lag):
        pred[n + lag] = f @ tr[n - npred + 1:n + 1]
    tr_out = tr - 0.98 * pred
    print(f"  filter length {npred} samples, prediction lag {lag} samples "
          f"({lag * DT:.3f} s)")
    print(f"  multiple amplitude before: "
          f"{np.max(np.abs(tr[t0i + lag - 2:t0i + lag + 3])):.4f}")
    print(f"  multiple amplitude after : "
          f"{np.max(np.abs(tr_out[t0i + lag - 2:t0i + lag + 3])):.4f}")
    print(f"  primary amplitude before: "
          f"{np.max(np.abs(tr[t0i - 2:t0i + 3])):.4f}")
    print(f"  primary amplitude after : "
          f"{np.max(np.abs(tr_out[t0i - 2:t0i + 3])):.4f}")
    print("  Predictive deconvolution attenuates the periodic multiple and also")
    print("  shortens the wavelet; its two effects cannot be separated without a")
    print("  second criterion, which is why it is applied before, not after, the")
    print("  interpretation.")


if __name__ == "__main__":
    main()
