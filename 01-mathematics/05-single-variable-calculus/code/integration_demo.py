"""Integration as accumulation, with quadrature error measured rather than assumed.

Run:  python3 integration_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-05. Every integral here is a physical total: a mass, a
moment of inertia, a heat flux, a mean temperature. In each case the exact value
is known, so the quadrature error can be printed instead of estimated - which is
the only way to learn how fast a rule actually converges.
"""

import math

G = 6.674e-11    # m^3 kg^-1 s^-2
R_EARTH = 6.371e6


def section(title: str) -> None:
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def trapezoid(f, a: float, b: float, n: int) -> float:
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def simpson(f, a: float, b: float, n: int) -> float:
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return total * h / 3.0


def main() -> None:
    section("1. Mass of a uniform sphere: int_0^R 4 pi r^2 rho dr")
    rho = 5510.0
    exact = (4.0 / 3.0) * math.pi * rho * R_EARTH ** 3
    print(f"  exact M = (4/3) pi rho R^3 = {exact:.6e} kg")
    print(f"{'n':>6}  {'trapezoid':>20}  {'rel. err':>10}  {'ratio':>6}"
          f"  {'Simpson':>20}  {'rel. err':>10}")
    f = lambda r: 4.0 * math.pi * r * r * rho
    previous_trap = None
    for n in (8, 16, 32, 64, 128, 256):
        trap = trapezoid(f, 0.0, R_EARTH, n)
        simp = simpson(f, 0.0, R_EARTH, n)
        etrap = abs(trap - exact) / exact
        esimp = abs(simp - exact) / exact
        rat_trap = previous_trap / etrap if previous_trap else float("nan")
        print(f"{n:>6}  {trap:>20.10e}  {etrap:>10.2e}  {rat_trap:>6.2f}"
              f"  {simp:>20.10e}  {esimp:>10.2e}")
        previous_trap = etrap
    print("  Reading: doubling n cuts the trapezoidal error by 4.00 - exactly")
    print("  the O(h^2) prediction. Simpson's error here is at the level of")
    print("  floating point, because Simpson's rule integrates any cubic")
    print("  exactly and the integrand is only quadratic. A rule that is exact")
    print("  for your integrand shows no convergence order at all; you have to")
    print("  test it on an integrand it cannot do analytically.")

    section("2. The orders appear on a realistic (non-polynomial) integrand")
    # Athy-style compaction: porosity decays exponentially with depth.
    rho_grain, rho_fluid = 2650.0, 1030.0
    porosity0, decay, thickness = 0.50, 1000.0, 3000.0

    def density(z: float) -> float:
        return rho_grain - (rho_grain - rho_fluid) * porosity0 * math.exp(-z / decay)

    exact_column = (rho_grain * thickness
                    - (rho_grain - rho_fluid) * porosity0 * decay
                    * (1.0 - math.exp(-thickness / decay)))
    print(f"  rho(z) = {rho_grain:.0f} - {porosity0 * (rho_grain - rho_fluid):.0f}"
          f" exp(-z/{decay:.0f}) kg/m^3  (SYNTHETIC Athy-type profile)")
    print(f"  exact mass per unit area over {thickness:.0f} m ="
          f" {exact_column:.6f} kg/m^2")
    print(f"{'n':>6}  {'trapezoid':>18}  {'rel. err':>10}  {'ratio':>6}"
          f"  {'Simpson':>18}  {'rel. err':>10}  {'ratio':>6}")
    previous_trap = previous_simp = None
    for n in (8, 16, 32, 64, 128, 256):
        trap = trapezoid(density, 0.0, thickness, n)
        simp = simpson(density, 0.0, thickness, n)
        etrap = abs(trap - exact_column) / exact_column
        esimp = abs(simp - exact_column) / exact_column
        rat_trap = previous_trap / etrap if previous_trap else float("nan")
        rat_simp = previous_simp / esimp if previous_simp else float("nan")
        print(f"{n:>6}  {trap:>18.9f}  {etrap:>10.2e}  {rat_trap:>6.2f}"
              f"  {simp:>18.9f}  {esimp:>10.2e}  {rat_simp:>6.2f}")
        previous_trap, previous_simp = etrap, esimp
    print("  Reading: trapezoid ratios are 4.00 and Simpson ratios are 16.00.")
    print("  That is the measured evidence for O(h^2) and O(h^4): the error")
    print("  exponent is not a claim about a rule in the abstract, it is a")
    print("  property of the rule applied to a particular integrand.")

    section("3. Moment of inertia of a uniform sphere: int r^2 dm")
    exact_moi = (2.0 / 5.0) * exact * R_EARTH ** 2
    numeric = simpson(lambda r: 8.0 * math.pi * rho * r ** 4 / 3.0,
                      0.0, R_EARTH, 512)
    print(f"  exact I = (2/5) M R^2 = {exact_moi:.6e} kg m^2")
    print(f"  numeric I (Simpson, n=512) = {numeric:.6e} kg m^2")
    print(f"  relative difference = {abs(numeric - exact_moi) / exact_moi:.2e}")
    print(f"  I / (M R^2) = {exact_moi / (exact * R_EARTH ** 2):.6f}")

    section("4. The same factor for a two-layer model (ILLUSTRATIVE)")
    # Core radius, core and mantle densities chosen to be Earth-like but rounded.
    r_core, rho_core, rho_mantle = 3.480e6, 11000.0, 4400.0
    mass_core = (4.0 / 3.0) * math.pi * rho_core * r_core ** 3
    mass_mantle = (4.0 / 3.0) * math.pi * rho_mantle * (R_EARTH ** 3 - r_core ** 3)
    mass_model = mass_core + mass_mantle
    moi_core = (8.0 / 15.0) * math.pi * rho_core * r_core ** 5
    moi_mantle = (8.0 / 15.0) * math.pi * rho_mantle * (R_EARTH ** 5 - r_core ** 5)
    moi_model = moi_core + moi_mantle
    print(f"  core radius = {r_core / 1.0e3:.0f} km, rho_core = {rho_core:.0f} kg/m^3,"
          f" rho_mantle = {rho_mantle:.0f} kg/m^3")
    print(f"  model mass  = {mass_model:.4e} kg (Earth 5.97e24 kg)")
    print(f"  I/(M R^2)   = {moi_model / (mass_model * R_EARTH ** 2):.4f}")
    print("  Reading: concentrating mass towards the centre lowers I/(M R^2)")
    print("  from 0.4000 for a uniform sphere to 0.3449 here. Earth's observed")
    print("  value of about 0.3308 is lower still, which is the quantitative")
    print("  statement that density in the Earth increases with depth more")
    print("  steeply than this two-step model allows. This single number is one")
    print("  of the classic integral constraints of geophysics.")

    section("5. Mean value theorem: the mean temperature of a conductive layer")
    k = 2.5            # W m^-1 K^-1
    q = 0.0625         # W m^-2, from a 25 K/km gradient
    T0 = 10.0          # deg C at the surface
    thickness = 30.0e3
    gradient = q / k
    print(f"  q = {q:.4f} W/m^2, k = {k:.1f} W m^-1 K^-1 -> dT/dz = {gradient * 1e3:.2f} K/km")
    print(f"  T(H) = {T0 + gradient * thickness:.2f} deg C at H = {thickness / 1e3:.0f} km")
    mean_numeric = trapezoid(lambda z: T0 + gradient * z, 0.0, thickness, 20000) / thickness
    print(f"  mean T (trapezoid) = {mean_numeric:.6f} deg C")
    print(f"  (T0 + T(H))/2      = {(T0 + T0 + gradient * thickness) / 2.0:.6f} deg C")
    print("  Reading: for a linear profile the mean over the interval is the")
    print("  arithmetic mean of the endpoints. This is the mean value theorem")
    print("  for integrals, and it is why a single borehole temperature cannot")
    print("  pin down a curved geotherm: the mean of a curve and the mean of")
    print("  the straight line with the same endpoints agree only when the")
    print("  curvature integrates to zero.")

    section("6. Accumulated heat: a total, and what it is worth")
    area = 100.0e3 * 100.0e3
    total_power = q * area
    print(f"  q over an area of 100 km x 100 km = {area:.3e} m^2")
    print(f"  total power = {total_power:.4e} W = {total_power / 1.0e6:.2f} MW")
    print(f"  energy over one year = {total_power * 3.156e7:.4e} J"
          f" = {total_power * 3.156e7 / 3.6e15:.3f} TWh")
    print("  Reading: integration turns a flux (per unit area) into a total")
    print("  (per second). The global geothermal resource is large in absolute")
    print("  terms and small compared with solar input, which is the reason")
    print("  geothermal energy is a local, load-following resource.")

    section("7. Signed accumulation always loses information")
    print(f"  int_0^pi sin(x) dx      = {simpson(math.sin, 0.0, math.pi, 2000):.6f}"
          "  (integrand positive throughout)")
    print(f"  int_0^(2 pi) sin(x) dx  = "
          f"{simpson(math.sin, 0.0, 2.0 * math.pi, 2000):.6e}  (the areas cancel)")
    absolute = simpson(lambda x: abs(math.sin(x)), 0.0, 2.0 * math.pi, 2000)
    print(f"  int_0^2pi |sin(x)| dx = {absolute:.6f}  (four times the half-cycle)")
    print("  Reading: a definite integral is a signed sum. Energy, mass and")
    print("  moment of inertia are not signed, so when a physical total")
    print("  cancels you have picked the wrong integrand, not the wrong rule.")


if __name__ == "__main__":
    main()
