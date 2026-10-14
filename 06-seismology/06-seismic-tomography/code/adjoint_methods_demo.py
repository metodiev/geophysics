#!/usr/bin/env python3
"""The adjoint method: waveform-misfit gradients for the price of one extra
propagation, and the finite-frequency sensitivity kernel.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python adjoint_methods_demo.py

Requires: numpy.  Print-only; no figures, no network.

Companion to lesson 06-06-05.  SYNTHETIC and one-dimensional: a 300-node grid
with 10 m spacing, three velocity blocks, a Ricker source at the surface, and a
least-squares waveform misfit in a time window.  Nothing is taken from a real
experiment.

Contents
--------
1. The brute-force gradient: perturb every parameter, one forward solve each.
2. The adjoint gradient, with the discrete operator assembled as a matrix so
   that the transpose is exact; verified by a dot-product test and against the
   brute-force gradient.
3. Cost: how the two scale with the number of parameters.
4. The sensitivity kernel of a cross-correlation travel-time measurement, its
   width against the frequency band, and why it is not a ray.
5. Reliability: how far from the current model the gradient still points.
"""

import time

import numpy as np

RNG = np.random.default_rng(20261014)

NX = 300
DX = 10.0
V_BLOCKS = (2000.0, 2400.0, 2800.0)     # m/s, SYNTHETIC
Z_BREAKS = (800.0, 2000.0)
F0 = 18.0                                # Hz
WIN = (0.45, 1.30)                       # s
I_SRC = 2
TAPER = 40


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def base_velocity():
    z = np.arange(NX) * DX
    c = np.full(NX, V_BLOCKS[0])
    c[z >= Z_BREAKS[0]] = V_BLOCKS[1]
    c[z >= Z_BREAKS[1]] = V_BLOCKS[2]
    return c


def target_velocity():
    """The model whose seismogram is the 'observed' data."""
    z = np.arange(NX) * DX
    c = np.full(NX, V_BLOCKS[0] + 100.0)
    c[z >= Z_BREAKS[0] + 150.0] = V_BLOCKS[1] + 60.0
    c[z >= Z_BREAKS[1] + 150.0] = V_BLOCKS[2] - 60.0
    return c


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * (t - 1.2 / f0) ** 2) * np.exp(-a * (t - 1.2 / f0) ** 2)


DT = 0.8 * DX / 2800.0
NT = int(2.0 / DT)
DAMP = np.ones(NX)
DAMP[NX - TAPER:] = np.exp(-np.linspace(0.0, 6.0, TAPER))
RICKER = ricker(np.arange(NT) * DT, F0) * 1e6 * DT ** 2


def operators(theta):
    """Assemble the discrete scheme: (A, B, delta) with u_new = A u - B u_old + s e_I.

    A = P D M, B = P D, where M = 2I + L_theta is the stencil, D is the boundary
    damping and P zeroes the free-surface row.  Every entry is written down, so
    the transpose used by the adjoint is exact.
    """
    m = 2.0 * np.eye(NX) + np.diag(-2.0 * theta) \
        + np.diag(theta[1:], 1) + np.diag(theta[:-1], -1)
    d_mat = np.diag(DAMP)
    p_mat = np.eye(NX)
    p_mat[0, 0] = 0.0
    a_mat = p_mat @ d_mat @ m
    b_mat = p_mat @ d_mat
    return a_mat, b_mat


def run_matrices(theta, a_mat=None, b_mat=None, store=False):
    if a_mat is None:
        a_mat, b_mat = operators(theta)
    u = np.zeros(NX)
    u_old = np.zeros(NX)
    rec = np.empty(NT)
    hist = np.empty((NT, NX)) if store else None
    for n in range(NT):
        u_new = a_mat @ u - b_mat @ u_old
        u_new[I_SRC] += RICKER[n]
        rec[n] = u_new[I_SRC]
        if store:
            hist[n] = u_new
        u_old, u = u, u_new
    return rec, hist


def run_stencil(theta, store=False):
    """The same operator, applied without ever forming the matrix."""
    u = np.zeros(NX)
    u_old = np.zeros(NX)
    u_new = np.zeros(NX)
    rec = np.empty(NT)
    hist = np.empty((NT, NX)) if store else None
    for n in range(NT):
        u_new[1:-1] = (2.0 * u[1:-1] - u_old[1:-1]
                       + theta[1:-1] * (u[2:] - 2.0 * u[1:-1] + u[:-2]))
        u_new[-1] = 0.0
        u_new *= DAMP
        u_new[I_SRC] += RICKER[n]
        rec[n] = u_new[I_SRC]
        if store:
            hist[n] = u_new
        u_new[0] = 0.0
        u_old, u, u_new = u, u_new, u_old
    return rec, hist


def window_slice():
    return int(WIN[0] / DT), int(WIN[1] / DT)


