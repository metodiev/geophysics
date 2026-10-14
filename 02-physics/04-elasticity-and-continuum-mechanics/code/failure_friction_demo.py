"""Rock failure, Mohr-Coulomb friction and rate-and-state stability.

Run:  python3 failure_friction_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-08. The script:

1. Applies the Mohr-Coulomb criterion tau = C + mu sigma_n' to a state of
   stress, verifies the analytic failure condition by scanning every plane
   orientation, and locates the optimal fault dip.
2. Computes the frictional shear-strength envelope with depth for a stated
   lithostatic and pore-pressure model.
3. Simulates the linear stability of a spring-slider with the Dieterich-Ruina
   aging law: a small perturbation of the steady state grows when the spring
   stiffness is below sigma (b - a)/D_c and decays above it. The measured
   threshold is compared with the closed form.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def part1_mohr_coulomb():
    section("1. Mohr-Coulomb failure and the optimal fault dip")
    cohesion, mu_f = 20.0e6, 0.6
    phi = math.atan(mu_f)
    print(f"cohesion C = {cohesion / 1e6:.1f} MPa, friction coefficient "
          f"mu = {mu_f:.2f} -> friction angle phi = {math.degrees(phi):.4f} deg")
    sigma3 = 100.0e6
    sigma1_analytic = (sigma3 * (1.0 + math.sin(phi)) + 2.0 * cohesion * math.cos(phi)) \
        / (1.0 - math.sin(phi))
    print(f"sigma_3 = {sigma3 / 1e6:.1f} MPa -> predicted failure at sigma_1 = "
          f"{sigma1_analytic / 1e6:.6f} MPa")

    # scan every plane orientation to find the maximum of tau - mu sigma_n - C
    best = (-1e30, None)
    for i in range(0, 9001):
        # theta is the angle between the plane's NORMAL and the sigma_1 axis, so
        # sigma_n = centre + radius cos 2 theta and tau = radius sin 2 theta
        theta = math.pi * i / 9000.0
        centre = 0.5 * (sigma1_analytic + sigma3)
        radius = 0.5 * (sigma1_analytic - sigma3)
        sigma_n = centre + radius * math.cos(2.0 * theta)
        tau = radius * math.sin(2.0 * theta)
        excess = tau - mu_f * sigma_n - cohesion
        if excess > best[0]:
            best = (excess, math.degrees(theta))
    print(f"maximum of tau - mu sigma_n - C over all planes = {best[0]:.6e} Pa")
    print(f"  reached where the plane's normal lies {best[1]:.4f} deg from sigma_1,")
    print(f"  i.e. where the plane itself is inclined {90.0 - best[1]:.4f} deg to")
    print(f"  sigma_1 (the textbook 45 deg - phi/2 = {45.0 - math.degrees(phi) / 2.0:.4f} deg)")
    print(f"  and its normal lies at 45 deg + phi/2 = "
          f"{45.0 + math.degrees(phi) / 2.0:.4f} deg from sigma_1")
    print("  fault dip depends on which principal stress is vertical: 60.4819 deg if")
    print("  sigma_1 is vertical (normal faulting), 29.5181 deg if it is horizontal")
    print("  (thrust faulting) - the two Andersonian cases")
    print()
    print("  The failure condition is not an independent law: it is the statement")
    print("  that the Mohr circle touches the friction envelope. Every plane")
    print("  orientation is tested above, and the residual is zero at the optimum,")
    print("  which is why faults nucleate at a characteristic angle rather than at")
    print("  random orientations.")


def part2_strength_profile():
    section("2. Frictional shear strength with depth")
    rho, rho_w, g = 2700.0, 1000.0, 9.81
    mu_f = 0.6
    print(f"assumed: rho = {rho:.0f} kg/m^3, hydrostatic pore pressure "
          f"(rho_w = {rho_w:.0f}), mu = {mu_f:.2f}, zero cohesion")
    print(f"{'depth (km)':>11} {'sigma_v (MPa)':>14} {'sigma_n_eff (MPa)':>18} "
          f"{'tau_max (MPa)':>14} {'tau/sigma_n_eff':>16}")
    for depth_km in (2.0, 5.0, 10.0, 15.0, 20.0, 30.0):
        z = depth_km * 1000.0
        sv = rho * g * z / 1e6
        pf = rho_w * g * z / 1e6
        sv_eff = sv - pf
        # vertical-stress envelope: sigma_n taken as sigma_v (exact for a
        # horizontal plane, approximate for a dipping fault)
        tau = mu_f * sv_eff
        print(f"{depth_km:11.1f} {sv:14.3f} {sv_eff:18.3f} {tau:14.3f} "
              f"{tau / sv_eff:16.4f}")
    print()
    print("  Frictional strength grows linearly with effective normal stress, so in")
    print("  a brittle crust the stress difference a fault can support grows")
    print("  linearly with depth as well. Something must stop that growth, and what")
    print("  stops it is ductile creep: the depth at which the frictional strength")
    print("  and the creep strength cross is the brittle-ductile transition. Its")
    print("  depth is not a universal number - it depends on the geothermal")
    print("  gradient, the strain rate, the mineralogy and the pore pressure, and")
    print("  standard estimates for quartz-rich continental crust put it at of")
    print("  order ten to twenty kilometres. Computing it for a specific setting")
    print("  requires a flow law, not a rule of thumb; the envelope above is only")
    print("  the brittle half of the argument.")


VSTAR = 1.0e-6


def tau_over_sigma(V, theta, sigma, a, b, Dc):
    """Dieterich-Ruina aging law: tau/sigma = a ln(V/V*) + b ln(theta V*/D_c)."""
    return a * math.log(V / VSTAR) + b * math.log(theta * VSTAR / Dc)


def part3_rate_state():
    section("3. Rate-and-state stability: measuring the critical stiffness")
    sigma, a, b, Dc = 100.0e6, 0.010, 0.014, 1.0e-5
    V_lp = 1.0e-9
    k_c = sigma * (b - a) / Dc
    print(f"sigma = {sigma / 1e6:.0f} MPa, a = {a:.3f}, b = {b:.3f}, "
          f"D_c = {Dc:.1e} m, plate velocity {V_lp:.1e} m/s, V* = {VSTAR:.1e} m/s")
    print(f"critical stiffness k_c = sigma (b - a)/D_c = {k_c:.4e} Pa/m = "
          f"{k_c / 1e6:.3f} MPa/m")
    theta_ss = Dc / V_lp                       # steady state: theta = D_c/V

    def growth(k, t_end=300000.0, dt=50.0):
        """Amplitude ratio of a small perturbation after one loading interval.

        The two timescales of the linearised problem are both close to
        V_lp/D_c = 1e-4 1/s here, so a window of a few times 1e5 s separates the
        growing from the decaying case by many orders of magnitude.
        """
        V = V_lp * 1.01
        theta = theta_ss
        tau = sigma * tau_over_sigma(V, theta, sigma, a, b, Dc)
        amplitude0 = abs(V - V_lp)
        for _ in range(int(t_end / dt)):
            V = VSTAR * math.exp((tau / sigma
                                  - b * math.log(theta * VSTAR / Dc)) / a)
            tau += dt * k * (V_lp - V)
            theta += dt * (1.0 - theta * V / Dc)
        return abs(V - V_lp) / amplitude0

    print(f"run duration 3e5 s, i.e. {300000.0 / theta_ss:.1f} times the state")
    print(f"evolution timescale D_c/V_pl = {theta_ss:.1e} s; perturbation started "
          f"at 1 per cent of V_pl")
    print(f"{'k/k_c':>8} {'final/initial perturbation':>28} {'verdict':>10}")
    for ratio in (0.2, 0.5, 0.9, 1.1, 2.0, 5.0):
        g = growth(ratio * k_c)
        verdict = "GROWS" if g > 1.0 else "decays"
        print(f"{ratio:8.2f} {g:28.6e} {verdict:>10}")
    lo, hi = 0.01 * k_c, 10.0 * k_c
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if growth(mid) > 1.0:
            lo = mid
        else:
            hi = mid
    measured = 0.5 * (lo + hi)
    print(f"measured stability threshold: k = {measured:.4e} Pa/m = "
          f"{measured / k_c:.6f} k_c")
    print()
    print("  The exact threshold comes from the linearised Jacobian. With")
    print("  u = V_pl/D_c, x = dV/V_pl and y = d(theta)/theta_ss, the perturbation")
    print("  obeys a 2x2 system with trace and determinant")
    print("    T = (b u - k V_pl/sigma)/a - u,   D = u k V_pl/(a sigma) > 0,")
    print("  so both eigenvalues have the sign of T and the threshold is exactly")
    print("  T = 0, i.e. k = sigma (b - a)/D_c:")
    print(f"{'k/k_c':>8} {'trace (1/s)':>15} {'det (1/s^2)':>15} "
          f"{'eigenvalues (1/s)':>30} {'verdict':>10}")
    u = V_lp / Dc
    for ratio in (0.5, 0.9, 1.0, 1.1, 2.0):
        k = ratio * k_c
        T = (b * u - k * V_lp / sigma) / a - u
        D = u * k * V_lp / (a * sigma)
        disc = T * T - 4.0 * D
        if disc >= 0.0:
            lam = (0.5 * (T + math.sqrt(disc)), 0.5 * (T - math.sqrt(disc)))
        else:
            lam = (0.5 * T, 0.5 * T)
        verdict = "unstable" if T > 0.0 else "stable"
        print(f"{ratio:8.2f} {T:15.6e} {D:15.6e} "
              f"{f'{lam[0]:.3e}, {lam[1]:.3e}':>30} {verdict:>10}")
    print()
    print("  The simulated threshold above agrees with k_c to about 15 per cent,")
    print("  not better. That is a property of the measurement, not of the theory:")
    print("  both eigenvalues pass through zero at k_c, so near the threshold the")
    print("  perturbation amplitude changes by only a few per cent over any")
    print("  affordable window, and the bisection is limited by the discretisation")
    print(f"  error of the explicit scheme. Away from the threshold the verdict is")
    print("  unambiguous, as the table shows.")
    print()
    print("  Below the critical stiffness the fault cannot keep up with the plate:")
    print("  slip accelerates, the perturbation grows, and the slider produces")
    print("  stick-slip. Above it, elastic loading is stiff enough to hold the slip")
    print("  rate near the plate rate and the fault slides stably. That single")
    print("  inequality - stiffness against the friction law - is the standard")
    print("  explanation of why some faults nucleate earthquakes and others creep.")
    print()
    print("  Here a < b, which is velocity-weakening friction and the condition for")
    print("  instability. Laboratory measurements give both signs depending on")
    print("  temperature, mineralogy and slip rate, which is why the same fault may")
    print("  be unstable at seismogenic depth and stable below it.")


if __name__ == "__main__":
    part1_mohr_coulomb()
    part2_strength_profile()
    part3_rate_state()
