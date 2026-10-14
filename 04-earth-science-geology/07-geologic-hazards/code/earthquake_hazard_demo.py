"""Earthquake hazard and ground motion: six things that can be computed.

Run:  .venv/bin/python earthquake_hazard_demo.py
Requires: numpy.

Companion to lesson 04-07-01.

The script deliberately keeps the *probabilistic* part of seismic hazard out of
the way (that belongs to 06-seismology/11) and computes only the pieces that
follow from mechanics:

1. Seismic moment and moment magnitude.  The magnitude is recovered from the
   dyn cm convention and the offset is then *converted* to the N m convention,
   which exposes a 0.037 difference against the value most often quoted.
2. Radiated energy from the empirical Gutenberg-Richter slope, with the slope
   labelled for what it is: a fitted constant, not a derivation.
3. Free-surface amplification, exactly 2 for a vertical SH wave, and the
   impedance ratio that sets the resonant amplification of a soft layer.
4. The 1-D SH transfer function by direct boundary-condition algebra, checked
   against the analytic peak value Z_rock/Z_soil at the fundamental frequency.
5. A Newmark-beta single-degree-of-freedom response spectrum of a synthetic
   pulse, with the integrator verified against the closed-form harmonic
   amplification 1/(2 zeta).
6. Geometric spreading plus anelastic attenuation, compared for body waves and
   surface waves.

Every scenario parameter is synthetic and labelled so.  No earthquake is
attributed a magnitude, a date or a catalogue number here, because this script
has no catalogue to attribute them from.
"""

import numpy as np

MU = 3.0e10          # Pa, shear modulus, NOMINAL for crustal rock (25-35 GPa)
RHO = 2700.0         # kg/m^3, NOMINAL crustal density
G = 9.80665          # m/s^2, standard gravity


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Seismic moment and moment magnitude
# --------------------------------------------------------------------------

def moment_magnitude(m0_nm):
    """Moment magnitude from M0 in N m, via the dyn cm convention.

    Hanks & Kanamori's relation is usually quoted as
        Mw = (2/3) log10(M0) - 10.7        (M0 in dyn cm)
    or, in SI units, with the offset *replaced* by -6.07.  The two are NOT the
    same relation: converting the dyn cm offset exactly (1 N m = 10^7 dyn cm)
    gives -10.7 + 2/3 * 7 = -6.0333.  Both offsets are reported below.
    """
    m0_dyncm = m0_nm * 1.0e7
    mw_dyncm = (2.0 / 3.0) * np.log10(m0_dyncm) - 10.7
    offset_nm = -10.7 + (2.0 / 3.0) * 7.0
    mw_nm = (2.0 / 3.0) * np.log10(m0_nm) + offset_nm
    return mw_dyncm, mw_nm, offset_nm


def part1():
    section("1. Seismic moment and moment magnitude")
    length_km, width_km, slip_m = 50.0, 20.0, 2.0
    area = length_km * 1e3 * width_km * 1e3
    m0 = MU * area * slip_m
    print("SYNTHETIC scenario (parameters chosen for arithmetic, not a real event)")
    print(f"  fault length L          = {length_km:.1f} km")
    print(f"  fault width  W          = {width_km:.1f} km")
    print(f"  mean slip    D          = {slip_m:.2f} m")
    print(f"  shear modulus mu        = {MU:.2e} Pa  (NOMINAL)")
    print(f"  rupture area A = L*W    = {area:.4e} m^2")
    print(f"  M0 = mu * A * D         = {m0:.6e} N m")
    print(f"  M0 in dyn cm            = {m0 * 1e7:.6e} dyn cm")
    mw_dyncm, mw_nm, offset_nm = moment_magnitude(m0)
    print(f"  Mw from dyn cm form     = {mw_dyncm:.4f}")
    print(f"  Mw from converted offset= {mw_nm:.4f}   (offset {offset_nm:+.4f})")
    print(f"  Mw from the usual -6.07 = {(2/3)*np.log10(m0) - 6.07:.4f}")
    d_mw = abs((2/3)*np.log10(m0) - 6.07 - mw_nm)
    print(f"  difference between the two SI conventions = {d_mw:.4f} magnitude units")
    print(f"  -> a factor {10**(1.5*d_mw):.4f} in M0: the offsets were rounded")
    print("     independently in the literature, and both are in use.")


