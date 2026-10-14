#!/usr/bin/env python3
"""Microseismic monitoring of geothermal fields: source scaling, detection range,
catalogue bias, location bias from a velocity error, and the pressure front.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python microseismic_geothermal_demo.py

Contents
--------
1. Source scaling: moment, magnitude, slip and corner frequency.
2. Detection radius versus magnitude, and the distance-dependent magnitude of
   completeness.
3. Catalogue bias: a Gutenberg-Richter b-value fitted to a threshold-limited
   synthetic catalogue.
4. Location bias from a velocity-model error, against the random error.
5. Hydraulic diffusivity and the pore-pressure front.

All models and numbers are SYNTHETIC teaching values: chosen stress drops, a
chosen amplitude model and chosen acquisition geometries.  The constants used
are physical or stated conventions.
"""

import numpy as np
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

MU_SHEAR = 25.0e9        # Pa, chosen shear modulus of the reservoir rock
V_S = 3000.0             # m/s, S-wave velocity (chosen)
Q_S = 50.0               # quality factor for S waves (chosen)
BRUNE = 2.34             # standard Brune-model coefficient for f_c = K v /(2 pi a)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mw_from_m0(m0):
    return 2.0 / 3.0 * (np.log10(m0) - 9.1)


def m0_from_mw(mw):
    return 10.0 ** (1.5 * mw + 9.1)


def corner_freq(radius):
    return BRUNE * V_S / (2.0 * np.pi * radius)


def amplitude(m0, radius, dist):
    """Relative far-field amplitude: plateau M0/r, corner frequency f_c."""
    f_c = corner_freq(radius)
    return m0 * f_c ** 2 * np.exp(-np.pi * f_c * dist / (Q_S * V_S)) / dist


