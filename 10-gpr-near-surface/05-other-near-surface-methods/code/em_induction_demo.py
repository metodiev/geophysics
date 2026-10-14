#!/usr/bin/env python3
"""EM induction (small-loop conductivity meter): skin depth, induction number,
and the low-induction-number (LIN) depth weighting computed from reciprocity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_induction_demo.py

Everything here is SYNTHETIC.  The coil radius, spacings, frequencies and soil
conductivities are chosen teaching values, not instrument specifications and not
measurements.  No field site is modelled.

Model
-----
Both coils are modelled as circular loops of finite radius in the horizontal
coplanar (HCP) mode: two coaxial vertical magnetic dipoles, axes a distance s
apart.  In the low-induction-number limit the eddy currents in the ground are
driven by the primary field alone, so the secondary coupling of a thin layer at
depth z is bilinear in the two coils' vector potentials:

    w(z) = INT (A1 . A2) dA over the plane at depth z,

and the apparent conductivity of a layered ground follows the additive rule

    sigma_a = SUM_i sigma_i W_i ,   W_i = (1/I) * INT_{layer i} w dz.

The weights W_i are normalised by I = INT_0^inf w dz, which is exactly the
calibration convention of a conductivity meter: a homogeneous half-space returns
its own conductivity.

Contents
--------
1. Skin depth and induction number for teaching soils and frequencies.
2. Verification of the loop vector potential against the Neumann line integral.
3. LIN depth weighting w(z): two spacings, quadrature convergence, cumulative
   sensitivity and depth of investigation.
4. Apparent conductivity of layered models and the equivalence (non-uniqueness)
   of two- and three-layer ground.
"""

import numpy as np
from scipy.special import ellipk, ellipe

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi          # H/m, exact SI constant
A_LOOP = 0.25                 # m, teaching value for the coil radius
S_SHALLOW = 1.00              # m, small inter-coil spacing
S_DEEP = 2.50                 # m, larger inter-coil spacing
F_LOW = 9.8e3                 # Hz, teaching value
F_HIGH = 24.5e3               # Hz, teaching value
SIGMA_SOIL = (0.010, 0.030, 0.100)   # S/m, teaching values
SIGMA_SALINE = 1.000          # S/m, a saline soil, teaching value


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def skin_depth(sigma_s_per_m, f_hz):
    """Diffusion skin depth sqrt(2/(omega mu0 sigma)), in metres."""
    omega = 2.0 * np.pi * f_hz
    return np.sqrt(2.0 / (omega * MU0 * sigma_s_per_m))


def induction_number(s_m, sigma_s_per_m, f_hz):
    """Dimensionless ratio s/delta of spacing to skin depth."""
    return s_m / skin_depth(sigma_s_per_m, f_hz)


def a_phi_closed(a_m, rho_m, z_m, cur=1.0):
    """Vector potential A_phi of a circular loop of radius a at (rho, z)."""
    rho = np.maximum(np.asarray(rho_m, dtype=float), 1e-12)
    k2 = 4.0 * a_m * rho / ((a_m + rho) ** 2 + z_m * z_m)
    k2 = np.clip(k2, 0.0, 1.0 - 1e-14)
    k = np.sqrt(k2)
    return (MU0 * cur / (np.pi * k)) * np.sqrt(a_m / rho) * (
        (1.0 - 0.5 * k2) * ellipk(k2) - ellipe(k2))


def a_phi_neumann(a_m, rho_m, z_m, cur=1.0, nphi=20001):
    """Same quantity from the defining Neumann integral, for verification."""
    phi = np.linspace(0.0, 2.0 * np.pi, nphi)
    dist = np.sqrt(a_m ** 2 + rho_m ** 2 + z_m ** 2 - 2.0 * a_m * rho_m * np.cos(phi))
    return MU0 * cur / (4.0 * np.pi) * np.trapezoid(a_m * np.cos(phi) / dist, phi)


def plane_weight(z_m, s_m, a_m=A_LOOP, nr=300, nt=240, rmax=8.0):
    """LIN per-depth weight w(z) = INT (A1 . A2) dA in polar coordinates."""
    xg, wg = np.polynomial.legendre.leggauss(nr)
    r = 0.5 * rmax * (xg + 1.0)
    wr = 0.5 * rmax * wg
    tg, wt = np.polynomial.legendre.leggauss(nt)
    t = np.pi * (tg + 1.0)
    wt = np.pi * wt
    x = 0.5 * s_m + r[:, None] * np.cos(t)[None, :]
    y = r[:, None] * np.sin(t)[None, :]
    rho1 = np.hypot(x, y)
    rho2 = np.hypot(x - s_m, y)
    dot = (rho1 ** 2 - x * s_m) / (rho1 * rho2)
    integrand = a_phi_closed(a_m, rho1, z_m) * a_phi_closed(a_m, rho2, z_m) * dot
    return float(np.sum(integrand * (r * wr)[:, None] * wt[None, :]))