# --------------------------------------------------------------------------
# 2. Radiated energy
# --------------------------------------------------------------------------

def part2():
    section("2. Radiated energy and the empirical magnitude-energy slope")
    print("The relation log10 E[J] = 1.5 M + 4.8 is EMPIRICAL (Gutenberg-Richter).")
    print("The slope 3/2 is a fitted constant; it is not derived here.")
    print()
    print("  dM   E ratio 10^(1.5 dM)")
    for dm in (0.2, 0.5, 1.0, 2.0):
        print(f"  {dm:4.1f}        {10**(1.5*dm):10.3f}")
    print()
    for m in (5.0, 6.0, 7.0, 8.0):
        e = 10.0 ** (1.5 * m + 4.8)
        print(f"  M = {m:.1f}:  E = {e:.4e} J  (empirical relation)")


# --------------------------------------------------------------------------
# 3. Free-surface amplification and layer impedance
# --------------------------------------------------------------------------

def part3():
    section("3. Free-surface doubling and the impedance ratio")
    print("A vertical SH wave reflects at the stress-free surface with")
    print("reflection coefficient +1, so the surface motion is 2 x the incident.")
    print("The factor is exact for a plane wave at normal incidence.  Nothing")
    print("about the medium enters, which is why 'the factor of two' is not a")
    print("site effect.")
    print()
    h = 50.0          # m, sediment thickness
    vs_soil = 200.0   # m/s, NOMINAL soft soil
    rho_soil = 1800.0
    vs_rock = 800.0   # m/s, NOMINAL weathered rock
    rho_rock = 2500.0
    z_soil = rho_soil * vs_soil
    z_rock = rho_rock * vs_rock
    f0 = vs_soil / (4.0 * h)
    print(f"  layer thickness H       = {h:.1f} m          (SYNTHETIC)")
    print(f"  Vs, rho of the layer    = {vs_soil:.0f} m/s, {rho_soil:.0f} kg/m^3  (NOMINAL)")
    print(f"  Vs, rho of the halfspace= {vs_rock:.0f} m/s, {rho_rock:.0f} kg/m^3  (NOMINAL)")
    print(f"  impedance Z = rho Vs: layer {z_soil:.3e}, halfspace {z_rock:.3e} kg m^-2 s^-1")
    print(f"  fundamental frequency f0 = Vs/(4H) = {f0:.4f} Hz")
    print(f"  resonant amplification |T|max = Z_rock/Z_soil = {z_rock/z_soil:.4f}")
    print("  The free-surface factor of two applies to BOTH the soil surface and")
    print("  the rock outcrop, so it cancels in the ratio |T|: the soil surface")
    print(f"  moves {z_rock/z_soil:.3f} x the rock outcrop motion at {f0:.3f} Hz,")
    print("  while the absolute surface motion is 2 x the incident wave at both.")


# --------------------------------------------------------------------------
# 4. The 1-D SH transfer function, from the boundary conditions
# --------------------------------------------------------------------------

def transfer_1d(f, h, vs1, rho1, vs2, rho2):
    """|T(f)| for an elastic layer over a halfspace, from the derivation.

    Derivation (see the lesson): matching displacement and shear traction at
    the interface with a traction-free surface gives

        |T(f)| = 1 / sqrt( cos^2(k1 h) + (Z1/Z2)^2 sin^2(k1 h) ),  k1 = 2 pi f / vs1
    """
    k1 = 2.0 * np.pi * f / vs1
    z1, z2 = rho1 * vs1, rho2 * vs2
    return 1.0 / np.sqrt(np.cos(k1 * h) ** 2 + (z1 / z2) ** 2 * np.sin(k1 * h) ** 2)


