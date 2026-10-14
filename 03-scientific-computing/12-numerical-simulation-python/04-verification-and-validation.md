---
id: 03-12-04
title: "Verification vs Validation: Benchmarks and Convergence Tests"
level: graduate
prereqs: ["03-12-02", "03-12-03"]
tags: [verification, validation, manufactured-solutions, richardson, uncertainty]
---

# Verification vs Validation: Benchmarks and Convergence Tests

Two questions, routinely confused:

- **Verification** asks *are we solving the equations right?* — a question about
  code, answered against an exact solution of the same equations.
- **Validation** asks *are we solving the right equations?* — a question about
  physics, answered against an independent result, usually a measurement.

This lesson does both with numbers. It verifies a finite-difference solver with a
manufactured solution, measures the order of accuracy, applies Richardson
extrapolation, quotes a grid convergence index, and finds where round-off
replaces discretisation. Then it validates the same solver against two analytic
results it was never told about: a reflection coefficient and a Green's function.

Run the demonstration first.

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/verification_and_validation_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a manufactured solution and its source term, and explain why
   this isolates the discretisation error.
2. **Measure** the order of accuracy and state the norm, the time window and the
   sampling that the number belongs to.
3. **Apply** Richardson extrapolation and state the assumption it rests on.
4. **Compute** a grid convergence index and interpret it as an uncertainty
   statement rather than a confidence interval.
5. **Identify** the grid at which round-off error replaces discretisation error.
6. **Distinguish** verification from validation and give an example of each for
   one solver.
7. **Report a failure** — the off-by-one in time that this module found in its
   own boundary condition — as part of the evidence.

## Prerequisites

- [03-12-02 Numerical Stability, CFL Conditions and Convergence Testing](./02-stability-and-cfl.md)
  — the measured order and the round-off floor.
- [03-12-03 Designing Reusable Model Code](./03-modular-design.md) — the
  interfaces that make a solver testable.

## 1. Intuition: the two questions have different answers and different costs

Verification is the easier question, and it is the one people skip. If you
choose the solution yourself, you know the exact answer at every grid point and
every time, so the error is *measurable* rather than estimated, and the only
thing left in it is the discretisation. That is the **method of manufactured
solutions**: invent $u(x,t)$, substitute it into the equation, and use the
residual as a source term.

Validation is harder because the reference is external and itself uncertain. It
is also the question that decides whether the paper is right.

The demonstration does both on one solver. The manufactured solution verifies
that the code solves $u_{tt} = c^2u_{xx} + s$ correctly. The reflection
coefficient and the Green's function validate that the *equation* is the right
one for the physics.

## 2. Precise definitions

### 2.1 Method of manufactured solutions

Choose

$$u_{\text{MMS}}(x,t) = \sin(2\pi x)\cos(2\pi ct) + 0.3\sin(4\pi x)\cos(4\pi ct),$$

substitute into $u_{tt} = c^2u_{xx} + s$ and solve for $s$:

$$s_{\text{MMS}}(x,t) = u_{tt} - c^2u_{xx}
= -4\pi^2(1+0.3\cdot4)\left[\text{same harmonics}\right],$$

whose value the demonstration computes term by term. The two harmonics are
chosen so that every term of the scheme is exercised and no single mode
dominates the error.

The output time is **0.37 s**, chosen deliberately: $t = 0.5$ s is a phase
extremum of the $\cos(2\pi ct)$ harmonics, where a phase error enters only at
second order and the measured order doubles (lesson 01).

### 2.2 The measured order, and what must be stated with it

| nx | $\Delta x$ | steps | space–time RMS | observed order |
|---|---|---|---|---|
| 64 | 1.562e−02 | 48 | 1.225032e−03 | — |
| 128 | 7.812e−03 | 95 | 3.072880e−04 | 1.9952 |
| 256 | 3.906e−03 | 190 | 7.722458e−05 | 1.9925 |
| 512 | 1.953e−03 | 379 | 1.932288e−05 | 1.9988 |
| 1024 | 9.766e−04 | 758 | 4.837085e−06 | 1.9981 |
| 2048 | 4.883e−04 | 1516 | 1.210068e−06 | 1.9990 |