def main():
    section("1. Source scaling")
    dsigma = 3.0e6      # Pa, chosen static stress drop
    print(f"chosen shear modulus mu = {MU_SHEAR / 1e9:.0f} GPa, stress drop "
          f"d_sigma = {dsigma / 1e6:.0f} MPa, v_s = {V_S / 1000:.1f} km/s")
    print("circular crack: M0 = (16/7) d_sigma a^3, Mw = (2/3)(log10 M0 - 9.1),")
    print("mean slip u = M0/(mu pi a^2), corner frequency f_c = 2.34 v_s/(2 pi a)")
    print("\n   radius a (m)   M0 (N m)   Mw    mean slip (mm)   f_c (Hz)")
    for a in (50.0, 100.0, 200.0, 500.0):
        m0 = 16.0 / 7.0 * dsigma * a ** 3
        slip = m0 / (MU_SHEAR * np.pi * a ** 2) * 1000.0
        print(f"  {a:12.0f}   {m0:10.3e}   {mw_from_m0(m0):5.2f}   "
              f"{slip:15.1f}   {corner_freq(a):8.2f}")
    print("Ruptures of tens to hundreds of metres, which is the scale of the")
    print("fracture patches a stimulation moves, give Mw of order 1 to 4: these")
    print("are small events, and the corner frequency of the largest falls below")
    print("the band the shallow layers transmit.")

    section("2. Detection radius and the magnitude of completeness")
    noise_floor = 1.0e-2
    ref_mw, ref_dist = 0.0, 1000.0
    ref_a = (m0_from_mw(ref_mw) * 7.0 / (16.0 * dsigma)) ** (1.0 / 3.0)
    ref_amp = amplitude(m0_from_mw(ref_mw), ref_a, ref_dist)
    print("relative amplitude A(r) = M0 f_c^2 exp(-pi f_c r/(Q v))/r,")
    print(f"normalised so that an Mw = {ref_mw:.0f} event at {ref_dist:.0f} m "
          f"has amplitude 1.0")
    print(f"chosen noise floor = {noise_floor:.1e} (a detection threshold 1/100")
    print(f"of a Mw 0 event at 1 km), Q = {Q_S:.0f}")
    print("\n   Mw     radius a (m)   f_c (Hz)   detection radius (m)   "
          "absorption loss at 2 km (%)")
    for mw in np.arange(-1.0, 3.01, 0.5):
        m0 = m0_from_mw(mw)
        a = (m0 * 7.0 / (16.0 * dsigma)) ** (1.0 / 3.0)
        r = 100.0
        while r < 100000.0:
            if amplitude(m0, a, r) / ref_amp < noise_floor:
                break
            r += 50.0
        f_c = corner_freq(a)
        loss = (1.0 - np.exp(-np.pi * f_c * 2000.0 / (Q_S * V_S))) * 100.0
        print(f"  {mw:5.1f}   {a:12.0f}   {f_c:8.2f}   {r:19.0f}   "
              f"{loss:27.1f}")
    print("The detection radius grows with magnitude while the absorption loss")
    print("falls: large events are detected far away because their energy sits")
    print("at low frequency, where the rock is transparent.  The magnitude of")
    print("completeness is therefore a function of position, and a single number")
    print("cannot describe a network.")

    section("3. Catalogue bias in a Gutenberg-Richter fit")
    b_true = 1.0
    m_min = -1.5
    n_true = 40000
    print(f"synthetic volume: events uniform in a half-space to 6 km radius,")
    print(f"magnitudes Gutenberg-Richter with b = {b_true:.1f} above "
          f"Mw = {m_min:.1f}, {n_true} events")
    rho = RNG.random(n_true) ** (1.0 / 3.0) * 6000.0
    az = RNG.uniform(0.0, 2.0 * np.pi, n_true)
    el = RNG.uniform(0.0, 1.0, n_true)
    xy = np.vstack([rho * np.cos(az) * el, rho * np.sin(az) * el])
    depth = rho * np.sqrt(1.0 - el ** 2)
    dist = np.sqrt(xy[0] ** 2 + xy[1] ** 2 + depth ** 2)
    mags_true = m_min - np.log10(1.0 - RNG.random(n_true)) / b_true
    a_true = (m0_from_mw(mags_true) * 7.0 / (16.0 * dsigma)) ** (1.0 / 3.0)
    amps = amplitude(m0_from_mw(mags_true), a_true, np.maximum(dist, 1.0))
    detected = amps >= noise_floor
    mags_det = mags_true[detected]
    print(f"detected {np.sum(detected)} of {n_true} events "
          f"({np.sum(detected) / n_true * 100:.1f}%)")
    print("\n   Mc used (Mw)   number of events   fitted b")
    for mc in (m_min, -0.5, 0.0, 0.5, 1.0):
        sel = mags_det[mags_det >= mc]
        if sel.size < 50:
            print(f"  {mc:13.1f}   {sel.size:16d}   too few")
            continue
        b_fit = 1.0 / (np.log(10.0) * (sel.mean() - mc))
        print(f"  {mc:13.1f}   {sel.size:16d}   {b_fit:9.3f}")
    print(f"\nthe true b is {b_true:.1f}.  Fitting the raw catalogue at a low Mc")
    print("gives a biased, too-small b, because a distant small event is missed")
    print("while an equally small nearby one is kept: the catalogue is")
    print("magnitude- and distance-dependent.  Above Mc = 0.5 the fit recovers")
    print(f"b = 1.0 to within a few percent, and the volume is small enough that")
    print("detection is complete there.  Reporting b requires reporting Mc(r).")

    section("4. Location bias from a velocity-model error")
    sigma_pick = 0.002
    z_lev = np.linspace(-2000.0, -3500.0, 8)
    downhole = np.vstack([np.zeros(8), np.zeros(8), z_lev]).T
    surface = np.array([[0.0, 0.0, 0.0], [500.0, 0.0, 0.0],
                        [0.0, 500.0, 0.0], [500.0, 500.0, 0.0]])
    stations = np.vstack([downhole, surface])
    src = np.array([500.0, 200.0, -3000.0])
    print(f"{downhole.shape[0]} downhole levels from {z_lev[0]:.0f} to "
          f"{z_lev[-1]:.0f} m, plus {surface.shape[0]} surface stations")
    print(f"event at ({src[0]:.0f}, {src[1]:.0f}, {src[2]:.0f}) m, chosen pick "
          f"error = {sigma_pick * 1000:.0f} ms, 100 realisations")

    def locate(v_model, picks):
        def resid(m):
            return (m[3] + np.linalg.norm(stations - m[:3], axis=1) / v_model) \
                - picks
        out = least_squares(resid, np.array([0.0, 0.0, -2000.0, 0.0]),
                            method="trf")
        return out.x[:3]

    print("\n   case                                  travel-time offset (m)   "
          "horizontal (m)   depth (m)")
    for label, v_true, v_used in (("picks and location both at 3.15 km/s",
                                   3150.0, 3150.0),
                                  ("picks 3.15, location 3.00 (5% slow)",
                                   3150.0, 3000.0),
                                  ("picks 2.85, location 3.00 (5% fast)",
                                   2850.0, 3000.0)):
        pt = np.linalg.norm(stations - src, axis=1) / v_true
        offs, horiz, dz = [], [], []
        for _ in range(100):
            picks = pt + sigma_pick * RNG.standard_normal(stations.shape[0])
            est = locate(v_used, picks)
            offs.append(np.linalg.norm(est - src))
            horiz.append(np.hypot(est[0] - src[0], est[1] - src[1]))
            dz.append(est[2] - src[2])
        print(f"  {label:36s}   {np.mean(offs):20.0f}   {np.mean(horiz):14.0f}"
              f"   {np.mean(dz):+9.0f}")
    print("With the right velocity the random error is a few tens of metres and")
    print("has no depth bias, because combining surface and downhole stations")
    print("breaks the depth-origin-time trade-off.  A 5% velocity error multiplies")
    print("the error by about five and pushes it into the horizontal coordinates:")
    print("it is systematic, so it does not average out over a thousand events.")

    section("5. Hydraulic diffusivity and the pressure front")
    mu_visc = 3.0e-4        # Pa s, water at reservoir temperature (chosen)
    phi = 0.05
    c_t = 1.0e-9            # 1/Pa, total compressibility (chosen)
    stor = phi * c_t
    print(f"chosen mu = {mu_visc:.1e} Pa s, porosity {phi:.2f}, total "
          f"compressibility {c_t:.1e} /Pa")
    print(f"storativity per unit volume = phi c_t = {stor:.2e} /Pa")
    print("D = k/(mu phi c_t);  front distance L = sqrt(4 D t)")
    print("\n   permeability (mD)   D (m^2/s)   1 day (m)   30 days (m)   "
          "365 days (m)")
    for k_md in (0.1, 1.0, 10.0, 100.0):
        k_si = k_md * 9.869233e-16
        d_hyd = k_si / (mu_visc * stor)
        row = [np.sqrt(4.0 * d_hyd * t * 86400.0) for t in (1.0, 30.0, 365.0)]
        print(f"  {k_md:17.1f}   {d_hyd:10.4f}   {row[0]:10.0f}   "
              f"{row[1]:11.0f}   {row[2]:11.0f}")
    print("The front grows as the square root of time, so ten times the elapsed")
    print("time moves it by 3.2x, and ten times the permeability moves it by")
    print("3.2x as well.  Microseismicity maps where the pressure change reached")
    print("a fracture already close to failure -- not the flow paths, and not")
    print("the resource.")


if __name__ == "__main__":
    main()
