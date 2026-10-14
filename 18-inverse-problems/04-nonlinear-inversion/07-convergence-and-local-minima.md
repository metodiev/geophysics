---
id: 18-04-07
title: "Convergence Diagnosis and Local-Minimum Traps"
level: doctoral
prereqs: ["18-04-01", "18-04-02", "18-04-06"]
tags: [inverse-problems, regularization, optimization, nonlinear-inversion, convergence, local-minima, uncertainty]
---

# Convergence Diagnosis and Local-Minimum Traps

## Learning objectives

1. **Distinguish** a stationary point from a minimiser and **decide** which one a stopped optimisation has produced from the eigenvalues of the Hessian.
2. **Reproduce** the failure of loose stopping rules, including a rule that reports success at a point with a degenerate Hessian.
3. **Quantify** the parameter error that a gradient tolerance permits from $\lvert\Delta\rvert \approx \text{tol}/\lambda_{\min}$, and **compare** it with the width of the valley.
4. **Compute** the linearised covariance $H^{-1}$ at the minimum and **interpret** the condition number and the parameter correlation as statements about the misfit surface rather than about the algorithm.
5. **Measure** the near-equivalent set at several tolerances and **state** why an inverse problem's answer is a set, not a point.
6. **Assemble** a convergence report whose fields are defensible to a reviewer.
7. **State** the regime of validity of the second-order diagnosis and name the cases where it does not apply.

## Prerequisites

- [Local Linearisation, Jacobians and Iteration](01-local-linearization.md) — the misfit and the linearisation whose Hessian is examined here.
- [Gradient, Gauss-Newton and Full Newton Methods](02-gradient-and-newton.md) — the methods whose stopping rules this lesson audits.
- [Multi-Start, Hybrid and Memetic Strategies](06-multi-start-and-hybrid.md) — the strategy that supplies the several candidate minima this lesson compares.

All models and data in this module are SYNTHETIC.

## 1. Stationary point, minimiser, and what a stopping rule certifies

A gradient-based optimiser stops when its own criterion is met. The classical criteria are a gradient measure, $\lVert\nabla f\rVert \le g_{\text{tol}}$, and a progress measure, $\lvert f_{k+1} - f_k\rvert \le f_{\text{tol}}\lvert f_k\rvert$. Neither tests the second-order condition

$$
\lambda_{\min}(H) > 0 , \qquad H = \nabla^2 f(u^{\ast}) ,
\tag{1.1}
$$

which is what distinguishes a minimiser from a saddle or a maximum. The declaration used in this lesson's demo is the two-parameter objective

$$
f(x,y) = 1 - \sum_{i} c_i \exp\!\left(-\frac{1}{2}\left[\left(\frac{x - c_{x,i}}{s_{x,i}}\right)^{2} + \left(\frac{y - c_{y,i}}{s_{y,i}}\right)^{2}\right]\right) - 0.02x + 0.01y ,
\tag{1.2}
$$

with two wells ($c = +1.00$ at $(-0.60,-0.45)$ with $\sigma = (0.55,0.90)$, and $c = +0.85$ at $(+0.75,+0.60)$ with $\sigma = (0.50,0.50)$) and one bump ($c = -0.30$ at $(+0.20,+0.10)$ with $\sigma = 0.60$), all lengths in km and $f$ a dimensionless misfit. The analytic gradient of (1.2) is checked in the demo against a central finite difference at 49 points:

```
  Analytic gradient checked against a central finite difference
  (h = 1e-6) at 49 points: worst discrepancy 1.509e-10,
```

which is the expected truncation level of the difference formula and confirms that the Hessian below is the true second derivative of the objective that was optimised.

## 2. Every stationary point found by a grid of starts

One L-BFGS-B run (analytic gradient, $g_{\text{tol}} = 10^{-10}$) from each of 625 grid starts, with duplicates removed, gives

```
   #   u (km)                 f          ||grad f||   eig(H)                       type
   0   (-0.6367, -0.5464)     0.07740  2.473e-12   (+1.1953, +3.4180)   minimum
   1   (+0.7886, +0.6442)     0.24967  1.241e-13   (+2.9228, +3.3487)   minimum

  Grid starts landing in each basin, in the order of the table: 234, 391
```

Two minima, of which the second has the larger basin (391 of 625 starts, 62.6%) and the worse objective (0.24967 against 0.07740, a factor 3.2). The best basin collects 37.4% of uniform starts. The lesson from these two numbers is the one [Global Search](04-global-search.md) made with volumes: the depth of a minimum and the size of its basin are unrelated, so a single start is not evidence of a global solution.

The declared landscape has no interior saddle — the wells are far enough apart that the ridge between them never becomes a stationary point inside the box — but the flat outer region does produce stationary points with a degenerate Hessian, and Section 3 uses one.

## 3. A worked stopping-rule audit

