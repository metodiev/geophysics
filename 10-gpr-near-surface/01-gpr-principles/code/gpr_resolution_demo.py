#!/usr/bin/env python3
"""GPR resolution: vertical (Rayleigh, tuning, thin-bed) limits, the Fresnel
zone, lateral resolution as the width of the migrated point-spread function, and
the spatial sampling (alias) limit.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_resolution_demo.py

Everything here is SYNTHETIC: a chosen teaching velocity, a Ricker source, a
simplified unweighted Kirchhoff migration written out in full, and chosen
detectability thresholds.  No field data, no published resolution figure and no
instrument is involved.

Contents
--------
1. Vertical resolution: the Rayleigh criterion measured on two equal reflectors
   of the same polarity, and the criterion dependence of the answer.
2. A thin layer in a wedge: tuning thickness and the thin-bed amplitude that
   survives after resolution is lost.
3. First Fresnel zone radius: exact, approximate and half-amplitude, with the
   convention stated.
4. Lateral resolution as the width of the migrated point-spread function, its
   dependence on the migration aperture, and the coherent interference of two
   close targets.
5. Spatial sampling: the maximum unaliased dip and the aliased apparent dip.
6. Verification: migrated apex position error and image widths.
"""

import numpy as np
from scipy.signal import hilbert

RNG = np.random.default_rng(20261014)

# SYNTHETIC acquisition and medium parameters (chosen teaching values)
V = 0.09993           # m/ns, eps_r = 9
F0 = 0.2              # GHz = 200 MHz -- with t in ns the frequency is in GHz
LAM = V / F0          # m, wavelength in the medium
DT = 0.025            # ns, time sample
NT = 4000             # samples -> 100 ns window (the aperture reaches 83 ns)
DXM = 0.025           # m, trace spacing of the synthetic line
DZG = 0.02            # m, migration depth step


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def gabor(t, f0, sigma):
    """Monochromatic burst: a cosine of frequency f0 under a Gaussian envelope."""
    return np.cos(2.0 * np.pi * f0 * t) * np.exp(-t ** 2 / (2.0 * sigma ** 2))


def wiggle(t, tw, ww, t0):
    """Interpolate wavelet ww defined on tw so that it peaks at t0."""
    return np.interp(t - t0, tw, ww, left=0.0, right=0.0)


def zero_offset_section(targets, x, t, tw, ww, z_depth):
    """Zero-offset section of point scatterers at (x_target, z_depth)."""
    d = np.zeros((x.size, t.size))
    for xt in targets:
        t0 = 2.0 * np.sqrt(z_depth ** 2 + (x - xt) ** 2) / V
        d += np.interp(t[None, :] - t0[:, None], tw, ww, left=0.0, right=0.0)
    return d


def kirchhoff_migrate(d, x, t, xg, zg, aperture):
    """Simplified 2-D Kirchhoff migration: unweighted sum along the zero-offset
    diffraction hyperbola t = 2 sqrt(z^2 + (x_t - x_g)^2)/v, restricted to
    |x_t - x_g| <= aperture (a limited migration aperture, as in practice)."""
    m = np.zeros((zg.size, xg.size))
    ix = np.arange(x.size)[:, None]
    for iz, z in enumerate(zg):
        tt = 2.0 * np.sqrt(z ** 2 + (xg[None, :] - x[:, None]) ** 2) / V
        idx = np.clip(tt / DT, 0.0, t.size - 1.001)
        i0 = idx.astype(int)
        fr = idx - i0
        weight = (np.abs(xg[None, :] - x[:, None]) <= aperture).astype(float)
        m[iz] = ((d[ix, i0] * (1.0 - fr) + d[ix, i0 + 1] * fr) * weight).sum(axis=0)
    return m


def envelope_fwhm(profile, dx, levels=0.5):
    """Width of the envelope of a migrated profile above `levels` of its peak.

    The analytic envelope (Hilbert transform along x) removes the oscillatory
    carrier of a band-limited image, so the width is a property of the image and
    not of the sampling; this must be stated with any width quoted from it.
    """
    env = np.abs(hilbert(profile))
    return float(np.sum(env > levels * env.max()) * dx)


def peaks_above(profile, frac=0.9):
    """Count local maxima above frac x the maximum (Rayleigh-type criterion)."""
    idx = np.where((profile[1:-1] > profile[:-2])
                   & (profile[1:-1] >= profile[2:]))[0] + 1
    return int(np.sum(profile[idx] > frac * profile.max()))


