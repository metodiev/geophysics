"""Planetary interiors and magnetic fields: hydrostatic equilibrium inward.

Run:  .venv/bin/python planetary_interiors_demo.py
Requires: numpy.

Companion to lesson 04-08-02.

1. Hydrostatic equilibrium integrated through a two-layer interior: the mass
   comes out of the density profile, and the central pressure comes out of the
   integration.  Two models are compared with the seismological value, and the
   comparison is the point: a central pressure is a MODEL OUTPUT, never a
   measurement.
2. The moment-of-inertia factor C/(M R^2), computed for a uniform sphere, for
   a two-layer model, and inverted for the core density that would reproduce
   the geodetic value.  The inversion fails in an informative way.
3. The magnetic Reynolds number, the diffusion time, and what a dynamo needs.
4. The dipole moment implied by the surface field, and the magnetisation that
   would be required if the field were remanent instead of generated.
5. Electromagnetic induction and the skin depth, which is how a subsurface
   ocean is detected from outside a body.

Every input density is NOMINAL and labelled; the geodetic and seismological
reference values are TABULATED inferences, labelled as inferences, because
neither the central pressure nor the moment of inertia has been measured
directly.
"""

import math

import numpy as np

G = 6.67430e-11
MU_0 = 1.25663706212e-6     # N/A^2, exact (SI)

R_EARTH = 6.371e6           # m, mean radius (tabulated)
M_EARTH = 5.9722e24         # kg, tabulated
C_FACTOR_GEODETIC = 0.3308  # TABULATED inference for the Earth (precession + J2)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Hydrostatic equilibrium
# --------------------------------------------------------------------------

def integrate_interior(radius, rho_core, r_core, rho_mantle, n=200000):
    """Return (mass, central pressure, r, rho, P) for a two-layer body.

    dM/dr = 4 pi r^2 rho,  g = G M / r^2,  dP/dr = -rho g, with P(R) = 0.
    """
    r = np.linspace(1.0, radius, n)
    rho = np.where(r < r_core, rho_core, rho_mantle)
    dm = 4.0 * math.pi * r ** 2 * rho * np.gradient(r)
    m = np.cumsum(dm)
    g = G * m / r ** 2
    dp = -rho * g * np.gradient(r)      # dP outward
    p = -np.cumsum(dp[::-1])[::-1]      # integrate inward from P(R) = 0
    return m[-1], float(p[0]), r, rho, p


