#!/usr/bin/env python3
"""Lower-mantle heterogeneity: what a damped travel-time inversion actually
recovers, how much of the true amplitude survives, and how much of the answer is
the analyst's choice of regularisation rather than a property of the Earth.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lower_mantle_heterogeneity_demo.py

Everything is SYNTHETIC.  The reference velocity profile, the anomaly model, the
ray geometry and the noise level are all chosen teaching values.  No tomographic
model, catalogue or measured anomaly is used.  "LLSVP" is used only as a label
for a large, low-velocity feature near the base of the mantle.

Contents
--------
1. The setup: reference profile, synthetic anomaly, ray geometry.
2. Forward problem: the travel-time residuals the true model produces.
3. Damped least squares: recovered amplitude versus damping.
4. The trade-off curve (data misfit against model norm).
5. Resolution: the diagonal and the point-spread function.
6. Amplitude recovery as a function of depth.
7. What the recovered anomaly implies for temperature -- and how much of that
   number is the damping.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC problem geometry ---------------------------------------------
Z_TOP, Z_BOT = 670.0, 2891.0        # km, top and bottom of the modelled region
WIDTH = 20000.0                     # km, horizontal extent of the section
NZ, NX = 12, 40                     # 12 depth layers, 40 columns
DZ = (Z_BOT - Z_TOP) / NZ
DX = WIDTH / NX
V_TOP, V_BOT = 10.75, 13.72         # km/s, linear reference P velocity
D_LN_V_DT = -1.2e-5                 # K^-1, chosen sensitivity of ln(vs) to T
NOISE = 0.03                        # s, a chosen picking error


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def v_ref(z_km):
    """Reference P velocity, linear in depth (km/s)."""
    return V_TOP + (V_BOT - V_TOP) * (z_km - Z_TOP) / (Z_BOT - Z_TOP)


def turning_depth_for(p):
    """Depth where 1/v(z) = p: the turning point on the linear profile."""
    return Z_TOP + (1.0 / (p * V_TOP) - 1.0) * (Z_BOT - Z_TOP) / (V_BOT / V_TOP - 1.0)


def build_path(p, x_start=0.0, n=3000):
    """One surface-to-surface ray, translated so it starts at x_start.

    Flat-Earth ray theory: with u = 1/v, the ray satisfies
    dx/dz = p / sqrt(u^2 - p^2) and its path element is dl = u |dz| / sqrt(u^2-p^2).
    The substitution z = z_tp - s^2 removes the inverse-square-root singularity
    at the turning point.  Returns the surfaces of constant weight used to
    accumulate path length into model cells:
        x_loc, z_loc  - one position per path segment (km)
        dl_seg        - the length of each segment (km)
    """
    z_tp = turning_depth_for(p)
    s_max = np.sqrt(z_tp - Z_TOP)
    s = (np.arange(n) + 0.5) * (s_max / n)
    ds = s_max / n
    z_half = z_tp - s ** 2                     # ordered turning point -> surface
    u = 1.0 / v_ref(z_half)
    rad = np.sqrt(np.maximum(u ** 2 - p ** 2, 1e-30))
    step = 2.0 * s * ds
    dx_half = p / rad * step
    dl_half = u / rad * step
    z_all = np.concatenate((z_half[::-1], z_half))          # down, then up
    dx_all = np.concatenate((dx_half[::-1], dx_half))
    dl_all = np.concatenate((dl_half[::-1], dl_half))
    x_edges = np.concatenate(([0.0], np.cumsum(dx_all)))
    return x_edges[:-1] + x_start, z_all, dl_all


def build_operator():
    """G_ij = (path length of ray i inside cell j) / v_j.

    With the model vector m = fractional *slowness* perturbation, the travel-time
    residual is dt = G m exactly to first order (and m = -dv/v for a velocity
    perturbation).  Units: km / (km/s) = s.
    """
    rows = []
    meta = []
    p_shallow = 1.0 / v_ref(Z_TOP + 0.5 * DZ)
    p_deep = 1.0 / v_ref(Z_BOT - 0.5 * DZ)
    for p in np.linspace(p_shallow, p_deep, 12):
        x_probe, _, _ = build_path(p, 0.0, 200)
        span = float(np.max(x_probe) - np.min(x_probe))
        for frac in np.linspace(0.0, 1.0, 10):
            x0 = frac * max(WIDTH - span, 0.0)
            x, z, dl = build_path(p, x0)
            inside = (x >= 0.0) & (x <= WIDTH)
            row = np.zeros(NZ * NX)
            ix = np.clip((x[inside] / DX).astype(int), 0, NX - 1)
            iz = np.clip(((z[inside] - Z_TOP) / DZ).astype(int), 0, NZ - 1)
            np.add.at(row, iz * NX + ix, dl[inside] / v_ref(z[inside]))
            if row.sum() > 0.0:
                rows.append(row)
                meta.append((float(p), float(x0), float(row.sum()),
                             float(turning_depth_for(p))))
    return np.vstack(rows), meta


def true_model():
    """SYNTHETIC fractional-slowness anomalies (positive = slow)."""
    m = np.zeros((NZ, NX))
    zc = Z_TOP + (np.arange(NZ) + 0.5) * DZ
    xc = (np.arange(NX) + 0.5) * DX
    for x0 in (0.30 * WIDTH, 0.72 * WIDTH):
        m += 0.012 * np.exp(-((xc[None, :] - x0) / 2600.0) ** 2
                            - ((zc[:, None] - (Z_BOT - 250.0)) / 420.0) ** 2)
    m += 0.003 * np.exp(-((zc[:, None] - 1600.0) / 700.0) ** 2)
    return m


def solve_damped(G, d, lam):
    """Damped least squares: (G^T G + lambda^2 I) m = G^T d."""
    A = G.T @ G + (lam ** 2) * np.eye(G.shape[1])
    return np.linalg.solve(A, G.T @ d)


def main():
    section("1. SYNTHETIC setup")
    print(f"  modelled region: depth {Z_TOP:.0f}-{Z_BOT:.0f} km, width "
          f"{WIDTH / 1000:.0f} x 10^3 km")
    print(f"  grid: {NZ} depth layers x {NX} columns = {NZ * NX} cells "
          f"({DZ:.1f} km x {DX:.0f} km)")
    print(f"  reference vp: {V_TOP:.2f} km/s at the top to {V_BOT:.2f} km/s at "
          "the bottom (linear in depth)")
    print(f"  sensitivity used later: d(ln vs)/dT = {D_LN_V_DT:.2e} K^-1 "
          "(a chosen value)")
    G, meta = build_operator()
    print(f"  rays: {G.shape[0]}; unknowns: {G.shape[1]}")
    depths = [m[3] for m in meta]
    times = [m[2] for m in meta]
    print(f"  turning depths span {min(depths):.0f} to {max(depths):.0f} km")
    print(f"  reference travel times span {min(times):.1f} to {max(times):.1f} s")
    print(f"  each ray crosses the section once; translations spread the "
          "turning points laterally")

    m_true = true_model().ravel()
    d_clean = G @ m_true
    d = d_clean + RNG.normal(0.0, NOISE, G.shape[0])
    rms_signal = float(np.sqrt(np.mean(d_clean ** 2)))
    print(f"\n  true model: two LLSVP-like bodies at 1.20 % slow near the base")
    print(f"              plus a broad 0.30 % slow anomaly at mid-depth")
    print(f"  data: {G.shape[0]} residuals. rms of the true signal = "
          f"{rms_signal:.3f} s")
    print(f"  added independent noise: sigma = {NOISE:.3f} s, so the noise is "
          f"{100 * NOISE / rms_signal:.2f} % of the signal rms")

    section("2. Forward problem: the residuals the true model produces")
    print("    ray   p (s/km)   turning depth (km)   reference T (s)   residual (s)")
    step = max(1, len(meta) // 8)
    for k in range(0, len(meta), step):
        p, x0, t_ref, z_tp = meta[k]
        print(f"  {k:5d}   {p:8.5f}   {z_tp:17.0f}   {t_ref:15.1f}   "
              f"{d[k]:+13.4f}")
    print("  the residuals are of the order of 1 s on paths that take ~1250 s:")
    print("  a 1 % anomaly produces a signal a thousand times smaller than the")
    print("  travel time itself, which is why the reference model must be known")

    section("3. Damped least squares: recovered amplitude versus damping")
    peak_true = float(np.max(np.abs(m_true)))
    print(f"  true peak anomaly: {peak_true * 100:.3f} % slow")
    print("    lambda   rms misfit (s)   peak recovered (% slow)   peak/true")
    lambdas = (1.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0)
    results = {}
    for lam in lambdas:
        m_est = solve_damped(G, d, lam)
        results[lam] = m_est
        resid = float(np.sqrt(np.mean((G @ m_est - d) ** 2)))
        peak = float(np.max(np.abs(m_est)))
        print(f"  {lam:8.1f}   {resid:15.5f}   {peak * 100:22.3f}   "
              f"{peak / peak_true:9.3f}")
    try:
        solve_damped(G, d, 0.0)
    except np.linalg.LinAlgError:
        print(f"   0.0     SINGULAR: {G.shape[0]} equations cannot determine "
              f"{G.shape[1]} cells")
    print("  the undamped solution does not exist: 120 data cannot determine 480")
    print("  cells, so the normal equations are singular. Damping is not cosmetic.")
    print("  Two separate deficits appear, and they must not be confused:")
    print("    * even at the smallest damping the peak is only "
          f"{np.max(np.abs(results[1.0])) / peak_true * 100:.0f} % of the truth,")
    print("      which is a RESOLUTION deficit -- the rays simply do not sample")
    print("      one cell independently;")
    print("    * growing lambda reduces it further, which is a DAMPING deficit.")
    misfits = {lam: float(np.sqrt(np.mean((G @ results[lam] - d) ** 2)))
               for lam in lambdas}
    lam_discrepancy = min(lambdas, key=lambda l: abs(misfits[l] - NOISE))
    print(f"  discrepancy principle: choose lambda so that the rms misfit matches")
    print(f"  the data noise ({NOISE:.3f} s) -- no better and no worse.  The")
    print(f"  matching lambda is {lam_discrepancy:.1f} (misfit "
          f"{misfits[lam_discrepancy]:.5f} s), giving a peak of "
          f"{np.max(np.abs(results[lam_discrepancy])) * 100:.3f} % "
          f"({np.max(np.abs(results[lam_discrepancy])) / peak_true * 100:.0f} % "
          "of the truth).")

    section("4. The trade-off curve (misfit against model norm)")
    print("    lambda   ||G m - d|| (s)   ||m|| x100 (% slow)   misfit^2")
    for lam in lambdas:
        m_est = results[lam]
        mis = float(np.linalg.norm(G @ m_est - d))
        norm = float(np.linalg.norm(m_est)) * 100.0
        print(f"  {lam:8.1f}   {mis:16.4f}   {norm:18.4f}   {mis ** 2:9.4f}")
    lam_best = lam_discrepancy
    m_est = results[lam_best]
    print(f"  every row answers the same data.  The analyst picks one, and the")
    print(f"  pick is made from the noise level and from prior expectations, not")
    print(f"  from the travel times.  We carry the discrepancy-principle choice")
    print(f"  lambda = {lam_best:.1f} forward.")

    section("5. Resolution: the diagonal and the point-spread function")
    A = G.T @ G + (lam_best ** 2) * np.eye(G.shape[1])
    R = np.linalg.solve(A, G.T @ G)
    diag = np.diag(R).reshape(NZ, NX)
    zc = Z_TOP + (np.arange(NZ) + 0.5) * DZ
    print(f"  resolution matrix diagonal (lambda = {lam_best:.2f}):")
    print("    depth (km)   mean diagonal   min      max")
    for i in range(NZ):
        print(f"  {zc[i]:10.0f}   {diag[i].mean():13.3f}   {diag[i].min():7.3f}"
              f"  {diag[i].max():7.3f}")
    print("  a diagonal of 1 means a cell is resolved independently; 0.05 means")
    print("  95 % of its value is borrowed from other cells.  Nothing here is")
    print("  close to 1, and the deepest layers are the worst: with long, steep")
    print("  paths the geometry provides almost no independent depth information.")
    j_probe = (NZ - 1) * NX + NX // 4
    psf = R[j_probe].reshape(NZ, NX)
    print(f"\n  point-spread function for cell {j_probe} "
          f"(depth {zc[-1]:.0f} km, x = {((j_probe % NX) + 0.5) * DX:.0f} km):")
    print("    depth (km)   max |R|   sum of the row over this layer")
    for i in range(NZ):
        print(f"  {zc[i]:10.0f}   {np.max(np.abs(psf[i])):7.4f}   "
              f"{psf[i].sum():+8.4f}")
    print("  the response is spread over every layer, and the negative lobes are")
    print("  the fingerprint of damping: the inversion trades amplitude between")
    print("  neighbouring cells to keep the model norm small.")

    section("6. Amplitude recovery as a function of depth")
    m_est_2d = m_est.reshape(NZ, NX)
    m_true_2d = m_true.reshape(NZ, NX)
    A_inv = np.linalg.inv(A)
    Cm = (NOISE ** 2) * A_inv @ (G.T @ G) @ A_inv
    noise_rms = np.sqrt(np.diag(Cm)).reshape(NZ, NX)
    m_smeared = (R @ m_true).reshape(NZ, NX)
    print("    depth   true rms   R*m_true rms   recovered rms   ratio   noise rms")
    print("     (km)   (% slow)      (% slow)        (% slow)            (% slow)")
    for i in range(NZ):
        t = float(np.sqrt(np.mean(m_true_2d[i] ** 2))) * 100.0
        s = float(np.sqrt(np.mean(m_smeared[i] ** 2))) * 100.0
        e = float(np.sqrt(np.mean(m_est_2d[i] ** 2))) * 100.0
        n = float(np.sqrt(np.mean(noise_rms[i] ** 2))) * 100.0
        print(f"  {zc[i]:8.0f}   {t:9.4f}   {s:13.4f}   {e:14.4f}   {e / t:6.3f}"
              f"   {n:9.4f}")
    print("  the third column is the noise-free prediction R m_true: it reproduces")
    print("  the recovered rms almost exactly, while the last column (the data")
    print("  noise mapped into the model, sqrt of the diagonal of")
    print("  sigma^2 A^-1 G^T G A^-1) is far smaller.  The amplitude pattern is")
    print("  therefore RESOLUTION, not noise: the inversion smears the strong deep")
    print("  anomalies upward and flattens them, so the shallow layers gain rms")
    print("  and the deep layers lose it.")
    corr = float(np.corrcoef(m_true, m_est)[0, 1])
    print(f"  correlation of the true and recovered models: {corr:.4f}")
    print("  SHAPE is recovered, STRENGTH is not, and the deficit is not uniform:")

    section("7. From recovered anomaly to temperature")
    print(f"  with d(ln vs)/dT = {D_LN_V_DT:.2e} K^-1, an anomaly of x % implies")
    print(f"  dT = x / 100 / 1.2e-5 K, i.e. {1 / 100 / abs(D_LN_V_DT):.0f} K per "
          "1 % of velocity anomaly")
    print("    lambda   peak recovered (% slow)   implied |dT| (K)")
    for lam in lambdas:
        p = float(np.max(np.abs(results[lam]))) * 100.0
        print(f"  {lam:8.1f}   {p:23.3f}   {p / 100.0 / abs(D_LN_V_DT):15.0f}")
    print(f"  the true 1.228 % peak would convert to "
          f"{peak_true * 100 / 100 / abs(D_LN_V_DT):.0f} K,")
    plausible = [lam for lam in lambdas
                 if lam <= 300.0]
    ratio = (np.max(np.abs(results[min(plausible)]))
             / np.max(np.abs(results[max(plausible)])))
    print(f"  and across the defensible damping range (lambda = 1 to 300, where the")
    print(f"  misfit stays within a fraction of a second) the answer varies by a")
    print(f"  factor of {ratio:.1f} -- {np.max(np.abs(results[1.0])) * 100 / 100 / abs(D_LN_V_DT):.0f} K "
          f"down to {np.max(np.abs(results[300.0])) * 100 / 100 / abs(D_LN_V_DT):.0f} K.")
    print("  A temperature quoted from a tomographic anomaly therefore inherits")
    print("  the regularisation as part of its uncertainty, and the regularisation")
    print("  is not a measured quantity.  This is the central caveat of the")
    print("  subject, and it is why tomographic amplitudes are best compared")
    print("  between regions *within one inversion* rather than across studies.")


if __name__ == "__main__":
    main()
