---
id: 05-06-02
title: "Noise Suppression: Stacking, Filtering, Median, KL Transform"
level: advanced
prereqs: ["05-06-01", "01-10-05"]
tags: [stacking, median-filter, band-pass, kl-transform, svd, deconvolution, regularization]
---

# Noise Suppression: Stacking, Filtering, Median, KL Transform

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the $\sqrt{N}$ stacking law and state the three conditions it requires.
2. **Choose** between stacking, median filtering, band-pass filtering and KL
   (SVD) filtering according to the *structure* of the noise, not its amplitude.
3. **Measure** the signal distortion that each method causes, and report it next to
   the noise reduction.
4. **Explain** why deconvolution is an ill-posed inverse problem, in spectral terms.
5. **Write** the Tikhonov/Wiener and water-level operators and explain what the
   regularisation parameter does.
6. **Measure** the noise amplification of a regularised inverse as a function of the
   regularisation parameter, and choose the parameter from a stated criterion.

## Prerequisites

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — where
  these methods sit in the sequence, and the transfer-function view.
- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md)
  — the spectral tools used throughout.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](../../01-mathematics/10-fourier-analysis/03-convolution.md)
  — the convolution model that deconvolution inverts.

## 1. Intuition: match the method to the noise's structure

Four methods dominate noise suppression, and they work for four different reasons:

| method | noise structure it defeats | why it works | what it costs |
|---|---|---|---|
| **stacking** | independent noise between traces | averaging reduces variance as $1/N$ | needs alignment; does nothing for coherent noise |
| **median filtering** | sparse, large outliers (spikes) | the median ignores a minority of extreme values | truncates the peaks of sharp events |
| **band-pass filtering** | noise outside the signal band | multiplication by a transfer function | removes signal in the rejected band; changes phase unless zero-phase |
| **KL / SVD filtering** | incoherent noise on a gather of coherent events | the coherent part is a few eigenimages | needs the signal to be both coherent and comparable to the noise |
| **deconvolution** | not noise suppression at all — it inverts a known wavelet | spectral division by the wavelet | amplifies noise without limit unless regularised |

The recurring theme is the one from
[05-06-01](./01-processing-pipeline-concept.md): **every one of these is a
measurement of two numbers, not one.** Report the noise reduction *and* the signal
distortion, or the report is not a report.

## 2. Derivation: the stacking law and its conditions

Let the recorded trace be $d_i(t) = s(t) + n_i(t)$ with a **common** signal and
independent zero-mean noise of variance $\sigma^2$. The $N$-trace stack is

$$S(t) = \frac{1}{N}\sum_{i=1}^{N} d_i(t) = s(t) + \frac{1}{N}\sum_i n_i(t),$$
$$\operatorname{Var}\big[S\big] = \frac{1}{N^2}\cdot N\sigma^{2} = \frac{\sigma^{2}}{N}
\quad\Longrightarrow\quad
\sigma_S = \frac{\sigma}{\sqrt{N}} .
\tag{1}$$

The three conditions that equation (1) requires are each a real field failure mode:

1. **Common signal** — the events must be aligned. Misalignment by a static
   $\sigma_t$ attenuates the stack by roughly $\exp(-2\pi^{2}f^{2}\sigma_t^{2})$
   ([05-06-03](./03-static-and-datum.md)), so alignment must come first.
2. **Independent noise** — coherent noise is not reduced. Source-generated noise
   (ground roll), power lines and air blast have the same moveout across traces and
   survive stacking almost intact.
3. **No outlier dominating the average** — a single huge spike in one trace raises the
   mean by (spike amplitude)/$N$, which is why the edit stage precedes stacking.

### 2.1 Measured

[`code/noise_suppression_demo.py`](./code/noise_suppression_demo.py) measures the
standard error of an $N$-trace stack over 40 000 realisations of unit-variance noise:

| $N$ | measured SEM | $\sigma/\sqrt{N}$ | S/N gain |
|---|---|---|---|
| 1 | 0.99218 | 1.00000 | 1.000 |
| 2 | 0.70472 | 0.70711 | 1.414 |
| 4 | 0.50141 | 0.50000 | 2.000 |
| 8 | 0.35395 | 0.35355 | 2.828 |
| 16 | 0.25136 | 0.25000 | 4.000 |
| 64 | 0.12575 | 0.12500 | 8.000 |

Agreement with $1/\sqrt{N}$ is to better than 0.4 %. **The square root is the tax:
sixteen times the acquisition effort for a factor four in signal-to-noise.**

## 3. Median filtering: outliers versus peaks

The median of a windowed set of samples ignores a minority of extreme values, which
makes it the right tool for spike removal and the wrong tool for preserving sharp
events. The demo filters a Ricker wavelet contaminated with three spikes of amplitude
2.5, −3.0 and +1.8 (*SYNTHETIC*), and measures both effects:

| window | RMS vs truth | spike residual at index 71 | peak retained (%) |
|---|---|---|---|
| (input, no filter) | 0.19211 | +2.50000 | 100.00 |
| 3 | 0.00221 | 0.00000 | 95.32 |
| 5 | 0.00290 | 0.00000 | 95.32 |
| 7 | 0.01343 | 0.00000 | 82.02 |
| 11 | 0.03363 | 0.00000 | 62.09 |

Read the table as a trade-off curve, not as a recommendation. The spike residual is
exactly zero for every window (the median rejects it completely), while the retained
peak falls from 95 % to 62 % as the window widens. **The distortion grows with the
window while the benefit saturates at window 3**: the spikes are isolated, so a wider
window buys nothing and costs amplitude. A window wider than the shortest event of
interest will destroy that event, and this is measurable in advance from the event's
own width.

## 4. Band-pass filtering: measured suppression and measured distortion

The demo places a coherent noise band at 70 and 95 Hz, a signal band from 5 to 40 Hz,
and applies a rectangular 5–40 Hz pass band (*SYNTHETIC* sampling at 500 Hz):

| quantity | measured |
|---|---|
| RMS outside the wavelet, before | 0.30410 |
| RMS outside the wavelet, after | 0.01169 |
| noise reduction factor | 26.02× |
| wavelet peak, before | 1.34114 |
| wavelet peak, after | 0.94471 (−5.53 %) |
| energy of the **true** wavelet retained | 99.18 % |

Two numbers, both required. The noise is suppressed by a factor 26 and the signal's
energy is retained to 99.18 % — because the signal band lay inside the pass band. A
rectangular pass band removes 0.82 % of the signal energy even in the best case,
because the Ricker wavelet is not exactly band-limited; a smooth (tapered) pass band
would trade a little noise suppression for less ringing and less leakage.

The honest statement of the physics is that **a filter cannot create bandwidth that
was never recorded**. If the acquisition band excluded 60 Hz, no band-pass recovers
it; the filter's job is to remove what is *outside* the band, and its success is
measured by how little of the inside it takes with it.

## 5. KL (SVD) filtering: a coherence bet, with a measurable success criterion

For a gather written as a matrix $\mathbf{D}$ of traces by time samples, the singular
value decomposition

$$\mathbf{D} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\!\top} ,
\qquad
\mathbf{D}_k = \sum_{j=1}^{k} \sigma_j\,\mathbf{u}_j\mathbf{v}_j^{\!\top}
\tag{2}$$

expresses the gather as a sum of eigenimages ordered by energy. If the signal is
coherent across traces it occupies the first few eigenimages; incoherent noise is
spread over all of them. Truncating at rank $k$ therefore suppresses noise — if the
signal really is coherent.

The demo builds a 24-trace gather with a single wavelet on a linear moveout and
white noise of $\sigma = 0.10$ (signal standard deviation 0.1478, so S/N = 1.48):

