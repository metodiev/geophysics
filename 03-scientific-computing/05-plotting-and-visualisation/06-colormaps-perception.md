---
id: 03-05-06
title: "Colour Perception, Sequential vs Diverging Colormaps"
level: intermediate
prereqs: ["03-05-01", "03-05-02", "02-01-02"]
estimated_minutes: 75
tags: [colour, colormaps, perception, accessibility, colour-vision]
---

# Colour Perception, Sequential vs Diverging Colormaps

A colormap is a function from a number to a colour. Like any function, it can be
injective, monotonic or neither, and the reader's ability to recover the number
from the colour depends entirely on which. This lesson replaces the folk rule
"rainbow maps are bad" with measurements: for each candidate palette it computes
the perceptual lightness of the rendered colour as a function of the data value,
counts the number of times the lightness changes direction, measures the steepest
lightness step relative to the typical one, and counts how far apart in data space
two values are that render with the same lightness.

Every one of those quantities answers a specific question a reader will ask, and
every one of them can be computed in a few lines.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** colour as a three-dimensional perceptual quantity — lightness,
   chroma and hue — and explain why lightness carries the ordering.
2. **Convert** sRGB to CIE L\*a\*b\* and compute the lightness profile of any
   colormap.
3. **Measure** a palette's lightness reversals, its steepest lightness step
   relative to its typical one, and its grayscale ambiguity width.
4. **Classify** data as sequential, diverging or cyclic, and select a palette from
   the class rather than from habit.
5. **Demonstrate** that a rainbow palette creates false boundaries on a smooth,
   synthetic ramp and that a sequential palette does not.
6. **Centre** a diverging palette on the value that the physics privileges, and
   explain what goes wrong when the centre is set to the data mean instead.

## Prerequisites

- [01 Matplotlib Figure/Axes Model and Anatomy of a Plot](./01-matplotlib-basics.md)
  — how to attach a colour bar and set `vmin`/`vmax`.
- [02 Line, Scatter and Error-Bar Plots with Correct Uncertainty](./02-line-scatter-plots.md)
  — encoding a third variable and the cost of doing so.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — why "no anomaly" is a meaningful value that the display must be able to show.

## 1. Colour as a perceptual quantity

Physically, a colour displayed on a screen is a triple of sRGB coordinates. That
triple is not a good model of what a viewer sees, for two reasons: the mapping
from sRGB to perceived intensity is nonlinear (the sRGB transfer function is
approximately a power law with exponent 2.4), and perceived colour has three
roughly independent dimensions rather than three additive primaries.

The dimensions that matter for data display are:

- **Lightness** — how bright the colour is. The eye extracts this fastest and most
  reliably, and it is the channel that carries *ordering*.
- **Chroma (saturation)** — how far the colour is from grey.
- **Hue** — where the colour sits on the red–green–blue–yellow circle. The eye is
  good at *categorical* discrimination of hue and poor at quantitative reading of
  it: "this is bluer than that" is easy, "this is 0.3 units bluer" is not.

The CIE 1976 lightness $L^*$ is constructed so that equal increments correspond
roughly to equal perceived differences, which is what makes it the right quantity
for auditing a colormap. The demonstration computes it with the standard
published transform: sRGB to linear RGB by the sRGB transfer function, linear RGB
to CIE XYZ by the sRGB matrix, then

$$L^* = 116\,f(Y/Y_n) - 16, \qquad
  f(t) = \begin{cases} t^{1/3} & t > (6/29)^3 \\ (t\kappa + 16)/116 & \text{otherwise,} \end{cases}$$

with $\kappa = 24389/27$ and $Y_n = 1$ for the D65 white point. The nonlinearity
in $f$ is exactly why $L^*$ and the raw green channel disagree: a colormap can
look "evenly spaced" in RGB and be visibly banded in perception.

## 2. Three classes of data, three classes of palette

| Data class | Structure | Palette class | Property required |
|---|---|---|---|
| magnitude, density, depth, phase-free intensity | a single direction of increase from a natural zero | **sequential** | lightness monotonic in the data |
| residual, anomaly, signed difference, reflection coefficient | two directions from a privileged centre | **diverging** | lightness monotonic on each side of the centre, and equal at equal distance from it |
| phase, azimuth, direction of a cyclic quantity | a circle with no natural zero | **cyclic** | the two ends identical |

