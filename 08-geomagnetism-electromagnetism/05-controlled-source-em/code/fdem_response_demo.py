#!/usr/bin/env python3
"""Frequency-domain electromagnetics (FDEM): skin depth, primary coil coupling,
and the measured secondary/primary response of a horizontal coplanar coil pair
over a homogeneous conductive halfspace.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fdem_response_demo.py

Everything here is SYNTHETIC.  The conductivities, separations, heights,
frequencies and noise level are chosen teaching values, not measurements of a
real ground or of a real instrument.

The response comes from the exact transform (Sommerfeld) solution for a vertical
magnetic dipole at height h above a halfspace, rearranged into a form whose low
induction limit is explicit:

    H_s/H_p = r^3 k^2 / (4 sqrt(r^2 + 4 h^2))
              - r^3 Integral_0^inf (k^4/4) (u+3l)/(l+u)^3 e^{-2 l h} J_0(l r) dl

with k^2 = i omega mu0 sigma, u = sqrt(l^2 + k^2), r the coil separation and h
the coil height.  The first term is the low-induction-number (LIN) response; the
integral carries the correction.  The two together reduce to the image value
r^3 (8h^2 - r^2)/(r^2 + 4h^2)^{5/2} as the ground becomes a perfect conductor.

Contents
--------
1. Diffusion constants and skin depth.
2. Primary (free-space) coupling: Neumann double integral vs the dipole limit.
3. Secondary/primary response versus frequency, with the induction number.
4. The low-induction-number asymptote and its measured power laws.
5. Independent checks: adaptive quadrature, height scaling, asymptote.
6. Approach to the perfect-conductor (screening) limit.
7. Numerical self-consistency and the receiver-noise detection limit.
"""

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

# Exact SI constants.
MU0 = 4.0e-7 * np.pi             # H/m, permeability of free space
EPS0 = 8.8541878128e-12          # F/m, permittivity of free space
RNG = np.random.default_rng(20261014)

# --- SYNTHETIC system and ground parameters (chosen, not measured) -----------
R_SEP = 20.0                     # m, transmitter-receiver separation (coplanar)
SIGMA = 0.05                     # S/m, homogeneous halfspace conductivity
SIGMA_RES = 0.005                # S/m, resistive ground used in section 7
FREQS = np.array([100.0, 300.0, 1000.0, 3000.0, 10000.0, 30000.0, 100000.0])
NOISE_PPM = 2.0                  # synthetic receiver noise, ppm of the primary
H_BIRD = 30.0                    # m, height of a towed bird (section 6)
H_RECV = 0.2                     # m, coil height used for the Born integral


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def skin_depth(f_hz, sigma):
    """Diffusive skin depth sqrt(2/(omega mu0 sigma)) in metres."""
    return np.sqrt(2.0 / (2.0 * np.pi * f_hz * MU0 * sigma))


def secondary_ratio(f_hz, sigma, r, h=0.0, lam_factor=80.0):
    """Secondary/primary vertical-field ratio of a horizontal coplanar coil pair.

    Conventions: time dependence e^{+i omega t}; the primary field of the
    transmitter dipole at the receiver is H_p = -m/(4 pi r^3); the returned
    complex ratio has in-phase = real part and quadrature = imaginary part.
    """
    omega = 2.0 * np.pi * f_hz
    k2 = 1j * omega * MU0 * sigma
    k = np.sqrt(k2)
    lam_max = lam_factor * max(1.0 / r, abs(k))
    dlam = min(1.0 / (30.0 * r), max(abs(k), 1e-30) / 200.0)
    n = int(min(800000, max(20000, lam_max / dlam)))
    lam = np.linspace(0.0, lam_max, n + 1)
    u = np.sqrt(lam ** 2 + k2)
    integrand = ((k2 ** 2 / 4.0) * (u + 3.0 * lam) / (lam + u) ** 3
                 * np.exp(-2.0 * lam * h) * j0(lam * r))
    i2 = np.trapezoid(integrand, lam)
    lin_term = k2 * r ** 3 / (4.0 * np.sqrt(r ** 2 + 4.0 * h ** 2))
    return lin_term - r ** 3 * i2