def main():
    f0 = F0
    t = np.arange(NT) * DT
    tw = np.arange(-25.0, 25.0, DT)
    ww = ricker(tw, f0)
    print(f"SYNTHETIC parameters: v = {V:.5f} m/ns, f0 = {F0*1000:.0f} MHz, "
          f"lambda = {LAM:.4f} m")
    print(f"sampling: dt = {DT:.3f} ns, {NT} samples = {NT*DT:.0f} ns window; "
          f"trace spacing {DXM:.3f} m")
    print(f"reference lengths: lambda/4 = {LAM/4:.4f} m, lambda/2 = {LAM/2:.4f} m, "
          f"lambda = {LAM:.4f} m")

    section("1. Vertical resolution: the Rayleigh criterion, measured")
    print("   Composite trace = two equal Ricker wavelets of the SAME polarity")
    print("   separated by dt = 2 dz/v (two interfaces with the same sign of")
    print("   reflection coefficient).  Criterion: resolved when the trace has two")
    print("   local maxima each above 0.9 of the largest, which excludes the")
    print("   Ricker's own sidelobes (they sit at 0.446 of the main lobe).")
    print("   dz (m)  dz/lambda   dt (ns)   peaks >= 0.9 max   composite max")
    first_two = None
    for k, dz in enumerate(np.arange(0.04, 0.302, 0.005)):
        dt_ns = 2.0 * dz / V
        comp = wiggle(t, tw, ww, 10.0) + wiggle(t, tw, ww, 10.0 + dt_ns)
        npk = peaks_above(comp)
        if npk >= 2 and first_two is None:
            first_two = dz
        if k % 8 == 0:
            print(f"   {dz:6.3f}  {dz/LAM:9.3f}   {dt_ns:7.2f}   {npk:16d}   "
                  f"{comp.max():13.4f}")
    print(f"   smallest resolved separation: {first_two:.3f} m = "
          f"{first_two/LAM:.3f} lambda = {2*first_two/V:.2f} ns of two-way time")
    print(f"   the classical Rayleigh rule quotes half the dominant period,")
    print(f"   1/(2 f0) = {0.5/F0:.2f} ns = {V*0.5/F0/2:.4f} m = "
          f"{V*0.5/F0/2/LAM:.3f} lambda; the criterion used here is more")
    print(f"   permissive than that by {-(first_two/(V*0.5/F0/2)-1)*100:.0f}%.  Two")
    print("   reasonable criteria therefore differ by a third, so a resolution number")
    print("   without its criterion is not a number.")
    print(f"   (The Ricker's own first zero crossing is at "
          f"{1/(np.sqrt(2)*np.pi*F0):.3f} ns, not 1/(2 f0) = {0.5/F0:.3f} ns.)")

    section("2. A thin layer in a wedge: tuning thickness and thin-bed amplitude")
    print("   A thin layer produces two reflections of OPPOSITE polarity, so the")
    print("   composite is w(t) - w(t - dt): the classic wedge model.  The tuning")
    print("   curve is |composite| max against thickness.")
    print("   dz (m)  dz/lambda   dt (ns)   |composite| max")
    best_z, best_a = None, -1.0
    for k, dz in enumerate(np.arange(0.02, 0.42, 0.01)):
        dt_ns = 2.0 * dz / V
        a = abs(wiggle(t, tw, ww, 10.0) - wiggle(t, tw, ww, 10.0 + dt_ns)).max()
        if a > best_a:
            best_a, best_z = a, dz
        if k % 5 == 0:
            print(f"   {dz:6.2f}  {dz/LAM:9.3f}   {dt_ns:7.2f}   {a:15.4f}")
    a_e = abs(wiggle(t, tw, ww, 10.0)
              - wiggle(t, tw, ww, 10.0 + 2.0 * (LAM / 8.0) / V)).max()
    a_q = abs(wiggle(t, tw, ww, 10.0)
              - wiggle(t, tw, ww, 10.0 + 2.0 * (LAM / 4.0) / V)).max()
    print(f"   tuning maximum at dz = {best_z:.2f} m = {best_z/LAM:.3f} lambda, "
          f"amplitude {best_a:.4f}")
    print(f"   rule-of-thumb lambda/4 = {LAM/4:.4f} m = {LAM/4/LAM:.3f} lambda "
          f"carries {a_q/best_a*100:.1f}% of that maximum; lambda/8 = "
          f"{LAM/8:.4f} m carries {a_e/best_a*100:.1f}%")
    dzs = np.arange(0.005, 0.0505, 0.005)
    amps = np.array([abs(wiggle(t, tw, ww, 10.0)
                         - wiggle(t, tw, ww, 10.0 + 2.0 * dz / V)).max()
                     for dz in dzs])
    slope = np.polyfit(dzs, amps, 1)[0]
    print(f"   fitted slope over dz = 0.005-0.050 m: {slope:.3f} per metre "
          f"= {slope*LAM:.3f} per wavelength")
    thresh = 0.05
    print(f"   with a chosen amplitude detection threshold of {thresh:.2f} of one")
    print(f"   reflector, the thinnest detectable bed is {thresh/slope:.4f} m = "
          f"{thresh/slope/LAM:.4f} lambda")
    print("   Detection is not resolution: a layer thinner than lambda/4 is")
    print("   detectable, but its thickness and its two interfaces cannot be")
    print("   separated.  Reporting one as the other is the commonest overclaim")
    print("   in shallow GPR.")

    section("3. First Fresnel zone: exact, approximate and half-amplitude")
    print("   Convention: the first Fresnel zone is the set of surface points whose")
    print("   TWO-WAY path is longer than the vertical path by at most lambda/2.")
    print("   Solving 2(sqrt(d^2+r^2) - d) = lambda/2 gives the exact radius")
    print("   r = sqrt(lambda d/2 + lambda^2/16); the usual approximation drops the")
    print("   second term and gives r ~ sqrt(lambda d / 2).")
    print("   d (m)   r exact   r approx   error (%)   diameter (m)   diameter/lambda"
          "   half-amplitude r")
    for d in (0.25, 0.5, 1.0, 2.0, 4.0):
        r_ex = np.sqrt(LAM * d / 2.0 + LAM ** 2 / 16.0)
        r_ap = np.sqrt(LAM * d / 2.0)
        r_half = np.sqrt(LAM * d / 4.0 + LAM ** 2 / 64.0)
        print(f"   {d:5.2f}   {r_ex:7.4f}   {r_ap:8.4f}   "
              f"{(r_ap/r_ex-1)*100:8.2f}   {2*r_ex:10.4f}   {2*r_ex/LAM:13.2f}   "
              f"{r_half:16.4f}")
    print("   The approximation UNDERestimates the zone: by 11% at d = lambda/2")
    print("   and by under 1% once d exceeds about 4 lambda.  The half-amplitude")
    print("   zone (two-way path difference lambda/4) is smaller by a factor")
    print("   sqrt(2).  The unmigrated horizontal resolution is the Fresnel")
    print("   DIAMETER, between 1.1 and 4.0 wavelengths for these depths.")

    section("4. Lateral resolution: width of the migrated point-spread function")
    x = np.arange(-4.0, 4.0 + 1e-9, DXM)
    xg = x.copy()
    zg = np.arange(0.20, 2.001, DZG)
    z_target = 1.00
    iz_target = int(round((z_target - zg[0]) / DZG))
    print(f"   SYNTHETIC point scatterer at z = {z_target:.2f} m, a {x.size}-trace")
    print(f"   line at {DXM:.3f} m spacing, migrated with the unweighted Kirchhoff")
    print("   sum of this script.  Width = envelope width at half maximum along x.")
    print("   migration aperture   image FWHM (m)   FWHM/lambda   comparison")
    for ap in (0.5, 1.0, 2.0, 4.0):
        d = zero_offset_section([0.0], x, t, tw, ww, z_target)
        m = kirchhoff_migrate(d, x, t, xg, zg, ap)
        prof = m[iz_target]
        fw = envelope_fwhm(prof, DXM)
        print(f"   +/- {ap:4.1f} m          {fw:13.3f}   {fw/LAM:11.3f}   "
              f"Fresnel diameter 2r = "
              f"{2*np.sqrt(LAM*z_target/2 + LAM**2/16):.3f} m")
    print("   With a small aperture the migrated width approaches the unmigrated")
    print(f"   Fresnel diameter ({2*np.sqrt(LAM*z_target/2 + LAM**2/16):.3f} m); as the aperture")
    print("   grows it falls to a floor set by the temporal bandwidth, about a")
    print("   third of a wavelength here.  Resolution is therefore a property of")
    print("   the ACQUISITION as much as of the frequency: a wider aperture at the")
    print("   same frequency resolves more.")
    print("\n   Two scatterers at separations s = 0.50 lambda and 1.50 lambda, same")
    print("   migration, aperture +/- 4.0 m.  The images interfere COHERENTLY, so")
    print("   the midpoint amplitude is not a monotone function of separation:")
    for s in (LAM / 2.0, 1.5 * LAM):
        d = zero_offset_section([-s / 2.0, s / 2.0], x, t, tw, ww, z_target)
        m = kirchhoff_migrate(d, x, t, xg, zg, 4.0)
        env = np.abs(hilbert(m[iz_target]))
        mid = env[np.argmin(np.abs(xg))]
        at_targets = 0.5 * (env[np.argmin(np.abs(xg + s / 2.0))]
                            + env[np.argmin(np.abs(xg - s / 2.0))])
        print(f"     s = {s:.3f} m = {s/LAM:.2f} lambda: envelope at the midpoint "
              f"{mid:.1f}, at the targets {at_targets:.1f}, ratio "
              f"{mid/at_targets:.3f}")
    print("   A single 'resolution' cannot be read off these ratios; the honest")
    print("   statement is the point-spread width plus the aperture and frequency")
    print("   that produced it.")

    section("5. Spatial sampling: unaliased dip and aliased apparent dip")
    dx_coarse = LAM / 2.0
    theta_true = np.radians(45.0)
    print(f"   Analytic relations for a zero-offset section sampled at dx = "
          f"{dx_coarse:.4f} m = lambda/2:")
    print("     maximum unaliased dip:  sin(theta_max) = lambda / (4 dx)")
    print("     aliased apparent dip:   sin(theta_app) = sin(theta) - lambda/(2 dx)")
    s_max = min(1.0, LAM / (4.0 * dx_coarse))
    print(f"     sin(theta_max) = {s_max:.4f} -> theta_max = "
          f"{np.degrees(np.arcsin(s_max)):.2f} deg")
    pred = np.sin(theta_true) - LAM / (2.0 * dx_coarse)
    print(f"     for theta = 45.00 deg: sin(theta_app) = {pred:.4f} -> "
          f"theta_app = {np.degrees(np.arcsin(pred)):.2f} deg")
    sigma = 1.5 / F0
    fine_x = np.arange(-2.0, 2.0 + 1e-9, 0.005)
    dip = 2.0 * np.sin(theta_true) / V
    traces = np.array([gabor(t - (4.0 + dip * xx), F0, sigma) for xx in fine_x])
    idx = np.arange(0, fine_x.size, int(round(dx_coarse / 0.005)))
    coarse = traces[idx]
    lags = []
    for i in range(1, coarse.shape[0]):
        c = np.correlate(coarse[i], coarse[i - 1], mode="full")
        lag_axis = (np.arange(c.size) - (coarse.shape[1] - 1)) * DT
        keep = np.abs(lag_axis) <= 0.5 / F0
        lags.append(lag_axis[keep][np.argmax(c[keep])])
    lag = float(np.median(lags))
    sin_meas = (lag / dx_coarse) * V / 2.0
    print(f"   measured adjacent-trace lag at dx = {dx_coarse:.4f} m: "
          f"{lag:+.3f} ns")
    print(f"   the true lag would be {dip*dx_coarse:+.3f} ns, beyond the half")
    print(f"   period {0.5/F0:.3f} ns, so the lag is measured modulo the period")
    print(f"   measured apparent dip: sin(theta_app) = {sin_meas:+.4f} -> "
          f"{np.degrees(np.arcsin(np.clip(sin_meas, -1, 1))):+.2f} deg")
    print(f"   analytic prediction: {np.degrees(np.arcsin(pred)):+.2f} deg "
          f"(difference {abs(sin_meas-pred):.4f} in sin theta)")
    print("   The event has not moved; it has been SAMPLED too coarsely, and the")
    print("   apparent dip has the wrong SIGN.  Line spacing in a grid is chosen")
    print("   from the shortest wavelength and the steepest expected dip.")

    section("6. Verification: migrated apex position and image widths")
    d = zero_offset_section([0.0], x, t, tw, ww, z_target)
    m = kirchhoff_migrate(d, x, t, xg, zg, 4.0)
    i_peak = np.unravel_index(np.argmax(m), m.shape)
    x_apex, z_apex = xg[i_peak[1]], zg[i_peak[0]]
    print(f"   true scatterer: x = 0.000 m, z = {z_target:.3f} m")
    print(f"   migrated apex : x = {x_apex:.3f} m, z = {z_apex:.3f} m")
    print(f"   position error: {abs(x_apex)*100:.2f} cm laterally, "
          f"{abs(z_apex-z_target)*100:.2f} cm in depth")
    row = m[i_peak[0]]
    col = m[:, i_peak[1]]
    xw = envelope_fwhm(row, DXM)
    zenv = np.abs(hilbert(col))
    zw = float(np.sum(zenv > 0.5 * zenv.max()) * DZG)
    print(f"   envelope width at half maximum: {xw:.3f} m = {xw/LAM:.3f} lambda "
          "laterally,")
    print(f"                                   {zw:.3f} m = {zw/LAM:.3f} lambda "
          "in depth")
    print("   A migrated point scatterer is not a point: its width IS the")
    print("   resolution of the section, measured here on the image this script")
    print("   produced.")
    print("\n   Every number above comes from the SYNTHETIC model of this script;")
    print("   no measured resolution figure is quoted.")


if __name__ == "__main__":
    main()
