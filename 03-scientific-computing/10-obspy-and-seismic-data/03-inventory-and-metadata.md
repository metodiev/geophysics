---
id: 03-10-03
title: "StationXML Inventory, Response and Instrument Correction"
level: advanced
prereqs: ["03-10-02", "03-03-05"]
tags: [obspy, stationxml, instrument-response, deconvolution, water-level]
---

# StationXML Inventory, Response and Instrument Correction

A seismogram in counts is not ground motion. The step that turns one into the
other — deconvolution of the instrument response — is the step where most
published amplitude errors are introduced, because the deconvolution is
ill-conditioned at low frequency and every implementation must choose how to
stabilise it. This lesson builds an instrument from its poles and zeros,
measures its response, inverts it, and measures exactly what the stabilisation
costs.

Run the demonstration before reading on; every number below is its output.

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/inventory_and_metadata_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** an `Inventory` in memory containing a `Station`, a `Channel` and
   a pole-zero `Response`, and state what each field means.
2. **Measure** $|H(f)|$ from the response object and check it against the
   analytic pole-zero expression, including the low-frequency asymptote.
3. **Explain** why two zeros at the origin produce a 40 dB/decade roll-off
   below the corner frequency and a flat velocity response above it.
4. **Perform** a forward model (ground motion → counts) and the inverse
   (counts → ground motion), and quantify the recovery.
5. **Explain** what the water level clamps, compute the frequency at which the
   clamp acts, and choose a level from the lowest frequency you need.
6. **Diagnose** a sensitivity mismatch caused by a wrong normalisation factor,
   and state why a validator flags it.

## Prerequisites

- [03-10-02 Reading MiniSEED/SAC](./02-reading-waveforms.md) — counts on disk
  and why the transfer function is not in the file.
- [03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../03-scipy/05-signal.md)
  — the frequency-domain operations inside `remove_response`.

## 1. Intuition: a filter you cannot switch off

Every seismometer is a mechanical filter. A geophone's coil moves relative to
its case; above the corner frequency the output voltage is proportional to
ground *velocity*, below it the response falls off as frequency squared. A
digitizer then samples that voltage. The chain therefore multiplies the ground
motion's spectrum by a frequency-dependent factor, and to recover ground motion
you must divide by it.

Dividing is where the trouble starts. Below the corner frequency the factor
tends to zero, so its reciprocal tends to infinity, and any noise in the
recording is amplified without limit. The physics is unambiguous; the
numerics are not, and the standard remedy — a *water level* — is a numerical
choice that leaves a physical fingerprint. This lesson measures that
fingerprint.

## 2. Precise definitions

### 2.1 The pole-zero response

A linear time-invariant instrument is described by a Laplace-domain transfer
function

$$H(s) = A_0\, G \,
\frac{\prod_{k=1}^{n_z}(s - z_k)}{\prod_{k=1}^{n_p}(s - p_k)},
\qquad s = \mathrm{i}\omega, \quad \omega = 2\pi f,$$

where $z_k$ are the zeros, $p_k$ the poles, $G$ the stage gain (counts per
m/s here) and $A_0$ the **normalisation factor** chosen so that the analogue
part has unit magnitude at the normalisation frequency $f_n$:

$$A_0 = \left|\frac{\prod_k (s_n - p_k)}{\prod_j (s_n - z_j)}\right|,
\qquad s_n = \mathrm{i}2\pi f_n.$$

Units: $H$ carries the units of $G$, i.e. counts per (m/s). Frequencies are in
Hz, poles and zeros in rad/s, and $A_0$ is dimensionless. Phase is in radians
and is only meaningful relative to the definition of $s$.

For the geophone used here, $f_0 = 1.0$ Hz, damping $\zeta = 1/\sqrt2$, two
zeros at the origin and a conjugate pole pair at
$-4.4429 \pm 4.4429\,\mathrm{i}$ rad/s (the demonstration prints the exact
values). The zeros at the origin are what make the response fall as $f^2$ at
low frequency; the pole pair places the corner.

### 2.2 StationXML

`StationXML` is the XML schema in which FDSN services deliver metadata. Its
hierarchy mirrors the data:

```
Inventory
└── Network (code, time window)
    └── Station (code, latitude, longitude, elevation, time window)
        └── Channel (code, location, sample rate, time window, azimuth, dip)
            └── Response (stages, sensitivity, input and output units)
```

