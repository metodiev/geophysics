---
id: 01-16-01
title: "Vector Spaces of Functions, Norms and Inner Products"
level: graduate
prereqs: ["01-07-01", "01-05-07"]
estimated_minutes: 90
tags: [functional-analysis, function-spaces, norms, inner-products, inverse-problems]
---

# Vector Spaces of Functions, Norms and Inner Products

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the three norm axioms, verify them for the norms that geophysics
   actually uses, and explain why a norm is the minimum equipment needed to say
   that one model is closer to the truth than another.
2. **Distinguish** a normed space from an inner-product space, and say what the
   inner product buys that a norm cannot: angles, orthogonality, projections.
3. **Write down** the $L^p$ norms, the supremum norm, and a weighted
   discretised norm, and identify which one a given inversion code is
   minimising.
4. **Explain** why the choice of norm is a statement about the noise model —
   $L^2$ for Gaussian errors, $L^1$ for heavy-tailed ones — and demonstrate the
   consequence with a pick set containing one gross error.
5. **Verify** Minkowski's and Hölder's inequalities numerically and state when
   equality holds.
6. **Show** that convergence in one norm does not imply convergence in another,
   and quantify the finite-dimensional equivalence constants that do hold.
7. **Recognise** the dual space as the home of data functionals, including the
   point source that is not a function at all.

## Prerequisites

- [01-07-01 Vectors, Vector Spaces and Basis](../07-linear-algebra/01-vectors-and-spaces.md)
  — linear independence, basis and dimension, now applied to spaces whose
  elements are functions rather than arrows.
- [01-05-07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md)
  — limits, and the difference between pointwise and uniform convergence, which
  reappears here as the difference between two norms.
- [01-06-02 Multiple Integrals and Change of Variables](../06-multivariable-calculus/02-multiple-integrals.md)
  — the integrals that define the $L^p$ norms; weighted integrals reappear as
  weighted norms.

## 1. Why a geophysicist needs a norm

A gravity survey returns numbers $d_1,\dots,d_m$. An inversion returns a density
model, which is a *function* $\rho(x,y,z)$. So the object we have to discuss,
compare, bound and optimise over is an element of a space of functions, not a
list of numbers. The immediate technical problem is that "close" has no meaning
in a bare set of functions:

- Is a model that differs from the truth by a thin 10 per cent error everywhere
  better or worse than one that is exact except for a factor of two in one small
  block?
- If a data set is fitted with residual 0.3, is that good? The question is not
  answerable until the residual is expressed in a norm that has the same units
  as the data.

Functional analysis answers both questions by supplying the structure that makes
them well posed. This lesson builds the first layer of that structure: linear
spaces of functions, the norm that measures size, and the inner product that
measures angle.

There is a second reason to be careful here. In finite-dimensional linear algebra
all norms are equivalent, so the choice rarely bites. In function spaces they are
*not* equivalent, and the differences are large enough to change the answer to a
geophysical question. Section 6 measures how large.

## 2. Spaces of functions

### 2.1 Linear structure

Let $\Omega$ be the region of interest — an interval, a surface patch, the whole
sphere, a volume of the subsurface. Let $V$ be a set of real-valued functions on
$\Omega$. $V$ is a **vector space** if it is closed under addition and scalar
multiplication:

$$f + g \in V, \qquad \alpha f \in V \quad \text{for all } f, g \in V,\ \alpha \in \mathbb{R}.$$

That is all. Every theorem in the rest of this module is a statement about such a
space with extra structure added, and the extra structure is always one of two
kinds: a way to measure size, or a way to measure angle.

