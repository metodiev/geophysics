"""Spectroscopy principles for remote sensing.

Run:  python3 spectroscopy_demo.py
Requires: Python standard library only.

Companion to lesson 02-10-04.

The demo works on a *synthetic* reflectance spectrum built from a continuum
and a few Gaussian absorption features.  The feature positions used in the
synthetic spectrum are chosen to sit where real mineral absorption features
are commonly reported (see the lesson for nominal ranges and the pointer to
a spectral library); they are illustrative here, not measurements of any
sample.  Nothing in this script is a claim about a real rock.

The script:

1. Builds a reflectance spectrum on a 1 nm grid and defines the continuum,
   the band depth and the band centre both before and after continuum
   removal.
2. Convolves the spectrum with Gaussian instrument response functions of
   several widths and measures how much band depth and band contrast survive:
   the quantitative statement of why spectral resolution matters.
3. Re-samples the spectrum on coarser grids to show the separate effect of
   sampling, as distinct from resolution.
4. Computes wavenumber positions, spectral resolution R = lambda/dlambda and
   the relation between a band depth and an optical depth through
   Beer-Lambert.
5. Demonstrates derivative spectroscopy: an additive offset is removed by a
   first derivative and a linear offset by a second derivative, and the
   located band centre is unaffected.
6. Computes a normalised difference index from two bands and shows how it
   responds to a change in continuum level, which is why indices are used
   rather than single-band radiances.
7. Converts the reflectance spectrum into an emissivity spectrum with
   Kirchhoff's law, eps = 1 - rho, and computes the spectral contrast of the
   resulting emissivity feature, the quantity a thermal infrared spectrometer
   measures.
"""

import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ------------------------------------------------------- synthetic spectrum
LAM_MIN, LAM_MAX, DLAM = 0.40e-6, 2.50e-6, 1e-9


def continuum(lam):
    """A smooth, gently rising background reflectance."""
    return 0.28 + 0.10 * (lam - LAM_MIN) / (LAM_MAX - LAM_MIN)


FEATURES = (
    # (centre in metres, Gaussian sigma in metres, peak absorption depth)
    (0.90e-6, 0.090e-6, 0.22),   # iron-oxide-like broad feature
    (1.40e-6, 0.045e-6, 0.18),   # water/hydroxyl-like
    (1.90e-6, 0.060e-6, 0.28),   # water-like
    (2.20e-6, 0.022e-6, 0.30),   # Al-OH-like, narrow
    (2.33e-6, 0.030e-6, 0.24),   # carbonate-like
)


def reflectance(lam):
    r = continuum(lam)
    for c, sigma, depth in FEATURES:
        r *= 1.0 - depth * math.exp(-0.5 * ((lam - c) / sigma) ** 2)
    return r


def make_grid(step_nm, offset_frac=0.0):
    """Sample wavelengths in metres, optionally offset by a fraction of a step."""
    step = step_nm * 1e-9
    start = LAM_MIN + offset_frac * step
    n = int(math.floor((LAM_MAX - start) / step)) + 1
    return [start + i * step for i in range(n)]


def gaussian_kernel(fwhm_m, step_m=1e-9):
    sigma = fwhm_m / 2.3548200450309493
    half = int(math.ceil(4.0 * sigma / step_m))
    kern = [math.exp(-0.5 * (i * step_m / sigma) ** 2)
            for i in range(-half, half + 1)]
    total = sum(kern)
    return [k / total for k in kern]


def convolve(values, kernel):
    half = len(kernel) // 2
    n = len(values)
    out = []
    for i in range(n):
        acc = 0.0
        for j, k in enumerate(kernel):
            idx = i + j - half
            idx = 0 if idx < 0 else (n - 1 if idx >= n else idx)
            acc += k * values[idx]
        out.append(acc)
    return out


def band_metrics(lams, refl, lo, hi, centre):
    """Continuum, depth and centre of a band between lo and hi (m).

    The continuum is the straight line joining the reflectance at lo and hi;
    depth is 1 - R(centre)/continuum(centre) after continuum removal.
    """
    inside = [(l, r) for l, r in zip(lams, refl) if lo <= l <= hi]
    if not inside:
        return None
    (l1, r1), (l2, r2) = inside[0], inside[-1]
    slope = (r2 - r1) / (l2 - l1)

    def cont(x):
        return r1 + slope * (x - l1)

    lmin, rmin = min(inside, key=lambda t: t[1] / cont(t[0]))
    return {
        "lo": l1, "hi": l2,
        "cont_at_min": cont(lmin),
        "min_lam": lmin,
        "min_refl": rmin,
        "depth": 1.0 - rmin / cont(lmin),
        "centre_offset_nm": (lmin - centre) * 1e9,
    }