A `Response` is a list of **stages**. Each stage has a gain and a filter
(pole-zero analogue, FIR coefficients, or a response list). The product of the
stage gains is the overall sensitivity, provided every pole-zero stage is
normalised to unity at the frequency where the overall sensitivity is defined.

### 2.3 Sensitivity versus full response

Let $H(f)$ be the full complex response in counts per (m/s) and let
$S$ be the overall sensitivity in counts per (m/s) at a reference frequency
$f_s$. Removing the sensitivity alone gives

$$v_{\text{approx}}(t) = \frac{\text{counts}(t)}{S},$$

which equals the true velocity only where $|H(f)| = S$. Removing the full
response gives

$$\hat v(t) = \mathcal{F}^{-1}\!\left[\frac{\tilde c(f)}{H(f)}\right],$$

which is correct at every frequency. For the demonstration's geophone the two
differ by the factor measured in the output:

```
remove_sensitivity peak       : 1.410627e-04 m/s
true peak                      : 9.974800e-05 m/s
ratio                          : 1.4142
```

$1.4142 = \sqrt2$, and the reason is that $|H|$ flattens at
$7.2125\times10^8$ counts per m/s while the nominal sensitivity at 1 Hz is
$5.1\times10^8$; their ratio is exactly $\sqrt2$. A sensitivity-only
correction is wrong by a constant factor here and by a frequency-dependent
factor for a broadband instrument.

## 3. Derivations and worked reasoning

### 3.1 The response is a ratio of distances in the complex plane

Write $H(\mathrm{i}\omega) = A_0 G \prod (\mathrm{i}\omega - z_k)/\prod(\mathrm{i}\omega - p_k)$.
Each factor $|\mathrm{i}\omega - a|$ is the distance from the point
$\mathrm{i}\omega$ on the imaginary axis to the singularity $a$. Two
consequences follow immediately and are worth checking against the measurement:

- A zero at the **origin** gives $|\mathrm{i}\omega| = \omega$, so each such
  zero multiplies $|H|$ by $\omega$: a factor 10 per decade. Two zeros give
  $f^2$, i.e. 40 dB per decade.
- At high frequency, $|\mathrm{i}\omega - a| \to \omega$ for both poles and
  zeros, so with $n_z = n_p$ the response flattens.

The demonstration measures the slope numerically rather than asserting it:

```
log-log slope, 0.004-0.02 Hz : 2.0000 decades/decade
log-log slope, 5-45 Hz       : +0.000118 decades/decade (flat passband)
```

The first value is exactly 2.0000 because the two frequencies are far below
the corner, where the pole distances are almost constant. The second is
$+1.2\times10^{-4}$ decades per decade — zero to three decimal places.

### 3.2 The corner frequency is where the two asymptotes meet

The low-frequency asymptote is $|H| \propto f^2$; the high-frequency asymptote
is $|H| \to |H(\infty)|$. Where they meet, $|H| = |H(\infty)|$, and for a
critically damped geophone the -3 dB point coincides with the corner:

```
|H(f0)| = |H(1.00 Hz)|     : 5.100000e+08 counts per m/s
flat level |H(inf)|        : 7.212250e+08 counts per m/s
ratio |H(f0)| / |H(inf)|   : 0.707130   (1/sqrt(2) = 0.707107)
```

The measured ratio is $0.70713$ against $1/\sqrt2 = 0.70711$; the difference is
the finite frequency spacing of the evaluation grid, not a discrepancy.

### 3.3 Forward modelling, done honestly

To test an inverse you need a forward model you can trust. The demonstration
does not convolve in the time domain; it multiplies in the frequency domain by
the *same* response object that `remove_response` will use, evaluated on the
*same* transform length:

```python
nfft = _npts2nfft(NPTS)                      # ObsPy's own choice of length
h, freqs = resp.get_evalresp_response(1.0/FS, nfft, output="VEL")
counts_true = np.fft.irfft(np.fft.rfft(v_true, n=nfft) * h, n=nfft)[:NPTS]
```

Using ObsPy's `_npts2nfft` matters: the deconvolution uses a transform length
that is a smooth number $\ge$ `npts` (12000 here, not 6000), and a forward
model built on a different grid would differ from the inverse at the edges for
reasons that have nothing to do with the physics. The demonstration prints

```
nfft used by remove_response  : 12000 samples (next smooth number >= npts)
```