| Space | Elements | Used for |
|---|---|---|
| $C[a,b]$ | continuous functions | classical solutions, before regularity is lost |
| $C^k[a,b]$ | functions with $k$ continuous derivatives | strong forms of differential equations |
| $L^2(\Omega)$ | $\int_\Omega f^2 < \infty$ | finite-energy models and data; least squares |
| $L^1(\Omega)$ | $\int_\Omega \lvert f\rvert < \infty$ | robust misfits; total-variation style priors |
| $L^\infty(\Omega)$ | $\sup \lvert f\rvert < \infty$ | worst-case bounds, maximum-error criteria |
| $L^2(\Omega; w)$ | $\int_\Omega w f^2 < \infty$ for a weight $w > 0$ | weighted inversion, error-weighted data |

$L^2$ needs one caveat that matters in geophysics. Its elements are not
functions but equivalence classes of functions that differ on sets of measure
zero. Changing a density model at a single point changes neither its $L^2$ norm
nor its gravity field, so no $L^2$-based method can ever detect such a change.
This is not pedantry: it is the reason point values of a model are not
observable, and it is the discrete ancestor of the non-uniqueness that lesson
01-16-05 makes precise.

### 2.2 Dimension

A vector space of functions can be finite- or infinite-dimensional. The
polynomials of degree $\le n$ form an $(n+1)$-dimensional space; $C[0,1]$ is
infinite-dimensional because no finite set of continuous functions spans it. The
distinction is the whole source of difficulty in the subject: an
infinite-dimensional space is not a limit of finite-dimensional ones in any
simple way, and choosing a finite-dimensional subspace — a *discretisation* — is
a modelling decision with consequences that lesson 01-16-07 examines.

## 3. Norms

### 3.1 Definition

A **norm** on a vector space $V$ is a map $\lVert\cdot\rVert: V \to [0,\infty)$
satisfying, for all $f, g \in V$ and all scalars $\alpha$:

$$\text{(N1) } \lVert f\rVert = 0 \iff f = 0; \qquad
\text{(N2) } \lVert \alpha f\rVert = \lvert\alpha\rvert\,\lVert f\rVert; \qquad
\text{(N3) } \lVert f + g\rVert \le \lVert f\rVert + \lVert g\rVert.$$

(N3) is the triangle inequality, and it is the one that is not automatic. It is
what makes the norm a usable notion of distance: $d(f,g) = \lVert f - g\rVert$
then satisfies the triangle inequality, so "closer than" behaves transitively and
the notion of a ball $\{g : \lVert g - f\rVert < r\}$ has the geometry one
expects.

The pair $(V, \lVert\cdot\rVert)$ is a **normed space**. Adding completeness —
every Cauchy sequence converges to an element of $V$ — makes it a **Banach
space**. Completeness is what lets one take limits of approximate solutions and
be sure the limit is an admissible model; it is the technical hypothesis behind
every existence theorem in this module, and it is the reason the weak formulation
of lesson [01-09-08](../09-partial-differential-equations/08-weak-solutions.md)
uses $H^1$ and not $C^1$.

### 3.2 The working norms

For $1 \le p < \infty$,

$$\lVert f\rVert_p = \left(\int_\Omega \lvert f(x)\rvert^p\,dx\right)^{1/p},
\qquad
\lVert f\rVert_\infty = \operatorname*{ess\,sup}_{x\in\Omega}\lvert f(x)\rvert ,$$

and the supremum norm is the $p \to \infty$ limit of the family. For discrete
data $d \in \mathbb{R}^m$ the same formulas hold with the sum replacing the
integral, and a weighted version replaces $dx$ by $w(x)\,dx$ or the sum by
$\sum_i w_i(\cdot)_i$.

Three structural facts are worth stating once, because they are used repeatedly:

- $\lVert f\rVert_p$ is non-increasing in $p$ on a set of finite measure. A model
  that is small in $L^\infty$ is small in every $L^p$, but not conversely.
- The larger $p$ is, the more the norm cares about the largest values. $L^\infty$
  cares only about the single worst point; $L^1$ averages magnitude and is
  therefore insensitive to a few large errors.