def part1_spectrum():
    section("1. A synthetic reflectance spectrum: continuum and band depth")
    lams = make_grid(1.0)
    refl = [reflectance(l) for l in lams]
    print(f"  grid: {len(lams)} samples from {LAM_MIN * 1e6:.2f} to "
          f"{LAM_MAX * 1e6:.2f} um at 1 nm spacing")
    print()
    feats = (("Fe-oxide-like", 0.90, 0.75, 1.05),
             ("water-like", 1.40, 1.30, 1.50),
             ("water-like", 1.90, 1.80, 2.00),
             ("Al-OH-like", 2.20, 2.14, 2.26),
             ("carbonate-like", 2.33, 2.26, 2.40))
    print(f"{'feature':<18}{'window (um)':<18}{'true depth':>12}"
          f"{'band centre (um)':>18}{'offset (nm)':>13}")
    for name, c, lo, hi in feats:
        m = band_metrics(lams, refl, lo * 1e-6, hi * 1e-6, c * 1e-6)
        print(f"{name:<18}{lo:>6.2f}-{hi:<8.2f}{m['depth']:>14.4f}"
              f"{m['min_lam'] * 1e6:>18.4f}{m['centre_offset_nm']:>13.2f}")
    print()
    print("  The 'true depth' is the value measured from the synthetic")
    print("  spectrum with the same straight-line continuum that a real")
    print("  analysis would fit.  For the narrow Al-OH-like feature the depth")
    print("  is recovered only because the grid resolves it: the grid is 1 nm")
    print("  and the feature is 22 nm wide (1 sigma).")
    print()
    print("  Convert to wavenumbers, the unit spectroscopy is written in:")
    for c in (0.90, 1.40, 1.90, 2.20, 2.33):
        print(f"    {c:.2f} um = {1.0 / (c * 1e-6) / 100:.1f} cm^-1")
    print("  A 1 nm step at 2.2 um is 2.07 cm^-1; the same 1 nm step at 0.9 um")
    print("  is 12.3 cm^-1.  Equal wavelength steps are unequal wavenumber")
    print("  steps, which is why an FTIR interferogram must be sampled at equal")
    print("  optical path difference and not at equal wavelength.")


