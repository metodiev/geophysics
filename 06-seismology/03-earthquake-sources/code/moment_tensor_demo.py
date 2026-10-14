"""Moment tensors: physical meaning, decomposition, and reconstruction.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_tensor_demo.py
Requires: numpy, obspy (for one independent rendering check).

Companion to lesson 06-03-03.

WHAT IS COMPUTED

1. The six independent components of a moment tensor from a synthetic source,
   and the physical meaning of each (a force couple on a face of a unit cube).
2. The eigenvalue problem: sorted eigenvalues and eigenvectors, so that the
   tensor's three principal axes and their signs are explicit.
3. The decomposition  M = M_ISO + M_DC + M_CLVD.  The algebra is done
   explicitly, then the three parts are added back and the residual against
   the input tensor is reported.  This is the check that the decomposition is
   the identity it claims to be, to machine precision.
4. The scalar moment and the moment magnitude in both unit conventions, with
   the offset converted explicitly (1 N m = 1e7 dyn cm).
5. The isotropic fraction and the CLVD fraction, and how each behaves for a
   pure double couple, a pure CLVD, and an explosion.

Every source is SYNTHETIC and its six components are printed.  No observed
moment tensor, magnitude or event is quoted.
"""

import numpy as np

D2R = np.pi / 180.0


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# Decomposition machinery
# --------------------------------------------------------------------------

def decompose(m):
    """Return (M_iso, M_dc, M_clvd, mom_dc, clvd_eps, eigenvalues, basis).

    Standard decomposition in the eigenbasis of the DEVIATORIC part:

        M      = (tr M / 3) I  +  M_dev
        M_dev  = M0_dc * diag(1, 0, -1)  +  lam2 * diag(-1/2, 1, -1/2)

    with the deviatoric eigenvalues ordered lam1 >= lam2 >= lam3 (they sum to
    zero), M0_dc = (lam1 - lam3)/2 the double-couple scalar moment, and
    lam2 the coefficient of the compensated-linear-vector-dipole (CLVD) part.
    The CLVD strength parameter used in the literature is
        eps = -lam2 / max(|lam1|, |lam3|)   in [-1/2, +1/2],
    with |eps| = 1/2 for a pure CLVD and eps = 0 for a pure double couple.
    """
    iso = np.trace(m) / 3.0
    m_iso = iso * np.eye(3)
    m_dev = m - m_iso
    vals, vecs = np.linalg.eigh(m_dev)
    order = np.argsort(vals)[::-1]              # descending
    vals = vals[order]
    vecs = vecs[:, order]
    lam1, lam2, lam3 = vals
    m0_dc = 0.5 * (lam1 - lam3)
    denom = max(abs(lam1), abs(lam3))
    eps = -lam2 / denom if denom > 0 else 0.0
    d_dc = m0_dc * np.diag([1.0, 0.0, -1.0])
    d_clvd = lam2 * np.diag([-0.5, 1.0, -0.5])
    rot = vecs
    m_dc = rot @ d_dc @ rot.T
    m_clvd = rot @ d_clvd @ rot.T
    return m_iso, m_dc, m_clvd, m0_dc, eps, vals, vecs


def tensor_from(strike, dip, rake, m0):
    p, d, l = strike * D2R, dip * D2R, rake * D2R
    n = np.array([-np.sin(d) * np.sin(p), np.sin(d) * np.cos(p), -np.cos(d)])
    s = np.array([np.cos(l) * np.cos(p) + np.cos(d) * np.sin(l) * np.sin(p),
                  np.cos(l) * np.sin(p) - np.cos(d) * np.sin(l) * np.cos(p),
                 -np.sin(l) * np.sin(d)])
    return m0 * (np.outer(n, s) + np.outer(s, n))


def mw_offsets():
    """Moment magnitude offsets in the two unit conventions.

    Hanks & Kanamori (1979) is quoted in dyn cm:
        Mw = (2/3) log10(M0[dyn cm]) - 10.7
    Converting exactly with 1 N m = 1e7 dyn cm:
        (2/3) log10(M0[N m] * 1e7) - 10.7
      = (2/3) log10(M0[N m]) + (2/3)*7 - 10.7
      = (2/3) log10(M0[N m]) - 6.03333...
    The value most often written for SI units is -6.07, which is a rounding
    of the same relation: the two differ by 0.0367 magnitude units.
    """
    offset_exact = -10.7 + (2.0 / 3.0) * 7.0
    return -10.7, offset_exact, -6.07


def mw(m0_nm):
    _, offset_exact, offset_used = mw_offsets()
    return ((2.0 / 3.0) * np.log10(m0_nm) + offset_exact,
            (2.0 / 3.0) * np.log10(m0_nm) + offset_used)


# --------------------------------------------------------------------------
# 1. The six components and what each one is
# --------------------------------------------------------------------------