and adds 0.5 counts RMS of noise plus one-count quantisation, so the inverse
problem is realistic. The ground motion is a 5 Hz wave packet of 102.7 µm/s
peak plus a 50 mHz signal of 5.0 µm/s; in counts the packet reaches 71 942 and
the long-period signal is invisible.

### 3.4 The water level, exactly

ObsPy's `invert_spectrum` computes

$$H_{\text{lim}}(f) = \max\!\big(|H(f)|,\ |H|_{\max}\,10^{-w/20}\big)$$

and then uses $1/H_{\text{lim}}$ with the *phase of $H$* preserved. The clamp
frequency $f_c$ is where $|H(f_c)| = |H|_{\max}10^{-w/20}$, and the
demonstration solves for it by interpolation at each water level. The measured
table is:

| water level (dB) | clamp $f_c$ (Hz) | recovered 50 mHz amplitude (µm/s) | error | 2–20 Hz RMS (µm/s) |
|---|---|---|---|---|
| 20 | 0.31702 | 0.1243 | −97.51 % | 11.1952 |
| 40 | 0.10000 | 1.2293 | −75.41 % | 11.1952 |
| 54 | 0.04449 | 4.8217 | −3.57 % | 11.1952 |
| 60 | 0.03143 | 5.2427 | +4.85 % | 11.1952 |
| 66 | 0.02203 | 5.5798 | +11.60 % | 11.1953 |
| 80 | 0.00956 | 6.7951 | +35.90 % | 11.1965 |
| 100 | 0.00120 | 7.4635 | +49.27 % | 11.1976 |

The true long-period amplitude is 5.0000 µm/s. Reading the table:

- **Below 54 dB the signal is attenuated**, because the clamp frequency sits
  *above* the signal frequency: the deconvolution cannot amplify what the
  clamp has flattened.
- **At 54 dB the error is −3.6 %**, the best in the sampled set.
- **Above 60 dB the estimate grows without bound**, reaching +49 % at 100 dB.
  The extra energy is the amplified half-count noise below the corner.
- **The 2–20 Hz band is unchanged** from 20 dB to 80 dB, and moves only in the
  fifth digit by 100 dB: the water level acts only where $|H|$ is small.

The design rule that follows, and it is the whole point: **choose the water
level so that the clamp frequency lies below the lowest frequency you intend to
keep.** For a 1 Hz geophone and a 50 mHz target, that means 54–60 dB. For a
broadband sensor with a 120 s corner, 60 dB would be far too low.

### 3.5 A pre-filter is the better tool

The water level is a blunt instrument: it protects the low frequencies by
distorting them. A `pre_filt`, applied as a cosine taper on the data spectrum
before division, removes the frequencies you do not want instead of clamping
them. Measured at 60 dB:

```
water_level=60, no pre_filt  : low-f (<0.04 Hz) RMS    0.7816 um/s, 2-20 Hz RMS  11.1952 um/s
water_level=60, pre_filt     : low-f (<0.04 Hz) RMS    0.2313 um/s, 2-20 Hz RMS  11.1952 um/s
true 2-20 Hz RMS             :                                        2-20 Hz RMS  11.1952 um/s
```

The pre-filter cuts the sub-0.04 Hz RMS by a factor of 3.4 while leaving the
signal band bit-identical at this precision. `pre_filt=(0.02, 0.04, 8, 10)` for
a 1 Hz geophone is the standard starting point: pass 1–8 Hz, taper in the two
transition bands, remove everything the instrument cannot support.

### 3.6 The normalisation factor is not decoration

Build the same instrument with $A_0 = 1$ instead of $1.414214$ and ObsPy
derives an overall sensitivity of $3.60624\times10^8$ counts per m/s where the
stage gain says $5.1\times10^8$:

```
Overall Sensitivity: 3.60624e+08 defined at 1.000 Hz
with A0 = 1.414214: overall sensitivity = 5.100000e+08 counts per m/s
```

A StationXML validator flags the mismatch between the declared sensitivity and
the product of stage gains. If nothing flags it, the effect is a 1.41×
amplitude error that no plot will reveal. Note that `remove_response` remains
*correct* with a wrong $A_0$, because it divides by the full response including
$A_0$; what breaks is every consumer that trusts the sensitivity number alone —
which includes most quick-look tools.

## 3b. Worked examples