- Because the discretised integral is a quadrature rule, a discretised norm is
  not the continuum norm. Using $\sum_i f_i^2$ instead of
  $h\sum_i f_i^2$ rescales the answer by $\sqrt{h}$ and changes any convergence
  rate it is used to measure. Every numerical statement about a $L^2$ error must
  say which of the two it means.

### 3.3 The norms we actually measure, and their closed forms

The demonstration evaluates the three norms of $f(x) = x(1-x)$ on $[0,1]$ and
compares them with the closed forms $\lVert f\rVert_1 = 1/6$,
$\lVert f\rVert_2 = 1/\sqrt{30}$ and $\lVert f\rVert_\infty = 1/4$:

```text
      norm      quadrature     closed form     abs error
        L1    0.1666666667    0.1666666667      4.17e-12
        L2    0.1825741858    0.1825741858      0.00e+00
      Linf    0.2500000000    0.2500000000      0.00e+00
```

The residuals are quadrature error, so the formulas are as stated. Note the
ratios, $\lVert f\rVert_1/\lVert f\rVert_2 = 0.9129$ and
$\lVert f\rVert_\infty/\lVert f\rVert_2 = 1.3693$: the three norms disagree by up
to 37 per cent on the same function. They are not interchangeable measures of
"small".

## 4. Inner products

### 4.1 Definition and the induced norm

An **inner product** on $V$ is a map $\langle\cdot,\cdot\rangle: V\times V \to
\mathbb{R}$ that is symmetric, linear in each argument and positive definite:

$$\langle f,f\rangle \ge 0, \qquad \langle f,f\rangle = 0 \iff f = 0 .$$

It induces a norm through $\lVert f\rVert = \sqrt{\langle f,f\rangle}$, so every
inner-product space is a normed space. The converse fails: the $L^p$ norms for
$p \ne 2$ do not come from any inner product, and that is exactly why
orthogonality, projection and least squares exist only in $L^2$ (or in a weighted
$L^2$).

The **Cauchy–Schwarz inequality**

$$\lvert\langle f,g\rangle\rvert \le \lVert f\rVert\,\lVert g\rVert$$

is what gives meaning to the angle between two functions,

$$\cos\theta = \frac{\langle f,g\rangle}{\lVert f\rVert\,\lVert g\rVert},$$

and hence to orthogonality, $\langle f,g\rangle = 0$. Every geometric idea in
lesson 01-16-02 — orthogonal expansion, projection, the normal equations — is
Cauchy–Schwarz plus completeness.

**Hölder's inequality** generalises Cauchy–Schwarz from the pair $(2,2)$ to
conjugate exponents $1/p + 1/q = 1$:

$$\lvert\langle f,g\rangle\rvert \le \lVert f\rVert_p\lVert g\rVert_q .$$

Hölder is the tool that shows a data functional is bounded, and boundedness is
the hypothesis needed before an adjoint can be defined at all. Its discrete form
is the reason a weighted least-squares misfit can be rewritten as a plain
least-squares misfit in whitened variables.

The demonstration checks both inequalities on
$f = e^{-8(x-0.35)^2}$ and $g = \sin^2(3\pi x)$:

```text
    (a) Minkowski: ||f+g||_p <= ||f||_p + ||g||_p
         p     ||f+g||_p   ||f||_p+||g||_p       slack
        1      1.073129          1.073129   0.000e+00
        2      1.177958          1.270012   9.205e-02
        4      1.315736          1.470818   1.551e-01
      inf      1.846079          2.000000   1.539e-01

    (b) Holder: |<f, g>| <= ||f||_p ||g||_q with 1/p + 1/q = 1
         p     q       |<f,g>|   ||f||_p ||g||_q     ratio
         1   inf      0.290048          0.573129    0.5061
       1.5     3      0.290048          0.421307    0.6884
         2     2      0.290048          0.402720    0.7202
         3   1.5      0.290048          0.401392    0.7226
       inf     1      0.290048          0.500000    0.5801
```

