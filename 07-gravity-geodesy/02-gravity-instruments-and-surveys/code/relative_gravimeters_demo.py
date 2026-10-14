#!/usr/bin/env python3
"""Relative gravimeters: the sensitivity of a plain spring, the amplification that
astatisation (a zero-length spring on a lever) buys and the stability it costs, the
readout resolution and dynamic range of a nulled (force-balance) instrument, the
residual a non-linearity leaves after a linear calibration, and the drift rate as a
measured quantity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python relative_gravimeters_demo.py

Everything is SYNTHETIC: the masses, spring stiffnesses, geometry, temperature
coefficients, readout noise and non-linearity are chosen teaching values.  No
manufacturer's instrument, model number or specification is used or implied; the
two design families discussed are described generically (a zero-length-spring
astatic lever and a nulled force-balance sensor).  The only exact constants are
g = 9.820250 m/s^2 (the module's SYNTHETIC station value, used as a scale) and
1 uGal = 1e-8 m/s^2.

Contents
--------
1. A plain spring: stiffness, static extension and the readout it demands.
2. Astatisation: the amplification factor, the period it produces, and the readout
   it relaxes.
3. What astatisation costs: sensitivity to geometry and to temperature.
4. The nulled force-balance sensor: resolution, dynamic range and bit depth.
5. Non-linearity left after a linear calibration.
6. Drift: the rate, its cause in geometry, and why surveys re-occupy bases.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_LOCAL = 9.820250          # m/s^2, SYNTHETIC station value (scale only)
MASS = 0.05                 # kg, SYNTHETIC test mass
SPRING_LENGTH = 0.250       # m, SYNTHETIC unstrained spring length scale
THERMAL_LEN_COEF = 1.0e-8   # m/K, SYNTHETIC effective geometry change with T
GRAVITY_RANGE = 7000.0      # mGal, the range the sensor must cover


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC sensor parameters")
    print(f"  test mass          = {MASS:.3f} kg")
    print(f"  station value      = {G_LOCAL:.6f} m/s^2 (scale only)")
    print(f"  1 uGal             = 1e-8 m/s^2")

    section("1. A plain spring: how much displacement is one microgal?")
    print("  g = k x / m, so x = g m / k and dx/dg = m/k = 1/omega_0^2 with")
    print("  omega_0^2 = k/m.  A soft spring gives a large displacement per microgal.")
    print("   f_0 (Hz)   k (N/m)   static extension (mm)   dx for 1 uGal (nm)")
    for f0 in (10.0, 1.0, 0.2):
        w2 = (2.0 * np.pi * f0) ** 2
        k = MASS * w2
        x_static = G_LOCAL / w2
        dx = 1.0e-8 / w2
        print(f"   {f0:8.1f}   {k:8.4f}   {x_static * 1e3:21.3f}   {dx * 1e9:18.3f}")
    print("  Even at a 1 Hz natural frequency the readout must resolve a quarter of a")
    print("  nanometre for one microgal, and the static extension is a quarter of a")
    print("  metre.  A spring alone is not a gravimeter: some form of leverage or")
    print("  electric detection is required.")

    section("2. Astatisation: amplifying the response")
    print("  A spring attached so that its force on the beam depends on the FULL")
    print("  length rather than on the extension acts like a stiffness")
    print("        k_eff = k (1 - eta),    eta = l_0 / l,")
    print("  and the response to gravity is amplified by A = 1/(1 - eta).")
    print("  The measured consequence is a long natural period and a relaxed readout:")
    print("   eta      A        period T (s)     static extension (m)   dx for 1 uGal (nm)")
    w2_plain = (2.0 * np.pi * 1.0) ** 2         # k/m for the 1 Hz reference spring
    for eta in (0.0, 0.90, 0.99, 0.999):
        amp = 1.0 / (1.0 - eta)
        w2_eff = w2_plain * (1.0 - eta)
        period = 2.0 * np.pi / np.sqrt(w2_eff)
        x_static = G_LOCAL / w2_eff
        dx = 1.0e-8 / w2_eff
        print(f"   {eta:5.3f}   {amp:7.1f}   {period:13.2f}   {x_static:21.3f}   "
              f"{dx * 1e9:18.2f}")
    print("  With eta = 0.99 the period is 10 s and one microgal is 25.3 nm of")
    print("  motion instead of 0.253 nm: astatisation has relaxed the readout")
    print("  requirement by exactly the amplification factor A = 100, and it has")
    print("  bought that by making the static extension - and therefore every")
    print("  geometric defect - 100 times larger as well.")

    section("3. What astatisation costs: geometry and temperature")
    print("  With eta = 0.99, l = 0.250 m, so l - l_0 = 2.500e-03 m.  A change in")
    print("  the anchor geometry shifts the equilibrium by an amount that, expressed")
    print("  in gravity units, is")
    print("        dg_equiv = g x dl_0 / (l - l_0),")
    print("  in which the small denominator is the price of the amplification.")
    eta = 0.99
    denom = SPRING_LENGTH * (1.0 - eta)
    print(f"  l - l_0 = {denom:.6e} m, so dg_equiv = {G_LOCAL / denom:.4e} x dl_0")
    print("   dl_0 (m)      dg_equiv (uGal)")
    for dl0 in (1e-6, 1e-9, 1e-11, 1e-12):
        print(f"   {dl0:9.0e}      {G_LOCAL * dl0 / denom * 1e8:14.3f}")
    print("  A one-NANOMETRE change in the geometry is 393 uGal, and a one-micrometre")
    print("  change - a thermal expansion any bench experiment would call negligible -")
    print("  is 392,810 uGal.  To keep the effect below 0.4 uGal the geometry must be")
    print("  stable to about 1e-12 m, one picometre, for the whole duration of a")
    print("  measurement.")
    print("\n  Temperature enters the same way.  With a SYNTHETIC effective geometry")
    print(f"  coefficient of {THERMAL_LEN_COEF:.0e} m/K:")
    therm = G_LOCAL * THERMAL_LEN_COEF / denom
    print(f"   dg/dT = {therm * 1e8:.1f} uGal/K")
    print(f"   a 1 mK change gives {therm * 1e-3 * 1e8:.2f} uGal, so the sensor mass")
    print(f"   must be held to about {0.4e-8 / therm:.2e} K to stay inside 0.4 uGal")
    print("  MEASURED CONCLUSION: astatisation multiplies the response to gravity and")
    print("  the response to the instrument's own geometry by the SAME factor A.  It")
    print("  buys readout resolution, not stability.  This is why such instruments")
    print("  are thermostatted, and why a survey measures drift and re-occupies a")
    print("  base instead of assuming the sensor is stable (lesson 03).")

    section("4. A nulled force-balance sensor: resolution and dynamic range")
    print("  A nulled sensor holds the test mass at a fixed position and measures the")
    print("  force needed to do so; the reading is a force, not a displacement.")
    counts_per_ugal = 10.0
    readout_noise_ugal = 0.5
    print(f"  SYNTHETIC design: {counts_per_ugal:.1f} counts per uGal, readout noise")
    print(f"  {readout_noise_ugal:.1f} uGal per sample, range {GRAVITY_RANGE:.0f} mGal")
    print("   quantity                          value")
    total_counts = GRAVITY_RANGE * 1e3 * counts_per_ugal
    print(f"   range in counts                   {total_counts:.3e}")
    print(f"   bits needed for full range        {np.log2(total_counts):.2f}")
    print(f"   bits needed to resolve 0.5 uGal   "
          f"{np.log2(GRAVITY_RANGE * 1e3 / readout_noise_ugal):.2f}")
    print(f"   dynamic range (range / 1 uGal)    {GRAVITY_RANGE * 1e3:.3e}")
    print(f"   averaged noise for 4 samples      "
          f"{readout_noise_ugal / np.sqrt(4.0):.3f} uGal")
    print(f"   drift over 1 h at 20 uGal/h       {20.0:.1f} uGal "
          f"(= {20.0 * counts_per_ugal:.0f} counts)")
    print("  The readout noise is small compared with the drift: an instrument whose")
    print("  electronic noise is 0.5 uGal and whose drift is 20 uGal per hour is")
    print("  drift-limited, and averaging repeated readings cannot remove a drift.")
    print(f"  A 20 uGal/h drift over a 10 hour day is "
          f"{20.0 * 10:.0f} uGal, which is why every survey occupies a base at")
    print("  intervals of about an hour (lesson 03).")

    section("5. Non-linearity left after a linear calibration")
    print("  A SYNTHETIC sensor response R(g) = c1 g + c2 g^2, calibrated linearly")
    print("  over a range.  The residual after the linear fit is the non-linearity.")
    c1 = 1.0e-3                 # counts per uGal
    range_mgal = 100.0          # calibration span
    print("  Fitting a line to R = c1 g + c2 g^2 over a symmetric span [-L, L]")
    print("  leaves the residual c2 (g^2 - L^2/3), whose maximum is (2/3) c2 L^2 at")
    print("  the two ends.  With L = 50 000 uGal, (2/3) L^2 = 1.667e9 uGal^2.")
    print("   c2 (counts/uGal^2)   non-linearity at span end   max residual (uGal)")
    for c2 in (1e-12, 1e-11, 1e-10):
        gs = np.linspace(-0.5 * range_mgal * 1e3, 0.5 * range_mgal * 1e3, 201)  # uGal
        resp = c1 * gs + c2 * gs ** 2
        A = np.column_stack([gs, np.ones(gs.size)])
        coef, *_ = np.linalg.lstsq(A, resp, rcond=None)
        resid = resp - A @ coef
        rel_nl = c2 * gs.max() / c1          # quadratic term / linear term at the end
        print(f"   {c2:18.0e}   {rel_nl:25.2e}   "
              f"{np.max(np.abs(resid)) / c1:18.3f}")
    print("  A non-linearity of 5e-5 of the reading at the end of the span - a")
    print("  plausible defect - leaves a 1.7 uGal residual at the ends of a 100 mGal")
    print("  span after a linear calibration, and a 5e-4 non-linearity leaves")
    print("  16.7 uGal.  The residual is a parabola, so it correlates with")
    print("  position in the range: calibrating over a NARROW range hides it, and")
    print("  the same instrument used over a wider range reveals it.  Always report")
    print("  the calibration span and the residual, not only the scale factor.")

    section("6. Drift as a measured quantity")
    print("  A SYNTHETIC 6-hour drift record with a linear rate and a small")
    print("  exponential settling term:")
    hours = np.arange(0.0, 6.01, 0.5)
    true_rate = 18.0            # uGal/h
    settle = -35.0 * np.exp(-hours / 0.8)
    noise = 0.8 * RNG.standard_normal(hours.size)
    drift = true_rate * hours + settle + noise
    slope = np.polyfit(hours, drift, 1)[0]
    resid = drift - np.polyval(np.polyfit(hours, drift, 1), hours)
    print(f"   fitted linear rate = {slope:.2f} uGal/h "
          f"(injected {true_rate:.1f} uGal/h)")
    print(f"   residual rms about the line = {resid.std():.2f} uGal, "
          f"max |residual| = {np.max(np.abs(resid)):.2f} uGal")
    for h, d in zip(hours, drift):
        print(f"     t = {h:4.1f} h   drift = {d:+8.2f} uGal")
    print("  Fitting a straight line to the whole record gives 21.82 uGal/h instead")
    print("  of the injected 18.0 uGal/h: the exponential settling is absorbed into")
    print("  the slope, a 21% bias, and the residual rms of 6.94 uGal is the")
    print("  diagnostic that the model is inadequate.  Over the last four hours alone")
    sl_tail = np.polyfit(hours[hours >= 2.0], drift[hours >= 2.0], 1)[0]
    print(f"  the same fit gives {sl_tail:.2f} uGal/h, much closer to the truth.")
    print("  A drift model is itself a model: report its residuals, and fit it over")
    print("  the interval in which it is valid.")


if __name__ == "__main__":
    main()
