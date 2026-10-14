"""From a symbolic result to fast numerical code, and the checks that prove it.

Run:  .venv/bin/python 03-scientific-computing/07-sympy/code/code_generation_demo.py
Requires: sympy, numpy, scipy, and a C compiler (cc) for Part 5.

Companion to lesson 03-07-05.

Part 1  derive a closed form by hand, verify it symbolically, and check it
        against numerical quadrature of the original integral.
Part 2  build one Cartesian expression bundle and measure what
        common-subexpression elimination removes.
Part 3  lambdify it for NumPy, and count how many Python calls the vectorised
        and the scalar routes need.
Part 4  check the float64 evaluation against 40-digit arithmetic.
Part 5  generate C from the same expression, compile it, run it, compare.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import integrate

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
CC = shutil.which("cc") or shutil.which("clang")


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def cse_c_code(expressions, names):
    """Emit C for ``expressions`` using cse, with temporaries ordered.

    ``free_symbols`` of the bundle are the C variables that already exist
    (X, Y, Z here), so they seed the set of names that are available.
    """
    replacements, reduced = sp.cse(expressions, optimizations="basic")
    defined: set = set()
    for expr in list(expressions) + [v for _, v in replacements]:
        defined |= expr.free_symbols
    lines: list[str] = []
    pending = list(replacements)
    while pending:
        progressed = False
        for item in list(pending):
            sym, value = item
            if value.free_symbols <= defined:
                lines.append(f"    const double {sym} = {sp.ccode(value)};")
                defined.add(sym)
                pending.remove(item)
                progressed = True
        if not progressed:
            raise RuntimeError("circular or unordered cse replacements")
    results = []
    for name, expr in zip(names, reduced):
        lines.append(f"    const double {name} = {sp.ccode(expr)};")
        results.append(name)
    return "\n".join(lines), len(replacements), results


def main() -> None:
    # ------------------------------------------------------------------
    section("1. A closed form, verified symbolically and numerically")
    # ------------------------------------------------------------------
    xi, zeta, x, z = sp.symbols("xi zeta x z", real=True)
    h_sq = sp.Symbol("h_sq", positive=True)
    kernel = (z - zeta) / ((x - xi) ** 2 + (z - zeta) ** 2)
    antideriv_zeta = -sp.Rational(1, 2) * sp.log((x - xi) ** 2 + (z - zeta) ** 2)
    print("  integrand d(zeta):  (z - zeta) / ((x - xi)^2 + (z - zeta)^2)")
    print(f"  proposed antiderivative: {antideriv_zeta}")
    print(f"  d/dzeta of it minus the integrand simplifies to "
          f"{sp.simplify(sp.diff(antideriv_zeta, zeta) - kernel)}")
    u = xi - x
    antideriv_xi = sp.Rational(1, 2) * (u * sp.log(u**2 + h_sq) - 2 * u
                                        + 2 * sp.sqrt(h_sq) * sp.atan(u / sp.sqrt(h_sq)))
    print("  the inner integral leaves a factor of 1/2, so the second step")
    print("  needs the antiderivative of (1/2) ln(u^2 + h^2), u = xi - x")
    print(f"  proposed: {antideriv_xi}")
    residual_xi = sp.simplify(sp.diff(antideriv_xi, xi)
                              - sp.Rational(1, 2) * sp.log(u**2 + h_sq))
    print(f"  d/dxi of it minus (1/2) ln(u^2 + h^2) simplifies to {residual_xi}")
    G_sym, rho_sym = sp.symbols("G rho", positive=True)
    x_1, x_2, z_1, z_2 = sp.symbols("x_1 x_2 z_1 z_2", real=True)

    def F(xi_value, z_k):
        uu = xi_value - x
        hh = z - z_k
        return sp.Rational(1, 2) * (uu * sp.log(uu**2 + hh**2) - 2 * uu
                                    + 2 * hh * sp.atan(uu / hh))

    closed_form = G_sym * rho_sym * (
        F(x_2, z_1) - F(x_1, z_1) - F(x_2, z_2) + F(x_1, z_2))
    print("  vertical gravity of a 2-D rectangular prism, infinite strike:")
    print("      g_z = G rho [F(x2,z1) - F(x1,z1) - F(x2,z2) + F(x1,z2)]")
    print(f"      with F built from the two verified antiderivatives "
          f"({int(sp.count_ops(closed_form))} operations)")
    gz_num = sp.lambdify((x, z, G_sym, rho_sym, x_1, x_2, z_1, z_2),
                         closed_form, "numpy")
    G_v, rho_v = 6.67430e-11, 2670.0
    x1v, x2v, z1v, z2v = -2000.0, 2000.0, 200.0, 1200.0
    print(f"  prism: x in [{x1v:.0f}, {x2v:.0f}] m, depth z in "
          f"[{z1v:.0f}, {z2v:.0f}] m, rho = {rho_v:.0f} kg/m^3")
    for x_obs in (0.0, 1500.0, 5000.0):
        z_obs = 0.0
        closed = float(gz_num(x_obs, z_obs, G_v, rho_v, x1v, x2v, z1v, z2v))
        numeric, err = integrate.dblquad(
            lambda zeta_v, xi_v: G_v * rho_v * (z_obs - zeta_v)
            / ((x_obs - xi_v) ** 2 + (z_obs - zeta_v) ** 2),
            x1v, x2v, z1v, z2v, epsabs=1e-12, epsrel=1e-12)
        print(f"      x = {x_obs:>7.0f} m: closed form {closed * 1e5:+.9f} mGal, "
              f"dblquad {numeric * 1e5:+.9f} mGal, "
              f"relative difference {abs(closed - numeric) / abs(numeric):.2e}")
    _, n_terms = sp.cse(closed_form)
    print("  Observation: two verified antiderivatives turn a double integral")
    print("  into an evaluation, and the quadrature agrees to the tolerance")
    print("  asked of it. The symbol is what makes the closed form auditable:")
    print("  the proof that it is right is a derivative, not a fitted constant.")

    # ------------------------------------------------------------------
    section("2. One expression bundle, and what cse removes")
    # ------------------------------------------------------------------
    px, py, pz = sp.symbols("X Y Z", real=True)
    d1, d2, d3 = sp.symbols("d_1 d_2 d_3", real=True)
    quad = sp.Matrix(3, 3, lambda i, j: sp.Symbol(
        f"Q_{min(i, j)}{max(i, j)}", real=True))
    mass_sym = sp.Symbol("M")
    r_sq = px**2 + py**2 + pz**2
    coords = [px, py, pz]
    potential = (mass_sym * r_sq**2
                 - (d1 * px + d2 * py + d3 * pz) * r_sq
                 + sp.Rational(1, 2) * sum(
                     quad[i, j] * coords[i] * coords[j]
                     for i in range(3) for j in range(3)))
    params = {mass_sym: 5.972e24, d1: 1.0e5, d2: -2.0e5, d3: 3.0e5}
    params.update({quad[i, j]: (i + 1) * (j + 1) * 1.0e10
                   for i in range(3) for j in range(i, 3)})
    bundle = [sp.expand(potential).subs(params)]
    bundle += [sp.expand(sp.diff(potential, c)).subs(params) for c in coords]
    naive_ops = sum(int(sp.count_ops(e)) for e in bundle)
    replacements, reduced = sp.cse(bundle, optimizations="basic")
    cse_ops = (sum(int(sp.count_ops(e)) for e in reduced)
               + sum(int(sp.count_ops(v)) for _, v in replacements))
    print("  bundle: a Cartesian multipole potential W = M r^4 - d_i X_i r^2")
    print("          + (1/2) Q_ij X_i X_j  and its three partial derivatives,")
    print("          with r^2 = X^2 + Y^2 + Z^2 and numeric moments")
    print(f"  naive operation count           : {naive_ops}")
    print(f"  cse temporaries introduced      : {len(replacements)}")
    print(f"  operation count after cse       : {cse_ops}")
    print(f"  reduction                       : "
          f"{100 * (1 - cse_ops / naive_ops):.1f} %")
    for sym, value in replacements[:6]:
        print(f"      {sym} = {value}")
    print(f"      ... and {max(0, len(replacements) - 6)} more")
    print("  Observation: cse found r^2-style sharing and the products")
    print("  X_i X_j. The saving is real but modest here; it is largest when")
    print("  the same subexpression appears many times, which is exactly the")
    print("  case for a polynomial written in more than one variable.")

    # ------------------------------------------------------------------
    section("3. lambdify, and counting evaluations")
    # ------------------------------------------------------------------
    funcs = sp.lambdify((px, py, pz), bundle, "numpy")
    X = np.linspace(-1.0, 1.0, 100)
    Y = np.linspace(-1.0, 1.0, 100)
    Z = np.linspace(-1.0, 1.0, 100)
    XX, YY, ZZ = np.meshgrid(X, Y, Z, indexing="ij")
    grid_points = XX.size
    values = funcs(XX, YY, ZZ)
    print(f"  grid: {grid_points} points ({XX.shape} array)")
    print(f"  Python calls to the lambdified function: 1 (whole array at once)")
    print(f"  Python calls a scalar 'math' module lambdify would need: "
          f"{grid_points}")

    def direct(pxv, pyv, pzv):
        r2 = pxv**2 + pyv**2 + pzv**2
        W = (5.972e24 * r2**2
             - (1.0e5 * pxv - 2.0e5 * pyv + 3.0e5 * pzv) * r2)
        q = {(0, 0): 1.0e10, (0, 1): 2.0e10, (0, 2): 3.0e10,
             (1, 1): 4.0e10, (1, 2): 6.0e10, (2, 2): 9.0e10}
        W = W + 0.5 * ((q[(0, 0)] * pxv * pxv + q[(1, 1)] * pyv * pyv
                        + q[(2, 2)] * pzv * pzv)
                       + 2 * (q[(0, 1)] * pxv * pyv + q[(0, 2)] * pxv * pzv
                              + q[(1, 2)] * pyv * pzv))
        return W

    reference = direct(XX, YY, ZZ)
    diff = np.abs(values[0] - reference)
    scale = np.max(np.abs(reference))
    print(f"  max |lambdified - hand-written NumPy difference| = "
          f"{float(diff.max()):.3e}")
    print(f"  largest value in the array                       = {scale:.6e}")
    print(f"  relative difference                              = "
          f"{float(diff.max()) / scale:.3e}")
    print("  Observation: the two routes are the same arithmetic in a different")
    print("  order, so they agree to rounding and not to the last bit. A")
    print("  symbolic derivation does not make a float computation exact; it")
    print("  makes the expression it computes the one you intended.")

    # ------------------------------------------------------------------
    section("4. The float64 result against 40-digit arithmetic")
    # ------------------------------------------------------------------
    params_hi = {sym: sp.Float(float(value), 40)
                 for sym, value in params.items()}
    expr_hi = potential.subs(params_hi)
    scalar = sp.lambdify((px, py, pz), bundle[0], "math")
    rng = np.random.default_rng(20261014)
    probes = rng.uniform(-2.0, 2.0, size=(200, 3))
    worst = (0.0, None, 0.0, 0.0)
    exact_agreements = 0
    for pv in probes:
        high = float(sp.N(expr_hi.subs(
            {px: sp.Float(float(pv[0]), 40), py: sp.Float(float(pv[1]), 40),
             pz: sp.Float(float(pv[2]), 40)}), 40))
        low = scalar(float(pv[0]), float(pv[1]), float(pv[2]))
        if low == high:
            exact_agreements += 1
        relative = abs(low - high) / abs(high) if high != 0 else 0.0
        if relative > worst[0]:
            worst = (relative, tuple(pv), high, low)
    print(f"  {len(probes)} probe points in [-2, 2]^3, evaluated twice:")
    print(f"  binary64 via lambdify, and 40-digit via SymPy evalf")
    print(f"  probes where the two agree to the last bit: "
          f"{exact_agreements} of {len(probes)}")
    print(f"  worst relative difference: {worst[0]:.3e} at "
          f"X, Y, Z = ({worst[1][0]:+.6f}, {worst[1][1]:+.6f}, {worst[1][2]:+.6f})")
    print(f"      high precision {worst[2]:.15e}, float64 {worst[3]:.15e}")
    print(f"  that is {worst[0] / np.finfo(float).eps:.2f} ulp of binary64 "
          f"(eps = {np.finfo(float).eps:.3e})")
    print("  Observation: the float64 answer is a few ulp away from the true")
    print("  value and at most probes it is exact. High precision tells you")
    print("  which digits the float route can be trusted to -- here about 15 --")
    print("  and nothing about whether the model that produced the expression")
    print("  was the right model.")

    # ------------------------------------------------------------------
    section("5. C code generation, compilation and comparison")
    # ------------------------------------------------------------------
    if CC is None:
        print("  no C compiler found on PATH; skipping this part")
    else:
        ARTIFACTS.mkdir(exist_ok=True)
        try:
            names = ["W", "dW_dX", "dW_dY", "dW_dZ"]
            body, n_temp, outputs = cse_c_code(bundle, names)
            probes = [(0.37, -0.52, 0.81), (-0.9, 0.1, 0.25),
                      (0.0, 0.0, 0.0)]
            print(f"  generated {n_temp} temporaries and {len(outputs)} outputs")
            source = ["#include <math.h>", "#include <stdio.h>", "",
                      "int main(void) {"]
            for i, (pv, qv, rv) in enumerate(probes):
                source.append("    {")
                source.append(f"        const double X = {pv!r}, Y = {qv!r}, "
                              f"Z = {rv!r};")
                source.append("\n".join("    " + line[4:]
                                        for line in body.splitlines()))
                for name in outputs:
                    source.append(
                        f'        printf("value {name} %d %.17g\\n", {i}, {name});')
                source.append("    }")
            source.append("    return 0;")
            source.append("}")
            source_text = "\n".join(source) + "\n"
            c_path = ARTIFACTS / "generated_multipole.c"
            exe_path = ARTIFACTS / "generated_multipole"
            c_path.write_text(source_text, encoding="utf-8")
            print(f"  wrote {c_path.name}: {len(source_text.splitlines())} lines, "
                  f"{len(source_text)} characters")
            compile_run = subprocess.run(
                [CC, "-O2", "-o", str(exe_path), str(c_path), "-lm"],
                capture_output=True, text=True)
            print(f"  '{Path(CC).name} -O2' exit code: {compile_run.returncode}")
            if compile_run.returncode != 0:
                print(f"  compiler stderr: {compile_run.stderr.strip()[:400]}")
                raise SystemExit(1)
            print(f"  compiled binary size: {exe_path.stat().st_size} bytes")
            run = subprocess.run([str(exe_path)], capture_output=True, text=True)
            parsed: dict = {}
            for line in run.stdout.splitlines():
                _, name, index, value = line.split()
                parsed[(name, int(index))] = float(value)
            exact = 0
            worst_rel = 0.0
            for i, pv in enumerate(probes):
                for j, name in enumerate(outputs):
                    expected = float(np.asarray(
                        funcs(pv[0], pv[1], pv[2]))[j])
                    got = parsed[(name, i)]
                    rel = (abs(got - expected) / abs(expected)
                           if expected != 0 else abs(got - expected))
                    exact += int(got == expected)
                    worst_rel = max(worst_rel, rel)
                    print(f"      probe {i} {name:<7} C {got:+.12e}   "
                          f"NumPy {expected:+.12e}   relative {rel:.2e}")
            pairs = len(probes) * len(outputs)
            print(f"  bit-identical at {exact} of {pairs} (probe, output) pairs; "
                  f"worst relative difference {worst_rel:.2e}")
            print("  Observation: the C is generated from the same expression,")
            print("  compiled at -O2, and reproduces the NumPy values either")
            print("  exactly or to about one ulp -- which is the point of code")
            print("  generation: one derivation, three consumers (the paper, the")
            print("  array library, the compiled kernel), and no transcription")
            print("  step between them where a sign can be lost.")
        finally:
            shutil.rmtree(ARTIFACTS, ignore_errors=True)

    # ------------------------------------------------------------------
    section("6. What the generated source is worth")
    # ------------------------------------------------------------------
    print(f"  the symbolic bundle evaluates to {len(bundle)} output values")
    print(f"  naive transcription would repeat {naive_ops} operations")
    print(f"  the cse form needs {cse_ops}, i.e. "
          f"{100 * cse_ops / naive_ops:.1f} % of the naive count")
    print(f"  Part 1's prism closed form is a separate expression and cost "
          f"{int(sp.count_ops(closed_form))} operations; both were built in")
    print(f"  this one session, which is the practical argument for keeping")
    print(f"  the derivation under version control next to the code.")
    print("  Observation: the three artefacts of this lesson -- a verified")
    print("  formula, a NumPy function and a C file -- all come from one")
    print("  expression object. That is the whole argument for symbolic")
    print("  pre-processing: the derivation is done once, and every consumer")
    print("  is generated from it rather than retyped.")


if __name__ == "__main__":
    main()
