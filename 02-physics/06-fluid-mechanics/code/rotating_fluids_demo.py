"""Rotating fluids: Coriolis parameter, Rossby number and geostrophy.

Run:  python3 rotating_fluids_demo.py
Requires: Python standard library only.

Companion to lesson 02-06-07. The script:

1. Computes the Coriolis parameter f = 2 Omega sin(phi) and the inertial period
   2 pi/f at a range of latitudes, including the equatorial limit.
2. Computes the Rossby number Ro = U/(f L) for a bathtub, a tornado, a coastal
   current, an ocean gyre and a mid-latitude weather system, and states which
   of rotation or advection dominates.
3. Uses geostrophic balance to convert a sea-surface slope into a current, and
   vice versa, at two latitudes.
4. Computes the Ekman depth and Ekman transport for a stated wind stress, and
   the internal Rossby radius of deformation from a stated stratification.
5. Computes the thermal-wind shear implied by a horizontal temperature
   gradient, and the vertical shear that follows.
6. Quantifies the bathtub-vortex claim: compares the Coriolis acceleration with
   the advective acceleration for a draining basin.

Every number printed below was produced by this script. Wind stresses,
viscosities and stratification parameters are nominal values chosen for
illustration; no observed current or wind is claimed.
"""

import math

OMEGA = 7.292115e-5     # rad/s, Earth angular velocity (WGS 84, defining)
G = 9.81
RHO_W = 1025.0
DEG = math.pi / 180.0


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def coriolis(lat_deg):
    return 2.0 * OMEGA * math.sin(lat_deg * DEG)


def part1_coriolis():
    section("1. The Coriolis parameter and the inertial period")

    print("f = 2 Omega sin(phi),  Omega = 7.292115e-05 rad/s (WGS 84 defining)")
    print(f"{'latitude':>10} {'sin(phi)':>10} {'f (1/s)':>12} "
          f"{'inertial period (h)':>21} {'2Omega (1/s)':>13}")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        f = coriolis(lat)
        period = math.inf if f == 0.0 else 2.0 * math.pi / abs(f) / 3600.0
        label = "infinite" if f == 0.0 else f"{period:21.3f}"
        print(f"{lat:10.1f} {math.sin(lat * DEG):10.4f} {f:12.5e} "
              f"{label:>21} {2 * OMEGA:13.5e}")
    print("\n  the inertial period is half a pendulum day, 12 h / sin(phi); at "
          "the equator")
    print("  there is no Coriolis force and the period diverges. The "
          "planetary vorticity")
    print("  2 Omega is 1.46e-4 1/s, which is the scale against which "
          "everything else is judged.")


def part2_rossby():
    section("2. Rossby number: when does rotation matter?")

    print("Ro = U / (f L). Ro << 1 is rotation-dominated, Ro >> 1 is not.")
    print(f"{'flow':>26} {'L (m)':>9} {'U (m/s)':>9} {'lat':>5} "
          f"{'f (1/s)':>11} {'Ro':>11} {'regime':>14}")
    flow = [
        ("bathtub drain", 0.5, 0.1, 45.0),
        ("tornado", 100.0, 50.0, 40.0),
        ("river", 1000.0, 1.0, 45.0),
        ("coastal current", 1.0e4, 0.3, 45.0),
        ("ocean gyre", 1.0e6, 0.1, 35.0),
        ("weather system", 1.0e6, 10.0, 45.0),
        ("gulf-stream meander", 1.0e5, 1.0, 40.0),
    ]
    for name, L, U, lat in flow:
        f = coriolis(lat)
        Ro = U / (f * L)
        regime = ("rotation-dominated" if Ro < 0.1
                  else "advection-dominated" if Ro > 1 else "intermediate")
        print(f"{name:>26} {L:9.1e} {U:9.2f} {lat:5.0f} {f:11.3e} "
              f"{Ro:11.3e} {regime:>14}")
    print("\n  the bathtub and the tornado are not rotating-fluid problems at "
          "all. The")
    print("  ocean gyre and the weather system are. The river and the coastal "
          "current sit")
    print("  in between, which is why they are the hard cases.")


def part3_geostrophic():
    section("3. Geostrophic balance: slope to current and back")

    print("geostrophic balance: f u = -g d(eta)/dy (eastward current along a "
          "meridional slope)")
    print(f"{'latitude':>9} {'slope d(eta)/dy':>17} {'u_g (m/s)':>11} "
          f"{'u_g (cm/s)':>11}")
    slopes = [1.0e-7, 1.0e-6, 1.0e-5, 1.0e-4]
    for lat in (30.0, 45.0, 60.0):
        f = coriolis(lat)
        for s in slopes:
            u = -G * s / f
            print(f"{lat:9.1f} {s:17.2e} {u:11.4f} {u * 100:11.3f}")
    print("\n  the slopes are tiny: 1e-6 is 10 cm of sea surface height per "
          "100 km. A")
    print("  geostrophic current of 10 cm/s at 45 degrees needs a slope of "
          f"{0.1 * coriolis(45.0) / G:.3e}.")

    print("\nsurface slope implied by a stated geostrophic current "
          "(d(eta)/dy = -f u / g):")
    for lat, u in ((30.0, 0.1), (45.0, 0.1), (45.0, 1.0), (60.0, 0.1)):
        s = -coriolis(lat) * u / G
        print(f"  lat {lat:4.0f}, u = {u:.2f} m/s  ->  slope = {s:.3e} "
              f"({abs(s) * 1e5 * 100:.2f} cm per 100 km)")


