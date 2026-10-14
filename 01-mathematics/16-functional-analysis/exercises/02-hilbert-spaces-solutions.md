# Solutions — 01-16-02 Hilbert Spaces and Orthogonal Expansions

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked "computed for these solutions"
> come from the direct calculation shown.

---

## ★1 — The parallelogram law

**Statement and proof.**

$$\lVert f+g\rVert^2 = \langle f+g,f+g\rangle = \lVert f\rVert^2 +
2\langle f,g\rangle + \lVert g\rVert^2$$

$$\lVert f-g\rVert^2 = \lVert f\rVert^2 - 2\langle f,g\rangle + \lVert g\rVert^2$$

Adding cancels the cross terms:

$$\lVert f+g\rVert^2 + \lVert f-g\rVert^2 = 2\lVert f\rVert^2 + 2\lVert g\rVert^2 .$$

**Evaluation with $f = g = 1$ on $[0,1]$.** In $L^2$:
$\lVert f+g\rVert^2 = \lVert 2\rVert^2 = 4$, $\lVert f-g\rVert^2 = 0$,
$2\lVert f\rVert^2 + 2\lVert g\rVert^2 = 4$; the law holds. In $L^1$:
$\lVert f+g\rVert_1^2 = 2^2 = 4$, $\lVert f-g\rVert_1^2 = 0$, and the right side
is $2\cdot1^2 + 2\cdot1^2 = 4$ — also equal! The law holds here too, which is why
this particular pair is a poor counterexample: with $f = g$ the parallelogram law
reduces to an identity in any normed space.

**A pair that does fail in $L^1$.** Take $f(x) = \mathbf{1}_{[0,1/2]}$ and
$g(x) = \mathbf{1}_{[1/2,1]}$ (disjoint supports of measure $\tfrac12$ each).
Then $\lVert f\rVert_1 = \lVert g\rVert_1 = \tfrac12$,
$\lVert f+g\rVert_1 = 1$, $\lVert f-g\rVert_1 = 1$. The left side is
$1^2 + 1^2 = 2$, the right side is $2\cdot\tfrac14 + 2\cdot\tfrac14 = 1$. So
$2 \neq 1$ and the law fails. The general lesson is that the parallelogram law
characterises inner-product norms, and the failure above is the geometric reason
$L^1$ has no orthogonal projection: its unit ball has "corners" in the directions
that matter.

---

## ★2 — The sine basis and the expansion of $x$

**Orthonormality.**
$\int_0^1 2\sin(m\pi x)\sin(n\pi x)\,dx = \int_0^1[\cos((m-n)\pi x) -
\cos((m+n)\pi x)]\,dx$, which is $1$ for $m = n$ (the first term integrates to 1
and the second to 0) and $0$ for $m \ne n$ (both terms integrate to zero since
$m \pm n$ is a nonzero integer).

**Coefficients of $f(x) = x$.**

$$c_n = \sqrt2\int_0^1 x\sin(n\pi x)\,dx
= \sqrt2\left[-\frac{x\cos(n\pi x)}{n\pi} + \frac{\sin(n\pi x)}{n^2\pi^2}\right]_0^1
= -\frac{\sqrt2\cos(n\pi)}{n\pi} = \frac{\sqrt2\,(-1)^{n+1}}{n\pi}.$$

Numerically $c_1 = \sqrt2/\pi = 0.4501582$, $c_2 = -\sqrt2/(2\pi) = -0.2250791$,
$c_3 = +\sqrt2/(3\pi) = 0.1500527$.

**Asymptotics.** $\lvert c_n\rvert = \sqrt2/(n\pi) = O(1/n)$, and
$\sum_n c_n^2 = \lVert x\rVert_2^2 = 1/3$ exactly (Parseval), since
$\sum_{n\ge1}2/(n^2\pi^2) = 2/\pi^2\cdot\pi^2/6 = 1/3$. The $O(1/n)$ decay is the
signature of a function with a jump in its periodic extension — $x$ on $(0,1)$
continued periodically is a sawtooth with jumps of size 1 at the joins.

---

## ★3 — An incomplete orthonormal set

