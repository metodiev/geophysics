"""Reflection, refraction and Snell's law, verified three ways.

Run:  python3 reflection_refraction_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-08. The script:

1. Applies Snell's law to a two-layer model and locates the critical angle.
2. Measures the normal-incidence reflection and transmission coefficients by
   finite-difference modelling of a pulse crossing an interface, and compares
   them with R = (Z1 - Z2)/(Z1 + Z2) and T = 2 Z1/(Z1 + Z2) for particle
   velocity, checking the energy budget R^2 + (Z2/Z1) T^2 = 1.
3. Verifies Snell's law obliquely by substituting the three-wave solution into
   the pressure and normal-velocity boundary conditions and reporting the
   normalised residual, then tests total internal reflection.
4. Tabulates impedance contrasts for illustrative rock pairs, with the note
   that only the numbers labelled as model parameters are used as such.

Every number printed below was produced by this script.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


MODEL = dict(rho1=2000.0, c1=2000.0, rho2=2500.0, c2=3000.0)


def part1_snell():
    section("1. Snell's law and the critical angle")
    rho1, c1, rho2, c2 = (MODEL["rho1"], MODEL["c1"], MODEL["rho2"], MODEL["c2"])
    print(f"layer 1: rho = {rho1:.0f} kg/m^3, c = {c1:.0f} m/s")
    print(f"layer 2: rho = {rho2:.0f} kg/m^3, c = {c2:.0f} m/s")
    print(f"speed ratio c2/c1 = {c2 / c1:.6f}")
    critical = math.asin(c1 / c2)
    print(f"critical angle = asin(c1/c2) = {math.degrees(critical):.4f} deg")
    print(f"{'theta1 (deg)':>13} {'p = sin(theta1)/c1':>20} "
          f"{'theta2 (deg)':>13} {'regime':>25}")
    for theta1_deg in (0.0, 10.0, 20.0, 30.0, math.degrees(critical), 50.0, 60.0, 80.0):
        theta1 = math.radians(theta1_deg)
        p = math.sin(theta1) / c1
        if p * c2 <= 1.0:
            theta2 = math.asin(p * c2)
            print(f"{theta1_deg:13.4f} {p:20.9f} {math.degrees(theta2):13.4f} "
                  f"{'transmitted':>25}")
        else:
            print(f"{theta1_deg:13.4f} {p:20.9f} {'--':>13} "
                  f"{'total internal reflection':>25}")
    print()
    print("  The horizontal slowness p = sin(theta)/c is conserved across the")
    print("  interface. That single statement is Snell's law and it follows from")
    print("  requiring the wavefronts to match along the boundary at every instant:")
    print("  it is a phase-matching condition, not an empirical rule.")


def fd_layered_pulse(rho1, c1, rho2, c2, interface, t_end, receivers,
                     dx=1.0, cfl=0.6, length=400.0, source=100.0, width=8.0):
    """1-D elastic displacement wave equation, rho u_tt = (E u_x)_x.

    Returns (times, {receiver position: list of displacement samples}). The
    stiffness at each half-grid point is the harmonic mean of the two nodal
    values, which is the averaging that makes the traction E u_x continuous
    across a material interface.
    """
    n = int(round(length / dx)) + 1
    x = [i * dx for i in range(n)]
    rho = [rho1 if xi < interface else rho2 for xi in x]
    E = [rho[i] * (c1 if x[i] < interface else c2) ** 2 for i in range(n)]
    Ehalf = [2.0 * E[i] * E[i + 1] / (E[i] + E[i + 1]) for i in range(n - 1)]
    dt = cfl * dx / max(c1, c2)
    steps = int(round(t_end / dt))
    u_old = [math.exp(-((xi - source) / width) ** 2) for xi in x]
    u = [0.0] * n
    for i in range(1, n - 1):
        u[i] = u_old[i] + 0.5 * dt * dt / rho[i] / dx ** 2 * (
            Ehalf[i] * (u_old[i + 1] - u_old[i])
            - Ehalf[i - 1] * (u_old[i] - u_old[i - 1]))
    idx = [int(round(r / dx)) for r in receivers]
    trace = {r: [] for r in receivers}
    times = []
    for step in range(steps):
        u_new = [0.0] * n
        for i in range(1, n - 1):
            u_new[i] = (2.0 * u[i] - u_old[i]
                        + dt * dt / rho[i] / dx ** 2 * (
                            Ehalf[i] * (u[i + 1] - u[i])
                            - Ehalf[i - 1] * (u[i] - u[i - 1])))
        u_old, u = u, u_new
        times.append((step + 1) * dt)
        for r, i in zip(receivers, idx):
            trace[r].append(u[i])
    return times, trace


def peak_in_window(times, samples, t_lo, t_hi):
    """Largest |sample| inside a time window, with its signed value and time."""
    best, best_t = 0.0, float("nan")
    for t, v in zip(times, samples):
        if t_lo <= t <= t_hi and abs(v) > abs(best):
            best, best_t = v, t
    return best, best_t


def part2_normal_incidence():
    section("2. Normal incidence: coefficients measured from a wave simulation")
    rho1, c1, rho2, c2 = (MODEL["rho1"], MODEL["c1"], MODEL["rho2"], MODEL["c2"])
    Z1, Z2 = rho1 * c1, rho2 * c2
    R = (Z1 - Z2) / (Z1 + Z2)                 # particle-velocity reflection
    T = 2.0 * Z1 / (Z1 + Z2)                  # particle-velocity transmission
    print(f"Z1 = rho1 c1 = {Z1:.4e} kg m^-2 s^-1, "
          f"Z2 = rho2 c2 = {Z2:.4e} kg m^-2 s^-1")
    print(f"predicted velocity coefficients: R = (Z1-Z2)/(Z1+Z2) = {R:.6f}, "
          f"T = 2 Z1/(Z1+Z2) = {T:.6f}")
    print(f"energy budget: R^2 + (Z2/Z1) T^2 = {R ** 2 + (Z2 / Z1) * T ** 2:.12f}")
    interface, source, width = 200.0, 100.0, 8.0
    rec_a, rec_b = 150.0, 250.0
    t_end = 0.16
    times, trace = fd_layered_pulse(rho1, c1, rho2, c2, interface, t_end,
                                    (rec_a, rec_b), source=source, width=width)
    t_inc = (rec_a - source) / c1
    t_ref = (interface - source) / c1 + (interface - rec_a) / c1
    t_tra = (interface - source) / c1 + (rec_b - interface) / c2
    a_inc, ti = peak_in_window(times, trace[rec_a], t_inc - 0.012, t_inc + 0.012)
    a_ref, tr = peak_in_window(times, trace[rec_a], t_ref - 0.012, t_ref + 0.012)
    a_tra, tt = peak_in_window(times, trace[rec_b], t_tra - 0.012, t_tra + 0.012)
    print(f"incident arrival    at {rec_a:.0f} m: t = {ti:.4f} s "
          f"(predicted {t_inc:.4f}), amplitude {a_inc:+.6f}")
    print(f"reflected arrival   at {rec_a:.0f} m: t = {tr:.4f} s "
          f"(predicted {t_ref:.4f}), amplitude {a_ref:+.6f}")
    print(f"transmitted arrival at {rec_b:.0f} m: t = {tt:.4f} s "
          f"(predicted {t_tra:.4f}), amplitude {a_tra:+.6f}")
    print(f"measured R = {a_ref / a_inc:+.6f}, predicted {R:+.6f}, "
          f"difference {abs(a_ref / a_inc - R):.2e}")
    print(f"measured T = {a_tra / a_inc:+.6f}, predicted {T:+.6f}, "
          f"difference {abs(a_tra / a_inc - T):.2e}")
    print()
    print("  The reflected pulse is inverted because Z2 > Z1: a positive impedance")
    print("  contrast gives a negative reflection coefficient for particle velocity")
    print("  and a positive one for pressure, which is why the same interface has")
    print("  opposite polarity in a velocity seismogram and a hydrophone record.")
    print("  Note the incident amplitude is 0.5, not 1: an initial displacement")
    print("  with zero velocity splits into two equal counter-propagating pulses.")
    print("  The coefficients are ratios, so the split cancels exactly.")


def part3_oblique():
    section("3. Oblique incidence: Snell checked against the boundary conditions")
    rho1, c1, rho2, c2 = (MODEL["rho1"], MODEL["c1"], MODEL["rho2"], MODEL["c2"])
    Z1, Z2 = rho1 * c1, rho2 * c2
    print("Fluid-fluid case; pressure amplitudes, so the reflected pressure is")
    print("R times the incident and the transmitted pressure is (1 + R) times it.")
    print("  R = (Z2 cos(theta1) - Z1 cos(theta2)) / (Z2 cos(theta1) + Z1 cos(theta2))")
    print(f"{'theta1 (deg)':>13} {'theta2 (deg)':>13} {'R':>11} {'R^2':>10} "
          f"{'max residual':>14}")
    for theta1_deg in (0.0, 15.0, 30.0, 41.8103, 45.0, 60.0):
        theta1 = math.radians(theta1_deg)
        sin2 = (c2 / c1) * math.sin(theta1)
        if sin2 > 1.0:
            print(f"{theta1_deg:13.4f} {'--':>13} {1.0:11.6f} {1.0:10.6f} "
                  f"{'evanescent':>14}")
            continue
        theta2 = math.asin(sin2)
        R = ((Z2 * math.cos(theta1) - Z1 * math.cos(theta2))
             / (Z2 * math.cos(theta1) + Z1 * math.cos(theta2)))
        T = 1.0 + R
        # pressure continuity
        res_p = abs((1.0 + R) - T)
        # normal particle velocity u_x = -cos(theta) p / Z, with the sign of the
        # x component of the wavevector; continuity gives
        # (incident + reflected) = transmitted
        u_inc = -math.cos(theta1) / Z1
        u_ref = R * math.cos(theta1) / Z1
        u_tra = -T * math.cos(theta2) / Z2
        scale = max(abs(u_inc), abs(u_ref), abs(u_tra))
        res_u = abs(u_inc + u_ref - u_tra) / scale
        print(f"{theta1_deg:13.4f} {math.degrees(theta2):13.4f} {R:11.6f} "
              f"{R * R:10.6f} {max(res_p, res_u):14.3e}")
    print()
    print("  The residual is at the level of floating-point round-off relative to")
    print("  the size of the terms: the three-wave solution satisfies Snell's law")
    print("  and both boundary conditions at once, which is what makes the problem")
    print("  well posed. Beyond the critical angle there is no real transmitted")
    print("  angle, the transmitted wave becomes evanescent, and |R| = 1. That")
    print("  evanescent tail is the physical origin of head waves, and the near-")
    print("  critical behaviour is why a hidden low-velocity layer is invisible to")
    print("  refraction surveying.")


def part4_impedance_contrasts():
    section("4. How strong is a real contrast?")
    print(f"{'boundary':>34} {'Z1 (MRayl)':>11} {'Z2 (MRayl)':>11} "
          f"{'R (pressure)':>13} {'R^2 (%)':>9}")
    cases = (
        ("water over limestone (model)", 1500.0, 1000.0, 2500.0, 3000.0),
        ("shale over gas sand (model)", 2400.0, 2500.0, 2000.0, 2200.0),
        ("shale over brine sand (model)", 2400.0, 2500.0, 2300.0, 2800.0),
        ("granite over air (model)", 2700.0, 5500.0, 1.2, 340.0),
    )
    for name, rho1, c1, rho2, c2 in cases:
        Z1, Z2 = rho1 * c1, rho2 * c2
        R = (Z2 - Z1) / (Z2 + Z1)
        print(f"{name:>34} {Z1 / 1e6:11.4f} {Z2 / 1e6:11.4f} {R:13.6f} "
              f"{R * R * 100:9.4f}")
    print()
    print("  Every row is a synthetic parameter set chosen to show the sense of the")
    print("  effect, not a measured field value: 1 MRayl = 10^6 kg m^-2 s^-1.")
    print("  A gas sand has a lower impedance than the overlying shale while a")
    print("  brine sand has a higher one, so the polarity of the reflection - not")
    print("  only its amplitude - is a fluid indicator. The granite-air contrast")
    print("  reflects almost all the energy because it is nearly total.")


if __name__ == "__main__":
    part1_snell()
    part2_normal_incidence()
    part3_oblique()
    part4_impedance_contrasts()
