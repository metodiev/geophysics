#!/usr/bin/env python3
"""Seismic network design arithmetic: detection capability, location geometry,
array resolution and spatial aliasing, on SYNTHETIC parameters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_network_design_demo.py

Everything here is SYNTHETIC.  The detection probabilities, magnitudes, network
geometries, velocity, pick uncertainty and sensor spacing are chosen teaching
values.  No real network, catalogue completeness estimate or array response is
used or reproduced.

Sections
--------
1. Detection capability versus magnitude for an N-station network.
2. Location geometry: the azimuthal gap and the horizontal error ellipse.
3. Array resolution: main-lobe width and peak sidelobe of two geometries.
4. Station spacing and spatial aliasing.
"""

import numpy as np
from math import comb

RNG = np.random.default_rng(20261014)

N_STATIONS = 8
DETECT_MIN = 4            # detections required to declare an event
M50 = 1.2                 # magnitude of 50 % single-station detection (chosen)
M_SLOPE = 0.25            # logistic width in magnitude units (chosen)
VELOCITY_KM_S = 6.0       # crustal velocity for the location model (chosen)
SIGMA_PICK_S = 0.05       # arrival-time uncertainty (chosen)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def p_single(m):
    """SYNTHETIC single-station detection probability, a logistic in magnitude."""
    return 1.0 / (1.0 + np.exp(-(m - M50) / M_SLOPE))


def p_network(m, n=N_STATIONS, k=DETECT_MIN):
    """Probability of at least k detections out of n stations."""
    p = p_single(m)
    return sum(comb(n, j) * p ** j * (1.0 - p) ** (n - j) for j in range(k, n + 1))


