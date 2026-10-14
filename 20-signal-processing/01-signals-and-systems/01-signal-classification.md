---
id: 20-01-01
title: "Signal Classification: Continuous/Discrete, Deterministic/Random"
level: intermediate
prereqs: ["01-01-03", "01-13-03", "03-02-01"]
tags: [signal-processing, signals, deterministic, random, energy, power]
---

# Signal Classification: Continuous/Discrete, Deterministic/Random

A geophysical signal is a *measurable quantity as a function of a variable we
can label*: ground velocity as a function of time, gravity as a function of
position, temperature as a function of depth. Everything later in this folder —
filtering, spectra, wavelets, coherence — is a statement about one or another
class of such functions. The classifications are not academic box-ticking:
almost every processing mistake is the application of a tool that assumes one
class to data that belongs to another. Averaging assumes a random signal;
Fourier summation assumes periodic or finite support; a stationarity assumption
is what allows a time average to stand in for an ensemble average.

**All models and data in this module are SYNTHETIC.** Every waveform used below
is generated inside the demonstration `code/signal_classification_demo.py` and
no number is quoted from a recording or a publication.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** a given geophysical time series along four independent axes:
   continuous vs discrete in the independent variable, real vs complex and
   continuous- vs discrete-valued in the dependent variable, deterministic vs
   random, and finite-energy vs finite-power.
2. **Compute** energy, average power, mean, rms and crest factor of a record
   from first principles, with correct units.
3. **Derive** the exact rms of a sinusoid, triangle and square wave, and verify
   the derivations numerically.
4. **Decompose** any signal into even and odd parts and **prove** that the two
   parts are orthogonal, so their energies add.
5. **Distinguish** periodic from aperiodic signals using the autocorrelation,
   and explain the difference between the biased and unbiased estimator.
6. **Quantify** the difference between a deterministic record and one
   realisation of a random process, including the
   $\sigma/\sqrt{2N}$ sampling spread of an rms estimate.
7. **Define** stationarity and ergodicity, and **test** for stationarity in a
   way that does not fail silently on a chirp.

## Prerequisites

- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md) —
  the unit discipline used in every table below.
- [01-13-03 Expectation, Variance and Covariance](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  expectation and variance, needed for the ensemble statements.
- [03-02-01 NumPy: ndarrays and dtypes](../../03-scientific-computing/02-numpy/01-ndarray-basics.md) —
  how a discrete record is actually stored.

## 1. What is being classified, and why it matters

Take a broadband seismometer. It reports ground velocity every
$0.01\ \mathrm{s}$ — a *discrete*, *real-valued*, finite-precision record that
is one *realisation* of a process we prefer to treat as random. Take the same
sensor and ask for its calibration sheet and you get a *deterministic* response
curve. Take a water-level gauge in a well and you get a record that is
deterministic in its tidal band and random in its weather-driven band, and the
honest classification is "band-dependent".

The four axes are independent, and each of them licenses a different tool:

| Axis | The two ends | What depends on it |
|---|---|---|
| Independent variable | continuous / discrete | whether you use integrals or sums; aliasing exists only in the discrete case |
| Dependent variable | continuous / quantised | the quantisation-noise floor of the record |
| Predictability | deterministic / random | whether one record is enough, or an ensemble is required |
| Quadratic size | finite energy / finite power | whether you can talk about total energy or only average power |

A finite-duration transient has finite energy and zero average power. A sine, or
a stationary noise record, has infinite energy and finite power. Those are
statements about limits, and the arithmetic that decides them is the subject of
Section 3.

## 2. Precise definitions

### 2.1 Signal

A **signal** is a function $x: \mathcal{D} \to \mathcal{R}$. The *domain*
$\mathcal{D}$ may be continuous time $\mathbb{R}$, discrete time $\mathbb{Z}$ (or
$\{0,1,\dots,N-1\}$), or a spatial variable such as distance, depth or
wavenumber. The *range* $\mathcal{R}$ may be real, complex, scalar, vector, or a
matrix (a moment tensor is a signal in this sense).

### 2.2 Discrete time and quantisation are different things

A **discrete-time** signal has samples at $t_n = n\Delta t$; the *sample
interval* $\Delta t$ (unit: seconds) is a property of the domain. A **quantised**
signal has a finite alphabet; the *least significant bit* is a property of the
range. Digital data are both, and the two limits are independent: sampling sets
the highest frequency that can be represented, quantisation sets the noise floor.
Discrete Fourier methods are exact statements about the samples and say nothing
about what happened between them (that is
[05 Sampling, Nyquist and Reconstruction](05-sampling-theory.md)).

### 2.3 Causal, real, symmetric

- **Causal**: $x(t) = 0$ for $t<0$. Real-time filters must be causal; recorded
  data usually are not treated that way.
- **Real**: $x = x^{*}$. Real records have conjugate-symmetric spectra, which is
  why one-sided spectra work at all ([20-02-01](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md)).
- **Even / odd**: $x(-t) = x(t)$ / $x(-t) = -x(t)$. Section 4 shows every signal
  is a sum of one of each.

### 2.4 Deterministic and random

A signal is **deterministic** if its value at any time is fixed by a formula,
table, or previously measured values — repeat the experiment, get the same
record. It is **random** (a *stochastic process*) if each measurement is a draw
from a probability distribution; formally we specify the joint distribution of
$(x(t_1),\dots,x(t_k))$ for every $k$ and every set of times. Repeat the
experiment and you get a *different* record: a **realisation**. The collection of
all possible realisations is the **ensemble**.

A random process is **stationary** if the joint distributions do not change when
all times are shifted, and **wide-sense stationary** (WSS) if only the mean is
constant and the autocovariance depends on the time difference alone. It is
**ergodic** if every ensemble average equals the corresponding long-time average
of one realisation; ergodicity is the licence that lets a single record
substitute for an ensemble, and it is an assumption, never a measurement.

## 3. Energy and power signals

### 3.1 Definitions

For a real continuous-time signal,

$$E = \int_{-\infty}^{\infty} x^{2}(t)\,\mathrm dt, \qquad
P = \lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2} x^{2}(t)\,\mathrm dt.$$

