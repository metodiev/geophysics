---
id: 06-07-01
title: "Sources of Ambient Seismic Noise"
level: advanced
prereqs: ["06-01-03", "03-03-05"]
tags: [seismology, ambient-noise, microseism, noise-sources, spectral-analysis]
---

# Sources of Ambient Seismic Noise

**All models and data in this module are SYNTHETIC.** No real station, event or
waveform is used, and no number is quoted from a published measurement. The
band centres, the ocean-wave periods, the source ring and the noise realisations
are chosen teaching values, and every number below is printed by
[`code/noise_sources_demo.py`](code/noise_sources_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the double-frequency relation between the ocean-wave period and
   the secondary-microseism period from the nonlinear interaction of two wave
   trains, and **state** why the primary microseism has the same period as the
   swell.
2. **Measure** the peak periods of a synthetic ambient-noise spectrum and
   **quote** the measurement error against the spectral resolution.
3. **Compute** the skewness and excess kurtosis of a noise series and
   **distinguish** a continuous source field from an impulsive one by its
   statistics.
4. **Derive** the cross-spectrum $C(f)=S(f)J_0(kd)$ of two stations in a diffuse
   2-D noise field, and **evaluate** it at a given period.
5. **Explain** why a one-sided source distribution makes the cross-spectrum
   complex, and **quantify** the phase by which it departs from the isotropic
   value.
6. **State** the assumptions of the diffuse-field model and the observations
   that violate them.

## Prerequisites

- [06-01-03 Surface Waves](../01-elastic-wave-propagation/03-surface-waves.md) —
  Rayleigh and Love waves, dispersion and depth sensitivity.
- [03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../../03-scientific-computing/03-scipy/05-signal.md) —
  Welch's periodogram and the windowing conventions used here.

---

## 1. What ambient noise is, and why it is a source rather than a nuisance

Every seismometer records motion when no earthquake is occurring. That motion
is not instrument noise: it is a real ground displacement produced by a large
population of sources — ocean waves, wind, rivers, traffic, industry. The
useful distinction is not "signal versus noise" but **who produced the motion**:

| Contribution | Where it comes from | Typical band (convention) |
|---|---|---|
| Instrument self-noise | the sensor and digitiser | depends on the instrument |
| Cultural noise | traffic, machinery | high frequency (short period) |
| Secondary microseism | nonlinear ocean-wave interaction | around half the swell period |
| Primary microseism | direct ocean-wave pressure | around the swell period |
| Long-period hum | ocean and atmospheric loading | long period |

The band labels are **conventions** and the exact periods are not universal.
What *is* universal, and what this lesson derives, is the relation between the
ocean-wave period and the two microseism bands. The demonstration uses a
teaching model in which the primary microseism sits at the swell period and the
secondary microseism at half of it:

| swell period (s) | primary (s) | secondary (s) |
|---|---|---|
| 8.0 | 8.0 | 4.0 |
| 10.0 | 10.0 | 5.0 |
| 12.0 | 12.0 | 6.0 |
| 14.0 | 14.0 | 7.0 |
| 16.0 | 16.0 | 8.0 |

These six numbers are printed by the demonstration, not measured.

## 2. Deriving the double-frequency relation

Let the sea surface displacement at a point be the sum of two wave trains of
angular frequencies $\omega_1$ and $\omega_2$ and amplitudes $a_1$, $a_2$:

$$\eta(t) = a_1\cos\omega_1 t + a_2\cos\omega_2 t .$$

The pressure exerted on the sea floor depends on the **square** of the wave
field (the wave-induced pressure is a second-order quantity in the wave
amplitude), so expand

$$
\eta^2 = \tfrac{a_1^2}{2}(1+\cos 2\omega_1 t)
+ \tfrac{a_2^2}{2}(1+\cos 2\omega_2 t)
+ a_1a_2\big[\cos(\omega_1-\omega_2)t + \cos(\omega_1+\omega_2)t\big].
$$

Two consequences follow immediately.

- **Primary microseism.** The term $\tfrac{a_1^2}{2}\cos 2\omega_1 t$ and its
  sibling oscillate at twice the *individual* wave frequency, but a single
  travelling wave train produces a *steady* pressure (the term with no time
  dependence) which does **not** radiate. What radiates at the swell frequency
  $\omega_1$ is the pressure variation caused by the wave passing over a sloping
  sea floor, where the depth changes the pressure under the crest and the
  trough differently. That mechanism is linear in the wave amplitude and
  therefore keeps the swell period.
- **Secondary microseism.** The cross term
  $a_1a_2\cos(\omega_1-\omega_2)t$ has the **difference** frequency. Two
  opposing wave trains of nearly equal frequency (periods $T$ and $T+\delta$)
  give a beat of period $1/(f_1-f_2)$, and the standing-wave pressure pattern
  oscillates at $f_1+f_2 \approx 2f$. Take the ideal case of two trains of equal
  period, $T_1 = T_2 = T$: the difference term has zero frequency and the sum
  term has frequency $2/T$, so the radiated secondary microseism has period

$$\boxed{\;T_{\text{secondary}} = \frac{1}{f_1+f_2} = \frac{T}{2}
\quad\text{when } T_1 = T_2 = T.}$$

That is the $\times 2$ relation of the table: a 14 s swell produces a 7 s
secondary microseism, and the same 14 s swell produces a 14 s primary
microseism. Both numbers are printed by the demonstration.

**Worked numeric example.** Swell of period $T = 12.5\ \mathrm{s}$ and
$13.5\ \mathrm{s}$:

$$f_1 = 0.0800\ \mathrm{Hz}, \quad f_2 = 0.0741\ \mathrm{Hz},$$
$$f_{\text{secondary}} = f_1+f_2 = 0.1541\ \mathrm{Hz}
\quad\Rightarrow\quad T_{\text{secondary}} = 6.49\ \mathrm{s},$$
$$f_{\text{beat}} = |f_1-f_2| = 0.0059\ \mathrm{Hz}
\quad\Rightarrow\quad T_{\text{beat}} = 168.9\ \mathrm{s}.$$

The secondary microseism is *not* a monochromatic line: the interaction of a
spectrum of swell trains produces a **band** of a few tenths of a hertz, not a
single period. This is why one quotes a microseism *band*, and why a
periodogram peak is a measurement with an error rather than a constant.

## 3. Measuring the bands: a synthetic spectrum with two peaks

The demonstration builds a synthetic ambient-noise time series from a chosen
amplitude spectrum — a $1/f$ background plus two Gaussian bumps centred at
$1/16\ \mathrm{Hz}$ and $1/7\ \mathrm{Hz}$ — gives it random phases and
transforms back to time. It then measures the spectrum the way a real study
would: Welch's method, then a search for the peak inside a stated band.

| search band (s) | input band centre (s) | measured peak (s) | error (s) |
|---|---|---|---|
| 12-20 (primary) | 16.0 | 15.87 | $-0.13$ |
| 5-9 (secondary) | 7.0 | 7.04 | $+0.04$ |

The frequency resolution of the periodogram is $df = 1.53\times10^{-4}\
\mathrm{Hz}$. At 7 s this corresponds to a period resolution of

$$\left|\frac{dT}{df}\right| df = \frac{df}{f^2}
= \frac{1.53\times10^{-4}}{(0.1429)^{2}} = 7.5\times10^{-3}\ \mathrm{s}.$$

The measured error of $+0.04\ \mathrm{s}$ is therefore far larger than the
bin width: it is dominated by the fact that the source spectrum is **broad and
smooth**, so the peak of a finite-length estimate wanders inside the bump. The
honest statement of a microseism measurement is a band and a peak with an
uncertainty, not a period.

## 4. Source statistics: continuous versus impulsive

A noise field built from millions of independent small sources is Gaussian by
the central limit theorem. A noise field containing a few large transients is
not. The two are separated by the third and fourth standardised moments, the
**skewness**

$$S = \frac{1}{N}\sum_{i=1}^{N}\left(\frac{x_i-\bar{x}}{\sigma}\right)^{3}$$

and the **excess kurtosis**

$$K = \frac{1}{N}\sum_{i=1}^{N}\left(\frac{x_i-\bar{x}}{\sigma}\right)^{4}-3,$$

so that $S = K = 0$ for a Gaussian. The demonstration measures both on two
synthetic series of $400\,000$ samples:

| series | skewness | excess kurtosis | rms (normalised) |
|---|---|---|---|
| continuous (Gaussian) | $-0.005$ | $-0.001$ | 0.999 |
| impulsive (transients) | $-0.150$ | $+35.277$ | 1.098 |

The impulsive series contains 400 samples boosted by a uniform factor between
8 and 20 with randomly chosen sign. Its excess kurtosis of $+35$ says that the
fourth moment is 38 times the Gaussian value: the variance is dominated by a
handful of samples, so a *spectral* estimate of an impulsive field is unstable
(a single transient can dominate a periodogram bin), while a *correlation*
estimate is not, because the transient appears at one lag only. This asymmetry
— correlations are more robust than spectra — is one reason ambient-noise
interferometry (lesson 02) is done in the time domain.

## 5. The coherence of a diffuse field

Now take two stations separated by $d$ and a population of sources on a large
ring of radius $R \gg d$ around them, each source emitting statistically
independent noise. Write the source ring in polar coordinates with
$\theta = 0$ along the station-pair axis. The distance from a ring source at
azimuth $\theta$ to a station at axial coordinate $x$ is $R - x\cos\theta$ in
the far field, so the phase that source imposes on the station record is
$-k(R-x\cos\theta)$ with $k = 2\pi f/c$. Because the sources are uncorrelated,
the cross-spectrum of the two station records is the **sum of their individual
phase factors**:

$$C(f) = S(f)\,\frac{1}{2\pi}\int_0^{2\pi}
e^{\,ikd\cos\theta}\,d\theta = S(f)\,J_0(kd),$$

where $J_0$ is the Bessel function of the first kind of order zero, defined
exactly by that integral, and $S(f)$ is the (common) power spectral density of
one station. Dividing by the auto-spectrum gives the **coherence**
$C(f)/S(f) = J_0(kd)$.

The demonstration evaluates the same integral by discrete summation over 720
azimuths and compares with `scipy.special.j0`:

| period (s) | $f$ (Hz) | $kd$ (rad) | measured $C$ | $J_0(kd)$ | difference |
|---|---|---|---|---|---|
| 20.0 | 0.050 | 5.890 | $+0.11922$ | $+0.11922$ | $2.4\times10^{-17}$ |
| 14.0 | 0.071 | 8.415 | $+0.06510$ | $+0.06510$ | $5.7\times10^{-17}$ |
| 10.0 | 0.100 | 11.781 | $-0.00246$ | $-0.00246$ | $2.2\times10^{-18}$ |
| 7.0 | 0.143 | 16.830 | $-0.18401$ | $-0.18401$ | $1.1\times10^{-16}$ |
| 5.0 | 0.200 | 23.562 | $-0.11683$ | $-0.11683$ | $4.3\times10^{-17}$ |
| 3.5 | 0.286 | 33.660 | $+0.01590$ | $+0.01590$ | $1.2\times10^{-16}$ |

The agreement at the level of $10^{-16}$ confirms that the discrete model *is*
the integral. Three features matter physically.

- The coherence is **real and sign-changing**: $C$ has no imaginary part for an
  isotropic field, so the two stations are either in or out of phase depending
  on frequency. It vanishes at every zero of $J_0$, the first being
  $kd = 2.4048$.
- At $d = 60\ \mathrm{km}$ and $T = 10\ \mathrm{s}$ the stations are almost
  completely **incoherent** ($|C| = 0.0025$).
- Coherence is not monotone in separation or frequency; it oscillates. The
  amplitude of the oscillation decays as $1/\sqrt{kd}$ for large $kd$, which is
  why the far-field retrieval is weak at high frequency.

**Worked numeric example (the 7 s row).** With $d = 60\ \mathrm{km}$,
$c = 3.20\ \mathrm{km\,s^{-1}}$, $T = 7\ \mathrm{s}$:

$$f = \frac{1}{7} = 0.142857\ \mathrm{Hz}, \qquad
k = \frac{2\pi f}{c} = \frac{2\pi \times 0.142857}{3.20}
= 0.28050\ \mathrm{rad\,km^{-1}},$$
$$kd = 0.28050 \times 60 = 16.830\ \mathrm{rad}, \qquad
J_0(16.830) = -0.18401.$$

The demonstration prints $kd = 16.830$ and $C = -0.18401$; the units of $k$ are
radians per kilometre and $kd$ is dimensionless, as a Bessel argument must be.

## 6. Directional sources: what a single sector does

Real noise is not isotropic. Confine the sources to a sector of width
$\Delta\theta$ centred on the station-pair axis and repeat the sum:

| sector (deg) | $\mathrm{Re}\,C$ | $\mathrm{Im}\,C$ | $|C|$ | phase (deg) | $|C|-|J_0|$ |
|---|---|---|---|---|---|
| 360 | $-0.1840$ | $+0.0000$ | 0.1840 | 179.99 | $+0.0000$ |
| 180 | $-0.1839$ | $-0.0252$ | 0.1857 | $-172.21$ | $+0.0017$ |
| 90 | $-0.3096$ | $-0.0386$ | 0.3120 | $-172.90$ | $+0.1280$ |
| 45 | $-0.7110$ | $-0.5974$ | 0.9287 | $-139.96$ | $+0.7447$ |
| 20 | $-0.5076$ | $-0.8582$ | 0.9971 | $-120.60$ | $+0.8131$ |

At $T = 7\ \mathrm{s}$ the isotropic value is $J_0 = -0.1840$ and it is real.
Narrowing the illumination to a $45^\circ$ sector raises the coherence magnitude
from $0.184$ to $0.929$ — a factor of five — and rotates its phase to
$-139.96^\circ$. **The coherence magnitude and phase are therefore not
properties of the Earth alone.** A one-sided source field produces a complex
cross-spectrum whose phase measures the mean source azimuth; in a single
measurement that phase is indistinguishable from propagation effects along a
laterally varying path. This is the central, honest difficulty of ambient-noise
interferometry, and lessons 02-05 are all, in one way or another, about coping
with it.

## 7. Assumptions and regime of validity

The results of §5-§6 rest on a specific set of assumptions. Each one has a
diagnostic that fails when the assumption does.

1. **Uncorrelated sources.** Each source emits noise independent of every other
   source. If two sources are coherent (for example two nearby resonating
   structures), the cross-terms add coherently and the retrieved function is
   wrong. *Diagnostic:* repeat the analysis on disjoint time windows and check
   the agreement; coherent sources are stationary, incoherent ones are not.
2. **Far field and a large ring.** $R \gg d$, so the incident wavefront is
   locally plane. For a source inside the array the cross-spectrum is not
   $J_0(kd)$ at all. *Diagnostic:* the coherence should be independent of
   source distance; if it is not, sources are too close.
3. **No scattering or attenuation between source and stations.** The model puts
   a phase $e^{ikr}$ on each path and nothing else. Attenuation multiplies the
   coherence by $e^{-\gamma d}$, which biases velocity estimates from amplitude
   ratios.
4. **Stationary source distribution.** The source statistics must not change
   over the analysis window; otherwise the average over windows mixes two
   different fields. *Diagnostic:* the retrieval must be stable between
   sub-windows.
5. **Single-mode propagation.** The derivation assumed one wave speed $c$. A
   superposition of modes or a dispersive medium makes $k$ a function of
   frequency, which is exactly what lesson 03 turns into a measurement.

Two further limits deserve to be stated as such. First, the Bessel result is a
statement about the **second-order statistics** of the fields, not about any
particular pair of records: with one hour of data the estimate of $C(f)$
fluctuates, and the fluctuation is what §3's periodogram noise and lesson 02's
emergence measurements quantify. Second, an isotropic *ambient* field is an
idealisation that fails exactly where the science is interesting: on real
arrays the directions of maximum noise power change with season and with
frequency, so the retrieved function is a **directional average** of the
Green's function, not the Green's function.

## Mastery checkpoint

Answer without notes, then compare with §5.

> Two stations are separated by $d = 60\ \mathrm{km}$ on a homogeneous
> half-space with $c = 3.20\ \mathrm{km\,s^{-1}}$. **(a)** Compute $kd$ for
> $T = 20\ \mathrm{s}$ and $T = 10\ \mathrm{s}$, and state the coherence at
> each period. **(b)** At which period does the coherence first vanish?
> **(c)** A narrow source sector makes the coherence at $T = 7\ \mathrm{s}$
> equal to $0.9287$ with phase $-139.96^\circ$. Give one physical
> interpretation of the phase and one of the magnitude, and explain why neither
> can be read as structure in a single measurement. **(d)** Explain in one
> sentence why the secondary microseism has half the period of the swell.

## Common pitfalls

1. **Treating the noise level as instrument noise.** Ambient noise is signal;
   what matters is its **directionality** and its **statistics**, not its size.
2. **Quoting a microseism period as a constant.** It is the peak of a broad
   band, and the measurement error exceeds the periodogram bin width.
3. **Assuming isotropy.** The default assumption of the mathematics, not a
   property of the Earth; report the azimuthal coverage before quoting a
   coherence.
4. **Reading a coherence magnitude without the phase.** The complex
   cross-spectrum carries both, and directional bias shows up in the phase
   first.
5. **Using a spectral estimate on impulsive noise.** Kurtosis of tens means a
   single transient dominates a periodogram bin; correlate instead.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  what the retrieved waves are.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  scattering versus intrinsic loss, the distinction the coda tests.
- [20-02 Fourier and Spectral Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/README.md) —
  the estimators used here in full.
- [21-07 Time Series and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md) —
  stationarity and the statistics of the source field.

## Code and exercises

- Demonstration: [`code/noise_sources_demo.py`](code/noise_sources_demo.py)
  (prints the microseism bands, the measured peak periods, the source
  statistics, the $J_0(kd)$ verification and the directional bias table).
- Exercises: [`exercises/01-noise-sources-exercises.md`](exercises/01-noise-sources-exercises.md)
  with worked [solutions](exercises/01-noise-sources-solutions.md).
