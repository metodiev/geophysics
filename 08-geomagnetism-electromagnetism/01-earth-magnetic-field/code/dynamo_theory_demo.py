#!/usr/bin/env python3
"""The geodynamo: induction, magnetic Reynolds number, flux freezing, the
alpha-omega mechanism and its energy budget.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dynamo_theory_demo.py

Everything here is SYNTHETIC.  Core size, conductivity, flow speed and dynamo
numbers are chosen teaching values, not measurements.  The only standard
constants used are mu0 = 4*pi*1e-7 H/m and the Earth radius 6371 km.

Contents
--------
1. Magnetic diffusivity from conductivity, and the diffusion time.
2. Magnetic Reynolds number and the frozen-flux regime.
3. The free-decay problem: why an undriven field dies.
4. A mean-field alpha-omega dynamo: growth, critical dynamo number, saturation.
5. Ohmic dissipation versus magnetic energy: the energy budget.
6. Numerical check: advection versus diffusion of one pattern.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi          # H/m, exact
A_EARTH_KM = 6371.0

# --- SYNTHETIC teaching parameters ------------------------------------------
SIGMA_S_M = 5.0e5             # S/m, chosen core conductivity
L_CORE_M = 2.1e6              # m, chosen core length scale
U_FLOW_M_S = 5.0e-4           # m/s, chosen core flow speed
B_TYPICAL_T = 3.0e-4          # T (= 300 000 nT), chosen characteristic field


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Magnetic diffusivity and the diffusion time")
    eta = 1.0 / (MU0 * SIGMA_S_M)
    print(f"SYNTHETIC parameters: sigma = {SIGMA_S_M:.1e} S/m, "
          f"L = {L_CORE_M:.2e} m")
    print(f"  magnetic diffusivity eta = 1/(mu0 sigma) = {eta:.4f} m^2/s")
    tau_diff = L_CORE_M ** 2 / eta
    print(f"  diffusion time L^2/eta = {tau_diff:.4e} s = "
          f"{tau_diff/(365.25*86400.0):.4e} yr")
    # fastest decaying free mode of a sphere: n(n+1) eta / a^2 with n = 1
    tau_free_s = L_CORE_M ** 2 / (2.0 * eta)
    YR_S = 365.25 * 86400.0
    tau_free_yr = tau_free_s / YR_S
    print(f"  slowest free decay of the dipole mode, L^2/(2 eta) = "
          f"{tau_free_yr:.4e} yr")
    print("  the field survives far longer than this, so it must be maintained.")

    section("2. Magnetic Reynolds number and the frozen-flux regime")
    Rm = U_FLOW_M_S * L_CORE_M / eta
    print(f"  Rm = U L / eta = {U_FLOW_M_S:.1e} x {L_CORE_M:.1e} / {eta:.4f} "
          f"= {Rm:.1f}")
    tau_adv = L_CORE_M / U_FLOW_M_S
    print(f"  advection time L/U = {tau_adv/(365.25*86400.0):.2f} yr")
    print(f"  ratio tau_diff/tau_adv = Rm = {Rm:.1f}")
    print("  with Rm >> 1 the field is carried with the fluid (frozen flux) on")
    print("  the advection time; diffusion matters only on scales below")
    l_d = np.sqrt(eta * tau_adv)
    print(f"  l ~ sqrt(eta L/U) = {l_d/1.0e3:.1f} km, the scale at which the two")
    print("  terms balance.")

    section("3. The free-decay problem")
    t = np.arange(0.0, 6.0e4, 1.0e3)
    b0 = B_TYPICAL_T
    dec = b0 * np.exp(-t / (2.0 * tau_free_yr))
    print("  an undriven dipole mode with the above eta decays as exp(-2 eta t/L^2):")
    for tt, bb in zip(t[::10], dec[::10]):
        print(f"    t = {tt:8.0f} yr: |B| = {bb*1e9:12.1f} nT "
              f"({100*bb/b0:7.3f}% of initial)")
    print(f"  characteristic e-folding time = {tau_free_yr:.4e} yr")
    print("  a field observed to persist for intervals far longer than this")
    print("  free-decay time is evidence for continuous maintenance, not for a")
    print("  fossil field.")

    section("4. A mean-field alpha-omega dynamo")
    # Coupled poloidal/toroidal amplitudes with regeneration alpha, shear omega,
    # and a common diffusive decay rate k.
    k = 1.0 / tau_free_yr                            # 1/yr, diffusive decay
    D_target = 2.0
    omega = np.sqrt(D_target) * k                    # SYNTHETIC shear
    alpha = np.sqrt(D_target) * k                    # SYNTHETIC regeneration
    print(f"  decay rate k = 1/tau_free = {k:.4e} 1/yr")
    print(f"  SYNTHETIC shear omega = {omega:.2e}, regeneration alpha = "
          f"{alpha:.2e}")
    D = alpha * omega / k ** 2
    print(f"  dynamo number D = alpha*omega/k^2 = {D:.3f}")
    M = np.array([[-k, alpha], [omega, -k]])
    w, _ = np.linalg.eig(M)
    print(f"  eigenvalues = {w[0]:+.6e}, {w[1]:+.6e} 1/yr")
    print(f"  growth rate = {w.real.max():+.6e} 1/yr for D = {D:.3f}")
    D_crit = 1.0
    print(f"  the system grows if and only if D > {D_crit:.1f}: with alpha = 0")
    print("  (no regeneration) or omega = 0 (no shear) it merely decays, which is")
    print("  why an axisymmetric, purely toroidal problem cannot sustain a field")
    print("  (Cowling's theorem).")
    for Dtest in (0.25, 0.9, 1.0, 1.21, 2.0, 4.0):
        sc = np.sqrt(Dtest) * k
        M2 = np.array([[-k, sc], [sc, -k]])
        w2 = np.linalg.eigvals(M2).real.max()
        label = "growth" if w2 > 1e-12 else ("marginal" if abs(w2) < 1e-15
                                            else "decay")
        print(f"  D = {Dtest:5.2f} -> growth rate {w2:+.4e} 1/yr ({label})")

    section("5. Saturation by alpha-quenching (time integration)")
    dt = 200.0
    nsteps = 4000
    P = 1.0e-3       # tiny seed, arbitrary units of the poloidal amplitude
    T = 0.0
    hist = []
    for step in range(nsteps):
        Bn = np.hypot(P, T) / 1.0e-2
        aq = alpha / (1.0 + Bn ** 2)
        dP = -k * P + aq * T
        dT = omega * P - k * T
        P += dt * dP
        T += dt * dT
        hist.append((step * dt, P, T))
    print(f"  integrated {nsteps} steps of {dt:.0f} yr = {nsteps*dt:.0f} yr;")
    print(f"  growth rate at D = {D_target:.1f} is {np.sqrt(alpha*omega)-k:+.4e} "
          "1/yr, so the seed grows before quenching")
    for frac in (0, 10, 50, 200, 1000, 3999):
        tt, pp, ttp = hist[frac]
        print(f"    t = {tt:8.0f} yr: poloidal {pp:9.4e}, toroidal {ttp:9.4e}, "
              f"|B| proxy {np.hypot(pp, ttp):9.4e}")
    print("  the field grows exponentially then saturates when the alpha effect")
    print("  is quenched - the non-linear feedback a dynamo needs to be stable.")

    section("6. Energy and ohmic dissipation budget")
    vol = (4.0 / 3.0) * np.pi * L_CORE_M ** 3
    emag = B_TYPICAL_T ** 2 / (2.0 * MU0) * vol
    print(f"  SYNTHETIC core volume (sphere of radius {L_CORE_M:.2e} m) = "
          f"{vol:.3e} m^3")
    print(f"  magnetic energy density B^2/(2 mu0) = "
          f"{B_TYPICAL_T**2/(2*MU0):.3e} J/m^3")
    print(f"  total magnetic energy = {emag:.3e} J = {emag/1e12:.3e} TJ")
    J = B_TYPICAL_T / (MU0 * L_CORE_M)
    diss = J ** 2 / SIGMA_S_M * vol
    print(f"  characteristic current density J = B/(mu0 L) = {J:.3e} A/m^2")
    print(f"  ohmic dissipation J^2/sigma x volume = {diss:.3e} W")
    print(f"  ratio (energy / dissipation) = {emag/diss:.3e} s = "
          f"{emag/diss/(365.25*86400.0):.3e} yr")
    print("  the magnetic (Lorentz) force drives the flow that makes the field,")
    print("  so the dissipation has to be paid for out of the same budget.")

    section("7. Numerical check: advection versus diffusion of a synthetic field")
    nx = 512
    x = np.linspace(0.0, 1.0, nx, endpoint=False)
    b = np.sin(2.0 * np.pi * x)
    kk = 2.0 * np.pi * np.fft.rfftfreq(nx, d=1.0 / nx)
    T = 1.0
    u, D_num = 0.10, 0.02
    B = np.fft.rfft(b)
    b_adv = np.fft.irfft(B * np.exp(-1j * kk * u * T), n=nx)
    b_diff = np.fft.irfft(B * np.exp(-D_num * kk ** 2 * T), n=nx)
    print(f"  exact spectral operators over one time unit: u = {u:.2f}, "
          f"D = {D_num:.2f}")
    print(f"    peak amplitude retained, advection: "
          f"{np.abs(b_adv).max()/np.abs(b).max():.6f} (pattern moves, kept)")
    print(f"    peak amplitude retained, diffusion: "
          f"{np.abs(b_diff).max()/np.abs(b).max():.6f} (amplitude lost)")
    print(f"    correlation with the initial field: advection "
          f"{np.corrcoef(b, b_adv)[0,1]:+.6f}, diffusion "
          f"{np.corrcoef(b, b_diff)[0,1]:+.6f}")
    print(f"    phase of the advected fundamental: "
          f"{np.degrees(np.angle(np.fft.rfft(b_adv)[1]/np.fft.rfft(b)[1])):.3f} deg")
    print("  advection transports the pattern and preserves it; diffusion leaves")
    print("  the pattern in place and destroys it.  Which term wins is decided by")
    print("  the magnetic Reynolds number, not by either term alone.")


if __name__ == "__main__":
    main()