| rank $k$ | error vs truth (%) | data residual | purity of reconstruction (%) |
|---|---|---|---|
| 1 | 73.20 | 0.1435 | 96.31 |
| 2 | 44.72 | 0.1123 | 96.12 |
| 3 | 32.78 | 0.0993 | 94.93 |
| **4** | **29.74** | 0.0917 | 93.01 |
| 6 | 38.07 | 0.0844 | 88.24 |
| 10 | 49.19 | 0.0703 | 81.12 |
| 24 (full) | 68.19 | 0.0000 | 68.53 |

Three points, each measurable:

- **The error against the truth has an interior minimum at rank 4.** Rank 1 is
  *biased* (it cannot hold the amplitude trend across the gather); rank 24 has zero
  data residual and reproduces the noise.
- **Pushing the rank to 24 drives the data residual to exactly zero.** That is
  overfitting, expressed in eigenimages, and it is the same failure as fitting a
  polynomial of degree $N-1$ to $N$ points.
- **Purity falls monotonically** from 96 % to 68.5 %, which is simply the input signal
  fraction. Rank selection trades purity against bias; there is no rank that is best
  by both.

The demo then repeats the experiment at three noise levels, which is the honest test
of whether the method is applicable at all:

| noise $\sigma$ | input S/N | best rank | best error (%) | error at full rank (%) |
|---|---|---|---|---|
| 0.05 | 2.96 | 4 | 15.91 | 33.96 |
| 0.10 | 1.48 | 4 | 28.99 | 67.59 |
| 0.30 | 0.49 | 2 | 75.17 | 204.56 |

**When the noise dominates the signal (S/N ≈ 0.5) the best possible low-rank
reconstruction leaves 75 % error.** KL filtering is a bet that the signal is coherent
*and* comparable to the noise in amplitude; when that bet fails the method fails, and
the failure is visible in advance by measuring the input S/N.

## 6. Deconvolution: why dividing by a wavelet is not a filter but an inverse problem

Seismic and some potential-field processing model the recorded trace as the
convolution of a reflectivity series $r$ with a wavelet $w$:

$$d(t) = (w * r)(t) + n(t) \qquad\Longleftrightarrow\qquad
\hat d(k) = \hat w(k)\,\hat r(k) + \hat n(k) .
\tag{3}$$

Deconvolution recovers $r$ by an operator $\hat h(k) = 1/\hat w(k)$, i.e. by spectral
division. That is the naive inverse, and it is unusable for a reason visible in
equation (3): the noise term appears **added**, so the recovered model is

$$\hat m(k) = \hat r(k) + \frac{\hat n(k)}{\hat w(k)} .
\tag{4}$$

Equation (4) is the whole problem. The noise is amplified by $1/|\hat w|$, which is
unbounded wherever the wavelet has little energy. This is not ill-conditioning; it is
**ill-posedness**: for a wavelet with a spectral null, the information at that
frequency has been multiplied by zero and is gone.

### 6.1 Measured ill-posedness

The demo uses a 30 Hz Ricker wavelet on a 512-sample trace (*SYNTHETIC*, $dt = 2$ ms)
and a spike reflectivity:

| quantity | measured |
|---|---|
| max $\lvert \hat w \rvert$ over the band | 6.9173 |
| min $\lvert \hat w \rvert$ over the band | $9.363\times10^{-19}$ |
| double-precision floor $\epsilon\max\lvert\hat w\rvert$ | $1.536\times10^{-15}$ |
| bins numerically indistinguishable from zero | **62 of 257**, from 191.41 Hz upward |
| max $\lvert 1/\hat w\rvert$ | $1.068\times10^{18}$ |
| samples of the naive result that are non-finite | **512 of 512** |

The naive inverse does not produce a noisy answer; it produces `NaN`, because in
finite precision the division by a null performs a division by zero. The demonstration
is worth remembering: the failure of deconvolution is not a subtle degradation that a
careful worker can spot in the section — it is total.

### 6.2 Tikhonov (Wiener) regularisation, and the measurement of its effect

Replace the inverse by

$$\hat h_\lambda(k) = \frac{\hat w^{*}(k)}{\lvert \hat w(k)\rvert^{2} + \lambda^{2}} ,
\tag{5}$$

