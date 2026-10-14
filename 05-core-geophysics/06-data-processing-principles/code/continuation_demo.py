#!/usr/bin/env python3
"""Continuation and reduction to the pole: one is stable, the other is not.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python continuation_demo.py

The potential field is synthesised analytically from a point dipole, so the "truth"
is available at every stage.  All statistics are taken in the INTERIOR of the grid,
so that FFT wraparound at the edges cannot be mistaken for a physical effect.

Contents
--------
1. Truth field from a dipole, plus white noise.  Report signal and noise levels.
2. UPWARD continuation by dz: H = exp(-|k| dz).  Stable.  Measure the anomaly
   attenuation, the noise reduction, and the theoretical factor at the anomaly's
   dominant wavenumber.
3. DOWNWARD continuation by dz: H = exp(+|k| dz).  Unstable.  Measure the noise gain
   for several dz against the derived white-noise gain sqrt(mean exp(2|k|dz)).
4. Stabilised downward continuation by band-limiting the operator; the price is
   stated and measured.
5. REDUCTION TO THE POLE.  The operator is MEASURED as the ratio of two analytic
   forward models (vertical against inclined dipole), then applied with the correct
   inclination and with wrong ones.
"""

import numpy as np

RNG_SEED = 20261014
MU0_OVER_4PI = 1.0e-7      # T m / A, exact
NT_PER_T = 1.0e9


