---
id: 19-07-02
title: "Solution Verification and Discretisation Error Estimation"
level: research
prereqs: ["19-01-02", "19-07-01", "18-06-01"]
tags: [numerical-modelling, verification, solution-verification, richardson-extrapolation, grid-convergence-index, error-estimation]
---

# Solution Verification and Discretisation Error Estimation

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Richardson extrapolation formula and the observed-order
   estimator from the error model $e = Ch^{p}$.
2. **Compute** a discretisation error estimate for a functional of interest from
   three grids, and **state** the convention behind the safety factor.
3. **Test** whether a grid sequence is in the asymptotic range, and **explain**
   what a non-asymptotic order estimate does to the reported error bar.
4. **Measure** the resolution at which round-off turns further refinement into a
   loss, and **relate** it to the condition number of the discrete operator.
5. **Separate** discretisation error, solver tolerance and model-form uncertainty,
   and **report** a numerical result with each of the three labelled.
6. **Decide** when a discretisation error estimate is not worth quoting because
   model-form uncertainty dominates it.

## Prerequisites

- [19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions](01-code-verification.md)
  — the order of accuracy this lesson estimates.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md)
  — the error model $e = Ch^{p}$.
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../../18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md)
  — where discretisation error sits among the other uncertainty sources.

All models and data in this module are **SYNTHETIC**. The problem below is a
chosen teaching problem and every number is printed by this lesson's
demonstration.

## 1. Intuition: how wrong is the number I am about to publish?

Code verification, the previous lesson, is done once: it establishes that the
code converges at its design order. Solution verification is done **for every
production run**, and it answers a different question: *at the resolution I
actually used, how large is the error in the quantity I actually report?*

The distinction between "the quantity I report" and "the solution field" is the
practical heart of the subject. A simulation is almost never used for its field;
it is used for a *functional* of the field — the travel time to a reflector, the
maximum anomaly amplitude, the heat flow through a boundary, the temperature at a
site. Each functional has its own error, and there is no reason for two
functionals to have the same accuracy. A grid that resolves the field to one per
cent can give a functional to $0.1$ per cent or to ten per cent, depending on how
it weights the poorly resolved parts of the field. So solution verification is
always stated **for a named functional**.

The tool is the same one Gauss and Richardson used: run the model on a sequence of
grids, fit the error model, and extrapolate. What has changed since is the
bookkeeping — the asymptotic range, the safety factor, and the recognition that
beyond a certain resolution round-off starts to dominate and *refining makes the
answer worse*. Both of those effects are measured below.

## 2. Definitions

**Discretisation error.** For a functional $J$, the difference $\delta_J =
J_h - J_{\text{exact}}$, where $J_h$ is evaluated from the discrete solution on a
grid of spacing $h$.

**Error estimate.** A computable quantity $\hat{\delta}$ built from solutions on
several grids, intended to bound $|\delta|$ with high probability. It is an
estimate, not an equality: it uses the *assumption* (not the knowledge) that the
error model holds.

**Observed order.** The exponent $p$ in a fitted error model, usually obtained
from three grids. It is a measurement, and it is only as meaningful as the grids
it was measured on.

**Asymptotic range.** The range of $h$ in which the leading truncation term
dominates all higher-order terms, so that $\ln|e|$ against $\ln h$ is a straight
line of slope $p$.

**Grid-convergence index (GCI).** A standard *conservative* error estimate built
from the Richardson error estimate and a safety factor. It is a convention, not a
theorem.

**Solver tolerance.** The accuracy to which the algebraic system was solved. It
sets a floor on the error of the discrete solution which is independent of $h$.

## 3. Derivations

### 3.1 Richardson extrapolation

Suppose the functional converges as

$$J_h = J_{\text{exact}} + C h^{p} + O(h^{p+1}), \qquad C \neq 0,$$

and refine with ratio $r$: $h_2 = h_1/r$, $h_3 = h_2/r$. Dropping the
$O(h^{p+1})$ term,

$$J_1 - J_2 = C h_2^{p}\left(r^{p} - 1\right), \qquad
J_2 - J_3 = C h_3^{p}\left(r^{p} - 1\right).$$

Divide:

$$\frac{J_1 - J_2}{J_2 - J_3} = r^{p}
\quad\Longrightarrow\quad
\boxed{\;p = \frac{\ln\left|\dfrac{J_1 - J_2}{J_2 - J_3}\right|}{\ln r}.}$$