The classification is a property of the data, not of the discipline. A gravity
anomaly is diverging because "zero anomaly" is a physically meaningful absence of
signal; a gravity *gradient magnitude* is sequential because there is no negative
magnitude. Getting this backwards produces the two classic failures: a sequential
palette on signed data makes the sign unreadable, and a diverging palette on
unsigned data invents a centre that does not exist.

## 3. Measured palette properties

The demonstration audits nine colormaps. Its output:

```text
  colormap  family                                         L* span  rev  max/med
  viridis   sequential (perceptually uniform)                 75.9    0     1.19
  cividis   sequential, colour-vision-deficiency optimised    77.3    0     1.34
  Greys     sequential, monochrome                           100.0    0     1.60
  magma     sequential (perceptually uniform)                 97.7    0     1.30
  jet       rainbow (legacy default)                          83.0    5     1.69
  turbo     rainbow (smoother legacy default)                 78.9    1     2.36
  hsv       cyclic / hue-only                                 63.9    5     5.64
  RdBu_r    diverging                                         77.1    1     1.53
  seismic   diverging                                         94.7    1     2.84
```

The three columns answer three different questions.

**`L* span`** — how much lightness the palette has available. `Greys` uses the
whole range (100.0), `viridis` 75.9, `hsv` only 63.9. A palette with a small span
has less room to encode value in the channel the eye reads best.

**`rev`** — the number of times the lightness changes direction as the data value
increases. This is the decisive number. Zero means lightness is a faithful proxy
for value; five means there are five places where increasing the data makes the
render *darker*, so a smooth gradient of data renders with visible edges. `viridis`,
`cividis`, `Greys` and `magma` all score 0. `jet` and `hsv` each score 5 and
`turbo` 1.

Note carefully that `RdBu_r` and `seismic` also score 1, and that reversal is
**not a defect**: a diverging palette is defined by lightness peaking in the
middle, because its job is to make the centre conspicuous. The reversal count must
therefore be read together with the data class, not in isolation.

**`max/med`** — the steepest lightness step divided by the typical one. `viridis`
runs smoothly (1.19); `hsv` accelerates by a factor of 5.64 somewhere along the
ramp. Wherever the palette runs faster through lightness than the data run through
value, an isopleth of constant data acquires a brightness halo.

## 4. Where the false boundaries are

The demonstration locates the steepest lightness step in each ramp and reports the
colour there:

```text
  viridis  steepest step at data fraction 0.000: |dL*| = 0.346 against a median of 0.291
           so the map runs 1.19 times faster through lightness there than it typically does;
           colour at that step: sRGB (68, 1, 84)
  jet      steepest step at data fraction 0.333: |dL*| = 1.162 against a median of 0.688
           so the map runs 1.69 times faster through lightness there than it typically does;
           colour at that step: sRGB (0, 212, 255)
  turbo    steepest step at data fraction 0.004: |dL*| = 1.386 against a median of 0.586
           so the map runs 2.36 times faster through lightness there than it typically does;
           colour at that step: sRGB (50, 21, 67)
  hsv      steepest step at data fraction 0.529: |dL*| = 1.716 against a median of 0.304
           so the map runs 5.64 times faster through lightness there than it typically does;
           colour at that step: sRGB (0, 223, 255)
```

The `jet` step sits at data fraction 0.333, in the blue-to-cyan transition, using
sRGB (0, 212, 255). Reaching that hue requires the lightness to climb unusually
fast. The result is visible in `06_lightness.png`, which stacks the rendered ramp
above the measured $L^*$ curve for `viridis` and `jet`: the `viridis` curve is a
nearly straight line, and the `jet` curve has a kink and a local maximum. A reader
looking at the `jet` strip sees a bright band at the kink and infers a contour in
the data. There is no contour. The data are a linear ramp.

This is what "a rainbow colormap creates false boundaries" means, quantitatively:
the rendered lightness is non-monotonic in the data, so its extrema are features
of the palette that the reader attributes to the field.

## 5. Grayscale collapse

Colour is not always available: a figure is printed in black and white, or read by
a viewer who cannot separate two hues. Then the figure is its own lightness map,
and two data values that render with the same lightness become indistinguishable.
The measure of the damage is how far apart in data space those values are:

```text
  colormap    widest shared L* bin  bins spanning >10 %
  viridis                     1.2 %                    0
  cividis                     1.2 %                    0
  Greys                       2.0 %                    0
  jet                        93.3 %                   62
  turbo                      96.5 %                   64
  hsv                       100.0 %                   34
```

