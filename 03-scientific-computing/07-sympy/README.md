# Module 03-07 — SymPy and Symbolic Computation

**Stages:** intermediate → graduate · **Prerequisites:**
[03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for the call model, and
[01-01-01 Number Systems, Precision and Scientific Notation](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md)
for exact versus measured numbers, which the first lesson re-derives from the
symbolic side.

Numerical libraries compute with numbers; SymPy computes with expressions. This
module is about what that change buys a geophysicist: derivations that can be
differentiated, checked, printed as LaTeX and turned into fast code without a
transcription step.

Five lessons, in dependency order:

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Symbolic Variables, Expressions and Assumptions](./01-symbolic-basics.md) | intermediate | Exact rationals, assumption sets, and why `sqrt(x**2)` has three answers |
| 02 | [Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md) | intermediate | Gradient, Laplacian, quadrature, limits, and the finite-difference trade measured |
| 03 | [Symbolic Solvers for Algebraic and Differential Equations](./03-solving-equations.md) | advanced | Closed forms, perturbation series, ODE systems and boundary-value problems |
| 04 | [Symbolic Tensors and Index Notation](./04-tensor-symbolic.md) | advanced | Strain, Hooke's law, $J_2$, and where SymPy's tensor module is not a calculator |
| 05 | [Generating Fast Numerical Code from Symbolic Results](./05-code-generation.md) | graduate | One expression, three consumers: NumPy, C, LaTeX |

## What makes this module different from a SymPy tutorial

Three commitments:

- **Every symbolic result is checked against an independent one.** A quadrature
  against `scipy.integrate.quad`, an ODE solution against `solve_ivp`, a tensor
  contraction against `numpy.einsum`, a generated kernel against a compiled C
  binary. The agreements are quoted as numbers.
- **Every verification is exact where it can be.** Where the algebra permits it,
  the check is "this simplifies to 0", not "this is small". The difference between
  those two statements is the difference between a proof and a test.
- **Limits are reported, not hidden.** Lesson 04 records three measured sharp
  edges in `sympy.tensor.tensor`, including a canonicalisation that returns 0 for
  a non-zero contraction, and lesson 05 reports where the float route's error
  distribution sits relative to binary64. Where I could not reconcile a
  measurement with the textbook expectation, the lesson says so and excludes that
  result from its claims.

## Prerequisites in detail

You should be able to write a Python function, import a module, and read a
traceback. Calculus at the level of
[01-05 Single-Variable Calculus](../../01-mathematics/05-single-variable-calculus/README.md)
is assumed from lesson 02 onwards; the elasticity of lesson 04 is developed from
scratch.

## How to run the demos

All five demos run under the project virtual environment, exit 0, and use no
network access:

```bash
.venv/bin/python 03-scientific-computing/07-sympy/code/symbolic_basics_demo.py
.venv/bin/python 03-scientific-computing/07-sympy/code/symbolic_calculus_demo.py
.venv/bin/python 03-scientific-computing/07-sympy/code/solving_equations_demo.py
.venv/bin/python 03-scientific-computing/07-sympy/code/tensor_symbolic_demo.py
.venv/bin/python 03-scientific-computing/07-sympy/code/code_generation_demo.py
```

| Demo | Does | Extra requirements |
|---|---|---|
| `symbolic_basics_demo.py` | assumptions, exact arithmetic, `nsimplify`, precision, `simplify` counts | sympy, mpmath |
| `symbolic_calculus_demo.py` | gradients, Laplacian, shell integration, Ricker extrema, quadrature, limits, flux, series, finite differences | sympy, numpy, scipy |
| `solving_equations_demo.py` | cubic, transcendental, Kepler series, decay chain, damped oscillator, linear system, geotherm | sympy, numpy, scipy |
| `tensor_symbolic_demo.py` | strain and rotation, Hooke's law by contraction, Lamé inversion, $J_2$, `einsum`, spherical Laplacian | sympy, numpy |
| `code_generation_demo.py` | closed form + quadrature check, cse, `lambdify`, 40-digit comparison, C generation and compilation | sympy, numpy, scipy, **a C compiler** (`cc` or `clang`) |

The last demo checks for a C compiler on the PATH and skips that part with a
printed message if neither `cc` nor `clang` is present. It writes its generated C
into a scratch directory under `code/` and deletes the directory before exiting.

No demo quotes a wall-clock time. Where a performance claim is natural, the demos
quote operation counts (`count_ops`), array sizes, Python call counts and byte
sizes instead.

## Materials in this module

| Path | Contents |
|---|---|
| `01-…05-*.md` | The five lessons |
| [`code/`](./code) | Five runnable demonstrations |
| [`exercises/`](./exercises) | Problem sets and solutions, with the measured numbers in the solutions |

## Suggested path

**If you are here to derive something:** lesson 01, then lesson 02, then use
`symbolic_calculus_demo.py` as a template for the verification.

**If you are here to speed up a kernel:** lesson 05, with lesson 04 as needed for
index notation. The measurement discipline (check against an independent route,
quote the difference) is the part that transfers.

**If you are here for elasticity or continuum mechanics:** lesson 04 first, then
[02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md).

## Related modules

- [03-03-scipy](../03-scipy/README.md) — the numerical routines every symbolic
  result in this module is checked against.
- [03-02-numpy](../02-numpy/README.md) — the array library the generated code
  targets.
- [03-06-jupyter-and-notebooks](../06-jupyter-and-notebooks/README.md) — where
  generated LaTeX goes.
- [01-12-numerical-methods](../../01-mathematics/12-numerical-methods/README.md)
  — the theory behind the finite differences and quadratures measured here.
- [02-04-elasticity-and-continuum-mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md)
  — the physics of lessons 04 and 05's worked models.

## Self-assessment checklist

- [ ] I can declare a symbol with exactly the assumptions a derivation uses. (§01)
- [ ] I can state the exact value of $0.1 + 0.2 - 0.3$ as a rational. (§01)
- [ ] I can verify Laplace's equation by simplifying a residual to zero. (§02)
- [ ] I can say why a quadrature falls short on a square-root endpoint. (§02)
- [ ] I can derive a perturbation series and measure its truncation error. (§03)
- [ ] I can contract $C_{ijkl}$ with a strain tensor and check the result. (§04)
- [ ] I can measure a float kernel's error against extended precision. (§05)
- [ ] I can generate, compile and compare a C kernel. (§05)
