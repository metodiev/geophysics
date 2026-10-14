---
id: 19-04-01
title: "Spectral Methods: Basis Choice and Exponential Convergence"
level: research
prereqs: ["19-01-02", "01-10-02", "01-10-05"]
tags: [numerical-modelling, spectral-methods, convergence, chebyshev, fourier, numerical-modelling]
---

# Spectral Methods: Basis Choice and Exponential Convergence

**All models and data in this module are SYNTHETIC.** The test functions are
chosen teaching models, all with exact derivatives known analytically; every
number is printed by
[`code/spectral_methods_demo.py`](./code/spectral_methods_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a global basis converges exponentially for a smooth function
   and only algebraically for a function with a kink, and **measure** both rates.
2. **Derive** the Fourier derivative operator and **state** exactly what its
   error is limited by.
3. **Compare** spectral and finite-difference accuracy at equal resolution, and
   **extrapolate** the measured error constants to a common tolerance.
4. **Choose** a basis from the geometry of the problem, and **justify** the
   choice with a measured error, not with a preference.
5. **Distinguish** the pointwise maximum error from the root-mean-square error at
   a discontinuity, and **say** which one does not converge.
6. **Measure** the conditioning of a differentiation operator and **relate** it
   to the round-off floor that truncates every convergence table.
7. **State** the assumptions under which the exponential rate is available.

## Prerequisites

- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the vocabulary of order and rate.
- [01-10-02 The Fourier Transform and Its Properties](../../01-mathematics/10-fourier-analysis/02-fourier-transform.md) —
  the transform used here.
- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) —
  sampling as a hard constraint, developed further in lesson
  [02](02-pseudospectral.md).

## 1. What "spectral" means, and what it is not

Every classical method approximates the solution by a finite sum of basis
functions. Two things distinguish a spectral method.

1. The basis functions are **global**: each one spans the whole domain, rather
   than a few cells.
2. The basis is **matched to the problem's geometry and smoothness**: Fourier
   modes for periodic problems, Chebyshev or Legendre polynomials for intervals,
   spherical harmonics for spheres.

The payoff is a change in the *kind* of convergence rather than in its constant.
A $p$-th order method reduces the error by a fixed factor when the mesh is
refined; a spectral method reduces it by a factor that grows without bound as the
resolution increases, until round-off stops it. For an analytic function on a
matched basis the error behaves like

$$\text{error} \sim C\,\rho^{-N}, \qquad \rho > 1, \tag{1.1}$$

so $\log(\text{error})$ is a straight line in $N$ — exponential convergence.
This is not a better constant on the same power law; it is a different law.

### 1.1 The cost that comes with it

A global basis produces a **dense** operator. The differentiation matrix of
Section 5 has $N^2$ non-zeros where a finite-difference stencil has $3N$, and its
norm grows with $N$. Exponential accuracy is bought with dense linear algebra and
with round-off amplification, and the rest of this module is largely about
managing that trade.

## 2. Fourier differentiation of a smooth periodic function

For a $1$-periodic function sampled at $N$ equally spaced points, the discrete
Fourier derivative is exact algebra:

$$\widehat{u'}_k = \mathrm{i}\,k\,\widehat{u}_k,
\qquad k = \frac{2\pi}{N}\,j,\quad j = -\tfrac{N}{2},\dots,\tfrac{N}{2}-1 . \tag{2.1}$$

The only error is that modes with $|k|$ above the Nyquist limit
$k_{\max} = \pi N$ are not represented at all. For an analytic function the
coefficients decay geometrically, so the omitted tail — and hence the error —
falls geometrically too. The demonstration measures the maximum derivative error
for $f(x) = e^{\sin(2\pi x)}$:

| $N$ | $\max|f'_N - f'|$ | relative | factor from the previous $N$ |
|---|---|---|---|
| 8 | $2.713\times10^{-2}$ | $3.011\times10^{-3}$ | — |
| 12 | $2.403\times10^{-4}$ | $2.679\times10^{-5}$ | $1.129\times10^{2}$ |
| 16 | $1.107\times10^{-6}$ | $1.229\times10^{-7}$ | $2.171\times10^{2}$ |
| 24 | $6.020\times10^{-12}$ | $6.681\times10^{-13}$ | $1.839\times10^{5}$ |
| 32 | $1.865\times10^{-14}$ | $2.048\times10^{-15}$ | $3.228\times10^{2}$ |
| 64 | $6.317\times10^{-14}$ | $6.897\times10^{-15}$ | $2.953\times10^{-1}$ |
| 128 | $1.424\times10^{-13}$ | $1.555\times10^{-14}$ | $4.435\times10^{-1}$ |

Read the table in two halves. From 8 to 24 modes the error falls by a factor
$4.5\times10^{9}$ — three doublings, i.e. not a power law at all. Beyond 24 modes
it *stops improving*, and the last two rows even get slightly worse
($6.3\times10^{-14}$ at 64 modes, $1.4\times10^{-13}$ at 128).

That floor is the important measurement. It is the double-precision round-off of
an FFT-based derivative amplified by the operator norm, and it grows slowly with
$N$ because the differentiation matrix does (Section 5). **A spectral convergence
table that continues past the floor is reporting noise.** The honest statement is
"exponential until $6\times10^{-14}$ relative, then round-off-limited".

## 3. Measured against finite differences

The same function, differentiated by a second-order centred difference and a
fourth-order centred difference:

| $N$ | error, 2nd order | order | error, 4th order | order |
|---|---|---|---|---|
| 8 | $2.137550\times10^{0}$ | — | $8.698719\times10^{-1}$ | — |
| 16 | $5.880345\times10^{-1}$ | 1.862 | $9.896258\times10^{-2}$ | 3.136 |
| 32 | $1.623105\times10^{-1}$ | 1.857 | $7.111481\times10^{-3}$ | 3.799 |
| 64 | $4.091487\times10^{-2}$ | 1.988 | $4.768917\times10^{-4}$ | 3.898 |
| 128 | $1.024995\times10^{-2}$ | 1.997 | $3.005158\times10^{-5}$ | 3.988 |
| 256 | $2.567483\times10^{-3}$ | 1.997 | $1.883613\times10^{-6}$ | 3.996 |

The orders are 2 and 4, as advertised, with the first refinement underestimating
both (1.862 and 3.136) — the usual pre-asymptotic transient. The interesting
number is not the order; it is the *extrapolation*. Using the measured constants
from the $N = 64$ rows,

$$\text{error}_2 \approx \frac{167.6}{N^{2}}, \qquad
\text{error}_4 \approx \frac{8.00\times10^{3}}{N^{4}} . \tag{3.1}$$

To reach the $6.0\times10^{-12}$ that the spectral method achieved with **24
modes**, (3.1) requires $N = 5.276\times10^{6}$ points at second order and
$N = 6.038\times10^{3}$ at fourth order. Both are arithmetic consequences of
measured constants. The comparison is not "spectral methods are better"; it is
"an exponent changes the resource requirement by three to five orders of
magnitude on this problem", and that sentence is checkable.

The trade is real in both directions. Finite differences give a sparse operator,
local support, easy boundary conditions and graceful behaviour on rough data;
spectral methods give dense operators and require smoothness or pay heavily (as
Section 4 measures).

## 4. What a kink costs

Let $f(x) = |\sin(\pi x)|$: continuous, periodic, but with a jump in the first
derivative at $x = 0$ and $x = \tfrac12$. Its Fourier coefficients decay like
$k^{-2}$, so the derivative series converges only like $k^{-1}$:

| $N$ | max error in $f'$ | rms error in $f'$ | rms order |
|---|---|---|---|
| 16 | $1.195655\times10^{0}$ | $5.276582\times10^{-1}$ | — |
| 32 | $1.209105\times10^{0}$ | $3.995314\times10^{-1}$ | 0.401 |
| 64 | $1.212461\times10^{0}$ | $2.920987\times10^{-1}$ | 0.452 |
| 128 | $1.213300\times10^{0}$ | $2.099800\times10^{-1}$ | 0.476 |
| 256 | $1.213510\times10^{0}$ | $1.497010\times10^{-1}$ | 0.488 |
| 512 | $1.213562\times10^{0}$ | $1.062883\times10^{-1}$ | 0.494 |

Two facts, both measured:

- The **pointwise maximum does not converge**. It sits at $1.21$ rad/m and stays
  there, because at a kink the interpolant's derivative has an $O(1)$ error
  however fine the grid — the Gibbs effect. The values of $f$ itself at the nodes
  remain exact; only the derivative is in trouble.
- The **rms error does converge**, at order $\tfrac12$ — the measured sequence
  0.401, 0.452, 0.476, 0.488, 0.494 approaches 0.5 from below. That is exactly
  what coefficients decaying like $k^{-2}$ predict for the derivative of the
  series.

So "spectral methods fail on non-smooth data" is too crude in both directions: the
solution *is* converging, in a norm, at a rate that can be predicted from the
coefficient decay — and the maximum error will not tell you so. **A convergence
claim must name its norm.**

## 5. Basis choice is dictated by geometry

Now take $f(x) = 1/(1+16x^2)$ on $[-1,1]$: analytic, even, and with
$f(-1) = f(1) = 1/17$, so its periodic extension is *continuous*. What jumps is
the derivative: $f'(x) = -32x/(1+16x^2)^2$ gives $f'(-1) = +32/289 = +0.110727$
and $f'(1) = -32/289$, so the periodic extension has a **kink at the join**. The
measured maximum Fourier derivative error settles at $1.107266\times10^{-1}$,
which is $32/289$ to six digits: the maximum error is exactly the size of the
derivative jump. That is the clearest possible statement of what a mismatched
basis costs, and it is a measurement rather than a theory.

The demonstration measures the Fourier rms error (kink-limited) against the
Chebyshev maximum error (kink-free):

| $N$ | Fourier rms in $f'$ | order | Chebyshev max in $f'$ | order |
|---|---|---|---|---|
| 8 | $3.182355\times10^{-1}$ | — | $1.028427\times10^{0}$ | — |
| 16 | $4.727172\times10^{-2}$ | 2.751 | $2.872896\times10^{-1}$ | 1.840 |
| 32 | $2.410755\times10^{-2}$ | 0.971 | $1.116890\times10^{-2}$ | 4.685 |
| 64 | $1.724540\times10^{-2}$ | 0.483 | $8.213854\times10^{-6}$ | 10.409 |
| 128 | $1.226932\times10^{-2}$ | 0.491 | $2.178258\times10^{-12}$ | 21.846 |

At $N = 128$ the Chebyshev maximum error is $2.178\times10^{-12}$ against the
Fourier rms error $1.227\times10^{-2}$ — a factor $5.633\times10^{9}$. The
Chebyshev column's *orders* (1.840, 4.685, 10.409, 21.846) are not orders at all:
they are the signature of exponential convergence, where a fixed factor per
doubling of $N$ no longer describes the behaviour. The Fourier column's orders
settle at $\tfrac12$, the kink rate.

Neither basis is better in the abstract. The periodic basis is wrong here *by
construction*: it is being asked to represent a function whose periodic extension
has a kink. Refining cannot repair a mismatch of that kind at a useful rate.

### 5.1 Chebyshev differentiation, concretely

The Chebyshev–Gauss–Lobatto nodes on $[-1,1]$ are $x_j = \cos(\pi j/N)$, and the
differentiation matrix has the explicit entries

$$D_{ij} = \frac{c_i}{c_j}\frac{(-1)^{i+j}}{x_i - x_j}\ (i \ne j), \qquad
D_{ii} = -\frac{x_i}{2(1-x_i^2)}\ (0 < i < N), \qquad
c_0 = c_N = 2,\ c_i = 1\ \text{otherwise}, \tag{5.1}$$

with the two endpoint rows fixed by the condition that $D$ annihilates constants:
$D_{ii} = -\sum_{j\ne i}D_{ij}$ there. That last step is where a hand-rolled
Chebyshev matrix usually goes wrong, and it is why the demonstration applies the
row-sum fix explicitly rather than computing the endpoint entries from a formula.

## 6. Conditioning, and the round-off floor

| $N$ | $\|D_{\rm Fourier}\|_2/N$ | $\|D_{\rm Chebyshev}\|_2$ |
|---|---|---|
| 8 | 2.3562 | 36.8027 |
| 16 | 2.7489 | 142.3488 |
| 32 | 2.9452 | 564.5655 |
| 64 | 3.0434 | 2253.4444 |

The Fourier operator's norm per point approaches $\pi$ (the largest wavenumber a
grid of $N$ points per unit length can carry is $\pi N$): measured 2.36 at $N=8$
and 3.04 at $N=64$, of order unity as it must be. The Chebyshev operator grows
like $N^2$ — 36.8, 142.3, 564.6, 2253.4 for successive doublings, i.e. a factor
3.9, 4.0, 4.0 — because its nodes cluster quadratically near the ends.