The Minkowski slack is exactly zero for $p = 1$ because both functions are
non-negative, so $\lvert f+g\rvert = \lvert f\rvert + \lvert g\rvert$ pointwise —
that is the equality case, and it is a useful diagnostic: a zero slack means the
two functions do not cancel anywhere, which for a misfit means every residual has
the same sign. The Hölder ratios are all below 1 and peak near $p = 3$ for these
particular functions; the equality case in Hölder is $g \propto
\operatorname{sign}(f)\lvert f\rvert^{p-1}$, which these functions do not
satisfy.

### 4.2 The weighted inner product, and why it is the geophysical default

Almost every real misfit functional has the form

$$\chi^2(m) = \sum_{i=1}^{m} \frac{(d_i - F_i(m))^2}{\sigma_i^2}
= \lVert W^{1/2}(d - F(m))\rVert_2^2 ,$$

with $W = \operatorname{diag}(\sigma_i^{-2})$. This is the $L^2$ norm with
respect to the weight $w_i = \sigma_i^{-2}$, and once it is recognised as a norm,
the machinery of the rest of this module applies unchanged. Two consequences are
worth committing to memory:

- **Units.** An unweighted sum of squared residuals in mixed units (mGal for
  gravity, seconds for travel times) is dimensionally meaningless. The weight
  $1/\sigma_i^2$ is what makes the sum a pure number.
- **Data importance.** The weight is the metric in data space. Changing it
  changes which directions of the data space are "large", and therefore changes
  the model. A correlation-weighted norm (a non-diagonal $W$) is the honest
  choice when the errors are correlated, and treating correlated data as
  independent is a modelling error that no algorithm repairs. Lesson
  [18-inverse-problems](../../18-inverse-problems/README.md) develops the
  covariance language for this.

## 5. Assumptions and regime of validity

Everything above rests on hypotheses that are easy to forget:

1. **Measurability and integrability.** $\lVert f\rVert_p < \infty$ requires $f$
   to be measurable and $p$-integrable. A model with a singularity is not in
   $L^p$ for any $p$, which is why a point mass is a distribution and not a
   density (Section 7).
2. **Finite measure of $\Omega$.** The ordering $\lVert f\rVert_p \le
   \lVert f\rVert_q$ for $p > q$ needs $\Omega$ of finite measure. On the whole
   real line it fails, and the failure is the reason Fourier-domain arguments on
   an unbounded domain need different norms from those on a survey area.
3. **The norm must match the noise model.** Using $L^2$ when the errors are
   heavy-tailed is not a stylistic choice; it is a mis-specified likelihood, and
   its consequence is quantified in Section 6.
4. **The discretised norm is not the continuum norm.** Convergence rates quoted
   from a grid must state whether they include the quadrature weights.
5. **Completeness must be checked, not assumed.** $C[0,1]$ with the $L^2$ norm is
   not complete: a sequence of continuous functions can converge in $L^2$ to a
   discontinuous limit. That is precisely why $L^2$ or $H^1$, and not $C$, is
   the working space.

## 6. Norms are not interchangeable

### 6.1 Convergence in one norm, not in another

If a sequence of models converges in one norm, it need not converge in another.
The demonstration shows this with $f_n(x) = x^n$ on $[0,1]$:

```text
         n      ||f_n||_L2    1/sqrt(2n+1)   ||f_n||_Linf    f_n(1)
         1      0.57735027      0.57735027       1.000000       1.0
        10      0.21821789      0.21821789       1.000000       1.0
       100      0.07053457      0.07053456       1.000000       1.0
      1000      0.02235546      0.02235509       1.000000       1.0
```

$\lVert f_n\rVert_2 \to 0$ exactly like $1/\sqrt{2n+1}$, while
$\lVert f_n\rVert_\infty = 1$ and $f_n(1) = 1$ for every $n$. The sequence
converges to the zero function in $L^2$ and converges pointwise to zero
*everywhere except at $x = 1$*, and there it does not converge at all. Two
lessons follow.

