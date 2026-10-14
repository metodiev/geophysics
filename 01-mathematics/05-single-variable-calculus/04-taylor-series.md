---
id: 01-05-04
title: "Taylor Series, Linearisation and Small-Angle Approximations"
level: intermediate
prereqs: ["01-05-03"]
estimated_minutes: 90
tags: [calculus, taylor-series, linearisation, perturbation]
---

# Taylor Series, Linearisation and Small-Angle Approximations

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Taylor polynomial of a function about a point, together with the
   Lagrange remainder, and state the conditions under which the formula holds.
2. **Derive** the Maclaurin series of $e^{x}$, $\sin x$, $\cos x$, $\ln(1+x)$ and
   $(1+x)^{\alpha}$ from the derivative rules.
3. **Bound** the truncation error of an approximation and decide from that bound
   whether the approximation is fit for a stated purpose.
4. **Quantify** the small-angle approximations: the relative error of
   $\sin\theta \approx \theta$ is $\theta^{2}/6$, so 1 % accuracy requires
   $\theta \lesssim 0.25$ rad.
5. **Linearise** a nonlinear model about a reference state, derive the
   free-air gradient and the parabolic moveout equation, and state where each
   linearisation fails.
6. **Recognise** the failure modes of linearisation: a large expansion parameter,
   a vanishing first derivative, a radius of convergence, and a function that is
   not analytic.

## Prerequisites

[01-05-03 Differentiation Rules and Implicit Differentiation](./03-differentiation-rules.md)
for the derivatives of the elementary functions, and
[01-05-01 Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md)
for asymptotic reasoning. Formal convergence theory for the series used here
appears in [01-05-07](./07-sequences-and-series.md); this lesson uses those
results and flags where they matter.

## 1. Intuition: replace a function by a polynomial you can compute

A Taylor series answers a very practical question: **if I know a function and its
derivatives at one point, how far can I predict it?** The answer is a polynomial
whose coefficients are those derivatives, plus a remainder term that tells you the
error you are incurring.

Almost every "linear" method in geophysics is the first-order Taylor polynomial in
disguise:

| Method | The linearisation |
|---|---|
| Free-air correction | $g(z) \approx g_0(1 - 2z/R)$ |
| Normal moveout | $t(x) \approx t_0 + x^{2}/(2v^{2}t_{0})$ |
| Linearised gravity inversion | $\delta d \approx J\,\delta m$ |
| Refraction with near-vertical rays | $\sin\theta \approx \theta$, so $\theta \approx pv$ |
| Thermal expansion of density | $\rho(T) \approx \rho_0[1 - \alpha(T-T_0)]$ |
| Ray perturbation theory | travel time expanded in a background model |

The reason is not laziness. A linear problem has a solution that can be computed
directly, analysed for uniqueness, and regularised in a well-understood way. A
nonlinear problem generally needs iteration. **Linearisation is how geophysics buys
tractability; the remainder term is the receipt.**

## 2. Precise definitions

### 2.1 Taylor polynomial and Taylor's theorem

Let $f$ have $n+1$ continuous derivatives on an interval containing $a$ and $x$.
Then