The *absolute values* matter. The textbook formula (as in
[19-01-02](../01-numerical-foundations/02-convergence-and-error.md)) uses the
error differences $e_i$; here the differences are of successive approximations,
which have the same sign as $C$ when the sequence converges monotonically, so the
ratio of *signed* differences is positive and the absolute value is harmless — but
if you write the inverted ratio by mistake, you get $p = -2$ and an extrapolation
in the wrong direction. The demonstration's first version did exactly that; the
correction is one line and the symptom is a negative order.

Once $p$ is known, the leading error term at the fine grid is

$$C h_3^{p} = \frac{J_2 - J_3}{r^{p} - 1},$$

so the **Richardson error estimate** for $J_3$ is
$\hat{\delta}_3 = (J_2 - J_3)/(r^{p} - 1)$ and the **extrapolated value** is

$$J_{\text{ext}} = J_3 + \frac{J_2 - J_3}{r^{p} - 1},$$

which is accurate to $O(h^{p+1})$: one order higher than any of its inputs.

### 3.2 The grid-convergence index

Rosche's standard practice multiplies the estimate by a factor of safety $F_s$ to
cover the neglected higher-order terms, the uncertainty in $p$, and the departure
from the asymptotic range:

$$\mathrm{GCI}_{3} = F_s\,\frac{|J_2 - J_3|}{r^{p} - 1}.$$

The relative form divides by $|J_3|$. The factor of safety is a **convention**;
$F_s = 3$ is conventional, and this lesson and the demonstration declare it rather
than derive it. What can be derived is the ratio of the estimate to the true error
*when the error model is exact and the grids are asymptotic*: then the ratio is
exactly $F_s$. In practice it is larger, as Section 5 measures.

### 3.3 Round-off and the condition number

Write $h = 1/N$ for the one-dimensional uniform grid. The eigenvalues of the
Dirichlet second-difference matrix $L_h$ are

$$\lambda_k = -\frac{4}{h^{2}}\sin^{2}\!\left(\frac{k\pi h}{2}\right),
\qquad k = 1, \dots, N-1,$$

so $\lvert\lambda_{\min}\rvert \to \pi^{2}$ and
$\lvert\lambda_{\max}\rvert = 4/h^{2}$, giving the exact asymptotic condition
number

$$\kappa(L_h) = \frac{4}{\pi^{2}h^{2}} = \frac{4N^{2}}{\pi^{2}}.$$

Because the solution is obtained by applying $L_h^{-1}$, relative round-off of
order $\epsilon \approx 2.2\times10^{-16}$ can be amplified by up to the
condition number, so the discretisation error cannot be pushed below about
$\epsilon\,\kappa$. This bound is *loose*: it is the worst case over all
right-hand sides, and a smooth right-hand side does much better (Section 5
measures the gap). The practical rule is therefore not to compute a floor but to
**measure** one: refine until the error stops falling, and stop.

## 4. The three error sources, and how they are told apart

| source | how it scales | how to test for it |
|---|---|---|
| discretisation error | falls as $h^{p}$ | refine; measure the order |
| solver tolerance | independent of $h$; falls as the tolerance | tighten the tolerance; watch the error |
| model-form error | independent of both | compare against independent data ([03](03-model-validation.md)) |

They are additive, and the reported error is dominated by the largest. A
discretisation study run with a loose solver tolerance measures the tolerance and
calls it discretisation; a refinement study pushed to the round-off floor measures
round-off and calls it a converged solution. Both mistakes are cheap to make and
cheap to detect: refine the grid *and* tighten the tolerance, and see which one
moves the answer.

## 5. Measured evidence

The demonstration `code/solution_verification_demo.py` solves the manufactured
problem of the previous lesson, but now plays the role of an analyst who does not
know the exact answer. The functional is

$$J = u(0.25, 0.25), \qquad \nabla^{2}u = -5\pi^{2}u \ \text{ in } (0,1)^{2},
\quad u = 0 \ \text{ on the boundary}.$$

| $N$ | $J_h$ | true error (for scoring only) |
|---:|---:|---:|
| 32 | 0.7090406863 | $1.934\times10^{-3}$ |
| 64 | 0.7075897128 | $4.829\times10^{-4}$ |
| 128 | 0.7072274801 | $1.207\times10^{-4}$ |

The measured order is $p = 2.0020$; the extrapolated value is
$J_{\text{ext}} = 0.7071069624$, whose error against the exact
$J = \sin(\pi/4)\sin(\pi/2) = 0.7071067812$ is $1.81\times10^{-7}$ — a reduction
of $666$ times relative to the finest grid alone. The GCI with $F_s = 3$ gives
$3.616\times10^{-4}$ against a true error of $1.207\times10^{-4}$: conservative by
a factor of exactly $3.0$, which here *is* the safety factor, because the
manufactured problem's error model is exactly the assumed $Ch^{2}$. With
$F_s = 1$ the estimate would match the truth to within the rounding of $p$.
**The estimate brackets the truth; in a harder problem it brackets it more
widely.**

