#!/usr/bin/env python3
"""Downhole induction logging: skin depth, the exact homogeneous-medium
response, Doll's geometric factor, and the shoulder effect of a thin bed.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python downhole_em_logging_demo.py

EVERYTHING IS SYNTHETIC.  The tool spacings, frequencies and formation
conductivities are chosen teaching values, not measurements from a site or
specifications of any instrument.  Only mu0, the flux identity and the
speed-of-light family of constants are standard.

Contents
--------
1. Skin depth: delta = sqrt(2/(omega mu sigma)) = 503.3 sqrt(rho/f) m.
2. Verification of the ring-flux identity used to build Doll's factor.
3. Doll's geometric factor: normalisation, vertical response, and how much of
   the reading comes from near the sonde.
4. Shoulder effect: a 1 m bed read by a 1 m and a 0.5 m sonde.
5. The exact homogeneous two-coil response, its small-p skin-effect expansion,
   the apparent-conductivity bias it causes, and an independent solution check.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi          # H/m
L_SONDE = 1.0                 # m, coil spacing of the SYNTHETIC tool
F_TOOL = 20e3                 # Hz, operating frequency of the SYNTHETIC tool


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def skin_depth(rho_ohm_m, freq):
    """Planar skin depth in m for resistivity rho (ohm m) and frequency f (Hz)."""
    return np.sqrt(2.0 * rho_ohm_m / (2.0 * np.pi * freq * MU0))


def ring_flux_numeric(rho, z, m):
    """Flux through a coaxial ring of radius rho at axial offset z, by quadrature.

    B_z(rho', z) = (mu0 m / 4 pi) (2 z^2 - rho'^2) / (rho'^2 + z^2)^{5/2}
    """
    gp, wp = leggauss(600)
    rp = 0.5 * rho * (gp + 1.0)
    wr = 0.5 * rho * wp
    r2 = rp ** 2 + z ** 2
    bz = (MU0 * m / (4.0 * np.pi)) * (2.0 * z ** 2 - rp ** 2) / r2 ** 2.5
    return float(np.sum(wr * 2.0 * np.pi * rp * bz))


def ring_flux_analytic(rho, z, m):
    """Closed form (mu0 m / 2) rho^2 / r^3, r = sqrt(rho^2 + z^2)."""
    r = np.sqrt(rho ** 2 + z ** 2)
    return 0.5 * MU0 * m * rho ** 2 / r ** 3


def doll_kernel(rho, z, L):
    """Doll geometric-factor density (unnormalised) for two coaxial coils.

    From Doll's ring-current argument the contribution of a ring of radius rho
    at axial offset z from the sonde centre is proportional to
        rho^2 / (r_T^3 r_R^3),   r_T^2 = rho^2 + (z - L/2)^2,
                                 r_R^2 = rho^2 + (z + L/2)^2.
    """
    rT = np.sqrt(rho ** 2 + (z - 0.5 * L) ** 2)
    rR = np.sqrt(rho ** 2 + (z + 0.5 * L) ** 2)
    return rho ** 2 / (rT ** 3 * rR ** 3)


def kernel_volume_integral(L, z_max=60.0, n_rho=400, n_z=1201):
    """Unnormalised integral of the Doll kernel over the whole space, per offset."""
    gz, wz = leggauss(n_rho * 4)
    rho = 0.5 * (z_max) * (gz + 1.0)
    wrho = 0.5 * z_max * wz
    zs = np.linspace(-z_max, z_max, n_z)
    dz = zs[1] - zs[0]
    gv = np.zeros_like(zs)
    total = 0.0
    for k, z in enumerate(zs):
        g = doll_kernel(rho, z, L)
        gv[k] = float(np.sum(wrho * 2.0 * np.pi * rho * g))
    # trapezoid in z (the integrand decays rapidly)
    total = float(np.trapezoid(gv, zs))
    return gv, zs, total


def main():
    section("1. Skin depth in a conducting medium")
    print("Ampere and Faraday give, for a plane wave in a conductor,")
    print("    delta = sqrt(2 / (omega mu sigma)) = sqrt(2 rho / (omega mu))")
    factor = np.sqrt(2.0 / (2.0 * np.pi * MU0))
    print(f"mu0 = {MU0:.10e} H/m")
    print(f"so delta = sqrt(2 rho/(2 pi f mu0)) = {factor:.4f} sqrt(rho/f) m")
    print("with rho in ohm m and f in Hz: the familiar 503.3 sqrt(rho/f) m.")
    print("\n  f (Hz)   rho (ohm m)   delta (m)   induction number p = L/delta")
    for freq in (1e3, 10e3, F_TOOL, 100e3):
        for rho in (1.0, 10.0, 100.0):
            d = skin_depth(rho, freq)
            print(f"  {freq:8.0f}  {rho:11.1f}   {d:9.4f}   {L_SONDE / d:8.4f}")
    print("p < 1 is the induction (low-frequency) regime; p > 1 is the wave")
    print("regime, where the tool reads a mixture of conductivity and distance.")

    section("2. Verification of the ring-flux identity")
    print("Magnetic dipole moment m along z.  The axial field is")
    print("    B_z(rho,z) = (mu0 m/4 pi)(2 z^2 - rho^2)/(rho^2+z^2)^{5/2}")
    print("and integrating it over a coaxial disc of radius rho gives")
    print("    Phi(rho,z) = (mu0 m / 2) rho^2 / r^3,   r = sqrt(rho^2+z^2).")
    m = 1.0
    print("\n   z (m)   rho (m)   Phi numeric       Phi closed form   ratio")
    for z, rho in ((0.25, 0.5), (0.5, 1.0), (1.0, 1.0), (2.0, 1.0), (2.0, 4.0)):
        num = ring_flux_numeric(rho, z, m)
        ana = ring_flux_analytic(rho, z, m)
        print(f"  {z:6.1f}  {rho:8.1f}   {num:.8e}   {ana:.8e}   "
              f"{num / ana:8.6f}")
    print("The identity is what lets Doll's geometric factor be written as a")
    print("product of two coil responses rather than as a double volume integral.")
    print("The case z = 0 is excluded: a ring lying in the dipole's equatorial")
    print("plane has a logarithmically divergent flux linkage in the point-dipole")
    print("model, so the identity is used only at offsets away from the coil plane.")

    section("3. Doll's geometric factor: normalisation and reach")
    L = L_SONDE
    gv, zs, total = kernel_volume_integral(L)
    gv = gv / total
    print(f"SYNTHETIC sonde spacing L = {L:.2f} m, frequency "
          f"{F_TOOL / 1e3:.1f} kHz")
    print(f"unnormalised kernel integral over all space = {total:.6e} m^3")
    print(f"check: integral of the normalised vertical response g_v(z) dz = "
          f"{np.trapezoid(gv, zs):.8f}   (must be 1)")
    print("\nvertical response g_v(z), in 1/m:")
    for zq in (0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0):
        i = np.argmin(np.abs(zs - zq))
        print(f"   z = {zq:5.2f} m:  g_v = {gv[i] * L:8.4f}  (x L)")
    half = np.abs(zs) <= 0.5 * L
    one = np.abs(zs) <= L
    two = np.abs(zs) <= 2.0 * L
    print(f"\nfraction of the vertical response within |z| <= L/2 = "
          f"{np.trapezoid(gv[half], zs[half]) * 1.0:.4f}")
    print(f"fraction within |z| <= L   = "
          f"{np.trapezoid(gv[one], zs[one]):.4f}")
    print(f"fraction within |z| <= 2L  = "
          f"{np.trapezoid(gv[two], zs[two]):.4f}")
    exact_flat = 2.0 * np.pi / (L ** 2 * total)
    print(f"\nanalytic check: for |z| <= L/2 the unnormalised vertical response is")
    print(f"exactly 2 pi/L^2 = {2.0 * np.pi / L ** 2:.6f} 1/m, so the normalised")
    print(f"value should be 2 pi/(L^2 * total) = {exact_flat:.6f} 1/m")
    for zq in (0.0, 0.25, 0.5):
        i = np.argmin(np.abs(zs - zq))
        print(f"   z = {zq:5.2f} m: numeric {gv[i]:.6f}, analytic {exact_flat:.6f}, "
              f"ratio {gv[i] / exact_flat:.6f}")
    print("analytic check: for large |z| the unnormalised response tends to")
    print("pi/(2 z^2), so g_v(z) z^2 / total -> pi/2:")
    for zq in (2.0, 3.0, 5.0, 8.0):
        i = np.argmin(np.abs(zs - zq))
        print(f"   z = {zq:5.2f} m: numeric {gv[i] * total * zq ** 2:.4f}, "
              f"pi/2 = {0.5 * np.pi:.4f}")
    print("A sonde of spacing L therefore averages the formation over a vertical")
    print("window of order L, with 1/z^2 tails that reach far.  That window, not")
    print("the depth sampling, is the vertical resolution of the measurement.")

    section("4. Shoulder effect: a thin bed read by two sonde lengths")
    z_bed, h_bed = 10.0, 1.0          # m, centre and thickness of the bed
    sig_bed, sig_bg = 1.0, 0.10       # S/m, SYNTHETIC conductivities
    zlog = np.linspace(4.0, 16.0, 241)
    sigma = np.where(np.abs(zlog - z_bed) <= 0.5 * h_bed, sig_bed, sig_bg)
    print(f"SYNTHETIC model: a {h_bed:.1f} m bed of {sig_bed:.2f} S/m in a "
          f"{sig_bg:.2f} S/m background")
    for Ltest in (1.0, 0.5, 0.25):
        gvL, zsL, totL = kernel_volume_integral(Ltest)
        gvL = gvL / totL
        sigma_a = np.convolve(sigma, gvL * (zsL[1] - zsL[0]), mode="same")
        peak = sigma_a.max()
        print(f"  sonde spacing L = {Ltest:.2f} m: peak apparent conductivity "
              f"= {peak:.4f} S/m")
        print(f"      that is {100.0 * peak / sig_bed:5.1f}% of the true bed "
              f"value {sig_bed:.2f} S/m")
    print("The reading never reaches the bed value: the tool averages over the")
    print("shoulders.  A thicker bed or a shorter sonde reads closer to the truth,")
    print("and the deficit is a measurement property, not a logging error.")

    section("5. Exact homogeneous two-coil response and skin effect")
    print("For a point magnetic dipole in a homogeneous whole space the mutual")
    print("coupling normalised to its free-space value is")
    print("    Z/Z0 = (1 + i k L) exp(-i k L),   k = (1 + i)/delta")
    print("with p = L/delta this is Z/Z0 = (1 - p + i p) exp(p - i p).")
    print("\n     p     In-phase      Quadrature   sigma_a/sigma = Q/p^2")
    rows = []
    for p in (0.05, 0.1, 0.2, 0.5, 0.8, 1.0, 1.4, 1.57, 2.0, 2.5, 3.0):
        z = (1.0 - p + 1j * p) * np.exp(p - 1j * p)
        q = z.imag
        rows.append((p, z.real, q, q / p ** 2))
        print(f"  {p:5.2f}   {z.real:9.5f}   {q:11.5f}   {q / p ** 2:12.5f}")
    ps = np.linspace(1e-4, 4.0, 40001)
    zz = (1.0 - ps + 1j * ps) * np.exp(ps - 1j * ps)
    ratio = zz.imag / ps ** 2
    ipk = int(np.argmax(ratio))
    print(f"\napparent conductivity from the quadrature, sigma_a/sigma:")
    print(f"  maximum {ratio[ipk]:.4f} at p = {ps[ipk]:.3f}")
    i5 = int(np.argmax(np.abs(ratio - 1.0) > 0.05))
    i1 = int(np.argmax(np.abs(ratio - 1.0) > 0.01))
    print(f"  within 1% of 1 for p <= {ps[i1 - 1]:.4f}; "
          f"within 5% for p <= {ps[i5 - 1]:.4f}")
    print("  leading bias: sigma_a/sigma - 1 ~ (2/3) p, so it grows as "
          "sqrt(sigma)")
    for pchk in (0.1, 0.2, 0.3):
        j = int(np.argmin(np.abs(ps - pchk)))
        print(f"     p = {pchk:.1f}: measured bias {100 * (ratio[j] - 1):+.3f}%, "
              f"formula (2/3)p = {100 * 2.0 / 3.0 * pchk:+.3f}%")
    print(f"  for p = {ps[ipk]:.3f} the quadrature reading overstates conduction "
          f"by {100 * (ratio[ipk] - 1):.1f}%")
    p_tool = L_SONDE / skin_depth(1.0, F_TOOL)
    r_tool = ((1.0 - p_tool + 1j * p_tool) * np.exp(p_tool - 1j * p_tool)).imag \
        / p_tool ** 2
    print(f"  for the SYNTHETIC tool (L = {L_SONDE:.2f} m, "
          f"{F_TOOL / 1e3:.0f} kHz) in a 1 ohm m formation:")
    print(f"     delta = {skin_depth(1.0, F_TOOL):.4f} m, p = {p_tool:.4f}, "
          f"skin-effect bias = {100 * (r_tool - 1):.2f}%")
    small = np.array([1e-3, 1e-2, 1e-1])
    zs_ = (1.0 - small + 1j * small) * np.exp(small - 1j * small)
    print("\nsmall-p series check: the expansion is Z/Z0 = 1 + i p^2 +"
          " (2/3)(1+i) p^3 + ...")
    for p in small:
        z = (1.0 - p + 1j * p) * np.exp(p - 1j * p)
        print(f"  p = {p:.0e}:  Im exact {z.imag:.6e},  p^2 = {p ** 2:.6e},  "
              f"ratio {z.imag / p ** 2:.6f}")
        print(f"              Re-1 exact {z.real - 1:.6e},  "
              f"(2/3)p^3 = {2.0 / 3.0 * p ** 3:.6e},  "
              f"ratio {(z.real - 1) / (2.0 / 3.0 * p ** 3):.6f}")
    print("So the QUADRATURE is linear in sigma while the IN-PHASE deviation goes")
    print("as sigma^(3/2): the quadrature is the calibration channel and the")
    print("in-phase is the skin-effect channel.")

    print("\nindependent check: does g(r) = (1+i k r) exp(-i k r)/r^2 solve the")
    print("radial wave equation g'' + (2/r) g' + (k^2 - 2/r^2) g = 0 ?")
    for p in (0.3, 1.0, 2.0):
        k = (1.0 + 1j) * p / L_SONDE
        r = np.linspace(0.35 * L_SONDE, 30.0 * L_SONDE, 40001)
        g = (1.0 + 1j * k * r) * np.exp(-1j * k * r) / r ** 2
        h = r[1] - r[0]
        g1 = np.gradient(g, h)
        g2 = np.gradient(g1, h)
        res = g2 + (2.0 / r) * g1 + (k ** 2 - 2.0 / r ** 2) * g
        rel = np.max(np.abs(res[5:-5])) / np.max(np.abs(k ** 2 * g))
        print(f"  p = {p:.1f}: max |residual| / |k^2 g| = {rel:.3e}")
    print("The residual is at finite-difference truncation level, so the closed")
    print("form used for the skin-effect analysis is verified independently of")
    print("the algebra that produced it.")


if __name__ == "__main__":
    main()
