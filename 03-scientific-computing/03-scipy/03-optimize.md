---
id: 03-03-03
title: "scipy.optimize: Root Finding, Minimisation and Curve Fitting"
level: intermediate
prereqs: ["03-03-01", "01-05-02", "03-02-05"]
estimated_minutes: 75
tags: [optimization, curve-fitting, root-finding, least-squares, uncertainty]
---

# scipy.optimize: Root Finding, Minimisation and Curve Fitting

`scipy.optimize` answers three questions that look different and are not.
**Where is the zero?** (root finding) **Where is the minimum?** (minimisation)
and **what parameters best explain these data, and how well are they
determined?** (fitting). All three are local, iterative and start-point
dependent, and all three will return an answer that satisfies their internal
stopping test whether or not that answer is the one you wanted.

The purpose of this lesson is to make the distinction between *converged* and
*correct* operational. It does that by fitting a decay curve with honest error
bars, inverting an equation of state, and counting function evaluations to
find out what an analytic derivative is actually worth.

Run the demonstration before reading on:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/optimize_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Fit** a non-linear model with `curve_fit` and convert its covariance
   matrix into 1σ parameter errors.
2. **Interpret** `absolute_sigma=True` against `absolute_sigma=False`, and
   state which one is honest when the measurement uncertainty is known.
3. **Detect** a degenerate parameter pair from the correlation matrix, and
   demonstrate that the degeneracy is usually a property of the sampled
   window rather than of the data.
4. **Choose** between `brentq`, `newton`, `fsolve` and `root_scalar` for a
   scalar root, and explain what a bracketing method guarantees that an
   open method does not.
5. **Explain** why a root finder returns one root of an equation with several,
   and why the returned root is not evidence that it is the only one.
6. **Compare** `least_squares` with `minimize`, with and without an analytic
   Jacobian, using function-evaluation counts rather than timings.
7. **State** what `res.success` means, and what it does not.

## Prerequisites

