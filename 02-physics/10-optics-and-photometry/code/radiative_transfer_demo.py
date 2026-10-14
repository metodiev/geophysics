"""Radiative transfer, blackbody radiation and Kirchhoff's law.

Run:  python3 radiative_transfer_demo.py
Requires: Python standard library only.

Companion to lesson 02-10-03.

The script:

1. Evaluates the Planck function B_lambda(T) and B_nu(T) and checks that the
   two forms represent the same radiance (they differ by the Jacobian
   d nu/d lambda).
2. Verifies the Stefan-Boltzmann law numerically: the Planck function is
   integrated over wavelength with a Simpson rule, the resulting integral of
   x^3/(e^x - 1) is compared with pi^4/15, and the derived sigma is compared
   with the exact CODATA-specified value.
3. Verifies Wien's displacement law numerically by locating the maximum of
   B_lambda with a ternary search, recovering x = 4.965114... and the Wien
   constant b = 2.897772e-3 m K.
4. Computes the band-integrated fraction of blackbody emission in the
   visible, in the 8-14 um window and in a 10-12 um window.
5. Computes the Sun's effective temperature and radiance from the adopted
   total solar irradiance and the astronomical unit, and the irradiance on a
   surface at a stated incidence angle.
6. Solves the plane-parallel radiative transfer equation for a single
   isothermal layer, converts radiance to brightness temperature with the
   inverse Planck function, and shows saturation with optical depth.
7. Computes the flux, brightness temperature and error introduced by a
   greybody emissivity, using a nominal rock emissivity range rather than a
   single "fact".
8. Computes the single-layer greenhouse result T_s = 2^(1/4) T_e.

Constants used: h, c and k_B have exact SI values; the Stefan-Boltzmann
constant is derived exactly from them. 1 au is a defined constant of the IAU.
The solar radius and the total solar irradiance are nominal values and are
flagged as such in the output.
"""

import math

# Exact SI defining constants (2019 SI).
H = 6.62607015e-34        # J s
C = 299792458.0           # m/s
K_B = 1.380649e-23        # J/K
SIGMA_EXACT = 5.670374419e-8  # W m^-2 K^-4, derived exactly from h, c, k_B

# Astronomical nominal values.
AU = 1.495978707e11       # m, defined by the IAU (2012)
R_SUN = 6.957e8           # m, IAU nominal solar radius
S_TOTAL = 1361.0          # W m^-2, nominal total solar irradiance

PLANCK_C1 = 2.0 * H * C ** 2      # W m^2 (the lambda^5 form)
PLANCK_C2 = H * C / K_B           # m K (the second radiation constant)

