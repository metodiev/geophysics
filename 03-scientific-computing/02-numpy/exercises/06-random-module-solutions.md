# Solutions — 03-02-06 Random Number Generation and Reproducible Seeds

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values attributed to a verified calculation were
> produced with the project interpreter (NumPy 2.5.4, seed `20261014`).

---

## ★1 — One or two sentences

**(a)** A seed determines the *initial state* of the generator, and therefore the
entire sequence of values that will be drawn from it, in order. It does not
determine "the result" of a computation that consumes a variable number of draws.

**(b)** Because the program's sequence of draws depends on the *order and number*
of calls. If one version performs two extra draws early — a debug print, a
different array size, a plotting routine — every later draw is shifted.

**(c)** `np.random.default_rng(seed)`, which returns an independent `Generator`
object holding its own PCG64 state. It can be passed explicitly as a function
argument, which is what makes a function reproducible in isolation.

**(d)** PCG64 is a fast, well-tested pseudo-random generator with a period of
$2^{128}$, but it is deterministic: given the state, all future values are
computable. It must never be used for key material.

---

## ★2 — Error bars for a noise test

**(a)** $\sigma/\sqrt{N} = 3/\sqrt{2500} = 3/50 = 0.06$ nT.

**(b)** $\sigma/\sqrt{2N} = 3/\sqrt{5000} = 0.0424$ nT, i.e. 1.41 per cent of
$\sigma$.

**(c)** $| \bar{\epsilon} | < 4 \times 0.06 = 0.24$ nT. This is a *test*, not a
result: it will reject a correct implementation about 6 times in 100 000, which is
the intended false-positive rate.

**(d)** Because the mean of $N$ independent values has standard deviation
$\sigma/\sqrt{N}$, not $\sigma$. Comparing the mean against $\sigma$ would accept
essentially any draw and the test would be vacuous; it would also fail to detect a
systematic offset of, say, $0.2$ nT, which is 3.3 standard errors of the mean.

---

## ★3 — Poisson counting

**(a)** Mean $= \lambda = 9$; variance $= \lambda = 9$.

**(b)** Relative standard deviation $= \sqrt{\lambda}/\lambda = 1/\sqrt{\lambda} =
1/3 = 33$ per cent.

**(c)** To reach 1 per cent you need $M$ days with $1/\sqrt{M\lambda} = 0.01$, so
$M = 10^4/\lambda = 10^4/9 = 1111$ days.