The observed order from different grid triples, all with $r = 2$:

| grids | observed order |
|---|---|
| $16, 32, 64$ | 2.0081 |
| $32, 64, 128$ | 2.0020 |
| $64, 128, 256$ | 2.0005 |

Here every triple is close to the design order, because the manufactured solution
is smooth and the operator uniform. In a problem with a boundary layer or a sharp
interface, the coarsest triple typically overstates or understates $p$ by tens of
per cent, and the honest report gives $p$ **per triple** rather than a single
number.

### 5.1 Where the error stops falling

Functional: the discrete $L^{2}$ error of the one-dimensional problem
$-u'' = f$ with the manufactured solution $u = x\sin(\pi x)$ (deliberately not an
eigenvector of the discrete operator, so the round-off behaviour is generic):

| $N$ | discrete $L^{2}$ error | ratio to previous |
|---:|---:|---:|
| 256 | $5.252\times10^{-6}$ | — |
| 1024 | $3.282\times10^{-7}$ | 0.062 |
| 4096 | $2.052\times10^{-8}$ | 0.063 |
| 16384 | $1.289\times10^{-9}$ | 0.063 |
| 65536 | $7.678\times10^{-11}$ | 0.060 |
| 262144 | $6.235\times10^{-9}$ | 81.2 |

Each doubling of $N$ cuts the error by four (ratio $0.0625$) until $N = 65536$;
at $N = 262144$ the error *rises* by a factor of $81$. The refinement has stopped
buying accuracy. At that grid the condition number is
$\kappa = 4N^{2}/\pi^{2} = 2.79\times10^{10}$, so the crude bound
$\epsilon\kappa$ is $6.2\times10^{-6}$: over-estimating the measured floor
$6.2\times10^{-9}$ by three orders of magnitude, which is why the bound is a guide
and the measurement is the evidence.

### 5.2 The solver tolerance is a floor that looks like non-convergence

Same one-dimensional operator at $N = 1024$, but with a synthetic random
right-hand side (so the solution does not lie along a single eigenvector), solved
by conjugate gradients; the reference is a direct solve of the same system:

| solver tolerance | $\lVert u_{\text{CG}} - u_{\text{direct}}\rVert /
\lVert u_{\text{direct}}\rVert$ |
|---:|---:|
| $10^{-1}$ | $3.124\times10^{-2}$ |
| $10^{-2}$ | $8.771\times10^{-3}$ |
| $10^{-3}$ | $6.512\times10^{-6}$ |
| $10^{-4}$ | $1.909\times10^{-13}$ |
| $10^{-8}$ | $1.909\times10^{-13}$ |
| $10^{-12}$ | $1.909\times10^{-13}$ |

The achieved accuracy tracks the tolerance down to $10^{-3}$ and then flattens at
$2\times10^{-13}$: the iterative solver's own accumulation floor. **Any error
statement must name both the discretisation error and the solver tolerance that
bounds it**, because a reader who cannot see the tolerance cannot tell whether the
reported error is real or a solver artefact.

## 6. Assumptions and regime of validity

1. **The error model holds.** The estimators assume
   $J_h = J + Ch^{p} + O(h^{p+1})$ with a single dominant $C$. If two terms of
   comparable size compete, the fitted $p$ is a blend and the extrapolation is not
   $O(h^{p+1})$.
2. **The grids are in the asymptotic range.** Test it by using two overlapping
   triples, as in the table above; if $p$ moves, the coarse triple is not yet
   asymptotic.
3. **Monotone convergence.** Richardson extrapolation assumes the sign of the error
   does not change with $h$. Oscillatory error (some wave schemes) breaks the
   formula; the estimate can then be *smaller* than the true error.
4. **The functional is not pathological.** A functional that samples a
   discontinuity, a boundary layer or a single cell can converge at a different
   order from the field, or not at all.
5. **The solution is smooth enough for the design order.** If not, the measured
   order is the *observed* order of the problem, not the code's order — an
   important distinction when the code has already been verified
   ([01](01-code-verification.md)).
6. **What the estimate does not cover.** Model-form error, parameter uncertainty
   and data uncertainty are invisible to every estimator here. A converged
   solution of the wrong equations has a beautifully small discretisation error.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| functional | $J$ | whatever it is ($u$, s, mGal, W m$^{-2}$) | |