def part4_ekman():
    section("4. Ekman depth, Ekman transport and the Rossby radius")

    print("Ekman depth D_E = sqrt(2 nu / |f|), with nu an eddy viscosity")
    print(f"{'latitude':>9} {'nu (m^2/s)':>11} {'f (1/s)':>11} "
          f"{'D_E (m)':>10}")
    for lat in (15.0, 30.0, 45.0, 60.0):
        f = abs(coriolis(lat))
        for nu in (1.0e-2, 1.0e-1):
            print(f"{lat:9.1f} {nu:11.2e} {f:11.3e} "
                  f"{math.sqrt(2 * nu / f):10.2f}")
    print("\n  metres. The Ekman depth is a few tens of metres for a typical "
          "eddy viscosity,")
    print("  which is why wind-driven transport is concentrated in the upper "
          "ocean.")

    print("\nEkman transport per unit length, M_E = tau / (rho f) (m^2/s):")
    for lat, tau in ((45.0, 0.1), (45.0, 1.0), (30.0, 0.1)):
        f = coriolis(lat)
        M = tau / (RHO_W * f)
        print(f"  lat {lat:4.0f}, tau = {tau:.2f} N/m^2  ->  M_E = {M:.3f} "
              f"m^2/s = {M * 86400:.1f} m^2/day")
    print("  the transport is at right angles to the wind, to the right in the "
          "northern")
    print("  hemisphere: that is why alongshore winds drive upwelling.")

    print("\ninternal Rossby radius of deformation L_R = N H / |f|:")
    print(f"{'N (1/s)':>10} {'H (m)':>9} {'lat':>6} {'L_R (km)':>10}")
    for N, H, lat in ((1.0e-2, 1000.0, 45.0), (1.0e-2, 500.0, 45.0),
                      (5.0e-3, 200.0, 30.0), (1.0e-2, 8000.0, 60.0)):
        f = abs(coriolis(lat))
        print(f"{N:10.1e} {H:9.0f} {lat:6.0f} {N * H / f / 1e3:10.1f}")
    print("  kilometres. L_R is the scale below which rotation cannot "
          "geostrophically")
    print("  adjust a disturbance: eddies smaller than L_R behave like gravity "
          "waves, larger")
    print("  ones like balanced flow. It is one of the most useful numbers in "
          "geophysical")
    print("  fluid dynamics.")


def part5_thermal_wind():
    section("5. Thermal wind: vertical shear from a horizontal gradient")

    print("thermal wind (Boussinesq): du/dz = -(g/f) (1/rho) d(rho)/dy; with "
          "density")
    print("carried by temperature, du/dz ~ (g alpha / f) d(T)/dy")
    alpha = 2.0e-4      # 1/K, thermal expansion of seawater, nominal
    print(f"alpha = {alpha:.1e} 1/K; dT/dy is taken positive northward")
    print(f"{'dT/dy (K/100km)':>17} {'lat':>6} {'f (1/s)':>11} "
          f"{'du/dz (1/s)':>12} {'shear over 500 m (m/s)':>24}")
    for dT in (0.5, 1.0, 2.0, 5.0):
        dTdy = dT / 1.0e5          # warming northward, dT/dy > 0
        for lat in (30.0, 45.0):
            f = coriolis(lat)
            dudz = (G * alpha / f) * dTdy
            print(f"{dT:17.2f} {lat:6.0f} {f:11.3e} {dudz:12.3e} "
                  f"{abs(dudz) * 500:24.3f}")
    print("\n  a 2 K difference over 100 km supports a few tenths of a metre "
          "per second of")
    print("  vertical shear over 500 m. This is how the Gulf Stream is tied to "
          "the")
    print("  north-south temperature contrast.")


def part6_bathtub():
    section("6. Why a bathtub does not obey Coriolis")

    L = 0.5
    U = 0.1
    lat = 45.0
    f = coriolis(lat)
    cor = f * U                 # Coriolis acceleration scale
    adv = U * U / L             # advective acceleration scale
    print(f"bathtub: L = {L} m, U = {U} m/s, latitude {lat} degrees")
    print(f"  Coriolis acceleration scale f U        = {cor:.3e} m/s^2")
    print(f"  advective acceleration scale U^2 / L   = {adv:.3e} m/s^2")
    print(f"  ratio (this is Ro)                     = {cor / adv:.3e}")
    print(f"  a plug hole 2 cm across, draining over 60 s, is a time scale "
          "of 60 s")
    print(f"  against an inertial period of "
          f"{2 * math.pi / f / 3600:.2f} h "
          f"({2 * math.pi / f:.0f} s)")
    print(f"  the basin empties about {(2 * math.pi / f) / 60:.0f} times "
          "faster than the Earth")
    print("  can organise a rotating flow in it.")
    print("\n  the acceleration ratio is about 5e-4 and the time-scale ratio "
          "is about 1e3.")
    print("  The rotation of the Earth cannot set the sense of a bathtub "
          "vortex; the")
    print("  residual swirl of filling, the shape of the basin and the geometry "
          "of the")
    print("  drain do. Claims to the contrary are a failure to estimate the "
          "Rossby")
    print("  number, not a subtle effect.")


def main():
    part1_coriolis()
    part2_rossby()
    part3_geostrophic()
    part4_ekman()
    part5_thermal_wind()
    part6_bathtub()


if __name__ == "__main__":
    main()