def part1():
    section("1. Hydrostatic equilibrium: mass and central pressure")
    print("  Equations: dM/dr = 4 pi r^2 rho;  dP/dr = -rho g;  g = G M/r^2.")
    print("  These are exact statements about a spherically symmetric body in")
    print("  hydrostatic equilibrium.  Everything uncertain is in rho(r).")
    print()
    print("  Model A: uniform density at the mean density of the Earth.")
    rho_mean = M_EARTH / (4.0 / 3.0 * math.pi * R_EARTH ** 3)
    p_uni = 2.0 / 3.0 * math.pi * G * rho_mean ** 2 * R_EARTH ** 2
    print(f"    rho_mean = M/(4/3 pi R^3) = {rho_mean:.1f} kg/m^3")
    print(f"    P_centre = (2/3) pi G rho^2 R^2 = {p_uni/1e9:.1f} GPa   (analytic)")
    m_uni, p_c_uni, _r, _rho, _p = integrate_interior(R_EARTH, rho_mean, 0.0, rho_mean)
    print(f"    the same quantity from the numerical integration = "
          f"{p_c_uni/1e9:.1f} GPa")
    print("    (the agreement of the analytic and numerical values is the check")
    print("    that the integration is right; the model itself is what is wrong)")
    print()
    print("  Model B: two layers, NOMINAL densities and a core radius.")
    r_core = 3480.0e3
    rho_core, rho_mantle = 11000.0, 4500.0
    m, p_c, _r, _rho, p = integrate_interior(R_EARTH, rho_core, r_core, rho_mantle)
    print(f"    core radius {r_core/1e3:.0f} km, rho_core = {rho_core:.0f}, "
          f"rho_mantle = {rho_mantle:.0f} kg/m^3")
    print(f"    mass from the profile   = {m:.4e} kg")
    print(f"    tabulated Earth mass    = {M_EARTH:.4e} kg"
          f"   (difference {abs(m-M_EARTH)/M_EARTH*100:.2f} per cent)")
    print(f"    central pressure        = {p_c/1e9:.1f} GPa")
    print(f"    pressure at the core-mantle boundary = "
          f"{p[np.searchsorted(_r, r_core)]/1e9:.1f} GPa")
    print()
    print("  The seismological reference for the Earth's central pressure is")
    print("  about 364 GPa (Preliminary Reference Earth Model, PREM, and its")
    print("  successors).  That number is not measured: it is obtained by")
    print("  integrating dP/dr = -rho g through a density profile that is itself")
    print("  inferred from seismic velocities, an equation of state and the")
    print("  mass.  A model that gives 173 GPa (uniform) or a few hundred GPa")
    print("  (layered) is not competing with a measurement; it is competing with")
    print("  another model, and the seismological one wins because it is")
    print("  constrained by data the others are not.")
    print()
    print("  Central pressure for the same body with different assumed profiles:")
    print("     rho_core   rho_mantle   mass (1e24 kg)   P_centre (GPa)")
    for rc, rm in ((10000.0, 4000.0), (11000.0, 4500.0), (13000.0, 5000.0),
                   (12000.0, 4200.0)):
        mm, pp, _r2, _rh2, _p2 = integrate_interior(R_EARTH, rc, r_core, rm, n=40000)
        print(f"  {rc:10.0f}   {rm:10.0f}   {mm/1e24:15.4f}   {pp/1e9:14.1f}")
    print()
    print("  The last row reproduces the seismological central pressure while")
    print("  its mass is 0.7 per cent low.  A two-parameter model that hits one")
    print("  target can miss another, and the target it hit was chosen to be")
    print("  hit.  This is why a central pressure is described as a property of")
    print("  a model and not of a planet.")


# --------------------------------------------------------------------------
# 2. Moment of inertia
# --------------------------------------------------------------------------

def c_factor(radius, rho_core, r_core, rho_mantle, n=200000):
    """C/(M R^2) for a two-layer body.  C = (8 pi/3) integral rho r^4 dr."""
    r = np.linspace(1.0, radius, n)
    rho = np.where(r < r_core, rho_core, rho_mantle)
    dr = np.gradient(r)
    m = float(np.sum(4.0 * math.pi * r ** 2 * rho * dr))
    c = float(np.sum(8.0 / 3.0 * math.pi * rho * r ** 4 * dr))
    return c / (m * radius ** 2), m