def solve_magnitude(target, lo=-1.0, hi=4.0):
    """Bisection for the magnitude at which the network detection probability is target."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if p_network(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def azimuth_gap(stations):
    """Largest gap in azimuth, degrees, for stations around the origin."""
    az = np.degrees(np.arctan2(stations[:, 1], stations[:, 0])) % 360.0
    az = np.sort(az)
    gaps = np.diff(np.concatenate([az, [az[0] + 360.0]]))
    return float(gaps.max())


def location_ellipse(stations):
    """68 % horizontal error ellipse from the linearised location problem."""
    dist = np.linalg.norm(stations, axis=1)
    gx = -stations[:, 0] / (VELOCITY_KM_S * dist)
    gy = -stations[:, 1] / (VELOCITY_KM_S * dist)
    g = np.column_stack([gx, gy, np.ones(stations.shape[0])])
    cov = SIGMA_PICK_S ** 2 * np.linalg.inv(g.T @ g)
    sub = cov[:2, :2]
    values, vectors = np.linalg.eigh(sub)
    semi = np.sqrt(values)
    major_direction = vectors[:, int(np.argmax(values))]
    major_az = np.degrees(np.arctan2(major_direction[1], major_direction[0])) % 180.0
    sigma_h = np.sqrt(cov[0, 0] + cov[1, 1])
    area95 = np.pi * 5.991 * np.sqrt(np.prod(values))
    return sigma_h, semi.max(), semi.min(), major_az, area95


def ring_array(n, radius_m):
    angle = 2.0 * np.pi * np.arange(n) / n
    return np.column_stack([radius_m * np.cos(angle), radius_m * np.sin(angle)])


def grid_array(nx, ny, spacing_m):
    x, y = np.meshgrid((np.arange(nx) - (nx - 1) / 2.0) * spacing_m,
                       (np.arange(ny) - (ny - 1) / 2.0) * spacing_m)
    return np.column_stack([x.ravel(), y.ravel()])


def array_response(geometry, frequency, dsx, dsy):
    """Beam response to a slowness offset (dsx, dsy), normalised to 1 at the peak."""
    phase = -2j * np.pi * frequency * (dsx * geometry[:, 0] + dsy * geometry[:, 1])
    return np.abs(np.exp(phase).mean())


def main():
    section("1. Detection capability versus magnitude")
    print(f"  {N_STATIONS} stations, {DETECT_MIN} detections required; single-station")
    print(f"  detection is a logistic with M50 = {M50:.2f} and width "
          f"{M_SLOPE:.2f} magnitude units (chosen)")
    print(f"  {'magnitude':>10s} {'p(1 station)':>13s} {'expected detections':>20s}"
          f" {'P(>= 4)':>10s}")
    for m in (0.0, 0.5, 1.0, 1.2, 1.5, 2.0, 2.5):
        p = p_single(m)
        print(f"  {m:10.1f} {p:13.4f} {N_STATIONS * p:20.2f} "
              f"{p_network(m):10.4f}")
    for target in (0.50, 0.90, 0.99):
        print(f"  magnitude of completeness at P = {target:.2f}: "
              f"{solve_magnitude(target):.3f}")
    print("  -> the completeness magnitude rises with the detection threshold")
    print("     because it is a statement about the NETWORK, not the station.")

    section("2. Location geometry: azimuthal gap and error ellipse")
    clustered = np.array([[18.0, 11.0], [18.6, 10.7], [19.2, 10.4], [19.8, 10.1],
                          [20.4, 9.8], [21.0, 9.5], [21.6, 9.2], [22.2, 8.9]])
    ring = ring_array(8, 20_000.0) / 1000.0
    print(f"  velocity = {VELOCITY_KM_S:.1f} km/s, pick uncertainty = "
          f"{SIGMA_PICK_S:.2f} s, source at the origin")
    print(f"  {'geometry':<22s} {'gap (deg)':>10s} {'sigma_h (km)':>13s}"
          f" {'a (km)':>9s} {'b (km)':>9s} {'azimuth (deg)':>14s}"
          f" {'95 % area (km^2)':>18s}")
    for label, stations in (("along an access road", clustered),
                            ("even ring, 20 km", ring)):
        sigma_h, a, b, az, area = location_ellipse(stations)
        print(f"  {label:<22s} {azimuth_gap(stations):10.1f} {sigma_h:13.3f} "
              f"{a:9.3f} {b:9.3f} {az:14.1f} {area:18.1f}")
    print(f"  closed form for a full ring: sigma_h = 2 V sigma_t / sqrt(N) = "
          f"{2 * VELOCITY_KM_S * SIGMA_PICK_S / np.sqrt(8):.3f} km")
    print("  -> an access-limited deployment concentrates azimuth, and the")
    print("     location error ellipse lengthens across the unobserved directions.")

    section("3. Array resolution: ring versus grid geometry")
    freq = np.array([0.5, 1.0, 2.0])
    radius = 500.0
    print(f"  ring array: 12 sensors on a radius of {radius:.0f} m")
    print("  theoretical first zero of the ring response: ds = 2.405/(2 pi f R)")
    print(f"  {'f (Hz)':>8s} {'ds (s/m)':>12s} {'ds (s/km)':>12s}")
    for f in freq:
        ds = 2.405 / (2.0 * np.pi * f * radius)
        print(f"  {f:8.2f} {ds:12.3e} {ds * 1000.0:12.3f}")
    ring12 = ring_array(12, radius)
    grid16 = grid_array(4, 4, 180.0)
    grid16b = grid_array(4, 4, 700.0)
    f_cut = 1.0
    v_min = 500.0
    s_limit = 1.0 / v_min
    ds = np.linspace(0.0, 0.006, 60001)
    print(f"  response cut along the x axis of slowness at f = {f_cut:.0f} Hz; "
          f"physical slowness limit for V_min = {v_min:.0f} m/s is "
          f"{s_limit * 1000.0:.2f} s/km")
    print(f"  {'geometry':<22s} {'main lobe (s/km)':>17s} {'first sidelobe (dB)':>20s}"
          f" {'peak in band (dB)':>19s} {'aliased?':>10s}")
    for label, geom in (("ring, 12 at 500 m", ring12),
                        ("grid, 4x4 at 180 m", grid16),
                        ("grid, 4x4 at 700 m", grid16b)):
        r = np.abs(np.exp(-2j * np.pi * f_cut * (ds[:, None] * geom[:, 0])).mean(axis=1))
        null_index = int(np.argmax(r < 0.05))
        width_half = ds[null_index]
        window = (ds > width_half) & (ds <= 3.0 * width_half)
        first_sidelobe = r[window].max() if window.any() else np.nan
        in_band = (ds > width_half) & (ds <= s_limit)
        peak_in_band = r[in_band].max() if in_band.any() else np.nan
        aliased = (not np.isnan(peak_in_band)) and peak_in_band > 0.5
        print(f"  {label:<22s} {2.0 * width_half * 1000.0:17.3f} "
              f"{20.0 * np.log10(first_sidelobe):20.1f} "
              f"{20.0 * np.log10(peak_in_band):19.1f} "
              f"{('yes' if aliased else 'no'):>10s}")
    print("  (aliased: a repeat of the main lobe exceeding half amplitude lies")
    print("   inside the reachable slowness range |s| <= 1/V_min)")
    print("  -> a ring suppresses sidelobes but has a broad, Bessel-shaped main")
    print("     lobe; a grid is sharper but repeats at 1/(f dx), and the repeat")
    print("     is harmless only while it lies outside the physical range.  The")
    print("     same 700 m grid is alias-free where V_min is high and aliased")
    print("     where it is low: the site sets the requirement, not the array.")

    section("4. Station spacing and spatial aliasing")
    print(f"  {'dx (m)':>8s} {'V_min (m/s)':>12s} {'f_max (Hz)':>11s}"
          f" {'k_Nyq (rad/m)':>14s}")
    for dx, v in ((25.0, 500.0), (25.0, 1500.0), (100.0, 1000.0),
                  (100.0, 3000.0), (250.0, 3000.0)):
        print(f"  {dx:8.0f} {v:12.0f} {v / (2.0 * dx):11.1f} "
              f"{np.pi / dx:14.5f}")
    print("  f_max = V_min/(2 dx); above it the apparent velocity of a wave is")
    print("  aliased to a slower, wrong value.  The site's LOWEST surface")
    print("  velocity sets the requirement, not the average.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain a design model, not any real network.")


if __name__ == "__main__":
    main()