$$f(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^{k} + R_n(x),$$

where the **Lagrange remainder** is

$$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

for some $\xi$ between $a$ and $x$. The finite sum is the **Taylor polynomial of
degree $n$**; the infinite sum (when it converges in an interval) is the **Taylor
series**. The case $a = 0$ is called a **Maclaurin series**.

$R_n$ is an *exact* statement, not an estimate: for every $x$ there is a $\xi$
making it true. Because $\xi$ is unknown, in practice you bound $|f^{(n+1)}|$ over
the interval, which turns $R_n$ into a usable error bound.

### 2.2 The linear and quadratic approximations

$$f(x) \approx f(a) + f'(a)(x-a) \quad\text{(linearisation)},$$
$$f(x) \approx f(a) + f'(a)(x-a) + \tfrac{1}{2}f''(a)(x-a)^{2} \quad\text{(second order)}.$$

The **expansion variable** $x - a$ must be dimensionless, or every term must be
interpreted with the units it carries. A quantity like "the depth in metres" cannot
be small; the dimensionless ratio $\delta z/z_0$ can.

### 2.3 The standard Maclaurin series

$$e^{x} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots, \qquad |x| < \infty,$$
$$\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \cdots, \qquad |x| < \infty,$$
$$\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \cdots, \qquad |x| < \infty,$$
$$\ln(1+x) = x - \frac{x^{2}}{2} + \frac{x^{3}}{3} - \cdots, \qquad -1 < x \le 1,$$
$$(1+x)^{\alpha} = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^{2} + \cdots, \qquad |x| < 1.$$

For an alternating series with decreasing terms, truncating after a term whose sign
matches the first omitted term leaves an error no larger than the first omitted
term — the **alternating series error bound**, which is proved in
[01-05-07](./07-sequences-and-series.md).

## 3. Step-by-step derivations

### 3.1 Deriving the Maclaurin series of $\sin x$

Evaluate the derivatives at $0$:

$$f = \sin x \Rightarrow f(0) = 0, \quad
f' = \cos x \Rightarrow f'(0) = 1, \quad
f'' = -\sin x \Rightarrow f''(0) = 0,$$
$$f''' = -\cos x \Rightarrow f'''(0) = -1, \quad
f^{(4)} = \sin x \Rightarrow f^{(4)}(0) = 0,$$

and the pattern repeats with period 4. Only odd powers survive, with alternating
signs, so $\sin x = x - x^{3}/3! + x^{5}/5! - \cdots$. The same computation for
$\cos x$ gives $1 - x^{2}/2! + x^{4}/4! - \cdots$. The coefficients are *forced*:
a polynomial matching $f$ and its first $n$ derivatives at $a$ is unique, so there
is no freedom in the expansion — which is why every calculus text gets the same
answer.

### 3.2 How many terms? A worked truncation budget

The script sums the terms of $\sin(0.5)$ one at a time:

| terms retained | partial sum | error | first omitted term |
|---|---|---|---|
| $x$ | `0.50000000000000000` | `2.057e-02` | `2.083e-02` |
| $x - x^{3}/3!$ | `0.47916666666666669` | `2.589e-04` | `2.604e-04` |
| $+x^{5}/5!$ | `0.47942708333333334` | `1.545e-06` | `1.550e-06` |
| $+x^{7}/7!$ | `0.47942553323412701` | `5.370e-09` | `5.382e-09` |
| $+x^{9}/9!$ | `0.47942553861641590` | `1.221e-11` | — |

Note how sharply the error tracks the first omitted term: the bound is not
pessimistic here, it is nearly exact, which is what the alternating series bound
promises. Each added pair of terms multiplies the error by about
$x^{2}/((k+1)(k+2))$: at $x = 0.5$ that is $1/79$, then $1/167$, then $1/279$.
**Taylor series converge fast or they do not converge at all**; there is no slow
middle ground inside the radius of convergence.

### 3.3 Small angles: $\sin\theta \approx \theta$, and its error

From the series, write $\sin\theta = \theta(1 - \theta^{2}/6 + \cdots)$, so

$$\frac{\theta - \sin\theta}{\sin\theta} \approx \frac{\theta^{2}}{6} .$$

The script tabulates both sides:

| $\theta$ | $\theta$ (rad) | $\sin\theta$ | relative error | $\theta^{2}/6$ |
|---|---|---|---|---|
| 0.1° | 0.0017453 | 0.0017453284 | `5.0770e-07` | `5.0770e-07` |
| 1° | 0.0174533 | 0.0174524064 | `5.0771e-05` | `5.0770e-05` |
| 10° | 0.1745329 | 0.1736481777 | `5.0951e-03` | `5.0770e-03` |
| 30° | 0.5235988 | 0.5000000000 | `4.7198e-02` | `4.5693e-02` |
| 60° | 1.0471976 | 0.8660254038 | `2.0920e-01` | `1.8277e-01` |

Read the table as a decision rule:

- $\theta \le 5°$: error below 0.13 %, safe for almost any purpose.
- $\theta \approx 14°$ ($= 0.25$ rad): error about 1 %. **This is the boundary of
  "small".**
- $\theta \ge 30°$: error above 4 %, and the $\theta^{2}/6$ estimate itself is
  becoming unreliable (it is 3 % off at $30°$ and 14 % off at $60°$).

For $\cos$ the analogous results are $\cos\theta = 1 - \theta^{2}/2 + \theta^{4}/24 - \cdots$
and a relative error of $\theta^{2}/6$ for the *second-order* approximation; the
cruder $\cos\theta \approx 1$ has relative error $\theta^{2}/2$, three times worse.
The script's $\cos$ table shows the second-order form holding to `3.9e-05` at $10°$
and to `9.7e-02` at $60°$, where it is useless.

### 3.4 Free-air gradient as a binomial expansion

Write $g(z) = g_0(1+u)^{-2}$ with $u = z/R$ and expand:

$$(1+u)^{-2} = 1 - 2u + 3u^{2} - 4u^{3} + \cdots
\quad\Longrightarrow\quad
g(z) \approx g_0\left(1 - \frac{2z}{R}\right),$$

hence $dg/dz = -2g_0/R$. With $g_0 = 9.80665\ \mathrm{m\,s^{-2}}$ and
$R = 6.371\times10^{6}$ m, the script prints $-0.3079\ \mathrm{mGal\,m^{-1}}$; with
the round mass and radius used in [01-05-02](./02-derivatives.md) it prints
$-0.3083\ \mathrm{mGal\,m^{-1}}$. The standard quoted free-air gradient,
$0.3086\ \mathrm{mGal\,m^{-1}}$, is the ellipsoidal value and differs in the third
decimal.

**How large is the neglected term?** At a height of 1 km, $u = 1.57\times10^{-4}$
and $3u^{2} = 7.4\times10^{-8}$: the quadratic correction is irrelevant. At the
altitude of a low Earth orbiter, $z = 400$ km, $u = 0.063$ and $3u^{2} = 0.012$ —
still small. At $z = R$ the expansion diverges, which is a statement about the
*series*, not about the physics: gravity is perfectly well defined above
$z = R$, but this particular expansion about $z=0$ is not. The singularity that
limits the radius of convergence is at the Earth's centre.

### 3.5 The Bouguer slab: a linearisation that is exact

The vertical field of an infinite slab of density $\rho$ and thickness $h$ is

$$g_z = 2\pi G \rho h .$$

This is linear in $h$ — not as an approximation but exactly, which is why the
Bouguer correction is a multiplication. Converting to the practical units used in
field work,

$$2\pi G \rho = 2\pi (6.674\times10^{-11})(2670)\ \mathrm{s^{-2}}
= 1.1196\times10^{-6}\ \mathrm{s^{-2}} = 0.11196\ \mathrm{mGal\,m^{-1}},$$

and the traditional coefficient form $0.04193\,\rho\,h$ with $\rho$ in
g/cm³ and $h$ in m gives $0.04193 \times 2.67 = 0.11195\ \mathrm{mGal\,m^{-1}}$,
agreeing to five figures. **Labelling the Bouguer correction a "linearisation" is a
misnomer**; the approximation is the assumption of an infinite flat slab, and the
error from that assumption is what the terrain correction removes.

### 3.6 Normal moveout: exact hyperbola, approximate parabola

For a single layer the reflection travel time is *exactly*

$$t(x) = \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}} = t_0\sqrt{1+u}, \qquad u = \left(\frac{x}{v t_0}\right)^{2} .$$

