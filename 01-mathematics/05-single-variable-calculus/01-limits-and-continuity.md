---
id: 01-05-01
title: "Limits, Continuity and the Idea of Approximation"
level: beginner
prereqs: ["01-01-01", "01-02-02"]
estimated_minutes: 90
tags: [calculus, limits, continuity, asymptotics]
---

# Limits, Continuity and the Idea of Approximation

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the $\varepsilon$–$\delta$ definition of a limit and use it to say
   precisely what "the mesh is fine enough" means in a numerical model.
2. **Evaluate** one-sided limits and decide whether a limit exists at a point
   where a model changes character.
3. **Classify** a discontinuity as removable, jump or infinite, and say what
   each implies for a ray, a potential or a solver.
4. **Determine** the leading asymptotic behaviour of a geophysical quantity as a
   parameter tends to infinity, and the rate of approach to that limit.
5. **Explain** why a floating-point evaluation of $\sin(x)/x$ returns exactly
   $1.0$ for $x = 10^{-8}$ and why that is a property of the arithmetic, not of
   the mathematics.
6. **Use** the limit definition to differentiate a function from first
   principles, which is the bridge to lesson 01-05-02.

## Prerequisites

[01-01-01 Number Systems, Precision and Scientific Notation](../01-arithmetic/01-number-systems-and-precision.md)
for the floating-point floor and for the habit of stating precision honestly, and
[01-02-02 Functions, Graphs and Transformations](../02-algebra/02-functions-and-graphs.md)
for the language of functions, domains and ranges. Nothing here assumes that you
have seen calculus before.

## 1. Intuition: every idealisation is a limit

Geophysics is built out of idealisations, and each one is a limit:

| Idealisation | Limiting statement |
|---|---|
| Point mass in a gravity model | body size $\to 0$ with mass fixed |
| Plane wave | distance $\to \infty$ from the source |
| Half-space | layer thickness $\to \infty$ |
| Seismic ray | frequency $\to \infty$, wavelength $\to 0$ |
| Thin sheet approximation | sheet thickness $\to 0$ with mass per area fixed |
| "The inversion converged" | iteration count $\to \infty$ (or residual $\to 0$) |

A limit is therefore not a technicality bolted onto calculus. It is the language
in which an approximation is stated, and the only way to say *how good* the
approximation is. "A point mass fits the data" is useless; "a point mass fits the
data to better than 1 %, because the body is 20 times smaller than its depth" is
a statement about a limit and its rate.

That last phrase — **and its rate** — is what separates useful mathematics from
formal mathematics. Throughout this module you will meet the same pattern: a
quantity $Q(\lambda)$ depending on a small parameter $\lambda$, a limit
$Q_0$, and an error term. The limit tells you the idealisation is legitimate in
principle; the error term tells you whether it is legitimate at the parameter
values you actually have.

## 2. Precise definitions

### 2.1 The limit of a function

Informally, $L$ is the **limit** of $f(x)$ as $x$ approaches $a$ if $f(x)$ can be
made as close to $L$ as we please by taking $x$ close enough to $a$, *without
requiring $f(a)$ itself to exist*.

Formally,

$$\lim_{x\to a} f(x) = L \iff \forall \varepsilon > 0\ \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon .$$

Read the quantification carefully: your adversary chooses the tolerance
$\varepsilon$, you reply with a distance $\delta$. The order is the content of the
definition, and it is exactly the order in a convergence criterion of a numerical
solver: "for any accuracy you demand, I can supply a grid spacing that delivers
it."

### 2.2 One-sided limits, and limits at infinity

- $x \to a^{+}$ means $x > a$; $x \to a^{-}$ means $x < a$.
- $\lim_{x\to a} f(x)$ **exists** if and only if both one-sided limits exist and
  are equal.
- $\lim_{x\to\infty} f(x) = L$ means: for every $\varepsilon > 0$ there is an $X$
  such that $x > X \implies |f(x) - L| < \varepsilon$.

### 2.3 Continuity

$f$ is **continuous at** $a$ if $\lim_{x\to a} f(x) = f(a)$: the limit exists, the
value exists, and they agree. Continuity on an interval means continuity at every
interior point, with the appropriate one-sided versions at the endpoints.

A discontinuity is one of three kinds:

