---
id: 03-02-06
title: "Random Number Generation and Reproducible Seeds"
level: intermediate
prereqs: ["03-02-04"]
estimated_minutes: 75
tags: [numpy, random, reproducibility, monte-carlo, uncertainty]
---

# Random Number Generation and Reproducible Seeds

Random numbers appear in geophysics for three quite different reasons, and
conflating them causes real damage. They are used **to simulate noise** (add an
instrument-like error to a synthetic test), **to sample an uncertainty** (draw
$10^4$ realisations of a model consistent with the data), and **to search a space**
(bootstrap resampling, simulated annealing, stochastic gradient). In the first
two the randomness is *not* the point — the point is the error distribution or
the posterior — and the numerical result should be reproducible exactly. In the
third the randomness is also not the point, but the answer is a statistical
statement that must be reported with its sampling variability.

NumPy's modern answer to all three is `np.random.default_rng`, which returns an
independent `Generator` object holding its own state. The legacy module-level
`np.random.*` functions share a single global state and are kept only for
compatibility with old code. This lesson covers the rule that makes results
reproducible (seed the generator, and pass it explicitly), the one that makes
them irreproducible (any dependence on the global state's call order), and the
statistical hygiene that lets you claim a result is "the same" as another when
the underlying draw is different.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** what a seed does and does not determine: it fixes a *sequence*,
   not a *result*.
2. **Produce** bit-identical output from two generators given the same seed, and
   **demonstrate** that different seeds give different output.
3. **Explain** why the legacy global API makes results depend on call order, and
   **migrate** code that depends on it.
4. **Generate** Gaussian noise for a synthetic test and **compare** the measured
   moments with the nominal values, including the standard error of the mean.
5. **Draw** from uniform, Poisson, and discrete distributions, and **check** each
   sample against its analytic moments.
6. **Measure** the $1/\sqrt{N}$ convergence of the sample mean and use it to size
   a synthetic experiment.
7. **State** the assumptions behind a Poisson or Gaussian draw and explain what
   breaks when they are violated by real data.

## Prerequisites

- [03-02-04 Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md)
  — the moments are reductions over an axis.
- [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md)
  — the distributions being sampled (recommended).

## 1. Seeds, states and sequences

A pseudo-random generator is a deterministic machine with an internal state. Each
call advances the state and returns a value that is a function of the state
alone. A seed is the initial state. Therefore:

- **The same seed reproduces the entire sequence**, in the same order.
- **The same seed does not reproduce "the same result" of a different program.**
  If your program consumes two extra numbers early — a plotting routine, a debug
  print, a differently sized array — every subsequent draw has shifted.

The demo:

```
rng(20261014).normal(size=5)   = [-0.47093105  0.46182906 -0.81016369  1.86095921 -1.46163856]
rng(20261014).normal(size=5)   = [-0.47093105  0.46182906 -0.81016369  1.86095921 -1.46163856]
rng(20261015).normal(size=5) = [ 0.46817796 -1.15220841 -1.7058637  -0.59049913 -0.0402362 ]
a and b are identical     : True
a and c differ            : True
a.tobytes() == b.tobytes(): True
```

and the statement that the draw is a *stream*:

```
splitting one stream two ways: normal(2)+normal(1) == normal(3): True
```

Two calls of `normal(2)` and `normal(1)` from a fresh generator produce exactly
the same three numbers as one call of `normal(3)`, because the underlying stream
is a sequence of random values that the shape argument merely re-partitions. This
is worth internalising: **changing the shape of a draw to a power-of-two
subdivision leaves the values unchanged; changing the order in which different
distributions are called does not.**

`a.tobytes() == b.tobytes()` is *True*: the reproducibility is exact, bit for bit,
not merely close. There is no floating-point ambiguity, because the same
algorithm produced the same bits.

## 2. The legacy global API, and why it is a reproducibility hazard

```
after seed(20261014): normal(3)              = [-2.49190959 -2.14783298  0.29810409]
after seed(20261014), uniform(2), normal(3)   = [ 0.29810409 -1.4027538  -0.2111473 ]
identical: False   <- they are not
```

Re-seeding and then drawing two uniform numbers *before* the three normals
changes the three normals: the first draw consumed state, so the later draw
starts at a different point in the sequence. This is the essence of the problem
with `np.random.seed`: the state is global, so any function anywhere in the
program can move it. Adding a diagnostic plot that draws two numbers silently
invalidates every downstream result.

`np.random.default_rng(seed)` fixes this by making the state local:

```python
def add_noise(traces, sigma, rng):
    return traces + rng.normal(0.0, sigma, size=traces.shape)

rng = np.random.default_rng(20261014)
a = add_noise(traces, 2.0, rng)
b = add_noise(traces, 2.0, np.random.default_rng(20261014))   # a == b
```

The generator is an *argument*, so the function's behaviour depends only on what
was passed to it. This is the only pattern under which a pipeline is
reproducible without global state.

Migrating legacy code is usually mechanical: replace `np.random.seed(s)` with
`rng = np.random.default_rng(s)` and `np.random.normal(...)` with
`rng.normal(...)`. The values change — the legacy `RandomState` and the modern
`Generator` use different algorithms — so any test that pins the exact numbers
must have its expected values regenerated. That is a feature, not a nuisance: it
forces the values into the test file rather than leaving them implicit.

## 3. Synthetic noise for a test

The canonical use. The demo draws $10^5$ samples at a nominal 2 nT:

```
nominal sigma       = 2.0 nT
sample mean         = -0.006197 nT
sample std (ddof=0) = 1.991922 nT
sample std (ddof=1) = 1.991932 nT
expected std of the mean = sigma/sqrt(n) = 0.006325 nT
observed |mean|          = 0.006197 nT
skewness (g1)       = -0.015579
excess kurtosis     = -0.023069
```

Four checks are packed into that block.

**The sample standard deviation is not the nominal one.** $1.9919$ against $2.0$
is a 0.4 per cent low, entirely consistent: the standard error of a sample
standard deviation is about $\sigma/\sqrt{2N} = 2/\sqrt{2 \times 10^5} = 0.45$ per
cent. Quoting "σ = 2.0000" from a finite sample would be an overclaim.

**The `ddof` difference is a systematic factor, not noise.** `np.std` defaults to
`ddof=0`; many texts and most statistics packages quote `ddof=1`. The factor is
$n/(n-1)$, which is $1 + 10^{-5}$ here — invisible at $10^5$ samples, and a
0.5 per cent discrepancy at $N = 200$. State the convention.

**The mean's standard error is the right scale for the mean.** $\sigma/\sqrt{N} =
0.006325$ nT and the observed mean is $0.006197$ nT — a $0.98\sigma$ fluctuation.
Testing "the mean is 0" against the right scale is the check; testing it against
$\sigma$ itself would be wrong by a factor of $\sqrt{N} = 316$.

**Higher moments are consistent with Gaussianity at this $N$.** For a Gaussian
sample the standard errors are $\sqrt{6/N}$ for the skewness ($0.0077$ here) and
$\sqrt{24/N}$ for the excess kurtosis ($0.0155$). The observed $-0.0156$ and
$-0.0231$ are about 2σ and 1.5σ from zero — ordinary, but a reminder that
normality tests need large samples to say anything.

The pattern to adopt for a synthetic test is:

```python
rng = np.random.default_rng(20261014)
noise = rng.normal(0.0, sigma, size=traces.shape)
assert abs(noise.mean()) < 4 * sigma / np.sqrt(noise.size)
assert abs(noise.std() - sigma) < 4 * sigma / np.sqrt(2 * noise.size)
```

with the seed *in the test*, not in a module-level constant shared across tests.

## 4. Distributions and their moments

```
uniform   : mean 0.499091 (nominal 0.5), std 0.288844 (nominal 0.288675)
poisson(4): mean 3.991510 (nominal 4), var  4.011248 (nominal 4)
choice    : frequencies = [0.10086 0.100855 0.10158 ...]  (nominal 0.1 each)
permutation of 0..51 is a permutation: True
first 10 of the shuffled order: [45 18 51 48 22 15 44 23  8  6]
```

Each of these answers a different modelling question:

- **`uniform(low, high)`** is the only distribution that is genuinely
  assumption-free on an interval. It is used for a *prior* with no information
  beyond bounds, and for randomising a search. Its standard deviation is
  $(b-a)/\sqrt{12}$, which the demo confirms: $1/\sqrt{12} = 0.288675$ against a
  measured $0.288844$.
- **`normal(loc, scale)`** is the noise model for a measurement that is a sum of
  many small independent errors. Its tails are thin — a real magnetometer has
  occasional spikes that a Gaussian will never produce, which is why robust
  processing uses Huber or $L_1$ norms (lesson [08](./08-vectorisation-patterns.md)).
- **`poisson(lam)`** counts events in a fixed interval when they occur
  independently at a constant rate. Mean and variance are both $\lambda$, and the
  demo's measured $3.9915$ and $4.0112$ confirm it. Global seismicity violates
  both assumptions (aftershocks are dependent; rates vary), so `poisson` is
  appropriate for a *declustered* catalogue or for a detector's counting
  statistics, and must be labelled as such when used.
- **`choice` and `permutation`** are the discrete tools: bootstrap resampling,
  randomising trace order, splitting into folds. `permutation` guarantees a
  bijection; `choice(..., replace=False)` is the same thing expressed differently.

## 5. The $1/\sqrt{N}$ law, measured

```
         N    observed std of mean     sigma/sqrt(N)     ratio
       100                0.288884          0.300000     0.963
     10000                0.030096          0.030000     1.003
   1000000                0.003145          0.003000     1.048
```

with $\sigma = 3$ and 400 repetitions per row. The observed spread of the mean
matches $\sigma/\sqrt{N}$ to within the sampling error of 400 repetitions itself
(about 3.5 per cent), and the ratios are 0.963, 1.003 and 1.048 — consistent with
1 and not with anything else.

Two practical consequences:

- **To characterise a noise level to 1 per cent you need about $10^4$ samples**,
  because the relative standard error of a mean is $1/\sqrt{N}$ and $1/\sqrt{10^4}
  = 0.01$. This is the arithmetic behind survey design: more averaging is
  expensive, and its benefit is square-root.
- **Quoting more decimals than the sampling error supports is a misrepresentation.**
  A Monte Carlo mean reported as "2.41378 mGal" from 100 realisations has an
  uncertainty of about 0.3 mGal; the last four digits are noise.

## 6. Physical interpretation

Randomness in geophysics enters in two ways, and naming them separately is useful.

**Randomness as a model of ignorance.** The instrument noise, the unknown
site condition, the heterogeneity below the resolution of the model: these are
real physical variations that are treated as random because they are
unresolvable, not because they are unknowable in principle. A Gaussian noise
model is a claim that the sum of many small unresolved effects is approximately
Gaussian — usually defensible, occasionally not.

**Randomness as an estimator.** Bootstrap resampling treats the observed sample
as a stand-in for the population; permutation tests ask whether a statistic is
larger than chance under the null hypothesis. Here randomness has no physical
claim at all; it is a computational device for estimating a distribution.

A result from the first kind is a statement about the Earth and must be reported
with the noise model. A result from the second kind is a statement about the
data and must be reported with the number of resamples and the resampling scheme.
Confusing them — reporting a bootstrap confidence interval as if it were a
physical uncertainty, or vice versa — is a common and serious error.

## 7. Assumptions and regime of validity

- **Pseudo-randomness is deterministic and periodic.** `default_rng` uses the
  PCG64 generator, whose period is $2^{128}$ — far beyond any computational
  budget — and it is not cryptographically secure. Never use it for keys or
  passwords.
- **"Statistically independent" is an approximation.** Successive values from
  PCG64 pass standard test batteries; a *bad* generator's correlation shows up as
  subtle bias in Monte Carlo results. Do not implement your own generator.
- **A seed fixes a sequence, not a result.** Any change upstream in the number or
  order of draws changes everything downstream. Record the seed *and* the
  version of NumPy, because the algorithm is not guaranteed to be bit-identical
  across major versions.
- **`np.random.default_rng` and `np.random.seed` produce different numbers** for
  the same seed. Never mix them, and never assume a result transfers between
  them.
- **Gaussian tails are not real.** A Gaussian draw can produce a 5σ outlier with
  probability $3 \times 10^{-7}$ per sample; a real instrument produces outliers
  far more often, and often asymmetrically (`lognormal` is the common model for
  amplitude).
- **The standard error formulas assume independence.** Correlated samples — a
  time series, a spatially smooth field — have an effective sample size far below
  $N$, and a naive $\sigma/\sqrt{N}$ understates the uncertainty by a large
  factor. This is the single most common statistical error in geophysics.
- **`rng.poisson` and `rng.normal` are not interchangeable in the tails.** For
  large $\lambda$, Poisson converges to Gaussian, but its *variance equals its
  mean*, so a counting channel with $\lambda = 4$ has a 50 per cent relative
  standard deviation — a property that no amount of scaling removes.
- **`choice(replace=False)` on a large array** is an $O(n)$ partial shuffle;
  `permutation` is the clearer tool when a full shuffle is wanted.

## 8. Python demonstration

The script is [`code/random_demo.py`](./code/random_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/random_demo.py
```

Everything generated is SYNTHETIC. The seed is `SEED = 20261014`, printed in the
script header, so every value below is reproducible exactly on any machine with
the same NumPy version; no dataset is read.

Key output (this machine, NumPy 2.5.4):

```
rng(20261014).normal(size=5)   = [-0.47093105  0.46182906 -0.81016369  1.86095921 -1.46163856]
rng(20261014).normal(size=5)   = [-0.47093105  0.46182906 -0.81016369  1.86095921 -1.46163856]
a.tobytes() == b.tobytes(): True
splitting one stream two ways: normal(2)+normal(1) == normal(3): True
```

```
after seed(20261014): normal(3)              = [-2.49190959 -2.14783298  0.29810409]
after seed(20261014), uniform(2), normal(3)   = [ 0.29810409 -1.4027538  -0.2111473 ]
identical: False   <- they are not
```

```
nominal sigma       = 2.0 nT
sample std (ddof=0) = 1.991922 nT
expected std of the mean = sigma/sqrt(n) = 0.006325 nT
observed |mean|          = 0.006197 nT
skewness (g1)       = -0.015579
excess kurtosis     = -0.023069
```

```
poisson(4): mean 3.991510 (nominal 4), var  4.011248 (nominal 4)
```

```
         N    observed std of mean     sigma/sqrt(N)     ratio
       100                0.288884          0.300000     0.963
     10000                0.030096          0.030000     1.003
   1000000                0.003145          0.003000     1.048
```

### What to observe

1. The two same-seed arrays are identical bit for bit (`tobytes()` equality), so
   the claim "reproducible" is stronger than "close".
2. The legacy block is the cautionary tale: the same seed, one extra draw, a
   completely different `normal(3)`. Nothing in the output flags the difference.
3. `observed |mean| = 0.006197` against `expected = 0.006325` is a $0.98\sigma$
   agreement — the correct way to check a mean is to compare it with its own
   standard error, not with the sample standard deviation.
4. The Poisson mean and variance agree with each other to 0.5 per cent, which is
   the defining property of the distribution and the check that the sampling is
   right.
5. The three `ratio` entries bracket 1 and their scatter is consistent with the
   400 repetitions used; the $1/\sqrt{N}$ law is verified as a scaling, not as an
   equality.

## 9. Common mistakes

1. **Calling `np.random.seed` inside a function.** Any caller can move the global
   state; the function is no longer reproducible in isolation.
2. **Seeding once and running experiments in sequence.** The second experiment's
   draws depend on how many numbers the first consumed.
3. **Using `np.random.rand` and `rng.random` interchangeably.** Different
   algorithms and different conventions: `rand(d0, d1)` takes dimensions, `random`
   takes a `size` tuple.
4. **Comparing a mean against $\sigma$ instead of $\sigma/\sqrt{N}$.** Off by
   $\sqrt{N}$.
5. **Reporting a sample standard deviation as if it were the population value.**
   Include the standard error.
6. **Assuming independence for a spatially or temporally correlated series.** The
   effective $N$ can be orders of magnitude smaller.
7. **Treating a Poisson noise model as Gaussian at small counts.** At
   $\lambda = 4$ the relative error is 50 per cent.
8. **Forgetting `ddof=1` where the sample variance is required**, or the reverse
   in a test written against `np.std`'s default.
9. **Checking reproducibility with `np.allclose`.** Use exact equality of bytes or
   values; "close" hides the call-order dependence you were trying to exclude.
10. **Putting the seed in the code but not in the report.** A result that depends
    on a seed must state the seed; otherwise it is not reproducible even in
    principle.

## 10. Real-world applications

- **Synthetic seismograms.** Adding seeded noise to a synthetic trace, then
  processing with the same pipeline as real data, is how a processing step is
  validated. The seed makes the test deterministic; the noise model is stated
  separately.
- **Monte Carlo uncertainty propagation.** Drawing $10^4$ velocity models from a
  prior, forward-modelling each, and reporting the distribution of predicted
  travel times; the number of draws and the sampler are part of the result.
- **Bootstrap confidence intervals.** Resampling a catalogue or a set of station
  measurements with replacement to estimate the standard error of a statistic
  whose analytic distribution is unknown.
- **Seismic hazard.** Ground-motion simulation uses random source and path
  parameters, and hazard curves are reported as the mean over many realisations
  with a stated number of samples.
- **Declustered catalogues.** Poisson process models of earthquake occurrence
  require a declustering step first; the residual dependence after declustering
  is itself a research question.
- **Machine learning.** Batch order, weight initialisation and augmentation all
  draw random numbers; a model reported without a seed is not reproducible, and
  the seed belongs in the configuration file.

## 11. Further reading

- **NumPy documentation, "Random sampling" and "Parallel random number
  generation".** [https://numpy.org](https://numpy.org) — the
  `Generator`/`BitGenerator` design, the `default_rng` entry point, and the list
  of distributions. Level: beginner to intermediate.
- **O'Neill, M. E. *PCG: A Family of Simple Fast Space-Efficient Statistically
  Good Algorithms for Random Number Generation* (Harvey Mudd College technical
  report HMC-CS-2014-0905, 2014).** The generator behind NumPy's default
  `PCG64`. Level: advanced.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P.
  *Numerical Recipes* (3rd ed., Cambridge University Press, 2007).** Chapter 7
  on random numbers, including the cautionary examples of bad generators and the
  discussion of deviates from non-uniform distributions. Level: advanced.
- **Efron, B., & Tibshirani, R. J. *An Introduction to the Bootstrap* (Chapman &
  Hall, 1993).** The reference for resampling, including the block bootstrap for
  dependent data. Level: graduate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and
  Inverse Problems* (2nd ed., Academic Press, 2018).** Monte Carlo and bootstrap
  uncertainty estimation in the geophysical setting. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04 Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md)
  — the moment calculations used throughout.
- [05 Linear Algebra with numpy.linalg](./05-linear-algebra-numpy.md) — the
  synthetic profile whose noise this lesson generates.
- [08 Replacing Loops: Vectorisation Patterns and Traps](./08-vectorisation-patterns.md)
  — resampling arrays without Python loops.
- [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md)
  — the distributions and the theory of estimation.
- [21-statistics-bayesian-ml/…](../../21-statistics-bayesian-ml/README.md) — the
  Bayesian and machine-learning uses of randomness.
- [22-data-engineering-reproducibility/…](../../22-data-engineering-reproducibility/README.md)
  — seeds, versions and configuration as part of reproducibility.

Exercises:
[`exercises/06-random-module-exercises.md`](./exercises/06-random-module-exercises.md)
and
[`exercises/06-random-module-solutions.md`](./exercises/06-random-module-solutions.md).

## Self-assessment checklist

- [ ] I can explain why the same seed does not guarantee the same result in two
      different programs. (§1)
- [ ] I can demonstrate a case where a legacy global draw changes a later result.
      (§2)
- [ ] I can write a seeded noise generator that takes the `Generator` as an
      argument. (§2, §3)
- [ ] I can state the standard error of the mean and use it as the right
      tolerance for a synthetic test. (§3)
- [ ] I can choose between Gaussian and Poisson for a counting measurement and
      justify the choice. (§4)
- [ ] I can state the $1/\sqrt{N}$ law and use it to size an experiment. (§5)
- [ ] I can distinguish "randomness as ignorance" from "randomness as estimator"
      and say which kind of statement each produces. (§6)
- [ ] I can name the assumption whose violation invalidates a $\sigma/\sqrt{N}$
      error bar. (§7)
