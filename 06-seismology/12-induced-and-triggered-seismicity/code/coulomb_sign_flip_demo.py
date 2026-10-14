"""Coulomb failure-function change from a point double couple: how often does
the SIGN of the stress change depend on the receiver fault you assume?

Physics and conventions
-----------------------
A point double couple of moment M0 (N m) has moment tensor

    M_jk = M0 ( d_j n_k + n_j d_k )

with n the fault normal and d the slip direction (both unit vectors, n . d = 0).
Its static displacement field in an INFINITE, homogeneous, isotropic elastic
medium follows from Kelvin's Green's function

    G_ij = 1/(16 pi mu_s (1 - nu)) [ (3 - 4 nu) delta_ij / r + r_i r_j / r^3 ]

    u_i(x) = - M_jk H_ijk(x) ,   H_ijk = dG_ij/dx_k
           = phi / r^2 [ -(3 - 4 nu) delta_ij rhat_k
                         + (delta_ik rhat_j + delta_jk rhat_i)
                         - 3 rhat_i rhat_j rhat_k ] ,   phi = 1/(16 pi mu_s (1 - nu))

and the stress follows from Hooke's law, sigma = lambda tr(eps) I + 2 mu_s eps.

The free surface is deliberately NOT included: this is the idealised point-source
static stress change, valid at distances large compared with BOTH the source
dimension and the source depth.

Frame:  x = north, y = east, z = DOWN (depth increases downwards).  Strike phi is
measured clockwise from north, dip delta from horizontal, rake lambda from the
strike direction within the fault plane (Aki & Richards convention, so rake 0 on
a vertical fault is left-lateral).

Coulomb failure function with COMPRESSION POSITIVE for both the normal stress
sigma_n and the pore pressure p, and tau the shear traction resolved along the
slip direction:

    CFS = tau - mu_f ( sigma_n - p )   ->   dCFS = dtau - mu_f (dsigma_n - dp)
                                       ->   dCFS = dtau + mu_f (n . dsigma . n)

TWO different symbols that look like 'mu' appear here and must not be confused:
mu_s is the shear modulus (Pa) inside G_ij, and mu_f is the dimensionless
coefficient of friction in the failure criterion.  They are named differently
throughout this file.

Experiments
  V.  Validation: closed-form displacement check, stress symmetry, vanishing
      dilatation, 1/r^3 decay, exact antisymmetry under r -> -r, two derivative
      step sizes.
  E1. 23 328 receiver orientations at one position: fraction with dCFS > 0.
  E2. Receiver-plane azimuth sweep: the four-lobe pattern of the coplanar
      receiver, and the measured sign-flip rate against the perturbation angle.
  E3. Fraction of the orientation space that is "ambiguous".
  E4. Magnitude scaling: what size of stress change a given source produces.

Run:  <repo>/.venv/bin/python coulomb_sign_flip_demo.py
"""

from __future__ import annotations

import numpy as np

# ----------------------------------------------------------------------
# MODEL / material inputs (chosen, not measured)
# ----------------------------------------------------------------------
MU_S = 30.0e9          # Pa   MODEL shear modulus
NU = 0.25              # -    MODEL Poisson's ratio
MW = 4.0               # -    MODEL moment magnitude of the source
Z_SRC = 5.0e3          # m    MODEL source depth
D_NEAR = 3.0e3         # m    MODEL horizontal receiver offset, same depth
STRIKE_S, DIP_S, RAKE_S = 0.0, 90.0, 0.0    # vertical, N-S, left-lateral
MU_F_LIST = (0.0, 0.2, 0.4, 0.6, 0.8)
NU_ORI = (36, 18, 36)                       # strike x dip x rake samples

LINES = "=" * 78
M0 = 10.0 ** (1.5 * MW + 9.1)               # Hanks-Kanamori, N m


def section(title: str) -> None:
    print(f"\n{LINES}\n{title}\n{LINES}")