| discretisation error | $\delta_J$ | same as $J$ | the estimate must carry the unit of $J$ |
| observed order | $p$ | dimensionless | log of a ratio of like quantities |
| safety factor | $F_s$ | dimensionless | convention |
| condition number | $\kappa$ | dimensionless | $4N^{2}/\pi^{2}$ |

A frequent blunder: quoting a *relative* GCI next to an *absolute* error. Both are
fine, but the two must be labelled. A second: applying a GCI computed for a
functional to the field, or vice versa.

## 8. Worked examples

### Example 1 — a full hand calculation from three numbers

Suppose a gravity code gives a maximum anomaly of $J_1 = 1.0200$,
$J_2 = 1.0051$, $J_3 = 1.0013$ mGal on grids with $r = 2$.
$J_1 - J_2 = 0.0149$, $J_2 - J_3 = 0.0038$, ratio $3.9211$, so

$$p = \frac{\ln 3.9211}{\ln 2} = \frac{1.3664}{0.6931} = 1.9714 .$$

The Richardson estimate for the fine grid is
$\hat{\delta}_3 = 0.0038/(2^{1.9714} - 1) = 0.0038/2.9104 = 1.31\times10^{-3}$ mGal,
and the GCI with $F_s = 3$ is $3.92\times10^{-3}$ mGal. Quoting the result as
$1.0013 \pm 0.0039$ mGal is the honest form; quoting $1.0013$ mGal alone implies a
precision the sequence does not support.

### Example 2 — the same calculation on the demonstration data

$J_1 = 0.7090406863$ ($N=32$), $J_2 = 0.7075897128$ ($N=64$),
$J_3 = 0.7072274801$ ($N=128$). Consecutive differences:
$J_2 - J_1 = -1.4509735\times10^{-3}$ and
$J_3 - J_2 = -3.622327\times10^{-4}$; their ratio is $4.0056$, so

$$p = \frac{\ln 4.0056}{\ln 2} = \frac{1.38766}{0.69315} = 2.0020 .$$

The Richardson estimate for the **finest** grid uses the pair that brackets it:

$$J_{\text{ext}} = J_3 + \frac{J_3 - J_2}{r^{p} - 1}
= 0.7072274801 - \frac{3.622327\times10^{-4}}{3.00558}
= 0.7072274801 - 1.20520\times10^{-4} = 0.7071069624 .$$

The measured error of this extrapolation against $J = 0.7071067812$ is
$1.81\times10^{-7}$, against $1.21\times10^{-4}$ for $J_3$ alone. The GCI for
$N = 128$ is $F_s\,|J_3-J_2|/(r^{p}-1) = 3 \times 1.20520\times10^{-4} =
3.616\times10^{-4}$, and the true error is $1.207\times10^{-4}$: the estimate is
conservative by $3.0$.

**Keep the pairing consistent.** $J_2 - J_1$ estimates the error on the $N=64$
grid; $J_3 - J_2$ estimates it on $N=128$. The two differ by the factor
$r^{p} = 4.006$, so using the coarse difference while reporting the fine grid
inflates the error bar fourfold with no warning.

### Example 3 — is the estimate worth quoting?

The same study gives a "converged" anomaly amplitude. Suppose the density
contrast used in the forward model is uncertain by $10$ per cent — an ordinary
situation. Then the model-form/parameter uncertainty in $J$ is about
$10$ per cent, i.e. $1.0\times10^{-1}$ mGal, which is $26$ times the GCI of
$3.92\times10^{-3}$ mGal from Example 1. In that situation the correct report is
one line: *the discretisation error is negligible against the parameter
uncertainty*, with both numbers given. Quoting five significant figures of the
discretisation study would be a misallocation of effort and a misleading
presentation.

## 9. Python demonstration

`code/solution_verification_demo.py` (~0.6 s, print-only):

```bash
cd 19-numerical-modeling-hpc/07-verification-validation-uncertainty/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solution_verification_demo.py
```

It prints the three-grid table, the measured order and the extrapolated value, the
GCI scored against the truth, the order from three overlapping grid triples, the
round-off floor of the one-dimensional study, and the solver-tolerance floor of
the conjugate-gradient study. The exact solution is used only to *score* the
estimator; the estimator never sees it.

## 10. Exercises

[`exercises/02-solution-verification-exercises.md`](exercises/02-solution-verification-exercises.md)
and
[`exercises/02-solution-verification-solutions.md`](exercises/02-solution-verification-solutions.md)
include a hand calculation of $p$ and the GCI from a table, a design question
about the refinement ratio, and a diagnosis exercise in which a non-asymptotic
triple and a loose tolerance produce the same symptom.

