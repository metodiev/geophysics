"""Fluid statics: hydrostatic pressure, buoyancy and isostasy.

Run:  python3 fluid_statics_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-01. The script:

1. Builds a layered hydrostatic pressure profile through the crust and verifies
   dp/dz = rho g by finite differences, first for a single density and then for
   a three-layer model, and compares the equivalent fluid column against the
   true integrated weight.
2. Solves the buoyancy balance for a magma body and for a Mantle blob, and
   computes the net driving pressure per unit height, (rho_host - rho_body) g.
3. Solves the Airy isostasy equation for the crustal root and compares the
   excess pressure of the topography with the buoyancy of the compensating
   root, reporting the mass-balance residual.
4. Computes ocean hydrostatic pressure and the gravitational head it represents.

Every number printed below was produced by this script. Densities and
temperatures are nominal values for illustration, not measurements of any
particular rock or magma body.
"""

import math

G = 9.81           # m/s^2, nominal surface gravity (handbook Sec. 3.2)
RHO_W = 1030.0     # kg/m^3, seawater, nominal (handbook Sec. 3.6)
RHO_CRUST = 2700.0  # kg/m^3, crustal rock, nominal (handbook Sec. 3.4)
RHO_MANTLE = 3300.0  # kg/m^3, uppermost mantle, nominal (handbook Sec. 3.3)
RHO_MAGMA = 2500.0   # kg/m^3, basaltic magma, nominal for illustration


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_hydrostatic():
    section("1. Hydrostatic pressure and the vertical gradient")

    print("homogeneous crust, rho = %.0f kg/m^3" % RHO_CRUST)
    print(f"{'z (km)':>7} {'p (MPa)':>10} {'dp/dz (MPa/km)':>16} "
          f"{'rho*g (MPa/km)':>16}")
    rho_g = RHO_CRUST * G * 1e3 / 1e6  # Pa/m -> MPa/km
    for z_km in (1.0, 5.0, 10.0, 20.0, 30.0):
        p = RHO_CRUST * G * z_km * 1e3          # Pa
        dpdz = RHO_CRUST * G                     # Pa/m
        print(f"{z_km:7.1f} {p / 1e6:10.3f} {dpdz * 1e3 / 1e6:16.6f} "
              f"{rho_g:16.6f}")
    print(f"  the two columns agree by construction: dp/dz = rho g = "
          f"{rho_g:.6f} MPa/km")

    # Three-layer model, numerically differentiated.
    layers = [("sediment", 0.0, 2.0, 2200.0),
              ("upper crust", 2.0, 15.0, 2650.0),
              ("lower crust", 15.0, 35.0, 2900.0)]
    print("\nthree-layer model (integrated weight):")
    print(f"{'layer':>12} {'top (km)':>9} {'base (km)':>10} {'rho':>7} "
          f"{'p_top (MPa)':>12} {'p_base (MPa)':>13}")
    p = 0.0
    grid = []
    dz = 0.05
    for name, z0, z1, rho in layers:
        start = p
        p_base = p + rho * G * (z1 - z0) * 1e3
        print(f"{name:>12} {z0:9.1f} {z1:10.1f} {rho:7.0f} "
              f"{start / 1e6:12.3f} {p_base / 1e6:13.3f}")
        # store samples every 0.05 km inside the layer
        zz = z0
        pp = start
        while zz < z1 - 1e-9:
            grid.append((zz, pp, rho))
            pp += rho * G * dz * 1e3
            zz += dz
        p = p_base
    grid.append((35.0, p, layers[-1][3]))

    # Finite-difference check of dp/dz inside each layer, away from interfaces.
    print("\nfinite-difference check of dp/dz (h = 0.05 km), samples well "
          "inside a layer:")
    worst = 0.0
    checked = 0
    for i in range(1, len(grid) - 1):
        z_prev, p_prev, rho_prev = grid[i - 1]
        z_next, p_next, rho_next = grid[i + 1]
        if rho_prev != rho_next:            # skip an interface
            continue
        fd = (p_next - p_prev) / ((z_next - z_prev) * 1e3)   # Pa/m
        exact = rho_prev * G
        worst = max(worst, abs(fd - exact))
        checked += 1
    print(f"  max |finite-difference - rho*g| over {checked} interior samples "
          f"= {worst:.3e} Pa/m")

    # Compare the layered pressure at 35 km with a single-density estimate.
    p_single = RHO_CRUST * G * 35e3
    print(f"\n  layered p(35 km)              = {grid[-1][1] / 1e6:9.3f} MPa")
    print(f"  single-density 2700 estimate  = {p_single / 1e6:9.3f} MPa")
    print(f"  relative difference           = "
          f"{100 * (grid[-1][1] - p_single) / p_single:+.2f} %")
    print("  the single-density model is a choice, not a law; the layered "
          "model needs no new physics.")


