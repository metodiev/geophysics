#!/usr/bin/env python3
"""Detectability: is the target anomaly larger than the noise?

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python detectability_demo.py

A uniform sphere's exterior field is exactly that of a point mass at its centre,
so no approximation is used.  All parameter values are SYNTHETIC; the noise level
is a stated synthetic instrument repeatability.

Contents
--------
1. Peak anomaly of a sphere target versus noise, as an amplitude signal-to-noise
   ratio, for four targets (two detectable, two not).
2. A simulated survey line: forward model + Gaussian noise, with the measured
   peak, the measured noise level, and a detection test that answers yes or no.
3. The 3-sigma detection limit expressed as a maximum depth for a given body.
4. Stacking: how many repeats N are needed to reach a target noise floor, with
   the measured sqrt(N) reduction.
"""

import numpy as np

G = 6.67430e-11        # m^3 kg^-1 s^-2
MGAL = 1.0e-5          # m s^-2 per mGal
RNG_SEED = 20261014


def sphere_peak_mgal(drho_kg_m3: float, radius_m: float, depth_m: float) -> float:
    """Peak vertical gravity of a uniform sphere whose CENTRE is at depth h."""
    mass = 4.0 / 3.0 * np.pi * radius_m ** 3 * drho_kg_m3
    g = G * mass / depth_m ** 2
    return g / MGAL


def sphere_profile_mgal(x, drho_kg_m3, radius_m, depth_m):
    mass = 4.0 / 3.0 * np.pi * radius_m ** 3 * drho_kg_m3
    return (G * mass * depth_m / (x ** 2 + depth_m ** 2) ** 1.5) / MGAL


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)
    sigma = 0.010          # mGal, SYNTHETIC repeatability (0.01 mGal class instrument)

    print(f"Synthetic instrument repeatability sigma = {sigma:.3f} mGal")
    print("Detection criterion: peak anomaly > 3 sigma = "
          f"{3 * sigma:.3f} mGal (a 3-sigma amplitude detection)\n")

    targets = [
        ("large massive orebody", 1000.0, 50.0, 200.0),
        ("modest massive body", 1000.0, 50.0, 300.0),
        ("deep host-rock variation", 100.0, 100.0, 700.0),
        ("small deep body", 200.0, 20.0, 500.0),
    ]

    print("1. Amplitude signal-to-noise of candidate targets")
    print(f"   {'target':<26}{'drho':>7}{'R (m)':>7}{'depth':>7}"
          f"{'peak (mGal)':>13}{'SNR':>8}{'detectable':>12}")
    for name, drho, radius, depth in targets:
        peak = sphere_peak_mgal(drho, radius, depth)
        snr = peak / sigma
        print(f"   {name:<26}{drho:>7.0f}{radius:>7.0f}{depth:>7.0f}"
              f"{peak:>13.5f}{snr:>8.2f}{('yes' if snr > 3 else 'NO'):>12}")

    # --- 2. Simulated line over the marginal target --------------------------
    print("\n2. Simulated 41-station line over the 'modest massive body'")
    x = np.linspace(-600.0, 600.0, 41)
    clean = sphere_profile_mgal(x, 1000.0, 50.0, 300.0)
    noise = rng.normal(0.0, sigma, size=x.size)
    observed = clean + noise
    peak_obs = float(observed.max())
    # Measured noise from a signal-free part of the line (|x| > 500 m).
    quiet = observed[np.abs(x) > 500.0]
    noise_meas = float(quiet.std(ddof=1))
    print(f"   stations                          = {x.size}")
    print(f"   station spacing                   = {x[1] - x[0]:.1f} m")
    print(f"   forward-model peak (noise-free)   = {clean.max():.5f} mGal")
    print(f"   observed maximum of the noisy line= {peak_obs:.5f} mGal")
    print(f"   measured background std (quiet)   = {noise_meas:.5f} mGal")
    print(f"   measured peak / measured noise    = {peak_obs / noise_meas:.2f}")
    print(f"   detection verdict (> 3)           = "
          f"{'DETECTABLE' if peak_obs / noise_meas > 3 else 'NOT DETECTABLE'}")

    # --- 3. Maximum detectable depth ----------------------------------------
    print("\n3. Maximum depth detectable at 3 sigma (drho = 1000 kg/m^3)")
    print(f"   {'radius (m)':>11}{'max depth (m)':>15}")
    for radius in (25.0, 50.0, 100.0):
        mass = 4.0 / 3.0 * np.pi * radius ** 3 * 1000.0
        # Solve G M / h^2 = 3 sigma  ->  h = sqrt(G M / (3 sigma))
        h = np.sqrt(G * mass / (3.0 * sigma * MGAL))
        print(f"   {radius:>11.0f}{h:>15.1f}")
    print("   -> detectability falls off as the SQUARE of depth: doubling the")
    print("      depth of a fixed body costs a factor of four in amplitude.")

    # --- 4. Stacking to beat the noise --------------------------------------
    print("\n4. Repeat measurements: measured noise of a stack of N repeats")
    print(f"   {'N':>5}{'sigma(mean) (mGal)':>21}{'predicted by 1/sqrt(N)':>25}")
    one_reading = 0.010
    for n_rep in (1, 4, 9, 16, 25):
        draws = rng.normal(0.0, one_reading, size=(2000, n_rep))
        measured = float(draws.mean(axis=1).std(ddof=1))
        print(f"   {n_rep:>5}{measured:>21.6f}{one_reading / np.sqrt(n_rep):>25.6f}")
    print("   -> repeatability improves as 1/sqrt(N); the square root is the tax")
    print("      on every averaging scheme in geophysics.")


if __name__ == "__main__":
    main()