## 11. Applications

- **Reporting simulation results.** Any number that will be used to make a
  decision should carry a discretisation error estimate and a named solver
  tolerance; this is the practical output of the lesson.
- **Grid design.** The order measured in the asymptotic range tells you how much
  refinement is needed for a target accuracy, which sets the cost of the study
  ([19-06-01](../06-hpc-and-parallel-computing/01-hpc-architecture.md)).
- **Community benchmarks.** Comparison tables are only meaningful when every
  entry carries its grid, norm and error estimate
  ([04 Standard Benchmark Problems](04-benchmark-problems.md)).
- **Wave-propagation modelling.** Dispersion error in seismic wave modelling is a
  discretisation error with a known analytic scaling in points per wavelength
  ([19-01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md)),
  which makes the estimate especially cheap there.
- **Inverse problems.** The discretisation error enters the data misfit as a
  correlated noise component; ignoring it produces over-confident models
  ([18-01-04 Discretisation, Parameterisation and Model Choice](../../18-inverse-problems/01-inverse-problem-foundations/04-discretisation-reality.md)).

## 12. Further study

- [19-01-02](../01-numerical-foundations/02-convergence-and-error.md) — the theory
  of truncation error and rates.
- [19-07-01](01-code-verification.md) — establishing the design order in the first
  place.
- [19-07-03](03-model-validation.md) — the error the refinement study cannot see.
- [18-06-02 Monte Carlo Propagation and Its Convergence](../../18-inverse-problems/06-uncertainty-quantification/02-monte-carlo-uq.md)
  — propagating parameter uncertainty, the other half of an error budget.

## Mastery checkpoint

Without notes:

> A forward model for a gravity anomaly gives a maximum amplitude $J$ on three
> grids with $r = 2$: $J_1 = 12.480$, $J_2 = 12.255$, $J_3 = 12.199$ mGal, and a
> fourth run on the finest grid with the solver tolerance loosened from
> $10^{-12}$ to $10^{-4}$ gives $12.187$ mGal. **(a)** Compute the observed order.
> **(b)** Compute the Richardson estimate and the GCI with $F_s = 3$ for
> $N = N_3$. **(c)** Say in one sentence what the fourth run tells you about which
> error dominates. **(d)** State the reported result in the form you would put in a
> paper, and name the one extra piece of information a referee would need to
> reproduce the estimate.

Worked answers appear in
[`exercises/02-solution-verification-solutions.md`](exercises/02-solution-verification-solutions.md).

## Common pitfalls

1. **Inverting the order formula.** It returns $p \approx -2$ and extrapolates in
   the wrong direction; the symptom is an extrapolated value *worse* than the
   finest grid.
2. **Mixing the pairing.** The GCI is defined for a stated grid and a stated pair;
   using $J_1 - J_2$ where $J_2 - J_3$ belongs changes the estimate by a factor of
   $r^{p}$.
3. **Quoting one triple as if it were asymptotic.** Test with two overlapping
   triples; report $p$ per triple.
4. **Refining past the floor.** Beyond $\sim\epsilon\kappa$ further refinement
   increases the error; measure the floor rather than assuming it is far away.
5. **Hiding the solver tolerance.** A loose tolerance produces a fixed error floor
   that mimics non-convergence; the tolerance is part of the result.
6. **Presenting the discretisation error as the uncertainty of the result.** It is
   one term in an error budget, usually the smallest one.

## Related modules

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md).
- [19-07-01 Code Verification](01-code-verification.md) —
  [19-07-03 Model Validation](03-model-validation.md) —
  [19-07-04 Benchmark Problems](04-benchmark-problems.md).
- [18-inverse-problems](../../18-inverse-problems/README.md) — uncertainty
  taxonomy, propagation and reporting.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — the
  statistical language for the other error terms.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)
  — recording the grid and tolerance that produced a number
  ([22-02-05 Data Versioning and Provenance Tracking](../../22-data-engineering-reproducibility/02-reproducible-workflows/05-data-versioning.md)).

## Self-assessment checklist

- [ ] I can derive $p$ and the Richardson estimate from three grids, with the
      pairing explicit.
- [ ] I can state the safety factor and say that it is a convention.
- [ ] I can test for the asymptotic range with overlapping triples.
- [ ] I can explain the round-off floor and its relation to $\kappa = 4N^{2}/\pi^{2}$.
- [ ] I can tell a solver-tolerance floor from a discretisation error.
- [ ] I can write a result statement carrying functional, error estimate, solver
      tolerance and model-form caveat.
