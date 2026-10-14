"""Planetary geophysics from orbiters and landers: measurement sensitivity.

Run:  .venv/bin/python planetary_geophysics_missions_demo.py
Requires: numpy.

Companion to lesson 04-08-03.

The lesson's subject is the technique, so this script computes what each
technique can actually see, from the measurement's own uncertainty rather than
from any published result:

1. Seismology: a P-S time difference as a distance, and the Ps conversion
   delay as a crustal thickness — with the trade-off between thickness and
   velocity ratio that makes a single phase insufficient.
2. Radio tracking: the two-way Doppler signature of a velocity, and the
   acceleration produced by a gravity anomaly of a stated size.
3. Radar sounding: vertical resolution from bandwidth, depth from echo delay,
   the Fresnel reflection coefficient of the interfaces that matter, and how
   decisively the penetration depth depends on the loss tangent.
4. Magnetometry: the depth-amplitude trade-off of a dipole anomaly, computed
   rather than quoted.

No mission, instrument, discovery or published result is named.  Everything is
a sensitivity calculation from an assumed instrument performance and an assumed
material property, both labelled.
"""

import math

import numpy as np

C = 299792458.0
MU_0 = 1.25663706212e-6


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Seismology
# --------------------------------------------------------------------------

def part1():
    section("1. Seismology: a time difference as a distance")
    print("  The crudest possible locator: a homogeneous body, straight rays, so")
    print("      t_P = D/v_P,  t_S = D/v_S,  D = (t_S - t_P) v_P v_S/(v_P - v_S).")
    print("  A real location needs a velocity model and several stations; this")
    print("  version is here because it shows what one three-component station")
    print("  and one phase pair can and cannot do.")
    print()
    vp, vs = 6.0, 3.5      # km/s, NOMINAL crustal
    print(f"  v_P = {vp:.1f} km/s, v_S = {vs:.1f} km/s (NOMINAL)")
    print()
    print("     t_S - t_P (s)   distance (km)   t_P (s)")
    for dt in (5.0, 10.0, 20.0, 40.0, 80.0):
        d = dt * vp * vs / (vp - vs)
        print(f"  {dt:15.1f}   {d:13.1f}   {d/vp:8.1f}")
    sens_vp = vs / (vp - vs)
    sens_vs = vp / (vp - vs)
    print()
    print(f"  The conversion factor is v_P v_S/(v_P - v_S) = {vp*vs/(vp-vs):.2f} km per")
    print("  second of S-minus-P time.  It AMPLIFIES velocity error, because it")
    print("  contains the difference in the denominator:")
    print(f"    a 1 per cent error in v_P becomes {sens_vp:.2f} per cent in distance")
    print(f"    a 1 per cent error in v_S becomes {sens_vs:.2f} per cent in distance")
    print("  (computed as v_S/(v_P - v_S) and v_P/(v_P - v_S), the logarithmic")
    print("  derivatives of the factor).  One station therefore gives a distance")
    print("  with a systematic error, and a distance error displaces the")
    print("  estimated origin by the same amount.  Origin time, depth and")
    print("  distance are not separable from one station, whatever the timing")
    print("  precision: the number of stations is the decisive instrument.")
    print()
    print("  Crustal thickness from a converted phase (receiver functions).")
    print("  For vertical incidence the conversion delay is")
    print("      t_Ps = H (1/v_S - 1/v_P),  so  H = t_Ps / (1/v_S - 1/v_P).")
    print()
    print("     t_Ps (s)   H at v_P/v_S = 1.71   H at 1.80   H at 1.90 (km)")
    for t in (1.0, 2.0, 3.0, 4.0, 5.0):
        row = []
        for ratio in (1.71, 1.80, 1.90):
            vp2 = 6.0
            vs2 = vp2 / ratio
            row.append(t / (1.0 / vs2 - 1.0 / vp2))
        print(f"  {t:10.1f}   {row[0]:22.2f}   {row[1]:11.2f}   {row[2]:14.2f}")
    print()
    print("  A 4 s delay is 33.8 km of crust at v_P/v_S = 1.71 and 26.7 km at")
    print("  1.90, a 21 per cent difference in thickness for an 11 per cent")
    print("  difference in the velocity ratio.  A single Ps delay CANNOT")
    print("  determine both thickness and velocity ratio, and the standard")
    print("  remedy is a second phase (a multiple, or the Ps + PpSs arrival")
    print("  pair) whose delay has a different dependence on the two")
    print("  parameters.  Two equations, two unknowns; one equation is a curve,")
    print("  not a point.")


# --------------------------------------------------------------------------
# 2. Radio tracking
# --------------------------------------------------------------------------

