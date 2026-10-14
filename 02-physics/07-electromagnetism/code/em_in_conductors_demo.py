"""EM fields in conductors: skin depth, the sqrt(frequency) scaling, diffusion,
the depth reached by a sounding, and the regime boundary between diffusion and
propagation.

Run:  python3 em_in_conductors_demo.py
Requires: Python standard library only.

Companion to lesson 02-07-06. The script:

1. Tabulates the skin depth delta = sqrt(2/(mu0 sigma omega)) for a 100 ohm m
   half-space and verifies the exact sqrt(f) scaling: delta(f/n) = sqrt(n) delta(f).
2. Verifies the formula against an independent numerical solution of
   d2E/dz2 = i omega mu0 sigma E obtained with a complex tridiagonal solve, and
   recovers the apparent resistivity from the numerical surface impedance.
3. Computes the period required for a skin depth of 10 km in a 100 ohm m
   half-space, and states the convention dependence.
4. Tabulates the sounding depth for representative earth materials and periods.
5. Compares the exact attenuation constant of a lossy dielectric with the two
   common approximations (low-loss and strong-conductor), and shows which is
   valid where.

Every number printed below was produced by this script.
"""

import cmath
import math

MU0 = 1.25663706212e-6
EPS0 = 8.8541878128e-12


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def skin_depth(rho, period):
    omega = 2.0 * math.pi / period
    return math.sqrt(2.0 * rho / (MU0 * omega))