Expanding $\sqrt{1+u} = 1 + u/2 - u^{2}/8 + u^{3}/16 - \cdots$ gives the
**parabolic (small-offset) moveout equation**

$$t(x) \approx t_0\left(1 + \frac{u}{2}\right) = t_0 + \frac{x^{2}}{2v^{2}t_0},$$

with relative error

$$\frac{t_{\text{par}} - t_{\text{exact}}}{t_{\text{exact}}}
= \frac{u^{2}/8 - u^{3}/16 + \cdots}{\sqrt{1+u}} \approx \frac{u^{2}}{8} .$$

The script evaluates this for $v = 2000$ m/s and $t_0 = 1$ s:

| $x$ (m) | $t$ exact (s) | $t$ parabolic (s) | relative error | $u$ |
|---|---|---|---|---|
| 100 | 1.001249220 | 1.001250000 | `7.793e-07` | 0.0025 |
| 500 | 1.030776406 | 1.031250000 | `4.595e-04` | 0.0625 |
| 1000 | 1.118033989 | 1.125000000 | `6.231e-03` | 0.25 |
| 2000 | 1.414213562 | 1.500000000 | `6.066e-02` | 1.0 |
| 3000 | 1.802775638 | 2.125000000 | `1.787e-01` | 2.25 |

