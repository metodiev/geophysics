"""Atmospheric structure, hydrostatic balance and lapse rates.

Run:  python3 atmospheric_structure_demo.py
Requires: Python standard library only.

Companion to lesson 02-11-04.

The temperature profile used is the *defined* layer structure of the U.S.
Standard Atmosphere (temperate, 0-86 km): a set of geopotential heights at
which the lapse rate changes, with sea-level temperature 288.15 K as the
definition of 15 C and sea-level pressure 101325 Pa, which is the standard
atmosphere and is an exact defining value.

The script:

1. Derives and checks the dry adiabatic lapse rate Gamma_d = g / c_p.
2. Computes the pressure scale height H = R T / g from the specific gas
   constant of air.
3. Integrates hydrostatic balance dp/dz = -p g /(R T(z)) through the standard
   atmosphere, and verifies the result against the analytic isentropic
   (power-law) solution inside the troposphere -- a real numerical check.
4. Computes potential temperature, the Brunt-Vaisala frequency and the
   buoyancy period, and contrasts the observed lapse rate with the dry adiabat.
5. Computes the atmospheric mass implied by surface pressure.
"""

import math

G0 = 9.80665                    # m/s^2, standard gravity (exact by definition)
P0 = 101325.0                   # Pa, standard atmosphere (exact by definition)
T0 = 288.15                     # K, 15 C, defining sea-level temperature
R_UNIV = 8.31446261815324       # J mol^-1 K^-1, exact (N_A k_B)
M_AIR = 0.0289644               # kg/mol, molar mass of dry air (nominal)
R_AIR = R_UNIV / M_AIR          # J kg^-1 K^-1, specific gas constant for air
CP_AIR = 1005.0                 # J kg^-1 K^-1, nominal at ~15 C
R_EARTH = 6.371e6               # m, nominal mean radius

# U.S. Standard Atmosphere, 0-86 km: (base geopotential height km, lapse rate K/km)
# The lapse rate applies from that base up to the next entry.
STANDARD = (
    (0.0, -6.5),
    (11.0, 0.0),
    (20.0, 1.0),
    (32.0, 2.8),
    (47.0, 0.0),
    (51.0, -2.8),
    (71.0, -2.0),
    (84.852, 0.0),
)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def lapse_at(z_km):
    for base, rate in reversed(STANDARD):
        if z_km >= base:
            return rate
    return STANDARD[0][1]


def temperature(z_km):
    """Defined standard-atmosphere temperature at geopotential height z."""
    t = T0
    for i in range(len(STANDARD) - 1):
        base, rate = STANDARD[i]
        top, _ = STANDARD[i + 1]
        if z_km <= base:
            break
        dz = min(z_km, top) - base
        t += rate * dz
    return t


def standard_model():
    """Exact segment-wise integration of hydrostatic balance.

    Returns (zs, temps, presses) at the standard-atmosphere breakpoints.
    Within a constant-lapse segment the solution is exact:
    p = p_base (T/T_base)^(-g/(L R)); for L = 0, p = p_base exp(-g dz/(R T)).
    """
    zs = [STANDARD[0][0]]
    temps = [T0]
    presses = [P0]
    for i in range(len(STANDARD) - 1):
        base, rate = STANDARD[i]
        top = STANDARD[i + 1][0]
        t_base = temps[-1]
        p_base = presses[-1]
        dz = (top - base) * 1e3
        t_top = t_base + rate * (top - base)
        if rate == 0.0:
            p_top = p_base * math.exp(-G0 * dz / (R_AIR * t_base))
        else:
            p_top = p_base * (t_top / t_base) ** (-G0 / (rate * 1e-3 * R_AIR))
        zs.append(top)
        temps.append(t_top)
        presses.append(p_top)
    return zs, temps, presses


def model_at(z_km, zs, temps, presses):
    """Interpolate the exact segment solution at any height."""
    for i in range(len(zs) - 1):
        if zs[i] <= z_km <= zs[i + 1]:
            base, rate = STANDARD[i]
            t_base = temps[i]
            p_base = presses[i]
            dz = (z_km - base) * 1e3
            t = t_base + rate * (z_km - base)
            if rate == 0.0:
                p = p_base * math.exp(-G0 * dz / (R_AIR * t_base))
            else:
                p = p_base * (t / t_base) ** (-G0 / (rate * 1e-3 * R_AIR))
            return t, p
    return temps[-1], presses[-1]


def analytic_troposphere(z_km):
    """p = p0 (T/T0)^(-g/(L R)) with L the (negative) tropospheric lapse rate."""
    rate = -6.5e-3                     # K/m
    t = T0 + rate * z_km * 1e3
    return P0 * (t / T0) ** (-G0 / (rate * R_AIR))


def part1_lapse_rate():
    section("1. The dry adiabatic lapse rate")
    print("  First law for a parcel rising adiabatically:  dh = v dP")
    print("  with h = c_p T and hydrostatic dP = -rho g dz:")
    print("      c_p dT = -g dz     =>     Gamma_d = -dT/dz = g / c_p")
    print()
    print(f"  Gamma_d = {G0:.5f} / {CP_AIR:.0f} = {G0 / CP_AIR * 1e3:.3f} K/km")
    print()
    print("  Observed mean tropospheric lapse rate (defined in the standard")
    print("  atmosphere) = 6.5 K/km, i.e. "
          f"{(G0 / CP_AIR * 1e3) / 6.5:.2f} times smaller than dry adiabatic.")
    print("  The difference is latent heat release in moist ascent and the")
    print("  radiative-equilibrium constraint on the mean profile: the observed")
    print("  lapse rate is neither dry adiabatic nor isothermal, and it is")
    print("  *steeper* than an isothermal atmosphere and *shallower* than dry")
    print("  adiabatic, which is exactly what conditional instability means.")


