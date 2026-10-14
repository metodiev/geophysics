---
id: 01-01-05
title: "Absolute vs Relative Error, Conditioning and Stability"
level: intermediate
prereqs: ["01-01-04"]
estimated_minutes: 75
tags: [error-analysis, conditioning, stability, backward-error]
---

# Absolute vs Relative Error, Conditioning and Stability

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** absolute, relative, forward and backward error, and the
   residual, and say which of them answers which question.
2. **Define** the relative condition number of a problem and compute it for a
   differentiable function as $\kappa = |x f'(x)/f(x)|$.
3. **Separate** *conditioning* (a property of the problem) from *stability* (a
   property of the algorithm), and give an example of each failure mode.
4. **Bound** the error of a linear solve in terms of $\kappa(A)$ and the data
   perturbations, and interpret the result for ill-conditioned matrices such as
   the Hilbert matrix.
5. **Recognise** the geophysical situations where ill-conditioning is intrinsic
   — downward continuation, depth estimation, and inverse problems — and say
   why no algorithm removes it.

## Prerequisites

[01-01-04 Floating-Point Representation, Round-Off and Catastrophic
Cancellation](./04-floating-point.md) for the error model
$\mathrm{fl}(a\odot b) = (a\odot b)(1+\delta)$, $|\delta|\le u$, and for
cancellation. Some linear algebra is used in Sections 5.4 and 6; the notation is
introduced as it appears.

## 1. Intuition: accuracy is a ratio, not a small number

Two statements about the same computation:

> "The depth is wrong by 1 metre."
> "The depth is wrong by 0.1 per cent."

The first is an **absolute** error and is meaningless without the size of the
quantity. The second is a **relative** error and immediately tells you whether
to worry. An error of 1 m in a 10 km depth is excellent; the same error in a
10 m depth is catastrophic.

The second, deeper idea is that error is not only a property of the arithmetic.
Some problems *amplify* whatever error you feed them, no matter how carefully
you compute. The depth-to-anomaly relation in gravity is gently amplifying;
downward continuation of a potential field is violently so. The number that
measures this intrinsic amplification is the **condition number**, and it is the
central concept of this lesson.

| Question | Tool |
|---|---|
| How far is my answer from the truth? | absolute and relative **forward** error |
| How far is my problem from a nearby solvable one? | **backward** error |
| How well have I satisfied the equations? | the **residual** |
| How much error *must* I have? | the **condition number** |
| How much error does my *method* add? | **stability** |

## 2. Precise definitions

Let $x$ be the true value, $\hat{x}$ a computed or measured approximation, and
$A x = b$ a problem whose solution $\hat{x}$ we have computed.

**Absolute error.** $\;|x - \hat{x}|$.

**Relative error.**

$$\mathrm{relerr}(\hat{x}) = \frac{|x-\hat{x}|}{|x|} \qquad (x \ne 0).$$

Relative error is what propagates through multiplication, division and
attenuation laws. Absolute error is what propagates through addition and
subtraction. Using the wrong one is the most common error-analysis mistake.

**Forward error.** The error in the answer, measured whichever way (relative is
usually the informative one): $\|\hat{x} - x\|/\|x\|$.

**Backward error.** The smallest perturbation $\Delta A$, $\Delta b$ such that
the computed $\hat{x}$ is the **exact** solution of the perturbed problem
$(A + \Delta A)\hat{x} = b + \Delta b$. Backward error measures how good the
*algorithm* is; it does not, by itself, say how good the *answer* is.

**Residual.** $\;r = b - A\hat{x}$. Note carefully: a small residual does **not**
imply a small forward error. For an ill-conditioned $A$ the residual can be
$10^{-16}$ while the answer is wrong in the third digit. That gap is exactly the
condition number.

**Measurement uncertainty.** A different quantity from all of the above. An
observed value 12.3 mGal with a 0.1 mGal instrument has a relative *uncertainty*
of about $8\times10^{-3}$, which dwarfs any floating-point error. Keep
uncertainty and numerical error in separate columns of your error budget.

## 3. Conditioning: a property of the problem

The **relative condition number** of a problem is the largest ratio of output
relative change to input relative change:

$$\kappa = \sup_{\Delta x \ne 0}
\frac{\big|\Delta f\big| \big/ |f(x)|}{\big|\Delta x\big| \big/ |x|}.$$