### 3b.1 Choosing a water level from the target frequency

**Problem.** A 1 Hz geophone records a local event, and the analysis needs the
signal between 0.2 and 5 Hz. What water level should be used, and how do you
know it is right?

The rule is that the clamp frequency $f_c$ must fall below the lowest frequency
you intend to keep, so $f_c < 0.2$ Hz. From the measured $|H(f)|$ table,
$|H(0.2\ \mathrm{Hz})| \approx 5.0\times10^{7}$ counts per m/s (interpolating
between 0.1 Hz at $7.21\times10^{6}$ and 0.5 Hz at $1.75\times10^{8}$), while
$|H|_{\max} = 7.2125\times10^{8}$. The required water level is therefore

$$w = -20\log_{10}\frac{|H(f_c)|}{|H|_{\max}}
= -20\log_{10}\frac{5.0\times10^{7}}{7.2125\times10^{8}}
= -20\log_{10}(0.0693) = +23.2\ \mathrm{dB}.$$

So 24 dB suffices — *less* than the 60 dB default. Using 60 dB would clamp at
0.031 Hz, well below the target, and amplify half-count noise there for no
benefit. **A lower water level than the default is often the correct answer**,
and it is only available if the target band is stated before the deconvolution.

Verification: run the sweep, measure the recovered amplitude of a known signal
at 0.2 Hz, and confirm it is within a few per cent. That is the same
measurement the demonstration performs at 50 mHz, and 54 dB was its best value.

### 3b.2 Diagnosing a response that looks wrong

**Problem.** A station's deconvolved velocity has a permanent DC offset and a
low-frequency wander. List the causes in the order of probability, with the
measurement that distinguishes them.

| cause | measurement that identifies it |
|---|---|
| wrong water level (too high) | the wander's amplitude falls as the water level falls; the clamp frequency moves below the band of interest |
| no `pre_filt` | the wander is removed by a `pre_filt` that excludes the frequencies, without changing the signal band |
| NO_INPUT/NO_OUTPUT metadata wrong | the recovered amplitudes are wrong by a *constant* factor at every frequency — the ratio $\lvert H(\omega)\rvert/\lvert H_{\text{true}}\rvert$ is flat |
| wrong $A_0$ | the amplitudes are wrong by a constant factor, and the overall sensitivity disagree with the stage gains — measurable: `5.1e8` vs `3.60624e8`, a factor 1.4142 |
| the sensor is a displacement sensor, not a velocity sensor | the factor is *frequency-dependent*, varying as $f$ or $f^2$ across the band |

The discriminator between the last three is whether the error is constant or
frequency-dependent. A constant factor is a scaling error (metadata); a
frequency-dependent one is a shape error (the wrong pole-zero model or the wrong
output type). The demonstration's `remove_sensitivity` versus `remove_response`
comparison is exactly this test: the ratio is 1.4142 at high frequency, because
the sensitivity-only correction applies a constant where the response varies.

### 3b.3 The cost of getting the normalisation wrong in a published amplitude

**Problem.** A study reports a peak ground velocity of 1.41 mm/s for a local
event using `remove_response` with an `Inventory` whose $A_0 = 1.0$ instead of
the correct 1.414214. Is the report wrong?

**No** — and this is the subtle part. `remove_response` divides by the *full*
response including $A_0$, so the frequency-dependent shape is applied correctly.
The derived overall sensitivity is what disagrees with the stage gains (measured:
$3.60624\times10^8$ instead of $5.1\times10^8$), and any consumer that reads the
sensitivity *alone* will be wrong by 1.41×.

So the failure mode is not in the reported number but in the chain of custody:
a station metadata record with an inconsistent sensitivity propagates the
inconsistency to every downstream user who trusts the scalar. The measurement
that detects it is a one-line comparison:

$$\left|\frac{S_{\text{declared}}}{\prod \text{stage gains}}\right| = 1
\quad\text{within a few per cent.}$$

If it is not, the metadata is wrong even though the waveform looks fine.

### 3b.4 What "instrument-corrected" does and does not mean

**Problem.** After `remove_response(output="VEL")`, what has been established
and what has not?

**Established:** the samples are now in metres per second, up to the accuracy of
the response used; the phase distortion of the instrument has been removed
within the same band; and the amplitude at every frequency inside the
deconvolution's valid band is a physical quantity.

**Not established:**