This is the measured explanation of the floor in Section 2: an operator with norm
$O(N)$ applied in double precision cannot deliver a relative error better than
about $\|D\| \epsilon_{\rm mach}$, and the residual $6\times10^{-14}$ in the
Fourier table is that product.

## 7. A fully worked resolution estimate

A geophysical field is smooth and periodic with a spectrum that decays like
$|\hat{u}_k| \le A\rho^{-k}$ for some $\rho > 1$. The derivative error is
dominated by the first omitted mode:

$$\|u' - u'_N\|_\infty \approx A\,k_{\max}\,\rho^{-k_{\max}},
\qquad k_{\max} = \pi N . \tag{7.1}$$

Work in terms of the integer mode number $m$ (cycles per domain), so that a
truncation at $m_{\max}$ has error $\approx m_{\max}\rho^{-m_{\max}}$, and a real
function on $N$ grid points carries modes up to $m_{\max} = N/2$. Take $A = 1$ and
$\rho = 1.5$, and require a relative derivative error of $10^{-6}$. Solving

$$m\,(1.5)^{-m} = 10^{-6} \tag{7.2}$$

numerically gives $m = 43.37$, hence $N \ge 2m \approx 87$ points. For comparison
$\log(1/\varepsilon)/\log\rho = 34.07$, so the mode count is only slightly above
that; the difference is the $m$ prefactor, which contributes a logarithm. The
shape of the conclusion is what matters:

$$N \sim \frac{\log(1/\varepsilon)}{\log \rho} \quad\text{(spectral)},
\qquad N \sim \varepsilon^{-1/p} \quad\text{(order } p\text{)}, \tag{7.3}$$

so the requirement grows **logarithmically** in the target accuracy rather than as
a power of it. That difference is the entire reason spectral methods exist, and it
is visible in the measured table of Section 2, where three doublings of $N$ carry
nine decades of error.

As a sanity check on the model, the measured errors were $2.7\times10^{-2}$ at
$N=8$, $2.4\times10^{-4}$ at $N=12$ and $1.1\times10^{-6}$ at $N=16$, so the real
$e^{\sin(2\pi x)}$ reaches $10^{-6}$ at about $N=16$ -- far sooner than the
$\rho = 1.5$ model's 87 points, because that function is entire and its
coefficients decay faster than any geometric sequence. The model is therefore a
*conservative* statement about a merely analytic field, which is the right way to
use it.

## 8. Assumptions and regime of validity

1. **Smoothness matched to the basis.** Exponential convergence is available for
   analytic $u$ *and* the right basis on the right geometry. A kink (Section 4) or
   a mismatch at the boundary (Section 5) removes it and leaves at best
   algebraic convergence.
2. **Periodicity for the Fourier basis.** The Fourier basis converges
   exponentially only if the periodic extension is smooth: the *function* and all
   its derivatives must agree at the join. In Section 5, $f(-1) = f(1)$ but
   $f'(-1) \ne f'(1)$, and the rate collapsed.
