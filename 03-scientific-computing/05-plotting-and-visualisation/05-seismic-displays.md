---
id: 03-05-05
title: "Seismic Displays: Wiggle, Variable-Density and Colormaps"
level: advanced
prereqs: ["03-05-02", "20-02-01", "06-01-04"]
estimated_minutes: 75
tags: [seismic, wiggle, variable-density, colormaps, polarity, amplitude]
---

# Seismic Displays: Wiggle, Variable-Density and Colormaps

Reflection seismic data are a two-dimensional array indexed by trace and by time,
and the way that array is displayed is not a neutral act. The eye is asked to
judge continuity, polarity, amplitude and geometry simultaneously, and each of
those judgements depends on a display parameter: the trace spacing, the gain, the
clip level and the palette. Change any one of them and a different geological
story becomes easy to tell.

This lesson treats the seismic display as a measurement instrument with stated
settings. The arithmetic is simple; the discipline is in deciding and recording
the settings, and in understanding what each one hides.

## Learning objectives

By the end of this lesson you will be able to:

1. **Draw** a wiggle display with the conventional positive-lobe fill, and state
   the trace spacing at which the display stops being readable.
2. **Choose** a gain convention and explain the difference between a fixed scale, a
   time-varying gain and automatic gain control in terms of what physical
   amplitude information survives.
3. **Draw** a variable-density display with an amplitude scale that is symmetric
   about zero, and justify the symmetry from the physics of a reflection
   coefficient.
4. **Select** a clip level from the amplitude distribution, and **quantify** how
   many samples saturate at that level and how much dynamic range is compressed.
5. **State** the polarity convention on the figure, and demonstrate why a figure
   without one cannot be compared with any other.
6. **Combine** wiggle and variable-density displays, and say what the overlay buys
   and what it costs.

## Prerequisites

- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — amplitude, sign and the difference between a value and its uncertainty.
- [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../../20-signal-processing/02-fourier-and-spectral-analysis/01-dft-fft-practice.md)
  — the wavelet and its spectrum, and why a zero-phase wavelet is symmetric.
- [06-01-04 Reflected, Refracted and Converted Body Waves](../../06-seismology/01-elastic-wave-propagation/04-body-wave-arrivals.md)
  — what a reflection coefficient is and why it carries a sign.

## 1. What the data are

A seismic section is an array $a(t, x)$ of samples, usually of the vertical
component of particle velocity or of pressure, after processing. It is a
zero-mean oscillation: every reflection is a wavelet with a positive and a
negative lobe, and the *sign* of the leading lobe carries the sign of the
reflection coefficient.

The demonstration builds a synthetic section from a stated model: three horizons
(two dipping, one flat), reflection coefficients $+1.0$, $-0.7$ and $+0.55$,
convolved with a 28 Hz Ricker wavelet at a 2 ms sample interval. Its amplitude
statistics are printed before any display choice is made:

```text
  section: 420 samples x 120 traces, dt = 2 ms
  mean  = +0.000092   median = +0.000000
  std   = 0.147212
  samples with |a| exactly 0: 65.18 %  (the gaps between wavelets)

  statistics of the NONZERO amplitudes, i.e. of the wavelets
    percentile    of nonzero |a|
          50.0          0.008555
          90.0          0.408570
          99.0          0.909507
          99.5          1.000000

  largest |a| in the whole section: 1.550000
```

Read three things from this. The mean is $9\times10^{-5}$, five orders of
magnitude below the largest amplitude, so the section is zero-mean to numerical
precision. Most samples are exactly zero, because a wavelet occupies a small part
of each trace. And the distribution of nonzero amplitudes has a very long tail:
the largest is 1.55 while the median nonzero amplitude is 0.0086, a ratio of 181.
**Every display decision in this lesson is a decision about how to fit that tail
onto a colour scale.**

## 2. Wiggle displays

The wiggle display draws each trace as a curve displaced horizontally in
proportion to amplitude, with the area between the curve and the trace baseline
filled where the amplitude is positive (by the most common convention; some
conventions fill the negative lobe, which is another reason to state polarity).

The demonstration draws 60 traces across 6.4 in:

```text
  60 traces across 6.4 in of figure width
    trace spacing = 2.71 mm  (7.7 pt)
    peak amplitude scaled so one full swing = one trace spacing
    scale factor applied: 0.58 per unit amplitude
  saved 05_wiggle.png  (150 dpi)
```

The scaling rule is the important line: the peak amplitude is scaled so that one
full swing occupies one trace spacing. That is the convention that keeps adjacent
traces from interpenetrating. Beyond about one trace spacing per swing the traces
overlap, and the eye can no longer distinguish a single large event from two
adjacent medium ones — the classic "wiggle spaghetti".

The demonstration quantifies the limit for a denser display: at 300 traces across
the same width the spacing is 0.54 mm, and the display is decorative rather than
quantitative. That is the regime in which variable density takes over, because a
raster can show 300 traces per centimetre while a wiggle cannot.

### 2.1 Gain, and what it does to amplitude

A wiggle display needs a scale factor. Three conventions are common, and they make
different physical claims:

| Convention | Scale factor | Physical information |
|---|---|---|
| Fixed | one constant for the whole section | true relative amplitudes between shallow and deep events are preserved |
| Time-varying gain | a function of $t$, e.g. $t$ or $t^2$ | compensates geometric spreading and attenuation; relative amplitudes within a time window survive, between windows they do not |
| Automatic gain control | computed in a sliding window per trace | continuity and geometry are maximised, absolute amplitude is destroyed |

AGC is the most seductive because it makes every event visible, and the most
dangerous because it makes every event look equally strong. It is legitimate for
picking a horizon and illegitimate for an amplitude-versus-offset argument.
Whichever convention is used, it belongs in the caption — a seismic figure with an
unstated gain is a figure whose amplitudes cannot be used for anything.

## 3. Variable-density displays and the clip level

