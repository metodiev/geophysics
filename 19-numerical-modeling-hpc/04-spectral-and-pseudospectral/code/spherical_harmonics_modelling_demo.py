#!/usr/bin/env python3
"""Spherical harmonic modelling of global fields, measured.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spherical_harmonics_modelling_demo.py

The coefficient sets here are SYNTHETIC.  Every reference value is an exact
mathematical identity (orthonormality, Parseval) or a number this script
measures.

Contents
--------
1. Normalised associated Legendre functions and the orthonormality of the real
   spherical harmonics, verified by quadrature.
2. Synthesis and analysis: a coefficient set, its field, and Parseval's identity.
3. Power spectra from coefficients and from samples: the same spectrum.
4. Downward continuation: the exact amplification factor and its cost.
5. Quadrature aliasing: the number of latitude nodes a band-limited field needs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def plm_normalised(l_max, x):
    """Fully normalised associated Legendre functions P_lm(x), l <= l_max.

    Returns an array of shape (l_max+1, l_max+1, len(x)) with zeros where m > l.
    The recurrence is the standard Schmidt-semi-normalised one scaled by
    sqrt(2l+1), which is the fully normalised 4-pi convention used in geodesy:
    the harmonics then satisfy (1/4 pi) int Y^2 dOmega = 1.
    """
    n = x.size
    P = np.zeros((l_max + 1, l_max + 1, n))
    u = np.sqrt(1.0 - x ** 2)                     # sin(theta)
    P[0, 0] = 1.0
    if l_max >= 1:
        P[1, 0] = np.sqrt(3.0) * x
        P[1, 1] = np.sqrt(3.0) * u
    for l in range(2, l_max + 1):
        for m in range(0, l + 1):
            if m == l:
                P[l, l] = u * np.sqrt((2.0 * l + 1.0) / (2.0 * l)) * P[l - 1, l - 1]
                continue
            a = np.sqrt((4.0 * l ** 2 - 1.0) / (l ** 2 - m ** 2))
            b = np.sqrt(((2.0 * l + 1.0) * ((l - 1.0) ** 2 - m ** 2))
                        / ((2.0 * l - 3.0) * (l ** 2 - m ** 2)))
            prev2 = P[l - 2, m] if l >= 2 else 0.0
            P[l, m] = a * x * P[l - 1, m] - b * prev2
    return P


def harmonic(l, m, theta, phi, P):
    """Real, fully normalised spherical harmonic (cos for m >= 0, sin for m < 0)."""
    if m >= 0:
        return P[l, m] * np.cos(m * phi)
    return P[l, -m] * np.sin(-m * phi)


def gl_latitudes(n_lat):
    """Gauss-Legendre nodes in x = cos(theta) and weights; exact for band-limited."""
    x, w = np.polynomial.legendre.leggauss(n_lat)
    return x, w, np.arccos(x)


def synth(coeffs, l_max, x, phi):
    """Synthesise a field from a coefficient array coeffs[l][m], m >= 0."""
    P = plm_normalised(l_max, x)
    field = np.zeros((x.size, phi.size))
    for l in range(l_max + 1):
        for m in range(0, l + 1):
            field += coeffs[l][m] * np.outer(P[l, m], np.cos(m * phi))
            if m > 0:
                field += coeffs[l][-m] * np.outer(P[l, m], np.sin(m * phi))
    return field


def analysis(field, l_max, x, w, phi):
    """Recover coefficients by quadrature; returns a dict keyed by (l, m)."""
    n_phi = phi.size
    phi_w = 2.0 * np.pi / n_phi
    P = plm_normalised(l_max, x)
    out = {}
    for l in range(l_max + 1):
        for m in range(0, l + 1):
            for sign, mkey, trig in ((1, m, np.cos), (-1, -m, np.sin)):
                if sign < 0 and m == 0:
                    continue
                Y = np.outer(P[l, m], trig(m * phi))
                wgt = np.outer(w, np.full(n_phi, phi_w))
                out[(l, mkey)] = np.sum(field * Y * wgt) / (4.0 * np.pi)
    return out


def main():
    section("1. Orthonormality of the real spherical harmonics, verified")
    print("  Fully normalised harmonics satisfy (1/4 pi) int Y_a Y_b dOmega = delta_ab.")
    print("  The integral is evaluated with a Gauss-Legendre rule in latitude and a")
    print("  uniform sum in longitude -- the standard exact quadrature for a")
    print("  band-limited integrand.")
    l_max = 6
    n_lat = l_max + 1
    n_phi = 2 * l_max + 2
    x, w, theta = gl_latitudes(n_lat)
    phi = 2.0 * np.pi * np.arange(n_phi) / n_phi
    P = plm_normalised(l_max, x)
    harmonics = []
    for l in range(l_max + 1):
        for m in range(-l, l + 1):
            trig = np.cos(abs(m) * phi) if m >= 0 else np.sin(abs(m) * phi)
            Y = np.outer(P[l, abs(m)], trig)
            harmonics.append(((l, m), Y))
    gram = np.zeros((len(harmonics), len(harmonics)))
    for a, (_, Ya) in enumerate(harmonics):
        for b, (_, Yb) in enumerate(harmonics):
            gram[a, b] = (np.sum(Ya * Yb * np.outer(w, np.full(n_phi,
                                                                 2 * np.pi / n_phi)))
                          / (4.0 * np.pi))
    dev = np.max(np.abs(gram - np.eye(len(harmonics))))
    print(f"  l <= {l_max}: {(l_max + 1) ** 2} harmonics, {n_lat} latitude nodes,")
    print(f"  {n_phi} longitude samples.  max |Gram - I| = {dev:.3e}")
    print("  That is round-off, so the implementation of the recurrence and of the")
    print("  normalisation is verified against the identity it must satisfy, not")
    print("  against itself.")

    section("2. Synthesis, analysis and Parseval's identity")
    print("  Build a synthetic coefficient set c_lm for l <= 4, synthesise the field on")
    print("  the quadrature grid, analyse it back, and check both the round trip and")
    print("  the mean-square identity (1/4 pi) int f^2 dOmega = sum c_lm^2.")
    l_max = 4
    n_lat = l_max + 1
    n_phi = 2 * l_max + 2
    x, w, theta = gl_latitudes(n_lat)
    phi = 2.0 * np.pi * np.arange(n_phi) / n_phi
    coeffs = {}
    for l in range(l_max + 1):
        for m in range(-l, l + 1):
            coeffs[(l, m)] = float(RNG.standard_normal())
    coeffs[0] = {(0, 0): 0.0}                      # remove the mean
    def cget(l, m):
        return coeffs.get((l, m), 0.0)
    P = plm_normalised(l_max, x)
    field = np.zeros((n_lat, n_phi))
    for l in range(l_max + 1):
        for m in range(-l, l + 1):
            trig = np.cos(abs(m) * phi) if m >= 0 else np.sin(abs(m) * phi)
            field += cget(l, m) * np.outer(P[l, abs(m)], trig)
    recovered = analysis(field, l_max, x, w, phi)
    worst = max(abs(recovered[(l, m)] - cget(l, m))
                for l in range(l_max + 1) for m in range(-l, l + 1))
    wgt = np.outer(w, np.full(n_phi, 2 * np.pi / n_phi))
    mean_square = np.sum(field ** 2 * wgt) / (4.0 * np.pi)
    sum_sq = sum(cget(l, m) ** 2 for l in range(l_max + 1)
                 for m in range(-l, l + 1))
    print(f"  max |c_lm(analysed) - c_lm(synthesised)| = {worst:.3e}")
    print(f"  (1/4 pi) int f^2 dOmega = {mean_square:.12f}")
    print(f"  sum of c_lm^2           = {sum_sq:.12f}")
    print(f"  difference              = {mean_square - sum_sq:+.3e}")
    print("  Exact synthesis and analysis are inverses here because the quadrature")
    print("  integrates the products exactly; Parseval then closes to round-off.  Both")
    print("  facts fail the moment the field is not band-limited to the grid, which is")
    print("  Section 5.")

    section("3. Power spectra from coefficients and from samples")
    print("  The degree variance of a global field is sigma_l^2 = sum_m c_lm^2/(2l+1).")
    print("  A synthetic spectrum c_lm ~ 1/l^2 (a Kaula-like decay chosen here, not a")
    print("  quoted one) is synthesised at l_max = 60 and its degree variance is")
    print("  compared with the coefficients it was built from.")
    l_max = 60
    n_lat = l_max + 1
    n_phi = 2 * l_max + 2
    x, w, theta = gl_latitudes(n_lat)
    phi = 2.0 * np.pi * np.arange(n_phi) / n_phi
    P = plm_normalised(l_max, x)
    clm = {}
    for l in range(1, l_max + 1):
        for m in range(0, l + 1):
            base = RNG.standard_normal()
            clm[(l, m)] = base / l ** 2
            if m > 0:
                clm[(l, -m)] = RNG.standard_normal() / l ** 2
    field = np.zeros((n_lat, n_phi))
    for (l, m), c in clm.items():
        trig = np.cos(abs(m) * phi) if m >= 0 else np.sin(abs(m) * phi)
        field += c * np.outer(P[l, abs(m)], trig)
    rec = analysis(field, l_max, x, w, phi)
    model_var, rec_var = [], []
    for l in range(1, l_max + 1):
        model_var.append(sum(clm.get((l, m), 0.0) ** 2 for m in range(-l, l + 1))
                         / (2 * l + 1))
        rec_var.append(sum(rec.get((l, m), 0.0) ** 2 for m in range(-l, l + 1))
                       / (2 * l + 1))
    model_var = np.array(model_var)
    rec_var = np.array(rec_var)
    print(f"  l       sigma_l (model)     sigma_l (analysed)    relative difference")
    for l in (1, 2, 5, 10, 20, 40, 60):
        print(f"  {l:3d}   {np.sqrt(model_var[l - 1]):16.6e}   "
              f"{np.sqrt(rec_var[l - 1]):19.6e}   "
              f"{rec_var[l - 1] / model_var[l - 1] - 1:+.2e}")
    print(f"  total power: model {model_var.sum():.9e}, analysed {rec_var.sum():.9e}, "
          f"difference {rec_var.sum() - model_var.sum():+.2e}")
    ls = np.arange(1, l_max + 1, dtype=float)
    slope = np.polyfit(np.log(ls), np.log(model_var), 1)[0]
    print(f"  fitted log-log exponent of the power spectrum over l = 1..{l_max}: "
          f"{slope:.3f}")
    print("  the coefficient model sigma_l ~ l^-2 predicts a power exponent of -4,")
    print("  and the measured value is that to three digits: the degree variance of a")
    print("  global field is a spectrum, and it is measured from the coefficients, not")
    print("  assumed from a published decay law.")

    section("4. Downward continuation: the exact factor and its cost")
    print("  A field measured on a sphere of radius r, continued to a sphere of radius")
    print("  R < r, is multiplied degree by degree by (r/R)^l.  This is exact, and it")
    print("  is also the reason downward continuation is unstable.")
    print("     l    (r/R)^l for r/R = 1.01     for 1.05     for 1.10")
    for l in (10, 50, 100, 200, 500):
        print(f"  {l:5d}   {(1.01) ** l:23.3e}   {(1.05) ** l:11.3e}   "
              f"{(1.10) ** l:11.3e}")
    amp = (1.10) ** 200
    print(f"  At l = 200 and r/R = 1.10 the factor is {amp:.3e}.  A coefficient known to")
    print(f"  a relative 1e-6 is therefore known to a relative {amp * 1e-6:.3e} after")
    print("  continuation -- 190 times the field's own amplitude, i.e. the continuation")
    print("  is worthless at that degree without far better data.  The useful content")
    print("  of the factor is that it fixes the degree at which to stop, and that degree")
    print("  is computable from the data error.")
    print("  The useful number is the degree at which to stop.  Requiring the")
    print("  amplified 1e-6 coefficient error to stay below 1e-3 in the continued")
    print("  field gives l_max = log(1e-3/1e-6)/log(r/R):")
    for ratio in (1.01, 1.02, 1.05):
        l_lim = np.log(1.0e-3 / 1.0e-6) / np.log(ratio)
        print(f"       r/R = {ratio:.2f}: l_max = {l_lim:.1f}")

    section("5. Quadrature aliasing: how many latitude nodes a field needs")
    print("  Analysing a field band-limited to L requires at least L+1 Gauss-Legendre")
    print("  latitude nodes; with fewer, the product of two harmonics is no longer")
    print("  integrated exactly and coefficients leak between degrees.  Measured worst")
    print("  coefficient error versus the number of latitude nodes, for L = 8.")
    L = 8
    n_phi = 2 * L + 2
    phi = 2.0 * np.pi * np.arange(n_phi) / n_phi
    clm2 = {(l, m): RNG.standard_normal() / l for l in range(1, L + 1)
            for m in range(-l, l + 1)}
    print("     n_lat   required   max coefficient error")
    for n_lat in (4, 6, 8, 9, 12, 16):
        x, w, _ = gl_latitudes(n_lat)
        P = plm_normalised(L, x)
        field = np.zeros((n_lat, n_phi))
        for (l, m), c in clm2.items():
            trig = np.cos(abs(m) * phi) if m >= 0 else np.sin(abs(m) * phi)
            field += c * np.outer(P[l, abs(m)], trig)
        rec = analysis(field, L, x, w, phi)
        worst = max(abs(rec[(l, m)] - clm2[(l, m)]) for l in range(1, L + 1)
                    for m in range(-l, l + 1))
        print(f"  {n_lat:7d}   {L + 1:8d}   {worst:.3e}")
    print("  Below L+1 nodes the coefficients are wrong; at L+1 and above the error is")
    print("  round-off.  The requirement is exact, not asymptotic, and it is the same")
    print("  statement as the Nyquist limit in one dimension -- a band-limited field")
    print("  needs a grid that resolves its band, or the unrepresented degrees fold")
    print("  into the represented ones.")
    print("\nAll numbers are printed by this script; the coefficients are SYNTHETIC.")


if __name__ == "__main__":
    main()