For discrete samples $x[n]$ at interval $\Delta t$, the same quantities are
Riemann sums:

$$E \approx \sum_{n} x^{2}[n]\,\Delta t, \qquad
P \approx \frac{1}{N\Delta t}\sum_{n=0}^{N-1} x^{2}[n]\,\Delta t .$$

A signal with $0<E<\infty$ is an **energy signal**; a signal with
$0<P<\infty$ is a **power signal**. No signal is both: if $E$ is finite then
$P = E/T \to 0$, and if $x$ is periodic with non-zero power then $E = \infty$.

### 3.2 Average power of a sinusoid, derived

Let $x(t) = A\sin(2\pi f_0 t)$ and average over exactly $M$ periods,
$T = M/f_0$:

$$
P = \frac{1}{T}\int_{0}^{T} A^{2}\sin^{2}(2\pi f_0 t)\,\mathrm dt
= \frac{A^{2}}{2}\left[1 - \underbrace{\frac{\sin(4\pi f_0 T)}{4\pi f_0 T}}_{=0}\right]
= \frac{A^{2}}{2},
$$

because $f_0 T = M$ is an integer. The result does not depend on $M$, so the
limit exists and $P = A^{2}/2$. Hence

$$x_{\mathrm{rms}} = \sqrt{P} = \frac{A}{\sqrt{2}}
\approx 0.7071\,A, \qquad
\text{crest factor} = \frac{A}{x_{\mathrm{rms}}} = \sqrt{2}.$$

### 3.3 Average power of a triangle and a square

For a triangle of peak amplitude $A$ and period $T$, use one quarter period
where $x(t) = 4At/T$:

$$P = \frac{4}{T}\int_{0}^{T/4}
\left(\frac{4At}{T}\right)^{2}\mathrm dt
= \frac{4}{T}\cdot\frac{16A^{2}}{T^{2}}\cdot\frac{(T/4)^{3}}{3}
= \frac{A^{2}}{3},$$

so $x_{\mathrm{rms}} = A/\sqrt{3}$ and the crest factor is $\sqrt{3}$. For a
square wave taking values $\pm A$, $x^{2} = A^{2}$ everywhere, so
$P = A^{2}$, $x_{\mathrm{rms}} = A$, and the crest factor is exactly $1$. These
three exact values — $A/\sqrt2$, $A/\sqrt3$, $A$ — are the ones the
demonstration checks.

### 3.4 What the "energy" of a geophysical record is not

If $x$ is ground velocity in $\mathrm{m\,s^{-1}}$, then $E$ has units
$\mathrm{m^{2}\,s^{-1}}$ and $P$ has units $\mathrm{m^{2}\,s^{-2}}$. Neither is
a physical energy in joules; physical energy requires a density and an
impedance. The quadratic integrals are nevertheless the right currency for
signal processing, because they are what Parseval's theorem counts and what a
matched filter maximises. Say "energy-like" when you mean this quantity.