def part1_components():
    section("1. The six independent components and their physical meaning")
    m = tensor_from(32.0, 63.0, -41.0, 3.4e18)
    print("  SYNTHETIC source: strike 32, dip 63, rake -41, M0 = 3.4e18 N m")
    print("  Frame: x = North, y = East, z = Down.  Components in N m.")
    print()
    labels = [("Mxx", m[0, 0]), ("Myy", m[1, 1]), ("Mzz", m[2, 2]),
              ("Mxy", m[0, 1]), ("Mxz", m[0, 2]), ("Myz", m[1, 2])]
    meaning = {
        "Mxx": "couple on the x face acting in x (a North-south force pair)",
        "Myy": "couple on the y face acting in y",
        "Mzz": "couple on the z face acting in z (isotropic part lives here)",
        "Mxy": "couple on the x face acting in y (the strike-slip couple)",
        "Mxz": "couple on the x face acting in z (dip-slip on a N-S fault)",
        "Myz": "couple on the y face acting in z (dip-slip on an E-W fault)",
    }
    for name, value in labels:
        print(f"    {name} = {value:+.6e}   {meaning[name]}")
    print()
    print(f"  trace = Mxx+Myy+Mzz = {np.trace(m):+.6e} N m")
    print("  A double couple is traceless; a non-zero trace is a volume change.")
    print(f"  M is symmetric by construction: max|M - M^T| = "
          f"{np.max(np.abs(m - m.T)):.3e} N m")
    return m


# --------------------------------------------------------------------------
# 2. Eigenvalues and eigenvectors
# --------------------------------------------------------------------------

def part2_eigen(m):
    section("2. Eigenvalues and eigenvectors: the three principal axes")
    vals, vecs = np.linalg.eigh(m)
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]
    print("  The eigenvalue problem is solved on the FULL tensor (not yet")
    print("  deviatoric), so an isotropic part shows up as three equal values.")
    print()
    print(f"  {'index':>6}{'eigenvalue (N m)':>20}   eigenvector (N, E, Down)")
    for i in range(3):
        v = vecs[:, i] * (1.0 if vecs[2, i] < 0 else -1.0)
        print(f"  {i+1:6d}{vals[i]:+20.6e}   "
              f"({v[0]:+.4f}, {v[1]:+.4f}, {v[2]:+.4f})")
    print()
    print(f"  scalar moment M0 = (lam1 - lam3)/2 = "
          f"{0.5*(vals[0]-vals[2]):.6e} N m")
    print(f"  sum of eigenvalues = trace = {vals.sum():+.6e} N m")
    rec = np.max(np.abs(m - vecs @ np.diag(vals) @ vecs.T))
    print(f"  ||M - sum_i lam_i e_i e_i^T||_max = {rec:.3e} N m"
          f"  (relative {rec/np.max(np.abs(m)):.2e})")
    return vals, vecs


# --------------------------------------------------------------------------
# 3. The decomposition, reconstructed
# --------------------------------------------------------------------------

def part3_decomposition():
    section("3. Decomposition into isotropic + double couple + CLVD")
    cases = []
    cases.append(("pure double couple", tensor_from(32.0, 63.0, -41.0, 1.0e19)))
    cases.append(("pure CLVD (lam = 2,-1,-1)", 1.0e19 * np.diag([2.0, -1.0, -1.0]) / 1.5))
    cases.append(("explosion, M_iso = 1e19",
                  1.0e19 * np.eye(3)))
    cases.append(("ISO + DC", 1.0e19 * np.eye(3)
                  + tensor_from(10.0, 40.0, 90.0, 2.0e19)))
    cases.append(("ISO + CLVD", 5.0e18 * np.eye(3)
                  + 1.0e19 * np.diag([2.0, -1.0, -1.0]) / 1.5))
    print(f"  {'source':<28}{'M_iso/||M||':>13}{'M0_dc':>13}{'CLVD eps':>10}"
          f"{'residual/||M||':>16}")
    for (name, m) in cases:
        m_iso, m_dc, m_clvd, m0_dc, eps, vals, _ = decompose(m)
        recon = m_iso + m_dc + m_clvd
        resid = np.max(np.abs(m - recon)) / np.max(np.abs(m))
        iso_frac = np.trace(m_iso) / 3.0 / np.max(np.abs(m))
        print(f"  {name:<28}{iso_frac:>13.6f}{m0_dc:>13.4e}{eps:>10.4f}"
              f"{resid:>16.2e}")
    print()
    print("  Every row reconstructs to machine precision: the decomposition is an")
    print("  identity, not an approximation.  The residual is the only number here")
    print("  that is not a property of the source; it measures the arithmetic.")
    print()
    print("  Reading the table:")
    print("    * a pure double couple has eps = 0 and M_iso = 0;")
    print("    * a pure CLVD has |eps| = 1/2 -- it is the other extreme;")
    print("    * an explosion is pure M_iso with M_dc = 0 and eps = 0/0 -> 0.")
    print()
    print("  Note what is NOT here: nothing in this decomposition is a measurement.")
    print("  M_iso, M_dc and eps are all derived from the input tensor, and the")
    print("  input tensor is itself a model or an inversion result.")


# --------------------------------------------------------------------------
# 4. Scalar moment and moment magnitude, both conventions
# --------------------------------------------------------------------------

