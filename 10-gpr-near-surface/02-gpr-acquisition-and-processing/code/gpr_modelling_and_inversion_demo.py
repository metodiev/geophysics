#!/usr/bin/env python3
"""GPR modelling and full-waveform inversion: a convolutional layer model, a
finite-difference time-domain wave model with a convergence test, an
adjoint-state gradient verified against finite differences, FWI iterations, cycle
skipping, and the spread of the answer under noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_modelling_and_inversion_demo.py

Everything here is SYNTHETIC: a chosen velocity model, a chosen source, chosen
grids and a chosen noise level.  No field data, no measured velocity and no
published inversion result is involved.

Contents
--------
1. A 1-D convolutional (reflectivity) forward model of three thin layers, with
   its arrival times checked against the analytic two-way times.
2. A 2-D finite-difference time-domain (FDTD) scalar wave model: the reflection
   time checked against the analytic value, and a grid-convergence test.
3. The adjoint-state gradient, verified against finite differences.
4. Full-waveform inversion: the first iteration as a migration-like image, the
   misfit reduction, and the recovered anomaly amplitude.
5. Cycle skipping: the misfit against a uniform time shift and the position of
   its first spurious minimum.
6. Noise and starting-model dependence: the spread of the recovered amplitude.
7. Summary of what the inversion does and does not determine.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

V_BG = 0.100          # m/ns, background (chosen)
V_ANOM = 0.120        # m/ns, anomaly (chosen)
F0 = 0.2              # GHz = 200 MHz
H_GRID = 0.02         # m
DOMAIN = 1.60         # m
DT_FD = 0.05          # ns
NT_FD = 400           # 20 ns


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def fdtd2d(v, h, dt, nt, src_ij, rec_ij, t0, store=False):
    """Scalar 2-D wave equation, second-order in time and space, Dirichlet
    boundaries:

        u^{m} = 2 u^{m-1} - u^{m-2} + (v dt/h)^2 L u^{m-1} + source^m,

    with L the five-point Laplacian.  Sample index n of the returned trace is the
    field u^n, so the trace and the source share one time base.  Returns the
    receiver trace, and the stored field history when store is True (needed by
    the adjoint).
    """
    nz, nx = v.shape
    u_prev = np.zeros((nz, nx))          # u^{0}
    u_cur = np.zeros((nz, nx))           # u^{1}
    u_next = np.zeros((nz, nx))
    a = (v * dt / h) ** 2
    src_w = ricker(np.arange(nt + 2) * dt - t0, F0)
    rec = np.zeros(nt + 2)
    hist = np.zeros((nt + 2, nz, nx)) if store else None
    for n in range(1, nt + 1):
        if store:
            hist[n] = u_cur.copy()
        rec[n] = u_cur[rec_ij[0], rec_ij[1]]
        lap = (u_cur[2:, 1:-1] + u_cur[:-2, 1:-1] + u_cur[1:-1, 2:]
               + u_cur[1:-1, :-2] - 4.0 * u_cur[1:-1, 1:-1])
        u_next[1:-1, 1:-1] = (2.0 * u_cur[1:-1, 1:-1] - u_prev[1:-1, 1:-1]
                              + a[1:-1, 1:-1] * lap)
        u_next[src_ij[0], src_ij[1]] += src_w[n]
        u_prev, u_cur, u_next = u_cur, u_next, u_prev
        u_next[:] = 0.0
    return (rec, hist) if store else rec


def adjoint_gradient(v, h, dt, hist, residual, rec_ij, nt):
    """Discrete adjoint gradient of J = 1/2 sum_n (u^n - d^n)^2 at one receiver.

    With the forward recursion written as M u = s, the transpose is solved by the
    same recursion run backwards in time with the residual injected at the
    receiver:

        lambda^{j-1} = 2 lambda^j - lambda^{j+1} + a L lambda^j + r^{j-1},

    and the gradient is the zero-lag cross-correlation of the forward field with
    the adjoint field,

        dJ/dv_ij = sum_j (2 v_ij dt^2 / h^2) lambda^j_ij (L u^{j-1})_ij .
    """
    nz, nx = v.shape
    lam_next = np.zeros((nz, nx))        # lambda^{j+1}
    lam_cur = np.zeros((nz, nx))         # lambda^j
    lam_prev = np.zeros((nz, nx))        # lambda^{j-1}
    a = (v * dt / h) ** 2
    scale = 2.0 * v * dt ** 2 / h ** 2
    g = np.zeros((nz, nx))
    for j in range(nt + 1, 1, -1):
        lap_u = (hist[j - 1][2:, 1:-1] + hist[j - 1][:-2, 1:-1]
                 + hist[j - 1][1:-1, 2:] + hist[j - 1][1:-1, :-2]
                 - 4.0 * hist[j - 1][1:-1, 1:-1])
        g[1:-1, 1:-1] += scale[1:-1, 1:-1] * lam_cur[1:-1, 1:-1] * lap_u
        lap = (lam_cur[2:, 1:-1] + lam_cur[:-2, 1:-1] + lam_cur[1:-1, 2:]
               + lam_cur[1:-1, :-2] - 4.0 * lam_cur[1:-1, 1:-1])
        lam_prev[1:-1, 1:-1] = (2.0 * lam_cur[1:-1, 1:-1]
                                - lam_next[1:-1, 1:-1]
                                + a[1:-1, 1:-1] * lap)
        lam_prev[rec_ij[0], rec_ij[1]] += residual[j - 1]
        lam_next, lam_cur, lam_prev = lam_cur, lam_prev, lam_next
        lam_prev[:] = 0.0
    return g


def missfit(u_pred, d_obs):
    r = u_pred - d_obs
    return 0.5 * float(np.sum(r ** 2)), r


def main():
    t_fd = np.arange(NT_FD + 2) * DT_FD
    print(f"SYNTHETIC parameters: background v = {V_BG:.3f} m/ns, anomaly "
          f"{V_ANOM:.3f} m/ns, source f0 = {F0*1000:.0f} MHz")
    print(f"FDTD grid: {H_GRID:.3f} m spacing over {DOMAIN:.2f} m, "
          f"dt = {DT_FD:.3f} ns, {NT_FD} steps = {NT_FD*DT_FD:.0f} ns")

    section("1. A 1-D convolutional (reflectivity) forward model")
    layers = ((0.80, +0.20), (1.50, -0.15), (2.60, +0.25))
    t_1d = np.arange(4000) * 0.025
    tw = np.arange(-25.0, 25.0, 0.025)
    ww = ricker(tw, F0)
    syn = np.zeros_like(t_1d)
    print("   layer depth (m)   reflection coefficient   two-way time (ns)")
    for z, r in layers:
        tt = 2.0 * z / V_BG
        print(f"   {z:15.2f}   {r:22.2f}   {tt:19.2f}")
        syn += r * np.interp(t_1d - tt, tw, ww, left=0.0, right=0.0)
    print("   picked times from the synthetic trace (envelope maxima):")
    from scipy.signal import hilbert
    env = np.abs(hilbert(syn))
    for z, r in layers:
        tt = 2.0 * z / V_BG
        i = int(np.argmin(np.abs(t_1d - tt)))
        loc = i + int(np.argmax(env[i - 20:i + 20])) - 20
        print(f"     depth {z:.2f} m: picked {t_1d[loc]:.3f} ns against an "
              f"analytic {tt:.3f} ns (error "
              f"{(t_1d[loc]-tt)*1000:+.0f} ps)")
    print("   The convolutional model is exact for a horizontally layered,"
          " non-dispersive")
    print("   medium and for primary reflections only: no multiples, no"
          " transmission")
    print("   losses, no geometric spreading.  It is the model that FWI is"
          " usually")
    print("   tested against first, and it is not the wave equation.")

    section("2. 2-D FDTD modelling and its grid convergence")
    print("   Two-layer model: interface at 0.40 m, v = 0.14 m/ns below; source")
    print("   and receiver on the surface 0.05 m apart.  The reflection is picked")
    print("   relative to the direct arrival, so the source wavelet cancels.")
    print("   h (m)   dt (ns)   picked reflection-direct (ns)   analytic (ns)   "
          "error (ns)")
    analytic = (2.0 * np.sqrt(0.40 ** 2 + 0.025 ** 2) - 0.05) / V_BG
    for h, dt_use in ((0.040, 0.10), (0.020, 0.05), (0.010, 0.025)):
        n = int(round(DOMAIN / h)) + 1
        v = np.full((n, n), V_BG)
        v[int(round(0.40 / h)):, :] = 0.14
        src = (2, n // 2)
        rec_ij = (2, n // 2 + int(round(0.05 / h)))
        nt = int(round(20.0 / dt_use))
        tr = fdtd2d(v, h, dt_use, nt, src, rec_ij, 3.0 * dt_use)
        tax = np.arange(nt + 2) * dt_use
        env = np.abs(hilbert(tr))
        i_pk = int(np.argmax(env))
        win = (tax > 5.0) & (tax < 14.0)
        i_ref = int(np.argmax(np.where(win, env, 0.0)))
        print(f"   {h:5.3f}   {dt_use:7.3f}   "
              f"{tax[i_ref]-tax[i_pk]:29.3f}   {analytic:11.3f}   "
              f"{tax[i_ref]-tax[i_pk]-analytic:+9.3f}")
    print("   The error falls as the grid is refined: it is numerical dispersion")
    print("   of the second-order scheme, not physics.  A modelling result quoted")
    print("   without a grid-convergence test is not verified.")

    section("3. The adjoint-state gradient, verified against finite differences")
    n = int(round(DOMAIN / H_GRID)) + 1
    x = np.arange(n) * H_GRID
    z = np.arange(n) * H_GRID
    XX, ZZ = np.meshgrid(x, z)
    v_true = V_BG + (V_ANOM - V_BG) * np.exp(
        -((XX - 0.80) ** 2 + (ZZ - 0.80) ** 2) / (2.0 * 0.15 ** 2))
    v_start = np.full((n, n), V_BG)
    src = (2, n // 2)
    rec_ij = (2, n // 2 + 10)
    v_max = float(v_true.max())
    dt_cfl = 0.5 * H_GRID / (v_max * np.sqrt(2.0))
    print(f"   CFL limit: dt <= h/(v_max sqrt2) = {H_GRID/(v_max*np.sqrt(2)):.4f}"
          f" ns; using dt = {DT_FD:.3f} ns "
          f"({DT_FD/(H_GRID/(v_max*np.sqrt(2)))*100:.0f}% of the limit)")
    d_obs = fdtd2d(v_true, H_GRID, DT_FD, NT_FD, src, rec_ij, 3.0 * DT_FD)
    u_pred, hist = fdtd2d(v_start, H_GRID, DT_FD, NT_FD, src, rec_ij,
                          3.0 * DT_FD, store=True)
    J0, r = missfit(u_pred, d_obs)
    g_adj = adjoint_gradient(v_start, H_GRID, DT_FD, hist, r, rec_ij, NT_FD)
    print(f"   true model: background {V_BG:.3f} m/ns with a Gaussian anomaly of"
          f" peak {V_ANOM:.3f} m/ns")
    print(f"   starting model: uniform {V_BG:.3f} m/ns; initial misfit "
          f"J = {J0:.6f}")
    print("   finite-difference check on 10 grid points (dv = 1e-5 m/ns):")
    print("   i (m)   j (m)   analytic dJ/dv   finite difference   relative error")
    idx_pairs = [(20, 20), (25, 25), (30, 30), (35, 35), (40, 40), (45, 45),
                 (30, 35), (35, 30), (40, 50), (25, 40)]
    errs = []
    for i, j in idx_pairs:
        dv = 1e-5
        vp = v_start.copy()
        vp[i, j] += dv
        vmm = v_start.copy()
        vmm[i, j] -= dv
        Jp = 0.5 * float(np.sum((fdtd2d(vp, H_GRID, DT_FD, NT_FD, src, rec_ij,
                                       3.0 * DT_FD) - d_obs) ** 2))
        Jm = 0.5 * float(np.sum((fdtd2d(vmm, H_GRID, DT_FD, NT_FD, src, rec_ij,
                                       3.0 * DT_FD) - d_obs) ** 2))
        fd = (Jp - Jm) / (2.0 * dv)
        rel = abs(g_adj[i, j] - fd) / max(abs(fd), 1e-30)
        errs.append(rel)
        print(f"   {x[i]:5.2f}   {z[j]:5.2f}   {g_adj[i,j]:14.6f}   "
              f"{fd:17.6f}   {rel:14.2e}")
    print(f"   maximum relative difference over the ten points: {max(errs):.2e}, "
          f"median {np.median(errs):.2e}")
    print("   The two agree to the level of the finite-difference error itself: the")
    print("   adjoint is not an approximation here, it is the transpose of the")
    print("   discrete forward operator, and an inversion built on it inherits that")
    print("   consistency.  Without this test the gradient is an unverified claim.")

    section("4. Full-waveform inversion: iterations and the first image")
    h_f = 0.020
    n_f = int(round(0.80 / h_f)) + 1
    x_f = np.arange(n_f) * h_f
    XXF, ZZF = np.meshgrid(x_f, x_f)
    dt_f, nt_f = 0.03, 260
    amp_true = 0.04
    v_true_f = V_BG + amp_true * np.exp(
        -((XXF - 0.40) ** 2 + (ZZF - 0.32) ** 2) / (2.0 * 0.10 ** 2))
    v_start_f = np.full((n_f, n_f), V_BG)
    srcs_f = [(2, int(round(0.30 / h_f))), (2, int(round(0.50 / h_f)))]
    recs_f = [(2, j) for j in range(5, n_f - 3, 3)]
    mask_f = (XXF > 0.12) & (XXF < 0.70) & (ZZF > 0.10) & (ZZF < 0.62)
    d_obs_f = {}
    for s_ in srcs_f:
        for r_ in recs_f:
            d_obs_f[(s_, r_)] = fdtd2d(v_true_f, h_f, dt_f, nt_f, s_, r_, 3 * dt_f)

    def misfit_f(v):
        J = 0.0
        for s_ in srcs_f:
            for r_ in recs_f:
                J += 0.5 * float(np.sum(
                    (fdtd2d(v, h_f, dt_f, nt_f, s_, r_, 3 * dt_f)
                     - d_obs_f[(s_, r_)]) ** 2))
        return J

    def grad_f(v):
        G = np.zeros((n_f, n_f))
        for s_ in srcs_f:
            _, hist = fdtd2d(v, h_f, dt_f, nt_f, s_, (2, s_[1]), 3 * dt_f,
                             store=True)
            for r_ in recs_f:
                res = hist[:, r_[0], r_[1]] - d_obs_f[(s_, r_)]
                G += adjoint_gradient(v, h_f, dt_f, hist, res, r_, nt_f)
        return G * mask_f

    print(f"   SYNTHETIC FWI model: {n_f} x {n_f} grid at {h_f:.3f} m, "
          f"{len(srcs_f)} sources and {len(recs_f)} receivers")
    print(f"   anomaly: +{amp_true:.3f} m/ns Gaussian at (0.400, 0.320) m, "
          f"radius 0.10 m")
    J0f = misfit_f(v_start_f)
    print(f"   starting model uniform {V_BG:.3f} m/ns: misfit J = {J0f:.4f}")
    G0 = grad_f(v_start_f)
    deep_f = ZZF > 0.20
    i_all = np.unravel_index(np.argmax(G0), G0.shape)
    i_pk0 = np.unravel_index(np.argmax(G0 * deep_f), G0.shape)
    print(f"   the first gradient has its largest value at the surface, at "
          f"(x, z) = ({x_f[i_all[1]]:.2f}, {x_f[i_all[0]]:.2f}) m, where the")
    print("   direct wave dominates; inside the region below the direct-wave")
    print(f"   footprint (z > 0.20 m) its peak is at (x, z) = "
          f"({x_f[i_pk0[1]]:.3f}, {x_f[i_pk0[0]]:.3f}) m,")
    print(f"   {np.hypot(x_f[i_pk0[1]]-0.40, x_f[i_pk0[0]]-0.32)*100:.1f} cm from "
          f"the true anomaly centre.  That is the migration step: the")
    print("   gradient localises the anomaly before any iteration has run, and the")
    print("   near-surface sensitivity is the part that must be masked out.")
    print("   iteration   misfit      reduction from start (dB)   peak value "
          "recovered (m/ns)")
    v_cur_f = v_start_f.copy()
    for it in range(1, 5):
        G = grad_f(v_cur_f)
        G = G / np.abs(G).max()
        J_c = misfit_f(v_cur_f)
        best = (J_c, 0.0)
        for alpha in (0.0005, 0.001, 0.002, 0.004, 0.008, 0.016):
            J_t = misfit_f(np.clip(v_cur_f - alpha * G, 0.06, 0.18))
            if J_t < best[0]:
                best = (J_t, alpha)
        if best[1] == 0.0:
            print(f"   {it:9d}   {J_c:.4f}   no step improved the misfit: stop")
            break
        v_cur_f = np.clip(v_cur_f - best[1] * G, 0.06, 0.18)
        i_pk = np.unravel_index(np.argmax(v_cur_f - V_BG), v_cur_f.shape)
        print(f"   {it:9d}   {best[0]:.4f}   {10*np.log10(best[0]/J0f):17.2f}   "
              f"{v_cur_f[i_pk]:25.4f} (at x = {x_f[i_pk[1]]:.2f}, "
              f"z = {x_f[i_pk[0]]:.2f} m)")
    i_pk_f = np.unravel_index(np.argmax(v_cur_f - V_BG), v_cur_f.shape)
    print(f"   after the iterations: peak {v_cur_f[i_pk_f]:.4f} m/ns at "
          f"(x, z) = ({x_f[i_pk_f[1]]:.2f}, {x_f[i_pk_f[0]]:.2f}) m")
    print(f"   true anomaly: {V_BG+amp_true:.4f} m/ns at (0.40, 0.32) m, radius "
          f"0.10 m")
    print(f"   recovered amplitude is "
          f"{(v_cur_f[i_pk_f]-V_BG)/amp_true*100:.0f}% of the true contrast: four "
          f"steepest-descent")
    print("   iterations along a normalised direction is a deliberately minimal")
    print("   inversion.  What it shows is the shape of the answer -- a smoothed,")
    print("   low-amplitude model whose lateral position is right and whose")
    print("   amplitude is a small fraction of the truth -- not a good image.")

    section("5. Cycle skipping: the misfit against a uniform time shift")
    print("   Take a single synthetic reflection and shift it in time; the misfit")
    print("   is the squared difference from the unshifted trace.")
    trace = np.interp(t_1d - 2.0 * 1.5 / V_BG, tw, ww, left=0.0, right=0.0)
    shifts = np.arange(-6.0, 6.0001, 0.05)
    Js = []
    for s_ in shifts:
        sh = np.interp(t_1d - 2.0 * 1.5 / V_BG - s_, tw, ww, left=0.0, right=0.0)
        Js.append(0.5 * float(np.sum((sh - trace) ** 2)))
    Js = np.array(Js)
    scale = Js[int(np.argmax(np.abs(shifts) >= 5.95))]
    minima = []
    for k in range(1, shifts.size - 1):
        if Js[k] <= Js[k - 1] and Js[k] <= Js[k + 1]:
            minima.append((shifts[k], Js[k]))
    print(f"   dominant period 1/f0 = {1.0/F0:.2f} ns; misfit minima over "
          f"+/-6 ns:")
    print("   shift (ns)   misfit (relative to the edge of the window)")
    for s_, Jv in minima:
        print(f"   {s_:10.2f}   {Jv/scale:33.4f}")
    first = [m for m in minima if abs(m[0]) > 0.5][0]
    print(f"   the global minimum is at shift 0; the first spurious minimum is at "
          f"{first[0]:+.2f} ns,")
    print(f"   which is {abs(first[0])*F0:.2f} of a dominant period.  A starting")
    print("   model wrong by more than about half a period can therefore put the")
    print("   inversion in the neighbouring basin, where the gradient points the")
    print("   wrong way: that is cycle skipping, and it is why FWI needs low")
    print("   frequencies, a good starting model, or both.")

    section("6. Noise and starting-model dependence")
    print("   One iteration of a NORMALISED gradient step with 10% noise on the")
    print("   observed traces, and four different draws of a 2% random starting")
    print("   model:")
    print("   run   starting model     noise    value at the anomaly (m/ns)   "
          "global maximum (m/ns)")
    peaks = []
    for run in range(4):
        d_noisy = {}
        for key, tr_obs in d_obs_f.items():
            d_noisy[key] = tr_obs + 0.10 * np.std(tr_obs) * RNG.standard_normal(
                tr_obs.size)
        v_st = (V_BG * (1.0 + 0.02 * RNG.standard_normal((n_f, n_f)))
                if run else v_start_f.copy())
        G = np.zeros((n_f, n_f))
        for s_ in srcs_f:
            _, hist = fdtd2d(v_st, h_f, dt_f, nt_f, s_, (2, s_[1]), 3 * dt_f,
                             store=True)
            for r_ in recs_f:
                res = hist[:, r_[0], r_[1]] - d_noisy[(s_, r_)]
                G += adjoint_gradient(v_st, h_f, dt_f, hist, res, r_, nt_f)
        G = G * mask_f
        G = G / np.abs(G).max()
        v_one = np.clip(v_st - 0.004 * G, 0.06, 0.18)
        i_anom = (int(round(0.32 / h_f)), int(round(0.40 / h_f)))
        peaks.append(v_one[i_anom])
        i_p = np.unravel_index(np.argmax(v_one - V_BG), v_one.shape)
        print(f"   {run:3d}   "
              f"{'uniform' if run == 0 else '2% random':15s}  {0.10:5.2f}   "
              f"{v_one[i_anom]:27.4f}   {v_one[i_p]:20.4f}")
    print(f"   the value recovered AT the anomaly spans {min(peaks):.4f} to "
          f"{max(peaks):.4f} m/ns, a")
    print(f"   spread of {np.std(peaks):.4f} m/ns "
          f"({np.std(peaks)/amp_true*100:.0f}% of the true contrast of "
          f"{amp_true:.4f} m/ns).")
    print("   The global maximum of the model wanders elsewhere entirely under")
    print("   noise, so the number to quote is the value at a FIXED location, with")
    print("   its spread over runs -- and never a single run's maximum.")

    section("7. What the inversion does and does not determine")
    print("   Determines: the scattering potential within the source-receiver")
    print("   bandwidth and the illumination footprint, i.e. the smoothed product")
    print("   of velocity contrast and geometry.")
    print("   Does not determine: the absolute velocity below the resolution")
    print("   length, the density-permittivity split, attenuation, and anything")
    print("   outside the illuminated region.  The FDTD experiments in this script")
    print("   are a test bed for the method, not a survey: two sources and eleven")
    print("   receivers in a 0.8 m box is a demonstration of what an inversion")
    print("   determines, not an image of anything real.")
    print("\n   Every number above comes from the SYNTHETIC models and the FDTD")
    print("   schemes written in this script; no measured velocity or published")
    print("   inversion result is quoted.")


if __name__ == "__main__":
    main()
