---
id: 20-07-02
title: "Compressive Sensing and Data Reconstruction"
level: research
prereqs: ["20-07-01", "20-01-05", "20-02-01"]
tags: [signal-processing, time-series, compressive-sensing, sampling, sparsity, reconstruction]
---

# Compressive Sensing and Data Reconstruction

**All models and data in this module are SYNTHETIC.** The signal is a chosen
sparse spectrum on a chosen grid, sampled at chosen times with seeded noise. No
field data, no acquisition geometry and no published number is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Nyquist limit as a statement about a *basis* — a signal is
   only band-limited once you have chosen a basis — and **state** why a sparse
   signal can evade it.
2. **Compute** the mutual coherence of a sensing matrix and **explain** why
   coherence, not sample count alone, governs recoverability.
3. **Demonstrate** that uniform subsampling admits an entire alias set that
   explains the data exactly, and that random subsampling does not.
4. **Implement** sparse recovery (FISTA with debiasing) and **measure** the
   empirical phase transition in the number of samples.
5. **Estimate** restricted eigenvalues on a known support and **interpret** them
   as the empirical version of the restricted isometry property.
6. **State** the sampling theorems' constants as problem-dependent and
   **identify** the assumptions that a real acquisition would violate.
7. **Predict** whether a given undersampling scheme can succeed, before running
   any algorithm, from the coherence of its columns.

## Prerequisites

- [20-07-01 Sparse and L1 Deconvolution](01-sparse-deconvolution.md) — the L1
  prior, soft thresholding and ISTA/FISTA.
- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md)
  — aliasing and the sampling theorem in its classical form.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md)
  — the discrete frequency grid and its bins.

The runnable companion is
[`code/compressive_sensing_demo.py`](code/compressive_sensing_demo.py); the
graded problems are in
[`exercises/02-compressive-sensing-signals-exercises.md`](exercises/02-compressive-sensing-signals-exercises.md).

## 1. The claim, stated precisely

The classical sampling theorem says that a signal whose spectrum vanishes above
$f_{\max}$ is determined by samples spaced $\Delta t \le 1/(2 f_{\max})$. The
compressive-sensing claim is different and narrower: if a signal has at most $k$
nonzero coefficients in a **known** dictionary, and if the sampling is
**incoherent** with that dictionary, then roughly
$m \sim k \log(n/k)$ samples suffice, where $n$ is the ambient dimension. Two
words in that sentence carry all the risk — *known* and *incoherent* — and this
lesson measures both.

Write the sensing problem as

$$
y = A x + \eta, \qquad A = S D, \qquad S \in \{0,1\}^{m \times n},
$$

where $D$ is the dictionary (here a real Fourier basis), $S$ is the sampling
mask, $x$ is the sparse coefficient vector and $y$ are the $m$ recorded samples.
The reconstruction is

$$
\hat{x} = \arg\min_{x}\ \tfrac{1}{2}\lVert A x - y \rVert_2^{2}
+ \lambda \lVert x \rVert_1 ,
$$

which is the problem of the previous lesson with a different operator. The
demonstration uses $n = 128$ samples and a 128-column orthonormal real Fourier
dictionary whose measured coherence is $7.6\times10^{-15}$, i.e. numerically
zero as an orthonormal basis requires.

## 2. Coherence: why the sampling pattern, not just the count, decides

For a matrix $A$ with unit-norm columns $a_j$, the **mutual coherence** is

$$
\mu(A) = \max_{i \neq j} \frac{\lvert a_i^{T} a_j \rvert}{\lVert a_i \rVert_2 \lVert a_j \rVert_2}.
$$

$\mu$ is a measure of how much two columns of the sensing matrix look alike after
sampling. Two columns with $\mu = 1$ are *identical*: no algorithm can tell them
apart, and no amount of sparsity helps. The demonstration keeps
$m = 32$ samples out of $n = 128$ and compares two masks:

| sampling | coherence of $A$ |
|---|---|
| uniform, stride 4 | **1.000** |
| random, 32 of 128 | **0.528** |

