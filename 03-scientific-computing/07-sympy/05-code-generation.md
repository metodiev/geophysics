---
id: 03-07-05
title: "Generating Fast Numerical Code from Symbolic Results"
level: graduate
prereqs: ["03-07-02", "03-07-04", "03-06-04"]
estimated_minutes: 120
tags: [sympy, code-generation, lambdify, cse, ccode, performance]
---

# Generating Fast Numerical Code from Symbolic Results

A derivation is useful once. A derivation turned into code is useful every time
someone runs the code. The step between them — transcription from paper to
Python to C — is where a sign is dropped, a factor of 2 is lost, and a unit
conversion goes missing, because there is no machine check on a copyist.

Symbolic computation removes the copyist. This lesson takes one expression,
derives it, verifies it, and then generates **three** consumers from it: a NumPy
function, a compiled C kernel, and the LaTeX in a report. All three come from one
object, so all three agree by construction.

The lesson is also about measurement. Every claim about accuracy, speed of
execution in the sense of operation counts, and agreement between the routes is a
number produced by the demonstration:

```bash
.venv/bin/python 03-scientific-computing/07-sympy/code/code_generation_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** a closed form by hand, **verify** it symbolically by
   differentiation, and **check** it against numerical quadrature of the original
   integral, quoting the relative difference.
2. **Measure** what common-subexpression elimination removes from an expression
   bundle, in operations and in temporaries.
3. **Generate** a NumPy function with `lambdify` and **count** the Python calls
   the vectorised and scalar routes need.
4. **Assess** a float64 evaluation against 40-digit arithmetic over a sample, and
   **state** what the comparison does and does not establish.
5. **Generate** C from the same expression, compile it, run it, and **compare**
   its values with NumPy.
6. **Decide** which of the three artefacts a given deliverable needs.

## Prerequisites

- [03-07-02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
- [03-07-04 Symbolic Tensors and Index Notation](./04-tensor-symbolic.md)
- [03-06-04 Converting Notebooks to Scripts, Tests and Reports](../06-jupyter-and-notebooks/04-notebooks-to-scripts.md)
  — the same "one source, several consumers" argument, for documents.

## 1. Intuition: the derivation should be the source, not the input to a translation

A numerical kernel is a transcription. Someone reads a formula and writes code;
the code is then the only thing that runs, and its agreement with the formula
rests on the transcription being right. Nothing in the workflow detects the case
where both are wrong in the same way.

Generating the kernel from the expression object removes the transcription step:

$$\text{derivation} \;\longrightarrow\; \text{expression}
\;\longrightarrow\; \begin{cases}\text{NumPy function}\\ \text{C source}\\
\text{LaTeX}\end{cases}$$

Each arrow is mechanical, and the first one is the only one that involves
judgement. The consequence is that a change to the derivation propagates to every
consumer when the generator is re-run, and a mistake in the derivation appears in
all of them at once instead of in one of them silently.

## 2. Precise definitions

**`lambdify`.** Converts a SymPy expression into a Python callable, with a chosen
numerical backend: `"numpy"` for arrays, `"math"` for scalars, `"scipy"` for
SciPy functions.

**`cse`.** Common subexpression elimination: returns a list of temporary
assignments and a reduced expression.

**`count_ops`.** The number of operations in an expression tree, as SymPy counts
them.

**`ccode` / `fortran`.** Printers that emit C or Fortran source for an
expression. SymPy also has a full `codegen` module for typed routines; this
lesson uses the printer plus a small amount of glue.

**Verification of a generated kernel.** Agreement between the kernel and an
independent numerical route, quoted as a maximum absolute or relative
difference.

## 3. Derivation: a closed form for the 2-D prism, verified three ways

### 3.1 The integral and the proposed antiderivatives

A 2-D body of infinite strike has vertical gravity

$$g_z(x,z) = 2G\rho\iint \frac{z-\zeta}{(x-\xi)^2 + (z-\zeta)^2}\,
d\zeta\, d\xi,$$

integrated over the body's cross-section. Two antiderivatives do the whole job,
and the demonstration verifies both by differentiation:

```
  integrand d(zeta):  (z - zeta) / ((x - xi)^2 + (z - zeta)^2)
  proposed antiderivative: -log((x - xi)**2 + (z - zeta)**2)/2
  d/dzeta of it minus the integrand simplifies to 0
  the inner integral leaves a factor of 1/2, so the second step
  needs the antiderivative of (1/2) ln(u^2 + h^2), u = xi - x
  proposed: sqrt(h_sq)*atan((-x + xi)/sqrt(h_sq)) + x - xi + (-x + xi)*log(h_sq + (-x + xi)**2)/2
  d/dxi of it minus (1/2) ln(u^2 + h^2) simplifies to 0