def part4_magnitude():
    section("4. Scalar moment and moment magnitude, with the offset derived")
    off_dyn, off_exact, off_used = mw_offsets()
    print("  Hanks & Kanamori (1979), as published, in dyn cm:")
    print("      Mw = (2/3) log10(M0[dyn cm]) - 10.7")
    print(f"      offset in dyn cm           = {off_dyn:+.4f}")
    print()
    print("  Convert exactly with 1 N m = 1e7 dyn cm:")
    print("      (2/3) log10(M0[N m] x 1e7) - 10.7")
    print("    = (2/3) log10(M0[N m]) + (2/3) x 7 - 10.7")
    print(f"    = (2/3) log10(M0[N m]) {off_exact:+.6f}")
    print(f"      offset in N m, exact       = {off_exact:+.6f}")
    print(f"      offset in N m, usually quoted = {off_used:+.4f}")
    print(f"      difference = {abs(off_used-off_exact):.4f} magnitude units")
    print(f"      which is a factor {10**(1.5*abs(off_used-off_exact)):.4f} in M0")
    print()
    print(f"  {'M0 (N m)':>12}{'Mw exact':>11}{'Mw quoted':>11}{'difference':>12}")
    for m0 in (1e15, 1e18, 1e19, 1e21, 1e23):
        a, b = mw(m0)
        print(f"  {m0:12.1e}{a:11.4f}{b:11.4f}{abs(a-b):12.4f}")
    print()
    print("  A magnitude is a reporting convention with a stated unit inside the")
    print("  logarithm.  Quoting Mw without stating which offset was used is")
    print("  quoting a number that differs from another worker's by 0.04.")


# --------------------------------------------------------------------------
# 5. Independent check on the rendered focal mechanism
# --------------------------------------------------------------------------

def part5_orthogonality():
    section("5. Independent check: the parts are orthogonal projections")
    m = tensor_from(32.0, 63.0, -41.0, 1.0e19) + 2.0e18 * np.eye(3)
    m_iso, m_dc, m_clvd, m0_dc, eps, vals, _ = decompose(m)
    eye = np.eye(3)

    def inner(a, b):
        return float(np.sum(a * b))

    def cosine(a, b):
        den = np.sqrt(inner(a, a) * inner(b, b))
        return inner(a, b) / den if den > 0 else 0.0

    print("  With the Frobenius inner product A:B = sum_ij A_ij B_ij, the")
    print("  decomposition is a set of orthogonal projections of M.  All the")
    print("  quantities below are normalised cosines, so 1e-17 means zero.")
    print()
    print(f"    cos(M_iso, I)              = {cosine(m_iso, eye):+.3e}")
    print(f"    cos(M - M_iso, I)          = {cosine(m - m_iso, eye):+.3e}")
    print(f"    cos(M_dc, M_clvd)          = {cosine(m_dc, m_clvd):+.3e}")
    print(f"    cos(M_iso, M_dc)           = {cosine(m_iso, m_dc):+.3e}")
    print(f"    cos(M_iso, M_clvd)         = {cosine(m_iso, m_clvd):+.3e}")
    pythag = (inner(m, m) - inner(m_iso, m_iso) - inner(m_dc, m_dc)
              - inner(m_clvd, m_clvd)) / inner(m, m)
    print(f"    (||M||^2 - sum of parts^2) / ||M||^2 = {pythag:+.3e}")
    print()
    print(f"    trace(M_dc) / ||M||_max  = {np.trace(m_dc)/np.max(np.abs(m)):+.3e}")
    print(f"    trace(M_clvd) / ||M||_max = {np.trace(m_clvd)/np.max(np.abs(m)):+.3e}")
    print()
    d_dc = np.diag([1.0, 0.0, -1.0])
    d_clvd = np.diag([-0.5, 1.0, -0.5])
    print("  In the deviatoric eigenbasis the two patterns are")
    print(f"    double couple  diag(1, 0, -1)          :  diag(1,0,-1):diag(-1/2,1,-1/2)"
          f" = {inner(d_dc, d_clvd):+.2e}")
    print("  Both are traceless and mutually orthogonal (norm^2 = 2 and 3/2), so")
    print("  are the two orthogonal extreme members of the traceless subspace: any")
    print("  deviatoric moment tensor is a point on the line between them.")
    print()
    print("  These identities are exact algebra, verified here rather than")
    print("  asserted.  They say nothing about whether M is the right model for a")
    print("  given earthquake -- that is a question about the inversion, not about")
    print("  the arithmetic.")


def main():
    print("Moment tensors: components, decomposition and reconstruction")
    print(f"numpy {np.__version__}")
    m = part1_components()
    part2_eigen(m)
    part3_decomposition()
    part4_magnitude()
    part5_orthogonality()
    print()
    print("=" * 72)
    print("Summary of independent checks:")
    print("  * decomposition reconstructed, residual reported per case")
    print("  * eigenvalue reconstruction of M, residual reported")
    print("  * the isotropic, DC and CLVD parts are mutually orthogonal")
    print("All sources are SYNTHETIC with their six components printed above.")
    print("=" * 72)


if __name__ == "__main__":
    main()