This is the whole mechanism in one line. Stride-4 sampling of a Fourier
dictionary creates exact aliases: a column at frequency $f$ and a column at
$f \pm 1/4$ produce identical sampled vectors. Random sampling keeps the columns
distinct, at the cost of raising the minimum number of samples needed for a
guarantee — and that cost is small compared with not being able to recover at
all.

## 3. Aliasing as a null space, measured

Take a synthetic unit-amplitude tone at $f = 0.3125$ cycles/sample, which is
bin 40 of the 128-point grid, exactly on the grid. For every dictionary column
$j$, fit one scalar by least squares to the sampled data and record the residual.
The frequencies whose residual is below $10^{-8}$ are those the data cannot
distinguish:

| sampling | bins with exact fit | frequencies (cycles/sample) |
|---|---|---|
| uniform stride 4 | 8, 24, 40, 56 | 0.0625, 0.1875, 0.3125, 0.4375 |
| random (32 of 128) | 40 | 0.3125 |

Stride-4 sampling admits **four** exact explanations of the same 32 numbers. The
true frequency is one of them; nothing in the data says which. This is the null
space of the sensing operator, in the only form a practitioner ever sees it.

The L1 reconstruction makes the consequence concrete. With coefficients
debiased (the L1 solution followed by unpenalised least squares on its support),
the recovered amplitudes are:

| sampling | largest coefficients |
|---|---|
| uniform stride 4 | bin 40 amp $+0.691$; bin 8 amp $+0.404$; bin 56 amp $-0.199$ |
| random | bin 40 amp $+1.000$; all other bins $0.000$ |

Both reconstructions fit the samples. Only the random one is the tone. The
uniform one spreads the amplitude over the alias set exactly as the null space
predicts, and a reader who only looked at "the largest peak" would read bin 40
and be right — for the wrong reason, since bin 8 is a defensible answer from the
data alone. **The honest statement is about the design, not the output.**

## 4. The phase transition, measured

The demonstration draws a $k$-sparse coefficient vector with random support and
random amplitudes, samples $m$ of the 128 grid points at random, and measures the
relative coefficient error after debiasing. The median over five draws is either
essentially zero or of order 1; there is no useful middle ground:

| $k \backslash m$ | 16 | 24 | 32 | 40 | 48 | 64 | 80 |
|---|---|---|---|---|---|---|---|
| 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 4 | 0.913 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 5 | 0.625 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 6 | 1.091 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

"0.000" is a median, not a guarantee: it means more than half the draws were
exact. Success counts over three independent trials show the edge of the
transition and are the more honest summary:

| $k \backslash m$ | 16 | 24 | 32 | 40 | 48 | 64 | 80 |
|---|---|---|---|---|---|---|---|
| 1 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| 2 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| 3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| 4 | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| 6 | 0/3 | 1/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| 8 | 0/3 | 0/3 | 1/3 | 3/3 | 3/3 | 3/3 | 3/3 |

The smallest $m$ with 3/3 exact recovery, and the two scalings often quoted for
it:

| $k$ | smallest $m$ | $m/k$ | $k\log(n/k)$ |
|---|---|---|---|
| 1 | 16 | 16.0 | 4.9 |
| 2 | 16 | 8.0 | 8.3 |
| 3 | 16 | 5.3 | 11.3 |
| 4 | 24 | 6.0 | 13.9 |
| 6 | 32 | 5.3 | 18.4 |
| 8 | 40 | 5.0 | 22.2 |

The observed $m/k$ falls from 16 to 5 as $k$ grows, and every $m$ is far below
$n = 128$. Both are consistent with $m \propto k\log(n/k)$, and neither
*establishes* it: the constant depends on the coherence of $A$, the sampling
pattern, and the success tolerance. Quoting $m = C k\log(n/k)$ with a number for
$C$ that was not measured is the commonest overclaim in the applied
compressive-sensing literature, and the table above is what a defensible version
looks like.

### 4.1 Worked example: what $m/k = 5$ buys