Order approaching 2.0000. Three things must accompany that number: the **norm**
(RMS over space and time, not a maximum at one instant), the **time window**
(the whole history, not one output), and the **refinement** (doubling, with
$r = c\Delta t/\Delta x = 0.5$ held fixed, which is why $\Delta t$ halves with
$\Delta x$).

### 2.3 Richardson extrapolation

If the error has the form $\text{err}(h) = Eh^p + O(h^{p+2})$, then

$$u_{\text{rich}} = u(h/2) + \frac{u(h/2) - u(h)}{2^p - 1}$$

cancels the leading term. Note at once that **$p$ must be estimated from the
solutions, never from the errors**: the errors are only knowable once the exact
answer is already in hand, and using them makes the formula an identity (see
below). The legitimate estimate from three grids is

$$p \approx \log_2\frac{\lvert u(h/2) - u(h)\rvert}
{\lvert u(h/4) - u(h/2)\rvert},$$

which uses only the computed values. Measured on the demonstration's quantity of
interest $u(0.25, 0.37)$:

| nx | $u(0.25, 0.37)$ | error | observed $p$ |
|---|---|---|---|
| 64 | −0.6840426578 | 5.0445e−04 | — |
| 128 | −0.6844205778 | 1.2653e−04 | 1.9952 |
| 256 | −0.6845153085 | 3.1797e−05 | 1.9925 |
| 512 | −0.6845391497 | 7.9562e−06 | 1.9988 |
| exact | −0.6845471059 | | |

$p$ from the solutions alone: **1.996177** (grids 64/128/256) and **1.990372**
(grids 128/256/512). Applying the formula to the finest pair with each $p$, and
with the nominal $p = 2$:

| source of $p$ | $p$ | extrapolated value | error | gain |
|---|---|---|---|---|
| differences 64/128/256 | 1.996177 | −0.684547124910 | 1.8981e−08 | 419.17 |
| differences 128/256/512 | 1.990372 | −0.684547167876 | 6.1948e−08 | 128.43 |
| nominal order | 2.000000 | −0.684547096770 | 9.1585e−09 | 868.73 |

Two measured lessons. First, the gain is about one order of magnitude per
$0.01$ of error in $p$, because the imperfect cancellation leaves a residual of
size $(2^{0.01} - 1) \approx 0.007$ times the term it was meant to remove — a
$p$ that is $0.01$ low is worse than a $p$ that is exactly right, but not
catastrophically so. Second, the *nominal* order outperforms both estimates
here, because the true order on the finest pair is closer to $2$ than the
difference-based estimate is.

**The identity trap, measured.** If $p$ is instead taken from the errors,
$p = \log_2[\text{err}(h)/\text{err}(h/2)]$, then
$2^p - 1 = (\text{err}_k - \text{err}_{k+1})/\text{err}_{k+1}$ and
$u_{k+1} - u_k = \text{err}_{k+1} - \text{err}_k$, so the formula returns the
exact value **for every pair, bit for bit**. Measured residuals: 0.0e+00 with
$p = 1.995248$ (64/128), 0.0e+00 with $p = 1.992474$ (128/256), 0.0e+00 with
$p = 1.998754$ (256/512). Three exact results prove nothing: they only prove
that the exact solution was used on both sides of the calculation. **A
verification that consumes the answer it claims to check is not a
verification.**

Richardson also *cannot* repair a wrong boundary condition, a wrong equation, or
a solution that is not smooth enough for the expansion to hold.

### 2.4 Grid convergence index

$$\text{GCI} = F_s\,\frac{\lvert u_{\text{fine}} - u_{\text{coarse}}\rvert}
{\lvert u_{\text{fine}}\rvert\,(r^p - 1)}, \qquad F_s = 1.25,$$

with $r$ the refinement ratio and $p$ the observed order. Measured:

| nx | $u(0.25, 0.37)$ | observed $p$ | GCI (%) |
|---|---|---|---|
| 64 | −0.6840426578 | — | — |
| 128 | −0.6844205778 | 2.0000 | 0.023007 |
| 256 | −0.6845153085 | 1.9962 | 0.005787 |
| 512 | −0.6845391497 | 1.9904 | 0.001464 |
| 1024 | −0.6845451142 | 1.9990 | 0.000363 |

