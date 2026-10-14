"""Improper integrals: what converges, what diverges, and how slowly.

Run:  python3 improper_integrals_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-06. Three questions are asked of every integral in
this file: does it converge, how fast, and what does the answer mean physically.
The third question is the one that decides whether a divergent integral is a
mistake in your model or a genuine feature of it.
"""

import math

G = 6.674e-11    # m^3 kg^-1 s^-2
MGAL = 1.0e-5    # m/s^2 per mGal


def section(title: str) -> None:
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def simpson(f, a: float, b: float, n: int) -> float:
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return total * h / 3.0


def main() -> None:
    section("1. int_1^L x^-p dx: the same family, opposite verdicts at the two ends")
    print(f"{'L':>10}  {'p = 0.5':>16}  {'p = 1':>16}"
          f"  {'p = 2':>16}  {'p = 3':>16}")
    for exponent in (2, 4, 6, 8):
        L = 10.0 ** exponent
        row = []
        for p in (0.5, 1.0, 2.0, 3.0):
            if p == 1.0:
                row.append(math.log(L))
            else:
                row.append((L ** (1.0 - p) - 1.0) / (1.0 - p))
        print(f"{L:>10.0e}  {row[0]:>16.4e}  {row[1]:>16.4e}"
              f"  {row[2]:>16.4e}  {row[3]:>16.4e}")
    print("  Limits: p = 1 diverges logarithmically, p = 0.5 diverges as")
    print("  2 sqrt(L) - 2, p = 2 converges to 1 with tail 1/L, and p = 3")
    print("  converges to 1/2 with tail 1/(2L^2). Rule: int_1^inf x^-p")
    print("  converges if and only if p > 1.")

    section("2. int_eps^1 x^-p dx: the mirror-image rule at zero")
    print(f"{'eps':>10}  {'p = 0.5':>16}  {'p = 1':>16}  {'p = 2':>16}")
    for exponent in (2, 4, 8, 12):
        eps = 10.0 ** (-exponent)
        p05 = (1.0 - eps ** 0.5) / 0.5
        p1 = -math.log(eps)
        p2 = (1.0 - eps ** -1.0) / (1.0 - 2.0)
        print(f"{eps:>10.0e}  {p05:>16.4e}  {p1:>16.4e}  {p2:>16.4e}")
    print("  Rule: int_0^1 x^-p dx converges if and only if p < 1. The")
    print("  integrable singularity x^-1/2 gives exactly 2; x^-1 diverges")
    print("  logarithmically; x^-2 diverges as 1/eps. A singularity is not")
    print("  fatal by itself - only an integrand that decays too slowly is.")

    section("3. Integrating through a singularity: substitute it away")
    # int_0^1 x^-1/2 exp(-x) dx = sqrt(pi) erf(1) = 1.4936482656248... after
    # the substitution x = u^2 (dx = 2u du), which removes the singularity
    # entirely: x^-1/2 dx = 2 du.
    reference = math.sqrt(math.pi) * math.erf(1.0)
    print(f"  exact value, sqrt(pi) erf(1) = {reference!r}")
    print(f"{'n':>8}  {'midpoint, raw':>18}  {'error':>12}"
          f"  {'Simpson after u^2':>22}  {'error':>12}")
    for n in (10, 100, 1000, 10000, 100000):
        h = 1.0 / n
        raw = sum(((i + 0.5) * h) ** -0.5 * math.exp(-(i + 0.5) * h) * h
                  for i in range(n))
        substituted = simpson(lambda u: 2.0 * math.exp(-u * u), 0.0, 1.0, n)
        print(f"{n:>8}  {raw:>18.9f}  {raw - reference:>12.3e}"
              f"  {substituted:>22.12f}  {substituted - reference:>12.3e}")
    print("  Reading: the raw midpoint error shrinks only like sqrt(h) - about")
    print("  a factor 3 per decade of n. After the substitution the integrand")
    print("  is smooth and the same rule reaches twelve digits. A singular")
    print("  integral is a reason to look for a substitution, not a reason to")
    print("  give up on quadrature or to switch to a much finer grid.")

    section("4. An integrable singularity: int_0^1 ln x dx = -1")
    for n in (10, 100, 1000, 10000):
        h = 1.0 / n
        # Left-endpoint rule with the log evaluated at the midpoints, since
        # ln(0) is not a number that arithmetic can use.
        raw = sum(math.log((i + 0.5) * h) * h for i in range(n))
        print(f"  midpoint n={n:>6}: {raw:.9f}   error = {raw + 1.0:+.3e}")
    # Substitute x = exp(-t), dx = -exp(-t) dt: the integral becomes
    # int_0^inf t exp(-t) dt = 1, which truncates with a known tail.
    print("  after x = exp(-t): int_0^inf t exp(-t) dt = 1")
    for T in (10.0, 20.0, 30.0):
        value = simpson(lambda t: t * math.exp(-t), 0.0, T, 20000)
        tail = math.exp(-T) * (T + 1.0)
        print(f"    truncated at T={T:>4.0f}: {value:.12f}"
              f"   error = {value - 1.0:+.3e}   tail bound = {tail:.3e}")
    print("  Reading: ln x is unbounded at 0, yet the area is finite, and the")
    print("  error after truncation is controlled by an explicit bound. That")
    print("  is what 'improper but convergent' means in practice.")

    section("5. The Gaussian integral: int_{-inf}^{inf} exp(-x^2) dx = sqrt(pi)")
    print(f"  sqrt(pi) = {math.sqrt(math.pi)!r}")
    for L in (2.0, 4.0, 6.0, 20.0):
        value = simpson(lambda x: math.exp(-x * x), -L, L, 4001)
        # The omitted tail is 2 int_L^inf exp(-x^2) dx, bounded by exp(-L^2)/L.
        tail_bound = math.exp(-L * L) / L
        print(f"  [-{L:>4.1f}, {L:>4.1f}]: {value:.12f}   error ="
              f" {value - math.sqrt(math.pi):+.3e}   tail bound = {tail_bound:.3e}")
    print("  Reading: the tail bound exp(-L^2)/L collapses so fast that")
    print("  [-6, 6] already gives a dozen digits. Gaussians are the easiest")
    print("  improper integrals in geophysics; power laws are the hardest. This")
    print("  contrast - exponential versus algebraic decay - decides the")
    print("  convergence of every Fourier transform you will compute.")

    section("6. A Fourier integral that converges: transform of exp(-|x|)")
    # int_{-inf}^{inf} exp(-|x|) cos(omega x) dx = 2 int_0^inf = 2/(1+omega^2).
    # The integral is split at zero because |x| is not differentiable there,
    # and quadrature rules converge slowly across a kink.
    print(f"{'omega':>8}  {'numeric':>18}  {'2/(1+omega^2)':>18}  {'difference':>12}")
    for omega in (0.0, 0.5, 1.0, 2.0, 5.0):
        L, n = 60.0, 60000
        value = 2.0 * simpson(lambda x: math.exp(-x) * math.cos(omega * x),
                              0.0, L, n)
        exact = 2.0 / (1.0 + omega * omega)
        print(f"{omega:>8.1f}  {value:>18.12f}  {exact:>18.12f}"
              f"  {value - exact:>12.3e}")
    print("  Reading: |exp(-|x|)| decays exponentially, so the transform")
    print("  integral converges absolutely for every omega and the result is a")
    print("  smooth, positive, even function that decays like 2/omega^2.")
    print("  Contrast the transform of a constant, which converges only as a")
    print("  distribution, and the transform of 1/x, which needs a principal")
    print("  value.")

    section("7. The Bouguer slab: an improper integral with a finite answer")
    # Vertical field of an infinite sheet of surface density sigma, built by
    # integrating 2 G sigma z dx/(x^2+z^2) along the sheet.
    sigma, z_obs = 2.67e6, 1000.0      # kg/m^2 (2670 kg/m^3 over 1000 m)
    exact = 2.0 * math.pi * G * sigma
    print(f"  sigma = {sigma:.3e} kg/m^2, observation height z = {z_obs:.0f} m")
    print(f"  exact 2 pi G sigma = {exact:.6e} m/s^2 = {exact / MGAL:.5f} mGal")
    print(f"{'half-length L (m)':>18}  {'numeric g_z (mGal)':>20}"
          f"  {'rel. error':>12}  {'2/(pi) * arctan(L/z)':>22}")
    for L in (1.0e3, 1.0e4, 1.0e5, 1.0e6, 1.0e7):
        integrand = lambda x: 2.0 * G * sigma * z_obs / (x * x + z_obs ** 2)
        value = simpson(integrand, -L, L, 200001)
        ratio = 4.0 * G * sigma * math.atan(L / z_obs)
        print(f"{L:>18.0e}  {value / MGAL:>20.8f}"
              f"  {(value - exact) / exact:>12.3e}  {ratio / exact:>22.10f}")
    print("\n  Reading: the integrand decays like 1/x^2, so the tail beyond |x|")
    print("  = L is about 4 G sigma z / L, and the relative error falls only as")
    print("  2 z/(pi L). Six correct digits would need L around 6e8 m - sixty")
    print("  times the observation height, because the tail decays so slowly.")
    print("  The limit exists and is finite precisely because each strip's")
    print("  contribution falls off as 1/x^2 while the number of strips grows")
    print("  only linearly.")

    section("8. Where the same argument diverges: the potential of a line mass")
    print("  A line of mass lambda per unit length gives a 2-D potential")
    print("  V(r) = 2 G lambda ln(r/r0), which needs a reference radius r0.")
    print(f"{'robs/rmass':>12}  {'2 G lambda ln(r) (arb. units)':>32}")
    lam = 1.0e6
    for ratio in (1.0, 10.0, 1.0e3, 1.0e6, 1.0e9):
        print(f"{ratio:>12.0e}  {2.0 * G * lam * math.log(ratio):>32.6e}")
    print("  Reading: however far you move the reference level the value shifts")
    print("  without bound. The divergence is not a numerical artefact; it is")
    print("  the statement that the potential of an infinite line (or an")
    print("  infinite cylinder) has no natural zero. Two-dimensional potential")
    print("  field problems therefore carry an arbitrary reference, and only")
    print("  differences of potential - the field - are observable.")


if __name__ == "__main__":
    main()