| Kind | Behaviour at $a$ | Geophysical example |
|---|---|---|
| Removable | limit exists, but $\neq f(a)$ or $f(a)$ undefined | density defined with a typo at one depth |
| Jump | both one-sided limits exist and differ | Moho, sediment–basement contact |
| Infinite | $|f| \to \infty$ | $1/r$ potential at a point source |

### 2.4 Tools for computing limits

1. **Direct substitution** whenever the function is continuous there.
2. **Algebraic rearrangement** to cancel a common factor (the standard treatment
   of $0/0$).
3. **The squeeze theorem**: if $g(x) \le f(x) \le h(x)$ and both $g$ and $h$ tend
   to $L$, then $f$ tends to $L$.
4. **L'Hôpital's rule**: if $f$ and $g$ are differentiable near $a$, $g'(x) \neq 0$
   nearby, and $f, g$ both tend to $0$ or both to $\pm\infty$, then
   $\lim f/g = \lim f'/g'$ *provided the latter limit exists*. It is a
   convenience, never a licence to differentiate blindly.

### 2.5 Asymptotic notation

- $f(x) \sim g(x)$ as $x \to \infty$ means $f/g \to 1$.
- $f(x) = O(g(x))$ means $|f/g|$ is bounded.
- The **leading-order behaviour** is the surviving term as a parameter becomes
  extreme. In geophysics the extreme parameter is usually depth, distance,
  frequency, time or iteration count.

## 3. Worked derivations

### 3.1 $\displaystyle\lim_{x\to 0}\frac{\sin x}{x} = 1$, by squeezing

Consider $0 < x < \pi/2$ and the three regions of the unit circle: the triangle
with vertices $(0,0)$, $(1,0)$, $(\cos x, \sin x)$; the circular sector between
angles $0$ and $x$; and the right triangle with vertices $(0,0)$, $(1,0)$,
$(1, \tan x)$. Comparing areas,

$$\tfrac{1}{2}\sin x \;\le\; \tfrac{1}{2}x \;\le\; \tfrac{1}{2}\tan x .$$

Drop the factor $\tfrac12$, divide through by $\sin x$ (positive for $0<x<\pi/2$),
and invert:

$$\cos x \le \frac{\sin x}{x} \le 1 .$$

Both bounds tend to $1$ as $x \to 0^{+}$, so the squeeze theorem gives
$\sin x / x \to 1$; the function is even, so the same holds from the left. This
single limit is the source of the small-angle approximation $\sin\theta \approx
\theta$ that underpins ray theory, and it is revisited quantitatively in
[01-05-04](./04-taylor-series.md).

### 3.2 The same limit by L'Hôpital, and why the squeeze was better

Numerator and denominator both tend to $0$, so l'Hôpital applies:

$$\lim_{x\to0}\frac{\sin x}{x} = \lim_{x\to0}\frac{\cos x}{1} = 1 .$$

The manipulation is shorter, but it is circular if used carelessly: the standard
proof that $\frac{d}{dx}\sin x = \cos x$ already uses this very limit. The squeeze
proof stands on geometry alone. **Use l'Hôpital to check, not to establish.**

### 3.3 $\displaystyle\lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^{n} = e$

Expand by the binomial theorem:

$$\left(1+\frac{1}{n}\right)^{n} = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^{k}} = \sum_{k=0}^{n}\frac{1}{k!}\prod_{j=1}^{k-1}\left(1-\frac{j}{n}\right).$$

For fixed $k$, every factor in the product tends to $1$ as $n \to \infty$, so each
term tends to $1/k!$ and the sum tends to $\sum_{k\ge0}1/k! = e$. The sequence is
increasing and bounded, so the limit exists and equals $e = 2.718281828\ldots$.
This is the limit behind every exponential decay law in Earth science — geothermal
cooling, radiometric dating, seismic attenuation — and it is why $e$ rather than
$10$ appears in decay constants.

### 3.4 Limit at infinity: a finite body looks like a point mass

For a thin uniform disc of mass $M$ and radius $a$, the gravitational potential on
the axis at distance $z$ is

$$V(z) = \frac{2GM}{a^{2}}\left(\sqrt{a^{2}+z^{2}} - z\right).$$

That bracket suffers catastrophic cancellation for large $z$, so rationalise it:

$$\sqrt{a^{2}+z^{2}} - z = \frac{a^{2}}{\sqrt{a^{2}+z^{2}} + z},
\qquad\text{so}\qquad
V(z) = \frac{2GM}{\sqrt{a^{2}+z^{2}} + z}.$$

