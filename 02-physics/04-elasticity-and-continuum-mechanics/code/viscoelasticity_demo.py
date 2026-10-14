"""Viscoelasticity: relaxation, creep, the standard linear solid and the
Maxwell time of the mantle.

Run:  python3 viscoelasticity_demo.py
Requires: Python standard library only.

Companion to lesson 02-04-07. The script:

1. Integrates a Maxwell element in stress relaxation and compares the result
   with the analytic exp(-t/tau), then runs a creep test and recovers the
   viscosity from the steady strain rate.
2. Integrates a Kelvin-Voigt element and verifies the delayed elastic creep
   curve.
3. Computes the complex modulus of a standard linear solid, its Q(omega) and its
   velocity dispersion, and tests the nearly-constant-Q relation that couples
   them.
4. Computes the Maxwell time for upper-mantle viscosity and uses it to show that
   the same rock is elastic for seismic waves and viscous for postglacial
   rebound - the regime-of-validity statement in its starkest form.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rk4(f, y, t, dt):
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, [yi + 0.5 * dt * ki for yi, ki in zip(y, k1)])
    k3 = f(t + 0.5 * dt, [yi + 0.5 * dt * ki for yi, ki in zip(y, k2)])
    k4 = f(t + dt, [yi + dt * ki for yi, ki in zip(y, k3)])
    return [yi + dt * (a + 2.0 * b + 2.0 * c + d) / 6.0
            for yi, a, b, c, d in zip(y, k1, k2, k3, k4)]


def part1_maxwell():
    section("1. Maxwell element: stress relaxation and creep")
    mu_0, eta = 30.0e9, 1.0e18            # Pa, Pa s
    tau = eta / mu_0
    print(f"shear modulus mu = {mu_0 / 1e9:.1f} GPa, viscosity eta = "
          f"{eta:.1e} Pa s")
    print(f"Maxwell relaxation time tau = eta/mu = {tau:.1f} s = "
          f"{tau / 86400.0 / 365.25:.4f} years")
    print("stress relaxation at constant strain: sigma(t) = sigma_0 exp(-t/tau)")
    print(f"{'t/tau':>8} {'sigma numeric (GPa)':>20} {'sigma analytic (GPa)':>21} "
          f"{'difference':>11}")
    sigma0 = 1.0e6
    f = lambda t, y: [-mu_0 / eta * y[0]]
    dt = tau / 2000.0
    worst = 0.0
    times, y = 0.0, [sigma0]
    for step in range(6001):
        if step % 1000 == 0:
            exact = sigma0 * math.exp(-times / tau)
            worst = max(worst, abs(y[0] - exact))
            print(f"{times / tau:8.2f} {y[0] / 1e6:20.9f} {exact / 1e6:21.9f} "
                  f"{abs(y[0] - exact):11.3e}")
        y = rk4(f, y, times, dt)
        times += dt
    print(f"max |numerical - analytic| over 3 tau = {worst:.3e} Pa")

    print()
    print("creep at constant stress: strain = sigma_0/mu + sigma_0 t/eta")
    sigma = 1.0e6
    strain = sigma / mu_0
    t = 0.0
    dt = tau / 1000.0
    steps = 5000
    print(f"{'t/tau':>8} {'strain numeric':>16} {'analytic':>16} "
          f"{'implicit strain rate (1/s)':>28}")
    previous = strain
    for step in range(steps + 1):
        if step % 1000 == 0 and step > 0:
            print(f"{t / tau:8.2f} {strain:16.9e} "
                  f"{sigma / mu_0 + sigma * t / eta:16.9e} "
                  f"{(strain - previous) / (1000 * dt):28.6e}")
            previous = strain
        # d(eps)/dt = sigma/eta for the Maxwell dashpot
        strain += dt * sigma / eta
        t += dt
    print(f"implicit viscosity recovered from the steady strain rate: "
          f"{sigma / ((strain - sigma / mu_0) / t):.6e} Pa s (input {eta:.1e})")
    print()
    print("  A Maxwell element has an instantaneous elastic response and then flows")
    print("  at a constant rate. The ratio of the two timescales is the relaxation")
    print("  time: for t << tau it is a solid, for t >> tau it is a fluid. No other")
    print("  sentence is more important for reading mantle rheology.")


def part2_kelvin_voigt():
    section("2. Kelvin-Voigt element: delayed elasticity")
    mu_0, eta = 30.0e9, 1.0e18
    tau = eta / mu_0
    print(f"mu = {mu_0 / 1e9:.1f} GPa, eta = {eta:.1e} Pa s, tau = {tau:.1f} s")
    print("creep: eps(t) = (sigma_0/mu) (1 - exp(-t/tau)); no instantaneous strain")
    sigma0 = 1.0e6
    print(f"{'t/tau':>8} {'strain numeric':>17} {'analytic':>17} {'difference':>11}")
    eps = 0.0
    dt = tau / 2000.0
    worst = 0.0
    for step in range(6001):
        if step % 1000 == 0:
            t = step * dt
            exact = sigma0 / mu_0 * (1.0 - math.exp(-t / tau))
            worst = max(worst, abs(eps - exact))
            print(f"{t / tau:8.2f} {eps:17.9e} {exact:17.9e} "
                  f"{abs(eps - exact):11.3e}")
        # backward difference of  eps' + eps/tau = sigma0/eta
        eps = (eps + dt * sigma0 / eta) / (1.0 + dt / tau)
    print(f"max |numerical - analytic| = {worst:.3e}")
    print()
    print("  Kelvin-Voigt has no instantaneous elastic response and a bounded creep")
    print("  strain: it is a solid with a dashpot in parallel, so the delay is")
    print("  elastic, not flow. A real rock is closer to a standard linear solid,")
    print("  which has both.")


def part3_sls():
    section("3. Standard linear solid: Q(omega) and the dispersion it forces")
    mu_ref = 30.0e9
    rho = 2600.0
    q0 = 30.0
    f0 = 10.0
    omega0 = 2.0 * math.pi * f0
    # M*(w) = mu_ref (1 + i w tau_e) / (1 + i w tau_s), the Zener standard
    # linear solid written with its relaxed (low-frequency) modulus as the
    # prefactor. The two relaxation times satisfy tau_e tau_s = 1/omega0^2, so
    # the Q minimum sits exactly at f0.
    tau_e = (math.sqrt(1.0 + 1.0 / q0 ** 2) + 1.0 / q0) / omega0
    tau_s = (math.sqrt(1.0 + 1.0 / q0 ** 2) - 1.0 / q0) / omega0
    delta = tau_e / tau_s - 1.0

    def modulus(omega):
        m = mu_ref * (1.0 + 1j * omega * tau_e) / (1.0 + 1j * omega * tau_s)
        return m.real, m.imag

    m1_0, m2_0 = modulus(omega0)
    v0 = math.sqrt(m1_0 / rho)
    print(f"relaxed modulus M(0) = {mu_ref / 1e9:.6f} GPa, unrelaxed modulus "
          f"M(inf) = {mu_ref * tau_e / tau_s / 1e9:.6f} GPa, "
          f"contrast Delta = {delta:.9f}")
    print(f"Q minimum = {q0:.1f} at f0 = {f0:.0f} Hz, V(f0) = {v0:.4f} m/s "
          f"(rho = {rho:.0f} kg/m^3)")
    print(f"{'f (Hz)':>9} {'Q(f)':>10} {'V (m/s)':>11} {'V/V0 - 1':>12} "
          f"{'ln(f/f0)/(pi Q)':>17} {'difference':>11}")
    for f in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0):
        omega = 2.0 * math.pi * f
        m1, m2 = modulus(omega)
        q = m1 / m2
        v = math.sqrt(m1 / rho)
        approx = math.log(f / f0) / (math.pi * q0)
        print(f"{f:9.1f} {q:10.4f} {v:11.4f} {v / v0 - 1:12.6f} "
              f"{approx:17.6f} {(v / v0 - 1) - approx:11.3e}")
    print()
    print("  Attenuation and dispersion are two faces of one anelastic response.")
    print("  The exact statement is the Kramers-Kronig relation, which forbids a")
    print("  material from attenuating without dispersing; the relation tested here")
    print("  is its nearly-constant-Q approximation, valid for Q >> 1 within a")
    print("  factor of a few of the reference frequency. Away from that regime it")
    print("  fails, as the last column shows.")
    print()
    print("  For a Maxwell solid the same calculation gives Q = omega tau exactly,")
    print("  which is verified by the numbers below:")
    eta_m, mu_m = 1.0e18, 30.0e9
    tau_m = eta_m / mu_m
    for f in (1.0, 100.0):
        omega = 2.0 * math.pi * f
        g = mu_m * (1j * omega * tau_m) / (1.0 + 1j * omega * tau_m)
        print(f"    f = {f:6.1f} Hz: Q = Re/Im = {g.real / g.imag:.6e}, "
              f"omega tau = {omega * tau_m:.6e}")
    print("  A Maxwell solid attenuates strongly at low frequency and becomes")
    print("  elastic at high frequency; it therefore cannot explain a nearly")
    print("  frequency-independent Q, which is why standard linear solids (or")
    print("  distributions of them) are used in seismology instead.")


def part4_regimes():
    section("4. The Maxwell time: same rock, two different materials")
    eta, mu = 1.0e21, 70.0e9             # model values for the upper mantle
    tau = eta / mu
    print(f"assumed upper-mantle values: eta = {eta:.1e} Pa s, mu = "
          f"{mu / 1e9:.0f} GPa")
    print(f"Maxwell time tau = eta/mu = {tau:.3e} s = {tau / 3.15576e7:.1f} years")
    for label, period in (("seismic wave", 1.0 / 30.0),
                          ("tidal cycle", 12.42 * 3600.0),
                          ("postglacial rebound", 1.0e4 * 3.15576e7)):
        omega = 2.0 * math.pi / period
        print(f"{label:>22}: period = {period:.3e} s, omega tau = "
              f"{omega * tau:.3e}, Q = omega tau = {omega * tau:.3e}")
    print()
    print("  At seismic frequencies omega tau is enormous, so the material behaves")
    print("  as an elastic solid with a very large Q - which is why seismic")
    print("  velocities are the elastic ones. Over a glacial cycle omega tau is of")
    print("  order 0.3, the material flows on the glacial timescale, and the same")
    print("  mantle that transmits")
    print("  shear waves responds to the removal of an ice sheet by viscous")
    print("  relaxation over thousands of years. The viscosity and the shear")
    print("  modulus are model values typical of the upper mantle, not measurements")
    print("  of a specific place, and both vary by orders of magnitude with")
    print("  temperature, pressure and water content.")


if __name__ == "__main__":
    part1_maxwell()
    part2_kelvin_voigt()
    part3_sls()
    part4_regimes()
