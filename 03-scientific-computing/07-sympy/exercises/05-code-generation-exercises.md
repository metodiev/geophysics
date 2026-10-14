# Exercises — 03-07-05 Generating Fast Numerical Code from Symbolic Results

> Solutions are in
> [`05-code-generation-solutions.md`](./05-code-generation-solutions.md).

---

## ★ Foundational

**★1.** Convert to a NumPy callable and state whether the result is array-capable:
(a) $\sin(kx)$, (b) $\mathrm{erfc}(x)$, (c) $\Gamma(x)$.

**★2.** Explain the difference between `lambdify(..., "math")` and
`lambdify(..., "numpy")` for a 10 000-point evaluation, in terms of call counts.

**★3.** Apply `cse` by hand to $ax^2 + bx + c$ together with its derivative and
state the temporaries.

**★4.** Why must a C generator order its temporaries by dependency?

**★5.** State what `count_ops` counts and what it does not.

---

## ★★ Applied

**★★6.** Derive the vertical gravity of a horizontal line mass (2-D, infinite
strike) symbolically from the point-mass kernel, verify it against a numerical
integral, and report the relative difference at three offsets.

**★★7.** Take an expression you use routinely, apply `cse`, and report the
operation counts before and after, the number of temporaries, and the percentage
reduction.

**★★8.** Generate C for a formula of your choice, compile it, and compare its
output with NumPy at 20 points. Report the worst relative difference and the
compile exit code.

**★★9.** Measure the float-versus-extended-precision error distribution for a
formula with cancellation (for example $\ln(1+x)$ at small $x$). Report the worst
relative error over 100 points and the $x$ at which it occurs.

**★★10.** Verify the lesson's prism closed form at three offsets of your choosing
by comparing with `scipy.integrate.dblquad`, and report the relative differences
and the tolerance you requested.

---

## ★★★ Research-oriented

**★★★11.** Build a complete generated-kernel pipeline for a closed-form
geophysical forward model: the symbolic derivation with verification, a NumPy
callable checked against an independent integral, a compiled C kernel compared at
50 points, and a `pytest` module asserting the agreement. Report every measured
difference and the number of generated versus hand-written lines.

**★★★12.** Assess `cse` on real expressions. Take five expressions of increasing
structural complexity, measure the operation-count reduction, and report whether
the reduction correlates with (i) the operation count before, (ii) the number of
distinct subexpressions of size two or more, or (iii) neither. State the limits of
a five-expression study.