def weight_curve(s_m, z_max=8.0, nz=241, **kw):
    z = np.linspace(0.002, z_max, nz)
    return z, np.array([plane_weight(zi, s_m, **kw) for zi in z])


def cumulative_fraction(z, w):
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (w[1:] + w[:-1]) * np.diff(z))])
    return cum / cum[-1]


def layer_weights(z, w, edges):
    """Normalised weight of each layer bounded by the edges of `edges`."""
    cum = cumulative_fraction(z, w)
    frac = [float(np.interp(e, z, cum)) for e in edges]
    return np.diff(frac)


def apparent_conductivity(z, w, edges, sigmas):
    """LIN apparent conductivity of a layered ground (weights normalised to 1)."""
    weights = layer_weights(z, w, edges)
    return float(np.sum(np.asarray(sigmas) * weights)), weights


def main():
    section("1. Skin depth and induction number")
    print("sigma (mS/m)   f (kHz)   delta (m)      B = s/delta")
    for sigma in SIGMA_SOIL + (SIGMA_SALINE,):
        for f in (F_LOW, F_HIGH):
            delta = skin_depth(sigma, f)
            print(f"{sigma * 1e3:11.0f}   {f / 1e3:7.1f}   {delta:10.2f}   "
                  f"{S_SHALLOW / delta:9.3f}   {S_DEEP / delta:9.3f}")
    print("Two columns of B are shown: spacing 1.00 m and 2.50 m.")
    print("LIN theory assumes B << 1; the entries above it are flagged by eye.")

    section("2. Verification: loop vector potential, closed form vs Neumann integral")
    for a, rho, z in ((A_LOOP, 0.60, 0.0), (A_LOOP, 0.30, 0.50), (A_LOOP, 0.05, 0.02)):
        closed = a_phi_closed(a, rho, z)
        direct = a_phi_neumann(a, rho, z)
        print(f"  a={a:.2f} m rho={rho:.2f} m z={z:.2f} m: closed={closed:.6e} "
              f"Neumann={direct:.6e} rel.dev={abs(closed - direct) / abs(direct):.2e}")
    print("  units of A_phi: T m (kg m s^-2 A^-1)")

    section("3. LIN depth weighting for the horizontal coplanar (HCP) mode")
    z_s, w_s = weight_curve(S_SHALLOW, z_max=12.0, nz=321)
    z_d, w_d = weight_curve(S_DEEP, z_max=12.0, nz=321)
    z_c, w_c = weight_curve(S_SHALLOW, z_max=12.0, nz=161, nr=150, nt=120)
    cum_c = cumulative_fraction(z_c, w_c)
    cum_s = cumulative_fraction(z_s, w_s)
    doi_c = float(np.interp(0.5, cum_c, z_c))
    doi_s = float(np.interp(0.5, cum_s, z_s))
    wl_c = layer_weights(z_c, w_c, (0.0, 0.5, 1.5, 12.0))
    wl_s = layer_weights(z_s, w_s, (0.0, 0.5, 1.5, 12.0))
    print("  quadrature convergence, spacing 1.00 m: 150x120 nodes vs 300x240 nodes")
    print(f"    depth containing 50% of the response: {doi_c:.4f} m vs {doi_s:.4f} m "
          f"(difference {abs(doi_c - doi_s) * 1e3:.2f} mm)")
    print(f"    layer weights 0-0.5 m / 0.5-1.5 m / 1.5-12 m: "
          f"{wl_c[0]:.4f} {wl_c[1]:.4f} {wl_c[2]:.4f} vs "
          f"{wl_s[0]:.4f} {wl_s[1]:.4f} {wl_s[2]:.4f}")
    tail_frac = float(np.trapezoid(w_s[z_s > 8.0], z_s[z_s > 8.0])
                      / np.trapezoid(w_s, z_s))
    print(f"    weight below z = 8 m as a fraction of the whole: {tail_frac:.2e}")
    print("\n   z (m)     w(z), s=1.00 m     w(z), s=2.50 m")
    for zi in (0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 4.00):
        print(f"  {zi:6.2f}   {np.interp(zi, z_s, w_s):.6e}    {np.interp(zi, z_d, w_d):.6e}")
    i_min_d = int(np.argmin(w_d))
    print(f"  sign check, s = 2.50 m: minimum w = {w_d[i_min_d]:.3e} at z = "
          f"{z_d[i_min_d]:.3f} m, which is {abs(w_d[i_min_d]) / w_d.max() * 100:.1f}% "
          f"of the peak magnitude: the weight is not sign-definite near the coils.")
    print("\n  cumulative fraction of the LIN response above depth z:")
    cum_d = cumulative_fraction(z_d, w_d)
    print("    fraction   z (s=1.00 m)   z/s      z (s=2.50 m)   z/s")
    for target in (0.10, 0.25, 0.50, 0.75, 0.90):
        z_a = float(np.interp(target, cum_s, z_s))
        z_b = float(np.interp(target, cum_d, z_d))
        print(f"    {target:8.2f}   {z_a:12.3f}   {z_a / S_SHALLOW:6.3f}   "
              f"{z_b:12.3f}   {z_b / S_DEEP:6.3f}")

    section("4. Apparent conductivity of layered ground (LIN superposition)")
    print("\n(a) homogeneous half-space check (the calibration convention):")
    for sigma in SIGMA_SOIL:
        edges = (0.0, 0.5, 1.0, 2.0, 4.0, 12.0)
        sa, wts = apparent_conductivity(z_s, w_s, edges, [sigma] * 5)
        print(f"    sigma = {sigma * 1e3:5.1f} mS/m -> sigma_a = {sa * 1e3:5.1f} mS/m "
              f"(layer weights sum to {wts.sum():.12f})")

    sig_hs = 0.020
    print("\n(b) two-layer ground over a 20 mS/m half-space")
    print("    model A: 0.50 m of 100 mS/m;  model B: 1.50 m of X mS/m")
    sa_A, w_A = apparent_conductivity(z_s, w_s, (0.0, 0.50, 12.0), [0.100, sig_hs])
    sd_A, w_A_d = apparent_conductivity(z_d, w_d, (0.0, 0.50, 12.0), [0.100, sig_hs])
    print(f"    A at s = 1.00 m: sigma_a = {sa_A * 1e3:.2f} mS/m")
    print(f"    A at s = 2.50 m: sigma_a = {sd_A * 1e3:.2f} mS/m")
    _, w_B = apparent_conductivity(z_s, w_s, (0.0, 1.50, 12.0), [1.0, sig_hs])
    sig_B = (sa_A - sig_hs * w_B[1]) / w_B[0]
    sb_B, w_B_d = apparent_conductivity(z_d, w_d, (0.0, 1.50, 12.0), [sig_B, sig_hs])
    print(f"    B with the same reading at s = 1.00 m needs sigma = {sig_B * 1e3:.2f} mS/m")
    print(f"    B at s = 2.50 m: sigma_a = {sb_B * 1e3:.2f} mS/m  "
          f"({(sb_B - sd_A) / sd_A * 100:+.1f}% against model A)")
    print(f"    layer weights at s = 1.00 m: A = {w_A[0]:.4f}, B = {w_B[0]:.4f};")
    print(f"    layer weights at s = 2.50 m: A = {w_A_d[0]:.4f}, B = {w_B_d[0]:.4f}")

    print("\n(c) a 1 m thick conductive lens (200 mS/m) in a 20 mS/m host")

    def lens_model(top, thick=1.0, sig_lens=0.200, sig_host=sig_hs, z_max=12.0):
        edges = [0.0]
        sigmas = []
        if top > 0.0:
            edges.append(top)
            sigmas.append(sig_host)
        edges.append(top + thick)
        sigmas.append(sig_lens)
        edges.append(z_max)
        sigmas.append(sig_host)
        i_lens = 1 if top > 0.0 else 0
        return tuple(edges), sigmas, i_lens

    for top in (0.0, 0.5, 1.0, 2.0, 3.0):
        edges, sigmas, i_lens = lens_model(top)
        sa, wl = apparent_conductivity(z_s, w_s, edges, sigmas)
        sd, wl_d = apparent_conductivity(z_d, w_d, edges, sigmas)
        print(f"    lens {top:.1f}-{top + 1:.1f} m: sigma_a = {sa * 1e3:6.2f} mS/m at "
              f"s = 1.00 m (lens weight {wl[i_lens]:.4f}), "
              f"{sd * 1e3:6.2f} mS/m at s = 2.50 m "
              f"(lens weight {wl_d[i_lens]:.4f})")

    section("5. Summary")
    print("  Skin depth falls as 1/sqrt(sigma f); the induction number B = s/delta sets")
    print("  whether the LIN (linear) interpretation of the reading is defensible.")
    print("  Within LIN, a reading is a weighted depth average of conductivity, and the")
    print("  weights are the quantity computed in section 3.  A reading is therefore not")
    print("  a conductivity, and two different layered grounds can give the same reading.")


if __name__ == "__main__":
    main()
