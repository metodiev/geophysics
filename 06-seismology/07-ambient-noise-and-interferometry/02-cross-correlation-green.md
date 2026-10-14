---
id: 06-07-02
title: "Retrieving the Green's Function by Cross-Correlation"
level: doctoral
prereqs: ["06-07-01", "06-01-03"]
tags: [seismology, ambient-noise, interferometry, green-function, stationary-phase]
---

# Retrieving the Green's Function by Cross-Correlation

**All models and data in this module are SYNTHETIC.** The station geometry, the
source ring, the passband and the noise realisations are chosen teaching values,
and every number below is printed by
[`code/cross_correlation_green_demo.py`](code/cross_correlation_green_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the cross-correlation of two records in a diffuse field by
   stationary phase, and **state** the resulting relation between the
   correlation function and the Green's function.
2. **Evaluate** the exact inverse transform of $J_0(kd)$ and **explain** why
   the correlation is time-limited to $|t|\le d/c$.
3. **Build** a synthetic noise experiment and **measure** the retrieved direct
   arrival, comparing it with $d/c$ and decomposing the error into its causes.
4. **Quantify** the emergence of the retrieval with stacking and **fit** the
   $\sqrt{N}$ law, reporting the measured exponent.
5. **Measure** the causal-to-acausal amplitude ratio for a one-sided source
   field and **interpret** it as a directional bias rather than structure.
6. **State** when the retrieved function is *not* a Green's function.

## Prerequisites

- [06-07-01 Sources of Ambient Seismic Noise](01-noise-sources.md) — the diffuse
  field, $J_0(kd)$ and the statistics of the source population.
- [06-01-03 Surface Waves](../01-elastic-wave-propagation/03-surface-waves.md) —
  the dispersed wave packet whose group delay is measured here.

---

## 1. The problem

Two stations record noise. Each record is a sum over sources, and the sources
are unknown. Yet the **cross-correlation** of the two records is dominated by
those sources that illuminate both stations in a special way, and the result
looks like the response of the medium to an impulsive source at one station,
recorded at the other. Written in the frequency domain,

$$\boxed{\;C_{AB}(\omega) \;=\; \sum_{\text{sources } s}
S_s(\omega)\,
G_{As}G_{Bs}^{*}
\;\longrightarrow\; \text{const}\times S(\omega)\,
\mathrm{Im}\,G_{AB}(\omega)\;}$$

for an equipartitioned, isotropic field, where $G$ is the Green's function and
$S$ the source spectrum. The relation is a special case of the
**correlation-type representation theorem**. The exact time-domain form
contains a time derivative and a sum of $G(t)$ and $G(-t)$; for arrival-time
measurement the derivative only reshapes the wavelet, so this lesson works with
the correlation function directly and states when that is legitimate.

The whole content of the method is in the arrow: the sum over *unknown* sources
becomes the Green's function *between the stations*. It works because of
stationary phase, which §2 derives.

## 2. Stationary phase, and why the result is time-limited

Put the sources on a large ring of radius $R\gg d$ and let $x_A = -d/2$,
$x_B = +d/2$ be the two stations on the ring axis. A ring source at azimuth
$\theta$ reaches station $i$ with travel time

$$\tau_i(\theta) = \frac{R - x_i\cos\theta}{c}, \qquad
\tau_A - \tau_B = \frac{d\cos\theta}{c}.$$

The cross-correlation of the two records is a sum over sources of the source
autocorrelation evaluated at the difference of the two delays:

$$c(\tau) = \sum_s C_{ss}\!\left(\tau - \frac{d\cos\theta_s}{c}\right).$$

Two facts follow, and both are visible in the demonstration.

- **Time limit.** Since $\cos\theta\in[-1,1]$, every source contributes at a lag
  between $-d/c$ and $+d/c$. Nothing contributes outside, so the correlation
  has **compact support in lag**. This is a strong, testable prediction:
  $|c(\tau)|$ must be noise for $|\tau| > d/c$.
- **Piling up at the ends.** The map $\theta\mapsto (d/c)\cos\theta$ has zero
  derivative at $\theta = 0$ and $\theta = \pi$, where sources are *stationary*
  and therefore add coherently. The density of contributions diverges there
  like $1/\sqrt{1-(\tau c/d)^2}$, so the correlation concentrates at
  $\tau = \pm d/c$: the two branches are the causal and acausal Green's
  functions.

In the frequency domain the same statement is the Bessel integral of lesson 01,
$C(f) = S(f)J_0(2\pi f d/c)$, and its exact inverse transform is

$$\int_0^{\infty} J_0(2\pi f a)\cos(2\pi f t)\,df
= \begin{cases}
\dfrac{1}{\pi\sqrt{a^{2}-t^{2}}}, & |t| < a,\\[2mm]
0, & |t| > a,
\end{cases}
\qquad a \equiv \frac{d}{c}.$$

The integrable singularity at $t = \pm a$ is the arrival. With a finite
bandwidth, as in any real (or synthetic) record, the singularity is smoothed
into a pulse whose width is set by the bandwidth; the *position* of the pulse is
what we measure.

**Worked numeric example.** With $d = 60\ \mathrm{km}$ and
$c = 3.20\ \mathrm{km\,s^{-1}}$,

$$a = \frac{d}{c} = \frac{60.0}{3.20} = 18.750\ \mathrm{s},$$

so the causal arrival is at $+18.750\ \mathrm{s}$ and its acausal twin at
$-18.750\ \mathrm{s}$. For a sampling interval $dt = 0.5\ \mathrm{s}$ the model
delays round to whole samples: $18.750/0.5 = 37.5$ samples, so the *discrete*
model places the arrival about half a sample (0.25 s) from the continuum value
— an irreducible $\pm dt/2$ uncertainty in this experiment.

## 3. Measuring the retrieved arrival

The demonstration builds the two records directly in the time domain. Ninety
uncorrelated sources lie on a ring of $500\ \mathrm{km}$; each emits white noise
which is delayed to each station by $\tau_i(\theta)$ and summed. The records are
band-passed to $0.05$-$0.60\ \mathrm{Hz}$, and the cross-correlation is stacked
over 64 segments of 64 s (4096 s of record).

| quantity | value |
|---|---|
| analytic arrival $d/c$ | $+18.750\ \mathrm{s}$ |
| measured causal peak lag | $+18.000\ \mathrm{s}$ |
| error | $-0.750\ \mathrm{s}$ |
| one sample at 2 Hz | $0.250\ \mathrm{s}$ |
| speed inferred from the measurement | $3.333\ \mathrm{km\,s^{-1}}$ |
| causal / acausal peak amplitude | $0.7625 / 0.5408$ |

The $0.750\ \mathrm{s}$ error decomposes exactly:

$$0.750 = \underbrace{0.250}_{\text{model: delay rounded to a sample}}
+ \underbrace{0.500}_{\text{estimator: peak of a broad wavelet, 1 sample}}.$$

Both terms are artefacts of the *measurement*, not of the physics. The first is
removed by interpolating the delays instead of rounding them; the second by
locating the peak of the envelope rather than of the waveform, or by using
higher frequencies where the pulse is sharper. The inferred speed,
$3.333\ \mathrm{km\,s^{-1}}$ against a model of $3.200\ \mathrm{km\,s^{-1}}$,
is biased high by $4\%$ for the same reason: a fixed timing error is a larger
fractional error at larger separation, and the estimator's bias does not cancel
between separations.

## 4. Emergence: how long must you record?

The retrieval is a stack of incoherent contributions. The **coherent** part —
the arrival — adds linearly; the **incoherent** part adds in quadrature and
therefore falls as $1/\sqrt{N}$ with the number of stacked segments. The
demonstration measures the noise floor of the correlation (its rms for
$25\ \mathrm{s} < |\tau| < 60\ \mathrm{s}$) as a function of the stack length:

| $N$ segments | noise floor | $\log_{10} N$ | $\log_{10}$(floor) |
|---|---|---|---|
| 1 | 0.41719 | 0.000 | $-0.380$ |
| 2 | 0.26682 | 0.301 | $-0.574$ |
| 4 | 0.21383 | 0.602 | $-0.670$ |
| 8 | 0.13690 | 0.903 | $-0.864$ |
| 16 | 0.11178 | 1.204 | $-0.952$ |
| 32 | 0.09760 | 1.505 | $-1.011$ |
| 64 | 0.04801 | 1.806 | $-1.319$ |

A straight-line fit gives

$$\frac{d\log_{10}(\text{floor})}{d\log_{10}N} = -0.471,$$

against the $-0.500$ predicted by the $\sqrt{N}$ law. The small discrepancy is
expected: the segments are not perfectly independent because the same source
realisation supplies all of them, and the residual correlation between
neighbouring lags is not zero. The converged arrival amplitude, measured on the
64-segment stack, is $A = 0.4537$, so the detection statistic grows from

$$\text{SNR}(1) = \frac{A}{\text{floor}(1)} = 1.1
\quad\text{to}\quad
\text{SNR}(64) = \frac{A}{\text{floor}(64)} = 9.5 .$$

**The retrieval is not visible until the incoherent part has been averaged
down.** A single 64 s segment would not have detected the arrival.

## 5. The second honest difficulty: one-sided sources

Restrict the sources to a sector centred on the station-pair axis and repeat the
measurement. The two branches of the correlation are no longer equal:

| sector (deg) | sources | $|c(+d/c)|$ | $|c(-d/c)|$ | ratio |
|---|---|---|---|---|
| 360 | 90 | 0.77862 | 1.03358 | 0.75 |
| 180 | 90 | 1.43095 | 0.13022 | 10.99 |
| 90 | 90 | 2.75800 | 0.30510 | 9.04 |
| 45 | 90 | 5.94233 | 0.28246 | 21.04 |

For the full ring the ratio is $0.75$, i.e. close to the value $1$ that the
theory demands, with a departure that is the *residual* of a finite (90-source)
ring. For a half ring the causal branch is $11\times$ the acausal one, and for a
$45^\circ$ sector $21\times$. Two consequences:

- The empty branch is never exactly zero in a real measurement, so the ratio is
  a **lower bound** on the true directional bias, not a measurement of it.
- A ratio greater than one is the standard diagnostic of a source distribution
  that is not symmetric about the station pair. Reporting it is the minimum
  honesty: a one-sided retrieval gives one branch of the Green's function, and
  the missing branch is not recoverable from the same data.

The same physics produces the magnitude and phase bias quantified in lesson 01
§6: a directional source field multiplies the retrieval by a complex factor, so
the *amplitude* of the arrival is a convolution of structure with source
strength, and the *time* is only unbiased if the source spectrum is smooth and
the bias is not dispersive.

## 6. Verification: the retrieved time is linear in separation

A retrieval that is actually the Green's function must move linearly with
station separation. The demonstration repeats the experiment for four
separations with the same ring:

| $d$ (km) | predicted $t = d/c$ (s) | measured lag (s) | $c$ from lag (km/s) |
|---|---|---|---|
| 20 | 6.25 | 6.00 | 3.333 |
| 40 | 12.50 | 12.50 | 3.200 |
| 60 | 18.75 | 18.50 | 3.243 |
| 80 | 25.00 | 22.50 | 3.556 |

The mean inferred speed is $3.333\ \mathrm{km\,s^{-1}}$ against the model
$3.200\ \mathrm{km\,s^{-1}}$, and the rms timing error is $2.52$ samples
($1.262\ \mathrm{s}$). The 80 km row is the worst: its measured lag is
$2.50\ \mathrm{s}$ early. Diagnosing *why* is exactly the skill this lesson
teaches — the candidates are (i) the discrete sample rounding of the delays,
(ii) the peak-picking window $\pm 4\ \mathrm{s}$, which is wide enough to admit
a noise peak, and (iii) the finite number of stationary sources, which for a
given bandwidth concentrates the arrival less sharply at larger $d$. The honest
report is the measured table plus the statement that the $4\%$ speed bias is
**not** a property of the model.

## 7. Assumptions and regime of validity

1. **Equipartition.** The energy must be distributed equally among the
   propagating modes of the medium. Without it, the retrieved function is the
   *illumination pattern* of the sources, not the Green's function. There is no
   internal test for equipartition; it must be checked with an independent
   source (an earthquake) whose Green's function is known.
2. **Isotropy of the source distribution.** §5 shows the failure mode
   quantitatively. The test is the causal/acausal ratio and the stability of the
   retrieval when data from the seasons with different storm tracks are used.
3. **No attenuation, or known attenuation.** Attenuation multiplies the
   retrieved arrival by $e^{-\gamma d}$ and adds a dispersive phase. Amplitude
   information is therefore unreliable; travel time is not.
4. **Far field and one mode.** The derivation used plane waves from a distant
   ring. A source inside the array, or two modes with different speeds, breaks
   the one-to-one map between lag and arrival.
5. **The correlation function is not the Green's function.** It is, at best,
   proportional to a time derivative of the sum of the causal and acausal
   Green's functions. The phase shift of $\pi/2$ that the derivative introduces
   matters for waveform fitting and does not matter for picking arrival times.

## 8. Worked example: reading the retrieval of a two-station pair

Let a measured empirical Green's function show a peak at $t = 24.0\ \mathrm{s}$
on the causal branch and at $-24.4\ \mathrm{s}$ on the acausal branch, for a
station separation of $d = 78\ \mathrm{km}$.

1. **Speed.** The two branches should be symmetric. The mean absolute lag is
   $(24.0 + 24.4)/2 = 24.2\ \mathrm{s}$, giving
   $c = 78/24.2 = 3.223\ \mathrm{km\,s^{-1}}$.
2. **Asymmetry.** The ratio is $24.0/24.4 = 0.984$ in amplitude-equivalent
   terms; more useful is the amplitude ratio, which the demonstration measures
   directly. If the *amplitudes* differ by a factor of 3, report the ratio as
   the directional diagnostic and return to §5.
3. **Uncertainty.** The timing uncertainty cannot be better than half a sample
   plus the ratio of the noise floor to the arrival amplitude. With
   $dt = 0.5\ \mathrm{s}$ and SNR $= 9.5$ (the measured value at $N=64$), and
   taking $f = 0.30\ \mathrm{Hz}$ as the nominal centre of the modelled
   $0.05$-$0.60\ \mathrm{Hz}$ passband, the standard error of the arrival time is
   roughly

$$\sigma_t \approx \frac{1}{2\pi f}\cdot\frac{1}{\text{SNR}}
= \frac{1}{2\pi \times 0.30}\cdot\frac{1}{9.5} = 0.056\ \mathrm{s},$$

   which is *smaller* than half a sample — the estimator, not the sampling, is
   then the limiting factor. Report which of the two dominates.

## Mastery checkpoint

> **(a)** Derive $\tau_A-\tau_B = (d/c)\cos\theta$ for ring sources and state why
> the correlation vanishes for $|\tau|>d/c$. **(b)** With $d = 78\ \mathrm{km}$
> and $c = 3.20\ \mathrm{km\,s^{-1}}$, where are the two arrivals? **(c)** The
> measured noise floor falls by a factor of $8.0$ when the stack grows from
> $N=1$ to $N=64$. What exponent does that imply, and what does the theory
> predict? **(d)** A colleague reports a $12\%$ asymmetry between the two
> branches and interprets it as a dipping interface. Give two alternative
> explanations and one measurement that would discriminate.

## Common pitfalls

1. **Reading one branch.** A one-sided source field makes one branch an artefact;
   always report both and their ratio.
2. **Treating the correlation as a Green's function.** It is the sum of the
   causal and acausal Green's functions with a wavelet-shaped source term; the
   absolute phase is not recovered without deconvolution.
3. **Quoting a speed from one station pair.** The estimator's bias (this lesson
   measures $4\%$) is a property of the estimator; use many pairs and quote the
   distribution.
4. **Assuming more stack always helps.** The $\sqrt{N}$ law assumes independent
   segments; correlated segments (a persistent source) do not average down, and
   the measured slope ($-0.471$ here, not $-0.500$) is the diagnostic.
5. **Ignoring the sample grid.** Half a sample is not zero.

## Related modules

- [06-07-01 Sources of Ambient Seismic Noise](01-noise-sources.md).
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same correlation identities in active-source geometry.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  why an average over an unknown source distribution is an inverse problem.
- [20-04 Deconvolution and Inverse Filtering](../../20-signal-processing/04-deconvolution-and-inverse-filtering/README.md) —
  the operator that turns a correlation into a Green's function estimate.

## Code and exercises

- Demonstration:
  [`code/cross_correlation_green_demo.py`](code/cross_correlation_green_demo.py).
- Exercises:
  [`exercises/02-cross-correlation-green-exercises.md`](exercises/02-cross-correlation-green-exercises.md)
  with worked [solutions](exercises/02-cross-correlation-green-solutions.md).
