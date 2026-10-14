---
id: 01-11-03
title: "Contour Integration, Residues and Real Integrals"
level: graduate
prereqs: ["01-11-02", "01-05-06"]
estimated_minutes: 90
tags: [contour-integration, residues, cauchy-theorem, green-functions, dispersion-relations]
---

# Contour Integration, Residues and Real Integrals

## Learning objectives

By the end of this lesson you will be able to:

1. **Integrate** a complex function along a parametrised path and explain when
   the answer is independent of the path.
2. **State** Cauchy's theorem and the Cauchy integral formula, and use both to
   replace an integral by the value of the integrand at a point.
3. **Classify** isolated singularities, compute residues of poles of any order,
   and apply the residue theorem.
4. **Choose** a contour for each standard family of real integrals — rational
   functions on the real line, Fourier-type integrals, and Cauchy principal
   values — and say which arc-closing argument justifies the choice.
5. **Verify** every closed form by numerical quadrature of the *real* integral,
   and say what the residual measures.
6. **Explain** why the closing arc may cancel to leading order, and how to
   measure the order at which it does not.
7. **Recognise** the residue machinery inside the Green's functions and
   dispersion relations used later in the curriculum.

## Prerequisites

[01-11-02 Holomorphic Functions and Cauchy-Riemann
Equations](./02-complex-functions.md) — holomorphy, harmonic functions and the
complex potential;
[01-05-06 Improper Integrals, Singularities and
Convergence](../05-single-variable-calculus/06-improper-integrals.md) — improper
integrals and convergence, because every integral evaluated here is improper at
both ends and possibly at an interior point.

## 1. Intuition: an integral along a path, and what a closed path knows

An ordinary integral is taken along the real line. A **contour integral** is
taken along a curve in the complex plane,

$$\int_{\gamma} f(z)\,\mathrm{d}z
= \int_{a}^{b} f\bigl(z(t)\bigr)\,z'(t)\,\mathrm{d}t,$$

with $z(t)$ a parametrisation of $\gamma$. Nothing in that definition is
mysterious: it is a real integral in disguise, and any quadrature rule evaluates
it. What is mysterious is what happens when $\gamma$ is a *closed* curve and $f$
is holomorphic inside it.

For holomorphic $f$, the integral depends only on the endpoints — a potential
function $F$ with $F' = f$ exists, and
$\int_{\gamma}f\,\mathrm{d}z = F(z_{1})-F(z_{0})$. So for a closed curve the
integral is zero. That is **Cauchy's theorem**. It is the complex analogue of
the statement that a conservative field does no work around a closed loop, and
it is immediate from the Cauchy-Riemann equations of the previous lesson: the
integrand $f\,\mathrm{d}z = (u\,\mathrm{d}x - v\,\mathrm{d}y) +
i(v\,\mathrm{d}x + u\,\mathrm{d}y)$ has both real forms satisfy the
cross-derivative condition exactly when the Cauchy-Riemann equations hold.

Everything follows from one observation about that zero. If $f$ has a
singularity inside the loop, the integral need not be zero, and its value turns
out to depend on the singularity and on nothing else — not on the shape of the
loop, not on how big it is. That is why a residue can be read off and why real
integrals that no substitution can crack fall to a computation that takes three
lines.

The three results, in the order they are used:

| result | statement | what it buys |
|---|---|---|
| Cauchy's theorem | $\oint_{\gamma} f\,\mathrm{d}z = 0$ for $f$ holomorphic inside $\gamma$ | path independence; the freedom to deform contours |
| Cauchy integral formula | $\oint_{\gamma} \frac{f(z)}{z-z_{0}}\mathrm{d}z = 2\pi i f(z_{0})$ | the value of $f$ at a point from its values on a loop |
| Residue theorem | $\oint_{\gamma} f\,\mathrm{d}z = 2\pi i\sum_{k}\operatorname{Res}_{z_{k}}f$ | real integrals, series, and the arithmetic of poles |

## 2. Contour integrals: the mechanics

### 2.1 Parametrisation and the two workhorses

A circle of radius $R$ centred at $z_{0}$ is parametrised by
$z(t) = z_{0} + Re^{it}$ with $\mathrm{d}z = iRe^{it}\mathrm{d}t$ and
$t \in [0,2\pi]$. A straight segment from $a$ to $b$ is
$z(t) = a + (b-a)t$ with $\mathrm{d}z = (b-a)\mathrm{d}t$. A semicircle in the
upper half plane is the same circle with $t \in [0,\pi]$.