def perfect_conductor_ratio(r, h=0.0):
    """Image-theory limit for sigma -> infinity: H_s/H_p for a coplanar pair."""
    return r ** 3 * (8.0 * h ** 2 - r ** 2) / (r ** 2 + 4.0 * h ** 2) ** 2.5


def mutual_inductance_neumann(a, b, s, n_phi=600):
    """Mutual inductance (H) of two coplanar circular loops, from its definition
    M = (mu0/4 pi) * closed-closed (dl1 . dl2)/R (Neumann double integral).

    Loop 1 has radius a centred at (-s/2, 0), loop 2 radius b at (+s/2, 0); both
    lie in the plane z = 0.
    """
    phi = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
    dphi = 2.0 * np.pi / n_phi
    p1x = -s / 2.0 + a * np.cos(phi)
    p1y = a * np.sin(phi)
    p2x = s / 2.0 + b * np.cos(phi)
    p2y = b * np.sin(phi)
    dx = p2x[None, :] - p1x[:, None]
    dy = p2y[None, :] - p1y[:, None]
    dist = np.sqrt(dx ** 2 + dy ** 2)
    dot = a * b * np.cos(phi[:, None] - phi[None, :])
    return MU0 / (4.0 * np.pi) * np.sum(dot / dist) * dphi ** 2


def dipole_mutual_inductance(a, b, s):
    """Dipole limit of the coplanar-loop mutual inductance (H)."""
    return -MU0 * np.pi * a ** 2 * b ** 2 / (4.0 * s ** 3)


def reference_ratio(f_hz, sigma, r, h, lam_factor=400.0):
    """The same response by a single adaptive quadrature of the unregularised
    kernel, with no analytic term and no split: this is an independent code path
    used only as a check (it is slow and it needs h > 0 to converge)."""
    k2 = 1j * 2.0 * np.pi * f_hz * MU0 * sigma
    k = np.sqrt(k2)
    lam_max = lam_factor * max(1.0 / r, abs(k))

    def kernel(lam):
        u = np.sqrt(lam ** 2 + k2)
        return (lam ** 2 * (lam - u) / (lam + u) * np.exp(-2.0 * lam * h)
                * j0(lam * r))

    re = quad(lambda l: kernel(l).real, 0.0, lam_max,
              limit=800, epsabs=1e-16, epsrel=1e-12)[0]
    im = quad(lambda l: kernel(l).imag, 0.0, lam_max,
              limit=800, epsabs=1e-16, epsrel=1e-12)[0]
    return -r ** 3 * (re + 1j * im)