which reduces to $1/\hat w$ where $|\hat w| \gg \lambda$ and to $\hat w^{*}/\lambda^{2}$
(strong attenuation) where $|\hat w| \ll \lambda$. The demo measures three quantities
for a sweep of $\lambda$: the **operator noise gain** (the standard deviation of the
operator applied to unit-variance white noise), the **leakage** into a quiet zone of
the sampled trace where the true reflectivity is zero, and the **spike recovery**
(the mean magnitude recovered at the true spike samples, relative to the truth).

| $\lambda$ | operator noise gain | leakage (quiet zone) | leakage / ($\sigma\times$gain) | spike recovery (%) |
|---|---|---|---|---|
| 0.0001 | 1107.1066 | 1.741970 | 0.830 | 264.09 |
| 0.0010 | 87.4174 | 0.180893 | 1.092 | 46.23 |
| 0.0030 | 37.8071 | 0.047483 | 0.663 | 39.41 |
| 0.0100 | 10.7210 | 0.013232 | 0.651 | 36.69 |
| 0.0300 | 3.7923 | 0.006319 | 0.880 | 35.00 |
| **0.1000** | **1.0292** | 0.004376 | 2.244 | **31.80** |
| 0.3000 | 0.4221 | 0.004661 | 5.828 | 27.42 |
| 1.0000 | 0.1549 | 0.003864 | 13.168 | 21.44 |
| 3.0000 | 0.0663 | 0.000646 | 5.141 | 13.58 |
| 30.0000 | 0.0022 | 0.000024 | 5.738 | 0.53 |

This is the required measurement of noise amplification against the regularisation
parameter, and it contains four things worth stating plainly:

1. **The gain falls by a factor $1107/0.0022 = 5\times10^{5}$ across the sweep.** The
   regularisation parameter is not a cosmetic knob; it changes the operator's noise
   response by five orders of magnitude.
2. **Leakage falls with it, monotonically beyond $\lambda \approx 0.1$**, from 0.0044
   to 0.000024 — the practical demonstration that damping removes noise from the
   model.
3. **Leakage is *not* simply $\sigma$ times the gain.** The measured ratio in the
   fourth column varies between 0.65 and 13.17, and the variation is a real effect,
   not scatter: leakage measures **two** things — the amplified noise *and* the
   smearing of the spikes into the quiet zone — and the smeared-signal part does not
   fall as fast as the operator gain. At small $\lambda$ (0.001–0.01) the ratio is
   near 1 and the amplified noise dominates, so the gain is the right proxy; at large
   $\lambda$ the noise is gone and the leakage is almost entirely smeared signal.
   An earlier draft of this lesson asserted that leakage *equals* noise times gain;
   the measurement refutes that, and the correction matters because it identifies
   which of the two mechanisms is binding at each $\lambda$.
4. **The recovery column falls monotonically with $\lambda$**, from 264 % (noise
   masquerading as signal) through 31.8 % at $\lambda = 0.1$ to 0.53 % at
   $\lambda = 30$. There is no $\lambda$ that is best by both leakage and recovery,
   so the choice must be made from a **stated criterion**: require leakage at or below
   the data noise and take the loosest $\lambda$ that achieves it, or estimate the
   noise level and use the Wiener form $\lambda^{2} = |\hat n|^{2}/|\hat r|^{2}$
   evaluated per frequency bin. The criterion belongs in the processing report.

The demonstration also shows the limit that no regularisation removes: the spike
recovery never reaches 100 %, because 62 of the 257 spectral bins carry no information
at all. A band-limited wavelet with nulls cannot reproduce a spike reflectivity
exactly, at any $\lambda$. Anyone who quotes a "perfect" deconvolution has not
measured the recovery.

### 6.3 The water-level method

An alternative to equation (5) floors the denominator directly:

$$\hat h_\mu(k) = \frac{\hat w^{*}(k)}{\max\big(\lvert\hat w(k)\rvert^{2},\;
\mu\,\max_k\lvert\hat w(k)\rvert^{2}\big)} .
\tag{6}$$