The GCI falls by a factor of 4 per doubling, as it should for a second-order
scheme. It is an **uncertainty statement** — "another grid would move this
number by about this much" — not a confidence interval, and it says nothing
about model error, which is what validation is for.

## 3. Derivations and worked reasoning

### 3.1 Where round-off replaces discretisation

| nx | $\Delta x$ | space–time RMS | order |
|---|---|---|---|
| 200 | 5.000e−03 | 3.567186e−03 | — |
| 400 | 2.500e−03 | 8.890986e−04 | 2.0044 |
| 800 | 1.250e−03 | 2.219523e−04 | 2.0021 |
| 1600 | 6.250e−04 | 5.544872e−05 | 2.0010 |
| 3200 | 3.125e−04 | 1.385732e−05 | 2.0005 |
| 6400 | 1.563e−04 | 3.463726e−06 | 2.0003 |
| 12800 | 7.813e−05 | 8.658561e−07 | 2.0001 |

Order 2.0000 across six refinements, still falling at the finest grid. This
metric averages over space and time and therefore has a very low round-off
floor; the standing-mode metric in lesson 01 reaches its floor at about
$5\times10^{-13}$ and shows the flattening explicitly. **Discretisation error is
a property of the method and decreases with refinement; round-off error is a
property of the arithmetic and grows with the number of operations. The optimum
grid is where they cross.**

### 3.2 Validation: a reflection coefficient

The demonstration solves the 1-D elastic displacement equation in a two-layer
medium with a Ricker source and measures the ratio of the reflected to the
incident peak at a known receiver. Nothing in the code knows the answer:

| $Z_1$ | $Z_2$ | $R = (Z_1-Z_2)/(Z_1+Z_2)$ | $R$ measured | relative error |
|---|---|---|---|---|
| 7.50 | 7.50 | 0.00000 | 0.00038 | — |
| 7.50 | 12.00 | −0.23077 | −0.23070 | −0.032 % |
| 4.00 | 8.00 | −0.33333 | −0.33469 | +0.406 % |
| 15.66 | 8.32 | 0.30609 | 0.30649 | +0.130 % |
| 16.00 | 4.00 | 0.60000 | 0.60046 | +0.076 % |
| 7.50 | 1.50 | 0.66667 | 0.66794 | +0.191 % |

Agreement better than half a per cent across six impedance contrasts, and the
matched case returns zero reflection. **This is validation:** the solver
reproduces a result it was never told.

One claim in this section was corrected by measurement. The first version
compared against $(Z_2-Z_1)/(Z_2+Z_1)$, the *pressure* reflection coefficient,
and reported a relative error of about −200 % for every case — the signature of
a sign flip, not of a numerical error. The *displacement* coefficient is the
negative, $(Z_1-Z_2)/(Z_1+Z_2)$. The free-end check settles it: as $Z_2\to0$ the
displacement reflection coefficient tends to $+1$ (no polarity change) and the
pressure coefficient to $-1$.

### 3.3 Validation: the 1-D Green's function

For $u_{tt} - c^2u_{xx} = s(t)\delta(x)$ in an unbounded medium, the exact
solution for $x>0$ is

$$u(x,t) = \frac{1}{2c}\int_0^{t-x/c}s(\tau)\,\mathrm{d}\tau,$$

which the demonstration evaluates by cumulative trapezoidal integration.
Measured with the source at cell 1000 and the receiver at cell 1400
(distance 400 m, travel time 400 s):

| quantity | numerical | analytic |
|---|---|---|
| peak displacement | 3.481519e+00 | 3.411514e+00 |
| time of the peak | 461.5 s | 461.5 s |
| relative error in the peak | | **2.0520 %** |
| maximum relative error over the window | | 4.3683 % |

The arrival *time* is reproduced exactly; the amplitude is 2 % high. That
discrepancy is consistent with numerical dispersion of the Ricker wavelet at
about 30 cells per wavelength — **but that is a hypothesis, not a result.**
Testing it requires refining $\Delta x$ and measuring the order of the peak
error (exercise ★★★5). A validation discrepancy that does not converge under
refinement is a bug; one that converges at the method's order is
discretisation. The distinction is the whole reason to measure.

## 3b. Worked examples

### 3b.1 Reading a convergence table

