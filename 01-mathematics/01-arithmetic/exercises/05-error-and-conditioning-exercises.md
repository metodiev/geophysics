# Exercises — 01-01-05 Absolute vs Relative Error, Conditioning and Stability

Attempt these **closed-book**, on paper, before opening the
[solutions](./05-error-and-conditioning-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Several exercises require computation. Write your prediction first, then run it.

---

## ★ Foundational

**★1.** The rational number $1/7$ is approximated by `0.142857`.

(a) Compute the absolute error.

(b) Compute the relative error.

(c) Which of the two would you put in a paper, and why?

(d) Repeat (a) and (b) for the approximation of $6.674\times10^{-11}$ by
`6.7e-11`, and state which approximation is *relatively* better.

---

**★2.** Use $\kappa_f(x) = \left| x f'(x) / f(x) \right|$ to compute the relative
condition number at the given points, and say in one phrase whether the
evaluation is well or badly conditioned:

(a) $f(x) = \sqrt{x}$ at $x = 10^{-8}$;

(b) $f(x) = \ln x$ at $x = 1.0001$;

(c) $f(x) = \ln x$ at $x = 10^{6}$;

(d) $f(x) = e^{x}$ at $x = 20$.

Then explain, in terms of $\kappa$, why `ln x` is a poor way to compute very
small quantities of the form $(x-1)$.

---

**★3.** Define **forward error**, **backward error** and **residual** in one
sentence each. Then consider

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \qquad b = (3, 4),$$

whose exact solution is $x = (1,1)$. Take the computed solution
$\hat{x} = (1.0000001,\ 0.9999999)$ and:

(a) compute the residual $r = b - A\hat{x}$;

(b) compute the forward error $\hat{x} - x$;

(c) compute $\|\Delta x\|_\infty/\|x\|_\infty$ and
$\|r\|_\infty/\|b\|_\infty$;

(d) compute $\kappa_\infty(A)$ and check that the bound
$\|\Delta x\|/\|x\| \le \kappa(A)\|r\|/\|b\|$ holds.

---

**★4.** A relative gravimeter resolves $0.01$ mGal. It is read at a station
where the value is $979\,812.37$ mGal.

(a) Compute the relative uncertainty of the reading.

(b) Compute $u = 2^{-53}$, the unit roundoff of binary64.

(c) Compute the ratio of (a) to (b). Which term dominates the error budget?

---

## ★★ Applied

**★★5.** The subtraction $1 - \cos x$ is the source of the cancellation studied
in lesson 01-01-04.

(a) For $x = 10^{-4}$ compute the amplification factor of the subtraction step,
$\mathrm{amp}(x) = \cos x / (1-\cos x)$, using binary64 values.

(b) Predict the relative error of the numerator as $u\,\mathrm{amp}(x)$ and
compare it with the relative error observed in lesson 01-01-04 for
$(1-\cos x)/x^{2}$ at that $x$, which is $5.24\times10^{-9}$.

(c) Repeat (a) and (b) at $x = 10^{-6}$. Does the predicted error still track the
observed one, and what happens to it as $x$ decreases further?

(d) Explain in two sentences why the *problem* $(1-\cos x)$ is
well-conditioned as a function evaluated at a given $x$, while the *route*
through `cos` and a subtraction is not.

---

**★★6.** The lecture's Hilbert-matrix experiment gave:

| $n$ | observed max relative error | $\kappa_\infty(A)$ | $\kappa_\infty(A)u$ |
|---|---|---|---|
| $3$ | $6.513\times10^{-15}$ | $7.480\times10^{2}$ | $8.304\times10^{-14}$ |
| $5$ | $3.668\times10^{-13}$ | $9.437\times10^{5}$ | $1.048\times10^{-10}$ |
| $8$ | $2.423\times10^{-8}$ | $3.387\times10^{10}$ | $3.761\times10^{-6}$ |
| $10$ | $1.927\times10^{-4}$ | $3.535\times10^{13}$ | $3.925\times10^{-3}$ |

(a) Compute the ratio observed$/(\kappa u)$ for each row.

(b) Is the bound violated anywhere? What does a ratio of about $0.005$–$0.08$
suggest about the tightness of the bound?

(c) At approximately which $n$ would you expect the computed solution to have
**no** correct significant digits at all, and how would you estimate that
without running the solver?

(d) The right-hand side is exactly $(1,1,\dots,1)$ and the entries of $H$ are
computed to full double precision. Someone says "the inputs are exact, so the
answer must be exact". Refute that in three sentences, using the terminology of
this lesson.

---

**★★7.** The integral family $I_n = \int_0^1 x^{n}/(x+10)\,dx$ satisfies
$I_n = 1/n - 10 I_{n-1}$.

(a) Show that the forward recurrence amplifies an initial error $\varepsilon$ by
a factor of $10^{n}$.

(b) Starting from $I_0 = \ln(1.1)$, which is known only to a relative error of
order $u$, how many forward steps does it take before the error exceeds the
value itself? Give the number of steps and the reasoning.

(c) The lecture's measured forward relative error at $n = 8$ is
$7.34\times10^{-7}$. Compare it with your prediction $10^{n}u$ and comment; note
that the reference $I_n$ values used were computed at 60 decimal digits.

(d) Show that the backward recurrence
$I_{n-1} = (1/n - I_n)/10$ contracts an error by 10 per step, and explain why
starting from a crude estimate of $I_{20}$ can still deliver $I_0$ to full
precision. (The lecture measured a starting relative error of $4.15\times10^{-3}$
at $n=20$ and $8.87\times10^{-17}$ at $n=0$.)

---

**★★8.** An instrument has an uncertainty $\delta$ and reports a value $v$.
Complete the table, and rank the measurements by relative uncertainty:

| measurement | $\delta$ | $v$ | relative uncertainty |
|---|---|---|---|
| relative gravimeter | $0.01$ mGal | $979\,812.37$ mGal | |
| magnetometer | $1$ nT | $500$ nT | |
| GNSS baseline | $5$ mm | $10\,000$ m | |
| binary64 roundoff $u$ | — | — | $1.11\times10^{-16}$ |

Then answer: for which of these measurements is floating-point round-off
*irrelevant*, and for which would you need to think about it? Justify each
answer with a ratio, not an adjective.

---

## ★★★ Research-oriented

**★★★9.** This exercise tests the perturbation bound of Section 5.4
quantitatively, using the $5\times5$ Hilbert matrix with $b = (1,1,1,1,1)$.

(a) Compute an exact reference solution using `fractions.Fraction` Gaussian
elimination, then convert to float.

(b) Perturb the right-hand side by a relative amount $\rho$ in the **alternating
direction** $v = (1,-1,1,-1,1)$, normalised so that
$\|\delta b\|_\infty/\|b\|_\infty = \rho$:
`b_new[i] = 1.0 + rho * v[i] / max(abs(z) for z in v)`. Solve the perturbed
system in binary64 with your own elimination routine.

(c) For $\rho = 10^{-3}$ and $\rho = 10^{-6}$, compute
$\|\Delta x\|_\infty/\|x\|_\infty$ and the observed amplification
$(\|\Delta x\|_\infty/\|x\|_\infty)/\rho$. Report both.

(d) Compare the observed amplification with $\kappa_\infty(A) = 9.437\times10^{5}$
and with the bound $\kappa_\infty(A)\rho$. By what factor is the bound larger
than reality?

(e) Now repeat with the **constant** direction $v = (1,1,1,1,1)$ and explain the
result without computing anything. (Hint: what is $x$ when $b$ is scaled by
$1+\rho$? Linearity applies.)

(f) Write three or four sentences stating what the exercise shows about the
difference between a worst-case bound and a measured amplification, and the
limits of your conclusion (one matrix, one norm, two directions).

---

**★★★10.** Two receivers record the same seismic arrival. The picks are

$$t_1 = 1.500\ \mathrm{s} \pm 1\ \mathrm{ms}, \qquad
t_2 = 1.520\ \mathrm{s} \pm 1\ \mathrm{ms},$$

and the quantity of interest is the differential arrival time
$\Delta t = t_2 - t_1$.

(a) Compute $\Delta t$ and its relative error in the worst case, treating both
pick uncertainties as independent and adding them in the most pessimistic way.
Verify the result directly as $(2\ \mathrm{ms})/\Delta t$.

(b) Compute the quantity $t/\Delta t$ with $t = 1.5$ s and show that it equals the
amplification that the conditioning $\kappa$ of the differencing step predicts:
if each pick carries relative uncertainty $\varepsilon = 1\ \mathrm{ms}/1.5\
\mathrm{s}$, the relative uncertainty of $\Delta t$ is about $\kappa\varepsilon$.
Evaluate that product.

(c) Reconcile the answers to (a) and (b). They differ by about a factor of two —
say precisely why.

(d) Find the value of $\Delta t$ for which the relative uncertainty of the
differential arrival falls to 1%, assuming the same 1 ms pick uncertainty.
Interpret the number as a statement about survey geometry.

(e) Suppose the two picks were correlated rather than independent (same
instrument, same operator, a common clock offset). Would the relative
uncertainty of $\Delta t$ be larger or smaller? Explain in one sentence, and
state what that implies for the conditioning of differential measurements.

---

## Extension ideas

- Compute $\kappa_\infty$ for the $n\times n$ Hilbert matrix for
  $n = 1,\dots,10$ and fit the growth. Is it exponential in $n$? Report the
  empirical growth and the limits of your fit.
- Take a forward model from your own field of interest and compute numerically
  the sensitivity $|x f'(x)/f(x)|$ over a plausible parameter range. Plot (by
  table, or with a plotting library if you have one) the regions where the
  inversion will lose more than half the available digits. This is the first
  step of a real resolution study.
- Reproduce the `exp(x)-1` result with `Decimal`: compute the true value at
  100 digits, then compare both `exp(x)-1` and `expm1(x)`. Confirm that
  `expm1` is accurate to $u$ and explain the residual difference.
- Find an unstable recurrence in a textbook (they are common in
  special-function evaluation) and devise the stable direction. Report the
  amplification factor per step for each direction.
