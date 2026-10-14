"""Interference and diffraction in optical instruments.

Run:  python3 interference_diffraction_demo.py
Requires: Python standard library only.

Companion to lesson 02-10-02.

The script:

1. Computes Young's two-slit fringe spacing and the number of fringes inside
   the central diffraction envelope.
2. Computes the single-slit minima analytically and locates them again by
   numerically integrating the aperture field, so that the analytic result
   is checked rather than asserted.
3. Numerically integrates the circular aperture to obtain the Airy pattern,
   locates its first two zeros, and verifies the textbook constants
   3.8317 (first zero of J1) and 1.2197 (Rayleigh coefficient).
4. Converts the Rayleigh criterion into the resolution of concrete optical
   instruments: a telescope, a satellite imager and the eye, and compares
   the diffraction limit with the detector sampling limit.
5. Computes thin-film interference: the quarter-wave antireflection coating
   and the residual reflectance of a real coating index.
6. Computes the resolving power of a diffraction grating and of a
   Fabry-Perot etalon.
7. Computes the temporal coherence length of a source and the path
   difference at which fringes vanish.

All integrals use the standard library only; the aperture quadrature is a
fixed-step sum whose accuracy is reported, not assumed.
"""

import math

C = 299792458.0  # m/s, exact


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def deg(rad):
    return math.degrees(rad)


# ------------------------------------------------------------------ helpers
def slit_field(sin_theta, a, lam):
    """Normalised far-field amplitude of a single slit, via the closed form.

    A(sin t) = sin(pi a sin t / lam) / (pi a sin t / lam)
    """
    x = math.pi * a * sin_theta / lam
    if x == 0.0:
        return 1.0
    return math.sin(x) / x


def slit_field_numeric(sin_theta, a, lam, n=4001):
    """Normalised far-field amplitude from a Riemann sum over the aperture."""
    k = 2.0 * math.pi / lam
    total_re = total_im = 0.0
    dx = a / (n - 1)
    for i in range(n):
        x = -0.5 * a + i * dx
        phase = -k * sin_theta * x
        total_re += math.cos(phase)
        total_im += math.sin(phase)
    amp = math.hypot(total_re, total_im) / n
    return amp


def disk_field(sin_theta, a, lam, n=2001):
    """Normalised far-field amplitude of a circular aperture of radius a.

    Integrates the chord integral over y:
        A = (1/(pi a^2)) * int_{-a}^{a} 2 sin(k s sqrt(a^2-y^2)) / (k s) dy
    with the s -> 0 limit a^2.  Returns the amplitude normalised to 1 at s=0.
    """
    k = 2.0 * math.pi / lam
    s = sin_theta
    dy = 2.0 * a / (n - 1)
    total = 0.0
    for i in range(n):
        y = -a + i * dy
        half = math.sqrt(max(a * a - y * y, 0.0))
        if s == 0.0:
            total += 2.0 * half
        else:
            total += 2.0 * math.sin(k * s * half) / (k * s)
    return total / (math.pi * a * a)


def locate_first_zero(func, lo, hi, tol=1e-14):
    """Bisection on the first sign change of func(sin_theta) in (lo, hi)."""
    n = 400
    step = (hi - lo) / n
    prev_s = lo
    prev_v = func(lo)
    for i in range(1, n + 1):
        s = lo + i * step
        v = func(s)
        if prev_v == 0.0:
            return prev_s
        if v * prev_v < 0.0:
            a_, b_ = prev_s, s
            fa = func(a_)
            for _ in range(200):
                m = 0.5 * (a_ + b_)
                fm = func(m)
                if fm == 0.0 or b_ - a_ < tol:
                    return m
                if fm * fa < 0.0:
                    b_ = m
                else:
                    a_, fa = m, fm
            return 0.5 * (a_ + b_)
        prev_s, prev_v = s, v
    return None


# ------------------------------------------------------------------- parts
def part1_young():
    section("1. Young's two-slit interference: fringe spacing and envelope")
    lam = 632.8e-9
    L = 2.0
    print(f"  lambda = {lam * 1e9:.1f} nm, screen distance L = {L:.1f} m")
    print()
    print(f"{'slit separation d (mm)':>24}{'fringe spacing (mm)':>22}"
          f"{'fringes per mm':>18}")
    for d_mm in (0.10, 0.25, 0.50, 1.00, 2.00):
        d = d_mm * 1e-3
        spacing = lam * L / d
        print(f"{d_mm:>24.2f}{spacing * 1e3:>22.4f}{1e-3 / spacing:>18.4f}")
    print()
    print("  Fringe spacing is linear in lambda and L and inverse in d.  An")
    print("  interferometer converts a length into a fringe count, which is why")
    print("  interferometry is the most precise length measurement there is: a")
    print(f"  fringe is {lam * 1e9 / 2:.1f} nm of path difference, and a fringe position")
    print("  can be measured to a thousandth of a fringe.")
    print()
    print("  With finite slits of width a the two-slit pattern is modulated by")
    print("  the single-slit envelope, and the envelope's first minimum falls at")
    print(f"  sin(theta) = lambda/a.  For a = 0.1 mm that is {deg(lam / 1e-4):.4f} deg;")
    print("  the number of interference fringes in the central envelope is")
    print(f"  2d/a = {2 * 0.5e-3 / 1e-4:.0f} for d = 0.5 mm and a = 0.1 mm.")


