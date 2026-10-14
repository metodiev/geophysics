---
id: 01-12-03
title: "Numerical Differentiation and Finite-Difference Stencils"
level: advanced
prereqs: ["01-01-04", "01-05-04", "01-06-01"]
estimated_minutes: 90
tags: [numerical-methods, finite-differences, round-off, errors]
---

# Numerical Differentiation and Finite-Difference Stencils

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the leading truncation term of the forward, backward and centred
   difference from Taylor expansions, and state the degree of polynomial each is
   exact on.
2. **Distinguish** the three error sources that afflict a numerical derivative —
   truncation, round-off and observation noise — and say which parameter each
   responds to.
3. **Predict and verify** the optimal step size: proportional to $u^{1/2}$ for a
   forward difference and to $u^{1/3}$ for a centred difference, where $u$ is the
   unit roundoff.
4. **Apply** Richardson extrapolation to raise the order of a stencil by one.
5. **Compute** a gravity gradient or a strain rate from sampled data, and state
   the resolution at which the result stops being meaningful.
6. **Design** a stencil of arbitrary order for a given grid, including one-sided
   stencils near a boundary.

## Prerequisites

[01-01-04 Floating-Point Representation, Round-Off and Catastrophic
Cancellation](../01-arithmetic/04-floating-point.md) — the error floor that sets
the optimal step. [01-05-04 Taylor Series](../05-single-variable-calculus/04-taylor-series.md)
— every derivation here is one Taylor expansion. [01-06-01 Partial
Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) — the
multi-dimensional case, where mixed stencils and the Laplacian appear.

## 1. Intuition: differentiation amplifies; integration damps

Integration averages and therefore suppresses error. Differentiation does the
opposite: two nearby samples with independent errors of size $\sigma$ produce a
difference of size $\sigma\sqrt2$, and dividing by a small interval $h$ gives an
error of order $\sigma/h$. **The derivative of sampled data is a high-pass filter
applied to noise.**

This has three consequences that shape the whole subject.

1. There is a **trade-off**, not a single right answer. Making $h$ smaller
   reduces the truncation error (which scales like a power of $h$) but increases
   the round-off error (which scales like $1/h$). The total error has an interior
   minimum, and the location of that minimum is a computable number.
2. The trade-off's **scaling depends on the stencil**. A forward difference has an
   $O(h)$ truncation term, so its optimum is $h^\* \propto u^{1/2}$; a centred
   difference has an $O(h^2)$ term, so its optimum is $h^\* \propto u^{1/3}$.
   These two exponents are routinely confused. Both are measured in the
   demonstration below, with fitted slopes $+0.4775$ and $+0.3329$ against the
   theoretical $+0.5$ and $+0.3333$.
3. Data noise sets a **floor that no stencil can remove**. If the samples carry
   error $\sigma$, the derivative error has a contribution $\sim\sigma/h$ that
   grows as $h$ shrinks no matter how the difference is formed. Beyond a certain
   resolution, differentiation must be replaced by smoothing or by model fitting.

## 2. Precise definitions

### 2.1 Stencils and their design order

For a uniform grid $x_i = x_0 + ih$, the **forward difference** is

$$D^{+}f(x_i) = \frac{f_{i+1}-f_i}{h},$$

the **backward difference** $D^{-}f(x_i) = (f_i-f_{i-1})/h$, and the **centred
difference**

$$D^{0}f(x_i) = \frac{f_{i+1}-f_{i-1}}{2h}.$$

The **second centred difference** is

$$D^{0}_2 f(x_i) = \frac{f_{i+1}-2f_i+f_{i-1}}{h^2}.$$

A stencil's **degree of exactness** is the highest polynomial degree on which it
is exact, and it equals its leading truncation order. The demonstration verifies
the degrees directly on monomials $x^p$: the forward difference is exact only for
$p\le1$, the centred difference for $p\le2$, and the centred second difference for
$p\le3$.

