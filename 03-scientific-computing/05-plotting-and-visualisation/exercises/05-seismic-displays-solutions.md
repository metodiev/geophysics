# Solutions — 03-05-05 Seismic Displays: Wiggle, Variable-Density and Colormaps

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — Clip levels in decibels

**(a)** $20\log_{10}(1.55/0.70) = 6.90$ dB. In amplitude terms the ratio is
$1.55/0.70 = 2.214$.

**(b)** $20\log_{10}(0.3875/0.70) = -5.14$ dB, i.e. the tight clip is a factor
$0.5536$ of the p99 amplitude.

**(c)** Every reflector renders with 6.90 dB less colour contrast than the
conventional clip would give it: an event twice as strong as another still looks
twice as strong, but both are compressed toward the neutral colour, so weak events
approach the background and the fine structure becomes invisible.

---

## ★2 — Intervals from a standard deviation

**(a)** $1\sigma = 0.40$ mGal; $2\sigma = 0.80$ mGal; $3\sigma = 1.20$ mGal.

**(b)** $1.645 \times 0.40 = 0.658$ mGal.

**(c)** A detection threshold is normally set at a stated multiple of $\sigma$ —
commonly 3σ or 5σ depending on the false-positive rate that can be tolerated — so
the threshold inherits the coverage of the quoted $\sigma$. Without the coverage
statement the threshold is unpinned: a "0.4 mGal detection threshold" could mean
$1\sigma$ (32 % false-positive rate for a single test) or $3\sigma$ (0.3 %), which
are very different claims about the data.

---

## ★3 — Wiggle spacing

**(a)** $6.4\ \text{in} \times 25.4 = 162.56$ mm and $460.8$ pt:

| traces | spacing (mm) | spacing (pt) |
|---|---|---|
| 60 | 2.709 | 7.68 |
| 120 | 1.355 | 3.84 |
| 300 | 0.542 | 1.54 |

**(b)** Adjacent traces overlap. The eye can no longer attribute a large excursion
to one trace, and a single strong event becomes indistinguishable from two weaker
ones on neighbouring traces — the classic loss of amplitude fidelity in a dense
wiggle display.

**(c)** At 300 traces. The 0.542 mm spacing is at the limit of what a printer or a
display can resolve, so the wiggle display adds no information that the raster
does not already carry; at 60 traces the wiggle is more informative than a raster
because it preserves both sign and amplitude with no clip.

---

## ★4 — Choices and consequences

| Choice | Consequence |
|---|---|
| 1. AGC | (b) absolute amplitude destroyed |
| 2. `interpolation="bilinear"` | (a) continuity invented between traces |
| 3. Rainbow palette on signed data | (e) sign of the reflection coefficient unreadable |
| 4. No clip level stated | (c) apparent amplitude ratios depend on the display |
| 5. Colour bar without units | (d) the section has no amplitude axis |

---

## ★5 — Running the demonstration

**(a)**

```text
  section: 420 samples x 120 traces, dt = 2 ms
  mean  = +0.000092   median = +0.000000
  std   = 0.147212
  samples with |a| exactly 0: 65.18 %  (the gaps between wavelets)
```

**(b)**

```text
          50.0          0.008555
          90.0          0.408570
          99.0          0.909507
          99.5          1.000000
  largest |a| in the whole section: 1.550000
```

**(c)**

```text
    trace spacing = 2.71 mm  (7.7 pt)
    scale factor applied: 0.58 per unit amplitude
```

**(d)**

```text
  clip level                   value   saturated %   clip / p99 (dB)
  0.25 x max (too tight)     0.38750         4.220             -5.14
  p99 (conventional)         0.70000         1.012              0.00
  max (too loose)            1.55000         0.002              6.90
```

**(e)**

```text
  data mean                = +0.000092
  symmetric clip about zero: [-1.5500, 1.5500]
  asym. percentile clip    : [-0.4653, 0.6648]
  relative asymmetry of the percentile clip: 17.65 %
```

---

## ★6 — Adding a clip at half the maximum

**(a)** $0.5 \times 1.55 = 0.775$.

**(b)** Smaller. The clip is larger, so fewer samples reach it; the saturated
fraction falls monotonically as the clip is raised. From the measured trend
(4.220 % at 0.3875, 1.012 % at 0.70, 0.002 % at 1.55) the value at 0.775 should
sit between 1.012 % and 0.002 %, and closer to the lower end because the
distribution is steeply decaying in the tail.

**(c)** Measured: 0.774 %, with a decibel offset of $+0.88$ dB from p99 — between
the two, as predicted.

