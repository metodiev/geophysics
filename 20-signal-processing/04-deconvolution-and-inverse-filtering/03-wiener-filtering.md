---
id: 20-04-03
title: "Wiener Filtering and Least-Squares Inverse Filters"
level: research
prereqs: ["20-04-01", "20-05-02"]
tags: [signal-processing, deconvolution, wiener-filter, least-squares, normal-equations, matched-filter, toeplitz, orthogonality]
---

# Wiener Filtering and Least-Squares Inverse Filters

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Wiener-Hopf normal equations from the mean squared error and
   **state** the orthogonality condition they encode.
2. **Solve** the normal equations with a Toeplitz solver and **choose** the design
   delay that makes the filter causal.
3. **Verify** optimality by measuring the cross-correlation between the error and
   the input.
4. **Measure** the recovered-reflectivity SNR as a function of filter length, and
   **state** where the gains stop.
5. **Contrast** the Wiener filter, the matched filter and the naive inverse in
   terms of the quantity each one optimises.
6. **Show** that the time-domain Wiener solution equals the frequency-domain
   regularised inverse $\overline{W}/(|W|^2 + \mathrm{NSR})$.

## Prerequisites

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) —
  the water-level inverse this lesson derives from a different starting point.
- [20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](../05-noise-and-random-signals/02-autocorrelation-spectra.md) —
  the correlation functions the normal equations are built from.

## 1. Intuition: the best filter of a given length

Deconvolution asks for the inverse of a fixed, known wavelet. Wiener filtering
asks a more general and more honest question: **of all causal filters of length
$L$, which one minimises the mean squared error between its output and a desired
signal?** The desired signal might be the reflectivity (deconvolution), a shifted
copy of the input (a shaping filter), or the noise (a canceller). The same normal
equations solve all three.

Because the filter is finite, the problem is always well posed: the normal
equations are a finite, symmetric, positive-definite Toeplitz system. Ill-posedness
reappears only as the degree to which the finite filter has to approximate an
unbounded inverse — and that shows up as the length dependence measured in §4.

All models and data in this module are SYNTHETIC. The spike train, wavelet and
noise are generated here.

## 2. Definitions

### 2.1 The filter and the cost

Let $h_0,\dots,h_{L-1}$ be the filter coefficients and $\mathbf{x}[n] =
(x[n], x[n-1], \dots, x[n-L+1])^{\top}$. The output is
$y[n] = h^{\top}\mathbf{x}[n]$. With a **design delay** $\Delta$, we want
$y[n] \approx d[n-\Delta]$ and therefore minimise

$$\xi(h) = \mathbb{E}\!\left[\left(d[n-\Delta] -
h^{\top}\mathbf{x}[n]\right)^2\right].$$

### 2.2 Normal equations

Expanding and differentiating gives the **Wiener-Hopf equations**

$$\sum_{k=0}^{L-1} h_k\, r_{xx}[j-k] = r_{dx}[\Delta - j],
\qquad j = 0,\dots,L-1,$$

with $r_{xx}[m] = \mathbb{E}[x[n+m]x[n]]$ and
$r_{dx}[m] = \mathbb{E}[d[n+m]x[n]]$. The $r_{dx}$ term is nonzero only where the
desired signal correlates with the input — for our convolutional model, only over
the wavelet's support, which is why the design delay $\Delta$ must be chosen to
place that support inside the filter's index range $[0,L-1]$.

### 2.3 Orthogonality

At the optimum the error $e[n] = d[n-\Delta] - y[n]$ satisfies

$$\mathbb{E}\!\left[e[n]\,x[n-j]\right] = 0, \qquad j = 0,\dots,L-1.$$

The error is uncorrelated with every input sample the filter can see. This is the
definition of a least-squares solution projected onto the filter's span, and it
gives us a computable optimality check that needs no knowledge of the answer.

## 3. Derivations

### 3.1 From the cost to the normal equations

$$\xi(h) = \mathbb{E}[d^2] - 2\sum_j h_j r_{dx}[\Delta-j]
+ \sum_j\sum_k h_j h_k r_{xx}[k-j].$$