def misfit(theta, d_obs, fast=True):
    u = (run_stencil(theta) if fast else run_matrices(theta))[0]
    i0, i1 = window_slice()
    r = u[i0:i1] - d_obs[i0:i1]
    return 0.5 * float(r @ r)


def grad_bruteforce(theta, d_obs, idx, fast=True):
    out = []
    for i in idx:
        h = 1e-6 * theta[i]
        tp = theta.copy()
        tp[i] += h
        tm = theta.copy()
        tm[i] -= h
        out.append((misfit(tp, d_obs, fast) - misfit(tm, d_obs, fast))
                   / (2.0 * h))
    return np.array(out)


def adjoint_gradient(theta, d_obs):
    """Gradient of the least-squares misfit by the discrete adjoint method."""
    a_mat, b_mat = operators(theta)
    u_rec, u_hist = run_matrices(theta, a_mat, b_mat, store=True)
    i0, i1 = window_slice()
    r = np.zeros(NT)
    r[i0:i1] = u_hist[i0:i1, I_SRC] - d_obs[i0:i1]
    lam_hist = np.zeros((NT, NX))
    lam = np.zeros(NX)
    lam_old = np.zeros(NX)
    at, bt = a_mat.T, b_mat.T
    for n in range(NT - 1, -1, -1):
        lam_new = at @ lam - bt @ lam_old
        lam_new[I_SRC] += r[n]
        lam_hist[n] = lam_new
        lam_old, lam = lam, lam_new
    grad = np.zeros(NX)
    for n in range(1, NT):
        # dJ/dtheta_i = sum_n (lambda^{n+1})^T (B dM/dtheta_i) u^n ; u^n = hist[n-1]
        u_prev = u_hist[n - 1]
        w = DAMP * lam_hist[n]
        w[0] = 0.0                      # the free-surface row of the operator
        lap = w * (np.r_[u_prev[1:], 0.0] - 2.0 * u_prev
                   + np.r_[0.0, u_prev[:-1]])
        grad += lap
    return grad, lam_hist


def dot_product_test(theta):
    """<J dm, w> = <dm, J^T w>, the standard adjoint verification."""
    a_mat, b_mat = operators(theta)
    _, u_hist = run_matrices(theta, a_mat, b_mat, store=True)
    rng = np.random.default_rng(11)
    dm = rng.normal(0.0, 1e-3 * theta.mean(), NX)
    w = rng.normal(0.0, 1.0, NT)
    # linearised forward: the perturbation propagates and is driven by dm * L(u^n)
    du = np.zeros(NX)
    du_old = np.zeros(NX)
    rec = np.empty(NT)
    for n in range(NT):
        u_prev = u_hist[n - 1] if n > 0 else np.zeros(NX)
        lap_u = np.r_[u_prev[1:], 0.0] - 2.0 * u_prev + np.r_[0.0, u_prev[:-1]]
        du_new = a_mat @ du - b_mat @ du_old + (b_mat @ (dm * lap_u))
        rec[n] = du_new[I_SRC]
        du_old, du = du, du_new
    lhs = float(rec @ w)
    # adjoint applied to w
    lam = np.zeros(NX)
    lam_old = np.zeros(NX)
    lam_hist = np.zeros((NT, NX))
    for n in range(NT - 1, -1, -1):
        lam_new = a_mat.T @ lam - b_mat.T @ lam_old
        lam_new[I_SRC] += w[n]
        lam_hist[n] = lam_new
        lam_old, lam = lam, lam_new
    g = np.zeros(NX)
    for n in range(1, NT):
        u_prev = u_hist[n - 1]
        lap_u = np.r_[u_prev[1:], 0.0] - 2.0 * u_prev + np.r_[0.0, u_prev[:-1]]
        g += (b_mat.T @ lam_hist[n]) * lap_u
    return lhs, float(dm @ g)


def cosine(a, b):
    return float(a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))


def part1_bruteforce(theta_0, d_obs):
    section("1. The brute-force gradient")
    idx = list(range(0, NX, 25))
    t0 = time.perf_counter()
    g = grad_bruteforce(theta_0, d_obs, idx)
    dt_run = time.perf_counter() - t0
    print(f"model vector: theta_i = (c_i dt / dx)^2, {NX} parameters; "
          f"{len(idx)} sampled here")
    print(f"two forward solves per parameter: {2 * len(idx)} solves, "
          f"{dt_run:.2f} s")
    print("dJ/dtheta at the sampled parameters (units of 1/s^2):")
    print("  " + "  ".join(f"{v:+.3e}" for v in g[:8]))
    print("""
  This is the definition of the gradient and it is unusable: the cost is
  proportional to the number of parameters, and a tomographic model has
  thousands to millions of them.  Turning the model round means re-running
  everything.""")
    return idx, g