At $u = 0.0625$ the leading term predicts $u^{2}/8 = 4.88\times10^{-4}$ against an
observed `4.595e-04`: the next term $-u^{3}/16 = -1.53\times10^{-5}$ and the factor
$1/\sqrt{1+u}$ account for the difference. By $u = 1$ — offset equal to $v t_0$,
that is, offset comparable with reflector depth — the "approximation" is wrong by
6 %, and by $u = 2.25$ it is wrong by 18 %. **NMO velocity analysis is a
small-offset method, and long-offset data must be handled with higher-order
moveout terms.**

### 3.7 Linearising a gravity perturbation, and its error

Let $g(d) = GM/d^{2}$ and perturb the depth by $\delta d$:

$$g(d+\delta d) = \frac{GM}{d^{2}}(1+u)^{-2} = g(d)\left(1 - 2u + 3u^{2} - \cdots\right),
\qquad u = \frac{\delta d}{d} .$$

The linearised perturbation is $\delta g \approx -2g(d)\,u$, and the relative error
of that linearisation is $-3u^{2}$. The script confirms both lines:

| $d$ (m) | $\delta d$ (m) | $u$ | observed relative error | $-3u^{2}$ |
|---|---|---|---|---|
| 100 | 1 | 0.010 | `-3.020e-04` | `-3.000e-04` |
| 100 | 5 | 0.050 | `-7.750e-03` | `-7.500e-03` |
| 500 | 1 | 0.002 | `-1.202e-05` | `-1.200e-05` |
| 500 | 5 | 0.010 | `-3.020e-04` | `-3.000e-04` |

The pattern is the one to remember: **a 1 % perturbation buys about three parts in
$10^{4}$ of linearisation error.** A perturbation of the model variable, not the
size of the data set, is what invalidates a linearisation.

### 3.8 Where the linearised inverse problem comes from

Write a forward model as $\mathbf{d} = F(\mathbf{m})$ and expand about a reference
model $\mathbf{m}_0$:

$$\mathbf{d} = F(\mathbf{m}_0) + J\,(\mathbf{m} - \mathbf{m}_0) + O(\|\mathbf{m}-\mathbf{m}_0\|^{2}),
\qquad J_{ij} = \frac{\partial F_i}{\partial m_j}\bigg|_{\mathbf{m}_0} .$$

Dropping the quadratic term gives the linear system

$$\delta\mathbf{m} = J^{-1}\bigl(\mathbf{d} - F(\mathbf{m}_0)\bigr),$$

which is the step in Gauss–Newton iteration. Whether it is a legitimate
linearisation is decided by the size of the neglected term relative to the data
uncertainty — the same test performed in Section 3.7. When the Jacobian is
ill-conditioned or rank-deficient, the inverse must be replaced by a
regularised (or pseudo-) inverse; that is the subject of
[01-07-08 SVD](../07-linear-algebra/08-svd.md) and
[18-inverse-problems](../../18-inverse-problems/README.md).