Setting $\partial\xi/\partial h_j = 0$:

$$-2r_{dx}[\Delta-j] + 2\sum_k h_k r_{xx}[k-j] = 0,$$

which is §2.2. Because $r_{xx}$ is an autocorrelation, the matrix is symmetric
Toeplitz and positive semidefinite, so the system is solvable in $O(L^2)$ by a
Levinson or Toeplitz solver. The demo uses `scipy.linalg.solve_toeplitz` with
$L = 61$, $\Delta = 30$.

### 3.2 Why the design delay must be chosen

$x$ is a *filtered, delayed* version of $d$: the spike at time $p$ appears in $x$
over the interval $[p, p+L_w-1]$. To estimate it from `x[n-j]` with $j\ge0$, the
filter must look at samples at or after the spike, so some delay is unavoidable.
The delay $\Delta$ is the largest index $j$ at which $r_{dx}[\Delta-j]$ is nonzero,
which is why the requirement is $\Delta \le L-1$ and, in practice,
$\Delta \approx L_w$, the wavelet length. The demo's measured best-lag equals the
design delay for every configuration tested (30, 45, 50, 60 samples) — a direct
confirmation that the alignment convention is consistent.

### 3.3 Orthogonality, measured

For $L = 61$, $\Delta = 30$, the demo reports

$$\max_{k\in[0,\,60]}\frac{\left|r_{ex}[k]\right|}{\|e\|\,\|x\|} =
4.11\times10^{-4}, \qquad
\max_{k\in[-60,\,0]}\frac{\left|r_{ex}[k]\right|}{\|e\|\,\|x\|} =
1.29\times10^{-2}.$$

Both are small. The larger value on the negative-lag side is expected: those lags
are outside the filter's causal span, so the orthogonality condition does not apply
to them. The first number is the one that matters and it is $4\times10^{-4}$ — the
least-squares solution is optimal for this finite record to three decimal places.

### 3.4 The frequency-domain form

Taking the transform of the normal equations (in the limit of an infinite filter)
gives

$$\boxed{\;H(f) = \frac{S_{dx}(f)}{S_{xx}(f)}
= \frac{\overline{W(f)}\,S_{dd}(f)}
{\left|W(f)\right|^{2}S_{dd}(f) + S_{ee}(f)}
= \frac{\overline{W(f)}}
{\left|W(f)\right|^{2} + \mathrm{NSR}(f)},\;}$$

where $\mathrm{NSR}(f) = S_{ee}/S_{dd}$ and the design delay appears as the phase
factor $e^{-i2\pi f\Delta\Delta t}$. This is exactly the water-level inverse of
[20-04-01](01-deconvolution-concept.md), derived here from least squares rather
than from a penalty term: **the water level IS the Wiener filter's noise-to-signal
ratio.** The two lessons are the same mathematics seen from two directions.

The equality is verified numerically. With $L = 121$ and $\Delta = 60$ the maximum
deviation between the time-domain filter's response and the frequency-domain form
is $0.1734$, against a filter peak response of $3.1029$ — about 5.6% of the peak.
The residual reflects the finite filter length and the finite-record estimates of
the correlation sequences, not a defect in the formula. The two routes give
recovered-reflectivity SNRs of $6.36$ dB (time domain) and $6.16$ dB (frequency
domain), a difference of 0.2 dB.

## 4. The measurements

### 4.1 Filter length

| length | design delay | recovered SNR (dB) |
|---|---|---|
| 5 | 2 | 5.81 |
| 11 | 5 | 6.14 |
| 21 | 10 | 6.17 |
| 41 | 20 | 6.20 |
| 81 | 40 | 6.27 |
| 161 | 80 | 6.36 |

The gain from length 5 to length 161 is only **0.55 dB**. Once the filter spans the
wavelet, the extra coefficients have nothing left to model and begin to fit the
noise in the estimated correlations. This is the finite-length counterpart of the
regularisation trade: a long filter is a small regulariser, a short one a large
one.

### 4.2 Against the alternatives

