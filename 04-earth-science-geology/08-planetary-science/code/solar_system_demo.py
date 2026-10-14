"""Solar system architecture: four derived relations and one budget.

Run:  .venv/bin/python solar_system_demo.py
Requires: numpy.

Companion to lesson 04-08-01.

1. Kepler's third law, used as a measurement of the Sun's gravitational
   parameter from the Earth's orbit and checked against the tabulated value.
2. Equilibrium temperature against heliocentric distance, which is where the
   idea of a "snow line" or ice line comes from.  It is derived from a flux
   balance and needs no planetary data at all beyond the Sun's luminosity.
3. The angular-momentum budget of the solar system, computed from orbital
   elements.  The Sun holds almost all the mass and almost none of the orbital
   angular momentum, and the ratio is a number rather than a slogan.
4. The Jeans escape parameter, the criterion that decides which gases a body
   keeps.  It is computed for four gases and three bodies, and one case where
   the criterion does NOT explain the observation is stated explicitly.
5. Two-component mixing densities, inverted to give an ice mass fraction from
   a measured uncompressed density.

Planetary masses, semimajor axes and eccentricities are TABULATED standard
values; they are quoted here as inputs to test relations against, not as
measurements made by this script.  They are revised as ephemerides improve, so
confirm them in a current source before quoting them.
"""

import math

import numpy as np

G = 6.67430e-11
AU = 1.495978707e11          # m, exact by definition of the astronomical unit
L_SUN = 3.828e26             # W, TABULATED solar luminosity (measured)
R_SUN = 6.957e8              # m, TABULATED nominal solar radius (defined)
T_SUN = 5772.0               # K, TABULATED nominal solar effective temperature
SIGMA = 5.670374419e-8       # W m^-2 K^-4, exact (SI)
K_B = 1.380649e-23           # J/K, exact (SI)
U_KG = 1.66053906892e-27     # kg, exact (SI) atomic mass constant
GM_SUN_TAB = 1.32712440018e20  # m^3/s^2, TABULATED (IAU)

# TABULATED standard planetary values (mass kg, semimajor axis m, eccentricity).
PLANETS = (
    ("Mercury", 3.3011e23, 5.7910e10, 0.2056),
    ("Venus", 4.8675e24, 1.0821e11, 0.0068),
    ("Earth", 5.97237e24, 1.49598e11, 0.0167),
    ("Mars", 6.4171e23, 2.2792e11, 0.0934),
    ("Jupiter", 1.8982e27, 7.7857e11, 0.0489),
    ("Saturn", 5.6834e26, 1.43353e12, 0.0565),
    ("Uranus", 8.6810e25, 2.87246e12, 0.0457),
    ("Neptune", 1.02413e26, 4.49506e12, 0.0113),
)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Kepler's third law
# --------------------------------------------------------------------------

