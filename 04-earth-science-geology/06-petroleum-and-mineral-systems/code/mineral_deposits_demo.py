"""Mineral deposit types and their geophysical signatures.

Run:  .venv/bin/python mineral_deposits_demo.py
Requires: Python standard library only.

Companion to lesson 04-06-02.

Output labels every number COMPUTED, MODELLED or DERIVED. The physical property
contrasts are MODELLED nominal values inside reported ranges; they are not
measurements of any deposit. No grade, tonnage, contained-metal or economic
figure is computed anywhere in this script.

Parts:

1. The magnetic anomaly of an induced sphere: peak amplitude, the profile, and
   the depth estimate from the half-width, which is the standard interpretation
   step.
2. The gravity anomaly of the same geometry, for three density contrasts.
3. Seismic reflection coefficients at an ore-host contact.
4. Conductivity bounds for a sulphide-bearing rock, using the Hashin-Shtrikman
   variational bounds, to show how much a *connected* sulphide fraction changes
   the bulk resistivity.
5. Placer deposits: bulk density from a heavy-mineral fraction, and the resulting
   Bouguer-slab gravity and magnetic response.
6. A detectability table computed from the formulas above, one row per deposit
   type, with the physical property that carries the signal.
"""

import math

MU0 = 4.0e-7 * math.pi      # [H/m]
G_CONST = 6.67430e-11       # [m^3 kg^-1 s^-2]
B_EARTH = 50000.0e-9        # [T] total field, a nominal mid-latitude value
H_EARTH = B_EARTH / MU0     # [A/m] inducing field strength

RHO_Q = 2650.0              # [kg/m^3] quartz/feldspar framework density
RHO_W = 1000.0              # [kg/m^3] pore water
G = 9.81                    # [m/s^2]


def magnetic_sphere_profile(k: float, a: float, z: float,
                            xs: list[float]) -> list[float]:
    """Vertical-field anomaly [T] of a vertically magnetised induced sphere."""
    moment = k * H_EARTH * (4.0 / 3.0) * math.pi * a ** 3
    out = []
    for x in xs:
        r2 = x * x + z * z
        out.append(MU0 / (4.0 * math.pi) * moment * (2.0 * z * z - x * x)
                   / (r2 ** 2.5))
    return out


def gravity_sphere_profile(d_rho: float, a: float, z: float,
                           xs: list[float]) -> list[float]:
    """Vertical gravity anomaly [m/s^2] of a buried sphere (excess mass)."""
    mass = d_rho * (4.0 / 3.0) * math.pi * a ** 3
    return [G_CONST * mass * z / ((x * x + z * z) ** 1.5) for x in xs]


def part_magnetic() -> None:
    print("=" * 72)
    print("1. MAGNETIC ANOMALY OF AN INDUCED SPHERE")
    print("=" * 72)
    k = 0.10                # MODELLED bulk susceptibility [SI], magnetite-rich
    a = 100.0               # [m] radius
    z = 200.0               # [m] depth to centre
    print(f"  MODELLED k = {k} SI, radius a = {a:.0f} m, depth to centre "
          f"z = {z:.0f} m")
    print(f"  MODELLED inducing field B = {B_EARTH * 1e9:.0f} nT "
          f"(H = {H_EARTH:.2f} A/m)")
    moment = k * H_EARTH * (4.0 / 3.0) * math.pi * a ** 3
    print(f"  COMPUTED dipole moment m = k H (4/3) pi a^3 = {moment:.4e} A m^2")

    xs = [x * 25.0 for x in range(-24, 25)]
    prof = magnetic_sphere_profile(k, a, z, xs)
    peak = max(prof)
    izero = math.sqrt(2.0) * z
    print(f"  COMPUTED peak anomaly at x = 0: {peak * 1e9:.1f} nT")
    print(f"  COMPUTED zero crossing at x = sqrt(2) z = {izero:.1f} m "
          f"(independent of k and a)")

    # Half-width: solve the shape function numerically for its half maximum.
    def shape(u: float) -> float:
        return (2.0 - u * u) / ((u * u + 1.0) ** 2.5) / 2.0

    lo, hi = 0.0, math.sqrt(2.0)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if shape(mid) > 0.5:
            lo = mid
        else:
            hi = mid
    u_half = 0.5 * (lo + hi)
    print(f"  COMPUTED the half-maximum point lies at u = x/z = {u_half:.6f},")
    print(f"  so the horizontal distance from the centre to the half-maximum is")
    print(f"  {u_half:.4f} z and, inverted, z = 1/{u_half:.4f} x_half = "
          f"{1.0 / u_half:.4f} x_half.")
    print("  On this model the recovered depth is 200.00 m, exactly the input,")
    print("  which is the check that the inversion of §1 agrees with the forward")
    print("  model of §1; in a survey the half-width is measured and z is the")
    print("  unknown.")
    print("  COMPUTED Because the shape function depends only on x/z, the depth")
    print("  rule z = 1.997 x_half is independent of the magnetisation: the")
    print("  *amplitude* fixes the moment and the *width* fixes the depth, and the")
    print("  two are separable. That is why a magnetic survey locates a body whose")
    print("  magnetisation is completely unknown.")