```

Both residuals are **exactly zero**, which is what makes the closed form
trustworthy before any integral is evaluated. The verifications are the answer to
"how do you know the antiderivative is right?" — you differentiate it.

Note the factor of $\frac12$ in the second step, flagged in the demonstration's
own output. It comes from the first antiderivative. Getting it wrong would scale
the anomaly by a factor of two, which a single numerical comparison would catch
but a hurried derivation would not.

### 3.2 The closed form and its numerical check

Assembling the antiderivatives gives

$$g_z = G\rho\left[F(x_2,z_1) - F(x_1,z_1) - F(x_2,z_2) + F(x_1,z_2)\right],$$

a sum over the four corners of the prism, with $F$ built from the two verified
antiderivatives (81 operations, as counted by `count_ops`). Checked against
numerical quadrature of the original double integral:

```
  prism: x in [-2000, 2000] m, depth z in [200, 1200] m, rho = 2670 kg/m^3
      x =       0 m: closed form -44.186027660 mGal, dblquad -44.186027660 mGal, relative difference 1.35e-15
      x =    1500 m: closed form -36.549373953 mGal, dblquad -36.549373953 mGal, relative difference 2.97e-16
      x =    5000 m: closed form -2.277684886 mGal, dblquad -2.277684886 mGal, relative difference 3.08e-14
```

Three geometries, three agreements at or below $3\times10^{-14}$ relative — the
level of `dblquad`'s requested tolerance, not the closed form's accuracy. **This is
the pattern to keep: the new method is verified against an independent one, and
the agreement is quoted as the tolerance of the weaker method.**

The values themselves are a useful sanity check: a 4 km wide prism extending from
200 m to 1200 m depth, with a 2670 kg/m³ density contrast, produces about −44 mGal
directly above it and −2.3 mGal 5 km away. An order-of-magnitude estimate from
$g \approx 2G\rho A/z$ puts the amplitude in the tens of mGal, which is consistent.

## 4. What common-subexpression elimination removes, measured

For the multipole bundle

$$W = M r^4 - d_i X_i r^2 + \tfrac12 Q_{ij}X_iX_j, \qquad r^2 = X^2+Y^2+Z^2,$$

together with its three partial derivatives and with numeric moments substituted,
the demonstration measures:

```
  naive operation count           : 167
  cse temporaries introduced      : 22
  operation count after cse       : 122
  reduction                       : 26.9 %
      x0 = 20000000000.0*Y
      x1 = 30000000000.0*Z
      x2 = 60000000000.0*Z
      x3 = X**2
      x4 = X**3
      x5 = Y**2
      ... and 16 more
```

The temporaries are the expected ones: the shared powers $X^2$, $X^3$, and the
products of the moments with the coordinates. A reduction of 26.9 % in operation
count is real and modest — cse is not a compiler, and an expression with little
repeated structure gains little. **The measured reduction depends on the
expression**, so the honest statement is the number, not a general claim.

## 5. `lambdify`: vectorisation and the call count

```
  grid: 1000000 points ((100, 100, 100) array)
  Python calls to the lambdified function: 1 (whole array at once)
  Python calls a scalar 'math' module lambdify would need: 1000000
  max |lambdified - hand-written NumPy difference| = 2.577e+10
  largest value in the array                       = 5.374800e+25
  relative difference                              = 4.795e-16