Three starts and three rules, with the tool's own termination message and the exact Hessian at whatever point it accepted:

```
   rule        start (km)        f reached   ||grad f||   eig(H)                    what eig(H) says   message
   gtol 1e-3   best basin       0.07740  1.344e-04   (+1.1952, +3.4181)   minimum           CONVERGENCE: NORM OF P
   gtol 1e-3   flat outer       0.91000  2.236e-02   (-0.0000, +0.0000)   flat/degenerate   CONVERGENCE: NORM OF P
   ftol 1e-3   best basin       1.04197  2.255e-02   (-0.0018, +0.0000)   saddle            CONVERGENCE: RELATIVE
   ftol 1e-3   flat outer       1.02960  2.237e-02   (-0.0001, +0.0000)   flat/degenerate   CONVERGENCE: RELATIVE
   gtol 1e-10  best basin       0.07740  2.473e-12   (+1.1953, +3.4180)   minimum           CONVERGENCE: NORM OF P
   gtol 1e-10  shallow basin    0.24967  1.241e-13   (+2.9228, +3.3487)   minimum           CONVERGENCE: NORM OF P
```

Every row reports convergence; the rows differ by a factor of 13 in the objective. The loose progress rule stopped the best-basin start at $f = 1.04197$ where the curvature is $1.5\times10^{-3}$ of the curvature at the true minimum, i.e. numerically flat; the same start under the tight gradient rule reached $f = 0.07740$ with $\lVert\nabla f\rVert = 2.5\times10^{-12}$. The message alone said nothing about which of these was an answer; $\lVert\nabla f\rVert$ and $\mathrm{eig}(H)$ did.

## 4. What a gradient tolerance costs in model space

Linearise about the minimum: a displacement $\delta$ along an eigenvector $v_i$ of $H$ changes the gradient by $\lambda_i\delta v_i$, so $\lVert\nabla f\rVert \le \text{tol}$ permits a displacement of about $\text{tol}/\lambda_i$ along that direction, with an objective change of $\tfrac12\lambda_i(\text{tol}/\lambda_i)^{2} = \text{tol}^{2}/(2\lambda_i)$. Measured at the global minimum, where $\lambda = (1.1953, 3.4180)$ and $\mathrm{cond}(H) = 2.860$:

```
   tol      |delta| steep dir (km)   |delta| flat dir (km)   misfit change on flat dir
   1e-02                    0.0029                   0.0084                    4.183e-05
   1e-03                    0.0003                   0.0008                    4.183e-07
   1e-06                    0.0000                   0.0000                    4.183e-13
```

At $\text{tol} = 10^{-3}$ the permitted displacement is $10^{-3}/1.1953$ km $= 0.84$ m along the flat direction and $10^{-3}/3.4180$ km $= 0.29$ m along the steep one. The ratio $1/\lambda_{\min}$ is exactly what converts a gradient tolerance into a model-space error, and it does the work that the condition number does in the linear theory of [Why Regularise?](../03-regularization/01-why-regularize.md): in a poorly conditioned problem $\lambda_{\min}$ is many orders of magnitude smaller and the same tolerance is ruinous.

## 5. The linearised covariance, correlation and what it measures

Taking the linearised Gaussian view, the parameter covariance is proportional to $H^{-1}$ at the minimum. Measured:

```
   H       = [[+3.3965, +0.2174], [+0.2174, +1.2167]]  misfit/km^2
   H^-1    = [[0.2978, -0.0532], [-0.0532, 0.8314]]  km^2/misfit
   marginal widths from H^-1 alone : (0.5457, 0.9118) km
   correlation coefficient         : -0.1069
   Eigenvector of the small eigenvalue (the flat direction): (+0.098, -0.995)
```

Two readings follow. First, the widths (0.55, 0.91) km are large compared with the grid spacing that found them, so the near-equivalent set of Section 6 is consistent with them: the surface supports a band of models much wider than the algorithm's step size. Second, the correlation is only $-0.107$, so in this landscape the two parameters are nearly independent and the marginals are a fair summary; had the correlation been near $\pm1$ the marginals would have overstated how well the pair is determined. Note carefully what has been measured: $H^{-1}$ describes the *misfit surface*. It knows nothing about the algorithm, the start, or the stopping rule, and quoting it as "the algorithm's uncertainty" is a category error.

## 6. The near-equivalent set, measured

Uniform sampling of the box with the objective evaluated in the same units:

```
   tol        accepted   % of box   spread from f_min (km)   extent x (km)   extent y (km)
   1e-04              5    0.0013                      0.011            0.007            0.017
   1e-03             39    0.0097                      0.039            0.047            0.069
   1e-02            345    0.0862                      0.129            0.152            0.254
   5e-02           1813    0.4532                      0.294            0.346            0.583
```

