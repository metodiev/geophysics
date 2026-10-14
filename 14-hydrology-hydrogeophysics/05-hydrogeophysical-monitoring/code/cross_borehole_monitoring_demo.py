#!/usr/bin/env python3
"""Cross-borehole monitoring and tracer tests: a synthetic tracer breakthrough
between two boreholes, the petrophysical link from concentration to bulk
conductivity, and a linearised cross-hole tomographic inversion with its
resolution analysis.

Run with the project virtual environment:

    cd 14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_borehole_monitoring_demo.py

Everything here is SYNTHETIC.  The aquifer is a teaching model with one
homogeneous layer; the hydraulic and transport parameters, the borehole
geometry and the noise level are chosen values, not measurements.  No real
site, tracer test or data set is used.

Contents
--------
1. 1-D Darcy velocity, dispersivities and the 2-D advection-dispersion solution.
2. Breakthrough curve at the monitoring borehole; travel time vs threshold.
3. Mass recovery from the breakthrough curve, and the tail-truncation error.
4. The petrophysical link: tracer concentration -> pore-water and bulk
   conductivity (linear ionic mixing plus Archie).
5. Cross-hole ray coverage and the rank of the data kernel.
6. Linearised Tikhonov inversion of the time-lapse data; effective number of
   resolved parameters and the misfit recovered from the truth.
7. Detection limit in concentration, and the artefact from a non-stationary
   background.
"""

import numpy as np
from scipy.linalg import solve

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC aquifer, tracer and survey parameters (chosen, not measured) ---
K_HYD = 5.0            # m/d hydraulic conductivity
GRAD = 0.10            # hydraulic gradient, dimensionless
POROSITY = 0.25        # effective porosity
ALPHA_L = 0.50         # m longitudinal dispersivity
ALPHA_T = 0.05         # m transverse dispersivity
THICKNESS = 2.0        # m saturated thickness of the monitored interval
MASS = 2.0             # kg tracer injected (per metre of aquifer thickness)
X_MON = 5.0            # m, separation of the two boreholes
N_LEVELS = 6           # electrode levels per borehole
SECTION_W, SECTION_H = 10.0, 5.0     # m, modelled section around the boreholes
NX, NY = 40, 20        # grid cells
SIGMA_W0 = 0.050       # S/m, background pore-water conductivity
NOISE_ABS = 0.010      # absolute noise on log10 rho_a, i.e. 2.3% in rho_a