### 2.2 The error decomposition

Let $\hat f_i$ be the computed value, $\hat f_i = f(x_i)(1+\delta_i)$ with
$|\delta_i|\le u$, and let $\epsilon_i$ be an additive observational error with
standard deviation $\sigma$. The computed derivative satisfies

$$D^{\text{comp}} = D^{\text{exact}} + \underbrace{E_{\text{trunc}}(h)}_{\text{stencil}}
+ \underbrace{E_{\text{round}}(h,u)}_{\text{arithmetic}}
+ \underbrace{E_{\text{noise}}(h,\sigma)}_{\text{data}} ,$$

with, for a centred difference on a function of magnitude $|f|$,

$$E_{\text{trunc}} = \frac{|f'''|}{6}h^2, \qquad
E_{\text{round}} \approx \frac{u|f|}{h}, \qquad
E_{\text{noise}} = \frac{\sigma}{h\sqrt2} .$$

The two last terms have the same $1/h$ structure, and they are routinely
conflated. They are different in kind: round-off is deterministic for a given
implementation (and can be reduced by extended precision or compensated
summation), while noise is a property of the data and can only be reduced by
smoothing or by fitting a model.

## 3. Derivations

### 3.1 Truncation terms from Taylor series

Expand forwards and backwards:

$$f_{i\pm1} = f_i \pm h f_i' + \frac{h^2}{2}f_i'' \pm \frac{h^3}{6}f_i'''
+ \frac{h^4}{24}f_i'''' + \cdots$$

Subtracting the backward from the forward expansion gives

$$f_{i+1}-f_{i-1} = 2hf_i' + \frac{h^3}{3}f_i''' + O(h^5)
\quad\Longrightarrow\quad
D^{0}f_i = f_i' + \frac{h^2}{6}f_i''' + O(h^4),$$

while subtracting $f_i$ gives $D^{+}f_i = f_i' + \frac{h}{2}f_i'' + O(h^2)$. So the
forward stencil's leading error is $O(h)$ with coefficient $f''/2$, and the
centred stencil's is $O(h^2)$ with coefficient $f'''/6$. Adding the two expansions
instead gives the second difference, $f_{i+1}-2f_i+f_{i-1} = h^2f_i'' +
\frac{h^4}{12}f_i''''+O(h^6)$, i.e. an $O(h^2)$ error with coefficient
$f''''/12$.

### 3.2 The optimal step, derived

For a forward difference the total error model is

$$E(h) \approx \frac{|f''|}{2}h + \frac{u|f|}{h},
\qquad \frac{dE}{dh} = \frac{|f''|}{2} - \frac{u|f|}{h^2} = 0
\quad\Longrightarrow\quad
h^\*_{\text{fwd}} = \sqrt{\frac{2u|f|}{|f''|}} \propto u^{1/2}.$$

For a centred difference,

$$E(h) \approx \frac{|f'''|}{6}h^2 + \frac{u|f|}{h},
\qquad \frac{dE}{dh} = \frac{|f'''|}{3}h - \frac{u|f|}{h^2} = 0
\quad\Longrightarrow\quad
h^\*_{\text{ctr}} = \left(\frac{3u|f|}{|f'''|}\right)^{1/3} \propto u^{1/3}.$$

**The exponent is the reciprocal of the order of the leading truncation term plus
one**: $1/(1+1) = 1/2$ for the first-order stencil and $1/(2+1)=1/3$ for the
second-order one. A third-order stencil would give $u^{1/4}$. At $u =
2.2\times10^{-16}$ the two numbers are $1.5\times10^{-8}$ and $6.0\times10^{-6}$ —
the centred stencil tolerates a step about $10^3$ times larger. This is not a
detail; it is the practical reason to use a centred stencil whenever the function
can be evaluated on both sides.

### 3.3 Measuring the exponent

To verify the exponents numerically rather than merely assert them, the
demonstration simulates reduced-precision arithmetic by rounding each function
value to a multiple of a prescribed $u$, scans $\log h$ over 16 decades for the
error-minimising step, and fits a line to $\log h^\*$ against $\log u$. Because a
single minimiser is quantised by the scan grid, the estimate is averaged over five
evaluation points $x$ for each $u$. The fitted slopes are

$$\text{forward: } +0.4775, \qquad \text{centred: } +0.3329,$$

against the theoretical $+0.5000$ and $+0.3333$. The measured constants
$h^\*/u^{1/2}$ and $h^\*/u^{1/3}$ scatter by a factor of a few, which is expected
because they depend on the local derivatives $f''$ and $f'''$ through the ratios
$2|f|/|f''|$ and $3|f|/|f'''|$.

### 3.4 Richardson extrapolation

Combining two evaluations of the same stencil at $h$ and $h/2$ cancels the
leading error term. For the forward difference, whose error is $C_1h+O(h^2)$,

$$D_R = 2D^{+}(h/2) - D^{+}(h) = f' + O(h^2),$$

and for the centred difference, whose error is $C_1h^2+O(h^4)$,

$$D_R = \frac{4D^{0}(h/2)-D^{0}(h)}{3} = f' + O(h^4).$$

The demonstration measures the resulting orders as 2.00 and 4.00–4.03, and the
cost is one extra stencil evaluation. The price is cancellation: the combination
subtracts two nearly equal numbers, so the round-off term grows and the optimal
step shifts to a larger $h$.

### 3.5 Higher-order and one-sided stencils

Any set of $m$ abscissae can be turned into a derivative stencil by solving the
moment conditions $\sum_j w_j (x_j-x_c)^p = \delta_{p,1}\,p!$ for $p=0,\dots,m-1$.
A five-point centred first derivative, for example, is

$$f'_i \approx \frac{-f_{i+2}+8f_{i+1}-8f_{i-1}+f_{i-2}}{12h} + O(h^4),$$

and at a boundary one uses a one-sided stencil of the same order,

$$f'_0 \approx \frac{-3f_0+4f_1-f_2}{2h}+O(h^2),$$

so that the boundary does not degrade the global order. This is exactly the
mechanism that made the *natural* cubic spline second-order in
[01-12-02](./02-interpolation.md): the wrong boundary treatment costs orders.

## 4. Physical interpretation

- **Gravity gradients.** The vertical gradient of gravity is what a gradiometer
  measures and what a structural interpretation reads. Differentiating a
  profile amplifies terrain and drift errors by $1/h$, so the achievable
  resolution is set by the survey's repeatability, not by the grid spacing.
- **Strain rates from GNSS.** Displacement time series are differenced in time.
  With daily solutions having 1–2 mm precision, a strain rate over a 10 km
  baseline is measurable over months but not over days, and the reason is
  $E_{\text{noise}} = \sigma/(h\sqrt2)$.
- **Electromagnetic and seismic attributes.** Apparent resistivity from a
  Schlumberger sounding requires a logarithmic derivative, where the step is a
  ratio rather than a difference; the same trade-off appears with $\ln r$ in
  place of $h$.
- **Edge detection on potential-field maps.** The horizontal gradient magnitude
  and the tilt derivative are finite-difference operators applied to grids, and
  the noise penalty is the price of the sharpened edges.

## 5. Assumptions and regime of validity

| Statement | Requires |
|---|---|
| $D^0$ has error $\frac{h^2}{6}f'''$ | $f\in C^4$ on the interval; a uniform grid |
| $D^+$ has error $\frac{h}{2}f''$ | $f\in C^3$; a uniform grid |
| Optimal step $\propto u^{1/2}$ (forward) | the truncation and round-off terms are the only errors, and $f''\neq0$ |
| Optimal step $\propto u^{1/3}$ (centred) | same, with $f'''\neq0$ |
| Richardson doubles the order | the error is a smooth power series in $h$; not at a kink |
| The measured order is the design order | $h$ is in the asymptotic range and round-off is not yet dominant |

Two regimes must be distinguished in practice. In the **asymptotic range** — $h$
small enough that the leading term dominates, large enough that round-off does
not — the order is visible and the formulas above hold. Outside it, the measured
error is dominated by whichever term happens to be largest, and an order measured
there is meaningless. The demonstration's error table shows the handover
explicitly: for the forward difference the observed error tracks
$|f''|h/2$ down to $h \approx 10^{-7}$ and then departs upward; for the centred
difference the departure begins near $h \approx 10^{-5}$.

A final caveat on **noise**. When the samples are data rather than a function, the
$1/h$ term is $\sigma/h$, and it is typically three to five orders of magnitude
larger than $u|f|/h$ for realistic survey precision. The optimum then occurs at
a much larger $h$, and no manipulation of the arithmetic helps.

## 6. Python demonstration

The script `code/numerical_differentiation.py` implements the stencils, measures
the design orders on monomials, sweeps $h$ for the error curve, measures the two
optimal-step exponents, applies Richardson extrapolation, and differentiates a
synthetic gravity profile with and without noise. Selected output:

```text
  Monomials f(x) = x^p at x = 0.7, h = 0.1
    p     exact df/dx     forward     centred  exact d2f/dx2     centred2
    1        1.000000    1.000000    1.000000        0.000000     0.000000
    2        1.400000    1.450000    1.400000        2.000000     2.000000
    3        1.470000    1.570000    1.470000        4.200000     4.200000
    4        1.372000    1.522000    1.372000        5.880000     5.880000

  f(x) = sin x at x = 1.0:  exact derivative = 0.5403023058681398
           h    fwd error    fwd trunc    ctr error    ctr trunc
    1.00e-01    4.294e-02    4.207e-02    9.001e-04    9.005e-04
    1.00e-03    4.208e-04    4.207e-04    9.005e-08    9.005e-08
    1.00e-05    4.207e-06    4.207e-06    1.114e-11    9.005e-12
    1.00e-07    4.183e-08    4.207e-08    1.943e-10    9.005e-16
    1.00e-09    2.631e-08    1.330e-09    8.759e-09    9.005e-19

           u    h* forward     h* u^-0.5    h* centred     h* u^-0.333
     1.0e-06     1.480e-04        0.1480     8.477e-03          0.8477
     1.0e-10     3.890e-06        0.3890     4.178e-04          0.9001
     1.0e-16     4.115e-09        0.4115     3.006e-06          0.6475
  fitted log-log slope, forward  = +0.4775  (theory +0.5000)
  fitted log-log slope, centred  = +0.3329  (theory +0.3333)
```

The gravity-gradient experiment:

```text
  SYNTHETIC sphere: M = 1e+12 kg at depth 500 m,
  profile sampled at x = 250 m; exact gradient = -3.417088e-02 mGal/m
   spacing h (m)     centred error    relative error
             1.0         1.312e-07         3.840e-06
            20.0         5.246e-05         1.535e-03
           250.0         7.475e-03         2.187e-01

  Now add OBSERVED-LIKE noise of 0.01 mGal (s.d.) to the profile.
       h (m)     RMS error    relative   predicted noise    truncation
         5.0     1.150e-03   3.365e-02         1.414e-03     8.197e-07
        25.0     3.379e-04   9.889e-03         2.828e-04     2.025e-05
       100.0     1.310e-03   3.833e-02         7.071e-05     2.539e-04
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Forward exact only for $p\le1$, centred for $p\le2$ | degree of exactness is the design order, and it is visible in one line |
| Observed error equals the truncation formula for large $h$ | the stencil's order is a real, checkable property |
| Error rises like $1/h$ below the optimal step | round-off, not the stencil, is then the limit |
| Fitted slopes 0.4775 and 0.3329 | the two exponents are different and each belongs to a specific stencil |
| Richardson takes order 1 → 2 and 2 → 4 | one extra evaluation buys a whole order |
| With 0.01 mGal noise the RMS minimum sits near $h=25$ m | data noise, not arithmetic, sets the resolution |
| Predicted noise $0.01/(h\sqrt2)$ matches the measured RMS | the $\sigma/(h\sqrt2)$ model for a centred difference is adequate |

> **Breaking exercise.** Reduce the noise standard deviation in the last section
> from 0.01 mGal to 0.001 mGal and predict, before running, by what factor the
> RMS error at $h=5$ m changes. Then run it. Finally, hold the noise fixed and
> change the sampling interval `step` from 5 m to 1 m, and explain what changes
> and what does not.

## 7. Common mistakes

1. **Using the wrong exponent.** The optimal step for a forward difference is
   $\propto u^{1/2}$ and for a centred difference $\propto u^{1/3}$. Quoting one
   for the other is a factor-of-1000 error in the recommended step at double
   precision.
2. **Assuming smaller $h$ is always better.** Below the optimum the error grows.
   In the demonstration the forward-difference error at $h=10^{-9}$ is larger
   than at $h=10^{-6}$.
3. **Confusing round-off with noise.** A $1/h$ term in the error does not tell
   you which one it is. The diagnostic is to change the precision of the
   arithmetic (round-off changes) or the number of realisations (noise changes).
4. **Differentiating an interpolant to get a derivative.** The interpolation and
   derivation errors add, and the derivation amplifies the interpolation
   oscillation — the worst possible combination around a boundary.
5. **Applying Richardson extrapolation to noisy data.** The cancellation it
   relies on is exactly what noise destroys; extrapolate above the noise floor
   only.
6. **Ignoring the boundary.** A one-sided first-order stencil at a boundary
   degrades the whole grid to first order. Use a one-sided stencil of the same
   order, or a ghost node.
7. **Forgetting the grid is not uniform.** Every formula here assumes constant
   $h$. On an irregular grid the stencils must be re-derived, and the truncation
   order can quietly drop.

## 8. Real-world applications

- **Gravity gradiometry.** Airborne and satellite gradiometers measure the
  second derivatives of the potential directly, which is the only way to obtain
  them without the $1/h$ amplification of differentiating the field itself.
- **GNSS strain and interseismic coupling.** Velocity fields are differentiated
  in space to obtain strain rates; the practical resolution is set by the
  station spacing and the monument stability, and the error model above is what
  an uncertainty budget must use.
- **Potential-field edge detection.** The tilt derivative and the theta map are
  finite-difference operators; their thresholds are chosen in practice by
  balancing edge sharpening against the noise gain, which is an explicit
  application of §5.
- **Seismic attribute analysis.** Instantaneous frequency and dip are derivatives
  of phase and of travel time; the same trade-off appears as a choice of window
  length in the attribute computation.
- **Numerical modelling.** Every finite-difference scheme in
  [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) is a
  stencil of the kind derived here, and the truncation/round-off balance is what
  fixes the usable grid spacing in production.

## 9. Further reading

- **Fornberg, B. (1988). Generation of finite difference formulas on arbitrarily
  spaced grids. *Mathematics of Computation*, 51(184), 699–706.** Level:
  graduate. The general algorithm for constructing stencils of arbitrary order
  on arbitrary nodes, of which §3.5 is the simplest case.
- **Fornberg, B. (1996). *A Practical Guide to Pseudospectral Methods*. Cambridge
  University Press.** Level: graduate. What to do when finite differences are not
  accurate enough, and how the choice relates to the grid.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Level: graduate. Chapter 1 is the standard careful treatment
  of the truncation/round-off trade-off and of the $\sqrt{u}$ scaling.
- **Burden, R. L., & Faires, J. D. (2010). *Numerical Analysis* (9th ed.).
  Brooks/Cole.** Level: undergraduate. Chapter 4 covers the classical stencils
  with the error terms derived in the same way as here.
- **Kahaner, D., Moler, C., & Nash, S. (1989). *Numerical Methods and Software*.
  Prentice Hall.** Level: undergraduate to graduate. Includes the practical
  advice on Richardson extrapolation that §3.4 summarises.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Full statements and difficulty grading are in
[`exercises/03-numerical-differentiation-exercises.md`](./exercises/03-numerical-differentiation-exercises.md),
with worked solutions in
[`exercises/03-numerical-differentiation-solutions.md`](./exercises/03-numerical-differentiation-solutions.md).

**★1.** Derive the truncation term of $D^{+}f_i$ and of $D^{-}f_i$ and show they
differ in sign.

**★2.** Verify that $D^0_2$ is exact on cubics and find its leading error term.

**★3.** For $u = 2.2\times10^{-16}$, $|f| = 1$, $|f''| = 2$ and $|f'''| = 6$,
compute the optimal step for the forward and centred stencils and the resulting
minimum errors.

**★4.** A gravity profile is sampled at 20 m and read to 0.01 mGal. Estimate the
smallest $h$ at which a centred difference of the gradient is dominated by
truncation rather than noise.

**★★5.** Construct the five-point centred first-derivative stencil from the
moment conditions and verify its $O(h^4)$ error on $\sin x$.

**★★6.** Derive the one-sided third-order stencil for $f'_0$ using $f_0,f_1,f_2,f_3$
and state the truncation term.

**★★7.** Show that applying step doubling to $D^{+}$ gives order 2 for *any*
smooth $f$, and that applying it twice more gives order 3 — and explain why the
first argument does not generalise to the centred stencil.

**★★8.** A strain rate is estimated from two GNSS stations 12 km apart, each with
1.5 mm of daily horizontal precision. Compute the noise floor of the strain rate
over one day and over one year, and state the conditioning assumption about the
baseline.

**★★★9.** Design and run a numerical experiment that distinguishes round-off from
data noise in the differentiation error of a centred stencil. Specify the
diagnostic, the predicted scaling under each hypothesis, and the result of your
experiment with numbers.

**★★★10.** A colleague reports a gravity gradient map computed on a 250 m grid
from readings with 0.02 mGal repeatability, and asks whether a finer grid would
improve the map. Using the models of this lesson, answer with numbers and state
the single most useful additional measurement.

## 11. Self-assessment checklist

- [ ] I can derive the leading truncation term of any three-point stencil from
      Taylor expansions without notes.
- [ ] I can state the degree of exactness of the forward, centred and centred-second
      stencils.
- [ ] I can derive the optimal step for both stencils, obtaining $u^{1/2}$ and
      $u^{1/3}$, and explain in words why the exponents differ.
- [ ] I can measure a convergence order from an error sequence and say whether
      the range of $h$ is asymptotic.
- [ ] I can write down the Richardson combination for each stencil and state the
      resulting order.
- [ ] I can model the noise contribution of a centred difference as
      $\sigma/(h\sqrt2)$ and use it to pick a usable $h$.
- [ ] I can name the three error sources and, for each, the parameter that
      reduces it.

## Related lessons

- [01-12-02 Interpolation, Splines and Approximation Theory](./02-interpolation.md)
  — the interpolant whose derivative you might be tempted to use instead, and why
  that is usually worse.
- [01-12-04 Numerical Integration: Trapezoid, Simpson, Gauss Quadrature](./04-numerical-integration.md)
  — the opposite trade-off: quadrature suppresses the error that differentiation
  amplifies.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](./07-pde-discretisation.md)
  — the same stencils assembled into a scheme, where the truncation error becomes
  the local truncation error of the PDE solve.
- [01-06-01 Partial Derivatives](../06-multivariable-calculus/01-partial-derivatives.md)
  — the multi-dimensional stencils, including the Laplacian.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  these stencils as they appear in production modelling codes.