def part2_resolution():
    section("2. Spectral resolution: what survives a wider instrument function")
    lams = make_grid(1.0)
    refl = [reflectance(l) for l in lams]
    print("  The spectrum is convolved with a Gaussian response of FWHM dlambda.")
    print("  R = lambda/dlambda is the resolving power at the feature.")
    print()
    print(f"{'FWHM (nm)':>10}{'R at 2.20 um':>14}{'depth 2.20 um':>15}"
          f"{'depth 1.40 um':>15}{'depth 0.90 um':>15}")
    truth = {}
    for c, lo, hi in ((2.20, 2.14, 2.26), (1.40, 1.30, 1.50),
                      (0.90, 0.75, 1.05)):
        truth[c] = band_metrics(lams, refl, lo * 1e-6, hi * 1e-6,
                                c * 1e-6)["depth"]
    for fwhm_nm in (1.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        kern = gaussian_kernel(fwhm_nm * 1e-9)
        conv = convolve(refl, kern)
        out = []
        for c, lo, hi in ((2.20, 2.14, 2.26), (1.40, 1.30, 1.50),
                          (0.90, 0.75, 1.05)):
            m = band_metrics(lams, conv, lo * 1e-6, hi * 1e-6, c * 1e-6)
            out.append(m["depth"])
        print(f"{fwhm_nm:>10.1f}{2.20e-6 / (fwhm_nm * 1e-9):>14.0f}"
              f"{out[0]:>15.4f}{out[1]:>15.4f}{out[2]:>15.4f}")
    print()
    print("  Reference depths at 1 nm sampling (unresolved-instrument limit):")
    print(f"    2.20 um: {truth[2.20]:.4f},  1.40 um: {truth[1.40]:.4f}, "
          f"0.90 um: {truth[0.90]:.4f}")
    print()
    print("  A 40 nm FWHM instrument (R = 55 at 2.2 um) recovers only a")
    kern = gaussian_kernel(40e-9)
    conv = convolve(refl, kern)
    m40 = band_metrics(lams, conv, 2.14e-6, 2.26e-6, 2.20e-6)
    print(f"  depth of {m40['depth']:.4f} against a true {truth[2.20]:.4f}: a fractional loss of")
    print(f"  {1.0 - m40['depth'] / truth[2.20]:.3f}.  The broad 0.90 um feature, by contrast,")
    m40b = band_metrics(lams, conv, 0.75e-6, 1.05e-6, 0.90e-6)
    print(f"  keeps a depth of {m40b['depth']:.4f} against {truth[0.90]:.4f}: a loss of only")
    print(f"  {1.0 - m40b['depth'] / truth[0.90]:.3f}.  Resolution loss is a *shape* effect:")
    print("  what is lost is the fraction of the feature narrower than the")
    print("  instrument function, not the feature's existence.")


def part3_sampling():
    section("3. Sampling is not resolution: the effect of a coarse grid")
    lams = make_grid(1.0)
    refl = [reflectance(l) for l in lams]
    print("  The same spectrum, sampled on coarser grids with the grid offset by")
    print("  0.37 of a step so that no grid lands exactly on the feature centre.")
    print("  Sampling can miss the feature minimum even when the instrument")
    print("  function is narrow.")
    print()
    print(f"{'step (nm)':>10}{'samples':>10}{'depth 2.20 um':>15}"
          f"{'recovered centre (um)':>23}{'error (nm)':>12}")
    for step_nm in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0):
        ls = make_grid(step_nm, offset_frac=0.37)
        rs = [reflectance(l) for l in ls]
        m = band_metrics(ls, rs, 2.14e-6, 2.26e-6, 2.20e-6)
        print(f"{step_nm:>10.1f}{len(ls):>10}{m['depth']:>15.4f}"
              f"{m['min_lam'] * 1e6:>23.4f}{m['centre_offset_nm']:>12.1f}")
    print()
    print("  At a 20 nm step only about one sample falls inside the 22 nm")
    print("  feature, and the measured depth is a sample of the feature rather")
    print("  than its minimum, so it depends on the phase of the grid; at 50 nm")
    print("  the feature may be missed altogether.  A feature must be sampled")
    print("  at least twice per resolved element, and a detection is not an")
    print("  identification if the diagnostic feature is under-sampled.")
    print()
    print("  This is why a 30 m, 10 nm-band multispectral instrument cannot do")
    print("  mineralogy: it has the pixels but not the bands.  Mineral mapping")
    print("  needs contiguous narrow bands, i.e. an imaging spectrometer.")


def part4_beer_lambert():
    section("4. Beer-Lambert, band depth and optical depth")
    print("  A single absorber: T = exp(-k c l), absorptance A = 1 - T.")
    print("  A reflectance feature at a surface is not a transmittance, but the")
    print("  depth of a feature and the optical depth of the absorption that")
    print("  causes it are related monotonically, and doubling the abundance")
    print("  doubles the optical depth while saturating the band depth:")
    print()
    print(f"{'tau':>10}{'T = e^-tau':>12}{'A = 1-T':>10}{'depth/tau':>12}")
    for tau in (0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0):
        T = math.exp(-tau)
        print(f"{tau:>10.2f}{T:>12.6f}{1 - T:>10.6f}{(1 - T) / tau:>12.6f}")
    print()
    print("  The depth saturates: an increase in abundance from tau = 5 to")
    print("  tau = 10 changes the depth by only")
    print(f"  {(1 - math.exp(-10)) - (1 - math.exp(-5)):.4f}.  Quantitative abundance from")
    print("  reflectance therefore needs either the weak bands (where depth is")
    print("  linear in abundance) or a radiative-transfer model (where the")
    print("  saturation is inverted).  This is exactly the same saturation")
    print("  computed for the emitting layer in lesson 02-10-03 section 6, seen")
    print("  from the reflecting side.")
    print()
    print("  Index of refraction and grain size matter here: a fine powder has a")
    print("  much greater effective path length than a polished slab of the same")
    print("  mineral, so reflectance spectra of powders and slabs differ in")
    print("  band depth even at identical composition.  Never compare a library")
    print("  spectrum to a scene spectrum without matching the grain size.")


