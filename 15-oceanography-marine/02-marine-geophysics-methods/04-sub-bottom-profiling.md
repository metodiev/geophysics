---
id: 15-02-04
title: "Sub-Bottom Profiling and Chirp Systems"
level: graduate
prereqs: ["15-02-01", "15-01-01", "20-01-03"]
tags: [oceanography, marine-geophysics, sub-bottom-profiler, chirp, pulse-compression, matched-filter, attenuation]
---

# Sub-Bottom Profiling and Chirp Systems

> **All models and data in this module are SYNTHETIC.** The chirp parameters,
> attenuation law and layered model are chosen teaching values, printed by the
> demonstration in `code/`. No profiler, survey, sediment property or published
> attenuation curve is reproduced.

A sub-bottom profiler measures the same thing a reflection seismic survey does —
two-way travel times to impedance contrasts beneath the seafloor — with a
trade that is the opposite of a seismic survey's. It works at kilohertz
frequencies where the wavelength is centimetres, so its vertical resolution is
centimetric; and it works at kilohertz frequencies where the attenuation is
hundreds of times larger, so its penetration is metres to tens of metres rather
than kilometres.

The engineering that makes this useful is **pulse compression**. A short pulse
gives resolution but carries little energy; a long pulse carries energy but
resolves nothing. A **chirp** — a long pulse whose frequency sweeps — and a
**matched filter** resolve the conflict, delivering the resolution of the swept
bandwidth with the energy of the long pulse. This lesson derives that, measures
it, and then measures the price: attenuation removes the high frequencies first,
so the effective bandwidth narrows with depth and **the resolution is not a
constant of the instrument but a function of the path.**

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a linear chirp and **relate** its duration, bandwidth and
   sweep rate.
2. **Derive** the compressed-pulse resolution $c/(2B)$ and **measure** it from a
   synthetic matched-filter output.
3. **Compare** a chirp with a continuous-wave pulse of equal duration, in
   resolution and in energy.
4. **Explain** the windowing trade between main-lobe width and side-lobe level,
   and **measure** both for a rectangular and a tapered chirp.
5. **Account for** the matched filter's processing gain in decibels, and
   **decompose** it into compression, band-limited noise rejection and the
   main-lobe peak-to-rms factor.
6. **Compute** a penetration limit from a frequency-dependent attenuation law,
   and **state** the resolution-versus-penetration trade it implies.
7. **Measure** the degradation of resolution with path length from the narrowing
   effective bandwidth, and **state** why the effect is not an instrument
   constant.

## Prerequisites