Take only the even modes, $\{e_{2n}(x) = \sqrt2\sin(2n\pi x)\}_{n\ge1}$. They are
orthonormal by the calculation above, but every one of them vanishes at
$x = \tfrac12$ and is odd about $x = \tfrac12$, so the odd function
$f(x) = x - \tfrac12$ is orthogonal to all of them. For $f(x) = 1$ the
coefficients are $c_{2n} = 0$ for every $n$, so $\sum_n c_n^2 = 0$ while
$\lVert f\rVert^2 = 1$. The gap is exactly $\lVert f - 0\rVert^2 = 1$: Bessel's
inequality holds with enormous slack, and Parseval fails. This is the operational
meaning of "the gap is the norm of the part of $f$ outside the span".

---

## ★4 — The normal equations by differentiation

Let $J(\boldsymbol\alpha) = \big\lVert f - \sum_j\alpha_jg_j\big\rVert^2$. Expanding,

$$J = \lVert f\rVert^2 - 2\sum_j\alpha_j\langle f,g_j\rangle +
\sum_{j,k}\alpha_j\alpha_k\langle g_j,g_k\rangle .$$

Differentiating with respect to $\alpha_i$ (all terms are quadratic or linear),
using the symmetry $\langle g_j,g_k\rangle = \langle g_k,g_j\rangle$:

$$\frac{\partial J}{\partial\alpha_i} = -2\langle f,g_i\rangle +
2\sum_j\alpha_j\langle g_j,g_i\rangle .$$

Setting this to zero for every $i$ gives
$\sum_j\langle g_j,g_i\rangle\alpha_j = \langle f,g_i\rangle$, which is (1) of
the lesson. The second derivative matrix is $2G$, positive definite when the
$g_j$ are independent, so the stationary point is a minimum. **If the $g_i$ are
orthonormal**, $\langle g_j,g_i\rangle = \delta_{ij}$, so $G = I$ and
$\alpha_i = \langle f,g_i\rangle$: each coefficient is computed independently,
with no linear solve and no coupling of round-off between coefficients.

---

## ★5 — How many modes for a $10^{-2}$ error?

The squared error of the truncated sine series of $f = 1$ is

$$\lVert f - S_N\rVert^2 = \sum_{\substack{n > N\\ n\ \text{odd}}}
\frac{8}{n^2\pi^2} = \frac{8}{\pi^2}\left(\frac{\pi^2}{8} -
\sum_{\substack{n\le N\\ n\ \text{odd}}}\frac{1}{n^2}\right),$$

using $\sum_{\text{odd}}1/n^2 = \pi^2/8$. Evaluating this by summing the
reciprocal squares (computed for these solutions):

| $N$ | exact tail (squared error) | $4/(\pi^2N)$ |
|---|---|---|
| 39 | $1.013001\times10^{-2}$ | $1.039192\times10^{-2}$ |
| 399 | $1.013210\times10^{-3}$ | $1.015751\times10^{-3}$ |
| 3999 | $1.013212\times10^{-4}$ | $1.013465\times10^{-4}$ |

The smallest odd $N$ with squared error below $10^{-4}$ is $N = 4053$, giving an
error of $0.009999$ — just inside the target. The asymptotic prediction
$4/(\pi^2N)$ (the factor 4 rather than 8 arises because the odd integers have
density $\tfrac12$) agrees with the exact tail to 0.03 per cent at $N = 3999$ and
to 2.5 per cent at $N = 39$. **A $10^{-2}$ relative error in a field that is
piecewise constant needs of order $4\times10^3$ modes**, which is the quantitative
form of "the convergence rate is set by the regularity".

---

## ★6 — The addition theorem at $\theta = \pi/2$, $\phi = 0$

With $\cos\theta = 0$ and $\phi = 0$, and using the real harmonics of the lesson:

- $l = 0$: $Y_{00} = 1/\sqrt{4\pi}$, so $\sum_m Y_{0m}^2 = 1/(4\pi) = 0.0795775$.
- $l = 1$: $Y_{10} = \sqrt{3/(4\pi)}\cos\theta = 0$ and
  $Y_{1,\pm1} = \mp\sqrt{3/(8\pi)}\sin\theta$, whose squares sum to
  $2\cdot3/(8\pi)\cdot1 = 3/(4\pi) = 0.2387324$.