- **A misfit that is small in one norm can hide an arbitrarily large pointwise
  error.** A smooth model can be 1 per cent wrong in $L^2$ and 100 per cent wrong
  at a single depth, which matters if the target is a well location rather than a
  regional field.
- **"The model is close to the data" is an incomplete sentence.** It becomes
  complete when it names the norm, and a defensible paper names it.

### 6.2 The equivalence constants in finite dimensions

In $\mathbb{R}^n$ there are constants $c, C > 0$ with
$c\lVert x\rVert_a \le \lVert x\rVert_b \le C\lVert x\rVert_a$ for any two norms,
so convergence in one norm does imply convergence in the other. This is often
quoted as if it settled the matter; it does not, because the constants depend on
$n$. The demonstration measures the worst case over random vectors:

```text
         n   max ||x||_1/||x||_2     sqrt(n)   max ||x||_2/||x||_inf
        10              3.054401      3.1623                2.422903
       100              8.432645     10.0000                5.045131
      1000             25.740814     31.6228               11.266970
     10000             80.422774    100.0000               29.290305
```

The measured maxima approach the bound $\sqrt{n}$ and grow without limit with
$n$. A model dimension of $10^4$ — small by modern standards — allows a ratio of
$10^2$ between the $L^1$ and $L^2$ sizes of the same error. So the finite-dimensional
equivalence theorem is true and practically useless until $n$ is fixed, at which
point it is a statement about that $n$ and nothing more.

The geometry changes too:

```text
         p   measured area     closed form
         2        2.001334        2.000000
        pi        3.141584        3.141593
         4        4.002667        4.000000
```

$\{x : \lVert x\rVert_p \le 1\} \subset \mathbb{R}^2$ has area 2 for $p = 1$
(a diamond), $\pi$ for $p = 2$ (a disk) and 4 for $p = \infty$ (a square). "Do
not let the model grow" is a different geometric constraint in each case, and the
difference is exactly why $L^1$ regularisation produces sparse models and $L^2$
regularisation produces smooth ones.

## 7. The dual space, and where the data live

The **dual space** $V^*$ is the set of continuous linear functionals
$\ell: V \to \mathbb{R}$, with norm

$$\lVert\ell\rVert_{V^*} = \sup_{\lVert f\rVert \le 1}\lvert\ell(f)\rvert .$$

Data are elements of $V^*$: each measurement is a linear functional of the model,
$d_i = \ell_i(m)$, whatever physical form $\ell_i$ takes. This is the correct
setting for geophysics because some data functionals are not representable as
integrations against a function:

- A point source is $\ell(m) = m(x_0)$, which is not
  $\int \delta(x-x_0)m(x)\,dx$ for any function: $\delta$ is a distribution, an
  element of the dual of $C$ or of $H^1$, not of $L^2$.
- A borehole measurement of a point value and a satellite measurement of a
  regional average are both linear functionals; they live in different parts of
  $V^*$ and are informative in different ways.

The practical payoff of this viewpoint appears in lesson
[01-09-08](../09-partial-differential-equations/08-weak-solutions.md): the
finite-element weak form is written with data as a functional $\ell(v)$ precisely
so that a point source can be admitted without pretending it is a function. The
same shift of viewpoint is what makes the adjoint of lesson 01-16-03 an operator
between $V$ and $V^*$ rather than a matrix transpose.

## 8. The choice of norm as a physical choice

This is the section that matters for the rest of the module. The demonstration
fits a line $t = a + bx$ to a ten-point travel-time pick set that follows
$t = 0.20 + 0.50x$ exactly except for one pick at $x = 10$ that is too large by
1.8 s, and minimises $\lVert t - (a + bx)\rVert_p$ for $p = 2, 1, \infty$:

```text
     criterion   intercept (s)   slope (s/km)        cost   residual at x=10
            L2         -0.1600         0.5982      1.4563            -1.1782
            L1          0.2000         0.5000      1.8001            -1.8000
          Linf         -0.6477         0.6840      0.8080            -0.8080
```

The three criteria disagree about the *parameters*, not merely about the residual:

- $L^2$ returns slope $0.5982$ against a true $0.5000$, a 20 per cent error, and
  spreads the misfit over all ten picks.
- $L^1$ returns the true $0.2000$ and $0.5000$ exactly, and lets the bad pick
  carry the whole 1.8 s.
- $L^\infty$ minimises the largest residual, forcing it down to $0.8080$ but
  biasing the slope to $0.6840$ and the intercept to $-0.65$.

Which is correct is not a mathematical question. It is a statement about the
error distribution:

| Error model | Maximum-likelihood misfit | Behaviour with an outlier |
|---|---|---|
| Gaussian, independent, known $\sigma_i$ | $\sum (r_i/\sigma_i)^2$ | outlier pulls the whole solution |
| Laplacian / heavy-tailed | $\sum \lvert r_i\rvert/\sigma_i$ | outlier is down-weighted |
| Bounded worst case | $\max_i \lvert r_i\rvert/\sigma_i$ | outlier dominates the cost |

Geophysical data are heavier-tailed than Gaussian far more often than the
literature admits: a mis-picked first arrival is not a sample from a Gaussian.
$L^1$-type misfits and Huber costs are therefore standard in travel-time
tomography, and total-variation ($L^1$ on a derivative) priors are standard in
potential-field and seismic inversion. Choosing $L^2$ out of habit is choosing to
believe every pick, including the wrong ones.

Two caveats of equal weight. $L^1$ and $L^\infty$ misfits are not smooth —
$\lvert r\rvert$ has a kink at $r = 0$ and $\max$ has no derivative at the active
point — so least-squares machinery does not apply directly and the problems are
solved by linear or convex programming
([01-14-07](../14-optimization/07-linear-programming.md)). And a robust norm
changes the *variance* of the estimate as well as its value: down-weighting
outliers reduces bias but increases variance when the "outliers" are real signal.

### Physical interpretation

The mathematics of this section is the reason two geophysical groups can invert the
same data and report different models without either being wrong. The norm is the
metric of the data space, and the metric is a physical assertion: $L^2$ says the
noise is Gaussian, $L^1$ says it is heavy-tailed, a weighted norm says the
measurement uncertainties are as stated, and a correlation-weighted norm says the
errors are correlated. Section 8 shows the consequence in numbers — a 19.6 per cent
bias in the fitted slowness under $L^2$ and none under $L^1$. The second physical
content is the *units*: an unweighted sum of squared residuals in mixed units is
dimensionally meaningless, so any misfit quoted without its weights is not a
physical quantity at all.

## 9. Python demonstration

`code/function_spaces.py` carries out the five checks quoted above, in this
order:

1. the three norms of $f(x) = x(1-x)$ against closed forms, with the quadrature
   error reported;
2. Minkowski and Hölder, with the slacks and the ratio to the bound;
3. convergence in $L^2$ but not in $L^\infty$ for $f_n(x) = x^n$;
4. the areas of the unit balls in $\mathbb{R}^2$ and the measured
   finite-dimensional equivalence constants;
5. the $L^2$, $L^1$ and $L^\infty$ fits of the pick set of Section 8.

It uses the Python standard library only and runs in about three seconds.

> **Breaking exercise.** Before running it, predict what happens to the
> equivalence constant $\max \lVert x\rVert_1/\lVert x\rVert_2$ if the random
> vectors are drawn from a heavy-tailed distribution instead of a Gaussian. Then
> add that case and explain the result in terms of the geometry of the norm
> balls: the maximum is attained by a vector concentrated on a few components,
> and a heavy-tailed distribution produces exactly those vectors more often.

## 10. Common mistakes