| water level (% of peak power) | operator noise gain | leakage | spike recovery (%) |
|---|---|---|---|
| 0.01 | 2.6189 | 0.007246 | 34.46 |
| 0.10 | 0.6959 | 0.006182 | 31.07 |
| 1.00 | 0.3252 | 0.006868 | 25.91 |
| 5.00 | 0.1669 | 0.006558 | 22.35 |
| 20.00 | 0.1018 | 0.003271 | 18.35 |
| 50.00 | 0.0724 | 0.004602 | 14.69 |
| 90.00 | 0.0465 | 0.001294 | 11.28 |

The water level behaves in the same direction as Tikhonov damping and is easier to
choose, because the level is compared with a spectrum that can be plotted and
inspected. The non-monotone leakage column is not noise in the numbers: leakage is
measured in a fixed quiet zone and includes the operator's own sidelobes, which move
as the floor changes.

## 7. Assumptions

1. **Independent noise for equation (1).** Correlated noise reduces the effective $N$.
   Measure the correlation; do not assume it.
2. **Aligned signal for equation (1).** Alignment error enters as attenuation, not as
   noise, and it is measured by the statics formula.
3. **A known wavelet for equations (3)–(6).** The wavelet is usually estimated from the
   data (statistical or deterministic wavelet extraction), and an error in the wavelet
   propagates directly into the model — as a *bias*, not as noise.
4. **Stationary noise for the regularisation.** The Wiener form of $\lambda$ assumes a
   known noise power spectrum; where the noise is non-stationary, $\lambda$ must vary.
5. **Additive noise in equation (3).** Multiplicative noise, timing jitter and
   amplitude errors are not described by this model and are not removed by
   deconvolution.
6. **Synthetic parameters.** Every number in Sections 2–6 comes from the stated
   synthetic configurations, not from a field dataset. The *method* is transferable;
   the numbers are not.

## 8. Units and dimensional analysis

Stacking, equation (1), preserves the unit: $\sigma_S$ and $\sigma$ are both in the
field unit, and $N$ is a pure count. The transfer functions in Sections 3–4 are
dimensionless.

Deconvolution is the interesting case. If $d$ and $r$ are amplitudes of the same kind
(a voltage ratio, a reflectivity), then $\hat w$ must be dimensionless for equation
(3) to balance, and the regularisation parameter $\lambda$ in equation (5) carries the
**same dimension as $\hat w$** — which is why $\lambda$ cannot be quoted as a bare
number: it is only meaningful together with the wavelet's scale. The water level in
equation (6) avoids this by being defined as a *ratio* of powers, and it is therefore
dimensionless and transferable between datasets. That is a genuine advantage of the
water-level parameterisation and a reason it is popular in practice.

## 9. Python demonstration

[`code/noise_suppression_demo.py`](./code/noise_suppression_demo.py) produces the
tables of Sections 2–5; the Tikhonov operator and its gain measurement are:

```python
H = np.conj(W) / (np.abs(W) ** 2 + lam ** 2)            # equation (5)
m = np.fft.irfft(D * H, n=nt)                           # the model
noise_gain = np.fft.irfft(np.fft.rfft(rng.normal(0.0, 1.0, nt)) * H, n=nt).std()
```

The key discipline is that `noise_gain` is obtained by applying the *same* operator to
a *known* noise realisation, so that the amplification is measured rather than
reasoned about. The companion
[`code/deconvolution_regularisation_demo.py`](./code/deconvolution_regularisation_demo.py)
produces the tables in Section 6, and constructs the data by circular convolution so
that $\hat d = \hat w \hat r$ holds bin by bin and the recovery measurement is not
confounded by a linear-phase offset.

## 10. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/02-noise-suppression-exercises.md`](./exercises/02-noise-suppression-exercises.md)
and [`exercises/02-noise-suppression-solutions.md`](./exercises/02-noise-suppression-solutions.md).

### Common mistakes