**(d)** Earthquakes cluster: a mainshock is followed by aftershocks whose rate
decays (Omori's law), so counts are neither independent nor stationary. The
standard processing step is **declustering** — removing aftershocks and foreshocks
by a windowed rule or a stochastic model — before Poisson statistics are applied to
the remaining, roughly independent, mainshocks. Declustering is itself a modelling
choice with consequences for the hazard estimate.

---

## ★4 — Seeded draws

```python
rng = np.random.default_rng(7)                       # (a)
normal = rng.normal(size=1000)                       # (b)
uniform = rng.uniform(10.0, 20.0, size=1000)         # (c)
order = rng.permutation(1000)                        # (d)
resample = rng.choice(v, size=v.size, replace=True)  # (e)
```

Two notes. `rng.permutation(1000)` shuffles `np.arange(1000)`; for an array it
returns a shuffled copy. And the bootstrap in (e) draws `v.size` values *with
replacement*, which is what makes it a resample rather than a shuffle.

---

## ★5 — Reporting the demo

**(a)**

```
rng(20261014).normal(size=5)   = [-0.47093105  0.46182906 -0.81016369  1.86095921 -1.46163856]
rng(20261014).normal(size=5)   = [-0.47093105  0.46182906 -0.81016369  1.86095921 -1.46163856]
a.tobytes() == b.tobytes(): True
```

**(b)**

```
after seed(20261014): normal(3)              = [-2.49190959 -2.14783298  0.29810409]
after seed(20261014), uniform(2), normal(3)   = [ 0.29810409 -1.4027538  -0.2111473 ]
identical: False   <- they are not
```

**(c)** `nominal sigma       = 2.0 nT`,
`sample std (ddof=0) = 1.991922 nT`,
`expected std of the mean = sigma/sqrt(n) = 0.006325 nT`,
`observed |mean|          = 0.006197 nT`.

**(d)** `poisson(4): mean 3.991510 (nominal 4), var  4.011248 (nominal 4)`.

**(e)**

```
         N    observed std of mean     sigma/sqrt(N)     ratio
       100                0.288884          0.300000     0.963
     10000                0.030096          0.030000     1.003
   1000000                0.003145          0.003000     1.048
```

---

## ★★6 — Monte Carlo error

**(a)** $\sigma_{\bar{x}} = 0.15/\sqrt{2000} = 0.00335$ s.

**(b)** Halving the standard error requires four times the draws: 8000.

**(c)** Because the Monte Carlo error is the error in estimating an expectation
*by sampling*; it shrinks as more samples are drawn. The number of *observations*
(the data) controls the posterior width itself — the thing being estimated — not
the precision with which the estimation is done. Conflating the two is the
standard error of Monte Carlo studies: a very precise estimate of a poorly
constrained distribution.

**(d)** Report the **distribution**: for example a median with the 5th and 95th
percentiles, plus the number of draws. A mean of a skew distribution (travel-time
distributions from a velocity prior are commonly skew) is a poor summary, and the
Monte Carlo standard error of the mean does not describe the spread of the
distribution at all.

---

## ★★7 — Two defects in `make_noise`

**(a)** (i) It reseeds the **global** legacy state, so every other routine in the
program that uses `np.random` is affected, and *its* reproducibility now depends on
call order. (ii) Reseeding to the same value on every call means that two calls in
the same program return the **same** noise, which is silently correlated between
otherwise independent test cases.

**(b)**

```python
def make_noise(n, rng):
    """Return n standard normal deviates from an explicit, seeded Generator."""
    return rng.normal(size=n)

rng = np.random.default_rng(0)
a = make_noise(100, rng)
b = make_noise(100, rng)      # a and b are different draws
```

**(c)** "Used twice without correlation" means two successive calls must return
statistically independent values, which is what a single generator called
sequentially provides — the state advances between calls. If the function kept a
*module-level* generator and was called from two threads, the generator's state
would be advanced concurrently, which for NumPy's `Generator` is not
thread-safe: the draws become non-reproducible and the results depend on thread
scheduling. The remedy is one generator per thread (or per worker), each seeded
from a `SeedSequence.spawn()` child so that the substreams are independent *and*
reproducible:

```python
ss = np.random.SeedSequence(20261014)
children = ss.spawn(4)                     # one per thread
```

---

## ★★★8 — Correlated samples

**(a)** $\sigma/\sqrt{N} = 1/\sqrt{8760} = 0.01068$.

**(b)** $N_{\text{eff}} \approx N(1-\rho)/(1+\rho) = 8760 \times 0.1/1.9 =
461$. The standard error becomes $1/\sqrt{461} = 0.04658$.

**(c)** Ratio $= 0.04658 / 0.01068 = 4.36$. A published uncertainty computed from
the naive formula is **4.4× too small** — i.e. the confidence interval is 4.4× too
narrow, and a real effect could be declared significant on the strength of a
fluctuation that is well within the corrected uncertainty.

**(d)** Use the **sample autocorrelation function** $\hat{\rho}(k)$ estimated from
the series (via an FFT for speed) and form
$N_{\text{eff}} = N / \bigl(1 + 2\sum_{k=1}^{K}\hat{\rho}(k)\bigr)$ with $K$ chosen
at the first zero crossing or where the autocorrelation falls below the
$\pm 1.96/\sqrt{N}$ band. This makes no assumption about the shape of $\rho(k)$. The
alternative, when the data are long enough, is a block bootstrap, which resamples
blocks of consecutive samples and thereby preserves the correlation within a block.

---

## ★★★9 — Bootstrap intervals

**(a)** The $\pm 0.3$ estimates the **standard error of the statistic** (here the
mean) under resampling — it is a statement about the sampling variability of the
estimate. It does **not** estimate any systematic error: instrument calibration, an
incorrect velocity model, a datum offset or a biased station distribution all shift
the statistic without increasing the bootstrap spread.

**(b)** The Monte Carlo standard error of a bootstrap standard error estimated from
$B$ resamples is approximately $s/\sqrt{2B}$, where $s$ is the estimated standard
error: for $B = 1000$ and $s = 0.3$ this is $0.3/\sqrt{2000} = 0.0067$, i.e. 2.2
per cent of 0.3. To bring it below 1 per cent, $B > 5000$; $B = 10^4$ is the
conventional choice and costs a few seconds for any statistic that is cheap to
evaluate.

**(c)** The bootstrap fails for **extremes** (maximum, minimum, and quantiles near
the tail) because the resampled values are drawn from the observed sample, so the
bootstrap distribution of the maximum has support confined to the observed values
and can never exceed the largest one. Yet a *new* observation exceeds the observed
maximum with probability $1/(N+1)$ — for $N = 100$ that is about 1 per cent per
draw, which is not negligible — so the bootstrap interval is systematically too
narrow and shifted inward. The remedy is the $m$-out-of-$n$ bootstrap
(subsampling) or an extreme-value (generalised Pareto) fit to the tail.

**(d)** The property is **exchangeability** — in the simplest case, that the
observations are independent and identically distributed. The block bootstrap
relaxes it to weak dependence within a block. A geophysical example where the
plain bootstrap is invalid is a spatially correlated gravity grid: resampling
individual stations destroys the spatial correlation, so the resampled fields have
far less variability than the real data and the interval is too narrow.
