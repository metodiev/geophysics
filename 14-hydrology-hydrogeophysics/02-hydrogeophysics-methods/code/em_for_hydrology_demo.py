#!/usr/bin/env python3
"""EM and TDEM for hydrogeology: skin depth, magnetic diffusion, the step-off
surface response, an apparent-conductivity inversion, depth of investigation,
two-layer conductance equivalence, and a comparison with DC resistivity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_for_hydrology_demo.py

All conductivities, depths, times and synthetic responses are SYNTHETIC teaching
values.  No real survey, instrument or field data are used.

Standard constants used:
    mu_0 = 4 pi x 10^-7 H/m (exact in SI)

Contents
--------
1. Skin depth versus frequency and conductivity (frequency-domain EM).
2. Magnetic diffusion depth versus time (TDEM), and the time to reach a depth.
3. A finite-difference solution of the 1-D diffusion equation, verified against
   the analytic erf solution.
4. The step-off surface response, its measured power law, and an inverted
   apparent conductivity with noise.
5. Layered ground: conductance equivalence and where it breaks down.
6. Penetration comparison with DC resistivity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi      # H/m, exact in SI


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def skin_depth(f_hz, sigma_s_m):
    """delta = sqrt(2/(omega mu_0 sigma)), in metres."""
    omega = 2.0 * np.pi * f_hz
    return np.sqrt(2.0 / (omega * MU0 * sigma_s_m))


def diffusion_depth(rho_ohm_m, t_s):
    """z = sqrt(2 rho t / mu_0): the 1-D diffusion depth for a step-off source."""
    return np.sqrt(2.0 * rho_ohm_m * t_s / MU0)


def diffusion_time(rho_ohm_m, z_m):
    """t = mu_0 z^2 / (2 rho): the time at which the diffusion reaches depth z."""
    return MU0 * z_m ** 2 / (2.0 * rho_ohm_m)


def solve_diffusion(sigma_profile, dz, dt, n_steps, nz):
    """Explicit 1-D magnetic diffusion with a step-off at the surface.

    d B/dt = d/dz [ D(z) dB/dz ],  D = 1/(mu_0 sigma(z)),
    B(z,0) = B0,  B(0,t) = 0,  B(L,t) = B0.
    Returns the surface gradient history and the final profile (B normalised to
    B0 = 1).
    """
    z = np.linspace(0.0, dz * (nz - 1), nz)
    D = 1.0 / (MU0 * sigma_profile)
    D_mid = 2.0 / (1.0 / D[1:] + 1.0 / D[:-1])       # harmonic mean at interfaces
    B = np.ones(nz)
    B[0] = 0.0
    grad_hist = np.zeros(n_steps)
    for s in range(n_steps):
        lap = np.zeros(nz)
        lap[1:-1] = (D_mid[1:] * (B[2:] - B[1:-1])
                     - D_mid[:-1] * (B[1:-1] - B[:-2])) / dz ** 2
        B = B + dt * lap
        B[0] = 0.0
        B[-1] = 1.0
        grad_hist[s] = (B[1] - B[0]) / dz
    return np.arange(1, n_steps + 1) * dt, grad_hist, z, B


def main():
    section("1. Skin depth versus frequency and conductivity")
    print("  delta = sqrt(2 / (omega mu_0 sigma)) = 503 / sqrt(f sigma) m "
          "(f in Hz, sigma in S/m)")
    print("   f (Hz)      sigma = 0.01    0.1          1.0 S/m   (delta in m)")
    for f in (10.0, 100.0, 1000.0, 10000.0):
        print(f"   {f:8.0f}   " + "   ".join(
            f"{skin_depth(f, s):12.2f}" for s in (0.01, 0.1, 1.0)))
    print("  a conductive ground (1 S/m) screens a 1 kHz signal within 16 m, while")
    print("  a resistive one (0.01 S/m) carries it 159 m: **conductivity, not depth,")
    print("  is the first thing that sets the frequency you need.**")

    section("2. Diffusion depth and time (TDEM)")
    print("  z = sqrt(2 rho t / mu_0);  t = mu_0 z^2 / (2 rho)")
    print("   rho (ohm m)   t = 0.1 ms   1 ms       10 ms      100 ms")
    for rho in (1.0, 10.0, 100.0):
        print(f"   {rho:11.1f}   " + "   ".join(
            f"{diffusion_depth(rho, t):9.1f}" for t in (1e-4, 1e-3, 1e-2, 1e-1)))
    print("  (values are depth in metres)")
    print("\n   depth (m)    rho = 1 ohm m   rho = 10       rho = 100")
    for z in (10.0, 50.0, 100.0, 200.0):
        print(f"   {z:9.1f}   " + "   ".join(
            f"{diffusion_time(r, z) * 1e3:12.3f}" for r in (1.0, 10.0, 100.0)))
    print("  (values are time in ms)")
    print("  Sounding to 100 m in a 10 ohm m ground needs about 0.6 ms of usable")
    print("  decay; in a 1 ohm m (saline) ground the same depth needs 6 ms, which")
    print("  is often beyond the instrument's noise floor: **saline ground is both")
    print("  the easiest target in principle and the hardest to sound deeply**.")

    section("3. Finite-difference diffusion verified against the analytic erf")
    sigma = 0.1
    rho = 1.0 / sigma
    dz, nz = 1.0, 401
    dt = 2.5e-8
    stable_dt = 0.5 * dz ** 2 * MU0 * sigma
    n_steps = 40000
    print(f"  explicit stability limit dt <= 0.5 dz^2 / D = {stable_dt:.3e} s; "
          f"using dt = {dt:.1e} s")
    t_axis, grad_num, z, B_num = solve_diffusion(np.full(nz, sigma), dz, dt,
                                                 n_steps, nz)
    D = 1.0 / (MU0 * sigma)
    from math import erf

    # analytic solution B = erf(z / (2 sqrt(D t))), compared at the final time
    t_final = t_axis[-1]
    B_ana = np.array([erf(zz / (2.0 * np.sqrt(D * t_final))) for zz in z])
    interior = slice(0, nz - 3)
    err = np.max(np.abs(B_num[interior] - B_ana[interior]))
    print(f"  sigma = {sigma:.1f} S/m (rho = {rho:.1f} ohm m), D = {D:.3e} m^2/s")
    print(f"  grid: {nz} nodes over {dz * (nz - 1):.0f} m, dt = {dt:.1e} s, "
          f"{n_steps} steps, t = {t_final * 1e3:.3f} ms")
    print(f"  diffusion length sqrt(4Dt) = {np.sqrt(4 * D * t_final):.1f} m, "
          f"inside the {dz * (nz - 1):.0f} m domain")
    print(f"  max |B_num - erf(z/2sqrt(Dt))| over the interior = {err:.3e}")
    print(f"  the error at the far boundary node only = "
          f"{abs(B_num[-1] - B_ana[-1]):.3e} (the Dirichlet condition pins it)")
    print(f"  the analytic erf solution solves d B/dt = D d2B/dz2 with B(z,0) = 1,")
    print("  B(0,t) = 0, B(inf,t) = 1 exactly, so this verifies the spatial stencil")
    print("  and the step-off boundary treatment.")

    section("4. The step-off surface response and its apparent conductivity")
    grad_ana = 1.0 / np.sqrt(np.pi * D * t_axis)
    print("  analytic surface gradient  g(t) = 1/sqrt(pi D t), so g ~ t^-1/2")
    print("   t (ms)    g_analytic   g_numerical   rel. error (%)")
    for t_t in (2.0e-4, 1.0e-3, 1.0e-2, 2.0e-2, 1.0e-1):
        idx = int(round(t_t * 1e-3 / dt)) - 1
        print(f"   {t_axis[idx] * 1e3:7.3f}   {grad_ana[idx]:11.5f}   "
              f"{grad_num[idx]:11.5f}   "
              f"{(grad_num[idx] / grad_ana[idx] - 1) * 100:+13.3f}")
    late_frac = t_axis > 0.02 * t_axis[-1]
    ratio = np.max(np.abs(grad_num[late_frac] - grad_ana[late_frac])
                   / grad_ana[late_frac]) * 100
    print(f"  max error for t > 0.02 ms = {ratio:.2f}%; the larger errors at the")
    print("  earliest samples are discretisation: when the diffusion length is only")
    print("  a couple of node spacings, the erf profile is not resolved near z = 0.")
    print("  This is a resolution limit of the grid, not a model error, and it is")
    print("  exactly the same effect that limits early-time TDEM data in the field.")
    late = t_axis > 0.2 * t_axis[-1]
    slope = np.polyfit(np.log10(t_axis[late]), np.log10(grad_num[late]), 1)[0]
    print(f"  measured power law on the last 80% of the window: g ~ t^({slope:.4f})")
    print("  -0.5 is the 1-D (plane-wave) step-off exponent.  A 3-D small-loop")
    print("  system over a half-space instead decays as t^-2.5 at late time; the")
    print("  difference is geometry, not physics, and the 1-D result here is")
    print("  derived and verified rather than quoted.")
    print("\n  apparent conductivity from the 1-D response: "
          "sigma_a = pi t (g)^2 / mu_0")
    print("   t (ms)     g_measured   sigma_a (S/m)   rho_a (ohm m)   "
          "diffusion depth (m)")
    for t_t in (0.02, 0.05, 0.1, 0.2, 0.5):
        idx = int(round(t_t * 1e-3 / dt)) - 1
        g = float(grad_num[idx])
        sig = np.pi * t_axis[idx] * g ** 2 / MU0
        print(f"   {t_axis[idx] * 1e3:8.3f}   {g:11.4f}   {sig:13.5f}   "
              f"{1.0 / sig:14.2f}   {diffusion_depth(1.0 / sig, t_axis[idx]):16.1f}")
    print("  the recovered conductivity is exact at every time (to the accuracy of")
    print("  the finite-difference gradient), as it must be for a half-space.")
    print("  With 3% multiplicative noise on g, sigma_a inherits (1 +- 0.03)^2 = "
          "+-6%,")
    print("  so the error on the apparent conductivity is TWICE the amplitude error.")
    noise = 0.03
    i_last = int(np.where(late)[0][-1])
    errs = []
    for _ in range(2000):
        g_n = grad_num * (1.0 + noise * RNG.standard_normal(grad_num.size))
        sig_n = np.pi * t_axis * g_n ** 2 / MU0
        errs.append(sig_n[i_last] / sigma - 1.0)
    errs = np.array(errs)
    print(f"  Monte Carlo (2000 realisations, 3% noise on g, single late-time "
          f"sample):")
    print(f"   mean sigma_a error = {errs.mean() * 100:+.3f}% "
          f"(second order, as predicted)")
    print(f"   standard deviation = {errs.std() * 100:.2f}% against the predicted "
          f"{2 * noise * 100:.1f}%")
    print("  so the small bias is second order in the noise, and the scatter is")
    print("  twice the amplitude noise as predicted.")

    section("5. Layered ground: conductance equivalence and where it breaks")
    host_sigma = 0.02
    t_end = 6.283e-5
    dt2 = 6.0e-9
    n_steps2 = int(round(t_end / dt2))
    stable2 = 0.5 * dz ** 2 * MU0 * host_sigma
    print(f"  host rho = {1.0 / host_sigma:.0f} ohm m; explicit stability limit "
          f"dt <= {stable2:.2e} s, using dt = {dt2:.1e} s")
    print(f"  SYNTHETIC: a conductive layer of conductance S = b sigma = 2.0 S,")
    print(f"  embedded at 20 m depth in a {host_sigma:.3f} S/m host, sounded to "
          f"{t_end * 1e3:.4f} ms")
    print(f"  host diffusion depth at t_end = "
          f"{diffusion_depth(1.0 / host_sigma, t_end):.1f} m, so the layer is a")
    print("  thin sheet compared with the diffusion length")
    print("   b (m)   sigma_layer (S/m)   surface g at t_end   deviation from "
          "thin-layer (%)")
    ref = None
    for b in (2.0, 4.0, 8.0, 16.0, 32.0):
        sig_prof = np.full(nz, host_sigma)
        top = int(round(20.0 / dz))
        thick = max(1, int(round(b / dz)))
        sig_prof[top: top + thick] = 2.0 / b
        _, g_hist, _, _ = solve_diffusion(sig_prof, dz, dt2, n_steps2, nz)
        val = float(g_hist[-1])
        if ref is None:
            ref = val
        print(f"   {b:5.1f}   {2.0 / b:17.4f}   {val:19.5f}   "
              f"{(val / ref - 1) * 100:24.2f}")
    print("  All five models have the SAME conductance, and the thin ones are")
    print("  indistinguishable: that is conductance equivalence.  It breaks down as")
    print("  the layer thickness approaches the diffusion depth, because then the")
    print("  layer's internal structure matters and not just its total conductance.")
    print("  **A TDEM (or ERT) model of a thin conductive layer is a model of its")
    print("  conductance.  Report S = b/rho, and say that b and rho are not")
    print("  separately determined.**")

    section("6. Penetration: EM versus DC resistivity")
    print("   method        typical depth    conductive-ground penalty   "
          "resolution at depth")
    print("   DC ERT        50-200 m         severe (current follows the")
    print("                                   conductor)                  poor")
    print("   FDEM          10-100 m         strong (screening)          poor")
    print("   TDEM          50-500 m         strong for depth, but the")
    print("                                   target itself is easy        moderate")
    print("   tem sounding of a 1 ohm m aquifer at 100 m:")
    t_need = diffusion_time(1.0, 100.0)
    print(f"     needs t = mu_0 z^2/(2 rho) = {t_need * 1e3:.2f} ms of usable decay")
    print(f"   the same target at 200 m needs {diffusion_time(1.0, 200.0) * 1e3:.2f} ms")
    print("   and a 100 ohm m resistive target at 200 m needs only "
          f"{diffusion_time(100.0, 200.0) * 1e3:.3f} ms")
    print("   a 10 ohm m target at 200 m needs "
          f"{diffusion_time(10.0, 200.0) * 1e3:.2f} ms")
    print("  The rule that follows: **every factor of 10 in target resistivity buys")
    print("  a factor of sqrt(10) in depth for the same time window** (because")
    print("  z ~ sqrt(rho t)), which is why TDEM is the method of choice for deep")
    print("  resistive aquifers and why saline aquifers are sounded at shallow depth")
    print("  or with larger transmitter moments.")


if __name__ == "__main__":
    main()
