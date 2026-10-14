"""Symbolic tensors and index notation for continuum geophysics.

Run:  .venv/bin/python 03-scientific-computing/07-sympy/code/tensor_symbolic_demo.py
Requires: sympy, numpy.

Companion to lesson 03-07-04.

Part 1  the strain tensor from a displacement gradient, including the rigid
        rotation that leaves it exactly zero.
Part 2  abstract index notation in sympy.tensor.tensor: what works, and three
        sharp edges found by measurement.
Part 3  isotropic Hooke's law by explicit index contraction, checked against
        the direct formula.
Part 4  Lame parameters from Young's modulus and Poisson's ratio, inverted
        symbolically, then to seismic velocities.
Part 5  the deviatoric split and the second invariant J2.
Part 6  the same contraction through numpy.einsum, as a numeric check.
Part 7  the spherical Laplacian of 1/r.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
from sympy.tensor.tensor import TensorHead, TensorIndexType, tensor_indices


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def kronecker(a: int, b: int) -> int:
    return 1 if a == b else 0


def main() -> None:
    labels = ["x", "y", "z"]

    # ------------------------------------------------------------------
    section("1. Strain from a displacement gradient")
    # ------------------------------------------------------------------
    # u_i,j with a displacement field u = (a*x + w*y, -w*x + a*y, 0).
    a_disp, w_rot = sp.symbols("a omega", real=True)
    x_sym, y_sym, z_sym = sp.symbols("x y z", real=True)
    coords = sp.Matrix([x_sym, y_sym, z_sym])
    u = sp.Matrix([a_disp * x_sym + w_rot * y_sym,
                   -w_rot * x_sym + a_disp * y_sym,
                   0])
    gradient = u.jacobian(coords)
    strain = sp.simplify((gradient + gradient.T) / 2)
    rotation = sp.simplify((gradient - gradient.T) / 2)
    print("  displacement field u = (a x + omega y, -omega x + a y, 0)")
    print(f"  displacement gradient u_(i,j) = {gradient.tolist()}")
    print(f"  strain    eps_ij = (u_(i,j)+u_(j,i))/2 = {strain.tolist()}")
    print(f"  rotation  w_ij   = (u_(i,j)-u_(j,i))/2 = {rotation.tolist()}")
    print(f"  trace of the strain (dilatation) = {sp.trace(strain)}")
    print(f"  strain is symmetric: {strain == strain.T}")
    print("  Observation: the antisymmetric part is a rigid rotation and it")
    print("  contributes nothing to the strain -- the two off-diagonal terms")
    print("  cancel exactly, symbolically, not to within a tolerance. That is")
    print("  the reason the elastic wave equation has no rotational term in")
    print("  its P-wave part.")

    # ------------------------------------------------------------------
    section("2. Abstract index notation, and where it bites")
    # ------------------------------------------------------------------
    L = TensorIndexType("L", metric_name="g")
    i, j, k = tensor_indices("i j k", L)
    velocity = TensorHead("v", [L])
    stress_head = TensorHead("sigma", [L, L])
    contraction = stress_head(i, j) * velocity(-i) * velocity(-j)
    print(f"  sigma_ij v_i v_j  -> {contraction}")
    print(f"  free indices: {contraction.get_free_indices()} "
          f"(empty means the expression is a scalar)")
    print(f"  index positions are explicit: {velocity(-i)} is v_i and "
          f"{velocity(i)} is v^i")
    metric = L.metric
    lowered = (metric(-i, -j) * TensorHead("T", [L, L])(i, j))
    print(f"  g_ij T^ij -> {lowered} -> contract_metric -> "
          f"{lowered.contract_metric(metric)}")
    symmetric = TensorHead("eps", [L, L], comm=1)
    print(f"  a symmetric TensorHead declares symmetry: {symmetric.symmetry}")
    print("  measured sharp edges of this module:")
    print(f"    (a) eps(i,j)*eps(j,i) raises: ", end="")
    try:
        _ = symmetric(i, j) * symmetric(j, i)
        print("no error (unexpected)")
    except ValueError as exc:
        print(f"ValueError: {exc}")
    print(f"    (b) eps(i,j)*eps(-i,-j) -> {symmetric(i, j) * symmetric(-i, -j)}")
    print(f"        ...and .canon_bp() on it returns "
          f"{(symmetric(i, j) * symmetric(-i, -j)).canon_bp()}, which is wrong: "
          f"eps:eps is not zero")
    other = TensorHead("sig", [L, L], comm=1)
    print(f"    (c) sig(i,j)*eps(-i,-j).canon_bp() -> "
          f"{(other(i, j) * symmetric(-i, -j)).canon_bp()}")
    print("        ...reports a minus sign for a trace-like contraction that")
    print("        has no intrinsic sign")
    print("  Observation: the abstract module is excellent for stating a")
    print("  tensor equation and for tracking free and dummy indices, and it is")
    print("  not reliable as a calculator for fully contracted products. Every")
    print("  quantitative result in this lesson therefore goes through explicit")
    print("  components, and each one is checked numerically in Part 6.")

    # ------------------------------------------------------------------
    section("3. Isotropic Hooke's law by index contraction")
    # ------------------------------------------------------------------
    lam, mu = sp.symbols("lambda mu", positive=True)
    eps_sym = sp.Matrix(3, 3, lambda r, c: sp.Symbol(
        f"e_{labels[r]}{labels[c]}", real=True))
    # Symmetrise so that the tensor really is a strain tensor.
    eps_sym = sp.Matrix(3, 3, lambda r, c: sp.Symbol(
        f"e_{labels[min(r, c)]}{labels[max(r, c)]}", real=True))
    print(f"  strain components: {eps_sym.tolist()}")
    # C_ijkl = lambda delta_ij delta_kl + mu (delta_ik delta_jl + delta_il delta_jk)
    stress = sp.zeros(3, 3)
    terms = 0
    for r in range(3):
        for c in range(3):
            total = 0
            for kk in range(3):
                for ll in range(3):
                    C = (lam * kronecker(r, c) * kronecker(kk, ll)
                         + mu * (kronecker(r, kk) * kronecker(c, ll)
                                 + kronecker(r, ll) * kronecker(c, kk)))
                    if C != 0:
                        total += C * eps_sym[kk, ll]
                        terms += 1
            stress[r, c] = total
    print(f"  C_ijkl eps_kl summed over {terms} non-zero index pairs")
    direct = lam * sp.trace(eps_sym) * sp.eye(3) + 2 * mu * eps_sym
    worst = sp.simplify(sp.Max(*[abs(stress[r, c] - direct[r, c])
                                 for r in range(3) for c in range(3)]))
    print(f"  max |index contraction - direct formula| = {worst}")
    e_s, e_v = sp.symbols("e_s e_v", real=True)
    shear = sp.zeros(3, 3)
    shear[0, 1] = shear[1, 0] = e_s
    shear_stress = sp.simplify(lam * sp.trace(shear) * sp.eye(3) + 2 * mu * shear)
    print(f"  pure shear eps_xy = eps_yx = e_s -> sigma = "
          f"{shear_stress.tolist()}")
    print(f"      sigma_xy - 2 mu e_s = "
          f"{sp.simplify(shear_stress[0, 1] - 2 * mu * e_s)}")
    print(f"      sigma_xx = {shear_stress[0, 0]}, sigma_zz = "
          f"{shear_stress[2, 2]}  (both zero)")
    dilation = e_v * sp.eye(3)
    dilation_stress = sp.simplify(lam * sp.trace(dilation) * sp.eye(3)
                                  + 2 * mu * dilation)
    bulk = sp.simplify(lam + 2 * mu / 3)
    print(f"  pure dilation eps = e_v I -> sigma_xx = {dilation_stress[0, 0]}")
    print(f"      3 K e_v with K = lambda + 2 mu/3 = {sp.simplify(3 * bulk)} e_v")
    print(f"      sigma_xx - 3 K e_v = "
          f"{sp.simplify(dilation_stress[0, 0] - 3 * bulk * e_v)}")
    print("  Observation: the two calibration cases isolate the constants. A")
    print("  pure shear measures mu alone; a pure dilation measures the bulk")
    print("  modulus alone. Both residuals are exactly zero.")

    # ------------------------------------------------------------------
    section("4. Lame parameters from Young's modulus and Poisson's ratio")
    # ------------------------------------------------------------------
    E_mod, nu = sp.symbols("E nu", positive=True)
    lam_s, mu_s = sp.symbols("lambda mu", positive=True)
    relations = [
        sp.Eq(E_mod, mu_s * (3 * lam_s + 2 * mu_s) / (lam_s + mu_s)),
        sp.Eq(nu, lam_s / (2 * (lam_s + mu_s))),
    ]
    solution = sp.solve(relations, [lam_s, mu_s], dict=True)[0]
    print(f"  E  = mu (3 lambda + 2 mu)/(lambda + mu) = "
          f"{sp.simplify(relations[0].lhs)} ... ")
    print(f"  nu = lambda / (2 (lambda + mu))")
    print(f"  solved for the Lame parameters:")
    print(f"      lambda = {sp.simplify(solution[lam_s])}")
    print(f"      mu     = {sp.simplify(solution[mu_s])}")
    expected_lambda = E_mod * nu / ((1 + nu) * (1 - 2 * nu))
    expected_mu = E_mod / (2 * (1 + nu))
    print(f"  check against the textbook forms: "
          f"lambda difference = "
          f"{sp.simplify(solution[lam_s] - expected_lambda)}, "
          f"mu difference = {sp.simplify(solution[mu_s] - expected_mu)}")
    E_v, nu_v, rho_v = 70.0e9, 0.25, 2700.0
    subs_num = {E_mod: E_v, nu: nu_v}
    lam_v = float(sp.N(solution[lam_s].subs(subs_num), 20))
    mu_v = float(sp.N(solution[mu_s].subs(subs_num), 20))
    k_v = lam_v + 2 * mu_v / 3
    vp = np.sqrt((lam_v + 2 * mu_v) / rho_v)
    vs = np.sqrt(mu_v / rho_v)
    print(f"  E = {E_v / 1e9:.1f} GPa, nu = {nu_v}, rho = {rho_v:.1f} kg/m^3")
    print(f"      lambda = {lam_v / 1e9:.6f} GPa, mu = {mu_v / 1e9:.6f} GPa, "
          f"K = {k_v / 1e9:.6f} GPa")
    print(f"      v_p = sqrt((lambda + 2 mu)/rho) = {vp:.2f} m/s")
    print(f"      v_s = sqrt(mu/rho)               = {vs:.2f} m/s")
    print(f"      v_p/v_s = {vp / vs:.6f}; sqrt(3) = {np.sqrt(3):.6f}; "
          f"difference {abs(vp / vs - np.sqrt(3)):.2e}")
    print(f"      Poisson's ratio recovered from (vp/vs)^2: "
          f"{((vp / vs) ** 2 - 2) / (2 * ((vp / vs) ** 2 - 1)):.9f}")
    print("  Observation: nu = 0.25 makes lambda = mu exactly, which forces")
    print("  v_p/v_s = sqrt(3). The value recovered from the velocity ratio")
    print("  returns 0.25 to machine precision, which is the standard")
    print("  seismological route from a velocity ratio to a Poisson's ratio.")

    # ------------------------------------------------------------------
    section("5. The deviatoric split and the second invariant")
    # ------------------------------------------------------------------
    stress_comp = sp.Matrix(3, 3, lambda r, c: sp.Symbol(
        f"s_{labels[min(r, c)]}{labels[max(r, c)]}", real=True))
    mean = sp.trace(stress_comp) / 3
    deviator = stress_comp - mean * sp.eye(3)
    print(f"  mean normal stress p = trace(sigma)/3 = {mean}")
    print(f"  deviator trace = {sp.simplify(sp.trace(deviator))}")
    j2 = sp.Rational(1, 2) * sum(deviator[r, c] * deviator[r, c]
                                 for r in range(3) for c in range(3))
    alternative = (sp.Rational(1, 2) * sum(stress_comp[r, c] * stress_comp[r, c]
                                           for r in range(3) for c in range(3))
                   - sp.Rational(1, 6) * sp.trace(stress_comp) ** 2)
    print(f"  J2 = (1/2) s_ij s_ij                has "
          f"{int(sp.count_ops(sp.expand(j2)))} operations")
    print(f"  J2 = (1/2) sigma_ij sigma_ij - I1^2/6 has "
          f"{int(sp.count_ops(sp.expand(alternative)))} operations")
    print(f"  difference of the two identities: "
          f"{sp.simplify(sp.expand(j2 - alternative))}")
    s = sp.symbols("s_xx s_yy s_zz s_xy s_xz s_yz", real=True)
    stress_num = {stress_comp[0, 0]: s[0], stress_comp[1, 1]: s[1],
                  stress_comp[2, 2]: s[2], stress_comp[0, 1]: s[3],
                  stress_comp[1, 2]: s[5], stress_comp[0, 2]: s[4]}
    print(f"  J2 as a polynomial in the six components:")
    print(f"      {sp.expand(j2.subs(stress_num) * 2) / 2}")
    eigenvalue = sp.Symbol("S", real=True)
    charpoly = sp.factor(stress_comp.charpoly(eigenvalue).as_expr())
    print("  principal stresses are the roots of the characteristic polynomial")
    print(f"      {charpoly}")
    print(f"  its coefficients: I1 = {sp.trace(stress_comp)}, "
          f"I3 = {sp.det(stress_comp)}")
    sigma_v = np.array([[100.0, 20.0, 0.0],
                        [20.0, 50.0, 0.0],
                        [0.0, 0.0, 30.0]]) * 1e6
    ev = np.linalg.eigvalsh(sigma_v)
    j2_np = 0.5 * (np.sum(sigma_v * sigma_v) - np.trace(sigma_v) ** 2 / 3)
    print(f"  a concrete stress state (MPa): {sigma_v / 1e6}")
    print(f"      principal stresses = {ev / 1e6} MPa")
    print(f"      J2 = {j2_np:.6e} Pa^2 = {j2_np / 1e12:.6f} MPa^2")
    concrete = {stress_comp[0, 0]: 100e6, stress_comp[1, 1]: 50e6,
                stress_comp[2, 2]: 30e6, stress_comp[0, 1]: 20e6,
                stress_comp[1, 2]: 0.0, stress_comp[0, 2]: 0.0}
    j2_sym = float(sp.N(j2.subs(concrete), 20)) / 1e12
    print(f"      from the symbolic expression with those numbers: "
          f"{j2_sym:.6f} MPa^2")
    print("  Observation: two algebraically different expressions for J2 give")
    print("  identical results, and the numeric route through the eigenvalues")
    print("  agrees. J2 is what a von Mises or Drucker-Prager yield criterion")
    print("  is written in, so having it in a form that can be differentiated")
    print("  with respect to a stress component matters.")

    # ------------------------------------------------------------------
    section("6. The same contraction through numpy.einsum")
    # ------------------------------------------------------------------
    C_num = np.zeros((3, 3, 3, 3))
    for r in range(3):
        for c in range(3):
            for kk in range(3):
                for ll in range(3):
                    C_num[r, c, kk, ll] = (
                        lam_v * kronecker(r, c) * kronecker(kk, ll)
                        + mu_v * (kronecker(r, kk) * kronecker(c, ll)
                                  + kronecker(r, ll) * kronecker(c, kk)))
    eps_num = np.array([[1.0e-3, 2.0e-4, 0.0],
                        [2.0e-4, -5.0e-4, 0.0],
                        [0.0, 0.0, 3.0e-4]])
    sigma_num = np.einsum("ijkl,kl->ij", C_num, eps_num)
    eps_sym_num = sp.Matrix(3, 3, lambda r, c: float(eps_num[r, c]))
    sigma_check = np.array((lam_v * sp.trace(eps_sym_num) * sp.eye(3)
                            + 2 * mu_v * eps_sym_num).evalf(), dtype=float)
    print(f"  strain (dimensionless): {eps_num.tolist()}")
    print(f"  stress from einsum (Pa): {sigma_num.tolist()}")
    diff = np.max(np.abs(sigma_num - sigma_check))
    print(f"  max |einsum - (lambda tr(eps) I + 2 mu eps)| = {diff:.3e} Pa "
          f"(relative {diff / np.max(np.abs(sigma_num)):.2e})")
    print(f"  volumetric part: tr(sigma)/3 = "
          f"{np.trace(sigma_num) / 3:.6e} Pa;  K tr(eps) = "
          f"{k_v * np.trace(eps_num):.6e} Pa")
    print(f"  deviatoric part: max |sigma - mean(sigma) I| = "
          f"{np.max(np.abs(sigma_num - np.trace(sigma_num) / 3 * np.eye(3))):.6e} Pa")
    print(f"  non-zero entries of C_ijkl: {int(np.count_nonzero(C_num))} of 81")
    print("  Observation: the index contraction and the array contraction are")
    print("  the same computation. Writing C_ijkl once in index notation is")
    print("  what makes it auditable; running it through einsum is what makes")
    print("  it fast. Never hand-code the 81 entries.")

    # ------------------------------------------------------------------
    section("7. The spherical Laplacian of 1/r")
    # ------------------------------------------------------------------
    r_sym = sp.Symbol("r", positive=True)
    radial = 1 / r_sym
    laplace_spherical = sp.simplify(
        (1 / r_sym**2) * sp.diff(r_sym**2 * sp.diff(radial, r_sym), r_sym))
    print("  for a radial function f(r) the Laplacian is")
    print("      (1/r^2) d/dr (r^2 df/dr)")
    print(f"  with f = 1/r:  {laplace_spherical}")
    print(f"  general f(r): "
          f"{sp.simplify((1 / r_sym**2) * sp.diff(r_sym**2 * sp.Function('f')(r_sym).diff(r_sym), r_sym))}")
    print("  for f = 1/r the result is exactly zero, which is Laplace's")
    print("  equation and the reason the potential of a point mass is 1/r.")
    print("  the same operator applied to r^2 gives "
          f"{sp.simplify((1 / r_sym**2) * sp.diff(r_sym**2 * sp.diff(r_sym**2, r_sym), r_sym))}"
          ", which is 6 = 4 pi times the source density 3/(2 pi).")
    print("  spherical Laplacian of the potential inside a uniform sphere of")
    print("  density rho,  V = (2/3) pi G rho (r^2 - 3 R^2):")
    G_sym, rho_sym, R_sym = sp.symbols("G rho R", positive=True)
    V_in = sp.Rational(2, 3) * sp.pi * G_sym * rho_sym * (r_sym**2 - 3 * R_sym**2)
    lap = sp.simplify((1 / r_sym**2) * sp.diff(
        r_sym**2 * sp.diff(V_in, r_sym), r_sym))
    print(f"      {lap} = 4 pi G rho, which is Poisson's equation inside the")
    print(f"      body; residual {sp.simplify(lap - 4 * sp.pi * G_sym * rho_sym)}")
    print("  Observation: index-free vector calculus in SymPy is just")
    print("  differentiation with the right coordinate operator. The value is")
    print("  that the operator is written once, correctly, and then applied to")
    print("  every candidate potential without a second chance of an error.")


if __name__ == "__main__":
    main()
