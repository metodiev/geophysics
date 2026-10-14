# Exercises — 03-03-08 scipy.special and scipy.stats in Practice

Attempt these **closed-book** before opening the
[solutions](./08-special-stats-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/special_stats_demo.py`](../code/special_stats_demo.py) require you to
run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/special_stats_demo.py
```

---

## ★ Foundational

**★1.** The demo reports the diffusion solution
$T/\Delta T = \mathrm{erfc}(z/2\sqrt{\kappa t})$ with
$\kappa = 1.2\times10^{-6}$ m² s⁻¹, $\Delta T = 12$ K:

```
          100      50              0.406254   0.565609    6.7873
         1000      50              0.128469   0.855832   10.2700
        10000      50              0.040625   0.954184   11.4502
```

(a) Verify the argument 0.406254 by hand.
(b) Verify that $\mathrm{erfc}(0.406254) = 0.565609$ using a table or a
calculator, and state the unit of the third column.
(c) The table reports 0.000000 at $z = 1000$ m, $t = 100$ yr. Compute the true
value and state why zero is the right physical answer.
(d) Compute the surface heat-flow perturbation at $t = 100$ yr and compare with
the value at 1000 yr (86.9769 mW m⁻²).

---

**★2.** The demo reports the three routes to the same value:

```
          x             erfc(x)    2*ndtr(-x sqrt2)            1-erf(x)   difference
       1.00  0.1572992070502852  0.1572992070502851  0.1572992070502852     1.11e-16
```

and the large-argument table:

```
        x         erfc(x)      1 - erf(x)        erfcx(x)
      4.0    1.541726e-08    1.541726e-08    1.369995e-01
      8.0    1.122430e-29    0.000000e+00    6.998517e-02
     26.0    5.663192e-296    0.000000e+00    2.168358e-02
     30.0    0.000000e+00    0.000000e+00    1.879589e-02
```

(a) State the identity linking `erfc` and `ndtr`.
(b) Explain why `1 - erf(x)` returns exactly zero from $x = 8$ onward.
(c) Compute $\mathrm{erfc}(4)$ from `erfcx` and verify.
(d) Compute $\ln\mathrm{erfc}(30)$ from the tabulated `erfcx(30)`, and explain
why that is the only route that works.

---

**★3.** The magnitude fit reports

```
    b_hat          = 0.981599
    standard error = b_hat/sqrt(n) = 0.025345
    truth          = 1.000000   difference = -0.726 standard errors
    stats.expon.fit(floc=0) gives scale = 0.442436 -> b = 0.981599
```

(a) State the maximum-likelihood formula for $b$ in terms of the sample mean and
$m_c$.
(b) Verify the standard error from $n = 1500$.
(c) Verify the conversion from the fitted exponential scale to $b$.
(d) Explain what "0.726 standard errors from the truth" does and does not tell
you.

---

## ★★ Applied

**★4.** The cumulative least-squares alternative reports

```
    slope = -0.852307 -> b = 0.852307 (standard error 0.017304, r^2 = 0.986180)
    bias against the MLE: -0.129293, i.e. -13.17%
```

(a) Compute the ratio of the least-squares $b$ to the maximum-likelihood $b$.
(b) Explain why the quoted standard error of 0.017304 is not merely inaccurate
but meaningless.
(c) The $r^2$ is 0.986. Explain why a high $r^2$ is not evidence that the
regression's assumptions hold.
(d) State how you would detect the dependence problem before fitting, using one
line of code.

---

**★5.** The goodness-of-fit section reports

```
    D against the *fitted* exponential      = 0.015415, naive p = 0.863
    D against the *true* distribution       = 0.020755, p = 0.531  (no parameters estimated: valid)
    Monte-Carlo calibration of the fitted case: D = 0.015415, p = 0.728
```

(a) Explain the difference between the first and second rows.
(b) Explain the direction of the discrepancy between the naive and calibrated
p-values, and why it must be in that direction.
(c) The mis-specified sample gives $D = 0.113479$ with a calibrated
$p = 0.0005$ and a fitted $b = 1.1840$. Explain what the two numbers together
show.
(d) Design the Monte-Carlo calibration in pseudocode, and state the number of
replications needed for a p-value accurate to 0.01.

---

**★6.** The correlation table is

```
          n         r   p (Pearson)   p (Spearman)          95% CI for rho
         10    0.7929     6.216e-03      3.815e-03        [+0.326, +0.949]
        100    0.4929     1.895e-07      1.605e-05        [+0.328, +0.628]
      20000    0.3525     0.000e+00      0.000e+00        [+0.340, +0.365]
```

(a) Compute the width of the 95% confidence interval at $n = 10$ and at
$n = 20000$, and the ratio.
(b) Compute the ratio of the widths you would predict from the $n^{-1/2}$
scaling and compare.
(c) Explain why the Pearson p-value at $n = 20\,000$ prints as 0.000e+00.
(d) State which single number you would report from this table if you had only
one line to quote, and why.

---

**★7.** The regression section reports

```
    slope = 11.0264 +/- 0.9019 (log10 mD per unit porosity)
    t(0.975, 23) = 2.0687 against the normal quantile 1.9600
    95% interval from t: [9.1607, 12.8921]   width 3.7313
    95% interval from z: [9.2587, 12.7941]   width 3.5353
    The z-interval is 5.25% too narrow and its actual coverage is 93.78%, not 95%
```

(a) Verify the t-interval endpoints from the slope and its standard error.
(b) Verify the 5.25% figure.
(c) Compute the coverage of the z-interval using
$2F_t(1.96, 23) - 1$.
(d) State the number of samples at which the z-interval would be within 1% of
the t-interval, and justify the answer with the $t$ quantile.

---

## ★★★ Research-oriented

**★8.** The lognormal section reports

```
    model                               KS D     naive p    log-likelihood
    normal(mu, sigma), fitted        0.40656   2.903e-60           -1375.7
    lognormal(s, 0, scale), fitted     0.02651   9.341e-01              41.1
    Shapiro-Wilk on log(k): W = 0.99542, p = 0.2912
    mean k   = 1.783 mD   median k = 0.08821 mD   geometric mean = 0.07779 mD
    the arithmetic mean is 20.2 times the median
```

(a) Verify the model's population statistics: for
$\log_{10}k \sim N(\mu = -1, \sigma = 1.2)$, compute the population median, the
population mean and their ratio.
(b) Explain why the sample mean (1.783 mD) differs from the population mean you
computed, and by how much in units of the standard error of the mean.
(c) Explain why the Shapiro test on $\log k$ is the correct test for the
lognormal claim, and what its $p = 0.29$ does and does not prove.
(d) State the two sentences that should accompany a reported mean permeability
of 1.783 mD.

---

**★9.** A catalogue of 8000 events above $m_c = 2.2$ is fitted with
$b = 0.94 \pm 0.011$ (Aki–Utsu) and a calibrated Kolmogorov–Smirnov
$p = 0.04$.

(a) Compute the expected standard error and state whether the reported value is
consistent with the formula.
(b) The calibrated p-value is 0.04. State the two reasons this might occur even
when the catalogue is complete and the GR law holds, and how to distinguish
them.
(c) The catalogue was compiled from two networks with different detection
thresholds, one complete at $m_c = 2.2$ and one at $m_c = 2.8$. Explain
precisely how the mixture biases the fitted $b$, in which direction, and what to
do about it.
(d) Propose the one additional computation that would settle whether the
magnitude distribution is truly GR.