def part2_buoyancy():
    section("2. Buoyancy: the driving pressure of a light body")

    print("net upward force per unit volume = (rho_host - rho_body) g")
    print(f"{'body':>22} {'rho_body':>9} {'rho_host':>9} "
          f"{'d(rho*g) (Pa/m)':>16} {'over 5 km (MPa)':>16}")
    cases = [("basaltic magma in crust", RHO_MAGMA, RHO_CRUST),
             ("granitic melt in crust", 2400.0, RHO_CRUST),
             ("mantle plume vs mantle", 3250.0, RHO_MANTLE),
             ("iceberg in seawater", 917.0, RHO_W),
             ("dense block in crust", 3000.0, RHO_CRUST)]
    for name, rho_body, rho_host in cases:
        drive = (rho_host - rho_body) * G
        print(f"{name:>22} {rho_body:9.0f} {rho_host:9.0f} "
              f"{drive:16.2f} {drive * 5e3 / 1e6:16.3f}")

    print("\nArchimedes check: a floating body displaces its own mass.")
    for name, rho_body, rho_host in (("iceberg", 917.0, RHO_W),
                                     ("magma", RHO_MAGMA, RHO_CRUST)):
        frac = rho_body / rho_host
        print(f"  {name:>8}: submerged fraction = rho_body/rho_host = "
              f"{frac:.4f}  (emergent fraction {1 - frac:.4f})")

    # Magma ascent: does a 1 km column of magma in a dike reach the surface?
    h = 1000.0
    drive = (RHO_CRUST - RHO_MAGMA) * G * h
    print(f"\n  a {h / 1e3:.0f} km column of magma has buoyancy pressure "
          f"{drive / 1e6:.3f} MPa at its base;")
    print("  it reaches the surface only while the tensile strength of the "
          "host rock and the viscous resistance")
    print("  of the conduit are smaller than this. The buoyancy term alone "
          "does not guarantee ascent.")


def part3_isostasy():
    section("3. Isostasy as a buoyancy balance (Airy model)")

    # Airy: a topography of height h above the reference level is supported by a
    # crustal root of thickness r below it, with rho_c h = (rho_m - rho_c) r.
    print("Airy balance: rho_c * h = (rho_m - rho_c) * r")
    print(f"{'h (km)':>8} {'root r (km)':>13} {'r/h':>8} "
          f"{'topo load (MPa)':>17} {'root buoy. (MPa)':>18} {'residual':>10}")
    for h_km in (0.5, 1.0, 2.0, 5.0):
        h = h_km * 1e3
        r = RHO_CRUST * h / (RHO_MANTLE - RHO_CRUST)
        topo = RHO_CRUST * G * h
        root = (RHO_MANTLE - RHO_CRUST) * G * r
        print(f"{h_km:8.1f} {r / 1e3:13.2f} {r / h:8.2f} "
              f"{topo / 1e6:17.3f} {root / 1e6:18.3f} "
              f"{(topo - root) / topo:+10.2e}")

    # Pratt: equal-pressure model at a compensation depth D.
    print("\nPratt model at compensation depth D = 30 km: "
          "rho * (D + h) = rho_0 * D")
    D = 30e3
    rho0 = 2700.0
    for h_km in (0.5, 1.0, 2.0, 5.0):
        h = h_km * 1e3
        rho = rho0 * D / (D + h)
        print(f"  h = {h_km:4.1f} km  ->  required density "
              f"{rho:7.1f} kg/m^3  (deficit {rho0 - rho:5.1f})")

    print("\n  both models enforce the same physics, hydrostatic balance at "
          "depth; they differ in where")
    print("  they place the compensation (a root versus a density anomaly). "
          "Neither is uniquely determined")
    print("  by surface gravity: that non-uniqueness is the subject of "
          "07-gravity-geodesy.")


def part4_ocean():
    section("4. Ocean hydrostatic pressure")

    print(f"{'depth (m)':>10} {'p (MPa)':>10} {'p (bar)':>10} "
          f"{'pressure head (m water)':>24}")
    for z in (10.0, 100.0, 1000.0, 4000.0, 11000.0):
        p = RHO_W * G * z
        print(f"{z:10.0f} {p / 1e6:10.3f} {p / 1e5:10.1f} "
              f"{p / (RHO_W * G):24.1f}")
    print(f"\n  dp/dz = rho_w g = {RHO_W * G / 1e3:.2f} kPa per metre, so the "
          "common rule of thumb")
    print("  'about 1 MPa per 100 m' is an over-estimate for seawater by a "
          "few per cent:")
    print(f"  100 m of seawater is {RHO_W * G * 100 / 1e6:.4f} MPa.")


def main():
    part1_hydrostatic()
    part2_buoyancy()
    part3_isostasy()
    part4_ocean()


if __name__ == "__main__":
    main()