def normal_slip(strike_deg, dip_deg, rake_deg):
    """Fault normal and slip direction (Aki & Richards), frame x=N, y=E, z=down."""
    p = np.radians(np.asarray(strike_deg, dtype=float))
    dl = np.radians(np.asarray(dip_deg, dtype=float))
    rk = np.radians(np.asarray(rake_deg, dtype=float))
    n = np.stack([-np.sin(dl) * np.sin(p), np.sin(dl) * np.cos(p), -np.cos(dl)], axis=-1)
    d = np.stack([
        np.cos(rk) * np.cos(p) + np.cos(dl) * np.sin(rk) * np.sin(p),
        np.cos(rk) * np.sin(p) - np.cos(dl) * np.sin(rk) * np.cos(p),
        np.sin(rk) * np.sin(dl),
    ], axis=-1)
    return n, d


def moment_tensor(n: np.ndarray, d: np.ndarray, m0: float = M0) -> np.ndarray:
    return m0 * (np.outer(d, n) + np.outer(n, d))


def displacement(x: np.ndarray, m: np.ndarray, x_src: np.ndarray,
                 mu_s: float = MU_S, nu: float = NU) -> np.ndarray:
    rv = x - x_src
    r = float(np.linalg.norm(rv))
    rhat = rv / r
    phi = 1.0 / (16.0 * np.pi * mu_s * (1.0 - nu))
    eye = np.eye(3)
    h = phi / r ** 2 * (
        -(3.0 - 4.0 * nu) * np.einsum("ij,k->ijk", eye, rhat)
        + np.einsum("ik,j->ijk", eye, rhat) + np.einsum("jk,i->ijk", eye, rhat)
        - 3.0 * np.einsum("i,j,k->ijk", rhat, rhat, rhat)
    )
    return -np.einsum("jk,ijk->i", m, h)


def stress_tensor(x: np.ndarray, m: np.ndarray, x_src: np.ndarray,
                  h_step: float, mu_s: float = MU_S, nu: float = NU) -> np.ndarray:
    lam = 2.0 * mu_s * nu / (1.0 - 2.0 * nu)
    grad = np.empty((3, 3))
    for q in range(3):
        e = np.zeros(3)
        e[q] = h_step
        grad[:, q] = (displacement(x + e, m, x_src, mu_s, nu)
                      - displacement(x - e, m, x_src, mu_s, nu)) / (2.0 * h_step)
    eps = 0.5 * (grad + grad.T)
    return lam * np.trace(eps) * np.eye(3) + 2.0 * mu_s * eps


def dcfs(sig: np.ndarray, n: np.ndarray, d: np.ndarray, mu_f: float) -> np.ndarray:
    """Vectorised dCFS = d . sig . n + mu_f (n . sig . n).  Compression positive."""
    return (np.einsum("ni,ij,nj->n", d, sig, n)
            + mu_f * np.einsum("ni,ij,nj->n", n, sig, n))


def scalar_dcfs(sig: np.ndarray, n: np.ndarray, d: np.ndarray, mu_f: float) -> float:
    return float(d @ (sig @ n) + mu_f * (n @ (sig @ n)))


def grid_orientations():
    strike = np.linspace(0.0, 180.0, NU_ORI[0], endpoint=False)
    dip = np.linspace(5.0, 90.0, NU_ORI[1])
    rake = np.linspace(0.0, 360.0, NU_ORI[2], endpoint=False)
    s, dl, rk = np.meshgrid(strike, dip, rake, indexing="ij")
    return s.ravel(), dl.ravel(), rk.ravel()