```

Two things to read out of that. First, the **call count**: a `"numpy"` lambda
called with arrays performs one Python-level call and does the rest in compiled
code; the scalar route needs one Python call per point — a million of them. That
is the quantitative version of "vectorise it", and it is why the scalar route is
reserved for code that evaluates a few hundred points.

Second, the **agreement**: $4.8\times10^{-16}$ relative against a hand-written
NumPy implementation. The two are the same arithmetic in a different order, so
they differ in the last bits and not more. **A symbolic derivation does not make a
float computation exact; it makes the expression you compute the one you meant.**

## 6. How far the float route is from the truth

```
  200 probe points in [-2, 2]^3, evaluated twice:
  binary64 via lambdify, and 40-digit via SymPy evalf
  probes where the two agree to the last bit: 93 of 200
  worst relative difference: 4.136e-16 at X, Y, Z = (-1.708996, -0.775482, +0.455876)
      high precision 8.308179437277349e+25, float64 8.308179437277353e+25
  that is 1.86 ulp of binary64 (eps = 2.220e-16)
```

At 93 of 200 probes the float64 result is *bit-identical* to the 40-digit
reference rounded to binary64; the worst case is 1.86 ulp. This is the correct
way to assess a float kernel: **evaluate at a sample of points against extended
precision and report the distribution of the error**, not a single difference.

It also sets the expectation for tests. Testing this function with a tolerance of
$10^{-15}$ relative would fail on 107 of 200 points; a tolerance of $10^{-14}$
would pass everywhere with room. Choose the tolerance from the measurement.

## 7. Generating C, compiling it, and comparing

The demonstration emits C from the cse form, ordering the temporaries by
dependency (the generator raises if it cannot order them), compiles with `cc -O2`,
and runs:

```
  generated 22 temporaries and 4 outputs
  wrote generated_multipole.c: 105 lines, 5774 characters
  'cc -O2' exit code: 0
  compiled binary size: 33440 bytes
      probe 0 W       C +6.753254412320e+24   NumPy +6.753254412320e+24   relative 0.00e+00
      ...
      probe 1 dW_dZ   C +5.270290000000e+24   NumPy +5.270290000000e+24   relative 2.04e-16
  bit-identical at 9 of 12 (probe, output) pairs; worst relative difference 2.04e-16
