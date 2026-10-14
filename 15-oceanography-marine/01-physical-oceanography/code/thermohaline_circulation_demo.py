#!/usr/bin/env python3
"""Thermohaline circulation: a two-box Stommel model with multiple equilibria,
the fold in the freshwater forcing, the advective-diffusive thermocline scale,
and an overturning heat transport.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermohaline_circulation_demo.py

Everything here is SYNTHETIC.  The box-model coefficients are chosen teaching
values, not calibrated to any ocean.  No hydrographic section, mooring or
reanalysis is used.

Contents
--------
1. The two-box model: steady states of q at a reference freshwater forcing.
2. Hysteresis: scanning the freshwater flux through the fold.
3. Stability of each branch by linearisation.
4. The advective-diffusive thermocline scale delta = kappa/w.
5. Overturning heat transport from a synthetic streamfunction.
6. Verification: root residuals, the |q| kink, and the thermocline ODE.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC box-model constants (chosen teaching values) ------------------
C_T = 1.0 / 25.0      # 1/yr, thermal restoring rate (25-year timescale)
DT_A = 25.0           # degC, imposed (atmospheric) temperature difference
ALPHA = 1.70e-4       # 1/degC, thermal expansion
BETA = 7.60e-4        # 1/(g/kg), haline contraction
K_Q = 30.0            # 1/yr, buoyancy-to-overturning proportionality (chosen)
F_S_REF = 0.02        # (g/kg)/yr, reference net freshwater forcing


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def residual(q, f_s):
    """F(q) = q - K_Q (alpha T - beta S), with T and S relaxed against advection.

    T = C_T DT_A / (C_T + |q|) and S = F_S / |q|.  The salinity balance is the
    important one: the freshwater flux is IMPOSED and must be balanced by
    advection, so a weak circulation builds a LARGE salinity difference.
    """
    absq = abs(q)
    T = C_T * DT_A / (C_T + absq)
    S = f_s / absq
    return q - K_Q * (ALPHA * T - BETA * S)


def steady_states(f_s, q_hi=0.5, n=200001):
    """All steady states of q in (0, q_hi] by sign-change scan + bisection."""
    qs = np.linspace(1e-6, q_hi, n)
    f = np.array([residual(q, f_s) for q in qs])
    roots = []
    for i in range(qs.size - 1):
        if f[i] * f[i + 1] < 0.0:
            a, b, fa = qs[i], qs[i + 1], f[i]
            for _ in range(100):
                m = 0.5 * (a + b)
                fm = residual(m, f_s)
                if fa * fm <= 0.0:
                    b = m
                else:
                    a, fa = m, fm
            roots.append(0.5 * (a + b))
    return np.array(roots)


def jacobian(q, f_s):
    """Jacobian of (dT/dt, dS/dt) at the steady state, and the state itself."""
    A = abs(q)
    s = 1.0 if q > 0 else -1.0
    T = C_T * DT_A / (C_T + A)
    S = f_s / A
    j11 = -C_T - A - T * s * K_Q * ALPHA
    j12 = T * s * K_Q * BETA
    j21 = -S * s * K_Q * ALPHA
    j22 = -A + S * s * K_Q * BETA
    return np.array([[j11, j12], [j21, j22]]), T, S


def main():
    section("1. The two-box model and its steady states")
    print("  Boxes: a warm low-latitude box and a cold high-latitude box.")
    print("  dT/dt = C_T (T_a - T) - |q| T        (temperature difference)")
    print("  dS/dt = F_S - |q| S                  (salinity difference)")
    print("  q = K_Q (alpha T - beta S)           (overturning, 1/yr)")
    print(f"  C_T = {C_T:.4f} 1/yr ({1 / C_T:.0f} yr), T_a = {DT_A:.1f} degC")
    print(f"  alpha = {ALPHA:.2e} 1/degC, beta = {BETA:.2e} 1/(g/kg), "
          f"K_Q = {K_Q:.1f} 1/yr")
    print(f"  F_S = {F_S_REF:.3f} (g/kg)/yr")
    print("\n  The salinity equation is NOT a relaxation to a fixed value: S is")
    print("  whatever balances the imposed freshwater flux against advection,")
    print("  S = F_S/|q|.  That single difference is what allows more than one")
    print("  steady state.")

    roots = steady_states(F_S_REF)
    print(f"\n  steady states at F_S = {F_S_REF:.3f} (g/kg)/yr:")
    print("    q (1/yr)    T (degC)   S (g/kg)   alpha T - beta S   mode")
    for r in roots:
        A = abs(r)
        T = C_T * DT_A / (C_T + A)
        S = F_S_REF / A
        buoy = ALPHA * T - BETA * S
        mode = "thermal" if buoy > 0 else "haline"
        print(f"  {r:+10.6f}   {T:9.3f}   {S:9.4f}   {buoy:+.6e}       {mode}")
    print(f"\n  number of steady states = {roots.size}.")
    for r in roots:
        print(f"    q = {r:.6f} 1/yr -> overturning period {1 / r:8.1f} yr, "
              f"|residual| = {abs(residual(r, F_S_REF)):.2e}")

    section("2. Hysteresis: scanning the freshwater forcing")
    print("  F_S is the strength of the freshwater forcing.  It is the control")
    print("  parameter for the collapse of the thermal mode.")
    print("\n   F_S ((g/kg)/yr)   states   q values (1/yr)")
    prev = None
    for f_s in np.arange(0.001, 0.081, 0.005):
        rr = steady_states(f_s)
        txt = ", ".join(f"{r:.6f}" for r in rr) if rr.size else "none"
        marker = ""
        if prev is not None and rr.size != prev:
            marker = "   <-- branch count changes"
        print(f"  {f_s:15.3f}   {rr.size:6d}   {txt}{marker}")
        prev = rr.size

    lo, hi = 0.001, 0.20
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if steady_states(mid).size > 1:
            lo = mid
        else:
            hi = mid
    f_fold = lo
    rr_fold = steady_states(f_fold)
    print(f"\n  the two branches survive up to F_S = {f_fold:.5f} (g/kg)/yr and")
    print(f"  meet there at q = {', '.join(f'{r:.6f}' for r in rr_fold)} 1/yr;")
    print("  beyond that value no positive-q steady state exists at all.  That is a")
    print("  SADDLE-NODE bifurcation: at the fold one eigenvalue of the Jacobian")
    print("  passes through zero, which section 3 confirms.")
    print("  For stronger freshwater forcing there is NO positive-q steady state")
    print("  in this model: the thermal mode has ceased to exist.  Note carefully")
    print("  that this is a statement about the MODEL.  The real ocean's answer to")
    print("  'where is the threshold' is not contained in these two boxes.")

    section("3. Stability of each branch (linearised)")
    print("  A steady state is stable if both eigenvalues of the Jacobian have")
    print("  negative real part.")
    for f_s in (F_S_REF, f_fold, 0.001):
        print(f"\n  F_S = {f_s:.5f} (g/kg)/yr")
        rr = steady_states(f_s)
        if rr.size == 0:
            print("    no steady state")
        for r in rr:
            J, T, S = jacobian(r, f_s)
            ev = np.linalg.eigvals(J)
            kind = "stable" if np.all(ev.real < 0) else "unstable"
            print(f"    q = {r:+.6f}: eigenvalues {ev[0]:+.5f}, {ev[1]:+.5f} "
                  f"-> {kind}")
    print("\n  On the main branch the eigenvalues are real and negative, so the")
    print("  approach to equilibrium is monotone.  Where a pair becomes complex")
    print("  the return would oscillate; that is the box model's only route to")
    print("  internal variability, and it is not a substitute for the real ocean's.")

    section("4. The advective-diffusive thermocline scale")
    print("  Steady balance  w dT/dz = kappa d2T/dz2,  T(0) = T0, T(inf) = T_deep")
    print("  gives  T(z) = T_deep + (T0 - T_deep) exp(-z/delta),  delta = kappa/w.")
    kappa = 1.0e-4       # m^2/s, vertical diffusivity (chosen teaching value)
    print(f"\n  kappa = {kappa:.2e} m^2/s")
    print("\n   w (m/s)     w (m/yr)   delta (m)   Pe = wH/kappa (H = 4000 m)")
    H = 4000.0
    for w in (3.17e-8, 1.0e-7, 3.17e-7, 1.0e-6):
        print(f"  {w:9.3e}   {w * 3.156e7:9.3f}   {kappa / w:9.1f}   "
              f"{w * H / kappa:18.1f}")
    w_ref = 1.0e-7
    delta_ref = kappa / w_ref
    print(f"\n  chosen w = {w_ref:.2e} m/s ({w_ref * 3.156e7:.2f} m/yr) "
          f"-> delta = {delta_ref:.0f} m")
    print("  Substituting the analytic solution back into the ODE:")
    T0, T_deep = 25.0, 2.0
    worst = 0.0
    print("\n     z (m)   w dT/dz (K/s)   kappa d2T/dz2 (K/s)   residual (K/s)")
    for zz in (0.0, 250.0, 500.0, 1000.0, 2000.0, 4000.0):
        dTdz = -(T0 - T_deep) / delta_ref * np.exp(-zz / delta_ref)
        d2Tdz2 = (T0 - T_deep) / delta_ref ** 2 * np.exp(-zz / delta_ref)
        lhs, rhs = w_ref * dTdz, kappa * d2Tdz2
        worst = max(worst, abs(lhs - rhs))
        print(f"  {zz:7.0f}   {lhs:14.4e}   {rhs:20.4e}   {lhs - rhs:14.3e}")
    print(f"\n  worst residual = {worst:.3e} K/s: the exponential thermocline is an")
    print("  exact solution, which is exactly why it is dangerous.  It contains one")
    print("  number (kappa/w) and it assumes kappa is constant, which a turbulent")
    print("  ocean is not.  An exact solution of a wrong equation is still wrong.")

    section("5. Overturning heat transport")
    RHO = 1025.0          # kg/m^3
    CP = 3994.0           # J/(kg K), conventional reference value for seawater
    print(f"  Q = rho c_p Psi dT with rho = {RHO:.0f} kg/m^3 and "
          f"c_p = {CP:.0f} J/(kg K)")
    print("\n   Psi (Sv)   dT (degC)   Q (PW)")
    for psi_sv in (5.0, 10.0, 15.0, 20.0):
        for dT in (10.0, 15.0, 20.0):
            print(f"  {psi_sv:10.1f}   {dT:10.1f}   "
                  f"{RHO * CP * psi_sv * 1e6 * dT / 1e15:6.3f}")
    q_ref = RHO * CP * 15.0e6 * 15.0
    print(f"\n  for Psi = 15 Sv and dT = 15 degC, Q = {q_ref:.4e} W = "
          f"{q_ref / 1e15:.2f} PW.")
    print("  The observable is a PRODUCT of a circulation and a temperature")
    print("  contrast.  An independent heat-transport estimate constrains the")
    print("  product and says nothing on its own about the circulation.")

    section("6. Verification")
    print("(a) root residuals at the reference forcing:")
    for r in steady_states(F_S_REF):
        print(f"    q = {r:.8f} 1/yr, |F(q)| = {abs(residual(r, F_S_REF)):.3e}")
    print("(b) the |q| kink at q = 0: one-sided slopes of F are infinite and of")
    print("    opposite sign, so F is continuous but not differentiable there.")
    for q in (1e-6, 2e-6, -1e-6, -2e-6):
        dq = 1e-9
        slope = (residual(q + dq, F_S_REF) - residual(q - dq, F_S_REF)) / (2 * dq)
        print(f"    q = {q:+.1e}: F = {residual(q, F_S_REF):+.6e}, "
              f"dF/dq = {slope:+.4e}")
    print("    A Newton method started near q = 0 can therefore be thrown out of")
    print("    the basin.  The sign-change scan used here cannot.")
    print("(c) dimensional check of the heat transport:")
    print("    [rho c_p Psi dT] = (kg/m^3)(J/(kg K))(m^3/s)(K) = J/s = W.  ok")
    print("(d) the steady-state relations reproduce the defining equations:")
    for r in steady_states(F_S_REF):
        A = abs(r)
        T, S = C_T * DT_A / (C_T + A), F_S_REF / A
        print(f"    q = {r:.6f}: |q| S = {A * S:.6f} (should equal F_S = "
              f"{F_S_REF:.6f}), K_Q(alpha T - beta S) = "
              f"{K_Q * (ALPHA * T - BETA * S):.6f}")


if __name__ == "__main__":
    main()