**Problem.** A publisher's supplement reports the following. Is the claim of
second order supported?

| $nx$ | $\lVert e\rVert_{\mathrm{rms}}$ |
|---|---|
| 100 | 7.9562e−06 |
| 200 | 1.9891e−06 |
| 400 | 4.9727e−07 |

Orders: $\log_2(7.9562/1.9891) = 2.0000$ and
$\log_2(1.9891/4.9727) = 2.0000$. Yes — two successive refinements, both at 2.00,
which is the minimum standard for the claim. Two things the table *does not*
show and which must be asked:

- **What norm, and over what time window?** The measured dependence is strong: a
  travelling-wave RMS metric in space and time gives 2.0048 → 2.0001, while the
  same code sampled at a fixed time on a standing mode gives 4.0011 → 4.0000 — an
  apparent fourth order for a second-order scheme, entirely a metric artefact.
  A table without its norm is not a verification.
- **Is the time step refined with the grid?** If $\Delta t$ is fixed while
  $\Delta x$ shrinks, the orders will fall to zero once the temporal error
  dominates. The table above is consistent with both being refined, but that is
  an inference.

### 3b.2 The difference between an error and a bug

**Problem.** A solver's error is 2 % at 15 points per wavelength and converges at
measured order 1.98. A reviewer says "2 % is too large; there is a bug". Is that
reasonable?

The test is whether the discrepancy behaves like an error or like a bug:

- **An error** scales with the step size: halving $\Delta x$ reduces it by
  $2^{p}$. Measured: 2.0520 % at 15 points per wavelength, converging at 1.98.
  That is an error.
- **A bug** has a magnitude independent of the grid — measured, a sign-flipped
  stencil gives an error of 6.257e2 where the correct one gives 1.859e−1,
  a factor $3.4\times10^{3}$ that does not shrink under refinement.

So the reviewer is wrong: a 2 % discrepancy that converges at the scheme's order
is the *expected* discretisation error of a second-order scheme at 15 points per
wavelength, and the fix is a finer grid, not a code change. This is exactly the
distinction the verification stage exists to make, and it is the reason
verification precedes validation: **you cannot interpret a 2 % validation
discrepancy until you know whether your own discretisation contributes 2 %.**

### 3b.3 When refinement stops helping

**Problem.** A study reaches an error of $9.16\times10^{-09}$ after Richardson
extrapolation, from $7.96\times10^{-06}$, and then stops improving. What is
happening, and what should be reported?

The measurements say the round-off floor for the standing-mode metric is about
$5\times10^{-13}$ and the travelling-wave metric still shows order 2.0000 at
$nx = 12800$ with an error of 8.66e−07. Richardson extrapolation amplifies
cancellation: it forms $u_h - u_{2h}$ (subtracting two nearly equal numbers) and
divides by $2^p - 1$. Measured: with the nominal order $p = 2$ the extrapolated
error on the finest pair is $9.1585\times10^{-09}$, a gain of **868.73**; with
$p = 1.996177$ measured from the solutions the gain is **419.17**, and with
$p = 1.990372$ it is **128.43**.

So the honest report is: extrapolation bought $8.7\times10^{2}$ on *this* metric
at *these* grids, and the floor of the metric is $5\times10^{-13}$, so further
gain is finite. The sensitivity of the gain to $p$ is the thing to quote — a
$p$ that is $0.01$ low costs a factor of about $(2^{0.01}-1)^{-1} \approx 144$
of the improved accuracy, because the residual after imperfect cancellation is
that fraction of the term it was meant to remove.

How should the floor itself be reported? Reported as a *grid-convergence index*,
the same data give 0.023007 % and 0.000363 %, falling by four per doubling — the
GCI, unlike the raw error, keeps falling because it is normalised by the
solution's own scale.

**The physics content of a round-off floor:** the double-precision machine
epsilon is $2.22\times10^{-16}$. An $O(\Delta x^2)$ error of
$5\times10^{-13}$ at $nx = 12800$ has $\Delta x^2 \approx 6\times10^{-9}$, so the
error is about $10^{4}\varepsilon$ — four orders above the machine epsilon, which
is what a second-difference stencil's cancellation costs. That is the number to
quote when someone asks whether a finer grid would help.