The demo's contour operations are exactly these two, so that its residue check
and arc check are verifiable by hand. For a circle,

$$I = \int_{0}^{2\pi} f\bigl(z_{0} + Re^{it}\bigr)\,
iRe^{it}\,\mathrm{d}t,$$

and since the integrand is periodic and analytic, the trapezoidal rule on $t$
converges *spectrally*: doubling the number of nodes changes nothing beyond
round-off. That is why the demo can compute a residue to $10^{-15}$ from a
contour that nobody would evaluate by hand.

### 2.2 The Cauchy integral formula, verified

If $f$ is holomorphic on and inside a simple closed contour $\gamma$ and $z_{0}$
is inside, then

$$\oint_{\gamma}\frac{f(z)}{z-z_{0}}\,\mathrm{d}z = 2\pi i f(z_{0}).$$

Differentiating $n$ times with respect to $z_{0}$ (legitimate, and the source of
the "infinitely differentiable" property) gives the general formula

$$\oint_{\gamma}\frac{f(z)}{(z-z_{0})^{n+1}}\,\mathrm{d}z
= \frac{2\pi i}{n!}f^{(n)}(z_{0}).$$

The demo evaluates three such integrals by quadrature around circles and
compares with the closed form:

| integrand | contour | quadrature | $2\pi i f(z_{0})$ | difference |
|---|---|---|---|---|
| $e^{z}/(z-1)$ | $\vert z-1\vert=3$ | $+17.079468445i$ | $+17.079468445i$ | $1.9\times10^{-14}$ |
| $z^{2}/(z-i)$ | $\vert z-i\vert=2$ | $-6.283185307i$ | $-6.283185307i$ | $6.0\times10^{-14}$ |
| $\cos z/(z-\pi/2)$ | $\vert z-\pi/2\vert=2$ | $0$ | $0$ | $7.3\times10^{-16}$ |

The first row is $2\pi ie = 17.079468445$, the second is
$2\pi i\cdot i^{2} = -2\pi i$, and the third is $2\pi i\cos(\pi/2) = 0$. Note
what the third row says: the *integrand* is singular, but its contour integral
vanishes because the numerator vanishes at the singularity faster than the pole
grows. A singularity is not the same thing as a non-zero residue.

### 2.3 Deforming the contour

Because a holomorphic function integrates to zero around a closed loop, two
contours with the same content can be deformed into each other without changing
the integral. This is the practical technique behind the standard real-integral
recipes:

1. Choose a closed contour made of (a) a piece of the real axis, (b) an arc at
   infinity that you will argue contributes nothing in the limit.
2. Evaluate the closed integral by residues.
3. Solve for the piece on the real axis.

Deforming a small circle up to a large one is what makes the *residue* local: the
integral around any loop containing a single singularity is the same as the
integral around an arbitrarily small circle, and the small circle is easy.

## 3. Singularities and residues

### 3.1 Classification

A point $z_{0}$ is an **isolated singularity** of $f$ if $f$ is holomorphic in a
punctured disc $0 < |z-z_{0}| < \rho$. Near such a point $f$ has a **Laurent
series**

$$f(z) = \sum_{n=-\infty}^{\infty} a_{n}(z-z_{0})^{n},$$

and the classification is by how far the negative powers reach:

| type | negative part | example | behaviour |
|---|---|---|---|
| removable | none | $\sin z / z$ | bounded; the singularity is an artefact |
| pole of order $m$ | stops at $n = -m$ | $1/z^{2}$ | $\vert f\vert\to\infty$ as $z\to z_{0}$ |
| essential | infinite | $e^{1/z}$ | no limit; the series never terminates |

The **residue** is the coefficient of $(z-z_{0})^{-1}$:

$$\operatorname{Res}_{z_{0}}f = a_{-1}.$$

The residue is the only Laurent coefficient that matters for contour integrals,
because $\oint (z-z_{0})^{n}\mathrm{d}z = 2\pi i$ for $n = -1$ and zero for every
other integer $n$. That single fact is the residue theorem.

### 3.2 Computing residues

**Simple pole.** If $f = g/h$ with $h(z_{0}) = 0$, $h'(z_{0}) \neq 0$ and $g$
holomorphic at $z_{0}$, then