1. **Reporting a noise reduction without a signal distortion.** Both come from the
   same transfer function.
2. **Stacking misaligned traces and expecting $\sqrt{N}$.** Alignment error is
   attenuation, and it grows with the square of frequency.
3. **Using a median window wider than the shortest event.** Measured: 62 % peak
   retained at window 11.
4. **Believing coherent noise averages out.** It is not reduced in proportion to
   $\sqrt{N}$, and the residual is not visible in the stack's statistical error.
5. **Applying KL filtering without checking the input S/N.** At S/N 0.49 the best
   rank leaves 75 % error.
6. **Using the naive spectral inverse "just to see".** It returns `NaN` on 512 of 512
   samples in the measured example.
7. **Quoting $\lambda$ without the wavelet's scale.** Section 8.

### Real-world applications

- **Seismic deconvolution.** Wavelet shaping, predictive deconvolution for multiples,
  and spiking deconvolution all use equation (5) or (6) with a data-estimated
  wavelet; the noise-gain table is the standard justification for the chosen
  operator length.
- **Potential-field filtering.** Upward continuation is a low-pass with a known
  transfer function; band-pass filtering between two continuation levels is the
  classical regional/residual separation of
  [05-06-05](./05-merge-and-regularisation.md).
- **Repeat surveys and time-lapse.** Stacking and KL filtering both appear as
  noise-reduction steps when comparing epochs; the coherence assumption is usually
  well satisfied because the same acquisition geometry is repeated.
- **Any inverse problem.** Equation (4) is the model case for the ill-posedness
  theory of [18-01-02](../../18-inverse-problems/01-inverse-problem-foundations/02-hadamard-well-posedness.md)
  and the regularisation practice of
  [18-03-02](../../18-inverse-problems/03-regularization/02-tikhonov.md).

## 11. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis* (2nd ed.). SEG.** The definitive
  practitioner treatment of stacking, filtering and deconvolution, with the operator
  mathematics. Level: advanced practitioner.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Chapters 5–6 on deconvolution and noise attenuation.
- **Hansen, P. C. (2010). *Discrete Inverse Problems: Insight and Algorithms*. SIAM.**
  Chapters 1–5. The rigorous treatment of ill-posedness, the Picard condition and
  Tikhonov regularisation; the mathematics behind Section 6. Level: advanced.
- **Tikhonov, A. N., & Arsenin, V. Y. (1977). *Solutions of Ill-Posed Problems*.
  Wiley.** The original source for equation (5). Level: advanced.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic Applications*.
  Cambridge University Press.** Chapter 9 for continuation-based band-pass filtering.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 12. Related lessons

- [05-06-01 The Processing Pipeline](./01-processing-pipeline-concept.md) — where each of these steps belongs in the sequence.
- [05-06-03 Static Corrections, Datum and Elevation Effects](./03-static-and-datum.md) — the alignment that stacking requires.
- [05-06-05 Gridding, Merging and Levelling of Survey Data](./05-merge-and-regularisation.md) — continuation as a filter, and the derivative noise gain.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) — the general theory of equation (5).
- [01-10-06 Hilbert Transform, Analytic Signal and Instantaneous Phase](../../01-mathematics/10-fourier-analysis/06-hilbert-transform.md) — the transform used when a phase change is wanted rather than removed.

## 13. Self-assessment checklist

- [ ] I can derive $\sigma_S = \sigma/\sqrt{N}$ and name the three conditions it needs.
- [ ] I can state, for each of the four suppression methods, the noise structure it suits.
- [ ] I can report a band-pass result with both the noise reduction and the retained signal energy.
- [ ] I can explain why deconvolution is ill-posed rather than merely ill-conditioned.
- [ ] I can write the Tikhonov operator and say what $\lambda$ does to low and high $|\hat w|$.
- [ ] I can measure an operator's noise gain by applying it to a known noise realisation.
- [ ] I can state a criterion for choosing $\lambda$ and defend it.
- [ ] I can explain why the regularisation parameter carries the wavelet's dimension.
