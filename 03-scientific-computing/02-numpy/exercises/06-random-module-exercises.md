# Exercises — 03-02-06 Random Number Generation and Reproducible Seeds

Attempt these **closed-book** before opening the
[solutions](./06-random-module-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/random_demo.py`](../code/random_demo.py) require
you to run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/random_demo.py
```

Every stochastic answer must state the **seed**, the **number of samples**, and
the **standard error** of the quantity being reported.

---

## ★ Foundational

**★1.** Answer in one or two sentences each.

(a) What does a seed determine?
(b) Why can the same seed give different results in two different programs?
(c) Which function should be used to create a modern generator, and what does it
return?
(d) Why is `np.random.default_rng(42)` not a cryptographic generator?

---

**★2.** A test adds noise of nominal $\sigma = 3$ nT to a synthetic trace of
$N = 2500$ samples.

(a) Compute the standard error of the mean of that noise.
(b) Compute the standard error of the sample standard deviation, using
$\sigma/\sqrt{2N}$.
(c) State a two-sided acceptance interval for the sample mean at roughly the
$4\sigma$ level.
(d) Explain why the test must compare the *mean* against (a) rather than against
$\sigma$.

---

**★3.** For a Poisson process with rate $\lambda = 9$ events per day:

(a) State the distribution's mean and variance.
(b) State the relative standard deviation of a one-day count.
(c) Compute the number of days' counts needed to determine $\lambda$ to 1 per
cent.
(d) State one physical reason why earthquake occurrence is *not* Poisson, and the
standard processing step that is performed before assuming that it is.

---

**★4.** Write one line each:

(a) A seeded generator with seed 7.
(b) A draw of 1000 standard normal values from it.
(c) A draw of 1000 uniform values in $[10, 20]$.
(d) A random permutation of 1000 trace indices.
(e) A bootstrap resample (with replacement) of 1000 values from an array `v`.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) The two same-seed `normal(size=5)` draws and the `tobytes()` verdict.
(b) The legacy-API pair of results and the `identical:` verdict.
(c) The `nominal sigma`, `sample std (ddof=0)`, `expected std of the mean` and
`observed |mean|`.
(d) The Poisson mean and variance.
(e) The three rows of the $1/\sqrt{N}$ table.

---

**★★6.** A Monte Carlo inversion draws 2000 slowness models from a Gaussian
prior with $\sigma = 0.02$ s km⁻¹ and predicts a travel time for each.

(a) State the standard error of the *mean* predicted time if the individual
prediction has standard deviation 0.15 s.
(b) State the number of draws needed to reduce it by a factor of two.
(c) Explain why the answer depends on the *number of draws* and not on the
number of observations.
(d) State the correct way to quote the result, given that the answer is a
distribution of travel times rather than the mean.

---

**★★7.** A colleague writes

```python
def make_noise(n):
    np.random.seed(0)
    return np.random.normal(size=n)
```

(a) State two distinct defects.
(b) Rewrite the function so that it is reproducible in isolation and can be used
twice in the same program without correlation.
(c) Explain what "used twice without correlation" means here, and what would go
wrong if the function kept a module-level generator and was called from two
threads.

---

## ★★★ Research-oriented

**★★★8.** A 1-year time series is sampled hourly (8760 samples) and has an
estimated lag-1 autocorrelation of $\rho = 0.9$.

(a) Compute the naive standard error of the mean assuming independence, for
$\sigma = 1$.
(b) Compute the **effective sample size** using
$N_{\text{eff}} \approx N (1-\rho)/(1+\rho)$, and the corresponding standard
error.
(c) Compute the ratio of the two standard errors and state what it means for a
published uncertainty.
(d) State one estimator of the autocorrelation that would let you compute
$N_{\text{eff}}$ without assuming a particular correlation model.

---

**★★★9.** A bootstrap confidence interval is reported as
"$12.4 \pm 0.3$ mGal (1000 resamples)".

(a) State what the $\pm 0.3$ estimates and what it does **not** estimate.
(b) State the Monte Carlo standard error of the bootstrap interval itself, and
how many resamples are needed for it to be small relative to 0.3.
(c) Explain why the bootstrap fails for the maximum of a sample, and name the
remedy.
(d) State the one property of the underlying data that, if violated, makes the
bootstrap interval invalid, and give a geophysical example where it is violated.