For a monotone palette every shared lightness bin holds *consecutive* data values,
so the widest bin spans a per cent or two of the range — that is ordinary
quantisation. For `jet`, one lightness bin is shared by data values 93.3 % of the
range apart: the far red and the far blue of the rainbow have nearly the same
brightness. A monochrome reader therefore sees the two ends of the scale as the
same tone, and the figure asserts that two very different values are equal.

`cividis` is the sequential member of this family designed for colour-vision
deficiency, and its 1.2 % ambiguity width is the reason: it keeps lightness
monotonic and varies hue only along an axis that survives the common forms of
colour blindness.

## 6. Centring a diverging palette

A diverging palette puts its neutral colour — usually white or a near-grey — at one
value. That value should be the one the physics privileges, and the demonstration
shows what happens when it is not:

```text
  field statistics: min -21.931, max +29.549, mean -0.332 mGal
  With vmin/vmax set to the data range (-21.931, +29.549), the
  neutral colour of a diverging palette sits at the MIDRANGE
  +3.809 mGal -- not at zero, and not at the mean either.
```

`06_sequential_vs_diverging.png` draws the same synthetic residual field four ways.
The two upper panels use a sequential and then a rainbow palette with auto-
scaled limits; in both, zero anomaly receives a mid colour, so a region of no
signal is rendered as strongly as a real anomaly and the sign cannot be read at
all. The two lower panels use `RdBu_r`, once with `vmin`/`vmax` symmetric about
zero, and once with limits set to the data range. Only the first puts white at
zero. The second puts its neutral colour at the *midrange* of the data,
$+3.809$ mGal, so a $3.809$ mGal anomaly is drawn as "no anomaly" — a larger error
than the field's own mean of $-0.332$ mGal, and a different number from it. The
general point is that neither the mean nor the midrange is zero, and only zero is
the value the physics privileges. It is also exactly the kind of error that makes
two figures from the same survey non-comparable, because the offset depends on
which subset each figure happened to contain.

The rule: **for a diverging quantity, set the limits to $\pm\max|a|$ (or to a
stated physical bound), never to the data minimum and maximum.** A symmetric
scale is what makes the neutral colour mean zero.

## 7. Cyclic quantities

Phase, azimuth and any angle are circular: 0 and $2\pi$ are the same value. A
sequential palette gives the two ends different colours, so the wrap at the period
boundary appears as a discontinuity in the field. The demonstration measures the
distance between the two ends in sRGB:

```text
  viridis: sRGB distance between the two ends = 1.1722
  hsv    : sRGB distance between the two ends = 0.0938
```

`viridis` puts the ends 1.1722 apart, about 68 % of the 1.732 that separates
opposite corners of the RGB cube — a strong, entirely fictitious edge. A cyclic
palette (`hsv`, `twilight`, `twilight_shifted`) closes the loop to 0.0938, thirteen
times smaller, and the seam
carries almost no information. `06_cyclic.png` draws one period of a phase field
under all three; the `viridis` panel shows a hard boundary where the phase wraps,
and the cyclic panels do not.

The choice is not aesthetic. It is the statement that the data have the topology of
a circle, which they do.

## 8. Worked code

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colormaps

def srgb_to_Lstar(rgb):
    c = np.asarray(rgb, dtype=float)
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    Y = 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]
    eps, kappa = 216.0 / 24389.0, 24389.0 / 27.0
    f = np.where(Y > eps, np.cbrt(Y), (kappa * Y + 16.0) / 116.0)
    return 116.0 * f - 16.0

