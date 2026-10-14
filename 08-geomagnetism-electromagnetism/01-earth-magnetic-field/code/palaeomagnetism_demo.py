#!/usr/bin/env python3
"""Palaeomagnetism: Fisher statistics on directions, inclination to
palaeolatitude, virtual geomagnetic poles and a synthetic reversal chronology.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python palaeomagnetism_demo.py

Everything here is SYNTHETIC.  The directions, poles and polarity sequence come
from a seeded random generator; no real site, core, section or published
polarity timescale is used.  The only standard values are the Earth radius
6371 km and the 11.5 deg dipole tilt.

Contents
--------
1. Fisher statistics on a set of synthetic directions, and the bias in k_hat.
2. Inclination to palaeolatitude, and the error it inherits from I.
3. Virtual geomagnetic poles from a site position and direction.
4. Accuracy versus number of sites: how a95 shrinks.
5. A synthetic reversal chronology and the reversal rate in windows.
6. How many reversals make a polarity pattern unique.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A_EARTH_KM = 6371.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def dir_to_vec(dec, inc):
    """(D, I) in degrees -> unit vector components (north, east, down)."""
    D = np.radians(dec)
    I = np.radians(inc)
    return np.stack([np.cos(I) * np.cos(D), np.cos(I) * np.sin(D), np.sin(I)])


def vec_to_dir(v):
    """Unit vector -> (D in [0,360), I) in degrees."""
    v = v / np.linalg.norm(v, axis=0)
    dec = np.degrees(np.arctan2(v[1], v[0])) % 360.0
    inc = np.degrees(np.arcsin(np.clip(v[2], -1.0, 1.0)))
    return dec, inc


def fisher_sample(dec0, inc0, kappa, size, rng):
    """Exact Fisher (1953) sampling about the mean direction (dec0, inc0)."""
    v0 = dir_to_vec(dec0, inc0)
    # an orthonormal basis of the plane perpendicular to v0
    tmp = np.array([0.0, 0.0, 1.0])
    a = np.cross(v0, tmp)
    a = a / np.linalg.norm(a)
    b = np.cross(v0, a)
    u = rng.random(size)
    cos_th = 1.0 + np.log(1.0 - u * (1.0 - np.exp(-2.0 * kappa))) / kappa
    cos_th = np.clip(cos_th, -1.0, 1.0)
    th = np.arccos(cos_th)
    psi = rng.random(size) * 2.0 * np.pi
    v = (np.cos(th) * v0[:, None]
         + np.sin(th) * (np.cos(psi) * a[:, None] + np.sin(psi) * b[:, None]))
    return vec_to_dir(v)


def fisher_mean(dec, inc):
    """Fisher (1953) mean direction plus R (resultant length), k_hat, alpha95.

    R is the LENGTH of the vector sum, not the mean unit vector, because the
    standard estimators use R directly:
        k_hat  = (n - 1) / (n - R)
        alpha95 = arccos[1 - (n - R)/R ((1/0.05)^(1/(n-1)) - 1)].
    """
    v = dir_to_vec(dec, inc)
    n = v.shape[1]
    R = float(np.linalg.norm(v.sum(axis=1)))
    k_hat = (n - 1.0) / (n - R)
    arg = 1.0 - (n - R) / R * ((1.0 / 0.05) ** (1.0 / (n - 1)) - 1.0)
    a95 = np.degrees(np.arccos(np.clip(arg, -1.0, 1.0)))
    return (*vec_to_dir(v.sum(axis=1)), R, k_hat, a95)


def main():
    section("1. Fisher statistics on synthetic directions")
    kappa_true, n = 30.0, 24
    dec, inc = fisher_sample(12.0, 48.0, kappa_true, n, RNG)
    Dm, Im, R, k_hat, a95 = fisher_mean(dec, inc)
    print(f"SYNTHETIC data: {n} directions drawn from a Fisher distribution with")
    print(f"true mean D = 12.000 deg, I = 48.000 deg, precision kappa = "
          f"{kappa_true:.1f}")
    print(f"  estimated mean direction: D = {Dm:.4f} deg, I = {Im:.4f} deg")
    print(f"  resultant length R = {R:.6f} (out of n = {n})")
    print(f"  precision k_hat = (n-1)/(n-R) = {k_hat:.4f}")
    print(f"  radius of the 95% confidence cone alpha95 = {a95:.4f} deg")
    print(f"  mean within alpha95 of the true mean? "
          f"{np.degrees(np.arccos(np.clip(np.dot(dir_to_vec(Dm,Im), dir_to_vec(12.0,48.0)),-1,1))) <= a95}")
    khats, a95s = [], []
    for _ in range(400):
        d2, i2 = fisher_sample(12.0, 48.0, kappa_true, n, RNG)
        _, _, _, kh, a = fisher_mean(d2, i2)
        khats.append(kh); a95s.append(a)
    print(f"  Monte Carlo over 400 samples of n = {n}:")
    print(f"    k_hat: median {np.median(khats):.3f}, 5-95% range "
          f"{np.percentile(khats,5):.3f} to {np.percentile(khats,95):.3f}")
    print(f"    alpha95: median {np.median(a95s):.3f} deg, 5-95% range "
          f"{np.percentile(a95s,5):.3f} to {np.percentile(a95s,95):.3f}")
    print("  k_hat is noisy and skewed: a single sample can fall well below or")
    print("  above the true precision.  alpha95 states the same information as an")
    print("  interval, which is why it is the number to report.")

    section("2. Inclination to palaeolatitude, and its error")
    print("  dipole relation inverted: latitude = atan(tan(I)/2)")
    print("  I (deg)   palaeolatitude (deg)   shift for dI = +5 deg (deg)")
    for I in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 85.0):
        lat = np.degrees(np.arctan(0.5 * np.tan(np.radians(I))))
        latp = np.degrees(np.arctan(0.5 * np.tan(np.radians(I + 5.0))))
        print(f"  {I:6.1f}   {lat:21.4f}   {latp-lat:28.4f}")
    print("  the mapping is strongly non-linear: a 5 deg inclination error moves")
    print("  a polar palaeolatitude by tens of degrees and an equatorial one by")
    print("  a few.  Sites with low inclination are therefore the best")
    print("  constrained, and polar sites the worst.")

    section("3. Virtual geomagnetic poles")
    site_lat, site_lon = 42.0, -18.0
    D_site, I_site = 14.5, 52.0
    colat_p = np.degrees(np.arctan2(2.0, np.tan(np.radians(I_site))))
    print(f"SYNTHETIC site at lat = {site_lat:.1f}, lon = {site_lon:.1f} with "
          f"D = {D_site:.1f}, I = {I_site:.1f}")
    print(f"  magnetic colatitude p = atan(2/tan I) = {colat_p:.4f} deg")
    lat_s = np.radians(site_lat)
    p = np.radians(colat_p)
    d = np.radians(D_site)
    # standard VGP construction: travel a distance p from the site along the
    # great circle whose initial azimuth is the declination D
    pole_lat = np.degrees(np.arcsin(np.sin(lat_s) * np.cos(p)
                                    + np.cos(lat_s) * np.sin(p) * np.cos(d)))
    pole_lon = site_lon + np.degrees(np.arctan2(
        np.sin(p) * np.sin(d),
        np.cos(lat_s) * np.cos(p) - np.sin(lat_s) * np.sin(p) * np.cos(d)))
    pole_lon = (pole_lon + 180.0) % 360.0 - 180.0
    print(f"  virtual geomagnetic pole: lat = {pole_lat:.4f} deg, "
          f"lon = {pole_lon:.4f} deg")
    print(f"  angular distance from the geographic pole = "
          f"{90.0 - abs(pole_lat):.4f} deg")
    d2 = np.radians(D_site + 10.0)
    pole_lat2 = np.degrees(np.arcsin(np.sin(lat_s) * np.cos(p)
                                     + np.cos(lat_s) * np.sin(p) * np.cos(d2)))
    print(f"  a +10 deg error in D moves the VGP latitude by "
          f"{pole_lat2 - pole_lat:+.4f} deg")
    print("  the VGP is an axis position inferred from one site, so it inherits")
    print("  the site error and the assumption of a geocentric dipole field.")

    section("4. How alpha95 shrinks with the number of sites")
    print("  n sites   median alpha95 (deg)   median k_hat")
    medians = {}
    for nsite in (5, 10, 24, 50, 100, 400):
        a95s, ks = [], []
        for _ in range(200):
            d3, i3 = fisher_sample(12.0, 48.0, 30.0, nsite, RNG)
            _, _, _, kh, a = fisher_mean(d3, i3)
            a95s.append(a); ks.append(kh)
        medians[nsite] = float(np.median(a95s))
        print(f"  {nsite:7d}   {np.median(a95s):16.4f}   {np.median(ks):12.3f}")
    print(f"  alpha95 falls from {medians[5]:.3f} deg at n = 5 to "
          f"{medians[400]:.3f} deg at n = 400,")
    print(f"  a factor of {medians[5]/medians[400]:.2f} for an n-ratio of "
          f"{400/5:.0f} (1/sqrt(n) predicts {np.sqrt(400/5):.2f}).")

    section("5. A synthetic reversal chronology")
    mean_interval_myr, total_myr = 0.22, 10.0
    intervals = RNG.exponential(mean_interval_myr, 400)
    times = np.cumsum(intervals)
    times = times[times < total_myr]
    print(f"SYNTHETIC chronology: exponential intervals with mean "
          f"{mean_interval_myr:.2f} Myr, span {total_myr:.1f} Myr")
    kept_intervals = np.diff(np.concatenate(([0.0], times)))
    print(f"  {len(times)} reversals; mean interval between them "
          f"{kept_intervals.mean():.4f} Myr; rate "
          f"{len(times)/total_myr:.3f} per Myr")
    print("  rate estimated in 2 Myr windows:")
    for lo in np.arange(0.0, total_myr, 2.0):
        cnt = int(np.sum((times >= lo) & (times < lo + 2.0)))
        print(f"    {lo:4.1f}-{lo+2.0:4.1f} Myr: {cnt:2d} reversals -> "
              f"{cnt/2.0:.2f} per Myr")
    print("  the window rates differ by a factor of two or more, so a single")
    print("  window rate is a noisy estimate of any long-term rate; exponential")
    print("  intervals are also consistent with the absence of periodicity")
    print("  (autocorrelation of the interval series = "
          f"{np.corrcoef(intervals[:-1], intervals[1:])[0,1]:+.4f}).")

    section("6. How many reversals make a polarity pattern unique?")
    print("  chance that a random polarity sequence matches a given one:")
    for nrev in (4, 6, 8, 10, 12):
        print(f"    n = {nrev:2d} intervals: 2^-n = {2.0**-nrev:.3e}")
    print("  a section with 10 or more reversals is effectively unique; one with")
    print("  three or four is not, and a correlation built on them is a")
    print("  coincidence until an independent date fixes it.")


if __name__ == "__main__":
    main()
