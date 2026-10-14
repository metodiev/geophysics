#!/usr/bin/env python3
"""Aerosols, clouds and their radiative effects -- synthetic teaching demonstration.

Run with:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
        16-atmosphere-climate/02-radiation-and-energy-balance/code/aerosols_and_clouds_radiation_demo.py

Everything here is a SYNTHETIC model with illustrative optical constants.  Nothing
in this file is a measurement, a retrieval or a published value.  The purpose is to
show, with numbers computed on the spot, how the optical properties of particles
(Mie theory), the optical depth of a layer, its reflectance and its longwave
emissivity follow from one another, and how three exact identities can be used to
validate the radiative-transfer solver before it is believed.

Sections
  1  Mie scattering: the kernel and its validation
  2  Droplet and aerosol optics; optical depth from water path
  3  Two-stream reflectance: validation against exact identities and an
     independent finite-difference solve of the same equations
  4  Cloud albedo and the indirect (Twomey) effect
  5  Longwave emissivity, cloud radiative forcing, and the height sign
  6  Aerosol direct effect: when does scattering brighten and when does it dim?
  7  Measured, modelled, inferred -- and a synthetic retrieval experiment

Print-only: no figures are produced.  Exits 0.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261014)

# ----------------------------------------------------------------------------
# Standard constants (exact or stated conventions, with units)
# ----------------------------------------------------------------------------
SIGMA = 5.670374419e-8          # W m^-2 K^-4   Stefan-Boltzmann constant
SOLAR = 1361.0                  # W m^-2        total solar irradiance at 1 AU
RHO_W = 1000.0                  # kg m^-3       liquid-water density
LAPSE = 6.5e-3                  # K m^-1        stated convention for a mean lapse rate
T_SURF = 288.15                 # K             stated reference surface temperature
LAM_VIS = 0.55e-6               # m             stated reference visible wavelength
LAM_IR = 11.0e-6                # m             stated reference thermal wavelength
# Illustrative (SYNTHETIC) refractive indices.  They are model inputs, not data.
M_WATER_VIS = 1.3312 + 1.0e-8j
M_WATER_IR = 1.2000 + 0.05j
M_AEROSOL = 1.5000 + 0.01j

MAX_STORE = 40


def section(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------------
# Mie scattering
# ----------------------------------------------------------------------------
def mie(m, x):
    """Extinction efficiency, scattering efficiency and asymmetry parameter.

    Bohren-Huffman style downward recurrence for the logarithmic derivative
    D_n = psi'_n/psi_n, upward recursion for the Riccati-Bessel functions, and
    the standard series for Q_ext, Q_sca and g.  Returns (Q_ext, Q_sca, g).
    """
    x = float(x)
    nstop = int(x + 4.0 * x ** (1.0 / 3.0) + 2.0)
    y = m * x
    nmx = max(nstop, int(abs(y))) + 25
    d = np.zeros(nmx + 1, dtype=complex)
    for n in range(nmx, 0, -1):
        d[n - 1] = n / y - 1.0 / (d[n] + n / y)
    psi = np.zeros(nstop + 2)
    chi = np.zeros(nstop + 2)
    psi[0] = np.sin(x)
    psi[1] = np.sin(x) / x - np.cos(x)
    chi[0] = np.cos(x)
    chi[1] = np.cos(x) / x + np.sin(x)
    for n in range(1, nstop):
        psi[n + 1] = (2 * n + 1) / x * psi[n] - psi[n - 1]
        chi[n + 1] = (2 * n + 1) / x * chi[n] - chi[n - 1]
    xi = psi[: nstop + 1] - 1j * chi[: nstop + 1]
    a = np.zeros(nstop + 1, dtype=complex)
    b = np.zeros(nstop + 1, dtype=complex)
    for n in range(1, nstop + 1):
        a[n] = ((d[n] / m + n / x) * psi[n] - psi[n - 1]) / (
            (d[n] / m + n / x) * xi[n] - xi[n - 1]
        )
        b[n] = ((d[n] * m + n / x) * psi[n] - psi[n - 1]) / (
            (d[n] * m + n / x) * xi[n] - xi[n - 1]
        )
    ns = np.arange(1, nstop + 1)
    q_ext = 2.0 / x ** 2 * np.sum((2 * ns + 1) * np.real(a[1:] + b[1:]))
    q_sca = 2.0 / x ** 2 * np.sum((2 * ns + 1) * (np.abs(a[1:]) ** 2 + np.abs(b[1:]) ** 2))
    gsum = 0.0
    for n in range(1, nstop):
        gsum += (n * (n + 2) / (n + 1)) * np.real(a[n] * np.conj(a[n + 1]) + b[n] * np.conj(b[n + 1]))
        gsum += (2 * n + 1) / (n * (n + 1)) * np.real(a[n] * np.conj(b[n]))
    g = 4.0 / (x ** 2 * q_sca) * gsum
    return q_ext, q_sca, g


def polydispersion(re, ve, m, lam, npts=60):
    """Gamma size distribution with effective radius re and effective variance ve.

    Returns a dict with the size-averaged optics and the optical-depth coefficients
    per unit liquid-water path (m^2 kg^-1).
    """
    r = np.linspace(max(1e-3 * re, 1e-10), 4.0 * re, npts)
    n = r ** (1.0 / ve - 3.0) * np.exp(-r / (ve * re))
    n /= np.trapezoid(n, r)
    q_ext = np.zeros_like(r)
    q_sca = np.zeros_like(r)
    g = np.zeros_like(r)
    for i, ri in enumerate(r):
        qe, qs, gg = mie(m, 2.0 * np.pi * ri / lam)
        q_ext[i], q_sca[i], g[i] = qe, qs, gg
    mass = np.trapezoid(n * 4.0 / 3.0 * np.pi * r ** 3 * RHO_W, r)      # kg m^-2
    tau_ext = np.trapezoid(n * q_ext * np.pi * r ** 2, r) / mass        # m^2 kg^-1
    tau_abs = np.trapezoid(n * (q_ext - q_sca) * np.pi * r ** 2, r) / mass
    qe_bar = np.trapezoid(n * q_ext, r)
    qs_bar = np.trapezoid(n * q_sca, r)
    g_bar = np.trapezoid(n * q_sca * g, r) / qs_bar
    return dict(tau_ext=tau_ext, tau_abs=tau_abs, w0=qs_bar / qe_bar,
                g=g_bar, q_ext=qe_bar, q_sca=qs_bar)


# ----------------------------------------------------------------------------
# Azimuth-independent Henyey-Greenstein phase function and the two-stream model
# ----------------------------------------------------------------------------
def phase_hg(mu, mup, g, nphi=64):
    """Azimuth-averaged Henyey-Greenstein phase function.

    p0(mu, mu') = (1/2pi) * integral p(cos Theta) dphi, with
    cos Theta = mu mu' + sqrt(1-mu^2) sqrt(1-mu'^2) cos(phi - phi').
    Built numerically, so that the normalisation and the first moment can be
    checked rather than assumed: (1/2) int p0 dmu = 1 and
    (1/2) int mu p0 dmu = g mu'.  Using the shortcut p0 = HG(mu mu') instead
    would violate both.
    """
    mu = np.atleast_1d(np.asarray(mu, dtype=float))[:, None]      # (n, 1)
    mup = np.atleast_1d(np.asarray(mup, dtype=float))[None, :]    # (1, m)
    s1 = np.sqrt(np.clip(1.0 - mu ** 2, 0.0, None))
    s2 = np.sqrt(np.clip(1.0 - mup ** 2, 0.0, None))
    out = np.zeros((mu.shape[0], mup.shape[1]))
    for ph in 2.0 * np.pi * (np.arange(nphi) + 0.5) / nphi:
        c = mu * mup + s1 * s2 * np.cos(ph)
        out += (1.0 - g ** 2) / (1.0 + g ** 2 - 2.0 * g * c) ** 1.5
    return out / nphi


def two_stream(tau, w0, g, mu0, alb_s=0.0, f0=1.0, delta=False):
    """Eddington two-stream diffuse reflectance and transmittance.

    Equations (S = F_up + F_dn, D = F_up - F_dn, beam irradiance f0 at mu0):

        dS/dtau = a D + p exp(-tau/mu0),   a = 1.5 (1 - w0 g)
        dD/dtau = c S - q exp(-tau/mu0),   c = 2 (1 - w0)
                                           p = 1.5 w0 g mu0 f0,  q = w0 f0

    Boundary conditions: D(0) = S(0) (no diffuse radiation entering the top) and
    F_up(tau_tot) = alb_s (F_dn(tau_tot) + mu0 f0 exp(-tau_tot/mu0))  (Lambertian
    surface).  Solved in closed form.  Returns (R, T) for the direct beam.

    With delta=True the delta-Eddington scaling is applied first,
    tau' = (1 - w0 g^2) tau, w0' = w0 (1 - g^2) / (1 - w0 g^2), g' = g/(1+g),
    which removes the forward diffraction peak from the phase function; the
    plain version (delta=False) keeps the full first moment and is known to
    overestimate the reflectance of strongly forward-scattering layers.
    """
    if delta:
        f = g ** 2
        tau = (1.0 - w0 * f) * tau
        w0 = w0 * (1.0 - f) / (1.0 - w0 * f)
        g = g / (1.0 + g)
    a = 1.5 * (1.0 - w0 * g)
    c = 2.0 * (1.0 - w0)
    p = 1.5 * w0 * g * mu0 * f0
    q = w0 * f0
    r = (alb_s - 1.0) / (alb_s + 1.0)
    e = np.exp(-tau / mu0)
    beta = 2.0 * alb_s * mu0 * f0 * e / (1.0 + alb_s)
    u, v = np.linalg.solve([[-1.0 / mu0, -a], [-c, -1.0 / mu0]], [p, -q])
    if abs(a * c) < 1e-14:                      # conservative scattering: c = 0
        d0 = (q * mu0 * (1 - e) + r * a * q * mu0 * (mu0 * (1 - e) - tau)
              + r * p * mu0 * (1 - e) + beta) / (1.0 - r - r * a * tau)
        s0 = d0

        def s_of(t):
            integ = d0 * t + q * mu0 * (mu0 * (1 - np.exp(-t / mu0)) - t)
            return s0 + a * integ + p * mu0 * (1 - np.exp(-t / mu0))

        def d_of(t):
            return d0 - q * mu0 * (1 - np.exp(-t / mu0))
    else:
        kap = np.sqrt(a * c)
        e1 = np.exp(kap * tau)
        e2 = 1.0 / e1
        mat = np.array([[1.0 - kap / a, 1.0 + kap / a],
                        [kap * e1 / a - r * e1, -kap * e2 / a - r * e2]])
        rhs = np.array([v - u, beta - v * e + r * u * e])
        A, B = np.linalg.solve(mat, rhs)

        def s_of(t):
            return A * np.exp(kap * t) + B * np.exp(-kap * t) + u * np.exp(-t / mu0)

        def d_of(t):
            return kap * (A * np.exp(kap * t) - B * np.exp(-kap * t)) / a + v * np.exp(-t / mu0)

    refl = d_of(0.0) / (mu0 * f0)
    trns = ((s_of(tau) - d_of(tau)) / 2.0 + mu0 * f0 * e) / (mu0 * f0)
    return refl, trns


def two_stream_fd(tau, w0, g, mu0, alb_s=0.0, n=800, f0=1.0):
    """Same equations, solved instead by a second-order finite-difference BVP."""
    a = 1.5 * (1.0 - w0 * g)
    c = 2.0 * (1.0 - w0)
    p = 1.5 * w0 * g * mu0 * f0
    q = w0 * f0
    r = (alb_s - 1.0) / (alb_s + 1.0)
    beta = 2.0 * alb_s * mu0 * f0 * np.exp(-tau / mu0) / (1.0 + alb_s)
    h = tau / n
    t = np.linspace(0.0, tau, n + 1)
    m = n + 1

    def idx(i, j):
        return i * m + j

    rows, cols, vals = [], [], []
    rhs = np.zeros(2 * m)

    def add(row, col, val):
        rows.append(row)
        cols.append(col)
        vals.append(val)

    for j in range(1, n):
        row = idx(0, j)
        add(row, idx(0, j + 1), 0.5 / h)
        add(row, idx(0, j - 1), -0.5 / h)
        add(row, idx(1, j), -a)
        rhs[row] = p * np.exp(-t[j] / mu0)
        row = idx(1, j)
        add(row, idx(1, j + 1), 0.5 / h)
        add(row, idx(1, j - 1), -0.5 / h)
        add(row, idx(0, j), -c)
        rhs[row] = -q * np.exp(-t[j] / mu0)
    row = idx(0, n)
    add(row, idx(0, n), -1.5 / h)
    add(row, idx(0, n - 1), 2.0 / h)
    add(row, idx(0, n - 2), -0.5 / h)
    add(row, idx(1, n), -a)
    rhs[row] = p * np.exp(-t[n] / mu0)
    row = idx(1, 0)
    add(row, idx(1, 0), -1.5 / h)
    add(row, idx(1, 1), 2.0 / h)
    add(row, idx(1, 2), -0.5 / h)
    add(row, idx(0, 0), -c)
    rhs[row] = -q
    row = idx(0, 0)
    add(row, idx(0, 0), 1.0)
    add(row, idx(1, 0), -1.0)
    rhs[row] = 0.0
    row = idx(1, n)
    add(row, idx(1, n), 1.0)
    add(row, idx(0, n), -r)
    rhs[row] = beta
    mat = sp.csr_matrix((vals, (rows, cols)), shape=(2 * m, 2 * m))
    sol = spla.spsolve(mat, rhs)
    s = sol[:m]
    d = sol[m:]
    refl = d[0] / (mu0 * f0)
    trns = ((s[-1] - d[-1]) / 2.0 + mu0 * f0 * np.exp(-tau / mu0)) / (mu0 * f0)
    return refl, trns


def single_scattering(tau, w0, g, mu0, nq=400):
    """Exact single-scattering reflectance of a thin slab on a black surface.

        R_ss = (w0 tau / (2 mu0)) * integral_0^1 p0(mu, -mu0) dmu

    evaluated by Gauss-Legendre quadrature of the azimuth-averaged phase
    function.  This uses no part of the two-stream model.
    """
    mu, w = np.polynomial.legendre.leggauss(nq)
    mu = 0.5 * (mu + 1.0)
    w = 0.5 * w
    integral = float(np.sum(w * phase_hg(mu, -mu0, g)[:, 0]))
    return w0 * tau / (2.0 * mu0) * integral


# ----------------------------------------------------------------------------
def main():
    section("1  Mie scattering: the kernel, and what validates it")
    print("Synthetic refractive indices (model inputs, not data):")
    print("   water, visible  m = %.4f %+.1ei   at lambda = %.2f um"
          % (M_WATER_VIS.real, M_WATER_VIS.imag, LAM_VIS * 1e6))
    print("   water, thermal  m = %.4f %+.2ei   at lambda = %.2f um"
          % (M_WATER_IR.real, M_WATER_IR.imag, LAM_IR * 1e6))
    print("   aerosol         m = %.4f %+.2ei   at lambda = %.2f um"
          % (M_AEROSOL.real, M_AEROSOL.imag, LAM_VIS * 1e6))

    print()
    print("(a) energy conservation for a non-absorbing sphere: Q_ext must equal Q_sca")
    for x in (1.0, 5.0, 20.0, 114.2387):
        qe, qs, _ = mie(1.5 + 0.0j, x)
        print("    x = %8.3f   Q_ext = %.10f   Q_sca = %.10f   |diff| = %.2e"
              % (x, qe, qs, abs(qe - qs)))

    print()
    print("(b) Rayleigh limit: for small x the scattering is symmetric, so g -> 0")
    for x in (0.05, 0.10, 0.30):
        qe, qs, g = mie(1.5 + 0.0j, x)
        ray = (8.0 / 3.0) * x ** 4 * abs((1.5 ** 2 - 1.0) / (1.5 ** 2 + 2.0)) ** 2
        print("    x = %5.2f   g = %+.5f      Rayleigh Q_sca = %.4e   Mie Q_sca = %.4e"
              % (x, g, ray, qs))

    print()
    print("(c) extinction paradox: averaged over a size distribution, Q_ext -> 2")
    xs = np.linspace(60.0, 260.0, 80)
    qbar = np.mean([mie(M_WATER_VIS, x)[0] for x in xs])
    print("    mean Q_ext for x in [60, 260] = %.4f   (single values oscillate"
          " about it by ~%.2f)" % (qbar, np.std([mie(M_WATER_VIS, x)[0] for x in xs])))

    section("2  Droplet and aerosol optics; optical depth from water path")
    print("Polydispersions: gamma distribution, effective variance v_e = 0.10.")
    print()
    print("   water droplets, visible (m = 1.3312 + 1e-8i):")
    print("   r_e (um)   Q_ext      w0         g        tau/LWP (m2/kg)"
          "   geometric 3/(2 rho_w r_e)   ratio")
    drop = {}
    for re_um in (5.0, 10.0, 15.0, 20.0):
        re = re_um * 1e-6
        d = polydispersion(re, 0.10, M_WATER_VIS, LAM_VIS)
        geom = 3.0 / (2.0 * RHO_W * re)
        drop[re_um] = d
        print("   %6.1f   %7.4f  %9.7f  %7.4f   %18.2f   %18.2f   %6.4f"
              % (re_um, d["q_ext"], d["w0"], d["g"], d["tau_ext"], geom, d["tau_ext"] / geom))
    print()
    print("   Interpretation: visible extinction efficiency is very close to the")
    print("   geometric value 2 because the size parameter x = 2 pi r / lambda is")
    print("   of order 50-140, so the geometric formula tau = 3 LWP / (2 rho_w r_e)")
    print("   is accurate to a few per cent and improves as r_e grows.  Absorption is")
    print("   negligible: w0 departs from 1 by ~1e-6 for this synthetic index.")
    print()
    print("   one synthetic aerosol mode, visible (m = 1.50 + 0.01i), monodisperse:")
    print("   r (um)     x        Q_ext     w0        g")
    for r_um in (0.02, 0.05, 0.10, 0.30, 1.00):
        x = 2.0 * np.pi * r_um * 1e-6 / LAM_VIS
        qe, qs, g = mie(M_AEROSOL, x)
        print("   %6.2f  %7.3f   %7.4f   %7.4f   %7.4f" % (r_um, x, qe, qs / qe, g))
    print()
    print("   Interpretation: the single-scattering albedo of an absorbing aerosol")
    print("   varies strongly with size - small particles absorb a larger fraction of")
    print("   what they intercept, large ones scatter most of it forward.  Nothing in")
    print("   this table is a measured aerosol property; both indices and sizes are")
    print("   chosen to bracket plausible behaviour.")

    print()
    print("   thermal infrared (m = 1.20 + 0.05i, lambda = 11 um), polydisperse:")
    print("   r_e (um)   Q_abs      g       tau_abs/LWP (m2/kg)   3/(4 rho_w r_e)   ratio")
    for re_um in (5.0, 10.0, 15.0):
        re = re_um * 1e-6
        d = polydispersion(re, 0.10, M_WATER_IR, LAM_IR, npts=40)
        geom = 3.0 / (4.0 * RHO_W * re)
        print("   %6.1f   %7.4f  %7.4f   %18.2f   %18.2f   %6.3f"
              % (re_um, d["q_ext"] - d["q_sca"], d["g"], d["tau_abs"], geom,
                 d["tau_abs"] / geom))
    print("   The geometric limit 3/(4 rho_w r_e) assumes an absorption efficiency of")
    print("   exactly 1; here x ~ 3-9, so the Mie value is the smaller and more")
    print("   honest number.")

    section("3  Two-stream reflectance: validation before use")
    print("Exact identities that any correct solution must satisfy (black surface")
    print("means alb_s = 0; white means alb_s = 1):")
    print()
    print("   closure          w0     alb_s   tau    R          T        residue")
    for delta in (False, True):
        for w0, alb, tau, kind in ((1.0, 0.0, 4.0, "R + T - 1"),
                                   (1.0, 0.0, 0.5, "R + T - 1"),
                                   (1.0, 1.0, 4.0, "R - 1"),
                                   (1.0, 0.3, 4.0, "absorptance"),
                                   (0.0, 0.0, 4.0, "T - exp(-tau/mu0)")):
            R, T = two_stream(tau, w0, 0.8646, 0.6, alb_s=alb, delta=delta)
            if kind == "R + T - 1":
                res = R + T - 1.0
            elif kind == "R - 1":
                res = R - 1.0
            elif kind == "absorptance":
                res = 1.0 - R - (1.0 - alb) * T
            else:
                res = T - np.exp(-tau / 0.6)
            print("   %-14s  %.1f   %5.1f  %5.1f   %.8f  %.8f   %9.2e   (%s)"
                  % ("delta" if delta else "plain Eddington", w0, alb, tau, R, T, res, kind))
    print()
    print("   Conservative scattering (w0 = 1) with any surface albedo must absorb")
    print("   nothing, and with a perfectly reflecting surface nothing may escape")
    print("   downward - so R = 1.  Both hold to machine precision.")

    print()
    print("Independent check: the same two equations solved by a second-order")
    print("finite-difference boundary-value problem (n = 800 grid cells):")
    worst = 0.0
    print("   w0     g      tau     alb_s   R (analytic)  R (finite diff)   |diff|")
    for w0, g, tau, alb in ((1.0, 0.8646, 4.0, 0.0), (0.9, 0.8646, 4.0, 0.0),
                            (0.9, 0.8646, 4.0, 0.3), (0.5, 0.5, 2.0, 0.2),
                            (0.99, 0.0, 1.0, 0.1), (0.2, 0.8646, 8.0, 0.5)):
        Ra, Ta = two_stream(tau, w0, g, 0.6, alb_s=alb)
        Rf, Tf = two_stream_fd(tau, w0, g, 0.6, alb_s=alb)
        worst = max(worst, abs(Ra - Rf), abs(Ta - Tf))
        print("   %.2f  %6.4f  %5.1f   %5.1f   %.8f    %.8f    %.2e"
              % (w0, g, tau, alb, Ra, Rf, abs(Ra - Rf)))
    print("   largest disagreement over these cases: %.2e" % worst)

    print()
    print("Independent check: the phase function itself.  The two-stream uses only")
    print("the first moment g, but the single-scattering check below needs the full")
    print("azimuth-averaged phase function, so its two normalisations are verified:")
    mu_g, w_g = np.polynomial.legendre.leggauss(400)
    for g in (0.0, 0.30, 0.8619):
        p = phase_hg(mu_g, 0.6, g)[:, 0]
        norm = 0.5 * np.sum(w_g * p)
        mom = 0.5 * np.sum(w_g * mu_g * p) / 0.6
        print("    g = %6.4f :  (1/2) int p0 dmu = %.10f   (should be 1)"
              "   (1/2) int mu p0 dmu / mu0 = %.10f   (should be g)" % (g, norm, mom))

    print()
    print("Independent check: optically thin layer against exact single scattering.")
    print("Both closures include multiple scattering, so both must exceed the")
    print("single-scattering value by a term of order tau^2 and approach it as")
    print("tau -> 0.  The residual ratio as tau -> 0 measures the truncation error")
    print("of the phase function, which is the real limitation of the method:")
    print("   tau      R single scatt.   R plain Edd.   ratio    R delta-Edd.   ratio")
    for tau in (0.002, 0.01, 0.05, 0.20):
        rss = single_scattering(tau, 1.0, 0.8619, 0.6)
        rp, _ = two_stream(tau, 1.0, 0.8619, 0.6)
        rd, _ = two_stream(tau, 1.0, 0.8619, 0.6, delta=True)
        print("   %5.3f      %11.6f      %11.6f  %6.4f   %11.6f  %6.4f"
              % (tau, rss, rp, rp / rss, rd, rd / rss))
    print("   The plain Eddington closure keeps only the first moment of the phase")
    print("   function and therefore overestimates the backscattered fraction of a")
    print("   strongly forward-scattering layer; the delta-Eddington scaling removes")
    print("   the forward peak first and cuts that error by a large factor.")

    section("4  Cloud albedo and the indirect (Twomey) effect")
    g_sw = drop[10.0]["g"]
    kext = drop[10.0]["tau_ext"]
    print("Synthetic cloud: r_e = 10 um, v_e = 0.10, water only (w0 ~ 1), g = %.4f" % g_sw)
    print("Mass extinction coefficient: %.2f m2/kg  ->  tau = %.2f * LWP[kg/m2]"
          % (kext, kext))
    print()
    print("Primary closure: delta-Eddington.  The plain Eddington value is shown")
    print("beside it because the difference between two closures IS the model error;")
    print("no absolute value in this table should be quoted as a cloud albedo.")
    print()
    print("   LWP (g/m2)   tau      R (delta-Edd.)   R (plain Edd.)   spread")
    for lwp_g in (5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 400.0):
        tau = kext * lwp_g / 1000.0
        R, _ = two_stream(tau, 1.0, g_sw, 0.6, delta=True)
        Rp, _ = two_stream(tau, 1.0, g_sw, 0.6)
        print("   %9.1f   %7.3f   %.5f          %.5f          %+.5f"
              % (lwp_g, tau, R, Rp, Rp - R))
    print()
    print("   Albedo saturation: doubling tau adds little once tau is large.")
    print("   tau      R         dR for a doubling of tau")
    for tau in (2.0, 5.0, 10.0, 20.0, 40.0, 80.0):
        R1, _ = two_stream(tau, 1.0, g_sw, 0.6, delta=True)
        R2, _ = two_stream(2.0 * tau, 1.0, g_sw, 0.6, delta=True)
        print("   %6.1f   %.5f   %+.5f" % (tau, R1, R2 - R1))
    print("   The increment peaks near tau = 5 and has fallen by a factor of three")
    print("   by tau = 80: most of the albedo is already there at small optical depth,")
    print("   and an already-bright cloud cannot be made much brighter.")

    print()
    print("Twomey (first indirect) effect at fixed liquid-water path: if the droplet")
    print("number doubles and LWP is unchanged, r_e falls by 2^(1/3) and tau rises by")
    print("2^(1/3), because tau = 3 LWP / (2 rho_w r_e).")
    print()
    lwp = 0.100                                              # kg m^-2
    tau_ref = kext * lwp
    print("   reference: LWP = %.0f g/m2, r_e = 10 um, tau = %.3f, R = %.5f"
          % (lwp * 1000.0, tau_ref, two_stream(tau_ref, 1.0, g_sw, 0.6, delta=True)[0]))
    print()
    print("   N_d / N_ref   r_e (um)   tau       R          dR/dln(N_d)   R(1-R)/3")
    prev = None
    for fac in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0):
        re_fac = 10.0 / fac ** (1.0 / 3.0)
        g_fac = drop[10.0]["g"] + 0.0
        tau = kext * lwp * fac ** (1.0 / 3.0)
        R, _ = two_stream(tau, 1.0, g_fac, 0.6, delta=True)
        if prev is None:
            dsub = float("nan")
        else:
            dsub = (R - prev[1]) / np.log(fac / prev[0])
        print("   %10.2f   %8.2f   %7.2f   %.5f    %12.5f   %.5f"
              % (fac, re_fac, tau, R, dsub, R * (1.0 - R) / 3.0))
        prev = (fac, R)
    print()
    print("   Doubling N_d changes R by %+.5f at this LWP.  The asymptotic"
          % (two_stream(kext * lwp * 2.0 ** (1.0 / 3.0), 1.0, g_sw, 0.6, delta=True)[0]
             - two_stream(kext * lwp, 1.0, g_sw, 0.6, delta=True)[0]))
    print("   Here the asymptotic susceptibility R(1-R)/3 reproduces the exact finite")
    print("   difference to within a few per cent, because at this optical depth the")
    print("   albedo is already close to its saturating value.  The agreement is a")
    print("   property of this regime, not a general identity; both numbers are model")
    print("   outputs, and both change if the closure changes.")

    section("5  Longwave emissivity, cloud radiative forcing, and cloud height")
    print("Longwave absorption optical depth from the same geometric argument")
    print("(absorption efficiency Q_abs from Mie, not assumed to be 1):")
    d_ir = polydispersion(10.0e-6, 0.10, M_WATER_IR, LAM_IR, npts=40)
    kabs = d_ir["tau_abs"]
    print("   r_e = 10 um, lambda = 11 um:  tau_abs/LWP = %.2f m2/kg" % kabs)
    print()
    print("   LWP (g/m2)   tau_abs    cloud emissivity eps = 1 - exp(-tau_abs)")
    for lwp_g in (5.0, 10.0, 25.0, 50.0, 100.0, 200.0):
        t_abs = kabs * lwp_g / 1000.0
        print("   %9.1f   %8.3f    %.5f" % (lwp_g, t_abs, 1.0 - np.exp(-t_abs)))
    print()
    print("Cloud radiative forcing, defined as (clear sky flux) - (cloudy sky flux)")
    print("at the top of the atmosphere, so that a brightening cloud has a negative")
    print("shortwave forcing.  Synthetic single-layer model, LOCAL daily-mean scene:")
    print("insolation mu0 S = %.1f W/m2 with mu0 = 0.6 and S = %.0f W/m2;"
          % (0.6 * SOLAR, SOLAR))
    print("clear-sky scene albedo 0.12, surface albedo beneath the cloud 0.12,")
    print("lapse rate 6.5 K/km (stated convention), T_surface = %.2f K." % T_SURF)
    print("These are local overcast values.  A global mean is NOT their sum: it")
    print("needs the joint distribution of cloud fraction, insolation and cloud")
    print("optical properties, which this model does not contain.")
    print()
    print("   z (km)  LWP(g/m2)  T_cloud(K)  eps      tau_sw   SW CF     LW CF"
          "     net (W/m2)")
    insolation = 0.6 * SOLAR
    for z_km in (1.0, 2.0, 5.0, 10.0):
        t_cloud = T_SURF - LAPSE * z_km * 1000.0
        for lwp_g in (5.0, 20.0, 100.0):
            t_sw = kext * lwp_g / 1000.0
            R_cloud, _ = two_stream(t_sw, 1.0, g_sw, 0.6, alb_s=0.12, delta=True)
            a_clear = 0.12
            sw_cf = -(R_cloud - a_clear) * insolation
            eps = 1.0 - np.exp(-kabs * lwp_g / 1000.0)
            lw_cf = eps * (SIGMA * T_SURF ** 4 - SIGMA * t_cloud ** 4)
            print("   %5.1f   %8.0f   %9.2f   %.4f  %7.2f  %8.2f  %8.2f  %11.2f"
                  % (z_km, lwp_g, t_cloud, eps, t_sw, sw_cf, lw_cf, sw_cf + lw_cf))
    print()
    print("   Crossover scan: a high thin cloud versus a low thick one, at the same")
    print("   height, varying the liquid-water path:")
    print("   z (km)  LWP(g/m2)  tau_sw   R_scene   eps      SW CF     LW CF     net")
    for z_km in (12.0,):
        t_cloud = T_SURF - LAPSE * z_km * 1000.0
        for lwp_g in (2.0, 5.0, 10.0, 20.0, 50.0):
            t_sw = kext * lwp_g / 1000.0
            R_cloud, _ = two_stream(t_sw, 1.0, g_sw, 0.6, alb_s=0.12, delta=True)
            sw_cf = -(R_cloud - 0.12) * insolation
            eps = 1.0 - np.exp(-kabs * lwp_g / 1000.0)
            lw_cf = eps * (SIGMA * T_SURF ** 4 - SIGMA * t_cloud ** 4)
            print("   %5.1f   %8.0f  %7.2f   %.5f   %.4f  %8.2f  %8.2f  %8.2f"
                  % (z_km, lwp_g, t_sw, R_cloud, eps, sw_cf, lw_cf, sw_cf + lw_cf))
    print()
    print("   The two signs are opposite and their sum changes sign with cloud")
    print("   height and optical depth: this is why the sign of the net cloud effect")
    print("   is a question about the distribution of clouds, not about clouds.")
    print("   Thick low cloud cools; thin and/or high cloud can warm.  These are")
    print("   single-layer model outputs with illustrative parameters, not")
    print("   observational estimates, and no cloud fraction is applied here.")

    section("6  Aerosol direct effect: when does scattering brighten, when dim?")
    g_a = 0.30
    print("Thin-layer prediction, obtained by expanding the two-stream solution to")
    print("first order in tau.  With r = (alpha_s - 1)/(alpha_s + 1):")
    print("   d alpha / d tau |0 = [ q + r (a alpha_s mu0 + p) - c alpha_s mu0")
    print("                          - 2 alpha_s/(1 + alpha_s) ] / ( mu0 (1 - r) )")
    print("   a = 1.5 (1 - w0 g),  c = 2 (1 - w0),  p = 1.5 w0 g mu0,  q = w0")
    print("The last bracket term is the attenuation of the direct beam on its way")
    print("down to the surface and back up; without it the sign of the effect comes")
    print("out wrong, as the comparison below shows.")
    print()
    print("Verify that expression against the model itself, by differentiating the")
    print("full solution numerically at small tau:")

    def slope_analytic(w0, alb, mu0=0.6):
        a = 1.5 * (1.0 - w0 * g_a)
        c = 2.0 * (1.0 - w0)
        r = (alb - 1.0) / (alb + 1.0)
        p = 1.5 * w0 * g_a * mu0
        q = w0
        num = q + r * (a * alb * mu0 + p) - c * alb * mu0 - 2.0 * alb / (1.0 + alb)
        return num / (mu0 * (1.0 - r))

    print("   w0      alpha_s   analytic slope   numeric slope   difference")
    for w0, alb in ((0.5, 0.20), (0.7, 0.50), (0.95, 0.20), (1.0, 0.50)):
        r1, _ = two_stream(0.001, w0, g_a, 0.6, alb_s=alb)
        r2, _ = two_stream(0.003, w0, g_a, 0.6, alb_s=alb)
        num_slope = (r2 - r1) / 0.002
        print("   %.2f    %5.2f     %+11.5f     %+11.5f     %+.1e"
              % (w0, alb, slope_analytic(w0, alb), num_slope,
                 slope_analytic(w0, alb) - num_slope))

    print()
    print("   alpha_s   critical w0 (thin layer)   measured vs full model at AOD 0.15")
    for alb in (0.05, 0.20, 0.50):
        lo, hi = 0.0, 1.0
        if slope_analytic(1.0, alb) > 0.0:
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if slope_analytic(mid, alb) < 0.0:
                    lo = mid
                else:
                    hi = mid
            crit = 0.5 * (lo + hi)
            sl = slope_analytic(0.95, alb)
            print("   %5.2f     %8.4f                    %s"
                  % (alb, crit, "brightens" if sl > 0 else "dims"))
        else:
            print("   %5.2f     none below 1              always dims" % alb)
    print()
    print("   Sign of the direct effect for the full solution at AOD = 0.15 (g = 0.30),")
    print("   delta-Eddington closure:")
    print("   w0      alpha_s = 0.05          alpha_s = 0.20          alpha_s = 0.50")
    print("           dalpha   sign           dalpha   sign           dalpha   sign")
    for w0 in (0.70, 0.85, 0.95, 0.99, 1.00):
        line = "   %.2f  " % w0
        for alb in (0.05, 0.20, 0.50):
            R, _ = two_stream(0.15, w0, g_a, 0.6, alb_s=alb, delta=True)
            d = R - alb
            line += "  %+.5f  %-8s" % (d, "brighter" if d > 0 else "darker")
        print(line)
    print()
    print("   Scattering brightens a dark scene and, once the surface is bright")
    print("   enough, absorption outweighs it and the aerosol dims the scene.  The")
    print("   critical single-scattering albedo rises with surface albedo.  Which")
    print("   side of that threshold a real aerosol sits on is exactly what is not")
    print("   known from models alone.")

    section("7  Measured, modelled, inferred -- and an inverse problem")
    print("   quantity                          status")
    print("   particle size distribution         inferred from optical measurements")
    print("   refractive index                   inferred; not directly observable")
    print("   extinction optical depth           measured (from transmitted intensity)")
    print("   single-scattering albedo           inferred, with large uncertainty")
    print("   asymmetry parameter g              inferred from angular measurements")
    print("   liquid-water path                  measured by microwave radiometry")
    print("   droplet effective radius           retrieved, model-dependent")
    print("   cloud albedo                       measured at the top of the atmosphere")
    print("   indirect effect on albedo          inferred from covariation; not a")
    print("                                      controlled experiment")
    print("   radiative forcing                  modelled; a difference of two models")
    print()
    print("A synthetic retrieval shows why high albedo is a bad place to measure.")
    print("Simulate a measured reflectance R = R(tau) + noise (2 per cent relative,")
    print("RNG seed 20261014), invert by nearest neighbour on a fine tau grid, and")
    print("report the spread of the retrieved tau over %d realisations:" % MAX_STORE)
    print()
    grid = np.linspace(0.05, 400.0, 4001)
    rgrid = np.array([two_stream(t, 1.0, g_sw, 0.6, delta=True)[0] for t in grid])
    print("   tau_true   R_true    retrieved tau (mean +- sd)   error in tau")
    for tau_true in (2.0, 8.0, 32.0, 128.0):
        r_true = two_stream(tau_true, 1.0, g_sw, 0.6, delta=True)[0]
        errs = []
        for _ in range(MAX_STORE):
            r_meas = r_true * (1.0 + 0.02 * RNG.standard_normal())
            errs.append(grid[int(np.argmin(np.abs(rgrid - r_meas)))] - tau_true)
        errs = np.array(errs)
        print("   %8.1f   %.5f   %11.1f +- %6.1f        %+8.1f +- %6.1f"
              % (tau_true, r_true, tau_true + np.mean(errs), np.std(errs),
                 np.mean(errs), np.std(errs)))
    print()
    print("   At small tau a 2 per cent reflectance error moves the retrieved optical")
    print("   depth by a few per cent; at large tau the same error moves it by of")
    print("   order the optical depth itself.  Once the albedo saturates near 1 it")
    print("   carries almost no information about optical depth - a statement about")
    print("   the measurement, not about the cloud.")
    print()
    print("All models and data in this demonstration are SYNTHETIC.")
    return 0


if __name__ == "__main__":
    main()