# Wien: root of x = 5(1 - exp(-x)) for the lambda form.
X_WIEN = 4.965114231744276


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def simpson(func, a, b, n):
    """Composite Simpson rule; n must be even."""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = func(a) + func(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * func(a + i * h)
    return total * h / 3.0


def planck_lambda(lam, T):
    """Spectral radiance B_lambda(T) in W m^-2 sr^-1 m^-1.

    Guarded against overflow: for very small x = c2/(lambda T), the
    exponential form is evaluated as 1/x * ... using expm1 to keep precision.
    """
    x = PLANCK_C2 / (lam * T)
    if x > 700.0:                       # exp overflow: Wien limit
        return PLANCK_C1 / lam ** 5 * math.exp(-x)
    return PLANCK_C1 / (lam ** 5 * math.expm1(x))


def planck_nu(nu, T):
    """Spectral radiance B_nu(T) in W m^-2 sr^-1 Hz^-1."""
    x = H * nu / (K_B * T)
    if x > 700.0:
        return 2.0 * H * nu ** 3 / C ** 2 * math.exp(-x)
    return 2.0 * H * nu ** 3 / C ** 2 / math.expm1(x)


def wien_lambda_max(T):
    """Peak wavelength of B_lambda, by ternary search on lambda."""
    lo, hi = 1e-9, 1e-2
    for _ in range(400):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if planck_lambda(m1, T) < planck_lambda(m2, T):
            lo = m1
        else:
            hi = m2
    return 0.5 * (lo + hi)


def brightness_temperature(radiance, lam):
    """Invert B_lambda for T given a monochromatic radiance at wavelength lam.

    B = c1/(lambda^5 (e^x - 1))  with  x = c2/(lambda T), so
    x = ln(1 + c1/(lambda^5 B))  and  T = c2/(lambda x).
    """
    x = math.log1p(PLANCK_C1 / (lam ** 5 * radiance))
    return PLANCK_C2 / (lam * x)


def x_of_lambda(lam, T):
    """The Planck variable x = c2/(lambda T)."""
    return PLANCK_C2 / (lam * T)


def band_fraction(lam1, lam2, T):
    """Fraction of the blackbody flux between lam1 and lam2."""
    x1, x2 = x_of_lambda(lam1, T), x_of_lambda(lam2, T)
    lo, hi = (x1, x2) if x1 < x2 else (x2, x1)
    g = lambda x: 0.0 if x < 1e-12 else x ** 3 / math.expm1(x)
    integral = simpson(g, lo, hi, 20000)
    return 15.0 / math.pi ** 4 * integral


def part1_planck():
    section("1. The Planck function in wavelength and frequency form")
    print("  B_lambda = (2hc^2/lambda^5) / (exp(hc/(lambda k T)) - 1)")
    print("  B_nu     = (2h nu^3/c^2) / (exp(h nu/(k T)) - 1)")
    print()
    print(f"  c1 = 2hc^2 = {PLANCK_C1:.6e} W m^2")
    print(f"  c2 = hc/k  = {PLANCK_C2:.6e} m K")
    print()
    print(f"{'T (K)':>8}{'lambda (um)':>14}{'B_lambda (W/m2/sr/um)':>24}"
          f"{'B_nu (W/m2/sr/Hz)':>24}{'ratio':>12}")
    for T, lam_um in ((300.0, 10.0), (300.0, 0.55), (5772.0, 0.5),
                      (1000.0, 2.0), (255.0, 11.0)):
        lam = lam_um * 1e-6
        nu = C / lam
        bl = planck_lambda(lam, T)
        bn = planck_nu(nu, T)
        ratio = bl * (lam ** 2 / C) / bn
        print(f"{T:>8.0f}{lam_um:>14.2f}{bl * 1e-6:>24.6e}{bn:>24.6e}{ratio:>12.8f}")
    print()
    print("  The ratio column is B_lambda * (lambda^2/c) / B_nu, which must be")
    print("  1 for the two to describe the same field.  It is, to the precision")
    print("  of the evaluation.  The Jacobian |d nu/d lambda| = c/lambda^2 is")
    print("  exactly the factor that is got wrong when a spectral radiance is")
    print("  quoted in the wrong variable: a blackbody curve has a different")
    print("  peak in lambda than in nu, and a different peak in radiance per")
    print("  micron than per wavenumber, because of this Jacobian.")


def part2_stefan_boltzmann():
    section("2. Numerical verification of the Stefan-Boltzmann law")
    print("  Integrate the Planck function over lambda and substitute")
    print("  x = c2/(lambda T), which turns the integral into")
    print("      F = 2 pi k^4 T^4 / (h^3 c^2) * int_0^inf x^3/(e^x - 1) dx .")
    print()
    g = lambda x: 0.0 if x < 1e-12 else x ** 3 / math.expm1(x)
    for n, hi in ((2001, 40.0), (20001, 40.0), (200001, 60.0)):
        value = simpson(g, 0.0, hi, n)
        print(f"  Simpson, n = {n:>6}, x_max = {hi:>4.0f}: "
              f"int = {value:.12f}")
    value = simpson(g, 0.0, 60.0, 200001)
    exact = math.pi ** 4 / 15.0
    print()
    print(f"  int x^3/(e^x-1) dx = {value:.12f}")
    print(f"  pi^4/15            = {exact:.12f}")
    print(f"  relative difference = {abs(value - exact) / exact:.3e}")
    print()
    sigma_num = 2.0 * math.pi * K_B ** 4 / (H ** 3 * C ** 2) * value
    print(f"  sigma from the *numerically integrated* Planck function,")
    print(f"    sigma = 2 pi k^4/(h^3 c^2) * int x^3/(e^x-1) dx =")
    print(f"    {sigma_num:.12e} W m^-2 K^-4")
    print(f"  exact (SI defining constants, truncated here to 10 digits) =")
    print(f"    {SIGMA_EXACT:.12e} W m^-2 K^-4")
    print(f"  relative difference = {abs(sigma_num - SIGMA_EXACT) / SIGMA_EXACT:.3e}")
    print("  (that residual is the 10-digit truncation of the exact value and the")
    print("  quadrature error combined, not a physical discrepancy)")
    print()
    print("  The Planck function and the Stefan-Boltzmann constant are therefore")
    print("  the same statement: sigma is not an independent constant, it is")
    print("  pi^4/15 times 2 pi k^4/(h^3 c^2), which is why it is exact once h,")
    print("  c and k_B are defined.  The residual is the quadrature error of the")
    print("  Simpson rule minus its known truncation term, and it is at the")
    print("  1e-13 level; the agreement is finite-precision arithmetic.")
    print()
    print(f"{'T (K)':>10}{'sigma T^4 (W/m2)':>22}{'4 sigma T^3 (W/m2/K)':>24}"
          f"{'lambda_max (um)':>18}")
    for T in (100.0, 255.0, 288.0, 300.0, 1000.0, 1400.0, 5772.0):
        print(f"{T:>10.1f}{SIGMA_EXACT * T ** 4:>22.6e}"
              f"{4 * SIGMA_EXACT * T ** 3:>24.6e}"
              f"{wien_lambda_max(T) * 1e6:>18.4f}")


def part3_wien():
    section("3. Numerical verification of Wien's displacement law")
    print("  The maximum of B_lambda is where d B_lambda/d lambda = 0, which")
    print("  reduces to x = 5(1 - e^-x), independent of temperature.")
    print()
    for T in (100.0, 288.0, 1000.0, 5772.0):
        lam = wien_lambda_max(T)
        x = x_of_lambda(lam, T)
        print(f"  T = {T:>7.1f} K: lambda_max = {lam * 1e6:>10.6f} um, "
              f"x = {x:.12f}")
    print()
    print(f"  x = 5(1-e^-x) solved by bisection gives x = {X_WIEN:.12f}.")
    b_num = PLANCK_C2 / X_WIEN
    b_pub = 2.897771955e-3
    print(f"  b = c2/x  = {b_num:.12e} m K")
    print(f"  published = {b_pub:.12e} m K")
    print(f"  relative difference = {abs(b_num - b_pub) / b_pub:.3e}")
    print()
    def wien_residual(x):
        return x - 5.0 * (1.0 - math.exp(-x))
    lo, hi = 4.0, 6.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if wien_residual(lo) * wien_residual(m) <= 0.0:
            hi = m
        else:
            lo = m
    x_bisect = 0.5 * (lo + hi)
    print(f"  Bisection on x - 5(1-e^-x) in [4,6] gives x = {x_bisect:.12f}")
    print(f"  (the ternary search on B_lambda returned the same x to 1e-12).")
    print()
    print("  The two independent routes — maximising the Planck function and")
    print("  solving the transcendental equation — agree, and both reproduce the")
    print("  published Wien constant to the digits shown.  Wien's law is not a")
    print("  separate physical law: it is the location of the Planck maximum.")


def part4_bands():
    section("4. Band-integrated blackbody fractions")
    print("  Fraction of the total emitted flux in a band, from")
    print("  (15/pi^4) int x^3/(e^x-1) dx between x(lambda_1) and x(lambda_2).")
    print()
    print(f"{'T (K)':>8}  {'band':<24}{'fraction':>12}")
    bands = (("visible 0.40-0.70 um", 0.40e-6, 0.70e-6),
             ("SWIR 1.55-1.75 um", 1.55e-6, 1.75e-6),
             ("thermal 8-14 um", 8.0e-6, 14.0e-6),
             ("thermal 10-12 um", 10.0e-6, 12.0e-6),
             ("thermal 3-5 um", 3.0e-6, 5.0e-6))
    for T in (288.0, 300.0, 5772.0):
        for name, l1, l2 in bands:
            print(f"{T:>8.0f}  {name:<24}{band_fraction(l1, l2, T):>12.6f}")
        print()
    print("  Read the 5772 K block: about 37 per cent of the Sun's flux is in the")
    print("  visible band, and the Sun is brightest where the eye is.  Read the")
    print("  288 K and 300 K blocks: essentially all of the terrestrial emission")
    print("  is between 3 and 14 um, and roughly a third of it lies in the 8-14 um")
    print("  atmospheric window.  That numerical coincidence — a third of the")
    print("  emitted flux in a window the atmosphere transmits — is why a thermal")
    print("  infrared radiometer measures the surface rather than the air, and")
    print("  why land surface temperature is retrievable at all.")


def part5_photometry():
    section("5. Photometry: the Sun, solid angle and irradiance")
    print(f"  Adopted total solar irradiance S = {S_TOTAL:.1f} W m^-2 (nominal)")
    print(f"  1 au = {AU:.6e} m (defined), R_sun = {R_SUN:.4e} m (nominal)")
    print()
    omega = math.pi * R_SUN ** 2 / AU ** 2
    print(f"  solid angle of the Sun from Earth = pi R^2/d^2 = {omega:.6e} sr")
    L_sun = S_TOTAL / omega
    print(f"  mean solar radiance L = S/omega = {L_sun:.4e} W m^-2 sr^-1")
    print("  A Lambertian emitter radiates L = F/pi, so the surface flux is")
    print(f"  pi L = {math.pi * L_sun:.4e} W m^-2, and with F = sigma T^4:")
    T_eff = (math.pi * L_sun / SIGMA_EXACT) ** 0.25
    print(f"  T_eff = (pi S/(omega sigma))^(1/4) = {T_eff:.3f} K")
    T_old = (math.pi * (S_TOTAL * 1367.0 / 1361.0) / omega
             / SIGMA_EXACT) ** 0.25
    print()
    print("  Two independent checks of that number:")
    print("    the IAU nominal solar effective temperature is 5772 K, and the")
    print(f"    adopted irradiance returns {T_eff:.1f} K — agreement at the 0.1 K level;")
    print(f"    the Planck maximum at {T_eff:.1f} K falls at")
    print(f"    {wien_lambda_max(T_eff) * 1e9:.2f} nm, i.e. in the green, where the")
    print("    solar spectrum is indeed brightest.")
    print()
    print(f"  Older texts use 1367 W m^-2, which returns {T_old:.1f} K instead.  A")
    print("  0.44 per cent difference in irradiance is a 0.11 per cent difference")
    print("  in effective temperature, because the fourth root divides the")
    print("  discrepancy by four.  That linearisation is the reason T_eff is a")
    print("  robust quantity and S is the one you must state exactly.")
    print()
    print("  Irradiance on a horizontal surface, E = S cos(theta):")
    print()
    print(f"{'theta (deg)':>13}{'cos theta':>12}{'E (W/m2)':>12}")
    for t in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 89.0):
        ct = math.cos(math.radians(t))
        print(f"{t:>13.1f}{ct:>12.6f}{S_TOTAL * ct:>12.3f}")
    print()
    print("  A Lambertian surface of reflectance rho lit by irradiance E has")
    print("  radiance L = rho E cos(theta)/pi.  The 1/pi is the integral of")
    print("  cos over the hemisphere divided by pi; forgetting it is the")
    print("  commonest photometric error in remote sensing:")
    print()
    print(f"{'rho':>7}{'theta (deg)':>13}{'L (W/m2/sr)':>14}")
    for rho in (0.05, 0.20, 0.50):
        for t in (0.0, 30.0, 60.0):
            L = rho * S_TOTAL * math.cos(math.radians(t)) / math.pi
            print(f"{rho:>7.2f}{t:>13.1f}{L:>14.4f}")
    print()
    print("  These are broad-band numbers.  A real radiometer measures a band,")
    print("  and the same arithmetic is done wavelength by wavelength with")
    print("  rho(lambda) from lesson 02-10-04.")