def part4():
    section("4. The 1-D SH transfer function, checked against the closed form")
    h, vs1, rho1 = 50.0, 200.0, 1800.0
    vs2, rho2 = 800.0, 2500.0
    f0 = vs1 / (4.0 * h)
    z_ratio = (rho2 * vs2) / (rho1 * vs1)
    print(f"  f0 = Vs/(4H) = {f0:.4f} Hz;  Z2/Z1 = {z_ratio:.4f}")
    print()
    print("      f (Hz)   |T(f)|     f/f0")
    for f in (0.25, 0.5, 0.99, 1.0, 2.0, 3.0):
        print(f"  {f:9.4f}   {transfer_1d(f, h, vs1, rho1, vs2, rho2):7.4f}   {f/f0:6.3f}")
    # A scan grid deliberately offset from the exact resonances: at an exact
    # resonance cos(k1 h) is ~1e-16 in floating point and |T| equals Z2/Z1
    # only up to rounding, so a grid that hits f0 exactly measures arithmetic,
    # not physics.
    f_scan = np.linspace(0.0105, 29.99895, 300001)
    t = transfer_1d(f_scan, h, vs1, rho1, vs2, rho2)
    i_max = int(np.argmax(t))
    print()
    print(f"  numerical maximum of |T| = {t[i_max]:.6f} at f = {f_scan[i_max]:.4f} Hz")
    print("  (grid offset from the exact resonances on purpose)")
    print(f"  closed form Z2/Z1        = {z_ratio:.6f}")
    print(f"  relative difference      = {abs(t[i_max]-z_ratio)/z_ratio:.3e}")
    print("  successive peaks (resonances at f0, 3f0, 5f0, ...):")
    for n in (1, 3, 5, 7):
        f_n = n * f0
        print(f"    {n} f0 = {f_n:6.3f} Hz -> |T| = {transfer_1d(f_n, h, vs1, rho1, vs2, rho2):7.4f}")


# --------------------------------------------------------------------------
# 5. SDOF response spectrum
# --------------------------------------------------------------------------

def sdof_response(dt, ag, periods, zeta, j_start=1):
    """Newmark-beta (linear acceleration) peaks for a set of oscillator periods.

    Solves  x'' + 2 zeta w x' + w^2 x = -a_g(t)  for unit mass, from rest.
    Returns (peak |x|, peak |x'' + a_g|) evaluated from sample ``j_start``
    onward, so a caller can exclude a start-up transient.
    """
    out = []
    for tn in periods:
        w = 2.0 * np.pi / tn
        c = 2.0 * zeta * w
        k = w * w
        beta, gamma = 0.25, 0.5
        x = v = a = 0.0
        peak_x = peak_a = 0.0
        for j in range(1, len(ag)):
            p = -ag[j]
            khat = 1.0 / (beta * dt * dt) + gamma * c / (beta * dt) + k
            phat = (p + x / (beta * dt * dt) + v / (beta * dt)
                    + (1.0 / (2.0 * beta) - 1.0) * a
                    + c * (gamma * x / (beta * dt) + (gamma / beta - 1.0) * v
                           + dt * (gamma / (2.0 * beta) - 1.0) * a))
            xn = phat / khat
            an = (xn - x) / (beta * dt * dt) - v / (beta * dt) - (1.0 / (2.0 * beta) - 1.0) * a
            vn = v + dt * ((1.0 - gamma) * a + gamma * an)
            x, v, a = xn, vn, an
            if j >= j_start:
                peak_x = max(peak_x, abs(x))
                peak_a = max(peak_a, abs(a + ag[j]))
        out.append((peak_x, peak_a))
    return out


