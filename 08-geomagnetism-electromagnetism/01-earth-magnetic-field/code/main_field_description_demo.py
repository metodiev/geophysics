#!/usr/bin/env python3
"""Describing the main field: the seven magnetic elements, their algebra, and
the unit conversions and sensitivities that go with them.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python main_field_description_demo.py

Everything here is SYNTHETIC.  The "sites" are chosen teaching vectors, not
measurements, and no observatory, survey or published field model is used.

Contents
--------
1. Field vector (X, Y, Z) -> elements (H, F, D, I); round-trip check.
2. Units: nT, T, gamma, and the equivalent magnetising field in A/m.
3. Sensitivity of D and I to component errors (small-angle and exact).
4. Element table for synthetic sites at several dipole inclinations.
5. Angular resolution: arcminutes, and what 1 nT buys in D and I.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NT_TO_T = 1.0e-9          # exact definition of the nanotesla
MU0 = 4.0e-7 * np.pi      # H/m, exact SI constant

# --- SYNTHETIC site: a chosen teaching field vector, north/east/down in nT ----
SITES = {
    "site A: mid-latitude": (20000.0, 1500.0, 42000.0),
    "site B: dip-equator side": (27000.0, -2500.0, 3000.0),
    "site C: high latitude": (9000.0, 800.0, 53000.0),
    "site D: near the dip pole": (400.0, 250.0, 58000.0),
}


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def elements(X, Y, Z):
    """(X, Y, Z) in nT -> (H, F, D_deg, I_deg).

    Convention: X north, Y east, Z down, all positive in nT.  D is measured
    clockwise (east) from geographic north, I downward from the horizontal.
    """
    H = np.hypot(X, Y)
    F = np.hypot(H, Z)
    D = np.degrees(np.arctan2(Y, X))
    I = np.degrees(np.arctan2(Z, H))
    return H, F, D, I


def components(H, D_deg, I_deg):
    """(H, D, I) -> (X, Y, Z) in nT: the inverse of :func:`elements`.

    X = H cos D, Y = H sin D, Z = H tan I, so that Z^2 + H^2 = H^2/cos^2 I.
    """
    D = np.radians(D_deg)
    I = np.radians(I_deg)
    return H * np.cos(D), H * np.sin(D), H * np.tan(I)


def main():
    section("1. From the measured components to the elements")
    for name, (X, Y, Z) in SITES.items():
        H, F, D, I = elements(X, Y, Z)
        print(f"{name}:")
        print(f"  X = {X:9.1f} nT   Y = {Y:9.1f} nT   Z = {Z:9.1f} nT")
        print(f"  H = {H:11.3f} nT (horizontal intensity)")
        print(f"  F = {F:11.3f} nT (total intensity)")
        print(f"  D = {D:+8.4f} deg  (declination, east positive)")
        print(f"  I = {I:+8.4f} deg  (inclination, down positive)")
        print(f"  checks: H^2+Z^2 = F^2 ? {H**2 + Z**2:.1f} vs {F**2:.1f} nT^2")
        print(f"          X^2+Y^2+Z^2 = F^2 ? {X**2+Y**2+Z**2:.1f} vs {F**2:.1f} nT^2")
        Xr, Yr, Zr = components(H, D, I)
        print(f"  round trip: dX = {Xr-X:+.2e}, dY = {Yr-Y:+.2e}, "
              f"dZ = {Zr-Z:+.2e} nT")

    section("2. Units: nT, T, gamma, and the equivalent magnetising field")
    F = elements(*SITES["site A: mid-latitude"])[1]
    print(f"reference total intensity F = {F:.3f} nT")
    print(f"  F = {F * NT_TO_T:.6e} T = {F * NT_TO_T * 1e6:.3f} microtesla")
    print(f"  F = {F:.3f} gamma   (1 gamma = 1 nT by definition)")
    Hmag = F * NT_TO_T / MU0
    print(f"  equivalent magnetising field F/mu0 = {Hmag:.4f} A/m")
    print(f"  so 1 A/m of magnetising field corresponds to "
          f"{MU0 * 1.0 / NT_TO_T:.2f} nT of flux density")
    print(f"  (mu0 = 4*pi*1e-7 = {MU0:.10e} H/m, an exact SI value)")
    print(f"  because B = mu0 H, 1 nT of flux density = {NT_TO_T/MU0:.6e} A/m; "
          "the conversion is linear, so it needs no derivative")

    section("3. Sensitivity of D and I to a component error")
    X, Y, Z = SITES["site A: mid-latitude"]
    H, F, D, I = elements(X, Y, Z)
    print(f"baseline: H = {H:.3f} nT, D = {D:.4f} deg, I = {I:.4f} deg")
    for err in (1.0, 10.0, 100.0):
        D_e = np.degrees(np.arctan2(Y + err, X))
        I_e = np.degrees(np.arctan2(Z, np.hypot(X, Y + err)))
        small = np.degrees(err / H)
        print(f"  dY = {err:6.1f} nT: dD exact = {D_e - D:+.5f} deg, "
              f"small-angle dD = {small:+.5f} deg")
    for err in (1.0, 10.0, 100.0):
        I_e = np.degrees(np.arctan2(Z + err, H))
        small = np.degrees(err * H / F**2)
        print(f"  dZ = {err:6.1f} nT: dI exact = {I_e - I:+.5f} deg, "
              f"small-angle dI = {small:+.5f} deg")

    section("4. Elements at synthetic sites along one dipole meridian")
    print("model: axial dipole, tan I = 2 tan(latitude); the table therefore")
    print("isolates the geometry of inclination from the intensity.")
    lat = np.array([0.0, 15.0, 30.0, 45.0, 60.0, 75.0])
    Igeo = np.degrees(np.arctan(2.0 * np.tan(np.radians(lat))))
    print("  latitude (deg)   I (deg)    Z/H = tan I    tan I/(2 tan lat)")
    for la, inc in zip(lat, Igeo):
        tl = 2.0 * np.tan(np.radians(la))
        chk = np.tan(np.radians(inc)) / tl if tl != 0.0 else float("nan")
        print(f"  {la:14.1f}   {inc:7.3f}   {np.tan(np.radians(inc)):12.4f}   "
              f"{chk:18.6f}")

    section("5. Angular resolution: arcminutes and what 1 nT buys")
    print(f"baseline H = {H:.3f} nT, F = {F:.3f} nT")
    for err in (0.1, 1.0, 5.0):
        dD = np.degrees(err / H)
        dI = np.degrees(err / F)
        print(f"  {err:4.1f} nT error -> dD = {dD:.5f} deg = {dD*60:.3f} arcmin; "
              f"dI = {dI:.5f} deg = {dI*60:.3f} arcmin")
    for arcmin in (1.0, 0.1):
        print(f"  reading D to {arcmin:.1f} arcmin = {arcmin/60:.5f} deg "
              f"requires dY below {H*np.radians(arcmin/60):.3f} nT")
    print("  the same 1 nT error at each synthetic site, because D is")
    print("  ill-conditioned where H is small:")
    print("    site                        H (nT)    dD for 1 nT (deg)  (arcmin)")
    for name, (X2, Y2, Z2) in SITES.items():
        H2, F2, D2, I2 = elements(X2, Y2, Z2)
        dD2 = np.degrees(np.arctan2(Y2 + 1.0, X2) - np.arctan2(Y2, X2))
        print(f"    {name:28s} {H2:9.3f}   {dD2:17.5f}   {dD2*60:8.3f}")

    section("6. Reproducibility check with the seeded generator")
    noise = RNG.normal(0.0, 1.0, 5)
    print("first five standard-normal draws from the seed 20261014:")
    print("  " + ", ".join(f"{v:+.6f}" for v in noise))


if __name__ == "__main__":
    main()