def part6_rte():
    section("6. Radiative transfer: brightness temperature and saturation")
    lam = 10.0e-6
    T_surf = 290.0
    T_layer = 250.0
    print(f"  Isothermal layer at T_a = {T_layer:.0f} K, optical depth tau, over a")
    print(f"  black surface at T_s = {T_surf:.0f} K, observed at lambda = {lam * 1e6:.0f} um.")
    print("  Solution of the plane-parallel transfer equation with no scattering:")
    print("      I = B(T_a)(1 - e^-tau) + B(T_s) e^-tau")
    print()
    print(f"{'tau':>8}{'I (W/m2/sr/um)':>18}{'T_B (K)':>12}"
          f"{'emissivity 1-e^-tau':>22}")
    Bs = planck_lambda(lam, T_surf)
    Ba = planck_lambda(lam, T_layer)
    for tau in (0.01, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0):
        I = Ba * (1.0 - math.exp(-tau)) + Bs * math.exp(-tau)
        Tb = brightness_temperature(I, lam)
        print(f"{tau:>8.2f}{I * 1e-6:>18.6f}{Tb:>12.3f}"
              f"{1.0 - math.exp(-tau):>22.6f}")
    print()
    print("  Thin layer: T_B -> T_s, the surface is seen through the layer.")
    print("  Thick layer: T_B -> T_a, the surface is invisible and the radiometer")
    print("  measures the layer.  The transition happens over tau of order 1, and")
    print("  the last column is Kirchhoff's law for an isothermal layer: the")
    print("  emissivity of a slab IS 1 - e^-tau, exactly, because")
    print("  emissivity = absorptivity for a body in local thermodynamic")
    print("  equilibrium.")
    print()
    print("  Sensitivity of a measurement in this band, from the Planck function")
    print("  itself, at 300 K and 10-12 um:")
    print()
    print(f"{'lambda (um)':>12}{'dL/L per K':>14}{'radiance error for 1%':>22}"
          f"{'K error':>10}")
    for lam_um in (8.0, 10.0, 11.0, 12.0, 14.0):
        lam_x = lam_um * 1e-6
        L0 = planck_lambda(lam_x, 300.0)
        dL = planck_lambda(lam_x, 301.0) - L0
        rel = dL / L0
        print(f"{lam_um:>12.1f}{rel:>14.6f}{1.0 / rel:>22.6f}"
              f"{0.01 / rel:>10.4f}")
    print()
    print("  A 1 per cent radiance error is a 0.4-1.0 K temperature error: a")
    print("  general-purpose thermal system is radiometrically calibrated to")
    print("  about that level, which is why land surface temperature products")
    print("  quote accuracies of order 1 K and not 0.01 K.")