def part2_single_slit():
    section("2. Single slit: analytic minima verified by integrating the aperture")
    lam = 600e-9
    a = 0.20e-3
    print(f"  lambda = {lam * 1e9:.0f} nm, slit width a = {a * 1e3:.2f} mm")
    print()
    print(f"{'order m':>9}{'analytic sin(theta)':>22}{'numeric zero':>16}"
          f"{'diff':>12}")
    for m in (1, 2, 3):
        s_ana = m * lam / a
        s_num = locate_first_zero(lambda s: slit_field(s, a, lam),
                                  s_ana * 0.75, s_ana * 1.25)
        print(f"{m:>9}{s_ana:>22.8f}{s_num:>16.10f}{abs(s_num - s_ana):>12.2e}")
    worst = 0.0
    worst_s = 0.0
    for i in range(501):
        s = 3.0 * lam / a * i / 500.0
        d = abs(slit_field_numeric(s, a, lam) - abs(slit_field(s, a, lam)))
        if d > worst:
            worst, worst_s = d, s
    print()
    print(f"  The 4001-point Riemann sum over the aperture reproduces the")
    print(f"  magnitude of the closed form sin(x)/x to {worst:.2e} in amplitude over")
    print(f"  0 <= sin(theta) <= 3*lambda/a (worst at sin(theta)/ (lambda/a) =")
    print(f"  {worst_s / (lam / a):.3f}).  A magnitude comparison is used because the field")
    print("  of a symmetric aperture is real and changes sign at each zero: the")
    print("  sum returns the magnitude, the closed form the signed amplitude.")
    print("  The located zeros agree with m*lambda/a to the precision of the")
    print("  bisection, which is what the exercise asks you to verify.")
    print()
    print("  Angular half-width of the central maximum = asin(lambda/a) =")
    print(f"  {deg(math.asin(lam / a)):.6f} deg.  Halving a doubles the width, so a")
    print("  smaller aperture makes a broader beam: this is why a small")
    print("  transmitter cannot be made directional and why astronomical")
    print("  interferometry uses baselines rather than big dishes.")


def part3_airy():
    section("3. Circular aperture: the Airy pattern, verified numerically")
    a = 0.15
    lam = 550e-9
    print(f"  aperture radius a = {a * 1e3:.1f} mm, lambda = {lam * 1e9:.0f} nm")
    print()
    print("  q = 2*pi*a*sin(theta)/lambda.  Zeros are located by bisection on the")
    print("  numerically integrated aperture field:")
    print()
    print(f"{'zero':>6}{'q numeric':>14}{'q textbook':>14}{'|diff|':>12}"
          f"{'sin(theta)':>15}{'theta (arcsec)':>16}")
    for idx, (lo, hi, book) in enumerate(((3.0, 5.0, 3.831705970),
                                          (6.0, 8.0, 7.015586670)), start=1):
        s = locate_first_zero(lambda s: disk_field(s, a, lam),
                              lo * lam / (2 * math.pi * a),
                              hi * lam / (2 * math.pi * a))
        q = 2 * math.pi * a * s / lam
        print(f"{idx:>6}{q:>14.6f}{book:>14.6f}{abs(q - book):>12.2e}"
              f"{s:>15.10f}{deg(math.asin(min(s, 1.0))) * 3600:>16.2f}")
    c_numeric = 3.831705970 / math.pi
    print()
    print(f"  Rayleigh coefficient C = 3.831705970/pi = {c_numeric:.7f}, so the")
    print(f"  textbook 1.22 is a rounding of {c_numeric:.4f}: a {abs(1.22 - c_numeric) / c_numeric * 100:.3f} per cent")
    print("  error if you use 1.22 in a calibration.")
    print()
    print("  The zero of J1 at 3.8317 is what the quadrature returns, to within")
    print("  its own tolerance, without any Bessel function ever being called:")
    print("  the aperture integral *is* the Bessel function J1(q)/q.")