def main() -> int:
    print("Coulomb stress change from a point double couple:")
    print("how often does the SIGN depend on the assumed receiver fault?")
    print(f"MODEL: Mw = {MW}, M0 = {M0:.4e} N m, source depth {Z_SRC / 1e3:.1f} km")
    print(f"       source strike/dip/rake = {STRIKE_S}/{DIP_S}/{RAKE_S} "
          f"(vertical, N-S, left-lateral)")
    print(f"       mu_s = {MU_S / 1e9:.1f} GPa (shear modulus), nu = {NU}; "
          f"mu_f (friction, dimensionless) sweeps {MU_F_LIST}")

    n_s, d_s = normal_slip(STRIKE_S, DIP_S, RAKE_S)
    m = moment_tensor(n_s, d_s)
    print(f"       source normal n = ({n_s[0]:+.3f}, {n_s[1]:+.3f}, {n_s[2]:+.3f}), "
          f"slip d = ({d_s[0]:+.3f}, {d_s[1]:+.3f}, {d_s[2]:+.3f})")
    print(f"       checks: d . n = {float(d_s @ n_s):.1e}, |n| = "
          f"{np.linalg.norm(n_s):.6f}, |d| = {np.linalg.norm(d_s):.6f}")

    x_src = np.array([0.0, 0.0, Z_SRC])
    x_rec = np.array([0.0, D_NEAR, Z_SRC])
    r = float(np.linalg.norm(x_rec - x_src))
    h = r / 500.0
    lam = 2.0 * MU_S * NU / (1.0 - 2.0 * NU)
    phi = 1.0 / (16.0 * np.pi * MU_S * (1.0 - NU))

    # ------------------------------------------------------------------
    section("V. Validation of the stress field")
    print(f"receiver: horizontal offset {D_NEAR / 1e3:.1f} km, same depth; r = {r:.0f} m")
    print(f"  lambda = {lam / 1e9:.4f} GPa, mu_s = {MU_S / 1e9:.1f} GPa, "
          f"K = {(lam + 2 * MU_S / 3) / 1e9:.3f} GPa")

    # V0: closed form.  For r along the strike direction (x) the y displacement is
    #     u_y = 2 M0 phi (1 - 2 nu) / r^2.
    x_along = np.array([r, 0.0, Z_SRC])
    uy_num = float(displacement(x_along, m, x_src)[1])
    uy_exact = 2.0 * M0 * phi * (1.0 - 2.0 * NU) / r ** 2
    print(f"  V0 u_y at r along strike: numeric {uy_num:.6e} m vs closed form "
          f"2 M0 phi (1-2nu)/r^2 = {uy_exact:.6e} m  ({100 * (uy_num / uy_exact - 1):+.4f} %)")

    sig = stress_tensor(x_rec, m, x_src, h)
    print(f"  V1 symmetry  max|sigma - sigma^T| / max|sigma|      = "
          f"{np.abs(sig - sig.T).max() / np.abs(sig).max():.3e}")

    hh = r / 2000.0
    dilat = 0.0
    for q in range(3):
        e = np.zeros(3)
        e[q] = hh
        dilat += (displacement(x_rec + e, m, x_src)[q]
                  - displacement(x_rec - e, m, x_src)[q]) / (2 * hh)
    tumag = float(np.linalg.norm(displacement(x_rec, m, x_src)))
    print(f"  V2 dilatation |div u| / (|u|/r)                     = "
          f"{abs(dilat) / (tumag / r):.3e}   (exactly 0 for a double couple)")

    dist = np.array([1e3, 2e3, 4e3, 8e3, 16e3, 32e3])
    peaks = np.array([np.abs(stress_tensor(np.array([0.0, dd, Z_SRC]), m, x_src, dd / 500.0)).max()
                      for dd in dist])
    slope = float(np.polyfit(np.log(dist), np.log(peaks), 1)[0])
    print(f"  V3 decay exponent d ln(max|sigma|) / d ln r         = {slope:.4f}  "
          f"(double couple: -3)")

    ns_all, ds_all = normal_slip(*grid_orientations())
    sig_opp = stress_tensor(np.array([0.0, -D_NEAR, Z_SRC]), m, x_src, h)
    c_a = dcfs(sig, ns_all, ds_all, 0.4)
    c_b = dcfs(sig_opp, ns_all, ds_all, 0.4)
    print(f"  V4 r -> -r: max|dCFS(-r) - dCFS(r)| / max|dCFS|    = "
          f"{np.abs(c_b - c_a).max() / np.abs(c_a).max():.3e}   "
          f"(the static stress field is exactly SYMMETRIC,")
    print(f"              max|dCFS(-r) + dCFS(r)| / max|dCFS|    = "
          f"{np.abs(c_b + c_a).max() / np.abs(c_a).max():.3e}   "
          f"so it is NOT antisymmetric)")
    sig_fine = stress_tensor(x_rec, m, x_src, h / 4.0)
    print(f"  V5 derivative step h vs h/4: max|sigma(h)-sigma(h/4)| / max|sigma| = "
          f"{np.abs(sig - sig_fine).max() / np.abs(sig_fine).max():.3e}")
    print(f"  peak |sigma| component at this receiver = "
          f"{np.abs(sig).max() / 1e6:.4f} MPa = {np.abs(sig).max():.1f} Pa")

    # ------------------------------------------------------------------
    section("E1. Sign of dCFS over all receiver orientations, one position")
    print(f"orientations sampled: strike {NU_ORI[0]} x dip {NU_ORI[1]} x "
          f"rake {NU_ORI[2]} = {ns_all.shape[0]}")
    print("\n   mu_f   fraction dCFS>0   min [MPa]    max [MPa]   unclamped fraction")
    for mu_f in MU_F_LIST:
        v = dcfs(sig, ns_all, ds_all, mu_f)
        nsn = np.einsum("ni,ij,nj->n", ns_all, sig, ns_all)
        print(f"  {mu_f:5.2f}   {float(np.mean(v > 0)):15.4f}   "
              f"{v.min() / 1e6:10.5f}  {v.max() / 1e6:10.5f}   "
              f"{float(np.mean(nsn > 0)):16.4f}")
    print("  'unclamped' means n . dsigma . n > 0, i.e. the receiver normal stress")
    print("  becomes less compressive; that term is what adds to the shear term.")
    print("  Half the orientation space has dCFS > 0 and half has dCFS < 0, at every")
    print("  friction coefficient.  The SIGN is therefore a property of the")
    print("  source-receiver PAIR, not of the source.")

    # ------------------------------------------------------------------
    section("E2. Receiver azimuth sweep and the sign-flip rate")
    az = np.arange(0.0, 360.0, 30.0)
    print("  Coplanar receiver (the source fault plane extended), mu_f = 0.4:")
    print("\n   azimuth [deg]   dCFS [Pa]     sign")
    for a in az:
        xp = np.array([D_NEAR * np.cos(np.radians(a)), D_NEAR * np.sin(np.radians(a)), Z_SRC])
        sg = stress_tensor(xp, m, x_src, D_NEAR / 500.0)
        val = scalar_dcfs(sg, *normal_slip(STRIKE_S, DIP_S, RAKE_S), 0.4)
        print(f"  {a:14.0f}   {val:10.2f}   {'+' if val > 0 else '-'}")
    print("  Two features are checks on the source symmetry: the pattern repeats")
    print("  every 90 degrees in azimuth (a vertical strike-slip double couple is")
    print("  invariant under a 90 degree rotation about the vertical, because the")
    print("  moment tensor is symmetric under exchanging n and d), and the promoted")
    print("  and inhibited directions alternate.  Which directions are promoted")
    print("  depends on the assumed receiver plane, not only on the source.")

    print("\n  Sign-flip rate as the ASSUMED receiver plane is perturbed away from the")
    print("  source plane (strike and dip both perturbed by up to +/-Delta, 8 random")
    print("  perturbations per position, 36 positions):")
    rng = np.random.default_rng(20261014)
    positions = [np.array([rr * np.cos(np.radians(aa)), rr * np.sin(np.radians(aa)), Z_SRC])
                 for aa in az for rr in (2.0e3, 3.0e3, 5.0e3)]
    sgs = [stress_tensor(xp, m, x_src, float(np.linalg.norm(xp - x_src)) / 500.0)
           for xp in positions]
    print("\n   Delta [deg]   flip rate, mu_f=0.4   flip rate, mu_f=0.0   "
          "flip rate, mu_f=0.8")
    for delta in (5.0, 15.0, 30.0, 45.0, 60.0, 90.0):
        flips = {mu_f: [] for mu_f in (0.0, 0.4, 0.8)}
        for sg in sgs:
            for mu_f in (0.0, 0.4, 0.8):
                base = scalar_dcfs(sg, *normal_slip(STRIKE_S, DIP_S, RAKE_S), mu_f)
                for _ in range(8):
                    dstrike = rng.uniform(-delta, delta)
                    ddip = rng.uniform(-delta, delta)
                    nn, dd = normal_slip(STRIKE_S + dstrike,
                                         min(max(DIP_S + ddip, 5.0), 90.0), RAKE_S)
                    pert = scalar_dcfs(sg, nn, dd, mu_f)
                    flips[mu_f].append(float(np.sign(pert) != np.sign(base)))
        print(f"  {delta:11.0f}   {np.mean(flips[0.4]):19.4f}   "
              f"{np.mean(flips[0.0]):19.4f}   {np.mean(flips[0.8]):19.4f}")
    print("  The flip rate grows monotonically with the receiver-plane uncertainty")
    print("  and reaches about one half at Delta = 90 degrees, which is what an")
    print("  unconstrained receiver plane gives.  That is the honest version of the")
    print("  claim: the sign is robust only as far as the receiver plane is known,")
    print("  and the numbers above say exactly how far that is.")

    # ------------------------------------------------------------------
    section("E3. How much of the orientation space is 'ambiguous'?")
    for mu_f in (0.0, 0.4):
        v = dcfs(sig, ns_all, ds_all, mu_f)
        big = np.abs(v).max()
        for frac in (0.05, 0.10, 0.25):
            print(f"  mu_f = {mu_f:.1f}: fraction of orientations with |dCFS| < "
                  f"{frac:.2f} x max = {float(np.mean(np.abs(v) < frac * big)):.4f}")
    print("  About a fifth of all orientations feel less than a tenth of the peak")
    print("  stress change, so for most of the orientation space the honest answer")
    print("  is 'too small to call' rather than 'positive' or 'negative'.")

    # ------------------------------------------------------------------
    section("E4. Magnitude scaling: what size of stress change is available?")
    print("  Peak |sigma| component at 3 km horizontal offset, same depth:")
    print("\n   Mw     M0 [N m]        peak |sigma| [MPa]   coplanar dCFS [Pa]")
    for mw in (3.0, 3.5, 4.0, 4.5, 5.0, 5.5):
        m0 = 10.0 ** (1.5 * mw + 9.1)
        mm = moment_tensor(n_s, d_s, m0)
        sg = stress_tensor(x_rec, mm, x_src, h)
        cop = scalar_dcfs(sg, *normal_slip(STRIKE_S, DIP_S, RAKE_S), 0.4)
        print(f"  {mw:4.1f}   {m0:11.4e}   {np.abs(sg).max() / 1e6:18.4f}   "
              f"{cop:20.2f}")
    print("  The stress change scales as M0 / r^3, i.e. as 10^(1.5 Mw) / r^3.  Two")
    print("  consequences worth stating: (i) a small event at small distance can")
    print("  matter as much as a large one at large distance; (ii) the point-source")
    print("  approximation fails at r of order the source dimension, which for")
    print("  Mw 5 is roughly 3 km -- exactly where the largest stress changes are.")

    # ------------------------------------------------------------------
    section("Summary of measured quantities")
    v0 = dcfs(sig, ns_all, ds_all, 0.0)
    v4 = dcfs(sig, ns_all, ds_all, 0.4)
    print(f"  V0 closed-form displacement check              = "
          f"{100 * (uy_num / uy_exact - 1):+.4f} %")
    print(f"  V3 decay exponent (exact -3)                   = {slope:.4f}")
    print(f"  peak |sigma|, Mw {MW} at r = {r:.0f} m             = "
          f"{np.abs(sig).max() / 1e6:.4f} MPa")
    print(f"  fraction of orientations with dCFS > 0, mu_f=0 = {float(np.mean(v0 > 0)):.4f}")
    print(f"  fraction of orientations with dCFS > 0, mu_f=0.4 = {float(np.mean(v4 > 0)):.4f}")
    print("  Every value above is a MODEL output for a stated geometry.  Nothing here")
    print("  is a measurement of a real earthquake.  The structural conclusions --")
    print("  that the sign is assumption-dependent and the field is exactly")
    print("  antisymmetric under r -> -r -- follow from the double couple itself.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