def part1():
    section("1. Kepler's third law as a measurement of GM_sun")
    print("  For a circular orbit, m v^2/a = GM m/a^2 with v = 2 pi a / T gives")
    print("      T^2 = 4 pi^2 a^3 / (GM),   i.e.  GM = 4 pi^2 a^3 / T^2.")
    print("  The astronomical unit is exactly defined, and the sidereal year is")
    print("  measured, so this is a measurement of the Sun's gravitational")
    print("  parameter from two numbers.")
    print()
    t_year = 365.256363004 * 86400.0     # s, TABULATED sidereal year
    gm = 4.0 * math.pi ** 2 * AU ** 3 / t_year ** 2
    print(f"  a  = 1 au            = {AU:.6e} m  (defined)")
    print(f"  T  = sidereal year   = {t_year:.6e} s  (TABULATED)")
    print(f"  GM = 4 pi^2 a^3/T^2  = {gm:.6e} m^3/s^2   (derived)")
    print(f"  GM tabulated (IAU)   = {GM_SUN_TAB:.6e} m^3/s^2")
    print(f"  relative difference  = {abs(gm-GM_SUN_TAB)/GM_SUN_TAB:.3e}")
    gm_emb = 3.986004418e14 + 4.9048695e12   # TABULATED GM_earth + GM_moon
    print(f"  GM_earth + GM_moon   = {gm_emb:.4e} m^3/s^2, which is "
          f"{gm_emb/GM_SUN_TAB:.3e}")
    print("  of GM_sun.  The derived value exceeds the tabulated one by almost")
    print("  exactly that fraction, because the orbit measured is the")
    print("  Earth-Moon barycentre's, and it responds to the Sun plus the")
    print("  Earth-Moon system.  The residual is that mass, not an error.")
    print()
    v = 2.0 * math.pi * AU / t_year
    print(f"  Earth's orbital speed = 2 pi a / T = {v:.3f} m/s = {v/1000:.3f} km/s")
    print()
    print("  Kepler's third law for the other planets, using GM above:")
    print("     planet      a (au)     T (yr)   from a")
    for name, _m, a, _e in PLANETS:
        T = 2.0 * math.pi * math.sqrt(a ** 3 / gm) / (365.25 * 86400.0)
        print(f"  {name:10s} {a/AU:10.4f}  {T:10.4f}")
    print("  These are the computed periods; compare them with a current")
    print("  ephemeris rather than with a remembered table.")


# --------------------------------------------------------------------------
# 2. Equilibrium temperature
# --------------------------------------------------------------------------

def t_eq(a, albedo):
    """Equilibrium temperature of a rapidly rotating airless body."""
    s = L_SUN / (4.0 * math.pi * a ** 2)
    return ((1.0 - albedo) * s / (4.0 * SIGMA)) ** 0.25


def part2():
    section("2. Equilibrium temperature and the ice line")
    print("  Absorbed flux  (1-A) L/(4 pi a^2);  emitted flux  sigma T^4 over")
    print("  the whole sphere, 4 pi R^2, divided by the absorbing cross section,")
    print("  pi R^2, gives a factor of 4:")
    print("      T_eq = [ (1-A) L / (16 pi sigma a^2) ]^(1/4).")
    print("  It contains no planetary property except the albedo.")
    print()
    for A in (0.0, 0.3):
        print(f"  albedo A = {A:.1f}:")
        print("     a (au)   T_eq (K)   T_eq (C)")
        for a_au in (0.39, 0.72, 1.0, 1.52, 2.0, 3.0, 5.2, 9.5, 19.2, 30.1):
            T = t_eq(a_au * AU, A)
            print(f"  {a_au:9.2f}   {T:8.1f}   {T-273.15:9.1f}")
        print()
    print("  With A = 0.3 the Earth's equilibrium temperature is")
    earth = t_eq(AU, 0.3)
    print(f"  {earth:.1f} K = {earth-273.15:.1f} C.  The measured mean surface")
    print("  temperature of the Earth is about 288 K, so the difference,")
    print(f"  {288.0-earth:.1f} K, is the greenhouse effect of the atmosphere —")
    print("  derived here as a residual, not asserted.")
    print()
    print("  The ice line: the distance at which an airless body with A = 0.3")
    print("  reaches the freezing point of water, and one at which it reaches a")
    print("  temperature typical of a comet's surface.")
    print("     T_eq (K)   a (au)")
    for T in (200.0, 273.0, 300.0):
        a = math.sqrt((1.0 - 0.3) * L_SUN / (16.0 * math.pi * SIGMA * T ** 4))
        print(f"  {T:10.0f}   {a/AU:8.3f}")
    print()
    print("  Water ice is stable against sublimation over a geological time at")
    print("  a few au, which is the physical content of the 'snow line' and the")
    print("  reason the giant planets, which formed beyond it, are volatile-rich")
    print("  and the terrestrial planets are not.  The exact distance is a")
    print("  model answer: it depends on the albedo, on the nebular optical")
    print("  depth, and on the disk's radial temperature profile.")