- [03-03-01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — the subpackage map.
- [01-05-02 Derivatives and Rates of Change](../../01-mathematics/05-single-variable-calculus/02-derivatives.md)
  — what a derivative is, which is what a Jacobian generalises.
- [03-02-05 Linear Algebra with numpy.linalg](../02-numpy/05-linear-algebra-numpy.md)
  — matrix products and inverses, which is what the covariance matrix is.
- [01-14-04 Least Squares](../../01-mathematics/14-optimization/04-least-squares.md)
  — the normal equations and why the problem is called linear least squares
  even when the model is not.

## 1. Curve fitting with an honest error bar

The geophysical task is a cooling anomaly: a temperature difference that
decays exponentially towards a background,

$$\Delta T(t) = A e^{-t/\tau} + c . \tag{1}$$

The demo builds synthetic data from $A = 95$ K, $\tau = 3000$ yr, $c = 4$ K
with 25 samples and Gaussian noise of known $\sigma = 1.5$ K, then fits with
an intentionally poor start guess $(50, 1000, 0)$:

```
  absolute_sigma=True   ->  reduced chi^2 = 1.243904
    parameter         fitted     1 sigma       truth  difference/sigma
    A (K)            94.7625      1.0974     95.0000              0.22
    tau (yr)       3051.1401     91.8566   3000.0000              0.56
    offset (K)        4.1972      0.7332      4.0000              0.27
```

`curve_fit` returns two things: the parameters and their covariance matrix.
The square roots of the diagonal of that matrix are the 1σ errors, *under
the assumptions listed at the end of this lesson*. Here all three parameters agree with the
truth within 0.6σ, and the reduced $\chi^2$ is 1.24.

The reduced $\chi^2$ is the single most useful second number in a fit. With
$n$ data points and $p$ parameters, $\chi^2_\nu = \chi^2/(n-p)$ has
expectation 1 when the model is right and the errors are the stated ones.
Values near 1 mean the model and the errors are mutually consistent; large
values mean underestimated errors or a model that misses structure; small
values mean overestimated errors or an over-fitted model.

### 1.1 `absolute_sigma` is not a detail

The same fit with `absolute_sigma=False`:

```
  absolute_sigma=False  ->  reduced chi^2 = 1.243904
    A (K)            94.7625      1.2239     95.0000              0.19
    tau (yr)       3051.1401    102.4480   3000.0000              0.50
    offset (K)        4.1972      0.8178      4.0000              0.24
```

The parameters are identical. The error bars are not: every one is larger by
a factor $\sqrt{1.2439} = 1.115$, which is exactly the factor that makes the
reduced $\chi^2$ equal to 1 by construction. The reported `1 sigma` column
then means "the error bar that would be consistent with this model", not "the
error bar implied by my measurement uncertainty".

> If you know σ from the instrument, use `absolute_sigma=True`. If you do not,
> use `False` and be aware that the error bars are then a statement about
> scatter, not about accuracy. Using `False` while knowing σ is a way of
> hiding a bad fit inside wider error bars.

### 1.2 The correlation matrix, and why a parameter can be unconstrained

The normalised covariance matrix is the parameter correlation matrix:
$r_{ij} = C_{ij}/\sqrt{C_{ii}C_{jj}}$, whose diagonal is 1. Fitting the same
model over one time constant and over four:

```
            window   corr(A, tau)  corr(tau, offset)  sigma_tau (yr)
           0-1 tau        0.96748           -0.98870           316.4
           0-4 tau       -0.07537           -0.83141            94.9
```

Over one time constant, $A$ and $\tau$ are nearly perfectly correlated
($r = +0.967$): raising the two *together* in proportion leaves the initial
slope $A/\tau$ unchanged, and the fit responds only through the second-order
term. The data constrain $A/\tau$ and very little else, and $\sigma_\tau$ is
316 yr. Over four time constants the correlation is gone
($r = -0.075$) and $\sigma_\tau$ is 95 yr — 3.3 times smaller.

**A parameter pair that reports "unconstrained" is usually a sampling window
that is too short, and the remedy is more data of the right kind rather than a
better optimiser.** This is the single most common misdiagnosis in
geophysical curve fitting: the fit reports a 50% error on a decay constant,
and the response is to try a different algorithm, when the response should be
to look at the range of the abscissa in units of the decay constant.

## 2. Root finding: inverting an equation of state

A different task with the same flavour: given a pressure, what volume does a
material have? For the Earth's mantle the standard answer is the third-order
Birch–Murnaghan isotherm,

$$P(V) = \tfrac32 K_0\left[\left(\tfrac{V}{V_0}\right)^{-7/3}
- \left(\tfrac{V}{V_0}\right)^{-5/3}\right]
\left\{1 + \tfrac34 (K_0'-4)\left[\left(\tfrac{V}{V_0}\right)^{2/3}-1\right]\right\} ,
\tag{2}$$

which is written $P(V)$ and must be inverted numerically to give $V(P)$. With
$K_0 = 260$ GPa and $K_0' = 4$ (parameters chosen for the demonstration, not
literature values) and a target of 135 GPa:

```
    brentq        V/V0 = 0.748138742561   iterations = 11   residual P-P_target = +2.84e-14 GPa
    newton (analytic f')  V/V0 = 0.748138742561   iterations = 8   converged = True
    fsolve (MINPACK hybrd) V/V0 = 0.748138742561   nfev = 13
    root_scalar(brentq)   V/V0 = 0.748138742561   iterations = 11
    spread across the four methods = 9.437e-15 in V/V0
```

Four methods, four routes, one answer to 14 digits. The differences between
them are what you choose on:

| Routine | Derivative needed | Requirement | Guarantee |
|---|---|---|---|
| `brentq` | no | a **bracket** with a sign change | Convergence to a root inside the bracket |
| `brentqh`/`brenth` | no | same | Same, with faster convergence |
| `newton` (via `root_scalar`) | yes (or numeric) | a start point and $f' \ne 0$ | Local convergence, quadratic near the root |
| `fsolve` | no (numerical) | a start point | Local convergence; no guarantee of a root |
| `root_scalar(method='brentq')` | no | a bracket | Same as `brentq`, with a uniform interface |

**A bracket is a guarantee.** If $f(a)$ and $f(b)$ have opposite signs and $f$
is continuous, a root exists in $(a,b)$, and Brent's method will find one. No
open method can make that claim, and the demo shows what happens when the
claim is false:

```
    brentq(f, 2.2, 2.4) raises: ValueError
    f(a) and f(b) must have different signs
```

A bracket without a sign change is a **hard error**, not a wrong answer.
That is a feature.

### 2.1 The root finder finds the root you ask for

Take a cubic with three real roots, $x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)$:

```
      start x0    method    root found    residual
          0.00    fsolve      1.000000    1.78e-15
          1.40    fsolve      1.000000    5.33e-15
          1.60    fsolve      2.000000    0.00e+00
          2.50    fsolve      1.000000    1.78e-15
          4.00    fsolve      3.000000   -7.11e-15
```

Every call converged, with residuals at the level of round-off. Three of them
returned the root at 1 — including the one started at 2.5, which is nearer to
2. **The returned answer does not tell you how many solutions the equation
has.** For a geophysical equation of state with a phase transition, the
multiple roots are the multiple phases, and choosing one by accident is
choosing a physical state by accident. The remedy is to bracket the branch
you want, or to scan $f$ over the physically plausible range and count sign
changes before solving.

## 3. What a Jacobian buys

Now the fitting question in its general form. `scipy.optimize.least_squares`
minimises $\tfrac12\|r(p)\|^2$ and knows that the objective is a sum of
squares; `scipy.optimize.minimize` minimises a general $f(p)$ and does not.
For a model with four parameters and 60 samples, the demo counts evaluations:

```
    variant                                      resid vectors  jac eval  point evals
    least_squares(method=lm), finite-difference Jacobian            35         0         2100
    least_squares(method=lm), analytic Jacobian              8         8          960
```

The finite-difference route spent 35 residual-vector evaluations on about
seven implicit Jacobians that the user never sees, because a forward
difference costs $1 + n_\text{params} = 5$ residual vectors per Jacobian. The
analytic route formed 8 Jacobians directly and needed 8 residual vectors.
Counting one Jacobian as one residual vector of work: 2100 point evaluations
against 960, **a factor of 2.19 for four parameters.** The factor is
$1 + n_\text{params}$, so it grows with the size of the model.

What is *not* different is the answer:

```
    Accuracy is not the issue here: both reach the same minimum
    2*cost = 201.7906843312
    Parameters agree to max |relative| = 1.87e-08
```

The analytic Jacobian buys **evaluations, not accuracy** — unless the problem
is ill-conditioned, in which case it buys accuracy too, because a finite
difference of a nearly-cancelling quantity loses digits.

### 3.1 Putting the same sum of squares through `minimize`

```
    method              nfev                 RSS   max |rel. param diff|
    Nelder-Mead          356        201.79068433                5.70e-09
    Powell               267        201.79070141                6.90e-05
    BFGS                  32        201.79068433                1.57e-08
    L-BFGS-B              36        201.79068433                4.13e-07
```

Read the columns in order. All five reach the same RSS to at least seven
digits, so **the choice of optimiser is not a choice about the answer here —
it is a choice about cost.** Nelder-Mead needs 356 evaluations against BFGS's
32, an order of magnitude more, because it builds a simplex and never uses a
derivative. Powell stops slightly early at RSS 201.79070141 rather than
201.79068433, a relative difference of $8\times10^{-8}$ — small, but the
demo's last line is the point:

```
    Restarting the analytic fit at the solution: 1 residual evaluations
```

Starting from the reported solution, `least_squares` converges in one
evaluation. Convergence is a claim about the stopping test — gradient norm
below `gtol`, step below `xtol`, objective change below `ftol` — and not a
certificate that a global minimum has been found. For a least-squares
problem with a quadratic basin near the answer, that distinction rarely
matters. For a multimodal geophysical misfit it matters always.

The practical rules:

- **If you can write $r(p)$, use `least_squares`.** It exploits the structure
  and gives you the Jacobian, the covariance estimate and bounds.
- **If you have a Jacobian, pass it.** The saving is a factor of
  $1+n_\text{params}$ and it is measurable (§3).
- **If the objective is not a sum of squares, or you cannot differentiate it,
  use `minimize`** and start with Nelder-Mead or Powell to find the basin, then
  refine with BFGS or `least_squares`. This two-stage pattern is the standard
  answer to "the fit converges to something different depending on the start
  guess".
- **Use `least_squares(method='trf', bounds=...)`** when parameters have
  physical limits (a positive decay constant, a depth greater than zero). The
  Levenberg–Marquardt method used above does not accept bounds; `trf` and
  `dogbox` do.

## Worked code

Fitting with uncertainty, and inverting an isotherm, in one self-contained
script:

```python
import math
import numpy as np
from scipy import optimize

# --- curve_fit with an honest error bar
def decay(t, a, tau, c):
    return a * np.exp(-t / tau) + c

t = np.linspace(0.0, 12000.0, 25)
y = 95.0 * np.exp(-t / 3000.0) + 4.0            # replace with your data
sigma = 1.5                                     # from the instrument
popt, pcov = optimize.curve_fit(decay, t, y, p0=(50.0, 1000.0, 0.0),
                                sigma=sigma, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
print("A = %.2f +/- %.2f K" % (popt[0], perr[0]))
print("tau = %.1f +/- %.1f yr" % (popt[1], perr[1]))

resid = y - decay(t, *popt)
chi2 = np.sum((resid / sigma) ** 2)
print("reduced chi2 = %.4f" % (chi2 / (t.size - popt.size)))

# --- inverting an isotherm, with the bracket written down explicitly
def birch_murnaghan(v, k0, k0p):
    return 1.5 * k0 * (v ** (-7/3) - v ** (-5/3)) * (
        1.0 + 0.75 * (k0p - 4.0) * (v ** (2/3) - 1.0))

v = optimize.brentq(lambda vv: birch_murnaghan(vv, 260.0, 4.0) - 135.0,
                    0.5, 1.5, xtol=1e-14)
print("V/V0 at 135 GPa = %.12f" % v)
```

The two calls worth noticing are `absolute_sigma=True` and the explicit
bracket `0.5, 1.5`. Neither is decoration: the first changes what the error
bars mean, and the second is what makes the root a guarantee rather than a
habit.

## Physical interpretation

The exponential of equation (1) is not a toy. It is the cooling law for a
small body with a linear heat loss (Newtonian cooling), the temperature
relaxation towards a new equilibrium after a step change in boundary
condition, and the response of a thermal system to a perturbation, with
$\tau = \rho c_p V/(hA)$ its time constant. A 1σ of 92 yr on a 3051 yr time
constant is a 3% measurement of the thermal response time of the body, which
is what the experiment was for.

The Birch–Murnaghan inversion has a direct geophysical reading: $V/V_0 =
0.7481$ at 135 GPa means the material is compressed by 25% at that pressure.
The value of $K_0'$ controls how the incompressibility stiffens with
compression, and $K_0$ is the seismic velocity in disguise, since
$V_P \propto \sqrt{K/\rho}$. A 135 GPa inversion is roughly the pressure at
the top of the lower mantle, which is why this particular inversion appears in
mantle mineral physics.

The correlation structure of §1.2 has a physical name too. A decay measured
over one time constant cannot separate amplitude from rate because they enter
the observable only through the product in the initial slope. A decay measured
over four can, because the tail is exponential in $\tau$ alone. **Design the
experiment so that the abscissa spans several characteristic scales, or the
fit will tell you — correctly — that it cannot separate your parameters.**

## Assumptions and limits

- **The 1σ errors from `pcov` assume the model is linear in its parameters
  near the solution, that residuals are Gaussian with constant σ, and that the
  data are independent.** Any of these failing makes the quoted error bar
  wrong, usually too small.
- **`curve_fit` is a local method.** A poor `p0` gives a worse local minimum
  or a non-convergence; the returned `pcov` may then be meaningless or
  infinite.
- **Exponential fits on noisy data are notoriously ill-conditioned** when the
  window is short (§1.2) and when a second exponential is added. Two-term
  exponential fits almost always have strongly correlated amplitudes and
  rates, even when the sum is well determined.
- **An open root finder assumes a root exists nearby and that the derivative
  does not vanish there.** Both can fail silently; `fsolve` reports
  `ier=2`/`converged=False` in some cases and a wrong root in others.
- **`least_squares` with `method='lm'` cannot take bounds.** Use `trf` or
  `dogbox` when parameters are physically constrained.
- **`minimize`'s derivative-free methods are not global methods.** Nelder-Mead
  and Powell are local; for a genuinely multimodal misfit you need
  `scipy.optimize.differential_evolution`, `shgo`, `dual_annealing` or a
  multi-start loop.

## Python demonstration

[`code/optimize_demo.py`](./code/optimize_demo.py) prints everything quoted
above. The experiments worth doing:

- Change the synthetic truth's $\tau$ from 3000 to 6000 yr while keeping the
  window at 12 000 yr. The correlation between $A$ and $\tau$ rises and
  $\sigma_\tau$ grows: the same data length, a worse-determined parameter,
  because the window now spans only two time constants.
- Delete the `jac` function in §3 and re-run. The evaluation counts change;
  the parameters do not.
- Replace `p0` with `(1.0, 1.0, 1000.0)` in the two-term fit. This is a
  realistic bad start: the optimiser lands in a different local minimum and
  the residual RMS is larger. Adding `bounds` restores the good answer, which
  is the standard fix.
- Change the cubic root-finding block to scan `f` from $-1$ to 5 on a grid and
  count sign changes. The count is the number of roots, and it is the step
  that `fsolve` does for you only if you ask.

## Common mistakes

- **Quoting a fitted parameter without its error bar.** A decay time of
  "3051 yr" and "3051 ± 92 yr" are different claims.
- **Using `absolute_sigma=False` with a known σ** and then quoting the
  inflated error bars as if they were the measurement's. (§1.1)
- **Reading a correlation coefficient of 0.99 as a good fit.** It means the
  two parameters are indistinguishable, not that the fit is excellent.
- **Starting an open root finder from a guess and reporting the root found.**
  Bracket instead, or count sign changes first. (§2.1)
- **Assuming `res.success == True` means the answer is the global optimum.**
  It means the stopping test was satisfied.
- **Comparing optimisers by wall-clock time.** Timings are machine-dependent;
  `nfev` counts are not, and they carry the same information. (§3)
- **Fitting a two-term exponential without checking the correlation matrix.**
  The amplitudes and decay rates of real two-term fits are often correlated at
  the 0.99 level, and the parameters are then not separately meaningful.

## Real-world applications

- **Thermal history and cooling.** Magma body cooling, borehole temperature
  relaxation, and the thermal response of a permafrost column are all fits of
  equation (1) to a measured temperature series.
- **Mineral physics.** The Birch–Murnaghan, Vinet and Mie–Grüneisen equations
  of state are inverted thousands of times per experiment; the bracket in §2
  is the standard protection against landing on the wrong branch.
- **Gravity and magnetic inversion.** Every inverse problem is a
  `least_squares` call in disguise, and the Jacobian is the sensitivity matrix
  that the resolution analysis is built from
  ([18-inverse-problems](../../18-inverse-problems/README.md)).
- **Seismic source parameters.** Aftershock decay (Omori's law), magnitude
  distributions and moment-rate functions are all fitted with `curve_fit`
  under constraints.
- **Instrument calibration.** Geodetic and gravimetric instruments are
  calibrated by fitting a known response; the reported 1σ is a calibration
  uncertainty that propagates into every subsequent measurement.
- **Hydrology and reservoir engineering.** Aquifer test analysis fits the
  Theis or Cooper–Jacob response to drawdown data, with the same degeneracy
  between transmissivity and storage coefficient that §1.2 demonstrates.

## Further reading

- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes: The Art of Scientific Computing* (3rd ed., Cambridge
  University Press, 2007).** Chapter 9 covers root finding and Chapter 15
  covers modelling of data, including the covariance matrix and the meaning
  of $\chi^2_\nu$. Level: intermediate to advanced.
- **Bevington, P. R., & Robinson, D. K. *Data Reduction and Error Analysis for
  the Physical Sciences* (3rd ed., McGraw-Hill, 2003).** The clearest account
  of what a fitted parameter's uncertainty means, and of how it differs from
  the scatter of the data. Level: intermediate.
- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed., Springer,
  2006).** The theory of the methods `minimize` exposes: line searches,
  trust regions, quasi-Newton updates. Level: advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (4th ed.,
  Academic Press, 2018).** The same least-squares algebra written for
  geophysicists, with the model resolution and covariance matrices that
  generalise the correlation matrix of §1.2. Level: graduate.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation* (SIAM, 2005).** What to do when the local linearisation behind
  `pcov` is not good enough. Level: doctoral.
- **Gubbins, D. *Time Series Analysis and Inverse Theory for Geophysicists*
  (Cambridge University Press, 2004).** Fitting, inversion and their failure
  modes in one geophysical frame. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text;
> confirm editions and availability through your library before citing them
> yourself.

## Related lessons

- [01 SciPy Organisation and When to Use Which Subpackage](./01-scipy-overview.md)
  — the subpackage map.
- [02 scipy.integrate](./02-integrate.md) — the forward problem that a fit is
  trying to invert.
- [07 scipy.ndimage and scipy.linalg](./07-ndimage-linalg.md) §5 — the same
  least-squares problem solved by Cholesky and by QR, and what the difference
  costs in digits.
- [08 scipy.special and scipy.stats](./08-special-stats.md) §2 — a fit whose
  goodness of fit has to be tested, not just reported.
- [01-14-04 Least Squares](../../01-mathematics/14-optimization/04-least-squares.md)
  — the normal equations behind `pcov`.
- [01-12-01 Root Finding](../../01-mathematics/12-numerical-methods/01-root-finding.md)
  — bisection, Newton and Brent derived rather than called.
- [18-inverse-problems/04 Nonlinear Inversion](../../18-inverse-problems/04-nonlinear-inversion/01-local-linearization.md)
  — where `least_squares` becomes a full inverse problem.
- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the cooling physics behind equation (1).

Exercises:
[`exercises/03-optimize-exercises.md`](./exercises/03-optimize-exercises.md)
and
[`exercises/03-optimize-solutions.md`](./exercises/03-optimize-solutions.md).

## Self-assessment checklist

- [ ] I can fit a decay and quote each parameter with its 1σ. (§1)
- [ ] I can compute and interpret the reduced $\chi^2$. (§1)
- [ ] I can explain what `absolute_sigma=True` does to the error bars and when
      it is the honest choice. (§1.1)
- [ ] I can read a correlation matrix and say whether a parameter pair is
      degenerate. (§1.2)
- [ ] I can demonstrate that a degeneracy is a property of the window, not of
      the data. (§1.2)
- [ ] I can bracket a root and say what the bracket guarantees. (§2)
- [ ] I can construct an equation with three roots and show that a solver
      returns only one. (§2.1)
- [ ] I can state the evaluation cost of a forward difference in terms of the
      number of parameters. (§3)
- [ ] I can choose between `least_squares` and `minimize` from the structure
      of the objective. (§3.1)
- [ ] I can say what `res.success` does not certify. (§3.1)
