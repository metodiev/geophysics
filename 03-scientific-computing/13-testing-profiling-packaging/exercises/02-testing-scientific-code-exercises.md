# Exercises — 03-13-02 Testing Numerical Code Against Analytic Solutions

Attempt these **closed-book** before opening the
[solutions](./02-testing-scientific-code-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems marked **[demo]** refer to
[`../code/analytic_solutions_demo.py`](../code/analytic_solutions_demo.py); run
it and report its actual output:

```
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/analytic_solutions_demo.py
```

The lesson is [`../02-testing-scientific-code.md`](../02-testing-scientific-code.md).

---

## ★ Foundational

**★1. [demo]** The demo tabulates the steady-problem convergence:

| $n$ | $h$ | $\max\lvert u_h - u_{\text{exact}}\rvert$ | observed $p$ |
|---|---|---|---|
| 8 | $1.111\times10^{-1}$ | $1.019379\times10^{-3}$ | — |
| 16 | $5.882\times10^{-2}$ | $2.876115\times10^{-4}$ | 1.8255 |
| 64 | $1.538\times10^{-2}$ | $1.972041\times10^{-5}$ | 1.9552 |
| 256 | $3.891\times10^{-3}$ | $1.261675\times10^{-6}$ | 1.9887 |

(a) Compute the missing observed orders for $n = 32$ and $n = 128$.
(b) State the order $p$ of the scheme and the mean of the last three observed
orders.
(c) Explain why the sequence rises towards 2 from below rather than oscillating
around it.

**★2.** For the explicit FTCS scheme on $u_t = \kappa u_{xx}$ with stability
condition $r = \kappa\,\Delta t/\Delta x^2 \le 1/2$:

(a) With $\Delta x = 0.005$ m and $\kappa = 10^{-6}$ m²/s, compute
$\Delta t_{\max}$.
(b) With $\Delta t_{\max}$ and $L = 1$ m, how many steps are needed to reach
$t = 2\times10^4$ s?
(c) If a student halves $\Delta x$ and keeps $\Delta t = \Delta t_{\max}$ from
(a), what happens?

**★3.** Classify each of these as code verification, solution verification or
validation, and justify each in one sentence:

(a) Comparing an FTCS solution with the analytic decay of a sine mode.
(b) Comparing a numerical heat-flow solution against a thermocouple record.
(c) Estimating the discretisation error of one particular fine-grid solution by
Richardson extrapolation.
(d) Comparing a prism-based gravity routine against $GM/d^2$ in the far field.

---

## ★★ Applied

**★★4. [demo]** The transient experiment measures

| $n_t$ | $\Delta t$ | measured max error |
|---|---|---|
| 2000 | 10.0 s | $4.6645\times10^{-6}$ |
| 4000 | 5.0 s | $6.6633\times10^{-7}$ |
| 8000 | 2.5 s | $1.3327\times10^{-6}$ |
| 16000 | 1.25 s | $2.3322\times10^{-6}$ |

with $A\phi = 4.0587\times10^{-6}$ and $B = 1.948\times10^{-6}$ per second.

(a) Using $\ln u_{\text{num}} - \ln u_{\text{exact}} = A\phi - \tfrac12 B\Delta t$,
predict the error at $\Delta t = 1.25$ s and compare with the measurement.
(b) Predict at which $\Delta t$ the two terms cancel, and say between which two
tabulated steps the measured minimum lies.
(c) A test asserts that halving $\Delta t$ always reduces the error. State which
two table rows refute it.

**★★5.** Richardson extrapolation from the error sequence. The refinement factor
between grids is $r = n_2/n_1$, so the observed order from any pair is
$p = \log_2(e_{n_1}/e_{n_2})/\log_2 r$.

(a) Compute $p$ from the successive pairs $(8 \to 16)$, $(64 \to 128)$ and
$(128 \to 256)$.
(b) Compute $p$ from the *non-successive* pairs $(8 \to 64)$ and
$(64 \to 256)$ using the same formula, and compare with the successive-pair
values.
(c) The consistency test is $\lvert p_{\text{first}} -
p_{\text{last}}\rvert \le 0.1$. Apply it to $(16 \to 64 \to 256)$ and to
$(8 \to 64 \to 256)$, and state what a failure would have told you.

**★★6. [demo]** The sphere quadrature experiment reports, at $d = 1000$ m and
$d = 110$ m:

| grid | points | rel. error $d = 1000$ m | rel. error $d = 110$ m |
|---|---|---|---|
| 60, 120, 180 | 1.30 M | $4.037\times10^{-5}$ | $2.860\times10^{-4}$ |
| 160, 320, 480 | 24.58 M | $5.677\times10^{-6}$ | $4.002\times10^{-5}$ |

(a) The exterior field of a uniform sphere is exactly $GM/d^2$. What, then, is
the difference between the quadrature and $GM/d^2$ measuring?
(b) State the ratio of errors between the two grids at each depth, and comment on
whether the rule is first or second order.
(c) A student uses the $d = 500$ m result, where the relative difference is
$3.873\times10^{-5}$, to argue that "the sphere's finite size matters at the
0.004% level". Refute the argument in two sentences.

---

## ★★★ Research-oriented

**★★★7.** Design a manufactured solution for a one-dimensional advection–
diffusion problem with a *variable* velocity, $u_t + c(x)u_x = \kappa u_{xx}$ on
$[0,1]$ with Dirichlet boundaries.

(a) Choose $u(x,t)$ and derive the source term $f(x,t)$ that makes it exact.
(b) Explain which term of the original equation your choice exercises, and which
it leaves nearly untested.
(c) Describe the two-refinement experiment that would let you claim
second-order convergence, and state the tolerance you would assert.

**★★★8.** A colleague's inversion code produces a $b$-value of 1.016 from 137
events and reports it with no uncertainty. You have the catalogue.

(a) State the two verification steps you would run before trusting the estimate,
and the analytic reference each uses.
(b) The colleague refines their grid four times and reports that the estimate
"converges to 1.016". Explain what that does and does not establish.
(c) State the one measurement that could establish that the estimate is *right*
rather than merely converged, and say why no test suite can perform it.

**★★★9. [demo]** The lesson writes a test that asserts the *non-monotone*
behaviour of the refinement study:

```python
assert errs[1] < errs[0]           # coarsening dt helps at first ...
assert errs[2] > errs[1]           # ... and then stops helping
assert errs[2] / errs[1] == pytest.approx(2.0, rel=0.1)
```

(a) Explain why asserting this is more valuable than deleting the test and
loosening the tolerance.
(b) The ratio is asserted with `rel=0.1`, i.e. $\pm$10%. Justify that margin from
the measured values.
(c) Suppose a future NumPy release changes the summation order and the three
errors move in the eighth digit. Which of the three assertions is at risk, and
what would you do about it?