# --------------------------------------------------------------------------
# 3. Angular momentum budget
# --------------------------------------------------------------------------

def part3():
    section("3. The angular-momentum budget")
    print("  For a Kepler orbit the angular momentum is L = m sqrt(GM a (1-e^2))")
    print("  (per unit mass h = sqrt(GM a (1-e^2)), from the vis-viva equation).")
    print()
    total = 0.0
    print("     planet      mass (kg)     L (kg m^2/s)   share of planets")
    lums = []
    for name, m, a, e in PLANETS:
        L = m * math.sqrt(GM_SUN_TAB * a * (1.0 - e ** 2))
        lums.append((name, L))
        total += L
    for name, L in lums:
        print(f"  {name:10s} {dict((n, mm) for n, mm, _a, _e in PLANETS)[name]:12.4e}"
              f"   {L:14.4e}   {L/total*100:10.2f} per cent")
    print()
    print(f"  total planetary orbital angular momentum = {total:.4e} kg m^2/s")
    m_planets = sum(mm for _n, mm, _a, _e in PLANETS)
    print(f"  total planetary mass = {m_planets:.4e} kg")
    print()
    m_sun, r_sun, p_sun = 1.98892e30, R_SUN, 25.38 * 86400.0
    omega = 2.0 * math.pi / p_sun
    print("  The Sun's rotational angular momentum needs a moment of inertia,")
    print("  and the Sun rotates differentially, so the value depends on the")
    print("  interior rotation profile.  Two coefficients bracket it:")
    for k in (0.4, 0.06):
        L = k * m_sun * r_sun ** 2 * omega
        print(f"    I = {k:.2f} M R^2 -> L_sun = {L:.4e} kg m^2/s"
              f" = {L/(total+L)*100:.3f} per cent of the system total")
    print()
    print(f"  Mass share of the Sun = "
          f"{m_sun/(m_sun+m_planets)*100:.4f} per cent.")
    print("  Angular-momentum share of the Sun is between about 0.5 and 3.5 per")
    print("  cent, i.e. the planets hold more than 96 per cent of the angular")
    print("  momentum and about 0.13 per cent of the mass.  The statement that")
    print("  survives is that ordering; any formation model has to explain how")
    print("  the disk shed or transported angular momentum outward.")


# --------------------------------------------------------------------------
# 4. Jeans escape
# --------------------------------------------------------------------------

# TABULATED: GM (m^3/s^2), radius (m), and an assumed exospheric temperature (K)
BODIES = {
    "Earth": (3.986004418e14, 6.3710e6, 1000.0),
    "Mars": (4.282837e13, 3.3895e6, 250.0),
    "Titan": (8.9781e12, 2.5747e6, 150.0),
}
GASES = {"H2": 2.016, "He": 4.003, "N2": 28.014, "CO2": 44.009, "CH4": 16.043}