Now write $u = a/z$ and factor out the point-mass potential $GM/z$:

$$V(z) = \frac{GM}{z}\cdot\frac{2}{\sqrt{1+u^{2}}+1}
\;\approx\; \frac{GM}{z}\left(1 - \frac{u^{2}}{4}\right)
= \frac{GM}{z}\left(1 - \frac{a^{2}}{4z^{2}}\right).$$

The limit is the point-mass potential, and the approach is **second order in**
$a/z$: at $z = 10a$ the fractional error is about $2.5\times10^{-3}$, at
$z = 100a$ about $2.5\times10^{-5}$. Both figures are confirmed by the table in
Section 5.

This has a hard geophysical consequence. Because every compact body's field tends
to that of a point mass at large distance, the far field of a gravity survey
constrains the *mass* of an anomaly but not its shape. Shape information lives in
the higher-order terms — which is precisely why potential-field interpretation
requires data close to the source, and why a depth–shape trade-off exists at all.

### 3.5 A limit that does not exist: the Moho as a velocity jump

Take a first-order model with $v = 6.0$ km/s above 33 km depth and $v = 8.0$ km/s
below it (ILLUSTRATIVE round values). At $z_0 = 33$ km,

$$\lim_{z\to z_0^{-}} v(z) = 6.0, \qquad \lim_{z\to z_0^{+}} v(z) = 8.0,$$

so the two-sided limit does not exist and the model has a **jump discontinuity**
of 2.0 km/s. The mathematics is not an inconvenience; it is the statement that a
ray reaching $z_0$ meets a change of medium, producing reflected and transmitted
branches. Replace the jump by a ramp of width $w$ and the limit at $z_0$ exists and
equals the midpoint of the ramp — the table in Section 5 shows $7.000$ km/s for a
smoothed model.

The practical rule: **a discontinuity in a model is a limit statement. Decide
whether you mean it, and if you do not, replace it with the ramp that your data
can actually resolve.**

## 4. Physical interpretation

**Singularities versus integrable singularities.** The potential of a point mass,
$-GM/r$, is unbounded as $r\to0$: an infinite discontinuity. Yet the potential of a
*finite* body is finite everywhere outside the body, because the volume of material
within distance $r$ grows like $r^{3}$ and its contribution per unit volume falls
only like $1/r$. The weighting $4\pi r^{2}$ beats the $1/r$ singularity, so
$4\pi r^{2}\cdot(1/r) = 4\pi r \to 0$. Whether a singularity destroys a physical
quantity is a question about the weight attached to it, which is the subject of
[01-05-06](./06-improper-integrals.md).

**Singularities as pointers to model failure, not to bad arithmetic.** A solver
that reports an infinite value at the surface of a model body is telling you that
your model has a point source where reality has a distributed one. The physics fix
is to spread the source; the mathematics fix is to use the integral formulation.

**Rate of convergence is the engineering content.** A residual that decays as
$1/n$ needs ten times the work for one more digit; one that decays geometrically
needs a fixed amount of work per digit. Lessons [01-05-07](./07-sequences-and-series.md)
and [01-05-04](./04-taylor-series.md) make this quantitative, and
[01-12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md)
turns it into solver design.

## 5. Python demonstration

The companion script is
[`code/limits_demo.py`](./code/limits_demo.py). It probes six limits numerically.
Run it and predict each table before reading it.

The central experiment is the numerical evaluation of $\sin(x)/x$ for shrinking
$x$:

```python
for exponent in range(1, 17):
    x = 10.0 ** (-exponent)
    ratio = math.sin(x) / x
    print(f"{x:>10.0e}  {ratio!r:>22}  {1.0 - ratio:>14.3e}")
```

Observed output (Python 3.14, IEEE-754 binary64):

| $x$ | $\sin(x)/x$ | $1 - \sin(x)/x$ |
|---|---|---|
| `1e-01` | `0.9983341664682815` | `1.666e-03` |
| `1e-05` | `0.9999999999833332` | `1.667e-11` |
| `1e-07` | `0.9999999999999983` | `1.665e-15` |
| `1e-08` | `1.0` | `0.000e+00` |
| `1e-16` | `1.0` | `0.000e+00` |

Two facts are worth extracting.

First, the deviation falls as $x^{2}/6$: at $x = 10^{-5}$ it is
$1.667\times10^{-11}$ and $x^{2}/6 = 1.667\times10^{-11}$. That is the leading
Taylor term of $\sin x$, not a numerical artefact.