- $l = 2$: $P_2(0) = -\tfrac12$ gives $Y_{20}^2 = 5/(16\pi)$; $P_2^1(0) = 0$ so
  $Y_{2,\pm1} = 0$; and $P_2^2(0) = 3$ with
  $N_{22} = \sqrt{5/(96\pi)}$ gives
  $Y_{22} = \sqrt2\sqrt{5/(96\pi)}\cdot3\cos(2\phi)$, which at $\phi = 0$ has
  square $15/(16\pi)$, while $Y_{2,-2}\propto\sin(2\phi)$ vanishes. The total is
  $5/(16\pi) + 15/(16\pi) = 5/(4\pi) = 0.3978874$.
- $l = 3$: the sum is $7/(4\pi) = 0.5570423$.

Each equals $(2l+1)/(4\pi)$. The demo's reported deviations of
$1.4\times10^{-17}$ to $6.7\times10^{-16}$ are **not** quadrature error: the
integrand for the orthonormality check is a polynomial in $\cos\theta$ of degree
at most 6 and a trigonometric polynomial in $\phi$, and the rules used integrate
both exactly. The deviations are therefore accumulated floating-point round-off
from the recurrence for $P_l^m$ and from the trigonometric evaluations — about
$10^{-16}$ relative to the magnitude of the sums, which is one unit in the last
place for double precision. Recognising that a residual is *round-off* rather
than *discretisation error* is the difference between a verification and a
misreading.

---

## ★7 — The Gibbs phenomenon

**(a)** With $f = \operatorname{sign}(x - \tfrac12)$,

$$\int_0^1 f(x)\sin(n\pi x)\,dx
= -\int_0^{1/2}\!\!\sin(n\pi x)\,dx + \int_{1/2}^1\!\!\sin(n\pi x)\,dx
= \frac{2\cos(n\pi/2) - 1 - (-1)^n}{n\pi},$$

and the sine-series coefficient in the basis $\sin(n\pi x)$ is twice this,
$b_n = 2(2\cos(n\pi/2) - 1 - (-1)^n)/(n\pi)$, confirming the stated formula.

**(b)** Computed directly by summing the series on a fine grid near the jump
(computed for these solutions):

| $N$ | $\max_x S_N(x)$ | overshoot above 1 | relative to the jump of 2 |
|---|---|---|---|
| 50 | 1.179473 | 0.179473 | 8.9737 % |
| 200 | 1.179013 | 0.179013 | 8.9507 % |
| 2000 | 1.178974 | 0.178974 | 8.9487 % |

**(c)** The limit is $\frac{2}{\pi}\operatorname{Si}(\pi) - 1$, where
$\operatorname{Si}(z) = \int_0^z\sin t/t\,dt$; numerically
$\frac{2}{\pi}\times1.8519371 - 1 = 0.1789797$, i.e. $17.898$ per cent of the
half-jump and $8.949$ per cent of the total jump of 2. The textbook statement
"about 9 per cent" refers to the fraction of the **total** jump; the partial sum
overshoots the upper level by 17.9 per cent of that level's distance from the
mean. Both statements are correct and they differ by a factor of two, which is
exactly why the number should be quoted with the reference it is measured
against. The $N = 10$ row of the demo run (not tabulated here) shows no overshoot
at all — the series has too few terms to resolve the jump — so the phenomenon is
asymptotic, not immediate.

---

## ★8 — Truncating a synthetic geoid

Let $f(\theta,\phi) = \sum_{(l,m)\in S}c_{lm}Y_{lm}$ with $S = \{(2,0),(3,1),(5,-2),
(8,3)\}$ and $c = (1.0, 0.5, 0.3, 0.1)$ km.

**(a)** The exact field lies in a 4-dimensional subspace, so **truncation at any
$L \ge 8$ reproduces it exactly** and the error is at the round-off level of the
quadrature. Truncation at $L \ge 8$ is the projection onto a subspace containing
$f$, hence $f - P_Lf = 0$. For $L < 8$ the error is the norm of the discarded
part:

| $L$ | retained | discarded | squared error (km²) |
|---|---|---|---|
| 2 | $(2,0)$ | $(3,1),(5,-2),(8,3)$ | $0.5^2 + 0.3^2 + 0.1^2 = 0.35$ |
| 4 | $(2,0),(3,1)$ | $(5,-2),(8,3)$ | $0.3^2 + 0.1^2 = 0.10$ |
| 6 | $(2,0),(3,1),(5,-2)$ | $(8,3)$ | $0.01$ |
| 10 | all | none | $0$ |

