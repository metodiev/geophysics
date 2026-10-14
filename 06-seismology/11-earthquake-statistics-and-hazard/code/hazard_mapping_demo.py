#!/usr/bin/env python3
"""Hazard mapping and site amplification: 1D SH site response, band-limited site
factors, the shift of a design amplitude, and nonlinearity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hazard_mapping_demo.py

Everything is SYNTHETIC.  The soil and rock profiles, the bedrock hazard curve
and the nonlinearity are teaching values; no measured site response and no
published design map is used.

Contents
--------
1. The 1D SH transfer function of a soil layer on rock, its resonance frequency
   and its peak amplification (impedance ratio).
2. The same response with attenuation: what damping does to the peak.
3. Band-limited site factors: the average amplification depends on the band, so
   "the amplification factor" is not a single number.
4. Applying a site factor to a bedrock hazard curve: the change in the
   10%-in-50-yr amplitude.
5. Nonlinearity: strain-dependent reduction of the site factor, solved by
   fixed-point iteration, and its effect on the design amplitude.
6. Interpolation of a mapped parameter between boreholes: three defensible rules,
   three answers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC profiles (chosen teaching values) -----------------------------
VS_SOIL = 200.0          # m/s
RHO_SOIL = 1.8           # g/cm^3
H_SOIL = 30.0            # m, thickness of the soil layer
VS_ROCK = 800.0          # m/s
RHO_ROCK = 2.4           # g/cm^3
Q_SOIL = 20.0            # quality factor of the soil layer (SYNTHETIC)

# --- SYNTHETIC bedrock hazard curve (chosen teaching values) -----------------
LAM_REF = 0.002          # per yr at the reference amplitude
Z_REF = 0.1              # g
NEG_SLOPE = 2.5          # power-law exponent of the bedrock hazard curve
T_RETURN_TARGET = 474.6  # yr, the 10%-in-50-yr mean return period
PGA_NL = 0.30            # g, reference amplitude of the nonlinearity


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def transfer_sh(freq_hz, vs_layer=VS_SOIL, rho_layer=RHO_SOIL, h=H_SOIL,
                vs_rock=VS_ROCK, rho_rock=RHO_ROCK, q=np.inf):
    """Amplitude of the SH transfer function of one layer on a half-space,
    relative to the bedrock outcrop.

    For a layer of thickness h with impedance Z1 = rho1 vs1 on a half-space with
    Z2 = rho2 vs2, the surface/bedrock-outcrop transfer function is
    1 / (cos k*h + i (Z1/Z2) sin k*h), with the vertical wavenumber k = omega/vs.
    At zero frequency it is 1; at the fundamental resonance k*h = pi/2 it equals
    the impedance ratio Z2/Z1.  A finite quality factor Q is included by the
    standard causal substitution k -> (omega/vs)(1 - i/(2Q)).
    """
    f = np.asarray(freq_hz, dtype=float)
    omega = 2.0 * np.pi * f
    k = (omega / vs_layer) * (1.0 - 0.5j / q)
    z_ratio = (rho_rock * vs_rock) / (rho_layer * vs_layer)
    denom = np.cos(k * h) + 1j * (1.0 / z_ratio) * np.sin(k * h)
    return 1.0 / np.abs(denom)


def bedrock_rate(z_g):
    """SYNTHETIC bedrock hazard curve: annual rate of exceeding z, power law."""
    return LAM_REF * (np.asarray(z_g, dtype=float) / Z_REF) ** (-NEG_SLOPE)


def bisect_amplitude(target_rate, factor_fn, lo=0.001, hi=5.0):
    """Find the SURFACE amplitude whose annual exceedance rate equals the target.

    The site factor acts on the amplitude, so P(A_surface > z) =
    P(A_bedrock > z / F); the surface curve is the bedrock curve evaluated at
    z/F.  Since the bedrock rate decreases with z, the root is unique.
    """
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bedrock_rate(mid / factor_fn(mid)) > target_rate:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    section("1. 1D SH transfer function: resonance and impedance ratio")
    z_ratio = (RHO_ROCK * VS_ROCK) / (RHO_SOIL * VS_SOIL)
    f0 = VS_SOIL / (4.0 * H_SOIL)
    print(f"SYNTHETIC profile: soil vs = {VS_SOIL:.0f} m/s, rho = "
          f"{RHO_SOIL:.2f} g/cm^3, H = {H_SOIL:.0f} m")
    print(f"                   rock vs = {VS_ROCK:.0f} m/s, rho = "
          f"{RHO_ROCK:.2f} g/cm^3")
    print(f"impedance ratio Z_rock/Z_soil = {z_ratio:.3f}")
    print(f"fundamental resonance f0 = vs/(4H) = {f0:.4f} Hz")
    print("\n  transfer function amplitude, relative to the bedrock outcrop:")
    print("      frequency (Hz)   A(f)")
    for f in (0.1, 0.5, 1.0, f0, 2.0 * f0, 3.0 * f0, 4.0 * f0, 10.0):
        print(f"      {f:14.3f}   {float(transfer_sh(np.array([f]))[0]):.4f}")
    print(f"\nat the fundamental resonance the amplitude is the impedance ratio")
    print(f"  A(f0) = {float(transfer_sh(np.array([f0]))[0]):.4f} = Z_rock/Z_soil "
          f"= {z_ratio:.3f}")
    print(f"odd harmonics f = {f0:.2f}, {3 * f0:.2f}, {5 * f0:.2f} Hz resonate "
          f"alike for a lossless layer; even harmonics do not.")

    section("2. The same layer with attenuation")
    print(f"  a finite quality factor Q lowers and broadens the resonance:")
    print("      Q          A(f0)     f0 (Hz)")
    for q in (np.inf, 100.0, 20.0, 10.0, 5.0):
        f_test = np.geomspace(0.2, 8.0, 4000)
        a_test = transfer_sh(f_test, q=q)
        i_peak = int(np.argmax(a_test))
        q_label = "infinite" if np.isinf(q) else f"{q:.0f}"
        print(f"      {q_label:10s}   {a_test[i_peak]:6.3f}   {f_test[i_peak]:8.4f}")
    print("  attenuation, not the impedance contrast, sets the height of the")
    print("  peak.  Reporting a site amplification without the damping is")
    print("  reporting half a model.")

    section("3. Band-limited site factors: one response, several numbers")
    f = np.geomspace(0.05, 20.0, 20000)
    a = transfer_sh(f, q=Q_SOIL)
    print(f"  average of A(f) over several bands (Q = {Q_SOIL:.0f}):")
    print("      band (Hz)        mean A(f)")
    for lo, hi in ((0.1, 1.0), (0.5, 2.0), (0.5, 10.0), (1.0, 10.0),
                   (0.1, 10.0)):
        sel = (f >= lo) & (f <= hi)
        print(f"      {lo:4.1f}-{hi:5.1f}   {a[sel].mean():10.4f}")
    sel = (f >= 0.5) & (f <= 10.0)
    site_factor = float(a[sel].mean())
    print(f"\n  the design-relevant 0.5-10 Hz mean is {site_factor:.4f}; the")
    print(f"  peak is {a.max():.4f} at {f[int(np.argmax(a))]:.3f} Hz.  A single")
    print("  'amplification factor' is a band-averaged statement, and the band is")
    print("  part of the definition.")

    section("4. A site factor shifts the bedrock hazard curve")
    lam_target = 1.0 / T_RETURN_TARGET
    z_bedrock = bisect_amplitude(lam_target, lambda zz: 1.0)
    z_surface = bisect_amplitude(lam_target, lambda zz: site_factor)
    print(f"  SYNTHETIC bedrock hazard curve: rate = {LAM_REF:.4f} x "
          f"(z/{Z_REF:.1f})^-{NEG_SLOPE:.1f} per yr")
    print(f"  target rate = 1/{T_RETURN_TARGET:.0f} = {lam_target:.6f} per yr")
    print(f"\n      case                       amplitude (g)   rate at 0.2 g "
          f"(per yr)")
    print(f"      bedrock                    {z_bedrock:13.4f}   "
          f"{bedrock_rate(0.2):14.5f}")
    print(f"      surface, factor {site_factor:.3f}    {z_surface:13.4f}   "
          f"{bedrock_rate(0.2 / site_factor):14.5f}")
    print(f"  the surface amplitude at the same probability is "
          f"{z_surface / z_bedrock:.2f} times the")
    print(f"  bedrock amplitude, and the rate of exceeding a fixed 0.2 g rises by")
    print(f"  a factor {bedrock_rate(0.2 / site_factor) / bedrock_rate(0.2):.1f}.")
    print("  A hazard MAP for a region of uniform bedrock therefore cannot be")
    print("  used at a soil site without this step -- and the factor is a model,")
    print("  not a measurement.")

    section("5. Nonlinearity: the site factor depends on the shaking")
    print(f"  SYNTHETIC nonlinearity: amp(PGA) = 1 + (A_lin - 1) / "
          f"(1 + (PGA/{PGA_NL:.2f})^2)")
    a_lin = site_factor
    print("\n      surface PGA (g)   amplification   implied bedrock PGA (g)")
    for pga in (0.02, 0.05, 0.1, 0.2, 0.4, 0.8):
        amp = 1.0 + (a_lin - 1.0) / (1.0 + (pga / PGA_NL) ** 2)
        print(f"      {pga:15.3f}   {amp:13.4f}   {pga / amp:21.4f}")

    def amp_of_surface(zs):
        return 1.0 + (a_lin - 1.0) / (1.0 + (zs / PGA_NL) ** 2)

    z_nl = bisect_amplitude(lam_target, amp_of_surface)
    print(f"\n  linear case, surface amplitude at the target rate : "
          f"{z_surface:.4f} g")
    print(f"  nonlinear case (fixed-point solution)              : "
          f"{z_nl:.4f} g")
    print(f"  ratio nonlinear / linear = {z_nl / z_surface:.3f}: the soil moves")
    print(f"  less than a linear factor would predict, because its stiffness rises")
    print(f"  with strain.  Ignoring this overestimates the design motion at strong")
    print(f"  shaking levels and underestimates it at weak ones.")

    section("6. Interpolating a mapped parameter between boreholes")
    xs = np.array([0.0, 4.0, 9.0, 15.0])          # borehole positions, km
    vs30 = np.array([420.0, 260.0, 620.0, 330.0])  # m/s, SYNTHETIC values
    x_target = 6.5
    nearest = float(vs30[np.argmin(np.abs(xs - x_target))])
    weights = 1.0 / np.abs(xs - x_target)
    inv_dist = float(np.sum(weights * vs30) / weights.sum())
    linear = float(np.interp(x_target, xs, vs30))
    print(f"  four boreholes at x = {xs} km with vs30 = {vs30} m/s (SYNTHETIC)")
    print(f"  target position x = {x_target:.1f} km")
    print(f"\n      rule                        vs30 (m/s)   amplification at "
          f"0.5-10 Hz")
    for label, val in (("nearest borehole", nearest),
                       ("inverse-distance weighting", inv_dist),
                       ("linear interpolation", linear)):
        # a first-order site-factor rule: A = (vs_ref / vs30)^0.5, vs_ref named
        vs_ref = 760.0
        print(f"      {label:26s}   {val:9.1f}   "
              f"{(vs_ref / val) ** 0.5:20.3f}")
    print(f"\n  spread of the three answers: {100.0 * (max(nearest, inv_dist, linear) / min(nearest, inv_dist, linear) - 1.0):.1f} % in vs30.")
    print("  A contour map is an interpolation rule applied to sparse points, and")
    print("  the rule is a modelling decision.  The uncertainty it introduces is")
    print("  epistemic and is invisible on the map itself.")


if __name__ == "__main__":
    main()