def part5_derivative():
    section("5. Derivative spectroscopy: killing the continuum")
    lams = make_grid(1.0)
    base = [reflectance(l) for l in lams]
    offset = [r + 0.10 for r in base]
    ramp = 0.30 * (LAM_MAX - LAM_MIN)
    sloped = [r + 0.10 + 0.30 * (l - LAM_MIN) / (LAM_MAX - LAM_MIN)
              for l, r in zip(lams, base)]
    step = 1e-9

    def d1(vals):
        return [(vals[i + 1] - vals[i - 1]) / (2 * step)
                for i in range(1, len(vals) - 1)]

    def d2(vals):
        return [(vals[i + 1] - 2 * vals[i] + vals[i - 1]) / step ** 2
                for i in range(1, len(vals) - 1)]

    def zero_crossing(vals, centre):
        best = None
        for i in range(len(vals) - 1):
            if vals[i] * vals[i + 1] < 0.0:
                x = lams[i + 1]
                if best is None or abs(x - centre) < abs(best - centre):
                    best = x
        return best

    def argmin_in(vals, lo, hi):
        cands = [lams[i + 1] for i in range(len(vals)) if lo <= lams[i + 1] <= hi]
        return min(cands, key=lambda x: vals[lams.index(x) - 1])

    centre = 2.20e-6
    print(f"  feature centre for reference: {centre * 1e6:.4f} um")
    print()
    d1_base, d1_off, d1_slop = d1(base), d1(offset), d1(sloped)
    d2_base, d2_slop = d2(base), d2(sloped)
    print("  Invariance of the *values*, as a maximum absolute difference:")
    print(f"    max |d1(+0.10 offset) - d1(raw)|        = "
          f"{max(abs(a - b) for a, b in zip(d1_off, d1_base)):.3e}")
    print(f"    max |d2(+0.10 + linear ramp) - d2(raw)| = "
          f"{max(abs(a - b) for a, b in zip(d2_slop, d2_base)):.3e}")
    print("  The first difference is a cancellation residue of the constant")
    print("  (the derivative of a constant is zero) and the second is a")
    print("  cancellation residue of the ramp (the second derivative of a")
    print("  linear function is zero); both are floating point against the")
    print("  1e14-1e18 magnitudes of the derivatives themselves, not physics.")
    print()
    print("  Located feature centre by two routes, searched in 2.14-2.26 um.")
    print("  For an absorption dip the centre is a *maximum* of the second")
    print("  derivative (the curve is convex at the bottom of a dip):")
    print(f"{'spectrum':<30}{'d1 zero (um)':>16}{'d2 maximum (um)':>18}")
    for name, vals in (("raw", base), ("+0.10 offset", offset),
                       ("+0.10 + linear ramp", sloped)):
        z = zero_crossing(d1(vals), centre)
        dd2 = d2(vals)
        i_max = max(range(len(dd2)),
                    key=lambda i: dd2[i] if 2.14e-6 <= lams[i + 1] <= 2.26e-6
                    else float("-inf"))
        print(f"{name:<30}{z * 1e6:>16.4f}{lams[i_max + 1] * 1e6:>18.4f}")
    dd2 = d2_base
    i_max = max(range(len(dd2)),
                key=lambda i: dd2[i] if 2.14e-6 <= lams[i + 1] <= 2.26e-6
                else float("-inf"))
    centre_from_d2 = lams[i_max + 1]
    print()
    print(f"  The second-derivative maximum locates the feature centre at")
    print(f"  {centre_from_d2 * 1e6:.4f} um on a 1 nm grid: the true centre to the grid")
    print("  resolution, and identical for all three spectra.  It is")
    print("  grid-limited, not method-limited.")
    slope = 0.30 / (LAM_MAX - LAM_MIN)
    i_c = lams.index(min(lams, key=lambda x: abs(x - centre)))
    curvature = abs((base[i_c + 1] - 2 * base[i_c] + base[i_c - 1]) / step ** 2)
    shift = slope / curvature
    print()
    print("  For the first derivative the immunity is only partial: an additive")
    print("  ramp of slope b shifts its zero crossing by b/curvature =")
    print(f"  {slope:.3e} / {curvature:.3e} = {shift * 1e9:.3f} nm, below the 1 nm grid step used")
    print("  here and therefore invisible in the table above, but real.  The")
    print("  second derivative has no such term at all.")
    print()
    print("  This is the entire reason derivative spectra are used to map")
    print("  mineralogy: the diagnostic *position* survives an unknown additive")
    print("  brightness trend, which is what an illumination and atmospheric")
    print("  continuum is.  The higher the derivative, the more of the")
    print("  continuum it removes — at the cost of amplifying noise, because")
    print("  differencing multiplies high-frequency noise by 1/step for d1 and")
    print("  by 1/step^2 for d2.")


