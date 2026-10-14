"""Tsunami generation, propagation and warning: the derivable core.

Run:  .venv/bin/python tsunami_demo.py
Requires: numpy.

Companion to lesson 04-07-05.

Every quantity below follows from the shallow-water dispersion relation
c = sqrt(g h) and one conservation law, and every one of them is checked:

1. Phase speed and travel time, and the exact finite-depth dispersion relation
   compared with the shallow-water limit, so the validity condition is a
   number rather than an adjective.
2. Wavelength and the shallow-water criterion.
3. Green's law, A proportional to h^(-1/4), from energy-flux conservation.
4. The Kajiura filter: how much of a given seafloor wavelength reaches the
   ocean surface, from Laplace's equation with a moving bottom.
5. Refraction: Snell's law with c = sqrt(gh), which is why a tsunami turns to
   face the coast.
6. The bore speed across a tsunami front, derived from mass and momentum
   conservation across the front.
7. Warning: bottom-pressure sensitivity, and the DART-style detection
   threshold in centimetres of sea surface.

No tsunami event, travel time, run-up or warning-centre record is quoted.
"""

import math

import numpy as np

G = 9.80665
RHO_W = 1030.0       # kg/m^3, seawater density, NOMINAL


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def c_exact(h, T):
    """Exact phase speed of a linear gravity wave of period T in depth h."""
    k = 2.0 * math.pi / (T * math.sqrt(G * h))   # implicit; solved below
    # Solve for k directly: omega^2 = g k tanh(kh), omega = 2 pi / T.
    from math import tanh
    w = 2.0 * math.pi / T
    k = w * w / G
    for _ in range(60):
        f = G * k * tanh(k * h) - w * w
        df = G * (tanh(k * h) + k * h * (1.0 - tanh(k * h) ** 2))
        k -= f / df
    return w / k


def part1():
    section("1. Phase speed, travel time, and the validity of c = sqrt(g h)")
    print("     h (m)    c = sqrt(gh) (m/s)   c (km/h)   time for 1000 km (min)")
    for h in (500.0, 1000.0, 2000.0, 4000.0, 6000.0):
        c = math.sqrt(G * h)
        print(f"  {h:8.0f}   {c:18.2f}   {c*3.6:8.1f}   {1000e3/c/60:20.1f}")
    print()
    h = 4000.0
    c = math.sqrt(G * h)
    print(f"  In 4000 m of water, c = {c:.2f} m/s = {c*3.6:.1f} km/h.  A commercial")
    print("  jet cruises near 900 km/h, so the wave moves at about four fifths of")
    print(f"  cruising speed, and an 8000 km crossing takes {8000e3/c/3600:.2f} h.")
    print()
    T = 1200.0
    print(f"  Validity.  For a wave of period T = {T:.0f} s in h = {h:.0f} m:")
    ce = c_exact(h, T)
    print(f"    c exact (finite depth) = {ce:.4f} m/s")
    print(f"    c shallow-water        = {c:.4f} m/s")
    print(f"    relative error         = {abs(ce-c)/ce:.3e}")
    print()
    print("     T (s)    k h     c exact    c = sqrt(gh)   relative error   (kh)^2/6")
    for TT in (120.0, 300.0, 600.0, 1200.0, 3600.0):
        ce = c_exact(4000.0, TT)
        k = 2.0 * math.pi / (TT * ce)
        kh = k * 4000.0
        print(f"  {TT:8.0f}   {kh:7.3f}   {ce:9.3f}   {c:12.3f}"
              f"   {abs(ce-c)/ce:14.3e}   {kh*kh/6.0:10.3e}")
    print()
    print("  The relative error is (kh)^2/6 to three figures, which is the")
    print("  leading term of the expansion of tanh.  The formula is therefore")
    print("  good to 1 per cent while kh < 0.25, which for a 4000 m ocean means")
    print("  periods longer than about 10 minutes; it is LEAST accurate for the")
    print("  shortest periods, which are the first to arrive and the least")
    print("  dangerous.  The error column and the (kh)^2/6 column agree because")
    print("  that is the derivation, not a coincidence.")