- **The band.** Outside $[f_c, f_{\text{Nyquist}}]$ the result is not a
  measurement. Measured: at a 60 dB water level the clamp acts below 0.031 Hz,
  and the recovered long-period amplitude is 8.4 % low there and 68 % high at
  100 dB in the demonstration's configuration.
- **The noise.** Deconvolution amplifies whatever is in the record, including
  half a count of quantisation noise, by $1/|H(f)|$.
- **The instrument.** A wrong pole-zero model produces a wrong answer that is
  internally consistent — the trace looks physical at every frequency.
- **The site.** No correction for soil response, tilt, or instrument–ground
  coupling is included. "Ground motion" means at the sensor's base plate, and
  the difference between that and free-field motion is a separate problem.

## 4. Physical and computational interpretation

The instrument response is a property of hardware, and its inverse is a
property of the noise in the record. That asymmetry is the whole difficulty:

- With a perfect, noise-free recording, **any** water level is defensible,
  because the clamp never acts where the signal is.
- With real data, the choice of water level determines the lowest frequency at
  which the recovered ground motion is a measurement rather than an
  amplification of noise.
- The right question is not "what water level?" but "what is the lowest
  frequency I can defend?", and the answer follows from the noise spectrum.

## 5. Python demonstration

[`code/inventory_and_metadata_demo.py`](./code/inventory_and_metadata_demo.py)
builds the inventory, verifies the response against its own analytic form,
runs the forward and inverse models, sweeps the water level and the noise
level, and demonstrates the wrong-$A_0$ failure. It needs no network.

Two habits to take from it:

1. **Build an inventory in memory when you are testing.** Thirty lines give
   you an instrument whose response you know exactly, which is the only way to
   measure an inverse.
2. **Interpolate the clamp frequency.** Never quote a water level without
   stating the frequency at which it starts to act.

## 6. Exercises

Full solutions:
[`exercises/03-inventory-and-metadata-solutions.md`](./exercises/03-inventory-and-metadata-solutions.md).

### ★ Foundational

**★1.** State the units of $H(f)$, of $G$, of $A_0$ and of $f$.

**★2.** A response has two zeros at the origin. Compute $|H(0.01\ \mathrm{Hz})|/|H(0.1\ \mathrm{Hz})|$
in the low-frequency limit and check it against the measured slope of 2.0000
decades per decade.

**★3.** The demonstration reports $|H(f_0)|/|H(\infty)| = 0.707130$ against
$1/\sqrt2 = 0.707107$. Explain the 0.003 % difference.

**★4.** Explain in one sentence each what `remove_sensitivity` and
`remove_response` do, and state the ratio the demonstration measures between
them.

### ★★ Applied

**★★5.** From the measured table, state the water level that minimises the
error in the 50 mHz amplitude, and give the error. Then compute the clamp
frequency for 57 dB by interpolating the measured $|H(f)|$ table (or by
running the demo with that level) and state whether 57 dB would be better than
54 dB for a target at 50 mHz.

**★★6.** A broadband sensor has a 120 s corner frequency (8.3 mHz). Argue,
using the clamp-frequency rule, what water level is needed to recover a
20 mHz signal, and why a user who leaves the default 60 dB would report an
amplitude that is too small.

**★★7.** Reconstruct the derivation of $A_0$ for the demonstration's
instrument: evaluate $|\mathrm{i}2\pi f_n - p_1||\mathrm{i}2\pi f_n - p_2|/|\mathrm{i}2\pi f_n|^2$
at $f_n = 1$ Hz and show that the result is 1.414214.

**★★8.** The demonstration adds 0.5 counts RMS of noise. Re-run the water-level
sweep with 5 counts RMS and report how the best water level changes. State the
general rule in one sentence.

### ★★★ Research-oriented

**★★★9.** Build a second instrument with $f_0 = 0.05$ Hz and the same damping
and sensitivity, then repeat the water-level sweep. Report the clamp frequency
and the best water level for a 50 mHz target, and compare with the 1 Hz
geophone. State the design implication for a station whose target is
long-period surface waves.

**★★★10.** The demo's sensitivity-only correction is wrong by exactly
$\sqrt2$. Find an instrument geometry for which it is wrong by a *frequency-
dependent* factor, measure the resulting waveform distortion (peak ratio and
RMS error in a signal band), and explain why the error cannot be represented by
a single number.