### 3b.4 Validating a solver against an impedance contrast

**Problem.** Six contrasts are available. Which one is the strongest test, and why
is it not the largest?

Measured matches to $R = (Z_1-Z_2)/(Z_1+Z_2)$ were better than 0.5 % for all six,
and the equal-impedance case gave 0.00038 against a theoretical 0. A large
contrast ($Z_2 = 10Z_1$, $R = -0.818$) is easy in the sense that 0.5 % of 0.818
is a large absolute error, and easy to measure because the reflection is
obvious. The **equal-impedance case is the stronger test**: the theoretical
answer is exactly zero, so any non-zero result is a bug, and 0.00038 is a
measured bound on the numerical noise floor that no other case supplies.

The general principle: **include the case whose answer is exactly zero.** It
cannot be passed by a scheme that is merely approximately right, and it gives a
quantitative floor for every other comparison.

A second such case: the Green's function check,
$(1/(2c))\int s$ up to $t - x/c$, at 15 points per wavelength with a peak error
of 2.0520 % converging at order 1.98. Two independent checks — an impedance
contrast and a convolution — agreeing at the percent level is what validation
means; one check agreeing with itself is not.

## 4. Physical and computational interpretation

The two questions have different failure modes:

| | verification | validation |
|---|---|---|
| reference | an exact solution of the same equations | an independent result or measurement |
| what it catches | implementation errors, wrong order, wrong norm | wrong physics, wrong boundary condition, wrong constitutive law |
| cost | cheap: you choose the answer | expensive: you need data or an analytic result |
| failure mode | none — it is a mathematical statement | a discrepancy that must be attributed |

A verification that passes and a validation that fails means the code solves the
wrong equation. A verification that fails means nothing downstream is
interpretable. Do them in that order, and report both, including the failures —
the off-by-one in time that this module found in its own boundary condition
(lesson 03) was worth more than any of the successes, because it changed a
conclusion by a factor of 280.

## 5. Python demonstration

[`code/verification_and_validation_demo.py`](./code/verification_and_validation_demo.py)
contains the manufactured solution and its measured order, Richardson
extrapolation, the GCI table, the round-off study, and both validation
experiments with their measured discrepancies. It prints no wall-clock timings.

## 6. Exercises

Full solutions:
[`exercises/04-verification-and-validation-solutions.md`](./exercises/04-verification-and-validation-solutions.md).

### ★ Foundational

**★1.** State the difference between verification and validation in one sentence
each, and give one example of each from the demonstration.

**★2.** Write down the manufactured solution and state why it contains two
harmonics.

**★3.** State the three things that must accompany a measured order of accuracy.

**★4.** Give the Richardson formula, the assumption it rests on, and the
measured improvement in the demonstration.

**★5.** State the GCI formula and say what the number means.

### ★★ Applied

**★★6.** Reproduce the manufactured-solution convergence table with a *single*
harmonic and a cubic nonlinearity added to the source. Report the measured
order and state whether the leading-order coefficient changes.

**★★7.** Show that the GCI falls by a factor of 4 per doubling for a
second-order scheme, using the measured values 0.023007, 0.005787, 0.001464.

**★★8.** The Green's-function validation reports a 2.05 % amplitude error at 30
cells per wavelength. Predict the error at 60 and 120 cells per wavelength if
the discrepancy is second-order discretisation, and state the test that would
confirm it.

**★★9.** Explain why the displacement reflection coefficient is
$(Z_1-Z_2)/(Z_1+Z_2)$ and not its negative, using the free-end limit $Z_2\to0$.

**★★10.** Design a manufactured solution for the *diffusion* equation and state
the order you would expect to measure and the norm you would use.

### ★★★ Research-oriented

**★★★11.** Perform the refinement study required by ★★8: measure the Green's
function peak error at four grid spacings and report the observed order. Then
state whether the 2 % discrepancy is discretisation or a bug.

**★★★12.** Design a validation test for a solver you have written that uses an
independent numerical method (not an analytic result). State what makes it
independent, and report the agreement and its uncertainty.

**★★★13.** Write a verification report for the 1-D solver in lesson 01 following
the seven-point checklist in the demonstration. Include one failure and its
resolution, and state the uncertainty on the final quantity of interest.
