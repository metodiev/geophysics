# Exercises — 01-16-02 Hilbert Spaces and Orthogonal Expansions

Attempt these **closed-book** before opening the
[solutions](./02-hilbert-spaces-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the inner product is $\langle f,g\rangle = \int fg$ with the stated
measure; $\{e_n\}$ is orthonormal; $c_n = \langle f,e_n\rangle$; the sine basis on
$(0,1)$ is $e_n(x) = \sqrt2\sin(n\pi x)$ and the sphere measure is
$d(\cos\theta)\,d\phi$. Numerical answers should be reported to four significant
figures unless a closed form is available.

---

## ★ Foundational

**★1.** State the parallelogram law and prove it from the inner-product axioms.
Then evaluate both sides for $f(x) = g(x) = 1$ in $L^1(0,1)$ and in $L^2(0,1)$,
and state the conclusion for $L^1$.

---

**★2.** Verify that $e_n(x) = \sqrt2\sin(n\pi x)$ is orthonormal on $(0,1)$, and
compute the coefficients $c_n$ of $f(x) = x$ in that basis. Give the leading
asymptotic behaviour of $c_n$ for large $n$.

---

**★3.** Give an example of an orthonormal set in $L^2(0,1)$ that is not complete,
and compute $\sum_n c_n^2$ for $f(x) = 1$ in that set. What is
$\lVert f\rVert^2 - \sum_n c_n^2$?

---

## ★★ Applied

**★★4.** Derive the normal equations $G\boldsymbol{\alpha} = \mathbf{b}$ with
$G_{ij} = \langle g_j,g_i\rangle$ and $b_i = \langle f,g_i\rangle$ by
differentiating $\lVert f - \sum_j\alpha_jg_j\rVert^2$ with respect to
$\alpha_i$. Show that for orthonormal $g_i$ the matrix $G$ is the identity.

---

**★★5.** For $f(x) = 1$ on $(0,1)$ expanded in the sine basis, find the smallest
odd $N$ for which $\lVert f - S_N\rVert_2 < 10^{-2}$. Compare with the
asymptotic prediction $4/(\pi^2N)$ for the squared error, and report the
percentage difference between the exact tail and the prediction at $N = 3999$.

---

**★★6.** Evaluate $\sum_m Y_{lm}(\theta,\phi)^2$ at $\theta = \pi/2$,
$\phi = 0$ for $l = 0,1,2,3$ using the explicit polynomials, and verify that each
equals $(2l+1)/(4\pi)$. The demo reports deviations of $1.4\times10^{-17}$ to
$4.4\times10^{-16}$; explain the source of those numbers.

---

**★★7.** The Gibbs overshoot for the square wave $f(x) =
\operatorname{sign}(x-\tfrac12)$ on $(0,1)$ is computed by summing the sine
series. Its coefficients are
$b_n = 2(2\cos(n\pi/2) - 1 - (-1)^n)/(n\pi)$.

(a) Verify this coefficient formula by integrating directly.
(b) Compute $\max_x S_N(x)$ for $N = 50, 200, 2000$.
(c) Express the limiting overshoot as a percentage of the jump, and reconcile
"about 9 per cent" with the value you measure.

---

## ★★★ Research-oriented

**★★★8.** Construct a synthetic geoid made of the harmonics $(l,m) = (2,0)$,
$(3,1)$, $(5,-2)$, $(8,3)$ with coefficients $1.0$, $0.5$, $0.3$, $0.1$ (units of
km). Truncate the expansion at $L = 2, 4, 6, 10$ and report the $L^2$ truncation
error against the exact field, using Gauss–Legendre quadrature in $\cos\theta$
and the trapezoid rule in $\phi$.

(a) Tabulate the error against $L$ and report the observed decay.
(b) Compare with the degree power $\sum_m c_{lm}^2$ of the constructed field and
explain the relation.
(c) State what the answer would be if one of the four coefficients were negative
and of the same magnitude, and why.

---

**★★★9.** A colleague parameterises a regional gravity field with Legendre
polynomials in latitude (flat weight) instead of associated Legendre functions
with the $\sin\theta$ weight, and reports coefficients that do not match a
spherical-harmonic model.

(a) Show that the two sets of basis functions are related by
$u = \cos\theta$ but the inner products are not.
(b) Compute $\int_0^\pi P_1(\cos\theta)P_3(\cos\theta)\sin\theta\,d\theta$ and
$\int_0^\pi P_1(\cos\theta)P_3(\cos\theta)\,d\theta$, and state which vanishes.
(c) Write two sentences telling the colleague exactly which quantity in their
code is wrong and how to detect it from the coefficients alone.

---

**★★★10.** Write a short methods paragraph for a paper that reports a
degree-360 gravity model. It must state: the basis and its normalisation; the
measure used in the inner product; the projection error from truncation; the
distinction between the resolved degrees and the regularised ones; and the fact
that the truncated model is the $L^2$-optimal representation at that degree.
Every claim must be one the theory of this lesson supports.