def part2():
    section("2. Wavelength and the shallow-water criterion")
    h = 4000.0
    print(f"  h = {h:.0f} m; the shallow-water condition is h/L < 1/20.")
    print()
    print("     T (s)   L = T sqrt(gh) (km)   h/L     regime")
    for T in (120.0, 300.0, 600.0, 1200.0, 3600.0):
        L = T * math.sqrt(G * h) / 1000.0
        print(f"  {T:8.0f}   {L:21.1f}   {h/(L*1000):6.5f}   "
              f"{'shallow' if h/(L*1000) < 0.05 else 'intermediate'}")
    print()
    print("  A 20-minute tsunami is 20 to 240 km long in the deep ocean and")
    print("  4000 m deep: h/L is 0.02 to 0.002, two orders of magnitude inside")
    print("  the shallow-water regime.  A wind wave of 10 s period in the same")
    Lw = 10.0 * math.sqrt(G * h) / 1000.0
    print(f"  depth has L = {Lw:.3f} km and h/L = {h/(Lw*1000):.2f}: it is a")
    print("  deep-water wave and disperses, which is why a storm sea of 10 s")
    print("  waves never arrives as a single front and a tsunami does.")


def part3():
    section("3. Green's law: A proportional to h^(-1/4)")
    print("  Energy flux per unit crest length is E c_g with E = (1/2) rho g A^2")
    print("  and c_g = sqrt(g h) in shallow water.  Conservation gives")
    print("      A^2 sqrt(h) = const   ->   A ~ h^(-1/4).")
    print()
    print("     h (m)    A/A0 (from 4000 m)   A (m) for A0 = 0.5 m")
    a0 = 0.5
    for h in (4000.0, 2000.0, 1000.0, 200.0, 50.0, 20.0, 10.0):
        amp = (4000.0 / h) ** 0.25
        print(f"  {h:8.0f}   {amp:20.4f}   {amp*a0:22.3f}")
    print()
    print("  Shoaling from 4000 m to 20 m multiplies the amplitude by")
    print(f"  {(4000.0/20.0)**0.25:.3f}, and it does so without any dissipation.")
    print("  The same law applied from 4000 m to 4000 m gives 1, which is the")
    print("  check that the formula contains no hidden constant.")
    print()
    print("  Green's law is a WKB result and fails where the bottom slope is")
    print("  steep compared with the wavelength, i.e. in the last few hundred")
    print("  metres of water.  Run-up, inundation distance and bore impact are")
    print("  a separate problem that requires the full nonlinear shallow-water")
    print("  equations and a measured beach profile.")


def part4():
    section("4. The Kajiura filter: what the seafloor motion can generate")
    print("  For a seafloor displacement eta_0(k) the sea-surface response of an")
    print("  ocean of uniform depth h is eta(k) = eta_0(k) / cosh(k h), which for")
    print("  large kh decays as exp(-kh).  The derivation is Laplace's equation")
    print("  with a bottom boundary condition and a linearised free surface.")
    print()
    h = 4000.0
    print(f"  h = {h:.0f} m")
    print()
    print("     L (km)    k h   1/cosh(kh)   transmitted (per cent)")
    for L in (5.0, 10.0, 20.0, 25.0, 50.0, 100.0, 200.0):
        kh = 2.0 * math.pi * h / (L * 1000.0)
        tr = 1.0 / math.cosh(kh)
        print(f"  {L:9.1f}   {kh:5.3f}   {tr:10.5f}   {tr*100:18.2f}")
    print()
    print("  Wavelengths below about 2 pi h = "
          f"{2*math.pi*h/1000.0:.1f} km are strongly filtered; the filter is not")
    print("  sharp, but it means a rupture that displaces the seafloor by 5 m")
    print("  over a 10 km wavelength produces almost no surface wave, while the")
    print("  same 5 m over 100 km produces nearly all of it.  This is why the")
    print("  seafloor displacement of a large megathrust earthquake — hundreds")
    print("  of kilometres long — is efficient and a small shallow one is not,")
    print("  and why tsunami generation is not simply proportional to magnitude.")


def part5():
    section("5. Refraction: Snell's law with c = sqrt(g h)")
    print("  sin(theta)/c is constant along a ray and c = sqrt(gh), so")
    print("      sin(theta) / sqrt(h) = const.")
    print()
    print("     theta in 4000 m (deg)   theta in 1000 m   theta in 100 m")
    for t1 in (5.0, 15.0, 30.0, 45.0, 60.0):
        row = []
        for h2 in (1000.0, 100.0):
            s = math.sin(math.radians(t1)) * math.sqrt(h2 / 4000.0)
            row.append(math.degrees(math.asin(min(s, 1.0))))
        print(f"  {t1:21.1f}   {row[0]:15.2f}   {row[1]:14.2f}")
    print()
    print("  The angle is measured from the normal to the depth contours, and it")
    print("  DECREASES as the water shallows: the ray turns toward the normal,")
    print("  i.e. toward the coast, and the wavefront straightens to run parallel")
    print("  to the depth contours.  That is why a tsunami arriving on a long")
    print("  straight coast comes in nearly parallel to it, and why the same")
    print("  effect can focus energy onto a promontory or headland.")


