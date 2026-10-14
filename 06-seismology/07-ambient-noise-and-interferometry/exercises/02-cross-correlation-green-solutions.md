# Solutions — 06-07-02 Retrieving the Green's Function by Cross-Correlation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [02 Retrieving the Green's Function by Cross-Correlation](../02-cross-correlation-green.md).

---

## ★1 — Causal and acausal lags

$$t = \frac{d}{c} = \frac{45.0}{3.00} = 15.000\ \mathrm{s}.$$

The causal arrival is at $+15.000\ \mathrm{s}$ and the acausal at
$-15.000\ \mathrm{s}$. The **pair** of lags measures the *symmetry* of the source
field: if the two branches have different amplitudes, the illumination is
one-sided (the demonstration measures ratios from $0.75$ to $21.04$), and if the
two branches have different magnitudes the medium is attenuating or the
estimator is biased.

---

## ★2 — Discrete versus continuum arrival

$$\frac{\tau_A}{dt} = \frac{146.875}{0.5} = 293.75 \longrightarrow 294,$$
$$\frac{\tau_B}{dt} = \frac{165.625}{0.5} = 331.25 \longrightarrow 331,$$
$$\tau_A - \tau_B = (294 - 331)\,dt = -37 \times 0.5 = -18.5\ \mathrm{s}.$$

The continuum value is $-18.75\ \mathrm{s}$, so the discrete model places the
arrival $0.25\ \mathrm{s}$ early — half a sample, the irreducible rounding error
of a whole-sample delay. Note the check: $|\tau_A-\tau_B| = d/c$ is satisfied to
$0.25\ \mathrm{s}$, i.e. to $1.3\%$.

---

## ★3 — Noise floor versus stack length

$$\text{ratio} = \frac{0.41719}{0.04801} = 8.69,$$
$$\text{exponent} = \frac{\log_{10} 8.69}{\log_{10} 64}
= \frac{0.9390}{1.8062} = 0.520 .$$

The theory predicts $0.5$: the incoherent part of the correlation adds in
quadrature and falls as $N^{-1/2}$. The fit over all seven points in the lesson
gives $-0.471$ rather than $-0.500$, and the difference is the diagnostic that
the segments are not perfectly independent.

---

## ★4 — Decomposing the $-0.750\ \mathrm{s}$ error

Two contributions, both measured:

1. **Rounding of the model delays.** From ★2 the model's own arrival is
   $0.25\ \mathrm{s}$ from the continuum value: $|18.75 - 18.50| = 0.25\
   \mathrm{s}$.
2. **The estimator.** The remaining

$$0.750 - 0.250 = 0.500\ \mathrm{s}$$

   is exactly **one sample** at $dt = 0.5\ \mathrm{s}$. It arises because the
   peak of a broad-band wavelet is located by taking the maximum of $|c(\tau)|$
   on the sample grid, without interpolation: a peak that falls between samples
   is displaced by up to half a sample, and here it lands one sample off.

**Justification.** The two contributions are identified separately. The model
rounding is a *known* offset of the discrete model ($0.25\ \mathrm{s}$), while
the remainder ($0.50\ \mathrm{s}$) is exactly one sample: the estimator takes
the maximum of $|c(\tau)|$ on the sample grid, and a broad wavelet (bandwidth
$0.05$-$0.60\ \mathrm{Hz}$, so a pulse of the order of $1\ \mathrm{s}$) can have
its sampled maximum displaced by a full sample from the underlying peak. The
bias is *not* bounded by half a sample in the way a rounding error is, because
it is a property of the estimator and of the wavelet shape, not of the grid. The
honest report is therefore: model rounding $0.25\ \mathrm{s}$, estimator
$0.50\ \mathrm{s}$, with the second removable by interpolating the peak or by
using a narrower band.

---

## ★5 — Why the ratio is not monotone in sector width

The ratio is the peak of the retrieval on the causal branch divided by the peak
on the acausal branch. Three effects compete as the sector narrows.

- The **stationary source** at $\theta = 0$ remains in every sector, so the
  causal branch stays strong.
- The acausal branch requires a stationary source at $\theta = \pi$, which
  disappears as soon as the sector excludes it. That drives the ratio up.
- The **cross-term floor** — the finite-($90$)-source contribution at every lag
  — does not vanish. Its rms at the acausal lag is set by the number of source
  pairs ($\sim N^2$) and by the wavelet width, and it does not fall
  monotonically as the sector narrows, because the sources become denser within
  the surviving azimuths.

The measured pair $10.99$ ($180^\circ$) and $9.04$ ($90^\circ$) is therefore a
flat-topped curve with the floor dominating the $90^\circ$ denominator.

