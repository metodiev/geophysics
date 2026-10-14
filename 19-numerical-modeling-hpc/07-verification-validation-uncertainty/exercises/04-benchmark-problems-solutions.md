# Solutions — 19-07-04 Standard Benchmark Problems and Community Comparisons

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [04 Benchmark Problems](../04-benchmark-problems.md).

---

## ★1 — Hand check of the fourth-order stencil

At $x = 1$ with $h = 1$ the stencil nodes are $x = -1, 0, 1, 2, 3$ and
$u = x^{4}$ gives $u = 1, 0, 1, 16, 81$:

$$\frac{-1 + 16\times0 - 30\times1 + 16\times16 - 81}{12\times1^{2}}
= \frac{-1 - 30 + 256 - 81}{12} = \frac{144}{12} = 12 .$$

The exact value is $u''(1) = 12x^{2} = 12$: **exact agreement**, with no residual
at all.

**Why it is exact.** The stencil's leading error term is $-h^{4}u^{(6)}/90$ and
every higher term contains $u^{(6)}$ or higher derivatives, so the operator
annihilates every polynomial of degree $\le 5$. Since $x^{4}$ has $u^{(6)} = 0$,
the discrete operator returns $u''$ exactly, whatever the position of the window
relative to the evaluation point — which is why this is a good *unit test* for the
stencil coefficients and a poor test of anything else (an error in the boundary
handling, for instance, is invisible on a polynomial that the interior stencil
reproduces exactly).

This is the arithmetic counterpart of the measured orders $3.95$, $3.99$, $4.00$
in the lesson: the derivation predicts exactness on $x^{4}$ and order $4$ on a
non-polynomial.

---

## ★2 — Observed order

$$p = \frac{\ln(1.20\times10^{-2}/3.00\times10^{-3})}{\ln 2}
= \frac{\ln 4}{\ln 2} = 2, \qquad \text{and the next pair gives } 2 \text{ again.}$$

The method is **second order** for this problem. The fourth-order stencil of ★1
would give a ratio of $16$ per doubling, i.e. errors falling as $2^{-4}$. A ratio
of exactly $4$ is the signature of order $2$ and cannot be reconciled with order
$4$ by any smooth coefficient choice.

---

## ★3 — The weight in the norm

$h\sum_i e_i^{2} \to \int e^{2}\,\mathrm{d}x$ as $h \to 0$, so
$\sqrt{h\sum_i e_i^{2}}$ approximates the continuous $L^{2}$ norm and is
independent of the number of points. Without the weight, the raw sum
$\sqrt{\sum_i e_i^{2}}$ grows as $N^{1/2}$ for a fixed per-point error, so two
methods compared at different $N$ differ by the $\sqrt{N}$ ratio whatever their
accuracy: a $400$-cell solution would look $\sqrt{2}$ times worse than a
$200$-cell solution even if both were exact. A refinement study without the weight
reports an apparent order $p + 1/2$ if written with the raw sum, or $p - 1/2$ if
the division by $N$ is mishandled. State the norm in full, including the weight.

---

## ★4 — A source with a non-zero mean

$$\sum_{i=0}^{N-1} f_i = \sum_i 1 + \sum_i \sin(2\pi x_i) = N + 0 = N \neq 0 .$$

The periodic second-difference matrix has the constant vector in its null space,
so solvability requires $f$ orthogonal to constants, i.e. $\sum_i f_i = 0$. Since
$\sum_i f_i = N$, the discrete system is inconsistent: there is no periodic $u$
with $L_h u = f$. A solver that returns an answer has silently changed the
problem (for example by subtracting the mean of $f$).

**Two changes that make it well posed:** (i) add the compatibility condition to the
problem statement by choosing a source with zero mean, for example
$f = \sin(2\pi x)$; or (ii) specify that the equation is to be solved *projected*
onto the zero-mean subspace, i.e. $L_h u = f - \bar{f}$, with $\bar{f} =
\frac{1}{N}\sum f_i$, and state that this is what is meant.

---

## ★5 — A missing gauge

Each code solves $L_h u = f$ correctly but returns
$u_1 = \sin(2\pi x)$ and $u_2 = \sin(2\pi x) + 0.5$. With the stated exact solution
$\sin(2\pi x)$:

$$\lVert u_1 - u_{\text{exact}}\rVert = 0, \qquad
\lVert u_2 - u_{\text{exact}}\rVert = 0.5 .$$

Both codes are right; the *errors* differ by $0.5$, and that number is entirely an
artefact of the gauge. What the specification is missing is the line "the mean of
$u$ is zero" (equivalently "the $k = 0$ Fourier mode of $u$ is fixed to zero"), and
without it neither reported error meaningfully describes either code. Note also
that the two codes' fields differ by a constant, so a comparison of *gradients* or
of any functional that annihilates constants is unaffected; that is the sense in
which the ambiguity is harmless and the sense in which it is fatal to an error
metric.

---

## ★6 — A specification with a piecewise-constant coefficient