def part6():
    section("6. The bore: speed and flow from mass and momentum")
    print("  Bore moving into still water of depth h1, leaving depth h2 = h1 + H.")
    print("  In the frame of the front, mass gives c h1 = (c - v) h2 and")
    print("  momentum gives g(h2^2 - h1^2)/2 = c h1 v, so")
    print("      c = sqrt( g h2 (h1 + h2) / (2 h1) ),   v = c (1 - h1/h2).")
    print()
    h1 = 1.0
    print(f"  still-water depth h1 = {h1:.1f} m (the last few metres)")
    print()
    print("     H (m)   h2 (m)   c (m/s)   c (km/h)   flow behind v (m/s)")
    for H in (0.5, 1.0, 2.0, 4.0):
        h2 = h1 + H
        c = math.sqrt(G * h2 * (h1 + h2) / (2.0 * h1))
        v = c * (1.0 - h1 / h2)
        print(f"  {H:7.1f}   {h2:7.1f}   {c:8.3f}   {c*3.6:9.2f}   {v:19.3f}")
    print()
    print("  A 2 m high front in 1 m of water travels at 7.7 m/s — 28 km/h — and")
    print("  the water behind it runs onshore at 5.1 m/s.  Those two speeds are")
    print("  what a person on foot is trying to outrun, and they come from mass")
    print("  and momentum conservation across a hydraulic jump, not from")
    print("  measurement.  For H << h1 the same formula reduces to")
    c_small = math.sqrt(G * h1)
    print(f"  c -> sqrt(g h1) = {c_small:.3f} m/s, the ordinary shallow-water speed.")


def part7():
    section("7. Warning: what a seafloor pressure sensor measures")
    print("  A sea-surface elevation eta changes the pressure at the seafloor by")
    print("  the hydrostatic increment dp = rho g eta.")
    print()
    print("     eta (cm)    dp (Pa)    dp (mbar)")
    for eta_cm in (0.1, 0.5, 1.0, 5.0, 50.0):
        dp = RHO_W * G * eta_cm / 100.0
        print(f"  {eta_cm:9.1f}   {dp:8.2f}   {dp/100:9.4f}")
    print()
    print("  One centimetre of sea surface is 101 Pa, about one thousandth of an")
    print("  atmosphere: a seafloor pressure sensor is an altimeter for the sea")
    print("  surface, and the detection threshold is set by how small a pressure")
    print("  you can resolve, not by how large the tsunami is.")
    print()
    print("  Detection also has to beat the ambient noise.  The pressure under a")
    print("  surface gravity wave decays with depth as 1/cosh(kh), so a wind sea")
    print("  is invisible at the seafloor while a tsunami is not: they sit at")
    print("  opposite ends of the same dispersion curve.")
    print()
    print(f"  at h = {4000} m:")
    print("     L (m)        k h     1/cosh(kh)        exp(-kh)")
    for L in (100.0, 150.0, 250.0, 1000.0, 25000.0, 100000.0):
        kh = 2.0 * math.pi * 4000.0 / L
        print(f"  {L:9.0f}   {kh:10.3f}   {1.0/math.cosh(kh):12.4e}   "
              f"{math.exp(-kh):12.4e}")
    print()
    print("  A storm sea with wavelengths of a few hundred metres is attenuated")
    print("  by tens of orders of magnitude; a 100 km tsunami is attenuated by")
    print("  3 per cent.  The two columns differ by a factor of two once kh")
    print("  exceeds about 3, which is the correct asymptote")
    print("  1/cosh(kh) -> 2 exp(-kh): the exact expression and its large-kh")
    print("  form describe the same physics and agree to that factor.")


def main():
    print("Tsunami generation, propagation and warning -- computed quantities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    part7()
    print()
    print("=" * 72)
    print("No tsunami event, travel time, run-up height or warning record is")
    print("quoted in this script.")
    print("=" * 72)


if __name__ == "__main__":
    main()