def part4_resolution():
    section("4. The resolution limit of an optical instrument")
    lam = 550e-9
    C_R = 3.831705970 / math.pi
    print("  theta_min = C * lambda/D with C = 1.219670 (disk) or 1.0 (slit)")
    print()
    print(f"{'system':<34}{'D (m)':>10}{'theta (rad)':>16}{'theta (arcsec)':>16}")
    systems = (("eye, dark-adapted pupil", 7.0e-3),
               ("eye, bright pupil", 2.5e-3),
               ("amateur telescope", 0.20),
               ("survey telescope", 1.00),
               ("large telescope", 8.20),
               ("satellite imager", 0.30))
    for name, D in systems:
        th = C_R * lam / D
        print(f"{name:<34}{D:>10.4g}{th:>16.4e}{deg(th) * 3600:>16.3f}")
    print()
    print("  Now the same number expressed as a ground sample distance (GSD):")
    print()
    alt = 700e3
    print(f"  altitude h = {alt / 1e3:.0f} km")
    print(f"{'D (m)':>8}{'theta (rad)':>16}{'diffraction GSD (m)':>22}")
    for D in (0.10, 0.30, 0.50, 1.00):
        gsd = C_R * lam / D * alt
        print(f"{D:>8.2f}{C_R * lam / D:>16.4e}{gsd:>22.4f}")
    print()
    print("  A 0.30 m aperture at 700 km has a diffraction-limited GSD of")
    print(f"  {C_R * lam / 0.30 * alt:.3f} m, so a nominal 10 m multispectral product is")
    print("  not diffraction-limited: it is set by the detector pixel and the")
    print("  swath, and the aperture has resolution in reserve.  That is the")
    print("  normal design trade for a wide-swath imager and the reason")
    print("  panchromatic bands are sharper than multispectral ones: the pixel,")
    print("  not the aperture, is the limit.")
    print()
    print("  Whether an instrument is diffraction-limited or pixel-limited is")
    print("  decided by the f-number: diffraction blurs by 1.22*lambda*F and the")
    print("  pixel samples at p, so diffraction takes over above")
    print("  F = 2p/lambda:")
    print()
    print(f"{'pixel pitch p (um)':>20}{'lambda (nm)':>13}{'F above which diffraction dominates':>38}")
    for p_um in (1.0, 2.0, 4.0, 8.0):
        for lam_nm in (450.0, 550.0):
            p = p_um * 1e-6
            lam_x = lam_nm * 1e-9
            print(f"{p_um:>20.1f}{lam_nm:>13.0f}{2 * p / lam_x:>38.1f}")
    print()
    print("  A 4 um pixel at 550 nm is diffraction-limited beyond f/14.5, which")
    print("  is the computed form of the photographer's rule that a lens stops")
    print("  improving past about f/16.  A 1 um pixel is diffraction-limited")
    print("  beyond f/3.6, which is why small-pixel sensors quickly become")
    print("  diffraction-limited: smaller pixels buy sampling, not resolution.")


def part5_thin_film():
    section("5. Thin-film interference: antireflection coatings")
    n_glass = 1.52
    R_bare = ((1.0 - n_glass) / (1.0 + n_glass)) ** 2
    n_ideal = math.sqrt(n_glass)
    print(f"  bare glass: R = ((1-n)/(1+n))^2 = {R_bare:.4f} = {R_bare * 100:.2f} per cent")
    print(f"  ideal quarter-wave coating index = sqrt(n) = {n_ideal:.4f}")
    print()
    print("  A quarter-wave film of index nc gives, at the design wavelength,")
    print("  R = ((n - nc^2)/(n + nc^2))^2:")
    print()
    print(f"{'nc':>8}{'R':>12}{'transmission gain vs bare':>26}")
    for nc in (1.22, 1.30, 1.38, 1.45, 1.52, 1.70, 2.00):
        R = ((n_glass - nc ** 2) / (n_glass + nc ** 2)) ** 2
        gain = (1.0 - R) / (1.0 - R_bare)
        print(f"{nc:>8.2f}{R:>12.5f}{gain:>26.4f}")
    print()
    print(f"  nc = sqrt(1.52) = {n_ideal:.4f} nulls the reflection exactly.  The")
    print("  practical coating is MgF2, nc about 1.38 (nominal), which leaves")
    R_mgf2 = ((n_glass - 1.38 ** 2) / (n_glass + 1.38 ** 2)) ** 2
    print(f"  R = {R_mgf2:.5f} = {R_mgf2 * 100:.2f} per cent instead of {R_bare * 100:.2f} per cent —")
    print("  a factor of")
    print(f"  {R_bare / R_mgf2:.1f} reduction with one layer, and not zero, because")
    print("  no suitable hard material has the ideal index.")
    lam0 = 550e-9
    t = lam0 / (4 * 1.38)
    print()
    print(f"  Design thickness at 550 nm: t = lambda/(4 nc) = {t * 1e9:.2f} nm.")
    print("  A 2 per cent thickness error moves the reflectance minimum by")
    dlam = lam0 * 0.02
    print(f"  about {dlam * 1e9:.1f} nm, which is why coatings are qualified on a")
    print("  spectrophotometer rather than by measurement with a micrometer.")