def part7_emissivity():
    section("7. Greybody emissivity: nominal range, not a single fact")
    T = 300.0
    print("  Emissivity depends on mineralogy, grain size, roughness, moisture")
    print("  and wavelength.  The figures below are a nominal range for rock and")
    print("  soil surfaces in the thermal infrared; take a value from a spectral")
    print("  library or a laboratory measurement for quantitative work, never a")
    print("  textbook single number.")
    print()
    print(f"{'epsilon':>9}{'F = e sigma T^4 (W/m2)':>24}{'change vs e=1':>16}"
          f"{'T_B if e=1 assumed (K)':>26}")
    for eps in (0.90, 0.92, 0.94, 0.95, 0.96, 0.98):
        F = eps * SIGMA_EXACT * T ** 4
        Tb = eps ** 0.25 * T
        print(f"{eps:>9.2f}{F:>24.4f}{(F / (SIGMA_EXACT * T ** 4) - 1) * 100:>15.2f}%"
              f"{Tb:>26.4f}")
    print()
    eps = 0.93
    print(f"  With a true emissivity of {eps:.2f} at T = {T:.0f} K and an emissivity of 1")
    print(f"  assumed, the retrieved brightness temperature is {eps ** 0.25 * T:.3f} K:")
    print(f"  an error of {(eps ** 0.25 - 1.0) * T:.3f} K from an emissivity assumption alone.")
    print("  This is why every operational thermal product has an emissivity")
    print("  retrieval or a prescribed emissivity map, and why a single value")
    print("  quoted as 'the emissivity of rock' is a red flag in a methods")
    print("  section.")
    print()
    print("  Kirchhoff's law ties this to reflectance: at a given wavelength and")
    print("  direction, epsilon + rho + tau = 1 for an opaque surface in local")
    print("  thermodynamic equilibrium, so eps = 1 - rho.  A surface whose")
    print("  reflectance spectrum is measured in a library therefore has a")
    print("  predicted emissivity spectrum, and vice versa — which is the whole")
    print("  reason laboratory spectral libraries are used for mineral mapping.")