def main():
    section("1. Diffusion constants and skin depth (exact mu0 = 4 pi x 10^-7 H/m)")
    print(f"SYNTHETIC ground: uniform conductivity sigma = {SIGMA:.3f} S/m")
    print(f"diffusion constant D = 1/(mu0 sigma) = {1.0 / (MU0 * SIGMA):.3e} m^2/s")
    print("\n   f (Hz)     omega (rad/s)   skin depth (m)   omega*eps0/sigma")
    for f in FREQS:
        print(f"  {f:8.0f}   {2.0 * np.pi * f:14.3e}   {skin_depth(f, SIGMA):14.2f}   "
              f"{2.0 * np.pi * f * EPS0 / SIGMA:.2e}")
    print("  displacement current is smaller than conduction current by at least")
    print("  four orders of magnitude over this band, which is what licenses the")
    print("  diffusive (quasi-static) form of the equations used below.")

    section("2. Primary coupling: Neumann integral vs the dipole limit")
    a = b = 1.0                      # loop radius, m
    ms = []
    for s in (5.0, 10.0, 20.0, 40.0):
        m_num = mutual_inductance_neumann(a, b, s)
        m_dip = dipole_mutual_inductance(a, b, s)
        ms.append((s, m_num))
        print(f"  separation {s:5.1f} m: M(Neumann) = {m_num:12.5e} H, "
              f"M(dipole) = {m_dip:12.5e} H, M_num/M_dip = {m_num / m_dip:8.5f}")
    ss = np.array([m[0] for m in ms])
    mm = np.array([abs(m[1]) for m in ms])
    print(f"  measured log-log slope of |M| vs separation = "
          f"{np.polyfit(np.log(ss), np.log(mm), 1)[0]:.5f}  (dipole theory: -3)")
    print("  the loops are small compared with the separation (a/s <= 0.2), so the")
    print("  dipole limit is recovered to 10% at a/s = 0.2 and to 1% at a/s = 0.05.")
    print("  The sign is negative: coplanar coils couple with opposite polarity, so")
    print("  the free-space primary must be bucked out before the ground response")
    print("  is visible.  The 1/s^3 decay of that primary is the dynamic-range")
    print("  problem every FDEM system is built around.")

    section("3. Secondary/primary response versus frequency (coplanar pair)")
    print(f"SYNTHETIC system: separation r = {R_SEP:.0f} m, coils on the ground (h = 0)")
    print("\n   f (Hz)   skin depth(m)   theta=r/delta   in-phase(ppm)"
          "   quadrature(ppm)   amplitude(ppm)")
    resp = {}
    for f in FREQS:
        theta = R_SEP / skin_depth(f, SIGMA)
        ratio = secondary_ratio(f, SIGMA, R_SEP, 0.0)
        resp[f] = ratio
        print(f"  {f:8.0f}   {skin_depth(f, SIGMA):12.2f}   {theta:13.3f}   "
              f"{ratio.real * 1e6:14.1f}   {ratio.imag * 1e6:15.1f}   "
              f"{abs(ratio) * 1e6:14.1f}")
    print("  quadrature rises with conductivity while the ground is transparent,")
    print("  passes through a maximum and then reverses sign, while the in-phase")
    print("  part swings negative: that reversal is the onset of screening, and a")
    print("  real system is unusable past it.  Two features are worth locating:")
    # theta where the quadrature changes sign, by bisection in log f
    lo, hi = 10000.0, 30000.0
    for _ in range(40):
        mid = np.sqrt(lo * hi)
        if secondary_ratio(mid, SIGMA, R_SEP, 0.0).imag > 0.0:
            lo = mid
        else:
            hi = mid
    f_null = np.sqrt(lo * hi)
    theta_null = R_SEP / skin_depth(f_null, SIGMA)
    # peak of the quadrature, on a coarse-to-fine grid in log f
    grid = np.geomspace(300.0, 30000.0, 400)
    vals = np.array([secondary_ratio(f, SIGMA, R_SEP, 0.0).imag for f in grid])
    i_pk = int(np.argmax(vals))
    f_pk = grid[i_pk]
    theta_pk = R_SEP / skin_depth(f_pk, SIGMA)
    print(f"    quadrature nulls at theta = {theta_null:.3f} "
          f"(f = {f_null:.0f} Hz for this model)")
    print(f"    quadrature peaks at theta = {theta_pk:.3f} "
          f"(f = {f_pk:.0f} Hz), value = {vals[i_pk] * 1e6:.0f} ppm")
    print("    so a survey has a usable window theta < 1; above it the response")
    print("    is dominated by screening and the conductivity resolution collapses.")

    section("3b. Worked-example values used in the lesson text")
    sigma_ex, r_ex, f_ex = 0.02, 15.0, 1000.0
    d_ex = skin_depth(f_ex, sigma_ex)
    theta_ex = r_ex / d_ex
    lin_ex = 1j * 2.0 * np.pi * f_ex * MU0 * sigma_ex * r_ex ** 2 / 4.0
    ex = secondary_ratio(f_ex, sigma_ex, r_ex, 0.0)
    print(f"  SYNTHETIC example: sigma = {sigma_ex:.2f} S/m, r = {r_ex:.0f} m, "
          f"f = {f_ex:.0f} Hz")
    print(f"    omega = {2.0 * np.pi * f_ex:.4f} rad/s")
    print(f"    omega mu0 sigma = {2.0 * np.pi * f_ex * MU0 * sigma_ex:.6e} 1/m^2")
    print(f"    skin depth delta = sqrt(2/(omega mu0 sigma)) = {d_ex:.3f} m")
    print(f"    induction number theta = r/delta = {theta_ex:.4f}")
    print(f"    LIN ratio k^2 r^2/4 = {lin_ex.real:.6e}{lin_ex.imag:+.6e}i")
    print(f"    exact ratio          = {ex.real:.6e}{ex.imag:+.6e}i")
    print(f"    exact quadrature     = {ex.imag * 1e6:.1f} ppm")
    print(f"    apparent conductivity from the LIN quadrature = "
          f"{4.0 * ex.imag / (2.0 * np.pi * f_ex * MU0 * r_ex ** 2):.6f} S/m "
          f"({(4.0 * ex.imag / (2.0 * np.pi * f_ex * MU0 * r_ex ** 2)) / sigma_ex - 1.0:+.2%})")

    section("4. Low-induction-number asymptote and its measured power laws")
    print("  LIN prediction for the whole-space (weak-induction) response:")
    print("      H_s/H_p -> k^2 r^2/4 = i omega mu0 sigma r^2/4,")
    print("  i.e. quadrature linear in omega with the coefficient above.")
    print("\n   f (Hz)   theta      |H_s/H_p|        |LIN|          (exact/LIN - 1)")
    for f in (1.0, 3.0, 10.0, 30.0, 100.0, 300.0):
        theta = R_SEP / skin_depth(f, SIGMA)
        lin = 1j * 2.0 * np.pi * f * MU0 * SIGMA * R_SEP ** 2 / 4.0
        exact = secondary_ratio(f, SIGMA, R_SEP, 0.0)
        print(f"  {f:8.1f}   {theta:7.4f}   {abs(exact):13.6e}   {abs(lin):13.6e}   "
              f"{abs(exact / lin - 1.0):14.4e}")
    f_lo = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
    q_lo = np.array([secondary_ratio(f, SIGMA, R_SEP, 0.0).imag for f in f_lo])
    ip_lo = np.array([secondary_ratio(f, SIGMA, R_SEP, 0.0).real for f in f_lo])
    print(f"\n  measured log-log slope of quadrature vs f = "
          f"{np.polyfit(np.log(f_lo), np.log(np.abs(q_lo)), 1)[0]:.3f}  (theory 1)")
    print(f"  measured log-log slope of in-phase  vs f = "
          f"{np.polyfit(np.log(f_lo), np.log(np.abs(ip_lo)), 1)[0]:.3f}  "
          f"(3/2, not 2)")
    print("  So for a HALFSPACE the in-phase part is smaller than the quadrature by")
    print("  one factor of theta and grows as omega^{3/2}, not omega^2.  The reason")
    print("  is structural: u = sqrt(lambda^2 + k^2) has a branch point at")
    print("  lambda = +/- i k, so the response is not a power series in omega but")
    print("  contains the odd powers of k that the branch cut generates.  The")
    print("  familiar 'in-phase ~ omega^2' rule belongs to a compact target with a")
    print("  single relaxation time, not to a halfspace.")

    section("5. Independent checks of the response")
    print("  (a) ADAPTIVE QUADRATURE of the unregularised kernel, a separate code")
    print("      path with no analytic term and no split:")
    print("\n   h (m)   f (Hz)   split formula          adaptive quadrature"
          "     relative difference")
    for h in (2.0, 20.0):
        for f in (10.0, 1000.0):
            a = secondary_ratio(f, SIGMA, R_SEP, h)
            b = reference_ratio(f, SIGMA, R_SEP, h)
            print(f"  {h:5.1f}   {f:8.0f}   {a.real:+.8e}{a.imag:+.8e}i   "
                  f"{b.real:+.8e}{b.imag:+.8e}i   {abs(a - b) / abs(a):.2e}")
    print("      the two routes agree to about one part in 1e8 at h = 2 m.  At")
    print("      h = 0 the kernel is only conditionally convergent, which is why")
    print("      the split is used there and why the screen limit below is the")
    print("      relevant check in that case.")

    print("\n  (b) ANALYTIC weak-induction limit.  With sigma -> 0 the kernel")
    print("      reduces to -(k^2/4) J_0(l r) and Integral_0^inf J_0(l r) dl = 1/r")
    print("      gives H_s/H_p = k^2 r^2/4 exactly.  Height enters that term as")
    print("      r/sqrt(r^2 + 4h^2), so the ratio of responses at two heights must")
    print("      tend to that factor as theta -> 0:")
    f_test = 0.05
    print("\n   h (m)   ratio(h)/ratio(0) measured   r/sqrt(r^2+4h^2)   difference")
    for h in (5.0, 10.0, 20.0, 40.0):
        r0 = secondary_ratio(f_test, SIGMA, R_SEP, 0.0)
        rh = secondary_ratio(f_test, SIGMA, R_SEP, h)
        pred = R_SEP / np.sqrt(R_SEP ** 2 + 4.0 * h ** 2)
        print(f"  {h:5.1f}   {abs(rh / r0):25.6f}   {pred:18.6f}   "
              f"{abs(abs(rh / r0) - pred):.3e}")
    print(f"  (check made at f = {f_test:.2f} Hz, where theta = "
          f"{R_SEP / skin_depth(f_test, SIGMA):.4f}; the residual is itself of")
    print("   order theta and shrinks as the frequency is lowered.)")

    print("\n  (c) MEASURED DEPARTURE from the weak-induction form.  The leading")
    print("      correction is of order theta (measured slope below is the")
    print("      exponent of (exact/LIN - 1) against theta):")
    t_small = np.array([0.002, 0.005, 0.01, 0.02, 0.05])
    # theta = r/delta with delta = sqrt(2/(omega mu0 sigma))
    #   => omega = 2 theta^2 /(mu0 sigma r^2)  => f = theta^2/(pi mu0 sigma r^2)
    f_small = t_small ** 2 / (np.pi * MU0 * SIGMA * R_SEP ** 2)
    dev = []
    for f in f_small:
        lin = 1j * 2.0 * np.pi * f * MU0 * SIGMA * R_SEP ** 2 / 4.0
        dev.append(abs(secondary_ratio(f, SIGMA, R_SEP, 0.0) / lin - 1.0))
    dev = np.array(dev)
    print(f"    theta            = {t_small}")
    print(f"    |exact/LIN - 1|  = {np.round(dev, 6)}")
    print(f"    ratio dev/theta  = {np.round(dev / t_small, 4)}")
    print(f"    measured exponent of dev against theta = "
          f"{np.polyfit(np.log(t_small), np.log(dev), 1)[0]:.3f}")
    print("      So the LIN form carries a relative error of about 1.5 theta: 1.5%")
    print("      at theta = 0.01 and 15% at theta = 0.1.  The error is a bias, not")
    print("      scatter, and it propagates straight into any apparent-conductivity")
    print("      estimate made by inverting the LIN formula.")

    print("\n  (d) SCALE INVARIANCE.  The response contains sigma, omega and r only")
    print("      through k r, so (sigma, r) and (sigma/4, 2r) at the same frequency")
    print("      must be indistinguishable:")
    for sigma, rr in ((SIGMA, R_SEP), (SIGMA / 4.0, 2.0 * R_SEP),
                      (4.0 * SIGMA, R_SEP / 2.0), (SIGMA / 16.0, 4.0 * R_SEP)):
        ratio = secondary_ratio(1000.0, sigma, rr, 0.0)
        print(f"    sigma = {sigma:8.5f} S/m, r = {rr:5.1f} m: "
              f"theta = {rr / skin_depth(1000.0, sigma):7.4f}, "
              f"H_s/H_p = {ratio.real:+.8e}{ratio.imag:+.8e}i")
    print("      the four responses are identical to numerical precision: this is")
    print("      the conductivity-separation ambiguity, and it is a property of the")
    print("      physics, not of the instrument.  Breaking it needs an independent")
    print("      length or an independent frequency, which is the whole reason")
    print("      multi-separation and multi-frequency systems exist.")

    section("6. Approach to the perfect-conductor (screening) limit")
    print(f"  image limit for coils on the ground (h = 0):      "
          f"{perfect_conductor_ratio(R_SEP, 0.0):+.6f}")
    print(f"  image limit for a bird at h = {H_BIRD:.0f} m:            "
          f"{perfect_conductor_ratio(R_SEP, H_BIRD):+.6f}")
    print(f"  image limit for a bird at h = {H_RECV:.1f} m:           "
          f"{perfect_conductor_ratio(R_SEP, H_RECV):+.6f}")
    print("\n   sigma (S/m)   f (Hz)   theta      in-phase     quadrature"
          "   |exact - image(h=0)|")
    for sigma in (0.05, 1.0, 20.0, 200.0):
        for f in (1000.0, 100000.0):
            theta = R_SEP / skin_depth(f, sigma)
            exact = secondary_ratio(f, sigma, R_SEP, 0.0)
            print(f"  {sigma:9.1f}   {f:8.0f}   {theta:7.2f}   "
                  f"{exact.real:+10.5f}   {exact.imag:+10.5f}   "
                  f"{abs(exact - perfect_conductor_ratio(R_SEP, 0.0)):9.2e}")
    print("  the response turns from the weak-induction form to the image value as")
    print("  the induction number grows: a ground whose skin depth is small")
    print("  compared with the geometry behaves as a mirror, not as a sounding")
    print("  target, and no frequency window below it recovers conductivities.")

    section("7. Numerical self-consistency and the receiver-noise detection limit")
    print("  truncation of the Sommerfeld integral (lam_factor 80 -> 160):")
    for f in (1000.0, 100000.0):
        r1 = secondary_ratio(f, SIGMA, R_SEP, 0.0, lam_factor=80.0)
        r2 = secondary_ratio(f, SIGMA, R_SEP, 0.0, lam_factor=160.0)
        print(f"    f = {f:8.0f} Hz: |ratio(80) - ratio(160)| = {abs(r1 - r2):.3e}   "
              f"(relative {abs(r1 - r2) / abs(r1):.2e})")
    print("  the J_0 tails are only conditionally convergent at h = 0, so the two")
    print("  truncations agree to about one part in 1e5: numbers below are quoted")
    print("  to four figures and no further.")

    print(f"\n  resistive synthetic ground sigma = {SIGMA_RES:.4f} S/m, receiver")
    print(f"  noise {NOISE_PPM:.1f} ppm rms of the primary, separation "
          f"{R_SEP:.0f} m")
    f_noise = np.array([1.0, 3.0, 10.0, 30.0, 100.0, 300.0])
    noise = NOISE_PPM * 1e-6 * np.abs(RNG.standard_normal(f_noise.size)
                                      + 1j * RNG.standard_normal(f_noise.size)) / np.sqrt(2.0)
    print("\n   f (Hz)   quadrature(ppm)   noise(ppm)   sigma_app(S/m)"
          "   error on sigma_app")
    for f, n in zip(f_noise, noise):
        q = secondary_ratio(f, SIGMA_RES, R_SEP, 0.0).imag
        sigma_app = 4.0 * q / (2.0 * np.pi * f * MU0 * R_SEP ** 2)
        err = sigma_app * (n / abs(q))
        print(f"  {f:8.0f}   {q * 1e6:15.2f}   {n * 1e6:10.2f}   "
              f"{sigma_app:14.5f}   {err:.5f}")
    print("  the apparent conductivity is the LIN formula inverted; its error is")
    print("  (noise/quadrature) x sigma.  The drift of sigma_app from the true")
    print("  0.0050 S/m across the band is the LIN bias measured in section 5(c),")
    print("  not noise: the 1 Hz estimate is unbiased but noise-limited, the 300 Hz")
    print("  estimate is quiet but biased low.  A detection limit for a FDEM system")
    print("  is therefore a statement about a conductivity AND a frequency AND a")
    print("  geometry AND an acceptable bias, never a single number.")


if __name__ == "__main__":
    main()