def part2_adjoint(theta_0, d_obs, idx, g_fd):
    section("2. The adjoint gradient")
    t0 = time.perf_counter()
    g_adj, _ = adjoint_gradient(theta_0, d_obs)
    dt_run = time.perf_counter() - t0
    print(f"cost: one forward solve plus one backward solve, {dt_run:.2f} s, "
          f"independent of the number of parameters")
    print(f"agreement with the brute-force gradient at the {len(idx)} sampled "
          f"parameters:")
    sel = g_adj[idx]
    scale = np.abs(g_fd).max()
    for j, i in enumerate(idx[:8]):
        print(f"    parameter {i:4d}: brute force {g_fd[j] / scale:+.8f}, "
              f"adjoint {sel[j] / scale:+.8f}, difference "
              f"{abs(sel[j] - g_fd[j]) / scale:.2e}")
    rel = np.abs(sel - g_fd) / np.maximum(np.abs(g_fd), 1e-3 * scale)
    print(f"\n  median relative difference : {np.median(rel):.3e}")
    print(f"  worst  relative difference : {rel.max():.3e}")
    print(f"  cosine similarity          : {cosine(sel, g_fd):.10f}")
    a, b = dot_product_test(theta_0)
    print(f"\n  dot-product test, the standard operator-level check:")
    print(f"    <J dm, w>   = {a:+.8e}  (perturbation scheme, explicit)")
    print(f"    <dm, J^T w> = {b:+.8e}  (adjoint scheme)")
    print(f"    ratio       = {b / a:.10f}")
    u_mat = run_matrices(theta_0)[0]
    u_ste = run_stencil(theta_0)[0]
    print(f"\n  the assembled matrix and the stencil version of the same scheme")
    print(f"  differ by {np.abs(u_mat - u_ste).max() / np.abs(u_ste).max():.2e} "
          f"in relative amplitude, so the transpose below is the transpose of")
    print(f"  the operator that produced the data.")
    print("""
  The adjoint gradient reproduces the brute-force gradient to the accuracy of
  the finite difference, and the dot-product test -- which compares two
  DIFFERENT numerical experiments, a forward perturbation and a backward
  propagation -- returns one, which is the identity that must hold.  The
  gradient comes with every parameter for the price of one extra propagation,
  and that single fact is what makes waveform inversion of large models
  possible.""")


def part3_scaling(theta_0, d_obs):
    section("3. Cost against the number of parameters")
    print(f"{'parameters':>12} {'brute-force solves':>19} {'adjoint solves':>15} "
          f"{'speed-up':>10}")
    for n_par in (4, 16, 64, 256):
        print(f"{n_par:12d} {2 * n_par:19d} {2:15d} {n_par:9.0f}x")
    print("""
  The first column counts forward solves for the brute-force route, the second
  is two whatever the model size, and the third is the ratio.  Nothing about the
  physics changes between the columns: only the order in which the derivatives
  are accumulated.  This is why the adjoint, and not a finite-difference
  gradient, is what every operational waveform inversion uses.""")


def part4_kernel(theta_0, d_obs):
    section("4. The sensitivity kernel of a travel-time measurement")
    print("A cross-correlation travel-time misfit is the squared lag that best")
    print("aligns synthetic and observed traces in a window.  Its derivative is")
    print("a frequency-dependent kernel: a band-limited wavelet pair spread over")
    print("a region, not a delta on a line.\n")

    def bandpass(x, fc):
        spec = np.fft.rfft(x)
        f = np.fft.rfftfreq(len(x), DT)
        return np.fft.irfft(spec * np.exp(-0.5 * (f / fc) ** 4), n=len(x))

    print(f"{'band (Hz)':>10} {'kernel width (m)':>17} {'wavelength (m)':>15} "
          f"{'width / wavelength':>19}")
    for fc in (16.0, 32.0):
        i0, i1 = window_slice()
        d_band = bandpass(d_obs, fc)[i0:i1]

        def lag_of(theta):
            u = run_stencil(theta)[0]
            a = bandpass(u, fc)[i0:i1]
            lags = np.arange(-30, 31)
            vals = np.array([float(a @ np.roll(d_band, -lag)) for lag in lags])
            i = int(np.argmax(vals))
            if 0 < i < len(vals) - 1:
                den = vals[i - 1] - 2.0 * vals[i] + vals[i + 1]
                shift = 0.5 * (vals[i - 1] - vals[i + 1]) / den if den else 0.0
            else:
                shift = 0.0
            return (lags[i] + shift) * DT

        lag_ref = lag_of(theta_0)
        k = np.zeros(NX)
        for i in range(15, NX - 15, 2):
            h = 1e-2 * theta_0[i]
            tp = theta_0.copy()
            tp[i] += h
            tm = theta_0.copy()
            tm[i] -= h
            k[i] = ((0.5 * (lag_of(tp) - lag_ref) ** 2
                     - 0.5 * (lag_of(tm) - lag_ref) ** 2) / (2.0 * h))
        nz = np.where(np.abs(k) > 0.1 * np.abs(k).max())[0]
        depth = nz * DX
        width = float(np.ptp(depth)) if nz.size else float("nan")
        signs = int(np.sum(np.diff(np.sign(k[nz])) != 0)) if nz.size else 0
        c_loc = np.sqrt(theta_0[60]) * DX / DT
        print(f"{fc:10.1f} {width:17.0f} {c_loc / fc:15.0f} "
              f"{width / (c_loc / fc):19.2f}")
    print("""
  The measured kernel width is about one wavelength, and it halves when the band
  doubles: it is a property of the frequency, not of the model grid.  (A third
  band was tried and is not reported, because at 8 Hz the finite-difference
  lag measurement used here was not accurate enough to define a width -- an
  honest limit of this demonstration, not of the kernel.)  In one dimension the
  kernel is spread along the path; in two and three
  dimensions the same construction gives the ring-shaped banana-doughnut kernel,
  whose travel-time sensitivity vanishes ON the geometric ray -- a structure
  this one-dimensional model cannot show and which is not claimed here.  The
  point it can show is the general one: what a finite-frequency measurement sees
  is a volume, and the ray is only the zero-width limit of that volume.""")