A variable-density display maps amplitude to colour. Because the amplitude is a
signed, zero-mean oscillation whose sign is physically meaningful, the palette must
be **diverging and symmetric about zero**: two hues for the two polarities and a
neutral colour at exactly zero. This is the argument of
[06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
applied to a specific dataset, and it is not a preference: a reflection
coefficient of zero means no contrast and no reflection, so zero is the physically
privileged value that must receive the neutral colour.

The amplitude scale is set by a **clip level**: amplitudes beyond $\pm c$ saturate
at the extreme colours. The demonstration compares three choices:

```text
  clip level                   value   saturated %   clip / p99 (dB)
  0.25 x max (too tight)     0.38750         4.220             -5.14
  p99 (conventional)         0.70000         1.012              0.00
  max (too loose)            1.55000         0.002              6.90
```

The trade is now explicit. A tight clip at a quarter of the maximum puts 4.220 % of
samples at the extreme colour: within those samples every amplitude difference is
gone, and they are precisely the strong, laterally continuous reflections that
carry the interpretation. A loose clip at the maximum saturates only the single
largest sample but compresses every event by 6.90 dB relative to the 99th
percentile, so the reflectors appear weak and the fine detail collapses into the
neutral colour.

The conventional choice — a percentile around the 99th, or a multiple of the RMS
amplitude — is a compromise that must be stated. A clip level quoted in the
caption ("amplitudes clipped at $\pm 0.7$, 1.012 % of samples saturated") converts the
display into a measurement; an unquoted clip level makes the figure
non-comparable with any other figure, including one made from the same data by a
different processor.

### 3.1 The same data at three clip levels

`05_clip_levels.png` draws the identical section three times at
$\pm0.25\,a_{\max}$, $\pm p_{99}$ and $\pm a_{\max}$. The panel at the tight clip
shows high contrast on weak events and saturated bands where the strong
reflectors are, so a reflector that changes amplitude laterally appears to
have a hole in it. The panel at the maximum clip shows every sample truly and is
almost uniformly pale, because two or three samples set the scale for the whole
section.

## 4. Polarity: the convention that must be printed

The display's palette determines whether a positive sample is drawn as, say, blue
or red. Nothing in the numbers does: the convention is inherited from the
acquisition and processing (whether a positive reflection coefficient produces a
peak or a trough in the recorded trace, the "SEG normal" and "SEG reverse"
polarities).

The demonstration draws the identical section under `RdBu_r` and `RdBu`:

```text
  saved 05_polarity.png  (150 dpi, 2 panels)

  Nothing in either panel says which direction is 'a hard interface',
  because that convention is a property of the acquisition (whether a
  positive reflection coefficient maps to a peak or a trough), not of
  the numbers. Every seismic figure therefore needs its polarity
  convention printed on it, and a figure without one cannot be
  compared with any other figure.
```

Reversing the palette flips the apparent polarity of every event in the figure.
Since the sign of a reflection coefficient is how an interpreter distinguishes a
hard interface from a soft one — a distinction that changes the lithological
interpretation — a figure that does not state its polarity is unresolvable on the
single most important question it is asked.

The practical form of the statement is one line on the panel or in the caption:
"positive amplitude plotted as blue (SEG normal); a positive reflection
coefficient is a peak."

## 5. Symmetry about zero

The demonstration reports the two candidate scales:

```text
  data mean                = +0.000092
  symmetric clip about zero: [-1.5500, 1.5500]
  asym. percentile clip    : [-0.4653, 0.6648]
  relative asymmetry of the percentile clip: 17.65 %
```

The percentile-based clip is asymmetric by 17.65 % about zero. Used with a diverging
palette, that asymmetry moves the neutral colour away from the physical zero, so
every polarity judgement read from the figure is offset by that amount. The
symmetric clip about zero is the correct construction for a signed oscillation,
and the asymmetry measurement above is the check that it has been applied.

If the analysis is genuinely one-sided — an envelope, a root-mean-square amplitude,
a single-signed attribute such as similarity or coherence — the palette must be
sequential instead, and the neutral-colour-at-zero rule no longer applies. The
palette family follows the data's structure, not the discipline's habit.

## 6. Combined displays

Real interpretation displays often overlay wiggles on a variable-density
background: the raster carries continuity and the wiggle adds a quantitative
trace at a readable density. The demonstration draws every fourth trace of the 120
as an overlay:

```text
  saved 05_combined.png  (150 dpi)
```

The overlay works when the wiggle density is low enough to read — a few traces per
centimetre — and the background is drawn with a light palette so that the wiggles
remain the strongest marks on the page. If the wiggles are as dark as the raster's
extremes, the two encodings compete and the figure shows neither well.

## 7. Physical interpretation

Every display parameter in this lesson is a statement about which physical
amplitudes the figure can still distinguish. A reflection coefficient of $+0.2$ and
one of $+0.3$ correspond to different contrasts in acoustic impedance and hence to
different lithological transitions; whether a reader can see the difference depends
on the clip level, the gain and the palette, none of which is a property of the
rock.

The gain convention is the sharpest example. A fixed gain preserves the physical
ratio between a shallow and a deep reflection, which is what an
amplitude-versus-offset or a hydrocarbon-indicator argument needs. A time-varying
gain restores some of the amplitude lost to geometric spreading and transmission,
which is defensible if the correction matches the physics that removed it. AGC
forces every window to the same amplitude regardless of what was there, so after
AGC the amplitudes carry no physical information at all — the display shows
continuity, which is a geometric property, and nothing about reflectivity.

The symmetric clip has a physical justification that is unusually direct: a
reflection coefficient is signed, zero means no contrast, and the display must
therefore give zero the neutral colour. The demonstration measures what a
percentile clip does instead — 17.65 % asymmetry — and that number is the size of
the polarity error a reader would make. On a section whose interpretation rests on
which polarity marks a hard interface, an error of that size is not cosmetic.

Finally, the vertical axis: a two-way time axis is a property of the wavefield, a
depth axis is a property of the rock plus an assumed velocity model. The vertical
exaggeration of the depth axis and the accuracy of the velocity model are separate
errors that multiply, and both must be stated for a structural measurement to be
reproducible.

## 8. Assumptions and limits

- **The synthetic section is generated from a stated model**, so the effect of
  every display parameter can be checked against ground truth. Real sections have
  noise, multiples, migration artefacts and an unknown $\sigma$; the display
  discipline is unchanged, but the numbers are not transferable.
- **Zero-phase wavelets are assumed.** The symmetry argument applies to a
  zero-phase wavelet; a mixed-phase wavelet has an asymmetric leading lobe, and
  amplitude-versus-offset measurements do not have a well-defined peak to pick
  (see
  [20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls](../../20-signal-processing/02-fourier-and-spectral-analysis/01-dft-fft-practice.md)).
- **Clipping is not compression.** A clip saturates; a logarithmic or power
  stretch compresses while preserving order. The two are different operations and
  only the second is amplitude-informative.
- **A diverging palette needs a symmetric scale.** Any asymmetry moves the neutral
  colour off the physical zero — measured in §5 at 17.65 % for a percentile clip
  on this section.
- **`imshow` interpolates.** `interpolation="nearest"` shows samples as blocks;
  `"bilinear"` or `"bicubic"` smooths between them and can invent continuity that
  is not in the data. On a display used for interpretation, `"nearest"` is the
  conservative default, and any smoothing belongs in the caption.
- **Colour bars are not optional** on a variable-density display, and they must
  carry units — the physical quantity of the amplitudes, whether that is a
  dimensionless reflection coefficient or a scaled pressure.
- **Screen resolution is a real constraint.** A 300-trace display at 0.54 mm
  spacing is below the resolving power of most displays; if the figure is only
  ever seen on screen, plan the density for the screen, not for print.

## 9. Python demonstration

[`code/05_seismic_displays_demo.py`](./code/05_seismic_displays_demo.py) builds the
synthetic layered section, tabulates its amplitude statistics, draws the wiggle
display (`05_wiggle.png`, 150 dpi), the three-clip comparison
(`05_clip_levels.png`, 150 dpi), the wiggle-plus-density composite
(`05_combined.png`, 150 dpi) and the polarity pair (`05_polarity.png`, 150 dpi).
The outputs quoted in §1, §2, §3 and §5 are its actual output; the wiggle spacing
line is:

```text
  60 traces across 6.4 in of figure width
    trace spacing = 2.71 mm  (7.7 pt)
    peak amplitude scaled so one full swing = one trace spacing
    scale factor applied: 0.58 per unit amplitude
```

### What to observe

| Observation | Consequence |
|---|---|
| 65.18 % of samples are exactly zero | The dynamic range of interest lives in a third of the array, so percentile choices act on the wavelet population, not the whole section |
| Nonzero amplitudes span a factor of 181 | Linear mapping of that range to a colour scale is impossible without a clip |
| 4.220 % of samples saturate at the tight clip, 0.002 % at the maximum | The tight clip deletes the strongest events; the loose one compresses everything |
| The percentile clip is asymmetric by 17.65 % | A diverging palette centred on zero cannot be given a percentile scale unchanged |
| The maximum clip is 6.90 dB above p99 | An unquoted clip changes every apparent amplitude ratio by that factor |

> **Breaking exercise.** Change the generating wavelet frequency from 28 Hz to
> 45 Hz and re-run. Predict first how the fraction of exactly-zero samples, the
> 99th percentile of nonzero amplitude and the optimum clip level will each
> change, and explain which of the three changes is a property of the wavelet
> and which is a property of the display.

## 10. Common mistakes

1. **Quoting amplitudes from an AGC'd display.** AGC destroys absolute amplitude;
   the figure then cannot support an amplitude-versus-offset or
   bright-spot argument.
2. **A rainbow palette on a seismic section.** It has no neutral colour, so it
   cannot encode a sign, and its lightness is non-monotonic, so it invents
   reflectors. See [06](./06-colormaps-perception.md).
3. **An unstated clip level.** Every apparent amplitude ratio is then a property
   of the display.
4. **An asymmetric clip with a diverging palette.** The neutral colour is no
   longer zero, so the polarity reading is offset.
5. **No polarity statement.** The figure cannot be compared with another figure.
6. **Bilinear interpolation on a section being interpreted.** It invents
   continuity across trace gaps, which is where the real discontinuities are.
7. **Too many wiggles.** At 300 traces across 6.4 in, the wiggles overlap and the
   display is decorative.
8. **Treating a colour bar as optional.** Without it, the section has no
   amplitude axis at all.
9. **Confusing a time axis with a depth axis.** Two-way travel time in seconds is
   not depth without a velocity model, and the conversion must be stated.

## 11. Real-world applications

- **Interpretation workstations.** Industry software uses exactly these display
  controls, and the discipline of recording them is what makes an interpretation
  reproducible.
- **Publication of seismic sections.** Journals require the clip level, gain and
  polarity in the caption, because their referees cannot otherwise compare the
  figure with a published section from the same basin.
- **Amplitude-versus-offset analysis.** The display must be amplitude-preserving,
  which rules out AGC and forces a stated fixed or time-varying gain.
- **Subsurface imaging in teaching and outreach.** The same conventions make a
  teaching figure comparable with a research figure.
- **Monitoring and time-lapse.** Difference sections require a common, stated
  amplitude scale across epochs; otherwise a display change masquerades as a
  reservoir change.
- **Attribute displays.** Envelope, instantaneous phase and similarity are
  one-sided or cyclic quantities with their own palette families: sequential for
  the envelope, cyclic for phase (see
  [20-02-05 Time-Frequency Analysis: STFT, Wavelets, Spectrograms](../../20-signal-processing/02-fourier-and-spectral-analysis/05-time-frequency.md)).

## 12. Further reading

- **Yilmaz, Ö. *Seismic Data Analysis* (Society of Exploration Geophysicists).**
  The standard reference for display conventions, gain and amplitude treatment.
  Level: intermediate to advanced.
- **Sheriff, R. E., & Geldart, L. P. *Exploration Seismology* (2nd ed., Cambridge
  University Press).** The reflection coefficient, polarity conventions and
  section displays in their physical setting. Level: intermediate.
- **Brown, A. R. *Interpretation of Three-Dimensional Seismic Data* (7th ed.,
  SEG/AAPG).** How displays are used in interpretation practice, including colour
  and clipping choices. Level: intermediate.
- **Simm, R., & Bacon, M. *Seismic Amplitude: An Interpreter's Handbook*
  (Cambridge University Press, 2014).** What amplitude means and how display
  choices interfere with reading it. Level: intermediate to advanced.
- **Bacon, M., Simm, R., & Redshaw, T. *3-D Seismic Interpretation* (Cambridge
  University Press).** Practical displays and their conventions. Level:
  intermediate.
- **ObsPy documentation, <https://docs.obspy.org>** — waveform handling and the
  plotting conventions used in observational seismology, which differ from
  exploration practice and are worth comparing.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [06 Colour Perception, Sequential vs Diverging Colormaps](./06-colormaps-perception.md)
  — why the palette for a signed amplitude is diverging, measured.
- [03 Maps, Cross-Sections and Geological Symbology](./03-maps-and-cross-sections.md)
  — the sections a 3-D volume is cut into, and their time-versus-depth axis.
- [04 3-D Plots, Surfaces and Voxel Rendering](./04-3d-and-surfaces.md) — what a
  volume display adds and hides.
- [06-01-04 Reflected, Refracted and Converted Body Waves](../../06-seismology/01-elastic-wave-propagation/04-body-wave-arrivals.md)
  — the physics of the wavelet being displayed.
- [20-02-05 Time-Frequency Analysis: STFT, Wavelets, Spectrograms](../../20-signal-processing/02-fourier-and-spectral-analysis/05-time-frequency.md)
  — attributes with their own palette requirements.

Exercises:
[`exercises/05-seismic-displays-exercises.md`](./exercises/05-seismic-displays-exercises.md)
and
[`exercises/05-seismic-displays-solutions.md`](./exercises/05-seismic-displays-solutions.md).

## Self-assessment checklist

- [ ] I can draw a wiggle display with the conventional fill and compute the trace
      spacing in millimetres. (§2)
- [ ] I can state the difference between fixed gain, time-varying gain and AGC in
      terms of what physical amplitude information survives. (§2.1)
- [ ] I can explain from the physics why a seismic palette must be diverging and
      symmetric about zero. (§3, §5)
- [ ] I can choose a clip level, measure the fraction of saturated samples, and
      state the clip in the caption. (§3)
- [ ] I can state the polarity convention on a figure and demonstrate why omitting
      it makes the figure unusable for interpretation. (§4)
- [ ] I can decide between a wiggle, a variable-density and a combined display
      from the trace density and the question being asked. (§2, §6)
- [ ] I can list the display parameters a caption must record. (§2.1, §3, §4, §8)