Its meaning is a sentence you can use in a paper: *if the input is known to $r$
relative accuracy, the answer is known to about $r\kappa$ relative accuracy at
best.* Conditioning is **not** a property of the algorithm, the programming
language, or the computer. It is a property of the question being asked.

A useful scale:

| $\kappa$ | interpretation |
|---|---|
| $\approx 1$ | benign; each digit of input buys a digit of output |
| $10^{3}$ | lose about 3 digits |
| $10^{10}$ | lose about 10 digits; double precision buys you 6 |
| $> 10^{16}$ | nothing survives in binary64; the problem must be reformulated or regularised |

## 4. Stability: a property of the algorithm

An algorithm is **numerically stable** if the error it produces is of the same
order as the error the conditioning forces — i.e. it does not amplify input
perturbations more than the problem does.

An algorithm is **backward stable** if the computed answer is the exact answer
to a nearby problem: formally, if there exist $\Delta A$, $\Delta b$ with
$\|\Delta A\| \le u\,c\,\|A\|$ and $\|\Delta b\| \le u\,c\,\|b\|$ for a modest
constant $c$, such that $\hat{x}$ solves $(A+\Delta A)\hat{x} = b + \Delta b$
exactly.

Backward stability is the standard modern yardstick because it is *achievable*
and *checkable*: Gaussian elimination with partial pivoting, QR factorisation,
and the standard library's linear algebra routines are all backward stable. The
combination

$$\text{forward error} \;\lesssim\; \kappa(A) \times \text{backward error}$$

is the whole story: a backward-stable algorithm reduces the question to the
conditioning. **A stable algorithm cannot fix an ill-conditioned problem.**

## 5. Worked derivations

### 5.1 Condition number of a differentiable function

Let $f$ be differentiable at $x \ne 0$ with $f(x) \ne 0$. A small perturbation
$\Delta x$ produces, to first order,

$$\Delta f \approx f'(x)\,\Delta x.$$

Divide by $f(x)$ and multiply by $x/x$:

$$\frac{\Delta f}{f} \approx \frac{x f'(x)}{f(x)} \cdot \frac{\Delta x}{x}.$$

Taking absolute values gives the **relative condition number of evaluating $f$
at $x$**:

$$\boxed{\;\kappa_f(x) = \left|\frac{x f'(x)}{f(x)}\right|.\;}$$

Three immediate consequences:

- The absolute magnitude of $f$ is irrelevant; only the logarithmic derivative
  $d(\ln|f|)/d(\ln|x|)$ matters.
- A root of $f$ makes $\kappa$ infinite: quantities that vanish are numerically
  dangerous to compute as ratios.
- If $f(x) \approx x^{p}$ then $\kappa \approx |p|$: powers are as well
  conditioned as their exponent suggests.

### 5.2 Applying the formula

| $f$ | $f'(x)$ | $\kappa_f(x)$ | value at the tested point |
|---|---|---|---|
| $e^{x}$ | $e^{x}$ | $\|x\|$ | $10$ at $x=10$; $20$ at $x=20$ |
| $\ln x$ | $1/x$ | $1/\|\ln x\|$ | $10000.5$ at $x = 1.0001$; $0.0724$ at $x=10^{6}$ |
| $\sqrt{x}$ | $1/(2\sqrt{x})$ | $1/2$ | $0.5$ at $x=10^{-8}$ |
| $\sin x$ | $\cos x$ | $\|x\cot x\|$ | $0.6421$ at $x=1$ |

The demonstration computes each of these twice — once by a central-difference
estimate of $\mathrm{d}(\ln f)/\mathrm{d}(\ln x)$ and once from the closed form
above — and the two agree to four decimals:

```text
exp(x) at x = 10      10.0000      10.0000
ln(x) at x = 1.0001   10000.5000   10000.5000
ln(x) at x = 1e6       0.0724       0.0724
sqrt(x) at x = 1e-8    0.5000       0.5000
```

Two lessons from the table. First, conditioning is a *local* property: $\ln$ is
ill-conditioned near $x=1$ and well conditioned at $x=10^{6}$, because
$\kappa = 1/|\ln x|$ blows up as $\ln x \to 0$. Second, exponentiation is only
mildly ill-conditioned ($\kappa = x$): evaluating $e^{20}$ in binary64 loses
$\log_{10}20 \approx 1.3$ digits, which is entirely acceptable.

### 5.3 Cancellation, re-examined as conditioning

Take $f(x) = x - 1$ near $x = 1$:

$$\kappa_f(x) = \left|\frac{x \cdot 1}{x-1}\right| = \frac{x}{|x-1|}
\;\xrightarrow[x\to1]{}\; \infty.$$

Computing a difference of nearly equal numbers is *intrinsically*
ill-conditioned. This is the honest way to state what
[01-01-04](./04-floating-point.md) called catastrophic cancellation: the loss
is not a defect of the subtraction, it is the condition number of the question
"what is the difference between these two nearly equal numbers?", given that
the inputs are each known only to relative precision $u$.

Now the instructive case: $f(x) = e^{x} - 1$ for small $x$. Its own condition
number is

$$\kappa_f(x) = \left|\frac{x e^{x}}{e^{x}-1}\right| \xrightarrow[x\to0]{} 1,$$

so the **problem** is perfectly well conditioned. Yet computing it as
`math.exp(x) - 1` is inaccurate. Where does the error come from? The computed
exponential $y = \mathrm{fl}(e^{x})$ carries an absolute error of order $u$, and
the subtraction step $y \mapsto y - 1$ has condition number

$$\text{amp}(x) = \frac{y}{y-1} = \frac{e^{x}}{e^{x}-1} \approx \frac{1}{x}.$$

Since $y - 1$ is small while $y$ is near 1, a relative perturbation of $u$ in
$y$ produces a relative perturbation of about $u\,\mathrm{amp}(x)$ in the
result. The demonstration confirms this quantitatively:

| $x$ | observed relative error of `exp(x)-1` | $u \times \mathrm{amp}(x)$ |
|---|---|---|
| $10^{-2}$ | $1.09\times10^{-14}$ | $1.12\times10^{-14}$ |
| $10^{-4}$ | $4.33\times10^{-13}$ | $1.11\times10^{-12}$ |
| $10^{-6}$ | $3.80\times10^{-11}$ | $1.11\times10^{-10}$ |
| $10^{-8}$ | $1.11\times10^{-8}$ | $1.11\times10^{-8}$ |

`math.expm1` avoids the differencing step (it evaluates the series directly), so
its error stays at the level of $u$ for every $x$ in the table.

**The general rule this illustrates.** Composite algorithms inherit the worst
conditioning of their intermediate steps. A function can be well conditioned
while a particular route to it is not, which is precisely why "stability" is a
separate word.

### 5.4 Perturbation bound for a linear system

Let $A$ be nonsingular, $Ax = b$, and let the data be perturbed:
$(A + \Delta A)(x + \Delta x) = b + \Delta b$. Expand and subtract $Ax = b$:

$$\Delta A\,x + A\,\Delta x + \Delta A\,\Delta x = \Delta b
\;\;\Longrightarrow\;\;
\Delta x \approx A^{-1}\big(\Delta b - \Delta A\,x\big),$$

dropping the second-order term. Taking norms,

$$\|\Delta x\| \le \|A^{-1}\|\big(\|\Delta b\| + \|\Delta A\|\,\|x\|\big).$$

Divide by $\|x\|$ and use $\|x\| \ge \|b\|/\|A\|$ (which follows from
$b = Ax$ and the definition of the induced norm):

$$\frac{\|\Delta x\|}{\|x\|}
\;\le\; \|A\|\,\|A^{-1}\|
\left(\frac{\|\Delta b\|}{\|b\|} + \frac{\|\Delta A\|}{\|A\|}\right)
\;=\; \kappa(A)\left(\frac{\|\Delta b\|}{\|b\|}
+ \frac{\|\Delta A\|}{\|A\|}\right).$$

So the relative error of the solution is bounded by the relative error of the
data multiplied by

$$\kappa(A) = \|A\|\,\|A^{-1}\|.$$

This is the classical result; the point of the derivation is that the two
factors are *data error* and *problem conditioning*, and the algorithm does not
appear. A backward-stable solver contributes a perturbation
$\|\Delta A\|/\|A\| = \mathcal{O}(u)$, giving the practical rule

$$\text{expected relative error} \;\approx\; \kappa(A)\,u.$$

The demonstration puts that rule to the test with the **Hilbert matrix**
$H_{ij} = 1/(i+j-1)$ and $b = (1,\dots,1)$:

| $n$ | observed max relative error | $\kappa_\infty(A)$ | $\kappa_\infty(A)\,u$ |
|---|---|---|---|
| $3$ | $6.513\times10^{-15}$ | $7.480\times10^{2}$ | $8.304\times10^{-14}$ |
| $5$ | $3.668\times10^{-13}$ | $9.437\times10^{5}$ | $1.048\times10^{-10}$ |
| $8$ | $2.423\times10^{-8}$ | $3.387\times10^{10}$ | $3.761\times10^{-6}$ |
| $10$ | $1.927\times10^{-4}$ | $3.535\times10^{13}$ | $3.925\times10^{-3}$ |

Every observed error is below the predicted bound, and the growth with $n$
tracks $\kappa(A)u$ rather than anything about the elimination routine. The data
are given to full double precision and nothing is "noisy"; the loss of accuracy
is a property of the matrix.

**Practical consequence.** Never solve a linear system by forming
$A^\mathsf{T}A$ if you can avoid it: in the 2-norm,
$\kappa_2(A^\mathsf{T}A) = \kappa_2(A)^{2}$, so the normal equations square an
already-large condition number. That is why
least-squares codes use QR or SVD — see
[18-inverse-problems](../../18-inverse-problems/README.md).

### 5.5 Conditioning versus stability: a worked counterexample

Consider the family of integrals

$$I_n = \int_0^1 \frac{x^{n}}{x+10}\,dx, \qquad n = 0, 1, 2, \dots$$

Integrating by parts gives the exact recurrence

$$I_n + 10\,I_{n-1} = \int_0^1 x^{n-1}\,dx = \frac{1}{n},
\qquad\text{i.e.}\qquad
I_n = \frac{1}{n} - 10\,I_{n-1}.$$

**What the recurrence does to errors.** Suppose the value fed to the forward
recurrence carries an error $\varepsilon$. Then

$$I_n = \frac{1}{n} - 10\,I_{n-1}
\;\;\Longrightarrow\;\;
|\varepsilon_n| = 10\,|\varepsilon_{n-1}|,$$

so an error of $\varepsilon$ at $n=0$ becomes $10^{n}\varepsilon$ at step $n$.
After 16 steps it has been amplified by $10^{16}$ — every digit of a double is
gone.

**Running it backwards.** Rearrange the same identity:

$$I_{n-1} = \frac{1}{10}\left(\frac{1}{n} - I_n\right),$$

so an error in $I_n$ is *divided* by 10 at each step. Start from an
approximation to $I_{20}$ and errors shrink by $10^{-20}$ as you march down to
$I_0$.

**The measurement.** The demonstration tabulates relative errors against
reference values computed with 60-digit decimal arithmetic:

| $n$ | reference $I_n$ | forward relative error | backward relative error |
|---|---|---|---|
| $0$ | $0.095310179804$ | $7.85\times10^{-16}$ | $8.87\times10^{-17}$ |
| $8$ | $0.010194390766$ | $7.34\times10^{-7}$ | $1.87\times10^{-15}$ |
| $12$ | $0.007038976131$ | $1.06\times10^{-2}$ | $2.56\times10^{-11}$ |
| $15$ | $0.005712513633$ | $1.31\times10^{1}$ | $3.16\times10^{-8}$ |
| $20$ | $0.004347035818$ | $1.72\times10^{6}$ | $4.15\times10^{-3}$ |

The forward recurrence at $n=15$ gives $I_{15} = -0.0691$, a **negative**
number for an integral of a strictly positive integrand: meaningless. The
backward recurrence, started from an estimate of $I_{20}$ that is itself wrong
by 0.4%, delivers $I_0$ to a relative error of $8.9\times10^{-17}$ — full
double precision.

**Interpretation.** The integral is well conditioned as a function of its
parameters; what is badly conditioned is the map "given $I_0$, produce $I_n$",
which stretches errors by $10^{n}$. The forward recurrence is therefore an
*unstable* algorithm for the well-conditioned task of evaluating the integral,
and the backward recurrence is the stable one. Halving the error by
using higher precision does not help — each extra decimal digit is consumed in
one additional forward step. The fix is algorithmic: run the recurrence in the
direction in which errors contract. This is the archetypal conditioning-versus-
stability example, and it is why the two concepts must be kept apart:

- **Conditioning** tells you the best possible accuracy for a given accuracy in
  the data.
- **Stability** tells you whether your algorithm achieves it.

### 5.6 Why backward stability is the right standard

A backward-stable algorithm can be trusted *in a precise sense*: the answer it
returns is not the answer to your problem, but it is exactly the answer to a
problem whose data differ from yours by a relative amount of order $u$. Since
data in geophysics are never known to 16 significant digits, an algorithm that
perturbs the data by $10^{-16}$ relative has perturbed it far less than the
measurement did. That is a far more useful guarantee than "the error is small",
which is problem-dependent and often false.

The catch is stated by the inequality at the start of Section 4: if
$\kappa(A) = 10^{10}$, a backward error of $10^{-16}$ still yields a forward
error of $10^{-6}$ — and for a matrix with $\kappa$ above $10^{16}$ the answer
carries no correct digits at all, however stable the algorithm.

## 6. Python demonstration

```bash
python3 code/conditioning_demo.py
```

The script `code/conditioning_demo.py` uses only the standard library
(`math`, `decimal`, `fractions`) and contains a hand-written Gaussian
elimination (float, with partial pivoting) and an exact rational solver used as
the reference. It covers: absolute vs relative error, condition numbers
computed both numerically and analytically, the `exp(x)-1` cancellation with
the $u\,\mathrm{amp}$ prediction, Hilbert-matrix conditioning with exact
reference solutions, and the integral recurrence of Section 5.5.

The companion `code/floating_point_demo.py` (lesson 01-01-04) supplies the
round-off observation used in Section 2 of this lesson: an anomaly computed as
the difference of two values near $10^{5}$ mGal loses about five decimal digits
to the common part, but that is a *conditioning* statement about differencing,
not an error introduced by the subtraction, which is exact.

Observed output worth dwelling on (verbatim from a run):

```text
  n  max relative error    cond_inf(A)     cond * u
  3           6.513e-15      7.480e+02    8.304e-14
 10           1.927e-04      3.535e+13    3.925e-03
```

and

```text
I_15 computed forward = -0.06912212310730485  (negative: meaningless,
since the integrand is positive everywhere)
```

Both are examples of the same principle: **the problem fixes the best
achievable accuracy; the algorithm determines whether you get it.**

## 7. Exercises

Ten graded exercises with full worked solutions are in
[`exercises/05-error-and-conditioning-exercises.md`](./exercises/05-error-and-conditioning-exercises.md)
and
[`exercises/05-error-and-conditioning-solutions.md`](./exercises/05-error-and-conditioning-solutions.md).

Three to attempt now, closed-book:

**★1.** Compute the absolute and relative error of approximating $1/7$ by
$0.142857$, and state which of the two describes the quality of the
approximation to a reader who does not know the size of the quantity.

**★★2.** Using $\kappa = |x f'(x)/f(x)|$, find the condition number of
$f(x) = \sin x$ at $x = \pi$ and explain the answer. What does it tell you about
estimating a small phase residual from a sinusoid?

**★★★3.** Verify the perturbation bound of Section 5.4 numerically for the
$5\times5$ Hilbert matrix: perturb $b$ by a relative amount $\rho$ in a random
direction, solve with the float elimination routine, and compare the observed
$\|\Delta x\|_\infty/\|x\|_\infty$ with $\kappa_\infty(A)\rho$. Report the
observed amplification ratio for $\rho = 10^{-3}, 10^{-6}$ and discuss why the
bound is not reached exactly.

## 8. Common mistakes

1. **Reporting an absolute error without the size of the quantity.** "Within
   0.01" says nothing until the reader knows whether the quantity is 0.05 or
   50 000.
2. **Confusing a small residual with a small error.** $\|b - A\hat{x}\|$ being
   tiny is guaranteed by a backward-stable solver even when $\hat{x}$ is
   rubbish, because the residual is insensitive to the conditioning.
3. **Blaming the algorithm for an ill-conditioned problem.** No amount of
   precision fixes downward continuation; the problem must be regularised or
   reformulated.
4. **Solving least squares through the normal equations** and then being
   surprised by the loss of digits: $\kappa(A^\mathsf{T}A) = \kappa(A)^{2}$.
5. **Treating conditioning as a property of the matrix format rather than of the
   matrix and the norm.** $\kappa$ depends on the norm you choose; quote it.
6. **Assuming higher precision is the fix for instability.** Forward recurrence
   5.5 consumes one decimal digit per step regardless of the working precision.
7. **Mixing measurement uncertainty with numerical error in one error bar.**
   Report them separately; they have different causes and different fixes.

## 9. Real-world applications

- **Downward continuation of potential fields.** Continuing a field measured at
  the surface down to a depth $z$ multiplies each wavenumber $k$ by
  $e^{|k|z}$. This is conditioning made explicit: the amplification is
  exponential in the product of wavenumber and depth, so the short wavelengths
  that would resolve deep structure are precisely the ones destroyed. Any
  practical implementation multiplies by a low-pass filter — a regularisation
  chosen to bound $\kappa$.
- **Depth estimation from gravity and magnetics.** The anomaly of a body at
  depth $z$ varies as $z^{-2}$ (point mass) or as a more slowly varying function
  for extended bodies, so the sensitivity $\partial g/\partial z$ falls with
  depth and the inverse problem becomes progressively more ill-conditioned.
  This is why there is an "ambiguity" literature in potential-field methods:
  it is a conditioning statement, not a measurement failure.
- **Seismic tomography.** The systems that arise from a large velocity model are
  ill-conditioned, and how ill-conditioned depends on the parametrisation, the
  ray coverage and the damping applied — which is why tomographers spend their
  effort on resolution and trade-off analysis rather than on quoting a single
  condition number. In practice the work is done with iterative solvers,
  preconditioning and explicit damping rather than with a direct factorisation.
- **Geodetic time series.** Estimating a secular rate from a position series is
  a linear least-squares problem whose condition number is controlled by the
  span and the noise model, both measurable; the numerical conditioning is
  irrelevant compared with the noise, and saying which one dominates is part of
  the analysis.
- **Attenuation and Q estimation.** Spectral-ratio methods difference the
  logarithms of two amplitudes measured at two frequencies; the differencing and
  the logarithmic sensitivity set the conditioning, which is why $\log$
  conditioning (Section 5.2) matters here.

## 10. Further reading

- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapters 1 (principles of finite-precision computation),
  3 (perturbation theory for linear systems) and 7 (error analysis of direct
  methods). Level: advanced undergraduate upward. The subtitle of Chapter 1 —
  the distinction between forward and backward error — is the frame used here.
- **Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
  Lectures 12 ("Conditioning of a problem") and 14–16 (stability). Level:
  intermediate. The clearest short treatment of conditioning as a geometry of
  level sets, and the source of the residual-versus-error distinction.
- **Wilkinson, J. H. (1963). *Rounding Errors in Algebraic Processes*.
  Prentice-Hall.** Level: advanced. The origin of backward error analysis;
  historical, but the ideas are still the standard.
- **Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.).
  Johns Hopkins University Press.** Chapters 2 and 3. Level: graduate. The
  reference for condition numbers and the error bounds of Gaussian elimination.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).
  University Science Books.** Level: beginner to intermediate. For the
  *measurement* side of the error budget, which is deliberately not treated
  here.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 11. Related lessons

- [04 Floating-Point Representation, Round-Off and Catastrophic
  Cancellation](./04-floating-point.md) — the error model and the cancellation
  phenomenon that this lesson reinterprets as conditioning.
- [01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md)
  — significant figures, and the reporting discipline this lesson justifies.
- [02 Algebra, Functions and Modelling](../02-algebra/README.md) — the algebraic
  rearrangements that improve conditioning without changing the mathematics.
- [18-inverse-problems](../../18-inverse-problems/README.md) — ill-posedness,
  regularisation, and why geophysical inversion lives at the conditioning
  boundary.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  discretisation error, which competes with the round-off described here.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) —
  uncertainty quantification, the measurement-side counterpart to numerical
  error.

## Self-assessment checklist

- [ ] I can define absolute, relative, forward and backward error, and the
      residual, without notes.
- [ ] I can derive $\kappa_f(x) = |x f'(x) / f(x)|$ and evaluate it for a given
      function.
- [ ] I can explain why a small residual does not guarantee a small error.
- [ ] I can state the difference between conditioning and stability and give one
      example of each.
- [ ] I can bound the forward error of a linear solve using $\kappa(A)$ and the
      data perturbation.
- [ ] I can name an ill-conditioned problem in geophysics and say why no
      algorithm removes the difficulty.