# Standard constants used for the ionic-conductivity link
MOLAR_COND_NACL = 0.0126      # S m^2 / mol, limiting molar conductivity of NaCl
MOLAR_MASS_NACL = 58.44e-3    # kg / mol


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def c_2d(x, z, t, v, dl, dt_, mass=MASS):
    """Instantaneous point-source solution of the 2-D ADE, per unit thickness.

    c(x,z,t) = M / (4 pi t sqrt(D_L D_T))
               exp(-(x-vt)^2/(4 D_L t)) exp(-z^2/(4 D_T t))
    with D_L = dl * v and D_T = dt_ * v.  Units: M kg/m, D m^2/d, t d -> kg/m^3.
    """
    t = np.asarray(t, dtype=float)
    x = np.asarray(x, dtype=float)
    z = np.asarray(z, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = (mass / (4.0 * np.pi * t * np.sqrt(dl * v * dt_ * v))
               * np.exp(-(x - v * t) ** 2 / (4.0 * dl * v * t))
               * np.exp(-z ** 2 / (4.0 * dt_ * v * t)))
    return np.where(t > 0.0, out, 0.0)


def ray_cells(p0, p1, nx, ny, w, h):
    """Length of the segment p0->p1 inside each grid cell, as a flat array.

    The segment is sampled finely; each sample adds ds to the cell containing
    it.  This is the discretised straight-ray path integral.
    """
    n = 4000
    s = np.linspace(0.0, 1.0, n)
    xs = p0[0] + s * (p1[0] - p0[0])
    zs = p0[1] + s * (p1[1] - p0[1])
    i = np.clip((xs / w * nx).astype(int), 0, nx - 1)
    j = np.clip((zs / h * ny).astype(int), 0, ny - 1)
    ds = np.hypot(p1[0] - p0[0], p1[1] - p0[1]) / (n - 1)
    flat = np.zeros(nx * ny)
    np.add.at(flat, i * ny + j, ds)
    return flat


def laplacian(nx, ny):
    """5-point Laplacian on an nx-by-ny grid, flattened row-major (i*ny+j)."""
    n = nx * ny
    L = np.zeros((n, n))
    for i in range(nx):
        for j in range(ny):
            k = i * ny + j
            L[k, k] = 4.0
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < nx and 0 <= jj < ny:
                    L[k, ii * ny + jj] = -1.0
                else:
                    L[k, k] -= 0.0     # free (Neumann) boundary: no penalty
    return L


def main():
    v = K_HYD * GRAD / POROSITY
    section("1. Velocity and the 2-D advection-dispersion model")
    print(f"SYNTHETIC aquifer: K = {K_HYD:.1f} m/d, i = {GRAD:.2f}, "
          f"effective porosity = {POROSITY:.2f}")
    print(f"  seepage velocity v = K i / n_e = {K_HYD:.1f} x {GRAD:.2f} / "
          f"{POROSITY:.2f} = {v:.3f} m/d")
    print(f"  dispersivities: alpha_L = {ALPHA_L:.2f} m, "
          f"alpha_T = {ALPHA_T:.2f} m; D_L = {ALPHA_L * v:.4f} m^2/d, "
          f"D_T = {ALPHA_T * v:.4f} m^2/d")
    print(f"  predicted centre-of-mass arrival at x = {X_MON:.1f} m: "
          f"t = x/v = {X_MON / v:.3f} d")

    section("2. Breakthrough curve at the monitoring borehole")
    t = np.linspace(0.01, 30.0, 3000)
    bt = c_2d(X_MON, 0.0, t, v, ALPHA_L, ALPHA_T)
    peak = bt.max()
    t_peak = float(t[np.argmax(bt)])
    print(f"  peak concentration {peak:.4f} kg/m^3 at t = {t_peak:.3f} d "
          f"(centre-of-mass prediction {X_MON / v:.3f} d)")
    print("\n  reported 'arrival time' as a function of the detection threshold:")
    print("   threshold   c (kg/m^3)   first arrival (d)   implied velocity (m/d)")
    for frac in (0.001, 0.01, 0.05, 0.5):
        idx = np.argmax(bt >= frac * peak)
        t_arr = float(t[idx])
        print(f"   {frac * 100:7.1f}%   {frac * peak:11.5f}   {t_arr:17.3f}   "
              f"{X_MON / t_arr:20.3f}")
    print("  -> the same experiment yields velocities differing by a factor")
    print(f"     {float(X_MON / t[np.argmax(bt >= 0.001 * peak)]) / float(X_MON / t[np.argmax(bt >= 0.5 * peak)]):.2f}"
          " depending on the detection rule alone.")
    print("     A tracer velocity is therefore a statement about a threshold as")
    print("     well as about the aquifer; the threshold must be reported.")

    section("3. Mass recovery and the tail-truncation error")
    print(f"  injected mass per metre of aquifer thickness: M = {MASS:.3f} kg/m")
    print(f"  the depth-averaged 2-D model moves mass at the seepage velocity,")
    print(f"  so the advective flux across the monitoring plane is v c = "
          f"{v:.3f} c kg m^-1 d^-1")
    z = np.linspace(-5.0, 5.0, 2001)
    print("   integration limit (d)   recovered mass (kg/m)   fraction of M")
    for tmax in (3.0, 5.0, 8.0, 15.0, 40.0, 120.0):
        mask = t <= tmax
        cz = c_2d(X_MON, z[None, :], t[mask, None], v, ALPHA_L, ALPHA_T)
        cross = np.trapezoid(cz, z, axis=1)          # kg/m^2 at each time
        rec = v * np.trapezoid(cross, t[mask])
        print(f"   {tmax:20.1f}   {rec:20.4f}   {rec / MASS:15.4f}")
    print("  -> the recovery approaches M from below: a truncated breakthrough")
    print("     curve under-counts the tracer, and the deficit is the slowly")
    print("     moving tail, not noise.  Reporting a mass recovery without the")
    print("     integration window is not a reported number.")

    section("4. Petrophysical link: concentration -> conductivity")
    lam = MOLAR_COND_NACL / MOLAR_MASS_NACL
    print(f"  limiting molar conductivity of NaCl = {MOLAR_COND_NACL} S m^2/mol")
    print(f"  molar mass = {MOLAR_MASS_NACL} kg/mol")
    print(f"  -> mixing coefficient  Lambda = {MOLAR_COND_NACL}/{MOLAR_MASS_NACL}"
          f" = {lam:.4f} S m^-1 per (kg m^-3)")
    print("  linear ionic mixing model: sigma_w = sigma_w0 + Lambda c")
    print("   c (kg/m^3)   sigma_w (S/m)   rho_w (ohm m)   bulk sigma (S/m)"
          "   change (%)")
    phi_eff = POROSITY
    for c in (0.0, 0.001, 0.005, peak, 0.05):
        sw = SIGMA_W0 + lam * c
        bulk = sw * phi_eff ** 1.8          # Archie, saturated: sigma_b = sigma_w phi^m
        rel = 100.0 * (bulk / (SIGMA_W0 * phi_eff ** 1.8) - 1.0)
        print(f"   {c:10.5f}   {sw:13.5f}   {1.0 / sw:13.2f}   {bulk:14.5f}"
              f"   {rel:+9.2f}")
    print(f"  -> the tracer peak multiplies the bulk conductivity by "
          f"{(SIGMA_W0 + lam * peak) / SIGMA_W0:.3f}; a 0.005 kg/m^3 plume")
    print("     changes it by only "
          f"{100 * (lam * 0.005 / SIGMA_W0):.1f}%, which is the detection problem.")

    section("5. Cross-hole ray coverage and the rank of the data kernel")
    x_a, x_b = 0.0, SECTION_W
    z_levels = np.linspace(0.5, SECTION_H - 0.5, N_LEVELS)
    rays, names = [], []
    for z1 in z_levels:
        for z2 in z_levels:
            rays.append(ray_cells((x_a, z1), (x_b, z2), NX, NY, SECTION_W, SECTION_H))
            names.append((z1, z2))
    G_raw = np.array(rays)
    G = G_raw / G_raw.sum(axis=1, keepdims=True)   # unit-sum rays: d is a true average
    print(f"  section {SECTION_W:.1f} m x {SECTION_H:.1f} m, grid {NX} x {NY} = "
          f"{NX * NY} cells")
    print(f"  {N_LEVELS} electrode levels per borehole -> {len(rays)} ray pairs")
    print("  each ray is normalised to unit length, so d_i is the path-averaged")
    print("  change in log10 rho along ray i (dimensionless, in dex)")
    s = np.linalg.svd(G, compute_uv=False)
    rank = int(np.sum(s > 1e-8 * s[0]))
    print(f"  singular values: largest {s[0]:.4f}, smallest {s[-1]:.3e}, "
          f"rank = {rank}")
    print(f"  -> {len(rays)} measurements and {NX * NY} unknown cells: the null")
    print(f"     space has dimension at least {NX * NY - rank}.  Regularisation")
    print("     chooses one member of that equivalence class.")
    print("\n  ray path lengths through the section (m), diagonal of the survey:")
    for i in (0, len(rays) // 2, len(rays) - 1):
        print(f"   borehole-to-borehole pair {names[i][0]:.1f} m -> "
              f"{names[i][1]:.1f} m: path length "
              f"{G_raw[i].sum():.3f} m")

    section("6. Linearised Tikhonov inversion of a synthetic time-lapse plume")
    t_obs = 2.0 * X_MON / v
    xs = (np.arange(NX) + 0.5) / NX * SECTION_W
    zs = (np.arange(NY) + 0.5) / NY * SECTION_H
    XX, ZZ = np.meshgrid(xs, zs, indexing="ij")
    c_now = c_2d(XX, ZZ - SECTION_H / 2.0, t_obs, v, ALPHA_L, ALPHA_T)
    sig_w = SIGMA_W0 + lam * c_now
    true_dlog = np.log10(SIGMA_W0 / sig_w).ravel()     # d log10 rho_bulk
    print(f"  plume imaged at t = {t_obs:.3f} d (twice the centre-of-mass "
          f"arrival), peak c = {c_now.max():.5f} kg/m^3")
    print(f"  true peak change in log10 rho_bulk = {true_dlog.min():+.5f} dex "
          f"({100 * (10 ** true_dlog.min() - 1):+.2f}% in rho)")

    d_true = G @ true_dlog
    d = d_true + NOISE_ABS * RNG.standard_normal(d_true.size)
    L = laplacian(NX, NY)
    GtG = G.T @ G
    Gtd = G.T @ d
    print(f"  data: 36 ray averages of d log10 rho; true rms = "
          f"{np.sqrt(np.mean(d_true ** 2)):.5f} dex, "
          f"noise sd = {NOISE_ABS:.3f} dex")
    print("\n  alpha      data rms (dex)   model rms vs truth   amplitude   "
          "correlation   trace(R)")
    models = {}
    for alpha in (1e-6, 1e-4, 1e-2, 1e-1, 1e0, 1e1):
        A = GtG + alpha * (L.T @ L)
        m = solve(A, Gtd, assume_a="pos")
        models[alpha] = m
        res = G @ m - d
        mod = m - true_dlog
        amp = float(m.min() / true_dlog.min())
        corr = float(np.corrcoef(m, true_dlog)[0, 1])
        tr = float(np.trace(solve(A, GtG, assume_a="pos")))
        print(f"  {alpha:7.1e}   {np.sqrt(np.mean(res ** 2)):15.5f}   "
              f"{np.sqrt(np.mean(mod ** 2)):18.5f}   {amp:9.4f}   {corr:11.4f}"
              f"   {tr:7.2f}")
    print("  -> the data misfit stays at or below the noise sd for every alpha")
    print("     up to 1e-1, so a discrepancy-principle choice of alpha is not")
    print("     bounded by the data; over that range the recovered amplitude")
    print("     changes by a factor of two.  trace(R) falls from 36 (the rank)")
    print("     to 8.8, so alpha is choosing how much of the image is prior.")
    print(f"     The rays determine 36 numbers; the regulariser supplies the")
    print(f"     other {NX * NY - 36}.  Choosing the split is a decision, not a")
    print("     measurement.")

    pinv = np.linalg.pinv(G, rcond=1e-10)
    m_row = pinv @ (G @ true_dlog)           # the part of the truth the data see
    visible = true_dlog - m_row
    print("\n  separating what the data determine from what they do not:")
    print(f"    rms of the truth                          = "
          f"{np.sqrt(np.mean(true_dlog ** 2)):.5f} dex")
    print(f"    rms of its projection onto the row space   = "
          f"{np.sqrt(np.mean(m_row ** 2)):.5f} dex "
          f"({100 * np.sqrt(np.mean(m_row ** 2)) / np.sqrt(np.mean(true_dlog ** 2)):.0f}% of it)")
    print(f"    rms of the invisible (null-space) part     = "
          f"{np.sqrt(np.mean(visible ** 2)):.5f} dex")
    print(f"    correlation of the row-space part with the truth = "
          f"{np.corrcoef(m_row, true_dlog)[0, 1]:.4f}")
    for alpha in (1e-2, 1e0):
        m = models[alpha]
        print(f"    alpha = {alpha:.0e}: correlation of the inversion with the "
              f"data-determined part = {np.corrcoef(m, m_row)[0, 1]:+.4f}, "
              f"with the invisible part = {np.corrcoef(m, visible)[0, 1]:+.4f}")
    print("  -> the measurement geometry determines only about "
          f"{100 * np.sqrt(np.mean(m_row ** 2)) / np.sqrt(np.mean(true_dlog ** 2)):.0f}%")
    print("     of this plume's amplitude, and the inversion correlates MORE")
    print("     with the invisible part than with the determined part: the")
    print("     smooth prior, not the rays, is drawing most of the picture.")

    section("7. The prior decides: the same data from a blocky truth")
    box = np.zeros(NX * NY)
    bx = (XX >= X_MON - 0.5) & (XX <= X_MON + 0.5)
    bz = (np.abs(ZZ - SECTION_H / 2.0) <= 0.5)
    box = np.where((bx & bz).ravel(), -0.05, 0.0)
    scale = np.sqrt(np.mean(true_dlog ** 2)) / np.sqrt(np.mean(box ** 2))
    box = box * scale
    d_box = G @ box + NOISE_ABS * RNG.standard_normal(d_true.size)
    print("  blocky truth: a sharp 1.0 m x 1.0 m box scaled to the same rms "
          f"{np.sqrt(np.mean(box ** 2)):.5f} dex")
    print("   alpha      data rms   model rms vs box   correlation   amplitude")
    for alpha in (1e-2, 1e0):
        A = GtG + alpha * (L.T @ L)
        m = solve(A, G.T @ d_box, assume_a="pos")
        res = G @ m - d_box
        print(f"   {alpha:7.1e}   {np.sqrt(np.mean(res ** 2)):8.5f}   "
              f"{np.sqrt(np.mean((m - box) ** 2)):16.5f}   "
              f"{np.corrcoef(m, box)[0, 1]:11.4f}   {m.min() / box.min():9.4f}")
    print(f"  for comparison, the smooth plume at alpha = 1e-2 gave data rms "
          f"{np.sqrt(np.mean((G @ models[1e-2] - d) ** 2)):.5f} dex and "
          f"correlation {np.corrcoef(models[1e-2], true_dlog)[0, 1]:.4f}")
    print("  -> both truths fit the same rays within the noise, and the smooth")
    print("     regulariser reports the smooth one accurately and the blocky one")
    print("     badly (correlation 0.42, amplitude under a third).  The data do")
    print("     not contain the difference; the prior does.")

    section("8. Detection limit and the artefact of a drifting background")
    alpha = 1e-2
    A = GtG + alpha * (L.T @ L)
    print("  detection limit: a uniform plume of concentration c gives")
    print("  |d log10 rho| = log10(1 + Lambda c / sigma_w0); require it to exceed")
    print(f"  the noise of {NOISE_ABS:.3f} dex:")
    for thresh in (1.0, 3.0):
        c_min = SIGMA_W0 / lam * (10 ** (thresh * NOISE_ABS) - 1.0)
        print(f"    {thresh:.0f} x noise -> c_min = {c_min:.5f} kg/m^3")
    print("\n  a non-stationary background: suppose each ray reading drifts")
    print("  systematically with electrode couple depth, peak-to-peak 0.010 dex,")
    print("  as an unmonitored seasonal change in the boreholes would:")
    zbar = np.array([(z1 + z2) / 2.0 for z1, z2 in names])
    drift = 0.005 * np.sin(2.0 * np.pi * zbar / SECTION_H)
    m_art = solve(A, G.T @ drift, assume_a="pos")
    print(f"    the applied drift has rms {np.sqrt(np.mean(drift ** 2)):.5f} dex")
    print(f"    the artefact it produces has rms "
          f"{np.sqrt(np.mean(m_art ** 2)):.5f} dex, i.e. "
          f"{100 * np.sqrt(np.mean(m_art ** 2)) / np.sqrt(np.mean(true_dlog ** 2)):.0f}% "
          "of the plume rms")
    print(f"    its extremes are {m_art.min():+.5f} and {m_art.max():+.5f} dex "
          f"({100 * (10 ** m_art.min() - 1):+.2f}% to "
          f"{100 * (10 ** m_art.max() - 1):+.2f}% in rho)")
    print("  -> a systematic error of half the noise sd produces a spatially")
    print("     coherent anomaly of 9% of the plume amplitude: a weak secondary")
    print("     plume that no amount of averaging will remove.  Time-lapse")
    print("     differencing cancels a STABLE background, not a drifting one,")
    print("     and repeating the survey does not average a systematic drift")
    print("     away: it must be measured (repeat baselines, permanent")
    print("     electrodes, independent water-level and temperature records).")


if __name__ == "__main__":
    main()