- [15-02-01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the reflection coefficient, the convolutional model and the trace geometry.
- [15-01-01 Seawater Properties: Temperature, Salinity, Density](../01-physical-oceanography/01-seawater-properties.md) —
  the sound speed and its sensitivity.
- [20-01-03 Convolution, Correlation and Filters](../../20-signal-processing/01-signals-and-systems/03-convolution-and-filters.md) —
  the operations a matched filter is built from.

## 1. A linear chirp

A **linear chirp** sweeps its frequency from $f_0$ to $f_1$ over a duration $T$:

$$s(t) = \sin\!\left[2\pi\left(f_0 t + \tfrac{1}{2}\frac{B}{T}t^{2}\right)\right],
\qquad 0 \le t \le T, \qquad B = f_1-f_0,$$

with instantaneous frequency $f_0 + (B/T)t$ and sweep rate $B/T$. The
demonstration's chosen parameters are $f_0 = 2\ \mathrm{kHz}$,
$f_1 = 6\ \mathrm{kHz}$ over $T = 20\ \mathrm{ms}$, so $B = 4\ \mathrm{kHz}$,
$B/T = 0.2\ \mathrm{MHz\,s^{-1}}$, and the **time–bandwidth product**
$BT = 80$.

Two facts about its spectrum:

- the rectangular chirp puts $97.35\,\%$ of its energy inside the swept band,
  with a spectral centroid at $3.995\ \mathrm{kHz}$;
- a Hann-tapered chirp puts $100.00\,\%$ inside the band (the taper removes the
  edge discontinuities), at the price of a slightly non-uniform amplitude.

The purpose of the sweep is to *spread the energy over a wide band* rather than
concentrate it at one frequency: what will be recovered, after compression, is a
narrow pulse whose width is set by $B$ while its amplitude is set by the total
energy of the long pulse.

## 2. Pulse compression by matched filtering

### 2.1 The measurement

A synthetic trace is built as the convolution of a reflectivity series with the
chirp, and is processed by cross-correlation with a replica of the chirp.

For a single isolated interface at $30.000\ \mathrm{ms}$:

| quantity | value |
|---|---|
| compressed peak position | $30.000\ \mathrm{ms}$ (the input position) |
| compressed FWHM | $0.2900\ \mathrm{ms}$ |
| resolution $c\,\mathrm{FWHM}/2$ in sediment ($1600\ \mathrm{m\,s^{-1}}$) | $0.2320\ \mathrm{m}$ |
| textbook limit $c/(2B)$ | $0.2000\ \mathrm{m}$ |
| $1/B$ | $0.2500\ \mathrm{ms}$; FWHM$/(1/B) = 1.160$ |

**The compressed pulse is 0.29 ms wide where the transmitted pulse was 20 ms
wide — a compression factor of 69.** The measured resolution, $0.232\ \mathrm{m}$,
is within $16\,\%$ of the limiting $c/(2B) = 0.200\ \mathrm{m}$; the excess is the
difference between the sinc's half-width ($0.886/B$) and $1/B$, plus the finite
sample rate.

The peak *position* is preserved exactly, which is the property that makes
compression usable: compression changes the pulse's shape, never the travel time
it encodes.

### 2.2 The comparison that motivates the whole method

A $4\ \mathrm{kHz}$ continuous-wave pulse of the same duration and the same energy:

| | CW pulse | chirp |
|---|---|---|
| compressed FWHM | $19.89\ \mathrm{ms}$ | $0.29\ \mathrm{ms}$ |
| resolution | $15.91\ \mathrm{m}$ | $0.23\ \mathrm{m}$ |
| theoretical form | $cT/2 = 16.00\ \mathrm{m}$ | $c/(2B) = 0.20\ \mathrm{m}$ |

**A factor 69 in resolution at equal energy.** The CW pulse's resolution is set by
its *duration*; the chirp's by its *bandwidth*. Since the two are independent
parameters of a swept pulse, a chirp is not a compromise but a way of having both.

## 3. Windowing: the side-lobe/width trade

A rectangular chirp compresses into a sinc whose range side lobes reach
$-13.3\ \mathrm{dB}$ — only $21\,\%$ of the main peak, which is easily mistaken
for a weak real reflector. Tapering the chirp suppresses them:

| taper | FWHM (ms) | resolution (m) | peak side lobe (dB) |
|---|---|---|---|
| rectangular | 0.2900 | 0.2320 | $-13.57$ |
| Hann | 0.5500 | 0.4400 | $-26.10$ |

The measured rectangular side lobe, $-13.6\ \mathrm{dB}$, is close to the analytic
sinc value of $-13.26\ \mathrm{dB}$, which is a check on the processing rather than
a coincidence. The Hann taper buys $12.5\ \mathrm{dB}$ of side-lobe suppression
for a factor $1.90$ in main-lobe width.

**This is a trade, not a defect.** The main-lobe width and the side-lobe level of
a matched filter are related by the taper's spectral leakage, and every window is a
point on that trade-off. A survey that must detect a weak layer adjacent to a
strong one applies a taper and accepts the loss of resolution; one that must
resolve closely spaced layers of similar amplitude does not.

## 4. Processing gain, accounted for

With the definitions

$$\mathrm{SNR}_{\text{in}} = \frac{\mathrm{rms(signal)}}{\mathrm{rms(noise)}},
\qquad
\mathrm{SNR}_{\text{out}} = \frac{\mathrm{peak(compressed)}}
{\mathrm{std(compressed\ noise)}},$$

the matched filter's gain is **exactly** $\sqrt{N}$ in amplitude, where $N =
T\,F_s$ is the number of samples in the pulse:

$$G = 10\log_{10}N = 10\log_{10}(T F_s).$$

With $N = 2000$ (20 ms at 100 kHz) that is $33.01\ \mathrm{dB}$, and it
decomposes into three named contributions:

| contribution | value |
|---|---|
| compression, $10\log_{10}(BT)$ | 19.03 dB |
| rejection of noise outside the signal band, $10\log_{10}[(F_s/2)/B]$ | 10.97 dB |
| peak-to-rms of the compressed main lobe, $10\log_{10}2$ | 3.01 dB |
| **sum** | **33.01 dB** |

Measured:

| noise $\sigma$ | input SNR (dB) | output SNR (dB) | gain (dB) |
|---|---|---|---|
| 0.05 | 23.01 | 56.20 | 33.19 |
| 0.10 | 16.99 | 50.54 | 33.55 |
| 0.30 | 7.45 | 41.00 | 33.55 |

**The gain is independent of the noise level** — it is a property of the waveform
— and the measured values sit within a decibel of the prediction. The residual is
the finite realisation of the noise-only estimate of the compressed noise
standard deviation, not a discrepancy in the physics.

The decomposition is worth remembering because only the *first* line is specific
to a chirp: the second is available to any filter matched to any signal, and the
third is a definitional artefact of using a peak where a mean square would be
symmetric. Quoting "the chirp gain" as $33\ \mathrm{dB}$ mixes three different
things.

## 5. Absorption and the penetration limit

Attenuation in sediment rises with frequency. The demonstration uses a chosen
teaching law, one-way:

$$\alpha(f) = 0.10 \times \left(\frac{f}{\mathrm{kHz}}\right)^{1.0}
\ \mathrm{dB\,m^{-1}},$$

so the two-way loss over a path $R$ is $2\alpha R$ and the penetration for a
given dynamic range DR is $R = \mathrm{DR}/(2\alpha)$:

| $f$ (kHz) | $\alpha$ (dB m$^{-1}$) | $R$ at 40 dB | at 60 dB | at 80 dB |
|---|---|---|---|---|
| 1 | 0.100 | 200.0 m | 300.0 m | 400.0 m |
| 2 | 0.200 | 100.0 | 150.0 | 200.0 |
| 4 | 0.400 | 50.0 | 75.0 | 100.0 |
| 8 | 0.800 | 25.0 | 37.5 | 50.0 |
| 16 | 1.600 | 12.5 | 18.8 | 25.0 |

Under this law a factor 2 in frequency costs a factor 2 in penetration. **The
trade is unavoidable and it is the defining constraint of the method: resolution
comes from frequency (through the bandwidth) and penetration is lost to frequency
(through attenuation).** A chirp does not beat it; it collects more energy at a
given frequency, which buys dynamic range — and therefore penetration — at fixed
resolution. That is why the *same* frequency band serves both shallow,
high-resolution work and (with a longer pulse and more energy) deeper work.

## 6. Resolution is a function of depth

Attenuation removes the high frequencies first, so the *effective* bandwidth of
the pulse narrows as it propagates. Using the half-power width of the surviving
spectrum:

| path (m) | extra loss at 6 kHz vs 2 kHz | half-power bandwidth (kHz) | resolution (m) |
|---|---|---|---|
| 0 | 0.00 dB | 4.000 | 0.200 |
| 5 | 4.00 dB | 3.009 | 0.266 |
| 15 | 12.00 dB | 1.002 | 0.798 |
| 30 | 24.00 dB | 0.500 | 1.599 |

The prediction is tested directly by measuring the compressed pulse's own FWHM
for the attenuated waveform at each path:

| path (m) | compressed FWHM (ms) | resolution (m) | two reflectors 0.6 m apart |
|---|---|---|---|
| 0 | 0.2900 | 0.2320 | resolved |
| 10 | 0.3300 | 0.2640 | resolved |
| 30 | 0.4700 | 0.3760 | resolved |
| 60 | 0.9300 | 0.7440 | **not resolved** |
| 100 | 1.3900 | 1.1120 | **not resolved** |

**Two reflectors that are trivially separated at the seabed merge into one by
60 m of path**, because the pulse that returns has lost its high frequencies.
Note the two tables disagree in detail — the half-power bandwidth predicts a
factor-8 degradation at 30 m where the measured FWHM degrades by only $1.6$ —
and the reason is instructive: the half-power width discards the low-amplitude
high-frequency content that still sharpens the correlation peak. **The measured
FWHM is the honest number; the half-power bandwidth is a convenience.**

This is the lesson's central teaching point in quantitative form: **a sub-bottom
system does not have a resolution, it has a resolution at a depth.** The
demonstration supplies both the wrong-but-instructive estimate and the right one.

## 7. Assumptions and regime of validity

1. **A single, known attenuation law.** Real sediment attenuation depends on
   grain size, porosity and gas content, and it is *depth*-dependent within the
   sediment, not just path-dependent. The demonstration's law is a shape.
2. **A layered, one-dimensional model.** No lateral variation, no diffractions,
   no three-dimensional scattering.
3. **A replica matched to the returned waveform.** The demonstration's Section 6
   assumes the replica is adjusted for the expected attenuation, which is the
   ideal case. Real processing uses a fixed reference and therefore suffers both
   the resolution loss and a mismatch loss.
4. **No source or receiver directivity.** A real transducer's beam pattern is
   frequency-dependent, so the effective bandwidth depends on angle as well as on
   depth.
5. **No multiple reflections.** In shallow water the seafloor-to-surface multiple
   appears within the sub-bottom record and is a first-order interpretation
   hazard.
6. **White noise.** Real noise is coloured; the band-rejection component of the
   processing gain is smaller than the ideal.
7. **No dispersion.** Velocity dispersion accompanies attenuation in real
   sediments (they are a Kramers-Kronig pair); it is omitted here.

## 8. Worked examples

### Example 1 — the resolution of a different chirp

A chirp sweeps $1.5\ \mathrm{kHz}$ to $5.5\ \mathrm{kHz}$ over $12\ \mathrm{ms}$ in
a sediment of $v = 1550\ \mathrm{m\,s^{-1}}$.

$$B = 4.0\ \mathrm{kHz}, \qquad
\Delta z = \frac{c}{2B} = \frac{1550}{2 \times 4000} = 0.194\ \mathrm{m},$$

$$BT = 4000 \times 0.012 = 48, \qquad
G = 10\log_{10}(F_s T) = 10\log_{10}(100000 \times 0.012) = 30.8\ \mathrm{dB}.$$

**The resolution depends only on $B$**, which is why a longer sweep at the same
bandwidth costs nothing in resolution; and the gain depends only on $T\,F_s$,
which is why it grows with duration.

### Example 2 — how much dynamic range does a target need?

A layer at $40\ \mathrm{m}$ below the seabed must be seen with $10\ \mathrm{dB}$ of
margin above the noise. The two-way loss from the transmission coefficient and the
attenuation at $4\ \mathrm{kHz}$ ($\alpha = 0.4\ \mathrm{dB\,m^{-1}}$) is

$$\mathrm{loss} = 2\alpha R = 2(0.4)(40) = 32\ \mathrm{dB},$$

plus the reflection loss. If the layer's reflection coefficient is $-20\ \mathrm{dB}$
and $10\ \mathrm{dB}$ of margin is required, the system must deliver
$62\ \mathrm{dB}$ of echo level before processing. The matched filter's
$33\ \mathrm{dB}$ of gain then leaves a comfortable margin — which is exactly how a
chirp turns an impossible target into a routine one.

### Example 3 — the cost of the Hann taper

Moving from rectangular to Hann taper: main lobe $0.2900 \to 0.5500\ \mathrm{ms}$
($\times 1.90$), side lobe $-13.57 \to -26.10\ \mathrm{dB}$. In range terms the
resolution goes from $0.232\ \mathrm{m}$ to $0.440\ \mathrm{m}$ — still better than
half a metre. **The taper costs a factor 1.9 and buys 12.5 dB of dynamic range
between adjacent events.** For a target at $0.5\ \mathrm{m}$ spacing the taper is
free; for one at $0.2\ \mathrm{m}$ it is not affordable.

## 9. Python demonstration

`code/sub_bottom_profiling_demo.py` prints everything above with units:

1. the chirp, its spectrum and the energy inside the band, for two tapers;
2. the matched-filter output for an isolated interface, with its measured FWHM
   and resolution against $c/(2B)$;
3. the same duration as a continuous-wave pulse, for comparison;
4. the side-lobe/width trade for a rectangular and a Hann taper;
5. the processing gain, measured against its three-term decomposition;
6. the penetration limit against frequency and dynamic range;
7. the resolution degradation with path, from the half-power bandwidth and from
   the measured compressed FWHM.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sub_bottom_profiling_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/04-sub-bottom-profiling-exercises.md`](exercises/04-sub-bottom-profiling-exercises.md)
and
[`exercises/04-sub-bottom-profiling-solutions.md`](exercises/04-sub-bottom-profiling-solutions.md).

- ★ Compute the sweep rate, $BT$ and $c/(2B)$ for a $1$–$8\ \mathrm{kHz}$ chirp of
  $15\ \mathrm{ms}$ in a sediment of $1700\ \mathrm{m\,s^{-1}}$.
- ★★ Derive the matched filter's gain under the two SNR definitions used in the
  lesson, and show that it is $\sqrt{N}$.
- ★★ Compute the penetration for $60\ \mathrm{dB}$ dynamic range at $3\ \mathrm{kHz}$
  and $6\ \mathrm{kHz}$ under the linear attenuation law, and state the trade.
- ★★★ Design a survey that resolves a $0.3\ \mathrm{m}$ layer at $25\ \mathrm{m}$
  below the seabed, and state which of the four constraints (bandwidth,
  attenuation, energy, side lobes) binds.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use
$c_{\text{sed}} = 1600\ \mathrm{m\,s^{-1}}$, $F_s = 100\ \mathrm{kHz}$,
$\alpha(f) = 0.1\,(f/\mathrm{kHz})\ \mathrm{dB\,m^{-1}}$ one-way.

> A chirp sweeps $2.5\ \mathrm{kHz}$ to $7.5\ \mathrm{kHz}$ in $30\ \mathrm{ms}$.
> **(a)** Compute $B$, $T$, $BT$ and the resolution in the sediment.
> **(b)** Compute the number of samples $N$ and the matched filter's gain in dB.
> **(c)** Compute the two-way loss at $3\ \mathrm{kHz}$ over $20\ \mathrm{m}$ of
> penetration and over $50\ \mathrm{m}$.
> **(d)** Compute the extra two-way loss at $7.5\ \mathrm{kHz}$ relative to
> $2.5\ \mathrm{kHz}$ over $20\ \mathrm{m}$ of path, and state what such a
> differential loss does to the effective bandwidth. Then state which estimate of
> the resulting resolution degradation you would quote — the half-power-bandwidth
> one, or the measured compressed FWHM — and why.

A worked version of (a)–(d) is in the lesson-04
[solutions](exercises/04-sub-bottom-profiling-solutions.md).

## Common pitfalls

1. **Quoting one resolution for the instrument.** Section 6: it degrades by a
   factor 4.8 over 100 m of path.
2. **Confusing duration with resolution.** The resolution is $c/(2B)$; a longer
   sweep at the same bandwidth does not worsen it.
3. **Ignoring side lobes.** A $-13.6\ \mathrm{dB}$ side lobe is $21\,\%$ of the
   main peak and is routinely mistaken for a reflector.
4. **Attributing the whole processing gain to the chirp.** Two of the three
   terms in Section 4 are not chirp-specific.
5. **Assuming the half-power bandwidth is the resolution.** Section 6 shows it
   over-predicts the degradation; measure the FWHM.
6. **Forgetting the transmission loss at the seabed.** The reflection coefficient
   subtracts tens of decibels before any attenuation is counted.
7. **Using a fixed replica.** A mismatched filter loses both amplitude and
   resolution; the demonstration's Section 6 assumes matching for the expected
   attenuation, which is the optimistic case.

## Related modules

- [01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the same convolutional model at a much lower frequency, with kilometres of
  penetration instead of metres.
- [03 Side-Scan Sonar and Seafloor Imaging](03-side-scan-sonar.md) —
  the same pulse-length trade, and the same seabed, imaged for texture rather
  than for layers.
- [Module 15-06 Sea Level Change and Marine Records](../06-sea-level-change-marine/README.md) —
  the palaeo-record that a sub-bottom profile samples.
- [20-04 Deconvolution and Inverse Filtering](../../20-signal-processing/04-deconvolution-and-inverse-filtering/README.md) —
  the general theory of which a matched filter is the simplest case.
- [02-03-10 Attenuation and Quality Factor](../../02-physics/03-oscillations-and-waves/10-attenuation.md) —
  the physical basis of $\alpha(f)$.

## Self-assessment checklist

- [ ] I can construct a chirp and state its $B$, $T$ and $BT$.
- [ ] I can derive and measure the compressed resolution.
- [ ] I can compare a chirp with a CW pulse quantitatively.
- [ ] I can measure a side-lobe level and a main-lobe width and state the trade.
- [ ] I can account for the processing gain in its three parts.
- [ ] I can compute a penetration limit and state the resolution trade.
- [ ] I can measure how resolution degrades with path and say why.