## 4. Even, odd, periodic and the autocorrelation

### 4.1 Even/odd decomposition, and orthogonality

Define the even and odd parts

$$x_e(t) = \tfrac12\bigl[x(t) + x(-t)\bigr], \qquad
x_o(t) = \tfrac12\bigl[x(t) - x(-t)\bigr],$$

so that $x = x_e + x_o$ identically, $x_e$ is even, and $x_o$ is odd. Their
inner product on a symmetric interval $-T/2 \le t \le T/2$ is

$$
\int_{-T/2}^{T/2} x_e x_o \,\mathrm dt
= \frac14\int_{-T/2}^{T/2}\bigl[x^{2}(t) - x^{2}(-t)\bigr]\mathrm dt
= 0,
$$

because the two terms are the same integral after the substitution $t \to -t$.
Orthogonal parts have additive energies:

$$\int_{-T/2}^{T/2} x^{2}\,\mathrm dt
= \int x_e^{2} + \int x_o^{2} + 2\underbrace{\int x_e x_o}_{0}.$$

*Numerical check (SYNTHETIC).* For a 17-sample decaying sinusoid the
demonstration reconstructs $x = x_e + x_o$ with a maximum error of
$5.55\times10^{-17}\ \mathrm{m\,s^{-1}}$ — one part in $10^{16}$, i.e. double
precision rounding — and finds $\sum x^{2} = 10.071472$ versus
$\sum x_e^{2} + \sum x_o^{2} = 10.071472\ (\mathrm{m\,s^{-1}})^{2}$, equal to all
printed digits.

### 4.2 Periodicity and incommensurate frequencies

$x$ is **periodic** with period $T_0$ if $x(t+T_0) = x(t)$ for all $t$. A finite
record is never periodic in this strict sense; what is testable is whether the
autocorrelation returns to $1$. For the sum
$a_1\sin(2\pi f_1 t) + a_2\sin(2\pi f_2 t)$ with means removed,

$$r_{xx}(\tau) = a_1^{2}\cos(2\pi f_1\tau)
+ a_2^{2}\cos(2\pi f_2\tau),$$

so $r_{xx}(\tau) = r_{xx}(0)$ exactly when $f_1\tau$ and $f_2\tau$ are both
integers. If $f_1/f_2$ is rational, such $\tau$ exist and the sum is periodic; if
the ratio is irrational, no non-zero $\tau$ works and the sum is aperiodic
forever.

*Numerical check.* With $f_1 = 5\ \mathrm{Hz}$ and $f_2 = 2.5\ \mathrm{Hz}$
(ratio $2$) the unbiased autocorrelation is $1.000000$ at a lag of $80$ samples
$= 0.4\ \mathrm{s}$, exactly the common period, and again at $160, 240, 320,
400$ samples. With $f_2 = 2\pi\ \mathrm{Hz}$ (irrational ratio) the largest
autocorrelation for $1 \le \text{lag} \le 1000$ is $0.991082$ and no lag exceeds
$0.999$: the record never repeats.

### 4.3 Biased and unbiased autocorrelation

The demonstration divides the lag-$\ell$ correlation by $N$ in one case and by
the number of overlapping samples $N-\ell$ in the other. The first is the
**biased** estimator and the second the **unbiased** one. For the exactly
periodic record above, both are applied at lag $80$:

| normalisation | value at lag 80 samples | interpretation |
|---|---|---|
| $\frac{1}{N}\sum_{n} x[n]x[n+\ell]$ | $0.960000$ | tapers to zero as $\ell \to N$ |
| $\frac{1}{N-\ell}\sum_{n}$ | $1.000000$ | the periodicity is exact |

Neither is "wrong": the biased form is the one whose Fourier transform is
non-negative and therefore is a valid spectral estimate; the unbiased form has
larger variance at long lags. Choosing between them is choosing which defect you
prefer, and the demonstration prints both so the choice cannot be invisible.
(The autocorrelation and its spectrum are the subject of
[05-02-02](../05-noise-and-random-signals/02-autocorrelation-spectra.md).)

## 5. Deterministic versus random in practice

### 5.1 One realisation is one draw

A deterministic signal is fixed: the rms of a $2\ \mathrm{m\,s^{-1}}$ sine is
$1.414214\ \mathrm{m\,s^{-1}}$ every time you compute it. A random signal is
defined by a distribution, and every finite record gives a slightly different
number.

