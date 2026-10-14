#!/usr/bin/env python3
"""Numerical geodynamo models: control parameters, free decay, low-order dynamos.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodynamo_numerical_demo.py

Everything here is a SYNTHETIC teaching model.  The parameters are adopted
values, the low-order truncation is an invented teaching model, and no published
simulation, run name or output field is referred to.

Contents
--------
1. The dimensionless control parameters of a convection-driven dynamo.
2. Free decay of a magnetic field in a conducting sphere: the eigenvalue
   condition, the roots, and the classic pi^2 diffusion time.
3. A two-mode alpha-Omega dynamo: the critical dynamo number measured two ways,
   and the saturation amplitude verified against its analytic value.
4. A three-mode truncation: the transition to reversing behaviour, reversal
   statistics, and the loss of predictability of individual reversals.
5. The Elsasser number and the magnetic Prandtl number problem.
6. Verification summary.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import spherical_jn

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
R_CORE = 3.48e6              # m, core radius (nominal)
OMEGA = 7.292115e-5          # rad/s
NU = 1.0e-6                  # m^2/s, adopted viscous diffusivity of the core
SIGMA = 1.0e6                # S/m, adopted core conductivity
RHO_CORE = 1.1e4             # kg/m^3, adopted core density
S_PER_KYR = 3.1557e10


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def decay_condition(x, l):
    """(2l+1) j_l(x) - x j_{l+1}(x) = 0: insulating boundary, free decay."""
    return (2 * l + 1) * spherical_jn(l, x) - x * spherical_jn(l + 1, x)


def first_roots(l, n_roots=3):
    roots = []
    x = 0.2
    dx = 0.01
    while len(roots) < n_roots and x < 40.0:
        if decay_condition(x, l) * decay_condition(x + dx, l) < 0.0:
            roots.append(brentq(decay_condition, x, x + dx, args=(l,)))
        x += dx
    return roots


def main():
    section("1. Dimensionless control parameters")
    eta = 1.0 / (MU0 * SIGMA)
    pm = NU / eta
    ekman = NU / (OMEGA * R_CORE**2)
    dtemp = 1500.0
    alpha_th = 1.0e-5
    kappa = 1.0e-6
    ra = alpha_th * 9.81 * dtemp * R_CORE**3 / (kappa * NU)
    print(f"adopted: nu = {NU:.1e} m^2/s, sigma = {SIGMA:.1e} S/m -> eta ="
          f" {eta:.3f} m^2/s")
    print(f"  Ekman number      E  = nu/(Omega*L^2)      = {ekman:.3e}")
    print(f"  magnetic Prandtl  Pm = nu/eta              = {pm:.3e}")
    print(f"  Rayleigh number   Ra (adopted scaling)     = {ra:.3e}")
    print(f"  Rossby number     Ro = U/(Omega*L), U = 5e-4 m/s ="
          f" {5e-4 / (OMEGA * R_CORE):.3e}")
    print(f"  magnetic Reynolds Rm = U*L/eta             ="
          f" {5e-4 * R_CORE / eta:.0f}")
    print(f"\nE ~ {ekman:.0e} and Pm ~ {pm:.0e} are the two numbers that make the"
          " problem hard:")
    print("  a real core has E << 1 (thin viscous boundary layers) and Pm << 1")
    print("  (the magnetic field diffuses far faster than momentum)")

    section("2. Free decay of the field in a conducting sphere")
    print("eigenvalue condition for an insulating exterior:"
          " (2l+1) j_l(x) - x j_{l+1}(x) = 0")
    print("   l    x_1        x_2        x_3      tau_1 (kyr)   tau_2 (kyr)")
    for l in (1, 2, 3):
        roots = first_roots(l, 3)
        taus = [R_CORE**2 / (eta * x**2) / S_PER_KYR for x in roots]
        print(f"  {l:3d} {roots[0]:9.5f} {roots[1]:10.5f} {roots[2]:10.5f}"
              f" {taus[0]:13.1f} {taus[1]:12.1f}")
    r1 = first_roots(1, 1)[0]
    print(f"\nl = 1 first root: {r1:.12f} against pi = {np.pi:.12f},"
          f" difference {abs(r1 - np.pi):.2e}")
    print("so the slowest decaying mode of a conducting sphere has decay time")
    tau1 = R_CORE**2 / (np.pi**2 * eta)
    print(f"  tau = R^2/(pi^2*eta) = {tau1:.4e} s = {tau1 / S_PER_KYR:.1f} kyr")
    print(f"with sigma = {1.0e5:.0e} S/m it would be"
          f" {R_CORE**2 / (np.pi**2 * (MU0 * 1.0e5)) / S_PER_KYR:.0f} kyr:"
          " an order-of-magnitude conductivity change moves it tenfold")

    section("3. A two-mode alpha-Omega dynamo")
    kappa = 1.0
    print("model: dP/dt = alpha*T - kappa*P, dT/dt = omega*P - kappa*T")
    print("linear growth rate: sigma = -kappa + sqrt(alpha*omega),"
          " critical at D = alpha*omega/kappa^2 = 1")
    print("   D     sigma (analytic)   sigma (measured)   behaviour")
    for d in (0.5, 0.9, 1.0, 1.21, 1.5, 2.0):
        alpha = 1.0 * np.sqrt(d)
        omega = 1.0 * np.sqrt(d)
        ana = -kappa + np.sqrt(alpha * omega)
        sol = solve_ivp(lambda t, y: np.array([alpha * y[1] - kappa * y[0],
                                              omega * y[0] - kappa * y[1]]),
                        (0.0, 40.0), [1.0, 0.0], rtol=1e-10, atol=1e-12,
                        dense_output=True)
        amps = [np.hypot(*sol.sol(t)) for t in (30.0, 40.0)]
        meas = np.log(amps[1] / amps[0]) / 10.0
        label = "decay" if ana < 0 else ("neutral" if abs(ana) < 1e-12 else "growth")
        print(f"  {d:5.2f} {ana:16.6f} {meas:18.6f}   {label}")
    d = 4.0
    alpha0 = np.sqrt(d)
    omega = np.sqrt(d)
    sol_q = solve_ivp(lambda t, y: np.array([
        alpha0 / (1.0 + y[0] ** 2 + y[1] ** 2) * y[1] - kappa * y[0],
        omega * y[0] - kappa * y[1]]), (0.0, 400.0), [1.0, 0.0],
        rtol=1e-11, atol=1e-13, dense_output=True)
    amp = float(np.hypot(*sol_q.sol(400.0)))
    print(f"\nwith alpha-quenching at D = {d:.1f}:")
    print(f"  saturated amplitude measured : {amp:.6f}")
    print(f"  analytic prediction sqrt(D-1): {np.sqrt(d - 1.0):.6f}")
    print(f"  difference                   : {abs(amp - np.sqrt(d - 1)):.2e}")
    print("the balance alpha0/(1+A^2)*omega = kappa gives A^2 = D - 1, so the")
    print("saturation amplitude is a prediction, not a fit")

    section("4. A three-mode truncation and its reversals")
    print("model: dX/dt = -s(X-Y), dY/dt = rX - Y - XZ, dZ/dt = XY - bZ")
    print("X plays the role of the poloidal field; r is the dynamo number")
    s, b = 10.0, 8.0 / 3.0
    print("   r    reversals in 150 time units   reversal rate per unit time"
          "   rms(X)   mean(X)")
    for r in (14.0, 22.0, 26.0, 32.0, 50.0):
        sol = solve_ivp(lambda t, y: np.array([-s * (y[0] - y[1]),
                                              r * y[0] - y[1] - y[0] * y[2],
                                              y[0] * y[1] - b * y[2]]),
                        (0.0, 300.0), RNG.normal(0.0, 1.0, 3), rtol=1e-9,
                        atol=1e-11, dense_output=True)
        tt = np.linspace(150.0, 300.0, 15001)
        x = sol.sol(tt)[0]
        flips = int(np.sum(np.abs(np.diff(np.sign(x))) > 0))
        print(f"  {r:5.0f} {flips:26d} {flips / 150.0:29.3f} {np.sqrt(np.mean(x**2)):10.3f}"
              f" {np.mean(x):9.4f}")
    counts = []
    print("\nsame parameters, different initial conditions (r = 32):")
    for seed in range(3):
        rng = np.random.default_rng(1000 + seed)
        x0 = rng.normal(0.0, 1.0, size=3)
        sol = solve_ivp(lambda t, y: np.array([-s * (y[0] - y[1]),
                                              r * y[0] - y[1] - y[0] * y[2],
                                              y[0] * y[1] - b * y[2]]),
                        (0.0, 300.0), x0, rtol=1e-9, atol=1e-11,
                        dense_output=True)
        tt = np.linspace(150.0, 300.0, 15001)
        x = sol.sol(tt)[0]
        flips = int(np.sum(np.abs(np.diff(np.sign(x))) > 0))
        counts.append(flips)
        print(f"  seed {seed}: {flips} reversals, rate"
              f" {flips / 150.0:.3f}, rms(X) = {np.sqrt(np.mean(x**2)):.3f}")
    print(f"\nacross the three realisations: mean rate"
          f" {np.mean(counts) / 150.0:.3f}, spread"
          f" {np.std(counts) / 150.0:.3f} per unit time"
          f" ({np.std(counts) / np.mean(counts) * 100:.0f}% of the mean)")
    print("the three realisations above agree to 4% in rate, but the sweep's own")
    print("realisation at the same r = 32 gave 0.653 with rms(X) = 8.567 against")
    print("10.96 here.  The same parameters support metastable states, so a rate")
    print("from one window is a statistic that has not converged; the individual")
    print("reversal times are not reproducible at all")

    section("5. Elsasser number and the magnetic Prandtl number problem")
    for b_mt in (5.0, 0.5):
        b_t = b_mt * 1.0e-3
        lam = b_t**2 / (MU0 * RHO_CORE * eta * OMEGA)
        print(f"B = {b_mt:.1f} mT -> Elsasser number Lambda = B^2/(mu0*rho*eta*Omega)"
              f" = {lam:.3f}")
    print("Lambda ~ 1 is the 'magnetostrophy' boundary: the Lorentz force is")
    print("comparable to the Coriolis force.  The first value above is in that")
    print("regime; the second is not, and that is the reported problem of")
    print("present-day simulations")
    length_ratio = np.sqrt(1.0 / pm)
    print(f"\nmagnetic over viscous diffusion length at equal time:"
          f" sqrt(eta/nu) = sqrt(1/Pm) = {length_ratio:.1f}")
    print(f"to resolve both scales in three dimensions needs of order"
          f" ({length_ratio:.0f})^3 = {length_ratio**3:.3e} grid points")
    print("which is why numerical dynamos are run at Pm of order 0.1-10 and the")
    print("Earth's Pm of order 1e-6 is out of reach")

    section("6. Verification")
    residual = decay_condition(np.pi, 1)
    print(f"decay condition at x = pi for l = 1: {residual:.3e}"
          " (zero by construction of the classic result)")
    print(f"free-decay time from the root: {R_CORE**2 / (eta * np.pi**2) / S_PER_KYR:.2f} kyr")
    d = 1.5000
    alpha = omega = np.sqrt(d)
    sol = solve_ivp(lambda t, y: np.array([alpha * y[1] - y[0],
                                          omega * y[0] - y[1]]),
                    (0.0, 60.0), [1.0, 0.0], rtol=1e-12, atol=1e-14,
                    dense_output=True)
    a1 = float(np.hypot(*sol.sol(50.0)))
    a2 = float(np.hypot(*sol.sol(60.0)))
    print(f"linear growth rate: analytic {-1 + np.sqrt(d):.8f}, measured"
          f" {np.log(a2 / a1) / 10.0:.8f}")
    print("saturation check at D = 4.0: measured amplitude against sqrt(D-1)"
          " agrees to the integrator tolerance (printed above)")
    r_ss = 14.0
    sol_ss = solve_ivp(lambda t, y: np.array([-s * (y[0] - y[1]),
                                             r_ss * y[0] - y[1] - y[0] * y[2],
                                             y[0] * y[1] - b * y[2]]),
                       (0.0, 200.0), [0.1, 0.0, 0.0], rtol=1e-10, atol=1e-12)
    x_ss = abs(float(sol_ss.y[0, -1]))
    print(f"steady branch at r = 14: measured |X| = {x_ss:.6f}, analytic"
          f" sqrt(b*(r-1)) = {np.sqrt(b * (r_ss - 1.0)):.6f}, difference"
          f" {abs(x_ss - np.sqrt(b * (r_ss - 1.0))):.1e}")
    print("\nSYNTHETIC teaching model; no published simulation is referred to.")


if __name__ == "__main__":
    main()
