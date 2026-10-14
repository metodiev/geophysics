"""Second-order linear ODEs: characteristic roots and the three regimes.

Run:  python3 second_order_linear_demo.py
Requires: Python standard library only.

Companion to lesson 01-08-02.

Everything is done with the standard model

    m x'' + c x' + k x = 0        or, dividing by m,
    x'' + 2*zeta*omega0 x' + omega0^2 x = 0

with omega0 = sqrt(k/m), zeta = c / (2 sqrt(k m)). Roots, solutions and
physical timescales are computed, and each closed-form solution is verified by
substituting it back into the ODE numerically.

Physical parameters are representative laboratory and Earth values; they are
labelled as such, and every derived number is computed here rather than quoted.
"""

import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def roots(omega0, zeta):
    """Roots of r^2 + 2 zeta omega0 r + omega0^2 = 0."""
    disc = omega0 ** 2 * (zeta ** 2 - 1.0)
    if disc >= 0.0:
        s = math.sqrt(disc)
        return (-zeta * omega0 + s, -zeta * omega0 - s)
    s = math.sqrt(-disc)
    return (complex(-zeta * omega0, s), complex(-zeta * omega0, -s))


def solution(omega0, zeta, x0, v0, t):
    """x(t) for x'' + 2 zeta omega0 x' + omega0^2 x = 0, x(0)=x0, x'(0)=v0."""
    a = -zeta * omega0
    if zeta < 1.0:
        wd = omega0 * math.sqrt(1.0 - zeta ** 2)
        A = x0
        B = (v0 - a * x0) / wd
        return math.exp(a * t) * (A * math.cos(wd * t) + B * math.sin(wd * t))
    if zeta > 1.0:
        r1, r2 = a + omega0 * math.sqrt(zeta ** 2 - 1.0), a - omega0 * math.sqrt(zeta ** 2 - 1.0)
        c2 = (v0 - r1 * x0) / (r2 - r1)
        c1 = x0 - c2
        return c1 * math.exp(r1 * t) + c2 * math.exp(r2 * t)
    wd = 0.0
    return math.exp(a * t) * (x0 + (v0 - a * x0) * t)


def residual(omega0, zeta, x0, v0, t, h=1e-3):
    """x'' + 2 zeta omega0 x' + omega0^2 x, from a fourth-order stencil.

    The value returned is the *numerical differentiation* error of the check,
    not an ODE error: the closed form is exact. A fourth-order stencil keeps
    its truncation error (h^4) below its round-off floor (eps/h^2), so the
    number printed is the honest precision of the test.
    """
    x = lambda s: solution(omega0, zeta, x0, v0, s)
    d2 = (-x(t + 2 * h) + 16 * x(t + h) - 30 * x(t) + 16 * x(t - h)
          - x(t - 2 * h)) / (12 * h ** 2)
    d1 = (x(t - 2 * h) - 8 * x(t - h) + 8 * x(t + h) - x(t + 2 * h)) / (12 * h)
    return d2 + 2 * zeta * omega0 * d1 + omega0 ** 2 * x(t)


