"""Surface-wave dispersion: the fundamental mode, its limits and its ambiguity.

Run:  .venv/bin/python masw_dispersion_demo.py
Requires: numpy.

Companion to lesson 06-10-04.

Love waves are used rather than Rayleigh waves because the Love-wave dispersion
relation for one layer over a half-space is a single transcendental equation with
a closed form, so the derivation in the lesson can be checked numerically without
a Thomson-Haskell implementation.  The physics that the lesson attributes to
surface-wave dispersion in general -- the mode exists, its velocity is bounded by
the layer and the half-space velocities, it is more sensitive to the layer near
the free surface, and thickness and velocity trade off -- is all present in this
one equation.

Sections.

1.  The dispersion relation solved for the fundamental mode, plus its two exact
    limits: c(f) -> vs2 as f -> 0 and c(f) -> vs1 as f -> infinity.
2.  Phase velocity versus frequency for a stated SYNTHETIC model, with the
    wavelength and the standard depth-estimate lambda/3 tabulated.
3.  The Jacobian of the dispersion curve with respect to (H, vs1, vs2), and the
    correlation between its columns: the thickness-velocity trade-off measured.
4.  A grid search over (H, vs1) that shows the trade-off ridge explicitly.
5.  The resolution trade-off: what a short spread can and cannot constrain.
"""

from __future__ import annotations

import numpy as np

VS1 = 200.0     # m/s  layer
VS2 = 800.0     # m/s  half-space
RHO1 = 1800.0   # kg/m^3
RHO2 = 2000.0   # kg/m^3
H = 10.0        # m
MU1 = RHO1 * VS1 ** 2
MU2 = RHO2 * VS2 ** 2


def banner(title: str) -> None:
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def love_phase_velocity(f, vs1=VS1, vs2=VS2, mu1=MU1, mu2=MU2, h=H,
                        n_scan=30001):
    """Fundamental-mode Love phase velocity at frequency f (Hz).

    Substituting x = omega H sqrt(1/vs1^2 - 1/c^2) turns the dispersion
    relation into

        sin x - (mu2/mu1) sqrt(1/c^2 - 1/vs2^2)/sqrt(1/vs1^2 - 1/c^2) cos x = 0,

    which has no poles.  The roots are the modes in order: the smallest root
    is the fundamental, and higher roots are the higher modes, which are
    faster at the same frequency.
    """
    w = 2.0 * np.pi * f
    a = 1.0 / vs1 ** 2 - 1.0 / vs2 ** 2
    x_max = w * h * np.sqrt(a)
    x = np.linspace(1e-12, x_max, n_scan)
    s1 = x / (w * h)
    s2 = np.sqrt(np.clip(1.0 / vs1 ** 2 - s1 ** 2 - 1.0 / vs2 ** 2, 0.0, None))
    r = (mu2 / mu1) * s2 / np.where(s1 > 0.0, s1, 1e-300)
    g = np.sin(x) - r * np.cos(x)
    sign_change = np.nonzero(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]
    if sign_change.size == 0:
        return np.nan, np.nan
    k = sign_change[0]                      # smallest root = fundamental mode
    x0, x1 = x[k], x[k + 1]
    g0, g1 = g[k], g[k + 1]
    x_root = x0 - g0 * (x1 - x0) / (g1 - g0)
    inv_c2 = 1.0 / vs1 ** 2 - (x_root / (w * h)) ** 2
    if inv_c2 <= 0.0:
        return np.nan, np.nan
    return 1.0 / np.sqrt(inv_c2), x_root


def dispersion_curve(freqs, **kw):
    return np.array([love_phase_velocity(f, **kw)[0] for f in freqs])