At a record SNR of 20 dB:

| method | recovered-reflectivity SNR (dB) |
|---|---|
| raw record (no filter) | $-4.65$ |
| matched filter ($w$ reversed) | $-5.57$ |
| naive inverse ($1/W$) | $5.16$ |
| **Wiener filter** | **$6.36$** |

The comparison needs care, because these filters optimise different things:

- the **matched filter** maximises the *peak* signal-to-noise ratio at a known
  epoch; it is optimal for *detection* and does not reconstruct the reflectivity,
  because it convolves the spike with the wavelet autocorrelation;
- the **naive inverse** reconstructs the reflectivity but amplifies noise
  wherever $|W|$ is small;
- the **Wiener filter** minimises mean squared reconstruction error and wins here
  by 1.2 dB over the naive inverse.

The margin depends strongly on the record quality:

| record SNR (dB) | naive inverse SNR (dB) | Wiener SNR (dB) |
|---|---|---|
| 10 | $-4.70$ | $0.17$ |
| 20 | $5.29$ | $6.61$ |
| 30 | $15.19$ | $15.48$ |
| 40 | $25.27$ | $25.45$ |

At 10 dB the Wiener filter is 4.9 dB better; at 40 dB the two differ by 0.2 dB
because the noise no longer matters and the naive inverse is essentially correct.
**Wiener filtering earns its keep exactly where the noise is significant.**

## 5. Worked example (SYNTHETIC)

A short recording has a wavelet of 40 ms effective length, a sampling interval of
2 ms, and a pre-first-break noise window whose variance is 1% of the signal's.

1. **Wavelet length**: $L_w = 40/2 = 20$ samples.
2. **Filter length**: $L = 4L_w = 80$ samples. From §4.1, beyond about $2L_w$ the
   returns are small.
3. **Design delay**: $\Delta = L_w = 20$ samples, which places the wavelet's
   correlation support inside the filter's index range.
4. **Noise-to-signal ratio**: $0.01$ (1% in power). Compare with the Wiener form:
   the frequency-domain filter is $\overline W/(|W|^2+0.01)$, i.e. a water level
   of $0.01$ relative to $S_{dd} = 1$.
5. **Predicted outcome**: from §4.2, a record SNR of 20 dB with a comparable
   wavelet gives roughly 6 dB of recovered-reflectivity SNR; with a 10 dB record,
   roughly 0 dB. State the prediction before running the inversion, then compare.

That last habit is the point. The Wiener filter is the *minimum* mean squared error
achievable by a causal filter of that length, so it is a benchmark: if your
deconvolution performs worse than the Wiener filter, your operator is suboptimal,
and if it performs better on a metric, the metric is measuring something else.

## 6. Assumptions and regime of validity

1. **Stationarity.** The correlations are assumed not to change over the design
   window. A first-arrival transient or a drifting wavelet breaks this.
2. **The desired signal is available for the design.** Wiener filtering is
   *supervised*: it needs $r_{dx}$, i.e. a recorded or modelled desired signal.
   Deconvolution substitutes the known wavelet for this supervision.
3. **The filter is causal and of fixed length.** The delay and the length are part
   of the design; changing either changes the answer.
4. **Linear time-invariant processing.** As always, adaptive or time-varying
   problems are outside this scope.
5. **Second-order statistics capture what matters.** The Wiener filter uses only
   autocorrelations and cross-correlations. It cannot exploit sparsity, which is
   why sparse (L1) methods can beat it on spiky reflectivity — see
   [20-07-01](../07-inversion-in-signal-processing/01-sparse-deconvolution.md).

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| filter length | $L$ | taps | |
| design delay | $\Delta$ | samples | $\le L-1$ |
| autocorrelation | $r_{xx}$ | (amplitude)$^2$ | $r[0]$ = variance |
| cross-correlation | $r_{dx}$ | (amplitude)$^2$ | same units as $r_{xx}$ |
| NSR | — | dimensionless | power ratio |
| filter coefficients | $h$ | dimensionless | $r_{dx}/r_{xx}$ ratio |