def part6_index():
    section("6. Band ratios and normalised difference indices")
    lams = make_grid(1.0)
    print("  A normalised difference index IDX = (R_b - R_a)/(R_b + R_a).")
    print("  Bands: a = 2.20 um (inside the Al-OH-like feature), b = 2.10 um")
    print("  (shoulder).  The index is computed for spectra scaled by a")
    print("  continuum multiplier, to show what a ratio removes.")
    print()
    ra_lam, rb_lam = 2.20e-6, 2.10e-6

    def idx(vals, scale):
        ra = math.exp(0.0) * reflectance(ra_lam) * scale
        rb = reflectance(rb_lam) * scale
        return (rb - ra) / (rb + ra)

    print(f"{'continuum scale':>17}{'R at 2.10':>12}{'R at 2.20':>12}"
          f"{'index':>10}")
    for scale in (0.5, 0.8, 1.0, 1.2, 2.0):
        print(f"{scale:>17.2f}{reflectance(rb_lam) * scale:>12.4f}"
              f"{reflectance(ra_lam) * scale:>12.4f}{idx(lams, scale):>10.4f}")
    print()
    print("  The index is invariant to a multiplicative continuum: a factor of 4")
    print("  in brightness moves it not at all, because the same factor cancels")
    print("  top and bottom.  An index of this kind is a first-order correction")
    print("  for illumination, topography and atmospheric transmission, and it")
    print("  costs nothing to compute.  What it does *not* do is remove an")
    print("  additive path radiance or a wavelength-dependent atmospheric")
    print("  absorption, which is why operational products are atmospherically")
    print("  corrected before indices are formed.")
    print()
    band_depth_only = (reflectance(rb_lam) - reflectance(ra_lam))
    print(f"  The un-normalised difference R_b - R_a = {band_depth_only:.4f} is not")
    print("  invariant: it scales linearly with the continuum, which is the")
    print("  reason the normalised form is used.")


def part7_emissivity():
    section("7. From reflectance to emissivity: Kirchhoff at a surface")
    print("  For an opaque surface in local thermodynamic equilibrium,")
    print("  eps(lambda) = 1 - rho(lambda) at the same wavelength and direction,")
    print("  so a reflectance feature becomes an emissivity feature of the same")
    print("  depth but the opposite sign, measured against a continuum of 1.")
    print()
    lams = make_grid(1.0)
    print(f"{'lambda (um)':>13}{'reflectance':>14}{'emissivity':>13}"
          f"{'emissivity contrast':>22}")
    cont = reflectance(2.10e-6)
    for lam_um in (0.90, 1.40, 1.90, 2.10, 2.20, 2.33):
        r = reflectance(lam_um * 1e-6)
        print(f"{lam_um:>13.2f}{r:>14.4f}{1.0 - r:>13.4f}"
              f"{r - cont:>22.4f}")
    r_feat = reflectance(2.20e-6)
    print()
    print(f"  Numerically, the model reflectance is {r_feat:.4f} at the feature and")
    print(f"  {cont:.4f} on the 2.10 um shoulder, so the emissivity is")
    print(f"  {1 - r_feat:.4f} and {1 - cont:.4f} respectively: a spectral contrast of")
    print(f"  {cont - r_feat:.4f} in emissivity, equal and opposite to the reflectance")
    print("  contrast.  That contrast is what a thermal infrared spectrometer")
    print("  measures, and it is why the same minerals are identifiable in the")
    print("  8-14 um region from emissivity and in the 1-2.5 um region from")
    print("  reflectance: the underlying vibrational transitions are the same,")
    print("  and Kirchhoff's law connects the two observables.")
    print()
    print("  The practical caveats are large: eps = 1 - rho holds at a stated")
    print("  wavelength and direction, the surface must be opaque and isothermal")
    print("  over the measurement, and a real scene contains mixtures of")
    print("  materials at different temperatures.  A measured emissivity is a")
    print("  retrieval with error bars, and a nominal single value is not a")
    print("  measurement.")


def main():
    print("Spectroscopy principles for remote sensing")
    part1_spectrum()
    part2_resolution()
    part3_sampling()
    part4_beer_lambert()
    part5_derivative()
    part6_index()
    part7_emissivity()


if __name__ == "__main__":
    main()