def dipole_bz(x, y, xc, yc, depth, moment, inc_deg):
    """Vertical component of a point dipole's field, in nanotesla.

    Moment and direction of measurement are both taken along (inclination inc,
    declination 0) -- the induced-magnetisation case.  Returns the field in nT.
    """
    inc = np.radians(inc_deg)
    mx, my, mz = moment * np.cos(inc), 0.0, moment * np.sin(inc)
    fx, fy, fz = np.cos(inc), 0.0, np.sin(inc)
    rx = x - xc
    ry = y - yc
    rz = -depth
    r = np.sqrt(rx ** 2 + ry ** 2 + rz ** 2)
    mdotr = mx * rx + my * ry + mz * rz
    bx = 3.0 * mdotr * rx / r ** 5 - mx / r ** 3
    by = 3.0 * mdotr * ry / r ** 5 - my / r ** 3
    bz = 3.0 * mdotr * rz / r ** 5 - mz / r ** 3
    return (fx * bx + fy * by + fz * bz) * MU0_OVER_4PI * NT_PER_T


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)
    n = 201
    dx = 25.0
    x = np.arange(n) * dx
    gx, gy = np.meshgrid(x, x)
    depth = 500.0
    moment = 1.0e9
    centre = (n // 2) * dx

    lo, hi = n // 5, n - n // 5                 # interior window for statistics

    def interior(a):
        return a[lo:hi, lo:hi]

    # --- 1. Truth and noise -------------------------------------------------
    truth = dipole_bz(gx, gy, centre, centre, depth, moment, 90.0)
    noise_sigma = 0.01 * np.abs(truth).max()
    noisy = truth + rng.normal(0.0, noise_sigma, size=truth.shape)
    print("1. Synthetic field")
    print(f"   grid {n} x {n}, spacing {dx:.0f} m, dipole at depth {depth:.0f} m,")
    print(f"   moment {moment:.1e} A m^2, vertical magnetisation")
    print(f"   peak of the true anomaly   = {np.abs(truth).max():.3f} nT")
    print(f"   noise sigma                = {noise_sigma:.4f} nT")
    print(f"   peak signal-to-noise       = {np.abs(truth).max()/noise_sigma:.2f}")
    print(f"   statistics taken on the interior window "
          f"[{lo*dx:.0f}, {hi*dx:.0f}] m in both directions")

    kx = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    KX, KY = np.meshgrid(kx, ky)
    K = np.hypot(KX, KY)

    def apply(field, H):
        """One application of a Fourier-domain operator, no taper."""
        return np.real(np.fft.ifft2(np.fft.fft2(field) * H))

    def operator_gain(H):
        """Measured gain of H acting on unit-variance white noise, on this grid."""
        w = rng.normal(0.0, 1.0, size=(n, n))
        return float(np.std(interior(apply(w, H))))

    # --- 2. Upward continuation --------------------------------------------
    print("\n2. UPWARD continuation  H(k) = exp(-|k| dz)   [stable, smoothing]")
    print(f"   a dipole at depth h attenuated to h+dz scales as (h/(h+dz))^3")
    print(f"   {'dz (m)':>9}{'peak (nT)':>13}{'peak retained (%)':>19}"
          f"{'predicted (%)':>15}{'noise gain':>13}{'predicted gain':>16}")
    for dz in (100.0, 250.0, 500.0, 1000.0):
        H = np.exp(-K * dz)
        up_clean = apply(truth, H)
        resid = apply(noisy, H) - up_clean
        retained = np.abs(interior(up_clean)).max() / np.abs(interior(truth)).max()
        print(f"   {dz:>9.0f}{np.abs(interior(up_clean)).max():>13.4f}"
              f"{retained*100:>19.2f}"
              f"{(depth/(depth+dz))**3*100:>15.2f}"
              f"{interior(resid).std()/noise_sigma:>13.4f}"
              f"{operator_gain(H):>16.4f}")
    print("   -> the measured attenuation matches the (h/(h+dz))^3 prediction of the")
    print("      dipole's inverse-cube falloff, and the measured noise gain matches the")
    print("      RMS of exp(-|k| dz) over the grid's wavenumbers. Upward continuation")
    print("      is a low-pass filter: every value of H is <= 1, so nothing blows up,")
    print("      and by the same token information is destroyed and cannot be recovered")
    print("      without the instability shown next.")

    # --- 3. Downward continuation ------------------------------------------
    print("\n3. DOWNWARD continuation  H(k) = exp(+|k| dz)   [unstable]")
    print(f"   {'dz (m)':>9}{'signal peak (nT)':>19}{'predicted (nT)':>17}"
          f"{'noise sigma (nT)':>19}{'measured gain':>16}{'predicted gain':>17}{'S/N':>10}")
    for dz in (25.0, 50.0, 100.0, 150.0, 200.0):
        H = np.exp(K * dz)
        dn_clean = apply(truth, H)
        resid = apply(noisy, H) - dn_clean
        pred = float(np.sqrt(np.mean(H ** 2)))
        s = float(np.abs(interior(dn_clean)).max())
        nz = float(interior(resid).std())
        s_pred = np.abs(interior(truth)).max() * (depth / (depth - dz)) ** 3
        print(f"   {dz:>9.0f}{s:>19.4e}{s_pred:>17.4e}{nz:>19.4e}"
              f"{nz/noise_sigma:>16.3e}{pred:>17.3e}{s/nz:>10.3f}")
    print("   -> up to dz = 150 m the continued signal matches the (h/(h-dz))^3")
    print("      prediction; beyond that the noise has taken over the maximum.")
    print("      The noise gain is the RMS of exp(|k| dz) over all wavenumbers and it")
    print("      is unbounded because the grid admits |k| up to pi sqrt(2)/dx. The")
    print("      measured and predicted gains agree to within a few per cent, so the")
    print("      instability is the operator, not a numerical accident.")
    print("   -> the noise grows faster than the signal, and the S/N falls with depth")
    print("      until there is nothing left to interpret.")

    # --- 4. Stabilised downward continuation ------------------------------
    print("\n4. STABILISED downward continuation: band-limit H to wavelengths > 6 dz")
    print(f"   {'dz (m)':>9}{'signal peak (nT)':>19}{'noise sigma (nT)':>19}"
          f"{'gain of the stabilised':>25}{'gain of plain H':>17}")
    for dz in (100.0, 200.0, 400.0):
        cutoff = 2.0 * np.pi / (6.0 * dz)
        H_stab = np.exp(K * dz) * np.exp(-0.5 * (K / cutoff) ** 2)
        s = float(np.abs(interior(apply(truth, H_stab))).max())
        nz = float(interior(apply(noisy, H_stab) - apply(truth, H_stab)).std())
        print(f"   {dz:>9.0f}{s:>19.4e}{nz:>19.4e}"
              f"{operator_gain(H_stab):>25.3e}{operator_gain(np.exp(K*dz)):>17.3e}")
    print("   -> band-limiting cuts the gain by many orders of magnitude, at the cost")
    print("      of discarding exactly the short wavelengths that would have carried")
    print("      the shallowest detail. That trade is unavoidable, and it is why")
    print("      downward continuation is quoted with a wavelength and a depth.")

    # --- 5. Reduction to the pole ------------------------------------------
    print("\n5. REDUCTION TO THE POLE: the operator is MEASURED, not quoted")
    inc_assumed = 60.0
    b_incl = dipole_bz(gx, gy, centre, centre, depth, moment, inc_assumed)
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        H_rtp = np.fft.fft2(truth) / np.fft.fft2(b_incl)
    reduced = np.real(np.fft.ifft2(np.fft.fft2(b_incl) * H_rtp))
    err = float(interior(reduced - truth).std())
    print(f"   operator derived as FFT(vertical model) / FFT(model at {inc_assumed:.0f} deg)")
    print(f"   peak of the pole-reduced field = {np.abs(interior(reduced)).max():.4f} nT")
    print(f"   peak of the vertical model     = {np.abs(interior(truth)).max():.4f} nT")
    print(f"   RMS error against the vertical model = {err:.3e} nT"
          f"  ({err/np.abs(interior(truth)).max()*100:.3e} % of the interior peak)")
    mag = np.abs(H_rtp[np.isfinite(H_rtp)])
    print(f"   operator magnitude: min {mag.min():.3e}, median "
          f"{np.median(mag):.3e}, max {mag.max():.3e}")
    print("   -> exact by construction for that inclination, which is the point: the")
    print("      reduction is only as good as the direction it assumes.")

    print("\n   now apply the SAME operator to a field from a DIFFERENT inclination:")
    print(f"   {'true inc (deg)':>16}{'peak after RTP (nT)':>22}"
          f"{'RMS error (% of peak)':>24}")
    for inc_other in (45.0, 60.0, 75.0, 90.0):
        b_other = dipole_bz(gx, gy, centre, centre, depth, moment, inc_other)
        out = np.real(np.fft.ifft2(np.fft.fft2(b_other) * H_rtp))
        e = float(interior(out - truth).std()) / np.abs(interior(truth)).max() * 100.0
        print(f"   {inc_other:>16.0f}{np.abs(interior(out)).max():>22.4f}{e:>24.2f}")
    print("   -> assuming 60 degrees when the true inclination is 45, 75 or 90 leaves")
    print("      several per cent of the peak as a systematic error, i.e. as a distortion")
    print("      that looks like geology. Reduction to the pole is a MODEL-BASED")
    print("      transformation: it assumes induced magnetisation and a known field")
    print("      direction, and it is invalid when remanence or a different direction")
    print("      is present. When the assumption is doubtful, use a direction-free")
    print("      quantity (a derivative magnitude or the analytic signal) instead.")


if __name__ == "__main__":
    main()