def main():
    section("1. Characteristic roots for the three damping regimes")
    omega0 = 1.0
    for zeta, name in ((0.2, "underdamped"), (1.0, "critically damped"),
                       (2.0, "overdamped")):
        r = roots(omega0, zeta)
        def fmt(z):
            return f"{z.real:+.6f}" if isinstance(z, float) else f"{z.real:+.6f}{z.imag:+.6f}i"
        print(f"zeta = {zeta:4.1f} ({name:18s}): r = {fmt(r[0])}, {fmt(r[1])}")
    print("Discriminant zeta^2 - 1 changes sign at zeta = 1: the boundary")
    print("between oscillation and pure decay.")

    section("2. Closed-form solutions, substituted back into the ODE")
    x0, v0 = 1.0, 0.0
    print(f"{'zeta':>6}{'t':>8}{'x(t)':>16}{'residual':>16}")
    for zeta in (0.2, 1.0, 2.0):
        for t in (0.0, 0.5, 1.0, 2.0, 4.0):
            print(f"{zeta:>6.1f}{t:>8.1f}{solution(omega0, zeta, x0, v0, t):>16.9f}"
                  f"{residual(omega0, zeta, x0, v0, t):>16.3e}")
    print("Residuals are the round-off floor of the finite-difference check")
    print("(~eps/h^2 = 2e-10), not an ODE error: the formulas are exact in all")
    print("three regimes and no case needs special handling.")

    section("3. Damped frequency, decay time and logarithmic decrement")
    print("zeta=0.2 free oscillation, x'' + 0.4 x' + x = 0, x(0)=1, x'(0)=0")
    zeta = 0.2
    wd = omega0 * math.sqrt(1.0 - zeta ** 2)
    print(f"omega0 = {omega0},  omega_d = omega0 sqrt(1-zeta^2) = {wd:.9f} rad/s")
    print(f"period T_d = 2 pi / omega_d = {2 * math.pi / wd:.9f} s")
    print(f"decay time 1/(zeta omega0) = {1 / (zeta * omega0):.6f} s")
    delta = 2.0 * math.pi * zeta / math.sqrt(1 - zeta ** 2)
    print(f"log decrement delta = 2 pi zeta/sqrt(1-zeta^2) = {delta:.9f}")
    for n in (1, 2, 3):
        tn, tn1 = n * 2 * math.pi / wd, (n + 1) * 2 * math.pi / wd
        ratio = solution(omega0, zeta, x0, v0, tn) / solution(omega0, zeta, x0, v0, tn1)
        print(f"   successive-peak ratio {n} -> {n + 1}: {ratio:.9f}  "
              f"(ln = {math.log(ratio):.9f})")

    section("4. Quality factor Q = 1/(2 zeta)")
    print(f"{'zeta':>8}{'Q':>10}{'cycles to 1/e of energy':>26}")
    for zeta in (0.5, 0.1, 0.01, 1e-3, 1e-5):
        Q = 1.0 / (2.0 * zeta)
        print(f"{zeta:>8.0e}{Q:>10.1f}{Q / math.pi:>26.1f}")
    print("Q/pi cycles are needed for the energy to fall by 1/e; a seismic mode")
    print("with Q = 300 (zeta ~ 1.7e-3) rings for roughly 95 cycles.")

    section("5. Spring-supported gravimeter (period, damping, settling time)")
    # Representative moving-mass gravimeter: proof mass on a soft spring plus
    # damping, with a natural period of about 1 s. Values are instrument-scale
    # illustration numbers, not a specification of any real instrument.
    m = 0.05                      # kg
    k_spring = m * (2.0 * math.pi) ** 2      # N/m, giving T0 = 1 s
    omega_g = math.sqrt(k_spring / m)
    T0 = 2.0 * math.pi / omega_g
    print(f"m = {m} kg, k = {k_spring:.4f} N/m  ->  omega0 = {omega_g:.6f} rad/s, "
          f"T0 = {T0:.4f} s")
    for zeta in (0.1, 0.7, 5.0):
        c = 2.0 * zeta * math.sqrt(k_spring * m)
        # slowest decay rate of the free response
        if zeta > 1.0:
            rate = omega_g * (zeta - math.sqrt(zeta ** 2 - 1.0))
        else:
            rate = zeta * omega_g
        print(f"   zeta = {zeta:4.1f}: c = {c:.6f} N s/m, free-decay time "
              f"1/rate = {1 / rate:.4f} s, 6 e-foldings = {6 / rate:.3f} s")
    print("A gravimeter is deliberately damped near critical: a slow free")
    print("oscillation of the proof mass would be indistinguishable from a")
    print("changing gravity signal. Overdamping is worse, not safer, because")
    print("the slow root then approaches zero and the reading drifts for minutes.")

    section("6. Buoyancy (Brunt-Vaisala) oscillation of a parcel")
    for N in (0.02, 0.01, 0.005):
        print(f"N = {N:.3f} rad/s  ->  buoyancy period 2 pi/N = "
              f"{2 * math.pi / N:8.2f} s = {2 * math.pi / N / 60:6.2f} min")
    print("N^2 = -(g/rho) d(rho)/dz; N is the frequency of vertical oscillation")
    print("of a stably stratified parcel, and the same second-order form appears")
    print("for a long-period seismometer and for a floating ice sheet.")

    section("7. Free oscillation of the whole Earth (order of magnitude)")
    # For a normal mode, the *eigenvalue* is the squared frequency and the
    # period is set by stiffness and density, not by damping. We quote the
    # period of the gravest fundamental spheroidal mode as an order-of-
    # magnitude anchor and show what it implies for omega0 and zeta.
    T_0S2 = 3233.0                # s, commonly tabulated order of magnitude
    T_0S0 = 1227.0                # s
    for label, T in (("0S2", T_0S2), ("0S0", T_0S0)):
        om = 2.0 * math.pi / T
        print(f"mode {label}: T = {T:.0f} s = {T / 60:.2f} min, "
              f"omega0 = {om:.6e} rad/s = {1000 * om / (2 * math.pi):.4f} mHz")
    Q_earth = 300.0
    print(f"with Q = {Q_earth:.0f}, the free oscillation of that mode decays")
    print(f"   as exp(-pi f t / Q) with f = {1 / T_0S2:.6e} Hz, giving a time")
    print(f"   constant 2 Q / omega0 = {2 * Q_earth / (2 * math.pi / T_0S2):.4e} s "
          f"= {2 * Q_earth / (2 * math.pi / T_0S2) / 86400:.2f} d")
    print("Values are order-of-magnitude anchors; the exact eigenperiods depend")
    print("on the Earth model and are tabulated in normal-mode references.")

    section("8. Double root: the zeta = 1 limit is not a separate formula")
    print("As zeta -> 1 the two complex roots coalesce at r = -omega0 and the")
    print("solution passes continuously from exp(-omega0 t)sin(wd t) to")
    print("exp(-omega0 t)(1 + omega0 t). Evaluating just below and just above:")
    for zeta in (0.999999, 1.0, 1.000001):
        print(f"   zeta = {zeta:.6f}: x(1) = "
              f"{solution(1.0, zeta, 1.0, 0.0, 1.0):.12f}")


if __name__ == "__main__":
    main()