def part2():
    section("2. The moment-of-inertia factor, and an inversion that fails")
    print("  C = (8 pi/3) integral rho r^4 dr over shells; alpha = C/(M R^2).")
    print("  For a uniform sphere alpha = (8 pi/15)/(4 pi/3) = 0.4 exactly,")
    print("  whatever the density.  Central condensation lowers it.")
    print()
    print("  Model A (uniform):")
    rho_mean = M_EARTH / (4.0 / 3.0 * math.pi * R_EARTH ** 3)
    a_uni, m_uni = c_factor(R_EARTH, rho_mean, 0.0, rho_mean, n=100000)
    print(f"    alpha = {a_uni:.6f}   (the analytic limit is 0.4)")
    print()
    print("  Model B (two layers), core radius 3480 km:")
    print("     rho_core   rho_mantle   alpha      mass (1e24 kg)")
    for rc, rm in ((9000.0, 4000.0), (10000.0, 4200.0), (11000.0, 4500.0),
                   (13000.0, 5000.0)):
        aa, mm = c_factor(R_EARTH, rc, 3480.0e3, rm, n=60000)
        print(f"  {rc:10.0f}   {rm:10.0f}   {aa:8.5f}   {mm/1e24:14.4f}")
    print()
    print(f"  The geodetic inference for the Earth is alpha = "
          f"{C_FACTOR_GEODETIC:.4f} (from the precession constant and J2,")
    print("  through the Darwin-Radau relation, which ASSUMES hydrostatic")
    print("  equilibrium; both the value and the assumption are tabulated")
    print("  inferences, not measurements).")
    print()
    print("  Every plausible two-layer model above gives an alpha ABOVE the")
    print("  geodetic value, i.e. too little central condensation.  Invert for")
    print("  the core density that would reproduce it at the same core radius:")
    lo, hi = 10500.0, 30000.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        aa, _mm = c_factor(R_EARTH, mid, 3480.0e3, 4500.0, n=40000)
        if aa > C_FACTOR_GEODETIC:
            lo = mid
        else:
            hi = mid
    aa, mm = c_factor(R_EARTH, 0.5 * (lo + hi), 3480.0e3, 4500.0, n=100000)
    print(f"    required rho_core = {0.5*(lo+hi):.0f} kg/m^3, giving alpha = "
          f"{aa:.4f} and M = {mm/1e24:.3f}e24 kg")
    print()
    print("  Seismology puts the outer core near 10-12 thousand kg/m^3 and the")
    print("  inner core a little above 13 thousand, so the required value is far")
    print("  too high, and the mass it implies is wrong too.  The conclusion is")
    print("  that a two-layer model is inadequate: the moment of inertia cannot")
    print("  be matched by a uniform mantle, because the real mantle density")
    print("  increases with depth.  The inversion did not give an answer; it")
    print("  gave a diagnosis, which is what a failed inversion is for.")


# --------------------------------------------------------------------------
# 3. Dynamo requirements
# --------------------------------------------------------------------------

def part3():
    section("3. What a dynamo requires: Rm, and the diffusion time")
    print("  Magnetic Reynolds number  Rm = mu_0 sigma U L,")
    print("  diffusion time            tau = L^2 / eta,  eta = 1/(mu_0 sigma).")
    print("  A dynamo sustains a field only if Rm exceeds a critical value;")
    print("  numerical experiments put that threshold somewhere in the range")
    print("  10 to 100 depending on the flow geometry, so treat it as an order")
    print("  of magnitude, not a constant.")
    print()
    u, l = 5.0e-4, 2.0e6      # m/s and m, NOMINAL core flow speed and length
    print(f"  NOMINAL core flow U = {u:.1e} m/s, length scale L = {l:.1e} m")
    print()
    print("     sigma (S/m)   Rm        tau = mu_0 sigma L^2")
    for sigma in (1.0e5, 3.0e5, 5.0e5, 1.0e6, 1.5e6):
        rm = MU_0 * sigma * u * l
        tau = MU_0 * sigma * l ** 2
        print(f"  {sigma:12.1e}   {rm:9.2f}   {tau/(365.25*86400):10.1f} yr")
    print()
    print("  Every entry exceeds the threshold: the core is a dynamo unless the")
    print("  flow is far slower than assumed.  The diffusion time is the more")
    print("  useful number: it is how long the field would persist if the flow")
    print("  stopped, and it is tens of thousands of years, which is why the")
    print("  field has not decayed away and why reversals take thousands of")
    print("  years rather than days.  It also means a dynamo is NOT needed to")
    print("  explain the field's existence in any single instant — only its")
    print("  persistence over geological time.")
    print()
    print("  The requirements a dynamo imposes on a body, then, are: a")
    print("  conducting fluid region; convection or another source of kinetic")
    print("  energy in that region; and sufficient electrical conductivity.")
    print("  A body that fails any one of those has no intrinsic field, and")
    print("  crustal remanent magnetism is the fossil of a time when it did.")


# --------------------------------------------------------------------------
# 4. Dipole moment
# --------------------------------------------------------------------------