Second, the trend *stops* at $x = 10^{-8}$ and the computed ratio becomes exactly
$1.0$. The reason is in the same Taylor expansion: $\sin x = x - x^{3}/6+\cdots$, so
$\sin x$ differs from $x$ by a relative amount $x^{2}/6$. Below
$x \approx \sqrt{6\varepsilon} = \sqrt{6\times2.22\times10^{-16}} \approx 3.6\times10^{-8}$
that difference is smaller than the machine epsilon
$\varepsilon \approx 2.22\times10^{-16}$, so `math.sin(x)` returns exactly `x` and
the ratio is exactly `1.0`. **The limit is a statement about all $x>0$; the
computation can only confirm it down to the arithmetic's floor** — the same floor
studied in
[01-04 Floating-Point Representation](../01-arithmetic/04-floating-point.md).

Other sections of the script confirm the analysis above:

| Script section | Observed | Interpretation |
|---|---|---|
| 2, $(1+1/n)^{n}$ | `n=10` → `2.5937424601`, `n=10**8` → `2.7182817983` | convergence to $e$ is slow: error $\approx 1/(2n)$ |
| 3, jump at the Moho | `v(z0-h)=6.0000`, `v(z0+h)=8.0000` for every $h$ | one-sided limits differ by exactly the jump, for every $h$ |
| 3, smoothed model | `z0` → `7.000000` km/s, $z_0 \pm 10^{-6}$ km → `7.005`/`6.995` | the ramp gives a genuine two-sided limit |
| 4, disc potential | rel. difference `-2.488e-03` at $z = 10^4$ m ($a=10^3$ m) | second-order approach, $-u^{2}/4$ with $u = 0.1$ |
| 5, naive vs stable disc form | `z=1e11` m: naive `0.0`, stable `6.674e-12` | the limit is real; the naive formula is not |
| 6, $4\pi r^{2}\cdot(1/r)$ | `r=1e-6` m → `4\pi r^{2}/r = 1.000e-06` m | the weighting defeats the singularity |

> **Breaking exercise.** Before running Section 2, predict the value of
> $n = 10^{8}$ from the asymptotic error $1/(2n)$. Then run it. The prediction
> $2.7182818235$ against the observed `2.7182817983` is off in the seventh digit:
> explain where the extra term in $1/(2n) - 1/(3n^{2})$ comes from.

## 6. Exercises

The full set, with worked solutions, is in
[`exercises/01-limits-and-continuity-exercises.md`](./exercises/01-limits-and-continuity-exercises.md)
and
[`exercises/01-limits-and-continuity-solutions.md`](./exercises/01-limits-and-continuity-solutions.md).
Attempt these four first, closed-book.

**★1.** Evaluate, showing each step: (a) $\lim_{x\to3}\frac{x^{2}-9}{x-3}$,
(b) $\lim_{x\to0}\frac{1-\cos x}{x^{2}}$, (c) $\lim_{x\to\infty}\frac{4x^{3}-2}{x^{3}+7}$.

**★2.** For $f(z) = |z - 33|$ (km), compute the left and right derivatives at
$z = 33$. Does $f'$ exist there? Relate the answer to a velocity model that has a
gradient change but no jump.

**★★3.** A body of mass $M$ and radius $a$ has disc potential as in Section 3.4.
How far away, in units of $a$, must an observation be for the point-mass
approximation to be accurate to 1 part in $10^{4}$? Work from the expansion, then
confirm against the script's table.

**★★★4.** The script's Section 1 stops improving at $x \approx 3.6\times10^{-8}$.
Predict, from the floating-point model, the corresponding floor for
$\tan(x)/x$ and for $(e^{x}-1)/x$, and test both predictions.

## 7. Common mistakes

1. **Confusing the value with the limit.** $\lim_{x\to a}f(x)$ can exist while
   $f(a)$ does not, and can differ from $f(a)$. Removable discontinuities are
   handled by taking the limit, not by evaluating.
2. **Assuming a limit exists because a table looks flat.** The harmonic series'
   partial sums look flat for a very long time and still diverge
   ([01-05-07](./07-sequences-and-series.md)). Probe with a *rate*, not with an
   eyeball.
3. **Using l'Hôpital as a first resort.** It requires the hypotheses (form of the
   limit, derivatives existing, and the ratio of derivatives converging) and it can
   be circular, as in Section 3.2.