## 4. Physical interpretation

**The expansion parameter must be small — and dimensionless.** "Small" always
means small relative to the reference scale: $z/R$, $x/(v t_0)$, $\theta$,
$\delta m/m$. If you cannot write the parameter as a ratio of two like quantities,
your expansion is dimensionally inconsistent and the coefficients are meaningless.

**Truncation is a modelling decision.** Keeping the linear term and dropping the
quadratic is a statement that the quadratic term is below the noise. Write the
bound down; do not assume it.

**Radius of convergence is a physical warning.** The expansion of $g(z)$ about the
surface fails at $z = R$ because the singularity of the point-mass model is at the
centre. When an expansion misbehaves, look for the singularity it is approaching —
it usually identifies a feature of the model (a point source, a layer boundary, a
resonance) rather than a defect of the mathematics.

**Analyticity is an assumption.** The function $f(x) = e^{-1/x^{2}}$ for $x \ne 0$,
$f(0) = 0$, has $f^{(k)}(0) = 0$ for every $k$, so its Taylor series at $0$ is
identically zero, yet the function is not. Taylor series describe *analytic*
functions, and not every smooth function is analytic. Physical fields are usually
analytic where they are smooth, but the counter-example is worth knowing because it
shows that "all derivatives exist" is not sufficient.

**Asymptotic series are allowed to diverge.** Expansions in a large parameter,
such as $1/x$ for a distant source, often have zero radius of convergence and are
still enormously useful when truncated at the smallest term. Every multipole
expansion used in potential fields is of this kind. This lesson treats the
convergent case; the divergent-but-useful case is flagged again in
[01-05-07](./07-sequences-and-series.md).

## 5. Python demonstration

The companion script is
[`code/taylor_linearisation_demo.py`](./code/taylor_linearisation_demo.py). It
contains eight sections, one per approximation discussed above. The core pattern is

```python
terms = [0.5, -(0.5 ** 3) / 6.0, (0.5 ** 5) / 120.0,
         -(0.5 ** 7) / 5040.0, (0.5 ** 9) / 362880.0]
total = 0.0
for index, term in enumerate(terms):
    total += term
    print(f"{2 * index + 1:>7}  {total:>22.17f}  {abs(total - math.sin(0.5)):>12.3e}")
```

Observed output for $\sin(0.5)$ (exact value `0.479425538604203`):

| order | partial sum | error | first omitted term |
|---|---|---|---|
| 1 | `0.50000000000000000` | `2.057e-02` | `2.083e-02` |
| 3 | `0.47916666666666669` | `2.589e-04` | `2.604e-04` |
| 5 | `0.47942708333333334` | `1.545e-06` | `1.550e-06` |
| 7 | `0.47942553323412701` | `5.370e-09` | `5.382e-09` |
| 9 | `0.47942553861641590` | `1.221e-11` | — |

The other sections reproduce the tables in Section 3. Two entries are worth
quoting because they are the sort of number that gets misquoted in the
literature:

| Section | Observed | Comment |
|---|---|---|
| 4, free-air gradient | `-2 g0 / R = -3.082572e-06 m/s^2 per m = -0.3083 mGal/m` | the spherical model; the standard ellipsoidal value is 0.3086 |
| 5, Bouguer slab | `2 pi G rho = 0.11196 mGal/m` vs `0.04193*rho = 0.11195` | two independent routes to the same coefficient |
| 7, linearised gravity | relative error `-3.020e-04` against `-3u^2 = -3.000e-04` at $u = 0.01$ | the $3u^{2}$ law |
| 8, $\ln(1+x)$ | at $x = 0.1$, ten terms give `0.095310179803492` (error `8.3e-13`); at $x = 1$, ten terms give `0.645634920634921` (error `4.8e-02`) | inside the radius of convergence, fast; at its edge, slow |

The last row is the bridge to [01-05-07](./07-sequences-and-series.md): the series
for $\ln(1+x)$ converges at $x = 1$ but only like $1/n$, so ten terms are worthless
there and ten terms are everything at $x = 0.1$.

