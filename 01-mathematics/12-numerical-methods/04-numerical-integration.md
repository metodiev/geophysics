---
id: 01-12-04
title: "Numerical Integration: Trapezoid, Simpson, Gauss Quadrature"
level: advanced
prereqs: ["01-05-04", "01-05-05", "01-06-02"]
estimated_minutes: 90
tags: [numerical-methods, quadrature, gauss-legendre, gravity-anomaly]
---

# Numerical Integration: Trapezoid, Simpson, Gauss Quadrature

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the composite trapezoid and Simpson error terms from the
   Euler–Maclaurin expansion, and state the order of each.
2. **State and use** the degree of exactness of an $n$-point Gauss–Legendre rule,
   $2n-1$, and verify it on monomials.
3. **Choose** between Newton–Cotes, Gauss, Romberg and adaptive quadrature from
   the integrand's behaviour, including the cases where each fails.
4. **Compute** the gravity anomaly of a body with no closed-form expression by
   three-dimensional quadrature, and validate the result against a limit.
5. **Recognise** the failure mode of adaptive rules on features they never
   sample, and the singularity that makes Gauss rules the wrong choice at a
   boundary.
6. **Explain** why quadrature is the numerically *favourable* operation —
   it damps error where differentiation amplifies it.

## Prerequisites

[01-05-04 Taylor Series](../05-single-variable-calculus/04-taylor-series.md) —
the error terms. [01-05-05 Integration](../05-single-variable-calculus/05-integration.md)
— the operation being approximated, including improper integrals.
[01-06-02 Multiple Integrals](../06-multivariable-calculus/02-multiple-integrals.md)
— the three-dimensional volume integrals that a gravity anomaly requires.

## 1. Intuition: quadrature is integration by sampling

You cannot integrate a function you cannot write down. What you can do is
evaluate it at selected points and form a weighted sum,

$$I = \int_a^b f(x)\,dx \;\approx\; \sum_{j=0}^{m} w_j f(x_j),$$

and the entire design of a quadrature rule is the choice of the $m+1$ nodes
$x_j$ and the weights $w_j$. Two questions then follow, and they are different:
given the nodes, what is the best choice of weights; and given a free choice,
where should the nodes go?

The answers are the two classical families.

- **Newton–Cotes rules** fix the nodes to be equally spaced and choose the
  weights by integrating the interpolating polynomial through them. They are what
  you use when the samples are given — a time series, a log, a measured profile.
- **Gauss rules** choose both nodes and weights to maximise the degree of
  exactness. An $n$-point rule integrates every polynomial of degree up to
  $2n-1$ exactly, which is the best possible with $n$ points. They are what you
  use when you may evaluate the function wherever you like.

The geophysical motivation is the potential-field volume integral. The vertical
attraction of a body of density $\rho$,

$$g_z(\mathbf r_0) = G\rho\iiint_V \frac{z_0-z'}{\lvert \mathbf r_0-\mathbf r'\rvert^3}\,
\mathrm dV',$$

has a closed form only for a handful of geometries — sphere, slab, some prisms.
For a real orebody, a salt body or a terrain correction, it is a quadrature
problem, and the integrand becomes very sharply peaked as the observation point
approaches the body. That single fact drives every practical choice in the
subject.

## 2. Precise definitions

### 2.1 Degree of exactness

A quadrature rule has **degree of exactness** $d$ if it is exact for every
polynomial of degree $\le d$ and not for some polynomial of degree $d+1$. The
composite trapezoid rule on one panel is exact for degree 1; Simpson's rule for
degree 3; an $n$-point Gauss–Legendre rule for degree $2n-1$.

### 2.2 The rules

Composite trapezoid on $n$ panels of width $h=(b-a)/n$:

$$T_n = h\left[\tfrac12 f(a) + \sum_{i=1}^{n-1} f(a+ih) + \tfrac12 f(b)\right].$$

Composite Simpson on an even $n$:

$$S_n = \frac{h}{3}\left[f(a) + 4\!\!\sum_{i\ \text{odd}}\!\! f_i
+ 2\!\!\sum_{i\ \text{even},\ i\ne0,n}\!\! f_i + f(b)\right].$$

Gauss–Legendre on $[-1,1]$, then mapped to $[a,b]$ by
$x = \frac{a+b}{2} + \frac{b-a}{2}\xi$ and a factor $\frac{b-a}{2}$:

$$\int_{-1}^{1} f\,d\xi \approx \sum_{j=1}^{n} w_j f(\xi_j),$$

where the $\xi_j$ are the roots of the Legendre polynomial $P_n$ and
$w_j = 2/[(1-\xi_j^2)P_n'(\xi_j)^2]$. The demonstration generates the nodes by
Newton's method on the recurrence for $P_n$ — the same tool as
[01-12-01](./01-root-finding.md) — which is how a library does it.

### 2.3 Adaptive quadrature

An adaptive rule estimates the local error on a subinterval and subdivides only
where the estimate is too large. The demonstration uses **adaptive Simpson**: on
each interval it compares the one-panel and two-panel Simpson estimates, whose
difference estimates the error of the coarser one, and subdivides when the
estimate exceeds the local tolerance.

## 3. Derivations

### 3.1 Trapezoid and Simpson orders from Euler–Maclaurin

The Euler–Maclaurin expansion of the trapezoid rule is

$$T_n = I + \frac{B_2}{2!}h^2\left[f'(b)-f'(a)\right]
+ \frac{B_4}{4!}h^4\left[f'''(b)-f'''(a)\right]+\cdots$$

with $B_2 = 1/6$, so the error is

$$I - T_n = -\frac{b-a}{12}h^2 f''(\xi) + O(h^4).$$

Every even power of $h$ appears and every odd power is absent — which is exactly
why Richardson extrapolation of the trapezoid rule works so well, as §3.3 shows.
Simpson's rule is the first Richardson level: the $h^2$ term cancels, leaving

$$I - S_n = -\frac{b-a}{180}h^4 f''''(\xi) + O(h^6).$$

The demonstration measures orders of 2.00 and 4.00 over seven refinements of
$\int_0^1\mathrm e^x\,dx$, and reports the values in the lesson's `code/` output.

### 3.2 Why Gauss is optimal

An $n$-point rule has $2n$ free parameters (nodes and weights). The moment
conditions

$$\sum_{j=1}^{n}w_j \xi_j^{p} = \int_{-1}^{1}\xi^p\,d\xi, \qquad p=0,\dots,2n-1,$$

are $2n$ equations, so a solution exists, and the nodes turn out to be the roots
of $P_n$ — which lie in $(-1,1)$ and are distinct, as required. Exactness for
degree $2n-1$ is therefore the *maximum* achievable with $n$ nodes, because a
rule exact to degree $2n$ would need $2n+1$ conditions from $2n$ parameters.

The demonstration verifies this monomial by monomial: the first non-zero entry in
its exactness table for the $n$-point rule is at $p = 2n$. It is worth noting
that this is a *verification of the node generation* rather than a discovery,
since it is how the nodes were chosen.

### 3.3 Romberg extrapolation

Because the trapezoid error is a series in even powers of $h$, combining two
refinement levels eliminates the leading term:

$$R_{j,k} = R_{j,k-1} + \frac{R_{j,k-1}-R_{j-1,k-1}}{4^{k}-1}.$$

The result is a triangular table in which level $j$ has order $2j+2$. The
demonstration's measured orders along the rows are

$$\text{j}=0:\ 1.98,\quad \text{j}=1:\ 3.97,\quad \text{j}=2:\ 5.96,\quad
\text{j}=3:\ 7.96,$$

i.e. 2, 4, 6, 8 as predicted, with the $j=4$ row already at round-off and carrying
no order information. This is the same Richardson idea as in
[01-12-03](./03-numerical-differentiation.md), and it fails the same way: the
cancellation that produces the higher order also destroys the digits.

### 3.4 Gauss versus Newton–Cotes: a measured comparison

For $\int_0^1\mathrm e^x\,dx = \mathrm e - 1$, the demonstration measures

| $n$ | Gauss error | trapezoid with $2^n$ panels |
|---|---|---|
| 1 | $6.96\times10^{-2}$ | $3.57\times10^{-2}$ |
| 2 | $3.86\times10^{-4}$ | $8.94\times10^{-3}$ |
| 3 | $8.24\times10^{-7}$ | $2.24\times10^{-3}$ |
| 4 | $9.33\times10^{-10}$ | $5.59\times10^{-4}$ |
| 6 | $0$ (below round-off) | $3.50\times10^{-5}$ |
| 8 | $2.22\times10^{-16}$ | $2.19\times10^{-6}$ |

Six Gauss nodes — six evaluations — out-perform sixty-four trapezoid panels.
That is the payoff of choosing where to sample. It is *not* a free lunch: the
Gauss nodes depend on $n$ (so a different rule means different sample locations),
the weights must be tabulated or generated, and a nested refinement is not
available, which is why adaptive schemes are built on Newton–Cotes panels.

### 3.5 Where Gauss fails

Gauss rules place no node at the endpoints, and this is exactly wrong for an
integrand with an endpoint singularity. A half-space anomaly integral such as
$\int_0^\infty$ with a $1/r^2$ kernel has infinite derivatives at the boundary,
and a Gauss rule converges only algebraically — no better than a composite rule
— because the error theory requires analyticity on the interval. The remedies
are a composite rule with the panels concentrated toward the singularity, or a
coordinate substitution (for example $x = \tan^2\theta$) that removes it. This is
a case where checking which model a formula assumes changes the conclusion: the
statement "Gauss is optimal" assumes a smooth integrand *including the ends*.

## 4. Physical interpretation and the gravity-anomaly quadrature

### 4.1 The sphere as the one geometry with a closed form

Newton's shell theorem states that the exterior field of a uniform sphere equals
that of a point mass at its centre. For a sphere of density $\rho$ and radius $R$
whose centre is at depth $d$, the vertical attraction is exactly

$$g_z = \frac{GM}{d^2}, \qquad M = \tfrac43\pi R^3\rho .$$

With $\rho = 2670\ \mathrm{kg\,m^{-3}}$, $R = 1000$ m and $d = 3000$ m — synthetic
values — the mass is $1.118407\times10^{13}$ kg and $g_z =
8.293609\times10^{-5}\ \mathrm{m\,s^{-2}} = 8.293609$ mGal. This is the
reference against which the quadrature is scored.

Writing the volume integral in spherical coordinates about the sphere's centre
and using the axial symmetry, the azimuthal integral gives $2\pi$ and

$$g_z = 2\pi G\rho R^3\int_0^1\!\!\int_{-1}^{1}
\frac{d-R r\mu}{\left[R^2r^2 - 2dRr\mu + d^2\right]^{3/2}} r^2\,\mathrm d\mu\,\mathrm dr ,$$

with $\mu=\cos\theta$ absorbing the Jacobian. Two nested Gauss–Legendre rules
then compute it. The measured relative errors are

| $n_r = n_\mu$ | relative error |
|---|---|
| 4 | $1.02\times10^{-4}$ |
| 8 | $1.25\times10^{-8}$ |
| 12 | $1.63\times10^{-12}$ |
| 16 | $1.63\times10^{-16}$ |

— roughly four correct digits gained per doubling, which is the geometric
convergence a Gauss rule achieves on an analytic integrand. A composite
trapezoid rule on the same volume would need hundreds of divisions per axis,
because it samples the near-point region no more densely than the far one.

### 4.2 A body with no closed form, validated by a limit

Replace the sphere with a tri-axial ellipsoid of semi-axes $(3,2,1)$ km and the
same density. There is no elementary closed form for its exterior field, which is
the point: this is what a real body looks like. What *is* available is the
multipole limit — for any compact body,

$$\lim_{d\to\infty} \frac{g_z d^2}{G} = M .$$

The demonstration computes $g_z$ on the axis by three-dimensional quadrature and
measures the ratio:

| $d/a$ | $g_z d^2/(GM)$ | $(d/a)^2\,[1-\text{ratio}]$ |
|---|---|---|
| 2 | 0.91802148 | 0.327914 |
| 4 | 0.97774971 | 0.356005 |
| 10 | 0.99635089 | 0.364911 |
| 20 | 0.99908444 | 0.366226 |
| 50 | 0.99985336 | 0.366596 |

The ratio rises monotonically to 1 and the deficit times $(d/a)^2$ settles on
0.3666: the leading correction is the quadrupole term, which falls as
$(\text{size}/d)^2$. **This is the validation pattern for every anomaly
quadrature**: the sphere supplies an exact check of the machinery, and a
far-field limit supplies a check on the geometry that has no closed form.

### 4.3 Why quadrature is favourable

Recall from [01-12-03](./03-numerical-differentiation.md) that a derivative
carries an error $\sim u/h$ and that data noise contributes $\sim\sigma/h$. A
quadrature rule instead sums $m$ values with weights of size $h$, so independent
round-off enters as $\sim u h \sqrt m$ and independent noise as
$\sim \sigma h \sqrt m$ — both *decreasing* with the panel width. The
consequence is practical: an anomaly computed by quadrature is limited by the
accuracy of the density model, not by the arithmetic, whereas a gradient computed
by differencing is limited by the arithmetic first. Integration is the safe
operation.

## 5. Assumptions and regime of validity

| Rule | Order | Requires | Fails when |
|---|---|---|---|
| Composite trapezoid | $O(h^2)$ | $f\in C^2$, uniform panels | $f$ has a kink or spike inside a panel |
| Composite Simpson | $O(h^4)$ | $f\in C^4$, even panel count | same, and it cannot localise |
| Gauss–Legendre | exact to degree $2n-1$; geometric for analytic $f$ | analytic $f$ on the *closed* interval | endpoint singularity, or an interior singularity inside the rule's support |
| Romberg | $O(h^{2j+2})$ at level $j$ | the even-power error series | round-off after four or five levels |
| Adaptive Simpson | meets a stated tolerance | the error estimator is valid (smooth, non-stiff integrand) | the feature is never sampled; the integrand is non-smooth |

Two assumptions deserve emphasis.

1. **Uniformity and smoothness of the panels.** Every Newton–Cotes order above
   assumes equal panel widths and $f$ smooth across each panel. A well log with a
   bed boundary inside a panel silently reduces the order to whatever the kink
   allows.
2. **A trustworthy error estimate.** Adaptive quadrature controls the error only
   where it has sampled. The demonstration's failure case is a Gaussian of width
   $10^{-3}$ on $[0,1]$: the three initial points have values below $10^{-3}$, the
   difference of the two Simpson estimates is zero, and the rule reports the
   integral as $0$ after five evaluations. The true value is
   $1.772454\times10^{-3}$. There is no warning, because every quantity the
   algorithm can see is consistent with a zero integrand.

## 6. Python demonstration

`code/numerical_integration.py` implements the composite rules, generates
Gauss–Legendre nodes by Newton iteration on $P_n$, builds a Romberg table,
implements adaptive Simpson, and performs the two gravity quadratures. Selected
output:

```text
  integral of exp(x) on [0, 1] = e - 1 = 1.718281828459045
       n     trapezoid err   order     Simpson err   order
       8         2.237e-03    2.00       2.326e-06    3.99
      32         1.398e-04    2.00       9.103e-09    4.00
     128         8.740e-06    2.00       3.556e-11    4.00

  Rows are the extrapolation levels j; the order is measured along
  each row by refining the trapezoid panel count (left to right).
    j = 0: measured order 1.98 (theory 2)
    j = 1: measured order 3.97 (theory 4)
    j = 2: measured order 5.96 (theory 6)
    j = 3: measured order 7.96 (theory 8)

  I = integral of |x - 0.37|^(1/2) on [0, 1]:
  exact (evaluated in closed form) = 0.4834061409414945
         tol        adaptive value       error   evals   uniform panels for same error
       1e-06     0.483406106269180   3.467e-08     181                           16384
       1e-09     0.483406140940562   9.324e-13    1009                         8388608

  SYNTHETIC uniform sphere: rho = 2670 kg/m^3, R = 1000 m, centre depth 3000 m
  mass = 1.118407e+13 kg;  GM/d^2 = 8.293609e-05 m/s^2 = 8.293609e+00 mGal
    nr  n_mu          quadrature    relative error
     4     4  8.292762756681e-05         1.021e-04
     8     8  8.293609024788e-05         1.252e-08
    12    12  8.293609128587e-05         1.632e-12
    16    16  8.293609128601e-05         1.634e-16

     d/a    d (km)      g_z (mGal)     g_z d^2 / (G M)   (d/a)^2 (1 - ratio)
       2         6    1.142057e+01          0.91802148              0.327914
      10        30    4.958007e-01          0.99635089              0.364911
      50       150    1.990174e-02          0.99985336              0.366596
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Trapezoid 2.00, Simpson 4.00 | the panel, not the number of panels, sets the order |
| Oscillatory integrand needs 128 panels for the same order | the order is unchanged but the constant grows with the frequency |
| First non-zero Gauss entry at $p=2n$ | degree of exactness $2n-1$ verified monomial by monomial |
| Six Gauss nodes beat 64 trapezoid panels | node placement is worth more than node count |
| Romberg rows 2, 4, 6, 8, then round-off | extrapolation buys two orders per level and then stops |
| Adaptive: 181 evals against 16384 | adaptivity pays when the difficulty is localised |
| Adaptive returns 0 on the narrow Gaussian | an estimator can only see what it samples |
| Sphere quadrature reaches $1.6\times10^{-16}$ | the machinery is exact to round-off where a closed form exists |
| Ellipsoid deficit $\to 0.3666(d/a)^{-2}$ | the far-field limit validates a body with no closed form |

> **Breaking exercise.** In `report_gravity_quadrature`, move the observation
> point from $d = 3R$ to $d = 1.05R$ and predict, before running, whether the
> Gauss convergence rate will stay geometric. Then run it and explain the result
> in terms of where the integrand's singularity lies relative to the rule's
> support.

## 7. Common mistakes

1. **Believing more panels change the order.** Refining a trapezoid rule gives
   order 2 forever. Raising the order requires a different rule or extrapolation.
2. **Using Gauss nodes with a tabulated integrand.** Gauss nodes are not nested
   and depend on $n$; if the samples are given, only Newton–Cotes applies.
3. **Applying Gauss to an endpoint singularity.** The optimality proof assumes
   analyticity on the closed interval, which a half-space kernel does not have.
4. **Trusting an adaptive rule on an unsampled feature.** The measured failure is
   a return of exactly zero with five evaluations.
5. **Extrapolating past the round-off floor in a Romberg table.** The $j=4$ row
   carries no order information; reading it as an accuracy estimate is a mistake.
6. **Scoring a quadrature against another quadrature.** Validating a computed
   anomaly against a second computation of the same integral proves nothing about
   either. Use a closed form, or a limit that the geometry must obey.
7. **Forgetting the Jacobian in a change of variables.** A three-dimensional
   volume integral in spherical coordinates carries $r^2\sin\theta$; omitting it
   changes the answer by a factor that can look plausible. The ellipsoid
   quadrature in the demonstration had exactly this bug during development, and
   the far-field limit is what exposed it: the ratio approached 3 instead of 1 —
   the ratio of $\int_0^1 r^2\,dr$ to $\int_0^1 dr$.

## 8. Real-world applications

- **Potential-field modelling of arbitrary bodies.** Terrain corrections, salt
  body gravity and orebody magnetics are all volume or surface quadratures. The
  practical algorithms (Gauss–Legendre in depth, polygon line integrals
  laterally) are refinements of the rules in this lesson.
- **Terrain and Bouguer corrections.** The Bouguer slab value $2\pi G\rho t$ is
  the infinite-plate limit of a quadrature, and the departure from it is computed
  by summing prisms; the limit is the validation, exactly as in §4.2.
- **Filter design in signal processing.** The response of a filter is the
  integral of its kernel against the spectrum, evaluated by quadrature in
  [10 Fourier Analysis](../10-fourier-analysis/README.md); oscillatory integrands
  are the norm and the constant in front of $h^2$ is what sets the required grid.
- **Statistical estimation.** Marginal likelihoods and expectation values are
  integrals; the same rules appear in
  [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md), where
  the integrand is typically sharply peaked around a mode — a case where adaptive
  or Laplace-type methods are required.
- **Geodesy.** The gravitational potential of a topographic mass distribution is
  computed by quadrature over a digital elevation model, and the resolution of
  the model is chosen by balancing the quadrature error against the model error.
- **Reference datums in gravity databases.** Regional gravity compilations, such
  as the [NOAA global gravity database](https://www.ngdc.noaa.gov/mgg/gravity/),
  involve reductions that are themselves integrals of the terrain.

## 9. Further reading

- **Davis, P. J., & Rabinowitz, P. (1984). *Methods of Numerical Integration*
  (2nd ed.). Academic Press.** Level: graduate. The encyclopaedic reference,
  including the sharp form of the Gauss error theory and the treatment of
  singular integrands.
- **Stoer, J., & Bulirsch, R. (2002). *Introduction to Numerical Analysis*
  (3rd ed.). Springer.** Level: graduate. The Euler–Maclaurin derivation and the
  Romberg algorithm in full, with the convergence proofs.
- **Trefethen, L. N. (2008). Is Gauss quadrature better than Clenshaw–Curtis?
  *SIAM Review*, 50(1), 67–87.** Level: graduate. The modern answer to the
  question in the title, with the point that for analytic integrands the node
  distribution matters more than the optimality.
- **Nagy, D., Papp, G., & Benedek, J. (2000). The gravitational potential and its
  derivatives for the prism. *Journal of Geodesy*, 74, 552–560.** Level:
  graduate. The closed form for a rectangular prism, which is the standard
  building block that replaces quadrature in production potential-field codes.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Level: advanced undergraduate to
  graduate. The geophysical framing of §4, including the terrain-correction
  quadratures.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/04-numerical-integration-exercises.md`](./exercises/04-numerical-integration-exercises.md),
with worked solutions in
[`exercises/04-numerical-integration-solutions.md`](./exercises/04-numerical-integration-solutions.md).

**★1.** Compute the composite trapezoid and Simpson estimates of
$\int_0^1 \mathrm e^x\,dx$ with $n=4$ and compare each with the exact value.

**★2.** State the degree of exactness of the 3-point Gauss rule and verify it by
integrating $x^5$ on $[-1,1]$.

**★3.** Derive the two-panel Simpson rule from the requirement of exactness on
cubics and show that its error term is $-h^4f''''/180$.

**★4.** A prism of density $2670\ \mathrm{kg\,m^{-3}}$ and thickness 200 m
extends to infinity laterally. Compute the Bouguer slab value of $g_z$ in mGal
and state which limit of a quadrature it represents.

**★★5.** Show that the trapezoid error series contains only even powers of $h$
by writing $f$ as a Taylor series and summing the panel errors.

**★★6.** Use the Romberg table in §6 to estimate $\int_0^1 \mathrm e^x\,dx$ to
eight digits, and say which table entry you used and why.

**★★7.** The integrand $\int_0^1 x^{-1/2}\,dx$ is improper. Compute it by
(a) a composite trapezoid rule with the endpoint value omitted, (b) the
substitution $x = t^2$ followed by Simpson, and (c) a 4-point Gauss rule. Compare
the errors and explain the ranking.

**★★8.** A gravity anomaly is computed by quadrature with $n_r=n_\mu=4$ and the
result is 1% low. Estimate the node counts needed for 0.01% accuracy from the
error table in §4.1 and state the assumption you are making about the integrand.

**★★★9.** Implement the finite-plate Bouguer quadrature: a square plate of
half-width $L$ and thickness $t$, observed at the surface at its centre, with the
observation point on the boundary of the plate. Measure the ratio $g_z/(2\pi G\rho t)$
for $L/t = 1, 10, 100$ and report the approach to the infinite-slab limit,
including how the corner singularity affects the Gauss convergence.

**★★★10.** A colleague integrates a magnetic anomaly over a dipping dyke by
Gauss–Legendre quadrature with 20 nodes and reports four-figure accuracy, verified
by repeating the calculation with 24 nodes. Critique the verification. State the
two independent checks you would require instead.

## 11. Self-assessment checklist

- [ ] I can state the error term of the composite trapezoid and Simpson rules and
      derive both from Euler–Maclaurin.
- [ ] I can state the degree of exactness of an $n$-point Gauss rule and explain
      why it cannot be higher.
- [ ] I can generate Gauss–Legendre nodes without a table.
- [ ] I can build a Romberg table and state the order of each level.
- [ ] I can describe the failure mode of adaptive quadrature on an unsampled
      feature, with the measured numbers.
- [ ] I can set up the volume integral for the gravity of an axisymmetric body
      and identify the Jacobian.
- [ ] I can validate an anomaly quadrature against a closed form and against a
      far-field limit, and say why scoring it against a second quadrature proves
      nothing.

## Related lessons

- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](./03-numerical-differentiation.md)
  — the mirror-image trade-off, where error is amplified instead of damped.
- [01-12-02 Interpolation, Splines and Approximation Theory](./02-interpolation.md)
  — Newton–Cotes rules *are* interpolatory quadrature, and the node-placement
  question is the same one.
- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](./05-linear-solvers.md)
  — the linear algebra that takes over when a quadrature is embedded in a model
  discretisation.
- [01-06-02 Multiple Integrals](../06-multivariable-calculus/02-multiple-integrals.md)
  — the volume and surface integrals being approximated here.
- [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md) — the
  same rules applied to probability integrals and marginalisation.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  quadrature inside production modelling codes, where the cost of node
  evaluations dominates.