```

Nine of twelve values match bit for bit; the worst disagreement is 2.04e-16.
The compiler reorders the arithmetic at `-O2`, so this is the same agreement
pattern as between two float routes: last bits, not more.

The C code is 105 lines for a 4-output expression, which is what "generated
code" looks like: verbose, mechanical, and not written by a human. It is also the
artefact that can be dropped into a solver, wrapped in a Python extension, or
compiled for a GPU — see
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).

## 8. What the three artefacts are for

| Artefact | Strength | Use |
|---|---|---|
| SymPy expression | exact, differentiable, printable | the derivation; LaTeX for a paper |
| `lambdify("numpy")` | array-level speed with no build step | analysis, inversion loops |
| Generated C | compiled speed, no Python in the loop | kernels for large grids or time stepping |

And the fourth, which this lesson does not demonstrate but the discipline implies:
**one test that checks all three against each other**. If the C kernel and the
NumPy function agree at 200 sample points to $10^{-15}$, then a disagreement
between a survey result and a synthetic test is a physics question, not a
transcription question.

## 9. Assumptions and limitations

- **`cse` finds syntactic common subexpressions**, not algebraic ones. It will not
  discover that $\sin^2 + \cos^2 = 1$; use `trigsimp` before `cse` if that matters.
- **Generated C is not optimised C.** The compiler optimises what it is given; the
  generator does not restructure the arithmetic to suit a particular CPU.
- **`ccode` prints `pow(x, 2)` or `x*x` depending on the expression** and does not
  choose between them for accuracy or speed. Inspect the output before shipping.
- **The comparison is at 12 points, not a proof.** A kernel verified at 12 points
  can still fail in a corner of parameter space; choose the probe points from the
  parameter ranges the kernel will actually see.
- **`lambdify("numpy")` uses NumPy functions**, so `erfc` maps to
  `scipy.special.erfc` only when the SciPy module list is given; otherwise it maps
  to whatever NumPy provides. Check the generated source for the functions you
  care about.
- **No timings are quoted.** The lesson quotes operation counts, array sizes,
  call counts and byte sizes. Wall-clock comparisons between a Python route and a
  C route are machine-dependent and would be dishonest to generalise.

## 10. Worked examples

### 10.1 The number a paper prints and the number the code computes

The prism closed form evaluates to $-44.186027660$ mGal at $x = 0$. In a paper
you would print −44.19 mGal (four significant figures, supported by a 2670 kg/m³
density known to four figures) and −2.28 mGal at $x = 5$ km. The generated
kernel prints twelve digits; **the significant figures come from the input
uncertainties, not from the kernel's output precision.** That is the same
principle as in
[01-01-01](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md),
and the symbolic route makes it easy to violate, because it will happily give you
50 digits.

### 10.2 A cse-ordered C generator

The ordering problem is real and worth stating: `cse` returns temporaries in an
order that is not guaranteed to be evaluable top to bottom, and a generator that
ignores this emits C that does not compile. The demonstration's solution is
simple and explicit:

```python
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
```

The `raise` is the important line: it turns a silent ordering bug into a failed
build.

### 10.3 Which route for which problem

For a survey of 10 000 stations and a prism model with 50 bodies, the anomaly is
$5\times10^5$ evaluations of a 81-operation expression — trivial for NumPy, and
the development cost of a C kernel is not repaid. For a 3-D finite-difference
simulation with $10^8$ cells and $10^4$ time steps, the kernel runs $10^{12}$
times, and the C route is the only one. **The decision is arithmetic on the
number of evaluations, and the derivation is shared either way.**

## 11. Python demonstration

`code/code_generation_demo.py` runs in six parts:

| Part | Result | Key measured output |
|---|---|---|
| 1 | Closed form by hand | two residuals `0`; `1.35e-15`, `2.97e-16`, `3.08e-14` against `dblquad` |
| 2 | cse | 167 → 122 operations, 22 temporaries, 26.9 % |
| 3 | `lambdify` | 1 call vs $10^6$; `4.795e-16` relative |
| 4 | Float against 40 digits | 93 of 200 bit-identical; worst 1.86 ulp |
| 5 | C generation and compile | 105 lines, `cc -O2` exit 0, 9 of 12 bit-identical |
| 6 | Summary | 73.1 % of the naive operation count |

Part 5 needs a C compiler; the script checks for `cc` or `clang` on the PATH and
skips the part with a printed message if neither is present. All generated files
are written to a scratch directory that is deleted before the script exits.

## 12. Exercises

Solutions are in
[`exercises/05-code-generation-solutions.md`](./exercises/05-code-generation-solutions.md).

### ★ Foundational

**★1.** Convert to a NumPy callable and state whether the result is
array-capable: (a) $\sin(kx)$, (b) $\mathrm{erfc}(x)$, (c) $\Gamma(x)$.

**★2.** Explain the difference between `lambdify(..., "math")` and
`lambdify(..., "numpy")` for a 10 000-point evaluation, in terms of call counts.

**★3.** Apply `cse` by hand to $ax^2 + bx + c$ together with its derivative and
state the temporaries.

**★4.** Why must the C generator order its temporaries by dependency?

### ★★ Applied

**★★5.** Derive the vertical gravity of a horizontal *line* mass (2-D,
infinite strike) symbolically from the point-mass kernel, verify it against a
numerical integral, and report the relative difference at three offsets.

**★★6.** Take an expression you use routinely, apply `cse`, and report the
operation counts before and after, the number of temporaries, and the reduction
as a percentage. State whether the reduction was worth the loss of readability.

**★★7.** Generate C for a formula of your choice, compile it, and compare its
output with NumPy at 20 points. Report the worst relative difference and the
compile exit code.

**★★8.** Measure the float-versus-extended-precision error distribution for a
formula with cancellation (for example $\ln(1+x)$ at small $x$). Report the worst
relative error over 100 points and the value of $x$ at which it occurs.

### ★★★ Research-oriented

**★★★9.** Build a complete generated kernel pipeline. Choose a geophysical
forward model with a closed form (a prism, a line mass, a magnetic dipole, or a
gravity gradient tensor component), and produce: (a) the symbolic derivation with
its verification, (b) a NumPy callable checked against an independent numerical
integration, (c) a C kernel compiled and compared at 50 points, and (d) a
`pytest` module asserting the agreement. Report every measured difference and the
total number of lines of generated versus hand-written code.

**★★★10.** Assess `cse` on real expressions. Take five expressions of increasing
structural complexity from your own work, measure the operation-count reduction
from `cse`, and report whether the reduction correlates with (i) the operation
count before, (ii) the number of distinct subexpressions of size two or more, or
(iii) neither. State your finding with the numbers and note the limits of a
five-expression study.

## 13. Common mistakes

1. **Hand-transcribing a formula you already have symbolically.** The copyist is
   the error.
2. **Assuming `cse` gives a large reduction.** Measure it.
3. **Emitting C without ordering temporaries.** It will not compile.
4. **Comparing a generated kernel with itself.** Use an independent route.
5. **Quoting wall-clock speed-ups from one machine.** Quote call counts and
   operation counts.
6. **Choosing a test tolerance without measuring the error distribution.**
7. **Forgetting that `lambdify` chooses the backend's functions.** Read the
   generated source.
8. **Believing the generated code is the derivation.** It is one consumer of it;
   keep the expression under version control too.

## 14. Real-world applications

- **Potential-field modelling.** Prism and polygon formulas are derived once and
  generated into the kernel a survey-processing package uses.
- **Seismic wavelets and source functions.** Analytic source terms, generated,
  mean a change of wavelet is a re-run rather than a re-implementation.
- **Finite-difference and finite-element solvers.** Constitutive updates generated
  from index notation, as in
  [03-07-04](./04-tensor-symbolic.md).
- **Inversion Jacobians.** Differentiating a forward model symbolically gives the
  Jacobian exactly, removing a finite-difference step from the inversion.
- **Publication.** The same expression prints its own LaTeX, so the equation in
  the paper and the equation in the code are the same equation.

## 15. Further reading

- **SymPy documentation** (sympy.org). Level: advanced. The `lambdify`,
  `codegen`, `utilities.lambdify` and `printing` pages, including the module-list
  argument that selects the numerical backend.
- **NumPy documentation** (numpy.org). Level: intermediate. Vectorised
  operations and `einsum`, the target of the generated NumPy code.
- **SciPy documentation** (scipy.org). Level: intermediate. `scipy.integrate`
  (`dblquad`), used here as the independent verification route.
- **Numba documentation** (numba.pydata.org, cited through the numerical
  modelling module). Level: advanced. An alternative route to compiled speed that
  does not require generating C.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms* (2nd
  ed.). SIAM.** Chapter 3. Level: advanced. Why reordering a sum changes its last
  bits, which is what the agreement numbers in Sections 5 and 7 are measuring.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 16. Related lessons

- [03-07-01 Symbolic Variables, Expressions and Assumptions](./01-symbolic-basics.md)
- [03-07-02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
- [03-07-03 Symbolic Solvers for Algebraic and Differential Equations](./03-solving-equations.md)
- [03-07-04 Symbolic Tensors and Index Notation](./04-tensor-symbolic.md)
- [03-03-02 scipy.integrate](../03-scipy/02-integrate.md) — the quadrature used as
  the independent check.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — where a
  generated kernel goes next.

## 17. Self-assessment checklist

- [ ] I can verify an antiderivative by differentiating it, exactly. (§3.1)
- [ ] I can check a closed form against quadrature and quote the difference. (§3.2)
- [ ] I can measure the operation-count reduction `cse` gives. (§4)
- [ ] I can state the call-count difference between the vectorised and scalar
      routes. (§5)
- [ ] I can quantify a float kernel's error against extended precision. (§6)
- [ ] I can generate, compile and compare a C kernel. (§7)
- [ ] I can decide between the NumPy and C routes from an evaluation count. (§10.3)
- [ ] I can say what makes a generated kernel trustworthy. (§8)
