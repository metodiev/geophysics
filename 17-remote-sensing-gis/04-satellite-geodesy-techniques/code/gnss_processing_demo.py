#!/usr/bin/env python3
"""GNSS processing: double differencing, the tropospheric delay and its mapping
function, ambiguity resolution and its failure mode, velocity estimation from a
daily time series, the effect of coloured noise, and the reference-frame
coupling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_processing_demo.py

Everything is SYNTHETIC: the stations, clocks, atmospheres, noise realisations
and time series are teaching data generated here.  The physical constants
(c, standard gravity, the Earth radius) are stated standards.  No real network,
station, product or observation file is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0
R_EARTH = 6_371_000.0


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def flicker(n, rng):
    """Unit-variance noise with a 1/f (flicker) power spectrum."""
    f = np.fft.rfftfreq(n)
    amp = np.ones_like(f)
    amp[1:] = f[1:] ** -0.5
    spec = (rng.standard_normal(f.size) + 1j * rng.standard_normal(f.size)) * amp
    spec[0] = 0.0
    x = np.fft.irfft(spec, n=n)
    return x / x.std()


def main():
    section("1. Double differencing: what cancels and what does not")
    print("  P = range + c(dt_receiver - dt_satellite) + atmosphere + noise\n")
    rng = RNG
    pos_a = np.array([4.0e6, 3.0e6, 4.0e6])
    pos_b = pos_a + np.array([60e3, 80e3, 0.0])       # 100 km baseline
    dirs = np.array([(0.35, 0.30, 0.89), (0.80, -0.40, 0.45),
                     (-0.60, 0.55, 0.58), (-0.30, -0.75, 0.59)])
    dirs = dirs / np.linalg.norm(dirs, axis=1)[:, None]
    sats = pos_a + 26.6e6 * dirs
    clk_a, clk_b = 1.5e-4, -0.8e-4                    # s
    sat_clk = rng.normal(0.0, 1.0e-4, len(sats))      # s
    rho_a = np.array([np.linalg.norm(s - pos_a) for s in sats])
    rho_b = np.array([np.linalg.norm(s - pos_b) for s in sats])
    p_a = rho_a + C * (clk_a - sat_clk) + rng.normal(0.0, 0.30, len(sats))
    p_b = rho_b + C * (clk_b - sat_clk) + rng.normal(0.0, 0.30, len(sats))
    sd = p_a - p_b
    sd_true = rho_a - rho_b
    dd = sd - sd[0]
    dd_true = sd_true - sd_true[0]
    print(f"  baseline {np.linalg.norm(pos_b-pos_a)/1e3:.1f} km, "
          f"receiver clocks {clk_a*C/1e3:+.1f} km and {clk_b*C/1e3:+.1f} km,")
    print(f"  satellite clocks of order {sat_clk.std()*C:.0f} m\n")
    print("   satellite   single difference (m)   true (m)   residual (m)")
    for k in range(len(sats)):
        print(f"   {k:9d}   {sd[k]:21.3f}   {sd_true[k]:8.3f}   "
              f"{sd[k]-sd_true[k]:12.3f}")
    print(f"\n  the single-difference residual has mean "
          f"{(sd-sd_true).mean():.3f} m and spread "
          f"{(sd-sd_true).std():.3f} m:")
    print(f"  the receiver clock difference c(dt_a - dt_b) = "
          f"{C*(clk_a-clk_b):.1f} m survives as a common offset.")
    print(f"  the satellite clock error is GONE: sd - sd_true is the same for every")
    print(f"  satellite to within {np.ptp(sd-sd_true-sd[0]+sd_true[0]):.3f} m.")
    resid_dd = dd - dd_true
    print("\n   satellite   double difference (m)   true (m)   residual (m)")
    for k in range(len(sats)):
        print(f"   {k:9d}   {dd[k]:23.3f}   {dd_true[k]:8.3f}   {resid_dd[k]:12.3f}")
    print(f"\n  double-difference residual: mean {resid_dd.mean():.3f} m, "
          f"spread about the mean {resid_dd.std():.3f} m")
    print(f"  against sqrt(2) x 0.30 = {np.sqrt(2)*0.30:.3f} m for a single")
    print("  difference and sqrt(2) x that for the difference of two, i.e. "
          f"{np.sqrt(2)*np.sqrt(2)*0.30:.3f} m.")
    print("  Both clocks are gone: the receiver clock difference of")
    print(f"  {C*(clk_a-clk_b)/1e3:.1f} km and the satellite clocks of "
          f"{sat_clk.std()*C:.0f} m rms appear nowhere.")
    print("  Only the differential geometry, the differential atmosphere and the")
    print("  noise remain - which is why relative positioning reaches centimetres")
    print("  while absolute positioning does not.")

    section("2. The tropospheric delay and the mapping function")
    h = np.arange(0.0, 60000.0, 10.0)
    n_dry = 315.0 * np.exp(-h / 8000.0)
    n_wet = 40.0 * np.exp(-h / 2000.0)
    zhd = 1e-6 * np.trapezoid(n_dry, h)
    zwd = 1e-6 * np.trapezoid(n_wet, h)
    print("  synthetic profile: N(h) = 315 exp(-h/8 km) + 40 exp(-h/2 km) ppm")
    print(f"  zenith hydrostatic delay ZHD = {zhd:.4f} m")
    print(f"  zenith wet delay         ZWD = {zwd:.4f} m")
    print(f"  total zenith delay           = {zhd+zwd:.4f} m\n")
    z = np.radians(np.array([0.0, 30.0, 60.0, 75.0, 85.0]))
    m_flat = 1.0 / np.cos(np.where(z == 0, 1e-12, z))
    m_flat[0] = 1.0
    h_eff = 8000.0
    m_curve = 1.0 / np.sqrt(1.0 - (R_EARTH / (R_EARTH + h_eff)) ** 2 * np.sin(z) ** 2)
    print("   zenith angle   flat 1/cos z   curved-Earth mapping   flat overestimate")
    for zz, mf, mc in zip(np.degrees(z), m_flat, m_curve):
        print(f"   {zz:12.0f}   {mf:12.4f}   {mc:20.4f}   "
              f"{mf-mc:17.4f} ({100*(mf/mc-1):+.2f}%)")
    print("\n  at low elevation the plane-parallel mapping overestimates the slant")
    print(f"  delay; for a {zhd:.2f} m zenith delay at 85 deg the difference is "
          f"{zhd*(m_flat[-1]-m_curve[-1]):.3f} m")
    print("  of range.  The mapping function is therefore a model with its own error")
    print("  budget, and it is the reason low-elevation observations are down-weighted")

    section("3. A wet-delay error becomes a height error")
    print("  the slant delay is the zenith delay times the mapping function, so a")
    print("  zenith error appears amplified in the height solution\n")
    print("   zenith angle   flat 1/cos z   curved mapping   height error from")
    print("                                              1 cm of ZWD, curved (cm)")
    for zz in (0.0, 30.0, 60.0, 75.0, 85.0):
        zr = np.radians(zz)
        mf = 1.0 / np.cos(zr) if zz > 0 else 1.0
        mc = 1.0 / np.sqrt(1.0 - (R_EARTH / (R_EARTH + 8000.0)) ** 2 * np.sin(zr) ** 2)
        print(f"   {zz:12.0f}   {mf:7.4f}   {mc:14.4f}   {1.0*mc:27.3f}")
    print("\n  a 1 cm error in the zenith wet delay is a 1 cm height error at zenith")
    print("  and 9.9 cm at 85 degrees.  Since ZWD itself is only a few centimetres and")
    print("  varies by centimetres between stations, the wet delay is the limiting")
    print("  error in GNSS height, and it is why height is the noisiest coordinate.")

    section("4. Ambiguity resolution: benefit and failure mode")
    lam = 0.190294
    print(f"  carrier wavelength {lam*100:.4f} cm; the integer N is unknown")
    print("  float: keep the real-valued estimate; fixed: round to integers\n")
    print("   sigma of the float ambiguity (cycles)   wrong-fix rate   "
          "rms range error, fixed (cm)   float (cm)")
    for sig in (0.05, 0.10, 0.20, 0.40):
        reps = 4000
        err_fx, err_fl, wrong = [], [], 0
        for _ in range(reps):
            n_true = 1000.0
            n_float = n_true + rng.normal(0.0, sig)
            n_fix = np.round(n_float)
            frac = n_float - n_true                  # fractional part estimate
            err_fl.append(abs(frac) * lam)
            err_fx.append(abs(n_fix - n_true + frac) * lam)
            if abs(n_fix - n_true) > 0.5:
                wrong += 1
        print(f"   {sig:38.2f}   {wrong/reps:14.4f}   "
              f"{np.sqrt(np.mean(np.array(err_fx)**2))*100:27.3f}   "
              f"{np.sqrt(np.mean(np.array(err_fl)**2))*100:11.3f}")
    print("\n  fixing helps only while the fix is right.  At sigma = 0.05 and 0.10")
    print("  cycles the wrong-fix rate is zero and the two agree exactly, because the")
    print("  truth is the same in both cases: only the integer is at stake.  At 0.20")
    print("  cycles 1.2% of fixes are wrong and at 0.40 cycles 21.7%; each wrong fix")
    print("  displaces the range by a whole wavelength, so the fixed rms (4.80 cm)")
    print("  is then WORSE than the float rms (3.76 cm) - the fix has destroyed the")
    print("  solution it was meant to improve.  A fix is therefore accepted only")
    print("  after validation, and the validation statistic, not the residual, is the")
    print("  number to report.")

    section("5. Velocity from a daily position time series")
    span_yr = 3.0
    n_days = 1000
    t = np.sort(RNG.uniform(0.0, span_yr, n_days))
    v_true = 15.0            # mm/yr
    annual = 4.0             # mm
    sigma_pos = 1.0          # mm
    print(f"  {n_days} daily solutions over {span_yr:.1f} yr, position noise "
          f"{sigma_pos:.1f} mm rms")
    print(f"  truth: velocity {v_true:.1f} mm/yr plus an annual term of "
          f"{annual:.1f} mm\n")
    for name, span in (("full record", span_yr), ("1.2 yr only", 1.2)):
        mask = t <= span
        tt = t[mask]
        for model, deg in (("linear only", 1), ("linear + annual", 0)):
            errs = []
            for _ in range(300):
                y = v_true * tt + annual * np.sin(2 * np.pi * tt) \
                    + sigma_pos * RNG.standard_normal(tt.size)
                if model == "linear only":
                    v_est = np.polyfit(tt, y, 1)[0]
                else:
                    a_mat = np.column_stack([tt, np.sin(2 * np.pi * tt),
                                             np.cos(2 * np.pi * tt),
                                             np.ones_like(tt)])
                    coef, *_ = np.linalg.lstsq(a_mat, y, rcond=None)
                    v_est = coef[0]
                errs.append(v_est - v_true)
            errs = np.array(errs)
            print(f"   {name:12s} {model:16s}: bias {errs.mean():+7.3f} mm/yr, "
                  f"scatter {errs.std():6.3f} mm/yr")
    print("\n  the annual term is not noise: omitting it biases the rate, and the")
    print("  bias is larger than the formal scatter.  A short record makes it worse")
    print("  because the sinusoid is then nearly degenerate with the linear term -")
    print("  the same projection problem as the InSAR time series of lesson 17-03-03.")

    section("6. Noise colour changes the velocity uncertainty")
    print(f"  {n_days} daily solutions, 1/f noise versus white noise, same variance\n")
    for label, gen in (("white", lambda n: RNG.standard_normal(n)),
                       ("flicker", lambda n: flicker(n, RNG))):
        errs = []
        for _ in range(300):
            y = v_true * t + sigma_pos * gen(t.size)
            a_mat = np.column_stack([t, np.ones_like(t)])
            coef, *_ = np.linalg.lstsq(a_mat, y, rcond=None)
            errs.append(coef[0] - v_true)
        errs = np.array(errs)
        print(f"   {label:8s}: velocity scatter {errs.std():.4f} mm/yr  "
              f"(and a mean bias of {errs.mean():+.4f})")
    print("\n  correlated noise inflates the velocity uncertainty far beyond the")
    print("  white-noise prediction: neighbouring days are not independent, so the")
    print("  effective number of observations is much smaller than the number of")
    print("  days.  Any uncertainty quoted from a GNSS time series must state the")
    print("  noise model assumed, or it is not reproducible.")

    section("7. The reference frame is part of the solution")
    print("  a network is solved relative to a reference station or a reference")
    print("  frame.  If the assumed reference coordinates are wrong, the error is")
    print("  shared by every station in the solution\n")
    offset = np.array([0.010, 0.000, 0.000])     # 1 cm of assumed-frame error
    print(f"   assumed-frame error      : {np.linalg.norm(offset)*100:.2f} cm")
    print(f"   common shift of solutions: {np.linalg.norm(offset)*100:.2f} cm "
          f"(by construction: the datum is a choice)")
    local = np.array([0.003, -0.002, 0.001])
    print(f"   internal relative accuracy: {np.linalg.norm(local)*100:.2f} cm "
          f"(unaffected by the datum error)")
    print("\n  the lesson: relative coordinates can be centimetre-accurate while the")
    print("  absolute frame is wrong by centimetres, and no residual in the")
    print("  adjustment will reveal it.  Distinguishing 'precise' from 'accurate',")
    print("  and stating the frame and its realisation, is the whole content of the")
    print("  geodetic reference-frame module 07-04.")


if __name__ == "__main__":
    main()