4. **Treating infinity as a number.** $\infty - \infty$, $\infty/\infty$ and
   $0\cdot\infty$ are undefined; the algebra of limits applies only to finite
   limits.
5. **Probing a limit numerically below the precision floor.** The table in
   Section 5 returns exactly $1.0$ for $x \le 10^{-8}$; a smaller $h$ is not
   more accurate, it is less informative.
6. **Believing a discontinuity is a modelling convenience.** A jump in a model is
   a claim about the Earth. If your data cannot resolve the ramp, say so rather
   than asserting a jump.
7. **Reporting the limiting value without its rate.** The far-field limit in
   Section 3.4 is useful only together with the $(a/z)^{2}$ correction that says
   how far "far" has to be.

## 8. Real-world applications

- **Potential-field interpretation.** The far-field limit of Section 3.4 is the
  reason the gravity anomaly of a compact body is quoted as an equivalent point
  mass, and the reason depth–shape ambiguity is intrinsic rather than an artefact
  of processing. See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Velocity discontinuities.** A first-order velocity jump produces a refracted
  head wave; a gradient produces a turning ray. Deciding which the data supports
  is a continuity question with a quantitative answer.
- **Numerical convergence criteria.** Every iterative solver's stopping rule is a
  limit statement in disguise, and its order of convergence decides cost. See
  [01-12 Numerical Methods](../12-numerical-methods/README.md) and
  [18-inverse-problems](../../18-inverse-problems/README.md).
- **Asymptotic analysis of source fields.** Field behaviour at large distance is
  the basis of monopole/dipole decomposition in gravity, magnetics and
  seismology: an unfolding series of moments, each one a correction to the
  previous limit. See
  [01-06-08 Potential Theory](../06-multivariable-calculus/08-potential-theory.md).
- **Data coverage and resolution.** "Resolved" always means "above the noise floor
  by more than the theory's error term" — the geophysical reading of the
  $\varepsilon$–$\delta$ definition.

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 5–7.
  Level: beginner upward. The rigorous treatment of limits; the squeeze-theorem
  proof in Section 3.1 follows its style.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapter 3.
  Level: beginner to intermediate. Careful treatment of continuity and the
  algebra of limits.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd ed.).
  Wiley.** Chapter 1. Level: beginner. Written for physicists, and unusually good
  at connecting limits to approximations that are actually used.
- **Turcotte, D. L. & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Level: intermediate. Uses limiting arguments
  (half-space, thin-sheet, boundary-layer) as the main modelling device.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapter 1. Level: intermediate. The
  definitive account of point-mass approximations and their errors.

> Note on citations: the bibliographic details above are given so that you can
> locate the works. This repository does not reproduce copyrighted text, and you
> should confirm editions and availability through your library before citing
> them. Chapter references are indicative rather than authoritative: editions
> differ in numbering and content, so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can write the $\varepsilon$–$\delta$ definition from memory and explain
      which quantifier comes first and why.
- [ ] I can compute a one-sided limit and decide whether a two-sided limit exists.
- [ ] I can classify a discontinuity as removable, jump or infinite and give a
      geophysical example of each.
- [ ] I can expand a quantity in a small parameter, take the limit, and state the
      leading correction term with its order.
- [ ] I can say at which $x$ a floating-point evaluation of $\sin(x)/x$ stops
      distinguishing the ratio from $1$, and justify the value from machine
      epsilon.
- [ ] I can compute at least one derivative from the limit definition.
- [ ] I can explain why the far field of any compact body is that of a point mass,
      and what information that destroys.

## 11. Related lessons

- [01-05-02 Derivatives and Rates of Change](./02-derivatives.md) — the limit of a
  difference quotient is the first serious use of this lesson.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](./04-taylor-series.md) —
  the systematic theory of the "leading correction term" used throughout.
- [01-05-06 Improper Integrals, Singularities and Convergence](./06-improper-integrals.md) —
  what happens when the singular limit does not go away.
- [01-05-07 Sequences, Series and Convergence Tests](./07-sequences-and-series.md) —
  limits of discrete sequences, and how to measure the rate.
- [01-01-01 Number Systems, Precision and Scientific Notation](../01-arithmetic/01-number-systems-and-precision.md) —
  the precision floor that stops the numerical limit.
- [01-04 Floating-Point Representation](../01-arithmetic/04-floating-point.md) —
  machine epsilon and catastrophic cancellation, both used in Section 5.