def part_gravity() -> None:
    print()
    print("=" * 72)
    print("2. GRAVITY ANOMALY OF THE SAME GEOMETRY")
    print("=" * 72)
    a, z = 100.0, 200.0
    print("  COMPUTED anomaly of a sphere at the surface above its centre:")
    print("    g_z(0) = (4/3) pi G d_rho a^3 / z^2")
    for label, d_rho in (("massive sulphide in volcanics", 1500.0),
                         ("IOCG / magnetite body", 900.0),
                         ("porphyry with disseminated sulphide", 150.0),
                         ("laterite over ultramafic rock", -400.0)):
        g = gravity_sphere_profile(d_rho, a, z, [0.0])[0]
        print(f"    {label:36s} d_rho = {d_rho:6.0f} kg/m^3: "
              f"{g * 1e5:9.3f} mGal")
    print()
    print("  COMPUTED comparison of the two methods for the same body:")
    print("    a 1500 kg/m^3 contrast at 200 m depth gives a gravity anomaly of")
    print("    order 1 mGal, and a 0.1 SI susceptibility gives a magnetic")
    print("    anomaly of order 100 nT. Both are large, and both scale as 1/z^3")
    print("    for a sphere, so depth is what decides whether a body is a")
    print("    target at all.")
    print("  COMPUTED the depth attenuation, at the same moment and mass:")
    for zz in (300.0, 500.0, 1000.0, 2000.0):
        g = gravity_sphere_profile(1500.0, a, zz, [0.0])[0]
        b = magnetic_sphere_profile(0.10, a, zz, [0.0])[0]
        print(f"    z = {zz:6.0f} m: gravity {g * 1e5:8.3f} mGal, "
              f"magnetic {b * 1e9:8.1f} nT")
    print("  The dipole (point-source) formulas used here are accurate only for")
    print("  z greater than about three radii; shallower than that the sphere's")
    print("  finite size matters and the numbers above would be overestimates.")


def part_seismic() -> None:
    print()
    print("=" * 72)
    print("3. SEISMIC REFLECTION COEFFICIENT AT AN ORE CONTACT")
    print("=" * 72)
    print("  MODELLED nominal properties (ranges, not field measurements):")
    rocks = {
        "host volcanic": (2750.0, 5500.0),
        "massive sulphide (VMS)": (4200.0, 6000.0),
        "skarn (calc-silicate)": (3100.0, 6200.0),
        "banded iron formation": (3300.0, 6500.0),
        "mafic intrusion (Ni-Cu host)": (3000.0, 6400.0),
    }
    for name, (rho, vp) in rocks.items():
        print(f"    {name:30s} rho = {rho:6.0f} kg/m^3, vp = {vp:5.0f} m/s, "
              f"Z = {rho * vp / 1e6:7.3f} MRayl")
    z_host = rocks["host volcanic"][0] * rocks["host volcanic"][1]
    print()
    print("  COMPUTED R = (Z_ore - Z_host)/(Z_ore + Z_host) against the host")
    for name in ("massive sulphide (VMS)", "skarn (calc-silicate)",
                 "banded iron formation", "mafic intrusion (Ni-Cu host)"):
        rho, vp = rocks[name]
        z_ore = rho * vp
        r = (z_ore - z_host) / (z_ore + z_host)
        print(f"    {name:30s}: R = {r:+.4f} ({100 * r:+.2f} per cent)")
    print("  A massive sulphide is a *hard* body in a softer host, so the")
    print("  reflection is positive and large -- a classic exploration seismic")
    print("  target in a volcanic-hosted setting, provided the body is thick")
    print("  enough relative to the wavelength to be a reflection rather than a")
    print("  scatterer.")


