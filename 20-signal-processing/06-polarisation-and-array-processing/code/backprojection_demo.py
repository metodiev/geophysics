#!/usr/bin/env python3
"""Back-projection imaging of a SYNTHETIC rupture with a local surface array.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python backprojection_demo.py

Everything here is SYNTHETIC.  The fault, the rupture, the records and the
noise are generated in this file; no real earthquake, station or waveform is
used and no published number is quoted.

Sections
--------
1. The rupture model and the synthetic array records.
2. The back-projection image: recover the rupture velocity from the ridge.
3. Resolution: the array point-spread function and the rupture image width.
4. Sensitivity to the velocity model: location bias from a wrong model.
5. What back-projection actually resolves: a whole-fault instantaneous source.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 6.0            # crustal wave speed, km/s used to make the data
H = 30.0           # fault depth below the array centre line, km
VR = 2.5           # true rupture velocity, km/s
SIGMA = 0.2        # source pulse half-width, s (high-frequency radiation)
L = 40.0           # fault length, km
DT = 0.02          # sampling interval, s
NT = 1300          # samples (26 s)

XI = np.arange(0.0, L + 0.001, 1.0)          # fault grid, km
XS = np.linspace(-20.0, 20.0, 20)            # station positions, km
TAU_GRID = np.arange(-2.0, 22.0001, 0.05)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def travel_time(xi, xs):
    """Travel time from fault point xi (km) to station xs (km), in seconds."""
    return np.sqrt((xi - xs) ** 2 + H ** 2) / C


def synth_array(t, rupture_time, stations=XS, sigma=SIGMA):
    """Synthetic records (n_stations, nt); rupture_time gives when each xi fires."""
    out = np.empty((stations.size, t.size))
    for i, xs in enumerate(stations):
        acc = np.zeros_like(t)
        for xi, tt0 in zip(XI, rupture_time):
            if not np.isfinite(tt0):
                continue
            acc += np.exp(-((t - tt0 - travel_time(xi, xs)) / sigma) ** 2)
        out[i] = acc
    return out


def backproject(records, t, c_model, xi_grid, tau_grid, stations=XS):
    """Image I(xi, tau) by stacking records along predicted travel-time curves."""
    img = np.zeros((xi_grid.size, tau_grid.size))
    for a, xi in enumerate(xi_grid):
        for i, xs in enumerate(stations):
            delay = tau_grid + np.sqrt((xi - xs) ** 2 + H ** 2) / c_model
            img[a] += np.interp(delay, t, records[i], left=0.0, right=0.0)
    return img


def point_source(t, xi0, tau0, stations=XS, sigma=SIGMA):
    """Records for a single point on the fault firing at time tau0."""
    rr = np.full(XI.shape, np.nan)
    rr[int(np.argmin(np.abs(XI - xi0)))] = tau0
    return synth_array(t, rr, stations=stations, sigma=sigma)


def psf_width(t, xi_grid, aperture, n_sta=20):
    """Half-width in xi of the image of a point source, for a given aperture."""
    stations = np.linspace(-aperture / 2.0, aperture / 2.0, n_sta)
    rec = point_source(t, 0.0, 0.0, stations=stations)
    taus = np.arange(-1.0, 6.0001, 0.05)
    img = backproject(rec, t, C, xi_grid, taus, stations=stations)
    prof = img.max(axis=1)
    prof /= prof.max()
    above = np.where(prof > 0.5)[0]
    return xi_grid[above[-1]] - xi_grid[above[0]]


def main():
    t = np.arange(NT) * DT
    xi_grid = np.arange(0.0, L + 0.001, 1.0)

    section("1. The rupture model and the synthetic array records")
    rupture_time = XI / VR                  # hypocentre at xi = 0, t = 0
    records = synth_array(t, rupture_time)
    noise = 0.05 * records.std() * RNG.standard_normal(records.shape)
    noisy = records + noise
    print(f"  SYNTHETIC: line fault 0-{L:.0f} km at {H:.0f} km depth, "
          f"c = {C:.1f} km/s")
    print(f"  rupture velocity {VR:.2f} km/s; source pulse sigma = {SIGMA:.2f} s; "
          f"rupture duration {rupture_time[-1]:.1f} s")
    print(f"  array: {XS.size} stations on a line from {XS[0]:.0f} to "
          f"{XS[-1]:.0f} km (aperture {XS[-1] - XS[0]:.0f} km)")
    print(f"  records: {NT} samples at {1 / DT:.0f} Hz; noise 5% of signal rms")
    print(f"  first arrival at the array centre = "
          f"{travel_time(0.0, 0.0):.2f} s; last arrival = "
          f"{rupture_time[-1] + travel_time(L, 0.0):.2f} s")
    print(f"  pulse spacing along the fault = 1 km / {VR:.1f} km/s = "
          f"{1.0 / VR:.2f} s, wider than sigma = {SIGMA:.2f} s, so the sub-events")
    print("  are individually radiated.  Back-projection needs that: a continuous")
    print("  smear of overlapping pulses has no times to back-project.")

    section("2. The back-projection image: rupture velocity from the ridge")
    img = backproject(noisy, t, C, xi_grid, TAU_GRID)
    img /= img.max()
    ridge = TAU_GRID[np.argmax(img, axis=1)]
    sel = (xi_grid > 4.0) & (xi_grid < 36.0)
    slope = np.polyfit(xi_grid[sel], ridge[sel], 1)[0]
    print(f"  image grid {xi_grid.size} x {TAU_GRID.size}; peak normalised to 1")
    print("     xi (km)     6     12     18     24     30     36")
    print("     tau peak  " + "  ".join(
        f"{ridge[np.argmin(np.abs(xi_grid - v))]:5.2f}"
        for v in (6, 12, 18, 24, 30, 36)))
    print("     expected  " + "  ".join(
        f"{v / VR:5.2f}" for v in (6, 12, 18, 24, 30, 36)))
    print(f"  fitted ridge slope d(tau)/d(xi) = {slope:.4f} s/km "
          f"(true 1/vr = {1.0 / VR:.4f})")
    print(f"  recovered rupture velocity = {1.0 / slope:.3f} km/s "
          f"(true {VR:.2f}); error {100 * abs(1 / slope - VR) / VR:.1f}%")
    print("  -> the diagonal ridge IS the rupture: each fault point radiates when")
    print("     the front reaches it, and the ridge slope is the inverse rupture")
    print("     velocity.  Back-projection measures WHEN a place radiates.")

    section("3. Resolution: the array point-spread function")
    psf_img = backproject(point_source(t, 0.0, 0.0), t, C, xi_grid,
                          np.arange(-1.0, 6.0001, 0.05))
    prof = psf_img.max(axis=1)
    prof /= prof.max()
    above = np.where(prof > 0.5)[0]
    psf_w = xi_grid[above[-1]] - xi_grid[above[0]]
    tau_col = np.arange(-1.0, 6.0001, 0.05)
    tau_prof = psf_img[:, np.argmax(psf_img.max(axis=1))]
    ta = np.where(tau_prof > 0.5 * tau_prof.max())[0]
    row = img[:, np.argmin(np.abs(TAU_GRID - 8.0))]
    ra = np.where(row > 0.5)[0]
    print(f"  a POINT sub-event under the 40 km array images as a peak of")
    print(f"  half-width {psf_w:.1f} km along strike and "
          f"{tau_col[ta[-1]] - tau_col[ta[0]]:.2f} s in origin time.")
    print("  The width is the array point-spread function; the 1 km fault grid")
    print("  is not the limit.  Half-width versus aperture (20 stations each):")
    print("     aperture (km)   10    20    40    60    80")
    print("     PSF width (km)  " + "  ".join(
        f"{psf_width(t, xi_grid, ap):4.0f}" for ap in (10, 20, 40, 60, 80)))
    print("  -> the image is the true source convolved with the array")
    print("     point-spread function, and the point-spread width falls with")
    print("     aperture exactly as the slowness resolution of lesson 20-06-03.")
    print("     A rupture shorter than that width cannot be resolved, however")
    print("     strong the data.")

    section("4. Sensitivity to the velocity model")
    pt = point_source(t, 20.0, 8.0)
    print("  a sub-event at xi = 20 km firing at tau = 8.0 s, imaged with")
    print("  different assumed speeds:")
    print("     c model (km/s)   imaged xi (km)   imaged tau (s)   bias in xi (km)")
    for c_model in (6.0, 5.7, 5.4, 6.3):
        im = backproject(pt, t, c_model, xi_grid, TAU_GRID)
        a, b = np.unravel_index(np.argmax(im), im.shape)
        print(f"     {c_model:14.1f}   {xi_grid[a]:14.0f}   "
              f"{TAU_GRID[b]:15.2f}   {xi_grid[a] - 20.0:+14.0f}")
    print("  -> back-projection does not invert for velocity: it PRESUMES one.")
    print("     Here a 5% too-slow model (5.7 km/s) shifts the image by 1 km at")
    print("     20 km from the array centre; the bias grows with distance from")
    print("     the part of the fault that is well sampled.  A back-projection")
    print("     location is only as good as the travel-time model behind it.")

    section("5. What back-projection resolves: a whole-fault instantaneous source")
    instant = synth_array(t, np.zeros_like(XI))
    im_inst = backproject(instant, t, C, xi_grid, np.arange(-1.0, 6.0001, 0.05))
    prof_i = im_inst.max(axis=1)
    prof_i /= prof_i.max()
    ai = np.where(prof_i > 0.5)[0]
    print(f"  a source firing the SAME pulse from the whole fault at t = 0 gives")
    print(f"  an image whose 50% extent along strike is "
          f"{xi_grid[ai[-1]] - xi_grid[ai[0]]:.1f} km")
    print(f"  the point source under the array gives {psf_w:.1f} km")
    print("  -> with no propagation delay along the fault to exploit, the image")
    print("     collapses to the array response plus the fault extent: a source")
    print("     distributed in space and time can resemble a different one.  That")
    print("     ambiguity between rupture propagation and a spatially extended")
    print("     simultaneous source is the honest limit of the method.")


if __name__ == "__main__":
    main()
