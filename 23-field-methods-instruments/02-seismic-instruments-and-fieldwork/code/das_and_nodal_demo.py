#!/usr/bin/env python3
"""Nodal and distributed-acoustic-sensing arithmetic, on SYNTHETIC parameters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python das_and_nodal_demo.py

Everything here is SYNTHETIC.  The gauge lengths, channel spacings, velocities,
battery lifetimes and strain sensitivities are chosen teaching values.  No
manufacturer specification, no measured fibre response and no field deployment
figure is used or reproduced.

Sections
--------
1. The gauge-length response of a DAS channel and its notches.
2. Channel spacing and spatial aliasing of the strain field.
3. Converting between strain rate, velocity and acceleration for a plane wave.
4. Nodal systems: channel count, recording duty cycle and battery margin.
5. Strain sensitivity referred to ground motion.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

VELOCITY = 1500.0        # apparent velocity of the wave along the fibre, m/s


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def gauge_response(f, gauge_m, velocity=VELOCITY):
    """|sinc(pi f L / v)| for a gauge of length L averaging a plane wave."""
    x = np.pi * np.asarray(f, dtype=float) * gauge_m / velocity
    out = np.ones_like(x)
    nonzero = x != 0.0
    out[nonzero] = np.abs(np.sin(x[nonzero]) / x[nonzero])
    return out


def main():
    section("1. Gauge-length response and its notches")
    print(f"  apparent velocity along the fibre = {VELOCITY:.0f} m/s")
    print("  response = |sinc(pi f L / v)|; zeros at f = k v / L")
    print(f"  {'gauge (m)':>10s} {'first notch (Hz)':>17s} "
          f"{'response at 50 Hz':>18s} {'response at 100 Hz':>19s}")
    for gauge in (1.0, 5.0, 10.0, 20.0):
        notch = VELOCITY / gauge
        print(f"  {gauge:10.1f} {notch:17.1f} "
              f"{gauge_response(50.0, gauge):18.4f} "
              f"{gauge_response(100.0, gauge):19.4f}")
    print("  -> a longer gauge is quieter and smoother at low frequency and")
    print("     BLIND near f = v/L.  Choosing the gauge is choosing which")
    print("     frequencies you will not see.")

    section("2. Channel spacing and spatial aliasing")
    print("  f_alias = v / (2 dx); above it the apparent velocity is aliased")
    print(f"  {'dx (m)':>8s} {'f_alias (Hz)':>14s} {'channels per km':>17s}")
    for dx in (0.5, 1.0, 2.0, 5.0, 10.0):
        print(f"  {dx:8.2f} {VELOCITY / (2.0 * dx):14.1f} "
              f"{1000.0 / dx:17.0f}")
    print("  -> a 1 m channel spacing gives 1000 channels per km and an alias")
    print("     frequency of 750 Hz at this velocity; the common 10 m spacing")
    print("     gives 100 channels per km and aliases above 75 Hz.")

    section("3. Strain rate, velocity and acceleration for a plane wave")
    print("  for u = A exp(i(kx - wt)):  strain = kA, strain rate = w k A,")
    print("  velocity = w A, acceleration = w^2 A, so strain rate = a / v")
    print(f"  {'f (Hz)':>8s} {'1 nm/s velocity -> strain rate (1/s)':>37s}"
          f" {'acceleration (m/s^2)':>22s}")
    for f in (1.0, 5.0, 10.0, 50.0):
        w = 2.0 * np.pi * f
        k = w / VELOCITY
        v_amp = 1.0e-9
        print(f"  {f:8.1f} {v_amp * k:37.3e} {v_amp * w:22.3e}")
    print("  -> DAS reports strain or strain rate; every comparison with a")
    print("     seismometer requires this conversion, and the factor depends on")
    print("     frequency and on the apparent velocity along the fibre.")

    section("4. Nodal systems: channels, duty cycle and battery margin")
    n_nodes = 1000
    n_day = 20
    battery_days_continuous = 30.0
    print(f"  {n_nodes} nodes, {n_day}-day survey; a node records continuously")
    print(f"  for {battery_days_continuous:.0f} days on one battery set (chosen)")
    print(f"  continuous margin = {battery_days_continuous / n_day:.2f}x")
    print(f"  {'duty cycle':>14s} {'lifetime (days)':>17s} {'margin':>9s}"
          f" {'hours recorded/day':>19s}")
    for on_hours, off_hours in ((24.0, 0.0), (12.0, 12.0), (6.0, 18.0),
                                (4.0, 20.0)):
        duty = on_hours / 24.0
        lifetime = battery_days_continuous / duty if duty > 0 else np.inf
        print(f"  {f'{on_hours:.0f} on / {off_hours:.0f} off':>14s} "
              f"{lifetime:17.1f} {lifetime / n_day:9.2f} "
              f"{on_hours:19.1f}")
    print("  -> duty cycling buys margin and costs the record you did not take;")
    print("     the data volume and the harvest labour are the real constraints.")

    section("5. Strain sensitivity referred to ground motion")
    strain_noise = 1.0e-9      # 1 nanostrain, a chosen single-sample level
    print(f"  chosen strain sensitivity = {strain_noise:.0e} (1 nanostrain)")
    print(f"  {'f (Hz)':>8s} {'velocity (m/s)':>16s} {'acceleration (m/s^2)':>22s}"
          f" {'equivalent to (chosen ambient)':>32s}")
    ambient = {1.0: 5.958e-8, 5.0: 3.0e-8, 10.0: 2.864e-8, 50.0: 2.619e-8}
    for f in (1.0, 5.0, 10.0, 50.0):
        w = 2.0 * np.pi * f
        k = w / VELOCITY
        v_equiv = strain_noise / k
        a_equiv = strain_noise * VELOCITY
        print(f"  {f:8.1f} {v_equiv:16.3e} {a_equiv:22.3e} "
              f"{v_equiv / ambient[f]:32.2f}x ambient")
    print("  (strain rate converted to velocity by dividing by k; the")
    print("   acceleration row is frequency-independent because strain rate and")
    print("   acceleration differ by the constant factor v)")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a DAS and nodal model, not any real system.")


if __name__ == "__main__":
    main()