**(d)** For lateral continuity of the strongest reflector, choose a clip *above*
that reflector's amplitude so it does not saturate. A clip at $0.5\,a_{\max} =
0.775$ saturates 0.774 % of samples, which is at the level of the strongest
reflectors, so the reflector of interest may still be clipped where it is
strongest. A clip at a percentile just above the reflector amplitude — or a stated
absolute clip — keeps it in range, and the caption must then report the saturated
fraction (which will be very small) and the clip value so the reader knows the
scale is not the data range.

---

## ★7 — Wavelet arithmetic

**(a)** Dominant period $= 1/28\ \text{Hz} = 35.71$ ms. At $dt = 2$ ms that is
$35.71/2 = 17.86$ samples per period.

**(b)** Nyquist $= 1/(2 \times 0.002) = 250$ Hz. The wavelet sits at
$28/250 = 11.2$ % of Nyquist.

**(c)** For 45 Hz: period 22.22 ms, 11.11 samples per period, and
$45/250 = 18$ % of Nyquist. A shorter wavelet occupies fewer samples per trace, so
the fraction of exactly-zero samples *increases*; and because a higher-frequency
wavelet produces sharper peaks from the same reflection coefficients, the
distribution of nonzero amplitudes becomes more concentrated, which puts the 99th
percentile closer to the maximum. The optimum clip therefore rises relative to the
maximum, and the useful clip range narrows.

**(d)** Polarity concerns the *sign* of the seismic response to a reflection
coefficient. Changing the wavelet frequency changes neither the sign of the
reflection coefficient nor the mapping from that sign to a colour; it changes only
the width of the response. The convention that must be printed is therefore
independent of the wavelet.

---

## ★8 — Reversing the palette

**(a)** Only the direction of the colour scale differs: with `RdBu_r` one sign of
amplitude is drawn blue and the other red; with `RdBu` the two are exchanged. The
data array is identical, the limits are identical, and every sample maps to the
complementary colour.

**(b)** The choice is a property of the acquisition and processing convention — the
"SEG normal"/"SEG reverse" polarity — not of the numbers. Nothing in the amplitude
array records whether a positive reflection coefficient was recorded as a peak or a
trough, so no inspection of the data can resolve it.

**(c)** "Positive amplitude is plotted as blue (SEG normal polarity); a positive
reflection coefficient therefore appears as a blue-to-white-to-red peak sequence."
The sentence must name both the colour that encodes positive amplitude and the
physical meaning of a positive amplitude.

---

## ★9 — An amplitude-versus-offset figure

**(a)** The specification, with the justification for each choice:

| Parameter | Choice | Justification |
|---|---|---|
| Gain | fixed, one scale for the whole section | the argument is that the reflector *brightens* downdip, which is a relative amplitude claim; AGC and time-varying gain both destroy part of that comparison |
| Palette | diverging, symmetric about zero, e.g. `RdBu_r` | the sign of the reflection coefficient carries the interface polarity, and the amplitude is a zero-mean oscillation |
| Interpolation | `"nearest"` | bilinear invents continuity across trace gaps, and trace-to-trace amplitude change is the measured quantity |
| Clip | stated, above the largest amplitude of the reflector of interest | saturation would flatten exactly the brightening being claimed |

**(b)** The gain and the clip would invalidate the argument if chosen differently:
AGC destroys absolute amplitude, and a clip below the reflector's peak removes the
brightening. The palette would not invalidate the *amplitude* claim but would
invert the *polarity* claim read from the same figure; the interpolation would
smear amplitudes between traces but not invert them.

**(c)** The caption must record: the gain convention and, if time-varying, its
form; the clip value and the saturated percentage; the palette's polarity
convention (which colour is positive amplitude); the interpolation; the units of
the amplitude; and the processing sequence that produced the amplitudes.

---

## ★10 — Time to depth

**(a)** A two-way time of 1.00 s is $0.500$ s one-way. At 2.0 km/s,
$z = 0.500 \times 2.0 = 1.00$ km.

**(b)** At 2.5 km/s, 1.25 km; at 3.0 km/s, 1.50 km. The range for an unknown
velocity between those bounds is 1.00–1.50 km, i.e. a factor of 1.5, or 50 %.

**(c)** Labelling the axis "depth (km)" while plotting travel time asserts a
velocity, and it asserts a *constant* one. The error is therefore not a uniform
scale factor: it grows with depth as the velocity structure diverges from the
assumed value, so shallow events are placed almost correctly and deep events can be
displaced by tens of per cent. Worse, the implied velocity is invisible: two
interpreters reading the same figure at different depths will infer inconsistent
depths, and no caption statement about the axis can recover the information unless
the velocity model is stated.