*Numerical check (SYNTHETIC, $\sigma = 1.0\ \mathrm{m\,s^{-1}}$, $N = 256$).*
One realisation of Gaussian white noise has sample mean
$-0.0887\ \mathrm{m\,s^{-1}}$ (not zero — that alone is a $0.089\sigma$ draw) and
sample rms $1.0090\ \mathrm{m\,s^{-1}}$. Across $400$ realisations the mean of
the $400$ sample rms values is $0.9947\ \mathrm{m\,s^{-1}}$, and the spread of
those $400$ values is $0.0460\ \mathrm{m\,s^{-1}}$.

### 5.2 The sampling spread of an rms estimate

For i.i.d. Gaussian samples of variance $\sigma^{2}$,
$\sum x^{2}/\sigma^{2} \sim \chi^{2}_{N}$, so the sample variance
$s^{2} = \tfrac1N\sum x^{2}$ has

$$\operatorname{Var}(s^{2}) = \frac{2\sigma^{4}}{N},
\qquad
\delta x_{\mathrm{rms}} \approx
\frac{\operatorname{std}(s^{2})}{2\sigma}
= \frac{\sigma}{\sqrt{2N}}.$$

For $N = 256$ and $\sigma = 1$: $\sigma/\sqrt{2N} = 0.0442\ \mathrm{m\,s^{-1}}$,
against the measured $0.0460$ — four per cent high, which is the expected
finite-$M$ error of a spread estimated from $400$ values. Averaging $M$
statistically independent realisations reduces the uncertainty of the mean by
$\sqrt{M}$: the measured spread of the ensemble mean is
$0.0023\ \mathrm{m\,s^{-1}}$, consistent with $0.0442/\sqrt{400} = 0.0022$.

Two consequences worth stating plainly:

- **A single rms of a noise record is uncertain at the level
  $\sigma/\sqrt{2N}$.** For a 1-second record at $100\ \mathrm{Hz}$ that is
  about $7\%$; the number is not a property of the noise, it is a property of
  the record length.
- The uncertainty shrinks only as $N^{-1/2}$. To halve it you must quadruple the
  record.

### 5.3 Stationarity, and a diagnostic that does not fail silently

A stationary process has time-independent statistics; the moving rms of a
stationary record fluctuates about a constant, and the fluctuation is itself
sample noise of order $\sigma/\sqrt{2N_{\text{win}}}$. In the demonstration
(synthetic noise, $\sigma = 1$, windows of $500$ samples, $200\ \mathrm{Hz}$) the
eight window rms values are $0.982$ to $1.074$, a spread of $1.125$ — close to
the expected $\pm 1.5\sigma/\sqrt{2\cdot500}$ band.

Now apply the same test to a linear chirp from $0.5$ to $8\ \mathrm{Hz}$ with
constant amplitude. Its window rms values are $0.697$ to $0.712$: constant. **An
amplitude-only stationarity test passes the chirp.** The frequency content is
what changes, and the same windows show it: the zero-crossing frequency estimate
rises monotonically through $0.80, 2.00, 2.80, 3.80, 4.80, 5.60, 6.60,
7.40\ \mathrm{Hz}$ as the sweep advances. Stationarity is a statement about *all*
the statistics; testing only the second moment is a partial test, and a partial
test must be reported as partial.

(The same windows give about $50\ \mathrm{Hz}$ for white noise, which is not a
frequency at all but the $\Delta t/4$ timescale of samples that change sign with
probability $\tfrac12$ — a reminder that an estimator answers the question it
was built for and no other.)

## 6. Units and dimensional analysis

| Quantity | Definition | Unit for $x$ in m/s, $t$ in s |
|---|---|---|
| mean | $\frac1T\int x\,\mathrm dt$ | m/s |
| rms | $\sqrt{\frac1T\int x^{2}\mathrm dt}$ | m/s |
| peak | $\max\lvert x\rvert$ | m/s |
| crest factor | peak / rms | dimensionless |
| energy | $\int x^{2}\mathrm dt$ | $(\mathrm{m/s})^{2}\,\mathrm{s} = \mathrm{m^{2}\,s^{-1}}$ |
| power | $\frac1T\int x^{2}\mathrm dt$ | $(\mathrm{m/s})^{2} = \mathrm{m^{2}\,s^{-2}}$ |

The mean and rms must share the unit of the signal; the crest factor must be
dimensionless; the energy must be power multiplied by time. If a computed rms
comes out in $\mathrm{m^{2}\,s^{-2}}$ you have squared it once too often.