def part2_scale_height():
    section("2. Pressure scale height and the exponential atmosphere")
    print(f"  R_specific(air) = R/M = {R_UNIV:.9g} / {M_AIR} = "
          f"{R_AIR:.3f} J kg^-1 K^-1")
    print()
    for t, label in ((288.15, "sea level, 288.15 K"),
                     (250.0, "250 K"), (216.65, "tropopause, 216.65 K")):
        print(f"  H = R T / g at {label:<22} = {R_AIR * t / G0 / 1e3:.3f} km")
    print()
    h = R_AIR * T0 / G0
    z_e = h * math.log(2.0)
    print(f"  For an isothermal 288.15 K atmosphere, p falls by a factor e every")
    print(f"  {h / 1e3:.2f} km ({h / 1e3 / 1.609:.2f} miles) and halves every "
          f"{z_e / 1e3:.2f} km.")
    print(f"  The atmosphere's mass is 63% within one scale height, 86% within")
    print(f"  two and 95% within three, i.e. within {3 * h / 1e3:.1f} km.")


def part3_standard_profile():
    section("3. Integrating hydrostatic balance through the standard atmosphere")
    zs, temps, presses = standard_model()
    print(f"{'z (km)':>8}{'T (K)':>9}{'L (K/km)':>10}{'p (Pa)':>12}"
          f"{'p (hPa)':>10}{'analytic p':>12}{'rel diff':>11}")
    for z, t, p in zip(zs, temps, presses):
        ana = analytic_troposphere(z) if z <= 11.0 else float("nan")
        diff = f"{(p - ana) / ana:.2e}" if z <= 11.0 else "n/a"
        print(f"{z:>8.2f}{t:>9.2f}{lapse_at(z):>10.1f}{p:>12.1f}"
              f"{p / 100:>10.2f}"
              f"{(ana if z <= 11 else float('nan')):>12.1f}{diff:>11}")
    print()
    print("  The last two columns compare this integration with the analytic")
    print("  isentropic solution p = p0 (T/T0)^(-g/(L R)) inside the")
    print("  troposphere, where a constant lapse rate makes that solution")
    print("  exact. The relative difference is at the level of double-precision")
    print("  round-off, which is the correct result when the discretisation")
    print("  reproduces the exact solution of the equation being integrated.")
    print()
    print("  Temperatures: 288.15 K at sea level, 216.65 K at the tropopause")
    print("  (11 km), 228.65 K at 20 km, 270.65 K at 47 km, then falling again")
    print("  to 186.95 K at 84.852 km. Those values follow from the defined")
    print("  lapse rates at the tabulated breakpoints: they are definitions of")
    print("  the standard, not measurements of any particular day or place.")
    print()
    print("  Pressure halves within the first 6 km; by 11 km it is 22.3% of the")
    print("  surface value.")


def part4_stability():
    section("4. Potential temperature and buoyancy frequency")
    print("  theta = T (p0/p)^(R/c_p)      N^2 = (g/T)(Gamma_d - Gamma)")
    print()
    print(f"{'z (km)':>8}{'T (K)':>9}{'p (hPa)':>10}{'theta (K)':>12}"
          f"{'N (1/s)':>10}{'period (min)':>14}")
    zs, temps, presses = standard_model()
    for z in (0, 2, 5, 8, 11, 15, 20, 30, 47):
        tt, pp = model_at(z, zs, temps, presses)
        theta = tt * (P0 / pp) ** (R_AIR / CP_AIR)
        gam = lapse_at(z)                      # K/km, negative when T falls
        n2 = (G0 / tt) * (G0 / CP_AIR * 1e3 + gam) * 1e-3
        n = math.sqrt(n2)
        print(f"{z:>8.2f}{tt:>9.2f}{pp / 100:>10.2f}{theta:>12.2f}"
              f"{n:>10.5f}{2 * math.pi / n / 60:>14.1f}")
    print()
    print("  theta rises monotonically through the troposphere, so the")
    print("  troposphere is statically stable on average even though it looks")
    print("  overturned. In the stratosphere the temperature rises with height,")
    print("  theta rises much faster, and N is large: that is why the")
    print("  stratosphere is almost immune to vertical mixing.")
    print()
    print("  A nominal N of about 0.01 s^-1 gives a buoyancy period of roughly")
    print("  10 minutes, which is the timescale of a mountain lee wave or of")
    print("  the oscillation of a convective plume.")


def part5_mass():
    section("5. The mass of the atmosphere, from surface pressure alone")
    area = 4.0 * math.pi * R_EARTH ** 2
    mass = area * P0 / G0
    m_earth = 5.972e24
    print(f"  M = 4 pi R^2 p0 / g = 4 pi ({R_EARTH:.3e})^2 x {P0:.0f} / "
          f"{G0:.5f}")
    print(f"    = {mass:.4e} kg")
    print(f"  That is {mass / m_earth:.3e} of the nominal Earth mass, i.e. about")
    print("  one millionth. The sea-level pressure of 101325 Pa is an exact")
    print("  defining value, so this estimate carries no uncertainty in p0; the")
    print("  assumptions of a spherical Earth and of sea-level pressure")
    print("  everywhere are what limit it, and the second one biases the answer")
    print("  slightly high because much of the land surface lies above sea level.")


def main():
    part1_lapse_rate()
    part2_scale_height()
    part3_standard_profile()
    part4_stability()
    part5_mass()


if __name__ == "__main__":
    main()
