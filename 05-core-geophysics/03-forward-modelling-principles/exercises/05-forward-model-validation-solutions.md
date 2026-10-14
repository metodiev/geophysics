# Solutions — 05-03-05 Validating Forward Codes Against Analytic Benchmarks

> Numbers marked *verified* were computed.

---

## ★1

Verification: are we solving the equations right (code versus mathematics)?
Validation: are we solving the right equations (mathematics versus the Earth)?
Verification is achievable with benchmarks; validation requires data.

---

## ★2

A closed form; an exact non-obvious identity; a limiting case; a manufactured
solution; a symmetry property; a conservation or invariance property.

---

## ★3

A test that cannot fail provides no evidence. Demonstrate by injecting a known
error — e.g. multiply the kernel by 1.02 — and confirming the test reports a
relative error of $2.000\times10^{-2}$ against a $10^{-6}$ tolerance, which it
does in the module demonstration.

---

## ★★4

Reference: the closed-form dipole field with moment $\mathbf{M}V$ (an
independent derivation). Test quantity: the relative difference in
$|\mathbf{B}|$ at a stated distance. Tolerance: set above the round-off floor,
e.g. $10^{-10}$ (the shell theorem is exact, so the only error is numerical).
Grid: a Gauss–Legendre grid in $(r,\cos\theta,\phi)$ inside the sphere, with
enough nodes that doubling them changes the answer by less than the tolerance.
Measured in the demonstration with a $30\times40\times40$ grid: relative
differences of $1.5\times10^{-14}$, $1.0\times10^{-15}$ and $5.1\times10^{-15}$
at 250, 400 and 1000 m.

---

## ★★5

It is a **modelling** difference: the prism is not a point dipole, and the
leading non-dipole term is the octupole on the symmetry axis. The experiment
that decides is grid refinement: refine the quadrature (or subdivide the prism)
and re-measure. If the discrepancy is unchanged, it is modelling; if it falls at
the scheme's order, it is discretisation. The demonstration's quadrature
converges to $<10^{-14}$ relative, so the residual $1.29\times10^{-1}$ at 200 m
cannot be numerical.

---

## ★★6

Double precision has relative resolution $\approx2.2\times10^{-16}$ and a
floating-point sum of $n$ terms accumulates error at least of order
$\sqrt{n}\,\epsilon$. A tolerance of $10^{-18}$ is below the representable
resolution and therefore unachievable by any implementation; the test would fail
even for a perfect code. Defensible: $10^{-12}$ to $10^{-14}$ for a
well-conditioned comparison of a few thousand operations, stated with the
number of operations. For a long summation (e.g. $10^{6}$ terms) even
$10^{-13}$ may be optimistic.

---

## ★★★7

Expected mapping:

| bug | caught by |
|---|---|
| wrong kernel prefactor (e.g. 2×) | (a), (b) |
| wrong sign in the $z$ term | (a), (c) |
| wrong quadrature weights | (a) |
| wrong node count handling | (a) |
| inconsistent stencil coefficient | (d) |
| boundary conditions mishandled | (d) |
| transposed coordinates ($x$ and $y$ swapped) | (c) only, and only if the body is asymmetric |
| a wrong *physical* assumption (e.g. ignoring a layer) | nothing in this suite |

The last row is the honest limitation: benchmark suites test the *implementation*
of the stated equations. They cannot detect that the stated equations are wrong
for the problem.

---

## ★★★8

A complete report states the equations and the discretisation, lists each
benchmark with its reference and tolerance, gives the measured numbers, and then
— crucially — states the limitations. Two things a code could still be wrong
about despite passing every benchmark: (i) the *validity of the physics* for the
target (e.g. an isotropic elastic assumption in a strongly anisotropic
formation); (ii) *units or coordinates* in the interface with other tools, which
is why a benchmark with realistic magnitudes and a non-trivial observation
position is worth including. A suite that only tests a body at the origin with
unit parameters would miss both.