Some unit conversions used in this folder are exact definitions, not measured
values: $1\ \mathrm{Gal} = 0.01\ \mathrm{m\,s^{-2}}$ so
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$; $1\ \mathrm{nT} = 10^{-9}\ \mathrm{T}$.

## 7. Worked examples

### Example 1 — energy, power and crest factor of a finite sinusoid

A synthetic record is $x(t) = 2.0\sin(2\pi\cdot1.0\,t)\ \mathrm{m\,s^{-1}}$
sampled for $T = 5.0\ \mathrm{s}$ at $200\ \mathrm{Hz}$ ($1000$ samples,
$\Delta t = 0.005\ \mathrm{s}$).

1. $E = \sum x^{2}\Delta t$. Because $T = 5$ periods exactly and $\Delta t$
   divides each period into $200$ samples, the sum is exact:
   $E = \frac{A^{2}T}{2} = \frac{4\cdot5}{2} = 10.000000\ (\mathrm{m\,s^{-1}})^{2}\,\mathrm{s}$.
2. $P = E/T = 2.000000\ (\mathrm{m\,s^{-1}})^{2}$, matching $A^{2}/2$.
3. Peak instantaneous power is $A^{2} = 4.000\ (\mathrm{m\,s^{-1}})^{2}$, four
   times the mean — the crest factor squared.
4. rms $=\sqrt{2} = 1.414214\ \mathrm{m\,s^{-1}}$, crest factor $1.4142$.

The demonstration prints every one of these and a relative difference of
$0.000\times10^{0}$ between the numeric energy and $A^{2}T/2$.

### Example 2 — checking a *shape* claim numerically

Suppose an analyst asserts that a synthetic square wave of amplitude
$2\ \mathrm{m\,s^{-1}}$ and a sine of the same amplitude carry the same average
power. The demonstration measures rms $1.414214$ for the sine and $2.000000$ for
the square: the square carries $2$ times the power and $1.414$ times the rms.
The triangle lies between, at $1.154816$ against the exact
$A/\sqrt3 = 1.154701$ (a relative difference of about $1.0\times10^{-4}$ from
discretising a piecewise-linear waveform). The general rule,

$$x_{\mathrm{rms,square}} = A, \quad
x_{\mathrm{rms,triangle}} = A/\sqrt3, \quad
x_{\mathrm{rms,sine}} = A/\sqrt2,$$

is why an instrument's *crest factor* specification, not its peak rating, sets
what waveform it can measure.

### Example 3 — how long a record must be to measure a noise level

A receiver at a quiet synthetic site produces Gaussian noise of
$\sigma = 1.0\ \mathrm{m\,s^{-1}}$. You want the rms known to $1\%$ from one
record. From $\delta x_{\mathrm{rms}}/x_{\mathrm{rms}} = 1/\sqrt{2N}$:

$$N = \frac{1}{2(0.01)^{2}} = 5000 \ \text{samples}.$$

At $100\ \mathrm{Hz}$ that is $50\ \mathrm{s}$ of data. Extrapolating the
demonstration, $N = 256$ gives a $4.4\%$ spread — so a 1-second $256$-sample
noise level reported to three significant figures overstates what the record can
support.

## 8. Python demonstration

`code/signal_classification_demo.py` is print-only, single-process, uses
`numpy` only, and finishes in well under a second. It:

1. tabulates the four-way classification of six synthetic signals;
2. measures mean, rms, peak and crest factor against the exact
   $A/\sqrt2$, $A/\sqrt3$, $A$ values;
3. measures energy and power against $A^{2}T/2$;
4. verifies the even/odd decomposition and the energy split;
5. tests periodicity with biased and unbiased autocorrelations;
6. compares one noise realisation with a $400$-member ensemble and the
   $\sigma/\sqrt{2N}$ prediction;
7. shows a stationarity test that passes a chirp on amplitude and catches it on
   frequency.

```bash
cd 20-signal-processing/01-signals-and-systems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python signal_classification_demo.py
```

## 9. Assumptions and regime of validity

1. **Quadratic size is time-averaged over a window you chose.** $P = A^{2}/2$
   is exact only when the average runs over a whole number of periods; over an
   arbitrary window it is exact only in the limit. The demonstration deliberately
   chose $T = 5$ periods so that the "measurement" is exact and any discrepancy
   would be a bug, not physics.
