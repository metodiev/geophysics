# Exercises — 03-03-03 scipy.optimize: Root Finding, Minimisation and Curve Fitting

Attempt these **closed-book** before opening the
[solutions](./03-optimize-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/optimize_demo.py`](../code/optimize_demo.py) require you to run it
and report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/optimize_demo.py
```

---

## ★ Foundational

**★1.** The demo fits $A e^{-t/\tau} + c$ to 25 samples with a known
$\sigma = 1.5$ K and reports

```
  absolute_sigma=True   ->  reduced chi^2 = 1.243904
    parameter         fitted     1 sigma       truth  difference/sigma
    A (K)            94.7625      1.0974     95.0000              0.22
    tau (yr)       3051.1401     91.8566   3000.0000              0.56
    offset (K)        4.1972      0.7332      4.0000              0.27
```

(a) State the number of degrees of freedom.
(b) Compute the total $\chi^2$.
(c) Compute the reduced $\chi^2$ that would be reported if the same data were
fitted with $\sigma$ declared as 0.75 K, and say whether that would be a better
or worse fit.
(d) Explain in one sentence what "difference/sigma = 0.56" for $\tau$ means.

---

**★2.** The demo's second fit reports larger error bars at the same parameters:

```
  absolute_sigma=False  ->  reduced chi^2 = 1.243904
    A (K)            94.7625      1.2239     95.0000              0.19
    tau (yr)       3051.1401    102.4480   3000.0000              0.50
```

(a) Compute the ratio of the $\tau$ error bars between the two fits.
(b) Show algebraically that the ratio equals $\sqrt{\chi^2_\nu}$.
(c) State which fit's error bars you would quote if $\sigma = 1.5$ K came from
the instrument, and why.
(d) Predict, with a reason, what happens to the `absolute_sigma=True` error
bars if the noise level in the synthetic data doubled while the stated
$\sigma$ stayed at 1.5 K.

---

**★3.** The demo brackets the Birch–Murnaghan isotherm with
$K_0 = 260$ GPa, $K_0' = 4$:

```
    brentq        V/V0 = 0.748138742561   iterations = 11   residual P-P_target = +2.84e-14 GPa
```

(a) Evaluate $P(V/V_0)$ at $V/V_0 = 0.5$, 1.0 and 1.5 and confirm that the
bracket $(0.5, 1.5)$ contains a sign change for a target of 135 GPa.
(b) Explain in one sentence why the bracket is a *guarantee*.
(c) Estimate how many iterations pure bisection would need to reach a bracket
width of $10^{-14}$, and compare with `brentq`'s 11.
(d) State what the residual column measures.

---

## ★★ Applied

**★4.** Use the demo's printed correlation matrix

```
          A    1.00000 -0.09193 -0.31027
        tau   -0.09193  1.00000 -0.82593
     offset   -0.31027 -0.82593  1.00000
```

(a) State which parameter pair is the most degenerate, and the value of the
correlation coefficient.
(b) The demo also measures that over a window of one time constant the
$A$–$\tau$ correlation is 0.967 and $\sigma_\tau = 316.4$ yr, while over four
time constants it is $-0.075$ and 94.9 yr. Compute the ratio of the two
$\sigma_\tau$ values.
(c) Explain, in terms of what the data constrain, why a short window cannot
separate $A$ from $\tau$.
(d) Design an experiment that would determine $\tau$ to 1% and state the
window length required.

---

**★5.** The demo reports the cost of a Jacobian:

```
    variant                                      resid vectors  jac eval  point evals
    least_squares(method=lm), finite-difference Jacobian            35         0         2100
    least_squares(method=lm), analytic Jacobian              8         8          960
```

(a) State the cost, in residual-vector evaluations, of one forward-difference
Jacobian for $p$ parameters.
(b) The finite-difference route used 35 residual vectors for about how many
Jacobians? Show the arithmetic.
(c) Compute the ratio 2100/960 and explain why it is not 5.
(d) Predict the ratio for a model with 12 parameters and explain how it scales.

---

**★6.** The demo shows that an open root finder returns one root of an
equation with three:

```
          0.00    fsolve      1.000000    1.78e-15
          1.60    fsolve      2.000000    0.00e+00
          2.50    fsolve      1.000000    1.78e-15
          4.00    fsolve      3.000000   -7.11e-15
```

(a) Explain why the start point 2.5 lands on the root at 1 rather than at 2.
(b) Design a procedure that finds *all three* roots reliably, and state its
guarantee.
(c) Explain what `brentq(f, 2.2, 2.4)` does and why that behaviour is
preferable to returning 2.3.
(d) A colleague fits a geophysical model with `fsolve`, obtains a residual of
$10^{-12}$, and concludes that the model is uniquely determined. State exactly
what is wrong with that conclusion.

---

**★7.** The two-term decay fit gives

```
    method              nfev                 RSS   max |rel. param diff|
    Nelder-Mead          356        201.79068433                5.70e-09
    Powell               267        201.79070141                6.90e-05
    BFGS                  32        201.79068433                1.57e-08
```

(a) Explain why Nelder-Mead needs an order of magnitude more evaluations than
BFGS on a smooth problem, and why that is not an argument against Nelder-Mead.
(b) Powell's RSS is larger in the eighth digit. State two possible causes and
how to distinguish them.
(c) The demo reports that a least-squares fit restarted at the solution stops
after one evaluation. Explain what this does and does not prove.
(d) Design a two-stage fitting strategy for a misfit function with several
local minima, and state what each stage is for.

---

## ★★★ Research-oriented

**★8.** Derive the degeneracy measured in ★4(b) analytically.

(a) For $\Delta T(t) = A e^{-t/\tau} + c$ with $t$ confined to
$[0, \tau]$, expand the exponential to second order and show that the data
constrain $\{A, A/\tau, A/\tau^2\}$ — three combinations that determine
$\{A, \tau\}$ only through the ratios.
(b) Hence explain why the $A$–$\tau$ correlation tends to $\pm1$ as the window
shrinks, and why a three-parameter fit to a one-time-constant window is
still formally determined but practically degenerate.
(c) Modify the demo to fit windows of 0.25, 0.5, 1, 2 and 4 time constants with
the same sample count, and tabulate $\sigma_\tau$ and the $A$–$\tau$
correlation. Fit a local exponent $p$ in $\sigma_\tau \propto W^{-p}$ between
consecutive windows and state whether $p$ is constant.
(d) State whether collecting four times as many samples over the same short
window helps, and why.

---

**★9.** A published study inverts for a thermal time constant from borehole
data spanning 0.8 time constants and reports $\tau = 240 \pm 8$ yr, having
fitted with `curve_fit(p0=(...)` and `absolute_sigma=False`.

(a) State the two questions you would ask before accepting the $\pm8$ yr.
(b) The covariance matrix implies a correlation of 0.994 between the amplitude
and the time constant. Compute $\sigma_A\sqrt{1-r^2}$ and state what it
represents.
(c) Write the two sentences that should accompany a reported $\tau$ from a
window shorter than two time constants.
(d) Propose the single most informative additional measurement, with a reason.