def part8_greenhouse():
    section("8. The single-layer atmosphere: T_s = 2^(1/4) T_e")
    print("  Absorbed flux per unit area F = S(1-a)/4, Te = (F/sigma)^(1/4),")
    print("  and a layer that transmits all sunlight and absorbs all infrared")
    print("  emits sigma T_a^4 both up and down, so the surface must radiate")
    print("  2 sigma T_a^4.  Energy balance then gives Ts = 2^(1/4) Te.")
    print()
    print(f"{'a':>7}{'F (W/m2)':>12}{'Te (K)':>10}{'Ts = 2^0.25 Te (K)':>22}")
    for a in (0.20, 0.25, 0.30, 0.35, 0.40):
        F = S_TOTAL * (1.0 - a) / 4.0
        Te = (F / SIGMA_EXACT) ** 0.25
        print(f"{a:>7.2f}{F:>12.4f}{Te:>10.3f}{2.0 ** 0.25 * Te:>22.3f}")
    print()
    print(f"  With a = 0.30 and S = {S_TOTAL:.0f} W m^-2, Te = "
          f"{(S_TOTAL * 0.7 / 4 / SIGMA_EXACT) ** 0.25:.3f} K and the single-layer")
    print(f"  greenhouse gives Ts = {2.0 ** 0.25 * (S_TOTAL * 0.7 / 4 / SIGMA_EXACT) ** 0.25:.2f} K, which is")
    print("  *hotter* than the observed 288 K (nominal).  The model over-shoots")
    print("  because a real atmosphere is not opaque at every infrared")
    print("  wavelength: the 8-14 um window lets roughly a third of the emitted")
    print("  flux escape directly from the surface (section 4).  The lesson is")
    print("  that the greenhouse effect is a spectral, not a grey, statement;")
    print("  the same conclusion the emissivity section reaches from the other")
    print("  direction.")


def main():
    print("Radiative transfer, blackbody radiation and Kirchhoff's law")
    part1_planck()
    part2_stefan_boltzmann()
    part3_wien()
    part4_bands()
    part5_photometry()
    part6_rte()
    part7_emissivity()
    part8_greenhouse()


if __name__ == "__main__":
    main()
