#!/usr/bin/env python3
"""InSAR atmospheric and orbital error: the delay-to-displacement equivalence,
a synthetic stratified screen and its correction, turbulence with a measured
structure function, orbital ramps, and how stacking does or does not average
a screen down.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_atmospheric_correction_demo.py

Everything is SYNTHETIC: the atmosphere is an exponential teaching profile, the
screens, ramps, DEM and noise are generated here, and no weather model, orbit
product or measurement is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0        # m/s
LAM = C / 5.300e9        # m     teaching carrier
COS_INC = np.cos(np.radians(35.0))


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def power_law_field(n, beta):
    """1-D periodic random field with spectral density ~ k^-beta."""
    kk = np.abs(2.0 * np.pi * np.fft.fftfreq(n))
    amp = np.zeros(n)
    ok = kk > 1e-12
    amp[ok] = kk[ok] ** (-beta / 2.0)
    amp[0] = 0.0
    spec = (RNG.standard_normal(n) + 1j * RNG.standard_normal(n)) * amp
    f = np.real(np.fft.ifft(spec))
    return f / f.std()


def band_limited_field(n, beta, k_min, k_max):
    """Random field with a power-law spectrum only between k_min and k_max.

    The band edges create the inertial subrange in which D(r) ~ r^(beta-1):
    below 1/k_max there is no power, above 1/k_min the structure function
    saturates at twice the variance.
    """
    kk = np.abs(2.0 * np.pi * np.fft.fftfreq(n))
    amp = np.where((kk >= k_min) & (kk <= k_max), kk ** (-beta / 2.0), 0.0)
    spec = (RNG.standard_normal(n) + 1j * RNG.standard_normal(n)) * amp
    f = np.real(np.fft.ifft(spec))
    return f / f.std()


def structure_function(f, separations):
    d = []
    for s in separations:
        diff = f[s:] - f[:-s]
        d.append(np.mean(diff ** 2))
    return np.array(d)


def main():
    section("1. The zenith delay from a synthetic atmosphere")
    print("  refractivity N [ppm] with N = 1e6 (n - 1); a teaching profile")
    print("  N(z) = N_s exp(-z / H) with N_s = 315 ppm and H = 8.0 km\n")
    n_s, scale_h = 315.0, 8000.0
    z = np.arange(0.0, 40000.0, 10.0)
    n_prof = n_s * np.exp(-z / scale_h)
    zhd = 1e-6 * np.trapezoid(n_prof, z)
    print(f"    zenith delay  = 1e-6 * integral N dz = {zhd:.4f} m (truncated at 40 km)")
    print(f"    analytically  = 1e-6 * N_s * H          = "
          f"{1e-6 * n_s * scale_h:.4f} m")
    print(f"    effective excess path at 35 deg        = "
          f"{zhd / np.cos(np.radians(35.0)):.4f} m (planar mapping 1/cos z)")
    print("\n  a two-metre path delay is enormous compared with a wavelength, but it is")
    print("  nearly identical in both acquisitions: interferometry measures the")
    print("  DIFFERENCE, which is of order centimetres.")

    section("2. Delay to apparent displacement: the conversion to memorise")
    print("  phase = 4 pi * (excess path) / lam, for a one-way differential delay\n")
    print("   differential delay   phase (rad)   fringes   apparent LOS (cm)")
    for l_mm in (1.0, 5.0, 10.0, 20.0):
        l_m = l_mm / 1000.0
        ph = 4.0 * np.pi * l_m / LAM
        print(f"   {l_mm:16.1f} mm   {ph:11.4f}   {ph/(2*np.pi):8.4f}   "
              f"{l_m*100:18.4f}")
    print("\n  the conversion is one-to-one: 1 cm of differential delay is 1 cm of")
    print("  apparent line-of-sight displacement, 0.354 of a fringe, 2.2216 rad.")
    print("  In a single interferogram a delay and a displacement are the same")
    print("  number, so separating them requires information beyond the pair.")

    section("3. A stratified screen and its correction by regression on elevation")
    n_x = 128
    x = np.arange(n_x) * 30.0
    dem = 400.0 + 1600.0 * np.exp(-((x - 6000.0) / 1800.0) ** 2) \
        + 150.0 * power_law_field(n_x, beta=3.5)
    print("  teaching relation: delay = 3.00*(h/1 km) - 0.25*(h/1 km)^2 mm, i.e. a")
    print("  linear part of 3.0 mm/km with the curvature a real pressure profile has")
    coef = 3.0        # mm/km
    screen = coef * (dem / 1000.0) - 0.25 * coef * (dem / 1000.0) ** 2   # mm
    print(f"  DEM range {dem.min():.0f} to {dem.max():.0f} m -> screen range "
          f"{screen.min():.2f} to {screen.max():.2f} mm")
    print(f"  induced apparent displacement: {np.ptp(screen)/10:.3f} cm peak to peak")
    resid_uncorr = screen - screen.mean()
    fit = np.polyfit(dem, screen, 1)
    resid_corr = screen - np.polyval(fit, dem)
    print(f"\n  linear fit to the screen against elevation: slope "
          f"{fit[0]*1000:.4f} mm/km")
    print(f"  residual rms before correction: "
          f"{np.sqrt(np.mean(resid_uncorr**2)):.4f} mm")
    print(f"  residual rms after  correction: "
          f"{np.sqrt(np.mean(resid_corr**2)):.4f} mm")
    print("  a linear regression removes the stratified part only if the true")
    print("  relation is linear in elevation; the residual is what the fit cannot")
    print("  express, and it does not shrink by adding more points, only by a better")
    print("  model or an independent measurement of the delay.")

    section("4. Turbulence: the structure function and its power law")
    print("  a synthetic screen with one-dimensional spectral density ~ k^-beta over")
    print("  the band k in [0.0005, 0.25] rad/sample.  The structure function")
    print("    D(r) = <(x(r+r0) - x(r0))^2>")
    print("  scales as D ~ r^(beta-1) for beta < 3 and as D ~ r^2 for beta >= 3, the")
    print("  second being the smooth (Taylor) limit.  The scaling range requires")
    print("  k_min r << 1 and k_max r >> 1, i.e. a wide separation of scales.\n")
    n_field = 131072
    seps = np.array([25, 40, 60, 90, 130, 190, 280, 400])
    seps_sat = np.array([800, 1400, 2400, 4000])
    print("   beta   D(r) exponent, r = 25-400   min(beta-1, 2)   exponent at r = 800-4000")
    for beta in (5.0 / 3.0, 2.0, 11.0 / 3.0, 4.0):
        f = band_limited_field(n_field, beta, 0.0005, 0.25)
        d = structure_function(f, seps)
        d_sat = structure_function(f, seps_sat)
        slope = np.polyfit(np.log(seps), np.log(d), 1)[0]
        slope_sat = np.polyfit(np.log(seps_sat), np.log(d_sat), 1)[0]
        print(f"   {beta:4.2f}   {slope:26.3f}   {min(beta-1.0, 2.0):14.2f}   "
              f"{slope_sat:+24.3f}")
    print("\n  inside the scaling range the measured exponent reproduces min(beta-1, 2)")
    print("  to within about 0.06.  Above the largest scale present in the screen the")
    print("  exponent collapses towards zero: D(r) saturates at twice the variance once")
    print("  samples separated by more than the largest scale are uncorrelated.  Note")
    print("  also that beta = 5/3, the one-dimensional spectrum of a fully developed")
    print("  turbulent screen, is the case with a genuine power law, while beta > 3")
    print("  gives the smooth r^2 limit and no turbulent exponent at all.")
    print("  The practical consequence: a fitted exponent is meaningless without the")
    print("  range of separations, a check that the saturation scale lies outside it,")
    print("  and enough field extent to separate the scales.  A scene that is only a")
    print("  few times the size of the smallest structure cannot measure beta.")

    section("5. Orbital ramp: what the quiet-pixel mask buys and costs")
    print("  a quadratic ramp plus one localised deformation signal, in centimetres\n")
    scene_x = x
    ramp = 0.6 + 2.2 * (scene_x - scene_x.mean()) / 1000.0 \
        + 0.35 * ((scene_x - scene_x.mean()) / 1000.0) ** 2
    ramp = ramp - ramp.mean()
    signal = 1.8 * np.exp(-((scene_x - 2000.0) / 400.0) ** 2)
    obs = ramp + signal
    quiet = np.abs(scene_x - 2000.0) > 1200.0
    print(f"  scene length {np.ptp(scene_x)/1000:.2f} km, signal peak "
          f"{signal.max():.3f} cm, ramp span {np.ptp(ramp):.3f} cm")
    print(f"  quiet pixels (|x - 2.0 km| > 1.2 km): {quiet.sum()} of {n_x}\n")
    print("   correction                       residual rms (cm)   recovered peak (cm)")
    for name, deg, mask in (("none", 0, None),
                            ("linear, quiet pixels", 1, quiet),
                            ("quadratic, quiet pixels", 2, quiet),
                            ("quadratic, ALL pixels", 2, np.ones(n_x, bool))):
        if deg == 0:
            resid = obs - obs.mean()
        else:
            pfit = np.polyfit(scene_x[mask], obs[mask], deg)
            resid = obs - np.polyval(pfit, scene_x)
        peak = resid[np.argmin(np.abs(scene_x - 2000.0))]
        print(f"   {name:32s}   {np.sqrt(np.mean(resid**2)):17.4f}   {peak:18.4f}")
    print(f"\n  the signal to recover is {signal.max():.3f} cm.  A quadratic fitted to")
    print("  the quiet pixels recovers it; the same quadratic fitted to ALL pixels")
    print("  absorbs part of the signal into the ramp, which is the bias that an")
    print("  unjustified quiet-pixel mask introduces.  A linear correction cannot")
    print("  represent the curvature and leaves a residual of the same order as the")
    print("  signal itself.  The mask is a modelling decision and must be justified.")
    print("  (no noise in this demonstration: every residual is a model error.)")

    section("6. Does stacking average an atmospheric screen away?")
    n_epochs = 20
    sigma_screen = 10.0     # mm per epoch
    print(f"  {n_epochs} epochs, independent screens of {sigma_screen:.0f} mm rms\n")
    print("   correlated fraction   residual of the epoch-mean (mm)")
    for rho in (0.0, 0.3, 0.6, 0.9):
        reps = 400
        out = []
        for _ in range(reps):
            common = RNG.standard_normal() * sigma_screen
            s = np.sqrt(rho) * common + np.sqrt(1.0 - rho) * sigma_screen \
                * RNG.standard_normal(n_epochs)
            out.append(abs(s.mean()))
        print(f"   {rho:19.1f}   {np.mean(out):27.3f}")
    print(f"\n  with fully independent screens the epoch mean has standard error")
    print(f"  sigma/sqrt(N) = {sigma_screen/np.sqrt(n_epochs):.3f} mm, and the")
    print("  measurement is close to that.  As a growing share of the screen is common")
    print("  to all epochs, the mean no longer shrinks: a screen that is present in")
    print("  every acquisition appears in NO difference and cancels, while a screen")
    print("  that persists over part of the record appears in the differences that")
    print("  straddle it and does not average away.")

    section("7. One uncorrected epoch in a rate estimate")
    n_dates = 40
    t = np.sort(RNG.uniform(0.0, 3.0, n_dates))
    v_true = 10.0        # mm/yr
    d_true = v_true * t
    d_obs = d_true.copy()
    d_obs[20] += 20.0    # 2 cm of uncorrected delay in one epoch
    v_clean = np.polyfit(t, d_true, 1)[0]
    v_dirty = np.polyfit(t, d_obs, 1)[0]
    print(f"  40 epochs over 3.0 yr, true rate {v_true:.2f} mm/yr")
    print(f"  a single epoch carries an uncorrected 20.00 mm screen")
    print(f"    rate from clean phases : {v_clean:.4f} mm/yr")
    print(f"    rate from biased phases: {v_dirty:.4f} mm/yr")
    print(f"    bias                   : {v_dirty - v_clean:+.4f} mm/yr "
          f"({100*(v_dirty-v_clean)/v_true:+.2f}% of the signal)")
    print("  a single bad epoch biases a rate for the whole record; the bias scales")
    print("  with the screen and with how far the epoch sits from the record centre.")
    print("  This is why outlier detection on the per-epoch residual, not just on the")
    print("  per-pair coherence, belongs in any time-series chain.")


if __name__ == "__main__":
    main()