def main():
    print("06-10-04 MASW / surface-wave dispersion -- SYNTHETIC model")
    print(f"  layer   : vs1 = {VS1:.0f} m/s, rho1 = {RHO1:.0f} kg/m^3,"
          f" H = {H:.1f} m")
    print(f"  halfspace: vs2 = {VS2:.0f} m/s, rho2 = {RHO2:.0f} kg/m^3")
    print(f"  rigidity ratio mu2/mu1 = {MU2 / MU1:.3f} (dimensionless)")

    banner("1. The two exact limits of the dispersion relation")
    print("      f (Hz)   c (m/s)   c/vs2   c/vs1")
    for f in (0.01, 0.1, 1.0, 10.0, 100.0, 1000.0):
        c, _ = love_phase_velocity(f)
        print(f"    {f:8.2f}  {c:8.3f}  {c / VS2:7.5f}  {c / VS1:7.4f}")
    print(f"  as f -> 0 the phase velocity must approach vs2 = {VS2:.0f} m/s,")
    print(f"  and at f = 0.01 Hz the computed value is within"
          f" {abs(love_phase_velocity(0.01)[0] - VS2) / VS2 * 100:.4f} % of it.")
    print(f"  as f -> infinity it must approach vs1 = {VS1:.0f} m/s, and at")
    print(f"  f = 1000 Hz the computed value is within"
          f" {abs(love_phase_velocity(1000.0)[0] - VS1) / VS1 * 100:.4f} % of it.")
    print("  -> the phase velocity is bounded by the two body-wave velocities,")
    print("     so a dispersion curve alone cannot produce a velocity outside")
    print("     that bracket.  Record it accurately and it still cannot.")

    banner("2. Phase velocity, wavelength and the lambda/3 depth estimate")
    freqs = np.array([2.0, 5.0, 10.0, 20.0, 30.0, 50.0])
    print("      f (Hz)   c (m/s)   lambda (m)   lambda/3 (m)   c/2f (m)")
    for f in freqs:
        c = float(love_phase_velocity(f)[0])
        lam = c / f
        print(f"    {f:8.1f}  {c:8.2f}  {lam:11.2f}  {lam / 3:13.2f}"
              f"  {c / (2 * f):10.2f}")
    print("  -> the depth estimate lambda/3 is a rule of thumb, not a")
    print("     derivation: it is the depth at which the mode's sensitivity")
    print("     peaks, and it moves with frequency, which is what makes the")
    print("     method a sounding rather than a single measurement.")

    banner("3. The Jacobian: which parameter does the curve constrain?")
    base = dispersion_curve(freqs)
    jac = np.zeros((freqs.size, 3))
    for j, (name, value) in enumerate((("h", H), ("vs1", VS1),
                                       ("vs2", VS2))):
        eps = 1e-4 * value
        kw_hi = {name: value + eps}
        kw_lo = {name: value - eps}
        jac[:, j] = (dispersion_curve(freqs, **kw_hi)
                     - dispersion_curve(freqs, **kw_lo)) / (2 * eps)
    rel = jac * np.array([H, VS1, VS2]) / base[:, None]
    print("  relative sensitivity (dln c / dln p) at each frequency:")
    print("      f (Hz)   dln c/dln H   dln c/dln vs1   dln c/dln vs2")
    for k, f in enumerate(freqs):
        print(f"    {f:8.1f}  {rel[k, 0]:13.5f}  {rel[k, 1]:14.5f}"
              f"  {rel[k, 2]:14.5f}")
    corr = np.corrcoef(rel.T)
    print(f"  correlation between the H column and the vs1 column:"
          f" {corr[0, 1]:+.6f}")
    print(f"  correlation between the H column and the vs2 column:"
          f" {corr[0, 2]:+.6f}")
    sv = np.linalg.svd(rel, compute_uv=False)
    print(f"  singular values of the 6 x 3 relative-sensitivity matrix:"
          f" {np.array2string(sv, precision=5)}")
    print(f"  condition number = {sv[0] / sv[-1]:.3e}")
    print("  -> the H and vs1 columns are almost perfectly anticorrelated over")
    print("     this band: a thinner layer with a faster velocity produces the")
    print("     same curve as a thicker layer with a slower one.  The two are")
    print("     separated only where the fundamental mode feels the half-space")

    banner("4. The trade-off ridge, by grid search")
    rng = np.random.default_rng(7)
    noise = 0.03                     # 3 % relative error on phase velocity
    h_grid = np.arange(4.0, 20.01, 0.5)
    v_grid = np.arange(140.0, 300.1, 5.0)
    print(f"  SYNTHETIC target curve from H = {H:.1f} m, vs1 = {VS1:.0f} m/s,")
    print(f"  vs2 = {VS2:.0f} m/s, perturbed by {noise * 100:.0f} % independent")
    print(f"  relative errors on each frequency.  A model is acceptable if its")
    print(f"  RMS misfit is below the noise level, i.e. below"
          f" {noise * 100:.0f} %.")
    print(f"  grid: H in {h_grid[0]:.1f}-{h_grid[-1]:.1f} m step 0.5 m,"
          f" vs1 in {v_grid[0]:.0f}-{v_grid[-1]:.0f} m/s step 5 m/s"
          f" ({h_grid.size * v_grid.size} models)")
    for label, band in (("short spread  (8-40 Hz)",
                         np.array([8.0, 10.0, 12.0, 15.0, 20.0, 25.0, 30.0, 40.0])),
                        ("wide band     (1-10 Hz)",
                         np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0])),
                        ("both bands   (1-40 Hz)",
                         np.array([1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 20.0, 40.0]))):
        target = dispersion_curve(band) * (1.0 + rng.normal(0.0, noise, band.size))
        accepted = []
        for h in h_grid:
            for v in v_grid:
                curve = dispersion_curve(band, h=h, vs1=v)
                rms = float(np.sqrt(np.mean(((curve - target) / target) ** 2)))
                if rms <= noise:
                    accepted.append((h, v, rms))
        accepted = np.array(accepted)
        print()
        print(f"  {label}: {accepted.shape[0]} of"
              f" {h_grid.size * v_grid.size} models acceptable")
        if accepted.shape[0] > 1:
            print(f"    H   : {accepted[:, 0].min():6.2f} to"
                  f" {accepted[:, 0].max():6.2f} m   (half-width"
                  f" {0.5 * (accepted[:, 0].max() - accepted[:, 0].min()):.2f} m)")
            print(f"    vs1 : {accepted[:, 1].min():6.1f} to"
                  f" {accepted[:, 1].max():6.1f} m/s (half-width"
                  f" {0.5 * (accepted[:, 1].max() - accepted[:, 1].min()):.1f} m/s)")
            print(f"    correlation between accepted H and vs1:"
                  f" {np.corrcoef(accepted[:, 0], accepted[:, 1])[0, 1]:+.4f}")
            best = accepted[np.argmin(accepted[:, 2])]
            print(f"    best fit on the grid: H = {best[0]:.2f} m,"
                  f" vs1 = {best[1]:.1f} m/s, RMS misfit"
                  f" {best[2] * 100:.3f} %")
    print("  -> at 3 % noise the acceptable set is a ridge, not a point, and")
    print("     the ridge runs along increasing H with increasing vs1: a")
    print("     thicker layer with a faster velocity fits the same curve as a")
    print("     thinner, slower one.  That is the thickness-velocity ambiguity")
    print("     of surface-wave inversion, and its width is set by the noise,")
    print("     not by the algorithm.  Widening the frequency band narrows the")
    print("     ridge because the low frequencies are where the mode feels the")
    print("     layer and the high frequencies are where it feels vs1.")

    banner("5. Resolution: what the spread length limits")
    print("  the standard rule of thumb is that reliable dispersion is")
    print("  available up to a wavelength comparable to the source-receiver")
    print("  offset, and that the mode averages the structure to about")
    print("  lambda/3.  Both are empirical; the numbers below apply them")
    print("  consistently rather than claiming they are physics.")
    print("      offset (m)   lambda_max (m)   f_min (Hz)   z_max = lambda/3")
    for L in (5.0, 10.0, 20.0, 50.0):
        lam_max = 2.0 * L          # generous: two offsets
        f_scan = np.logspace(-1, 3, 1200)
        c_scan = dispersion_curve(f_scan)
        ok = (c_scan / f_scan) <= lam_max
        f_min = float(f_scan[ok][0]) if ok.any() else np.nan
        print(f"    {L:10.1f}   {lam_max:13.1f}   {f_min:11.4f}"
              f"   {lam_max / 3:13.2f}")
    print("  -> a short spread misses the low frequencies, the low frequencies")
    print("     are the long wavelengths, and the long wavelengths are the only")
    print("     ones that feel the half-space.  A short spread therefore")
    print("     constrains a thin, fast layer and a thick, slow one equally")
    print("     well, which is the same statement as section 3.")
    print()
    print("done")


if __name__ == "__main__":
    main()