3. **Uniform grids for Fourier, clustered grids for Chebyshev.** The node sets
   are part of the method, not an implementation detail.
4. **Round-off is a hard floor.** The measured $6\times10^{-14}$ absolute limit,
   amplified by the operator norm of Section 6, is not improvable by refinement
   in double precision.
5. **The error norm must be stated.** Section 4 measured a maximum error that
   does not converge and an rms error that does, for the same solution.
6. **A dense operator.** Spectral accuracy costs $O(N^2)$ storage for the operator
   and, in more than one dimension, a tensor-product grid unless something else
   (a spectral element decomposition, or a fast transform) is brought in — see
   lesson [03](03-spectral-elements.md).

## 9. Mastery checkpoint

Complete this without notes.

> A 1 Hz seismic wavelet is to be propagated on a periodic grid of length
> $L = 10$ km, and the wavefield is smooth with coefficients decaying like
> $\rho^{-k}$ for $\rho = 1.5$.
>
> **(a)** Write the error model and estimate the number of grid points needed for
> a $10^{-6}$ relative derivative error.
> **(b)** A colleague replaces the periodic grid with a Fourier basis on a
> non-periodic boundary and measures an order of 0.5. Explain why the measured
> order is 0.5 and what coefficient decay predicts it.
> **(c)** The same code is run with $N$ doubled twice past the point where the
> error stopped improving. Predict what happens to the measured error, and say
> what that tells you about the operator you are applying.
> **(d)** State one property of the operator that grows with $N$ and one that does
> not, with the measured values from this lesson.
> **(e)** The run must also handle a source with a travel-time kink. State which
> norm you would report and why a maximum-error plot would mislead.

A worked version appears with the
[exercises](exercises/01-spectral-methods-exercises.md).

## 10. Common pitfalls

1. **Continuing a convergence table past the floor.** Measured: the error rises
   from $6.3\times10^{-14}$ to $1.4\times10^{-13}$ between $N=64$ and $N=128$.
2. **Removing a kink by refinement.** The pointwise error at a kink stays at
   $1.21$ rad/m at every mesh from 16 to 512 points.
3. **Reporting a maximum error where the norm is rms.** The two differ by two
   orders of magnitude in the measured table.
4. **Choosing a basis by reputation.** The periodic basis is wrong by
   construction for a non-periodic function; the measured penalty at $N=128$ is
   a factor $5.6\times10^{9}$.
5. **Trusting a fitted "order" from an exponentially converging sequence.** The
   Chebyshev orders measured here are 1.840, 4.685, 10.409, 21.846.
6. **Blaming the physics for a round-off floor.** The floor is
   $\|D\|\epsilon_{\rm mach}$, a property of the operator and the arithmetic.
7. **Forgetting that the operator is dense.** The spectral derivative at $N$
   points costs $N^2$ multiplications if formed as a matrix, against $3N$ for a
   second-order stencil; that is the price of Section 3's three-to-five order
   reduction in $N$.

## 11. Related modules

- [19-04-02 Pseudospectral Methods, Transforms and Aliasing](02-pseudospectral.md) —
  what happens when the transform is used to evaluate nonlinear terms.
- [19-04-03 Spectral Element Methods and Their Geophysical Use](03-spectral-elements.md) —
  how global accuracy is recovered on a domain that cannot be one grid.
- [19-04-04 Spherical Harmonic Modelling of Global Fields](04-spherical-harmonics-modelling.md) —
  the basis that matches a sphere.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the finite-difference counterpart of Sections 3 and 6.
- [20-signal-processing](../../20-signal-processing/README.md) —
  the same transforms applied to measured data rather than to model fields.

## Materials

- Demonstration: [`code/spectral_methods_demo.py`](./code/spectral_methods_demo.py).
- Exercises: [`exercises/01-spectral-methods-exercises.md`](./exercises/01-spectral-methods-exercises.md)
  with worked [solutions](./exercises/01-spectral-methods-solutions.md).