def part4():
    section("4. The dipole moment from the surface field")
    print("  For a centred dipole, B_r = (mu_0/4 pi) 2 m cos(theta) / r^3 and")
    print("  B_theta = (mu_0/4 pi) m sin(theta) / r^3, so the equatorial")
    print("  surface field gives  m = (4 pi / mu_0) B_eq R^3.")
    print()
    b_eq = 3.1e-5       # T, order of the equatorial surface field of the Earth
    bb_equiv = b_eq / 1e-9
    m = 4.0 * math.pi / MU_0 * b_eq * R_EARTH ** 3
    print(f"  B_eq = {bb_equiv:.0f} nT (the surface field is about 30 000 nT,")
    print("  latitude-dependent; the dipole term is roughly this)")
    print(f"  m = {m:.4e} A m^2")
    print("  The tabulated value of the Earth's dipole moment from geomagnetic")
    print("  field models such as IGRF is a little under 8e22 A m^2, so the")
    print("  conversion is right to a few per cent and the residual is the")
    print("  non-dipole part of the field.  Confirm the current value in the")
    print("  current IGRF release; the moment is decreasing by a fraction of a")
    print("  per cent per decade.")
    print()
    r_core = 3480.0e3
    vol = 4.0 / 3.0 * math.pi * r_core ** 3
    mag = m / vol
    print("  If that moment were remanent magnetisation of the whole core:")
    print(f"    M = m / V_core = {mag:.1f} A/m")
    print("  which is small compared with the saturation magnetisation of iron")
    print("  (of order 1e6 A/m).  So the required magnetisation is easy, and the")
    print("  argument for a dynamo is not the amplitude.  It is (i) the field")
    print("  changes on a human timescale, which a fossil cannot do, and (ii)")
    print("  the core is far above the Curie temperature of iron, near 1043 K,")
    print("  so ferromagnetic ordering cannot persist there at all.")


# --------------------------------------------------------------------------
# 5. Induction and skin depth
# --------------------------------------------------------------------------

def skin_depth(sigma, period):
    """delta = sqrt(2 / (mu_0 sigma omega)) for a good conductor."""
    omega = 2.0 * math.pi / period
    return math.sqrt(2.0 / (MU_0 * sigma * omega))


def part5():
    section("5. Induction: skin depth, and detecting an ocean from outside")
    print("  A time-varying external field diffuses into a conductor with skin")
    print("  depth  delta = sqrt(2 / (mu_0 sigma omega)).")
    print("  If a conducting layer is thin compared with delta, the induced")
    print("  field is weak; if it is thick, the layer responds as a perfect")
    print("  conductor and the induced dipole is strong.  That is the whole")
    print("  basis of induction sounding of a planetary body.")
    print()
    print("  Periods that matter for a satellite in a planetary magnetosphere:")
    for name, period in (("synodic period, 11.2 h", 11.2 * 3600.0),
                         ("spin period, 1 d", 86400.0),
                         ("orbit period, 3.55 d", 3.55 * 86400.0)):
        print(f"    {name}: T = {period:.4e} s")
    print()
    print("     sigma (S/m)   delta at 11.2 h (km)   delta at 3.55 d (km)")
    for sigma in (0.1, 1.0, 3.0, 10.0):
        d1 = skin_depth(sigma, 11.2 * 3600.0) / 1000.0
        d2 = skin_depth(sigma, 3.55 * 86400.0) / 1000.0
        print(f"  {sigma:12.1f}   {d1:20.1f}   {d2:19.1f}")
    print()
    print("  For a conductivity of order 1 S/m (a salty ocean; the salinity of")
    print("  any particular ocean is an assumption), the skin depth at an 11 h")
    print("  period is about a hundred kilometres.  An ocean thinner than that")
    print("  induces less than the full response, so the amplitude of the")
    print("  induced field is a constraint on ocean thickness AND conductivity")
    print("  AND the conductivity of everything above and below it.")
    print("  Induction measures a product, not a thickness: reporting it as an")
    print("  ocean thickness requires a model that fixes the other factors.")


def main():
    print("Planetary interiors and magnetic fields -- computed quantities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    part5()
    print()
    print("=" * 72)
    print("Densities are NOMINAL; the seismological central pressure, the")
    print("geodetic moment-of-inertia factor and the dipole moment are")
    print("TABULATED inferences, labelled as such and subject to revision.")
    print("=" * 72)


if __name__ == "__main__":
    main()
