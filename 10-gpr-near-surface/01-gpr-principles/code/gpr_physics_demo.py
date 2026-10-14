#!/usr/bin/env python3
"""GPR physics: propagation speed, reflection coefficients, the low-loss
regime, and the spectral content of the source pulse.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_physics_demo.py

Everything here is SYNTHETIC.  The material permittivities are chosen teaching
values that span the range encountered in the shallow subsurface, not measured
site values.  The only physical constant that is not chosen is the static
relative permittivity of pure water at 20 C (80.1) and the speed of light,
c = 2.99792458e8 m/s.

Contents
--------
1. Low-loss wave speed v = c / sqrt(eps_r); the sqrt(eps_r) thickness -> time map.
2. Normal-incidence reflection and transmission coefficients at layer contacts,
   with the energy check R^2 + T_energy = 1.
3. Loss tangent sigma / (omega eps): which of these media are low-loss at which
   frequency (regime of validity of every formula used in this module).
4. Exact complex-wavenumber alpha and phase speed versus their low-loss
   approximations, as a function of loss tangent.
5. The Ricker source pulse: measured peak, mean and bandwidth versus the
   analytic values for that wavelet.
6. A two-layer SYNTHETIC model: two-way times, amplitudes, and the depth
   conversion of a picked time.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_S = 2.99792458e8          # speed of light in vacuum, m/s (exact by definition)
C_M_NS = 0.299792458          # the same, in m/ns -- the unit GPR works in
EPS0_F_M = 8.8541878128e-12   # vacuum permittivity, F/m
MU0_H_M = 4.0e-7 * np.pi      # vacuum permeability, H/m (definition, exact)
EPS_WATER = 80.1              # static relative permittivity of pure water, 20 C

# SYNTHETIC materials: (name, relative permittivity) -- chosen teaching values
MATERIALS = (
    ("air (dry soil pore space)", 1.0),
    ("ice", 3.17),
    ("dry sand / dry soil", 4.0),
    ("wet sand (moderate saturation)", 9.0),
    ("wet sand (high saturation)", 16.0),
    ("saturated clay-rich soil", 25.0),
    ("fresh water", EPS_WATER),
)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def v_low_loss(eps_r):
    """Low-loss, non-magnetic phase speed, m/ns.  eps_r dimensionless."""
    return C_M_NS / np.sqrt(eps_r)


def reflection_coeff(eps_1, eps_2):
    """Normal-incidence E-field reflection coefficient for non-magnetic media."""
    return (np.sqrt(eps_1) - np.sqrt(eps_2)) / (np.sqrt(eps_1) + np.sqrt(eps_2))


def ricker(t, t0, f0):
    """Zero-phase Ricker wavelet, peak at t0, peak frequency f0 (same units of t)."""
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def exact_alpha_beta(eps_r, sigma, f_hz):
    """Exact attenuation constant and phase constant for a lossy dielectric.

    Returns (alpha, beta) in 1/m.  alpha + i*beta = sqrt(i*omega*mu*(sigma + i*omega*eps)).
    Low-loss forms: alpha ~ (sigma/2) sqrt(mu/eps), beta ~ omega sqrt(mu eps).
    """
    omega = 2.0 * np.pi * f_hz
    eps = EPS0_F_M * eps_r
    gamma = np.sqrt(1j * omega * MU0_H_M * (sigma + 1j * omega * eps))
    return gamma.real, gamma.imag


def main():
    section("1. Low-loss wave speed v = c / sqrt(eps_r)   [c = 0.299792458 m/ns]")
    print("   medium                          eps_r      v (m/ns)   v (cm/ns)")
    for name, eps_r in MATERIALS:
        v = v_low_loss(eps_r)
        print(f"   {name:30s} {eps_r:6.2f}   {v:9.5f}   {v * 100:8.3f}")
    print("   v is non-unique in eps_r: eps_r = (c/v)^2, so a 10% speed error")
    print("   corresponds to a (1.1^2 - 1) = 21% error in permittivity.")

    section("2. Normal-incidence reflection coefficients (non-magnetic)")
    print("   interface                                     R        R^2    T_energy")
    pairs = ((1.0, 4.0), (1.0, 9.0), (4.0, 9.0), (4.0, 16.0), (4.0, 25.0),
             (9.0, 16.0), (9.0, EPS_WATER), (16.0, 25.0))
    for e1, e2 in pairs:
        R = reflection_coeff(e1, e2)
        print(f"   eps_r {e1:5.2f} -> {e2:6.2f}{'':22s} {R:+7.4f}  {R**2:6.4f}   "
              f"{1.0 - R**2:8.4f}")
    print("   R = (sqrt(e1) - sqrt(e2)) / (sqrt(e1) + sqrt(e2)); energy reflection R^2,")
    print("   energy transmission 1 - R^2.  Sign is irrelevant to a zero-phase")
    print("   wavelet; the magnitude is what sets the reflection amplitude.")
    e1, e2 = 4.0, 9.0
    R = reflection_coeff(e1, e2)
    print(f"   check: |R| = {abs(R):.4f}, energy sum = "
          f"{R**2 + (1 - R**2):.6f} (must be 1.000000)")

    section("3. Loss tangent tan(delta) = sigma / (omega eps): regime of validity")
    print("   Low-loss formulas require tan(delta) << 1.  Here: tan(delta) = "
          "sigma / (2 pi f eps0 eps_r)")
    print("   sigma (S/m)  eps_r      f = 50 MHz   f = 100 MHz   f = 200 MHz   "
          "f = 400 MHz")
    for sigma in (1e-4, 1e-3, 1e-2, 1e-1):
        for eps_r in (4.0, 16.0):
            tans = [sigma / (2 * np.pi * f * EPS0_F_M * eps_r)
                    for f in (50e6, 100e6, 200e6, 400e6)]
            print(f"   {sigma:8.0e}   {eps_r:6.2f}   " +
                  "".join(f"{t:12.4f}  " for t in tans))
    print("   Reading the table: tan(delta) <= 0.1 (low-loss) holds for sigma up to")
    print("   about 1e-3 S/m at 100 MHz in a wet medium (eps_r = 16), and up to")
    print("   about 4e-3 S/m at 400 MHz in a dry medium (eps_r = 4) -- and only")
    print("   2.5e-4 S/m in the dry medium at 50 MHz.  Above that every low-loss")
    print("   formula in this module degrades and the dispersive full expressions")
    print("   are required.")

    section("4. Exact versus low-loss attenuation and speed (measured error)")
    f_hz, eps_r = 100e6, 9.0
    omega = 2.0 * np.pi * f_hz
    print(f"   f = {f_hz/1e6:.0f} MHz, eps_r = {eps_r:.1f}, "
          f"v_lowloss = {v_low_loss(eps_r):.5f} m/ns")
    print("   tan(delta)   alpha exact   alpha approx   err alpha    v exact    "
          "v approx   err v")
    for td in (0.01, 0.03, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0):
        sigma = td * omega * EPS0_F_M * eps_r
        a_ex, b_ex = exact_alpha_beta(eps_r, sigma, f_hz)
        a_ap = 0.5 * sigma * np.sqrt(MU0_H_M / (EPS0_F_M * eps_r))
        b_ap = omega * np.sqrt(MU0_H_M * EPS0_F_M * eps_r)
        v_ex = omega / b_ex / 1e9
        v_ap = omega / b_ap / 1e9
        print(f"   {td:9.2f}   {a_ex:11.4f}   {a_ap:12.4f}   "
              f"{(a_ap/a_ex - 1)*100:+8.2f}%   {v_ex:8.5f}   {v_ap:8.5f}   "
              f"{(v_ap/v_ex - 1)*100:+7.2f}%")
    print("   alpha in 1/m, v in m/ns.  Both approximations are accurate to better")
    print("   than 0.5% for tan(delta) <= 0.2 and to about 1% for tan(delta) = 0.3;")
    print("   at tan(delta) = 1 the speed is already 9.9% too high, and at")
    print("   tan(delta) = 2 it is 27.2% too high.  That is the honest boundary of")
    print("   v = c/sqrt(eps_r) and of alpha = (sigma/2) sqrt(mu/eps).")

    section("5. Ricker wavelet: measured spectrum versus analytic properties")
    f0 = 200e6                     # 200 MHz nominal antenna
    dt = 2.0e-11                   # 0.02 ns sampling
    n = 4096
    t = np.arange(n) * dt - 20e-9
    w = ricker(t, 0.0, f0)
    W = np.abs(np.fft.rfft(w))
    freqs = np.fft.rfftfreq(n, dt)
    ipeak = int(np.argmax(W))
    df = freqs[1] - freqs[0]
    # refine the peak by a parabolic fit on the three bins around the maximum
    y0, y1, y2 = W[ipeak - 1], W[ipeak], W[ipeak + 1]
    off = 0.5 * (y0 - y2) / (y0 - 2.0 * y1 + y2)
    f_peak = freqs[ipeak] + off * df
    f_mean = np.sum(freqs * W) / np.sum(W)
    f_std = np.sqrt(np.sum(W * (freqs - f_mean) ** 2) / np.sum(W))
    half = 0.5 * W.max()
    above = np.where(W >= half)[0]
    print(f"   f0 (design) = {f0/1e6:.1f} MHz, dt = {dt*1e9:.3f} ns, n = {n}")
    print(f"   spectral bin spacing        : {df/1e6:8.3f} MHz")
    print(f"   measured spectral peak      : {f_peak/1e6:8.3f} MHz "
          f"(analytic {f0/1e6:.3f}; the 195.312 MHz bin is "
          f"{freqs[ipeak]/1e6:.3f})")
    print(f"   measured mean frequency     : {f_mean/1e6:8.3f} MHz "
          f"(analytic {2/np.sqrt(np.pi)*f0/1e6:.3f} = 2/sqrt(pi) f0)")
    print(f"   measured rms bandwidth      : {f_std/1e6:8.3f} MHz "
          f"(analytic {np.sqrt(1.5 - 4/np.pi)*f0/1e6:.3f} = "
          f"sqrt(3/2 - 4/pi) f0)")
    print(f"   -6 dB band (|W| >= 0.5 peak): {freqs[above[0]]/1e6:.1f} to "
          f"{freqs[above[-1]]/1e6:.1f} MHz, fractional width "
          f"{(freqs[above[-1]]-freqs[above[0]])/f_peak:.3f}")
    i0 = np.argmax(np.abs(w))
    zc = t[np.where(np.diff(np.sign(w)) != 0)[0]]
    zc = zc[np.abs(zc) > 1e-9]
    print(f"   peak amplitude {w[i0]:+.4f} at t = {t[i0]*1e9:+.3f} ns")
    print(f"   measured first zero crossing at |t| = {abs(zc[0])*1e9:.4f} ns "
          f"(analytic 1/(sqrt(2) pi f0) = {1/(np.sqrt(2)*np.pi*f0)*1e9:.4f} ns)")
    print("   the Ricker zero crossing is NOT 1/(2 f0); that is the zero crossing")
    print("   of a sine.  Confusing the two changes a wavelength by a factor 1.11.")

    section("6. Two-layer SYNTHETIC model: times, amplitudes, depth conversion")
    eps_1, eps_2, eps_3 = 4.0, 9.0, 16.0     # dry sand / wet sand / saturated sand
    h_1 = 1.20                                # m, thickness of layer 1
    h_2 = 1.80                                # m, thickness of layer 2
    v1, v2, v3 = v_low_loss(eps_1), v_low_loss(eps_2), v_low_loss(eps_3)
    t1 = 2.0 * h_1 / v1          # ns, because v is in m/ns
    t2 = t1 + 2.0 * h_2 / v2     # ns
    R12 = reflection_coeff(eps_1, eps_2)
    R23 = reflection_coeff(eps_2, eps_3)
    print(f"   layer 1: eps_r = {eps_1:.1f}, v = {v1:.5f} m/ns, h = {h_1:.2f} m")
    print(f"   layer 2: eps_r = {eps_2:.1f}, v = {v2:.5f} m/ns, h = {h_2:.2f} m")
    print(f"   half-space: eps_r = {eps_3:.1f}, v = {v3:.5f} m/ns")
    print(f"   two-way time to interface 1: {t1:7.2f} ns   R12 = {R12:+.4f}")
    print(f"   two-way time to interface 2: {t2:7.2f} ns   R23 = {R23:+.4f}")
    print(f"   primary-reflection interval on the record: "
          f"{t2-t1:.2f} ns = {(t2-t1)*v2/2:.2f} m at v2")
    print("   depth conversion d = v t / 2, checked:")
    for t_pick_ns, v_use in ((t2, v2), (t2, v1), (t2, v1 * 1.1)):
        d = v_use * t_pick_ns / 2.0
        print(f"     pick {t_pick_ns:6.2f} ns, v = {v_use:.5f} m/ns -> "
              f"d = {d:6.3f} m")
    print("   A 10% velocity error moves that depth by 10%: the depth is a ratio,")
    print("   and the velocity is an assumption, not a measurement.")

    section("7. Sensitivity of the two-way time to a permittivity error")
    print("   t = 2 d sqrt(eps_r) / c, so dt/t = d(eps_r) / (2 eps_r).")
    d, eps_nom = 2.0, 9.0
    t_nom = 2.0 * d * np.sqrt(eps_nom) / C_M_NS
    print(f"   d = {d:.1f} m, eps_r = {eps_nom:.1f} -> t = {t_nom:.3f} ns")
    for deps in (-0.2, -0.1, 0.1, 0.2):
        t_new = 2.0 * d * np.sqrt(eps_nom * (1 + deps)) / C_M_NS
        print(f"     eps_r {deps*100:+5.1f}%  ->  t = {t_new:7.3f} ns  "
              f"({(t_new/t_nom - 1)*100:+6.2f}%)")
    print("   The time is detected; the permittivity is converted.  Half of a")
    print("   fractional permittivity error passes straight into the depth.")


if __name__ == "__main__":
    main()