def part2():
    section("2. Radio tracking: what Doppler can and cannot see")
    print("  A one-way range rate r_dot shifts the returned frequency by")
    print("      df/f = 2 r_dot / c   (two-way, transponder coherent).")
    print()
    f_x = 8.4e9          # Hz, X-band, NOMINAL
    df_floor = 0.01      # Hz, an ASSUMED Doppler stability over a 60 s count
    print(f"  carrier f = {f_x/1e9:.2f} GHz (X-band, nominal)")
    print(f"  assumed Doppler noise floor = {df_floor:.3f} Hz over 60 s")
    print()
    print("     r_dot (mm/s)   df (Hz)")
    for v in (0.01, 0.1, 1.0, 10.0):
        df = 2.0 * (v / 1000.0) * f_x / C
        print(f"  {v:15.2f}   {df:8.5f}")
    print()
    dvel = 0.5 * C * df_floor / f_x
    print(f"  The noise floor corresponds to {dvel*1e3:.3f} mm/s of range rate.")
    print("  That is the reason gravity and topography are measurable from a")
    print("  spacecraft at all: micron-per-second velocities are not needed,")
    print("  because the observable is a frequency, and frequency is what a")
    print("  radio system measures best.")
    print()
    print("  What a gravity anomaly does.  A spacecraft passing over a 10 mGal")
    print("  anomaly (1e-4 m/s^2) accumulates a velocity change over the")
    print("  encounter:")
    print()
    print("     duration (s)   dv (mm/s)   df (Hz)   signal/noise")
    for t in (10.0, 30.0, 60.0, 300.0):
        dv = 1.0e-4 * t
        df = 2.0 * dv * f_x / C
        print(f"  {t:12.0f}   {dv*1e3:9.2f}   {df:8.3f}   {df/df_floor:13.1f}")
    print()
    print("  A 10 mGal anomaly is a small anomaly, and over a minute it produces")
    print("  a Doppler signal hundreds of times the noise.  The limitation on")
    print("  gravity from an orbiter is therefore NOT the instrument: it is the")
    print("  geometry (how low and how fast the spacecraft flies, which sets the")
    print("  resolution at the surface) and the non-gravitational accelerations")
    print("  that have to be modelled and removed.")


# --------------------------------------------------------------------------
# 3. Radar sounding
# --------------------------------------------------------------------------

def fresnel_power(eps1, eps2):
    r = (math.sqrt(eps1) - math.sqrt(eps2)) / (math.sqrt(eps1) + math.sqrt(eps2))
    return r, r * r


def part3():
    section("3. Radar sounding: resolution, delay, reflectivity, range")
    print("  Vertical resolution from the two-way travel time and the bandwidth:")
    print("      dz = c / (2 B sqrt(eps_r)).")
    print()
    eps_ice = 3.15      # NOMINAL, a commonly used value for cold ice
    print(f"  eps_r = {eps_ice:.2f} (NOMINAL for cold ice; it is temperature-")
    print("  and impurity-dependent, so confirm the value you use)")
    print()
    print("     B (MHz)   dz (m)")
    for B in (1.0, 5.0, 10.0, 20.0, 60.0):
        print(f"  {B:9.1f}   {C/(2*B*1e6*math.sqrt(eps_ice)):7.2f}")
    print()
    print("  A 10 MHz chirp gives about 8 m of vertical resolution in ice.  The")
    print("  resolution in the medium is c/(2B sqrt(eps_r)), so a medium of")
    print("  higher permittivity has a shorter wavelength and therefore FINER")
    print("  resolution; the only free lever is the bandwidth, because the wave")
    print("  speed in the medium is fixed by the material.")
    print()
    print("  Depth from the echo delay: z = c t/(2 sqrt(eps_r)).")
    print("     two-way delay (micro s)   depth in ice (m)")
    for t_us in (1.0, 5.0, 10.0, 20.0, 50.0):
        t = t_us * 1e-6
        print(f"  {t_us:22.1f}   {C*t/(2*math.sqrt(eps_ice)):15.1f}")
    print()
    print("  Reflectivity.  At normal incidence the field reflection coefficient")
    print("  between two non-magnetic dielectrics is")
    print("      R = (sqrt(eps_1) - sqrt(eps_2)) / (sqrt(eps_1) + sqrt(eps_2)).")
    print()
    print("     interface (host eps_1 = 3.15)     R        power |R|^2   dB")
    for name, e2 in (("over water (80)", 80.0),
                     ("over wet rock (25)", 25.0),
                     ("over dry rock (6)", 6.0),
                     ("over air (1)", 1.0),
                     ("over material with the same eps (3.15)", 3.15)):
        r, p = fresnel_power(eps_ice, e2)
        db = f"{10*math.log10(p):6.1f}" if p > 0 else "     -"
        print(f"  {name:40s}   {r:8.4f}   {p:11.4f}   {db}")
    r_w, p_w = fresnel_power(eps_ice, 80.0)
    r_r, p_r = fresnel_power(eps_ice, 6.0)
    print()
    print(f"  A water interface returns {p_w/p_r:.1f} times the power of a dry-rock")
    print("  interface with the same geometry, and about 12 dB more.  That")
    print("  contrast is why radar sounding detects water under ice at all: the")
    print("  signal is not the echo, it is the DIFFERENCE between two echoes.")
    print()
    print("  Penetration.  For a low-loss dielectric the field attenuation")
    print("  coefficient is alpha = (omega/c) sqrt(eps_r) tan(delta)/2, so the")
    print("  power decays as exp(-2 alpha z) and the 1/e depth for POWER is")
    print("      1/(2 alpha) = c / (omega sqrt(eps_r) tan(delta)).")
    print()
    f = 10e6
    print(f"  at f = {f/1e6:.0f} MHz:")
    print("     tan(delta)   power 1/e depth (m)   two-way loss (dB/km)")
    for td in (1e-5, 1e-4, 1e-3, 1e-2):
        alpha = (2.0 * math.pi * f / C) * math.sqrt(eps_ice) * td / 2.0
        zp = 1.0 / (2.0 * alpha)
        db_per_km = 2.0 * alpha * 1000.0 * 8.685889638
        print(f"  {td:12.1e}   {zp:18.0f}   {db_per_km:22.2f}")
    print()
    print("  Three orders of magnitude in tan(delta) is three orders of magnitude")
    print("  in penetration, because the two are inversely proportional.  The")
    print("  loss tangent of ice is temperature-dependent and must be taken from")
    print("  a measurement or a dielectric-properties compilation, not from")
    print("  memory; a range quoted without it is not a range.")