The accepted volume rises by a factor of 363 between $\text{tol} = 10^{-4}$ and $\text{tol} = 0.05$, and the extent of the accepted set grows with it. For a chi-square misfit with $N$ data points, tolerances are quoted as changes of $\chi^{2}$: 1 is about one standard error of the fit and 9 about three. Here $f$ is a bare dimensionless misfit, so the tolerance is a modelling choice and is declared, not derived. What the table establishes is that the answer to an inverse problem is a set whose size depends on a tolerance the analyst chose, and that no single model should be quoted without it.

## 7. A convergence report worth defending

Assembling the measured quantities, a defensible report for a converged inversion contains, at minimum:

- the objective value, the number of forward evaluations, and the termination message;
- $\lVert\nabla f\rVert$ at the accepted point **and** $\mathrm{eig}(H)$ or $\lambda_{\min}$;
- the stopping tolerances, and the model-space displacement they permit via $\text{tol}/\lambda_{\min}$;
- the condition number of $H$ and the parameter correlation, or the full covariance;
- the best objective found by a multi-start of declared size, to show that the basin is not obviously the wrong one;
- the near-equivalent set at one declared tolerance, as the honest width of the answer.

Two of these fields are cheap and one is not: $\lVert\nabla f\rVert$ and the termination message come free with the optimiser, $\mathrm{eig}(H)$ costs one Hessian (or a few matrix-vector products with a finite-difference Hessian–vector product), and the multi-start costs its budget. Omitting the Hessian field is the single most common way a converged inversion is misreported.

## 8. Assumptions and regime of validity

- **Second-order sufficiency at the accepted point.** (1.1) decides locally. If $\lambda_{\min}(H) \approx 0$ — as at the flat outer corner measured in Section 3 — the test is inconclusive and the point must be reported as flat rather than as a minimum.
- **The Hessian exists and is inexpensive enough to evaluate.** For a noisy objective, a finite-difference Hessian is dominated by noise; then a Gauss–Newton approximation $H \approx J^{\mathsf T}J$ from lesson 18-04-02 is the usable substitute, and it is positive semidefinite by construction, so it cannot detect a saddle — a limitation, not a convenience.
- **The Gaussian covariance model.** $H^{-1}$ is a small-displacement, linearised statement; the measured accepted set at $\text{tol} = 0.05$ spans 0.29 km and is not described by a single quadratic.
- **Tolerance is declared.** Every width in Section 6 changes by orders of magnitude with it; a report without the tolerance is not falsifiable.
- **The objective is the right objective.** All of this diagnoses the misfit surface for a declared data fit and a declared noise model. A minimum of the wrong misfit is a correct answer to the wrong question, and no Hessian test detects that.

## Mastery checkpoint

1. Verify the finite-difference check of the analytic gradient at a point of your choosing and state the expected order of the discrepancy.
2. From the measured $\lambda = (1.1953, 3.4180)$, compute the displacement permitted at $\text{tol} = 10^{-5}$ in metres, in both directions.
3. Explain why a Gauss–Newton Hessian $J^{\mathsf T}J$ cannot classify a saddle, and what it *can* still certify.
4. Recompute the condition number if both eigenvalues of the measured $H$ were ten times smaller, and say what changes in the tables of Sections 4 and 5 and what does not.
5. Given the measured accepted-set extents, decide which tolerance you would quote for a depth estimate quoted to 50 m, and justify it.
6. List the fields of Section 7 that a paper you know reports, and identify the missing ones as a reviewer would.

## Common pitfalls

- **Treating the termination message as evidence.** Every row of Section 3 reported convergence, including the flat points.
- **Reporting $H^{-1}$ as algorithm uncertainty.** It is a property of the misfit surface.
- **Using $\lambda_{\min}$ from a noisy finite-difference Hessian.** The sign can flip on noise alone.
- **Quoting a model without a tolerance.** Section 6 shows the accepted volume changing by a factor 363 within the same box.
- **Assuming the found basin is the global one.** Measured: 37.4% of starts reach the best basin, and the basin with 62.6% of starts was 3.2 times worse in objective.

## Related modules

- [Why Regularise?](../03-regularization/01-why-regularize.md) — the condition number and the resolution trade-off that Section 4 re-derives from the solver's side.
- [Multi-Start, Hybrid and Memetic Strategies](06-multi-start-and-hybrid.md) — the strategy that produces the several candidate minima compared here.
- [Choosing the Regularisation Parameter](../03-regularization/03-parameter-choice.md) — the same arbitrariness, in the choice of $\alpha$ rather than of a stopping rule.

## Materials

- Demo: `code/convergence_diagnostics_demo.py` (print-only, about 1 s, exit 0).
- Exercises: `exercises/07-convergence-and-local-minima-exercises.md` with solutions in `exercises/07-convergence-and-local-minima-solutions.md`.

All models and data in this module are SYNTHETIC.