- **Comparing two models without naming the norm.** "Model A fits better than
  model B" is meaningless when A is better in $L^2$ and B in $L^\infty$, which
  Section 8 shows is normal.
- **Assuming the $L^2$-optimal model is the best model.** It is the
  maximum-likelihood model for one particular noise assumption. Change the
  assumption and the answer changes, as the table of Section 8 demonstrates.
- **Forgetting the quadrature weights.** $\sum_i r_i^2$ and $h\sum_i r_i^2$
  differ by $\sqrt{h}$, which silently corrupts any quoted convergence rate.
- **Unweighted least squares on data with different units or errors.** The
  weight is the metric; dropping it is choosing a metric by accident (typically
  one that lets the largest-magnitude data set decide everything).
- **Treating a point source or a point measurement as a function.** Both are
  functionals. Writing them as densities invites a division by zero that the
  mathematics is trying to prevent.
- **Believing the finite-dimensional equivalence theorem settles the choice.**
  The constants grow like $\sqrt{n}$; at $n = 10^4$ they are already $10^2$.
- **Ignoring measure-zero differences.** A model changed at one point is the same
  element of $L^2$; no least-squares method can detect the change.

## 11. Real-world applications

- **Travel-time tomography.** The misfit is a norm in data space; robust norms
  (Huber, $L^1$) are used precisely because pick errors are heavy-tailed. The
  norm choice determines which arrivals are allowed to be wrong.
- **Gravity and magnetic inversion.** Weighted $L^2$ is standard because the
  noise is closer to Gaussian after levelling; conversion to a norm with units
  (Eötvös, mGal) makes the residual interpretable.
- **Full-waveform inversion.** The misfit is an $L^2$ norm on waveforms, and its
  notorious cycle-skipping is a statement about that norm: $L^2$ on oscillatory
  signals is a poor measure of phase agreement, which is why
  correlation-based and $L^1$ misfits were introduced.
- **Joint inversion.** Combining two data sets means combining two norms; the
  weighting between them is a metric choice in a direct product space.
- **Uncertainty quantification.** A norm on model space is what converts a
  posterior covariance into a scalar resolution or error estimate, and the
  estimate changes with the norm.
- **Machine-learning surrogates.** A network trained to minimise $L^2$ error is
  trained for Gaussian noise, and the failure of such surrogates on outliers is
  the same fact as Section 8.

## 12. Further reading

- **Kreyszig, E. (1978). *Introductory Functional Analysis with Applications*.
  Wiley.** Level: advanced. The standard entry point: normed spaces, Banach and
  Hilbert spaces, completeness, with worked problems.
- **Rudin, W. (1991). *Functional Analysis* (2nd ed.). McGraw-Hill.** Level:
  doctoral. The reference for the $L^p$ theory, duality and the theorems this
  module states without proof.
- **Aster, R. C., Borchers, B., & Thurber, C. H. (2018). *Parameter Estimation
  and Inverse Problems* (3rd ed.). Academic Press.** Level: graduate. Weighted
  least squares, the norm on data space, and the misfit choices of Section 8, in
  the form used by working geophysicists.
- **Menke, W. (2018). *Geophysical Data Analysis: Discrete Inverse Theory*
  (4th ed.). Academic Press.** Level: graduate. The classic text; the geometry of
  model and data spaces and the role of norms is treated accessibly.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model
  Parameter Estimation*. SIAM.** Level: graduate. Norms and distances in model
  and data spaces as the foundation of a probabilistic formulation.
- **Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge
  University Press.** Level: graduate. Norm balls as constraint sets, and why
  $L^1$ gives sparsity and $L^2$ does not.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 13. Exercises

Solutions are in
[`exercises/01-function-spaces-solutions.md`](./exercises/01-function-spaces-solutions.md),
and the problems are in
[`exercises/01-function-spaces-exercises.md`](./exercises/01-function-spaces-exercises.md).