The filter coefficients are dimensionless because they are a ratio of two
correlations in the same units. If your coefficients come out with units, you have
divided the wrong two things.

## 8. Python demonstration

`code/wiener_filtering_demo.py` builds the model, solves the normal equations,
verifies orthogonality, sweeps the filter length and the record SNR, compares the
three filter types, and checks the time-domain solution against the
frequency-domain form. It is self-contained, seeded with
`np.random.default_rng(20261014)`, and exits 0.

What to look for:

1. **section 2** — the orthogonality residual of $4.11\times10^{-4}$ and the best
   lag equalling the design delay.
2. **section 3** — the 0.55 dB total gain from length 5 to 161.
3. **section 4** — Wiener beats the naive inverse by 4.9 dB at 10 dB record SNR and
   by 0.2 dB at 40 dB.
4. **section 5** — the time-domain and frequency-domain responses agreeing to
   0.1734 against a peak of 3.1029, with SNRs of 6.36 and 6.16 dB.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-wiener-filtering-exercises.md`](exercises/03-wiener-filtering-exercises.md)
and
[`exercises/03-wiener-filtering-solutions.md`](exercises/03-wiener-filtering-solutions.md).

- **★** Write the Wiener-Hopf equations for $L = 2$ and a given correlation pair.
- **★★** Explain, using the orthogonality condition, why the Wiener filter is the
  best *linear* estimator of a given length.
- **★★** From the record-SNR table, state where you would bother with Wiener
  filtering and where you would not, with numbers.
- **★★★** Derive the excess mean squared error of a length-$L$ Wiener filter
  relative to the infinite-length filter and compare with the measured 0.55 dB.

## Mastery checkpoint

Complete this without notes:

> A wavelet has effective length 30 samples at 1 ms sampling. A record has a
> signal-to-noise ratio of 30 dB. **(a)** Choose a filter length and design delay
> and justify both. **(b)** Write the frequency-domain Wiener filter and identify
> the regulariser. **(c)** State the orthogonality condition and how you would
> measure it. **(d)** State whether the Wiener filter or the matched filter would
> give a larger *peak* at a reflection, and which would give a better estimated
> reflectivity. **(e)** State one situation where an L1 method would beat the
> Wiener filter, and why.

A worked version appears in the
[solutions](exercises/03-wiener-filtering-solutions.md).

## Common pitfalls

1. **Setting the design delay too small.** The desired signal then correlates with
   input samples outside the filter's span and the normal equations are
   inconsistent-looking (the best lag will not match the design delay).
2. **Using too long a filter.** The gain beyond $2L_w$ is decimal places, and the
   extra coefficients fit noise in the estimated correlations.
3. **Confusing detection with estimation.** The matched filter maximises peak SNR;
   the Wiener filter minimises reconstruction error. They are different problems.
4. **Forgetting that Wiener needs a desired signal.** If you have no reference, you
   are doing blind deconvolution, not Wiener filtering.
5. **Assuming the frequency-domain form is exact for a short filter.** It is the
   infinite-length limit; the demo's 5.6%-of-peak deviation is the finite-length
   cost.

## Related modules

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](01-deconvolution-concept.md) —
  the same filter derived from a penalty term.
- [20-04-02 Spiking (Predictive) Deconvolution and Wavelet Estimation](02-spiking-deconvolution.md) —
  the unsupervised, statistical route.
- [20-04-04 Deconvolution in the Presence of Noise](04-deconvolution-noise.md) —
  where the NSR that appears here comes from.
- [20-03-05 Adaptive Filtering and Noise Cancellation](../03-digital-filtering/05-adaptive-filtering.md) —
  the recursive, data-driven version of the same normal equations.
- [20-05-02 Autocorrelation, Power Spectral Density and Wiener-Khinchin](../05-noise-and-random-signals/02-autocorrelation-spectra.md) —
  the correlation theory.
- [18-02-01 Overdetermined Problems and Least Squares](../../18-inverse-problems/02-linear-inverse-problems/01-overdetermined.md) —
  the linear-algebra view of the normal equations.