def solve_helmholtz(rho, period, n=6000):
    """Solve d2E/dz2 = i omega mu0 sigma E on 0 <= z <= 12 delta.

    E(0) = 1, E(12 delta) = 0, by the Thomas algorithm in complex arithmetic.
    Returns (h, E array) so that delta and the surface impedance can be measured.
    """
    omega = 2.0 * math.pi / period
    delta = skin_depth(rho, period)
    length = 12.0 * delta
    h = length / n
    lam = 1j * omega * MU0 / rho * h ** 2          # i omega mu0 sigma h^2
    b = -(2.0 + lam)
    c = [1.0] * (n - 1)                            # super-diagonal
    a = [1.0] * (n - 1)                            # sub-diagonal
    d = [0.0] * (n - 1)
    d[0] = -1.0                                    # -a*E_0 with E_0 = 1
    cp = [0.0] * (n - 1)
    dp = [0.0] * (n - 1)
    cp[0] = c[0] / b
    dp[0] = d[0] / b
    for i in range(1, n - 1):
        m = b - a[i] * cp[i - 1]
        cp[i] = c[i] / m
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * (n - 1)
    x[n - 2] = dp[n - 2]
    for i in range(n - 3, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return h, [1.0] + x + [0.0]


def part1_scaling():
    section("1. Skin depth and the sqrt(f) scaling")
    rho = 100.0
    print(f"  rho = {rho:.0f} ohm m, sigma = {1.0 / rho:.4f} S/m")
    print(f"{'T (s)':>12}{'f (Hz)':>14}{'delta (m)':>16}{'delta sqrt(f)':>18}")
    ref = None
    for period in (1000.0, 100.0, 10.0, 1.0, 0.1, 0.01, 0.001):
        f = 1.0 / period
        d = skin_depth(rho, period)
        print(f"{period:12.4f}{f:14.4e}{d:16.4f}{d * math.sqrt(f):18.6f}")
        if ref is None:
            ref = d * math.sqrt(f)
    print(f"  delta sqrt(f) is constant to six figures: delta is exactly"
          f" proportional to")
    print("  1/sqrt(f). This is why a decade of frequency buys only a factor 3.16 in")
    print("  depth, and why broadband MT is needed rather than a few spot frequencies.")
    print()
    for n in (10.0, 100.0, 10000.0):
        d1 = skin_depth(rho, 1.0)
        d2 = skin_depth(rho, 1.0 / n)
        print(f"  delta(T = 1/{n:.0f} s)/delta(T = 1 s) = {d2 / d1:.6f}"
              f"   (1/sqrt({n:.0f}) = {1.0 / math.sqrt(n):.6f})")


def part2_direct_check():
    section("2. Direct verification against a numerical solution of the diffusion ODE")
    print("  Solve d2E/dz2 = i omega mu0 sigma E numerically (complex tridiagonal,")
    print("  no exponential ansatz assumed), then measure the decay length and the")
    print("  surface impedance from the numerical solution.")
    rho = 100.0
    print(f"{'T (s)':>10}{'delta formula (m)':>20}{'delta measured (m)':>20}"
          f"{'rel. error':>14}")
    for period in (1.0e-4, 1.0e-2, 1.0):
        h, e = solve_helmholtz(rho, period)
        delta = skin_depth(rho, period)
        pts = []
        for j in range(int(1.0 * delta / h), int(4.0 * delta / h) + 1):
            z = j * h
            if abs(e[j]) > 0.0:
                pts.append((z, math.log(abs(e[j]))))
        n = len(pts)
        sx = sum(p[0] for p in pts)
        sy = sum(p[1] for p in pts)
        sxx = sum(p[0] ** 2 for p in pts)
        sxy = sum(p[0] * p[1] for p in pts)
        slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        measured = -1.0 / slope
        print(f"{period:10.1e}{delta:20.6f}{measured:20.6f}"
              f"{abs(measured - delta) / delta:14.3e}")
    print()
    print("  Surface impedance from the same numerical solution, using the 3-point")
    print("  one-sided derivative of E at the surface and Z = -i omega mu0 E/(dE/dz):")
    print(f"{'T (s)':>10}{'|Z| numeric':>16}{'sqrt(omega mu0 rho)':>22}"
          f"{'rho_a numeric':>16}{'phase (deg)':>14}")
    for period in (1.0e-4, 1.0e-2, 1.0):
        h, e = solve_helmholtz(rho, period)
        dbdz = (-3.0 * e[0] + 4.0 * e[1] - e[2]) / (2.0 * h)
        omega = 2.0 * math.pi / period
        z = -1j * omega * MU0 * e[0] / dbdz
        analytic = math.sqrt(omega * MU0 * rho)
        print(f"{period:10.1e}{abs(z):16.6e}{analytic:22.6e}"
              f"{abs(z) ** 2 / (omega * MU0):16.6f}{math.degrees(cmath.phase(z)):14.4f}")
    print("  The numerical solution reproduces delta to better than 1e-6 relative and")
    print("  gives back rho_a = 100.0000 ohm m with a 45 degree phase: the formula")
    print("  and the differential equation are consistent.")


def part3_ten_km():
    section("3. The period needed to sound to 10 km in a 100 ohm m half-space")
    rho, depth = 100.0, 10000.0
    period = math.pi * MU0 * depth ** 2 / rho
    print(f"  Set delta = {depth:.0f} m: T = pi mu0 delta^2/rho ="
          f" {period:.6f} s ({period * 1000:.1f} ms)")
    print(f"  check: delta(100 ohm m, {period:.4f} s) ="
          f" {skin_depth(rho, period):.3f} m")
    print("  The convention matters: if a nominal depth of 10 km is defined as")
    print(f"    delta          : T = {period:.4f} s")
    print(f"    delta/sqrt(2)  : delta = 14 142 m, T = {2 * period:.4f} s")
    print(f"    0.5 delta      : delta = 20 000 m, T = {4 * period:.4f} s")
    print("  Since T scales as the square of the nominal depth, a factor of two in")
    print("  the depth convention is a factor of four in the required period - a")
    print("  bandwidth decision, not a detail. Always state the convention when you")
    print("  attribute a depth to a period.")
    print()
    print("  For comparison, the same calculation for other resistivities:")
    for r in (10.0, 100.0, 1000.0):
        t = math.pi * MU0 * depth ** 2 / r
        print(f"    rho = {r:7.0f} ohm m: T = {t:10.4f} s")


def part4_sounding_depth():
    section("4. What a period reaches: sounding depths in earth materials")
    print("  Resistivities are NOMINAL order-of-magnitude values, not measurements.")
    cases = [("sea water (0.25 ohm m)", 0.25, 1.0),
             ("wet soil (100 ohm m)", 100.0, 1.0),
             ("crustal basement (1000 ohm m)", 1000.0, 1.0),
             ("crustal basement (1000 ohm m)", 1000.0, 1000.0),
             ("mantle (0.1 S/m nominal)", 10.0, 86400.0),
             ("mantle (0.01 S/m nominal)", 100.0, 3.156e7)]
    print(f"{'medium':>32}{'T (s)':>12}{'delta (m)':>16}{'delta (km)':>14}")
    for name, rho, period in cases:
        d = skin_depth(rho, period)
        print(f"{name:>32}{period:12.4g}{d:16.4g}{d / 1000.0:14.4g}")
    print("  A one-day period in a 10 ohm m (0.1 S/m) mantle reaches ~470 km, which")
    print("  is the asthenosphere: that is the depth window of geomagnetic depth")
    print("  sounding, and it is set entirely by the conductivity of the ground.")
    print("  Where delta exceeds the thickness of the conducting layer the half-space")
    print("  formula is only an upper bound, since the layer then controls the")
    print("  response - which is exactly the two-layer behaviour of demo 3 of this")
    print("  lesson series. The 0.01 S/m row gives delta > Earth radius, and the")
    print("  half-space model is simply invalid there.")


def part5_regime():
    section("5. Exact attenuation against the two standard approximations")
    sigma, epsr = 0.01, 20.0
    eps = epsr * EPS0
    print(f"  wet-soil model: sigma = {sigma} S/m, eps_r = {epsr:.0f}, mu = mu0")
    print(f"  crossover frequency f_c = sigma/(2 pi eps) ="
          f" {sigma / (2 * math.pi * eps):.4e} Hz")
    print(f"{'f (Hz)':>12}{'sigma/(omega eps)':>18}{'alpha exact':>14}"
          f"{'alpha low-loss':>16}{'1/delta':>12}{'v (m/s)':>14}{'lambda (m)':>12}")
    for f in (1.0e-3, 1.0e6, 1.0e7, 1.0e8, 1.0e9):
        omega = 2.0 * math.pi * f
        x = sigma / (omega * eps)
        root = math.sqrt(1.0 + x * x)
        alpha_exact = omega * math.sqrt(MU0 * eps / 2.0) * math.sqrt(root - 1.0)
        alpha_ll = (sigma / 2.0) * math.sqrt(MU0 / eps)
        alpha_skin = 1.0 / skin_depth(1.0 / sigma, 1.0 / f)
        beta = omega * math.sqrt(MU0 * eps / 2.0) * math.sqrt(root + 1.0)
        v = omega / beta
        print(f"{f:12.4g}{x:18.4e}{alpha_exact:14.5e}{alpha_ll:16.5e}"
              f"{alpha_skin:12.5e}{v:14.5e}{2 * math.pi / beta:12.5e}")
    omega = 2.0 * math.pi * 1.0e8
    x = sigma / (omega * eps)
    alpha100 = omega * math.sqrt(MU0 * eps / 2.0) * math.sqrt(math.sqrt(1 + x * x) - 1)
    np_to_db = 8.685889638
    print("  Note the three regimes:")
    print("    x >> 1 (left): the strong-conductor result alpha = 1/delta is right and")
    print("      the field is diffusive - mHz to Hz frequencies in rock.")
    print("    x << 1 (right): the low-loss result alpha = (sigma/2)sqrt(mu/eps) is")
    print("      right and the field is a wave - GPR frequencies in resistive rock.")
    print("    x ~ 1 (middle): both approximations fail and only the exact form is")
    print(f"      safe. At 1e8 Hz, 1/delta overestimates alpha by a factor"
          f" {1.98692 / alpha100:.1f}.")
    print(f"  At f = 1e8 Hz the exact alpha is {alpha100:.6e} Np/m ="
          f" {alpha100 * np_to_db:.4f} dB/m one-way.")
    print(f"  A two-way GPR path to 5 m loses {2 * 5 * alpha100 * np_to_db:.1f} dB,"
          f" which is")
    print("  consistent with the few-metre penetration of high-frequency GPR in wet")
    print("  soil, and with the fact that penetration improves markedly in drier,")
    print("  more resistive ground where sigma is smaller.")


def main():
    part1_scaling()
    part2_direct_check()
    part3_ten_km()
    part4_sounding_depth()
    part5_regime()


if __name__ == "__main__":
    main()