> 1-D steady diffusion benchmark. Equation:
> $-\dfrac{\mathrm{d}}{\mathrm{d}x}\left(k(x)\dfrac{\mathrm{d}u}{\mathrm{d}x}\right)
> = f(x)$ on $(0,1)$, with $u(0) = 0$, $u(1) = 0$. Coefficient:
> $k = 2$ for $x < 0.5$ and $k = 1$ for $x > 0.5$, with the interface at $x = 0.5$.
> Interface conditions: $u$ continuous and $k\,\mathrm{d}u/\mathrm{d}x$ continuous.
> Source: $f(x) = 1$ everywhere. Exact solution: obtained by solving the two
> constant-coefficient problems and matching at the interface. Gauge: not needed
> (the operator has no null space with these Dirichlet data). Source
> discretisation: cell averaged. Interface treatment: the grid contains a node
> exactly at $x = 0.5$, and $k$ is taken as the harmonic mean across a face and the
> arithmetic mean at a node; state which. Norm: discrete $L^{2}$,
> $\sqrt{h\sum_i e_i^{2}}$, over all nodes. Grid sequence: $N = 32, 64, 128, 256$
> with the interface aligned on a node. Solver: direct, no tolerance.

**The choice a competing code is most likely to make differently** is the interface
treatment: harmonic face averages (which give the correct flux continuity and
second-order accuracy), arithmetic averages (which degrade to first order), or a
staggered grid where $k$ lives on faces and $u$ at nodes. The measured difference
between these is a *first-order* error term, so the two codes will differ by the
same order as their error — the situation §5.2 of the lesson quantifies for a
simpler case.

---

## ★7 — Detecting a second-order boundary treatment in a fourth-order code

**Expected order.** With a fourth-order interior and a second-order boundary
condition, the error is $O(h^{4})$ in all but a fixed number of boundary nodes
where it is $O(h^{2})$. As in the lesson's exercise for the first-order case, the
discrete $L^{2}$ norm is then
$\sqrt{h(m h^{4} + N h^{8})} = O(h^{3.5})$: the *observed order is about 3.5*, not
$4$ and not $2$. That fractional order is the signature.

**Grid sequence.** $N = 32, 64, 128, 256, 512$ with $r = 2$, and the observed order
reported **per triple** (values around $3.5$ that slowly drift toward $4$ as the
higher-order term loses weight).

**Diagnostic.** Plot $\log|e_i|$ against node index for two resolutions. A genuine
fourth-order code shows a uniformly falling interior error and a boundary region
whose error is *smaller* than the interior's; the defective code shows a wedge at
each boundary whose amplitude falls by a factor of $4$ per doubling while the
interior falls by $16$, so the ratio of the boundary error to the interior error
*grows* by $4$ each refinement. Equivalently: compute the error restricted to the
interior (excluding the boundary layers) and to the boundary nodes separately; the
interior order will read $4$ and the boundary order $2$. That separation is the
statement the specification should ask for, because the single global order
$3.5$ is otherwise easy to misread as "not yet asymptotic".

---

## ★8 — Review of an unusable table

**Unstated assumptions, one per row.**

1. **No problem statement.** Which equation, which domain, which boundary
   conditions? A spectral method is only applicable to some of them (Section 5.4
   of the lesson measures an $O(1)$ failure when it is applied to the wrong class).
2. **No norm.** $L^{2}$, RMS, $L^{\infty}$, at nodes, interior only? The three
   differ by orders of magnitude and the ranking can reverse.
3. **Resolution is not comparable.** "200 cells", "32$^{2}$ modes" and "400 cells"
   measure three different things: for the spectral method the resolution is the
   number of modes retained, and its *effective* resolution on a grid is not
   $32^{2}$.
4. **Run time without hardware, language, tolerance or thread count.** The
   differences between rows (1.1 s and 1.2 s) are smaller than the difference a
   change of machine, compiler flags or BLAS library would produce.
5. **Method C is anomalous.** Its error is *larger* at 400 cells
   ($4\times10^{-3}$) than method A's at 200 cells ($3\times10^{-3}$) while costing
   twice the time: either a different norm or a different problem was used, or C is
   not converging. Either way the row cannot be used as a data point.
6. **No tolerances or reference values stated**, so none of the errors can be
   checked.
7. **No refinement study**, so no order is available for any method and the numbers
   cannot be extrapolated to a target accuracy.

**Rewritten form that would support the conclusion.**

> Problem: [state equation, domain, boundary conditions, gauge, source
> discretisation]. Exact solution: [state it]. Norm: [state it]. Target tolerance:
> $10^{-4}$ RMS. For each method report (i) the resolution needed to reach the
> target, found by a refinement study with $r = 2$ using the stated norm,
> (ii) the observed order from that study, (iii) the cost metric — number of
> unknowns and non-zeros, plus wall time on a named machine with a named build and
> a stated solver tolerance, and (iv) the applicability statement: the assumed
> smoothness and boundary conditions. Then the comparison is: method B reaches the
> target at $N = 32$ with observed order [measured], method A needs $N = [\ldots]$
> with order $2$, and method C is excluded because [reason]. Under those stated
> conditions, B is preferable for this problem class; the conclusion does not
> transfer to a non-periodic or non-smooth problem without a new benchmark.