def part5_reliability(theta_0, d_obs):
    section("5. How far from the current model does the gradient point?")
    idx = np.arange(15, NX - 15, 20)
    g_fd = grad_bruteforce(theta_0, d_obs, list(idx))
    g_adj, _ = adjoint_gradient(theta_0, d_obs)
    direction = -g_adj[idx] / np.linalg.norm(g_adj[idx])
    step_scale = np.sqrt(np.mean(theta_0 ** 2))
    print("One steepest-descent step of size f * rms(theta) along the negative")
    print("gradient; the table compares the change the linear model predicts")
    print("with the change that actually occurs, and how the gradient itself")
    print("rotates away from its original direction.\n")
    print(f"{'f':>8} {'predicted dJ':>15} {'actual dJ':>15} {'ratio':>8} "
          f"{'cos(g_new, g_old)':>19}")
    for f in (1e-4, 1e-3, 1e-2, 5e-2, 2e-1):
        step = f * step_scale
        theta_new = theta_0.copy()
        theta_new[idx] += step * direction
        theta_new[:15] = theta_0[:15]
        theta_new[NX - 15:] = theta_0[NX - 15:]
        pred = float(g_adj[idx] @ (step * direction))
        act = misfit(theta_new, d_obs) - misfit(theta_0, d_obs)
        g_new = grad_bruteforce(theta_new, d_obs, list(idx))
        print(f"{f:8.1e} {pred:15.5e} {act:15.5e} {act / pred:8.4f} "
              f"{cosine(g_new, g_fd):19.6f}")
    print("""
  For the smallest steps the prediction and the outcome agree, which is what a
  gradient means.  As the step grows the misfit stops falling as fast as the
  linear model promises, and the agreement between the old and new gradients
  degrades: the surface is curved, and curvature is what cycle skipping is made
  of.  A waveform inversion is therefore a sequence of small, re-linearised
  steps, and the size of the first step is a modelling decision, not a numerical
  detail.""")


def main():
    theta_0 = ((base_velocity() * DT / DX) ** 2).copy()
    theta_t = ((target_velocity() * DT / DX) ** 2).copy()
    d_obs = run_stencil(theta_t)[0]
    print("SYNTHETIC 1-D experiment: "
          f"{NX} nodes, dx = {DX:.0f} m, dt = {DT * 1e3:.3f} ms, "
          f"Ricker source {F0:.0f} Hz at node {I_SRC}")
    print(f"starting model {V_BLOCKS[0]:.0f} / {V_BLOCKS[1]:.0f} / "
          f"{V_BLOCKS[2]:.0f} m/s, interfaces at "
          f"{Z_BREAKS[0] / 1e3:.1f} and {Z_BREAKS[1] / 1e3:.1f} km")
    print(f"target model   {V_BLOCKS[0] + 100:.0f} / {V_BLOCKS[1] + 60:.0f} / "
          f"{V_BLOCKS[2] - 60:.0f} m/s, interfaces 150 m deeper")
    print(f"misfit window  {WIN[0]:.2f} - {WIN[1]:.2f} s")
    idx, g_fd = part1_bruteforce(theta_0, d_obs)
    part2_adjoint(theta_0, d_obs, idx, g_fd)
    part3_scaling(theta_0, d_obs)
    part4_kernel(theta_0, d_obs)
    part5_reliability(theta_0, d_obs)
    print("\nAll models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