def part5():
    section("5. SDOF oscillator: integrator check, then a response spectrum")
    zeta = 0.05
    dt = 0.002
    t = np.arange(0.0, 120.0, dt)
    print(f"  zeta = {zeta}; harmonic support acceleration of amplitude 1 m/s^2")
    print("  driven AT the oscillator natural frequency (beta = 1), and the peak")
    print("  taken over the final 10 per cent of a 120 s record so that the")
    print("  start-up transient (which decays as exp(-zeta w t)) is below 1e-6:")
    print()
    print("    T (s)   peak|x| (m)   w^2 peak|x|   1/(2 zeta)   rel. diff")
    for tn in (0.5, 1.0, 2.0):
        w = 2.0 * np.pi / tn
        ag = np.sin(w * t)
        (px, _pa), = sdof_response(dt, ag, [tn], zeta, j_start=int(0.9 * len(t)))
        pseudo = w * w * px
        exact = 1.0 / (2.0 * zeta)
        print(f"  {tn:6.2f}   {px:11.6f}   {pseudo:10.5f}   {exact:10.5f}"
              f"   {abs(pseudo-exact)/exact:.2e}")
    print()
    print("  The integrator reproduces the closed-form dynamic amplification")
    print("  1/(2 zeta) = 10, which is what validates it before it is used on a")
    print("  ground motion that has no closed form.")
    print()

    f_dom = 2.0
    t2 = np.arange(0.0, 12.0, dt)
    xi = t2 - 6.0
    ag = (1.0 - 2.0 * (np.pi * f_dom * xi) ** 2) * np.exp(-(np.pi * f_dom * xi) ** 2)
    print(f"  synthetic Ricker pulse: peak frequency {f_dom:.2f} Hz, peak 1.0 m/s^2")
    print(f"  peak ground acceleration of the pulse = {np.abs(ag).max():.4f} m/s^2")
    periods = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0])
    peaks = sdof_response(dt, ag, periods, zeta)
    print()
    print("    T (s)    Sa (m/s^2)    Sd (m)   Sa/PGA")
    pga = float(np.abs(ag).max())
    for tn, (px, pa) in zip(periods, peaks):
        print(f"  {tn:6.2f}   {pa:10.4f}   {px:8.5f}   {pa/pga:6.3f}")
    sa = np.array([p[1] for p in peaks])
    print()
    print(f"  peak spectral acceleration {sa.max():.4f} m/s^2 at T = "
          f"{periods[int(np.argmax(sa))]:.2f} s")
    print(f"  pulse dominant period 1/f_dom = {1.0/f_dom:.2f} s; the spectrum peaks")
    print(f"  at the adjacent ordinate T = {periods[int(np.argmax(sa))]:.2f} s at about")
    print(f"  {sa.max()/pga:.2f} x the peak ground acceleration. The peak is near, not")
    print("  exactly at, the pulse period: a pulse is not a harmonic wave, and its")
    print("  spectrum is broad.")


# --------------------------------------------------------------------------
# 6. Attenuation
# --------------------------------------------------------------------------

def part6():
    section("6. Geometric spreading and anelastic attenuation")
    q, v, f = 300.0, 3500.0, 2.0
    r_ref = 10.0e3
    print(f"  Q = {q:.0f}, v = {v:.0f} m/s, f = {f:.1f} Hz  (NOMINAL rock)")
    print(f"  anelastic exponent pi f / (Q v) = {np.pi*f/(q*v):.3e} m^-1")
    print()
    print("     r (km)   1/r body   geometric loss (dB)   total body   total surface")
    for r_km in (10, 20, 50, 100, 200):
        r = r_km * 1e3
        anel = np.exp(-np.pi * f * (r - r_ref) / (q * v))
        geo_body = r_ref / r
        geo_surf = np.sqrt(r_ref / r)
        print(f"  {r_km:8.0f}   {geo_body:8.4f}   {20*np.log10(geo_body):8.2f}"
              f"        {geo_body*anel:10.5f}   {geo_surf*anel:12.5f}")
    r = 100e3
    anel = np.exp(-np.pi * f * (r - r_ref) / (q * v))
    print()
    print(f"  at 100 km the anelastic factor alone is {anel:.4f} "
          f"({20*np.log10(anel):.2f} dB)")
    print("  a body wave also loses 20 dB from 10 to 100 km of spreading alone;")
    print("  a surface wave loses 10 dB, which is why surface waves are the ones")
    print("  felt at regional distance.")


def main():
    print("Earthquake hazard and ground motion -- computed quantities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    print()
    print("=" * 72)
    print("All quantities above are derived in the script from the printed")
    print("inputs.  Empirical constants (the 1.5 energy slope, the -10.7 and")
    print("-6.07 magnitude offsets) are labelled as such and are not derived.")
    print("=" * 72)


if __name__ == "__main__":
    main()