def part6_dispersive():
    section("6. Resolving power: grating and Fabry-Perot etalon")
    lam = 500e-9
    print("  Diffraction grating: R = m N, with N the number of illuminated")
    print("  grooves and m the order.  Dispersion: d(theta)/d(lambda) = m/(d cos t).")
    print()
    print(f"{'grooves/mm':>12}{'width (mm)':>12}{'m':>5}{'N':>10}{'R':>12}"
          f"{'dlambda (pm)':>14}")
    for gpm, W, m in ((600, 50.0, 1), (600, 50.0, 2), (1200, 50.0, 1),
                      (1200, 100.0, 1), (1800, 50.0, 1)):
        N = gpm * W
        R = m * N
        print(f"{gpm:>12}{W:>12.0f}{m:>5}{N:>10.0f}{R:>12.0f}"
              f"{lam / R * 1e12:>14.3f}")
    print()
    print("  A 1200 groove/mm, 50 mm grating in first order resolves")
    print(f"  R = {1200 * 50:.0f}, i.e. {lam / 60000 * 1e12:.2f} pm at 500 nm.  That is a laboratory")
    print("  spectrometer; a spaceborne imaging spectrometer with 10 nm bands")
    print(f"  has R = {lam / 10e-9:.0f}.")
    print()
    print("  Fabry-Perot: F = pi*sqrt(Rr)/(1-Rr) and R_res = m F.")
    print()
    print(f"{'mirror R':>10}{'finesse F':>12}{'m (d=0.5 mm)':>15}{'R_res':>14}"
          f"{'dlambda (fm)':>14}")
    d = 0.5e-3
    for Rr in (0.50, 0.80, 0.90, 0.95, 0.98):
        F = math.pi * math.sqrt(Rr) / (1.0 - Rr)
        m = 2.0 * d / lam
        R_res = m * F
        print(f"{Rr:>10.2f}{F:>12.2f}{m:>15.0f}{R_res:>14.3e}"
              f"{lam / R_res * 1e15:>14.3f}")
    print()
    print("  A 0.5 mm etalon with 98 per cent mirrors resolves")
    Rs = 0.98
    Fs = math.pi * math.sqrt(Rs) / (1 - Rs)
    ms = 2 * d / lam
    print(f"  R_res = {ms * Fs:.3e}, i.e. {lam / (ms * Fs) * 1e12:.3f} pm at 500 nm — far beyond")
    print("  any grating, which is why etalons are used to measure line shapes in")
    print("  the laboratory and why they are unusable for broadband sensing: the")
    print(f"  free spectral range is only lambda^2/(2d) = {lam ** 2 / (2 * d) * 1e9:.3f} nm.")


def part7_coherence():
    section("7. Temporal coherence: when fringes vanish")
    print("  A source of bandwidth dlambda has a coherence length")
    print("  l_c = lambda^2/dlambda (equal-time limit).")
    print()
    print(f"{'source':<28}{'lambda (nm)':>13}{'dlambda (nm)':>14}"
          f"{'l_c':>14}")
    sources = (("He-Ne laser (nominal)", 632.8, 0.002),
               ("mercury green line", 546.1, 0.05),
               ("white light, visible", 550.0, 300.0),
               ("LED, 20 nm FWHM", 850.0, 20.0),
               ("broadband lamp", 1000.0, 500.0))
    for name, lam_nm, dlam_nm in sources:
        lam = lam_nm * 1e-9
        dlam = dlam_nm * 1e-9
        lc = lam ** 2 / dlam
        text = f"{lc * 1e3:.3f} mm" if lc >= 1e-3 else f"{lc * 1e6:.3f} um"
        print(f"{name:<28}{lam_nm:>13.1f}{dlam_nm:>14.3f}{text:>14}")
    print()
    lam = 550e-9
    print(f"  White light at 550 nm with 300 nm of bandwidth has l_c =")
    print(f"  {lam ** 2 / 300e-9 * 1e9:.2f} nm, i.e. about {lam ** 2 / 300e-9 / lam:.1f} wavelengths: fringes survive only")
    print("  a few wavelengths of path difference, which is why white-light")
    print("  interferometry works only in a nulled, near-zero path configuration.")
    print("  A narrowband laser has a coherence length of centimetres to metres,")
    print("  which is what makes phase-based fibre sensing (lesson 02-10-05)")
    print("  possible: the two arms of the interferometer must stay matched to")
    print("  better than l_c.")


def main():
    print("Interference and diffraction in optical instruments")
    part1_young()
    part2_single_slit()
    part3_airy()
    part4_resolution()
    part5_thin_film()
    part6_dispersive()
    part7_coherence()


if __name__ == "__main__":
    main()