> **Breaking exercise.** Section 6 uses $v = 2000$ m/s, $t_0 = 1$ s. Predict the
> offset at which the parabolic moveout error reaches 1 %, then run the script to
> check. Then state the corresponding condition on the *depth* of the reflector,
> remembering that $t_0 = 2h/v$.

## 6. Exercises

Full set and worked solutions:
[`exercises/04-taylor-series-exercises.md`](./exercises/04-taylor-series-exercises.md)
and [`exercises/04-taylor-series-solutions.md`](./exercises/04-taylor-series-solutions.md).
Four to start with:

**★1.** Write the Maclaurin series to four nonzero terms and state the radius of
convergence: (a) $e^{-x}$, (b) $\cos(2x)$, (c) $\ln(1+x)$, (d) $(1+x)^{-1}$.

**★2.** Use the linearisation about $x = 0$ to estimate
$\sqrt{1.02}$ and $\sin(0.05)$. Bound the error with the Lagrange remainder in
each case, and compare your bound with the true error.

**★★3.** A gravity anomaly from a point mass of $10^{10}$ kg is measured at
$d = 500$ m with a relative precision of $10^{-3}$. Using the result of
Section 3.7, what uncertainty in $d$ does a linearised interpretation support?
Is a linearised inversion with perturbation $u = 0.05$ consistent with that
precision?

**★★4.** A wave speeds up as it propagates: $v(s) = v_0 + \alpha s$ with
$s$ the path length. (a) Expand the travel time $t = \int ds/v(s)$ to first order
in $\alpha s/v_0$ and obtain the correction to the straight-ray travel time.
(b) State the dimensionless expansion parameter and the range over which the
result is useful. This is the first-order perturbation method used in ray
tomography.

**★★★5.** The NMO expansion of Section 3.6 was truncated after the $u/2$ term.
Carry the expansion to order $u^{2}$ and show that the resulting expression for
$t(x)$ includes a term in $x^{4}$. Estimate the offset at which the $x^{4}$ term
becomes as large as a 1 % timing error for $v = 2000$ m/s, $t_0 = 1$ s, and
compare with the script's table. Report the method, the result, and the limits of
your conclusion.

## 7. Common mistakes

1. **Expanding in a dimensional quantity.** "$z$ is small" is meaningless;
   "$z/R = 0.01$" is a statement. Always name the dimensionless ratio.
2. **Forgetting the remainder.** An approximation without an error bound is a
   guess. Use the Lagrange form and bound the derivative on the interval.
3. **Using a first-order approximation where the first derivative vanishes.**
   At a maximum, minimum or inflection of the expansion variable, the linear term
   is zero and the quadratic term governs; the linearisation is not merely
   inaccurate, it gives no information.
4. **Ignoring the radius of convergence.** The binomial expansion of
   $(1+z/R)^{-2}$ is invalid for $z > R$; expansions of $\ln(1+x)$ fail for
   $x > 1$. The failure is a property of the series, and it always has a cause.
5. **Believing that a Taylor series always converges to its function.** It does not
   for non-analytic smooth functions such as $e^{-1/x^{2}}$.
6. **Confusing the exact moveout hyperbola with the parabolic approximation.**
   For a single layer the hyperbola is exact; the parabola is the approximation.
   In a layered medium neither is exact.
7. **Assuming a linearised inversion is valid because the data are small.**
   Validity depends on the *model perturbation*, through $u = \delta m/m_0$, not on
   the size of the residual.
8. **Quoting the free-air gradient to five figures.** The spherical model gives
   0.3083 mGal/m and the ellipsoidal value 0.3086 mGal/m; the third decimal is
   where the Earth's shape enters.

## 8. Real-world applications