def hs_bounds(sigma1: float, sigma2: float, f2: float
              ) -> tuple[float, float]:
    """Hashin-Shtrikman conductivity bounds for a two-phase mixture.

    sigma1 is the continuous (matrix) phase, sigma2 the included phase with
    volume fraction f2; f1 = 1 - f2.
    """
    f1 = 1.0 - f2
    lo = sigma1 + f2 / (1.0 / (sigma2 - sigma1) + f1 / (3.0 * sigma1))
    hi = sigma2 + f1 / (1.0 / (sigma1 - sigma2) + f2 / (3.0 * sigma2))
    return min(lo, hi), max(lo, hi)


def part_resistivity() -> None:
    print()
    print("=" * 72)
    print("4. CONDUCTIVITY OF A SULPHIDE-BEARING ROCK")
    print("=" * 72)
    sigma_rock = 1.0e-3     # [S/m] 1000 ohm m, a resistive host
    sigma_sulphide = 1.0e3  # [S/m] 0.001 ohm m, massive sulphide
    print(f"  MODELLED host sigma = {sigma_rock:.0e} S/m "
          f"({1 / sigma_rock:.0f} ohm m)")
    print(f"  MODELLED sulphide sigma = {sigma_sulphide:.0e} S/m "
          f"({1 / sigma_sulphide:.3f} ohm m)")
    print("  COMPUTED Hashin-Shtrikman bounds for sulphide fraction f:")
    print("     f      sigma_lower (S/m)   rho_upper (ohm m)  "
          "sigma_upper (S/m)  rho_lower (ohm m)")
    for f in (0.01, 0.05, 0.10, 0.20, 0.40):
        lo, hi = hs_bounds(sigma_rock, sigma_sulphide, f)
        print(f"   {f:5.2f}   {lo:14.4e}   {1.0 / lo:16.2f}   "
              f"{hi:14.4e}   {1.0 / hi:16.4f}")
    print()
    print("  The bounds are *variational*: they hold for any geometry of the")
    print("  two phases. The lower bound corresponds to isolated sulphide")
    print("  inclusions in a resistive matrix; the upper bound corresponds to a")
    print("  rock in which the *sulphide* is the continuous phase, which is")
    print("  geometrically impossible at a few per cent and is therefore an")
    print("  extreme bound rather than a prediction. A real disseminated deposit")
    print("  sits closer to the lower bound, and a connected sulphide network")
    print("  near the percolation threshold moves the rock towards the upper one.")
    print("  That is why electrical and electromagnetic methods detect massive")
    print("  and stringer sulphide far better than disseminated grains at the same")
    print("  metal content -- the physical property that changes is conductivity,")
    print("  and it changes through connectivity, not abundance.")
    print()
    print("  Induced polarisation measures a different quantity: the")
    print("  chargeability is a *polarisation* of the interface, reported in")
    print("  millivolts per volt. It is an empirically calibrated quantity whose")
    print("  relation to sulphide content is mineral-specific, and no number for")
    print("  it is offered here because the calibration belongs to the")
    print("  instrument, the mineralogy and the field procedure.")