v = np.linspace(0.0, 1.0, 256)
cmap = colormaps["viridis"]
L = srgb_to_Lstar(np.asarray([cmap(t)[:3] for t in v]))
dL = np.diff(L)
print("reversals:", int(np.sum(np.diff(np.sign(dL)) != 0)))
print("max/median |dL|:", float(abs(dL).max() / np.median(abs(dL))))
```

Twelve lines produce the two numbers that decide whether a palette is fit for
sequential data. The same audit should be run on any custom palette before it is
used in a figure.

## 9. Physical interpretation

Colour is a display channel, not a physical quantity, but a reader recovers physics
from it — and the recovery is only valid when the palette preserves the structure
of the physical quantity. Three structures occur repeatedly in the Earth sciences,
and each imposes a requirement that is measurable:

- **Order.** A magnitude, a depth, a density: larger must be brighter, or at least
  never darker. This is the requirement that `jet` violates five times, and each
  violation is a place where the figure asserts a boundary in a field that has
  none. On a depth-to-basement map a false edge reads as a fault or a basin margin,
  which is a structural claim, not a rendering artefact.
- **Sign about a physical zero.** A residual anomaly, a reflection coefficient, a
  definite integral: the neutral colour must sit at zero, because zero is the value
  that means "nothing there". A reader who sees a neutral-toned region concludes
  that no anomaly exists; if the palette's centre is the midrange, that conclusion
  is wrong by 3.809 mGal in the demonstration's field — a real anomaly rendered as
  absence of signal.
- **Periodicity.** Phase, azimuth, an angle: the two ends of the scale are the same
  physical value, and only a cyclic palette implements that identity. A sequential
  palette on wrapped phase puts a fabricated discontinuity at every wrap, and in an
  interferogram a fabricated discontinuity is indistinguishable from a real one.

The common thread is that the figure's encoding must be an isomorphism onto the
structure of the physics — order, sign or periodicity. When it is not, the reader
supplies a physical interpretation that the data do not contain.

## 10. Assumptions and limits

- **$L^*$ is one axis of three.** A palette can be monotonic in lightness and still
  be a poor choice if its chroma or hue excursions are wild; the audit here is
  necessary, not sufficient.
- **The `max/med` ratio is a local diagnostic.** It finds the worst step; a
  palette could be smooth everywhere except at an unnoticeable place. Read it with
  the reversal count and the render.
- **Grayscale ambiguity is measured on quantised $L^*$.** The choice of 256 levels
  matches the display; the *comparison* between palettes is robust to it, the
  absolute number is not.
- **No colour-vision simulation is performed here.** The lesson reports lightness
  behaviour, which is the axis that survives all common forms of colour blindness,
  and the palette named for that purpose (`cividis`). It does not model a specific
  deficiency, because such a model would need a citation and a verification this
  module does not carry. The measurable claim is the one made: a palette whose
  members differ in lightness survives monochrome.
- **Jet remains a legacy default.** Tools that predate perceptually uniform palettes
  still ship it, and many published figures still use it. The argument here is
  about what to do next, not about the past.
- **The palette does not fix a bad display.** A diverging palette on data with no
  meaningful zero, or a sequential palette on a signed residual, will mislead
  regardless of its perceptual properties.
- **Colour bars need units and end values.** A perceptually perfect palette with an
  unlabelled bar is still unreadable.

## 11. Python demonstration

[`code/06_colormaps_perception_demo.py`](./code/06_colormaps_perception_demo.py)
computes the CIE $L^*$ profile of nine colormaps, prints the metrics quoted in §3
and §5, writes `06_lightness.png` (150 dpi, ramp above its $L^*$ curve for
`viridis` and `jet`), `06_sequential_vs_diverging.png` (150 dpi, the same field
under four palette/limit combinations) and `06_cyclic.png` (150 dpi, one period of
phase under three palettes). Observed output is quoted in §3, §4, §5, §6 and §7.

### What to observe

| Observation | Consequence |
|---|---|
| `viridis`, `cividis`, `Greys`, `magma` score 0 reversals; `jet` and `hsv` score 5 | Lightness is monotonic in the data for the sequential family and not for the rainbow family |
| `hsv`'s steepest step is 5.64 times its median | A hue-only palette has no lightness budget to spend, so it spends it in one place |
| `jet`'s widest shared lightness bin spans 93.3 % of the range | Two very different values render as the same tone in monochrome |
| The four-panel field shows white at zero in only one panel | The neutral colour position is a choice, and only a symmetric limit makes it zero |
| `viridis`'s two ends are 1.1722 apart in sRGB | A sequential palette on a cyclic quantity manufactures a discontinuity |

> **Breaking exercise.** Audit `twilight` and `twilight_shifted` with the same
> twelve lines. Predict first (i) their reversal counts, (ii) whether their two
> ends agree in sRGB, and (iii) whether they would be acceptable for the linear
> ramp of §4. Then explain why a palette can legitimately fail the linear-ramp test
> and pass the cyclic test.

## 12. Common mistakes

1. **Rainbow for continuous data.** Non-monotonic lightness creates false
   boundaries; measured here at five reversals for `jet`.
2. **A sequential palette on a signed quantity.** Zero anomaly becomes a strong
   colour and the sign is lost.
3. **A diverging palette with limits set to the data range.** The neutral colour
   leaves zero by the mean of the data.
4. **A sequential palette on phase.** The wrap becomes a fictitious edge.
5. **Assuming a "perceptually uniform" name means suitable.** `viridis` is
   excellent for sequential data and wrong for cyclic data.
6. **Ignoring the grayscale path.** A figure with no lightness ordering is
   unreadable in print.
7. **Using colour alone to distinguish categories.** Add marker shape or line
   style; measured in
   [07 Publication-Quality Figures, Fonts, DPI and Accessibility](./07-publication-figures.md)
   as the lightness gap inside a palette.
8. **An unlabelled colour bar.** The palette is meaningless without the mapping.
9. **Reversing a palette by accident.** `RdBu` and `RdBu_r` are different figures;
   the direction must be stated, as it must for seismic polarity.

## 13. Real-world applications

- **Gravity and magnetic anomaly maps.** Diverging palettes centred on zero; the
  residual, not the total field, is the signed quantity.
- **Bouguer anomaly over a basin.** The depth-to-basement result is sequential;
  the residual used to get there is diverging. One survey, two palettes, two
  different data classes.
- **Topography and bathymetry.** Sequential, with a land–sea boundary drawn as a
  contour at zero elevation; a diverging palette with the centre at sea level is
  the alternative and is equally defensible if the centre is stated.
- **Seismic amplitude and attributes.** Diverging for signed amplitude (see
  [05](./05-seismic-displays.md)), sequential for the envelope, cyclic for
  instantaneous phase.
- **Interferometric phase and InSAR.** Cyclic palettes are mandatory; a sequential
  palette on a wrapped phase field creates fringes that do not exist.
- **Satellite imagery and indices.** Sequential for NDVI-like indices with a
  natural zero and one direction; the palette and its limits belong in the caption
  so the index can be recomputed.

## 14. Further reading

- **Borland, D., & Taylor, R. M. (2007). "Rainbow color map (still) considered
  harmful." *IEEE Computer Graphics and Applications* 27(2), 14–17.** The short
  paper that made the case to a wide audience. Level: beginner.
- **Ware, C. *Information Visualization: Perception for Design* (3rd ed., Morgan
  Kaufmann).** The perceptual basis for lightness, hue and the ordering
  argument. Level: intermediate.
- **Kovesi, P. (2015). "Good colour maps: How to design them." arXiv:1509.03700.**
  Construction of perceptually uniform and cyclic maps. Level: intermediate.
- **Crameri, F., Shephard, G. E., & Heron, P. J. (2020). "The misuse of colour in
  science communication." *Nature Communications* 11, 5444.** A review of palette
  misuses across the geosciences, with examples. Level: intermediate.
- **Munzner, T. *Visualization Analysis and Design* (CRC Press).** Encoding
  channels and their suitability, treated systematically. Level: intermediate.
- **CIE 1976 colour-space publications and the CIE's own documentation** — the
  authority for the $L^*a^*b^*$ transform used here; consult the CIE for the
  definitive formulae and the current edition of the standard.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [05 Seismic Displays: Wiggle, Variable-Density and Colormaps](./05-seismic-displays.md)
  — the dataset where the diverging argument is most acute.
- [07 Publication-Quality Figures, Fonts, DPI and Accessibility](./07-publication-figures.md)
  — palettes and accessibility in a submission context.
- [08 Interactive Exploration: Plotly and HoloViews](./08-interactive-viz.md) — what
  a reader can do about a palette when they can change it themselves.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../../17-remote-sensing-gis/01-remote-sensing-physics/04-resolution-concepts.md)
  — the raster data that colour ramps usually display.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md)
  — where the percentiles that set a clip level come from.

Exercises:
[`exercises/06-colormaps-perception-exercises.md`](./exercises/06-colormaps-perception-exercises.md)
and
[`exercises/06-colormaps-perception-solutions.md`](./exercises/06-colormaps-perception-solutions.md).

## Self-assessment checklist

- [ ] I can name the three perceptual dimensions of colour and say which one
      carries ordering. (§1)
- [ ] I can convert sRGB to $L^*$ and compute a palette's lightness profile. (§1,
      §8)
- [ ] I can measure a palette's reversals, its steepest relative lightness step
      and its grayscale ambiguity width. (§3, §5)
- [ ] I can classify a dataset as sequential, diverging or cyclic and choose the
      palette family from the class. (§2)
- [ ] I can demonstrate false boundaries on a smooth ramp under a rainbow palette
      and explain the mechanism. (§4)
- [ ] I can centre a diverging palette on the value the physics privileges and
      explain what setting the limits to the data range does instead. (§6)
- [ ] I can decide from the data's topology whether a cyclic palette is required.
      (§7)