With $k = 8$ and $m = 40$, the demonstration recovers the sparse spectrum
exactly in 3 of 3 trials. Classical sampling would need $m = 128$ samples for a
signal band-limited to the grid; the reduction here is a factor
$128/40 = 3.2$. It is paid for in three ways: the recovery is exact *only*
because the signal really is $k$-sparse in this dictionary, the sampling must be
random rather than uniform, and the algorithm is nonlinear and must be run per
record. If any one of the three fails, the factor disappears.

## 5. The empirical restricted isometry property

The guarantee machinery is the **restricted isometry property**: for every
support $T$ with $\lvert T \rvert \le k$, the restricted Gram $A_T^{T} A_T$ must
have all eigenvalues within $[1-\delta_k, 1+\delta_k]$ with $\delta_k$ small. A
zero restricted eigenvalue means the support is invisible to the sampling, and
then *no* algorithm can recover it. The demonstration estimates the extremes
over ten random supports with $m = 4k$ samples:

| $k$ | $m$ | mean min eigenvalue | mean max eigenvalue |
|---|---|---|---|
| 2 | 12 | 0.0760 | 0.1246 |
| 4 | 16 | 0.0596 | 0.2014 |
| 6 | 24 | 0.0925 | 0.3178 |
| 8 | 32 | 0.0953 | 0.4157 |

The eigenvalues are *not* close to 1, and the reason is a normalisation artefact
rather than a failure: the Fourier dictionary's columns have unit norm in the
full space, so restricting to $m$ of $n$ rows scales every Gram entry by about
$m/n$. For $k = 2$, $m/n = 12/128 = 0.094$, and the observed range
$0.0760$–$0.1246$ straddles it, as expected. What matters for identifiability is
that the eigenvalues remain bounded away from zero, so that the map from the $k$
coefficients to the $m$ data is invertible on that support; a restricted
eigenvalue of exactly 0 would mean the support is invisible to the sampling, and
then *no* algorithm can recover it. This diagnostic is a property of the design
alone and can be computed before any recovery algorithm is run.

### 5.1 A sufficient condition, and how conservative it is

The coherence of $A$ also gives a certificate that needs no computation. Suppose
$A h = 0$ for a vector $h$ with $s$ nonzero entries and unit-norm columns
$a_j$. Let $i$ index the largest entry. Then $a_i^{T}(Ah) = 0$ gives

$$
h_i = -\sum_{j \neq i} h_j \left(a_i^{T}a_j\right),
\qquad\text{so}\qquad
\lvert h_i \rvert \le \mu \sum_{j \neq i}\lvert h_j \rvert
\le \mu\,(s - 1)\,\lvert h_i \rvert .
$$

If $\mu(s-1) < 1$ this forces $h_i = 0$, contradicting the choice of $i$: no such
$h$ exists. Two $k$-sparse coefficient vectors giving the same data would imply a
$2k$-sparse null vector, so **any $k$-sparse solution is unique** whenever

$$
2k - 1 < \frac{1}{\mu}
\qquad\Longleftrightarrow\qquad
k < \frac{1}{2}\left(1 + \frac{1}{\mu}\right).
$$

With the measured $\mu = 0.528$ for the random 32-of-128 mask this is
$k < \tfrac{1}{2}(1 + 1.894) = 1.447$, i.e. the certificate covers $k = 1$ and
nothing else.

The measurement says more. In §4 the phase-transition table shows $k = 1, 2$ and
$3$ all recovering exactly in 3 of 3 trials at $m = 16$ — the smallest grid
value — so the sufficient condition is conservative here by about a factor of 3
in $k$. Two reasons, both worth stating whenever a bound like this is quoted:

- It is a **worst-case** statement: it must hold for every $k$-sparse signal and
  every support, including the least favourable one. A particular signal with a
  favourable support does better.
- It uses only the single number $\mu$ and discards the structure of the
  dictionary (here, the alias classes of §3) and of the sampling pattern. A
  bound built on more of the design would be tighter.

The practical reading: a coherence bound tells you when recovery is *certified*,
never when it is *possible*. Failure of the condition is not evidence of failure
of the method, and the phase transition has to be measured.