**★1.** Verify the three norm axioms for $\lVert f\rVert_\infty$ on $C[0,1]$ and
exhibit the failure of (N1) for $L^1$ if functions are treated as pointwise
objects.

**★2.** Compute $\lVert f\rVert_1$, $\lVert f\rVert_2$ and
$\lVert f\rVert_\infty$ for $f(x) = \sin(\pi x)$ on $[0,1]$, in closed form and
by quadrature, and report the three ratios.

**★★3.** Show that $\lVert f\rVert_p$ is non-increasing in $p$ for $f$ of finite
measure, and give an example on $[0,1]$ where the three norms differ by more than
a factor of 3.

**★★4.** Verify Hölder's inequality for $p = 1, q = \infty$ and state the
equality condition. Use it to bound the gravity datum $\ell(m) = m(x_0)$ and
explain why a bound in $L^2$ is unavailable.

**★★5.** Reproduce the pick-fit table of Section 8, then repeat it with the
outlier reduced from $+1.8$ s to $+0.2$ s and report how the $L^2$ slope changes.
Interpret the result.

**★★6.** Prove that the finite-dimensional constant
$\max_{\lVert x\rVert_2 \le 1}\lVert x\rVert_1 = \sqrt{n}$ and verify the
measured values in the demonstration against it.

**★★★7.** Implement a Huber misfit with threshold $\gamma$, fit the pick set,
and report the recovered slope as a function of $\gamma$ between $0.05$ and
$2.0$. Identify the $\gamma$ at which the fit changes character between the $L^1$
and $L^2$ answers of Section 8, and explain the transition.

**★★★8.** Take the weighted norm $\chi^2 = \sum (r_i/\sigma_i)^2$ with
$\sigma_i = 0.05 + 0.02 x_i$ and refit the pick set. Compare with the unweighted
$L^2$ fit and state precisely which data the weighting made more important.

## 14. Self-assessment checklist

- [ ] I can state the three norm axioms and check them for a proposed norm.
- [ ] I can write the $L^p$, supremum and weighted norms, and identify which one
      a given inversion code minimises.
- [ ] I can explain what an inner product adds to a norm and why $L^p$ for
      $p \neq 2$ has no orthogonality.
- [ ] I can demonstrate convergence in one norm without convergence in another,
      and quote the finite-dimensional equivalence constants.
- [ ] I can argue from the error distribution to the choice of misfit norm, with
      a numerical example where the choice changes the answer.
- [ ] I can explain why a point source and a point measurement are functionals
      rather than functions, and why that matters for weak formulations.
- [ ] I can state the hypotheses (integration, finite measure, completeness) and
      one concrete way each can fail in practice.

## Related lessons

- [01-07-01 Vectors, Vector Spaces and Basis](../07-linear-algebra/01-vectors-and-spaces.md)
  — the finite-dimensional version of this lesson, with the same axioms.
- [01-07-07 Orthogonality, Projections and Least Squares](../07-linear-algebra/07-orthogonality.md)
  — least squares as a geometric construction, which lesson 01-16-02 lifts to
  function spaces.
- [01-05-07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md)
  — convergence, and the pointwise-versus-uniform distinction of Section 6.
- [01-09-08 Weak Solutions, Variational Forms and Well-Posedness](../09-partial-differential-equations/08-weak-solutions.md)
  — where $H^1$, the dual space and the data functional are used in anger.
- [01-10-02 The Fourier Transform and Its Properties](../10-fourier-analysis/02-fourier-transform.md)
  — a different basis for the same function space, and the convergence questions
  it raises.
- [01-16-02 Hilbert Spaces and Orthogonal Expansions](./02-hilbert-spaces.md) —
  the next lesson, which adds completeness and turns geometry into algorithms.
- [01-16-05 Ill-Posedness in the Sense of Hadamard](./05-ill-posedness.md) — what
  goes wrong when a normed-space formulation is inverted.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the norms and
  data weights of this lesson in operational use.