- **Gravity reduction.** Free-air and Bouguer corrections are a Taylor expansion in
  height plus an exact slab formula; the residual is what an interpreter reads.
  See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Seismic velocity analysis.** Semblance and NMO stacking assume the parabolic or
  hyperbolic moveout of Section 3.6. Modern long-offset surveys use higher-order
  and anisotropic moveout equations because $u$ is not small. See
  [11-exploration-geophysics](../../11-exploration-geophysics/README.md) and
  [06-seismology](../../06-seismology/README.md).
- **Ray perturbation theory.** Travel-time anomalies are linear functionals of
  slowness perturbations along the unperturbed ray, which is why tomographic
  inversions are written as linear systems. See
  [06-seismology](../../06-seismology/README.md).
- **Linearised inverse problems.** Almost every practical inversion begins with
  $\delta\mathbf{d} = J\,\delta\mathbf{m}$ and iterates. See
  [18-inverse-problems](../../18-inverse-problems/README.md).
- **Refraction at near-vertical incidence.** Small-angle approximations convert
  Snell's law into a linear relation between offset and ray parameter, the basis
  of the classical refraction interpretation.
- **Thermal and elastic equations of state.** Density and velocity are linearised
  in temperature and pressure because the perturbations are small — except in
  problems such as mantle convection, where they are not, and the linearisation
  must be justified explicitly.

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 19–20.
  Level: beginner upward. Taylor's theorem with the Lagrange remainder, proved.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapters 7–8.
  Level: beginner to intermediate. Power series and the theory of convergence
  radius.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd ed.).
  Wiley.** Chapters 1 and 11. Level: beginner. Series expansions with the physical
  applications attached.
- **Turcotte, D. L. & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Level: intermediate. Perturbation and boundary-layer methods
  in mantle dynamics, all built on the expansions of this lesson.
- **Stein, S. & Wysession, M. (2003). *An Introduction to Seismology, Earthquakes,
  and Earth Structure*. Blackwell.** Chapters 2–4. Level: beginner to intermediate.
  Moveout, ray parameters and the small-angle regime.
- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Volume 1, Chapter 3. Level: intermediate to advanced. Normal
  moveout and its higher-order corrections as used in processing.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Chapter 5. Level: advanced. Linearisation, the Jacobian, and
  the conditions under which a linearised inversion is honest.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not reproduce copyrighted text; confirm editions and
> availability through your library before citing them. Chapter references are
> indicative rather than authoritative: editions differ in numbering and content,
> so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can state Taylor's theorem with the Lagrange remainder and name the
      conditions on $f$.
- [ ] I can derive the Maclaurin series of $e^{x}$, $\sin x$, $\cos x$ and
      $\ln(1+x)$ and state each radius of convergence.
- [ ] I can quote the relative error of $\sin\theta \approx \theta$ and pick a
      maximum angle for a required accuracy.
- [ ] I can derive the free-air gradient from the binomial expansion and estimate
      the size of the neglected quadratic term at a stated height.
- [ ] I can derive the parabolic moveout equation and say at which offset it stops
      being adequate.
- [ ] I can linearise a nonlinear forward model, write the Jacobian, and quantify
      the neglected term as $3u^{2}$ for a $1/d^{2}$ law.
- [ ] I can name at least three ways a Taylor approximation fails, with an example
      of each.

## 11. Related lessons

- [01-05-03 Differentiation Rules and Implicit Differentiation](./03-differentiation-rules.md) —
  the derivatives that supply the coefficients.
- [01-05-02 Derivatives and Rates of Change](./02-derivatives.md) — the truncation
  errors of finite differences, which are Taylor remainders.
- [01-05-05 Integration Techniques and Definite Integrals](./05-integration.md) —
  the same expansions applied inside integrals, especially for perturbations.
- [01-05-07 Sequences, Series and Convergence Tests](./07-sequences-and-series.md) —
  the convergence theory behind the radius of convergence used here.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  Taylor expansion in several variables, where the Jacobian appears.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../07-linear-algebra/08-svd.md) —
  what to do when the linearised inverse cannot be formed.
- [18-inverse-problems](../../18-inverse-problems/README.md) — linearisation in
  practice, including when to stop trusting it.