$$\operatorname{Res}_{z_{0}}f = \frac{g(z_{0})}{h'(z_{0})}
= \lim_{z\to z_{0}}(z-z_{0})f(z).$$

**Pole of order $m$.**

$$\operatorname{Res}_{z_{0}}f = \frac{1}{(m-1)!}
\lim_{z\to z_{0}}\frac{\mathrm{d}^{m-1}}{\mathrm{d}z^{m-1}}
\bigl[(z-z_{0})^{m}f(z)\bigr].$$

**The residue theorem.** For a simple closed contour $\gamma$ traversed
counter-clockwise with $f$ holomorphic on and inside it except for isolated
singularities $z_{1},\dots,z_{n}$ inside,

$$\oint_{\gamma}f(z)\,\mathrm{d}z
= 2\pi i\sum_{k=1}^{n}\operatorname{Res}_{z_{k}}f .$$

### 3.3 Verified residues

The demo computes each residue twice: analytically, and as a contour integral
around a small circle, $\operatorname{Res} = (2\pi i)^{-1}\oint f\,\mathrm{d}z$.
It uses a radius of $0.005$, small enough that no other singularity is enclosed,
but the answer does not depend on the radius at all — the proof above says so, and
the demo prints the same value at radii $0.3$, $0.05$ and $0.005$:

| pole | analytic residue | numerical residue | difference |
|---|---|---|---|
| $1/(1+z^{2})$, simple, at $i$ | $-0.500000i$ | $-0.500000i$ | $1.3\times10^{-15}$ |
| $1/(1+z^{2})^{2}$, order 2, at $i$ | $-0.250000i$ | $-0.250000i$ | $1.6\times10^{-14}$ |
| $1/(z^{2}+2z+5)$, simple, at $-1+2i$ | $-0.250000i$ | $-0.250000i$ | $4.2\times10^{-16}$ |

The double-pole case is the one worth doing by hand, because the derivative in
the formula is easy to forget. Write $1/(1+z^{2})^{2} = 1/[(z-i)^{2}(z+i)^{2}]$,
so $(z-i)^{2}f = 1/(z+i)^{2}$ and

$$\operatorname{Res}_{i}f = \frac{\mathrm{d}}{\mathrm{d}z}
\frac{1}{(z+i)^{2}}\bigg|_{z=i} = \frac{-2}{(2i)^{3}} = \frac{-2}{-8i}
= \frac{1}{4i} = -\frac{i}{4},$$

matching the measured $-0.250000i$.

### 3.4 The same coefficient, read three ways

The Laurent coefficient $a_{-1}$ is a contour integral, so it is also a Fourier
coefficient. On a circle of radius $r$ about the origin,

$$\oint\frac{f(z)}{z^{n+1}}\,\mathrm{d}z = 2\pi i\,a_{n},
\qquad\text{so}\qquad a_{n} = \frac{1}{2\pi r^{n}}
\int_{0}^{2\pi} f\bigl(re^{i\theta}\bigr)e^{-in\theta}\,\mathrm{d}\theta .$$

At $r = 1$ this is the discrete Fourier transform, and the negative powers of the
Laurent series are the negative frequencies. This is the technical reason the
unit circle is the natural home of the $z$-transform
([05 The z-Transform](./05-z-transform.md)): expanding a rational function in its
Laurent series and evaluating a DFT on the unit circle are the same operation.

Residues also sum series, and the identity is worth having because it is how a
periodic array of sources is summed. Integrate

$$f(z) = \frac{\pi\cot(\pi z)}{z^{2}+a^{2}}$$

around a large square whose sides avoid the integers. $\pi\cot(\pi z)$ has a
simple pole with residue $1$ at every integer, so the residue of $f$ at $z = n$ is
$1/(n^{2}+a^{2})$; at $z = \pm ia$ the residues are each
$-\pi\coth(\pi a)/(2a)$, using $\cot(i\pi a) = -i\coth(\pi a)$. The integral
around the square vanishes as the square grows, because $\cot$ is bounded away
from the real axis and $1/(z^{2}+a^{2}) \to 0$, so the residues sum to zero:

$$\sum_{n=-\infty}^{\infty}\frac{1}{n^{2}+a^{2}}
= \frac{\pi}{a}\coth(\pi a).$$

Checked directly with $a = 1$: the truncated sum over $|n| \leq 2\times10^{5}$ is
$3.153338094962$, the analytic tail is $2/N = 1.0000\times10^{-5}$, and the
corrected value $3.153348094962$ agrees with $\pi\coth\pi = 3.153348094937$ to
$2.5\times10^{-11}$. The physical reading: an infinite periodic array of
line sources produces a field that is *not* the sum of $\ln r$ terms taken
naively, but it is the cotangent combination above — and the reason the sum
converges at all is that the individual logarithmic potentials cancel between
neighbours, which is exactly the cancellation that makes $\cot$ bounded.

## 4. Real integrals, one family at a time
### 4.1 Rational functions on the whole line

Take $f(x) = P(x)/Q(x)$ with $\deg Q \geq \deg P + 2$, no real poles, and close
the contour by a large semicircle in the upper half plane. Then

$$\int_{-\infty}^{\infty}\frac{P(x)}{Q(x)}\,\mathrm{d}x
= 2\pi i\sum_{\operatorname{Im}z_{k} > 0}
\operatorname{Res}_{z_{k}}\frac{P}{Q}.$$

The degree condition is what makes the arc vanish: on $|z| = R$ the integrand is
$O(R^{-2})$, the arc length is $\pi R$, so the arc integral is $O(1/R)$.

**Example: $\int_{-\infty}^{\infty}\mathrm{d}x/(1+x^{2}) = \pi$.** The poles are
at $\pm i$; only $+i$ is inside, with residue $1/(2z)|_{z=i} = 1/(2i) = -i/2$.
Hence $2\pi i(-i/2) = \pi$. The demo's sinh-substitution quadrature of the real
integral gives $3.141592653589738$ against $\pi = 3.141592653589793$, a
difference of $5.5\times10^{-14}$.

**Example: $\int_{-\infty}^{\infty}\mathrm{d}x/(x^{4}+1) = \pi/\sqrt2$.** The
poles are the four roots $e^{i\pi/4}$, $e^{3i\pi/4}$, $e^{5i\pi/4}$,
$e^{7i\pi/4}$; two lie in the upper half plane. Since
$4z_{k}^{3} = 4z_{k}^{4}/z_{k} = 4/z_{k}$ at a root,
$\operatorname{Res} = 1/(4z_{k}^{3}) = z_{k}/4 \cdot (1/z_{k}^{4}) =
-z_{k}/4$ using $z_{k}^{4} = -1$. So

$$\sum_{\text{upper}}\operatorname{Res} = -\frac{1}{4}
\left(e^{i\pi/4} + e^{3i\pi/4}\right)
= -\frac{1}{4}\cdot\frac{\sqrt2}{2}\bigl[(1+i) + (-1+i)\bigr]
= -\frac{i\sqrt2}{4},$$

and $2\pi i \times (-i\sqrt2/4) = \pi\sqrt2/2 = \pi/\sqrt2 = 2.2214414691$. The
quadrature gives $2.221441469079$, a difference of $1.1\times10^{-14}$.

The full verification table is:

| integral | closed form | quadrature | difference |
|---|---|---|---|
| $\int 1/(1+x^{2})$ | $3.1415926536$ | $3.141592653590$ | $5.5\times10^{-14}$ |
| $\int 1/(x^{2}+4)$ | $1.5707963268$ | $1.570796326795$ | $3.5\times10^{-14}$ |
| $\int 1/(1+x^{2})^{2}$ | $1.5707963268$ | $1.570796326795$ | $1.3\times10^{-14}$ |
| $\int 1/(x^{4}+1)$ | $2.2214414691$ | $2.221441469079$ | $1.1\times10^{-14}$ |
| $\int (x^{2}+1)/(x^{4}+1)$ | $4.4428829382$ | $4.442882938158$ | $3.8\times10^{-14}$ |
| $\int_{0}^{\infty}1/(1+x^{2})^{2}$ | $0.7853981634$ | $0.785398163397$ | $6.3\times10^{-15}$ |

The fourth and fifth rows are worth comparing, because the two integrands look
unrelated yet are tied by the substitution $x \to 1/x$. Under that substitution
$\int_{0}^{\infty}\mathrm{d}x/(x^{4}+1)$ is mapped to
$\int_{0}^{\infty}x^{2}\mathrm{d}x/(x^{4}+1)$, so the two halves sum to
$\int_{0}^{\infty}(x^{2}+1)\mathrm{d}x/(x^{4}+1)$, which is exactly twice the
first. Hence the half-line values are $\pi/(2\sqrt2) = 1.1107207345$ and
$\pi/\sqrt2 = 2.2214414691$, and the whole-line values are twice those:
$\pi/\sqrt2$ and $\pi\sqrt2$. A residue computation that produces
$4.4428829382$ where the table says $2.2214414691$ has mis-set the problem, not
the algebra — the standard slip being to integrate only over the upper half plane
of a function that was already even.

### 4.2 Quadrature of an integral over an infinite domain

The quadrature used above is a **substitution $x = \sinh t$**, which maps
$(-\infty,\infty)$ onto itself and turns an integrand decaying like $x^{-n}$ into
one decaying like $e^{-(n-1)|t|}$. A truncated Simpson rule is then accurate to
near round-off. The demo prints the convergence:

| $t_{\max}$ | nodes | value | error |
|---|---|---|---|
| 5 | 2000 | $3.114641273452012$ | $2.7\times10^{-2}$ |
| 10 | 5000 | $3.141411053870873$ | $1.8\times10^{-4}$ |
| 20 | 10000 | $3.141592645345183$ | $8.2\times10^{-9}$ |
| 40 | 20000 | $3.141592653589738$ | $5.5\times10^{-14}$ |

The reason this matters beyond bookkeeping: the residual of a contour-integral
claim is only meaningful if the *real* integral can be computed independently to
better accuracy. A truncated quadrature whose own truncation error is $10^{-3}$
cannot certify a closed form to $10^{-6}$.

### 4.3 Fourier-type integrals and Jordan's lemma

Integrals with a factor $e^{i\omega x}$ are the ones that arise in Fourier
analysis, Green's functions and dispersion relations. The relevant estimate is
**Jordan's lemma**: if $f(z)\to 0$ uniformly as $|z|\to\infty$ in the upper half
plane, then

$$\left|\int_{\text{upper arc}}f(z)e^{i\omega z}\,\mathrm{d}z\right| \to 0
\qquad \text{as } R\to\infty,\ \text{for } \omega > 0,$$

because $|e^{i\omega z}| = e^{-\omega\,\operatorname{Im}z} \leq 1$ on the upper
arc, and the oscillation cancels the arc length. For $\omega < 0$ the same
argument closes the contour in the *lower* half plane; for $\omega = 0$ the
plain $O(1/R)$ estimate is all that is available.

**Example.** With $a > 0$ and $\omega > 0$, close in the upper half plane and pick
up the pole at $z = ia$, where

$$\operatorname{Res}_{ia}\frac{e^{i\omega z}}{z^{2}+a^{2}}
= \frac{e^{-\omega a}}{2ia},
\qquad\text{so}\qquad
\int_{-\infty}^{\infty}\frac{\cos\omega x}{x^{2}+a^{2}}\,\mathrm{d}x
= \frac{\pi}{a}e^{-a\omega}.$$

This is the Green's function of the 2-D screened Poisson (Helmholtz) equation:
the potential at horizontal distance $\omega$ from a line source in a medium with
screening $a$. The demo verifies it with $a = 0.8$:

| $\omega$ | quadrature | $(\pi/a)e^{-a|\omega|}$ | difference |
|---|---|---|---|
| 0.5 | $2.632340697607$ | $2.632340665224$ | $3.2\times10^{-8}$ |
| 1.5 | $1.182786906529$ | $1.182786904309$ | $2.2\times10^{-9}$ |
| 3.0 | $0.356248569489$ | $0.356248569503$ | $1.4\times10^{-11}$ |

The residual is the truncation error of the oscillatory quadrature, which is at
worst $3\times10^{-8}$ — five orders of magnitude coarser than the rational
cases, and reported honestly rather than hidden. Oscillatory quadrature needs its
own convergence argument, and the one used here is a substitution plus a two-term
asymptotic tail.

### 4.4 Principal values and the Dirichlet integral

An integral with a simple pole on the path is defined by **Cauchy's principal
value**,

$$\mathrm{P.V.}\int_{-\infty}^{\infty}f(x)\,\mathrm{d}x
= \lim_{\epsilon\to 0^{+}}\left[\int_{-\infty}^{x_{0}-\epsilon}f
+ \int_{x_{0}+\epsilon}^{\infty}f\right],$$

which is the limit taken symmetrically. Contour integration handles it by
indenting the contour around the pole: a small semicircular detour contributes
$-i\pi\operatorname{Res}$ or $+i\pi\operatorname{Res}$ depending on side, against
the $2\pi i\operatorname{Res}$ of a full encircling.

Two measured examples:

- **The Dirichlet integral.** $\int_{0}^{\infty}\sin x/x\,\mathrm{d}x = \pi/2$.
  The demo's corrected quadrature gives $1.570796326703$ against
  $1.570796326795$, a difference of $9.2\times10^{-11}$; a bare truncation at
  $L$ converges only as $1/L$, which is why an asymptotic correction is needed
  before the comparison means anything.
- **An odd integrand.** $\mathrm{P.V.}\int 1/[x(1+x^{2})]\mathrm{d}x = 0$
  exactly, because the integrand is odd and the principal value punctures
  symmetrically. The demo's punctured sum gives $-2.3\times10^{-11}$.

## 5. The vanishing arc, measured

Section 4.1 asserted that the arc contributes $O(1/R)$ and therefore vanishes.
That is true but incomplete, and the incompleteness has bitten every student who
has ever written "the integral over the arc tends to zero" and moved on. The demo
measures the arc directly. For $f = 1/(1+z^{2})$ and $R = 5, 20, 100, 500$:

| $R$ | $\int_{-R}^{R}f(x)\mathrm{d}x$ | $\vert$arc$\vert$ | sum | $2\pi i\operatorname{Res}$ |
|---|---|---|---|---|
| 5 | $2.746801534$ | $3.948\times10^{-1}$ | $3.141592653$ | $3.141592654$ |
| 20 | $3.041675862$ | $9.992\times10^{-2}$ | $3.141592653$ | $3.141592654$ |
| 100 | $3.121593320$ | $2.000\times10^{-2}$ | $3.141592654$ | $3.141592654$ |
| 500 | $3.137592659$ | $4.000\times10^{-3}$ | $3.141592654$ | $3.141592654$ |

Every row already sums to $\pi$ to nine figures: the residue theorem is exact at
every $R$, and only the splitting between the line and the arc changes. The
product $R|\text{arc}|$ takes the values

$$1.973956, \quad 1.998336, \quad 1.999933, \quad 1.999997,$$

converging to **2**, not to $\pi$. The leading term of the arc expansion cancels
identically over a semicircle, because

$$\int_{0}^{\pi}e^{-2i\theta}\,\mathrm{d}\theta =
\left[\frac{e^{-2i\theta}}{-2i}\right]_{0}^{\pi} = 0 .$$

The $2/R$ that remains comes from the next term of
$1/(1+z^{2}) = z^{-2} - z^{-4} + \cdots$. Two lessons follow:

1. A bound of the form "$|$arc$| = O(1/R)$" is not enough to conclude anything;
   you must know that the coefficient is non-zero, or at least that the arc is
   bounded.
2. Verifying "the arc vanishes" numerically is cheap, and it distinguishes a
   correct contour from one that happens to work at the endpoints tested.

## Assumptions and regime of validity

Every closed form in Section 4 rests on four conditions, and each one can be
violated:

| condition | what it requires | symptom when it fails |
|---|---|---|
| **Simple closed contour, positively oriented** | one loop, no self-intersection, counter-clockwise | a factor of $-1$ on every residue |
| **Isolated singularities inside** | no branch cuts or accumulations in the enclosed region | the residue sum is incomplete; a keyhole or a cut-respecting contour is needed |
| **Uniform decay on the closing arc** | $f(z)\to0$ uniformly as $\vert z\vert\to\infty$ on the arc | the arc integral is not zero, and the "answer" is the arc contribution |
| **No poles on the contour** | otherwise the integral is not defined without an indentation | a divergent, grid-dependent numerical result (Section 4.4) |

The degree condition $\deg Q \geq \deg P + 2$ is how the third row is usually
checked for a rational function, and Jordan's lemma is how it is checked for an
integrand with a factor $e^{i\omega z}$. Note that the degree condition is
*sufficient but not necessary*: a rational function with a smaller gap can still
have a vanishing arc if the leading term cancels over the semicircle, which is
exactly what Section 5 measures for $1/(1+z^{2})$.

**Principal values are not ordinary integrals.** A principal value exists when the
two one-sided logarithmic divergences cancel, and it is a *stated convention*
rather than a limit that exists in the usual sense. Its contour implementation is
an indentation, and the indentation's contribution depends on which side of the
pole the contour passes — a sign that is easy to get backwards and impossible to
detect from the magnitude of the answer.

**Regime of validity of the numerical verifications.** The quadratures used here
are accurate only within the class of integrands they were designed for: the
$\sinh$ substitution assumes algebraic decay, the $\tan$ substitution assumes the
integrand is smooth after subtraction, and the oscillatory quadrature assumes
algebraic decay multiplied by a single oscillation. Applying a rule outside its
class produces a plausible number with no error control, which is why every table
in this lesson includes either a convergence column or a comparison with a second
method.

## 6. Python demonstration

[`code/contour_residues_demo.py`](./code/contour_residues_demo.py) prints all
seven tables above and runs in under a second:

```text
python3 code/contour_residues_demo.py
```

Only the standard library is used. Three methodological notes:

**Every contour integral is checked two ways.** Residues are verified from a
small circular contour as well as from the closed form; real integrals are
verified by real quadrature; the semicircle closure is verified by measuring the
arc. A closed form that has been checked only against itself has not been
checked.

**The quadrature is chosen to match the integrand.** $x = \sinh t$ for
algebraically decaying integrands, $x = \tan u$ for principal values and for
integrands with an endpoint singularity, and a truncation plus an asymptotic tail
for oscillatory integrands. Using one rule everywhere would have hidden the
$3\times10^{-8}$ residual of Section 4.3 inside a much larger error.

**The singularity in a principal-value quadrature is removed, not avoided.** In
$g(\omega') = \omega'\operatorname{Im}H(\omega') - \omega\operatorname{Im}H(\omega)$
the subtraction makes the integrand finite at $\omega' = \omega$, and the omitted
term carries the principal value because
$\mathrm{P.V.}\int_{0}^{\infty}\mathrm{d}\omega'/(\omega'^{2}-\omega^{2}) = 0$.
That identity is the reason the subtraction is legitimate, and it is used again
in [06 Dispersion Relations](./06-dispersion-relations.md).

## 7. Common mistakes

1. **Forgetting the derivative in a higher-order pole.** The residue of a double
   pole is a derivative, not a limit; measure it once with a small contour and
   the error becomes obvious.
2. **Enclosing the wrong poles.** Only singularities *inside* the contour count.
   For a Fourier integral the sign of $\omega$ decides which half plane is
   enclosed, so the answer switches contour when the sign flips.
3. **Closing the contour for an integrand that does not decay.** A polynomial of
   degree $\geq -1$ has no vanishing arc; either subtract the divergent part
   first or use a different method. $\int_{0}^{\infty}\sin x/x$ is of this kind
   and needs the indented contour, not a large semicircle.
4. **Treating the arc as obviously zero.** Section 5: the leading term may
   cancel, and the surviving term has a coefficient you should know.
5. **Assuming a singularity implies a non-zero residue.** $\cos z/(z-\pi/2)$
   integrates to zero around its own pole (Section 2.2).
6. **Using a contour that crosses a branch cut.** $\log z$ and $\sqrt z$ need a
   cut; a contour that crosses it picks up the discontinuity, which is either the
   whole point (keyhole contours) or a fatal error (careless circles).
7. **Reporting a closed form without a quadrature check.** It is cheap; do it.
   Case in point: the integral $\int(x^{2}+1)/(x^{4}+1)\mathrm{d}x$ is
   $\pi\sqrt2$, not $\pi/\sqrt2$, and only the quadrature makes that memorable.

## 8. Real-world applications

- **Green's functions.** The 2-D kernel $(\pi/a)e^{-a|\omega|}$ of Section 4.3,
  and the $1/z$ and $\log z$ potentials of
  [02 Complex Functions](./02-complex-functions.md), are Green's functions
  obtained by residues. Seismic, electromagnetic and potential-field modelling
  all reduce to superpositions of such kernels
  ([01-08-06 Green's
  functions](../08-ordinary-differential-equations/06-green-functions.md)).
- **Dispersion relations.** The Kramers-Kronig relation is a principal-value
  integral of exactly the type in Section 4.4, and the way it is derived is by
  indenting a contour; [06 Dispersion Relations](./06-dispersion-relations.md)
  takes that as its starting point.
- **Inverse Laplace and z-transforms.** Both are contour integrals, and the
  inversion is done by residues; that is the content of
  [04 The Laplace Transform](./04-laplace-transform.md) and
  [05 The z-Transform](./05-z-transform.md).
- **Integrals in spectral estimation.** The smoothness and window leakage of a
  spectral estimate are integrals of a sinc-squared kernel, evaluated by
  residues; the tails matter, as Section 4.3's residual shows
  ([01-10-05 Window
  leakage](../10-fourier-analysis/05-windowing-aliasing.md)).
- **Wave and diffusion kernels.** The reflected/transmitted amplitudes of a
  layered medium come from integrals with poles on the real axis (real
  wavenumbers) and branch points (turning points); the pole/indentation bookkeeping
  is the same as Section 4.4.
- **Stability of numerical schemes.** The von Neumann condition is an integral
  around the unit circle in the complex plane, evaluated by residues
  ([01-09-08 Weak
  solutions](../09-partial-differential-equations/08-weak-solutions.md)).

## 9. Further reading

- **Ahlfors, L. V. (1979). *Complex Analysis* (3rd ed.). McGraw-Hill.**
  Chapters 4–5. Level: graduate. Cauchy's theorem, the integral formula and the
  residue theorem with complete proofs.
- **Carrier, G. F., Krook, M. & Pearson, C. E. (2005). *Functions of a Complex
  Variable*. Society for Industrial and Applied Mathematics.** Level: graduate.
  Written for physicists and engineers; the chapter on evaluating real integrals
  is the most useful 30 pages in the subject.
- **Abramowitz, M. & Stegun, I. A. (1964). *Handbook of Mathematical
  Functions*. NBS Applied Mathematics Series 55.** Chapters 4–5. Level:
  reference. Tables of Fourier, Laplace and complex integrals that residues are
  used to derive.
- **Whittaker, E. T. & Watson, G. N. (1927). *A Course of Modern Analysis*
  (4th ed.). Cambridge University Press.** Chapter 4. Level: graduate. The
  classical derivation of the residue theorem from the Cauchy integral formula.
- **Nayfeh, A. H. (1993). *Introduction to Perturbation Techniques*. Wiley.**
  Chapter 4. Level: graduate. Steepest descent and stationary phase, the
  generalisation of contour integration to the integrals that appear in wave
  asymptotics.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library before citing them.

## 10. Related lessons

- [02 Holomorphic Functions and Cauchy-Riemann
  Equations](./02-complex-functions.md) — the hypothesis of every theorem in this
  lesson.
- [04 The Laplace Transform and Transient
  Problems](./04-laplace-transform.md) — the Bromwich contour, which is this
  lesson applied to $e^{st}$.
- [05 The z-Transform and Discrete Linear
  Systems](./05-z-transform.md) — residues of rational functions in $z$, i.e.
  the impulse response of a digital filter.
- [06 Dispersion Relations and Causality in Wave
  Physics](./06-dispersion-relations.md) — the principal-value integral of
  Section 4.4 as a physical constraint.
- [01-05-06 Improper Integrals, Singularities and
  Convergence](../05-single-variable-calculus/06-improper-integrals.md) — the
  real-analysis statements these computations rely on.
- [01-08-06 Green's Functions](../08-ordinary-differential-equations/06-green-functions.md) —
  the object that most of these integrals represent.

## 11. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/03-contour-integration-exercises.md`](./exercises/03-contour-integration-exercises.md).
Solutions:
[`exercises/03-contour-integration-solutions.md`](./exercises/03-contour-integration-solutions.md).

## Self-assessment checklist

- [ ] I can integrate along a circle and a straight segment by parametrisation.
- [ ] I can state Cauchy's theorem and the Cauchy integral formula and explain
      what each one buys.
- [ ] I can classify an isolated singularity and compute a residue of a simple
      pole and of a pole of any order.
- [ ] I can evaluate a rational integral over the whole line by residues and
      state the degree condition on the arc.
- [ ] I can choose the half plane for a Fourier-type integral and justify it with
      Jordan's lemma.
- [ ] I can handle a simple pole on the path with a principal value and a small
      indentation.
- [ ] I can verify a residue numerically from a small contour and a closed form
      numerically by real quadrature.
- [ ] I can measure the arc contribution and say at what order it decays.
