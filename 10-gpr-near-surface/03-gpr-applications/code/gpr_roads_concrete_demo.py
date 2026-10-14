#!/usr/bin/env python3
"""GPR for pavements, concrete and infrastructure: layer thickness, the metal
plate calibration, thin-layer interference, rebar and multiples.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_roads_concrete_demo.py

All models and data in this module are SYNTHETIC.  The permittivities, layer
thicknesses, cover depths and pick errors are chosen teaching values, not
measurements of any road, bridge deck or building.  Physical constants and
standard material permittivities (water, air, ice) are labelled as such.

Contents
--------
1. Layer thickness from a two-way time, and its sensitivity to eps_r.
2. The metal plate calibration: eps_r from the surface reflection amplitude,
   with a round-trip verification against a chosen truth.
3. Thin-layer interference: the exact three-layer response, the tuning
   thickness, and the two thicknesses that give the same amplitude.
4. Rebar: cover depth and spacing from diffraction apexes, velocity from the
   hyperbola curvature.
5. Multiples: where the layer multiple appears and what it can be mistaken for.
6. A depth budget for a layer thickness measurement.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458        # m/ns (exact)
EPS_AIR = 1.0               # air
EPS_ASPHALT = 4.5           # SYNTHETIC asphalt permittivity
EPS_BASE_WET = 9.0          # SYNTHETIC wet base
EPS_BASE_DRY = 3.0          # SYNTHETIC dry base
F0_GHZ = 1.5                # SYNTHETIC antenna centre frequency, GHz


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def v_of_eps(eps):
    return C_M_NS / np.sqrt(eps)


def reflection_coeff(eps1, eps2):
    return (np.sqrt(eps1) - np.sqrt(eps2)) / (np.sqrt(eps1) + np.sqrt(eps2))


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def slab_response(h_m, eps1, eps2, eps0=EPS_AIR, f0_hz=F0_GHZ * 1e9,
                  n=4096, dt_ns=0.01):
    """Peak-to-peak of the reflected pulse from a slab, normalised to the
    response of a perfect reflector (metal plate) convolved with the pulse.

    Exact three-layer reflection coefficient:
        r(w) = (r01 + r12 exp(-2 i w h / v1)) / (1 + r01 r12 exp(-2 i w h / v1))
    evaluated on the Ricker spectrum of the antenna and inverse transformed.
    """
    r01 = reflection_coeff(eps0, eps1)
    r12 = reflection_coeff(eps1, eps2)
    v1 = v_of_eps(eps1)
    t = np.arange(n) * dt_ns
    pulse = ricker(t, 4.0, f0_hz * 1e-9)
    P = np.fft.rfft(pulse)
    f = np.fft.rfftfreq(n, dt_ns * 1e-9)
    w = 2.0 * np.pi * f
    # h_m / v1 is in ns (v is in m/ns); the phase needs seconds.
    phase = np.exp(-2j * w * (h_m / v1) * 1e-9)
    r = (r01 + r12 * phase) / (1.0 + r01 * r12 * phase)
    out = np.fft.irfft(P * r, n=n)
    ref = np.fft.irfft(P * (-1.0), n=n)
    return (out.max() - out.min()) / (ref.max() - ref.min()), out


def main():
    section("1. Layer thickness from a two-way time")
    v_asph = v_of_eps(EPS_ASPHALT)
    print(f"SYNTHETIC asphalt eps_r = {EPS_ASPHALT:.1f} -> v = {v_asph:.4f} m/ns")
    print(f"  h = v t / 2, so dh/h = d(eps_r)/(2 eps_r): the permittivity is the")
    print(f"  whole error budget.  A +5% error in eps_r gives "
          f"{(1.0 / np.sqrt(1.05) - 1.0) * 100:+.2f}% in thickness.")
    print("  t (ns)   eps_r assumed   h (mm)   error vs eps_r = 4.5 (mm)")
    for eps in (4.0, 4.5, 5.0, 5.5):
        t_ns = 1.00
        h = v_of_eps(eps) * t_ns / 2.0 * 1e3
        print(f"  {t_ns:6.2f}   {eps:13.1f}   {h:6.1f}   "
              f"{h - v_asph * t_ns / 2.0 * 1e3:+23.1f}")
    print("  One measured two-way time of 1.00 ns, four candidate permittivities,")
    print("  and a thickness anywhere from 63.9 to 74.9 mm.  The permittivity is")
    print("  not a nuisance correction to the geometry; it IS the geometry.")

    section("2. The metal plate calibration of eps_r")
    print("  With the antenna on the surface and a metal plate at the surface the")
    print("  response is R = -1 by definition; the surface reflection is")
    print("  R = (1 - sqrt(eps_r)) / (1 + sqrt(eps_r)) against it.")
    for eps in (4.0, EPS_ASPHALT, 5.5, 9.0):
        r = reflection_coeff(EPS_AIR, eps)
        eps_inv = ((1.0 - r) / (1.0 + r)) ** 2
        print(f"  true eps_r {eps:5.2f} -> R = {r:+.4f} -> eps_r recovered "
              f"{eps_inv:6.3f}  (exact round trip: {abs(eps_inv - eps) < 1e-9})")
    print("\n  The inversion is exact and algebraic, so the error in eps_r comes")
    print("  entirely from the amplitude measurement: d(eps_r)/eps_r = 4 dR/(1-R^2).")
    for dr in (0.01, 0.02, 0.05):
        r = reflection_coeff(EPS_AIR, EPS_ASPHALT)
        rel = abs(4.0 * dr / (1.0 - r ** 2))
        print(f"  an amplitude error of {dr:.2f} in R -> {rel * 100:.2f}% in eps_r"
              f" -> {rel / 2 * 100:.2f}% in thickness")

    section("3. Thin-layer interference: what an amplitude can and cannot say")
    print("  exact three-layer response of an asphalt slab between air and base;")
    print("  p2p is normalised to the response of a perfect reflector")
    r02_wet = abs(reflection_coeff(EPS_AIR, EPS_BASE_WET))
    p_zero, _ = slab_response(1e-9, EPS_ASPHALT, EPS_BASE_WET)
    print(f"  check on the limit h -> 0: the slab disappears and the response")
    print(f"  magnitude must equal the air/base contact |r02| = {r02_wet:.4f}; the")
    print(f"  formula returns {p_zero:.4f}")
    print("  h (mm)   tau (ns)   p2p, wet base   p2p, dry base")
    for h_mm in (5.0, 10.0, 15.0, 20.0, 24.0, 30.0, 40.0, 47.0, 60.0, 90.0, 140.0):
        h = h_mm * 1e-3
        p_wet, _ = slab_response(h, EPS_ASPHALT, EPS_BASE_WET)
        p_dry, _ = slab_response(h, EPS_ASPHALT, EPS_BASE_DRY)
        print(f"  {h_mm:6.1f}   {2 * h / v_asph:8.3f}   {p_wet:14.4f}   "
              f"{p_dry:14.4f}")
    print(f"\n  lam = v/f = {v_asph / F0_GHZ * 1e3:.1f} mm, so lam/4 = "
          f"{v_asph / F0_GHZ * 1e3 / 4:.1f} mm, and the interference is at its")
    print("  strongest near lam/4.  In the table the wet base gives a MINIMUM")
    print("  there (0.3165 at 20 mm, 12% below the asymptotic 0.3592) while the dry")
    print("  base gives a MAXIMUM (0.4441 at 20 mm, 24% above it).  Whether a")
    print("  quarter-wave slab is bright or dim is decided by the SIGN of the base")
    print("  contrast, which is not known in advance.")
    print("  For h well above lam/4 the two echoes separate in time and the")
    print("  composite amplitude converges on the surface coefficient alone, 0.3592")
    print("  -- a second independent check on the implementation.")
    print("  The composite response is therefore NOT monotonic in h, and below")
    print("  lam/4 the amplitude carries h only jointly with the base contrast:")
    hs = np.linspace(0.002, 0.150, 149)
    pps = np.array([slab_response(h, EPS_ASPHALT, EPS_BASE_WET)[0] for h in hs])
    target = slab_response(0.030, EPS_ASPHALT, EPS_BASE_WET)[0]
    hits = hs[np.abs(pps - target) < 0.002]
    print(f"\n  The ambiguity, measured: an amplitude of {target:.4f} is returned by")
    print("  every one of these thicknesses (mm): "
          + ", ".join(f"{h * 1e3:.1f}" for h in hits))
    print(f"  Their two-way times differ by a factor of {hits[-1] / hits[0]:.0f},")
    print("  so no timing measurement separates them.  Below the resolution limit a")
    print("  slab thickness is an inverse problem in (h, layer permittivity, base")
    print("  contrast, wavelet), not a pick.")

    section("4. Rebar: cover depth and spacing from the apexes")
    eps_conc = 6.0
    v_conc = v_of_eps(eps_conc)
    cover, spacing = 0.060, 0.150
    print(f"SYNTHETIC dry concrete eps_r = {eps_conc:.1f} -> v = {v_conc:.4f} m/ns")
    print(f"  cover {cover * 1e3:.0f} mm, bar spacing {spacing * 1e3:.0f} mm")
    print("  offset x (m)   apex two-way time (ns)   depth if v is right (mm)")
    x = np.array([0.0, 0.05, 0.10, 0.15, 0.20, 0.30])
    t_bar = 2.0 * np.sqrt(x ** 2 + cover ** 2) / v_conc
    for xi, ti in zip(x, t_bar):
        print(f"  {xi:12.2f}   {ti:23.2f}   {v_conc * ti / 2.0 * 1e3:24.1f}")
    # velocity and cover from a Monte Carlo fit of the first four samples
    x_fit = x[:4]
    t_clean = 2.0 * np.sqrt(x_fit ** 2 + cover ** 2) / v_conc
    vs, zs = [], []
    for _ in range(4000):
        t_noisy = t_clean + RNG.normal(0.0, 0.02, x_fit.size)
        m, c = np.polyfit(x_fit ** 2, t_noisy ** 2, 1)
        vv = 2.0 / np.sqrt(m)
        vs.append(vv)
        zs.append(np.sqrt(c) * vv / 2.0)
    vs = np.array(vs)
    zs = np.array(zs)
    print(f"\n  from a +/-0.30 m aperture with 0.02 ns picking error:")
    print(f"    velocity {vs.mean():.4f} +/- {vs.std():.4f} m/ns "
          f"({vs.std() / vs.mean() * 100:.1f}%)")
    print(f"    cover    {zs.mean() * 1e3:.1f} +/- {zs.std() * 1e3:.1f} mm "
          f"({zs.std() / zs.mean() * 100:.1f}%)")
    print("  The spacing of the bars is read directly from the spacing of the")
    print("  apexes, which measures the RULE, not the velocity, and is therefore")
    print("  exact in the limit of well-picked apexes.  The cover depth needs the")
    print("  velocity, and the velocity needs an aperture.")

    section("5. Multiples: where they land and what they mimic")
    for h_mm in (30.0, 60.0, 90.0, 140.0):
        h = h_mm * 1e-3
        tau = 2.0 * h / v_asph
        print(f"  slab {h_mm:6.1f} mm: primary {tau:6.3f} ns, layer multiple "
              f"{2 * tau:6.3f} ns,")
        print(f"      the multiple's apparent depth as a primary "
              f"{v_asph * 2 * tau / 2.0 * 1e3:7.1f} mm (true slab "
              f"{h_mm:.1f} mm)")
    print("\n  In a layered road the multiple of a thin surface layer lands in")
    print("  the time window of the layers below it.  It is separated by its")
    print("  moveout (which is larger) and by its dependence on the layer above,")
    print("  not by its travel time.")

    section("6. A depth budget for one layer thickness")
    t_ns, eps_rel, t_rel = 1.4, 0.03, 0.01
    h_nom = v_asph * t_ns / 2.0 * 1e3
    n = 20000
    e_draw = EPS_ASPHALT * (1.0 + eps_rel * RNG.standard_normal(n))
    t_draw = t_ns * (1.0 + t_rel * RNG.standard_normal(n))
    h_draw = v_of_eps(e_draw) * t_draw / 2.0 * 1e3
    print(f"  nominal {h_nom:.1f} mm from t = {t_ns:.1f} ns and eps_r = "
          f"{EPS_ASPHALT:.1f}")
    print(f"  3% eps_r error and 1% time error -> {h_draw.mean():.1f} +/- "
          f"{h_draw.std():.1f} mm (1 sigma)")
    print(f"    eps_r alone: "
          f"{np.std(v_of_eps(e_draw) * t_ns / 2.0 * 1e3):.2f} mm; time alone: "
          f"{np.std(v_asph * t_draw / 2.0 * 1e3):.2f} mm")
    print("  For a 100 mm design layer the permittivity error contributes about")
    print("  1.5 mm and the timing about 1.0 mm.  The method is precise enough to")
    print("  control a paving operation, but only if the permittivity is measured")
    print("  on site, per layer, by the metal plate method of Section 2: an")
    print("  assumed permittivity error of 20% would be a 10 mm thickness error,")
    print("  which is the tolerance of the whole job.")


if __name__ == "__main__":
    main()