def part4():
    section("4. The Jeans escape parameter: which gases a body keeps")
    print("  v_esc = sqrt(2 GM / R);  v_th = sqrt(3 k T / m);  lambda = v_esc^2/v_th^2")
    print("  Jeans escape is slow when lambda is large; the conventional")
    print("  criterion is that a gas is retained if lambda exceeds roughly 25")
    print("  over the age of the solar system.  The exospheric temperature is a")
    print("  MODEL/measured quantity, and lambda is exponentially sensitive to")
    print("  it, so the numbers below are order-of-magnitude statements.")
    print()
    for body, (gm, r, T) in BODIES.items():
        vesc = math.sqrt(2.0 * gm / r)
        print(f"  {body}: GM = {gm:.4e}, R = {r:.4e} m, T_exo = {T:.0f} K (assumed)")
        print(f"      v_esc = {vesc:.1f} m/s")
        print("        gas     m (u)   v_th (m/s)   lambda   retained?")
        for gas, mu in GASES.items():
            m = mu * U_KG
            vth = math.sqrt(3.0 * K_B * T / m)
            lam = (vesc / vth) ** 2
            print(f"  {gas:>9s}   {mu:7.3f}   {vth:10.1f}   {lam:7.1f}   "
                  f"{'yes' if lam > 25 else 'no'}")
        print()
    print("  Earth retains N2 and CO2 and loses H2 and He, which is the observed")
    print("  behaviour.  The Mars column is the instructive one: it predicts")
    print("  retention of N2, CO2 and CH4, yet the Martian surface pressure is")
    print("  about two orders of magnitude below the Earth's.  Escape over the")
    print("  age of the solar system from a body with less than half the Earth's")
    print("  escape velocity is what thinned it, and the isotope ratios that")
    print("  record that loss are not predicted by the thermal criterion alone.")
    print("  Treat lambda as a threshold, not as a prediction.")
    print()
    print("  WHERE THE CRITERION FAILS.  For water on Mars, lambda using an")
    print("  exospheric temperature of 250 K is:")
    gm, r, T = BODIES["Mars"]
    vesc = math.sqrt(2.0 * gm / r)
    for mu in (18.015,):
        vth = math.sqrt(3.0 * K_B * T / (mu * U_KG))
        print(f"      H2O: v_th = {vth:.1f} m/s, lambda = {(vesc/vth)**2:.0f},")
        print("  which the criterion says is safely retained — and yet Mars has")
        print("  lost most of its water.  The reason is that escape is not a")
        print("  Jeans problem for water: H2O is photodissociated in the upper")
        print("  atmosphere and the hydrogen produced escapes, which is a")
        print("  non-thermal, chemistry-limited process this criterion does not")
        print("  describe at all.  A criterion that is right for four gases is")
        print("  still not a theory of atmospheric loss.")


# --------------------------------------------------------------------------
# 5. Two-component densities
# --------------------------------------------------------------------------

def part5():
    section("5. Two-component mixing density, inverted")
    print("  For a body made of a rock component (density r1) and an ice")
    print("  component (density r2) with ice MASS fraction f the specific volume")
    print("  adds linearly:")
    print("      1/rho = f/rho_ice + (1-f)/rho_rock.")
    print("  This is a mass-balance identity, not a model.")
    print()
    r_rock, r_ice = 3500.0, 1000.0
    print(f"  rho_rock = {r_rock:.0f} kg/m^3, rho_ice = {r_ice:.0f} kg/m^3")
    print()
    print("     ice mass fraction f   uncompressed density (kg/m^3)")
    for f in (0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0):
        rho = 1.0 / (f / r_ice + (1.0 - f) / r_rock)
        print(f"  {f:19.2f}   {rho:30.1f}")
    print()
    print("  Inverted: f = (1/rho - 1/rho_rock) / (1/rho_ice - 1/rho_rock)")
    print()
    print("     measured rho (kg/m^3)   implied f")
    for rho in (3300.0, 3000.0, 2500.0, 2000.0, 1500.0):
        f = (1.0 / rho - 1.0 / r_rock) / (1.0 / r_ice - 1.0 / r_rock)
        print(f"  {rho:21.0f}   {f:10.4f}")
    print()
    print("  The catch is in the word UNCOMPRESSED.  A measured mean density is")
    print("  a compressed density, and removing the compression requires an")
    print("  interior model with a pressure-density relation — which is lesson")
    print("  02 of this module.  The mixing arithmetic above is exact; the")
    print("  quantity you feed it is not, and saying so is the difference")
    print("  between an inference and a guess.")


def main():
    print("Solar system architecture -- computed quantities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    part5()
    print()
    print("=" * 72)
    print("All planetary values used as inputs are TABULATED standard values,")
    print("labelled as such, and are subject to revision.")
    print("=" * 72)


if __name__ == "__main__":
    main()