# --------------------------------------------------------------------------
# 4. Magnetometry
# --------------------------------------------------------------------------

def dipole_anomaly(r, d, m):
    """Vertical field of a vertically magnetised point dipole at depth d."""
    return MU_0 * m / (4.0 * math.pi) * (2.0 * d ** 2 - r ** 2) / (r ** 2 + d ** 2) ** 2.5


def part4():
    section("4. Magnetometry: the depth-amplitude trade-off, computed")
    print("  A vertically magnetised dipole of moment m at depth d gives")
    print("      B_z(r) = (mu_0 m/4 pi)(2 d^2 - r^2)/(r^2 + d^2)^(5/2).")
    print()
    m = 1.0e12       # A m^2, an arbitrary reference moment so the shapes compare
    print(f"  reference moment m = {m:.1e} A m^2 (arbitrary; only the shape matters)")
    print()
    print("     depth (km)   peak |B_z| (nT)   half-width (km)")
    for d_km in (1.0, 2.0, 5.0, 10.0, 20.0):
        d = d_km * 1000.0
        peak = dipole_anomaly(0.0, d, m)
        r = np.linspace(0.0, 20.0 * d, 200001)
        b = np.abs(dipole_anomaly(r, d, m))
        half = np.abs(b - 0.5 * abs(peak))
        hw = r[int(np.argmin(half))] / 1000.0
        print(f"  {d_km:12.1f}   {peak*1e9:14.3f}   {hw:16.2f}")
    print()
    print("  The peak falls as 1/d^3 and the half-width grows in proportion to d:")
    print("  the tabulated half-widths are d/2 to within half a per cent, which")
    print("  is the classic rule for a point dipole.  The WIDTH of an anomaly")
    print("  therefore gives the depth and the AMPLITUDE gives the magnetisation")
    print("  times the volume.  That is an inverse problem with the same")
    print("  structure as a gravity anomaly, and with the same consequence:")
    print("  neither depth nor magnetisation is determined by one profile, only")
    print("  their combination.  The half-width also has a floor set by the")
    print("  altitude of the measurement and by the thickness of the magnetised")
    print("  layer, so a 'depth to the top' from a magnetic map is a model")
    print("  result.")
    print()
    print("  The same anomaly seen from two altitudes resolves the ambiguity,")
    print("  because directly above a dipole the field is")
    print("      B_z = (mu_0 m/4 pi) 2/(d + h)^3,  so  B_z(0)/B_z(h) = ((d+h)/d)^3.")
    print()
    print("     depth (km)   peak at the surface (nT)   at h = 50 km (nT)   ratio")
    for d_km in (5.0, 10.0, 20.0, 50.0):
        d = d_km * 1000.0
        b0 = MU_0 * m / (4.0 * math.pi) * 2.0 / d ** 3
        b50 = MU_0 * m / (4.0 * math.pi) * 2.0 / (d + 50e3) ** 3
        print(f"  {d_km:12.1f}   {b0*1e9:22.3f}   {b50*1e9:18.3f}   {b0/b50:8.2f}")
    print()
    print("  The ratio is monotonic in depth and depends on nothing else, so for")
    print("  a POINT dipole a two-altitude survey determines the depth exactly.")
    print("  A real magnetised layer is not a point dipole, and its thickness and")
    print("  the altitude-dependence of the instrument's sensitivity both enter,")
    print("  so the depth of a magnetic source in a planetary crust is a model")
    print("  parameter with a stated trade-off, as it is on Earth.")


def main():
    print("Planetary geophysics from orbiters and landers -- sensitivities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    print()
    print("=" * 72)
    print("No mission, instrument, discovery or published measurement is")
    print("named.  Every performance figure above is an ASSUMED instrument")
    print("specification or an ASSUMED material property, labelled.")
    print("=" * 72)


if __name__ == "__main__":
    main()