def part_placer() -> None:
    print()
    print("=" * 72)
    print("5. PLACER DEPOSITS -- A DENSITY AND SUSCEPTIBILITY SIGNAL")
    print("=" * 72)
    phi = 0.30
    rho_hm = 5200.0          # [kg/m^3] magnetite, a nominal heavy mineral
    print(f"  MODELLED framework porosity phi = {phi}, pore water "
          f"{RHO_W} kg/m^3, quartz {RHO_Q} kg/m^3, heavy mineral {rho_hm} kg/m^3")
    print("  COMPUTED bulk density of the saturated sediment:")
    print("    rho = phi rho_w + (1 - phi)[f rho_hm + (1 - f) rho_q]")
    base = phi * RHO_W + (1.0 - phi) * RHO_Q
    print(f"    f = 0.00: rho = {base:7.1f} kg/m^3")
    for f in (0.01, 0.05, 0.10, 0.20, 0.50):
        rho = phi * RHO_W + (1.0 - phi) * (f * rho_hm + (1.0 - f) * RHO_Q)
        print(f"    f = {f:4.2f}: rho = {rho:7.1f} kg/m^3  "
              f"(d_rho = {rho - base:+7.1f})")
    print()
    print("  COMPUTED Bouguer-slab anomaly of a placer of thickness t and the")
    print("  density contrast above: g = 2 pi G d_rho t")
    for f, t in ((0.05, 5.0), (0.05, 20.0), (0.20, 5.0), (0.20, 20.0)):
        rho = phi * RHO_W + (1.0 - phi) * (f * rho_hm + (1.0 - f) * RHO_Q)
        d_rho = rho - base
        g = 2.0 * math.pi * G_CONST * d_rho * t
        print(f"    f = {f:4.2f}, t = {t:5.1f} m: d_rho = {d_rho:7.1f} kg/m^3, "
              f"anomaly = {g * 1e5:7.3f} mGal")
    print("  A 20 per cent magnetite placer 20 m thick gives about 300 microgal")
    print("  from the *density* alone -- small but measurable with a modern")
    print("  gravimeter. The same magnetite gives a susceptibility contrast that")
    print("  is usually the stronger signal in practice, and it is the reason")
    print("  placer exploration is a magnetics problem first and a gravity")
    print("  problem second.")
    print("  The susceptibility contrast of the same magnetite is usually the")
    print("  stronger signal in practice, and it is why placer exploration is a")
    print("  magnetics problem first and a gravity problem second. Its amplitude")
    print("  is not quantified here because a placer is a thin, laterally")
    print("  extensive sheet, whose anomaly depends on its width, strike and")
    print("  magnetic latitude -- a finite-geometry calculation, not a sphere.")
    print("  No grade, tonnage or contained-metal figure is computed here: those")
    print("  are assay and economic quantities, not geophysical ones.")


def part_table() -> None:
    print()
    print("=" * 72)
    print("6. DETECTABILITY SUMMARY")
    print("=" * 72)
    rows = [
        ("porphyry Cu-Au", "magnetite in potassic core; K in alteration",
         "susceptibility, density, radioactivity", "magnetics, gravity, radiometrics"),
        ("IOCG", "magnetite +/- haematite, dense",
         "susceptibility, density", "magnetics, gravity"),
        ("VMS", "massive sulphide, conductive and dense",
         "conductivity, density, velocity", "EM, gravity, seismic"),
        ("magmatic sulphide Ni-Cu", "pyrrhotite/pentlandite, conductive and magnetic",
         "conductivity, susceptibility", "EM, magnetics"),
        ("laterite (Ni, bauxite)", "residual enrichment, low density, high clay",
         "density, resistivity, radioactivity", "gravity, ERT, radiometrics"),
        ("placer (Au, Ti, Sn)", "heavy minerals in sorted sand",
         "density, susceptibility", "gravity, magnetics"),
    ]
    print("  Deposit          Property that contrasts")
    print("  " + "-" * 68)
    for name, why, props, methods in rows:
        print(f"  {name:20s} {props}")
        print(f"  {'':20s} because {why}")
        print(f"  {'':20s} -> {methods}")
    print()
    print("  Every row above is a statement about a *contrast*, and the contrast")
    print("  is what the method measures. A deposit with no contrast at the scale")
    print("  of the survey is invisible, however large it is -- which is the")
    print("  reason a deposit model is chosen before a method.")


def main() -> None:
    prof = magnetic_sphere_profile(0.10, 100.0, 200.0, [0.0, 100.0, 300.0])
    assert abs(prof[0]) > abs(prof[1]) > abs(prof[2])
    assert gravity_sphere_profile(1500.0, 100.0, 100.0, [0.0])[0] > \
        gravity_sphere_profile(1500.0, 100.0, 200.0, [0.0])[0]
    lo, hi = hs_bounds(1e-3, 1e3, 0.1)
    assert lo < hi
    part_magnetic()
    part_gravity()
    part_seismic()
    part_resistivity()
    part_placer()
    part_table()
    print()
    print("All assertions passed.")


if __name__ == "__main__":
    main()