2. **The random-signal results assume i.i.d. Gaussian samples.** The
   $\sigma/\sqrt{2N}$ formula follows from $\chi^{2}_{N}$; for correlated (red)
   noise the effective number of independent samples is smaller and the spread is
   *larger*. Do not apply it to a strongly autocorrelated record (see
   [05-03 Noise Colour](../05-noise-and-random-signals/03-noise-colour.md)).
3. **Stationarity is assumed, not established, in most processing.** The moving
   rms in Section 5.3 tests the second moment only. A record can be
   wide-sense stationary and non-stationary in every other respect, and a chirp
   is the counter-example to the popular amplitude-only test.
4. **Ergodicity is an assumption.** Time averages equal ensemble averages only
   for ergodic processes. Nothing in a single record can prove ergodicity.
5. **The classification of a real record can be band-dependent.** Flood records,
   tidal records and seismic records are often modelled as deterministic in one
   band and stochastic in another. Classifying the whole record once is a
   convenience, not a fact.
6. **Discreteness is assumed from here on.** From
   [02 LTI Systems](02-lti-systems.md) onward, signals are discrete sequences;
   the bridge from continuous to discrete is
   [05 Sampling, Nyquist and Reconstruction](05-sampling-theory.md).

## 10. Exercises

Graded problem sets and full worked solutions:

- [`exercises/01-signal-classification-exercises.md`](./exercises/01-signal-classification-exercises.md)
- [`exercises/01-signal-classification-solutions.md`](./exercises/01-signal-classification-solutions.md)

## 11. Common pitfalls

1. **Calling a sampled sine "continuous".** The record is a sequence; whether
   the *underlying* physical quantity was continuous is a separate statement that
   sampling cannot settle.
2. **Reporting an rms from a short noise record without its uncertainty.** The
   number is a draw; quote $\sigma/\sqrt{2N}$ beside it.
3. **Using the biased autocorrelation to test periodicity.** It decays as
   $1-\ell/N$ whether or not the signal is periodic, so a threshold on the biased
   curve tests the record length.
4. **Testing stationarity on rms alone.** The $0.5 \to 8\ \mathrm{Hz}$ chirp
   passes that test.
5. **Confusing energy with physical energy.** $E$ here is a quadratic integral in
   $\mathrm{m^{2}\,s^{-1}}$ for a velocity record, not joules.
6. **Assuming a signal is real.** Analytic signals, complex spectra and transfer
   functions are complex-valued from
   [20-02-04](../02-fourier-and-spectral-analysis/04-cross-spectra-coherence.md)
   onward; the conjugate symmetry of a real signal's spectrum is a special case,
   not a rule.

## 12. Mastery checkpoint

Without notes:

**(a)** A synthetic record is $x(t) = 3.0\sin(2\pi\cdot 2.0t)\ \mathrm{m\,s^{-1}}$
sampled for $2.0\ \mathrm{s}$ at $100\ \mathrm{Hz}$. State its class on all four
axes and compute $E$, $P$, rms and crest factor with units.
**(b)** The same record is a triangle wave of the same peak amplitude. What is
its rms, and what is the ratio of its power to the sine's?
**(c)** A single realisation of Gaussian noise of unknown $\sigma$ gives rms
$1.20\ \mathrm{m\,s^{-1}}$ over $N = 400$ samples. Give the rms and its
$1\sigma$ uncertainty, and the uncertainty of that uncertainty's estimate.
**(d)** Two sinusoids of $4.0$ and $6.0\ \mathrm{Hz}$ are added. What is the
shortest non-zero lag at which the unbiased autocorrelation is exactly $1$?
**(e)** Give one statistic whose time-dependence detects the non-stationarity of
a constant-amplitude chirp and one that does not.

Worked answers to (a), (b) and (e) are in the
[solutions](./exercises/01-signal-classification-solutions.md).

## 13. Related modules

- [20-01-02 LTI Systems and Impulse Response](02-lti-systems.md) — what a system
  does to a classified signal.
- [20-01-05 Sampling, Nyquist and Reconstruction](05-sampling-theory.md) — the
  continuous-to-discrete bridge and its price.
- [20-02-01 Practical DFT/FFT](../02-fourier-and-spectral-analysis/01-dft-fft-practice.md) —
  the discrete spectral description of these records.
- [20-05 Noise and Random Signals](../05-noise-and-random-signals/README.md) —
  the systematic treatment of the random class.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the mathematics of the transforms assumed here.
- [03-02 NumPy for Scientific Computing](../../03-scientific-computing/02-numpy/README.md) —
  the array discipline used by every demo in this folder.
