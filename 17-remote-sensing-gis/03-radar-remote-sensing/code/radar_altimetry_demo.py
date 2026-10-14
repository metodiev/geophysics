#!/usr/bin/env python3
"""Radar altimetry: two-way range, the pulse-limited footprint, the leading edge
and significant wave height, speckle averaging, sea surface height and
geostrophic velocity, tidal aliasing, and ice freeboard to thickness.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radar_altimetry_demo.py

Everything is SYNTHETIC: the orbit height, pulse length, wave heights, sea
surface profiles, repeat cycle, freeboard and densities are teaching values
generated here.  The M2 tidal period is the standard astronomical constant
12.4206012 h; the physical constants (c, g, Omega) are stated standards.
No real mission, product or measured sea surface is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0        # m/s   exact
G_ACC = 9.80665          # m/s^2 standard gravity
OMEGA_EARTH = 7.292_115_0e-5    # rad/s  Earth rotation rate (standard value)
M2_PERIOD_H = 12.4206012        # h  principal lunar semidiurnal constituent


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def leading_edge_width(swh_m, tau_s):
    """10-90 percent width (in metres of range) of a pulse-limited return.

    The flat-surface response is a step convolved with a rectangular pulse of
    length c*tau/2 in range; the rough-surface response convolves that with the
    Gaussian distribution of surface heights, sigma = SWH/4.  The width is
    measured on the synthesised waveform, not taken from a formula.
    """
    sigma = swh_m / 4.0
    dr = 0.005                       # 5 mm range sampling
    span = max(60.0, 20.0 * sigma)   # grid long enough for the widest pdf
    n = int(span / dr)
    r = np.arange(n) * dr
    flat = (r > 0.20 * span).astype(float)
    n_tau = max(1, int(round((C * tau_s / 2.0) / dr)))
    box = np.ones(n_tau) / n_tau
    w_flat = np.convolve(flat, box, mode="same")
    g = np.arange(-10.0 * sigma, 10.0 * sigma, dr)
    pdf = np.exp(-0.5 * (g / sigma) ** 2)
    pdf /= pdf.sum()
    w = np.convolve(w_flat, pdf, mode="same")
    # the plateau must be read in the middle of the window: 'same'-mode
    # convolution truncates the tail, so the last samples under-report
    plateau = w[int(0.50 * n):int(0.85 * n)].mean()
    scan = slice(0, int(0.45 * n))
    i90 = np.argmax(w[scan] > 0.90 * plateau)
    i10 = np.argmax(w[scan] > 0.10 * plateau)
    return (i90 - i10) * dr


def main():
    section("1. Range from the round-trip time")
    print("  r = c t / 2  (the factor 2 is the round trip)\n")
    print("   timing precision   range precision   equivalent in the SSH")
    for dt_ns in (10.0, 1.0, 0.1, 0.01):
        dr = C * dt_ns * 1e-9 / 2.0
        print(f"   {dt_ns:13.2f} ns   {dr*100:11.2f} cm   {dr*100:11.2f} cm")
    print("\n  a 1 ns timing error is 15 cm of range: altimetry is a timing")
    print("  measurement, and the science requires the timing to be understood to")
    print("  a small fraction of a nanosecond.  Averaging helps only because the")
    print("  errors are independent from pulse to pulse (Section 4).")

    section("2. The pulse-limited footprint")
    print("  the leading edge of the return comes from the annulus where the range")
    print("  differs from nadir by less than half the pulse: r^2/(2h) < c tau/2,")
    print("  so r_pl = sqrt(c tau h) and the diameter is twice that.\n")
    print("   pulse (ns)   altitude (km)   footprint radius (m)   area (km^2)")
    for tau_ns in (1.0, 3.0):
        for h_km in (500.0, 800.0, 1300.0):
            h = h_km * 1e3
            r_pl = np.sqrt(C * tau_ns * 1e-9 * h)
            print(f"   {tau_ns:10.1f}   {h_km:13.0f}   {r_pl:20.1f}   "
                  f"{np.pi*r_pl**2/1e6:10.4f}")
    print("\n  note that the footprint is set by the pulse length and the altitude,")
    print("  not by the antenna beam: a short pulse gives a small footprint.  The")
    print("  antenna beam is made wide enough to fill the range window, which is the")
    print("  opposite of the SAR design of lesson 01.")

    section("3. The leading edge and significant wave height")
    print("  a rough surface convolves the flat-pulse return with the distribution of")
    print("  surface heights; for a Gaussian height distribution with standard")
    print("  deviation sigma the 10-90 percent width of a step convolution is")
    print("  2.5628 sigma, and SWH = 4 sigma by definition, so the expected ratio is")
    print(f"  SWH / (2 c t_rise) ... in terms of the measured rise time in range,")
    print("  SWH = 4 sigma and the rise width = 2.5628 sigma = 0.6407 SWH.\n")
    print("   SWH (m)   sigma (m)   measured rise width (m)   ratio width/SWH")
    taus = 1.0e-9
    for swh in (1.0, 2.0, 4.0, 8.0):
        w = leading_edge_width(swh, taus)
        print(f"   {swh:7.1f}   {swh/4:9.3f}   {w:24.4f}   {w/swh:16.4f}")
    print(f"\n  1 ns pulse -> the flat-pulse rise alone contributes "
          f"{C*taus/2:.4f} m;")
    print("  it is negligible against a 1-8 m sea, which is why the simple")
    print("  SWH = rise/0.6407 conversion works and why a calm sea needs the")
    print("  pulse-limited correction back.")
    print("  (The rise time in TIME is the width in range divided by c.)")

    section("4. Speckle averaging: why the height is better than one pulse")
    print("  each pulse illuminates a different set of scatterers, so its range")
    print("  estimate has an independent error; averaging N gives sigma/sqrt(N)\n")
    print("   N pulses   relative height precision   height error for sigma_1 = 45 cm")
    sigma1 = 0.45
    for n_pulse in (1, 10, 100, 1000, 10000):
        print(f"   {n_pulse:8d}   {1/np.sqrt(n_pulse):24.4f}   "
              f"{sigma1/np.sqrt(n_pulse)*100:26.2f} cm")
    print("\n  at 2 kHz the 1 s of averaging that gives N = 2000 pulses needs the")
    print("  waveform samples to be gathered along a short along-track segment, which")
    print("  costs spatial resolution: the footprint becomes a strip, and the")
    print("  resolution/noise trade is the altimeter's version of lesson 01.")

    section("5. Sea surface height and geostrophic velocity")
    lat = 45.0
    f_cor = 2.0 * OMEGA_EARTH * np.sin(np.radians(lat))
    print(f"  Coriolis parameter at {lat:.0f} deg: f = 2 Omega sin(phi) = "
          f"{f_cor:.6e} 1/s")
    print("  geostrophic balance: f u = -g d(SSH)/dy, so u = -(g/f) d(SSH)/dy\n")
    y = np.linspace(-300e3, 300e3, 601)
    ssh = 0.20 * np.exp(-(y ** 2) / (2.0 * 60e3 ** 2)) + 0.02 * y / 300e3
    slope = np.gradient(ssh, y)
    u_geo = -(G_ACC / f_cor) * slope
    print("   SSH anomaly (cm)   max slope          max geostrophic speed (m/s)")
    for scale in (0.5, 1.0, 2.0):
        s2 = scale * ssh
        sl = np.gradient(s2, y)
        u2 = -(G_ACC / f_cor) * sl
        print(f"   {np.ptp(s2)*100:16.2f}   {np.abs(sl).max():17.3e}   "
              f"{np.abs(u2).max():27.3f}")
    print(f"\n  the rule of thumb hidden here: at 45 deg, a slope of 1 cm per 10 km")
    print(f"  (1e-6) gives u = (g/f) x 1e-6 = {G_ACC/f_cor*1e-2/1e4:.4f} m/s, i.e.")
    print("  about 10 cm/s.  That is why")
    print("  altimetry needs centimetre SSH accuracy over tens of kilometres to see a")
    print("  decimetre-per-second current; the measurement is a difference of large")
    print("  numbers, and the large numbers are the orbit and the geoid.")

    section("6. Aliasing of the tides by the repeat cycle")
    print(f"  the principal lunar semidiurnal tide has period {M2_PERIOD_H:.7f} h")
    print("  (standard astronomical value).  A satellite samples a fixed location")
    print("  once per repeat cycle, so the tide is aliased.\n")
    print("   repeat cycle (days)   alias period (days)   alias period (hours)")
    for rep_days in (5.0, 10.0, 20.0, 35.0):
        f_s = 1.0 / (rep_days * 24.0)          # cycles per hour
        f_m2 = 1.0 / M2_PERIOD_H
        n_turns = round(f_m2 / f_s)
        f_alias = abs(f_m2 - n_turns * f_s)
        print(f"   {rep_days:19.1f}   {1.0/f_alias/24.0:20.2f}   "
              f"{1.0/f_alias:20.1f}")
    print("\n  the aliased tide appears as a slow variation that is fully coherent")
    print("  with the sampling, so it does not average away: it must be *modelled*")
    print("  (with a tide model constrained by the same geometry) or removed by a")
    print("  different sampling.  This is aliasing as a design constraint, not a")
    print("  processing nuisance: the repeat cycle chooses which frequencies are")
    print("  observable and which are folded.")

    section("7. Ice freeboard to thickness")
    rho_i, rho_w = 0.917, 1.028      # g/cm^3, teaching density values
    print(f"  hydrostatic equilibrium of a floating slab: T = F rho_w/(rho_w - rho_i)")
    print(f"  with rho_i = {rho_i:.3f} and rho_w = {rho_w:.3f} g/cm^3, so")
    print(f"  T = {rho_w/(rho_w-rho_i):.4f} F: one metre of freeboard is "
          f"{rho_w/(rho_w-rho_i):.4f} m of ice.\n")
    print("   freeboard (m)   thickness (m)")
    for fb in (0.1, 0.25, 0.5, 1.0):
        print(f"   {fb:13.2f}   {fb*rho_w/(rho_w-rho_i):13.4f}")
    dens = rho_w - rho_i
    dtdrho_i = 0.5 * rho_w / dens ** 2      # m of thickness per (g/cm^3) at F = 0.5 m
    print(f"\n  the sensitivity to the density assumption is the whole difficulty.")
    print(f"  The difference rho_w - rho_i = {dens:.3f} g/cm^3 is small, so the")
    print(f"  derivative is large: for F = 0.5 m, dT/d(rho_i) = {dtdrho_i:.2f} m per")
    print(f"  (g/cm^3).  A density error of 0.001 g/cm^3 therefore moves the thickness")
    print(f"  by {dtdrho_i*0.001*100:.2f} cm, i.e. {dtdrho_i*0.001/ (0.5*rho_w/dens)*100:.2f}% of a "
          f"{0.5*rho_w/dens:.3f} m answer.")
    print("  The freeboard is measured to centimetres while the thickness is")
    print("  quoted in metres.  Also: the freeboard is a *range* difference between")
    print("  the ice and the nearby open water, so it inherits both surfaces' errors,")
    print("  plus the question of whether the radar penetrated the snow layer.  All")
    print("  of these are assumptions, and none is resolved by more averaging.")


if __name__ == "__main__":
    main()
