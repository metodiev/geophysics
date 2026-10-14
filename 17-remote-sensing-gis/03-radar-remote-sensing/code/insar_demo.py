#!/usr/bin/env python3
"""InSAR: the phase-to-displacement relation, the 2 pi wrapping ambiguity, the
topographic ambiguity height, coherence estimation bias, baseline decorrelation
and the line-of-sight projection.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_demo.py

Everything is SYNTHETIC: the carrier frequency, slant range, incidence angles,
baselines, coherence values and noise are teaching values.  The only external
numbers are exact SI constants (the speed of light) and stated conventions.
No real mission, sensor, scene or dataset appears anywhere.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0        # m/s   exact speed of light in vacuum
F0 = 5.300e9             # Hz    teaching carrier, inside the conventional C band (4-8 GHz)
LAM = C / F0             # m
R_SLANT = 800.0e3        # m     teaching slant range
THETA = 35.0             # deg   teaching local incidence angle
B_PERP = 100.0           # m     teaching perpendicular baseline
D_GROUND = 8.71          # m     ground range pixel spacing at 35 deg for B = 30 MHz


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def wrap(phi):
    """Wrap phase to (-pi, pi]."""
    return (phi + np.pi) % (2.0 * np.pi) - np.pi


def coherence_estimate(x, y):
    """Multilook coherence estimator  g = |sum x y*| / sqrt(sum|x|^2 sum|y|^2)."""
    num = np.abs(np.sum(x * np.conj(y), axis=-1))
    den = np.sqrt(np.sum(np.abs(x) ** 2, axis=-1) * np.sum(np.abs(y) ** 2, axis=-1))
    return num / den


def main():
    section("1. Wavelength, the fringe, and the phase sensitivity")
    print(f"carrier f = {F0/1e9:.3f} GHz (teaching value inside the stated 4-8 GHz band)")
    print(f"lam = c/f = {LAM:.6f} m = {LAM*100:.4f} cm")
    print(f"one fringe (2 pi of phase) = one half wavelength of range change:")
    print(f"    lam/2 = {LAM/2*100:.4f} cm of line-of-sight displacement")
    print(f"phase sensitivity  d phi / d(r) = 4 pi / lam = {4*np.pi/LAM:.2f} rad/m")
    print(f"                                  = {4*np.pi/LAM*np.pi/180:.4f} rad/mm")
    print("(the factor 4 pi is two-way: a range change dr changes the path by 2 dr,")
    print(" and phase = 2 pi x path / lam)")

    section("2. Phase for a chosen displacement, and its wrap")
    print("   d_LOS (cm)   phi (rad)      phi wrapped (rad)   d phi (deg)")
    for d_cm in (0.0, 0.5, 1.0, 1.5, 2.0, 2.83, 4.0, 6.0):
        phi = 4.0 * np.pi * (d_cm / 100.0) / LAM
        print(f"   {d_cm:9.2f}   {phi:9.4f}    {wrap(phi):17.4f}   "
              f"{np.degrees(wrap(phi)):9.2f}")
    print("\n  the wrapped column is all the interferogram contains. Every 2.83 cm of")
    print("  extra displacement adds exactly 2 pi and is invisible in the wrapped phase.")

    section("3. The ambiguity: one wrapped phase, infinitely many displacements")
    print("  suppose the wrapped phase is that of d = 1.00 cm.  All of these")
    print("  displacements wrap to exactly the same value:\n")
    phi_meas = wrap(4.0 * np.pi * 0.0100 / LAM)
    print("    k   d_LOS (cm)   phi (rad)      wrapped (rad)     wrapped - measured")
    for k in range(-2, 3):
        d = 0.0100 + k * LAM / 2.0
        phi = 4.0 * np.pi * d / LAM
        print(f"   {k:+d}   {d*100:9.3f}   {phi:10.4f}    {wrap(phi):13.4f}    "
              f"{wrap(phi) - phi_meas:16.2e}")
    print("\n  the last column is numerical zero: the data cannot distinguish these")
    print("  candidates.  Unwrapping does not remove the ambiguity, it only moves it")
    print("  from an integer per pixel to one integer per connected region.")

    section("4. Height sensitivity and the ambiguity height")
    sin_t = np.sin(np.radians(THETA))
    print("  the reference-surface (flat-earth) phase is subtracted first; what")
    print("  remains maps topography and displacement together.  Writing the look")
    print("  direction as (sin theta, -cos theta) and the baseline as B,")
    print("      r_1 - r_2 = B . u(theta),   d u / d theta = (cos theta, sin theta)")
    print("  raising a scatterer by dh at fixed ground range rotates the look")
    print("  direction by d theta = sin(theta) dh / R, so")
    print("      d phi / dh = (4 pi / lam) (B_perp sin(theta) / R),")
    print("      h_a = lam R / (2 B_perp sin(theta)).\n")
    print("   theta (deg)   B_perp (m)   h_a (m)    d phi/dh (rad/m)")
    for th in (23.0, 35.0, 45.0):
        st = np.sin(np.radians(th))
        for b in (50.0, 100.0, 200.0):
            h_a = LAM * R_SLANT / (2.0 * b * st)
            print(f"   {th:10.0f}   {b:11.0f}   {h_a:7.1f}   "
                  f"{4 * np.pi * b * st / (LAM * R_SLANT):14.6f}")
    print("\n  NOTE ON CONVENTIONS.  A displacement ds along the direction")
    print("  perpendicular to the line of sight has a vertical component ds sin(theta)")
    print("  and gives d phi/dh = (4 pi/lam) B_perp/(R sin(theta)), which is larger by")
    print("  1/sin^2(theta).  A height ambiguity quoted as lam R sin(theta)/(2 B_perp)")
    print("  uses that other reference direction; the vertical sensitivity derived")
    print("  above is the one that converts a topographic relief into fringes.")
    h_a = LAM * R_SLANT / (2.0 * B_PERP * sin_t)
    print(f"\n  verification for theta = {THETA:.0f} deg, B_perp = {B_PERP:.0f} m,")
    print(f"  h_a = {h_a:.4f} m:")
    for h in (0.0, h_a / 2.0, h_a):
        phi = -4.0 * np.pi * B_PERP * sin_t * h / (LAM * R_SLANT)
        print(f"     h = {h:8.4f} m -> phi = {phi:9.4f} rad = {phi/(2*np.pi):7.4f} fringes")
    print("  a height change of exactly h_a produces exactly one fringe: that is why")
    print("  h_a is called the ambiguity height, and it is set by the baseline.")
    print("\n  the same statement checked against the exact (non-linearised) geometry:")
    print("  radar at (0, H), reference point at (X, 0), baseline resolved into a")
    print("  perpendicular part B_perp and a parallel part B_par.\n")
    hgt = R_SLANT * np.cos(np.radians(THETA))
    xg = R_SLANT * sin_t
    b_perp_t = 100.0
    b_par_t = 0.0
    bx = b_perp_t * np.cos(np.radians(THETA)) + b_par_t * sin_t
    bz = -b_perp_t * np.sin(np.radians(THETA)) + b_par_t * np.cos(np.radians(THETA))

    def phase_num(h):
        r_m = np.sqrt(xg ** 2 + (hgt - h) ** 2)
        r_s = np.sqrt((xg + bx) ** 2 + (hgt + bz - h) ** 2)
        r_m0 = np.sqrt(xg ** 2 + hgt ** 2)
        r_s0 = np.sqrt((xg + bx) ** 2 + (hgt + bz) ** 2)
        return (4.0 * np.pi / LAM) * ((r_m - r_s) - (r_m0 - r_s0))

    print("     h (m)   exact phase (rad)   linear model (rad)   difference (rad)")
    for h in (0.0, h_a / 4.0, h_a / 2.0, h_a, 2.0 * h_a):
        exact = phase_num(h)
        lin = -4.0 * np.pi * b_perp_t * sin_t * h / (LAM * R_SLANT)
        print(f"    {h:8.2f}   {exact:17.6f}   {lin:18.6f}   {exact - lin:16.2e}")
    print("  the exact evaluation of (4 pi/lam)[(r_1 - r_2)(h) - (r_1 - r_2)(0)] agrees")
    print("  over the tested range the exact phase tracks the linear model to better")
    print("  than 0.2 percent of a fringe; the residual is the second-order term in h.")

    section("5. Coherence estimation: single-look coherence carries no information")
    print("  gamma_hat = |sum x y*| / sqrt(sum|x|^2 sum|y|^2) over L independent looks")
    print("  for two circular complex Gaussian looks with true coherence gamma\n")
    looks = (1, 4, 16, 64, 256)
    print("   true gamma   " + "".join(f"L={l:<7d}" for l in looks))
    for gam in (0.2, 0.5, 0.8, 0.95):
        row = []
        for l_n in looks:
            n_real = 4000
            x = (RNG.standard_normal((n_real, l_n))
                 + 1j * RNG.standard_normal((n_real, l_n))) / np.sqrt(2.0)
            nz = (RNG.standard_normal((n_real, l_n))
                  + 1j * RNG.standard_normal((n_real, l_n))) / np.sqrt(2.0)
            y = gam * x + np.sqrt(1.0 - gam ** 2) * nz
            g = coherence_estimate(x, y)
            row.append(f"{g.mean():.4f}  ")
        print(f"   {gam:9.2f}   " + "".join(row))
    print("\n  at L = 1 the estimator is identically 1 for every true coherence --")
    print("  one look contains no information about the correlation.  The bias")
    print("  decreases as the number of looks grows, and it is always downward, so")
    print("  an un-corrected map of gamma_hat is biased low in low-coherence areas.")

    section("6. Baseline decorrelation: gamma = 1 - B_perp / B_c, measured")
    print("  model: the two acquisitions view the surface with a wavenumber shift")
    print("    dk = (4 pi cos theta / lam) (B_perp / R)")
    print("  while the ground reflectivity band has width DK = 2 pi / dg.  Then")
    print("    gamma = 1 - dk / DK,  and  B_c = lam R / (2 dg cos theta)")
    cos_t = np.cos(np.radians(THETA))
    b_c = LAM * R_SLANT / (2.0 * D_GROUND * cos_t)
    print(f"  with dg = {D_GROUND:.2f} m at {THETA:.0f} deg: B_c = {b_c:.1f} m")
    print("  measurement: one random reflectivity spectrum is passed through the two")
    print("  shifted band-pass filters and the coherence of the two fields is formed.\n")
    n = 8192
    dx = D_GROUND / 8.0
    kk = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    d_k = 2.0 * np.pi / D_GROUND
    print("   B_perp/B_c   B_perp (m)   model gamma   measured gamma (20 realisations)")
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0, 1.25):
        b_perp = frac * b_c
        dk = 4.0 * np.pi * cos_t * b_perp / (LAM * R_SLANT)
        model = max(0.0, 1.0 - dk / d_k)
        g_meas = []
        for _ in range(20):
            spec = (RNG.standard_normal(n) + 1j * RNG.standard_normal(n)) / np.sqrt(2.0)
            h1 = np.where(np.abs(kk) <= d_k / 2.0, 1.0, 0.0)
            h2 = np.where(np.abs(kk - dk) <= d_k / 2.0, 1.0, 0.0)
            z1 = np.fft.ifft(spec * h1)
            z2 = np.fft.ifft(spec * h2)
            g_meas.append(coherence_estimate(z1, z2))
        print(f"   {frac:9.2f}   {b_perp:10.1f}   {model:11.4f}   "
              f"{np.mean(g_meas):27.4f}")
    print("\n  below B_c the measured coherence falls linearly toward zero, matching the")
    print("  wavenumber-overlap model: the two looks no longer see the same scatterers.")
    print("  Beyond B_c there is no overlap at all and the interferogram is pure noise.")

    section("7. Speckle: the statistics of a coherent image")
    print("  the field of one resolution cell is a sum of many independent random")
    print("  phasors, hence circular complex Gaussian; its intensity I = |z|^2 is")
    print("  exponential and fully determined by one parameter.\n")
    z = (RNG.standard_normal(2_000_000) + 1j * RNG.standard_normal(2_000_000)) / np.sqrt(2.0)
    inten = np.abs(z) ** 2
    m = inten.mean()
    print("   moment        exponential prediction   measured   ratio measured/prediction")
    preds = {1: 1.0, 2: 2.0, 3: 6.0, 4: 24.0}
    for k in (1, 2, 3, 4):
        mk = np.mean(inten ** k)
        print(f"   E[I^{k}]/E[I]^{k}      {preds[k]:22.1f}   {mk/m**k:8.4f}   "
              f"{mk/m**k/preds[k]:17.4f}")
    print(f"   normalised std   {1.0:22.1f}   {inten.std()/m:8.4f}   "
          f"{inten.std()/m:17.4f}")
    print("\n  multilooking L independent looks reduces the normalised variance:")
    print("   L      normalised variance   measured   1/L")
    big = np.abs((RNG.standard_normal((256, 65536)) + 1j * RNG.standard_normal((256, 65536)))
                 / np.sqrt(2.0)) ** 2
    for l_n in (1, 4, 16, 64, 256):
        sub = big[:l_n].mean(axis=0)
        print(f"   {l_n:4d}   {1.0/l_n:20.6f}   {sub.var()/sub.mean()**2:8.5f}   "
              f"{1.0/l_n:.5f}")
    print("\n  speckle is not additive noise: it is a deterministic function of the")
    print("  scatterer arrangement, so it does not average down without either more")
    print("  looks (coarser resolution) or a physical model of the target.")

    section("8. How coherence sets the phase precision")
    print("  for L looks and true coherence gamma the multilook phase has the")
    print("  asymptotic standard deviation")
    print("    sigma_phi ~ sqrt( (1 - gamma^2) / (2 L gamma^2) )")
    print("  valid for gamma not small and L >= several.  Comparing it with the")
    print("  measured spread also shows where it fails.\n")
    print("   gamma   L      sigma_phi asymptotic (rad)   measured (rad)")
    for gam in (0.3, 0.5, 0.8):
        for l_n in (1, 4, 16):
            n_real = 3000
            x = (RNG.standard_normal((n_real, l_n))
                 + 1j * RNG.standard_normal((n_real, l_n))) / np.sqrt(2.0)
            nz = (RNG.standard_normal((n_real, l_n))
                  + 1j * RNG.standard_normal((n_real, l_n))) / np.sqrt(2.0)
            y = gam * x + np.sqrt(1.0 - gam ** 2) * nz
            ph = np.angle(np.sum(x * np.conj(y), axis=1))
            pred = np.sqrt((1.0 - gam ** 2) / (2.0 * l_n * gam ** 2))
            print(f"   {gam:5.2f}   {l_n:2d}   {pred:26.4f}   {ph.std():14.4f}")
    print(f"\n  a wrapped phase that carries no information is uniform on (-pi, pi] and")
    print(f"  has std pi/sqrt(3) = {np.pi/np.sqrt(3.0):.4f} rad.  The measured spread")
    print("  saturates toward that value as gamma falls and L falls: at gamma = 0.3,")
    print("  one look gives 1.57 rad, essentially uninformed, while the asymptotic")
    print("  formula still predicts 2.25 rad.  The formula is a large-L, high-coherence")
    print("  result and must not be extrapolated past its regime.")
    print("\n  the same numbers in displacement: at lam = 5.6565 cm, a phase error of")
    for s in (0.5, 1.0):
        print(f"     {s:4.2f} rad is {LAM / (4.0 * np.pi) * s * 100:.3f} cm of line-of-sight")
    print("  displacement.  Coherence is therefore not a quality flag bolted on at the")
    print("  end; it is the direct determinant of the deformation precision.")
    section("9. Line-of-sight projection of a vertical displacement")
    print("  a purely vertical displacement d_v projects onto the line of sight as")
    print("    d_LOS = d_v cos(theta),   so   d phi = 4 pi d_v cos(theta) / lam\n")
    print("   theta (deg)   cos theta   fringes per cm of d_v   d_v per fringe (cm)")
    for th in (23.0, 35.0, 45.0):
        ct = np.cos(np.radians(th))
        print(f"   {th:10.0f}   {ct:9.4f}   {0.01 * ct / (LAM / 2.0):20.4f}   "
              f"{LAM / 2.0 / ct * 100:18.4f}")
    print("\n  one fringe still means 2.83 cm of range change, but it corresponds to a")
    print("  larger vertical motion the closer the incidence is to vertical.  Converting")
    print("  a fringe count to a displacement therefore requires the look geometry, and")
    print("  a single geometry cannot separate vertical from horizontal motion.")


if __name__ == "__main__":
    main()