**(b)** The squared error equals the sum of the discarded degree powers
**because the basis is orthonormal**: $\lVert\sum_n c_ne_n\rVert^2 = \sum_n
c_n^2$, so the error of a truncation is the $\ell^2$ norm of the coefficients
outside the retained set, with no cross terms. This is Parseval used as an error
identity rather than as a curiosity, and it is why degree variance is the right
summary: it *is* the contribution of that degree to the field's power.

**(c)** If a coefficient changed sign, the error would be unchanged: it depends on
$c_{lm}^2$. So a truncation-error table carries no information about the sign of
the discarded coefficients, and a model compared with data only through the
truncation error cannot distinguish $+c$ from $-c$. That is a real limitation when
the target quantity is a gradient or a deflection rather than the field itself,
since gradients are odd in the coefficients.

---

## ★9 — Legendre in latitude versus associated Legendre on the sphere

**(a)** With $u = \cos\theta$, the substitution
$\int_0^\pi F(\theta)\sin\theta\,d\theta = \int_{-1}^{1}F(\arccos u)\,du$ shows
that an integral over the sphere becomes a flat-weight integral in $u$, whereas
the same integrand integrated over $\theta$ carries the weight $\sin\theta$.
The basis functions $P_l(\cos\theta)$ and the measure are tied together; changing
one without the other changes the inner product.

**(b)** Using orthogonality of Legendre polynomials under the flat weight,
$\int_{-1}^{1}P_1(u)P_3(u)\,du = 0$, so

$$\int_0^\pi P_1(\cos\theta)P_3(\cos\theta)\sin\theta\,d\theta =
\int_{-1}^{1}P_1(u)P_3(u)\,du = 0 .$$

With the flat $\theta$ measure instead, the integral does **not** vanish: the
integrand is $P_1(\cos\theta)P_3(\cos\theta) = \cos\theta\cdot\tfrac12(5\cos^3
\theta - 3\cos\theta)$, and
$\int_0^\pi\cos^2\theta\,d\theta = \pi/2$ while
$\int_0^\pi\cos^4\theta\,d\theta = 3\pi/8$; hence the integral is
$\tfrac12(5\cdot\tfrac{3\pi}{8} - 3\cdot\tfrac{\pi}{2}) =
\tfrac12(\tfrac{15\pi}{8} - \tfrac{12\pi}{8}) = \tfrac{3\pi}{16} = 0.5890486
\ne 0$. So **the $\sin\theta$-weighted integral vanishes and the flat one does
not**: the flat measure is the wrong inner product for functions on the sphere.

**(c)** The wrong quantity is the inner product used to compute the coefficients —
the quadrature weights are missing the $\sin\theta$ factor (equivalently, the
latitude weights are not those of Gauss–Legendre in $\cos\theta$). It is
detectable from the coefficients alone: if the basis is truly orthonormal under
the inner product used, then recomputing the field from its coefficients and
re-projecting must reproduce the same coefficients exactly, and the "energy"
$\sum_l\sum_m c_{lm}^2$ must equal $\int f^2$ evaluated by an independent
quadrature. A mismatch in either check, larger than round-off, means the weights
used to project are not the weights of the inner product being claimed.

---

## ★10 — Methods paragraph for a degree-360 gravity model

A defensible paragraph, with each clause traced to the theory:

> The gravity field is represented as a truncated spherical-harmonic expansion
> $V = \frac{GM}{r}\sum_{l=0}^{360}(a/r)^l\sum_mC_{lm}Y_{lm}(\theta,\phi)$ with
> the real, $4\pi$-normalised harmonics of
> [convention citation], so that $\{Y_{lm}\}$ is orthonormal under
> $d(\cos\theta)\,d\phi$. Coefficients are obtained by orthogonal projection in
> that inner product, discretised with Gauss–Legendre quadrature in
> $\cos\theta$; the projection is the $L^2$-optimal representation of the sampled
> field at degree 360, so the truncation error is not a modelling penalty but the
> norm of the true field's power above degree 360. Degrees whose coefficients the
> data cannot constrain at their stated error level are stabilised by
> regularisation, and are reported separately from the resolved degrees rather
> than mixed with them. Resolution is assessed by the degree at which the formal
> coefficient errors reach the signal level, not by the truncation degree.

Every claim is supported by this lesson: the measure and orthonormality by
Section 5.1, the optimality of the projection by Section 4, the error identity by
Parseval (Section 3.2), and the resolved-versus-regularised distinction by the
projection theorem's dependence on the norm and by lesson 01-16-06.