## 6. Assumptions and regime of validity

1. **The signal is exactly $k$-sparse in the chosen dictionary** — not
   approximately, not "mostly". A signal that is merely compressible (sparse
   after a small tail) degrades gracefully in a way that this demonstration does
   not measure, and the degradation is not quantified by the tables above.
2. **The dictionary is known before the experiment.** Choosing the dictionary
   after seeing the data, and reporting the sparsity of the result, is fitting
   the prior to the test. The next lesson measures how much a dictionary choice
   is worth.
3. **The sampling is incoherent with the dictionary and the pattern is random.**
   Coherence 0.528 in §2 is not a threshold; it is one measured value for one
   pattern. Nothing here says that any particular \(m\) works for any particular
   mask.
4. **The measurements are noiseless.** Every number in §4 and §5 comes from
   clean data with debiasing. Real data have noise, and the recovery threshold
   becomes a function of the signal-to-noise ratio as well as $k$ and $m$.
5. **The grid is finite and the frequencies are on it.** A tone between grid
   points is not $k$-sparse on the grid; it is dense, and the whole construction
   fails. This is why practical implementations use an oversampled (redundant)
   dictionary, which raises $\mu$ and partially undoes the benefit.
6. **The phase transition is empirical.** It was measured on one generator, one
   dictionary size and three trials per cell. It is a teaching measurement, not
   a calibration of any field system.

## Mastery checkpoint

Without notes: **(a)** state the compressive-sensing problem and define mutual
coherence; **(b)** explain, using the alias table of §3, why uniform stride-4
sampling cannot recover one tone from 32 samples while random sampling can;
**(c)** for $k = 4$ and $m = 16$, read the measured success count and state the
recovery probability with its uncertainty; **(d)** explain what the restricted
eigenvalue on the support has to do with identifiability, and why it can be
checked without running an algorithm; **(e)** name two assumptions of §6 that a
real seismic acquisition would break, and say what the failure would look like
in the reconstruction.

A worked answer to (a)–(c) appears in the
[solutions](exercises/02-compressive-sensing-signals-solutions.md).

## Common pitfalls

1. **Reading the largest peak as the answer.** In §3 the uniform reconstruction
   gets the true bin right while bin 8 carries twice the amplitude of bin 56;
   the ambiguity, not the winner, is the result.
2. **Quoting $m = C k \log(n/k)$ with a borrowed $C$.** $C$ is
   dictionary-, mask- and tolerance-dependent; measure it or omit it.
3. **Treating coherence as a boolean.** $\mu = 1.000$ is a hard failure;
   $\mu = 0.528$ is a measured value for one design. Nothing in between is
   automatically safe.
4. **Forgetting that the sparsity claim is a model claim.** A "sparse
   reconstruction" of a signal that is not sparse will look sparse, because the
   penalty says so.
5. **Comparing $m$ values without fixing the success criterion.** "Recovery"
   at a $10^{-1}$ tolerance and at a $10^{-6}$ tolerance are different
   experiments; the demonstration's threshold is $10^{-6}$ relative error.
6. **Skipping the debiasing step.** Raw soft-thresholded coefficients are
   shrunk; the errors of §4 would be order $10^{-2}$ rather than $10^{-16}$, and
   the phase transition would be a smooth blur instead of an edge.

## Related modules

- [20-07-01 Sparse and L1 Deconvolution](01-sparse-deconvolution.md) — the
  proximal algorithm used here, and the shrinkage bias it produces.
- [20-07-03 Sparse Representations for Seismic Data](03-sparsity-seismic.md) —
  what happens when the dictionary is redundant and coherence is large.
- [20-01-05 Sampling, Nyquist and Reconstruction](../01-signals-and-systems/05-sampling-theory.md)
  — the classical theorem this lesson is an exception to, and the aliasing it
  describes.
- [18-03-04 Sparsity](../../18-inverse-problems/03-regularization/04-sparsity.md)
  — recovery guarantees stated in the language of inverse theory rather than
  engineering.