**Control experiment.** Repeat the measurement with a *larger* number of
sources, e.g. $N = 90,\,360,\,1440$ at fixed sector width. If the ratio is
limited by the cross-term floor, it must **grow** with $N$ (as the floor falls);
if it is limited by the physics, it must converge to a stable value. A second
control is to reduce the bandwidth: a narrower wavelet raises the floor's rms
and lowers the ratio, again a test of the artefact hypothesis rather than of the
physics.

---

## ★6 — Required signal-to-noise ratio

$$\sigma_t \approx \frac{1}{2\pi f\,\text{SNR}}
\;\Longrightarrow\;
\text{SNR} \approx \frac{1}{2\pi f\,\sigma_t}
= \frac{1}{2\pi \times 1.0 \times 0.050}
= 3.18 .$$

So an SNR of about $3.2$ suffices at $1\ \mathrm{Hz}$. At
$f = 0.25\ \mathrm{Hz}$ the required SNR scales as $1/f$:

$$\text{SNR}(0.25) = \frac{1}{2\pi\times0.25\times0.050} = 12.7,$$

four times larger. This is the quantitative form of the trade discussed in the
lesson: the same fractional precision costs more signal-to-noise at longer
periods, which is why long-period monitoring is harder than short-period
monitoring at fixed instrument quality.

---

## ★7 — Testing equipartition (specification)

**Observable.** Compare the noise-derived empirical Green's function $g_N(t)$
(the stacked cross-correlation of the pair) with the controlled-shot Green's
function $g_S(t)$ (the direct arrival from the shot, deconvolved from its
source). Normalise both by their peak amplitude on the causal branch.

**Prediction if equipartition holds.** $g_N$ and $g_S$ agree in *arrival time*
to within the timing uncertainty and in *waveform* to within the source
bandwidth; in particular the amplitude ratio of the causal to acausal branch of
$g_N$ is $1.0$ within its confidence interval, and the acausal branch of
$g_N$ matches the time-reversed causal branch of $g_S$.

**Prediction if it fails.** $g_N$ has a systematic amplitude asymmetry between
branches, and the *velocity* inferred from $g_N$ differs from that inferred from
$g_S$ because the retrieved phase is weighted by the illumination rather than by
the medium.

**Decision rule.** Compute the ratio $r$ of the branch amplitudes of $g_N$ and
its standard error $\sigma_r$ from the scatter between seasons. Fail
equipartition if $|r-1| > 3\sigma_r$; report $r$, $\sigma_r$ and the seasonal
consistency of $r$. Note that the test is one-sided in practice: equipartition
can be *falsified* much more sharply than it can be *confirmed*, because a
failing test gives a systematic number while a passing test gives only
consistency within stated uncertainties.

---

## ★8 — The time derivative in the representation theorem

**Origin.** The correlation of two records is a *second-order* quantity in the
wavefield, whereas the Green's function is the *impulse response*. Relating them
requires differentiating one of the fields (equivalently, multiplying the
cross-spectrum by $i\omega$ before transforming), which is where the time
derivative comes from. In the time domain the exact statement is, for an
equipartitioned field,

$$C_{AB}(t) \;\propto\; \frac{d}{dt}\big[G_{AB}(t) - G_{AB}(-t)\big] * S(t).$$

**What it affects.**

- *Amplitude spectra and waveform shape:* a factor $i\omega$ tilts the spectrum
  by $+6\ \mathrm{dB}$ per octave. Any statement about the *relative* amplitude
  of two arrivals with different frequency content (a low-frequency direct wave
  versus a high-frequency coda arrival) is wrong by the ratio of their centre
  frequencies.
- *Phase:* it adds a constant $\pi/2$. Fitting a synthetic wavelet to a
  retrieved waveform without it produces a systematic phase error.

**What it does not affect.**

- *Arrival times*, to first order: a constant $\pi/2$ shift does not move the
  envelope peak, and the $i\omega$ factor is symmetric in $i\omega$ and
  $e^{i\omega t}$ conventions. This is why picking travel times from
  ambient-noise correlations is robust.
- *Relative amplitudes of arrivals with the same spectrum*, e.g. the causal and
  acausal branches of one retrieval, because both carry the same factor.

**A wrong published number.** A study that compares the amplitude of a
noise-retrieved surface wave with the amplitude of a controlled-source surface
wave at a *different* dominant period, without applying the $i\omega$ (and
without deconvolving the source), will report an amplitude discrepancy that is
entirely an artefact of the missing derivative: a factor of two in frequency
becomes a factor of two in amplitude.
